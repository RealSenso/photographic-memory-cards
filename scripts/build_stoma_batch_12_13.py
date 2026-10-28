"""Build StoMA Topics 12 & 13 (Cards 31201 to 31306).
Dual-coding photographic plates with pure black-and-white vector diagrams.
"""
import sys, os
sys.path.append(os.path.dirname(__file__))
from stoma_lib import (
    T, N, L, V, P, C, R, E, PG, AX, box, svg, make_stoma_card, save_stoma_cards
)

CARDS = []

# ==============================================================================
# TOPIC 12: CONDITIONAL EXPECTATION & MMSE ESTIMATION (31201 - 31206)
# ==============================================================================

# Card 31201: Conditional Expectation: The Unconstrained MMSE Estimator
svg_31201 = [
    # Curved manifold representing L²(σ(X))
    P("M 25,115 Q 120,85 215,115", fill="none", w=1.8),
    N(200, 125, "L²(σ(X)) subspace", 7.5),
    # Target point Y outside
    C(120, 25, 4, fill="#000000"), N(120, 15, "Target Y", 9, w="bold"),
    # Projection down to E[Y|X]
    L(120, 25, 120, 93, 1.8, d="3 3"),
    C(120, 93, 4, fill="#000000"), N(120, 106, "E[Y | X] (MMSE)", 9, w="bold"),
    N(165, 55, "Error: Y - E[Y|X]", 8, w="bold"),
    N(120, 138, "E[Y|X] is the unique projection of Y onto L²(σ(X)), minimizing unconstrained MSE", 8)
]
CARDS.append(make_stoma_card(
    12, 1, "MMSE OPTIMALITY",
    "Conditional Expectation: The Unconstrained MMSE Estimator",
    svg_31201,
    "Conditional expectation E[Y|X] is the optimal unconstrained estimator, minimizing mean squared error over all functions",
    [
        "<strong>Optimization Problem:</strong> Find $g^*(X) = \\arg\\min_{g} \\mathbb{E}[(Y - g(X))^2]$ over ALL measurable functions (linear or non-linear).",
        "<strong>Fundamental Theorem:</strong> The unique minimizer is the conditional expectation: $g^*(X) = \\mathbb{E}[Y \\mid X] = \\int y f_{Y \\mid X}(y \\mid X)\\,dy$.",
        "<strong>Random Variable Character:</strong> $\\mathbb{E}[Y \\mid X]$ is NOT a fixed number! It is a random variable measurable with respect to $\\sigma(X)$, taking value $\\mathbb{E}[Y \\mid X=x]$ when $X=x$."
    ],
    r"$$\hat{Y}_{\text{MMSE}} = \mathbb{E}[Y \mid X] = \arg\min_{g \in \sigma(X)} \mathbb{E}\left[(Y - g(X))^2\right], \qquad \mathbb{E}\left[\mathbb{E}[Y \mid X]\right] = \mathbb{E}[Y]$$",
    "A weather forecaster: after observing thermometer and barometer readings X, your optimal forecast for tomorrow's rain Y is the conditional mean of rain given today's exact instruments.",
    "Treating E[Y|X] as a deterministic number! E[Y|X] is a random variable, a function of X. Only when evaluated at a fixed sample realization X = x does it become a constant."
))

