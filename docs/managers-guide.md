# drericlim.com: guide for the practice team

*A living guide. It grows as the new website is built, and will be presented to the practice managers when the site is complete. Last updated 1 November 2026.*

---

## 1. The new website at a glance

- The new drericlim.com is being built to replace the current Squarespace site. Squarespace stays live until the new site is finished and approved.
- While it is being built, the new site can be seen at **https://drericlim.github.io/**. It is hidden from Google until launch.
- At launch, the drericlim.com address will be moved to the new site.

### The main pages

| Page | Address | What it is for |
|---|---|---|
| Home | `/` | First impression for patients, referrers and clinicians |
| For patients | `/for-patients` | Guides, articles and videos about conditions, operations and recovery |
| For professionals | `/for-professionals` | Research, statistics teaching and the Thoracic Reflections articles |
| virtual Grand Rounds | `/virtual-grand-rounds` | The teaching programme, upcoming talks and archive |
| About | `/about` | Professor Lim's story, career, where he practises and the team |
| Contact | `/contact-us` | The enquiry form, phone number and directions |

---

## 2. Where everything is kept

| What | Where | Who uses it |
|---|---|---|
| **The website itself** | GitHub: **github.com/drericlim/drericlim.github.io** (the website's *repository*: one online folder holding every page, photo and text file of the site) | This is the master copy. Every change is made here and appears on the site within a few minutes. |
| **Reference copies of approved pages** | Google Drive, "Personal website" folder | A dated copy of each approved page (e.g. `20261025-homepage.html`). Older copies are marked "-superseded". They are saved **automatically every night** by a small script in Professor Lim's Google account, so nobody needs to do this by hand. Professor Lim gets an email when pages are saved or if anything goes wrong. |
| **Testimonials** | GitHub: `_data/testimonials.yml` | Every patient testimonial on the site, newest first |
| **All photos and logos** | GitHub: `assets/`, one folder per kind (see section 6, and the full list in Appendix A) | Every picture on the website |
| **Version record** | GitHub: `README.md`, "Version register" | Which version of each page is current |

GitHub keeps every earlier version of every file, so nothing is ever lost. Any change can be seen or undone from a file's **History**.

---

## 3. What each team member needs

1. **A GitHub account**, added to the **drericlim** organisation on GitHub. Professor Lim (or whoever manages the organisation) sends the invitation.
2. **A Claude account**, with GitHub connected so Claude can save changes to the website.

Once both are set up, most updates can be made simply by asking Claude in plain English.

---

## 4. Making changes to the website

**The easy way: ask Claude.** In a Claude session with access to the website, describe the change, for example: "On the About page, change Michael's description to …". Claude makes the change, checks it, and saves it. It follows the house rules and design kept in the website's notes file (`CLAUDE.md`).

**House style.** Claude already knows these, but they are useful for the team too:

- Professor Lim practises only at the **Royal Brompton Hospital**, Sydney Street, London SW3 6NP. The telephone number is **+44 (0) 207 352 8121**. There is no fax.
- Private patients are **self-funding**; the practice does not work with insurers.
- NHS patients are referred through their own hospital's **multidisciplinary team**.
- Team members do not give out their own phone numbers; patients call the **office**.
- Always write **"virtual Grand Rounds"** with a small v.
- Describe results plainly, without boasting: for example, "Many patients now go home on the day of their operation."
- Photos have rounded corners. The design has no sticky menus and no pill-shaped buttons.

---

## 5. Adding a patient testimonial

All testimonials live in one file, **`_data/testimonials.yml`**. The Testimonials page and the rotating quotes on the homepage are both built from it, so a testimonial only ever needs adding once. Each testimonial has the patient's full words, plus a short extract of a sentence or two for the homepage. The homepage shows these one at a time, in a different random order on every visit, changing every seven seconds.

**Before you start:** make sure the patient has agreed **in writing** to their words being published with their name, and to their photo too if they sent one. The simplest record is the patient's reply to our standard request email (below): keep that thread on file.

### Asking a patient for a testimonial

When a patient thanks the practice, or asks how they can help, Maria sends the request below. It tells the patient everything they need to know, so their reply is their consent and no separate consent step is needed. Everything in square brackets is filled in.

```
Subject: Would you be happy to share your experience?

Dear [Mr Smith],

Thank you for your kind words about your care with Professor Lim and the team.
They mean a great deal to all of us.

Other patients often tell us that reading about someone else's experience helped
them when they were anxious before their own treatment. If you would be happy to,
we would be very grateful if you could send us a few words that we could share on
Professor Lim's website, drericlim.com. A sentence or two is plenty, or as much as
you would like to write. We publish testimonials exactly as written, in the
patient's own words.

So that you know what to expect:

- Your words would appear on the website with your name. We would show your full
  name unless you tell us you would prefer your first name only, or your initials.
- A short extract may also appear among the patient quotes on the homepage.
- If you would like to include a photograph of yourself, you are welcome to, but
  there is no need.
- You can ask us to change or remove it at any time, by emailing or calling the
  office.

Simply reply to this email with what you would like to say. If you would rather
not, please don't give it another thought; we are glad to have been able to help.

With warm wishes,

Maria Leung
Practice Manager, Professor Eric Lim
Royal Brompton Hospital
+44 (0) 207 352 8121
```

If the patient has already sent their testimonial without being asked, use the same email with the second paragraph replaced by: "Would you be happy for us to share the words you sent on [date] on Professor Lim's website, drericlim.com? We would publish them exactly as you wrote them." Their "yes" completes the record.

### Planned: forward the email, and the rest happens by itself (agreed 1 November 2026, not yet live)

This will become the normal way to add a testimonial. Until it is built and tested, use "The easy way: ask Claude" below.

1. When the patient's reply arrives, open it and click **Forward**.
2. Type two lines at the very top of the message:
   `Name: John Smith` (the name exactly as it should appear on the website)
   `Treatment: Day case lobectomy` (optional, a few words)
3. Send it to **ekslim+testimonials@gmail.com**. If the patient sent a photo, keep it attached.

That is all. Every day at 5pm, Claude reads anything sent to that address and, for each new email:

- keeps the patient's words **in full and exactly as written**, leaving out greetings, sign-offs, contact details and any private clinical detail;
- chooses the short extract for the homepage, **copied word for word** from the quote (never rewritten);
- resizes and files any photo;
- publishes the testimonial, and emails Maria a confirmation showing exactly what is now on the site, with a link. Reply to that email with any correction, or "please remove", and it is done the next day.

Nothing is published if anything is unclear. Instead Maria gets a one-line email asking, for example, how the name should appear. In particular:

- **Name:** the `Name:` line always wins. Without it, Claude uses the name the patient signed off with, then the sender's name on the email. If the email came from a relative or a shared address and the name is still unclear, Claude asks rather than guesses.
- **Consent:** the forwarded thread should contain our request email and the patient's reply. If it doesn't (for example an unprompted thank-you), Claude asks Maria to confirm consent before publishing.
- **Year:** taken from the date the patient wrote; nothing to add.

An example of what Maria sends:

```
To:      ekslim+testimonials@gmail.com
Subject: Fwd: Would you be happy to share your experience?

Name: John Smith
Treatment: Day case lobectomy

---------- Forwarded message ----------
From: John Smith <john.smith@example.com>
Date: Tue, 4 Nov 2026 at 09:12
Subject: Re: Would you be happy to share your experience?

Dear Maria,

Of course, I'd be delighted. Please use my full name.

From the first appointment Professor Lim explained everything clearly and never
once made me feel rushed. I went home the same day as my operation, which I would
not have believed possible, and Michael and Sarah checked on me by phone the
following morning. I cannot thank the whole team enough.

Best wishes,
John

> On 3 Nov 2026, Maria Leung wrote:
> Dear Mr Smith, ...
```

Anyone on the team can use the address, not only Maria. The address is an alias of Professor Lim's own email, filed automatically into a folder, so the confirmation emails come from his address.

**Testimonials sent as a card or letter.** Photograph or scan it (both sides of a card, if written on both) and email the pictures to the same address with a `Name:` line. Because a card is usually unprompted, add how the patient agreed: either forward their email saying yes along with the pictures, or add a line such as `Consent: by telephone, 5 November 2026, full name`. Claude types out the handwriting exactly as written and emails the typed version to Maria **the same evening to check against the card**; reply "yes" (or with corrections) and it is published the following evening. One email per patient, even when photographing several cards at once, so each email is a complete record for that person. The card itself is not shown on the website, only the words.

```
To:      ekslim+testimonials@gmail.com
Subject: Testimonial card from Margaret Jones

Name: Margaret Jones
Consent: by telephone, 5 November 2026. Happy for full name to be used.

[card-front.jpg, card-inside.jpg attached]
```

Still to decide before this goes live: whether email testimonials are published first and checked afterwards (as described above), or checked by Maria first like cards; and whether Professor Lim is copied on every confirmation or only on questions.

### The easy way: ask Claude

1. Open Claude with access to the website.
2. Paste the patient's email (or forward or attach it) and write: **"Please add this testimonial to drericlim.com."** Attach their photo too, if they sent one.
3. Claude asks you to confirm the patient has agreed to publication. It then shows you exactly how the testimonial will read. It uses the patient's own words, unedited, and leaves out greetings, signatures, contact details and private clinical details. It also picks a short extract (a sentence or two, still in the patient's own words) for the rotating quotes on the homepage.
4. Reply **"yes"**. Claude saves it, and the website updates within a few minutes.

