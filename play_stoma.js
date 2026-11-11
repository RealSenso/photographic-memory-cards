/* StoMA: interactive versions of the commute examples. One Play.add per card id (see play_lib.js). */
(function () {
  'use strict';
  const { M, C, fmt, pct } = Play;
  const add = Play.add;

  /* ===================== 01 · Probability spaces ===================== */
  add(30101, 'Every morning is a point in Ω', 'Each dot is one possible morning (wait, ride). Move the cut-off for “late”: the event A is the set of red dots, and ℙ(A) is the share of Ω they cover.', ui => {
    let pts = [];
    const fresh = () => { pts = Array.from({ length: 400 }, () => [Math.random() * 15, 15 + Math.random() * 25]); };
    fresh();
    const cut = ui.slider('late if wait + ride >', 20, 55, 0.5, 38, v => fmt(v, 1) + ' min');
    const p = ui.plot({ x: [0, 15], y: [15, 40], h: 260, xl: 'wait (min)', yl: 'ride (min)' });
    ui.btn('New 400 mornings', fresh);
    ui.draw(() => {
      p.clear();
      p.poly([[0, cut.v], [15, cut.v - 15], [15, 40], [0, 40]].map(([x, y]) => [x, M.clamp(y, 15, 40)]), { fill: C.red, op: 0.08 });
      p.seg(0, cut.v, 15, cut.v - 15, { c: C.red, dash: '5 4' });
      let k = 0; pts.forEach(([x, y]) => { const late = x + y > cut.v; if (late) k++; p.dot(x, y, { r: 2.6, c: late ? C.red : '#555', op: late ? 0.9 : 0.45 }); });
      p.txt(13.5, 38.5, 'A = late', { c: C.red, a: 'end', bold: true });
      ui.say(`A = {mornings with wait + ride > ${fmt(cut.v, 1)}} is a set of points, so it is an event. ` +
        `<b class="r">${k}</b> of 400 mornings are in A: ℙ(A) ≈ <b class="r">${fmt(k / 400, 3)}</b>, and its complement Aᶜ (on time) gets ℙ(Aᶜ) ≈ <b>${fmt(1 - k / 400, 3)}</b>. ` +
        `They add to 1 = ℙ(Ω), because every morning is in exactly one of them.`);
    });
  });

  add(30102, 'Disjoint causes just add', 'Three causes of lateness that never happen on the same morning. Set their chances and watch ℙ(A₁ ∪ A₂ ∪ A₃) = ℙ(A₁) + ℙ(A₂) + ℙ(A₃). Push the total past 1 to break the axioms.', ui => {
    const a = ui.slider('ℙ(rain)', 0, 0.6, 0.01, 0.15), b = ui.slider('ℙ(breakdown)', 0, 0.6, 0.01, 0.08), c = ui.slider('ℙ(overslept)', 0, 0.6, 0.01, 0.1);
    const p = ui.plot({ x: [0, 1], y: [0, 1], h: 150, axes: false, pad: { l: 10, r: 10, t: 10, b: 10 } });
    ui.draw(() => {
      p.clear();
      const s = a.v + b.v + c.v;
      p.rect(0, 0.3, 1, 0.75, { fill: '#000', op: 0.04, c: '#333' });
      p.txt(0.5, 0.88, 'Ω: all mornings (total chance 1)', { size: 13 });
      let x = 0;[[a.v, C.red, 'rain'], [b.v, C.blue, 'breakdown'], [c.v, C.amber, 'overslept']].forEach(([w, col, n]) => {
        const x1 = Math.min(x + w, 1); if (x1 > x) { p.rect(x, 0.3, x1, 0.75, { fill: col, op: 0.55 }); if (w > 0.14) p.txt((x + x1) / 2, 0.5, n, { size: 12, c: '#111' }); } x += w;
      });
      if (s > 1) p.rect(1, 0.3, 1, 0.75, { c: C.red, w: 3 });
      p.txt(Math.min(s, 1), 0.18, `sum = ${fmt(s, 2)}`, { c: s > 1 ? C.red : '#111', bold: true, a: s > 0.85 ? 'end' : 'middle' });
      ui.say(s <= 1
        ? `No morning is in two causes, so the blocks sit side by side and ℙ(late for one of these reasons) = ${fmt(a.v, 2)} + ${fmt(b.v, 2)} + ${fmt(c.v, 2)} = <b class="r">${fmt(s, 2)}</b>. The rest of Ω, <b>${fmt(1 - s, 2)}</b>, is mornings with none of them.`
        : `<b class="r">Impossible:</b> the blocks are disjoint, so their chances must add, but ${fmt(s, 2)} &gt; 1 = ℙ(Ω). No probability measure can give these three disjoint events these chances.`);
    });
  });

  add(30103, 'Chances creep up to the limit', 'Aₙ = “late at least once in the first n days” grows with n. Here the risk on day k fades as you learn the route: q·rᵏ⁻¹. ℙ(Aₙ) climbs without jumping to ℙ(A), the chance of ever being late.', ui => {
    const q = ui.slider('day-1 late chance q', 0.01, 0.6, 0.01, 0.2), r = ui.slider('risk kept each day r', 0, 1, 0.01, 0.8), n = ui.slider('days checked n', 1, 40, 1, 6, v => v);
    const p = ui.plot({ x: [0, 40], y: [0, 1], h: 240, xl: 'n (days)', yl: 'ℙ(Aₙ)' });
    ui.draw(() => {
      p.clear();
      const vals = []; let none = 1; for (let k = 1; k <= 400; k++) { none *= 1 - q.v * Math.pow(r.v, k - 1); vals.push(1 - none); }
      const lim = vals[399];
      p.hline(lim, { c: C.red }); p.txt(39.5, lim, `ℙ(A) = ${fmt(lim, 3)}`, { a: 'end', dy: -6, c: C.red });
      for (let k = 1; k <= 40; k++) p.dot(k, vals[k - 1], { r: k === n.v ? 5.5 : 3, c: k <= n.v ? C.ink : '#bbb' });
      p.vline(n.v);
      ui.say(`ℙ(A<sub>${n.v}</sub>) = 1 − ∏(1 − q·rᵏ⁻¹) = <b>${fmt(vals[n.v - 1], 4)}</b>. The events grow, A₁ ⊆ A₂ ⊆ …, so the chances can only rise, and they rise to ℙ(⋃Aₙ) = <b class="r">${fmt(lim, 4)}</b>. ` +
        (r.v < 1 ? 'Because the risk fades, the limit stays below 1: you may never be late.' : 'With r = 1 the risk never fades and the limit is 1: you will be late some day.'));
    });
  });

  /* three causes as arcs of a circle of mornings: shifting them apart changes how much they overlap */
  function arcs(ps, spread) { return ps.map((w, i) => [(i * spread) % 1, w]); }
  function inArc(x, [s, w]) { return w > 0 && ((x - s + 1) % 1) < w; }
  function overlapStats(A) {
    const N = 4000; let union = 0, pairs = 0, triple = 0;
    for (let i = 0; i < N; i++) { const x = (i + 0.5) / N, h = A.map(a => inArc(x, a)), k = h.filter(Boolean).length; if (k) union++; pairs += k * (k - 1) / 2; if (k === 3) triple++; }
    return { union: union / N, pairs: pairs / N, triple: triple / N };
  }
  function drawArcs(p, A) {
    const cols = [C.red, C.blue, C.amber], names = ['rain', 'breakdown', 'strike'];
    p.rect(0, 0, 1, 0.12, { fill: '#000', op: 0.04, c: '#999' });
    p.txt(0.5, 0.95, 'all mornings, laid out on a line (each cause is a stretch of mornings)', { size: 12, c: '#555' });
    A.forEach(([s, w], i) => {
      const y0 = 0.25 + i * 0.2, parts = s + w <= 1 ? [[s, s + w]] : [[s, 1], [0, s + w - 1]];
      parts.forEach(([u, v]) => { p.rect(u, y0, v, y0 + 0.13, { fill: cols[i], op: 0.6 }); p.rect(u, 0, v, 0.12, { fill: cols[i], op: 0.25 }); });
      p.txt(Math.min(s + 0.01, 0.9), y0 + 0.065, `${names[i]} ${fmt(w, 2)}`, { a: 'start', size: 11.5, mid: true });
    });
  }
  add(30104, 'Boole: the sum is a safe ceiling', 'Three causes of lateness. Slide them apart or together. The chance that something goes wrong (the union) never exceeds the sum of the three chances, and Bonferroni gives a floor.', ui => {
    const a = ui.slider('ℙ(rain)', 0, 0.5, 0.01, 0.1), b = ui.slider('ℙ(breakdown)', 0, 0.5, 0.01, 0.05), c = ui.slider('ℙ(strike)', 0, 0.5, 0.01, 0.03);
    const sp = ui.slider('how far apart', 0, 0.34, 0.005, 0.02);
    const p = ui.plot({ x: [0, 1], y: [0, 1], h: 210, axes: false });
    ui.draw(() => {
      p.clear(); const A = arcs([a.v, b.v, c.v], sp.v); drawArcs(p, A);
      const s = overlapStats(A), S1 = a.v + b.v + c.v;
      ui.say(`ℙ(⋃Aᵢ) = <b class="r">${fmt(s.union, 3)}</b> ≤ ∑ℙ(Aᵢ) = <b>${fmt(S1, 3)}</b> (Boole). ` +
        `The gap ${fmt(S1 - s.union, 3)} is the overlap counted more than once. ` +
        `Bonferroni floor: ∑ℙ(Aᵢ) − ∑ℙ(Aᵢ∩Aⱼ) = ${fmt(S1, 3)} − ${fmt(s.pairs, 3)} = <b>${fmt(S1 - s.pairs, 3)}</b> ≤ ${fmt(s.union, 3)}. ` +
        (s.pairs < 1e-9 ? 'Now nothing overlaps and the ceiling is exact.' : 'Spread them apart to make the ceiling exact.'));
    });
  });

  add(30105, 'Inclusion–exclusion, term by term', 'Add the singles, subtract the pairs, add back the triple. The bars show each partial sum zig-zagging onto the true chance of being late for some reason.', ui => {
    const a = ui.slider('ℙ(rain)', 0, 0.6, 0.01, 0.3), b = ui.slider('ℙ(breakdown)', 0, 0.6, 0.01, 0.25), c = ui.slider('ℙ(strike)', 0, 0.6, 0.01, 0.2);
    const sp = ui.slider('how far apart', 0, 0.34, 0.005, 0.08);
    const row = ui.row();
    const p = ui.plot({ x: [0, 1], y: [0, 1], h: 210, w: 420, axes: false, into: row });
    const q = ui.plot({ x: [0, 4], y: [0, 1.4], h: 210, w: 300, into: row, xt: [], yl: 'partial sum' });
    ui.draw(() => {
      p.clear(); const A = arcs([a.v, b.v, c.v], sp.v); drawArcs(p, A);
      const s = overlapStats(A), S1 = a.v + b.v + c.v, steps = [S1, S1 - s.pairs, S1 - s.pairs + s.triple];
      q.clear(); q.hline(s.union, { c: C.red }); q.txt(3.95, s.union, 'true', { a: 'end', dy: -5, c: C.red });
      ['+ singles', '− pairs', '+ triple'].forEach((t, i) => { q.rect(i + 0.6, 0, i + 1.4, steps[i], { fill: [C.blue, C.amber, C.green][i], op: 0.5 }); q.txt(i + 1, 0, t, { dy: 14, size: 11 }); q.txt(i + 1, steps[i], fmt(steps[i], 3), { dy: -5, size: 11 }); });
      ui.say(`∑ℙ(Aᵢ) = ${fmt(S1, 3)}, ∑ℙ(Aᵢ∩Aⱼ) = ${fmt(s.pairs, 3)}, ℙ(A₁∩A₂∩A₃) = ${fmt(s.triple, 3)}. ` +
        `ℙ(⋃Aᵢ) = ${fmt(S1, 3)} − ${fmt(s.pairs, 3)} + ${fmt(s.triple, 3)} = <b class="r">${fmt(steps[2], 3)}</b> (measured directly: ${fmt(s.union, 3)}). ` +
        `Each partial sum alternately over- and under-shoots: those are the Bonferroni bounds.`);
    });
  });

  /* ===================== 02 · Conditioning ===================== */
  /* weather blocks: width = ℙ(weather), red height = ℙ(late | weather) */
  function weatherWidget(ui, mode) {
    const pd = ui.slider('ℙ(dry)', 0.05, 0.9, 0.01, 0.6), pr = ui.slider('ℙ(rain)', 0.05, 0.9, 0.01, 0.32);
    const ld = ui.slider('ℙ(late | dry)', 0, 1, 0.01, 0.1), lr = ui.slider('ℙ(late | rain)', 0, 1, 0.01, 0.35), ls = ui.slider('ℙ(late | storm)', 0, 1, 0.01, 0.9);
    const see = mode === 'bayes' ? null : ui.check(mode === 'cond' ? 'Look out of the window: it is raining (condition on B)' : 'Highlight the late part of each block', mode !== 'cond');
    const row = ui.row();
    const p = ui.plot({ x: [0, 1], y: [0, 1], h: 250, w: mode === 'bayes' ? 470 : 640, into: row, xt: [0, 0.5, 1], yl: 'ℙ(late | weather)' });
    const q = mode === 'bayes' ? ui.plot({ x: [0, 3], y: [0, 1], h: 250, w: 260, into: row, xt: [], yl: 'ℙ(weather | late)' }) : null;
    ui.draw(() => {
      let d = pd.v, r = pr.v; if (d + r > 0.97) r = 0.97 - d; const s = 1 - d - r;
      const W = [['dry', d, ld.v, C.blue], ['rain', r, lr.v, C.ink], ['storm', s, ls.v, C.purple]];
      const pl = W.reduce((a, w) => a + w[1] * w[2], 0);
      p.clear(); let x = 0;
      W.forEach(([n, w, l, col], i) => {
        const dim = mode === 'cond' && see.v && i !== 1;
        p.rect(x, 0, x + w, 1, { fill: col, op: dim ? 0.03 : 0.08, c: '#888' });
        p.rect(x, 0, x + w, l, { fill: C.red, op: dim ? 0.12 : 0.55 });
        if (w > 0.06) p.txt(x + w / 2, 0.93, `${n} ${fmt(w, 2)}`, { size: 12, c: dim ? '#bbb' : '#111' });
        x += w;
      });
      if (mode === 'cond') {
        const pB = r, pAB = r * lr.v;
        ui.say(see.v
          ? `Knowing it rains throws away every dry and stormy morning. Inside the rain block, the late share is ℙ(A∩B)/ℙ(B) = ${fmt(pAB, 3)} / ${fmt(pB, 3)} = <b class="r">${fmt(lr.v, 3)}</b>: the same red area, rescaled so the rain block counts as the whole universe.`
          : `Before looking out of the window: ℙ(late) = <b class="r">${fmt(pl, 3)}</b> (all red area). ℙ(A∩B) = ℙ(late and rain) = ${fmt(pAB, 3)}. Tick the box to condition on rain.`);
      } else if (mode === 'total') {
        ui.say(`ℙ(late) = ${W.map(w => `${fmt(w[2], 2)}·${fmt(w[1], 2)}`).join(' + ')} = <b class="r">${fmt(pl, 3)}</b>: the total red area, a weighted average of the late rates with the weather frequencies as weights.`);
      } else {
        q.clear(); const post = W.map(w => w[1] * w[2] / (pl || 1));
        W.forEach(([n, , , col], i) => { q.rect(i + 0.2, 0, i + 0.8, post[i], { fill: col, op: 0.55 }); q.txt(i + 0.5, post[i], fmt(post[i], 2), { dy: -5 }); q.txt(i + 0.5, 0, n, { dy: 14, size: 11 }); });
        const best = post.indexOf(Math.max(...post));
        ui.say(`You walked in late. Keep only the red parts: each weather's share of the red area is ℙ(weather | late) = ℙ(late | weather)ℙ(weather) / ℙ(late), with ℙ(late) = ${fmt(pl, 3)}. ` +
          `Storm: ${fmt(ls.v, 2)}·${fmt(s, 2)} / ${fmt(pl, 3)} = <b class="r">${fmt(post[2], 3)}</b>. Most likely cause: <b>${W[best][0]}</b>. ` +
          'Try a rare storm that almost always makes you late: it can still lose to the common rain.');
      }
    });
  }
  add(30201, 'Seeing rain shrinks the universe', 'The square is all mornings: block width = chance of the weather, red height = chance of being late in that weather. Tick the box to condition on rain.', ui => weatherWidget(ui, 'cond'));
  add(30203, 'Total probability: weighted average of late rates', 'Each block is a kind of weather (width = how often it happens), and its red part is how often you are late in it. The total red area is ℙ(late).', ui => weatherWidget(ui, 'total'));
  add(30204, 'Bayes: which weather made me late?', 'Same blocks, but now you know you were late. Only the red area remains, and the share of each block in it is the posterior chance of that weather.', ui => weatherWidget(ui, 'bayes'));

  add(30202, 'A morning built step by step', 'Leave on time, then catch the bus, then no jam on the bridge. Each bar keeps a fraction of the one before it: the chain rule multiplies conditional chances.', ui => {
    const a = ui.slider('ℙ(leave on time)', 0, 1, 0.01, 0.8), b = ui.slider('ℙ(bus in 5 min | left on time)', 0, 1, 0.01, 0.7), c = ui.slider('ℙ(no jam | both)', 0, 1, 0.01, 0.6);
    const p = ui.plot({ x: [0, 1], y: [0, 4], h: 220, axes: false, pad: { l: 150, r: 60, t: 8, b: 8 } });
    let sim = null; ui.btn('Simulate 1000 mornings', () => { let k = 0; for (let i = 0; i < 1000; i++) if (Math.random() < a.v && Math.random() < b.v && Math.random() < c.v) k++; sim = k; });
    ui.draw(() => {
      p.clear(); const v = [1, a.v, a.v * b.v, a.v * b.v * c.v], lab = ['all mornings', 'left on time', '… and caught bus', '… and no jam'];
      v.forEach((w, i) => { const y = 3.5 - i; p.rect(0, y - 0.32, w, y + 0.32, { fill: i === 3 ? C.red : C.ink, op: i === 3 ? 0.6 : 0.18 + 0.08 * i }); p.txt(0, y, lab[i], { a: 'end', dx: -8, mid: true, size: 12.5 }); p.txt(w, y, fmt(w, 3), { a: 'start', dx: 6, mid: true, size: 12.5, bold: i === 3 }); });
      ui.say(`ℙ(A₁∩A₂∩A₃) = ℙ(A₁)·ℙ(A₂|A₁)·ℙ(A₃|A₁∩A₂) = ${fmt(a.v, 2)} × ${fmt(b.v, 2)} × ${fmt(c.v, 2)} = <b class="r">${fmt(v[3], 4)}</b>.` +
        (sim != null ? ` Simulation: ${sim} of 1000 mornings got all three (${fmt(sim / 1000, 3)}).` : ''));
      sim = null;
    });
  });

  add(30205, 'Linked through the jam', 'You and a friend ride the same bus. A jam makes both of you likely to be late; given the jam (or no jam) you are late independently. Overall, your lateness tells something about theirs.', ui => {
    const pc = ui.slider('ℙ(jam)', 0, 1, 0.01, 0.3), a1 = ui.slider('ℙ(late | jam)', 0, 1, 0.01, 0.8), a0 = ui.slider('ℙ(late | no jam)', 0, 1, 0.01, 0.1);
    const p = ui.plot({ x: [0, 3], y: [0, 1], h: 230, xt: [], yl: 'chance' });
    ui.draw(() => {
      p.clear();
      const c = pc.v, pa = c * a1.v + (1 - c) * a0.v, both = c * a1.v * a1.v + (1 - c) * a0.v * a0.v, prod = pa * pa;
      const groups = [['overall', both, prod], ['given a jam', a1.v * a1.v, a1.v * a1.v], ['given no jam', a0.v * a0.v, a0.v * a0.v]];
      groups.forEach(([n, x, y], i) => { p.rect(i + 0.15, 0, i + 0.48, x, { fill: C.red, op: 0.6 }); p.rect(i + 0.52, 0, i + 0.85, y, { fill: C.blue, op: 0.5 }); p.txt(i + 0.5, 0, n, { dy: 14, size: 11.5 }); p.txt(i + 0.315, x, fmt(x, 3), { dy: -4, size: 10.5 }); p.txt(i + 0.685, y, fmt(y, 3), { dy: -4, size: 10.5 }); });
      ui.say(`<span class="r">Red</span> = ℙ(both late), <span class="bl">blue</span> = ℙ(you late)·ℙ(friend late). Overall: ${fmt(both, 3)} vs ${fmt(prod, 3)}, ` +
        (Math.abs(both - prod) < 1e-4 ? '<b>equal: independent</b> (the jam does not change the late rate, or it never/always happens).' : `<b class="r">not equal: dependent</b>. ℙ(friend late | you late) = ${fmt(both / (pa || 1), 3)} &gt; ℙ(friend late) = ${fmt(pa, 3)}.`) +
        ' Inside each case (jam / no jam) the bars match: conditionally independent.');
    });
  });

  /* ===================== 03 · Random variables ===================== */
  /* ride time = 20 + Gamma(2, scale 5): mean 30, sd ≈ 7.1 */
  const RIDE = { pdf: x => x <= 20 ? 0 : (x - 20) / 25 * Math.exp(-(x - 20) / 5), cdf: x => x <= 20 ? 0 : 1 - Math.exp(-(x - 20) / 5) * (1 + (x - 20) / 5), draw: () => 20 + M.rexp(0.2) + M.rexp(0.2) };
  add(30301, 'The CDF answers “at most x minutes?” for every x', 'Each tick is one morning\'s ride time. Move x: F(x) is the share of mornings at or below it. The step curve is the data; the smooth curve is the true CDF.', ui => {
    let data = Array.from({ length: 60 }, RIDE.draw);
    const x = ui.slider('x (minutes)', 15, 70, 0.5, 30), n = ui.select('mornings', [['20', '20'], ['60', '60'], ['500', '500']], '60');
    ui.btn('New mornings', () => { data = Array.from({ length: +n.v }, RIDE.draw); });
    const p = ui.plot({ x: [15, 70], y: [0, 1.05], h: 260, xl: 'ride time (min)', yl: 'F(x) = ℙ(X ≤ x)' });
    ui.draw(() => {
      if (data.length !== +n.v) data = Array.from({ length: +n.v }, RIDE.draw);
      const s = [...data].sort((a, b) => a - b), N = s.length;
      p.clear(); p.fn(RIDE.cdf, { c: C.blue, w: 2 });
      const pts = [[15, 0]]; s.forEach((v, i) => { pts.push([v, i / N], [v, (i + 1) / N]); }); pts.push([70, 1]); p.path(pts, { c: C.ink, w: 1.3 });
      s.forEach(v => p.seg(v, 0, v, 0.035, { c: v <= x.v ? C.red : '#888', w: 1 }));
      const k = s.filter(v => v <= x.v).length; p.vline(x.v, { c: C.red }); p.dot(x.v, k / N, { c: C.red });
      ui.say(`${k} of ${N} mornings took at most ${fmt(x.v, 1)} min, so the empirical F(${fmt(x.v, 1)}) = <b class="r">${fmt(k / N, 3)}</b>; the true F(${fmt(x.v, 1)}) = <b class="bl">${fmt(RIDE.cdf(x.v), 3)}</b>. ` +
        'F never goes down, starts at 0 and ends at 1. Try 500 mornings: the step curve hugs the true one.');
    });
  });

  add(30302, 'Missed buses: PMF bars and the step CDF', 'Set how likely you are to miss 0, 1, 2 or 3 buses (the weights are rescaled to add to 1). The CDF jumps by each bar\'s height.', ui => {
    const w = [ui.slider('weight of 0 missed', 0, 1, 0.01, 0.5), ui.slider('weight of 1 missed', 0, 1, 0.01, 0.3), ui.slider('weight of 2 missed', 0, 1, 0.01, 0.15), ui.slider('weight of 3 missed', 0, 1, 0.01, 0.05)];
    const x = ui.slider('read F at x', -0.5, 3.5, 0.05, 1.5);
    const row = ui.row();
    const p = ui.plot({ x: [-0.5, 3.5], y: [0, 1], h: 220, w: 360, into: row, xt: [0, 1, 2, 3], yl: 'p(k)' });
    const q = ui.plot({ x: [-0.5, 3.5], y: [0, 1.05], h: 220, w: 360, into: row, xt: [0, 1, 2, 3], yl: 'F(x)' });
    ui.draw(() => {
      const tot = M.sum(w.map(s => s.v)) || 1, pm = w.map(s => s.v / tot), F = []; pm.reduce((a, v, i) => (F[i] = a + v), 0);
      p.clear(); pm.forEach((v, k) => { p.rect(k - 0.25, 0, k + 0.25, v, { fill: C.blue, op: 0.5 }); p.txt(k, v, fmt(v, 2), { dy: -5 }); });
      q.clear(); let prev = 0;
      for (let k = 0; k < 4; k++) { const nx = k < 3 ? k + 1 : 3.5; q.seg(k, F[k], nx, F[k], { w: 2 }); q.seg(k, prev, k, F[k], { c: C.blue, dash: '3 3', w: 1 }); q.dot(k, prev, { fill: '#fff', stroke: C.ink, r: 3.5 }); q.dot(k, F[k], { r: 3.5 }); prev = F[k]; }
      q.seg(-0.5, 0, 0, 0, { w: 2 });
      const Fx = x.v < 0 ? 0 : F[Math.min(3, Math.floor(x.v))]; q.vline(x.v, { c: C.red }); q.dot(x.v, Fx, { c: C.red });
      ui.say(`F(${fmt(x.v, 2)}) = ℙ(X ≤ ${fmt(x.v, 2)}) = <b class="r">${fmt(Fx, 3)}</b>: the sum of the bars at k ≤ ${fmt(x.v, 2)}. ` +
        'Between whole numbers F is flat; at k it jumps by p(k) (filled dot = the value taken, open dot = the value just before). ℙ(X = 1.5) = 0.');
    });
  });

  add(30303, 'Probability is area under the density', 'The ride-time density. ℙ(a < X ≤ b) is the shaded area. Squeeze b onto a: the area, and the chance of any exact time, goes to 0.', ui => {
    const a = ui.slider('a', 15, 70, 0.1, 25), b = ui.slider('b', 15, 70, 0.1, 35);
    const p = ui.plot({ x: [15, 70], y: [0, 0.08], h: 250, xl: 'ride time (min)', yl: 'f(x)' });
    ui.draw(() => {
      const lo = Math.min(a.v, b.v), hi = Math.max(a.v, b.v);
      p.clear(); p.area(RIDE.pdf, lo, hi, { fill: C.red, op: 0.35 }); p.fn(RIDE.pdf, { w: 2 });
      const pr = RIDE.cdf(hi) - RIDE.cdf(lo);
      ui.say(`ℙ(${fmt(lo, 1)} &lt; X ≤ ${fmt(hi, 1)}) = ∫f = F(${fmt(hi, 1)}) − F(${fmt(lo, 1)}) = <b class="r">${fmt(pr, 4)}</b>. ` +
        `The height f(${fmt(lo, 1)}) = ${fmt(RIDE.pdf(lo), 4)} is not a chance (it is chance per minute). Width ${fmt(hi - lo, 2)} min → ` + (hi - lo < 0.5 ? '<b>almost no area: ℙ(X = c) = 0.</b>' : 'make it tiny to see the area vanish.'));
    });
  });

  add(30304, 'The bus that never owes you', 'Buses come at random, rate λ. You have already waited t minutes. The red curve is the rest of your wait, rescaled: it is exactly the original exponential.', ui => {
    const lam = ui.slider('λ (buses per min)', 0.05, 0.5, 0.01, 0.15), t = ui.slider('already waited t', 0, 20, 0.5, 8, v => v + ' min'), s = ui.slider('extra wait s', 0.5, 20, 0.5, 5, v => v + ' min');
    let sim = null;
    ui.btn('Simulate 5000 waits', () => { const w = []; for (let i = 0; i < 5000; i++) { const x = M.rexp(lam.v); if (x > t.v) w.push(x - t.v); } sim = w; });
    const p = ui.plot({ x: [0, 40], y: [0, 0.5], h: 250, xl: 'minutes', yl: 'density' });
    ui.draw(() => {
      const l = lam.v; p.setY(0, Math.max(0.06, l * 1.1)); p.clear();
      if (sim) p.bars(M.hist(sim, 0, 40, 40).map(([x, h]) => [x + t.v, h]), 1, { fill: C.grey, op: 0.35 });
      p.area(x => l * Math.exp(-l * x), t.v, 40, { fill: C.red, op: 0.12 });
      p.fn(x => l * Math.exp(-l * x), { w: 2 });
      p.fn(x => l * Math.exp(-l * (x - t.v)), { from: t.v, c: C.red, w: 2, dash: '6 4' });
      p.vline(t.v, { c: C.red });
      const a = Math.exp(-l * (t.v + s.v)) / Math.exp(-l * t.v), b = Math.exp(-l * s.v);
      ui.say(`ℙ(X &gt; t + s | X &gt; t) = e^(−λ(t+s)) / e^(−λt) = <b class="r">${fmt(a, 4)}</b> = e^(−λs) = ℙ(X &gt; s) = <b>${fmt(b, 4)}</b>. ` +
        `Mean remaining wait: 1/λ = ${fmt(1 / l, 2)} min, whatever t is.` + (sim ? ` Simulation: of the waits longer than ${t.v} min (${sim.length} of 5000), the extra wait averages <b>${fmt(M.mean(sim), 2)}</b> min (grey bars).` : ''));
      sim = null;
    });
  });

  add(30305, 'How many spreads late?', 'Ride time X ~ 𝒩(μ, σ²). Subtracting μ and dividing by σ turns any bell into the standard one. The shaded chance is the same on both.', ui => {
    const mu = ui.slider('μ (typical ride)', 15, 45, 0.5, 30), sg = ui.slider('σ (spread)', 1, 12, 0.1, 5), x = ui.slider('today\'s ride x', 5, 60, 0.5, 38);
    const row = ui.row();
    const p = ui.plot({ x: [0, 65], y: [0, 0.42], h: 220, w: 380, into: row, xl: 'X (min)' });
    const q = ui.plot({ x: [-4, 4], y: [0, 0.42], h: 220, w: 340, into: row, xl: 'Z = (X − μ)/σ' });
    ui.draw(() => {
      const z = (x.v - mu.v) / sg.v, f = v => M.npdf(v, mu.v, sg.v);
      p.setY(0, Math.max(0.09, 1.15 * f(mu.v))); p.clear(); p.area(f, 0, Math.min(x.v, 65), { op: 0.3 }); p.fn(f, { w: 2 }); p.vline(mu.v); p.vline(x.v, { c: C.red, dash: null });
      q.clear(); q.area(v => M.npdf(v), -4, M.clamp(z, -4, 4), { op: 0.3 }); q.fn(v => M.npdf(v), { w: 2 }); q.vline(M.clamp(z, -4, 4), { c: C.red, dash: null });
      ui.say(`z = (${fmt(x.v, 1)} − ${fmt(mu.v, 1)}) / ${fmt(sg.v, 1)} = <b class="r">${fmt(z, 2)}</b> spreads ${z >= 0 ? 'late' : 'early'}. ℙ(X ≤ ${fmt(x.v, 1)}) = Φ(${fmt(z, 2)}) = <b>${fmt(M.Phi(z), 4)}</b>, the same shaded area on both curves. ` +
        `Rides more than 2 spreads late happen on ${pct(1 - M.Phi(2))} of mornings, whatever μ and σ are.`);
    });
  });

  /* ===================== 04 · Transformations ===================== */
  add(30401, 'CDF method: which x make g(x) ≤ y?', 'X = minutes late (negative = early), X ~ 𝒩(0, 1). Pick what you compute from it. For a level y, the red stretch of the x-axis is {x : g(x) ≤ y}; its chance is F_Y(y).', ui => {
    const G = { sq: [x => x * x, 'penalty X²', y => y < 0 ? 0 : 2 * M.Phi(Math.sqrt(y)) - 1, [0, 6]], abs: [x => Math.abs(x), 'gap |X|', y => y < 0 ? 0 : 2 * M.Phi(y) - 1, [0, 3]], fare: [x => Math.exp(x / 2), 'fare e^(X/2)', y => y <= 0 ? 0 : M.Phi(2 * Math.log(y)), [0, 5]] };
    const g = ui.select('Y = g(X)', [['sq', 'penalty Y = X²'], ['abs', 'gap Y = |X|'], ['fare', 'fare Y = e^(X/2)']], 'sq');
    const y = ui.slider('level y', 0.01, 6, 0.01, 1.5);
    const row = ui.row();
    const p = ui.plot({ x: [-3.2, 3.2], y: [-0.2, 6], h: 240, w: 380, into: row, xl: 'x (minutes late)', yl: 'g(x)' });
    const q = ui.plot({ x: [0, 6], y: [0, 1.05], h: 240, w: 330, into: row, xl: 'y', yl: 'F_Y(y)' });
    ui.draw(() => {
      const [f, , FY, xr] = G[g.v], yy = Math.min(y.v, xr[1]);
      p.clear(); p.area(x => 1.3 * M.npdf(x) * 4 - 0.2, -3.2, 3.2, { fill: C.grey, op: 0.12, base: -0.2 });
      const xs = M.range(-3.2, 3.2, 641);
      let run = null; xs.forEach((x, i) => { const ok = f(x) <= yy; if (ok && run == null) run = x; if ((!ok || i === xs.length - 1) && run != null) { p.rect(run, -0.2, x, 0.05, { fill: C.red, op: 0.7 }); p.area(t => 1.3 * M.npdf(t) * 4 - 0.2, run, x, { fill: C.red, op: 0.3, base: -0.2 }); run = null; } });
      p.fn(f, { w: 2 }); p.hline(yy, { c: C.red, dash: '5 4' });
      q.setX(xr[0], xr[1]); q.clear(); q.fn(FY, { c: C.blue, w: 2 }); q.dot(yy, FY(yy), { c: C.red }); q.vline(yy, { c: C.red });
      ui.say(`{x : g(x) ≤ ${fmt(yy, 2)}} is the red stretch (grey hill = density of X). Its chance is F_Y(${fmt(yy, 2)}) = <b class="r">${fmt(FY(yy), 4)}</b>` +
        (g.v === 'sq' ? `: the stretch is [−√y, √y], so F_Y(y) = Φ(√y) − Φ(−√y) = 2Φ(√y) − 1. Two branches of x feed one y.` : g.v === 'abs' ? ': the stretch is [−y, y].' : ': g is increasing, so the stretch is (−∞, 2 ln y] and F_Y(y) = Φ(2 ln y).'));
    });
  });

  add(30402, 'Minutes into speed: the 1D Jacobian', 'Ride time X ~ Uniform(20, 40) minutes over 10 km, speed Y = 600/X km/h. A band of width dx maps to a band dy holding the same chance, so the density rescales by |dx/dy|.', ui => {
    const x = ui.slider('ride time x', 20.5, 39.5, 0.1, 25, v => fmt(v, 1) + ' min'), dx = ui.slider('band width dx', 0.2, 3, 0.1, 1.5, v => fmt(v, 1) + ' min');
    let sim = null; ui.btn('Simulate 5000 rides', () => { sim = Array.from({ length: 5000 }, () => 600 / (20 + 20 * Math.random())); });
    const row = ui.row();
    const p = ui.plot({ x: [18, 42], y: [0, 0.08], h: 220, w: 340, into: row, xl: 'ride time x (min)', yl: 'f_X' });
    const q = ui.plot({ x: [14, 31], y: [0, 0.16], h: 220, w: 380, into: row, xl: 'speed y (km/h)', yl: 'f_Y' });
    const fY = y => (y < 15 || y > 30) ? 0 : (1 / 20) * 600 / (y * y);
    ui.draw(() => {
      const a = x.v - dx.v / 2, b = Math.min(40, x.v + dx.v / 2), ya = 600 / b, yb = 600 / Math.max(20, a);
      p.clear(); p.rect(20, 0, 40, 0.05, { fill: C.blue, op: 0.15, c: C.blue }); p.rect(Math.max(20, a), 0, b, 0.05, { fill: C.red, op: 0.55 });
      q.clear(); if (sim) q.bars(M.hist(sim, 14, 31, 34), 0.5, { fill: C.grey, op: 0.35 });
      q.area(fY, ya, yb, { fill: C.red, op: 0.55 }); q.fn(fY, { w: 2, c: C.blue, n: 400 });
      const pr = (b - Math.max(20, a)) / 20;
      ui.say(`The red band of ride times has chance (dx)/20 = <b class="r">${fmt(pr, 4)}</b>. It maps to speeds ${fmt(ya, 2)}–${fmt(yb, 2)} km/h, width dy = ${fmt(yb - ya, 3)}, carrying the same chance. ` +
        `So f_Y(y) = f_X(x)·|dx/dy| = (1/20)·600/y²: at y = ${fmt(600 / x.v, 2)}, f_Y = <b>${fmt(fY(600 / x.v), 4)}</b>. Short rides (fast speeds) get squeezed, so the density is lower there.` + (sim ? ' Grey: 5000 simulated speeds.' : ''));
    });
  });

  /* ===================== 05 · Expectation ===================== */
  add(30501, 'The average trip is the sum of the average legs', 'Walk ~ Uniform, wait ~ Exponential, ride ~ Normal. Add a rain link that makes long waits come with long rides: the average total still equals the sum of the averages.', ui => {
    const mw = ui.slider('average walk', 4, 20, 0.5, 8), mt = ui.slider('average wait', 2, 20, 0.5, 6), mr = ui.slider('average ride', 10, 50, 0.5, 25);
    const link = ui.check('rain links wait and ride (dependent legs)', false);
    let runs = [];
    ui.btn('Simulate 2000 mornings', () => {
      runs = [];
      for (let i = 0; i < 2000; i++) {
        const rain = link.v && Math.random() < 0.3, walk = mw.v * 2 * Math.random();
        const wait = M.rexp(1 / mt.v) * (link.v ? (rain ? 2 : 0.5714) : 1); // mean kept: 0.3·2 + 0.7·0.5714 = 1
        const ride = mr.v + (link.v ? (rain ? 8 : -3.4286) : 0) + 4 * M.rnorm();
        runs.push([walk, wait, ride]);
      }
    });
    const p = ui.plot({ x: [0, 90], y: [0, 3], h: 160, axes: false, pad: { l: 110, r: 20, t: 10, b: 10 } });
    ui.draw(() => {
      p.clear(); const m = [mw.v, mt.v, mr.v], cols = [C.green, C.amber, C.blue], names = ['walk', 'wait', 'ride'];
      let x = 0; m.forEach((v, i) => { p.rect(x, 1.8, x + v, 2.6, { fill: cols[i], op: 0.6 }); p.txt(x + v / 2, 2.2, names[i], { mid: true, size: 11.5 }); x += v; });
      p.txt(0, 2.2, 'sum of averages', { a: 'end', dx: -8, mid: true, size: 12 });
      let msg = `𝔼[walk + wait + ride] = ${fmt(mw.v, 1)} + ${fmt(mt.v, 1)} + ${fmt(mr.v, 1)} = <b class="r">${fmt(x, 1)}</b> min. `;
      if (runs.length) {
        const tot = M.mean(runs.map(r => r[0] + r[1] + r[2]));
        p.rect(0, 0.5, tot, 1.3, { fill: C.red, op: 0.55 }); p.txt(0, 0.9, 'simulated average', { a: 'end', dx: -8, mid: true, size: 12 });
        msg += `Simulated average total: <b>${fmt(tot, 2)}</b> min${link.v ? ', even though rain makes the wait and the ride move together' : ''}. Linearity needs no independence.`;
      } else msg += 'Press simulate, with and without the rain link.';
      ui.say(msg);
    });
  });

  add(30502, 'Average ride = area under the survival curve', 'ℙ(X > t) is the chance the ride is still going at minute t. Adding those chances minute by minute (the shaded area) gives 𝔼[X].', ui => {
    const shape = ui.select('ride law', [['exp', 'Exponential'], ['uni', 'Uniform(0, b)'], ['gam', 'Gamma(2): two exponential halves'], ['cnt', 'whole minutes (Geometric)']], 'exp');
    const m = ui.slider('mean / scale', 2, 30, 0.5, 12);
    const p = ui.plot({ x: [0, 80], y: [0, 1.05], h: 240, xl: 't (min)', yl: 'ℙ(X > t)' });
    ui.draw(() => {
      const S = { exp: t => Math.exp(-t / m.v), uni: t => M.clamp(1 - t / (2 * m.v), 0, 1), gam: t => Math.exp(-2 * t / m.v) * (1 + 2 * t / m.v), cnt: t => Math.pow(1 - 1 / m.v, Math.floor(t)) }[shape.v];
      p.clear();
      let area;
      if (shape.v === 'cnt') { area = 0; for (let k = 0; k < 80; k++) { const s = Math.pow(1 - 1 / m.v, k); area += s; p.rect(k, 0, k + 1, s, { fill: C.red, op: 0.3, c: '#fff', w: 0.5 }); } }
      else { p.area(S, 0, 80, { fill: C.red, op: 0.3, n: 300 }); area = M.integrate(S, 0, 400, 4000); }
      p.fn(S, { w: 2, n: 400 });
      ui.say(`Shaded area = ${shape.v === 'cnt' ? '∑ₖ ℙ(X ≥ k+1)… = ∑ₖ₌₀ ℙ(X > k)' : '∫₀^∞ ℙ(X > t) dt'} = <b class="r">${fmt(area, 3)}</b>, and the true mean is <b>${fmt(m.v, 3)}</b>. ` +
        'Each minute contributes the chance that the ride is still on at that minute: a long tail adds a lot.');
    });
  });

  add(30503, 'Var(X + Y): the square with the cross terms', 'Wait X and ride Y. The square of sides σ_X and σ_Y splits into Var X, Var Y and two copies of Cov(X, Y). Negative covariance subtracts.', ui => {
    const sx = ui.slider('σ wait', 0.5, 6, 0.1, 3), sy = ui.slider('σ ride', 0.5, 6, 0.1, 4), r = ui.slider('correlation ρ', -1, 1, 0.01, 0.5);
    let sim = null; ui.btn('Simulate 4000 mornings', () => { sim = Array.from({ length: 4000 }, () => M.rbiv(0, 0, sx.v, sy.v, r.v)); });
    const row = ui.row();
    const p = ui.plot({ x: [0, 12], y: [0, 12], w: 300, h: 300, axes: false, into: row });
    const q = ui.plot({ x: [-15, 15], y: [-15, 15], w: 300, h: 300, into: row, xl: 'wait', yl: 'ride' });
    ui.draw(() => {
      const a = sx.v, b = sy.v, cov = r.v * a * b, tot = a * a + b * b + 2 * cov;
      p.clear(); const ccol = cov >= 0 ? C.amber : C.purple;
      p.rect(0, 12 - a, a, 12, { fill: C.blue, op: 0.45, c: '#333' }); p.txt(a / 2, 12 - a / 2, 'Var X', { mid: true });
      p.rect(a, 12 - a - b, a + b, 12 - a, { fill: C.green, op: 0.45, c: '#333' }); p.txt(a + b / 2, 12 - a - b / 2, 'Var Y', { mid: true });
      p.rect(a, 12 - a, a + b, 12, { fill: ccol, op: 0.2 + 0.5 * Math.abs(r.v), c: '#333' }); p.txt(a + b / 2, 12 - a / 2, 'Cov', { mid: true });
      p.rect(0, 12 - a - b, a, 12 - a, { fill: ccol, op: 0.2 + 0.5 * Math.abs(r.v), c: '#333' }); p.txt(a / 2, 12 - a - b / 2, 'Cov', { mid: true });
      q.clear(); if (sim) sim.slice(0, 800).forEach(([x, y]) => q.dot(x, y, { r: 1.6, op: 0.4 }));
      ui.say(`Var(X+Y) = Var X + Var Y + 2Cov = ${fmt(a * a, 2)} + ${fmt(b * b, 2)} + 2·(${fmt(cov, 2)}) = <b class="r">${fmt(tot, 2)}</b>` +
        (sim ? `; simulated: <b>${fmt(M.variance(sim.map(([x, y]) => x + y)), 2)}</b>.` : '.') +
        ` Independent legs (ρ = 0) just add: ${fmt(a * a + b * b, 2)}. ${r.v > 0 ? 'Rain lengthening both makes bad mornings stack up.' : r.v < 0 ? 'A long wait with a short ride cancels out, so the total is steadier.' : ''}`);
    });
  });

  /* ===================== 06 · Inequalities ===================== */
  add(30601, 'Markov: long rides cannot be common', 'Know only the average ride. Pick a threshold a: the chance of a ride at least a is at most 𝔼[X]/a, whatever the shape. The two-point law makes the bound exact.', ui => {
    const mu = ui.slider('average ride 𝔼[X]', 5, 40, 0.5, 30), a = ui.slider('threshold a', 5, 150, 1, 90), law = ui.select('ride law', [['exp', 'Exponential'], ['gam', 'Gamma(4), less spread'], ['two', 'worst case: 0 or a']], 'exp');
    const p = ui.plot({ x: [0, 160], y: [0, 0.1], h: 240, xl: 'ride (min)', yl: 'density' });
    ui.draw(() => {
      const m = mu.v, A = a.v; let tail;
      p.clear();
      if (law.v === 'two') {
        const w = Math.min(1, m / A); tail = A >= m ? w : 1;
        p.setY(0, 1.05); p.clear(); p.rect(-1.5, 0, 1.5, 1 - w, { fill: C.blue, op: 0.6 }); p.rect(A - 1.5, 0, A + 1.5, w, { fill: C.red, op: 0.7 });
        p.txt(A, w, `ℙ = ${fmt(w, 3)}`, { dy: -6 });
      } else {
        const k = law.v === 'exp' ? 1 : 4, rate = k / m, f = x => M.gammaPdf(x, k, rate);
        tail = M.integrate(f, A, A + 400, 2000);
        p.setY(0, f(law.v === 'exp' ? 0.001 : (k - 1) / rate) * 1.15); p.clear(); p.area(f, A, 160, { fill: C.red, op: 0.35 }); p.fn(f, { w: 2, from: 0.001 });
      }
      p.vline(m, { c: C.blue }); p.vline(A, { c: C.red, dash: null });
      ui.say(`True ℙ(X ≥ ${A}) = <b class="r">${fmt(tail, 4)}</b> ≤ 𝔼[X]/a = ${fmt(m, 1)}/${A} = <b>${fmt(Math.min(1, m / A), 4)}</b>. ` +
        (law.v === 'two' ? 'The worst case puts all the tail chance exactly at a and the rest at 0: then the bound is met with equality.' : 'Crude but always valid: it used only the mean and X ≥ 0.'));
    });
  });

  add(30602, 'Chebyshev: far-off days are rare', 'Average ride μ = 30, spread σ. Mornings more than ε away from 30 have total chance at most σ²/ε², for any shape.', ui => {
    const sg = ui.slider('σ', 1, 10, 0.1, 5), eps = ui.slider('ε (minutes off)', 1, 30, 0.5, 15), law = ui.select('ride law', [['n', 'Normal'], ['u', 'Uniform'], ['t', 'worst case: 3 points']], 'n');
    const p = ui.plot({ x: [-10, 70], y: [0, 0.2], h: 240, xl: 'ride (min)', yl: 'density' });
    ui.draw(() => {
      const s = sg.v, e = eps.v, mu = 30, bound = Math.min(1, s * s / (e * e)); let tail;
      p.clear();
      if (law.v === 'n') { const f = x => M.npdf(x, mu, s); p.setY(0, f(mu) * 1.15); p.clear(); p.area(f, -10, mu - e, { op: 0.4 }); p.area(f, mu + e, 70, { op: 0.4 }); p.fn(f, { w: 2 }); tail = 2 * (1 - M.Phi(e / s)); }
      else if (law.v === 'u') { const h = s * Math.sqrt(3), f = x => Math.abs(x - mu) <= h ? 1 / (2 * h) : 0; p.setY(0, 1.3 / (2 * h)); p.clear(); if (e < h) { p.rect(mu - h, 0, mu - e, 1 / (2 * h), { op: 0.4 }); p.rect(mu + e, 0, mu + h, 1 / (2 * h), { op: 0.4 }); } p.fn(f, { w: 2, n: 800 }); tail = Math.max(0, (h - e) / h); }
      else { const q = Math.min(1, s * s / (e * e)), d = q >= 1 ? s : e; p.setY(0, 1.05); p.clear(); p.rect(mu - 0.6, 0, mu + 0.6, 1 - q, { fill: C.blue, op: 0.6 }); [mu - d, mu + d].forEach(x => p.rect(x - 0.6, 0, x + 0.6, q / 2, { op: 0.7 })); tail = q; }
      p.vline(mu - e, { c: C.red }); p.vline(mu + e, { c: C.red });
      ui.say(`ℙ(|X − 30| ≥ ${fmt(e, 1)}) = <b class="r">${fmt(tail, 4)}</b> ≤ σ²/ε² = ${fmt(s * s, 2)}/${fmt(e * e, 2)} = <b>${fmt(bound, 4)}</b>. With ε = 3σ the bound is 1/9 ≈ 0.111 for every shape; ` +
        (law.v === 't' ? 'the 3-point law (mass at 30 and at 30 ± ε) meets it exactly.' : 'a bell actually gives much less.'));
    });
  });

  /* ===================== 07 · Joint distributions ===================== */
  function cloud(n, r) { return Array.from({ length: n }, () => { const [x, y] = M.rbiv(8, 28, 3, 5, r); return [x, y]; }); }
  add(30701, 'A rectangle from four corners', 'Each dot is a morning (wait, ride). F(x, y) counts the dots to the lower-left of (x, y). The rectangle\'s share is F(b,d) − F(a,d) − F(b,c) + F(a,c).', ui => {
    let pts = cloud(500, 0.5);
    const a = ui.slider('a (wait from)', 0, 16, 0.25, 6), b = ui.slider('b (wait to)', 0, 16, 0.25, 11), c = ui.slider('c (ride from)', 10, 46, 0.5, 24), d = ui.slider('d (ride to)', 10, 46, 0.5, 34);
    ui.btn('New mornings', () => { pts = cloud(500, 0.5); });
    const p = ui.plot({ x: [0, 16], y: [10, 46], h: 280, xl: 'wait (min)', yl: 'ride (min)' });
    ui.draw(() => {
      const F = (x, y) => pts.filter(([u, v]) => u <= x && v <= y).length / pts.length;
      const [A, B] = [Math.min(a.v, b.v), Math.max(a.v, b.v)], [Cc, D] = [Math.min(c.v, d.v), Math.max(c.v, d.v)];
      p.clear(); p.rect(A, Cc, B, D, { fill: C.red, op: 0.12, c: C.red, w: 1.5 });
      pts.forEach(([x, y]) => p.dot(x, y, { r: 2, c: x > A && x <= B && y > Cc && y <= D ? C.red : '#666', op: 0.55 }));
      [[B, D, '+'], [A, D, '−'], [B, Cc, '−'], [A, Cc, '+']].forEach(([x, y, s]) => { p.dot(x, y, { r: 5, fill: '#fff', stroke: C.ink }); p.txt(x, y, s, { mid: true, size: 11, bold: true }); });
      const v = [F(B, D), F(A, D), F(B, Cc), F(A, Cc)], inside = pts.filter(([x, y]) => x > A && x <= B && y > Cc && y <= D).length / pts.length;
      ui.say(`F(b,d) − F(a,d) − F(b,c) + F(a,c) = ${fmt(v[0], 3)} − ${fmt(v[1], 3)} − ${fmt(v[2], 3)} + ${fmt(v[3], 3)} = <b class="r">${fmt(v[0] - v[1] - v[2] + v[3], 3)}</b>, and the share of red dots is <b>${fmt(inside, 3)}</b>. ` +
        'The lower-left corner region gets subtracted twice, so it is added back once.');
    });
  });

  /* a two-blob joint density for (wait, ride): dry mornings and rainy mornings */
  const J = {
    f(x, y, r = 0.4) { const g = (x, y, m1, m2, s1, s2, rr) => { const u = (x - m1) / s1, v = (y - m2) / s2, q = (u * u - 2 * rr * u * v + v * v) / (1 - rr * rr); return Math.exp(-q / 2) / (2 * Math.PI * s1 * s2 * Math.sqrt(1 - rr * rr)); }; return 0.65 * g(x, y, 5, 24, 2, 3.5, r) + 0.35 * g(x, y, 11, 34, 2.5, 4, r); },
    xs: [0, 18], ys: [10, 48],
  };
  add(30702, 'Probability as volume under the hill', 'Darker = more common (wait, ride) pairs. Pick the region “wait under s and ride over t”: its chance is the volume of the hill over it.', ui => {
    const s = ui.slider('wait under s', 0, 18, 0.25, 6), t = ui.slider('ride over t', 10, 48, 0.5, 30), r = ui.slider('link ρ inside each weather', -0.8, 0.9, 0.05, 0.4);
    const p = ui.plot({ x: J.xs, y: J.ys, h: 300, xl: 'wait (min)', yl: 'ride (min)' });
    ui.draw(() => {
      p.clear(); p.heat((x, y) => J.f(x, y, r.v), { nx: 54, ny: 38 });
      p.rect(0, t.v, s.v, 48, { fill: C.red, op: 0.18, c: C.red, w: 2 });
      let vol = 0; const nx = 120, ny = 120, hx = s.v / nx, hy = (48 - t.v) / ny;
      for (let i = 0; i < nx; i++) for (let j = 0; j < ny; j++) vol += J.f((i + 0.5) * hx, t.v + (j + 0.5) * hy, r.v) * hx * hy;
      ui.say(`ℙ(wait &lt; ${fmt(s.v, 2)}, ride &gt; ${fmt(t.v, 1)}) = ∬ f dx dy over the red box = <b class="r">${fmt(vol, 4)}</b>. ` +
        'The height f(x, y) itself is a density (chance per minute²); only volumes are probabilities. Move the box over the dark rain blob to see the volume grow.');
    });
  });

  add(30703, 'Marginal: add up each column', 'Slide x along the waits. The column of the joint picture at x is added up over all rides; doing that for every x draws the marginal density of the wait.', ui => {
    const x = ui.slider('wait x', 0, 18, 0.1, 6);
    const p = ui.plot({ x: J.xs, y: J.ys, h: 240, xl: '', yl: 'ride' });
    const q = ui.plot({ x: J.xs, y: [0, 0.2], h: 150, xl: 'wait (min)', yl: 'f_X(x)' });
    const fX = u => M.integrate(y => J.f(u, y), 0, 70, 300);
    ui.draw(() => {
      p.clear(); p.heat((u, v) => J.f(u, v), { nx: 54, ny: 34 }); p.rect(x.v - 0.18, 10, x.v + 0.18, 48, { fill: C.red, op: 0.45 });
      q.clear(); q.fn(fX, { w: 2, n: 120 }); q.area(fX, 0, x.v, { fill: C.blue, op: 0.12, n: 80 }); const v = fX(x.v); q.seg(x.v, 0, x.v, v, { c: C.red, w: 3 }); q.dot(x.v, v, { c: C.red });
      ui.say(`f_X(${fmt(x.v, 1)}) = ∫ f(${fmt(x.v, 1)}, y) dy = <b class="r">${fmt(v, 4)}</b>: everything in the red column, squashed onto the wait axis. ` +
        'The two bumps of the marginal are the dry and the rainy mornings; the ride information is gone.');
    });
  });

  add(30704, 'Conditional: slice and rescale', 'Fix your wait x. The slice of the joint picture at x (grey) has some area f_X(x); dividing by it gives the conditional density of the ride (red), with area 1.', ui => {
    const x = ui.slider('your wait x', 0.5, 17.5, 0.1, 5);
    const row = ui.row();
    const p = ui.plot({ x: J.xs, y: J.ys, h: 260, w: 330, into: row, xl: 'wait', yl: 'ride' });
    const q = ui.plot({ x: J.ys, y: [0, 0.14], h: 260, w: 390, into: row, xl: 'ride y (min)', yl: 'density' });
    ui.draw(() => {
      p.clear(); p.heat((u, v) => J.f(u, v), { nx: 40, ny: 34 }); p.vline(x.v, { c: C.red, dash: null, w: 2.5 });
      const slice = y => J.f(x.v, y), area = M.integrate(slice, 0, 70, 400), cond = y => slice(y) / area;
      const peak = Math.max(...M.range(10, 48, 200).map(cond));
      q.setY(0, Math.max(0.05, peak * 1.15)); q.clear(); q.area(slice, 10, 48, { fill: C.grey, op: 0.3 }); q.fn(cond, { c: C.red, w: 2.2 });
      const mean = M.integrate(y => y * cond(y), 0, 70, 400); q.vline(mean, { c: C.red });
      ui.say(`Slice area f_X(${fmt(x.v, 1)}) = ${fmt(area, 4)}. f(y | x) = f(x, y)/f_X(x) has area 1; the average ride given this wait is 𝔼[Y | X = ${fmt(x.v, 1)}] = <b class="r">${fmt(mean, 2)}</b> min. ` +
        'A long wait usually means rain, so the conditional ride shifts up.');
    });
  });

  add(30705, 'Independence and the shape of the support', 'Rectangle: f = 4xy on [0,1]². Triangle: f = 8xy on 0 ≤ x ≤ y ≤ 1. Both formulas factor into “x-part × y-part”, but only one is independent. Move x and watch the allowed rides.', ui => {
    const sup = ui.select('support', [['rect', 'rectangle [0,1]², f = 4xy'], ['tri', 'triangle 0 ≤ x ≤ y ≤ 1, f = 8xy']], 'tri');
    const x = ui.slider('x (wait)', 0.02, 0.98, 0.01, 0.6);
    const row = ui.row();
    const p = ui.plot({ x: [0, 1], y: [0, 1], w: 300, h: 300, into: row, xl: 'x', yl: 'y' });
    const q = ui.plot({ x: [0, 1], y: [0, 4.2], w: 400, h: 300, into: row, xl: 'y', yl: 'f(y | x)' });
    ui.draw(() => {
      const tri = sup.v === 'tri', f = (u, v) => tri ? (u <= v ? 8 * u * v : 0) : 4 * u * v;
      p.clear(); p.heat(f, { nx: 40, ny: 40 }); p.vline(x.v, { c: C.red, dash: null, w: 2 });
      const cond = y => tri ? (y >= x.v ? 2 * y / (1 - x.v * x.v) : 0) : 2 * y;
      q.clear(); q.fn(y => 2 * y, { c: C.grey, dash: '5 4' }); q.fn(cond, { c: C.red, w: 2.2, n: 400 });
      const fx = tri ? 4 * x.v * (1 - x.v * x.v) : 2 * x.v, y0 = 0.9, fy = tri ? 4 * y0 ** 3 : 2 * y0;
      ui.say(tri
        ? `Given x = ${fmt(x.v, 2)}, the ride must be ≥ x: f(y | x) = 2y/(1 − x²) on [x, 1] (red) changes with x, so X and Y are <b class="r">dependent</b>. Check at (x, 0.9): f = ${fmt(f(x.v, y0), 3)} but f_X·f_Y = ${fmt(fx, 3)}·${fmt(fy, 3)} = ${fmt(fx * fy, 3)}. The coupled limit x ≤ y spoils the factorisation.`
        : `On the rectangle, f(y | x) = 2y for every x (red sits on the dashed curve): <b class="g">independent</b>. f = 4xy = (2x)(2y) = f_X·f_Y everywhere, because the allowed rides never depend on the wait.`);
    });
  });

  /* ===================== 08 · Order statistics ===================== */
  add(30801, 'First and last of n routes', 'n routes to campus, each arriving after a Uniform(0, 20)-minute wait. The first arrival is short unless every route is slow; the last is long unless every route is quick.', ui => {
    const n = ui.slider('number of routes n', 1, 10, 1, 4, v => v);
    let trials = [];
    const sim = () => { trials = Array.from({ length: 3000 }, () => Array.from({ length: n.v }, () => 20 * Math.random())); };
    ui.btn('Simulate 3000 mornings', sim);
    const row = ui.row();
    const t = ui.plot({ x: [0, 20], y: [0, 6], h: 120, w: 760, into: row, axes: false, pad: { l: 20, r: 20, t: 6, b: 6 } });
    const p = ui.plot({ x: [0, 20], y: [0, 0.5], h: 230, xl: 'minutes', yl: 'density' });
    ui.draw(() => {
      if (!trials.length || trials[0].length !== n.v) sim();
      const N = n.v, F = x => x / 20, f = () => 1 / 20;
      t.clear(); trials.slice(0, 5).forEach((tr, i) => { const y = 5.2 - i; t.seg(0, y, 20, y, { c: '#ddd' }); const lo = Math.min(...tr), hi = Math.max(...tr); tr.forEach(v => t.dot(v, y, { r: 3.5, c: v === lo ? C.blue : v === hi ? C.red : '#999' })); });
      const mins = trials.map(a => Math.min(...a)), maxs = trials.map(a => Math.max(...a));
      const fmin = x => N * Math.pow(1 - F(x), N - 1) * f(), fmax = x => N * Math.pow(F(x), N - 1) * f();
      p.setY(0, Math.max(0.1, N / 20 * 1.15)); p.clear();
      p.bars(M.hist(mins, 0, 20, 40), 0.5, { fill: C.blue, op: 0.3 }); p.bars(M.hist(maxs, 0, 20, 40), 0.5, { fill: C.red, op: 0.3 });
      p.fn(fmin, { c: C.blue, w: 2 }); p.fn(fmax, { c: C.red, w: 2 });
      ui.say(`Top: five mornings, <span class="bl">first</span> and <span class="r">last</span> arrivals marked. ` +
        `ℙ(first &gt; x) = (1 − x/20)ⁿ and ℙ(last ≤ x) = (x/20)ⁿ, so f_first = n(1−F)ⁿ⁻¹f and f_last = nFⁿ⁻¹f (curves). ` +
        `Average first wait: <b class="bl">${fmt(M.mean(mins), 2)}</b> (theory 20/(n+1) = ${fmt(20 / (N + 1), 2)}), average last: <b class="r">${fmt(M.mean(maxs), 2)}</b> (theory 20n/(n+1) = ${fmt(20 * N / (N + 1), 2)}).`);
    });
  });

  /* ===================== 09 · Sums ===================== */
  add(30901, 'Convolution: every way to make z minutes', 'Walk X and wait Y. Flip the wait density and slide it to z; the overlap of f_X(x) and f_Y(z − x) adds up to the density of the total at z.', ui => {
    const lx = ui.select('walk law', [['u', 'Uniform(5, 15)'], ['e', 'Exponential, mean 6']], 'u'), ly = ui.select('wait law', [['u', 'Uniform(0, 10)'], ['e', 'Exponential, mean 6']], 'e');
    const z = ui.slider('total z', 0, 45, 0.25, 15);
    const D = { u: (a, b) => x => (x >= a && x <= b) ? 1 / (b - a) : 0, e: () => x => x >= 0 ? Math.exp(-x / 6) / 6 : 0 };
    const p = ui.plot({ x: [-5, 45], y: [0, 0.22], h: 200, xl: 'x (minutes of walk)' });
    const q = ui.plot({ x: [0, 45], y: [0, 0.12], h: 170, xl: 'z (total minutes)', yl: 'f_Z(z)' });
    ui.draw(() => {
      const fx = lx.v === 'u' ? D.u(5, 15) : D.e(), fy = ly.v === 'u' ? D.u(0, 10) : D.e();
      const fz = s => M.integrate(x => fx(x) * fy(s - x), 0, 45, 500);
      p.clear(); p.fn(fx, { c: C.blue, w: 2, n: 500 }); p.fn(x => fy(z.v - x), { c: C.amber, w: 2, n: 500 }); p.area(x => fx(x) * fy(z.v - x) * 8, -5, 45, { fill: C.red, op: 0.45, n: 500 }); p.vline(z.v);
      const zs = M.range(0, 45, 120), vals = zs.map(fz), mx = Math.max(...vals);
      q.setY(0, mx * 1.2); q.clear(); q.path(zs.map((s, i) => [s, vals[i]]), { w: 2 }); q.dot(z.v, fz(z.v), { c: C.red });
      ui.say(`<span class="bl">Blue</span> f_X(x), <span style="color:#d98a00">amber</span> f_Y(z − x) (flipped and slid to z), <span class="r">red</span> their product (scaled ×8). ` +
        `Its area is f_Z(${fmt(z.v, 2)}) = ∫ f_X(x) f_Y(z − x) dx = <b class="r">${fmt(fz(z.v), 4)}</b>, the red dot below.`);
    });
  });

  add(30905, 'Families that survive addition', 'Add two independent legs. Normal + Normal is Normal (means add, variances add); Poisson + Poisson is Poisson (rates add). Simulated totals (bars) sit on the predicted law (curve).', ui => {
    const fam = ui.select('family', [['n', 'Normal: walk + wait times'], ['p', 'Poisson: buses on two routes']], 'n');
    const a = ui.slider('leg 1: mean (μ₁ or λ₁)', 1, 20, 0.5, 8), sa = ui.slider('leg 1: σ₁ (Normal only)', 0.5, 6, 0.1, 2);
    const b = ui.slider('leg 2: mean (μ₂ or λ₂)', 1, 20, 0.5, 5), sb = ui.slider('leg 2: σ₂ (Normal only)', 0.5, 6, 0.1, 3);
    let sims = null; ui.btn('Simulate 5000 totals', () => { sims = fam.v === 'n' ? Array.from({ length: 5000 }, () => a.v + sa.v * M.rnorm() + b.v + sb.v * M.rnorm()) : Array.from({ length: 5000 }, () => M.rpois(a.v) + M.rpois(b.v)); });
    const p = ui.plot({ x: [-5, 50], y: [0, 0.3], h: 250, xl: fam.v === 'n' ? 'minutes' : 'buses' });
    ui.draw(() => {
      if (sims && sims.fam !== fam.v && sims.fam) sims = null;
      p.clear();
      if (fam.v === 'n') {
        const m = a.v + b.v, s = Math.hypot(sa.v, sb.v), f1 = x => M.npdf(x, a.v, sa.v), f2 = x => M.npdf(x, b.v, sb.v), fs = x => M.npdf(x, m, s);
        p.setY(0, Math.max(f1(a.v), f2(b.v)) * 1.15); p.clear(); if (sims) p.bars(M.hist(sims, -5, 50, 55), 1, { fill: C.grey, op: 0.35 });
        p.fn(f1, { c: C.blue }); p.fn(f2, { c: C.amber }); p.fn(fs, { c: C.red, w: 2.4 });
        ui.say(`Total ~ 𝒩(μ₁+μ₂, σ₁²+σ₂²) = 𝒩(<b class="r">${fmt(m, 1)}</b>, <b class="r">${fmt(s * s, 2)}</b>): the centres add and the <i>variances</i> add (σ = ${fmt(s, 2)}, not ${fmt(sa.v + sb.v, 1)}).` + (sims ? ` Simulated mean ${fmt(M.mean(sims), 2)}, variance ${fmt(M.variance(sims), 2)}.` : ''));
      } else {
        const l = a.v + b.v, pmf = k => M.pois(k, l);
        p.setY(0, Math.max(0.05, pmf(Math.floor(l)) * 1.25)); p.clear();
        if (sims) p.bars(M.hist(sims, -0.5, 49.5, 50), 0.8, { fill: C.grey, op: 0.4 });
        for (let k = 0; k <= 49; k++) p.dot(k, pmf(k), { r: 3, c: C.red });
        ui.say(`Poisson(${fmt(a.v, 1)}) + Poisson(${fmt(b.v, 1)}) = Poisson(<b class="r">${fmt(l, 1)}</b>) (red dots).` + (sims ? ` Simulated mean ${fmt(M.mean(sims), 2)}, variance ${fmt(M.variance(sims), 2)}: equal, as a Poisson must have.` : ''));
      }
      if (sims) sims.fam = fam.v;
    });
  });

  /* ===================== 11 · Covariance & LLSE ===================== */
  const ellipse = (m1, m2, s1, s2, r, k, n = 120) => { // points at Mahalanobis distance k
    const a = s1 * s1, b = r * s1 * s2, d = s2 * s2, tr = a + d, det = a * d - b * b, l1 = tr / 2 + Math.sqrt(tr * tr / 4 - det), l2 = tr / 2 - Math.sqrt(Math.max(0, tr * tr / 4 - det));
    const th = Math.abs(b) < 1e-12 ? (a >= d ? 0 : Math.PI / 2) : Math.atan2(l1 - a, b);
    return M.range(0, 2 * Math.PI, n).map(t => { const u = k * Math.sqrt(l1) * Math.cos(t), v = k * Math.sqrt(Math.max(l2, 0)) * Math.sin(t); return [m1 + u * Math.cos(th) - v * Math.sin(th), m2 + u * Math.sin(th) + v * Math.cos(th)]; });
  };
  add(31101, 'Every direction has a non-negative spread', 'The cloud of (wait, ride) mornings around their averages. Turn the direction v: the projected spread vᵀΣv is a variance, so it can never go below 0. That is Σ ⪰ 0.', ui => {
    const s1 = ui.slider('σ wait', 0.5, 6, 0.1, 3), s2 = ui.slider('σ ride', 0.5, 6, 0.1, 4.5), r = ui.slider('correlation ρ', -0.99, 0.99, 0.01, 0.7), th = ui.slider('direction angle', 0, 180, 1, 30, v => v + '°');
    let pts = [];
    const row = ui.row();
    const p = ui.plot({ x: [-15, 15], y: [-15, 15], w: 330, h: 330, into: row, xl: 'wait − avg', yl: 'ride − avg' });
    const q = ui.plot({ x: [0, 180], y: [0, 40], w: 400, h: 330, into: row, xl: 'angle of v (°)', yl: 'vᵀΣv' });
    ui.draw(() => {
      if (!pts.key || pts.key !== [s1.v, s2.v, r.v].join()) { pts = Array.from({ length: 500 }, () => M.rbiv(0, 0, s1.v, s2.v, r.v)); pts.key = [s1.v, s2.v, r.v].join(); }
      const t = th.v * Math.PI / 180, v = [Math.cos(t), Math.sin(t)], S = [[s1.v ** 2, r.v * s1.v * s2.v], [r.v * s1.v * s2.v, s2.v ** 2]];
      const q2 = a => { const u = [Math.cos(a), Math.sin(a)]; return u[0] * u[0] * S[0][0] + 2 * u[0] * u[1] * S[0][1] + u[1] * u[1] * S[1][1]; };
      p.clear(); pts.forEach(([x, y]) => p.dot(x, y, { r: 1.6, op: 0.3 }));
      p.path(ellipse(0, 0, s1.v, s2.v, r.v, 2), { c: C.blue, w: 1.5 }); p.seg(-15 * v[0], -15 * v[1], 15 * v[0], 15 * v[1], { c: C.red, w: 1.5 });
      pts.slice(0, 150).forEach(([x, y]) => { const d = x * v[0] + y * v[1]; p.dot(d * v[0], d * v[1], { r: 1.8, c: C.red, op: 0.5 }); });
      const mx = Math.max(...M.range(0, Math.PI, 90).map(q2)); q.setY(0, mx * 1.15); q.clear();
      q.fn(a => q2(a * Math.PI / 180), { w: 2 }); q.dot(th.v, q2(t), { c: C.red });
      const emp = M.variance(pts.map(([x, y]) => x * v[0] + y * v[1]));
      const tr = S[0][0] + S[1][1], det = S[0][0] * S[1][1] - S[0][1] ** 2, lmin = tr / 2 - Math.sqrt(tr * tr / 4 - det);
      ui.say(`Var(vᵀX) = vᵀΣv = <b class="r">${fmt(q2(t), 3)}</b> (from the cloud: ${fmt(emp, 3)}). Over all directions the smallest spread is the smallest eigenvalue, <b>${fmt(lmin, 3)}</b> ≥ 0. ` +
        'Push ρ towards ±1: the cloud flattens onto a line and the minimum touches 0 (Σ singular), but never goes negative.');
    });
  });

  add(31105, 'How much to believe the ETA', 'Phone ETA X and actual ride Y with correlation ρ. The best straight-line guess removes ρ² of the variance; the rest, σ_Y²(1 − ρ²), is the error. Pythagoras on the triangle.', ui => {
    const r = ui.slider('correlation ρ', -1, 1, 0.01, 0.9), sy = ui.slider('σ_Y (ride spread)', 1, 10, 0.1, 6);
    let pts = [];
    const row = ui.row();
    const p = ui.plot({ x: [10, 50], y: [5, 55], w: 380, h: 300, into: row, xl: 'ETA (min)', yl: 'ride (min)' });
    const q = ui.plot({ x: [0, 11], y: [0, 11], w: 300, h: 300, into: row, axes: false });
    ui.draw(() => {
      if (pts.key !== r.v + ',' + sy.v) { pts = Array.from({ length: 300 }, () => M.rbiv(30, 30, 5, sy.v, r.v)); pts.key = r.v + ',' + sy.v; }
      const b = r.v * sy.v / 5, line = x => 30 + b * (x - 30), mse = sy.v ** 2 * (1 - r.v ** 2), emp = M.mean(pts.map(([x, y]) => (y - line(x)) ** 2));
      p.clear(); pts.forEach(([x, y]) => p.dot(x, y, { r: 1.8, op: 0.4 })); p.fn(line, { c: C.red, w: 2.2 }); p.hline(30, { c: C.blue });
      q.clear(); const H = sy.v, L1 = Math.abs(r.v) * H, L2 = H * Math.sqrt(1 - r.v ** 2), k = 9.5 / H;
      q.poly([[1, 1], [1 + L1 * k, 1], [1 + L1 * k, 1 + L2 * k]], { fill: C.amber, op: 0.15, c: C.ink, w: 1.5 });
      q.seg(1, 1, 1 + L1 * k, 1, { c: C.green, w: 3 }); q.seg(1 + L1 * k, 1, 1 + L1 * k, 1 + L2 * k, { c: C.red, w: 3 }); q.seg(1, 1, 1 + L1 * k, 1 + L2 * k, { w: 3 });
      q.txt(1 + L1 * k / 2, 1, `|ρ|σ_Y = ${fmt(L1, 2)}`, { dy: 15, c: C.green }); q.txt(1 + L1 * k, 1 + L2 * k / 2, `σ_Y√(1−ρ²) = ${fmt(L2, 2)}`, { a: 'end', dx: -6, c: C.red, size: 11 }); q.txt(1 + L1 * k / 2, 1 + L2 * k / 2, `σ_Y = ${fmt(H, 1)}`, { dx: -14, dy: -8 });
      ui.say(`Best line: Ŷ = 30 + ρ(σ_Y/σ_X)(X − 30), slope ${fmt(b, 3)} (red). It explains ρ² = <b class="g">${pct(r.v ** 2)}</b> of the ride variance. ` +
        `MSE = σ_Y²(1 − ρ²) = <b class="r">${fmt(mse, 2)}</b> (on the dots: ${fmt(emp, 2)}). With ρ = 0 the line is flat at the average (blue): the ETA is useless.`);
    });
  });

  /* ===================== 12 · Conditional expectation ===================== */
  const RUSH = x => 25 + 15 * Math.exp(-(((x - 8.5) / 0.45) ** 2));
  add(31201, 'The average of similar mornings', 'X = departure time, Y = ride. Rush hour bends the relation. Slide x: the red dots are mornings that left around x, and their average is 𝔼[Y | X = x]. That curve beats every straight line.', ui => {
    const x0 = ui.slider('departure x', 7, 10, 0.05, 8.5, v => { const h = Math.floor(v), m = Math.round((v - h) * 60); return h + ':' + String(m).padStart(2, '0'); });
    const w = ui.slider('slice width', 0.05, 0.5, 0.01, 0.12);
    const pts = Array.from({ length: 700 }, () => { const x = 7 + 3 * Math.random(); return [x, RUSH(x) + 3.5 * M.rnorm()]; });
    const p = ui.plot({ x: [7, 10], y: [10, 55], h: 280, xl: 'departure time (h)', yl: 'ride (min)' });
    const xm = M.mean(pts.map(a => a[0])), ym = M.mean(pts.map(a => a[1])), sxy = M.mean(pts.map(([x, y]) => (x - xm) * (y - ym))), sxx = M.variance(pts.map(a => a[0]));
    const lin = x => ym + sxy / sxx * (x - xm);
    ui.draw(() => {
      p.clear(); p.rect(x0.v - w.v, 10, x0.v + w.v, 55, { fill: C.red, op: 0.07 });
      const sl = pts.filter(([x]) => Math.abs(x - x0.v) <= w.v);
      pts.forEach(([x, y]) => p.dot(x, y, { r: 1.8, c: Math.abs(x - x0.v) <= w.v ? C.red : '#777', op: 0.5 }));
      p.fn(RUSH, { c: C.ink, w: 2.4 }); p.fn(lin, { c: C.blue, w: 1.8, dash: '6 4' });
      const avg = sl.length ? M.mean(sl.map(a => a[1])) : NaN; if (sl.length) p.dot(x0.v, avg, { r: 6, c: C.red, stroke: '#fff' });
      const mseC = M.mean(pts.map(([x, y]) => (y - RUSH(x)) ** 2)), mseL = M.mean(pts.map(([x, y]) => (y - lin(x)) ** 2)), mse0 = M.variance(pts.map(a => a[1]));
      ui.say(`${sl.length} mornings in the slice, average ride <b class="r">${fmt(avg, 2)}</b> min; the curve 𝔼[Y | X] there is ${fmt(RUSH(x0.v), 2)}. ` +
        `Mean squared error: always guess the overall average ${fmt(mse0, 1)}, best straight line <span class="bl">${fmt(mseL, 1)}</span>, conditional mean <b>${fmt(mseC, 1)}</b> (only the noise is left).`);
    });
  });

  add(31203, 'Refine, then coarsen', 'Y = ride, X₁ = short/long ETA, X₂ = dry/rain. The finer forecast 𝔼[Y | X₁, X₂] averaged over the weather you do not know gives back 𝔼[Y | X₁].', ui => {
    const rs = ui.slider('ℙ(rain | short ETA)', 0, 1, 0.01, 0.2), rl = ui.slider('ℙ(rain | long ETA)', 0, 1, 0.01, 0.6), pl = ui.slider('ℙ(long ETA)', 0, 1, 0.01, 0.4);
    const mu = { sd: 22, sr: 28, ld: 32, lr: 41 };
    let est = null; ui.btn('Simulate 20000 mornings', () => {
      const acc = { s: [0, 0], l: [0, 0] };
      for (let i = 0; i < 20000; i++) { const L = Math.random() < pl.v, rain = Math.random() < (L ? rl.v : rs.v), y = mu[(L ? 'l' : 's') + (rain ? 'r' : 'd')] + 4 * M.rnorm(); const a = acc[L ? 'l' : 's']; a[0] += y; a[1]++; }
      est = { s: acc.s[0] / acc.s[1], l: acc.l[0] / acc.l[1] };
    });
    const p = ui.plot({ x: [0, 2], y: [0, 50], h: 260, xt: [], yl: 'expected ride (min)' });
    ui.draw(() => {
      p.clear(); const tower = { s: (1 - rs.v) * mu.sd + rs.v * mu.sr, l: (1 - rl.v) * mu.ld + rl.v * mu.lr };
      [['s', 'short ETA', rs.v], ['l', 'long ETA', rl.v]].forEach(([k, n, pr], i) => {
        const x = i + 0.5; p.rect(x - 0.35, 0, x - 0.05, mu[k + 'd'], { fill: C.blue, op: 0.35 }); p.rect(x + 0.05, 0, x + 0.35, mu[k + 'r'], { fill: C.ink, op: 0.35 });
        p.txt(x - 0.2, mu[k + 'd'], 'dry', { dy: -5, size: 11 }); p.txt(x + 0.2, mu[k + 'r'], 'rain', { dy: -5, size: 11 });
        p.seg(x - 0.42, tower[k], x + 0.42, tower[k], { c: C.red, w: 3 }); p.txt(x, 0, n, { dy: 14 });
        if (est) p.dot(x, est[k], { r: 6, fill: '#fff', stroke: C.red });
      });
      ui.say(`𝔼[Y | short] = (1 − ${fmt(rs.v, 2)})·22 + ${fmt(rs.v, 2)}·28 = <b class="r">${fmt(tower.s, 2)}</b>; 𝔼[Y | long] = <b class="r">${fmt(tower.l, 2)}</b> (red bars: the fine forecasts averaged over the weather, weighted by ℙ(X₂ | X₁)). ` +
        (est ? `Direct averages from the simulation: ${fmt(est.s, 2)} and ${fmt(est.l, 2)} (circles). ` : 'Simulate to check them against direct averages. ') + `Averaging once more over the ETA gives 𝔼[Y] = <b>${fmt((1 - pl.v) * tower.s + pl.v * tower.l, 2)}</b>.`);
      est = null;
    });
  });

  add(31204, 'Eve\'s law: signal plus noise', 'Rides in three kinds of weather. Separate the weather averages (signal) or widen the spread within each weather (noise): the total variance is always the sum of the two.', ui => {
    const sep = ui.slider('gap between weather averages', 0, 15, 0.5, 8), noise = ui.slider('spread within a weather σ', 0.5, 8, 0.1, 3);
    const p = ui.plot({ x: [0, 70], y: [0, 0.15], h: 220, xl: 'ride (min)' });
    const q = ui.plot({ x: [0, 1], y: [0, 1], h: 70, axes: false, pad: { l: 10, r: 10, t: 6, b: 6 } });
    ui.draw(() => {
      const w = [0.5, 0.3, 0.2], m = [30 - sep.v, 30, 30 + 1.5 * sep.v], s = noise.v, cols = [C.blue, C.ink, C.purple];
      const Em = M.sum(w.map((a, i) => a * m[i])), sig = M.sum(w.map((a, i) => a * (m[i] - Em) ** 2)), noi = s * s, tot = sig + noi;
      p.setY(0, 0.5 * M.npdf(0, 0, s) * 1.2); p.clear(); w.forEach((a, i) => p.fn(x => a * M.npdf(x, m[i], s), { c: cols[i], w: 1.4 })); p.fn(x => M.sum(w.map((a, i) => a * M.npdf(x, m[i], s))), { c: C.red, w: 2.2 });
      q.clear(); q.rect(0, 0.2, sig / tot, 0.8, { fill: C.green, op: 0.6 }); q.rect(sig / tot, 0.2, 1, 0.8, { fill: C.grey, op: 0.5 });
      if (sig / tot > 0.12) q.txt(sig / tot / 2, 0.5, 'signal Var(𝔼[Y|X])', { mid: true, size: 12 }); if (1 - sig / tot > 0.12) q.txt((1 + sig / tot) / 2, 0.5, 'noise 𝔼[Var(Y|X)]', { mid: true, size: 12 });
      ui.say(`Var(Y) = Var(𝔼[Y | weather]) + 𝔼[Var(Y | weather)] = <b class="g">${fmt(sig, 2)}</b> + <b>${fmt(noi, 2)}</b> = <b class="r">${fmt(tot, 2)}</b>. ` +
        `Knowing the weather removes the signal part; the noise part, ${fmt(noi, 2)}, is the smallest mean squared error any forecast from the weather can reach.`);
    });
  });

  /* ===================== 13 · Jointly Gaussian ===================== */
  const gauss = (s1, s2, r) => ({ S: [[s1 * s1, r * s1 * s2], [r * s1 * s2, s2 * s2]], maha(x, y) { const z = (x / s1) ** 2 - 2 * r * (x / s1) * (y / s2) + (y / s2) ** 2; return Math.sqrt(z / (1 - r * r)); } });
  add(31301, 'Distance measured in the cloud\'s own shape', 'Click anywhere to put a morning there. Euclidean distance ignores the oval; the Mahalanobis distance d counts how many “oval steps” out it is, and the density falls like e^(−d²/2).', ui => {
    const s1 = ui.slider('σ₁', 0.5, 5, 0.1, 3), s2 = ui.slider('σ₂', 0.5, 5, 0.1, 1.5), r = ui.slider('ρ', -0.95, 0.95, 0.01, 0.7);
    let pt = [3, 2.5];
    const p = ui.plot({ x: [-10, 10], y: [-7, 7], h: 300, xl: 'wait − avg', yl: 'ride − avg' });
    p.onclick((x, y) => { pt = [x, y]; ui.redraw(); });
    ui.draw(() => {
      const G = gauss(s1.v, s2.v, r.v);
      p.clear(); p.heat((x, y) => Math.exp(-0.5 * G.maha(x, y) ** 2), { nx: 50, ny: 35 });
      [1, 2, 3].forEach(k => p.path(ellipse(0, 0, s1.v, s2.v, r.v, k), { c: C.blue, w: 1.2, dash: k > 1 ? '4 3' : null }));
      const d = G.maha(pt[0], pt[1]), e = Math.hypot(pt[0], pt[1]);
      p.seg(0, 0, pt[0], pt[1], { c: C.red }); p.dot(pt[0], pt[1], { r: 5, c: C.red }); p.dot(0, 0, { r: 3 });
      const det = s1.v ** 2 * s2.v ** 2 * (1 - r.v ** 2), dens = Math.exp(-d * d / 2) / (2 * Math.PI * Math.sqrt(det));
      ui.say(`Euclidean distance ${fmt(e, 2)}, Mahalanobis distance d = √((x−μ)ᵀΣ⁻¹(x−μ)) = <b class="r">${fmt(d, 2)}</b>. Density f = e^(−d²/2)/(2π√det Σ) = <b>${fmt(dens, 4)}</b>. ` +
        'Click along the long axis of the oval and then across it at the same Euclidean distance: across counts as much further.');
    });
  });

  add(31302, 'Every mix of a Gaussian cloud is a bell', 'Weights t = (cos θ, sin θ) on (wait, ride). The histogram of tᵀX is always a bell with mean tᵀμ and variance tᵀΣt, for every direction.', ui => {
    const s1 = ui.slider('σ wait', 0.5, 5, 0.1, 2), s2 = ui.slider('σ ride', 0.5, 5, 0.1, 4), r = ui.slider('ρ', -0.95, 0.95, 0.01, 0.6), th = ui.slider('direction θ', 0, 180, 1, 45, v => v + '°');
    const pts = [];
    const row = ui.row();
    const p = ui.plot({ x: [-6, 22], y: [10, 46], w: 330, h: 300, into: row, xl: 'wait', yl: 'ride' });
    const q = ui.plot({ x: [-15, 50], y: [0, 0.2], w: 400, h: 300, into: row, xl: 'tᵀX' });
    ui.draw(() => {
      if (pts.key !== [s1.v, s2.v, r.v].join()) { pts.length = 0; for (let i = 0; i < 3000; i++) pts.push(M.rbiv(8, 28, s1.v, s2.v, r.v)); pts.key = [s1.v, s2.v, r.v].join(); }
      const t = th.v * Math.PI / 180, c = Math.cos(t), s = Math.sin(t), m = 8 * c + 28 * s, v = c * c * s1.v ** 2 + 2 * c * s * r.v * s1.v * s2.v + s * s * s2.v ** 2;
      p.clear(); pts.slice(0, 500).forEach(([x, y]) => p.dot(x, y, { r: 1.5, op: 0.3 })); p.arrow(8, 28, 8 + 10 * c, 28 + 10 * s, { c: C.red, w: 2 }); p.txt(8 + 11 * c, 28 + 11 * s, 't', { c: C.red, bold: true });
      const proj = pts.map(([x, y]) => c * x + s * y), sd = Math.sqrt(v);
      q.setX(m - 4.5 * sd, m + 4.5 * sd); q.setY(0, M.npdf(0, 0, sd) * 1.25); q.clear(); q.bars(M.hist(proj, m - 4.5 * sd, m + 4.5 * sd, 45), 9 * sd / 45, { fill: C.grey, op: 0.4 }); q.fn(x => M.npdf(x, m, sd), { c: C.red, w: 2.2 });
      ui.say(`tᵀX ~ 𝒩(tᵀμ, tᵀΣt) = 𝒩(<b class="r">${fmt(m, 2)}</b>, <b class="r">${fmt(v, 2)}</b>). From the 3000 simulated mornings: mean ${fmt(M.mean(proj), 2)}, variance ${fmt(M.variance(proj), 2)}. Turn θ: the bell moves and widens, but stays a bell.`);
    });
  });

  add(31303, 'No tilt, no link (for Gaussians only)', 'Look at the ride when the wait is short versus long. For a Gaussian cloud the two histograms differ exactly when ρ ≠ 0. The non-Gaussian example Y = X² − 1 has ρ = 0 yet is clearly dependent.', ui => {
    const mode = ui.select('cloud', [['g', 'jointly Gaussian with correlation ρ'], ['sq', 'not Gaussian: Y = X² − 1 (ρ = 0)']], 'g');
    const r = ui.slider('ρ (Gaussian)', -0.9, 0.9, 0.01, 0);
    const row = ui.row();
    const p = ui.plot({ x: [-3.5, 3.5], y: [-3.5, 6], w: 330, h: 300, into: row, xl: 'X', yl: 'Y' });
    const q = ui.plot({ x: [-4, 6], y: [0, 0.9], w: 400, h: 300, into: row, xl: 'Y within a slice' });
    ui.draw(() => {
      const pts = Array.from({ length: 4000 }, () => { if (mode.v === 'g') return M.rbiv(0, 0, 1, 1, r.v); const x = M.rnorm(); return [x, x * x - 1 + 0.15 * M.rnorm()]; });
      const lo = pts.filter(([x]) => x > -1.6 && x < -0.6).map(a => a[1]), hi = pts.filter(([x]) => Math.abs(x) < 0.5).map(a => a[1]);
      p.clear(); pts.slice(0, 700).forEach(([x, y]) => p.dot(x, y, { r: 1.5, op: 0.3 })); p.rect(-1.6, -3.5, -0.6, 6, { fill: C.red, op: 0.1 }); p.rect(-0.5, -3.5, 0.5, 6, { fill: C.blue, op: 0.1 });
      q.clear(); q.bars(M.hist(lo, -4, 6, 40), 0.25, { fill: C.red, op: 0.35 }); q.bars(M.hist(hi, -4, 6, 40), 0.25, { fill: C.blue, op: 0.35 });
      const cov = M.mean(pts.map(([x, y]) => x * y)) - M.mean(pts.map(a => a[0])) * M.mean(pts.map(a => a[1]));
      ui.say(`Sample covariance ${fmt(cov, 3)}. Rides in the <span class="r">red slice</span> average ${fmt(M.mean(lo), 2)}, in the <span class="bl">blue slice</span> ${fmt(M.mean(hi), 2)}. ` +
        (mode.v === 'g' ? (Math.abs(r.v) < 0.02 ? '<b class="g">ρ = 0: the slices look the same, independent.</b> For a jointly Gaussian pair, no correlation means no dependence at all.' : '<b class="r">ρ ≠ 0: the slices differ, dependent.</b>') : '<b class="r">Uncorrelated but dependent</b>: X fully decides Y, yet the parabola has no linear tilt. The theorem needs the pair to be jointly Gaussian.'));
    });
  });

  add(31304, 'Slicing the cloud gives a narrower bell', 'X₂ = phone reading, X₁ = actual ride. Fix the reading: the rides in that slice form a bell centred on the regression line, with the same width whatever the reading.', ui => {
    const r = ui.slider('ρ', -0.95, 0.95, 0.01, 0.8), x2 = ui.slider('phone reading x₂', 15, 45, 0.5, 34);
    const s1 = 6, s2 = 5, m1 = 30, m2 = 30;
    const pts = []; const row = ui.row();
    const p = ui.plot({ x: [12, 48], y: [8, 52], w: 330, h: 300, into: row, xl: 'reading x₂', yl: 'ride x₁' });
    const q = ui.plot({ x: [8, 52], y: [0, 0.2], w: 400, h: 300, into: row, xl: 'ride x₁' });
    ui.draw(() => {
      if (pts.key !== r.v) { pts.length = 0; for (let i = 0; i < 6000; i++) { const [a, b] = M.rbiv(m2, m1, s2, s1, r.v); pts.push([a, b]); } pts.key = r.v; }
      const m = m1 + r.v * s1 / s2 * (x2.v - m2), S = s1 * s1 * (1 - r.v * r.v), sl = pts.filter(([a]) => Math.abs(a - x2.v) < 0.6).map(a => a[1]);
      p.clear(); pts.slice(0, 700).forEach(([a, b]) => p.dot(a, b, { r: 1.5, op: 0.3 })); p.fn(a => m1 + r.v * s1 / s2 * (a - m2), { c: C.red, w: 2 }); p.vline(x2.v, { c: C.blue, dash: null, w: 2 });
      q.setY(0, M.npdf(0, 0, Math.sqrt(S)) * 1.2); q.clear(); q.bars(M.hist(sl, 8, 52, 44), 1, { fill: C.blue, op: 0.3 });
      q.fn(x => M.npdf(x, m1, s1), { c: C.grey, dash: '5 4' }); q.fn(x => M.npdf(x, m, Math.sqrt(S)), { c: C.red, w: 2.2 });
      ui.say(`Given x₂ = ${fmt(x2.v, 1)}: X₁ ~ 𝒩(m, S) with m = μ₁ + Σ₁₂Σ₂₂⁻¹(x₂ − μ₂) = <b class="r">${fmt(m, 2)}</b> and S = Σ₁₁ − Σ₁₂²/Σ₂₂ = <b class="r">${fmt(S, 2)}</b> (all rides: variance ${s1 * s1}). ` +
        `The slice holds ${sl.length} simulated mornings. m is a straight line in x₂, so the best guess (MMSE) is the linear one (LLSE), and S does not depend on x₂.`);
    });
  });

  /* ===================== 15 · Convergence ===================== */
  add(31501, 'Four ways of settling down', 'Each row is one run of days; a dot is drawn where Xₙ ≠ 0. Compare the sliding typewriter, the escaping spike, and the running average: which modes of convergence hold?', ui => {
    const ex = ui.select('sequence', [['tw', 'sliding typewriter: 1 on a sliding interval'], ['sp', 'escaping spike: n on [0, 1/n]'], ['avg', 'running average of fair coin − ½']], 'tw');
    const n = ui.slider('look at day n', 1, 200, 1, 60, v => v);
    let U = Array.from({ length: 30 }, () => Math.random()), C2 = Array.from({ length: 30 }, () => Array.from({ length: 200 }, () => Math.random() < 0.5 ? 1 : 0));
    ui.btn('New runs', () => { U = Array.from({ length: 30 }, () => Math.random()); C2 = Array.from({ length: 30 }, () => Array.from({ length: 200 }, () => Math.random() < 0.5 ? 1 : 0)); });
    const p = ui.plot({ x: [0, 200], y: [0, 31], h: 260, xl: 'day n', yt: [], yl: 'runs' });
    const tw = (k, u) => { let m = 0; while ((m + 1) * (m + 2) / 2 <= k - 1) m++; const len = m + 1, j = k - 1 - m * (m + 1) / 2; return u >= j / len && u < (j + 1) / len ? 1 : 0; };
    const X = (k, i) => ex.v === 'tw' ? tw(k, U[i]) : ex.v === 'sp' ? (U[i] < 1 / k ? k : 0) : (() => { let s = 0; for (let t = 0; t < k; t++) s += C2[i][t]; return s / k - 0.5; })();
    ui.draw(() => {
      p.clear(); for (let i = 0; i < 30; i++) for (let k = 1; k <= 200; k++) { const v = X(k, i); if (Math.abs(v) > (ex.v === 'avg' ? 0.1 : 0)) p.dot(k, i + 1, { r: 1.6, c: k === n.v ? C.red : C.ink, op: 0.65 }); }
      p.vline(n.v, { c: C.red });
      const N = n.v; let probNZ, mean;
      if (ex.v === 'tw') { let m = 0; while ((m + 1) * (m + 2) / 2 <= N - 1) m++; probNZ = 1 / (m + 1); mean = probNZ; }
      else if (ex.v === 'sp') { probNZ = 1 / N; mean = 1; } else { probNZ = 2 * (1 - M.Phi(0.1 * 2 * Math.sqrt(N))); mean = Math.sqrt(1 / (4 * N)) * Math.sqrt(2 / Math.PI); }
      const rows = ex.v === 'tw' ? ['in probability ✓ (ℙ(Xₙ ≠ 0) = interval length → 0)', 'in L¹ ✓ (𝔼|Xₙ| → 0)', 'almost surely ✗: every run is hit once per sweep, for ever', 'in law ✓']
        : ex.v === 'sp' ? ['in probability ✓ (ℙ(Xₙ ≠ 0) = 1/n)', 'in L¹ ✗: 𝔼|Xₙ| = n·(1/n) = 1 for every n', 'almost surely ✓: once n &gt; 1/U the run is 0 for ever', 'in law ✓']
          : ['in probability ✓', 'in L² ✓ (𝔼[(X̄ₙ − ½)²] = 1/(4n))', 'almost surely ✓ (strong law)', 'in law ✓'];
      ui.say(`Day ${N}: ${ex.v === 'avg' ? 'ℙ(|X̄ₙ − ½| &gt; 0.1)' : 'ℙ(Xₙ ≠ 0)'} ≈ <b class="r">${fmt(probNZ, 4)}</b>, 𝔼|Xₙ| ≈ <b>${fmt(mean, 4)}</b>.<br>` + rows.map(s => '• ' + s).join('<br>'));
    });
  });

  add(31502, 'Piling up at one number', 'Your average commute over n days. When its law piles up at the constant c = 30, that is the same as convergence in probability: the chance of being more than ε off goes to 0.', ui => {
    const n = ui.slider('days averaged n', 1, 400, 1, 10, v => v), eps = ui.slider('ε (minutes)', 0.2, 5, 0.1, 1);
    const p = ui.plot({ x: [20, 40], y: [0, 1], h: 240, xl: 'average commute (min)' });
    ui.draw(() => {
      const sd = 6 / Math.sqrt(n.v), f = x => M.npdf(x, 30, sd);
      p.setY(0, f(30) * 1.15); p.clear(); p.area(f, 20, 30 - eps.v, { op: 0.4 }); p.area(f, 30 + eps.v, 40, { op: 0.4 }); p.fn(f, { w: 2, n: 400 }); p.vline(30 - eps.v, { c: C.red }); p.vline(30 + eps.v, { c: C.red });
      const pr = 2 * (1 - M.Phi(eps.v / sd));
      ui.say(`ℙ(|X̄ₙ − 30| &gt; ${fmt(eps.v, 1)}) = <b class="r">${fmt(pr, 5)}</b> → 0 as n grows: X̄ₙ → 30 in law, and because the limit is a constant, also in probability. ` +
        'Convergence in law to a non-constant limit would not give this. Along the thinned days nₖ = k², the chances are summable, so Borel–Cantelli gives almost sure convergence on that subsequence.');
    });
  });

  /* ===================== 17 · Laws of large numbers ===================== */
  const DAY = () => M.rexp(1 / 30); // one commute: exponential, mean 30, sd 30
  add(31701, 'Weak law: the bell of the average narrows', '500 people each average n of their commutes. The histogram of those averages squeezes around 30; the chance of being more than ε off falls below the Chebyshev bound σ²/(nε²).', ui => {
    const n = ui.slider('days averaged n', 1, 300, 1, 10, v => v), eps = ui.slider('ε (minutes)', 1, 15, 0.5, 5);
    let avgs = [], key = 0;
    const p = ui.plot({ x: [0, 90], y: [0, 0.1], h: 250, xl: 'average commute (min)' });
    ui.draw(() => {
      if (key !== n.v) { avgs = Array.from({ length: 500 }, () => { let s = 0; for (let i = 0; i < n.v; i++) s += DAY(); return s / n.v; }); key = n.v; }
      const h = M.hist(avgs, 0, 90, 90), mx = Math.max(...h.map(a => a[1]));
      p.setY(0, mx * 1.15); p.clear(); p.rect(30 - eps.v, 0, 30 + eps.v, mx * 1.15, { fill: C.green, op: 0.08 }); p.bars(h, 1, { fill: C.blue, op: 0.45 }); p.vline(30, { c: C.red, dash: null });
      const out = avgs.filter(a => Math.abs(a - 30) >= eps.v).length / 500, cheb = 900 / (n.v * eps.v ** 2);
      ui.say(`ℙ(|X̄ₙ − 30| ≥ ${fmt(eps.v, 1)}) ≈ <b class="r">${fmt(out, 3)}</b> (share of the 500 averages outside the green band) ≤ Chebyshev σ²/(nε²) = ${fmt(Math.min(1, cheb), 3)}. ` +
        `Var(X̄ₙ) = σ²/n = ${fmt(900 / n.v, 2)}: one commute can be anything; the average of many cannot.`);
    });
  });

  add(31702, 'Strong law: your own running average settles', 'Five people keep a running average of their commutes. Each path wobbles, then enters the band 30 ± ε and stays there for good.', ui => {
    const eps = ui.slider('ε (minutes)', 0.5, 10, 0.5, 3);
    let paths = [];
    const grow = k => { paths.forEach(pp => { for (let i = 0; i < k; i++) { const d = DAY(); pp.s += d; pp.v.push(pp.s / (pp.v.length + 1)); } }); };
    const reset = () => { paths = Array.from({ length: 5 }, () => ({ s: 0, v: [] })); grow(50); };
    reset();
    ui.btn('Add 200 days', () => grow(200)); ui.btn('Start over', reset);
    const p = ui.plot({ x: [1, 50], y: [0, 70], h: 260, xl: 'day n', yl: 'running average' });
    ui.draw(() => {
      const N = paths[0].v.length; p.setX(1, N); p.clear(); p.rect(1, 30 - eps.v, N, 30 + eps.v, { fill: C.green, op: 0.12 });
      const cols = [C.red, C.blue, C.amber, C.purple, C.ink];
      const last = paths.map((pp, i) => { const step = Math.max(1, Math.floor(N / 400)); p.path(pp.v.map((v, k) => [k + 1, v]).filter((_, k) => k % step === 0), { c: cols[i], w: 1.4 }); let L = 0; pp.v.forEach((v, k) => { if (Math.abs(v - 30) > eps.v) L = k + 1; }); return L; });
      ui.say(`After ${N} days, the last day each path was outside 30 ± ${fmt(eps.v, 1)}: ${last.map(l => `<b>${l}</b>`).join(', ')}. ` +
        'The strong law says that, with probability 1, every path has such a last day (for every ε): the running average enters the band and never leaves. Shrink ε and add days to see it again.');
    });
  });

  add(31705, 'One day versus the rest of your life', '200 people\'s running averages. The weak law looks at a single day n: what share is off? The strong law looks at the whole future: what share is ever off again after day n?', ui => {
    const n = ui.slider('day n', 5, 395, 5, 50, v => v), eps = ui.slider('ε (minutes)', 1, 15, 0.5, 6);
    const H = 400, paths = Array.from({ length: 200 }, () => { let s = 0; return Array.from({ length: H }, (_, k) => (s += DAY()) / (k + 1)); });
    const p = ui.plot({ x: [1, H], y: [0, 80], h: 260, xl: 'day', yl: 'running average' });
    ui.draw(() => {
      p.clear(); p.rect(1, 30 - eps.v, H, 30 + eps.v, { fill: C.green, op: 0.12 }); p.vline(n.v, { c: C.red, dash: null });
      let snap = 0, ever = 0;
      paths.forEach((pp, i) => {
        const offNow = Math.abs(pp[n.v - 1] - 30) > eps.v, offLater = pp.slice(n.v - 1).some(v => Math.abs(v - 30) > eps.v);
        if (offNow) snap++; if (offLater) ever++;
        if (i < 25) p.path(pp.map((v, k) => [k + 1, v]).filter((_, k) => k % 3 === 0), { c: offLater ? C.red : C.grey, w: 1, op: 0.7 });
      });
      ui.say(`Weak law (snapshot): ℙ(|X̄ₙ − 30| &gt; ${fmt(eps.v, 1)}) on day ${n.v} ≈ <b>${fmt(snap / 200, 3)}</b>. ` +
        `Strong law (trajectory): ℙ(off on some day m ≥ ${n.v}, up to day ${H}) ≈ <b class="r">${fmt(ever / 200, 3)}</b> (red paths). ` +
        'The trajectory chance is always at least the snapshot one; the strong law says it too goes to 0.');
    });
  });

  /* ===================== 18 · CLT ===================== */
  add(31803, 'Whatever one day looks like, the total is a bell', 'Pick a lopsided one-day law. Add n days and standardise: (Sₙ − nμ)/(σ√n). The histogram of 4000 such totals approaches the standard bell.', ui => {
    const law = ui.select('one-day law', [['exp', 'Exponential (long late tail)'], ['uni', 'Uniform'], ['skew', 'usually 25, sometimes 60 (10%)']], 'skew');
    const n = ui.slider('days n', 1, 100, 1, 1, v => v);
    const L = { exp: [() => M.rexp(1 / 30), 30, 30], uni: [() => 20 + 20 * Math.random(), 30, 20 / Math.sqrt(12)], skew: [() => Math.random() < 0.1 ? 60 : 25, 28.5, Math.sqrt(0.09) * 35] };
    const p = ui.plot({ x: [-4, 4], y: [0, 0.6], h: 260, xl: 'standardised total Zₙ' });
    ui.draw(() => {
      const [draw, mu, sd] = L[law.v], N = n.v, z = Array.from({ length: 4000 }, () => { let s = 0; for (let i = 0; i < N; i++) s += draw(); return (s - N * mu) / (sd * Math.sqrt(N)); });
      const h = M.hist(z, -4, 4, 48), mx = Math.max(...h.map(a => a[1]));
      p.setY(0, Math.max(0.5, mx * 1.1)); p.clear(); p.bars(h, 8 / 48, { fill: C.blue, op: 0.45 }); p.fn(x => M.npdf(x), { c: C.red, w: 2.2 });
      const tail = z.filter(v => v > 1.645).length / 4000;
      ui.say(`n = ${N}: ℙ(Zₙ &gt; 1.645) ≈ <b class="r">${fmt(tail, 3)}</b>; the bell says 0.05. ` +
        'The characteristic function of Zₙ is (1 − t²/(2n) + o(1/n))ⁿ → e^(−t²/2): only the mean and the spread of one day survive the limit. The two-value law needs more days than the uniform one.');
    });
  });

  add(31804, 'How good is the bell for a month of late days?', 'S = number of late days in n days, each late with chance p: Binomial(n, p). Compare the exact staircase with the bell, read the bell at k + ½, and check the worst gap against Berry–Esseen.', ui => {
    const n = ui.slider('days n', 5, 200, 1, 30, v => v), pp = ui.slider('ℙ(late) p', 0.02, 0.98, 0.01, 0.15), k = ui.slider('at most k late days', 0, 60, 1, 6, v => v);
    const p = ui.plot({ x: [0, 30], y: [0, 1.05], h: 270, xl: 'k', yl: 'ℙ(S ≤ k)' });
    ui.draw(() => {
      const N = n.v, P = pp.v, mu = N * P, sd = Math.sqrt(N * P * (1 - P)), K = Math.min(k.v, N);
      const lo = Math.max(0, Math.floor(mu - 4.5 * sd)), hi = Math.min(N, Math.ceil(mu + 4.5 * sd) + 1);
      p.setX(lo - 0.5, hi + 0.5); p.clear();
      const cdf = []; let s = 0; for (let j = 0; j <= N; j++) { s += M.binom(N, j, P); cdf.push(s); }
      for (let j = lo; j <= hi; j++) p.seg(j, cdf[j], j + 1, cdf[j], { w: 2 });
      p.fn(x => M.Phi((x - mu) / sd), { c: C.blue, w: 1.8, dash: '6 4' });
      let gap = 0; for (let j = 0; j <= N; j++) gap = Math.max(gap, Math.abs(cdf[j] - M.Phi((j - mu) / sd)), Math.abs((j ? cdf[j - 1] : 0) - M.Phi((j - mu) / sd)));
      p.vline(K, { c: C.red }); p.dot(K, cdf[K], { c: C.red }); p.dot(K + 0.5, M.Phi((K + 0.5 - mu) / sd), { c: C.green, r: 5 });
      const rho = P * (1 - P) * (P * P + (1 - P) * (1 - P)), be = 0.4748 * rho / (Math.pow(P * (1 - P), 1.5) * Math.sqrt(N));
      ui.say(`Exact ℙ(S ≤ ${K}) = <b class="r">${fmt(cdf[K], 4)}</b>. Bell at k: Φ((k − np)/σ) = ${fmt(M.Phi((K - mu) / sd), 4)}; with the continuity correction at k + ½: <b class="g">${fmt(M.Phi((K + 0.5 - mu) / sd), 4)}</b>. ` +
        `Largest gap between the staircase and the bell: ${fmt(gap, 4)} ≤ Berry–Esseen 0.4748·𝔼|X−p|³/(σ³√n) = <b>${fmt(be, 4)}</b>. Rare late days (small p) are lopsided and need more days.`);
    });
  });

  /* ===================== 19–20 · Markov chains ===================== */
  const NAMES3 = ['O', 'L', 'C'], FULL3 = ['on time', 'late', 'cancelled'], COL3 = [C.green, C.red, C.grey];
  const POS3 = [[0.18, 0.3], [0.82, 0.3], [0.5, 0.82]];
  /* each row: sliders for the two off-diagonal moves, the stay chance is what is left */
  function rowSliders(ui, def) {
    return def.map((r, i) => [0, 1, 2].filter(j => j !== i).map(j => [j, ui.slider(`P(${NAMES3[i]}→${NAMES3[j]})`, 0, 1, 0.01, r[j])]));
  }
  function readP(rs) {
    return rs.map((pairs, i) => { const row = [0, 0, 0]; let s = 0; pairs.forEach(([j, sl]) => { row[j] = sl.v; s += sl.v; }); if (s > 1) row.forEach((v, j) => { row[j] = v / s; }); row[i] = Math.max(0, 1 - M.sum(row)); return row; });
  }
  function drawChain(p, P, pos, names, hi) {
    const n = P.length;
    for (let i = 0; i < n; i++) for (let j = 0; j < n; j++) { const v = P[i][j]; if (v < 0.005) continue; if (i === j) p.loop(pos[i][0], pos[i][1], { label: fmt(v, 2), w: 0.6 + 4 * v, down: pos[i][1] < 0.5, c: hi === i ? C.red : C.ink }); else p.link(pos[i][0], pos[i][1], pos[j][0], pos[j][1], { label: fmt(v, 2), w: 0.6 + 4 * v, bend: 0.18, r: 22, c: hi === i ? C.red : C.ink }); }
    pos.forEach(([x, y], i) => p.node(x, y, names[i], { c: hi === i ? C.red : C.ink }));
  }
  const stationary = P => { const n = P.length, A = P[0].map((_, j) => P.map((r, i) => r[j] - (i === j ? 1 : 0))); A[n - 1] = new Array(n).fill(1); const b = new Array(n).fill(0); b[n - 1] = 1; return M.solve(A, b); };
  const DEF3 = [[0.75, 0.2, 0.05], [0.5, 0.4, 0.1], [0.6, 0.3, 0.1]];

  add(31901, 'Tomorrow depends only on today', 'Three kinds of morning. Each row of the table is the odds for tomorrow given today, and must add to 1 (the stay chance is whatever is left). Run the chain to see a month of mornings.', ui => {
    const rs = rowSliders(ui, DEF3);
    let run = null; ui.btn('Run 40 days', () => { const P = readP(rs); let s = 0; run = [s]; for (let d = 1; d < 40; d++) { const u = Math.random(); s = u < P[s][0] ? 0 : u < P[s][0] + P[s][1] ? 1 : 2; run.push(s); } });
    const row = ui.row();
    const p = ui.plot({ x: [0, 1], y: [0, 1], w: 380, h: 300, axes: false, into: row });
    const t = ui.plot({ x: [0, 40], y: [0, 3], w: 380, h: 120, axes: false, into: row, pad: { l: 26, r: 6, t: 6, b: 6 } });
    ui.draw(() => {
      const P = readP(rs); p.clear(); drawChain(p, P, POS3, NAMES3);
      t.clear(); if (run) run.forEach((s, d) => t.rect(d, 3 - s - 0.9, d + 0.9, 3 - s - 0.1, { fill: COL3[s], op: 0.85 })); ['O', 'L', 'C'].forEach((n, i) => t.txt(-0.3, 2.5 - i, n, { a: 'end', mid: true, size: 11 }));
      ui.say('<table>' + P.map((r, i) => `<tr><th>${FULL3[i]} today →</th>${r.map(v => `<td>${fmt(v, 2)}</td>`).join('')}<td>row sum <b>${fmt(M.sum(r), 2)}</b></td></tr>`).join('') + '</table>' +
        'Columns: tomorrow on time, late, cancelled. Whatever happened last week does not enter: only today\'s row is used.' + (run ? ' Right: one simulated run.' : ''));
    });
  });

  add(31902, 'n days ahead is the n-th power', 'Pick today\'s state and how far ahead to look. Pⁿ\'s row gives the odds for day n; going through any middle day k and summing is exactly a matrix product.', ui => {
    const rs = rowSliders(ui, DEF3);
    const st = ui.select('today', [['0', 'on time'], ['1', 'late'], ['2', 'cancelled']], '1'), n = ui.slider('days ahead n', 1, 15, 1, 2, v => v);
    const p = ui.plot({ x: [0, 15], y: [0, 1], h: 230, xl: 'days ahead', yl: 'ℙ(state on day n)' });
    ui.draw(() => {
      const P = readP(rs), i = +st.v, rows = []; let R = [[1, 0, 0], [0, 1, 0], [0, 0, 1]];
      for (let d = 0; d <= 15; d++) { rows.push(R[i]); R = M.matmul(R, P); }
      p.clear(); [0, 1, 2].forEach(j => { p.path(rows.map((r, d) => [d, r[j]]), { c: COL3[j], w: 2 }); rows.forEach((r, d) => p.dot(d, r[j], { r: 2.5, c: COL3[j] })); }); p.vline(n.v, { c: C.ink });
      const Pn = M.matpow(P, n.v), m = Math.floor(n.v / 2), via = [0, 1, 2].map(k => M.matpow(P, m)[i][k] * M.matpow(P, n.v - m)[k][1]);
      ui.say(`Row ${FULL3[i]} of P<sup>${n.v}</sup>: on time <b>${fmt(Pn[i][0], 4)}</b>, late <b class="r">${fmt(Pn[i][1], 4)}</b>, cancelled <b>${fmt(Pn[i][2], 4)}</b>. ` +
        `Chapman–Kolmogorov for “late on day ${n.v}”, splitting at day ${m}: ∑ₖ P<sup>${m}</sup>(${NAMES3[i]},k)·P<sup>${n.v - m}</sup>(k,L) = ${via.map(v => fmt(v, 4)).join(' + ')} = <b class="r">${fmt(M.sum(via), 4)}</b>.`);
    });
  });

  /* strongly connected components by reachability */
  function classes(n, E) {
    const R = Array.from({ length: n }, (_, i) => { const seen = new Set([i]), st = [i]; while (st.length) { const u = st.pop(); E.forEach(([a, b]) => { if (a === u && !seen.has(b)) { seen.add(b); st.push(b); } }); } return seen; });
    const cls = [], done = new Set();
    for (let i = 0; i < n; i++) { if (done.has(i)) continue; const c = [...R[i]].filter(j => R[j].has(i)); c.forEach(j => done.add(j)); const closed = c.every(u => [...R[u]].every(v => c.includes(v))); cls.push({ c, closed }); }
    return cls;
  }
  add(31903, 'Which situations connect?', 'Four states of your route. Switch transitions on and off. States that can reach each other form a class; a class you can leave but never re-enter is open (transient), one you can never leave is closed.', ui => {
    const names = ['normal', 'delayed', 'diverted', 'scrapped'], pos = [[0.15, 0.7], [0.5, 0.85], [0.5, 0.25], [0.87, 0.5]];
    const all = [[0, 1, true], [1, 0, true], [1, 2, true], [2, 0, false], [2, 1, true], [2, 3, true], [3, 2, false], [0, 2, false]];
    const ch = all.map(([a, b, on]) => [a, b, ui.check(`${names[a]} → ${names[b]}`, on)]);
    const p = ui.plot({ x: [0, 1], y: [0, 1], h: 300, axes: false });
    ui.draw(() => {
      const E = ch.filter(c => c[2].v).map(c => [c[0], c[1]]), cls = classes(4, E), palette = [C.blue, C.amber, C.purple, C.green];
      const colOf = i => palette[cls.findIndex(k => k.c.includes(i))];
      p.clear(); E.forEach(([a, b]) => p.link(pos[a][0], pos[a][1], pos[b][0], pos[b][1], { bend: 0.15, r: 30 }));
      pos.forEach(([x, y], i) => p.node(x, y, names[i], { r: 30, size: 11, c: colOf(i), w: 3 }));
      ui.say(cls.map((k, i) => `<b style="color:${palette[i]}">{${k.c.map(j => names[j]).join(', ')}}</b> ${k.closed ? '— closed (recurrent once you are in it, for a finite chain)' : '— open: you can leave and never come back (transient)'}`).join('<br>') +
        '<br>Classes never overlap: together they split the states.');
    });
  });

  add(31904, 'Does the walk keep coming home?', 'A random walk on the integers: one step right with chance p, left with 1 − p. The chances of being home at time 2n sum to infinity only when p = ½: then home is recurrent.', ui => {
    const pr = ui.slider('p (step right)', 0.3, 0.7, 0.005, 0.5), N = ui.slider('look up to n', 10, 2000, 10, 400, v => v);
    const row = ui.row();
    const p = ui.plot({ x: [0, 400], y: [0, 0.6], w: 380, h: 240, into: row, xl: 'n', yl: 'P₀₀⁽²ⁿ⁾' });
    const q = ui.plot({ x: [0, 400], y: [0, 30], w: 380, h: 240, into: row, xl: 'n', yl: '∑ P₀₀⁽²ᵏ⁾' });
    ui.draw(() => {
      const P = pr.v, Q = 1 - P, n = N.v, term = k => Math.exp(M.lgamma(2 * k + 1) - 2 * M.lgamma(k + 1) + k * Math.log(P * Q));
      const ts = [], cs = []; let s = 0; for (let k = 1; k <= n; k++) { const t = term(k); s += t; ts.push([k, t]); cs.push([k, s]); }
      p.setX(0, n); p.clear(); p.path(ts, { c: C.blue, w: 2 }); q.setX(0, n); q.setY(0, Math.max(3, s * 1.15)); q.clear(); q.path(cs, { c: C.red, w: 2 });
      const f = 1 - Math.abs(P - Q), G = f < 1 ? f / (1 - f) : Infinity;
      ui.say(`P₀₀⁽²ⁿ⁾ = C(2n, n)(pq)ⁿ. Partial sum up to n = ${n}: <b class="r">${fmt(s, 3)}</b>. ` +
        (Math.abs(P - 0.5) < 1e-9 ? 'With p = ½ the terms fall only like 1/√(πn), so the sum grows without bound: <b>recurrent</b>, the walk returns with probability 1.' :
          `The terms fall geometrically (4pq = ${fmt(4 * P * Q, 4)} &lt; 1), so the sum converges to ∑ = f/(1 − f) = ${fmt(G, 3)}: <b class="r">transient</b>. Return probability f = 1 − |p − q| = <b>${fmt(f, 3)}</b>.`));
    });
  });

  add(31905, 'A fixed rhythm: the period', 'A cycle of shift days of length a, plus an optional shortcut that closes a second cycle of length b. You can be back at state 0 only at times built from a and b; their gcd is the period, shared by every state.', ui => {
    const a = ui.slider('main cycle length a', 2, 8, 1, 4, v => v), b = ui.slider('shortcut cycle length b', 2, 8, 1, 6, v => v), on = ui.check('shortcut on', false);
    const row = ui.row();
    const p = ui.plot({ x: [-1.3, 1.3], y: [-1.3, 1.3], w: 300, h: 300, axes: false, into: row });
    const q = ui.plot({ x: [0, 30], y: [0, 1], w: 420, h: 140, into: row, xl: 'n', yt: [], yl: 'can be home at n?' });
    ui.draw(() => {
      const A = a.v, B = Math.min(b.v, A), S = on.v && B < A + 1;
      const pos = Array.from({ length: A }, (_, i) => [Math.cos(Math.PI / 2 - 2 * Math.PI * i / A), Math.sin(Math.PI / 2 - 2 * Math.PI * i / A)]);
      const E = pos.map((_, i) => [i, (i + 1) % A]); if (on.v && b.v <= A && b.v < A) E.push([b.v - 1, 0]);
      p.clear(); E.forEach(([u, v]) => p.link(pos[u][0], pos[u][1], pos[v][0], pos[v][1], { bend: u === b.v - 1 && v === 0 && on.v && b.v < A ? -0.3 : 0.12, r: 18, c: u === b.v - 1 && v === 0 && on.v && b.v < A ? C.red : C.ink }));
      pos.forEach(([x, y], i) => p.node(x, y, String(i), { r: 18, c: i === 0 ? C.blue : C.ink }));
      let cur = new Set([0]); const ret = [];
      for (let n = 1; n <= 30; n++) { const nx = new Set(); cur.forEach(u => E.forEach(([s, t]) => { if (s === u) nx.add(t); })); cur = nx; if (cur.has(0)) ret.push(n); }
      q.clear(); for (let n = 1; n <= 30; n++) q.rect(n - 0.4, 0, n + 0.4, ret.includes(n) ? 0.9 : 0.06, { fill: ret.includes(n) ? C.blue : '#ccc', op: 0.7 });
      const d = ret.reduce((g, x) => M.gcd(g, x), 0);
      ui.say(`Return times to 0: ${ret.slice(0, 12).join(', ')}${ret.length > 12 ? ', …' : ''}. Period d = gcd = <b class="r">${d}</b>. ` +
        (on.v && b.v < A ? `Cycles of length ${A} and ${b.v} give period gcd(${A}, ${b.v}) = ${d}${d === 1 ? ': the rhythm is broken (aperiodic).' : '.'}` : `A single cycle of length ${A}: period ${A}. Switch the shortcut on (with b &lt; a) to add a second cycle of length b.`));
    });
  });

  const twoState = ui => [ui.slider('a = P(on time → late)', 0, 1, 0.01, 0.2), ui.slider('b = P(late → on time)', 0, 1, 0.01, 0.4)];
  add(32001, 'The steady mix of mornings', 'Start from any split of on-time and late mornings and press “next day”: the split moves towards π = (b/(a+b), a/(a+b)), and π itself does not move.', ui => {
    const [a, b] = twoState(ui), s0 = ui.slider('start: share on time', 0, 1, 0.01, 0.1);
    let hist = null; const reset = () => { hist = [s0.v]; };
    ui.btn('Next day', () => { if (!hist) reset(); const x = hist[hist.length - 1]; hist.push(x * (1 - a.v) + (1 - x) * b.v); });
    ui.btn('Start again', reset);
    const p = ui.plot({ x: [-0.6, 12], y: [0, 1], h: 240, xl: 'day', yl: 'share on time' });
    ui.draw(() => {
      if (!hist || hist[0] !== s0.v) reset();
      const pi = a.v + b.v ? b.v / (a.v + b.v) : 0.5; p.setX(-0.6, Math.max(12, hist.length)); p.clear(); p.hline(pi, { c: C.red });
      hist.forEach((v, d) => { p.rect(d - 0.35, 0, d + 0.35, v, { fill: C.green, op: 0.5 }); p.rect(d - 0.35, v, d + 0.35, 1, { fill: C.red, op: 0.25 }); });
      const x = hist[hist.length - 1];
      ui.say(`π = (b/(a+b), a/(a+b)) = (<b class="g">${fmt(pi, 3)}</b>, <b class="r">${fmt(1 - pi, 3)}</b>). Check πP = π: ${fmt(pi, 3)}·${fmt(1 - a.v, 2)} + ${fmt(1 - pi, 3)}·${fmt(b.v, 2)} = <b>${fmt(pi * (1 - a.v) + (1 - pi) * b.v, 3)}</b>. ` +
        `Today the split is ${fmt(x, 3)} on time; each day closes the gap by the factor |1 − a − b| = ${fmt(Math.abs(1 - a.v - b.v), 2)}.`);
    });
  });

  add(32002, 'The first day is forgotten', 'Chance of an on-time morning on day n, starting on time (solid) or late (dashed). Both curves meet at π_O. Simulate a long run: the average gap between on-time days is 1/π_O.', ui => {
    const [a, b] = twoState(ui);
    let gap = null; ui.btn('Simulate 20000 days', () => { let s = 0, last = 0, gaps = []; for (let d = 1; d <= 20000; d++) { s = s === 0 ? (Math.random() < a.v ? 1 : 0) : (Math.random() < b.v ? 0 : 1); if (s === 0) { gaps.push(d - last); last = d; } } gap = M.mean(gaps); });
    const p = ui.plot({ x: [0, 20], y: [0, 1], h: 250, xl: 'day n', yl: 'ℙ(on time on day n)' });
    ui.draw(() => {
      const pi = b.v / (a.v + b.v || 1), lam = 1 - a.v - b.v, fO = n => pi + (1 - pi) * Math.pow(lam, n), fL = n => pi - pi * Math.pow(lam, n);
      p.clear(); p.hline(pi, { c: C.red }); const ns = M.range(0, 20, 21); p.path(ns.map(n => [n, fO(n)]), { c: C.green, w: 2 }); p.path(ns.map(n => [n, fL(n)]), { c: C.ink, w: 2, dash: '6 4' });
      ns.forEach(n => { p.dot(n, fO(n), { r: 2.5, c: C.green }); p.dot(n, fL(n), { r: 2.5 }); });
      ui.say(`Both converge to π_O = <b class="r">${fmt(pi, 3)}</b> at the rate |1 − a − b|ⁿ = ${fmt(Math.abs(lam), 2)}ⁿ. Mean return time to “on time”: μ_O = 1/π_O = <b>${fmt(1 / pi, 3)}</b> days.` +
        (gap ? ` Simulated average gap between on-time days: <b class="g">${fmt(gap, 3)}</b>.` : '') + (Math.abs(lam) > 0.999 ? ' (With a = b = 1 the chain is periodic and never settles.)' : ''));
      gap = null;
    });
  });

  add(32004, 'Balance the traffic across a cut', 'In the steady state, draw a line between some states. The flow of probability across it one way equals the flow the other way. For a two-state cut this is detailed balance.', ui => {
    const rs = rowSliders(ui, DEF3);
    const cut = ui.select('cut', [['0', '{on time} | {late, cancelled}'], ['1', '{late} | {on time, cancelled}'], ['2', '{cancelled} | {on time, late}']], '0');
    const p = ui.plot({ x: [0, 1], y: [0, 1], h: 300, axes: false });
    ui.draw(() => {
      const P = readP(rs), pi = stationary(P), i = +cut.v, others = [0, 1, 2].filter(j => j !== i);
      p.clear(); drawChain(p, P, POS3, NAMES3, i);
      const out = others.reduce((s, j) => s + pi[i] * P[i][j], 0), inn = others.reduce((s, j) => s + pi[j] * P[j][i], 0);
      const pairs = [[0, 1], [0, 2], [1, 2]].map(([u, v]) => `${NAMES3[u]}↔${NAMES3[v]}: ${fmt(pi[u] * P[u][v], 4)} vs ${fmt(pi[v] * P[v][u], 4)}`);
      ui.say(`π = (${pi.map(v => fmt(v, 3)).join(', ')}). Across the cut around <b class="r">${FULL3[i]}</b>: out-flow ∑ π_${NAMES3[i]}P = <b>${fmt(out, 4)}</b>, in-flow ∑ π_jP_j${NAMES3[i]} = <b>${fmt(inn, 4)}</b>: equal for every cut. ` +
        `Pairwise flows (detailed balance holds only if each pair matches): ${pairs.join('; ')}.`);
    });
  });

  add(32005, 'Alternating days still have a share', 'With a = b = 1 the days strictly alternate. The chance of an on-time day jumps between 0 and 1 for ever, but the running share of on-time days settles at π.', ui => {
    const a = ui.slider('a = P(on time → late)', 0, 1, 0.01, 1), b = ui.slider('b = P(late → on time)', 0, 1, 0.01, 1);
    const p = ui.plot({ x: [0, 30], y: [0, 1.05], h: 260, xl: 'day n', yl: 'chance / share on time' });
    ui.draw(() => {
      const pi = b.v / (a.v + b.v || 1), lam = 1 - a.v - b.v, f = n => pi + (1 - pi) * Math.pow(lam, n);
      const pts = M.range(0, 30, 31).map(n => [n, f(n)]); let s = 0; const ces = pts.map(([n, v]) => [n, (s += v) / (n + 1)]);
      p.clear(); p.hline(pi, { c: C.red }); p.path(pts, { c: C.ink, w: 1.4 }); pts.forEach(([n, v]) => p.dot(n, v, { r: 3 })); p.path(ces, { c: C.blue, w: 2.4 });
      ui.say(`Black: ℙ(on time on day n) starting on time = π + (1 − π)(1 − a − b)ⁿ. Blue: the average of those over days 0…n (Cesàro). ` +
        (Math.abs(lam + 1) < 1e-9 ? '<b class="r">Period 2</b>: the black dots never settle, but the blue average → π = ½.' : `Here |1 − a − b| = ${fmt(Math.abs(lam), 2)} &lt; 1, so both settle at π = ${fmt(pi, 3)}. Set a = b = 1 to see the periodic case.`));
    });
  });

  /* ===================== 21 · Absorption ===================== */
  function lineChain(ui, mode) {
    const N = ui.slider('stops between (0 = give up, N = campus)', 3, 12, 1, 6, v => v), p = ui.slider('ℙ(move one stop towards campus)', 0.05, 0.95, 0.01, 0.5);
    let sims = null; ui.btn('Simulate 2000 trips from every stop', () => {
      sims = [];
      for (let i = 0; i <= N.v; i++) { let hit = 0, steps = 0; for (let t = 0; t < 2000; t++) { let x = i, s = 0; while (x !== N.v && (mode === 'time' || x !== 0) && s < 1e5) { if (mode === 'time' && x === 0) x = 1; else x += Math.random() < p.v ? 1 : -1; s++; } if (x === N.v) hit++; steps += s; } sims.push(mode === 'time' ? steps / 2000 : hit / 2000); }
    });
    const pl = ui.plot({ x: [-0.5, 12.5], y: [0, 1.05], h: 250, xl: 'stop i', yl: mode === 'time' ? 'expected steps to campus' : 'ℙ(campus before giving up)' });
    ui.draw(() => {
      const n = N.v, P = p.v, Q = 1 - P;
      const A = [], b = [];
      for (let i = 0; i <= n; i++) {
        const row = new Array(n + 1).fill(0); row[i] = 1;
        if (i === n) b.push(mode === 'time' ? 0 : 1);
        else if (i === 0) { if (mode === 'time') { row[1] -= 1; b.push(1); } else b.push(0); }
        else { row[i + 1] -= P; row[i - 1] -= Q; b.push(mode === 'time' ? 1 : 0); }
        A.push(row);
      }
      const v = M.solve(A, b), mx = Math.max(...v, ...(sims || [0]));
      pl.setX(-0.5, n + 0.5); pl.setY(0, mode === 'time' ? mx * 1.15 : 1.05); pl.clear();
      v.forEach((x, i) => { pl.rect(i - 0.3, 0, i + 0.3, x, { fill: i === n ? C.green : i === 0 && mode !== 'time' ? C.grey : C.blue, op: 0.5 }); pl.txt(i, x, fmt(x, mode === 'time' ? 1 : 2), { dy: -5, size: 10.5 }); });
      if (sims && sims.length === n + 1) sims.forEach((x, i) => pl.dot(i, x, { r: 4.5, fill: '#fff', stroke: C.red }));
      const k = Math.min(2, n - 1);
      ui.say(mode === 'time'
        ? `μᵢ = 1 + p·μᵢ₊₁ + (1 − p)·μᵢ₋₁ for 0 &lt; i &lt; N, with μ_N = 0 and stop 0 bouncing back (μ₀ = 1 + μ₁). From stop ${k}: 1 + ${fmt(P, 2)}·${fmt(v[k + 1], 2)} + ${fmt(Q, 2)}·${fmt(v[k - 1], 2)} = <b class="r">${fmt(v[k], 2)}</b> steps.` + (sims ? ' Circles: simulated averages.' : '')
        : `aᵢ = p·aᵢ₊₁ + (1 − p)·aᵢ₋₁ with a₀ = 0, a_N = 1. From stop ${k}: ${fmt(P, 2)}·${fmt(v[k + 1], 3)} + ${fmt(Q, 2)}·${fmt(v[k - 1], 3)} = <b class="r">${fmt(v[k], 3)}</b>. ` +
          (Math.abs(P - 0.5) < 1e-9 ? 'Fair steps: aᵢ = i/N, a straight line.' : `Gambler's ruin: aᵢ = (1 − r^i)/(1 − r^N) with r = q/p = ${fmt(Q / P, 3)}.`) + (sims ? ' Circles: simulated shares.' : ''));
      sims = null;
    });
  }
  add(32101, 'Look one stop ahead', 'A line of stops: 0 = give up and go home, N = campus. Each stop\'s chance of reaching campus first is the average of its neighbours\' chances. Bars: the solution; circles: simulation.', ui => lineChain(ui, 'abs'));
  add(32102, 'Counting steps to campus', 'Same line, but now you never give up (stop 0 bounces you back). The expected number of steps from a stop is 1 plus the average over where you land.', ui => lineChain(ui, 'time'));

  /* ===================== 23 · Random processes ===================== */
  add(32301, 'Does the delay signal look the same at 8 and at 9?', 'Five runs of a delay signal X(t), with the ensemble mean (red) and the correlation of readings τ apart, measured at two different start times. WSS: constant mean and a correlation that depends only on τ.', ui => {
    const kind = ui.select('signal', [['ph', 'A·cos(ωt + Θ), random phase Θ'], ['fix', 'A·cos(ωt), fixed phase'], ['ar', 'smoothed noise (AR(1))'], ['tr', 'rush-hour trend + noise']], 'ph');
    const tau = ui.slider('lag τ', 0, 40, 1, 10, v => v);
    const T = 200, gen = k => {
      if (k === 'ph' || k === 'fix') { const A = 1 + 0.3 * M.rnorm(), th = k === 'ph' ? 2 * Math.PI * Math.random() : 0; return Array.from({ length: T }, (_, t) => A * Math.cos(2 * Math.PI * t / 50 + th)); }
      if (k === 'ar') { let x = M.rnorm(); return Array.from({ length: T }, () => (x = 0.9 * x + Math.sqrt(1 - 0.81) * M.rnorm())); }
      return Array.from({ length: T }, (_, t) => 1.5 * Math.exp(-(((t - 100) / 35) ** 2)) + 0.4 * M.rnorm());
    };
    let ens = [], key = '';
    const p = ui.plot({ x: [0, T], y: [-2.5, 2.5], h: 250, xl: 't (minutes)', yl: 'delay' });
    ui.draw(() => {
      if (key !== kind.v) { ens = Array.from({ length: 600 }, () => gen(kind.v)); key = kind.v; }
      const mean = Array.from({ length: T }, (_, t) => M.mean(ens.map(e => e[t])));
      const R = t0 => M.mean(ens.map(e => e[t0] * e[t0 + tau.v]));
      p.clear(); ens.slice(0, 5).forEach((e, i) => p.path(e.map((v, t) => [t, v]), { c: [C.blue, C.amber, C.purple, C.green, C.ink][i], w: 1, op: 0.75 })); p.path(mean.map((v, t) => [t, v]), { c: C.red, w: 2.6 });
      p.vline(20, { c: C.ink }); p.vline(20 + tau.v, { c: C.ink, dash: '2 3' }); p.vline(100, { c: C.ink }); p.vline(100 + tau.v, { c: C.ink, dash: '2 3' });
      const r1 = R(20), r2 = R(100), mVar = Math.max(...mean) - Math.min(...mean);
      const ok = mVar < 0.25 && Math.abs(r1 - r2) < 0.12;
      ui.say(`Ensemble mean ranges over ${fmt(mVar, 2)} (red curve). 𝔼[X(20)X(${20 + tau.v})] = <b>${fmt(r1, 3)}</b>, 𝔼[X(100)X(${100 + tau.v})] = <b>${fmt(r2, 3)}</b>. ` +
        (ok ? '<b class="g">Same mean, same correlation at the same lag: wide-sense stationary.</b>' + (kind.v === 'ph' ? ' The random phase is what makes it so.' : '') : '<b class="r">Not stationary:</b> ' + (kind.v === 'fix' ? 'without the random phase every run peaks at the same times, so the mean follows the cosine.' : 'the rush hour changes the mean with t.')));
    });
  });

  add(32302, 'Not every curve is an autocorrelation', 'A valid R(τ) is largest at τ = 0, symmetric, and has a spectrum S(f) that is never negative (Wiener–Khinchin). Try the candidates and the width.', ui => {
    const c = ui.select('candidate R(τ)', [['e', 'e^(−|τ|/w)'], ['g', 'e^(−τ²/w²)'], ['tri', 'triangle max(0, 1 − |τ|/w)'], ['box', 'box: 1 if |τ| < w'], ['cos', 'cos(τ/w)'], ['bump', '(τ/w)² e^(−|τ|/w)']], 'e');
    const w = ui.slider('width w', 0.5, 4, 0.1, 1.5);
    const row = ui.row();
    const p = ui.plot({ x: [-10, 10], y: [-0.6, 1.2], w: 370, h: 240, into: row, xl: 'τ', yl: 'R(τ)' });
    const q = ui.plot({ x: [0, 2], y: [-1, 3], w: 370, h: 240, into: row, xl: 'frequency f', yl: 'S(f)' });
    ui.draw(() => {
      const W = w.v, R = { e: t => Math.exp(-Math.abs(t) / W), g: t => Math.exp(-((t / W) ** 2)), tri: t => Math.max(0, 1 - Math.abs(t) / W), box: t => Math.abs(t) < W ? 1 : 0, cos: t => Math.cos(t / W), bump: t => (t / W) ** 2 * Math.exp(-Math.abs(t) / W) }[c.v];
      p.clear(); p.fn(R, { w: 2, n: 600 }); p.hline(0, { c: '#bbb', dash: null });
      const S = f => 2 * M.integrate(t => R(t) * Math.cos(2 * Math.PI * f * t), 0, 40, 4000);
      const fs = M.range(0, 2, 80), Sv = fs.map(S), lo = Math.min(...Sv), hi = Math.max(...Sv);
      q.setY(Math.min(-0.2, lo * 1.2), Math.max(0.5, hi * 1.15)); q.clear(); q.hline(0, { c: '#999', dash: null });
      q.path(fs.map((f, i) => [f, Sv[i]]), { c: C.blue, w: 2 }); fs.forEach((f, i) => { if (Sv[i] < -1e-3) q.dot(f, Sv[i], { r: 2.5, c: C.red }); });
      const max0 = M.range(-10, 10, 401).every(t => R(t) <= R(0) + 1e-9), neg = lo < -1e-3;
      ui.say(`R(0) is the largest value: <b class="${max0 ? 'g' : 'r'}">${max0 ? 'yes' : 'no'}</b>. Spectrum never negative: <b class="${neg ? 'r' : 'g'}">${neg ? 'no (red dots)' : 'yes'}</b>. ` +
        (c.v === 'cos' ? 'cos is valid (its spectrum is two spikes at f = ±1/(2πw), off this smooth plot).' : !max0 || neg ? '<b class="r">Not a valid autocorrelation:</b> some weighted mix of readings would get a negative variance.' : '<b class="g">Valid.</b>'));
    });
  });

  /* ===================== 24 · Poisson process ===================== */
  add(32401, 'Random buses from tiny time slices', 'Cut the window into slices of length h. In each slice a bus comes with chance λh. As h shrinks, the count in the window becomes Poisson(λt).', ui => {
    const lam = ui.slider('λ (buses per hour)', 1, 12, 0.5, 6), t = ui.slider('window t (hours)', 0.1, 2, 0.05, 0.5), h = ui.slider('slice h (minutes)', 0.1, 15, 0.1, 5);
    let counts = null;
    ui.btn('Simulate 3000 windows', () => { const n = Math.max(1, Math.round(t.v * 60 / h.v)), pr = Math.min(1, lam.v * h.v / 60); counts = Array.from({ length: 3000 }, () => { let k = 0; for (let i = 0; i < n; i++) if (Math.random() < pr) k++; return k; }); });
    const row = ui.row();
    const tl = ui.plot({ x: [0, 60], y: [0, 1], h: 70, w: 760, into: row, axes: false, pad: { l: 10, r: 10, t: 4, b: 4 } });
    const p = ui.plot({ x: [-0.5, 20.5], y: [0, 0.5], h: 230, xl: 'buses in the window' });
    ui.draw(() => {
      const L = lam.v * t.v, n = Math.max(1, Math.round(t.v * 60 / h.v)), pr = Math.min(1, lam.v * h.v / 60);
      tl.setX(0, t.v * 60); tl.clear(); for (let i = 0; i < n; i++) { const hit = Math.random() < pr; tl.rect(i * h.v, 0.2, (i + 1) * h.v, 0.8, { fill: hit ? C.red : '#eee', op: hit ? 0.8 : 1, c: '#fff', w: 0.5 }); }
      const mx = Math.max(M.pois(Math.floor(L), L), M.binom(n, Math.round(n * pr), pr)); p.setX(-0.5, Math.max(10, Math.ceil(L + 4 * Math.sqrt(L))) + 0.5); p.setY(0, mx * 1.25); p.clear();
      if (counts) p.bars(M.hist(counts, -0.5, 40.5, 41), 0.7, { fill: C.grey, op: 0.4 });
      for (let k = 0; k <= 40; k++) { p.dot(k, M.binom(n, k, pr), { r: 3.5, fill: '#fff', stroke: C.blue }); p.dot(k, M.pois(k, L), { r: 2.5, c: C.red }); }
      ui.say(`Top: one window cut into ${n} slices of ${fmt(h.v, 1)} min, a bus in each with chance λh = ${fmt(pr, 4)} (red slices). The count is Binomial(${n}, ${fmt(pr, 3)}) (<span class="bl">circles</span>), which approaches Poisson(λt = ${fmt(L, 2)}) (<span class="r">dots</span>) as h → 0. ` +
        `The Poisson limit has mean and variance both ${fmt(L, 2)}; with these slices the count's variance is n·λh(1 − λh) = ${fmt(n * pr * (1 - pr), 2)}, closer to ${fmt(L, 2)} the thinner the slices.` + (counts ? ` Simulated: mean ${fmt(M.mean(counts), 2)}, variance ${fmt(M.variance(counts), 2)}.` : ''));
      counts = null;
    });
  });

  add(32402, 'Gaps are exponential; the n-th bus is their sum', 'One random timetable with rate λ. The gaps between buses are exponential with mean 1/λ; the wait for the n-th bus is a sum of n gaps, a Gamma(n, λ) time.', ui => {
    const lam = ui.slider('λ (buses per hour)', 1, 12, 0.5, 6), n = ui.slider('wait for bus number n', 1, 8, 1, 3, v => v);
    let tt = [], sims = [];
    const fresh = () => { tt = []; let s = 0; while (s < 120) { s += 60 * M.rexp(lam.v); tt.push(s); } sims = Array.from({ length: 4000 }, () => { let s = 0; for (let i = 0; i < n.v; i++) s += 60 * M.rexp(lam.v); return s; }); sims.key = [lam.v, n.v].join(); };
    ui.btn('New timetable', fresh);
    const tl = ui.plot({ x: [0, 120], y: [0, 1], h: 80, xl: 'minutes', yt: [] });
    const p = ui.plot({ x: [0, 120], y: [0, 0.1], h: 220, xl: 'minutes until bus n', yl: 'density' });
    ui.draw(() => {
      if (sims.key !== [lam.v, n.v].join()) fresh();
      tl.clear(); tl.seg(0, 0.4, 120, 0.4, { c: '#ccc' }); tt.forEach((t, i) => { if (t <= 120) { tl.dot(t, 0.4, { r: 4.5, c: i === n.v - 1 ? C.red : C.ink }); } });
      if (tt[n.v - 1] <= 120) tl.seg(0, 0.75, tt[n.v - 1], 0.75, { c: C.red, w: 3 });
      const r = lam.v / 60, f = x => M.gammaPdf(x, n.v, r), mode = (n.v - 1) / r, top = n.v === 1 ? r : f(mode);
      p.setY(0, top * 1.25); p.clear(); p.bars(M.hist(sims, 0, 120, 60), 2, { fill: C.grey, op: 0.4 }); p.fn(f, { c: C.red, w: 2.2, from: 0.01 });
      const pr = 1 - Array.from({ length: n.v }, (_, k) => M.pois(k, r * 60)).reduce((a, b) => a + b, 0);
      ui.say(`Gap mean 1/λ = <b>${fmt(60 / lam.v, 1)}</b> min. Bus ${n.v} arrives after S<sub>${n.v}</sub> ~ Gamma(${n.v}, λ), mean <b class="r">${fmt(60 * n.v / lam.v, 1)}</b> min (simulated ${fmt(M.mean(sims), 1)}). ` +
        `“At least ${n.v} buses within an hour” is the same event as “S<sub>${n.v}</sub> ≤ 60”: ℙ = ${fmt(pr, 4)} by the Poisson count, ${fmt(sims.filter(s => s <= 60).length / sims.length, 4)} by simulation.`);
    });
  });

  add(32403, 'Given n buses came, they fell like uniform darts', 'Keep only the hours in which exactly n buses arrived. Their arrival times are n uniform points in the hour, sorted; the k-th sits on average k/(n + 1) of the way through.', ui => {
    const n = ui.slider('buses in the hour n', 1, 8, 1, 3, v => v), k = ui.slider('look at the k-th', 1, 8, 1, 2, v => v);
    let hours = [];
    const sim = () => { hours = []; let tries = 0; while (hours.length < 1500 && tries < 200000) { tries++; const ts = []; let s = 60 * M.rexp(n.v); while (s < 60) { ts.push(s); s += 60 * M.rexp(n.v); } if (ts.length === n.v) hours.push(ts); } hours.key = n.v; };
    ui.btn('Resample', sim);
    const tl = ui.plot({ x: [0, 60], y: [0, 6], h: 130, axes: false, pad: { l: 20, r: 20, t: 4, b: 4 } });
    const p = ui.plot({ x: [0, 60], y: [0, 0.1], h: 220, xl: 'minute of the k-th bus', yl: 'density' });
    ui.draw(() => {
      if (hours.key !== n.v) sim(); const K = Math.min(k.v, n.v);
      tl.clear(); hours.slice(0, 5).forEach((h, i) => { const y = 5.3 - i; tl.seg(0, y, 60, y, { c: '#ddd' }); h.forEach((t, j) => tl.dot(t, y, { r: 4, c: j === K - 1 ? C.red : C.ink })); });
      const kth = hours.map(h => h[K - 1]);
      const beta = x => { const u = x / 60; return Math.exp(M.lgamma(n.v + 1) - M.lgamma(K) - M.lgamma(n.v - K + 1) + (K - 1) * Math.log(u) + (n.v - K) * Math.log(1 - u)) / 60; };
      const top = Math.max(...M.range(0.5, 59.5, 120).map(beta)); p.setY(0, top * 1.25); p.clear(); p.bars(M.hist(kth, 0, 60, 30), 2, { fill: C.grey, op: 0.4 }); p.fn(beta, { c: C.red, w: 2.2, from: 0.05, to: 59.95 });
      ui.say(`${hours.length} simulated hours with exactly ${n.v} buses (top: five of them). The ${K}${['st', 'nd', 'rd'][K - 1] || 'th'} bus averages minute <b class="r">${fmt(M.mean(kth), 1)}</b>; theory 60·k/(n+1) = <b>${fmt(60 * K / (n.v + 1), 1)}</b>. ` +
        `Its law is the k-th of ${n.v} sorted uniforms, a Beta(${K}, ${n.v - K + 1}) stretched over the hour (red). The rate λ has dropped out.`);
    });
  });

  add(32404, 'Splitting one line into two routes', 'Buses arrive at rate λ and each is independently route A with chance p. The A buses and the B buses form two independent Poisson streams, of rates λp and λ(1 − p).', ui => {
    const lam = ui.slider('λ (buses per hour)', 1, 12, 0.5, 6), p = ui.slider('ℙ(route A)', 0, 1, 0.01, 1 / 3);
    let hrs = []; const sim = () => { hrs = Array.from({ length: 3000 }, () => { const n = M.rpois(lam.v); let a = 0; for (let i = 0; i < n; i++) if (Math.random() < p.v) a++; return [a, n - a]; }); hrs.key = [lam.v, p.v].join(); };
    ui.btn('Simulate 3000 hours', sim);
    const tl = ui.plot({ x: [0, 60], y: [0, 3], h: 110, axes: false, pad: { l: 70, r: 10, t: 4, b: 4 } });
    const q = ui.plot({ x: [-0.5, 14.5], y: [0, 0.5], h: 210, xl: 'buses in an hour' });
    ui.draw(() => {
      if (hrs.key !== [lam.v, p.v].join()) sim();
      tl.clear(); const ts = []; let s = 60 * M.rexp(lam.v); while (s < 60) { ts.push([s, Math.random() < p.v]); s += 60 * M.rexp(lam.v); }
      [['all', 2.5], ['route A', 1.5], ['route B', 0.5]].forEach(([n, y]) => { tl.seg(0, y, 60, y, { c: '#ddd' }); tl.txt(0, y, n, { a: 'end', dx: -6, mid: true, size: 11.5 }); });
      ts.forEach(([t, A]) => { tl.dot(t, 2.5, { r: 4, c: A ? C.red : C.blue }); tl.dot(t, A ? 1.5 : 0.5, { r: 4, c: A ? C.red : C.blue }); });
      const a = hrs.map(h => h[0]), b = hrs.map(h => h[1]), ma = M.mean(a), mb = M.mean(b), cov = M.mean(hrs.map(([x, y]) => x * y)) - ma * mb;
      const LA = lam.v * p.v, LB = lam.v * (1 - p.v), top = Math.max(M.pois(Math.floor(LA), LA), M.pois(Math.floor(LB), LB));
      q.setY(0, Math.max(0.1, top * 1.25)); q.clear(); q.bars(M.hist(a, -0.5, 14.5, 15).map(([x, h]) => [x - 0.18, h]), 0.34, { fill: C.red, op: 0.4 }); q.bars(M.hist(b, -0.5, 14.5, 15).map(([x, h]) => [x + 0.18, h]), 0.34, { fill: C.blue, op: 0.4 });
      for (let k = 0; k <= 14; k++) { q.dot(k - 0.18, M.pois(k, LA), { r: 3, c: C.red }); q.dot(k + 0.18, M.pois(k, LB), { r: 3, c: C.blue }); }
      ui.say(`Route A ~ Poisson(λp = <b class="r">${fmt(LA, 2)}</b>) per hour (simulated mean ${fmt(ma, 2)}), route B ~ Poisson(λ(1 − p) = <b class="bl">${fmt(LB, 2)}</b>) (simulated ${fmt(mb, 2)}). ` +
        `Covariance of the two hourly counts: <b>${fmt(cov, 3)}</b> ≈ 0, independent, even though both come from the same buses. Merging them back gives rate ${fmt(LA + LB, 2)}.`);
    });
  });

  /* ===================== 25 · Brownian motion ===================== */
  add(32502, 'Zoom out a random walk: Brownian motion', 'One fine path of 4096 tiny delay nudges, viewed as a walk of n steps of size 1/√n. Every n gives a path with independent normal increments of variance equal to the time span; zooming in never smooths it.', ui => {
    const n = ui.slider('steps n', 2, 4096, 1, 16, v => v);
    let fine = []; const fresh = () => { let s = 0; fine = [0]; for (let i = 0; i < 4096; i++) { s += M.rnorm() / 64; fine.push(s); } };
    fresh(); ui.btn('New path', fresh);
    let ends = null; ui.btn('Simulate 2000 endpoints B(1)', () => { ends = Array.from({ length: 2000 }, () => { let s = 0; for (let i = 0; i < n.v; i++) s += (Math.random() < 0.5 ? 1 : -1) / Math.sqrt(n.v); return s; }); });
    const p = ui.plot({ x: [0, 1], y: [-2.5, 2.5], h: 250, xl: 't', yl: 'B(t)' });
    ui.draw(() => {
      const N = Math.pow(2, Math.round(Math.log2(n.v))), step = 4096 / N;
      p.clear(); p.path(fine.map((v, i) => [i / 4096, v]), { c: '#ccc', w: 1 }); p.path(Array.from({ length: N + 1 }, (_, i) => [i / N, fine[i * step]]), { c: C.red, w: 1.8 });
      ui.say(`Red: the walk seen at ${N} steps (each step ±√(1/${N}) in size, here using the fine path's values). Grey: the full path. ` +
        `B(t) − B(s) ~ 𝒩(0, t − s), independent over disjoint spans.` + (ends ? ` Coin-flip walk with n = ${n.v}: B(1) has mean ${fmt(M.mean(ends), 3)} and variance <b class="r">${fmt(M.variance(ends), 3)}</b> ≈ 1, whatever n (Donsker).` : ''));
      ends = null;
    });
  });

  add(32503, 'Delay builds up and is shared: Cov = min(s, t)', 'B(s) is the delay at time s, B(t) later at t. The later delay contains the earlier one, so their covariance is the earlier time. Scaling time by c and space by √c gives a path that looks the same.', ui => {
    const s = ui.slider('s', 0.05, 1, 0.01, 0.3), t = ui.slider('t', 0.05, 1, 0.01, 0.7), c = ui.slider('zoom c (shows B(ct)/√c)', 0.1, 1, 0.01, 1);
    const paths = Array.from({ length: 800 }, () => { let x = 0; return Array.from({ length: 201 }, (_, i) => i ? (x += M.rnorm() * Math.sqrt(1 / 200)) : 0); });
    const row = ui.row();
    const p = ui.plot({ x: [0, 1], y: [-3, 3], w: 400, h: 260, into: row, xl: 't', yl: 'B' });
    const q = ui.plot({ x: [-3, 3], y: [-3, 3], w: 300, h: 260, into: row, xl: 'B(s)', yl: 'B(t)' });
    ui.draw(() => {
      const i = Math.round(s.v * 200), j = Math.round(t.v * 200);
      p.clear(); paths.slice(0, 6).forEach((pp, k) => { const sc = Math.sqrt(c.v); p.path(pp.slice(0, Math.round(200 * c.v) + 1).map((v, m) => [m / (200 * c.v), v / sc]).filter(a => a[0] <= 1), { c: [C.blue, C.amber, C.purple, C.green, C.ink, C.red][k], w: 1.1 }); });
      p.vline(s.v, { c: C.ink }); p.vline(t.v, { c: C.ink });
      q.clear(); paths.forEach(pp => q.dot(pp[i], pp[j], { r: 1.5, op: 0.3 }));
      const cov = M.mean(paths.map(pp => pp[i] * pp[j])) - M.mean(paths.map(pp => pp[i])) * M.mean(paths.map(pp => pp[j]));
      ui.say(`Cov(B(s), B(t)) from 800 paths: <b class="r">${fmt(cov, 3)}</b>; theory min(s, t) = <b>${fmt(Math.min(s.v, t.v), 2)}</b>. Correlation √(min/max) = ${fmt(Math.sqrt(Math.min(s.v, t.v) / Math.max(s.v, t.v)), 3)}. ` +
        `Left: paths shown as B(ct)/√c with c = ${fmt(c.v, 2)}; zooming in on the first ${fmt(c.v, 2)} of the time and stretching by 1/√c looks statistically the same.`);
    });
  });
})();
