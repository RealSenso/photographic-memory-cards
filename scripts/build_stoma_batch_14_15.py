"""Build StoMA Topics 14 & 15 (Cards 31401 to 31506).
Dual-coding photographic plates with pure black-and-white vector diagrams.
"""
import sys, os
sys.path.append(os.path.dirname(__file__))
from stoma_lib import (
    T, N, L, V, P, C, R, E, PG, AX, box, svg, make_stoma_card, save_stoma_cards
)

CARDS = []

# ==============================================================================
# TOPIC 14: RANDOM SUMS & WALD'S EQUATION (31401 - 31406)
# ==============================================================================

# Card 31401: Random Sums S_N = ∑_{i=1}^N X_i & Stopping Times
svg_31401 = [
    # Timeline with N terms
    L(20, 72, 220, 72, 1.8),
    C(35, 72, 3.5, fill="#000000"), N(35, 58, "X₁", 8.5),
    C(70, 72, 3.5, fill="#000000"), N(70, 58, "X₂", 8.5),
    C(105, 72, 3.5, fill="#000000"), N(105, 58, "X₃", 8.5),
    C(140, 72, 3.5, fill="#000000"), N(140, 58, "...", 8.5),
    C(175, 72, 4, fill="#000000"), N(175, 58, "X_N", 9, w="bold"),
    # Stopping gate
    L(175, 35, 175, 105, 1.8, d="3 3"),
    N(175, 26, "Stop N", 8, w="bold"),
    box(24, 90, 192, 32, "S_N = ∑_{i=1}^∞ Xᵢ · 1_{N ≥ i}\nEvent {N ≥ i} = {N ≤ i-1}ᶜ is independent of Xᵢ!", "#ffffff", 7.5),
    N(120, 138, "Stopping time N depends only on past history X₁, ..., X_{i-1}; no future peering", 8)
]
CARDS.append(make_stoma_card(
    14, 1, "RANDOM SUMS",
    "Random Sums S_N = ∑_{i=1}^N X_i & Stopping Times",
    svg_31401,
    "Random sums add a stochastic number of terms N; stopping times decide to halt without peering into the future",
    [
        "<strong>Random Sum Formulation:</strong> For i.i.d. $X_i$ with mean $\\mu$ and variance $\\sigma^2$, $S_N = \\sum_{i=1}^N X_i$ sums a random integer number of terms $N \\in \\mathbb{N}_0$.",
        "<strong>Stopping Time Condition:</strong> $N$ is a stopping time with respect to filtration $\\mathcal{F}_n = \\sigma(X_1, \\dots, X_n)$ if $\\{N = n\\} \\in \\mathcal{F}_n$ for all $n$ (halting rule does NOT depend on future outcomes).",
        "<strong>Indicator Independence:</strong> $S_N = \\sum_{i=1}^\\infty X_i \\mathbf{1}_{\\{N \\ge i\\}}$. Crucially, event $\\{N \\ge i\\} = \\{N \\le i-1\\}^c$ depends only on $X_1, \\dots, X_{i-1}$, and is therefore independent of $X_i$."
    ],
    r"$$S_N = \sum_{i=1}^N X_i = \sum_{i=1}^\infty X_i\,\mathbf{1}_{\{N \ge i\}}, \qquad \{N \ge i\} \in \sigma(X_1, \dots, X_{i-1}) \implies \mathbf{1}_{\{N \ge i\}} \perp X_i$$",
    "Blackjack card strategy: deciding whether to draw another card based on your current hand is a stopping time; stopping when the next card would bust you is clairvoyant and impossible.",
    "Applying Wald's identities when N looks into the future! For example, N = argmax_{1 ≤ i ≤ 5} X_i depends on future terms; Wald's equation fails completely for anticipatory stopping rules."
))

