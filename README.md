# drericlim.com

The website of Professor Eric Lim, thoracic surgeon at the Royal Brompton Hospital.

## Status: testing

This repository holds the new site while it is being built and tested. The live site is still drericlim.com on Squarespace. The domain moves here only once every page is approved and tested.

The test site is published at https://drericlim.github.io/

## Where the pages live

Each page is an `index.html` in a folder named after its web address:

| Page | Address | File |
|---|---|---|
| Home (temporary test page) | `/` | `index.html` |
| For professionals | `/for-professionals` | `for-professionals/index.html` |
| virtual Grand Rounds | `/virtual-grand-rounds` | `virtual-grand-rounds/index.html` |
| About | `/about` | `about/index.html` |
| Contact | `/contact-us` | `contact-us/index.html` |
| Page not built yet | any missing address | `404.html` |

## Before launch

- Every page carries `<meta name="robots" content="noindex, nofollow">` so search engines ignore the test site. At launch this changes back to `index, follow` on every page.
- The contact form needs a form service connected before it can send messages.
