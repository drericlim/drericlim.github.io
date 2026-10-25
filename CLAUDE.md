# Notes for Claude working on drericlim.com

Read `README.md` first. Its **Version register** is the single record of which version of each page is approved and where it is kept. Several separate conversations work on this site, and they do not share memory, so:

- Start every change from the file in this repository, never from an older copy in a conversation or in Drive.
- After any change, update the version register and the amendment history in `README.md` in the same commit.
- Work in GitHub only during a session: make each change here and push, and the test site updates within a minute or two. Do **not** save to Google Drive after every change. Saving to Drive is slow, because the whole page has to be pasted through the conversation.
- At the end of a session (when Professor Lim says so, or before finishing), save the final version of each page changed that session to the Google Drive folder `1d-suhHutQ2Nndfd-cHDlm_kAuBiztmFl`, named `YYYYMMDD-page-name.html`, and rename the copy it replaces with `-superseded`. Drive copies use `index, follow`; repository copies use `noindex, nofollow` until launch. Then record in the register which version Drive holds.
- Keep the register in the claude.ai project doc `claude/site-register.md` in step with `README.md`.

## Standing design rules (agreed with Professor Lim)

- No sticky navigation or sticky elements. No pill or chip-style buttons.
- Content reads top to bottom (down each column, then across).
- Each section has a pressed, engraved header texture: For patients = raked sand around one stone; For professionals = forest plot; virtual Grand Rounds = globe; About = sutures; Contact = conversation bubbles. The small mark beside each section heading is clickable and returns to the top of the page.
- Always write "virtual Grand Rounds" with a lower-case v.
- Key figures sit high on the page.
- Every page must be SEO-ready: title, description, canonical, Open Graph and JSON-LD.
- Mock-ups carry a version number (v0.x for drafts, v1.0 when approved, v1.1 and so on for later amendments).

## Practice facts

- Professor Lim practises only at the Royal Brompton Hospital, Sydney Street, London SW3 6NP. Telephone +44 (0) 207 352 8121. There is no fax.
- Private patients are self-funding; he does not work with insurers. NHS referrals come through the patient's hospital multidisciplinary team; no out-of-area NHS referrals.
- Team: Maria Leung (practice manager), Christopher Arumugam (medical secretary), Sarah Booth (surgical care practitioner), Michael Evans (clinical nurse specialist), Paulo De Sousa (research nurse).
- No donations or giving page.