# Card 31402: Wald’s First Identity: E[S_N] = E[N] E[X]
svg_31402 = [
    # Grid of terms
    box(24, 20, 192, 44, "Wald's First Identity (Wald's Equation):\nE[ S_N ] = E[N] · E[X]\n(Valid for any stopping time with E[N] < ∞, E[|X|] < ∞)", "#f8fafc", 8.5),
    # Proof sketch box
    box(24, 72, 192, 42, "Indicator Proof:\nE[S_N] = ∑ E[Xᵢ 1_{N ≥ i}] = ∑ E[Xᵢ] P(N ≥ i)\n= E[X] ∑ P(N ≥ i) = E[X] E[N]  (via tail sum!)", "#ffffff", 7.5),
    N(120, 138, "Expected total payout equals expected count E[N] times expected cost per event E[X]", 8.5)
]
CARDS.append(make_stoma_card(
    14, 2, "WALD IDENTITIES",
    "Wald’s First Identity: E[S_N] = E[N] · E[X]",
    svg_31402,
    "The expected value of a random sum equals the expected number of terms times the expected individual value",
    [
        "<strong>Theorem Statement:</strong> If $X_i$ are i.i.d. with $\\mathbb{E}[|X|] < \\infty$ and $N$ is a stopping time with $\\mathbb{E}[N] < \\infty$, then $\\mathbb{E}[S_N] = \\mathbb{E}[N]\\,\\mathbb{E}[X]$.",
        "<strong>Indicator Proof:</strong> $\\mathbb{E}[S_N] = \\mathbb{E}[\\sum_{i=1}^\\infty X_i \\mathbf{1}_{\\{N \\ge i\\}}] = \\sum_{i=1}^\\infty \\mathbb{E}[X_i] \\mathbb{P}(N \\ge i) = \\mathbb{E}[X] \\sum_{i=1}^\\infty \\mathbb{P}(N \\ge i) = \\mathbb{E}[X]\\mathbb{E}[N]$.",
        "<strong>Tower Proof (if $N \\perp X$):</strong> By the law of total expectation, $\\mathbb{E}[S_N] = \\mathbb{E}[\\mathbb{E}[S_N \\mid N]] = \\mathbb{E}[N \\mathbb{E}[X]] = \\mathbb{E}[N]\\,\\mathbb{E}[X]$."
    ],
    r"$$\mathbb{E}\left[\sum_{i=1}^N X_i\right] = \mathbb{E}[N]\,\mathbb{E}[X], \quad \text{provided } \mathbb{E}[N] < \infty, \; \mathbb{E}[|X|] < \infty$$",
    "Hospital emergency room: an average of E[N] = 40 patients arrive per day, each incurring an average treatment cost of E[X] = $1,500; total expected daily expenditure is $60,000.",
    "Ignoring integrability conditions: if E[N] = ∞ or E[|X|] = ∞, Wald's equation breaks down and can yield undefined ∞ × 0 forms."
))

# Card 31403: Wald’s Second Identity: Two-Source Variance Decomposition
svg_31403 = [
    box(20, 20, 200, 36, "Wald's Second Identity:\nVar(S_N) = E[N] Var(X) + (E[X])² Var(N)", "#ffffff", 8.5),
    # Eve's law decomposition
    box(20, 62, 96, 46, "E[ Var(S_N | N) ]\n= E[N σ²]\n= E[N] Var(X)\n(Claim variability)", "#f8fafc", 7.5),
    box(124, 62, 96, 46, "Var( E[S_N | N] )\n= Var(N μ)\n= μ² Var(N)\n(Count variability)", "#f8fafc", 7.5),
    N(120, 138, "Two variance sources: randomness in each step PLUS randomness in the total number of steps", 8)
]
CARDS.append(make_stoma_card(
    14, 3, "WALD IDENTITIES",
    "Wald’s Second Identity: Two-Source Variance Decomposition",
    svg_31403,
    "The variance of a random sum combines individual claim variability with count volatility via Eve’s Law",
    [
        "<strong>Identity Statement:</strong> If $N$ is independent of i.i.d. $X_i$ with finite variances, $\\operatorname{Var}(S_N) = \\mathbb{E}[N]\\operatorname{Var}(X) + (\\mathbb{E}[X])^2 \\operatorname{Var}(N)$.",
        "<strong>Derivation via Total Variance:</strong> $\\operatorname{Var}(S_N) = \\mathbb{E}[\\operatorname{Var}(S_N \\mid N)] + \\operatorname{Var}(\\mathbb{E}[S_N \\mid N]) = \\mathbb{E}[N\\sigma^2] + \\operatorname{Var}(N\\mu) = \\mathbb{E}[N]\\sigma^2 + \\mu^2 \\operatorname{Var}(N)$.",
        "<strong>Zero-Mean Simplification:</strong> If $\\mathbb{E}[X] = 0$, the second term vanishes: $\\operatorname{Var}(S_N) = \\mathbb{E}[N]\\operatorname{Var}(X)$ (holds even when $N$ is a general stopping time)."
    ],
    r"$$\operatorname{Var}\left(\sum_{i=1}^N X_i\right) = \mathbb{E}[N]\operatorname{Var}(X) + \left(\mathbb{E}[X]\right)^2 \operatorname{Var}(N)$$",
    "Retail inventory risk: total weekly revenue variance stems from two distinct drivers: fluctuating customer foot traffic Var(N) and fluctuating basket size Var(X).",
    "Using Var(S_N) = E[N]Var(X)! Omitting the second term μ² Var(N) severely underestimates risk whenever mean E[X] is non-zero."
))

