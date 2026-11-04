/* Study-slot timer: setup dialog, the bar under the top bar, alarms, and the log / confirm-before-marking dialog.
   The clock itself is study_timer_core.js. Everything here is local to this browser: no server, and the sync token is never touched.
   Progress marks are only ever written through applyMarks() in index.html (the same doneTs path as the Done / Physical-card buttons)
   and only after an explicit confirmation. */
(function () {
  'use strict';
  const T = window.StudyTimerCore;
  const KEY = 'plates_timer_v1', PREF = 'plates_timer_prefs_v1', LOGK = 'plates_timer_log_v1';
  const BASE_TITLE = document.title;
  const speedParam = Number(new URLSearchParams(location.search).get('timerSpeed')) || 1;   // testing only: ?timerSpeed=60 makes a minute pass in a second

  /* ---------- storage (every access guarded: private windows and blocked storage must not break the page) ---------- */
  const lsGet = (k, d) => { try { const v = JSON.parse(localStorage.getItem(k)); return v == null ? d : v; } catch (e) { return d; } };
  const lsSet = (k, v) => { try { localStorage.setItem(k, JSON.stringify(v)); return true; } catch (e) { return false; } };
  let memState = null;                          // fallback if storage is blocked: the timer still works until the page closes
  function loadState() {
    let s = rawState();
    if (!s || s.status === 'cleared' || !T.validState(s)) return null;
    const fixed = T.sanitize(s, speedParam, Date.now());         // a speed carried in from another device is ignored
    if (fixed !== s) { s = fixed; saveState(s); }
    return s;
  }
  const rawState = () => lsGet(KEY, null) || memState;
  function saveState(s) { memState = s; if (s) lsSet(KEY, s); else try { localStorage.removeItem(KEY); } catch (e) {} }
  const prefs = Object.assign({ learn: T.defaultMinutes('learn'), make: T.defaultMinutes('make'), vol: 70, muted: false }, lsGet(PREF, {}));
  const savePrefs = () => lsSet(PREF, prefs);

  let st = loadState(), form = null, logForm = null, notice = '', flashUntil = 0, audioBlocked = false, ctx = null, timerId = null, missedNote = '';
  const E = s => esc(s);

  /* ---------- cards: only numbers the user typed are used; nothing is invented ---------- */
  const norm = x => String(x == null ? '' : x).trim().toLowerCase().replace(/^#/, '').replace(/^0+(?=\d)/, '').replace(/[ab]$/, '');
  const parseNums = t => String(t || '').split(/[\s,;]+/).map(x => x.trim().replace(/^#/, '')).filter(Boolean);
  const topicCards = (sub, topic) => masterCards.filter(c => (c.subject || 'CMO') === sub && topicOf(c) === topic && !isPractice(c));
  const findCard = (sub, topic, num) => topicCards(sub, topic).find(c => norm(c.cardNumber) === norm(num)) || null;
  const topicTitle = (sub, topic) => { const t = window.getTopicsList(sub).find(x => x.id === topic); return t ? t.title : ''; };
  const plain = s => String(s || '').replace(/<\/?[^>]+(>|$)/g, '').replace(/\$/g, '');
  const hashes = list => list.filter(Boolean).map(n => '#' + n).join(' ');

  /* ---------- sound, vibration, notification ---------- */
  function unlockAudio() {
    try {
      if (!ctx) { const A = window.AudioContext || window.webkitAudioContext; if (!A) return; ctx = new A(); }
      if (ctx.state === 'suspended') ctx.resume().then(() => { audioBlocked = ctx.state !== 'running'; render(); }).catch(() => {});
      else audioBlocked = false;
    } catch (e) {}
  }
  ['pointerdown', 'keydown'].forEach(ev => document.addEventListener(ev, () => { if (st && (ctx == null || ctx.state !== 'running')) unlockAudio(); }, true));
  function beeps(freqs, vol) {
    if (!ctx) return;
    const g = ctx.createGain(); g.gain.value = 0; g.connect(ctx.destination);
    let t = ctx.currentTime + 0.02;
    freqs.forEach(f => {
      const o = ctx.createOscillator(); o.type = 'sine'; o.frequency.value = f; o.connect(g);
      g.gain.setValueAtTime(0, t); g.gain.linearRampToValueAtTime(vol, t + 0.02); g.gain.setValueAtTime(vol, t + 0.2); g.gain.linearRampToValueAtTime(0, t + 0.26);
      o.start(t); o.stop(t + 0.28); t += 0.38;
    });
  }
  function playSound(kind) {
    if (prefs.muted || prefs.vol <= 0) return;
    unlockAudio();
    if (!ctx || ctx.state !== 'running') { audioBlocked = true; return; }
    const vol = Math.min(0.5, prefs.vol / 100 * 0.4);
    beeps(kind === 'final' ? [660, 520, 440] : kind === 'focusEnd' ? [523, 659, 784] : [880, 880], vol);
  }
  const notifState = () => !('Notification' in window) ? 'unsupported' : Notification.permission;      // 'default' | 'granted' | 'denied'
  function notify(text, tag) {
    if (notifState() !== 'granted' || !(document.hidden || !document.hasFocus())) return;
    try { new Notification('Study timer', { body: text, tag, silent: !!prefs.muted }); } catch (e) { /* some mobile browsers only allow this from a service worker */ }
  }
  function fire(alert, missed) {
    missedNote = missed.length ? missed.length + ' earlier cue' + (missed.length > 1 ? 's' : '') + ' passed while this page was away.' : '';
    flashUntil = Date.now() + 8000;
    playSound(alert.kind);
    if (!prefs.muted && navigator.vibrate) try { navigator.vibrate([200, 100, 200]); } catch (e) {}
    notify(alert.text, 'plates-timer-' + st.id + '-' + alert.index);
  }

  /* ---------- the loop: read the stored state, let the core decide what is due, store, alarm once ---------- */
  function tick() {
    const cur = loadState();
    if (!cur) { if (st) { st = null; render(); } return; }
    const r = T.tick(cur, Date.now());
    if (r.state !== cur) { saveState(r.state); syncSoon(); }
    st = r.state;
    if (r.alert) fire(r.alert, r.missed);
    render();
  }
  function ensureLoop() {
    if (st && !timerId) timerId = setInterval(tick, 500);
    if (!st && timerId) { clearInterval(timerId); timerId = null; }
  }
  ['visibilitychange', 'focus', 'pageshow', 'online'].forEach(ev => (ev === 'visibilitychange' ? document : window).addEventListener(ev, () => { if (st) tick(); }));
  window.addEventListener('storage', e => { if (e.key === KEY) { st = loadState(); ensureLoop(); render(); } });

  /* ---------- controls ---------- */
  const mutate = f => { const cur = loadState(); if (!cur) return; saveState(f(cur)); st = loadState(); syncSoon(); tick(); };
  const clearSlot = () => { saveState(T.cleared(st, Date.now())); st = null; ensureLoop(); render(); syncSoon(); };
  function pause() { mutate(s => T.pause(s, Date.now())); }
  function resume() { unlockAudio(); mutate(s => T.resume(s, Date.now())); }
  function skip() { mutate(s => T.skip(s, Date.now())); }
  function stay() { mutate(s => T.extend(s, Date.now(), 120)); }
  function setMute(m) { prefs.muted = !!m; savePrefs(); render(); if (form) renderSetup(); }
  function setVol(v) { prefs.vol = Math.max(0, Math.min(100, Number(v) || 0)); savePrefs(); }
  function testSound() {
    if (prefs.muted) { notice = 'Muted: untick Mute to hear the test.'; return renderSetup(); }
    unlockAudio(); audioBlocked = false;
    setTimeout(() => { playSound('phase'); notice = ctx && ctx.state === 'running' ? '' : 'This browser is blocking sound until you tap the page. Tap once more.'; renderSetup(); }, 80);
  }
  function endEarly() { confirmBox('End this slot now?', 'The clock stops. You can then log what you actually did.', [['End and log progress', () => { saveState(T.end(st, Date.now())); st = loadState(); syncSoon(); closeBox(); render(); openLog(); }], ['End without logging', () => { closeBox(); clearSlot(); }], ['Keep going', closeBox]]); }
  function dismiss() { clearSlot(); }
  function beginPlanned() { unlockAudio(); mutate(s => T.begin(s, Date.now())); }

  /* ---------- small dialogs ---------- */
  function modal(html) {
    let m = document.getElementById('timer-modal');
    if (!m) { m = document.createElement('div'); m.id = 'timer-modal'; document.body.appendChild(m); }
    m.innerHTML = html ? `<div class="tm-wrap" onclick="if(event.target===this)StudyTimer.closeAll()"><div class="tm-box" role="dialog" aria-modal="true">${html}</div></div>` : '';
  }
  function closeBox() { const b = document.getElementById('timer-confirm'); if (b) b.remove(); }
  function confirmBox(title, text, buttons) {
    closeBox();
    const el = document.createElement('div'); el.id = 'timer-confirm'; el.className = 'tm-wrap tm-top';
    el.innerHTML = `<div class="tm-box" role="alertdialog"><h3>${E(title)}</h3><p>${text}</p><div class="tm-row">${buttons.map((b, i) => `<button class="btn ${i === 0 ? 'primary' : ''}" data-i="${i}">${E(b[0])}</button>`).join('')}</div></div>`;
    el.addEventListener('click', e => { const b = e.target.closest('button[data-i]'); if (b) buttons[b.dataset.i][1](); else if (e.target === el) closeBox(); });
    document.body.appendChild(el);
  }
  function closeAll() { closeBox(); modal(''); form = null; }
  document.addEventListener('keydown', e => { if (e.key === 'Escape' && document.getElementById('timer-modal') && document.getElementById('timer-modal').innerHTML) { e.stopPropagation(); closeBox(); if (!document.getElementById('timer-confirm')) closeAll(); } }, true);

  /* ---------- setup ---------- */
  function openSetup() {
    const sub = currentSubject, topic = currentTopic || (window.getTopicsList(sub)[0] || {}).id;
    const last = lsGet(PREF + '_plan', {}) || {};
    form = { mode: (st && st.mode) || last.mode || 'learn', subject: sub, topic, recap: '', cards: ['', '', '', '', ''], make: '', tab: '' };
    notice = ''; renderSetup();
  }
  function renderSetup() {
    if (!form) return;
    const active = busy();
    const mode = form.mode, sched = T.buildSchedule(mode, prefs[mode]), cardsHere = topicCards(form.subject, form.topic);
    const madeHere = cardsHere.filter(c => phys.has(c.id));
    const chk = n => { const c = findCard(form.subject, form.topic, n); return c ? `<span class="ok">#${E(n)} ${E(plain(c.title)).slice(0, 48)}</span>` : `<span class="bad">#${E(n)} not found in this topic</span>`; };
    const learnNums = [...new Set([form.recap, ...form.cards].flatMap(parseNums).map(norm))];
    const ns = notifState();
    const nTxt = { unsupported: 'Not supported in this browser. You still get the in-page banner and sound.', default: 'Not enabled. Sound and the in-page banner still work.', granted: 'Enabled. Shown only when this tab is in the background and still running.', denied: 'Blocked in the browser settings for this site. The timer still works with the banner and sound; re-allow it in the site settings if you want notifications.' }[ns];
    const logs = lsGet(LOGK, []).slice(-3).reverse();
    modal(`
      <h3>Study slot timer</h3>
      <div class="tm-seg" role="group" aria-label="Mode">
        <button class="${mode === 'learn' ? 'on' : ''}" onclick="StudyTimer.setField('mode','learn')">Learn</button>
        <button class="${mode === 'make' ? 'on' : ''}" onclick="StudyTimer.setField('mode','make')">Revise + Make</button>
      </div>
      <p class="tm-small">${mode === 'learn' ? 'Five cards is a trial target, not a quota. Cues are pacing nudges: stay on a card as long as you need.' : 'A timebox after a sub-topic is learned. Not every card has to be finished.'}</p>
      <div class="tm-grid2">
        <label>Subject<select onchange="StudyTimer.setField('subject',this.value)">${SUBJECTS.map(s => `<option value="${s.id}" ${s.id === form.subject ? 'selected' : ''}>${s.id}</option>`).join('')}</select></label>
        <label>Topic<select onchange="StudyTimer.setField('topic',this.value)">${window.getTopicsList(form.subject).map(t => `<option value="${E(t.id)}" ${t.id === form.topic ? 'selected' : ''}>${E(t.title)}</option>`).join('')}</select></label>
      </div>
      ${mode === 'learn' ? `
        <label>Recap: this slot's prerequisite card numbers <input value="${E(form.recap)}" placeholder="physical-card numbers, e.g. 03, 04" oninput="StudyTimer.setField('recap',this.value,1)"></label>
        <div class="tm-cards">${form.cards.map((c, i) => `<label>Card ${i + 1}<input value="${E(c)}" placeholder="no." oninput="StudyTimer.setCard(${i},this.value)"></label>`).join('')}</div>
        <div class="tm-small">${learnNums.length ? learnNums.map(chk).join(' · ') : 'Type the card numbers you plan to cover. Nothing is filled in for you; leave boxes empty for fewer cards.'}</div>
        <button class="btn" onclick="StudyTimer.suggest()">Suggest the next unfinished cards in this topic</button>`
      : `
        <label>Cards to make (numbers) <input value="${E(form.make)}" placeholder="e.g. 03, 04, 05" oninput="StudyTimer.setField('make',this.value,1)"></label>
        <div class="tm-small">${madeHere.length ? 'Already made, will not be remade: ' + E(hashes(madeHere.map(c => c.cardNumber))) : 'No physical card marked as made in this topic yet.'}</div>
        <button class="btn" onclick="StudyTimer.suggest()">Suggest: done but no physical card yet</button>`}
      <details class="tm-det"><summary>Phase lengths (minutes) · total ${sched.total / 60}</summary>
        <div class="tm-lens">${sched.phases.map((p, i) => `<label>${E(p.label)}<input type="number" min="1" max="180" step="1" value="${p.min}" onchange="StudyTimer.setLen(${i},this.value)"></label>`).join('')}</div>
        <button class="btn" onclick="StudyTimer.resetLens()">Reset to ${mode === 'learn' ? '2 / 8×5 / 8 / 10' : '10 / 35 / 5 / 10'}</button>
      </details>
      <div class="tm-sound">
        <label class="tm-inl"><input type="checkbox" ${prefs.muted ? 'checked' : ''} onchange="StudyTimer.setMute(this.checked)"> Mute</label>
        <label class="tm-inl">Volume <input type="range" min="0" max="100" value="${prefs.vol}" oninput="StudyTimer.setVol(this.value)"></label>
        <button class="btn" onclick="StudyTimer.testSound()">Test sound</button>
      </div>
      <div class="tm-small"><b>Notifications:</b> ${nTxt} ${ns === 'default' ? '<button class="btn" onclick="StudyTimer.enableNotif()">Enable notifications</button>' : ''}</div>
      <details class="tm-det"><summary>What works when the phone is locked or the tab is in the background</summary>
        <p class="tm-small">This is a web page, not an alarm app. Alarms only sound while this page is allowed to run. Browsers slow down background tabs, and a locked phone, a discarded tab or a closed browser stops the page completely, so no cue sounds then. I cannot promise otherwise.</p>
        <p class="tm-small">What is reliable: the time is worked out from the clock, not counted. When you open the page again the right phase and countdown are shown, and you get one alarm for the latest cue you missed, with the earlier ones listed silently. A refresh keeps the slot.</p>
        <p class="tm-small">For alarms you cannot miss, keep this tab open with the screen on, or set a phone alarm as a backup. While a slot runs, the bar lists the clock time of every cue to copy into one.</p>
      </details>
      ${active ? `<details class="tm-det"><summary>Cue clock times (for a backup phone alarm)</summary><pre class="tm-pre">${E(cueTimes()) || 'Resume the slot to see them.'}</pre></details>` : ''}
      ${notice ? `<p class="tm-warn">${E(notice)}</p>` : ''}
      ${logs.length ? `<p class="tm-small"><b>Recent slots:</b> ${logs.map(l => E(new Date(l.ts).toLocaleDateString() + ' ' + (T.MODE_LABEL[l.mode] || l.mode) + ' · ' + l.summary)).join(' | ')}</p>` : ''}
      <div class="tm-row tm-actions">
        ${active ? '<span class="tm-small">A slot is already running; end it to start another.</span>' : '<button class="btn primary" onclick="StudyTimer.start()">Start</button>'}
        <button class="btn" onclick="StudyTimer.closeAll()">Close</button>
      </div>`);
  }
  function setField(k, v, quiet) {
    if (!form) return;
    form[k] = v;
    if (k === 'subject') form.topic = (window.getTopicsList(v)[0] || {}).id;
    if (k === 'subject' || k === 'topic' || k === 'mode') { form.recap = ''; form.cards = ['', '', '', '', '']; form.make = ''; }
    if (!quiet) renderSetup();
  }
  function setCard(i, v) { form.cards[i] = v; }
  function setLen(i, v) { const a = prefs[form.mode].slice(); a[i] = v; prefs[form.mode] = T.cleanMinutes(form.mode, a); savePrefs(); renderSetup(); }
  function resetLens() { prefs[form.mode] = T.defaultMinutes(form.mode); savePrefs(); renderSetup(); }
  function suggest() {
    const cs = topicCards(form.subject, form.topic);
    if (form.mode === 'learn') { form.cards = cs.filter(c => !done.has(c.id)).slice(0, 5).map(c => String(c.cardNumber)).concat(['', '', '', '', '']).slice(0, 5); }
    else form.make = cs.filter(c => done.has(c.id) && !phys.has(c.id)).map(c => c.cardNumber).join(', ');
    renderSetup();
  }
  async function enableNotif() {
    if (!('Notification' in window)) { notice = 'Notifications are not supported in this browser.'; return renderSetup(); }
    try { await Notification.requestPermission(); } catch (e) { notice = 'The browser did not show the permission prompt.'; }
    renderSetup();
  }
  /* One builder for the dialog and for outside callers (e.g. an assistant adding slots through StudyTimer.addSlot). Only the numbers given are used. */
  function buildSlot(spec, planned) {
    spec = spec || {};
    const mode = spec.mode === 'make' ? 'make' : 'learn', list = x => Array.isArray(x) ? x.map(String) : parseNums(x);
    if (!SUBJECTS.some(x => x.id === spec.subject)) return { error: 'Unknown subject: ' + spec.subject };
    if (!getTopicsList(spec.subject).some(t => t.id === spec.topic)) return { error: 'Unknown topic for ' + spec.subject + ': ' + spec.topic };
    const plan = { subject: spec.subject, topic: spec.topic, topicTitle: topicTitle(spec.subject, spec.topic), mode };
    if (mode === 'learn') { plan.recap = list(spec.recap); plan.cards = [0, 1, 2, 3, 4].map(i => list(spec.cards)[i] || ''); }
    else {
      const asked = list(spec.make), dup = asked.filter(n => { const c = findCard(spec.subject, spec.topic, n); return c && phys.has(c.id); });
      plan.cards = asked.filter(n => !dup.includes(n)); plan.skippedMade = dup;
    }
    return { state: T.newState(mode, spec.minutes || prefs[mode], plan, Date.now(), { planned }) };
  }
  const busy = () => st && (st.status === 'running' || st.status === 'paused' || st.status === 'planned');
  function addSlot(spec) {   // always lands as 'planned': the clock only ever starts from a tap on Start
    if (busy()) return { error: 'A slot is already running or waiting; close it first.' };
    const r = buildSlot(spec, true);
    if (r.error) return r;
    saveState(r.state); st = loadState(); missedNote = ''; ensureLoop(); render(); syncSoon();
    return { ok: true, id: r.state.id, status: r.state.status };
  }
  function start() {
    if (!form || busy()) return;
    const r = buildSlot({ mode: form.mode, subject: form.subject, topic: form.topic, recap: form.recap, cards: form.cards, make: form.make }, false);
    if (r.error) { notice = r.error; return renderSetup(); }
    unlockAudio();
    saveState(r.state);
    lsSet(PREF + '_plan', { mode: form.mode });
    st = loadState(); form = null; modal(''); notice = ''; missedNote = ''; ensureLoop(); render(); syncSoon();
  }

  /* ---------- log + confirm-before-marking ---------- */
  function planCards() {
    const p = st.plan, nums = st.mode === 'learn' ? p.cards.filter(Boolean) : p.cards;
    return nums.map(n => ({ n, card: findCard(p.subject, p.topic, n) }));
  }
  function openLog() {
    if (!st) return;
    if (!logForm || logForm.slot !== st.id) logForm = { slot: st.id, status: {}, made: {}, note: '' };
    renderLog();
  }
  function renderLog() {
    const learn = st.mode === 'learn', rows = planCards();
    const doneSel = (i, row) => learn
      ? `<select onchange="StudyTimer.logSet('status',${i},this.value)">${[['none', 'Not reached'], ['unclear', 'Still unclear'], ['ok', 'Understood']].map(([v, l]) => `<option value="${v}" ${(logForm.status[i] || 'none') === v ? 'selected' : ''}>${l}</option>`).join('')}</select>`
      : row.card && phys.has(row.card.id) ? '<span class="tm-small">already made</span>'
        : `<label class="tm-inl"><input type="checkbox" ${logForm.made[i] ? 'checked' : ''} onchange="StudyTimer.logSet('made',${i},this.checked)"> Made</label>`;
    modal(`
      <h3>${learn ? 'Log actual progress' : 'Record what was made'}</h3>
      <p class="tm-small">${learn ? 'Planned cards are only a target. Mark what you actually understood.' : 'Record what was made and what remains. Cards already made are not remade.'}</p>
      ${rows.length ? rows.map((r, i) => `<div class="tm-log"><span><b>#${E(r.n)}</b> ${r.card ? E(plain(r.card.title)).slice(0, 56) : '<i>no matching card</i>'}${r.card && (learn ? done.has(r.card.id) : phys.has(r.card.id)) ? ' · <span class="ok">' + (learn ? 'already done' : 'already made') + '</span>' : ''}</span>
          <span>${r.card ? `<button class="btn tm-sm" onclick="StudyTimer.openCard(${r.card.id})">Open</button>` : ''} ${doneSel(i, r)}</span></div>`).join('')
        : '<p class="tm-small">No card numbers were set for this slot.</p>'}
      <label>Note <textarea rows="2" oninput="StudyTimer.logSet('note',0,this.value)" placeholder="${learn ? 'what is still unclear' : 'what remains to make'}">${E(logForm.note)}</textarea></label>
      <div class="tm-small">Saving the log never marks anything. Marking is a separate step that asks you to confirm.</div>
      <div class="tm-row">
        <button class="btn primary" onclick="StudyTimer.saveLog()">Save log</button>
        <button class="btn" onclick="StudyTimer.askMark()">${learn ? 'Mark understood cards as Done…' : 'Mark made cards as physical-card made…'}</button>
        <button class="btn" onclick="StudyTimer.closeAll()">Close</button>
      </div>`);
  }
  function logSet(k, i, v) { if (k === 'note') logForm.note = v; else logForm[k][i] = v; if (k !== 'note') renderLog(); }
  function openCardAndKeep(id) { modal(''); window.openCard(id); }
  function pending() {                                                // [{n, card}] the user ticked and that are not already marked
    const learn = st.mode === 'learn';
    return planCards().map((r, i) => ({ r, i })).filter(x => x.r.card && (learn ? logForm.status[x.i] === 'ok' && !done.has(x.r.card.id) : logForm.made[x.i] && !phys.has(x.r.card.id))).map(x => x.r);
  }
  function askMark() {
    const list = pending(), learn = st.mode === 'learn';
    if (!list.length) return confirmBox('Nothing to mark', learn ? 'No card is set to "Understood" (or they are already done).' : 'No new card is ticked as made (or they are already marked).', [['OK', closeBox]]);
    confirmBox(`Mark ${list.length} card${list.length > 1 ? 's' : ''} as ${learn ? 'Done' : 'physical card made'}?`,
      `${E(hashes(list.map(r => r.n)))}<br>This uses the normal progress marks and syncs like them. You can undo each one from its card.`,
      [['Confirm and mark', () => { const n = applyMarks(learn ? 'done' : 'phys', list.map(r => r.card.id)); closeBox(); showToast(n + ' card' + (n === 1 ? '' : 's') + ' marked'); renderLog(); }], ['Cancel', closeBox]]);
  }
  function saveLog() {
    const learn = st.mode === 'learn', rows = planCards();
    const lab = i => learn ? (logForm.status[i] || 'none') : (logForm.made[i] || (rows[i].card && phys.has(rows[i].card.id)) ? 'made' : 'remaining');
    const entry = { ts: Date.now(), mode: st.mode, subject: st.plan.subject, topic: st.plan.topic, planned: rows.map(r => r.n), actual: rows.map((r, i) => [r.n, lab(i)]), note: logForm.note, endedEarly: st.status === 'ended' };
    const cnt = k => entry.actual.filter(a => a[1] === k).length;
    entry.summary = learn ? `${cnt('ok')} understood, ${cnt('unclear')} unclear, ${cnt('none')} not reached` : `${cnt('made')} made, ${cnt('remaining')} remaining`;
    const all = lsGet(LOGK, []); all.push(entry); lsSet(LOGK, all.slice(-200));
    logForm = null; modal('');
    if (st.status === 'ended') dismiss(); else { saveState(Object.assign({}, st, { logged: true, upd: Date.now() })); st = loadState(); syncSoon(); render(); }
    showToast('Slot log saved');
  }

  /* ---------- the bar ---------- */
  function phaseLabel(sched, i) {
    const p = sched.phases[i], plan = st.plan || {}, num = k => (plan.cards && plan.cards[k] ? ' · #' + plan.cards[k] : '');
    if (st.mode === 'learn') {
      if (p.id === 'recap') return 'Recap' + (plan.recap && plan.recap.length ? ' · ' + hashes(plan.recap) : '');
      if (/^c\d$/.test(p.id)) return 'Card ' + p.id.slice(1) + num(Number(p.id.slice(1)) - 1);
      return p.isBreak ? 'Break' : 'Revisit and log';
    }
    if (p.id === 'make') return 'Make cards' + (plan.cards && plan.cards.length ? ' · ' + hashes(plan.cards) : '');
    return p.isBreak ? 'Break' : p.id === 'revise' ? 'Revise' : 'Check and record';
  }
  function barEl() {
    let b = document.getElementById('timer-bar');
    if (!b) { b = document.createElement('div'); b.id = 'timer-bar'; const strip = document.getElementById('card-strip'); strip.parentNode.insertBefore(b, strip); }
    return b;
  }
  let lastBarKey = '';
  function render() {
    ensureLoop();
    const btn = document.getElementById('timer-btn'), bar = barEl(), now = Date.now();
    if (!st) { bar.hidden = true; bar.innerHTML = ''; lastBarKey = ''; if (btn) btn.textContent = 'Timer'; if (document.title !== BASE_TITLE) document.title = BASE_TITLE; refit(false); return; }
    const sched = T.buildSchedule(st.mode, st.minutes), pos = T.position(st, now), i = T.phaseIndex(sched, pos), n = sched.phases.length;
    const over = st.status === 'finished' || i >= n, ended = st.status === 'ended', paused = st.status === 'paused', planned = st.status === 'planned', idle = over || ended || planned;
    const cur = sched.phases[Math.min(i, n - 1)], left = over ? 0 : cur.end - pos, tag = over ? 'Finished' : ended ? 'Ended' : paused ? 'Paused' : planned ? 'Ready · ' + T.MODE_LABEL[st.mode] : T.MODE_LABEL[st.mode];
    const nextTxt = planned ? 'Added for you. The clock starts only when you tap Start.' : over || ended ? '' : i + 1 < n ? `Next cue: ${E(phaseLabel(sched, i + 1))}` : 'Next cue: end of break';
    const cue = st.lastCue && (now - st.lastCue.firedAt < 60000 || over) ? st.lastCue.text : '';
    const base = (st.plan.topicTitle || '').replace(/^\d+_/, '').replace(/_/g, ' ');
    const key = [st.id, st.status, i, ended, over, flashUntil > now, audioBlocked, prefs.muted, cue, missedNote].join('|');
    const clock = over ? '–' : T.fmt(left);
    if (btn) btn.textContent = ended ? 'Timer · ended' : over ? 'Timer · done' : '⏱ ' + clock;
    document.title = (planned ? 'Ready' : over ? 'Slot complete' : clock + ' · ' + phaseLabel(sched, Math.min(i, n - 1))) + ' · ' + BASE_TITLE;
    if (key !== lastBarKey || !bar.firstChild) {
      lastBarKey = key; bar.hidden = false;
      bar.className = flashUntil > now ? 'flash' : '';
      bar.innerHTML = `
        <span class="tb-tag ${paused ? 'p' : over ? 'f' : ''}">${E(tag)}</span>
        <span class="tb-phase" title="${E(base)}">${E(over ? 'Slot complete' : phaseLabel(sched, i))}<small>${E(base)}</small></span>
        <span class="tb-clock" id="tb-clock" aria-live="off">${clock}</span>
        <span class="tb-next">${nextTxt}</span>
        <span class="tb-ctl">
          ${planned ? '<button class="btn primary" onclick="StudyTimer.beginPlanned()">Start</button><button class="btn" onclick="StudyTimer.dismiss()">Discard</button>' : over || ended ? '' : paused ? '<button class="btn" onclick="StudyTimer.resume()">Resume</button>' : '<button class="btn" onclick="StudyTimer.pause()">Pause</button>'}
          ${idle ? '' : '<button class="btn tm-sm" onclick="StudyTimer.skip()" title="Move to the next phase now">Next phase</button><button class="btn tm-sm" onclick="StudyTimer.stay()" title="Stay longer on this phase">+2 min</button>'}
          ${planned ? '' : '<button class="btn tm-sm" onclick="StudyTimer.openLog()">Log progress</button>'}
          ${planned ? '' : over || ended ? '<button class="btn" onclick="StudyTimer.dismiss()">Close</button><button class="btn primary" onclick="StudyTimer.openSetup()">New slot</button>' : '<button class="btn tm-sm" onclick="StudyTimer.endEarly()">End early</button>'}
          <button class="btn tm-sm" onclick="StudyTimer.setMute(${!prefs.muted})" aria-pressed="${prefs.muted}" title="${prefs.muted ? 'Unmute' : 'Mute'}">${prefs.muted ? '🔇' : '🔊'}</button>
          <input class="tb-vol" type="range" min="0" max="100" value="${prefs.vol}" oninput="StudyTimer.setVol(this.value)" aria-label="Volume">
          <button class="btn tm-sm" onclick="StudyTimer.openSetup()" title="Settings and cue times">⚙</button>
        </span>
        ${cue || missedNote || audioBlocked ? `<span class="tb-cue">${cue ? '<b>' + E(cue) + '</b> ' : ''}${E(missedNote)}${audioBlocked && !prefs.muted ? ' Sound is blocked until you tap the page once.' : ''}</span>` : ''}`;
      refit(true);
    } else { const c = document.getElementById('tb-clock'); if (c) c.textContent = clock; const nx = bar.querySelector('.tb-next'); if (nx) nx.innerHTML = nextTxt; }
  }
  let barShown = false;
  function refit(on) { if (on === barShown) return; barShown = on; if (typeof window.fitCard === 'function') setTimeout(window.fitCard, 0); }

  /* backup phone-alarm times, shown in the settings dialog while a slot runs */
  function cueTimes() {
    const c = st && T.cueClock(st, Date.now());
    return c ? c.filter(x => !x.fired).map(x => new Date(x.at).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }) + '  ' + x.text).join('\n') : '';
  }

  /* ---- cross-device sync: index.html's syncNow hands over the remote copy and stores what this returns in the same private gist ---- */
  const canon = v => JSON.stringify(v, (k, x) => x && typeof x === 'object' && !Array.isArray(x) ? Object.keys(x).sort().reduce((o, key) => (o[key] = x[key], o), {}) : x);
  function syncMerge(remote) {
    remote = remote && typeof remote === 'object' ? remote : {};
    const local = rawState(), rt = validRemote(remote.timer) ? T.sanitize(remote.timer, speedParam, Date.now()) : null, merged = T.merge(local, rt);
    if (merged && canon(merged) !== canon(local)) { saveState(merged); st = loadState(); ensureLoop(); if (st) tick(); else render(); }
    const logs = T.mergeLogs(lsGet(LOGK, []), remote.logs);
    if (canon(logs) !== canon(lsGet(LOGK, []))) lsSet(LOGK, logs);
    const payload = { v: 1, timer: merged || null, logs };
    return { content: JSON.stringify(payload), push: canon(payload) !== canon({ v: 1, timer: validRemote(remote.timer), logs: remote.logs || [] }) };
  }
  const validRemote = t => T.validState(t) ? t : null;
  /* while a slot is open, look for changes made on another device every 15 s (the normal sync poll is 45 s) */
  setInterval(() => { if (st && !document.hidden && typeof syncCfg !== 'undefined' && syncCfg.token) syncNow(); }, 15000);

  /* ---------- boot ---------- */
  function boot() {
    const sb = document.getElementById('sync-btn');
    if (sb && !document.getElementById('timer-btn')) { const b = document.createElement('button'); b.className = 'btn'; b.id = 'timer-btn'; b.textContent = 'Timer'; b.onclick = openSetup; sb.parentNode.insertBefore(b, sb); }
    if (st) { tick(); } else render();
  }
  window.StudyTimer = { addSlot, beginPlanned, syncMerge, openSetup, closeAll, setField, setCard, setLen, resetLens, suggest, enableNotif, start, pause, resume, skip, stay, endEarly, dismiss, setMute, setVol, testSound,
    openLog, logSet, saveLog, askMark, openCard: openCardAndKeep, tick, cueTimes, _state: () => st };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot); else boot();
})();
