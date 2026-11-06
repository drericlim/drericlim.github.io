/**
 * drericlim.com: nightly Google Drive copies of the approved pages.
 *
 * Runs inside Professor Lim's own Google account (script.google.com), once a
 * night between 11pm and midnight UK time. For each page listed in
 * tools/drive-backup/pages.json it:
 *   1. reads the page's approved version from the version register in README.md
 *      (drafts, v0.x, are never saved);
 *   2. fetches the page from GitHub at the latest commit and swaps the robots tag
 *      from "noindex, nofollow" to "index, follow";
 *   3. if the result differs from the newest Drive copy, saves it as
 *      YYYYMMDD-<name>.html, checks its size (repository file minus 4 bytes),
 *      and only then renames the old copy <old name>-v<version>-superseded.html.
 *      A second change on the same day updates that day's copy instead.
 * It emails Professor Lim only when something was saved or went wrong.
 *
 * Set-up (once): paste this file into a new Apps Script project, choose
 * setUp in the toolbar, press Run and allow access. See README.md in this folder.
 * The master copy of this script is tools/drive-backup/Code.gs in GitHub.
 */

var CONFIG = {
  repo: 'drericlim/drericlim.github.io',
  branch: 'main',
  folderId: '1d-suhHutQ2Nndfd-cHDlm_kAuBiztmFl',
  pagesFile: 'tools/drive-backup/pages.json',
  registerFile: 'README.md',
  timeZone: 'Europe/London',
  runAtHour: 23,
  email: 'changes' // 'changes' (only when something was saved or failed), 'always' or 'never'
};

var ROBOTS_REPO = '<meta name="robots" content="noindex, nofollow">';
var ROBOTS_DRIVE = '<meta name="robots" content="index, follow">';

/** Run once by hand: creates the nightly schedule and does a first run now. */
function setUp() {
  ScriptApp.getProjectTriggers().forEach(function (t) {
    if (t.getHandlerFunction() === 'saveApprovedPagesToDrive') ScriptApp.deleteTrigger(t);
  });
  ScriptApp.newTrigger('saveApprovedPagesToDrive')
    .timeBased().everyDays(1).atHour(CONFIG.runAtHour).inTimezone(CONFIG.timeZone)
    .create();
  return saveApprovedPagesToDrive();
}

/** The nightly job. Can also be run by hand at any time. */
function saveApprovedPagesToDrive() {
  var report = { saved: [], unchanged: [], skipped: [], warnings: [], errors: [] };
  var sha = '';
  try {
    sha = latestCommit_();
    var pages = JSON.parse(fetchFile_(sha, CONFIG.pagesFile).text);
    var versions = readRegister_(fetchFile_(sha, CONFIG.registerFile).text);
    var folder = DriveApp.getFolderById(CONFIG.folderId);
    var today = Utilities.formatDate(new Date(), CONFIG.timeZone, 'yyyyMMdd');
    pages.forEach(function (page) {
      try {
        savePage_(page, versions, folder, sha, today, report);
      } catch (e) {
        report.errors.push(page.name + ': ' + e.message);
      }
    });
  } catch (e) {
    report.errors.push(e.message);
  }
  console.log(JSON.stringify(report, null, 2));
  sendReport_(report, sha);
  return report;
}

function savePage_(page, versions, folder, sha, today, report) {
  var version = versions[page.file];
  if (!version) throw new Error(page.file + ' is not in the version register in README.md, so nothing was saved.');
  if (!/^v[1-9]/.test(version)) {
    report.skipped.push(page.name + ' (' + version + ' is a draft)');
    return;
  }

  var source = fetchFile_(sha, page.file);
  var text = toDriveCopy_(source.text, page);
  var bytes = byteLength_(text);
  var expected = source.text.indexOf(ROBOTS_REPO) >= 0 ? source.bytes - 4 : source.bytes;
  if (bytes !== expected) throw new Error('size check failed before saving (' + bytes + ' bytes, expected ' + expected + ').');

  var current = newestCopy_(folder, page.drive);
  if (current && current.file.getBlob().getDataAsString('UTF-8') === text) {
    report.unchanged.push(page.name + ' ' + version);
    return;
  }

  var currentVersion = current ? versionOf_(current.file) : '';
  if (current && currentVersion === version) {
    report.warnings.push(page.name + ' changed in GitHub but the register still says ' + version +
      '. Saved anyway; check the version number in README.md.');
  }
  var description = version + ' (GitHub ' + sha.substring(0, 7) + ')';

  if (current && current.date === today) {
    // A second change today: update today's copy rather than superseding it.
    current.file.setContent(text);
    checkSize_(current.file, expected, false);
    current.file.setDescription(description);
    report.saved.push(page.name + ' ' + version + ': updated today\'s copy ' + current.file.getName());
    return;
  }

  var name = today + '-' + page.drive + '.html';
  var blob = Utilities.newBlob('', 'text/html', name).setDataFromString(text, 'UTF-8');
  var created = folder.createFile(blob);
  checkSize_(created, expected, true);
  created.setDescription(description);

  var line = page.name + ' ' + version + ': saved ' + name;
  if (current) {
    var oldName = current.file.getName();
    var newOldName = oldName.replace(/\.html$/, (currentVersion ? '-' + currentVersion : '') + '-superseded.html');
    current.file.setName(newOldName);
    line += '; ' + oldName + ' renamed ' + newOldName;
    if (!currentVersion) report.warnings.push(oldName + ' had no version recorded, so its new name has no version number.');
  }
  report.saved.push(line);
}