# Card 31404: Compound Distributions: Functional Composition
svg_31404 = [
    # MGF & PGF composition diagram
    box(24, 20, 192, 40, "Compound MGF:  M_{S_N}(t) = G_N( M_X(t) ) = M_N( ln M_X(t) )\n(Outer function is counter N; inner function is term X)", "#ffffff", 8),
    box(24, 68, 192, 40, "Compound PGF:  G_{S_N}(s) = G_N( G_X(s) )   [for Xᵢ ∈ ℕ₀]\n(Functional composition evaluates all higher moments)", "#f8fafc", 8),
    N(120, 138, "Functional composition: nested generating functions mirror the nested nature of random sums", 8.5)
]
CARDS.append(make_stoma_card(
    14, 4, "COMPOUND DISTRIBUTIONS",
    "Compound Distributions: Functional Composition of PGFs & MGFs",
    svg_31404,
    "The generating function of a random sum is the functional composition of the parent and offspring generators",
    [
        "<strong>Compound MGF:</strong> $M_{S_N}(t) \\triangleq \\mathbb{E}[e^{t S_N}] = \\mathbb{E}[\\mathbb{E}[e^{t \\sum X_i} \\mid N]] = \\mathbb{E}[(M_X(t))^N] = G_N(M_X(t))$.",
        "<strong>Compound PGF:</strong> For discrete non-negative integer RVs $X_i \\in \\mathbb{N}_0$, $G_{S_N}(s) \\triangleq \\mathbb{E}[s^{S_N}] = G_N(G_X(s))$ (exact nested functional composition).",
        "<strong>Cumulant Generating Function:</strong> $\\log M_{S_N}(t) = \\log G_N(M_X(t))$. Successive derivatives at $t=0$ generate all higher-order cumulants and skewness."
    ],
    r"$$M_{S_N}(t) = G_N\left(M_X(t)\right), \qquad G_{S_N}(s) = G_N\left(G_X(s)\right) \quad (X_i \in \mathbb{N}_0)$$",
    "Russian nesting dolls (Matryoshka): the offspring generating function G_X(s) is packed inside the population count doll G_N.",
    "Swapping the composition order: writing M_X(G_N(t)) instead of G_N(M_X(t))! The outer function is always the counter N; the inner function is the term X."
))

