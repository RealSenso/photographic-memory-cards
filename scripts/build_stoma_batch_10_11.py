"""Build StoMA Topics 10 & 11 (Cards 31001 to 31106).
Dual-coding photographic plates with pure black-and-white vector diagrams.
"""
import sys, os
sys.path.append(os.path.dirname(__file__))
from stoma_lib import (
    T, N, L, V, P, C, R, E, PG, AX, box, svg, make_stoma_card, save_stoma_cards
)

CARDS = []

# ==============================================================================
# TOPIC 10: EXCHANGEABLE RANDOM VARIABLES (31001 - 31006)
# ==============================================================================

# Card 31001: Exchangeability Definition & Permutation Invariance
svg_31001 = [
    box(16, 20, 85, 36, "(X₁, X₂, ..., X_n)\nJoint Law P", "#ffffff", 8.5),
    L(101, 38, 139, 38, 1.4, ar=True),
    N(120, 28, "Permute π", 7.5, w="bold"),
    box(139, 20, 85, 36, "(X_{π(1)}, ..., X_{π(n)})\nIdentical Law P", "#e2e8f0", 8.5),
    # Hierarchy Venn
    R(24, 70, 192, 46, fill="#f8fafc", sw=1.3),
    N(120, 84, "i.i.d.  ⊂  Exchangeable  ⊂  Identically Distributed", 9, w="bold"),
    N(120, 102, "Order does not matter; variables are symmetric but CAN be dependent", 7.5),
    N(120, 138, "Exchangeability: Joint distribution is invariant under all permutations π ∈ S_n", 8.5)
]
CARDS.append(make_stoma_card(
    10, 1, "EXCHANGEABILITY",
    "Exchangeability: Permutation Invariance of Joint Law",
    svg_31001,
    "A sequence is exchangeable if its joint distribution is completely unchanged by any index permutation",
    [
        "<strong>Formal Definition:</strong> $(X_1, \\dots, X_n)$ is exchangeable if $(X_1, \\dots, X_n) \\stackrel{d}{=} (X_{\\pi(1)}, \\dots, X_{\\pi(n)})$ for every permutation $\\pi \\in S_n$.",
        "<strong>Hierarchy:</strong> $\\text{i.i.d.} \\subsetneq \\text{Exchangeable} \\subsetneq \\text{Identically Distributed}$. Exchangeability is strictly weaker than i.i.d. because mutual dependence is permitted.",
        "<strong>Equi-marginality:</strong> All $X_i$ share identical marginal distributions $F$, and all pairs $(X_i, X_j)$ share identical joint bivariate laws."
    ],
    r"$$(X_1, \dots, X_n) \stackrel{d}{=} (X_{\pi(1)}, \dots, X_{\pi(n)}) \quad \forall \pi \in S_n; \qquad \text{i.i.d.} \subset \text{Exchangeable}$$",
    "Dealing hands in poker: whether a royal card is dealt first, third, or fifth, the joint probability of the entire hand configuration remains identical.",
    "Confusing exchangeable with i.i.d.! Exchangeable variables can be strongly correlated (e.g. sampling without replacement from a finite urn)."
))

