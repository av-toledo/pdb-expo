#!/usr/bin/env python3
"""Generate branded vector illustrations for the homepage image slots.
Modern flat/gradient 'spot illustration' style in the PDB Expo palette.
Overwrites the placeholder SVGs of the same name in assets/."""
import os
A = os.path.join(os.path.dirname(__file__), "..", "assets")

def svg(w, h, defs, body, label=None):
    lab = label.replace("&", "&amp;") if label else label
    cap = f'<text x="{w/2}" y="{h-16}" text-anchor="middle" fill="#7f8aa1" font-family="Arial,sans-serif" font-size="13" font-weight="700" letter-spacing="2">{lab}</text>' if label else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
            f'preserveAspectRatio="xMidYMid slice" role="img"{f" aria-label=\"{lab}\"" if label else ""}>'
            f'<defs>{COMMON_DEFS}{defs}</defs>'
            f'<rect width="{w}" height="{h}" fill="url(#bg)"/>'
            f'<rect width="{w}" height="{h}" fill="url(#vig)"/>'
            f'{body}{cap}</svg>')

COMMON_DEFS = (
    '<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">'
    '<stop offset="0" stop-color="#101c33"/><stop offset="1" stop-color="#070b15"/></linearGradient>'
    '<radialGradient id="vig" cx="50%" cy="38%" r="75%">'
    '<stop offset="0" stop-color="#1b2c4d" stop-opacity="0.55"/>'
    '<stop offset="1" stop-color="#070b15" stop-opacity="0"/></radialGradient>'
    '<linearGradient id="steel" x1="0" y1="0" x2="0" y2="1">'
    '<stop offset="0" stop-color="#3a4a6b"/><stop offset="1" stop-color="#141d31"/></linearGradient>'
    '<linearGradient id="red" x1="0" y1="0" x2="1" y2="1">'
    '<stop offset="0" stop-color="#ff5a72"/><stop offset="1" stop-color="#b3162c"/></linearGradient>'
    '<radialGradient id="redglow" cx="50%" cy="50%" r="50%">'
    '<stop offset="0" stop-color="#ff3651" stop-opacity="0.7"/>'
    '<stop offset="1" stop-color="#ff3651" stop-opacity="0"/></radialGradient>'
)

def write(name, content):
    open(os.path.join(A, name), "w").write(content)

# ---------------------------------------------------------------- HERO TALL
# Sports-car side silhouette with red rim light + technician + work light.
hero_tall = svg(520, 760, '', '''
  <ellipse cx="260" cy="430" rx="250" ry="150" fill="url(#redglow)" opacity="0.5"/>
  <!-- light streaks -->
  <g stroke="#ff5a72" stroke-width="3" opacity="0.5" stroke-linecap="round">
    <line x1="60" y1="120" x2="240" y2="150"/><line x1="300" y1="95" x2="470" y2="135"/>
    <line x1="120" y1="200" x2="210" y2="212"/>
  </g>
  <!-- car body (side profile, sporty) -->
  <g>
    <path d="M40 470
             C70 420 120 392 190 388
             C235 360 300 356 350 386
             C420 392 470 410 486 452
             L488 506 L40 506 Z" fill="url(#steel)" stroke="#46587e" stroke-width="2"/>
    <!-- greenhouse / windows -->
    <path d="M196 392 C232 372 300 370 340 390 L322 430 L214 430 Z" fill="#0c1322" />
    <path d="M196 392 C232 372 300 370 340 390 L322 430 L214 430 Z" fill="#0c1322"/>
    <!-- red rim light along top -->
    <path d="M40 470 C70 420 120 392 190 388 C235 360 300 356 350 386 C420 392 470 410 486 452"
          fill="none" stroke="url(#red)" stroke-width="4" stroke-linecap="round"/>
    <!-- headlight -->
    <path d="M470 442 l18 6 -2 16 -18 -4 z" fill="#ffd9df"/>
    <circle cx="478" cy="452" r="16" fill="url(#redglow)"/>
    <!-- wheels -->
    <circle cx="150" cy="506" r="46" fill="#0a0f1c" stroke="#46587e" stroke-width="3"/>
    <circle cx="150" cy="506" r="20" fill="#1b2740" stroke="#5a6c92" stroke-width="2"/>
    <circle cx="382" cy="506" r="46" fill="#0a0f1c" stroke="#46587e" stroke-width="3"/>
    <circle cx="382" cy="506" r="20" fill="#1b2740" stroke="#5a6c92" stroke-width="2"/>
  </g>
  <!-- technician silhouette working on the door panel -->
  <g fill="#0a0f1c" stroke="#46587e" stroke-width="2">
    <circle cx="262" cy="300" r="26"/>
    <path d="M226 360 C226 322 298 322 298 360 L296 470 L228 470 Z"/>
  </g>
  <!-- arm + PDR rod to panel -->
  <path d="M286 372 L344 432" stroke="#aebacd" stroke-width="7" stroke-linecap="round"/>
  <circle cx="344" cy="432" r="6" fill="#ff5a72"/>
  <circle cx="344" cy="432" r="16" fill="url(#redglow)"/>
''', "TECHNICIAN")
write("hero-tall.svg", hero_tall)