# Card 31202: The Non-Linear Orthogonality Principle: L²(σ(X))
svg_31202 = [
    # Orthogonal projection onto manifold
    P("M 30,110 Q 120,80 210,110", fill="none", w=1.6),
    V(50, 105, 120, 30, 2.0), N(125, 25, "Y", 9, w="bold"),
    V(50, 105, 120, 88, 2.0), N(120, 102, "E[Y | X]", 9, w="bold"),
    L(120, 30, 120, 88, 1.8, d="3 3"),
    # Perpendicular mark
    PG("120,78 110,78 110,88", fill="none", w=1.2),
    box(24, 20, 85, 34, "Error e = Y - E[Y|X]\nOrthogonal to all h(X)", "#f8fafc", 7.5),
    N(120, 138, "Non-linear orthogonality: E[(Y - E[Y|X]) h(X)] = 0 for ALL measurable functions h", 8)
]
CARDS.append(make_stoma_card(
    12, 2, "ORTHOGONALITY",
    "The Non-Linear Orthogonality Principle: L²(σ(X))",
    svg_31202,
    "The MMSE error e = Y - E[Y|X] is orthogonal to every measurable transformation h(X), linear or non-linear",
    [
        "<strong>Orthogonality Condition:</strong> For any measurable function $h(X)$ with $\\mathbb{E}[h(X)^2] < \\infty$, $\\mathbb{E}[(Y - \\mathbb{E}[Y \\mid X]) h(X)] = 0$.",
        "<strong>Zero Residual Prediction:</strong> No transformation of $X$—whether $X, X^2, e^X$, or a deep neural network—can extract any further predictive correlation from the residual error.",
        "<strong>Unbiasedness:</strong> Setting $h(X) = 1$ immediately proves $\\mathbb{E}[Y - \\mathbb{E}[Y \\mid X]] = 0$, guaranteeing that the MMSE estimator is unconditionally unbiased."
    ],
    r"$$\mathbb{E}\left[\left(Y - \mathbb{E}[Y \mid X]\right) h(X)\right] = 0 \quad \forall h \in L^2(\sigma(X))$$",
    "Complete data exhaustion: a gold miner who has extracted every particle of gold from an ore sample: no acid or mechanical wash can extract any remaining trace.",
    "Confusing LLSE with MMSE orthogonality! LLSE error is orthogonal only to affine functions aX + b; MMSE error is orthogonal to ALL measurable non-linear functions h(X)."
))

# Card 31203: The Tower Property & "Taking Out What is Known"
svg_31203 = [
    # Nested information boxes
    box(24, 20, 192, 32, "Nested Conditioning:  E[ E[Y | X₁, X₂] | X₁ ] = E[Y | X₁]\n(Conditioning on LESS information always dominates)", "#ffffff", 8),
    box(24, 60, 192, 32, "Law of Total Expectation:  E[ E[Y | X] ] = E[Y]\n(Average of local conditional means equals unconditional mean)", "#f8fafc", 8),
    box(24, 100, 192, 26, "Taking out what is known:  E[ g(X) Y | X ] = g(X) · E[Y | X]", "#f1f5f9", 8.5),
    N(120, 138, "Information hierarchies: coarser information washes out finer details; known factors factor out", 8)
]
CARDS.append(make_stoma_card(
    12, 3, "TOWER PROPERTY",
    "The Tower Property & 'Taking Out What is Known'",
    svg_31203,
    "Nested conditioning preserves the coarser information filter: E[E[Y|X₁, X₂]|X₁] = E[Y|X₁]",
    [
        "<strong>Tower Property (Total Expectation):</strong> $\\mathbb{E}[\\mathbb{E}[Y \\mid X]] = \\mathbb{E}[Y]$. The expectation of the conditional expectation recovers the unconditional mean.",
        "<strong>Nested Conditioning:</strong> For nested $\\sigma$-algebras $\\mathcal{G}_1 \\subset \\mathcal{G}_2$, $\\mathbb{E}[\\mathbb{E}[Y \\mid \\mathcal{G}_2] \\mid \\mathcal{G}_1] = \\mathbb{E}[Y \\mid \\mathcal{G}_1]$. Conditioning on less information always wins.",
        "<strong>Taking Out What Is Known:</strong> If $g(X)$ is $\\sigma(X)$-measurable, $\\mathbb{E}[g(X) Y \\mid X] = g(X)\\,\\mathbb{E}[Y \\mid X]$. Known variables act as scalars inside the conditional expectation."
    ],
    r"$$\mathbb{E}\left[\mathbb{E}[Y \mid X_1, X_2] \;\middle|\; X_1\right] = \mathbb{E}[Y \mid X_1], \qquad \mathbb{E}[g(X) Y \mid X] = g(X) \mathbb{E}[Y \mid X]$$",
    "A national census: aggregating regional school averages yields the total national average; reporting local data to a high-level authority collapses fine-grained distinctions.",
    "Reversing the tower ordering: E[E[Y|X₁]|X₁, X₂] = E[Y|X₁], NOT E[Y|X₁, X₂]! Finer conditioning cannot invent new information that was already lost."
))