# Card 31405: Galton-Watson Branching Processes & Extinction
svg_31405 = [
    # Family tree
    C(120, 20, 4, fill="#000000"), N(120, 10, "Z₀ = 1", 7.5),
    L(120, 20, 70, 50, 1.2), L(120, 20, 170, 50, 1.2),
    C(70, 50, 3.5, fill="#000000"), C(170, 50, 3.5, fill="#000000"), N(200, 50, "Z₁ ~ ξ", 7.5),
    L(70, 50, 45, 80, 1.0), L(70, 50, 95, 80, 1.0), L(170, 50, 170, 80, 1.0),
    C(45, 80, 3, fill="#000000"), C(95, 80, 3, fill="#000000"), C(170, 80, 3, fill="#000000"),
    N(200, 80, "Z₂", 7.5),
    box(24, 96, 192, 28, "E[Z_n] = μⁿ (μ = E[ξ]);  Extinction π₀ = min{s ∈ [0, 1] : s = G_ξ(s)}", "#f8fafc", 8),
    N(120, 138, "Branching process: Subcritical μ < 1 ⇒ π₀ = 1; Supercritical μ > 1 ⇒ π₀ < 1", 8.5)
]
CARDS.append(make_stoma_card(
    14, 5, "BRANCHING PROCESSES",
    "Galton-Watson Branching Processes & Extinction Probability",
    svg_31405,
    "Population grows geometrically as E[Z_n] = μⁿ; extinction probability π₀ is the smallest root of s = G_ξ(s)",
    [
        "<strong>Model Formulation:</strong> $Z_0 = 1$. Generation $n+1$ has size $Z_{n+1} = \\sum_{i=1}^{Z_n} \\xi_{n,i}$ where $\\xi_{n,i} \\stackrel{\\text{i.i.d.}}{\\sim} \\xi$. By Wald's equation, $\\mathbb{E}[Z_n] = \\mu^n$ with $\\mu = \\mathbb{E}[\\xi]$.",
        "<strong>Phase Transition:</strong> (1) If $\\mu < 1$ (subcritical) or $\\mu = 1$ (critical, $\\xi \\not\\equiv 1$), extinction is CERTAIN: $\\pi_0 = 1$; (2) If $\\mu > 1$ (supercritical), survival is possible: $\\pi_0 < 1$.",
        "<strong>Fixed-Point Theorem:</strong> The extinction probability $\\pi_0 = \\mathbb{P}(\\lim Z_n = 0)$ is the SMALLEST non-negative root of the fixed-point equation $s = G_\\xi(s)$ in $[0, 1]$."
    ],
    r"$$\mathbb{E}[Z_n] = \mu^n \quad (\mu = \mathbb{E}[\xi]); \qquad \pi_0 = \min \{s \in [0, 1] : s = G_\xi(s)\}$$",
    "Viral chain reaction: if basic reproduction number R₀ = μ is below 1, the epidemic dies out with 100% certainty; if R₀ > 1, the disease has a non-zero probability of permanent endemic survival.",
    "Selecting the trivial root s = 1 when solving s = G(s). The root s = 1 is always a mathematical solution (G(1)=1); the true extinction probability is the SMALLEST root in [0, 1]."
))

# Card 31406: Worked Benchmark: Compound Poisson Claims (Lundberg Model)
svg_31406 = [
    AX(24, 115, 220, 20),
    # Poisson jumps trajectory
    L(24, 110, 65, 110, 1.8),
    L(65, 110, 65, 80, 1.8), C(65, 80, 3, fill="#000000"), N(65, 70, "X₁", 7.5),
    L(65, 80, 120, 80, 1.8),
    L(120, 80, 120, 45, 1.8), C(120, 45, 3, fill="#000000"), N(120, 35, "X₂", 7.5),
    L(120, 45, 185, 45, 1.8),
    box(130, 60, 96, 44, "N ~ Pois(λ), Xᵢ ~ Exp(β)\nE[S_N] = λ / β\nVar(S_N) = 2λ / β² = λ E[X²]", "#ffffff", 7.5),
    N(120, 138, "Compound Poisson variance: Var(S_N) = λ E[X²]; count volatility doubles the total variance", 8)
]
CARDS.append(make_stoma_card(
    14, 6, "WORKED BENCHMARK",
    "Worked Benchmark: Compound Poisson Claims (The Lundberg Model)",
    svg_31406,
    "For compound Poisson processes, total variance equals rate λ times second moment E[X²]: Var(S_N) = λ E[X²]",
    [
        "<strong>Problem Setup:</strong> Claim count $N \\sim \\text{Poisson}(\\lambda)$ (so $\\mathbb{E}[N] = \\lambda, \\operatorname{Var}(N) = \\lambda$). Individual claim amounts $X_i \\stackrel{\\text{i.i.d.}}{\\sim} \\text{Exp}(\\beta)$ with mean $1/\\beta$ and variance $1/\\beta^2$.",
        "<strong>Expected Total Claim:</strong> $\\mathbb{E}[S_N] = \\mathbb{E}[N]\\mathbb{E}[X] = \\lambda \\cdot \\frac{1}{\\beta} = \\frac{\\lambda}{\\beta}$.",
        "<strong>Aggregate Variance:</strong> $\\operatorname{Var}(S_N) = \\lambda(1/\\beta^2) + (1/\\beta)^2 \\lambda = \\frac{2\\lambda}{\\beta^2} = \\lambda \\mathbb{E}[X^2]$. For ANY compound Poisson sum, $\\operatorname{Var}(S_N) = \\lambda \\mathbb{E}[X^2]$!"
    ],
    r"$$N \sim \text{Pois}(\lambda) \implies \mathbb{E}[S_N] = \lambda \mathbb{E}[X], \qquad \operatorname{Var}(S_N) = \lambda \mathbb{E}[X^2] = \frac{2\lambda}{\beta^2}$$",
    "Insurance reserve solvency: premium inflows arrive continuously while claim payouts arrive in sudden random compound Poisson jumps, requiring reserves calibrated to λ E[X²].",
    "Omitting the count variance term: calculating Var(S_N) = λ / β² by treating N as a constant! Because Var(N) = λ, the second term adds another λ/β², exactly doubling the variance."
))

