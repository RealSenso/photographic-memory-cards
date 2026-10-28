"""Build StoMA Topics 18 & 19 (Cards 31801 to 31906).
Dual-coding photographic plates with pure black-and-white vector diagrams.
"""
import sys, os
sys.path.append(os.path.dirname(__file__))
from stoma_lib import (
    T, N, L, V, P, C, R, E, PG, AX, box, svg, make_stoma_card, save_stoma_cards
)

CARDS = []

# ==============================================================================
# TOPIC 18: CHARACTERISTIC FUNCTIONS & CENTRAL LIMIT THEOREM (31801 - 31806)
# ==============================================================================

# Card 31801: The Characteristic Function: Universal Fourier Dual
svg_31801 = [
    # Unit circle in complex plane
    E(70, 72, 40, 40, fill="#f8fafc", w=1.4),
    AX(25, 72, 115, 25),
    N(112, 70, "Re", 7), N(70, 24, "Im", 7),
    # e^{itx} vector on unit circle
    V(70, 72, 98, 44, 1.8),
    C(98, 44, 3, fill="#000000"),
    N(112, 40, "e^{itX}", 8, w="bold"),
    N(70, 126, "|φ_X(t)| ≤ 1 (Always bounded!)", 7.5, w="bold"),
    # Formula box on right
    box(125, 25, 100, 52, "φ_X(t) = E[e^{itX}]\n= ∫ e^{itx} dF(x)\nALWAYS EXISTS for every distribution", "#ffffff", 7.5),
    N(120, 138, "Universal Fourier dual: bounded by 1, uniformly continuous, exists even for Cauchy", 8.5)
]
CARDS.append(make_stoma_card(
    18, 1, "FOURIER TRANSFORM",
    "The Characteristic Function: Universal Fourier Dual",
    svg_31801,
    "The characteristic function φ_X(t) = E[e^{itX}] always exists and is universally bounded by 1 on the real line",
    [
        "<strong>Definition:</strong> $\\phi_X(t) \\triangleq \\mathbb{E}[e^{itX}] = \\int_{-\\infty}^\\infty e^{itx} dF_X(x)$ for all $t \\in \\mathbb{R}$.",
        "<strong>Universal Existence:</strong> Because $|e^{itX}| = |\\cos(tX) + i\\sin(tX)| = 1$, the integral $\\int |e^{itx}| dF(x) = \\int 1 dF(x) = 1 < \\infty$ ALWAYS converges. Unlike MGFs, $\\phi_X(t)$ exists for every distribution.",
        "<strong>Fundamental Properties:</strong> (1) $\\phi_X(0) = 1$; (2) $|\\phi_X(t)| \\le 1$; (3) $\\phi_X(-t) = \\overline{\\phi_X(t)}$; (4) Uniformly continuous on $\\mathbb{R}$; (5) $\\phi_{aX+b}(t) = e^{itb}\\phi_X(at)$."
    ],
    r"$$\phi_X(t) = \mathbb{E}\left[e^{itX}\right], \qquad |\phi_X(t)| \le \mathbb{E}\left[|e^{itX}|\right] = 1 \quad \forall t \in \mathbb{R}, \qquad \phi_{aX+b}(t) = e^{itb}\phi_X(at)$$",
    "Radio frequency tuning: Fourier decomposition translates any arbitrary time-domain signal into clean, bounded sinusoidal frequencies.",
    "Believing characteristic functions can diverge to infinity like MGFs! Because |e^{itx}| = 1, the characteristic function is universally bounded by 1 everywhere."
))

