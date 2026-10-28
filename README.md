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
| Home | `/` | v1.22 | 28 Oct 2026 | `index.html` | `20261027-homepage.html` |
| For patients | `/for-patients` | v1.6 | 28 Oct 2026 | `for-patients/index.html` | `20261025-hub-for-patients.html` |
| For professionals | `/for-professionals` | v1.7 | 28 Oct 2026 | `for-professionals/index.html` | `20261025-hub-for-professionals.html` |
| virtual Grand Rounds | `/virtual-grand-rounds` | v1.7 | 28 Oct 2026 | `virtual-grand-rounds/index.html` | `20261025-hub-virtual-grand-rounds.html` |
| About | `/about` | v1.11 | 28 Oct 2026 | `about/index.html` | `20261025-hub-about.html` |
| Contact | `/contact-us` | v1.4 | 28 Oct 2026 | `contact-us/index.html` | `20261025-contact.html` |
| Site map (planning document, not a web page) | none | agreed | 25 Oct 2026 | none | `20261025-sitemap.html` |
| Logo (dark and light) | none | official | 27 Oct 2026 | `assets/icons/logo-on-dark.svg`, `assets/icons/logo-on-light.svg` | `20261027-logo-dark.svg`, `20261027-logo-light.svg` |
| Page not built yet | any missing address | test page | 25 Oct 2026 | `404.html` | none |

### Amendment history