Claude also has a saved skill called **add-drericlim-testimonial** for this. Ask Professor Lim to share it with your Claude account.

### By hand, if you prefer (about 5 minutes, in your web browser)

1. Go to **github.com/drericlim/drericlim.github.io** and sign in.
2. Open the folder **`_data`**, then the file **`testimonials.yml`**, and click the **pencil icon** (Edit this file).
3. Find the line `# ---------- NEWEST FIRST ----------` and paste a new entry directly under it:

```yaml
- name: "Jane Smith"
  year: 2026
  treatment: "Day case lobectomy"
  photo: ""
  homepage: yes
  short: "I was home the same day and back walking the dog within a week."
  quote: |
    I was home the same day and back walking the dog within a week.

    Thank you to Professor Lim, Maria and the whole team.

```

4. Click **Commit changes…**, write a short note such as "Add testimonial from Jane Smith", and click **Commit changes** again. The site updates within a couple of minutes.

| Line | What to put | Required? |
|---|---|---|
| `name` | The patient's name as they want it shown, in quotation marks | Yes |
| `year` | The year they sent it, e.g. `2026` | Yes |
| `treatment` | A few words about their operation, or `""` if unsure | No |
| `photo` | The photo's file name, e.g. `"jane-smith.jpg"`, or `""` | No |
| `homepage` | `yes` to include the patient in the homepage's rotating quotes (the more patients the better), otherwise `no` | Yes |
| `short` | For the homepage: one or two sentences copied exactly from the quote, in quotation marks. Use … where words are left out | When `homepage` is `yes` |
| `quote` | The patient's own words, on the lines below `quote: \|` | Yes |