# ---------------------------------------------------------------- HERO 2
# Dual-action polisher on a curved glossy panel.
hero_2 = svg(520, 360, '', '''
  <!-- glossy panel -->
  <path d="M0 250 C160 180 360 180 520 250 L520 360 L0 360 Z" fill="url(#steel)"/>
  <path d="M0 250 C160 180 360 180 520 250" fill="none" stroke="#5a6c92" stroke-width="2"/>
  <!-- reflection streak -->
  <path d="M70 286 C200 250 330 250 460 286" fill="none" stroke="#9fb0cf" stroke-width="5" opacity="0.5" stroke-linecap="round"/>
  <!-- polisher -->
  <g>
    <ellipse cx="300" cy="232" rx="78" ry="26" fill="#0a0f1c"/>
    <ellipse cx="300" cy="230" rx="78" ry="26" fill="#0e1626" stroke="#46587e" stroke-width="2"/>
    <ellipse cx="300" cy="226" rx="70" ry="20" fill="url(#red)"/>
    <rect x="288" y="150" width="24" height="70" rx="10" fill="#1b2740" stroke="#46587e" stroke-width="2"/>
    <rect x="272" y="132" width="120" height="26" rx="13" fill="#26334f" stroke="#46587e" stroke-width="2"/>
  </g>
  <!-- motion arcs -->
  <g fill="none" stroke="#ff5a72" stroke-width="3" opacity="0.6" stroke-linecap="round">
    <path d="M214 248 a92 30 0 0 0 172 0"/>
    <path d="M232 264 a70 22 0 0 0 136 0" opacity="0.4"/>
  </g>
  <ellipse cx="300" cy="248" rx="120" ry="42" fill="url(#redglow)" opacity="0.4"/>
''', "PAINT & SURFACE")
write("hero-2.svg", hero_2)

# ---------------------------------------------------------------- HERO 3
# Stage with spotlight beams + speaker + audience.
hero_3 = svg(520, 360, '', '''
  <!-- beams -->
  <g opacity="0.5">
    <polygon points="150,0 110,300 250,300" fill="url(#redglow)"/>
    <polygon points="370,0 290,300 430,300" fill="url(#redglow)"/>
    <polygon points="260,0 220,300 320,300" fill="#3b62d8" opacity="0.35"/>
  </g>
  <!-- stage floor -->
  <rect x="0" y="286" width="520" height="74" fill="#0a0f1c"/>
  <path d="M0 286 L520 286" stroke="#46587e" stroke-width="2"/>
  <!-- screen -->
  <rect x="150" y="70" width="220" height="120" rx="6" fill="#0e1626" stroke="#46587e" stroke-width="2"/>
  <path d="M170 160 l40 -36 30 22 36 -44 38 58" fill="none" stroke="#ff5a72" stroke-width="3"/>
  <!-- speaker -->
  <g fill="#0a0f1c" stroke="#46587e" stroke-width="2">
    <circle cx="410" cy="214" r="16"/>
    <path d="M388 250 C388 224 432 224 432 250 L430 300 L390 300 Z"/>
  </g>
  <rect x="356" y="262" width="34" height="44" rx="4" fill="#1b2740" stroke="#46587e" stroke-width="2"/>
  <!-- audience -->
  <g fill="#0c1322">''' + "".join(
    f'<circle cx="{40+i*52}" cy="338" r="15" fill="#10192e"/>' for i in range(9)
  ) + '''</g>
''', "SUMMIT STAGE")
write("hero-3.svg", hero_3)