# ==============================================================================
# TOPIC 15: MODES OF CONVERGENCE & RELATIONS (31501 - 31506)
# ==============================================================================

# Card 31501: The Four Modes of Stochastic Convergence
svg_31501 = [
    box(16, 20, 60, 28, "Almost Sure\nX_n →^{a.s.} X", "#ffffff", 8),
    V(76, 34, 100, 34, 1.4),
    box(100, 20, 60, 28, "Probability\nX_n →^{P} X", "#e2e8f0", 8),
    V(160, 34, 184, 34, 1.4),
    box(184, 20, 48, 28, "Dist.\n→^{d}", "#ffffff", 8),
    # L^p vertical arrow down to Probability
    box(100, 72, 60, 28, "L^p Mean\nX_n →^{L^p} X", "#f1f5f9", 8),
    V(130, 72, 130, 48, 1.4),
    N(145, 60, "p ≥ 1", 7),
    N(120, 118, "Hierarchy: a.s. ⇒ P ⇒ d;   L^p ⇒ L^r ⇒ P (p > r ≥ 1)", 8.5, w="bold"),
    N(120, 138, "Four distinct topology strengths: a.s. is pointwise almost everywhere; d only matches CDFs", 8)
]
CARDS.append(make_stoma_card(
    15, 1, "CONVERGENCE MODES",
    "The Four Modes of Stochastic Convergence",
    svg_31501,
    "The fundamental implication hierarchy: Almost Sure implies Probability implies Distribution; L^p implies Probability",
    [
        "<strong>Almost Sure ($X_n \\xrightarrow{a.s.} X$):</strong> $\\mathbb{P}(\\{\\omega : \\lim X_n(\\omega) = X(\\omega)\\}) = 1$ (pointwise path convergence for 100% of outcomes).",
        "<strong>In Probability ($X_n \\xrightarrow{P} X$):</strong> $\\lim_{n \\to \\infty} \\mathbb{P}(|X_n - X| \\ge \\epsilon) = 0$ for all $\\epsilon > 0$ (probability of error vanishes).",
        "<strong>In $L^p$ Mean & Distribution:</strong> In $L^p$: $\\lim \\mathbb{E}[|X_n - X|^p] = 0$. In Distribution ($X_n \\xrightarrow{d} X$): $\\lim F_{X_n}(x) = F_X(x)$ at all continuity points of $F_X$ (weakest mode)."
    ],
    r"$$X_n \xrightarrow{a.s.} X \implies X_n \xrightarrow{P} X \implies X_n \xrightarrow{d} X; \qquad X_n \xrightarrow{L^p} X \implies X_n \xrightarrow{L^r} X \implies X_n \xrightarrow{P} X \quad (p > r)$$",
    "Target archery: almost sure means every arrow lands closer and closer to center; probability allows rare wild shots with vanishing likelihood; distribution means only the spray pattern matches the target.",
    "Assuming convergence in distribution requires a shared sample space! X_n →^d X depends ONLY on CDFs; variables can be defined on completely unrelated probability spaces."
))