Rules that keep the file working:

- Every line of an entry starts with two spaces, and every line of the quote with **four** spaces. Copying the example keeps this right.
- Leave a blank line between paragraphs, and one blank line after each entry.
- Use the patient's words exactly; don't correct their grammar or spelling unless they ask.

If a mistake breaks the file, the website simply keeps showing the last good version until it is fixed.

### Adding a photo by hand

1. Rename the photo with the patient's name in lower case and hyphens, e.g. `jane-smith.jpg`. It should be at least 800 pixels wide and under 500 KB.
2. On GitHub, open **`assets/testimonials`**, click **Add file → Upload files**, drag the photo in, and click **Commit changes**.
3. In `testimonials.yml`, set `photo: "jane-smith.jpg"` on that patient's entry.

### Editing or removing a testimonial

Ask Claude, or open `testimonials.yml` with the pencil icon, find the patient's name (Ctrl+F or Cmd+F), change or delete their whole entry, and commit.

### Feedback on the virtual Grand Rounds

The virtual Grand Rounds page has its own "In their own words" section, with comments from attendees and speakers. They are kept in `_data/vgr-feedback.yml`, one entry each: the quote word for word, the person's name, whether they were an attendee or a speaker, and the year. To add one, ask Claude ("Please add this vGR feedback to drericlim.com") or copy an existing entry, change it, and commit. Newest go at the top; the page shuffles them on each visit.

---

## 6. Photos and logos

Every picture on the website is kept in GitHub, in the **`assets`** folder, with one folder for each kind of picture:

