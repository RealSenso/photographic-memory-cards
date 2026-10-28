import json

with open('/Users/senso/Projects/photographic-memory-cards/cards_data.js') as f:
    text = f.read()

start = text.find('[')
end = text.rfind(']') + 1
cards = json.loads(text[start:end])

topic09_cards = [
    {
        "id": 901,
        "subject": "CMO",
        "topicId": "09_Geometry_of_Constrained_Optimization_Tangent_Cone_and_LICQ",
        "topicTitle": "09 · Tangent Cones & LICQ Geometry",
        "cardNumber": "01",
        "category": "OPTIMIZATION GEOMETRY",
        "highlighterClass": "highlight-amber",
        "title": "Feasible Set & Active Constraints",
        "textbookImg": "assets/luenberger_fig11_1.png",
        "textbookRef": "Luenberger & Ye (4th ed), Sect. 11.1, Fig. 11.1 (p. 322)",
        "drawingCaption": "Luenberger Fig. 11.1: Inactive g₂ and g₃ are far from x* with zero local effect",
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
        "topicTitle": "09 · Tangent Cones & LICQ Geometry",
        "cardNumber": "02",
        "category": "LIMIT DEFINITIONS",
        "highlighterClass": "highlight-cyan",
        "title": "The Tangent Vector d & Tangent Plane",
        "textbookImg": "assets/luenberger_fig11_2a.png",
        "textbookRef": "Luenberger & Ye (4th ed), Sect. 11.2, Fig. 11.2a (p. 324)",
        "drawingCaption": "Luenberger Fig. 11.2a: Tangent plane M to surface S at x* with normal ∇h(x*)ᵀ",
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
        "topicTitle": "09 · Tangent Cones & LICQ Geometry",
        "cardNumber": "03",
        "category": "CONE GEOMETRY",
        "highlighterClass": "highlight-emerald",
        "title": "The Tangent Cone T_Ω(x)",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
            <defs>
              <radialGradient id="cone-glow" cx="20%" cy="70%" r="80%">
                <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.35"/>
                <stop offset="100%" stop-color="#38bdf8" stop-opacity="0.02"/>
              </radialGradient>
            </defs>
            <path d="M 50 110 L 190 40 L 190 110 Z" fill="url(#cone-glow)" stroke="#38bdf8" stroke-width="2"/>
            <circle cx="50" cy="110" r="4.5" fill="#f59e0b"/>
            <text x="50" y="128" fill="#f59e0b" font-size="9" font-family="monospace" text-anchor="middle">x*</text>
            <text x="135" y="90" fill="#38bdf8" font-size="11" font-weight="bold" font-family="monospace">T_Ω(x*)</text>
          </svg>""",
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
        "topicTitle": "09 · Tangent Cones & LICQ Geometry",
        "cardNumber": "04",
        "category": "WORKED STEP-BY-STEP",
        "highlighterClass": "highlight-rose",
        "title": "Computing T_Ω(0,0) for x₁, x₂ ≥ 0",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
            <line x1="40" y1="115" x2="200" y2="115" stroke="#475569" stroke-width="1.5"/>
            <line x1="50" y1="125" x2="50" y2="25" stroke="#475569" stroke-width="1.5"/>
            <rect x="50" y="25" width="140" height="90" fill="rgba(56,189,248,0.18)" stroke="#38bdf8" stroke-dasharray="3,3"/>
            <circle cx="50" cy="115" r="4.5" fill="#f59e0b"/>
            <text x="120" y="65" fill="#38bdf8" font-size="10" font-weight="bold" font-family="monospace">T_Ω = R²₊ (First Quadrant)</text>
          </svg>""",
        "drawingCaption": "Worked Calculation: Positive orthant feasible set Ω generates identical tangent cone T_Ω = R²₊ at the origin",
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
        "topicTitle": "09 · Tangent Cones & LICQ Geometry",
        "cardNumber": "05",
        "category": "OPTIMALITY THEOREM",
        "highlighterClass": "highlight-violet",
        "title": "First-Order Optimality: ∇f(x*)ᵀd ≥ 0",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
            <line x1="120" y1="80" x2="60" y2="40" stroke="#ef4444" stroke-width="2"/>
            <text x="50" y="35" fill="#ef4444" font-size="8" font-family="monospace">-∇f(x*)</text>
            <path d="M 120 80 L 190 30 L 190 120 Z" fill="rgba(56,189,248,0.2)" stroke="#38bdf8" stroke-width="2"/>
            <circle cx="120" cy="80" r="4" fill="#f59e0b"/>
            <text x="145" y="75" fill="#38bdf8" font-size="9" font-family="monospace">T_Ω(x*)</text>
            <text x="120" y="130" fill="#cbd5e1" font-size="8" font-family="monospace" text-anchor="middle">Separation: -∇f ∉ Interior(T_Ω)</text>
          </svg>""",
        "drawingCaption": "Fundamental Theorem: Steepest descent vector -∇f points away from the cone of feasible directions T_Ω",
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
        "topicTitle": "09 · Tangent Cones & LICQ Geometry",
        "cardNumber": "06",
        "category": "EXAM TRAPS & CQ",
        "highlighterClass": "highlight-amber",
        "title": "Tangent Cone vs Linearized Cone (LICQ)",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
            <line x1="50" y1="120" x2="190" y2="40" stroke="#38bdf8" stroke-width="2"/>
            <text x="195" y="45" fill="#38bdf8" font-size="8" font-family="monospace">T_Ω (True Curve)</text>
            <line x1="50" y1="120" x2="190" y2="80" stroke="#f59e0b" stroke-dasharray="3,3" stroke-width="2"/>
            <text x="195" y="85" fill="#f59e0b" font-size="8" font-family="monospace">L_Ω (Linearized)</text>
            <circle cx="50" cy="120" r="4.5" fill="#ef4444"/>
            <text x="120" y="130" fill="#ef4444" font-size="8" font-family="monospace" text-anchor="middle">LICQ Fails: T_Ω ⊊ L_Ω (Cusp)</text>
          </svg>""",
        "drawingCaption": "Constraint Qualification Failure: Linearized cone L_Ω over-approximates true geometric tangent cone T_Ω",
        "coreTranslation": [
            "The <strong>Linearized Cone $L_\\Omega(x)$</strong> is defined by active constraint gradients: $L_\\Omega = \\{d : \\nabla h_i^T d = 0, \\nabla g_j^T d \\le 0\\}$. In general, $T_\\Omega \\subseteq L_\\Omega$.",
            "<strong>Constraint Qualification (CQ):</strong> A condition guaranteeing $T_\\Omega(x^*) = L_\\Omega(x^*)$. The gold standard is <strong>LICQ</strong>: active gradients $\\{\\nabla h_i, \\nabla g_j\\}_{j \\in \\mathcal{A}}$ are linearly independent.",
            "Without CQ, $T_\\Omega \\subsetneq L_\\Omega$. KKT conditions can FAIL completely even at an obvious local minimum!"
        ],
        "math": "$$\\text{LICQ Holds} \\implies T_\\Omega(x^*) = L_\\Omega(x^*) = \\{d : \\nabla h_i^T d = 0, \\, \\nabla g_j^T d \\le 0 \\, (j \\in \\mathcal{A})\\}$$",
        "personalConnection": "Contractor drawing straight tangent lines on blueprints to approximate a sharp curved wall: if the wall has an acute cusp, the blueprint allows steps that smash into brick.",
        "examTrap": "Assuming KKT multipliers always exist! If $T_\\Omega \\ne L_\\Omega$ (CQ fails), a local minimum can exist where KKT multipliers DO NOT exist at all."
    }
]

all_cards = cards + topic09_cards

with open('/Users/senso/Projects/photographic-memory-cards/cards_data.js', 'w') as f:
    f.write('/* Master Cards Database for CMO, LAA, StoMA, DIP */\n')
    f.write('window.MASTER_CARDS_DATA = ')
    json.dump(all_cards, f, indent=2)
    f.write(';\n')

print(f'Total cards in master database: {len(all_cards)}')