# Card 31002: Marginal Invariance & Equi-Correlation Property
svg_31002 = [
    # Covariance Matrix showing identical diagonal and identical off-diagonals
    box(30, 20, 180, 85, "Σ =\n[ σ²    ρσ²  ...  ρσ² ]\n[ ρσ²   σ²   ...  ρσ² ]\n[ ...   ...  ...  ... ]\n[ ρσ²   ρσ²  ...  σ²  ]", "#ffffff", 8.5),
    N(120, 118, "Var(Xᵢ) = σ²   and   Corr(Xᵢ, X_j) = ρ  for all i ≠ j", 8.5, w="bold"),
    N(120, 138, "Symmetry forces all variances to be equal and all pairwise covariances to be identical", 8)
]
CARDS.append(make_stoma_card(
    10, 2, "EQUI-CORRELATION",
    "Equi-Marginality & Universal Pairwise Equi-Correlation",
    svg_31002,
    "Exchangeability imposes compound symmetry: all variances are identical and all pairwise correlations match",
    [
        "<strong>Marginal Identity:</strong> By taking $\\pi$ swapping $1$ and $i$, $\\mathbb{P}(X_1 \\le x) = \\mathbb{P}(X_i \\le x)$ for all $i$. All variables have identical mean $\\mu$ and variance $\\sigma^2$.",
        "<strong>Pairwise Equi-Correlation:</strong> By swapping pairs $(1, 2) \\leftrightarrow (i, j)$, $\\operatorname{Cov}(X_i, X_j) = \\operatorname{Cov}(X_1, X_2) \\triangleq c$ for all $i \\ne j$.",
        "<strong>Compound Symmetry Matrix:</strong> The covariance matrix is $\\Sigma = \\sigma^2 [(1 - \\rho) I_n + \\rho \\mathbf{1}\\mathbf{1}^\\top]$, completely parameterized by just two numbers: $\\sigma^2$ and $\\rho$."
    ],
    r"$$\operatorname{Var}(X_i) = \sigma^2, \quad \operatorname{Cov}(X_i, X_j) = \rho\sigma^2 \quad \forall i \ne j \implies \Sigma = \sigma^2 \left[(1-\rho)I + \rho \mathbf{1}\mathbf{1}^\top\right]$$",
    "A round discussion table of identical twins: each has the exact same baseline reaction and shares the exact same mutual affinity with every other sibling.",
    "Assuming pairwise covariances can vary across indices. In an exchangeable sequence, Cov(X₁, X₂) MUST equal Cov(X₇, X₉)—any discrepancy disproves exchangeability."
))

# Card 31003: Finite Exchangeability Correlation Bound: ρ ≥ -1/(n - 1)
svg_31003 = [
    AX(24, 115, 220, 20),
    # Region for rho from -1/(n-1) to 1
    L(60, 65, 200, 65, 2.5),
    C(60, 65, 4, fill="#000000"), N(60, 50, "-1/(n - 1)", 8.5, w="bold"),
    C(200, 65, 4, fill="#000000"), N(200, 50, "+1", 8.5, w="bold"),
    L(130, 60, 130, 70, 1.2), N(130, 80, "0 (i.i.d.)", 8),
    # Derivation note
    box(24, 18, 192, 22, "Var(∑ Xᵢ) = n σ² [1 + (n - 1) ρ] ≥ 0 ⇒ ρ ≥ -1 / (n - 1)", "#ffffff", 8),
    N(120, 138, "Finite exchangeable variables can be negatively correlated down to -1/(n - 1)", 8.5)
]
CARDS.append(make_stoma_card(
    10, 3, "FINITE CORRELATION",
    "Finite Exchangeability Correlation Bound: ρ ≥ -1/(n - 1)",
    svg_31003,
    "Variance non-negativity of the sum bounds negative correlation: ρ ≥ -1/(n - 1)",
    [
        "<strong>Sum Variance Expansion:</strong> For sum $S_n = \\sum_{i=1}^n X_i$, $\\operatorname{Var}(S_n) = \\sum \\operatorname{Var}(X_i) + \\sum_{i \\ne j} \\operatorname{Cov}(X_i, X_j) = n\\sigma^2 + n(n-1)\\rho\\sigma^2$.",
        "<strong>Positivity Constraint:</strong> Since $\\operatorname{Var}(S_n) \\ge 0$, we have $n\\sigma^2 [1 + (n-1)\\rho] \\ge 0 \\implies \\rho \\ge -\\frac{1}{n-1}$.",
        "<strong>Extreme Negative Attainment:</strong> Equality $\\rho = -\\frac{1}{n-1}$ is achieved when the sum is deterministic: $\\sum_{i=1}^n X_i = c$ almost surely."
    ],
    r"$$\operatorname{Var}\left(\sum_{i=1}^n X_i\right) \ge 0 \implies 1 + (n-1)\rho \ge 0 \implies \rho \ge -\frac{1}{n-1}$$",
    "Cutting a fixed birthday cake among n guests: if guest 1 gets a larger slice, the other slices must collectively shrink, producing mutual negative correlation -1/(n-1).",
    "Believing correlation can never be negative in exchangeable systems. For finite n, negative correlation is completely valid down to the barrier -1/(n-1)."
))