# Card 31802: Lévy’s Continuity Theorem: Pointwise Fourier Convergence
svg_31802 = [
    # Pointwise convergence curves
    AX(24, 115, 220, 20),
    P("M 24,60 Q 70,30 120,30 Q 170,30 215,60", fill="none", w=2.0),
    N(170, 25, "φ_X(t)", 8.5, w="bold"),
    P("M 24,70 Q 70,35 120,30 Q 170,35 215,70", fill="none", w=1.2, dash="3 3"),
    P("M 24,65 Q 70,32 120,30 Q 170,32 215,65", fill="none", w=1.4, dash="2 2"),
    C(120, 30, 3, fill="#000000"), N(120, 18, "φ(0) = 1", 7.5),
    box(24, 85, 192, 28, "Lévy: X_n →^{d} X  ⇔  φ_{X_n}(t) → φ_X(t) pointwise ∀t ∈ ℝ", "#ffffff", 8.5),
    N(120, 138, "Pointwise convergence of characteristic functions is equivalent to convergence in distribution", 8.5)
]
CARDS.append(make_stoma_card(
    18, 2, "CONTINUITY THEOREM",
    "Lévy’s Continuity Theorem: Pointwise Fourier Convergence",
    svg_31802,
    "Convergence in distribution is mathematically equivalent to pointwise convergence of characteristic functions",
    [
        "<strong>Equivalence Statement:</strong> $X_n \\xrightarrow{d} X \\iff \\lim_{n \\to \\infty} \\phi_{X_n}(t) = \\phi_X(t)$ for all $t \\in \\mathbb{R}$.",
        "<strong>Continuity at Origin:</strong> If $\\lim_{n \\to \\infty} \\phi_{X_n}(t) = g(t)$ pointwise, and $g(t)$ is continuous at $t = 0$, then $g(t)$ is the characteristic function of a valid random variable $X$, and $X_n \\xrightarrow{d} X$.",
        "<strong>Mass Escape Warning:</strong> If $g(t)$ is discontinuous at $t=0$, probability mass escapes to $\\pm\\infty$ (tightness fails) and no limiting random variable exists."
    ],
    r"$$X_n \xrightarrow{d} X \iff \lim_{n \to \infty} \phi_{X_n}(t) = \phi_X(t) \quad \forall t \in \mathbb{R}$$",
    "Tuning musical instruments by acoustic frequencies: matching the sound spectrum pointwise ensures the acoustic waveforms sound identical in physical space.",
    "Ignoring continuity at t = 0! For Unif[-n, n], φ(t) = sin(nt)/(nt) → 0 for t ≠ 0 and 1 at t = 0. The limit is discontinuous at 0, signaling mass escape to infinity."
))

# Card 31803: The Lindeberg-Lévy Central Limit Theorem
svg_31803 = [
    AX(24, 115, 220, 20),
    # Standard normal bell curve
    P("M 30,114 Q 80,114 100,85 Q 120,25 125,25 Q 130,25 150,85 Q 170,114 220,114", fill="none", w=2.0),
    L(125, 25, 125, 114, 1.0, d="2 2"),
    N(125, 126, "0", 9, w="bold"),
    N(175, 45, "Z_n = \\frac{S_n - nμ}{σ√n} →^{d} N(0, 1)", 8.5, w="bold"),
    # CF proof note
    box(24, 20, 100, 36, "φ_{Z_n}(t) = [1 - t²/(2n) + o(t²/n)]ⁿ\n→ exp(-t²/2) = φ_{N(0,1)}(t)", "#ffffff", 7),
    N(120, 138, "CLT: Standardized sum of any i.i.d. variables with finite variance converges to N(0, 1)", 8.5)
]
CARDS.append(make_stoma_card(
    18, 3, "CENTRAL LIMIT THEOREM",
    "The Lindeberg-Lévy Central Limit Theorem",
    svg_31803,
    "The standardized sum of i.i.d. variables with finite variance converges in distribution to the standard Gaussian",
    [
        "<strong>Theorem Statement:</strong> Let $X_1, X_2, \\dots$ be i.i.d. with mean $\\mu$ and finite variance $\\sigma^2 > 0$. Then $Z_n = \\frac{\\sum_{i=1}^n X_i - n\\mu}{\\sigma \\sqrt{n}} \\xrightarrow{d} \\mathcal{N}(0, 1)$.",
        "<strong>Characteristic Function Proof:</strong> Taylor expansion: $\\phi_{\\frac{X-\\mu}{\\sigma}}(u) = 1 - \\frac{u^2}{2} + o(u^2)$. Standardized sum has CF $\\phi_{Z_n}(t) = \\left[1 - \\frac{t^2}{2n} + o(t^2/n)\\right]^n \\to e^{-t^2/2}$ (the exact CF of $\\mathcal{N}(0, 1)$).",
        "<strong>Universal Invariance:</strong> Holds regardless of the underlying distribution's shape (bimodal, uniform, exponential, discrete) as long as variance $\\sigma^2 < \\infty$."
    ],
    r"$$Z_n = \frac{\sum_{i=1}^n X_i - n\mu}{\sigma \sqrt{n}} \xrightarrow{d} \mathcal{N}(0, 1), \qquad \phi_{Z_n}(t) = \left(1 - \frac{t^2}{2n} + o\left(\frac{t^2}{n}\right)\right)^n \to e^{-t^2/2}$$",
    "Galton's bean machine (quincunx): thousands of steel balls bouncing randomly off pins collect at the bottom in an immaculate Gaussian bell curve.",
    "Applying CLT to unscaled sums S_n or raw means X̄_n! S_n variance explodes to ∞; X̄_n variance collapses to 0. CLT applies ONLY to the √n-standardized deviation."
))