# Card 31204: Law of Total Variance (Eve’s Law)
svg_31204 = [
    # Total variance split bar
    box(24, 20, 192, 28, "Total Variance:  Var(Y)", "#e2e8f0", 9.5),
    # Two component bars below
    box(24, 58, 92, 44, "E[ Var(Y | X) ]\nExpected\nwithin-slice variance\n(Unexplained noise)", "#f8fafc", 7.5),
    N(120, 80, "+", 12, w="bold"),
    box(124, 58, 92, 44, "Var( E[Y | X] )\nVariance of\nconditional mean\n(Explained signal)", "#ffffff", 7.5),
    N(120, 118, "MMSE Error = E[Var(Y | X)] ≤ Var(Y)", 8.5, w="bold"),
    N(120, 138, "Eve's Law: Var(Y) = E[Var(Y | X)] + Var(E[Y | X]) decomposes total risk into noise and signal", 8)
]
CARDS.append(make_stoma_card(
    12, 4, "VARIANCE DECOMPOSITION",
    "Law of Total Variance (Eve’s Law): Noise vs Signal",
    svg_31204,
    "Total variance decomposes into expected conditional variance (noise) plus variance of conditional mean (signal)",
    [
        "<strong>Formal Decomposition:</strong> $\\operatorname{Var}(Y) = \\mathbb{E}[\\operatorname{Var}(Y \\mid X)] + \\operatorname{Var}(\\mathbb{E}[Y \\mid X])$.",
        "<strong>Signal vs Noise:</strong> $\\operatorname{Var}(\\mathbb{E}[Y \\mid X])$ is the variance explained by observation $X$ (signal), while $\\mathbb{E}[\\operatorname{Var}(Y \\mid X)]$ is the residual unexplained dispersion (noise).",
        "<strong>MMSE Error Formula:</strong> The minimum mean squared estimation error is precisely the expected conditional variance: $\\mathbb{E}[(Y - \\hat{Y}_{\\text{MMSE}})^2] = \\mathbb{E}[\\operatorname{Var}(Y \\mid X)] \\le \\operatorname{Var}(Y)$."
    ],
    r"$$\operatorname{Var}(Y) = \mathbb{E}\left[\operatorname{Var}(Y \mid X)\right] + \operatorname{Var}\left(\mathbb{E}[Y \mid X]\right), \qquad \text{MMSE Error} = \mathbb{E}\left[\operatorname{Var}(Y \mid X)\right]$$",
    "Exam scores across a nation: within-school variance (students differing inside each school) PLUS across-school variance (school district averages differing from each other).",
    "Missing one of the two terms in Eve's law! Forgetting Var(E[Y|X]) or E[Var(Y|X)] creates severe underestimates of total population volatility."
))

# Card 31205: MMSE vs LLSE: Non-Linearity & Superiority
svg_31205 = [
    AX(24, 115, 220, 20),
    # Parabola Y = X^2
    P("M 40,30 Q 120,130 200,30", fill="none", w=2.0),
    N(185, 30, "MMSE: E[Y|X] = X²", 8, w="bold"),
    # Flat LLSE line
    L(40, 75, 200, 75, 1.4, d="3 3"),
    N(180, 85, "LLSE: Ŷ = E[Y]", 8),
    box(24, 20, 110, 36, "Symmetric X ⇒ Cov(X, X²)=0\nLLSE error = Var(Y)\nMMSE error = 0!", "#ffffff", 7.5),
    N(120, 138, "MMSE ≤ LLSE ≤ Var(Y); LLSE coincides with MMSE if and only if E[Y|X] is affine", 8.5)
]
CARDS.append(make_stoma_card(
    12, 5, "MMSE VS LLSE",
    "MMSE vs LLSE: Non-Linearity & Superiority",
    svg_31205,
    "LLSE is constrained to straight lines; MMSE explores all curves and can achieve zero error when LLSE fails completely",
    [
        "<strong>Performance Ordering:</strong> $\\text{MMSE Error} = \\mathbb{E}[(Y - \\mathbb{E}[Y \\mid X])^2] \\le \\text{LLSE Error} \\le \\operatorname{Var}(Y)$.",
        "<strong>Extreme Non-Linear Gap:</strong> When $Y = X^2$ with symmetric $X$, $\\operatorname{Cov}(X, Y) = 0$. LLSE outputs a useless flat line $\\hat{Y} = \\mathbb{E}[Y]$, while MMSE outputs exact parabola $\\mathbb{E}[Y \\mid X] = X^2$ with zero error!",
        "<strong>Coincidence Theorem:</strong> MMSE and LLSE are IDENTICAL if and only if $\\mathbb{E}[Y \\mid X]$ is an affine function of $X$ (which holds automatically for jointly Gaussian systems)."
    ],
    r"$$\mathbb{E}\left[\left(Y - \mathbb{E}[Y \mid X]\right)^2\right] \le \mathbb{E}\left[\left(Y - \hat{Y}_{\text{LLSE}}\right)^2\right] \le \operatorname{Var}(Y)$$",
    "Fitting a curve to a circle: a straight ruler (LLSE) fails miserably to follow the circular contour, whereas a flexible spline (MMSE) tracks the contour perfectly.",
    "Assuming LLSE is always a close approximation to MMSE. In non-linear symmetric systems, LLSE has 0% predictive power while MMSE has 100% predictive accuracy."
))

