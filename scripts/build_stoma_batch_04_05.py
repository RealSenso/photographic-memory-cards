"""Build StoMA Topics 04 & 05 (Cards 30401 to 30506).
Dual-coding photographic plates with pure black-and-white vector diagrams.
"""
import sys, os
sys.path.append(os.path.dirname(__file__))
from stoma_lib import (
    T, N, L, V, P, C, R, E, PG, AX, box, svg, make_stoma_card, save_stoma_cards
)

CARDS = []

# ==============================================================================
# TOPIC 04: TRANSFORMATIONS AND FUNCTIONS OF A RANDOM VARIABLE (30401 - 30406)
# ==============================================================================

# Card 30401: The CDF Method for Transformations Y = g(X)
svg_30401 = [
    box(16, 20, 80, 28, "X ~ f_X(x)", "#ffffff", 9.5),
    V(96, 34, 134, 34, 1.4),
    N(115, 26, "Y = g(X)", 7.5, w="bold"),
    box(134, 20, 90, 28, "Find f_Y(y)", "#e2e8f0", 9.5),
    # 2 step boxes
    box(16, 62, 208, 26, "Step 1: F_Y(y) = P(Y ≤ y) = P(g(X) ≤ y) = ∫_{g(x)≤y} f_X(x) dx", "#f8fafc", 8, bold=False),
    box(16, 94, 208, 26, "Step 2: Differentiate: f_Y(y) = d/dy [F_Y(y)]  (by FTC / Leibniz)", "#f1f5f9", 8, bold=False),
    N(120, 134, "The CDF method works for ALL transformations without requiring monotonicity", 8.5, w="bold")
]
CARDS.append(make_stoma_card(
    4, 1, "CDF METHOD",
    "The CDF Method for Transformations Y = g(X)",
    svg_30401,
    "Universal two-step protocol: compute cumulative probability F_Y(y) = P(g(X) ≤ y) and differentiate",
    [
        "<strong>Universal 2-Step Protocol:</strong> Step 1: express the CDF of $Y$ directly in terms of $X$: $F_Y(y) = \\mathbb{P}(Y \\le y) = \\mathbb{P}(g(X) \\le y) = \\int_{\\{x : g(x) \\le y\\}} f_X(x)\\,dx$.",
        "<strong>Differentiation Step:</strong> Step 2: differentiate $F_Y(y)$ with respect to $y$ (via Fundamental Theorem of Calculus or Leibniz rule) to find density $f_Y(y) = F_Y'(y)$.",
        "<strong>Universal Validity:</strong> Works unconditionally for any measurable $g$ (monotonic, non-monotonic, multi-to-one, piecewise) without requiring invertibility."
    ],
    r"$$F_Y(y) = \mathbb{P}(g(X) \le y) = \int_{\{x: g(x) \le y\}} f_X(x)\,dx, \qquad f_Y(y) = \frac{d}{dy} F_Y(y)$$",
    "Pouring fluid through a shaped glass funnel: measuring the accumulated liquid volume below height y directly from the incoming flow.",
    "Differentiating without determining the valid support of Y! You must track y ∈ g(supp(X)); omitting indicator functions 1_{y ∈ support} leads to invalid densities with infinite integrals."
))

