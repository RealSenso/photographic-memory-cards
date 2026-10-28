"""Build StoMA Topics 16 & 17 (Cards 31601 to 31706).
Dual-coding photographic plates with pure black-and-white vector diagrams.
"""
import sys, os
sys.path.append(os.path.dirname(__file__))
from stoma_lib import (
    T, N, L, V, P, C, R, E, PG, AX, box, svg, make_stoma_card, save_stoma_cards
)

CARDS = []

# ==============================================================================
# TOPIC 16: BOREL-CANTELLI LEMMAS & LIMSUP/LIMINF (31601 - 31606)
# ==============================================================================

# Card 31601: Limsup (Infinitely Often) vs Liminf (All But Finitely Often)
svg_31601 = [
    box(16, 20, 208, 44, "limsup A_n = {A_n i.o.} = ⋂_{n=1}^∞ ⋃_{k=n}^∞ A_k\n(Outcome ω occurs in infinitely many events A_n)", "#ffffff", 8.5),
    box(16, 70, 208, 44, "liminf A_n = {A_n a.b.f.o.} = ⋃_{n=1}^∞ ⋂_{k=n}^∞ A_k\n(Outcome ω occurs in all but finitely many events A_n)", "#f8fafc", 8.5),
    N(120, 138, "De Morgan Duality: (limsup A_n)ᶜ = liminf A_nᶜ; liminf A_n ⊆ limsup A_n always", 8)
]
CARDS.append(make_stoma_card(
    16, 1, "SET LIMITS",
    "Limsup (Infinitely Often) vs Liminf (All But Finitely Often)",
    svg_31601,
    "Limsup captures outcomes occurring infinitely often; Liminf captures outcomes occurring in all but finitely many events",
    [
        "<strong>Limsup Definition:</strong> $\\limsup_{n \\to \\infty} A_n \\triangleq \\bigcap_{n=1}^\\infty \\bigcup_{k=n}^\\infty A_k = \\{A_n \\text{ i.o.}\\}$ (infinitely often). $\\omega \\in \\limsup A_n \\iff \\omega$ belongs to infinitely many $A_n$.",
        "<strong>Liminf Definition:</strong> $\\liminf_{n \\to \\infty} A_n \\triangleq \\bigcup_{n=1}^\\infty \\bigcap_{k=n}^\\infty A_k = \\{A_n \\text{ a.b.f.o.}\\}$ (all but finitely often). $\\omega \\in \\liminf A_n \\iff \\exists N$ such that $\\omega \\in A_n$ for all $n \\ge N$.",
        "<strong>De Morgan Duality:</strong> $(\\limsup A_n)^c = \\liminf A_n^c$. Furthermore, $\\liminf A_n \\subseteq \\limsup A_n$ always holds."
    ],
    r"$$\limsup_{n \to \infty} A_n = \bigcap_{n=1}^\infty \bigcup_{k=n}^\infty A_k = \{A_n \text{ i.o.}\}, \qquad \left(\limsup A_n\right)^c = \liminf A_n^c$$",
    "Meteor showers: seeing shooting stars infinitely often (limsup) means they never permanently stop; seeing them in all but finitely many seconds (liminf) means they eventually become continuous.",
    "Swapping intersection and union! Limsup is intersection of unions (⋂ ⋃); Liminf is union of intersections (⋃ ⋂). Swapping them completely reverses their mathematical meaning."
))

