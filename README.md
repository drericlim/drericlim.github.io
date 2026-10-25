# drericlim.com

The website of Professor Eric Lim, thoracic surgeon at the Royal Brompton Hospital.

## Status: testing

This repository holds the new site while it is being built and tested. The live site is still drericlim.com on Squarespace. The domain moves here only once every page is approved and tested.

The test site is published at https://drericlim.github.io/

## Version register

This table is the single record of the latest approved version of every page. Update it whenever a page changes, in the same commit.

Versions: drafts are v0.x. The approved version is v1.0. Amendments after approval are v1.1, v1.2 and so on.

| Page | Address | Approved version | Approved on | File in this repository | Copy in Google Drive |
|---|---|---|---|---|---|
| Home | `/` | v1.11 | 25 Oct 2026 | `index.html` | `20261025-homepage.html` |
| For patients | `/for-patients` | v1.1 | 25 Oct 2026 | `for-patients/index.html` | `20261025-hub-for-patients.html` |
| For professionals | `/for-professionals` | v1.1 | 25 Oct 2026 | `for-professionals/index.html` | `20261025-hub-for-professionals.html` |
| virtual Grand Rounds | `/virtual-grand-rounds` | v1.1 | 25 Oct 2026 | `virtual-grand-rounds/index.html` | `20261025-hub-virtual-grand-rounds.html` |
| About | `/about` | v1.2 | 25 Oct 2026 | `about/index.html` | `20261025-hub-about.html` |
| Contact | `/contact-us` | v1.0 | 25 Oct 2026 | `contact-us/index.html` | `20261025-contact.html` |
| Site map (planning document, not a web page) | none | agreed | 25 Oct 2026 | none | `20261025-sitemap.html` |
| Page not built yet | any missing address | test page | 25 Oct 2026 | `404.html` | none |

### Amendment history

- **Home v1.11**: the patient quote section ("In their own words") now rotates through 54 different patients, built by GitHub Pages from the `short` extracts in `_data/testimonials.yml`. Shuffled on every visit, changes every 7 seconds, with previous, pause and next buttons; stays still for visitors who prefer reduced motion. The five decorative stars were removed, as these are letters rather than star ratings. `index.html` now starts with a front-matter block (`---`) so GitHub Pages fills in the quotes; keep it.
- **Home v1.10**: Start here, "I'm a clinician" also mentions Thoracic Reflections; its single link, "Explore teaching for clinicians", goes to the For professionals hub, which holds both.
- **Home v1.9**: opening section ends "With single-incision keyhole surgery and a drain-free recovery, many patients now go home the same day."
- **Home v1.8**: Start here, "I'm a patient" reads "Guides, articles and videos on your condition, your options and what to expect, from first consultation to full recovery." (Videos are planned; add them before launch.)
- **For patients v1.1**: Day case card reads "Drain-free, pain-managed surgery. Many patients now go home the same day." (was "selected patients").
- **Home v1.7**: opening section ends "Many patients home the same day." (was "Home, in some cases, the same day."), consistent with Your journey.
- **Home v1.6**: Start here, "I'm a clinician" shortened to "Join the virtual Grand Rounds: free international teaching across the thoracic specialties."
- **Home v1.5**: Your journey, Your recovery reads "Many patients now go home on the day of their operation. If you have any questions once you're home, you can call my office."
- **Home v1.4**: About section reads "Private consultations at the Royal Brompton Hospital, Chelsea, London, United Kingdom." with "More about my practice" on its own line.
- **Home v1.3**: the About photo has rounded corners (site style: 12px for photos).
- **About v1.2**: rounded corners on the portrait and film (12px) and on the award and book thumbnails (8px).
- **Home v1.2**: the frame around the About photo removed; the photo stands on its own.
- **Home v1.1**: the About photo frame now sits evenly around the photo (option B). The first key figure counts years as a consultant since 2007, working out the number from today's date, and the About text says "Since 2007" instead of "more than two decades".
- **Home v1.0**: approved from draft v0.8. Changes at approval: consultations now say "at the Royal Brompton Hospital" rather than "in London", and the footer's patient links match the other pages ("Screening and giving" removed).
- **For patients v1.0**: approved from draft v0.7, unchanged.
- **For professionals v1.1**: the programme button links to the virtual Grand Rounds programme.
- **virtual Grand Rounds v1.1**: footer updated (fax removed, "Message us", social links).
- **About v1.1**: Paulo De Sousa, research nurse, added to My team.
- **Contact v1.0**: approved with the conversation-bubble header and the self-funding note.

## Where things are kept

- **This repository** is the master copy of every approved page. Always start changes from the file here.
- **Google Drive** ([Personal website folder](https://drive.google.com/drive/folders/1d-suhHutQ2Nndfd-cHDlm_kAuBiztmFl)) holds a reference copy of each approved version, named by date (for example `20261025-homepage.html`). Older copies are renamed with `-superseded` and kept. Drive is updated **once, at the end of each working session**, so during a session it can be a version behind this repository.

**Drive copies waiting to be saved:** Home v1.11 (Drive holds v1.1), About v1.2 (Drive holds v1.1), For patients v1.1 (Drive holds v1.0).
- The only difference between the two copies is the search-engine setting. The repository copy says `noindex, nofollow` during testing. The Drive copy says `index, follow`, as it will at launch.

## Guide for the practice team

`docs/managers-guide.md` is the practice team's guide to the site: where things are kept, what each person needs, and how to make changes. It is kept up to date as the site is built, and will be presented to the managers at launch.

## Content that managers edit

- **Testimonials:** `_data/testimonials.yml` holds every patient testimonial (69 moved from the old site on 25 Oct 2026, word for word), newest first. Each has a `short` extract (one or two sentences, verbatim) for the homepage's rotating quotes; 54 patients are in the rotation. Patient photos are in `assets/testimonials/`. Step-by-step guide: `docs/managers-guide.md`, section 5. The Testimonials page and the homepage's rotating quote will both be built from this file.

## Before launch

- Every page carries `<meta name="robots" content="noindex, nofollow">` so search engines ignore the test site. At launch this changes back to `index, follow` on every page.
- The contact form needs a form service connected before it can send messages, and a privacy notice page at `/privacy`.
- Photos are still loaded from the Squarespace site. Copy them into this repository before Squarespace is closed.
- The hero video link is still to be added.
- Build the `/testimonials` page from `_data/testimonials.yml`.
- Check the photo beside Tony Marsh's testimonial (it shows a woman and a baby).
- The virtual Grand Rounds registration link (Zoom) is a placeholder.
