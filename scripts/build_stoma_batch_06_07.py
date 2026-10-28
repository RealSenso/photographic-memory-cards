"""Build StoMA Topics 06 & 07 (Cards 30601 to 30706).
Dual-coding photographic plates with pure black-and-white vector diagrams.
"""
import sys, os
sys.path.append(os.path.dirname(__file__))
from stoma_lib import (
    T, N, L, V, P, C, R, E, PG, AX, box, svg, make_stoma_card, save_stoma_cards
)

CARDS = []

# ==============================================================================
# TOPIC 06: PROBABILITY INEQUALITIES (30601 - 30606)
# ==============================================================================

# Card 30601: Markov’s Inequality & Indicator Bounding
svg_30601 = [
    AX(24, 115, 220, 20),
    # RV identity curve y = x
    L(24, 114, 190, 28, 1.4, d="3 3"),
    N(195, 25, "y = x", 8.5),
    # Step indicator a · 1_{x ≥ a}
    L(24, 114, 110, 114, 2.0),
    L(110, 114, 110, 68, 1.2, d="2 2"),
    L(110, 68, 215, 68, 2.2),
    C(110, 68, 3, fill="#000000"),
    C(110, 114, 2.5, fill="#ffffff"),
    N(16, 68, "a", 9, w="bold"),
    N(110, 126, "a", 9, w="bold"),
    N(160, 54, "a · 1_{X ≥ a} ≤ X", 9, w="bold"),
    N(120, 138, "Taking expectations: a P(X ≥ a) ≤ E[X] ⇒ P(X ≥ a) ≤ E[X] / a  (X ≥ 0)", 8)
]
CARDS.append(make_stoma_card(
    6, 1, "MOMENT BOUND",
    "Markov’s Inequality: The Foundation of Concentration",
    svg_30601,
    "The step indicator a 1_{X ≥ a} lies everywhere below X; taking expectations proves P(X ≥ a) ≤ E[X]/a",
    [
        "<strong>Hypothesis & Bound:</strong> For any non-negative random variable $X \\ge 0$ and any threshold $a > 0$, $\\mathbb{P}(X \\ge a) \\le \\frac{\\mathbb{E}[X]}{a}$.",
        "<strong>Indicator Proof:</strong> Observe that $a \\mathbf{1}_{\\{X \\ge a\\}} \\le X \\mathbf{1}_{\\{X \\ge a\\}} \\le X$. Taking expectations preserves monotonicity: $a \\mathbb{E}[\\mathbf{1}_{\\{X \\ge a\\}}] = a \\mathbb{P}(X \\ge a) \\le \\mathbb{E}[X]$.",
        "<strong>Master Engine:</strong> Markov is the foundational engine generating Chebyshev (via $\\phi(u)=u^2$), Chernoff (via $\\phi(u)=e^{tu}$), and all higher-order concentration inequalities."
    ],
    r"$$X \ge 0, \; a > 0 \implies a\,\mathbf{1}_{\{X \ge a\}} \le X \implies \mathbb{P}(X \ge a) \le \frac{\mathbb{E}[X]}{a}$$",
    "Average wealth in a society: if mean wealth is $50,000, at most 10% of citizens can possess $500,000 or more, otherwise the total wealth would exceed the mean.",
    "Applying Markov directly to random variables with negative values! Markov strictly requires X ≥ 0. For general variables, apply Markov to |X|, (X - μ)², or e^{tX}."
))

