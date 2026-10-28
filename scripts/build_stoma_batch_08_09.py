"""Build StoMA Topics 08 & 09 (Cards 30801 to 30906).
Dual-coding photographic plates with pure black-and-white vector diagrams.
"""
import sys, os
sys.path.append(os.path.dirname(__file__))
from stoma_lib import (
    T, N, L, V, P, C, R, E, PG, AX, box, svg, make_stoma_card, save_stoma_cards
)

CARDS = []

# ==============================================================================
# TOPIC 08: MULTIPLE RANDOM VARIABLES & ORDER STATISTICS (30801 - 30806)
# ==============================================================================

# Card 30801: Order Statistics & Extremes: Sample Minimum and Maximum
svg_30801 = [
    # Number line with order statistics
    L(20, 72, 220, 72, 1.8),
    C(40, 72, 4, fill="#000000"), N(40, 60, "X_{(1)}", 9, w="bold"), N(40, 86, "Min", 7.5),
    C(80, 72, 3, fill="#000000"), N(80, 60, "X_{(2)}", 8),
    C(120, 72, 3, fill="#000000"), N(120, 60, "...", 8),
    C(160, 72, 3, fill="#000000"), N(160, 60, "X_{(n-1)}", 8),
    C(200, 72, 4, fill="#000000"), N(200, 60, "X_{(n)}", 9, w="bold"), N(200, 86, "Max", 7.5),
    # Extremes formula boxes
    box(20, 18, 96, 32, "Max: P(X_{(n)} ≤ x)\n= [F(x)]^n", "#ffffff", 8),
    box(124, 18, 96, 32, "Min: P(X_{(1)} > x)\n= [1 - F(x)]^n", "#ffffff", 8),
    N(120, 114, "f_{X_{(n)}}(x) = n [F(x)]^{n-1} f(x),   f_{X_{(1)}}(x) = n [1 - F(x)]^{n-1} f(x)", 8, w="bold"),
    N(120, 138, "Sample extremes: Max requires all Xᵢ ≤ x; Min requires all Xᵢ > x", 8.5)
]
CARDS.append(make_stoma_card(
    8, 1, "EXTREME VALUES",
    "Order Statistics & Extremes: Sample Minimum and Maximum",
    svg_30801,
    "The sample maximum requires every item to be below x; the sample minimum requires every item to exceed x",
    [
        "<strong>Ascending Sort:</strong> For i.i.d. $X_1, \\dots, X_n \\sim F$, sorting in ascending order yields order statistics $X_{(1)} \\le X_{(2)} \\le \\dots \\le X_{(n)}$.",
        "<strong>Sample Maximum:</strong> $X_{(n)} \\le x \\iff$ every $X_i \\le x$. By independence, $F_{X_{(n)}}(x) = [F(x)]^n$, so $f_{X_{(n)}}(x) = n [F(x)]^{n-1} f(x)$.",
        "<strong>Sample Minimum:</strong> $X_{(1)} > x \\iff$ every $X_i > x$. Thus $\\mathbb{P}(X_{(1)} > x) = [1 - F(x)]^n$, giving $F_{X_{(1)}}(x) = 1 - [1 - F(x)]^n$."
    ],
    r"$$F_{X_{(n)}}(x) = [F(x)]^n, \qquad F_{X_{(1)}}(x) = 1 - [1 - F(x)]^n, \qquad f_{X_{(1)}}(x) = n[1-F(x)]^{n-1} f(x)$$",
    "Weakest link of a chain: the entire chain snaps as soon as its weakest link fails (minimum X_{(1)}); a flood wall fails when the highest wave tops it (maximum X_{(n)}).",
    "Differentiating 1 - [1 - F(x)]^n and losing the negative sign from the inner derivative! -n[1 - F(x)]^{n-1}(-f(x)) = +n[1 - F(x)]^{n-1}f(x)."
))