- **virtual Grand Rounds v1.7**: the 2026 programme (section 02) is collapsed by default to save space. A single line, "See all 35 lectures, January to December", opens the full list and changes to "Hide the full programme". Built with the browser's own open-and-close element (`<details>`), so it works without JavaScript and search engines still read every lecture. Section height on a laptop drops from about 2,600px to 440px; on a phone from about 5,400px to 490px.
- **All pages, 28 Oct (Home v1.22, For patients v1.6, For professionals v1.7, virtual Grand Rounds v1.6, About v1.11, Contact v1.4)**: For patients section 05 is labelled "Articles" (was "Patient information", which was confusing as the whole page is patient information). Changed in the For patients contents list and section label, and in the footer link on every page. The section heading "Articles for patients and families." and the `#articles` address are unchanged.
- **All pages, 28 Oct (files only; no page versions changed)**: the browser-tab icon (`favicon.ico`, `favicon-32.png`) and Android icons (`icon-192.png`, `icon-512.png`) show the light logo in a subtle circle (white, with a pale blue rim; Professor Lim chose this of three styles) instead of a white square, from `assets/icons/logo-light-circle.svg`. The iPhone home-screen icon (`apple-touch-icon.png`) stays square, as iPhones round it themselves.
- **All pages, 27 Oct (files only; no page versions changed)**: the site icon (browser tab and phone home screen) now uses Professor Lim's light logo on white instead of the dark logo on navy: `favicon.ico`, `favicon-32.png`, `apple-touch-icon.png`, `icon-192.png`, `icon-512.png`, made from `assets/icons/logo-light-tile.svg` (`logo-dark-tile.svg` removed).
- **Home v1.21**: the rotating patient quotes break into lines of even length, so a quote never ends with a last line of one or two words. Uses the browser's built-in balancing (`text-wrap: balance`); a short script does the same in older browsers without it. Tested on all 54 homepage quotes at desktop, tablet and phone widths: short last lines went from 12 to 0 (desktop) and 16 to 0 (phone).
- **Home v1.20**: the pressed section marks beside each homepage heading are redrawn from Professor Lim's official logo (the same shape as `assets/icons/logo-on-dark.svg`: lobes, line and ring, all pressed in one colour). The drawing is kept once (`lung-k`) and shared by the light and dark marks.
- **All pages, 27 Oct (no page versions changed; files only)**: Professor Lim's official logo replaces the traced one. Dark version `assets/icons/logo-on-dark.svg` (beside his name at the top left of every page) and light version `assets/icons/logo-on-light.svg` (replaces `logo.svg`), both traced as sharp drawings from the originals he supplied (kept as `logo-dark-original.png` and `logo-light-original.png`), with 1200px transparent PNG copies for documents. The site icon (`favicon.ico`, `favicon-32.png`, `apple-touch-icon.png`, `icon-192.png`, `icon-512.png`) is remade from the dark version on a navy square (`logo-dark-tile.svg`). `lung-mark.png` removed. Details: `assets/icons/README.md`.
- **Home v1.19**: "I'm a clinician" reads "Free international teaching through the virtual Grand Rounds, and Thoracic Reflections, my essays on the trials, guidelines and debates shaping our practice." (matches the For professionals page).
- **For professionals v1.6**: Thoracic Reflections text reads "Essays on the trials, guidelines and debates shaping our practice. Read them here, or receive each new one by email."
- **Home v1.18**: "I'm a clinician" describes Thoracic Reflections as "my take on where the field is heading, from new evidence to how we train surgeons" (not only articles on new evidence).
- **All pages, 25 Oct (Home v1.17, For patients v1.5, For professionals v1.5, virtual Grand Rounds v1.5, About v1.10, Contact v1.3)**: less space between sections, about 25% tighter. Homepage sections 110px to 80px above and below, headings 64px to 44px above content; other pages 72px to 54px, headings 40px to 32px; closing call-to-action 100–120px to 72–88px; smaller still on phones. Set in a block marked "Tighter spacing between sections" at the end of each page's styles.
- **Home v1.16**: section marks added beside each homepage section heading (Start here, About, Your journey, Expertise, In their own words): Professor Lim's lung logo, pressed into the surface in the same engraved style as the other pages' marks (option B). Clicking a mark returns to the top. The homepage's section labels are now the same size (16px) as on every other page (they had been 17px, and "In their own words" 12px).
- **All pages, 25 Oct (Home v1.15, For patients v1.4, For professionals v1.4, virtual Grand Rounds v1.4, About v1.9, Contact v1.2)**: Professor Lim's lung logo beside his name at the top left of every page (light version for the dark top bar, `assets/icons/logo-on-dark.svg`; full-colour version `assets/icons/logo.svg`), traced from the favicon so it stays sharp.
- **All pages, 25 Oct (Home v1.14, For patients v1.3, For professionals v1.3, virtual Grand Rounds v1.3, About v1.8, Contact v1.1, 404)**: site icon (the lung symbol from the old site) added: `favicon.ico` at the top of the repository and phone home-screen icons in `assets/icons/`.
- **About v1.7**: each film shows its cover picture (taken from Vimeo, black bars trimmed) behind the play button, from `assets/films/`. Introduction 2 has Arabic subtitles on purpose (for Arabic-speaking patients). Any film can be previewed with `/about/?film=1`, `2` or `3`.
- **About v1.6**: when a film finishes, the cover and play button come back, so Vimeo's "More from Eric Lim" end screen is never shown.
- **About v1.5**: the film band rotates weekly through three Vimeo films listed in `_data/about-films.yml`: Introduction part 1 (199325659), Introduction part 2 (199445739) and ctDNA research (231725351). The play button wording changes with the film. Vimeo's title, byline and badge are hidden in the player.
- **Home v1.13 and About v1.4**: rotating photos. The homepage background, the homepage About photo and the About page portrait each take turns through the photos in `assets/rotating/hero/`, `home-profile/` and `about-profile/`, changing every Monday (or daily; set in `_data/photo-rotation.yml`). Pages are built by GitHub Pages (both now start with front matter). The homepage About photo is trimmed to a consistent 4:5 shape. The hero rotates once its folder has two or more photos.
- **All pages, 25 Oct (Home v1.12, For patients v1.2, For professionals v1.2, virtual Grand Rounds v1.2, About v1.3)**: images moved off Squarespace into `assets/`, one folder per kind. Pages now use `/assets/...`; social-preview and Google images use `https://www.drericlim.com/assets/images/eric-lim-portrait.jpg`. The About page now expects team photos, award pictures and book covers by name, showing initials or the drawn placeholder until each is uploaded. The Medela logo still comes from a public logo website until the official file arrives.
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