# Card 31004: Infinite Exchangeability & Non-Negative Correlation
svg_31004 = [
    # Limit n -> infinity
    box(20, 20, 200, 42, "Finite sequence: ρ ≥ -1 / (n - 1)\nTake n → ∞ (infinite sequence):\nρ ≥ lim_{n → ∞} [-1 / (n - 1)] = 0", "#f8fafc", 8.5),
    # Number line showing [0, 1]
    L(30, 85, 210, 85, 1.4),
    L(100, 85, 200, 85, 2.5),
    C(100, 85, 4, fill="#000000"), N(100, 100, "0", 9, w="bold"),
    C(200, 85, 4, fill="#000000"), N(200, 100, "1", 9, w="bold"),
    N(150, 72, "Valid range for infinite exchangeability: ρ ∈ [0, 1]", 8, w="bold"),
    N(120, 138, "An infinitely extendable exchangeable sequence CANNOT be negatively correlated!", 8.5)
]
CARDS.append(make_stoma_card(
    10, 4, "INFINITE EXCHANGEABILITY",
    "Infinite Exchangeability & Non-Negative Correlation",
    svg_31004,
    "If an exchangeable sequence is infinitely extendable, its pairwise correlation must be non-negative: ρ ≥ 0",
    [
        "<strong>Infinite Extension:</strong> Sequence $(X_1, X_2, \\dots)$ is infinitely exchangeable if every finite subvector $(X_1, \\dots, X_n)$ is exchangeable for all $n \\ge 2$.",
        "<strong>Vanishing Lower Bound:</strong> The bound $\\rho \\ge -\\frac{1}{n-1}$ must hold for arbitrarily large $n$. Taking $n \\to \\infty$ yields $\\rho \\ge 0$.",
        "<strong>Impossibility of Negative Correlation:</strong> You cannot have an infinite family of variables that are all mutually negatively correlated! Mutual conflict cannot scale to infinity."
    ],
    r"$$\rho \ge -\frac{1}{n-1} \quad \forall n \ge 2 \implies \rho \ge \lim_{n \to \infty} \left(-\frac{1}{n-1}\right) = 0 \implies \rho \ge 0$$",
    "Musical harmony: you can tune 2 or 3 instruments to clash out of phase with each other, but you cannot have an infinite orchestra where every pair clashes negatively.",
    "Applying De Finetti or claiming ρ ≥ 0 for a finite sequence! Sampling without replacement from an urn of N balls stops at N; its correlation -1/(N-1) CANNOT be extended to infinity."
))

# Card 31005: De Finetti’s Representation Theorem
svg_31005 = [
    # Latent parameter Theta
    box(80, 18, 80, 28, "Latent Prior: Θ ~ F(θ)", "#d9dee7", 8.5),
    V(120, 46, 120, 70, 1.4),
    N(155, 58, "Condition on Θ", 7.5),
    # Conditionally i.i.d. draws
    box(24, 70, 192, 34, "Given Θ = θ:  X₁, X₂, ... are i.i.d. Bernoulli(θ)\nP(X₁=x₁, ..., X_n=x_n) = ∫₀¹ θ^k (1-θ)^{n-k} dF(θ)", "#ffffff", 7.5),
    N(120, 138, "De Finetti: Every infinite exchangeable binary sequence is a mixture of i.i.d. Bernoulli trials", 8)
]
CARDS.append(make_stoma_card(
    10, 5, "DE FINETTI THEOREM",
    "De Finetti’s Representation Theorem: Conditionally i.i.d. Mixtures",
    svg_31005,
    "Infinite exchangeability is mathematically equivalent to conditional independence given a latent random parameter",
    [
        "<strong>Representation Statement:</strong> Let $(X_1, X_2, \\dots)$ be an infinite exchangeable sequence of binary variables $X_i \\in \\{0, 1\\}$. Then there exists a unique distribution function $F_\\Theta$ on $[0, 1]$ such that given $\\Theta = \\theta$, $X_i$ are i.i.d. $\\text{Bernoulli}(\\theta)$.",
        "<strong>Integral Mixture:</strong> $\\mathbb{P}(X_1 = x_1, \\dots, X_n = x_n) = \\int_0^1 \\theta^{\\sum x_i} (1 - \\theta)^{n - \\sum x_i} dF_\\Theta(\\theta)$.",
        "<strong>Bayesian Foundation:</strong> Justifies Bayesian probability: the 'unknown parameter' $\\Theta$ is mathematically proven to exist as the almost sure limiting frequency $\\Theta = \\lim_{n \\to \\infty} \\frac{1}{n}\\sum_{i=1}^n X_i$."
    ],
    r"$$\mathbb{P}(X_1=x_1, \dots, X_n=x_n) = \int_0^1 \theta^{\sum x_i} (1-\theta)^{n - \sum x_i}\,dF_\Theta(\theta), \quad \Theta = \lim_{n \to \infty} \frac{1}{n}\sum_{i=1}^n X_i$$",
    "A factory coin: the coin's bias θ is chosen once at manufacturing time from prior F_Θ, after which all tosses with that coin are independent given θ.",
    "Applying De Finetti to finite sequences! De Finetti FAILS for finite exchangeable collections; the infinite horizon is strictly necessary for the representation integral to hold."
))