# Card 30802: General Marginal Density of the k-th Order Statistic
svg_30802 = [
    # Axis divided into 3 zones around x
    L(20, 72, 220, 72, 1.8),
    # Zone 1: (-∞, x)
    R(25, 45, 75, 54, fill="#f8fafc", sw=1.1, d="2 2"),
    N(62, 60, "(k - 1) items", 8.5, w="bold"),
    N(62, 80, "prob: [F(x)]^{k-1}", 7.5),
    # Zone 2: [x, x+dx]
    R(105, 40, 30, 64, fill="#d9dee7", sw=1.3),
    N(120, 58, "1 item", 8.5, w="bold"),
    N(120, 80, "f(x)dx", 8, w="bold"),
    # Zone 3: (x, ∞)
    R(140, 45, 75, 54, fill="#f8fafc", sw=1.1, d="2 2"),
    N(177, 60, "(n - k) items", 8.5, w="bold"),
    N(177, 80, "prob: [1-F(x)]^{n-k}", 7.5),
    N(120, 25, "f_{X_{(k)}}(x) = \\frac{n!}{(k-1)!(n-k)!} [F(x)]^{k-1} [1-F(x)]^{n-k} f(x)", 8.5, w="bold"),
    N(120, 138, "Multinomial placement: (k-1) to left, exactly 1 in [x, x+dx], and (n-k) to right", 8)
]
CARDS.append(make_stoma_card(
    8, 2, "ORDER DENSITIES",
    "General Marginal Density of the k-th Order Statistic",
    svg_30802,
    "Trisection of the real line into left tail, pivot element in [x, x+dx], and right tail via multinomial counting",
    [
        "<strong>Trisection Probability:</strong> Probability that 1 item lies in $[x, x+dx]$ is $f(x)dx$, $(k-1)$ items lie in $(-\\infty, x)$ with probability $F(x)$, and $(n-k)$ items lie in $(x, \\infty)$ with probability $1 - F(x)$.",
        "<strong>Combinatorial Multiplicity:</strong> There are $\\frac{n!}{(k-1)! 1! (n-k)!} = k \\binom{n}{k}$ distinct assignments of the $n$ samples to these three zones.",
        "<strong>General Marginal PDF:</strong> $f_{X_{(k)}}(x) = \\frac{n!}{(k-1)!(n-k)!} [F(x)]^{k-1} [1 - F(x)]^{n-k} f(x)$."
    ],
    r"$$f_{X_{(k)}}(x) = \frac{n!}{(k-1)!(n-k)!} [F(x)]^{k-1} [1 - F(x)]^{n-k} f(x) = k \binom{n}{k} [F(x)]^{k-1} [1 - F(x)]^{n-k} f(x)$$",
    "Median score on an entrance exam: (k-1) students score below, exactly 1 student sits at the pivot cut-off, and (n-k) students score above.",
    "Forgetting the trailing density factor f(x)! Without f(x), the expression is a discrete binomial probability mass, NOT a continuous probability density function."
))

# Card 30803: Joint Density of All n Order Statistics & n! Factor
svg_30803 = [
    # 2D simplex cone illustration (x₁ < x₂)
    AX(24, 115, 220, 20),
    # Diagonal x₁ = x₂
    L(40, 114, 180, 25, 1.2, d="3 3"),
    N(165, 25, "x₁ = x₂", 8),
    # Shaded ordered cone x₁ < x₂
    PG("40,114 180,114 180,25", fill="#d9dee7", w=1.5),
    N(130, 85, "Ordered Cone:\nx₁ < x₂ < ... < x_n", 8.5, w="bold"),
    # Formula box
    box(24, 20, 100, 44, "Joint Density:\nn! ∏ f(xᵢ)\non x₁ < x₂ < ... < x_n", "#ffffff", 8),
    N(120, 138, "Sorting folds all n! sample permutations into a single ordered cone; density scales by n!", 8)
]
CARDS.append(make_stoma_card(
    8, 3, "JOINT ORDER STATS",
    "Joint Density of All n Order Statistics & The n! Permutation",
    svg_30803,
    "Sorting folds the n-dimensional hypercube into a single ordered simplex cone, multiplying density by n!",
    [
        "<strong>Joint Density Formula:</strong> $f_{X_{(1)}, \\dots, X_{(n)}}(x_1, \\dots, x_n) = n! \\prod_{i=1}^n f(x_i) \\cdot \\mathbf{1}_{\\{x_1 < x_2 < \\dots < x_n\\}}$.",
        "<strong>Origin of $n!$:</strong> There are $n!$ distinct permutations of the original unordered vector $(X_1, \\dots, X_n)$ that sort into the identical ordered list $(x_1, \\dots, x_n)$.",
        "<strong>Induced Dependence:</strong> Even though raw samples $X_i$ are independent, order statistics $X_{(1)}, \\dots, X_{(n)}$ are STRONGLY DEPENDENT through the ordering constraints $X_{(1)} < \\dots < X_{(n)}$."
    ],
    r"$$f_{X_{(1)},\dots,X_{(n)}}(x_1, \dots, x_n) = n! \prod_{i=1}^n f(x_i) \cdot \mathbf{1}_{\{x_1 < x_2 < \dots < x_n\}}$$",
    "Folding a paper fan: folding an n-dimensional sheet along all diagonals collapses n! identical symmetric wedges into one single compact ordered cone of volume 1/n!.",
    "Omitting the factor n! in joint calculations. Without n!, integrating over the ordered domain x₁ < ... < x_n yields 1/n! instead of the required probability 1."
))

