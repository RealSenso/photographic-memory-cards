/* Card study time: how long each card has been open while the timer is playing.
   Time counts only for the card on screen, only while this page is visible, and only while Play is on. Switching card stops the old card's
   count and starts the new one's. A beep sounds every 10 minutes of playing time.
   Totals sync through the same private gist as progress, as a per-device counter (each device only ever raises its own numbers, merging takes the
   larger value per device and card), so two devices never double-count or erase each other. */
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
  const api = { merge, ahead, total, fmtClock, fmtShort };
  if (typeof module !== 'undefined' && module.exports) { module.exports = api; return; }

  /* ---------- page ---------- */
  const lsGet = (k, d) => { try { const v = JSON.parse(localStorage.getItem(k)); return v == null ? d : v; } catch (e) { return d; } };
  const lsSet = (k, v) => { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} };
  let data = lsGet(KEY, null);
  if (!data || !data.dev || !data.c) data = { dev: Math.random().toString(36).slice(2, 10), c: {} };
  data.c[data.dev] = data.c[data.dev] || {};
  let run = Object.assign({ on: false, ms: 0 }, lsGet(RUN, {}));
  let curKey = null, last = Date.now(), dirty = false, ctx = null;
  ['plates_timer_v1', 'plates_timer_prefs_v1', 'plates_timer_prefs_v1_plan'].forEach(k => { try { localStorage.removeItem(k); } catch (e) {} });   // the old slot timer

  /* card id for explanation cards (split halves share it); subject/topic/number for practice questions */
  function keyOf(c) {
    if (!c) return null;
    return c.kind === 'practice' ? 'p:' + c.subject + ':' + c.topicId + ':' + c.cardNumber : c.id != null ? String(c.id) : null;
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
    if (run.on && !document.hidden && curKey) {
      const mine = data.c[data.dev];
      mine[curKey] = (mine[curKey] || 0) + dt;
      const before = run.ms; run.ms += dt; dirty = true;
      if (Math.floor(run.ms / BEEP_EVERY) > Math.floor(before / BEEP_EVERY)) beep();
    }
    curKey = keyOf(visibleCard());
    paint();
  }
  function persist() { if (!dirty) return; lsSet(KEY, data); lsSet(RUN, run); dirty = false; }

  function paint() {
    const t = document.getElementById('ctime');
    if (t) t.textContent = fmtClock(curKey ? total(data.c, curKey) : 0);
    const b = document.getElementById('ctime-btn');
    if (b) { b.textContent = run.on ? '❚❚' : '▶'; b.setAttribute('aria-label', run.on ? 'Pause card timer' : 'Start card timer'); b.classList.toggle('on', run.on); }
    document.querySelectorAll('.stime[data-s]').forEach(el => { const v = subjectTotal(el.dataset.s); el.textContent = v ? fmtShort(v) : ''; });
  }

  function toggle() { tick(); run.on = !run.on; dirty = true; if (run.on) unlock(); persist(); paint(); }
  function barHtml(card) {
    const k = keyOf(card);
    return `<span class="ctime-wrap"><button class="ctime-btn ${run.on ? 'on' : ''}" id="ctime-btn" onclick="CardTime.toggle()" aria-label="${run.on ? 'Pause' : 'Start'} card timer" title="Play / pause the card timer (T)">${run.on ? '❚❚' : '▶'}</button><span class="ctime" id="ctime" title="Time this card has been open with the timer playing">${fmtClock(k ? total(data.c, k) : 0)}</span></span>`;
  }
  const subjHtml = sub => { const v = subjectTotal(sub); return `<span class="stime" data-s="${sub}" title="Total card time in ${sub}">${v ? fmtShort(v) : ''}</span>`; };

  /* sync: index.html's syncNow passes the gist copy and stores what this returns */
  function syncMerge(remote) {
    const rc = remote && remote.c && typeof remote.c === 'object' ? remote.c : {};
    const merged = merge(data.c, rc);
    if (ahead(rc, data.c)) { data.c = merged; data.c[data.dev] = data.c[data.dev] || {}; lsSet(KEY, data); paint(); }
    return { push: ahead(data.c, rc), content: JSON.stringify({ v: 1, c: merge(data.c, rc) }) };
  }

  setInterval(tick, 1000);
  setInterval(persist, 5000);
  document.addEventListener('visibilitychange', () => { tick(); persist(); });
  window.addEventListener('pagehide', () => { tick(); persist(); });

  root.CardTime = Object.assign({ toggle, tick, barHtml, subjHtml, syncMerge, _data: () => data, _run: () => run }, api);
})(typeof window !== 'undefined' ? window : globalThis);