/** Swaps the robots tag; refuses a page with neither tag. */
function toDriveCopy_(text, page) {
  var count = text.split(ROBOTS_REPO).length - 1;
  if (count === 1) return text.replace(ROBOTS_REPO, ROBOTS_DRIVE);
  if (count === 0 && text.indexOf(ROBOTS_DRIVE) >= 0) return text; // after launch
  throw new Error('found ' + count + ' copies of the robots tag in ' + page.file + '; expected exactly one.');
}

/** The newest current (not superseded) copy, e.g. 20261101-homepage.html. */
function newestCopy_(folder, stem) {
  var pattern = new RegExp('^(\\d{8})-' + stem.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '\\.html$');
  var files = folder.searchFiles('title contains "' + stem + '" and trashed = false');
  var best = null;
  while (files.hasNext()) {
    var f = files.next();
    var m = pattern.exec(f.getName());
    if (m && (!best || m[1] > best.date)) best = { file: f, date: m[1] };
  }
  return best;
}

function versionOf_(file) {
  var m = /\bv\d+(?:\.\d+)*/.exec(file.getDescription() || '');
  return m ? m[0] : '';
}

function checkSize_(file, expected, trashIfWrong) {
  var size = file.getSize();
  if (size !== expected) {
    if (trashIfWrong) file.setTrashed(true);
    throw new Error('size check failed after saving ' + file.getName() + ' (' + size + ' bytes, expected ' + expected +
      '). ' + (trashIfWrong ? 'The new copy was deleted and the old copy left as it was.' : ''));
  }
}

/** Reads README.md's version register: { 'index.html': 'v1.22', ... }. */
function readRegister_(markdown) {
  var lines = markdown.split('\n');
  var versionCol = -1, fileCol = -1, result = {};
  for (var i = 0; i < lines.length; i++) {
    var line = lines[i].trim();
    if (line.charAt(0) !== '|') { if (versionCol >= 0 && Object.keys(result).length) break; continue; }
    var cells = line.split('|').slice(1, -1).map(function (c) { return c.trim(); });
    if (versionCol < 0) {
      versionCol = cells.indexOf('Approved version');
      fileCol = cells.indexOf('File in this repository');
      if (versionCol < 0 || fileCol < 0) versionCol = fileCol = -1;
      continue;
    }
    var paths = cells[fileCol].match(/`[^`]+`/g) || [];
    paths.forEach(function (p) { result[p.slice(1, -1)] = cells[versionCol]; });
  }
  if (versionCol < 0) throw new Error('could not find the version register table in README.md.');
  return result;
}

/**
 * The latest commit on the branch. Read the way git itself does (info/refs),
 * not through api.github.com: the API allows only 60 anonymous requests an hour
 * per address, and Apps Script shares Google's addresses with everyone, so it
 * often answers 403.
 */
function latestCommit_() {
  var url = 'https://github.com/' + CONFIG.repo + '.git/info/refs?service=git-upload-pack';
  var r = UrlFetchApp.fetch(url, { muteHttpExceptions: true });
  if (r.getResponseCode() !== 200) throw new Error('could not reach GitHub (' + r.getResponseCode() + ').');
  var m = new RegExp('([0-9a-f]{40}) refs/heads/' + CONFIG.branch + '\\b').exec(r.getContentText());
  if (!m) throw new Error('could not find the ' + CONFIG.branch + ' branch on GitHub.');
  return m[1];
}

function fetchFile_(sha, path) {
  var url = 'https://raw.githubusercontent.com/' + CONFIG.repo + '/' + sha + '/' + path;
  var r = UrlFetchApp.fetch(url, { muteHttpExceptions: true });
  if (r.getResponseCode() !== 200) throw new Error('could not fetch ' + path + ' from GitHub (' + r.getResponseCode() + ').');
  var blob = r.getBlob();
  return { text: blob.getDataAsString('UTF-8'), bytes: blob.getBytes().length };
}

function byteLength_(text) {
  return Utilities.newBlob('').setDataFromString(text, 'UTF-8').getBytes().length;
}

function sendReport_(report, sha) {
  var problems = report.warnings.length + report.errors.length;
  if (CONFIG.email === 'never') return;
  if (CONFIG.email === 'changes' && !report.saved.length && !problems) return;
  var subject = 'drericlim.com Drive copies: ' +
    (report.errors.length ? 'problem, please check' :
      report.saved.length ? report.saved.length + ' page' + (report.saved.length > 1 ? 's' : '') + ' saved' : 'nothing changed');
  var section = function (title, items) { return items.length ? title + '\n- ' + items.join('\n- ') + '\n\n' : ''; };
  var body = section('Saved', report.saved) + section('Problems (nothing was changed for these)', report.errors) +
    section('Please check', report.warnings) + section('Unchanged', report.unchanged) + section('Not saved (drafts)', report.skipped) +
    'Drive folder: https://drive.google.com/drive/folders/' + CONFIG.folderId + '\n' +
    (sha ? 'GitHub version: https://github.com/' + CONFIG.repo + '/commit/' + sha + '\n' : '') +
    '\nSent by the nightly Drive-copy script in your Google account (tools/drive-backup in GitHub).';
  MailApp.sendEmail(Session.getEffectiveUser().getEmail(), subject, body);
}
