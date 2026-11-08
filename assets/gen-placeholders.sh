#!/bin/zsh
# Generates themed SVG placeholders so the page renders before real photos exist.
# Swap any file in /assets with a real .jpg/.png and update the src in index.html.
cd "$(dirname "$0")"

placeholder () {
  local file="$1" w="$2" h="$3" label="$4"
  cat > "$file" <<SVG
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${w} ${h}" preserveAspectRatio="xMidYMid slice" role="img" aria-label="${label}">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#16203a"/>
      <stop offset="1" stop-color="#0b1120"/>
    </linearGradient>
  </defs>
  <rect width="${w}" height="${h}" fill="url(#g)"/>
  <rect x="6" y="6" width="$((w-12))" height="$((h-12))" fill="none" stroke="#27324d" stroke-width="2" rx="10"/>
  <g opacity="0.9">
    <circle cx="$((w/2))" cy="$((h/2-18))" r="20" fill="none" stroke="#d8203a" stroke-width="3"/>
    <rect x="$((w/2-26))" y="$((h/2+12))" width="52" height="6" rx="3" fill="#33425f"/>
  </g>
  <text x="50%" y="$((h/2+44))" fill="#8b97ad" font-family="Arial, sans-serif" font-size="16" font-weight="700" text-anchor="middle" letter-spacing="1">${label}</text>
</svg>
SVG
}

placeholder hero-tall.svg   520 760 "TECHNICIAN / HERO"
placeholder hero-2.svg      520 360 "POLISHING DETAIL"
placeholder hero-3.svg      520 360 "SUMMIT STAGE"
placeholder why-network.svg 360 240 "NETWORKING"
placeholder why-surface.svg 360 240 "SURFACE CARE"
placeholder prog-1.svg      400 300 "PDR COMPETITION"
placeholder prog-2.svg      400 300 "LIVE DEMOS"
placeholder prog-3.svg      400 300 "SEMINARS"
placeholder prog-4.svg      400 300 "INDUSTRY EXPO"
placeholder skyline.svg     700 900 "TAIPEI SKYLINE"

echo "placeholders generated"
