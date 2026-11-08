# PDB Expo — Website

Plain HTML/CSS/JS. No build step. Open `index.html` or run a local server:

```
python3 -m http.server 5050
# then visit http://localhost:5050
```

## Structure
```
index.html          Home page (matches mockup 1)
css/styles.css      Theme + all section styles
js/main.js          Mobile menu + dropdown toggles
assets/             Logo + image placeholders
  logo.svg          PDB Expo wordmark (editable SVG)
  gen-placeholders.sh   Regenerates the grey image placeholders
```

## Swapping in real photos
Every grey placeholder is a file in `assets/` (e.g. `hero-tall.svg`, `prog-1.svg`).
To use a real photo, drop your image in `assets/` and update the matching `src="..."`
in `index.html`. Recommended sizes:

| Placeholder        | Used for                    | Suggested size |
|--------------------|-----------------------------|----------------|
| hero-tall.svg      | Hero — tall left image      | 520×760        |
| hero-2 / hero-3    | Hero — stacked right images | 520×360        |
| why-network/surface| Why-Attend photo cards      | 360×240        |
| prog-1…4           | Featured Programs           | 400×300        |

The hero is **4 separate images in a CSS grid** — no need for one combined photo.

## Pages still to build (from the layout)
About · Championships & Showcases · Expo · Summit · Contact · Register
(nav + footer links already point to these.)

## Brand
Navy `#080c16` · Red `#d8203a` · Blue `#1d4ed8` · Silver `#c9d2df`
Fonts: Oswald (headings) + Inter (body), loaded from Google Fonts.
