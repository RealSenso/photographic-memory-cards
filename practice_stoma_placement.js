/* Where each older StoMA practice question belongs (audit of 12 Nov 2026).
   Loaded right after practice_stoma.js (before the Ivy League questions). It works on questions by their numeric id,
   so practice_stoma.js stays as it is and the visible P-numbers renumber by themselves.
   - moves:   a question goes to the topic whose cards teach the tools it needs
   - splits:  a part that needs a later topic's tool is cut out and placed there
   - stretch: a note on questions that need a step no card scaffolds (Cantelli, the delta method and martingale
     convergence are now bridge bullets on 6.02, 15.05 and 26.06, so those questions are no longer stretch) */
(function () {
  'use strict';
  const all = window.PRACTICE_DATA = (window.PRACTICE_DATA || []).flat(Infinity);
  const TOP = {
    5: ['05_Expectation_Variance_Moments_and_Generating_Functions', '05 · Expectation, Variance & Generating Functions'],
    8: ['08_Multiple_Random_Variables_and_Order_Statistics', '08 · Order Statistics'],
    26: ['26_Martingales_and_Optional_Stopping_Theorem', '26 · Martingales & Optional Stopping']
  };
  /* use the topic titles the cards themselves carry, when they are loaded */
  (window.MASTER_CARDS_DATA || []).forEach(c => { for (const k in TOP) if (c.topicId === TOP[k][0]) TOP[k][1] = c.topicTitle; });
  const at = id => all.findIndex(q => q.id === id);
  const get = id => all[at(id)];
  const endOf = topicId => { let j = -1; all.forEach((q, k) => { if (q.topicId === topicId) j = k + 1; }); return j < 0 ? all.length : j; };
  function place(q, t) {
    const i = all.indexOf(q); if (i >= 0) all.splice(i, 1);
    q.topicId = TOP[t][0]; q.topicTitle = TOP[t][1];
    all.splice(endOf(q.topicId), 0, q);
  }

  /* ---- moves ---- */
  const move = (id, t) => { const q = get(id); if (q) place(q, t); };
  move(30393, 5);    // Cauchy has no mean: an expectation question (Topic 05), not a density one
  move(30793, 8);    // competing exponentials: the minimum of exponentials is taught on the order-statistics cards

  /* ---- split: 32591 part (c) needs optional stopping (Topic 26) ---- */
  const hit = get(32591);
  if (hit) {
    const QP = /<p><span class="part">\((\w)\)<\/span>[\s\S]*?<\/p>/g, SP = /<p><span class="part">Part \((\w)\)[\s\S]*?<\/p>/g;
    const keep = (html, re, letters) => html.replace(re, (m, l) => letters.includes(l) ? m : '').trim();
    const part = Object.assign({}, hit, {
      id: 392591, question: keep(hit.question, QP, 'c'), solution: keep(hit.solution, SP, 'c'), marks: '',
      partNote: 'part (c)', splitFrom: 32591,
      takeaway: 'Optional stopping on the exponential martingale e^{θB(t) − θ²t/2} gives $\\mathbb E[e^{-s\\tau_a}]=e^{-a\\sqrt{2s}}$.'
    });
    Object.assign(hit, { question: keep(hit.question, QP, 'ab'), solution: keep(hit.solution, SP, 'ab'), partNote: 'parts (a), (b)' });
    place(part, 26);
  }

  /* ---- stretch notes ---- */
  const STRETCH = {
    31092: 'Part (b) needs convergence in law (Topic 15), which comes later.',
    31992: 'Part (c), the limit of Pⁿ, is Topic 20 material (stationary distribution and limit theorem).'
  };
  Object.keys(STRETCH).forEach(id => { const q = get(Number(id)); if (q) q.stretch = STRETCH[id]; });
})();