# Card 31006: Worked Benchmark: Pólya’s Urn Scheme
svg_31006 = [
    # Urn graphic
    R(24, 25, 60, 55, fill="#f8fafc", sw=1.4),
    N(54, 45, "w white", 8, w="bold"),
    N(54, 62, "b black", 8, w="bold"),
    V(84, 52, 120, 52, 1.4),
    N(102, 42, "Draw color", 7),
    # Add c matching balls
    box(120, 35, 96, 36, "Return ball PLUS\nc balls of same color\n(Reinforcement)", "#ffffff", 7.5),
    # Equal probability result
    box(24, 90, 192, 28, "Any sequence of k white and (n-k) black balls has IDENTICAL probability!", "#e2e8f0", 7.5),
    N(120, 138, "Pólya's Urn generates an infinite exchangeable sequence; limiting fraction Θ ~ Beta(w/c, b/c)", 8)
]
CARDS.append(make_stoma_card(
    10, 6, "WORKED BENCHMARK",
    "Worked Benchmark: Pólya’s Urn Scheme & Exchangeability",
    svg_31006,
    "Reinforced urn sampling creates an exchangeable process where color count matters, but sequence order is irrelevant",
    [
        "<strong>Urn Dynamics:</strong> Start with $w$ white and $b$ black balls. Draw a ball, note its color, and replace it along with $c$ additional balls of the SAME color.",
        "<strong>Exchangeable Proof:</strong> The probability of any specific sequence with $k$ white and $(n - k)$ black balls is identical regardless of order: $\\frac{w(w+c)\\cdots(w+(k-1)c) \\cdot b(b+c)\\cdots(b+(n-k-1)c)}{(w+b)(w+b+c)\\cdots(w+b+(n-1)c)}$.",
        "<strong>Limiting Law:</strong> As $n \\to \\infty$, the proportion of white balls converges almost surely to random variable $\\Theta \\sim \\text{Beta}\\left(\\frac{w}{c}, \\frac{b}{c}\\right)$. For $w=1, b=1, c=1$, $\\Theta \\sim \\text{Uniform}(0, 1)$."
    ],
    r"$$\mathbb{P}(X_1=x_1, \dots, X_n=x_n) = \frac{\prod_{j=0}^{k-1}(w + jc) \prod_{j=0}^{n-k-1}(b + jc)}{\prod_{j=0}^{n-1}(w + b + jc)}, \quad \Theta \sim \text{Beta}\left(\tfrac{w}{c}, \tfrac{b}{c}\right)$$",
    "Social media virality: a post with initial upvotes attracts further upvotes proportionally, stabilizing to an exchangeable popularity distribution.",
    "Assuming Pólya's urn trials are independent. The draws are heavily dependent (positive feedback reinforcement), yet perfectly exchangeable!"
))

# ==============================================================================
# TOPIC 11: COVARIANCE & LINEAR LEAST SQUARES (LLSE) (31101 - 31106)
# ==============================================================================