# Card 31602: First Borel-Cantelli Lemma (BC1): Sum P(A_n) < ∞
svg_31602 = [
    # Finite sum arrow to P = 0
    box(24, 20, 96, 36, "Finite Sum:\n∑_{n=1}^∞ P(A_n) < ∞", "#ffffff", 9),
    V(120, 38, 144, 38, 1.4),
    box(144, 20, 72, 36, "P(A_n i.o.) = 0\n(Zero prob!)", "#e2e8f0", 9),
    # Proof sketch
    box(24, 68, 192, 46, "Proof: P(limsup A_n) = P(⋂_{n=1}^∞ ⋃_{k=n}^∞ A_k)\n≤ P(⋃_{k=n}^∞ A_k) ≤ ∑_{k=n}^∞ P(A_k) → 0  (tail sum of convergent series!)\nNO INDEPENDENCE REQUIRED!", "#f8fafc", 7.5),
    N(120, 138, "First Borel-Cantelli Lemma: Convergent probability sum implies event occurs only finitely many times", 8)
]
CARDS.append(make_stoma_card(
    16, 2, "BOREL-CANTELLI 1",
    "The First Borel-Cantelli Lemma: Sum P(A_n) < ∞ ⇒ P(A_n i.o.) = 0",
    svg_31602,
    "If the sum of probabilities converges, the events occur infinitely often with probability exactly zero",
    [
        "<strong>Theorem Statement:</strong> For ANY sequence of events $\\{A_n\\}$, if $\\sum_{n=1}^\\infty \\mathbb{P}(A_n) < \\infty$, then $\\mathbb{P}(\\limsup A_n) = \\mathbb{P}(A_n \\text{ i.o.}) = 0$.",
        "<strong>Direct Union Bound Proof:</strong> By continuity of measure, $\\mathbb{P}(\\limsup A_n) \\le \\mathbb{P}(\\bigcup_{k=n}^\\infty A_k) \\le \\sum_{k=n}^\\infty \\mathbb{P}(A_k)$. As $n \\to \\infty$, the tail of a convergent series tends to 0.",
        "<strong>ZERO Independence Assumption:</strong> BC1 holds unconditionally for dependent, correlated, or adversarial sequences of events."
    ],
    r"$$\sum_{n=1}^\infty \mathbb{P}(A_n) < \infty \implies \mathbb{P}\left(\limsup_{n \to \infty} A_n\right) = \mathbb{P}(A_n \text{ i.o.}) = 0 \quad (\text{NO independence needed})$$",
    "A leaky faucet: if the total expected number of water drops over all future time is finite (∑ P(A_n) < ∞), the faucet is guaranteed to stop dripping permanently after some finite hour.",
    "Assuming BC1 requires independence! BC1 is a pure measure-theoretic consequence of countable sub-additivity; it requires zero independence."
))

# Card 31603: Second Borel-Cantelli Lemma (BC2): Sum P(A_n) = ∞ + Independence
svg_31603 = [
    box(20, 20, 200, 36, "Second Borel-Cantelli Lemma (BC2):\nIf {A_n} are INDEPENDENT and ∑_{n=1}^∞ P(A_n) = ∞\n⇒ P(limsup A_n) = P(A_n i.o.) = 1", "#ffffff", 8),
    # Product bound proof box
    box(20, 64, 200, 48, "Proof: P( (⋃_{k=n}^m A_k)ᶜ ) = ∏_{k=n}^m (1 - P(A_k))\n≤ ∏_{k=n}^m exp(-P(A_k)) = exp( - ∑_{k=n}^m P(A_k) ) → 0\n⇒ P(⋃_{k=n}^∞ A_k) = 1  ∀n  ⇒  P(limsup A_n) = 1", "#f8fafc", 7),
    N(120, 138, "BC2 strictly requires independence: divergent sum + independence forces event to recur infinitely often", 8)
]
CARDS.append(make_stoma_card(
    16, 3, "BOREL-CANTELLI 2",
    "The Second Borel-Cantelli Lemma: Independence & Divergence",
    svg_31603,
    "If events are mutually independent and their probabilities diverge, the event occurs infinitely often with probability 1",
    [
        "<strong>Theorem Statement:</strong> If events $\\{A_n\\}$ are MUTUALLY INDEPENDENT and $\\sum_{n=1}^\\infty \\mathbb{P}(A_n) = \\infty$, then $\\mathbb{P}(\\limsup A_n) = \\mathbb{P}(A_n \\text{ i.o.}) = 1$.",
        "<strong>Product Inequality Proof:</strong> $\\mathbb{P}(\\bigcap_{k=n}^m A_k^c) = \\prod_{k=n}^m (1 - \\mathbb{P}(A_k)) \\le \\prod_{k=n}^m e^{-\\mathbb{P}(A_k)} = \\exp(-\\sum_{k=n}^m \\mathbb{P}(A_k)) \\to 0$. Thus $\\mathbb{P}(\\bigcup_{k=n}^\\infty A_k) = 1$ for all $n$.",
        "<strong>Strict Independence Mandate:</strong> Unlike BC1, BC2 FAILS without independence! Correlated events with divergent sums can fail to occur infinitely often."
    ],
    r"$$\{A_n\} \text{ independent}, \quad \sum_{n=1}^\infty \mathbb{P}(A_n) = \infty \implies \mathbb{P}\left(\limsup_{n \to \infty} A_n\right) = 1$$",
    "Infinite monkeys on typewriters: the probability of typing 'HAMLET' on any attempt is tiny (~10⁻⁵⁰), but independent attempts continue forever (∑ p = ∞), guaranteeing the event occurs with probability 1.",
    "Applying BC2 without independence! If A_n = A for all n with P(A) = 1/2, then ∑ P(A_n) = ∞, yet P(A_n i.o.) = P(A) = 1/2 ≠ 1! Independence is indispensable."
))

