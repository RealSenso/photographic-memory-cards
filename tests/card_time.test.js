/* node tests/card_time.test.js */
const assert = require('assert');
const T = require('../card_time.js');
let n = 0; const test = (name, fn) => { fn(); n++; console.log('ok  ' + name); };
test('merge keeps the larger count per device and card; never adds devices together twice', () => {
  const a = { d1: { '101': 5000, '102': 100 } }, b = { d1: { '101': 3000 }, d2: { '101': 7000 } };
  assert.deepStrictEqual(T.merge(a, b), { d1: { '101': 5000, '102': 100 }, d2: { '101': 7000 } });
  assert.strictEqual(T.total(T.merge(a, b), '101'), 12000);
  assert.deepStrictEqual(T.merge(T.merge(a, b), b), T.merge(a, b));
  assert.deepStrictEqual(T.merge(a, b), T.merge(b, a));
});
test('ahead tells whether a push / pull is needed', () => {
  assert.strictEqual(T.ahead({ d1: { x: 2 } }, { d1: { x: 1 } }), true);
  assert.strictEqual(T.ahead({ d1: { x: 1 } }, { d1: { x: 1 } }), false);
  assert.strictEqual(T.ahead({}, { d1: { x: 1 } }), false);
});
test('garbage from the gist is ignored', () => {
  assert.deepStrictEqual(T.merge({ d1: { x: 1 } }, { d2: null, d3: 'x' }), { d1: { x: 1 } });
});
test('formats', () => {
  assert.strictEqual(T.fmtClock(0), '0:00'); assert.strictEqual(T.fmtClock(65000), '1:05'); assert.strictEqual(T.fmtClock(3725000), '1:02:05');
  assert.strictEqual(T.fmtShort(59000), '<1m'); assert.strictEqual(T.fmtShort(125 * 60000), '2h 05m');
});
console.log('\n' + n + ' tests passed');