# Card 31101: Covariance Matrix Properties & PSD Invariance
svg_31101 = [
    box(24, 18, 192, 34, "Σ_X = E[(X - μ_X)(X - μ_X)ᵀ] = E[X Xᵀ] - μ_X μ_Xᵀ\nSymmetric Positive Semidefinite: Σ_X ⪰ 0", "#ffffff", 8.5),
    # Quadratic form v^T Sigma v
    box(24, 60, 192, 30, "∀ v ∈ ℝⁿ:   vᵀ Σ_X v = Var(vᵀ X) ≥ 0   (Eigenvalues λᵢ ≥ 0)", "#f8fafc", 8.5),
    # Affine transform
    box(24, 96, 192, 26, "Affine transform: Y = A X + b  ⇒  Σ_Y = A Σ_X Aᵀ", "#f1f5f9", 8.5),
    N(120, 138, "Covariance matrices are symmetric positive semidefinite; quadratic forms equal variance", 8.5)
]
CARDS.append(make_stoma_card(
    11, 1, "COVARIANCE MATRICES",
    "Covariance Matrix Properties & Positive Semidefiniteness",
    svg_31101,
    "The covariance matrix is always symmetric positive semidefinite; its quadratic form measures directional variance",
    [
        "<strong>Definition:</strong> For random vector $X \\in \\mathbb{R}^n$, $\\Sigma_X \\triangleq \\mathbb{E}[(X - \\mu_X)(X - \\mu_X)^\\top] = \\mathbb{E}[XX^\\top] - \\mu_X\\mu_X^\\top$.",
        "<strong>Positive Semidefiniteness ($\\Sigma_X \\succeq 0$):</strong> For any deterministic vector $v \\in \\mathbb{R}^n$, $v^\\top \\Sigma_X v = \\operatorname{Var}(v^\\top X) \\ge 0$. All eigenvalues are real and non-negative ($\\lambda_i \\ge 0$).",
        "<strong>Affine Transformation Law:</strong> If $Y = A X + b$, then $\\mu_Y = A\\mu_X + b$ and $\\Sigma_Y = A \\Sigma_X A^\\top$."
    ],
    r"$$\Sigma_X = \mathbb{E}[(X - \mu)(X - \mu)^\top] \succeq 0, \qquad \Sigma_{AX + b} = A \Sigma_X A^\top, \qquad v^\top \Sigma_X v = \operatorname{Var}(v^\top X) \ge 0$$",
    "Ellipsoid of inertia: the eigenvalues of Σ dictate the lengths of the principal dispersion axes of a multidimensional data cloud.",
    "Writing Σ_{AX} = Aᵀ Σ_X A instead of A Σ_X Aᵀ! If A is m × n, A Σ_X Aᵀ produces the correct m × m covariance matrix."
))

# Card 31102: The Orthogonality Principle of LLSE
svg_31102 = [
    # Orthogonal projection in Hilbert space
    L(30, 110, 210, 110, 1.4), N(200, 122, "Affine subspace of X", 7.5),
    V(60, 110, 140, 35, 2.0), N(145, 30, "Target Y", 9, w="bold"),
    V(60, 110, 140, 110, 2.0), N(140, 124, "LLSE: Ŷ", 9, w="bold"),
    # Error vector e
    L(140, 110, 140, 35, 1.8, d="3 3"),
    N(165, 72, "Error: e = Y - Ŷ", 8, w="bold"),
    # Right angle symbol
    PG("140,100 130,100 130,110", fill="none", w=1.2),
    N(120, 138, "Orthogonality: E[(Y - Ŷ) Xᵀ] = 0 and E[Y - Ŷ] = 0 (Error is orthogonal to data)", 8)
]
CARDS.append(make_stoma_card(
    11, 2, "ORTHOGONALITY PRINCIPLE",
    "The Orthogonality Principle: Hilbert Space Geometry of Estimation",
    svg_31102,
    "The optimal linear estimator projects Y onto the linear subspace of X; error e = Y - Ŷ is orthogonal to X",
    [
        "<strong>Geometric Formulation:</strong> Random variables form an inner product space under $\\langle U, V \\rangle = \\mathbb{E}[UV]$. Distance is root-mean-square error $\\|Y - \\hat{Y}\\|_{L^2} = \\sqrt{\\mathbb{E}[|Y - \\hat{Y}|^2]}$.",
        "<strong>Orthogonality Condition:</strong> $\\hat{Y} = AX + b$ minimizes MSE if and only if estimation error $e = Y - \\hat{Y}$ is orthogonal to all observations and affine constants: $\\mathbb{E}[e X^\\top] = 0$ and $\\mathbb{E}[e] = 0$.",
        "<strong>Zero Residual Information:</strong> The error $e$ has zero correlation with $X$, meaning no further linear predictive power remains in the observation."
    ],
    r"$$\mathbb{E}[Y - \hat{Y}] = 0, \qquad \mathbb{E}\left[(Y - \hat{Y}) X^\top\right] = 0 \iff \hat{Y} \text{ minimizes } \mathbb{E}\left[\|Y - \hat{Y}\|^2\right]$$",
    "Dropping a perpendicular shadow: the shortest path from a point in the air to a tabletop is the perpendicular drop; any oblique shadow is strictly longer.",
    "Assuming error is independent of X. Orthogonality guarantees ZERO CORRELATION (Cov(e, X) = 0), not independence! Independence holds only under joint Gaussianity."
))

