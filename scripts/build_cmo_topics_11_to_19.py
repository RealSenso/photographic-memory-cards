import json

# =============================================================================
# TOPIC 11: Karush-Kuhn-Tucker Conditions: FONC and Sufficiency
# =============================================================================
topic11_cards = [
    {
        "id": 1101,
        "subject": "CMO",
        "topicId": "11_Karush_Kuhn_Tucker_Conditions_FONC_and_Sufficiency",
        "topicTitle": "11 · KKT Conditions & Sufficiency",
        "cardNumber": "01",
        "category": "CONSTRAINED OPTIMALITY",
        "highlighterClass": "highlight-cyan",
        "title": "The Four Karush-Kuhn-Tucker (KKT) Conditions",
        "textbookImg": "assets/luenberger_fig11_8.png",
        "textbookRef": "Luenberger & Ye (4th ed), Sect. 11.8, Fig. 11.8 (p. 356)",
        "drawingCaption": "Luenberger Fig. 11.8: Separating hyperplane for inequalities proving existence of non-negative KKT multipliers",
        "drawingSvg": "",
        "coreTranslation": [
            "<strong>The Problem:</strong> Minimize $f(x)$ subject to equality constraints $h_i(x) = 0$ ($i=1..p$) and inequality constraints $g_j(x) \\le 0$ ($j=1..m$).",
            "<strong>KKT First-Order Necessary Conditions:</strong> If $x^*$ is a local minimizer satisfying a Constraint Qualification (like LICQ), there exist multipliers $\\lambda^* \\in \\mathbb{R}^p$ and $\\mu^* \\in \\mathbb{R}^m$ satisfying the 4 KKT pillars:",
            "<strong>1. Stationarity:</strong> $\\nabla_x \\mathcal{L} = \\nabla f(x^*) + \\sum \\lambda_i^* \\nabla h_i(x^*) + \\sum \\mu_j^* \\nabla g_j(x^*) = 0$. <strong>2. Primal Feasibility:</strong> $h(x^*) = 0, g(x^*) \\le 0$. <strong>3. Dual Feasibility:</strong> $\\mu^* \\ge 0$. <strong>4. Complementary Slackness:</strong> $\\mu_j^* g_j(x^*) = 0$."
        ],
        "math": "$$\\nabla f(x^*) + \\sum_{i=1}^p \\lambda_i^* \\nabla h_i(x^*) + \\sum_{j=1}^m \\mu_j^* \\nabla g_j(x^*) = 0, \\quad \\mu_j^* \\ge 0, \\quad \\mu_j^* g_j(x^*) = 0$$",
        "personalConnection": "Walking your dog on a leash: if the leash is loose ($g(x) < 0$), it exerts zero pulling force ($\mu = 0$). Only when the dog hits the end of the leash ($g(x) = 0$) does tension pull back ($\mu > 0$).",
        "examTrap": "Pay obsessive attention to constraint orientation! If constraints are written $g_j(x) \\le 0$, then $\\mu_j \\ge 0$ with $\\mathcal{L} = f + \\mu^T g$. If written $g_j(x) \\ge 0$, either negate the constraint or write $\\mathcal{L} = f - \\mu^T g$."
    },
    {
        "id": 1102,
        "subject": "CMO",
        "topicId": "11_Karush_Kuhn_Tucker_Conditions_FONC_and_Sufficiency",
        "topicTitle": "11 · KKT Conditions & Sufficiency",
        "cardNumber": "02",
        "category": "COMPLEMENTARY SLACKNESS",
        "highlighterClass": "highlight-amber",
        "title": "Complementary Slackness as an On/Off Switch",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-1102" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- Active state box -->
  <rect x="25" y="25" width="85" height="75" rx="6" fill="#f8fafc" stroke="#000000" stroke-width="1.5"/>
  <text x="67" y="42" fill="#000000" font-size="8.5" font-family="sans-serif" font-weight="bold" text-anchor="middle">ACTIVE BOUNDARY</text>
  <text x="67" y="60" fill="#000000" font-size="9" font-family="serif" font-style="italic" text-anchor="middle">g_j(x*) = 0</text>
  <text x="67" y="75" fill="#000000" font-size="8.5" font-family="serif" text-anchor="middle">⇒ μ_j* ≥ 0</text>
  <text x="67" y="90" fill="#000000" font-size="7.5" font-family="sans-serif" text-anchor="middle">(Wall pushes back)</text>
  <!-- Inactive state box -->
  <rect x="130" y="25" width="85" height="75" rx="6" fill="#f1f5f9" stroke="#000000" stroke-width="1.5"/>
  <text x="172" y="42" fill="#000000" font-size="8.5" font-family="sans-serif" font-weight="bold" text-anchor="middle">STRICT INTERIOR</text>
  <text x="172" y="60" fill="#000000" font-size="9" font-family="serif" font-style="italic" text-anchor="middle">g_j(x*) &lt; 0</text>
  <text x="172" y="75" fill="#000000" font-size="8.5" font-family="serif" text-anchor="middle">⇒ μ_j* = 0</text>
  <text x="172" y="90" fill="#000000" font-size="7.5" font-family="sans-serif" text-anchor="middle">(Wall does nothing)</text>
  <text x="120" y="122" fill="#000000" font-size="9.5" font-family="serif" font-style="italic" font-weight="bold" text-anchor="middle">μ_j* · g_j(x*) = 0  (At least one must be zero)</text>
  <text x="120" y="136" fill="#000000" font-size="8.5" font-family="sans-serif" text-anchor="middle">Strict Complementarity: exactly one is strictly zero</text>
</svg>""",
        "drawingCaption": "Complementary Slackness: Either the constraint is active (g=0, μ≥0) or it is inactive (g<0, μ=0)",
        "coreTranslation": [
            "<strong>The Product Condition:</strong> $\\mu_j^* g_j(x^*) = 0$ means that for each inequality constraint $j$, the product of the multiplier and constraint value is zero.",
            "<strong>Case 1 ($g_j(x^*) < 0$, Inactive):</strong> The candidate point lies strictly inside the feasible set. The boundary does not obstruct the minimizer, so its multiplier MUST vanish: $\\mu_j^* = 0$.",
            "<strong>Case 2 ($\\mu_j^* > 0$, Active):</strong> The constraint exerts a positive normal force against $-\\nabla f(x^*)$. This requires the point to lie right on the boundary: $g_j(x^*) = 0$."
        ],
        "math": "$$\\mu_j^* g_j(x^*) = 0 \\iff \\begin{cases} g_j(x^*) < 0 \\implies \\mu_j^* = 0 \\\\ \\mu_j^* > 0 \\implies g_j(x^*) = 0 \\end{cases}$$",
        "personalConnection": "A car parked inside a garage: if the front bumper doesn't touch the back wall ($g < 0$), the wall exerts zero normal force ($\mu = 0$). If you bump into the wall ($g = 0$), the wall pushes back ($\mu > 0$).",
        "examTrap": "Can BOTH $g_j(x^*) = 0$ and $\\mu_j^* = 0$? YES! This is called <strong>weak complementarity</strong> (or degeneracy). It often causes non-isolated Lagrange multipliers and numerical difficulties."
    },
    {
        "id": 1103,
        "subject": "CMO",
        "topicId": "11_Karush_Kuhn_Tucker_Conditions_FONC_and_Sufficiency",
        "topicTitle": "11 · KKT Conditions & Sufficiency",
        "cardNumber": "03",
        "category": "CONVEX SUFFICIENCY",
        "highlighterClass": "highlight-emerald",
        "title": "KKT Convex Sufficiency Theorem",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <!-- Convex bowl objective f(x) -->
  <path d="M 35 35 Q 120 120 205 35" fill="none" stroke="#000000" stroke-width="2"/>
  <text x="210" y="40" fill="#000000" font-size="9" font-family="serif" font-style="italic">f(x)</text>
  <!-- Feasible convex set interval [a, b] -->
  <line x1="80" y1="110" x2="190" y2="110" stroke="#000000" stroke-width="3"/>
  <circle cx="80" cy="110" r="3.5" fill="#000000"/>
  <circle cx="190" cy="110" r="3.5" fill="#000000"/>
  <text x="80" y="125" fill="#000000" font-size="8.5" font-family="serif">a</text>
  <text x="190" y="125" fill="#000000" font-size="8.5" font-family="serif">b</text>
  <!-- KKT minimum at x* -->
  <circle cx="120" cy="77" r="4" fill="#000000"/>
  <text x="120" y="70" fill="#000000" font-size="9" font-family="serif" font-style="italic" font-weight="bold" text-anchor="middle">x* (Global Min)</text>
  <text x="120" y="18" fill="#000000" font-size="8.5" font-family="sans-serif" font-weight="bold" text-anchor="middle">Convex f, Convex g_j, Affine h_i ⇒ KKT is SUFFICIENT</text>
  <text x="120" y="138" fill="#000000" font-size="8" font-family="serif" font-style="italic" text-anchor="middle">f(x*) ≤ ℒ(x*, λ*, μ*) ≤ ℒ(x, λ*, μ*) ≤ f(x)</text>
</svg>""",
        "drawingCaption": "Convex Sufficiency: For convex f, convex g, and affine h, any KKT stationary point is a global minimizer",
        "coreTranslation": [
            "<strong>Master Sufficiency Theorem:</strong> Suppose $f(x)$ and all inequality constraints $g_j(x)$ are convex functions, and all equality constraints $h_i(x) = a_i^T x - b_i$ are affine.",
            "If $(x^*, \\lambda^*, \\mu^*)$ satisfies the 4 KKT conditions, then $x^*$ is an <strong>absolute global minimizer</strong> of the constrained optimization problem!",
            "<strong>Proof:</strong> Since $\\mu_j^* \\ge 0$, $\\mathcal{L}(x, \\lambda^*, \\mu^*)$ is convex in $x$. Stationarity $\\nabla_x \\mathcal{L} = 0$ makes $x^*$ a global minimizer of $\\mathcal{L}$. Complementary slackness then sandwiches $f(x^*) \\le \\mathcal{L}(x^*, \\lambda^*, \\mu^*) \\le \\mathcal{L}(x, \\lambda^*, \\mu^*) \\le f(x)$."
        ],
        "math": "$$f, g_j \\text{ convex}, \\, h_i \\text{ affine}, \\, (x^*, \\lambda^*, \\mu^*) \\in \\text{KKT} \\implies f(x^*) \\le f(x) \\; \\forall \\, x \\in \\Omega$$",
        "personalConnection": "Water pooling in a convex salad bowl with sliced flat bread boundaries: there is only one lowest point, and if the water settles in a stationary equilibrium, it is impossible for a deeper puddle to exist elsewhere.",
        "examTrap": "Equality constraints $h_i(x) = 0$ MUST be AFFINE ($A x = b$)! If an equality constraint is non-linear (even if $h_i$ is convex), the feasible set $\\{x : h_i(x) = 0\\}$ is NOT convex, and KKT sufficiency fails."
    },
    {
        "id": 1104,
        "subject": "CMO",
        "topicId": "11_Karush_Kuhn_Tucker_Conditions_FONC_and_Sufficiency",
        "topicTitle": "11 · KKT Conditions & Sufficiency",
        "cardNumber": "04",
        "category": "CONSTRAINT QUALIFICATIONS",
        "highlighterClass": "highlight-violet",
        "title": "LICQ & Why Regularity is Essential",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-1104" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- Degenerate cusp x_2^2 ≤ x_1^3 at origin -->
  <path d="M 120 75 Q 160 55 210 25" fill="none" stroke="#000000" stroke-width="2"/>
  <path d="M 120 75 Q 160 95 210 125" fill="none" stroke="#000000" stroke-width="2"/>
  <circle cx="120" cy="75" r="4" fill="#000000"/>
  <text x="105" y="78" fill="#000000" font-size="9" font-family="serif" font-style="italic">x* = 0</text>
  <!-- Gradient arrow is zero at cusp -->
  <line x1="120" y1="75" x2="60" y2="75" stroke="#000000" stroke-width="2" marker-end="url(#arr-1104)"/>
  <text x="50" y="78" fill="#000000" font-size="8.5" font-family="serif" font-style="italic">-∇f</text>
  <text x="120" y="20" fill="#000000" font-size="8.5" font-family="sans-serif" font-weight="bold" text-anchor="middle">LICQ Failure: Active gradients are linearly dependent</text>
  <text x="120" y="135" fill="#000000" font-size="8" font-family="sans-serif" text-anchor="middle">Without LICQ, KKT multipliers may NOT exist at a true local minimum!</text>
</svg>""",
        "drawingCaption": "LICQ Failure: At a non-smooth cusp or tangent tangency, constraint gradients vanish or align, failing KKT",
        "coreTranslation": [
            "<strong>Linear Independence Constraint Qualification (LICQ):</strong> The gradients of all active constraints $\\{\\nabla h_i(x^*)\\}_{i=1}^p \\cup \\{\\nabla g_j(x^*)\\}_{j \\in \\mathcal{A}(x^*)}$ must be <strong>linearly independent vectors</strong> in $\\mathbb{R}^n$.",
            "<strong>The Danger:</strong> KKT conditions are NOT guaranteed to hold at a local minimum if LICQ (or another CQ like MFCQ or Slater) fails!",
            "<strong>Classic Counterexample:</strong> $\\min x_1$ s.t. $(1-x_1)^3 - x_2 \\ge 0, x_2 \\ge 0$. At $x^* = (1, 0)$, both active gradients point along $(0, 1)^T$. They are collinear (linearly dependent). $-\\nabla f = (-1, 0)^T$ cannot be spanned by $(0, 1)^T$, so NO KKT multipliers exist!"
        ],
        "math": "$$\\operatorname{rank}\\left( [\\nabla h_i(x^*)_{i=1}^p, \\; \\nabla g_j(x^*)_{j \\in \\mathcal{A}(x^*)}] \\right) = p + |\\mathcal{A}(x^*)| \\quad (\\text{LICQ})$$",
        "personalConnection": "Two laser beams intersecting: if the beams cross at an angle, they define a unique 3D point (LICQ holds). If both laser beams point in the identical direction, they don't form a coordinate cross, and you lose spatial stability.",
        "examTrap": "Never apply KKT necessary conditions without stating that LICQ holds! If an exam question asks 'Does $x^*$ satisfy KKT?', first test if the active constraint gradients are linearly independent."
    },
    {
        "id": 1105,
        "subject": "CMO",
        "topicId": "11_Karush_Kuhn_Tucker_Conditions_FONC_and_Sufficiency",
        "topicTitle": "11 · KKT Conditions & Sufficiency",
        "cardNumber": "05",
        "category": "CONSTRAINT QUALIFICATIONS",
        "highlighterClass": "highlight-indigo",
        "title": "Slater’s Condition for Convex Programs",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <!-- Convex region C with strictly interior point x_rel -->
  <ellipse cx="120" cy="75" rx="75" ry="45" fill="#f8fafc" stroke="#000000" stroke-width="2"/>
  <circle cx="105" cy="65" r="4" fill="#000000"/>
  <text x="105" y="55" fill="#000000" font-size="9" font-family="serif" font-style="italic" font-weight="bold" text-anchor="middle">x̂ (Strictly Feasible)</text>
  <text x="105" y="80" fill="#000000" font-size="8.5" font-family="serif" font-style="italic" text-anchor="middle">g_j(x̂) &lt; 0  ∀ j</text>
  <text x="120" y="18" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Slater’s Condition (Boyd Sect. 5.2.3)</text>
  <text x="120" y="135" fill="#000000" font-size="8.5" font-family="sans-serif" text-anchor="middle">Strict interior point guarantees Strong Duality: d* = p*</text>
</svg>""",
        "drawingCaption": "Slater's Condition: Existence of a strictly interior point x̂ with g_j(x̂) < 0 guarantees strong duality",
        "coreTranslation": [
            "<strong>Slater's Constraint Qualification:</strong> For a convex optimization problem $\\min f(x)$ s.t. $g_j(x) \\le 0, A x = b$, Slater's condition holds if there exists at least one point $\\hat{x} \\in \\operatorname{relint}(\\mathcal{D})$ such that:",
            "$$g_j(\\hat{x}) < 0 \\quad \\forall \\, j = 1, \\dots, m, \\quad \\text{and} \\quad A \\hat{x} = b$$",
            "<strong>Fundamental Implication:</strong> If the primal problem is convex and Slater's condition holds, then <strong>Strong Duality holds ($d^* = p^*$)</strong>, the dual optimal value is attained, and KKT multipliers are guaranteed to exist!"
        ],
        "math": "$$\\exists \\, \\hat{x} : g_j(\\hat{x}) < 0 \\; (j=1..m), \\; A \\hat{x} = b \\implies d^* = p^* \\quad (\\text{Strong Duality})$$",
        "personalConnection": "A fenced backyard with actual room to play: Slater's condition means the yard is not squeezed into a zero-width fence line ($g < 0$ has interior volume). You have breathing room inside the fence.",
        "examTrap": "Slater requires STRICT inequality $g_j(\\hat{x}) < 0$ only for NON-AFFINE convex constraints. For purely affine inequality constraints ($c_j^T x \\le d_j$), simple feasibility without strict inequality is sufficient!"
    },
    {
        "id": 1106,
        "subject": "CMO",
        "topicId": "11_Karush_Kuhn_Tucker_Conditions_FONC_and_Sufficiency",
        "topicTitle": "11 · KKT Conditions & Sufficiency",
        "cardNumber": "06",
        "category": "WORKED BENCHMARK",
        "highlighterClass": "highlight-rose",
        "title": "Worked Benchmark: KKT Active Set Case Analysis",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-1106" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- Constraint line x₁ + x₂ = 1 -->
  <line x1="40" y1="30" x2="190" y2="120" stroke="#000000" stroke-width="2"/>
  <text x="195" y="125" fill="#000000" font-size="8.5" font-family="serif" font-style="italic">x₁ + x₂ = 1</text>
  <!-- Elliptical contour of f(x) = x₁² + 4x₂² -->
  <ellipse cx="120" cy="75" rx="50" ry="25" fill="none" stroke="#000000" stroke-width="1.5" stroke-dasharray="3,3"/>
  <circle cx="100" cy="65" r="4" fill="#000000"/>
  <text x="100" y="55" fill="#000000" font-size="9" font-family="serif" font-style="italic" font-weight="bold">x* = (4/5, 1/5)</text>
  <!-- Multiplier normal vector -->
  <line x1="100" y1="65" x2="60" y2="35" stroke="#000000" stroke-width="1.8" marker-end="url(#arr-1106)"/>
  <text x="45" y="32" fill="#000000" font-size="8.5" font-family="serif" font-style="italic">μ ∇g</text>
  <text x="120" y="138" fill="#000000" font-size="8.5" font-family="sans-serif" text-anchor="middle">Case 2 Active: μ = 8/5 &gt; 0 confirms constrained minimum</text>
</svg>""",
        "drawingCaption": "Worked KKT Solution: Systematic test of inactive case (fails feasibility) and active case (yields unique μ* > 0)",
        "coreTranslation": [
            "<strong>Problem:</strong> Minimize $f(x) = x_1^2 + 4 x_2^2$ subject to $g(x) = 1 - x_1 - x_2 \\le 0$.",
            "<strong>Case 1 (Inactive, $\\mu = 0$):</strong> $\\nabla f(x) = [2 x_1, 8 x_2]^T = [0, 0]^T \\implies x = (0, 0)$. Check feasibility: $g(0, 0) = 1 > 0$ $\\implies$ <strong>INFEASIBLE!</strong> Reject Case 1.",
            "<strong>Case 2 (Active, $g(x) = 0$):</strong> $x_1 + x_2 = 1$. Stationarity: $2 x_1 - \\mu = 0$ and $8 x_2 - \\mu = 0 \\implies x_1 = \\mu/2, x_2 = \\mu/8$. Substitute: $\\frac{\\mu}{2} + \\frac{\\mu}{8} = 1 \\implies \\frac{5\\mu}{8} = 1 \\implies \\mu^* = 8/5 > 0$. Point $x^* = (4/5, 1/5)$. Both dual feasibility and complementary slackness hold!"
        ],
        "math": "$$\\nabla f(x^*) + \\mu^* \\nabla g(x^*) = \\begin{bmatrix} 2 x_1 \\\\ 8 x_2 \\end{bmatrix} + \\mu^* \\begin{bmatrix} -1 \\\\ -1 \\end{bmatrix} = \\mathbf{0} \\implies x^* = \\left(\\frac{4}{5}, \\frac{1}{5}\\right), \\; \\mu^* = \\frac{8}{5} > 0$$",
        "personalConnection": "Checking light switches: if turning the switch OFF leaves you in the dark (Case 1 infeasible), flip it ON and measure the exact current flow (Case 2 $\mu = 8/5$).",
        "examTrap": "When solving KKT by cases, NEVER stop upon finding a solution! You must verify dual feasibility ($\\mu_j \\ge 0$) and check if any other active sets could also satisfy KKT."
    }
]

# Write Topic 11 cards
with open('/Users/senso/Projects/photographic-memory-cards/scripts/cmo_topic11.json', 'w') as f:
    json.dump(topic11_cards, f, indent=2)

print(f"Generated {len(topic11_cards)} cards for Topic 11")