# Card 30402: Monotonic Transformation & The 1D Jacobian
svg_30402 = [
    AX(24, 115, 220, 20),
    # Monotonic curve
    P("M 40,105 Q 80,95 130,55 Q 180,25 210,25", fill="none", w=2.0),
    N(180, 20, "y = g(x)", 9.5, w="bold"),
    # dx slice
    L(70, 114, 70, 100, 1.0, d="2 2"),
    L(90, 114, 90, 88, 1.0, d="2 2"),
    N(80, 126, "dx", 8.5),
    # dy slice
    L(24, 100, 70, 100, 1.0, d="2 2"),
    L(24, 88, 90, 88, 1.0, d="2 2"),
    N(16, 94, "dy", 8.5),
    N(150, 85, "f_Y(y)|dy| = f_X(x)|dx|", 9, w="bold"),
    N(120, 138, "f_Y(y) = f_X(g⁻¹(y)) · |dx/dy| = f_X(g⁻¹(y)) / |g'(x)|", 8.5)
]
CARDS.append(make_stoma_card(
    4, 2, "JACOBIAN FORMULA",
    "Monotonic Transformation & The 1D Jacobian",
    svg_30402,
    "Conserving probability mass across differential slices: f_Y(y)|dy| = f_X(x)|dx|",
    [
        "<strong>1-to-1 Mapping:</strong> If $g$ is strictly monotonic and continuously differentiable on the support of $X$, the inverse $x = g^{-1}(y)$ exists uniquely.",
        "<strong>Mass Conservation:</strong> Probability in an infinitesimal interval must match: $f_Y(y)|dy| = f_X(x)|dx| \\implies f_Y(y) = f_X(g^{-1}(y)) \\left|\\frac{dx}{dy}\\right|$.",
        "<strong>Reciprocal Derivative Form:</strong> Expressing via derivative of $g$: $f_Y(y) = \\frac{f_X(g^{-1}(y))}{|g'(g^{-1}(y))|}$ for all $y$ in the image of $g$."
    ],
    r"$$f_Y(y) = f_X\left(g^{-1}(y)\right) \left| \frac{d}{dy} g^{-1}(y) \right| = \frac{f_X(g^{-1}(y))}{|g'(g^{-1}(y))|}, \quad y \in g(\text{supp}(X))$$",
    "Stretching a rubber band: where the rubber stretches thin (|g'| > 1), the local density of ink marks drops inversely to preserve total ink mass.",
    "Omitting the absolute value |dx/dy| for strictly decreasing functions (e.g. Y = -X or Y = 1/X). Probabilities and densities must NEVER be negative!"
))

# Card 30403: Non-Monotonic Transformations & Multi-Branch Sums
svg_30403 = [
    AX(24, 115, 220, 20),
    # Parabola y = x^2 centered at x=120
    P("M 50,25 Q 120,115 190,25", fill="none", w=2.0),
    N(195, 25, "y = x²", 9, w="bold"),
    # Horizontal line at y
    L(24, 55, 215, 55, 1.0, d="3 3"),
    N(16, 55, "y", 9, w="bold"),
    # Roots x1 and x2
    L(75, 55, 75, 114, 1.0, d="2 2"),
    L(165, 55, 165, 114, 1.0, d="2 2"),
    C(75, 55, 3, fill="#000000"),
    C(165, 55, 3, fill="#000000"),
    N(75, 126, "-√y", 8.5, w="bold"),
    N(165, 126, "+√y", 8.5, w="bold"),
    N(120, 85, "Two roots x₁ and x₂ contribute", 8.5, w="bold"),
    N(120, 138, "f_Y(y) = ∑ f_X(xₖ) / |g'(xₖ)| = [f_X(√y) + f_X(-√y)] / (2√y)", 8)
]
CARDS.append(make_stoma_card(
    4, 3, "MULTI-BRANCH MAPPINGS",
    "Non-Monotonic Transformations & Multi-Branch Sums",
    svg_30403,
    "When g is multi-to-one, the output density sums the probability contributions across all preimage branches",
    [
        "<strong>Piecewise Monotonicity:</strong> If $g(x) = y$ has multiple discrete roots $\\{x_1, \\dots, x_k\\}$, split the domain into monotonic segments.",
        "<strong>Branch Summation:</strong> Total density sums contributions from every root: $f_Y(y) = \\sum_{k} f_X(x_k) \\left|\\frac{dx_k}{dy}\\right| = \\sum_{k} \\frac{f_X(x_k)}{|g'(x_k)|}$.",
        "<strong>Canonical Square Law:</strong> For $Y = X^2$, roots are $x = \\pm\\sqrt{y}$, yielding $f_Y(y) = \\frac{1}{2\\sqrt{y}} [f_X(\\sqrt{y}) + f_X(-\\sqrt{y})] \\mathbf{1}_{\\{y > 0\\}}$."
    ],
    r"$$f_Y(y) = \sum_{x_k \in g^{-1}(y)} \frac{f_X(x_k)}{|g'(x_k)|}; \quad Y = X^2 \implies f_Y(y) = \frac{f_X(\sqrt{y}) + f_X(-\sqrt{y})}{2\sqrt{y}}\,\mathbf{1}_{\{y>0\}}$$",
    "Two mountain streams feeding into a single river: the river's water flow rate is the sum of the flow rates from each separate tributary.",
    "Missing branches when g(x) is even or periodic (e.g. Y = |X|, Y = X⁴, Y = cos X). Every real root x_k contributing to y must be included in the sum!"
))

