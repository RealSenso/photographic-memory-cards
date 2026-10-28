import json

# =============================================================================
# TOPIC 17: Wolfe Duality
# =============================================================================
topic17_cards = [
    {
        "id": 1701,
        "subject": "CMO",
        "topicId": "17_Wolfe_Duality",
        "topicTitle": "17 · Wolfe Duality",
        "cardNumber": "01",
        "category": "DUAL FORMULATIONS",
        "highlighterClass": "highlight-cyan",
        "title": "The Wolfe Dual Formulation for Convex NLP",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <!-- Primal NLP box -->
  <rect x="25" y="30" width="85" height="85" rx="6" fill="#f8fafc" stroke="#000000" stroke-width="1.8"/>
  <text x="67" y="50" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">PRIMAL (NLP)</text>
  <text x="67" y="70" fill="#000000" font-size="8.5" font-family="serif" text-anchor="middle">min f(x)</text>
  <text x="67" y="88" fill="#000000" font-size="8" font-family="serif" text-anchor="middle">s.t. g(x) ≤ 0</text>
  <text x="67" y="103" fill="#000000" font-size="8" font-family="serif" text-anchor="middle">h(x) = 0</text>
  <!-- Equivalence arrows -->
  <line x1="115" y1="72" x2="130" y2="72" stroke="#000000" stroke-width="2"/>
  <!-- Wolfe Dual box -->
  <rect x="135" y="30" width="85" height="85" rx="6" fill="#f1f5f9" stroke="#000000" stroke-width="1.8"/>
  <text x="177" y="50" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">WOLFE DUAL</text>
  <text x="177" y="70" fill="#000000" font-size="8.5" font-family="serif" text-anchor="middle">max ℒ(x, λ, μ)</text>
  <text x="177" y="88" fill="#000000" font-size="8" font-family="serif" text-anchor="middle">s.t. ∇_x ℒ = 0</text>
  <text x="177" y="103" fill="#000000" font-size="8" font-family="serif" text-anchor="middle">μ ≥ 0</text>
  <text x="120" y="136" fill="#000000" font-size="8.5" font-family="sans-serif" text-anchor="middle">Wolfe explicitly couples primal variables x and dual multipliers via ∇_x ℒ = 0</text>
</svg>""",
        "drawingCaption": "Wolfe Duality: Replaces unconstrained infimum over x with an explicit stationarity constraint ∇_x ℒ = 0",
        "coreTranslation": [
            "<strong>Primal Problem:</strong> Minimize $f(x)$ subject to $g_j(x) \\le 0$ ($j=1..m$) and $h_i(x) = 0$ ($i=1..p$).",
            "<strong>Lagrangian Duality vs. Wolfe:</strong> Standard Lagrange duality defines $q(\\lambda, \\mu) = \\inf_x \\mathcal{L}(x, \\lambda, \\mu)$, which often requires eliminating $x$ analytically. If $x$ cannot be eliminated, the dual problem is hard to evaluate.",
            "<strong>The Wolfe Dual:</strong> Philip Wolfe (1961) observed that for convex $f, g$, the infimum over $x$ must occur where the gradient with respect to $x$ vanishes! Thus, Wolfe treats both $(x, \\lambda, \\mu)$ as joint optimization variables:",
            "$$\\max_{x, \\lambda, \\mu} \\mathcal{L}(x, \\lambda, \\mu) = f(x) + \\sum_{i=1}^p \\lambda_i h_i(x) + \\sum_{j=1}^m \\mu_j g_j(x) \\quad \\text{s.t. } \\nabla_x \\mathcal{L}(x, \\lambda, \\mu) = 0, \\; \\mu \\ge 0$$"
        ],
        "math": "$$\\max_{x, \\lambda, \\mu} \\left\\{ f(x) + \\lambda^T h(x) + \\mu^T g(x) \\right\\} \\quad \\text{subject to} \\quad \\nabla f(x) + \\nabla h(x) \\lambda + \\nabla g(x) \\mu = \\mathbf{0}, \\; \\mu \\ge 0$$",
        "personalConnection": "Pricing an apartment: instead of searching through every possible floor plan to find the cheapest cost, you restrict your search strictly to architects who have already optimized their floor blueprints (satisfying $\\nabla_x \\mathcal{L} = 0$).",
        "examTrap": "The variable $x$ in the Wolfe dual DOES NOT need to be primal feasible ($g(x) \\le 0$ is NOT required in the Wolfe dual)! The only constraints on $(x, \\lambda, \\mu)$ in the Wolfe dual are $\\nabla_x \\mathcal{L} = 0$ and $\\mu \\ge 0$."
    },
    {
        "id": 1702,
        "subject": "CMO",
        "topicId": "17_Wolfe_Duality",
        "topicTitle": "17 · Wolfe Duality",
        "cardNumber": "02",
        "category": "WOLFE THEOREMS",
        "highlighterClass": "highlight-amber",
        "title": "Wolfe Duality Theorem & Zero Duality Gap",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <!-- Primal descent and dual ascent curves meeting at x* -->
  <path d="M 40 30 Q 120 70 200 70" fill="none" stroke="#000000" stroke-width="2"/>
  <text x="50" y="25" fill="#000000" font-size="8.5" font-family="serif">Primal f(x) descends</text>
  <path d="M 40 120 Q 120 70 200 70" fill="none" stroke="#000000" stroke-width="2"/>
  <text x="50" y="130" fill="#000000" font-size="8.5" font-family="serif">Dual ℒ(x, μ) ascends</text>
  <!-- Meeting point at optimal value -->
  <circle cx="170" cy="70" r="4.5" fill="#000000"/>
  <text x="170" y="58" fill="#000000" font-size="9" font-family="serif" font-weight="bold" text-anchor="middle">f(x*) = ℒ(x*, μ*)</text>
  <text x="120" y="18" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Wolfe Duality Theorem (Convex f, Convex g)</text>
  <text x="120" y="138" fill="#000000" font-size="8" font-family="sans-serif" text-anchor="middle">If x* solves primal with KKT multipliers μ*, (x*, μ*) solves Wolfe dual</text>
</svg>""",
        "drawingCaption": "Wolfe Duality Theorem: For convex problems, the primal minimum equals the Wolfe dual maximum with zero duality gap",
        "coreTranslation": [
            "<strong>Wolfe Duality Theorem:</strong> Let $f(x)$ and $g_j(x)$ be convex and continuously differentiable, and $h_i(x)$ be affine.",
            "If $x^*$ is an optimal solution to the primal problem satisfying a constraint qualification, and $(\\lambda^*, \\mu^*)$ are its corresponding KKT multipliers, then:",
            "1. The triple $(x^*, \\lambda^*, \\mu^*)$ is an <strong>optimal solution</strong> to the Wolfe dual problem.",
            "2. The optimal objective values are <strong>strictly equal</strong>: $\\min \\text{Primal} = \\max \\text{Wolfe Dual}$."
        ],
        "math": "$$f, g_j \\text{ convex}, \\; h_i \\text{ affine} \\implies \\max_{(x, \\lambda, \\mu) \\in \\text{Wolfe}} \\mathcal{L}(x, \\lambda, \\mu) = f(x^*) = \\min_{x \\in \\Omega} f(x)$$",
        "personalConnection": "Two mountain climbers ascending and descending along opposite sides of a saddle pass: under convex conditions, the lowest saddle pass seen by the descent climber is the exact highest altitude reachable by the ascent climber.",
        "examTrap": "Remember that if $f$ or $g_j$ is NOT convex, Wolfe duality completely breaks down! Because the stationarity condition $\\nabla_x \\mathcal{L} = 0$ can capture local maxima or inflection points, producing false duality bounds."
    },
    {
        "id": 1703,
        "subject": "CMO",
        "topicId": "17_Wolfe_Duality",
        "topicTitle": "17 · Wolfe Duality",
        "cardNumber": "03",
        "category": "QUADRATIC DUALITY",
        "highlighterClass": "highlight-emerald",
        "title": "Symmetric Dual of Quadratic Programming",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <!-- Primal QP box -->
  <rect x="25" y="30" width="85" height="85" rx="6" fill="#f8fafc" stroke="#000000" stroke-width="1.8"/>
  <text x="67" y="48" fill="#000000" font-size="8.5" font-family="sans-serif" font-weight="bold" text-anchor="middle">PRIMAL QP</text>
  <text x="67" y="66" fill="#000000" font-size="8" font-family="serif" text-anchor="middle">min 1/2 xᵀ Q x + cᵀ x</text>
  <text x="67" y="84" fill="#000000" font-size="8" font-family="serif" text-anchor="middle">s.t. A x ≥ b</text>
  <text x="67" y="100" fill="#000000" font-size="8" font-family="serif" text-anchor="middle">x ≥ 0</text>
  <!-- Duality arrows -->
  <line x1="115" y1="72" x2="130" y2="72" stroke="#000000" stroke-width="2"/>
  <!-- Dual QP box -->
  <rect x="135" y="30" width="85" height="85" rx="6" fill="#f1f5f9" stroke="#000000" stroke-width="1.8"/>
  <text x="177" y="48" fill="#000000" font-size="8.5" font-family="sans-serif" font-weight="bold" text-anchor="middle">WOLFE DUAL QP</text>
  <text x="177" y="66" fill="#000000" font-size="8" font-family="serif" text-anchor="middle">max -1/2 xᵀ Q x + bᵀ y</text>
  <text x="177" y="84" fill="#000000" font-size="8" font-family="serif" text-anchor="middle">s.t. Q x - Aᵀ y + c ≥ 0</text>
  <text x="177" y="100" fill="#000000" font-size="8" font-family="serif" text-anchor="middle">y ≥ 0</text>
  <text x="120" y="136" fill="#000000" font-size="8.5" font-family="sans-serif" text-anchor="middle">Symmetric QP Duality: Quadratic term flips sign to -1/2 xᵀ Q x</text>
</svg>""",
        "drawingCaption": "Symmetric QP Duality: The quadratic objective flips to -1/2 x^T Q x + b^T y under Wolfe duality",
        "coreTranslation": [
            "<strong>Primal Quadratic Program:</strong> Minimize $\\frac{1}{2} x^T Q x + c^T x$ subject to $A x \\ge b, x \\ge 0$ ($Q \\succ 0$).",
            "<strong>Wolfe Dual Formulation:</strong> Construct $\\mathcal{L}(x, y, v) = \\frac{1}{2} x^T Q x + c^T x - y^T (A x - b) - v^T x$ with $y \\ge 0, v \\ge 0$.",
            "Stationarity w.r.t. $x$: $\\nabla_x \\mathcal{L} = Q x + c - A^T y - v = 0 \\implies v = Q x + c - A^T y \\ge 0$.",
            "Substitute into $\\mathcal{L}$: $x^T (Q x + c - A^T y) = 0$ by stationarity, yielding the elegant <strong>Wolfe Dual QP</strong>:",
            "$$\\max_{x, y} \\left\\{ -\\frac{1}{2} x^T Q x + b^T y \\right\\} \\quad \\text{s.t. } Q x - A^T y + c \\ge 0, \\; y \\ge 0$$"
        ],
        "math": "$$\\max_{x, y} \\left\\{ -\\frac{1}{2} x^T Q x + b^T y \\right\\} \\quad \\text{s.t.} \\quad Q x - A^T y + c \\ge \\mathbf{0}, \\; y \\ge \\mathbf{0}$$",
        "personalConnection": "Trading stock positions in a financial exchange: buying long shares ($x$) has positive variance exposure ($\frac{1}{2} x^T Q x$). Short sellers hedging the market ($y$) flip the risk profile ($-\\frac{1}{2} x^T Q x$) while collecting contract premiums ($b^T y$).",
        "examTrap": "Notice that the dual objective has $- \\frac{1}{2} x^T Q x$ (NEGATIVE sign)! Many exam candidates mistakenly write $+\\frac{1}{2} x^T Q x$. The sign flip comes from expanding $x^T Q x + c^T x - y^T A x = \\frac{1}{2} x^T Q x - x^T Q x = -\\frac{1}{2} x^T Q x$."
    },
    {
        "id": 1704,
        "subject": "CMO",
        "topicId": "17_Wolfe_Duality",
        "topicTitle": "17 · Wolfe Duality",
        "cardNumber": "04",
        "category": "COUNTEREXAMPLE TRAPS",
        "highlighterClass": "highlight-rose",
        "title": "Exam Trap: Wolfe Dual Failure on Non-Convex Problems",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <!-- Non-convex double-well curve with local max in middle -->
  <path d="M 35 110 Q 70 25 105 110 Q 140 25 205 110" fill="none" stroke="#000000" stroke-width="2"/>
  <!-- Local maximum where ∇f = 0 but f''(x) < 0 -->
  <circle cx="105" cy="110" r="4" fill="#000000"/>
  <text x="105" y="125" fill="#000000" font-size="8.5" font-family="serif" font-style="italic">Local Min</text>
  <circle cx="140" cy="25" r="4" fill="#000000"/>
  <text x="140" y="15" fill="#000000" font-size="8.5" font-family="serif" font-weight="bold">Local Max (∇f=0!)</text>
  <text x="120" y="45" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Wolfe Dual Trap: Captures False Stationarity Points</text>
  <text x="120" y="138" fill="#000000" font-size="8.5" font-family="sans-serif" text-anchor="middle">When f is non-convex, Wolfe dual maximum can EXCEED primal minimum!</text>
</svg>""",
        "drawingCaption": "Non-Convex Failure: Stationarity ∇_x ℒ = 0 captures local maxima, completely destroying weak and strong duality",
        "coreTranslation": [
            "<strong>The Counterexample Trap:</strong> Consider the unconstrained non-convex problem $\\min f(x) = -x^2$. The minimum over $\\mathbb{R}$ is $-\\infty$.",
            "<strong>Wolfe Dual Formulation:</strong> $\\max_x f(x) = -x^2$ s.t. $f'(x) = -2x = 0$. The only stationary point is $x=0$, giving dual value $f(0) = 0$.",
            "<strong>The Paradox:</strong> Here $\\max \\text{Wolfe Dual} = 0 > -\\infty = \\min \\text{Primal}$! <strong>Weak duality fails completely</strong> ($d^* > p^*$)!",
            "<strong>Why this happens:</strong> $\\nabla_x \\mathcal{L} = 0$ is a necessary condition for a minimum ONLY if $\\mathcal{L}$ is convex. On non-convex problems, it captures local maxima, creating false dual solutions."
        ],
        "math": "$$f(x) = -x^2 \\implies \\min_{x \\in \\mathbb{R}} f(x) = -\\infty, \\quad \\max_{f'(x)=0} f(x) = f(0) = 0 \\implies d^* > p^* \\; (\\text{Fails!})$$",
        "personalConnection": "A metal detector that beeps on both gold nuggets and buried landmines: if you rely on the beep without verifying that you are in a safe zone (convexity), you dig up a disaster.",
        "examTrap": "IISc / Ivy League exams love to present non-convex problems and ask: 'What does the Wolfe dual tell us?' Answer: NOTHING! The Wolfe dual is invalid for non-convex optimization. You must use standard Lagrangian duality instead."
    },
    {
        "id": 1705,
        "subject": "CMO",
        "topicId": "17_Wolfe_Duality",
        "topicTitle": "17 · Wolfe Duality",
        "cardNumber": "05",
        "category": "NON-SMOOTH OPTIMIZATION",
        "highlighterClass": "highlight-violet",
        "title": "The Dual Subgradient Method",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-1705" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- Piecewise linear concave dual function q(μ) with sharp kink -->
  <path d="M 35 110 L 110 40 L 205 115" fill="none" stroke="#000000" stroke-width="2.2"/>
  <circle cx="110" cy="40" r="4" fill="#000000"/>
  <text x="110" y="25" fill="#000000" font-size="9" font-family="serif" font-style="italic" font-weight="bold" text-anchor="middle">μ* (Non-smooth Kink)</text>
  <!-- Subgradient ascent steps -->
  <circle cx="65" cy="82" r="3.5" fill="#000000"/>
  <line x1="65" y1="82" x2="95" y2="55" stroke="#000000" stroke-width="1.8" marker-end="url(#arr-1705)"/>
  <text x="75" y="60" fill="#000000" font-size="8.5" font-family="serif">s_k = g(x(μ_k))</text>
  <text x="120" y="136" fill="#000000" font-size="8.5" font-family="sans-serif" text-anchor="middle">Dual Subgradient Step: μ_{k+1} = max(0, μ_k + α_k g(x(μ_k)))</text>
</svg>""",
        "drawingCaption": "Dual Subgradient Method: Maximizing non-smooth concave dual by stepping along constraint violation vector g(x(μ))",
        "coreTranslation": [
            "<strong>Non-Smoothness of the Dual:</strong> Even when primal functions $f, g$ are smooth, the dual function $q(\\mu) = \\inf_x \\mathcal{L}(x, \\mu)$ often has <strong>sharp kinks (non-differentiable corners)</strong> whenever multiple primal minimizers exist.",
            "<strong>The Subgradient:</strong> For any $\\mu$, let $x(\\mu) = \\arg\\min_x \\mathcal{L}(x, \\mu)$. Then the constraint violation vector $g(x(\\mu))$ is a valid <strong>subgradient</strong> of $q(\\mu)$!",
            "<strong>Dual Subgradient Ascent:</strong> Update multipliers by stepping along the subgradient and projecting onto $\\mathbb{R}_+^m$:",
            "$$\\mu_{k+1} = \\left[ \\mu_k + \\alpha_k g(x(\\mu_k)) \\right]_+$$",
            "With diminishing step sizes $\\sum \\alpha_k = \\infty, \\sum \\alpha_k^2 < \\infty$, the sequence converges to the dual optimum $\\mu^*$."
        ],
        "math": "$$\\mu_{k+1} = \\max\\left( \\mathbf{0}, \\; \\mu_k + \\alpha_k g(x(\\mu_k)) \\right) \\quad \\text{where } x(\\mu_k) = \\arg\\min_{x} \\mathcal{L}(x, \\mu_k)$$",
        "personalConnection": "Adjusting water pipe valves in a city: if district $j$ experiences a water shortage ($g_j > 0$), you raise the water price ($\\mu_{k+1} > \\mu_k$) to penalize waste. If a district has surplus water ($g_j < 0$), you lower the price.",
        "examTrap": "The subgradient method is NOT a descent method! The objective $q(\\mu_k)$ can decrease at individual iterations. You must track the best iterate encountered: $q_{\\text{best}}^{(k)} = \\max_{i=1..k} q(\\mu_i)$."
    },
    {
        "id": 1706,
        "subject": "CMO",
        "topicId": "17_Wolfe_Duality",
        "topicTitle": "17 · Wolfe Duality",
        "cardNumber": "06",
        "category": "WORKED BENCHMARK",
        "highlighterClass": "highlight-indigo",
        "title": "Worked Benchmark: Entropy Maximization Dual",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <!-- Exponential curve of dual unconstrained objective -->
  <path d="M 35 125 Q 110 115 150 70 Q 180 30 205 15" fill="none" stroke="#000000" stroke-width="2"/>
  <text x="180" y="45" fill="#000000" font-size="8.5" font-family="serif">e^{-1 - Aᵀλ}</text>
  <circle cx="120" cy="100" r="4" fill="#000000"/>
  <text x="120" y="88" fill="#000000" font-size="8.5" font-family="serif" font-weight="bold">λ*</text>
  <text x="120" y="20" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Primal: min ∑ x_i ln(x_i)  s.t. A x = b</text>
  <text x="120" y="136" fill="#000000" font-size="8.5" font-family="sans-serif" text-anchor="middle">Dual: max bᵀ λ - ∑ e^{-1 - a_iᵀ λ}  (Unconstrained Smooth Convex Dual!)</text>
</svg>""",
        "drawingCaption": "Worked Dual: Constrained entropy minimization converts into an unconstrained smooth exponential dual problem",
        "coreTranslation": [
            "<strong>Problem:</strong> Minimize negative entropy $f(x) = \\sum_{i=1}^n x_i \\ln x_i$ subject to $A x = b, x > 0$.",
            "<strong>Step 1 (Lagrangian):</strong> $\\mathcal{L}(x, \\lambda) = \\sum_{i=1}^n x_i \\ln x_i + \\lambda^T (b - A x) = \\sum_{i=1}^n x_i \\ln x_i - \\lambda^T A x + b^T \\lambda$.",
            "<strong>Step 2 (Stationarity w.r.t. $x$):</strong> $\\frac{\\partial \\mathcal{L}}{\\partial x_i} = \\ln x_i + 1 - (A^T \\lambda)_i = 0 \\implies \\ln x_i = (A^T \\lambda)_i - 1 \\implies x_i^* = e^{(A^T \\lambda)_i - 1}$.",
            "<strong>Step 3 (Dual Function):</strong> Substitute $x_i^*$ into $\\mathcal{L}$ to eliminate $x$ entirely: $x_i^* \\ln x_i^* - (A^T \\lambda)_i x_i^* = x_i^* [(A^T \\lambda)_i - 1] - (A^T \\lambda)_i x_i^* = -x_i^* = -e^{(A^T \\lambda)_i - 1}$.",
            "The dual problem is <strong>completely unconstrained and smooth</strong>: $\\max_\\lambda \\left\\{ b^T \\lambda - \\sum_{i=1}^n e^{(A^T \\lambda)_i - 1} \\right\\}$!"
        ],
        "math": "$$q(\\lambda) = b^T \\lambda - \\sum_{i=1}^n \\exp\\left( a_i^T \\lambda - 1 \\right) \\implies \\text{Unconstrained Smooth Concave Maximization}$$",
        "personalConnection": "Boltzmann distribution in statistical physics: minimizing thermodynamic free energy subject to conservation of energy produces the famous exponential Maxwell-Boltzmann energy distribution.",
        "examTrap": "Notice that the positivity constraint $x > 0$ is AUTOMATICALLY satisfied by the exponential $x_i^* = e^{\\dots} > 0$! Duality magically eliminates both the non-negativity constraint and the linear equalities."
    }
]

# Write Topic 17 cards
with open('/Users/senso/Projects/photographic-memory-cards/scripts/cmo_topic17.json', 'w') as f:
    json.dump(topic17_cards, f, indent=2)

print(f"Generated {len(topic17_cards)} cards for Topic 17")