# Card 31804: Berry-Esseen Bound & The Continuity Correction
svg_31804 = [
    # Berry-Esseen envelope and formula
    box(16, 20, 208, 42, "Berry-Esseen Theorem (Uniform Rate of Convergence):\nsup_{x ∈ ℝ} |F_{Z_n}(x) - Φ(x)| ≤ \\frac{0.4748 · E[|X - μ|³]}{σ³ √n} = O(1/√n)\n(Convergence rate is governed by skewness and 1/√n)", "#ffffff", 7.5),
    box(16, 68, 208, 44, "Continuity Correction for Integer Sums:\nP(a ≤ S_n ≤ b) ≈ Φ( \\frac{b + 0.5 - nμ}{σ√n} ) - Φ( \\frac{a - 0.5 - nμ}{σ√n} )\n(Shifting limits by ±0.5 accounts for discrete histogram steps)", "#f8fafc", 7.5),
    N(120, 138, "Berry-Esseen guarantees O(1/√n) uniform error; continuity correction fixes discrete steps", 8)
]
CARDS.append(make_stoma_card(
    18, 4, "ASYMPTOTIC CONVERGENCE",
    "Berry-Esseen Bound & The Continuity Correction",
    svg_31804,
    "Berry-Esseen bounds normal approximation error at O(1/√n); continuity correction aligns discrete integer steps",
    [
        "<strong>Berry-Esseen Bound:</strong> If $\\mathbb{E}[|X - \\mu|^3] = \\rho < \\infty$, then $\\sup_{x \\in \\mathbb{R}} |F_{Z_n}(x) - \\Phi(x)| \\le \\frac{C \\rho}{\\sigma^3 \\sqrt{n}}$ with universal constant $C \\le 0.4748$. Error decays strictly at rate $O(1/\\sqrt{n})$.",
        "<strong>Skewness Sensitivity:</strong> Heavy skewness $\\rho/\\sigma^3$ widens the error bound, requiring larger sample sizes $n$ for normal accuracy.",
        "<strong>Continuity Correction:</strong> For discrete integer sums (Binomial, Poisson), adjust integer bounds by $\\pm 0.5$: $\\mathbb{P}(a \\le S_n \\le b) \\approx \\Phi\\left(\\frac{b + 0.5 - n\\mu}{\\sigma\\sqrt{n}}\\right) - \\Phi\\left(\\frac{a - 0.5 - n\\mu}{\\sigma\\sqrt{n}}\\right)$."
    ],
    r"$$\sup_{x \in \mathbb{R}} \left| F_{Z_n}(x) - \Phi(x) \right| \le \frac{0.4748 \cdot \mathbb{E}[|X - \mu|^3]}{\sigma^3 \sqrt{n}}, \quad \mathbb{P}(S_n \le k) \approx \Phi\left(\frac{k + 0.5 - n\mu}{\sigma\sqrt{n}}\right)$$",
    "Sub-pixel antialiasing on computer screens: rendering staircase-like discrete pixels as smooth curves requires a half-pixel offset (±0.5) to balance areas.",
    "Omitting the continuity correction on exam calculations! For moderate sample sizes (n = 50-100), omitting ±0.5 can induce up to 10% calculation error."
))