# Card 30602: Chebyshev’s Inequality & Dispersion Bounds
svg_30602 = [
    AX(24, 115, 220, 20),
    # Symmetrical distribution
    P("M 30,114 Q 80,114 100,85 Q 120,25 125,25 Q 130,25 150,85 Q 170,114 220,114", fill="none", w=1.8),
    L(125, 25, 125, 114, 1.0, d="2 2"),
    N(125, 125, "μ", 9.5, w="bold"),
    # Left and right rejection tail bands
    L(75, 55, 75, 114, 1.2, d="2 2"),
    L(175, 55, 175, 114, 1.2, d="2 2"),
    N(75, 125, "μ - kσ", 8), N(175, 125, "μ + kσ", 8),
    # Shaded tails
    P("M 30,114 Q 60,114 75,100 L 75,114 Z", fill="#d9dee7", w=1.0),
    P("M 175,100 Q 190,114 220,114 L 175,114 Z", fill="#d9dee7", w=1.0),
    N(120, 50, "P(|X - μ| ≥ kσ) ≤ 1 / k²", 9.5, w="bold"),
    N(120, 138, "Universal dispersion bound: at least (1 - 1/k²) mass lies within k standard deviations", 8)
]
CARDS.append(make_stoma_card(
    6, 2, "VARIANCE BOUND",
    "Chebyshev’s Inequality & Variance Dispersion",
    svg_30602,
    "Chebyshev bounds deviation from the mean: tail probability outside k standard deviations is at most 1/k²",
    [
        "<strong>Formal Statement:</strong> For any random variable with mean $\\mu$ and finite variance $\\sigma^2$, $\\mathbb{P}(|X - \\mu| \\ge \\epsilon) \\le \\frac{\\operatorname{Var}(X)}{\\epsilon^2}$.",
        "<strong>Canonical Form ($k\\sigma$):</strong> Setting $\\epsilon = k\\sigma$, $\\mathbb{P}(|X - \\mu| \\ge k\\sigma) \\le \\frac{1}{k^2}$.",
        "<strong>Distribution-Free Guarantee:</strong> Holds for ANY distribution: at least $75\\%$ of mass lies within $2\\sigma$ ($k=2$), and at least $88.89\\%$ lies within $3\\sigma$ ($k=3$), regardless of skewness."
    ],
    r"$$\mathbb{P}(|X - \mu| \ge \epsilon) \le \frac{\operatorname{Var}(X)}{\epsilon^2}, \qquad \mathbb{P}(|X - \mu| \ge k\sigma) \le \frac{1}{k^2}$$",
    "Factory quality control: regardless of how defective or skewed machine tolerances are, at least 96% of items must lie within 5 standard deviations (failure rate ≤ 4%).",
    "Using Chebyshev when a 1-sided bound is required. For 1-sided deviations P(X - μ ≥ ε), Cantelli's inequality gives the strictly sharper bound σ² / (σ² + ε²)."
))

# Card 30603: The Chernoff Bound & Exponential Tilt
svg_30603 = [
    AX(24, 115, 220, 20),
    # Convex curve e^{-ta} M(t) with minimum
    P("M 35,30 Q 100,105 130,105 Q 160,105 210,30", fill="none", w=2.0),
    C(130, 105, 3.5, fill="#000000"),
    L(130, 105, 130, 114, 1.0, d="2 2"),
    N(130, 126, "t* (optimal tilt)", 8.5, w="bold"),
    N(130, 92, "inf_{t > 0} e^{-ta} M_X(t)", 8.5, w="bold"),
    N(120, 16, "P(X ≥ a) ≤ e^{-ta} M_X(t)  ∀ t > 0", 9, w="bold"),
    N(120, 138, "Exponential Markov bound optimized over t > 0 gives exponential tail decay", 8)
]
CARDS.append(make_stoma_card(
    6, 3, "EXPONENTIAL CONCENTRATION",
    "The Chernoff Bound & Exponential Moment Optimization",
    svg_30603,
    "Applying Markov to e^{tX} and optimizing over tilt parameter t > 0 delivers sharp exponential concentration",
    [
        "<strong>Exponential Markov Step:</strong> For any $t > 0$, $\\mathbb{P}(X \\ge a) = \\mathbb{P}(e^{tX} \\ge e^{ta}) \\le \\frac{\\mathbb{E}[e^{tX}]}{e^{ta}} = e^{-ta} M_X(t)$.",
        "<strong>Convex Dual Optimization:</strong> Squeezing over all $t > 0$ yields the sharpest bound: $\\mathbb{P}(X \\ge a) \\le \\inf_{t > 0} \\exp(-(ta - \\log M_X(t)))$.",
        "<strong>Legendre-Fenchel Conjugate:</strong> Exponent $-I(a) \\triangleq -\\sup_{t > 0}(ta - \\Lambda_X(t))$ is the convex conjugate of the cumulant MGF, giving exponential decay $O(e^{-n I(a)})$ for sample sums."
    ],
    r"$$\mathbb{P}(X \ge a) \le \inf_{t > 0} e^{-ta} M_X(t) = \exp\left(-\sup_{t > 0}[ta - \Lambda_X(t)]\right)$$",
    "Focusing an optical laser: tuning parameter t sharpens the probability bound until it reaches the absolute tightest physical focus point.",
    "Forgetting the constraint t > 0 for upper tails (and t < 0 for lower tails P(X ≤ a)). Plugging negative t into an upper-tail bound flips the inequality direction!"
))