# Card 30804: Uniform Order Statistics & Beta Distribution
svg_30804 = [
    # Unit interval [0, 1] split into n+1 pieces
    L(20, 72, 220, 72, 2.0),
    C(20, 72, 3, fill="#000000"), N(20, 86, "0", 8.5, w="bold"),
    C(220, 72, 3, fill="#000000"), N(220, 86, "1", 8.5, w="bold"),
    # Spacings
    C(60, 72, 3.5, fill="#000000"), N(60, 60, "U_{(1)}", 8),
    C(110, 72, 3.5, fill="#000000"), N(110, 60, "U_{(k)}", 8.5, w="bold"),
    C(170, 72, 3.5, fill="#000000"), N(170, 60, "U_{(n)}", 8),
    N(110, 88, "E[U_{(k)}] = k / (n + 1)", 8.5, w="bold"),
    box(20, 20, 200, 26, "U_{(k)} ~ Beta(k, n - k + 1)   on [0, 1]", "#f8fafc", 8.5),
    N(120, 138, "n uniform points divide [0, 1] into (n+1) equal-mean spacings of length 1/(n+1)", 8.5)
]
CARDS.append(make_stoma_card(
    8, 4, "UNIFORM ORDER",
    "Uniform Order Statistics & The Beta Distribution",
    svg_30804,
    "Order statistics of Uniform(0, 1) follow exact Beta distributions; expected spacing between all points is 1/(n+1)",
    [
        "<strong>Beta Distribution Law:</strong> For $U_1, \\dots, U_n \\stackrel{\\text{i.i.d.}}{\\sim} \\text{Uniform}(0, 1)$, $f_{U_{(k)}}(u) = \\frac{n!}{(k-1)!(n-k)!} u^{k-1} (1-u)^{n-k} \\sim \\text{Beta}(k, n - k + 1)$.",
        "<strong>Expected Position:</strong> $\\mathbb{E}[U_{(k)}] = \\frac{k}{n+1}$, and variance $\\operatorname{Var}(U_{(k)}) = \\frac{k(n - k + 1)}{(n+1)^2(n+2)}$.",
        "<strong>Equal Mean Spacings:</strong> The $n$ order statistics partition $[0, 1]$ into $(n+1)$ sub-intervals (spacings) whose expected lengths are all IDENTICAL: $\\mathbb{E}[D_i] = \\frac{1}{n+1}$."
    ],
    r"$$U_{(k)} \sim \text{Beta}(k, n - k + 1), \qquad \mathbb{E}[U_{(k)}] = \frac{k}{n+1}, \qquad \operatorname{Var}(U_{(k)}) = \frac{k(n - k + 1)}{(n+1)^2(n+2)}$$",
    "Dropping n random markers along a 1 km running track: on average, the markers cut the track into (n+1) segments of exactly equal length 1/(n+1) km.",
    "Believing edge spacings 0 to U_{(1)} and U_{(n)} to 1 behave differently from interior spacings. All (n+1) spacings are identically distributed with expected length 1/(n+1)."
))