# Card 31604: Kolmogorov’s Zero-One Law & Tail Events
svg_31604 = [
    # Tail algebra diagram
    box(24, 20, 192, 42, "Tail σ-Algebra:  𝒯 = ⋂_{n=1}^∞ σ(X_n, X_{n+1}, ...)\n(Events whose occurrence is unaffected by any finite prefix)", "#ffffff", 8),
    box(24, 70, 192, 42, "Kolmogorov's Zero-One Law:\nFor independent {X_n}, if E ∈ 𝒯  ⇒  P(E) = 0   OR   P(E) = 1\n(Tail events have NO intermediate probabilities!)", "#e2e8f0", 8),
    N(120, 138, "Tail events include: convergence of series ∑ X_n, limsup X_n, and asymptotic frequency limits", 8)
]
CARDS.append(make_stoma_card(
    16, 4, "ZERO-ONE LAW",
    "Kolmogorov’s Zero-One Law: Binary Tail Probabilities",
    svg_31604,
    "Any event that does not depend on finite prefixes of an independent sequence has probability strictly 0 or 1",
    [
        "<strong>Tail $\\sigma$-Algebra:</strong> $\\mathcal{T} \\triangleq \\bigcap_{n=1}^\\infty \\sigma(X_n, X_{n+1}, \\dots)$. An event $E \\in \\mathcal{T}$ is unaffected by changing the values of any finite prefix $X_1, \\dots, X_M$.",
        "<strong>Kolmogorov's Theorem:</strong> If $\\{X_n\\}$ are independent, then for every tail event $E \\in \\mathcal{T}$, $\\mathbb{P}(E) \\in \\{0, 1\\}$. Tail probabilities are binary: either impossible or certain!",
        "<strong>Canonical Tail Events:</strong> Event $\\{\\sum X_n \\text{ converges}\\}$, $\\{\\lim X_n \\text{ exists}\\}$, $\\{\\limsup X_n \\le c\\}$, and $\\{\\lim \\frac{1}{n}\\sum X_i = \\mu\\}$ are all tail events."
    ],
    r"$$\mathcal{T} = \bigcap_{n=1}^\infty \sigma(X_n, X_{n+1}, \dots), \quad \{X_n\} \text{ independent} \implies \mathbb{P}(E) \in \{0, 1\} \quad \forall E \in \mathcal{T}$$",
    "A coin toss destiny: whether the fraction of heads converges as n → ∞ cannot be altered by altering the first 100 tosses; its truth is an all-or-nothing tail property.",
    "Assuming event {X₁ = 1} is a tail event! The first step X₁ is in the prefix, not the tail. Only asymptotic properties invariant to finite prefixes belong to 𝒯."
))

# Card 31605: Proving Almost Sure Convergence via Borel-Cantelli
svg_31605 = [
    # 3-step proof bridge
    box(20, 20, 200, 26, "Target: Prove X_n →^{a.s.} X", "#ffffff", 8.5),
    V(120, 46, 120, 60, 1.2),
    box(20, 60, 200, 26, "Define bad events: A_n(ε) = { |X_n - X| ≥ ε }", "#f8fafc", 8),
    V(120, 86, 120, 100, 1.2),
    box(20, 100, 200, 26, "Show ∑_{n=1}^∞ P(|X_n - X| ≥ ε) < ∞  ∀ε > 0  ⇒  P(A_n(ε) i.o.) = 0", "#e2e8f0", 8),
    N(120, 138, "Master recipe: Summability of error probabilities proves almost sure convergence via BC1", 8.5)
]
CARDS.append(make_stoma_card(
    16, 5, "BC1 PROOF METHOD",
    "Proving Almost Sure Convergence via Borel-Cantelli 1",
    svg_31605,
    "The standard analytical method for establishing almost sure convergence: show error probability series converges",
    [
        "<strong>Equivalence Criterion:</strong> $X_n \\xrightarrow{a.s.} X \\iff \\mathbb{P}(\\limsup_{n \\to \\infty} \\{|X_n - X| \\ge \\epsilon\\}) = 0$ for all $\\epsilon > 0$.",
        "<strong>Sufficient Condition:</strong> By BC1, to prove $X_n \\xrightarrow{a.s.} X$, it is SUFFICIENT to show that $\\sum_{n=1}^\\infty \\mathbb{P}(|X_n - X| \\ge \\epsilon) < \\infty$ for every $\\epsilon > 0$.",
        "<strong>Markov / Chebyshev Synergy:</strong> Combine with Markov's inequality: if $\\mathbb{P}(|X_n - X| \\ge \\epsilon) \\le \\frac{\\mathbb{E}[|X_n - X|^p]}{\\epsilon^p}$ and $\\sum \\mathbb{E}[|X_n - X|^p] < \\infty$, almost sure convergence follows immediately."
    ],
    r"$$\sum_{n=1}^\infty \mathbb{P}(|X_n - X| \ge \epsilon) < \infty \quad \forall \epsilon > 0 \implies X_n \xrightarrow{\text{a.s.}} X$$",
    "Eradicating a disease: if the probability of outbreaks at year n sums to a finite number over all centuries, the disease is guaranteed to disappear permanently with probability 1.",
    "Attempting to check a.s. convergence pointwise by hand! Pathwise limits are analytically intractable; the summable probability test (BC1) is the universal tool."
))

