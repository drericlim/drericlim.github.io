#!/usr/bin/env python3
"""Check the three rotating photo spots never show the same photo in the same week.

The spots are the homepage hero (assets/rotating/hero/), the homepage About photo
(assets/rotating/home-profile/) and the About page portrait (assets/rotating/about-profile/).
A photo is identified by its file name after the number, so the same photo must keep the
same name in every folder (for example 07-eric-lim-theatre.jpg in about-profile/ and
02-eric-lim-theatre.jpg in hero/).

It also checks that home-profile/ holds the same photos as about-profile/, numbered one
step ahead (About 02 = home 01; About 01 = home's last).

Run from the repository root:  python3 tools/check-photo-rotation.py
It mirrors the rotation in the pages' script: photos taken in file-name order, one step
per week (or per day) counted from Monday 5 January 2026, as set in _data/photo-rotation.yml.
"""
import math
import os
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
EXTS = (".jpg", ".jpeg", ".png", ".webp")


def photos(spot):
    folder = os.path.join(ROOT, "assets", "rotating", spot)
    return sorted(f for f in os.listdir(folder) if f.lower().endswith(EXTS))


def name(f):
    """The photo's identity: the file name without its number and extension."""
    stem = os.path.splitext(f)[0].lower()
    return stem.split("-", 1)[1] if stem[:2].isdigit() and "-" in stem else stem


def main():
    hero, home, about = photos("hero"), photos("home-profile"), photos("about-profile")
    problems = []

    # 1. home-profile is about-profile, one step ahead
    expected = [name(f) for f in about[1:] + about[:1]]
    if [name(f) for f in home] != expected:
        problems.append(
            "home-profile/ is not about-profile/ numbered one step ahead.\n"
            "    about-profile: " + ", ".join(about) + "\n"
            "    home-profile:  " + ", ".join(home) + "\n"
            "    home-profile should hold, in order: " + ", ".join(expected)
        )

    # 2. no photo in two spots in the same week, over a full cycle
    spots = [("homepage hero", hero), ("homepage About photo", home), ("About page", about)]
    spots = [(label, [name(f) for f in files]) for label, files in spots if files]
    cycle = 1
    for _, files in spots:
        cycle = cycle * len(files) // math.gcd(cycle, len(files))
    clashes = []
    for k in range(cycle):
        seen = {}
        for label, files in spots:
            n = files[k % len(files)]
            if n in seen:
                clashes.append((k, n, seen[n], label))
            seen[n] = label
    if clashes:
        k, n, a, b = clashes[0]
        problems.append(
            f"'{n}' would show on the {a} and the {b} in the same week "
            f"({len(clashes)} clash(es) in a {cycle}-week cycle). Reorder or rename the photos."
        )

    if problems:
        print("PHOTO ROTATION PROBLEMS:\n- " + "\n- ".join(problems))
        sys.exit(1)
    print(f"OK: hero {len(hero)}, homepage About {len(home)}, About page {len(about)} photos; "
          f"no repeats across the three spots over the full {cycle}-week cycle.")


if __name__ == "__main__":
    main()
