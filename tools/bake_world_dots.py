#!/usr/bin/env python3
"""Bake Natural Earth land GeoJSON into a compact dot grid for the canvas map.
Uses a scanline polygon fill (even-odd) so coastlines are real and lakes/holes
are carved out. Output: assets/world-dots.json  ->  {cols, rows, cells:[[c,r],...]}"""
import json, os

SRC = "/tmp/ne_50m_land.geojson"
OUT = os.path.join(os.path.dirname(__file__), "..", "assets", "world-dots.json")

# Visible latitude band (drop most of Antarctica, keep a touch of north)
LAT_TOP, LAT_BOT = 83.0, -56.0
COLS, ROWS = 150, 60            # dot grid resolution (pixel spacing ~ equal)

def lonlat_to_grid(lon, lat):
    fx = (lon + 180.0) / 360.0 * COLS
    fy = (LAT_TOP - lat) / (LAT_TOP - LAT_BOT) * ROWS
    return fx, fy

# ---- collect every ring (exterior + holes) as grid-space polylines ----
edges = []  # (x0,y0,x1,y1)
def add_ring(ring):
    pts = [lonlat_to_grid(p[0], p[1]) for p in ring]
    for i in range(len(pts) - 1):
        x0, y0 = pts[i]; x1, y1 = pts[i + 1]
        if y0 != y1:                       # ignore horizontal edges
            edges.append((x0, y0, x1, y1))

with open(SRC) as f:
    gj = json.load(f)

for feat in gj["features"]:
    geom = feat["geometry"]; t = geom["type"]
    if t == "Polygon":
        for ring in geom["coordinates"]:
            add_ring(ring)
    elif t == "MultiPolygon":
        for poly in geom["coordinates"]:
            for ring in poly:
                add_ring(ring)

# ---- scanline fill (even-odd) ----
cells = []
for r in range(ROWS):
    y = r + 0.5
    xs = []
    for (x0, y0, x1, y1) in edges:
        if (y0 <= y < y1) or (y1 <= y < y0):
            x = x0 + (y - y0) * (x1 - x0) / (y1 - y0)
            xs.append(x)
    xs.sort()
    for i in range(0, len(xs) - 1, 2):
        c0 = max(0, int(xs[i] + 0.5))
        c1 = min(COLS - 1, int(xs[i + 1] - 0.5))
        for c in range(c0, c1 + 1):
            cells.append((c, r))

data = {"cols": COLS, "rows": ROWS, "latTop": LAT_TOP, "latBot": LAT_BOT,
        "cells": cells}
with open(OUT, "w") as f:
    json.dump(data, f, separators=(",", ":"))

print(f"edges={len(edges)} dots={len(cells)} bytes={os.path.getsize(OUT)}")
