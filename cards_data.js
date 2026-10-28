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
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\">\n  <defs>\n    <marker id=\"arr-101\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\">\n      <path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/>\n    </marker>\n  </defs>\n  <!-- Open Ball B_eps(x) -->\n  <circle cx=\"65\" cy=\"72\" r=\"38\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.5\" stroke-dasharray=\"4,3\"/>\n  <circle cx=\"65\" cy=\"72\" r=\"3\" fill=\"#000000\"/>\n  <line x1=\"65\" y1=\"72\" x2=\"93\" y2=\"48\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-101)\"/>\n  <text x=\"82\" y=\"56\" fill=\"#000000\" font-size=\"10\" font-family=\"serif\" font-style=\"italic\">\u03b5</text>\n  <text x=\"65\" y=\"87\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" text-anchor=\"middle\">x\u2080</text>\n  <text x=\"65\" y=\"124\" fill=\"#000000\" font-size=\"9\" font-family=\"sans-serif\" font-weight=\"bold\" text-anchor=\"middle\">B_\u03b5(x\u2080) (Open: Dashed)</text>\n\n  <!-- Compact Set K -->\n  <rect x=\"135\" y=\"34\" width=\"85\" height=\"76\" rx=\"14\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.8\"/>\n  <circle cx=\"177\" cy=\"72\" r=\"3\" fill=\"#000000\"/>\n  <text x=\"177\" y=\"64\" fill=\"#000000\" font-size=\"11\" font-family=\"serif\" font-style=\"italic\" font-weight=\"bold\" text-anchor=\"middle\">K</text>\n  <text x=\"177\" y=\"84\" fill=\"#000000\" font-size=\"8.5\" font-family=\"sans-serif\" text-anchor=\"middle\">Closed (Solid)</text>\n  <text x=\"177\" y=\"96\" fill=\"#000000\" font-size=\"8.5\" font-family=\"sans-serif\" text-anchor=\"middle\">+ Bounded</text>\n  <text x=\"177\" y=\"124\" fill=\"#000000\" font-size=\"9\" font-family=\"sans-serif\" font-weight=\"bold\" text-anchor=\"middle\">Compact Set</text>\n</svg>",
    "drawingCaption": "Open ball B_\u03b5(x) with dashed boundary vs. Compact set K (closed solid boundary & bounded)",
    "coreTranslation": [
      "An <strong>Open Set $S \\subset \\mathbb{R}^n$</strong> contains an open ball $B_\\epsilon(x) = \\{y : \\|y-x\\| < \\epsilon\\} \\subset S$ around every interior point.",
      "A <strong>Closed Set</strong> contains all of its boundary limit points: if a sequence $x_k \\in S \\to x^*$, the limit point $x^* \\in S$ must belong to $S$.",
      "<strong>Heine-Borel Theorem:</strong> In Euclidean space $\\mathbb{R}^n$, a subset $K$ is <strong>compact</strong> if and only if it is simultaneously <strong>closed and bounded</strong>."
    ],
    "math": "$$K \\subset \\mathbb{R}^n \\text{ is compact} \\iff K \\text{ is closed and bounded}$$",
    "personalConnection": "A walled garden with a locked gate is compact (closed boundary, finite perimeter). An infinite runway is closed but unbounded. A garden with missing fence boards is bounded but not closed.",
    "examTrap": "Heine-Borel strictly fails in infinite dimensions! In infinite-dimensional function spaces (such as $L^2$ or Sobolev spaces), a closed and bounded unit ball is NEVER compact."
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
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\">\n  <defs>\n    <marker id=\"arr-102\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\">\n      <path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/>\n    </marker>\n  </defs>\n  <!-- Axes -->\n  <line x1=\"25\" y1=\"120\" x2=\"225\" y2=\"120\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-102)\"/>\n  <line x1=\"35\" y1=\"130\" x2=\"35\" y2=\"15\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-102)\"/>\n  <text x=\"225\" y=\"132\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\">x</text>\n  <text x=\"25\" y=\"20\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\">y</text>\n  <!-- Curve approaching jump from left -->\n  <path d=\"M 45 50 Q 80 55 110 68\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.8\"/>\n  <circle cx=\"110\" cy=\"68\" r=\"3.5\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.5\"/>\n  <!-- Downward jump point (solid black) -->\n  <circle cx=\"110\" cy=\"92\" r=\"3.5\" fill=\"#000000\"/>\n  <!-- Curve continuing right -->\n  <path d=\"M 110 92 Q 160 96 210 38\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.8\"/>\n  <!-- Sublevel threshold alpha -->\n  <line x1=\"30\" y1=\"78\" x2=\"220\" y2=\"78\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"4,3\"/>\n  <text x=\"20\" y=\"81\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\">\u03b1</text>\n  <line x1=\"110\" y1=\"92\" x2=\"110\" y2=\"120\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"2,2\"/>\n  <text x=\"110\" y=\"132\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" text-anchor=\"middle\">x\u2080</text>\n  <text x=\"155\" y=\"108\" fill=\"#000000\" font-size=\"8.5\" font-family=\"sans-serif\" font-style=\"italic\">f(x\u2080) \u2264 liminf f(x)</text>\n</svg>",
    "drawingCaption": "Lower semicontinuity: Function can jump downward at boundary x\u2080, ensuring sublevel set {x : f(x) \u2264 \u03b1} is closed",
    "coreTranslation": [
      "A function $f: \\mathbb{R}^n \\to \\mathbb{R}$ is <strong>Lower Semicontinuous (LSC)</strong> if at every point $x_0$, $\\liminf_{x \\to x_0} f(x) \\ge f(x_0)$. It can jump downward, but never jump upward.",
      "<strong>Sublevel Set Equivalence:</strong> $f$ is LSC if and only if for every scalar threshold $\\alpha \\in \\mathbb{R}$, the sublevel set $\\mathcal{L}_\\alpha(f) = \\{x \\in \\mathbb{R}^n : f(x) \\le \\alpha\\}$ is <strong>closed</strong>.",
      "Lower semicontinuity is the exact mathematical property needed to preserve minima: limits of minimizing sequences stay within closed sublevel sets."
    ],
    "math": "$$\\liminf_{x \\to x_0} f(x) \\ge f(x_0) \\iff \\mathcal{L}_\\alpha(f) = \\{x : f(x) \\le \\alpha\\} \\text{ is closed } \\forall \\alpha$$",
    "personalConnection": "Walking down basement stairs: if a step abruptly drops 2 inches lower, you step onto solid stone, never falling through an imaginary floor. The true value at the drop is at or below incoming heights.",
    "examTrap": "Full continuity is NOT required for minimum attainment! Lower semicontinuity is the exact minimal condition needed for global infimum attainment. Upper semicontinuity guarantees maximum attainment."
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
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\">\n  <defs>\n    <marker id=\"arr-103\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\">\n      <path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/>\n    </marker>\n  </defs>\n  <!-- Axes -->\n  <line x1=\"25\" y1=\"120\" x2=\"225\" y2=\"120\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-103)\"/>\n  <line x1=\"35\" y1=\"130\" x2=\"35\" y2=\"15\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-103)\"/>\n  <!-- Compact interval [a, b] on axis -->\n  <line x1=\"60\" y1=\"120\" x2=\"195\" y2=\"120\" stroke=\"#000000\" stroke-width=\"3\"/>\n  <line x1=\"60\" y1=\"115\" x2=\"60\" y2=\"125\" stroke=\"#000000\" stroke-width=\"2\"/>\n  <line x1=\"195\" y1=\"115\" x2=\"195\" y2=\"125\" stroke=\"#000000\" stroke-width=\"2\"/>\n  <text x=\"60\" y=\"134\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" text-anchor=\"middle\">a</text>\n  <text x=\"195\" y=\"134\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" text-anchor=\"middle\">b</text>\n  <!-- Continuous curve on [a, b] -->\n  <path d=\"M 60 70 Q 95 22 120 75 T 195 40\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2\"/>\n  <!-- Max point -->\n  <circle cx=\"95\" cy=\"36\" r=\"3.5\" fill=\"#000000\"/>\n  <text x=\"95\" y=\"26\" fill=\"#000000\" font-size=\"9\" font-family=\"sans-serif\" font-weight=\"bold\" text-anchor=\"middle\">Max f(x)</text>\n  <!-- Min point -->\n  <circle cx=\"150\" cy=\"92\" r=\"3.5\" fill=\"#000000\"/>\n  <line x1=\"150\" y1=\"92\" x2=\"150\" y2=\"120\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"2,2\"/>\n  <text x=\"150\" y=\"105\" fill=\"#000000\" font-size=\"9\" font-family=\"sans-serif\" font-weight=\"bold\" text-anchor=\"middle\">Min f(x*)</text>\n  <text x=\"150\" y=\"134\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" text-anchor=\"middle\">x*</text>\n</svg>",
    "drawingCaption": "Weierstrass Theorem: Continuous curve on non-empty compact domain [a, b] physically attains both minimum and maximum",
    "coreTranslation": [
      "<strong>Theorem:</strong> Let $K \\subset \\mathbb{R}^n$ be non-empty and <strong>compact</strong> (closed & bounded), and let $f: K \\to \\mathbb{R}$ be <strong>continuous</strong> (or lower semicontinuous). Then $f$ attains its global minimum and maximum.",
      "<strong>Proof Engine:</strong> The continuous image $f(K) \\subset \\mathbb{R}$ is compact, hence closed and bounded. Since $f(K)$ is bounded below, infimum $m = \\inf_{x \\in K} f(x)$ exists and is finite. Since $f(K)$ is closed, $m \\in f(K)$, so $\\exists x^* \\in K$ with $f(x^*) = m$.",
      "This converts an abstract theoretical infimum $\\inf f(x)$ into an exact, physically reachable minimizer $\\min f(x) = f(x^*)$."
    ],
    "math": "$$K \\ne \\emptyset \\text{ compact, } f \\in C(K) \\implies \\exists x^* \\in K : f(x^*) = \\min_{x \\in K} f(x)$$",
    "personalConnection": "A roller coaster track constructed entirely inside an enclosed stadium (compact domain): the lowest point of the track is physically reachable and touching steel, rather than tapering off into infinity.",
    "examTrap": "If the domain is open (e.g. $K = (0, 1)$), $f(x) = x$ has infimum 0, but attains NO minimum in $K$! Both closedness and boundedness of the domain are strictly mandatory."
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
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\">\n  <defs>\n    <marker id=\"arr-104\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\">\n      <path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/>\n    </marker>\n  </defs>\n  <!-- Axes -->\n  <line x1=\"25\" y1=\"120\" x2=\"225\" y2=\"120\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-104)\"/>\n  <line x1=\"120\" y1=\"130\" x2=\"120\" y2=\"15\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-104)\"/>\n  <!-- Sublevel region shaded -->\n  <path d=\"M 68 65 Q 120 115 172 65 Z\" fill=\"#f1f5f9\" stroke=\"none\"/>\n  <!-- Coercive bowl curve -->\n  <path d=\"M 45 22 Q 120 125 195 22\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2\"/>\n  <!-- Sublevel threshold line alpha -->\n  <line x1=\"30\" y1=\"65\" x2=\"210\" y2=\"65\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"4,3\"/>\n  <text x=\"215\" y=\"68\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\">\u03b1</text>\n  <!-- Interval on axis -->\n  <line x1=\"68\" y1=\"65\" x2=\"68\" y2=\"120\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"2,2\"/>\n  <line x1=\"172\" y1=\"65\" x2=\"172\" y2=\"120\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"2,2\"/>\n  <line x1=\"68\" y1=\"120\" x2=\"172\" y2=\"120\" stroke=\"#000000\" stroke-width=\"2.5\"/>\n  <text x=\"120\" y=\"88\" fill=\"#000000\" font-size=\"9\" font-family=\"sans-serif\" font-weight=\"bold\" text-anchor=\"middle\">S_\u03b1 is Compact</text>\n  <text x=\"120\" y=\"133\" fill=\"#000000\" font-size=\"8.5\" font-family=\"serif\" font-style=\"italic\" text-anchor=\"middle\">Bounded interval {x : f(x) \u2264 \u03b1}</text>\n  <text x=\"45\" y=\"15\" fill=\"#000000\" font-size=\"8\" font-family=\"sans-serif\">+\u221e</text>\n  <text x=\"195\" y=\"15\" fill=\"#000000\" font-size=\"8\" font-family=\"sans-serif\">+\u221e</text>\n</svg>",
    "drawingCaption": "Coercivity: Objective blows up as ||x|| \u2192 \u221e, trapping minimizing search inside compact sublevel set S",
    "coreTranslation": [
      "In unconstrained optimization on $\\mathbb{R}^n$, the domain is unbounded, so Weierstrass theorem cannot be applied directly.",
      "<strong>Coercivity:</strong> $f: \\mathbb{R}^n \\to \\mathbb{R}$ is coercive if $\\lim_{\\|x\\| \\to \\infty} f(x) = +\\infty$. As you escape toward infinity in any radial direction, the objective blows up.",
      "<strong>Compactness Recovery:</strong> Pick any basepoint $x_0$. The sublevel set $S = \\{x : f(x) \\le f(x_0)\\}$ is <strong>bounded</strong> and closed, hence <strong>compact</strong>. Applying Weierstrass on $S$ guarantees global minimizer $x^*$ exists on all of $\\mathbb{R}^n$!"
    ],
    "math": "$$\\lim_{\\|x\\| \\to \\infty} f(x) = +\\infty \\implies \\mathcal{L}_\\alpha = \\{x : f(x) \\le \\alpha\\} \\text{ is compact} \\implies \\min_{x \\in \\mathbb{R}^n} f(x) \\text{ exists}$$",
    "personalConnection": "A deep soup bowl with steep walls: no matter which direction you kick a marble, it climbs infinite walls. The marble must settle at a global low point in the finite bowl bottom.",
    "examTrap": "A function strictly bounded below by zero (like $f(x) = e^{-x^2}$ or $f(x) = \\frac{1}{1+x^2}$) is NOT coercive! It has infimum 0, but attains NO minimum anywhere on $\\mathbb{R}$."
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
    "drawingCaption": "Luenberger Fig. 7.5: The epigraph epi(f) in R\u207f\u207a\u00b9 is a convex set supported by a non-vertical hyperplane",
    "coreTranslation": [
      "The <strong>Epigraph</strong> of $f$ is the set of all points lying on or above its graph in $\\mathbb{R}^{n+1}$: $\\operatorname{epi}(f) = \\{(x, t) \\in \\mathbb{R}^n \\times \\mathbb{R} : f(x) \\le t\\}$.",
      "<strong>Fundamental Geometric Bridge:</strong> A function $f$ is a <strong>convex function</strong> if and only if its epigraph $\\operatorname{epi}(f)$ is a <strong>convex set</strong>.",
      "Horizontal slices of $\\operatorname{epi}(f)$ at height $t = \\alpha$ are precisely the sublevel sets $\\mathcal{L}_\\alpha(f)$. If $f$ is convex, all its sublevel sets are convex."
    ],
    "math": "$$\\operatorname{epi}(f) = \\{(x, t) \\in \\mathbb{R}^{n+1} : f(x) \\le t\\}, \\quad f \\text{ is convex} \\iff \\operatorname{epi}(f) \\text{ is a convex set}$$",
    "personalConnection": "Pouring broth into a convex bowl: the broth filling the space above the ceramic interior is the epigraph. Any straight line drawn between two soup droplets remains entirely within the soup.",
    "examTrap": "The converse does NOT hold! A function with convex sublevel sets is NOT necessarily convex (it is only quasiconvex, e.g. $f(x) = \\sqrt{|x|}$ or $f(x) = \\log(x)$)."
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
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\">\n  <defs>\n    <marker id=\"arr-106\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\">\n      <path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/>\n    </marker>\n  </defs>\n  <!-- Axes -->\n  <line x1=\"20\" y1=\"72\" x2=\"225\" y2=\"72\" stroke=\"#000000\" stroke-width=\"1\" marker-end=\"url(#arr-106)\"/>\n  <line x1=\"120\" y1=\"135\" x2=\"120\" y2=\"10\" stroke=\"#000000\" stroke-width=\"1\" marker-end=\"url(#arr-106)\"/>\n  <text x=\"225\" y=\"84\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\">x\u2081</text>\n  <text x=\"126\" y=\"15\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\">x\u2082</text>\n  <!-- Concentric Contours -->\n  <ellipse cx=\"120\" cy=\"72\" rx=\"30\" ry=\"18\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1\"/>\n  <ellipse cx=\"120\" cy=\"72\" rx=\"60\" ry=\"34\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.2\"/>\n  <ellipse cx=\"120\" cy=\"72\" rx=\"95\" ry=\"52\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.5\"/>\n  <text x=\"153\" y=\"70\" fill=\"#000000\" font-size=\"8\" font-family=\"monospace\">c=1</text>\n  <text x=\"183\" y=\"70\" fill=\"#000000\" font-size=\"8\" font-family=\"monospace\">c=5</text>\n  <text x=\"212\" y=\"70\" fill=\"#000000\" font-size=\"8\" font-family=\"monospace\">c=20</text>\n  <circle cx=\"120\" cy=\"72\" r=\"3\" fill=\"#000000\"/>\n  <text x=\"120\" y=\"132\" fill=\"#000000\" font-size=\"9\" font-family=\"sans-serif\" font-weight=\"bold\" text-anchor=\"middle\">All Sublevel Sets Closed &amp; Bounded</text>\n</svg>",
    "drawingCaption": "Worked Template: Level curves bounded by compact set S containing global minima (\u00b11, \u00b11)",
    "coreTranslation": [
      "<strong>Problem:</strong> Prove that $f(x_1, x_2) = x_1^4 + x_2^4 - 4x_1 x_2$ attains a global minimum on $\\mathbb{R}^2$.",
      "<strong>Step 1 (Coercivity):</strong> By AM-GM, $4|x_1 x_2| \\le 2(x_1^2 + x_2^2)$. For large $\\|x\\|$, fourth-order terms dominate quadratics: $f(x) \\ge \\frac{1}{2}(x_1^4 + x_2^4) - C \\to +\\infty$. Thus $f$ is coercive.",
      "<strong>Step 2 (Weierstrass on S):</strong> Choose $x_0 = (0,0)$ where $f(0,0)=0$. The sublevel set $S = \\{x : f(x) \\le 0\\}$ is closed and bounded (compact). By Weierstrass, $\\exists x^* \\in S$ achieving $\\min f(x) = -2$ at $(\\pm 1, \\pm 1)$."
    ],
    "math": "$$f(x) \\ge \\frac{1}{2}\\|x\\|^4 - C \\implies \\lim_{\\|x\\| \\to \\infty} f(x) = +\\infty \\implies \\min_{x \\in \\mathbb{R}^2} f(x) \\text{ is attained}$$",
    "personalConnection": "The 3-Step IISc Proof Template: (1) Lower bound by radial norm $\\to$ prove coercivity. (2) Choose base point $x_0$ to isolate compact sublevel set $S$. (3) Invoke Weierstrass on $S$.",
    "examTrap": "Don't just set $\\nabla f(x) = 0$! Stationary points only give local candidates. Setting gradient to zero without proving coercivity leaves the question of whether a global minimum exists completely unanswered."
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
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\">\n  <defs>\n    <marker id=\"arr-201\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\">\n      <path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/>\n    </marker>\n  </defs>\n  <!-- Axes -->\n  <line x1=\"25\" y1=\"125\" x2=\"225\" y2=\"125\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-201)\"/>\n  <line x1=\"35\" y1=\"135\" x2=\"35\" y2=\"15\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-201)\"/>\n  <!-- Tangent line (1st order) -->\n  <line x1=\"45\" y1=\"110\" x2=\"195\" y2=\"35\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"3,3\"/>\n  <text x=\"198\" y=\"38\" fill=\"#000000\" font-size=\"8\" font-family=\"sans-serif\">1st Order (Linear)</text>\n  <!-- 2nd order osculating parabola -->\n  <path d=\"M 50 115 Q 110 75 180 30\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.5\" stroke-dasharray=\"5,3\"/>\n  <text x=\"175\" y=\"20\" fill=\"#000000\" font-size=\"8\" font-family=\"sans-serif\">2nd Order (Quadratic)</text>\n  <!-- True function f(x) -->\n  <path d=\"M 50 115 Q 110 75 185 45\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.2\"/>\n  <text x=\"190\" y=\"55\" fill=\"#000000\" font-size=\"8.5\" font-family=\"serif\" font-style=\"italic\" font-weight=\"bold\">f(x) True</text>\n  <!-- Expansion point x\u2080 -->\n  <circle cx=\"110\" cy=\"75\" r=\"3.5\" fill=\"#000000\"/>\n  <line x1=\"110\" y1=\"75\" x2=\"110\" y2=\"125\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"2,2\"/>\n  <text x=\"110\" y=\"136\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" text-anchor=\"middle\">x\u2080</text>\n</svg>",
    "drawingCaption": "Taylor Quadratic Approximation: Local landscape modeled by gradient slope \u2207f and curvature Hessian \u2207\u00b2f",
    "coreTranslation": [
      "For $f \\in C^2(\\mathbb{R}^n)$, the 2nd-order expansion along perturbation $d$ is: $f(x+d) = f(x) + \\nabla f(x)^T d + \\frac{1}{2} d^T \\nabla^2 f(x) d + o(\\|d\\|^2)$.",
      "<strong>Mean-Value Remainder:</strong> There exists $\\theta \\in (0, 1)$ such that the remainder is exact: $R_2 = \\frac{1}{2} d^T \\nabla^2 f(x + \\theta d) d$.",
      "The quadratic model $m(d) = f(x) + \\nabla f(x)^T d + \\frac{1}{2} d^T B d$ forms the foundational engine for all Newton, Quasi-Newton, and trust-region algorithms."
    ],
    "math": "$$f(x+d) = f(x) + \\nabla f(x)^T d + \\frac{1}{2} d^T \\nabla^2 f(x+\\theta d) d, \\quad \\theta \\in (0, 1)$$",
    "personalConnection": "Walking through hilly terrain in thick fog with a flashlight: your current elevation is $f(x)$, the slope under your boots is $\\nabla f(x)$, and the bowl curvature around your feet is $\\nabla^2 f(x)$.",
    "examTrap": "The Hessian $\\nabla^2 f(x)$ must be evaluated at an INTERMEDIATE point $x + \\theta d$ for exact equality! Evaluating at $x$ requires adding the asymptotic remainder term $o(\\|d\\|^2)$."
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
    "drawingCaption": "Luenberger Fig. 7.1: Directional derivative \u03d5'(0) = \u2207f(x*)\u1d40d must equal 0 in all directions d \u2208 R\u207f",
    "coreTranslation": [
      "<strong>Theorem (FONC):</strong> If $x^*$ is an unconstrained local minimizer of $f \\in C^1$, then the gradient must vanish: $\\nabla f(x^*) = 0$.",
      "<strong>Proof Engine:</strong> Define 1D slice $\\phi(t) = f(x^* + t d)$. Because $t=0$ is a local minimum of $\\phi(t)$, single-variable calculus gives $\\phi'(0) = 0$. By chain rule, $\\phi'(0) = \\nabla f(x^*)^T d = 0$.",
      "Because this holds for EVERY direction $d \\in \\mathbb{R}^n$, we choose $d = \\nabla f(x^*)$, which forces $\\|\\nabla f(x^*)\\|^2 = 0 \\implies \\nabla f(x^*) = 0$."
    ],
    "math": "$$x^* \\text{ local min of } f \\in C^1 \\implies \\nabla f(x^*) = \\mathbf{0}$$",
    "personalConnection": "Standing at the absolute bottom of a mountain pass: in whichever compass direction you take a tiny step, the instantaneous slope is zero; you neither gain nor lose height initially.",
    "examTrap": "FONC is strictly NECESSARY, not sufficient! A zero gradient $\\nabla f(x^*) = 0$ also occurs at local maxima and saddle points (e.g., $f(x_1, x_2) = x_1^2 - x_2^2$ at the origin)."
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
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\">\n  <defs>\n    <marker id=\"arr-203\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\">\n      <path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/>\n    </marker>\n  </defs>\n  <!-- Axes -->\n  <line x1=\"25\" y1=\"120\" x2=\"225\" y2=\"120\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-203)\"/>\n  <line x1=\"120\" y1=\"130\" x2=\"120\" y2=\"15\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-203)\"/>\n  <!-- Bowl curve -->\n  <path d=\"M 45 40 Q 120 115 195 40\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2\"/>\n  <!-- Flat horizontal tangent at x* -->\n  <line x1=\"60\" y1=\"95\" x2=\"180\" y2=\"95\" stroke=\"#000000\" stroke-width=\"1.5\" stroke-dasharray=\"4,3\"/>\n  <circle cx=\"120\" cy=\"95\" r=\"3.5\" fill=\"#000000\"/>\n  <text x=\"120\" y=\"83\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" font-weight=\"bold\" text-anchor=\"middle\">\u2207f(x*) = 0</text>\n  <text x=\"120\" y=\"112\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" text-anchor=\"middle\">x*</text>\n  <text x=\"120\" y=\"30\" fill=\"#000000\" font-size=\"9\" font-family=\"sans-serif\" font-weight=\"bold\" text-anchor=\"middle\">Hessian PSD: d\u1d40\u2207\u00b2f(x*)d \u2265 0 (\u2200 d)</text>\n</svg>",
    "drawingCaption": "SONC: At a local minimum, the terrain must curve upward or stay flat in every direction (\u2207\u00b2f(x*) \u2ab0 0)",
    "coreTranslation": [
      "<strong>Theorem (SONC):</strong> If $x^*$ is a local minimizer of $f \\in C^2$, then $\\nabla f(x^*) = 0$ AND the Hessian matrix is <strong>positive semidefinite</strong>: $\\nabla^2 f(x^*) \\succeq 0$.",
      "<strong>Proof:</strong> Using 2nd-order Taylor with $\\nabla f(x^*)=0$: $f(x^* + t d) - f(x^*) = \\frac{1}{2} t^2 d^T \\nabla^2 f(x^*) d + o(t^2) \\ge 0$. Dividing by $t^2$ and taking $t \\to 0$ yields $d^T \\nabla^2 f(x^*) d \\ge 0$ for all $d$.",
      "This implies that all eigenvalues of the Hessian at $x^*$ are non-negative: $\\lambda_i(\\nabla^2 f(x^*)) \\ge 0$ for all $i = 1, \\dots, n$."
    ],
    "math": "$$x^* \\text{ local min of } f \\in C^2 \\implies \\nabla f(x^*) = \\mathbf{0} \\quad \\text{and} \\quad \\nabla^2 f(x^*) \\succeq 0$$",
    "personalConnection": "A marble resting inside a teacup: any displacement encounters an upward slope. If even one direction curved downward, gravity would immediately roll the marble away.",
    "examTrap": "$\\nabla^2 f(x^*) \\succeq 0$ alone is NOT sufficient for a local minimum! Consider $f(x) = x^3$ at $x=0$: $f'(0)=0$ and $f''(0)=0 \\ge 0$, but $x=0$ is an inflection point, not a minimum."
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
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\">\n  <defs>\n    <marker id=\"arr-204\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\">\n      <path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/>\n    </marker>\n  </defs>\n  <!-- Axes -->\n  <line x1=\"25\" y1=\"120\" x2=\"225\" y2=\"120\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-204)\"/>\n  <line x1=\"120\" y1=\"130\" x2=\"120\" y2=\"15\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-204)\"/>\n  <!-- Strict bowl with shading -->\n  <path d=\"M 50 35 Q 120 115 190 35\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.2\"/>\n  <!-- Lower bounding quadratic (m/2)||d||^2 -->\n  <path d=\"M 65 48 Q 120 115 175 48\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"3,3\"/>\n  <circle cx=\"120\" cy=\"95\" r=\"3.5\" fill=\"#000000\"/>\n  <text x=\"120\" y=\"112\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" text-anchor=\"middle\">x* (Strict Local Minimum)</text>\n  <text x=\"120\" y=\"24\" fill=\"#000000\" font-size=\"9\" font-family=\"sans-serif\" font-weight=\"bold\" text-anchor=\"middle\">\u2207\u00b2f(x*) \u227b 0  (Strictly Positive Definite)</text>\n  <text x=\"120\" y=\"134\" fill=\"#000000\" font-size=\"8.5\" font-family=\"monospace\" text-anchor=\"middle\">\u03bb_min(\u2207\u00b2f) &gt; 0 \u21d2 Strict Isolation</text>\n</svg>",
    "drawingCaption": "SOSC: Strictly positive eigenvalues (\u03bb_min > 0) guarantee a strict local valley with quadratic growth",
    "coreTranslation": [
      "<strong>Theorem (SOSC):</strong> If $\\nabla f(x^*) = 0$ AND the Hessian is <strong>strictly positive definite</strong> ($\\nabla^2 f(x^*) \\succ 0$), then $x^*$ is a <strong>strict local minimizer</strong>.",
      "<strong>Proof Engine:</strong> Let $\\lambda_{\\min} > 0$ be the smallest eigenvalue of $\\nabla^2 f(x^*)$. By Rayleigh quotient, $d^T \\nabla^2 f(x^*) d \\ge \\lambda_{\\min} \\|d\\|^2$. Taylor expansion gives: $f(x^*+d) - f(x^*) \\ge \\frac{1}{2} \\lambda_{\\min} \\|d\\|^2 + o(\\|d\\|^2) > 0$ for all small $d \\ne 0$.",
      "This condition is completely decisive: no higher-order derivatives need to be evaluated once $\\lambda_{\\min} > 0$ is verified."
    ],
    "math": "$$\\nabla f(x^*) = \\mathbf{0} \\quad \\text{and} \\quad \\nabla^2 f(x^*) \\succ 0 \\implies x^* \\text{ is a strict local minimizer}$$",
    "personalConnection": "Sitting in the center of a parabolic satellite dish: every radial direction pushes you strictly upward with nonzero quadratic curvature. You are trapped at a guaranteed strict local low point.",
    "examTrap": "SOSC requires STRICT inequality $\\nabla^2 f(x^*) \\succ 0$. If $\\lambda_{\\min} = 0$ (e.g. $f(x) = x^4$ at $x=0$), $x^*$ can still be a minimizer, but SOSC fails to prove it and 4th-order analysis is needed."
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
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\">\n  <defs>\n    <marker id=\"arr-205\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\">\n      <path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/>\n    </marker>\n  </defs>\n  <!-- Contour hyperbolas of saddle f = x1^2 - x2^2 -->\n  <line x1=\"20\" y1=\"72\" x2=\"220\" y2=\"72\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-205)\"/>\n  <line x1=\"120\" y1=\"135\" x2=\"120\" y2=\"10\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-205)\"/>\n  <text x=\"220\" y=\"84\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\">x\u2081</text>\n  <text x=\"126\" y=\"18\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\">x\u2082</text>\n  <!-- Asymptotes x1 = +/- x2 -->\n  <line x1=\"50\" y1=\"122\" x2=\"190\" y2=\"22\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"3,3\"/>\n  <line x1=\"50\" y1=\"22\" x2=\"190\" y2=\"122\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"3,3\"/>\n  <!-- Hyperbolic branches -->\n  <path d=\"M 60 72 Q 95 72 100 20\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.5\"/>\n  <path d=\"M 60 72 Q 95 72 100 124\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.5\"/>\n  <path d=\"M 180 72 Q 145 72 140 20\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.5\"/>\n  <path d=\"M 180 72 Q 145 72 140 124\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.5\"/>\n  <!-- Saddle point -->\n  <circle cx=\"120\" cy=\"72\" r=\"3.5\" fill=\"#000000\"/>\n  <text x=\"120\" y=\"60\" fill=\"#000000\" font-size=\"9\" font-family=\"sans-serif\" font-weight=\"bold\" text-anchor=\"middle\">Saddle Point (\u03bb\u2081 &gt; 0, \u03bb\u2082 &lt; 0)</text>\n  <text x=\"120\" y=\"134\" fill=\"#000000\" font-size=\"8.5\" font-family=\"sans-serif\" text-anchor=\"middle\">Indefinite Hessian: Neither Min nor Max</text>\n</svg>",
    "drawingCaption": "Saddle Point: Hessian has mixed eigenvalue signs (\u03bb\u2081 > 0, \u03bb\u2082 < 0), permitting descent along negative eigenvector",
    "coreTranslation": [
      "At any critical point where $\\nabla f(x^*) = 0$, the Hessian eigenvalues $\\{\\lambda_1, \\dots, \\lambda_n\\}$ govern the local topology:",
      "<strong>Local Minimum:</strong> All $\\lambda_i > 0$ (positive definite). <strong>Local Maximum:</strong> All $\\lambda_i < 0$ (negative definite).",
      "<strong>Saddle Point:</strong> Both positive and negative eigenvalues exist (indefinite). The eigenvector $v$ corresponding to $\\lambda_{\\min} < 0$ provides a strict <strong>negative curvature descent direction</strong>: $v^T \\nabla^2 f(x^*) v < 0$."
    ],
    "math": "$$\\text{Saddle Point} \\iff \\exists \\, i, j \\text{ s.t. } \\lambda_i(\\nabla^2 f(x^*)) > 0 \\text{ and } \\lambda_j(\\nabla^2 f(x^*)) < 0$$",
    "personalConnection": "A horse saddle or mountain pass: you are at the lowest point along the north-south ridge, but at the highest point along the east-west trail.",
    "examTrap": "Sylvester's Criterion for negative definiteness requires alternating leading principal minors: $(-1)^k \\Delta_k > 0$ ($\\Delta_1 < 0, \\Delta_2 > 0, \\Delta_3 < 0$). Many students erroneously check if all $\\Delta_k < 0$."
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
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\">\n  <defs>\n    <marker id=\"arr-206\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\">\n      <path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/>\n    </marker>\n  </defs>\n  <!-- Banana valley contour lines -->\n  <path d=\"M 35 110 Q 110 130 155 80 T 215 25\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"3,3\"/>\n  <path d=\"M 45 100 Q 115 120 155 75 T 205 32\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.2\"/>\n  <path d=\"M 55 90 Q 120 110 155 70 T 195 40\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.5\"/>\n  <!-- Parabolic trough x2 = x1^2 -->\n  <path d=\"M 60 85 Q 125 105 155 65\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2\"/>\n  <!-- Global min at (1, 1) -->\n  <circle cx=\"155\" cy=\"65\" r=\"4\" fill=\"#000000\"/>\n  <text x=\"175\" y=\"68\" fill=\"#000000\" font-size=\"9\" font-family=\"sans-serif\" font-weight=\"bold\">x* = (1, 1)</text>\n  <text x=\"120\" y=\"22\" fill=\"#000000\" font-size=\"9\" font-family=\"sans-serif\" font-weight=\"bold\" text-anchor=\"middle\">Rosenbrock Banana Valley: x\u2082 = x\u2081\u00b2</text>\n  <text x=\"120\" y=\"136\" fill=\"#000000\" font-size=\"8.5\" font-family=\"monospace\" text-anchor=\"middle\">f(x) = 100(x\u2082 - x\u2081\u00b2)\u00b2 + (1 - x\u2081)\u00b2</text>\n</svg>",
    "drawingCaption": "Rosenbrock Valley: Deep parabolic trough x\u2082 = x\u2081\u00b2 leading to unique global minimum at (1, 1)",
    "coreTranslation": [
      "<strong>Problem:</strong> Analyze critical points of Rosenbrock's function $f(x, y) = 100(y - x^2)^2 + (1 - x)^2$.",
      "<strong>Step 1 (Gradient = 0):</strong> $\\nabla f = [-400x(y-x^2) - 2(1-x), \\; 200(y-x^2)]^T = [0, 0]^T$. The 2nd equation gives $y = x^2$. Substituting into 1st gives $-2(1-x) = 0 \\implies x^* = 1, y^* = 1$.",
      "<strong>Step 2 (Hessian at (1, 1)):</strong> $\\nabla^2 f(1, 1) = \\begin{bmatrix} 802 & -400 \\\\ -400 & 200 \\end{bmatrix}$. Trace $= 1002 > 0$, Determinant $= 802(200) - 160000 = 400 > 0$. Both eigenvalues are strictly positive $\\implies$ unique strict local (and global) minimum!"
    ],
    "math": "$$\\nabla f(1, 1) = \\mathbf{0}, \\quad \\det(\\nabla^2 f) = 400 > 0, \\quad \\operatorname{tr}(\\nabla^2 f) = 1002 > 0 \\implies (1,1) \\text{ is strict min}$$",
    "personalConnection": "Finding the drain in a curved sink: the valley bottom is along $y = x^2$. Moving along the valley requires tiny adjustments because the Hessian condition number $\\kappa \\approx 2500$ is massive.",
    "examTrap": "When evaluating $2 \\times 2$ Hessians, always check BOTH $\\det(H) > 0$ and $\\operatorname{tr}(H) > 0$. If $\\det(H) > 0$ and $\\operatorname{tr}(H) < 0$, both eigenvalues are negative, giving a local MAXIMUM!"
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
    "drawingCaption": "Luenberger Fig. 7.3: Convex function chord lies on or above function curve; nonconvex function dips below chord",
    "coreTranslation": [
      "A set $C \\subset \\mathbb{R}^n$ is <strong>Convex</strong> if for any $x, y \\in C$ and $\\theta \\in [0, 1]$, the line segment $\\theta x + (1-\\theta)y \\in C$ remains inside $C$.",
      "A function $f: C \\to \\mathbb{R}$ is <strong>Convex</strong> if for all $x, y \\in C$ and $\\theta \\in [0, 1]$: $f(\\theta x + (1-\\theta)y) \\le \\theta f(x) + (1-\\theta)f(y)$.",
      "Geometrically, the secant line segment joining $(x, f(x))$ and $(y, f(y))$ lies completely on or above the graph of $f$."
    ],
    "math": "$$f(\\theta x + (1-\\theta)y) \\le \\theta f(x) + (1-\\theta)f(y) \\quad \\forall \\, x, y \\in C, \\; \\theta \\in [0, 1]$$",
    "personalConnection": "A taut guitar string stretched between two frets: the vibrating string always hovers above the wooden dip of the hollow fretboard.",
    "examTrap": "The domain $C$ of $f$ MUST be a convex set for the definition to even be valid! You cannot define convexity on disjoint or non-convex domains like $C = \\mathbb{R} \\setminus \\{0\\}$."
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
    "drawingCaption": "Luenberger Fig. 7.4: Tangent hyperplane at any point x globally under-estimates the entire convex curve f(y)",
    "coreTranslation": [
      "<strong>Theorem:</strong> Let $f \\in C^1$ on convex open set $C$. Then $f$ is convex if and only if for all $x, y \\in C$: $f(y) \\ge f(x) + \\nabla f(x)^T(y - x)$.",
      "<strong>Global Underestimator:</strong> The 1st-order Taylor affine approximation at ANY point $x$ forms a global lower bound across the ENTIRE domain.",
      "<strong>Critical Consequence:</strong> If $\\nabla f(x^*) = 0$, then $f(y) \\ge f(x^*) + 0^T(y - x) = f(x^*)$ for all $y$. Thus, <strong>every stationary point of a convex function is a global minimizer!</strong>"
    ],
    "math": "$$f \\text{ is convex} \\iff f(y) \\ge f(x) + \\nabla f(x)^T (y - x) \\quad \\forall \\, x, y$$",
    "personalConnection": "Holding a stiff piece of cardboard flat against a smooth bowl: the cardboard touches the bowl at exactly one tangent point and rests strictly underneath the rest of the bowl everywhere else.",
    "examTrap": "Monotonicity of gradient is completely equivalent: $( \\nabla f(y) - \\nabla f(x) )^T (y - x) \\ge 0$. In 1D, this simply states that the derivative $f'(x)$ is non-decreasing."
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
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\">\n  <defs>\n    <marker id=\"arr-303\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\">\n      <path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/>\n    </marker>\n  </defs>\n  <!-- Axes -->\n  <line x1=\"25\" y1=\"120\" x2=\"225\" y2=\"120\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-303)\"/>\n  <line x1=\"120\" y1=\"130\" x2=\"120\" y2=\"15\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-303)\"/>\n  <!-- Globally convex curve -->\n  <path d=\"M 40 25 Q 120 115 200 25\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2\"/>\n  <!-- Tangents at x and y -->\n  <line x1=\"45\" y1=\"95\" x2=\"115\" y2=\"55\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"3,3\"/>\n  <circle cx=\"80\" cy=\"75\" r=\"3.5\" fill=\"#000000\"/>\n  <text x=\"75\" y=\"90\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\">x</text>\n  <line x1=\"125\" y1=\"55\" x2=\"195\" y2=\"95\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"3,3\"/>\n  <circle cx=\"160\" cy=\"75\" r=\"3.5\" fill=\"#000000\"/>\n  <text x=\"165\" y=\"90\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\">y</text>\n  <text x=\"120\" y=\"24\" fill=\"#000000\" font-size=\"9\" font-family=\"sans-serif\" font-weight=\"bold\" text-anchor=\"middle\">\u2207\u00b2f(x) \u2ab0 0  \u2200 x \u2208 C  (Global Convexity)</text>\n  <text x=\"120\" y=\"134\" fill=\"#000000\" font-size=\"8.5\" font-family=\"sans-serif\" text-anchor=\"middle\">Every stationary point is a global minimum</text>\n</svg>",
    "drawingCaption": "Second-Order Convexity: Hessian matrix \u2207\u00b2f(x) must remain positive semidefinite everywhere across domain C",
    "coreTranslation": [
      "<strong>Theorem:</strong> Let $f \\in C^2$ on convex open set $C$. Then $f$ is convex if and only if its Hessian is <strong>positive semidefinite everywhere</strong>: $\\nabla^2 f(x) \\succeq 0$ for all $x \\in C$.",
      "This means that at every single point $x \\in C$, all eigenvalues of $\\nabla^2 f(x)$ are non-negative: $\\lambda_{\\min}(\\nabla^2 f(x)) \\ge 0$.",
      "For quadratic $f(x) = \\frac{1}{2} x^T Q x - b^T x$, $\\nabla^2 f(x) = Q$. Hence $f$ is convex if and only if the matrix $Q \\succeq 0$."
    ],
    "math": "$$f \\text{ is convex on } C \\iff \\nabla^2 f(x) \\succeq 0 \\quad \\forall \\, x \\in C$$",
    "personalConnection": "A car driving across undulating hills: if the driver's stomach always feels pressed down into the seat (positive vertical acceleration) and never floats upward, the terrain is convex.",
    "examTrap": "Do not confuse $\\nabla^2 f(x^*) \\succeq 0$ at a single critical point (which is merely SONC for a local min) with $\\nabla^2 f(x) \\succeq 0$ for ALL $x \\in C$ (which proves global convexity of $f$)."
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
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\">\n  <defs>\n    <marker id=\"arr-304\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\">\n      <path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/>\n    </marker>\n  </defs>\n  <!-- Linear tangent -->\n  <line x1=\"40\" y1=\"110\" x2=\"200\" y2=\"50\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"3,3\"/>\n  <text x=\"202\" y=\"52\" fill=\"#000000\" font-size=\"8\" font-family=\"sans-serif\">Linear Tangent</text>\n  <!-- Quadratic lower bound -->\n  <path d=\"M 45 95 Q 100 88 190 35\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.5\" stroke-dasharray=\"4,3\"/>\n  <text x=\"195\" y=\"32\" fill=\"#000000\" font-size=\"8\" font-family=\"sans-serif\">+ (m/2)||y-x||\u00b2</text>\n  <!-- True function f(y) -->\n  <path d=\"M 45 80 Q 100 88 185 20\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.2\"/>\n  <text x=\"185\" y=\"14\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" font-weight=\"bold\">f(y)</text>\n  <!-- Expansion point x -->\n  <circle cx=\"100\" cy=\"88\" r=\"3.5\" fill=\"#000000\"/>\n  <text x=\"100\" y=\"104\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" text-anchor=\"middle\">x</text>\n  <text x=\"120\" y=\"132\" fill=\"#000000\" font-size=\"9\" font-family=\"sans-serif\" font-weight=\"bold\" text-anchor=\"middle\">m-Strong Convexity: Strict Quadratic Growth</text>\n</svg>",
    "drawingCaption": "Strong Convexity: Objective is uniformly curved with a quadratic lower bowl parameter \u03bc > 0",
    "coreTranslation": [
      "A function $f$ is <strong>$\\mu$-Strongly Convex</strong> ($\\mu > 0$) if $g(x) = f(x) - \\frac{\\mu}{2}\\|x\\|^2$ is convex.",
      "<strong>Quadratic Underestimator:</strong> $f(y) \\ge f(x) + \\nabla f(x)^T(y-x) + \\frac{\\mu}{2}\\|y-x\\|^2$. It grows at least quadratically away from any point.",
      "<strong>Second-Order Equivalent:</strong> $\\nabla^2 f(x) \\succeq \\mu I$, meaning the minimum eigenvalue is uniformly bounded away from zero: $\\lambda_{\\min}(\\nabla^2 f(x)) \\ge \\mu > 0$."
    ],
    "math": "$$f \\text{ is } \\mu\\text{-strongly convex} \\iff \\nabla^2 f(x) \\succeq \\mu I \\quad \\forall \\, x$$",
    "personalConnection": "A heavy steel spring: the further you compress or stretch it, the restoring force pushes back with strict linear resistance and quadratic energy storage $\\frac{1}{2} k x^2$.",
    "examTrap": "Strict convexity does NOT imply strong convexity! For instance, $f(x) = x^4$ is strictly convex on $\\mathbb{R}$, but its 2nd derivative $f''(0) = 0$, so it is NOT strongly convex ($\\mu = 0$)."
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
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\">\n  <defs>\n    <marker id=\"arr-305\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\">\n      <path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/>\n    </marker>\n  </defs>\n  <!-- Two connected basins sharing global min f* -->\n  <path d=\"M 35 30 Q 75 110 115 110 T 195 30\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2\"/>\n  <!-- Flat bottom line f* -->\n  <line x1=\"30\" y1=\"110\" x2=\"210\" y2=\"110\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"3,3\"/>\n  <text x=\"215\" y=\"113\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\">f*</text>\n  <!-- Point x on slope -->\n  <circle cx=\"60\" cy=\"65\" r=\"3.5\" fill=\"#000000\"/>\n  <text x=\"50\" y=\"62\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\">x</text>\n  <!-- Gradient vector arrow -->\n  <line x1=\"60\" y1=\"65\" x2=\"40\" y2=\"35\" stroke=\"#000000\" stroke-width=\"1.8\" marker-end=\"url(#arr-305)\"/>\n  <text x=\"32\" y=\"30\" fill=\"#000000\" font-size=\"8.5\" font-family=\"serif\" font-style=\"italic\">\u2207f(x)</text>\n  <text x=\"120\" y=\"22\" fill=\"#000000\" font-size=\"9\" font-family=\"sans-serif\" font-weight=\"bold\" text-anchor=\"middle\">\u00bd ||\u2207f(x)||\u00b2 \u2265 \u03bc (f(x) - f*)</text>\n  <text x=\"120\" y=\"132\" fill=\"#000000\" font-size=\"8.5\" font-family=\"sans-serif\" text-anchor=\"middle\">Every stationary point is global min; no strict convexity needed</text>\n</svg>",
    "drawingCaption": "PL Inequality: Gradient magnitude ||\u2207f(x)||\u00b2 dominates suboptimality gap, guaranteeing linear convergence",
    "coreTranslation": [
      "<strong>Theorem:</strong> Every $\\mu$-strongly convex function satisfies the <strong>Polyak-\u0141ojasiewicz (PL) inequality</strong>: $\\frac{1}{2}\\|\\nabla f(x)\\|^2 \\ge \\mu (f(x) - f^*)$.",
      "<strong>Proof:</strong> Minimize the quadratic underestimator $f(y) \\ge f(x) + \\nabla f(x)^T(y-x) + \\frac{\\mu}{2}\\|y-x\\|^2$ with respect to $y$. The minimum of the RHS is attained at $y = x - \\frac{1}{\\mu}\\nabla f(x)$, giving value $f(x) - \\frac{1}{2\\mu}\\|\\nabla f(x)\\|^2$. Since $f(y) \\ge f^*$, rearranging yields the result.",
      "The PL inequality is the exact mathematical engine that enables <strong>linear convergence</strong> of gradient descent without needing strong convexity of non-critical coordinates."
    ],
    "math": "$$\\|\\nabla f(x)\\|^2 \\ge 2\\mu (f(x) - f^*) \\quad \\forall \\, x$$",
    "personalConnection": "A compass needle on a steep cone: the moment you are away from the bottom ($f(x) > f^*$), the tilt force $\\|\\nabla f(x)\\|$ is guaranteed to be strong, pulling you back toward the minimum.",
    "examTrap": "Functions can satisfy the PL inequality WITHOUT being convex! Overparameterized neural networks often satisfy PL locally, allowing gradient descent to find global minima despite non-convexity."
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
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\">\n  <!-- Quasiconvex Outer Box -->\n  <rect x=\"20\" y=\"18\" width=\"200\" height=\"110\" rx=\"8\" fill=\"#f8fafc\" stroke=\"#000000\" stroke-width=\"1.5\"/>\n  <text x=\"30\" y=\"34\" fill=\"#000000\" font-size=\"9\" font-family=\"sans-serif\" font-weight=\"bold\">Quasiconvex (Sublevel sets convex)</text>\n  <!-- Convex Box -->\n  <rect x=\"35\" y=\"42\" width=\"170\" height=\"78\" rx=\"7\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.5\"/>\n  <text x=\"45\" y=\"58\" fill=\"#000000\" font-size=\"9\" font-family=\"sans-serif\" font-weight=\"bold\">Convex (Secant above graph)</text>\n  <!-- Strictly Convex Box -->\n  <rect x=\"50\" y=\"66\" width=\"140\" height=\"48\" rx=\"6\" fill=\"#e2e8f0\" stroke=\"#000000\" stroke-width=\"1.5\"/>\n  <text x=\"60\" y=\"80\" fill=\"#000000\" font-size=\"8.5\" font-family=\"sans-serif\" font-weight=\"bold\">Strictly Convex (Unique min)</text>\n  <!-- Strongly Convex Inner Box -->\n  <rect x=\"65\" y=\"86\" width=\"110\" height=\"24\" rx=\"4\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.8\"/>\n  <text x=\"120\" y=\"102\" fill=\"#000000\" font-size=\"9\" font-family=\"sans-serif\" font-weight=\"bold\" text-anchor=\"middle\">Strongly Convex (m &gt; 0)</text>\n</svg>",
    "drawingCaption": "Hierarchy: Strongly Convex \u2282 Strictly Convex \u2282 Convex. Understanding classic counterexamples prevents exam traps",
    "coreTranslation": [
      "<strong>Convexity Hierarchy:</strong> $\\mu\\text{-Strongly Convex} \\subsetneq \\text{Strictly Convex} \\subsetneq \\text{Convex}$.",
      "<strong>Counterexample 1 ($x^4$):</strong> $f(x) = x^4$ is strictly convex on $\\mathbb{R}$, but $f''(0) = 0$. Hence it is NOT strongly convex.",
      "<strong>Counterexample 2 ($e^x$):</strong> $f(x) = e^x$ is strictly convex on $\\mathbb{R}$ with $f''(x) = e^x > 0$, but $\\lim_{x \\to -\\infty} f''(x) = 0$. Hence it is NOT strongly convex on $\\mathbb{R}$."
    ],
    "math": "$$\\mu\\text{-Strongly Convex } (\\nabla^2 f \\succeq \\mu I) \\implies \\text{Strictly Convex} \\implies \\text{Convex } (\\nabla^2 f \\succeq 0)$$",
    "personalConnection": "Convex = flat surfaces allowed (e.g. ramps). Strictly convex = no flat line segments, but can flatten infinitesimally ($x^4$). Strongly convex = strictly curved everywhere like a bowling ball.",
    "examTrap": "An exam question asking 'Is $f(x) = e^{-x} + x^2$ strongly convex on $\\mathbb{R}$?' Answer: YES! $f''(x) = e^{-x} + 2 \\ge 2 > 0$ for all $x$, so $\\mu = 2$."
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
    "drawingCaption": "Luenberger Fig. 8.1: Unimodal 1D objective \u03d5(\u03b1) = f(x_k + \u03b1 d_k) along search ray d_k",
    "coreTranslation": [
      "The general line search algorithm updates: $x_{k+1} = x_k + \\alpha_k d_k$, where $d_k$ is the search direction and $\\alpha_k > 0$ is the step length.",
      "<strong>Descent Direction Condition:</strong> $d_k$ is a descent direction if the directional derivative is strictly negative: $\\nabla f(x_k)^T d_k < 0$.",
      "This guarantees that for all sufficiently small step sizes $\\alpha > 0$, the objective strictly decreases: $f(x_k + \\alpha d_k) < f(x_k)$."
    ],
    "math": "$$x_{k+1} = x_k + \\alpha_k d_k \\quad \\text{with} \\quad \\nabla f(x_k)^T d_k < 0$$",
    "personalConnection": "Downhill skiing: $d_k$ is the heading angle of your skis pointing downward with the fall line ($\nabla f^T d < 0$), and $\\alpha_k$ is how far you glide before re-evaluating the slope.",
    "examTrap": "If $\\nabla f(x_k)^T d_k = 0$, $d_k$ is orthogonal to the gradient, meaning $f$ stays flat to 1st order. If $\\nabla f(x_k)^T d_k > 0$, taking any step $\\alpha > 0$ climbs uphill!"
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
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\">\n  <defs>\n    <marker id=\"arr-402\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\">\n      <path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/>\n    </marker>\n  </defs>\n  <!-- Axes -->\n  <line x1=\"25\" y1=\"120\" x2=\"225\" y2=\"120\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-402)\"/>\n  <line x1=\"35\" y1=\"130\" x2=\"35\" y2=\"15\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-402)\"/>\n  <text x=\"225\" y=\"132\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\">\u03b1</text>\n  <text x=\"22\" y=\"20\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\">\u03c6(\u03b1)</text>\n  <!-- 1D Quadratic parabola -->\n  <path d=\"M 45 40 Q 120 125 195 40\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2\"/>\n  <!-- Tangent line at alpha=0 -->\n  <line x1=\"35\" y1=\"50\" x2=\"95\" y2=\"105\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"3,3\"/>\n  <circle cx=\"45\" cy=\"59\" r=\"3\" fill=\"#000000\"/>\n  <text x=\"52\" y=\"52\" fill=\"#000000\" font-size=\"8.5\" font-family=\"serif\" font-style=\"italic\">\u03b1 = 0</text>\n  <!-- Min point alpha* -->\n  <circle cx=\"120\" cy=\"100\" r=\"3.5\" fill=\"#000000\"/>\n  <line x1=\"120\" y1=\"100\" x2=\"120\" y2=\"120\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"2,2\"/>\n  <text x=\"120\" y=\"133\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" text-anchor=\"middle\">\u03b1* = -g\u1d40d / (d\u1d40Qd)</text>\n  <text x=\"120\" y=\"24\" fill=\"#000000\" font-size=\"9\" font-family=\"sans-serif\" font-weight=\"bold\" text-anchor=\"middle\">Exact 1D Minimizer for Quadratics</text>\n</svg>",
    "drawingCaption": "Exact Line Search on Quadratic: Optimal step length \u03b1* obtained analytically by setting derivative to zero",
    "coreTranslation": [
      "For a quadratic objective $f(x) = \\frac{1}{2} x^T Q x - b^T x$, the 1D slice along $d_k$ is $\\phi(\\alpha) = f(x_k + \\alpha d_k)$.",
      "Setting derivative $\\phi'(\\alpha) = \\nabla f(x_k + \\alpha d_k)^T d_k = (g_k + \\alpha Q d_k)^T d_k = 0$ yields the exact closed-form step size: $\\alpha_k = -\\frac{g_k^T d_k}{d_k^T Q d_k}$.",
      "<strong>Orthogonality Property:</strong> Under exact line search, the next gradient is strictly orthogonal to the search direction: $\\nabla f(x_{k+1})^T d_k = 0$."
    ],
    "math": "$$\\alpha_k^* = -\\frac{\\nabla f(x_k)^T d_k}{d_k^T Q d_k}, \\quad \\nabla f(x_{k+1})^T d_k = 0$$",
    "personalConnection": "Throwing a bowling ball down a parabolic chute: the ball glides until it reaches the exact deepest point of that straight track before turning around.",
    "examTrap": "In steepest descent on quadratics ($d_k = -g_k$), successive gradients are orthogonal: $g_{k+1}^T g_k = 0$. This orthogonality forces a rigid 90-degree zig-zag trajectory that slows convergence."
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
    "drawingCaption": "Luenberger Fig. 8.8: Armijo rule accepts step sizes where curve f(x_k + \u03b1 d_k) lies below the linear bound line",
    "coreTranslation": [
      "Exact line search is too expensive for general nonlinear functions. The <strong>Armijo Condition</strong> requires a sufficient decrease proportional to step length:",
      "$f(x_k + \\alpha d_k) \\le f(x_k) + c_1 \\alpha \\nabla f(x_k)^T d_k$ with constant $c_1 \\in (0, 1)$ (typically $c_1 = 10^{-4}$).",
      "Geometrically, it specifies a linear upper bound ray with slope $c_1 \\nabla f(x_k)^T d_k$. The step $\\alpha$ is accepted only if $f$ lies below this line, preventing overly large steps."
    ],
    "math": "$$f(x_k + \\alpha d_k) \\le f(x_k) + c_1 \\alpha \\nabla f(x_k)^T d_k, \\quad c_1 \\in (0, 1)$$",
    "personalConnection": "Negotiating a wage bonus: you refuse to accept a long contract unless it guarantees at least a fraction $c_1$ of your initial asking price.",
    "examTrap": "The Armijo condition ALONE is not enough! It accepts arbitrarily small steps $\\alpha \\to 0$. If an algorithm takes $\\alpha_k = 1/2^k$, Armijo holds trivially, yet the algorithm stalls without reaching a minimum!"
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
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\">\n  <defs>\n    <marker id=\"arr-404\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\">\n      <path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/>\n    </marker>\n  </defs>\n  <!-- Axes -->\n  <line x1=\"25\" y1=\"120\" x2=\"225\" y2=\"120\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-404)\"/>\n  <line x1=\"35\" y1=\"130\" x2=\"35\" y2=\"15\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-404)\"/>\n  <!-- 1D function curve phi(alpha) -->\n  <path d=\"M 35 45 Q 85 110 140 105 T 215 35\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2\"/>\n  <!-- Armijo line c1 -->\n  <line x1=\"35\" y1=\"45\" x2=\"210\" y2=\"95\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"4,3\"/>\n  <text x=\"190\" y=\"85\" fill=\"#000000\" font-size=\"8\" font-family=\"sans-serif\">Armijo Line (c\u2081)</text>\n  <!-- Curvature condition point -->\n  <circle cx=\"120\" cy=\"107\" r=\"3.5\" fill=\"#000000\"/>\n  <!-- Acceptable interval on axis -->\n  <line x1=\"105\" y1=\"120\" x2=\"165\" y2=\"120\" stroke=\"#000000\" stroke-width=\"3\"/>\n  <line x1=\"105\" y1=\"116\" x2=\"105\" y2=\"124\" stroke=\"#000000\" stroke-width=\"1.5\"/>\n  <line x1=\"165\" y1=\"116\" x2=\"165\" y2=\"124\" stroke=\"#000000\" stroke-width=\"1.5\"/>\n  <text x=\"135\" y=\"133\" fill=\"#000000\" font-size=\"8.5\" font-family=\"sans-serif\" font-weight=\"bold\" text-anchor=\"middle\">Wolfe Interval</text>\n  <text x=\"120\" y=\"24\" fill=\"#000000\" font-size=\"9\" font-family=\"sans-serif\" font-weight=\"bold\" text-anchor=\"middle\">Armijo (c\u2081) + Curvature (c\u2082) = Wolfe</text>\n</svg>",
    "drawingCaption": "Wolfe Interval: Armijo eliminates oversized steps; Curvature condition eliminates unproductively tiny steps",
    "coreTranslation": [
      "To prevent step sizes from becoming unproductively tiny, the <strong>Curvature Condition</strong> requires: $\\nabla f(x_k + \\alpha d_k)^T d_k \\ge c_2 \\nabla f(x_k)^T d_k$ with $c_2 \\in (c_1, 1)$ (typically $c_2 = 0.9$).",
      "This forces the slope at the new point to become significantly less steep, meaning substantial progress down the valley has been achieved.",
      "<strong>Strong Wolfe Conditions:</strong> Replaces curvature with absolute value $|\\nabla f(x_k + \\alpha d_k)^T d_k| \\le c_2 |\\nabla f(x_k)^T d_k|$, forcing the new point to be near a stationary point of $\\phi$."
    ],
    "math": "$$|\\nabla f(x_k + \\alpha_k d_k)^T d_k| \\le c_2 |\\nabla f(x_k)^T d_k|, \\quad 0 < c_1 < c_2 < 1$$",
    "personalConnection": "Braking a descending bicycle: Armijo ensures you don't overshoot off the cliff; the curvature condition ensures you don't ride the brakes so hard you freeze in place at the top of the hill.",
    "examTrap": "Constants MUST satisfy $0 < c_1 < c_2 < 1$. If $c_1 \\ge c_2$, the acceptable step size interval can become completely empty, causing line search algorithms to crash!"
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
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\">\n  <defs>\n    <marker id=\"arr-405\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"6\" markerHeight=\"6\" orient=\"auto-start-reverse\">\n      <path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/>\n    </marker>\n  </defs>\n  <!-- Vertex x_k -->\n  <circle cx=\"50\" cy=\"95\" r=\"4\" fill=\"#000000\"/>\n  <text x=\"40\" y=\"102\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\">x_k</text>\n  <!-- Negative gradient vector -\u2207f -->\n  <line x1=\"50\" y1=\"95\" x2=\"190\" y2=\"95\" stroke=\"#000000\" stroke-width=\"2\" marker-end=\"url(#arr-405)\"/>\n  <text x=\"195\" y=\"99\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" font-weight=\"bold\">-\u2207f(x_k)</text>\n  <!-- Search direction vector d_k -->\n  <line x1=\"50\" y1=\"95\" x2=\"175\" y2=\"35\" stroke=\"#000000\" stroke-width=\"2\" marker-end=\"url(#arr-405)\"/>\n  <text x=\"180\" y=\"35\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" font-weight=\"bold\">d_k</text>\n  <!-- Angle theta_k arc -->\n  <path d=\"M 90 95 A 40 40 0 0 0 84 79\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.2\"/>\n  <text x=\"96\" y=\"85\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\">\u03b8_k</text>\n  <text x=\"120\" y=\"20\" fill=\"#000000\" font-size=\"9\" font-family=\"sans-serif\" font-weight=\"bold\" text-anchor=\"middle\">Zoutendijk Condition</text>\n  <text x=\"120\" y=\"132\" fill=\"#000000\" font-size=\"9\" font-family=\"monospace\" text-anchor=\"middle\">\u03a3 cos\u00b2 \u03b8_k ||\u2207f(x_k)||\u00b2 &lt; \u221e</text>\n</svg>",
    "drawingCaption": "Zoutendijk Angle: Angle \u03b8_k between search direction d_k and steepest descent direction -\u2207f(x_k)",
    "coreTranslation": [
      "<strong>Theorem (Zoutendijk):</strong> Consider any line search iteration with descent directions $d_k$ and step sizes $\\alpha_k$ satisfying Wolfe conditions. If $f$ is bounded below and $\\nabla f$ is $L$-Lipschitz, then:",
      "$$\\sum_{k=0}^\\infty \\cos^2 \\theta_k \\|\\nabla f(x_k)\\|^2 < \\infty, \\quad \\text{where } \\cos \\theta_k = -\\frac{\\nabla f(x_k)^T d_k}{\\|\\nabla f(x_k)\\| \\|d_k\\|}$$",
      "<strong>Global Convergence ($\\nabla f(x_k) \\to 0$):</strong> If the search directions remain bounded away from orthogonality ($\\cos \\theta_k \\ge \\delta > 0$ for all $k$), then $\\lim_{k \\to \\infty} \\|\\nabla f(x_k)\\| = 0$."
    ],
    "math": "$$\\sum_{k=0}^\\infty \\cos^2 \\theta_k \\|\\nabla f(x_k)\\|^2 < \\infty \\implies \\lim_{k \\to \\infty} \\|\\nabla f(x_k)\\| = 0 \\quad (\\text{if } \\cos \\theta_k \\ge \\delta > 0)$$",
    "personalConnection": "Rowing a boat across cross-currents: as long as your boat is not oriented completely sideways to the current ($\\theta_k \\ne 90^\\circ$), your strokes are guaranteed to transport you to the opposite shore.",
    "examTrap": "If $\\cos \\theta_k \\to 0$ (directions become orthogonal to gradient), Zoutendijk's sum can converge with $\\|\\nabla f(x_k)\\| \\ge \\epsilon > 0$, causing the algorithm to fail!"
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
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\">\n  <defs>\n    <marker id=\"arr-406\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\">\n      <path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/>\n    </marker>\n  </defs>\n  <!-- Axis of alpha -->\n  <line x1=\"25\" y1=\"95\" x2=\"225\" y2=\"95\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-406)\"/>\n  <text x=\"225\" y=\"108\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\">\u03b1</text>\n  <!-- alpha = 1 point (rejected) -->\n  <circle cx=\"195\" cy=\"95\" r=\"3.5\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.8\"/>\n  <line x1=\"191\" y1=\"91\" x2=\"199\" y2=\"99\" stroke=\"#000000\" stroke-width=\"1.5\"/>\n  <line x1=\"191\" y1=\"99\" x2=\"199\" y2=\"91\" stroke=\"#000000\" stroke-width=\"1.5\"/>\n  <text x=\"195\" y=\"80\" fill=\"#000000\" font-size=\"8.5\" font-family=\"sans-serif\" text-anchor=\"middle\">\u03b1\u2080 = 1 (Fails)</text>\n  <!-- alpha = rho (rejected) -->\n  <circle cx=\"135\" cy=\"95\" r=\"3.5\" fill=\"#ffffff\" stroke=\"#000000\" stroke-width=\"1.8\"/>\n  <line x1=\"131\" y1=\"91\" x2=\"139\" y2=\"99\" stroke=\"#000000\" stroke-width=\"1.5\"/>\n  <line x1=\"131\" y1=\"99\" x2=\"139\" y2=\"91\" stroke=\"#000000\" stroke-width=\"1.5\"/>\n  <text x=\"135\" y=\"80\" fill=\"#000000\" font-size=\"8.5\" font-family=\"sans-serif\" text-anchor=\"middle\">\u03b1 = \u03c1 (Fails)</text>\n  <!-- alpha = rho^2 (accepted) -->\n  <circle cx=\"80\" cy=\"95\" r=\"4.5\" fill=\"#000000\"/>\n  <text x=\"80\" y=\"80\" fill=\"#000000\" font-size=\"8.5\" font-family=\"sans-serif\" font-weight=\"bold\" text-anchor=\"middle\">\u03b1 = \u03c1\u00b2 (Accept!)</text>\n  <!-- Backtracking contraction arrows -->\n  <path d=\"M 190 65 Q 165 52 140 65\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-406)\"/>\n  <path d=\"M 130 65 Q 107 52 85 65\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-406)\"/>\n  <text x=\"120\" y=\"24\" fill=\"#000000\" font-size=\"9\" font-family=\"sans-serif\" font-weight=\"bold\" text-anchor=\"middle\">Backtracking: \u03b1 \u2190 \u03c1\u03b1  until Armijo Holds</text>\n  <text x=\"120\" y=\"132\" fill=\"#000000\" font-size=\"8.5\" font-family=\"monospace\" text-anchor=\"middle\">Typical params: \u03c1 \u2208 [0.5, 0.8], c\u2081 = 10\u207b\u2074</text>\n</svg>",
    "drawingCaption": "Backtracking: Start boldly at initial \u03b1 = 1, systematically contracting \u03b1 \u2190 \u03c1 \u03b1 until Armijo condition holds",
    "coreTranslation": [
      "<strong>Algorithm:</strong> Choose $\\alpha_0 = 1$, contraction factor $\\rho \\in (0, 1)$ (e.g. $\\rho = 0.5$), and Armijo constant $c_1 \\in (0, 1)$.",
      "While $f(x_k + \\alpha d_k) > f(x_k) + c_1 \\alpha \\nabla f(x_k)^T d_k$ do: $\\alpha \\leftarrow \\rho \\alpha$. Return $\\alpha_k = \\alpha$.",
      "<strong>Why $\\alpha_0 = 1$ is Essential:</strong> For Newton and Quasi-Newton methods, starting at unit step size $\\alpha_0 = 1$ allows the algorithm to naturally adopt quadratic or superlinear convergence near $x^*$."
    ],
    "math": "$$\\alpha^{(j+1)} = \\rho \\alpha^{(j)}, \\quad \\rho \\in (0, 1), \\quad \\text{until } f(x + \\alpha d) \\le f(x) + c_1 \\alpha \\nabla f(x)^T d$$",
    "personalConnection": "Testing water temperature with your toe: you plan a full forward step, but if the water burns, you immediately step backward halfway, repeating until the temperature is comfortable.",
    "examTrap": "Never start backtracking with $\\alpha_0 < 1$ in Newton's method! Restricting $\\alpha_0 < 1$ permanently degrades Newton's quadratic convergence to slow linear convergence."
  },
  {
    "id": 501,
    "subject": "CMO",
    "topicId": "05_Gradient_Descent_and_Convergence_Analysis",
    "topicTitle": "05 \u00b7 Gradient Descent & Convergence",
    "cardNumber": "01",
    "category": "STEEPEST DESCENT",
    "highlighterClass": "highlight-cyan",
    "title": "Method of Steepest Descent",
    "textbookImg": "assets/luenberger_fig8_9.png",
    "textbookRef": "Luenberger & Ye (4th ed), Sect. 8.2, Fig. 8.9 (p. 243)",
    "drawingCaption": "Luenberger Fig. 8.9: Steepest descent path zig-zags orthogonally across elliptical level contours",
    "coreTranslation": [
      "Steepest descent chooses search direction along the negative gradient: $d_k = -\\nabla f(x_k)$, giving update: $x_{k+1} = x_k - \\alpha_k \\nabla f(x_k)$.",
      "<strong>Directional Optimality:</strong> $-\\nabla f(x_k)$ is the direction that maximizes the instantaneous rate of decrease per unit Euclidean step: $\\arg\\min_{\\|d\\| \\le 1} \\nabla f(x_k)^T d = -\\frac{\\nabla f(x_k)}{\\|\\nabla f(x_k)\\|}$.",
      "Under exact line search, consecutive search directions are perpendicular: $(x_{k+2} - x_{k+1})^T (x_{k+1} - x_k) = 0$, producing a characteristic zig-zag path."
    ],
    "math": "$$x_{k+1} = x_k - \\alpha_k \\nabla f(x_k), \\quad d_k = -\\nabla f(x_k)$$",
    "personalConnection": "Pouring a drop of water on a steep roof: gravity pulls it along the steepest fall line at every millisecond, tracing the orthogonal gradient trajectory.",
    "examTrap": "Steepest descent is only steepest locally in the EUCLIDEAN norm! Changing coordinates or using a Mahalanobis norm changes the gradient direction entirely (which is why Newton's method is superior)."
  },
  {
    "id": 502,
    "subject": "CMO",
    "topicId": "05_Gradient_Descent_and_Convergence_Analysis",
    "topicTitle": "05 \u00b7 Gradient Descent & Convergence",
    "cardNumber": "02",
    "category": "CONVERGENCE ANALYSIS",
    "highlighterClass": "highlight-amber",
    "title": "O(1/k) Convergence on L-Smooth Convex Objectives",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\">\n  <defs>\n    <marker id=\"arr-502\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\">\n      <path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/>\n    </marker>\n  </defs>\n  <!-- Axes -->\n  <line x1=\"25\" y1=\"120\" x2=\"225\" y2=\"120\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-502)\"/>\n  <line x1=\"35\" y1=\"130\" x2=\"35\" y2=\"15\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-502)\"/>\n  <text x=\"225\" y=\"132\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\">k (Iterations)</text>\n  <text x=\"15\" y=\"20\" fill=\"#000000\" font-size=\"8.5\" font-family=\"serif\" font-style=\"italic\">f(x_k) - f*</text>\n  <!-- 1/k decay curve -->\n  <path d=\"M 45 30 Q 75 105 210 115\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2\"/>\n  <!-- Points at k = 1, 2, 5 -->\n  <circle cx=\"55\" cy=\"48\" r=\"3\" fill=\"#000000\"/>\n  <circle cx=\"95\" cy=\"98\" r=\"3\" fill=\"#000000\"/>\n  <circle cx=\"175\" cy=\"113\" r=\"3\" fill=\"#000000\"/>\n  <text x=\"125\" y=\"45\" fill=\"#000000\" font-size=\"9\" font-family=\"monospace\" text-anchor=\"middle\">f(x_k) - f* \u2264 L ||x\u2080 - x*||\u00b2 / (2k)</text>\n  <text x=\"125\" y=\"65\" fill=\"#000000\" font-size=\"8.5\" font-family=\"sans-serif\" text-anchor=\"middle\">Sublinear O(1/k) with Step \u03b1 = 1/L</text>\n</svg>",
    "drawingCaption": "Sublinear Convergence: Suboptimality gap decays as O(1/k) for convex objectives with L-Lipschitz gradients",
    "coreTranslation": [
      "A function is <strong>$L$-Smooth</strong> if $\\|\\nabla f(x) - \\nabla f(y)\\| \\le L \\|x - y\\|$, which implies the Descent Lemma: $f(y) \\le f(x) + \\nabla f(x)^T(y-x) + \\frac{L}{2}\\|y-x\\|^2$.",
      "Taking step size $\\alpha = 1/L$: $f(x_{k+1}) \\le f(x_k) - \\frac{1}{2L}\\|\\nabla f(x_k)\\|^2$, guaranteeing strict monotonic decrease.",
      "<strong>Theorem:</strong> For any convex $L$-smooth function with constant step $\\alpha = 1/L$, the suboptimality error decays as: $f(x_k) - f^* \\le \\frac{L \\|x_0 - x^*\\|^2}{2k}$."
    ],
    "math": "$$f(x_k) - f^* \\le \\frac{L \\|x_0 - x^*\\|^2}{2k} = \\mathcal{O}\\left(\\frac{1}{k}\\right)$$",
    "personalConnection": "Filling an empty jar with sand: the first few scoops make massive progress, but getting the final grains in to reach exact capacity requires progressively more scoops.",
    "examTrap": "If the step size $\\alpha \\ge 2/L$, gradient descent can violently DIVERGE! The stability threshold is strictly $\\alpha < 2/L$."
  },
  {
    "id": 503,
    "subject": "CMO",
    "topicId": "05_Gradient_Descent_and_Convergence_Analysis",
    "topicTitle": "05 \u00b7 Gradient Descent & Convergence",
    "cardNumber": "03",
    "category": "LINEAR CONVERGENCE",
    "highlighterClass": "highlight-emerald",
    "title": "Linear Convergence on Strongly Convex Functions",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\">\n  <defs>\n    <marker id=\"arr-503\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"5\" markerHeight=\"5\" orient=\"auto-start-reverse\">\n      <path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/>\n    </marker>\n  </defs>\n  <!-- Axes -->\n  <line x1=\"25\" y1=\"120\" x2=\"225\" y2=\"120\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-503)\"/>\n  <line x1=\"35\" y1=\"130\" x2=\"35\" y2=\"15\" stroke=\"#000000\" stroke-width=\"1.2\" marker-end=\"url(#arr-503)\"/>\n  <text x=\"225\" y=\"132\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\">k</text>\n  <text x=\"10\" y=\"20\" fill=\"#000000\" font-size=\"8\" font-family=\"serif\" font-style=\"italic\">log ||x_k - x*||</text>\n  <!-- Straight linear decay line on semilog scale -->\n  <line x1=\"45\" y1=\"28\" x2=\"210\" y2=\"115\" stroke=\"#000000\" stroke-width=\"2\"/>\n  <!-- Points at successive k -->\n  <circle cx=\"45\" cy=\"28\" r=\"3\" fill=\"#000000\"/>\n  <circle cx=\"95\" cy=\"54\" r=\"3\" fill=\"#000000\"/>\n  <circle cx=\"150\" cy=\"83\" r=\"3\" fill=\"#000000\"/>\n  <circle cx=\"205\" cy=\"112\" r=\"3\" fill=\"#000000\"/>\n  <text x=\"135\" y=\"40\" fill=\"#000000\" font-size=\"9\" font-family=\"monospace\" text-anchor=\"middle\">||x_k - x*|| \u2264 C \u00b7 ((\u03ba - 1) / (\u03ba + 1))^k</text>\n  <text x=\"135\" y=\"133\" fill=\"#000000\" font-size=\"8.5\" font-family=\"sans-serif\" font-weight=\"bold\" text-anchor=\"middle\">Linear (Geometric) Rate: Error Halves Periodically</text>\n</svg>",
    "drawingCaption": "Linear Convergence: Error decays exponentially as a straight line on semilog scale with contraction factor (\u03ba-1)/(\u03ba+1)",
    "coreTranslation": [
      "When $f$ is both $\\mu$-strongly convex and $L$-smooth, the condition number is $\\kappa = L / \\mu \\ge 1$.",
      "<strong>Linear Convergence Rate:</strong> Gradient descent with optimal constant step size $\\alpha = \\frac{2}{L+\\mu}$ contracts the distance to the optimum geometrically: $\\|x_k - x^*\\| \\le \\left(\\frac{\\kappa - 1}{\\kappa + 1}\\right)^k \\|x_0 - x^*\\|$.",
      "In optimization terminology, 'linear convergence' means that the log-error $\\log \\|x_k - x^*\\|$ decreases linearly with iteration count $k$."
    ],
    "math": "$$\\|x_k - x^*\\| \\le \\left(\\frac{\\kappa - 1}{\\kappa + 1}\\right)^k \\|x_0 - x^*\\|, \\quad \\kappa = \\frac{L}{\\mu}$$",
    "personalConnection": "Radioactive decay: every half-life, half of the remaining radioactive atoms decay. In each iteration, error is multiplied by a fixed contraction fraction $\\rho < 1$.",
    "examTrap": "Don't confuse computer science linear time $O(k)$ with optimization 'linear convergence'! Linear convergence in optimization means geometric/exponential decay $O(\\rho^k)$, which is dramatically faster than sublinear $O(1/k)$."
  },
  {
    "id": 504,
    "subject": "CMO",
    "topicId": "05_Gradient_Descent_and_Convergence_Analysis",
    "topicTitle": "05 \u00b7 Gradient Descent & Convergence",
    "cardNumber": "04",
    "category": "KANTOROVICH INEQUALITY",
    "highlighterClass": "highlight-violet",
    "title": "Kantorovich Inequality & Quadratic Bound",
    "textbookImg": "assets/luenberger_fig8_10.png",
    "textbookRef": "Luenberger & Ye (4th ed), Sect. 8.3, Fig. 8.10 (p. 245)",
    "drawingCaption": "Luenberger Fig. 8.10: The convex curve 1/\u03bb and the secant line establishing the Kantorovich ratio bound",
    "coreTranslation": [
      "For a positive definite matrix $Q$ with eigenvalues $A = \\lambda_{\\max} \\ge \\dots \\ge a = \\lambda_{\\min} > 0$, the <strong>Kantorovich Inequality</strong> states: $\\frac{(x^T x)^2}{(x^T Q x)(x^T Q^{-1} x)} \\ge \\frac{4 A a}{(A + a)^2}$.",
      "Applying this to steepest descent on quadratic objective $E(x) = \\frac{1}{2}(x-x^*)^T Q (x-x^*)$ gives the exact error reduction factor per iteration:",
      "$$E(x_{k+1}) \\le \\left(\\frac{A - a}{A + a}\\right)^2 E(x_k) = \\left(\\frac{\\kappa - 1}{\\kappa + 1}\\right)^2 E(x_k)$$"
    ],
    "math": "$$\\frac{(x^T x)^2}{(x^T Q x)(x^T Q^{-1} x)} \\ge \\frac{4 A a}{(A + a)^2} \\implies E(x_{k+1}) \\le \\left(\\frac{\\kappa - 1}{\\kappa + 1}\\right)^2 E(x_k)$$",
    "personalConnection": "The worst-case scenario theorem: Kantorovich bounds the worst possible misalignment between the steepest descent gradient vector and the true axis of the elliptical bowl.",
    "examTrap": "The rate bound is TIGHT! For starting points aligned at 45 degrees to the principal eigenvectors, steepest descent achieves the exact upper bound $\\left(\\frac{\\kappa-1}{\\kappa+1}\\right)^2$ at every single iteration."
  },
  {
    "id": 505,
    "subject": "CMO",
    "topicId": "05_Gradient_Descent_and_Convergence_Analysis",
    "topicTitle": "05 \u00b7 Gradient Descent & Convergence",
    "cardNumber": "05",
    "category": "CONDITION NUMBER DYNAMICS",
    "highlighterClass": "highlight-indigo",
    "title": "Condition Number \u03ba & The Zig-Zag Phenomenon",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\">\n  <!-- Elongated Ellipses -->\n  <ellipse cx=\"120\" cy=\"72\" rx=\"95\" ry=\"24\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.2\"/>\n  <ellipse cx=\"120\" cy=\"72\" rx=\"60\" ry=\"14\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.2\"/>\n  <ellipse cx=\"120\" cy=\"72\" rx=\"25\" ry=\"6\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.2\"/>\n  <!-- 90-degree zig-zag steepest descent trajectory -->\n  <polyline points=\"40,88 80,58 92,84 108,62 115,78 120,72\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2\"/>\n  <!-- Successive steps -->\n  <circle cx=\"40\" cy=\"88\" r=\"3\" fill=\"#000000\"/>\n  <circle cx=\"80\" cy=\"58\" r=\"2.5\" fill=\"#000000\"/>\n  <circle cx=\"92\" cy=\"84\" r=\"2.5\" fill=\"#000000\"/>\n  <circle cx=\"120\" cy=\"72\" r=\"3.5\" fill=\"#000000\"/>\n  <text x=\"120\" y=\"24\" fill=\"#000000\" font-size=\"9\" font-family=\"sans-serif\" font-weight=\"bold\" text-anchor=\"middle\">Ill-Conditioned Valley: \u03ba = \u03bb_max / \u03bb_min \u226b 1</text>\n  <text x=\"120\" y=\"132\" fill=\"#000000\" font-size=\"8.5\" font-family=\"sans-serif\" text-anchor=\"middle\">Severe 90\u00b0 Orthogonal Zig-Zag Trajectory</text>\n</svg>",
    "drawingCaption": "Zig-Zagging: When condition number \u03ba \u226b 1, steepest descent bounces between steep canyon walls rather than gliding along the floor",
    "coreTranslation": [
      "The condition number $\\kappa = \\frac{\\lambda_{\\max}}{\\lambda_{\\min}}$ measures the eccentric elongation of objective level contours.",
      "<strong>If $\\kappa = 1$ (Spherical Contours):</strong> $\\frac{\\kappa-1}{\\kappa+1} = 0$. Steepest descent points directly at the center and converges in exactly <strong>ONE step</strong>!",
      "<strong>If $\\kappa = 1000$ (Elongated Canyon):</strong> $\\frac{\\kappa-1}{\\kappa+1} = \\frac{999}{1001} \\approx 0.998$. The algorithm bounces back and forth across canyon walls, making almost zero forward progress per step."
    ],
    "math": "$$\\kappa = \\frac{\\lambda_{\\max}}{\\lambda_{\\min}}, \\quad \\lim_{\\kappa \\to \\infty} \\frac{\\kappa - 1}{\\kappa + 1} = 1 \\implies \\text{Stagnation}$$",
    "personalConnection": "Walking through a narrow ravine: taking steps perpendicular to the canyon walls sends you slamming into the rock face across from you, rather than walking down the stream.",
    "examTrap": "Preconditioning transforms coordinates ($y = P x$) to make the condition number $\\kappa(P^{-T} Q P^{-1}) \\approx 1$, curing the zig-zag phenomenon without changing the minimum point."
  },
  {
    "id": 506,
    "subject": "CMO",
    "topicId": "05_Gradient_Descent_and_Convergence_Analysis",
    "topicTitle": "05 \u00b7 Gradient Descent & Convergence",
    "cardNumber": "06",
    "category": "ADVANCED STEP SIZES",
    "highlighterClass": "highlight-rose",
    "title": "Barzilai-Borwein & Heavy Ball Momentum",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\">\n  <!-- Elongated Ellipses in background -->\n  <ellipse cx=\"120\" cy=\"72\" rx=\"95\" ry=\"25\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"2,2\"/>\n  <ellipse cx=\"120\" cy=\"72\" rx=\"55\" ry=\"14\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1\" stroke-dasharray=\"2,2\"/>\n  <!-- Standard zig-zag (dashed) -->\n  <polyline points=\"40,90 80,56 92,84 108,62\" fill=\"none\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"3,3\"/>\n  <!-- Momentum smooth path (solid) -->\n  <path d=\"M 40 90 Q 90 68 120 72\" fill=\"none\" stroke=\"#000000\" stroke-width=\"2.2\"/>\n  <circle cx=\"120\" cy=\"72\" r=\"3.5\" fill=\"#000000\"/>\n  <text x=\"120\" y=\"24\" fill=\"#000000\" font-size=\"9\" font-family=\"sans-serif\" font-weight=\"bold\" text-anchor=\"middle\">Heavy Ball Momentum: + \u03b2(x_k - x_{k-1})</text>\n  <text x=\"120\" y=\"115\" fill=\"#000000\" font-size=\"8.5\" font-family=\"sans-serif\" text-anchor=\"middle\">Cuts across zig-zag oscillations straight to minimum</text>\n  <text x=\"120\" y=\"132\" fill=\"#000000\" font-size=\"8\" font-family=\"monospace\" text-anchor=\"middle\">BB Spectral Step: \u03b1_k = (s\u1d40y) / ||y||\u00b2</text>\n</svg>",
    "drawingCaption": "Acceleration: Momentum dampens oscillations along steep directions while accelerating down flat valley floors",
    "coreTranslation": [
      "<strong>Barzilai-Borwein (BB) Method:</strong> Uses secant equation $s_k \\approx \\alpha y_k$ (where $s_k = x_k - x_{k-1}$ and $y_k = g_k - g_{k-1}$) to choose step size without line search: $\\alpha_{k}^{BB1} = \\frac{s_k^T y_k}{y_k^T y_k}$, $\\alpha_{k}^{BB2} = \\frac{s_k^T s_k}{s_k^T y_k}$.",
      "BB step sizes produce non-monotonic objective decrease, but achieve dramatically faster convergence on ill-conditioned problems.",
      "<strong>Polyak's Heavy Ball:</strong> Adds momentum: $x_{k+1} = x_k - \\alpha \\nabla f(x_k) + \\beta (x_k - x_{k-1})$. Improves convergence rate from $\\frac{\\kappa-1}{\\kappa+1}$ to $\\frac{\\sqrt{\\kappa}-1}{\\sqrt{\\kappa}+1}$!"
    ],
    "math": "$$x_{k+1} = x_k - \\alpha \\nabla f(x_k) + \\beta(x_k - x_{k-1}), \\quad \\text{Rate: } \\frac{\\sqrt{\\kappa}-1}{\\sqrt{\\kappa}+1}$$",
    "personalConnection": "Rolling a heavy bowling ball down a washboard road: its inertia prevents it from bouncing erratically into every side ditch, rolling smoothly through the center.",
    "examTrap": "Heavy Ball momentum does NOT guarantee convergence on general non-convex functions (it can overshoot and oscillate). Nesterov accelerated gradient (NAG) fixes this by computing gradient at the look-ahead point."
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
    "textbookImg": "assets/luenberger_fig11_1.png",
    "textbookRef": "Luenberger & Ye (4th ed), Sect. 11.1, Fig. 11.1 (p. 322)",
    "drawingCaption": "Luenberger Fig. 11.1: Inactive g\u2082 and g\u2083 are far from x* with zero local effect",
    "coreTranslation": [
      "The <strong>Feasible Set $\\Omega$</strong> is your legal playground where $h_i(x)=0$ and $g_j(x)\\le 0$ hold simultaneously.",
      "The <strong>Active Set $\\mathcal{A}(x) = \\{j : g_j(x)=0\\}$</strong> identifies boundary walls you are physically pressing against right now.",
      "<strong>Inactive constraints ($g_j(x) < 0$):</strong> In Luenberger's Fig. 11.1, candidate $x^*$ touches $g_1(x)=0$, while $g_2(x)=0$ and $g_3(x)=0$ are far away! In a local ball around $x^*$, they remain strictly $< 0$ and have zero local influence."
    ],
    "math": "$$\\Omega = \\{x : h_i(x)=0, \\, g_j(x) \\le 0\\}, \\quad \\mathcal{A}(x) = \\{j : g_j(x) = 0\\}$$",
    "personalConnection": "Standing in the corner of an elevator: only the two walls your shoulders are touching restrict immediate steps. The elevator door across the room has plenty of distance and plays zero local role.",
    "examTrap": "Never include inactive constraints in local gradient calculations! $g_j(x^*) < 0$ implies $\\mu_j^* = 0$ by complementary slackness. Carrying inactive constraints into gradient equations produces false stationary points."
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
    "textbookImg": "assets/luenberger_fig11_2a.png",
    "textbookRef": "Luenberger & Ye (4th ed), Sect. 11.2, Fig. 11.2a (p. 324)",
    "drawingCaption": "Luenberger Fig. 11.2a: Tangent plane M to surface S at x* with normal \u2207h(x*)\u1d40",
    "coreTranslation": [
      "<strong>Luenberger's Curve Definition (p. 323):</strong> A curve on surface $S$ is parameterized as $x(t) \\in S$. The derivative at $x^*$ is velocity $\\dot{x}(t^*)$. The tangent plane is the collection of all such derivatives!",
      "Discrete sequence definition: $d = \\lim_{k\\to\\infty} \\frac{x_k - x}{t_k}$ with $x_k \\in \\Omega$ and $t_k \\downarrow 0$.",
      "As shown in Fig. 11.2a, tangent plane $M = \\{y : \\nabla h(x^*)^T y = 0\\}$ is strictly orthogonal to normal gradient $\\nabla h(x^*)^T$."
    ],
    "math": "$$\\dot{x}(t^*) = \\lim_{t \\to t^*} \\frac{x(t) - x^*}{t - t^*}, \\quad M = \\{y : \\nabla h(x^*)^T y = 0\\}$$",
    "personalConnection": "An airplane touching down on a runway: $d$ is its exact velocity vector at touchdown. The crucial requirement is that the entire approach path $x_k$ remained strictly within legal airspace $\\Omega$.",
    "examTrap": "Scalars $t_k$ MUST strictly approach 0 from the positive side ($t_k > 0$). Negative steps reverse direction and can launch you outside $\\Omega$."
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
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\">\n  <defs>\n    <marker id=\"arr-903\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"6\" markerHeight=\"6\" orient=\"auto-start-reverse\">\n      <path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/>\n    </marker>\n  </defs>\n  <!-- Cone Shaded Fan -->\n  <polygon points=\"50,110 205,35 205,125\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.8\"/>\n  <!-- Direction ray d -->\n  <line x1=\"50\" y1=\"110\" x2=\"175\" y2=\"75\" stroke=\"#000000\" stroke-width=\"2\" marker-end=\"url(#arr-903)\"/>\n  <text x=\"180\" y=\"78\" fill=\"#000000\" font-size=\"9.5\" font-family=\"serif\" font-style=\"italic\" font-weight=\"bold\">\u03b1 d</text>\n  <!-- Base point x* -->\n  <circle cx=\"50\" cy=\"110\" r=\"4\" fill=\"#000000\"/>\n  <text x=\"40\" y=\"125\" fill=\"#000000\" font-size=\"10\" font-family=\"serif\" font-style=\"italic\" font-weight=\"bold\">x*</text>\n  <!-- Cone label -->\n  <text x=\"135\" y=\"55\" fill=\"#000000\" font-size=\"11\" font-family=\"serif\" font-style=\"italic\" font-weight=\"bold\">T_\u03a9(x*)</text>\n  <text x=\"120\" y=\"138\" fill=\"#000000\" font-size=\"8.5\" font-family=\"sans-serif\" text-anchor=\"middle\">Fan of all admissible departure rays: d \u2208 T_\u03a9 \u21d2 \u03b1d \u2208 T_\u03a9 (\u03b1 \u2265 0)</text>\n</svg>",
    "drawingCaption": "Tangent Cone: Pointed apex at x*, expanding outward to encompass all feasible limiting vectors",
    "coreTranslation": [
      "The <strong>Tangent Cone $T_\\Omega(x)$</strong> is the set of all tangent vectors to $\\Omega$ at point $x$.",
      "<strong>Cone Property:</strong> If $d \\in T_\\Omega(x)$, then $\\lambda d \\in T_\\Omega(x)$ for all $\\lambda \\ge 0$. You can stretch the arrow as long as you want.",
      "It is <strong>always a closed set</strong>, even if the underlying feasible set $\\Omega$ is non-convex or has sharp jagged edges."
    ],
    "math": "$$T_\\Omega(x) = \\left\\{ d \\in \\mathbb{R}^n : \\exists x_k \\in \\Omega, t_k \\downarrow 0 \\text{ s.t. } \\lim_{k\\to\\infty} \\frac{x_k - x}{t_k} = d \\right\\}$$",
    "personalConnection": "Shining a flashlight from the sharp corner of a room into the interior: the conical cone of light illuminating the floor is $T_\\Omega(x^*)$.",
    "examTrap": "Tangent cones are NOT always convex! If $\\Omega$ is a non-convex set (e.g., union of two crossing lines), $T_\\Omega(x)$ is a union of lines, which fails convexity."
  },
  {
    "id": 904,
    "subject": "CMO",
    "topicId": "09_Geometry_of_Constrained_Optimization_Tangent_Cone_and_LICQ",
    "topicTitle": "09 \u00b7 Tangent Cones & LICQ Geometry",
    "cardNumber": "04",
    "category": "WORKED STEP-BY-STEP",
    "highlighterClass": "highlight-rose",
    "title": "Computing T_\u03a9(0,0) for x\u2081, x\u2082 \u2265 0",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\">\n  <defs>\n    <marker id=\"arr-904\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"6\" markerHeight=\"6\" orient=\"auto-start-reverse\">\n      <path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/>\n    </marker>\n  </defs>\n  <!-- Axes -->\n  <line x1=\"35\" y1=\"115\" x2=\"215\" y2=\"115\" stroke=\"#000000\" stroke-width=\"1.5\" marker-end=\"url(#arr-904)\"/>\n  <line x1=\"55\" y1=\"130\" x2=\"55\" y2=\"20\" stroke=\"#000000\" stroke-width=\"1.5\" marker-end=\"url(#arr-904)\"/>\n  <text x=\"215\" y=\"128\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\">x\u2081</text>\n  <text x=\"42\" y=\"25\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\">x\u2082</text>\n  <!-- Shaded First Quadrant -->\n  <rect x=\"55\" y=\"25\" width=\"145\" height=\"90\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"4,3\"/>\n  <!-- Origin -->\n  <circle cx=\"55\" cy=\"115\" r=\"4\" fill=\"#000000\"/>\n  <text x=\"40\" y=\"128\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\">(0,0)</text>\n  <text x=\"125\" y=\"65\" fill=\"#000000\" font-size=\"10\" font-family=\"serif\" font-style=\"italic\" font-weight=\"bold\">T_\u03a9(0,0) = \u211d\u00b2\u208a</text>\n  <text x=\"125\" y=\"82\" fill=\"#000000\" font-size=\"8.5\" font-family=\"monospace\">[0, \u221e) \u00d7 [0, \u221e)</text>\n</svg>",
    "drawingCaption": "Worked Calculation: Positive orthant feasible set \u03a9 generates identical tangent cone T_\u03a9 = R\u00b2\u208a at the origin",
    "coreTranslation": [
      "Let $\\Omega = \\{(x_1, x_2) : x_1 \\ge 0, x_2 \\ge 0\\}$. We compute $T_\\Omega(0,0)$ step by step:",
      "Take any direction $d = (d_1, d_2)$ with $d_1 \\ge 0, d_2 \\ge 0$. Choose test sequence $x_k = t_k d$ with $t_k = 1/k > 0$.",
      "Since $t_k > 0$ and $d_i \\ge 0$, every element $x_k \\in \\Omega$ is strictly feasible. Ratio $\\frac{x_k - 0}{t_k} = d$ identically, so $d \\in T_\\Omega(0,0)$. Thus $T_\\Omega(0,0) = \\mathbb{R}^2_+$. "
    ],
    "math": "$$x_k = \\left( \\frac{d_1}{k}, \\frac{d_2}{k} \\right) \\in \\Omega \\implies \\lim_{k\\to\\infty} \\frac{x_k - 0}{1/k} = (d_1, d_2) \\implies T_\\Omega(0,0) = \\mathbb{R}^2_+$$",
    "personalConnection": "Pushing a toy car resting in the bottom-left corner of a flat tabletop: you can push forward or right, but pulling backward drops off the edge.",
    "examTrap": "For interior points ($x_1 > 0, x_2 > 0$), NO constraints are active! The tangent cone is the ENTIRE space $T_\\Omega(x) = \\mathbb{R}^2$, NOT just the first quadrant."
  },
  {
    "id": 905,
    "subject": "CMO",
    "topicId": "09_Geometry_of_Constrained_Optimization_Tangent_Cone_and_LICQ",
    "topicTitle": "09 \u00b7 Tangent Cones & LICQ Geometry",
    "cardNumber": "05",
    "category": "OPTIMALITY THEOREM",
    "highlighterClass": "highlight-violet",
    "title": "First-Order Optimality: \u2207f(x*)\u1d40d \u2265 0",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\">\n  <defs>\n    <marker id=\"arr-905\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"6\" markerHeight=\"6\" orient=\"auto-start-reverse\">\n      <path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/>\n    </marker>\n  </defs>\n  <!-- Tangent cone fan -->\n  <polygon points=\"110,85 195,35 195,120\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.8\"/>\n  <text x=\"155\" y=\"75\" fill=\"#000000\" font-size=\"10\" font-family=\"serif\" font-style=\"italic\" font-weight=\"bold\">T_\u03a9(x*)</text>\n  <!-- Supporting hyperplane (dashed line) -->\n  <line x1=\"110\" y1=\"25\" x2=\"110\" y2=\"135\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"3,3\"/>\n  <!-- Negative gradient -\u2207f pointing into exterior -->\n  <line x1=\"110\" y1=\"85\" x2=\"45\" y2=\"50\" stroke=\"#000000\" stroke-width=\"2\" marker-end=\"url(#arr-905)\"/>\n  <text x=\"35\" y=\"45\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" font-weight=\"bold\">-\u2207f(x*)</text>\n  <!-- Vertex x* -->\n  <circle cx=\"110\" cy=\"85\" r=\"4\" fill=\"#000000\"/>\n  <text x=\"100\" y=\"100\" fill=\"#000000\" font-size=\"9.5\" font-family=\"serif\" font-style=\"italic\">x*</text>\n  <text x=\"120\" y=\"20\" fill=\"#000000\" font-size=\"9\" font-family=\"sans-serif\" font-weight=\"bold\" text-anchor=\"middle\">Optimality: \u2207f(x*)\u1d40d \u2265 0  (\u2200 d \u2208 T_\u03a9)</text>\n  <text x=\"120\" y=\"138\" fill=\"#000000\" font-size=\"8.5\" font-family=\"sans-serif\" text-anchor=\"middle\">-\u2207f(x*) makes obtuse angle (\u2265 90\u00b0) with all feasible directions</text>\n</svg>",
    "drawingCaption": "Fundamental Theorem: Steepest descent vector -\u2207f points away from the cone of feasible directions T_\u03a9",
    "coreTranslation": [
      "<strong>Fundamental Constrained Theorem:</strong> If $x^*$ is a local minimizer of $f$ over $\\Omega$, then for all $d \\in T_\\Omega(x^*)$: $\\nabla f(x^*)^T d \\ge 0$.",
      "<strong>Intuition:</strong> Directional derivative $f'(x^*; d) \\ge 0$ along every feasible direction. Moving anywhere into the interior of $\\Omega$ only increases $f$.",
      "Equivalently: $-\\nabla f(x^*) \\in (T_\\Omega(x^*))^*$ belongs to the <strong>polar cone</strong>. The steepest descent vector points strictly outside the feasible directions."
    ],
    "math": "$$x^* \\text{ local min of } f \\text{ on } \\Omega \\implies \\nabla f(x^*)^T d \\ge 0 \\quad \\forall \\, d \\in T_\\Omega(x^*)$$",
    "personalConnection": "A marble resting at the bottom of a bowl with a solid barrier wall: gravity pulls downward ($-\\nabla f$), but the barrier blocks entry, forcing the marble to sit motionless.",
    "examTrap": "This condition is necessary, NOT sufficient. It holds at local maxima if the feasible set only permits stepping downhill."
  },
  {
    "id": 906,
    "subject": "CMO",
    "topicId": "09_Geometry_of_Constrained_Optimization_Tangent_Cone_and_LICQ",
    "topicTitle": "09 \u00b7 Tangent Cones & LICQ Geometry",
    "cardNumber": "06",
    "category": "EXAM TRAPS & CQ",
    "highlighterClass": "highlight-amber",
    "title": "Tangent Cone vs Linearized Cone (LICQ)",
    "drawingSvg": "<svg viewBox=\"0 0 240 145\" class=\"w-full h-full\">\n  <defs>\n    <marker id=\"arr-906\" viewBox=\"0 0 10 10\" refX=\"6\" refY=\"5\" markerWidth=\"6\" markerHeight=\"6\" orient=\"auto-start-reverse\">\n      <path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#000000\"/>\n    </marker>\n  </defs>\n  <!-- Linearized Cone L_\u03a9 (wider dashed wedge) -->\n  <polygon points=\"50,115 195,35 195,115\" fill=\"#f1f5f9\" stroke=\"#000000\" stroke-width=\"1.2\" stroke-dasharray=\"4,3\"/>\n  <text x=\"160\" y=\"95\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\">L_\u03a9 (Linearized)</text>\n  <!-- True Tangent Cone T_\u03a9 (single ray or narrow curve) -->\n  <line x1=\"50\" y1=\"115\" x2=\"190\" y2=\"45\" stroke=\"#000000\" stroke-width=\"2.5\" marker-end=\"url(#arr-906)\"/>\n  <text x=\"150\" y=\"42\" fill=\"#000000\" font-size=\"9\" font-family=\"serif\" font-style=\"italic\" font-weight=\"bold\">T_\u03a9 (True Tangents)</text>\n  <!-- Cusp vertex -->\n  <circle cx=\"50\" cy=\"115\" r=\"4\" fill=\"#000000\"/>\n  <text x=\"40\" y=\"128\" fill=\"#000000\" font-size=\"9.5\" font-family=\"serif\" font-style=\"italic\">x*</text>\n  <text x=\"120\" y=\"20\" fill=\"#000000\" font-size=\"9\" font-family=\"sans-serif\" font-weight=\"bold\" text-anchor=\"middle\">LICQ Fails: T_\u03a9(x*) \u2acb L_\u03a9(x*)</text>\n  <text x=\"120\" y=\"135\" fill=\"#000000\" font-size=\"8.5\" font-family=\"sans-serif\" text-anchor=\"middle\">Linearization predicts directions that immediately exit \u03a9</text>\n</svg>",
    "drawingCaption": "Constraint Qualification Failure: Linearized cone L_\u03a9 over-approximates true geometric tangent cone T_\u03a9",
    "coreTranslation": [
      "The <strong>Linearized Cone $L_\\Omega(x)$</strong> is defined by active constraint gradients: $L_\\Omega = \\{d : \\nabla h_i^T d = 0, \\nabla g_j^T d \\le 0\\}$. In general, $T_\\Omega \\subseteq L_\\Omega$.",
      "<strong>Constraint Qualification (CQ):</strong> A condition guaranteeing $T_\\Omega(x^*) = L_\\Omega(x^*)$. The gold standard is <strong>LICQ</strong>: active gradients $\\{\\nabla h_i, \\nabla g_j\\}_{j \\in \\mathcal{A}}$ are linearly independent.",
      "Without CQ, $T_\\Omega \\subsetneq L_\\Omega$. KKT conditions can FAIL completely even at an obvious local minimum!"
    ],
    "math": "$$\\text{LICQ Holds} \\implies T_\\Omega(x^*) = L_\\Omega(x^*) = \\{d : \\nabla h_i^T d = 0, \\, \\nabla g_j^T d \\le 0 \\, (j \\in \\mathcal{A})\\}$$",
    "personalConnection": "Contractor drawing straight tangent lines on blueprints to approximate a sharp curved wall: if the wall has an acute cusp, the blueprint allows steps that smash into brick.",
    "examTrap": "Assuming KKT multipliers always exist! If $T_\\Omega \\ne L_\\Omega$ (CQ fails), a local minimum can exist where KKT multipliers DO NOT exist at all."
  }
];