# Card 31502: Implication Hierarchy & When Reverses Hold
svg_31502 = [
    # Reverse bridges
    box(20, 20, 200, 32, "Bridge 1: X_n →^{d} c  (Constant limit)  ⇔  X_n →^{P} c", "#ffffff", 8.5),
    box(20, 56, 200, 32, "Bridge 2: X_n →^{P} X  AND  |X_n| ≤ Y with E[Y^p]<∞  ⇒  X_n →^{L^p} X (DCT)", "#f8fafc", 8),
    box(20, 92, 200, 32, "Bridge 3: X_n →^{P} X  ⇒  ∃ Subsequence {n_k} s.t. X_{n_k} →^{a.s.} X", "#f1f5f9", 8),
    N(120, 138, "Reverses fail in general, but hold under constant limits, domination, and subsequences", 8.5)
]
CARDS.append(make_stoma_card(
    15, 2, "CONVERGENCE HIERARCHY",
    "Implication Hierarchy & When the Reverses Hold",
    svg_31502,
    "Reverses fail in general, but hold under constant limits, Dominated Convergence (DCT), and subsequences",
    [
        "<strong>Constant Limit Bridge:</strong> If $X_n \\xrightarrow{d} c$ where $c$ is a deterministic CONSTANT, then $X_n \\xrightarrow{P} c$ (distribution convergence promotes to probability convergence).",
        "<strong>Dominated Convergence Bridge:</strong> If $X_n \\xrightarrow{P} X$ and $|X_n| \\le Y$ with $\\mathbb{E}[Y^p] < \\infty$, then $X_n \\xrightarrow{L^p} X$ (Lebesgue Dominated Convergence Theorem).",
        "<strong>Subsequential Bridge:</strong> If $X_n \\xrightarrow{P} X$, there exists a SUBSEQUENCE $\\{n_k\\}$ such that $X_{n_k} \\xrightarrow{a.s.} X$."
    ],
    r"$$X_n \xrightarrow{d} c \iff X_n \xrightarrow{P} c \quad (c \text{ constant}); \qquad X_n \xrightarrow{P} X \implies \exists \{n_k\} \text{ s.t. } X_{n_k} \xrightarrow{a.s.} X$$",
    "Refining an optical focus: coarse adjustment (d) generally cannot ensure sharp paths (a.s.), but if you restrict to a target landmark (constant), coarse focus coincides with fine focus.",
    "Assuming X_n →^d X implies X_n →^P X for non-constant X! E.g. let X ~ N(0, 1) and X_n = -X. Then X_n has the same normal distribution, but X_n - X = -2X never converges to 0."
))

# Card 31503: The Sliding Typewriter (In Probability !=> Almost Sure)
svg_31503 = [
    # Sliding intervals across [0, 1]
    L(20, 35, 220, 35, 1.4), N(20, 48, "0", 7.5), N(220, 48, "1", 7.5),
    R(20, 26, 100, 18, fill="#d9dee7", sw=1.2), N(70, 37, "I₁ = [0, 1/2]", 7),
    L(20, 70, 220, 70, 1.4),
    R(120, 61, 100, 18, fill="#d9dee7", sw=1.2), N(170, 72, "I₂ = [1/2, 1]", 7),
    L(20, 105, 220, 105, 1.4),
    R(20, 96, 67, 18, fill="#d9dee7", sw=1.2), N(53, 107, "I₃ = [0, 1/3]", 7),
    N(120, 138, "Typewriter sweeps endlessly: P(X_n = 1) = 1/k → 0 (in P), yet limsup X_n(ω) = 1 ∀ω (not a.s.)", 8)
]
CARDS.append(make_stoma_card(
    15, 3, "COUNTEREXAMPLE",
    "The Sliding Typewriter: Convergence in Probability ≠ Almost Sure",
    svg_31503,
    "Indicator intervals of shrinking width sweep endlessly across [0, 1]: converges in probability, but diverges almost surely",
    [
        "<strong>Typewriter Construction:</strong> On $\\Omega = [0, 1]$ with uniform Lebesgue measure. Let $X_n = \\mathbf{1}_{I_n}$ where intervals $I_n$ of width $1/k$ sweep from left to right across $[0, 1]$ repeatedly.",
        "<strong>Convergence in Probability:</strong> $\\mathbb{P}(|X_n| \\ge \\epsilon) = \\text{Length}(I_n) = 1/k \\to 0$, so $X_n \\xrightarrow{P} 0$.",
        "<strong>Almost Sure Divergence:</strong> Because the intervals sweep past every point $\\omega \\in [0, 1]$ infinitely many times, the sequence of values $X_n(\\omega)$ oscillates between $0$ and $1$ forever for EVERY $\\omega$. Thus $\\mathbb{P}(\\lim X_n = 0) = 0$!"
    ],
    r"$$\mathbb{P}(X_n = 1) = \frac{1}{k} \to 0 \implies X_n \xrightarrow{P} 0, \quad \text{yet } \limsup_{n \to \infty} X_n(\omega) = 1 \quad \forall \omega \implies X_n \not\xrightarrow{a.s.} 0$$",
    "A sweeping radar beam: the beam gets thinner and thinner over time (prob → 0), but because it never stops rotating, every target on the radar screen is illuminated periodically forever.",
    "Assuming that P(|X_n| ≥ ε) → 0 guarantees sample paths settle down. Probability measures only instantaneous mass size; almost sure convergence requires mass to stop wandering across points."
))

