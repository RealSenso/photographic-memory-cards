/* Where each CMO practice question belongs (audit of 6 Nov 2026, topics 10-19).
   Loaded right after the CMO practice files. It works on the questions by their numeric id, so the question files (one of them is
   generated) stay as they are, the exam source strings are untouched, and the visible P-numbers renumber by themselves.
   - moves:  a question goes to the topic whose cards teach every tool it needs
   - splits: a mixed question is cut into its parts; each part goes where its tools are taught
   - stretch: a note shown on questions that need a step no card scaffolds
   - mockLocked: questions from the 2025 Midterm 3 paper stay out of the decks until the 9 Nov mock is done */
(function () {
  'use strict';
  const all = window.PRACTICE_DATA = (window.PRACTICE_DATA || []).flat(Infinity);
  const TOP = {
    3: '03_Convexity_and_Strong_Convexity',
    10: '10_Separating_Hyperplanes_and_Farkas_Lemma',
    11: '11_Karush_Kuhn_Tucker_Conditions_FONC_and_Sufficiency',
    13: '13_Projections_onto_Convex_Sets',
    16: '16_Lagrangian_Duality_and_Slaters_Condition',
    18: '18_Linear_Programming_Duality_and_Polyhedral_Geometry'
  };
  const at = id => all.findIndex(q => q.id === id);
  const get = id => all[at(id)];
  /* the slot right after the last question already in a topic */
  const endOf = topicId => { let j = -1; all.forEach((q, k) => { if (q.topicId === topicId) j = k + 1; }); return j < 0 ? all.length : j; };
  function place(q, topicId, afterId) {
    const i = all.indexOf(q);
    if (i >= 0) all.splice(i, 1);
    q.topicId = topicId;
    const j = afterId != null && at(afterId) >= 0 ? at(afterId) + 1 : endOf(topicId);
    all.splice(j, 0, q);
  }
  /* cut "<p><span class="part">(a)</span> …</p>" paragraphs out of a question or solution */
  const PART = /<p><span class="part">\((\w)\)<\/span>[\s\S]*?<\/p>/g;
  function pick(html, letters) {
    const intro = html.replace(PART, '').trim();
    const parts = [...html.matchAll(PART)].filter(m => letters.includes(m[1])).map(m => m[0]);
    return { intro, body: parts.join('\n') };
  }
  function split(id, keep, take) {
    const q = get(id);
    if (!q) return null;
    const qa = pick(q.question, keep.letters), sa = pick(q.solution, keep.letters);
    const qb = pick(q.question, take.letters), sb = pick(q.solution, take.letters);
    const part = Object.assign({}, q, {
      id: take.id, question: qb.intro + '\n' + qb.body, solution: sb.body, marks: take.marks, takeaway: take.takeaway,
      partNote: take.note, splitFrom: id
    });
    Object.assign(q, { question: qa.intro + '\n' + qa.body, solution: sa.body, marks: keep.marks, takeaway: keep.takeaway, partNote: keep.note });
    return part;
  }

  /* ---- splits ---- */
  const conv = split(601001,
    { letters: 'c', marks: '1 mark', note: 'part (c)', takeaway: 'The separating hyperplane theorem separates a point from any closed convex set (and two disjoint convex sets), not just halfspaces.' },
    { id: 691001, letters: 'ab', marks: '2 marks', note: 'parts (a), (b)', takeaway: 'Sublevel sets of convex functions are convex. The outside of a ball is not.' });
  if (conv) place(conv, TOP[3]);                       // Topic 3 review slot
  const entropyMin = split(601105,
    { letters: 'ab', marks: '8 marks', note: 'parts (a), (b)', takeaway: 'Entropy over the simplex: KKT gives the uniform distribution, value log d.' },
    { id: 691105, letters: 'c', marks: '2 marks', note: 'part (c)', takeaway: 'A concave function on a polytope is minimised at a vertex: entropy is 0 at the point masses e_i.' });

  /* ---- moves (into the topic whose cards teach the tools) ---- */
  const move = (id, t, afterId) => { const q = get(id); if (q) place(q, TOP[t], afterId); };
  move(601023, 13, 601305);                            // projection existence + VI, after the non-expansiveness proof
  move(601024, 13);                                    // VI => strict separation: Topic 13 capstone
  move(601124, 16);                                    // complementary slackness and sensitivities (shadow prices)
  move(601524, 18);                                    // active-set vs interior-point complexity
  if (entropyMin) place(entropyMin, TOP[18]);          // concave minimisation at vertices (taught on 18C3)

  /* ---- stretch notes ---- */
  const STRETCH = {
    601022: 'The strict-inequality proof pattern is not scaffolded on any card.',
    601101: 'The relaxation argument in part (b) is a step no card scaffolds.',
    601224: 'Needs a null-space basis, which no Topic 12 card teaches (the bordered Hessian of 12C3 is the taught route).',
    601424: 'Finite active-set identification is not taught on a Topic 14 card; answer it as a self-contained explanation.',
    601522: 'Null-space basis construction is not taught; 15C1 teaches the direct KKT system.',
    601624: 'A proof-level question: the stretch item of this topic.'
  };
  Object.keys(STRETCH).forEach(id => { const q = get(Number(id)); if (q) q.stretch = STRETCH[id]; });

  /* ---- 2025 Midterm 3 questions: locked until the mock on 9 Nov 2026 is done ---- */
  [601002, 601302, 601402, 601502, 601801, 601803].forEach(id => { const q = get(id); if (q) q.mockLocked = true; });
  const MOCK_DONE = new Date(2026, 10, 10);             // from 10 Nov 2026, local time
  try {
    const p = new URLSearchParams(location.search).get('mock');
    if (p === 'done') localStorage.setItem('plates_mock_unlocked', '1');
    if (p === 'lock') localStorage.removeItem('plates_mock_unlocked');
  } catch (e) {}
  window.mockUnlocked = () => { try { if (localStorage.getItem('plates_mock_unlocked') === '1') return true; } catch (e) {} return new Date() >= MOCK_DONE; };

  /* ---- 601623: only the example that works, without the abandoned attempts ---- */
  const gap = get(601623);
  if (gap) {
    gap.solution = String.raw`<p><b>Example.</b> Keep $x\ge0$ as the domain $X=[0,\infty)$ and dualise only the non-convex constraint:
$$\min_{x\ge0}\ x\quad\text{s.t.}\quad g(x)=1-x^2\le0 .$$</p>
<p><b>Primal.</b> The feasible points are $x\ge1$, so $p^*=1$ (at $x=1$).</p>
<p><b>Dual function.</b> For $\mu\ge0$, $L(x,\mu)=x+\mu(1-x^2)=-\mu x^2+x+\mu$ and $q(\mu)=\inf_{x\ge0}L(x,\mu)$. If $\mu>0$, the $-\mu x^2$ term sends $L\to-\infty$ as $x\to\infty$, so $q(\mu)=-\infty$. If $\mu=0$, $q(0)=\inf_{x\ge0}x=0$.</p>
<p><b>Dual.</b> $d^*=\max_{\mu\ge0}q(\mu)=q(0)=0$, so <span class="ans">$p^*-d^*=1-0=1>0$</span>.</p>
<p><b>Why.</b> The feasible set $[1,\infty)$ happens to be convex, but it is described by $1-x^2\le0$ with $1-x^2$ concave, so this is not a convex program and Slater’s theorem does not apply. Weak duality $d^*\le p^*$ still holds; nothing forces equality.</p>`;
    gap.takeaway = 'A non-convex constraint can leave a positive gap: $\\min_{x\\ge0}x$ s.t. $1-x^2\\le0$ has $p^*=1$ but $d^*=0$.';
  }
})();