# Card 30404: Probability Integral Transform & Inverse CDF Sampling
svg_30404 = [
    AX(24, 115, 220, 20),
    # CDF curve
    P("M 24,114 C 70,114 90,80 120,60 C 150,40 180,26 215,26", fill="none", w=2.0),
    N(16, 26, "1", 8.5), N(16, 115, "0", 8.5),
    # Mapping U on y-axis to X on x-axis
    L(24, 60, 120, 60, 1.2, d="2 2"),
    V(24, 60, 120, 60, 1.4),
    L(120, 60, 120, 114, 1.2, d="2 2"),
    V(120, 60, 120, 114, 1.4),
    C(120, 60, 3, fill="#000000"),
    N(16, 60, "U", 9.5, w="bold"),
    N(120, 126, "X = F⁻¹(U)", 9.5, w="bold"),
    N(120, 138, "U ~ Unif(0, 1) ⇒ X = F⁻¹(U) has exact distribution F", 8.5)
]
CARDS.append(make_stoma_card(
    4, 4, "GENERATIVE TRANSFORM",
    "Probability Integral Transform & Inverse CDF Sampling",
    svg_30404,
    "Universal algorithm for sampling random variables: apply the quantile function F⁻¹ to Uniform(0, 1)",
    [
        "<strong>Uniformization Theorem:</strong> If $X$ has continuous CDF $F_X$, the transformed variable $U \\triangleq F_X(X)$ is strictly distributed as $\\text{Uniform}(0, 1)$.",
        "<strong>Inverse Sampling Principle:</strong> Conversely, if $U \\sim \\text{Uniform}(0, 1)$, then $X \\triangleq F_X^{-1}(U)$ has exact CDF $F_X$. This is the basis of all computer random number generators.",
        "<strong>Generalized Inverse:</strong> For CDFs with flat zones or jumps, the quantile function $F_X^{-1}(u) \\triangleq \\inf\\{x : F_X(x) \\ge u\\}$ preserves universality."
    ],
    r"$$U = F_X(X) \sim \text{Uniform}(0, 1); \qquad U \sim \text{Uniform}(0, 1) \implies X = F_X^{-1}(U) \sim F_X$$",
    "A standardized grading curve: raw test scores X map into uniform percentile ranks U from 0% to 100%; knowing someone's percentile rank inverts back to their exact score.",
    "Applying F_X(X) ~ Uniform(0, 1) to discrete random variables! For discrete distributions, F_X(X) takes only discrete values and is emphatically NOT uniform."
))

