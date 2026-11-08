#!/usr/bin/env python3
"""Extract Taiwan's real coastline from Natural Earth 10m land and emit a
clean, glowing SVG silhouette -> assets/taiwan-map.svg"""
import json, math, os

SRC = "/tmp/ne_10m_land.geojson"
OUT = os.path.join(os.path.dirname(__file__), "..", "assets", "taiwan-map.svg")

# Main-island bounding box (excludes Penghu/Kinmen/Matsu so the shape is clean)
LON0, LON1, LAT0, LAT1 = 120.0, 122.05, 21.85, 25.35

def rings_of(geom):
    t = geom["type"]
    if t == "Polygon":
        for r in geom["coordinates"]:
            yield r
    elif t == "MultiPolygon":
        for poly in geom["coordinates"]:
            for r in poly:
                yield r

gj = json.load(open(SRC))
best = None
for feat in gj["features"]:
    for ring in rings_of(feat["geometry"]):
        if all(LON0 <= x <= LON1 and LAT0 <= y <= LAT1 for x, y in ring):
            if best is None or len(ring) > len(best):
                best = ring
if not best:
    raise SystemExit("Taiwan ring not found")

lons = [p[0] for p in best]; lats = [p[1] for p in best]
lon_min, lon_max = min(lons), max(lons)
lat_min, lat_max = min(lats), max(lats)
lat_mean = math.radians((lat_min + lat_max) / 2)
sx = math.cos(lat_mean)                      # longitude foreshortening

H, PAD = 360.0, 26.0
h_raw = lat_max - lat_min
scale = (H - 2 * PAD) / h_raw
W = (lon_max - lon_min) * sx * scale + 2 * PAD

def project(lon, lat):
    X = PAD + (lon - lon_min) * sx * scale
    Y = PAD + (lat_max - lat) * scale
    return round(X, 1), round(Y, 1)

pts = [project(x, y) for x, y in best]
d = "M" + " L".join(f"{x} {y}" for x, y in pts) + " Z"
# Taipei (host city) marker
tx, ty = project(121.565, 25.033)
Wr = round(W, 1)

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {Wr} {round(H,1)}" role="img" aria-label="Taiwan — host location">
  <defs>
    <radialGradient id="tw-glow" cx="50%" cy="46%" r="60%">
      <stop offset="0" stop-color="#ff3651" stop-opacity="0.55"/>
      <stop offset="0.55" stop-color="#d8203a" stop-opacity="0.16"/>
      <stop offset="1" stop-color="#d8203a" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="tw-fill" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#ec2c46"/>
      <stop offset="1" stop-color="#9c1424"/>
    </linearGradient>
    <filter id="tw-shadow" x="-60%" y="-60%" width="220%" height="220%">
      <feDropShadow dx="0" dy="0" stdDeviation="9" flood-color="#ff2d4a" flood-opacity="0.75"/>
    </filter>
  </defs>
  <ellipse cx="{round(Wr/2,1)}" cy="{round(H*0.5,1)}" rx="{round(Wr*0.46,1)}" ry="{round(H*0.44,1)}" fill="url(#tw-glow)"/>
  <path d="{d}" fill="url(#tw-fill)" stroke="#ff7286" stroke-width="1.3"
        stroke-linejoin="round" filter="url(#tw-shadow)"/>
  <g>
    <!-- radar ping -->
    <circle cx="{tx}" cy="{ty}" r="4" fill="none" stroke="#fff" stroke-width="1.8">
      <animate attributeName="r" values="4;18" dur="3.4s" repeatCount="indefinite" calcMode="spline" keyTimes="0;1" keySplines="0.2 0.6 0.3 1"/>
      <animate attributeName="opacity" values="0.9;0" dur="3.4s" repeatCount="indefinite"/>
      <animate attributeName="stroke-width" values="2;0.3" dur="3.4s" repeatCount="indefinite"/>
    </circle>
    <!-- soft beating halo -->
    <circle cx="{tx}" cy="{ty}" r="7" fill="#fff" opacity="0.28">
      <animate attributeName="r" values="5.5;9.5;5.5" dur="2.2s" repeatCount="indefinite" calcMode="spline" keyTimes="0;0.3;1" keySplines="0.2 0.7 0.3 1;0.4 0 0.6 1"/>
      <animate attributeName="opacity" values="0.34;0.04;0.34" dur="2.2s" repeatCount="indefinite"/>
    </circle>
    <!-- beating core -->
    <circle cx="{tx}" cy="{ty}" r="3.6" fill="#fff">
      <animate attributeName="r" values="3.2;5;3.2" dur="2.2s" repeatCount="indefinite" calcMode="spline" keyTimes="0;0.3;1" keySplines="0.2 0.7 0.3 1;0.4 0 0.6 1"/>
    </circle>
    <!-- label -->
    <text x="{tx}" y="{round(ty-12,1)}" text-anchor="middle" font-family="Arial, Helvetica, sans-serif"
          font-size="11.5" font-weight="500" letter-spacing="0.3" fill="#ffffff"
          stroke="#0a0f1c" stroke-width="2.6" paint-order="stroke" stroke-linejoin="round">Taipei</text>
  </g>
</svg>
'''
open(OUT, "w").write(svg)
print(f"points={len(pts)} W={Wr} H={H} taipei=({tx},{ty})")