# Card 31606: Worked Benchmark: Infinite Coin Toss Runs of Consecutive Heads
svg_31606 = [
    # Consecutive heads blocks
    box(20, 20, 96, 36, "Event A_k:\nBlock k of length L_k\nhas ALL Heads", "#ffffff", 8),
    box(124, 20, 96, 36, "P(A_k) = (1/2)^{L_k}\nDisjoint blocks ⇒\nMutually independent", "#ffffff", 7.5),
    # Dichotomy box
    box(20, 68, 200, 44, "Dichotomy by Borel-Cantelli:\n(1) L_k = c log₂(k): ∑ k⁻ᶜ < ∞ for c > 1 ⇒ Finitely many runs (BC1)\n(2) L_k = c log₂(k): ∑ k⁻ᶜ = ∞ for c ≤ 1 ⇒ Infinitely many runs (BC2)", "#f8fafc", 7.5),
    N(120, 138, "Runs of length (1 - ε) log₂(n) occur infinitely often; runs of (1 + ε) log₂(n) cease permanently", 8)
]
CARDS.append(make_stoma_card(
    16, 6, "WORKED BENCHMARK",
    "Worked Benchmark: Longest Head Runs in Infinite Coin Tosses",
    svg_31606,
    "Borel-Cantelli pins down the exact logarithmic growth of the longest streak of heads in infinite coin tosses",
    [
        "<strong>Problem Setup:</strong> Divide an infinite sequence of fair coin tosses into non-overlapping blocks of length $L_k$. Event $A_k$: block $k$ consists entirely of Heads ($P(A_k) = 2^{-L_k}$). Blocks are independent.",
        "<strong>Case 1 ($L_k = (1+\\epsilon)\\log_2 k$):</strong> $\\mathbb{P}(A_k) = k^{-(1+\\epsilon)}$. Since $\\sum k^{-(1+\\epsilon)} < \\infty$, BC1 proves such runs occur only FINITELY many times.",
        "<strong>Case 2 ($L_k = (1-\\epsilon)\\log_2 k$):</strong> $\\mathbb{P}(A_k) = k^{-(1-\\epsilon)}$. Since $\\sum k^{-(1-\\epsilon)} = \\infty$, BC2 proves such runs occur INFINITELY OFTEN. Thus longest run length in $n$ tosses is $\\approx \\log_2 n$ almost surely!"
    ],
    r"$$\sum_{k=1}^\infty 2^{-L_k} < \infty \implies \text{finitely often}; \qquad \sum_{k=1}^\infty 2^{-L_k} = \infty \implies \text{infinitely often (a.s.)}$$",
    "Winning streaks in casino games: in an infinite lifetime of fair betting, you will encounter winning streaks of length log₂(n) infinitely many times, but streaks exceeding (1+ε) log₂(n) will permanently vanish.",
    "Selecting overlapping blocks and applying BC2! Overlapping blocks are correlated, violating the independence mandate of BC2. Non-overlapping partitioning restores independence."
))

# ==============================================================================
# TOPIC 17: LAWS OF LARGE NUMBERS (WLLN & SLLN) (31701 - 31706)
# ==============================================================================

