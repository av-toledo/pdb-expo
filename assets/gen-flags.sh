#!/bin/zsh
# Generates simplified region flags (60x40) for the About page participation row.
# Recognizable placeholders — swap for accurate flag art anytime.
cd "$(dirname "$0")"
mkdir -p flags

# United States
cat > flags/us.svg <<'SVG'
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 60 40">
  <rect width="60" height="40" fill="#b22234"/>
  <g fill="#fff"><rect y="3.1" width="60" height="3.1"/><rect y="9.2" width="60" height="3.1"/><rect y="15.4" width="60" height="3.1"/><rect y="21.5" width="60" height="3.1"/><rect y="27.7" width="60" height="3.1"/><rect y="33.8" width="60" height="3.1"/></g>
  <rect width="26" height="21.5" fill="#3c3b6e"/>
  <g fill="#fff"><circle cx="5" cy="4" r="1"/><circle cx="11" cy="4" r="1"/><circle cx="17" cy="4" r="1"/><circle cx="23" cy="4" r="1"/><circle cx="8" cy="8" r="1"/><circle cx="14" cy="8" r="1"/><circle cx="20" cy="8" r="1"/><circle cx="5" cy="12" r="1"/><circle cx="11" cy="12" r="1"/><circle cx="17" cy="12" r="1"/><circle cx="23" cy="12" r="1"/><circle cx="8" cy="16" r="1"/><circle cx="14" cy="16" r="1"/><circle cx="20" cy="16" r="1"/></g>
</svg>
SVG

# Europe
cat > flags/eu.svg <<'SVG'
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 60 40">
  <defs>
    <path id="eu-star" fill="#ffcc00" d="M0,-3 L0.71,-0.97 L2.85,-0.93 L1.14,0.37 L1.76,2.43 L0,1.2 L-1.76,2.43 L-1.14,0.37 L-2.85,-0.93 L-0.71,-0.97 Z"/>
  </defs>
  <rect width="60" height="40" fill="#003399"/>
  <use href="#eu-star" x="42" y="20"/><use href="#eu-star" x="40.4" y="26"/><use href="#eu-star" x="36" y="30.4"/>
  <use href="#eu-star" x="30" y="32"/><use href="#eu-star" x="24" y="30.4"/><use href="#eu-star" x="19.6" y="26"/>
  <use href="#eu-star" x="18" y="20"/><use href="#eu-star" x="19.6" y="14"/><use href="#eu-star" x="24" y="9.6"/>
  <use href="#eu-star" x="30" y="8"/><use href="#eu-star" x="36" y="9.6"/><use href="#eu-star" x="40.4" y="14"/>
</svg>
SVG

# South America (Brazil)
cat > flags/br.svg <<'SVG'
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 60 40">
  <rect width="60" height="40" fill="#009c3b"/>
  <polygon points="30,5 55,20 30,35 5,20" fill="#ffdf00"/>
  <circle cx="30" cy="20" r="8" fill="#002776"/>
  <path d="M22 18 q8 -4 16 1" stroke="#fff" stroke-width="1.4" fill="none"/>
</svg>
SVG

# Japan
cat > flags/jp.svg <<'SVG'
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 60 40">
  <rect width="60" height="40" fill="#fff"/>
  <rect x="1" y="1" width="58" height="38" fill="none" stroke="#e3e8f0" stroke-width="1"/>
  <circle cx="30" cy="20" r="11" fill="#bc002d"/>
</svg>
SVG

