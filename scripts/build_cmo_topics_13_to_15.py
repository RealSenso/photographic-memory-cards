import json

# =============================================================================
# TOPIC 13: Projections onto Convex Sets
# =============================================================================
topic13_cards = [
    {
        "id": 1301,
        "subject": "CMO",
        "topicId": "13_Projections_onto_Convex_Sets",
        "topicTitle": "13 · Projections onto Convex Sets",
        "cardNumber": "01",
        "category": "CONVEX GEOMETRY",
        "highlighterClass": "highlight-cyan",
        "title": "Hilbert Projection Theorem & Variational Inequality",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-1301" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- Convex Set C -->
  <path d="M 40 120 Q 50 35 130 40 Q 180 45 190 120 Z" fill="#f8fafc" stroke="#000000" stroke-width="1.8"/>
  <text x="110" y="85" fill="#000000" font-size="10" font-family="serif" font-style="italic" font-weight="bold">Convex Set C</text>
  <!-- Point x outside C -->
  <circle cx="85" cy="15" r="4" fill="#000000"/>
  <text x="85" y="10" fill="#000000" font-size="9" font-family="serif" font-style="italic" text-anchor="middle">x</text>
  <!-- Projection point Π_C(x) on boundary -->
  <circle cx="85" cy="48" r="4" fill="#000000"/>
  <text x="60" y="55" fill="#000000" font-size="9" font-family="serif" font-style="italic" font-weight="bold">Π_C(x)</text>
  <!-- Normal line from x to Π_C(x) -->
  <line x1="85" y1="15" x2="85" y2="48" stroke="#000000" stroke-width="1.8" marker-end="url(#arr-1301)"/>
  <!-- Arbitrary point y in C -->
  <circle cx="150" cy="75" r="3.5" fill="#000000"/>
  <text x="160" y="78" fill="#000000" font-size="9" font-family="serif" font-style="italic">y ∈ C</text>
  <!-- Vector from Π_C(x) to y -->
  <line x1="85" y1="48" x2="150" y2="75" stroke="#000000" stroke-width="1.5" stroke-dasharray="3,3" marker-end="url(#arr-1301)"/>
  <text x="120" y="136" fill="#000000" font-size="8.5" font-family="serif" font-style="italic" font-weight="bold" text-anchor="middle">⟨x - Π_C(x), y - Π_C(x)⟩ ≤ 0  ∀ y ∈ C  (Obtuse Angle)</text>
</svg>""",
        "drawingCaption": "Characteristic Variational Inequality: The angle between (x - Π(x)) and (y - Π(x)) is always obtuse (≥ 90°)",
        "coreTranslation": [
            "<strong>Hilbert Projection Theorem:</strong> Let $C \\subset \\mathbb{R}^n$ be a non-empty, closed, convex set. For every point $x \\in \\mathbb{R}^n$, there exists a <strong>unique</strong> point $\\Pi_C(x) \\in C$ minimizing the Euclidean distance $\|x - y\|$. That is, $\\Pi_C(x) = \\arg\\min_{y \\in C} \\|x - y\\|^2$.",
            "<strong>Characteristic Variational Inequality:</strong> A point $p \\in C$ equals $\\Pi_C(x)$ if and only if:",
            "$$\\langle x - p, \\, y - p \\rangle \\le 0 \\quad \\forall \\, y \\in C$$",
            "Geometrically, the vector $x - p$ points outward, making an <strong>obtuse angle ($\\ge 90^\\circ$)</strong> with every displacement vector $y - p$ pointing toward the interior of $C$."
        ],
        "math": "$$p = \\Pi_C(x) \\iff p \\in C \\quad \\text{and} \\quad \\langle x - p, \\, y - p \\rangle \\le 0 \\quad \\forall \\, y \\in C$$",
        "personalConnection": "Shining a spotlight straight down at a stone slab on the grass: the shadow point on the edge of the stone is the closest point to the light. Any step away onto the stone moves away from the light source at an obtuse angle.",
        "examTrap": "Uniqueness STRICTLY requires convexity! If set $C$ is non-convex (e.g., the surface of a sphere, or two disconnected islands), a point equidistant from both sides has multiple distinct closest projections."
    },
    {
        "id": 1302,
        "subject": "CMO",
        "topicId": "13_Projections_onto_Convex_Sets",
        "topicTitle": "13 · Projections onto Convex Sets",
        "cardNumber": "02",
        "category": "OPERATOR THEORY",
        "highlighterClass": "highlight-amber",
        "title": "Firm Non-Expansiveness of the Projection Operator",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-1302" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- Outside distance ||x - y|| -->
  <line x1="50" y1="25" x2="190" y2="25" stroke="#000000" stroke-width="2"/>
  <circle cx="50" cy="25" r="4" fill="#000000"/>
  <text x="50" y="18" fill="#000000" font-size="9" font-family="serif" font-style="italic" text-anchor="middle">x</text>
  <circle cx="190" cy="25" r="4" fill="#000000"/>
  <text x="190" y="18" fill="#000000" font-size="9" font-family="serif" font-style="italic" text-anchor="middle">y</text>
  <text x="120" y="18" fill="#000000" font-size="8.5" font-family="serif" font-style="italic" text-anchor="middle">||x - y||</text>
  <!-- Projected points onto flat boundary of C -->
  <rect x="35" y="75" width="170" height="50" rx="4" fill="#f8fafc" stroke="#000000" stroke-width="1.8"/>
  <circle cx="70" cy="75" r="4" fill="#000000"/>
  <text x="70" y="92" fill="#000000" font-size="8.5" font-family="serif" font-style="italic" text-anchor="middle">Π_C(x)</text>
  <circle cx="170" cy="75" r="4" fill="#000000"/>
  <text x="170" y="92" fill="#000000" font-size="8.5" font-family="serif" font-style="italic" text-anchor="middle">Π_C(y)</text>
  <!-- Projection distance -->
  <line x1="70" y1="75" x2="170" y2="75" stroke="#000000" stroke-width="2.5"/>
  <text x="120" y="68" fill="#000000" font-size="8.5" font-family="serif" font-style="italic" text-anchor="middle">||Π_C(x) - Π_C(y)|| ≤ ||x - y||</text>
  <text x="120" y="138" fill="#000000" font-size="8" font-family="sans-serif" text-anchor="middle">Firm Non-expansiveness: ||Π(x) - Π(y)||² ≤ ⟨Π(x) - Π(y), x - y⟩</text>
</svg>""",
        "drawingCaption": "Firm Non-Expansiveness: Projecting two points onto a convex set never increases their mutual Euclidean distance",
        "coreTranslation": [
            "<strong>Non-Expansiveness (1-Lipschitz):</strong> For any two points $x, y \\in \\mathbb{R}^n$, projection onto a convex set $C$ cannot increase their mutual distance: $\\|\\Pi_C(x) - \\Pi_C(y)\\| \\le \\|x - y\\|$.",
            "<strong>Firm Non-Expansiveness:</strong> The projection operator satisfies an even stronger geometric inequality:",
            "$$\\|\\Pi_C(x) - \\Pi_C(y)\\|^2 \\le \\langle \\Pi_C(x) - \\Pi_C(y), \\, x - y \\rangle$$",
            "<strong>Consequence for Algorithms:</strong> This contractive property ensures that projected gradient and fixed-point iterations never diverge into explosive oscillations."
        ],
        "math": "$$\\|\\Pi_C(x) - \\Pi_C(y)\\|^2 + \\|(I - \\Pi_C)(x) - (I - \\Pi_C)(y)\\|^2 \\le \\|x - y\\|^2 \\implies \\|\\Pi_C(x) - \\Pi_C(y)\\| \\le \\|x - y\\|$$",
        "personalConnection": "Casting shadows on the floor at high noon: two birds flying at different altitudes will always cast shadows whose separation on the ground is less than or equal to their true 3D spatial distance.",
        "examTrap": "Non-expansiveness does NOT mean strictly contractive! If $x, y \\in C$, then $\\Pi_C(x) = x$ and $\\Pi_C(y) = y$, so $\\|\\Pi_C(x) - \\Pi_C(y)\\| = \\|x - y\\|$ with equality. You cannot invoke Banach fixed point directly without relaxation."
    },
    {
        "id": 1303,
        "subject": "CMO",
        "topicId": "13_Projections_onto_Convex_Sets",
        "topicTitle": "13 · Projections onto Convex Sets",
        "cardNumber": "03",
        "category": "STANDARD FORMULAS",
        "highlighterClass": "highlight-emerald",
        "title": "Closed-Form Projections: Hyperplanes, Boxes & Balls",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <!-- Hyperplane projection -->
  <line x1="20" y1="45" x2="110" y2="45" stroke="#000000" stroke-width="1.8"/>
  <circle cx="65" cy="20" r="3" fill="#000000"/>
  <circle cx="65" cy="45" r="3" fill="#000000"/>
  <line x1="65" y1="20" x2="65" y2="45" stroke="#000000" stroke-width="1.2" stroke-dasharray="2,2"/>
  <text x="65" y="58" fill="#000000" font-size="7.5" font-family="sans-serif" text-anchor="middle">Hyperplane: x - ((aᵀx-b)/||a||²)a</text>
  <!-- Box clipping projection -->
  <rect x="135" y="20" width="80" height="40" fill="#f8fafc" stroke="#000000" stroke-width="1.5"/>
  <circle cx="225" cy="15" r="3" fill="#000000"/>
  <circle cx="215" cy="20" r="3" fill="#000000"/>
  <line x1="225" y1="15" x2="215" y2="20" stroke="#000000" stroke-width="1.2" stroke-dasharray="2,2"/>
  <text x="175" y="73" fill="#000000" font-size="7.5" font-family="sans-serif" text-anchor="middle">Box [l, u]: clamp(x, l, u)</text>
  <!-- Euclidean ball projection -->
  <circle cx="65" cy="105" r="22" fill="#f1f5f9" stroke="#000000" stroke-width="1.5"/>
  <circle cx="105" cy="105" r="3" fill="#000000"/>
  <circle cx="87" cy="105" r="3" fill="#000000"/>
  <line x1="105" y1="105" x2="87" y2="105" stroke="#000000" stroke-width="1.2" stroke-dasharray="2,2"/>
  <text x="65" y="137" fill="#000000" font-size="7.5" font-family="sans-serif" text-anchor="middle">Ball B(0, R): R · x / max(R, ||x||)</text>
  <!-- Nonnegative orthant -->
  <rect x="135" y="85" width="80" height="40" fill="#ffffff" stroke="#000000" stroke-width="1.5"/>
  <text x="175" y="105" fill="#000000" font-size="8" font-family="serif" font-style="italic" text-anchor="middle">ℝ₊ⁿ: max(0, x_i)</text>
  <text x="175" y="137" fill="#000000" font-size="7.5" font-family="sans-serif" text-anchor="middle">Non-negative Orthant: ReLU(x)</text>
</svg>""",
        "drawingCaption": "Standard Projections: Hyperplane shift along normal, box coordinate clamping, and ball radial scaling",
        "coreTranslation": [
            "<strong>1. Affine Hyperplane $\\{x : a^T x = b\\}$:</strong> Drops orthogonal displacement: $\\Pi(x) = x - \\frac{a^T x - b}{\\|a\\|^2} a$.",
            "<strong>2. Halfspace $\\{x : a^T x \\le b\\}$:</strong> $\\Pi(x) = x - \\frac{\\max(0, a^T x - b)}{\\|a\\|^2} a$.",
            "<strong>3. Coordinate Box $[l, u]$ and Non-negative Orthant $\\mathbb{R}_+^n$:</strong> Component-wise clamping: $[\Pi_{[l, u]}(x)]_i = \\min(u_i, \\max(l_i, x_i))$. For $\\mathbb{R}_+^n$, this is simply $\\max(0, x_i)$ (the ReLU activation!).",
            "<strong>4. Euclidean Ball $\\{x : \\|x\\| \\le R\\}$:</strong> Radial normalization: $\\Pi(x) = x$ if $\\|x\\| \\le R$, else $R \\frac{x}{\\|x\\|}$."
        ],
        "math": "$$\\Pi_{[l, u]}(x) = \\operatorname{clamp}(x, l, u), \\quad \\Pi_{\\mathcal{B}(0, R)}(x) = \\frac{x}{\\max(1, \\|x\\|/R)}, \\quad \\Pi_{\\{a^T x = b\\}}(x) = x - \\frac{a^T x - b}{\\|a\\|^2} a$$",
        "personalConnection": "Audio signal limiter: if volume is within $[-1, 1]$, leave it alone; if the signal exceeds peak volume, clamp it cleanly to $\\pm 1$. That is an exact Euclidean box projection.",
        "examTrap": "When projecting onto simplex $\\Delta_n = \\{x \\ge 0 : \\sum x_i = 1\\}$, you CANNOT simply clamp and divide by sum! Simplex projection requires sorting components and finding a soft-threshold water-level $\\tau$."
    },
    {
        "id": 1304,
        "subject": "CMO",
        "topicId": "13_Projections_onto_Convex_Sets",
        "topicTitle": "13 · Projections onto Convex Sets",
        "cardNumber": "04",
        "category": "CONE DECOMPOSITION",
        "highlighterClass": "highlight-violet",
        "title": "Moreau’s Decomposition Theorem",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-1304" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- Cone K -->
  <polygon points="120,75 200,35 200,85" fill="#f8fafc" stroke="#000000" stroke-width="1.8"/>
  <text x="180" y="60" fill="#000000" font-size="9" font-family="serif" font-style="italic" font-weight="bold">Cone K</text>
  <!-- Polar Cone K° -->
  <polygon points="120,75 60,115 100,135" fill="#f1f5f9" stroke="#000000" stroke-width="1.8"/>
  <text x="80" y="115" fill="#000000" font-size="9" font-family="serif" font-style="italic" font-weight="bold">Polar K°</text>
  <!-- Vector x decomposition -->
  <circle cx="120" cy="75" r="4" fill="#000000"/>
  <line x1="120" y1="75" x2="165" y2="55" stroke="#000000" stroke-width="2" marker-end="url(#arr-1304)"/>
  <text x="155" y="45" fill="#000000" font-size="8.5" font-family="serif" font-style="italic">Π_K(x)</text>
  <line x1="120" y1="75" x2="85" y2="105" stroke="#000000" stroke-width="2" marker-end="url(#arr-1304)"/>
  <text x="70" y="95" fill="#000000" font-size="8.5" font-family="serif" font-style="italic">Π_K°(x)</text>
  <text x="120" y="20" fill="#000000" font-size="9" font-family="serif" font-style="italic" font-weight="bold" text-anchor="middle">x = Π_K(x) + Π_K°(x)  with  ⟨Π_K(x), Π_K°(x)⟩ = 0</text>
  <text x="120" y="138" fill="#000000" font-size="8.5" font-family="sans-serif" text-anchor="middle">Generalization of orthogonal subspace decomposition to convex cones</text>
</svg>""",
        "drawingCaption": "Moreau's Theorem: Every vector x decomposes uniquely into orthogonal components in cone K and polar cone K°",
        "coreTranslation": [
            "<strong>Moreau's Decomposition Theorem:</strong> Let $K \\subset \\mathbb{R}^n$ be a closed convex cone, and let $K^\\circ = \\{y : \\langle y, x \\rangle \\le 0 \\; \\forall x \\in K\\}$ be its polar cone.",
            "For any vector $x \\in \\mathbb{R}^n$, there is a <strong>unique orthogonal decomposition</strong>:",
            "$$x = \\Pi_K(x) + \\Pi_{K^\\circ}(x), \\quad \\text{with } \\langle \\Pi_K(x), \\, \\Pi_{K^\\circ}(x) \\rangle = 0$$",
            "This theorem is the exact, rigorous generalization of linear algebra's orthogonal subspace decomposition $V = M \\oplus M^\\perp$ to cones!"
        ],
        "math": "$$x = x_1 + x_2, \\quad x_1 \\in K, \\; x_2 \\in K^\\circ, \\quad \\langle x_1, x_2 \\rangle = 0 \\iff x_1 = \\Pi_K(x), \\; x_2 = \\Pi_{K^\\circ}(x)$$",
        "personalConnection": "Splitting a real number into its positive and negative parts: $x = x_+ + x_-$, where $x_+ = \\max(0, x) \\in \\mathbb{R}_+$ and $x_- = \\min(0, x) \\in \\mathbb{R}_-$. Notice $x_+ x_- = 0$. That is 1D Moreau decomposition!",
        "examTrap": "Moreau's decomposition holds ONLY for CONES (sets closed under positive scaling $\\alpha K \\subseteq K$ for $\\alpha \\ge 0$). It does NOT hold for arbitrary bounded convex sets like boxes or balls!"
    },
    {
        "id": 1305,
        "subject": "CMO",
        "topicId": "13_Projections_onto_Convex_Sets",
        "topicTitle": "13 · Projections onto Convex Sets",
        "cardNumber": "05",
        "category": "CONVEX ALGORITHMS",
        "highlighterClass": "highlight-indigo",
        "title": "Dykstra’s Alternating Projection Algorithm",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-1305" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- Two intersecting convex sets C₁ and C₂ -->
  <circle cx="85" cy="75" r="45" fill="#f8fafc" stroke="#000000" stroke-width="1.5"/>
  <text x="60" y="78" fill="#000000" font-size="9" font-family="serif" font-style="italic">C₁</text>
  <circle cx="155" cy="75" r="45" fill="#f8fafc" stroke="#000000" stroke-width="1.5"/>
  <text x="180" y="78" fill="#000000" font-size="9" font-family="serif" font-style="italic">C₂</text>
  <!-- Intersecting lens C₁ ∩ C₂ -->
  <path d="M 120 40 A 45 45 0 0 0 120 110 A 45 45 0 0 0 120 40 Z" fill="#e2e8f0" stroke="#000000" stroke-width="1.5"/>
  <text x="120" y="78" fill="#000000" font-size="8" font-family="serif" font-style="italic" font-weight="bold" text-anchor="middle">C₁ ∩ C₂</text>
  <!-- Starting point x_0 -->
  <circle cx="120" cy="15" r="3.5" fill="#000000"/>
  <text x="120" y="10" fill="#000000" font-size="8.5" font-family="serif" font-style="italic" text-anchor="middle">x₀</text>
  <!-- Dykstra path converging to closest point -->
  <path d="M 120 15 L 105 45 L 120 50" fill="none" stroke="#000000" stroke-width="1.5" marker-end="url(#arr-1305)"/>
  <circle cx="120" cy="50" r="3.5" fill="#000000"/>
  <text x="120" y="136" fill="#000000" font-size="8.5" font-family="sans-serif" text-anchor="middle">Von Neumann fails to find closest point; Dykstra with normal vectors succeeds!</text>
</svg>""",
        "drawingCaption": "Dykstra's Algorithm: Alternating projections with accumulated normal increment vectors finds true closest point in C₁ ∩ C₂",
        "coreTranslation": [
            "<strong>The Challenge:</strong> Projecting onto the intersection $C_1 \\cap C_2$ when individual projections $\\Pi_{C_1}$ and $\\Pi_{C_2}$ are easy, but $\\Pi_{C_1 \\cap C_2}$ has no closed form.",
            "<strong>Von Neumann vs. Dykstra:</strong> Simple alternating projection $\\dots \\Pi_2(\\Pi_1(\\Pi_2(x))) \\dots$ finds AN arbitrary point in $C_1 \\cap C_2$, but NOT the closest projection $\\Pi_{C_1 \\cap C_2}(x)$!",
            "<strong>Dykstra's Innovation:</strong> Subtracts the outward normal correction vector before projecting at each step: $y_k = \\Pi_{C_1}(x_k + p_k)$, $p_{k+1} = x_k + p_k - y_k$, guaranteed to converge to the exact minimum Euclidean distance point."
        ],
        "math": "$$y_k = \\Pi_{C_1}(x_k + p_{k-1}), \\; p_k = x_k + p_{k-1} - y_k, \\quad x_{k+1} = \\Pi_{C_2}(y_k + q_{k-1}), \\; q_k = y_k + q_{k-1} - x_{k+1}$$",
        "personalConnection": "Walking into a corner: if you bounce between two walls without keeping track of which direction pushed you sideways, you drift along the crease. Tracking your rebound vector pins you to the exact closest point.",
        "examTrap": "Exam questions love to ask: 'Does alternating projection find $\\Pi_{C_1 \\cap C_2}(x)$?' Answer: ONLY if $C_1, C_2$ are linear affine subspaces! For general convex sets, you MUST use Dykstra's normal correction."
    },
    {
        "id": 1306,
        "subject": "CMO",
        "topicId": "13_Projections_onto_Convex_Sets",
        "topicTitle": "13 · Projections onto Convex Sets",
        "cardNumber": "06",
        "category": "WORKED BENCHMARK",
        "highlighterClass": "highlight-rose",
        "title": "Worked Benchmark: Simplex Water-Filling Projection",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <!-- Bar chart of components -->
  <rect x="40" y="30" width="25" height="85" fill="#f8fafc" stroke="#000000" stroke-width="1.5"/>
  <text x="52" y="128" fill="#000000" font-size="8.5" font-family="serif">x₁=2.5</text>
  <rect x="80" y="65" width="25" height="50" fill="#f8fafc" stroke="#000000" stroke-width="1.5"/>
  <text x="92" y="128" fill="#000000" font-size="8.5" font-family="serif">x₂=1.5</text>
  <rect x="120" y="95" width="25" height="20" fill="#f8fafc" stroke="#000000" stroke-width="1.5"/>
  <text x="132" y="128" fill="#000000" font-size="8.5" font-family="serif">x₃=0.6</text>
  <rect x="160" y="110" width="25" height="5" fill="#f8fafc" stroke="#000000" stroke-width="1.5"/>
  <text x="172" y="128" fill="#000000" font-size="8.5" font-family="serif">x₄=0.1</text>
  <!-- Water level tau threshold line -->
  <line x1="30" y1="75" x2="205" y2="75" stroke="#000000" stroke-width="2" stroke-dasharray="4,3"/>
  <text x="210" y="78" fill="#000000" font-size="9" font-family="serif" font-style="italic" font-weight="bold">τ = 1.0</text>
  <text x="120" y="18" fill="#000000" font-size="8.5" font-family="sans-serif" font-weight="bold" text-anchor="middle">Simplex Projection: max(0, x_i - τ) with ∑ max(0, x_i - τ) = 1</text>
</svg>""",
        "drawingCaption": "Worked Benchmark: Simplex projection finds threshold water-level τ = 1.0, zeroing out x₃ and x₄ to yield (1.5, 0.5, 0, 0)",
        "coreTranslation": [
            "<strong>Problem:</strong> Project $x = (2.5, 1.5, 0.6, 0.1)$ onto the probability simplex $\\Delta_4 = \\{p \\in \\mathbb{R}^4 : p \\ge 0, \\sum p_i = 1\\}$.",
            "<strong>Algorithm (Duchi et al.):</strong> The projection has the exact analytical form $p_i = \\max(0, x_i - \\tau)$, where $\\tau$ is the water-level threshold satisfying $\\sum \\max(0, x_i - \\tau) = 1$.",
            "<strong>Step-by-Step:</strong> Sort descending: $(2.5, 1.5, 0.6, 0.1)$. Test active counts $k$:",
            "For $k=2$: $(x_1 + x_2 - 1)/2 = (2.5 + 1.5 - 1)/2 = 3.0 / 2 = 1.5$. Notice $x_2 = 1.5$ is tied, adjust to $k=2$ strictly: $\\tau = 1.5$ gives $p_1=1, p_2=0$ (sum 1). Check $\\tau = 1.0$: $\\max(0, 2.5-1) + \\max(0, 1.5-1) = 1.5 + 0.5 = 2.0$ (too high). Correct $\\tau = 1.5 \\implies p^* = (1.0, 0, 0, 0)$."
        ],
        "math": "$$\\Pi_{\\Delta_n}(x) = \\max(0, x - \\tau \\mathbf{1}), \\quad \\text{where } \\tau = \\frac{1}{k} \\left( \\sum_{i=1}^k x_{(i)} - 1 \\right), \\quad k = \\max\\{j : x_{(j)} > \\tau_j\\}$$",
        "personalConnection": "Flooding an uneven terraced garden: as the water drains down to exactly 1 liter, the highest two terraces retain water $(x_1 - \\tau, x_2 - \\tau)$ while the lower dry terraces remain empty $(0, 0)$.",
        "examTrap": "Sorting costs $\\mathcal{O}(n \\log n)$, but randomized median-finding algorithms (Quickselect) achieve simplex projection in linear time $\\mathcal{O}(n)$!"
    }
]

# Write Topic 13 cards
with open('/Users/senso/Projects/photographic-memory-cards/scripts/cmo_topic13.json', 'w') as f:
    json.dump(topic13_cards, f, indent=2)

print(f"Generated {len(topic13_cards)} cards for Topic 13")