# Card 31701: The Weak Law of Large Numbers (WLLN)
svg_31701 = [
    AX(24, 115, 220, 20),
    # Tightening distribution of sample mean X̄_n as n grows
    P("M 30,114 Q 80,114 125,70 Q 170,114 220,114", fill="none", w=1.2, dash="3 3"),
    P("M 70,114 Q 100,114 125,40 Q 150,114 180,114", fill="none", w=1.6),
    P("M 100,114 Q 115,114 125,20 Q 135,114 150,114", fill="none", w=2.2),
    L(125, 20, 125, 114, 1.0, d="2 2"),
    N(125, 126, "μ", 9.5, w="bold"),
    N(175, 45, "Var(X̄_n) = σ² / n → 0", 8, w="bold"),
    N(120, 138, "WLLN: P(|X̄_n - μ| ≥ ε) ≤ σ² / (n ε²) → 0 proves convergence in probability", 8.5)
]
CARDS.append(make_stoma_card(
    17, 1, "WLLN",
    "The Weak Law of Large Numbers: Dispersion Collapse",
    svg_31701,
    "The variance of the sample mean shrinks as σ²/n; Chebyshev’s inequality proves convergence in probability to μ",
    [
        "<strong>Theorem Statement:</strong> For i.i.d. $X_i$ with mean $\\mu$ and finite variance $\\sigma^2$, sample mean $\\bar{X}_n = \\frac{1}{n}\\sum_{i=1}^n X_i$ satisfies $\\bar{X}_n \\xrightarrow{P} \\mu$: for all $\\epsilon > 0$, $\\lim_{n \\to \\infty} \\mathbb{P}(|\\bar{X}_n - \\mu| \\ge \\epsilon) = 0$.",
        "<strong>Chebyshev Proof:</strong> $\\mathbb{E}[\\bar{X}_n] = \\mu$ and $\\operatorname{Var}(\\bar{X}_n) = \\frac{\\sigma^2}{n}$. By Chebyshev, $\\mathbb{P}(|\\bar{X}_n - \\mu| \\ge \\epsilon) \\le \\frac{\\operatorname{Var}(\\bar{X}_n)}{\\epsilon^2} = \\frac{\\sigma^2}{n\\epsilon^2} \\to 0$.",
        "<strong>Relaxation:</strong> Finite variance is not necessary! Khinchin's WLLN requires ONLY $\\mathbb{E}[|X|] < \\infty$ (proved via characteristic functions)."
    ],
    r"$$\bar{X}_n = \frac{1}{n}\sum_{i=1}^n X_i \xrightarrow{P} \mu, \qquad \mathbb{P}\left(|\bar{X}_n - \mu| \ge \epsilon\right) \le \frac{\sigma^2}{n\epsilon^2} \to 0$$",
    "A pollster averaging 1,000 voter responses: the average response has sampling error variance 1,000 times smaller than any single respondent's volatility.",
    "Believing WLLN guarantees paths settle down without wild fluctuations. WLLN guarantees only that at step n, error is unlikely; it does NOT preclude infinite future deviations at later times!"
))

# Card 31702: The Strong Law of Large Numbers (SLLN)
svg_31702 = [
    # Tube [μ - ε, μ + ε] around mean
    AX(24, 115, 220, 20),
    L(24, 55, 215, 55, 1.0, d="2 2"), N(205, 50, "μ + ε", 7.5),
    L(24, 85, 215, 85, 1.0, d="2 2"), N(205, 95, "μ - ε", 7.5),
    L(24, 70, 215, 70, 1.2), N(205, 70, "μ", 8, w="bold"),
    # Sample path wandering and then permanently trapped in tube
    P("M 24,100 Q 50,30 80,80 Q 110,65 140,73 L 215,70", fill="none", w=1.8),
    N(120, 35, "Trajectory enters tube and NEVER leaves!", 8.5, w="bold"),
    N(120, 138, "SLLN: P(lim_{n → ∞} X̄_n = μ) = 1 guarantees 100% of sample paths converge to μ", 8.5)
]
CARDS.append(make_stoma_card(
    17, 2, "SLLN",
    "The Strong Law of Large Numbers: Pathwise Certainty",
    svg_31702,
    "The Strong Law guarantees that 100% of actual sample trajectories permanently converge to the true mean μ",
    [
        "<strong>Theorem Statement (Kolmogorov):</strong> Let $X_1, X_2, \\dots$ be i.i.d. with $\\mathbb{E}[|X|] < \\infty$. Then $\\mathbb{P}\\left(\\lim_{n \\to \\infty} \\bar{X}_n = \\mu\\right) = 1$ (Almost Sure convergence).",
        "<strong>Trajectory Geometry:</strong> For almost every sample path $\\omega$, for ANY $\\epsilon > 0$, there exists an integer $N(\\omega)$ such that $|\\bar{X}_n(\\omega) - \\mu| < \\epsilon$ for ALL $n \\ge N(\\omega)$. The path enters the $\\epsilon$-tube and NEVER leaves.",
        "<strong>Fundamental Foundation:</strong> Justifies the frequentist definition of probability: empirical frequencies $\\frac{1}{n}\\sum \\mathbf{1}_{A}$ converge almost surely to true probability $\\mathbb{P}(A)$."
    ],
    r"$$\mathbb{P}\left(\lim_{n \to \infty} \frac{1}{n}\sum_{i=1}^n X_i = \mu\right) = 1 \iff \mathbb{E}[|X|] < \infty$$",
    "Casino house edge: occasional lucky gamblers win on single days, but over millions of cumulative bets, the casino's average profit per game converges with 100% mathematical certainty to the house edge.",
    "Confusing WLLN with SLLN! WLLN is a snapshot statement (prob at time n); SLLN is a full-path statement (the entire future trajectory never strays)."
))

