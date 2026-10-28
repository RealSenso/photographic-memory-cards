import re

with open('/Users/senso/Projects/photographic-memory-cards/index.html', 'r') as f:
    html = f.read()

# 1. Add <script src="cards_data.js"></script> in <head>
if 'src="cards_data.js"' not in html:
    html = html.replace('<!-- KaTeX for mathematical equations -->', '<script src="cards_data.js"></script>\n  <!-- KaTeX for mathematical equations -->')

# 2. Update Header: Add Topic Selector and Subject Badge
old_search_block = """        <!-- Search Input -->
        <div class="flex-1 max-w-md">
          <div class="relative">
            <input type="text" id="search-input" oninput="filterCards()" placeholder="Search concepts, math equations, or analogies..." class="w-full bg-[#0d1326] border border-slate-700/80 rounded-xl py-2 pl-9 pr-3 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-cyan-400 focus:ring-1 focus:ring-cyan-400 transition">
            <span class="absolute left-3 top-2.5 text-xs text-cyan-400 opacity-75">🔍</span>
          </div>
        </div>"""

new_search_and_nav = """        <!-- Subject & Topic Selector Bar -->
        <div class="flex flex-wrap items-center gap-2.5 flex-1 max-w-2xl">
          <!-- Subject Badge -->
          <div class="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-cyan-950/80 border border-cyan-500/30 text-cyan-300 font-mono text-xs font-bold shrink-0">
            <span>📚</span> CMO (E0 230)
          </div>

          <!-- Topic Dropdown -->
          <div class="flex items-center gap-1.5 bg-[#0d1326] border border-cyan-500/30 px-3 py-1.5 rounded-xl text-xs text-slate-200 flex-1 min-w-[280px]">
            <span class="text-[10px] text-cyan-400 font-mono font-bold shrink-0">TOPIC:</span>
            <select id="topic-select" onchange="switchTopic(this.value)" class="w-full bg-[#080c18] border border-cyan-500/40 rounded-lg py-1 px-2 text-xs text-white focus:outline-none focus:border-cyan-400 cursor-pointer">
              <option value="01_Mathematical_Preliminaries_Topology_and_Weierstrass">Topic 01 · Preliminaries & Weierstrass (6 cards)</option>
              <option value="02_Multivariate_Taylor_Series_and_Optimality_Conditions">Topic 02 · Taylor Series & Optimality (6 cards)</option>
              <option value="03_Convexity_and_Strong_Convexity">Topic 03 · Convexity & Strong Convexity (6 cards)</option>
              <option value="04_Line_Search_Methods_Exact_Armijo_and_Wolfe">Topic 04 · Line Search: Armijo & Wolfe (6 cards)</option>
              <option value="05_Gradient_Descent_and_Convergence_Analysis">Topic 05 · Gradient Descent & Convergence (6 cards)</option>
              <option value="09_Geometry_of_Constrained_Optimization_Tangent_Cone_and_LICQ">Topic 09 · Tangent Cones & LICQ Geometry (6 cards)</option>
              <option value="all">🌟 All Available Topics (36 cards in sequence)</option>
            </select>
          </div>

          <!-- Search Input -->
          <div class="relative flex-1 min-w-[220px]">
            <input type="text" id="search-input" oninput="filterCards()" placeholder="Search formulas, mechanisms, traps..." class="w-full bg-[#0d1326] border border-slate-700/80 rounded-xl py-1.5 pl-8 pr-3 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-cyan-400 focus:ring-1 focus:ring-cyan-400 transition">
            <span class="absolute left-2.5 top-2 text-xs text-cyan-400 opacity-75">🔍</span>
          </div>
        </div>"""

html = html.replace(old_search_block, new_search_and_nav)

