#!/bin/zsh
# Generates themed SVG placeholders for the About & Championships pages.
# Swap any file with a real .jpg/.png and update the src in the HTML.
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
  <text x="50%" y="$((h/2+44))" fill="#8b97ad" font-family="Arial, sans-serif" font-size="18" font-weight="700" text-anchor="middle" letter-spacing="1">${label}</text>
</svg>
SVG
}

placeholder about-hero.svg    1600 600 "TAIPEI SKYLINE"
placeholder vision.svg         760 500 "INDUSTRY COLLABORATION"
placeholder champ-hero.svg    1600 600 "CHAMPIONSHIP STAGE"
placeholder dent-tech.svg      680 540 "PDR TECHNICIAN"
placeholder showcase-1.svg     480 340 "LIVE DEMONSTRATIONS"
placeholder showcase-2.svg     480 340 "PRODUCT INNOVATIONS"
placeholder showcase-3.svg     480 340 "SURFACE CARE"
placeholder demo-stage.svg     760 500 "DEMONSTRATION STAGE"
placeholder awards-trophy.svg  460 560 "AWARDS TROPHY"

echo "page-2 placeholders generated"