**Drive is one change behind** (last saved 27 Oct 2026): the 28 Oct "Articles" label (Home v1.22, For patients v1.6, For professionals v1.7, virtual Grand Rounds v1.6, About v1.11, Contact v1.4) and the collapsed programme (virtual Grand Rounds v1.7) are in this repository but not yet in Drive. Drive holds Home v1.21 (`20261027-homepage.html`; v1.20 renamed `20261027-homepage-v1.20-superseded.html`, v1.19 `20261025-homepage-v1.19-superseded.html`), the official logos (`20261027-logo-dark.svg`, `20261027-logo-light.svg`), and For patients v1.5, For professionals v1.6, virtual Grand Rounds v1.5, About v1.10 and Contact v1.3 as `20261025-<page>.html`. Older copies are kept as `20261025-<page>-v<old version>-superseded.html`.
- Drive file IDs: homepage `1615yAufISKoC4KdgPSHXsY3aXlNKxdji`, hub-for-patients `1dtECmQtuAHUR8FEY32D8gw9izD0vb_lZ`, hub-for-professionals `1OlnH1picwu1RPwinbHAGY-ovtPthkxbi`, hub-virtual-grand-rounds `1xcrndPsLC6za-CI5pxnRAsm56H2b7rBG`, hub-about `1MbCY6ceg1ogWsrRoCrxKeaHh4_bKfooe`, contact `1OTCxvrMDuv9OdMdGtoaIj-PviR1wzv5d`.
- Home and About copies keep their GitHub Pages front matter and Liquid tags (they are the source files; rotating photos, films and quotes are filled in by GitHub Pages).
- The only difference between the two copies is the search-engine setting. The repository copy says `noindex, nofollow` during testing. The Drive copy says `index, follow`, as it will at launch.

## Guide for the practice team

`docs/managers-guide.md` is the practice team's guide to the site: where things are kept, what each person needs, and how to make changes. It is kept up to date as the site is built, and will be presented to the managers at launch.

## Content that managers edit

- **About page films:** `_data/about-films.yml` (Vimeo numbers, button wording), rotating weekly.
- **Rotating photos:** `assets/rotating/` (hero, home-profile, about-profile). Upload to add, delete to remove; frequency in `_data/photo-rotation.yml`.
- **Images:** `assets/`, one folder per kind, each with a note on what goes in it and how to name files. Guide: `docs/managers-guide.md`, section 6.
- **Testimonials:** `_data/testimonials.yml` holds every patient testimonial (69 moved from the old site on 25 Oct 2026, word for word), newest first. Each has a `short` extract (one or two sentences, verbatim) for the homepage's rotating quotes; 54 patients are in the rotation. Patient photos are in `assets/testimonials/`. Step-by-step guide: `docs/managers-guide.md`, section 5. The Testimonials page and the homepage's rotating quote will both be built from this file.

## Before launch

- Every page carries `<meta name="robots" content="noindex, nofollow">` so search engines ignore the test site. At launch this changes back to `index, follow` on every page.
- The contact form needs a form service connected before it can send messages, and a privacy notice page at `/privacy`.
- Images: all now in `assets/` (see `assets/README.md`). Still to supply: team photos (4), award pictures (LaingBuisson, SCTS), book covers (2), official partner logos (Medtronic, AstraZeneca, Medela), speaker headshots, and ideally higher-resolution originals of the two portraits.
- The hero video link is still to be added.
- Build the `/testimonials` page from `_data/testimonials.yml`.
- Check the photo beside Tony Marsh's testimonial (it shows a woman and a baby).
- The virtual Grand Rounds registration link (Zoom) is a placeholder.
- Vimeo: each About page film must list `drericlim.com`, `www.drericlim.com` and `drericlim.github.io` under Privacy → "Where can this be embedded?" (Specific domains). Requested from Professor Lim on 25 Oct 2026.