# Card 30604: Jensen’s Inequality & Convex Geometry
svg_30604 = [
    AX(24, 115, 220, 20),
    # Convex curve g(x)
    P("M 40,105 Q 120,110 190,30", fill="none", w=2.0),
    N(195, 30, "g(x)", 9.5, w="bold"),
    # Chord / Secant line
    L(55, 100, 175, 45, 1.2, d="2 2"),
    # Point E[X] on x-axis
    L(115, 114, 115, 96, 1.0, d="2 2"),
    C(115, 96, 3, fill="#000000"),
    N(115, 126, "E[X]", 8.5),
    N(80, 96, "g(E[X])", 8.5, w="bold"),
    # E[g(X)] on secant line
    C(115, 72, 3, fill="#000000"),
    N(80, 72, "E[g(X)]", 8.5, w="bold"),
    L(115, 72, 115, 96, 1.4),
    N(155, 85, "g(E[X]) ≤ E[g(X)]", 9, w="bold"),
    N(120, 138, "For convex g, secants lie above the curve: the function of the mean is below the mean of the function", 8)
]
CARDS.append(make_stoma_card(
    6, 4, "CONVEXITY",
    "Jensen’s Inequality: Secant Dominance & Convexity",
    svg_30604,
    "For any convex function g, the secant line lies above the curve, ensuring g(E[X]) ≤ E[g(X)]",
    [
        "<strong>Convexity Definition:</strong> Function $g$ is convex if $g(\\lambda x + (1-\\lambda)y) \\le \\lambda g(x) + (1-\\lambda)g(y)$ for all $\\lambda \\in [0, 1]$.",
        "<strong>Jensen’s Statement:</strong> If $g$ is convex and expectations exist, $g(\\mathbb{E}[X]) \\le \\mathbb{E}[g(X)]$.",
        "<strong>Supporting Hyperplane Proof:</strong> At $\\mu = \\mathbb{E}[X]$, a tangent subgradient $c$ satisfies $g(x) \\ge g(\\mu) + c(x - \\mu)$. Taking expectations: $\\mathbb{E}[g(X)] \\ge g(\\mu) + c(0) = g(\\mathbb{E}[X])$."
    ],
    r"$$g \text{ convex} \implies g(\mathbb{E}[X]) \le \mathbb{E}[g(X)]; \qquad g \text{ concave} \implies \mathbb{E}[g(X)] \le g(\mathbb{E}[X])$$",
    "Driving with varying speeds: traveling 100 miles at 40 mph then 100 miles at 60 mph takes longer than driving constant 50 mph because travel time T(v) = D/v is strictly convex.",
    "Reversing the inequality for concave functions! For concave functions like log(x) or √x, E[g(X)] ≤ g(E[X]) (which directly proves the Arithmetic-Geometric Mean AM-GM inequality)."
))

