/* Play: interactive versions of a card's example.
   A subject file registers widgets with Play.add(cardId, title, how, build); the card shows a "▶ Try it" button
   on its drawing, and the widget opens in a panel over the card (key I, Esc closes).
   build(ui) gets a small toolkit: sliders, selects, checkboxes, buttons, SVG plots in data units, and a readout. */
(function () {
  'use strict';
  const REG = {};
  const C = { ink: '#111', red: '#e5484d', blue: '#2f6fd6', green: '#1f9d61', grey: '#9a9a9a', soft: '#e8e8e8', amber: '#d98a00', purple: '#7b4fd0' };
  const NS = 'http://www.w3.org/2000/svg';
  const FONT = "'Helvetica Neue LT Std','Helvetica Neue',Helvetica,Arial,sans-serif";

  /* ---------- maths ---------- */
  const M = {
    clamp: (x, a, b) => Math.max(a, Math.min(b, x)),
    range: (a, b, n) => Array.from({ length: n }, (_, i) => a + (b - a) * i / (n - 1)),
    sum: a => a.reduce((s, x) => s + x, 0),
    mean: a => a.reduce((s, x) => s + x, 0) / a.length,
    variance: a => { const m = M.mean(a); return a.reduce((s, x) => s + (x - m) * (x - m), 0) / a.length; },
    erf(x) { // Abramowitz-Stegun 7.1.26, |error| < 1.5e-7
      const s = Math.sign(x); x = Math.abs(x);
      const t = 1 / (1 + 0.3275911 * x);
      const y = 1 - (((((1.061405429 * t - 1.453152027) * t) + 1.421413741) * t - 0.284496736) * t + 0.254829592) * t * Math.exp(-x * x);
      return s * y;
    },
    Phi: z => 0.5 * (1 + M.erf(z / Math.SQRT2)),
    npdf: (x, mu = 0, s = 1) => Math.exp(-0.5 * ((x - mu) / s) ** 2) / (s * Math.sqrt(2 * Math.PI)),
    lgamma(z) { // Lanczos
      const g = 7, c = [0.99999999999980993, 676.5203681218851, -1259.1392167224028, 771.32342877765313, -176.61502916214059,
        12.507343278686905, -0.13857109526572012, 9.9843695780195716e-6, 1.5056327351493116e-7];
      if (z < 0.5) return Math.log(Math.PI / Math.sin(Math.PI * z)) - M.lgamma(1 - z);
      z -= 1; let x = c[0]; for (let i = 1; i < g + 2; i++) x += c[i] / (z + i);
      const t = z + g + 0.5; return 0.5 * Math.log(2 * Math.PI) + (z + 0.5) * Math.log(t) - t + Math.log(x);
    },
    binom: (n, k, p) => k < 0 || k > n ? 0 : Math.exp(M.lgamma(n + 1) - M.lgamma(k + 1) - M.lgamma(n - k + 1) + k * Math.log(p || 1e-300) + (n - k) * Math.log((1 - p) || 1e-300)),
    pois: (k, l) => k < 0 ? 0 : Math.exp(-l + k * Math.log(l || 1e-300) - M.lgamma(k + 1)),
    gammaPdf: (x, k, rate) => x <= 0 ? 0 : Math.exp(k * Math.log(rate) + (k - 1) * Math.log(x) - rate * x - M.lgamma(k)),
    rnorm() { let u = 0, v = 0; while (!u) u = Math.random(); while (!v) v = Math.random(); return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v); },
    rexp: rate => -Math.log(1 - Math.random()) / rate,
    rpois(l) { let k = 0, p = Math.exp(-l), s = p; const u = Math.random(); while (u > s && k < 1000) { k++; p *= l / k; s += p; } return k; },
    /* correlated pair with sds s1, s2 and correlation r around (m1, m2) */
    rbiv(m1, m2, s1, s2, r) { const a = M.rnorm(), b = M.rnorm(); return [m1 + s1 * a, m2 + s2 * (r * a + Math.sqrt(Math.max(0, 1 - r * r)) * b)]; },
    hist(a, lo, hi, bins) { const h = new Array(bins).fill(0), w = (hi - lo) / bins; a.forEach(x => { const i = Math.floor((x - lo) / w); if (i >= 0 && i < bins) h[i]++; }); return h.map((c, i) => [lo + (i + 0.5) * w, c / (a.length * w)]); },
    gcd: (a, b) => b ? M.gcd(b, a % b) : Math.abs(a),
    matmul(A, B) { return A.map(r => B[0].map((_, j) => r.reduce((s, x, k) => s + x * B[k][j], 0))); },
    matpow(A, n) { let R = A.map((r, i) => r.map((_, j) => +(i === j))); for (let i = 0; i < n; i++) R = M.matmul(R, A); return R; },
    solve(A, b) { // Gaussian elimination with partial pivoting
      const n = b.length, a = A.map((r, i) => [...r, b[i]]);
      for (let c = 0; c < n; c++) {
        let p = c; for (let r = c + 1; r < n; r++) if (Math.abs(a[r][c]) > Math.abs(a[p][c])) p = r;
        [a[c], a[p]] = [a[p], a[c]];
        for (let r = 0; r < n; r++) if (r !== c) { const f = a[r][c] / a[c][c]; for (let k = c; k <= n; k++) a[r][k] -= f * a[c][k]; }
      }
      return a.map((r, i) => r[n] / r[i]);
    },
    integrate(f, a, b, n = 400) { const h = (b - a) / n; let s = 0.5 * (f(a) + f(b)); for (let i = 1; i < n; i++) s += f(a + i * h); return s * h; },
  };
  const fmt = (x, d = 3) => (!isFinite(x) ? '∞' : Math.abs(x) < 1e-12 ? '0' : (+x.toFixed(d)).toString()).replace('-', '−');
  const pct = (x, d = 1) => fmt(100 * x, d) + '%';

  const el = (tag, cls, html) => { const e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; };
  const sv = (tag, attrs) => { const e = document.createElementNS(NS, tag); for (const k in attrs) if (attrs[k] != null) e.setAttribute(k, attrs[k]); return e; };

  /* ---------- an SVG plot in data units ---------- */
  function Plot(opts) {
    const o = Object.assign({ x: [0, 1], y: [0, 1], w: 560, h: 230, axes: true, pad: null }, opts);
    const pad = o.pad || (o.axes ? { l: 44, r: 14, t: 12, b: 34 } : { l: 6, r: 6, t: 6, b: 6 });
    const svg = sv('svg', { viewBox: `0 0 ${o.w} ${o.h}`, class: 'pl-svg', 'font-family': FONT });
    const W = o.w - pad.l - pad.r, H = o.h - pad.t - pad.b;
    const X = x => pad.l + (x - o.x[0]) / (o.x[1] - o.x[0]) * W;
    const Y = y => pad.t + H - (y - o.y[0]) / (o.y[1] - o.y[0]) * H;
    const P = { svg, X, Y, o };
    const add = (tag, a) => { const e = sv(tag, a); svg.appendChild(e); return e; };
    const ticks = (a, b, n) => { const step = Math.pow(10, Math.floor(Math.log10((b - a) / n))); const err = (b - a) / n / step; const s = step * (err >= 7.5 ? 10 : err >= 3.5 ? 5 : err >= 1.5 ? 2 : 1); const out = []; for (let t = Math.ceil(a / s) * s; t <= b + 1e-9; t += s) out.push(+t.toFixed(10)); return out; };
    P.setY = (y0, y1) => { o.y = [y0, y1]; };
    P.setX = (x0, x1) => { o.x = [x0, x1]; };
    P.clear = () => {
      svg.innerHTML = '';
      if (!o.axes) return P;
      const xt = o.xt || ticks(o.x[0], o.x[1], 6), yt = o.yt || ticks(o.y[0], o.y[1], 4);
      yt.forEach(t => { add('line', { x1: pad.l, x2: pad.l + W, y1: Y(t), y2: Y(t), stroke: '#efefef' }); add('text', { x: pad.l - 6, y: Y(t) + 4, 'text-anchor': 'end', 'font-size': 11, fill: '#777' }).textContent = o.yf ? o.yf(t) : fmt(t, 3); });
      xt.forEach(t => add('text', { x: X(t), y: pad.t + H + 15, 'text-anchor': 'middle', 'font-size': 11, fill: '#777' }).textContent = o.xf ? o.xf(t) : fmt(t, 3));
      add('line', { x1: pad.l, x2: pad.l + W, y1: pad.t + H, y2: pad.t + H, stroke: '#333' });
      add('line', { x1: pad.l, x2: pad.l, y1: pad.t, y2: pad.t + H, stroke: '#333' });
      if (o.xl) add('text', { x: pad.l + W, y: o.h - 3, 'text-anchor': 'end', 'font-size': 11.5, fill: '#444' }).textContent = o.xl;
      if (o.yl) add('text', { x: pad.l + 4, y: pad.t + 10, 'font-size': 11.5, fill: '#444' }).textContent = o.yl;
      return P;
    };
    const st = (q, def) => ({ stroke: q.c || def || C.ink, 'stroke-width': q.w || 1.6, 'stroke-dasharray': q.dash || null, fill: 'none', opacity: q.op });
    P.path = (pts, q = {}) => { const lo = o.y[0] - 0.02 * (o.y[1] - o.y[0]), hi = o.y[1] + 0.02 * (o.y[1] - o.y[0]); // lines are clipped to the plot
      return add('path', Object.assign(st(q), { d: pts.map((p, i) => (i ? 'L' : 'M') + X(p[0]).toFixed(1) + ' ' + Y(M.clamp(p[1], lo, hi)).toFixed(1)).join('') })); };
    P.fn = (f, q = {}) => { const a = q.from != null ? q.from : o.x[0], b = q.to != null ? q.to : o.x[1], n = q.n || 200; return P.path(M.range(a, b, n).map(x => [x, f(x)]).filter(p => isFinite(p[1])), q); };
    P.poly = (pts, q = {}) => add('path', { d: pts.map((p, i) => (i ? 'L' : 'M') + X(p[0]).toFixed(1) + ' ' + Y(p[1]).toFixed(1)).join('') + 'Z', fill: q.fill || C.red, 'fill-opacity': q.op != null ? q.op : 0.25, stroke: q.c || 'none', 'stroke-width': q.w || 1 });
    P.area = (f, a, b, q = {}) => { const xs = M.range(a, b, q.n || 120); return P.poly([[a, q.base || 0], ...xs.map(x => [x, f(x)]), [b, q.base || 0]], q); };
    P.seg = (x1, y1, x2, y2, q = {}) => add('line', Object.assign(st(q), { x1: X(x1), y1: Y(y1), x2: X(x2), y2: Y(y2) }));
    P.vline = (x, q = {}) => P.seg(x, o.y[0], x, o.y[1], Object.assign({ c: C.grey, dash: '4 3', w: 1.2 }, q));
    P.hline = (y, q = {}) => P.seg(o.x[0], y, o.x[1], y, Object.assign({ c: C.grey, dash: '4 3', w: 1.2 }, q));
    P.dot = (x, y, q = {}) => add('circle', { cx: X(x), cy: Y(y), r: q.r || 4, fill: q.fill || q.c || C.ink, stroke: q.stroke || 'none', 'stroke-width': 1.5, 'fill-opacity': q.op != null ? q.op : 1 });
    P.rect = (x0, y0, x1, y1, q = {}) => add('rect', { x: Math.min(X(x0), X(x1)), y: Math.min(Y(y0), Y(y1)), width: Math.abs(X(x1) - X(x0)), height: Math.abs(Y(y1) - Y(y0)), fill: q.fill || C.red, 'fill-opacity': q.op != null ? q.op : 0.25, stroke: q.c || 'none', 'stroke-width': q.w || 1, rx: q.rx || 0 });
    P.txt = (x, y, s, q = {}) => { const t = add('text', { x: X(x) + (q.dx || 0), y: Y(y) + (q.dy || 0), 'text-anchor': q.a || 'middle', 'font-size': q.size || 12, fill: q.c || C.ink, 'font-weight': q.bold ? 700 : null, 'dominant-baseline': q.mid ? 'middle' : null }); t.textContent = s; return t; };
    P.bars = (pts, width, q = {}) => pts.forEach(([x, h]) => P.rect(x - width / 2, 0, x + width / 2, h, Object.assign({ fill: C.blue, op: 0.35 }, q)));
    P.arrow = (x1, y1, x2, y2, q = {}) => { // data-space start, end; screen-space head
      const a = X(x1), b = Y(y1), c = X(x2), d = Y(y2), L = Math.hypot(c - a, d - b) || 1, ux = (c - a) / L, uy = (d - b) / L, hs = q.head || 8;
      add('line', { x1: a, y1: b, x2: c - ux * hs * 0.8, y2: d - uy * hs * 0.8, stroke: q.c || C.ink, 'stroke-width': q.w || 1.6, opacity: q.op });
      add('path', { d: `M${c} ${d}L${c - ux * hs - uy * hs * 0.45} ${d - uy * hs + ux * hs * 0.45}L${c - ux * hs + uy * hs * 0.45} ${d - uy * hs - ux * hs * 0.45}Z`, fill: q.c || C.ink, opacity: q.op });
    };
    /* screen-space curved arrow between two circles (Markov chain diagrams) */
    P.link = (x1, y1, x2, y2, q = {}) => {
      const a = X(x1), b = Y(y1), c = X(x2), d = Y(y2), r = q.r || 20, bend = q.bend == null ? 0.25 : q.bend;
      const mx = (a + c) / 2, my = (b + d) / 2, dx = c - a, dy = d - b, L = Math.hypot(dx, dy) || 1;
      const cx = mx - dy * bend, cy = my + dx * bend;
      const sx = a + (cx - a) / Math.hypot(cx - a, cy - b) * r, sy = b + (cy - b) / Math.hypot(cx - a, cy - b) * r;
      const ex = c + (cx - c) / Math.hypot(cx - c, cy - d) * r, ey = d + (cy - d) / Math.hypot(cx - c, cy - d) * r;
      const w = q.w || 1.6, col = q.c || C.ink;
      add('path', { d: `M${sx} ${sy}Q${cx} ${cy} ${ex} ${ey}`, fill: 'none', stroke: col, 'stroke-width': w, opacity: q.op });
      const tx = ex - cx, ty = ey - cy, tl = Math.hypot(tx, ty) || 1, ux = tx / tl, uy = ty / tl, hs = 6 + w;
      add('path', { d: `M${ex} ${ey}L${ex - ux * hs - uy * hs * 0.45} ${ey - uy * hs + ux * hs * 0.45}L${ex - ux * hs + uy * hs * 0.45} ${ey - uy * hs - ux * hs * 0.45}Z`, fill: col, opacity: q.op });
      if (q.label != null) { const lx = 0.25 * a + 0.5 * cx + 0.25 * c, ly = 0.25 * b + 0.5 * cy + 0.25 * d; const t = add('text', { x: lx, y: ly + 4, 'text-anchor': 'middle', 'font-size': 12, fill: col, stroke: '#fff', 'stroke-width': 3, 'paint-order': 'stroke' }); t.textContent = q.label; }
    };
    P.loop = (x, y, q = {}) => { // self-loop above a node
      const a = X(x), b = Y(y), r = q.r || 20, w = q.w || 1.6, col = q.c || C.ink, up = q.down ? 1 : -1;
      add('path', { d: `M${a - r * 0.55} ${b + up * r * 0.8}C${a - r * 1.4} ${b + up * r * 2.6} ${a + r * 1.4} ${b + up * r * 2.6} ${a + r * 0.55} ${b + up * r * 0.8}`, fill: 'none', stroke: col, 'stroke-width': w, opacity: q.op });
      if (q.label != null) { const t = add('text', { x: a, y: b + up * r * 2.35 + (q.down ? 10 : 0), 'text-anchor': 'middle', 'font-size': 12, fill: col }); t.textContent = q.label; }
    };
    P.node = (x, y, label, q = {}) => { add('circle', { cx: X(x), cy: Y(y), r: q.r || 20, fill: q.fill || '#fff', stroke: q.c || C.ink, 'stroke-width': q.w || 1.8 }); const t = add('text', { x: X(x), y: Y(y) + 5, 'text-anchor': 'middle', 'font-size': q.size || 14, fill: q.tc || C.ink, 'font-weight': 700 }); t.textContent = label; };
    P.onclick = fn => { svg.style.cursor = 'crosshair'; svg.addEventListener('click', e => { const r = svg.getBoundingClientRect(), sx = (e.clientX - r.left) / r.width * o.w, sy = (e.clientY - r.top) / r.height * o.h; fn(o.x[0] + (sx - pad.l) / W * (o.x[1] - o.x[0]), o.y[0] + (pad.t + H - sy) / H * (o.y[1] - o.y[0])); }); };
    /* a heat map of f over the plot: dark = high */
    P.heat = (f, q = {}) => {
      const nx = q.nx || 48, ny = q.ny || 32, vals = [];
      let mx = 0; for (let i = 0; i < nx; i++) for (let j = 0; j < ny; j++) { const x = o.x[0] + (i + 0.5) / nx * (o.x[1] - o.x[0]), y = o.y[0] + (j + 0.5) / ny * (o.y[1] - o.y[0]); const v = f(x, y); vals.push([i, j, v]); if (v > mx) mx = v; }
      const cw = W / nx, ch = H / ny, col = q.color || '47,111,214';
      vals.forEach(([i, j, v]) => { if (v > 0) add('rect', { x: pad.l + i * cw, y: pad.t + H - (j + 1) * ch, width: cw + 0.5, height: ch + 0.5, fill: `rgba(${col},${(0.9 * v / (mx || 1)).toFixed(3)})` }); });
      return mx;
    };
    return P.clear();
  }

  /* ---------- the panel ---------- */
  let overlay = null, timers = [];
  function UI(body) {
    const stage = el('div', 'pl-stage'), ctl = el('div', 'pl-ctl'), out = el('div', 'pl-out');
    body.append(stage, ctl, out);
    const draws = [];
    const ui = {
      C, M, fmt, pct,
      redraw() { draws.forEach(f => { try { f(); } catch (e) { console.error(e); out.textContent = 'Widget error: ' + e.message; } }); },
      draw(f) { draws.push(f); },
      say(html) { out.innerHTML = html; },
      plot(opts) { const p = Plot(opts); (opts.into || stage).appendChild(p.svg); return p; },
      row() { const r = el('div', 'pl-row'); stage.appendChild(r); return r; },
      note(html) { const n = el('p', 'pl-note', html); stage.appendChild(n); return n; },
      slider(label, min, max, step, val, f = v => fmt(v, 3)) {
        const row = el('label', 'pl-sl'), name = el('span', 'pl-lab', label), inp = el('input'), show = el('b', 'pl-val');
        Object.assign(inp, { type: 'range', min, max, step, value: val });
        const s = { v: +val, set(x) { s.v = +x; inp.value = x; show.textContent = f(s.v); }, input: inp };
        show.textContent = f(s.v);
        inp.addEventListener('input', () => { s.v = +inp.value; show.textContent = f(s.v); ui.redraw(); });
        row.append(name, inp, show); ctl.appendChild(row); return s;
      },
      select(label, options, val) {
        const row = el('label', 'pl-sl pl-selrow'), name = el('span', 'pl-lab', label), sel = el('select');
        options.forEach(([v, t]) => { const op = el('option', null, t); op.value = v; sel.appendChild(op); });
        sel.value = val; const s = { v: val };
        sel.addEventListener('change', () => { s.v = sel.value; ui.redraw(); });
        row.append(name, sel); ctl.appendChild(row); return s;
      },
      check(label, val) {
        const row = el('label', 'pl-chk'), inp = el('input'); inp.type = 'checkbox'; inp.checked = !!val;
        const s = { v: !!val }; inp.addEventListener('change', () => { s.v = inp.checked; ui.redraw(); });
        row.append(inp, document.createTextNode(' ' + label)); ctl.appendChild(row); return s;
      },
      btn(label, fn) { const b = el('button', 'pl-btn', label); b.addEventListener('click', () => { fn(); ui.redraw(); }); ctl.appendChild(b); return b; },
      /* call fn every ms until it returns false or the panel closes */
      every(ms, fn) { const t = setInterval(() => { if (fn() === false) clearInterval(t); ui.redraw(); }, ms); timers.push(t); return t; },
    };
    return ui;
  }

  function close() {
    timers.forEach(clearInterval); timers = [];
    if (overlay) { overlay.remove(); overlay = null; }
  }
  function open(id) {
    const w = REG[id]; if (!w) return;
    close();
    overlay = el('div', 'pl-overlay');
    const box = el('div', 'pl-box'), head = el('div', 'pl-head'), body = el('div', 'pl-body');
    head.innerHTML = `<div><span class="pl-kick">TRY IT</span><h2>${w.title}</h2><p class="pl-how">${w.how}</p></div>`;
    const x = el('button', 'pl-x', '✕'); x.title = 'Close (Esc)'; x.addEventListener('click', close); head.appendChild(x);
    box.append(head, body); overlay.appendChild(box);
    overlay.addEventListener('click', e => { if (e.target === overlay) close(); });
    document.body.appendChild(overlay);
    const ui = UI(body);
    try { w.build(ui); ui.redraw(); } catch (e) { console.error(e); ui.say('Widget error: ' + e.message); }
  }
  document.addEventListener('keydown', e => { if (overlay && e.key === 'Escape') { e.stopImmediatePropagation(); close(); } }, true);

  const css = `
  .pl-overlay { position: fixed; inset: 0; z-index: 9000; background: rgba(0,0,0,.62); display: flex; align-items: center; justify-content: center; padding: 16px; animation: plfade .18s ease-out; }
  @keyframes plfade { from { opacity: 0; } }
  .pl-box { background: #fff; color: #111; width: min(940px, 100%); max-height: calc(100vh - 32px); overflow: auto; border-radius: 10px; box-shadow: 0 20px 60px rgba(0,0,0,.45); font-family: ${FONT}; }
  .pl-head { display: flex; gap: 16px; align-items: flex-start; justify-content: space-between; padding: 18px 22px 8px; position: sticky; top: 0; background: #fff; z-index: 1; border-bottom: 1px solid #eee; }
  .pl-kick { font-size: 11px; letter-spacing: 1.4px; color: #e5484d; font-weight: 700; }
  .pl-head h2 { margin: 2px 0 4px; font-size: 21px; line-height: 1.2; }
  .pl-how { margin: 0 0 6px; font-size: 14px; color: #555; line-height: 1.4; }
  .pl-x { border: 1px solid #ddd; background: #fff; border-radius: 8px; width: 34px; height: 34px; font-size: 15px; color: #333; flex: none; }
  .pl-x:hover { border-color: #e5484d; color: #e5484d; }
  .pl-body { padding: 10px 22px 20px; }
  .pl-stage { display: flex; flex-direction: column; gap: 6px; }
  .pl-row { display: flex; gap: 8px; flex-wrap: wrap; } .pl-row > svg { flex: 1 1 280px; min-width: 0; }
  .pl-svg { width: 100%; height: auto; display: block; }
  .pl-note { margin: 0; font-size: 13px; color: #666; }
  .pl-ctl { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 6px 18px; margin: 12px 0 10px; align-items: center; }
  .pl-sl { display: grid; grid-template-columns: minmax(90px, auto) 1fr 52px; gap: 8px; align-items: center; font-size: 13.5px; color: #333; }
  .pl-selrow { grid-template-columns: minmax(90px, auto) 1fr; }
  .pl-sl input[type=range] { width: 100%; accent-color: #e5484d; }
  .pl-sl select { font: inherit; padding: 4px 6px; border: 1px solid #ccc; border-radius: 6px; background: #fff; color: #111; }
  .pl-val { font-variant-numeric: tabular-nums; text-align: right; font-weight: 700; }
  .pl-chk { font-size: 13.5px; color: #333; display: flex; align-items: center; gap: 4px; } .pl-chk input { accent-color: #e5484d; }
  .pl-btn { justify-self: start; border: 1px solid #111; background: #111; color: #fff; border-radius: 7px; padding: 7px 14px; font: inherit; font-size: 13.5px; font-weight: 600; }
  .pl-btn:hover { background: #e5484d; border-color: #e5484d; }
  .pl-out { background: #f6f6f6; border-left: 3px solid #e5484d; border-radius: 6px; padding: 10px 14px; font-size: 14.5px; line-height: 1.55; color: #222; }
  .pl-out b { font-variant-numeric: tabular-nums; } .pl-out .r { color: #e5484d; } .pl-out .bl { color: #2f6fd6; } .pl-out .g { color: #1f9d61; }
  .pl-out table { border-collapse: collapse; margin: 4px 0; } .pl-out td, .pl-out th { padding: 2px 10px 2px 0; text-align: left; font-variant-numeric: tabular-nums; }
  .playbtn { position: absolute; right: 8px; bottom: 8px; border: 1px solid #111; background: #fff; color: #111; border-radius: 999px; padding: 4px 11px; font-size: 12px; font-weight: 700; letter-spacing: .3px; box-shadow: 1px 2px 0 rgba(0,0,0,.15); z-index: 2; }
  .playbtn:hover { background: #e5484d; border-color: #e5484d; color: #fff; }
  .sketch-box { position: relative; }`;
  const style = document.createElement('style'); style.textContent = css; document.head.appendChild(style);

  window.Play = { add(id, title, how, build) { REG[id] = { title, how, build }; }, has: id => !!REG[id], open, close, isOpen: () => !!overlay, M, C, fmt, pct };
})();
