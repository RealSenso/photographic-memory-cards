/* Command palette (⌘K or /): jump to a subject, topic or card, or run an action, without leaving the keyboard.
   ↑ ↓ to move, Enter to run, Esc to close. Uses the page's own functions (step, toggleDone, switchTopic, openCard, ...). */
(function () {
  'use strict';
  let wrap = null, items = [], sel = 0;

  function actions() {
    const c = deck[idx], card = c && !isPractice(c);
    return [
      { g: 'Actions', l: 'Next card', k: 'J', run: () => step(1) },
      { g: 'Actions', l: 'Previous card', k: 'K', run: () => step(-1) },
      card && { g: 'Actions', l: done.has(c.id) ? 'Unmark as done' : 'Mark as done', k: 'D', run: toggleDone },
      card && { g: 'Actions', l: phys.has(c.id) ? 'Unmark physical card' : 'Mark physical card made', k: 'P', run: togglePhys },
      c && isPractice(c) && { g: 'Actions', l: 'Flip question / solution', k: 'F', run: flipCard },
      window.CardTime && { g: 'Actions', l: CardTime._run().on ? 'Pause card timer' : 'Start card timer', k: 'T', run: () => CardTime.toggle() },
      { g: 'Actions', l: 'Toggle sidebar', k: '[', run: () => setRailCollapsed(!document.querySelector('.app').classList.contains('rail-collapsed')) },
      card && { g: 'Actions', l: 'Copy this card', run: () => copyCard(c.id) },
      { g: 'Actions', l: syncCfg.token ? 'Sync now' : 'Set up sync', run: () => (syncCfg.token ? syncNow() : openSync()) },
      { g: 'Actions', l: 'Print this topic', run: printDeck },
      { g: 'Actions', l: 'New card', run: openAddModal }
    ].filter(Boolean);
  }
  function places() {
    const out = SUBJECTS.map(s => ({ g: 'Subjects', l: s.id, sub: getSubjectCards(s.id).length + ' cards', run: () => switchSubject(s.id) }));
    SUBJECTS.forEach(s => getTopicsList(s.id).forEach(t => out.push({ g: 'Topics', l: t.title, sub: s.id, run: () => { if (currentSubject !== s.id) switchSubject(s.id); switchTopic(t.id); } })));
    return out;
  }
  function cards(q) {
    return masterCards.filter(c => {
      const hay = (stripTags(c.title) + ' ' + (c.subject || 'CMO') + ' ' + (c.topicTitle || '') + ' card ' + c.cardNumber + ' ' + c.id).toLowerCase();
      return q.every(w => hay.includes(w));
    }).slice(0, 30).map(c => ({ g: 'Cards', l: stripTags(c.title), sub: (c.subject || 'CMO') + ' · ' + (c.topicTitle || '') + ' · Card ' + c.cardNumber, run: () => openCard(c.id) }));
  }
  function build(text) {
    const q = text.trim().toLowerCase().split(/\s+/).filter(Boolean);
    if (!q.length) return actions().concat(places().filter(p => p.g === 'Subjects' || p.sub === currentSubject));
    const hit = x => q.every(w => (x.l + ' ' + (x.sub || '')).toLowerCase().includes(w));
    return actions().filter(hit).concat(places().filter(hit).slice(0, 12), cards(q));
  }
  function paint() {
    const list = wrap.querySelector('.cp-list');
    let g = '', i = 0;
    list.innerHTML = items.length ? items.map(x => {
      const head = x.g !== g ? `<div class="cp-g">${esc(x.g)}</div>` : ''; g = x.g;
      return head + `<button class="cp-i ${i === sel ? 'sel' : ''}" data-i="${i++}"><span class="cp-l">${esc(x.l)}</span>${x.sub ? `<span class="cp-sub">${esc(x.sub)}</span>` : ''}${x.k ? `<kbd>${esc(x.k)}</kbd>` : ''}</button>`;
    }).join('') : '<div class="cp-empty">Nothing matches.</div>';
    const s = list.querySelector('.cp-i.sel'); if (s) s.scrollIntoView({ block: 'nearest' });
  }
  function run(i) { const x = items[i]; close(); if (x) x.run(); }
  function close() { if (wrap) { wrap.remove(); wrap = null; } }
  function open() {
    if (wrap) { wrap.querySelector('input').select(); return; }
    wrap = document.createElement('div');
    wrap.className = 'cp-wrap';
    wrap.innerHTML = `<div class="cp" role="dialog" aria-modal="true" aria-label="Command palette">
      <input type="text" placeholder="Search cards, topics and actions…" aria-label="Search cards, topics and actions" autocomplete="off" spellcheck="false">
      <div class="cp-list" role="listbox"></div>
      <div class="cp-foot"><span><kbd>↑</kbd> <kbd>↓</kbd> move</span><span><kbd>↵</kbd> open</span><span><kbd>esc</kbd> close</span></div></div>`;
    document.body.appendChild(wrap);
    const input = wrap.querySelector('input');
    const refresh = () => { items = build(input.value); sel = 0; paint(); };
    input.addEventListener('input', refresh);
    input.addEventListener('keydown', e => {
      if (e.key === 'ArrowDown') { e.preventDefault(); sel = Math.min(items.length - 1, sel + 1); paint(); }
      else if (e.key === 'ArrowUp') { e.preventDefault(); sel = Math.max(0, sel - 1); paint(); }
      else if (e.key === 'Enter') { e.preventDefault(); run(sel); }
      else if (e.key === 'Escape') { e.preventDefault(); close(); }
      e.stopPropagation();
    });
    wrap.addEventListener('click', e => { const b = e.target.closest('.cp-i'); if (b) run(Number(b.dataset.i)); else if (e.target === wrap) close(); });
    wrap.addEventListener('mousemove', e => { const b = e.target.closest('.cp-i'); if (b && Number(b.dataset.i) !== sel) { sel = Number(b.dataset.i); paint(); } });
    refresh();
    input.focus();
  }
  window.CommandPalette = { open, close };
})();