# Card 30605: Cauchy-Schwarz & Hoeffding’s Inequality
svg_30605 = [
    box(16, 20, 96, 42, "Cauchy-Schwarz:\n|E[XY]|² ≤ E[X²]E[Y²]\n(Equality ⇔ Y = cX)", "#ffffff", 8),
    box(128, 20, 96, 42, "Hoeffding's Lemma:\nX ∈ [a, b], E[X]=0\nM_X(t) ≤ e^{t²(b-a)²/8}", "#ffffff", 8),
    # Hoeffding sum inequality box
    R(16, 72, 208, 42, fill="#f8fafc", sw=1.3),
    N(120, 86, "Hoeffding's Inequality (Sums of Bounded Independent RVs):", 8, w="bold"),
    N(120, 102, "P(∑ (Xᵢ - μᵢ) ≥ t) ≤ exp( - 2t² / ∑ (bᵢ - aᵢ)² )", 8.5, w="bold"),
    N(120, 138, "Cauchy-Schwarz bounds correlations (|ρ| ≤ 1); Hoeffding bounds tails of bounded sums", 8)
]
CARDS.append(make_stoma_card(
    6, 5, "CANONICAL BOUNDS",
    "Cauchy-Schwarz & Hoeffding’s Concentration Inequality",
    svg_30605,
    "Cauchy-Schwarz bounds inner products; Hoeffding provides sub-Gaussian tails for bounded independent sums",
    [
        "<strong>Cauchy-Schwarz:</strong> $|\\mathbb{E}[XY]|^2 \\le \\mathbb{E}[X^2]\\,\\mathbb{E}[Y^2]$. Equality holds if and only if $Y = c X$ almost surely for some constant $c$. Guarantees correlation $|\\rho_{X,Y}| \\le 1$.",
        "<strong>Hoeffding's Lemma:</strong> If $X \\in [a, b]$ with $\\mathbb{E}[X] = 0$, its MGF satisfies sub-Gaussian proxy $M_X(t) \\le \\exp\\left(\\frac{t^2(b - a)^2}{8}\\right)$.",
        "<strong>Hoeffding’s Inequality:</strong> For independent $X_i \\in [a_i, b_i]$, $\\mathbb{P}(\\sum_{i=1}^n (X_i - \\mu_i) \\ge t) \\le \\exp\\left(-\\frac{2t^2}{\\sum_{i=1}^n (b_i - a_i)^2}\\right)$."
    ],
    r"$$|\mathbb{E}[XY]|^2 \le \mathbb{E}[X^2]\mathbb{E}[Y^2], \quad \mathbb{P}\left(\sum_{i=1}^n (X_i - \mu_i) \ge t\right) \le \exp\left(-\frac{2t^2}{\sum_{i=1}^n (b_i - a_i)^2}\right)$$",
    "Geometric dot product: the shadow cast by vector X onto Y cannot exceed the product of their lengths (|cos θ| ≤ 1).",
    "Applying Hoeffding to dependent variables! Mutual independence of X₁,...,X_n is strictly mandatory to factorize the joint MGF in Hoeffding's proof."
))

# Card 30606: Worked Benchmark: Chernoff vs Chebyshev on Fair Coins
svg_30606 = [
    AX(24, 115, 220, 20),
    # Chebyshev 1/n decay (slow)
    P("M 30,35 Q 70,75 120,95 Q 170,105 215,110", fill="none", w=1.6, dash="3 3"),
    N(200, 100, "Chebyshev: 4/n", 7.5),
    # Chernoff e^{-cn} decay (exponentially fast)
    P("M 30,35 Q 45,95 70,112 L 215,114", fill="none", w=2.2),
    N(90, 80, "Chernoff: e^{-n/8}", 8, w="bold"),
    # Comparison box
    box(110, 24, 114, 46, "For n = 100:\nChebyshev: ≤ 0.04 (4%)\nChernoff: ≤ 3.7 × 10⁻⁶", "#f8fafc", 8),
    N(120, 138, "Chernoff delivers exponential concentration; Chebyshev provides only weak polynomial decay", 8)
]
CARDS.append(make_stoma_card(
    6, 6, "WORKED BENCHMARK",
    "Worked Benchmark: Chernoff vs Chebyshev on Coin Flips",
    svg_30606,
    "Chebyshev gives weak O(1/n) polynomial bounds; Chernoff harnesses all moments to achieve exponential decay",
    [
        "<strong>Problem Setup:</strong> Let $S_n \\sim \\text{Binomial}(n, 1/2)$, so $\\mu = n/2$ and $\\sigma^2 = n/4$. Bound tail $\\mathbb{P}(S_n \\ge \\frac{3}{4}n)$ ($\ge 25\\%$ excess).",
        "<strong>Chebyshev Evaluation:</strong> $\\mathbb{P}(S_n - n/2 \\ge n/4) \\le \\frac{\\sigma^2}{(n/4)^2} = \\frac{n/4}{n^2/16} = \\frac{4}{n}$ (slow polynomial rate $O(1/n)$).",
        "<strong>Chernoff Evaluation:</strong> Hoeffding gives $\\exp(-2(n/4)^2 / n) = \\exp(-n/8)$. For $n=100$: Chebyshev gives $\\le 0.04$, while Chernoff gives $\\le e^{-12.5} \\approx 3.7 \\times 10^{-6}$!"
    ],
    r"$$\mathbb{P}\left(S_n \ge \tfrac{3}{4}n\right) \le \frac{4}{n} \quad (\text{Chebyshev}) \quad \text{vs} \quad \exp\left(-\frac{n}{8}\right) \quad (\text{Chernoff/Hoeffding})$$",
    "A structural safety factor: Chebyshev guarantees the bridge stands with 96% confidence, while Chernoff proves the failure probability is under four in a million.",
    "Using Chebyshev for large sample sizes (n >> 100). Chebyshev captures only 2nd moments, missing the exponential destructive cancellation across independent terms."
))