# Card 30405: Chi-Square Distribution as Z^2
svg_30405 = [
    AX(24, 115, 220, 20),
    # Chi-square with 1 d.o.f. curve (asymptote at 0, decaying)
    P("M 28,25 Q 32,80 60,95 Q 110,110 215,114", fill="none", w=2.0),
    N(140, 45, "Y = Z²,  Z ~ N(0, 1)", 9, w="bold"),
    N(140, 62, "f_Y(y) = (2πy)^{-1/2} e^{-y/2}", 8.5),
    N(140, 78, "Gamma(1/2, 1/2) ≡ χ₁²", 8.5, w="bold"),
    N(40, 30, "y → 0⁺ asymptote", 7.5),
    N(120, 138, "Squaring standard normal produces Chi-Square with 1 degree of freedom", 8.5)
]
CARDS.append(make_stoma_card(
    4, 5, "CANONICAL TRANSFORM",
    "Gaussian Square: Derivation of χ₁² Density",
    svg_30405,
    "Squaring a standard normal random variable produces the Chi-Square distribution with 1 degree of freedom",
    [
        "<strong>Derivation:</strong> For $Z \\sim \\mathcal{N}(0, 1)$ and $Y = Z^2$, apply 2-branch formula: $f_Y(y) = \\frac{1}{2\\sqrt{y}}[f_Z(\\sqrt{y}) + f_Z(-\\sqrt{y})]$.",
        "<strong>Symmetry Simplification:</strong> Gaussian symmetry $f_Z(\\sqrt{y}) = f_Z(-\\sqrt{y}) = \\frac{1}{\\sqrt{2\\pi}} e^{-y/2}$ yields $f_Y(y) = \\frac{1}{\\sqrt{2\\pi y}} e^{-y/2} \\mathbf{1}_{\\{y > 0\\}}$.",
        "<strong>Gamma Identification:</strong> Matches standard Gamma PDF $\\frac{\\lambda^\\alpha}{\\Gamma(\\alpha)} y^{\\alpha - 1} e^{-\\lambda y}$ with $\\alpha = 1/2, \\lambda = 1/2$ (using $\\Gamma(1/2) = \\sqrt{\\pi}$)."
    ],
    r"$$Y = Z^2, \; Z \sim \mathcal{N}(0, 1) \implies f_Y(y) = \frac{1}{\sqrt{2\pi y}} e^{-y/2}\,\mathbf{1}_{\{y > 0\}} \sim \chi_1^2 \equiv \text{Gamma}\left(\tfrac{1}{2}, \tfrac{1}{2}\right)$$",
    "Kinetic energy of a gas particle with 1D thermal Gaussian velocity v: energy E = (1/2) m v² clusters heavily near 0 with an exponential decay tail.",
    "Worrying that f_Y(y) → ∞ as y → 0⁺. An integrable pole (y^{-1/2}) is completely legal for continuous probability densities; the integral remains strictly equal to 1."
))

# Card 30406: Worked Benchmark: Cauchy Law via Tangent Transform
svg_30406 = [
    # Unit circle and projection
    E(70, 72, 38, 38, fill="none", w=1.4),
    L(70, 72, 108, 72, 0.8),
    L(108, 18, 108, 126, 1.4),
    N(118, 25, "x = tan θ", 8.5, w="bold"),
    # Angle theta ray
    L(70, 72, 108, 42, 1.2),
    N(84, 64, "θ", 8),
    C(108, 42, 3, fill="#000000"),
    N(116, 44, "X", 8.5, w="bold"),
    # Cauchy formula box
    box(136, 36, 92, 54, "f_X(x) = \\frac{1}{\\pi(1+x²)}\nHeavy Tails\nE[|X|] = ∞", "#f8fafc", 8),
    N(120, 138, "Uniform angle θ ~ Unif(-π/2, π/2) produces Cauchy density with undefined mean", 8)
]
CARDS.append(make_stoma_card(
    4, 6, "WORKED BENCHMARK",
    "Worked Benchmark: Tangent Transform & The Cauchy Law",
    svg_30406,
    "Uniform angular projection generates the standard Cauchy distribution whose heavy tails destroy the mean",
    [
        "<strong>Projection Setup:</strong> Angle $\\Theta \\sim \\text{Uniform}(-\\pi/2, \\pi/2)$ with density $f_\\Theta(\\theta) = 1/\\pi$. Define shoreline coordinate $X = \\tan(\\Theta)$.",
        "<strong>Jacobian Step:</strong> Inverse is $\\theta = \\arctan(x)$, with derivative $\\left|\\frac{d\\theta}{dx}\\right| = \\frac{1}{1 + x^2}$.",
        "<strong>Standard Cauchy PDF:</strong> $f_X(x) = f_\\Theta(\\arctan x) \\left|\\frac{d\\theta}{dx}\\right| = \\frac{1}{\\pi (1 + x^2)}$ on $\\mathbb{R}$. The integral $\\int_{-\\infty}^\\infty |x| f_X(x)dx = \\infty$, so $\\mathbb{E}[X]$ does not exist!"
    ],
    r"$$X = \tan\Theta, \; \Theta \sim \text{Unif}\left(-\tfrac{\pi}{2}, \tfrac{\pi}{2}\right) \implies f_X(x) = \frac{1}{\pi (1 + x^2)}, \quad \mathbb{E}[X] \text{ does not exist!}$$",
    "A spinning lighthouse beam shining onto a straight infinite coastline: the location of the illuminated light spot on the shore obeys the Cauchy distribution.",
    "Claiming E[X] = 0 by symmetry! For Cauchy, the positive tail integral is +∞ and the negative tail is -∞. The expression ∞ - ∞ is undefined, so the expected value does not exist."
))

