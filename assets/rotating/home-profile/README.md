# Homepage About photo (rotating)

The photo beside "About" on the homepage.

The website shows one photo from this folder at a time, changing **weekly** (each Monday) or **daily**, as set in `_data/photo-rotation.yml`. Every visitor sees the same photo that week or day. 

## Adding or removing photos

- **Add:** upload the photo here (Add file, then Upload files). It joins the rotation automatically. Nothing else needs changing.
- **Remove:** open the photo and delete it. It leaves the rotation.
- **Order:** photos take turns in file-name order, so start names with a number: `01-…`, `02-…`, `03-…`.

## Which photos

Any real photo of Professor Lim works (no AI-generated pictures). It is trimmed automatically to an upright 4:5 shape, keeping the top of the picture (the face) in view. Best supplied already cropped to 4:5 at 1200 by 1500 pixels; at least 800 pixels wide.

Name files in lower case with hyphens, e.g. `03-eric-lim-clinic.jpg`. Keep each under 500 KB. Anyone else recognisable in a photo, patients especially, must have agreed to it being on the website.

## Keep this folder paired with `about-profile/`

The homepage About photo and the About page portrait use **the same photos**, so a visitor never sees the same picture on both pages in one week:

- Both folders hold the same set of photos, with the same names after the number.
- The **homepage is one step ahead**: the photo numbered `02` in `about-profile/` is numbered `01` in `home-profile/`, `03` becomes `02`, and so on; the About page's `01` is the homepage's last number.
- To add or remove a photo, do it in **both** folders and keep this numbering. Easiest: ask Claude ("add this photo to the About photos on drericlim.com"), which renumbers both folders.