# Card 31703: 4th Moment Proof of SLLN via BC1
svg_31703 = [
    box(16, 20, 208, 44, "Step 1: Assume E[X⁴] < ∞\nExpand E[ (∑ (Xᵢ - μ))⁴ ] = n E[(X-μ)⁴] + 3n(n-1) (E[(X-μ)²])² ≤ C n²\n⇒ E[ (X̄_n - μ)⁴ ] ≤ C / n²", "#ffffff", 7.5),
    box(16, 68, 208, 44, "Step 2: Markov on 4th Power + Borel-Cantelli 1:\nP(|X̄_n - μ| ≥ ε) ≤ E[(X̄_n - μ)⁴] / ε⁴ ≤ C / (n² ε⁴)\nSum converges: ∑_{n=1}^∞ 1/n² < ∞ ⇒ X̄_n →^{a.s.} μ !", "#f8fafc", 7.5),
    N(120, 138, "4th moment power gives 1/n² decay; summability unlocks Borel-Cantelli 1 to prove SLLN", 8)
]
CARDS.append(make_stoma_card(
    17, 3, "SLLN 4TH MOMENT PROOF",
    "The 4th Moment Proof of the Strong Law via BC1",
    svg_31703,
    "Assuming E[X⁴] < ∞ achieves O(1/n²) variance decay, whose summability unlocks Borel-Cantelli 1",
    [
        "<strong>4th Moment Expansion:</strong> Assume $\\mathbb{E}[X^4] < \\infty$ and $\\mu = 0$. $\\mathbb{E}[(\\sum X_i)^4] = \\sum \\mathbb{E}[X_i^4] + 6\\sum_{i < j} \\mathbb{E}[X_i^2 X_j^2] = n \\mathbb{E}[X^4] + 3n(n-1)\\sigma^4 \\le C n^2$.",
        "<strong>Fourth Power Decay:</strong> $\\mathbb{E}[(\\bar{X}_n)^4] = \\frac{1}{n^4} \\mathbb{E}[(\\sum X_i)^4] \\le \\frac{C n^2}{n^4} = \\frac{C}{n^2}$.",
        "<strong>Summability via BC1:</strong> By Markov, $\\mathbb{P}(|\\bar{X}_n| \\ge \\epsilon) \\le \\frac{\\mathbb{E}[(\\bar{X}_n)^4]}{\\epsilon^4} \\le \\frac{C}{n^2 \\epsilon^4}$. Since $\\sum_{n=1}^\\infty \\frac{1}{n^2} = \\frac{\\pi^2}{6} < \\infty$, BC1 proves $\\bar{X}_n \\xrightarrow{a.s.} 0$!"
    ],
    r"$$\mathbb{E}\left[(\bar{X}_n - \mu)^4\right] \le \frac{C}{n^2} \implies \sum_{n=1}^\infty \mathbb{P}\left(|\bar{X}_n - \mu| \ge \epsilon\right) \le \sum_{n=1}^\infty \frac{C}{n^2 \epsilon^4} < \infty \implies \bar{X}_n \xrightarrow{\text{a.s.}} \mu$$",
    "Accelerating brake pad: 2nd moment gives 1/n decay (harmonic series diverges, no BC1); 4th moment gives 1/n² decay (quadratic series converges, unlocking BC1).",
    "Chebyshev gives 1/n decay: ∑ 1/n = ∞ (diverges), which CANNOT be plugged into BC1! The 4th moment is essential to force the series to converge."
))