# Card 31206: Worked Benchmark: Random Sums via Eve’s Law
svg_31206 = [
    box(16, 20, 96, 36, "N ~ Poisson(λ)\nFlips of p-coin\nK ~ Binomial(N, p)", "#ffffff", 8),
    V(112, 38, 136, 38, 1.4),
    box(136, 20, 88, 36, "Condition on N:\nE[K | N] = Np\nVar(K | N) = Np(1-p)", "#e2e8f0", 7.5),
    # Moments via Eve
    R(16, 68, 208, 44, fill="#f8fafc", sw=1.3),
    N(120, 82, "E[K] = E[Np] = λp", 8.5, w="bold"),
    N(120, 98, "Var(K) = E[Np(1-p)] + Var(Np) = λp(1-p) + λp² = λp", 8, w="bold"),
    N(120, 138, "Poisson thinning: Total heads K has Mean = Var = λp, confirming K ~ Poisson(λp)", 8.5)
]
CARDS.append(make_stoma_card(
    12, 6, "WORKED BENCHMARK",
    "Worked Benchmark: Random Sums via Eve’s Law (Poisson Thinning)",
    svg_31206,
    "Evaluating random sums through conditioning: E[K] = λp and Var(K) = λp confirm Poisson thinning",
    [
        "<strong>Problem Setup:</strong> Number of coin tosses $N \\sim \\text{Poisson}(\\lambda)$. Each flip lands Heads with probability $p$. Total heads is $K = \\sum_{i=1}^N X_i$.",
        "<strong>Conditional Moments:</strong> Given $N$, $K \\mid N \\sim \\text{Binomial}(N, p)$, so $\\mathbb{E}[K \\mid N] = Np$ and $\\operatorname{Var}(K \\mid N) = Np(1-p)$.",
        "<strong>Moments via Total Variance:</strong> $\\mathbb{E}[K] = \\mathbb{E}[Np] = \\lambda p$. $\\operatorname{Var}(K) = \\mathbb{E}[Np(1-p)] + \\operatorname{Var}(Np) = \\lambda p(1-p) + p^2 \\lambda = \\lambda p$. Matches Poisson($\\lambda p$) thinning!"
    ],
    r"$$\mathbb{E}[K] = \lambda p, \qquad \operatorname{Var}(K) = \mathbb{E}[Np(1-p)] + \operatorname{Var}(Np) = \lambda p \implies K \sim \text{Poisson}(\lambda p)$$",
    "Customer arrivals at a coffee shop: N visitors arrive per hour (Poisson λ); each buys a pastry with probability p; pastry sales K follow a thinned Poisson law λp.",
    "Attempting to compute Var(K) as Var(N) × Var(Xᵢ)! You must use the Law of Total Variance: E[Var(K|N)] + Var(E[K|N])."
))

# ==============================================================================
# TOPIC 13: JOINTLY GAUSSIAN RANDOM VARIABLES (31301 - 31306)
# ==============================================================================