# Card 31805: Lindeberg vs Lyapunov Conditions for Non-Identical Sums
svg_31805 = [
    box(20, 20, 200, 42, "Lindeberg Condition (Necessary & Sufficient):\ns_n² = ∑ σᵢ²;   ∀ε > 0:  lim_{n → ∞} \\frac{1}{s_n²} ∑_{i=1}^n E[(Xᵢ - μᵢ)² 1_{|Xᵢ - μᵢ| ≥ ε s_n}] = 0\n(Guarantees no single term dominates total variance)", "#ffffff", 7.5),
    box(20, 68, 200, 44, "Lyapunov Condition (Stronger, Easier to Check):\nlim_{n → ∞} \\frac{∑_{i=1}^n E[|Xᵢ - μᵢ|^{2+δ}]}{(s_n²)^{(2+δ)/2}} = 0  for some δ > 0\n⇒ Lindeberg condition holds automatically!", "#f8fafc", 7.5),
    N(120, 138, "CLT extends to non-identical variables as long as no single term swamps the aggregate variance", 8)
]
CARDS.append(make_stoma_card(
    18, 5, "ADVANCED CLT",
    "Lindeberg vs Lyapunov Conditions for Non-Identical Sums",
    svg_31805,
    "Lindeberg and Lyapunov conditions extend the Central Limit Theorem to independent non-identically distributed variables",
    [
        "<strong>Setup:</strong> Let $X_i$ be independent with means $\\mu_i$ and variances $\\sigma_i^2$. Total variance is $s_n^2 = \\sum_{i=1}^n \\sigma_i^2$.",
        "<strong>Lindeberg Condition:</strong> For all $\\epsilon > 0$, $\\lim_{n \\to \\infty} \\frac{1}{s_n^2} \\sum_{i=1}^n \\mathbb{E}[(X_i - \\mu_i)^2 \\mathbf{1}_{\\{|X_i - \\mu_i| \\ge \\epsilon s_n\\}}] = 0$. Guarantees $\\frac{\\sum (X_i - \\mu_i)}{s_n} \\xrightarrow{d} \\mathcal{N}(0, 1)$.",
        "<strong>Lyapunov Condition:</strong> If $\\lim_{n \\to \\infty} \\frac{1}{s_n^{2+\\delta}} \\sum_{i=1}^n \\mathbb{E}[|X_i - \\mu_i|^{2+\\delta}] = 0$ for some $\\delta > 0$, then Lindeberg's condition holds automatically."
    ],
    r"$$\text{Lyapunov: } \lim_{n \to \infty} \frac{\sum_{i=1}^n \mathbb{E}[|X_i - \mu_i|^{2+\delta}]}{\left(\sum_{i=1}^n \sigma_i^2\right)^{(2+\delta)/2}} = 0 \implies \frac{\sum_{i=1}^n (X_i - \mu_i)}{\sqrt{\sum \sigma_i^2}} \xrightarrow{d} \mathcal{N}(0, 1)$$",
    "Electronic noise floor: thousands of dissimilar microscopic resistors contributing random thermal noise; as long as no single component dominates, the output is Gaussian.",
    "Applying CLT when one giant term dominates the sum! If X₁ contributes 90% of total variance, the sum reflects X₁'s individual distribution and fails CLT."
))

# Card 31806: Worked Benchmark: De Moivre-Laplace on 100 Coin Flips
svg_31806 = [
    box(16, 20, 208, 44, "Problem: S₁₀₀ ~ Binomial(100, 0.5). Find P(45 ≤ S₁₀₀ ≤ 55)\nParameters: μ = np = 50,  σ² = np(1-p) = 25 ⇒ σ = 5\nContinuity Correction: Expand [45, 55] to [44.5, 55.5]", "#ffffff", 7.5),
    box(16, 70, 208, 44, "Standardize:\nz₁ = (44.5 - 50)/5 = -1.1,   z₂ = (55.5 - 50)/5 = +1.1\nP(45 ≤ S₁₀₀ ≤ 55) ≈ Φ(1.1) - Φ(-1.1) = 2Φ(1.1) - 1\n= 2(0.8643) - 1 = 0.7286  (Exact: 0.72874)", "#f8fafc", 7.5),
    N(120, 138, "Continuity correction delivers 99.98% accuracy matching the exact Binomial sum", 8.5)
]
CARDS.append(make_stoma_card(
    18, 6, "WORKED BENCHMARK",
    "Worked Benchmark: De Moivre-Laplace CLT on 100 Coin Flips",
    svg_31806,
    "Applying the Central Limit Theorem with continuity correction matches exact binomial probability to 4 decimal places",
    [
        "<strong>Problem Setup:</strong> Toss a fair coin $n = 100$ times ($p = 0.5$). Find $\\mathbb{P}(45 \\le S_{100} \\le 55)$.",
        "<strong>Parameters:</strong> $\\mu = np = 50$, $\\sigma = \\sqrt{np(1-p)} = \\sqrt{25} = 5$.",
        "<strong>Continuity Correction & Evaluation:</strong> Expand to $[44.5, 55.5]$. Standardized bounds: $z_1 = -1.1, z_2 = +1.1$. Probability is $\\Phi(1.1) - \\Phi(-1.1) = 2\\Phi(1.1) - 1 = 2(0.8643) - 1 = 0.7286$ (error vs exact binomial is $< 0.02\\%$)."
    ],
    r"$$\mathbb{P}(45 \le S_{100} \le 55) \approx \Phi\left(\frac{55.5 - 50}{5}\right) - \Phi\left(\frac{44.5 - 50}{5}\right) = 2\Phi(1.1) - 1 \approx 0.7286$$",
    "Precinct vote tallies: in a razor-thin 50/50 election, a random sample of 100 votes lands within ±5 votes of dead center with 73% probability.",
    "Evaluating without continuity correction: (55 - 50)/5 = 1.0 ⇒ 2Φ(1.0) - 1 = 0.6827, introducing an unnecessary 4.6% approximation error."
))