# 3. Update Banner with Topic Title and Previous/Next buttons
old_banner = """      <!-- Topic Header Banner -->
      <div class="flex flex-wrap items-center justify-between gap-3 mb-6 pb-3 border-b border-cyan-500/15">
        <div class="flex items-center gap-3">
          <span class="px-2.5 py-1 rounded-lg text-xs font-mono font-bold bg-cyan-500/10 text-cyan-400 border border-cyan-500/30 uppercase tracking-widest flex items-center gap-1.5">
            <span>🪐</span> ORBITAL DECK
          </span>
          <h2 class="text-xl sm:text-2xl font-bold text-white tracking-tight">
            Feasible Sets, Active Constraints & Tangent Cones
          </h2>
      </div>"""

new_banner = """      <!-- Topic Header Banner with Interactive Sequence Navigator -->
      <div class="flex flex-wrap items-center justify-between gap-3 mb-6 pb-3 border-b border-cyan-500/15">
        <div class="flex items-center gap-3">
          <span class="px-2.5 py-1 rounded-lg text-xs font-mono font-bold bg-cyan-500/10 text-cyan-400 border border-cyan-500/30 uppercase tracking-widest flex items-center gap-1.5 shrink-0">
            <span>🪐</span> ORBITAL DECK
          </span>
          <h2 id="topic-title-banner" class="text-xl sm:text-2xl font-bold text-white tracking-tight">
            01 · Mathematical Preliminaries & Weierstrass
          </h2>
        </div>

        <!-- Sequential Topic Stepper Controls -->
        <div class="flex items-center gap-2">
          <button onclick="navigateTopic(-1)" class="px-3 py-1.5 rounded-xl bg-[#0d1326] hover:bg-slate-800 text-xs font-mono text-cyan-300 border border-cyan-500/30 transition flex items-center gap-1.5 cursor-pointer shadow hover:shadow-cyan-500/20 active:scale-95">
            <span>←</span> Prev Topic
          </button>
          <span id="topic-card-counter" class="px-3 py-1.5 rounded-xl bg-cyan-950/80 text-cyan-300 text-xs font-mono font-bold border border-cyan-800/80">
            6 Cards Active
          </span>
          <button onclick="navigateTopic(1)" class="px-3 py-1.5 rounded-xl bg-[#0d1326] hover:bg-slate-800 text-xs font-mono text-cyan-300 border border-cyan-500/30 transition flex items-center gap-1.5 cursor-pointer shadow hover:shadow-cyan-500/20 active:scale-95">
            Next Topic <span>→</span>
          </button>
        </div>
      </div>"""

html = html.replace(old_banner, new_banner)

# 4. Replace deck loading logic with dynamic multi-topic handling
old_deck_init = """    let deck = JSON.parse(localStorage.getItem('sirianni_index_cards_cosmos_v7')) || defaultDeck;
    let gridCols = 1; // Default to expansive 1 Wide layout as requested
    let currentScale = 'large'; // Default to large 125% scale"""

new_deck_init = """    const masterCards = window.MASTER_CARDS_DATA || defaultDeck;
    let currentTopic = '01_Mathematical_Preliminaries_Topology_and_Weierstrass';
    let deck = masterCards.filter(c => c.topicId === currentTopic);
    let gridCols = 1; // Default to expansive 1 Wide layout as requested
    let currentScale = 'large'; // Default to large 125% scale

    function getTopicsList() {
      const map = new Map();
      masterCards.forEach(c => {
        if (!map.has(c.topicId)) {
          map.set(c.topicId, c.topicTitle || c.topicId);
        }
      });
      return Array.from(map.entries());
    }

    function switchTopic(topicId) {
      currentTopic = topicId;
      const searchInput = document.getElementById('search-input');
      if (searchInput) searchInput.value = '';

      if (topicId === 'all') {
        deck = [...masterCards];
        document.getElementById('topic-title-banner').textContent = 'All Available Topics in Sequence (CMO)';
      } else {
        deck = masterCards.filter(c => c.topicId === topicId);
        const match = masterCards.find(c => c.topicId === topicId);
        document.getElementById('topic-title-banner').textContent = match ? match.topicTitle : topicId;
      }

      const select = document.getElementById('topic-select');
      if (select && select.value !== topicId) select.value = topicId;

      const counter = document.getElementById('topic-card-counter');
      if (counter) counter.textContent = `${deck.length} Cards Active`;

      renderDeck();
    }

    function navigateTopic(dir) {
      const topics = getTopicsList().map(t => t[0]);
      let idx = topics.indexOf(currentTopic);
      if (idx === -1) idx = 0;
      let nextIdx = idx + dir;
      if (nextIdx < 0) nextIdx = topics.length - 1;
      if (nextIdx >= topics.length) nextIdx = 0;
      switchTopic(topics[nextIdx]);
    }"""

