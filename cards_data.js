/* Master Multi-Subject Cards Database for CMO, LAA, StoMA, DIP */
window.MASTER_CARDS_DATA = [
  {
    "id": 101,
    "subject": "CMO",
    "topicId": "01_Mathematical_Preliminaries_Topology_and_Weierstrass",
    "topicTitle": "01 \u00b7 Mathematical Preliminaries & Weierstrass",
    "cardNumber": "01",
    "category": "TOPOLOGY & METRIC SPACES",
    "highlighterClass": "highlight-cyan",
    "title": "Open, Closed & Bounded Sets (Heine-Borel)",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-101\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"80\" y1=\"8\" x2=\"80\" y2=\"138\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"3 3\"/><line x1=\"160\" y1=\"8\" x2=\"160\" y2=\"138\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"3 3\"/><rect x=\"14\" y=\"40\" width=\"52\" height=\"44\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"2.2\"/><g transform=\"translate(40.0 62.0) rotate(0) scale(0.7)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.71\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"40\" y=\"98\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">fenced + gate</text><text x=\"40\" y=\"110\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">compact \u2713</text><line x1=\"92.0\" y1=\"62.0\" x2=\"148.0\" y2=\"62.0\" stroke=\"#000000\" stroke-width=\"2.4\" marker-end=\"url(#arr-101)\"/><line x1=\"92\" y1=\"62\" x2=\"148\" y2=\"62\" stroke=\"#000000\" stroke-width=\"2.4\"/><line x1=\"92\" y1=\"54\" x2=\"92\" y2=\"70\" stroke=\"#000000\" stroke-width=\"2\"/><text x=\"120\" y=\"90\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">endless runway</text><text x=\"120\" y=\"102\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">closed, unbounded</text><line x1=\"176\" y1=\"40\" x2=\"226\" y2=\"40\" stroke=\"#000000\" stroke-width=\"2.2\"/><line x1=\"226\" y1=\"40\" x2=\"226\" y2=\"84\" stroke=\"#000000\" stroke-width=\"2.2\"/><line x1=\"226\" y1=\"84\" x2=\"176\" y2=\"84\" stroke=\"#000000\" stroke-width=\"2.2\"/><line x1=\"176\" y1=\"84\" x2=\"176\" y2=\"56\" stroke=\"#000000\" stroke-width=\"2.2\" stroke-dasharray=\"3 3\"/><g transform=\"translate(200.0 62.0) rotate(0) scale(0.6)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.00\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"194.4\" y=\"100\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">missing fence boards</text><text x=\"196.48\" y=\"112\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">bounded, not closed</text></svg>",
    "drawingCaption": "Left: a fenced airfield with a locked gate (closed and bounded = compact). Middle: an endless runway (closed, unbounded). Right: fence boards missing (bounded, not closed).",
    "coreTranslation": [
      "An <strong>Open Set $S \\subset \\mathbb{R}^n$</strong> contains an open ball $B_\\epsilon(x) = \\{y : \\|y-x\\| < \\epsilon\\} \\subset S$ around every interior point.",
      "A <strong>Closed Set</strong> contains all of its boundary limit points: if a sequence $x_k \\in S \\to x^*$, the limit point $x^* \\in S$ must belong to $S$.",
      "<strong>Heine-Borel Theorem:</strong> In Euclidean space $\\mathbb{R}^n$, a subset $K$ is <strong>compact</strong> if and only if it is simultaneously <strong>closed and bounded</strong>."
    ],
    "math": "$$K \\subset \\mathbb{R}^n \\text{ is compact} \\iff K \\text{ is closed and bounded}$$",
    "personalConnection": "<strong>The airplane analogy.</strong> A fenced airfield with a locked gate is compact: closed (its boundary belongs to it) and bounded (finite size). An endless runway is closed but unbounded, and an airfield with missing fence boards is bounded but not closed.",
    "examTrap": "Heine-Borel strictly fails in infinite dimensions! In infinite-dimensional function spaces (such as $L^2$ or Sobolev spaces), a closed and bounded unit ball is NEVER compact.",
    "hint": "Which two properties must the airfield have so the lowest point can actually be reached?",
    "breakdown": [
      "<strong>Closed = the fence belongs to the airfield,</strong> so a plane heading for the boundary can really land on it.",
      "<strong>Bounded = a finite size,</strong> so the search cannot run off to infinity.",
      "<strong>Heine-Borel:</strong> in $\\mathbb R^n$ these two together are exactly compactness, the property Weierstrass needs."
    ]
  },
  {
    "id": 102,
    "subject": "CMO",
    "topicId": "01_Mathematical_Preliminaries_Topology_and_Weierstrass",
    "topicTitle": "01 \u00b7 Mathematical Preliminaries & Weierstrass",
    "cardNumber": "02",
    "category": "FUNCTIONAL ANALYSIS",
    "highlighterClass": "highlight-emerald",
    "title": "Lower Semicontinuity & Sublevel Sets",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-102\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"20\" y1=\"130\" x2=\"226\" y2=\"130\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-102)\"/><line x1=\"30\" y1=\"52\" x2=\"120\" y2=\"52\" stroke=\"#000000\" stroke-width=\"2.6\"/><line x1=\"120\" y1=\"88\" x2=\"214\" y2=\"88\" stroke=\"#000000\" stroke-width=\"2.6\"/><line x1=\"120.0\" y1=\"52.0\" x2=\"120.0\" y2=\"88.0\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"2 2\"/><circle cx=\"120.0\" cy=\"88.0\" r=\"3.2\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><circle cx=\"120.0\" cy=\"52.0\" r=\"3.2\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.5\"/><g transform=\"translate(70.0 38.0) rotate(0) scale(0.65)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.85\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><g transform=\"translate(176.0 76.0) rotate(0) scale(0.65)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.85\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"120\" y=\"112\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">cliff: altimeter reads the lower height</text><text x=\"140.32\" y=\"40\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">closed dot = true value</text></svg>",
    "drawingCaption": "At a cliff edge the altimeter reports the lower of the two heights (filled dot), so a plane landing there touches real ground.",
    "coreTranslation": [
      "A function $f: \\mathbb{R}^n \\to \\mathbb{R}$ is <strong>Lower Semicontinuous (LSC)</strong> if at every point $x_0$, $\\liminf_{x \\to x_0} f(x) \\ge f(x_0)$. It can jump downward, but never jump upward.",
      "<strong>Sublevel Set Equivalence:</strong> $f$ is LSC if and only if for every scalar threshold $\\alpha \\in \\mathbb{R}$, the sublevel set $\\mathcal{L}_\\alpha(f) = \\{x \\in \\mathbb{R}^n : f(x) \\le \\alpha\\}$ is <strong>closed</strong>.",
      "Lower semicontinuity is the exact mathematical property needed to preserve minima: limits of minimizing sequences stay within closed sublevel sets."
    ],
    "math": "$$\\liminf_{x \\to x_0} f(x) \\ge f(x_0) \\iff \\mathcal{L}_\\alpha(f) = \\{x : f(x) \\le \\alpha\\} \\text{ is closed } \\forall \\alpha$$",
    "personalConnection": "<strong>The airplane analogy.</strong> At a cliff edge the altimeter reports the lower of the two heights, so a plane approaching from above still lands on the true low point and never falls through an imaginary floor.",
    "examTrap": "Full continuity is NOT required for minimum attainment! Lower semicontinuity is the exact minimal condition needed for global infimum attainment. Upper semicontinuity guarantees maximum attainment.",
    "hint": "What does the altimeter read at a cliff edge, and why does that keep the lowest point reachable?",
    "breakdown": [
      "<strong>$\\liminf_{x\\to x_0}f(x)\\ge f(x_0)$:</strong> the value at the edge is at or below everything you approach it with, so the true value sits on the low side of any jump.",
      "<strong>Sublevel sets $\\{f\\le\\alpha\\}$:</strong> the region at or below altitude $\\alpha$; being closed means the boundary of that region is landable.",
      "<strong>The two statements are equivalent:</strong> jumps downward are allowed, jumps upward (a hole in the floor) are not."
    ]
  },
  {
    "id": 103,
    "subject": "CMO",
    "topicId": "01_Mathematical_Preliminaries_Topology_and_Weierstrass",
    "topicTitle": "01 \u00b7 Mathematical Preliminaries & Weierstrass",
    "cardNumber": "03",
    "category": "OPTIMIZATION FOUNDATIONS",
    "highlighterClass": "highlight-amber",
    "title": "Weierstrass Extreme Value Theorem",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-103\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"40.0\" y1=\"18.0\" x2=\"40.0\" y2=\"130.0\" stroke=\"#000000\" stroke-width=\"2.4\"/><line x1=\"40.0\" y1=\"25.0\" x2=\"35.0\" y2=\"25.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"40.0\" y1=\"39.0\" x2=\"35.0\" y2=\"39.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"40.0\" y1=\"53.0\" x2=\"35.0\" y2=\"53.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"40.0\" y1=\"67.0\" x2=\"35.0\" y2=\"67.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"40.0\" y1=\"81.0\" x2=\"35.0\" y2=\"81.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"40.0\" y1=\"95.0\" x2=\"35.0\" y2=\"95.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"40.0\" y1=\"109.0\" x2=\"35.0\" y2=\"109.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"40.0\" y1=\"123.0\" x2=\"35.0\" y2=\"123.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"200.0\" y1=\"18.0\" x2=\"200.0\" y2=\"130.0\" stroke=\"#000000\" stroke-width=\"2.4\"/><line x1=\"200.0\" y1=\"25.0\" x2=\"205.0\" y2=\"25.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"200.0\" y1=\"39.0\" x2=\"205.0\" y2=\"39.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"200.0\" y1=\"53.0\" x2=\"205.0\" y2=\"53.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"200.0\" y1=\"67.0\" x2=\"205.0\" y2=\"67.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"200.0\" y1=\"81.0\" x2=\"205.0\" y2=\"81.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"200.0\" y1=\"95.0\" x2=\"205.0\" y2=\"95.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"200.0\" y1=\"109.0\" x2=\"205.0\" y2=\"109.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"200.0\" y1=\"123.0\" x2=\"205.0\" y2=\"123.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><path d=\"M40.0,78.0 L42.0,77.7 L44.0,77.5 L46.0,77.6 L48.0,77.9 L50.0,78.7 L52.0,79.8 L54.0,81.5 L56.0,83.5 L58.0,86.1 L60.0,89.0 L62.0,92.2 L64.0,95.6 L66.0,99.1 L68.0,102.5 L70.0,105.7 L72.0,108.7 L74.0,111.1 L76.0,113.0 L78.0,114.3 L80.0,114.8 L82.0,114.5 L84.0,113.5 L86.0,111.6 L88.0,109.1 L90.0,105.8 L92.0,102.1 L94.0,97.8 L96.0,93.3 L98.0,88.7 L100.0,84.0 L102.0,79.4 L104.0,75.2 L106.0,71.3 L108.0,67.8 L110.0,65.0 L112.0,62.7 L114.0,61.1 L116.0,60.0 L118.0,59.5 L120.0,59.5 L122.0,59.9 L124.0,60.6 L126.0,61.5 L128.0,62.5 L130.0,63.4 L132.0,64.2 L134.0,64.7 L136.0,64.9 L138.0,64.8 L140.0,64.3 L142.0,63.4 L144.0,62.2 L146.0,60.7 L148.0,58.9 L150.0,57.1 L152.0,55.3 L154.0,53.6 L156.0,52.2 L158.0,51.1 L160.0,50.5 L162.0,50.5 L164.0,51.1 L166.0,52.4 L168.0,54.4 L170.0,57.1 L172.0,60.4 L174.0,64.3 L176.0,68.6 L178.0,73.3 L180.0,78.3 L182.0,83.3 L184.0,88.2 L186.0,92.9 L188.0,97.2 L190.0,101.1 L192.0,104.3 L194.0,106.9 L196.0,108.8 L198.0,109.9 L200.0,110.3\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.6\"/><g transform=\"translate(76.0 94.8) rotate(0) scale(0.6)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.00\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><circle cx=\"80.0\" cy=\"114.8\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"88\" y=\"118.8\" font-size=\"8.5\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">lowest \u2713</text><circle cx=\"161.0\" cy=\"50.4\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"161\" y=\"42.4\" font-size=\"8.5\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">peak</text><text x=\"120\" y=\"12\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">continuous terrain over a fenced airfield</text><text x=\"120\" y=\"142\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">always has a lowest point you can touch</text></svg>",
    "drawingCaption": "A continuous terrain over a fenced, finite airfield always has a lowest point the plane can touch down on (and a highest peak).",
    "coreTranslation": [
      "<strong>Theorem:</strong> Let $K \\subset \\mathbb{R}^n$ be non-empty and <strong>compact</strong> (closed & bounded), and let $f: K \\to \\mathbb{R}$ be <strong>continuous</strong> (or lower semicontinuous). Then $f$ attains its global minimum and maximum.",
      "<strong>Proof Engine:</strong> The continuous image $f(K) \\subset \\mathbb{R}$ is compact, hence closed and bounded. Since $f(K)$ is bounded below, infimum $m = \\inf_{x \\in K} f(x)$ exists and is finite. Since $f(K)$ is closed, $m \\in f(K)$, so $\\exists x^* \\in K$ with $f(x^*) = m$.",
      "This converts an abstract theoretical infimum $\\inf f(x)$ into an exact, physically reachable minimizer $\\min f(x) = f(x^*)$."
    ],
    "math": "$$K \\ne \\emptyset \\text{ compact, } f \\in C(K) \\implies \\exists x^* \\in K : f(x^*) = \\min_{x \\in K} f(x)$$",
    "personalConnection": "<strong>The airplane analogy.</strong> A continuous terrain over a fenced, finite airfield always has a lowest point the plane can actually touch down on, rather than tapering off toward infinity.",
    "examTrap": "If the domain is open (e.g. $K = (0, 1)$), $f(x) = x$ has infimum 0, but attains NO minimum in $K$! Both closedness and boundedness of the domain are strictly mandatory.",
    "hint": "What two conditions guarantee the pilot a lowest point he can actually touch down on?",
    "breakdown": [
      "<strong>$K$ compact:</strong> the airfield is fenced (closed) and finite (bounded).",
      "<strong>$f$ continuous:</strong> no cliffs or holes in the terrain.",
      "<strong>Conclusion:</strong> a lowest point $x^*$ exists inside $K$, so a search over the airfield cannot come up empty."
    ]
  },
  {
    "id": 104,
    "subject": "CMO",
    "topicId": "01_Mathematical_Preliminaries_Topology_and_Weierstrass",
    "topicTitle": "01 \u00b7 Mathematical Preliminaries & Weierstrass",
    "cardNumber": "04",
    "category": "UNCONSTRAINED OPTIMIZATION",
    "highlighterClass": "highlight-violet",
    "title": "Coercivity & Sublevel Compactness",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-104\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><path d=\"M28.0,32.0 L32.6,39.8 L37.2,47.2 L41.8,54.2 L46.4,60.8 L51.0,67.0 L55.6,72.8 L60.2,78.2 L64.8,83.2 L69.4,87.8 L74.0,92.0 L78.6,95.8 L83.2,99.2 L87.8,102.2 L92.4,104.8 L97.0,107.0 L101.6,108.8 L106.2,110.2 L110.8,111.2 L115.4,111.8 L120.0,112.0 L124.6,111.8 L129.2,111.2 L133.8,110.2 L138.4,108.8 L143.0,107.0 L147.6,104.8 L152.2,102.2 L156.8,99.2 L161.4,95.8 L166.0,92.0 L170.6,87.8 L175.2,83.2 L179.8,78.2 L184.4,72.8 L189.0,67.0 L193.6,60.8 L198.2,54.2 L202.8,47.2 L207.4,39.8 L212.0,32.0\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.6\"/><line x1=\"28.0\" y1=\"40.0\" x2=\"28.0\" y2=\"18.0\" stroke=\"#000000\" stroke-width=\"2\" marker-end=\"url(#arr-104)\"/><line x1=\"212.0\" y1=\"40.0\" x2=\"212.0\" y2=\"18.0\" stroke=\"#000000\" stroke-width=\"2\" marker-end=\"url(#arr-104)\"/><g transform=\"translate(120.0 98.0) rotate(0) scale(0.75)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.60\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"120\" y=\"16\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">walls rise without limit</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">the lowest point cannot be far away</text><line x1=\"54.0\" y1=\"62.0\" x2=\"186.0\" y2=\"62.0\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"4 3\"/><text x=\"120\" y=\"58\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">sublevel set</text></svg>",
    "drawingCaption": "The terrain rises without limit in every direction: the lowest point cannot be far away, so the sublevel fence (dashed) is finite.",
    "coreTranslation": [
      "In unconstrained optimization on $\\mathbb{R}^n$, the domain is unbounded, so Weierstrass theorem cannot be applied directly.",
      "<strong>Coercivity:</strong> $f: \\mathbb{R}^n \\to \\mathbb{R}$ is coercive if $\\lim_{\\|x\\| \\to \\infty} f(x) = +\\infty$. As you escape toward infinity in any radial direction, the objective blows up.",
      "<strong>Compactness Recovery:</strong> Pick any basepoint $x_0$. The sublevel set $S = \\{x : f(x) \\le f(x_0)\\}$ is <strong>bounded</strong> and closed, hence <strong>compact</strong>. Applying Weierstrass on $S$ guarantees global minimizer $x^*$ exists on all of $\\mathbb{R}^n$!"
    ],
    "math": "$$\\lim_{\\|x\\| \\to \\infty} f(x) = +\\infty \\implies \\mathcal{L}_\\alpha = \\{x : f(x) \\le \\alpha\\} \\text{ is compact} \\implies \\min_{x \\in \\mathbb{R}^n} f(x) \\text{ exists}$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Mountain walls rise without limit in every direction around the airport, so the lowest altitude cannot be far away: the plane never has to search to infinity.",
    "examTrap": "A function strictly bounded below by zero (like $f(x) = e^{-x^2}$ or $f(x) = \\frac{1}{1+x^2}$) is NOT coercive! It has infimum 0, but attains NO minimum anywhere on $\\mathbb{R}$.",
    "hint": "Why can the pilot stop worrying about searching to infinity when the walls rise forever?",
    "breakdown": [
      "<strong>$f(x)\\to+\\infty$ as $\\|x\\|\\to\\infty$:</strong> far from the airport every direction is a mountain wall.",
      "<strong>The sublevel set $\\{f\\le\\alpha\\}$ is therefore bounded and closed:</strong> a fenced, finite airfield.",
      "<strong>Then Weierstrass applies inside it:</strong> the lowest point exists in all of $\\mathbb R^n$."
    ]
  },
  {
    "id": 105,
    "subject": "CMO",
    "topicId": "01_Mathematical_Preliminaries_Topology_and_Weierstrass",
    "topicTitle": "01 \u00b7 Mathematical Preliminaries & Weierstrass",
    "cardNumber": "05",
    "category": "CONVEX ANALYSIS",
    "highlighterClass": "highlight-indigo",
    "title": "Epigraph & Convexity Geometry",
    "textbookImg": "assets/luenberger_fig7_5.png",
    "textbookRef": "Luenberger & Ye (4th ed), Sect. 7.6, Fig. 7.5 (p. 204)",
    "drawingCaption": "The sky above a convex terrain is the epigraph: any straight flight path between two points in it stays in the sky.",
    "coreTranslation": [
      "The <strong>Epigraph</strong> of $f$ is the set of all points lying on or above its graph in $\\mathbb{R}^{n+1}$: $\\operatorname{epi}(f) = \\{(x, t) \\in \\mathbb{R}^n \\times \\mathbb{R} : f(x) \\le t\\}$.",
      "<strong>Fundamental Geometric Bridge:</strong> A function $f$ is a <strong>convex function</strong> if and only if its epigraph $\\operatorname{epi}(f)$ is a <strong>convex set</strong>.",
      "Horizontal slices of $\\operatorname{epi}(f)$ at height $t = \\alpha$ are precisely the sublevel sets $\\mathcal{L}_\\alpha(f)$. If $f$ is convex, all its sublevel sets are convex."
    ],
    "math": "$$\\operatorname{epi}(f) = \\{(x, t) \\in \\mathbb{R}^{n+1} : f(x) \\le t\\}, \\quad f \\text{ is convex} \\iff \\operatorname{epi}(f) \\text{ is a convex set}$$",
    "personalConnection": "<strong>The airplane analogy.</strong> The sky above the terrain is the epigraph. If the terrain is convex then any straight flight path between two points in that sky stays in the sky.",
    "examTrap": "The converse does NOT hold! A function with convex sublevel sets is NOT necessarily convex (it is only quasiconvex, e.g. $f(x) = \\sqrt{|x|}$ or $f(x) = \\log(x)$).",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-105\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><path d=\"M28.0,12.0 L28.0,23.1 L36.0,37.9 L44.0,51.4 L52.0,63.4 L60.0,74.2 L68.0,83.6 L76.0,91.7 L84.0,98.4 L92.0,103.8 L100.0,107.8 L108.0,110.5 L116.0,111.8 L124.0,111.8 L132.0,110.5 L140.0,107.8 L148.0,103.8 L156.0,98.4 L164.0,91.7 L172.0,83.6 L180.0,74.2 L188.0,63.4 L196.0,51.4 L204.0,37.9 L212.0,23.1 L212.0,12.0\" fill=\"#e5e7eb\" stroke=\"#000000\" stroke-width=\"0.8\"/><path d=\"M28.0,23.1 L32.6,31.8 L37.2,40.0 L41.8,47.8 L46.4,55.1 L51.0,62.0 L55.6,68.5 L60.2,74.5 L64.8,80.0 L69.4,85.1 L74.0,89.8 L78.6,94.0 L83.2,97.8 L87.8,101.1 L92.4,104.0 L97.0,106.4 L101.6,108.4 L106.2,110.0 L110.8,111.1 L115.4,111.8 L120.0,112.0 L124.6,111.8 L129.2,111.1 L133.8,110.0 L138.4,108.4 L143.0,106.4 L147.6,104.0 L152.2,101.1 L156.8,97.8 L161.4,94.0 L166.0,89.8 L170.6,85.1 L175.2,80.0 L179.8,74.5 L184.4,68.5 L189.0,62.0 L193.6,55.1 L198.2,47.8 L202.8,40.0 L207.4,31.8 L212.0,23.1\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.6\"/><circle cx=\"60.0\" cy=\"74.2\" r=\"2.8\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><circle cx=\"180.0\" cy=\"74.2\" r=\"2.8\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><line x1=\"60.0\" y1=\"74.2\" x2=\"180.0\" y2=\"74.2\" stroke=\"#000000\" stroke-width=\"1.6\" stroke-dasharray=\"5 3\"/><g transform=\"translate(120.0 52.0) rotate(0) scale(0.7)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.71\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"120\" y=\"134\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">the sky above the terrain (epigraph)</text><text x=\"120\" y=\"144\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">straight flight paths stay in the sky</text></svg>",
    "hint": "What region is the epigraph, and how does it show whether the terrain is convex?",
    "breakdown": [
      "<strong>$\\operatorname{epi}(f)=\\{(x,t):f(x)\\le t\\}$</strong> is all the sky on or above the terrain, with height $t$ as the extra coordinate.",
      "<strong>Convex terrain $\\iff$ convex sky:</strong> any straight flight path between two points in that sky stays in it.",
      "<strong>Why it matters:</strong> it turns a statement about a function into a statement about a set, where separating hyperplanes work."
    ]
  },
  {
    "id": 106,
    "subject": "CMO",
    "topicId": "01_Mathematical_Preliminaries_Topology_and_Weierstrass",
    "topicTitle": "01 \u00b7 Mathematical Preliminaries & Weierstrass",
    "cardNumber": "06",
    "category": "WORKED BENCHMARK",
    "highlighterClass": "highlight-rose",
    "title": "Worked Benchmark: Coercivity Proof",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-106\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><path d=\"M50.0,68.4 L51.8,73.6 L53.5,78.3 L55.2,82.2 L57.0,85.6 L58.8,88.5 L60.5,90.8 L62.2,92.7 L64.0,94.1 L65.8,95.1 L67.5,95.7 L69.2,96.0 L71.0,96.0 L72.8,95.7 L74.5,95.1 L76.2,94.4 L78.0,93.4 L79.8,92.3 L81.5,91.0 L83.2,89.7 L85.0,88.2 L86.8,86.7 L88.5,85.1 L90.2,83.5 L92.0,81.9 L93.8,80.3 L95.5,78.7 L97.2,77.1 L99.0,75.7 L100.8,74.2 L102.5,72.9 L104.2,71.7 L106.0,70.5 L107.8,69.5 L109.5,68.6 L111.2,67.8 L113.0,67.2 L114.8,66.7 L116.5,66.3 L118.2,66.1 L120.0,66.0 L121.8,66.1 L123.5,66.3 L125.2,66.7 L127.0,67.2 L128.8,67.8 L130.5,68.6 L132.2,69.5 L134.0,70.5 L135.8,71.7 L137.5,72.9 L139.2,74.2 L141.0,75.7 L142.8,77.1 L144.5,78.7 L146.2,80.3 L148.0,81.9 L149.8,83.5 L151.5,85.1 L153.2,86.7 L155.0,88.2 L156.8,89.7 L158.5,91.0 L160.2,92.3 L162.0,93.4 L163.8,94.4 L165.5,95.1 L167.2,95.7 L169.0,96.0 L170.8,96.0 L172.5,95.7 L174.2,95.1 L176.0,94.1 L177.8,92.7 L179.5,90.8 L181.2,88.5 L183.0,85.6 L184.8,82.2 L186.5,78.3 L188.2,73.6 L190.0,68.4\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.6\"/><line x1=\"26.0\" y1=\"96.0\" x2=\"214.0\" y2=\"96.0\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"4 3\"/><line x1=\"50\" y1=\"20\" x2=\"50\" y2=\"130\" stroke=\"#000000\" stroke-width=\"1.6\"/><line x1=\"190\" y1=\"20\" x2=\"190\" y2=\"130\" stroke=\"#000000\" stroke-width=\"1.6\"/><g transform=\"translate(120.0 46.0) rotate(0) scale(0.6)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.00\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><circle cx=\"70.0\" cy=\"96.0\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"68\" y=\"112.0\" font-size=\"8.5\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">(\u22121,\u22121)</text><circle cx=\"170.0\" cy=\"96.0\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"172\" y=\"112.0\" font-size=\"8.5\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">(1,1)</text><circle cx=\"120.0\" cy=\"66.0\" r=\"2.6\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"138\" y=\"70.0\" font-size=\"8.5\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">saddle</text><text x=\"120\" y=\"12\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">coercive: build a fence, search inside</text><text x=\"120\" y=\"142\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">global minimum \u22122 at \u00b1(1,1)</text></svg>",
    "drawingCaption": "The terrain along the diagonal x\u2081=x\u2082 is a double well with its two lowest points at \u00b1(1,1) (altitude \u22122) and a saddle at the origin; the fence encloses both.",
    "coreTranslation": [
      "<strong>What:</strong> show that $f(x_1,x_2)=x_1^4+x_2^4-4x_1x_2$ has a global minimum on all of $\\mathbb{R}^2$ (not only on a closed box).",
      "<strong>How:</strong> (1) <em>Coercive:</em> since $4|x_1x_2|\\le2(x_1^2+x_2^2)$, we get $f\\ge x_1^4+x_2^4-2(x_1^2+x_2^2)\\to+\\infty$ as $\\|x\\|\\to\\infty$. (2) <em>Fence it in:</em> take the base point $(0,0)$, where $f=0$; the set $S=\\{f\\le0\\}$ is closed and bounded, so compact. (3) <em>Weierstrass</em> on $S$ gives a minimizer, and it is global because $f>0$ outside $S$.",
      "<strong>Why / where it is:</strong> setting $\\nabla f=0$ gives $x_1^3=x_2$ and $x_2^3=x_1$, so the candidates are $(0,0)$ with $f=0$ (a saddle) and $\\pm(1,1)$ with $f=-2$. The global minimum is $-2$ at $(1,1)$ <em>and</em> $(-1,-1)$ only (note $f(1,-1)=6$)."
    ],
    "math": "$$f(x)\\ge x_1^4+x_2^4-2(x_1^2+x_2^2)\\to\\infty\\ \\Rightarrow\\ \\text{a global min exists;}\\quad \\min f=f(1,1)=f(-1,-1)=-2$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Build the fence first: coercivity says the terrain outside a large enough fence is higher than your starting altitude, so searching inside the fence cannot miss the lowest point.",
    "examTrap": "Solving \u2207f = 0 does not prove a minimum exists, and the candidates need checking: only (1,1) and (\u22121,\u22121) are global minimizers here. (1,\u22121) and (\u22121,1) are NOT, since f = 6 there.",
    "hint": "How do you prove a lowest point exists on all of the plane when the airfield has no fence?",
    "breakdown": [
      "<strong>The bound $4|x_1x_2|\\le2(x_1^2+x_2^2)$</strong> shows $f\\ge x_1^4+x_2^4-2(x_1^2+x_2^2)$, which rises without limit: $f$ is coercive.",
      "<strong>Coercive means the lowest point is inside some finite fence,</strong> so Weierstrass guarantees a global minimum.",
      "<strong>Setting $\\nabla f=0$</strong> gives the candidates $(0,0)$ (a saddle, $f=0$) and $\\pm(1,1)$ with $f=-2$: the true lowest points."
    ]
  },
  {
    "id": 201,
    "subject": "CMO",
    "topicId": "02_Multivariate_Taylor_Series_and_Optimality_Conditions",
    "topicTitle": "02 \u00b7 Multivariate Taylor Series & Optimality",
    "cardNumber": "01",
    "category": "MULTIVARIATE CALCULUS",
    "highlighterClass": "highlight-cyan",
    "title": "Multivariate Taylor Theorem",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-201\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><path d=\"M20.0,60.0 L23.4,60.0 L26.9,60.0 L30.3,60.1 L33.7,60.1 L37.2,60.1 L40.6,60.2 L44.0,60.3 L47.5,60.4 L50.9,60.6 L54.3,60.8 L57.8,61.2 L61.2,61.6 L64.6,62.1 L68.1,62.7 L71.5,63.5 L74.9,64.5 L78.4,65.7 L81.8,67.0 L85.2,68.6 L88.7,70.3 L92.1,72.2 L95.5,74.3 L99.0,76.4 L102.4,78.6 L105.8,80.8 L109.3,82.9 L112.7,84.9 L116.1,86.6 L119.6,88.0 L123.0,89.1 L126.4,89.8 L129.9,90.0 L133.3,89.8 L136.7,89.2 L140.2,88.1 L143.6,86.7 L147.0,85.0 L150.5,83.1 L153.9,81.0 L157.3,78.8 L160.8,76.6 L164.2,74.4 L167.6,72.4 L171.1,70.5 L174.5,68.7 L177.9,67.1 L181.4,65.8 L184.8,64.6 L188.2,63.6 L191.7,62.8 L195.1,62.1 L198.5,61.6 L202.0,61.2 L205.4,60.9 L208.8,60.6 L212.3,60.4 L215.7,60.3 L219.1,60.2 L222.6,60.1 L226.0,60.1\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.6\"/><line x1=\"50\" y1=\"45.04320086296832\" x2=\"150\" y2=\"109.14376862088704\" stroke=\"#000000\" stroke-width=\"1.5\" stroke-dasharray=\"5 3\"/><path d=\"M60.0,53.6 L62.9,55.1 L65.7,56.7 L68.6,58.3 L71.5,59.9 L74.3,61.5 L77.2,63.2 L80.1,64.8 L82.9,66.5 L85.8,68.3 L88.7,70.0 L91.5,71.8 L94.4,73.5 L97.3,75.4 L100.1,77.2 L103.0,79.0 L105.9,80.9 L108.7,82.8 L111.6,84.7 L114.5,86.6 L117.3,88.6 L120.2,90.6 L123.1,92.6 L125.9,94.6 L128.8,96.7 L131.7,98.7 L134.5,100.8 L137.4,102.9 L140.3,105.1 L143.1,107.2 L146.0,109.4\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.4\" stroke-dasharray=\"2 2\"/><g transform=\"translate(96.0 61.1) rotate(0) scale(0.6)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.00\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><circle cx=\"100.0\" cy=\"77.1\" r=\"2.6\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"40\" y=\"24\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"start\" fill=\"#000000\">altimeter  f</text><text x=\"40\" y=\"36\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">slope gauge  \u2207f  (dashed line)</text><text x=\"40\" y=\"48\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">curvature gauge  \u2207\u00b2f  (dotted curve)</text><text x=\"120\" y=\"140\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">local model of the terrain</text></svg>",
    "drawingCaption": "The pilot's three fog instruments at one point: altimeter f, slope gauge \u2207f (tangent line) and curvature gauge \u2207\u00b2f (the bending parabola).",
    "coreTranslation": [
      "For $f \\in C^2(\\mathbb{R}^n)$, the 2nd-order expansion along perturbation $d$ is: $f(x+d) = f(x) + \\nabla f(x)^T d + \\frac{1}{2} d^T \\nabla^2 f(x) d + o(\\|d\\|^2)$.",
      "<strong>Mean-Value Remainder:</strong> There exists $\\theta \\in (0, 1)$ such that the remainder is exact: $R_2 = \\frac{1}{2} d^T \\nabla^2 f(x + \\theta d) d$.",
      "The quadratic model $m(d) = f(x) + \\nabla f(x)^T d + \\frac{1}{2} d^T B d$ forms the foundational engine for all Newton, Quasi-Newton, and trust-region algorithms."
    ],
    "math": "$$f(x+d) = f(x) + \\nabla f(x)^T d + \\frac{1}{2} d^T \\nabla^2 f(x+\\theta d) d, \\quad \\theta \\in (0, 1)$$",
    "personalConnection": "<strong>The airplane analogy.</strong> In fog the pilot has three instruments: the altimeter $f(x)$, the slope gauge $\\nabla f(x)$ and the curvature gauge $\\nabla^2f(x)$. Together they give a local model of the terrain around the plane.",
    "examTrap": "The Hessian $\\nabla^2 f(x)$ must be evaluated at an INTERMEDIATE point $x + \\theta d$ for exact equality! Evaluating at $x$ requires adding the asymptotic remainder term $o(\\|d\\|^2)$.",
    "hint": "Which three instrument readings let the pilot model the terrain near his position?",
    "breakdown": [
      "<strong>$f(x)$ = the altimeter.</strong> Your altitude right now.",
      "<strong>$\\nabla f(x)^\\top d$ = the slope term.</strong> The altitude change from moving $d$ at the current slope; the dot product keeps only the part of $d$ pointing along the slope.",
      "<strong>$\\tfrac12d^\\top\\nabla^2f\\,d$ = the curvature term.</strong> The extra correction because the slope itself bends as you move; the $\\tfrac12$ and the square come from integrating a changing slope."
    ]
  },
  {
    "id": 202,
    "subject": "CMO",
    "topicId": "02_Multivariate_Taylor_Series_and_Optimality_Conditions",
    "topicTitle": "02 \u00b7 Multivariate Taylor Series & Optimality",
    "cardNumber": "02",
    "category": "FIRST-ORDER OPTIMALITY",
    "highlighterClass": "highlight-amber",
    "title": "First-Order Necessary Condition (FONC)",
    "textbookImg": "assets/luenberger_fig7_1.png",
    "textbookRef": "Luenberger & Ye (4th ed), Sect. 7.1, Fig. 7.1 (p. 191)",
    "drawingCaption": "At the lowest parking spot the slope gauge reads zero: the tangent is level and no direction starts to descend.",
    "coreTranslation": [
      "<strong>Theorem (FONC):</strong> If $x^*$ is an unconstrained local minimizer of $f \\in C^1$, then the gradient must vanish: $\\nabla f(x^*) = 0$.",
      "<strong>Proof Engine:</strong> Define 1D slice $\\phi(t) = f(x^* + t d)$. Because $t=0$ is a local minimum of $\\phi(t)$, single-variable calculus gives $\\phi'(0) = 0$. By chain rule, $\\phi'(0) = \\nabla f(x^*)^T d = 0$.",
      "Because this holds for EVERY direction $d \\in \\mathbb{R}^n$, we choose $d = \\nabla f(x^*)$, which forces $\\|\\nabla f(x^*)\\|^2 = 0 \\implies \\nabla f(x^*) = 0$."
    ],
    "math": "$$x^* \\text{ local min of } f \\in C^1 \\implies \\nabla f(x^*) = \\mathbf{0}$$",
    "personalConnection": "<strong>The airplane analogy.</strong> At the lowest parking spot the slope gauge reads zero: in no direction does the plane start to descend.",
    "examTrap": "FONC is strictly NECESSARY, not sufficient! A zero gradient $\\nabla f(x^*) = 0$ also occurs at local maxima and saddle points (e.g., $f(x_1, x_2) = x_1^2 - x_2^2$ at the origin).",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-202\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><path d=\"M28.0,40.0 L32.6,46.8 L37.2,53.3 L41.8,59.4 L46.4,65.2 L51.0,70.6 L55.6,75.7 L60.2,80.4 L64.8,84.8 L69.4,88.8 L74.0,92.5 L78.6,95.8 L83.2,98.8 L87.8,101.4 L92.4,103.7 L97.0,105.6 L101.6,107.2 L106.2,108.4 L110.8,109.3 L115.4,109.8 L120.0,110.0 L124.6,109.8 L129.2,109.3 L133.8,108.4 L138.4,107.2 L143.0,105.6 L147.6,103.7 L152.2,101.4 L156.8,98.8 L161.4,95.8 L166.0,92.5 L170.6,88.8 L175.2,84.8 L179.8,80.4 L184.4,75.7 L189.0,70.6 L193.6,65.2 L198.2,59.4 L202.8,53.3 L207.4,46.8 L212.0,40.0\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.6\"/><line x1=\"60.0\" y1=\"110.0\" x2=\"180.0\" y2=\"110.0\" stroke=\"#000000\" stroke-width=\"1.4\" stroke-dasharray=\"5 3\"/><g transform=\"translate(120.0 96.0) rotate(0) scale(0.8)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.50\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><circle cx=\"120.0\" cy=\"110.0\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"120\" y=\"24\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">slope gauge reads 0</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">no direction goes downhill first: \u2207f(x*) = 0</text></svg>",
    "hint": "What must the slope gauge read at the very bottom of a valley?",
    "breakdown": [
      "<strong>$\\nabla f(x^*)=0$:</strong> the radar sees no slope in any direction.",
      "<strong>Why:</strong> if any component were nonzero, moving against it would lose altitude, so $x^*$ could not be a lowest point.",
      "<strong>Warning:</strong> it is only necessary. A hilltop or a saddle also reads zero."
    ]
  },
  {
    "id": 203,
    "subject": "CMO",
    "topicId": "02_Multivariate_Taylor_Series_and_Optimality_Conditions",
    "topicTitle": "02 \u00b7 Multivariate Taylor Series & Optimality",
    "cardNumber": "03",
    "category": "SECOND-ORDER OPTIMALITY",
    "highlighterClass": "highlight-emerald",
    "title": "Second-Order Necessary Condition (SONC)",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-203\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"120\" y1=\"8\" x2=\"120\" y2=\"138\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"3 3\"/><path d=\"M22.0,57.8 L24.9,64.8 L27.9,71.3 L30.8,77.3 L33.7,82.8 L36.7,87.9 L39.6,92.5 L42.5,96.6 L45.5,100.2 L48.4,103.3 L51.3,106.0 L54.3,108.1 L57.2,109.8 L60.1,111.0 L63.1,111.8 L66.0,112.0 L68.9,111.8 L71.9,111.0 L74.8,109.8 L77.7,108.1 L80.7,106.0 L83.6,103.3 L86.5,100.2 L89.5,96.6 L92.4,92.5 L95.3,87.9 L98.3,82.8 L101.2,77.3 L104.1,71.3 L107.1,64.8 L110.0,57.8\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.6\"/><g transform=\"translate(66.0 98.0) rotate(0) scale(0.6)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.00\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"66\" y=\"128\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">curves up \u2713 stays put</text><path d=\"M124.0,110.0 L127.3,101.0 L130.7,92.6 L134.0,84.8 L137.3,77.6 L140.7,71.1 L144.0,65.2 L147.3,59.9 L150.7,55.2 L154.0,51.2 L157.3,47.8 L160.7,45.0 L164.0,42.8 L167.3,41.2 L170.7,40.3 L174.0,40.0 L177.3,40.3 L180.7,41.2 L184.0,42.8 L187.3,45.0 L190.7,47.8 L194.0,51.2 L197.3,55.2 L200.7,59.9 L204.0,65.2 L207.3,71.1 L210.7,77.6 L214.0,84.8 L217.3,92.6 L220.7,101.0 L224.0,110.0\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.6\" stroke-dasharray=\"5 3\"/><g transform=\"translate(174.0 28.0) rotate(0) scale(0.6)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.00\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><line x1=\"174.0\" y1=\"36.0\" x2=\"206.0\" y2=\"56.0\" stroke=\"#000000\" stroke-width=\"1.8\" marker-end=\"url(#arr-203)\"/><text x=\"174\" y=\"128\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">curves down \u2717 rolls away</text><text x=\"66\" y=\"16\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">SONC: \u2207\u00b2f \u2ab0 0</text></svg>",
    "drawingCaption": "Left: ground curving up in every direction holds the plane. Right: one direction curving down and the plane rolls away, so the Hessian must be positive semidefinite.",
    "coreTranslation": [
      "<strong>Theorem (SONC):</strong> If $x^*$ is a local minimizer of $f \\in C^2$, then $\\nabla f(x^*) = 0$ AND the Hessian matrix is <strong>positive semidefinite</strong>: $\\nabla^2 f(x^*) \\succeq 0$.",
      "<strong>Proof:</strong> Using 2nd-order Taylor with $\\nabla f(x^*)=0$: $f(x^* + t d) - f(x^*) = \\frac{1}{2} t^2 d^T \\nabla^2 f(x^*) d + o(t^2) \\ge 0$. Dividing by $t^2$ and taking $t \\to 0$ yields $d^T \\nabla^2 f(x^*) d \\ge 0$ for all $d$.",
      "This implies that all eigenvalues of the Hessian at $x^*$ are non-negative: $\\lambda_i(\\nabla^2 f(x^*)) \\ge 0$ for all $i = 1, \\dots, n$."
    ],
    "math": "$$x^* \\text{ local min of } f \\in C^2 \\implies \\nabla f(x^*) = \\mathbf{0} \\quad \\text{and} \\quad \\nabla^2 f(x^*) \\succeq 0$$",
    "personalConnection": "<strong>The airplane analogy.</strong> The curvature gauge must never read negative at the lowest spot: if even one direction curved downward, the plane would roll off that way.",
    "examTrap": "$\\nabla^2 f(x^*) \\succeq 0$ alone is NOT sufficient for a local minimum! Consider $f(x) = x^3$ at $x=0$: $f'(0)=0$ and $f''(0)=0 \\ge 0$, but $x=0$ is an inflection point, not a minimum.",
    "hint": "What must the curvature gauge say at a lowest point so no direction rolls the marble away?",
    "breakdown": [
      "<strong>$\\nabla f(x^*)=0$</strong> removes the slope term of the Taylor expansion.",
      "<strong>$\\nabla^2f(x^*)\\succeq0$ means $d^\\top\\nabla^2f\\,d\\ge0$ for every $d$:</strong> the ground curves up or stays flat in every direction.",
      "<strong>If one direction had negative curvature,</strong> the plane would roll down it, so $x^*$ would not be a minimum."
    ]
  },
  {
    "id": 204,
    "subject": "CMO",
    "topicId": "02_Multivariate_Taylor_Series_and_Optimality_Conditions",
    "topicTitle": "02 \u00b7 Multivariate Taylor Series & Optimality",
    "cardNumber": "04",
    "category": "SUFFICIENT CONDITIONS",
    "highlighterClass": "highlight-violet",
    "title": "Second-Order Sufficient Condition (SOSC)",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-204\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><path d=\"M30.0,34.0 L34.5,41.4 L39.0,48.4 L43.5,55.1 L48.0,61.4 L52.5,67.2 L57.0,72.8 L61.5,77.9 L66.0,82.6 L70.5,87.0 L75.0,91.0 L79.5,94.6 L84.0,97.8 L88.5,100.7 L93.0,103.2 L97.5,105.2 L102.0,107.0 L106.5,108.3 L111.0,109.2 L115.5,109.8 L120.0,110.0 L124.5,109.8 L129.0,109.2 L133.5,108.3 L138.0,107.0 L142.5,105.2 L147.0,103.2 L151.5,100.7 L156.0,97.8 L160.5,94.6 L165.0,91.0 L169.5,87.0 L174.0,82.6 L178.5,77.9 L183.0,72.8 L187.5,67.2 L192.0,61.4 L196.5,55.1 L201.0,48.4 L205.5,41.4 L210.0,34.0\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.6\"/><path d=\"M40.0,86.3 L45.3,89.4 L50.7,92.2 L56.0,94.8 L61.3,97.3 L66.7,99.5 L72.0,101.5 L77.3,103.3 L82.7,104.8 L88.0,106.2 L93.3,107.4 L98.7,108.3 L104.0,109.1 L109.3,109.6 L114.7,109.9 L120.0,110.0 L125.3,109.9 L130.7,109.6 L136.0,109.1 L141.3,108.3 L146.7,107.4 L152.0,106.2 L157.3,104.8 L162.7,103.3 L168.0,101.5 L173.3,99.5 L178.7,97.3 L184.0,94.8 L189.3,92.2 L194.7,89.4 L200.0,86.3\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"4 3\"/><g transform=\"translate(120.0 96.0) rotate(0) scale(0.75)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.60\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><circle cx=\"120.0\" cy=\"110.0\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"120\" y=\"22\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">strictly up in every direction</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u2207f=0 and \u2207\u00b2f \u227b 0  \u21d2  strict local min</text><text x=\"206\" y=\"66\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"end\" fill=\"#000000\">c\u2016d\u2016\u00b2 floor</text></svg>",
    "drawingCaption": "The ground curves strictly upward in every direction, at least like the dotted floor c\u2016d\u2016\u00b2: a guaranteed strict local lowest spot.",
    "coreTranslation": [
      "<strong>Theorem (SOSC):</strong> If $\\nabla f(x^*) = 0$ AND the Hessian is <strong>strictly positive definite</strong> ($\\nabla^2 f(x^*) \\succ 0$), then $x^*$ is a <strong>strict local minimizer</strong>.",
      "<strong>Proof Engine:</strong> Let $\\lambda_{\\min} > 0$ be the smallest eigenvalue of $\\nabla^2 f(x^*)$. By Rayleigh quotient, $d^T \\nabla^2 f(x^*) d \\ge \\lambda_{\\min} \\|d\\|^2$. Taylor expansion gives: $f(x^*+d) - f(x^*) \\ge \\frac{1}{2} \\lambda_{\\min} \\|d\\|^2 + o(\\|d\\|^2) > 0$ for all small $d \\ne 0$.",
      "This condition is completely decisive: no higher-order derivatives need to be evaluated once $\\lambda_{\\min} > 0$ is verified."
    ],
    "math": "$$\\nabla f(x^*) = \\mathbf{0} \\quad \\text{and} \\quad \\nabla^2 f(x^*) \\succ 0 \\implies x^* \\text{ is a strict local minimizer}$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Every direction curves strictly upward, like the inside of a valley with steep sides, so the plane is trapped at a guaranteed strict local low point.",
    "examTrap": "SOSC requires STRICT inequality $\\nabla^2 f(x^*) \\succ 0$. If $\\lambda_{\\min} = 0$ (e.g. $f(x) = x^4$ at $x=0$), $x^*$ can still be a minimizer, but SOSC fails to prove it and 4th-order analysis is needed.",
    "hint": "What upgrade turns the necessary conditions into a guarantee of a strict valley?",
    "breakdown": [
      "<strong>$\\nabla f(x^*)=0$ and $\\nabla^2f(x^*)\\succ0$:</strong> zero slope and strictly positive curvature in every direction.",
      "<strong>Strict positivity gives a bowl floor</strong> $d^\\top\\nabla^2f\\,d\\ge c\\|d\\|^2$ with $c\\gt0$, so leaving $x^*$ always raises the altitude.",
      "<strong>It is sufficient but not necessary:</strong> $f=x^4$ has a strict minimum at 0 even though its curvature there is 0."
    ]
  },
  {
    "id": 205,
    "subject": "CMO",
    "topicId": "02_Multivariate_Taylor_Series_and_Optimality_Conditions",
    "topicTitle": "02 \u00b7 Multivariate Taylor Series & Optimality",
    "cardNumber": "05",
    "category": "EIGENVALUE CLASSIFICATION",
    "highlighterClass": "highlight-indigo",
    "title": "Hessian Spectral Classification of Critical Points",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-205\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"80\" y1=\"10\" x2=\"80\" y2=\"136\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"3 3\"/><line x1=\"160\" y1=\"10\" x2=\"160\" y2=\"136\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"3 3\"/><path d=\"M12.0,44.0 L14.8,54.6 L17.6,64.2 L20.4,72.6 L23.2,79.8 L26.0,86.0 L28.8,91.0 L31.6,95.0 L34.4,97.8 L37.2,99.4 L40.0,100.0 L42.8,99.4 L45.6,97.8 L48.4,95.0 L51.2,91.0 L54.0,86.0 L56.8,79.8 L59.6,72.6 L62.4,64.2 L65.2,54.6 L68.0,44.0\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.4\"/><g transform=\"translate(40.0 84.0) rotate(0) scale(0.5)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.40\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"40\" y=\"126\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">all \u03bb>0</text><text x=\"40\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">bowl: min</text><path d=\"M92.0,100.0 L94.8,89.4 L97.6,79.8 L100.4,71.4 L103.2,64.2 L106.0,58.0 L108.8,53.0 L111.6,49.0 L114.4,46.2 L117.2,44.6 L120.0,44.0 L122.8,44.6 L125.6,46.2 L128.4,49.0 L131.2,53.0 L134.0,58.0 L136.8,64.2 L139.6,71.4 L142.4,79.8 L145.2,89.4 L148.0,100.0\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.4\"/><g transform=\"translate(120.0 32.0) rotate(0) scale(0.5)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.40\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"120\" y=\"126\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">all \u03bb&lt;0</text><text x=\"120\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">hilltop: max</text><path d=\"M172.0,54.7 L174.8,63.3 L177.6,71.0 L180.4,77.8 L183.2,83.7 L186.0,88.7 L188.8,92.8 L191.6,95.9 L194.4,98.2 L197.2,99.5 L200.0,100.0 L202.8,99.5 L205.6,98.2 L208.4,95.9 L211.2,92.8 L214.0,88.7 L216.8,83.7 L219.6,77.8 L222.4,71.0 L225.2,63.3 L228.0,54.7\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.4\"/><path d=\"M172.0,89.3 L174.8,80.7 L177.6,73.0 L180.4,66.2 L183.2,60.3 L186.0,55.3 L188.8,51.2 L191.6,48.1 L194.4,45.8 L197.2,44.5 L200.0,44.0 L202.8,44.5 L205.6,45.8 L208.4,48.1 L211.2,51.2 L214.0,55.3 L216.8,60.3 L219.6,66.2 L222.4,73.0 L225.2,80.7 L228.0,89.3\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.4\" stroke-dasharray=\"4 3\"/><g transform=\"translate(200.0 60.0) rotate(0) scale(0.5)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.40\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"200\" y=\"126\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">mixed \u03bb</text><text x=\"200\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">saddle (pass)</text></svg>",
    "drawingCaption": "Hessian eigenvalues tell the shape: all positive is a bowl, all negative a hilltop, mixed is a mountain pass (low along the ridge, high across the trail).",
    "coreTranslation": [
      "<strong>What:</strong> at a critical point ($\\nabla f=0$) the eigenvalues of the Hessian tell you the shape: all $>0$ is a <strong>bowl</strong> (local min), all $<0$ is a <strong>hill</strong> (local max), mixed signs is a <strong>saddle</strong>.",
      "<strong>How:</strong> each eigenvalue is the curvature along its eigenvector: positive means the ground curves up in that direction, negative means it curves down.",
      "<strong>Why it matters:</strong> at a saddle there is always a way down (an eigenvector $v$ with $v^T\\nabla^2f\\,v<0$), so an algorithm that sees negative curvature can walk off the saddle instead of getting stuck."
    ],
    "math": "$$\\text{Saddle Point} \\iff \\exists \\, i, j \\text{ s.t. } \\lambda_i(\\nabla^2 f(x^*)) > 0 \\text{ and } \\lambda_j(\\nabla^2 f(x^*)) < 0$$",
    "personalConnection": "<strong>The airplane analogy.</strong> The Hessian's eigenvalues are the curvature along each natural axis: all positive is a valley bottom, all negative a hilltop, mixed is a mountain pass (low along the ridge, high across the trail).",
    "examTrap": "Sylvester's Criterion for negative definiteness requires alternating leading principal minors: $(-1)^k \\Delta_k > 0$ ($\\Delta_1 < 0, \\Delta_2 > 0, \\Delta_3 < 0$). Many students erroneously check if all $\\Delta_k < 0$.",
    "hint": "What do the signs of the Hessian eigenvalues say about the terrain shape at a critical point?",
    "breakdown": [
      "<strong>Each eigenvalue is the curvature along its own eigen-direction.</strong> Positive curves up, negative curves down.",
      "<strong>All positive = valley bottom; all negative = hilltop;</strong> at least one of each sign = saddle (low along one axis, high along another).",
      "<strong>At a saddle there is always a way down,</strong> along an eigenvector with negative curvature."
    ]
  },
  {
    "id": 206,
    "subject": "CMO",
    "topicId": "02_Multivariate_Taylor_Series_and_Optimality_Conditions",
    "topicTitle": "02 \u00b7 Multivariate Taylor Series & Optimality",
    "cardNumber": "06",
    "category": "WORKED BENCHMARK",
    "highlighterClass": "highlight-rose",
    "title": "Worked Benchmark: Rosenbrock Critical Points",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-206\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><path d=\"M26.0,19.2 L30.7,28.3 L35.4,36.8 L40.1,45.0 L44.8,52.6 L49.5,59.8 L54.2,66.5 L58.9,72.8 L63.6,78.6 L68.3,83.9 L73.0,88.8 L77.7,93.2 L82.4,97.2 L87.1,100.6 L91.8,103.6 L96.5,106.2 L101.2,108.3 L105.9,109.9 L110.6,111.1 L115.3,111.8 L120.0,112.0 L124.7,111.8 L129.4,111.1 L134.1,109.9 L138.8,108.3 L143.5,106.2 L148.2,103.6 L152.9,100.6 L157.6,97.2 L162.3,93.2 L167.0,88.8 L171.7,83.9 L176.4,78.6 L181.1,72.8 L185.8,66.5 L190.5,59.8 L195.2,52.6 L199.9,45.0 L204.6,36.8 L209.3,28.3 L214.0,19.2\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.8\"/><path d=\"M26.0,43.2 L30.7,52.3 L35.4,60.8 L40.1,69.0 L44.8,76.6 L49.5,83.8 L54.2,90.5 L58.9,96.8 L63.6,102.6 L68.3,107.9 L73.0,112.8 L77.7,117.2 L82.4,121.2 L87.1,124.6 L91.8,127.6 L96.5,130.2 L101.2,132.3 L105.9,133.9 L110.6,135.1 L115.3,135.8 L120.0,136.0 L124.7,135.8 L129.4,135.1 L134.1,133.9 L138.8,132.3 L143.5,130.2 L148.2,127.6 L152.9,124.6 L157.6,121.2 L162.3,117.2 L167.0,112.8 L171.7,107.9 L176.4,102.6 L181.1,96.8 L185.8,90.5 L190.5,83.8 L195.2,76.6 L199.9,69.0 L204.6,60.8 L209.3,52.3 L214.0,43.2\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.8\"/><path d=\"M26.0,31.2 L30.7,40.3 L35.4,48.8 L40.1,57.0 L44.8,64.6 L49.5,71.8 L54.2,78.5 L58.9,84.8 L63.6,90.6 L68.3,95.9 L73.0,100.8 L77.7,105.2 L82.4,109.2 L87.1,112.6 L91.8,115.6 L96.5,118.2 L101.2,120.3 L105.9,121.9 L110.6,123.1 L115.3,123.8 L120.0,124.0 L124.7,123.8 L129.4,123.1 L134.1,121.9 L138.8,120.3 L143.5,118.2 L148.2,115.6 L152.9,112.6 L157.6,109.2 L162.3,105.2 L167.0,100.8 L171.7,95.9 L176.4,90.6 L181.1,84.8 L185.8,78.5 L190.5,71.8 L195.2,64.6 L199.9,57.0 L204.6,48.8 L209.3,40.3 L214.0,31.2\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.0\" stroke-dasharray=\"3 3\"/><g transform=\"translate(46.0 50.5) rotate(20) scale(0.6)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.00\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><circle cx=\"120.0\" cy=\"124.0\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"120\" y=\"20\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">banana canyon y = x\u00b2</text><text x=\"120\" y=\"32\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u03ba \u2248 2500: walls far steeper than the floor</text><text x=\"120\" y=\"142\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">follow the floor with tiny careful legs</text></svg>",
    "drawingCaption": "Rosenbrock is a long curved canyon: the floor (dashed) is almost flat while the walls are enormously steeper, condition number about 2500.",
    "coreTranslation": [
      "<strong>Problem:</strong> Analyze critical points of Rosenbrock's function $f(x, y) = 100(y - x^2)^2 + (1 - x)^2$.",
      "<strong>Step 1 (Gradient = 0):</strong> $\\nabla f = [-400x(y-x^2) - 2(1-x), \\; 200(y-x^2)]^T = [0, 0]^T$. The 2nd equation gives $y = x^2$. Substituting into 1st gives $-2(1-x) = 0 \\implies x^* = 1, y^* = 1$.",
      "<strong>Step 2 (Hessian at (1, 1)):</strong> $\\nabla^2 f(1, 1) = \\begin{bmatrix} 802 & -400 \\\\ -400 & 200 \\end{bmatrix}$. Trace $= 1002 > 0$, Determinant $= 802(200) - 160000 = 400 > 0$. Both eigenvalues are strictly positive $\\implies$ unique strict local (and global) minimum!"
    ],
    "math": "$$\\nabla f(1, 1) = \\mathbf{0}, \\quad \\det(\\nabla^2 f) = 400 > 0, \\quad \\operatorname{tr}(\\nabla^2 f) = 1002 > 0 \\implies (1,1) \\text{ is strict min}$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Rosenbrock is a long curved banana canyon along $y=x^2$: the floor is nearly flat while the walls are steep, with condition number around 2500, so following the floor needs tiny careful legs.",
    "examTrap": "When evaluating $2 \\times 2$ Hessians, always check BOTH $\\det(H) > 0$ and $\\operatorname{tr}(H) > 0$. If $\\det(H) > 0$ and $\\operatorname{tr}(H) < 0$, both eigenvalues are negative, giving a local MAXIMUM!",
    "hint": "Why is $(1,1)$ a strict minimum of Rosenbrock even though the canyon is so hard to follow?",
    "breakdown": [
      "<strong>$\\det=400\\gt0$ and $\\operatorname{tr}=1002\\gt0$</strong> for a 2\u00d72 Hessian means both eigenvalues are positive, so $\\nabla^2f\\succ0$.",
      "<strong>The two eigenvalues are very different</strong> (about 1000 and 0.4), so the floor is nearly flat compared with the walls.",
      "<strong>That huge ratio is the condition number:</strong> it is why gradient methods crawl along this canyon."
    ]
  },
  {
    "id": 301,
    "subject": "CMO",
    "topicId": "03_Convexity_and_Strong_Convexity",
    "topicTitle": "03 \u00b7 Convexity & Strong Convexity",
    "cardNumber": "01",
    "category": "CONVEXITY DEFINITIONS",
    "highlighterClass": "highlight-cyan",
    "title": "Convex Sets & Secant Inequality",
    "textbookImg": "assets/luenberger_fig7_3.png",
    "textbookRef": "Luenberger & Ye (4th ed), Sect. 7.4, Fig. 7.3 (p. 199)",
    "drawingCaption": "Left: a convex airspace, where every straight flight path between two points stays inside. Right: a crescent, where the straight path leaves the airspace.",
    "coreTranslation": [
      "A set $C \\subset \\mathbb{R}^n$ is <strong>Convex</strong> if for any $x, y \\in C$ and $\\theta \\in [0, 1]$, the line segment $\\theta x + (1-\\theta)y \\in C$ remains inside $C$.",
      "A function $f: C \\to \\mathbb{R}$ is <strong>Convex</strong> if for all $x, y \\in C$ and $\\theta \\in [0, 1]$: $f(\\theta x + (1-\\theta)y) \\le \\theta f(x) + (1-\\theta)f(y)$.",
      "Geometrically, the secant line segment joining $(x, f(x))$ and $(y, f(y))$ lies completely on or above the graph of $f$."
    ],
    "math": "$$f(\\theta x + (1-\\theta)y) \\le \\theta f(x) + (1-\\theta)f(y) \\quad \\forall \\, x, y \\in C, \\; \\theta \\in [0, 1]$$",
    "personalConnection": "<strong>The airplane analogy.</strong> A convex corridor: any two points can be joined by a straight flight path that stays inside. The straight path between two points on a convex terrain always flies above the terrain.",
    "examTrap": "The domain $C$ of $f$ MUST be a convex set for the definition to even be valid! You cannot define convexity on disjoint or non-convex domains like $C = \\mathbb{R} \\setminus \\{0\\}$.",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-301\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"120\" y1=\"8\" x2=\"120\" y2=\"138\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"3 3\"/><ellipse cx=\"60\" cy=\"66\" rx=\"44\" ry=\"32\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"2\" transform=\"rotate(0 60 66)\"/><circle cx=\"34.0\" cy=\"70.0\" r=\"2.6\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><circle cx=\"90.0\" cy=\"56.0\" r=\"2.6\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><line x1=\"34\" y1=\"70\" x2=\"90\" y2=\"56\" stroke=\"#000000\" stroke-width=\"2\"/><text x=\"60\" y=\"112\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">convex \u2713</text><path d=\"M140,38 Q176,100 226,38 Q184,70 140,38 Z\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"2\"/><circle cx=\"146.0\" cy=\"42.0\" r=\"2.6\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><circle cx=\"220.0\" cy=\"42.0\" r=\"2.6\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><line x1=\"146\" y1=\"42\" x2=\"220\" y2=\"42\" stroke=\"#000000\" stroke-width=\"2\" stroke-dasharray=\"4 3\"/><text x=\"182\" y=\"112\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">crescent \u2717</text><g transform=\"translate(60.0 66.0) rotate(0) scale(0.5)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.40\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g></svg>",
    "hint": "What does 'the string above the terrain' say about convexity?",
    "breakdown": [
      "<strong>$\\theta x+(1-\\theta)y$</strong> is a point on the straight flight path between $x$ and $y$.",
      "<strong>$\\theta f(x)+(1-\\theta)f(y)$</strong> is the height of the straight string stretched between the two altitudes.",
      "<strong>The inequality says the terrain never rises above the string,</strong> which is convexity."
    ]
  },
  {
    "id": 302,
    "subject": "CMO",
    "topicId": "03_Convexity_and_Strong_Convexity",
    "topicTitle": "03 \u00b7 Convexity & Strong Convexity",
    "cardNumber": "02",
    "category": "FIRST-ORDER CONVEXITY",
    "highlighterClass": "highlight-amber",
    "title": "First-Order Condition: Tangent Underestimator",
    "textbookImg": "assets/luenberger_fig7_4.png",
    "textbookRef": "Luenberger & Ye (4th ed), Sect. 7.5, Fig. 7.4 (p. 201)",
    "drawingCaption": "At any point the flat glide plane touching the terrain lies beneath the terrain everywhere else (a convex terrain is always above its tangents).",
    "coreTranslation": [
      "<strong>Theorem:</strong> Let $f \\in C^1$ on convex open set $C$. Then $f$ is convex if and only if for all $x, y \\in C$: $f(y) \\ge f(x) + \\nabla f(x)^T(y - x)$.",
      "<strong>Global Underestimator:</strong> The 1st-order Taylor affine approximation at ANY point $x$ forms a global lower bound across the ENTIRE domain.",
      "<strong>Critical Consequence:</strong> If $\\nabla f(x^*) = 0$, then $f(y) \\ge f(x^*) + 0^T(y - x) = f(x^*)$ for all $y$. Thus, <strong>every stationary point of a convex function is a global minimizer!</strong>"
    ],
    "math": "$$f \\text{ is convex} \\iff f(y) \\ge f(x) + \\nabla f(x)^T (y - x) \\quad \\forall \\, x, y$$",
    "personalConnection": "<strong>The airplane analogy.</strong> At any point the flat glide plane touching the terrain there lies beneath the terrain everywhere else: the slope gauge always underestimates the true altitude of a convex terrain.",
    "examTrap": "Monotonicity of gradient is completely equivalent: $( \\nabla f(y) - \\nabla f(x) )^T (y - x) \\ge 0$. In 1D, this simply states that the derivative $f'(x)$ is non-decreasing.",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-302\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><path d=\"M30.0,36.0 L34.5,43.4 L39.0,50.4 L43.5,57.1 L48.0,63.4 L52.5,69.2 L57.0,74.8 L61.5,79.9 L66.0,84.6 L70.5,89.0 L75.0,93.0 L79.5,96.6 L84.0,99.8 L88.5,102.7 L93.0,105.2 L97.5,107.2 L102.0,109.0 L106.5,110.3 L111.0,111.2 L115.5,111.8 L120.0,112.0 L124.5,111.8 L129.0,111.2 L133.5,110.3 L138.0,109.0 L142.5,107.2 L147.0,105.2 L151.5,102.7 L156.0,99.8 L160.5,96.6 L165.0,93.0 L169.5,89.0 L174.0,84.6 L178.5,79.9 L183.0,74.8 L187.5,69.2 L192.0,63.4 L196.5,57.1 L201.0,50.4 L205.5,43.4 L210.0,36.0\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.6\"/><line x1=\"90\" y1=\"149.53086419787508\" x2=\"200\" y2=\"66.96296296276627\" stroke=\"#000000\" stroke-width=\"1.6\" stroke-dasharray=\"5 3\"/><g transform=\"translate(158.0 113.0) rotate(0) scale(0.6)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.00\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><circle cx=\"160.0\" cy=\"97.0\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"89.1104\" y=\"134\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">the glide plane touching at your spot lies under the whole terrain</text></svg>",
    "hint": "What does the glide plane touching at your position say about the rest of the terrain?",
    "breakdown": [
      "<strong>$f(x)+\\nabla f(x)^\\top(y-x)$</strong> is the flat plane through your position with the radar's slope.",
      "<strong>$f(y)\\ge$ that plane:</strong> the true terrain is never below its tangent plane.",
      "<strong>Consequence:</strong> if $\\nabla f(x)=0$ the plane is level and the terrain is everywhere above it, so $x$ is a global minimum."
    ]
  },
  {
    "id": 303,
    "subject": "CMO",
    "topicId": "03_Convexity_and_Strong_Convexity",
    "topicTitle": "03 \u00b7 Convexity & Strong Convexity",
    "cardNumber": "03",
    "category": "SECOND-ORDER CONVEXITY",
    "highlighterClass": "highlight-emerald",
    "title": "Second-Order Condition: Global PSD Hessian",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-303\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><path d=\"M30.0,36.0 L34.5,43.4 L39.0,50.4 L43.5,57.1 L48.0,63.4 L52.5,69.2 L57.0,74.8 L61.5,79.9 L66.0,84.6 L70.5,89.0 L75.0,93.0 L79.5,96.6 L84.0,99.8 L88.5,102.7 L93.0,105.2 L97.5,107.2 L102.0,109.0 L106.5,110.3 L111.0,111.2 L115.5,111.8 L120.0,112.0 L124.5,111.8 L129.0,111.2 L133.5,110.3 L138.0,109.0 L142.5,107.2 L147.0,105.2 L151.5,102.7 L156.0,99.8 L160.5,96.6 L165.0,93.0 L169.5,89.0 L174.0,84.6 L178.5,79.9 L183.0,74.8 L187.5,69.2 L192.0,63.4 L196.5,57.1 L201.0,50.4 L205.5,43.4 L210.0,36.0\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.6\"/><g transform=\"translate(120.0 98.0) rotate(0) scale(0.7)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.71\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><line x1=\"120.0\" y1=\"86.0\" x2=\"120.0\" y2=\"54.0\" stroke=\"#000000\" stroke-width=\"2.4\" marker-end=\"url(#arr-303)\"/><text x=\"130\" y=\"56\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"start\" fill=\"#000000\">seat pressed up</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">never floats off the seat: \u2207\u00b2f \u2ab0 0 everywhere</text><g transform=\"translate(66.0 72.6) rotate(0) scale(0.45)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.67\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><g transform=\"translate(174.0 72.6) rotate(0) scale(0.45)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.67\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g></svg>",
    "drawingCaption": "Flying across a convex terrain the seat is always pressed up by the ground and never floats off: the terrain curves upward everywhere (PSD Hessian).",
    "coreTranslation": [
      "<strong>Theorem:</strong> Let $f \\in C^2$ on convex open set $C$. Then $f$ is convex if and only if its Hessian is <strong>positive semidefinite everywhere</strong>: $\\nabla^2 f(x) \\succeq 0$ for all $x \\in C$.",
      "This means that at every single point $x \\in C$, all eigenvalues of $\\nabla^2 f(x)$ are non-negative: $\\lambda_{\\min}(\\nabla^2 f(x)) \\ge 0$.",
      "For quadratic $f(x) = \\frac{1}{2} x^T Q x - b^T x$, $\\nabla^2 f(x) = Q$. Hence $f$ is convex if and only if the matrix $Q \\succeq 0$."
    ],
    "math": "$$f \\text{ is convex on } C \\iff \\nabla^2 f(x) \\succeq 0 \\quad \\forall \\, x \\in C$$",
    "personalConnection": "<strong>The airplane analogy.</strong> At every point the seat is pressed up by the ground (never floats up): the terrain curves upward everywhere, which is the positive semidefinite Hessian.",
    "examTrap": "Do not confuse $\\nabla^2 f(x^*) \\succeq 0$ at a single critical point (which is merely SONC for a local min) with $\\nabla^2 f(x) \\succeq 0$ for ALL $x \\in C$ (which proves global convexity of $f$).",
    "hint": "What does 'the seat is always pressed up' say about the Hessian?",
    "breakdown": [
      "<strong>$\\nabla^2f(x)\\succeq0$:</strong> in every direction the second derivative $d^\\top\\nabla^2f\\,d$ is not negative, so the ground never curves away from the seat.",
      "<strong>It must hold at every point of the set,</strong> not only at the bottom.",
      "<strong>It is the practical test for convexity</strong> of a smooth function."
    ]
  },
  {
    "id": 304,
    "subject": "CMO",
    "topicId": "03_Convexity_and_Strong_Convexity",
    "topicTitle": "03 \u00b7 Convexity & Strong Convexity",
    "cardNumber": "04",
    "category": "STRONG CONVEXITY",
    "highlighterClass": "highlight-violet",
    "title": "Strong Convexity & Quadratic Lower Bound",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-304\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><path d=\"M30.0,36.0 L34.5,43.4 L39.0,50.4 L43.5,57.1 L48.0,63.4 L52.5,69.2 L57.0,74.8 L61.5,79.9 L66.0,84.6 L70.5,89.0 L75.0,93.0 L79.5,96.6 L84.0,99.8 L88.5,102.7 L93.0,105.2 L97.5,107.2 L102.0,109.0 L106.5,110.3 L111.0,111.2 L115.5,111.8 L120.0,112.0 L124.5,111.8 L129.0,111.2 L133.5,110.3 L138.0,109.0 L142.5,107.2 L147.0,105.2 L151.5,102.7 L156.0,99.8 L160.5,96.6 L165.0,93.0 L169.5,89.0 L174.0,84.6 L178.5,79.9 L183.0,74.8 L187.5,69.2 L192.0,63.4 L196.5,57.1 L201.0,50.4 L205.5,43.4 L210.0,36.0\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.6\"/><path d=\"M52.0,49.2 L56.5,57.3 L61.1,64.8 L65.6,71.8 L70.1,78.2 L74.7,84.1 L79.2,89.4 L83.7,94.1 L88.3,98.3 L92.8,102.0 L97.3,105.0 L101.9,107.5 L106.4,109.5 L110.9,110.9 L115.5,111.7 L120.0,112.0 L124.5,111.7 L129.1,110.9 L133.6,109.5 L138.1,107.5 L142.7,105.0 L147.2,102.0 L151.7,98.3 L156.3,94.1 L160.8,89.4 L165.3,84.1 L169.9,78.2 L174.4,71.8 L178.9,64.8 L183.5,57.3 L188.0,49.2\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.4\" stroke-dasharray=\"4 3\"/><g transform=\"translate(120.0 98.0) rotate(0) scale(0.75)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.60\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><circle cx=\"120.0\" cy=\"112.0\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"206\" y=\"28\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"end\" fill=\"#000000\">floor: m/2 \u2016x\u2212x*\u2016\u00b2</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">leaving the bottom always costs altitude</text><text x=\"120\" y=\"20\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">strong convexity</text></svg>",
    "drawingCaption": "The terrain stays above a bowl-shaped floor (dotted) of fixed steepness: leaving the bottom always costs at least m/2 \u2016x \u2212 x*\u2016\u00b2 of altitude.",
    "coreTranslation": [
      "A function $f$ is <strong>$\\mu$-Strongly Convex</strong> ($\\mu > 0$) if $g(x) = f(x) - \\frac{\\mu}{2}\\|x\\|^2$ is convex.",
      "<strong>Quadratic Underestimator:</strong> $f(y) \\ge f(x) + \\nabla f(x)^T(y-x) + \\frac{\\mu}{2}\\|y-x\\|^2$. It grows at least quadratically away from any point.",
      "<strong>Second-Order Equivalent:</strong> $\\nabla^2 f(x) \\succeq \\mu I$, meaning the minimum eigenvalue is uniformly bounded away from zero: $\\lambda_{\\min}(\\nabla^2 f(x)) \\ge \\mu > 0$."
    ],
    "math": "$$f \\text{ is } \\mu\\text{-strongly convex} \\iff \\nabla^2 f(x) \\succeq \\mu I \\quad \\forall \\, x$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Strong convexity means the terrain curves up at least like a bowl of fixed steepness $m$: leaving the bottom costs at least $\\tfrac m2\\|x-x^*\\|^2$ of altitude.",
    "examTrap": "Strict convexity does NOT imply strong convexity! For instance, $f(x) = x^4$ is strictly convex on $\\mathbb{R}$, but its 2nd derivative $f''(0) = 0$, so it is NOT strongly convex ($\\mu = 0$).",
    "hint": "What bowl is the terrain guaranteed to stay above?",
    "breakdown": [
      "<strong>$\\nabla^2f\\succeq\\mu I$:</strong> the curvature is at least $\\mu$ in every direction, never flatter than a bowl of steepness $\\mu$.",
      "<strong>Equivalent floor:</strong> $f(y)\\ge f(x)+\\nabla f(x)^\\top(y-x)+\\tfrac\\mu2\\|y-x\\|^2$, the tangent plane plus a quadratic bowl.",
      "<strong>Consequence:</strong> there is a unique lowest point and leaving it always costs altitude."
    ]
  },
  {
    "id": 305,
    "subject": "CMO",
    "topicId": "03_Convexity_and_Strong_Convexity",
    "topicTitle": "03 \u00b7 Convexity & Strong Convexity",
    "cardNumber": "05",
    "category": "GRADIENT DOMINANCE",
    "highlighterClass": "highlight-indigo",
    "title": "Polyak-\u0141ojasiewicz (PL) Inequality",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-305\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><path d=\"M30.0,32.0 L34.5,39.8 L39.0,47.2 L43.5,54.2 L48.0,60.8 L52.5,67.0 L57.0,72.8 L61.5,78.2 L66.0,83.2 L70.5,87.8 L75.0,92.0 L79.5,95.8 L84.0,99.2 L88.5,102.2 L93.0,104.8 L97.5,107.0 L102.0,108.8 L106.5,110.2 L111.0,111.2 L115.5,111.8 L120.0,112.0 L124.5,111.8 L129.0,111.2 L133.5,110.2 L138.0,108.8 L142.5,107.0 L147.0,104.8 L151.5,102.2 L156.0,99.2 L160.5,95.8 L165.0,92.0 L169.5,87.8 L174.0,83.2 L178.5,78.2 L183.0,72.8 L187.5,67.0 L192.0,60.8 L196.5,54.2 L201.0,47.2 L205.5,39.8 L210.0,32.0\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.6\"/><g transform=\"translate(120.0 98.0) rotate(0) scale(0.6)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.00\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><line x1=\"74.0\" y1=\"85.1\" x2=\"102.0\" y2=\"102.7\" stroke=\"#000000\" stroke-width=\"1.8\" marker-end=\"url(#arr-305)\"/><line x1=\"52.0\" y1=\"60.3\" x2=\"102.0\" y2=\"82.3\" stroke=\"#000000\" stroke-width=\"1.8\" marker-end=\"url(#arr-305)\"/><line x1=\"166.0\" y1=\"85.1\" x2=\"138.0\" y2=\"102.7\" stroke=\"#000000\" stroke-width=\"1.8\" marker-end=\"url(#arr-305)\"/><line x1=\"188.0\" y1=\"60.3\" x2=\"138.0\" y2=\"82.3\" stroke=\"#000000\" stroke-width=\"1.8\" marker-end=\"url(#arr-305)\"/><text x=\"120\" y=\"20\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">higher up = steeper slope</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">no flat plateau far above the valley floor</text></svg>",
    "drawingCaption": "The higher you are above the lowest point the steeper the slope under you (longer arrows), so the plane never sits on a flat plateau far above the floor.",
    "coreTranslation": [
      "<strong>What:</strong> the PL inequality says <em>the steeper the slope, the farther you are from the best value</em>: $\\tfrac12\\|\\nabla f(x)\\|^2\\ge\\mu\\,(f(x)-f^*)$.",
      "<strong>How:</strong> a $\\mu$-strongly convex $f$ lies above the bowl $f(x)+\\nabla f^T(y-x)+\\tfrac\\mu2\\|y-x\\|^2$. That bowl's lowest value is $f(x)-\\tfrac1{2\\mu}\\|\\nabla f(x)\\|^2$, and $f^*$ can't be lower than the bowl, so rearranging gives PL.",
      "<strong>Why it matters:</strong> PL alone (no convexity needed) makes gradient descent with step $1/L$ converge <em>linearly</em>: the gap to $f^*$ shrinks by a fixed factor $(1-\\mu/L)$ every step."
    ],
    "math": "$$\\|\\nabla f(x)\\|^2\\ge2\\mu\\,(f(x)-f^*)\\ \\Longrightarrow\\ f(x_k)-f^*\\le\\Big(1-\\frac{\\mu}{L}\\Big)^{k}\\big(f(x_0)-f^*\\big)$$",
    "personalConnection": "<strong>The airplane analogy.</strong> The higher you are above the lowest point, the steeper the slope under you, so the plane can never sit on a flat plateau far above the valley floor.",
    "examTrap": "PL is weaker than strong convexity. A non-convex function such as f(x) = x\u00b2 + 3 sin\u00b2x satisfies PL (every stationary point is a global min), so gradient descent still converges linearly on it.",
    "hint": "What does the PL inequality say about slope and height above the floor?",
    "breakdown": [
      "<strong>$\\|\\nabla f\\|^2$ = how steep the radar reads;</strong> $f-f^*$ = how high you still are above the floor.",
      "<strong>The inequality says steepness $\\ge2\\mu\\times$ height:</strong> the higher you are, the steeper the ground, so there are no plateaus far above the floor.",
      "<strong>Then each leg of size $1/L$ removes a fixed fraction $\\mu/L$ of the height,</strong> giving linear convergence without needing convexity."
    ]
  },
  {
    "id": 306,
    "subject": "CMO",
    "topicId": "03_Convexity_and_Strong_Convexity",
    "topicTitle": "03 \u00b7 Convexity & Strong Convexity",
    "cardNumber": "06",
    "category": "WORKED BENCHMARK",
    "highlighterClass": "highlight-rose",
    "title": "Worked Benchmark: Convexity Hierarchy Traps",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-306\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"80\" y1=\"10\" x2=\"80\" y2=\"136\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"3 3\"/><line x1=\"160\" y1=\"10\" x2=\"160\" y2=\"136\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"3 3\"/><path d=\"M10.0,60.0 L10.0,52.0 L28.0,92.0 L52.0,92.0 L70.0,52.0\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.4\"/><text x=\"40\" y=\"118\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">convex</text><text x=\"41.44\" y=\"130\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">flat ramps allowed</text><path d=\"M92.0,62.6 L93.9,70.7 L95.7,77.2 L97.6,82.3 L99.5,86.3 L101.3,89.4 L103.2,91.7 L105.1,93.3 L106.9,94.4 L108.8,95.1 L110.7,95.6 L112.5,95.8 L114.4,95.9 L116.3,96.0 L118.1,96.0 L120.0,96.0 L121.9,96.0 L123.7,96.0 L125.6,95.9 L127.5,95.8 L129.3,95.6 L131.2,95.1 L133.1,94.4 L134.9,93.3 L136.8,91.7 L138.7,89.4 L140.5,86.3 L142.4,82.3 L144.3,77.2 L146.1,70.7 L148.0,62.6\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.4\"/><text x=\"120\" y=\"118\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">strictly convex</text><text x=\"120\" y=\"130\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">no flat stretch, x\u2074</text><path d=\"M172.0,57.7 L173.9,62.6 L175.7,67.2 L177.6,71.5 L179.5,75.4 L181.3,79.0 L183.2,82.2 L185.1,85.1 L186.9,87.7 L188.8,89.9 L190.7,91.7 L192.5,93.3 L194.4,94.5 L196.3,95.3 L198.1,95.8 L200.0,96.0 L201.9,95.8 L203.7,95.3 L205.6,94.5 L207.5,93.3 L209.3,91.7 L211.2,89.9 L213.1,87.7 L214.9,85.1 L216.8,82.2 L218.7,79.0 L220.5,75.4 L222.4,71.5 L224.3,67.2 L226.1,62.6 L228.0,57.7\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.4\"/><text x=\"200\" y=\"118\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">strongly convex</text><text x=\"200\" y=\"130\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">true bowl</text><g transform=\"translate(200.0 80.0) rotate(0) scale(0.45)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.67\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g></svg>",
    "drawingCaption": "Three terrains: convex allows level ramps, strictly convex has no level stretch but can flatten (x\u2074), strongly convex is a true bowl everywhere.",
    "coreTranslation": [
      "<strong>Convexity Hierarchy:</strong> $\\mu\\text{-Strongly Convex} \\subsetneq \\text{Strictly Convex} \\subsetneq \\text{Convex}$.",
      "<strong>Counterexample 1 ($x^4$):</strong> $f(x) = x^4$ is strictly convex on $\\mathbb{R}$, but $f''(0) = 0$. Hence it is NOT strongly convex.",
      "<strong>Counterexample 2 ($e^x$):</strong> $f(x) = e^x$ is strictly convex on $\\mathbb{R}$ with $f''(x) = e^x > 0$, but $\\lim_{x \\to -\\infty} f''(x) = 0$. Hence it is NOT strongly convex on $\\mathbb{R}$."
    ],
    "math": "$$\\mu\\text{-Strongly Convex } (\\nabla^2 f \\succeq \\mu I) \\implies \\text{Strictly Convex} \\implies \\text{Convex } (\\nabla^2 f \\succeq 0)$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Convex allows level ramps (cruise flat forever); strictly convex has no level stretch but can flatten near the bottom ($x^4$); strongly convex is a true bowl everywhere.",
    "examTrap": "An exam question asking 'Is $f(x) = e^{-x} + x^2$ strongly convex on $\\mathbb{R}$?' Answer: YES! $f''(x) = e^{-x} + 2 \\ge 2 > 0$ for all $x$, so $\\mu = 2$.",
    "hint": "What separates convex, strictly convex and strongly convex terrain?",
    "breakdown": [
      "<strong>Convex:</strong> $\\nabla^2f\\succeq0$; level ramps are allowed.",
      "<strong>Strictly convex:</strong> no flat stretch, but the curvature may vanish at a point (for example $x^4$ at 0).",
      "<strong>Strongly convex:</strong> $\\nabla^2f\\succeq\\mu I$ with a fixed $\\mu\\gt0$, a true bowl everywhere; each condition implies the one before it."
    ]
  },
  {
    "id": 401,
    "subject": "CMO",
    "topicId": "04_Line_Search_Methods_Exact_Armijo_and_Wolfe",
    "topicTitle": "04 \u00b7 Line Search (Armijo & Wolfe)",
    "cardNumber": "01",
    "category": "LINE SEARCH FOUNDATIONS",
    "highlighterClass": "highlight-cyan",
    "title": "Line Search Framework & Descent Directions",
    "textbookImg": "assets/luenberger_fig8_1.png",
    "textbookRef": "Luenberger & Ye (4th ed), Sect. 8.1, Fig. 8.1 (p. 224)",
    "drawingCaption": "Choose a heading d\u2096 that points downhill (\u2207f\u1d40d<0) and decide how far \u03b1 to fly before checking the radar again.",
    "coreTranslation": [
      "The general line search algorithm updates: $x_{k+1} = x_k + \\alpha_k d_k$, where $d_k$ is the search direction and $\\alpha_k > 0$ is the step length.",
      "<strong>Descent Direction Condition:</strong> $d_k$ is a descent direction if the directional derivative is strictly negative: $\\nabla f(x_k)^T d_k < 0$.",
      "This guarantees that for all sufficiently small step sizes $\\alpha > 0$, the objective strictly decreases: $f(x_k + \\alpha d_k) < f(x_k)$."
    ],
    "math": "$$x_{k+1} = x_k + \\alpha_k d_k \\quad \\text{with} \\quad \\nabla f(x_k)^T d_k < 0$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Pick a heading $d_k$ that points downhill ($\\nabla f^\\top d_k\\lt0$) and decide how far $\\alpha_k$ to fly before checking the radar again.",
    "examTrap": "If $\\nabla f(x_k)^T d_k = 0$, $d_k$ is orthogonal to the gradient, meaning $f$ stays flat to 1st order. If $\\nabla f(x_k)^T d_k > 0$, taking any step $\\alpha > 0$ climbs uphill!",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-401\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"20\" y1=\"100\" x2=\"226\" y2=\"40\" stroke=\"#000000\" stroke-width=\"1.4\" stroke-dasharray=\"5 3\"/><g transform=\"translate(70.0 84.0) rotate(16.0) scale(0.8)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.50\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><line x1=\"80.0\" y1=\"82.0\" x2=\"176.0\" y2=\"108.0\" stroke=\"#000000\" stroke-width=\"3\" marker-end=\"url(#arr-401)\"/><text x=\"180\" y=\"118\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"start\" fill=\"#000000\">d\u2096</text><line x1=\"70.0\" y1=\"76.0\" x2=\"84.0\" y2=\"24.0\" stroke=\"#000000\" stroke-width=\"1.8\" stroke-dasharray=\"3 2\" marker-end=\"url(#arr-401)\"/><text x=\"88\" y=\"30\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">\u2207f (uphill)</text><circle cx=\"176.0\" cy=\"108.0\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"176\" y=\"128\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">x\u2096 + \u03b1\u2096d\u2096</text><text x=\"120\" y=\"140\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u2207f\u1d40d\u2096 &lt; 0: heading points downhill</text><text x=\"120\" y=\"14\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u03b1: how far before checking the radar</text></svg>",
    "hint": "What must be true of the heading, and what does the step size decide?",
    "breakdown": [
      "<strong>$d_k$ = the nose.</strong> The condition $\\nabla f(x_k)^\\top d_k\\lt0$ means the nose has a component pointing downhill.",
      "<strong>$\\alpha_k$ = the flight distance.</strong> Multiplying turns the heading into an actual displacement.",
      "<strong>Together:</strong> a good direction with a badly chosen distance can still overshoot or crawl, which is what line search fixes."
    ]
  },
  {
    "id": 402,
    "subject": "CMO",
    "topicId": "04_Line_Search_Methods_Exact_Armijo_and_Wolfe",
    "topicTitle": "04 \u00b7 Line Search (Armijo & Wolfe)",
    "cardNumber": "02",
    "category": "QUADRATIC EXACT LINE SEARCH",
    "highlighterClass": "highlight-amber",
    "title": "Exact Line Search for Quadratic Forms",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-402\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"20\" y1=\"130\" x2=\"226\" y2=\"130\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-402)\"/><path d=\"M30.0,40.0 L34.5,47.0 L39.0,53.7 L43.5,60.0 L48.0,65.9 L52.5,71.5 L57.0,76.7 L61.5,81.6 L66.0,86.1 L70.5,90.2 L75.0,94.0 L79.5,97.4 L84.0,100.5 L88.5,103.2 L93.0,105.5 L97.5,107.5 L102.0,109.1 L106.5,110.4 L111.0,111.3 L115.5,111.8 L120.0,112.0 L124.5,111.8 L129.0,111.3 L133.5,110.4 L138.0,109.1 L142.5,107.5 L147.0,105.5 L151.5,103.2 L156.0,100.5 L160.5,97.4 L165.0,94.0 L169.5,90.2 L174.0,86.1 L178.5,81.6 L183.0,76.7 L187.5,71.5 L192.0,65.9 L196.5,60.0 L201.0,53.7 L205.5,47.0 L210.0,40.0\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.6\"/><g transform=\"translate(120.0 96.0) rotate(0) scale(0.7)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.71\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><circle cx=\"120.0\" cy=\"112.0\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><line x1=\"120.0\" y1=\"112.0\" x2=\"120.0\" y2=\"130.0\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"3 3\"/><text x=\"120\" y=\"142\" font-size=\"9.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u03b1*</text><text x=\"206\" y=\"56\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"end\" fill=\"#000000\">altitude along the track</text><text x=\"120\" y=\"12\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">exact line search: fly to the very bottom</text><text x=\"216\" y=\"142\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"end\" fill=\"#000000\">\u03b1</text></svg>",
    "drawingCaption": "Altitude along one straight track: fly exactly to the bottom (\u03b1*) before turning, found in closed form for a quadratic.",
    "coreTranslation": [
      "For a quadratic objective $f(x) = \\frac{1}{2} x^T Q x - b^T x$, the 1D slice along $d_k$ is $\\phi(\\alpha) = f(x_k + \\alpha d_k)$.",
      "Setting derivative $\\phi'(\\alpha) = \\nabla f(x_k + \\alpha d_k)^T d_k = (g_k + \\alpha Q d_k)^T d_k = 0$ yields the exact closed-form step size: $\\alpha_k = -\\frac{g_k^T d_k}{d_k^T Q d_k}$.",
      "<strong>Orthogonality Property:</strong> Under exact line search, the next gradient is strictly orthogonal to the search direction: $\\nabla f(x_{k+1})^T d_k = 0$."
    ],
    "math": "$$\\alpha_k^* = -\\frac{\\nabla f(x_k)^T d_k}{d_k^T Q d_k}, \\quad \\nabla f(x_{k+1})^T d_k = 0$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Fly dead straight until the altitude stops dropping and starts rising: that is the very bottom of that straight track, found exactly for a quadratic.",
    "examTrap": "In steepest descent on quadratics ($d_k = -g_k$), successive gradients are orthogonal: $g_{k+1}^T g_k = 0$. This orthogonality forces a rigid 90-degree zig-zag trajectory that slows convergence.",
    "hint": "How far should the pilot fly along a straight track on a quadratic terrain?",
    "breakdown": [
      "<strong>Numerator $-g^\\top d$ = the downward momentum:</strong> how steeply the heading dives down the slope.",
      "<strong>Denominator $d^\\top Qd$ = the brakes:</strong> how fast the terrain curves back up along $d$.",
      "<strong>The condition $\\nabla f(x_{k+1})^\\top d_k=0$:</strong> at the bottom of that track the slope along it is zero, so the new radar reading is perpendicular to the old heading."
    ]
  },
  {
    "id": 403,
    "subject": "CMO",
    "topicId": "04_Line_Search_Methods_Exact_Armijo_and_Wolfe",
    "topicTitle": "04 \u00b7 Line Search (Armijo & Wolfe)",
    "cardNumber": "03",
    "category": "INEXACT LINE SEARCH",
    "highlighterClass": "highlight-emerald",
    "title": "Armijo Sufficient Decrease Condition",
    "textbookImg": "assets/luenberger_fig8_8.png",
    "textbookRef": "Luenberger & Ye (4th ed), Sect. 8.1, Fig. 8.8 (p. 239)",
    "drawingCaption": "Altitude along the leg: accept only steps where the actual altitude falls below the dashed Armijo line (a fair drop for the distance and slope).",
    "coreTranslation": [
      "Exact line search is too expensive for general nonlinear functions. The <strong>Armijo Condition</strong> requires a sufficient decrease proportional to step length:",
      "$f(x_k + \\alpha d_k) \\le f(x_k) + c_1 \\alpha \\nabla f(x_k)^T d_k$ with constant $c_1 \\in (0, 1)$ (typically $c_1 = 10^{-4}$).",
      "Geometrically, it specifies a linear upper bound ray with slope $c_1 \\nabla f(x_k)^T d_k$. The step $\\alpha$ is accepted only if $f$ lies below this line, preventing overly large steps."
    ],
    "math": "$$f(x_k + \\alpha d_k) \\le f(x_k) + c_1 \\alpha \\nabla f(x_k)^T d_k, \\quad c_1 \\in (0, 1)$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Armijo asks each leg for a fair altitude drop in proportion to the distance flown and the slope: refuse a leg that burns lots of fuel for little drop.",
    "examTrap": "The Armijo condition ALONE is not enough! It accepts arbitrarily small steps $\\alpha \\to 0$. If an algorithm takes $\\alpha_k = 1/2^k$, Armijo holds trivially, yet the algorithm stalls without reaching a minimum!",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-403\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"20\" y1=\"130\" x2=\"226\" y2=\"130\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-403)\"/><path d=\"M30.0,46.0 L33.0,49.1 L36.0,52.0 L39.0,55.0 L42.0,57.8 L45.0,60.5 L48.0,63.2 L51.0,65.8 L54.0,68.3 L57.0,70.8 L60.0,73.1 L63.0,75.4 L66.0,77.6 L69.0,79.8 L72.0,81.8 L75.0,83.8 L78.0,85.7 L81.0,87.5 L84.0,89.2 L87.0,90.9 L90.0,92.5 L93.0,94.0 L96.0,95.4 L99.0,96.8 L102.0,98.1 L105.0,99.3 L108.0,100.4 L111.0,101.5 L114.0,102.4 L117.0,103.3 L120.0,104.1 L123.0,104.9 L126.0,105.5 L129.0,106.1 L132.0,106.6 L135.0,107.0 L138.0,107.4 L141.0,107.7 L144.0,107.8 L147.0,108.0 L150.0,108.0 L153.0,108.0 L156.0,107.8 L159.0,107.7 L162.0,107.4 L165.0,107.0 L168.0,106.6 L171.0,106.1 L174.0,105.5 L177.0,104.9 L180.0,104.1 L183.0,103.3 L186.0,102.4 L189.0,101.5 L192.0,100.4 L195.0,99.3 L198.0,98.1 L201.0,96.8 L204.0,95.4 L207.0,94.0 L210.0,92.5\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.6\"/><line x1=\"30\" y1=\"46.0\" x2=\"210\" y2=\"111.09999999999965\" stroke=\"#000000\" stroke-width=\"1.6\" stroke-dasharray=\"5 3\"/><rect x=\"31\" y=\"132\" width=\"154\" height=\"6\" rx=\"0\" fill=\"#c9ced8\" stroke=\"#000000\" stroke-width=\"1.2\"/><text x=\"108.0\" y=\"128\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">accept</text><g transform=\"translate(30.0 32.0) rotate(0) scale(0.6)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.00\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"120\" y=\"12\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Armijo: the drop must beat the dashed line</text><text x=\"216\" y=\"126\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"end\" fill=\"#000000\">\u03b1</text><text x=\"60\" y=\"76\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">fair drop</text></svg>",
    "hint": "How much altitude must a leg earn to be accepted?",
    "breakdown": [
      "<strong>$\\alpha\\nabla f(x_k)^\\top d_k$</strong> is the drop you would get if the slope stayed constant over the whole leg.",
      "<strong>$c_1$</strong> demands only a fraction of that promised drop, because the terrain curves back up.",
      "<strong>A leg that earns less than that is refused:</strong> too much fuel for too little altitude."
    ]
  },
  {
    "id": 404,
    "subject": "CMO",
    "topicId": "04_Line_Search_Methods_Exact_Armijo_and_Wolfe",
    "topicTitle": "04 \u00b7 Line Search (Armijo & Wolfe)",
    "cardNumber": "04",
    "category": "WOLFE CONDITIONS",
    "highlighterClass": "highlight-violet",
    "title": "Curvature Condition & Strong Wolfe Conditions",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-404\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"20\" y1=\"130\" x2=\"226\" y2=\"130\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-404)\"/><path d=\"M30.0,46.0 L33.0,49.1 L36.0,52.0 L39.0,55.0 L42.0,57.8 L45.0,60.5 L48.0,63.2 L51.0,65.8 L54.0,68.3 L57.0,70.8 L60.0,73.1 L63.0,75.4 L66.0,77.6 L69.0,79.8 L72.0,81.8 L75.0,83.8 L78.0,85.7 L81.0,87.5 L84.0,89.2 L87.0,90.9 L90.0,92.5 L93.0,94.0 L96.0,95.4 L99.0,96.8 L102.0,98.1 L105.0,99.3 L108.0,100.4 L111.0,101.5 L114.0,102.4 L117.0,103.3 L120.0,104.1 L123.0,104.9 L126.0,105.5 L129.0,106.1 L132.0,106.6 L135.0,107.0 L138.0,107.4 L141.0,107.7 L144.0,107.8 L147.0,108.0 L150.0,108.0 L153.0,108.0 L156.0,107.8 L159.0,107.7 L162.0,107.4 L165.0,107.0 L168.0,106.6 L171.0,106.1 L174.0,105.5 L177.0,104.9 L180.0,104.1 L183.0,103.3 L186.0,102.4 L189.0,101.5 L192.0,100.4 L195.0,99.3 L198.0,98.1 L201.0,96.8 L204.0,95.4 L207.0,94.0 L210.0,92.5\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.6\"/><line x1=\"30\" y1=\"46.0\" x2=\"100\" y2=\"118.33333333333294\" stroke=\"#000000\" stroke-width=\"1.4\" stroke-dasharray=\"4 3\"/><text x=\"60\" y=\"38.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">initial slope</text><line x1=\"110\" y1=\"108.0\" x2=\"190\" y2=\"108.0\" stroke=\"#000000\" stroke-width=\"1.6\"/><circle cx=\"150.0\" cy=\"108.0\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><g transform=\"translate(150.0 94.0) rotate(0) scale(0.6)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.00\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"120\" y=\"12\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">curvature: slope must have flattened enough</text><text x=\"120\" y=\"144\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">tiny hops on a steep slope are refused</text><text x=\"216\" y=\"126\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"end\" fill=\"#000000\">\u03b1</text></svg>",
    "drawingCaption": "After the leg the slope under you must have flattened enough compared with the starting slope; tiny hops that leave you on a steep slope are refused.",
    "coreTranslation": [
      "To prevent step sizes from becoming unproductively tiny, the <strong>Curvature Condition</strong> requires: $\\nabla f(x_k + \\alpha d_k)^T d_k \\ge c_2 \\nabla f(x_k)^T d_k$ with $c_2 \\in (c_1, 1)$ (typically $c_2 = 0.9$).",
      "This forces the slope at the new point to become significantly less steep, meaning substantial progress down the valley has been achieved.",
      "<strong>Strong Wolfe Conditions:</strong> Replaces curvature with absolute value $|\\nabla f(x_k + \\alpha d_k)^T d_k| \\le c_2 |\\nabla f(x_k)^T d_k|$, forcing the new point to be near a stationary point of $\\phi$."
    ],
    "math": "$$|\\nabla f(x_k + \\alpha_k d_k)^T d_k| \\le c_2 |\\nabla f(x_k)^T d_k|, \\quad 0 < c_1 < c_2 < 1$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Armijo stops you flying so far that you overshoot the valley; the curvature condition stops tiny hops by demanding that the slope has flattened enough after the leg.",
    "examTrap": "Constants MUST satisfy $0 < c_1 < c_2 < 1$. If $c_1 \\ge c_2$, the acceptable step size interval can become completely empty, causing line search algorithms to crash!",
    "hint": "What stops the pilot from stopping early on a slope that is still steep?",
    "breakdown": [
      "<strong>$|\\nabla f(x_k+\\alpha d)^\\top d|$ = the slope along the heading after the leg.</strong>",
      "<strong>The inequality demands it be at most $c_2$ times the starting slope:</strong> the slope must have flattened enough, so tiny hops are refused.",
      "<strong>$0\\lt c_1\\lt c_2\\lt1$</strong> keeps Armijo (not too far) and curvature (not too short) compatible: together they are the Wolfe conditions."
    ]
  },
  {
    "id": 405,
    "subject": "CMO",
    "topicId": "04_Line_Search_Methods_Exact_Armijo_and_Wolfe",
    "topicTitle": "04 \u00b7 Line Search (Armijo & Wolfe)",
    "cardNumber": "05",
    "category": "CONVERGENCE THEOREM",
    "highlighterClass": "highlight-indigo",
    "title": "Zoutendijk\u2019s Theorem & Global Convergence",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-405\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"70.0\" y1=\"100.0\" x2=\"78.0\" y2=\"38.0\" stroke=\"#000000\" stroke-width=\"2.6\" stroke-dasharray=\"4 3\" marker-end=\"url(#arr-405)\"/><text x=\"68\" y=\"34\" font-size=\"9.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"end\" fill=\"#000000\">\u2212\u2207f</text><line x1=\"70.0\" y1=\"100.0\" x2=\"168.0\" y2=\"56.0\" stroke=\"#000000\" stroke-width=\"3\" marker-end=\"url(#arr-405)\"/><text x=\"170\" y=\"54\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"start\" fill=\"#000000\">d\u2096</text><path d=\"M100,78 A32,32 0 0,1 77,69\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"108\" y=\"64\" font-size=\"11\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u03b8</text><g transform=\"translate(70.0 100.0) rotate(-25) scale(0.75)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.60\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"176\" y=\"108\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u03a3 cos\u00b2\u03b8 \u2016g\u2016\u00b2 &lt; \u221e</text><text x=\"176\" y=\"122\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u21d2 g \u2192 0 if \u03b8 \u2260 90\u00b0</text><text x=\"120\" y=\"14\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">never turn sideways to the slope</text></svg>",
    "drawingCaption": "The angle \u03b8 between your heading and straight downhill: as long as it never reaches 90\u00b0 the slope gauge is driven to zero.",
    "coreTranslation": [
      "<strong>What:</strong> Zoutendijk's theorem: if every step satisfies the Wolfe conditions, $f$ is bounded below and $\\nabla f$ is Lipschitz, then $\\sum_k\\cos^2\\theta_k\\,\\|\\nabla f(x_k)\\|^2<\\infty$.",
      "<strong>How:</strong> $\\theta_k$ is the angle between your direction $d_k$ and steepest descent $-\\nabla f(x_k)$. A sum that stays finite forces its terms $\\cos^2\\theta_k\\|\\nabla f(x_k)\\|^2$ to go to $0$.",
      "<strong>Why it matters:</strong> if the directions never turn fully sideways ($\\cos\\theta_k\\ge\\delta>0$), then $\\|\\nabla f(x_k)\\|\\to0$: the method reaches a stationary point. This one theorem proves global convergence of steepest descent, CG and BFGS."
    ],
    "math": "$$\\sum_{k=0}^\\infty \\cos^2 \\theta_k \\|\\nabla f(x_k)\\|^2 < \\infty \\implies \\lim_{k \\to \\infty} \\|\\nabla f(x_k)\\| = 0 \\quad (\\text{if } \\cos \\theta_k \\ge \\delta > 0)$$",
    "personalConnection": "<strong>The airplane analogy.</strong> As long as your heading is not turned sideways to the slope ($\\theta_k\\ne90^\\circ$), each leg keeps taking altitude and the slope gauge is driven to zero.",
    "examTrap": "If $\\cos \\theta_k \\to 0$ (directions become orthogonal to gradient), Zoutendijk's sum can converge with $\\|\\nabla f(x_k)\\| \\ge \\epsilon > 0$, causing the algorithm to fail!",
    "hint": "What must the nose never do, to guarantee the radar eventually reads zero?",
    "breakdown": [
      "<strong>$\\cos\\theta_k$ measures the alignment</strong> of the heading with straight downhill. Sideways ($\\theta=90^\\circ$) means $\\cos\\theta=0$.",
      "<strong>The sum $\\sum\\cos^2\\theta_k\\|g_k\\|^2\\lt\\infty$</strong> forces its terms to 0.",
      "<strong>If $\\cos\\theta_k\\ge\\delta\\gt0$ always,</strong> that leaves $\\|g_k\\|\\to0$: the plane reaches flat ground."
    ]
  },
  {
    "id": 406,
    "subject": "CMO",
    "topicId": "04_Line_Search_Methods_Exact_Armijo_and_Wolfe",
    "topicTitle": "04 \u00b7 Line Search (Armijo & Wolfe)",
    "cardNumber": "06",
    "category": "ALGORITHMIC IMPLEMENTATION",
    "highlighterClass": "highlight-rose",
    "title": "Backtracking Line Search Algorithm",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-406\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"20\" y1=\"130\" x2=\"226\" y2=\"130\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-406)\"/><path d=\"M30.0,46.0 L33.1,49.1 L36.1,52.2 L39.2,55.1 L42.3,58.0 L45.3,60.8 L48.4,63.6 L51.5,66.2 L54.5,68.8 L57.6,71.2 L60.7,73.6 L63.7,76.0 L66.8,78.2 L69.9,80.4 L72.9,82.4 L76.0,84.4 L79.1,86.3 L82.1,88.2 L85.2,89.9 L88.3,91.6 L91.3,93.2 L94.4,94.7 L97.5,96.1 L100.5,97.5 L103.6,98.7 L106.7,99.9 L109.7,101.0 L112.8,102.0 L115.9,103.0 L118.9,103.8 L122.0,104.6 L125.1,105.3 L128.1,105.9 L131.2,106.5 L134.3,106.9 L137.3,107.3 L140.4,107.6 L143.5,107.8 L146.5,107.9 L149.6,108.0 L152.7,108.0 L155.7,107.9 L158.8,107.7 L161.9,107.4 L164.9,107.0 L168.0,106.6 L171.1,106.1 L174.1,105.5 L177.2,104.8 L180.3,104.1 L183.3,103.2 L186.4,102.3 L189.5,101.3 L192.5,100.2 L195.6,99.0 L198.7,97.8 L201.7,96.5 L204.8,95.1 L207.9,93.6 L210.9,92.0 L214.0,90.4\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.6\"/><line x1=\"30\" y1=\"46.0\" x2=\"214\" y2=\"103.0399999999997\" stroke=\"#000000\" stroke-width=\"1.5\" stroke-dasharray=\"5 3\"/><g transform=\"translate(30.0 32.0) rotate(0) scale(0.6)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.00\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><circle cx=\"205.0\" cy=\"95.0\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"205\" y=\"144\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u03b1\u2080 \u2717</text><circle cx=\"118.0\" cy=\"103.6\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"118\" y=\"144\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u03b1\u2080/2 \u2717</text><circle cx=\"80.0\" cy=\"86.9\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"80\" y=\"144\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u03b1\u2080/4 \u2713</text><text x=\"120\" y=\"12\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">too big? halve it and look again</text></svg>",
    "drawingCaption": "Plan a long leg; if the altitude drop is too small (above the dashed line), halve the leg and check again until the drop is acceptable.",
    "coreTranslation": [
      "<strong>Algorithm:</strong> Choose $\\alpha_0 = 1$, contraction factor $\\rho \\in (0, 1)$ (e.g. $\\rho = 0.5$), and Armijo constant $c_1 \\in (0, 1)$.",
      "While $f(x_k + \\alpha d_k) > f(x_k) + c_1 \\alpha \\nabla f(x_k)^T d_k$ do: $\\alpha \\leftarrow \\rho \\alpha$. Return $\\alpha_k = \\alpha$.",
      "<strong>Why $\\alpha_0 = 1$ is Essential:</strong> For Newton and Quasi-Newton methods, starting at unit step size $\\alpha_0 = 1$ allows the algorithm to naturally adopt quadratic or superlinear convergence near $x^*$."
    ],
    "math": "$$\\alpha^{(j+1)} = \\rho \\alpha^{(j)}, \\quad \\rho \\in (0, 1), \\quad \\text{until } f(x + \\alpha d) \\le f(x) + c_1 \\alpha \\nabla f(x)^T d$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Plan a long leg, check the altitude drop; if it is too small, shorten the leg by half and check again until the drop is acceptable.",
    "examTrap": "Never start backtracking with $\\alpha_0 < 1$ in Newton's method! Restricting $\\alpha_0 < 1$ permanently degrades Newton's quadratic convergence to slow linear convergence.",
    "hint": "What does the pilot do when his planned leg earns too little altitude?",
    "breakdown": [
      "<strong>Start with a bold step</strong> $\\alpha^{(0)}$ (often 1).",
      "<strong>Multiply by $\\rho\\in(0,1)$ each time</strong> the Armijo test fails: 'halve it and look again'.",
      "<strong>Stop at the first success.</strong> It always ends, because a short enough leg always earns the promised drop."
    ]
  },
  {
    "id": 501,
    "subject": "CMO",
    "topicId": "05_Gradient_Descent_and_Convergence_Analysis",
    "topicTitle": "05 \u00b7 Gradient Descent & Convergence",
    "cardNumber": "01",
    "category": "STEEPEST DESCENT",
    "highlighterClass": "highlight-cyan",
    "title": "Method of Steepest Descent: The Pilot's Rule",
    "textbookImg": "",
    "textbookRef": "",
    "drawingCaption": "Contour lines of the terrain: the pilot points the nose exactly opposite to the steepest upward slope, perpendicular to the contour.",
    "coreTranslation": [
      "<strong>The pilot's rule:</strong> steepest descent points the plane exactly opposite to the steepest upward slope, $d_k=-\\nabla f(x_k)$. Update: $x_{k+1}=x_k-\\alpha_k\\nabla f(x_k)$, where $\\alpha_k$ is how far the plane flies before checking the radar again.",
      "<strong>Directional optimality:</strong> $-\\nabla f(x_k)$ is the direction that maximises the instantaneous rate of decrease per unit Euclidean step: $\\arg\\min_{\\|d\\|\\le1}\\nabla f(x_k)^\\top d=-\\dfrac{\\nabla f(x_k)}{\\|\\nabla f(x_k)\\|}$.",
      "<strong>Relative stop:</strong> the algorithm stops when the current slope is a tiny fraction of the starting cliff, $\\|g_k\\|\\le\\text{tol}\\cdot\\|g_0\\|$, rather than waiting for mathematically perfect flat ground."
    ],
    "math": "$$x_{k+1}=x_k-\\alpha_k\\nabla f(x_k),\\quad d_k=-\\nabla f(x_k),\\quad \\|g_k\\|\\le\\text{tol}\\cdot\\|g_0\\|$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Fly with the nose pointing exactly opposite to the steepest upward slope under your wings. Pour a drop of water on a steep roof and gravity makes it trace the same line at every millisecond. You stop when the slope gauge reads only a tiny fraction of what it read at the start (the relative stop), not when it reads exactly zero.",
    "examTrap": "Steepest descent is only steepest locally in the EUCLIDEAN norm! Changing coordinates or using a Mahalanobis norm changes the gradient direction entirely (which is why Newton's method is superior).",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-501\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><ellipse cx=\"150\" cy=\"72\" rx=\"28\" ry=\"14\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.3\" transform=\"rotate(0 150 72)\"/><ellipse cx=\"150\" cy=\"72\" rx=\"56\" ry=\"28\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.3\" transform=\"rotate(0 150 72)\"/><ellipse cx=\"150\" cy=\"72\" rx=\"84\" ry=\"42\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.3\" transform=\"rotate(0 150 72)\"/><g transform=\"translate(92.0 52.0) rotate(79.72666935837071) scale(0.8)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.50\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><line x1=\"92.0\" y1=\"52.0\" x2=\"99.8\" y2=\"95.3\" stroke=\"#000000\" stroke-width=\"2.8\" marker-end=\"url(#arr-501)\"/><text x=\"105.84714606065337\" y=\"105.29459895532896\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"start\" fill=\"#000000\">d = \u2212\u2207f</text><line x1=\"92.0\" y1=\"52.0\" x2=\"86.6\" y2=\"22.5\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"3 3\"/><text x=\"30\" y=\"24\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">steepest UP</text><circle cx=\"150.0\" cy=\"72.0\" r=\"2.6\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"150\" y=\"86\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">lowest</text><text x=\"120\" y=\"140\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">fly opposite to the steepest upward slope</text></svg>",
    "hint": "Which way should the nose point if the radar only tells you the slope under your wheels?",
    "breakdown": [
      "<strong>$\\nabla f(x_k)$ is the radar.</strong> It points up the steepest slope, so the minus sign swings the nose 180\u00b0 to point straight downhill.",
      "<strong>$\\alpha_k$ is the flight distance.</strong> Multiplying by it turns a direction into an actual displacement: how far you fly before checking the radar again.",
      "<strong>Why stop at $\\|g_k\\|\\le\\text{tol}\\,\\|g_0\\|$?</strong> Flat ground is never exactly 0.0000, so the landing check compares the slope now with the cliff you started on."
    ]
  },
  {
    "id": 508,
    "subject": "CMO",
    "topicId": "05_Gradient_Descent_and_Convergence_Analysis",
    "topicTitle": "05 \u00b7 Gradient Descent & Convergence",
    "cardNumber": "02",
    "category": "STEEPEST DESCENT",
    "highlighterClass": "highlight-amber",
    "title": "Exact Line Search, Step Size & the Zig-Zag",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-508\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><ellipse cx=\"150\" cy=\"72\" rx=\"18.0\" ry=\"9.0\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.1\" transform=\"rotate(0 150 72)\"/><ellipse cx=\"150\" cy=\"72\" rx=\"36.0\" ry=\"18.0\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.1\" transform=\"rotate(0 150 72)\"/><ellipse cx=\"150\" cy=\"72\" rx=\"56.92099788303083\" ry=\"28.460498941515414\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.1\" transform=\"rotate(0 150 72)\"/><ellipse cx=\"150\" cy=\"72\" rx=\"84.90583018850943\" ry=\"42.45291509425471\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.1\" transform=\"rotate(0 150 72)\"/><path d=\"M78.0,49.5 L103.4,81.3 L124.9,64.2 L133.8,75.2 L141.2,69.3 L144.3,73.1 L146.9,71.0\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.4\"/><g transform=\"translate(78.0 37.5) rotate(0) scale(0.65)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.85\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><circle cx=\"78.0\" cy=\"49.5\" r=\"2.2\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><circle cx=\"103.4\" cy=\"81.3\" r=\"2.2\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><circle cx=\"124.9\" cy=\"64.2\" r=\"2.2\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><circle cx=\"133.8\" cy=\"75.2\" r=\"2.2\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><circle cx=\"141.2\" cy=\"69.3\" r=\"2.2\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"150\" y=\"14\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">right angle at every turn</text><text x=\"212\" y=\"112\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"end\" fill=\"#000000\">zig-zag</text><text x=\"120\" y=\"140\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u03b1 = \u2212g\u1d40u / u\u1d40Qu : slope over brakes</text></svg>",
    "drawingCaption": "Under exact line search every turn is a right angle: the path zig-zags across the contour lines toward the lowest point.",
    "coreTranslation": [
      "<strong>Exact line search:</strong> the pilot flies perfectly straight until the altitude stops dropping and begins to curve back up.",
      "<strong>The zig-zag:</strong> because of this, consecutive search directions are perpendicular, $(x_{k+2}-x_{k+1})^\\top(x_{k+1}-x_k)=0$, so the path zig-zags across the contour lines.",
      "<strong>Step size for a quadratic:</strong> the exact distance to fly before hitting the bottom of the curve is $\\alpha=\\dfrac{-g^\\top u}{u^\\top Qu}$. The numerator is the downward momentum (how steep the slope is); the denominator is the brakes (how fast the terrain curves back up along that path)."
    ],
    "math": "$$\\alpha_k=\\frac{-g_k^\\top u_k}{u_k^\\top Q u_k},\\qquad (x_{k+2}-x_{k+1})^\\top(x_{k+1}-x_k)=0$$",
    "personalConnection": "<strong>The airplane analogy.</strong> You fly dead straight along your heading $u$ until the altimeter stops falling, and at that moment the new downhill is exactly 90 degrees to your old heading: that is the zig-zag. The slope gauge ($-g^\\top u$) says how hard you are diving; the curvature brakes ($u^\\top Qu$) say how soon the ground curves back up, so a steep dive on gently curving ground means a long leg.",
    "examTrap": "Perpendicular turns do NOT mean fast. In a long narrow valley (large condition number) the zig-zag wastes many legs. Also, the right-angle property holds only for an EXACT line search, not for Armijo/backtracking steps.",
    "hint": "What tells the pilot when to stop flying straight and turn, and why is the turn exactly 90\u00b0?",
    "breakdown": [
      "<strong>Numerator $-g^\\top u$ = downward momentum.</strong> How steeply the heading $u$ dives down the slope: a steeper dive means a longer leg.",
      "<strong>Denominator $u^\\top Qu$ = the brakes.</strong> How fast the terrain curves back up along $u$: a sharper curve means you must stop sooner.",
      "<strong>Momentum over brakes = the distance to the bottom of that straight track.</strong> Right there the new slope is perpendicular to $u$, which is why every turn is 90\u00b0 and the path zig-zags."
    ]
  },
  {
    "id": 502,
    "subject": "CMO",
    "topicId": "05_Gradient_Descent_and_Convergence_Analysis",
    "topicTitle": "05 \u00b7 Gradient Descent & Convergence",
    "cardNumber": "03",
    "category": "CONVERGENCE ANALYSIS",
    "highlighterClass": "highlight-amber",
    "title": "O(1/k) Convergence on L-Smooth Convex Objectives",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-502\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"30\" y1=\"124\" x2=\"226\" y2=\"124\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-502)\"/><line x1=\"30\" y1=\"124\" x2=\"30\" y2=\"10\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-502)\"/><path d=\"M30.0,28.0 L38.0,41.2 L46.0,51.3 L54.0,59.1 L62.0,65.5 L70.0,70.7 L78.0,75.0 L86.0,78.7 L94.0,81.9 L102.0,84.7 L110.0,87.1 L118.0,89.2 L126.0,91.1 L134.0,92.8 L142.0,94.4 L150.0,95.8 L158.0,97.0 L166.0,98.2 L174.0,99.3 L182.0,100.2 L190.0,101.1 L198.0,102.0 L206.0,102.8 L214.0,103.5 L222.0,104.2\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.6\"/><g transform=\"translate(60.0 22.0) rotate(0) scale(0.6)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.00\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"206\" y=\"76\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"end\" fill=\"#000000\">f(x\u2096) \u2212 f*</text><text x=\"206\" y=\"90\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"end\" fill=\"#000000\">\u2264 L\u2016x\u2080\u2212x*\u2016\u00b2 / 2k</text><text x=\"206\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"end\" fill=\"#000000\">k (legs flown)</text><text x=\"150\" y=\"108\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">last metres: many legs</text></svg>",
    "drawingCaption": "Descending with step 1/L: the first legs shed lots of altitude, the last metres above the valley floor take many legs, so the gap shrinks only like 1/k.",
    "coreTranslation": [
      "A function is <strong>$L$-Smooth</strong> if $\\|\\nabla f(x) - \\nabla f(y)\\| \\le L \\|x - y\\|$, which implies the Descent Lemma: $f(y) \\le f(x) + \\nabla f(x)^T(y-x) + \\frac{L}{2}\\|y-x\\|^2$.",
      "Taking step size $\\alpha = 1/L$: $f(x_{k+1}) \\le f(x_k) - \\frac{1}{2L}\\|\\nabla f(x_k)\\|^2$, guaranteeing strict monotonic decrease.",
      "<strong>Theorem:</strong> For any convex $L$-smooth function with constant step $\\alpha = 1/L$, the suboptimality error decays as: $f(x_k) - f^* \\le \\frac{L \\|x_0 - x^*\\|^2}{2k}$."
    ],
    "math": "$$f(x_k) - f^* \\le \\frac{L \\|x_0 - x^*\\|^2}{2k} = \\mathcal{O}\\left(\\frac{1}{k}\\right)$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Descending with step $1/L$: the first legs shed lots of altitude, but squeezing out the last few metres above the valley floor takes progressively more legs, so the gap shrinks only like $1/k$.",
    "examTrap": "If the step size $\\alpha \\ge 2/L$, gradient descent can violently DIVERGE! The stability threshold is strictly $\\alpha < 2/L$.",
    "hint": "Why can the pilot fly legs of exactly $1/L$ without ever overshooting the valley?",
    "breakdown": [
      "<strong>$L$ = the sharpest bend anywhere.</strong> The ground can never curve back up faster than $L$, so a leg of $1/L$ is a safe distance everywhere.",
      "<strong>$\\|x_0-x^*\\|^2$ = how far away you start.</strong> A bigger first cliff means a bigger gap to close.",
      "<strong>Dividing by $2k$:</strong> each extra leg trims only a shrinking share of what is left, so the error falls like $1/k$ (sublinear), not geometrically."
    ]
  },
  {
    "id": 503,
    "subject": "CMO",
    "topicId": "05_Gradient_Descent_and_Convergence_Analysis",
    "topicTitle": "05 \u00b7 Gradient Descent & Convergence",
    "cardNumber": "04",
    "category": "LINEAR CONVERGENCE",
    "highlighterClass": "highlight-emerald",
    "title": "Linear Convergence on Strongly Convex Functions",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-503\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"14\" y1=\"124\" x2=\"226\" y2=\"124\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-503)\"/><rect x=\"24\" y=\"34.0\" width=\"26\" height=\"90.0\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"37\" y=\"136\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">k=0</text><line x1=\"52.0\" y1=\"40.0\" x2=\"62.0\" y2=\"64.2\" stroke=\"#000000\" stroke-width=\"1.4\" marker-end=\"url(#arr-503)\"/><text x=\"57\" y=\"30.0\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u00d7\u03c1</text><rect x=\"64\" y=\"68.2\" width=\"26\" height=\"55.8\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"77\" y=\"136\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">k=1</text><line x1=\"92.0\" y1=\"74.2\" x2=\"102.0\" y2=\"85.4\" stroke=\"#000000\" stroke-width=\"1.4\" marker-end=\"url(#arr-503)\"/><text x=\"97\" y=\"64.2\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u00d7\u03c1</text><rect x=\"104\" y=\"89.404\" width=\"26\" height=\"34.596000000000004\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"117\" y=\"136\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">k=2</text><line x1=\"132.0\" y1=\"95.4\" x2=\"142.0\" y2=\"98.6\" stroke=\"#000000\" stroke-width=\"1.4\" marker-end=\"url(#arr-503)\"/><text x=\"137\" y=\"85.404\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u00d7\u03c1</text><rect x=\"144\" y=\"102.55048\" width=\"26\" height=\"21.44952\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"157\" y=\"136\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">k=3</text><line x1=\"172.0\" y1=\"108.6\" x2=\"182.0\" y2=\"106.7\" stroke=\"#000000\" stroke-width=\"1.4\" marker-end=\"url(#arr-503)\"/><rect x=\"184\" y=\"110.7012976\" width=\"26\" height=\"13.298702399999998\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"197\" y=\"136\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">k=4</text><g transform=\"translate(206.0 40.0) rotate(180) scale(0.6)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.00\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"200\" y=\"62\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"end\" fill=\"#000000\">\u03c1 = 1 \u2212 \u03bc/L</text><text x=\"200\" y=\"76\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"end\" fill=\"#000000\">gap \u00d7 \u03c1 per leg</text></svg>",
    "drawingCaption": "Every leg removes the same fraction of the altitude still left above the valley floor: the gap is multiplied by \u03c1<1 each leg.",
    "coreTranslation": [
      "When $f$ is both $\\mu$-strongly convex and $L$-smooth, the condition number is $\\kappa = L / \\mu \\ge 1$.",
      "<strong>Linear Convergence Rate:</strong> Gradient descent with optimal constant step size $\\alpha = \\frac{2}{L+\\mu}$ contracts the distance to the optimum geometrically: $\\|x_k - x^*\\| \\le \\left(\\frac{\\kappa - 1}{\\kappa + 1}\\right)^k \\|x_0 - x^*\\|$.",
      "In optimization terminology, 'linear convergence' means that the log-error $\\log \\|x_k - x^*\\|$ decreases linearly with iteration count $k$."
    ],
    "math": "$$\\|x_k - x^*\\| \\le \\left(\\frac{\\kappa - 1}{\\kappa + 1}\\right)^k \\|x_0 - x^*\\|, \\quad \\kappa = \\frac{L}{\\mu}$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Each leg removes a fixed fraction of the altitude still left above the valley floor, like a glide path losing the same percentage every mile: error is multiplied by $\\rho\\lt1$ per leg, so the gap vanishes geometrically.",
    "examTrap": "Don't confuse computer science linear time $O(k)$ with optimization 'linear convergence'! Linear convergence in optimization means geometric/exponential decay $O(\\rho^k)$, which is dramatically faster than sublinear $O(1/k)$.",
    "hint": "By what fixed fraction does each leg shrink the distance to the valley floor?",
    "breakdown": [
      "<strong>$\\kappa=L/\\mu$ = sharpest bend over gentlest bend.</strong> It measures how stretched the valley is.",
      "<strong>$\\frac{\\kappa-1}{\\kappa+1}$ = the contraction per leg.</strong> A round bowl ($\\kappa=1$) gives 0 (one leg); a long thin canyon ($\\kappa$ large) gives almost 1 (almost no progress).",
      "<strong>The power $k$:</strong> the same fraction is multiplied in again on every leg, so the error decays geometrically (linear convergence)."
    ]
  },
  {
    "id": 504,
    "subject": "CMO",
    "topicId": "05_Gradient_Descent_and_Convergence_Analysis",
    "topicTitle": "05 \u00b7 Gradient Descent & Convergence",
    "cardNumber": "05",
    "category": "KANTOROVICH INEQUALITY",
    "highlighterClass": "highlight-violet",
    "title": "Kantorovich Inequality & Quadratic Bound",
    "textbookImg": "assets/luenberger_fig8_10.png",
    "textbookRef": "Luenberger & Ye (4th ed), Sect. 8.3, Fig. 8.10 (p. 245)",
    "drawingCaption": "The nose (\u2212g) is never perfectly aligned with the valley axis; Kantorovich bounds the worst misalignment, and with it the least altitude you must gain per leg.",
    "coreTranslation": [
      "<strong>What:</strong> steepest descent with exact line search on a quadratic shrinks the error every step by at least the factor $\\left(\\frac{\\kappa-1}{\\kappa+1}\\right)^2$, where $\\kappa=\\lambda_{\\max}/\\lambda_{\\min}$.",
      "<strong>How:</strong> the Kantorovich inequality $\\frac{(x^Tx)^2}{(x^TQx)(x^TQ^{-1}x)}\\ge\\frac{4\\lambda_{\\max}\\lambda_{\\min}}{(\\lambda_{\\max}+\\lambda_{\\min})^2}$ limits how badly the gradient can point away from the axes of the elliptical bowl.",
      "<strong>Why it matters:</strong> $\\kappa=1$ gives $0$ (one step). $\\kappa=100$ gives $(99/101)^2\\approx0.96$ per step, so it takes about 50 steps just to halve the error. The bound is tight: a worst-case start achieves it at every step."
    ],
    "math": "$$\\frac{(x^T x)^2}{(x^T Q x)(x^T Q^{-1} x)} \\ge \\frac{4 A a}{(A + a)^2} \\implies E(x_{k+1}) \\le \\left(\\frac{\\kappa - 1}{\\kappa + 1}\\right)^2 E(x_k)$$",
    "personalConnection": "<strong>The airplane analogy.</strong> The worst-case guarantee: how badly can your nose ($-g$) be misaligned with the valley's long axis? Kantorovich bounds that misalignment, and with it the least altitude you must gain back per leg.",
    "examTrap": "The rate bound is TIGHT! For starting points aligned at 45 degrees to the principal eigenvectors, steepest descent achieves the exact upper bound $\\left(\\frac{\\kappa-1}{\\kappa+1}\\right)^2$ at every single iteration.",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-504\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><ellipse cx=\"150\" cy=\"76\" rx=\"13.063945294843617\" ry=\"32.0\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.2\" transform=\"rotate(-90.0 150 76)\"/><ellipse cx=\"150\" cy=\"76\" rx=\"23.094010767585033\" ry=\"56.568542494923804\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.2\" transform=\"rotate(-90.0 150 76)\"/><ellipse cx=\"150\" cy=\"76\" rx=\"34.25395354310701\" ry=\"83.90470785361212\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.2\" transform=\"rotate(-90.0 150 76)\"/><g transform=\"translate(78.0 58.4) rotate(55.71312302279106) scale(0.75)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.60\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><line x1=\"78.0\" y1=\"58.4\" x2=\"99.4\" y2=\"89.8\" stroke=\"#000000\" stroke-width=\"2.6\" marker-end=\"url(#arr-504)\"/><text x=\"103.40679933637736\" y=\"101.79663902668682\" font-size=\"9.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"start\" fill=\"#000000\">\u2212g</text><line x1=\"86.0\" y1=\"54.4\" x2=\"140.0\" y2=\"74.0\" stroke=\"#000000\" stroke-width=\"1.6\" stroke-dasharray=\"4 3\" marker-end=\"url(#arr-504)\"/><text x=\"86\" y=\"108\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">valley axis</text><circle cx=\"150.0\" cy=\"76.0\" r=\"2.4\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"188\" y=\"20\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u03b8 = misalignment</text><text x=\"150\" y=\"140\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">worst case: cos \u03b8 \u2265 2\u221a\u03ba/(\u03ba+1)</text></svg>",
    "hint": "How badly can the nose be misaligned with the valley axis, and what does it cost per leg?",
    "breakdown": [
      "<strong>The ratio $\\frac{(x^\\top x)^2}{(x^\\top Qx)(x^\\top Q^{-1}x)}$</strong> compares straight downhill with the valley's two extreme curvatures; it equals 1 when the nose is perfectly aligned.",
      "<strong>$\\frac{4Aa}{(A+a)^2}$ = the worst case.</strong> It is set by the sharpest curvature $A$ and the gentlest curvature $a$.",
      "<strong>Result:</strong> each leg shrinks the altitude gap above the floor by at least $\\left(\\frac{\\kappa-1}{\\kappa+1}\\right)^2$, the square of the distance rate."
    ]
  },
  {
    "id": 505,
    "subject": "CMO",
    "topicId": "05_Gradient_Descent_and_Convergence_Analysis",
    "topicTitle": "05 \u00b7 Gradient Descent & Convergence",
    "cardNumber": "06",
    "category": "CONDITION NUMBER DYNAMICS",
    "highlighterClass": "highlight-indigo",
    "title": "Condition Number \u03ba & The Zig-Zag Phenomenon",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-505\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><ellipse cx=\"140\" cy=\"74\" rx=\"9.561828874675149\" ry=\"35.77708763999664\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.3\" transform=\"rotate(-90.0 140 74)\"/><ellipse cx=\"140\" cy=\"74\" rx=\"17.88854381999832\" ry=\"66.93280212272605\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.3\" transform=\"rotate(-90.0 140 74)\"/><ellipse cx=\"140\" cy=\"74\" rx=\"28.685486624025447\" ry=\"107.33126291998991\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.3\" transform=\"rotate(-90.0 140 74)\"/><path d=\"M40.0,63.6 L50.2,78.4 L67.6,66.5 L74.9,77.2 L87.5,68.5 L92.9,76.3 L102.0,70.0\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.4\"/><g transform=\"translate(36.0 49.6) rotate(0) scale(0.6)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.00\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"120\" y=\"18\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">narrow canyon: large \u03ba</text><text x=\"120\" y=\"140\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">bounces off the walls, crawls along the floor</text></svg>",
    "drawingCaption": "In a long thin canyon (large condition number \u03ba) heading perpendicular to the contour slams you into the opposite wall; progress along the floor is slow.",
    "coreTranslation": [
      "The condition number $\\kappa = \\frac{\\lambda_{\\max}}{\\lambda_{\\min}}$ measures the eccentric elongation of objective level contours.",
      "<strong>If $\\kappa = 1$ (Spherical Contours):</strong> $\\frac{\\kappa-1}{\\kappa+1} = 0$. Steepest descent points directly at the center and converges in exactly <strong>ONE step</strong>!",
      "<strong>If $\\kappa = 1000$ (Elongated Canyon):</strong> $\\frac{\\kappa-1}{\\kappa+1} = \\frac{999}{1001} \\approx 0.998$. The algorithm bounces back and forth across canyon walls, making almost zero forward progress per step."
    ],
    "math": "$$\\kappa = \\frac{\\lambda_{\\max}}{\\lambda_{\\min}}, \\quad \\lim_{\\kappa \\to \\infty} \\frac{\\kappa - 1}{\\kappa + 1} = 1 \\implies \\text{Stagnation}$$",
    "personalConnection": "<strong>The airplane analogy.</strong> A narrow canyon: heading perpendicular to the contour sends you straight into the opposite canyon wall instead of down the stream. The longer and thinner the valley (large condition number $\\kappa$), the worse the zig-zag.",
    "examTrap": "Preconditioning transforms coordinates ($y = P x$) to make the condition number $\\kappa(P^{-T} Q P^{-1}) \\approx 1$, curing the zig-zag phenomenon without changing the minimum point.",
    "hint": "Why does a very long, thin canyon make the pilot zig-zag instead of flying down the middle?",
    "breakdown": [
      "<strong>$\\lambda_{\\max}$ = the steep canyon wall, $\\lambda_{\\min}$ = the gentle floor.</strong> Their ratio $\\kappa$ says how stretched the valley is.",
      "<strong>The radar mostly sees the steep wall,</strong> so the nose points across the canyon and each leg slams into the opposite side.",
      "<strong>As $\\kappa\\to\\infty$ the factor $\\frac{\\kappa-1}{\\kappa+1}\\to1$:</strong> each leg barely shrinks the error, which is the stagnation."
    ]
  },
  {
    "id": 506,
    "subject": "CMO",
    "topicId": "05_Gradient_Descent_and_Convergence_Analysis",
    "topicTitle": "05 \u00b7 Gradient Descent & Convergence",
    "cardNumber": "07",
    "category": "STEP-SIZE RULES",
    "highlighterClass": "highlight-rose",
    "title": "Barzilai\u2013Borwein Step Sizes (No Line Search)",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-506\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"20\" y1=\"126\" x2=\"226\" y2=\"126\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-506)\"/><path d=\"M20.0,126.0 L25.1,120.3 L30.3,114.9 L35.5,109.8 L40.6,104.9 L45.8,100.4 L50.9,96.1 L56.0,92.1 L61.2,88.4 L66.3,85.0 L71.5,81.9 L76.7,79.0 L81.8,76.4 L87.0,74.1 L92.1,72.1 L97.2,70.4 L102.4,69.0 L107.5,67.8 L112.7,66.9 L117.8,66.4 L123.0,66.0 L128.2,66.0 L133.3,66.3 L138.4,66.8 L143.6,67.7 L148.8,68.8 L153.9,70.2 L159.1,71.8 L164.2,73.8 L169.3,76.0 L174.5,78.6 L179.7,81.4 L184.8,84.5 L189.9,87.8 L195.1,91.5 L200.2,95.4 L205.4,99.7 L210.6,104.2 L215.7,109.0 L220.8,114.0 L226.0,119.4\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.4\"/><circle cx=\"70.0\" cy=\"126.0\" r=\"2.4\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><circle cx=\"118.0\" cy=\"126.0\" r=\"2.4\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><g transform=\"translate(70.0 114.0) rotate(0) scale(0.6)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.00\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"70\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">x\u2096\u208b\u2081</text><text x=\"118\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">x\u2096</text><line x1=\"72.0\" y1=\"120.0\" x2=\"116.0\" y2=\"120.0\" stroke=\"#000000\" stroke-width=\"2.2\" marker-end=\"url(#arr-506)\"/><text x=\"94\" y=\"112\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">s</text><line x1=\"150\" y1=\"124\" x2=\"150\" y2=\"98\" stroke=\"#000000\" stroke-width=\"1.6\"/><line x1=\"150.0\" y1=\"124.0\" x2=\"150.0\" y2=\"98.0\" stroke=\"#000000\" stroke-width=\"2\" marker-end=\"url(#arr-506)\"/><text x=\"156\" y=\"112\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"start\" fill=\"#000000\">y</text><text x=\"150\" y=\"56\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"start\" fill=\"#000000\">\u03b1 = s\u1d40s / s\u1d40y</text><text x=\"150\" y=\"68\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">(no radar sweep)</text><text x=\"40\" y=\"22\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">how far you flew (s)</text><text x=\"40\" y=\"34\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">vs how the slope changed (y)</text></svg>",
    "drawingCaption": "Size the next leg from the last two footprints: how far you flew (s) against how much the slope gauge changed (y).",
    "coreTranslation": [
      "<strong>What:</strong> choose the step size from the last two iterates instead of running a line search.",
      "<strong>How:</strong> let $s=x_k-x_{k-1}$ and $y=g_k-g_{k-1}$. Pretend the Hessian is $\\approx hI$ and fit the secant $hs\\approx y$; then the step is $\\alpha=1/h$, giving $\\alpha^{BB1}=\\frac{s^Ts}{s^Ty}$ (long step) or $\\alpha^{BB2}=\\frac{s^Ty}{y^Ty}$ (short step).",
      "<strong>Why it matters:</strong> BB steps are cheap (no function evaluations) and converge dramatically faster than fixed steps on ill-conditioned problems. The price: the objective is <em>not</em> decreased at every step."
    ],
    "math": "$$\\alpha_k^{BB1}=\\frac{s_{k}^{T}s_{k}}{s_{k}^{T}y_{k}},\\qquad \\alpha_k^{BB2}=\\frac{s_{k}^{T}y_{k}}{y_{k}^{T}y_{k}},\\qquad s_k=x_k-x_{k-1},\\ \\ y_k=g_k-g_{k-1}$$",
    "personalConnection": "<strong>The airplane analogy.</strong> No radar sweeps: size your next leg from your last two footprints, how far you flew ($s$) compared with how much the slope gauge changed ($y$), so the stride matches the terrain.",
    "examTrap": "BB iterations are non-monotone: f can go up for a few steps and that is expected. Forcing a strict descent line search on top destroys the speed-up. Also check s\u1d40y > 0 before dividing.",
    "hint": "How can the pilot size the next leg from the last two footprints with no radar sweep?",
    "breakdown": [
      "<strong>$s_k$ = how far you flew; $y_k$ = how much the slope reading changed.</strong> Together they say how fast the ground curves along your path.",
      "<strong>BB1 $=s^\\top s/s^\\top y$</strong> is distance squared over slope change: one over the local curvature, which is the bottom-of-the-curve distance.",
      "<strong>BB2 $=s^\\top y/y^\\top y$</strong> is the same idea measured from the slope side. Neither needs a line search."
    ]
  },
  {
    "id": 507,
    "subject": "CMO",
    "topicId": "05_Gradient_Descent_and_Convergence_Analysis",
    "topicTitle": "05 \u00b7 Gradient Descent & Convergence",
    "cardNumber": "08",
    "category": "ACCELERATED METHODS",
    "highlighterClass": "highlight-rose",
    "title": "Heavy-Ball Momentum & Nesterov",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-507\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><ellipse cx=\"150\" cy=\"74\" rx=\"8.0\" ry=\"27.712812921102035\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.2\" transform=\"rotate(-90.0 150 74)\"/><ellipse cx=\"150\" cy=\"74\" rx=\"16.32993161855452\" ry=\"56.568542494923804\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.2\" transform=\"rotate(-90.0 150 74)\"/><ellipse cx=\"150\" cy=\"74\" rx=\"29.21186973360886\" ry=\"101.19288512538814\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.2\" transform=\"rotate(-90.0 150 74)\"/><path d=\"M54.0,64.4 L66.8,79.8 L81.9,67.2 L91.0,78.1 L101.7,69.2 L108.2,76.9 L115.8,70.6\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.4\" stroke-dasharray=\"3 3\"/><path d=\"M38.0,62.0 L70.0,74.0 L100.0,75.0 L126.0,74.5 L150.0,74.0\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.8\"/><g transform=\"translate(38.0 62.0) rotate(20) scale(0.7)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.71\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"120\" y=\"20\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">plain: bounces (dashed)</text><text x=\"120\" y=\"134\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">momentum: keeps its heading, rolls down the floor</text><circle cx=\"150.0\" cy=\"74.0\" r=\"2.4\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/></svg>",
    "drawingCaption": "A heavy airliner keeps its heading through small gusts: the momentum path (solid) glides down the canyon floor while plain steepest descent (dashed) rattles between the walls.",
    "coreTranslation": [
      "<strong>What:</strong> add a fraction $\\beta$ of the previous step to the gradient step: $x_{k+1}=x_k-\\alpha\\nabla f(x_k)+\\beta\\,(x_k-x_{k-1})$.",
      "<strong>How:</strong> the wall-to-wall bounces cancel out because they flip sign every step, while the steady motion along the valley adds up. It is a heavy ball rolling with inertia.",
      "<strong>Why it matters:</strong> with the best $\\alpha,\\beta$ on a quadratic, the rate improves from $\\frac{\\kappa-1}{\\kappa+1}$ to $\\frac{\\sqrt\\kappa-1}{\\sqrt\\kappa+1}$. For $\\kappa=100$ that is $0.98\\to0.82$ per step, about <strong>10\u00d7 fewer iterations</strong>."
    ],
    "math": "$$x_{k+1}=x_k-\\alpha\\nabla f(x_k)+\\beta(x_k-x_{k-1}),\\qquad \\text{rate}\\ \\ \\frac{\\sqrt\\kappa-1}{\\sqrt\\kappa+1}\\ \\text{ vs }\\ \\frac{\\kappa-1}{\\kappa+1}$$",
    "personalConnection": "<strong>The airplane analogy.</strong> A heavy airliner keeps its heading through small gusts, so it rattles less between the canyon walls and holds the line down the valley. Nesterov looks ahead along the heading before correcting.",
    "examTrap": "Heavy ball's speed-up is proven for quadratics. For general convex functions use Nesterov's version, which takes the gradient at the look-ahead point $x_k+\\beta(x_k-x_{k-1})$ and has the optimal $O(1/k^2)$ guarantee.",
    "hint": "What lets a heavy plane keep rolling down the canyon instead of bouncing off the walls?",
    "breakdown": [
      "<strong>$-\\alpha\\nabla f(x_k)$</strong> is the usual radar-guided push downhill.",
      "<strong>$\\beta(x_k-x_{k-1})$ = momentum.</strong> The last leg's displacement carries you on, so the side-to-side bounces cancel while the steady downhill part adds up.",
      "<strong>The rate $\\frac{\\sqrt\\kappa-1}{\\sqrt\\kappa+1}$</strong> uses $\\sqrt\\kappa$ instead of $\\kappa$, so thin canyons cost far fewer legs."
    ]
  },
  {
    "id": 601,
    "subject": "CMO",
    "topicId": "06_Newtons_Method_and_Hessian_Modifications",
    "topicTitle": "06 \u00b7 Newton\u2019s Method & Modifications",
    "cardNumber": "01",
    "category": "SECOND-ORDER OPTIMIZATION",
    "highlighterClass": "highlight-cyan",
    "title": "Pure Newton\u2019s Method & Parabolic Model",
    "textbookImg": "assets/luenberger_fig8_5.png",
    "textbookRef": "Luenberger & Ye (4th ed), Sect. 8.5, Fig. 8.5 (p. 231)",
    "drawingCaption": "The autopilot fits a parabola to the local terrain (slope and curvature gauges) and flies straight to the bottom of that model in one leg.",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-601\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><path d=\"M20.0,56.1 L23.4,56.1 L26.9,56.2 L30.3,56.3 L33.7,56.4 L37.2,56.5 L40.6,56.7 L44.0,57.0 L47.5,57.3 L50.9,57.7 L54.3,58.2 L57.8,58.9 L61.2,59.6 L64.6,60.6 L68.1,61.7 L71.5,63.0 L74.9,64.6 L78.4,66.4 L81.8,68.4 L85.2,70.7 L88.7,73.2 L92.1,75.9 L95.5,78.9 L99.0,82.0 L102.4,85.2 L105.8,88.5 L109.3,91.8 L112.7,95.1 L116.1,98.2 L119.6,101.0 L123.0,103.6 L126.4,105.9 L129.9,107.6 L133.3,109.0 L136.7,109.8 L140.2,110.0 L143.6,109.7 L147.0,108.9 L150.5,107.5 L153.9,105.7 L157.3,103.4 L160.8,100.8 L164.2,97.9 L167.6,94.8 L171.1,91.5 L174.5,88.2 L177.9,84.9 L181.4,81.7 L184.8,78.6 L188.2,75.7 L191.7,73.0 L195.1,70.5 L198.5,68.2 L202.0,66.2 L205.4,64.4 L208.8,62.9 L212.3,61.6 L215.7,60.5 L219.1,59.6 L222.6,58.8 L226.0,58.2\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.6\"/><path d=\"M76.0,38.2 L78.8,43.9 L81.6,49.4 L84.4,54.7 L87.2,59.7 L90.0,64.5 L92.8,69.0 L95.6,73.4 L98.4,77.5 L101.2,81.3 L104.0,85.0 L106.8,88.4 L109.6,91.6 L112.4,94.5 L115.2,97.3 L118.0,99.7 L120.8,102.0 L123.6,104.1 L126.4,105.9 L129.2,107.4 L132.0,108.8 L134.8,109.9 L137.6,110.8 L140.4,111.5 L143.2,111.9 L146.0,112.1 L148.8,112.1 L151.6,111.8 L154.4,111.3 L157.2,110.6 L160.0,109.7 L162.8,108.5 L165.6,107.1 L168.4,105.4 L171.2,103.6 L174.0,101.5 L176.8,99.2 L179.6,96.6 L182.4,93.8 L185.2,90.8 L188.0,87.6\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.6\" stroke-dasharray=\"4 3\"/><g transform=\"translate(118.0 88.9) rotate(0) scale(0.6)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.00\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><circle cx=\"122.0\" cy=\"102.9\" r=\"2.6\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"116\" y=\"116.9\" font-size=\"9.5\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"end\" fill=\"#000000\">x\u2096</text><circle cx=\"147.1\" cy=\"112.1\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><line x1=\"147.1\" y1=\"112.1\" x2=\"147.1\" y2=\"124.0\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"2 2\"/><text x=\"147.05751202718355\" y=\"136\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">x\u2096\u208a\u2081</text><line x1=\"126.0\" y1=\"124.0\" x2=\"143.1\" y2=\"124.0\" stroke=\"#000000\" stroke-width=\"2\" marker-end=\"url(#arr-601)\"/><text x=\"120\" y=\"16\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">fit a parabola, fly to its bottom</text></svg>",
    "coreTranslation": [
      "<strong>What:</strong> Newton's method replaces $f$ near $x_k$ by its best-fitting parabola (the second-order Taylor model) and jumps straight to the bottom of that parabola.",
      "<strong>How:</strong> the model is $q(p)=f(x_k)+\\nabla f(x_k)^Tp+\\tfrac12p^T\\nabla^2f(x_k)\\,p$. Setting $\\nabla q=0$ gives the linear system $\\nabla^2f(x_k)\\,p_k=-\\nabla f(x_k)$, and then $x_{k+1}=x_k+p_k$.",
      "<strong>Why it matters:</strong> on a quadratic it lands on the exact minimum in one step, and near a minimum it converges extremely fast. It is also <em>affine invariant</em>: rescaling the coordinates does not change its path, unlike gradient descent."
    ],
    "math": "$$x_{k+1} = x_k - [\\nabla^2 f(x_k)]^{-1} \\nabla f(x_k), \\quad \\nabla^2 f(x_k) p_k = -\\nabla f(x_k)$$",
    "personalConnection": "<strong>The airplane analogy.</strong> The autopilot fits a parabola-shaped model of the terrain from the slope and curvature gauges and flies straight to the lowest point of that model in one leg, instead of inching along with the slope alone.",
    "examTrap": "NEVER invert the Hessian matrix explicitly ($H^{-1}$)! Inverting an $n \\times n$ matrix costs $\\mathcal{O}(n^3)$ operations and destroys sparsity. Always solve the linear system $H_k p_k = -g_k$ via Cholesky factorization.",
    "hint": "What shape does the autopilot fit to the terrain, and where does it fly?",
    "breakdown": [
      "<strong>$\\nabla^2f$ = the radar that sees curvature,</strong> not only the slope but how fast the slope changes.",
      "<strong>Solving $\\nabla^2f\\,p=-\\nabla f$</strong> flies to the bottom of the parabola built from slope and curvature.",
      "<strong>The inverse Hessian rescales the nose:</strong> steep walls get short moves, flat floors long moves, so the zig-zag disappears."
    ]
  },
  {
    "id": 602,
    "subject": "CMO",
    "topicId": "06_Newtons_Method_and_Hessian_Modifications",
    "topicTitle": "06 \u00b7 Newton\u2019s Method & Modifications",
    "cardNumber": "02",
    "category": "CONVERGENCE THEORY",
    "highlighterClass": "highlight-amber",
    "title": "Quadratic (Superlinear) Local Convergence",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-602\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"14\" y1=\"124\" x2=\"226\" y2=\"124\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-602)\"/><rect x=\"30\" y=\"116\" width=\"30\" height=\"8\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"45\" y=\"136\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">leg 1</text><text x=\"45\" y=\"112\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">1 digits</text><rect x=\"78\" y=\"106\" width=\"30\" height=\"18\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"93\" y=\"136\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">leg 2</text><text x=\"93\" y=\"102\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">2 digits</text><rect x=\"126\" y=\"86\" width=\"30\" height=\"38\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"141\" y=\"136\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">leg 3</text><text x=\"141\" y=\"82\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">4 digits</text><rect x=\"174\" y=\"46\" width=\"30\" height=\"78\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"189\" y=\"136\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">leg 4</text><text x=\"189\" y=\"42\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">8 digits</text><g transform=\"translate(40.0 40.0) rotate(0) scale(0.6)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.00\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"120\" y=\"18\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">inside the final approach bubble</text><text x=\"120\" y=\"30\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">correct digits double each leg</text></svg>",
    "drawingCaption": "Inside the terminal approach bubble each leg squares the remaining error, so the number of correct digits roughly doubles every leg.",
    "coreTranslation": [
      "<strong>What:</strong> near a strict local minimum, Newton's error is <em>squared</em> at every step: $\\|x_{k+1}-x^*\\|\\le\\frac{L}{2m}\\|x_k-x^*\\|^2$.",
      "<strong>How:</strong> it needs three things: $\\nabla^2f(x^*)\\succeq mI$ with $m>0$, a Hessian that is $L$-Lipschitz near $x^*$, and a start close enough that $\\frac{L}{2m}\\|x_0-x^*\\|<1$.",
      "<strong>Why it matters:</strong> squaring the error doubles the number of correct digits each step: $10^{-1}\\to10^{-2}\\to10^{-4}\\to10^{-8}$. It is called <em>quadratic</em> convergence, and it is faster than superlinear."
    ],
    "math": "$$\\|x_{k+1} - x^*\\| \\le \\frac{L}{2 m} \\|x_k - x^*\\|^2 \\quad \\implies \\quad \\lim_{k\\to\\infty} \\frac{\\|x_{k+1} - x^*\\|}{\\|x_k - x^*\\|} = 0 \\; (\\text{Superlinear})$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Far from the airfield the autopilot manoeuvres cautiously; once inside the terminal approach bubble each leg squares the remaining error, so the number of correct digits roughly doubles.",
    "examTrap": "Quadratic convergence is strictly a LOCAL property! If $x_0$ is outside the radius of attraction, Newton's method can oscillate wildly or diverge to infinity.",
    "hint": "What happens to the error once you are inside the terminal approach bubble?",
    "breakdown": [
      "<strong>$\\|x_k-x^*\\|^2$:</strong> the error is squared each leg, so $0.1\\to0.01\\to0.0001$ and the number of correct digits doubles.",
      "<strong>$\\frac{L}{2m}$ = roughest bend over gentlest bend</strong> controls how small the bubble is: the bigger the ratio, the closer you must start.",
      "<strong>Superlinear:</strong> the ratio of successive errors tends to 0, faster than any fixed geometric rate."
    ]
  },
  {
    "id": 603,
    "subject": "CMO",
    "topicId": "06_Newtons_Method_and_Hessian_Modifications",
    "topicTitle": "06 \u00b7 Newton\u2019s Method & Modifications",
    "cardNumber": "03",
    "category": "FAILURE MODES",
    "highlighterClass": "highlight-rose",
    "title": "Failure Modes: Non-Convexity & Saddle Points",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-603\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><path d=\"M20.0,81.9 L23.4,82.4 L26.9,82.9 L30.3,83.4 L33.7,83.8 L37.2,84.2 L40.6,84.4 L44.0,84.5 L47.5,84.5 L50.9,84.2 L54.3,83.7 L57.8,82.9 L61.2,81.8 L64.6,80.3 L68.1,78.4 L71.5,76.1 L74.9,73.3 L78.4,70.2 L81.8,66.6 L85.2,62.7 L88.7,58.6 L92.1,54.4 L95.5,50.2 L99.0,46.2 L102.4,42.4 L105.8,39.2 L109.3,36.7 L112.7,34.8 L116.1,33.9 L119.6,33.9 L123.0,34.9 L126.4,36.8 L129.9,39.7 L133.3,43.3 L136.7,47.6 L140.2,52.4 L143.6,57.7 L147.0,63.1 L150.5,68.5 L153.9,73.9 L157.3,79.1 L160.8,84.0 L164.2,88.5 L167.6,92.6 L171.1,96.3 L174.5,99.5 L177.9,102.3 L181.4,104.8 L184.8,106.9 L188.2,108.7 L191.7,110.2 L195.1,111.6 L198.5,112.7 L202.0,113.8 L205.4,114.7 L208.8,115.5 L212.3,116.3 L215.7,117.0 L219.1,117.7 L222.6,118.4 L226.0,119.0\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.6\"/><path d=\"M62.0,73.2 L66.3,66.8 L70.5,60.9 L74.8,55.5 L79.1,50.4 L83.3,45.8 L87.6,41.7 L91.9,38.0 L96.1,34.7 L100.4,31.9 L104.7,29.5 L108.9,27.5 L113.2,26.0 L117.5,24.9 L121.7,24.2 L126.0,24.0 L130.3,24.2 L134.5,24.9 L138.8,26.0 L143.1,27.5 L147.3,29.5 L151.6,31.9 L155.9,34.7 L160.1,38.0 L164.4,41.7 L168.7,45.8 L172.9,50.4 L177.2,55.5 L181.5,60.9 L185.7,66.8 L190.0,73.2\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.4\" stroke-dasharray=\"4 3\"/><g transform=\"translate(88.0 38.5) rotate(0) scale(0.6)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.00\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><circle cx=\"126.0\" cy=\"24.0\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><line x1=\"98.0\" y1=\"36.5\" x2=\"120.0\" y2=\"28.0\" stroke=\"#000000\" stroke-width=\"2.2\" marker-end=\"url(#arr-603)\"/><text x=\"150\" y=\"14\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"start\" fill=\"#000000\">model peak \u2717</text><text x=\"191.8\" y=\"74\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">flies over</text><text x=\"191.8\" y=\"86\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">the summit</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">negative curvature: parabola opens downward</text></svg>",
    "drawingCaption": "In fog near a hilltop or saddle the parabola model opens downward: the autopilot flies to the model's peak, straight over the summit.",
    "coreTranslation": [
      "<strong>What:</strong> Newton's step is only guaranteed to go downhill when the Hessian is positive definite.",
      "<strong>How:</strong> $p=-H^{-1}g$ has slope $g^Tp=-g^TH^{-1}g$. If $H$ has a negative eigenvalue this number can be <em>positive</em> (the step goes uphill). If $H$ is singular there is no step at all. And near a saddle or a maximum Newton happily converges to it, because it only looks for $\\nabla f=0$.",
      "<strong>Why it matters:</strong> pure Newton needs safeguards: a line search (damped Newton) and a fix for the Hessian (add $\\tau I$), covered in the next two cards."
    ],
    "math": "$$\\nabla^2 f(x_k) \\not\\succ 0 \\implies p_k^T \\nabla f(x_k) \\not\\le 0 \\quad (\\text{Not Guaranteed to be a Descent Direction})$$",
    "personalConnection": "<strong>The airplane analogy.</strong> In fog near a hilltop or saddle the parabola model opens downward. The autopilot flies to the model's peak, straight over the summit, because pure Newton hunts any flat ground, not low ground.",
    "examTrap": "Pure Newton on f(x) = x\u00b3 \u2212 3x started at x\u2080 = \u22120.5 runs UPHILL: x goes \u22120.5 \u2192 \u22121.25 \u2192 \u22121.025 \u2192 \u22121 and f rises 1.375 \u2192 1.80 \u2192 2.00, converging to the local MAXIMUM at x = \u22121 (where f\u2033 = \u22126 < 0).",
    "hint": "What goes wrong when the radar sees the ground curving downward?",
    "breakdown": [
      "<strong>If $\\nabla^2f$ is not positive definite,</strong> the fitted parabola opens downward or is flat, and its 'bottom' is really a peak or a saddle.",
      "<strong>The Newton nose $p_k$ then need not satisfy $p_k^\\top\\nabla f\\lt0$:</strong> it can point uphill.",
      "<strong>Fix:</strong> check the curvature first and stabilise (Levenberg-Marquardt) or fall back to straight downhill when it is not all positive."
    ]
  },
  {
    "id": 604,
    "subject": "CMO",
    "topicId": "06_Newtons_Method_and_Hessian_Modifications",
    "topicTitle": "06 \u00b7 Newton\u2019s Method & Modifications",
    "cardNumber": "04",
    "category": "GLOBALIZATION",
    "highlighterClass": "highlight-emerald",
    "title": "Damped Newton with Backtracking Line Search",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-604\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"20\" y1=\"134\" x2=\"226\" y2=\"134\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-604)\"/><path d=\"M24.0,26.0 L29.1,35.4 L34.1,43.9 L39.1,51.6 L44.2,58.6 L49.2,64.9 L54.3,70.5 L59.4,75.7 L64.4,80.3 L69.5,84.5 L74.5,88.3 L79.5,91.7 L84.6,94.8 L89.7,97.6 L94.7,100.2 L99.8,102.5 L104.8,104.5 L109.8,106.4 L114.9,108.1 L120.0,109.6 L125.0,111.0 L130.1,112.2 L135.1,113.4 L140.2,114.4 L145.2,115.3 L150.2,116.2 L155.3,116.9 L160.3,117.6 L165.4,118.2 L170.4,118.8 L175.5,119.3 L180.6,119.7 L185.6,120.1 L190.7,120.5 L195.7,120.8 L200.8,121.1 L205.8,121.4 L210.8,121.7 L215.9,121.9 L220.9,122.1 L226.0,122.3\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.0\" stroke-dasharray=\"4 3\"/><circle cx=\"24.0\" cy=\"26.0\" r=\"2.6\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><line x1=\"26.0\" y1=\"32.0\" x2=\"44.0\" y2=\"58.9\" stroke=\"#000000\" stroke-width=\"1.8\" marker-end=\"url(#arr-604)\"/><circle cx=\"46.0\" cy=\"60.9\" r=\"2.6\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><line x1=\"48.0\" y1=\"66.9\" x2=\"72.0\" y2=\"85.9\" stroke=\"#000000\" stroke-width=\"1.8\" marker-end=\"url(#arr-604)\"/><circle cx=\"74.0\" cy=\"87.9\" r=\"2.6\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><line x1=\"76.0\" y1=\"93.9\" x2=\"108.0\" y2=\"104.5\" stroke=\"#000000\" stroke-width=\"1.8\" marker-end=\"url(#arr-604)\"/><circle cx=\"110.0\" cy=\"106.5\" r=\"2.6\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><line x1=\"112.0\" y1=\"112.5\" x2=\"148.0\" y2=\"114.1\" stroke=\"#000000\" stroke-width=\"1.8\" marker-end=\"url(#arr-604)\"/><circle cx=\"150.0\" cy=\"116.1\" r=\"2.6\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><line x1=\"152.0\" y1=\"122.1\" x2=\"194.0\" y2=\"118.9\" stroke=\"#000000\" stroke-width=\"1.8\" marker-end=\"url(#arr-604)\"/><circle cx=\"196.0\" cy=\"120.9\" r=\"2.6\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"54\" y=\"62\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u03b1&lt;1</text><text x=\"176\" y=\"110\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u03b1=1</text><g transform=\"translate(30.0 16.0) rotate(0) scale(0.55)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.18\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"120\" y=\"144\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">short cautious legs \u2192 full unit steps</text></svg>",
    "drawingCaption": "Far from the field fly short, cautious legs (backtracking, \u03b1<1); on the final approach fly the full unit step \u03b1=1.",
    "coreTranslation": [
      "<strong>What:</strong> damped Newton takes a shortened step $x_{k+1}=x_k+\\alpha_kp_k$, with $p_k$ the Newton direction and $\\alpha_k\\in(0,1]$ chosen by backtracking.",
      "<strong>How:</strong> start at $\\alpha=1$ and shrink ($\\alpha\\leftarrow\\tfrac12\\alpha$) until the Armijo test $f(x_k+\\alpha p_k)\\le f(x_k)+c_1\\alpha\\nabla f(x_k)^Tp_k$ holds.",
      "<strong>Why it matters:</strong> far from the solution the shrinking guarantees descent; near the solution the full step $\\alpha=1$ is always accepted (if $c_1<\\tfrac12$), so the method <em>automatically</em> switches back to fast quadratic convergence."
    ],
    "math": "$$x_{k+1} = x_k + \\alpha_k p_k, \\quad \\alpha_k = \\beta^m, \\quad \\text{with } c_1 \\in (0, 1/2) \\implies \\alpha_k = 1 \\text{ near } x^*$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Far from the field you shorten each leg after a backtracking check (small $\\alpha_k$); on the final approach you fly the full unit step $\\alpha=1$.",
    "examTrap": "Choosing $c_1 > 1/2$ destroys the quadratic convergence! If $c_1 > 1/2$, the unit step $\\alpha_k = 1$ will be rejected even when the quadratic model is exact, permanently capping your rate at linear.",
    "hint": "When does the pilot take the full unit step and when only a cautious one?",
    "breakdown": [
      "<strong>$\\alpha_k=\\beta^m$:</strong> start with the full step 1 and multiply by $\\beta$ until the Armijo altitude drop is achieved.",
      "<strong>$c_1\\lt\\tfrac12$</strong> is a modest demand for altitude loss, so near the optimum the full Newton step already satisfies it.",
      "<strong>Result:</strong> short careful legs far away and full Newton legs ($\\alpha=1$) near the valley, which keeps the fast local rate."
    ]
  },
  {
    "id": 605,
    "subject": "CMO",
    "topicId": "06_Newtons_Method_and_Hessian_Modifications",
    "topicTitle": "06 \u00b7 Newton\u2019s Method & Modifications",
    "cardNumber": "05",
    "category": "HESSIAN MODIFICATION",
    "highlighterClass": "highlight-violet",
    "title": "Levenberg-Marquardt & Spectral Shift (H + \u03c4I)",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-605\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><path d=\"M40.0,58.8 L44.0,56.0 L48.0,53.3 L52.0,50.8 L56.0,48.4 L60.0,46.2 L64.0,44.1 L68.0,42.2 L72.0,40.4 L76.0,38.7 L80.0,37.2 L84.0,35.8 L88.0,34.6 L92.0,33.5 L96.0,32.6 L100.0,31.8 L104.0,31.2 L108.0,30.6 L112.0,30.3 L116.0,30.1 L120.0,30.0 L124.0,30.1 L128.0,30.3 L132.0,30.6 L136.0,31.2 L140.0,31.8 L144.0,32.6 L148.0,33.5 L152.0,34.6 L156.0,35.8 L160.0,37.2 L164.0,38.7 L168.0,40.4 L172.0,42.2 L176.0,44.1 L180.0,46.2 L184.0,48.4 L188.0,50.8 L192.0,53.3 L196.0,56.0 L200.0,58.8\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.6\" stroke-dasharray=\"4 3\"/><path d=\"M40.0,40.0 L44.0,47.8 L48.0,55.2 L52.0,62.2 L56.0,68.8 L60.0,75.0 L64.0,80.8 L68.0,86.2 L72.0,91.2 L76.0,95.8 L80.0,100.0 L84.0,103.8 L88.0,107.2 L92.0,110.2 L96.0,112.8 L100.0,115.0 L104.0,116.8 L108.0,118.2 L112.0,119.2 L116.0,119.8 L120.0,120.0 L124.0,119.8 L128.0,119.2 L132.0,118.2 L136.0,116.8 L140.0,115.0 L144.0,112.8 L148.0,110.2 L152.0,107.2 L156.0,103.8 L160.0,100.0 L164.0,95.8 L168.0,91.2 L172.0,86.2 L176.0,80.8 L180.0,75.0 L184.0,68.8 L188.0,62.2 L192.0,55.2 L196.0,47.8 L200.0,40.0\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.6\"/><g transform=\"translate(120.0 92.0) rotate(0) scale(0.6)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.00\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"120\" y=\"12\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">H not positive definite: the model is a hill (dashed)</text><text x=\"120\" y=\"134\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">add \u03c4I: the model becomes a bowl</text><text x=\"120\" y=\"144\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u03c4\u21920 Newton \u00b7 \u03c4\u2192\u221e short gradient leg</text></svg>",
    "drawingCaption": "If the curvature gauge is not all positive the model is a hill (dashed). Adding the stabiliser \u03c4I stiffens it into a bowl (solid) the autopilot can safely fly to.",
    "coreTranslation": [
      "<strong>The Core Modification:</strong> When $\\nabla^2 f(x_k)$ is indefinite or ill-conditioned, replace it with $B_k = \\nabla^2 f(x_k) + \\tau_k I$, choosing scalar $\\tau_k \\ge 0$ large enough so that $B_k \\succ 0$.",
      "<strong>Eigenvalue Impact:</strong> If $H$ has eigendecomposition $H = Q \\Lambda Q^T$, then $H + \\tau I = Q (\\Lambda + \\tau I) Q^T$. All eigenvectors are preserved; every eigenvalue shifts by $+\\tau$.",
      "<strong>Interpolation Property:</strong> If $\\tau_k = 0$, you get pure Newton. As $\\tau_k \\to \\infty$, $p_k \\approx -\\frac{1}{\\tau_k} \\nabla f(x_k)$, smoothly recovering steepest descent!"
    ],
    "math": "$$(\\nabla^2 f(x_k) + \\tau_k I) p_k = -\\nabla f(x_k), \\quad \\tau_k \\ge \\max\\left(0, \\; -\\lambda_{\\min}(\\nabla^2 f(x_k)) + \\delta\\right) \\; (\\delta > 0)$$",
    "personalConnection": "<strong>The airplane analogy.</strong> If the curvature gauge is not all positive, add a stabiliser $\\tau I$ to stiffen the terrain model into a bowl. A large $\\tau$ behaves like a short gradient leg, $\\tau\\to0$ is pure Newton.",
    "examTrap": "Choosing $\\tau_k$ too large degrades the method to slow Gradient Descent with tiny steps! Set $\\tau_k$ dynamically: decrease $\\tau$ when function value decreases rapidly, increase $\\tau$ when progress stalls.",
    "hint": "How does the pilot make a hill-shaped terrain model safe to fly to?",
    "breakdown": [
      "<strong>$\\tau_kI$ adds stiffness along every axis,</strong> lifting all the curvatures by $\\tau_k$.",
      "<strong>$\\tau_k\\ge-\\lambda_{\\min}+\\delta$</strong> is just enough that even the most negative curvature becomes strictly positive.",
      "<strong>The dial:</strong> $\\tau\\to0$ is pure Newton (trust the curvature), $\\tau\\to\\infty$ is a tiny gradient step (trust only the slope)."
    ]
  },
  {
    "id": 606,
    "subject": "CMO",
    "topicId": "06_Newtons_Method_and_Hessian_Modifications",
    "topicTitle": "06 \u00b7 Newton\u2019s Method & Modifications",
    "cardNumber": "06",
    "category": "WORKED BENCHMARK",
    "highlighterClass": "highlight-indigo",
    "title": "Worked Benchmark: Rosenbrock Newton vs GD",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-606\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><path d=\"M28.0,22.1 L32.6,30.8 L37.2,39.0 L41.8,46.8 L46.4,54.1 L51.0,61.0 L55.6,67.5 L60.2,73.5 L64.8,79.0 L69.4,84.1 L74.0,88.8 L78.6,93.0 L83.2,96.8 L87.8,100.1 L92.4,103.0 L97.0,105.4 L101.6,107.4 L106.2,109.0 L110.8,110.1 L115.4,110.8 L120.0,111.0 L124.6,110.8 L129.2,110.1 L133.8,109.0 L138.4,107.4 L143.0,105.4 L147.6,103.0 L152.2,100.1 L156.8,96.8 L161.4,93.0 L166.0,88.8 L170.6,84.1 L175.2,79.0 L179.8,73.5 L184.4,67.5 L189.0,61.0 L193.6,54.1 L198.2,46.8 L202.8,39.0 L207.4,30.8 L212.0,22.1\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.6\"/><path d=\"M28.0,40.1 L32.6,48.8 L37.2,57.0 L41.8,64.8 L46.4,72.1 L51.0,79.0 L55.6,85.5 L60.2,91.5 L64.8,97.0 L69.4,102.1 L74.0,106.8 L78.6,111.0 L83.2,114.8 L87.8,118.1 L92.4,121.0 L97.0,123.4 L101.6,125.4 L106.2,127.0 L110.8,128.1 L115.4,128.8 L120.0,129.0 L124.6,128.8 L129.2,128.1 L133.8,127.0 L138.4,125.4 L143.0,123.4 L147.6,121.0 L152.2,118.1 L156.8,114.8 L161.4,111.0 L166.0,106.8 L170.6,102.1 L175.2,97.0 L179.8,91.5 L184.4,85.5 L189.0,79.0 L193.6,72.1 L198.2,64.8 L202.8,57.0 L207.4,48.8 L212.0,40.1\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.6\"/><path d=\"M28.0,31.1 L32.6,39.8 L37.2,48.0 L41.8,55.8 L46.4,63.1 L51.0,70.0 L55.6,76.5 L60.2,82.5 L64.8,88.0 L69.4,93.1 L74.0,97.8 L78.6,102.0 L83.2,105.8 L87.8,109.1 L92.4,112.0 L97.0,114.4 L101.6,116.4 L106.2,118.0 L110.8,119.1 L115.4,119.8 L120.0,120.0 L124.6,119.8 L129.2,119.1 L133.8,118.0 L138.4,116.4 L143.0,114.4 L147.6,112.0 L152.2,109.1 L156.8,105.8 L161.4,102.0 L166.0,97.8 L170.6,93.1 L175.2,88.0 L179.8,82.5 L184.4,76.5 L189.0,70.0 L193.6,63.1 L198.2,55.8 L202.8,48.0 L207.4,39.8 L212.0,31.1\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.0\" stroke-dasharray=\"3 3\"/><path d=\"M34.0,36.3 L40.0,58.8 L40.0,46.8 L46.0,68.5 L46.0,56.5 L52.0,77.4 L52.0,65.4 L58.0,85.6 L58.0,73.6 L64.0,93.1 L64.0,81.1 L70.0,99.8 L70.0,87.8 L76.0,105.7 L76.0,93.7 L82.0,110.8 L82.0,98.8 L88.0,115.2 L88.0,103.2 L94.0,118.9 L94.0,106.9 L100.0,121.8 L100.0,109.8 L106.0,123.9 L106.0,111.9 L112.0,125.3 L112.0,113.3 L118.0,126.0\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"2 2\"/><path d=\"M34.0,42.3 L84.0,106.4 L122.0,120.0\" fill=\"none\" stroke=\"#000000\" stroke-width=\"3\"/><circle cx=\"122.0\" cy=\"120.0\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><g transform=\"translate(40.0 28.3) rotate(20) scale(0.6)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.00\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"236\" y=\"50\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"end\" fill=\"#000000\">Newton: 2\u20133 legs</text><text x=\"236\" y=\"62\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"end\" fill=\"#000000\">(a bridge)</text><text x=\"236\" y=\"82\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"end\" fill=\"#000000\">gradient descent:</text><text x=\"236\" y=\"94\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"end\" fill=\"#000000\">many switchbacks</text><text x=\"120\" y=\"142\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Rosenbrock banana canyon</text></svg>",
    "drawingCaption": "Newton flies a bridge across the banana canyon in a few legs; gradient descent hikes down hundreds of switchbacks along the walls.",
    "coreTranslation": [
      "<strong>What:</strong> compare gradient descent (GD) and Newton on Rosenbrock $f=100(x_2-x_1^2)^2+(1-x_1)^2$, starting at the origin.",
      "<strong>GD:</strong> there $\\nabla^2f=\\mathrm{diag}(2,200)$, so $\\kappa=100$ and each step only shrinks the error by about $\\left(\\tfrac{99}{101}\\right)^2\\approx0.96$. It zig-zags across the valley and needs hundreds of steps.",
      "<strong>Newton:</strong> $\\nabla f(0,0)=(-2,0)$ and $H^{-1}=\\mathrm{diag}(\\tfrac12,\\tfrac1{200})$, so $p=-H^{-1}g=(1,0)$: one step to $(1,0)$. Dividing by the Hessian rescales the squeezed valley into a round bowl, and a few more steps land on $(1,1)$."
    ],
    "math": "$$\\nabla f(0,0)=\\begin{bmatrix}-2\\\\0\\end{bmatrix},\\ \\ H=\\begin{bmatrix}2&0\\\\0&200\\end{bmatrix}\\ \\Rightarrow\\ p_N=-H^{-1}g=\\begin{bmatrix}1\\\\0\\end{bmatrix},\\qquad \\kappa=100$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Newton flies a bridge straight across the banana-shaped canyon in a few legs, while gradient descent hikes down hundreds of switchbacks to the riverbed and back up the other wall.",
    "examTrap": "Far from the spine (e.g. $x = (-1.2, 1)$), Rosenbrock's Hessian has negative eigenvalues! You MUST use Hessian modification $\\tau I$ or Damped line search, otherwise Newton steps uphill and fails.",
    "hint": "Why does Newton cross the banana canyon in one leg while gradient descent switchbacks?",
    "breakdown": [
      "<strong>$H=\\operatorname{diag}(2,200)$:</strong> the curvature along $x_2$ is 100 times that along $x_1$ (steep walls, gentle floor), so $\\kappa=100$.",
      "<strong>$p_N=-H^{-1}g$ divides each slope component by its own curvature,</strong> giving the move $(1,0)$ straight down the floor.",
      "<strong>Gradient descent sees only the slope,</strong> so with $\\kappa=100$ it zig-zags between the walls."
    ]
  },
  {
    "id": 701,
    "subject": "CMO",
    "topicId": "07_Conjugate_Direction_and_Conjugate_Gradient_Methods",
    "topicTitle": "07 \u00b7 Conjugate Direction & CG Methods",
    "cardNumber": "01",
    "category": "CONJUGATE DIRECTIONS",
    "highlighterClass": "highlight-cyan",
    "title": "Conjugate Directions & Q-Orthogonality",
    "textbookImg": "assets/luenberger_fig9_1.png",
    "textbookRef": "Luenberger & Ye (4th ed), Sect. 9.1, Fig. 9.1 (p. 276)",
    "drawingCaption": "In a skewed valley perpendicular legs (dashed) undo each other; Q-conjugate headings (solid) follow the valley's natural axes and reach the bottom in two legs.",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-701\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><ellipse cx=\"150\" cy=\"74\" rx=\"16.390673951580528\" ry=\"26.520667552174842\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.2\" transform=\"rotate(-31.71747441146101 150 74)\"/><ellipse cx=\"150\" cy=\"74\" rx=\"28.389480054433214\" ry=\"45.93514365101015\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.2\" transform=\"rotate(-31.71747441146101 150 74)\"/><ellipse cx=\"150\" cy=\"74\" rx=\"44.88770927996497\" ry=\"72.62983929210739\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.2\" transform=\"rotate(-31.71747441146101 150 74)\"/><path d=\"M96.0,51.5 L140.6,48.6 L142.1,70.7 L148.6,70.3 L148.8,73.5\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.4\" stroke-dasharray=\"3 3\"/><path d=\"M96.0,51.5 L140.6,48.6 L150.0,74.0\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.8\"/><g transform=\"translate(90.0 37.5) rotate(0) scale(0.65)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.85\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><circle cx=\"140.6\" cy=\"48.6\" r=\"2.4\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"144.6\" y=\"42.6\" font-size=\"8\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">d\u2080 ends</text><text x=\"120\" y=\"16\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">perpendicular legs (dashed) zig-zag</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Q-conjugate legs (solid) follow the natural axes</text></svg>",
    "coreTranslation": [
      "<strong>Definition:</strong> Given a symmetric positive definite matrix $Q \\succ 0$, non-zero vectors $d_0, d_1, \\dots, d_{k-1}$ are <strong>$Q$-Conjugate (Q-Orthogonal)</strong> if $d_i^T Q d_j = 0$ for all $i \\ne j$.",
      "<strong>Linear Independence:</strong> Any set of mutually $Q$-conjugate directions is automatically <strong>linearly independent</strong>. If $d_0, \\dots, d_{n-1}$ are conjugate in $\\mathbb{R}^n$, they form a basis!",
      "<strong>Decoupling Quadratic Forms:</strong> Expanding $x - x^*$ in the conjugate basis completely diagonalizes $f(x) = \\frac{1}{2} x^T Q x - b^T x$. Minimizing over $\\mathbb{R}^n$ decouples into $n$ independent 1D minimizations."
    ],
    "math": "$$d_i^T Q d_j = 0 \\quad (\\forall i \\ne j), \\quad \\alpha_k = -\\frac{g_k^T d_k}{d_k^T Q d_k} = \\frac{r_k^T d_k}{d_k^T Q d_k} \\quad (r_k = b - Q x_k = -g_k)$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Headings that are $Q$-conjugate follow the valley's own natural axes: pushing down along one heading does not undo what you gained along another, unlike plain perpendicular headings in a skewed valley.",
    "examTrap": "Conjugacy depends strictly on matrix $Q$! Directions that are orthogonal in standard Euclidean geometry ($d_i^T d_j = 0$) are generally NOT $Q$-conjugate unless $Q = I$.",
    "hint": "Why are Q-conjugate headings better than perpendicular ones in a skewed valley?",
    "breakdown": [
      "<strong>$d_i^\\top Qd_j=0$ = a $Q$-twisted right angle.</strong> The valley's own curvature $Q$ decides what counts as 'not interfering', so moving along $d_j$ does not undo the altitude already won along $d_i$.",
      "<strong>$\\alpha_k=-g_k^\\top d_k/d_k^\\top Qd_k$:</strong> downward momentum over the brakes along that heading, exactly the bottom of that line.",
      "<strong>$r_k=-g_k$</strong> is the residual: the same radar reading with the sign flipped."
    ]
  },
  {
    "id": 702,
    "subject": "CMO",
    "topicId": "07_Conjugate_Direction_and_Conjugate_Gradient_Methods",
    "topicTitle": "07 \u00b7 Conjugate Direction & CG Methods",
    "cardNumber": "02",
    "category": "EXPANDING SUBSPACE",
    "highlighterClass": "highlight-amber",
    "title": "The Expanding Subspace Theorem",
    "textbookImg": "assets/luenberger_fig9_2.png",
    "textbookRef": "Luenberger & Ye (4th ed), Sect. 9.1, Fig. 9.2 (p. 277)",
    "drawingCaption": "After k legs you sit at the lowest point of the whole flight plane spanned by your headings, not just along the last line.",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-702\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><polygon points=\"20,128 220,128 232,20 32,20\" fill=\"#eef0f4\" stroke=\"#000000\" stroke-width=\"0.8\"/><ellipse cx=\"150\" cy=\"74\" rx=\"16.390673951580528\" ry=\"26.520667552174842\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.2\" transform=\"rotate(-31.71747441146101 150 74)\"/><ellipse cx=\"150\" cy=\"74\" rx=\"28.389480054433214\" ry=\"45.93514365101015\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.2\" transform=\"rotate(-31.71747441146101 150 74)\"/><ellipse cx=\"150\" cy=\"74\" rx=\"44.88770927996497\" ry=\"72.62983929210739\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.2\" transform=\"rotate(-31.71747441146101 150 74)\"/><line x1=\"56.0\" y1=\"69.5\" x2=\"200.6492537313433\" y2=\"22.61940298507463\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"5 3\"/><path d=\"M96.0,51.5 L140.6,48.6 L150.0,74.0\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.8\"/><g transform=\"translate(90.0 37.5) rotate(0) scale(0.65)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.85\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><circle cx=\"150.0\" cy=\"74.0\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"155.0\" y=\"86.0\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">x\u2082</text><text x=\"117.76499999999999\" y=\"136\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">lowest point of the whole flight plane span{d\u2080,d\u2081}</text><text x=\"40\" y=\"34\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">span{d\u2080,d\u2081}</text></svg>",
    "coreTranslation": [
      "<strong>The Fundamental Theorem:</strong> Let $\\{d_i\\}_{i=0}^{n-1}$ be $Q$-conjugate directions. For any starting point $x_0$, generate iterates via exact line search: $x_{k+1} = x_k + \\alpha_k d_k$.",
      "<strong>Subspace Optimality:</strong> At iteration $k$, the iterate $x_k$ minimizes the quadratic objective $f(x)$ globally over the entire affine subspace $x_0 + \\mathcal{B}_k$, where $\\mathcal{B}_k = \\operatorname{span}\\{d_0, d_1, \\dots, d_{k-1}\\}$!",
      "<strong>Gradient Orthogonality:</strong> Consequently, the gradient $g_k = \\nabla f(x_k)$ is strictly orthogonal to all previously traversed directions: $g_k^T d_i = 0$ for all $i < k$."
    ],
    "math": "$$x_k = \\arg\\min_{x \\in x_0 + \\mathcal{B}_k} f(x), \\quad g_k^T d_i = 0 \\quad (\\forall i = 0, 1, \\dots, k-1)$$",
    "personalConnection": "<strong>The airplane analogy.</strong> After $k$ legs you sit at the lowest point of the entire flight plane spanned by your $k$ headings, not only along the last line, and later conjugate legs never spoil the altitude already won.",
    "examTrap": "Distinguish between inner products: $g_k$ is orthogonal to $d_i$ under the standard Euclidean dot product ($g_k^T d_i = 0$), whereas the directions $d_i$ are orthogonal under the $Q$-weighted inner product ($d_i^T Q d_j = 0$).",
    "hint": "After k legs, where in the whole flight plane is the pilot sitting?",
    "breakdown": [
      "<strong>$x_k=\\arg\\min_{x_0+\\mathcal B_k}f$:</strong> you are at the lowest point of the entire flight plane spanned by all $k$ headings so far, not just along the last line.",
      "<strong>$g_k^\\top d_i=0$ for every earlier heading:</strong> the slope under you is perpendicular to all of them, so no earlier heading can improve the altitude any more.",
      "<strong>Why it matters:</strong> later conjugate legs never spoil what is already won."
    ]
  },
  {
    "id": 703,
    "subject": "CMO",
    "topicId": "07_Conjugate_Direction_and_Conjugate_Gradient_Methods",
    "topicTitle": "07 \u00b7 Conjugate Direction & CG Methods",
    "cardNumber": "03",
    "category": "CG ALGORITHM",
    "highlighterClass": "highlight-emerald",
    "title": "Conjugate Gradient Method (Fletcher-Reeves)",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-703\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"62.0\" y1=\"96.0\" x2=\"122.0\" y2=\"90.0\" stroke=\"#000000\" stroke-width=\"2\" stroke-dasharray=\"4 3\" marker-end=\"url(#arr-703)\"/><text x=\"124\" y=\"88\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">\u03b2 d\u2096</text><line x1=\"62.0\" y1=\"96.0\" x2=\"70.0\" y2=\"42.0\" stroke=\"#000000\" stroke-width=\"2\" stroke-dasharray=\"4 3\" marker-end=\"url(#arr-703)\"/><text x=\"64\" y=\"38\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u2212g\u2096\u208a\u2081</text><line x1=\"62.0\" y1=\"96.0\" x2=\"130.0\" y2=\"36.0\" stroke=\"#000000\" stroke-width=\"3\" marker-end=\"url(#arr-703)\"/><text x=\"132\" y=\"36\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"start\" fill=\"#000000\">d\u2096\u208a\u2081</text><line x1=\"122.0\" y1=\"90.0\" x2=\"130.0\" y2=\"36.0\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"2 2\"/><line x1=\"70.0\" y1=\"42.0\" x2=\"130.0\" y2=\"36.0\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"2 2\"/><g transform=\"translate(62.0 96.0) rotate(-40) scale(0.7)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.71\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"176\" y=\"108\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"end\" fill=\"#000000\">d\u2096\u208a\u2081 = \u2212g\u2096\u208a\u2081 + \u03b2\u2096 d\u2096</text><text x=\"236\" y=\"122\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"end\" fill=\"#000000\">\u03b2 = \u2016g\u2096\u208a\u2081\u2016\u00b2 / \u2016g\u2096\u2016\u00b2</text><text x=\"120\" y=\"20\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">fresh downhill + part of the last heading</text></svg>",
    "drawingCaption": "The new heading is fresh downhill (\u2212g) plus a fraction \u03b2 of the previous heading: you keep some momentum instead of restarting.",
    "coreTranslation": [
      "<strong>The Breakthrough:</strong> Pure Conjugate Directions requires pre-computing and storing $n$ directions. Conjugate Gradient generates directions <strong>on the fly</strong> using only current gradients!",
      "<strong>The Recurrence:</strong> Start with $d_0 = -g_0$. At each step, set $d_{k+1} = -g_{k+1} + \\beta_k d_k$, where $\\beta_k = \\frac{\\|g_{k+1}\\|^2}{\\|g_k\\|^2}$.",
      "<strong>Gram-Schmidt Magic:</strong> Although $d_{k+1}$ only explicitly references $d_k$, the expanding subspace theorem guarantees that $d_{k+1}$ is automatically $Q$-conjugate to ALL previous directions $d_0, d_1, \\dots, d_{k-1}$!"
    ],
    "math": "$$d_{k+1} = -g_{k+1} + \\beta_k d_k, \\quad \\beta_k = \\frac{g_{k+1}^T g_{k+1}}{g_k^T g_k} = \\frac{\\|r_{k+1}\\|^2}{\\|r_k\\|^2}, \\quad \\alpha_k = \\frac{\\|r_k\\|^2}{d_k^T Q d_k}$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Instead of recalculating the whole voyage, trim the previous heading: the new heading is fresh downhill plus a fraction $\\beta_k=\\|g_{k+1}\\|^2/\\|g_k\\|^2$ of the previous heading, like keeping some momentum from the last leg.",
    "examTrap": "Remember that residual $r_k = b - Q x_k = -g_k$. In literature, $\\beta_k$ is written interchangeably as $\\frac{g_{k+1}^T g_{k+1}}{g_k^T g_k}$ or $\\frac{r_{k+1}^T r_{k+1}}{r_k^T r_k}$. Both are identical because sign cancels in squared norm.",
    "hint": "Which fraction of the old heading does the pilot keep when choosing the next one?",
    "breakdown": [
      "<strong>$-g_{k+1}$ is the fresh downhill from the radar;</strong> $\\beta_kd_k$ is the memory of the previous flight (the GPS memory).",
      "<strong>$\\beta_k=\\|g_{k+1}\\|^2/\\|g_k\\|^2$:</strong> if the slope has shrunk a lot, you keep little of the old heading; if not, you keep more.",
      "<strong>$\\alpha_k=\\|r_k\\|^2/d_k^\\top Qd_k$:</strong> the leg length is still momentum over brakes, along the remembered heading."
    ]
  },
  {
    "id": 704,
    "subject": "CMO",
    "topicId": "07_Conjugate_Direction_and_Conjugate_Gradient_Methods",
    "topicTitle": "07 \u00b7 Conjugate Direction & CG Methods",
    "cardNumber": "04",
    "category": "KRYLOV SPACES",
    "highlighterClass": "highlight-violet",
    "title": "Finite Termination & Krylov Subspace",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-704\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"14\" y1=\"124\" x2=\"226\" y2=\"124\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-704)\"/><rect x=\"30\" y=\"54\" width=\"18\" height=\"70\" rx=\"0\" fill=\"#c9ced8\" stroke=\"#000000\" stroke-width=\"1.4\"/><rect x=\"52\" y=\"84\" width=\"18\" height=\"40\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"50\" y=\"136\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">after leg 0</text><rect x=\"100\" y=\"123\" width=\"18\" height=\"1\" rx=\"0\" fill=\"#c9ced8\" stroke=\"#000000\" stroke-width=\"1.4\"/><rect x=\"122\" y=\"84\" width=\"18\" height=\"40\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"120\" y=\"136\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">after leg 1</text><rect x=\"170\" y=\"123\" width=\"18\" height=\"1\" rx=\"0\" fill=\"#c9ced8\" stroke=\"#000000\" stroke-width=\"1.4\"/><rect x=\"192\" y=\"123\" width=\"18\" height=\"1\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"190\" y=\"136\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">after leg 2</text><text x=\"120\" y=\"18\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">each leg kills one more curvature axis</text><text x=\"120\" y=\"30\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">n axes \u2192 at most n legs</text><g transform=\"translate(204.0 62.0) rotate(0) scale(0.6)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.00\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g></svg>",
    "drawingCaption": "Each conjugate leg removes the error along one more natural axis (dark bar, light bar), so after n legs the error is zero: finite termination.",
    "coreTranslation": [
      "<strong>Krylov Connection:</strong> The subspace $\\mathcal{B}_k = \\operatorname{span}\\{d_0, \\dots, d_{k-1}\\}$ generated by CG is identical to the <strong>Krylov Subspace</strong>: $\\mathcal{K}_k(Q, r_0) = \\operatorname{span}\\{r_0, Q r_0, Q^2 r_0, \\dots, Q^{k-1} r_0\\}$.",
      "<strong>Finite $n$-Step Termination:</strong> Because $\\mathbb{R}^n$ has dimension $n$, after at most $n$ iterations $\\mathcal{B}_n = \\mathbb{R}^n$, meaning $x_n = x^*$ is the EXACT global minimizer in exact arithmetic!",
      "<strong>Distinct Eigenvalues Super-Convergence:</strong> If $Q$ has only $m < n$ distinct eigenvalues, CG terminates in at most $m$ iterations! E.g. in 10,000 dimensions with 5 clusters of eigenvalues, CG finishes in 5 steps."
    ],
    "math": "$$\\mathcal{B}_k = \\mathcal{K}_k(Q, r_0) = \\operatorname{span}\\{r_0, Q r_0, \\dots, Q^{k-1} r_0\\}, \\quad x_m = x^* \\; \\text{for } m = |\\sigma(Q)| \\le n$$",
    "personalConnection": "<strong>The airplane analogy.</strong> In $n$ dimensions a quadratic valley has only $n$ natural axes: each conjugate leg kills one more, so you land after at most $n$ legs (only $m$ if there are just $m$ distinct curvature values).",
    "examTrap": "In computer floating-point arithmetic with roundoff error, finite termination can fail! Directions lose $Q$-orthogonality over many steps, turning CG into an iterative method that requires restarts.",
    "hint": "How many legs does the pilot need, and what do the legs span?",
    "breakdown": [
      "<strong>$\\mathcal K_k=\\operatorname{span}\\{r_0,Qr_0,\\dots\\}$</strong> is the flight plane the radar and the curvature gauge can reach in $k$ legs.",
      "<strong>Each leg kills one more natural axis of the valley,</strong> so with $m$ distinct curvature values you land after at most $m\\le n$ legs.",
      "<strong>Why it matters:</strong> in exact arithmetic CG is a direct method, and an iterative one that is usually done long before $n$ legs."
    ]
  },
  {
    "id": 705,
    "subject": "CMO",
    "topicId": "07_Conjugate_Direction_and_Conjugate_Gradient_Methods",
    "topicTitle": "07 \u00b7 Conjugate Direction & CG Methods",
    "cardNumber": "05",
    "category": "NON-LINEAR CG",
    "highlighterClass": "highlight-indigo",
    "title": "Non-Linear CG & Polak-Ribi\u00e8re Restarts",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-705\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><circle cx=\"60.0\" cy=\"62.0\" r=\"30.0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.8\"/><line x1=\"60\" y1=\"62\" x2=\"76\" y2=\"40\" stroke=\"#000000\" stroke-width=\"3\"/><line x1=\"60.0\" y1=\"62.0\" x2=\"76.0\" y2=\"40.0\" stroke=\"#000000\" stroke-width=\"3\" marker-end=\"url(#arr-705)\"/><text x=\"60\" y=\"108\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">corrupted heading</text><text x=\"60\" y=\"120\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">(wrong direction)</text><circle cx=\"176.0\" cy=\"62.0\" r=\"30.0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.8\"/><line x1=\"176.0\" y1=\"62.0\" x2=\"176.0\" y2=\"34.0\" stroke=\"#000000\" stroke-width=\"3\" marker-end=\"url(#arr-705)\"/><text x=\"176\" y=\"108\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">restart: d = \u2212g</text><text x=\"176\" y=\"120\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">(straight downhill)</text><line x1=\"98.0\" y1=\"60.0\" x2=\"138.0\" y2=\"60.0\" stroke=\"#000000\" stroke-width=\"2.2\" marker-end=\"url(#arr-705)\"/><text x=\"118\" y=\"52\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">reset</text><g transform=\"translate(60.0 24.0) rotate(0) scale(0.55)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.18\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><g transform=\"translate(176.0 24.0) rotate(0) scale(0.55)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.18\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g></svg>",
    "drawingCaption": "After a magnetic deposit the compass heading is corrupted; restart resets the heading to straight downhill (\u2212g) like re-zeroing the compass.",
    "coreTranslation": [
      "<strong>Beyond Quadratics:</strong> For general non-linear functions $f(x)$, exact line search is replaced by line search satisfying the <strong>Strong Wolfe conditions</strong>.",
      "<strong>Fletcher-Reeves Jamming:</strong> In Fletcher-Reeves ($\\beta_k = \\|g_{k+1}\\|^2 / \\|g_k\\|^2$), if a poor step is taken, the search directions can become nearly orthogonal to the gradient, trapping the algorithm in tiny zigzagging steps.",
      "<strong>Polak-Ribi\u00e8re (PR) Immunity:</strong> Polak-Ribi\u00e8re sets $\\beta_k = \\frac{g_{k+1}^T (g_{k+1} - g_k)}{\\|g_k\\|^2}$. If consecutive gradients are nearly identical ($g_{k+1} \\approx g_k$), $\\beta_k \\to 0$, automatically resetting $d_{k+1} \\approx -g_{k+1}$!"
    ],
    "math": "$$\\beta_k^{PR} = \\frac{g_{k+1}^T (g_{k+1} - g_k)}{\\|g_k\\|^2}, \\quad \\beta_k^+ = \\max\\left(0, \\; \\beta_k^{PR}\\right) \\quad (\\text{Automatic Reset})$$",
    "personalConnection": "<strong>The airplane analogy.</strong> When the terrain is not a perfect quadratic, Polak-Ribi\u00e8re headings can go bad. Reset the heading to straight downhill (a restart), like re-zeroing a compass after passing a magnetic deposit.",
    "examTrap": "FR guarantees descent under strong Wolfe conditions ($c_2 < 1/2$), but PR can produce an ascent direction on non-convex functions unless modified as $\\beta_k = \\max(0, \\beta_k^{PR})$.",
    "hint": "What stops the pilot following a corrupted heading when the terrain is not a quadratic?",
    "breakdown": [
      "<strong>$\\beta^{PR}=g_{k+1}^\\top(g_{k+1}-g_k)/\\|g_k\\|^2$</strong> measures how much the radar reading actually changed, instead of only its size.",
      "<strong>$\\beta^+=\\max(0,\\beta^{PR})$:</strong> if the formula goes negative, the memory is thrown away and the pilot restarts with straight downhill.",
      "<strong>Why it matters:</strong> restarting protects the global convergence of non-linear CG."
    ]
  },
  {
    "id": 706,
    "subject": "CMO",
    "topicId": "07_Conjugate_Direction_and_Conjugate_Gradient_Methods",
    "topicTitle": "07 \u00b7 Conjugate Direction & CG Methods",
    "cardNumber": "06",
    "category": "WORKED BENCHMARK",
    "highlighterClass": "highlight-rose",
    "title": "Worked Benchmark: 2D CG in Exactly 2 Steps",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-706\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><ellipse cx=\"150\" cy=\"74\" rx=\"16.390673951580528\" ry=\"26.520667552174842\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.2\" transform=\"rotate(-31.71747441146101 150 74)\"/><ellipse cx=\"150\" cy=\"74\" rx=\"28.389480054433214\" ry=\"45.93514365101015\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.2\" transform=\"rotate(-31.71747441146101 150 74)\"/><ellipse cx=\"150\" cy=\"74\" rx=\"44.88770927996497\" ry=\"72.62983929210739\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.2\" transform=\"rotate(-31.71747441146101 150 74)\"/><path d=\"M96.0,51.5 L140.6,48.6 L150.0,74.0\" fill=\"none\" stroke=\"#000000\" stroke-width=\"3\"/><g transform=\"translate(90.0 37.5) rotate(0) scale(0.65)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.85\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><circle cx=\"96.0\" cy=\"51.5\" r=\"2.8\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"90.0\" y=\"63.5\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"end\" fill=\"#000000\">x\u2080</text><circle cx=\"140.6\" cy=\"48.6\" r=\"2.8\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"146.6\" y=\"42.6\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">x\u2081</text><circle cx=\"150.0\" cy=\"74.0\" r=\"3.2\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"156.0\" y=\"86.0\" font-size=\"9.5\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">x*</text><text x=\"120\" y=\"18\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">2D: exactly two legs</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">leg 1 kills the error along d\u2080; leg 2 kills the rest</text></svg>",
    "drawingCaption": "In 2D conjugate gradient lands on the optimum in exactly two legs: the first removes the error along d\u2080, the second removes the rest.",
    "coreTranslation": [
      "<strong>Problem:</strong> minimize $f=x_1^2+4x_2^2$ (so $Q=\\mathrm{diag}(2,8)$) from $x_0=(4,1)$. First step is steepest descent: $g_0=(8,8)$, $d_0=-g_0$.",
      "<strong>Step 1:</strong> $\\alpha_0=\\frac{g_0^Tg_0}{d_0^TQd_0}=\\frac{128}{640}=\\frac15$, so $x_1=(2.4,\\,-0.6)$ and $g_1=(4.8,-4.8)$. Check: $g_1^Td_0=-38.4+38.4=0$ \u2713.",
      "<strong>Step 2:</strong> $\\beta_0=\\frac{\\|g_1\\|^2}{\\|g_0\\|^2}=\\frac{46.08}{128}=0.36$, $d_1=-g_1+\\beta_0d_0=(-7.68,\\,1.92)$, $\\alpha_1=\\frac{46.08}{d_1^TQd_1}=\\frac{46.08}{147.456}=\\frac5{16}$, giving $x_2=(0,0)$ exactly."
    ],
    "math": "$$x_0=\\begin{bmatrix}4\\\\1\\end{bmatrix}\\xrightarrow{\\ \\alpha_0=1/5\\ }x_1=\\begin{bmatrix}2.4\\\\-0.6\\end{bmatrix}\\xrightarrow{\\ \\beta_0=0.36,\\ \\alpha_1=5/16\\ }x_2=\\begin{bmatrix}0\\\\0\\end{bmatrix}=x^*$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Two legs finish the job in 2D: the first removes the error along $d_0$, the second removes the rest along $d_1$, and the first leg is never spoiled by the second.",
    "examTrap": "Always check the two identities: g\u2081\u1d40d\u2080 = 0 (exact line search) and d\u2081\u1d40Qd\u2080 = 0 (conjugacy). Here d\u2080\u1d40Qd\u2081 = 2(\u22128)(\u22127.68) + 8(\u22128)(1.92) = 122.88 \u2212 122.88 = 0 \u2713.",
    "hint": "Why does the second leg finish the job in 2D?",
    "breakdown": [
      "<strong>Leg 1 ($\\alpha_0=1/5$):</strong> fly straight downhill from $x_0$ until the altitude stops falling, landing at $x_1$.",
      "<strong>$\\beta_0=0.36$ blends the memory in:</strong> the second heading is fresh downhill plus 36% of the first heading, which makes it $Q$-conjugate to it.",
      "<strong>Leg 2 ($\\alpha_1=5/16$):</strong> flying that heading removes the remaining error, so $x_2=x^*=(0,0)$ exactly: two legs for two dimensions."
    ]
  },
  {
    "id": 801,
    "subject": "CMO",
    "topicId": "08_Quasi_Newton_Methods_SR1_DFP_and_BFGS",
    "topicTitle": "08 \u00b7 Quasi-Newton Methods (BFGS)",
    "cardNumber": "01",
    "category": "THE SECANT EQUATION",
    "highlighterClass": "highlight-cyan",
    "title": "The Secant Equation & Approximate Hessians",
    "textbookImg": "assets/luenberger_fig10_1.png",
    "textbookRef": "Luenberger & Ye (4th ed), Sect. 10.1, Fig. 10.1 (p. 317)",
    "drawingCaption": "From the flight log: how far you flew (s) and how much the slope gauge changed (y) give the curvature along the path, B s = y.",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-801\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"20\" y1=\"126\" x2=\"226\" y2=\"126\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-801)\"/><line x1=\"30\" y1=\"22\" x2=\"30\" y2=\"130\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-801)\"/><line x1=\"34\" y1=\"110\" x2=\"220\" y2=\"40\" stroke=\"#000000\" stroke-width=\"2.2\"/><circle cx=\"80.0\" cy=\"91.0\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><circle cx=\"170.0\" cy=\"57.0\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><line x1=\"80.0\" y1=\"126.0\" x2=\"80.0\" y2=\"91.0\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"2 2\"/><line x1=\"170.0\" y1=\"126.0\" x2=\"170.0\" y2=\"57.0\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"2 2\"/><line x1=\"82.0\" y1=\"120.0\" x2=\"168.0\" y2=\"120.0\" stroke=\"#000000\" stroke-width=\"2\" marker-end=\"url(#arr-801)\"/><text x=\"125\" y=\"116\" font-size=\"9.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">s</text><line x1=\"80.0\" y1=\"91.0\" x2=\"170.0\" y2=\"91.0\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"2 2\"/><line x1=\"172.0\" y1=\"89.0\" x2=\"172.0\" y2=\"59.0\" stroke=\"#000000\" stroke-width=\"2\" marker-end=\"url(#arr-801)\"/><text x=\"184\" y=\"76\" font-size=\"9.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"start\" fill=\"#000000\">y</text><g transform=\"translate(80.0 78.0) rotate(0) scale(0.55)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.18\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"80\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">x\u2096</text><text x=\"170\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">x\u2096\u208a\u2081</text><text x=\"40\" y=\"18\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">slope gauge \u2207f</text><text x=\"120\" y=\"12\" font-size=\"9.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">B s = y</text></svg>",
    "coreTranslation": [
      "<strong>The Core Dilemma:</strong> Newton's method converges quadratically but requires $\\mathcal{O}(n^2)$ storage and $\\mathcal{O}(n^3)$ operations to compute and invert the true Hessian matrix $\\nabla^2 f(x)$.",
      "<strong>Quasi-Newton Idea:</strong> Build an approximation $B_{k+1} \\approx \\nabla^2 f$ (or inverse $H_{k+1} \\approx [\\nabla^2 f]^{-1}$) using ONLY gradient evaluations from successive steps!",
      "<strong>The Secant Condition:</strong> By Taylor expansion, $g_{k+1} - g_k \\approx \\nabla^2 f(x_{k+1}) (x_{k+1} - x_k)$. Defining displacement $s_k = x_{k+1} - x_k$ and gradient difference $y_k = g_{k+1} - g_k$, the approximation MUST satisfy: $B_{k+1} s_k = y_k$ (or $H_{k+1} y_k = s_k$)."
    ],
    "math": "$$B_{k+1} s_k = y_k \\quad \\text{or} \\quad H_{k+1} y_k = s_k \\quad (s_k = x_{k+1} - x_k, \\; y_k = g_{k+1} - g_k)$$",
    "personalConnection": "<strong>The airplane analogy.</strong> From the flight log: how far you flew ($s_k$) and how much the slope gauge changed ($y_k$) reveal the terrain's curvature along that path, so you learn it without surveying the whole valley.",
    "examTrap": "The secant equation has $n$ equations for $n(n+1)/2$ unknown symmetric matrix entries. It is underdetermined! The specific update formulas (SR1, DFP, BFGS) are derived by minimizing different matrix norms.",
    "hint": "What does the flight log reveal about the curvature, without surveying the whole valley?",
    "breakdown": [
      "<strong>$s_k$ = how far you flew; $y_k$ = how much the slope reading changed.</strong>",
      "<strong>$B_{k+1}s_k=y_k$:</strong> the curvature estimate must turn the displacement you made into the slope change you saw, which is exactly what the true Hessian does along a straight path.",
      "<strong>$H_{k+1}y_k=s_k$ is the inverse form:</strong> it maps the slope change back to the displacement."
    ]
  },
  {
    "id": 802,
    "subject": "CMO",
    "topicId": "08_Quasi_Newton_Methods_SR1_DFP_and_BFGS",
    "topicTitle": "08 \u00b7 Quasi-Newton Methods (BFGS)",
    "cardNumber": "02",
    "category": "SR1 UPDATE",
    "highlighterClass": "highlight-amber",
    "title": "Symmetric Rank-1 (SR1) Update",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-802\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"8\" y=\"50\" width=\"28\" height=\"36\" rx=\"3\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"22.0\" y=\"72\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">B\u2096</text><rect x=\"42\" y=\"50\" width=\"10\" height=\"36\" rx=\"3\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"47.0\" y=\"72\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">+</text><rect x=\"58\" y=\"50\" width=\"88\" height=\"36\" rx=\"3\" fill=\"#d9dee7\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"102.0\" y=\"72\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">(y\u2212Bs)(y\u2212Bs)\u1d40</text><rect x=\"152\" y=\"50\" width=\"10\" height=\"36\" rx=\"3\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"157.0\" y=\"72\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">/</text><rect x=\"168\" y=\"50\" width=\"58\" height=\"36\" rx=\"3\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"197.0\" y=\"72\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">(y\u2212Bs)\u1d40s</text><text x=\"120\" y=\"24\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">SR1: one set screw (rank-1)</text><text x=\"120\" y=\"112\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">fast and light</text><text x=\"120\" y=\"130\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">denominator \u2248 0 \u2192 the mechanism jams</text><g transform=\"translate(222.0 24.0) rotate(0) scale(0.5)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.40\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g></svg>",
    "drawingCaption": "A single rank-one correction to the curvature estimate: quick and light, but if the denominator is near zero the update jams.",
    "coreTranslation": [
      "<strong>Unique Rank-1 Form:</strong> If we seek a symmetric rank-1 update $B_{k+1} = B_k + c u u^T$ satisfying the secant equation, there is <strong>EXACTLY ONE</strong> unique mathematical solution: the SR1 update.",
      "<strong>Key Strength:</strong> Remarkably, on quadratics, SR1 generates true Hessian approximations even with ARBITRARY step sizes (no line search required)!",
      "<strong>Fatal Flaw:</strong> The denominator $(y_k - B_k s_k)^T s_k$ can vanish or become negative. SR1 does NOT guarantee positive definiteness ($B_{k+1} \\succ 0$), making it unstable for standard line search."
    ],
    "math": "$$B_{k+1} = B_k + \\frac{(y_k - B_k s_k)(y_k - B_k s_k)^T}{(y_k - B_k s_k)^T s_k}, \\quad H_{k+1} = H_k + \\frac{(s_k - H_k y_k)(s_k - H_k y_k)^T}{(s_k - H_k y_k)^T y_k}$$",
    "personalConnection": "<strong>The airplane analogy.</strong> A single rank-one correction to the curvature estimate: quick and light, but if the denominator is near zero the update can blow up and the estimate jams.",
    "examTrap": "Never use SR1 with line search without a skip check! Production SR1 codes skip the update whenever $|s_k^T (y_k - B_k s_k)| < r \\|s_k\\| \\|y_k - B_k s_k\\|$, and pair it with Trust Region frameworks.",
    "hint": "What is the cheapest possible correction that still satisfies the secant equation?",
    "breakdown": [
      "<strong>$y_k-B_ks_k$ = the error:</strong> what the old estimate failed to predict about the slope change.",
      "<strong>$vv^\\top/(v^\\top s)$ with $v=y_k-B_ks_k$</strong> adds a correction in exactly that direction, a rank-one update.",
      "<strong>The denominator $(y_k-B_ks_k)^\\top s_k$</strong> rescales it so the secant equation holds; if it is near 0 the update blows up."
    ]
  },
  {
    "id": 803,
    "subject": "CMO",
    "topicId": "08_Quasi_Newton_Methods_SR1_DFP_and_BFGS",
    "topicTitle": "08 \u00b7 Quasi-Newton Methods (BFGS)",
    "cardNumber": "03",
    "category": "DFP ALGORITHM",
    "highlighterClass": "highlight-violet",
    "title": "Davidon-Fletcher-Powell (DFP) Dual Update",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-803\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"8\" y=\"50\" width=\"26\" height=\"36\" rx=\"3\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"21.0\" y=\"72\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">H\u2096</text><rect x=\"40\" y=\"50\" width=\"12\" height=\"36\" rx=\"3\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"46.0\" y=\"72\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u2212</text><rect x=\"58\" y=\"50\" width=\"78\" height=\"36\" rx=\"3\" fill=\"#d9dee7\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"97.0\" y=\"72\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Hy y\u1d40H / y\u1d40Hy</text><rect x=\"142\" y=\"50\" width=\"12\" height=\"36\" rx=\"3\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"148.0\" y=\"72\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">+</text><rect x=\"160\" y=\"50\" width=\"62\" height=\"36\" rx=\"3\" fill=\"#d9dee7\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"191.0\" y=\"72\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">s s\u1d40 / y\u1d40s</text><text x=\"120\" y=\"24\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">DFP: two counterbalancing weights</text><text x=\"120\" y=\"112\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">one removes the old direction</text><text x=\"120\" y=\"130\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">one adds the new leg you flew</text><g transform=\"translate(222.0 24.0) rotate(0) scale(0.5)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.40\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g></svg>",
    "drawingCaption": "Two corrections to the curvature estimate: one balances out the old information along y, the other adds the leg you just flew.",
    "coreTranslation": [
      "<strong>First Rank-2 Solution:</strong> Developed by Davidon (1959) and refined by Fletcher and Powell (1963), DFP was the historical breakthrough that made Quasi-Newton practical.",
      "<strong>Rank-2 Structure:</strong> Uses two symmetric rank-1 corrections: one adds positive curvature along $s_k$, the other subtracts projected components along $H_k y_k$.",
      "<strong>Hereditary Property:</strong> If $H_k \\succ 0$ and the curvature condition $s_k^T y_k > 0$ holds, then $H_{k+1}$ is GUARANTEED to be positive definite ($H_{k+1} \\succ 0$)."
    ],
    "math": "$$H_{k+1}^{\\text{DFP}} = H_k + \\frac{s_k s_k^T}{s_k^T y_k} - \\frac{H_k y_k y_k^T H_k}{y_k^T H_k y_k}$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Two corrections to the curvature estimate: one matches the leg you just flew, the other cleans up so the estimate stays consistent.",
    "examTrap": "DFP is extremely sensitive to line search inaccuracies! If inexact line search is used, DFP's Hessian approximation tends to become ill-conditioned, which is why BFGS replaced it.",
    "hint": "Which two corrections does DFP apply to the inverse curvature estimate?",
    "breakdown": [
      "<strong>$+\\dfrac{s_ks_k^\\top}{s_k^\\top y_k}$ adds the leg you just flew,</strong> so the new estimate reproduces $H_{k+1}y_k=s_k$.",
      "<strong>$-\\dfrac{H_ky_ky_k^\\top H_k}{y_k^\\top H_ky_k}$ removes the old estimate's opinion</strong> along $H_ky_k$, which it would otherwise double-count.",
      "<strong>Both are rank one and symmetric,</strong> so the update stays symmetric."
    ]
  },
  {
    "id": 804,
    "subject": "CMO",
    "topicId": "08_Quasi_Newton_Methods_SR1_DFP_and_BFGS",
    "topicTitle": "08 \u00b7 Quasi-Newton Methods (BFGS)",
    "cardNumber": "04",
    "category": "BFGS MASTER FORMULA",
    "highlighterClass": "highlight-emerald",
    "title": "BFGS: The Gold Standard Quasi-Newton",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-804\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"8\" y=\"50\" width=\"28\" height=\"36\" rx=\"3\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"22.0\" y=\"72\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">B\u2096</text><rect x=\"42\" y=\"50\" width=\"12\" height=\"36\" rx=\"3\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"48.0\" y=\"72\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u2212</text><rect x=\"60\" y=\"50\" width=\"76\" height=\"36\" rx=\"3\" fill=\"#d9dee7\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"98.0\" y=\"72\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Bs s\u1d40B / s\u1d40Bs</text><rect x=\"142\" y=\"50\" width=\"12\" height=\"36\" rx=\"3\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"148.0\" y=\"72\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">+</text><rect x=\"160\" y=\"50\" width=\"62\" height=\"36\" rx=\"3\" fill=\"#d9dee7\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"191.0\" y=\"72\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">y y\u1d40 / y\u1d40s</text><text x=\"120\" y=\"24\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">BFGS: self-correcting gyro (rank-2)</text><text x=\"120\" y=\"112\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">stays positive definite</text><text x=\"120\" y=\"130\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">the gold standard</text><g transform=\"translate(222.0 24.0) rotate(0) scale(0.5)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.40\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g></svg>",
    "drawingCaption": "BFGS's rank-two update removes the old direction and adds the new one, keeping the curvature estimate positive definite: the standard choice.",
    "coreTranslation": [
      "<strong>The Gold Standard:</strong> Discovered independently by Broyden, Fletcher, Goldfarb, and Shanno (1970). It is universally recognized as the most robust unconstrained optimization algorithm.",
      "<strong>Dual Equivalence:</strong> BFGS is the exact mathematical <strong>dual</strong> of DFP obtained by swapping $B \\leftrightarrow H$ and $s \\leftrightarrow y$.",
      "<strong>Self-Correcting Robustness:</strong> Unlike DFP, BFGS possesses a self-correcting property: if an inaccurate step corrupts the Hessian estimate, subsequent iterations automatically damp out the error."
    ],
    "math": "$$H_{k+1} = \\left(I - \\rho_k s_k y_k^T\\right) H_k \\left(I - \\rho_k y_k s_k^T\\right) + \\rho_k s_k s_k^T, \\quad \\rho_k = \\frac{1}{y_k^T s_k}$$",
    "personalConnection": "<strong>The airplane analogy.</strong> BFGS is the autopilot that corrects its own gyro drift: each rank-two update keeps the curvature estimate positive definite and consistent with the flight log, so it is the standard choice.",
    "examTrap": "The direction is $p_k = -H_k g_k$, which requires ONLY matrix-vector multiplication ($\\mathcal{O}(n^2)$), NEVER matrix inversion ($\\mathcal{O}(n^3)$)! This gives Newton-like superlinear convergence at a fraction of the cost.",
    "hint": "Why is BFGS the preferred quasi-Newton update?",
    "breakdown": [
      "<strong>$\\rho_k=1/y_k^\\top s_k$ is one over the curvature measured along the last leg.</strong>",
      "<strong>$(I-\\rho sy^\\top)H(I-\\rho ys^\\top)$ filters the old estimate</strong> so it agrees with the new secant condition, and $+\\rho ss^\\top$ adds the new leg back.",
      "<strong>If $H_k\\succ0$ and $y_k^\\top s_k\\gt0$, then $H_{k+1}\\succ0$:</strong> every nose it produces points downhill."
    ]
  },
  {
    "id": 805,
    "subject": "CMO",
    "topicId": "08_Quasi_Newton_Methods_SR1_DFP_and_BFGS",
    "topicTitle": "08 \u00b7 Quasi-Newton Methods (BFGS)",
    "cardNumber": "05",
    "category": "CURVATURE CONDITION",
    "highlighterClass": "highlight-indigo",
    "title": "Hereditary Positive Definiteness & Wolfe",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-805\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"120\" y1=\"8\" x2=\"120\" y2=\"138\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"3 3\"/><path d=\"M18.0,55.3 L20.9,62.5 L23.7,69.2 L26.6,75.4 L29.5,81.1 L32.3,86.3 L35.2,90.9 L38.1,95.1 L40.9,98.7 L43.8,101.9 L46.7,104.5 L49.5,106.6 L52.4,108.2 L55.3,109.3 L58.1,109.9 L61.0,110.0 L63.9,109.5 L66.7,108.6 L69.6,107.1 L72.5,105.2 L75.3,102.7 L78.2,99.7 L81.1,96.2 L83.9,92.2 L86.8,87.7 L89.7,82.7 L92.5,77.2 L95.4,71.2 L98.3,64.6 L101.1,57.6 L104.0,50.0\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.4\"/><line x1=\"40.0\" y1=\"118.0\" x2=\"78.0\" y2=\"118.0\" stroke=\"#000000\" stroke-width=\"2\" marker-end=\"url(#arr-805)\"/><text x=\"60\" y=\"132\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">s</text><line x1=\"86.0\" y1=\"112.0\" x2=\"86.0\" y2=\"76.0\" stroke=\"#000000\" stroke-width=\"2\" marker-end=\"url(#arr-805)\"/><text x=\"96\" y=\"94\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"start\" fill=\"#000000\">y</text><text x=\"60\" y=\"18\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">ground curves up</text><text x=\"60\" y=\"30\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">s\u1d40y > 0 \u2713 trust it</text><path d=\"M138.0,107.4 L140.9,101.1 L143.7,95.3 L146.6,90.0 L149.5,85.0 L152.3,80.6 L155.2,76.5 L158.1,72.9 L160.9,69.8 L163.8,67.0 L166.7,64.8 L169.5,62.9 L172.4,61.6 L175.3,60.6 L178.1,60.1 L181.0,60.0 L183.9,60.4 L186.7,61.2 L189.6,62.5 L192.5,64.2 L195.3,66.3 L198.2,68.9 L201.1,71.9 L203.9,75.4 L206.8,79.3 L209.7,83.6 L212.5,88.4 L215.4,93.7 L218.3,99.3 L221.1,105.4 L224.0,112.0\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.4\" stroke-dasharray=\"5 3\"/><line x1=\"160.0\" y1=\"118.0\" x2=\"198.0\" y2=\"118.0\" stroke=\"#000000\" stroke-width=\"2\" marker-end=\"url(#arr-805)\"/><text x=\"180\" y=\"132\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">s</text><line x1=\"206.0\" y1=\"76.0\" x2=\"206.0\" y2=\"108.0\" stroke=\"#000000\" stroke-width=\"2\" marker-end=\"url(#arr-805)\"/><text x=\"214\" y=\"92\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"start\" fill=\"#000000\">y</text><text x=\"180\" y=\"18\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">ground sags</text><text x=\"180\" y=\"30\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">s\u1d40y \u2264 0 \u2717 refuse</text></svg>",
    "drawingCaption": "Trust a leg only if the terrain curved upward along it (s\u1d40y>0), which a Wolfe line search guarantees; if the ground sagged, refuse to log that leg.",
    "coreTranslation": [
      "<strong>The Positive Definite Guarantee:</strong> For both BFGS and DFP, $H_{k+1} \\succ 0$ if and only if $H_k \\succ 0$ and the <strong>Curvature Condition</strong> holds: $s_k^T y_k > 0$.",
      "<strong>Why Wolfe is Mandatory:</strong> On non-convex functions, a simple line search can produce $s_k^T y_k \\le 0$. But the <strong>Wolfe Curvature Condition</strong> $\\nabla f(x_k + \\alpha_k p_k)^T p_k \\ge c_2 \\nabla f(x_k)^T p_k$ mathematically FORCES $s_k^T y_k \\ge (1 - c_2) \\alpha_k |\\nabla f(x_k)^T p_k| > 0$!",
      "Therefore, pairing BFGS with Wolfe line search guarantees that every single search direction is a descent direction."
    ],
    "math": "$$s_k^T y_k > 0 \\iff H_{k+1} \\succ 0 \\quad \\left( \\text{Wolfe: } \\nabla f(x_k + \\alpha_k p_k)^T p_k \\ge c_2 \\nabla f(x_k)^T p_k \\implies s_k^T y_k > 0 \\right)$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Only trust a leg if the terrain curved upward along it ($s_k^\\top y_k\\gt0$), which a Wolfe line search guarantees. If the ground sagged, refuse to log that leg so the estimate stays safe.",
    "examTrap": "Standard Armijo condition alone does NOT guarantee $s_k^T y_k > 0$! You MUST enforce the second Wolfe condition (curvature condition), otherwise $H_{k+1}$ can lose positive definiteness.",
    "hint": "What must the slope reading do along a leg for the curvature log to stay trustworthy?",
    "breakdown": [
      "<strong>$s_k^\\top y_k\\gt0$:</strong> along the leg you flew, the slope reading rose, which means the terrain curved upward.",
      "<strong>This is equivalent to $H_{k+1}$ staying positive definite,</strong> so the nose stays a descent direction.",
      "<strong>The Wolfe curvature condition guarantees it,</strong> so a Wolfe line search makes BFGS safe."
    ]
  },
  {
    "id": 806,
    "subject": "CMO",
    "topicId": "08_Quasi_Newton_Methods_SR1_DFP_and_BFGS",
    "topicTitle": "08 \u00b7 Quasi-Newton Methods (BFGS)",
    "cardNumber": "06",
    "category": "LARGE-SCALE OPTIMIZATION",
    "highlighterClass": "highlight-rose",
    "title": "Limited-Memory BFGS (L-BFGS) Algorithm",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-806\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"12\" y=\"52\" width=\"32\" height=\"40\" rx=\"3\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.6\" stroke-dasharray=\"3 3\"/><text x=\"28\" y=\"70\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">s</text><text x=\"28\" y=\"84\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">y</text><rect x=\"50\" y=\"52\" width=\"32\" height=\"40\" rx=\"3\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.6\" stroke-dasharray=\"3 3\"/><text x=\"66\" y=\"70\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">s</text><text x=\"66\" y=\"84\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">y</text><rect x=\"88\" y=\"52\" width=\"32\" height=\"40\" rx=\"3\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"104\" y=\"70\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">s</text><text x=\"104\" y=\"84\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">y</text><rect x=\"126\" y=\"52\" width=\"32\" height=\"40\" rx=\"3\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"142\" y=\"70\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">s</text><text x=\"142\" y=\"84\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">y</text><rect x=\"164\" y=\"52\" width=\"32\" height=\"40\" rx=\"3\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"180\" y=\"70\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">s</text><text x=\"180\" y=\"84\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">y</text><rect x=\"202\" y=\"52\" width=\"32\" height=\"40\" rx=\"3\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"218\" y=\"70\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">s</text><text x=\"218\" y=\"84\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">y</text><text x=\"120\" y=\"24\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">L-BFGS: keep only the last m legs</text><text x=\"50\" y=\"108\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">old: forgotten</text><text x=\"160\" y=\"108\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">last m kept</text><g transform=\"translate(222.0 24.0) rotate(0) scale(0.5)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.40\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"120\" y=\"130\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">nearly the same guidance, a fraction of the memory</text></svg>",
    "drawingCaption": "Keep only the last m flight-log legs (s, y) instead of a full curvature map: nearly the same guidance for a fraction of the memory.",
    "coreTranslation": [
      "<strong>Large-Scale Bottleneck:</strong> When $n = 10^7$ (e.g. deep learning or PDE optimization), storing an $n \\times n$ dense matrix $H_k$ requires 800 Terabytes of RAM!",
      "<strong>The L-BFGS Solution:</strong> Store ONLY the last $m$ vector pairs $\\{s_i, y_i\\}_{i=k-m}^{k-1}$ (typically $m \\in [5, 20]$). Memory cost drops from $\\mathcal{O}(n^2)$ to just $\\mathcal{O}(m n)$.",
      "<strong>Two-Loop Recursion:</strong> Computes the search direction $p_k = -H_k g_k$ directly via an ingenious two-pass backward-forward loop requiring ZERO matrix multiplications, costing only $4mn$ floating-point ops!"
    ],
    "math": "$$\\text{Memory: } \\mathcal{O}(m n) \\ll \\mathcal{O}(n^2), \\quad H_0^k = \\gamma_k I, \\quad \\gamma_k = \\frac{s_{k-1}^T y_{k-1}}{\\|y_{k-1}\\|^2}$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Keep only the last $m$ legs of the flight log $(s,y)$ instead of a full curvature map: nearly the same guidance for a fraction of the memory.",
    "examTrap": "The initial base scaling $\\gamma_k = \\frac{s_{k-1}^T y_{k-1}}{\\|y_{k-1}\\|^2}$ is CRITICAL! It estimates the local spectral magnitude of the inverse Hessian so that the unit step $\\alpha_k = 1$ is accepted in line search.",
    "hint": "What does the pilot keep from the flight log, and what does he throw away?",
    "breakdown": [
      "<strong>Only the last $m$ pairs $(s,y)$:</strong> memory $O(mn)$ instead of the full $O(n^2)$ curvature map.",
      "<strong>$\\gamma_k=\\frac{s^\\top y}{y^\\top y}$ rescales the starting guess $H_0=\\gamma_kI$</strong> so it already matches the latest curvature.",
      "<strong>Old legs are forgotten:</strong> nearly the same guidance for a fraction of the memory."
    ]
  },
  {
    "id": 901,
    "subject": "CMO",
    "topicId": "09_Geometry_of_Constrained_Optimization_Tangent_Cone_and_LICQ",
    "topicTitle": "09 \u00b7 Tangent Cones & LICQ Geometry",
    "cardNumber": "01",
    "category": "OPTIMIZATION GEOMETRY",
    "highlighterClass": "highlight-amber",
    "title": "Feasible Set & Active Constraints",
    "textbookImg": "",
    "textbookRef": "",
    "drawingCaption": "A top-down view of an airplane parked against one mountain wall (g\u2081). The other walls are far across the valley. The open tarmac is \u03a9; the dashed circle is the local ball around x*.",
    "coreTranslation": [
      "The <strong>Feasible Set $\\Omega$</strong> is your legal playground where $h_i(x)=0$ and $g_j(x)\\le 0$ hold simultaneously.",
      "The <strong>Active Set $\\mathcal{A}(x)=\\{j: g_j(x)=0\\}$</strong> identifies boundary walls you are physically pressing against right now.",
      "<strong>Inactive constraints ($g_j(x)<0$):</strong> candidate $x^*$ touches $g_1(x)=0$, while $g_2(x)=0$ and $g_3(x)=0$ are far away! In a local ball around $x^*$, they remain strictly $<0$ and have zero local influence."
    ],
    "math": "$$\\Omega = \\{x : h_i(x)=0, \\, g_j(x) \\le 0\\}, \\quad \\mathcal{A}(x) = \\{j : g_j(x) = 0\\}$$",
    "personalConnection": "<strong>The airplane analogy.</strong> The Feasible Set (\u03a9) is the legal airspace and runway tarmac where you are permitted to fly and taxi. The Active Set names the mountain walls your plane is physically parked against right now. The mountains on the other side of the valley (inactive constraints) have zero effect on your immediate next move.  <br><br><em>Key for the whole Midterm 3 deck.</em> $\\Omega$ = legal airspace; $f$ = altitude (gravity is $-\\nabla f$); walls $g_j\\le0$ = mountain walls; wall push = multiplier $\\mu_j$; $T_\\Omega$ = legal headings; air-traffic control = the projection operator.",
    "examTrap": "Never include inactive constraints in local gradient calculations! $g_j(x^*) < 0$ implies $\\mu_j^* = 0$ by complementary slackness. Carrying inactive constraints into gradient equations produces false stationary points.",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-901\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><polygon points=\"54,36 190,24 214,92 150,126 70,122 40,80\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"2.4\"/><line x1=\"41.8\" y1=\"74.5\" x2=\"34.8\" y2=\"72.5\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"45.2\" y1=\"63.5\" x2=\"38.2\" y2=\"61.5\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"48.8\" y1=\"52.5\" x2=\"41.8\" y2=\"50.5\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"52.2\" y1=\"41.5\" x2=\"45.2\" y2=\"39.5\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"62.5\" y1=\"35.2\" x2=\"61.5\" y2=\"28.2\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"79.5\" y1=\"33.8\" x2=\"78.5\" y2=\"26.8\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"96.5\" y1=\"32.2\" x2=\"95.5\" y2=\"25.2\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"113.5\" y1=\"30.8\" x2=\"112.5\" y2=\"23.8\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"130.5\" y1=\"29.2\" x2=\"129.5\" y2=\"22.2\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"147.5\" y1=\"27.8\" x2=\"146.5\" y2=\"20.8\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"164.5\" y1=\"26.2\" x2=\"163.5\" y2=\"19.2\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"181.5\" y1=\"24.8\" x2=\"180.5\" y2=\"17.8\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"192.4\" y1=\"30.8\" x2=\"198.4\" y2=\"28.8\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"197.2\" y1=\"44.4\" x2=\"203.2\" y2=\"42.4\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"202.0\" y1=\"58.0\" x2=\"208.0\" y2=\"56.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"206.8\" y1=\"71.6\" x2=\"212.8\" y2=\"69.6\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"211.6\" y1=\"85.2\" x2=\"217.6\" y2=\"83.2\" stroke=\"#000000\" stroke-width=\"1.1\"/><text x=\"125\" y=\"82\" font-size=\"15\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u03a9</text><circle cx=\"47\" cy=\"58\" r=\"3.2\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"62\" y=\"62\" font-size=\"10\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">x*</text><circle cx=\"47\" cy=\"58\" r=\"14\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"3 2.5\"/><text x=\"4\" y=\"42\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"start\" fill=\"#000000\">g\u2081=0</text><text x=\"122\" y=\"14\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">g\u2082=0</text><text x=\"213\" y=\"44\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"start\" fill=\"#000000\">g\u2083=0</text><text x=\"120\" y=\"140\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">only g\u2081 is touching x*; g\u2082, g\u2083 are far away</text></svg>",
    "hint": "Which walls is the plane actually touching, and which can it ignore?",
    "breakdown": [
      "<strong>$h_i(x)=0$ and $g_j(x)\\le0$</strong> define the legal airspace $\\Omega$: equality walls you must stay on, inequality walls you must stay behind.",
      "<strong>$\\mathcal A(x)=\\{j:g_j(x)=0\\}$ = the walls you are pressed against right now.</strong>",
      "<strong>Walls with $g_j\\lt0$ are far away:</strong> in a small ball around $x$ they never matter."
    ]
  },
  {
    "id": 902,
    "subject": "CMO",
    "topicId": "09_Geometry_of_Constrained_Optimization_Tangent_Cone_and_LICQ",
    "topicTitle": "09 \u00b7 Tangent Cones & LICQ Geometry",
    "cardNumber": "02",
    "category": "LIMIT DEFINITIONS",
    "highlighterClass": "highlight-cyan",
    "title": "The Tangent Vector d & Tangent Plane",
    "textbookImg": "",
    "textbookRef": "",
    "drawingCaption": "A time-lapse dotted line tracking an airplane coming down onto the tarmac. At the touchdown point x* a single bold arrow d shoots forward along the tarmac: that is the velocity.",
    "coreTranslation": [
      "<strong>Curve definition (Luenberger, p. 323):</strong> a curve on the surface $S$ is parameterized as $x(t)\\in S$. Its derivative at $x^*$ is the velocity $\\dot x(t^*)$, and the tangent plane is the collection of all such derivatives!",
      "<strong>Discrete sequence version:</strong> $d=\\lim_{k\\to\\infty}\\dfrac{x_k-x^*}{t_k}$ with $x_k\\in\\Omega$ and $t_k\\downarrow 0$.",
      "<strong>Tangent plane:</strong> the plane $M=\\{y:\\nabla h(x^*)^\\top y=0\\}$ is strictly orthogonal to the normal gradient $\\nabla h(x^*)$."
    ],
    "math": "$$\\dot{x}(t^*) = \\lim_{t \\to t^*} \\frac{x(t) - x^*}{t - t^*}, \\quad M = \\{y : \\nabla h(x^*)^T y = 0\\}$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Think of $x_k$ as your GPS coordinates ticking down every millisecond ($t_k\\downarrow 0$) during your final descent through legal airspace. The tangent vector $d$ is your exact, instantaneous velocity at the precise moment your tires touch the tarmac at $x^*$. The crucial requirement: the whole approach path stayed inside legal airspace ($\\Omega$).",
    "examTrap": "Scalars $t_k$ MUST strictly approach 0 from the positive side ($t_k > 0$). Negative steps reverse direction and can launch you outside $\\Omega$.",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-902\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><path d=\"M30,115 Q120,30 210,115\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.2\"/><line x1=\"95\" y1=\"72.5\" x2=\"215\" y2=\"72.5\" stroke=\"#000000\" stroke-width=\"1.1\" stroke-dasharray=\"4 3\"/><line x1=\"120\" y1=\"72.5\" x2=\"120\" y2=\"28\" stroke=\"#000000\" stroke-width=\"1.8\" marker-end=\"url(#arr-902)\"/><text x=\"128\" y=\"34\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">\u2207h(x*)</text><line x1=\"66\" y1=\"88\" x2=\"120\" y2=\"72.5\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"2 2.5\"/><circle cx=\"66\" cy=\"88\" r=\"2.4\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"64\" y=\"101\" font-size=\"8.5\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">x\u2081</text><line x1=\"84\" y1=\"79\" x2=\"120\" y2=\"72.5\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"2 2.5\"/><circle cx=\"84\" cy=\"79\" r=\"2.4\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"82\" y=\"92\" font-size=\"8.5\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">x\u2082</text><line x1=\"102\" y1=\"74\" x2=\"120\" y2=\"72.5\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"2 2.5\"/><circle cx=\"102\" cy=\"74\" r=\"2.4\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"100\" y=\"87\" font-size=\"8.5\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">x\u2083</text><circle cx=\"120\" cy=\"72.5\" r=\"3.4\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"113\" y=\"86\" font-size=\"10\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">x*</text><line x1=\"120\" y1=\"72.5\" x2=\"182\" y2=\"72.5\" stroke=\"#000000\" stroke-width=\"3\" marker-end=\"url(#arr-902)\"/><text x=\"186\" y=\"66\" font-size=\"11\" font-family=\"serif\" font-style=\"italic\" font-weight=\"bold\" text-anchor=\"start\" fill=\"#000000\">d</text><text x=\"214\" y=\"80\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">M</text><text x=\"38\" y=\"128\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">t_k \u2193 0</text><text x=\"206\" y=\"128\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">h(x)=0</text><text x=\"120\" y=\"140\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">d = lim (x_k \u2212 x*) / t_k</text></svg>",
    "hint": "What is the plane's velocity at the instant of touchdown?",
    "breakdown": [
      "<strong>$\\dot x(t^*)$ is the limit of displacement over time.</strong> Dividing $x(t)-x^*$ by $t-t^*$ turns a small step into a velocity.",
      "<strong>$M=\\{y:\\nabla h(x^*)^\\top y=0\\}$ = the tangent plane:</strong> every velocity perpendicular to the wall normal, i.e. along the wall.",
      "<strong>Equality constraints allow only these sliding directions.</strong>"
    ]
  },
  {
    "id": 903,
    "subject": "CMO",
    "topicId": "09_Geometry_of_Constrained_Optimization_Tangent_Cone_and_LICQ",
    "topicTitle": "09 \u00b7 Tangent Cones & LICQ Geometry",
    "cardNumber": "03",
    "category": "CONE GEOMETRY",
    "highlighterClass": "highlight-emerald",
    "title": "The Tangent Cone T_\u03a9(x)",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-903\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><polygon points=\"45,72 85,40 110,50 140,26 160,40 200,24 215,70 190,110 150,96 120,128 85,104\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.8\"/><line x1=\"45\" y1=\"72\" x2=\"125\" y2=\"8\" stroke=\"#000000\" stroke-width=\"1.5\"/><line x1=\"45\" y1=\"72\" x2=\"125\" y2=\"22\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"3 3\"/><line x1=\"45\" y1=\"72\" x2=\"125\" y2=\"47\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"3 3\"/><line x1=\"45\" y1=\"72\" x2=\"125\" y2=\"72\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"3 3\"/><line x1=\"45\" y1=\"72\" x2=\"125\" y2=\"97\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"3 3\"/><line x1=\"45\" y1=\"72\" x2=\"125\" y2=\"122\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"3 3\"/><line x1=\"45\" y1=\"72\" x2=\"125\" y2=\"136\" stroke=\"#000000\" stroke-width=\"1.5\"/><line x1=\"45\" y1=\"72\" x2=\"112\" y2=\"72\" stroke=\"#000000\" stroke-width=\"2.8\" marker-end=\"url(#arr-903)\"/><text x=\"98\" y=\"66\" font-size=\"10\" font-family=\"serif\" font-style=\"italic\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">d</text><line x1=\"114\" y1=\"72\" x2=\"205\" y2=\"72\" stroke=\"#000000\" stroke-width=\"1.4\" stroke-dasharray=\"5 3\" marker-end=\"url(#arr-903)\"/><text x=\"166\" y=\"65\" font-size=\"10\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u03bbd</text><circle cx=\"45\" cy=\"72\" r=\"3.4\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"33\" y=\"90\" font-size=\"10\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">x*</text><text x=\"6\" y=\"133\" font-size=\"9.5\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">T_\u03a9(x*)</text></svg>",
    "drawingCaption": "Radiating out from the nose of the parked plane is a pie-shaped wedge (the cone), drawn with several dashed runway lines: the whole fan of safe departure headings.",
    "coreTranslation": [
      "The <strong>Tangent Cone $T_\\Omega(x)$</strong> is the set of all tangent vectors to $\\Omega$ at the point $x$.",
      "<strong>Cone property:</strong> if $d\\in T_\\Omega(x)$, then $\\lambda d\\in T_\\Omega(x)$ for all $\\lambda\\ge0$. You can stretch the arrow as long as you want.",
      "It is <strong>always a closed set</strong>, even if the underlying feasible set $\\Omega$ is non-convex or has sharp jagged edges."
    ],
    "math": "$$T_\\Omega(x) = \\left\\{ d \\in \\mathbb{R}^n : \\exists x_k \\in \\Omega, t_k \\downarrow 0 \\text{ s.t. } \\lim_{k\\to\\infty} \\frac{x_k - x}{t_k} = d \\right\\}$$",
    "personalConnection": "<strong>The airplane analogy.</strong> This is the complete catalog of every legal runway heading available to you from your parked position. Cone property: if a heading $d$ is safe, you can throttle forward along it as far as you want ($\\lambda d$) without immediately hitting the mountain.",
    "examTrap": "Tangent cones are NOT always convex! If $\\Omega$ is a non-convex set (e.g., union of two crossing lines), $T_\\Omega(x)$ is a union of lines, which fails convexity.",
    "textbookImg": "",
    "textbookRef": "",
    "hint": "Which headings can the plane really take off along from its parked position?",
    "breakdown": [
      "<strong>$x_k\\in\\Omega$, $t_k\\downarrow0$:</strong> a sequence of legal points closing in on $x$ from inside the airspace.",
      "<strong>$\\frac{x_k-x}{t_k}\\to d$:</strong> dividing by the shrinking step $t_k$ turns the tiny displacement into a heading $d$.",
      "<strong>The set of all such $d$ is a cone,</strong> not a subspace: you can scale a safe heading but not reverse it."
    ]
  },
  {
    "id": 905,
    "subject": "CMO",
    "topicId": "09_Geometry_of_Constrained_Optimization_Tangent_Cone_and_LICQ",
    "topicTitle": "09 \u00b7 Tangent Cones & LICQ Geometry",
    "cardNumber": "04",
    "category": "OPTIMALITY THEOREM",
    "highlighterClass": "highlight-violet",
    "title": "First-Order Optimality: \u2207f(x*)\u1d40d \u2265 0",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-905\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><circle cx=\"10\" cy=\"73\" r=\"55\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"3 3\"/><circle cx=\"10\" cy=\"73\" r=\"85\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"3 3\"/><circle cx=\"10\" cy=\"73\" r=\"120\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"3 3\"/><rect x=\"0\" y=\"0\" width=\"65\" height=\"145\" rx=\"0\" fill=\"#d1d5db\" stroke=\"#000000\" stroke-width=\"0\"/><line x1=\"65\" y1=\"0\" x2=\"65\" y2=\"145\" stroke=\"#000000\" stroke-width=\"2.6\"/><line x1=\"65.0\" y1=\"6.0\" x2=\"56.0\" y2=\"12.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"65.0\" y1=\"18.1\" x2=\"56.0\" y2=\"24.1\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"65.0\" y1=\"30.2\" x2=\"56.0\" y2=\"36.2\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"65.0\" y1=\"42.3\" x2=\"56.0\" y2=\"48.3\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"65.0\" y1=\"54.4\" x2=\"56.0\" y2=\"60.4\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"65.0\" y1=\"66.5\" x2=\"56.0\" y2=\"72.5\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"65.0\" y1=\"78.5\" x2=\"56.0\" y2=\"84.5\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"65.0\" y1=\"90.6\" x2=\"56.0\" y2=\"96.6\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"65.0\" y1=\"102.7\" x2=\"56.0\" y2=\"108.7\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"65.0\" y1=\"114.8\" x2=\"56.0\" y2=\"120.8\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"65.0\" y1=\"126.9\" x2=\"56.0\" y2=\"132.9\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"65.0\" y1=\"139.0\" x2=\"56.0\" y2=\"145.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><text x=\"30\" y=\"14\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">rock</text><line x1=\"65\" y1=\"73\" x2=\"140\" y2=\"73\" stroke=\"#000000\" stroke-width=\"3.2\" marker-end=\"url(#arr-905)\"/><text x=\"142\" y=\"67\" font-size=\"11\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">\u2207f</text><line x1=\"62\" y1=\"73\" x2=\"24\" y2=\"73\" stroke=\"#000000\" stroke-width=\"1.6\" stroke-dasharray=\"4 3\" marker-end=\"url(#arr-905)\"/><text x=\"44\" y=\"90\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u2212\u2207f</text><circle cx=\"65\" cy=\"73\" r=\"3.6\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"74\" y=\"90\" font-size=\"10\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">x*</text><line x1=\"65\" y1=\"73\" x2=\"105\" y2=\"42\" stroke=\"#000000\" stroke-width=\"1.3\" marker-end=\"url(#arr-905)\"/><line x1=\"65\" y1=\"73\" x2=\"110\" y2=\"104\" stroke=\"#000000\" stroke-width=\"1.3\" marker-end=\"url(#arr-905)\"/><line x1=\"65\" y1=\"73\" x2=\"65\" y2=\"30\" stroke=\"#000000\" stroke-width=\"1.3\" marker-end=\"url(#arr-905)\"/><line x1=\"65\" y1=\"73\" x2=\"65\" y2=\"116\" stroke=\"#000000\" stroke-width=\"1.3\" marker-end=\"url(#arr-905)\"/><text x=\"108\" y=\"38\" font-size=\"9.5\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">d</text><text x=\"168\" y=\"112\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u2207f\u00b7d \u2265 0</text><text x=\"168\" y=\"126\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">for every legal d</text></svg>",
    "drawingCaption": "The bold arrow (gravity, \u2212\u2207f is the dashed one) points straight into the rock. Every open runway d points away from the wall or along it. The plane is trapped at the lowest point.",
    "coreTranslation": [
      "<strong>What:</strong> if $x^*$ is a local minimizer over $\\Omega$, then $f$ cannot decrease to first order in any feasible direction: $\\nabla f(x^*)^Td\\ge0$ for every $d\\in T_\\Omega(x^*)$.",
      "<strong>How:</strong> moving a little along a feasible direction $d$ changes $f$ by about $\\nabla f(x^*)^Td$; if this were negative you would find a feasible point with smaller $f$.",
      "<strong>Why it matters:</strong> in cone language, $\\nabla f(x^*)$ lies in the dual cone $T_\\Omega(x^*)^*$ (equivalently $-\\nabla f(x^*)$ lies in the polar cone). This is the general first-order condition from which KKT is derived."
    ],
    "math": "$$x^* \\text{ local min of } f \\text{ on } \\Omega \\implies \\nabla f(x^*)^T d \\ge 0 \\quad \\forall \\, d \\in T_\\Omega(x^*)$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Your objective $f$ is altitude: you want to park at the lowest elevation possible, and the negative gradient $-\\nabla f$ (gravity) points exactly downhill. At the minimum, gravity must pull the plane straight into the solid mountain wall. $\\nabla f(x^*)^\\top d\\ge0$ is the pre-flight check proving that every legal runway $d$ goes flat or uphill. If one sloped downhill, you could just release the brakes!",
    "examTrap": "This is a NECESSARY condition only. It also holds at constrained saddle points and maxima. For a convex f over a convex \u03a9 it becomes sufficient.",
    "textbookImg": "",
    "textbookRef": "",
    "hint": "Why must every legal heading go flat or uphill at the lowest parking spot?",
    "breakdown": [
      "<strong>$\\nabla f(x^*)^\\top d$ = the altitude change per unit leg along $d$.</strong>",
      "<strong>It must be $\\ge0$ for every legal $d\\in T_\\Omega(x^*)$:</strong> if some legal heading went downhill, releasing the brakes would lower the altitude.",
      "<strong>$\\nabla f(x^*)$ is usually not zero here:</strong> the wall is what stops the plane, not flat ground."
    ]
  },
  {
    "id": 906,
    "subject": "CMO",
    "topicId": "09_Geometry_of_Constrained_Optimization_Tangent_Cone_and_LICQ",
    "topicTitle": "09 \u00b7 Tangent Cones & LICQ Geometry",
    "cardNumber": "05",
    "category": "EXAM TRAPS & CQ",
    "highlighterClass": "highlight-amber",
    "title": "Tangent Cone vs Linearized Cone (LICQ)",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-906\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"12\" y=\"62\" width=\"68\" height=\"54\" rx=\"0\" fill=\"#d1d5db\" stroke=\"#000000\" stroke-width=\"1.2\"/><line x1=\"80.0\" y1=\"65.4\" x2=\"74.0\" y2=\"70.4\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"80.0\" y1=\"72.1\" x2=\"74.0\" y2=\"77.1\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"80.0\" y1=\"78.9\" x2=\"74.0\" y2=\"83.9\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"80.0\" y1=\"85.6\" x2=\"74.0\" y2=\"90.6\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"80.0\" y1=\"92.4\" x2=\"74.0\" y2=\"97.4\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"80.0\" y1=\"99.1\" x2=\"74.0\" y2=\"104.1\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"80.0\" y1=\"105.9\" x2=\"74.0\" y2=\"110.9\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"80.0\" y1=\"112.6\" x2=\"74.0\" y2=\"117.6\" stroke=\"#000000\" stroke-width=\"1.1\"/><text x=\"46\" y=\"112\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">rock</text><polygon points=\"80,90.0 90,89.9 100,89.6 110,88.6 120,86.6 130,83.4 140,78.6 150,72.0 160,63.1 170,51.7 180,37.4 190,20.0 190,90\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.8\"/><line x1=\"14\" y1=\"90\" x2=\"218\" y2=\"90\" stroke=\"#000000\" stroke-width=\"1.1\" stroke-dasharray=\"5 3\" marker-end=\"url(#arr-906)\"/><line x1=\"80\" y1=\"90\" x2=\"214\" y2=\"90\" stroke=\"#000000\" stroke-width=\"3.2\" marker-end=\"url(#arr-906)\"/><circle cx=\"80\" cy=\"90\" r=\"3.4\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"85\" y=\"105\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">x*=0</text><text x=\"96\" y=\"16\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">g\u2081: x\u2082 \u2264 x\u2081\u00b3</text><text x=\"96\" y=\"28\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">g\u2082: \u2212x\u2082 \u2264 0</text><text x=\"150\" y=\"118\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"start\" fill=\"#000000\">T = just this ray \u2192</text><text x=\"57.120000000000005\" y=\"132\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">L = the whole x\u2081-axis, also \u2190 into the rock</text><text x=\"34\" y=\"84\" font-size=\"8.5\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">L says ok</text></svg>",
    "drawingCaption": "A thin horn of tarmac pinches to a point at x* (g\u2081: x\u2082 \u2264 x\u2081\u00b3, g\u2082: x\u2082 \u2265 0). The Nav Computer draws a straight safe line through the whole x\u2081-axis, including the stretch that runs into the rock.",
    "coreTranslation": [
      "The <strong>Linearized Cone $L_\\Omega(x)$</strong> is defined by the active constraint gradients: $L_\\Omega=\\{d:\\nabla h_i^\\top d=0,\\ \\nabla g_j^\\top d\\le0\\}$. In general $T_\\Omega\\subseteq L_\\Omega$.",
      "<strong>Constraint Qualification (CQ):</strong> a condition guaranteeing $T_\\Omega(x^*)=L_\\Omega(x^*)$. The gold standard is <strong>LICQ</strong>: the active gradients $\\{\\nabla h_i,\\nabla g_j\\}_{j\\in\\mathcal A}$ are linearly independent.",
      "Without CQ, $T_\\Omega\\subsetneq L_\\Omega$, and the KKT conditions can FAIL completely even at an obvious local minimum!"
    ],
    "math": "$$\\text{LICQ Holds} \\implies T_\\Omega(x^*) = L_\\Omega(x^*) = \\{d : \\nabla h_i^T d = 0, \\, \\nabla g_j^T d \\le 0 \\, (j \\in \\mathcal{A})\\}$$",
    "personalConnection": "<strong>The airplane analogy.</strong> $L_\\Omega$ is your Nav Computer's map: it guesses the safe airspace with perfectly straight lines based only on the slope where your wheels touch. LICQ is the safety check. If the wall curves sharply inwards (a cusp), the straight-line map over-approximates the safe zone, and if you follow the computer you smash into solid rock.",
    "examTrap": "Assuming KKT multipliers always exist! If $T_\\Omega \\ne L_\\Omega$ (CQ fails), a local minimum can exist where KKT multipliers DO NOT exist at all.",
    "textbookImg": "",
    "textbookRef": "",
    "hint": "When can the plane trust the straight-line map of the walls?",
    "breakdown": [
      "<strong>$L_\\Omega$ replaces each curved wall by its tangent line at $x^*$:</strong> the Nav Computer's straight-edged map.",
      "<strong>$T_\\Omega\\subseteq L_\\Omega$ always,</strong> but a cusp makes the map over-approximate.",
      "<strong>LICQ (independent wall normals) forces $T_\\Omega=L_\\Omega$,</strong> so the straight-line map is exact and KKT works."
    ]
  },
  {
    "id": 1001,
    "subject": "CMO",
    "topicId": "10_Separating_Hyperplanes_and_Farkas_Lemma",
    "topicTitle": "10 \u00b7 Separating Hyperplanes & Farkas\u2019 Lemma",
    "cardNumber": "01",
    "category": "SEPARATION THEOREMS",
    "highlighterClass": "highlight-cyan",
    "title": "Separating Hyperplane Theorem",
    "textbookImg": "assets/luenberger_fig11_7.png",
    "textbookRef": "Luenberger & Ye (4th ed), Sect. 11.7, Fig. 11.7 (p. 353)",
    "drawingCaption": "Two convex airspaces that do not overlap: one flat do-not-cross wall (a\u1d40x = b) has the restricted zone on one side and your corridor on the other.",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1001\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><ellipse cx=\"60\" cy=\"72\" rx=\"42\" ry=\"40\" fill=\"#d1d5db\" stroke=\"#000000\" stroke-width=\"1.8\" transform=\"rotate(0 60 72)\"/><text x=\"60\" y=\"76\" font-size=\"9.5\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">restricted</text><text x=\"60\" y=\"88\" font-size=\"9.5\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">zone C\u2081</text><polygon points=\"150,38 212,48 222,100 162,116 138,76\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.8\"/><g transform=\"translate(186.0 80.0) rotate(-20) scale(0.9)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.33\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"186\" y=\"36\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">your corridor C\u2082</text><line x1=\"112\" y1=\"14\" x2=\"100\" y2=\"132\" stroke=\"#000000\" stroke-width=\"2.4\" stroke-dasharray=\"6 3\"/><text x=\"110\" y=\"11\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">a\u1d40x = b</text><line x1=\"106.0\" y1=\"74.0\" x2=\"134.0\" y2=\"72.0\" stroke=\"#000000\" stroke-width=\"1.8\" marker-end=\"url(#arr-1001)\"/><text x=\"124\" y=\"66\" font-size=\"9.5\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">a</text></svg>",
    "coreTranslation": [
      "<strong>What:</strong> two convex sets $A$ and $B$ that do not overlap can always be split by a flat wall (hyperplane): there are $a\\ne0$ and $\\beta$ with $a^Tx\\le\\beta\\le a^Ty$ for all $x\\in A$, $y\\in B$.",
      "<strong>How:</strong> the wall $H=\\{z:a^Tz=\\beta\\}$ puts $A$ in the lower half-space and $B$ in the upper. If $A$ is closed and $B$ is compact, there is a gap and the separation can be strict: $a^Tx<\\beta<a^Ty$.",
      "<strong>Why it matters:</strong> this is the engine behind Farkas' lemma, the KKT conditions and duality: whenever a point is outside a convex set, there is a wall that proves it."
    ],
    "math": "$$A \\cap B = \\emptyset, \\; A, B \\text{ convex} \\implies \\exists a \\ne 0, \\beta : \\sup_{x \\in A} a^T x \\le \\inf_{y \\in B} a^T y$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Two rival airspaces (say a military zone and your civilian corridor) that do not overlap and are both convex. Air-traffic control can always draw one flat, infinite 'do-not-cross' wall that puts your corridor entirely on one side and the military zone entirely on the other.",
    "examTrap": "Strict separation strictly fails if neither set is compact! E.g. $A = \\{(x_1, x_2) : x_2 \\le 0\\}$ and $B = \\{(x_1, x_2) : x_1 x_2 \\ge 1, x_1 > 0\\}$ are closed and disjoint, but can only be weakly separated by $x_2 = 0$.",
    "hint": "What guarantees one flat wall can separate two airspaces?",
    "breakdown": [
      "<strong>$A\\cap B=\\emptyset$, both convex:</strong> the airspaces do not overlap and have no dents.",
      "<strong>$\\sup_Aa^\\top x\\le\\inf_Ba^\\top y$:</strong> in the direction $a$, every point of $A$ is behind every point of $B$.",
      "<strong>The wall is $a^\\top x=\\beta$ with $\\beta$ between those two numbers.</strong>"
    ]
  },
  {
    "id": 1002,
    "subject": "CMO",
    "topicId": "10_Separating_Hyperplanes_and_Farkas_Lemma",
    "topicTitle": "10 \u00b7 Separating Hyperplanes & Farkas\u2019 Lemma",
    "cardNumber": "02",
    "category": "BOUNDARY GEOMETRY",
    "highlighterClass": "highlight-amber",
    "title": "Supporting Hyperplane Theorem",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1002\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><ellipse cx=\"112\" cy=\"82\" rx=\"74\" ry=\"50\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"2\" transform=\"rotate(0 112 82)\"/><line x1=\"28\" y1=\"32\" x2=\"196\" y2=\"32\" stroke=\"#000000\" stroke-width=\"2.6\"/><line x1=\"28.0\" y1=\"32.0\" x2=\"196.0\" y2=\"32.0\" stroke=\"#000000\" stroke-width=\"0.1\"/><line x1=\"34.0\" y1=\"32.0\" x2=\"34.0\" y2=\"27.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"46.0\" y1=\"32.0\" x2=\"46.0\" y2=\"27.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"58.0\" y1=\"32.0\" x2=\"58.0\" y2=\"27.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"70.0\" y1=\"32.0\" x2=\"70.0\" y2=\"27.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"82.0\" y1=\"32.0\" x2=\"82.0\" y2=\"27.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"94.0\" y1=\"32.0\" x2=\"94.0\" y2=\"27.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"106.0\" y1=\"32.0\" x2=\"106.0\" y2=\"27.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"118.0\" y1=\"32.0\" x2=\"118.0\" y2=\"27.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"130.0\" y1=\"32.0\" x2=\"130.0\" y2=\"27.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"142.0\" y1=\"32.0\" x2=\"142.0\" y2=\"27.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"154.0\" y1=\"32.0\" x2=\"154.0\" y2=\"27.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"166.0\" y1=\"32.0\" x2=\"166.0\" y2=\"27.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"178.0\" y1=\"32.0\" x2=\"178.0\" y2=\"27.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"190.0\" y1=\"32.0\" x2=\"190.0\" y2=\"27.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><g transform=\"translate(112.0 42.0) rotate(0) scale(0.9)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.33\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><circle cx=\"112.0\" cy=\"32.0\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"118\" y=\"20\" font-size=\"9.5\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">x\u2080</text><line x1=\"112.0\" y1=\"32.0\" x2=\"112.0\" y2=\"8.0\" stroke=\"#000000\" stroke-width=\"1.8\" marker-end=\"url(#arr-1002)\"/><text x=\"122\" y=\"14\" font-size=\"9.5\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">a</text><text x=\"112\" y=\"142\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">whole airspace lies on one side: a\u1d40x \u2264 a\u1d40x\u2080</text></svg>",
    "drawingCaption": "A flat cliff face touches the airspace at exactly one parked spot x\u2080; the entire airspace stays on one side of it.",
    "coreTranslation": [
      "<strong>What:</strong> at every boundary point $x_0$ of a convex set $C$ you can lay a flat wall touching $C$ at $x_0$ with all of $C$ on one side: $a^T(x-x_0)\\le0$ for all $x\\in C$.",
      "<strong>How:</strong> the wall is $H=\\{x:a^Tx=a^Tx_0\\}$ and $a$ is a normal vector pointing away from $C$. At a smooth point $a$ is unique (the gradient direction); at a corner there are many valid $a$ (a whole cone of normals).",
      "<strong>Why it matters:</strong> a closed convex set is exactly the intersection of all its supporting half-spaces, and normal vectors are what become the multipliers in KKT."
    ],
    "math": "$$x_0 \\in \\partial C \\implies \\exists a \\ne 0 : a^T x \\le a^T x_0 \\quad \\forall x \\in C$$",
    "personalConnection": "<strong>The airplane analogy.</strong> The mountain wall you are parked against: a flat cliff face that touches your legal airspace at exactly your parking spot $x_0$, with the whole of the airspace lying on one side of it. That cliff face is the supporting hyperplane at the boundary point.",
    "examTrap": "At a corner the supporting hyperplane is NOT unique: there is a whole cone of valid normals (the normal cone). Uniqueness holds only at smooth boundary points.",
    "hint": "Why is there always a flat wall touching a convex airspace at its edge?",
    "breakdown": [
      "<strong>$x_0\\in\\partial C$:</strong> you are standing on the boundary.",
      "<strong>$a^\\top x\\le a^\\top x_0$ for all $x\\in C$:</strong> the whole airspace is on one side of the wall through $x_0$ with normal $a$.",
      "<strong>It follows from separating $x_0$ from the interior of $C$.</strong>"
    ]
  },
  {
    "id": 1003,
    "subject": "CMO",
    "topicId": "10_Separating_Hyperplanes_and_Farkas_Lemma",
    "topicTitle": "10 \u00b7 Separating Hyperplanes & Farkas\u2019 Lemma",
    "cardNumber": "03",
    "category": "FARKAS LEMMA",
    "highlighterClass": "highlight-emerald",
    "title": "Farkas\u2019 Lemma: Theorem of Alternatives",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1003\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"120\" y1=\"8\" x2=\"120\" y2=\"138\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"3 3\"/><path d=\"M18.0,116.0 L109.0,101.0 L57.0,35.0\" fill=\"#e5e7eb\" stroke=\"#000000\" stroke-width=\"1.2\"/><line x1=\"18.0\" y1=\"116.0\" x2=\"88.0\" y2=\"104.0\" stroke=\"#000000\" stroke-width=\"2.4\" marker-end=\"url(#arr-1003)\"/><line x1=\"18.0\" y1=\"116.0\" x2=\"48.0\" y2=\"54.0\" stroke=\"#000000\" stroke-width=\"2.4\" marker-end=\"url(#arr-1003)\"/><text x=\"92\" y=\"108\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">a\u2081</text><text x=\"42\" y=\"52\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"end\" fill=\"#000000\">a\u2082</text><g transform=\"translate(18.0 116.0) rotate(-20) scale(0.6)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.00\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><path d=\"M138.0,116.0 L229.0,101.0 L177.0,35.0\" fill=\"#e5e7eb\" stroke=\"#000000\" stroke-width=\"1.2\"/><line x1=\"138.0\" y1=\"116.0\" x2=\"208.0\" y2=\"104.0\" stroke=\"#000000\" stroke-width=\"2.4\" marker-end=\"url(#arr-1003)\"/><line x1=\"138.0\" y1=\"116.0\" x2=\"168.0\" y2=\"54.0\" stroke=\"#000000\" stroke-width=\"2.4\" marker-end=\"url(#arr-1003)\"/><text x=\"212\" y=\"108\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">a\u2081</text><text x=\"162\" y=\"52\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"end\" fill=\"#000000\">a\u2082</text><g transform=\"translate(138.0 116.0) rotate(-20) scale(0.6)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.00\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><line x1=\"18.0\" y1=\"116.0\" x2=\"66.0\" y2=\"84.0\" stroke=\"#000000\" stroke-width=\"2.8\" marker-end=\"url(#arr-1003)\"/><text x=\"70\" y=\"82\" font-size=\"10.5\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">b</text><text x=\"60\" y=\"134\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">b inside: walls hold \u2713</text><line x1=\"138.0\" y1=\"116.0\" x2=\"200.0\" y2=\"124.0\" stroke=\"#000000\" stroke-width=\"2.8\" marker-end=\"url(#arr-1003)\"/><text x=\"194\" y=\"138\" font-size=\"10.5\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"end\" fill=\"#000000\">b</text><line x1=\"128.0\" y1=\"118.0\" x2=\"232.0\" y2=\"116.0\" stroke=\"#000000\" stroke-width=\"1.4\" stroke-dasharray=\"5 3\"/><line x1=\"138.0\" y1=\"116.0\" x2=\"138.0\" y2=\"84.0\" stroke=\"#000000\" stroke-width=\"2.2\" marker-end=\"url(#arr-1003)\"/><text x=\"144\" y=\"88\" font-size=\"10\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">y</text><text x=\"180\" y=\"12\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">b outside: y proves it \u2717</text></svg>",
    "drawingCaption": "Left: gravity b sits inside the cone of wall pushes a\u2081, a\u2082, so the walls hold the plane. Right: b is outside; the heading y is allowed by every wall yet gravity drags you down it.",
    "coreTranslation": [
      "<strong>What:</strong> for a matrix $A$ and a vector $b$, <em>exactly one</em> of two statements is true: (1) $b$ is a non-negative combination of the columns of $A$ ($Ax=b,\\ x\\ge0$), or (2) some $y$ has $A^Ty\\ge0$ but $b^Ty<0$.",
      "<strong>How:</strong> the non-negative combinations of the columns form a closed convex cone $K$. If $b\\notin K$, the separating hyperplane theorem gives a wall $y$ with $K$ on its non-negative side and $b$ strictly on the other side.",
      "<strong>Why it matters:</strong> $y$ is a one-line <em>certificate</em> that $b$ is not in the cone. This is the tool that produces KKT multipliers and proves LP duality."
    ],
    "math": "$$\\exists x \\ge 0 : A x = b \\quad \\mathbf{XOR} \\quad \\exists y : A^T y \\ge 0, \\; b^T y < 0$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Gravity $b$ is pulling on your plane; the columns of $A$ are the normals of the mountain walls, and walls can only push (never pull). Either the wall pushes can add up exactly to cancel gravity ($Ax=b,\\ x\\ge0$) and the plane stays parked, or there is a heading $y$ that no wall blocks ($A^Ty\\ge0$) along which gravity still drags you downhill ($b^Ty<0$). Exactly one of the two stories is true.",
    "examTrap": "The two systems are mutually exclusive and exhaustive! They can NEVER both have a solution, and they can NEVER both fail. If you prove one holds, the other is automatically false.",
    "hint": "Either the walls can hold gravity or some heading proves they cannot. Which?",
    "breakdown": [
      "<strong>$Ax=b,\\ x\\ge0$:</strong> gravity $b$ is a non-negative combination of the wall normals (columns of $A$), so the walls can hold it.",
      "<strong>$A^\\top y\\ge0,\\ b^\\top y\\lt0$:</strong> a heading $y$ no wall blocks along which gravity still drags you down.",
      "<strong>Exactly one of the two holds:</strong> that heading is the certificate that the first story is impossible."
    ]
  },
  {
    "id": 1007,
    "subject": "CMO",
    "topicId": "10_Separating_Hyperplanes_and_Farkas_Lemma",
    "topicTitle": "10 \u00b7 Separating Hyperplanes & Farkas\u2019 Lemma",
    "cardNumber": "04",
    "category": "THEOREMS OF THE ALTERNATIVE",
    "highlighterClass": "highlight-emerald",
    "title": "Worked Example: Farkas with Real Numbers",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1007\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><path d=\"M40.0,112.0 L206.0,112.0 L144.0,8.0\" fill=\"#e5e7eb\" stroke=\"#000000\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"112.0\" x2=\"214.0\" y2=\"112.0\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"4 3\"/><line x1=\"40.0\" y1=\"112.0\" x2=\"150.0\" y2=\"2.0\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"4 3\"/><line x1=\"40.0\" y1=\"112.0\" x2=\"78.0\" y2=\"112.0\" stroke=\"#000000\" stroke-width=\"2.8\" marker-end=\"url(#arr-1007)\"/><text x=\"84\" y=\"124\" font-size=\"9.5\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">a\u2081</text><line x1=\"40.0\" y1=\"112.0\" x2=\"78.0\" y2=\"74.0\" stroke=\"#000000\" stroke-width=\"2.8\" marker-end=\"url(#arr-1007)\"/><text x=\"84\" y=\"60\" font-size=\"9.5\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">a\u2082</text><line x1=\"40.0\" y1=\"112.0\" x2=\"116.0\" y2=\"74.0\" stroke=\"#000000\" stroke-width=\"2.2\" marker-end=\"url(#arr-1007)\"/><circle cx=\"116.0\" cy=\"74.0\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"121\" y=\"68\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">b \u2713</text><line x1=\"40.0\" y1=\"112.0\" x2=\"40.0\" y2=\"74.0\" stroke=\"#000000\" stroke-width=\"2.2\" marker-end=\"url(#arr-1007)\"/><circle cx=\"40.0\" cy=\"74.0\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"45\" y=\"68\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">b\u2032 \u2717</text><line x1=\"40.0\" y1=\"112.0\" x2=\"64.0\" y2=\"138.0\" stroke=\"#000000\" stroke-width=\"2.2\" marker-end=\"url(#arr-1007)\"/><text x=\"66\" y=\"142\" font-size=\"9.5\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">y</text><g transform=\"translate(40.0 112.0) rotate(-30) scale(0.6)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.00\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g></svg>",
    "drawingCaption": "Cone of two wall pushes a\u2081=(1,0), a\u2082=(1,1). Gravity b=(2,1) sits inside; b\u2032=(0,1) sits outside, and y=(1,\u22121) is the heading that proves it.",
    "coreTranslation": [
      "<strong>Setup:</strong> columns $a_1=(1,0)$ and $a_2=(1,1)$, so $A=\\begin{pmatrix}1&1\\\\0&1\\end{pmatrix}$. Is $b=(2,1)$ a non-negative combination of them? Is $b'=(0,1)$?",
      "<strong>$b=(2,1)$:</strong> solve $x_1+x_2=2$, $x_2=1$, so $x=(1,1)\\ge0$ \u2713: system 1 holds (and so system 2 must fail). <strong>$b'=(0,1)$:</strong> $x_2=1$ and $x_1+x_2=0$ force $x_1=-1<0$, so system 1 has no solution.",
      "<strong>Certificate for $b'$:</strong> take $y=(1,-1)$. Then $A^Ty=(y\\cdot a_1,\\ y\\cdot a_2)=(1,\\ 0)\\ge0$ and $b'^Ty=-1<0$. This proves in one line that $b'$ is not in the cone: system 2 holds."
    ],
    "math": "$$A^Ty=\\begin{pmatrix}1\\\\0\\end{pmatrix}\\ge0,\\quad b'^Ty=-1<0\\ \\Rightarrow\\ b'\\notin\\operatorname{cone}(a_1,a_2)$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Farkas with numbers is a parking check. Write gravity $b'$ and the wall normals. If $b'$ lies inside the cone of wall pushes, the walls can hold the plane. If it sits outside, exhibit one heading $y$ that every wall allows but that gravity favours: that single $y$ is the certificate that the plane rolls away.",
    "examTrap": "To prove 'b is NOT a non-negative combination' do not try all x. Exhibit one y with A\u1d40y \u2265 0 and b\u1d40y < 0. Check both inequalities, including the sign of b\u1d40y.",
    "hint": "Which heading proves $b'=(0,1)$ cannot be held by the walls $a_1=(1,0),a_2=(1,1)$?",
    "breakdown": [
      "<strong>$A^\\top y=(1,0)\\ge0$ for $y=(1,-1)$:</strong> neither wall blocks that heading ($a_2\\cdot y=0$ is the edge of the cone).",
      "<strong>$b'^\\top y=-1\\lt0$:</strong> gravity $b'$ still pulls along it.",
      "<strong>So $b'$ is outside the cone,</strong> while $b=(2,1)=a_1+a_2$ sits inside it."
    ]
  },
  {
    "id": 1004,
    "subject": "CMO",
    "topicId": "10_Separating_Hyperplanes_and_Farkas_Lemma",
    "topicTitle": "10 \u00b7 Separating Hyperplanes & Farkas\u2019 Lemma",
    "cardNumber": "05",
    "category": "THEOREMS OF THE ALTERNATIVE",
    "highlighterClass": "highlight-violet",
    "title": "Gordan\u2019s Theorem of the Alternative",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1004\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"120\" y1=\"8\" x2=\"120\" y2=\"138\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"3 3\"/><line x1=\"14.0\" y1=\"110.0\" x2=\"100.0\" y2=\"120.0\" stroke=\"#000000\" stroke-width=\"2.4\"/><line x1=\"19.4\" y1=\"110.6\" x2=\"20.0\" y2=\"116.6\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"30.1\" y1=\"111.9\" x2=\"30.7\" y2=\"117.9\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"40.9\" y1=\"113.1\" x2=\"41.5\" y2=\"119.1\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"51.6\" y1=\"114.4\" x2=\"52.2\" y2=\"120.4\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"62.4\" y1=\"115.6\" x2=\"63.0\" y2=\"121.6\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"73.1\" y1=\"116.9\" x2=\"73.7\" y2=\"122.9\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"83.9\" y1=\"118.1\" x2=\"84.5\" y2=\"124.1\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"94.6\" y1=\"119.4\" x2=\"95.2\" y2=\"125.4\" stroke=\"#000000\" stroke-width=\"1.1\"/><g transform=\"translate(56.0 78.0) rotate(-30) scale(1)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.20\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><line x1=\"66.0\" y1=\"72.0\" x2=\"98.0\" y2=\"50.0\" stroke=\"#000000\" stroke-width=\"2.6\" marker-end=\"url(#arr-1004)\"/><text x=\"100\" y=\"46\" font-size=\"10\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">x</text><text x=\"60\" y=\"20\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">open sky: Ax &lt; 0</text><text x=\"60\" y=\"34\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">tilt away from all walls</text><polygon points=\"176,24 226,104 132,108\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.2\"/><line x1=\"201.0\" y1=\"64.0\" x2=\"187.2\" y2=\"72.2\" stroke=\"#000000\" stroke-width=\"2\" marker-end=\"url(#arr-1004)\"/><line x1=\"179.0\" y1=\"106.0\" x2=\"177.3\" y2=\"91.2\" stroke=\"#000000\" stroke-width=\"2\" marker-end=\"url(#arr-1004)\"/><line x1=\"154.0\" y1=\"66.0\" x2=\"166.1\" y2=\"73.2\" stroke=\"#000000\" stroke-width=\"2\" marker-end=\"url(#arr-1004)\"/><g transform=\"translate(176.0 80.0) rotate(0) scale(0.75)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.60\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"178\" y=\"126\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">boxed in: \u03a3 y\u1d62a\u1d62 = 0</text><text x=\"178\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">pushes cancel exactly</text></svg>",
    "drawingCaption": "Gordan: either a heading tilts you strictly away from every wall (open sky), or the wall pushes cancel with non-negative weights (boxed into a canyon).",
    "coreTranslation": [
      "<strong>What:</strong> for a matrix $A$ with rows $a_i^T$, exactly one holds: (1) some $x$ has $Ax<0$ (every $a_i^Tx$ is strictly negative), or (2) some $y\\ge0$, $y\\ne0$ has $A^Ty=0$.",
      "<strong>How:</strong> case (1) means all the vectors $a_i$ lie in an open half-plane (you can point $x$ away from all of them). Case (2) means the vectors $a_i$ surround the origin: $0$ is in their convex hull.",
      "<strong>Why it matters:</strong> Gordan is Farkas for strict inequalities. It is used to show 'no descent direction' implies $\\sum y_i\\nabla g_i=0$ (the Fritz-John conditions)."
    ],
    "math": "$$\\exists x : A x < 0 \\quad \\mathbf{XOR} \\quad \\exists y \\ge 0, \\; y \\ne 0 : A^T y = 0$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Either some heading takes you strictly away from every wall at once ($Ax<0$: open sky in all directions), or the wall pushes can balance each other out with non-negative weights ($A^Ty=0,\\ y\\ge0,\\ y\\ne0$): you are boxed into a canyon whose walls cancel exactly, with no escape heading.",
    "examTrap": "Notice the strict inequality $Ax < 0$! If the question asks for $Ax \\le 0$, you must use Farkas' Lemma or Ville's theorem, NOT Gordan's theorem.",
    "hint": "Either some heading frees the plane from every wall, or the pushes balance. Which?",
    "breakdown": [
      "<strong>$Ax\\lt0$:</strong> a heading that moves you strictly away from every wall at once: open sky.",
      "<strong>$A^\\top y=0,\\ y\\ge0,\\ y\\ne0$:</strong> the wall pushes cancel with non-negative weights: you are boxed in.",
      "<strong>Exactly one of the two holds;</strong> this is how interior points and degenerate boxes are told apart."
    ]
  },
  {
    "id": 1005,
    "subject": "CMO",
    "topicId": "10_Separating_Hyperplanes_and_Farkas_Lemma",
    "topicTitle": "10 \u00b7 Separating Hyperplanes & Farkas\u2019 Lemma",
    "cardNumber": "06",
    "category": "CONE POLARITY",
    "highlighterClass": "highlight-indigo",
    "title": "Dual Cones & Polar Cones (K* and K\u00b0)",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1005\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><path d=\"M118.0,76.0 L59.7,54.8 L56.9,65.2 L56.0,76.0 L56.9,86.8 L59.7,97.2 L64.3,107.0 L70.5,115.9 L78.1,123.5 L87.0,129.7 L96.8,134.3 L107.2,137.1 L118.0,138.0 L128.8,137.1\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\" stroke-dasharray=\"4 3\"/><path d=\"M118.0,76.0 L170.6,95.2 L173.3,84.9 L174.0,74.4 L172.7,63.9 L169.4,53.8 L164.3,44.6 L157.6,36.4 L149.4,29.7 L140.2,24.6 L130.1,21.3 L119.6,20.0 L109.1,20.7 L98.8,23.4\" fill=\"#eef0f4\" stroke=\"#000000\" stroke-width=\"1.4\" stroke-dasharray=\"5 3\"/><path d=\"M118.0,76.0 L163.3,68.0 L162.4,64.1 L161.2,60.3 L159.7,56.6 L157.8,53.0 L155.7,49.6 L153.2,46.4 L150.5,43.5 L147.6,40.8 L144.4,38.3 L141.0,36.2 L137.4,34.3 L133.7,32.8\" fill=\"#c9ced8\" stroke=\"#000000\" stroke-width=\"2\"/><g transform=\"translate(118.0 76.0) rotate(-40) scale(0.7)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.71\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"141.7\" y=\"56.1\" font-size=\"11\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">K</text><text x=\"183.4\" y=\"85.2\" font-size=\"10.5\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">K*</text><text x=\"89.8\" y=\"101.4\" font-size=\"10.5\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">K\u00b0</text><text x=\"120\" y=\"142\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">K legal headings \u00b7 K\u00b0 safe pulls</text></svg>",
    "drawingCaption": "The shaded wedge K is the set of legal headings. K* (dashed, wide) contains every force that never opposes a legal heading; its mirror image K\u00b0 contains every pull that makes every legal heading uphill.",
    "coreTranslation": [
      "<strong>Dual Cone $K^*$:</strong> For any cone $K \\subset \\mathbb{R}^n$, its dual cone is: $K^* = \\{y \\in \\mathbb{R}^n : y^T x \\ge 0, \\; \\forall x \\in K\\}$. It is always convex and closed, even if $K$ is neither!",
      "<strong>Polar Cone $K^\\circ$:</strong> Defined by negative inner products: $K^\\circ = \\{y \\in \\mathbb{R}^n : y^T x \\le 0, \\; \\forall x \\in K\\} = -K^*$.",
      "<strong>Bipolar Theorem:</strong> For any closed convex cone $K$, the double dual recovers the original cone: $(K^*)^* = K$ and $(K^\\circ)^\\circ = K$."
    ],
    "math": "$$K^* = \\{y : y^T x \\ge 0 \\, \\forall x \\in K\\}, \\quad (K^*)^* = K \\iff K \\text{ is closed and convex}$$",
    "personalConnection": "<strong>The airplane analogy.</strong> The legal headings from your parking spot form a cone $K$. The polar cone $K^\\circ$ is the set of 'gravity pulls' that make every legal heading go uphill or flat: pulls that can never make the plane roll anywhere legal. At a minimum, $-\\nabla f$ must lie in $K^\\circ$.",
    "examTrap": "Self-dual cones: The non-negative orthant $\\mathbb{R}_+^n$ and the cone of positive semidefinite matrices $\\mathbb{S}_+^n$ are strictly <strong>self-dual</strong> ($K^* = K$).",
    "hint": "Which pulls can never make a legal heading go downhill?",
    "breakdown": [
      "<strong>$K^*=\\{y:y^\\top x\\ge0\\ \\forall x\\in K\\}$:</strong> forces that never oppose any legal heading.",
      "<strong>The polar cone $K^\\circ=-K^*$</strong> is the set of pulls that make every legal heading go flat or uphill: at a minimum, $-\\nabla f\\in K^\\circ$.",
      "<strong>$(K^*)^*=K$ for closed convex $K$:</strong> taking the dual twice gets the original cone back."
    ]
  },
  {
    "id": 1006,
    "subject": "CMO",
    "topicId": "10_Separating_Hyperplanes_and_Farkas_Lemma",
    "topicTitle": "10 \u00b7 Separating Hyperplanes & Farkas\u2019 Lemma",
    "cardNumber": "07",
    "category": "WORKED BENCHMARK",
    "highlighterClass": "highlight-rose",
    "title": "Worked Benchmark: Proving KKT via Farkas",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1006\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"110.0\" y1=\"14.0\" x2=\"110.0\" y2=\"108.0\" stroke=\"#000000\" stroke-width=\"2.4\"/><line x1=\"110.0\" y1=\"19.2\" x2=\"104.0\" y2=\"19.2\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"110.0\" y1=\"29.7\" x2=\"104.0\" y2=\"29.7\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"110.0\" y1=\"40.1\" x2=\"104.0\" y2=\"40.1\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"110.0\" y1=\"50.6\" x2=\"104.0\" y2=\"50.6\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"110.0\" y1=\"61.0\" x2=\"104.0\" y2=\"61.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"110.0\" y1=\"71.4\" x2=\"104.0\" y2=\"71.4\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"110.0\" y1=\"81.9\" x2=\"104.0\" y2=\"81.9\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"110.0\" y1=\"92.3\" x2=\"104.0\" y2=\"92.3\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"110.0\" y1=\"102.8\" x2=\"104.0\" y2=\"102.8\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"110.0\" y1=\"108.0\" x2=\"228.0\" y2=\"108.0\" stroke=\"#000000\" stroke-width=\"2.4\"/><line x1=\"115.9\" y1=\"108.0\" x2=\"115.9\" y2=\"114.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"127.7\" y1=\"108.0\" x2=\"127.7\" y2=\"114.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"139.5\" y1=\"108.0\" x2=\"139.5\" y2=\"114.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"151.3\" y1=\"108.0\" x2=\"151.3\" y2=\"114.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"163.1\" y1=\"108.0\" x2=\"163.1\" y2=\"114.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"174.9\" y1=\"108.0\" x2=\"174.9\" y2=\"114.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"186.7\" y1=\"108.0\" x2=\"186.7\" y2=\"114.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"198.5\" y1=\"108.0\" x2=\"198.5\" y2=\"114.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"210.3\" y1=\"108.0\" x2=\"210.3\" y2=\"114.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"222.1\" y1=\"108.0\" x2=\"222.1\" y2=\"114.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><rect x=\"0\" y=\"0\" width=\"0\" height=\"0\" rx=\"0\" fill=\"none\" stroke=\"#000000\" stroke-width=\"0\"/><g transform=\"translate(124.0 94.0) rotate(-45) scale(0.8)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.50\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><circle cx=\"110.0\" cy=\"108.0\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><line x1=\"110.0\" y1=\"108.0\" x2=\"76.0\" y2=\"136.0\" stroke=\"#000000\" stroke-width=\"2.2\" stroke-dasharray=\"4 3\" marker-end=\"url(#arr-1006)\"/><text x=\"106\" y=\"142\" font-size=\"9.5\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"end\" fill=\"#000000\">\u2212\u2207f</text><line x1=\"114.0\" y1=\"64.0\" x2=\"150.0\" y2=\"64.0\" stroke=\"#000000\" stroke-width=\"2.6\" marker-end=\"url(#arr-1006)\"/><text x=\"152\" y=\"68\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">push\u2081</text><line x1=\"162.0\" y1=\"104.0\" x2=\"162.0\" y2=\"68.0\" stroke=\"#000000\" stroke-width=\"2.6\" marker-end=\"url(#arr-1006)\"/><text x=\"166\" y=\"84\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">push\u2082</text><text x=\"176\" y=\"134\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u2212\u2207f = \u03bc\u2081\u2207g\u2081 + \u03bc\u2082\u2207g\u2082</text><text x=\"176\" y=\"144\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u03bc \u2265 0</text></svg>",
    "drawingCaption": "Parked in a mountain corner: gravity pulls into both walls and each wall pushes back with a non-negative weight, so the net force is zero.",
    "coreTranslation": [
      "<strong>Problem:</strong> Prove why Karush-Kuhn-Tucker multipliers $\\mu_j \\ge 0$ must exist at a constrained local minimum $x^*$.",
      "<strong>Step 1 (No Descent):</strong> At a local minimum, there can be NO feasible descent direction: $\\nexists d$ such that $\\nabla f(x^*)^T d < 0$ and $\\nabla g_j(x^*)^T d \\le 0$ for all $j \\in \\mathcal{A}(x^*)$.",
      "<strong>Step 2 (Apply Farkas / Gordan):</strong> The failure of this inequality system implies by Farkas' Lemma that the dual system MUST have a solution: $-\\nabla f(x^*) = \\sum_{j \\in \\mathcal{A}} \\mu_j \\nabla g_j(x^*)$ with $\\mu_j \\ge 0$. This is the KKT condition!"
    ],
    "math": "$$-\\nabla f(x^*) = \\sum_{j \\in \\mathcal{A}(x^*)} \\mu_j^* \\nabla g_j(x^*), \\quad \\mu_j^* \\ge 0 \\quad (\\text{Farkas Dual of } \\nexists d : \\nabla f^T d < 0, \\nabla g_j^T d \\le 0)$$",
    "personalConnection": "<strong>The airplane analogy.</strong> You are wedged in a mountain corner touching two walls. Gravity $-\\nabla f$ pulls you into the corner, the two walls push back with forces $\\mu_1\\nabla g_1$ and $\\mu_2\\nabla g_2$, and Farkas guarantees the pushes can be chosen non-negative so that the net force is zero: that is the KKT equation.",
    "examTrap": "Farkas' lemma applies to LINEARIZED directions $\\nabla g_j^T d \\le 0$. For this to match physical feasible curves in $\\Omega$, a Constraint Qualification (like LICQ) is strictly required!",
    "hint": "Why must the wall pushes balance gravity at a constrained minimum?",
    "breakdown": [
      "<strong>No legal heading is downhill:</strong> there is no $d$ with $\\nabla f^\\top d\\lt0$ and $\\nabla g_j^\\top d\\le0$.",
      "<strong>Farkas turns that 'no heading' statement</strong> into $-\\nabla f=\\sum\\mu_j\\nabla g_j$ with $\\mu_j\\ge0$.",
      "<strong>Reading it back:</strong> gravity is exactly cancelled by non-negative pushes from the walls you touch."
    ]
  },
  {
    "id": 1101,
    "subject": "CMO",
    "topicId": "11_Karush_Kuhn_Tucker_Conditions_FONC_and_Sufficiency",
    "topicTitle": "11 \u00b7 KKT Conditions & Sufficiency",
    "cardNumber": "01",
    "category": "CONSTRAINED OPTIMALITY",
    "highlighterClass": "highlight-cyan",
    "title": "The Four Karush-Kuhn-Tucker (KKT) Conditions",
    "textbookImg": "assets/luenberger_fig11_8.png",
    "textbookRef": "Luenberger & Ye (4th ed), Sect. 11.8, Fig. 11.8 (p. 356)",
    "drawingCaption": "The four KKT checks as a pre-flight list: forces cancel, you are inside, walls only push, and a wall you are not touching pushes zero.",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1101\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"10\" y=\"10\" width=\"48\" height=\"118\" rx=\"0\" fill=\"#d1d5db\" stroke=\"#000000\" stroke-width=\"0\"/><line x1=\"58.0\" y1=\"10.0\" x2=\"58.0\" y2=\"128.0\" stroke=\"#000000\" stroke-width=\"2.4\"/><line x1=\"58.0\" y1=\"14.9\" x2=\"51.0\" y2=\"14.9\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"58.0\" y1=\"24.8\" x2=\"51.0\" y2=\"24.8\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"58.0\" y1=\"34.6\" x2=\"51.0\" y2=\"34.6\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"58.0\" y1=\"44.4\" x2=\"51.0\" y2=\"44.4\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"58.0\" y1=\"54.2\" x2=\"51.0\" y2=\"54.2\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"58.0\" y1=\"64.1\" x2=\"51.0\" y2=\"64.1\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"58.0\" y1=\"73.9\" x2=\"51.0\" y2=\"73.9\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"58.0\" y1=\"83.8\" x2=\"51.0\" y2=\"83.8\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"58.0\" y1=\"93.6\" x2=\"51.0\" y2=\"93.6\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"58.0\" y1=\"103.4\" x2=\"51.0\" y2=\"103.4\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"58.0\" y1=\"113.2\" x2=\"51.0\" y2=\"113.2\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"58.0\" y1=\"123.1\" x2=\"51.0\" y2=\"123.1\" stroke=\"#000000\" stroke-width=\"1.1\"/><text x=\"30\" y=\"70\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">rock</text><g transform=\"translate(84.0 70.0) rotate(0) scale(1)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.20\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><line x1=\"80.0\" y1=\"58.0\" x2=\"62.0\" y2=\"58.0\" stroke=\"#000000\" stroke-width=\"2.4\" stroke-dasharray=\"4 3\" marker-end=\"url(#arr-1101)\"/><text x=\"94\" y=\"54\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u2212\u2207f</text><line x1=\"70.0\" y1=\"90.0\" x2=\"112.0\" y2=\"90.0\" stroke=\"#000000\" stroke-width=\"2.6\" marker-end=\"url(#arr-1101)\"/><text x=\"116\" y=\"94\" font-size=\"10\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">\u03bc</text><line x1=\"150\" y1=\"10\" x2=\"150\" y2=\"128\" stroke=\"#000000\" stroke-width=\"0.8\" stroke-dasharray=\"2 3\"/><text x=\"160\" y=\"28\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">\u2460 \u2207f + \u03bc\u2207g = 0</text><text x=\"160\" y=\"50\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">\u2461 g \u2264 0</text><text x=\"160\" y=\"72\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">\u2462 \u03bc \u2265 0</text><text x=\"160\" y=\"94\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">\u2463 \u03bc\u00b7g = 0</text><text x=\"150.2\" y=\"115\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">forces cancel \u00b7 inside</text><text x=\"138.5\" y=\"126\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">walls only push \u00b7 off = 0</text></svg>",
    "coreTranslation": [
      "<strong>What:</strong> for $\\min f(x)$ subject to $h_i(x)=0$ and $g_j(x)\\le0$, a local minimizer that satisfies a constraint qualification (such as LICQ) has multipliers $\\lambda^*,\\mu^*$ making four conditions true.",
      "<strong>How:</strong> (1) <em>Stationarity</em> $\\nabla f+\\sum\\lambda_i\\nabla h_i+\\sum\\mu_j\\nabla g_j=0$; (2) <em>primal feasibility</em> $h=0,\\ g\\le0$; (3) <em>dual feasibility</em> $\\mu\\ge0$; (4) <em>complementary slackness</em> $\\mu_jg_j=0$.",
      "<strong>Why it matters:</strong> these four conditions turn a constrained minimization into a system you can solve by cases. They are necessary at a minimizer, and sufficient when the problem is convex."
    ],
    "math": "$$\\nabla f(x^*) + \\sum_{i=1}^p \\lambda_i^* \\nabla h_i(x^*) + \\sum_{j=1}^m \\mu_j^* \\nabla g_j(x^*) = 0, \\quad \\mu_j^* \\ge 0, \\quad \\mu_j^* g_j(x^*) = 0$$",
    "personalConnection": "<strong>The airplane analogy.</strong> The four KKT checks are the four things a parked plane must satisfy: gravity is cancelled by wall pushes ($\\nabla f+\\sum\\mu_j\\nabla g_j=0$), you are inside legal airspace ($g\\le0$), walls only push, never pull ($\\mu\\ge0$), and a wall you are not touching pushes with zero force ($\\mu_jg_j=0$).",
    "examTrap": "Pay obsessive attention to constraint orientation! If constraints are written $g_j(x) \\le 0$, then $\\mu_j \\ge 0$ with $\\mathcal{L} = f + \\mu^T g$. If written $g_j(x) \\ge 0$, either negate the constraint or write $\\mathcal{L} = f - \\mu^T g$.",
    "hint": "What four things must a parked plane satisfy?",
    "breakdown": [
      "<strong>$\\nabla f+\\sum\\lambda_i\\nabla h_i+\\sum\\mu_j\\nabla g_j=0$:</strong> gravity is cancelled by the wall pushes.",
      "<strong>$g\\le0$, $h=0$:</strong> you are inside the airspace.",
      "<strong>$\\mu_j\\ge0$:</strong> walls only push, never pull. <strong>$\\mu_jg_j=0$:</strong> a wall you are not touching pushes with zero."
    ]
  },
  {
    "id": 1102,
    "subject": "CMO",
    "topicId": "11_Karush_Kuhn_Tucker_Conditions_FONC_and_Sufficiency",
    "topicTitle": "11 \u00b7 KKT Conditions & Sufficiency",
    "cardNumber": "02",
    "category": "COMPLEMENTARY SLACKNESS",
    "highlighterClass": "highlight-amber",
    "title": "Complementary Slackness as an On/Off Switch",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1102\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"120\" y1=\"8\" x2=\"120\" y2=\"138\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"3 3\"/><line x1=\"104.0\" y1=\"20.0\" x2=\"104.0\" y2=\"120.0\" stroke=\"#000000\" stroke-width=\"2.4\"/><line x1=\"104.0\" y1=\"25.6\" x2=\"110.0\" y2=\"25.6\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"104.0\" y1=\"36.7\" x2=\"110.0\" y2=\"36.7\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"104.0\" y1=\"47.8\" x2=\"110.0\" y2=\"47.8\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"104.0\" y1=\"58.9\" x2=\"110.0\" y2=\"58.9\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"104.0\" y1=\"70.0\" x2=\"110.0\" y2=\"70.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"104.0\" y1=\"81.1\" x2=\"110.0\" y2=\"81.1\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"104.0\" y1=\"92.2\" x2=\"110.0\" y2=\"92.2\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"104.0\" y1=\"103.3\" x2=\"110.0\" y2=\"103.3\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"104.0\" y1=\"114.4\" x2=\"110.0\" y2=\"114.4\" stroke=\"#000000\" stroke-width=\"1.1\"/><g transform=\"translate(46.0 70.0) rotate(0) scale(1)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.20\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><line x1=\"66.0\" y1=\"70.0\" x2=\"98.0\" y2=\"70.0\" stroke=\"#000000\" stroke-width=\"1.4\" stroke-dasharray=\"2 2\" marker-end=\"url(#arr-1102)\"/><text x=\"82\" y=\"62\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">gap</text><text x=\"60\" y=\"18\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">g &lt; 0 : OFF</text><text x=\"60\" y=\"128\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u03bc = 0, no push</text><line x1=\"228.0\" y1=\"20.0\" x2=\"228.0\" y2=\"120.0\" stroke=\"#000000\" stroke-width=\"2.4\"/><line x1=\"228.0\" y1=\"25.6\" x2=\"234.0\" y2=\"25.6\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"228.0\" y1=\"36.7\" x2=\"234.0\" y2=\"36.7\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"228.0\" y1=\"47.8\" x2=\"234.0\" y2=\"47.8\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"228.0\" y1=\"58.9\" x2=\"234.0\" y2=\"58.9\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"228.0\" y1=\"70.0\" x2=\"234.0\" y2=\"70.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"228.0\" y1=\"81.1\" x2=\"234.0\" y2=\"81.1\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"228.0\" y1=\"92.2\" x2=\"234.0\" y2=\"92.2\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"228.0\" y1=\"103.3\" x2=\"234.0\" y2=\"103.3\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"228.0\" y1=\"114.4\" x2=\"234.0\" y2=\"114.4\" stroke=\"#000000\" stroke-width=\"1.1\"/><g transform=\"translate(210.0 70.0) rotate(0) scale(1)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.20\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><line x1=\"196.0\" y1=\"90.0\" x2=\"164.0\" y2=\"90.0\" stroke=\"#000000\" stroke-width=\"2.6\" marker-end=\"url(#arr-1102)\"/><text x=\"166\" y=\"84\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">\u03bc>0</text><text x=\"172\" y=\"18\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">g = 0 : ON</text><text x=\"172\" y=\"128\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">wall pushes back</text></svg>",
    "drawingCaption": "A wall is an on/off switch: across the valley (gap, g<0) it pushes with zero; wing against it (g=0) it may push back with \u03bc>0.",
    "coreTranslation": [
      "<strong>What:</strong> complementary slackness says $\\mu_j\\,g_j(x^*)=0$ for every inequality: for each constraint, either the multiplier is zero or the constraint is active, never a positive multiplier on a slack constraint.",
      "<strong>How:</strong> if $g_j(x^*)<0$ (inside, not touching) then $\\mu_j=0$ because the wall does nothing. If $\\mu_j>0$ then $g_j(x^*)=0$ because the wall only pushes when you are on it.",
      "<strong>Why it matters:</strong> it is an on/off switch that lets you solve KKT by guessing which constraints are active. Both $g_j=0$ and $\\mu_j=0$ can hold at once (weak complementarity, a degenerate case)."
    ],
    "math": "$$\\mu_j^* g_j(x^*) = 0 \\iff \\begin{cases} g_j(x^*) < 0 \\implies \\mu_j^* = 0 \\\\ \\mu_j^* > 0 \\implies g_j(x^*) = 0 \\end{cases}$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Each mountain wall is an on/off switch. A wall across the valley ($g\\lt0$, not touching) is OFF: $\\mu=0$. A wall your wing is resting on ($g=0$) is ON and may push back with $\\mu\\gt0$. You never have both a gap and a push.",
    "examTrap": "Can BOTH $g_j(x^*) = 0$ and $\\mu_j^* = 0$? YES! This is called <strong>weak complementarity</strong> (or degeneracy). It often causes non-isolated Lagrange multipliers and numerical difficulties.",
    "hint": "Which two statements does $\\mu_jg_j=0$ hide?",
    "breakdown": [
      "<strong>$g_j\\lt0\\Rightarrow\\mu_j=0$:</strong> a gap between wing and wall means no push (switch OFF).",
      "<strong>$\\mu_j\\gt0\\Rightarrow g_j=0$:</strong> a wall that is pushing must be touching (switch ON).",
      "<strong>Multiplying them is a compact way to say 'never both'.</strong>"
    ]
  },
  {
    "id": 1103,
    "subject": "CMO",
    "topicId": "11_Karush_Kuhn_Tucker_Conditions_FONC_and_Sufficiency",
    "topicTitle": "11 \u00b7 KKT Conditions & Sufficiency",
    "cardNumber": "03",
    "category": "CONVEX SUFFICIENCY",
    "highlighterClass": "highlight-emerald",
    "title": "KKT Convex Sufficiency Theorem",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1103\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><path d=\"M32.0,32.0 L36.4,39.8 L40.8,47.2 L45.2,54.2 L49.6,60.8 L54.0,67.0 L58.4,72.8 L62.8,78.2 L67.2,83.2 L71.6,87.8 L76.0,92.0 L80.4,95.8 L84.8,99.2 L89.2,102.2 L93.6,104.8 L98.0,107.0 L102.4,108.8 L106.8,110.2 L111.2,111.2 L115.6,111.8 L120.0,112.0 L124.4,111.8 L128.8,111.2 L133.2,110.2 L137.6,108.8 L142.0,107.0 L146.4,104.8 L150.8,102.2 L155.2,99.2 L159.6,95.8 L164.0,92.0 L168.4,87.8 L172.8,83.2 L177.2,78.2 L181.6,72.8 L186.0,67.0 L190.4,60.8 L194.8,54.2 L199.2,47.2 L203.6,39.8 L208.0,32.0\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.4\"/><line x1=\"32.0\" y1=\"28.0\" x2=\"32.0\" y2=\"112.0\" stroke=\"#000000\" stroke-width=\"2.4\"/><line x1=\"32.0\" y1=\"35.0\" x2=\"26.0\" y2=\"35.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"32.0\" y1=\"49.0\" x2=\"26.0\" y2=\"49.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"32.0\" y1=\"63.0\" x2=\"26.0\" y2=\"63.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"32.0\" y1=\"77.0\" x2=\"26.0\" y2=\"77.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"32.0\" y1=\"91.0\" x2=\"26.0\" y2=\"91.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"32.0\" y1=\"105.0\" x2=\"26.0\" y2=\"105.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"208.0\" y1=\"28.0\" x2=\"208.0\" y2=\"112.0\" stroke=\"#000000\" stroke-width=\"2.4\"/><line x1=\"208.0\" y1=\"35.0\" x2=\"214.0\" y2=\"35.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"208.0\" y1=\"49.0\" x2=\"214.0\" y2=\"49.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"208.0\" y1=\"63.0\" x2=\"214.0\" y2=\"63.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"208.0\" y1=\"77.0\" x2=\"214.0\" y2=\"77.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"208.0\" y1=\"91.0\" x2=\"214.0\" y2=\"91.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"208.0\" y1=\"105.0\" x2=\"214.0\" y2=\"105.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><g transform=\"translate(120.0 94.0) rotate(0) scale(1)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.20\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><line x1=\"66.0\" y1=\"112.0\" x2=\"174.0\" y2=\"112.0\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"4 3\"/><circle cx=\"120.0\" cy=\"112.0\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"120\" y=\"126\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">global min</text><text x=\"120\" y=\"16\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">convex valley, flat walls: one lowest spot</text><text x=\"120\" y=\"142\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">KKT holds  \u21d2  global minimum</text></svg>",
    "drawingCaption": "A convex valley with flat walls has only one lowest parking spot: if the forces balance there, nothing deeper exists elsewhere.",
    "coreTranslation": [
      "<strong>Master Sufficiency Theorem:</strong> Suppose $f(x)$ and all inequality constraints $g_j(x)$ are convex functions, and all equality constraints $h_i(x) = a_i^T x - b_i$ are affine.",
      "If $(x^*, \\lambda^*, \\mu^*)$ satisfies the 4 KKT conditions, then $x^*$ is an <strong>absolute global minimizer</strong> of the constrained optimization problem!",
      "<strong>Proof:</strong> Since $\\mu_j^* \\ge 0$, $\\mathcal{L}(x, \\lambda^*, \\mu^*)$ is convex in $x$. Stationarity $\\nabla_x \\mathcal{L} = 0$ makes $x^*$ a global minimizer of $\\mathcal{L}$. Complementary slackness then sandwiches $f(x^*) \\le \\mathcal{L}(x^*, \\lambda^*, \\mu^*) \\le \\mathcal{L}(x, \\lambda^*, \\mu^*) \\le f(x)$."
    ],
    "math": "$$f, g_j \\text{ convex}, \\, h_i \\text{ affine}, \\, (x^*, \\lambda^*, \\mu^*) \\in \\text{KKT} \\implies f(x^*) \\le f(x) \\; \\forall \\, x \\in \\Omega$$",
    "personalConnection": "<strong>The airplane analogy.</strong> In a convex valley with flat walls there is only one lowest parking spot. If you are parked where the wall pushes cancel gravity (KKT holds), no deeper valley exists anywhere else in the legal airspace, so this stationary spot is already the global minimum.",
    "examTrap": "Equality constraints $h_i(x) = 0$ MUST be AFFINE ($A x = b$)! If an equality constraint is non-linear (even if $h_i$ is convex), the feasible set $\\{x : h_i(x) = 0\\}$ is NOT convex, and KKT sufficiency fails.",
    "hint": "When does a balanced parking spot have to be the global lowest one?",
    "breakdown": [
      "<strong>$f,g_j$ convex and $h_i$ affine:</strong> a convex valley with convex airspace.",
      "<strong>KKT then says a balanced point</strong> beats every other legal point: $f(x^*)\\le f(x)$.",
      "<strong>It works because the tangent plane at $x^*$ lies under the terrain,</strong> and the wall pushes cannot make it better."
    ]
  },
  {
    "id": 1104,
    "subject": "CMO",
    "topicId": "11_Karush_Kuhn_Tucker_Conditions_FONC_and_Sufficiency",
    "topicTitle": "11 \u00b7 KKT Conditions & Sufficiency",
    "cardNumber": "04",
    "category": "CONSTRAINT QUALIFICATIONS",
    "highlighterClass": "highlight-violet",
    "title": "LICQ & Why Regularity is Essential",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1104\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"120\" y1=\"8\" x2=\"120\" y2=\"138\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"3 3\"/><line x1=\"20.0\" y1=\"100.0\" x2=\"100.0\" y2=\"100.0\" stroke=\"#000000\" stroke-width=\"2.4\"/><line x1=\"25.7\" y1=\"100.0\" x2=\"25.7\" y2=\"106.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"37.1\" y1=\"100.0\" x2=\"37.1\" y2=\"106.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"48.6\" y1=\"100.0\" x2=\"48.6\" y2=\"106.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"60.0\" y1=\"100.0\" x2=\"60.0\" y2=\"106.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"71.4\" y1=\"100.0\" x2=\"71.4\" y2=\"106.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"82.9\" y1=\"100.0\" x2=\"82.9\" y2=\"106.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"94.3\" y1=\"100.0\" x2=\"94.3\" y2=\"106.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"100.0\" y1=\"100.0\" x2=\"100.0\" y2=\"24.0\" stroke=\"#000000\" stroke-width=\"2.4\"/><line x1=\"100.0\" y1=\"93.7\" x2=\"106.0\" y2=\"93.7\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"100.0\" y1=\"81.0\" x2=\"106.0\" y2=\"81.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"100.0\" y1=\"68.3\" x2=\"106.0\" y2=\"68.3\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"100.0\" y1=\"55.7\" x2=\"106.0\" y2=\"55.7\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"100.0\" y1=\"43.0\" x2=\"106.0\" y2=\"43.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"100.0\" y1=\"30.3\" x2=\"106.0\" y2=\"30.3\" stroke=\"#000000\" stroke-width=\"1.1\"/><g transform=\"translate(70.0 70.0) rotate(-45) scale(0.8)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.50\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><circle cx=\"100.0\" cy=\"100.0\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><line x1=\"60.0\" y1=\"100.0\" x2=\"60.0\" y2=\"122.0\" stroke=\"#000000\" stroke-width=\"2\" marker-end=\"url(#arr-1104)\"/><text x=\"66\" y=\"124\" font-size=\"8.5\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">\u2207g\u2081</text><line x1=\"100.0\" y1=\"50.0\" x2=\"118.0\" y2=\"50.0\" stroke=\"#000000\" stroke-width=\"2\" marker-end=\"url(#arr-1104)\"/><text x=\"104\" y=\"44\" font-size=\"8.5\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">\u2207g\u2082</text><text x=\"60\" y=\"18\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">independent normals \u2713</text><text x=\"60\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">LICQ holds</text><path d=\"M130.0,76.0 L136.0,75.6 L142.0,74.3 L148.0,72.1 L154.0,69.1 L160.0,65.2 L166.0,60.4 L172.0,54.8 L178.0,48.4 L184.0,41.0 L190.0,32.8 L196.0,23.7 L202.0,13.8 L208.0,3.0 L214.0,-8.7\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.2\"/><line x1=\"130\" y1=\"76\" x2=\"224\" y2=\"76\" stroke=\"#000000\" stroke-width=\"2.2\"/><circle cx=\"130.0\" cy=\"76.0\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><g transform=\"translate(168.0 64.0) rotate(0) scale(0.6)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.00\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><line x1=\"196.0\" y1=\"76.0\" x2=\"196.0\" y2=\"100.0\" stroke=\"#000000\" stroke-width=\"2\" marker-end=\"url(#arr-1104)\"/><text x=\"200\" y=\"104\" font-size=\"8.5\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">\u2207g\u2082</text><line x1=\"196.0\" y1=\"42.0\" x2=\"196.0\" y2=\"20.0\" stroke=\"#000000\" stroke-width=\"2\" marker-end=\"url(#arr-1104)\"/><text x=\"200\" y=\"24\" font-size=\"8.5\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">\u2207g\u2081</text><text x=\"176\" y=\"18\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\"></text><text x=\"176\" y=\"128\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">parallel normals \u2717</text><text x=\"176\" y=\"140\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">LICQ fails (cusp)</text></svg>",
    "drawingCaption": "Left: two touching walls with independent normals pin the plane uniquely. Right: a cusp where both normals point the same way, so the wall pushes cannot be told apart.",
    "coreTranslation": [
      "<strong>Linear Independence Constraint Qualification (LICQ):</strong> The gradients of all active constraints $\\{\\nabla h_i(x^*)\\}_{i=1}^p \\cup \\{\\nabla g_j(x^*)\\}_{j \\in \\mathcal{A}(x^*)}$ must be <strong>linearly independent vectors</strong> in $\\mathbb{R}^n$.",
      "<strong>The Danger:</strong> KKT conditions are NOT guaranteed to hold at a local minimum if LICQ (or another CQ like MFCQ or Slater) fails!",
      "<strong>Classic Counterexample:</strong> $\\min x_1$ s.t. $(1-x_1)^3 - x_2 \\ge 0, x_2 \\ge 0$. At $x^* = (1, 0)$, both active gradients point along $(0, 1)^T$. They are collinear (linearly dependent). $-\\nabla f = (-1, 0)^T$ cannot be spanned by $(0, 1)^T$, so NO KKT multipliers exist!"
    ],
    "math": "$$\\operatorname{rank}\\left( [\\nabla h_i(x^*)_{i=1}^p, \\; \\nabla g_j(x^*)_{j \\in \\mathcal{A}(x^*)}] \\right) = p + |\\mathcal{A}(x^*)| \\quad (\\text{LICQ})$$",
    "personalConnection": "<strong>The airplane analogy.</strong> LICQ says the walls you are touching push in independent directions. If two touching walls have normals pointing the same way (a cusp or a knife-edge), the pilot cannot tell how gravity splits between them: the push forces are not unique and may not exist at all, so KKT can fail at a true minimum.",
    "examTrap": "Never apply KKT necessary conditions without stating that LICQ holds! If an exam question asks 'Does $x^*$ satisfy KKT?', first test if the active constraint gradients are linearly independent.",
    "hint": "What do the touching walls' normals have to look like for the pushes to be well defined?",
    "breakdown": [
      "<strong>rank = $p+|\\mathcal A|$:</strong> the normals of all active walls are linearly independent.",
      "<strong>Independence means the push on each wall is uniquely determined</strong> by the force balance.",
      "<strong>If two normals line up (a cusp),</strong> the pushes are not unique or may not exist and KKT can fail at a true minimum."
    ]
  },
  {
    "id": 1105,
    "subject": "CMO",
    "topicId": "11_Karush_Kuhn_Tucker_Conditions_FONC_and_Sufficiency",
    "topicTitle": "11 \u00b7 KKT Conditions & Sufficiency",
    "cardNumber": "05",
    "category": "CONSTRAINT QUALIFICATIONS",
    "highlighterClass": "highlight-indigo",
    "title": "Slater\u2019s Condition for Convex Programs",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1105\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><polygon points=\"20,30 104,22 112,112 28,120\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"2\"/><g transform=\"translate(66.0 70.0) rotate(-10) scale(1)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.20\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><circle cx=\"66.0\" cy=\"70.0\" r=\"2.5\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"70\" y=\"88\" font-size=\"9.5\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">x\u0304</text><text x=\"66\" y=\"140\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">room inside: g &lt; 0 strictly \u2713</text><line x1=\"120\" y1=\"8\" x2=\"120\" y2=\"138\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"3 3\"/><line x1=\"146\" y1=\"36\" x2=\"218\" y2=\"106\" stroke=\"#000000\" stroke-width=\"4\"/><text x=\"176\" y=\"132\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">no interior: knife-edge \u2717</text><text x=\"176\" y=\"18\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">Slater fails</text><g transform=\"translate(182.0 71.0) rotate(40) scale(0.7)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.71\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g></svg>",
    "drawingCaption": "Slater's condition: a hangar with room to move (a strictly interior point x\u0304, left) versus a zero-thickness knife-edge corridor (right).",
    "coreTranslation": [
      "<strong>Slater's Constraint Qualification:</strong> For a convex optimization problem $\\min f(x)$ s.t. $g_j(x) \\le 0, A x = b$, Slater's condition holds if there exists at least one point $\\hat{x} \\in \\operatorname{relint}(\\mathcal{D})$ such that:",
      "$$g_j(\\hat{x}) < 0 \\quad \\forall \\, j = 1, \\dots, m, \\quad \\text{and} \\quad A \\hat{x} = b$$",
      "<strong>Fundamental Implication:</strong> If the primal problem is convex and Slater's condition holds, then <strong>Strong Duality holds ($d^* = p^*$)</strong>, the dual optimal value is attained, and KKT multipliers are guaranteed to exist!"
    ],
    "math": "$$\\exists \\, \\hat{x} : g_j(\\hat{x}) < 0 \\; (j=1..m), \\; A \\hat{x} = b \\implies d^* = p^* \\quad (\\text{Strong Duality})$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Slater's condition: the legal airspace has real volume, so there is at least one point strictly inside every wall ($g\\lt0$). It is a hangar with room to move, not a zero-thickness corridor squeezed between walls. With that breathing room, strong duality holds.",
    "examTrap": "Slater requires STRICT inequality $g_j(\\hat{x}) < 0$ only for NON-AFFINE convex constraints. For purely affine inequality constraints ($c_j^T x \\le d_j$), simple feasibility without strict inequality is sufficient!",
    "hint": "What kind of room does the airspace need for the dual floor to touch the lowest altitude?",
    "breakdown": [
      "<strong>$g_j(\\hat x)\\lt0$ for all $j$:</strong> a point strictly inside every wall.",
      "<strong>$A\\hat x=b$:</strong> it also satisfies the equality walls.",
      "<strong>With that room, $d^*=p^*$:</strong> zero duality gap for a convex program."
    ]
  },
  {
    "id": 1106,
    "subject": "CMO",
    "topicId": "11_Karush_Kuhn_Tucker_Conditions_FONC_and_Sufficiency",
    "topicTitle": "11 \u00b7 KKT Conditions & Sufficiency",
    "cardNumber": "06",
    "category": "WORKED BENCHMARK",
    "highlighterClass": "highlight-rose",
    "title": "Worked Benchmark: KKT Active Set Case Analysis",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1106\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><ellipse cx=\"56\" cy=\"112\" rx=\"66\" ry=\"33\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"4 3\" transform=\"rotate(0 56 112)\"/><line x1=\"168.0\" y1=\"144.0\" x2=\"40.0\" y2=\"16.0\" stroke=\"#000000\" stroke-width=\"2.4\"/><line x1=\"136.0\" y1=\"112.0\" x2=\"56.0\" y2=\"32.0\" stroke=\"#000000\" stroke-width=\"0.1\"/><line x1=\"131.0\" y1=\"107.0\" x2=\"126.8\" y2=\"111.2\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"121.0\" y1=\"97.0\" x2=\"116.8\" y2=\"101.2\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"111.0\" y1=\"87.0\" x2=\"106.8\" y2=\"91.2\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"101.0\" y1=\"77.0\" x2=\"96.8\" y2=\"81.2\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"91.0\" y1=\"67.0\" x2=\"86.8\" y2=\"71.2\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"81.0\" y1=\"57.0\" x2=\"76.8\" y2=\"61.2\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"71.0\" y1=\"47.0\" x2=\"66.8\" y2=\"51.2\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"61.0\" y1=\"37.0\" x2=\"56.8\" y2=\"41.2\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"42\" y1=\"112\" x2=\"226\" y2=\"112\" stroke=\"#000000\" stroke-width=\"1\" marker-end=\"url(#arr-1106)\"/><line x1=\"56\" y1=\"120\" x2=\"56\" y2=\"8\" stroke=\"#000000\" stroke-width=\"1\" marker-end=\"url(#arr-1106)\"/><circle cx=\"56.0\" cy=\"112.0\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"6\" y=\"20\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"start\" fill=\"#000000\">Case 1: \u03bc = 0</text><text x=\"6\" y=\"32\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">lowest point is outside \u2717</text><g transform=\"translate(120.0 96.0) rotate(-35) scale(0.7)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.71\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><circle cx=\"120.0\" cy=\"96.0\" r=\"2.5\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"126.0\" y=\"108.0\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">x*</text><text x=\"236\" y=\"50\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"end\" fill=\"#000000\">Case 2: on the wall</text><text x=\"236\" y=\"62\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"end\" fill=\"#000000\">\u03bc* = 8/5 > 0 \u2713</text></svg>",
    "drawingCaption": "Contours of f centred at the origin. Case 1 (free flight, \u03bc=0) lands outside the legal side of the wall x\u2081+x\u2082 \u2265 1. Case 2 (pressed to the wall) gives x*=(4/5,1/5) with \u03bc*=8/5.",
    "coreTranslation": [
      "<strong>Problem:</strong> Minimize $f(x) = x_1^2 + 4 x_2^2$ subject to $g(x) = 1 - x_1 - x_2 \\le 0$.",
      "<strong>Case 1 (Inactive, $\\mu = 0$):</strong> $\\nabla f(x) = [2 x_1, 8 x_2]^T = [0, 0]^T \\implies x = (0, 0)$. Check feasibility: $g(0, 0) = 1 > 0$ $\\implies$ <strong>INFEASIBLE!</strong> Reject Case 1.",
      "<strong>Case 2 (Active, $g(x) = 0$):</strong> $x_1 + x_2 = 1$. Stationarity: $2 x_1 - \\mu = 0$ and $8 x_2 - \\mu = 0 \\implies x_1 = \\mu/2, x_2 = \\mu/8$. Substitute: $\\frac{\\mu}{2} + \\frac{\\mu}{8} = 1 \\implies \\frac{5\\mu}{8} = 1 \\implies \\mu^* = 8/5 > 0$. Point $x^* = (4/5, 1/5)$. Both dual feasibility and complementary slackness hold!"
    ],
    "math": "$$\\nabla f(x^*) + \\mu^* \\nabla g(x^*) = \\begin{bmatrix} 2 x_1 \\\\ 8 x_2 \\end{bmatrix} + \\mu^* \\begin{bmatrix} -1 \\\\ -1 \\end{bmatrix} = \\mathbf{0} \\implies x^* = \\left(\\frac{4}{5}, \\frac{1}{5}\\right), \\; \\mu^* = \\frac{8}{5} > 0$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Case analysis is the pilot's two guesses. Case 1: assume you are floating free in the open (wall push $\\mu=0$); if the lowest open-air point lies outside legal airspace, that guess is dead. Case 2: assume you are pressed against the wall; solving the force balance gives a positive push $\\mu=8/5$, so the guess is consistent.",
    "examTrap": "When solving KKT by cases, NEVER stop upon finding a solution! You must verify dual feasibility ($\\mu_j \\ge 0$) and check if any other active sets could also satisfy KKT.",
    "hint": "Which of the two guesses survives: floating free or pressed to the wall?",
    "breakdown": [
      "<strong>$\\nabla f=(2x_1,8x_2)$:</strong> the gravity pull; $\\nabla g=(-1,-1)$ is the wall normal.",
      "<strong>Case 1 ($\\mu=0$):</strong> $\\nabla f=0$ puts you at the origin, which breaks the wall constraint, so the guess fails.",
      "<strong>Case 2 (on the wall):</strong> $x_1+x_2=1$ and $2x_1=8x_2$ give $x^*=(4/5,1/5)$ and $\\mu^*=8/5\\gt0$."
    ]
  },
  {
    "id": 1201,
    "subject": "CMO",
    "topicId": "12_Second_Order_Optimality_Conditions_in_Constrained_Optimization",
    "topicTitle": "12 \u00b7 Second-Order Constrained Conditions",
    "cardNumber": "01",
    "category": "SECOND-ORDER NECESSARY CONDITIONS",
    "highlighterClass": "highlight-cyan",
    "title": "SONC: Curvature on the Tangent Subspace M",
    "textbookImg": "assets/luenberger_fig11_4.png",
    "textbookRef": "Luenberger & Ye (4th ed), Sect. 11.5, Fig. 11.4 (p. 336)",
    "drawingCaption": "Solid: the terrain along the runway (tangent subspace M) must be level or curve up. Dashed: across the runway it may plunge steeply, and that does not matter.",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1201\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><path d=\"M40.0,30.0 L44.0,34.5 L48.0,38.7 L52.0,42.8 L56.0,46.6 L60.0,50.1 L64.0,53.5 L68.0,56.6 L72.0,59.4 L76.0,62.1 L80.0,64.5 L84.0,66.7 L88.0,68.6 L92.0,70.4 L96.0,71.9 L100.0,73.1 L104.0,74.2 L108.0,75.0 L112.0,75.5 L116.0,75.9 L120.0,76.0 L124.0,75.9 L128.0,75.5 L132.0,75.0 L136.0,74.2 L140.0,73.1 L144.0,71.9 L148.0,70.4 L152.0,68.6 L156.0,66.7 L160.0,64.5 L164.0,62.1 L168.0,59.4 L172.0,56.6 L176.0,53.5 L180.0,50.1 L184.0,46.6 L188.0,42.8 L192.0,38.7 L196.0,34.5 L200.0,30.0\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.4\"/><path d=\"M40.0,126.0 L44.0,121.1 L48.0,116.5 L52.0,112.1 L56.0,108.0 L60.0,104.1 L64.0,100.5 L68.0,97.1 L72.0,94.0 L76.0,91.1 L80.0,88.5 L84.0,86.1 L88.0,84.0 L92.0,82.1 L96.0,80.5 L100.0,79.1 L104.0,78.0 L108.0,77.1 L112.0,76.5 L116.0,76.1 L120.0,76.0 L124.0,76.1 L128.0,76.5 L132.0,77.1 L136.0,78.0 L140.0,79.1 L144.0,80.5 L148.0,82.1 L152.0,84.0 L156.0,86.1 L160.0,88.5 L164.0,91.1 L168.0,94.0 L172.0,97.1 L176.0,100.5 L180.0,104.1 L184.0,108.0 L188.0,112.1 L192.0,116.5 L196.0,121.1 L200.0,126.0\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.6\" stroke-dasharray=\"5 3\"/><g transform=\"translate(120.0 66.0) rotate(0) scale(0.8)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.50\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><circle cx=\"120.0\" cy=\"76.0\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"42\" y=\"20\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">along runway M: d\u1d40\u2207\u00b2L d \u2265 0 \u2713</text><text x=\"160\" y=\"134\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">off the runway it may plunge</text><text x=\"120\" y=\"144\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">(that is fine)</text></svg>",
    "coreTranslation": [
      "<strong>Second-Order Necessary Condition (SONC):</strong> Let $x^*$ be a regular local minimizer of $f$ subject to $h(x) = 0$ and $g(x) \\le 0$, with multipliers $\\lambda^*, \\mu^*$.",
      "Then the Hessian of the Lagrangian with respect to $x$, denoted $\\nabla_{xx}^2 \\mathcal{L}(x^*, \\lambda^*, \\mu^*)$, must be <strong>Positive Semidefinite on the Tangent Subspace $M$</strong>:",
      "$$d^T \\nabla_{xx}^2 \\mathcal{L}(x^*, \\lambda^*, \\mu^*) d \\ge 0 \\quad \\forall \\, d \\in M(x^*)$$, where $M(x^*) = \\{d : \\nabla h_i(x^*)^T d = 0, \\; \\nabla g_j(x^*)^T d = 0 \\; (j \\in \\mathcal{A}(x^*))\\}$."
    ],
    "math": "$$d^T \\nabla_{xx}^2 \\mathcal{L}(x^*, \\lambda^*, \\mu^*) d \\ge 0 \\quad \\forall \\, d \\in M(x^*) = \\operatorname{Null}\\left( [\\nabla h(x^*)^T ; \\nabla g_{\\mathcal{A}}(x^*)^T] \\right)$$",
    "personalConnection": "<strong>The airplane analogy.</strong> The runway is the tangent subspace $M$: the only headings you can roll along while keeping your wheels on the ground. The terrain may fall steeply away on both sides of the runway (negative curvature in the full space), but what matters is that the runway itself is level or curves upward, i.e. $d^\\top\\nabla^2\\mathcal L\\,d\\ge0$ for $d\\in M$.",
    "examTrap": "The ambient Hessian $\\nabla^2 f(x^*)$ or even $\\nabla_{xx}^2 \\mathcal{L}$ DOES NOT need to be positive semidefinite everywhere! It only needs to be positive semidefinite when tested against vectors $d$ lying in the tangent subspace $M$.",
    "hint": "Along which directions must the terrain curve upward?",
    "breakdown": [
      "<strong>$\\nabla^2_{xx}\\mathcal L$ = the Lagrangian's curvature:</strong> the terrain's curvature plus the walls' curvature weighted by their pushes.",
      "<strong>$d\\in M(x^*)$ = the runway:</strong> directions that keep all touching walls fixed.",
      "<strong>$d^\\top\\nabla^2\\mathcal Ld\\ge0$ on the runway only:</strong> off the runway the ground may drop and it does not matter."
    ]
  },
  {
    "id": 1202,
    "subject": "CMO",
    "topicId": "12_Second_Order_Optimality_Conditions_in_Constrained_Optimization",
    "topicTitle": "12 \u00b7 Second-Order Constrained Conditions",
    "cardNumber": "02",
    "category": "SECOND-ORDER SUFFICIENCY",
    "highlighterClass": "highlight-amber",
    "title": "SOSC: Strict Positivity on the Critical Cone",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1202\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><path d=\"M36.0,47.5 L40.2,53.8 L44.4,59.8 L48.6,65.4 L52.8,70.7 L57.0,75.7 L61.2,80.4 L65.4,84.8 L69.6,88.8 L73.8,92.5 L78.0,95.9 L82.2,98.9 L86.4,101.7 L90.6,104.1 L94.8,106.2 L99.0,108.0 L103.2,109.4 L107.4,110.5 L111.6,111.4 L115.8,111.8 L120.0,112.0 L124.2,111.8 L128.4,111.4 L132.6,110.5 L136.8,109.4 L141.0,108.0 L145.2,106.2 L149.4,104.1 L153.6,101.7 L157.8,98.9 L162.0,95.9 L166.2,92.5 L170.4,88.8 L174.6,84.8 L178.8,80.4 L183.0,75.7 L187.2,70.7 L191.4,65.4 L195.6,59.8 L199.8,53.8 L204.0,47.5\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.4\"/><path d=\"M36.0,86.6 L40.2,89.1 L44.4,91.4 L48.6,93.7 L52.8,95.7 L57.0,97.7 L61.2,99.6 L65.4,101.3 L69.6,102.9 L73.8,104.3 L78.0,105.7 L82.2,106.9 L86.4,107.9 L90.6,108.9 L94.8,109.7 L99.0,110.4 L103.2,111.0 L107.4,111.4 L111.6,111.7 L115.8,111.9 L120.0,112.0 L124.2,111.9 L128.4,111.7 L132.6,111.4 L136.8,111.0 L141.0,110.4 L145.2,109.7 L149.4,108.9 L153.6,107.9 L157.8,106.9 L162.0,105.7 L166.2,104.3 L170.4,102.9 L174.6,101.3 L178.8,99.6 L183.0,97.7 L187.2,95.7 L191.4,93.7 L195.6,91.4 L199.8,89.1 L204.0,86.6\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"4 3\"/><g transform=\"translate(120.0 98.0) rotate(0) scale(0.8)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.50\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><circle cx=\"120.0\" cy=\"112.0\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><line x1=\"60.0\" y1=\"112.0\" x2=\"180.0\" y2=\"112.0\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"4 3\"/><text x=\"120\" y=\"20\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">strict bowl along every critical direction</text><text x=\"120\" y=\"132\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">d\u1d40\u2207\u00b2L d \u2265 c\u2016d\u2016\u00b2 > 0</text></svg>",
    "drawingCaption": "Along every critical heading the ground rises at least like a bowl c\u2016d\u2016\u00b2 above the parking spot: a strict local minimum.",
    "coreTranslation": [
      "<strong>Second-Order Sufficient Condition (SOSC):</strong> Suppose $(x^*, \\lambda^*, \\mu^*)$ satisfies KKT. If for all non-zero vectors $d \\in M(x^*)$ ($d \\ne 0$):",
      "$$d^T \\nabla_{xx}^2 \\mathcal{L}(x^*, \\lambda^*, \\mu^*) d > 0$$, then $x^*$ is a <strong>strict, isolated local minimizer</strong> of the constrained problem.",
      "<strong>Why SOSC is Powerful:</strong> Unlike the first-order KKT conditions (which could pick up local maxima or saddles), SOSC eliminates all doubt by guaranteeing positive quadratic bowl curvature along every feasible escape route."
    ],
    "math": "$$d^T \\nabla_{xx}^2 \\mathcal{L}(x^*, \\lambda^*, \\mu^*) d > 0 \\quad \\forall \\, d \\in M(x^*) \\setminus \\{0\\} \\implies x^* \\text{ is a strict local minimizer}$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Strict version: along every runway heading in the critical cone the ground curves strictly upward under your wheels, like the bottom of a bowl-shaped runway. Then your parking spot is a strict local minimum, even if the surrounding terrain drops off sideways.",
    "examTrap": "Semidefiniteness ($d^T \\nabla_{xx}^2 \\mathcal{L} d \\ge 0$) is NECESSARY, NOT sufficient! Strict inequality ($> 0$) is mandatory for sufficiency, exactly like $f''(x) > 0$ in single-variable calculus.",
    "hint": "What turns the necessary curvature test into a guarantee?",
    "breakdown": [
      "<strong>Strict $\\gt0$ for every non-zero critical direction:</strong> the runway curves strictly upward under the wheels.",
      "<strong>Critical cone = directions that neither gain nor lose altitude to first order.</strong>",
      "<strong>Together with the KKT conditions this proves a strict local minimum.</strong>"
    ]
  },
  {
    "id": 1203,
    "subject": "CMO",
    "topicId": "12_Second_Order_Optimality_Conditions_in_Constrained_Optimization",
    "topicTitle": "12 \u00b7 Second-Order Constrained Conditions",
    "cardNumber": "03",
    "category": "MATRIX ALGEBRA",
    "highlighterClass": "highlight-emerald",
    "title": "The Bordered Hessian Matrix Test",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1203\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"30\" y=\"26\" width=\"22\" height=\"22\" rx=\"0\" fill=\"#d9dee7\" stroke=\"#000000\" stroke-width=\"1.2\"/><rect x=\"52\" y=\"26\" width=\"70\" height=\"22\" rx=\"0\" fill=\"#d9dee7\" stroke=\"#000000\" stroke-width=\"1.2\"/><rect x=\"30\" y=\"48\" width=\"22\" height=\"70\" rx=\"0\" fill=\"#d9dee7\" stroke=\"#000000\" stroke-width=\"1.2\"/><rect x=\"52\" y=\"48\" width=\"70\" height=\"70\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.2\"/><text x=\"41\" y=\"41\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">0</text><text x=\"87\" y=\"41\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">J\u1d40 (wall normals)</text><text x=\"41\" y=\"86\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">J</text><text x=\"87\" y=\"86\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u2207\u00b2L</text><g transform=\"translate(160.0 40.0) rotate(0) scale(0.8)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.50\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"164\" y=\"66\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">(\u22121)^m \u00d7 minors</text><text x=\"164\" y=\"80\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">alternate in sign</text><text x=\"164\" y=\"94\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u21d2 runway dips</text><text x=\"120\" y=\"134\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">border the Hessian with the wall normals</text></svg>",
    "drawingCaption": "The bordered Hessian: wall normals J form the border around \u2207\u00b2L, and the sign pattern of its trailing minors tells you whether the runway dips at your parking spot.",
    "coreTranslation": [
      "<strong>What:</strong> the second-order test needs $d^T\\nabla^2_{xx}\\mathcal{L}\\,d>0$ only for directions $d$ in the tangent subspace. The bordered Hessian lets you test that without computing a basis of the subspace.",
      "<strong>How:</strong> with $p$ equality constraints and $A=\\nabla h(x^*)^T$, form $B=\\begin{bmatrix}0&A\\\\A^T&L\\end{bmatrix}$ ($L=\\nabla^2_{xx}\\mathcal{L}$). A strict local minimum needs the last $n-p$ leading principal minors of $B$ to all have the sign $(-1)^p$.",
      "<strong>Why it matters:</strong> for one constraint ($p=1$) in 2D you only check one number: $\\det B<0$ means minimum. Students often expect $\\det>0$ because that is the unconstrained rule."
    ],
    "math": "$$\\operatorname{sign}(\\det B_{2p+m}) = (-1)^p \\quad (\\forall \\, m = 1, \\dots, n-p)$$",
    "personalConnection": "<strong>The airplane analogy.</strong> The bordered Hessian is the instrument-panel shortcut. You do not parametrise the runway; you border the Hessian with the wall normals, and the sign pattern of its trailing minors tells you whether the runway dips at your parking spot (a minimum) or peaks (a maximum).",
    "examTrap": "For a single equality constraint ($p=1$), $(-1)^1 = -1$, meaning the determinant of the bordered Hessian MUST BE NEGATIVE ($\\det B < 0$) for a local minimum! Students routinely confuse this with unconstrained positive definiteness.",
    "hint": "How can the pilot test the runway's curvature without parametrising the runway?",
    "breakdown": [
      "<strong>The bordered matrix puts the wall normals around $\\nabla^2\\mathcal L$:</strong> $B=\\begin{bmatrix}0&J\\\\J^\\top&\\nabla^2\\mathcal L\\end{bmatrix}$.",
      "<strong>Its trailing principal minors carry the sign of the curvature restricted to the runway.</strong>",
      "<strong>The rule $\\operatorname{sign}\\det=(-1)^p$</strong> (for $p$ walls) says the runway dips: a minimum."
    ]
  },
  {
    "id": 1204,
    "subject": "CMO",
    "topicId": "12_Second_Order_Optimality_Conditions_in_Constrained_Optimization",
    "topicTitle": "12 \u00b7 Second-Order Constrained Conditions",
    "cardNumber": "04",
    "category": "CONE GEOMETRY",
    "highlighterClass": "highlight-violet",
    "title": "Strict Complementarity & The Critical Cone",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1204\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"120\" y1=\"8\" x2=\"120\" y2=\"138\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"3 3\"/><line x1=\"20.0\" y1=\"100.0\" x2=\"100.0\" y2=\"100.0\" stroke=\"#000000\" stroke-width=\"2.4\"/><line x1=\"25.7\" y1=\"100.0\" x2=\"25.7\" y2=\"106.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"37.1\" y1=\"100.0\" x2=\"37.1\" y2=\"106.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"48.6\" y1=\"100.0\" x2=\"48.6\" y2=\"106.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"60.0\" y1=\"100.0\" x2=\"60.0\" y2=\"106.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"71.4\" y1=\"100.0\" x2=\"71.4\" y2=\"106.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"82.9\" y1=\"100.0\" x2=\"82.9\" y2=\"106.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"94.3\" y1=\"100.0\" x2=\"94.3\" y2=\"106.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"100.0\" y1=\"100.0\" x2=\"100.0\" y2=\"20.0\" stroke=\"#000000\" stroke-width=\"2.4\"/><line x1=\"100.0\" y1=\"94.3\" x2=\"106.0\" y2=\"94.3\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"100.0\" y1=\"82.9\" x2=\"106.0\" y2=\"82.9\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"100.0\" y1=\"71.4\" x2=\"106.0\" y2=\"71.4\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"100.0\" y1=\"60.0\" x2=\"106.0\" y2=\"60.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"100.0\" y1=\"48.6\" x2=\"106.0\" y2=\"48.6\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"100.0\" y1=\"37.1\" x2=\"106.0\" y2=\"37.1\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"100.0\" y1=\"25.7\" x2=\"106.0\" y2=\"25.7\" stroke=\"#000000\" stroke-width=\"1.1\"/><g transform=\"translate(78.0 78.0) rotate(-45) scale(0.7)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.71\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><circle cx=\"100.0\" cy=\"100.0\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><line x1=\"60.0\" y1=\"100.0\" x2=\"60.0\" y2=\"78.0\" stroke=\"#000000\" stroke-width=\"2\" marker-end=\"url(#arr-1204)\"/><line x1=\"100.0\" y1=\"60.0\" x2=\"78.0\" y2=\"60.0\" stroke=\"#000000\" stroke-width=\"2\" marker-end=\"url(#arr-1204)\"/><text x=\"60\" y=\"22\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">all \u03bc > 0: pinned</text><text x=\"60\" y=\"122\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u03bc\u2081, \u03bc\u2082 > 0</text><text x=\"60\" y=\"134\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">critical cone = {0}</text><line x1=\"130.0\" y1=\"100.0\" x2=\"226.0\" y2=\"100.0\" stroke=\"#000000\" stroke-width=\"2.4\"/><line x1=\"135.3\" y1=\"100.0\" x2=\"135.3\" y2=\"106.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"146.0\" y1=\"100.0\" x2=\"146.0\" y2=\"106.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"156.7\" y1=\"100.0\" x2=\"156.7\" y2=\"106.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"167.3\" y1=\"100.0\" x2=\"167.3\" y2=\"106.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"178.0\" y1=\"100.0\" x2=\"178.0\" y2=\"106.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"188.7\" y1=\"100.0\" x2=\"188.7\" y2=\"106.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"199.3\" y1=\"100.0\" x2=\"199.3\" y2=\"106.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"210.0\" y1=\"100.0\" x2=\"210.0\" y2=\"106.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"220.7\" y1=\"100.0\" x2=\"220.7\" y2=\"106.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><g transform=\"translate(176.0 82.0) rotate(0) scale(0.8)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.50\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><circle cx=\"176.0\" cy=\"100.0\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><line x1=\"176.0\" y1=\"98.0\" x2=\"176.0\" y2=\"98.0\" stroke=\"#000000\" stroke-width=\"1\" marker-end=\"url(#arr-1204)\"/><line x1=\"176.0\" y1=\"84.0\" x2=\"214.0\" y2=\"70.0\" stroke=\"#000000\" stroke-width=\"1.5\" stroke-dasharray=\"3 2\" marker-end=\"url(#arr-1204)\"/><line x1=\"176.0\" y1=\"84.0\" x2=\"138.0\" y2=\"70.0\" stroke=\"#000000\" stroke-width=\"1.5\" stroke-dasharray=\"3 2\" marker-end=\"url(#arr-1204)\"/><line x1=\"176.0\" y1=\"84.0\" x2=\"176.0\" y2=\"44.0\" stroke=\"#000000\" stroke-width=\"1.5\" stroke-dasharray=\"3 2\" marker-end=\"url(#arr-1204)\"/><text x=\"176\" y=\"22\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u03bc = 0 : can peel off</text><text x=\"176\" y=\"134\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">critical cone = a wedge</text></svg>",
    "drawingCaption": "Left: both touching walls push strictly (\u03bc>0), so the plane is pinned with no freedom. Right: a touching wall pushing zero lets you peel away in some headings, so the critical cone is a wedge.",
    "coreTranslation": [
      "When inequality constraints are present, the tangent subspace generalises to the <strong>Critical Cone $C(x^*, \\mu^*)$</strong>:",
      "$$C(x^*, \\mu^*) = \\left\\{ d \\in \\mathbb{R}^n : \\begin{array}{ll} \\nabla h_i(x^*)^T d = 0 & \\forall i \\\\ \\nabla g_j(x^*)^T d = 0 & \\text{if } \\mu_j^* > 0 \\\\ \\nabla g_j(x^*)^T d \\le 0 & \\text{if } \\mu_j^* = 0, \\; j \\in \\mathcal{A}(x^*) \\end{array} \\right\\}$$",
      "<strong>Strict Complementarity:</strong> If $\\mu_j^* > 0$ for ALL active constraints ($j \\in \\mathcal{A}(x^*)$), the inequality conditions vanish and $C(x^*, \\mu^*)$ collapses into a <strong>pure linear subspace</strong>, making second-order checks vastly simpler!"
    ],
    "math": "$$\\text{Strict Complementarity } (\\mu_j^* > 0 \\; \\forall j \\in \\mathcal{A}) \\implies C(x^*, \\mu^*) = \\operatorname{Null}([\\nabla h(x^*)^T ; \\nabla g_{\\mathcal{A}}(x^*)^T])$$",
    "personalConnection": "<strong>The airplane analogy.</strong> If every wall you touch pushes strictly ($\\mu\\gt0$), the plane is pinned and the only legal motions are the headings that slide along all those walls: a subspace. If a touching wall pushes with exactly zero, you can peel away from it in some headings and the critical cone is a proper cone, not a subspace. In 2D, two strictly pushing walls leave zero freedom.",
    "examTrap": "If strict complementarity fails (i.e. an active constraint has $\\mu_j^* = 0$), $C(x^*)$ is a CONE, not a subspace! You must check $d^T \\nabla^2 \\mathcal{L} d > 0$ over the full cone, not just a subspace.",
    "hint": "When is the critical cone a subspace and when is it a wedge?",
    "breakdown": [
      "<strong>Every touching wall pushing ($\\mu_j\\gt0$):</strong> each wall's inequality becomes an equality, so the critical cone is a subspace (all directions that slide along all walls).",
      "<strong>A touching wall pushing zero ($\\mu_j=0$):</strong> you may peel away from it in one direction, which adds a half-space and gives a proper cone.",
      "<strong>In 2D with two strictly pushing walls the only legal direction is zero.</strong>"
    ]
  },
  {
    "id": 1205,
    "subject": "CMO",
    "topicId": "12_Second_Order_Optimality_Conditions_in_Constrained_Optimization",
    "topicTitle": "12 \u00b7 Second-Order Constrained Conditions",
    "cardNumber": "05",
    "category": "GEOMETRIC INTUITION",
    "highlighterClass": "highlight-indigo",
    "title": "Manifold Curvature vs. Ambient Space",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1205\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><path d=\"M24,34 Q120,176 216,34\" fill=\"none\" stroke=\"#000000\" stroke-width=\"3\"/><g transform=\"translate(120.0 98.0) rotate(0) scale(0.85)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.41\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><line x1=\"120.0\" y1=\"118.0\" x2=\"120.0\" y2=\"52.0\" stroke=\"#000000\" stroke-width=\"2.6\" marker-end=\"url(#arr-1205)\"/><text x=\"126\" y=\"62\" font-size=\"8.5\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">bank pushes</text><line x1=\"80.0\" y1=\"98.0\" x2=\"80.0\" y2=\"122.0\" stroke=\"#000000\" stroke-width=\"1.8\" stroke-dasharray=\"3 2\" marker-end=\"url(#arr-1205)\"/><text x=\"76\" y=\"132\" font-size=\"8.5\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"end\" fill=\"#000000\">\u2212\u2207f</text><text x=\"120\" y=\"18\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u2207\u00b2f alone: flat or negative</text><text x=\"120\" y=\"142\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u2207\u00b2f + \u03bc\u2207\u00b2g > 0 \u2713</text></svg>",
    "drawingCaption": "A banked, curved runway: the curve of the wall itself supplies an extra push, so the Lagrangian's curvature \u2207\u00b2f + \u03bc\u2207\u00b2g is what holds the plane in the bowl.",
    "coreTranslation": [
      "Why does the second-order condition use the Hessian of the <strong>Lagrangian</strong> $\\nabla_{xx}^2 \\mathcal{L} = \\nabla^2 f + \\sum \\lambda_i \\nabla^2 h_i$, rather than just $\\nabla^2 f$?",
      "<strong>Surface Curvature:</strong> As a point moves along a curved constraint surface $h(x) = 0$, the surface itself bends! The term $\\sum \\lambda_i \\nabla^2 h_i(x^*)$ accounts for the <strong>normal acceleration</strong> of curves constrained to the surface.",
      "<strong>Key Insight:</strong> Even if $\\nabla^2 f$ is flat or negative in the ambient space, strong curvature of the constraint surface $h(x)=0$ can make the restricted objective strictly convex!"
    ],
    "math": "$$\\frac{d^2}{dt^2} f(x(t))\\Big|_{t=0} = \\dot{x}(0)^T \\nabla^2 f(x^*) \\dot{x}(0) + \\nabla f(x^*)^T \\ddot{x}(0) = d^T \\left[ \\nabla^2 f(x^*) + \\sum_{i=1}^p \\lambda_i^* \\nabla^2 h_i(x^*) \\right] d$$",
    "personalConnection": "<strong>The airplane analogy.</strong> A banked, curved runway. Even if the terrain looks flat or hilltop-like in the ambient space, the curvature of the wall supplies an extra centripetal push, so the right curvature to check is that of the Lagrangian, $\\nabla^2 f+\\sum\\mu_j\\nabla^2 g_j$, restricted to the runway.",
    "examTrap": "Forgetting the $\\lambda_i \\nabla^2 h_i$ term! If you only evaluate $d^T \\nabla^2 f(x^*) d$, you are implicitly assuming the constraints are FLAT linear planes. For non-linear constraints, this yields completely wrong answers.",
    "hint": "What curvature actually matters on a banked runway: the terrain's or the Lagrangian's?",
    "breakdown": [
      "<strong>$\\dot x^\\top\\nabla^2f\\,\\dot x$:</strong> the terrain's own curvature along your velocity.",
      "<strong>$\\nabla f^\\top\\ddot x$:</strong> the extra term because your path is curved (a bank); at a KKT point it equals $\\sum\\mu_j\\nabla g_j^\\top\\ddot x$.",
      "<strong>Adding them gives $d^\\top[\\nabla^2f+\\sum\\mu_j\\nabla^2g_j]d$:</strong> the Lagrangian's curvature on the runway."
    ]
  },
  {
    "id": 1206,
    "subject": "CMO",
    "topicId": "12_Second_Order_Optimality_Conditions_in_Constrained_Optimization",
    "topicTitle": "12 \u00b7 Second-Order Constrained Conditions",
    "cardNumber": "06",
    "category": "WORKED BENCHMARK",
    "highlighterClass": "highlight-rose",
    "title": "Worked Benchmark: Bordered Hessian Sign Test",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1206\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><circle cx=\"112.0\" cy=\"66.0\" r=\"46.0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"2.2\"/><line x1=\"59.5\" y1=\"78.5\" x2=\"99.5\" y2=\"118.5\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"4 3\"/><circle cx=\"79.5\" cy=\"98.5\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"71.5\" y=\"112.5\" font-size=\"9.5\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"end\" fill=\"#000000\">x*</text><line x1=\"79.5\" y1=\"98.5\" x2=\"53.5\" y2=\"124.5\" stroke=\"#000000\" stroke-width=\"2.2\" marker-end=\"url(#arr-1206)\"/><text x=\"49.5\" y=\"138.5\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"end\" fill=\"#000000\">\u2212\u2207f</text><g transform=\"translate(126.0 26.0) rotate(-20) scale(0.7)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.71\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"112\" y=\"12\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">ring x\u2081\u00b2+x\u2082\u00b2 = 1</text><text x=\"168\" y=\"48\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">altitude</text><text x=\"168\" y=\"60\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">x\u2081+x\u2082</text><text x=\"168\" y=\"76\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">lowest: SW</text><text x=\"168\" y=\"96\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"start\" fill=\"#000000\">det B &lt; 0</text><text x=\"168\" y=\"108\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">\u21d2 min \u2713</text></svg>",
    "drawingCaption": "The plane laps a circular ring; altitude is x\u2081+x\u2082. The lowest point is south-west, and the bordered Hessian determinant \u22124\u221a2 < 0 confirms a strict minimum.",
    "coreTranslation": [
      "<strong>Problem:</strong> minimize $x_1+x_2$ on the circle $x_1^2+x_2^2=1$. Stationarity $1+2\\lambda x_i=0$ gives $x_1=x_2=-\\tfrac1{2\\lambda}$, so the candidates are $\\pm\\tfrac1{\\sqrt2}(1,1)$; take $x^*=(-\\tfrac1{\\sqrt2},-\\tfrac1{\\sqrt2})$ with $\\lambda^*=\\tfrac1{\\sqrt2}$.",
      "<strong>Second order:</strong> $\\nabla h=(-\\sqrt2,-\\sqrt2)$ and $\\nabla^2_{xx}\\mathcal{L}=2\\lambda^*I=\\sqrt2\\,I$, so $B=\\begin{bmatrix}0&-\\sqrt2&-\\sqrt2\\\\-\\sqrt2&\\sqrt2&0\\\\-\\sqrt2&0&\\sqrt2\\end{bmatrix}$ and $\\det B=-4\\sqrt2<0$, which is the required sign $(-1)^1=-1$. So $x^*$ is a strict local minimum.",
      "<strong>Cross-check:</strong> at the other candidate $+\\tfrac1{\\sqrt2}(1,1)$ we get $\\lambda^*=-\\tfrac1{\\sqrt2}$ and $\\det B=+4\\sqrt2>0$, which has the wrong sign: it is the maximum."
    ],
    "math": "$$\\det B = \\det \\begin{bmatrix} 0 & -\\sqrt{2} & -\\sqrt{2} \\\\ -\\sqrt{2} & \\sqrt{2} & 0 \\\\ -\\sqrt{2} & 0 & \\sqrt{2} \\end{bmatrix} = -4\\sqrt{2} < 0 = (-1)^1 \\implies x^* \\text{ is a strict local min}$$",
    "personalConnection": "<strong>The airplane analogy.</strong> The plane circles a circular no-fly ring and you want the lowest altitude $x_1+x_2$ on the ring. The lowest point is south-west at $(-1/\\sqrt2,-1/\\sqrt2)$: every step along the ring from there climbs, which is exactly what the bordered Hessian sign test confirms.",
    "examTrap": "If you tested the maximum at $(+1/\\sqrt{2}, +1/\\sqrt{2})$, you get $\\lambda^* = -1/\\sqrt{2}$ and $\\det B = +4\\sqrt{2} > 0$. Since $\\det B > 0 \\ne (-1)^1$, the SOSC fails, correctly detecting a local maximum!",
    "hint": "Does the sign of the bordered determinant confirm a minimum at the south-west point?",
    "breakdown": [
      "<strong>$B$'s border is the ring's normal;</strong> the inner block is the Lagrangian's Hessian at $x^*$.",
      "<strong>$\\det B=-4\\sqrt2\\lt0=(-1)^1$</strong> with one constraint ($p=1$) is exactly the sign pattern for a strict local minimum.",
      "<strong>If it were positive,</strong> the south-west point would be a maximum."
    ]
  },
  {
    "id": 1301,
    "subject": "CMO",
    "topicId": "13_Projections_onto_Convex_Sets",
    "topicTitle": "13 \u00b7 Projections onto Convex Sets",
    "cardNumber": "01",
    "category": "CONVEX GEOMETRY",
    "highlighterClass": "highlight-cyan",
    "title": "Hilbert Projection Theorem & Variational Inequality",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1301\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><polygon points=\"40,56 110,30 158,60 150,114 70,122 34,88\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"2\"/><text x=\"88\" y=\"86\" font-size=\"14\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u03a9</text><g transform=\"translate(190.0 20.0) rotate(130) scale(0.8)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.50\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><line x1=\"190.0\" y1=\"20.0\" x2=\"140.0\" y2=\"46.0\" stroke=\"#000000\" stroke-width=\"1.4\" stroke-dasharray=\"4 3\"/><circle cx=\"140.0\" cy=\"46.0\" r=\"2.8\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"136\" y=\"60\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"end\" fill=\"#000000\">P(p)</text><text x=\"204\" y=\"14\" font-size=\"11\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">p</text><circle cx=\"70.0\" cy=\"100.0\" r=\"2.4\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"65\" y=\"114\" font-size=\"9.5\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"end\" fill=\"#000000\">y</text><line x1=\"140.0\" y1=\"46.0\" x2=\"70.0\" y2=\"100.0\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"2 3\"/><text x=\"200\" y=\"112\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">(p\u2212P)\u1d40(y\u2212P) \u2264 0</text><text x=\"200\" y=\"126\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">every y makes an</text><text x=\"200\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">obtuse angle</text></svg>",
    "drawingCaption": "A plane blown outside the airspace is guided to the closest legal point P(p); every other legal point y sits at an obtuse angle from there.",
    "coreTranslation": [
      "<strong>What:</strong> for a non-empty, closed, convex set $C$ and any point $x$ there is exactly one closest point $\\Pi_C(x)\\in C$.",
      "<strong>How:</strong> $p=\\Pi_C(x)$ exactly when $\\langle x-p,\\ y-p\\rangle\\le0$ for every $y\\in C$: the arrow from $p$ to $x$ makes an obtuse (or right) angle with every arrow from $p$ into the set.",
      "<strong>Why it matters:</strong> this one inequality characterizes projections; it is the backbone of projected gradient, optimality conditions and every fixed-point argument that follows."
    ],
    "math": "$$p = \\Pi_C(x) \\iff p \\in C \\quad \\text{and} \\quad \\langle x - p, \\, y - p \\rangle \\le 0 \\quad \\forall \\, y \\in C$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Wind blows you out of legal airspace. The closest legal point $P(p)$ is where you reach the boundary by flying the shortest path. Every other legal point $y$ makes an obtuse (or right) angle at $P(p)$ with the line back to you: $(p-P(p))^\\top(y-P(p))\\le0$.",
    "examTrap": "Uniqueness STRICTLY requires convexity! If set $C$ is non-convex (e.g., the surface of a sphere, or two disconnected islands), a point equidistant from both sides has multiple distinct closest projections.",
    "hint": "Where does the nearest legal point sit relative to the plane and the rest of the airspace?",
    "breakdown": [
      "<strong>$x-p$ = the vector from the nearest legal spot to the plane.</strong>",
      "<strong>$\\langle x-p,y-p\\rangle\\le0$ for every legal $y$:</strong> the angle at $p$ between that vector and any other legal point is obtuse or right.",
      "<strong>That is the entire characterisation of the projection:</strong> $p\\in C$ and the inequality hold iff $p=\\Pi_C(x)$."
    ]
  },
  {
    "id": 1302,
    "subject": "CMO",
    "topicId": "13_Projections_onto_Convex_Sets",
    "topicTitle": "13 \u00b7 Projections onto Convex Sets",
    "cardNumber": "02",
    "category": "OPERATOR THEORY",
    "highlighterClass": "highlight-amber",
    "title": "Firm Non-Expansiveness of the Projection Operator",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1302\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"14\" y1=\"124\" x2=\"226\" y2=\"62\" stroke=\"#000000\" stroke-width=\"2.6\"/><line x1=\"14.0\" y1=\"124.0\" x2=\"226.0\" y2=\"62.0\" stroke=\"#000000\" stroke-width=\"0.1\"/><line x1=\"21.6\" y1=\"121.8\" x2=\"23.3\" y2=\"127.5\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"36.7\" y1=\"117.4\" x2=\"38.4\" y2=\"123.1\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"51.9\" y1=\"112.9\" x2=\"53.5\" y2=\"118.7\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"67.0\" y1=\"108.5\" x2=\"68.7\" y2=\"114.3\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"82.1\" y1=\"104.1\" x2=\"83.8\" y2=\"109.8\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"97.3\" y1=\"99.6\" x2=\"99.0\" y2=\"105.4\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"112.4\" y1=\"95.2\" x2=\"114.1\" y2=\"101.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"127.6\" y1=\"90.8\" x2=\"129.3\" y2=\"96.5\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"142.7\" y1=\"86.4\" x2=\"144.4\" y2=\"92.1\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"157.9\" y1=\"81.9\" x2=\"159.5\" y2=\"87.7\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"173.0\" y1=\"77.5\" x2=\"174.7\" y2=\"83.3\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"188.1\" y1=\"73.1\" x2=\"189.8\" y2=\"78.8\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"203.3\" y1=\"68.6\" x2=\"205.0\" y2=\"74.4\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"218.4\" y1=\"64.2\" x2=\"220.1\" y2=\"70.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><g transform=\"translate(60.0 35.0) rotate(20) scale(0.7)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.71\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><g transform=\"translate(175.0 50.0) rotate(20) scale(0.7)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.71\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><line x1=\"60.0\" y1=\"35.0\" x2=\"80.0\" y2=\"102.0\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"4 3\"/><line x1=\"175.0\" y1=\"50.0\" x2=\"181.0\" y2=\"72.0\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"4 3\"/><circle cx=\"80.0\" cy=\"102.0\" r=\"2.5\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"80\" y=\"118\" font-size=\"8.5\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">P(p)</text><circle cx=\"181.0\" cy=\"72.0\" r=\"2.5\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"189\" y=\"86\" font-size=\"8.5\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">P(q)</text><line x1=\"60\" y1=\"21\" x2=\"175\" y2=\"36\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"2 2\"/><text x=\"118\" y=\"28\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u2016p\u2212q\u2016</text><text x=\"122\" y=\"140\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u2016P(p)\u2212P(q)\u2016 \u2264 \u2016p\u2212q\u2016</text></svg>",
    "drawingCaption": "Two off-course planes are each guided to the nearest legal spot on the wall: their landing spots are never farther apart than the planes were.",
    "coreTranslation": [
      "<strong>What:</strong> projecting two points onto a convex set never moves them farther apart: $\\|\\Pi_C(x)-\\Pi_C(y)\\|\\le\\|x-y\\|$ (the projection is 1-Lipschitz, or <em>non-expansive</em>).",
      "<strong>How:</strong> it is even <em>firmly</em> non-expansive: $\\|\\Pi_C(x)-\\Pi_C(y)\\|^2\\le\\langle\\Pi_C(x)-\\Pi_C(y),\\ x-y\\rangle$, which follows by adding the two variational inequalities for $x$ and $y$.",
      "<strong>Why it matters:</strong> projections can never blow errors up, which is why projected gradient and alternating projections are stable. But it is not a strict contraction: points already inside $C$ keep their distance."
    ],
    "math": "$$\\|\\Pi_C(x) - \\Pi_C(y)\\|^2 + \\|(I - \\Pi_C)(x) - (I - \\Pi_C)(y)\\|^2 \\le \\|x - y\\|^2 \\implies \\|\\Pi_C(x) - \\Pi_C(y)\\| \\le \\|x - y\\|$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Two off-course planes are each guided by ATC to their nearest legal spot. The two landing spots are never farther apart than the two planes were: projection never stretches distances, it can only squeeze them together.",
    "examTrap": "Non-expansiveness does NOT mean strictly contractive! If $x, y \\in C$, then $\\Pi_C(x) = x$ and $\\Pi_C(y) = y$, so $\\|\\Pi_C(x) - \\Pi_C(y)\\| = \\|x - y\\|$ with equality. You cannot invoke Banach fixed point directly without relaxation.",
    "hint": "Why can a projection never pull two planes farther apart?",
    "breakdown": [
      "<strong>$\\|\\Pi x-\\Pi y\\|^2+\\|(I-\\Pi)x-(I-\\Pi)y\\|^2\\le\\|x-y\\|^2$:</strong> the along-the-wall and across-the-wall parts together are at most the original distance squared.",
      "<strong>Dropping the second (non-negative) term</strong> gives $\\|\\Pi x-\\Pi y\\|\\le\\|x-y\\|$.",
      "<strong>That is what makes projected methods stable:</strong> the correction never amplifies errors."
    ]
  },
  {
    "id": 1303,
    "subject": "CMO",
    "topicId": "13_Projections_onto_Convex_Sets",
    "topicTitle": "13 \u00b7 Projections onto Convex Sets",
    "cardNumber": "03",
    "category": "STANDARD FORMULAS",
    "highlighterClass": "highlight-emerald",
    "title": "Projection onto a Hyperplane and a Halfspace",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1303\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"24\" y1=\"118\" x2=\"214\" y2=\"46\" stroke=\"#000000\" stroke-width=\"2.6\"/><line x1=\"24.0\" y1=\"118.0\" x2=\"214.0\" y2=\"46.0\" stroke=\"#000000\" stroke-width=\"0.1\"/><line x1=\"30.8\" y1=\"115.4\" x2=\"32.9\" y2=\"121.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"44.4\" y1=\"110.3\" x2=\"46.5\" y2=\"115.9\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"57.9\" y1=\"105.1\" x2=\"60.1\" y2=\"110.7\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"71.5\" y1=\"100.0\" x2=\"73.7\" y2=\"105.6\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"85.1\" y1=\"94.9\" x2=\"87.2\" y2=\"100.4\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"98.6\" y1=\"89.7\" x2=\"100.8\" y2=\"95.3\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"112.2\" y1=\"84.6\" x2=\"114.4\" y2=\"90.2\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"125.8\" y1=\"79.4\" x2=\"127.9\" y2=\"85.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"139.4\" y1=\"74.3\" x2=\"141.5\" y2=\"79.9\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"152.9\" y1=\"69.1\" x2=\"155.1\" y2=\"74.7\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"166.5\" y1=\"64.0\" x2=\"168.7\" y2=\"69.6\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"180.1\" y1=\"58.9\" x2=\"182.2\" y2=\"64.4\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"193.6\" y1=\"53.7\" x2=\"195.8\" y2=\"59.3\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"207.2\" y1=\"48.6\" x2=\"209.4\" y2=\"54.2\" stroke=\"#000000\" stroke-width=\"1.1\"/><g transform=\"translate(130.0 22.0) rotate(20) scale(0.75)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.60\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><line x1=\"130.0\" y1=\"28.0\" x2=\"147.0\" y2=\"69.0\" stroke=\"#000000\" stroke-width=\"1.4\" stroke-dasharray=\"4 3\"/><circle cx=\"147.0\" cy=\"69.0\" r=\"2.5\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"155\" y=\"83\" font-size=\"8.5\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">P(p)</text><text x=\"115.36\" y=\"14\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">outside \u2192 dropped on the wall</text><g transform=\"translate(70.0 96.0) rotate(20) scale(0.75)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.60\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"70\" y=\"128\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">already legal: stays</text></svg>",
    "drawingCaption": "Half-space of legal altitudes: a plane outside is dropped straight along the wall's normal; a plane already on the legal side stays put.",
    "coreTranslation": [
      "<strong>What:</strong> the hyperplane $\\{x:a^Tx=b\\}$ and the halfspace $\\{x:a^Tx\\le b\\}$ have one-line closed-form projections.",
      "<strong>How (hyperplane):</strong> subtract the part of $x$ that sticks out along the normal: $\\Pi(x)=x-\\frac{a^Tx-b}{\\|a\\|^2}\\,a$. <strong>(Halfspace):</strong> do the same, but only if $a^Tx>b$; otherwise $x$ is already feasible: $\\Pi(x)=x-\\frac{\\max(0,\\,a^Tx-b)}{\\|a\\|^2}\\,a$.",
      "<strong>Why it matters:</strong> these two formulas are the building blocks for projecting onto polyhedra (e.g. by Dykstra) and for constraint-by-constraint methods. Example: $x=(3,1)$, $a=(1,1)$, $b=2$ gives $\\Pi=(3,1)-\\tfrac{4-2}{2}(1,1)=(2,0)$."
    ],
    "math": "$$\\Pi_{\\{a^Tx=b\\}}(x)=x-\\frac{a^Tx-b}{\\|a\\|^2}a,\\qquad \\Pi_{\\{a^Tx\\le b\\}}(x)=x-\\frac{\\max(0,\\,a^Tx-b)}{\\|a\\|^2}a$$",
    "personalConnection": "<strong>The airplane analogy.</strong> ATC dropping you onto a flat ceiling plane (hyperplane) sends you straight along its normal. For a half-space of legal altitudes: if you are already on the allowed side you stay put, otherwise you are dropped along the normal onto the wall.",
    "examTrap": "For the halfspace use max(0, a\u1d40x \u2212 b): a feasible point must NOT move. Applying the hyperplane formula to a halfspace wrongly drags inside points onto the boundary.",
    "hint": "How do you drop a plane onto a wall along its normal?",
    "breakdown": [
      "<strong>$a^\\top x-b$ = how far past the wall the plane is,</strong> measured along the normal direction (in units of $\\|a\\|$).",
      "<strong>Dividing by $\\|a\\|^2$ and multiplying by $a$</strong> turns that signed excess into the displacement back along the normal.",
      "<strong>The half-space version has $\\max(0,\\cdot)$:</strong> if you are already on the legal side, the excess is 0 and you stay put."
    ]
  },
  {
    "id": 1307,
    "subject": "CMO",
    "topicId": "13_Projections_onto_Convex_Sets",
    "topicTitle": "13 \u00b7 Projections onto Convex Sets",
    "cardNumber": "04",
    "category": "CLOSED-FORM PROJECTIONS",
    "highlighterClass": "highlight-emerald",
    "title": "Projection onto a Box and a Ball",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1307\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"120\" y1=\"8\" x2=\"120\" y2=\"138\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"3 3\"/><rect x=\"22\" y=\"52\" width=\"74\" height=\"60\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"2\"/><g transform=\"translate(116.0 24.0) rotate(130) scale(0.7)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.71\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><line x1=\"110.0\" y1=\"30.0\" x2=\"99.0\" y2=\"49.0\" stroke=\"#000000\" stroke-width=\"1.4\" stroke-dasharray=\"2 2\" marker-end=\"url(#arr-1307)\"/><circle cx=\"96.0\" cy=\"52.0\" r=\"2.5\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"100\" y=\"48\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">P</text><text x=\"60\" y=\"128\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">clamp each coordinate</text><text x=\"60\" y=\"140\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">to its own limits</text><circle cx=\"178.0\" cy=\"75.0\" r=\"32.0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"2\"/><g transform=\"translate(226.0 30.0) rotate(135) scale(0.7)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.71\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><line x1=\"222.0\" y1=\"34.0\" x2=\"202.0\" y2=\"53.0\" stroke=\"#000000\" stroke-width=\"1.4\" stroke-dasharray=\"4 3\"/><circle cx=\"201.0\" cy=\"52.0\" r=\"2.5\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"205\" y=\"66\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">P</text><text x=\"178\" y=\"128\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">scale back to the radius</text><text x=\"178\" y=\"140\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">if outside the ball</text></svg>",
    "drawingCaption": "Left: a box is clamped coordinate by coordinate. Right: a ball is the holding circle around the airport, so you steer to the centre until you reach its edge.",
    "coreTranslation": [
      "<strong>What:</strong> boxes (including the non-negative orthant) and Euclidean balls also have simple closed-form projections.",
      "<strong>How (box $[l,u]$):</strong> project each coordinate separately: $[\\Pi(x)]_i=\\min(u_i,\\max(l_i,x_i))$. For $\\mathbb{R}^n_+$ this is $\\max(0,x_i)$, the ReLU. <strong>(Ball $\\|x\\|\\le R$):</strong> keep $x$ if it is inside, otherwise scale it to length $R$: $\\Pi(x)=x\\cdot\\min(1,R/\\|x\\|)$.",
      "<strong>Why it matters:</strong> these cost only $O(n)$, which is why projected gradient is so cheap for bound constraints. Not every set is this easy: the simplex needs a sort (see the worked benchmark)."
    ],
    "math": "$$[\\Pi_{[l,u]}(x)]_i=\\min\\big(u_i,\\max(l_i,x_i)\\big),\\qquad \\Pi_{\\mathcal B(0,R)}(x)=\\frac{x}{\\max(1,\\ \\|x\\|/R)}$$",
    "personalConnection": "<strong>The airplane analogy.</strong> A box is a corridor with an altitude floor and ceiling and lane limits: ATC clamps each coordinate independently. A ball is a circular holding zone around the airport: if you are outside, steer straight at the centre until you touch the circle's edge, otherwise stay.",
    "examTrap": "Clamping works coordinate by coordinate only for BOXES (the constraints separate). It is wrong for the ball and for the simplex, where you cannot treat coordinates independently.",
    "hint": "What do the box and the ball do to a plane that is outside?",
    "breakdown": [
      "<strong>Box:</strong> $\\min(u_i,\\max(l_i,x_i))$ clamps each coordinate to its own limits independently.",
      "<strong>Ball:</strong> $x/\\max(1,\\|x\\|/R)$ leaves you alone inside the ball and scales you back along the ray to the centre once outside.",
      "<strong>Both are one-line projections:</strong> cheap to compute, which is why projected gradient uses them."
    ]
  },
  {
    "id": 1304,
    "subject": "CMO",
    "topicId": "13_Projections_onto_Convex_Sets",
    "topicTitle": "13 \u00b7 Projections onto Convex Sets",
    "cardNumber": "05",
    "category": "CONE DECOMPOSITION",
    "highlighterClass": "highlight-violet",
    "title": "Moreau\u2019s Decomposition Theorem",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1304\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><path d=\"M128.0,106.0 L191.0,94.9 L189.8,89.4 L188.1,84.1 L186.0,79.0 L183.4,74.0 L180.4,69.3 L177.0,64.9 L173.3,60.7 L169.1,57.0 L164.7,53.6 L160.0,50.6 L155.0,48.0 L149.9,45.9\" fill=\"#c9ced8\" stroke=\"#000000\" stroke-width=\"2\"/><path d=\"M128.0,106.0 L79.1,88.2 L76.8,97.0 L76.0,106.0 L76.8,115.0 L79.1,123.8 L83.0,132.0 L88.2,139.4 L94.6,145.8 L102.0,151.0 L110.2,154.9 L119.0,157.2 L128.0,158.0 L137.0,157.2\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"4 3\"/><line x1=\"128.0\" y1=\"106.0\" x2=\"88.0\" y2=\"36.7\" stroke=\"#000000\" stroke-width=\"2.6\" marker-end=\"url(#arr-1304)\"/><text x=\"84\" y=\"32\" font-size=\"11\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"end\" fill=\"#000000\">x</text><line x1=\"128.0\" y1=\"106.0\" x2=\"145.6\" y2=\"57.7\" stroke=\"#000000\" stroke-width=\"2.2\" marker-end=\"url(#arr-1304)\"/><text x=\"152\" y=\"52\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">P_K(x)</text><line x1=\"128.0\" y1=\"106.0\" x2=\"70.4\" y2=\"85.0\" stroke=\"#000000\" stroke-width=\"2.2\" marker-end=\"url(#arr-1304)\"/><text x=\"68\" y=\"78\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"end\" fill=\"#000000\">P_K\u00b0(x)</text><line x1=\"88.0\" y1=\"36.7\" x2=\"145.6\" y2=\"57.7\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"2 3\"/><line x1=\"88.0\" y1=\"36.7\" x2=\"70.4\" y2=\"85.0\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"2 3\"/><g transform=\"translate(128.0 106.0) rotate(-40) scale(0.6)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.00\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"108\" y=\"134\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">x = P_K(x) + P_K\u00b0(x),  \u27c2</text><text x=\"166\" y=\"96\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">K</text><text x=\"90\" y=\"112\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">K\u00b0</text></svg>",
    "drawingCaption": "Any wind vector x splits into a part along the legal cone K and a part in its polar cone K\u00b0, and the two parts are perpendicular.",
    "coreTranslation": [
      "<strong>What:</strong> for a closed convex cone $K$ and its polar cone $K^\\circ$, every vector splits uniquely into $x=\\Pi_K(x)+\\Pi_{K^\\circ}(x)$ with the two pieces perpendicular.",
      "<strong>How:</strong> the polar cone $K^\\circ=\\{y:\\langle y,x\\rangle\\le0\\ \\forall x\\in K\\}$ is the set of vectors at an obtuse (or right) angle to everything in $K$. The pieces satisfy $\\langle\\Pi_K(x),\\Pi_{K^\\circ}(x)\\rangle=0$.",
      "<strong>Why it matters:</strong> it generalizes the split of $\\mathbb{R}^n$ into a subspace plus its orthogonal complement to cones. In 1-D it is just $x=\\max(0,x)+\\min(0,x)$."
    ],
    "math": "$$x = x_1 + x_2, \\quad x_1 \\in K, \\; x_2 \\in K^\\circ, \\quad \\langle x_1, x_2 \\rangle = 0 \\iff x_1 = \\Pi_K(x), \\; x_2 = \\Pi_{K^\\circ}(x)$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Any wind vector splits into a part pointing inside the legal cone ($K$) and a part pointing out of it (the polar cone $K^\\circ$), and the two parts are perpendicular. One way of resolving wind into 'with the airspace' and 'against the wall' is the Moreau decomposition, like $x=x_++x_-$ in one dimension.",
    "examTrap": "Moreau's decomposition holds ONLY for CONES (sets closed under positive scaling $\\alpha K \\subseteq K$ for $\\alpha \\ge 0$). It does NOT hold for arbitrary bounded convex sets like boxes or balls!",
    "hint": "How does Moreau split any wind vector into 'with the airspace' and 'against the wall'?",
    "breakdown": [
      "<strong>$x_1=\\Pi_K(x)\\in K$:</strong> the part that points into the legal cone.",
      "<strong>$x_2=\\Pi_{K^\\circ}(x)\\in K^\\circ$:</strong> the part that points out of it.",
      "<strong>$\\langle x_1,x_2\\rangle=0$:</strong> the two parts are perpendicular; in 1D this is $x=x_++x_-$."
    ]
  },
  {
    "id": 1305,
    "subject": "CMO",
    "topicId": "13_Projections_onto_Convex_Sets",
    "topicTitle": "13 \u00b7 Projections onto Convex Sets",
    "cardNumber": "06",
    "category": "CONVEX ALGORITHMS",
    "highlighterClass": "highlight-indigo",
    "title": "Dykstra\u2019s Alternating Projection Algorithm",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1305\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><path d=\"M140.0,75.0 L234.0,128.0 L234.0,22.0\" fill=\"#d9dee7\" stroke=\"#000000\" stroke-width=\"1.6\"/><line x1=\"52\" y1=\"28\" x2=\"226\" y2=\"128\" stroke=\"#000000\" stroke-width=\"1.2\"/><line x1=\"52\" y1=\"122\" x2=\"226\" y2=\"22\" stroke=\"#000000\" stroke-width=\"1.2\"/><text x=\"34\" y=\"20\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">C\u2081</text><text x=\"34\" y=\"138\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">C\u2082</text><g transform=\"translate(40.0 76.0) rotate(0) scale(0.8)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.50\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><path d=\"M40.0,76.0 L96.0,108.0 L130.0,90.0 L160.0,106.0 L176.0,98.0 L190.0,105.0\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.3\" stroke-dasharray=\"3 2\"/><circle cx=\"190.0\" cy=\"105.0\" r=\"2.5\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"190\" y=\"120\" font-size=\"8\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">plain: some point</text><circle cx=\"140.0\" cy=\"75.0\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"140\" y=\"67\" font-size=\"8.5\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Dykstra: apex</text><path d=\"M40.0,76.0 L140.0,75.0\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.4\"/></svg>",
    "drawingCaption": "Two overlapping airspaces C\u2081, C\u2082. Plain alternating projections zig-zag and stop at some point of the overlap; Dykstra's memory sends the plane straight to the nearest point (the apex).",
    "coreTranslation": [
      "<strong>The Challenge:</strong> Projecting onto the intersection $C_1 \\cap C_2$ when individual projections $\\Pi_{C_1}$ and $\\Pi_{C_2}$ are easy, but $\\Pi_{C_1 \\cap C_2}$ has no closed form.",
      "<strong>Von Neumann vs. Dykstra:</strong> Simple alternating projection $\\dots \\Pi_2(\\Pi_1(\\Pi_2(x))) \\dots$ finds AN arbitrary point in $C_1 \\cap C_2$, but NOT the closest projection $\\Pi_{C_1 \\cap C_2}(x)$!",
      "<strong>Dykstra's Innovation:</strong> Subtracts the outward normal correction vector before projecting at each step: $y_k = \\Pi_{C_1}(x_k + p_k)$, $p_{k+1} = x_k + p_k - y_k$, guaranteed to converge to the exact minimum Euclidean distance point."
    ],
    "math": "$$y_k = \\Pi_{C_1}(x_k + p_{k-1}), \\; p_k = x_k + p_{k-1} - y_k, \\quad x_{k+1} = \\Pi_{C_2}(y_k + q_{k-1}), \\; q_k = y_k + q_{k-1} - x_{k+1}$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Two overlapping airspaces. Plain alternating ATC projections drift along the crease and end at some point in the overlap, not the nearest one. Dykstra's algorithm remembers the sideways correction from each bounce, so the plane lands on the closest point of the overlap.",
    "examTrap": "Exam questions love to ask: 'Does alternating projection find $\\Pi_{C_1 \\cap C_2}(x)$?' Answer: ONLY if $C_1, C_2$ are linear affine subspaces! For general convex sets, you MUST use Dykstra's normal correction.",
    "hint": "What does Dykstra's memory do that plain alternating projection does not?",
    "breakdown": [
      "<strong>$y_k=\\Pi_{C_1}(x_k+p_{k-1})$:</strong> project onto the first airspace, but first add back the correction remembered from last time.",
      "<strong>$p_k=x_k+p_{k-1}-y_k$:</strong> remember what this projection moved you sideways by.",
      "<strong>Without these memory vectors you end at some point of the overlap;</strong> with them you end at the nearest point of the overlap."
    ]
  },
  {
    "id": 1306,
    "subject": "CMO",
    "topicId": "13_Projections_onto_Convex_Sets",
    "topicTitle": "13 \u00b7 Projections onto Convex Sets",
    "cardNumber": "07",
    "category": "WORKED BENCHMARK",
    "highlighterClass": "highlight-rose",
    "title": "Worked Benchmark: Projecting onto the Simplex",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1306\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"30\" y=\"32\" width=\"24\" height=\"90\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.5\"/><rect x=\"30\" y=\"32\" width=\"24\" height=\"45\" rx=\"0\" fill=\"#c9ced8\" stroke=\"#000000\" stroke-width=\"1.5\"/><rect x=\"62\" y=\"62\" width=\"24\" height=\"60\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.5\"/><rect x=\"62\" y=\"62\" width=\"24\" height=\"15\" rx=\"0\" fill=\"#c9ced8\" stroke=\"#000000\" stroke-width=\"1.5\"/><rect x=\"94\" y=\"92\" width=\"24\" height=\"30\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.5\"/><rect x=\"126\" y=\"110\" width=\"24\" height=\"12\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.5\"/><line x1=\"20\" y1=\"77\" x2=\"158\" y2=\"77\" stroke=\"#000000\" stroke-width=\"1.6\" stroke-dasharray=\"5 3\"/><text x=\"20\" y=\"72\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">\u03c4 = 0.75</text><line x1=\"14\" y1=\"122\" x2=\"158\" y2=\"122\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"74\" y=\"136\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">tanks (x)</text><g transform=\"translate(206.0 40.0) rotate(0) scale(0.9)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.33\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"198.43\" y=\"66\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">fuel budget \u03a3 = 1</text><text x=\"202.72\" y=\"84\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">keep what sticks</text><text x=\"202.72\" y=\"96\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">above the level:</text><text x=\"198.1648\" y=\"112\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">p = (.75,.25,0,0)</text></svg>",
    "drawingCaption": "Fuel tanks with readings x. Shave one common level \u03c4 off every tank, clip at empty, and choose \u03c4 so the leftover fuel sums to exactly 1.",
    "coreTranslation": [
      "<strong>Problem:</strong> project $x=(1.5,\\,1.0,\\,0.2,\\,-0.3)$ onto the simplex $\\{p\\ge0,\\ \\sum p_i=1\\}$. The answer has the form $p_i=\\max(0,\\,x_i-\\tau)$ for a single threshold $\\tau$ with $\\sum p_i=1$.",
      "<strong>Find $\\tau$:</strong> sort descending ($1.5,1.0,0.2,-0.3$). For $k$ active coordinates try $\\tau_k=\\frac{(\\text{sum of top }k)-1}{k}$: $\\tau_1=0.5$, $\\tau_2=\\frac{2.5-1}{2}=0.75$, $\\tau_3=\\frac{2.7-1}{3}\\approx0.57$. Keep the largest $k$ with $x_{(k)}>\\tau_k$: $1.0>0.75$ \u2713 but $0.2>0.57$ \u2717, so $k=2$, $\\tau=0.75$.",
      "<strong>Result:</strong> $p=(1.5-0.75,\\ 1.0-0.75,\\ 0,\\ 0)=(0.75,\\ 0.25,\\ 0,\\ 0)$. Check: $p\\ge0$ and $\\sum p=1$ \u2713."
    ],
    "math": "$$\\Pi_\\Delta(x)=\\max(0,\\,x-\\tau\\mathbf 1),\\quad \\tau=\\frac{\\sum_{i\\le k}x_{(i)}-1}{k}=\\frac{2.5-1}{2}=0.75\\ \\Rightarrow\\ p=(0.75,\\,0.25,\\,0,\\,0)$$",
    "personalConnection": "<strong>The airplane analogy.</strong> A fixed fuel budget (total exactly 1) shared among tanks. Shave one common level $\\tau$ off every tank reading, clipping at empty: the tanks that stay above the level keep their excess, the rest go dry, and $\\tau$ is chosen so the leftover fuel sums to 1. That is the simplex projection.",
    "examTrap": "Do not just clip negatives and divide by the sum: that gives (1.5, 1.0, 0.2, 0)/2.7 = (0.56, 0.37, 0.07, 0), which is NOT the Euclidean projection. The threshold \u03c4 must be subtracted first. Sorting makes it O(n log n); a median-finding method gets O(n).",
    "hint": "How do you find the water level $\\tau$ that makes the leftover fuel sum to one?",
    "breakdown": [
      "<strong>$x-\\tau\\mathbf1$ shaves the same level off every tank;</strong> $\\max(0,\\cdot)$ lets empty tanks stay empty.",
      "<strong>$\\tau=\\frac{\\sum_{i\\le k}x_{(i)}-1}{k}$:</strong> the extra over 1 in the $k$ largest tanks, shared equally ($\\frac{2.5-1}{2}=0.75$).",
      "<strong>Result $(0.75,0.25,0,0)$ sums to 1 and is the nearest point of the simplex.</strong>"
    ]
  },
  {
    "id": 1401,
    "subject": "CMO",
    "topicId": "14_Gradient_Projection_Algorithm_and_Convergence",
    "topicTitle": "14 \u00b7 Gradient Projection Algorithm",
    "cardNumber": "01",
    "category": "CONSTRAINED DESCENT",
    "highlighterClass": "highlight-cyan",
    "title": "The Projected Gradient Iteration",
    "textbookImg": "assets/luenberger_fig12_4.png",
    "textbookRef": "Luenberger & Ye (4th ed), Sect. 12.4, Fig. 12.4 (p. 384)",
    "drawingCaption": "A gravity step would carry the plane into the mountain; air-traffic control projects it straight back to the nearest legal point on the wall.",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1401\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"150\" y=\"8\" width=\"80\" height=\"130\" rx=\"0\" fill=\"#d1d5db\" stroke=\"#000000\" stroke-width=\"0\"/><line x1=\"150.0\" y1=\"8.0\" x2=\"150.0\" y2=\"138.0\" stroke=\"#000000\" stroke-width=\"2.4\"/><line x1=\"150.0\" y1=\"12.6\" x2=\"157.0\" y2=\"12.6\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"150.0\" y1=\"21.9\" x2=\"157.0\" y2=\"21.9\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"150.0\" y1=\"31.2\" x2=\"157.0\" y2=\"31.2\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"150.0\" y1=\"40.5\" x2=\"157.0\" y2=\"40.5\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"150.0\" y1=\"49.8\" x2=\"157.0\" y2=\"49.8\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"150.0\" y1=\"59.1\" x2=\"157.0\" y2=\"59.1\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"150.0\" y1=\"68.4\" x2=\"157.0\" y2=\"68.4\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"150.0\" y1=\"77.6\" x2=\"157.0\" y2=\"77.6\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"150.0\" y1=\"86.9\" x2=\"157.0\" y2=\"86.9\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"150.0\" y1=\"96.2\" x2=\"157.0\" y2=\"96.2\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"150.0\" y1=\"105.5\" x2=\"157.0\" y2=\"105.5\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"150.0\" y1=\"114.8\" x2=\"157.0\" y2=\"114.8\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"150.0\" y1=\"124.1\" x2=\"157.0\" y2=\"124.1\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"150.0\" y1=\"133.4\" x2=\"157.0\" y2=\"133.4\" stroke=\"#000000\" stroke-width=\"1.1\"/><text x=\"206\" y=\"28\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">rock</text><g transform=\"translate(96.0 38.0) rotate(20) scale(0.85)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.41\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><circle cx=\"96.0\" cy=\"38.0\" r=\"2.5\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"94\" y=\"26\" font-size=\"9.5\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"end\" fill=\"#000000\">x\u2096</text><line x1=\"98.0\" y1=\"40.0\" x2=\"186.0\" y2=\"70.0\" stroke=\"#000000\" stroke-width=\"1.8\" stroke-dasharray=\"4 3\" marker-end=\"url(#arr-1401)\"/><circle cx=\"186.0\" cy=\"70.0\" r=\"2.2\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"186\" y=\"94\" font-size=\"8.5\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"end\" fill=\"#000000\">x\u2096\u2212\u03b1\u2207f</text><line x1=\"184.0\" y1=\"71.0\" x2=\"154.0\" y2=\"71.0\" stroke=\"#000000\" stroke-width=\"2.8\" marker-end=\"url(#arr-1401)\"/><circle cx=\"150.0\" cy=\"71.0\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"146\" y=\"87\" font-size=\"9.5\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"end\" fill=\"#000000\">x\u2096\u208a\u2081</text><text x=\"83.04\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">slide along the wall, never through it</text></svg>",
    "coreTranslation": [
      "<strong>What:</strong> projected gradient minimizes $f$ over a closed convex set $\\Omega$ by taking an ordinary gradient step and then snapping back onto $\\Omega$: $x_{k+1}=\\Pi_\\Omega\\big(x_k-\\alpha_k\\nabla f(x_k)\\big)$.",
      "<strong>How:</strong> equivalently, $x_{k+1}$ minimizes the local model $\\nabla f(x_k)^T(y-x_k)+\\tfrac1{2\\alpha_k}\\|y-x_k\\|^2$ over $y\\in\\Omega$. When $\\Omega$ is simple (a box, a ball) the projection is a cheap formula.",
      "<strong>Why it matters:</strong> it is as easy as gradient descent but never leaves the feasible set. On curved constraint surfaces Luenberger splits it into a tangent step followed by a restoration step back onto the surface."
    ],
    "math": "$$x_{k+1} = \\Pi_\\Omega(x_k - \\alpha_k \\nabla f(x_k)) = \\arg\\min_{y \\in \\Omega} \\left\\{ \\nabla f(x_k)^T (y - x_k) + \\frac{1}{2\\alpha_k} \\|y - x_k\\|^2 \\right\\}$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Follow gravity downhill one step. If that carries you out of legal airspace into the mountain, ATC immediately projects you back to the nearest legal point: you slide along the wall instead of crashing through it.",
    "examTrap": "Step size $\\alpha_k$ must satisfy $\\alpha_k < 2/L$ (where $L$ is the Lipschitz constant of $\\nabla f$)! If $\\alpha_k$ is too large, projecting back can cause iterates to bounce back and forth indefinitely across the boundary.",
    "hint": "What does the pilot do when a gravity step would carry him into the mountain?",
    "breakdown": [
      "<strong>$x_k-\\alpha_k\\nabla f(x_k)$ = the plain downhill step</strong> (nose along $-\\nabla f$, flight distance $\\alpha_k$).",
      "<strong>$\\Pi_\\Omega$ = air-traffic control:</strong> if the step lands outside the airspace, it puts you on the nearest legal point.",
      "<strong>Equivalent form:</strong> $\\arg\\min_{y\\in\\Omega}\\{\\nabla f^\\top(y-x_k)+\\frac1{2\\alpha_k}\\|y-x_k\\|^2\\}$ = the best legal point under a linear slope plus a leash of strength $\\frac1{\\alpha_k}$."
    ]
  },
  {
    "id": 1402,
    "subject": "CMO",
    "topicId": "14_Gradient_Projection_Algorithm_and_Convergence",
    "topicTitle": "14 \u00b7 Gradient Projection Algorithm",
    "cardNumber": "02",
    "category": "STATIONARITY CRITERIA",
    "highlighterClass": "highlight-amber",
    "title": "Fixed-Point Characterization of Optimality",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1402\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"150\" y=\"8\" width=\"80\" height=\"130\" rx=\"0\" fill=\"#d1d5db\" stroke=\"#000000\" stroke-width=\"0\"/><line x1=\"150.0\" y1=\"8.0\" x2=\"150.0\" y2=\"138.0\" stroke=\"#000000\" stroke-width=\"2.4\"/><line x1=\"150.0\" y1=\"12.6\" x2=\"157.0\" y2=\"12.6\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"150.0\" y1=\"21.9\" x2=\"157.0\" y2=\"21.9\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"150.0\" y1=\"31.2\" x2=\"157.0\" y2=\"31.2\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"150.0\" y1=\"40.5\" x2=\"157.0\" y2=\"40.5\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"150.0\" y1=\"49.8\" x2=\"157.0\" y2=\"49.8\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"150.0\" y1=\"59.1\" x2=\"157.0\" y2=\"59.1\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"150.0\" y1=\"68.4\" x2=\"157.0\" y2=\"68.4\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"150.0\" y1=\"77.6\" x2=\"157.0\" y2=\"77.6\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"150.0\" y1=\"86.9\" x2=\"157.0\" y2=\"86.9\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"150.0\" y1=\"96.2\" x2=\"157.0\" y2=\"96.2\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"150.0\" y1=\"105.5\" x2=\"157.0\" y2=\"105.5\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"150.0\" y1=\"114.8\" x2=\"157.0\" y2=\"114.8\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"150.0\" y1=\"124.1\" x2=\"157.0\" y2=\"124.1\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"150.0\" y1=\"133.4\" x2=\"157.0\" y2=\"133.4\" stroke=\"#000000\" stroke-width=\"1.1\"/><text x=\"192\" y=\"40\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">rock</text><g transform=\"translate(126.0 72.0) rotate(0) scale(0.9)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.33\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><circle cx=\"150.0\" cy=\"72.0\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"146\" y=\"90\" font-size=\"10\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"end\" fill=\"#000000\">x*</text><line x1=\"130.0\" y1=\"62.0\" x2=\"196.0\" y2=\"62.0\" stroke=\"#000000\" stroke-width=\"2\" stroke-dasharray=\"4 3\" marker-end=\"url(#arr-1402)\"/><text x=\"194\" y=\"56\" font-size=\"8.5\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"end\" fill=\"#000000\">x*\u2212\u03b1\u2207f</text><line x1=\"196.0\" y1=\"82.0\" x2=\"154.0\" y2=\"82.0\" stroke=\"#000000\" stroke-width=\"2.8\" marker-end=\"url(#arr-1402)\"/><text x=\"184\" y=\"98\" font-size=\"10\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">P</text><text x=\"86\" y=\"20\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">P(x* \u2212 \u03b1\u2207f(x*)) = x*</text><text x=\"86\" y=\"134\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">no net motion: a stationary spot</text></svg>",
    "drawingCaption": "At the optimum gravity shoves the plane into the wall with full force and the projection returns it to the same parked spot: a fixed point.",
    "coreTranslation": [
      "<strong>What:</strong> $x^*$ is a stationary point of $\\min_{x\\in\\Omega}f$ exactly when a gradient step followed by projection leaves it where it is: $x^*=\\Pi_\\Omega\\big(x^*-\\alpha\\nabla f(x^*)\\big)$ (for any $\\alpha>0$).",
      "<strong>How:</strong> define the gradient mapping $G_\\alpha(x)=\\frac1\\alpha\\big(x-\\Pi_\\Omega(x-\\alpha\\nabla f(x))\\big)$. Then $x^*$ is stationary iff $G_\\alpha(x^*)=0$, iff $-\\nabla f(x^*)$ points into the normal cone of $\\Omega$ at $x^*$.",
      "<strong>Why it matters:</strong> $\\|G_\\alpha(x_k)\\|\\le\\epsilon$ is the correct stopping test for constrained problems, because $\\nabla f$ itself does not vanish on the boundary."
    ],
    "math": "$$x^* \\text{ is stationary} \\iff G_\\alpha(x^*) = \\frac{x^* - \\Pi_\\Omega(x^* - \\alpha \\nabla f(x^*))}{\\alpha} = \\mathbf{0} \\iff -\\nabla f(x^*) \\in \\mathcal{N}_\\Omega(x^*)$$",
    "personalConnection": "<strong>The airplane analogy.</strong> At the optimum, gravity pushes the plane into the mountain wall with full force, but ATC projects you straight back to the same parking spot: $P(x^*-\\alpha\\nabla f(x^*))=x^*$. A point that does not move under one gradient-projection step is exactly a stationary parking spot.",
    "examTrap": "Remember that unconstrained stationarity ($\\nabla f(x^*) = 0$) DOES NOT HOLD on the boundary! The physical gradient $\\nabla f(x^*)$ can be massive; stationarity only requires that its negative points outward into the normal cone.",
    "hint": "What does a stationary parking spot look like to the projection operator?",
    "breakdown": [
      "<strong>$x^*-\\alpha\\nabla f(x^*)$:</strong> gravity shoves the plane into the wall.",
      "<strong>$\\Pi_\\Omega(\\cdot)$ puts it straight back on $x^*$,</strong> so $G_\\alpha(x^*)=0$: no net motion.",
      "<strong>Equivalent:</strong> $-\\nabla f(x^*)$ lies in the normal cone, i.e. points straight into the wall, so no legal direction goes downhill."
    ]
  },
  {
    "id": 1403,
    "subject": "CMO",
    "topicId": "14_Gradient_Projection_Algorithm_and_Convergence",
    "topicTitle": "14 \u00b7 Gradient Projection Algorithm",
    "cardNumber": "03",
    "category": "CONVERGENCE THEORY",
    "highlighterClass": "highlight-emerald",
    "title": "Convergence Rates: Sublinear to Linear",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1403\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"30\" y1=\"124\" x2=\"226\" y2=\"124\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-1403)\"/><line x1=\"30\" y1=\"124\" x2=\"30\" y2=\"10\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-1403)\"/><path d=\"M30.0,24.0 L38.0,37.0 L46.0,47.1 L54.0,55.0 L62.0,61.5 L70.0,66.9 L78.0,71.4 L86.0,75.2 L94.0,78.5 L102.0,81.4 L110.0,84.0 L118.0,86.3 L126.0,88.3 L134.0,90.1 L142.0,91.7 L150.0,93.2 L158.0,94.6 L166.0,95.8 L174.0,97.0 L182.0,98.0 L190.0,99.0 L198.0,99.9 L206.0,100.7 L214.0,101.5\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.4\" stroke-dasharray=\"5 3\"/><path d=\"M30.0,24.0 L38.0,39.0 L46.0,51.8 L54.0,62.6 L62.0,71.8 L70.0,79.6 L78.0,86.3 L86.0,91.9 L94.0,96.8 L102.0,100.8 L110.0,104.3 L118.0,107.3 L126.0,109.8 L134.0,111.9 L142.0,113.7 L150.0,115.3 L158.0,116.6 L166.0,117.7 L174.0,118.6 L182.0,119.4 L190.0,120.1 L198.0,120.7 L206.0,121.2 L214.0,121.6\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.4\"/><text x=\"190\" y=\"44\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"end\" fill=\"#000000\">O(1/k) merely convex</text><text x=\"176\" y=\"106\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"end\" fill=\"#000000\">\u03c1\u1d4f strongly convex</text><text x=\"18\" y=\"18\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">gap</text><text x=\"212\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"end\" fill=\"#000000\">k (legs flown)</text><g transform=\"translate(54.0 22.0) rotate(0) scale(0.6)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.00\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g></svg>",
    "drawingCaption": "Distance to the best parking spot versus legs flown: a merely convex valley closes in like 1/k, a strongly convex bowl shrinks by a fixed factor each leg. The walls do not change the rate.",
    "coreTranslation": [
      "<strong>Remarkable Theorem:</strong> The projected gradient algorithm inherits the <strong>exact same theoretical convergence rates</strong> as unconstrained gradient descent!",
      "<strong>Convex Objectives ($L$-Lipschitz gradient):</strong> With step size $\\alpha = 1/L$, the objective error decreases at a sublinear rate: $f(x_k) - f^* \\le \\frac{L \\|x_0 - x^*\\|^2}{2k} = \\mathcal{O}(1/k)$.",
      "<strong>Strongly Convex Objectives ($m$-strongly convex):</strong> With step size $\\alpha = 2/(L+m)$, the sequence converges with geometric linear rate: $\\|x_k - x^*\\| \\le \\left( \\frac{L-m}{L+m} \\right)^k \\|x_0 - x^*\\|$."
    ],
    "math": "$$f(x_k) - f^* \\le \\frac{L \\|x_0 - x^*\\|^2}{2k} \\; (\\text{Convex}), \\quad \\|x_k - x^*\\| \\le c \\cdot \\rho^k \\; (\\text{Strongly Convex, } \\rho < 1)$$",
    "personalConnection": "<strong>The airplane analogy.</strong> The glide path to the lowest legal parking spot. On a merely convex (smooth) valley the approach is sublinear, $O(1/k)$. In a strongly convex bowl each leg shrinks the remaining distance by a fixed factor (linear rate). The mountain walls do not slow the glide rate.",
    "examTrap": "Projection does NOT slow down asymptotic convergence rates! The only difference is the computational cost of evaluating $\\Pi_\\Omega(x)$ at each iteration.",
    "hint": "How fast does the pilot close in on the best parking spot?",
    "breakdown": [
      "<strong>Convex, smooth terrain:</strong> $\\frac{L\\|x_0-x^*\\|^2}{2k}$, the gap shrinks like $1/k$ (sublinear).",
      "<strong>Strongly convex terrain:</strong> $c\\rho^k$ with $\\rho\\lt1$, a fixed fraction of the distance removed each leg (linear).",
      "<strong>The walls do not change either rate:</strong> projection is non-expansive, so it never undoes progress."
    ]
  },
  {
    "id": 1404,
    "subject": "CMO",
    "topicId": "14_Gradient_Projection_Algorithm_and_Convergence",
    "topicTitle": "14 \u00b7 Gradient Projection Algorithm",
    "cardNumber": "04",
    "category": "LINE SEARCH",
    "highlighterClass": "highlight-violet",
    "title": "Armijo Line Search along the Projection Arc",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1404\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"8\" y=\"8\" width=\"72\" height=\"130\" rx=\"0\" fill=\"#d1d5db\" stroke=\"#000000\" stroke-width=\"0\"/><line x1=\"80.0\" y1=\"8.0\" x2=\"80.0\" y2=\"138.0\" stroke=\"#000000\" stroke-width=\"2.4\"/><line x1=\"80.0\" y1=\"12.6\" x2=\"73.0\" y2=\"12.6\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"80.0\" y1=\"21.9\" x2=\"73.0\" y2=\"21.9\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"80.0\" y1=\"31.2\" x2=\"73.0\" y2=\"31.2\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"80.0\" y1=\"40.5\" x2=\"73.0\" y2=\"40.5\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"80.0\" y1=\"49.8\" x2=\"73.0\" y2=\"49.8\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"80.0\" y1=\"59.1\" x2=\"73.0\" y2=\"59.1\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"80.0\" y1=\"68.4\" x2=\"73.0\" y2=\"68.4\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"80.0\" y1=\"77.6\" x2=\"73.0\" y2=\"77.6\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"80.0\" y1=\"86.9\" x2=\"73.0\" y2=\"86.9\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"80.0\" y1=\"96.2\" x2=\"73.0\" y2=\"96.2\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"80.0\" y1=\"105.5\" x2=\"73.0\" y2=\"105.5\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"80.0\" y1=\"114.8\" x2=\"73.0\" y2=\"114.8\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"80.0\" y1=\"124.1\" x2=\"73.0\" y2=\"124.1\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"80.0\" y1=\"133.4\" x2=\"73.0\" y2=\"133.4\" stroke=\"#000000\" stroke-width=\"1.1\"/><g transform=\"translate(170.0 30.0) rotate(20) scale(0.8)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.50\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><circle cx=\"170.0\" cy=\"30.0\" r=\"2.5\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"170\" y=\"18\" font-size=\"9.5\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">x\u2096</text><line x1=\"170.0\" y1=\"30.0\" x2=\"20.0\" y2=\"132.0\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"3 3\"/><text x=\"34\" y=\"128\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u2212\u03b1\u2207f</text><path d=\"M80.0,62.0 L80.0,112.0\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.4\" stroke-dasharray=\"2 2\"/><circle cx=\"80.0\" cy=\"66.0\" r=\"2.8\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"88\" y=\"69\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"start\" fill=\"#000000\">\u2713 accepted</text><circle cx=\"80.0\" cy=\"78.0\" r=\"2.8\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"88\" y=\"81\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">\u2717</text><circle cx=\"80.0\" cy=\"102.0\" r=\"2.8\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"88\" y=\"105\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">\u2717</text><text x=\"176\" y=\"108\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">trial points slide</text><text x=\"176\" y=\"120\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">along the wall (arc)</text><text x=\"176\" y=\"134\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">first big enough drop wins</text></svg>",
    "drawingCaption": "Shortening the step traces an arc along the mountain wall. Try points on that arc and accept the first one that gives a big enough altitude drop.",
    "coreTranslation": [
      "<strong>What:</strong> a straight ray $x_k-\\alpha\\nabla f(x_k)$ leaves $\\Omega$, so the line search must follow the bent path $x(\\alpha)=\\Pi_\\Omega\\big(x_k-\\alpha\\nabla f(x_k)\\big)$, the <em>projection arc</em>.",
      "<strong>How:</strong> backtrack $\\alpha=s,\\beta s,\\beta^2s,\\dots$ until the Armijo test along the arc holds: $f(x(\\alpha))\\le f(x_k)-\\tfrac\\sigma\\alpha\\|x_k-x(\\alpha)\\|^2$.",
      "<strong>Why it matters:</strong> the test measures progress with the displacement actually taken, $x_k-x(\\alpha)$, not with $-\\alpha\\nabla f$. The arc can bend along several faces of $\\Omega$, so many bound constraints can become active in one iteration."
    ],
    "math": "$$f(x(\\alpha)) \\le f(x_k) - \\frac{\\gamma}{\\alpha} \\|x_k - x(\\alpha)\\|^2 \\quad \\text{with } \\alpha \\in \\{\\beta^0 s, \\beta^1 s, \\beta^2 s, \\dots\\}$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Armijo along the arc: as you shorten the step $\\alpha$, the points $P(x_k-\\alpha\\nabla f)$ trace an arc that bends along the mountain wall. You try points on that arc and accept the first one that gives a big enough altitude drop, the sufficient-decrease check.",
    "examTrap": "Do NOT evaluate the Armijo gradient test against $-\\alpha \\nabla f(x_k)$! You must evaluate the reduction against the actual displacement vector $x_k - x(\\alpha)$, because that is the physical step taken.",
    "hint": "How does the pilot test a leg when the step slides along the wall?",
    "breakdown": [
      "<strong>$x(\\alpha)=\\Pi_\\Omega(x_k-\\alpha\\nabla f(x_k))$ traces an arc along the wall</strong> as $\\alpha$ changes.",
      "<strong>$\\frac\\gamma\\alpha\\|x_k-x(\\alpha)\\|^2$ is the promised drop:</strong> big for a long actual displacement, scaled by the leash $\\frac1\\alpha$.",
      "<strong>Try $\\alpha=s,\\beta s,\\beta^2s,\\dots$ and keep the first that earns it.</strong>"
    ]
  },
  {
    "id": 1405,
    "subject": "CMO",
    "topicId": "14_Gradient_Projection_Algorithm_and_Convergence",
    "topicTitle": "14 \u00b7 Gradient Projection Algorithm",
    "cardNumber": "05",
    "category": "MANIFOLD RESTORATION",
    "highlighterClass": "highlight-indigo",
    "title": "Restoration Phase for Non-Linear Manifolds",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1405\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><circle cx=\"112.0\" cy=\"84.0\" r=\"46.0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"2.2\"/><g transform=\"translate(112.0 38.0) rotate(0) scale(0.8)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.50\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><circle cx=\"112.0\" cy=\"38.0\" r=\"2.5\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"108\" y=\"29\" font-size=\"9.5\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"end\" fill=\"#000000\">x\u2096</text><line x1=\"126.0\" y1=\"36.0\" x2=\"165.0\" y2=\"36.0\" stroke=\"#000000\" stroke-width=\"2\" stroke-dasharray=\"4 3\" marker-end=\"url(#arr-1405)\"/><circle cx=\"168.0\" cy=\"36.0\" r=\"2.5\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"174\" y=\"34\" font-size=\"10\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">y</text><line x1=\"168.0\" y1=\"36.0\" x2=\"148.9\" y2=\"53.1\" stroke=\"#000000\" stroke-width=\"2.8\" marker-end=\"url(#arr-1405)\"/><circle cx=\"146.9\" cy=\"54.1\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"153.9\" y=\"64.1\" font-size=\"9.5\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">x\u2096\u208a\u2081</text><text x=\"108\" y=\"88\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">curved surface</text><text x=\"28.0\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">tangent step leaves it; drop back along the radius</text></svg>",
    "drawingCaption": "On a curved runway a straight tangent step floats off the surface (y); restoration descends along the normal to plant the wheels back on it.",
    "coreTranslation": [
      "<strong>What:</strong> on a curved constraint surface $h(x)=0$ a step along the tangent plane lands slightly off the surface, so each iteration is a <em>tangent step</em> followed by a <em>restoration step</em>.",
      "<strong>How:</strong> (1) tangent step $y=x_k-\\alpha P_k\\nabla f(x_k)$ with $P_k$ the projector onto the tangent plane; (2) restoration: Newton-correct $y$ back to feasibility along the normal: $x_{k+1}=y-\\nabla h\\,[\\nabla h^T\\nabla h]^{-1}h(y)$.",
      "<strong>Why it matters:</strong> this is how gradient projection extends from simple sets to nonlinear equality constraints. If $\\alpha$ is too large, $y$ is too far from the surface and restoration may fail or land on a different branch."
    ],
    "math": "$$y = x_k - \\alpha P_k \\nabla f(x_k), \\quad x_{k+1} = y - \\nabla h(x_k) [\\nabla h(x_k)^T \\nabla h(x_k)]^{-1} h(y) \\quad (\\text{Feasibility Restored})$$",
    "personalConnection": "<strong>The airplane analogy.</strong> On a curved boundary (a banked runway), flying straight ahead along the tangent takes you off the surface. Restoration is the fix: descend along the normal to put your wheels back on the curved surface before the next leg.",
    "examTrap": "If step size $\\alpha$ is chosen too large, the tangent point $y$ may fly so far from the manifold that the Newton restoration phase fails to converge (or converges to a completely different branch of the constraint surface)!",
    "hint": "How does the pilot get back onto a curved runway after a straight step?",
    "breakdown": [
      "<strong>$y=x_k-\\alpha P_k\\nabla f(x_k)$:</strong> project gravity onto the tangent plane so you slide along the wall (nose $P_k\\nabla f$).",
      "<strong>The straight step leaves the curved surface,</strong> so $h(y)\\ne0$ measures how far off you are.",
      "<strong>$-\\nabla h[\\nabla h^\\top\\nabla h]^{-1}h(y)$ = drop along the normal</strong> by exactly the amount needed to restore $h=0$."
    ]
  },
  {
    "id": 1406,
    "subject": "CMO",
    "topicId": "14_Gradient_Projection_Algorithm_and_Convergence",
    "topicTitle": "14 \u00b7 Gradient Projection Algorithm",
    "cardNumber": "06",
    "category": "WORKED BENCHMARK",
    "highlighterClass": "highlight-rose",
    "title": "Worked Benchmark: Projected GD on Non-Negative Orthant",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1406\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><polygon points=\"50,100 226,100 226,12 50,12\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"0.1\"/><line x1=\"50\" y1=\"100\" x2=\"226\" y2=\"100\" stroke=\"#000000\" stroke-width=\"2\" marker-end=\"url(#arr-1406)\"/><line x1=\"50\" y1=\"100\" x2=\"50\" y2=\"8\" stroke=\"#000000\" stroke-width=\"2\" marker-end=\"url(#arr-1406)\"/><text x=\"120\" y=\"26\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"start\" fill=\"#000000\">x \u2265 0 : legal</text><text x=\"236\" y=\"112\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"end\" fill=\"#000000\">ground x\u2082 = 0</text><g transform=\"translate(76.0 22.0) rotate(0) scale(0.75)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.60\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><circle cx=\"102.0\" cy=\"126.0\" r=\"2.4\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><line x1=\"82.0\" y1=\"32.0\" x2=\"100.0\" y2=\"122.0\" stroke=\"#000000\" stroke-width=\"1.8\" stroke-dasharray=\"4 3\" marker-end=\"url(#arr-1406)\"/><line x1=\"102.0\" y1=\"126.0\" x2=\"102.0\" y2=\"98.7\" stroke=\"#000000\" stroke-width=\"2.8\" marker-end=\"url(#arr-1406)\"/><circle cx=\"102.0\" cy=\"100.0\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"107\" y=\"92\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">(2,0)</text><text x=\"150\" y=\"128\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">x \u2212 \u03b1\u2207f dips below ground</text><text x=\"120\" y=\"140\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">max(0, \u00b7) clamps it back</text></svg>",
    "drawingCaption": "Altitude cannot go below the ground x\u2082 = 0: the gradient step dips under it and the clamp max(0,\u00b7) puts the plane back on the tarmac.",
    "coreTranslation": [
      "<strong>Problem:</strong> minimize $f=\\tfrac12x_1^2+x_2^2-2x_1+3x_2$ over $x_1,x_2\\ge0$, starting at $x_0=(1,1)$ with step $\\alpha=1$. Gradient: $\\nabla f=(x_1-2,\\ 2x_2+3)$, so $\\nabla f(x_0)=(-1,5)$.",
      "<strong>One iteration:</strong> unconstrained step $y=x_0-\\nabla f=(2,\\,-4)$; project onto $\\mathbb{R}^2_+$ by clipping negatives: $x_1=(2,\\,0)$. The second coordinate hit its wall in a single step.",
      "<strong>Check optimality:</strong> at $(2,0)$, $\\nabla f=(0,3)$. A step gives $y=(2,-3)$, which projects back to $(2,0)$: a <strong>fixed point</strong>, so $(2,0)$ is optimal ($x_2$ would like to go negative but the wall stops it)."
    ],
    "math": "$$x_1=\\max\\!\\Big(0,\\ \\begin{bmatrix}1\\\\1\\end{bmatrix}-\\begin{bmatrix}-1\\\\5\\end{bmatrix}\\Big)=\\begin{bmatrix}2\\\\0\\end{bmatrix},\\qquad \\max\\!\\Big(0,\\begin{bmatrix}2\\\\0\\end{bmatrix}-\\begin{bmatrix}0\\\\3\\end{bmatrix}\\Big)=\\begin{bmatrix}2\\\\0\\end{bmatrix}\\ \\ (\\text{fixed point})$$",
    "personalConnection": "<strong>The airplane analogy.</strong> The ground is the altitude floor $x\\ge0$. After each gravity step any negative coordinate is clamped to the ground: $x_{k+1}=\\max(0,x_k-\\alpha\\nabla f(x_k))$. The plane never sinks below the tarmac.",
    "examTrap": "Notice how projected gradient immediately identifies active constraints! Unlike active set methods (which add constraints one-by-one), projected gradient can activate DOZENS of bound constraints simultaneously in a single iteration.",
    "hint": "Which coordinate gets clamped and where does the plane end up?",
    "breakdown": [
      "<strong>$x-\\alpha\\nabla f=(1,1)-(-1,5)=(2,-4)$:</strong> the step dives below the ground ($x_2\\lt0$).",
      "<strong>$\\max(0,\\cdot)$ clamps the negative coordinate:</strong> the plane lands on the ground at $(2,0)$.",
      "<strong>The second step gives $(2,0)$ again:</strong> a fixed point, so the method has found the stationary point."
    ]
  },
  {
    "id": 1501,
    "subject": "CMO",
    "topicId": "15_Active_Set_Methods_for_Quadratic_Programming",
    "topicTitle": "15 \u00b7 Active Set Methods for QP",
    "cardNumber": "01",
    "category": "QUADRATIC PROGRAMMING",
    "highlighterClass": "highlight-cyan",
    "title": "Working Set Strategy & Equality Subproblems",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1501\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"14.0\" y1=\"42.0\" x2=\"226.0\" y2=\"42.0\" stroke=\"#000000\" stroke-width=\"2.4\"/><line x1=\"19.9\" y1=\"42.0\" x2=\"19.9\" y2=\"34.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"31.7\" y1=\"42.0\" x2=\"31.7\" y2=\"34.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"43.4\" y1=\"42.0\" x2=\"43.4\" y2=\"34.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"55.2\" y1=\"42.0\" x2=\"55.2\" y2=\"34.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"67.0\" y1=\"42.0\" x2=\"67.0\" y2=\"34.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"78.8\" y1=\"42.0\" x2=\"78.8\" y2=\"34.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"90.6\" y1=\"42.0\" x2=\"90.6\" y2=\"34.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"102.3\" y1=\"42.0\" x2=\"102.3\" y2=\"34.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"114.1\" y1=\"42.0\" x2=\"114.1\" y2=\"34.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"125.9\" y1=\"42.0\" x2=\"125.9\" y2=\"34.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"137.7\" y1=\"42.0\" x2=\"137.7\" y2=\"34.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"149.4\" y1=\"42.0\" x2=\"149.4\" y2=\"34.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"161.2\" y1=\"42.0\" x2=\"161.2\" y2=\"34.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"173.0\" y1=\"42.0\" x2=\"173.0\" y2=\"34.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"184.8\" y1=\"42.0\" x2=\"184.8\" y2=\"34.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"196.6\" y1=\"42.0\" x2=\"196.6\" y2=\"34.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"208.3\" y1=\"42.0\" x2=\"208.3\" y2=\"34.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"220.1\" y1=\"42.0\" x2=\"220.1\" y2=\"34.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"14.0\" y1=\"104.0\" x2=\"226.0\" y2=\"104.0\" stroke=\"#000000\" stroke-width=\"2.4\"/><line x1=\"19.9\" y1=\"104.0\" x2=\"19.9\" y2=\"112.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"31.7\" y1=\"104.0\" x2=\"31.7\" y2=\"112.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"43.4\" y1=\"104.0\" x2=\"43.4\" y2=\"112.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"55.2\" y1=\"104.0\" x2=\"55.2\" y2=\"112.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"67.0\" y1=\"104.0\" x2=\"67.0\" y2=\"112.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"78.8\" y1=\"104.0\" x2=\"78.8\" y2=\"112.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"90.6\" y1=\"104.0\" x2=\"90.6\" y2=\"112.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"102.3\" y1=\"104.0\" x2=\"102.3\" y2=\"112.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"114.1\" y1=\"104.0\" x2=\"114.1\" y2=\"112.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"125.9\" y1=\"104.0\" x2=\"125.9\" y2=\"112.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"137.7\" y1=\"104.0\" x2=\"137.7\" y2=\"112.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"149.4\" y1=\"104.0\" x2=\"149.4\" y2=\"112.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"161.2\" y1=\"104.0\" x2=\"161.2\" y2=\"112.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"173.0\" y1=\"104.0\" x2=\"173.0\" y2=\"112.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"184.8\" y1=\"104.0\" x2=\"184.8\" y2=\"112.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"196.6\" y1=\"104.0\" x2=\"196.6\" y2=\"112.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"208.3\" y1=\"104.0\" x2=\"208.3\" y2=\"112.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"220.1\" y1=\"104.0\" x2=\"220.1\" y2=\"112.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><g transform=\"translate(120.0 73.0) rotate(0) scale(1.1)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.09\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><line x1=\"142.0\" y1=\"73.0\" x2=\"214.0\" y2=\"73.0\" stroke=\"#000000\" stroke-width=\"2.6\" marker-end=\"url(#arr-1501)\"/><line x1=\"98.0\" y1=\"73.0\" x2=\"26.0\" y2=\"73.0\" stroke=\"#000000\" stroke-width=\"2.6\" marker-end=\"url(#arr-1501)\"/><text x=\"120\" y=\"24\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">walls you touch act as rails</text><text x=\"120\" y=\"130\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">A_W p = 0 : slide along the corridor only</text></svg>",
    "drawingCaption": "Lock down the walls you are touching and treat them as rails: only motion along the corridor is left to solve for.",
    "coreTranslation": [
      "<strong>Core Philosophy:</strong> An Active Set method converts an inequality-constrained Quadratic Program $\\min \\frac{1}{2} x^T Q x + c^T x$ s.t. $A x \\ge b$ into a sequence of <strong>equality-constrained QP subproblems</strong>.",
      "<strong>The Working Set $\\mathcal{W}_k$:</strong> A subset of constraint indices currently treated as active equalities: $a_i^T x = b_i$ for $i \\in \\mathcal{W}_k$.",
      "<strong>The Search Step $p_k$:</strong> At each iteration, solve for the step $p_k$: $\\min_p \\frac{1}{2} p^T Q p + g_k^T p$ s.t. $a_i^T p = 0$ for $i \\in \\mathcal{W}_k$. This is solved directly via the linear KKT system $\\begin{bmatrix} Q & A_\\mathcal{W}^T \\\\ A_\\mathcal{W} & 0 \\end{bmatrix} \\begin{bmatrix} p \\\\ -\\lambda \\end{bmatrix} = \\begin{bmatrix} -g_k \\\\ 0 \\end{bmatrix}$."
    ],
    "math": "$$\\begin{bmatrix} Q & A_{\\mathcal{W}_k}^T \\\\ A_{\\mathcal{W}_k} & 0 \\end{bmatrix} \\begin{bmatrix} p_k \\\\ -\\lambda_k \\end{bmatrix} = \\begin{bmatrix} -\\nabla f(x_k) \\\\ \\mathbf{0} \\end{bmatrix} \\quad (\\text{KKT Linear System for } p_k)$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Lock down the walls you are touching and treat them as rails: your motion must satisfy $A_{\\mathcal W}p=0$, so you only solve for sliding along the runway between the walls. That is the equality-constrained subproblem.",
    "examTrap": "The working set $\\mathcal{W}_k$ must be linearly independent! If redundant constraints are added to $\\mathcal{W}_k$, the KKT matrix becomes singular. Active set codes must ensure LICQ on $\\mathcal{W}_k$.",
    "hint": "What equation does the pilot solve while sliding along the walls he is touching?",
    "breakdown": [
      "<strong>$A_{\\mathcal W}p=0$:</strong> the move $p$ must keep every wall in the working set fixed (slide along the rails).",
      "<strong>$Qp+g=A_{\\mathcal W}^\\top\\lambda$:</strong> inside that rail, balance the quadratic's slope against the wall pushes.",
      "<strong>The KKT system solves both at once,</strong> giving the step $p_k$ and the pushes $\\lambda_k$."
    ]
  },
  {
    "id": 1502,
    "subject": "CMO",
    "topicId": "15_Active_Set_Methods_for_Quadratic_Programming",
    "topicTitle": "15 \u00b7 Active Set Methods for QP",
    "cardNumber": "02",
    "category": "BLOCKING CONSTRAINTS",
    "highlighterClass": "highlight-amber",
    "title": "Adding a Blocking Constraint to the Working Set",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1502\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"138\" y=\"14\" width=\"90\" height=\"118\" rx=\"0\" fill=\"#d1d5db\" stroke=\"#000000\" stroke-width=\"0\"/><line x1=\"138.0\" y1=\"14.0\" x2=\"138.0\" y2=\"132.0\" stroke=\"#000000\" stroke-width=\"2.4\"/><line x1=\"138.0\" y1=\"19.4\" x2=\"145.0\" y2=\"19.4\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"138.0\" y1=\"30.1\" x2=\"145.0\" y2=\"30.1\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"138.0\" y1=\"40.8\" x2=\"145.0\" y2=\"40.8\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"138.0\" y1=\"51.5\" x2=\"145.0\" y2=\"51.5\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"138.0\" y1=\"62.3\" x2=\"145.0\" y2=\"62.3\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"138.0\" y1=\"73.0\" x2=\"145.0\" y2=\"73.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"138.0\" y1=\"83.7\" x2=\"145.0\" y2=\"83.7\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"138.0\" y1=\"94.5\" x2=\"145.0\" y2=\"94.5\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"138.0\" y1=\"105.2\" x2=\"145.0\" y2=\"105.2\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"138.0\" y1=\"115.9\" x2=\"145.0\" y2=\"115.9\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"138.0\" y1=\"126.6\" x2=\"145.0\" y2=\"126.6\" stroke=\"#000000\" stroke-width=\"1.1\"/><g transform=\"translate(46.0 72.0) rotate(0) scale(1)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.20\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><line x1=\"64.0\" y1=\"72.0\" x2=\"130.0\" y2=\"72.0\" stroke=\"#000000\" stroke-width=\"2.8\" marker-end=\"url(#arr-1502)\"/><circle cx=\"138.0\" cy=\"72.0\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"136\" y=\"92\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"end\" fill=\"#000000\">stop: \u03b1 &lt; 1</text><line x1=\"140.0\" y1=\"72.0\" x2=\"190.0\" y2=\"72.0\" stroke=\"#000000\" stroke-width=\"1.5\" stroke-dasharray=\"4 3\" marker-end=\"url(#arr-1502)\"/><circle cx=\"186.0\" cy=\"72.0\" r=\"2.4\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"190\" y=\"56\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"end\" fill=\"#000000\">intended x\u0302</text><text x=\"60\" y=\"20\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"start\" fill=\"#000000\">blocking wall joins</text><text x=\"60\" y=\"32\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"start\" fill=\"#000000\">the working set</text></svg>",
    "drawingCaption": "Rolling toward the target, a wall ahead stops the plane early (step \u03b1<1) and joins the working set.",
    "coreTranslation": [
      "<strong>What:</strong> the equality subproblem proposes a full step $p_k$; if $x_k+p_k$ breaks an inactive constraint, you can only go part of the way and must stop at the wall you hit.",
      "<strong>How:</strong> only constraints with $a_i^Tp_k<0$ (moving toward the forbidden side) can block. The allowed fraction is $\\alpha_k=\\min\\big(1,\\ \\min_{i\\notin\\mathcal{W}_k,\\ a_i^Tp_k<0}\\frac{b_i-a_i^Tx_k}{a_i^Tp_k}\\big)$.",
      "<strong>Why it matters:</strong> the constraint that attains the minimum is the <em>blocking constraint</em>: set $x_{k+1}=x_k+\\alpha_kp_k$ and add it to the working set."
    ],
    "math": "$$\\alpha_k = \\min\\left( 1, \\; \\min_{i \\notin \\mathcal{W}_k, a_i^T p_k < 0} \\frac{b_i - a_i^T x_k}{a_i^T p_k} \\right), \\quad \\mathcal{W}_{k+1} = \\mathcal{W}_k \\cup \\{i_{\\text{blocking}}\\}$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Rolling along the runway toward the target, a mountain wall ahead stops you before you reach it: the step length is $\\alpha\\lt1$, you halt at the wall, and add that wall to the working set (the list of walls you are touching).",
    "examTrap": "Only consider constraints with $a_i^T p_k < 0$ (direction pointing INTO the forbidden halfspace)! If $a_i^T p_k \\ge 0$, you are moving parallel to or away from constraint $i$, so it can never block your step.",
    "hint": "How far can the pilot roll before another wall stops him?",
    "breakdown": [
      "<strong>$\\frac{b_i-a_i^\\top x_k}{a_i^\\top p_k}$ = distance to wall $i$:</strong> the gap divided by how fast you approach it.",
      "<strong>Only walls with $a_i^\\top p_k\\lt0$ matter</strong> (you are heading toward them); the minimum over them is the first wall you hit.",
      "<strong>$\\min(1,\\cdot)$:</strong> a full step $\\alpha=1$ if nothing blocks, otherwise stop at the wall and add it to $\\mathcal W$."
    ]
  },
  {
    "id": 1503,
    "subject": "CMO",
    "topicId": "15_Active_Set_Methods_for_Quadratic_Programming",
    "topicTitle": "15 \u00b7 Active Set Methods for QP",
    "cardNumber": "03",
    "category": "CONSTRAINT RELEASE",
    "highlighterClass": "highlight-emerald",
    "title": "Dropping a Constraint with Negative Multiplier",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1503\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"10\" y=\"104\" width=\"220\" height=\"34\" rx=\"0\" fill=\"#d1d5db\" stroke=\"#000000\" stroke-width=\"0\"/><line x1=\"10.0\" y1=\"104.0\" x2=\"230.0\" y2=\"104.0\" stroke=\"#000000\" stroke-width=\"2.4\"/><line x1=\"16.1\" y1=\"104.0\" x2=\"16.1\" y2=\"111.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"28.3\" y1=\"104.0\" x2=\"28.3\" y2=\"111.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"40.6\" y1=\"104.0\" x2=\"40.6\" y2=\"111.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"52.8\" y1=\"104.0\" x2=\"52.8\" y2=\"111.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"65.0\" y1=\"104.0\" x2=\"65.0\" y2=\"111.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"77.2\" y1=\"104.0\" x2=\"77.2\" y2=\"111.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"89.4\" y1=\"104.0\" x2=\"89.4\" y2=\"111.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"101.7\" y1=\"104.0\" x2=\"101.7\" y2=\"111.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"113.9\" y1=\"104.0\" x2=\"113.9\" y2=\"111.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"126.1\" y1=\"104.0\" x2=\"126.1\" y2=\"111.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"138.3\" y1=\"104.0\" x2=\"138.3\" y2=\"111.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"150.6\" y1=\"104.0\" x2=\"150.6\" y2=\"111.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"162.8\" y1=\"104.0\" x2=\"162.8\" y2=\"111.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"175.0\" y1=\"104.0\" x2=\"175.0\" y2=\"111.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"187.2\" y1=\"104.0\" x2=\"187.2\" y2=\"111.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"199.4\" y1=\"104.0\" x2=\"199.4\" y2=\"111.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"211.7\" y1=\"104.0\" x2=\"211.7\" y2=\"111.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"223.9\" y1=\"104.0\" x2=\"223.9\" y2=\"111.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><g transform=\"translate(80.0 92.0) rotate(0) scale(1)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.20\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><line x1=\"80.0\" y1=\"82.0\" x2=\"80.0\" y2=\"36.0\" stroke=\"#000000\" stroke-width=\"2.4\" stroke-dasharray=\"4 3\" marker-end=\"url(#arr-1503)\"/><text x=\"86\" y=\"44\" font-size=\"8.5\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">gravity points away</text><text x=\"155.8784\" y=\"82\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"start\" fill=\"#000000\">\u03bc &lt; 0 : the wall</text><text x=\"145.8632\" y=\"94\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"start\" fill=\"#000000\">would have to pull</text><line x1=\"98.0\" y1=\"88.0\" x2=\"178.0\" y2=\"52.0\" stroke=\"#000000\" stroke-width=\"2.8\" marker-end=\"url(#arr-1503)\"/><text x=\"232\" y=\"44\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"end\" fill=\"#000000\">take off \u2197</text></svg>",
    "drawingCaption": "A negative multiplier means gravity actually pulls you away from the wall: release the brakes, drop that wall from the working set, and take off.",
    "coreTranslation": [
      "<strong>What:</strong> when the equality subproblem gives $p_k=0$ you are at the minimum on the current working surface. Now ask: is leaving that surface worthwhile?",
      "<strong>How:</strong> compute the multipliers $\\lambda_i$ of the working constraints. If all $\\lambda_i\\ge0$, the KKT conditions hold and you are done. If some $\\lambda_j<0$, then $-\\nabla f$ points <em>into</em> the feasible side of wall $j$, so dropping it lets you decrease $f$.",
      "<strong>Why it matters:</strong> drop the constraint with the most negative multiplier. Drop only when $p_k=0$; dropping while $p_k\\ne0$ can cause cycling."
    ],
    "math": "$$p_k = \\mathbf{0} \\quad \\text{and} \\quad \\lambda_j = \\min_{i \\in \\mathcal{W}_k} \\lambda_i < 0 \\implies \\mathcal{W}_{k+1} = \\mathcal{W}_k \\setminus \\{j\\}$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Parked against a wall, the force calculation says the wall would have to pull you (a negative multiplier). Walls cannot pull, so gravity actually wants you off that wall: release the brakes, drop that wall from the working set and take off away from it.",
    "examTrap": "You can ONLY drop a constraint when $p_k = 0$ (at a stationary point of the current working surface)! Dropping a constraint while $p_k \\ne 0$ can cause premature release and severe algorithmic cycling.",
    "hint": "When does the pilot release a wall, and which one?",
    "breakdown": [
      "<strong>$p_k=0$:</strong> sliding along the current walls goes nowhere, you are at the lowest point of that runway.",
      "<strong>$\\lambda_j\\lt0$:</strong> that wall would have to pull, which walls cannot do: gravity actually wants you off it.",
      "<strong>Drop the most negative $\\lambda_j$</strong> and the next step leaves that wall and gains altitude."
    ]
  },
  {
    "id": 1504,
    "subject": "CMO",
    "topicId": "15_Active_Set_Methods_for_Quadratic_Programming",
    "topicTitle": "15 \u00b7 Active Set Methods for QP",
    "cardNumber": "04",
    "category": "FINITE TERMINATION",
    "highlighterClass": "highlight-violet",
    "title": "Finite Termination Property of Active Set QP",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1504\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"14\" y=\"24\" width=\"50\" height=\"22\" rx=\"3\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"39\" y=\"39\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">W\u2080  f\u2080</text><line x1=\"66.0\" y1=\"35.0\" x2=\"64.0\" y2=\"63.0\" stroke=\"#000000\" stroke-width=\"2\" marker-end=\"url(#arr-1504)\"/><rect x=\"66\" y=\"52\" width=\"50\" height=\"22\" rx=\"3\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"91\" y=\"67\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">W\u2081  f\u2081</text><line x1=\"118.0\" y1=\"63.0\" x2=\"116.0\" y2=\"91.0\" stroke=\"#000000\" stroke-width=\"2\" marker-end=\"url(#arr-1504)\"/><rect x=\"118\" y=\"80\" width=\"50\" height=\"22\" rx=\"3\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"143\" y=\"95\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">W\u2082  f\u2082</text><line x1=\"170.0\" y1=\"91.0\" x2=\"168.0\" y2=\"119.0\" stroke=\"#000000\" stroke-width=\"2\" marker-end=\"url(#arr-1504)\"/><rect x=\"170\" y=\"108\" width=\"50\" height=\"22\" rx=\"3\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"195\" y=\"123\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">W\u2083  f\u2083</text><g transform=\"translate(234.0 136.0) rotate(0) scale(0.5)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.40\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"10\" y=\"112\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">altitude strictly falls:</text><text x=\"10\" y=\"124\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"start\" fill=\"#000000\">f\u2080 > f\u2081 > f\u2082 > f\u2083</text><text x=\"10\" y=\"136\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">no working set repeats</text></svg>",
    "drawingCaption": "Each leg lowers altitude, so a working set is never revisited; with only finitely many wall subsets the flight must end in finitely many legs.",
    "coreTranslation": [
      "<strong>What:</strong> for a strictly convex QP ($Q\\succ0$) with no degeneracy (every step length $\\alpha_k>0$), the active-set method reaches the exact optimum in a finite number of iterations.",
      "<strong>How:</strong> there are at most $2^m$ possible working sets, and each real step (a full step or a move after dropping a constraint) strictly lowers $f$. So no working set can ever be visited twice.",
      "<strong>Why it matters:</strong> it is an <em>exact</em> method: no tolerance, no infinite convergence. The one danger is degeneracy, where a zero-length step leaves $f$ unchanged."
    ],
    "math": "$$Q \\succ 0 \\; \\text{ and } \\; \\alpha_k > 0 \\implies f(x_{k+1}) < f(x_k) \\implies \\text{Algorithm terminates in } \\le 2^m \\text{ steps}$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Every leg either hits a new wall or lands at the lowest point of the current runway, and every leg lowers altitude, so you never return to a working set you already used. There are only finitely many wall subsets, so the flight must finish in finitely many legs.",
    "examTrap": "Finite termination strictly requires <strong>non-degeneracy</strong>! If $\\alpha_k = 0$ (a degenerate vertex where multiple constraints intersect), $f(x)$ does not decrease, which opens the possibility of infinite cycling.",
    "hint": "Why does the flight always end in finitely many legs?",
    "breakdown": [
      "<strong>$Q\\succ0$ and $\\alpha_k\\gt0$:</strong> every real leg strictly lowers the altitude.",
      "<strong>So no working set ever repeats,</strong> because a repeat would mean the same altitude twice.",
      "<strong>There are only $2^m$ possible working sets,</strong> hence at most $2^m$ legs."
    ]
  },
  {
    "id": 1505,
    "subject": "CMO",
    "topicId": "15_Active_Set_Methods_for_Quadratic_Programming",
    "topicTitle": "15 \u00b7 Active Set Methods for QP",
    "cardNumber": "05",
    "category": "DEGENERACY & CYCLING",
    "highlighterClass": "highlight-indigo",
    "title": "Degeneracy, Zero Steps (\u03b1 = 0) & Anti-Cycling",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1505\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"40.0\" y1=\"72.0\" x2=\"200.0\" y2=\"72.0\" stroke=\"#000000\" stroke-width=\"2.2\"/><line x1=\"80.0\" y1=\"141.3\" x2=\"160.0\" y2=\"2.7\" stroke=\"#000000\" stroke-width=\"2.2\"/><line x1=\"160.0\" y1=\"141.3\" x2=\"80.0\" y2=\"2.7\" stroke=\"#000000\" stroke-width=\"2.2\"/><g transform=\"translate(120.0 72.0) rotate(0) scale(0.85)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.41\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><path d=\"M150,64 A30,30 0 1,1 128,42\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.6\" stroke-dasharray=\"3 2\" marker-end=\"url(#arr-1505)\"/><text x=\"120\" y=\"14\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">three walls meet at one point</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u03b1 = 0 : tower swaps walls, plane idles</text></svg>",
    "drawingCaption": "A degenerate corner: three walls meet at one point, the step is zero, and without an anti-cycling rule the tower can swap walls forever.",
    "coreTranslation": [
      "<strong>Degeneracy in QP:</strong> Occurs when more than $n$ constraints are simultaneously active at $x_k$, or when an unselected constraint also passes through $x_k$ with $a_i^T p_k < 0$.",
      "<strong>The Consequence ($\\alpha_k = 0$):</strong> Formula $\\alpha_k = \\frac{b_i - a_i^T x_k}{a_i^T p_k} = \\frac{0}{a_i^T p_k} = 0$. The iterate does NOT move in physical space ($x_{k+1} = x_k$), but the working set changes $\\mathcal{W}_{k+1} \\ne \\mathcal{W}_k$.",
      "<strong>Anti-Cycling Strategies:</strong> If zero steps persist, the algorithm can cycle endlessly through a loop of working sets without making progress. Anti-cycling rules (Bland's smallest-subscript rule, or lexicographic perturbation $b_i \\leftarrow b_i + \\epsilon^i$) guarantee finite termination even under degeneracy."
    ],
    "math": "$$\\text{Degeneracy: } b_i - a_i^T x_k = 0 \\implies \\alpha_k = 0 \\implies x_{k+1} = x_k, \\quad f(x_{k+1}) = f(x_k)$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Degenerate corner: three or more walls meet at one point, so the plane sits on the tarmac with step $\\alpha=0$ while the tower swaps which walls are officially in the working set. An anti-cycling rule (a fixed order for the tower to follow) stops it swapping in circles forever.",
    "examTrap": "Cycling cannot happen in strictly convex QP as long as $\\alpha_k > 0$. Zero-step $\\alpha_k = 0$ is the SOLE mechanism through which cycling can theoretically occur.",
    "hint": "What happens when several walls meet at the plane's position?",
    "breakdown": [
      "<strong>$b_i-a_i^\\top x_k=0$ for a wall outside the working set:</strong> it is already touching, so the blocking distance is 0.",
      "<strong>$\\alpha_k=0$:</strong> the plane does not move; only the working set changes.",
      "<strong>The altitude stays equal,</strong> so cycling is possible: an anti-cycling rule fixes the order walls enter and leave."
    ]
  },
  {
    "id": 1506,
    "subject": "CMO",
    "topicId": "15_Active_Set_Methods_for_Quadratic_Programming",
    "topicTitle": "15 \u00b7 Active Set Methods for QP",
    "cardNumber": "06",
    "category": "WORKED BENCHMARK",
    "highlighterClass": "highlight-rose",
    "title": "Worked Benchmark: 2D Active Set QP Traversal",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1506\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"36\" y=\"52\" width=\"68\" height=\"68\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"2\"/><g transform=\"translate(36.0 120.0) rotate(0) scale(0.75)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.60\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><circle cx=\"104.0\" cy=\"120.0\" r=\"2.5\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"110\" y=\"134\" font-size=\"8.5\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">x\u2081=(2,0)</text><circle cx=\"104.0\" cy=\"52.0\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"110\" y=\"48\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">x*=(2,2)</text><path d=\"M36.0,120.0 L104.0,120.0 L104.0,52.0\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.8\"/><circle cx=\"144.8\" cy=\"11.2\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"148.8\" y=\"3.1999999999999886\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">beacon</text><line x1=\"104.0\" y1=\"52.0\" x2=\"144.8\" y2=\"11.2\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"2 3\"/><text x=\"236\" y=\"96\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"end\" fill=\"#000000\">slide, block,</text><text x=\"236\" y=\"108\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"end\" fill=\"#000000\">drop, slide</text></svg>",
    "drawingCaption": "A beacon lies outside the square room: slide along one wall, get blocked, drop the wall that no longer pushes, slide again, and park at the corner nearest it.",
    "coreTranslation": [
      "<strong>Problem:</strong> minimize $(x_1-3)^2+(x_2-3)^2$ on the box $0\\le x_1,x_2\\le2$. The unconstrained minimum $(3,3)$ is outside, so expect the answer at the corner nearest to it, $(2,2)$.",
      "<strong>Step 1:</strong> start at $x_0=(0,0)$ with $\\mathcal{W}=\\{x_1=0,\\ x_2=0\\}$; both multipliers are $-6<0$, so drop $x_1=0$. Move along the bottom edge toward $x_1=3$; the wall $x_1\\le2$ blocks at $\\alpha=\\tfrac23$, giving $(2,0)$. <strong>Step 2:</strong> at $(2,0)$ the multiplier of $x_2=0$ is $-6<0$, so drop it and move up the right edge; the wall $x_2\\le2$ blocks at $(2,2)$.",
      "<strong>Step 3:</strong> at $(2,2)$ the working constraints are $x_1=2,\\ x_2=2$ and both multipliers equal $2>0$. All multipliers non-negative means KKT holds, so $x^*=(2,2)$ is optimal."
    ],
    "math": "$$x_0 = (0,0) \\xrightarrow{\\text{drop } x_1=0} x_1 = (2, 0) \\xrightarrow{\\text{drop } x_2=0} x^* = (2, 2) \\quad (\\lambda_1^* = 2 > 0, \\; \\lambda_2^* = 2 > 0)$$",
    "personalConnection": "<strong>The airplane analogy.</strong> A beacon (the unconstrained minimiser) lies outside the legal airspace. The plane slides along one wall toward it until another wall stops it, drops walls whose pushes turn negative, and finally parks at the legal point nearest the beacon.",
    "examTrap": "Drop a constraint only after checking its multiplier is negative, and then check that the new direction really moves INTO the freed side (a\u2c7c\u1d40p > 0). Otherwise you re-enter the forbidden region.",
    "hint": "Why does the plane end at $(2,2)$ with both pushes positive?",
    "breakdown": [
      "<strong>Start at $(0,0)$ with walls $x_1=0,x_2=0$;</strong> the pushes say drop $x_1=0$ first.",
      "<strong>Slide along $x_2=0$ to the blocking wall $x_1=2$,</strong> reaching $(2,0)$; then drop $x_2=0$.",
      "<strong>At $(2,2)$ both pushes are $\\lambda=2\\gt0$,</strong> so no wall wants to be dropped: the optimum."
    ]
  },
  {
    "id": 1601,
    "subject": "CMO",
    "topicId": "16_Lagrangian_Duality_and_Slaters_Condition",
    "topicTitle": "16 \u00b7 Lagrangian Duality & Slater\u2019s",
    "cardNumber": "01",
    "category": "DUALITY GEOMETRY",
    "highlighterClass": "highlight-cyan",
    "title": "The Primal Function \u03c9(z) & Hyperplane Support",
    "textbookImg": "assets/luenberger_fig14_1.png",
    "textbookRef": "Luenberger & Ye (4th ed), Sect. 14.1, Fig. 14.1 (p. 425)",
    "drawingCaption": "Move the wall by z and record the lowest legal altitude \u03c9(z). A flat ruler of slope \u2212\u03bc pushed up from underneath touches \u03c9; where it crosses z=0 is the dual value \u03c6(\u03bc).",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1601\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"34\" y1=\"128\" x2=\"226\" y2=\"128\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-1601)\"/><line x1=\"70\" y1=\"132\" x2=\"70\" y2=\"10\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"4 3\"/><path d=\"M50.0,114.0 L54.3,108.1 L58.6,102.7 L62.9,97.7 L67.2,93.1 L71.5,88.8 L75.8,84.8 L80.1,81.1 L84.4,77.7 L88.7,74.6 L93.0,71.7 L97.3,69.0 L101.6,66.5 L105.9,64.2 L110.2,62.1 L114.5,60.1 L118.8,58.3 L123.1,56.6 L127.4,55.1 L131.7,53.7 L136.0,52.3 L140.3,51.1 L144.6,50.0 L148.9,48.9 L153.2,47.9 L157.5,47.0 L161.8,46.2 L166.1,45.4 L170.4,44.7 L174.7,44.1 L179.0,43.5 L183.3,42.9 L187.6,42.4 L191.9,41.9 L196.2,41.5 L200.5,41.1 L204.8,40.7 L209.1,40.3 L213.4,40.0 L217.7,39.7 L222.0,39.4\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.6\"/><line x1=\"70\" y1=\"78\" x2=\"190\" y2=\"126\" stroke=\"#000000\" stroke-width=\"1.6\"/><circle cx=\"120.0\" cy=\"57.8\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><g transform=\"translate(128.0 43.8) rotate(20) scale(0.6)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.00\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><circle cx=\"70.0\" cy=\"78.0\" r=\"2.8\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"64\" y=\"82\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"end\" fill=\"#000000\">\u03c6(\u03bc)</text><circle cx=\"70.0\" cy=\"90.2\" r=\"2.5\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"64\" y=\"94.2\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"end\" fill=\"#000000\">p*</text><text x=\"214\" y=\"20\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"end\" fill=\"#000000\">\u03c9(z)</text><text x=\"214\" y=\"140\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"end\" fill=\"#000000\">z (wall position)</text><text x=\"190\" y=\"110\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">slope \u2212\u03bc</text></svg>",
    "coreTranslation": [
      "<strong>What:</strong> the primal function $\\omega(z)=\\inf\\{f(x):g(x)\\le z\\}$ is a 'price list': it is the best cost you can get if the constraint is relaxed to $g(x)\\le z$. The real problem's answer is $\\omega(0)=f^*$.",
      "<strong>How:</strong> take a hyperplane with normal $(\\mu,1)$ lying below the graph of $\\omega$. Its height at $z=0$ is $\\phi(\\mu)=\\inf_x\\{f(x)+\\mu^Tg(x)\\}$, the <em>dual function</em>.",
      "<strong>Why it matters:</strong> maximizing the dual means lifting that supporting hyperplane as high as possible. If $\\omega$ is convex, the highest one touches $\\omega$ at $z=0$, so the gap vanishes (strong duality)."
    ],
    "math": "$$\\omega(z) = \\inf_{x \\in \\Omega} \\{f(x) : g(x) \\le z\\}, \\quad \\phi(\\mu) = \\inf_{z} \\{\\omega(z) + \\mu^T z\\} = \\inf_{x \\in \\Omega} \\{f(x) + \\mu^T g(x)\\}$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Move a mountain wall by $z$ and record the lowest legal altitude $\\omega(z)$ you can reach. Slide a flat ruler (a hyperplane of slope $-\\mu$) up from underneath this altitude curve until it touches it: where the ruler crosses the $z=0$ pole is the dual value $\\phi(\\mu)$.",
    "examTrap": "Notice that $\\omega(z)$ is non-increasing ($z_1 \\le z_2 \\implies \\omega(z_1) \\ge \\omega(z_2)$) because relaxing constraints ($z_2 > z_1$) enlarges the feasible region, which can only lower the minimum value.",
    "hint": "How does the ruler under the altitude curve give the dual value?",
    "breakdown": [
      "<strong>$\\omega(z)$ = lowest legal altitude when the wall is moved by $z$.</strong>",
      "<strong>$\\omega(z)+\\mu^\\top z$ = that curve plus a tilted ruler of slope $\\mu$;</strong> the lowest point of the sum is $\\phi(\\mu)$, where the ruler touches the curve from below.",
      "<strong>$\\phi(\\mu)=\\inf_x\\{f+\\mu^\\top g\\}$:</strong> the same quantity, computed directly from the Lagrangian."
    ]
  },
  {
    "id": 1602,
    "subject": "CMO",
    "topicId": "16_Lagrangian_Duality_and_Slaters_Condition",
    "topicTitle": "16 \u00b7 Lagrangian Duality & Slater\u2019s",
    "cardNumber": "02",
    "category": "WEAK DUALITY",
    "highlighterClass": "highlight-amber",
    "title": "Weak Duality Theorem & The Duality Gap",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1602\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"20\" y1=\"54\" x2=\"150\" y2=\"54\" stroke=\"#000000\" stroke-width=\"3\"/><text x=\"156\" y=\"50\" font-size=\"10\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"start\" fill=\"#000000\">p*</text><g transform=\"translate(60.0 42.0) rotate(0) scale(0.7)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.71\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><line x1=\"20\" y1=\"84\" x2=\"150\" y2=\"84\" stroke=\"#000000\" stroke-width=\"1.4\" stroke-dasharray=\"5 3\"/><line x1=\"20\" y1=\"106\" x2=\"150\" y2=\"106\" stroke=\"#000000\" stroke-width=\"1.4\" stroke-dasharray=\"5 3\"/><line x1=\"20\" y1=\"124\" x2=\"150\" y2=\"124\" stroke=\"#000000\" stroke-width=\"1.4\" stroke-dasharray=\"5 3\"/><text x=\"156\" y=\"88\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">q(\u03bc) \u2264 p*</text><line x1=\"40.0\" y1=\"124.0\" x2=\"40.0\" y2=\"90.0\" stroke=\"#000000\" stroke-width=\"1.6\" marker-end=\"url(#arr-1602)\"/><text x=\"160\" y=\"128\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">raise the floor</text><line x1=\"120.0\" y1=\"82.0\" x2=\"120.0\" y2=\"58.0\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"2 2\" marker-end=\"url(#arr-1602)\"/><text x=\"130\" y=\"72\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">gap</text><text x=\"120\" y=\"12\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">dual floors can never pass the true floor</text></svg>",
    "drawingCaption": "Every wall price \u03bc builds a floor q(\u03bc) beneath the lowest legal altitude p*. The best floor can never rise above it, and the leftover distance is the duality gap.",
    "coreTranslation": [
      "<strong>What:</strong> for <em>any</em> problem, convex or not, the dual optimum never exceeds the primal optimum: $d^*\\le p^*$. The difference $p^*-d^*\\ge0$ is the <em>duality gap</em>.",
      "<strong>How:</strong> for any feasible $x$ and any $\\mu\\ge0$: $q(\\lambda,\\mu)=\\inf_{\\tilde x}\\mathcal{L}\\le\\mathcal{L}(x,\\lambda,\\mu)=f(x)+\\lambda^Th+\\mu^Tg\\le f(x)$, because $h=0$ and $\\mu^Tg\\le0$. Take sup on the left and inf on the right.",
      "<strong>Why it matters:</strong> every dual feasible point gives a certified lower bound on the best cost. It needs no assumption at all; closing the gap (strong duality) is what needs convexity and Slater."
    ],
    "math": "$$d^* = \\sup_{\\mu \\ge 0, \\lambda} q(\\lambda, \\mu) \\le \\inf_{g(x) \\le 0, h(x) = 0} f(x) = p^* \\implies p^* - d^* \\ge 0 \\quad (\\text{Universal})$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Any wall price $\\mu\\ge0$ gives a floor beneath the lowest legal altitude. The best floor you can build (the dual optimum) can never rise above the true lowest legal altitude (the primal optimum): that gap is the duality gap.",
    "examTrap": "Weak duality requires ABSOLUTELY NO ASSUMPTIONS! It holds whether $f$ is convex, non-convex, discontinuous, or integer-valued. Strong duality ($p^* = d^*$), on the other hand, requires convexity and constraint qualifications.",
    "hint": "Why can the best floor never pass the true lowest altitude?",
    "breakdown": [
      "<strong>$q(\\lambda,\\mu)$ = the floor built from prices $(\\lambda,\\mu)$.</strong>",
      "<strong>For any legal $x$ and $\\mu\\ge0$,</strong> the Lagrangian $f(x)+\\mu^\\top g(x)\\le f(x)$ because $g\\le0$, so the floor is below every legal altitude.",
      "<strong>Hence $d^*\\le p^*$ for every problem:</strong> the gap $p^*-d^*\\ge0$ is the duality gap."
    ]
  },
  {
    "id": 1603,
    "subject": "CMO",
    "topicId": "16_Lagrangian_Duality_and_Slaters_Condition",
    "topicTitle": "16 \u00b7 Lagrangian Duality & Slater\u2019s",
    "cardNumber": "03",
    "category": "STRONG DUALITY",
    "highlighterClass": "highlight-emerald",
    "title": "Strong Duality Theorem & Zero Duality Gap",
    "textbookImg": "assets/luenberger_fig14_3.png",
    "textbookRef": "Luenberger & Ye (4th ed), Sect. 14.2, Fig. 14.3 (p. 427)",
    "drawingCaption": "Under convexity and Slater's room to move, the pilot descending from above and the tower raising a floor from below meet at the same altitude.",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1603\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"20\" y1=\"76\" x2=\"220\" y2=\"76\" stroke=\"#000000\" stroke-width=\"3\"/><g transform=\"translate(120.0 36.0) rotate(90) scale(0.9)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.33\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><line x1=\"120.0\" y1=\"48.0\" x2=\"120.0\" y2=\"70.0\" stroke=\"#000000\" stroke-width=\"2.2\" marker-end=\"url(#arr-1603)\"/><line x1=\"120.0\" y1=\"124.0\" x2=\"120.0\" y2=\"82.0\" stroke=\"#000000\" stroke-width=\"2.2\" marker-end=\"url(#arr-1603)\"/><text x=\"130\" y=\"108\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">dual floor rises</text><text x=\"130\" y=\"36\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">primal descends</text><text x=\"120\" y=\"138\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">p* = q*   gap = 0</text><text x=\"34\" y=\"70\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">meet</text></svg>",
    "coreTranslation": [
      "<strong>Strong Duality Theorem:</strong> If the primal objective $f(x)$ and inequality constraints $g_j(x)$ are convex, equality constraints $h_i(x)$ are affine, and <strong>Slater's condition</strong> holds, then:",
      "$$p^* = d^* \\quad (\\text{Duality Gap is Exactly Zero!})$$",
      "<strong>Geometric Proof (Luenberger):</strong> Convexity of $f$ and $g$ guarantees that the primal function $\\omega(z)$ is a convex curve. By the Separating Hyperplane Theorem, there exists a non-vertical supporting hyperplane touching $\\omega(z)$ at $z=0$. Its intercept is $f^* = \\phi^*$, closing the gap!"
    ],
    "math": "$$\\text{Convexity } + \\text{ Slater's CQ } \\implies p^* = \\min_{x \\in \\Omega} f(x) = \\max_{\\mu \\ge 0, \\lambda} q(\\lambda, \\mu) = d^*$$",
    "personalConnection": "<strong>The airplane analogy.</strong> With a convex valley and Slater's room to move, the best floor you can build touches the lowest legal altitude: zero gap. The pilot descending from above and the tower raising a floor from below meet at the same altitude.",
    "examTrap": "If Slater's condition fails (e.g., $g_1(x) = x_1^2 \\le 0$, which has no strictly interior point since $x_1$ must equal 0), strong duality can FAIL even for perfectly convex problems!",
    "hint": "What two conditions make the floor touch the lowest altitude exactly?",
    "breakdown": [
      "<strong>Convexity:</strong> the primal function $\\omega$ is convex, so a supporting ruler exists.",
      "<strong>Slater's room to move:</strong> a strictly interior point guarantees the ruler is not vertical.",
      "<strong>Then $p^*=d^*$:</strong> the pilot from above and the tower from below meet."
    ]
  },
  {
    "id": 1604,
    "subject": "CMO",
    "topicId": "16_Lagrangian_Duality_and_Slaters_Condition",
    "topicTitle": "16 \u00b7 Lagrangian Duality & Slater\u2019s",
    "cardNumber": "04",
    "category": "CONCAVITY OF DUAL",
    "highlighterClass": "highlight-violet",
    "title": "Universal Concavity of the Dual Function q(\u03bb, \u03bc)",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1604\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"20\" y1=\"128\" x2=\"224\" y2=\"128\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-1604)\"/><line x1=\"20\" y1=\"104.8\" x2=\"222\" y2=\"-121.4\" stroke=\"#000000\" stroke-width=\"1\"/><line x1=\"20\" y1=\"75.0\" x2=\"222\" y2=\"-28.4\" stroke=\"#000000\" stroke-width=\"1\"/><line x1=\"20\" y1=\"15.2\" x2=\"222\" y2=\"47.5\" stroke=\"#000000\" stroke-width=\"1\"/><line x1=\"20\" y1=\"-82.7\" x2=\"222\" y2=\"98.3\" stroke=\"#000000\" stroke-width=\"1\"/><path d=\"M30.0,96.8 L34.6,90.3 L39.2,84.2 L43.8,78.5 L48.4,73.0 L53.0,67.9 L57.6,63.2 L62.2,58.7 L66.8,54.6 L71.4,50.9 L76.0,47.5 L80.6,44.4 L85.2,41.7 L89.8,39.3 L94.4,37.2 L99.0,35.5 L103.6,34.2 L108.2,33.1 L112.8,32.4 L117.4,32.1 L122.0,32.0 L126.6,32.3 L131.2,33.0 L135.8,34.0 L140.4,35.3 L145.0,37.0 L149.6,39.0 L154.2,41.4 L158.8,44.0 L163.4,47.1 L168.0,50.4 L172.6,54.1 L177.2,58.2 L181.8,62.6 L186.4,67.3 L191.0,72.3 L195.6,77.7 L200.2,83.5 L204.8,89.5 L209.4,95.9 L214.0,102.7\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.8\"/><text x=\"120\" y=\"12\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">each plan x gives a straight line in \u03bc</text><text x=\"120\" y=\"142\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">lowest of all lines = concave q(\u03bc)</text><g transform=\"translate(196.0 40.0) rotate(0) scale(0.6)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.00\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g></svg>",
    "drawingCaption": "For each fixed flight plan x, 'altitude + \u03bc \u00d7 wall violation' is a straight line in \u03bc. The lowest of all those lines is always a concave arch.",
    "coreTranslation": [
      "<strong>Universal Concavity Theorem:</strong> The Lagrange dual function $q(\\lambda, \\mu) = \\inf_{x \\in \\mathcal{D}} \\mathcal{L}(x, \\lambda, \\mu)$ is <strong>concave</strong>, and the dual constraint set $\\{\\mu \\ge 0\\}$ is convex.",
      "<strong>Why this is Astonishing:</strong> Even if the primal problem $f(x)$ is horribly non-convex, non-smooth, or an integer combinatorial problem, the dual problem is <strong>ALWAYS a tractable convex optimization problem</strong>!",
      "<strong>Proof:</strong> For each fixed $x$, the function $(\\lambda, \\mu) \\mapsto f(x) + \\lambda^T h(x) + \\mu^T g(x)$ is an <strong>affine function</strong> of $(\\lambda, \\mu)$. The pointwise infimum of affine functions is always concave."
    ],
    "math": "$$q(\\alpha y_1 + (1-\\alpha) y_2) \\ge \\alpha q(y_1) + (1-\\alpha) q(y_2) \\quad (\\text{Pointwise Infimum of Affine Families})$$",
    "personalConnection": "<strong>The airplane analogy.</strong> For each fixed flight plan $x$, the quantity 'altitude + $\\mu\\cdot$wall violation' is a straight line in the price $\\mu$. The dual function takes the lowest of all these lines at each $\\mu$, and a pointwise minimum of straight lines is always concave, however wild the terrain.",
    "examTrap": "The dual function is concave, which means dual optimization is a MAXIMIZATION problem: $\\max_{\\mu \\ge 0, \\lambda} q(\\lambda, \\mu)$. Maximizing a concave function is equivalent to minimizing a convex function.",
    "hint": "Why is the dual function always concave, however wild the terrain?",
    "breakdown": [
      "<strong>For a fixed plan $x$, $f(x)+\\mu^\\top g(x)$ is a straight line in $\\mu$.</strong>",
      "<strong>$q$ is the lowest of all those lines</strong> (a pointwise infimum).",
      "<strong>A pointwise minimum of straight lines bends only one way:</strong> $q(\\alpha y_1+(1-\\alpha)y_2)\\ge\\alpha q(y_1)+(1-\\alpha)q(y_2)$."
    ]
  },
  {
    "id": 1605,
    "subject": "CMO",
    "topicId": "16_Lagrangian_Duality_and_Slaters_Condition",
    "topicTitle": "16 \u00b7 Lagrangian Duality & Slater\u2019s",
    "cardNumber": "05",
    "category": "SENSITIVITY & SHADOW PRICES",
    "highlighterClass": "highlight-indigo",
    "title": "Sensitivity Analysis & Multipliers as Shadow Prices",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1605\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"34\" y1=\"128\" x2=\"226\" y2=\"128\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-1605)\"/><path d=\"M50.0,114.0 L54.3,108.1 L58.6,102.7 L62.9,97.7 L67.2,93.1 L71.5,88.8 L75.8,84.8 L80.1,81.1 L84.4,77.7 L88.7,74.6 L93.0,71.7 L97.3,69.0 L101.6,66.5 L105.9,64.2 L110.2,62.1 L114.5,60.1 L118.8,58.3 L123.1,56.6 L127.4,55.1 L131.7,53.7 L136.0,52.3 L140.3,51.1 L144.6,50.0 L148.9,48.9 L153.2,47.9 L157.5,47.0 L161.8,46.2 L166.1,45.4 L170.4,44.7 L174.7,44.1 L179.0,43.5 L183.3,42.9 L187.6,42.4 L191.9,41.9 L196.2,41.5 L200.5,41.1 L204.8,40.7 L209.1,40.3 L213.4,40.0 L217.7,39.7 L222.0,39.4\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.6\"/><line x1=\"60\" y1=\"94.3\" x2=\"190\" y2=\"5.2\" stroke=\"#000000\" stroke-width=\"1.6\" stroke-dasharray=\"5 3\"/><circle cx=\"90.0\" cy=\"73.7\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"88\" y=\"63.7\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">z=0</text><g transform=\"translate(72.0 55.7) rotate(20) scale(0.55)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.18\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><line x1=\"90.0\" y1=\"75.7\" x2=\"130.0\" y2=\"75.7\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"2 2\"/><line x1=\"130.0\" y1=\"75.7\" x2=\"130.0\" y2=\"48.3\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"2 2\"/><text x=\"150\" y=\"107.69155633280639\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u0394z = +1</text><text x=\"206\" y=\"60\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"end\" fill=\"#000000\">\u03c9 drops by \u03bc*</text><text x=\"120\" y=\"142\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">multiplier = shadow price</text></svg>",
    "drawingCaption": "Slide the wall back by \u0394z: the lowest legal altitude falls along the tangent of slope \u2212\u03bc*, so \u03bc* prices one unit of extra airspace.",
    "coreTranslation": [
      "<strong>What:</strong> the multiplier $\\mu_j^*$ is the <em>price</em> of constraint $j$: the rate at which the optimal cost drops when you relax the constraint to $g_j(x)\\le z_j$.",
      "<strong>How:</strong> if strong duality holds, $p^*(z)\\ge p^*(0)-\\mu^{*T}z$, so $\\mu^*$ is a (negative) slope of the optimal-value curve at $z=0$: $\\partial p^*/\\partial z_j=-\\mu_j^*$ (and $-\\lambda_i^*$ for equalities).",
      "<strong>Why it matters:</strong> a multiplier of 50 means an extra unit of that resource saves about 50 in cost, and $\\mu_j^*=0$ means that constraint isn't limiting you at all."
    ],
    "math": "$$p^*(z) \\ge p^*(0) - \\sum_{j=1}^m \\mu_j^* z_j - \\sum_{i=1}^p \\lambda_i^* w_i \\implies \\nabla_z p^*(0) = -\\mu^*$$",
    "personalConnection": "<strong>The airplane analogy.</strong> The multiplier is a shadow price. If moving a mountain wall back by one metre of extra airspace lowers your lowest legal altitude by $\\mu^*$, then $\\mu^*$ is what the wall's push is worth per metre of room.",
    "examTrap": "Remember the negative sign! Because relaxing a constraint means $z_j > 0$ (enlarging the feasible set), the cost decreases ($p^*(z) \\le p^*(0)$), which is why $\\partial p^* / \\partial z_j = -\\mu_j^* \\le 0$.",
    "hint": "What does a multiplier tell the pilot about moving a wall?",
    "breakdown": [
      "<strong>$p^*(z)$ = lowest legal altitude after moving the wall by $z$.</strong>",
      "<strong>$p^*(z)\\ge p^*(0)-\\mu^{*\\top}z$:</strong> a wall moved back by $z$ cannot save more than $\\mu^*z$.",
      "<strong>So $\\nabla_zp^*(0)=-\\mu^*$:</strong> the multiplier is the price of one unit of extra airspace."
    ]
  },
  {
    "id": 1606,
    "subject": "CMO",
    "topicId": "16_Lagrangian_Duality_and_Slaters_Condition",
    "topicTitle": "16 \u00b7 Lagrangian Duality & Slater\u2019s",
    "cardNumber": "06",
    "category": "WORKED BENCHMARK",
    "highlighterClass": "highlight-rose",
    "title": "SVM: Margin, Primal Problem and Lagrangian",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1606\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"90\" y=\"10\" width=\"60\" height=\"124\" rx=\"0\" fill=\"#eef0f4\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"4 3\"/><line x1=\"90\" y1=\"10\" x2=\"90\" y2=\"134\" stroke=\"#000000\" stroke-width=\"1.6\"/><line x1=\"150\" y1=\"10\" x2=\"150\" y2=\"134\" stroke=\"#000000\" stroke-width=\"1.6\"/><line x1=\"120\" y1=\"10\" x2=\"120\" y2=\"134\" stroke=\"#000000\" stroke-width=\"1.4\" stroke-dasharray=\"6 3\"/><line x1=\"92.0\" y1=\"70.0\" x2=\"148.0\" y2=\"70.0\" stroke=\"#000000\" stroke-width=\"1.4\" marker-end=\"url(#arr-1606)\"/><line x1=\"148.0\" y1=\"70.0\" x2=\"92.0\" y2=\"70.0\" stroke=\"#000000\" stroke-width=\"1.4\" marker-end=\"url(#arr-1606)\"/><text x=\"120\" y=\"64\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">margin</text><text x=\"120\" y=\"84\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">2/\u2016w\u2016</text><g transform=\"translate(80.0 38.0) rotate(0) scale(0.5)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.40\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><g transform=\"translate(80.0 104.0) rotate(0) scale(0.5)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.40\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><g transform=\"translate(42.0 70.0) rotate(0) scale(0.5)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.40\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><g transform=\"translate(28.0 112.0) rotate(0) scale(0.5)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.40\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><g transform=\"translate(52.0 26.0) rotate(0) scale(0.5)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.40\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><g transform=\"translate(160.0 52.0) rotate(180) scale(0.5)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.40\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><g transform=\"translate(160.0 112.0) rotate(180) scale(0.5)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.40\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><g transform=\"translate(198.0 86.0) rotate(180) scale(0.5)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.40\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><g transform=\"translate(216.0 38.0) rotate(180) scale(0.5)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.40\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><g transform=\"translate(188.0 124.0) rotate(180) scale(0.5)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.40\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"46\" y=\"140\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">eastbound</text><text x=\"194\" y=\"140\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">westbound</text></svg>",
    "drawingCaption": "Two opposing traffic flows: the widest no-fly strip between them has a width set only by the planes nearest its edges, so maximising the margin means minimising \u00bd\u2016w\u2016\u00b2.",
    "coreTranslation": [
      "<strong>What:</strong> a support vector machine separates two classes ($y_i=\\pm1$) with the line $w^Tx+b=0$ so that the empty 'street' around it is as wide as possible.",
      "<strong>How:</strong> require every point to be outside the street, $y_i(w^Tx_i+b)\\ge1$. The street's width is $2/\\|w\\|$, so the widest street comes from the convex QP $\\min_{w,b}\\tfrac12\\|w\\|^2$ subject to those $N$ inequalities.",
      "<strong>Why it matters:</strong> one multiplier $\\alpha_i\\ge0$ per point gives the Lagrangian $\\mathcal{L}=\\tfrac12\\|w\\|^2-\\sum_i\\alpha_i\\big[y_i(w^Tx_i+b)-1\\big]$. Stationarity in $w$ and $b$ then gives $w=\\sum\\alpha_iy_ix_i$ and $\\sum\\alpha_iy_i=0$ (next card)."
    ],
    "math": "$$\\min_{w,b}\\ \\tfrac12\\|w\\|^2\\ \\ \\text{s.t.}\\ \\ y_i(w^Tx_i+b)\\ge1,\\qquad \\text{margin}=\\frac{2}{\\|w\\|}$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Two opposing traffic flows must be separated. Draw the widest possible no-fly strip between them: the strip's width (the margin) is set only by the aircraft that come closest to its edges, so maximising the margin is minimising $\\tfrac12\\|w\\|^2$.",
    "examTrap": "The constraints are y_i(w\u1d40x_i + b) \u2265 1, not \u2265 0. The 1 sets the scale of w and is what makes the margin exactly 2/\u2016w\u2016.",
    "hint": "What quantity does the margin strip depend on, and why do we minimise $\\|w\\|$?",
    "breakdown": [
      "<strong>$y_i(w^\\top x_i+b)\\ge1$:</strong> every plane is on its correct side and at least a margin away.",
      "<strong>Margin $=2/\\|w\\|$:</strong> the strip width shrinks as $w$ grows.",
      "<strong>Maximising the margin = minimising $\\tfrac12\\|w\\|^2$,</strong> a convex quadratic problem."
    ]
  },
  {
    "id": 1608,
    "subject": "CMO",
    "topicId": "16_Lagrangian_Duality_and_Slaters_Condition",
    "topicTitle": "16 \u00b7 Lagrangian Duality & Slater\u2019s",
    "cardNumber": "07",
    "category": "DUALITY IN PRACTICE",
    "highlighterClass": "highlight-rose",
    "title": "SVM Dual: Support Vectors and the Kernel Trick",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1608\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"90\" y1=\"10\" x2=\"90\" y2=\"134\" stroke=\"#000000\" stroke-width=\"1.6\"/><line x1=\"150\" y1=\"10\" x2=\"150\" y2=\"134\" stroke=\"#000000\" stroke-width=\"1.6\"/><line x1=\"120\" y1=\"10\" x2=\"120\" y2=\"134\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"6 3\"/><g transform=\"translate(80.0 38.0) rotate(0) scale(0.5)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.40\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"80\" y=\"28\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u03b1>0</text><g transform=\"translate(80.0 104.0) rotate(0) scale(0.5)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.40\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"80\" y=\"94\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u03b1>0</text><g transform=\"translate(42.0 70.0) rotate(0) scale(0.5)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.40\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"42\" y=\"60\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u03b1=0</text><g transform=\"translate(28.0 112.0) rotate(0) scale(0.5)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.40\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"28\" y=\"102\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u03b1=0</text><g transform=\"translate(52.0 26.0) rotate(0) scale(0.5)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.40\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"52\" y=\"16\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u03b1=0</text><g transform=\"translate(160.0 52.0) rotate(180) scale(0.5)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.40\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"160\" y=\"42\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u03b1>0</text><g transform=\"translate(160.0 112.0) rotate(180) scale(0.5)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.40\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"160\" y=\"102\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u03b1>0</text><g transform=\"translate(198.0 86.0) rotate(180) scale(0.5)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.40\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"198\" y=\"76\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u03b1=0</text><g transform=\"translate(216.0 38.0) rotate(180) scale(0.5)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.40\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"216\" y=\"28\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u03b1=0</text><g transform=\"translate(188.0 124.0) rotate(180) scale(0.5)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.40\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"188\" y=\"114\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u03b1=0</text><text x=\"120\" y=\"144\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">only planes on the edges carry weight</text></svg>",
    "drawingCaption": "Only the planes touching the edges of the strip (support vectors, \u03b1>0) carry weight; every other plane has \u03b1=0 and could be removed without moving the strip.",
    "coreTranslation": [
      "<strong>What:</strong> substituting $w=\\sum\\alpha_iy_ix_i$ back into the Lagrangian gives the SVM dual: $\\max_\\alpha\\ \\sum_i\\alpha_i-\\tfrac12\\sum_{i,j}\\alpha_i\\alpha_jy_iy_j\\,x_i^Tx_j$ subject to $\\alpha_i\\ge0$, $\\sum\\alpha_iy_i=0$.",
      "<strong>How:</strong> complementary slackness $\\alpha_i[y_i(w^Tx_i+b)-1]=0$ says $\\alpha_i>0$ only for points exactly on the margin. These <em>support vectors</em> alone determine $w$; deleting any other point changes nothing.",
      "<strong>Why it matters:</strong> the data enter only through inner products $x_i^Tx_j$, so you may replace them by a kernel $K(x_i,x_j)$ and get a curved boundary at no extra cost (<em>kernel trick</em>). <strong>Check on two points:</strong> $x_1=(1,1),y_1=+1$ and $x_2=(-1,-1),y_2=-1$ give $\\alpha_1=\\alpha_2=\\tfrac14$, $w=(\\tfrac12,\\tfrac12)$, and dual value $\\tfrac14=\\tfrac12\\|w\\|^2$ (no gap)."
    ],
    "math": "$$\\max_{\\alpha\\ge0,\\ \\sum\\alpha_iy_i=0}\\ \\sum_i\\alpha_i-\\tfrac12\\sum_{i,j}\\alpha_i\\alpha_jy_iy_j\\,x_i^Tx_j,\\qquad w^*=\\sum_i\\alpha_i^*y_ix_i,\\ \\ \\alpha_i^*>0\\Rightarrow\\text{support vector}$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Only the planes touching the edges of the buffer strip (the support vectors) carry non-zero weight $\\alpha_i$ in the dual; every other aircraft has $\\alpha_i=0$ and could be removed without moving the strip. The kernel trick means the radar only needs distances and dot products between aircraft, not their coordinates.",
    "examTrap": "\u03b1_i > 0 means the point is exactly ON the margin, but a point on the margin can still have \u03b1_i = 0 (a degenerate case). 'Support vector \u21d2 \u03b1 > 0' is the safe direction; 'on the margin \u21d2 \u03b1 > 0' is not.",
    "hint": "Which planes carry weight in the dual, and why does the kernel trick work?",
    "breakdown": [
      "<strong>$w^*=\\sum\\alpha_i^*y_ix_i$:</strong> the strip's normal is a weighted sum of planes.",
      "<strong>$\\alpha_i^*\\gt0$ only for planes on the strip's edge (support vectors);</strong> all others have weight 0.",
      "<strong>The dual uses data only through $x_i^\\top x_j$,</strong> so replacing it by a kernel changes the geometry without changing the algorithm."
    ]
  },
  {
    "id": 1701,
    "subject": "CMO",
    "topicId": "17_Wolfe_Duality",
    "topicTitle": "17 \u00b7 Wolfe Duality",
    "cardNumber": "01",
    "category": "DUAL FORMULATIONS",
    "highlighterClass": "highlight-cyan",
    "title": "The Wolfe Dual Formulation for Convex NLP",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1701\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><g transform=\"translate(60.0 74.0) rotate(0) scale(1.1)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.09\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><line x1=\"60.0\" y1=\"60.0\" x2=\"60.0\" y2=\"34.0\" stroke=\"#000000\" stroke-width=\"2.4\" stroke-dasharray=\"4 3\" marker-end=\"url(#arr-1701)\"/><text x=\"66\" y=\"42\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">wall push</text><line x1=\"60.0\" y1=\"88.0\" x2=\"60.0\" y2=\"114.0\" stroke=\"#000000\" stroke-width=\"2.4\" marker-end=\"url(#arr-1701)\"/><text x=\"66\" y=\"112\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">gravity</text><text x=\"60.7528\" y=\"18\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u2207\u2093L = 0 : forces balance</text><text x=\"64.32\" y=\"136\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">only equilibrium states count</text><line x1=\"130\" y1=\"10\" x2=\"130\" y2=\"134\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"3 3\"/><line x1=\"170\" y1=\"118\" x2=\"170\" y2=\"28\" stroke=\"#000000\" stroke-width=\"2.2\"/><rect x=\"160\" y=\"70\" width=\"20\" height=\"8\" rx=\"0\" fill=\"#d9dee7\" stroke=\"#000000\" stroke-width=\"1.4\"/><line x1=\"190.0\" y1=\"100.0\" x2=\"190.0\" y2=\"36.0\" stroke=\"#000000\" stroke-width=\"2.4\" marker-end=\"url(#arr-1701)\"/><text x=\"186.3413\" y=\"24\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">maximise L over \u03bc \u2265 0</text><text x=\"176\" y=\"134\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u03bc dial</text></svg>",
    "drawingCaption": "Restrict to equilibrium states where wall pushes exactly balance gravity (\u2207\u2093L = 0), then turn the dial \u03bc up to make the Lagrangian as large as possible.",
    "coreTranslation": [
      "<strong>What:</strong> the Wolfe dual of a convex differentiable problem $\\min f$ s.t. $g\\le0$, $h=0$ is $\\max_{x,\\lambda,\\mu}\\mathcal{L}(x,\\lambda,\\mu)$ subject to $\\nabla_x\\mathcal{L}=0$ and $\\mu\\ge0$.",
      "<strong>How:</strong> in ordinary Lagrange duality the dual function is $\\inf_x\\mathcal{L}$, which needs the minimizing $x$ in closed form. For a convex $\\mathcal{L}$ that infimum sits exactly where $\\nabla_x\\mathcal{L}=0$, so Wolfe just imposes that equation as a constraint and treats $x$ as a variable.",
      "<strong>Why it matters:</strong> you never have to eliminate $x$ by hand. Note that $x$ in the Wolfe dual need not be primal feasible; only $\\nabla_x\\mathcal{L}=0$ and $\\mu\\ge0$ are required."
    ],
    "math": "$$\\max_{x, \\lambda, \\mu} \\left\\{ f(x) + \\lambda^T h(x) + \\mu^T g(x) \\right\\} \\quad \\text{subject to} \\quad \\nabla f(x) + \\nabla h(x) \\lambda + \\nabla g(x) \\mu = \\mathbf{0}, \\; \\mu \\ge 0$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Instead of checking every possible flight plan, the Wolfe dual restricts to equilibrium states: the positions where gravity is exactly balanced by wall pushes ($\\nabla_x\\mathcal L=0$). Among those equilibria you then maximise the Lagrangian over the wall pushes.",
    "examTrap": "The variable $x$ in the Wolfe dual DOES NOT need to be primal feasible ($g(x) \\le 0$ is NOT required in the Wolfe dual)! The only constraints on $(x, \\lambda, \\mu)$ in the Wolfe dual are $\\nabla_x \\mathcal{L} = 0$ and $\\mu \\ge 0$.",
    "hint": "Why does restricting to $\\nabla_x\\mathcal L=0$ give a usable dual problem?",
    "breakdown": [
      "<strong>$\\nabla_x\\mathcal L=0$ = wall pushes balance gravity:</strong> the plane is at equilibrium.",
      "<strong>For a convex valley, equilibrium is the lowest point of $\\mathcal L(\\cdot,\\mu)$,</strong> so no inner minimisation is needed.",
      "<strong>Maximising $\\mathcal L$ over $(x,\\lambda,\\mu)$ subject to equilibrium</strong> gives a smooth problem with the same value."
    ]
  },
  {
    "id": 1702,
    "subject": "CMO",
    "topicId": "17_Wolfe_Duality",
    "topicTitle": "17 \u00b7 Wolfe Duality",
    "cardNumber": "02",
    "category": "WOLFE THEOREMS",
    "highlighterClass": "highlight-amber",
    "title": "Wolfe Duality Theorem & Zero Duality Gap",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1702\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"28\" y1=\"138\" x2=\"226\" y2=\"138\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-1702)\"/><line x1=\"20\" y1=\"66\" x2=\"226\" y2=\"66\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"4 3\"/><path d=\"M28.0,26.0 L36.0,32.1 L44.0,37.3 L52.0,41.7 L60.0,45.5 L68.0,48.6 L76.0,51.3 L84.0,53.5 L92.0,55.5 L100.0,57.1 L108.0,58.4 L116.0,59.6 L124.0,60.6 L132.0,61.4 L140.0,62.1 L148.0,62.7 L156.0,63.2 L164.0,63.6 L172.0,64.0 L180.0,64.3 L188.0,64.6 L196.0,64.8 L204.0,65.0 L212.0,65.1 L220.0,65.3\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.6\"/><path d=\"M28.0,106.0 L36.0,99.9 L44.0,94.7 L52.0,90.3 L60.0,86.5 L68.0,83.4 L76.0,80.7 L84.0,78.5 L92.0,76.5 L100.0,74.9 L108.0,73.6 L116.0,72.4 L124.0,71.4 L132.0,70.6 L140.0,69.9 L148.0,69.3 L156.0,68.8 L164.0,68.4 L172.0,68.0 L180.0,67.7 L188.0,67.4 L196.0,67.2 L204.0,67.0 L212.0,66.9 L220.0,66.7\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.6\" stroke-dasharray=\"5 3\"/><g transform=\"translate(60.0 18.0) rotate(0) scale(0.6)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.00\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"116\" y=\"26\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">primal: \u2193</text><text x=\"116\" y=\"114\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">dual: \u2191</text><text x=\"226\" y=\"60\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"end\" fill=\"#000000\">p* = q*</text><text x=\"120\" y=\"12\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\"></text></svg>",
    "drawingCaption": "Two climbers on opposite sides of a saddle: the lowest legal altitude seen from above and the highest equilibrium floor from below meet at the same value when the valley is convex.",
    "coreTranslation": [
      "<strong>What:</strong> for a convex differentiable problem, if $x^*$ is optimal and has KKT multipliers $(\\lambda^*,\\mu^*)$, then $(x^*,\\lambda^*,\\mu^*)$ is optimal for the Wolfe dual.",
      "<strong>How:</strong> the KKT conditions say exactly that $(x^*,\\lambda^*,\\mu^*)$ is Wolfe-feasible ($\\nabla_x\\mathcal{L}=0$, $\\mu\\ge0$), and complementary slackness gives $\\mathcal{L}(x^*,\\lambda^*,\\mu^*)=f(x^*)$. Weak duality then says no Wolfe-feasible point beats it.",
      "<strong>Why it matters:</strong> primal minimum $=$ Wolfe dual maximum, with zero gap. Solve either problem and you get the other's value for free."
    ],
    "math": "$$f, g_j \\text{ convex}, \\; h_i \\text{ affine} \\implies \\max_{(x, \\lambda, \\mu) \\in \\text{Wolfe}} \\mathcal{L}(x, \\lambda, \\mu) = f(x^*) = \\min_{x \\in \\Omega} f(x)$$",
    "personalConnection": "<strong>The airplane analogy.</strong> For a convex valley, the best floor built from equilibrium states touches the lowest legal altitude: Wolfe duality has zero gap, so the cockpit and the control tower report the same number.",
    "examTrap": "Remember that if $f$ or $g_j$ is NOT convex, Wolfe duality completely breaks down! Because the stationarity condition $\\nabla_x \\mathcal{L} = 0$ can capture local maxima or inflection points, producing false duality bounds.",
    "hint": "What do the cockpit and the tower report at the optimum?",
    "breakdown": [
      "<strong>$f,g_j$ convex and $h_i$ affine:</strong> a convex valley.",
      "<strong>The Wolfe dual value $\\mathcal L(x,\\lambda,\\mu)$ at the best equilibrium</strong> equals the primal lowest altitude.",
      "<strong>Zero gap:</strong> the maximum on one side equals the minimum on the other."
    ]
  },
  {
    "id": 1703,
    "subject": "CMO",
    "topicId": "17_Wolfe_Duality",
    "topicTitle": "17 \u00b7 Wolfe Duality",
    "cardNumber": "03",
    "category": "QUADRATIC DUALITY",
    "highlighterClass": "highlight-emerald",
    "title": "Symmetric Dual of Quadratic Programming",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1703\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"10\" y=\"24\" width=\"92\" height=\"78\" rx=\"4\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.8\"/><g transform=\"translate(56.0 44.0) rotate(0) scale(0.9)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.33\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"56\" y=\"70\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">cockpit (primal)</text><text x=\"56\" y=\"84\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">min \u00bdx\u1d40Qx</text><text x=\"56\" y=\"96\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\"></text><rect x=\"138\" y=\"24\" width=\"92\" height=\"78\" rx=\"4\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.8\"/><polygon points=\"176,52 184,38 192,52\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><rect x=\"178\" y=\"52\" width=\"12\" height=\"14\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.2\"/><text x=\"184\" y=\"80\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">tower (dual)</text><text x=\"184\" y=\"94\" font-size=\"7.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">max \u2212\u00bdy\u1d40Qy+b\u1d40y</text><line x1=\"104.0\" y1=\"63.0\" x2=\"136.0\" y2=\"63.0\" stroke=\"#000000\" stroke-width=\"1.8\" marker-end=\"url(#arr-1703)\"/><line x1=\"136.0\" y1=\"63.0\" x2=\"104.0\" y2=\"63.0\" stroke=\"#000000\" stroke-width=\"1.8\" marker-end=\"url(#arr-1703)\"/><text x=\"120\" y=\"56\" font-size=\"12\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">=</text><text x=\"120\" y=\"128\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">same risk, opposite sign: totals meet</text></svg>",
    "drawingCaption": "Cockpit and tower look at the same flight: the pilot minimises the quadratic fuel burn and the tower maximises its mirror image, and the totals meet at the optimum.",
    "coreTranslation": [
      "<strong>What:</strong> for the QP $\\min\\tfrac12x^TQx+c^Tx$ s.t. $Ax\\ge b,\\ x\\ge0$ ($Q\\succ0$) the Wolfe dual is again a QP: $\\max_{x,y}\\ -\\tfrac12x^TQx+b^Ty$ s.t. $Qx-A^Ty+c\\ge0,\\ y\\ge0$.",
      "<strong>How:</strong> write $\\mathcal{L}=\\tfrac12x^TQx+c^Tx-y^T(Ax-b)-v^Tx$. Stationarity gives $Qx+c-A^Ty-v=0$, so $v=Qx+c-A^Ty\\ge0$ (that is the dual constraint). Substituting, the linear terms combine into $-x^TQx$, leaving $-\\tfrac12x^TQx+b^Ty$.",
      "<strong>Why it matters:</strong> the quadratic term flips sign and the roles of $b$ and $c$ swap, so you can check a QP solution by evaluating both objectives (they must agree)."
    ],
    "math": "$$\\max_{x, y} \\left\\{ -\\frac{1}{2} x^T Q x + b^T y \\right\\} \\quad \\text{s.t.} \\quad Q x - A^T y + c \\ge \\mathbf{0}, \\; y \\ge \\mathbf{0}$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Cockpit and tower look at the same flight. The cockpit minimises the fuel burn $\\tfrac12x^\\top Qx$ while the tower hedges with resources $b$ and pays the same quadratic cost with the opposite sign. At the optimum their totals meet.",
    "examTrap": "The dual objective is \u2212\u00bd x\u1d40Qx + b\u1d40y (note the MINUS). It comes from \u00bdx\u1d40Qx \u2212 x\u1d40Qx = \u2212\u00bdx\u1d40Qx after using stationarity x\u1d40(Qx + c \u2212 A\u1d40y \u2212 v) = 0.",
    "hint": "What are the cockpit and the tower each optimising for a quadratic program?",
    "breakdown": [
      "<strong>Primal:</strong> minimise $\\tfrac12x^\\top Qx+c^\\top x$ subject to $Ax\\ge b$.",
      "<strong>Dual objective $-\\tfrac12x^\\top Qx+b^\\top y$:</strong> the same quadratic with the opposite sign plus the resource value.",
      "<strong>Constraint $Qx-A^\\top y+c\\ge0$:</strong> the equilibrium condition; at the optimum the two objectives are equal."
    ]
  },
  {
    "id": 1704,
    "subject": "CMO",
    "topicId": "17_Wolfe_Duality",
    "topicTitle": "17 \u00b7 Wolfe Duality",
    "cardNumber": "04",
    "category": "COUNTEREXAMPLE TRAPS",
    "highlighterClass": "highlight-rose",
    "title": "Exam Trap: Wolfe Dual Failure on Non-Convex Problems",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1704\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><path d=\"M22.0,94.0 L25.4,94.0 L28.8,93.4 L32.2,92.2 L35.6,90.6 L39.0,88.5 L42.4,85.9 L45.8,83.0 L49.2,79.8 L52.6,76.3 L56.0,72.7 L59.4,69.0 L62.8,65.2 L66.2,61.6 L69.6,58.1 L73.0,54.8 L76.4,51.9 L79.8,49.2 L83.2,47.0 L86.6,45.3 L90.0,44.1 L93.4,43.4 L96.8,43.2 L100.2,43.7 L103.6,44.6 L107.0,46.2 L110.4,48.2 L113.8,50.7 L117.2,53.7 L120.6,57.0 L124.0,60.6 L127.4,64.6 L130.8,68.6 L134.2,72.8 L137.6,77.0 L141.0,81.1 L144.4,85.2 L147.8,88.9 L151.2,92.5 L154.6,95.6 L158.0,98.4 L161.4,100.7 L164.8,102.5 L168.2,103.7 L171.6,104.4 L175.0,104.6 L178.4,104.2 L181.8,103.2 L185.2,101.8 L188.6,99.8 L192.0,97.4 L195.4,94.6 L198.8,91.5 L202.2,88.1 L205.6,84.5 L209.0,80.8 L212.4,77.1 L215.8,73.4 L219.2,69.9 L222.6,66.5 L226.0,63.4\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.6\"/><g transform=\"translate(100.0 33.6) rotate(0) scale(0.7)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.71\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><circle cx=\"100.0\" cy=\"43.6\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"124\" y=\"22\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"start\" fill=\"#000000\">\u2207\u2093L = 0 here too</text><text x=\"124\" y=\"34\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">but it is a peak \u2717</text><circle cx=\"176.0\" cy=\"104.5\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"176\" y=\"120.5\" font-size=\"9.5\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">x*</text><text x=\"176\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">true lowest point</text><text x=\"40\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">false floor</text></svg>",
    "drawingCaption": "Equilibrium means forces balance, but a force-balanced plane can sit on a mountain peak. Without convexity the Wolfe dual builds a false floor.",
    "coreTranslation": [
      "<strong>What:</strong> the Wolfe dual is only valid for convex problems. For $\\min f(x)=-x^2$ the primal value is $-\\infty$.",
      "<strong>How:</strong> the Wolfe dual is $\\max f(x)$ s.t. $f'(x)=-2x=0$, whose only point is $x=0$ with value $0$. So $d^*=0>-\\infty=p^*$: weak duality fails.",
      "<strong>Why it happens:</strong> $\\nabla_x\\mathcal{L}=0$ only identifies the minimum of $\\mathcal{L}$ when $\\mathcal{L}$ is convex in $x$. In general it also finds maxima and saddles, giving false bounds."
    ],
    "math": "$$f(x) = -x^2 \\implies \\min_{x \\in \\mathbb{R}} f(x) = -\\infty, \\quad \\max_{f'(x)=0} f(x) = f(0) = 0 \\implies d^* > p^* \\; (\\text{Fails!})$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Equilibrium ($\\nabla_x\\mathcal L=0$) means forces balance, but a force-balanced plane can sit at the top of a mountain peak or on a saddle. If the valley is not convex, trusting equilibrium builds a false floor, so the Wolfe dual is invalid.",
    "examTrap": "If a question gives a NON-convex problem and asks what the Wolfe dual says, the answer is: nothing reliable (it can exceed the primal value). Use ordinary Lagrangian duality, which always gives a valid lower bound.",
    "hint": "Why can the equilibrium trick fail on a hill?",
    "breakdown": [
      "<strong>$f=-x^2$ has $f'(x)=0$ only at 0,</strong> which is its maximum, so the 'equilibrium' value is $f(0)=0$.",
      "<strong>True minimum $=-\\infty$:</strong> the dual value 0 is above the primal value, $d^*\\gt p^*$.",
      "<strong>Without convexity,</strong> force balance can happen at a peak or saddle."
    ]
  },
  {
    "id": 1705,
    "subject": "CMO",
    "topicId": "17_Wolfe_Duality",
    "topicTitle": "17 \u00b7 Wolfe Duality",
    "cardNumber": "05",
    "category": "NON-SMOOTH OPTIMIZATION",
    "highlighterClass": "highlight-violet",
    "title": "The Dual Subgradient Method",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1705\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"20\" y1=\"128\" x2=\"226\" y2=\"128\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-1705)\"/><path d=\"M36.0,106.9 L40.8,100.1 L45.5,93.7 L50.2,87.6 L55.0,81.9 L59.8,76.5 L64.5,71.5 L69.2,66.8 L74.0,62.5 L78.8,58.5 L83.5,54.9 L88.2,51.6 L93.0,48.7 L97.8,46.1 L102.5,43.9 L107.2,42.0 L112.0,40.5 L116.8,39.4 L121.5,38.6 L126.2,38.1 L131.0,38.0 L135.8,38.3 L140.5,38.9 L145.2,39.8 L150.0,41.1 L154.8,42.8 L159.5,44.8 L164.2,47.1 L169.0,49.9 L173.8,52.9 L178.5,56.3 L183.2,60.1 L188.0,64.2 L192.8,68.7 L197.5,73.5 L202.2,78.7 L207.0,84.2 L211.8,90.1 L216.5,96.4 L221.2,102.9 L226.0,109.9\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.6\"/><circle cx=\"48.0\" cy=\"90.4\" r=\"2.6\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><line x1=\"48.0\" y1=\"90.4\" x2=\"48.0\" y2=\"128.0\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"2 2\"/><text x=\"48\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u03bc\u2080</text><line x1=\"51.0\" y1=\"86.4\" x2=\"81.0\" y2=\"50.5\" stroke=\"#000000\" stroke-width=\"1.6\" marker-end=\"url(#arr-1705)\"/><circle cx=\"84.0\" cy=\"54.5\" r=\"2.6\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><line x1=\"84.0\" y1=\"54.5\" x2=\"84.0\" y2=\"128.0\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"2 2\"/><text x=\"84\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u03bc\u2081</text><line x1=\"87.0\" y1=\"50.5\" x2=\"105.0\" y2=\"37.8\" stroke=\"#000000\" stroke-width=\"1.6\" marker-end=\"url(#arr-1705)\"/><circle cx=\"108.0\" cy=\"41.8\" r=\"2.6\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><line x1=\"108.0\" y1=\"41.8\" x2=\"108.0\" y2=\"128.0\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"2 2\"/><text x=\"108\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u03bc\u2082</text><line x1=\"111.0\" y1=\"37.8\" x2=\"119.0\" y2=\"34.5\" stroke=\"#000000\" stroke-width=\"1.6\" marker-end=\"url(#arr-1705)\"/><circle cx=\"122.0\" cy=\"38.5\" r=\"2.6\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><line x1=\"122.0\" y1=\"38.5\" x2=\"122.0\" y2=\"128.0\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"2 2\"/><text x=\"122\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u03bc\u2083</text><g transform=\"translate(52.0 22.0) rotate(0) scale(0.6)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.00\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"132.0\" y=\"24\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">g > 0 (hitting the wall):</text><text x=\"142\" y=\"36\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"start\" fill=\"#000000\">raise the price \u03bc</text><text x=\"140.32\" y=\"50\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">g &lt; 0 (slack): lower it</text><text x=\"228\" y=\"100\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"end\" fill=\"#000000\">q(\u03bc)</text></svg>",
    "drawingCaption": "The tower climbs the concave dual: raise the wall price when the plane violates the wall (g>0), lower it when there is slack, never below zero.",
    "coreTranslation": [
      "<strong>What:</strong> the dual function $q(\\mu)$ is concave but often has kinks, so ordinary gradient ascent doesn't apply. The <em>subgradient method</em> maximizes it anyway.",
      "<strong>How:</strong> for the current $\\mu_k$ find $x(\\mu_k)=\\arg\\min_x\\mathcal{L}(x,\\mu_k)$; the constraint violation $g(x(\\mu_k))$ is a subgradient of $q$ at $\\mu_k$. Update $\\mu_{k+1}=\\big[\\mu_k+\\alpha_kg(x(\\mu_k))\\big]_+$ (project onto $\\mu\\ge0$).",
      "<strong>Why it matters:</strong> it works like a price adjustment: a violated constraint ($g_j>0$) gets a higher price $\\mu_j$. With steps $\\sum\\alpha_k=\\infty$, $\\sum\\alpha_k^2<\\infty$ it converges to the dual optimum, but $q(\\mu_k)$ is <em>not</em> monotone: keep the best iterate."
    ],
    "math": "$$\\mu_{k+1} = \\max\\left( \\mathbf{0}, \\; \\mu_k + \\alpha_k g(x(\\mu_k)) \\right) \\quad \\text{where } x(\\mu_k) = \\arg\\min_{x} \\mathcal{L}(x, \\mu_k)$$",
    "personalConnection": "<strong>The airplane analogy.</strong> The tower raises the wall price when the plane violates the wall ($g_j\\gt0$, flying into the mountain) and lowers it when there is slack ($g_j\\lt0$), never letting it go negative: $\\mu_{k+1}=\\max(0,\\mu_k+\\alpha g_j(x_k))$.",
    "examTrap": "The subgradient method is NOT a descent method! The objective $q(\\mu_k)$ can decrease at individual iterations. You must track the best iterate encountered: $q_{\\text{best}}^{(k)} = \\max_{i=1..k} q(\\mu_i)$.",
    "hint": "How does the tower decide whether to raise or lower the price of a wall?",
    "breakdown": [
      "<strong>$x(\\mu_k)=\\arg\\min\\mathcal L(x,\\mu_k)$:</strong> the plane flies to its best spot under the current prices.",
      "<strong>$g(x(\\mu_k))$ = violation:</strong> positive means the plane is flying into the wall, so $\\mu$ goes up.",
      "<strong>$\\max(0,\\cdot)$ keeps prices non-negative:</strong> $\\alpha_kg$ is the subgradient step of the dual."
    ]
  },
  {
    "id": 1706,
    "subject": "CMO",
    "topicId": "17_Wolfe_Duality",
    "topicTitle": "17 \u00b7 Wolfe Duality",
    "cardNumber": "06",
    "category": "WORKED BENCHMARK",
    "highlighterClass": "highlight-indigo",
    "title": "Worked Benchmark: Entropy Maximization Dual",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1706\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"14\" y1=\"124\" x2=\"226\" y2=\"124\" stroke=\"#000000\" stroke-width=\"1.4\" marker-end=\"url(#arr-1706)\"/><rect x=\"26\" y=\"38.0\" width=\"26\" height=\"86.0\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"39\" y=\"136\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">A1</text><rect x=\"66\" y=\"74.38231630727815\" width=\"26\" height=\"49.617683692721855\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"79\" y=\"136\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">A2</text><rect x=\"106\" y=\"95.37308680196516\" width=\"26\" height=\"28.626913198034842\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"119\" y=\"136\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">A3</text><rect x=\"146\" y=\"107.48370785861515\" width=\"26\" height=\"16.516292141384852\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"159\" y=\"136\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">A4</text><rect x=\"186\" y=\"114.47092838083928\" width=\"26\" height=\"9.529071619160712\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"199\" y=\"136\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">A5</text><path d=\"M39.0,38.0 L44.3,44.1 L49.7,49.7 L55.0,55.0 L60.3,59.9 L65.7,64.4 L71.0,68.6 L76.3,72.5 L81.7,76.2 L87.0,79.6 L92.3,82.7 L97.7,85.6 L103.0,88.3 L108.3,90.9 L113.7,93.2 L119.0,95.4 L124.3,97.4 L129.7,99.3 L135.0,101.0 L140.3,102.7 L145.7,104.2 L151.0,105.6 L156.3,106.9 L161.7,108.1 L167.0,109.2 L172.3,110.3 L177.7,111.2 L183.0,112.1 L188.3,113.0 L193.7,113.7 L199.0,114.5\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.4\" stroke-dasharray=\"4 3\"/><g transform=\"translate(190.0 30.0) rotate(180) scale(0.7)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.71\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"170\" y=\"56\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"start\" fill=\"#000000\">p\u1d62 \u221d e^(\u2212\u03b2E\u1d62)</text><text x=\"170\" y=\"70\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">(Boltzmann)</text></svg>",
    "drawingCaption": "A fixed fleet spread over airports A\u2081\u2026A\u2085 with a fixed average fuel cost: maximising entropy gives traffic that decays exponentially with each airport's cost.",
    "coreTranslation": [
      "<strong>What:</strong> minimize the negative entropy $\\sum x_i\\ln x_i$ subject to linear constraints $Ax=b$, $x>0$. Its dual turns out to be a smooth, unconstrained problem.",
      "<strong>How:</strong> $\\mathcal{L}=\\sum x_i\\ln x_i+\\lambda^T(b-Ax)$. Stationarity $\\ln x_i+1-(A^T\\lambda)_i=0$ gives $x_i=e^{(A^T\\lambda)_i-1}$ (automatically positive). Substituting, each term collapses to $-x_i$, so $q(\\lambda)=b^T\\lambda-\\sum_ie^{(A^T\\lambda)_i-1}$.",
      "<strong>Why it matters:</strong> you replace a constrained problem in $x$ by an unconstrained concave maximization in $\\lambda$, and the optimal $x$ has the exponential (Boltzmann) form."
    ],
    "math": "$$q(\\lambda) = b^T \\lambda - \\sum_{i=1}^n \\exp\\left( a_i^T \\lambda - 1 \\right) \\implies \\text{Unconstrained Smooth Concave Maximization}$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Spread a fixed fleet of aircraft across airports so that the total fuel budget is fixed. Maximising entropy under a fixed energy constraint gives the exponential (Boltzmann) distribution, and the wall price is the inverse temperature.",
    "examTrap": "Notice that the positivity constraint $x > 0$ is AUTOMATICALLY satisfied by the exponential $x_i^* = e^{\\dots} > 0$! Duality magically eliminates both the non-negativity constraint and the linear equalities.",
    "hint": "What shape does the entropy-maximising traffic take?",
    "breakdown": [
      "<strong>$q(\\lambda)=b^\\top\\lambda-\\sum_ie^{a_i^\\top\\lambda-1}$:</strong> the dual is smooth, unconstrained and concave, easy to maximise.",
      "<strong>The optimal primal is $x_i\\propto e^{a_i^\\top\\lambda-1}$:</strong> exponential, the Boltzmann form.",
      "<strong>$\\lambda$ plays the role of an inverse temperature</strong> set by the energy budget."
    ]
  },
  {
    "id": 1801,
    "subject": "CMO",
    "topicId": "18_Linear_Programming_Duality_and_Polyhedral_Geometry",
    "topicTitle": "18 \u00b7 LP Duality & Polyhedral Geometry",
    "cardNumber": "01",
    "category": "LINEAR PROGRAMMING",
    "highlighterClass": "highlight-cyan",
    "title": "LP Primal-Dual Pair in Standard Form",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1801\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"8\" y=\"24\" width=\"100\" height=\"84\" rx=\"4\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.8\"/><g transform=\"translate(58.0 44.0) rotate(0) scale(0.9)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.33\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"58\" y=\"70\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">airline (primal)</text><text x=\"58\" y=\"84\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">min c\u1d40x</text><text x=\"58\" y=\"96\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">Ax = b, x \u2265 0</text><rect x=\"132\" y=\"24\" width=\"100\" height=\"84\" rx=\"4\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.8\"/><rect x=\"172\" y=\"38\" width=\"12\" height=\"14\" rx=\"0\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.2\"/><polygon points=\"170,38 178,28 186,38\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.4\"/><text x=\"182\" y=\"70\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">airport (dual)</text><text x=\"182\" y=\"84\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">max b\u1d40y</text><text x=\"182\" y=\"96\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">A\u1d40y \u2264 c</text><line x1=\"110.0\" y1=\"66.0\" x2=\"130.0\" y2=\"66.0\" stroke=\"#000000\" stroke-width=\"1.6\" marker-end=\"url(#arr-1801)\"/><line x1=\"130.0\" y1=\"66.0\" x2=\"110.0\" y2=\"66.0\" stroke=\"#000000\" stroke-width=\"1.6\" marker-end=\"url(#arr-1801)\"/><text x=\"120\" y=\"130\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">cost \u2265 revenue, equal at optimum</text></svg>",
    "drawingCaption": "The airline minimises the cost of a schedule that meets demand b; the airport authority sets fees y to maximise revenue without pricing any route above the airline's cost.",
    "coreTranslation": [
      "<strong>What:</strong> the standard-form LP $\\min c^Tx$ s.t. $Ax=b,\\ x\\ge0$ has the dual $\\max b^Ty$ s.t. $A^Ty\\le c$ ($y$ free).",
      "<strong>How (the dictionary):</strong> each primal <em>equality</em> row becomes a free dual variable $y_i$; each primal <em>non-negative variable</em> $x_j$ becomes a dual <em>inequality</em> $(A^Ty)_j\\le c_j$; $c$ and $b$ swap roles; and the dual of the dual is the primal.",
      "<strong>Why it matters:</strong> if the primal has $Ax\\ge b,\\ x\\ge0$, the dual is $\\max b^Ty$ s.t. $A^Ty\\le c,\\ y\\ge0$ (inequality rows give sign-restricted dual variables). Example: min $x_1+2x_2$ s.t. $x_1+x_2\\ge3$ has dual $\\max3y$ s.t. $y\\le1,\\ y\\le2,\\ y\\ge0$, both with value $3$."
    ],
    "math": "$$\\min_{x \\ge 0, A x = b} c^T x \\iff \\max_{y \\in \\mathbb{R}^m, A^T y \\le c} b^T y \\quad (\\text{Standard Form LP Duality})$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Airline vs airport authority. The airline minimises the cost $c^\\top x$ of a flight schedule that meets demand $b$. The authority picks landing fees $y$ to maximise revenue $b^\\top y$ while keeping every route no more expensive than the airline's cost ($A^\\top y\\le c$) so the airline still agrees to fly.",
    "examTrap": "If primal has inequality $A x \\ge b, x \\ge 0$, then dual is $\\max b^T y$ s.t. $A^T y \\le c, y \\ge 0$ (dual variables become non-negative). If primal has equality $A x = b$, dual variables $y$ are completely free!",
    "hint": "Who is minimising what, and who is maximising what?",
    "breakdown": [
      "<strong>Primal (airline):</strong> $\\min c^\\top x$ with $Ax=b$, $x\\ge0$: the cheapest schedule meeting demand.",
      "<strong>Dual (authority):</strong> $\\max b^\\top y$ with $A^\\top y\\le c$: highest revenue without pricing any route above its cost.",
      "<strong>Weak duality:</strong> revenue never exceeds cost; at the optimum they are equal."
    ]
  },
  {
    "id": 1807,
    "subject": "CMO",
    "topicId": "18_Linear_Programming_Duality_and_Polyhedral_Geometry",
    "topicTitle": "18 \u00b7 LP Duality & Polyhedral Geometry",
    "cardNumber": "02",
    "category": "POLYHEDRAL GEOMETRY",
    "highlighterClass": "highlight-cyan",
    "title": "Basic Feasible Solutions = Vertices",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1807\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><polygon points=\"40,112 36,44 126,22 206,70 176,120\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"2\"/><circle cx=\"40.0\" cy=\"112.0\" r=\"2.8\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><circle cx=\"36.0\" cy=\"44.0\" r=\"2.8\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><circle cx=\"126.0\" cy=\"22.0\" r=\"2.8\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><circle cx=\"206.0\" cy=\"70.0\" r=\"2.8\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><circle cx=\"176.0\" cy=\"120.0\" r=\"2.8\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><g transform=\"translate(136.0 36.0) rotate(0) scale(0.7)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.71\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><circle cx=\"126.0\" cy=\"22.0\" r=\"3.2\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"132\" y=\"16\" font-size=\"8.5\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">pinned: 2 walls meet</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">corners = basic feasible solutions</text><text x=\"110\" y=\"78\" font-size=\"13\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u03a9</text></svg>",
    "drawingCaption": "A plane can only be pinned in place at a corner of the polygon, where enough walls meet in independent directions. Those corners are the basic feasible solutions.",
    "coreTranslation": [
      "<strong>What:</strong> in the standard form $\\{x:Ax=b,\\ x\\ge0\\}$ with $A$ of size $m\\times n$ (full row rank), the <em>corners</em> of the feasible region are exactly the <strong>basic feasible solutions (BFS)</strong>.",
      "<strong>How:</strong> choose $m$ columns forming an invertible basis $B$, set the other $n-m$ variables to $0$ (so $n-m$ constraints $x_j\\ge0$ are tight), and solve $x_B=B^{-1}b$. It is a BFS if $x_B\\ge0$.",
      "<strong>Why it matters:</strong> there are at most $\\binom nm$ vertices, a finite list. A BFS with some $x_B$ entry equal to $0$ is <em>degenerate</em>: more than $n-m$ walls meet there."
    ],
    "math": "$$x=\\begin{bmatrix}x_B\\\\x_N\\end{bmatrix}=\\begin{bmatrix}B^{-1}b\\\\\\mathbf 0\\end{bmatrix},\\quad B\\ \\text{invertible},\\ \\ x_B\\ge0\\iff x\\ \\text{is a vertex of}\\ \\{Ax=b,\\ x\\ge0\\}$$",
    "personalConnection": "<strong>The airplane analogy.</strong> A plane can only be pinned in place at a corner of the polygonal airspace, where enough walls meet in independent directions that there is nowhere to slide. Those corners are the basic feasible solutions.",
    "examTrap": "A vertex is not 'any point with m non-zeros'. It needs the columns of the non-zero entries to be linearly independent. Two different bases can describe the same degenerate vertex.",
    "hint": "Why are corners the only places the plane can be pinned?",
    "breakdown": [
      "<strong>$x_N=0$:</strong> the non-basic variables are zero, i.e. those walls are touched.",
      "<strong>$x_B=B^{-1}b$:</strong> the remaining variables are determined by the independent walls through the corner (needs $B$ invertible).",
      "<strong>$x_B\\ge0$ makes the corner legal,</strong> so basic feasible solutions are exactly the vertices."
    ]
  },
  {
    "id": 1802,
    "subject": "CMO",
    "topicId": "18_Linear_Programming_Duality_and_Polyhedral_Geometry",
    "topicTitle": "18 \u00b7 LP Duality & Polyhedral Geometry",
    "cardNumber": "03",
    "category": "POLYHEDRAL GEOMETRY",
    "highlighterClass": "highlight-amber",
    "title": "Fundamental Theorem of LP: The Optimum Is at a Vertex",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1802\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><polygon points=\"50,112 40,48 120,26 200,66 176,118\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"2\"/><line x1=\"10\" y1=\"1.0\" x2=\"232\" y2=\"45.0\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"4 3\"/><line x1=\"10\" y1=\"23.0\" x2=\"232\" y2=\"67.0\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"4 3\"/><line x1=\"10\" y1=\"45.0\" x2=\"232\" y2=\"89.0\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"4 3\"/><line x1=\"10\" y1=\"67.0\" x2=\"232\" y2=\"111.0\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"4 3\"/><line x1=\"10\" y1=\"89.0\" x2=\"232\" y2=\"133.0\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"4 3\"/><line x1=\"10\" y1=\"111.0\" x2=\"232\" y2=\"155.0\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"4 3\"/><line x1=\"10\" y1=\"133.0\" x2=\"232\" y2=\"177.0\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"4 3\"/><circle cx=\"176.0\" cy=\"118.0\" r=\"4\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"180\" y=\"112\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">lowest</text><g transform=\"translate(130.0 62.0) rotate(-20) scale(0.7)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.71\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><line x1=\"60.0\" y1=\"24.0\" x2=\"60.0\" y2=\"52.0\" stroke=\"#000000\" stroke-width=\"2.4\" marker-end=\"url(#arr-1802)\"/><text x=\"64\" y=\"20\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">gravity</text><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">tilted sheet: lowest point is a corner</text></svg>",
    "drawingCaption": "A linear altitude is a tilted flat sheet over the polygonal airspace: its lowest point is always at a corner.",
    "coreTranslation": [
      "<strong>What:</strong> for the standard LP $\\min c^Tx$ s.t. $Ax=b,\\ x\\ge0$: if a feasible point exists then a basic feasible solution (vertex) exists, and if an optimal point exists then an <em>optimal vertex</em> exists.",
      "<strong>How:</strong> a linear objective has no curvature, so from any non-vertex optimal point you can slide along the face without getting worse until you hit a vertex (the objective is constant or improves in at least one direction).",
      "<strong>Why it matters:</strong> you only need to search the finitely many vertices, which is what the simplex method does. A degenerate vertex (some basic variable equals 0) can make simplex pivot without moving."
    ],
    "math": "$$x = \\begin{bmatrix} x_B \\\\ x_N \\end{bmatrix} = \\begin{bmatrix} B^{-1} b \\\\ \\mathbf{0} \\end{bmatrix} \\iff x \\text{ is an Extreme Point of } \\mathcal{P} = \\{x : A x = b, x \\ge 0\\}$$",
    "personalConnection": "<strong>The airplane analogy.</strong> With a linear altitude (a tilted flat sheet over the polygonal airspace), the lowest point of the sheet over the polygon is always at a corner of the polygon, so the best parking spot is a vertex.",
    "examTrap": "'An optimal vertex exists' does not mean every optimum is a vertex: when the objective is parallel to a face, the whole face is optimal. And a vertex is guaranteed to exist only if the feasible set has no line inside it (true when x \u2265 0).",
    "hint": "Why must the lowest point of a tilted sheet over a polygon be a corner?",
    "breakdown": [
      "<strong>The altitude is linear,</strong> so there are no hills or valleys inside the polygon.",
      "<strong>Moving along any direction raises or lowers the altitude at a constant rate,</strong> so you can keep going until you hit a wall, then slide, until a corner.",
      "<strong>So an optimum can always be found among the finitely many basic feasible solutions.</strong>"
    ]
  },
  {
    "id": 1803,
    "subject": "CMO",
    "topicId": "18_Linear_Programming_Duality_and_Polyhedral_Geometry",
    "topicTitle": "18 \u00b7 LP Duality & Polyhedral Geometry",
    "cardNumber": "04",
    "category": "COMPLEMENTARITY",
    "highlighterClass": "highlight-emerald",
    "title": "LP Complementary Slackness Theorem",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1803\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><text x=\"60\" y=\"18\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">plan / wall</text><text x=\"184\" y=\"18\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">fee / price</text><g transform=\"translate(120.0 22.0) rotate(0) scale(0.5)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.40\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><rect x=\"16\" y=\"40\" width=\"88\" height=\"22\" rx=\"3\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"60\" y=\"55\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">x_j > 0</text><rect x=\"136\" y=\"40\" width=\"88\" height=\"22\" rx=\"3\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"180\" y=\"55\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">fee = cost</text><line x1=\"106.0\" y1=\"51.0\" x2=\"134.0\" y2=\"51.0\" stroke=\"#000000\" stroke-width=\"1.8\" marker-end=\"url(#arr-1803)\"/><line x1=\"134.0\" y1=\"51.0\" x2=\"106.0\" y2=\"51.0\" stroke=\"#000000\" stroke-width=\"1.8\" marker-end=\"url(#arr-1803)\"/><rect x=\"16\" y=\"72\" width=\"88\" height=\"22\" rx=\"3\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"60\" y=\"87\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">fee &lt; cost</text><rect x=\"136\" y=\"72\" width=\"88\" height=\"22\" rx=\"3\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"180\" y=\"87\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">x_j = 0</text><line x1=\"106.0\" y1=\"83.0\" x2=\"134.0\" y2=\"83.0\" stroke=\"#000000\" stroke-width=\"1.8\" marker-end=\"url(#arr-1803)\"/><line x1=\"134.0\" y1=\"83.0\" x2=\"106.0\" y2=\"83.0\" stroke=\"#000000\" stroke-width=\"1.8\" marker-end=\"url(#arr-1803)\"/><rect x=\"16\" y=\"104\" width=\"88\" height=\"22\" rx=\"3\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"60\" y=\"119\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">wall untouched</text><rect x=\"136\" y=\"104\" width=\"88\" height=\"22\" rx=\"3\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"180\" y=\"119\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">y_i = 0</text><line x1=\"106.0\" y1=\"115.0\" x2=\"134.0\" y2=\"115.0\" stroke=\"#000000\" stroke-width=\"1.8\" marker-end=\"url(#arr-1803)\"/><line x1=\"134.0\" y1=\"115.0\" x2=\"106.0\" y2=\"115.0\" stroke=\"#000000\" stroke-width=\"1.8\" marker-end=\"url(#arr-1803)\"/><text x=\"120\" y=\"142\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">x_j (c_j \u2212 A_j\u1d40y) = 0  and  y_i (A_i x \u2212 b_i) = 0</text></svg>",
    "drawingCaption": "The airline's rulebook: a route that is flown must have fee equal to cost; a route whose fee is below cost is never flown; a resource wall that is not touched has price zero.",
    "coreTranslation": [
      "<strong>Theorem:</strong> Let $x^*$ be primal feasible ($A x^* = b, x^* \\ge 0$) and $y^*$ be dual feasible ($A^T y^* \\le c$). Then $x^*$ and $y^*$ are <strong>mutually optimal</strong> if and only if:",
      "$$x_j^* \\cdot (c_j - A_{\\cdot j}^T y^*) = 0 \\quad \\forall \\, j = 1, \\dots, n$$",
      "<strong>Computational Power:</strong> If you know which primal variables are non-zero ($x_j^* > 0$), you instantly know which dual constraints are equalities ($A_{\\cdot j}^T y = c_j$)! This allows you to solve for the dual vector $y^*$ by solving a small linear system without running an optimization algorithm."
    ],
    "math": "$$x^*, y^* \\text{ optimal} \\iff x_j^* (c_j - A_{\\cdot j}^T y^*) = 0 \\; (\\forall j) \\quad \\text{and} \\quad y_i^* (A_{i \\cdot} x^* - b_i) = 0 \\; (\\forall i)$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Complementary slackness is the airline's rulebook. If a route is flown ($x_j\\gt0$), its fee exactly equals its cost. If the fee is below cost ($c_j\\gt A_j^\\top y$), nobody flies it ($x_j=0$). If a resource wall is not touched, its price $y_i$ is zero.",
    "examTrap": "Complementary slackness allows you to check whether a proposed solution $x$ is optimal in seconds! Form the dual equality system for $x_j > 0$, solve for $y$, and check if $A^T y \\le c$. If yes, $x$ is guaranteed optimal.",
    "hint": "Which pairs of statements must hold together at the optimum?",
    "breakdown": [
      "<strong>$x_j(c_j-A_j^\\top y)=0$:</strong> a route is flown only if its fee equals its cost.",
      "<strong>$y_i(A_ix-b_i)=0$:</strong> a resource has a positive price only if it is fully used.",
      "<strong>Either factor can be zero,</strong> but never both strictly positive: the same on/off switch as KKT."
    ]
  },
  {
    "id": 1804,
    "subject": "CMO",
    "topicId": "18_Linear_Programming_Duality_and_Polyhedral_Geometry",
    "topicTitle": "18 \u00b7 LP Duality & Polyhedral Geometry",
    "cardNumber": "05",
    "category": "THEOREMS OF THE ALTERNATIVE",
    "highlighterClass": "highlight-violet",
    "title": "From Farkas to LP Duality: Infeasible Primal \u21d2 Unbounded Dual",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1804\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><path d=\"M26.0,114.0 L116.0,100.0 L64.0,34.0\" fill=\"#e5e7eb\" stroke=\"#000000\" stroke-width=\"1.2\"/><line x1=\"26.0\" y1=\"114.0\" x2=\"92.0\" y2=\"104.0\" stroke=\"#000000\" stroke-width=\"2.4\" marker-end=\"url(#arr-1804)\"/><line x1=\"26.0\" y1=\"114.0\" x2=\"54.0\" y2=\"56.0\" stroke=\"#000000\" stroke-width=\"2.4\" marker-end=\"url(#arr-1804)\"/><g transform=\"translate(26.0 114.0) rotate(-20) scale(0.55)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.18\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><line x1=\"26.0\" y1=\"114.0\" x2=\"88.0\" y2=\"128.0\" stroke=\"#000000\" stroke-width=\"2.4\" marker-end=\"url(#arr-1804)\"/><text x=\"92\" y=\"138\" font-size=\"9.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"start\" fill=\"#000000\">b</text><line x1=\"20.0\" y1=\"120.0\" x2=\"126.0\" y2=\"110.0\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"4 3\"/><text x=\"50\" y=\"20\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"start\" fill=\"#000000\">no legal plan:</text><text x=\"50\" y=\"32\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">b outside the cone</text><line x1=\"138\" y1=\"10\" x2=\"138\" y2=\"134\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"3 3\"/><line x1=\"190.0\" y1=\"120.0\" x2=\"190.0\" y2=\"26.0\" stroke=\"#000000\" stroke-width=\"3\" marker-end=\"url(#arr-1804)\"/><text x=\"196\" y=\"34\" font-size=\"14\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"start\" fill=\"#000000\">\u221e</text><text x=\"192\" y=\"136\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">dual objective</text><text x=\"160\" y=\"62\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">unbounded \u2191</text></svg>",
    "drawingCaption": "If no legal flight plan exists (b outside the cone of walls), Farkas gives a heading that no wall blocks; along it the dual can be pushed up without bound.",
    "coreTranslation": [
      "<strong>What:</strong> Farkas' lemma says exactly one of (1) $Ax=b,\\ x\\ge0$ and (2) $A^Ty\\ge0,\\ b^Ty<0$ holds. For an LP, (1) is <em>primal feasibility</em>, and (2) is the <em>certificate</em> that it is infeasible.",
      "<strong>How:</strong> let $y$ solve (2) and put $d=-y$. Then $A^Td\\le0$ and $b^Td>0$. So if some $y_0$ is dual feasible ($A^Ty_0\\le c$), so is $y_0+td$ for every $t\\ge0$, and the dual objective $b^T(y_0+td)\\to+\\infty$.",
      "<strong>Why it matters:</strong> this is the proof that 'primal infeasible and dual feasible' forces 'dual unbounded'. Together with the symmetric case it gives the four outcomes of LP duality: both optimal with equal values, or one unbounded and the other infeasible, or both infeasible."
    ],
    "math": "$$A^Ty\\ge0,\\ b^Ty<0\\ \\Rightarrow\\ d=-y:\\ A^Td\\le0,\\ b^Td>0\\ \\Rightarrow\\ b^T(y_0+td)\\to+\\infty\\ \\ (t\\to\\infty)$$",
    "personalConnection": "<strong>The airplane analogy.</strong> If no legal flight plan exists (the primal is infeasible), Farkas gives a heading $y$ that no wall blocks along which you can keep improving forever, so the dual can be pushed without bound: infeasible primal means unbounded dual.",
    "examTrap": "Farkas' lemma is the engine behind Strong Duality in Linear Programming! Proving that the primal has no feasible solution is mathematically equivalent to exhibiting a certificate vector $y$ solving System 2.",
    "hint": "What does an infeasible primal force the dual to do?",
    "breakdown": [
      "<strong>$A^\\top y\\ge0,\\ b^\\top y\\lt0$ (Farkas):</strong> the walls cannot hold gravity.",
      "<strong>$d=-y$ then has $A^\\top d\\le0$ and $b^\\top d\\gt0$:</strong> a direction that keeps the dual feasible and increases its objective.",
      "<strong>$b^\\top(y_0+td)\\to\\infty$:</strong> the dual is unbounded."
    ]
  },
  {
    "id": 1805,
    "subject": "CMO",
    "topicId": "18_Linear_Programming_Duality_and_Polyhedral_Geometry",
    "topicTitle": "18 \u00b7 LP Duality & Polyhedral Geometry",
    "cardNumber": "06",
    "category": "LP ALGORITHMS",
    "highlighterClass": "highlight-indigo",
    "title": "The Simplex Method: Walking Along the Edges",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1805\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><polygon points=\"40,112 36,48 110,24 200,56 200,108\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"2\"/><path d=\"M36.0,48.0 L110.0,24.0 L200.0,56.0 L200.0,108.0\" fill=\"none\" stroke=\"#000000\" stroke-width=\"3.2\"/><circle cx=\"36.0\" cy=\"48.0\" r=\"3.2\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><circle cx=\"110.0\" cy=\"24.0\" r=\"3.2\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><circle cx=\"200.0\" cy=\"56.0\" r=\"3.2\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><circle cx=\"200.0\" cy=\"108.0\" r=\"3.2\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><g transform=\"translate(36.0 62.0) rotate(90) scale(0.6)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.00\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"34\" y=\"38\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"end\" fill=\"#000000\">9</text><text x=\"110\" y=\"18\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">7</text><text x=\"207\" y=\"54\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"start\" fill=\"#000000\">4</text><text x=\"207\" y=\"112\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"start\" fill=\"#000000\">1</text><text x=\"115.81759999999998\" y=\"138\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">hop to a lower neighbouring corner until none is lower</text></svg>",
    "drawingCaption": "At each corner the pilot looks at the neighbouring airports along the edges, hops to a lower one (altitudes 9, 7, 4, 1) and stops when no neighbour is lower.",
    "coreTranslation": [
      "<strong>What:</strong> Dantzig's simplex method (1947) moves along the 1-dimensional <em>edges</em> of the feasible polyhedron from one vertex (BFS) to an adjacent vertex with a better objective value.",
      "<strong>How:</strong> each <em>pivot</em> brings one non-basic variable into the basis and removes one basic variable. It stops when no neighbor improves the objective: that vertex is optimal.",
      "<strong>Why it matters:</strong> it returns an <em>exact</em> vertex solution and is superb in practice (typically linear in the number of constraints). Its worst case is exponential, as the Klee-Minty cube shows."
    ],
    "math": "$$x_B=B^{-1}b\\ \\ge0,\\ \\ x_N=0;\\quad \\text{optimal if all reduced costs}\\ \\ c_N^T-c_B^TB^{-1}N\\ \\ge\\ 0$$",
    "personalConnection": "<strong>The airplane analogy.</strong> At each airport corner the pilot looks at the neighbouring airports along the edges, hops to one that is lower, and stops when no neighbour is lower: that corner is the optimum.",
    "examTrap": "A degenerate vertex (a basic variable equals 0) lets simplex pivot without moving and, in rare cases, cycle. Bland's rule prevents that.",
    "hint": "How does the pilot know when to stop hopping between corners?",
    "breakdown": [
      "<strong>$x_B=B^{-1}b\\ge0,\\ x_N=0$:</strong> the current corner.",
      "<strong>Reduced cost $c_N^\\top-c_B^\\top B^{-1}N$:</strong> how the objective changes per unit of moving along each edge.",
      "<strong>If all reduced costs are $\\ge0$, no neighbouring corner is lower,</strong> so this corner is optimal."
    ]
  },
  {
    "id": 1808,
    "subject": "CMO",
    "topicId": "18_Linear_Programming_Duality_and_Polyhedral_Geometry",
    "topicTitle": "18 \u00b7 LP Duality & Polyhedral Geometry",
    "cardNumber": "07",
    "category": "LP ALGORITHMS",
    "highlighterClass": "highlight-indigo",
    "title": "Interior-Point Methods: The Central Path",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1808\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><polygon points=\"40,112 36,44 126,22 206,70 176,120\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"2\"/><path d=\"M36.0,44.0 L126.0,22.0 L206.0,70.0 L176.0,120.0\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.4\" stroke-dasharray=\"4 3\"/><path d=\"M110.0,74.0 L126.0,82.0 L146.0,94.0 L162.0,106.0 L176.0,118.0\" fill=\"none\" stroke=\"#000000\" stroke-width=\"3\"/><circle cx=\"110.0\" cy=\"74.0\" r=\"3\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><g transform=\"translate(144.0 90.0) rotate(40) scale(0.6)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.00\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><circle cx=\"176.0\" cy=\"120.0\" r=\"3.6\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"180\" y=\"112\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">optimum</text><text x=\"46\" y=\"128\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"start\" fill=\"#000000\">central path:</text><text x=\"100\" y=\"128\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"start\" fill=\"#000000\">stay off the walls</text><text x=\"120\" y=\"140\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">dashed: simplex edges</text></svg>",
    "drawingCaption": "Fly down the middle of the corridor (solid central path) instead of scraping along the walls from corner to corner (dashed), letting the clearance shrink to zero at the destination corner.",
    "coreTranslation": [
      "<strong>What:</strong> instead of walking along the edges, interior-point methods (Karmarkar 1984) stay <em>strictly inside</em> the feasible set and follow the <strong>central path</strong> $x(\\mu)$ as a barrier parameter $\\mu\\to0$.",
      "<strong>How:</strong> for each $\\mu>0$ solve $\\min c^Tx-\\mu\\sum_j\\ln x_j$ s.t. $Ax=b$. The log term repels the walls; shrinking $\\mu$ lets the iterate approach the optimal vertex. Primal-dual versions solve for $x$ and $y$ together by Newton's method.",
      "<strong>Why it matters:</strong> they take a few dozen iterations even for huge problems and have polynomial worst-case complexity $O(\\sqrt nL)$ iterations. The answer is only $\\epsilon$-optimal, so an exact vertex needs a 'crossover' step."
    ],
    "math": "$$x(\\mu)=\\arg\\min_{Ax=b,\\ x>0}\\Big\\{c^Tx-\\mu\\sum_{j=1}^n\\ln x_j\\Big\\}\\ \\xrightarrow{\\ \\mu\\to0\\ }\\ x^*$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Instead of scraping along the walls from corner to corner, fly down the centre of the corridor (the central path), a safe distance from every wall, and let the clearance shrink toward zero as you approach the destination corner.",
    "examTrap": "Simplex returns an exact vertex; interior-point methods return a point inside the polyhedron within \u03b5 of optimal. Know which one a question's 'basic solution' wording requires.",
    "hint": "What keeps the interior-point plane away from the walls?",
    "breakdown": [
      "<strong>$-\\mu\\sum\\ln x_j$ is the barrier:</strong> it blows up as any $x_j\\to0$, repelling the plane from the walls.",
      "<strong>$c^\\top x$ still pulls toward lower cost.</strong>",
      "<strong>The minimiser $x(\\mu)$ traces the central path;</strong> as $\\mu\\to0$ the barrier fades and the plane reaches the optimal corner."
    ]
  },
  {
    "id": 1806,
    "subject": "CMO",
    "topicId": "18_Linear_Programming_Duality_and_Polyhedral_Geometry",
    "topicTitle": "18 \u00b7 LP Duality & Polyhedral Geometry",
    "cardNumber": "08",
    "category": "WORKED BENCHMARK",
    "highlighterClass": "highlight-rose",
    "title": "Worked Benchmark: Primal-Dual Graphical Equality",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1806\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"16\" y1=\"78\" x2=\"224\" y2=\"78\" stroke=\"#000000\" stroke-width=\"1.6\" marker-end=\"url(#arr-1806)\"/><line x1=\"120\" y1=\"66\" x2=\"120\" y2=\"90\" stroke=\"#000000\" stroke-width=\"2.4\"/><text x=\"120\" y=\"70\" font-size=\"11\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">12</text><rect x=\"20\" y=\"52\" width=\"100\" height=\"22\" rx=\"0\" fill=\"#e5e7eb\" stroke=\"#000000\" stroke-width=\"1.2\"/><text x=\"70\" y=\"46\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">primal 3x\u2081+2x\u2082 \u2264 12</text><rect x=\"120\" y=\"82\" width=\"100\" height=\"22\" rx=\"0\" fill=\"#e5e7eb\" stroke=\"#000000\" stroke-width=\"1.2\"/><text x=\"170\" y=\"120\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">dual 5y\u2081+7y\u2082 \u2265 12</text><g transform=\"translate(120.0 36.0) rotate(90) scale(0.6)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.00\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"70\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">(2,3)</text><text x=\"176\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">(1,1)</text><text x=\"120\" y=\"12\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">cockpit and tower agree</text></svg>",
    "drawingCaption": "Every feasible primal value sits at or below 12 and every feasible dual value at or above 12; they meet at exactly 12 (primal at (2,3), dual at (1,1)).",
    "coreTranslation": [
      "<strong>Problem:</strong> maximize $3x_1+2x_2$ s.t. $x_1+x_2\\le5,\\ 2x_1+x_2\\le7,\\ x\\ge0$. The best vertex is $x^*=(2,3)$, value $3(2)+2(3)=12$ (both constraints are tight there).",
      "<strong>Dual:</strong> minimize $5y_1+7y_2$ s.t. $y_1+2y_2\\ge3,\\ y_1+y_2\\ge2,\\ y\\ge0$. Complementary slackness: since $x_1^*,x_2^*>0$ both dual constraints must be equalities: $y_1+2y_2=3,\\ y_1+y_2=2$, so $y_2=1,\\ y_1=1$ (both $\\ge0$ \u2713).",
      "<strong>Check:</strong> dual value $5(1)+7(1)=12$ equals the primal value, which proves $x^*$ is optimal. Both primal constraints are tight and both $y_i>0$, consistent with $y_i(\\text{slack}_i)=0$."
    ],
    "math": "$$z^* = 3(2) + 2(3) = 12 = 5(1) + 7(1) = w^* \\quad (\\text{Complementary Slackness } x_j > 0 \\implies A_j^T y = c_j)$$",
    "personalConnection": "<strong>The airplane analogy.</strong> The pilot in the cockpit and the tower with its price list reach the same total cost: the primal and dual optimum are equal, the strong duality of LP.",
    "examTrap": "Remember that if the primal is a MAXIMIZATION problem, the dual is a MINIMIZATION problem, and primal constraints $\\le$ become dual variables $y \\ge 0$. Watch the direction of the inequalities!",
    "hint": "Where do the cockpit's and the tower's numbers meet?",
    "breakdown": [
      "<strong>Primal:</strong> $3(2)+2(3)=12$ at $(2,3)$. <strong>Dual:</strong> $5(1)+7(1)=12$ at $(1,1)$.",
      "<strong>Every feasible primal value is at most 12 and every feasible dual value at least 12;</strong> they meet exactly at 12.",
      "<strong>Complementary slackness explains why:</strong> positive $x_j$ forces the matching dual constraint to be tight."
    ]
  },
  {
    "id": 1901,
    "subject": "CMO",
    "topicId": "19_Penalty_and_Barrier_Methods",
    "topicTitle": "19 \u00b7 Penalty & Barrier Methods",
    "cardNumber": "01",
    "category": "EXTERIOR PENALTY",
    "highlighterClass": "highlight-cyan",
    "title": "Quadratic Exterior Penalty Function",
    "textbookImg": "assets/luenberger_fig13_1.png",
    "textbookRef": "Luenberger & Ye (4th ed), Sect. 13.1, Fig. 13.1 (p. 399)",
    "drawingCaption": "Crossing into forbidden airspace triggers a fine c\u00b7max(0,g)\u00b2 that grows quadratically; inside legal airspace there is no fine at all.",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1901\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"20\" y1=\"112\" x2=\"226\" y2=\"112\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-1901)\"/><line x1=\"120\" y1=\"118\" x2=\"120\" y2=\"14\" stroke=\"#000000\" stroke-width=\"1.4\" stroke-dasharray=\"4 3\"/><path d=\"M20.0,112.0 L23.4,112.0 L26.9,112.0 L30.3,112.0 L33.7,112.0 L37.2,112.0 L40.6,112.0 L44.0,112.0 L47.5,112.0 L50.9,112.0 L54.3,112.0 L57.8,112.0 L61.2,112.0 L64.6,112.0 L68.1,112.0 L71.5,112.0 L74.9,112.0 L78.4,112.0 L81.8,112.0 L85.2,112.0 L88.7,112.0 L92.1,112.0 L95.5,112.0 L99.0,112.0 L102.4,112.0 L105.8,112.0 L109.3,112.0 L112.7,112.0 L116.1,112.0 L119.6,112.0 L123.0,111.9 L126.4,111.5 L129.9,110.8 L133.3,109.9 L136.7,108.6 L140.2,107.1 L143.6,105.3 L147.0,103.2 L150.5,100.9 L153.9,98.2 L157.3,95.3 L160.8,92.1 L164.2,88.6 L167.6,84.8 L171.1,80.7 L174.5,76.4 L177.9,71.7 L181.4,66.8 L184.8,61.6 L188.2,56.1 L191.7,50.4 L195.1,44.3 L198.5,38.0 L202.0,31.4 L205.4,24.5 L208.8,17.3 L212.3,9.8 L215.7,2.1 L219.1,-5.9 L222.6,-14.2 L226.0,-22.8\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.8\"/><rect x=\"20\" y=\"118\" width=\"100\" height=\"14\" rx=\"0\" fill=\"#eef0f4\" stroke=\"#000000\" stroke-width=\"0\"/><text x=\"70\" y=\"128\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">legal airspace g \u2264 0</text><text x=\"176\" y=\"128\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">forbidden</text><g transform=\"translate(60.0 96.0) rotate(0) scale(0.8)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.50\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><g transform=\"translate(176.0 62.0) rotate(180) scale(0.8)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.50\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"60\" y=\"80\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">no fine</text><text x=\"196\" y=\"36\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">fine c\u00b7max(0,g)\u00b2</text><text x=\"18\" y=\"140\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\"></text></svg>",
    "coreTranslation": [
      "<strong>Core Philosophy:</strong> Exterior penalty methods approximate a constrained problem by an <strong>unconstrained problem</strong> that places a severe penalty on infeasible points outside $\\Omega$:",
      "$$q(c, x) = f(x) + c P(x), \\quad \\text{where } P(x) = \\frac{1}{2} \\sum_{i=1}^p h_i(x)^2 + \\frac{1}{2} \\sum_{j=1}^m [\\max(0, g_j(x))]^2$$",
      "<strong>Convergence Mechanics:</strong> As penalty parameter $c_k \\to \\infty$, the sequence of unconstrained minimizers $x(c_k)$ approaches the boundary from the <strong>exterior (infeasible side)</strong>, converging to the exact constrained minimizer $x^*$."
    ],
    "math": "$$\\min_{x \\in \\mathbb{R}^n} q(c_k, x) = f(x) + \\frac{c_k}{2} \\sum_{i=1}^p h_i(x)^2 + \\frac{c_k}{2} \\sum_{j=1}^m [\\max(0, g_j(x))]^2 \\xrightarrow{c_k \\to \\infty} x^*$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Restricted airspace with fines. Inside legal airspace ($g\\le0$) you fly free; the moment you cross into the forbidden zone, the fine $c\\,[\\max(0,g)]^2$ grows quadratically. As the fine stiffens ($c\\to\\infty$) you are forced back to the boundary.",
    "examTrap": "The quadratic penalty function for inequalities $[\\max(0, g(x))]^2$ is only ONCE continuously differentiable ($C^1$)! Its second derivative has a discontinuous jump across the boundary $g(x) = 0$, which can impair pure Newton methods.",
    "hint": "How big is the fine for a given amount of violation?",
    "breakdown": [
      "<strong>$\\max(0,g_j)^2$:</strong> no fine inside the airspace, a quadratic fine outside; squaring keeps it smooth at the wall.",
      "<strong>$\\tfrac{c_k}2h_i^2$:</strong> equality walls are fined for any deviation in either direction.",
      "<strong>As $c_k\\to\\infty$ the fine becomes so steep</strong> that the unconstrained minimiser is forced onto the boundary."
    ]
  },
  {
    "id": 1902,
    "subject": "CMO",
    "topicId": "19_Penalty_and_Barrier_Methods",
    "topicTitle": "19 \u00b7 Penalty & Barrier Methods",
    "cardNumber": "02",
    "category": "INTERIOR BARRIER",
    "highlighterClass": "highlight-amber",
    "title": "Logarithmic & Inverse Barrier Methods",
    "textbookImg": "assets/luenberger_fig13_3.png",
    "textbookRef": "Luenberger & Ye (4th ed), Sect. 13.2, Fig. 13.3 (p. 402)",
    "drawingCaption": "An invisible repulsive field around the mountain: the closer the plane gets to the wall the more the barrier blows up, so it always flies strictly inside legal airspace.",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1902\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"190.0\" y1=\"10.0\" x2=\"190.0\" y2=\"120.0\" stroke=\"#000000\" stroke-width=\"2.4\"/><line x1=\"190.0\" y1=\"15.5\" x2=\"197.0\" y2=\"15.5\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"190.0\" y1=\"26.5\" x2=\"197.0\" y2=\"26.5\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"190.0\" y1=\"37.5\" x2=\"197.0\" y2=\"37.5\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"190.0\" y1=\"48.5\" x2=\"197.0\" y2=\"48.5\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"190.0\" y1=\"59.5\" x2=\"197.0\" y2=\"59.5\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"190.0\" y1=\"70.5\" x2=\"197.0\" y2=\"70.5\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"190.0\" y1=\"81.5\" x2=\"197.0\" y2=\"81.5\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"190.0\" y1=\"92.5\" x2=\"197.0\" y2=\"92.5\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"190.0\" y1=\"103.5\" x2=\"197.0\" y2=\"103.5\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"190.0\" y1=\"114.5\" x2=\"197.0\" y2=\"114.5\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"20\" y1=\"118\" x2=\"192\" y2=\"118\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-1902)\"/><path d=\"M20.0,112.0 L27.0,111.1 L34.0,110.1 L41.0,109.1 L48.0,108.0 L55.0,106.9 L62.0,105.8 L69.0,104.5 L76.0,103.2 L83.0,101.8 L90.0,100.3 L97.0,98.7 L104.0,97.0 L111.0,95.1 L118.0,93.1 L125.0,90.8 L132.0,88.3 L139.0,85.5 L146.0,82.3 L153.0,78.5 L160.0,73.8 L167.0,68.0 L174.0,60.0 L181.0,47.4\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.8\"/><g transform=\"translate(60.0 96.0) rotate(0) scale(0.8)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.50\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"120\" y=\"138\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u2212\u03bc ln(\u2212g) \u2192 \u221e at the wall</text><text x=\"150\" y=\"20\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"end\" fill=\"#000000\">field repels</text></svg>",
    "coreTranslation": [
      "<strong>Interior Point Barrier:</strong> Unlike penalty methods (which approach from outside), barrier methods generate iterates strictly from the <strong>interior</strong> of the feasible set $\\mathcal{S}^\\circ = \\{x : g_j(x) < 0\\}$:",
      "$$r(c, x) = f(x) + \\frac{1}{c} B(x), \\quad B(x) = -\\sum_{j=1}^m \\ln(-g_j(x)) \\quad (\\text{or } \\sum \\frac{-1}{g_j(x)})$$",
      "<strong>Infinite Boundary Repulsion:</strong> As $x$ approaches the boundary ($g_j(x) \\to 0^-$), $\\ln(-g_j(x)) \\to -\\infty$, creating an <strong>infinite vertical energy wall</strong> that physically prevents iterates from ever becoming infeasible. As $c \\to \\infty$, the unconstrained minimizers converge to $x^*$ from the inside!"
    ],
    "math": "$$B(x) = -\\sum_{j=1}^m \\ln(-g_j(x)) \\implies \\lim_{g_j(x) \\to 0} B(x) = +\\infty, \\quad x(c) = \\arg\\min_{x \\in \\mathcal{S}^\\circ} \\left\\{ f(x) + \\frac{1}{c} B(x) \\right\\}$$",
    "personalConnection": "<strong>The airplane analogy.</strong> An invisible repulsive field around the mountains: the closer you get to a wall, the more the barrier $-\\mu\\ln(-g)$ blows up, so you can never touch the boundary and always fly strictly inside legal airspace.",
    "examTrap": "Barrier methods CANNOT handle equality constraints $h_i(x) = 0$! Because equality constraints have no strict interior ($\\{x : h_i(x) < 0\\}$ is empty). Equalities must be handled via penalties, projection, or Lagrange multipliers.",
    "hint": "What stops the plane from ever touching the wall?",
    "breakdown": [
      "<strong>$-\\ln(-g_j)$ is finite inside</strong> ($g_j\\lt0$) and $\\to+\\infty$ as $g_j\\to0^-$.",
      "<strong>Adding $\\frac1cB(x)$ to $f$ keeps the plane strictly inside;</strong> as $c$ grows the barrier weakens and the plane approaches the boundary from inside.",
      "<strong>Needs a strict interior:</strong> that is Slater's condition again."
    ]
  },
  {
    "id": 1903,
    "subject": "CMO",
    "topicId": "19_Penalty_and_Barrier_Methods",
    "topicTitle": "19 \u00b7 Penalty & Barrier Methods",
    "cardNumber": "03",
    "category": "ILL-CONDITIONING",
    "highlighterClass": "highlight-emerald",
    "title": "Hessian Ill-Conditioning in Penalty Methods",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1903\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><ellipse cx=\"120\" cy=\"74\" rx=\"106\" ry=\"10\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.4\" transform=\"rotate(-6 120 74)\"/><ellipse cx=\"120\" cy=\"74\" rx=\"78\" ry=\"7\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.4\" transform=\"rotate(-6 120 74)\"/><ellipse cx=\"120\" cy=\"74\" rx=\"50\" ry=\"4.5\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.4\" transform=\"rotate(-6 120 74)\"/><path d=\"M30.0,63.0 L52.0,85.0 L74.0,67.0 L98.0,88.0 L122.0,71.0 L146.0,87.0 L170.0,70.0 L196.0,84.0\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.4\"/><g transform=\"translate(206.0 84.0) rotate(20) scale(0.6)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.00\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"120\" y=\"22\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">huge fine c: razor-thin canyon</text><text x=\"120\" y=\"128\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">zig-zag between the walls, slow progress</text><text x=\"120\" y=\"140\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">cond(Hessian) \u2248 c</text></svg>",
    "drawingCaption": "With a huge fine the valley becomes a razor-thin canyon: stiff across, flat along. The plane zig-zags between the walls instead of making forward progress.",
    "coreTranslation": [
      "<strong>What:</strong> as the penalty weight $c\\to\\infty$, the penalty function becomes extremely ill-conditioned: its Hessian is $\\nabla^2f+c\\sum\\nabla h_i\\nabla h_i^T+c\\sum h_i\\nabla^2h_i$.",
      "<strong>How:</strong> the $p$ directions normal to the constraints get curvature that grows like $c$, while the $n-p$ tangent directions keep $O(1)$ curvature. So $\\kappa=\\lambda_{\\max}/\\lambda_{\\min}\\sim O(c)\\to\\infty$: a long, narrow canyon.",
      "<strong>Why it matters:</strong> gradient descent zig-zags and Newton systems lose accuracy. So raise $c$ gradually (e.g. $c_{k+1}=10c_k$) and warm-start each subproblem from the previous solution."
    ],
    "math": "$$\\kappa(\\nabla^2 q(c, x)) = \\frac{\\lambda_{\\max}}{\\lambda_{\\min}} \\approx \\mathcal{O}(c) \\xrightarrow{c \\to \\infty} \\infty \\implies \\text{Catastrophic Numerical Instability}$$",
    "personalConnection": "<strong>The airplane analogy.</strong> With a huge fine $c$ the valley becomes a razor-thin canyon: extremely stiff across the wall and flat along the runway, so the pilot zig-zags between the canyon walls instead of making forward progress: the Hessian has condition number growing with $c$.",
    "examTrap": "Do NOT increase penalty parameter $c$ too fast! Classical penalty codes multiply $c_{k+1} = 10 c_k$ slowly and warm-start each minimization from the previous iterate $x_k$ to survive the severe ill-conditioning.",
    "hint": "Why does a huge fine make the pilot zig-zag?",
    "breakdown": [
      "<strong>Across the wall the curvature grows like $c$;</strong> along the runway it stays $O(1)$.",
      "<strong>$\\kappa=\\lambda_{\\max}/\\lambda_{\\min}\\approx O(c)\\to\\infty$:</strong> the valley becomes a razor-thin canyon.",
      "<strong>Gradient and Newton steps then lose accuracy:</strong> catastrophic ill-conditioning."
    ]
  },
  {
    "id": 1904,
    "subject": "CMO",
    "topicId": "19_Penalty_and_Barrier_Methods",
    "topicTitle": "19 \u00b7 Penalty & Barrier Methods",
    "cardNumber": "04",
    "category": "MULTIPLIER RECOVERY",
    "highlighterClass": "highlight-violet",
    "title": "Lagrange Multiplier Recovery from Penalty Iterates",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1904\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><rect x=\"150\" y=\"10\" width=\"80\" height=\"126\" rx=\"0\" fill=\"#d1d5db\" stroke=\"#000000\" stroke-width=\"0\"/><line x1=\"150.0\" y1=\"10.0\" x2=\"150.0\" y2=\"136.0\" stroke=\"#000000\" stroke-width=\"2.4\"/><line x1=\"150.0\" y1=\"14.5\" x2=\"157.0\" y2=\"14.5\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"150.0\" y1=\"23.5\" x2=\"157.0\" y2=\"23.5\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"150.0\" y1=\"32.5\" x2=\"157.0\" y2=\"32.5\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"150.0\" y1=\"41.5\" x2=\"157.0\" y2=\"41.5\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"150.0\" y1=\"50.5\" x2=\"157.0\" y2=\"50.5\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"150.0\" y1=\"59.5\" x2=\"157.0\" y2=\"59.5\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"150.0\" y1=\"68.5\" x2=\"157.0\" y2=\"68.5\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"150.0\" y1=\"77.5\" x2=\"157.0\" y2=\"77.5\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"150.0\" y1=\"86.5\" x2=\"157.0\" y2=\"86.5\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"150.0\" y1=\"95.5\" x2=\"157.0\" y2=\"95.5\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"150.0\" y1=\"104.5\" x2=\"157.0\" y2=\"104.5\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"150.0\" y1=\"113.5\" x2=\"157.0\" y2=\"113.5\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"150.0\" y1=\"122.5\" x2=\"157.0\" y2=\"122.5\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"150.0\" y1=\"131.5\" x2=\"157.0\" y2=\"131.5\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"130\" y1=\"10\" x2=\"130\" y2=\"136\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"4 3\"/><text x=\"130\" y=\"144\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">boundary</text><g transform=\"translate(88.0 72.0) rotate(0) scale(0.9)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.33\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><path d=\"M100.0,72.0 L108.0,64.0 L113.0,80.0 L118.0,64.0 L123.0,80.0 L128.0,64.0 L133.0,80.0 L138.0,64.0 L143.0,80.0 L150.0,72.0\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.8\"/><line x1=\"148.0\" y1=\"100.0\" x2=\"100.0\" y2=\"100.0\" stroke=\"#000000\" stroke-width=\"2.6\" marker-end=\"url(#arr-1904)\"/><text x=\"124\" y=\"114\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u03bb \u2248 c\u00b7h</text><text x=\"130\" y=\"24\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"end\" fill=\"#000000\">sinks a little: h(x)</text><text x=\"120\" y=\"134\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\"></text></svg>",
    "drawingCaption": "The plane sinks slightly into the forbidden zone like a foot on a spring scale; stiffness c times the depth h gives the wall's push, the multiplier.",
    "coreTranslation": [
      "<strong>What:</strong> even though penalty iterates are slightly infeasible, they hand you good estimates of the Lagrange multipliers for free: $\\lambda_i^{(k)}=c_k\\,h_i(x_k)$.",
      "<strong>How:</strong> at the minimizer $x_k$ of $q(c_k,x)=f+\\tfrac{c_k}2\\sum h_i^2$, $\\nabla f(x_k)+\\sum[c_kh_i(x_k)]\\nabla h_i(x_k)=0$. Compare with KKT, $\\nabla f+\\sum\\lambda_i^*\\nabla h_i=0$: the bracket plays the role of $\\lambda_i$. For inequalities, $\\mu_j^{(k)}=c_k\\max(0,g_j(x_k))$.",
      "<strong>Why it matters:</strong> since $\\lambda^{(k)}\\to\\lambda^*$ (finite) while $c_k\\to\\infty$, the constraint violation is $h_i(x_k)\\approx\\lambda_i^*/c_k$: it shrinks like $1/c_k$. This is also the idea behind the augmented Lagrangian."
    ],
    "math": "$$\\lambda_i^{(k)} = c_k h_i(x(c_k)) \\xrightarrow{c_k \\to \\infty} \\lambda_i^*, \\quad \\mu_j^{(k)} = c_k \\max(0, g_j(x(c_k))) \\xrightarrow{c_k \\to \\infty} \\mu_j^*$$",
    "personalConnection": "<strong>The airplane analogy.</strong> At each penalty iterate the plane sinks slightly into the forbidden zone. Fine times depth gives the wall's push force: $\\lambda^*\\approx c\\,\\max(0,g)$ or $c\\,h(x_k)$ for equalities, so the multiplier is recovered for free.",
    "examTrap": "Notice that because $\\lambda_k \\to \\lambda^*$ (a finite number) while $c_k \\to \\infty$, the constraint violation must decay like $\\mathcal{O}(1/c_k)$: $h_i(x_k) \\approx \\frac{\\lambda_i^*}{c_k}$. This proves the constraint error is inversely proportional to $c$.",
    "hint": "How do you read the wall's push from the penalty iterates?",
    "breakdown": [
      "<strong>$h_i(x(c_k))$ = how far the plane sinks into the forbidden zone.</strong>",
      "<strong>Multiplying by the stiffness $c_k$ gives the restoring force,</strong> like a spring: $\\lambda_i^{(k)}=c_kh_i$.",
      "<strong>As $c_k\\to\\infty$ the depth $\\to0$ but the product converges to the true multiplier $\\lambda^*_i$.</strong>"
    ]
  },
  {
    "id": 1905,
    "subject": "CMO",
    "topicId": "19_Penalty_and_Barrier_Methods",
    "topicTitle": "19 \u00b7 Penalty & Barrier Methods",
    "cardNumber": "05",
    "category": "AUGMENTED LAGRANGIAN",
    "highlighterClass": "highlight-indigo",
    "title": "Augmented Lagrangian (Method of Multipliers)",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1905\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"206.0\" y1=\"10.0\" x2=\"206.0\" y2=\"134.0\" stroke=\"#000000\" stroke-width=\"2.4\"/><line x1=\"206.0\" y1=\"15.6\" x2=\"213.0\" y2=\"15.6\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"206.0\" y1=\"26.9\" x2=\"213.0\" y2=\"26.9\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"206.0\" y1=\"38.2\" x2=\"213.0\" y2=\"38.2\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"206.0\" y1=\"49.5\" x2=\"213.0\" y2=\"49.5\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"206.0\" y1=\"60.7\" x2=\"213.0\" y2=\"60.7\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"206.0\" y1=\"72.0\" x2=\"213.0\" y2=\"72.0\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"206.0\" y1=\"83.3\" x2=\"213.0\" y2=\"83.3\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"206.0\" y1=\"94.5\" x2=\"213.0\" y2=\"94.5\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"206.0\" y1=\"105.8\" x2=\"213.0\" y2=\"105.8\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"206.0\" y1=\"117.1\" x2=\"213.0\" y2=\"117.1\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"206.0\" y1=\"128.4\" x2=\"213.0\" y2=\"128.4\" stroke=\"#000000\" stroke-width=\"1.1\"/><line x1=\"20\" y1=\"44\" x2=\"204\" y2=\"44\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"2 3\"/><line x1=\"20\" y1=\"100\" x2=\"204\" y2=\"100\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"2 3\"/><circle cx=\"30.0\" cy=\"44.0\" r=\"2.8\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><circle cx=\"100.0\" cy=\"44.0\" r=\"2.8\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><circle cx=\"148.0\" cy=\"44.0\" r=\"2.8\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><circle cx=\"172.0\" cy=\"44.0\" r=\"2.8\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><circle cx=\"186.0\" cy=\"44.0\" r=\"2.8\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><circle cx=\"194.0\" cy=\"44.0\" r=\"2.8\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><text x=\"110\" y=\"24\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">penalty: creeps toward the wall, never lands</text><circle cx=\"30.0\" cy=\"100.0\" r=\"2.8\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><circle cx=\"120.0\" cy=\"100.0\" r=\"2.8\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><circle cx=\"206.0\" cy=\"100.0\" r=\"2.8\" fill=\"#000000\" stroke=\"#000000\" stroke-width=\"1.5\"/><g transform=\"translate(160.0 86.0) rotate(0) scale(0.55)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.18\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"110\" y=\"120\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">augmented: adjust \u03bb and land exactly</text><text x=\"110\" y=\"134\" font-size=\"8\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">with only a moderate fine c</text></svg>",
    "drawingCaption": "Ordinary penalty only creeps toward the wall as c grows. The augmented Lagrangian also adjusts the standing reservation \u03bb and lands on the boundary with a moderate fine.",
    "coreTranslation": [
      "<strong>What:</strong> the augmented Lagrangian $\\mathcal{L}_c(x,\\lambda)=f+\\lambda^Th+\\tfrac c2\\|h\\|^2$ (Hestenes\u2013Powell) adds a multiplier term to the quadratic penalty.",
      "<strong>How:</strong> alternate (1) minimize $\\mathcal{L}_c(x,\\lambda_k)$ over $x$; (2) update the multiplier by $\\lambda_{k+1}=\\lambda_k+c\\,h(x_k)$ (gradient <em>ascent</em> on the dual, with a plus sign).",
      "<strong>Why it matters:</strong> the multiplier does most of the work of balancing $-\\nabla f$, so $c$ only has to be large enough to make $\\mathcal{L}_c$ locally convex, a <em>finite</em> value. No $c\\to\\infty$ means no ill-conditioning."
    ],
    "math": "$$\\lambda_{k+1} = \\lambda_k + c_k h(x_k) \\quad (\\text{First-Order Dual Multiplier Update without Matrix Inverses})$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Ordinary penalty needs the fine to grow forever ($c\\to\\infty$). The augmented Lagrangian lets the tower also adjust a standing reservation $\\lambda$ so that the plane lands exactly on the boundary with only a moderate fine.",
    "examTrap": "The multiplier update is $\\lambda_{k+1} = \\lambda_k + c_k h(x_k)$ (NOT minus!). Because $h(x) = \\nabla_\\lambda \\mathcal{L}_c$ is the exact gradient of the dual function with respect to $\\lambda$, this update is pure gradient ascent on the dual.",
    "hint": "What does the tower adjust so the fine does not have to grow forever?",
    "breakdown": [
      "<strong>$h(x_k)$ = remaining violation after the current leg.</strong>",
      "<strong>$c_kh(x_k)$ = the correction the multiplier needs:</strong> the same force-from-depth reading as penalty recovery.",
      "<strong>$\\lambda_{k+1}=\\lambda_k+c_kh(x_k)$</strong> converges without sending $c_k\\to\\infty$, so the problem stays well conditioned."
    ]
  },
  {
    "id": 1906,
    "subject": "CMO",
    "topicId": "19_Penalty_and_Barrier_Methods",
    "topicTitle": "19 \u00b7 Penalty & Barrier Methods",
    "cardNumber": "06",
    "category": "WORKED BENCHMARK",
    "highlighterClass": "highlight-rose",
    "title": "Worked Benchmark: Augmented Lagrangian Sequence",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\"><defs><marker id=\"arr-1906\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/></marker></defs><line x1=\"14\" y1=\"124\" x2=\"226\" y2=\"124\" stroke=\"#000000\" stroke-width=\"1.4\" marker-end=\"url(#arr-1906)\"/><line x1=\"14\" y1=\"36\" x2=\"226\" y2=\"36\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"4 3\"/><text x=\"224\" y=\"32\" font-size=\"9.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"end\" fill=\"#000000\">\u03bb*</text><rect x=\"26\" y=\"104\" width=\"24\" height=\"20\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"38\" y=\"136\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u03bb\u2080</text><rect x=\"62\" y=\"72\" width=\"24\" height=\"52\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"74\" y=\"136\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u03bb\u2081</text><rect x=\"98\" y=\"54\" width=\"24\" height=\"70\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"110\" y=\"136\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u03bb\u2082</text><rect x=\"134\" y=\"45\" width=\"24\" height=\"79\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"146\" y=\"136\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u03bb\u2083</text><rect x=\"170\" y=\"40\" width=\"24\" height=\"84\" rx=\"0\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.6\"/><text x=\"182\" y=\"136\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">\u03bb\u2084</text><text x=\"120\" y=\"20\" font-size=\"9\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"bold\" text-anchor=\"middle\" fill=\"#000000\">\u03bb\u2096\u208a\u2081 = \u03bb\u2096 + c\u00b7h(x\u2096)</text><g transform=\"translate(210.0 60.0) rotate(180) scale(0.6)\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"2.00\" stroke-linejoin=\"round\"><polygon points=\"12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2\"/><polygon points=\"3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10\"/><polygon points=\"-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5\"/></g><text x=\"120\" y=\"32\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"normal\" font-weight=\"normal\" text-anchor=\"middle\" fill=\"#000000\">small tuning turns, not brute force</text></svg>",
    "drawingCaption": "The tower turns the fine-tuning screw by a small correction c\u00b7h(x\u2096) each leg, so \u03bb\u2096 climbs to \u03bb* while the fine stays moderate.",
    "coreTranslation": [
      "<strong>Problem:</strong> minimize $x_1^2+x_2^2$ s.t. $h(x)=x_1+x_2-2=0$ (solution $x^*=(1,1)$, $\\lambda^*=-2$). Use $\\mathcal{L}_c=x_1^2+x_2^2+\\lambda h+\\tfrac c2h^2$ with $c=2$, $\\lambda_0=0$. By symmetry set $x_1=x_2=t$: $\\partial_x\\mathcal{L}=2t+\\lambda+2(2t-2)=0\\Rightarrow t=\\frac{4-\\lambda}{6}$.",
      "<strong>Iteration 1:</strong> $\\lambda_0=0$ gives $t=\\tfrac23$, so $h=-\\tfrac23$ and $\\lambda_1=0+2(-\\tfrac23)=-\\tfrac43$. <strong>Iteration 2:</strong> $t=\\frac{4+4/3}{6}=\\tfrac89$, $h=-\\tfrac29$, $\\lambda_2=-\\tfrac43-\\tfrac49=-\\tfrac{16}9$. <strong>Iteration 3:</strong> $t=\\tfrac{26}{27}$.",
      "<strong>Pattern:</strong> $x^{(k)}=1-3^{-(k+1)}$ and $\\lambda_k-\\lambda^*=-2\\cdot3^{-k}$: the error drops by a factor of 3 each update while $c$ stays at 2."
    ],
    "math": "$$\\lambda_0=0\\to x^{(0)}=\\Big(\\tfrac23,\\tfrac23\\Big);\\ \\ \\lambda_1=-\\tfrac43\\to x^{(1)}=\\Big(\\tfrac89,\\tfrac89\\Big);\\ \\ \\lambda_2=-\\tfrac{16}9\\to x^{(2)}=\\Big(\\tfrac{26}{27},\\tfrac{26}{27}\\Big)\\to(1,1),\\ \\lambda^*=-2$$",
    "personalConnection": "<strong>The airplane analogy.</strong> Instead of ever-tighter fines, the tower nudges the reservation $\\lambda_{k+1}=\\lambda_k+c\\,h(x_k)$ by small corrections until the plane touches down on the boundary exactly: tuning, not brute force.",
    "examTrap": "Compare with the plain quadratic penalty, whose minimizer is x = c/(1+c)\u00b7(1,1): the error is 1/(1+c), so 1% accuracy needs c \u2248 100 (and a terribly conditioned Hessian). The augmented Lagrangian reaches 0.4% with c = 2 after 4 multiplier updates.",
    "hint": "How does $\\lambda$ climb to its target in the worked sequence?",
    "breakdown": [
      "<strong>$\\lambda_0=0$ gives $x^{(0)}=(2/3,2/3)$,</strong> a plane still short of the boundary.",
      "<strong>$\\lambda_1=-4/3$ gives $x^{(1)}=(8/9,8/9)$, and $\\lambda_2=-16/9$ is next:</strong> each update closes a fixed fraction of the remaining gap.",
      "<strong>The multiplier converges to $\\lambda^*$ and the plane lands on the constraint</strong> with the penalty $c$ held fixed."
    ]
  },
  {
    "id": 20101,
    "subject": "LAA",
    "topicId": "01_Vector_Spaces_Subspaces_and_Direct_Sums",
    "topicTitle": "01 \u00b7 Vector Spaces, Subspaces & Direct Sums",
    "cardNumber": "01",
    "category": "VECTOR SPACE FOUNDATIONS",
    "highlighterClass": "highlight-cyan",
    "title": "Subspace 3-Step Verification Test",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\">\n  <defs>\n    <marker id=\"arr-laa1\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\">\n      <path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/>\n    </marker>\n  </defs>\n  <!-- Ambient Box -->\n  <rect x=\"25\" y=\"20\" width=\"190\" height=\"105\" rx=\"8\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"3,3\"/>\n  <text x=\"35\" y=\"34\" fill=\"#000000\" font-size=\"8.5\" font-family=\"serif\" font-style=\"italic\">Ambient V = \u211d\u00b3</text>\n  <!-- Subspace Plane Passing through Origin -->\n  <polygon points=\"45,105 110,35 195,45 130,115\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.8\"/>\n  <!-- Origin 0 -->\n  <circle cx=\"120\" cy=\"75\" r=\"3.5\" fill=\"#000000\"/>\n  <text x=\"120\" y=\"65\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" font-weight=\"bold\" text-anchor=\"middle\">0 \u2208 U</text>\n  <!-- Vectors u and v -->\n  <line x1=\"120\" y1=\"75\" x2=\"160\" y2=\"58\" stroke=\"#000000\" stroke-width=\"1.8\" marker-end=\"url(#arr-laa1)\"/>\n  <text x=\"165\" y=\"56\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\">u</text>\n  <line x1=\"120\" y1=\"75\" x2=\"95\" y2=\"98\" stroke=\"#000000\" stroke-width=\"1.8\" marker-end=\"url(#arr-laa1)\"/>\n  <text x=\"88\" y=\"106\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\">v</text>\n  <!-- Sum vector u + v -->\n  <line x1=\"120\" y1=\"75\" x2=\"140\" y2=\"82\" stroke=\"#000000\" stroke-width=\"2\" marker-end=\"url(#arr-laa1)\"/>\n  <text x=\"145\" y=\"94\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" font-weight=\"bold\">u + v \u2208 U</text>\n  <text x=\"120\" y=\"134\" fill=\"#000000\" font-size=\"8.5\" font-family=\"sans-serif\" text-anchor=\"middle\">Plane U passes through 0 and is closed under addition &amp; scaling</text>\n</svg>",
    "drawingCaption": "Subspace Test: Plane U must pass through the origin 0 and be closed under vector addition and scaling",
    "coreTranslation": [
      "A subset $U \\subset V$ of a vector space over field $\\mathbb{F}$ is a <strong>Subspace</strong> if and only if it satisfies the <strong>3-Step Test</strong>:",
      "<strong>1. Additive Identity:</strong> $0 \\in U$. (If the origin is missing, $U$ fails immediately).",
      "<strong>2. Closure under Addition:</strong> $u, v \\in U \\implies u + v \\in U$. <strong>3. Closure under Scalar Mult:</strong> $u \\in U, c \\in \\mathbb{F} \\implies c u \\in U$."
    ],
    "math": "$$U \\le V \\iff 0 \\in U \\quad \\text{and} \\quad \\alpha u + \\beta v \\in U \\quad \\forall \\, u, v \\in U, \\; \\alpha, \\beta \\in \\mathbb{F}$$",
    "personalConnection": "A flat sheet of glass slicing through 3D space: it is only a valid subspace if the exact origin $(0, 0, 0)$ is drilled through the glass. An affine plane displaced by even $10^{-6}$ fails the zero test.",
    "examTrap": "Testing if an affine plane (e.g. $W = \\{(x, y, z) : x + 2y - z = 4\\}$) is a subspace. Answer: NO! $(0,0,0) \\notin W$. It is an affine manifold, not a linear subspace."
  },
  {
    "id": 20102,
    "subject": "LAA",
    "topicId": "01_Vector_Spaces_Subspaces_and_Direct_Sums",
    "topicTitle": "01 \u00b7 Vector Spaces, Subspaces & Direct Sums",
    "cardNumber": "02",
    "category": "DIRECT SUMS",
    "highlighterClass": "highlight-amber",
    "title": "Sum of Subspaces vs. Direct Sum U\u2081 \u2295 U\u2082",
    "textbookImg": "assets/meyer_fig5_13_1.png",
    "textbookRef": "Carl Meyer, Matrix Analysis, Fig. 5.13.1 (p. 438)",
    "drawingCaption": "Meyer Fig. 5.13.1: Unique direct sum decomposition v = m + n where m \u2208 M and n \u2208 M^\u22a5",
    "drawingSvg": "",
    "coreTranslation": [
      "The <strong>Sum of Subspaces</strong> is $U_1 + \\dots + U_m = \\{u_1 + \\dots + u_m : u_i \\in U_i\\}$. It is the smallest subspace containing all $U_i$.",
      "The sum is called a <strong>Direct Sum</strong>, written $U_1 \\oplus \\dots \\oplus U_m$, if every vector $v \\in U_1 + \\dots + U_m$ can be written as $v = u_1 + \\dots + u_m$ in <strong>EXACTLY ONE UNIQUE WAY</strong>.",
      "<strong>Two Subspaces ($m = 2$):</strong> The sum $U_1 + U_2$ is direct if and only if their intersection is trivial: $U_1 \\cap U_2 = \\{0\\}$."
    ],
    "math": "$$U_1 + U_2 = U_1 \\oplus U_2 \\iff U_1 \\cap U_2 = \\{\\mathbf{0}\\}$$",
    "personalConnection": "Coordinate axes in 2D space: the x-axis and y-axis share ONLY the origin $(0,0)$. Every point $(x, y)$ decomposes uniquely into an x-component and a y-component.",
    "examTrap": "The intersection condition $U_i \\cap U_j = \\{0\\}$ ONLY works for $m=2$ subspaces! For 3 or more subspaces, pairwise trivial intersection does NOT guarantee a direct sum."
  },
  {
    "id": 20103,
    "subject": "LAA",
    "topicId": "01_Vector_Spaces_Subspaces_and_Direct_Sums",
    "topicTitle": "01 \u00b7 Vector Spaces, Subspaces & Direct Sums",
    "cardNumber": "03",
    "category": "DIRECT SUM CRITERION",
    "highlighterClass": "highlight-emerald",
    "title": "Fundamental Direct Sum Zero-Vector Criterion",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\">\n  <defs>\n    <marker id=\"arr-laa3\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\">\n      <path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/>\n    </marker>\n  </defs>\n  <!-- 3 independent axes meeting strictly at origin -->\n  <line x1=\"120\" y1=\"75\" x2=\"195\" y2=\"75\" stroke=\"#000000\" stroke-width=\"2\" marker-end=\"url(#arr-laa3)\"/>\n  <text x=\"200\" y=\"78\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\">u\u2081 \u2208 U\u2081</text>\n  <line x1=\"120\" y1=\"75\" x2=\"120\" y2=\"18\" stroke=\"#000000\" stroke-width=\"2\" marker-end=\"url(#arr-laa3)\"/>\n  <text x=\"120\" y=\"14\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" text-anchor=\"middle\">u\u2082 \u2208 U\u2082</text>\n  <line x1=\"120\" y1=\"75\" x2=\"60\" y2=\"120\" stroke=\"#000000\" stroke-width=\"2\" marker-end=\"url(#arr-laa3)\"/>\n  <text x=\"45\" y=\"125\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\">u\u2083 \u2208 U\u2083</text>\n  <!-- Origin -->\n  <circle cx=\"120\" cy=\"75\" r=\"4\" fill=\"#000000\"/>\n  <text x=\"120\" y=\"93\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" font-weight=\"bold\" text-anchor=\"middle\">u\u2081 + u\u2082 + u\u2083 = 0 \u21d2 u\u2081 = u\u2082 = u\u2083 = 0</text>\n  <text x=\"120\" y=\"136\" fill=\"#000000\" font-size=\"8.5\" font-family=\"sans-serif\" text-anchor=\"middle\">Zero-Vector Test: Unique representation of 0 guarantees direct sum</text>\n</svg>",
    "drawingCaption": "Zero-Vector Test: The only way to sum components to zero is if each individual component is zero",
    "coreTranslation": [
      "<strong>Master Theorem (Axler 1.44):</strong> The sum $U_1 + \\dots + U_m$ is a direct sum if and only if the only way to write the zero vector as a sum $u_1 + \\dots + u_m = 0$ (with $u_i \\in U_i$) is: $u_1 = u_2 = \\dots = u_m = 0$.",
      "<strong>Proof $(\\implies)$:</strong> If the sum is direct, representation of 0 is unique. Since $0 + \\dots + 0 = 0$, this must be the only representation.",
      "<strong>Proof $(\\impliedby)$:</strong> If $v = u_1 + \\dots + u_m = w_1 + \\dots + w_m$, subtracting gives $(u_1 - w_1) + \\dots + (u_m - w_m) = 0$. By hypothesis, each $u_i - w_i = 0 \\implies u_i = w_i$."
    ],
    "math": "$$U_1 \\oplus \\dots \\oplus U_m \\iff \\left( \\sum_{i=1}^m u_i = 0, \\; u_i \\in U_i \\implies u_1 = \\dots = u_m = 0 \\right)$$",
    "personalConnection": "Linear independence scaled up to entire rooms: no room's contents can be combined with other rooms to cancel out and leave an empty house.",
    "examTrap": "Always use the zero-vector criterion when testing 3 or more subspaces! It is universal, completely immune to pairwise intersection traps, and matches the definition of linear independence."
  },
  {
    "id": 20104,
    "subject": "LAA",
    "topicId": "01_Vector_Spaces_Subspaces_and_Direct_Sums",
    "topicTitle": "01 \u00b7 Vector Spaces, Subspaces & Direct Sums",
    "cardNumber": "04",
    "category": "COUNTEREXAMPLE TRAPS",
    "highlighterClass": "highlight-rose",
    "title": "Exam Trap: Pairwise Disjoint \u2260 Direct Sum",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\">\n  <!-- 3 coplanar lines in R\u00b2 -->\n  <line x1=\"25\" y1=\"75\" x2=\"215\" y2=\"75\" stroke=\"#000000\" stroke-width=\"1.8\"/>\n  <text x=\"215\" y=\"87\" fill=\"#000000\" font-size=\"8.5\" font-family=\"serif\" font-style=\"italic\">U\u2081 (x-axis)</text>\n  <line x1=\"120\" y1=\"130\" x2=\"120\" y2=\"18\" stroke=\"#000000\" stroke-width=\"1.8\"/>\n  <text x=\"120\" y=\"14\" fill=\"#000000\" font-size=\"8.5\" font-family=\"serif\" font-style=\"italic\" text-anchor=\"middle\">U\u2082 (y-axis)</text>\n  <line x1=\"50\" y1=\"125\" x2=\"190\" y2=\"25\" stroke=\"#000000\" stroke-width=\"1.8\" stroke-dasharray=\"4,3\"/>\n  <text x=\"195\" y=\"25\" fill=\"#000000\" font-size=\"8.5\" font-family=\"serif\" font-style=\"italic\">U\u2083 (y = x)</text>\n  <circle cx=\"120\" cy=\"75\" r=\"4\" fill=\"#000000\"/>\n  <text x=\"120\" y=\"98\" fill=\"#000000\" font-size=\"8.5\" font-family=\"sans-serif\" font-weight=\"bold\" text-anchor=\"middle\">U_i \u2229 U_j = {0} pair-wise, BUT sum is NOT direct!</text>\n  <text x=\"120\" y=\"138\" fill=\"#000000\" font-size=\"8.5\" font-family=\"monospace\" text-anchor=\"middle\">(1,0) + (0,1) + (-1,-1) = (0,0)</text>\n</svg>",
    "drawingCaption": "Classic IISc Trap: Three lines in R\u00b2 have pairwise trivial intersections, yet (1,1) + (-1,0) + (0,-1) = 0",
    "coreTranslation": [
      "<strong>The Classic Trap:</strong> In $\\mathbb{R}^2$, consider three distinct lines through the origin: $U_1 = \\{(x, 0)\\}$, $U_2 = \\{(0, y)\\}$, $U_3 = \\{(x, x)\\}$.",
      "Notice that $U_1 \\cap U_2 = \\{0\\}$, $U_1 \\cap U_3 = \\{0\\}$, and $U_2 \\cap U_3 = \\{0\\}$. They are strictly pairwise disjoint at the origin!",
      "YET $U_1 + U_2 + U_3$ is <strong>NOT a direct sum</strong>: $(1, 0) + (0, 1) + (-1, -1) = (0, 0)$ with non-zero vectors! Representation of zero is not unique."
    ],
    "math": "$$U_i \\cap U_j = \\{0\\} \\, (\\forall i \\ne j) \\; \\not\\!\\!\\implies U_1 + \\dots + U_m \\text{ is direct for } m \\ge 3$$",
    "personalConnection": "Three tripod legs that lie completely flat on the kitchen floor: each leg points in a different direction, but because they are all in the same 2D floor, they cannot support a 3D table.",
    "examTrap": "The correct intersection condition for $m \\ge 3$ subspaces is: $U_j \\cap \\left( \\sum_{i \\ne j} U_i \\right) = \\{0\\}$ for each $j$. Each subspace must intersect the sum of ALL other subspaces trivially."
  },
  {
    "id": 20105,
    "subject": "LAA",
    "topicId": "01_Vector_Spaces_Subspaces_and_Direct_Sums",
    "topicTitle": "01 \u00b7 Vector Spaces, Subspaces & Direct Sums",
    "cardNumber": "05",
    "category": "DIMENSION THEOREMS",
    "highlighterClass": "highlight-violet",
    "title": "Dimension Formula for Subspace Sums",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\">\n  <!-- Venn Subspace Dimension Overlap -->\n  <circle cx=\"95\" cy=\"65\" r=\"45\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.8\"/>\n  <circle cx=\"145\" cy=\"65\" r=\"45\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.8\"/>\n  <!-- Overlap Region -->\n  <path d=\"M 120 28 A 45 45 0 0 0 120 102 A 45 45 0 0 0 120 28 Z\" fill=\"#e2e8f0\" stroke=\"none\"/>\n  <circle cx=\"95\" cy=\"65\" r=\"45\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.8\"/>\n  <circle cx=\"145\" cy=\"65\" r=\"45\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.8\"/>\n  <text x=\"75\" y=\"68\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\">dim U\u2081</text>\n  <text x=\"165\" y=\"68\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\">dim U\u2082</text>\n  <text x=\"120\" y=\"68\" fill=\"#000000\" font-size=\"8\" font-family=\"serif\" font-style=\"italic\" text-anchor=\"middle\">dim(U\u2081\u2229U\u2082)</text>\n  <text x=\"120\" y=\"125\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" font-weight=\"bold\" text-anchor=\"middle\">dim(U\u2081 + U\u2082) = dim U\u2081 + dim U\u2082 - dim(U\u2081 \u2229 U\u2082)</text>\n</svg>",
    "drawingCaption": "Dimension Formula: Overlap dim(U\u2081 \u2229 U\u2082) is subtracted once to avoid double-counting basis elements",
    "coreTranslation": [
      "<strong>Theorem:</strong> For finite-dimensional subspaces $U_1, U_2 \\le V$: $\\dim(U_1 + U_2) = \\dim U_1 + \\dim U_2 - \\dim(U_1 \\cap U_2)$.",
      "<strong>Direct Sum Characterization:</strong> The sum is direct ($U_1 \\oplus U_2$) if and only if $\\dim(U_1 \\cap U_2) = 0$, which yields the additive formula: $\\dim(U_1 \\oplus U_2) = \\dim U_1 + \\dim U_2$.",
      "<strong>Proof Mechanism:</strong> Start with basis $\\{v_1, \\dots, v_k\\}$ of $U_1 \\cap U_2$. Extend to basis of $U_1$ and basis of $U_2$. The union of these extended bases forms a basis of $U_1 + U_2$."
    ],
    "math": "$$\\dim(U_1 + U_2) = \\dim U_1 + \\dim U_2 - \\dim(U_1 \\cap U_2) \\le \\dim U_1 + \\dim U_2$$",
    "personalConnection": "Inclusion-Exclusion for sets: $|A \\cup B| = |A| + |B| - |A \\cap B|$. If the sets share zero common elements, the total size is simply the sum of their individual sizes.",
    "examTrap": "If $\\dim(U_1) + \\dim(U_2) > \\dim(V)$, the subspaces MUST have a non-trivial intersection! E.g., two 2D planes in $\\mathbb{R}^3$ must intersect in at least a line: $\\dim(U_1 \\cap U_2) \\ge 2 + 2 - 3 = 1$."
  },
  {
    "id": 20106,
    "subject": "LAA",
    "topicId": "01_Vector_Spaces_Subspaces_and_Direct_Sums",
    "topicTitle": "01 \u00b7 Vector Spaces, Subspaces & Direct Sums",
    "cardNumber": "06",
    "category": "WORKED BENCHMARK",
    "highlighterClass": "highlight-indigo",
    "title": "Worked Benchmark: Symmetric \u2295 Skew-Symmetric",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\">\n  <rect x=\"25\" y=\"20\" width=\"190\" height=\"105\" rx=\"8\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.5\"/>\n  <text x=\"120\" y=\"38\" fill=\"#000000\" font-size=\"10\" font-family=\"serif\" font-style=\"italic\" font-weight=\"bold\" text-anchor=\"middle\">M_{n\u00d7n}(\u211d) = \ud835\udcae_n \u2295 \ud835\udc9c_n</text>\n  <!-- Matrix decomposition boxes -->\n  <rect x=\"40\" y=\"52\" width=\"70\" height=\"45\" rx=\"4\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.2\"/>\n  <text x=\"75\" y=\"70\" fill=\"#000000\" font-size=\"8.5\" font-family=\"sans-serif\" font-weight=\"bold\" text-anchor=\"middle\">Symmetric</text>\n  <text x=\"75\" y=\"84\" fill=\"#000000\" font-size=\"8\" font-family=\"serif\" font-style=\"italic\" text-anchor=\"middle\">\u00bd(A + A\u1d40)</text>\n  <text x=\"120\" y=\"78\" fill=\"#000000\" font-size=\"14\" font-family=\"sans-serif\" font-weight=\"bold\" text-anchor=\"middle\">\u2295</text>\n  <rect x=\"130\" y=\"52\" width=\"70\" height=\"45\" rx=\"4\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.2\"/>\n  <text x=\"165\" y=\"70\" fill=\"#000000\" font-size=\"8.5\" font-family=\"sans-serif\" font-weight=\"bold\" text-anchor=\"middle\">Skew-Symm</text>\n  <text x=\"165\" y=\"84\" fill=\"#000000\" font-size=\"8\" font-family=\"serif\" font-style=\"italic\" text-anchor=\"middle\">\u00bd(A - A\u1d40)</text>\n  <text x=\"120\" y=\"115\" fill=\"#000000\" font-size=\"8.5\" font-family=\"monospace\" text-anchor=\"middle\">\ud835\udcae_n \u2229 \ud835\udc9c_n = {0} \u21d2 Direct Sum</text>\n</svg>",
    "drawingCaption": "Canonical Matrix Direct Sum: Every square matrix splits uniquely into symmetric and skew-symmetric parts",
    "coreTranslation": [
      "<strong>Problem:</strong> Prove $M_{n \\times n}(\\mathbb{R}) = \\mathcal{S}_n \\oplus \\mathcal{A}_n$, where $\\mathcal{S}_n = \\{A : A^T = A\\}$ and $\\mathcal{A}_n = \\{A : A^T = -A\\}$.",
      "<strong>Step 1 (Existence):</strong> For any $A \\in M_{n \\times n}$, write: $A = \\frac{A + A^T}{2} + \\frac{A - A^T}{2}$. $\\frac{A + A^T}{2} \\in \\mathcal{S}_n$ and $\\frac{A - A^T}{2} \\in \\mathcal{A}_n$. Thus $M_{n \\times n} = \\mathcal{S}_n + \\mathcal{A}_n$.",
      "<strong>Step 2 (Uniqueness / Intersection):</strong> Let $A \\in \\mathcal{S}_n \\cap \\mathcal{A}_n$. Then $A^T = A$ and $A^T = -A \\implies A = -A \\implies 2A = 0 \\implies A = 0$. Hence $\\mathcal{S}_n \\cap \\mathcal{A}_n = \\{0\\}$, proving direct sum!"
    ],
    "math": "$$A = \\underbrace{\\frac{A + A^T}{2}}_{\\in \\mathcal{S}_n} + \\underbrace{\\frac{A - A^T}{2}}_{\\in \\mathcal{A}_n}, \\quad \\mathcal{S}_n \\cap \\mathcal{A}_n = \\{0\\} \\implies M_n = \\mathcal{S}_n \\oplus \\mathcal{A}_n$$",
    "personalConnection": "Decomposing any musical sound wave into an even symmetric cosine wave and an odd antisymmetric sine wave. Both components are completely orthogonal and span the full sound space.",
    "examTrap": "Check the dimensions: $\\dim \\mathcal{S}_n = \\frac{n(n+1)}{2}$, $\\dim \\mathcal{A}_n = \\frac{n(n-1)}{2}$. Their sum is $\\frac{n(n+1)}{2} + \\frac{n(n-1)}{2} = n^2 = \\dim M_{n \\times n}$, confirming the direct sum dimension theorem."
  },
  {
    "id": 30101,
    "subject": "StoMA",
    "topicId": "01_Probability_Spaces_Axioms_and_Continuity_of_Probability",
    "topicTitle": "01 \u00b7 Probability Spaces & Continuity",
    "cardNumber": "01",
    "category": "MEASURE & PROBABILITY",
    "highlighterClass": "highlight-cyan",
    "title": "Probability Space Triple (\u03a9, F, P)",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\">\n  <defs>\n    <marker id=\"arr-stoma1\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\">\n      <path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/>\n    </marker>\n  </defs>\n  <!-- Sample Space Universe Omega -->\n  <rect x=\"25\" y=\"20\" width=\"190\" height=\"105\" rx=\"8\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.5\"/>\n  <text x=\"35\" y=\"36\" fill=\"#000000\" font-size=\"10\" font-family=\"serif\" font-style=\"italic\" font-weight=\"bold\">Sample Space \u03a9</text>\n  <!-- Sigma-algebra Event A -->\n  <ellipse cx=\"90\" cy=\"75\" rx=\"45\" ry=\"30\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.8\"/>\n  <text x=\"90\" y=\"78\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" font-weight=\"bold\" text-anchor=\"middle\">Event A \u2208 \u2131</text>\n  <!-- Probability Measure P Arrow to [0, 1] -->\n  <line x1=\"140\" y1=\"75\" x2=\"185\" y2=\"75\" stroke=\"#000000\" stroke-width=\"1.8\" marker-end=\"url(#arr-stoma1)\"/>\n  <text x=\"162\" y=\"68\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" text-anchor=\"middle\">\u2119(A)</text>\n  <text x=\"195\" y=\"78\" fill=\"#000000\" font-size=\"9\" font-family=\"sans-serif\">[0, 1]</text>\n  <text x=\"120\" y=\"136\" fill=\"#000000\" font-size=\"8.5\" font-family=\"sans-serif\" text-anchor=\"middle\">Probability Triple: (\u03a9, \u2131, \u2119)</text>\n</svg>",
    "drawingCaption": "Probability Triple: Sample space \u03a9, \u03c3-algebra of observable events F, and measure P mapping to [0, 1]",
    "coreTranslation": [
      "A <strong>Probability Space</strong> is a rigorous mathematical triple $(\\Omega, \\mathcal{F}, \\mathbb{P})$:",
      "<strong>1. Sample Space $\\Omega$:</strong> The set of all possible outcomes of an experiment.",
      "<strong>2. $\\sigma$-Algebra $\\mathcal{F}$ (Events):</strong> A collection of subsets of $\\Omega$ containing $\\emptyset$, closed under complements ($A \\in \\mathcal{F} \\implies A^c \\in \\mathcal{F}$), and closed under <strong>countable unions</strong> ($A_i \\in \\mathcal{F} \\implies \\bigcup_{i=1}^\\infty A_i \\in \\mathcal{F}$).",
      "<strong>3. Probability Measure $\\mathbb{P}$:</strong> A function $\\mathbb{P}: \\mathcal{F} \\to [0, 1]$ satisfying Kolmogorov's axioms."
    ],
    "math": "$$\\mathbb{P}: \\mathcal{F} \\to [0, 1] \\quad \\text{on } (\\Omega, \\mathcal{F}), \\quad \\Omega \\in \\mathcal{F}, \\quad A \\in \\mathcal{F} \\implies A^c \\in \\mathcal{F}$$",
    "personalConnection": "A dartboard: $\\Omega$ is the wooden board. $\\mathcal{F}$ is the rulebook defining which regions you can score points on (bullseye, rings). $\\mathbb{P}(A)$ is your probability of hitting area $A$.",
    "examTrap": "Why do we need a $\\sigma$-algebra rather than the entire power set $2^\\Omega$? Because on uncountably infinite spaces (like $\\mathbb{R}$), non-measurable sets (e.g. Vitali sets) exist where probabilities CANNOT be consistently assigned!"
  },
  {
    "id": 30102,
    "subject": "StoMA",
    "topicId": "01_Probability_Spaces_Axioms_and_Continuity_of_Probability",
    "topicTitle": "01 \u00b7 Probability Spaces & Continuity",
    "cardNumber": "02",
    "category": "KOLMOGOROV AXIOMS",
    "highlighterClass": "highlight-amber",
    "title": "Kolmogorov\u2019s Three Axioms of Probability",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\">\n  <!-- 3 disjoint event bubbles -->\n  <circle cx=\"60\" cy=\"65\" r=\"25\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.8\"/>\n  <text x=\"60\" y=\"68\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" text-anchor=\"middle\">A\u2081</text>\n  <circle cx=\"120\" cy=\"65\" r=\"25\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.8\"/>\n  <text x=\"120\" y=\"68\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" text-anchor=\"middle\">A\u2082</text>\n  <circle cx=\"180\" cy=\"65\" r=\"25\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.8\"/>\n  <text x=\"180\" y=\"68\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" text-anchor=\"middle\">A\u2083</text>\n  <text x=\"120\" y=\"115\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" font-weight=\"bold\" text-anchor=\"middle\">Countable Additivity: \u2119(\u22c3 A_i) = \u2211 \u2119(A_i)</text>\n  <text x=\"120\" y=\"134\" fill=\"#000000\" font-size=\"8.5\" font-family=\"sans-serif\" text-anchor=\"middle\">Pairwise disjoint events: A_i \u2229 A_j = \u2205 (i \u2260 j)</text>\n</svg>",
    "drawingCaption": "Axiom 3: For mutually disjoint events A_i \u2229 A_j = \u2205, the probability of the union equals the sum of probabilities",
    "coreTranslation": [
      "<strong>Axiom 1 (Non-negativity):</strong> For every event $A \\in \\mathcal{F}$, $\\mathbb{P}(A) \\ge 0$.",
      "<strong>Axiom 2 (Normalization):</strong> The entire sample space has certainty: $\\mathbb{P}(\\Omega) = 1$.",
      "<strong>Axiom 3 (Countable Additivity):</strong> For any sequence of pairwise disjoint events $A_1, A_2, \\dots$ ($A_i \\cap A_j = \\emptyset$ for $i \\ne j$): $\\mathbb{P}\\left( \\bigcup_{i=1}^\\infty A_i \\right) = \\sum_{i=1}^\\infty \\mathbb{P}(A_i)$."
    ],
    "math": "$$\\mathbb{P}(A) \\ge 0, \\quad \\mathbb{P}(\\Omega) = 1, \\quad \\mathbb{P}\\left(\\bigcup_{i=1}^\\infty A_i\\right) = \\sum_{i=1}^\\infty \\mathbb{P}(A_i) \\; (A_i \\cap A_j = \\emptyset)$$",
    "personalConnection": "Pouring a litre bottle of milk into mutually separate teacups: the total volume of milk across all cups is the sum of the volumes in each cup; no milk is created or destroyed.",
    "examTrap": "FINITE additivity ($\\mathbb{P}(A \\cup B) = \\mathbb{P}(A) + \\mathbb{P}(B)$) is NOT enough! Countable additivity is strictly required to prove limit theorems and continuity of probability."
  },
  {
    "id": 30103,
    "subject": "StoMA",
    "topicId": "01_Probability_Spaces_Axioms_and_Continuity_of_Probability",
    "topicTitle": "01 \u00b7 Probability Spaces & Continuity",
    "cardNumber": "03",
    "category": "LIMIT THEOREMS",
    "highlighterClass": "highlight-emerald",
    "title": "Continuity of Probability (Up & Down Limits)",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\">\n  <!-- Concentric expanding rings A_n -->\n  <circle cx=\"120\" cy=\"65\" r=\"18\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.2\"/>\n  <text x=\"120\" y=\"68\" fill=\"#000000\" font-size=\"8\" font-family=\"serif\" font-style=\"italic\" text-anchor=\"middle\">A\u2081</text>\n  <circle cx=\"120\" cy=\"65\" r=\"32\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.5\"/>\n  <text x=\"120\" y=\"44\" fill=\"#000000\" font-size=\"8\" font-family=\"serif\" font-style=\"italic\" text-anchor=\"middle\">A\u2082</text>\n  <circle cx=\"120\" cy=\"65\" r=\"48\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.8\"/>\n  <text x=\"120\" y=\"28\" fill=\"#000000\" font-size=\"8.5\" font-family=\"serif\" font-style=\"italic\" font-weight=\"bold\" text-anchor=\"middle\">A_n \u2191 A</text>\n  <text x=\"120\" y=\"125\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" font-weight=\"bold\" text-anchor=\"middle\">Continuity: lim \u2119(A_n) = \u2119(lim A_n)</text>\n  <text x=\"120\" y=\"138\" fill=\"#000000\" font-size=\"8.5\" font-family=\"sans-serif\" text-anchor=\"middle\">Increasing sequence: A\u2081 \u2282 A\u2082 \u2282 A\u2083 ...</text>\n</svg>",
    "drawingCaption": "Continuity from below: Expanding sequence of events A\u2081 \u2282 A\u2082 \u2282 ... whose probabilities limit to P(A)",
    "coreTranslation": [
      "<strong>Continuity from Below:</strong> If $A_1 \\subset A_2 \\subset A_3 \\subset \\dots$ is an increasing sequence of events with limit $A = \\bigcup_{n=1}^\\infty A_n$ (denoted $A_n \\uparrow A$), then: $\\lim_{n \\to \\infty} \\mathbb{P}(A_n) = \\mathbb{P}(A)$.",
      "<strong>Continuity from Above:</strong> If $B_1 \\supset B_2 \\supset B_3 \\dots$ is a decreasing sequence of events with limit $B = \\bigcap_{n=1}^\\infty B_n$ (denoted $B_n \\downarrow B$), then: $\\lim_{n \\to \\infty} \\mathbb{P}(B_n) = \\mathbb{P}(B)$.",
      "<strong>Proof Core:</strong> Partition $A$ into disjoint rings: $C_1 = A_1$, $C_k = A_k \\setminus A_{k-1}$. Then apply Kolmogorov's countable additivity to the disjoint sum: $\\mathbb{P}(A) = \\sum_{k=1}^\\infty \\mathbb{P}(C_k) = \\lim_{n\\to\\infty} \\sum_{k=1}^n \\mathbb{P}(C_k) = \\lim \\mathbb{P}(A_n)$."
    ],
    "math": "$$A_n \\uparrow A \\implies \\mathbb{P}(A) = \\lim_{n\\to\\infty} \\mathbb{P}(A_n), \\quad B_n \\downarrow B \\implies \\mathbb{P}(B) = \\lim_{n\\to\\infty} \\mathbb{P}(B_n)$$",
    "personalConnection": "Blowing air into a spherical balloon: as the volume of air inside the balloon expands smoothly toward its maximum burst capacity, the surface area approaches the limit continuously without teleporting.",
    "examTrap": "Continuity of probability is mathematically EQUIVALENT to countable additivity (assuming finite additivity). If a measure fails countable additivity, continuity of probability fails immediately."
  },
  {
    "id": 30104,
    "subject": "StoMA",
    "topicId": "01_Probability_Spaces_Axioms_and_Continuity_of_Probability",
    "topicTitle": "01 \u00b7 Probability Spaces & Continuity",
    "cardNumber": "04",
    "category": "PROBABILITY INEQUALITIES",
    "highlighterClass": "highlight-violet",
    "title": "Boole\u2019s Inequality & Bonferroni Bounds",
    "textbookImg": "assets/stoma_fig2_venn.png",
    "textbookRef": "Hoel, Port, Stone, Intro to Probability, Fig. 2 (p. 23)",
    "drawingCaption": "Hoel-Port-Stone Fig. 2: Partition of A \u222a B into disjoint regions A \u2229 B\u1d9c, A \u2229 B, A\u1d9c \u2229 B",
    "drawingSvg": "",
    "coreTranslation": [
      "<strong>Boole's Inequality (Countable Subadditivity):</strong> For ANY sequence of events $A_1, A_2, \\dots$ (disjoint or overlapping): $\\mathbb{P}\\left( \\bigcup_{i=1}^\\infty A_i \\right) \\le \\sum_{i=1}^\\infty \\mathbb{P}(A_i)$.",
      "<strong>Bonferroni Bounds:</strong> Truncating the inclusion-exclusion series produces alternating upper and lower bounds:",
      "$\\mathbb{P}\\left( \\bigcup_{i=1}^n A_i \\right) \\ge \\sum \\mathbb{P}(A_i) - \\sum_{i < j} \\mathbb{P}(A_i \\cap A_j)$, and $\\le$ the 3-term sum."
    ],
    "math": "$$\\mathbb{P}\\left( \\bigcup_{i=1}^\\infty A_i \\right) \\le \\sum_{i=1}^\\infty \\mathbb{P}(A_i), \\quad \\mathbb{P}(A \\cup B) = \\mathbb{P}(A) + \\mathbb{P}(B) - \\mathbb{P}(A \\cap B)$$",
    "personalConnection": "Purchasing multiple lottery tickets: your probability of winning on AT LEAST one ticket cannot exceed the sum of the individual ticket winning probabilities, because overlapping wins don't multiply your chances.",
    "examTrap": "Boole's inequality requires NO assumption of independence or disjointness! It holds universally for arbitrary events, making it the most versatile bounding tool in proof questions."
  },
  {
    "id": 30105,
    "subject": "StoMA",
    "topicId": "01_Probability_Spaces_Axioms_and_Continuity_of_Probability",
    "topicTitle": "01 \u00b7 Probability Spaces & Continuity",
    "cardNumber": "05",
    "category": "INCLUSION-EXCLUSION",
    "highlighterClass": "highlight-indigo",
    "title": "General Inclusion-Exclusion Principle",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\">\n  <!-- 3-set Venn Diagram -->\n  <circle cx=\"100\" cy=\"55\" r=\"32\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.5\"/>\n  <circle cx=\"140\" cy=\"55\" r=\"32\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.5\"/>\n  <circle cx=\"120\" cy=\"85\" r=\"32\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.5\"/>\n  <circle cx=\"120\" cy=\"65\" r=\"4\" fill=\"#000000\"/>\n  <text x=\"120\" y=\"68\" fill=\"#ffffff\" font-size=\"6\" font-family=\"monospace\" text-anchor=\"middle\">+</text>\n  <text x=\"80\" y=\"48\" fill=\"#000000\" font-size=\"8\" font-family=\"serif\" font-style=\"italic\">A\u2081</text>\n  <text x=\"155\" y=\"48\" fill=\"#000000\" font-size=\"8\" font-family=\"serif\" font-style=\"italic\">A\u2082</text>\n  <text x=\"120\" y=\"110\" fill=\"#000000\" font-size=\"8\" font-family=\"serif\" font-style=\"italic\" text-anchor=\"middle\">A\u2083</text>\n  <text x=\"120\" y=\"128\" fill=\"#000000\" font-size=\"8.5\" font-family=\"sans-serif\" font-weight=\"bold\" text-anchor=\"middle\">Alternating signs: + Singles - Pairs + Triples</text>\n  <text x=\"120\" y=\"139\" fill=\"#000000\" font-size=\"8\" font-family=\"monospace\" text-anchor=\"middle\">\u2119(\u222a A_i) = S\u2081 - S\u2082 + S\u2083 - ...</text>\n</svg>",
    "drawingCaption": "3-Set Inclusion-Exclusion: Add single probabilities, subtract double intersections, add triple intersection back",
    "coreTranslation": [
      "For $n$ arbitrary events $A_1, \\dots, A_n$, the probability of their union is given by the exact alternating sum:",
      "$$\\mathbb{P}\\left( \\bigcup_{i=1}^n A_i \\right) = \\sum_{k=1}^n (-1)^{k-1} S_k, \\quad \\text{where } S_k = \\sum_{1 \\le i_1 < \\dots < i_k \\le n} \\mathbb{P}(A_{i_1} \\cap \\dots \\cap A_{i_k})$$",
      "For $n = 3$: $\\mathbb{P}(A_1 \\cup A_2 \\cup A_3) = \\sum \\mathbb{P}(A_i) - \\sum \\mathbb{P}(A_i \\cap A_j) + \\mathbb{P}(A_1 \\cap A_2 \\cap A_3)$."
    ],
    "math": "$$\\mathbb{P}\\left(\\bigcup_{i=1}^n A_i\\right) = \\sum_{i} \\mathbb{P}(A_i) - \\sum_{i<j} \\mathbb{P}(A_i \\cap A_j) + \\dots + (-1)^{n-1} \\mathbb{P}\\left(\\bigcap_{i=1}^n A_i\\right)$$",
    "personalConnection": "Adjusting accounting ledger double-counts: adding items from all departments overcounts shared projects, so you subtract joint projects, but now projects shared by three groups were removed too many times, so you add them back.",
    "examTrap": "Remember that the sign of the full intersection $\\mathbb{P}(\\bigcap_{i=1}^n A_i)$ is $(-1)^{n-1}$. For $n=2$, it's negative $(-)$; for $n=3$, it's positive $(+)$; for $n=4$, it's negative $(-)$."
  },
  {
    "id": 30106,
    "subject": "StoMA",
    "topicId": "01_Probability_Spaces_Axioms_and_Continuity_of_Probability",
    "topicTitle": "01 \u00b7 Probability Spaces & Continuity",
    "cardNumber": "06",
    "category": "WORKED BENCHMARK",
    "highlighterClass": "highlight-rose",
    "title": "Worked Benchmark: Infinite Coin Toss Limit",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\">\n  <defs>\n    <marker id=\"arr-stoma6\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\">\n      <path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/>\n    </marker>\n  </defs>\n  <line x1=\"25\" y1=\"75\" x2=\"215\" y2=\"75\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-stoma6)\"/>\n  <text x=\"215\" y=\"88\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\">n</text>\n  <!-- Decreasing probabilities -->\n  <circle cx=\"50\" cy=\"75\" r=\"3.5\" fill=\"#000000\"/>\n  <text x=\"50\" y=\"60\" fill=\"#000000\" font-size=\"8.5\" font-family=\"monospace\" text-anchor=\"middle\">(\u00bd)\u00b9</text>\n  <circle cx=\"90\" cy=\"75\" r=\"3.5\" fill=\"#000000\"/>\n  <text x=\"90\" y=\"60\" fill=\"#000000\" font-size=\"8.5\" font-family=\"monospace\" text-anchor=\"middle\">(\u00bd)\u00b2</text>\n  <circle cx=\"130\" cy=\"75\" r=\"3.5\" fill=\"#000000\"/>\n  <text x=\"130\" y=\"60\" fill=\"#000000\" font-size=\"8.5\" font-family=\"monospace\" text-anchor=\"middle\">(\u00bd)\u00b3</text>\n  <circle cx=\"175\" cy=\"75\" r=\"3.5\" fill=\"#000000\"/>\n  <text x=\"175\" y=\"60\" fill=\"#000000\" font-size=\"8.5\" font-family=\"monospace\" text-anchor=\"middle\">(\u00bd)\u207f \u2192 0</text>\n  <text x=\"120\" y=\"115\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" font-weight=\"bold\" text-anchor=\"middle\">\u2119(Never Toss Tails) = lim (\u00bd)\u207f = 0</text>\n  <text x=\"120\" y=\"132\" fill=\"#000000\" font-size=\"8.5\" font-family=\"sans-serif\" text-anchor=\"middle\">Decreasing sequence of events: B_n \u2193 \u2205</text>\n</svg>",
    "drawingCaption": "Worked Continuity Proof: Decreasing event sequence B_n = {First n tosses are all Heads} limits to probability 0",
    "coreTranslation": [
      "<strong>Problem:</strong> A fair coin is tossed infinitely many times. Prove that the probability of NEVER getting Tails is 0.",
      "<strong>Step 1 (Formulate Events):</strong> Let $B_n = \\{\\text{first } n \\text{ tosses are all Heads}\\}$. Clearly $B_{n+1} \\subset B_n$, so $\\{B_n\\}$ is a decreasing sequence.",
      "<strong>Step 2 (Intersection Event):</strong> The event $B = \\bigcap_{n=1}^\\infty B_n = \\{\\text{all infinite tosses are Heads}\\}$.",
      "<strong>Step 3 (Continuity from Above):</strong> $\\mathbb{P}(B) = \\lim_{n\\to\\infty} \\mathbb{P}(B_n) = \\lim_{n\\to\\infty} (1/2)^n = 0$. Hence almost surely, Tails will eventually appear!"
    ],
    "math": "$$B_n \\downarrow B \\implies \\mathbb{P}(B) = \\lim_{n\\to\\infty} \\mathbb{P}(B_n) = \\lim_{n\\to\\infty} \\left(\\frac{1}{2}\\right)^n = 0$$",
    "personalConnection": "Rolling a die repeatedly: the probability of rolling forever without ever seeing a 6 is an infinite decreasing chain $(5/6)^n$, which decays to zero with absolute certainty.",
    "examTrap": "An event having probability 0 does NOT mean it is impossible! Flipping infinite heads is an element of $\\Omega$ (it is a valid sequence $HHHH\\dots$), but its measure $\\mathbb{P}$ is zero."
  },
  {
    "id": 40101,
    "subject": "DIP",
    "topicId": "01_Image_Formation_Camera_Geometry_and_Transformations",
    "topicTitle": "01 \u00b7 Image Formation & Transformations",
    "cardNumber": "01",
    "category": "CAMERA GEOMETRY",
    "highlighterClass": "highlight-cyan",
    "title": "Pinhole Camera Model & Perspective",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\">\n  <defs>\n    <marker id=\"arr-dip1\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\">\n      <path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/>\n    </marker>\n  </defs>\n  <!-- Optical Axis -->\n  <line x1=\"20\" y1=\"75\" x2=\"220\" y2=\"75\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"3,3\"/>\n  <!-- Pinhole Barrier with aperture C -->\n  <line x1=\"120\" y1=\"20\" x2=\"120\" y2=\"70\" stroke=\"#000000\" stroke-width=\"2.5\"/>\n  <line x1=\"120\" y1=\"80\" x2=\"120\" y2=\"130\" stroke=\"#000000\" stroke-width=\"2.5\"/>\n  <circle cx=\"120\" cy=\"75\" r=\"3.5\" fill=\"#000000\"/>\n  <text x=\"120\" y=\"65\" fill=\"#000000\" font-size=\"8.5\" font-family=\"serif\" font-style=\"italic\" text-anchor=\"middle\">Pinhole C</text>\n  <!-- 3D Object Point (X, Y, Z) -->\n  <line x1=\"200\" y1=\"75\" x2=\"200\" y2=\"35\" stroke=\"#000000\" stroke-width=\"2.2\" marker-end=\"url(#arr-dip1)\"/>\n  <circle cx=\"200\" cy=\"35\" r=\"3\" fill=\"#000000\"/>\n  <text x=\"200\" y=\"28\" fill=\"#000000\" font-size=\"8.5\" font-family=\"serif\" font-style=\"italic\" text-anchor=\"middle\">(X, Y, Z)</text>\n  <!-- Ray through pinhole -->\n  <line x1=\"200\" y1=\"35\" x2=\"40\" y2=\"115\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"2,2\"/>\n  <!-- Inverted Image Plane -->\n  <line x1=\"40\" y1=\"75\" x2=\"40\" y2=\"115\" stroke=\"#000000\" stroke-width=\"2.2\" marker-end=\"url(#arr-dip1)\"/>\n  <circle cx=\"40\" cy=\"115\" r=\"3\" fill=\"#000000\"/>\n  <text x=\"40\" y=\"128\" fill=\"#000000\" font-size=\"8.5\" font-family=\"serif\" font-style=\"italic\" text-anchor=\"middle\">(-f X/Z)</text>\n  <text x=\"80\" y=\"87\" fill=\"#000000\" font-size=\"8.5\" font-family=\"serif\" font-style=\"italic\">f</text>\n  <text x=\"160\" y=\"87\" fill=\"#000000\" font-size=\"8.5\" font-family=\"serif\" font-style=\"italic\">Z</text>\n</svg>",
    "drawingCaption": "Pinhole Model: Similar triangles project 3D point (X, Y, Z) into inverted 2D image coordinates x = -f(X/Z)",
    "coreTranslation": [
      "In the standard pinhole camera, light rays pass through optical center $C = (0, 0, 0)$ and intersect an image plane located at distance $f$ (focal length).",
      "<strong>Similar Triangles Geometry:</strong> By geometry of similar triangles, a 3D point $(X, Y, Z)$ projects to inverted image coordinates: $x = -f \\frac{X}{Z}, \\quad y = -f \\frac{Y}{Z}$.",
      "In virtual camera models, the image plane is placed in FRONT of the pinhole at $+f$ to eliminate the negative sign, yielding the standard non-inverted projection: $x = f \\frac{X}{Z}$."
    ],
    "math": "$$x = f \\frac{X}{Z}, \\quad y = f \\frac{Y}{Z} \\quad (\\text{Perspective Division by Depth } Z)$$",
    "personalConnection": "Holding your thumb in front of your face: the closer your thumb is to your eye (small depth $Z$), the more massive it appears, completely blocking a building in the distance.",
    "examTrap": "Perspective projection is NON-LINEAR in Cartesian coordinates because of the division by $Z$! To make it linear, we MUST convert to <strong>homogeneous coordinates</strong>."
  },
  {
    "id": 40102,
    "subject": "DIP",
    "topicId": "01_Image_Formation_Camera_Geometry_and_Transformations",
    "topicTitle": "01 \u00b7 Image Formation & Transformations",
    "cardNumber": "02",
    "category": "PROJECTIVE GEOMETRY",
    "highlighterClass": "highlight-amber",
    "title": "Camera Matrix: x = K [R | t] X",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\">\n  <defs>\n    <marker id=\"arr-dip2\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\">\n      <path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/>\n    </marker>\n  </defs>\n  <!-- Flow: World -> Camera -> Pixel -->\n  <rect x=\"25\" y=\"45\" width=\"55\" height=\"50\" rx=\"6\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.5\"/>\n  <text x=\"52\" y=\"66\" fill=\"#000000\" font-size=\"8.5\" font-family=\"sans-serif\" font-weight=\"bold\" text-anchor=\"middle\">World 3D</text>\n  <text x=\"52\" y=\"82\" fill=\"#000000\" font-size=\"8\" font-family=\"serif\" font-style=\"italic\" text-anchor=\"middle\">X_w \u2208 \u211d\u2074</text>\n  <line x1=\"80\" y1=\"70\" x2=\"105\" y2=\"70\" stroke=\"#000000\" stroke-width=\"1.8\" marker-end=\"url(#arr-dip2)\"/>\n  <text x=\"92\" y=\"62\" fill=\"#000000\" font-size=\"8\" font-family=\"serif\" font-style=\"italic\" text-anchor=\"middle\">[R|t]</text>\n  <rect x=\"105\" y=\"45\" width=\"55\" height=\"50\" rx=\"6\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.5\"/>\n  <text x=\"132\" y=\"66\" fill=\"#000000\" font-size=\"8.5\" font-family=\"sans-serif\" font-weight=\"bold\" text-anchor=\"middle\">Camera 3D</text>\n  <text x=\"132\" y=\"82\" fill=\"#000000\" font-size=\"8\" font-family=\"serif\" font-style=\"italic\" text-anchor=\"middle\">X_c \u2208 \u211d\u00b3</text>\n  <line x1=\"160\" y1=\"70\" x2=\"185\" y2=\"70\" stroke=\"#000000\" stroke-width=\"1.8\" marker-end=\"url(#arr-dip2)\"/>\n  <text x=\"172\" y=\"62\" fill=\"#000000\" font-size=\"8\" font-family=\"serif\" font-style=\"italic\" text-anchor=\"middle\">K</text>\n  <rect x=\"185\" y=\"45\" width=\"45\" height=\"50\" rx=\"6\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.8\"/>\n  <text x=\"207\" y=\"66\" fill=\"#000000\" font-size=\"8.5\" font-family=\"sans-serif\" font-weight=\"bold\" text-anchor=\"middle\">Pixel</text>\n  <text x=\"207\" y=\"82\" fill=\"#000000\" font-size=\"8\" font-family=\"serif\" font-style=\"italic\" text-anchor=\"middle\">x \u2208 \u211d\u00b3</text>\n  <text x=\"120\" y=\"125\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" font-weight=\"bold\" text-anchor=\"middle\">x = K [R | t] X  (Extrinsics then Intrinsics)</text>\n</svg>",
    "drawingCaption": "Full Projection Pipeline: Extrinsics [R|t] map world to camera; Intrinsics K map camera to 2D pixels",
    "coreTranslation": [
      "In homogeneous coordinates, perspective projection is represented by a single $3 \\times 4$ projection matrix $P$:",
      "$$\\mathbf{x} = P \\mathbf{X} = K [R \\mid t] \\mathbf{X}, \\quad \\text{where } \\mathbf{x} = [u, v, 1]^T, \\; \\mathbf{X} = [X, Y, Z, 1]^T$$",
      "<strong>Extrinsic Matrix $[R \\mid t]$ ($3 \\times 4$):</strong> Represents the rigid body camera pose (rotation $R \\in SO(3)$ and translation $t \\in \\mathbb{R}^3$) relative to the world frame.",
      "<strong>Intrinsic Matrix $K$ ($3 \\times 3$):</strong> Encodes the internal geometric calibration of the optical sensor."
    ],
    "math": "$$\\begin{bmatrix} u \\\\ v \\\\ 1 \\end{bmatrix} \\sim \\begin{bmatrix} f_x & s & c_x \\\\ 0 & f_y & c_y \\\\ 0 & 0 & 1 \\end{bmatrix} \\begin{bmatrix} r_{11} & r_{12} & r_{13} & t_x \\\\ r_{21} & r_{22} & r_{23} & t_y \\\\ r_{31} & r_{32} & r_{33} & t_z \\end{bmatrix} \\begin{bmatrix} X \\\\ Y \\\\ Z \\\\ 1 \\end{bmatrix}$$",
    "personalConnection": "Filming a movie scene: the tripod position and swivel angle are the extrinsic parameters $[R|t]$. The lens choice (wide-angle vs telephoto) and camera sensor resolution are the intrinsic parameters $K$.",
    "examTrap": "The equality holds UP TO SCALE (indicated by $\\sim$)! You must divide the resulting homogeneous vector by its third coordinate: $u = \\tilde{u}/\\tilde{w}, v = \\tilde{v}/\\tilde{w}$ to obtain actual pixel coordinates."
  },
  {
    "id": 40103,
    "subject": "DIP",
    "topicId": "01_Image_Formation_Camera_Geometry_and_Transformations",
    "topicTitle": "01 \u00b7 Image Formation & Transformations",
    "cardNumber": "03",
    "category": "CAMERA INTRINSICS",
    "highlighterClass": "highlight-emerald",
    "title": "Intrinsic Calibration Matrix K",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\">\n  <!-- Sensor array rectangle with principal point -->\n  <rect x=\"40\" y=\"25\" width=\"160\" height=\"90\" rx=\"4\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.8\"/>\n  <!-- Sensor pixel grid ticks -->\n  <line x1=\"40\" y1=\"70\" x2=\"200\" y2=\"70\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"3,3\"/>\n  <line x1=\"120\" y1=\"25\" x2=\"120\" y2=\"115\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"3,3\"/>\n  <!-- Principal Point (c_x, c_y) -->\n  <circle cx=\"135\" cy=\"75\" r=\"4\" fill=\"#000000\"/>\n  <text x=\"145\" y=\"88\" fill=\"#000000\" font-size=\"8.5\" font-family=\"serif\" font-style=\"italic\">(c_x, c_y) Principal Point</text>\n  <!-- Focal lengths f_x and f_y -->\n  <line x1=\"40\" y1=\"125\" x2=\"100\" y2=\"125\" stroke=\"#000000\" stroke-width=\"2\"/>\n  <text x=\"70\" y=\"137\" fill=\"#000000\" font-size=\"8.5\" font-family=\"serif\" font-style=\"italic\" text-anchor=\"middle\">f_x = f \u00b7 m_x</text>\n</svg>",
    "drawingCaption": "Sensor Geometry: Focal lengths f_x, f_y in pixels and optical center (c_x, c_y) offset from sensor corner",
    "coreTranslation": [
      "The upper-triangular <strong>Intrinsic Calibration Matrix $K$</strong> has 5 degrees of freedom:",
      "$$K = \\begin{bmatrix} f_x & s & c_x \\\\ 0 & f_y & c_y \\\\ 0 & 0 & 1 \\end{bmatrix}$$",
      "<strong>Focal Lengths $f_x, f_y$:</strong> $f_x = f \\cdot m_x, f_y = f \\cdot m_y$, where $m_x, m_y$ are pixels per millimeter. For square pixels, $f_x = f_y$.",
      "<strong>Principal Point $(c_x, c_y)$:</strong> Pixel coordinates where the camera's optical axis pierces the sensor. <strong>Skew $s$:</strong> Non-zero only if sensor axes are not orthogonal (usually $s = 0$)."
    ],
    "math": "$$K = \\begin{bmatrix} f_x & 0 & c_x \\\\ 0 & f_y & c_y \\\\ 0 & 0 & 1 \\end{bmatrix} \\quad (5 \\text{ Intrinsic Parameters for General CCD})$$",
    "personalConnection": "Measuring a printed photo with a misaligned ruler: $f_x, f_y$ scale millimeter distances into pixel tick marks, while $(c_x, c_y)$ shifts the ruler's zero-mark to the center of the photo.",
    "examTrap": "Never assume the principal point is at $(0, 0)$! In image coordinates, $(0,0)$ is the TOP-LEFT corner of the image. For a $1920 \\times 1080$ sensor, the principal point is approximately $(960, 540)$."
  },
  {
    "id": 40104,
    "subject": "DIP",
    "topicId": "01_Image_Formation_Camera_Geometry_and_Transformations",
    "topicTitle": "01 \u00b7 Image Formation & Transformations",
    "cardNumber": "04",
    "category": "2D TRANSFORMATIONS",
    "highlighterClass": "highlight-violet",
    "title": "2D Transformation Hierarchy: Euclidean to Projective",
    "textbookImg": "assets/dip_table2_3_affine.png",
    "textbookRef": "Gonzalez & Woods (4th ed), Table 2.3 (p. 104)",
    "drawingCaption": "Gonzalez & Woods Table 2.3: Affine Transformation Matrices (Identity, Scaling, Rotation, Translation, Shear)",
    "drawingSvg": "",
    "coreTranslation": [
      "<strong>1. Euclidean (Isometry, 3 DOF):</strong> Rotation + Translation ($R, t$). Preserves lengths, angles, and area.",
      "<strong>2. Similarity (4 DOF):</strong> Euclidean + Uniform Scale ($s R, t$). Preserves angles (shapes) and length ratios.",
      "<strong>3. Affine (6 DOF):</strong> Parallelism preserved; lines remain parallel. Preserves ratio of areas and parallel lengths.",
      "<strong>4. Projective (Homography, 8 DOF):</strong> Collinearity preserved (straight lines remain straight). Parallel lines converge to vanishing points!"
    ],
    "math": "$$H_{\\text{proj}} = \\begin{bmatrix} h_{11} & h_{12} & h_{13} \\\\ h_{21} & h_{22} & h_{23} \\\\ h_{31} & h_{32} & h_{33} \\end{bmatrix} \\quad (8 \\text{ Degrees of Freedom Up to Scale})$$",
    "personalConnection": "Looking at train tracks: in world coordinates, the tracks are Euclidean (parallel). In the camera's photo, perspective homography causes the parallel rails to intersect at a vanishing point on the horizon.",
    "examTrap": "An Affine transformation has $h_{31} = 0, h_{32} = 0, h_{33} = 1$. The bottom row $[0, 0, 1]$ is what preserves parallel lines! When $[h_{31}, h_{32}] \\ne [0, 0]$, lines converge."
  },
  {
    "id": 40105,
    "subject": "DIP",
    "topicId": "01_Image_Formation_Camera_Geometry_and_Transformations",
    "topicTitle": "01 \u00b7 Image Formation & Transformations",
    "cardNumber": "05",
    "category": "IMAGE WARPING",
    "highlighterClass": "highlight-indigo",
    "title": "Forward vs. Inverse Warping & Bilinear Interpolation",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\">\n  <defs>\n    <marker id=\"arr-dip5\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\">\n      <path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/>\n    </marker>\n  </defs>\n  <!-- Forward Warping Grid with Holes -->\n  <rect x=\"25\" y=\"30\" width=\"80\" height=\"70\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"3,3\"/>\n  <circle cx=\"45\" cy=\"50\" r=\"3\" fill=\"#000000\"/>\n  <circle cx=\"85\" cy=\"60\" r=\"3\" fill=\"#000000\"/>\n  <circle cx=\"65\" cy=\"85\" r=\"3\" fill=\"#000000\"/>\n  <text x=\"65\" y=\"115\" fill=\"#000000\" font-size=\"8.5\" font-family=\"sans-serif\" text-anchor=\"middle\">Forward: Holes &amp; Clumping</text>\n  <!-- Inverse Warping Grid -->\n  <rect x=\"135\" y=\"30\" width=\"80\" height=\"70\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.5\"/>\n  <circle cx=\"175\" cy=\"65\" r=\"3.5\" fill=\"#000000\"/>\n  <path d=\"M 175 65 Q 140 35 100 45\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.5\" marker-end=\"url(#arr-dip5)\"/>\n  <text x=\"175\" y=\"115\" fill=\"#000000\" font-size=\"8.5\" font-family=\"sans-serif\" font-weight=\"bold\" text-anchor=\"middle\">Inverse: Pull via H\u207b\u00b9</text>\n  <text x=\"120\" y=\"135\" fill=\"#000000\" font-size=\"8.5\" font-family=\"sans-serif\" text-anchor=\"middle\">Guarantees every output pixel is interpolated</text>\n</svg>",
    "drawingCaption": "Warping: Forward mapping leaves unsightly holes and moir\u00e9 artifacts; Inverse mapping guarantees every output pixel is filled",
    "coreTranslation": [
      "<strong>Forward Mapping:</strong> Iterates over input pixels $(x, y)$, computing destination $(x', y') = T(x, y)$. Since $(x', y')$ are floating-point numbers, rounding causes <strong>holes (unassigned pixels)</strong> and overlap collisions.",
      "<strong>Inverse Mapping (Standard):</strong> Iterates over every discrete destination pixel $(x', y')$, querying source position $(x, y) = T^{-1}(x', y')$.",
      "<strong>Bilinear Interpolation:</strong> Because $(x, y)$ falls between integer coordinates, its intensity is interpolated using a weighted average of its 4 nearest neighbors: $f(x, y) = (1-a)(1-b) f_{00} + a(1-b) f_{10} + (1-a)b f_{01} + ab f_{11}$."
    ],
    "math": "$$I_{\\text{dest}}(x', y') = I_{\\text{src}}(T^{-1}(x', y')) \\quad \\text{via Bilinear 4-Neighbor Interpolation}$$",
    "personalConnection": "Filling an ice cube tray: forward mapping is splashing water randomly from across the room (many cells stay dry). Inverse mapping is inspecting each cell directly and filling it from the pitcher.",
    "examTrap": "Forward mapping requires expensive splatting algorithms to avoid gaps. All production computer vision and DIP pipelines strictly use INVERSE warping with $T^{-1}$."
  },
  {
    "id": 40106,
    "subject": "DIP",
    "topicId": "01_Image_Formation_Camera_Geometry_and_Transformations",
    "topicTitle": "01 \u00b7 Image Formation & Transformations",
    "cardNumber": "06",
    "category": "WORKED BENCHMARK",
    "highlighterClass": "highlight-rose",
    "title": "Worked Benchmark: 4-Point Homography via DLT",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\">\n  <defs>\n    <marker id=\"arr-dip6\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\">\n      <path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/>\n    </marker>\n  </defs>\n  <!-- 4 matching points between two quadrilaterals -->\n  <polygon points=\"30,40 75,30 85,90 25,95\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.5\"/>\n  <circle cx=\"30\" cy=\"40\" r=\"3\" fill=\"#000000\"/>\n  <circle cx=\"75\" cy=\"30\" r=\"3\" fill=\"#000000\"/>\n  <circle cx=\"85\" cy=\"90\" r=\"3\" fill=\"#000000\"/>\n  <circle cx=\"25\" cy=\"95\" r=\"3\" fill=\"#000000\"/>\n  <!-- Arrow H -->\n  <line x1=\"95\" y1=\"65\" x2=\"140\" y2=\"65\" stroke=\"#000000\" stroke-width=\"2\" marker-end=\"url(#arr-dip6)\"/>\n  <text x=\"117\" y=\"58\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" font-weight=\"bold\" text-anchor=\"middle\">H (8 DOF)</text>\n  <!-- Target Rectified Quad -->\n  <rect x=\"150\" y=\"35\" width=\"65\" height=\"60\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.5\"/>\n  <circle cx=\"150\" cy=\"35\" r=\"3\" fill=\"#000000\"/>\n  <circle cx=\"215\" cy=\"35\" r=\"3\" fill=\"#000000\"/>\n  <circle cx=\"215\" cy=\"95\" r=\"3\" fill=\"#000000\"/>\n  <circle cx=\"150\" cy=\"95\" r=\"3\" fill=\"#000000\"/>\n  <text x=\"120\" y=\"125\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" font-weight=\"bold\" text-anchor=\"middle\">4 Point Matches \u21d2 8 Equations (Ah = 0)</text>\n</svg>",
    "drawingCaption": "Direct Linear Transformation: 4 coplanar point correspondences provide 8 independent equations to solve 3\u00d73 matrix H",
    "coreTranslation": [
      "<strong>Problem:</strong> How many point correspondences are needed to estimate a 2D homography $H$, and how is it computed?",
      "<strong>Degree of Freedom Count:</strong> A $3 \\times 3$ homography matrix has 9 elements, but overall scale is arbitrary $\\implies$ <strong>8 Degrees of Freedom</strong>.",
      "Each point match $(x_i, y_i) \\leftrightarrow (x_i', y_i')$ gives 2 independent linear equations: $x_i' (h_{31} x_i + h_{32} y_i + h_{33}) = h_{11} x_i + h_{12} y_i + h_{13}$.",
      "Therefore, exactly <strong>4 point correspondences</strong> (no three collinear) yield 8 equations $A h = 0$. The solution is the eigenvector of $A^T A$ corresponding to the smallest eigenvalue (SVD)."
    ],
    "math": "$$A h = \\mathbf{0}, \\quad A \\in \\mathbb{R}^{8 \\times 9}, \\quad h = \\arg\\min_{\\|h\\|=1} \\|A h\\| \\implies h = v_9 \\text{ of } \\operatorname{SVD}(A)$$",
    "personalConnection": "Scanning a document with your phone from an angle: the phone finds the 4 corners of the paper and applies the 4-point homography $H$ to un-skew the rectangular page flat on your screen.",
    "examTrap": "Collinear points trap: If any 3 of the 4 points lie on a straight line, the rows of matrix $A$ become linearly dependent, causing SVD estimation to fail completely."
  }
];