# ==============================================================================
# TOPIC 19: DTMC & STATE CLASSIFICATION (31901 - 31906)
# ==============================================================================

# Card 31901: The Markov Property & Row-Stochastic Transition Matrix
svg_31901 = [
    # 3-state directed graph
    C(50, 45, 14, fill="#ffffff", w=1.5), N(50, 48, "1", 10, w="bold"),
    C(150, 45, 14, fill="#ffffff", w=1.5), N(150, 48, "2", 10, w="bold"),
    C(100, 105, 14, fill="#ffffff", w=1.5), N(100, 108, "3", 10, w="bold"),
    # Directed arrows
    V(64, 45, 136, 45, 1.4), N(100, 38, "P₁₂", 7.5),
    V(142, 57, 108, 93, 1.4), N(132, 78, "P₂₃", 7.5),
    V(92, 93, 58, 57, 1.4), N(68, 78, "P₃₁", 7.5),
    # Row-stochastic definition box
    box(160, 80, 72, 36, "Row-Stochastic:\nP ≥ 0\n∑_j P_{ij} = 1", "#f8fafc", 7.5),
    N(120, 138, "Markov Property: Future is conditionally independent of past given the present state", 8.5)
]
CARDS.append(make_stoma_card(
    19, 1, "MARKOV PROPERTY",
    "The Markov Property & Row-Stochastic Transition Matrix",
    svg_31901,
    "The future state depends only on the present state, encoded by row-stochastic matrix P where each row sums to 1",
    [
        "<strong>Markov Property:</strong> $\\mathbb{P}(X_{n+1} = j \\mid X_n = i, X_{n-1} = i_{n-1}, \\dots, X_0 = i_0) = \\mathbb{P}(X_{n+1} = j \\mid X_n = i) \\triangleq P_{ij}$.",
        "<strong>Memoryless Future:</strong> Conditioned on current state $X_n$, future evolution $X_{n+1}$ is independent of past history $X_0, \\dots, X_{n-1}$.",
        "<strong>Row-Stochastic Matrix:</strong> $P = [P_{ij}]$ satisfies $P_{ij} \\ge 0$ and $\\sum_{j \\in S} P_{ij} = 1$ for all $i \\in S$ (matrix equation $P \\mathbf{1} = \\mathbf{1}$)."
    ],
    r"$$\mathbb{P}(X_{n+1} = j \mid X_n = i, X_{n-1} = i_{n-1}, \dots, X_0 = i_0) = P_{ij}, \qquad \sum_{j \in S} P_{ij} = 1 \quad \forall i$$",
    "Board game of Monopoly: the square you land on next depends strictly on your current square and the dice roll, regardless of what path you traveled in earlier turns.",
    "Assuming matrix columns sum to 1! In general, P is ROW-stochastic (rows sum to 1). A matrix whose columns also sum to 1 is doubly stochastic (a special subclass)."
))

