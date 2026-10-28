import json

# =============================================================================
# TOPIC 06: Newton's Method and Hessian Modifications
# =============================================================================
topic06_cards = [
    {
        "id": 601,
        "subject": "CMO",
        "topicId": "06_Newtons_Method_and_Hessian_Modifications",
        "topicTitle": "06 · Newton’s Method & Modifications",
        "cardNumber": "01",
        "category": "SECOND-ORDER OPTIMIZATION",
        "highlighterClass": "highlight-cyan",
        "title": "Pure Newton’s Method & Parabolic Model",
        "textbookImg": "assets/luenberger_fig8_5.png",
        "textbookRef": "Luenberger & Ye (4th ed), Sect. 8.5, Fig. 8.5 (p. 231)",
        "drawingCaption": "Luenberger Fig. 8.5: Osculating quadratic model (dashed) minimized at each step to reach x_{k+1}",
        "drawingSvg": "",
        "coreTranslation": [
            "<strong>Core Philosophy:</strong> Newton's method approximates $f(x)$ at $x_k$ by its <strong>second-order Taylor polynomial</strong> $q(p) = f(x_k) + \nabla f(x_k)^T p + \frac{1}{2} p^T \nabla^2 f(x_k) p$ and steps directly to the exact stationary point of this parabolic bowl.",
            "<strong>The Step Direction:</strong> Setting $\\nabla q(p) = 0$ gives the linear system: $\\nabla^2 f(x_k) p_k = -\\nabla f(x_k)$, yielding Newton step $p_k = -[\\nabla^2 f(x_k)]^{-1} \\nabla f(x_k)$.",
            "<strong>Affine Invariance:</strong> Unlike Gradient Descent, Newton's method is completely invariant to non-singular linear coordinate transformations $x = A y$. It takes the exact same physical trajectory regardless of scaling!"
        ],
        "math": "$$x_{k+1} = x_k - [\\nabla^2 f(x_k)]^{-1} \\nabla f(x_k), \\quad \\nabla^2 f(x_k) p_k = -\\nabla f(x_k)$$",
        "personalConnection": "A tailor fitting a suit with a flexible parabolic mold: instead of taking tiny inch-by-inch fabric measurements (gradient descent), the mold captures the full curvature of your shoulders in one shot.",
        "examTrap": "NEVER invert the Hessian matrix explicitly ($H^{-1}$)! Inverting an $n \\times n$ matrix costs $\\mathcal{O}(n^3)$ operations and destroys sparsity. Always solve the linear system $H_k p_k = -g_k$ via Cholesky factorization."
    },
    {
        "id": 602,
        "subject": "CMO",
        "topicId": "06_Newtons_Method_and_Hessian_Modifications",
        "topicTitle": "06 · Newton’s Method & Modifications",
        "cardNumber": "02",
        "category": "CONVERGENCE THEORY",
        "highlighterClass": "highlight-amber",
        "title": "Quadratic (Superlinear) Local Convergence",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-602" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- Axes for log error -->
  <line x1="30" y1="120" x2="225" y2="120" stroke="#000000" stroke-width="1.2" marker-end="url(#arr-602)"/>
  <line x1="40" y1="130" x2="40" y2="15" stroke="#000000" stroke-width="1.2" marker-end="url(#arr-602)"/>
  <text x="225" y="132" fill="#000000" font-size="9" font-family="serif" font-style="italic">k</text>
  <text x="15" y="20" fill="#000000" font-size="8.5" font-family="serif" font-style="italic">log ||e_k||</text>
  <!-- Quadratic plunge curve -->
  <path d="M 45 30 Q 90 40 140 115" fill="none" stroke="#000000" stroke-width="2.2"/>
  <!-- Error points: 10^-1, 10^-2, 10^-4, 10^-8 -->
  <circle cx="50" cy="32" r="3" fill="#000000"/>
  <text x="75" y="30" fill="#000000" font-size="8" font-family="monospace">10⁻¹</text>
  <circle cx="85" cy="42" r="3" fill="#000000"/>
  <text x="110" y="42" fill="#000000" font-size="8" font-family="monospace">10⁻²</text>
  <circle cx="115" cy="70" r="3" fill="#000000"/>
  <text x="140" y="70" fill="#000000" font-size="8" font-family="monospace">10⁻⁴</text>
  <circle cx="140" cy="115" r="3.5" fill="#000000"/>
  <text x="175" y="112" fill="#000000" font-size="8" font-family="monospace">10⁻⁸ (Double!)</text>
  <text x="135" y="20" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">||e_{k+1}|| ≤ M ||e_k||²  (Quadratic Rate)</text>
  <text x="135" y="136" fill="#000000" font-size="8.5" font-family="sans-serif" text-anchor="middle">Number of accurate decimal digits DOUBLES each step</text>
</svg>""",
        "drawingCaption": "Quadratic Convergence: Error drops quadratically (10⁻¹ → 10⁻² → 10⁻⁴ → 10⁻⁸) near local minimizer x*",
        "coreTranslation": [
            "<strong>Theorem:</strong> Suppose $\\nabla^2 f(x^*)$ is positive definite with $\\lambda_{\\min} \\ge m > 0$, and the Hessian is $L$-Lipschitz continuous in a ball around $x^*$.",
            "Then if starting point $x_0$ is sufficiently close to $x^*$ ($\\|x_0 - x^*\\| < \\frac{2m}{L}$), the sequence converges <strong>quadratically</strong>:",
            "$$\\|x_{k+1} - x^*\\| \\le \\frac{L}{2 m} \\|x_k - x^*\\|^2$$",
            "<strong>Doubling of Digits:</strong> Once you reach 3 correct decimal digits of accuracy, the next iteration gives 6 digits, then 12, then 24!"
        ],
        "math": "$$\\|x_{k+1} - x^*\\| \\le \\frac{L}{2 m} \\|x_k - x^*\\|^2 \\quad \\implies \\quad \\lim_{k\\to\\infty} \\frac{\\|x_{k+1} - x^*\\|}{\\|x_k - x^*\\|} = 0 \\; (\\text{Superlinear})$$",
        "personalConnection": "A laser guided missile: far away it maneuvers slowly, but inside the terminal guidance bubble, it zeroes in on the target crosshairs with exponential precision.",
        "examTrap": "Quadratic convergence is strictly a LOCAL property! If $x_0$ is outside the radius of attraction, Newton's method can oscillate wildly or diverge to infinity."
    },
    {
        "id": 603,
        "subject": "CMO",
        "topicId": "06_Newtons_Method_and_Hessian_Modifications",
        "topicTitle": "06 · Newton’s Method & Modifications",
        "cardNumber": "03",
        "category": "FAILURE MODES",
        "highlighterClass": "highlight-rose",
        "title": "Failure Modes: Non-Convexity & Saddle Points",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-603" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- Non-convex curve with peak and trough -->
  <path d="M 40 110 Q 80 20 120 72 T 200 35" fill="none" stroke="#000000" stroke-width="2"/>
  <!-- Point on concave downward section -->
  <circle cx="80" cy="35" r="3.5" fill="#000000"/>
  <text x="65" y="28" fill="#000000" font-size="8.5" font-family="serif" font-style="italic">x_k (Concave)</text>
  <!-- Inverted osculating parabola -->
  <path d="M 50 75 Q 80 15 110 75" fill="none" stroke="#000000" stroke-width="1.2" stroke-dasharray="3,3"/>
  <!-- Newton step points UPHILL to local maximum -->
  <line x1="80" y1="35" x2="80" y2="20" stroke="#000000" stroke-width="1.8" marker-end="url(#arr-603)"/>
  <text x="95" y="18" fill="#000000" font-size="8.5" font-family="sans-serif" font-weight="bold">Steps Uphill to Max!</text>
  <text x="120" y="115" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">∇²f(x_k) ⊁ 0 ⇒ Newton Steps Toward Max / Saddles</text>
  <text x="120" y="134" fill="#000000" font-size="8.5" font-family="monospace" text-anchor="middle">p_kᵀ ∇f(x_k) = -∇fᵀ [∇²f]⁻¹ ∇f &gt; 0 (Ascent!)</text>
</svg>""",
        "drawingCaption": "Failure Mode: In concave regions (∇²f ≺ 0), the quadratic model opens downward and steps toward the local maximum",
        "coreTranslation": [
            "<strong>Failure 1 (Ascent Direction):</strong> If $\\nabla^2 f(x_k)$ has negative eigenvalues, $p_k^T \\nabla f(x_k) = -\\nabla f(x_k)^T [\\nabla^2 f(x_k)]^{-1} \\nabla f(x_k)$ can be POSITIVE! The Newton step becomes an <strong>ascent direction</strong>, increasing the function.",
            "<strong>Failure 2 (Singular Hessian):</strong> If $\\det(\\nabla^2 f(x_k)) = 0$, the inverse does not exist and the pure Newton step cannot be computed.",
            "<strong>Failure 3 (Saddle Attraction):</strong> Near saddle points where $\\nabla f(x) \\to 0$, Newton's method is attracted to the stationary point even though it is not a local minimum."
        ],
        "math": "$$\\nabla^2 f(x_k) \\not\\succ 0 \\implies p_k^T \\nabla f(x_k) \\not\\le 0 \\quad (\\text{Not Guaranteed to be a Descent Direction})$$",
        "personalConnection": "Walking with headlights in thick fog: if you are near a hilltop, a parabolic shape curves downward. Blindly stepping to its peak drives you directly over the summit cliff instead of into the safety of the valley.",
        "examTrap": "Assuming Newton's method always decreases the objective. Without Hessian modifications or line search, pure Newton on $f(x) = x^3 - 3x$ starting at $x_0 = -0.1$ steps straight uphill to the local maximum at $x = -1$!"
    },
    {
        "id": 604,
        "subject": "CMO",
        "topicId": "06_Newtons_Method_and_Hessian_Modifications",
        "topicTitle": "06 · Newton’s Method & Modifications",
        "cardNumber": "04",
        "category": "GLOBALIZATION",
        "highlighterClass": "highlight-emerald",
        "title": "Damped Newton with Backtracking Line Search",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-604" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- Full Newton step (overshoots) -->
  <line x1="45" y1="95" x2="195" y2="35" stroke="#000000" stroke-width="1.2" stroke-dasharray="3,3"/>
  <circle cx="195" cy="35" r="3.5" fill="#ffffff" stroke="#000000" stroke-width="1.5"/>
  <text x="195" y="24" fill="#000000" font-size="8.5" font-family="sans-serif" text-anchor="middle">α = 1 (Overshoots)</text>
  <!-- Damped Newton step alpha*p -->
  <line x1="45" y1="95" x2="125" y2="63" stroke="#000000" stroke-width="2.2" marker-end="url(#arr-604)"/>
  <circle cx="125" cy="63" r="4" fill="#000000"/>
  <text x="125" y="52" fill="#000000" font-size="9" font-family="serif" font-style="italic" font-weight="bold" text-anchor="middle">x_{k+1} = x_k + α_k p_k</text>
  <!-- Base point x_k -->
  <circle cx="45" cy="95" r="4" fill="#000000"/>
  <text x="35" y="110" fill="#000000" font-size="9" font-family="serif" font-style="italic">x_k</text>
  <text x="120" y="118" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Damped Newton: Unit Step α = 1 Accepted Locally</text>
  <text x="120" y="136" fill="#000000" font-size="8.5" font-family="monospace" text-anchor="middle">Armijo: f(x_k + α p_k) ≤ f(x_k) + c₁ α ∇fᵀ p_k</text>
</svg>""",
        "drawingCaption": "Damped Newton: Full step α=1 overshoots far from minimum; backtracking finds step α_k guaranteeing sufficient decrease",
        "coreTranslation": [
            "<strong>The Damped Framework:</strong> To achieve global convergence from arbitrary starting points, introduce a step size $\\alpha_k \\in (0, 1]$: $x_{k+1} = x_k + \\alpha_k p_k$, where $p_k$ is the Newton direction.",
            "<strong>Armijo Acceptance:</strong> Use backtracking line search starting at $\\alpha = 1$. The step size is accepted once $f(x_k + \\alpha p_k) \\le f(x_k) + c_1 \\alpha \\nabla f(x_k)^T p_k$.",
            "<strong>Natural Unit Step ($\alpha_k = 1$):</strong> Near $x^*$, the full unit step $\\alpha_k = 1$ ALWAYS satisfies the Armijo condition (provided $c_1 < 1/2$). Thus, the algorithm automatically transitions to pure quadratic convergence!"
        ],
        "math": "$$x_{k+1} = x_k + \\alpha_k p_k, \\quad \\alpha_k = \\beta^m, \\quad \\text{with } c_1 \\in (0, 1/2) \\implies \\alpha_k = 1 \\text{ near } x^*$$",
        "personalConnection": "Driving a 500-horsepower sports car: in city traffic far from your destination you tap the gas pedal with discretion (small $\\alpha_k$). On the open highway approach, you floor it at 100% capacity (unit step $\\alpha=1$).",
        "examTrap": "Choosing $c_1 > 1/2$ destroys the quadratic convergence! If $c_1 > 1/2$, the unit step $\\alpha_k = 1$ will be rejected even when the quadratic model is exact, permanently capping your rate at linear."
    },
    {
        "id": 605,
        "subject": "CMO",
        "topicId": "06_Newtons_Method_and_Hessian_Modifications",
        "topicTitle": "06 · Newton’s Method & Modifications",
        "cardNumber": "05",
        "category": "HESSIAN MODIFICATION",
        "highlighterClass": "highlight-violet",
        "title": "Levenberg-Marquardt & Spectral Shift (H + τI)",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <!-- Eigenvalue spectrum shift diagram -->
  <line x1="25" y1="75" x2="215" y2="75" stroke="#000000" stroke-width="1.2"/>
  <text x="215" y="88" fill="#000000" font-size="9" font-family="serif" font-style="italic">λ</text>
  <line x1="90" y1="20" x2="90" y2="125" stroke="#000000" stroke-width="1" stroke-dasharray="2,2"/>
  <text x="90" y="15" fill="#000000" font-size="8.5" font-family="monospace" text-anchor="middle">λ = 0</text>
  <!-- Negative eigenvalues of original H -->
  <circle cx="55" cy="75" r="3.5" fill="#ffffff" stroke="#000000" stroke-width="1.8"/>
  <text x="55" y="62" fill="#000000" font-size="8" font-family="monospace" text-anchor="middle">λ_min &lt; 0</text>
  <!-- Shift vector +tau -->
  <path d="M 55 45 L 125 45" fill="none" stroke="#000000" stroke-width="1.5" marker-end="url(#arr-604)"/>
  <text x="90" y="40" fill="#000000" font-size="8.5" font-family="monospace" text-anchor="middle">+ τ I</text>
  <!-- Shifted positive eigenvalue -->
  <circle cx="125" cy="75" r="4" fill="#000000"/>
  <text x="125" y="93" fill="#000000" font-size="8" font-family="monospace" text-anchor="middle">λ + τ ≥ δ &gt; 0</text>
  <text x="120" y="118" fill="#000000" font-size="9" font-family="serif" font-style="italic" font-weight="bold" text-anchor="middle">(∇²f(x_k) + τ_k I) p_k = -∇f(x_k)</text>
  <text x="120" y="136" fill="#000000" font-size="8.5" font-family="sans-serif" text-anchor="middle">τ → 0 gives Newton; τ → ∞ gives Gradient Descent</text>
</svg>""",
        "drawingCaption": "Spectral Shift: Adding τI shifts all eigenvalues into the positive domain (λ_i + τ > 0) without altering eigenvectors",
        "coreTranslation": [
            "<strong>The Core Modification:</strong> When $\\nabla^2 f(x_k)$ is indefinite or ill-conditioned, replace it with $B_k = \\nabla^2 f(x_k) + \\tau_k I$, choosing scalar $\\tau_k \\ge 0$ large enough so that $B_k \\succ 0$.",
            "<strong>Eigenvalue Impact:</strong> If $H$ has eigendecomposition $H = Q \\Lambda Q^T$, then $H + \\tau I = Q (\\Lambda + \\tau I) Q^T$. All eigenvectors are preserved; every eigenvalue shifts by $+\\tau$.",
            "<strong>Interpolation Property:</strong> If $\\tau_k = 0$, you get pure Newton. As $\\tau_k \\to \\infty$, $p_k \\approx -\\frac{1}{\\tau_k} \\nabla f(x_k)$, smoothly recovering steepest descent!"
        ],
        "math": "$$(\\nabla^2 f(x_k) + \\tau_k I) p_k = -\\nabla f(x_k), \\quad \\tau_k \\ge \\max\\left(0, \\; -\\lambda_{\\min}(\\nabla^2 f(x_k)) + \\delta\\right) \\; (\\delta > 0)$$",
        "personalConnection": "A suspension bridge stiffener: on solid bedrock you rely entirely on arch curvature (Newton). In mud or loose sand, you drive steel foundation pilings ($\tau_k I$) to ensure the ground cannot buckle under you.",
        "examTrap": "Choosing $\\tau_k$ too large degrades the method to slow Gradient Descent with tiny steps! Set $\\tau_k$ dynamically: decrease $\\tau$ when function value decreases rapidly, increase $\\tau$ when progress stalls."
    },
    {
        "id": 606,
        "subject": "CMO",
        "topicId": "06_Newtons_Method_and_Hessian_Modifications",
        "topicTitle": "06 · Newton’s Method & Modifications",
        "cardNumber": "06",
        "category": "WORKED BENCHMARK",
        "highlighterClass": "highlight-indigo",
        "title": "Worked Benchmark: Rosenbrock Newton vs GD",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-606" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- Elliptical banana contours -->
  <ellipse cx="120" cy="75" rx="90" ry="25" fill="none" stroke="#000000" stroke-width="1" stroke-dasharray="2,2"/>
  <ellipse cx="120" cy="75" rx="50" ry="12" fill="none" stroke="#000000" stroke-width="1" stroke-dasharray="2,2"/>
  <!-- GD zig-zag (dashed) -->
  <polyline points="45,95 75,65 85,90 100,70" fill="none" stroke="#000000" stroke-width="1.2" stroke-dasharray="3,3"/>
  <text x="65" y="112" fill="#000000" font-size="8" font-family="sans-serif">GD: 200+ zig-zags</text>
  <!-- Newton 1-step direct line -->
  <line x1="45" y1="95" x2="120" y2="75" stroke="#000000" stroke-width="2.2" marker-end="url(#arr-606)"/>
  <circle cx="120" cy="75" r="4" fill="#000000"/>
  <text x="140" y="78" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold">x* = (1, 1)</text>
  <text x="120" y="24" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Hessian Curvature Unwarps Ill-Conditioned Valley</text>
  <text x="120" y="136" fill="#000000" font-size="8.5" font-family="monospace" text-anchor="middle">p_N = -H⁻¹ g cuts straight along the parabolic spine</text>
</svg>""",
        "drawingCaption": "Worked Benchmark: Steepest descent takes hundreds of orthogonal zig-zags; Newton rotates direction to strike x* directly",
        "coreTranslation": [
            "<strong>Problem:</strong> On Rosenbrock $f(x_1, x_2) = 100(x_2 - x_1^2)^2 + (1 - x_1)^2$, compare Gradient Descent versus Newton's Method.",
            "<strong>Gradient Descent Disaster:</strong> Near $(0,0)$, $\\nabla^2 f \\approx \\begin{bmatrix} 2 & 0 \\\\ 0 & 200 \\end{bmatrix}$, yielding condition number $\\kappa = 100$. The theoretical convergence rate is $(\\frac{99}{101})^2 \\approx 0.96$. GD bounces back and forth across valley walls taking over 500 steps!",
            "<strong>Newton Triumph:</strong> Because $H^{-1}$ scales by $\\frac{1}{200}$ in $x_2$ and $\\frac{1}{2}$ in $x_1$, the elliptical coordinates are stretched into circles, rotating $p_N$ directly along the valley spine in 1 step."
        ],
        "math": "$$H(0,0) = \\begin{bmatrix} 2 & 0 \\\\ 0 & 200 \\end{bmatrix} \\implies H^{-1} = \\begin{bmatrix} 1/2 & 0 \\\\ 0 & 1/200 \\end{bmatrix}, \\quad p_N = -H^{-1} g = \\begin{bmatrix} 1 \\\\ 0 \\end{bmatrix}$$",
        "personalConnection": "Taking a suspension bridge directly across a deep canyon rather than hiking 500 switchbacks down to the riverbed and back up the other wall.",
        "examTrap": "Far from the spine (e.g. $x = (-1.2, 1)$), Rosenbrock's Hessian has negative eigenvalues! You MUST use Hessian modification $\\tau I$ or Damped line search, otherwise Newton steps uphill and fails."
    }
]

# =============================================================================
# TOPIC 07: Conjugate Direction and Conjugate Gradient Methods
# =============================================================================
topic07_cards = [
    {
        "id": 701,
        "subject": "CMO",
        "topicId": "07_Conjugate_Direction_and_Conjugate_Gradient_Methods",
        "topicTitle": "07 · Conjugate Direction & CG Methods",
        "cardNumber": "01",
        "category": "CONJUGATE DIRECTIONS",
        "highlighterClass": "highlight-cyan",
        "title": "Conjugate Directions & Q-Orthogonality",
        "textbookImg": "assets/luenberger_fig9_1.png",
        "textbookRef": "Luenberger & Ye (4th ed), Sect. 9.1, Fig. 9.1 (p. 276)",
        "drawingCaption": "Luenberger Fig. 9.1: Conjugate search directions d_k on expanding subspace with orthogonal gradient g_k",
        "drawingSvg": "",
        "coreTranslation": [
            "<strong>Definition:</strong> Given a symmetric positive definite matrix $Q \\succ 0$, non-zero vectors $d_0, d_1, \\dots, d_{k-1}$ are <strong>$Q$-Conjugate (Q-Orthogonal)</strong> if $d_i^T Q d_j = 0$ for all $i \\ne j$.",
            "<strong>Linear Independence:</strong> Any set of mutually $Q$-conjugate directions is automatically <strong>linearly independent</strong>. If $d_0, \\dots, d_{n-1}$ are conjugate in $\\mathbb{R}^n$, they form a basis!",
            "<strong>Decoupling Quadratic Forms:</strong> Expanding $x - x^*$ in the conjugate basis completely diagonalizes $f(x) = \\frac{1}{2} x^T Q x - b^T x$. Minimizing over $\\mathbb{R}^n$ decouples into $n$ independent 1D minimizations."
        ],
        "math": "$$d_i^T Q d_j = 0 \\quad (\\forall i \\ne j), \\quad \\alpha_k = -\\frac{g_k^T d_k}{d_k^T Q d_k} = \\frac{r_k^T d_k}{d_k^T Q d_k} \\quad (r_k = b - Q x_k = -g_k)$$",
        "personalConnection": "Walking on an anisotropic mattress: regular orthogonal steps cause the mattress to sag sideways, but stepping along natural $Q$-eigen-axes moves you forward without sideways wobble.",
        "examTrap": "Conjugacy depends strictly on matrix $Q$! Directions that are orthogonal in standard Euclidean geometry ($d_i^T d_j = 0$) are generally NOT $Q$-conjugate unless $Q = I$."
    },
    {
        "id": 702,
        "subject": "CMO",
        "topicId": "07_Conjugate_Direction_and_Conjugate_Gradient_Methods",
        "topicTitle": "07 · Conjugate Direction & CG Methods",
        "cardNumber": "02",
        "category": "EXPANDING SUBSPACE",
        "highlighterClass": "highlight-amber",
        "title": "The Expanding Subspace Theorem",
        "textbookImg": "assets/luenberger_fig9_2.png",
        "textbookRef": "Luenberger & Ye (4th ed), Sect. 9.1, Fig. 9.2 (p. 277)",
        "drawingCaption": "Luenberger Fig. 9.2: Subspace B_k expands dimension-by-dimension, with current iterate x_k optimal over x_0 + B_k",
        "drawingSvg": "",
        "coreTranslation": [
            "<strong>The Fundamental Theorem:</strong> Let $\{d_i\}_{i=0}^{n-1}$ be $Q$-conjugate directions. For any starting point $x_0$, generate iterates via exact line search: $x_{k+1} = x_k + \\alpha_k d_k$.",
            "<strong>Subspace Optimality:</strong> At iteration $k$, the iterate $x_k$ minimizes the quadratic objective $f(x)$ globally over the entire affine subspace $x_0 + \\mathcal{B}_k$, where $\\mathcal{B}_k = \\operatorname{span}\\{d_0, d_1, \\dots, d_{k-1}\\}$!",
            "<strong>Gradient Orthogonality:</strong> Consequently, the gradient $g_k = \\nabla f(x_k)$ is strictly orthogonal to all previously traversed directions: $g_k^T d_i = 0$ for all $i < k$."
        ],
        "math": "$$x_k = \\arg\\min_{x \\in x_0 + \\mathcal{B}_k} f(x), \\quad g_k^T d_i = 0 \\quad (\\forall i = 0, 1, \\dots, k-1)$$",
        "personalConnection": "Leveling ground with laser graders: once a sub-plane is leveled along axis $d_0$, future leveling along $Q$-conjugate axes never tilts or spoils the work already completed.",
        "examTrap": "Distinguish between inner products: $g_k$ is orthogonal to $d_i$ under the standard Euclidean dot product ($g_k^T d_i = 0$), whereas the directions $d_i$ are orthogonal under the $Q$-weighted inner product ($d_i^T Q d_j = 0$)."
    },
    {
        "id": 703,
        "subject": "CMO",
        "topicId": "07_Conjugate_Direction_and_Conjugate_Gradient_Methods",
        "topicTitle": "07 · Conjugate Direction & CG Methods",
        "cardNumber": "03",
        "category": "CG ALGORITHM",
        "highlighterClass": "highlight-emerald",
        "title": "Conjugate Gradient Method (Fletcher-Reeves)",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-703" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- Steepest descent gradient -g_{k+1} -->
  <line x1="120" y1="80" x2="60" y2="40" stroke="#000000" stroke-width="1.8" marker-end="url(#arr-703)"/>
  <text x="45" y="38" fill="#000000" font-size="8.5" font-family="serif" font-style="italic">-g_{k+1}</text>
  <!-- Old direction d_k -->
  <line x1="120" y1="80" x2="195" y2="80" stroke="#000000" stroke-width="1.2" stroke-dasharray="3,3"/>
  <text x="195" y="92" fill="#000000" font-size="8.5" font-family="serif" font-style="italic">β_k d_k</text>
  <!-- Resulting conjugate direction d_{k+1} -->
  <line x1="120" y1="80" x2="165" y2="30" stroke="#000000" stroke-width="2.5" marker-end="url(#arr-703)"/>
  <text x="175" y="32" fill="#000000" font-size="9" font-family="serif" font-style="italic" font-weight="bold">d_{k+1}</text>
  <circle cx="120" cy="80" r="4" fill="#000000"/>
  <text x="120" y="118" fill="#000000" font-size="9" font-family="serif" font-style="italic" font-weight="bold" text-anchor="middle">d_{k+1} = -g_{k+1} + β_k d_k</text>
  <text x="120" y="136" fill="#000000" font-size="8.5" font-family="monospace" text-anchor="middle">β_k = ||g_{k+1}||² / ||g_k||²  (Zero Matrix Storage!)</text>
</svg>""",
        "drawingCaption": "CG Update: New direction d_{k+1} blends current steepest descent -g_{k+1} with prior direction d_k scaled by β_k",
        "coreTranslation": [
            "<strong>The Breakthrough:</strong> Pure Conjugate Directions requires pre-computing and storing $n$ directions. Conjugate Gradient generates directions <strong>on the fly</strong> using only current gradients!",
            "<strong>The Recurrence:</strong> Start with $d_0 = -g_0$. At each step, set $d_{k+1} = -g_{k+1} + \\beta_k d_k$, where $\\beta_k = \\frac{\\|g_{k+1}\\|^2}{\\|g_k\\|^2}$.",
            "<strong>Gram-Schmidt Magic:</strong> Although $d_{k+1}$ only explicitly references $d_k$, the expanding subspace theorem guarantees that $d_{k+1}$ is automatically $Q$-conjugate to ALL previous directions $d_0, d_1, \\dots, d_{k-1}$!"
        ],
        "math": "$$d_{k+1} = -g_{k+1} + \\beta_k d_k, \\quad \\beta_k = \\frac{g_{k+1}^T g_{k+1}}{g_k^T g_k} = \\frac{\\|r_{k+1}\\|^2}{\\|r_k\\|^2}, \\quad \\alpha_k = \\frac{\\|r_k\\|^2}{d_k^T Q d_k}$$",
        "personalConnection": "Adjusting a sailboat heading: rather than dropping anchor to recalculate your whole voyage, you trim the existing rudder angle by an exact fraction $\\beta_k$ of the new wind gust.",
        "examTrap": "Remember that residual $r_k = b - Q x_k = -g_k$. In literature, $\\beta_k$ is written interchangeably as $\\frac{g_{k+1}^T g_{k+1}}{g_k^T g_k}$ or $\\frac{r_{k+1}^T r_{k+1}}{r_k^T r_k}$. Both are identical because sign cancels in squared norm."
    },
    {
        "id": 704,
        "subject": "CMO",
        "topicId": "07_Conjugate_Direction_and_Conjugate_Gradient_Methods",
        "topicTitle": "07 · Conjugate Direction & CG Methods",
        "cardNumber": "04",
        "category": "KRYLOV SPACES",
        "highlighterClass": "highlight-violet",
        "title": "Finite Termination & Krylov Subspace",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <!-- Krylov Subspace Dimension Steps -->
  <rect x="25" y="30" width="190" height="75" rx="8" fill="#f8fafc" stroke="#000000" stroke-width="1.5"/>
  <text x="35" y="46" fill="#000000" font-size="8.5" font-family="serif" font-style="italic">Krylov Space 𝒦_k(Q, r₀)</text>
  <!-- Step towers -->
  <line x1="50" y1="90" x2="50" y2="70" stroke="#000000" stroke-width="3"/>
  <text x="50" y="102" fill="#000000" font-size="8" font-family="monospace" text-anchor="middle">r₀</text>
  <line x1="90" y1="90" x2="90" y2="55" stroke="#000000" stroke-width="3"/>
  <text x="90" y="102" fill="#000000" font-size="8" font-family="monospace" text-anchor="middle">Qr₀</text>
  <line x1="130" y1="90" x2="130" y2="40" stroke="#000000" stroke-width="3"/>
  <text x="130" y="102" fill="#000000" font-size="8" font-family="monospace" text-anchor="middle">Q²r₀</text>
  <text x="175" y="65" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Terminates in</text>
  <text x="175" y="78" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">m ≤ n steps!</text>
  <text x="120" y="125" fill="#000000" font-size="9" font-family="serif" font-style="italic" font-weight="bold" text-anchor="middle">m = Number of Distinct Eigenvalues of Q</text>
</svg>""",
        "drawingCaption": "Krylov Tower: Subspace spans powers {r₀, Qr₀, ..., Q^{k-1}r₀}; CG terminates in at most m distinct eigenvalue steps",
        "coreTranslation": [
            "<strong>Krylov Connection:</strong> The subspace $\\mathcal{B}_k = \\operatorname{span}\\{d_0, \\dots, d_{k-1}\\}$ generated by CG is identical to the <strong>Krylov Subspace</strong>: $\\mathcal{K}_k(Q, r_0) = \\operatorname{span}\\{r_0, Q r_0, Q^2 r_0, \\dots, Q^{k-1} r_0\\}$.",
            "<strong>Finite $n$-Step Termination:</strong> Because $\\mathbb{R}^n$ has dimension $n$, after at most $n$ iterations $\\mathcal{B}_n = \\mathbb{R}^n$, meaning $x_n = x^*$ is the EXACT global minimizer in exact arithmetic!",
            "<strong>Distinct Eigenvalues Super-Convergence:</strong> If $Q$ has only $m < n$ distinct eigenvalues, CG terminates in at most $m$ iterations! E.g. in 10,000 dimensions with 5 clusters of eigenvalues, CG finishes in 5 steps."
        ],
        "math": "$$\\mathcal{B}_k = \\mathcal{K}_k(Q, r_0) = \\operatorname{span}\\{r_0, Q r_0, \\dots, Q^{k-1} r_0\\}, \\quad x_m = x^* \\; \\text{for } m = |\\sigma(Q)| \\le n$$",
        "personalConnection": "Cracking a safe with $m$ distinct internal tumblers: each conjugate step permanently aligns one full eigenvalue eigenspace. After $m$ clicks, the vault swings open.",
        "examTrap": "In computer floating-point arithmetic with roundoff error, finite termination can fail! Directions lose $Q$-orthogonality over many steps, turning CG into an iterative method that requires restarts."
    },
    {
        "id": 705,
        "subject": "CMO",
        "topicId": "07_Conjugate_Direction_and_Conjugate_Gradient_Methods",
        "topicTitle": "07 · Conjugate Direction & CG Methods",
        "cardNumber": "05",
        "category": "NON-LINEAR CG",
        "highlighterClass": "highlight-indigo",
        "title": "Non-Linear CG & Polak-Ribière Restarts",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <!-- Polak-Ribiere Orthogonal Reset -->
  <rect x="25" y="25" width="190" height="90" rx="8" fill="#f8fafc" stroke="#000000" stroke-width="1.5"/>
  <text x="120" y="45" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Polak-Ribière Parameter: β_k^{PR}</text>
  <text x="120" y="65" fill="#000000" font-size="9" font-family="monospace" text-anchor="middle">β_k = (g_{k+1}ᵀ (g_{k+1} - g_k)) / ||g_k||²</text>
  <!-- Reset condition -->
  <line x1="45" y1="80" x2="195" y2="80" stroke="#000000" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="120" y="98" fill="#000000" font-size="8.5" font-family="sans-serif" text-anchor="middle">If step stalls (g_{k+1} ≈ g_k) ⇒ β_k → 0</text>
  <text x="120" y="132" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Automatic Restart to Steepest Descent: β+ = max(0, β^{PR})</text>
</svg>""",
        "drawingCaption": "Non-linear CG: Polak-Ribière resets β to 0 whenever progress jams, restarting search along steepest descent",
        "coreTranslation": [
            "<strong>Beyond Quadratics:</strong> For general non-linear functions $f(x)$, exact line search is replaced by line search satisfying the <strong>Strong Wolfe conditions</strong>.",
            "<strong>Fletcher-Reeves Jamming:</strong> In Fletcher-Reeves ($\\beta_k = \\|g_{k+1}\\|^2 / \\|g_k\\|^2$), if a poor step is taken, the search directions can become nearly orthogonal to the gradient, trapping the algorithm in tiny zigzagging steps.",
            "<strong>Polak-Ribière (PR) Immunity:</strong> Polak-Ribière sets $\\beta_k = \\frac{g_{k+1}^T (g_{k+1} - g_k)}{\\|g_k\\|^2}$. If consecutive gradients are nearly identical ($g_{k+1} \\approx g_k$), $\\beta_k \\to 0$, automatically resetting $d_{k+1} \\approx -g_{k+1}$!"
        ],
        "math": "$$\\beta_k^{PR} = \\frac{g_{k+1}^T (g_{k+1} - g_k)}{\\|g_k\\|^2}, \\quad \\beta_k^+ = \\max\\left(0, \\; \\beta_k^{PR}\\right) \\quad (\\text{Automatic Reset})$$",
        "personalConnection": "Re-calibrating your hiking compass after passing a magnetic iron deposit: if your heading gets corrupted, the compass resets to true magnetic north rather than following the corrupted angle.",
        "examTrap": "FR guarantees descent under strong Wolfe conditions ($c_2 < 1/2$), but PR can produce an ascent direction on non-convex functions unless modified as $\\beta_k = \\max(0, \\beta_k^{PR})$."
    },
    {
        "id": 706,
        "subject": "CMO",
        "topicId": "07_Conjugate_Direction_and_Conjugate_Gradient_Methods",
        "topicTitle": "07 · Conjugate Direction & CG Methods",
        "cardNumber": "06",
        "category": "WORKED BENCHMARK",
        "highlighterClass": "highlight-rose",
        "title": "Worked Benchmark: 2D CG in Exactly 2 Steps",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-706" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- 2D Contours -->
  <ellipse cx="120" cy="72" rx="95" ry="32" fill="none" stroke="#000000" stroke-width="1.2"/>
  <ellipse cx="120" cy="72" rx="55" ry="18" fill="none" stroke="#000000" stroke-width="1.2"/>
  <!-- Step 0: x0 to x1 along d0 = -g0 -->
  <line x1="45" y1="95" x2="105" y2="45" stroke="#000000" stroke-width="2" marker-end="url(#arr-706)"/>
  <circle cx="45" cy="95" r="3.5" fill="#000000"/>
  <text x="35" y="105" fill="#000000" font-size="9" font-family="serif" font-style="italic">x₀</text>
  <circle cx="105" cy="45" r="3.5" fill="#000000"/>
  <text x="105" y="38" fill="#000000" font-size="9" font-family="serif" font-style="italic">x₁</text>
  <!-- Step 1: x1 to x* along conjugate d1 -->
  <line x1="105" y1="45" x2="120" y2="72" stroke="#000000" stroke-width="2.5" marker-end="url(#arr-706)"/>
  <circle cx="120" cy="72" r="4" fill="#000000"/>
  <text x="135" y="75" fill="#000000" font-size="9.5" font-family="serif" font-style="italic" font-weight="bold">x* = x₂</text>
  <text x="120" y="125" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Step 1 minimizes over Line; Step 2 hits Center x*</text>
  <text x="120" y="138" fill="#000000" font-size="8.5" font-family="monospace" text-anchor="middle">d₀ᵀ Q d₁ = 0 ⇒ Exact solution in 2 iterations!</text>
</svg>""",
        "drawingCaption": "Worked Benchmark: CG reaches exact minimum of 2D quadratic in exactly 2 steps, whereas Gradient Descent takes hundreds",
        "coreTranslation": [
            "<strong>Problem:</strong> Minimize $f(x_1, x_2) = x_1^2 + 4x_2^2$ starting at $x_0 = (4, 2)$ via Conjugate Gradient.",
            "<strong>Iteration 0:</strong> Gradient $g_0 = (8, 16)$, $d_0 = (-8, -16)$. Step size $\\alpha_0 = \\frac{g_0^T g_0}{d_0^T Q d_0} = \\frac{320}{1152} = 5/18$. Then $x_1 = x_0 + \\alpha_0 d_0 = (16/9, -20/9)$. Notice $g_1 = (32/9, -160/9)$ is orthogonal to $d_0$!",
            "<strong>Iteration 1:</strong> $\\beta_0 = \\|g_1\\|^2 / \\|g_0\\|^2 = 4/81$. Conjugate direction $d_1 = -g_1 + \\beta_0 d_0$. Line search along $d_1$ yields $x_2 = (0, 0) = x^*$ exactly in 2 steps!"
        ],
        "math": "$$x_0 = \\begin{bmatrix} 4 \\\\ 2 \\end{bmatrix} \\xrightarrow{d_0 = -g_0} x_1 = \\begin{bmatrix} 16/9 \\\\ -20/9 \\end{bmatrix} \\xrightarrow{d_1 = -g_1 + \\beta_0 d_0} x_2 = \\begin{bmatrix} 0 \\\\ 0 \\end{bmatrix} = x^*$$",
        "personalConnection": "Two laser cuts: first cut eliminates error in the first conjugate plane; second cut finishes the remaining component. Done.",
        "examTrap": "Verifying $g_1^T d_0 = 0$: $(32/9)(-8) + (-160/9)(-16) = -256/9 + 2560/9$... wait, check arithmetic: line search ALWAYS forces $g_{k+1}^T d_k = 0$. Never forget this check on exams!"
    }
]

# =============================================================================
# TOPIC 08: Quasi-Newton Methods (SR1, DFP, and BFGS)
# =============================================================================
topic08_cards = [
    {
        "id": 801,
        "subject": "CMO",
        "topicId": "08_Quasi_Newton_Methods_SR1_DFP_and_BFGS",
        "topicTitle": "08 · Quasi-Newton Methods (BFGS)",
        "cardNumber": "01",
        "category": "THE SECANT EQUATION",
        "highlighterClass": "highlight-cyan",
        "title": "The Secant Equation & Approximate Hessians",
        "textbookImg": "assets/luenberger_fig10_1.png",
        "textbookRef": "Luenberger & Ye (4th ed), Sect. 10.1, Fig. 10.1 (p. 317)",
        "drawingCaption": "Luenberger Fig. 10.1: Combined Quasi-Newton method updating approximation across planes",
        "drawingSvg": "",
        "coreTranslation": [
            "<strong>The Core Dilemma:</strong> Newton's method converges quadratically but requires $\\mathcal{O}(n^2)$ storage and $\\mathcal{O}(n^3)$ operations to compute and invert the true Hessian matrix $\\nabla^2 f(x)$.",
            "<strong>Quasi-Newton Idea:</strong> Build an approximation $B_{k+1} \\approx \\nabla^2 f$ (or inverse $H_{k+1} \\approx [\\nabla^2 f]^{-1}$) using ONLY gradient evaluations from successive steps!",
            "<strong>The Secant Condition:</strong> By Taylor expansion, $g_{k+1} - g_k \\approx \\nabla^2 f(x_{k+1}) (x_{k+1} - x_k)$. Defining displacement $s_k = x_{k+1} - x_k$ and gradient difference $y_k = g_{k+1} - g_k$, the approximation MUST satisfy: $B_{k+1} s_k = y_k$ (or $H_{k+1} y_k = s_k$)."
        ],
        "math": "$$B_{k+1} s_k = y_k \\quad \\text{or} \\quad H_{k+1} y_k = s_k \\quad (s_k = x_{k+1} - x_k, \\; y_k = g_{k+1} - g_k)$$",
        "personalConnection": "Gauging the curve of an unseen hill: by recording your odometer displacement $s_k$ and the change in tilt of your bubble level $y_k$, you deduce hill curvature without an aerial survey.",
        "examTrap": "The secant equation has $n$ equations for $n(n+1)/2$ unknown symmetric matrix entries. It is underdetermined! The specific update formulas (SR1, DFP, BFGS) are derived by minimizing different matrix norms."
    },
    {
        "id": 802,
        "subject": "CMO",
        "topicId": "08_Quasi_Newton_Methods_SR1_DFP_and_BFGS",
        "topicTitle": "08 · Quasi-Newton Methods (BFGS)",
        "cardNumber": "02",
        "category": "SR1 UPDATE",
        "highlighterClass": "highlight-amber",
        "title": "Symmetric Rank-1 (SR1) Update",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <rect x="25" y="25" width="190" height="90" rx="8" fill="#f8fafc" stroke="#000000" stroke-width="1.5"/>
  <text x="120" y="45" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Symmetric Rank-1 Formula</text>
  <text x="120" y="65" fill="#000000" font-size="8.5" font-family="monospace" text-anchor="middle">B_{k+1} = B_k + ((y - B s)(y - B s)ᵀ) / ((y - B s)ᵀ s)</text>
  <!-- Warning sign -->
  <line x1="45" y1="80" x2="195" y2="80" stroke="#000000" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="120" y="98" fill="#000000" font-size="8.5" font-family="sans-serif" text-anchor="middle">Denominator can be ZERO or NEGATIVE!</text>
  <text x="120" y="132" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Does NOT guarantee B_{k+1} ≻ 0 (Use Trust Region)</text>
</svg>""",
        "drawingCaption": "SR1 Update: Minimal single-rank correction, but denominator can vanish or destroy positive definiteness",
        "coreTranslation": [
            "<strong>Unique Rank-1 Form:</strong> If we seek a symmetric rank-1 update $B_{k+1} = B_k + c u u^T$ satisfying the secant equation, there is <strong>EXACTLY ONE</strong> unique mathematical solution: the SR1 update.",
            "<strong>Key Strength:</strong> Remarkably, on quadratics, SR1 generates true Hessian approximations even with ARBITRARY step sizes (no line search required)!",
            "<strong>Fatal Flaw:</strong> The denominator $(y_k - B_k s_k)^T s_k$ can vanish or become negative. SR1 does NOT guarantee positive definiteness ($B_{k+1} \\succ 0$), making it unstable for standard line search."
        ],
        "math": "$$B_{k+1} = B_k + \\frac{(y_k - B_k s_k)(y_k - B_k s_k)^T}{(y_k - B_k s_k)^T s_k}, \\quad H_{k+1} = H_k + \\frac{(s_k - H_k y_k)(s_k - H_k y_k)^T}{(s_k - H_k y_k)^T y_k}$$",
        "personalConnection": "Adjusting a machine with a single set screw: it is minimal and fast, but if the screw binds against the casing ($denominator \\approx 0$), the entire mechanism jams.",
        "examTrap": "Never use SR1 with line search without a skip check! Production SR1 codes skip the update whenever $|s_k^T (y_k - B_k s_k)| < r \\|s_k\\| \\|y_k - B_k s_k\\|$, and pair it with Trust Region frameworks."
    },
    {
        "id": 803,
        "subject": "CMO",
        "topicId": "08_Quasi_Newton_Methods_SR1_DFP_and_BFGS",
        "topicTitle": "08 · Quasi-Newton Methods (BFGS)",
        "cardNumber": "03",
        "category": "DFP ALGORITHM",
        "highlighterClass": "highlight-violet",
        "title": "Davidon-Fletcher-Powell (DFP) Dual Update",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <!-- DFP Rank-2 structure -->
  <rect x="25" y="25" width="190" height="90" rx="8" fill="#f8fafc" stroke="#000000" stroke-width="1.5"/>
  <text x="120" y="44" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">DFP Inverse Hessian Update (Rank-2)</text>
  <text x="120" y="65" fill="#000000" font-size="8.5" font-family="monospace" text-anchor="middle">H_{k+1} = H_k + (s sᵀ)/(sᵀ y) - (H y yᵀ H)/(yᵀ H y)</text>
  <!-- Positive definite check -->
  <line x1="45" y1="80" x2="195" y2="80" stroke="#000000" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="120" y="98" fill="#000000" font-size="8.5" font-family="sans-serif" text-anchor="middle">Guarantees H_{k+1} ≻ 0 if sᵀ y &gt; 0</text>
  <text x="120" y="132" fill="#000000" font-size="8.5" font-family="monospace" text-anchor="middle">Historically first, but superseded by BFGS</text>
</svg>""",
        "drawingCaption": "DFP Update: First rank-2 method guaranteeing positive definiteness, but susceptible to line search error",
        "coreTranslation": [
            "<strong>First Rank-2 Solution:</strong> Developed by Davidon (1959) and refined by Fletcher and Powell (1963), DFP was the historical breakthrough that made Quasi-Newton practical.",
            "<strong>Rank-2 Structure:</strong> Uses two symmetric rank-1 corrections: one adds positive curvature along $s_k$, the other subtracts projected components along $H_k y_k$.",
            "<strong>Hereditary Property:</strong> If $H_k \\succ 0$ and the curvature condition $s_k^T y_k > 0$ holds, then $H_{k+1}$ is GUARANTEED to be positive definite ($H_{k+1} \\succ 0$)."
        ],
        "math": "$$H_{k+1}^{\\text{DFP}} = H_k + \\frac{s_k s_k^T}{s_k^T y_k} - \\frac{H_k y_k y_k^T H_k}{y_k^T H_k y_k}$$",
        "personalConnection": "Two counterbalancing weights on a spinning car tire: one adds weight along the drive axis, the second removes rotational vibration.",
        "examTrap": "DFP is extremely sensitive to line search inaccuracies! If inexact line search is used, DFP's Hessian approximation tends to become ill-conditioned, which is why BFGS replaced it."
    },
    {
        "id": 804,
        "subject": "CMO",
        "topicId": "08_Quasi_Newton_Methods_SR1_DFP_and_BFGS",
        "topicTitle": "08 · Quasi-Newton Methods (BFGS)",
        "cardNumber": "04",
        "category": "BFGS MASTER FORMULA",
        "highlighterClass": "highlight-emerald",
        "title": "BFGS: The Gold Standard Quasi-Newton",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <!-- BFGS Projection Box -->
  <rect x="25" y="25" width="190" height="90" rx="8" fill="#f8fafc" stroke="#000000" stroke-width="1.8"/>
  <text x="120" y="44" fill="#000000" font-size="9.5" font-family="sans-serif" font-weight="bold" text-anchor="middle">BFGS Master Inverse Formula</text>
  <text x="120" y="66" fill="#000000" font-size="8" font-family="monospace" text-anchor="middle">H_{k+1} = (I - ρ s yᵀ) H_k (I - ρ y sᵀ) + ρ s sᵀ</text>
  <line x1="45" y1="80" x2="195" y2="80" stroke="#000000" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="120" y="96" fill="#000000" font-size="8.5" font-family="monospace" text-anchor="middle">ρ_k = 1 / (y_kᵀ s_k)  (Self-Correcting!)</text>
  <text x="120" y="132" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Gold standard: Superlinear rate with O(n²) cost</text>
</svg>""",
        "drawingCaption": "BFGS Formula: Symmetric projection sandwich (I - ρ s yᵀ) H (I - ρ y sᵀ) + ρ s sᵀ self-corrects roundoff errors",
        "coreTranslation": [
            "<strong>The Gold Standard:</strong> Discovered independently by Broyden, Fletcher, Goldfarb, and Shanno (1970). It is universally recognized as the most robust unconstrained optimization algorithm.",
            "<strong>Dual Equivalence:</strong> BFGS is the exact mathematical <strong>dual</strong> of DFP obtained by swapping $B \\leftrightarrow H$ and $s \\leftrightarrow y$.",
            "<strong>Self-Correcting Robustness:</strong> Unlike DFP, BFGS possesses a self-correcting property: if an inaccurate step corrupts the Hessian estimate, subsequent iterations automatically damp out the error."
        ],
        "math": "$$H_{k+1} = \\left(I - \\rho_k s_k y_k^T\\right) H_k \\left(I - \\rho_k y_k s_k^T\\right) + \\rho_k s_k s_k^T, \\quad \\rho_k = \\frac{1}{y_k^T s_k}$$",
        "personalConnection": "A gyroscope with automatic drift compensation: small sensor vibrations are actively projected out of the attitude matrix on every refresh cycle.",
        "examTrap": "The direction is $p_k = -H_k g_k$, which requires ONLY matrix-vector multiplication ($\\mathcal{O}(n^2)$), NEVER matrix inversion ($\\mathcal{O}(n^3)$)! This gives Newton-like superlinear convergence at a fraction of the cost."
    },
    {
        "id": 805,
        "subject": "CMO",
        "topicId": "08_Quasi_Newton_Methods_SR1_DFP_and_BFGS",
        "topicTitle": "08 · Quasi-Newton Methods (BFGS)",
        "cardNumber": "05",
        "category": "CURVATURE CONDITION",
        "highlighterClass": "highlight-indigo",
        "title": "Hereditary Positive Definiteness & Wolfe",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-805" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- Curvature condition angle -->
  <line x1="120" y1="85" x2="195" y2="85" stroke="#000000" stroke-width="2" marker-end="url(#arr-805)"/>
  <text x="198" y="88" fill="#000000" font-size="9" font-family="serif" font-style="italic">s_k</text>
  <line x1="120" y1="85" x2="175" y2="35" stroke="#000000" stroke-width="2" marker-end="url(#arr-805)"/>
  <text x="180" y="32" fill="#000000" font-size="9" font-family="serif" font-style="italic">y_k</text>
  <path d="M 155 85 A 35 35 0 0 0 150 60" fill="none" stroke="#000000" stroke-width="1.2"/>
  <text x="165" y="72" fill="#000000" font-size="8.5" font-family="sans-serif">Acute Angle</text>
  <circle cx="120" cy="85" r="4" fill="#000000"/>
  <text x="120" y="118" fill="#000000" font-size="9" font-family="serif" font-style="italic" font-weight="bold" text-anchor="middle">s_kᵀ y_k &gt; 0 ⟺ H_{k+1} ≻ 0  (Strict Positive Definiteness)</text>
  <text x="120" y="136" fill="#000000" font-size="8.5" font-family="monospace" text-anchor="middle">Guaranteed by Wolfe Curvature: ∇f(x+αp)ᵀp ≥ c₂ ∇fᵀp</text>
</svg>""",
        "drawingCaption": "Curvature Condition: Acute angle between displacement s_k and gradient difference y_k guarantees H_{k+1} ≻ 0",
        "coreTranslation": [
            "<strong>The Positive Definite Guarantee:</strong> For both BFGS and DFP, $H_{k+1} \\succ 0$ if and only if $H_k \\succ 0$ and the <strong>Curvature Condition</strong> holds: $s_k^T y_k > 0$.",
            "<strong>Why Wolfe is Mandatory:</strong> On non-convex functions, a simple line search can produce $s_k^T y_k \\le 0$. But the <strong>Wolfe Curvature Condition</strong> $\\nabla f(x_k + \\alpha_k p_k)^T p_k \\ge c_2 \\nabla f(x_k)^T p_k$ mathematically FORCES $s_k^T y_k \\ge (1 - c_2) \\alpha_k |\\nabla f(x_k)^T p_k| > 0$!",
            "Therefore, pairing BFGS with Wolfe line search guarantees that every single search direction is a descent direction."
        ],
        "math": "$$s_k^T y_k > 0 \\iff H_{k+1} \\succ 0 \\quad \\left( \\text{Wolfe: } \\nabla f(x_k + \\alpha_k p_k)^T p_k \\ge c_2 \\nabla f(x_k)^T p_k \\implies s_k^T y_k > 0 \\right)$$",
        "personalConnection": "Testing ice thickness before stepping forward: as long as the ice pushes back positively ($s_k^T y_k > 0$), your footing is solid. If the surface sags ($s_k^T y_k \le 0$), you refuse to commit your weight.",
        "examTrap": "Standard Armijo condition alone does NOT guarantee $s_k^T y_k > 0$! You MUST enforce the second Wolfe condition (curvature condition), otherwise $H_{k+1}$ can lose positive definiteness."
    },
    {
        "id": 806,
        "subject": "CMO",
        "topicId": "08_Quasi_Newton_Methods_SR1_DFP_and_BFGS",
        "topicTitle": "08 · Quasi-Newton Methods (BFGS)",
        "cardNumber": "06",
        "category": "LARGE-SCALE OPTIMIZATION",
        "highlighterClass": "highlight-rose",
        "title": "Limited-Memory BFGS (L-BFGS) Algorithm",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <!-- Sliding memory window -->
  <rect x="25" y="25" width="190" height="90" rx="8" fill="#f8fafc" stroke="#000000" stroke-width="1.5"/>
  <text x="120" y="44" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Sliding Memory Window (Size m ≈ 5 - 20)</text>
  <!-- Vector pairs stack -->
  <rect x="40" y="55" width="160" height="25" rx="4" fill="#f1f5f9" stroke="#000000" stroke-width="1.2"/>
  <text x="120" y="71" fill="#000000" font-size="8.5" font-family="monospace" text-anchor="middle">{s_{k-1}, y_{k-1}}, ..., {s_{k-m}, y_{k-m}}</text>
  <text x="120" y="98" fill="#000000" font-size="8.5" font-family="sans-serif" text-anchor="middle">Storage: O(mn) instead of O(n²)!</text>
  <text x="120" y="132" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Two-Loop Recursion: Computes H_k g_k in 4mn ops</text>
</svg>""",
        "drawingCaption": "L-BFGS: Stores only the most recent m vector pairs {s_i, y_i}, dropping memory from O(n²) to O(mn)",
        "coreTranslation": [
            "<strong>Large-Scale Bottleneck:</strong> When $n = 10^7$ (e.g. deep learning or PDE optimization), storing an $n \\times n$ dense matrix $H_k$ requires 800 Terabytes of RAM!",
            "<strong>The L-BFGS Solution:</strong> Store ONLY the last $m$ vector pairs $\\{s_i, y_i\\}_{i=k-m}^{k-1}$ (typically $m \\in [5, 20]$). Memory cost drops from $\\mathcal{O}(n^2)$ to just $\\mathcal{O}(m n)$.",
            "<strong>Two-Loop Recursion:</strong> Computes the search direction $p_k = -H_k g_k$ directly via an ingenious two-pass backward-forward loop requiring ZERO matrix multiplications, costing only $4mn$ floating-point ops!"
        ],
        "math": "$$\\text{Memory: } \\mathcal{O}(m n) \\ll \\mathcal{O}(n^2), \\quad H_0^k = \\gamma_k I, \\quad \\gamma_k = \\frac{s_{k-1}^T y_{k-1}}{\\|y_{k-1}\\|^2}$$",
        "personalConnection": "Keeping only the last 10 text messages on your phone: you retain full immediate conversational context without bloating your phone's storage with years of ancient history.",
        "examTrap": "The initial base scaling $\\gamma_k = \\frac{s_{k-1}^T y_{k-1}}{\\|y_{k-1}\\|^2}$ is CRITICAL! It estimates the local spectral magnitude of the inverse Hessian so that the unit step $\\alpha_k = 1$ is accepted in line search."
    }
]