# Card 31301: Multivariate Gaussian PDF & The Mahalanobis Form
svg_31301 = [
    AX(24, 115, 220, 20),
    # Elliptical contour level sets
    E(125, 65, 60, 32, rot=-25, fill="none", w=1.4),
    E(125, 65, 40, 20, rot=-25, fill="none", w=1.4),
    C(125, 65, 3.5, fill="#000000"), N(125, 52, "μ", 9, w="bold"),
    # Principal axes
    L(80, 85, 170, 45, 1.2, d="2 2"),
    N(165, 35, "v₁ (λ₁)", 8, w="bold"),
    box(24, 18, 192, 26, "f_X(x) = (2π)^{-n/2} |Σ|^{-1/2} exp( - 1/2 (x - μ)ᵀ Σ⁻¹ (x - μ) )", "#ffffff", 8),
    N(120, 138, "Mahalanobis distance (x - μ)ᵀ Σ⁻¹ (x - μ) = c² defines concentric elliptical contours", 8)
]
CARDS.append(make_stoma_card(
    13, 1, "MULTIVARIATE NORMAL",
    "Multivariate Gaussian PDF & The Mahalanobis Form",
    svg_31301,
    "Multivariate Gaussian density contours are concentric ellipsoids oriented along the eigenvectors of Σ",
    [
        "<strong>Density Formula:</strong> For non-singular $\\Sigma \\succ 0$, $f_{\\mathbf{X}}(\\mathbf{x}) = \\frac{1}{(2\\pi)^{n/2} |\\Sigma|^{1/2}} \\exp\\left(-\\frac{1}{2}(\\mathbf{x} - \\boldsymbol{\mu})^\\top \\Sigma^{-1} (\\mathbf{x} - \\boldsymbol{\mu})\\right)$ on $\\mathbb{R}^n$.",
        "<strong>Mahalanobis Distance:</strong> Level sets of constant probability density are ellipsoids defined by quadratic form $d_M^2(\\mathbf{x}, \\boldsymbol{\mu}) = (\\mathbf{x} - \\boldsymbol{\mu})^\\top \\Sigma^{-1} (\\mathbf{x} - \\boldsymbol{\mu}) = c^2$.",
        "<strong>Eigenvector Geometry:</strong> Principal axes align with eigenvectors $v_i$ of $\\Sigma$, with half-lengths proportional to standard deviations $\\sqrt{\\lambda_i}$."
    ],
    r"$$f_{\mathbf{X}}(\mathbf{x}) = \frac{1}{(2\pi)^{n/2} |\Sigma|^{1/2}} \exp\left(-\frac{1}{2}(\mathbf{x} - \boldsymbol{\mu})^\top \Sigma^{-1}(\mathbf{x} - \boldsymbol{\mu})\right), \quad \Sigma \succ 0$$",
    "Elliptical spiral galaxy: star density falls exponentially with Mahalanobis distance from the galactic nucleus, stretching along principal inertia axes.",
    "Attempting to write density when |Σ| = 0 (singular covariance). When variables are linearly dependent, the distribution is degenerate and has no density with respect to Lebesgue measure on ℝⁿ."
))

# Card 31302: Fundamental Linear Combination Characterization
svg_31302 = [
    # 2D Gaussian vector X projected along vector t to 1D line
    box(20, 20, 85, 36, "X ~ N(μ, Σ)\nin ℝⁿ", "#ffffff", 8.5),
    V(105, 38, 135, 38, 1.4),
    N(120, 28, "tᵀ X", 8, w="bold"),
    box(135, 20, 85, 36, "tᵀ X ~ N(tᵀμ, tᵀΣt)\nin ℝ¹", "#e2e8f0", 8.5),
    # Affine mapping box
    box(20, 72, 200, 36, "General Linear Map: Y = A X + b  ⇒  Y ~ N(Aμ + b,  A Σ Aᵀ)\n(Linear operations preserve joint Gaussianity unconditionally)", "#f8fafc", 8),
    N(120, 138, "Fundamental theorem: X is jointly Gaussian if and only if EVERY 1D projection tᵀX is Gaussian", 8)
]
CARDS.append(make_stoma_card(
    13, 2, "GAUSSIAN DEFINITION",
    "Fundamental Theorem: All Linear Projections are Gaussian",
    svg_31302,
    "A random vector is jointly Gaussian iff every one-dimensional projection tᵀX is a standard 1D Gaussian",
    [
        "<strong>Fundamental Characterization:</strong> $\\mathbf{X}$ is jointly Gaussian if and only if every linear combination $a_1 X_1 + \\dots + a_n X_n = \\mathbf{t}^\\top \\mathbf{X}$ is a 1D Gaussian for all $\\mathbf{t} \\in \\mathbb{R}^n$.",
        "<strong>Linear Transformation Invariance:</strong> If $\\mathbf{X} \\sim \\mathcal{N}(\\boldsymbol{\mu}, \\Sigma)$ and $Y = A \\mathbf{X} + b$, then $Y$ is strictly Gaussian: $Y \\sim \\mathcal{N}(A\\boldsymbol{\mu} + b, A \\Sigma A^\\top)$.",
        "<strong>Complete Parametrization:</strong> A joint Gaussian law is 100% specified by its mean vector $\\boldsymbol{\mu}$ and covariance matrix $\\Sigma$; all higher cumulants are identically zero."
    ],
    r"$$\mathbf{X} \sim \mathcal{N}(\boldsymbol{\mu}, \Sigma) \iff \mathbf{t}^\top \mathbf{X} \sim \mathcal{N}\left(\mathbf{t}^\top \boldsymbol{\mu}, \; \mathbf{t}^\top \Sigma \mathbf{t}\right) \quad \forall \mathbf{t} \in \mathbb{R}^n$$",
    "Shadows of a 3D cloud: if every 1D shadow cast by a 3D gas cloud from every angle is a bell curve, the 3D cloud itself is an ellipsoidal Gaussian.",
    "Assuming marginally Gaussian variables are jointly Gaussian! Having X ~ N(0, 1) and Y ~ N(0, 1) does NOT imply (X, Y) is jointly Gaussian (e.g. Y = SX with sign flip S)."
))