# ==============================================================================
# TOPIC 05: EXPECTATION, VARIANCE & GENERATING FUNCTIONS (30501 - 30506)
# ==============================================================================

# Card 30501: Expectation, LOTUS & Universal Linearity
svg_30501 = [
    # Seesaw balance
    L(30, 95, 210, 75, 2.0),
    PG("120,85 110,110 130,110", fill="#000000", w=1.2),
    N(120, 125, "Pivot: E[X]", 9, w="bold"),
    # Weights on seesaw
    R(45, 78, 20, 14, fill="#d9dee7", sw=1.2),
    N(55, 88, "x₁", 8),
    R(180, 58, 20, 14, fill="#d9dee7", sw=1.2),
    N(190, 68, "x₂", 8),
    box(24, 20, 192, 30, "Linearity: E[aX + bY] = a E[X] + b E[Y]  (Always holds!)", "#f8fafc", 8.5),
    N(120, 138, "LOTUS: E[g(X)] = ∫ g(x) f_X(x) dx without finding distribution of g(X)", 8)
]
CARDS.append(make_stoma_card(
    5, 1, "EXPECTATION & LOTUS",
    "Expectation, LOTUS & Universal Linearity",
    svg_30501,
    "Expectation is the probability center of mass; linearity holds unconditionally without independence",
    [
        "<strong>Center of Mass:</strong> $\\mathbb{E}[X] \\triangleq \\int_\\Omega X(\\omega) d\\mathbb{P}(\\omega) = \\int_{-\\infty}^\\infty x\\,dF_X(x)$. Exists if and only if $\\mathbb{E}[|X|] < \\infty$.",
        "<strong>LOTUS:</strong> To compute the expected value of $g(X)$, you do NOT need the density of $g(X)$: $\\mathbb{E}[g(X)] = \\int_{-\\infty}^\\infty g(x) f_X(x)\\,dx$ (Law of the Unconscious Statistician).",
        "<strong>Universal Linearity:</strong> $\\mathbb{E}[\\sum_{i=1}^n c_i X_i] = \\sum_{i=1}^n c_i \\mathbb{E}[X_i]$ holds for ANY random variables, requiring ZERO independence assumptions."
    ],
    r"$$\mathbb{E}[g(X)] = \int_{-\infty}^\infty g(x) f_X(x)\,dx, \qquad \mathbb{E}\left[\sum_{i=1}^n c_i X_i\right] = \sum_{i=1}^n c_i \mathbb{E}[X_i]$$",
    "Center of mass of a physical balance beam: the combined center of mass of several objects is always the weighted sum of their individual centers.",
    "Assuming E[g(X)] = g(E[X]). By Jensen's inequality, this holds only for linear/affine functions; for non-linear convex g, E[g(X)] ≥ g(E[X])."
))