# Card 31704: Kolmogorov’s SLLN & The Truncation Method
svg_31704 = [
    box(20, 20, 200, 42, "Kolmogorov's Sharp SLLN Criterion:\nXᵢ i.i.d. ⇒ X̄_n →^{a.s.} μ  IF AND ONLY IF  E[|X|] < ∞\n(Requires NO variance; first moment is necessary and sufficient)", "#ffffff", 8),
    box(20, 68, 200, 44, "The Truncation Method:\nDefine Yₙ = Xₙ · 1_{|Xₙ| ≤ n}  (Truncate at n)\n(1) P(Xₙ ≠ Yₙ i.o.) = 0 via BC1 since ∑ P(|X| > n) ≤ E[|X|] < ∞\n(2) Apply Kolmogorov's Maximal Inequality to Yₙ", "#f8fafc", 7),
    N(120, 138, "Kolmogorov's truncation removes extreme tails, proving SLLN with zero variance assumptions", 8)
]
CARDS.append(make_stoma_card(
    17, 4, "KOLMOGOROV SLLN",
    "Kolmogorov’s Sharp SLLN & The Truncation Technique",
    svg_31704,
    "Finite expectation E[|X|] < ∞ is both necessary and sufficient for the Strong Law to hold",
    [
        "<strong>Sharpest Condition:</strong> For i.i.d. $X_i$, $\\bar{X}_n \\xrightarrow{a.s.} \\mu$ IF AND ONLY IF $\\mathbb{E}[|X|] < \\infty$. Finite variance is NOT required!",
        "<strong>Truncation Idea:</strong> Define $Y_n = X_n \\mathbf{1}_{\\{|X_n| \\le n\\}}$. The tails satisfy $\\sum_{n=1}^\\infty \\mathbb{P}(X_n \\ne Y_n) = \\sum_{n=1}^\\infty \\mathbb{P}(|X| > n) \\le \\mathbb{E}[|X|] < \\infty$.",
        "<strong>Equivalence via BC1:</strong> By BC1, $X_n = Y_n$ for all but finitely many $n$ almost surely! Thus $\\bar{X}_n$ and $\\bar{Y}_n$ have identical asymptotic limits."
    ],
    r"$$\bar{X}_n \xrightarrow{\text{a.s.}} \mu \iff \mathbb{E}[|X|] < \infty, \qquad Y_n = X_n\,\mathbf{1}_{\{|X_n| \le n\}} \implies \sum_{n=1}^\infty \mathbb{P}(X_n \ne Y_n) \le \mathbb{E}[|X|] < \infty$$",
    "Filtering rare black swans: trimming off the extreme rare tail above n creates a well-behaved sequence Yₙ, while BC1 proves you only trimmed finitely many observations.",
    "Assuming variance is required for SLLN. Kolmogorov proved that E[|X|] < ∞ alone suffices; distributions with infinite variance (e.g. Pareto with 1 < α ≤ 2) still satisfy SLLN!"
))