# Card 30805: Exponential Order Statistics & Spacings Property
svg_30805 = [
    # Timeline of exponential arrivals
    L(20, 72, 220, 72, 1.8),
    C(20, 72, 3, fill="#000000"), N(20, 86, "0", 8),
    C(70, 72, 3.5, fill="#000000"), N(70, 60, "X_{(1)}", 8.5),
    C(130, 72, 3.5, fill="#000000"), N(130, 60, "X_{(2)}", 8.5),
    C(200, 72, 3.5, fill="#000000"), N(200, 60, "X_{(3)}", 8.5),
    # Spacing intervals
    L(20, 88, 70, 88, 1.2), N(45, 100, "W₁ ~ Exp(3λ)", 7.5, w="bold"),
    L(70, 88, 130, 88, 1.2), N(100, 100, "W₂ ~ Exp(2λ)", 7.5, w="bold"),
    L(130, 88, 200, 88, 1.2), N(165, 100, "W₃ ~ Exp(λ)", 7.5, w="bold"),
    box(20, 18, 200, 26, "Spacings W_k = X_{(k)} - X_{(k-1)} ~ Exp((n - k + 1)λ) are INDEPENDENT", "#f8fafc", 8),
    N(120, 138, "Maximum mean: E[X_{(n)}] = (1/λ) ∑_{j=1}^n (1/j) ≈ (log n + γ) / λ", 8.5)
]
CARDS.append(make_stoma_card(
    8, 5, "EXPONENTIAL ORDER",
    "Exponential Order Statistics & Independent Spacings",
    svg_30805,
    "Exponential order statistics decompose into mutually independent exponential spacings with accelerating rates",
    [
        "<strong>Exponential Setup:</strong> Let $X_1, \\dots, X_n \\stackrel{\\text{i.i.d.}}{\\sim} \\text{Exp}(\\lambda)$.",
        "<strong>Independent Spacings:</strong> The spacings $W_k = X_{(k)} - X_{(k-1)}$ (with $X_{(0)} = 0$) are MUTUALLY INDEPENDENT Exponential RVs with parameter $(n - k + 1)\\lambda$.",
        "<strong>Harmonic Mean Sum:</strong> $\\mathbb{E}[X_{(k)}] = \\frac{1}{\\lambda} \\sum_{j=1}^k \\frac{1}{n - j + 1}$. The maximum has expected value $\\mathbb{E}[X_{(n)}] = \\frac{1}{\\lambda} \\sum_{j=1}^n \\frac{1}{j} \\approx \\frac{\\ln n + \\gamma}{\\lambda}$."
    ],
    r"$$W_k = X_{(k)} - X_{(k-1)} \sim \text{Exp}((n - k + 1)\lambda) \text{ independent}; \quad \mathbb{E}[X_{(n)}] = \frac{1}{\lambda} \sum_{j=1}^n \frac{1}{j}$$",
    "Lightbulb array: all n bulbs race to burn out first at collective rate nλ; once one burns out, remaining (n-1) race at rate (n-1)λ, down to the final survivor.",
    "Applying independent spacings to non-exponential variables! The independent spacings property is a UNIQUE signature of the memoryless exponential distribution."
))

# Card 30806: Worked Benchmark: Minimum of Exponential Lifetimes in Series
svg_30806 = [
    # Series circuit: component 1, component 2, component 3
    L(20, 72, 45, 72, 1.5),
    box(45, 58, 40, 28, "T₁~Exp(λ₁)", "#ffffff", 7.5),
    L(85, 72, 105, 72, 1.5),
    box(105, 58, 40, 28, "T₂~Exp(λ₂)", "#ffffff", 7.5),
    L(145, 72, 165, 72, 1.5),
    box(165, 58, 40, 28, "T_n~Exp(λ_n)", "#ffffff", 7),
    L(205, 72, 225, 72, 1.5),
    # Result box
    box(20, 18, 200, 28, "T_{sys} = min(T₁, ..., T_n) ~ Exp(∑ λᵢ),   E[T_{sys}] = 1 / ∑ λᵢ", "#f8fafc", 8.5),
    N(120, 114, "P(Component k fails first) = λ_k / ∑ λᵢ", 8.5, w="bold"),
    N(120, 138, "Series reliability: multiply survival functions P(Tᵢ > t) = exp(-λᵢ t); rates sum linearly", 8)
]
CARDS.append(make_stoma_card(
    8, 6, "WORKED BENCHMARK",
    "Worked Benchmark: System Reliability via Minimum of Exponentials",
    svg_30806,
    "The minimum of independent exponentials is exponential with sum of rates; failure identity is proportional to rate",
    [
        "<strong>Series Setup:</strong> System of $n$ components in series with independent lifetimes $T_i \\sim \\text{Exp}(\\lambda_i)$. System fails at $T_{\\text{sys}} = \\min(T_1, \\dots, T_n)$.",
        "<strong>Survival Product:</strong> $\\mathbb{P}(T_{\\text{sys}} > t) = \\prod_{i=1}^n \\mathbb{P}(T_i > t) = \\prod_{i=1}^n e^{-\\lambda_i t} = \\exp(-(\\sum_{i=1}^n \\lambda_i) t)$.",
        "<strong>Failure Probability:</strong> The system lifetime is strictly $\\text{Exp}(\\sum_{i=1}^n \\lambda_i)$, and component $k$ is the one that causes system failure with probability $\\frac{\\lambda_k}{\\sum_{i=1}^n \\lambda_i}$."
    ],
    r"$$T_{\text{sys}} = \min_{1 \le i \le n} T_i \sim \text{Exp}\left(\sum_{i=1}^n \lambda_i\right), \qquad \mathbb{P}(T_k = \min T_i) = \frac{\lambda_k}{\sum_{i=1}^n \lambda_i}$$",
    "A sprint race among n runners: the winning time is distributed as the minimum, and each runner's chance of winning is directly proportional to their running speed λ_k.",
    "Attempting convolution integration to find the minimum of lifetimes! Always compute minimums via the product of survival functions P(T_i > t)—convolution is for SUMS, not minimums."
))