# Card 30502: The Tail Sum Integral Formula for E[X]
svg_30502 = [
    AX(24, 115, 220, 20),
    # Survival curve P(X > t)
    P("M 24,35 Q 80,45 130,85 Q 180,110 215,114", fill="none", w=2.0),
    # Shaded area under survival curve
    P("M 24,35 Q 80,45 130,85 Q 180,110 215,114 L 24,114 Z", fill="#d9dee7", w=1.0),
    N(16, 35, "1", 8.5),
    N(120, 75, "Area = E[X]", 10, w="bold"),
    N(160, 40, "P(X > t)", 9, w="bold"),
    N(120, 138, "For non-negative RVs (X ≥ 0): E[X] = ∫₀^∞ P(X > t) dt = ∑_{k=1}^∞ P(X ≥ k)", 8)
]
CARDS.append(make_stoma_card(
    5, 2, "TAIL PROBABILITY",
    "Tail Sum Integral Formula for Non-Negative RVs",
    svg_30502,
    "The expected value of a non-negative random variable equals the integral of its survival function",
    [
        "<strong>Continuous Tail Formula:</strong> For any non-negative random variable $X \\ge 0$, $\\mathbb{E}[X] = \\int_0^\\infty \\mathbb{P}(X > t)\\,dt$.",
        "<strong>Discrete Integer Formula:</strong> For non-negative integer-valued random variables $X \\in \\{0, 1, 2, \\dots\\}$, $\\mathbb{E}[X] = \\sum_{k=1}^\\infty \\mathbb{P}(X \\ge k)$.",
        "<strong>Higher Moments Extension:</strong> $\\mathbb{E}[X^p] = \\int_0^\\infty p t^{p-1} \\mathbb{P}(X > t)\\,dt$ for any $p > 0$ and $X \\ge 0$."
    ],
    r"$$X \ge 0 \implies \mathbb{E}[X] = \int_0^\infty \mathbb{P}(X > t)\,dt = \sum_{k=1}^\infty \mathbb{P}(X \ge k) \quad (X \in \mathbb{N}_0)$$",
    "Measuring the volume of a wedding cake by slicing it horizontally into layers from bottom to top rather than cutting vertical wedges.",
    "Applying the one-sided tail integral to random variables with negative values. For general RVs on ℝ, E[X] = ∫₀^∞ P(X > t)dt - ∫_{-∞}^0 P(X < t)dt."
))

# Card 30503: Variance, Covariance & Bilinear Expansion
svg_30503 = [
    box(16, 20, 96, 36, "Var(X) = E[(X-μ)²]\n= E[X²] - (E[X])²", "#ffffff", 8.5),
    box(128, 20, 96, 36, "Cov(X,Y) =\nE[XY] - E[X]E[Y]", "#ffffff", 8.5),
    # Expansion box
    R(16, 68, 208, 44, fill="#f8fafc", sw=1.3),
    N(120, 82, "Var(X₁ + ... + X_n) = ∑ Var(Xᵢ) + 2 ∑_{i < j} Cov(Xᵢ, X_j)", 8, w="bold"),
    N(120, 98, "If uncorrelated: Var(∑ Xᵢ) = ∑ Var(Xᵢ)", 8.5),
    N(120, 134, "Variance scales quadratically: Var(aX + b) = a² Var(X)", 8.5, w="bold")
]
CARDS.append(make_stoma_card(
    5, 3, "SECOND MOMENTS",
    "Variance, Covariance & Bilinear Expansion",
    svg_30503,
    "Variance measures squared dispersion; sum variance includes all pairwise covariance cross-terms",
    [
        "<strong>Definitions:</strong> $\\operatorname{Var}(X) \\triangleq \\mathbb{E}[(X - \\mu)^2] = \\mathbb{E}[X^2] - (\\mathbb{E}[X])^2 \\ge 0$. Covariance: $\\operatorname{Cov}(X, Y) \\triangleq \\mathbb{E}[(X - \\mu_X)(Y - \\mu_Y)]$.",
        "<strong>Quadratic Scaling:</strong> $\\operatorname{Var}(aX + b) = a^2 \\operatorname{Var}(X)$. Additive constants shift position without altering spread.",
        "<strong>Bilinear Expansion:</strong> $\\operatorname{Var}(\\sum_{i=1}^n X_i) = \\sum_{i=1}^n \\operatorname{Var}(X_i) + 2 \\sum_{i < j} \\operatorname{Cov}(X_i, X_j)$. If pairwise uncorrelated, cross-terms vanish."
    ],
    r"$$\operatorname{Var}\left(\sum_{i=1}^n X_i\right) = \sum_{i=1}^n \operatorname{Var}(X_i) + 2 \sum_{1 \le i < j \le n} \operatorname{Cov}(X_i, X_j)$$",
    "Investment portfolio volatility: total portfolio risk is not merely the sum of asset risks, but is governed primarily by their mutual correlation.",
    "Assuming Cov(X, Y) = 0 implies independence! Zero covariance only means no LINEAR relationship. Deterministic non-linear pairs (e.g. Y = X²) can have Cov(X, Y) = 0."
))

