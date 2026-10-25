# Adding a patient testimonial

All testimonials live in one file: **`_data/testimonials.yml`**. The Testimonials page and the rotating quote on the homepage are both built from this file, so a testimonial only ever needs adding once.

Before you start, make sure the patient has agreed **in writing** to their words being published with their full name, and to their photo too if they sent one. Keep that email or letter on file.

## The easy way: ask Claude

1. Open Claude, in a session that has access to the `drericlim/drericlim.github.io` repository on GitHub.
2. Paste the patient's email (or forward it, or attach it) and write: **"Please add this testimonial to drericlim.com."** Attach their photo too, if they sent one.
3. Claude will ask you to confirm that the patient has agreed to publication. It will then show you exactly how the testimonial will read.
4. Reply "yes" and Claude saves it. The website updates within a few minutes.

Claude follows the house rules for this, which are kept in `CLAUDE.md` in the repository: the patient's own words, unedited, with personal details left out.

## By hand, if you prefer (about 5 minutes, all in your web browser)

1. Go to **github.com/drericlim/drericlim.github.io** and sign in.
2. Open the folder **`_data`**, then the file **`testimonials.yml`**.
3. Click the **pencil icon** (Edit this file), at the top right of the file.
4. Near the top you will see a block marked **TEMPLATE**. Below it is the line `# ---------- NEWEST FIRST ----------`.
5. Click at the start of the line directly **under** `NEWEST FIRST` and paste in a new entry like this:

```yaml
- name: "Jane Smith"
  year: 2026
  treatment: "Day case lobectomy"
  photo: ""
  homepage: no
  quote: |
    I was home the same day and back walking the dog within a week.

    Thank you to Professor Lim, Maria and the whole team.

```

6. Click **Commit changes…**. In the box that appears, write a short note such as "Add testimonial from Jane Smith", then click **Commit changes** again.
7. The website updates itself within a couple of minutes.

### What each line means

| Line | What to put | Required? |
|---|---|---|
| `name` | The patient's name exactly as they want it shown, inside quotation marks. | Yes |
| `year` | The year they sent it, e.g. `2026`. No quotation marks. | Yes |
| `treatment` | A few words about their operation, e.g. `"Keyhole lobectomy"`. Leave as `""` if unsure. | No |
| `photo` | The photo's file name, e.g. `"jane-smith.jpg"` (see below). Leave as `""` if there's no photo. | No |
| `homepage` | `yes` to include it in the rotating quote on the homepage, otherwise `no`. Only choose `yes` for short quotes of one to three sentences. | Yes |
| `quote` | The patient's own words, starting on the line below `quote: \|`. | Yes |

### Rules that keep the file working

- **Indents matter.** Every line of an entry starts with two spaces, and every line of the quote starts with **four** spaces. Copying the example above keeps this right.
- Leave a **blank line** between paragraphs of the quote, and one blank line after each entry.
- Use the patient's words exactly. Don't correct their grammar or spelling unless they ask you to.
- If a name contains a quotation mark, ask Claude or your web developer for help.

If anything goes wrong, GitHub keeps every earlier version, so nothing is ever lost. Open the file, click **History**, and you can see or restore any previous version.

## Adding a photo

1. Ask the patient for a photo, and make sure they agree to it appearing on the site.
2. Rename it with their name in lower case and hyphens, e.g. `jane-smith.jpg`.
3. On GitHub, open the folder **`assets/testimonials`**, click **Add file → Upload files**, drag the photo in, and click **Commit changes**.
4. In `testimonials.yml`, put the file name on the photo line: `photo: "jane-smith.jpg"`.

Photos look best when they are at least 800 pixels wide and under 500 KB.

## Editing or removing a testimonial

Open `testimonials.yml` with the pencil icon, find the patient's name (Ctrl+F or Cmd+F), change or delete their whole entry (from `- name:` to the end of their quote), and commit as above.
