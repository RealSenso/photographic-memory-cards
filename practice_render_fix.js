/* Practice questions, every subject: loaded after all the practice files, which stay as they are.
   An answer highlight written inside a formula stops KaTeX reading that formula, so it becomes a KaTeX box.
   A bare % inside a formula starts a TeX comment and cuts the formula off, so it is escaped. */
(function () {
  'use strict';
  const ANS = /<span class="ans">([\s\S]*?)<\/span>/g;
  const inMath = s => s.replace(/\$\$[\s\S]+?\$\$|\$[^$]+\$/g, m => m.replace(ANS, '\\boxed{$1}').replace(/(^|[^\\])%/g, '$1\\%'));
  const all = window.PRACTICE_DATA = (window.PRACTICE_DATA || []).flat(Infinity);
  all.forEach(q => ['question', 'solution', 'takeaway'].forEach(k => { if (typeof q[k] === 'string') q[k] = inMath(q[k]); }));
})();