# ---------------------------------------------------------------- WHY NETWORK
why_network = svg(360, 240, '', '''
  <!-- connection lines -->
  <g stroke="#ff5a72" stroke-width="2" opacity="0.5">
    <line x1="96" y1="150" x2="180" y2="120"/><line x1="180" y1="120" x2="264" y2="150"/>
    <line x1="96" y1="150" x2="264" y2="150"/>
  </g>
  <g stroke="#3b62d8" stroke-width="2" opacity="0.4">
    <line x1="180" y1="120" x2="180" y2="186"/>
  </g>
  <!-- people -->
  ''' + "".join(
    f'<g fill="url(#steel)" stroke="#5a6c92" stroke-width="2">'
    f'<circle cx="{cx}" cy="{cy}" r="20"/>'
    f'<path d="M{cx-28} {cy+78} C{cx-28} {cy+30} {cx+28} {cy+30} {cx+28} {cy+78} Z"/></g>'
    f'<circle cx="{cx}" cy="{cy}" r="26" fill="url(#redglow)" opacity="0.5"/>'
    for cx, cy in [(96, 150), (264, 150), (180, 110)]
  ) + '', "NETWORKING")
write("why-network.svg", why_network)

# ---------------------------------------------------------------- WHY SURFACE
why_surface = svg(360, 240, '', '''
  <!-- glossy surface -->
  <rect x="0" y="150" width="360" height="90" fill="url(#steel)"/>
  <path d="M0 150 H360" stroke="#5a6c92" stroke-width="2"/>
  <!-- beading droplet -->
  <path d="M150 150 a40 40 0 0 1 60 0 C214 120 196 92 180 78 C164 92 146 120 150 150 Z" fill="#1b2740" stroke="#5a6c92" stroke-width="2"/>
  <ellipse cx="168" cy="116" rx="10" ry="16" fill="#9fb0cf" opacity="0.7"/>
  <circle cx="196" cy="132" r="4" fill="#ffffff" opacity="0.8"/>
  <!-- small droplets -->
  <circle cx="96" cy="150" r="12" fill="#1b2740" stroke="#5a6c92" stroke-width="1.5"/>
  <circle cx="266" cy="150" r="16" fill="#1b2740" stroke="#5a6c92" stroke-width="1.5"/>
  <!-- sparkle -->
  <g stroke="#ff5a72" stroke-width="2" stroke-linecap="round">
    <path d="M230 70 v16 M222 78 h16"/></g>
  <ellipse cx="180" cy="150" rx="120" ry="34" fill="url(#redglow)" opacity="0.3"/>
''', "SURFACE CARE")
write("why-surface.svg", why_surface)

# ---------------------------------------------------------------- PROG 1 (trophy)
prog_1 = svg(400, 300, '', '''
  <g opacity="0.6"><polygon points="120,0 90,210 200,210" fill="url(#redglow)"/>
  <polygon points="280,0 200,210 310,210" fill="url(#redglow)"/></g>
  <ellipse cx="200" cy="246" rx="120" ry="26" fill="url(#redglow)" opacity="0.5"/>
  <!-- trophy -->
  <g fill="url(#red)" stroke="#ff8090" stroke-width="2">
    <path d="M150 70 h100 v22 a50 50 0 0 1 -100 0 z"/>
    <path d="M150 78 h-22 a18 18 0 0 0 18 22" fill="none" stroke="#ff8090" stroke-width="4"/>
    <path d="M250 78 h22 a18 18 0 0 1 -18 22" fill="none" stroke="#ff8090" stroke-width="4"/>
    <rect x="190" y="138" width="20" height="34"/>
    <rect x="160" y="172" width="80" height="14" rx="3"/>
    <rect x="172" y="186" width="56" height="20" rx="3"/>
  </g>
  <!-- podium -->
  <rect x="150" y="210" width="100" height="40" fill="#1b2740" stroke="#46587e" stroke-width="2"/>
  <g fill="#ffd9df"><circle cx="120" cy="60" r="3"/><circle cx="300" cy="80" r="3"/><circle cx="250" cy="40" r="2.5"/><circle cx="150" cy="40" r="2.5"/></g>
''', "PDR COMPETITION")
write("prog-1.svg", prog_1)