# ==============================================================================
# TOPIC 09: SUMS & JACOBIAN TRANSFORMATIONS (30901 - 30906)
# ==============================================================================

# Card 30901: The Convolution Formula for Sums of Independent RVs
svg_30901 = [
    AX(24, 115, 220, 20),
    # Diagonal line x + y = z
    L(40, 114, 160, 25, 1.8),
    N(145, 25, "x + y = z", 9, w="bold"),
    # Point (x, z - x)
    C(100, 70, 3.5, fill="#000000"),
    N(125, 70, "(x, z - x)", 8, w="bold"),
    L(100, 70, 100, 114, 1.0, d="2 2"),
    N(100, 126, "x", 8.5),
    # Formula box
    box(24, 20, 96, 36, "Continuous:\nf_Z(z) = ∫ f_X(x) f_Y(z-x) dx", "#ffffff", 7.5),
    box(128, 20, 96, 36, "Discrete:\nP(Z=k) = ∑ P(X=j) P(Y=k-j)", "#ffffff", 7.5),
    N(120, 138, "Convolution integrates joint mass along the diagonal line x + y = z", 8.5)
]
CARDS.append(make_stoma_card(
    9, 1, "CONVOLUTION",
    "The Convolution Formula for Sums of Independent RVs",
    svg_30901,
    "The density of Z = X + Y integrates joint density along the diagonal slice x + y = z",
    [
        "<strong>Continuous Convolution:</strong> For independent $X \\perp Y$, the density of $Z = X + Y$ is $(f_X * f_Y)(z) = \\int_{-\\infty}^\\infty f_X(x) f_Y(z - x)\\,dx$.",
        "<strong>Discrete Convolution:</strong> For independent integer RVs, $\\mathbb{P}(Z = k) = \\sum_{j=-\\infty}^\\infty \\mathbb{P}(X = j)\\,\\mathbb{P}(Y = k - j)$.",
        "<strong>Algebraic Properties:</strong> Convolution is commutative ($f_X * f_Y = f_Y * f_X$) and associative ($(f_X * f_Y) * f_W = f_X * (f_Y * f_W)$)."
    ],
    r"$$f_{X+Y}(z) = (f_X * f_Y)(z) = \int_{-\infty}^\infty f_X(x) f_Y(z - x)\,dx = \int_{-\infty}^\infty f_X(z - y) f_Y(y)\,dy$$",
    "Sliding an audio filter across an audio signal: reversing one signal in time (z - x) and integrating total overlap energy at time delay z.",
    "Neglecting to adjust integration limits for non-negative variables! If X, Y ≥ 0, then 0 ≤ x ≤ z; integrating from -∞ to ∞ without truncating limits produces severe calculation errors."
))