# Card 31303: Independence <=> Uncorrelated for Joint Gaussians
svg_31303 = [
    # Diagonal covariance matrix
    box(24, 20, 192, 42, "Jointly Gaussian + Cov(Xᵢ, X_j) = 0\n⇒ Σ is diagonal: Σ = diag(σ₁², ..., σ_n²)\n⇒ Exponent separates: ∑ (xᵢ - μᵢ)² / (2σᵢ²)", "#ffffff", 8),
    box(24, 70, 192, 38, "Density factorizes: f_X(x) = f_{X₁}(x₁) ... f_{X_n}(x_n)\n⇒ X₁, ..., X_n are MUTUALLY INDEPENDENT!", "#e2e8f0", 8.5),
    N(120, 138, "For JOINTLY Gaussian vectors: Uncorrelated ⇔ Independent (a unique Gaussian signature)", 8)
]
CARDS.append(make_stoma_card(
    13, 3, "GAUSSIAN INDEPENDENCE",
    "Uncorrelated ⇔ Independent for Joint Gaussians",
    svg_31303,
    "For jointly Gaussian random variables, zero covariance is strictly equivalent to mutual statistical independence",
    [
        "<strong>Unique Invariant:</strong> For JOINTLY Gaussian vectors, $\\operatorname{Cov}(X_i, X_j) = 0 \\iff X_i \\perp X_j$. Zero correlation implies statistical independence.",
        "<strong>Factorization Proof:</strong> When covariances are zero, $\\Sigma = \\operatorname{diag}(\\sigma_i^2)$, so $\\Sigma^{-1} = \\operatorname{diag}(1/\\sigma_i^2)$ and $|\\Sigma| = \\prod \\sigma_i^2$. The quadratic form decouples: $(\\mathbf{x}-\\boldsymbol{\mu})^\\top \\Sigma^{-1}(\\mathbf{x}-\\boldsymbol{\mu}) = \\sum \\frac{(x_i - \\mu_i)^2}{\\sigma_i^2}$.",
        "<strong>Exclusivity:</strong> This equivalence is FALSE for general non-Gaussian variables (and false for variables that are individually Gaussian but not jointly Gaussian)."
    ],
    r"$$\mathbf{X} \text{ jointly Gaussian}, \; \operatorname{Cov}(X_i, X_j) = 0 \iff X_i \perp X_j \iff f_{\mathbf{X}}(\mathbf{x}) = \prod_{i=1}^n f_{X_i}(x_i)$$",
    "Orthogonal thermal velocities: molecular velocity components v_x, v_y, v_z in an ideal gas are uncorrelated and therefore completely independent.",
    "Applying this equivalence without verifying JOINT Gaussianity. If joint normality fails, zero covariance tells you nothing about independence."
))