# ---------------------------------------------------------------- PROG 2 (products)
prog_2 = svg(400, 300, '', '''
  <rect x="0" y="210" width="400" height="90" fill="url(#steel)"/>
  <path d="M0 210 H400" stroke="#5a6c92" stroke-width="2"/>
  ''' + "".join(
    f'<g><rect x="{x}" y="{y}" width="{w}" height="{210-y}" rx="8" fill="#1b2740" stroke="#5a6c92" stroke-width="2"/>'
    f'<rect x="{x+w/2-7}" y="{y-16}" width="14" height="18" rx="3" fill="#26334f" stroke="#5a6c92" stroke-width="1.5"/>'
    f'<rect x="{x+6}" y="{y+22}" width="{w-12}" height="34" rx="4" fill="url(#red)" opacity="0.85"/></g>'
    for x, y, w in [(96, 96, 40), (150, 70, 46), (212, 86, 42), (268, 110, 38)]
  ) + '''
  <path d="M120 150 q80 -30 170 0" fill="none" stroke="#9fb0cf" stroke-width="3" opacity="0.4"/>
''', "LIVE DEMOS")
write("prog-2.svg", prog_2)

# ---------------------------------------------------------------- PROG 3 (seminar/AI)
prog_3 = svg(400, 300, '', '''
  <!-- screen with chart -->
  <rect x="70" y="50" width="260" height="150" rx="8" fill="#0e1626" stroke="#46587e" stroke-width="2"/>
  <g fill="url(#red)" opacity="0.9">
    <rect x="100" y="150" width="26" height="30"/><rect x="138" y="128" width="26" height="52"/>
    <rect x="176" y="104" width="26" height="76"/><rect x="214" y="120" width="26" height="60"/>
  </g>
  <path d="M100 150 l38 -22 38 -24 38 16 56 -28" fill="none" stroke="#ff5a72" stroke-width="3"/>
  <!-- AI node motif -->
  <g stroke="#3b62d8" stroke-width="2" opacity="0.7"><circle cx="288" cy="92" r="6" fill="#3b62d8"/>
  <line x1="288" y1="92" x2="262" y2="120"/><line x1="288" y1="92" x2="300" y2="128"/></g>
  <!-- audience -->
  <g fill="#10192e">''' + "".join(
    f'<circle cx="{56+i*40}" cy="250" r="16"/>' for i in range(8)
  ) + '''</g>
  <rect x="0" y="266" width="400" height="34" fill="#0a0f1c"/>
''', "SEMINARS")
write("prog-3.svg", prog_3)

# ---------------------------------------------------------------- PROG 4 (expo hall)
prog_4 = svg(400, 300, '', '''
  <!-- perspective floor -->
  <polygon points="0,300 400,300 300,150 100,150" fill="#0c1326"/>
  <polygon points="0,300 400,300 300,150 100,150" fill="#0c1326"/>
  <line x1="200" y1="150" x2="200" y2="300" stroke="#22304d" stroke-width="2"/>
  <line x1="100" y1="150" x2="0" y2="300" stroke="#22304d" stroke-width="1.5"/>
  <line x1="300" y1="150" x2="400" y2="300" stroke="#22304d" stroke-width="1.5"/>
  <!-- booths -->
  <g fill="url(#steel)" stroke="#46587e" stroke-width="2">
    <rect x="60" y="120" width="90" height="70" rx="4"/>
    <rect x="250" y="120" width="90" height="70" rx="4"/>
  </g>
  <!-- banners -->
  <rect x="70" y="96" width="70" height="16" rx="3" fill="url(#red)"/>
  <rect x="260" y="96" width="70" height="16" rx="3" fill="#3b62d8"/>
  <!-- arch banner -->
  <rect x="150" y="60" width="100" height="20" rx="4" fill="url(#red)"/>
  <!-- people dots -->
  <g fill="#10192e"><circle cx="180" cy="240" r="12"/><circle cx="220" cy="250" r="12"/><circle cx="150" cy="265" r="12"/><circle cx="260" cy="262" r="12"/></g>
''', "INDUSTRY EXPO")
write("prog-4.svg", prog_4)

print("illustrations generated: hero-tall, hero-2, hero-3, why-network, why-surface, prog-1..4")
