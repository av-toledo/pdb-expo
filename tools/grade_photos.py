#!/usr/bin/env python3
"""Apply one consistent, subtle film grade to every photo so the set feels like a
cohesive shoot (not raw AI renders). Desaturate a touch, gentle contrast, warm
split-tone, fine grain. Run ONCE after gen_photos.py."""
import glob, os
from PIL import Image, ImageEnhance, ImageChops

A = os.path.join(os.path.dirname(__file__), "..", "assets")

def grade(path):
    im = Image.open(path).convert("RGB")
    w, h = im.size
    im = ImageEnhance.Color(im).enhance(0.90)      # slightly desaturate
    im = ImageEnhance.Contrast(im).enhance(1.05)   # gentle contrast
    im = ImageEnhance.Brightness(im).enhance(0.99)
    # warm highlights / cooler blues (subtle split-tone)
    r, g, b = im.split()
    r = r.point(lambda x: min(255, int(x + 6)))
    b = b.point(lambda x: max(0, int(x - 5)))
    im = Image.merge("RGB", (r, g, b))
    # fine grain via mid-grey noise overlay, blended very low
    noise = Image.effect_noise((w, h), 16).convert("L")
    noise = Image.merge("RGB", (noise, noise, noise))
    im = Image.blend(im, ImageChops.overlay(im, noise), 0.06)
    im.save(path, quality=88, optimize=True)

n = 0
for p in sorted(glob.glob(os.path.join(A, "*.jpg"))):
    grade(p); n += 1
    print("graded", os.path.basename(p))
print(f"done: {n} images")