# Card 31705: Geometry Comparison: WLLN vs SLLN
svg_31705 = [
    # Top: WLLN vertical slice
    box(20, 20, 96, 44, "WLLN (Snapshot):\nP(|X̄_n - μ| ≥ ε) → 0\nChecks only step n\n(Can escape at n+1)", "#ffffff", 7.5),
    # Bottom: SLLN whole path
    box(124, 20, 96, 44, "SLLN (Whole path):\nP(⋃_{k=n}^∞ {|X̄_k-μ|≥ε}) → 0\nChecks ALL future k ≥ n\n(Trapped forever!)", "#e2e8f0", 7.5),
    # Visual comparison
    L(20, 90, 220, 90, 1.4),
    N(20, 100, "n", 8), N(120, 100, "k → ∞", 8),
    P("M 20,90 Q 70,70 120,88 L 220,90", fill="none", w=1.8),
    N(120, 138, "WLLN controls the vertical slice at n; SLLN controls the entire horizontal tail trajectory", 8)
]
CARDS.append(make_stoma_card(
    17, 5, "LAW COMPARISON",
    "Geometric Contrast: WLLN (Snapshots) vs SLLN (Trajectories)",
    svg_31705,
    "WLLN controls a single point in time; SLLN controls the entire infinite tail trajectory from step n onward",
    [
        "<strong>WLLN Condition:</strong> $\\lim_{n \\to \\infty} \\mathbb{P}(|\\bar{X}_n - \\mu| \\ge \\epsilon) = 0$. Evaluates probability at single vertical slice $n$.",
        "<strong>SLLN Condition:</strong> $\\lim_{n \\to \\infty} \\mathbb{P}\\left(\\bigcup_{k=n}^\\infty \\{|\\bar{X}_k - \\mu| \\ge \\epsilon\\}\\right) = 0$. Evaluates the probability of ANY departure across the entire infinite future $k \\ge n$.",
        "<strong>Strict Superiority:</strong> Because $\\mathbb{P}(|\\bar{X}_n - \\mu| \\ge \\epsilon) \\le \\mathbb{P}(\\bigcup_{k=n}^\\infty \\{|\\bar{X}_k - \\mu| \\ge \\epsilon\\})$, SLLN trivially implies WLLN."
    ],
    r"$$\text{WLLN}: \mathbb{P}(|\bar{X}_n - \mu| \ge \epsilon) \to 0, \qquad \text{SLLN}: \mathbb{P}\left(\bigcup_{k=n}^\infty \{|\bar{X}_k - \mu| \ge \epsilon\}\right) \to 0$$",
    "A missile guidance path: WLLN says the missile is near target at second 100 (but might veer off at second 101); SLLN guarantees the missile stays locked inside the target crosshair for all seconds t ≥ 100.",
    "Assuming WLLN implies SLLN. Variables can satisfy WLLN while oscillating violently out of the tube infinitely many times (e.g. typewriter sequence)."
))

# Card 31706: Worked Benchmark: Failure of LLN on Cauchy Variables
svg_31706 = [
    box(20, 20, 200, 42, "Cauchy Distribution: f(x) = \\frac{1}{π(1+x²)}\nCharacteristic Function: φ_X(t) = exp(-|t|)\nE[|X|] = ∞  (First moment fails to exist!)", "#ffffff", 8),
    box(20, 68, 200, 44, "Sample Mean of n i.i.d. Cauchy RVs:\nφ_{X̄_n}(t) = [φ_X(t/n)]ⁿ = [exp(-|t|/n)]ⁿ = exp(-|t|) = φ_X(t) !\n⇒ X̄_n has the EXACT SAME Cauchy distribution for ALL n!", "#f8fafc", 7.5),
    N(120, 138, "Cauchy fails LLN completely: averaging n Cauchy variables provides ZERO noise reduction!", 8)
]
CARDS.append(make_stoma_card(
    17, 6, "WORKED BENCHMARK",
    "Worked Benchmark: Catastrophic Failure of the Law of Large Numbers (Cauchy)",
    svg_31706,
    "The sample mean of n independent Cauchy variables is identical to a single Cauchy variable; averaging provides zero gain",
    [
        "<strong>Problem Setup:</strong> Let $X_1, \\dots, X_n \\stackrel{\\text{i.i.d.}}{\\sim} \\text{Cauchy}(0, 1)$ with density $f(x) = \\frac{1}{\\pi(1+x^2)}$. Its characteristic function is $\\phi_X(t) = e^{-|t|}$. First moment $\\mathbb{E}[|X|] = \\infty$.",
        "<strong>Sample Mean Characteristic Function:</strong> $\\phi_{\\bar{X}_n}(t) = [\\phi_X(t/n)]^n = [e^{-|t|/n}]^n = e^{-|t|} = \\phi_X(t)$!",
        "<strong>Zero Averaging Gain:</strong> The sample mean $\\bar{X}_n$ is identically distributed to $X_1$ for every $n$. Averaging 1,000,000 Cauchy variables does NOT concentrate around 0; both WLLN and SLLN fail completely!"
    ],
    r"$$\phi_{\bar{X}_n}(t) = \left[\exp\left(-\frac{|t|}{n}\right)\right]^n = \exp(-|t|) \implies \bar{X}_n \stackrel{d}{=} X_1 \quad \forall n \ge 1$$",
    "A broken clock whose error doubles with every tick: averaging multiple readings produces a result just as wildly erratic as a single glance.",
    "Attempting to apply LLN to Cauchy distributions because the PDF looks symmetric! Symmetry is irrelevant when the tail integral ∫ |x| f(x)dx diverges to infinity."
))

# Save cards to cards_stoma.js
save_stoma_cards(CARDS)
print(f"Successfully generated {len(CARDS)} cards for StoMA Topics 16 & 17!")
