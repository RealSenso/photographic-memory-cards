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
test('mergeRun: newer remote seq is adopted', () => {
  const r = T.mergeRun({ on: false, seq: 100 }, { v: 1, on: true, until: null, seq: 200, by: 'agent' }, 1000);
  assert.strictEqual(r.adopt, true); assert.strictEqual(r.push, false);
  assert.deepStrictEqual(r.state, { on: true, until: null, seq: 200, by: 'agent', dev: null });
});
test('mergeRun: older or equal remote seq is ignored and local ahead pushes', () => {
  assert.strictEqual(T.mergeRun({ on: true, seq: 300 }, { on: false, seq: 200 }, 1000).adopt, false);
  assert.strictEqual(T.mergeRun({ on: true, seq: 300 }, { on: false, seq: 200 }, 1000).push, true);
  assert.strictEqual(T.mergeRun({ on: true, seq: 200 }, { on: false, seq: 200 }, 1000).push, false);
});
test('mergeRun: no remote file publishes the local baseline, even at seq 0', () => {
  const r = T.mergeRun({ on: true, ms: 1234 }, null, 1000);
  assert.strictEqual(r.adopt, false); assert.strictEqual(r.push, true);
  assert.strictEqual(r.state.on, true); assert.strictEqual(r.state.seq, 0);
});
test('mergeRun: a remote start whose deadline already passed applies as paused (no backfill)', () => {
  const r = T.mergeRun({ on: false, seq: 0 }, { v: 1, on: true, until: 500, seq: 200, by: 'agent' }, 1000);
  assert.strictEqual(r.adopt, true);
  assert.deepStrictEqual(r.state, { on: false, until: null, seq: 200, by: 'agent', dev: null });
});
test('mergeRun: a remote start with a future deadline keeps it', () => {
  const r = T.mergeRun({ on: false, seq: 0 }, { v: 1, on: true, until: 5000, seq: 200, by: 'agent' }, 1000);
  assert.deepStrictEqual(r.state, { on: true, until: 5000, seq: 200, by: 'agent', dev: null });
});
test('mergeRun: garbage remote run state is ignored', () => {
  assert.strictEqual(T.mergeRun({ on: true, seq: 5 }, 'junk', 1000).push, true);
  assert.strictEqual(T.mergeRun({ on: true, seq: 5 }, { on: true }, 1000).push, true);
});
test('mergeRun: the counting device travels with the run state', () => {
  const r = T.mergeRun({ on: true, seq: 100, dev: 'a' }, { v: 1, on: true, until: null, seq: 200, by: 'claim', dev: 'b' }, 1000);
  assert.strictEqual(r.state.dev, 'b');
  assert.strictEqual(T.mergeRun({ on: false, seq: 0 }, { on: true, seq: 200, by: 'agent' }, 1000).state.dev, null);
  assert.strictEqual(T.mergeRun({ on: false, seq: 0 }, { on: true, seq: 200, dev: 42 }, 1000).state.dev, null);
});
console.log('\n' + n + ' tests passed');
