/* DIP practice audit (22 Nov 2026): keep only questions at the level of the real PYQs or above.
   Loaded right after practice_dip.js, which stays as it is, so a question comes back by removing its id here. */
(function () {
  'use strict';
  const BELOW_PYQ = new Set([
    40193, 40292, 40393, 40493,   // plug-in warp, matrix arithmetic, gamma substitution, labelling trace
    40592, 40691, 40692,          // equalization table, rank check, one 3x3 sum
    41291, 41293,                 // one-step mean / median
    41891, 41992, 42091           // nearest centroid, integral image fill, CNN formula substitution
  ]);
  window.PRACTICE_DATA = (window.PRACTICE_DATA || []).flat(Infinity).filter(q => !(q.subject === 'DIP' && BELOW_PYQ.has(q.id)));
})();