# Card 31304: Jointly Gaussian Conditioning & MMSE = LLSE
svg_31304 = [
    box(20, 20, 200, 44, "Conditional Law: X₁ | X₂ = x₂ ~ N(μ_{1|2}, Σ_{1|2})\nμ_{1|2} = μ₁ + Σ₁₂ Σ₂₂⁻¹ (x₂ - μ₂)   [Linear in x₂ ⇒ MMSE = LLSE]\nΣ_{1|2} = Σ₁₁ - Σ₁₂ Σ₂₂⁻¹ Σ₂₁       [CONSTANT, independent of x₂!]", "#f8fafc", 8),
    # Geometric illustration of slice
    AX(24, 115, 220, 70),
    L(140, 70, 140, 114, 1.8), N(140, 126, "X₂ = x₂", 8, w="bold"),
    P("M 140,114 Q 160,85 180,114", fill="none", w=1.8),
    N(170, 95, "N(μ_{1|2}, Σ_{1|2})", 7.5),
    N(120, 138, "Gaussian conditional mean is linear (MMSE = LLSE); conditional variance is constant", 8.5)
]
CARDS.append(make_stoma_card(
    13, 4, "GAUSSIAN CONDITIONING",
    "Gaussian Conditioning: Exact Normality & MMSE = LLSE",
    svg_31304,
    "Conditioning a Gaussian vector yields another Gaussian: conditional mean is linear (MMSE = LLSE), and covariance is constant",
    [
        "<strong>Conditional Law:</strong> If $\\begin{bmatrix} X_1 \\\\ X_2 \\end{bmatrix} \\sim \\mathcal{N}\\left(\\begin{bmatrix}\\mu_1\\\\\\mu_2\\end{bmatrix}, \\begin{bmatrix}\\Sigma_{11}&\\Sigma_{12}\\\\\\Sigma_{21}&\\Sigma_{22}\\end{bmatrix}\\right)$, then $X_1 \\mid X_2 = x_2 \\sim \\mathcal{N}(\\mu_{1|2}, \\Sigma_{1|2})$.",
        "<strong>Linear Conditional Mean:</strong> $\\mu_{1|2} = \\mu_1 + \\Sigma_{12} \\Sigma_{22}^{-1}(x_2 - \\mu_2)$. The conditional mean is strictly affine, proving **MMSE $\\equiv$ LLSE**!",
        "<strong>Constant Conditional Covariance:</strong> $\\Sigma_{1|2} = \\Sigma_{11} - \\Sigma_{12} \\Sigma_{22}^{-1} \\Sigma_{21}$ is completely independent of the observed value $x_2$."
    ],
    r"$$X_1 \mid X_2 = x_2 \sim \mathcal{N}\left(\mu_1 + \Sigma_{12}\Sigma_{22}^{-1}(x_2 - \mu_2), \; \Sigma_{11} - \Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21}\right)$$",
    "Linear Kalman Filtering: every updated state estimate is strictly Gaussian; error covariance is independent of measurement values and can be computed offline.",
    "Expecting conditional variance Σ_{1|2} to change with observation x₂! For Gaussians, measurements shift the mean, but uncertainty reduction is invariant to observed data."
))

# Card 31305: Direct Matrix Inversion: Reading Moments from Exponents
svg_31305 = [
    box(20, 20, 200, 36, "Exponent: - 1/2 [ a(x - μ_x)² + 2b(x - μ_x)(y - μ_y) + c(y - μ_y)² ]\nPrecision Matrix:  Σ⁻¹ = [ a  b ;  b  c ]", "#ffffff", 8),
    box(20, 64, 200, 46, "Invert 2×2 Matrix:\nΣ = [ a b ; b c ]⁻¹ = \\frac{1}{ac - b²} [ c  -b ;  -b  a ]\nVar(X) = c / (ac - b²),   Var(Y) = a / (ac - b²),   Cov(X,Y) = -b / (ac - b²)", "#f8fafc", 7.5),
    N(120, 138, "Read moments instantly without integration: off-diagonal in precision is b, not 2b", 8.5)
]
CARDS.append(make_stoma_card(
    13, 5, "GAUSSIAN ALGEBRA",
    "Direct Matrix Inversion: Reading Moments from Quadratic Forms",
    svg_31305,
    "The quadratic form in the exponent is the precision matrix Σ⁻¹; invert analytically to read all moments instantly",
    [
        "<strong>Exponent Identification:</strong> The exponent is $-\\frac{1}{2} (\\mathbf{x} - \\boldsymbol{\mu})^\\top \\Sigma^{-1} (\\mathbf{x} - \\boldsymbol{\mu})$. The matrix of quadratic coefficients IS $\\Sigma^{-1}$!",
        "<strong>2D Analytical Inversion:</strong> If $\\Sigma^{-1} = \\begin{bmatrix} a & b \\\\ b & c \\end{bmatrix}$, then $\\Sigma = \\frac{1}{ac - b^2}\\begin{bmatrix} c & -b \\\\ -b & a \\end{bmatrix}$.",
        "<strong>Direct Moment Extraction:</strong> $\\operatorname{Var}(X) = \\frac{c}{ac - b^2}$, $\\operatorname{Var}(Y) = \\frac{a}{ac - b^2}$, and $\\operatorname{Cov}(X, Y) = \\frac{-b}{ac - b^2}$. Zero integration needed!"
    ],
    r"$$-\frac{1}{2}\begin{bmatrix}x \\ y\end{bmatrix}^\top \begin{bmatrix}a & b \\ b & c\end{bmatrix}\begin{bmatrix}x \\ y\end{bmatrix} \implies \Sigma = \begin{bmatrix}a & b \\ b & c\end{bmatrix}^{-1} = \frac{1}{ac - b^2}\begin{bmatrix}c & -b \\ -b & a\end{bmatrix}$$",
    "Reading an prescription bottle: the numbers in the quadratic exponent directly specify the precision matrix without needing to recalculate the volume.",
    "Forgetting the factor of 2 in cross-term 2b xy! The off-diagonal element of Σ⁻¹ is b, NOT 2b. The matrix must be symmetric."
))