| Folder | What goes in it | Example file name |
|---|---|---|
| `assets/images/` | Photos of Professor Lim and the hospital, used across the site | `eric-lim-portrait.jpg` |
| `assets/team/` | Team photos for the About page (shown in a circle) | `sarah-booth.jpg` |
| `assets/awards/` | Award pictures for the About page | `laingbuisson-innovation-in-care-2025.jpg` |
| `assets/books/` | Book covers for the About page | `integrated-textbook-of-medicine-and-surgery.jpg` |
| `assets/partners/` | Partner and sponsor logos for the virtual Grand Rounds page | `medtronic.svg` |
| `assets/speakers/` | virtual Grand Rounds speaker headshots | `jane-smith.jpg` |
| `assets/testimonials/` | Photos patients sent with their testimonials | `jane-smith.jpg` |
| `assets/articles/` | Pictures for patient guides, articles and Thoracic Reflections | `day-case-thoracic-surgery-ward.jpg` |

Each folder contains a short note listing what is in it, what is still needed, and the recommended size. GitHub shows that note below the list of files.

Appendix A at the end of this guide lists every folder and every file in it, and which page uses each one.

### Professor Lim's logo

The official logo is kept in `assets/icons/`, in two versions:

- **Dark version** (`logo-on-dark.svg`, or `logo-on-dark-1200.png` for Word, slides and emails): white and blue lungs, for dark or photo backgrounds.
- **Light version** (`logo-on-light.svg`, or `logo-on-light-1200.png`): navy and blue lungs, for white or pale backgrounds.

Always use these files rather than a screenshot or a copy from an email, so the logo looks the same everywhere. The small icon in browser tabs and on phone home screens is made from the light version, in a subtle pale circle; ask Claude to remake it if the logo ever changes.

### Naming photos

- Lower case, with hyphens instead of spaces, and no other punctuation: `sarah-booth.jpg`, not `Sarah Booth (1).JPG`.
- The name says what the picture is: a person's name, an award and year, a book title or a company name.

### Adding or replacing a photo

The pages already expect some photos by name. For example, the About page looks for `assets/team/sarah-booth.jpg` and shows Sarah's initials until it is there. To add or replace one of these:

1. On GitHub, open the right folder (e.g. `assets/team`).
2. Click **Add file → Upload files**, drag the photo in, and click **Commit changes**.
3. Make sure the file name matches **exactly** (rename it on your computer first). The photo appears on the site within a few minutes.

For a new photo that the pages don't yet expect, upload it to the right folder and ask Claude to place it on the page.

Keep photos under 500 KB where possible. Claude can resize a large photo if you ask.

---

### Rotating photos

Three spots on the site take turns showing a set of photos, so the site looks fresh for returning visitors:

| Spot | Folder |
|---|---|
| Homepage background photo | `assets/rotating/hero/` |
| Homepage About photo | `assets/rotating/home-profile/` |
| About page portrait | `assets/rotating/about-profile/` |

- **To add a photo to a rotation,** upload it into that folder. To take one out, delete it. Nothing else needs changing.
- **Photos take turns in file-name order,** so start each name with a number: `01-…`, `02-…`.
- **The photos change every Monday.** Every visitor sees the same photo that week. To change a spot to daily, open `_data/photo-rotation.yml`, change `weekly` to `daily` on that line, and commit.
- **Homepage background photos** must be wide (saved at 2400 by 1600 pixels), with Professor Lim on the **right**, because the headline sits on the left. Ask Claude to check and position them before they go in.
- **No repeats:** the homepage background, the homepage About photo and the About page portrait never show the same photo in the same week. This works because of the order of the photos, so the same photo keeps the same name in every folder (only the number differs). After adding, removing or renaming any rotating photo, ask Claude to run the photo check (`tools/check-photo-rotation.py`); it reports OK or tells you which photo would repeat.
- **The homepage About photo and the About page portrait share one set of photos,** so the two pages never show the same picture in the same week. Both folders hold the same photos, but the homepage is numbered one step ahead (the About page's `02` is the homepage's `01`, and the About page's `01` is the homepage's last). Add or remove a photo in **both** folders and keep this numbering, or simply ask Claude to do it.
- **About photos** (both of those spots) are upright 4:5, ideally 1200 by 1500 pixels, real photos only, with no colour effects.
- The picture shown when a page is shared on social media stays fixed on the main portrait (`assets/images/eric-lim-portrait.jpg`).
- Anyone else recognisable in a photo, patients especially, must have agreed to it being on the website.