# Card 30902: 2D Multivariate Jacobian Transformation Theorem
svg_30902 = [
    # xy-plane patch
    PG("30,90 70,80 80,105 40,115", fill="#f8fafc", w=1.2),
    N(55, 98, "dx dy", 8),
    V(85, 95, 125, 95, 1.4),
    N(105, 85, "g(X, Y)", 7.5, w="bold"),
    # uv-plane transformed parallelogram patch
    PG("140,85 195,70 210,110 155,125", fill="#d9dee7", w=1.4),
    N(175, 98, "du dv = |J| dx dy", 8, w="bold"),
    # Jacobian matrix box
    box(24, 20, 192, 42, "J(u, v) = det [ ∂x/∂u  ∂x/∂v ;  ∂y/∂u  ∂y/∂v ]\nf_{U,V}(u, v) = f_{X,Y}(x(u, v), y(u, v)) · |J(u, v)|", "#ffffff", 8),
    N(120, 138, "The Jacobian determinant scales differential area: |J(u, v)| = 1 / |J(x, y)|", 8.5)
]
CARDS.append(make_stoma_card(
    9, 2, "2D JACOBIAN",
    "2D Multivariate Jacobian Transformation Theorem",
    svg_30902,
    "Multivariate 2D mappings scale local area elements by the absolute determinant of the coordinate Jacobian",
    [
        "<strong>Bijective Smooth Mapping:</strong> Let $(U, V) = g(X, Y)$ be an invertible, continuously differentiable mapping from $S \\subset \\mathbb{R}^2$ to $T \\subset \\mathbb{R}^2$.",
        "<strong>Jacobian Determinant:</strong> $J(u, v) \\triangleq \\det \\begin{bmatrix} \\partial x/\\partial u & \\partial x/\\partial v \\\\ \\partial y/\\partial u & \\partial y/\\partial v \\end{bmatrix}$. Reciprocal identity: $J(u, v) = [J(x, y)]^{-1}$.",
        "<strong>Transformed Density:</strong> $f_{U,V}(u, v) = f_{X,Y}(x(u, v), y(u, v)) |J(u, v)| \\cdot \\mathbf{1}_{\\{(u, v) \\in T\\}}$."
    ],
    r"$$f_{U,V}(u, v) = f_{X,Y}\left(x(u, v), y(u, v)\right) \left| \det \frac{\partial(x, y)}{\partial(u, v)} \right|$$",
    "Mercator map projection: flattening spherical latitude and longitude onto a flat map distorts area sizes by the local metric Jacobian determinant.",
    "Inverting forward vs inverse Jacobian! If you calculate the forward derivative matrix ∂(u,v)/∂(x,y), you must DIVIDE by its determinant rather than multiply."
))

# Card 30903: Ratio Distribution & Polar Transformations
svg_30903 = [
    # Polar coordinates circle
    E(70, 72, 40, 40, fill="#f8fafc", w=1.2),
    AX(30, 72, 110, 25),
    L(70, 72, 100, 45, 1.4),
    N(88, 54, "r", 8, w="bold"),
    N(78, 68, "θ", 7),
    N(70, 126, "dx dy = r dr dθ", 8, w="bold"),
    # Ratio distribution box
    box(125, 30, 100, 50, "Ratio Z = Y / X:\nf_Z(z) = ∫ |x| f_{X,Y}(x, xz) dx\n(Cauchy if X, Y ~ N(0, 1))", "#ffffff", 7.5),
    N(120, 138, "Polar Jacobian is r; Ratio transformation integrates along radial rays y = xz with factor |x|", 8)
]
CARDS.append(make_stoma_card(
    9, 3, "RATIO & POLAR",
    "Ratio Distribution & Polar Coordinate Transformations",
    svg_30903,
    "Polar coordinates introduce metric area factor r; ratio distributions integrate radial rays with factor |x|",
    [
        "<strong>Ratio Formula:</strong> For $Z = Y / X$, introduce auxiliary $W = X$. Inverse is $x = w, y = wz$ with Jacobian $|J| = |w|$, yielding $f_Z(z) = \\int_{-\\infty}^\\infty |x| f_{X,Y}(x, xz)\\,dx$.",
        "<strong>Polar Coordinates:</strong> $(X, Y) = (R \\cos\\Theta, R \\sin\\Theta)$. The Jacobian determinant is $\\det \\begin{bmatrix} \\cos\\theta & -r\\sin\\theta \\\\ \\sin\\theta & r\\cos\\theta \\end{bmatrix} = r$.",
        "<strong>Polar Density:</strong> $f_{R,\\Theta}(r, \\theta) = r f_{X,Y}(r \\cos\\theta, r \\sin\\theta)$ for $r \\ge 0, \\theta \\in [0, 2\\pi)$."
    ],
    r"$$Z = \frac{Y}{X} \implies f_Z(z) = \int_{-\infty}^\infty |x|\,f_{X,Y}(x, xz)\,dx, \qquad f_{R,\Theta}(r, \theta) = r\,f_{X,Y}(r\cos\theta, r\sin\theta)$$",
    "Marine sonar sweep: scanning targets in range r and angle θ; rings expand in area as 2π r dr, introducing the linear geometric weighting factor r.",
    "Forgetting the absolute value factor |x| in the ratio formula! Neglecting |x| violates physical dimensions (density must have units 1/z) and gives wrong integrals."
))