# ==============================================================================
# TOPIC 07: JOINT, MARGINAL & CONDITIONAL DISTRIBUTIONS (30701 - 30706)
# ==============================================================================

# Card 30701: Joint CDF & The 2D Rectangle Formula
svg_30701 = [
    AX(24, 115, 220, 20),
    # 2D Rectangle (a, b] x (c, d]
    R(60, 45, 90, 50, fill="#d9dee7", sw=1.5),
    N(105, 70, "P(a < X ≤ b, c < Y ≤ d)", 7.5, w="bold"),
    # Vertices
    C(60, 95, 3, fill="#000000"), N(50, 102, "(a, c)", 7),
    C(150, 95, 3, fill="#000000"), N(160, 102, "(b, c)", 7),
    C(60, 45, 3, fill="#000000"), N(50, 40, "(a, d)", 7),
    C(150, 45, 3, fill="#000000"), N(160, 40, "(b, d)", 7),
    # Formula box
    box(24, 18, 192, 22, "Δ_{a,c}^{b,d} F = F(b, d) - F(a, d) - F(b, c) + F(a, c) ≥ 0", "#ffffff", 7.5),
    N(120, 138, "2D CDF must satisfy 2-monotonicity: all rectangle probabilities must be non-negative", 8)
]
CARDS.append(make_stoma_card(
    7, 1, "JOINT CDF",
    "Joint Cumulative Distribution Function & 2D Rectangle Measure",
    svg_30701,
    "The 2D rectangle formula computes cell probability by inclusion-exclusion of quadrant corners",
    [
        "<strong>Joint CDF:</strong> $F_{X,Y}(x, y) \\triangleq \\mathbb{P}(X \\le x, Y \\le y)$ evaluates the cumulative measure of infinite lower-left quadrant $(-\\infty, x] \\times (-\\infty, y]$.",
        "<strong>2D Rectangle Measure:</strong> Probability in $(a, b] \\times (c, d]$ is $\\mathbb{P}(a < X \\le b, c < Y \\le d) = F(b, d) - F(a, d) - F(b, c) + F(a, c) \\ge 0$.",
        "<strong>2-Monotonicity Axiom:</strong> Increasing in $x$ and $y$ separately is NOT enough! The 2D cross-difference must be non-negative for every rectangle."
    ],
    r"$$\mathbb{P}(a < X \le b, c < Y \le d) = F_{X,Y}(b, d) - F_{X,Y}(a, d) - F_{X,Y}(b, c) + F_{X,Y}(a, c) \ge 0$$",
    "Measuring the area of an interior floor tile by subtracting left and bottom border carpets and restoring the doubly subtracted corner piece.",
    "Assuming coordinate-wise monotonicity guarantees a valid 2D CDF. Functions exist where ∂F/∂x ≥ 0 and ∂F/∂y ≥ 0, yet the rectangle measure evaluates to a negative number!"
))