html = html.replace(old_deck_init, new_deck_init)

# 5. Fix filterCards to render full rich cards rather than simplified markup
old_filter_cards = """    /* Filter Cards */
    function filterCards() {
      const q = document.getElementById('search-input').value.toLowerCase();
      if (!q) {
        renderDeck();
        return;
      }
      const filtered = deck.filter(c => 
        c.title.toLowerCase().includes(q) ||
        c.personalConnection.toLowerCase().includes(q) ||
        c.coreTranslation.some(t => t.toLowerCase().includes(q))
      );
      
      const grid = document.getElementById('desk-grid');
      const countEl = document.getElementById('card-count');
      if (countEl) countEl.textContent = filtered.length;
      grid.innerHTML = filtered.map(c => `
        <div class="cosmic-card aspect-16-9 p-8 flex flex-col justify-between relative overflow-hidden">
          <canvas class="card-stars absolute inset-0 w-full h-full pointer-events-none z-0 rounded-[20px]"></canvas>
          <div class="relative z-10 flex items-center justify-between pb-3 border-b border-white/10">
            <span class="font-mono text-cyan-400 font-bold">CARD ${c.cardNumber} · ${c.category}</span>
            <span class="font-serif-title font-bold text-xl text-white">${c.title}</span>
          </div>
          <div class="relative z-10 my-3 text-slate-200">
            <div class="text-sm text-cyan-300 font-mono mb-2">CORE MECHANISM:</div>
            <ul class="space-y-1.5 text-sm">
              ${c.coreTranslation.map(pt => `<li>› ${pt}</li>`).join('')}
            </ul>
          </div>
          <div class="relative z-10 p-3 bg-black/40 rounded-xl font-mono text-sm border border-cyan-500/20 text-cyan-200">
            ${c.math}
          </div>
          <div class="relative z-10 text-xs italic text-amber-200 pt-2 border-t border-white/10">
            💡 "${c.personalConnection}"
          </div>
        </div>
      `).join('');

      if (window.renderMathInElement) {
        renderMathInElement(grid, {
          delimiters: [
            {left: '$$', right: '$$', display: true},
            {left: '$', right: '$', display: false}
          ]
        });
      }
      setTimeout(() => initCardStarfields(), 30);
    }"""

new_filter_cards = """    /* Filter Cards within active scope */
    function filterCards() {
      const q = document.getElementById('search-input').value.toLowerCase();
      let baseList = (currentTopic === 'all') ? masterCards : masterCards.filter(c => c.topicId === currentTopic);
      if (!q) {
        deck = baseList;
        renderDeck();
        return;
      }
      deck = baseList.filter(c => 
        c.title.toLowerCase().includes(q) ||
        (c.category && c.category.toLowerCase().includes(q)) ||
        (c.personalConnection && c.personalConnection.toLowerCase().includes(q)) ||
        (c.examTrap && c.examTrap.toLowerCase().includes(q)) ||
        c.coreTranslation.some(t => t.toLowerCase().includes(q))
      );
      renderDeck();
    }"""

html = html.replace(old_filter_cards, new_filter_cards)

with open('/Users/senso/Projects/photographic-memory-cards/index.html', 'w') as f:
    f.write(html)

print("Updated index.html successfully!")
