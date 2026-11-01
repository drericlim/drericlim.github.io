# Homepage background photo (rotating)

The large photo behind the headline at the top of the homepage.

The website shows one photo from this folder at a time, changing **weekly** (each Monday) or **daily**, as set in `_data/photo-rotation.yml`. Every visitor sees the same photo that week or day. It rotates once there are two or more photos in this folder. Until then the one photo here stays.

## Adding or removing photos

- **Add:** upload the photo here (Add file, then Upload files). It joins the rotation automatically. Nothing else needs changing.
- **Remove:** open the photo and delete it. It leaves the rotation.
- **Order:** photos take turns in file-name order, so start names with a number: `01-…`, `02-…`, `03-…`.

## Which photos

Landscape (wide) photos, saved at 2400 by 1600 pixels (at least 2000 wide). The headline sits over the **left** side, so Professor Lim must be on the **right**, about three-quarters of the way across. Ask Claude to check and position new photos so they all sit the same way. Where a photo had to move right, its left edge fades into the site's navy, which the dark overlay covers; the photo itself is not altered. Real photos only, with no colour effects.

Name files in lower case with hyphens, e.g. `03-eric-lim-clinic.jpg`. Keep each under 500 KB. Anyone else recognisable in a photo, patients especially, must have agreed to it being on the website.

## No repeats across the three photo spots

The hero, the homepage About photo and the About page portrait never show the same photo in the same week (agreed with Professor Lim, 1 Nov 2026). This depends on the order of the photos in all three folders:

- **The same photo keeps the same name in every folder** (only the number differs), e.g. `02-eric-lim-theatre.jpg` here is `07-eric-lim-theatre.jpg` in `about-profile/`.
- After adding, removing or renaming a photo in any of the three folders, run `python3 tools/check-photo-rotation.py` (or ask Claude to). It says OK, or which photo would repeat and in which week; then reorder or renumber.