# Card 30702: Joint PDF & Probability as Volume
svg_30702 = [
    # 3D isometric representation of surface z = f(x, y)
    PG("40,110 140,110 200,75 100,75", fill="#f8fafc", w=1.2),
    N(120, 102, "Region A in xy-plane", 8),
    # Column of probability volume
    P("M 80,95 L 80,45 Q 120,30 160,40 L 160,85 L 80,95 Z", fill="#d9dee7", w=1.4),
    N(120, 58, "Volume = P((X, Y) ∈ A)", 8, w="bold"),
    N(165, 30, "z = f_{X,Y}(x, y)", 8.5, w="bold"),
    N(120, 138, "Joint density: Probability is volume under 2D surface; f(x, y) = ∂²F / ∂x∂y", 8.5)
]
CARDS.append(make_stoma_card(
    7, 2, "CONTINUOUS 2D",
    "Joint Probability Density Function & Probability as Volume",
    svg_30702,
    "The joint PDF f_{X,Y}(x, y) defines a surface whose volume above any 2D region A equals P((X, Y) ∈ A)",
    [
        "<strong>Mixed Derivative:</strong> If $F_{X,Y}$ is differentiable, the joint PDF is $f_{X,Y}(x, y) = \\frac{\\partial^2 F_{X,Y}(x, y)}{\\partial x \\partial y}$.",
        "<strong>Volume Representation:</strong> For any Borel region $A \\subseteq \\mathbb{R}^2$, $\\mathbb{P}((X, Y) \\in A) = \\iint_A f_{X,Y}(x, y)\\,dx\\,dy$.",
        "<strong>Normalization:</strong> $f_{X,Y}(x, y) \\ge 0$ everywhere and total volume $\\int_{-\\infty}^\\infty \\int_{-\\infty}^\\infty f_{X,Y}(x, y)\\,dx\\,dy = 1$."
    ],
    r"$$f_{X,Y}(x, y) = \frac{\partial^2 F_{X,Y}(x, y)}{\partial x \partial y}, \qquad \mathbb{P}((X, Y) \in A) = \iint_A f_{X,Y}(x, y)\,dx\,dy$$",
    "A topographical relief map of sand on a tabletop: the probability of a falling drop hitting zone A is the exact physical volume of sand standing directly over A.",
    "Swapping integration order in non-rectangular domains without adjusting boundaries! For coupled domains like 0 ≤ x ≤ y ≤ 1, ∫₀¹ dx ∫_x¹ dy = ∫₀¹ dy ∫₀^y dx."
))

# Card 30703: Marginal Distributions via Integration / Summation
svg_30703 = [
    # 2D Joint ellipse
    E(115, 65, 45, 28, rot=20, fill="#f1f5f9", w=1.4),
    N(115, 65, "f_{X,Y}(x, y)", 8.5, w="bold"),
    # Marginal X projection below
    AX(24, 115, 220, 20),
    L(70, 65, 70, 114, 0.8, d="2 2"),
    L(160, 65, 160, 114, 0.8, d="2 2"),
    P("M 70,114 Q 115,85 160,114", fill="none", w=2.0),
    N(115, 96, "f_X(x) = ∫ f(x, y) dy", 8, w="bold"),
    # Marginal Y projection on left
    P("M 24,40 Q 42,65 24,90", fill="none", w=2.0),
    N(40, 35, "f_Y(y) = ∫ f(x, y) dx", 7.5),
    N(120, 138, "Marginalization collapses dimensions by integrating out the unwanted variable", 8)
]
CARDS.append(make_stoma_card(
    7, 3, "MARGINALIZATION",
    "Marginal Distributions: Collapsing Dimensions",
    svg_30703,
    "Marginals project joint densities onto 1D coordinate axes by integrating out the orthogonal variable",
    [
        "<strong>Continuous Marginalization:</strong> $f_X(x) = \\int_{-\\infty}^\\infty f_{X,Y}(x, y)\\,dy$ and $f_Y(y) = \\int_{-\\infty}^\\infty f_{X,Y}(x, y)\\,dx$.",
        "<strong>Discrete Marginalization:</strong> $p_X(x) = \\sum_{y} p_{X,Y}(x, y)$ and $p_Y(y) = \\sum_{x} p_{X,Y}(x, y)$ (row and column sums).",
        "<strong>Correlation Erasure:</strong> Marginals retain only single-variable laws, discarding all mutual dependence structure. Infinite distinct joints share the same marginals."
    ],
    r"$$f_X(x) = \int_{-\infty}^\infty f_{X,Y}(x, y)\,dy, \qquad p_X(x) = \sum_{y} p_{X,Y}(x, y)$$",
    "A 2D shadow of a flying bird: the shadow on the ground collapses vertical altitude while preserving horizontal ground position.",
    "Neglecting dependent boundary limits during integration! If the support is triangular 0 ≤ y ≤ x ≤ 1, then f_X(x) = ∫₀^x f(x, y)dy, NOT ∫₀¹!"
))