# Card 31306: Worked Benchmark: Non-Jointly Gaussian Marginals (Y = S · X)
svg_31306 = [
    AX(24, 115, 220, 20),
    # X-shaped scatter plot (y = x and y = -x)
    L(50, 100, 190, 30, 1.8),
    L(50, 30, 190, 100, 1.8),
    N(180, 25, "Y = X", 8, w="bold"),
    N(180, 108, "Y = -X", 8, w="bold"),
    # Description box
    box(24, 20, 100, 44, "X ~ N(0, 1)\nS = ±1 (p = 1/2)\nY = S · X ~ N(0, 1)\nCov(X, Y) = 0", "#ffffff", 7.5),
    N(120, 138, "Both X, Y ~ N(0, 1) and Cov=0, but P(X+Y=0)=1/2 ⇒ NOT jointly Gaussian!", 8)
]
CARDS.append(make_stoma_card(
    13, 6, "WORKED BENCHMARK",
    "Worked Benchmark: Marginally Normal ≠ Jointly Normal (Y = S · X)",
    svg_31306,
    "Classic counterexample: X and Y are each standard normal and uncorrelated, yet completely dependent and not jointly Gaussian",
    [
        "<strong>Setup:</strong> Let $X \\sim \\mathcal{N}(0, 1)$ and let $S \\in \\{-1, +1\\}$ with $\\mathbb{P}(S = 1) = \\mathbb{P}(S = -1) = 1/2$ independently of $X$. Define $Y = S \\cdot X$.",
        "<strong>Marginal Normality & Zero Covariance:</strong> By symmetry, $Y \\sim \\mathcal{N}(0, 1)$ and $\\operatorname{Cov}(X, Y) = \\mathbb{E}[S X^2] = \\mathbb{E}[S]\\mathbb{E}[X^2] = 0(1) = 0$.",
        "<strong>Non-Gaussian Joint Law:</strong> The sum $X + Y = X(1 + S)$ equals $2X$ with probability $1/2$, and equals $0$ with probability $1/2$. It has atom $\\mathbb{P}(X + Y = 0) = 1/2$, so $X+Y$ is NOT normal $\\implies (X, Y)$ is NOT jointly Gaussian!"
    ],
    r"$$X, Y \sim \mathcal{N}(0, 1), \quad \operatorname{Cov}(X, Y) = 0, \quad \text{yet } \mathbb{P}(X + Y = 0) = \tfrac{1}{2} \implies (X, Y) \text{ NOT jointly Gaussian!}$$",
    "An 'X'-shaped target: projection onto either coordinate axis produces a smooth Gaussian shadow, but projection along the diagonal reveals a sharp 50% spike at the origin.",
    "Concluding independence because Cov(X, Y) = 0! They are uncorrelated, but |Y| = |X| (complete deterministic dependence). Joint normality is strictly required for uncorrelated ⇔ independent."
))

# Save cards to cards_stoma.js
save_stoma_cards(CARDS)
print(f"Successfully generated {len(CARDS)} cards for StoMA Topics 12 & 13!")