# South Korea (taegeuk + four trigrams)
cat > flags/kr.svg <<'SVG'
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 60 40">
  <rect width="60" height="40" fill="#fff"/>
  <rect x="1" y="1" width="58" height="38" fill="none" stroke="#e3e8f0" stroke-width="1"/>
  <!-- taegeuk: red top, blue bottom -->
  <circle cx="30" cy="20" r="9.5" fill="#cd2e3a"/>
  <path d="M20.5 20 A9.5 9.5 0 0 0 39.5 20 A4.75 4.75 0 0 0 30 20 A4.75 4.75 0 0 1 20.5 20 Z" fill="#0047a0"/>
  <!-- trigrams (simplified, hoist=top-left Geon / fly=bottom-right Gon) -->
  <g fill="#222">
    <!-- top-left: Geon (3 solid) -->
    <g transform="translate(9,7) rotate(33)">
      <rect x="-5.5" y="-3.2" width="11" height="1.5"/><rect x="-5.5" y="-0.75" width="11" height="1.5"/><rect x="-5.5" y="1.7" width="11" height="1.5"/>
    </g>
    <!-- top-right: Gam (broken-solid-broken) -->
    <g transform="translate(51,7) rotate(-33)">
      <rect x="-5.5" y="-3.2" width="4.4" height="1.5"/><rect x="1.1" y="-3.2" width="4.4" height="1.5"/>
      <rect x="-5.5" y="-0.75" width="11" height="1.5"/>
      <rect x="-5.5" y="1.7" width="4.4" height="1.5"/><rect x="1.1" y="1.7" width="4.4" height="1.5"/>
    </g>
    <!-- bottom-left: Ri (solid-broken-solid) -->
    <g transform="translate(9,33) rotate(-33)">
      <rect x="-5.5" y="-3.2" width="11" height="1.5"/>
      <rect x="-5.5" y="-0.75" width="4.4" height="1.5"/><rect x="1.1" y="-0.75" width="4.4" height="1.5"/>
      <rect x="-5.5" y="1.7" width="11" height="1.5"/>
    </g>
    <!-- bottom-right: Gon (3 broken) -->
    <g transform="translate(51,33) rotate(33)">
      <rect x="-5.5" y="-3.2" width="4.4" height="1.5"/><rect x="1.1" y="-3.2" width="4.4" height="1.5"/>
      <rect x="-5.5" y="-0.75" width="4.4" height="1.5"/><rect x="1.1" y="-0.75" width="4.4" height="1.5"/>
      <rect x="-5.5" y="1.7" width="4.4" height="1.5"/><rect x="1.1" y="1.7" width="4.4" height="1.5"/>
    </g>
  </g>
</svg>
SVG

# Taiwan
cat > flags/tw.svg <<'SVG'
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 60 40">
  <rect width="60" height="40" fill="#fe0000"/>
  <rect width="30" height="20" fill="#000095"/>
  <g stroke="#fff" stroke-width="1.4"><line x1="15" y1="3" x2="15" y2="17"/><line x1="8" y1="10" x2="22" y2="10"/><line x1="10" y1="5" x2="20" y2="15"/><line x1="20" y1="5" x2="10" y2="15"/></g>
  <circle cx="15" cy="10" r="4.2" fill="#fff"/>
  <circle cx="15" cy="10" r="3" fill="#000095"/>
</svg>
SVG

# Southeast Asia (Vietnam)
cat > flags/vn.svg <<'SVG'
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 60 40">
  <rect width="60" height="40" fill="#da251d"/>
  <polygon points="30,9 32.6,16.4 40.5,16.6 34.2,21.4 36.5,28.9 30,24.4 23.5,28.9 25.8,21.4 19.5,16.6 27.4,16.4" fill="#ff0"/>
</svg>
SVG

# Australia
cat > flags/au.svg <<'SVG'
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 60 40">
  <defs>
    <path id="au-star" fill="#fff" d="M0,-3 L0.71,-0.97 L2.85,-0.93 L1.14,0.37 L1.76,2.43 L0,1.2 L-1.76,2.43 L-1.14,0.37 L-2.85,-0.93 L-0.71,-0.97 Z"/>
    <clipPath id="au-canton"><rect width="30" height="20"/></clipPath>
  </defs>
  <rect width="60" height="40" fill="#00247d"/>
  <!-- Union Jack canton -->
  <g clip-path="url(#au-canton)">
    <path d="M0,0 L30,20 M30,0 L0,20" stroke="#fff" stroke-width="4.2"/>
    <path d="M0,0 L30,20 M30,0 L0,20" stroke="#cf142b" stroke-width="1.7"/>
    <path d="M15,0 V20 M0,10 H30" stroke="#fff" stroke-width="5"/>
    <path d="M15,0 V20 M0,10 H30" stroke="#cf142b" stroke-width="2.8"/>
  </g>
  <!-- Commonwealth star -->
  <use href="#au-star" transform="translate(15,30) scale(1.75)"/>
  <!-- Southern Cross -->
  <use href="#au-star" transform="translate(47,8.5) scale(1.15)"/>
  <use href="#au-star" transform="translate(39,20) scale(1.15)"/>
  <use href="#au-star" transform="translate(54.5,16.5) scale(1.15)"/>
  <use href="#au-star" transform="translate(47,33) scale(1.15)"/>
  <use href="#au-star" transform="translate(49.5,24.5) scale(0.72)"/>
</svg>
SVG

echo "flags generated"
