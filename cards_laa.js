/* LAA knowledge plates. Loaded after cards_data.js and appended to it. */
window.MASTER_CARDS_DATA = (window.MASTER_CARDS_DATA || []).concat([
  {
    "id": 20201,
    "subject": "LAA",
    "topicId": "02_Linear_Independence_Bases_and_Dimension",
    "topicTitle": "02 \u00b7 Independence, Bases & Dimension",
    "cardNumber": "01",
    "category": "LINEAR INDEPENDENCE",
    "highlighterClass": "highlight-cyan",
    "title": "Span & Linear Independence",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-20201\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"24\" y1=\"72\" x2=\"112\" y2=\"72\" stroke=\"#000000\" stroke-width=\"0.8\" stroke-dasharray=\"2 3\"/><line x1=\"68\" y1=\"20\" x2=\"68\" y2=\"124\" stroke=\"#000000\" stroke-width=\"0.8\" stroke-dasharray=\"2 3\"/><line x1=\"68\" y1=\"72\" x2=\"104\" y2=\"40\" stroke=\"#000000\" stroke-width=\"2.2\" marker-end=\"url(#arr-20201)\"/><line x1=\"68\" y1=\"72\" x2=\"34\" y2=\"50\" stroke=\"#000000\" stroke-width=\"2.2\" marker-end=\"url(#arr-20201)\"/><text x=\"110\" y=\"36\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">v\u2081</text><text x=\"28\" y=\"44\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">v\u2082</text><text x=\"68\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">independent: a plane</text><line x1=\"132\" y1=\"72\" x2=\"226\" y2=\"72\" stroke=\"#000000\" stroke-width=\"0.8\" stroke-dasharray=\"2 3\"/><line x1=\"150\" y1=\"108\" x2=\"190\" y2=\"72\" stroke=\"#000000\" stroke-width=\"2.2\" marker-end=\"url(#arr-20201)\"/><line x1=\"150\" y1=\"108\" x2=\"210\" y2=\"48\" stroke=\"#000000\" stroke-width=\"1.6\" stroke-dasharray=\"4 3\" marker-end=\"url(#arr-20201)\"/><text x=\"204\" y=\"112\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">u\u2082 = 1.5 u\u2081</text><text x=\"180\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">dependent: a line</text></svg>",
    "drawingCaption": "Independent vectors point in genuinely different directions; dependent ones lie on one line",
    "coreTranslation": [
      "<strong>Span:</strong> $\\operatorname{span}(v_1,\\dots,v_m)$ is the set of all linear combinations $a_1v_1+\\dots+a_mv_m$, the smallest subspace containing the list.",
      "<strong>Independence:</strong> the list is independent if the <strong>only</strong> way to make $0$ is with every coefficient zero: $a_1v_1+\\dots+a_mv_m=0\\Rightarrow a_1=\\dots=a_m=0$.",
      "<strong>Meaning:</strong> no vector is redundant, i.e. none lies in the span of the others. Any list containing $0$ or a repeated vector is dependent."
    ],
    "math": "$$a_1v_1+\\cdots+a_mv_m=0\\ \\Longrightarrow\\ a_1=\\cdots=a_m=0\\quad(\\text{independent})$$",
    "personalConnection": "A band where every member plays a unique instrument: remove anyone and the sound changes; a duplicate instrument adds nothing new.",
    "examTrap": "Independence is a property of the LIST, not the set of vectors: the list (v, v) is dependent even though the set {v} is not."
  },
  {
    "id": 20202,
    "subject": "LAA",
    "topicId": "02_Linear_Independence_Bases_and_Dimension",
    "topicTitle": "02 \u00b7 Independence, Bases & Dimension",
    "cardNumber": "02",
    "category": "BASES",
    "highlighterClass": "highlight-amber",
    "title": "Basis = Independent + Spanning (Unique Coordinates)",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-20202\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"24\" y1=\"110\" x2=\"214\" y2=\"110\" stroke=\"#000000\" stroke-width=\"0.8\" stroke-dasharray=\"2 3\"/><line x1=\"40\" y1=\"130\" x2=\"40\" y2=\"16\" stroke=\"#000000\" stroke-width=\"0.8\" stroke-dasharray=\"2 3\"/><line x1=\"40\" y1=\"110\" x2=\"100\" y2=\"90\" stroke=\"#000000\" stroke-width=\"2.4\" marker-end=\"url(#arr-20202)\"/><line x1=\"40\" y1=\"110\" x2=\"60\" y2=\"50\" stroke=\"#000000\" stroke-width=\"2.4\" marker-end=\"url(#arr-20202)\"/><text x=\"104\" y=\"90\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">b\u2081</text><text x=\"48\" y=\"44\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">b\u2082</text><line x1=\"40\" y1=\"110\" x2=\"140\" y2=\"56\" stroke=\"#000000\" stroke-width=\"2.0\" stroke-dasharray=\"5 3\" marker-end=\"url(#arr-20202)\"/><line x1=\"100\" y1=\"90\" x2=\"140\" y2=\"56\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"2 2\"/><line x1=\"60\" y1=\"50\" x2=\"140\" y2=\"56\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"2 2\"/><text x=\"150\" y=\"52\" font-size=\"11\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"start\" fill=\"#000000\">v</text><text x=\"150\" y=\"126\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">v = 2 b\u2081 + 1.5 b\u2082 : coordinates (2, 1.5)</text><text x=\"150\" y=\"140\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">exactly ONE way to reach every v</text></svg>",
    "drawingCaption": "Every vector is reached in exactly one way as a combination of basis vectors",
    "coreTranslation": [
      "<strong>Basis:</strong> a list that is <strong>both independent and spanning</strong>: no redundancy, and nothing missing.",
      "<strong>Key property:</strong> every $v\\in V$ can be written as $v=a_1b_1+\\dots+a_nb_n$ in <strong>exactly one</strong> way; the $a_j$ are its <strong>coordinates</strong> $[v]_B$.",
      "<strong>Why it matters:</strong> a basis turns an abstract space into $\\mathbb{F}^n$: vectors become columns, linear maps become matrices."
    ],
    "math": "$$v=\\sum_{j=1}^{n}a_jb_j\\ \\text{ (unique } a_j),\\qquad [v]_B=(a_1,\\dots,a_n)^T\\in\\mathbb{F}^n$$",
    "personalConnection": "Street addresses: 'two blocks east, one and a half north' pins down a location in exactly one way once the compass directions are fixed.",
    "examTrap": "Coordinates depend on the BASIS (and its ORDER). Reordering the basis permutes the coordinates; changing it changes them entirely."
  },
  {
    "id": 20203,
    "subject": "LAA",
    "topicId": "02_Linear_Independence_Bases_and_Dimension",
    "topicTitle": "02 \u00b7 Independence, Bases & Dimension",
    "cardNumber": "03",
    "category": "DIMENSION",
    "highlighterClass": "highlight-emerald",
    "title": "Steinitz Exchange: Independent Lists Are No Longer Than Spanning Lists",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-20203\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"20\" y=\"20\" width=\"90\" height=\"26\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"65.0\" y=\"32.0\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">spanning list:</text><text x=\"65.0\" y=\"41.5\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">n vectors</text><rect x=\"20\" y=\"62\" width=\"62\" height=\"26\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"51.0\" y=\"78.0\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">independent: m</text><line x1=\"82\" y1=\"75\" x2=\"130\" y2=\"75\" stroke=\"#000000\" stroke-width=\"1.4\" marker-end=\"url(#arr-20203)\"/><text x=\"106\" y=\"68\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">swap one at a time</text><text x=\"180\" y=\"79\" font-size=\"14\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">m \u2264 n</text><text x=\"120\" y=\"112\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">length of any independent list \u2264 length of any spanning list</text><text x=\"120\" y=\"128\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">so every basis of V has the same length</text></svg>",
    "drawingCaption": "Swap independent vectors into the spanning list one at a time; you can never run out of room",
    "coreTranslation": [
      "<strong>Statement:</strong> in a finite-dimensional space, <strong>length of any independent list $\\le$ length of any spanning list</strong>.",
      "<strong>Idea:</strong> put an independent vector $u_1$ into the spanning list, which makes it dependent, so one old vector can be dropped; repeat. If $m>n$ you would run out of old vectors first, a contradiction.",
      "<strong>Consequence:</strong> any two bases have the <strong>same length</strong>, which is what makes <strong>dimension</strong> well defined."
    ],
    "math": "$$u_1,\\dots,u_m\\ \\text{independent},\\quad w_1,\\dots,w_n\\ \\text{span}\\ \\Longrightarrow\\ m\\le n$$",
    "personalConnection": "Moving boxes into a van one at a time: if every box you bring in pushes one old box out, you can't have brought in more boxes than the van held.",
    "examTrap": "The inequality needs independence on the SHORT side and spanning on the LONG side. A spanning list may be longer than a basis; an independent list may be shorter."
  },
  {
    "id": 20204,
    "subject": "LAA",
    "topicId": "02_Linear_Independence_Bases_and_Dimension",
    "topicTitle": "02 \u00b7 Independence, Bases & Dimension",
    "cardNumber": "04",
    "category": "DIMENSION",
    "highlighterClass": "highlight-purple",
    "title": "Dimension Facts You Use Constantly",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-20204\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"14\" y=\"20\" width=\"100\" height=\"30\" rx=\"0\" fill=\"#e2e8f0\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"64.0\" y=\"38.0\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">dim V = n</text><rect x=\"14\" y=\"66\" width=\"100\" height=\"26\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"64.0\" y=\"82.0\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">U \u2286 V \u21d2 dim U \u2264 dim V</text><rect x=\"14\" y=\"104\" width=\"100\" height=\"26\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"64.0\" y=\"120.0\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">dim U = dim V \u21d2 U = V</text><rect x=\"130\" y=\"20\" width=\"96\" height=\"40\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"178.0\" y=\"39.0\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">any n independent</text><text x=\"178.0\" y=\"48.5\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">vectors = a basis</text><rect x=\"130\" y=\"72\" width=\"96\" height=\"40\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"178.0\" y=\"91.0\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">any n spanning</text><text x=\"178.0\" y=\"100.5\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">vectors = a basis</text><text x=\"178\" y=\"128\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">(check one half, get the other)</text></svg>",
    "drawingCaption": "With the right count you only need to verify half of 'basis'",
    "coreTranslation": [
      "<strong>Subspaces:</strong> if $U\\subseteq V$ then $\\dim U\\le\\dim V$, and <strong>equality forces $U=V$</strong> (finite-dimensional case).",
      "<strong>Half-check:</strong> in an $n$-dimensional space, any <strong>independent list of length $n$</strong> is automatically a basis, and so is any <strong>spanning list of length $n$</strong>.",
      "<strong>Examples:</strong> $\\dim\\mathbb{F}^n=n$, $\\dim\\mathcal{P}_m(\\mathbb{F})=m+1$, $\\dim\\mathbb{F}^{m\\times n}=mn$, $\\dim\\mathcal{L}(V,W)=\\dim V\\cdot\\dim W$."
    ],
    "math": "$$\\dim\\mathcal{P}_m=m+1,\\quad \\dim\\mathbb{F}^{m\\times n}=mn,\\quad \\dim\\mathcal{L}(V,W)=\\dim V\\,\\dim W$$",
    "personalConnection": "A full set of n keys for n locks: if you have n keys and they are all different (independent), you automatically have a complete set.",
    "examTrap": "The half-check works only when the length EQUALS dim V. Three independent vectors in a 4-D space do NOT form a basis."
  },
  {
    "id": 20205,
    "subject": "LAA",
    "topicId": "02_Linear_Independence_Bases_and_Dimension",
    "topicTitle": "02 \u00b7 Independence, Bases & Dimension",
    "cardNumber": "05",
    "category": "BASES",
    "highlighterClass": "highlight-cyan",
    "title": "Reduce a Spanning List, Extend an Independent One",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-20205\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"10\" y=\"16\" width=\"100\" height=\"30\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"60.0\" y=\"34.0\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">spanning list</text><line x1=\"60\" y1=\"46\" x2=\"60\" y2=\"66\" stroke=\"#000000\" stroke-width=\"1.4\" marker-end=\"url(#arr-20205)\"/><text x=\"116\" y=\"60\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">delete redundant vectors</text><rect x=\"10\" y=\"68\" width=\"100\" height=\"30\" rx=\"0\" fill=\"#e2e8f0\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"60.0\" y=\"86.0\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">BASIS</text><line x1=\"60\" y1=\"98\" x2=\"60\" y2=\"118\" stroke=\"#000000\" stroke-width=\"1.4\" marker-end=\"url(#arr-20205)\"/><rect x=\"130\" y=\"68\" width=\"96\" height=\"30\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"178.0\" y=\"86.0\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">independent list</text><line x1=\"178\" y1=\"98\" x2=\"178\" y2=\"118\" stroke=\"#000000\" stroke-width=\"1.4\" marker-end=\"url(#arr-20205)\"/><text x=\"176\" y=\"132\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">add vectors until it spans</text><text x=\"60\" y=\"134\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\"></text><line x1=\"122\" y1=\"83\" x2=\"112\" y2=\"83\" stroke=\"#000000\" stroke-width=\"1.4\" marker-end=\"url(#arr-20205)\"/></svg>",
    "drawingCaption": "From either side you land on a basis: shrink a spanning list, grow an independent one",
    "coreTranslation": [
      "<strong>Reduction:</strong> every spanning list contains a <strong>basis</strong>. Scan left to right and delete any vector already in the span of those before it.",
      "<strong>Extension:</strong> every independent list can be <strong>extended to a basis</strong> by adjoining vectors from a basis (or any spanning list) until it spans.",
      "<strong>Subspace complements:</strong> for any subspace $U\\subseteq V$ there is a subspace $W$ with $V=U\\oplus W$ (extend a basis of $U$)."
    ],
    "math": "$$\\text{span list}\\ \\xrightarrow{\\ \\text{delete}\\ }\\ \\text{basis}\\ \\xleftarrow{\\ \\text{adjoin}\\ }\\ \\text{independent list},\\qquad V=U\\oplus W$$",
    "personalConnection": "Packing a suitcase: from an overstuffed bag you remove duplicates until nothing is repeated; from a nearly empty bag you add items until you are covered.",
    "examTrap": "The complement W of U is NOT unique (only its dimension is). Different extensions of a basis of U give different complements."
  },
  {
    "id": 20206,
    "subject": "LAA",
    "topicId": "02_Linear_Independence_Bases_and_Dimension",
    "topicTitle": "02 \u00b7 Independence, Bases & Dimension",
    "cardNumber": "06",
    "category": "WORKED BENCHMARK",
    "highlighterClass": "highlight-amber",
    "title": "Worked Benchmark: Independence and Basis in \u211d\u00b3",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-20206\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"14\" y=\"18\" width=\"24\" height=\"24\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.1\"/><text x=\"26.0\" y=\"33.0\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">1</text><rect x=\"38\" y=\"18\" width=\"24\" height=\"24\" rx=\"0\" fill=\"#d9dee7\" stroke=\"#000000\" stroke-width=\"1.1\"/><text x=\"50.0\" y=\"33.0\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">2</text><rect x=\"62\" y=\"18\" width=\"24\" height=\"24\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.1\"/><text x=\"74.0\" y=\"33.0\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">1</text><rect x=\"14\" y=\"42\" width=\"24\" height=\"24\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.1\"/><text x=\"26.0\" y=\"57.0\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">2</text><rect x=\"38\" y=\"42\" width=\"24\" height=\"24\" rx=\"0\" fill=\"#d9dee7\" stroke=\"#000000\" stroke-width=\"1.1\"/><text x=\"50.0\" y=\"57.0\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">4</text><rect x=\"62\" y=\"42\" width=\"24\" height=\"24\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.1\"/><text x=\"74.0\" y=\"57.0\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">0</text><rect x=\"14\" y=\"66\" width=\"24\" height=\"24\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.1\"/><text x=\"26.0\" y=\"81.0\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">3</text><rect x=\"38\" y=\"66\" width=\"24\" height=\"24\" rx=\"0\" fill=\"#d9dee7\" stroke=\"#000000\" stroke-width=\"1.1\"/><text x=\"50.0\" y=\"81.0\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">6</text><rect x=\"62\" y=\"66\" width=\"24\" height=\"24\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.1\"/><text x=\"74.0\" y=\"81.0\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">1</text><text x=\"50\" y=\"14\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">v\u2081   v\u2082   v\u2083</text><text x=\"122\" y=\"30\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"start\" fill=\"#000000\">v\u2082 = 2 v\u2081</text><text x=\"122\" y=\"50\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">\u21d2 dependent list</text><text x=\"122\" y=\"70\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">span = span(v\u2081, v\u2083)</text><text x=\"122\" y=\"90\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">v\u2081, v\u2083 independent</text><text x=\"122\" y=\"110\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"start\" fill=\"#000000\">basis, dim = 2</text><text x=\"14\" y=\"108\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">columns are the vectors</text></svg>",
    "drawingCaption": "The middle column is twice the first, so it adds nothing; two columns remain and they are independent",
    "coreTranslation": [
      "<strong>Columns:</strong> $v_1=(1,2,3)$, $v_2=(2,4,6)$, $v_3=(1,0,1)$. Clearly $v_2=2v_1$, so $2v_1-v_2+0\\,v_3=0$ is a nontrivial relation: the list is <strong>dependent</strong>.",
      "<strong>Reduce:</strong> drop $v_2$. The remaining pair $v_1,v_3$ is independent because neither is a multiple of the other (compare first coordinates: $1:1$, second: $2:0$).",
      "<strong>Conclusion:</strong> $\\operatorname{span}(v_1,v_2,v_3)=\\operatorname{span}(v_1,v_3)$ is a <strong>plane</strong> with basis $\\{v_1,v_3\\}$ and $\\dim=2$ (so these three vectors do not span $\\mathbb{R}^3$)."
    ],
    "math": "$$2v_1-v_2+0\\,v_3=0,\\qquad \\operatorname{span}(v_1,v_2,v_3)=\\operatorname{span}(v_1,v_3),\\quad \\dim=2$$",
    "personalConnection": "Three roads on a map where one is just the first road traveled twice as far: you really only have two distinct directions.",
    "examTrap": "Three vectors in \u211d\u00b3 do not automatically span \u211d\u00b3. Count the INDEPENDENT ones (the rank), not the list length."
  },
  {
    "id": 20301,
    "subject": "LAA",
    "topicId": "03_Linear_Maps_Null_Space_Range_and_Matrices",
    "topicTitle": "03 \u00b7 Linear Maps, Null Space & Range",
    "cardNumber": "01",
    "category": "LINEAR MAPS",
    "highlighterClass": "highlight-cyan",
    "title": "What 'Linear' Means Geometrically",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-20301\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"20\" y1=\"24\" x2=\"20\" y2=\"104\" stroke=\"#000000\" stroke-width=\"0.8\"/><line x1=\"20\" y1=\"24\" x2=\"100\" y2=\"24\" stroke=\"#000000\" stroke-width=\"0.8\"/><line x1=\"40\" y1=\"24\" x2=\"40\" y2=\"104\" stroke=\"#000000\" stroke-width=\"0.8\"/><line x1=\"20\" y1=\"44\" x2=\"100\" y2=\"44\" stroke=\"#000000\" stroke-width=\"0.8\"/><line x1=\"60\" y1=\"24\" x2=\"60\" y2=\"104\" stroke=\"#000000\" stroke-width=\"0.8\"/><line x1=\"20\" y1=\"64\" x2=\"100\" y2=\"64\" stroke=\"#000000\" stroke-width=\"0.8\"/><line x1=\"80\" y1=\"24\" x2=\"80\" y2=\"104\" stroke=\"#000000\" stroke-width=\"0.8\"/><line x1=\"20\" y1=\"84\" x2=\"100\" y2=\"84\" stroke=\"#000000\" stroke-width=\"0.8\"/><line x1=\"100\" y1=\"24\" x2=\"100\" y2=\"104\" stroke=\"#000000\" stroke-width=\"0.8\"/><line x1=\"20\" y1=\"104\" x2=\"100\" y2=\"104\" stroke=\"#000000\" stroke-width=\"0.8\"/><rect x=\"20\" y=\"24\" width=\"80\" height=\"80\" rx=\"0\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.4\"/><line x1=\"108\" y1=\"64\" x2=\"128\" y2=\"64\" stroke=\"#000000\" stroke-width=\"1.5\" marker-end=\"url(#arr-20301)\"/><text x=\"118\" y=\"56\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">T</text><line x1=\"140\" y1=\"104\" x2=\"180\" y2=\"24\" stroke=\"#000000\" stroke-width=\"0.8\"/><line x1=\"140.0\" y1=\"24\" x2=\"220\" y2=\"24\" stroke=\"#000000\" stroke-width=\"0.0\"/><line x1=\"160\" y1=\"104\" x2=\"200\" y2=\"24\" stroke=\"#000000\" stroke-width=\"0.8\"/><line x1=\"140.0\" y1=\"44\" x2=\"220\" y2=\"44\" stroke=\"#000000\" stroke-width=\"0.0\"/><line x1=\"180\" y1=\"104\" x2=\"220\" y2=\"24\" stroke=\"#000000\" stroke-width=\"0.8\"/><line x1=\"140.0\" y1=\"64\" x2=\"220\" y2=\"64\" stroke=\"#000000\" stroke-width=\"0.0\"/><line x1=\"200\" y1=\"104\" x2=\"240\" y2=\"24\" stroke=\"#000000\" stroke-width=\"0.8\"/><line x1=\"140.0\" y1=\"84\" x2=\"220\" y2=\"84\" stroke=\"#000000\" stroke-width=\"0.0\"/><line x1=\"220\" y1=\"104\" x2=\"260\" y2=\"24\" stroke=\"#000000\" stroke-width=\"0.8\"/><line x1=\"140.0\" y1=\"104\" x2=\"220\" y2=\"104\" stroke=\"#000000\" stroke-width=\"0.0\"/><line x1=\"180.0\" y1=\"24\" x2=\"260.0\" y2=\"24\" stroke=\"#000000\" stroke-width=\"0.8\"/><line x1=\"170.0\" y1=\"44\" x2=\"250.0\" y2=\"44\" stroke=\"#000000\" stroke-width=\"0.8\"/><line x1=\"160.0\" y1=\"64\" x2=\"240.0\" y2=\"64\" stroke=\"#000000\" stroke-width=\"0.8\"/><line x1=\"150.0\" y1=\"84\" x2=\"230.0\" y2=\"84\" stroke=\"#000000\" stroke-width=\"0.8\"/><line x1=\"140.0\" y1=\"104\" x2=\"220.0\" y2=\"104\" stroke=\"#000000\" stroke-width=\"0.8\"/><text x=\"70\" y=\"120\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">straight lines stay straight</text><text x=\"180\" y=\"120\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">parallel stay parallel; 0 \u21a6 0</text><circle cx=\"20\" cy=\"104\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><circle cx=\"140\" cy=\"104\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/></svg>",
    "drawingCaption": "A linear map warps the whole grid but keeps lines straight, parallels parallel, and the origin fixed",
    "coreTranslation": [
      "<strong>Definition:</strong> $T:V\\to W$ is linear if $T(u+v)=Tu+Tv$ and $T(\\lambda v)=\\lambda\\,Tv$ (additivity and homogeneity).",
      "<strong>Consequences:</strong> $T(0)=0$, and $T$ is <strong>completely determined by its values on a basis</strong>: $T(\\sum a_jv_j)=\\sum a_jTv_j$.",
      "<strong>Geometry:</strong> lines go to lines (or points), parallel lines stay parallel, the origin is fixed, and grid cells become parallelograms. Maps like $x\\mapsto x+1$ are <strong>not</strong> linear."
    ],
    "math": "$$T(au+bv)=aTu+bTv,\\qquad T(0)=0,\\qquad T\\Big(\\sum a_jv_j\\Big)=\\sum a_jT(v_j)$$",
    "personalConnection": "Stretching a rubber sheet with a drawn grid, pinned at one point: lines may tilt and cells may skew, but no line may bend.",
    "examTrap": "'Linear' in this sense (a linear map) is NOT the same as 'a line y = mx + b'. The map x \u21a6 2x + 1 is affine, not linear (T(0) \u2260 0)."
  },
  {
    "id": 20302,
    "subject": "LAA",
    "topicId": "03_Linear_Maps_Null_Space_Range_and_Matrices",
    "topicTitle": "03 \u00b7 Linear Maps, Null Space & Range",
    "cardNumber": "02",
    "category": "LINEAR MAPS",
    "highlighterClass": "highlight-amber",
    "title": "Null Space and Range",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-20302\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"14\" y=\"20\" width=\"100\" height=\"90\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.6\"/><rect x=\"14\" y=\"50\" width=\"100\" height=\"30\" rx=\"0\" fill=\"#d9dee7\" stroke=\"#000000\" stroke-width=\"1.4\" stroke-dasharray=\"4 3\"/><text x=\"64\" y=\"40\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">V</text><text x=\"64\" y=\"68\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">null T</text><text x=\"64\" y=\"100\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">complement</text><rect x=\"150\" y=\"20\" width=\"76\" height=\"90\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.6\"/><rect x=\"150\" y=\"50\" width=\"76\" height=\"32\" rx=\"0\" fill=\"#e2e8f0\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"188\" y=\"40\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">W</text><text x=\"188\" y=\"70\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">range T</text><line x1=\"116\" y1=\"64\" x2=\"148\" y2=\"64\" stroke=\"#000000\" stroke-width=\"1.5\" marker-end=\"url(#arr-20302)\"/><text x=\"132\" y=\"56\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">T</text><circle cx=\"188\" cy=\"100\" r=\"3.5\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"188\" y=\"114\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">0</text><path d=\"M114 66 Q132 90 186 100\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.3\" stroke-dasharray=\"4 3\" marker-end=\"url(#arr-20302)\"/><text x=\"120\" y=\"132\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\"></text></svg>",
    "drawingCaption": "The null space is the part of V that T crushes to zero; the range is what T actually reaches in W",
    "coreTranslation": [
      "<strong>Null space</strong> $\\operatorname{null}T=\\{v\\in V:Tv=0\\}$ is a <strong>subspace of $V$</strong>: the 'lost information'.",
      "<strong>Range</strong> $\\operatorname{range}T=\\{Tv:v\\in V\\}$ is a <strong>subspace of $W$</strong>: everything the map can output (the column space of its matrix).",
      "<strong>Meaning:</strong> $T$ is injective exactly when nothing but $0$ is lost, and surjective exactly when the range fills $W$."
    ],
    "math": "$$\\operatorname{null}T=\\{v:Tv=0\\}\\subseteq V,\\qquad \\operatorname{range}T=\\{Tv:v\\in V\\}\\subseteq W$$",
    "personalConnection": "A paper shredder (T): the null space is what comes out as zero pieces of information; the range is the shapes of confetti it can produce.",
    "examTrap": "null T lives in the DOMAIN V, range T lives in the CODOMAIN W. Mixing up where each one lives is the most common slip."
  },
  {
    "id": 20303,
    "subject": "LAA",
    "topicId": "03_Linear_Maps_Null_Space_Range_and_Matrices",
    "topicTitle": "03 \u00b7 Linear Maps, Null Space & Range",
    "cardNumber": "03",
    "category": "RANK-NULLITY",
    "highlighterClass": "highlight-emerald",
    "title": "Rank\u2013Nullity Theorem",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-20303\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"20\" y=\"30\" width=\"200\" height=\"36\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.8\"/><rect x=\"20\" y=\"30\" width=\"70\" height=\"36\" rx=\"0\" fill=\"#d9dee7\" stroke=\"#000000\" stroke-width=\"1.8\"/><text x=\"55\" y=\"52\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">dim null T</text><text x=\"155\" y=\"52\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">dim range T</text><text x=\"120\" y=\"22\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">dim V</text><line x1=\"20\" y1=\"74\" x2=\"220\" y2=\"74\" stroke=\"#000000\" stroke-width=\"1.2\"/><text x=\"120\" y=\"98\" font-size=\"11\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">dim V = dim null T + dim range T</text><text x=\"120\" y=\"116\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">(nullity + rank = number of columns)</text><text x=\"120\" y=\"132\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\"></text></svg>",
    "drawingCaption": "Every dimension of the domain either gets crushed (nullity) or survives as output (rank)",
    "coreTranslation": [
      "<strong>Theorem:</strong> for $T\\in\\mathcal{L}(V,W)$ with $V$ finite-dimensional, <strong>$\\dim V=\\dim\\operatorname{null}T+\\dim\\operatorname{range}T$</strong>.",
      "<strong>Proof idea:</strong> extend a basis of $\\operatorname{null}T$ to a basis of $V$; the added vectors map to a <strong>basis of the range</strong> (independent and spanning).",
      "<strong>Use:</strong> for an $m\\times n$ matrix, <strong>rank + nullity $=n$</strong> (number of columns). It is the single most used dimension-counting tool."
    ],
    "math": "$$\\dim V=\\dim\\operatorname{null}T+\\dim\\operatorname{range}T,\\qquad \\operatorname{rank}A+\\operatorname{nullity}A=n$$",
    "personalConnection": "A budget: each input dimension is either spent (destroyed by the map) or invested (shows up in the output); the total is fixed.",
    "examTrap": "The count is by COLUMNS (domain dimension), not rows. A tall matrix and its transpose have the same rank but different nullities."
  },
  {
    "id": 20304,
    "subject": "LAA",
    "topicId": "03_Linear_Maps_Null_Space_Range_and_Matrices",
    "topicTitle": "03 \u00b7 Linear Maps, Null Space & Range",
    "cardNumber": "04",
    "category": "LINEAR MAPS",
    "highlighterClass": "highlight-purple",
    "title": "Injective & Surjective: The Dimension Tests",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-20304\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"10\" y=\"16\" width=\"104\" height=\"34\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"62.0\" y=\"32.0\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">injective \u21d4</text><text x=\"62.0\" y=\"42.0\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">null T = {0}</text><rect x=\"126\" y=\"16\" width=\"104\" height=\"34\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"178.0\" y=\"32.0\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">surjective \u21d4</text><text x=\"178.0\" y=\"42.0\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">range T = W</text><rect x=\"10\" y=\"64\" width=\"104\" height=\"34\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"62.0\" y=\"80.0\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">injective \u21d2</text><text x=\"62.0\" y=\"89.5\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">dim V \u2264 dim W</text><rect x=\"126\" y=\"64\" width=\"104\" height=\"34\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"178.0\" y=\"80.0\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">surjective \u21d2</text><text x=\"178.0\" y=\"89.5\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">dim V \u2265 dim W</text><text x=\"120\" y=\"120\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">dim V > dim W \u21d2 some nonzero v \u21a6 0</text><text x=\"120\" y=\"134\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">dim V &lt; dim W \u21d2 cannot be onto</text></svg>",
    "drawingCaption": "Injectivity needs the domain to be no bigger than the codomain; surjectivity needs it to be no smaller",
    "coreTranslation": [
      "<strong>Injective</strong> $\\iff\\operatorname{null}T=\\{0\\}$ (a linear map is one-to-one exactly when only $0$ maps to $0$): you never have to compare pairs of points.",
      "<strong>Surjective</strong> $\\iff\\operatorname{range}T=W$. By rank\u2013nullity, injective forces $\\dim V\\le\\dim W$ and surjective forces $\\dim V\\ge\\dim W$.",
      "<strong>Consequence:</strong> a linear system with <strong>more unknowns than equations</strong> ($\\dim V>\\dim W$) always has a nonzero solution of the homogeneous system, so solutions are never unique."
    ],
    "math": "$$T\\ \\text{injective}\\iff\\operatorname{null}T=\\{0\\},\\qquad T\\ \\text{surjective}\\iff\\operatorname{range}T=W$$",
    "personalConnection": "Parking cars in spots: more cars than spots means two must share (not injective); more spots than cars means some stay empty (not surjective).",
    "examTrap": "The dimension tests are NECESSARY conditions only. dim V \u2264 dim W does not by itself make T injective (the zero map is a counterexample)."
  },
  {
    "id": 20305,
    "subject": "LAA",
    "topicId": "03_Linear_Maps_Null_Space_Range_and_Matrices",
    "topicTitle": "03 \u00b7 Linear Maps, Null Space & Range",
    "cardNumber": "05",
    "category": "MATRICES",
    "highlighterClass": "highlight-cyan",
    "title": "The Matrix of a Linear Map",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-20305\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><text x=\"14\" y=\"22\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">T v\u2081</text><text x=\"14\" y=\"36\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">T v\u2082</text><rect x=\"80\" y=\"14\" width=\"34\" height=\"34\" rx=\"0\" fill=\"#d9dee7\" stroke=\"#000000\" stroke-width=\"1.1\"/><text x=\"97.0\" y=\"34.0\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">a\u2081\u2081</text><rect x=\"114\" y=\"14\" width=\"34\" height=\"34\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.1\"/><text x=\"131.0\" y=\"34.0\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">a\u2081\u2082</text><rect x=\"148\" y=\"14\" width=\"34\" height=\"34\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.1\"/><text x=\"165.0\" y=\"34.0\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">a\u2081\u2083</text><rect x=\"80\" y=\"48\" width=\"34\" height=\"34\" rx=\"0\" fill=\"#d9dee7\" stroke=\"#000000\" stroke-width=\"1.1\"/><text x=\"97.0\" y=\"68.0\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">a\u2082\u2081</text><rect x=\"114\" y=\"48\" width=\"34\" height=\"34\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.1\"/><text x=\"131.0\" y=\"68.0\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">a\u2082\u2082</text><rect x=\"148\" y=\"48\" width=\"34\" height=\"34\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.1\"/><text x=\"165.0\" y=\"68.0\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">a\u2082\u2083</text><text x=\"97\" y=\"96\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">col 1 =</text><text x=\"97\" y=\"108\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">coords of T v\u2081</text><text x=\"97\" y=\"120\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">in basis of W</text><text x=\"170\" y=\"96\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">col j =</text><text x=\"170\" y=\"108\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">[T v_j]_{w}</text><text x=\"170\" y=\"124\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">(m \u00d7 n matrix)</text><line x1=\"97\" y1=\"80\" x2=\"97\" y2=\"86\" stroke=\"#000000\" stroke-width=\"1.1\"/><text x=\"14\" y=\"54\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\"></text></svg>",
    "drawingCaption": "Column j of the matrix lists the coordinates of T(v_j) in the target basis",
    "coreTranslation": [
      "<strong>Build:</strong> pick a basis $v_1..v_n$ of $V$ and $w_1..w_m$ of $W$. Express each $Tv_j=\\sum_i A_{ij}w_i$; the numbers $A_{ij}$ form the matrix $\\mathcal{M}(T)$ ($m\\times n$).",
      "<strong>Act:</strong> then $[Tv]_{w}=\\mathcal{M}(T)\\,[v]_{v}$: applying $T$ is multiplying coordinates by the matrix. The matrix <strong>depends on both bases</strong>.",
      "<strong>Dictionary:</strong> $\\mathcal{M}(S+T)=\\mathcal{M}(S)+\\mathcal{M}(T)$, $\\mathcal{M}(\\lambda T)=\\lambda\\mathcal{M}(T)$, and $\\mathcal{M}(ST)=\\mathcal{M}(S)\\mathcal{M}(T)$: <strong>matrix multiplication is composition</strong>."
    ],
    "math": "$$Tv_j=\\sum_{i=1}^{m}A_{ij}\\,w_i,\\qquad [Tv]_w=A\\,[v]_v,\\qquad \\mathcal{M}(ST)=\\mathcal{M}(S)\\,\\mathcal{M}(T)$$",
    "personalConnection": "A recipe card for a machine: each column says what the machine does to one standard input, and everything else is a mix of those.",
    "examTrap": "Rows are indexed by the TARGET basis, columns by the SOURCE basis. And the composition ST means T acts first, so M(ST) = M(S)M(T) in that order."
  },
  {
    "id": 20306,
    "subject": "LAA",
    "topicId": "03_Linear_Maps_Null_Space_Range_and_Matrices",
    "topicTitle": "03 \u00b7 Linear Maps, Null Space & Range",
    "cardNumber": "06",
    "category": "WORKED BENCHMARK",
    "highlighterClass": "highlight-amber",
    "title": "Worked Benchmark: T(x,y,z) = (x+y, y+z)",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-20306\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"14\" y=\"18\" width=\"30\" height=\"30\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.1\"/><text x=\"29.0\" y=\"36.0\" font-size=\"11\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">1</text><rect x=\"44\" y=\"18\" width=\"30\" height=\"30\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.1\"/><text x=\"59.0\" y=\"36.0\" font-size=\"11\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">1</text><rect x=\"74\" y=\"18\" width=\"30\" height=\"30\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.1\"/><text x=\"89.0\" y=\"36.0\" font-size=\"11\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">0</text><rect x=\"14\" y=\"48\" width=\"30\" height=\"30\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.1\"/><text x=\"29.0\" y=\"66.0\" font-size=\"11\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">0</text><rect x=\"44\" y=\"48\" width=\"30\" height=\"30\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.1\"/><text x=\"59.0\" y=\"66.0\" font-size=\"11\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">1</text><rect x=\"74\" y=\"48\" width=\"30\" height=\"30\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.1\"/><text x=\"89.0\" y=\"66.0\" font-size=\"11\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">1</text><text x=\"60\" y=\"90\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">A  (columns = T e\u2081, T e\u2082, T e\u2083)</text><text x=\"122\" y=\"30\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">null T: x+y=0, y+z=0</text><text x=\"122\" y=\"44\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"start\" fill=\"#000000\">\u21d2 (x,y,z) = t(1,\u22121,1)</text><text x=\"122\" y=\"64\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">nullity = 1</text><text x=\"122\" y=\"78\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"start\" fill=\"#000000\">range T = \u211d\u00b2 (rank 2)</text><text x=\"122\" y=\"98\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"start\" fill=\"#000000\">check: 3 = 1 + 2 \u2713</text><text x=\"122\" y=\"116\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">T is onto but not injective</text></svg>",
    "drawingCaption": "One free direction is crushed (nullity 1) and the plane \u211d\u00b2 is fully hit (rank 2)",
    "coreTranslation": [
      "<strong>Matrix:</strong> $T e_1=(1,0)$, $Te_2=(1,1)$, $Te_3=(0,1)$, so $A=\\begin{pmatrix}1&1&0\\\\0&1&1\\end{pmatrix}$.",
      "<strong>Null space:</strong> $x+y=0$ and $y+z=0$ give $(x,y,z)=t(1,-1,1)$, a line, so <strong>nullity $=1$</strong>.",
      "<strong>Rank:</strong> the columns $(1,0)$ and $(1,1)$ already span $\\mathbb{R}^2$, so rank $=2$ and $T$ is surjective. <strong>Check:</strong> $\\dim V=3=1+2$ \u2713. $T$ is not injective because $\\operatorname{null}T\\ne\\{0\\}$."
    ],
    "math": "$$\\operatorname{null}T=\\operatorname{span}\\{(1,-1,1)\\},\\quad \\operatorname{rank}=2,\\quad 3=1+2$$",
    "personalConnection": "A scanner projecting a 3-D object onto a 2-D screen: one whole line of depth collapses onto a single point of the screen.",
    "examTrap": "Surjective does not mean injective. Here the map covers all of \u211d\u00b2 and still loses a whole direction because dim V > dim W."
  },
  {
    "id": 20401,
    "subject": "LAA",
    "topicId": "04_Invertibility_Isomorphisms_and_Change_of_Basis",
    "topicTitle": "04 \u00b7 Isomorphisms & Change of Basis",
    "cardNumber": "01",
    "category": "INVERTIBILITY",
    "highlighterClass": "highlight-cyan",
    "title": "Invertible = Bijective (and the Inverse is Linear)",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-20401\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"14\" y=\"28\" width=\"70\" height=\"70\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.6\"/><rect x=\"156\" y=\"28\" width=\"70\" height=\"70\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.6\"/><circle cx=\"34\" cy=\"46\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><circle cx=\"34\" cy=\"66\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><circle cx=\"34\" cy=\"86\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><circle cx=\"206\" cy=\"46\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><circle cx=\"206\" cy=\"66\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><circle cx=\"206\" cy=\"86\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><line x1=\"38\" y1=\"46\" x2=\"202\" y2=\"46\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-20401)\"/><line x1=\"38\" y1=\"66\" x2=\"202\" y2=\"66\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-20401)\"/><line x1=\"38\" y1=\"86\" x2=\"202\" y2=\"86\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-20401)\"/><text x=\"120\" y=\"40\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">T</text><text x=\"120\" y=\"112\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">T\u207b\u00b9 goes back along every arrow</text><text x=\"49\" y=\"114\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">V</text><text x=\"191\" y=\"114\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">W</text><text x=\"120\" y=\"130\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">one-to-one AND onto</text></svg>",
    "drawingCaption": "Each point of W is hit exactly once, so the arrows can be reversed",
    "coreTranslation": [
      "<strong>Invertible</strong> means there is $S$ with $ST=I_V$ and $TS=I_W$. This holds <strong>iff $T$ is bijective</strong> (injective and surjective).",
      "<strong>Linearity is free:</strong> the inverse of a linear bijection is automatically linear. Also $(ST)^{-1}=T^{-1}S^{-1}$ (reverse order).",
      "<strong>Test:</strong> $T$ is invertible $\\iff\\operatorname{null}T=\\{0\\}$ and $\\operatorname{range}T=W$; for matrices, $A$ is invertible $\\iff\\det A\\ne0\\iff$ columns are a basis."
    ],
    "math": "$$T\\ \\text{invertible}\\iff T\\ \\text{bijective},\\qquad (ST)^{-1}=T^{-1}S^{-1}$$",
    "personalConnection": "Putting on socks then shoes: to undo it you remove the shoes first, then the socks (reverse order).",
    "examTrap": "(ST)\u207b\u00b9 is T\u207b\u00b9S\u207b\u00b9, NOT S\u207b\u00b9T\u207b\u00b9. Matrix products do not commute, so the order matters."
  },
  {
    "id": 20402,
    "subject": "LAA",
    "topicId": "04_Invertibility_Isomorphisms_and_Change_of_Basis",
    "topicTitle": "04 \u00b7 Isomorphisms & Change of Basis",
    "cardNumber": "02",
    "category": "ISOMORPHISMS",
    "highlighterClass": "highlight-amber",
    "title": "Isomorphic \u21d4 Same Dimension",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-20402\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"14\" y=\"24\" width=\"70\" height=\"36\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"49.0\" y=\"45.0\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">V (dim n)</text><rect x=\"156\" y=\"24\" width=\"70\" height=\"36\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"191.0\" y=\"45.0\" font-size=\"11\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\ud835\udd3d\u207f</text><line x1=\"86\" y1=\"42\" x2=\"154\" y2=\"42\" stroke=\"#000000\" stroke-width=\"1.6\" marker-end=\"url(#arr-20402)\"/><line x1=\"154\" y1=\"42\" x2=\"86\" y2=\"42\" stroke=\"#000000\" stroke-width=\"1.6\" marker-end=\"url(#arr-20402)\"/><text x=\"120\" y=\"34\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">coordinates [\u00b7]_B</text><rect x=\"14\" y=\"84\" width=\"70\" height=\"34\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"49.0\" y=\"104.0\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">dim V = n</text><rect x=\"156\" y=\"84\" width=\"70\" height=\"34\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"191.0\" y=\"104.0\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">dim W = n</text><line x1=\"86\" y1=\"101\" x2=\"154\" y2=\"101\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120\" y=\"96\" font-size=\"14\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u2245</text><text x=\"120\" y=\"132\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">same dimension \u21d2 the spaces are structurally identical</text></svg>",
    "drawingCaption": "Any n-dimensional space over \ud835\udd3d is just a relabeled \ud835\udd3d\u207f",
    "coreTranslation": [
      "<strong>Isomorphism:</strong> an invertible linear map $V\\to W$. Isomorphic spaces behave identically as vector spaces.",
      "<strong>Theorem:</strong> finite-dimensional $V\\cong W\\iff\\dim V=\\dim W$. Choosing a basis gives the isomorphism $v\\mapsto[v]_B\\in\\mathbb{F}^n$.",
      "<strong>Payoff:</strong> every finite-dimensional question can be moved to $\\mathbb{F}^n$ and answered with matrices. Dimension is the <strong>only</strong> invariant of a vector space up to isomorphism."
    ],
    "math": "$$V\\cong W\\iff\\dim V=\\dim W,\\qquad V\\cong\\mathbb{F}^{n}\\ \\ (n=\\dim V)$$",
    "personalConnection": "Translating the same book into different languages: the plot (structure) is identical; only the words (basis choice) change.",
    "examTrap": "Isomorphic does not mean equal. The space of 2\u00d72 matrices, P\u2083 and \u211d\u2074 are isomorphic, but the isomorphism depends on a chosen basis."
  },
  {
    "id": 20403,
    "subject": "LAA",
    "topicId": "04_Invertibility_Isomorphisms_and_Change_of_Basis",
    "topicTitle": "04 \u00b7 Isomorphisms & Change of Basis",
    "cardNumber": "03",
    "category": "INVERTIBILITY",
    "highlighterClass": "highlight-emerald",
    "title": "Operators: Injective \u21d4 Surjective \u21d4 Invertible",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-20403\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"76\" y=\"12\" width=\"88\" height=\"30\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"120.0\" y=\"30.0\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">injective</text><rect x=\"14\" y=\"92\" width=\"88\" height=\"30\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"58.0\" y=\"110.0\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">surjective</text><rect x=\"138\" y=\"92\" width=\"88\" height=\"30\" rx=\"0\" fill=\"#e2e8f0\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"182.0\" y=\"110.0\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">invertible</text><line x1=\"130\" y1=\"42\" x2=\"168\" y2=\"90\" stroke=\"#000000\" stroke-width=\"1.5\" marker-end=\"url(#arr-20403)\"/><line x1=\"100\" y1=\"107\" x2=\"136\" y2=\"107\" stroke=\"#000000\" stroke-width=\"1.5\" marker-end=\"url(#arr-20403)\"/><line x1=\"54\" y1=\"90\" x2=\"90\" y2=\"44\" stroke=\"#000000\" stroke-width=\"1.5\" marker-end=\"url(#arr-20403)\"/><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">operators on a finite-dimensional V (same space in and out)</text></svg>",
    "drawingCaption": "For a map from a finite-dimensional space to itself, any one of the three properties gives the other two",
    "coreTranslation": [
      "<strong>Theorem:</strong> if $T\\in\\mathcal{L}(V)$ and $\\dim V<\\infty$, then <strong>injective $\\iff$ surjective $\\iff$ invertible</strong>.",
      "<strong>Why:</strong> rank\u2013nullity with $\\dim V=\\dim W$: $\\operatorname{null}T=\\{0\\}$ forces $\\dim\\operatorname{range}T=\\dim V$, so the range is all of $V$ (and conversely).",
      "<strong>Shortcut:</strong> to prove $A$ is invertible, <strong>show only $Ax=0\\Rightarrow x=0$</strong>. Also $ST=I\\Rightarrow TS=I$ for operators: a one-sided inverse is two-sided."
    ],
    "math": "$$T\\in\\mathcal{L}(V),\\ \\dim V<\\infty:\\quad \\operatorname{null}T=\\{0\\}\\iff\\operatorname{range}T=V\\iff T^{-1}\\ \\text{exists}$$",
    "personalConnection": "A full theater where the number of seats equals the number of guests: if no two guests share a seat, no seat is empty.",
    "examTrap": "This FAILS in infinite dimensions (e.g. the right shift is injective but not surjective) and for maps between spaces of different dimension."
  },
  {
    "id": 20404,
    "subject": "LAA",
    "topicId": "04_Invertibility_Isomorphisms_and_Change_of_Basis",
    "topicTitle": "04 \u00b7 Isomorphisms & Change of Basis",
    "cardNumber": "04",
    "category": "CHANGE OF BASIS",
    "highlighterClass": "highlight-purple",
    "title": "Change of Basis & Similarity",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-20404\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"14\" y=\"14\" width=\"78\" height=\"30\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"53.0\" y=\"32.0\" font-size=\"11\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">[v]_B</text><rect x=\"148\" y=\"14\" width=\"78\" height=\"30\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"187.0\" y=\"32.0\" font-size=\"11\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">[v]_{B\u2032}</text><line x1=\"94\" y1=\"29\" x2=\"146\" y2=\"29\" stroke=\"#000000\" stroke-width=\"1.5\" marker-end=\"url(#arr-20404)\"/><text x=\"120\" y=\"22\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">S\u207b\u00b9</text><rect x=\"14\" y=\"78\" width=\"78\" height=\"30\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"53.0\" y=\"96.0\" font-size=\"11\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">[Tv]_B</text><rect x=\"148\" y=\"78\" width=\"78\" height=\"30\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"187.0\" y=\"96.0\" font-size=\"11\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">[Tv]_{B\u2032}</text><line x1=\"53\" y1=\"46\" x2=\"53\" y2=\"76\" stroke=\"#000000\" stroke-width=\"1.5\" marker-end=\"url(#arr-20404)\"/><text x=\"36\" y=\"64\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">A</text><line x1=\"187\" y1=\"46\" x2=\"187\" y2=\"76\" stroke=\"#000000\" stroke-width=\"1.5\" marker-end=\"url(#arr-20404)\"/><text x=\"208\" y=\"64\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">A\u2032</text><line x1=\"94\" y1=\"93\" x2=\"146\" y2=\"93\" stroke=\"#000000\" stroke-width=\"1.5\" marker-end=\"url(#arr-20404)\"/><text x=\"120\" y=\"86\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">S\u207b\u00b9</text><text x=\"120\" y=\"128\" font-size=\"12\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">A\u2032 = S\u207b\u00b9 A S</text><text x=\"120\" y=\"142\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">S = columns are the new basis in old coordinates</text></svg>",
    "drawingCaption": "Go to the new basis, apply the matrix in the old basis, come back: A\u2032 = S\u207b\u00b9AS",
    "coreTranslation": [
      "<strong>Change-of-basis matrix:</strong> if $B'=(b_1',\\dots,b_n')$ and $S$ has these vectors (written in basis $B$) as columns, then $[v]_B=S\\,[v]_{B'}$.",
      "<strong>Operators:</strong> the matrix of the same $T$ in the new basis is $A'=S^{-1}AS$. Matrices related this way are called <strong>similar</strong>.",
      "<strong>Goal of the course:</strong> pick the basis that makes $A'$ as simple as possible (diagonal, Jordan, or orthonormal-diagonal)."
    ],
    "math": "$$[v]_B=S\\,[v]_{B'},\\qquad A'=S^{-1}AS\\ \\ (\\text{operator}),\\qquad A'=Q^{-1}AP\\ \\ (\\text{map, two bases})$$",
    "personalConnection": "Reading a map in kilometers versus miles: the territory is the same, but the numbers you write down change by a fixed conversion.",
    "examTrap": "S has the NEW basis vectors as columns (in old coordinates). Using S instead of S\u207b\u00b9 (or the reverse) is the usual sign error."
  },
  {
    "id": 20405,
    "subject": "LAA",
    "topicId": "04_Invertibility_Isomorphisms_and_Change_of_Basis",
    "topicTitle": "04 \u00b7 Isomorphisms & Change of Basis",
    "cardNumber": "05",
    "category": "CHANGE OF BASIS",
    "highlighterClass": "highlight-cyan",
    "title": "What Similar Matrices Share",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-20405\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"14\" y=\"14\" width=\"100\" height=\"28\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"64.0\" y=\"31.0\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">trace  tr A = tr A\u2032</text><rect x=\"126\" y=\"14\" width=\"100\" height=\"28\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"176.0\" y=\"31.0\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">determinant</text><rect x=\"14\" y=\"52\" width=\"100\" height=\"28\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"64.0\" y=\"69.0\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">eigenvalues</text><rect x=\"126\" y=\"52\" width=\"100\" height=\"28\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"176.0\" y=\"69.0\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">characteristic poly</text><rect x=\"14\" y=\"90\" width=\"100\" height=\"28\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"64.0\" y=\"107.0\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">rank &amp; nullity</text><rect x=\"126\" y=\"90\" width=\"100\" height=\"28\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"176.0\" y=\"107.0\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">min polynomial</text><text x=\"120\" y=\"134\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">invariants of the OPERATOR, not of the basis</text></svg>",
    "drawingCaption": "Everything that describes the operator itself survives a change of basis",
    "coreTranslation": [
      "<strong>Same operator, different clothes:</strong> if $A'=S^{-1}AS$ then $A$ and $A'$ have the same <strong>trace, determinant, rank, eigenvalues (with multiplicity), characteristic and minimal polynomials</strong>.",
      "<strong>Quick proof:</strong> $\\det(\\lambda I-S^{-1}AS)=\\det(S^{-1}(\\lambda I-A)S)=\\det(\\lambda I-A)$, and $\\operatorname{tr}(S^{-1}AS)=\\operatorname{tr}(ASS^{-1})=\\operatorname{tr}A$.",
      "<strong>Use:</strong> to show two matrices are <strong>not</strong> similar, find one invariant that differs. The converse is false in general: equal invariants do not guarantee similarity."
    ],
    "math": "$$A'=S^{-1}AS\\Rightarrow\\ \\operatorname{tr}A'=\\operatorname{tr}A,\\ \\ \\det A'=\\det A,\\ \\ p_{A'}=p_A$$",
    "personalConnection": "Two photos of the same sculpture from different angles: the angles differ, but the sculpture's weight and volume do not.",
    "examTrap": "Same characteristic polynomial does NOT imply similar. [[0,1],[0,0]] and the zero matrix share eigenvalues but have different ranks."
  },
  {
    "id": 20406,
    "subject": "LAA",
    "topicId": "04_Invertibility_Isomorphisms_and_Change_of_Basis",
    "topicTitle": "04 \u00b7 Isomorphisms & Change of Basis",
    "cardNumber": "06",
    "category": "WORKED BENCHMARK",
    "highlighterClass": "highlight-amber",
    "title": "Worked Benchmark: Coordinates in the Basis {(1,1), (1,\u22121)}",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-20406\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"26\" y1=\"72\" x2=\"214\" y2=\"72\" stroke=\"#000000\" stroke-width=\"0.8\" stroke-dasharray=\"2 3\"/><line x1=\"120\" y1=\"12\" x2=\"120\" y2=\"132\" stroke=\"#000000\" stroke-width=\"0.8\" stroke-dasharray=\"2 3\"/><line x1=\"120\" y1=\"72\" x2=\"160\" y2=\"32\" stroke=\"#000000\" stroke-width=\"2.4\" marker-end=\"url(#arr-20406)\"/><line x1=\"120\" y1=\"72\" x2=\"160\" y2=\"112\" stroke=\"#000000\" stroke-width=\"2.4\" marker-end=\"url(#arr-20406)\"/><text x=\"168\" y=\"30\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">b\u2081=(1,1)</text><text x=\"168\" y=\"120\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">b\u2082=(1,\u22121)</text><line x1=\"120\" y1=\"72\" x2=\"200\" y2=\"56\" stroke=\"#000000\" stroke-width=\"2\" stroke-dasharray=\"5 3\" marker-end=\"url(#arr-20406)\"/><text x=\"204\" y=\"54\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"start\" fill=\"#000000\">v=(3,1)</text><text x=\"30\" y=\"22\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">a(1,1)+b(1,\u22121) = (3,1)</text><text x=\"30\" y=\"36\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">a+b=3, a\u2212b=1</text><text x=\"30\" y=\"50\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"start\" fill=\"#000000\">\u21d2 a=2, b=1</text><text x=\"30\" y=\"116\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">S = [[1,1],[1,\u22121]]</text><text x=\"30\" y=\"128\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"start\" fill=\"#000000\">[v]_B = S\u207b\u00b9v = (2, 1)</text></svg>",
    "drawingCaption": "(3,1) = 2\u00b7(1,1) + 1\u00b7(1,\u22121): its coordinates in the new basis are (2, 1)",
    "coreTranslation": [
      "<strong>Basis:</strong> $B=\\{(1,1),(1,-1)\\}$, so $S=\\begin{pmatrix}1&1\\\\1&-1\\end{pmatrix}$ (columns = basis vectors in standard coordinates).",
      "<strong>Solve</strong> $a(1,1)+b(1,-1)=(3,1)$: $a+b=3$ and $a-b=1$, giving <strong>$a=2,\\ b=1$</strong>, so $[v]_B=(2,1)$.",
      "<strong>Check with the matrix:</strong> $S^{-1}=\\tfrac12\\begin{pmatrix}1&1\\\\1&-1\\end{pmatrix}$ and $S^{-1}(3,1)^T=\\tfrac12(4,2)^T=(2,1)^T$ \u2713."
    ],
    "math": "$$[v]_B=S^{-1}v=\\tfrac12\\begin{pmatrix}1&1\\\\1&-1\\end{pmatrix}\\begin{pmatrix}3\\\\1\\end{pmatrix}=\\begin{pmatrix}2\\\\1\\end{pmatrix}$$",
    "personalConnection": "Giving someone directions along the diagonal streets of a city instead of the north-south grid: the same spot, new street names.",
    "examTrap": "To go from standard coordinates to the new basis you apply S\u207b\u00b9 (not S). S converts the other way, from new coordinates to standard."
  },
  {
    "id": 20501,
    "subject": "LAA",
    "topicId": "05_Polynomials_and_Minimal_Polynomial",
    "topicTitle": "05 \u00b7 Polynomials & Minimal Polynomial",
    "cardNumber": "01",
    "category": "POLYNOMIALS OF OPERATORS",
    "highlighterClass": "highlight-cyan",
    "title": "p(T): Plugging an Operator into a Polynomial",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-20501\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"14\" y=\"14\" width=\"100\" height=\"28\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"64.0\" y=\"31.0\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">p(z) = z\u00b2 \u2212 3z + 2</text><line x1=\"114\" y1=\"28\" x2=\"136\" y2=\"28\" stroke=\"#000000\" stroke-width=\"1.5\" marker-end=\"url(#arr-20501)\"/><rect x=\"138\" y=\"14\" width=\"88\" height=\"28\" rx=\"0\" fill=\"#e2e8f0\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"182.0\" y=\"27.0\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">p(T) = T\u00b2</text><text x=\"182.0\" y=\"37.0\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u2212 3T + 2I</text><text x=\"120\" y=\"66\" font-size=\"9.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">p(z) = (z\u22121)(z\u22122)</text><line x1=\"120\" y1=\"72\" x2=\"120\" y2=\"82\" stroke=\"#000000\" stroke-width=\"1.3\" marker-end=\"url(#arr-20501)\"/><text x=\"120\" y=\"96\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">p(T) = (T \u2212 I)(T \u2212 2I) = (T \u2212 2I)(T \u2212 I)</text><text x=\"120\" y=\"116\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">polynomials in ONE operator always commute</text><text x=\"120\" y=\"132\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">constant term c \u21a6 c\u00b7I</text></svg>",
    "drawingCaption": "The factoring identities of ordinary polynomials survive when z is replaced by an operator",
    "coreTranslation": [
      "<strong>Definition:</strong> for $p(z)=a_0+a_1z+\\dots+a_mz^m$ set $p(T)=a_0I+a_1T+\\dots+a_mT^m$ (the constant term becomes $a_0I$).",
      "<strong>Algebra:</strong> $(pq)(T)=p(T)\\,q(T)=q(T)\\,p(T)$, so <strong>polynomials in a single $T$ commute</strong> and factor like numbers.",
      "<strong>Spectral link:</strong> if $Tv=\\lambda v$ then $p(T)v=p(\\lambda)v$: eigenvalues of $p(T)$ are $p(\\lambda)$."
    ],
    "math": "$$p(T)=\\sum a_kT^k,\\quad (pq)(T)=p(T)q(T),\\qquad Tv=\\lambda v\\Rightarrow p(T)v=p(\\lambda)v$$",
    "personalConnection": "Taking a recipe written for numbers and cooking it with a machine instead: the steps compose in the same order and give the same algebra.",
    "examTrap": "Polynomials in the SAME operator commute. Polynomials in two different operators S and T generally do not."
  },
  {
    "id": 20502,
    "subject": "LAA",
    "topicId": "05_Polynomials_and_Minimal_Polynomial",
    "topicTitle": "05 \u00b7 Polynomials & Minimal Polynomial",
    "cardNumber": "02",
    "category": "EIGENVALUE EXISTENCE",
    "highlighterClass": "highlight-amber",
    "title": "Every Complex Operator Has an Eigenvalue",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-20502\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><text x=\"120\" y=\"18\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">dim V = n \u2265 1, \ud835\udd3d = \u2102</text><text x=\"120\" y=\"40\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">v, Tv, T\u00b2v, \u2026, T\u207fv   (n+1 vectors in dim n)</text><line x1=\"120\" y1=\"46\" x2=\"120\" y2=\"58\" stroke=\"#000000\" stroke-width=\"1.3\" marker-end=\"url(#arr-20502)\"/><text x=\"120\" y=\"72\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">dependent \u21d2 a\u2080v + a\u2081Tv + \u2026 + a\u2099T\u207fv = 0</text><line x1=\"120\" y1=\"78\" x2=\"120\" y2=\"90\" stroke=\"#000000\" stroke-width=\"1.3\" marker-end=\"url(#arr-20502)\"/><text x=\"120\" y=\"104\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">p(T)v = 0, p factors over \u2102:</text><text x=\"120\" y=\"118\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">p(z) = c(z\u2212\u03bb\u2081)\u2026(z\u2212\u03bb_m)</text><text x=\"120\" y=\"134\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">some (T \u2212 \u03bb\u2c7cI) is not injective \u21d2 \u03bb\u2c7c is an eigenvalue</text></svg>",
    "drawingCaption": "A dependent list v, Tv, \u2026, T\u207fv forces a factor (T \u2212 \u03bbI) to be non-injective",
    "coreTranslation": [
      "<strong>Theorem:</strong> every operator on a <strong>nonzero finite-dimensional complex</strong> vector space has an eigenvalue.",
      "<strong>Proof:</strong> pick $v\\ne0$; the $n+1$ vectors $v,Tv,\\dots,T^nv$ are dependent, giving a nonzero $p$ with $p(T)v=0$. Factor $p$ over $\\mathbb{C}$ into linear terms.",
      "<strong>Why a product of non-injective maps is non-injective:</strong> $(T-\\lambda_1I)\\cdots(T-\\lambda_mI)$ sends the nonzero $v$ to $0$, so at least one factor has a nonzero null vector: an eigenvector."
    ],
    "math": "$$p(T)v=0,\\ \\ p(z)=c\\prod(z-\\lambda_j)\\ \\Rightarrow\\ \\exists j:\\ T-\\lambda_jI\\ \\text{not injective}$$",
    "personalConnection": "A chain of locked doors that a person walked through: at least one lock must have been open, or they could not have gotten through.",
    "examTrap": "This is false over \u211d (rotation by 90\u00b0 in the plane has no real eigenvalue) and for infinite-dimensional spaces. It needs algebraic closure (\u2102)."
  },
  {
    "id": 20503,
    "subject": "LAA",
    "topicId": "05_Polynomials_and_Minimal_Polynomial",
    "topicTitle": "05 \u00b7 Polynomials & Minimal Polynomial",
    "cardNumber": "03",
    "category": "MINIMAL POLYNOMIAL",
    "highlighterClass": "highlight-emerald",
    "title": "The Minimal Polynomial",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-20503\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><text x=\"120\" y=\"18\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">annihilating polynomials of T:  {p : p(T) = 0}</text><rect x=\"30\" y=\"28\" width=\"180\" height=\"44\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"120\" y=\"48\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">(z\u22121)(z\u22122)(z\u22123)     (z\u22121)\u00b2(z\u22122)(z\u22123)  \u2026</text><text x=\"120\" y=\"64\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">all multiples of the minimal one</text><line x1=\"120\" y1=\"72\" x2=\"120\" y2=\"86\" stroke=\"#000000\" stroke-width=\"1.3\" marker-end=\"url(#arr-20503)\"/><rect x=\"60\" y=\"88\" width=\"120\" height=\"28\" rx=\"0\" fill=\"#e2e8f0\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"120.0\" y=\"101.0\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">min poly q: monic,</text><text x=\"120.0\" y=\"110.5\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">smallest degree</text><text x=\"120\" y=\"134\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">q divides EVERY annihilating polynomial</text></svg>",
    "drawingCaption": "The minimal polynomial is the smallest-degree monic polynomial that kills T, and it divides all others",
    "coreTranslation": [
      "<strong>Definition:</strong> the <strong>minimal polynomial</strong> $q$ of $T$ is the monic polynomial of <strong>least degree</strong> with $q(T)=0$. It exists since $I,T,\\dots,T^{n^2}$ are dependent.",
      "<strong>Divisibility:</strong> if $p(T)=0$ then <strong>$q$ divides $p$</strong> (divide with remainder; the remainder would be a smaller annihilator unless it is $0$).",
      "<strong>Degree bound:</strong> $\\deg q\\le n=\\dim V$ (Cayley\u2013Hamilton) and $q$ is unique."
    ],
    "math": "$$q(T)=0,\\quad q\\ \\text{monic, minimal degree};\\qquad p(T)=0\\iff q\\mid p$$",
    "personalConnection": "The shortest rope that still ties the knot: any longer rope that works must contain the short one.",
    "examTrap": "Minimal polynomial is monic. And p(T) = 0 is an identity of OPERATORS, not of numbers: it does not mean p has T as a root of a scalar equation."
  },
  {
    "id": 20504,
    "subject": "LAA",
    "topicId": "05_Polynomials_and_Minimal_Polynomial",
    "topicTitle": "05 \u00b7 Polynomials & Minimal Polynomial",
    "cardNumber": "04",
    "category": "MINIMAL POLYNOMIAL",
    "highlighterClass": "highlight-purple",
    "title": "Cayley\u2013Hamilton & Roots = Eigenvalues",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-20504\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"14\" y=\"14\" width=\"100\" height=\"34\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"64.0\" y=\"30.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">char poly p_T(\u03bb)</text><text x=\"64.0\" y=\"39.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">= det(\u03bbI \u2212 T)</text><rect x=\"126\" y=\"14\" width=\"100\" height=\"34\" rx=\"0\" fill=\"#e2e8f0\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"176.0\" y=\"34.0\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">min poly q(\u03bb)</text><line x1=\"120\" y1=\"62\" x2=\"120\" y2=\"80\" stroke=\"#000000\" stroke-width=\"1.4\" marker-end=\"url(#arr-20504)\"/><text x=\"120\" y=\"72\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">q | p_T</text><text x=\"120\" y=\"98\" font-size=\"9.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">p_T(T) = 0   (Cayley\u2013Hamilton)</text><text x=\"120\" y=\"114\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">roots of q = roots of p_T = eigenvalues</text><text x=\"120\" y=\"130\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">different multiplicities possible</text></svg>",
    "drawingCaption": "Same roots, but the minimal polynomial may have smaller multiplicities",
    "coreTranslation": [
      "<strong>Cayley\u2013Hamilton:</strong> every operator satisfies its own characteristic polynomial, $p_T(T)=0$, so the minimal polynomial <strong>divides</strong> $p_T$ and $\\deg q\\le n$.",
      "<strong>Roots:</strong> the zeros of $q$ are <strong>exactly the eigenvalues</strong> of $T$ (if $Tv=\\lambda v$ then $q(\\lambda)v=q(T)v=0$; conversely every root is an eigenvalue).",
      "<strong>Difference:</strong> $p_T$ records <strong>algebraic multiplicity</strong> (size of the generalized eigenspace); $q$ records the <strong>largest Jordan block</strong> for each eigenvalue."
    ],
    "math": "$$p_T(T)=0,\\quad q\\mid p_T,\\quad \\{\\text{roots of }q\\}=\\{\\text{eigenvalues}\\}$$",
    "personalConnection": "The full guest list (char poly) versus the shortest invitation that still reaches every distinct guest (min poly).",
    "examTrap": "A matrix can satisfy a polynomial of degree less than n. Do not assume q = p_T. Equality happens for operators with a single Jordan block per eigenvalue."
  },
  {
    "id": 20505,
    "subject": "LAA",
    "topicId": "05_Polynomials_and_Minimal_Polynomial",
    "topicTitle": "05 \u00b7 Polynomials & Minimal Polynomial",
    "cardNumber": "05",
    "category": "MINIMAL POLYNOMIAL",
    "highlighterClass": "highlight-cyan",
    "title": "Diagonalizable \u21d4 Minimal Polynomial Has Distinct Roots",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-20505\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"14\" y=\"20\" width=\"100\" height=\"38\" rx=\"0\" fill=\"#e2e8f0\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"64.0\" y=\"42.0\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">q(z) = (z\u2212\u03bb\u2081)(z\u2212\u03bb\u2082)\u2026</text><text x=\"64\" y=\"74\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">no repeated factors</text><line x1=\"116\" y1=\"39\" x2=\"138\" y2=\"39\" stroke=\"#000000\" stroke-width=\"1.6\" marker-end=\"url(#arr-20505)\"/><rect x=\"140\" y=\"20\" width=\"86\" height=\"38\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"183.0\" y=\"42.0\" font-size=\"9.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">diagonalizable</text><rect x=\"14\" y=\"92\" width=\"100\" height=\"38\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"64.0\" y=\"114.0\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">q(z) = (z\u2212\u03bb)\u00b2\u2026</text><text x=\"64\" y=\"144\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">repeated factor</text><line x1=\"116\" y1=\"111\" x2=\"138\" y2=\"111\" stroke=\"#000000\" stroke-width=\"1.6\" marker-end=\"url(#arr-20505)\"/><rect x=\"140\" y=\"92\" width=\"86\" height=\"38\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"183.0\" y=\"114.0\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">NOT diagonalizable</text></svg>",
    "drawingCaption": "A repeated factor in the minimal polynomial signals a Jordan block and blocks diagonalization",
    "coreTranslation": [
      "<strong>Theorem:</strong> $T$ is diagonalizable $\\iff$ its minimal polynomial has <strong>no repeated roots</strong> (equals $(z-\\lambda_1)\\cdots(z-\\lambda_m)$ with distinct $\\lambda_j$).",
      "<strong>Why:</strong> a squarefree $q$ splits $V$ into the eigenspaces $\\operatorname{null}(T-\\lambda_jI)$; a repeated factor means some vector needs $(T-\\lambda I)^2$ to be killed, i.e. a Jordan chain.",
      "<strong>Shortcut:</strong> if $T$ has $n$ distinct eigenvalues then $q$ has $n$ distinct roots, so $T$ is diagonalizable. If you find a polynomial with distinct roots that annihilates $T$, you're done."
    ],
    "math": "$$T\\ \\text{diagonalizable}\\iff q(z)=\\prod_{j=1}^{m}(z-\\lambda_j)\\ \\text{(distinct }\\lambda_j)$$",
    "personalConnection": "A team where each job has exactly one owner is easy to split; a job that needs a chain of two people in sequence cannot be handed out in parallel.",
    "examTrap": "It is the MINIMAL polynomial, not the characteristic one, that must be squarefree. The char poly can have repeated roots and the operator can still be diagonalizable (e.g. I)."
  },
  {
    "id": 20506,
    "subject": "LAA",
    "topicId": "05_Polynomials_and_Minimal_Polynomial",
    "topicTitle": "05 \u00b7 Polynomials & Minimal Polynomial",
    "cardNumber": "06",
    "category": "WORKED BENCHMARK",
    "highlighterClass": "highlight-amber",
    "title": "Worked Benchmark: [[2,1],[0,2]] vs 2I",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-20506\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"14\" y=\"18\" width=\"30\" height=\"30\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.1\"/><text x=\"29.0\" y=\"36.0\" font-size=\"12\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">2</text><rect x=\"44\" y=\"18\" width=\"30\" height=\"30\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.1\"/><text x=\"59.0\" y=\"36.0\" font-size=\"12\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">1</text><rect x=\"14\" y=\"48\" width=\"30\" height=\"30\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.1\"/><text x=\"29.0\" y=\"66.0\" font-size=\"12\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">0</text><rect x=\"44\" y=\"48\" width=\"30\" height=\"30\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.1\"/><text x=\"59.0\" y=\"66.0\" font-size=\"12\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">2</text><text x=\"44\" y=\"94\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">A</text><rect x=\"110\" y=\"18\" width=\"30\" height=\"30\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.1\"/><text x=\"125.0\" y=\"36.0\" font-size=\"12\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">2</text><rect x=\"140\" y=\"18\" width=\"30\" height=\"30\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.1\"/><text x=\"155.0\" y=\"36.0\" font-size=\"12\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">0</text><rect x=\"110\" y=\"48\" width=\"30\" height=\"30\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.1\"/><text x=\"125.0\" y=\"66.0\" font-size=\"12\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">0</text><rect x=\"140\" y=\"48\" width=\"30\" height=\"30\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.1\"/><text x=\"155.0\" y=\"66.0\" font-size=\"12\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">2</text><text x=\"140\" y=\"94\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">2I</text><text x=\"20\" y=\"112\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">p_A = (z\u22122)\u00b2</text><text x=\"20\" y=\"126\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"start\" fill=\"#000000\">A \u2212 2I \u2260 0 \u21d2 q = (z\u22122)\u00b2</text><text x=\"112\" y=\"112\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">p = (z\u22122)\u00b2</text><text x=\"112\" y=\"126\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"start\" fill=\"#000000\">2I \u2212 2I = 0 \u21d2 q = z\u22122</text><text x=\"210\" y=\"40\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">A: Jordan block</text><text x=\"210\" y=\"52\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">not diagonal.</text><text x=\"210\" y=\"78\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">2I: already</text><text x=\"210\" y=\"90\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">diagonal</text></svg>",
    "drawingCaption": "Same characteristic polynomial (z\u22122)\u00b2, but different minimal polynomials and different behavior",
    "coreTranslation": [
      "<strong>Both</strong> matrices have characteristic polynomial $(z-2)^2$ and the single eigenvalue $2$.",
      "<strong>For $A$:</strong> $A-2I=\\begin{pmatrix}0&1\\\\0&0\\end{pmatrix}\\ne0$, but $(A-2I)^2=0$, so the minimal polynomial is $\\mathbf{(z-2)^2}$, which has a repeated root: <strong>$A$ is not diagonalizable</strong>.",
      "<strong>For $2I$:</strong> $2I-2I=0$ already, so the minimal polynomial is $\\mathbf{z-2}$ (squarefree): <strong>diagonalizable</strong> (it is diagonal)."
    ],
    "math": "$$(A-2I)^2=\\begin{pmatrix}0&1\\\\0&0\\end{pmatrix}^{2}=0\\ \\Rightarrow\\ q_A=(z-2)^2,\\qquad q_{2I}=z-2$$",
    "personalConnection": "Two clocks with the same number of gears (char poly) but one has gears that must turn in sequence (a chain) while the other's all run independently.",
    "examTrap": "Equal characteristic polynomials do not mean similar. The minimal polynomial (or Jordan structure) is what distinguishes A from 2I."
  }
]);