# Card 31902: Chapman-Kolmogorov Equations: P^{(n)} = P^n
svg_31902 = [
    # State i to k to j
    C(40, 72, 12, fill="#ffffff", w=1.5), N(40, 75, "i", 9, w="bold"),
    C(120, 35, 12, fill="#f8fafc", w=1.5), N(120, 38, "k₁", 8),
    C(120, 72, 12, fill="#f8fafc", w=1.5), N(120, 75, "k₂", 8),
    C(120, 108, 12, fill="#f8fafc", w=1.5), N(120, 111, "k₃", 8),
    C(200, 72, 12, fill="#ffffff", w=1.5), N(200, 75, "j", 9, w="bold"),
    # Transition lines
    V(52, 68, 108, 38, 1.2), V(132, 38, 188, 68, 1.2),
    V(52, 72, 108, 72, 1.2), V(132, 72, 188, 72, 1.2),
    V(52, 76, 108, 105, 1.2), V(132, 105, 188, 76, 1.2),
    N(80, 24, "P_{ik}^{(m)}", 7.5), N(160, 24, "P_{kj}^{(n)}", 7.5),
    N(120, 138, "Chapman-Kolmogorov: P_{ij}^{(m+n)} = ∑_k P_{ik}^{(m)} P_{kj}^{(n)}  ⇔  P^{(n)} = Pⁿ", 8.5)
]
CARDS.append(make_stoma_card(
    19, 2, "CHAPMAN-KOLMOGOROV",
    "Chapman-Kolmogorov Equations: P^{(n)} = Pⁿ",
    svg_31902,
    "The n-step transition probability matrix is the n-th algebraic matrix power: P^{(n)} = Pⁿ",
    [
        "<strong>Intermediate Splitting:</strong> To transition from $i$ to $j$ in $(m+n)$ steps, the chain must pass through some intermediate state $k$ at step $m$.",
        "<strong>Chapman-Kolmogorov Formula:</strong> $P_{ij}^{(m+n)} = \\sum_{k \\in S} P_{ik}^{(m)} P_{kj}^{(n)}$ for all $m, n \\ge 1$.",
        "<strong>Matrix Power Representation:</strong> In matrix form, $P^{(n)} = P^n$. Unconditional distribution after $n$ steps is $\\mathbf{p}^{(n)} = \\mathbf{p}^{(0)} P^n$ (where $\\mathbf{p}^{(0)}$ is a row vector)."
    ],
    r"$$P_{ij}^{(m+n)} = \sum_{k \in S} P_{ik}^{(m)} P_{kj}^{(n)} \iff P^{(m+n)} = P^m P^n, \qquad \mathbf{p}^{(n)} = \mathbf{p}^{(0)} P^n$$",
    "Airline route planning: the probability of reaching destination J from origin I in two flights sums the probabilities over all possible intermediate layover hubs K.",
    "Multiplying state distribution from the wrong side: p^{(n)} = p^{(0)} P^n where p^{(0)} is a ROW vector. Writing P^n p^{(0)} causes matrix dimension mismatch!"
))

# Card 31903: Accessibility, Communication & Class Decomposition
svg_31903 = [
    # Communicating class {1, 2}
    R(25, 30, 85, 75, fill="#f8fafc", sw=1.3, rx=8),
    N(67, 45, "Class C₁ (1 ↔ 2)", 8, w="bold"),
    C(45, 75, 10, fill="#ffffff", w=1.4), N(45, 78, "1", 8.5),
    C(90, 75, 10, fill="#ffffff", w=1.4), N(90, 78, "2", 8.5),
    V(55, 72, 80, 72, 1.2), V(80, 78, 55, 78, 1.2),
    # One-way bridge to absorbing class {3}
    V(110, 67, 145, 67, 1.5),
    N(127, 58, "1-way", 7),
    R(145, 30, 70, 75, fill="#e2e8f0", sw=1.3, rx=8),
    N(180, 45, "Class C₂", 8, w="bold"),
    C(180, 75, 10, fill="#ffffff", w=1.4), N(180, 78, "3", 8.5),
    N(120, 138, "Communication (i ↔ j) partitions states into disjoint classes; irreducible if 1 class", 8.5)
]
CARDS.append(make_stoma_card(
    19, 3, "COMMUNICATION CLASSES",
    "Accessibility, Communication & Class Decomposition",
    svg_31903,
    "Communication is an equivalence relation that partitions the Markov chain into disjoint communicating classes",
    [
        "<strong>Accessibility ($i \\to j$):</strong> State $j$ is accessible from $i$ if $P_{ij}^{(n)} > 0$ for some $n \\ge 0$ (path of positive probability).",
        "<strong>Communication ($i \\leftrightarrow j$):</strong> States communicate if $i \\to j$ and $j \\to i$. Communication is an EQUIVALENCE RELATION (reflexive, symmetric, transitive).",
        "<strong>Class Partition & Irreducibility:</strong> State space $S$ partitions into disjoint communicating classes $C_k$. A chain is **irreducible** if it consists of exactly ONE communicating class."
    ],
    r"$$i \to j \iff \exists n \ge 0 \text{ s.t. } P_{ij}^{(n)} > 0; \qquad i \leftrightarrow j \iff i \to j \text{ and } j \to i; \qquad S = \bigcup C_k$$",
    "Subway transit network: if you can ride from station A to station B and return from B to A, both stations belong to the same connected transit line.",
    "Confusing 1-step transitions with accessibility! P_{ij} = 0 does NOT imply j is inaccessible from i; state j might be reached in 2, 3, or more hops (P_{ij}^{(n)} > 0)."
))

