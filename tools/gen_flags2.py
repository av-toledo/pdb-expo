#!/usr/bin/env python3
"""Generate accurate US and South Korea flag SVGs -> assets/flags/{us,kr}.svg"""
import os
A = os.path.join(os.path.dirname(__file__), "..", "assets", "flags")

# ---------------- United States ----------------
W, H = 60, 40
stripe = H / 13
white_stripes = "".join(
    f'<rect y="{round(i*stripe,3)}" width="60" height="{round(stripe,3)}"/>'
    for i in range(1, 13, 2)
)
uw, uh = 24.0, stripe * 7          # union: 2/5 width, 7 stripes tall
stars = ""
for row in range(9):                # 9 rows: 6,5,6,5,6,5,6,5,6 = 50
    n = 6 if row % 2 == 0 else 5
    y = uh * (row + 0.5) / 9
    for col in range(n):
        x = uw * (col + 0.5) / 6 if row % 2 == 0 else uw * (col + 1) / 6
        stars += f'<circle cx="{round(x,3)}" cy="{round(y,3)}" r="0.82"/>'
us = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 60 40">'
    '<rect width="60" height="40" fill="#b22234"/>'
    f'<g fill="#fff">{white_stripes}</g>'
    f'<rect width="{uw}" height="{round(uh,3)}" fill="#3c3b6e"/>'
    f'<g fill="#fff">{stars}</g>'
    '</svg>'
)
open(os.path.join(A, "us.svg"), "w").write(us)

# ---------------- South Korea ----------------
cx, cy, R = 30.0, 20.0, 9.6
r = R / 2
# Taegeuk drawn horizontally (red on top, blue on bottom), then tilted -33.69deg.
red = (f'M{cx-R},{cy} A{r},{r} 0 0 1 {cx},{cy} A{r},{r} 0 0 0 {cx+R},{cy} '
       f'A{R},{R} 0 0 0 {cx-R},{cy} Z')
blue = (f'M{cx-R},{cy} A{r},{r} 0 0 1 {cx},{cy} A{r},{r} 0 0 0 {cx+R},{cy} '
        f'A{R},{R} 0 0 1 {cx-R},{cy} Z')

def trigram(tx, ty, pattern, rot):
    """pattern: list of 1(solid)/0(broken), top->bottom."""
    bl, th, vgap, bgap = 9.0, 1.5, 2.9, 2.4
    bars = ""
    for i, solid in enumerate(pattern):
        y = (i - 1) * vgap - th / 2
        if solid:
            bars += f'<rect x="{-bl/2}" y="{round(y,2)}" width="{bl}" height="{th}"/>'
        else:
            seg = (bl - bgap) / 2
            bars += (f'<rect x="{-bl/2}" y="{round(y,2)}" width="{seg}" height="{th}"/>'
                     f'<rect x="{bgap/2}" y="{round(y,2)}" width="{seg}" height="{th}"/>')
    return f'<g transform="translate({tx},{ty}) rotate({rot})">{bars}</g>'

# Geon(TL) & Gon(BR) lie on the main diagonal -> bars parallel to anti-diagonal (-33.69)
# Gam(TR) & Ri(BL) lie on the anti-diagonal -> bars parallel to main diagonal (+33.69)
trigrams = (
    trigram(11.4, 7.6, [1, 1, 1], -33.69) +   # Geon  (top-left)
    trigram(48.6, 7.6, [0, 1, 0], 33.69) +    # Gam   (top-right)
    trigram(11.4, 32.4, [1, 0, 1], 33.69) +   # Ri    (bottom-left)
    trigram(48.6, 32.4, [0, 0, 0], -33.69)    # Gon   (bottom-right)
)
kr = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 60 40">'
    '<rect width="60" height="40" fill="#fff"/>'
    '<rect x="1" y="1" width="58" height="38" fill="none" stroke="#e3e8f0" stroke-width="1"/>'
    f'<g transform="rotate(-33.69 {cx} {cy})">'
    f'<path d="{red}" fill="#cd2e3a"/><path d="{blue}" fill="#0047a0"/></g>'
    f'<g fill="#111">{trigrams}</g>'
    '</svg>'
)
open(os.path.join(A, "kr.svg"), "w").write(kr)
print("us + kr flags written")