# Card 30504: Moment Generating Functions (MGF) & Uniqueness
svg_30504 = [
    AX(24, 115, 220, 20),
    # Convex MGF curve through (0, 1)
    P("M 30,110 Q 120,105 120,80 Q 120,40 180,25", fill="none", w=2.0),
    C(120, 80, 3, fill="#000000"),
    N(105, 80, "(0, 1)", 8.5, w="bold"),
    N(170, 38, "M_X(t) = E[e^{tX}]", 9, w="bold"),
    L(70, 114, 70, 25, 0.8, d="2 2"),
    L(170, 114, 170, 25, 0.8, d="2 2"),
    N(120, 126, "open interval (-h, h) around 0", 8),
    N(120, 138, "M_X'(0) = E[X],  M_X''(0) = E[X²];  X ⊥ Y ⇒ M_{X+Y}(t) = M_X(t) M_Y(t)", 8)
]
CARDS.append(make_stoma_card(
    5, 4, "GENERATING FUNCTIONS",
    "Moment Generating Functions (MGF) & Uniqueness",
    svg_30504,
    "The MGF generates all moments via derivatives at 0; identity of MGFs uniquely determines the distribution",
    [
        "<strong>Definition:</strong> $M_X(t) \\triangleq \\mathbb{E}[e^{tX}]$. If $M_X(t) < \\infty$ on $(-h, h)$ around $t=0$, then $\\mathbb{E}[X^k] = M_X^{(k)}(0)$ for all $k \\ge 1$.",
        "<strong>Convolution Factorization:</strong> For independent random variables $X \\perp Y$, $M_{X+Y}(t) = \\mathbb{E}[e^{t(X+Y)}] = M_X(t) M_Y(t)$. Sums of RVs become products of MGFs.",
        "<strong>Uniqueness Theorem:</strong> If $M_X(t) = M_Y(t)$ in an open neighborhood around $0$, then $X$ and $Y$ have the exact same probability distribution."
    ],
    r"$$M_X(t) = \mathbb{E}[e^{tX}] = \sum_{k=0}^\infty \frac{t^k}{k!} \mathbb{E}[X^k], \quad X \perp Y \implies M_{X+Y}(t) = M_X(t) M_Y(t)$$",
    "A genetic fingerprint: an analytical formula that uniquely encodes the entire infinite sequence of moments for a probability distribution.",
    "Assuming the MGF always exists! Heavy-tailed distributions (Cauchy, Pareto, Log-Normal) have M_X(t) = ∞ for all t > 0. In such cases, use the Characteristic Function φ_X(t) = E[e^{itX}]."
))

# Card 30505: Probability Generating Functions (PGF) for Discrete RVs
svg_30505 = [
    # Unit disk on complex plane
    E(75, 72, 42, 42, fill="#f8fafc", w=1.4),
    AX(30, 72, 120, 20),
    N(118, 72, "Re(s)", 7), N(75, 26, "Im(s)", 7),
    N(75, 52, "|s| ≤ 1", 8.5, w="bold"),
    C(117, 72, 3, fill="#000000"),
    N(117, 84, "s=1", 8, w="bold"),
    # Formulas on right
    box(130, 24, 96, 44, "G_X(s) = E[s^X]\n= ∑ P(X=k) s^k", "#ffffff", 8.5),
    box(130, 74, 96, 44, "E[X] = G_X'(1)\nVar = G''(1)+G'(1)-(G')²", "#ffffff", 8),
    N(120, 138, "Random Sums / Branching: G_{∑_{i=1}^N Xᵢ}(s) = G_N(G_X(s))", 8)
]
CARDS.append(make_stoma_card(
    5, 5, "DISCRETE GENERATING",
    "Probability Generating Function (PGF) & Branching",
    svg_30505,
    "For integer random variables, the PGF always converges on the unit disk; random sums compose PGFs",
    [
        "<strong>Definition:</strong> For $X \\in \\mathbb{N}_0$, $G_X(s) \\triangleq \\mathbb{E}[s^X] = \\sum_{k=0}^\\infty p_k s^k$. Always converges absolutely for all $|s| \\le 1$ with $G_X(1) = 1$.",
        "<strong>Probability Extraction:</strong> $\\mathbb{P}(X = k) = \\frac{1}{k!} G_X^{(k)}(0)$. Moments: $\\mathbb{E}[X] = G_X'(1)$ and $\\operatorname{Var}(X) = G_X''(1) + G_X'(1) - (G_X'(1))^2$.",
        "<strong>Random Sums (Branching):</strong> If $S_N = \\sum_{i=1}^N X_i$ with $X_i$ i.i.d. and independent of $N$, then $G_{S_N}(s) = G_N(G_X(s))$ (functional composition)."
    ],
    r"$$G_X(s) = \mathbb{E}[s^X] = \sum_{k=0}^\infty \mathbb{P}(X=k) s^k, \quad \mathbb{E}[X] = G_X'(1), \quad G_{\sum_{i=1}^N X_i}(s) = G_N(G_X(s))$$",
    "Russian nesting dolls (Matryoshka): composing G_N with G_X places the offspring distribution directly inside the parent population count.",
    "Evaluating moments at s = 0 instead of s = 1! G_X(0) = P(X = 0), while expectations and variances require derivatives evaluated at s = 1."
))

