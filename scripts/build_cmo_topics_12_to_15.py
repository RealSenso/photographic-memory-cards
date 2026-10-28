import json

# =============================================================================
# TOPIC 12: Second-Order Optimality Conditions in Constrained Optimization
# =============================================================================
topic12_cards = [
    {
        "id": 1201,
        "subject": "CMO",
        "topicId": "12_Second_Order_Optimality_Conditions_in_Constrained_Optimization",
        "topicTitle": "12 · Second-Order Constrained Conditions",
        "cardNumber": "01",
        "category": "SECOND-ORDER NECESSARY CONDITIONS",
        "highlighterClass": "highlight-cyan",
        "title": "SONC: Curvature on the Tangent Subspace M",
        "textbookImg": "assets/luenberger_fig11_4.png",
        "textbookRef": "Luenberger & Ye (4th ed), Sect. 11.5, Fig. 11.4 (p. 336)",
        "drawingCaption": "Luenberger Fig. 11.4: Hessian L acting on vector y projected orthogonally back onto tangent subspace M as L_M y",
        "drawingSvg": "",
        "coreTranslation": [
            "<strong>Second-Order Necessary Condition (SONC):</strong> Let $x^*$ be a regular local minimizer of $f$ subject to $h(x) = 0$ and $g(x) \\le 0$, with multipliers $\\lambda^*, \\mu^*$.",
            "Then the Hessian of the Lagrangian with respect to $x$, denoted $\\nabla_{xx}^2 \\mathcal{L}(x^*, \\lambda^*, \\mu^*)$, must be <strong>Positive Semidefinite on the Tangent Subspace $M$</strong>:",
            "$$d^T \\nabla_{xx}^2 \\mathcal{L}(x^*, \\lambda^*, \\mu^*) d \\ge 0 \\quad \\forall \\, d \\in M(x^*)$$, where $M(x^*) = \\{d : \\nabla h_i(x^*)^T d = 0, \\; \\nabla g_j(x^*)^T d = 0 \\; (j \\in \\mathcal{A}(x^*))\\}$."
        ],
        "math": "$$d^T \\nabla_{xx}^2 \\mathcal{L}(x^*, \\lambda^*, \\mu^*) d \\ge 0 \\quad \\forall \\, d \\in M(x^*) = \\operatorname{Null}\\left( [\\nabla h(x^*)^T ; \\nabla g_{\\mathcal{A}}(x^*)^T] \\right)$$",
        "personalConnection": "Walking along a knife-edge ridge on a mountain summit: the terrain plunges steeply on both sides (negative curvature in ambient 3D space), but as long as the trail itself remains level or curves upward, you stay safe at a constrained minimum.",
        "examTrap": "The ambient Hessian $\\nabla^2 f(x^*)$ or even $\\nabla_{xx}^2 \\mathcal{L}$ DOES NOT need to be positive semidefinite everywhere! It only needs to be positive semidefinite when tested against vectors $d$ lying in the tangent subspace $M$."
    },
    {
        "id": 1202,
        "subject": "CMO",
        "topicId": "12_Second_Order_Optimality_Conditions_in_Constrained_Optimization",
        "topicTitle": "12 · Second-Order Constrained Conditions",
        "cardNumber": "02",
        "category": "SECOND-ORDER SUFFICIENCY",
        "highlighterClass": "highlight-amber",
        "title": "SOSC: Strict Positivity on the Critical Cone",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-1202" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- Tangent line M -->
  <line x1="30" y1="110" x2="210" y2="110" stroke="#000000" stroke-width="1.8"/>
  <text x="215" y="113" fill="#000000" font-size="9" font-family="serif" font-style="italic">M</text>
  <!-- Upward parabola along M -->
  <path d="M 60 40 Q 120 110 180 40" fill="none" stroke="#000000" stroke-width="2.2"/>
  <circle cx="120" cy="110" r="4" fill="#000000"/>
  <text x="120" y="125" fill="#000000" font-size="9" font-family="serif" font-style="italic" font-weight="bold" text-anchor="middle">x* (Strict Local Min)</text>
  <text x="120" y="25" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">d^T ∇²_xx ℒ(x*) d &gt; 0  ∀ d ∈ M \ {0}</text>
  <text x="120" y="138" fill="#000000" font-size="8.5" font-family="sans-serif" text-anchor="middle">Strict positivity on tangent subspace guarantees isolated minimizer</text>
</svg>""",
        "drawingCaption": "SOSC: Strict positive curvature along the tangent subspace M guarantees an isolated local minimizer",
        "coreTranslation": [
            "<strong>Second-Order Sufficient Condition (SOSC):</strong> Suppose $(x^*, \\lambda^*, \\mu^*)$ satisfies KKT. If for all non-zero vectors $d \\in M(x^*)$ ($d \\ne 0$):",
            "$$d^T \\nabla_{xx}^2 \\mathcal{L}(x^*, \\lambda^*, \\mu^*) d > 0$$, then $x^*$ is a <strong>strict, isolated local minimizer</strong> of the constrained problem.",
            "<strong>Why SOSC is Powerful:</strong> Unlike the first-order KKT conditions (which could pick up local maxima or saddles), SOSC eliminates all doubt by guaranteeing positive quadratic bowl curvature along every feasible escape route."
        ],
        "math": "$$d^T \\nabla_{xx}^2 \\mathcal{L}(x^*, \\lambda^*, \\mu^*) d > 0 \\quad \\forall \\, d \\in M(x^*) \\setminus \\{0\\} \\implies x^* \\text{ is a strict local minimizer}$$",
        "personalConnection": "A marble trapped at the bottom of a curved rain gutter: the roof may slope downward in 3D, but the gutter itself curves strictly upward in both directions along its length, holding the marble securely in place.",
        "examTrap": "Semidefiniteness ($d^T \\nabla_{xx}^2 \\mathcal{L} d \\ge 0$) is NECESSARY, NOT sufficient! Strict inequality ($> 0$) is mandatory for sufficiency, exactly like $f''(x) > 0$ in single-variable calculus."
    },
    {
        "id": 1203,
        "subject": "CMO",
        "topicId": "12_Second_Order_Optimality_Conditions_in_Constrained_Optimization",
        "topicTitle": "12 · Second-Order Constrained Conditions",
        "cardNumber": "03",
        "category": "MATRIX ALGEBRA",
        "highlighterClass": "highlight-emerald",
        "title": "The Bordered Hessian Matrix Test",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <!-- Bordered Hessian Matrix Bracket -->
  <rect x="45" y="25" width="150" height="90" rx="4" fill="#f8fafc" stroke="#000000" stroke-width="1.8"/>
  <line x1="95" y1="25" x2="95" y2="115" stroke="#000000" stroke-width="1.2" stroke-dasharray="3,3"/>
  <line x1="45" y1="65" x2="195" y2="65" stroke="#000000" stroke-width="1.2" stroke-dasharray="3,3"/>
  <!-- Block labels -->
  <text x="70" y="50" fill="#000000" font-size="11" font-family="serif" font-weight="bold" text-anchor="middle">0</text>
  <text x="145" y="50" fill="#000000" font-size="10" font-family="serif" font-weight="bold" text-anchor="middle">∇h(x*)ᵀ</text>
  <text x="70" y="95" fill="#000000" font-size="10" font-family="serif" font-weight="bold" text-anchor="middle">∇h(x*)</text>
  <text x="145" y="95" fill="#000000" font-size="10" font-family="serif" font-weight="bold" text-anchor="middle">∇²_xx ℒ</text>
  <text x="120" y="132" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Sign Alternation: sign(det B_k) = (-1)^p  (for k &gt; 2p)</text>
</svg>""",
        "drawingCaption": "Bordered Hessian: Block matrix pairing zero block, constraint Jacobian, and Lagrangian Hessian",
        "coreTranslation": [
            "To test positive definiteness of $\\nabla_{xx}^2 \\mathcal{L}$ on nullspace $M = \\{d : A d = 0\\}$ without explicitly computing nullspace bases, construct the <strong>Bordered Hessian Matrix</strong>:",
            "$$B = \\begin{bmatrix} 0 & A \\\\ A^T & L \\end{bmatrix}, \\quad \\text{where } A = \\nabla h(x^*)^T \\in \\mathbb{R}^{p \\times n}, \\; L = \\nabla_{xx}^2 \\mathcal{L} \\in \\mathbb{R}^{n \\times n}$$",
            "<strong>Determinant Test:</strong> $L$ is positive definite on $M$ if and only if the last $n - p$ leading principal minors of $B$ have the <strong>same sign</strong>, given by $(-1)^p$."
        ],
        "math": "$$\\operatorname{sign}(\\det B_{2p+m}) = (-1)^p \\quad (\\forall \\, m = 1, \\dots, n-p)$$",
        "personalConnection": "Balancing a chandelier on a gimbal: the bordered Hessian computes whether the pendulum hangs stably downward (positive definite) by checking the orientation of its hinge constraints.",
        "examTrap": "For a single equality constraint ($p=1$), $(-1)^1 = -1$, meaning the determinant of the bordered Hessian MUST BE NEGATIVE ($\\det B < 0$) for a local minimum! Students routinely confuse this with unconstrained positive definiteness."
    },
    {
        "id": 1204,
        "subject": "CMO",
        "topicId": "12_Second_Order_Optimality_Conditions_in_Constrained_Optimization",
        "topicTitle": "12 · Second-Order Constrained Conditions",
        "cardNumber": "04",
        "category": "CONE GEOMETRY",
        "highlighterClass": "highlight-violet",
        "title": "Strict Complementarity & The Critical Cone",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-1204" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- Critical Cone Sector -->
  <polygon points="120,85 195,35 195,115" fill="#f1f5f9" stroke="#000000" stroke-width="1.8"/>
  <circle cx="120" cy="85" r="4" fill="#000000"/>
  <text x="110" y="90" fill="#000000" font-size="9" font-family="serif" font-style="italic">x*</text>
  <text x="170" y="75" fill="#000000" font-size="9.5" font-family="serif" font-style="italic" font-weight="bold">C(x*, μ*)</text>
  <!-- μ > 0 plane line -->
  <line x1="120" y1="85" x2="195" y2="35" stroke="#000000" stroke-width="2.5"/>
  <text x="160" y="30" fill="#000000" font-size="8" font-family="serif">∇g_jᵀ d = 0 (μ_j &gt; 0)</text>
  <!-- μ = 0 boundary -->
  <line x1="120" y1="85" x2="195" y2="115" stroke="#000000" stroke-width="1.2" stroke-dasharray="3,3"/>
  <text x="160" y="130" fill="#000000" font-size="8" font-family="serif">∇g_jᵀ d ≤ 0 (μ_j = 0)</text>
  <text x="120" y="18" fill="#000000" font-size="8.5" font-family="sans-serif" font-weight="bold" text-anchor="middle">Critical Cone: Directions where first-order descent is zero</text>
</svg>""",
        "drawingCaption": "Critical Cone: Directions where gradient vanishes, requiring second-order curvature testing",
        "coreTranslation": [
            "When inequality constraints are present, the tangent subspace generalises to the <strong>Critical Cone $C(x^*, \\mu^*)$</strong>:",
            "$$C(x^*, \\mu^*) = \\left\\{ d \\in \\mathbb{R}^n : \\begin{array}{ll} \\nabla h_i(x^*)^T d = 0 & \\forall i \\\\ \\nabla g_j(x^*)^T d = 0 & \\text{if } \\mu_j^* > 0 \\\\ \\nabla g_j(x^*)^T d \\le 0 & \\text{if } \\mu_j^* = 0, \\; j \\in \\mathcal{A}(x^*) \\end{array} \\right\\}$$",
            "<strong>Strict Complementarity:</strong> If $\\mu_j^* > 0$ for ALL active constraints ($j \\in \\mathcal{A}(x^*)$), the inequality conditions vanish and $C(x^*, \\mu^*)$ collapses into a <strong>pure linear subspace</strong>, making second-order checks vastly simpler!"
        ],
        "math": "$$\\text{Strict Complementarity } (\\mu_j^* > 0 \\; \\forall j \\in \\mathcal{A}) \\implies C(x^*, \\mu^*) = \\operatorname{Null}([\\nabla h(x^*)^T ; \\nabla g_{\\mathcal{A}}(x^*)^T])$$",
        "personalConnection": "A car wedged tightly into a parallel parking spot: if both front and back bumpers press against the cars ahead and behind ($\mu_1, \mu_2 > 0$), you have 0 degrees of freedom (linear subspace of motion is zero).",
        "examTrap": "If strict complementarity fails (i.e. an active constraint has $\\mu_j^* = 0$), $C(x^*)$ is a CONE, not a subspace! You must check $d^T \\nabla^2 \\mathcal{L} d > 0$ over the full cone, not just a subspace."
    },
    {
        "id": 1205,
        "subject": "CMO",
        "topicId": "12_Second_Order_Optimality_Conditions_in_Constrained_Optimization",
        "topicTitle": "12 · Second-Order Constrained Conditions",
        "cardNumber": "05",
        "category": "GEOMETRIC INTUITION",
        "highlighterClass": "highlight-indigo",
        "title": "Manifold Curvature vs. Ambient Space",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <!-- Saddle Surface with constraint circle -->
  <ellipse cx="120" cy="75" rx="75" ry="35" fill="#f8fafc" stroke="#000000" stroke-width="1.8"/>
  <!-- Tangent trajectory showing local minimum on constraint -->
  <path d="M 65 75 Q 120 100 175 75" fill="none" stroke="#000000" stroke-width="2.5"/>
  <circle cx="120" cy="87" r="4" fill="#000000"/>
  <text x="120" y="103" fill="#000000" font-size="8.5" font-family="serif" font-style="italic" font-weight="bold" text-anchor="middle">x* (Min on S, Saddle in ℝ³)</text>
  <text x="120" y="22" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Why Lagrangian Hessian ∇²_xx ℒ Includes ∑ λ_i ∇²h_i</text>
  <text x="120" y="136" fill="#000000" font-size="8.5" font-family="sans-serif" text-anchor="middle">Constraint surface curvature bends the space under the objective</text>
</svg>""",
        "drawingCaption": "Manifold Curvature: The second derivative of the constraint λ ∇²h compensates for the curved surface",
        "coreTranslation": [
            "Why does the second-order condition use the Hessian of the <strong>Lagrangian</strong> $\\nabla_{xx}^2 \\mathcal{L} = \\nabla^2 f + \\sum \\lambda_i \\nabla^2 h_i$, rather than just $\\nabla^2 f$?",
            "<strong>Surface Curvature:</strong> As a point moves along a curved constraint surface $h(x) = 0$, the surface itself bends! The term $\\sum \\lambda_i \\nabla^2 h_i(x^*)$ accounts for the <strong>normal acceleration</strong> of curves constrained to the surface.",
            "<strong>Key Insight:</strong> Even if $\\nabla^2 f$ is flat or negative in the ambient space, strong curvature of the constraint surface $h(x)=0$ can make the restricted objective strictly convex!"
        ],
        "math": "$$\\frac{d^2}{dt^2} f(x(t))\\Big|_{t=0} = \\dot{x}(0)^T \\nabla^2 f(x^*) \\dot{x}(0) + \\nabla f(x^*)^T \\ddot{x}(0) = d^T \\left[ \\nabla^2 f(x^*) + \\sum_{i=1}^p \\lambda_i^* \\nabla^2 h_i(x^*) \\right] d$$",
        "personalConnection": "Riding a bobsled on a steeply banked track: the curvature of the ice wall creates a centrifugal normal force that keeps you securely at the bottom of the curve, even when horizontal gravity tries to pull you away.",
        "examTrap": "Forgetting the $\\lambda_i \\nabla^2 h_i$ term! If you only evaluate $d^T \\nabla^2 f(x^*) d$, you are implicitly assuming the constraints are FLAT linear planes. For non-linear constraints, this yields completely wrong answers."
    },
    {
        "id": 1206,
        "subject": "CMO",
        "topicId": "12_Second_Order_Optimality_Conditions_in_Constrained_Optimization",
        "topicTitle": "12 · Second-Order Constrained Conditions",
        "cardNumber": "06",
        "category": "WORKED BENCHMARK",
        "highlighterClass": "highlight-rose",
        "title": "Worked Benchmark: Bordered Hessian Sign Test",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <!-- Unit circle constraint and linear objective contours -->
  <circle cx="120" cy="75" r="40" fill="none" stroke="#000000" stroke-width="1.8"/>
  <text x="175" y="75" fill="#000000" font-size="8.5" font-family="serif" font-style="italic">x₁² + x₂² = 1</text>
  <!-- Tangent line at minimizer (-1/√2, -1/√2) -->
  <line x1="60" y1="125" x2="115" y2="70" stroke="#000000" stroke-width="1.5" stroke-dasharray="3,3"/>
  <circle cx="92" cy="103" r="4" fill="#000000"/>
  <text x="75" y="100" fill="#000000" font-size="8.5" font-family="serif" font-style="italic" font-weight="bold">x*</text>
  <text x="120" y="20" fill="#000000" font-size="8.5" font-family="sans-serif" font-weight="bold" text-anchor="middle">det(B) = -4√2 &lt; 0 ⇒ Strict Local Minimum Verified!</text>
  <text x="120" y="138" fill="#000000" font-size="8.5" font-family="sans-serif" text-anchor="middle">Worked verification for min x₁ + x₂ s.t. x₁² + x₂² = 1</text>
</svg>""",
        "drawingCaption": "Worked Verification: Bordered Hessian determinant is negative (-4√2 < 0), verifying local minimum",
        "coreTranslation": [
            "<strong>Problem:</strong> Minimize $f(x) = x_1 + x_2$ subject to $h(x) = x_1^2 + x_2^2 - 1 = 0$.",
            "<strong>FONC Solution:</strong> $\\nabla \\mathcal{L} = [1 + 2\\lambda x_1, 1 + 2\\lambda x_2]^T = 0 \\implies x_1 = x_2 = -1/(2\\lambda)$. Using $x_1^2 + x_2^2 = 1$ gives $x^* = (-1/\\sqrt{2}, -1/\\sqrt{2})$ with $\\lambda^* = 1/\\sqrt{2}$.",
            "<strong>Second-Order Bordered Hessian:</strong> $\\nabla h = [-\\sqrt{2}, -\\sqrt{2}]^T$, $\\nabla_{xx}^2 \\mathcal{L} = 2\\lambda^* I = \\sqrt{2} I$. The $3 \\times 3$ Bordered Hessian is:",
            "$$B = \\begin{bmatrix} 0 & -\\sqrt{2} & -\\sqrt{2} \\\\ -\\sqrt{2} & \\sqrt{2} & 0 \\\\ -\\sqrt{2} & 0 & \\sqrt{2} \\end{bmatrix} \\implies \\det B = -4\\sqrt{2} < 0$$. Since $p=1$, $(-1)^1 = -1$, confirming a <strong>strict local minimum</strong>!"
        ],
        "math": "$$\\det B = \\det \\begin{bmatrix} 0 & -\\sqrt{2} & -\\sqrt{2} \\\\ -\\sqrt{2} & \\sqrt{2} & 0 \\\\ -\\sqrt{2} & 0 & \\sqrt{2} \\end{bmatrix} = -4\\sqrt{2} < 0 = (-1)^1 \\implies x^* \\text{ is a strict local min}$$",
        "personalConnection": "Walking south-west on a circular racetrack: the furthest point south-west is $(-1/\\sqrt{2}, -1/\\sqrt{2})$. Any step along the circular track carries you to higher elevations ($x_1 + x_2 > -\\sqrt{2}$).",
        "examTrap": "If you tested the maximum at $(+1/\\sqrt{2}, +1/\\sqrt{2})$, you get $\\lambda^* = -1/\\sqrt{2}$ and $\\det B = +4\\sqrt{2} > 0$. Since $\\det B > 0 \\ne (-1)^1$, the SOSC fails, correctly detecting a local maximum!"
    }
]

# Write Topic 12 cards
with open('/Users/senso/Projects/photographic-memory-cards/scripts/cmo_topic12.json', 'w') as f:
    json.dump(topic12_cards, f, indent=2)

print(f"Generated {len(topic12_cards)} cards for Topic 12")
