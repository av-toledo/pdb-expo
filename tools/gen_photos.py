#!/usr/bin/env python3
"""Regenerate site photos with a NATURAL, editorial look (not neon/AI-cinematic).
Pollinations (free). A unified film grade is applied afterwards by grade_photos.py."""
import os, ssl, time, urllib.parse, urllib.request

SSL_CTX = ssl._create_unverified_context()
A = os.path.join(os.path.dirname(__file__), "..", "assets")
MODEL = "flux"  # flux = more photoreal; falls back handled by retry
STYLE = (", natural soft daylight, realistic true-to-life muted colours, shallow depth of field, "
         "candid editorial documentary photograph, 35mm, fine detail, no text")

JOBS = {
    "hero-tall.jpg":   ("a focused automotive technician carefully repairing a small dent on a dark car body panel in a clean professional workshop, natural window light", 720, 1040, 101),
    "hero-2.jpg":      ("close up of a detailer's gloved hand buffing a polished car panel, soft natural daylight, subtle reflections", 720, 540, 102),
    "hero-3.jpg":      ("a speaker presenting at a professional business summit on a stage with a seated audience, warm natural ambient light", 720, 540, 103),
    "skyline.jpg":     ("Manila Makati skyline at golden hour, modern skyscrapers, soft warm daylight, realistic wide cityscape photograph", 1280, 760, 104),
    "why-champ.jpg":   ("an automotive technician concentrating while repairing a car dent at a skills competition, professional workshop, natural light", 720, 480, 105),
    "why-network.jpg": ("business professionals in smart attire talking and networking at a conference, candid, soft natural indoor light", 720, 480, 106),
    "why-summit.jpg":  ("attendees at a business seminar in a modern conference room listening to a presenter, natural light", 720, 480, 107),
    "why-surface.jpg": ("macro close up of water droplets beading on a freshly polished glossy car surface, soft daylight", 720, 480, 108),
    "prog-1.jpg":      ("an automotive paintless dent repair technician working carefully on a car panel, professional workshop, natural light", 800, 600, 109),
    "prog-2.jpg":      ("a tidy display of car detailing products and hand tools on a table at an industry trade show booth, soft even lighting", 800, 600, 110),
    "prog-3.jpg":      ("people collaborating at a professional business workshop around a table in a modern venue, natural light", 800, 600, 111),
    "prog-4.jpg":      ("a busy automotive trade exhibition hall with booths and visitors walking, natural ambient lighting, wide documentary photograph", 800, 600, 112),
    "about-hero.jpg":  ("wide interior view of a modern automotive trade exhibition hall with booths and attendees, natural ambient daylight", 1600, 660, 113),
    "about-intro.jpg": ("an automotive technician inspecting the panel of a car in a professional workshop, natural window light, candid", 760, 620, 114),
    "manila.jpg":      ("Manila Makati skyline at golden hour, modern skyscrapers along the bay, warm soft daylight, realistic wide cityscape photograph", 1100, 680, 115),
}

def fetch(name, prompt, w, h, seed):
    dest = os.path.join(A, name)
    url = ("https://image.pollinations.ai/prompt/"
           + urllib.parse.quote(prompt + STYLE)
           + f"?width={w}&height={h}&seed={seed}&nologo=true&model={MODEL}")
    for attempt in range(5):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=200, context=SSL_CTX) as r:
                data = r.read()
            if len(data) < 4000:
                raise ValueError(f"too small ({len(data)}b)")
            open(dest, "wb").write(data)
            return f"ok {len(data)//1024}KB {w}x{h}"
        except urllib.error.HTTPError as e:
            if e.code in (429, 402, 500, 502, 503) and attempt < 4:
                time.sleep(16); continue
            return f"ERROR {e}"
        except Exception as e:
            if attempt < 4:
                time.sleep(8); continue
            return f"ERROR {e}"

for name, (prompt, w, h, seed) in JOBS.items():
    print(f"{name}: {fetch(name, prompt, w, h, seed)}", flush=True)
    time.sleep(5)
