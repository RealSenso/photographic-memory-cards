/* Study-slot timer: the clock and cue logic, with no DOM, so it can be tested in Node.
   Time is never counted with setInterval ticks. Every answer is derived from wall-clock timestamps kept in the state,
   so a refresh, a throttled background tab or a frozen phone gives the right phase the moment the page runs again. */
(function (root) {
  'use strict';

  /* [id, label, minutes]; the last phase of every mode is the break, and focus ends where it starts */
  const DEFAULTS = {
    learn: [['recap', 'Recap prerequisites', 2], ['c1', 'Card 1', 8], ['c2', 'Card 2', 8], ['c3', 'Card 3', 8], ['c4', 'Card 4', 8], ['c5', 'Card 5', 8],
            ['revisit', 'Revisit unclear material, log understanding', 8], ['break', 'Break', 10]],
    make:  [['revise', 'Revise the sub-topic', 10], ['make', 'Make physical cards', 35], ['check', 'Check cards, record made / remaining', 5], ['break', 'Break', 10]]
  };
  const MODE_LABEL = { learn: 'Learn', make: 'Revise + Make' };
  const FOCUS_END_TEXT = 'Focus finished - log actual progress and take a break.';
  const FINAL_TEXT = 'Break finished - ready for the next slot?';

  function defaultMinutes(mode) { return DEFAULTS[mode].map(p => p[2]); }

  /* editable lengths: whole minutes 1..180, anything else falls back to the default for that phase */
  function cleanMinutes(mode, arr) {
    const def = defaultMinutes(mode);
    return def.map((d, i) => { const n = Math.round(Number(arr && arr[i])); return n >= 1 && n <= 180 ? n : d; });
  }

  /* [{id,label,min,start,end,isBreak}] with start/end in seconds from the slot start */
  function buildSchedule(mode, minutes) {
    const mins = cleanMinutes(mode, minutes), def = DEFAULTS[mode];
    let t = 0;
    const phases = def.map((p, i) => {
      const o = { id: p[0], label: p[1], min: mins[i], start: t, end: t + mins[i] * 60, isBreak: i === def.length - 1 };
      t = o.end; return o;
    });
    return { mode, phases, total: t, focusEnd: phases[phases.length - 1].start };
  }

  const pad = n => String(n).padStart(2, '0');
  const fmt = sec => { sec = Math.max(0, Math.ceil(sec - 1e-9)); return Math.floor(sec / 60) + ':' + pad(sec % 60); };
  const minuteMark = sec => { const m = sec / 60; return Number.isInteger(m) ? String(m) : m.toFixed(1); };

  /* the cue for the boundary that opens phase i (1..n-1) or ends the slot (i = n) */
  function cueText(sched, i, plan) {
    plan = plan || {};
    const n = sched.phases.length, at = minuteMark(i < n ? sched.phases[i].start : sched.total);
    if (i === n) return FINAL_TEXT;
    const ph = sched.phases[i];
    if (ph.isBreak) return FOCUS_END_TEXT;
    const num = k => (plan.cards && plan.cards[k] ? ' (#' + plan.cards[k] + ')' : '');
    if (sched.mode === 'learn') {
      if (ph.id === 'revisit') return 'Minute ' + at + ': revisit unclear material and log what you actually understood.';
      const k = Number(ph.id.slice(1)) - 1;
      return 'Minute ' + at + ': Card ' + (k + 1) + num(k) + '. Pacing nudge only - stay if you are mid-thought.';
    }
    if (ph.id === 'make') return 'Minute ' + at + ': revision done - start making the physical cards.';
    return 'Minute ' + at + ': check the cards, record what was made and what remains.';
  }

  function newState(mode, minutes, plan, now, opts) {
    return { v: 1, id: String(now), mode, minutes: cleanMinutes(mode, minutes), plan: plan || {}, startedAt: now, pausedAt: null, pausedMs: 0,
             adjust: 0, speed: (opts && opts.speed) || 1, fired: [], status: 'running', lastCue: null, logged: false };
  }

  /* running time with pauses removed (x speed, only for testing), then the manual skip / stay adjustment */
  function elapsed(s, now) {
    const end = s.pausedAt != null ? s.pausedAt : now;
    return Math.max(0, (end - s.startedAt - s.pausedMs) / 1000) * s.speed;
  }
  function position(s, now) { return Math.max(0, elapsed(s, now) + s.adjust); }

  /* index of the phase pos is in; phases.length once the slot is over. A boundary belongs to the phase it opens. */
  function phaseIndex(sched, pos) {
    if (pos >= sched.total) return sched.phases.length;
    for (let i = sched.phases.length - 1; i >= 0; i--) if (pos >= sched.phases[i].start) return i;
    return 0;
  }

  const clone = s => JSON.parse(JSON.stringify(s));

  /* Fire what is due. Every due boundary is marked fired, but only the latest one alarms; earlier ones come back as `missed`
     (shown silently), so coming back after a long absence gives one alarm, never a burst, and a cue never fires twice. */
  function tick(s, now) {
    if (s.status !== 'running') return { state: s, alert: null, missed: [] };
    const sched = buildSchedule(s.mode, s.minutes), pos = position(s, now), n = sched.phases.length, next = clone(s);
    const due = [];
    for (let i = 1; i <= n; i++) {
      const at = i < n ? sched.phases[i].start : sched.total;
      if (pos >= at && !next.fired.includes(i)) due.push(i);
    }
    if (!due.length) return { state: s, alert: null, missed: [] };
    due.forEach(i => next.fired.push(i));
    const last = due[due.length - 1];
    const mk = i => ({ index: i, text: cueText(sched, i, s.plan), kind: i === n ? 'final' : sched.phases[i].isBreak ? 'focusEnd' : 'phase' });
    const alert = mk(last), missed = due.slice(0, -1).map(mk);
    next.lastCue = Object.assign({ firedAt: now }, alert);
    if (last === n) next.status = 'finished';
    return { state: next, alert, missed };
  }

  function pause(s, now) { if (s.status !== 'running') return s; const x = clone(s); x.pausedAt = now; x.status = 'paused'; return x; }
  function resume(s, now) {
    if (s.status !== 'paused') return s;
    const x = clone(s); x.pausedMs += Math.max(0, now - x.pausedAt); x.pausedAt = null; x.status = 'running'; return x;
  }
  function end(s) { if (s.status === 'ended') return s; const x = clone(s); x.status = 'ended'; return x; }

  /* manual advance: jump to the start of the next phase; the boundary crossed is marked fired without an alarm */
  function skip(s, now) {
    if (s.status !== 'running' && s.status !== 'paused') return s;
    const sched = buildSchedule(s.mode, s.minutes), pos = position(s, now), i = phaseIndex(sched, pos), x = clone(s);
    const target = i + 1 < sched.phases.length ? sched.phases[i + 1].start : sched.total;
    x.adjust += target - pos;
    if (!x.fired.includes(i + 1)) x.fired.push(i + 1);
    if (i + 1 >= sched.phases.length) x.status = 'finished';
    return x;
  }
  /* stay longer on the current phase: moves the plan back, never before the phase's own start */
  function extend(s, now, sec) {
    if (s.status !== 'running' && s.status !== 'paused') return s;
    const sched = buildSchedule(s.mode, s.minutes), pos = position(s, now), i = phaseIndex(sched, pos);
    if (i >= sched.phases.length) return s;
    const x = clone(s); x.adjust -= Math.min(sec || 120, pos - sched.phases[i].start); return x;
  }

  /* when each cue is due on the clock, for a backup phone alarm; null while paused */
  function cueClock(s, now) {
    if (s.status !== 'running') return null;
    const sched = buildSchedule(s.mode, s.minutes), pos = position(s, now), n = sched.phases.length, out = [];
    for (let i = 1; i <= n; i++) {
      const at = i < n ? sched.phases[i].start : sched.total;
      out.push({ index: i, text: cueText(sched, i, s.plan), at: now + (at - pos) / s.speed * 1000, fired: s.fired.includes(i) });
    }
    return out;
  }

  const api = { DEFAULTS, MODE_LABEL, FOCUS_END_TEXT, FINAL_TEXT, defaultMinutes, cleanMinutes, buildSchedule, cueText, newState, elapsed, position,
                phaseIndex, tick, pause, resume, end, skip, extend, cueClock, fmt };
  if (typeof module !== 'undefined' && module.exports) module.exports = api; else root.StudyTimerCore = api;
})(typeof window !== 'undefined' ? window : globalThis);
