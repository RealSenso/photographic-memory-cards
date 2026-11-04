/* node tests/study_timer_core.test.js */
const assert = require('assert');
const T = require('../study_timer_core.js');
const S = 1000, M = 60 * S, t0 = 1_700_000_000_000;
let passed = 0;
const test = (name, fn) => { fn(); passed++; console.log('ok  ' + name); };
const learn = (extra) => T.newState('learn', null, { cards: ['11', '12', '13', '14', '15'] }, t0, extra);
const run = (s, now) => T.tick(s, now);   // {state, alert, missed}
const cueMinutes = (s) => { const sc = T.buildSchedule(s.mode, s.minutes); return sc.phases.slice(1).map(p => p.start / 60).concat(sc.total / 60); };

test('learn schedule: 2,10,18,26,34,42 phase cues, focus end 50, final 60', () => {
  const sc = T.buildSchedule('learn');
  assert.deepStrictEqual(sc.phases.map(p => p.start / 60), [0, 2, 10, 18, 26, 34, 42, 50]);
  assert.strictEqual(sc.focusEnd, 3000); assert.strictEqual(sc.total, 3600);
});
test('make schedule: cues at 10, 45, 50, 60', () => {
  const s = T.newState('make', null, {}, t0);
  assert.deepStrictEqual(cueMinutes(s), [10, 45, 50, 60]);
});
test('no cue before the first boundary; start never alarms by itself', () => {
  let s = learn();
  assert.strictEqual(run(s, t0).alert, null);
  assert.strictEqual(run(s, t0 + 119 * S + 999).alert, null);
});
test('every boundary fires exactly at its second, once', () => {
  let s = learn();
  cueMinutes(s).forEach((m, i) => {
    let r = run(s, t0 + m * M - 1);            // 1 ms early
    assert.strictEqual(r.alert, null, 'early ' + m);
    r = run(s, t0 + m * M);                    // exactly on the boundary
    assert.ok(r.alert, 'at ' + m); assert.strictEqual(r.alert.index, i + 1);
    s = r.state;
    assert.strictEqual(run(s, t0 + m * M + 5 * S).alert, null, 'no repeat ' + m);   // duplicate guard
  });
  assert.strictEqual(s.status, 'finished');
});
test('cue texts: exact end strings; card cues use supplied numbers only', () => {
  let s = learn(); const sc = T.buildSchedule('learn');
  assert.strictEqual(T.cueText(sc, 7, s.plan), 'Focus finished - log actual progress and take a break.');
  assert.strictEqual(T.cueText(sc, 8, s.plan), 'Break finished - ready for the next slot?');
  assert.ok(/Card 1 \(#11\)/.test(T.cueText(sc, 2 - 1, s.plan)));
  assert.ok(!/#/.test(T.cueText(sc, 1, {})), 'no number invented when none supplied');
});
test('a later cue never starts the next slot: finished stays finished', () => {
  let s = learn(); s = run(s, t0 + 60 * M).state;
  assert.strictEqual(s.status, 'finished');
  const r = run(s, t0 + 600 * M); assert.strictEqual(r.alert, null); assert.strictEqual(r.state.status, 'finished');
});
test('pause stops elapsed time; resume continues from the same point', () => {
  let s = learn();
  s = T.pause(s, t0 + 5 * M);
  assert.strictEqual(T.position(s, t0 + 5 * M), 300); assert.strictEqual(T.position(s, t0 + 500 * M), 300);
  assert.strictEqual(run(s, t0 + 500 * M).alert, null, 'no alarm while paused');
  s = T.resume(s, t0 + 30 * M);
  assert.strictEqual(T.position(s, t0 + 30 * M), 300);
  assert.strictEqual(T.position(s, t0 + 35 * M), 600);          // 5 + 5 minutes of real focus
  assert.strictEqual(run(s, t0 + 34 * M + 59 * S).alert.index, 1);   // 9:59 of focus: only the 2-min cue is due
  assert.strictEqual(run(T.tick(s, t0 + 34 * M + 59 * S).state, t0 + 35 * M).alert.index, 2); // 10:00 of focus
});
test('pause / resume twice accumulates and cue fires at the right wall time', () => {
  let s = learn();
  s = T.pause(s, t0 + 1 * M); s = T.resume(s, t0 + 11 * M);      // 10 min paused
  s = T.pause(s, t0 + 12 * M); s = T.resume(s, t0 + 14 * M);     // 2 min paused
  assert.strictEqual(s.pausedMs, 12 * M);
  assert.strictEqual(run(s, t0 + 13 * M + 59 * S).alert, null);  // 1.9 min of focus
  const r = run(s, t0 + 14 * M);                                  // focus = 2 min exactly
  assert.ok(r.alert && r.alert.index === 1);
});
test('returning after a long absence: one alarm for the latest cue, earlier ones silent, none repeats', () => {
  let s = learn();
  const r = run(s, t0 + 37 * M);                                  // cues at 2,10,18,26,34 all due
  assert.strictEqual(r.alert.index, 5); assert.strictEqual(r.missed.length, 4);
  assert.deepStrictEqual(r.state.fired, [1, 2, 3, 4, 5]);
  assert.strictEqual(run(r.state, t0 + 37 * M + 3 * S).alert, null);
  assert.strictEqual(run(r.state, t0 + 42 * M).alert.index, 6);
});
test('returning after the slot is over: one final alarm, whole thing marked fired', () => {
  const r = run(learn(), t0 + 400 * M);
  assert.strictEqual(r.alert.kind, 'final'); assert.strictEqual(r.missed.length, 7); assert.strictEqual(r.state.status, 'finished');
});
test('refresh recovery: state survives JSON round-trip and gives the same answers', () => {
  let s = run(learn(), t0 + 11 * M).state;
  const back = JSON.parse(JSON.stringify(s));
  assert.deepStrictEqual(back, s);
  assert.strictEqual(run(back, t0 + 11 * M + S).alert, null);
  assert.strictEqual(run(back, t0 + 18 * M).alert.index, 3);
});
test('clock going backwards never gives negative time', () => {
  const s = learn(); assert.strictEqual(T.position(s, t0 - 10 * M), 0);
  let p = T.pause(s, t0 + 5 * M); p = T.resume(p, t0 + 1 * M); assert.ok(p.pausedMs >= 0);
});
test('skip: jumps to next phase start, marks crossed cue fired silently, no alarm', () => {
  let s = learn();
  s = T.skip(s, t0 + 30 * S);                                      // inside recap -> card 1 starts
  assert.strictEqual(T.position(s, t0 + 30 * S), 120); assert.deepStrictEqual(s.fired, [1]);
  assert.strictEqual(run(s, t0 + 30 * S).alert, null);
  assert.strictEqual(run(s, t0 + 30 * S + 8 * M).alert.index, 2); // next cue 8 minutes after the skip
});
test('skip through the break finishes the slot, never auto-starts another', () => {
  let s = learn(); s = run(s, t0 + 51 * M).state; s = T.skip(s, t0 + 51 * M);
  assert.strictEqual(s.status, 'finished');
});
test('extend (stay): pushes the next cue later, never earlier than the phase start', () => {
  let s = learn();
  s = T.extend(s, t0 + 9 * M, 120);                                // at 9:00 inside card 1 (2..10) -> plan position 7:00
  assert.strictEqual(T.position(s, t0 + 9 * M), 420);
  assert.strictEqual(run(s, t0 + 11 * M + 59 * S).alert && run(s, t0 + 11 * M + 59 * S).alert.index, 1); // only the 2-min cue so far
  s = T.extend(s, t0 + 9 * M, 99999); assert.strictEqual(T.position(s, t0 + 9 * M), 120);
});
test('editable lengths: cues follow the edited boundaries; junk falls back to defaults', () => {
  const mins = [3, 5, 5, 5, 5, 5, 5, 10];
  const s = T.newState('learn', mins, {}, t0);
  assert.deepStrictEqual(cueMinutes(s), [3, 8, 13, 18, 23, 28, 33, 43]);
  assert.deepStrictEqual(T.cleanMinutes('learn', [0, 'x', -4, 999, null, 7.4]), [2, 8, 8, 8, 8, 7, 8, 10]);
});
test('end marks ended and nothing fires afterwards', () => {
  let s = T.end(learn()); assert.strictEqual(run(s, t0 + 90 * M).alert, null);
});
test('cueClock gives clock times for a backup alarm and moves with pause', () => {
  let s = learn(); const c = T.cueClock(s, t0 + 60 * S);
  assert.strictEqual(c[0].at, t0 + 2 * M); assert.strictEqual(c.length, 8);
  assert.strictEqual(T.cueClock(T.pause(s, t0), t0), null);
});
test('phaseIndex boundaries', () => {
  const sc = T.buildSchedule('learn');
  assert.strictEqual(T.phaseIndex(sc, 119.999), 0); assert.strictEqual(T.phaseIndex(sc, 120), 1);
  assert.strictEqual(T.phaseIndex(sc, 3599.9), 7); assert.strictEqual(T.phaseIndex(sc, 3600), 8);
});
test('countdown format rounds up so it hits 0:00 at the boundary', () => {
  assert.strictEqual(T.fmt(119.2), '2:00'); assert.strictEqual(T.fmt(0.01), '0:01'); assert.strictEqual(T.fmt(0), '0:00');
});
console.log('\n' + passed + ' tests passed');