# Card 30904: Box-Muller Transform: Generating Standard Normals
svg_30904 = [
    box(16, 20, 96, 36, "U₁, U₂ ~ i.i.d. Unif(0, 1)\n(Standard uniform)", "#ffffff", 8),
    V(112, 38, 136, 38, 1.4),
    box(136, 20, 88, 36, "Z₁, Z₂ ~ i.i.d. N(0, 1)\n(Standard normal)", "#e2e8f0", 8),
    # Box-Muller formulas
    R(16, 68, 208, 44, fill="#f8fafc", sw=1.3),
    N(120, 82, "Z₁ = √(-2 ln U₁) · cos(2π U₂)", 9, w="bold"),
    N(120, 98, "Z₂ = √(-2 ln U₁) · sin(2π U₂)", 9, w="bold"),
    N(120, 138, "Radius R² = -2 ln U₁ ~ Exp(1/2) ≡ χ₂²; Angle Θ = 2π U₂ ~ Unif(0, 2π)", 8.5)
]
CARDS.append(make_stoma_card(
    9, 4, "BOX-MULLER",
    "The Box-Muller Transform: Exact Gaussian Simulation",
    svg_30904,
    "Converts two independent Uniform(0, 1) variates into two independent standard Gaussian variates in closed form",
    [
        "<strong>Motivation:</strong> Gaussian quantile function $\\Phi^{-1}(u)$ has no closed form. Box-Muller bypasses 1D intractability by operating in 2D polar coordinates.",
        "<strong>Construction:</strong> For $U_1, U_2 \\stackrel{\\text{i.i.d.}}{\\sim} \\text{Uniform}(0, 1)$, set radius $R = \\sqrt{-2\\ln U_1}$ (so $R^2 \\sim \\text{Exp}(1/2) \\equiv \\chi_2^2$) and angle $\\Theta = 2\\pi U_2 \\sim \\text{Uniform}(0, 2\\pi)$.",
        "<strong>Exact Normals:</strong> $Z_1 = R \\cos\\Theta$ and $Z_2 = R \\sin\\Theta$ are EXACTLY independent standard normal random variables: $Z_1, Z_2 \\stackrel{\\text{i.i.d.}}{\\sim} \\mathcal{N}(0, 1)$."
    ],
    r"$$Z_1 = \sqrt{-2\ln U_1}\cos(2\pi U_2), \quad Z_2 = \sqrt{-2\ln U_1}\sin(2\pi U_2) \implies Z_1, Z_2 \stackrel{\text{i.i.d.}}{\sim} \mathcal{N}(0, 1)$$",
    "Dartboard simulation: choosing a radial distance from center according to a Rayleigh law and a completely random 360° angle creates a 2D circularly symmetric Gaussian cloud.",
    "Generating standard normals one at a time and discarding Z₂! Box-Muller generates TWO independent normal values per pair of uniforms; saving both doubles computational efficiency."
))