# Card 31504: The Escaping Spike (Almost Sure !=> L^p)
svg_31504 = [
    AX(24, 115, 220, 20),
    # Spike at n^2 with area 1/n
    L(160, 114, 160, 30, 2.2),
    C(160, 30, 3.5, fill="#000000"),
    N(160, 20, "Height = n²", 8, w="bold"),
    N(160, 126, "n²", 8.5),
    box(24, 20, 110, 48, "P(X_n = n²) = 1/n\nP(X_n = 0) = 1 - 1/n\nX_n(ω) → 0 a.s.\nE[X_n] = n²(1/n) = n → ∞!", "#ffffff", 7.5),
    N(120, 138, "Escaping spike: X_n → 0 a.s., but E[X_n] = n → ∞ diverges completely (fails L¹)", 8.5)
]
CARDS.append(make_stoma_card(
    15, 4, "COUNTEREXAMPLE",
    "The Escaping Spike: Almost Sure Convergence ≠ L^p Convergence",
    svg_31504,
    "A spike of height n² with probability 1/n vanishes almost surely, but its expectation diverges to infinity",
    [
        "<strong>Spike Construction:</strong> Let $\\mathbb{P}(X_n = n^2) = 1/n$ and $\\mathbb{P}(X_n = 0) = 1 - 1/n$.",
        "<strong>Almost Sure Zero:</strong> By Borel-Cantelli (using independent trials with $\\sum 1/n^2 < \\infty$), for almost every $\\omega$, $X_n(\\omega) = 0$ for all sufficiently large $n$, so $X_n \\xrightarrow{a.s.} 0$.",
        "<strong>$L^1$ Mean Explosion:</strong> $\\mathbb{E}[|X_n|] = n^2 \\cdot \\frac{1}{n} = n \\to \\infty$. The expectation explodes to infinity even though the variable is zero almost surely!"
    ],
    r"$$X_n(\omega) \to 0 \text{ a.s.}, \quad \text{yet } \mathbb{E}[|X_n|] = n \to \infty \implies X_n \not\xrightarrow{L^1} 0$$",
    "A runaway lottery jackpot: the probability of winning shrinks toward zero, but the jackpot prize grows so exponentially that the expected ticket payout explodes to infinity.",
    "Assuming almost sure convergence allows exchanging limit and expectation: lim E[X_n] = E[lim X_n] strictly requires Uniform Integrability or a Dominated Bound (DCT)."
))

# Card 31505: Slutsky’s Theorem & Continuous Mapping
svg_31505 = [
    # Slutsky arithmetic boxes
    box(16, 20, 208, 28, "Continuous Mapping (CMT):  X_n → X  ⇒  g(X_n) → g(X)  (for continuous g)", "#ffffff", 8),
    box(16, 54, 208, 30, "Slutsky: X_n →^{d} X   and   Y_n →^{P} c (Constant c)\n(1) X_n + Y_n →^{d} X + c,    (2) X_n · Y_n →^{d} c X", "#f8fafc", 8),
    box(16, 90, 208, 28, "Ratio Law: X_n / Y_n →^{d} X / c   (for constant c ≠ 0)", "#f1f5f9", 8.5),
    N(120, 138, "Slutsky enables asymptotic hypothesis testing: plug in consistent estimators Y_n →^P c", 8.5)
]
CARDS.append(make_stoma_card(
    15, 5, "ASYMPTOTIC ALGEBRA",
    "Slutsky’s Theorem & The Continuous Mapping Theorem",
    svg_31505,
    "Slutsky preserves distribution convergence under algebraic operations when the second variable converges in probability to a constant",
    [
        "<strong>Continuous Mapping Theorem (CMT):</strong> If $X_n \\to X$ in mode (a.s., $P$, or $d$) and $g$ is continuous, then $g(X_n) \\to g(X)$ in the SAME mode.",
        "<strong>Slutsky’s Theorem:</strong> If $X_n \\xrightarrow{d} X$ and $Y_n \\xrightarrow{P} c$ (where $c$ is a deterministic constant): (1) $X_n + Y_n \\xrightarrow{d} X + c$; (2) $X_n Y_n \\xrightarrow{d} c X$; (3) $X_n / Y_n \\xrightarrow{d} X / c$ (if $c \\ne 0$).",
        "<strong>Statistical Powerhouse:</strong> Slutsky allows replacing unknown nuisance parameters (like population variance $\\sigma$) with consistent sample estimates $S_n \\xrightarrow{P} \\sigma$."
    ],
    r"$$X_n \xrightarrow{d} X, \; Y_n \xrightarrow{P} c \implies X_n Y_n \xrightarrow{d} cX, \quad \frac{X_n}{Y_n} \xrightarrow{d} \frac{X}{c} \quad (c \ne 0)$$",
    "Calibrating a precision laboratory balance: if your object weight error is Gaussian (X_n →^d N), and tare calibration offset converges to true constant c (Y_n →^P c), total reading error is N + c.",
    "Applying Slutsky when Y_n →^d Y with non-constant Y! If Y is random, X_n + Y_n does NOT necessarily converge to X + Y because distribution convergence tells you nothing about mutual joint alignment."
))

