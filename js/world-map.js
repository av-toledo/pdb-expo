/* ===========================================================
   PDB Expo — Animated Global Participation map
   Real Natural Earth coastlines baked to a dot grid
   (assets/world-dots.json) + pulsing city markers with
   on-map labels + animated connection arcs from Taiwan.
   Pure canvas, no libraries.
   =========================================================== */
(function () {
  const canvas = document.getElementById('world-canvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  /* ---- Projection band must match the baker (bake_world_dots.py) ---- */
  const LAT_TOP = 83, LAT_BOT = -56;
  const proj = (lon, lat) => ({
    x: (lon + 180) / 360 * W,
    y: (LAT_TOP - lat) / (LAT_TOP - LAT_BOT) * H,
  });

  /* ---- Participating regions ----
     label.pos avoids overlap in the dense East-Asia cluster. */
  const HUB = { name: 'TAIWAN', lon: 121, lat: 23.7, hub: true, pos: 'below' };
  const MARKERS = [
    { name: 'UNITED STATES', lon: -98, lat: 39, pos: 'below' },
    { name: 'EUROPE', lon: 12, lat: 50, pos: 'above' },
    { name: 'SOUTH AMERICA', lon: -58, lat: -12, pos: 'below' },
    { name: 'JAPAN', lon: 139, lat: 37, pos: 'right' },
    { name: 'SOUTH KOREA', lon: 127.5, lat: 37, pos: 'left' },
    HUB,
    { name: 'SOUTHEAST ASIA', lon: 104, lat: 9, pos: 'below' },
    { name: 'AUSTRALIA', lon: 134, lat: -25, pos: 'below' },
  ];
  // particles travel from each region toward Taiwan (the hub)
  const ARCS = MARKERS.filter((m) => !m.hub).map((m) => ({ a: m, b: HUB }));

  /* ---- State ---- */
  let W = 0, H = 0, dpr = 1, grid = null, landLayer = null;

  /* Pre-render the (static) land dots to an offscreen canvas once per size. */
  function buildLand() {
    const rect = canvas.getBoundingClientRect();
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    W = Math.max(1, rect.width); H = Math.max(1, rect.height);
    canvas.width = Math.round(W * dpr);
    canvas.height = Math.round(H * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    if (!grid) return;

    const off = document.createElement('canvas');
    off.width = canvas.width; off.height = canvas.height;
    const o = off.getContext('2d');
    o.setTransform(dpr, 0, 0, dpr, 0, 0);

    const cw = W / grid.cols, ch = H / grid.rows;
    const dotR = Math.max(0.9, Math.min(cw, ch) * 0.34);
    const cx = W / 2, cy = H / 2, maxd = Math.hypot(cx, cy);
    for (let i = 0; i < grid.cells.length; i++) {
      const c = grid.cells[i][0], r = grid.cells[i][1];
      const x = (c + 0.5) * cw, y = (r + 0.5) * ch;
      // brighter toward the centre of the map for depth
      const fall = 1 - Math.hypot(x - cx, y - cy) / maxd;
      o.fillStyle = `rgba(120,150,205,${0.22 + fall * 0.30})`;
      o.beginPath();
      o.arc(x, y, dotR, 0, Math.PI * 2);
      o.fill();
    }
    landLayer = off;
  }

  /* ---- Animated frame ---- */
  let raf = null;
  function frame(t) {
    const time = t / 1000;
    ctx.clearRect(0, 0, W, H);

    if (landLayer) ctx.drawImage(landLayer, 0, 0, W, H);

    // connection arcs + travelling pulse
    for (let i = 0; i < ARCS.length; i++) {
      const a = proj(ARCS[i].a.lon, ARCS[i].a.lat);
      const b = proj(ARCS[i].b.lon, ARCS[i].b.lat);
      const mx = (a.x + b.x) / 2, my = (a.y + b.y) / 2;
      const dist = Math.hypot(b.x - a.x, b.y - a.y);
      const cx = mx, cy = my - Math.min(dist * 0.32, 90);

      const grad = ctx.createLinearGradient(a.x, a.y, b.x, b.y);
      grad.addColorStop(0, 'rgba(216,32,58,0.04)');
      grad.addColorStop(0.5, 'rgba(216,32,58,0.5)');
      grad.addColorStop(1, 'rgba(216,32,58,0.04)');
      ctx.strokeStyle = grad;
      ctx.lineWidth = 1.3;
      ctx.beginPath();
      ctx.moveTo(a.x, a.y);
      ctx.quadraticCurveTo(cx, cy, b.x, b.y);
      ctx.stroke();

      const tt = ((time * 0.095 + i * 0.17) % 1), u = 1 - tt;
      const px = u * u * a.x + 2 * u * tt * cx + tt * tt * b.x;
      const py = u * u * a.y + 2 * u * tt * cy + tt * tt * b.y;
      const pg = ctx.createRadialGradient(px, py, 0, px, py, 6);
      pg.addColorStop(0, 'rgba(255,90,110,0.95)');
      pg.addColorStop(1, 'rgba(255,90,110,0)');
      ctx.fillStyle = pg;
      ctx.beginPath();
      ctx.arc(px, py, 6, 0, Math.PI * 2);
      ctx.fill();
    }

    // markers + on-map labels
    const fs = Math.max(9.5, Math.min(13, W / 95));
    for (let i = 0; i < MARKERS.length; i++) {
      const m = MARKERS[i];
      const pt = proj(m.lon, m.lat);
      const phase = (time * 0.42 + i * 0.4) % 1;

      ctx.strokeStyle = `rgba(216,32,58,${(1 - phase) * 0.6})`;
      ctx.lineWidth = 1.4;
      ctx.beginPath();
      ctx.arc(pt.x, pt.y, 4 + phase * (m.hub ? 22 : 15), 0, Math.PI * 2);
      ctx.stroke();

      const r = m.hub ? 9 : 6;
      const g = ctx.createRadialGradient(pt.x, pt.y, 0, pt.x, pt.y, r * 2.4);
      g.addColorStop(0, m.hub ? 'rgba(255,120,140,1)' : 'rgba(255,80,100,1)');
      g.addColorStop(0.4, 'rgba(216,32,58,0.55)');
      g.addColorStop(1, 'rgba(216,32,58,0)');
      ctx.fillStyle = g;
      ctx.beginPath();
      ctx.arc(pt.x, pt.y, r * 2.4, 0, Math.PI * 2);
      ctx.fill();

      ctx.fillStyle = m.hub ? '#fff' : '#ffdce1';
      ctx.beginPath();
      ctx.arc(pt.x, pt.y, m.hub ? 3.4 : 2.6, 0, Math.PI * 2);
      ctx.fill();

      drawLabel(m, pt, fs);
    }

    raf = requestAnimationFrame(frame);
  }

  function drawLabel(m, pt, fs) {
    const core = m.hub ? 3.4 : 2.6;
    const gap = (m.hub ? 9 : 6) + 5;
    ctx.font = `${m.hub ? 700 : 600} ${fs}px Oswald, system-ui, sans-serif`;
    ctx.fillStyle = m.hub ? '#ffffff' : 'rgba(225,233,245,0.92)';
    ctx.shadowColor = 'rgba(3,7,15,0.95)';
    ctx.shadowBlur = 4;
    let x = pt.x, y = pt.y;
    if (m.pos === 'below') { ctx.textAlign = 'center'; ctx.textBaseline = 'top'; y = pt.y + gap; }
    else if (m.pos === 'above') { ctx.textAlign = 'center'; ctx.textBaseline = 'bottom'; y = pt.y - gap; }
    else if (m.pos === 'right') { ctx.textAlign = 'left'; ctx.textBaseline = 'middle'; x = pt.x + core + 7; }
    else { ctx.textAlign = 'right'; ctx.textBaseline = 'middle'; x = pt.x - core - 7; }
    ctx.fillText(m.name, x, y);
    ctx.shadowBlur = 0;
  }

  /* ---- Lifecycle ---- */
  function start() { if (!raf && grid) raf = requestAnimationFrame(frame); }
  function stop() { if (raf) { cancelAnimationFrame(raf); raf = null; } }

  fetch('assets/world-dots.json')
    .then((r) => r.json())
    .then((data) => { grid = data; buildLand(); start(); })
    .catch(() => { /* map data unavailable — section still renders empty canvas */ });

  let rz;
  window.addEventListener('resize', () => {
    clearTimeout(rz);
    rz = setTimeout(buildLand, 150);
  });
  if ('IntersectionObserver' in window) {
    new IntersectionObserver((e) => { e[0].isIntersecting ? start() : stop(); },
      { threshold: 0.01 }).observe(canvas);
  }
})();
