/* Card study time: how long each card has been open while the timer is playing.
   Time counts only for the card on screen, only while this page is visible, and only while Play is on. Switching card stops the old card's
   count and starts the new one's. A beep sounds after every 10 minutes of playing time since you last pressed Play, counted over all cards
   together (not per card).
   Totals sync through the same private gist as progress, as a per-device counter (each device only ever raises its own numbers, merging takes the
   larger value per device and card), so two devices never double-count or erase each other.
   The play/pause state also syncs (plates-card-run.json, last change wins by `seq` timestamp), so the timer can be started or paused
   from another device - e.g. Instinct starting it when he says "starting" and pausing it when the slot ends. A start command can carry an
   `until` deadline that pauses the timer on this page by itself, exactly on time, with no sync round-trip. A stale command whose deadline
   has already passed is applied as paused, so time is never backfilled: counting only ever accrues live, while this page is visible.
   Only one device counts at a time: the run state names the device in use (`dev`, set by Play or by any tap / key press there while the
   timer is on), so a second screen left open on the same card does not double the time or beep as well. After a remote start (no `dev`
   yet) a device counts only while its window has focus, until someone touches one. */
(function (root) {
  'use strict';
  const KEY = 'plates_cardtime_v1', RUN = 'plates_cardtime_run_v1', BEEP_EVERY = 10 * 60 * 1000, MAX_STEP = 2000;

  /* ---------- pure helpers (also used by the Node test) ---------- */
  /* G-counter merge: {dev: {card: ms}} */
  function merge(a, b) {
    const out = {};
    [a || {}, b || {}].forEach(src => Object.keys(src).forEach(dev => {
      const m = src[dev]; if (!m || typeof m !== 'object') return;
      out[dev] = out[dev] || {};
      Object.keys(m).forEach(k => { const v = Number(m[k]) || 0; if (v > (out[dev][k] || 0)) out[dev][k] = v; });
    }));
    return out;
  }
  /* does `a` hold any number larger than `b`'s? */
  function ahead(a, b) {
    return Object.keys(a || {}).some(dev => Object.keys(a[dev]).some(k => (a[dev][k] || 0) > (((b || {})[dev] || {})[k] || 0)));
  }
  function total(c, key) { let t = 0; Object.keys(c).forEach(dev => { t += c[dev][key] || 0; }); return t; }
  const pad = n => String(n).padStart(2, '0');
  function fmtClock(ms) { const s = Math.floor(ms / 1000), h = Math.floor(s / 3600), m = Math.floor(s / 60) % 60; return (h ? h + ':' + pad(m) : m) + ':' + pad(s % 60); }
  function fmtShort(ms) { const m = Math.floor(ms / 60000), h = Math.floor(m / 60); return h ? h + 'h ' + pad(m % 60) + 'm' : m ? m + 'm' : '<1m'; }
  /* shared play/pause state: {on, until, seq, by}; the larger seq wins. A remote start whose deadline already passed applies as paused. */
  function mergeRun(local, remote, now) {
    const l = Object.assign({ on: false, until: null, seq: 0, by: 'manual', dev: null }, local || {});
    const r = (remote && typeof remote === 'object' && typeof remote.seq === 'number') ? remote : null;
    const rseq = r ? r.seq : -1;
    if (rseq > (l.seq || 0)) {
      let on = !!r.on, until = (typeof r.until === 'number') ? r.until : null;
      if (on && until && until <= now) { on = false; until = null; }
      return { adopt: true, state: { on, until, seq: rseq, by: (r && r.by) || 'remote', dev: typeof r.dev === 'string' ? r.dev : null }, push: false };
    }
    return { adopt: false, state: l, push: (l.seq || 0) > rseq };
  }
  const api = { merge, ahead, total, fmtClock, fmtShort, mergeRun };
  if (typeof module !== 'undefined' && module.exports) { module.exports = api; return; }

  /* ---------- page ---------- */
  const lsGet = (k, d) => { try { const v = JSON.parse(localStorage.getItem(k)); return v == null ? d : v; } catch (e) { return d; } };
  const lsSet = (k, v) => { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} };
  let data = lsGet(KEY, null);
  if (!data || !data.dev || !data.c) data = { dev: Math.random().toString(36).slice(2, 10), c: {} };
  data.c[data.dev] = data.c[data.dev] || {};
  let run = Object.assign({ on: false, ms: 0, until: null, seq: 0, by: 'manual', dev: null }, lsGet(RUN, {}));
  /* seq must never go backwards, or a local action could lose to an older remote state on the next sync */
  const nextSeq = () => Math.max(Date.now(), (run.seq || 0) + 1);
  let curKey = null, last = Date.now(), dirty = false, ctx = null;
  ['plates_timer_v1', 'plates_timer_prefs_v1', 'plates_timer_prefs_v1_plan'].forEach(k => { try { localStorage.removeItem(k); } catch (e) {} });   // the old slot timer

  /* card id for explanation cards (split halves share it); subject + question id for practice questions */
  function keyOf(c) {
    if (!c) return null;
    return c.kind === 'practice' ? 'p:' + c.subject + ':' + (c.id != null ? 'id' + c.id : c.topicId + ':' + c.cardNumber) : c.id != null ? String(c.id) : null;   // practice by id, so moving a question keeps its time
  }
  let subjOf = null;
  function subjectOfKey(k) {
    if (k.startsWith('p:')) return k.split(':')[1];
    if (!subjOf) { subjOf = {}; masterCards.forEach(c => { subjOf[String(c.id)] = c.subject || 'CMO'; }); }
    return subjOf[k];
  }
  function subjectTotal(sub) {
    const seen = new Set(); let t = 0;
    Object.keys(data.c).forEach(dev => Object.keys(data.c[dev]).forEach(k => seen.add(k)));
    seen.forEach(k => { if (subjectOfKey(k) === sub) t += total(data.c, k); });
    return t;
  }
  const visibleCard = () => (typeof deck !== 'undefined' && deck.length ? deck[idx] : null);

  function beep() {
    try {
      if (!ctx) { const A = window.AudioContext || window.webkitAudioContext; if (!A) return; ctx = new A(); }
      if (ctx.state === 'suspended') ctx.resume();
      const g = ctx.createGain(); g.connect(ctx.destination); let t = ctx.currentTime + 0.02;
      [880, 1175].forEach(f => {
        const o = ctx.createOscillator(); o.frequency.value = f; o.connect(g);
        g.gain.setValueAtTime(0, t); g.gain.linearRampToValueAtTime(0.25, t + 0.02); g.gain.setValueAtTime(0.25, t + 0.18); g.gain.linearRampToValueAtTime(0, t + 0.24);
        o.start(t); o.stop(t + 0.26); t += 0.32;
      });
    } catch (e) {}
  }
  const unlock = () => { try { if (!ctx) { const A = window.AudioContext || window.webkitAudioContext; if (A) ctx = new A(); } if (ctx && ctx.state === 'suspended') ctx.resume(); } catch (e) {} };
  document.addEventListener('pointerdown', () => { if (run.on) unlock(); }, true);

  /* Credit the time since the last call to the card that was on screen during it, then follow the card now shown. */
  function tick() {
    const now = Date.now(), dt = Math.max(0, Math.min(now - last, MAX_STEP));
    last = now;
    if (run.on && run.until && now >= run.until) {   /* the slot's deadline pauses the timer on this page by itself */
      run.on = false; run.until = null; run.seq = nextSeq(); run.by = 'auto'; dirty = true;
      if (root.syncSoon) root.syncSoon();
    }
    if (run.on && !document.hidden && curKey && countsHere()) {
      const mine = data.c[data.dev];
      mine[curKey] = (mine[curKey] || 0) + dt;
      const before = run.ms; run.ms += dt; dirty = true;
      if (Math.floor(run.ms / BEEP_EVERY) > Math.floor(before / BEEP_EVERY)) beep();
    }
    curKey = keyOf(visibleCard());
    paint();
  }
  /* the device in use counts; with no device named yet (a remote start), whichever window has focus */
  function countsHere() { return run.dev ? run.dev === data.dev : (typeof document.hasFocus !== 'function' || document.hasFocus()); }
  /* touching this device while the timer runs elsewhere moves the counting here */
  function claim() {
    if (!run.on || run.dev === data.dev) return;
    tick(); run.dev = data.dev; run.seq = nextSeq(); run.by = 'claim'; run.ms = 0; dirty = true; persist(); paint();
    if (root.syncSoon) root.syncSoon();
  }
  document.addEventListener('pointerdown', claim, true);
  document.addEventListener('keydown', claim, true);
  function persist() { if (!dirty) return; lsSet(KEY, data); lsSet(RUN, run); dirty = false; }

  function paint() {
    const t = document.getElementById('ctime');
    if (t) t.textContent = fmtClock(curKey ? total(data.c, curKey) : 0);
    const b = document.getElementById('ctime-btn');
    if (b) { b.textContent = run.on ? '❚❚' : '▶'; b.setAttribute('aria-label', run.on ? 'Pause card timer' : 'Start card timer'); b.classList.toggle('on', run.on); b.title = run.on && !countsHere() ? 'Counting on your other device - tap anywhere here to count on this one' : 'Play / pause the card timer (T)'; }
    document.querySelectorAll('.stime[data-s]').forEach(el => { const v = subjectTotal(el.dataset.s); el.textContent = v ? fmtShort(v) : ''; });
  }

  /* Play starts a fresh 10-minute count (run.ms = playing time since the last Play, across every card you open);
     Pause freezes it, so the beep comes after 10 minutes of real study, then every 10 minutes after that. */
  function toggle() { tick(); run.on = !run.on; run.until = null; run.seq = nextSeq(); run.by = 'manual'; run.dev = data.dev; if (run.on) { run.ms = 0; unlock(); } dirty = true; persist(); paint(); if (root.syncSoon) root.syncSoon(); }
  /* Remote command from another device (e.g. Instinct on "starting" / at the slot's end). Latest seq wins over anything older. */
  function command(cmd, until) {
    tick();
    if (cmd === 'start') { run.on = true; run.ms = 0; const u = Number(until); run.until = (isFinite(u) && u > Date.now()) ? u : null; }
    else if (cmd === 'pause') { run.on = false; run.until = null; }
    else return false;
    run.seq = nextSeq(); run.by = 'agent'; run.dev = null; dirty = true; persist(); paint();
    if (root.syncSoon) root.syncSoon();
    return true;
  }
  function barHtml(card) {
    const k = keyOf(card);
    return `<span class="ctime-wrap"><button class="ctime-btn ${run.on ? 'on' : ''}" id="ctime-btn" onclick="CardTime.toggle()" aria-label="${run.on ? 'Pause' : 'Start'} card timer" title="Play / pause the card timer (T)">${run.on ? '❚❚' : '▶'}</button><span class="ctime" id="ctime" title="Time this card has been open with the timer playing">${fmtClock(k ? total(data.c, k) : 0)}</span></span>`;
  }
  const subjHtml = sub => { const v = subjectTotal(sub); return `<span class="stime" data-s="${sub}" title="Total card time in ${sub}">${v ? fmtShort(v) : ''}</span>`; };

  /* sync: index.html's syncNow passes the gist copies and stores what this returns */
  function syncMerge(remote, remoteRun) {
    const rc = remote && remote.c && typeof remote.c === 'object' ? remote.c : {};
    const merged = merge(data.c, rc);
    if (ahead(rc, data.c)) { data.c = merged; data.c[data.dev] = data.c[data.dev] || {}; lsSet(KEY, data); paint(); }
    const mr = mergeRun(run, remoteRun, Date.now());
    if (mr.adopt) {
      tick();   /* settle counting under the old state before switching */
      run.on = mr.state.on; run.until = mr.state.until; run.seq = mr.state.seq; run.by = mr.state.by; run.dev = mr.state.dev;
      lsSet(RUN, run); paint();
    }
    return { push: ahead(data.c, rc), content: JSON.stringify({ v: 1, c: merge(data.c, rc) }),
      pushRun: mr.push, runContent: JSON.stringify({ v: 1, on: run.on, until: run.until || null, seq: run.seq || 0, by: run.by || 'manual', dev: run.dev || null }) };
  }

  setInterval(tick, 1000);
  setInterval(persist, 5000);
  document.addEventListener('visibilitychange', () => { tick(); persist(); });
  window.addEventListener('pagehide', () => { tick(); persist(); });

  root.CardTime = Object.assign({ toggle, command, tick, barHtml, subjHtml, syncMerge, _data: () => data, _run: () => run }, api);
})(typeof window !== 'undefined' ? window : globalThis);
