import json

# =============================================================================
# TOPIC 15: Active Set Methods for Quadratic Programming
# =============================================================================
topic15_cards = [
    {
        "id": 1501,
        "subject": "CMO",
        "topicId": "15_Active_Set_Methods_for_Quadratic_Programming",
        "topicTitle": "15 · Active Set Methods for QP",
        "cardNumber": "01",
        "category": "QUADRATIC PROGRAMMING",
        "highlighterClass": "highlight-cyan",
        "title": "Working Set Strategy & Equality Subproblems",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-1501" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- Polyhedral feasible region facets -->
  <polygon points="35,115 65,40 160,30 205,95 140,125" fill="#f8fafc" stroke="#000000" stroke-width="1.8"/>
  <!-- Active facet edge (Working set W_k) -->
  <line x1="65" y1="40" x2="160" y2="30" stroke="#000000" stroke-width="3"/>
  <text x="110" y="24" fill="#000000" font-size="8.5" font-family="sans-serif" font-weight="bold">Working Facet 𝒲_k: a_iᵀ x = b_i</text>
  <!-- Current iterate x_k -->
  <circle cx="85" cy="38" r="4" fill="#000000"/>
  <text x="80" y="52" fill="#000000" font-size="8.5" font-family="serif" font-style="italic">x_k</text>
  <!-- Step p_k along active facet -->
  <line x1="85" y1="38" x2="145" y2="32" stroke="#000000" stroke-width="2" marker-end="url(#arr-1501)"/>
  <circle cx="145" cy="32" r="3.5" fill="#000000"/>
  <text x="145" y="46" fill="#000000" font-size="8.5" font-family="serif" font-style="italic">x_k + p_k</text>
  <text x="120" y="138" fill="#000000" font-size="8.5" font-family="sans-serif" text-anchor="middle">Equality-Constrained Subproblem: min 1/2 pᵀ Q p + g_kᵀ p  s.t. A_𝒲 p = 0</text>
</svg>""",
        "drawingCaption": "Working Set Strategy: Active inequality constraints are treated as equalities, reducing QP to a linear system",
        "coreTranslation": [
            "<strong>Core Philosophy:</strong> An Active Set method converts an inequality-constrained Quadratic Program $\\min \\frac{1}{2} x^T Q x + c^T x$ s.t. $A x \\ge b$ into a sequence of <strong>equality-constrained QP subproblems</strong>.",
            "<strong>The Working Set $\\mathcal{W}_k$:</strong> A subset of constraint indices currently treated as active equalities: $a_i^T x = b_i$ for $i \\in \\mathcal{W}_k$.",
            "<strong>The Search Step $p_k$:</strong> At each iteration, solve for the step $p_k$: $\\min_p \\frac{1}{2} p^T Q p + g_k^T p$ s.t. $a_i^T p = 0$ for $i \\in \\mathcal{W}_k$. This is solved directly via the linear KKT system $\\begin{bmatrix} Q & A_\\mathcal{W}^T \\\\ A_\\mathcal{W} & 0 \\end{bmatrix} \\begin{bmatrix} p \\\\ -\\lambda \\end{bmatrix} = \\begin{bmatrix} -g_k \\\\ 0 \\end{bmatrix}$."
        ],
        "math": "$$\\begin{bmatrix} Q & A_{\\mathcal{W}_k}^T \\\\ A_{\\mathcal{W}_k} & 0 \\end{bmatrix} \\begin{bmatrix} p_k \\\\ -\\lambda_k \\end{bmatrix} = \\begin{bmatrix} -\\nabla f(x_k) \\\\ \\mathbf{0} \\end{bmatrix} \\quad (\\text{KKT Linear System for } p_k)$$",
        "personalConnection": "Walking with your back against a corridor wall: you don't worry about falling into the wall; the wall eliminates one lateral degree of freedom ($A_\\mathcal{W} p = 0$), so you only solve for motion along the hallway.",
        "examTrap": "The working set $\\mathcal{W}_k$ must be linearly independent! If redundant constraints are added to $\\mathcal{W}_k$, the KKT matrix becomes singular. Active set codes must ensure LICQ on $\\mathcal{W}_k$."
    },
    {
        "id": 1502,
        "subject": "CMO",
        "topicId": "15_Active_Set_Methods_for_Quadratic_Programming",
        "topicTitle": "15 · Active Set Methods for QP",
        "cardNumber": "02",
        "category": "BLOCKING CONSTRAINTS",
        "highlighterClass": "highlight-amber",
        "title": "Adding a Blocking Constraint to the Working Set",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-1502" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- Search path from x_k toward unconstrained minimum x_k + p_k -->
  <circle cx="50" cy="110" r="4" fill="#000000"/>
  <text x="50" y="125" fill="#000000" font-size="8.5" font-family="serif" font-style="italic">x_k</text>
  <!-- Blocking wall a_iᵀ x = b_i -->
  <line x1="140" y1="25" x2="140" y2="125" stroke="#000000" stroke-width="2.5"/>
  <text x="145" y="35" fill="#000000" font-size="8.5" font-family="serif" font-style="italic">Blocking Constraint i</text>
  <!-- Full step would violate boundary -->
  <line x1="50" y1="110" x2="195" y2="50" stroke="#000000" stroke-width="1.2" stroke-dasharray="3,3"/>
  <circle cx="195" cy="50" r="3" fill="#000000"/>
  <text x="195" y="42" fill="#000000" font-size="8" font-family="serif">x_k + p_k (Infeasible!)</text>
  <!-- Truncated step striking blocking wall -->
  <line x1="50" y1="110" x2="140" y2="73" stroke="#000000" stroke-width="2" marker-end="url(#arr-1502)"/>
  <circle cx="140" cy="73" r="4" fill="#000000"/>
  <text x="115" y="68" fill="#000000" font-size="8.5" font-family="serif" font-style="italic" font-weight="bold">x_{k+1}</text>
  <text x="120" y="18" fill="#000000" font-size="8.5" font-family="sans-serif" font-weight="bold" text-anchor="middle">Maximum Feasible Step: α_k = min(1, (b_i - a_iᵀ x_k) / a_iᵀ p_k)</text>
</svg>""",
        "drawingCaption": "Adding a Constraint: Step p_k is blocked by constraint boundary; we take maximum feasible step α_k and add i to 𝒲",
        "coreTranslation": [
            "If the full step $x_k + p_k$ is feasible ($a_i^T (x_k + p_k) \\ge b_i$ for all $i \\notin \\mathcal{W}_k$), we take the full step $\\alpha_k = 1$.",
            "<strong>The Blocking Constraint:</strong> If $x_k + p_k$ violates one or more inactive constraints, we compute the maximum step length $\\alpha_k \\in [0, 1)$ that maintains feasibility:",
            "$$\\alpha_k = \\min_{i \\notin \\mathcal{W}_k, \\, a_i^T p_k < 0} \\left\\{ \\frac{b_i - a_i^T x_k}{a_i^T p_k} \\right\\}$$",
            "The constraint achieving this minimum is called the <strong>blocking constraint</strong>. Set $x_{k+1} = x_k + \\alpha_k p_k$, and <strong>add index $i$ to the working set</strong> $\\mathcal{W}_{k+1} = \\mathcal{W}_k \\cup \\{i\\}$."
        ],
        "math": "$$\\alpha_k = \\min\\left( 1, \\; \\min_{i \\notin \\mathcal{W}_k, a_i^T p_k < 0} \\frac{b_i - a_i^T x_k}{a_i^T p_k} \\right), \\quad \\mathcal{W}_{k+1} = \\mathcal{W}_k \\cup \\{i_{\\text{blocking}}\\}$$",
        "personalConnection": "Walking forward in a dark room until your shin strikes a coffee table: you stop right at the edge of the table (step length $\\alpha < 1$) and add the coffee table to your mental map of active obstacles.",
        "examTrap": "Only consider constraints with $a_i^T p_k < 0$ (direction pointing INTO the forbidden halfspace)! If $a_i^T p_k \\ge 0$, you are moving parallel to or away from constraint $i$, so it can never block your step."
    },
    {
        "id": 1503,
        "subject": "CMO",
        "topicId": "15_Active_Set_Methods_for_Quadratic_Programming",
        "topicTitle": "15 · Active Set Methods for QP",
        "cardNumber": "03",
        "category": "CONSTRAINT RELEASE",
        "highlighterClass": "highlight-emerald",
        "title": "Dropping a Constraint with Negative Multiplier",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-1503" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- Constraint boundary wall to be dropped -->
  <line x1="120" y1="25" x2="120" y2="125" stroke="#000000" stroke-width="2.5"/>
  <text x="75" y="35" fill="#000000" font-size="8.5" font-family="serif">Feasible Set (a_jᵀ x ≥ b_j)</text>
  <!-- Stationary point on wall x_k with p_k = 0 -->
  <circle cx="120" cy="75" r="4" fill="#000000"/>
  <text x="125" y="70" fill="#000000" font-size="8.5" font-family="serif" font-style="italic">x_k (p_k = 0)</text>
  <!-- Negative multiplier pushes into interior -->
  <line x1="120" y1="75" x2="60" y2="75" stroke="#000000" stroke-width="2.2" marker-end="url(#arr-1503)"/>
  <text x="70" y="68" fill="#000000" font-size="8.5" font-family="serif" font-style="italic">μ_j &lt; 0 (Drop j!)</text>
  <text x="120" y="18" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Stationary on Facet (p_k = 0) with μ_j &lt; 0 ⇒ Release Constraint!</text>
  <text x="120" y="138" fill="#000000" font-size="8.5" font-family="sans-serif" text-anchor="middle">Moving into the interior decreases objective f without violating constraint j</text>
</svg>""",
        "drawingCaption": "Dropping a Constraint: When p_k = 0 and a multiplier μ_j < 0, dropping constraint j opens a descent direction into the interior",
        "coreTranslation": [
            "<strong>Stationarity on the Working Surface:</strong> When the equality subproblem yields $p_k = 0$, the current point $x_k$ is the exact minimizer on the current working facet $\\mathcal{W}_k$.",
            "<strong>Checking Multipliers:</strong> Compute the Lagrange multipliers $\\lambda_k$ for the working set. If all $\\lambda_i \\ge 0$, then $x_k$ satisfies all KKT conditions $\\implies$ <strong>OPTIMALITY ACHIEVED!</strong>",
            "<strong>Dropping Rule:</strong> If there exists a negative multiplier $\\lambda_j < 0$, the constraint is holding us back! By sensitivity theory, moving off this constraint into the feasible interior ($a_j^T x > b_j$) strictly <strong>decreases the objective</strong> $f$.",
            "We drop the constraint with the most negative multiplier: $\\mathcal{W}_{k+1} = \\mathcal{W}_k \\setminus \\{j\\}$."
        ],
        "math": "$$p_k = \\mathbf{0} \\quad \\text{and} \\quad \\lambda_j = \\min_{i \\in \\mathcal{W}_k} \\lambda_i < 0 \\implies \\mathcal{W}_{k+1} = \\mathcal{W}_k \\setminus \\{j\\}$$",
        "personalConnection": "Leaning against a closed door: if the door pushes you backward with negative force (someone unlocks and pulls the door open from the other side), you immediately step through into the open room.",
        "examTrap": "You can ONLY drop a constraint when $p_k = 0$ (at a stationary point of the current working surface)! Dropping a constraint while $p_k \\ne 0$ can cause premature release and severe algorithmic cycling."
    },
    {
        "id": 1504,
        "subject": "CMO",
        "topicId": "15_Active_Set_Methods_for_Quadratic_Programming",
        "topicTitle": "15 · Active Set Methods for QP",
        "cardNumber": "04",
        "category": "FINITE TERMINATION",
        "highlighterClass": "highlight-violet",
        "title": "Finite Termination Property of Active Set QP",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <!-- Facet graph transition nodes -->
  <circle cx="50" cy="75" r="18" fill="#f8fafc" stroke="#000000" stroke-width="1.8"/>
  <text x="50" y="78" fill="#000000" font-size="8.5" font-family="serif" text-anchor="middle">𝒲₁</text>
  <circle cx="120" cy="75" r="18" fill="#f8fafc" stroke="#000000" stroke-width="1.8"/>
  <text x="120" y="78" fill="#000000" font-size="8.5" font-family="serif" text-anchor="middle">𝒲₂</text>
  <circle cx="190" cy="75" r="18" fill="#ffffff" stroke="#000000" stroke-width="2.5"/>
  <text x="190" y="78" fill="#000000" font-size="8.5" font-family="serif" font-weight="bold" text-anchor="middle">𝒲*</text>
  <!-- Directed transitions with strictly decreasing f -->
  <line x1="68" y1="75" x2="102" y2="75" stroke="#000000" stroke-width="1.8" marker-end="url(#arr-1503)"/>
  <text x="85" y="65" fill="#000000" font-size="8" font-family="serif">f decreases</text>
  <line x1="138" y1="75" x2="172" y2="75" stroke="#000000" stroke-width="1.8" marker-end="url(#arr-1503)"/>
  <text x="155" y="65" fill="#000000" font-size="8" font-family="serif">f decreases</text>
  <text x="120" y="20" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Finite Termination: At Most 2^m Subproblems</text>
  <text x="120" y="136" fill="#000000" font-size="8.5" font-family="sans-serif" text-anchor="middle">Strict decrease in f prevents any working set from being revisited</text>
</svg>""",
        "drawingCaption": "Finite Termination: Since objective f strictly decreases at every step with α > 0, no working set is ever repeated",
        "coreTranslation": [
            "<strong>Master Theorem:</strong> For a strictly convex Quadratic Program ($Q \\succ 0$), assuming non-degeneracy (every step size $\\alpha_k > 0$), the active set algorithm <strong>terminates in a finite number of iterations</strong> at the unique global minimizer.",
            "<strong>Proof Mechanism:</strong>",
            "1. There are at most $2^m$ possible distinct working sets $\\mathcal{W}$.",
            "2. Whenever a full step $\\alpha_k = 1$ is taken, or a constraint is dropped with $\\mu_j < 0$, the objective $f(x)$ <strong>strictly decreases</strong>.",
            "3. Because $f(x)$ decreases monotonically, no working set $\\mathcal{W}$ can ever be visited more than once! Hence the algorithm must terminate in finite steps."
        ],
        "math": "$$Q \\succ 0 \\; \\text{ and } \\; \\alpha_k > 0 \\implies f(x_{k+1}) < f(x_k) \\implies \\text{Algorithm terminates in } \\le 2^m \\text{ steps}$$",
        "personalConnection": "Playing a board game with non-reversing tiles: every turn you move forward into a lower-numbered rank. Since the board has a finite number of squares ($2^m$), you are guaranteed to reach the finish line.",
        "examTrap": "Finite termination strictly requires <strong>non-degeneracy</strong>! If $\\alpha_k = 0$ (a degenerate vertex where multiple constraints intersect), $f(x)$ does not decrease, which opens the possibility of infinite cycling."
    },
    {
        "id": 1505,
        "subject": "CMO",
        "topicId": "15_Active_Set_Methods_for_Quadratic_Programming",
        "topicTitle": "15 · Active Set Methods for QP",
        "cardNumber": "05",
        "category": "DEGENERACY & CYCLING",
        "highlighterClass": "highlight-indigo",
        "title": "Degeneracy, Zero Steps (α = 0) & Anti-Cycling",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <!-- Degenerate vertex: 3 lines intersecting at single 2D point -->
  <line x1="30" y1="75" x2="210" y2="75" stroke="#000000" stroke-width="1.8"/>
  <text x="215" y="78" fill="#000000" font-size="8.5" font-family="serif">a₁ᵀx=b₁</text>
  <line x1="50" y1="125" x2="190" y2="25" stroke="#000000" stroke-width="1.8"/>
  <text x="195" y="28" fill="#000000" font-size="8.5" font-family="serif">a₂ᵀx=b₂</text>
  <line x1="50" y1="25" x2="190" y2="125" stroke="#000000" stroke-width="1.8"/>
  <text x="195" y="128" fill="#000000" font-size="8.5" font-family="serif">a₃ᵀx=b₃</text>
  <!-- Overdetermined vertex -->
  <circle cx="120" cy="75" r="4.5" fill="#000000"/>
  <text x="120" y="95" fill="#000000" font-size="9" font-family="serif" font-style="italic" font-weight="bold" text-anchor="middle">Degenerate Vertex (3 constraints in ℝ²)</text>
  <text x="120" y="20" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Zero Step Size: α_k = 0 ⇒ Infinite Cycling Risk</text>
</svg>""",
        "drawingCaption": "Degeneracy: More than n constraints intersect at a single vertex, leading to step size α=0 and potential cycling",
        "coreTranslation": [
            "<strong>Degeneracy in QP:</strong> Occurs when more than $n$ constraints are simultaneously active at $x_k$, or when an unselected constraint also passes through $x_k$ with $a_i^T p_k < 0$.",
            "<strong>The Consequence ($\\alpha_k = 0$):</strong> Formula $\\alpha_k = \\frac{b_i - a_i^T x_k}{a_i^T p_k} = \\frac{0}{a_i^T p_k} = 0$. The iterate does NOT move in physical space ($x_{k+1} = x_k$), but the working set changes $\\mathcal{W}_{k+1} \\ne \\mathcal{W}_k$.",
            "<strong>Anti-Cycling Strategies:</strong> If zero steps persist, the algorithm can cycle endlessly through a loop of working sets without making progress. Anti-cycling rules (Bland's smallest-subscript rule, or lexicographic perturbation $b_i \\leftarrow b_i + \\epsilon^i$) guarantee finite termination even under degeneracy."
        ],
        "math": "$$\\text{Degeneracy: } b_i - a_i^T x_k = 0 \\implies \\alpha_k = 0 \\implies x_{k+1} = x_k, \\quad f(x_{k+1}) = f(x_k)$$",
        "personalConnection": "A revolving door stuck at a three-way junction: the door spins in place without anyone moving into a new room. An anti-cycling rule pushes the door in a fixed priority sequence to break the loop.",
        "examTrap": "Cycling cannot happen in strictly convex QP as long as $\\alpha_k > 0$. Zero-step $\\alpha_k = 0$ is the SOLE mechanism through which cycling can theoretically occur."
    },
    {
        "id": 1506,
        "subject": "CMO",
        "topicId": "15_Active_Set_Methods_for_Quadratic_Programming",
        "topicTitle": "15 · Active Set Methods for QP",
        "cardNumber": "06",
        "category": "WORKED BENCHMARK",
        "highlighterClass": "highlight-rose",
        "title": "Worked Benchmark: 2D Active Set QP Traversal",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-1506" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- Box constraints [0, 2] x [0, 2] -->
  <rect x="50" y="30" width="120" height="90" fill="#f8fafc" stroke="#000000" stroke-width="1.8"/>
  <!-- Unconstrained minimizer at (3, 3) -->
  <circle cx="210" cy="15" r="3" fill="#000000"/>
  <text x="210" y="28" fill="#000000" font-size="8" font-family="serif">x_unc = (3,3)</text>
  <!-- Start x_0 = (0, 0) -->
  <circle cx="50" cy="120" r="4" fill="#000000"/>
  <text x="40" y="132" fill="#000000" font-size="8.5" font-family="serif">x₀=(0,0)</text>
  <!-- Step 1 to (2, 0) -->
  <line x1="50" y1="120" x2="170" y2="120" stroke="#000000" stroke-width="2" marker-end="url(#arr-1506)"/>
  <circle cx="170" cy="120" r="4" fill="#000000"/>
  <text x="175" y="132" fill="#000000" font-size="8.5" font-family="serif">x₁=(2,0)</text>
  <!-- Step 2 to (2, 2) -->
  <line x1="170" y1="120" x2="170" y2="30" stroke="#000000" stroke-width="2" marker-end="url(#arr-1506)"/>
  <circle cx="170" cy="30" r="4.5" fill="#000000"/>
  <text x="175" y="24" fill="#000000" font-size="8.5" font-family="serif" font-weight="bold">x*=(2,2)</text>
  <text x="110" y="75" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Feasible Box [0,2]²</text>
</svg>""",
        "drawingCaption": "Worked Active Set Traversal: Starts at (0,0), hits x₁=2 wall, drops x₂=0, and reaches optimal vertex (2,2) with positive multipliers",
        "coreTranslation": [
            "<strong>Problem:</strong> Minimize $f(x) = (x_1 - 3)^2 + (x_2 - 3)^2$ subject to $0 \\le x_1 \\le 2, \\; 0 \\le x_2 \\le 2$.",
            "<strong>Iteration 1:</strong> Start $x_0 = (0, 0)$ with $\\mathcal{W}_0 = \\{x_1 = 0, x_2 = 0\\}$. Multipliers $\\lambda = [-6, -6]^T < 0$. Drop $x_1 = 0$. Move along $x_2 = 0$ toward $x_1 = 3$. Blocked at $x_1 = 2$ ($\alpha = 2/3$). New iterate $x_1 = (2, 0)$ with $\\mathcal{W}_1 = \\{x_1 = 2, x_2 = 0\\}$.",
            "<strong>Iteration 2:</strong> Subproblem on $\\mathcal{W}_1$ gives $p_1 = 0$. Multiplier on $x_2 = 0$ is $\\lambda_2 = -6 < 0$. Drop $x_2 = 0$. Move vertically along $x_1 = 2$ toward $x_2 = 3$. Blocked at $x_2 = 2$. New iterate $x_2 = (2, 2)$ with $\\mathcal{W}_2 = \\{x_1 = 2, x_2 = 2\\}$.",
            "<strong>Iteration 3:</strong> Subproblem yields $p = 0$. Multipliers are $\\lambda_1 = 2(2-3)(-1) = 2 > 0$ and $\\lambda_2 = 2(2-3)(-1) = 2 > 0$. Both multipliers are strictly positive! <strong>$x^* = (2, 2)$ is optimal.</strong>"
        ],
        "math": "$$x_0 = (0,0) \\xrightarrow{\\text{drop } x_1=0} x_1 = (2, 0) \\xrightarrow{\\text{drop } x_2=0} x^* = (2, 2) \\quad (\\lambda_1^* = 2 > 0, \\; \\lambda_2^* = 2 > 0)$$",
        "personalConnection": "Navigating a corner of a square room toward a beacon outside: you walk along the south baseboard until you hit the east wall, then walk up the east wall until you reach the north-east corner.",
        "examTrap": "Verify that when dropping a constraint, the search direction $p$ is strictly feasible with respect to the dropped constraint: $a_j^T p > 0$! If $a_j^T p < 0$, you would re-enter the forbidden zone."
    }
]

# Write Topic 15 cards
with open('/Users/senso/Projects/photographic-memory-cards/scripts/cmo_topic15.json', 'w') as f:
    json.dump(topic15_cards, f, indent=2)

print(f"Generated {len(topic15_cards)} cards for Topic 15")