---

### Films on the About page

The About page shows one film at a time beside the quote, taking turns weekly like the rotating photos. The films are listed in **`_data/about-films.yml`**:

```yaml
- vimeo: 231725351
  thumbnail: "vimeo-231725351.jpg"
  label: "Watch: my research on blood tests for cancer"
  title: "Professor Eric Lim on ctDNA research, blood tests for the early detection of cancer"
```

- `vimeo` is the number at the end of the film's Vimeo address (vimeo.com/**231725351**).
- `label` is the wording on the play button. `title` is a short description read out to visitors who use screen readers.
- **To preview a particular film** without waiting for its week, add `?film=` and its position in the list to the About page address, e.g. **drericlim.github.io/about/?film=2#film** for the second film.
- `thumbnail` is the cover picture shown behind the play button, kept in `assets/films/` (named `vimeo-` plus the film's number). Ask Claude to fetch it from Vimeo when adding a film.
- **To add a film,** copy a block, paste it at the end of the list, change the details and commit. Or simply give Claude the Vimeo link.
- **To remove one,** delete its block. Films take turns in the order listed.
- **In Vimeo, each film must be allowed to play on the website.** Open the film in Vimeo, go to **Settings → Privacy → "Where can this be embedded?"**, choose **Specific domains**, and add `drericlim.com`, `www.drericlim.com` and (while testing) `drericlim.github.io`. Otherwise the site shows a Vimeo message saying the video can't be played here.
- When a film finishes, the website puts the cover back automatically. In Vimeo, it's still worth setting each film's **End screen** to **Empty** (Share → Embed → End screen), so Vimeo never suggests other videos.
- To change how often the film changes, edit the `about-film` line in `_data/photo-rotation.yml` (`weekly` or `daily`).

---

## 7. Still to come before launch

These sections of the guide will be added as each piece is built:

- **The contact form:** where enquiries arrive and how to reply.
- **Privacy notice:** what the practice tells patients about their data.
- **virtual Grand Rounds:** updating the programme, speakers and the Zoom registration link. **Agreed on 1 November 2026, not yet built:** Annie will keep next year's programme in a shared Google Sheet. One tab, *Website*, will hold only what the website shows (date, title, speaker, institution, country, a Status column, and a link to the speaker's photo); planning notes, fees and Zoom links stay on other tabs. Every day at 5pm the website will read that tab and update itself; only rows marked Confirmed appear. Talks are always at 8am UK time, so only the date is needed. Speaker photos: save the headshot the speaker sent into the shared Drive folder "vGR speaker photos", copy its link and paste it into the sheet; the website crops and resizes it and shows the speaker's initials until a photo arrives. Please don't paste links to university web pages (they are usually not a photo, and the photo is not ours to copy) or put pictures inside the sheet (they cannot be read back out).
- **Testimonials by email:** the forwarding address described in section 5, once built and tested.
- **Articles and patient guides:** publishing a new article or video.
- **Launch day:** moving the drericlim.com address to the new site.

---

## Appendix A. Where every picture and file is kept

The master copy of everything on the website is in GitHub (**github.com/drericlim/drericlim.github.io**). Google Drive holds reference copies and the original photo library. **Whenever a picture or file is added, renamed or removed, update this appendix** (Claude does this automatically when it makes the change).

Last updated 6 November 2026.

### In GitHub: pictures (`assets/`)