# Card 31904: Recurrence vs Transience: Return Probability & Green Function
svg_31904 = [
    # State with looping arrow
    box(20, 20, 96, 44, "Recurrent State:\nf_{ii} = P(τ_i < ∞ | X₀=i) = 1\n∑_{n=1}^∞ P_{ii}^{(n)} = ∞\n(Certain infinite returns)", "#ffffff", 7.5),
    box(124, 20, 96, 44, "Transient State:\nf_{ii} = P(τ_i < ∞ | X₀=i) < 1\n∑_{n=1}^∞ P_{ii}^{(n)} < ∞\n(Total visits ~ Geom(1-f))", "#f8fafc", 7.5),
    # Green function formula
    R(20, 72, 200, 42, fill="#ffffff", sw=1.3),
    N(120, 86, "Green Function (Expected Total Visits): G_{ii} = ∑_{n=0}^∞ P_{ii}^{(n)}", 8, w="bold"),
    N(120, 102, "Recurrent: G_{ii} = ∞;    Transient: G_{ii} = 1 / (1 - f_{ii}) < ∞", 8.5),
    N(120, 138, "Every finite-state Markov chain contains at least one recurrent class", 8.5)
]
CARDS.append(make_stoma_card(
    19, 4, "RECURRENCE & TRANSIENCE",
    "Recurrence vs Transience: Return Probability f_{ii} & Green Function",
    svg_31904,
    "Recurrent states guarantee return with probability 1 and infinite expected visits; transient states drift away forever",
    [
        "<strong>First Return Probability:</strong> Let $\\tau_i \\triangleq \\min\\{n \\ge 1 : X_n = i\\}$. Return probability is $f_{ii} \\triangleq \\mathbb{P}(\\tau_i < \\infty \\mid X_0 = i)$.",
        "<strong>Recurrent ($f_{ii} = 1$):</strong> Returns to state $i$ with probability 1; the chain visits state $i$ infinitely many times almost surely, so $\\sum_{n=1}^\\infty P_{ii}^{(n)} = \\infty$.",
        "<strong>Transient ($f_{ii} < 1$):</strong> Non-zero probability $(1 - f_{ii})$ of never returning; total return visits follow $\\text{Geometric}(1 - f_{ii})$ with finite expectation $\\sum_{n=1}^\\infty P_{ii}^{(n)} = \\frac{f_{ii}}{1 - f_{ii}} < \\infty$."
    ],
    r"$$i \text{ recurrent} \iff f_{ii} = 1 \iff \sum_{n=1}^\infty P_{ii}^{(n)} = \infty; \qquad i \text{ transient} \iff f_{ii} < 1 \iff \sum_{n=1}^\infty P_{ii}^{(n)} < \infty$$",
    "Boomerang vs paper airplane: a boomerang returns to your hand with 100% certainty (recurrent); a paper airplane drifts away with positive probability and never returns (transient).",
    "Assuming all states in a finite Markov chain can be transient. In ANY finite-state Markov chain, at least ONE state must be recurrent (probability mass has nowhere to escape)."
))

# Card 31905: Periodicity & Class Invariant Theorem
svg_31905 = [
    # Bipartite period 2 graph
    box(24, 25, 75, 45, "Set A\n(States 1, 3)", "#ffffff", 8.5),
    V(99, 42, 141, 42, 1.4), V(141, 52, 99, 52, 1.4),
    box(141, 25, 75, 45, "Set B\n(States 2, 4)", "#ffffff", 8.5),
    N(120, 34, "Step 1", 7), N(120, 62, "Step 2", 7),
    # Period formula box
    box(24, 78, 192, 40, "Period d(i) = gcd{n ≥ 1 : P_{ii}^{(n)} > 0}\nSelf-loop P_{ii} > 0  ⇒  d(i) = 1 (Aperiodic!)\nClass Property: i ↔ j ⇒ d(i) = d(j)", "#f8fafc", 8),
    N(120, 138, "Periodicity, recurrence, and transience are shared by all states in a communicating class", 8.5)
]
CARDS.append(make_stoma_card(
    19, 5, "PERIODICITY",
    "State Periodicity & Class Sharing Properties",
    svg_31905,
    "Period is the gcd of all possible return times; periodicity and recurrence are shared class invariants",
    [
        "<strong>Period Definition:</strong> Period of state $i$ is $d(i) \\triangleq \\gcd\\{n \\ge 1 : P_{ii}^{(n)} > 0\\}$. If $d(i) = 1$, the state is **aperiodic**.",
        "<strong>Class Invariance Theorem:</strong> Recurrence, transience, and periodicity are **CLASS PROPERTIES**: if $i \\leftrightarrow j$, then $d(i) = d(j)$, and $i$ is recurrent $\\iff j$ is recurrent.",
        "<strong>Self-Loop Shortcut:</strong> If state $i$ has a self-loop ($P_{ii} > 0$), then $1 \\in \\{n : P_{ii}^{(n)} > 0\\}$, so $d(i) = \\gcd(1, \\dots) = 1$ (instantly aperiodic!)."
    ],
    r"$$d(i) \triangleq \gcd\{n \ge 1 : P_{ii}^{(n)} > 0\}; \qquad i \leftrightarrow j \implies d(i) = d(j) \text{ and } (i \text{ rec} \iff j \text{ rec})$$",
    "A grandfather clock pendulum: swinging left then right returns to the starting position only at even ticks n = 2, 4, 6... (period 2).",
    "Defining period as the minimum return time! Period is the GREATEST COMMON DIVISOR of all return times, not the length of the shortest loop."
))