# Card 30905: Canonical Sum Invariants: Normal, Poisson & Gamma
svg_30905 = [
    # 3 closure boxes
    box(16, 20, 208, 28, "Normals: N(μ₁, σ₁²) + N(μ₂, σ₂²) = N(μ₁ + μ₂, σ₁² + σ₂²)", "#ffffff", 8.5),
    box(16, 56, 208, 28, "Poisson: Pois(λ₁) + Pois(λ₂) = Pois(λ₁ + λ₂)", "#ffffff", 8.5),
    box(16, 92, 208, 28, "Gamma: Gamma(α₁, β) + Gamma(α₂, β) = Gamma(α₁ + α₂, β)  [Same β!]", "#f1f5f9", 8.5),
    N(120, 138, "Independent sum closures: Gaussians, Poissons, and shared-scale Gammas are closed under addition", 8)
]
CARDS.append(make_stoma_card(
    9, 5, "CONVOLUTION STABILITY",
    "Sum Invariants: Stability of Normal, Poisson & Gamma",
    svg_30905,
    "Independent sums of Gaussians are Gaussian, sums of Poissons are Poisson, and sums of Gammas are Gamma",
    [
        "<strong>Gaussian Closure:</strong> If $X_i \\sim \\mathcal{N}(\\mu_i, \\sigma_i^2)$ are independent, $\\sum_{i=1}^n X_i \\sim \\mathcal{N}(\\sum \\mu_i, \\sum \\sigma_i^2)$.",
        "<strong>Poisson Closure:</strong> If $X_i \\sim \\text{Poisson}(\\lambda_i)$ are independent, $\\sum_{i=1}^n X_i \\sim \\text{Poisson}(\\sum \\lambda_i)$.",
        "<strong>Gamma Closure (Shared Rate):</strong> If $X_i \\sim \\text{Gamma}(\\alpha_i, \\beta)$ are independent with IDENTICAL scale $\\beta$, then $\\sum_{i=1}^n X_i \\sim \\text{Gamma}(\\sum \\alpha_i, \\beta)$."
    ],
    r"$$\sum_{i=1}^n \mathcal{N}(\mu_i, \sigma_i^2) = \mathcal{N}\left(\sum \mu_i, \sum \sigma_i^2\right), \quad \sum_{i=1}^n \text{Pois}(\lambda_i) = \text{Pois}\left(\sum \lambda_i\right)$$",
    "Combining incoming service calls: two independent streams of Poisson calls with rates λ₁ and λ₂ merge into a single stream of Poisson calls with rate λ₁ + λ₂.",
    "Adding Gamma random variables with different scale parameters β₁ ≠ β₂! The sum of Gammas is Gamma ONLY when the rate/scale parameter is identical across all terms."
))

# Card 30906: Worked Benchmark: Sum of Two Uniforms (Irwin-Hall n=2)
svg_30906 = [
    AX(24, 115, 220, 20),
    # Triangle distribution on [0, 2] peaking at z=1, height 1
    P("M 40,114 L 120,35 L 200,114", fill="#d9dee7", w=2.0),
    L(120, 35, 120, 114, 1.2, d="2 2"),
    N(40, 126, "0", 8.5, w="bold"),
    N(120, 126, "1", 8.5, w="bold"),
    N(200, 126, "2", 8.5, w="bold"),
    N(16, 35, "1", 8.5, w="bold"),
    N(70, 65, "f_Z(z) = z", 8, w="bold"),
    N(170, 65, "f_Z(z) = 2 - z", 8, w="bold"),
    N(120, 138, "Convolution of two independent Unif(0, 1) pulses creates a symmetric triangle distribution", 8.5)
]
CARDS.append(make_stoma_card(
    9, 6, "WORKED BENCHMARK",
    "Worked Benchmark: Sum of Two Uniforms (The Triangle Law)",
    svg_30906,
    "Convolving two rectangular uniform pulses generates a symmetric triangular probability density",
    [
        "<strong>Problem Setup:</strong> Let $X, Y \\stackrel{\\text{i.i.d.}}{\\sim} \\text{Uniform}[0, 1]$. Compute the PDF of $Z = X + Y$.",
        "<strong>Convolution Integral:</strong> $f_Z(z) = \\int_0^1 \\mathbf{1}_{\\{0 \\le z - x \\le 1\\}}\\,dx = \\int_{\\max(0, z-1)}^{\\min(1, z)} 1\\,dx$.",
        "<strong>Piecewise Triangle:</strong> For $0 \\le z \\le 1$, $f_Z(z) = z$. For $1 < z \\le 2$, $f_Z(z) = 2 - z$. Mean is $\\mathbb{E}[Z] = 1$, variance $\\operatorname{Var}(Z) = 1/12 + 1/12 = 1/6$."
    ],
    r"$$f_{X+Y}(z) = \begin{cases} z & 0 \le z \le 1 \\ 2 - z & 1 < z \le 2 \\ 0 & \text{otherwise} \end{cases}, \qquad \mathbb{E}[Z] = 1, \; \operatorname{Var}(Z) = \tfrac{1}{6}$$",
    "Rolling two fair dice: the sum of two uniform outcomes forms a triangular frequency peak at 7, tapering linearly toward 2 and 12.",
    "Treating the convolution integral as a single algebraic formula over [0, 2]! The overlap geometry changes at z = 1, splitting the solution into two distinct linear regimes."
))

# Save cards to cards_stoma.js
save_stoma_cards(CARDS)
print(f"Successfully generated {len(CARDS)} cards for StoMA Topics 08 & 09!")
