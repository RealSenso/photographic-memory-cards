import json

cards = [
    # =========================================================================
    # TOPIC 01: Mathematical Preliminaries, Topology and Weierstrass
    # =========================================================================
    {
        "id": 101,
        "subject": "CMO",
        "topicId": "01_Mathematical_Preliminaries_Topology_and_Weierstrass",
        "topicTitle": "01 · Mathematical Preliminaries & Weierstrass",
        "cardNumber": "01",
        "category": "TOPOLOGY & METRIC SPACES",
        "highlighterClass": "highlight-cyan",
        "title": "Open, Closed & Bounded Sets (Heine-Borel)",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
            <defs>
              <radialGradient id="open-ball" cx="50%" cy="50%" r="50%">
                <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.25"/>
                <stop offset="100%" stop-color="#38bdf8" stop-opacity="0.05"/>
              </radialGradient>
            </defs>
            <!-- Open Ball B_eps(x) -->
            <circle cx="65" cy="70" r="40" fill="url(#open-ball)" stroke="#38bdf8" stroke-dasharray="3,3" stroke-width="1.5"/>
            <circle cx="65" cy="70" r="3" fill="#38bdf8"/>
            <line x1="65" y1="70" x2="95" y2="45" stroke="#38bdf8" stroke-width="1.2"/>
            <text x="75" y="55" fill="#38bdf8" font-size="9" font-family="monospace">ε</text>
            <text x="65" y="85" fill="#94a3b8" font-size="9" font-family="monospace" text-anchor="middle">B_ε(x) Open</text>

            <!-- Closed & Bounded Compact Set -->
            <rect x="135" y="30" width="85" height="80" rx="12" fill="rgba(16,185,129,0.12)" stroke="#10b981" stroke-width="2"/>
            <circle cx="177" cy="70" r="3" fill="#10b981"/>
            <text x="177" y="62" fill="#10b981" font-size="10" font-family="monospace" text-anchor="middle" font-weight="bold">K (Compact)</text>
            <text x="177" y="88" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Closed (Solid line)</text>
            <text x="177" y="99" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">+ Bounded</text>
          </svg>""",
        "drawingCaption": "Open ball B_ε(x) with dashed boundary vs. Compact set K (closed solid boundary & bounded)",
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
        "topicTitle": "01 · Mathematical Preliminaries & Weierstrass",
        "cardNumber": "02",
        "category": "FUNCTIONAL ANALYSIS",
        "highlighterClass": "highlight-emerald",
        "title": "Lower Semicontinuity & Sublevel Sets",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
            <!-- Axes -->
            <line x1="25" y1="125" x2="220" y2="125" stroke="#475569" stroke-width="1.2"/>
            <line x1="30" y1="130" x2="30" y2="20" stroke="#475569" stroke-width="1.2"/>
            <!-- LSC Function Curve with Jump Down -->
            <path d="M 40 50 Q 80 55 110 70" fill="none" stroke="#10b981" stroke-width="2"/>
            <circle cx="110" cy="70" r="3.5" fill="none" stroke="#10b981" stroke-width="2"/>
            <!-- Lower point at jump -->
            <circle cx="110" cy="95" r="3.5" fill="#10b981"/>
            <path d="M 110 95 Q 160 98 210 40" fill="none" stroke="#10b981" stroke-width="2"/>
            <!-- Sublevel set threshold alpha -->
            <line x1="25" y1="80" x2="220" y2="80" stroke="#f59e0b" stroke-dasharray="3,3" stroke-width="1.2"/>
            <text x="215" y="76" fill="#f59e0b" font-size="8" font-family="monospace">α</text>
            <text x="110" y="112" fill="#10b981" font-size="8" font-family="monospace" text-anchor="middle">f(x₀) ≤ liminf f(x)</text>
          </svg>""",
        "drawingCaption": "Lower semicontinuity: Function can jump downward at boundary x₀, ensuring sublevel set {x : f(x) ≤ α} is closed",
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
        "topicTitle": "01 · Mathematical Preliminaries & Weierstrass",
        "cardNumber": "03",
        "category": "OPTIMIZATION FOUNDATIONS",
        "highlighterClass": "highlight-amber",
        "title": "Weierstrass Extreme Value Theorem",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
            <line x1="25" y1="125" x2="220" y2="125" stroke="#475569" stroke-width="1.2"/>
            <!-- Compact interval [a, b] -->
            <line x1="50" y1="125" x2="190" y2="125" stroke="#f59e0b" stroke-width="3"/>
            <circle cx="50" cy="125" r="3" fill="#f59e0b"/>
            <circle cx="190" cy="125" r="3" fill="#f59e0b"/>
            <text x="50" y="137" fill="#f59e0b" font-size="8" font-family="monospace" text-anchor="middle">a</text>
            <text x="190" y="137" fill="#f59e0b" font-size="8" font-family="monospace" text-anchor="middle">b</text>
            <!-- Continuous Curve on [a, b] -->
            <path d="M 50 65 Q 90 20 120 75 T 190 40" fill="none" stroke="#38bdf8" stroke-width="2.2"/>
            <!-- Global Min & Max points -->
            <circle cx="140" cy="88" r="4" fill="#ef4444"/>
            <circle cx="85" cy="35" r="4" fill="#10b981"/>
            <text x="140" y="103" fill="#ef4444" font-size="8" font-family="monospace" text-anchor="middle">x_min (Achieved!)</text>
            <text x="85" y="27" fill="#10b981" font-size="8" font-family="monospace" text-anchor="middle">x_max (Achieved!)</text>
          </svg>""",
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
        "topicTitle": "01 · Mathematical Preliminaries & Weierstrass",
        "cardNumber": "04",
        "category": "UNCONSTRAINED OPTIMIZATION",
        "highlighterClass": "highlight-violet",
        "title": "Coercivity & Sublevel Compactness",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
            <!-- Coercive Bowl Curve -->
            <path d="M 35 25 Q 70 120 120 120 Q 170 120 205 25" fill="none" stroke="#a855f7" stroke-width="2.5"/>
            <!-- Sublevel set line L_alpha -->
            <line x1="45" y1="75" x2="195" y2="75" stroke="#38bdf8" stroke-dasharray="3,3" stroke-width="1.5"/>
            <text x="200" y="72" fill="#38bdf8" font-size="8" font-family="monospace">f(x₀)</text>
            <!-- Compact Sublevel Domain S -->
            <line x1="58" y1="130" x2="182" y2="130" stroke="#10b981" stroke-width="2.5"/>
            <text x="120" y="140" fill="#10b981" font-size="8" font-family="monospace" text-anchor="middle">S = {x : f(x) ≤ f(x₀)} (Compact!)</text>
            <!-- Arrows to +infinity -->
            <text x="25" y="22" fill="#a855f7" font-size="9" font-family="monospace">f(x)→+∞</text>
            <text x="205" y="22" fill="#a855f7" font-size="9" font-family="monospace">f(x)→+∞</text>
          </svg>""",
        "drawingCaption": "Coercivity: Objective blows up as ||x|| → ∞, trapping minimizing search inside compact sublevel set S",
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
        "topicTitle": "01 · Mathematical Preliminaries & Weierstrass",
        "cardNumber": "05",
        "category": "CONVEX ANALYSIS",
        "highlighterClass": "highlight-indigo",
        "title": "Epigraph & Convexity Geometry",
        "textbookImg": "assets/luenberger_fig7_5.png",
        "textbookRef": "Luenberger & Ye (4th ed), Sect. 7.6, Fig. 7.5 (p. 204)",
        "drawingCaption": "Luenberger Fig. 7.5: The epigraph epi(f) in Rⁿ⁺¹ is a convex set supported by a non-vertical hyperplane",
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
        "topicTitle": "01 · Mathematical Preliminaries & Weierstrass",
        "cardNumber": "06",
        "category": "WORKED BENCHMARK",
        "highlighterClass": "highlight-rose",
        "title": "Worked Benchmark: Coercivity Proof",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
            <!-- Contour circles of f(x) -->
            <ellipse cx="120" cy="72" rx="85" ry="55" fill="none" stroke="#475569" stroke-dasharray="2,2" stroke-width="1"/>
            <ellipse cx="120" cy="72" rx="60" ry="38" fill="none" stroke="#64748b" stroke-width="1.2"/>
            <ellipse cx="120" cy="72" rx="35" ry="22" fill="rgba(56,189,248,0.15)" stroke="#38bdf8" stroke-width="1.5"/>
            <!-- Candidate Minima points at (1,1) and (-1,-1) -->
            <circle cx="100" cy="72" r="3.5" fill="#ef4444"/>
            <circle cx="140" cy="72" r="3.5" fill="#ef4444"/>
            <text x="120" y="38" fill="#cbd5e1" font-size="8" font-family="monospace" text-anchor="middle">f(x) = x₁⁴ + x₂⁴ - 4x₁x₂</text>
            <text x="120" y="115" fill="#10b981" font-size="8" font-family="monospace" text-anchor="middle">S = {x : f(x) ≤ f(0,0)} (Compact!)</text>
          </svg>""",
        "drawingCaption": "Worked Template: Level curves bounded by compact set S containing global minima (±1, ±1)",
        "coreTranslation": [
            "<strong>Problem:</strong> Prove that $f(x_1, x_2) = x_1^4 + x_2^4 - 4x_1 x_2$ attains a global minimum on $\\mathbb{R}^2$.",
            "<strong>Step 1 (Coercivity):</strong> By AM-GM, $4|x_1 x_2| \\le 2(x_1^2 + x_2^2)$. For large $\\|x\\|$, fourth-order terms dominate quadratics: $f(x) \\ge \\frac{1}{2}(x_1^4 + x_2^4) - C \\to +\\infty$. Thus $f$ is coercive.",
            "<strong>Step 2 (Weierstrass on S):</strong> Choose $x_0 = (0,0)$ where $f(0,0)=0$. The sublevel set $S = \\{x : f(x) \\le 0\\}$ is closed and bounded (compact). By Weierstrass, $\\exists x^* \\in S$ achieving $\\min f(x) = -2$ at $(\\pm 1, \\pm 1)$."
        ],
        "math": "$$f(x) \\ge \\frac{1}{2}\\|x\\|^4 - C \\implies \\lim_{\\|x\\| \\to \\infty} f(x) = +\\infty \\implies \\min_{x \\in \\mathbb{R}^2} f(x) \\text{ is attained}$$",
        "personalConnection": "The 3-Step IISc Proof Template: (1) Lower bound by radial norm $\\to$ prove coercivity. (2) Choose base point $x_0$ to isolate compact sublevel set $S$. (3) Invoke Weierstrass on $S$.",
        "examTrap": "Don't just set $\\nabla f(x) = 0$! Stationary points only give local candidates. Setting gradient to zero without proving coercivity leaves the question of whether a global minimum exists completely unanswered."
    },

    # =========================================================================
    # TOPIC 02: Multivariate Taylor Series and Optimality Conditions
    # =========================================================================
    {
        "id": 201,
        "subject": "CMO",
        "topicId": "02_Multivariate_Taylor_Series_and_Optimality_Conditions",
        "topicTitle": "02 · Multivariate Taylor Series & Optimality",
        "cardNumber": "01",
        "category": "MULTIVARIATE CALCULUS",
        "highlighterClass": "highlight-cyan",
        "title": "Multivariate Taylor Theorem",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
            <!-- Curve and tangent parabola -->
            <path d="M 30 110 Q 100 20 210 50" fill="none" stroke="#475569" stroke-width="1.2" stroke-dasharray="3,3"/>
            <!-- 2nd order Taylor quadratic approximation -->
            <path d="M 45 118 Q 110 32 195 45" fill="none" stroke="#38bdf8" stroke-width="2.2"/>
            <circle cx="110" cy="36" r="3.5" fill="#f59e0b"/>
            <text x="110" y="24" fill="#f59e0b" font-size="8" font-family="monospace" text-anchor="middle">x* (Basepoint)</text>
            <line x1="110" y1="36" x2="170" y2="40" stroke="#ec4899" stroke-width="1.5"/>
            <text x="145" y="52" fill="#ec4899" font-size="8" font-family="monospace">d</text>
            <text x="120" y="132" fill="#38bdf8" font-size="8" font-family="monospace" text-anchor="middle">f(x*+d) ≈ f(x*) + ∇fᵀd + ½ dᵀ∇²f d</text>
          </svg>""",
        "drawingCaption": "Taylor Quadratic Approximation: Local landscape modeled by gradient slope ∇f and curvature Hessian ∇²f",
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
        "topicTitle": "02 · Multivariate Taylor Series & Optimality",
        "cardNumber": "02",
        "category": "FIRST-ORDER OPTIMALITY",
        "highlighterClass": "highlight-amber",
        "title": "First-Order Necessary Condition (FONC)",
        "textbookImg": "assets/luenberger_fig7_1.png",
        "textbookRef": "Luenberger & Ye (4th ed), Sect. 7.1, Fig. 7.1 (p. 191)",
        "drawingCaption": "Luenberger Fig. 7.1: Directional derivative ϕ'(0) = ∇f(x*)ᵀd must equal 0 in all directions d ∈ Rⁿ",
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
        "topicTitle": "02 · Multivariate Taylor Series & Optimality",
        "cardNumber": "03",
        "category": "SECOND-ORDER OPTIMALITY",
        "highlighterClass": "highlight-emerald",
        "title": "Second-Order Necessary Condition (SONC)",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
            <!-- Upward Curvature Bowl -->
            <path d="M 40 40 Q 120 130 200 40" fill="none" stroke="#10b981" stroke-width="2.5"/>
            <circle cx="120" cy="85" r="4" fill="#f59e0b"/>
            <!-- Zero tangent line -->
            <line x1="80" y1="85" x2="160" y2="85" stroke="#38bdf8" stroke-dasharray="3,3" stroke-width="1.5"/>
            <text x="120" y="103" fill="#10b981" font-size="9" font-family="monospace" text-anchor="middle">∇²f(x*) ⪰ 0 (Positive Semidefinite)</text>
            <text x="120" y="117" fill="#cbd5e1" font-size="8" font-family="monospace" text-anchor="middle">λ_min(∇²f) ≥ 0</text>
          </svg>""",
        "drawingCaption": "SONC: At a local minimum, the terrain must curve upward or stay flat in every direction (∇²f(x*) ⪰ 0)",
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
        "topicTitle": "02 · Multivariate Taylor Series & Optimality",
        "cardNumber": "04",
        "category": "SUFFICIENT CONDITIONS",
        "highlighterClass": "highlight-violet",
        "title": "Second-Order Sufficient Condition (SOSC)",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
            <!-- Strictly convex quadratic bowl -->
            <path d="M 45 30 Q 120 125 195 30" fill="none" stroke="#a855f7" stroke-width="2.5"/>
            <circle cx="120" cy="78" r="4" fill="#38bdf8"/>
            <text x="120" y="98" fill="#38bdf8" font-size="9" font-family="monospace" text-anchor="middle">∇²f(x*) ≻ 0 (Strictly Positive Definite)</text>
            <text x="120" y="112" fill="#cbd5e1" font-size="8" font-family="monospace" text-anchor="middle">λ_min > 0 ⟹ Strict Local Minimizer</text>
          </svg>""",
        "drawingCaption": "SOSC: Strictly positive eigenvalues (λ_min > 0) guarantee a strict local valley with quadratic growth",
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
        "topicTitle": "02 · Multivariate Taylor Series & Optimality",
        "cardNumber": "05",
        "category": "EIGENVALUE CLASSIFICATION",
        "highlighterClass": "highlight-indigo",
        "title": "Hessian Spectral Classification of Critical Points",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
            <!-- Saddle surface wireframe -->
            <path d="M 50 40 Q 120 90 190 40" fill="none" stroke="#ef4444" stroke-width="2"/>
            <path d="M 120 20 Q 120 70 120 120" fill="none" stroke="#38bdf8" stroke-width="2"/>
            <circle cx="120" cy="65" r="4" fill="#f59e0b"/>
            <text x="120" y="80" fill="#f59e0b" font-size="8" font-family="monospace" text-anchor="middle">Saddle Point (λ₁ > 0, λ₂ < 0)</text>
            <text x="50" y="32" fill="#ef4444" font-size="8" font-family="monospace">Curving UP</text>
            <text x="190" y="125" fill="#38bdf8" font-size="8" font-family="monospace" text-anchor="end">Curving DOWN</text>
          </svg>""",
        "drawingCaption": "Saddle Point: Hessian has mixed eigenvalue signs (λ₁ > 0, λ₂ < 0), permitting descent along negative eigenvector",
        "coreTranslation": [
            "At any critical point where $\\nabla f(x^*) = 0$, the Hessian eigenvalues $\\{\\lambda_1, \\dots, \\lambda_n\\}$ govern the local topology:",
            "<strong>Local Minimum:</strong> All $\\lambda_i > 0$ (positive definite). <strong>Local Maximum:</strong> All $\\lambda_i < 0$ (negative definite).",
            "<strong>Saddle Point:</strong> Both positive and negative eigenvalues exist (indefinite). The eigenvector $v$ corresponding to $\\lambda_{\\min} < 0$ provides a strict <strong>negative curvature descent direction</strong>: $v^T \\nabla^2 f(x^*) v < 0$."
        ],
        "math": "$$\\text{Saddle Point} \\iff \\exists \\, i, j \\text{ s.t. } \\lambda_i(\\nabla^2 f(x^*)) > 0 \\text{ and } \\lambda_j(\\nabla^2 f(x^*)) < 0$$",
        "personalConnection": "A horse saddle or mountain pass: you are at the lowest point along the north-south ridge, but at the highest point along the east-west trail.",
        "examTrap": "Sylvester's Criterion for negative definiteness requires alternating leading principal minors: $(-1)^k \\Delta_k > 0$ ($\Delta_1 < 0, \\Delta_2 > 0, \\Delta_3 < 0$). Many students erroneously check if all $\\Delta_k < 0$."
    },
    {
        "id": 206,
        "subject": "CMO",
        "topicId": "02_Multivariate_Taylor_Series_and_Optimality_Conditions",
        "topicTitle": "02 · Multivariate Taylor Series & Optimality",
        "cardNumber": "06",
        "category": "WORKED BENCHMARK",
        "highlighterClass": "highlight-rose",
        "title": "Worked Benchmark: Rosenbrock Critical Points",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
            <!-- Banana Valley Curve -->
            <path d="M 40 115 Q 110 95 180 35" fill="none" stroke="#f59e0b" stroke-width="2.5"/>
            <circle cx="180" cy="35" r="4" fill="#10b981"/>
            <text x="180" y="24" fill="#10b981" font-size="8" font-family="monospace" text-anchor="middle">Global Min (1, 1)</text>
            <text x="40" y="130" fill="#94a3b8" font-size="8" font-family="monospace">f(x,y) = 100(y - x²)² + (1 - x)²</text>
          </svg>""",
        "drawingCaption": "Rosenbrock Valley: Deep parabolic trough x₂ = x₁² leading to unique global minimum at (1, 1)",
        "coreTranslation": [
            "<strong>Problem:</strong> Analyze critical points of Rosenbrock's function $f(x, y) = 100(y - x^2)^2 + (1 - x)^2$.",
            "<strong>Step 1 (Gradient = 0):</strong> $\\nabla f = [-400x(y-x^2) - 2(1-x), \\; 200(y-x^2)]^T = [0, 0]^T$. The 2nd equation gives $y = x^2$. Substituting into 1st gives $-2(1-x) = 0 \\implies x^* = 1, y^* = 1$.",
            "<strong>Step 2 (Hessian at (1, 1)):</strong> $\\nabla^2 f(1, 1) = \\begin{bmatrix} 802 & -400 \\\\ -400 & 200 \\end{bmatrix}$. Trace $= 1002 > 0$, Determinant $= 802(200) - 160000 = 400 > 0$. Both eigenvalues are strictly positive $\\implies$ unique strict local (and global) minimum!"
        ],
        "math": "$$\\nabla f(1, 1) = \\mathbf{0}, \\quad \\det(\\nabla^2 f) = 400 > 0, \\quad \\operatorname{tr}(\\nabla^2 f) = 1002 > 0 \\implies (1,1) \\text{ is strict min}$$",
        "personalConnection": "Finding the drain in a curved sink: the valley bottom is along $y = x^2$. Moving along the valley requires tiny adjustments because the Hessian condition number $\\kappa \\approx 2500$ is massive.",
        "examTrap": "When evaluating $2 \\times 2$ Hessians, always check BOTH $\\det(H) > 0$ and $\\operatorname{tr}(H) > 0$. If $\\det(H) > 0$ and $\\operatorname{tr}(H) < 0$, both eigenvalues are negative, giving a local MAXIMUM!"
    },

    # =========================================================================
    # TOPIC 03: Convexity and Strong Convexity
    # =========================================================================
    {
        "id": 301,
        "subject": "CMO",
        "topicId": "03_Convexity_and_Strong_Convexity",
        "topicTitle": "03 · Convexity & Strong Convexity",
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
        "topicTitle": "03 · Convexity & Strong Convexity",
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
        "topicTitle": "03 · Convexity & Strong Convexity",
        "cardNumber": "03",
        "category": "SECOND-ORDER CONVEXITY",
        "highlighterClass": "highlight-emerald",
        "title": "Second-Order Condition: Global PSD Hessian",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
            <!-- Global Convex Basin -->
            <path d="M 35 25 Q 120 135 205 25" fill="none" stroke="#10b981" stroke-width="2.5"/>
            <!-- Curvature indicators at multiple points -->
            <circle cx="70" cy="65" r="3" fill="#38bdf8"/>
            <circle cx="120" cy="80" r="3" fill="#f59e0b"/>
            <circle cx="170" cy="65" r="3" fill="#38bdf8"/>
            <text x="120" y="105" fill="#10b981" font-size="9" font-family="monospace" text-anchor="middle">∇²f(x) ⪰ 0 for ALL x ∈ C</text>
            <text x="120" y="120" fill="#cbd5e1" font-size="8" font-family="monospace" text-anchor="middle">Global Positive Semidefiniteness</text>
          </svg>""",
        "drawingCaption": "Second-Order Convexity: Hessian matrix ∇²f(x) must remain positive semidefinite everywhere across domain C",
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
        "topicTitle": "03 · Convexity & Strong Convexity",
        "cardNumber": "04",
        "category": "STRONG CONVEXITY",
        "highlighterClass": "highlight-violet",
        "title": "Strong Convexity & Quadratic Lower Bound",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
            <!-- Strongly convex curve -->
            <path d="M 40 30 Q 120 130 200 30" fill="none" stroke="#a855f7" stroke-width="2.5"/>
            <!-- Quadratic underestimator parabola -->
            <path d="M 55 50 Q 120 130 185 50" fill="none" stroke="#38bdf8" stroke-dasharray="3,3" stroke-width="1.8"/>
            <circle cx="120" cy="80" r="3.5" fill="#f59e0b"/>
            <text x="120" y="100" fill="#a855f7" font-size="8" font-family="monospace" text-anchor="middle">f(y) ≥ f(x) + ∇fᵀ(y-x) + (μ/2)||y-x||²</text>
            <text x="120" y="115" fill="#38bdf8" font-size="8" font-family="monospace" text-anchor="middle">Hessian Curvature: ∇²f(x) ⪰ μI (μ > 0)</text>
          </svg>""",
        "drawingCaption": "Strong Convexity: Objective is uniformly curved with a quadratic lower bowl parameter μ > 0",
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
        "topicTitle": "03 · Convexity & Strong Convexity",
        "cardNumber": "05",
        "category": "GRADIENT DOMINANCE",
        "highlighterClass": "highlight-indigo",
        "title": "Polyak-Łojasiewicz (PL) Inequality",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
            <!-- Curve and gradient vector -->
            <path d="M 40 35 Q 120 120 200 35" fill="none" stroke="#6366f1" stroke-width="2.5"/>
            <circle cx="160" cy="55" r="3.5" fill="#ef4444"/>
            <line x1="160" y1="55" x2="190" y2="40" stroke="#ef4444" stroke-width="2"/>
            <text x="180" y="32" fill="#ef4444" font-size="8" font-family="monospace">∇f(x)</text>
            <circle cx="120" cy="78" r="3.5" fill="#10b981"/>
            <text x="120" y="93" fill="#10b981" font-size="8" font-family="monospace" text-anchor="middle">x* (Global Min)</text>
            <text x="120" y="115" fill="#6366f1" font-size="9" font-family="monospace" text-anchor="middle">||∇f(x)||² ≥ 2μ(f(x) - f*)</text>
          </svg>""",
        "drawingCaption": "PL Inequality: Gradient magnitude ||∇f(x)||² dominates suboptimality gap, guaranteeing linear convergence",
        "coreTranslation": [
            "<strong>Theorem:</strong> Every $\\mu$-strongly convex function satisfies the <strong>Polyak-Łojasiewicz (PL) inequality</strong>: $\\frac{1}{2}\\|\\nabla f(x)\\|^2 \\ge \\mu (f(x) - f^*)$.",
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
        "topicTitle": "03 · Convexity & Strong Convexity",
        "cardNumber": "06",
        "category": "WORKED BENCHMARK",
        "highlighterClass": "highlight-rose",
        "title": "Worked Benchmark: Convexity Hierarchy Traps",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
            <!-- Table / Venn Hierarchy -->
            <rect x="25" y="25" width="190" height="95" rx="10" fill="rgba(99,102,241,0.08)" stroke="#6366f1" stroke-width="1.2"/>
            <rect x="40" y="40" width="160" height="70" rx="8" fill="rgba(168,85,247,0.12)" stroke="#a855f7" stroke-width="1.2"/>
            <rect x="55" y="55" width="130" height="45" rx="6" fill="rgba(56,189,248,0.18)" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="120" y="36" fill="#6366f1" font-size="8" font-family="monospace" text-anchor="middle">Convex Functions (f'' ≥ 0)</text>
            <text x="120" y="50" fill="#a855f7" font-size="8" font-family="monospace" text-anchor="middle">Strictly Convex (f(x) = x⁴)</text>
            <text x="120" y="80" fill="#38bdf8" font-size="8" font-family="monospace" text-anchor="middle" font-weight="bold">Strongly Convex (f'' ≥ μ > 0)</text>
          </svg>""",
        "drawingCaption": "Hierarchy: Strongly Convex ⊂ Strictly Convex ⊂ Convex. Understanding classic counterexamples prevents exam traps",
        "coreTranslation": [
            "<strong>Convexity Hierarchy:</strong> $\\mu\\text{-Strongly Convex} \\subsetneq \\text{Strictly Convex} \\subsetneq \\text{Convex}$.",
            "<strong>Counterexample 1 ($x^4$):</strong> $f(x) = x^4$ is strictly convex on $\\mathbb{R}$, but $f''(0) = 0$. Hence it is NOT strongly convex.",
            "<strong>Counterexample 2 ($e^x$):</strong> $f(x) = e^x$ is strictly convex on $\\mathbb{R}$ with $f''(x) = e^x > 0$, but $\\lim_{x \\to -\\infty} f''(x) = 0$. Hence it is NOT strongly convex on $\\mathbb{R}$."
        ],
        "math": "$$\\mu\\text{-Strongly Convex } (\\nabla^2 f \\succeq \\mu I) \\implies \\text{Strictly Convex} \\implies \\text{Convex } (\\nabla^2 f \\succeq 0)$$",
        "personalConnection": "Convex = flat surfaces allowed (e.g. ramps). Strictly convex = no flat line segments, but can flatten infinitesimally ($x^4$). Strongly convex = strictly curved everywhere like a bowling ball.",
        "examTrap": "An exam question asking 'Is $f(x) = e^{-x} + x^2$ strongly convex on $\\mathbb{R}$?' Answer: YES! $f''(x) = e^{-x} + 2 \\ge 2 > 0$ for all $x$, so $\\mu = 2$."
    },

    # =========================================================================
    # TOPIC 04: Line Search Methods: Exact, Armijo and Wolfe
    # =========================================================================
    {
        "id": 401,
        "subject": "CMO",
        "topicId": "04_Line_Search_Methods_Exact_Armijo_and_Wolfe",
        "topicTitle": "04 · Line Search (Armijo & Wolfe)",
        "cardNumber": "01",
        "category": "LINE SEARCH FOUNDATIONS",
        "highlighterClass": "highlight-cyan",
        "title": "Line Search Framework & Descent Directions",
        "textbookImg": "assets/luenberger_fig8_1.png",
        "textbookRef": "Luenberger & Ye (4th ed), Sect. 8.1, Fig. 8.1 (p. 224)",
        "drawingCaption": "Luenberger Fig. 8.1: Unimodal 1D objective ϕ(α) = f(x_k + α d_k) along search ray d_k",
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
        "topicTitle": "04 · Line Search (Armijo & Wolfe)",
        "cardNumber": "02",
        "category": "QUADRATIC EXACT LINE SEARCH",
        "highlighterClass": "highlight-amber",
        "title": "Exact Line Search for Quadratic Forms",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
            <!-- 1D Parabola for phi(alpha) -->
            <path d="M 40 40 Q 120 125 200 40" fill="none" stroke="#f59e0b" stroke-width="2.5"/>
            <line x1="80" y1="83" x2="160" y2="83" stroke="#38bdf8" stroke-dasharray="3,3" stroke-width="1.5"/>
            <circle cx="120" cy="83" r="4" fill="#10b981"/>
            <text x="120" y="103" fill="#10b981" font-size="8" font-family="monospace" text-anchor="middle">α* = -g_kᵀd_k / (d_kᵀ Q d_k)</text>
            <text x="120" y="118" fill="#cbd5e1" font-size="8" font-family="monospace" text-anchor="middle">Exact 1D Minimizer: ϕ'(α*) = 0</text>
          </svg>""",
        "drawingCaption": "Exact Line Search on Quadratic: Optimal step length α* obtained analytically by setting derivative to zero",
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
        "topicTitle": "04 · Line Search (Armijo & Wolfe)",
        "cardNumber": "03",
        "category": "INEXACT LINE SEARCH",
        "highlighterClass": "highlight-emerald",
        "title": "Armijo Sufficient Decrease Condition",
        "textbookImg": "assets/luenberger_fig8_8.png",
        "textbookRef": "Luenberger & Ye (4th ed), Sect. 8.1, Fig. 8.8 (p. 239)",
        "drawingCaption": "Luenberger Fig. 8.8: Armijo rule accepts step sizes where curve f(x_k + α d_k) lies below the linear bound line",
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
        "topicTitle": "04 · Line Search (Armijo & Wolfe)",
        "cardNumber": "04",
        "category": "WOLFE CONDITIONS",
        "highlighterClass": "highlight-violet",
        "title": "Curvature Condition & Strong Wolfe Conditions",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
            <!-- 1D Curve with Armijo Line and Curvature Bounds -->
            <path d="M 30 30 Q 110 120 210 50" fill="none" stroke="#a855f7" stroke-width="2.5"/>
            <!-- Armijo line -->
            <line x1="30" y1="30" x2="180" y2="105" stroke="#ef4444" stroke-dasharray="3,3" stroke-width="1.5"/>
            <text x="185" y="105" fill="#ef4444" font-size="8" font-family="monospace">Armijo Line</text>
            <!-- Valid Wolfe interval -->
            <line x1="85" y1="125" x2="165" y2="125" stroke="#10b981" stroke-width="3"/>
            <text x="125" y="137" fill="#10b981" font-size="8" font-family="monospace" text-anchor="middle">Valid Wolfe Step Interval [α_min, α_max]</text>
          </svg>""",
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
        "topicTitle": "04 · Line Search (Armijo & Wolfe)",
        "cardNumber": "05",
        "category": "CONVERGENCE THEOREM",
        "highlighterClass": "highlight-indigo",
        "title": "Zoutendijk’s Theorem & Global Convergence",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
            <!-- Vector Angle diagram -->
            <line x1="120" y1="80" x2="60" y2="40" stroke="#ef4444" stroke-width="2"/>
            <text x="50" y="35" fill="#ef4444" font-size="8" font-family="monospace">-∇f(x_k)</text>
            <line x1="120" y1="80" x2="80" y2="120" stroke="#38bdf8" stroke-width="2"/>
            <text x="65" y="130" fill="#38bdf8" font-size="8" font-family="monospace">d_k</text>
            <!-- Angle arc -->
            <path d="M 95 65 A 30 30 0 0 0 102 98" fill="none" stroke="#f59e0b" stroke-width="1.5"/>
            <text x="110" y="85" fill="#f59e0b" font-size="8" font-family="monospace">θ_k</text>
            <text x="140" y="130" fill="#cbd5e1" font-size="8" font-family="monospace">cos θ_k = -∇fᵀd / (||∇f|| ||d||)</text>
          </svg>""",
        "drawingCaption": "Zoutendijk Angle: Angle θ_k between search direction d_k and steepest descent direction -∇f(x_k)",
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
        "topicTitle": "04 · Line Search (Armijo & Wolfe)",
        "cardNumber": "06",
        "category": "ALGORITHMIC IMPLEMENTATION",
        "highlighterClass": "highlight-rose",
        "title": "Backtracking Line Search Algorithm",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
            <!-- Backtracking Steps: alpha_0 -> rho*alpha_0 -> rho^2*alpha_0 -->
            <circle cx="190" cy="50" r="4" fill="#ef4444"/>
            <text x="190" y="38" fill="#ef4444" font-size="8" font-family="monospace" text-anchor="middle">α = 1 (Rejected)</text>
            <circle cx="130" cy="75" r="4" fill="#f59e0b"/>
            <text x="130" y="65" fill="#f59e0b" font-size="8" font-family="monospace" text-anchor="middle">α = ρ (Rejected)</text>
            <circle cx="80" cy="95" r="4" fill="#10b981"/>
            <text x="80" y="112" fill="#10b981" font-size="8" font-family="monospace" text-anchor="middle">α = ρ² (Accepted!)</text>
            <path d="M 185 55 Q 155 75 135 75" fill="none" stroke="#cbd5e1" stroke-dasharray="2,2"/>
            <path d="M 125 80 Q 100 95 85 95" fill="none" stroke="#cbd5e1" stroke-dasharray="2,2"/>
          </svg>""",
        "drawingCaption": "Backtracking: Start boldly at initial α = 1, systematically contracting α ← ρ α until Armijo condition holds",
        "coreTranslation": [
            "<strong>Algorithm:</strong> Choose $\\alpha_0 = 1$, contraction factor $\\rho \\in (0, 1)$ (e.g. $\\rho = 0.5$), and Armijo constant $c_1 \\in (0, 1)$.",
            "While $f(x_k + \\alpha d_k) > f(x_k) + c_1 \\alpha \\nabla f(x_k)^T d_k$ do: $\\alpha \\leftarrow \\rho \\alpha$. Return $\\alpha_k = \\alpha$.",
            "<strong>Why $\\alpha_0 = 1$ is Essential:</strong> For Newton and Quasi-Newton methods, starting at unit step size $\\alpha_0 = 1$ allows the algorithm to naturally adopt quadratic or superlinear convergence near $x^*$."
        ],
        "math": "$$\\alpha^{(j+1)} = \\rho \\alpha^{(j)}, \\quad \\rho \\in (0, 1), \\quad \\text{until } f(x + \\alpha d) \\le f(x) + c_1 \\alpha \\nabla f(x)^T d$$",
        "personalConnection": "Testing water temperature with your toe: you plan a full forward step, but if the water burns, you immediately step backward halfway, repeating until the temperature is comfortable.",
        "examTrap": "Never start backtracking with $\\alpha_0 < 1$ in Newton's method! Restricting $\\alpha_0 < 1$ permanently degrades Newton's quadratic convergence to slow linear convergence."
    },

    # =========================================================================
    # TOPIC 05: Gradient Descent and Convergence Analysis
    # =========================================================================
    {
        "id": 501,
        "subject": "CMO",
        "topicId": "05_Gradient_Descent_and_Convergence_Analysis",
        "topicTitle": "05 · Gradient Descent & Convergence",
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
        "topicTitle": "05 · Gradient Descent & Convergence",
        "cardNumber": "02",
        "category": "CONVERGENCE ANALYSIS",
        "highlighterClass": "highlight-amber",
        "title": "O(1/k) Convergence on L-Smooth Convex Objectives",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
            <!-- 1/k Convergence curve -->
            <path d="M 30 30 Q 60 100 210 115" fill="none" stroke="#f59e0b" stroke-width="2.5"/>
            <circle cx="30" cy="30" r="3.5" fill="#ef4444"/>
            <circle cx="90" cy="103" r="3.5" fill="#38bdf8"/>
            <circle cx="180" cy="113" r="3.5" fill="#10b981"/>
            <text x="120" y="60" fill="#f59e0b" font-size="9" font-family="monospace" text-anchor="middle">f(x_k) - f* ≤ L ||x₀ - x*||² / (2k)</text>
            <text x="120" y="80" fill="#cbd5e1" font-size="8" font-family="monospace" text-anchor="middle">Step size: α = 1/L (Sublinear O(1/k))</text>
          </svg>""",
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
        "topicTitle": "05 · Gradient Descent & Convergence",
        "cardNumber": "03",
        "category": "LINEAR CONVERGENCE",
        "highlighterClass": "highlight-emerald",
        "title": "Linear Convergence on Strongly Convex Functions",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
            <!-- Exponential decay semilog line -->
            <path d="M 30 25 L 210 120" fill="none" stroke="#10b981" stroke-width="2.5"/>
            <circle cx="30" cy="25" r="3.5" fill="#f59e0b"/>
            <circle cx="90" cy="57" r="3.5" fill="#38bdf8"/>
            <circle cx="150" cy="88" r="3.5" fill="#38bdf8"/>
            <circle cx="210" cy="120" r="3.5" fill="#10b981"/>
            <text x="120" y="45" fill="#10b981" font-size="9" font-family="monospace" text-anchor="middle">||x_k - x*|| ≤ C · ((κ-1)/(κ+1))^k</text>
            <text x="120" y="135" fill="#cbd5e1" font-size="8" font-family="monospace" text-anchor="middle">Linear (Geometric) Rate: Error halves every N steps</text>
          </svg>""",
        "drawingCaption": "Linear Convergence: Error decays exponentially as a straight line on semilog scale with contraction factor (κ-1)/(κ+1)",
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
        "topicTitle": "05 · Gradient Descent & Convergence",
        "cardNumber": "04",
        "category": "KANTOROVICH INEQUALITY",
        "highlighterClass": "highlight-violet",
        "title": "Kantorovich Inequality & Quadratic Bound",
        "textbookImg": "assets/luenberger_fig8_10.png",
        "textbookRef": "Luenberger & Ye (4th ed), Sect. 8.3, Fig. 8.10 (p. 245)",
        "drawingCaption": "Luenberger Fig. 8.10: The convex curve 1/λ and the secant line establishing the Kantorovich ratio bound",
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
        "topicTitle": "05 · Gradient Descent & Convergence",
        "cardNumber": "05",
        "category": "CONDITION NUMBER DYNAMICS",
        "highlighterClass": "highlight-indigo",
        "title": "Condition Number κ & The Zig-Zag Phenomenon",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
            <!-- Elongated Ellipses -->
            <ellipse cx="120" cy="72" rx="95" ry="25" fill="none" stroke="#475569" stroke-width="1.2"/>
            <ellipse cx="120" cy="72" rx="60" ry="15" fill="none" stroke="#64748b" stroke-width="1.2"/>
            <!-- Zig-zag trajectory -->
            <polyline points="40,90 85,55 95,85 110,62 118,78 120,72" fill="none" stroke="#ef4444" stroke-width="1.8"/>
            <circle cx="120" cy="72" r="3.5" fill="#10b981"/>
            <text x="120" y="30" fill="#cbd5e1" font-size="8" font-family="monospace" text-anchor="middle">Ill-Conditioned Valley: κ = λ_max / λ_min ≫ 1</text>
            <text x="120" y="115" fill="#ef4444" font-size="8" font-family="monospace" text-anchor="middle">Severe 90° Zig-Zag Trajectory</text>
          </svg>""",
        "drawingCaption": "Zig-Zagging: When condition number κ ≫ 1, steepest descent bounces between steep canyon walls rather than gliding along the floor",
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
        "topicTitle": "05 · Gradient Descent & Convergence",
        "cardNumber": "06",
        "category": "ADVANCED STEP SIZES",
        "highlighterClass": "highlight-rose",
        "title": "Barzilai-Borwein & Heavy Ball Momentum",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
            <!-- Momentum smooth trajectory vs zig zag -->
            <polyline points="40,90 85,55 95,85 110,62" fill="none" stroke="#ef4444" stroke-width="1.2" stroke-dasharray="2,2"/>
            <!-- Momentum curve -->
            <path d="M 40 90 Q 90 70 120 72" fill="none" stroke="#10b981" stroke-width="2.5"/>
            <circle cx="120" cy="72" r="3.5" fill="#10b981"/>
            <text x="120" y="55" fill="#10b981" font-size="8" font-family="monospace" text-anchor="middle">Heavy Ball Momentum: β(x_k - x_{k-1})</text>
            <text x="120" y="115" fill="#38bdf8" font-size="8" font-family="monospace" text-anchor="middle">BB Spectral Step: α_k = (sᵀy) / ||y||²</text>
          </svg>""",
        "drawingCaption": "Acceleration: Momentum dampens oscillations along steep directions while accelerating down flat valley floors",
        "coreTranslation": [
            "<strong>Barzilai-Borwein (BB) Method:</strong> Uses secant equation $s_k \\approx \\alpha y_k$ (where $s_k = x_k - x_{k-1}$ and $y_k = g_k - g_{k-1}$) to choose step size without line search: $\\alpha_{k}^{BB1} = \\frac{s_k^T y_k}{y_k^T y_k}$, $\\alpha_{k}^{BB2} = \\frac{s_k^T s_k}{s_k^T y_k}$.",
            "BB step sizes produce non-monotonic objective decrease, but achieve dramatically faster convergence on ill-conditioned problems.",
            "<strong>Polyak's Heavy Ball:</strong> Adds momentum: $x_{k+1} = x_k - \\alpha \\nabla f(x_k) + \\beta (x_k - x_{k-1})$. Improves convergence rate from $\\frac{\\kappa-1}{\\kappa+1}$ to $\\frac{\\sqrt{\\kappa}-1}{\\sqrt{\\kappa}+1}$!"
        ],
        "math": "$$x_{k+1} = x_k - \\alpha \\nabla f(x_k) + \\beta(x_k - x_{k-1}), \\quad \\text{Rate: } \\frac{\\sqrt{\\kappa}-1}{\\sqrt{\\kappa}+1}$$",
        "personalConnection": "Rolling a heavy bowling ball down a washboard road: its inertia prevents it from bouncing erratically into every side ditch, rolling smoothly through the center.",
        "examTrap": "Heavy Ball momentum does NOT guarantee convergence on general non-convex functions (it can overshoot and oscillate). Nesterov accelerated gradient (NAG) fixes this by computing gradient at the look-ahead point."
    }
]

# Write to cards_data.js
with open("/Users/senso/Projects/photographic-memory-cards/cards_data.js", "w") as f:
    f.write("/* Master Cards Database for CMO, LAA, StoMA, DIP */\n")
    f.write("window.MASTER_CARDS_DATA = ")
    json.dump(cards, f, indent=2)
    f.write(";\n")

print(f"Successfully generated cards_data.js with {len(cards)} cards!")