# Card 31906: Worked Benchmark: 1D Random Walk Recurrence (Pólya’s Theorem)
svg_31906 = [
    # 1D lattice
    L(20, 72, 220, 72, 1.8),
    C(40, 72, 3, fill="#000000"), N(40, 86, "-2", 7.5),
    C(80, 72, 3, fill="#000000"), N(80, 86, "-1", 7.5),
    C(120, 72, 4, fill="#000000"), N(120, 86, "0", 8.5, w="bold"),
    C(160, 72, 3, fill="#000000"), N(160, 86, "+1", 7.5),
    C(200, 72, 3, fill="#000000"), N(200, 86, "+2", 7.5),
    # Arcs
    P("M 120,72 Q 140,50 160,72", fill="none", w=1.2, ar=True), N(140, 45, "p", 7.5),
    P("M 120,72 Q 100,50 80,72", fill="none", w=1.2, ar=True), N(100, 45, "1-p", 7.5),
    # Stirling result box
    box(20, 18, 200, 24, "P_{00}^{(2n)} = \\binom{2n}{n} p^n (1-p)^n ~ \\frac{(4p(1-p))^n}{\\sqrt{πn}}", "#ffffff", 8),
    box(20, 96, 200, 28, "Symmetric p = 1/2: ∑ 1/√n = ∞ ⇒ RECURRENT (Pólya 1921)\nAsymmetric p ≠ 1/2: 4p(1-p) < 1 ⇒ ∑ < ∞ ⇒ TRANSIENT", "#f8fafc", 7.5),
    N(120, 138, "1D symmetric random walk returns home with certainty; asymmetric walk drifts away forever", 8)
]
CARDS.append(make_stoma_card(
    19, 6, "WORKED BENCHMARK",
    "Worked Benchmark: 1D Random Walk Recurrence (Pólya’s Theorem)",
    svg_31906,
    "Symmetric 1D random walk returns home with probability 1 (recurrent); asymmetric walks are transient",
    [
        "<strong>Problem Setup:</strong> Random walk on $\\mathbb{Z}$: $X_{n+1} = X_n + \\xi_n$ where $\\mathbb{P}(\\xi = +1) = p$ and $\\mathbb{P}(\\xi = -1) = 1 - p$. Returns occur only at even steps $2n$.",
        "<strong>Return Probability:</strong> $P_{00}^{(2n)} = \\binom{2n}{n} p^n (1-p)^n$. By Stirling's approximation, $\\binom{2n}{n} \\sim \\frac{4^n}{\\sqrt{\\pi n}}$, so $P_{00}^{(2n)} \\sim \\frac{(4p(1-p))^n}{\\sqrt{\\pi n}}$.",
        "<strong>Dichotomy:</strong> If $p = 1/2$, $4p(1-p) = 1$, so $\\sum P_{00}^{(2n)} \\sim \\sum \\frac{1}{\\sqrt{\\pi n}} = \\infty \\implies$ **RECURRENT**. If $p \\ne 1/2$, $4p(1-p) < 1$, so the series converges geometrically $\\implies$ **TRANSIENT**."
    ],
    r"$$P_{00}^{(2n)} \sim \frac{(4p(1-p))^n}{\sqrt{\pi n}} \implies \sum_{n=1}^\infty P_{00}^{(2n)} = \begin{cases} \infty & p = 1/2 \quad (\text{Recurrent}) \\ < \infty & p \ne 1/2 \quad (\text{Transient}) \end{cases}$$",
    "Pólya's famous theorem: 'A drunk man will always find his way home (1D is recurrent), but a drunk bird can get lost forever (3D random walk is transient with return probability ~0.34).'",
    "Missing period 2: P_{00}^{(2n+1)} = 0 for all odd steps. Returns require an equal number of left and right steps; only even powers contribute to the return series."
))

# Save cards to cards_stoma.js
save_stoma_cards(CARDS)
print(f"Successfully generated {len(CARDS)} cards for StoMA Topics 18 & 19!")