| Folder | Used on | What is in it now | Still needed |
|---|---|---|---|
| `assets/images/` | Across the site, and the preview picture when a page is shared | `eric-lim-portrait.jpg`, `eric-lim-portrait-2.jpg`, `ward-round.jpg` | Higher-resolution portraits |
| `assets/rotating/hero/` | Homepage, large photo at the top (changes weekly) | 6 photos, all 2400 by 1600, Professor Lim on the right: `01-eric-lim-speaking-green.jpg`, `02-eric-lim-theatre.jpg`, `03-eric-lim-seated-theatre.jpg`, `04-eric-lim-speaking-slide.jpg`, `05-eric-lim-speaking-blue.jpg`, `06-eric-lim-theatre-team.jpg` | Nothing (theatre photos 02, 03, 06 are enlarged from the only copies available). The colleagues shown in 02 and 06 have agreed to appear |
| `assets/rotating/home-profile/` | Homepage, About section photo (changes weekly) | The same 9 photos as `about-profile/`, numbered one step ahead (see Rotating photos) | Nothing; add new About photos to both folders |
| `assets/rotating/about-profile/` | About page, portrait at the top (changes weekly) | 9 photos, all 1200 by 1500: `01-eric-lim-speaking-blue.jpg`, `02-eric-lim-theatre-profile.jpg`, `03-eric-lim-speaking-green.jpg`, `04-eric-lim-lab.jpg`, `05-eric-lim-theatre-red-screen.jpg`, `06-eric-lim-speaking-slide.jpg`, `07-eric-lim-theatre.jpg`, `08-eric-lim-speaking-podium.jpg`, `09-eric-lim-theatre-masked.jpg` (this one 500 by 749) | Nothing (theatre photos 02, 05, 07, 09 are enlarged from the only copies available) |
| `assets/awards/` | About page, Awards list (small 80px squares) | `laingbuisson-innovation-in-care-2025.jpg` (award evening photo), `iaslc-ginsberg-award.jpg` (IASLC logo), `scts-research-prizes.jpg` (SCTS crest) | None |
| `assets/team/` | About page, team list (circles) | `maria-leung.jpg` | 4 more team photos |
| `assets/books/` | About page, books | `integrated-textbook-of-medicine-and-surgery.jpg`, `churchills-pocketbook-of-differential-diagnosis.jpg` | None |
| `assets/films/` | About page, cover pictures for the three films | `vimeo-199325659.jpg`, `vimeo-199445739.jpg`, `vimeo-231725351.jpg` | None |
| `assets/partners/` | virtual Grand Rounds page, partner logos | `astrazeneca.svg`, `medtronic.svg` | Official Medtronic, AstraZeneca and Medela logos |
| `assets/speakers/` | virtual Grand Rounds page, speaker headshots | none yet | Speaker headshots |
| `assets/testimonials/` | Homepage quotes and the future testimonials page | `duilio-barbosa.jpg`, `erika-dwek.jpg`, `richard-warren.jpg`, `tony-marsh.jpg` | Check whether the Tony Marsh photo belongs to Rachel Loye |
| `assets/articles/` | Patient guides, articles and Thoracic Reflections | none yet | Added with each article |
| `assets/icons/` | Every page: the logo beside Professor Lim's name, the browser-tab icon and phone icons | Logo files (`logo-on-dark.svg`, `logo-on-light.svg` and PNG copies), icon files (`favicon.ico`, `favicon-32.png`, `apple-touch-icon.png`, `icon-192.png`, `icon-512.png`) and their sources | None |

### In GitHub: text the team edits (`_data/`)

| File | Used on | What it holds |
|---|---|---|
| `_data/testimonials.yml` | Homepage "In their own words" | Patient testimonials, newest first |
| `_data/vgr-feedback.yml` | virtual Grand Rounds "In their own words" | Attendee and speaker quotes, newest first |
| `_data/photo-rotation.yml` | Homepage and About | How often the rotating photos change |
| `_data/about-films.yml` | About page | The three Vimeo films and their cover pictures |

### In GitHub: records

| File | What it holds |
|---|---|
| `README.md` | Version register and full history of changes |
| `docs/managers-guide.md` | This guide |
| `CLAUDE.md` | Instructions Claude follows when the team asks it to make changes |
| `tools/drive-backup/` | The nightly script that saves Drive copies of the approved pages (with setup steps) |

### In Google Drive

| Folder | What is in it |
|---|---|
| **Personal website** folder (drive.google.com/drive/folders/1d-suhHutQ2Nndfd-cHDlm_kAuBiztmFl) | Reference copies of approved pages and logos, named by date, e.g. `20261027-homepage.html`. Older copies end in `-superseded`. Saved automatically every night (between 11pm and midnight) by the script in `tools/drive-backup/` in GitHub, which runs in Professor Lim's Google account. Please don't add or rename page copies here by hand. |
| **Images** folder (drive.google.com/drive/folders/1MIgcWqehVYCUfLlW7_2Eu7OitVH7p38p) | Professor Lim's original photo library (theatre, clinic, portraits, awards and conferences, 2008 to 2026). Photos are chosen from here, resized, and the website copy is put in the right `assets/` folder above. The originals stay in Drive. |

