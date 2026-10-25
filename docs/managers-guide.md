# drericlim.com: guide for the practice team

*A living guide. It grows as the new website is built, and will be presented to the practice managers when the site is complete. Last updated 25 October 2026.*

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
| **Reference copies of approved pages** | Google Drive, "Personal website" folder | A dated copy of each approved page (e.g. `20261025-homepage.html`). Older copies are marked "-superseded". These are saved at the end of each working session. |
| **Testimonials** | GitHub: `_data/testimonials.yml` | Every patient testimonial on the site, newest first |
| **All photos and logos** | GitHub: `assets/`, one folder per kind (see section 6) | Every picture on the website |
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

**Before you start:** make sure the patient has agreed **in writing** to their words being published with their full name, and to their photo too if they sent one. Keep that email on file.

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
- **Homepage background photos** must be wide, with the subject on the **right**, because the headline sits on the left. Ask Claude to check and crop them before they go in.
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
- **virtual Grand Rounds:** updating the programme, speakers and the Zoom registration link.
- **Articles and patient guides:** publishing a new article or video.
- **Launch day:** moving the drericlim.com address to the new site.