# Card 31506: Worked Benchmark: Slutsky on Student's t-Statistic
svg_31506 = [
    box(16, 20, 208, 42, "Student's t-Statistic:  T_n = \\frac{\\sqrt{n}(\\bar{X}_n - μ)}{S_n} = \\frac{\\frac{\\sqrt{n}(\\bar{X}_n - μ)}{σ}}{\\frac{S_n}{σ}}\nNumerator: Z_n →^{d} N(0, 1)  (by Central Limit Theorem)\nDenominator: S_n / σ →^{P} 1  (by WLLN + CMT)", "#ffffff", 7.5),
    # Slutsky conclusion
    box(16, 68, 208, 44, "Apply Slutsky (Ratio with c = 1):\nT_n = Z_n / (S_n/σ)  →^{d}  N(0, 1) / 1 = N(0, 1)\nStudent's t distribution collapses to Standard Normal!", "#f8fafc", 8),
    N(120, 138, "Asymptotic normality of Student's t: Slutsky proves T_n →^d N(0, 1) as n → ∞", 8.5)
]
CARDS.append(make_stoma_card(
    15, 6, "WORKED BENCHMARK",
    "Worked Benchmark: Asymptotic Normality of Student's t-Statistic",
    svg_31506,
    "Slutsky proves that Student’s t statistic converges in distribution to the standard normal as sample size grows",
    [
        "<strong>Problem Setup:</strong> For i.i.d. $X_i \\sim (\\mu, \\sigma^2)$, test statistic is $T_n = \\frac{\\sqrt{n}(\\bar{X}_n - \\mu)}{S_n}$ where $S_n^2 = \\frac{1}{n-1}\\sum (X_i - \\bar{X}_n)^2$.",
        "<strong>Component Decomposition:</strong> Numerator $Z_n = \\frac{\\sqrt{n}(\\bar{X}_n - \\mu)}{\\sigma} \\xrightarrow{d} \\mathcal{N}(0, 1)$ by Central Limit Theorem. Denominator $\\frac{S_n}{\\sigma} \\xrightarrow{P} 1$ by WLLN and Continuous Mapping Theorem.",
        "<strong>Slutsky Ratio Law:</strong> By Slutsky's theorem with constant $c = 1$, $T_n = \\frac{Z_n}{S_n / \\sigma} \\xrightarrow{d} \\frac{\\mathcal{N}(0, 1)}{1} = \\mathcal{N}(0, 1)$. Student's $t$ statistic is asymptotically Gaussian!"
    ],
    r"$$T_n = \frac{\sqrt{n}(\bar{X}_n - \mu)}{S_n} = \frac{\frac{\sqrt{n}(\bar{X}_n - \mu)}{\sigma}}{\frac{S_n}{\sigma}} \xrightarrow{d} \frac{\mathcal{N}(0, 1)}{1} = \mathcal{N}(0, 1)$$",
    "Industrial sample testing: when testing more than 30 samples (n > 30), Student's t critical values become virtually indistinguishable from standard normal z-scores.",
    "Assuming T_n is strictly Gaussian for finite n! T_n has heavier polynomial tails (Student's t) for finite n; it becomes Gaussian ONLY in the asymptotic limit n → ∞."
))

# Save cards to cards_stoma.js
save_stoma_cards(CARDS)
print(f"Successfully generated {len(CARDS)} cards for StoMA Topics 14 & 15!")