# Card 30704: Conditional Distributions & Slicing Densities
svg_30704 = [
    AX(24, 115, 220, 20),
    # 2D contour ellipses
    E(120, 65, 55, 30, fill="none", w=1.2),
    E(120, 65, 35, 18, fill="none", w=1.2),
    # Vertical slice at X = x
    L(140, 25, 140, 114, 1.8),
    C(140, 65, 3.5, fill="#000000"),
    N(140, 126, "X = x", 9, w="bold"),
    # Sliced distribution
    box(150, 40, 80, 36, "Slice profile:\nf_{Y|X}(y|x) =\nf(x, y) / f_X(x)", "#ffffff", 7.5),
    N(120, 138, "Conditional PDF is the 1D slice along X=x re-normalized by 1/f_X(x) to integrate to 1", 8)
]
CARDS.append(make_stoma_card(
    7, 4, "CONDITIONAL DENSITIES",
    "Conditional Density: Slicing and Renormalizing",
    svg_30704,
    "The conditional PDF f_{Y|X}(y|x) is a 1D cross-sectional slice of the joint surface normalized to area 1",
    [
        "<strong>Formal Definition:</strong> For any $x$ with $f_X(x) > 0$, the conditional PDF of $Y$ given $X=x$ is $f_{Y \\mid X}(y \\mid x) \\triangleq \\frac{f_{X,Y}(x, y)}{f_X(x)}$.",
        "<strong>Bona Fide 1D Density:</strong> For fixed $x$, the function $y \\mapsto f_{Y \\mid X}(y \\mid x)$ is a valid density on $\\mathbb{R}$: non-negative and integrates to $\\int_{-\\infty}^\\infty f_{Y \\mid X}(y \\mid x)\\,dy = 1$.",
        "<strong>Cross-Section Geometry:</strong> Taking a knife slice across the 2D density mountain along $X=x$, dividing by marginal $f_X(x)$ to restore unit area."
    ],
    r"$$f_{Y \mid X}(y \mid x) = \frac{f_{X,Y}(x, y)}{f_X(x)}, \quad f_X(x) > 0; \qquad \int_{-\infty}^\infty f_{Y \mid X}(y \mid x)\,dy = 1$$",
    "A CT scan slice through a medical patient: isolating the 2D organ profile at a fixed longitudinal position x.",
    "Borel-Kolmogorov Paradox: conditioning continuous distributions on measure-zero curves g(X,Y)=0 depends on the coordinate parametrization! Slicing is well-defined along coordinate projections."
))

# Card 30705: Independence of RVs & Product Support Theorem
svg_30705 = [
    # Product rectangle support (Independent)
    R(24, 25, 85, 65, fill="#f1f5f9", sw=1.3),
    N(66, 57, "S_X × S_Y\n(Product Set)", 8),
    N(66, 102, "Independent OK", 8.5, w="bold"),
    # Non-product triangular support (Dependent)
    PG("140,90 210,90 210,25", fill="#d9dee7", w=1.3),
    N(185, 70, "Coupled Support\n0 ≤ y ≤ x ≤ 1", 7.5),
    N(175, 102, "Coupled ⇒ Dependent!", 8.5, w="bold"),
    N(120, 138, "Independence REQUIRES: (1) density factorizes f(x, y)=g(x)h(y) AND (2) support is a product set", 8)
]
CARDS.append(make_stoma_card(
    7, 5, "INDEPENDENCE",
    "Independence: Factorization & The Product Support Test",
    svg_30705,
    "Independence requires both algebraic density factorization and an uncoupled Cartesian product support",
    [
        "<strong>Definition:</strong> $X \\perp Y \\iff F_{X,Y}(x, y) = F_X(x) F_Y(y)$ for all $x, y$, equivalent to $f_{X,Y}(x, y) = f_X(x) f_Y(y)$ almost everywhere.",
        "<strong>Product Support Requirement:</strong> Independence strictly REQUIRES the support $\\operatorname{supp}(X, Y)$ to be a Cartesian product set $S_X \\times S_Y$ (e.g. a rectangle).",
        "<strong>Factorization Test:</strong> If $f_{X,Y}(x, y) = g(x) h(y)$ AND the support is a product set, then $X \\perp Y$, with marginals proportional to $g(x)$ and $h(y)$."
    ],
    r"$$X \perp Y \iff f_{X,Y}(x, y) = f_X(x) f_Y(y) \quad \forall (x, y) \in S_X \times S_Y$$",
    "A standard chessboard: choosing a rank (1-8) and a file (A-H) are completely independent; on a triangular board, the choice of rank restricts available files.",
    "Declaring independence when f(x, y) = 4xy on coupled domain 0 ≤ x ≤ y ≤ 1! Even though the algebraic formula factorizes, coupled boundary limits destroy independence instantly."
))