# Card 31103: The Multivariate LLSE Formula
svg_31103 = [
    # Full LLSE formula box
    box(20, 20, 200, 44, "Multivariate LLSE:\nŶ(X) = μ_Y + Σ_{YX} Σ_X⁻¹ (X - μ_X)\n(Best linear approximation of Y given X)", "#f8fafc", 9),
    # Gain matrix box
    box(20, 72, 200, 36, "Optimal Gain Matrix: K = Σ_{YX} Σ_X⁻¹\nError Covariance: Σ_e = Σ_Y - Σ_{YX} Σ_X⁻¹ Σ_{XY}", "#ffffff", 8.5),
    N(120, 138, "Requires ONLY first and second moments (means and covariances); no full densities needed", 8)
]
CARDS.append(make_stoma_card(
    11, 3, "LLSE FORMULA",
    "The Multivariate Linear Least Squares Estimator (LLSE)",
    svg_31103,
    "The closed-form LLSE requires only first and second moments, adjusting prior mean by optimal gain matrix",
    [
        "<strong>Closed-Form Estimator:</strong> $\\hat{Y}_{\\text{LLSE}}(X) = \\mu_Y + \\Sigma_{YX} \\Sigma_X^{-1} (X - \\mu_X)$, where $\\Sigma_{YX} = \\mathbb{E}[(Y - \\mu_Y)(X - \\mu_X)^\\top]$.",
        "<strong>Optimal Kalman Gain:</strong> The matrix $K \\triangleq \\Sigma_{YX} \\Sigma_X^{-1}$ is the optimal linear regression weight matrix.",
        "<strong>Data Parsimony:</strong> LLSE requires ONLY means $\\mu_X, \\mu_Y$ and covariances $\\Sigma_X, \\Sigma_{YX}$. It computes without knowing the underlying probability density functions."
    ],
    r"$$\hat{Y}_{\text{LLSE}}(X) = \mu_Y + \Sigma_{YX}\Sigma_X^{-1}(X - \mu_X), \qquad K = \Sigma_{YX}\Sigma_X^{-1}$$",
    "GPS position filtering: starting at baseline belief μ_Y and correcting position by multiplying sensor error (X - μ_X) by Kalman gain matrix K.",
    "Assuming LLSE is the optimal overall estimator. LLSE is optimal ONLY among affine estimators (cᵀX + d). The unconditional MMSE estimator is conditional expectation E[Y|X], which may be highly non-linear."
))

