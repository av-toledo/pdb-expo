#!/usr/bin/env python3
"""Generate photorealistic images for the homepage via Pollinations (free, no key).
Saves JPEGs into assets/. Cohesive cinematic dark-blue + red brand look."""
import os, ssl, time, urllib.parse, urllib.request

SSL_CTX = ssl._create_unverified_context()  # macOS python lacks CA bundle; images are public

A = os.path.join(os.path.dirname(__file__), "..", "assets")
STYLE = ", cinematic, dark navy blue and red accent lighting, professional, high detail, photorealistic"

JOBS = {
    # filename: (prompt, width, height, seed)
    "hero-tall.jpg": ("a professional automotive technician performing paintless dent repair on a luxury black sports car, holding a metal PDR rod, focused, dramatic studio lighting", 720, 1040, 11),
    "hero-2.jpg":    ("close up of a gloved hand using a dual action polisher on a glossy black car panel, car detailing, reflections", 720, 540, 7),
    "hero-3.jpg":    ("keynote speaker on a modern conference stage presenting to a large audience, business technology summit, big LED screen, stage lights", 720, 540, 23),
    "skyline.jpg":   ("Taipei 101 and city skyline at dusk blue hour, glowing city lights, wide cinematic panorama, moody dark blue sky", 1280, 760, 31),
    "manila.jpg": ("Manila Makati city skyline at dusk, modern glass skyscrapers, Philippines, warm golden-hour light, wide cinematic panorama", 1100, 680, 61),
    "about-hero.jpg": ("premium international automotive expo hall with exhibition booths and a crowd, dramatic red and blue stage lighting, cinematic wide atmosphere", 1600, 660, 63),
    "about-intro.jpg": ("professional paintless dent repair technician inspecting a glossy black luxury car panel under a bright inspection light, premium workshop", 760, 620, 65),
    "why-champ.jpg": ("paintless dent repair championship competition, technician working intensely on a car under bright arena spotlights, gold trophy nearby", 720, 480, 41),
    "why-summit.jpg": ("business and AI summit, professional speaker presenting with futuristic holographic data charts on a large screen, modern conference audience", 720, 480, 47),
    "why-network.jpg": ("diverse group of business professionals networking and shaking hands at a conference, modern venue", 720, 480, 5),
    "why-surface.jpg": ("macro water beading on a freshly ceramic coated glossy black car surface, droplets, sharp reflections", 720, 480, 9),
    "prog-1.jpg":    ("automotive paintless dent repair competition, technician working fast on a car under bright arena lights, intense", 800, 600, 14),
    "prog-2.jpg":    ("row of premium car detailing product bottles and ceramic coatings on a trade show booth table, studio lighting", 800, 600, 18),
    "prog-3.jpg":    ("business seminar workshop, presenter at a podium with an audience taking notes, modern conference room", 800, 600, 27),
    "prog-4.jpg":    ("busy automotive trade show expo hall with exhibitor booths, crowds and banners, bright lighting, wide shot", 800, 600, 33),
}

def fetch(name, prompt, w, h, seed):
    dest = os.path.join(A, name)
    if os.path.exists(dest) and os.path.getsize(dest) > 4000:
        return f"skip (already {os.path.getsize(dest)//1024}KB)"
    url = ("https://image.pollinations.ai/prompt/"
           + urllib.parse.quote(prompt + STYLE)
           + f"?width={w}&height={h}&seed={seed}&nologo=true&model=turbo")
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=180, context=SSL_CTX) as r:
                data = r.read()
            if len(data) < 4000:
                raise ValueError(f"too small ({len(data)}b)")
            open(dest, "wb").write(data)
            return f"ok {len(data)//1024}KB {w}x{h}"
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503) and attempt < 3:
                time.sleep(15)
                continue
            return f"ERROR {e}"
        except Exception as e:
            if attempt < 3:
                time.sleep(8); continue
            return f"ERROR {e}"

for name, (prompt, w, h, seed) in JOBS.items():
    print(f"{name}: {fetch(name, prompt, w, h, seed)}", flush=True)
    time.sleep(5)   # stay under the rate limit