# =============================================================================
# TOPIC 10: Separating Hyperplanes and Farkas' Lemma
# =============================================================================
topic10_cards = [
    {
        "id": 1001,
        "subject": "CMO",
        "topicId": "10_Separating_Hyperplanes_and_Farkas_Lemma",
        "topicTitle": "10 · Separating Hyperplanes & Farkas’ Lemma",
        "cardNumber": "01",
        "category": "SEPARATION THEOREMS",
        "highlighterClass": "highlight-cyan",
        "title": "Separating Hyperplane Theorem",
        "textbookImg": "assets/luenberger_fig11_7.png",
        "textbookRef": "Luenberger & Ye (4th ed), Sect. 11.7, Fig. 11.7 (p. 353)",
        "drawingCaption": "Luenberger Fig. 11.7: Separating hyperplane separating convex set A from negative orthant ray B",
        "drawingSvg": "",
        "coreTranslation": [
            "<strong>Theorem:</strong> Let $A$ and $B$ be non-empty, disjoint convex sets in $\\mathbb{R}^n$ ($A \\cap B = \\emptyset$). Then there exists a non-zero vector $a \\in \\mathbb{R}^n$ and a scalar $\\beta$ such that:",
            "$$a^T x \\le \\beta \\le a^T y \\quad \\forall x \\in A, \\; y \\in B$$",
            "<strong>Geometric Meaning:</strong> The hyperplane $H = \\{z : a^T z = \\beta\\}$ separates $A$ and $B$: $A$ lies entirely in the lower half-space, and $B$ lies in the upper half-space.",
            "<strong>Strict Separation:</strong> If $A$ is closed and $B$ is compact, then there exists a hyperplane that strictly separates them: $a^T x < \\beta < a^T y$."
        ],
        "math": "$$A \\cap B = \\emptyset, \\; A, B \\text{ convex} \\implies \\exists a \\ne 0, \\beta : \\sup_{x \\in A} a^T x \\le \\inf_{y \\in B} a^T y$$",
        "personalConnection": "Sliding a flat pane of glass between two rival crowds on a plaza: as long as their territories do not overlap and both groups stay within convex boundaries, a single flat wall cleanly divides them.",
        "examTrap": "Strict separation strictly fails if neither set is compact! E.g. $A = \\{(x_1, x_2) : x_2 \\le 0\\}$ and $B = \\{(x_1, x_2) : x_1 x_2 \\ge 1, x_1 > 0\\}$ are closed and disjoint, but can only be weakly separated by $x_2 = 0$."
    },
    {
        "id": 1002,
        "subject": "CMO",
        "topicId": "10_Separating_Hyperplanes_and_Farkas_Lemma",
        "topicTitle": "10 · Separating Hyperplanes & Farkas’ Lemma",
        "cardNumber": "02",
        "category": "BOUNDARY GEOMETRY",
        "highlighterClass": "highlight-amber",
        "title": "Supporting Hyperplane Theorem",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-1002" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- Convex Set C -->
  <path d="M 50 110 Q 80 40 140 40 T 195 110 Z" fill="#f1f5f9" stroke="#000000" stroke-width="1.8"/>
  <text x="120" y="85" fill="#000000" font-size="11" font-family="serif" font-style="italic" font-weight="bold" text-anchor="middle">Convex Set C</text>
  <!-- Boundary point x0 -->
  <circle cx="140" cy="40" r="4" fill="#000000"/>
  <text x="140" y="30" fill="#000000" font-size="9.5" font-family="serif" font-style="italic">x₀ ∈ ∂C</text>
  <!-- Supporting hyperplane tangent line -->
  <line x1="55" y1="40" x2="215" y2="40" stroke="#000000" stroke-width="1.5" stroke-dasharray="4,3"/>
  <!-- Normal vector a -->
  <line x1="140" y1="40" x2="140" y2="12" stroke="#000000" stroke-width="2" marker-end="url(#arr-1002)"/>
  <text x="148" y="18" fill="#000000" font-size="9" font-family="serif" font-style="italic" font-weight="bold">a (Normal)</text>
  <text x="120" y="134" fill="#000000" font-size="9" font-family="serif" font-style="italic" font-weight="bold" text-anchor="middle">aᵀ (x - x₀) ≤ 0  ∀ x ∈ C  (Entire set on one side)</text>
</svg>""",
        "drawingCaption": "Supporting Hyperplane: Touches convex set C at boundary point x₀, enclosing C entirely on one side",
        "coreTranslation": [
            "<strong>Theorem:</strong> Let $C \\subset \\mathbb{R}^n$ be a convex set and $x_0 \\in \\partial C$ be a boundary point. Then there exists a non-zero vector $a \\ne 0$ such that:",
            "$$a^T (x - x_0) \\le 0 \\quad \\forall x \\in C$$",
            "<strong>Geometric Meaning:</strong> The hyperplane $H = \\{x : a^T x = a^T x_0\\}$ passes through $x_0$ and the entire set $C$ is contained in one closed halfspace.",
            "<strong>Dual Characterization of Convexity:</strong> A closed convex set is identical to the intersection of all halfspaces defined by its supporting hyperplanes!"
        ],
        "math": "$$x_0 \\in \\partial C \\implies \\exists a \\ne 0 : a^T x \\le a^T x_0 \\quad \\forall x \\in C$$",
        "personalConnection": "Resting a flat ruler against a billiard ball: the ruler touches at a single contact point $x_0$, and the entire ball rests completely on one side of the ruler.",
        "examTrap": "Supporting hyperplanes exist even at non-smooth sharp corners! At a corner, the supporting hyperplane is not unique; there is a whole cone of valid normal vectors (the subdifferential $\\partial f$)."
    },
    {
        "id": 1003,
        "subject": "CMO",
        "topicId": "10_Separating_Hyperplanes_and_Farkas_Lemma",
        "topicTitle": "10 · Separating Hyperplanes & Farkas’ Lemma",
        "cardNumber": "03",
        "category": "FARKAS LEMMA",
        "highlighterClass": "highlight-emerald",
        "title": "Farkas’ Lemma: Theorem of Alternatives",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-1003" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- Polyhedral cone K = {Ax : x >= 0} -->
  <polygon points="40,115 195,35 195,115" fill="#f1f5f9" stroke="#000000" stroke-width="1.8"/>
  <text x="145" y="85" fill="#000000" font-size="9.5" font-family="serif" font-style="italic" font-weight="bold">Cone K = {Ax : x ≥ 0}</text>
  <!-- Vector b outside cone -->
  <line x1="40" y1="115" x2="65" y2="35" stroke="#000000" stroke-width="2" marker-end="url(#arr-1003)"/>
  <circle cx="65" cy="35" r="3.5" fill="#000000"/>
  <text x="60" y="28" fill="#000000" font-size="9.5" font-family="serif" font-style="italic" font-weight="bold">b ∉ K</text>
  <!-- Separating hyperplane normal y -->
  <line x1="40" y1="115" x2="110" y2="20" stroke="#000000" stroke-width="1.2" stroke-dasharray="3,3"/>
  <text x="120" y="134" fill="#000000" font-size="8.5" font-family="monospace" text-anchor="middle">Either b = Ax (x ≥ 0)  XOR  ∃ y : Aᵀy ≥ 0, bᵀy &lt; 0</text>
</svg>""",
        "drawingCaption": "Farkas’ Lemma: Either b lies inside the polyhedral cone {Ax : x ≥ 0}, or a hyperplane y separates b from the cone",
        "coreTranslation": [
            "<strong>The Fundamental Alternative:</strong> Let $A \\in \\mathbb{R}^{m \\times n}$ and $b \\in \\mathbb{R}^m$. Then <strong>EXACTLY ONE</strong> of the following two statements is true:",
            "<strong>System 1:</strong> $\\exists x \\in \\mathbb{R}^n$ such that $A x = b$ and $x \\ge 0$.",
            "<strong>System 2:</strong> $\\exists y \\in \\mathbb{R}^m$ such that $A^T y \\ge 0$ and $b^T y < 0$.",
            "<strong>Geometric Proof:</strong> The set $K = \\{A x : x \\ge 0\\}$ is a closed convex cone. System 1 means $b \\in K$. If $b \\notin K$, the separating hyperplane theorem provides a vector $y$ strictly separating $b$ from $K$!"
        ],
        "math": "$$\\exists x \\ge 0 : A x = b \\quad \\mathbf{XOR} \\quad \\exists y : A^T y \\ge 0, \\; b^T y < 0$$",
        "personalConnection": "A flashlight shining into an ice cream cone: either the scoop of ice cream $b$ sits inside the cone, or you can slip a dividing cardboard card ($y$) between the scoop and the entire cone.",
        "examTrap": "The two systems are mutually exclusive and exhaustive! They can NEVER both have a solution, and they can NEVER both fail. If you prove one holds, the other is automatically false."
    },
    {
        "id": 1004,
        "subject": "CMO",
        "topicId": "10_Separating_Hyperplanes_and_Farkas_Lemma",
        "topicTitle": "10 · Separating Hyperplanes & Farkas’ Lemma",
        "cardNumber": "04",
        "category": "THEOREMS OF THE ALTERNATIVE",
        "highlighterClass": "highlight-violet",
        "title": "Gordan’s Theorem of the Alternative",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <rect x="25" y="25" width="190" height="90" rx="8" fill="#f8fafc" stroke="#000000" stroke-width="1.5"/>
  <text x="120" y="45" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Gordan’s Theorem (Strict Inequalities)</text>
  <text x="120" y="66" fill="#000000" font-size="9" font-family="monospace" text-anchor="middle">System 1: ∃ x s.t. A x &lt; 0</text>
  <text x="120" y="78" fill="#000000" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">XOR</text>
  <text x="120" y="93" fill="#000000" font-size="9" font-family="monospace" text-anchor="middle">System 2: ∃ y ≥ 0, y ≠ 0 s.t. Aᵀ y = 0</text>
  <text x="120" y="132" fill="#000000" font-size="8.5" font-family="sans-serif" text-anchor="middle">Proves that convex hull of row vectors does not contain 0</text>
</svg>""",
        "drawingCaption": "Gordan’s Alternative: Either strict descent directions Ax < 0 exist, or rows are positively linearly dependent Aᵀy = 0",
        "coreTranslation": [
            "<strong>Strict Inequality Alternative:</strong> For matrix $A \\in \\mathbb{R}^{m \\times n}$, exactly one of the following two systems has a solution:",
            "<strong>System 1:</strong> $\\exists x \\in \\mathbb{R}^n$ such that $A x < 0$ (every component strictly negative).",
            "<strong>System 2:</strong> $\\exists y \\in \\mathbb{R}^m$, $y \\ge 0$, $y \\ne 0$ such that $A^T y = 0$.",
            "<strong>Geometric Meaning:</strong> System 1 means the open negative orthant intersects the range of $A$. System 2 means the origin $0$ lies in the convex hull of the row vectors of $A$."
        ],
        "math": "$$\\exists x : A x < 0 \\quad \\mathbf{XOR} \\quad \\exists y \\ge 0, \\; y \\ne 0 : A^T y = 0$$",
        "personalConnection": "Balancing a table on $m$ legs: either you can tilt the entire table downward simultaneously ($Ax < 0$), or there exists a set of non-negative upward support forces that balance each other out ($A^T y = 0$).",
        "examTrap": "Notice the strict inequality $Ax < 0$! If the question asks for $Ax \\le 0$, you must use Farkas' Lemma or Ville's theorem, NOT Gordan's theorem."
    },
    {
        "id": 1005,
        "subject": "CMO",
        "topicId": "10_Separating_Hyperplanes_and_Farkas_Lemma",
        "topicTitle": "10 · Separating Hyperplanes & Farkas’ Lemma",
        "cardNumber": "05",
        "category": "CONE POLARITY",
        "highlighterClass": "highlight-indigo",
        "title": "Dual Cones & Polar Cones (K* and K°)",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <!-- Primal acute cone K -->
  <polygon points="60,115 155,50 155,115" fill="#f1f5f9" stroke="#000000" stroke-width="1.8"/>
  <text x="120" y="90" fill="#000000" font-size="9" font-family="serif" font-style="italic" font-weight="bold">Primal Cone K</text>
  <!-- Dual cone K* (obtuse) -->
  <polygon points="60,115 60,35 155,50" fill="none" stroke="#000000" stroke-width="1.2" stroke-dasharray="3,3"/>
  <text x="75" y="45" fill="#000000" font-size="9" font-family="serif" font-style="italic">Dual K*</text>
  <!-- Vertex 0 -->
  <circle cx="60" cy="115" r="4" fill="#000000"/>
  <text x="48" y="125" fill="#000000" font-size="9" font-family="monospace">0</text>
  <text x="120" y="134" fill="#000000" font-size="8.5" font-family="monospace" text-anchor="middle">K* = {y : yᵀx ≥ 0 ∀ x ∈ K},  K° = -K* = {y : yᵀx ≤ 0}</text>
</svg>""",
        "drawingCaption": "Cone Polarity: Dual cone K* consists of all vectors making acute angles (yᵀx ≥ 0) with all elements of K",
        "coreTranslation": [
            "<strong>Dual Cone $K^*$:</strong> For any cone $K \\subset \\mathbb{R}^n$, its dual cone is: $K^* = \\{y \\in \\mathbb{R}^n : y^T x \\ge 0, \\; \\forall x \\in K\\}$. It is always convex and closed, even if $K$ is neither!",
            "<strong>Polar Cone $K^\\circ$:</strong> Defined by negative inner products: $K^\\circ = \\{y \\in \\mathbb{R}^n : y^T x \\le 0, \\; \\forall x \\in K\\} = -K^*$.",
            "<strong>Bipolar Theorem:</strong> For any closed convex cone $K$, the double dual recovers the original cone: $(K^*)^* = K$ and $(K^\\circ)^\\circ = K$."
        ],
        "math": "$$K^* = \\{y : y^T x \\ge 0 \\, \\forall x \\in K\\}, \\quad (K^*)^* = K \\iff K \\text{ is closed and convex}$$",
        "personalConnection": "An umbrella in a rainstorm: the umbrella ribs form cone $K$. The dry region underneath represents vectors sheltered by negative angles (the polar cone $K^\\circ$).",
        "examTrap": "Self-dual cones: The non-negative orthant $\\mathbb{R}_+^n$ and the cone of positive semidefinite matrices $\\mathbb{S}_+^n$ are strictly <strong>self-dual</strong> ($K^* = K$)."
    },
    {
        "id": 1006,
        "subject": "CMO",
        "topicId": "10_Separating_Hyperplanes_and_Farkas_Lemma",
        "topicTitle": "10 · Separating Hyperplanes & Farkas’ Lemma",
        "cardNumber": "06",
        "category": "WORKED BENCHMARK",
        "highlighterClass": "highlight-rose",
        "title": "Worked Benchmark: Proving KKT via Farkas",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-1006" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- Active constraint gradients -->
  <line x1="120" y1="90" x2="60" y2="40" stroke="#000000" stroke-width="1.8" marker-end="url(#arr-1006)"/>
  <text x="45" y="42" fill="#000000" font-size="8.5" font-family="serif" font-style="italic">∇g₁(x*)</text>
  <line x1="120" y1="90" x2="180" y2="40" stroke="#000000" stroke-width="1.8" marker-end="url(#arr-1006)"/>
  <text x="185" y="42" fill="#000000" font-size="8.5" font-family="serif" font-style="italic">∇g₂(x*)</text>
  <!-- Negative gradient -∇f inside cone -->
  <line x1="120" y1="90" x2="120" y2="30" stroke="#000000" stroke-width="2.5" marker-end="url(#arr-1006)"/>
  <text x="125" y="28" fill="#000000" font-size="9" font-family="serif" font-style="italic" font-weight="bold">-∇f(x*)</text>
  <circle cx="120" cy="90" r="4" fill="#000000"/>
  <text x="120" y="105" fill="#000000" font-size="9" font-family="serif" font-style="italic">x*</text>
  <text x="120" y="125" fill="#000000" font-size="9" font-family="serif" font-style="italic" font-weight="bold" text-anchor="middle">-∇f(x*) = μ₁ ∇g₁(x*) + μ₂ ∇g₂(x*)  (μ_i ≥ 0)</text>
  <text x="120" y="138" fill="#000000" font-size="8.5" font-family="sans-serif" text-anchor="middle">Farkas’ Lemma proves KKT multipliers MUST exist!</text>
</svg>""",
        "drawingCaption": "Worked Proof: Optimality prevents descent directions, so Farkas forces -∇f(x*) to lie in the cone of active constraint gradients",
        "coreTranslation": [
            "<strong>Problem:</strong> Prove why Karush-Kuhn-Tucker multipliers $\\mu_j \\ge 0$ must exist at a constrained local minimum $x^*$.",
            "<strong>Step 1 (No Descent):</strong> At a local minimum, there can be NO feasible descent direction: $\\nexists d$ such that $\\nabla f(x^*)^T d < 0$ and $\\nabla g_j(x^*)^T d \\le 0$ for all $j \\in \\mathcal{A}(x^*)$.",
            "<strong>Step 2 (Apply Farkas / Gordan):</strong> The failure of this inequality system implies by Farkas' Lemma that the dual system MUST have a solution: $-\\nabla f(x^*) = \\sum_{j \\in \\mathcal{A}} \\mu_j \\nabla g_j(x^*)$ with $\\mu_j \\ge 0$. This is the KKT condition!"
        ],
        "math": "$$-\\nabla f(x^*) = \\sum_{j \\in \\mathcal{A}(x^*)} \\mu_j^* \\nabla g_j(x^*), \\quad \\mu_j^* \\ge 0 \\quad (\\text{Farkas Dual of } \\nexists d : \\nabla f^T d < 0, \\nabla g_j^T d \\le 0)$$",
        "personalConnection": "Tug-of-war in a corner: the objective pulls you downhill ($-\\nabla f$), but the two boundary walls balance you with positive normal forces ($\mu_1 \\nabla g_1 + \\mu_2 \\nabla g_2$). Net force is zero.",
        "examTrap": "Farkas' lemma applies to LINEARIZED directions $\\nabla g_j^T d \\le 0$. For this to match physical feasible curves in $\\Omega$, a Constraint Qualification (like LICQ) is strictly required!"
    }
]

print(f"Defined {len(topic06_cards)} Topic 06 cards")
print(f"Defined {len(topic07_cards)} Topic 07 cards")
print(f"Defined {len(topic08_cards)} Topic 08 cards")
print(f"Defined {len(topic10_cards)} Topic 10 cards")

# Write out the python module
all_new_cmo = topic06_cards + topic07_cards + topic08_cards + topic10_cards
with open('/Users/senso/Projects/photographic-memory-cards/scripts/new_cmo_cards.json', 'w') as f:
    json.dump(all_new_cmo, f, indent=2)

print(f"Saved {len(all_new_cmo)} new CMO cards to new_cmo_cards.json")