# Card 31104: Error Covariance Matrix & Schur Complement
svg_31104 = [
    box(24, 20, 192, 42, "Error Covariance Matrix Σ_e:\nΣ_e = E[(Y - Ŷ)(Y - Ŷ)ᵀ]\n= Σ_Y - Σ_{YX} Σ_X⁻¹ Σ_{XY}", "#ffffff", 8.5),
    # Schur complement box
    box(24, 70, 192, 40, "Schur Complement of Joint Covariance:\n[ Σ_X    Σ_{XY} ]\n[ Σ_{YX} Σ_Y    ]   ⇒  Σ_e = Σ_Y - Σ_{YX} Σ_X⁻¹ Σ_{XY} ⪰ 0", "#f8fafc", 8),
    N(120, 138, "Information reduction: Observation X always reduces (or preserves) error covariance: Σ_e ⪯ Σ_Y", 8)
]
CARDS.append(make_stoma_card(
    11, 4, "ERROR COVARIANCE",
    "Error Covariance Matrix & Schur Complement Geometry",
    svg_31104,
    "The estimation error covariance is the Schur complement of the joint covariance matrix: Σ_e = Σ_Y - Σ_{YX} Σ_X⁻¹ Σ_{XY}",
    [
        "<strong>Matrix Formula:</strong> $\\Sigma_e \\triangleq \\operatorname{Cov}(Y - \\hat{Y}) = \\Sigma_Y - \\Sigma_{YX} \\Sigma_X^{-1} \\Sigma_{XY}$.",
        "<strong>Monotonic Variance Reduction:</strong> Since $\\Sigma_{YX} \\Sigma_X^{-1} \\Sigma_{XY} \\succeq 0$, the error covariance satisfies $\\Sigma_e \\preceq \\Sigma_Y$ (in the Loewner positive semidefinite order). Observation $X$ can only decrease uncertainty.",
        "<strong>Schur Complement Identity:</strong> $\\Sigma_e$ is precisely the Schur complement of block $\\Sigma_X$ in the joint covariance matrix $\\begin{bmatrix} \\Sigma_X & \\Sigma_{XY} \\\\ \\Sigma_{YX} & \\Sigma_Y \\end{bmatrix}$."
    ],
    r"$$\Sigma_e = \operatorname{Cov}(Y - \hat{Y}) = \Sigma_Y - \Sigma_{YX}\Sigma_X^{-1}\Sigma_{XY} \preceq \Sigma_Y$$",
    "Measuring an object through fog: taking a photo never increases your uncertainty about its shape; error variance drops by the amount captured in Σ_{YX} Σ_X⁻¹ Σ_{XY}.",
    "Singular Σ_X: If Σ_X is not invertible (observations are linearly redundant), replace Σ_X⁻¹ with the Moore-Penrose pseudoinverse Σ_X⁺."
))

# Card 31105: Scalar LLSE & The Pearson Correlation Coefficient
svg_31105 = [
    # Scatter plot with regression line
    AX(24, 115, 220, 20),
    L(40, 95, 200, 35, 1.8),
    N(180, 28, "Slope = ρ (σ_Y / σ_X)", 8, w="bold"),
    C(120, 65, 3.5, fill="#000000"), N(120, 52, "(μ_X, μ_Y)", 8),
    # Scalar formulas
    box(24, 20, 100, 34, "Ŷ = μ_Y + ρ (σ_Y/σ_X)(X - μ_X)\nSlope = Cov(X,Y)/Var(X)", "#ffffff", 7.5),
    box(130, 20, 86, 34, "MSE = σ_Y² (1 - ρ²)\nR² = ρ²", "#ffffff", 8),
    N(120, 138, "Scalar LLSE is the classic linear regression line; MSE drops by factor (1 - ρ²)", 8.5)
]
CARDS.append(make_stoma_card(
    11, 5, "SCALAR LLSE",
    "Scalar LLSE & The Pearson Correlation Coefficient",
    svg_31105,
    "In 1D, the LLSE is the standard regression line whose residual variance equals σ_Y² (1 - ρ²)",
    [
        "<strong>Scalar Formula:</strong> $\\hat{Y} = \\mu_Y + \\rho \\frac{\\sigma_Y}{\\sigma_X} (X - \\mu_X)$, where Pearson correlation $\\rho = \\frac{\\operatorname{Cov}(X, Y)}{\\sigma_X \\sigma_Y} \\in [-1, 1]$.",
        "<strong>Slope & Anchor:</strong> The line passes through the bivariate centroid $(\\mu_X, \\mu_Y)$ with regression slope $\\beta = \\frac{\\operatorname{Cov}(X, Y)}{\\operatorname{Var}(X)} = \\rho \\frac{\\sigma_Y}{\\sigma_X}$.",
        "<strong>Residual MSE:</strong> $\\mathbb{E}[(Y - \\hat{Y})^2] = \\sigma_Y^2 (1 - \\rho^2)$. When $|\\rho| = 1$, MSE is 0 (exact prediction); when $\\rho = 0$, $\\hat{Y} = \\mu_Y$ and MSE is $\\sigma_Y^2$."
    ],
    r"$$\hat{Y} = \mu_Y + \rho \frac{\sigma_Y}{\sigma_X}(X - \mu_X), \qquad \operatorname{MSE} = \sigma_Y^2(1 - \rho^2)$$",
    "Regression to the mean (Galton): children of exceptionally tall parents (X) are predicted to be above average (Y), but shrunk toward the population mean by factor ρ.",
    "Swapping X and Y in the regression slope: the slope for predicting Y from X is ρ(σ_Y/σ_X), while the slope for predicting X from Y is ρ(σ_X/σ_Y) (which is NOT 1/slope!)."
))

