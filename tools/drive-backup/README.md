# Nightly Drive copies of the approved pages

Every night between 11pm and midnight (UK time), a small script in Professor Lim's own Google account saves a reference copy of each approved page to the Google Drive **Personal website** folder. Nobody needs to save pages to Drive by hand any more.

## What it does

For each page listed in `pages.json`:

1. It looks up the page's approved version in the **Version register** in `README.md`. Drafts (v0.x) are never saved.
2. It fetches the page from GitHub at the latest commit and changes the search-engine setting from `noindex, nofollow` to `index, follow`.
3. If that differs from the newest Drive copy, it saves `YYYYMMDD-<name>.html` (for example `20261106-hub-about.html`) and checks that its size is exactly the repository file's size minus 4 bytes. Only then does it rename the old copy, for example `20261101-hub-about-v1.13-superseded.html`. If the size is wrong, it deletes the new copy and leaves the old one as it was.
4. If a page changes twice in one day, that day's copy is updated rather than superseded.
5. It writes the version (and the GitHub commit) into each copy's Drive **description**. That is how it knows which version number to put in the name when the copy is superseded.

It emails Professor Lim only when something was saved or something went wrong. If nothing changed, there is no email.

## Files

| File | What it is |
|---|---|
| `Code.gs` | The script. This is the master copy; the copy in Google Apps Script is pasted from here. |
| `pages.json` | The pages to save, and the name each has in Drive. The script reads this file from GitHub every night, so adding a page here needs no change to the script. |
| `appsscript.json` | Optional settings file for the Apps Script project (UK time zone and the permissions it uses). |

To add a page once it is approved (for example Publications), add a line to `pages.json` with its file and Drive name, and make sure its row is in the README version register.

## Setting it up (once, about five minutes)

1. Signed in to Google as ekslim@gmail.com, go to **script.google.com** and click **New project**.
2. Click **Untitled project** at the top and rename it **drericlim.com nightly Drive copies**.
3. Open [`Code.gs` on GitHub](https://github.com/drericlim/drericlim.github.io/blob/main/tools/drive-backup/Code.gs) and click the **Copy raw file** button (two overlapping squares, top right of the file).
4. Back in Apps Script, select everything in the editor (Ctrl+A, or Cmd+A on a Mac), paste over it, and press Ctrl+S (Cmd+S) to save.
5. In the toolbar, choose **setUp** from the list of functions and click **Run**.
6. Google asks for permission. Click **Review permissions** and choose your account. It then says **"Google hasn't verified this app"**. This is normal for a script you wrote for yourself: click **Advanced**, then **Go to drericlim.com nightly Drive copies (unsafe)**, then **Allow**. The script can see your Drive (to save the copies), fetch pages from GitHub, send you an email, and run on a schedule.
7. The **Execution log** at the bottom shows the result. The first time, all six pages should be listed as **Unchanged**, because Drive already matches GitHub.
8. Click the clock icon (**Triggers**) on the left: there should be one trigger, `saveApprovedPagesToDrive`, daily, 11pm to midnight.

To run it at any other time, choose **saveApprovedPagesToDrive** and click **Run**.

## If the script is changed

The page list and the versions are read from GitHub every night, so most changes need nothing in Apps Script. If `Code.gs` itself changes, paste it in again (steps 3 and 4). Running **setUp** again is safe: it replaces the trigger rather than adding a second one.

## Testing

`Code.gs` was tested on 6 Nov 2026 with Google's services simulated, against the real pages and the real Drive file names. The cases covered were: nothing changed, a page changed with a new version, a second change on the same day, a change without a version bump (saved, with a warning), a draft (not saved), and a wrong file size (new copy deleted, old copy kept).
