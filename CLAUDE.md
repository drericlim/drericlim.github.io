# Notes for Claude working on drericlim.com

Read `README.md` first. Its **Version register** is the single record of which version of each page is approved and where it is kept. Several separate conversations work on this site, and they do not share memory, so:

- Start every change from the file in this repository, never from an older copy in a conversation or in Drive.
- After any change, update the version register and the amendment history in `README.md` in the same commit.
- Work in GitHub only during a session: make each change here and push, and the test site updates within a minute or two. Do **not** save to Google Drive after every change. Saving to Drive is slow, because the whole page has to be pasted through the conversation.
- At the end of a session (when Professor Lim says so, or before finishing), save the final version of each page changed that session to the Google Drive folder `1d-suhHutQ2Nndfd-cHDlm_kAuBiztmFl`, named `YYYYMMDD-page-name.html`, and rename the copy it replaces with `-superseded`. Drive copies use `index, follow`; repository copies use `noindex, nofollow` until launch. Then record in the register which version Drive holds.
- Keep the register in the claude.ai project doc `claude/site-register.md` in step with `README.md`.
- **Keep `docs/managers-guide.md` up to date.** Whenever something is built or decided that the practice team will need to use or know (a new editing process, where something is kept, a new account or tool), add it there in plain English for non-technical readers. It will be presented to the managers when the site is complete.

## Standing design rules (agreed with Professor Lim)

- No sticky navigation or sticky elements. No pill or chip-style buttons.
- Content reads top to bottom (down each column, then across).
- Each section has a pressed, engraved header texture: For patients = raked sand around one stone; For professionals = forest plot; virtual Grand Rounds = globe; About = sutures; Contact = conversation bubbles. The small mark beside each section heading is clickable and returns to the top of the page.
- Always write "virtual Grand Rounds" with a lower-case v.
- Key figures sit high on the page.
- Photos have rounded corners: 12px for photos and video frames, 8px for small thumbnails. Photos of people in team and speaker lists are circles. Full-width background photos (such as the homepage hero) stay square-edged.
- Every page must be SEO-ready: title, description, canonical, Open Graph and JSON-LD.
- Mock-ups carry a version number (v0.x for drafts, v1.0 when approved, v1.1 and so on for later amendments).

## Practice facts

- Professor Lim practises only at the Royal Brompton Hospital, Sydney Street, London SW3 6NP. Telephone +44 (0) 207 352 8121. There is no fax.
- Private patients are self-funding; he does not work with insurers. NHS referrals come through the patient's hospital multidisciplinary team; no out-of-area NHS referrals.
- Team: Maria Leung (practice manager), Christopher Arumugam (medical secretary), Sarah Booth (surgical care practitioner), Michael Evans (clinical nurse specialist), Paulo De Sousa (research nurse).
- No donations or giving page.

## Adding a patient testimonial (for any Claude session)

Team members add testimonials by pasting or forwarding the patient's email to Claude and asking for it to be added. Follow these steps exactly:

1. **Consent first.** Ask: "Has the patient agreed in writing to this being published with their name (and photo, if any)?" Do not continue without a yes.
2. **Extract**, without rewording: the patient's own words of thanks only (leave out greetings such as "Dear Professor Lim", clinical details the patient would not want public, phone numbers, addresses and email signatures), the name exactly as the patient wants it shown, and the year the email was sent. Ask about anything unclear rather than guessing. Never correct the patient's grammar or spelling unless asked.
3. **Treatment** (optional): a few plain words only if the email states it, e.g. "Day case lobectomy". Otherwise leave it empty.
4. **Homepage extract:** choose one or two sentences copied exactly from the quote (at most about 200 characters, using … where words are left out) that best say what the patient valued, and put them in `short`. Set `homepage: yes` so the patient joins the rotating quotes on the homepage; the aim is many different patients there. Use `homepage: no` only if no part of the quote suits the homepage (for example it criticises another hospital or doctor).
5. **Photo:** if attached and consented, save it as `assets/testimonials/firstname-lastname.jpg` (at most 1000px wide, under 500 KB) and set `photo` to that file name.
6. **Show the team member a preview** of the entry as it will read on the site, and get a yes before saving.
7. **Insert** the entry directly under the `# ---------- NEWEST FIRST ----------` line in `_data/testimonials.yml`, in the same format as the entries already there (two-space indent, quote under `quote: |` with four-space indent, a blank line between paragraphs and after the entry).
8. **Check** the file still loads (for example `python3 -c "import yaml; yaml.safe_load(open('_data/testimonials.yml'))"`) and that the number of entries went up by one.
9. **Commit** with the message `Add testimonial from <name>` and push. Tell the team member it will appear on the site within a few minutes.