# Card 31106: Worked Benchmark: Estimating a Signal in Additive White Noise
svg_31106 = [
    # Signal + Noise block diagram
    box(16, 20, 60, 28, "Signal X\n(Var = σ_X²)", "#ffffff", 8),
    V(76, 34, 106, 34, 1.4),
    C(114, 34, 8, fill="#ffffff", w=1.3),
    N(114, 37, "+", 10, w="bold"),
    V(114, 10, 114, 26, 1.2),
    N(114, 6, "Noise W ~ (0, σ_W²)", 7),
    V(122, 34, 150, 34, 1.4),
    box(150, 20, 66, 28, "Observe Y\nY = X + W", "#e2e8f0", 8),
    # Wiener filter shrinkage result
    box(16, 68, 208, 44, "Optimal Filter: X̂(Y) = [ σ_X² / (σ_X² + σ_W²) ] · Y  (Wiener gain)\nMSE = [ σ_X² σ_W² ] / (σ_X² + σ_W²) = σ_X² · (1 - SNR / (1 + SNR))", "#f8fafc", 7.5),
    N(120, 138, "Signal shrinkage: High SNR (σ_X² >> σ_W²) yields X̂ ≈ Y; Low SNR shrinks X̂ → 0", 8)
]
CARDS.append(make_stoma_card(
    11, 6, "WORKED BENCHMARK",
    "Worked Benchmark: Signal Estimation in Additive Noise (Wiener Filter)",
    svg_31106,
    "Estimating zero-mean signal X from noisy observation Y = X + W shrinks Y by signal-to-noise ratio fraction",
    [
        "<strong>Problem Setup:</strong> Signal $X$ has mean $0$ and variance $\\sigma_X^2$. Observation is $Y = X + W$, where noise $W$ has mean $0$, variance $\\sigma_W^2$, and $X \\perp W$.",
        "<strong>Covariance Derivation:</strong> $\\operatorname{Var}(Y) = \\sigma_X^2 + \\sigma_W^2$. Cross-covariance is $\\operatorname{Cov}(X, Y) = \\mathbb{E}[X(X + W)] = \\mathbb{E}[X^2] = \\sigma_X^2$.",
        "<strong>Wiener Shrinkage Estimator:</strong> $\\hat{X}(Y) = \\frac{\\sigma_X^2}{\\sigma_X^2 + \\sigma_W^2} Y = \\frac{\\text{SNR}}{1 + \\text{SNR}} Y$. Minimum MSE is $\\frac{\\sigma_X^2 \\sigma_W^2}{\\sigma_X^2 + \\sigma_W^2}$."
    ],
    r"$$\hat{X}(Y) = \frac{\sigma_X^2}{\sigma_X^2 + \sigma_W^2} Y, \qquad \operatorname{MSE} = \frac{\sigma_X^2 \sigma_W^2}{\sigma_X^2 + \sigma_W^2} = \sigma_X^2 \left(1 - \frac{\text{SNR}}{1 + \text{SNR}}\right)$$",
    "Noise-cancelling audio headphones: when music is loud and static is faint (high SNR), pass the audio directly; when music is faint and static dominates, heavily suppress the signal toward zero.",
    "Using raw observation Y as the estimator without shrinkage! Y is unbiased, but has MSE equal to σ_W², which is strictly WORSE than the Wiener estimate's MSE."
))

# Save cards to cards_stoma.js
save_stoma_cards(CARDS)
print(f"Successfully generated {len(CARDS)} cards for StoMA Topics 10 & 11!")