# Card 30506: Worked Benchmark: Uncorrelated but Strongly Dependent (Y = X^2)
svg_30506 = [
    AX(24, 115, 220, 20),
    # Three points (-1, 1), (0, 0), (1, 1)
    C(60, 45, 5, fill="#000000"),
    N(60, 32, "(-1, 1)", 8.5, w="bold"),
    C(120, 114, 5, fill="#000000"),
    N(120, 102, "(0, 0)", 8.5, w="bold"),
    C(180, 45, 5, fill="#000000"),
    N(180, 32, "(1, 1)", 8.5, w="bold"),
    # Dashed parabola through points
    P("M 40,30 Q 120,130 200,30", fill="none", w=1.3, dash="3 3"),
    N(120, 68, "Cov(X, X²) = E[X³] - E[X]E[X²] = 0 - 0 = 0", 8, w="bold"),
    N(120, 138, "Zero covariance does NOT imply independence! Y is completely determined by X", 8)
]
CARDS.append(make_stoma_card(
    5, 6, "WORKED BENCHMARK",
    "Worked Benchmark: Zero Covariance ≠ Independence (Y = X²)",
    svg_30506,
    "Symmetric non-linear relationships yield exactly zero covariance while being 100% deterministic",
    [
        "<strong>Symmetric Setup:</strong> Let $X \\in \\{-1, 0, 1\\}$ with equal probability $1/3$ each. Let $Y = X^2$.",
        "<strong>Covariance Evaluation:</strong> By symmetry, $\\mathbb{E}[X] = 0$ and $\\mathbb{E}[XY] = \\mathbb{E}[X^3] = \\frac{(-1)^3 + 0^3 + 1^3}{3} = 0$. Thus $\\operatorname{Cov}(X, Y) = 0 - 0 = 0$.",
        "<strong>Complete Dependence:</strong> $\\mathbb{P}(X=0, Y=1) = 0 \\ne \\mathbb{P}(X=0)\\mathbb{P}(Y=1) = \\frac{1}{3} \\times \\frac{2}{3} = \\frac{2}{9}$. Knowing $X$ determines $Y$ with 100% certainty!"
    ],
    r"$$\mathbb{E}[X] = 0, \quad \mathbb{E}[X^3] = 0 \implies \operatorname{Cov}(X, X^2) = 0; \quad \mathbb{P}(X=0, X^2=1) = 0 \ne \tfrac{2}{9}$$",
    "A parabolic satellite dish: knowing horizontal coordinate X dictates vertical focus coordinate Y = X² with exact precision, yet linear correlation registers 0.",
    "Assuming uncorrelated variables are independent! Covariance measures ONLY linear association; quadratic, circular, or higher-order dependencies have Cov = 0."
))

# Save cards to cards_stoma.js
save_stoma_cards(CARDS)
print(f"Successfully generated {len(CARDS)} cards for StoMA Topics 04 & 05!")