# Card 30706: Worked Benchmark: Coupled Triangular Support Uniform Density
svg_30706 = [
    AX(24, 115, 220, 20),
    # Right triangle 0 ≤ y ≤ x ≤ 1
    PG("40,114 180,114 180,25", fill="#d9dee7", w=1.8),
    L(40, 114, 180, 25, 1.4, d="2 2"),
    N(110, 60, "y = x", 8),
    N(180, 126, "1", 9, w="bold"),
    N(40, 126, "0", 9, w="bold"),
    N(24, 25, "1", 8.5),
    N(130, 85, "f_{X,Y} = 2", 9, w="bold"),
    # Results box
    box(24, 20, 100, 48, "f_X(x) = 2x, x∈[0,1]\nf_Y(y) = 2(1-y), y∈[0,1]\nf_{Y|X}(y|x) = 1/x\n⇒ Y|X ~ Unif[0, x]", "#ffffff", 7),
    N(120, 138, "f_{X,Y} ≠ f_X f_Y ⇒ strongly dependent; conditional expectation E[Y|X=x] = x/2", 8)
]
CARDS.append(make_stoma_card(
    7, 6, "WORKED BENCHMARK",
    "Worked Benchmark: Triangular Support & Dependent Marginals",
    svg_30706,
    "Uniform density on a triangle produces non-uniform marginals and conditional uniform distributions",
    [
        "<strong>Problem Setup:</strong> Uniform density on triangle $T = \\{(x, y) : 0 \\le y \\le x \\le 1\\}$. Area is $1/2$, so $f_{X,Y}(x, y) = 2 \\cdot \\mathbf{1}_{\\{0 \\le y \\le x \\le 1\\}}$.",
        "<strong>Marginal Integrals:</strong> $f_X(x) = \\int_0^x 2\\,dy = 2x$ on $[0, 1]$. $f_Y(y) = \\int_y^1 2\\,dx = 2(1 - y)$ on $[0, 1]$. Product $f_X f_Y = 4x(1-y) \\ne 2 \\implies X \\not\\perp Y$.",
        "<strong>Conditional Uniformity:</strong> $f_{Y \\mid X}(y \\mid x) = \\frac{2}{2x} = \\frac{1}{x} \\mathbf{1}_{\\{0 \\le y \\le x\\}}$, so $Y \\mid X=x \\sim \\text{Uniform}[0, x]$ with $\\mathbb{E}[Y \\mid X=x] = x/2$."
    ],
    r"$$f_{X,Y} = 2, \quad f_X(x) = 2x, \quad f_Y(y) = 2(1-y); \quad f_{Y \mid X}(y \mid x) = \frac{1}{x}\,\mathbf{1}_{\{0 \le y \le x\}}$$",
    "Breaking a stick at point X, then picking a point Y uniformly on the broken piece: Y is bounded by X and cannot be independent of X.",
    "Integrating y from 0 to 1 when finding f_X(x)! Because y ≤ x, integrating past x includes forbidden empty territory, producing an erroneous constant marginal."
))

# Save cards to cards_stoma.js
save_stoma_cards(CARDS)
print(f"Successfully generated {len(CARDS)} cards for StoMA Topics 06 & 07!")
