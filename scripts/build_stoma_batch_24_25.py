"""Build StoMA Topics 24 & 25 (Cards 32401 to 32506).
Dual-coding photographic plates with pure black-and-white vector diagrams.
"""
import sys, os
sys.path.append(os.path.dirname(__file__))
from stoma_lib import (
    T, N, L, V, P, C, R, E, PG, AX, box, svg, make_stoma_card, save_stoma_cards
)

CARDS = []

# ==============================================================================
# TOPIC 24: POISSON PROCESSES: PROPERTIES & EXTENSIONS (32401 - 32406)
# ==============================================================================

# Card 32401: Axiomatic Formulations & Small-o Increments
svg_32401 = [
    # Timeline with small intervals
    L(20, 70, 220, 70, 1.8, ar=True), N(225, 70, "t", 8),
    # Infinitesimal interval [t, t+h]
    L(100, 60, 100, 80, 1.4), L(140, 60, 140, 80, 1.4),
    R(100, 62, 40, 16, "#f1f5f9", 1.2),
    N(120, 52, "Interval h", 7.5),
    # Event occurrence in interval
    C(120, 70, 3, fill="#000000"),
    # Probability annotations
    N(120, 92, "P(1 event) = λh + o(h)", 7.5, w="bold"),
    N(120, 104, "P(≥2 events) = o(h)", 7),
    # Poisson law box
    box(20, 15, 95, 34, "Poisson Law:\nP(N(t) = k) = (λt)^k e^{-λt} / k!\nIndependent Increments", "#ffffff", 7),
    N(120, 138, "Poisson process: small-o axioms guarantee discrete point arrivals at constant average rate λ", 8.5)
]
CARDS.append(make_stoma_card(
    24, 1, "POISSON AXIOMS",
    "Axiomatic Formulations & Small-o Increments",
    svg_32401,
    "The Poisson counting process emerges from independent increments with small-o infinitesimal transition probabilities",
    [
        "<strong>Small-$o$ Axiomatic Definition:</strong> A counting process $\{N(t), t \\ge 0\}$ with $N(0)=0$ and independent increments is a Poisson process with rate $\\lambda > 0$ if: (1) $P(N(t+h) - N(t) = 1) = \\lambda h + o(h)$; (2) $P(N(t+h) - N(t) \\ge 2) = o(h)$; and (3) increments are stationary.",
        "<strong>Counting Distribution:</strong> Solving the Kolmogorov differential equation system yields the exact Poisson probability mass function for interval length $t$: $P(N(t+s) - N(s) = k) = \\frac{(\\lambda t)^k e^{-\\lambda t}}{k!}$ with $\\mathbb{E}[N(t)] = \\operatorname{Var}(N(t)) = \\lambda t$.",
        "<strong>Pure Jump Structure:</strong> Sample paths $t \\mapsto N(t)$ are non-decreasing step functions that start at 0, increase only by unit jumps of size $+1$ almost surely, and are right-continuous with left limits (cadlag)."
    ],
    r"$$P(N(t+h) - N(t) = 1) = \lambda h + o(h), \quad P(N(t) = k) = \frac{(\lambda t)^k e^{-\lambda t}}{k!}, \quad \mathbb{E}[N(t)] = \operatorname{Var}(N(t)) = \lambda t$$",
    "Geiger counter radiation clicks: radioactive atomic nuclei decay completely independently at microscopic rate λ, producing discrete clicks over time.",
    "Assuming P(N(t)=k) depends on absolute time s! Stationarity ensures the count distribution in (s, s+t] depends *only* on interval duration t, completely independent of starting timestamp s."
))

# Card 32402: Inter-Arrival & Waiting Time Distributions
svg_32402 = [
    # Timeline with arrivals S_1, S_2, S_3
    L(20, 80, 220, 80, 1.8, ar=True), N(225, 80, "t", 8),
    C(60, 80, 3, fill="#000000"), N(60, 92, "S_1", 8, w="bold"),
    C(110, 80, 3, fill="#000000"), N(110, 92, "S_2", 8, w="bold"),
    C(180, 80, 3, fill="#000000"), N(180, 92, "S_3", 8, w="bold"),

    # Inter-arrival spans T_1, T_2, T_3
    L(20, 68, 60, 68, 1.2), N(40, 62, "T_1 ~ Exp(λ)", 7),
    L(60, 68, 110, 68, 1.2), N(85, 62, "T_2 ~ Exp(λ)", 7),
    L(110, 68, 180, 68, 1.2), N(145, 62, "T_3 ~ Exp(λ)", 7),

    # Waiting time Gamma curve on top
    box(25, 12, 100, 35, "Arrival Time:\nS_n = Σ_{i=1}^n T_i ~ Gamma(n, λ)\nf_{S_n}(t) = λ^n t^{n-1} e^{-λt} / (n-1)!", "#f8fafc", 7),
    # Duality note
    box(135, 12, 85, 35, "Counting-Time Duality:\n{N(t) ≥ n}  ⟺  {S_n ≤ t}", "#f1f5f9", 7.5, bold=True),
    N(120, 138, "Inter-arrival times are i.i.d. Exp(λ); waiting times S_n follow Gamma(n, λ) via counting-time duality", 8.5)
]
CARDS.append(make_stoma_card(
    24, 2, "ARRIVAL TIMES",
    "Inter-Arrival & Waiting Time Distributions",
    svg_32402,
    "Inter-arrival times are memoryless i.i.d. Exp(λ), while waiting times S_n sum to Gamma(n, λ) distributions",
    [
        "<strong>Independent Exponential Spacings:</strong> The inter-arrival times $T_k = S_k - S_{k-1}$ are independent and identically distributed exponential random variables: $T_k \\stackrel{\\text{i.i.d.}}{\\sim} \\text{Exp}(\\lambda)$ with density $f_T(t) = \\lambda e^{-\\lambda t}$ and mean $\\mathbb{E}[T_k] = 1/\\lambda$.",
        "<strong>Gamma Waiting Times:</strong> The arrival timestamp of the $n$-th event is the sum of $n$ i.i.d. exponentials: $S_n = \\sum_{k=1}^n T_k \\sim \\text{Gamma}(n, \\lambda)$ (Erlang distribution) with density $f_{S_n}(t) = \\frac{\\lambda^n t^{n-1} e^{-\\lambda t}}{(n-1)!}$ and mean $\\mathbb{E}[S_n] = n/\\lambda$.",
        "<strong>Counting-Time Duality:</strong> The fundamental event equivalence connects the discrete counting process and continuous arrival times: $\\{N(t) \\ge n\\} \\iff \\{S_n \\le t\\}$, converting tail probabilities between Poisson and Gamma distributions."
    ],
    r"$$T_k \stackrel{\text{i.i.d.}}{\sim} \text{Exp}(\lambda), \quad S_n = \sum_{k=1}^n T_k \sim \text{Gamma}(n, \lambda), \quad P(N(t) \ge n) = P(S_n \le t)$$",
    "Call center customer queue: individual wait times between successive incoming calls are memoryless exponentials, while the wait for the 10th call follows a predictable Erlang curve.",
    "Confusing rate parameter λ with scale parameter β = 1/λ! In StoMA and engineering, Exp(λ) denotes rate λ with mean 1/λ and density λ e^{-λt}, not mean λ!"
))

# Card 32403: The Order Statistics Property & Uniform Conditioning
svg_32403 = [
    # Interval [0, t]
    L(25, 75, 215, 75, 1.8),
    C(25, 75, 4, fill="#000000"), N(25, 88, "0", 8),
    C(215, 75, 4, fill="#000000"), N(215, 88, "t", 8),
    # Conditioned arrival marks
    C(65, 75, 3, fill="#000000"), N(65, 63, "S_1", 8),
    C(115, 75, 3, fill="#000000"), N(115, 63, "S_2", 8),
    C(175, 75, 3, fill="#000000"), N(175, 63, "S_3", 8),
    # Uniform density box
    box(25, 15, 190, 32, "Given N(t) = n, arrival times (S_1, ..., S_n)\n~ Order Statistics of n i.i.d. Uniform[0, t] variables\nJoint Density: f(s_1, ..., s_n | N(t)=n) = n! / t^n", "#f1f5f9", 7.5, bold=True),
    N(120, 115, "Expected arrival timestamp: E[S_k | N(t) = n] = k · t / (n + 1)", 8),
    N(120, 138, "Order statistics property: conditioning on N(t) = n uniformly scatters the n arrivals over [0, t]", 8.5)
]
CARDS.append(make_stoma_card(
    24, 3, "ORDER STATISTICS",
    "The Order Statistics Property & Uniform Conditioning",
    svg_32403,
    "Conditioned on N(t) = n, arrival times are jointly distributed as the order statistics of n i.i.d. Uniform[0, t] RVs",
    [
        "<strong>Uniform Order Statistics Theorem:</strong> Given that exactly $n$ arrivals occurred in $[0, t]$, the unordered arrival times $U_1, \\dots, U_n$ are mutually independent and identically distributed as $\\text{Uniform}[0, t]$. Consequently, $(S_1, \\dots, S_n)$ are the order statistics $U_{(1)} \\le \\dots \\le U_{(n)}$.",
        "<strong>Constant Joint Conditional Density:</strong> The joint conditional density is constant over the simplex $0 < s_1 < s_2 < \\dots < s_n < t$: $f_{S_1, \\dots, S_n \\mid N(t)=n}(s_1, \\dots, s_n) = \\frac{n!}{t^n}$, where $n!$ accounts for the permutations of unordered uniforms.",
        "<strong>Marginal Conditional Expectations:</strong> Using properties of uniform order statistics, the conditional expected arrival time of the $k$-th customer is evenly spaced: $\\mathbb{E}[S_k \\mid N(t) = n] = \\frac{k}{n+1} t$."
    ],
    r"$$f_{S_1, \dots, S_n \mid N(t) = n}(s_1, \dots, s_n) = \frac{n!}{t^n} \quad (0 < s_1 < \dots < s_n < t); \quad \mathbb{E}[S_k \mid N(t) = n] = \frac{k}{n+1}t$$",
    "Raindrops on a sidewalk: given that exactly 10 drops fell on a slab during a 1-minute drizzle, each drop was equally likely to fall at any second, independently of the others.",
    "Assuming arrivals are uniformly spaced deterministically! Conditioned on N(t) = n, arrival times are *random* order statistics with expected spacing t/(n+1), NOT equally spaced grid points k·t/n!"
))

# Card 32404: Poisson Thinning & Superposition
svg_32404 = [
    # Top: Superposition (Merging)
    box(15, 18, 55, 22, "N_1 ~ PP(λ_1)", "#ffffff", 7),
    V(70, 29, 95, 38, 1.4),
    box(15, 44, 55, 22, "N_2 ~ PP(λ_2)", "#ffffff", 7),
    V(70, 55, 95, 46, 1.4),
    box(95, 28, 65, 30, "Merge: N_1 + N_2\n~ PP(λ_1 + λ_2)", "#f1f5f9", 7.5, bold=True),

    # Bottom: Thinning (Splitting)
    box(15, 88, 60, 28, "Parent Process\nN ~ PP(λ)", "#f8fafc", 7.5),
    V(75, 98, 105, 88, 1.4), N(90, 86, "p", 7),
    box(105, 78, 65, 20, "N_kept ~ PP(λp)", "#ffffff", 7),
    V(75, 106, 105, 116, 1.4), N(90, 118, "1-p", 7),
    box(105, 108, 65, 20, "N_drop ~ PP(λ(1-p))", "#ffffff", 7),

    # Independence highlight
    box(175, 85, 55, 40, "N_kept ⟂ N_drop\nINDEPENDENT!\n(Thinning)", "#f1f5f9", 6.8, bold=True),
    N(120, 138, "Thinning splits PP(λ) into independent PP(λp) and PP(λ(1-p)); merging sums independent rates", 8.5)
]
CARDS.append(make_stoma_card(
    24, 4, "THINNING & MERGING",
    "Poisson Thinning (Splitting) & Superposition (Merging)",
    svg_32404,
    "Poisson streams merge by rate addition; Bernoulli thinning splits a Poisson stream into independent Poisson sub-streams",
    [
        "<strong>Superposition (Merging):</strong> If $N_1(t)$ and $N_2(t)$ are independent Poisson processes with rates $\\lambda_1$ and $\\lambda_2$, their sum $N(t) = N_1(t) + N_2(t)$ is a Poisson process with aggregate rate $\\lambda = \\lambda_1 + \\lambda_2$.",
        "<strong>Bernoulli Thinning (Splitting):</strong> If each event of a Poisson process $N(t) \\sim \\text{PP}(\\lambda)$ is independently classified as Type 1 with probability $p$ and Type 2 with probability $1-p$, the resulting subprocesses $N_1(t)$ and $N_2(t)$ are Poisson processes with rates $\\lambda p$ and $\\lambda (1-p)$.",
        "<strong>Surprising Independence of Subprocesses:</strong> Remarkably, the split processes $N_1(t)$ and $N_2(t)$ are completely *independent* random variables for all $t$, despite both originating from the exact same parent process $N(t)$."
    ],
    r"$$\text{Merge: } N_1 + N_2 \sim \text{PP}(\lambda_1 + \lambda_2); \quad \text{Split: } N_1 \sim \text{PP}(\lambda p) \ \perp \ N_2 \sim \text{PP}(\lambda(1-p))$$",
    "Highway toll plaza traffic: merging cars from North and South ramps creates an aggregate Poisson stream; routing trucks to lane 1 and sedans to lane 2 produces independent streams.",
    "Assuming split streams N_1 and N_2 must be correlated because N_1 + N_2 = N! For a fixed total N=n, they are dependent Binomials. But when total count N is Poisson, the random total decouples them into strictly independent Poisson processes!"
))

# Card 32405: Non-Homogeneous Poisson Processes (NHPP)
svg_32405 = [
    # Time-varying rate curve λ(t)
    AX(25, 115, 215, 25),
    N(220, 115, "t", 8), N(20, 22, "λ(t)", 8),
    P("M 25,100 Q 60,100 80,45 Q 100,20 120,45 Q 150,110 215,80", fill="none", w=1.8),
    # Shaded area under curve
    P("M 40,115 L 40,100 Q 60,100 80,45 Q 100,20 120,45 L 120,115 Z", fill="#f1f5f9", w=1.0),
    N(80, 85, "m(t) = ∫_0^t λ(s)ds", 7.5, w="bold"),
    # NHPP increment law
    box(125, 20, 95, 34, "NHPP Increment Law:\nN(t+s) - N(s)\n~ Poisson(m(t+s) - m(s))", "#ffffff", 7),
    N(120, 138, "Non-homogeneous Poisson process: intensity λ(t) varies over time; count follows Poisson(m(t))", 8.5)
]
CARDS.append(make_stoma_card(
    24, 5, "NON-HOMOGENEOUS POISSON",
    "Non-Homogeneous Poisson Processes (NHPP)",
    svg_32405,
    "Time-varying arrival intensity λ(t) yields independent increments distributed as Poisson with mean m(t) = ∫ λ(s)ds",
    [
        "<strong>Time-Varying Intensity:</strong> An NHPP relaxes stationary increments by allowing instantaneous arrival rate $\\lambda(t) \\ge 0$ to vary with time: $P(N(t+h) - N(t) = 1) = \\lambda(t) h + o(h)$ with independent increments.",
        "<strong>Mean Value Function:</strong> The cumulative expected arrivals over $[0, t]$ is given by $m(t) = \\int_0^t \\lambda(s) ds$. The number of arrivals in any interval $(s, t]$ follows a Poisson distribution with mean $m(t) - m(s)$: $N(t) - N(s) \\sim \\text{Poisson}\\left(\\int_s^t \\lambda(u) du\\right)$.",
        "<strong>Time-Warping Equivalence:</strong> By transforming the time axis via $\\tau = m(t)$, any NHPP can be transformed into a standard homogeneous Poisson process of unit rate $\\lambda = 1$, enabling simulation via the inverse transform method."
    ],
    r"$$m(t) = \int_0^t \lambda(s) ds, \qquad N(t+s) - N(s) \sim \text{Poisson}(m(t+s) - m(s))$$",
    "Rush-hour coffee shop arrivals: customer arrival rate λ(t) surges during 8:00–9:00 AM and dies down at midday, governed by time-dependent intensity λ(t).",
    "Using exponential inter-arrival times for NHPP! Because rate λ(t) changes over time, inter-arrival intervals are *neither* identically distributed nor exponential. Only increments over fixed time windows remain Poisson."
))

# Card 32406: The Inspection Paradox & Renewal Intervals
svg_32406 = [
    # Timeline with uneven intervals
    L(20, 75, 220, 75, 1.8),
    C(35, 75, 3, fill="#000000"), N(35, 88, "L(t)", 7.5),
    C(195, 75, 3, fill="#000000"), N(195, 88, "A(t)", 7.5),
    # Fixed inspection point t
    L(120, 60, 120, 90, 1.8),
    C(120, 75, 3, fill="#000000"), N(120, 52, "Fixed Time t", 8, w="bold"),

    # Backward and forward spans
    L(35, 66, 120, 66, 1.2), N(75, 60, "B(t) (Spent)", 7),
    L(120, 66, 195, 66, 1.2), N(160, 60, "W(t) (Wait)", 7),

    # Paradox note
    box(25, 12, 190, 32, "Inspection Paradox (as t → ∞):\nE[W(t)] = 1/λ,  E[B(t)] = 1/λ\nE[Interval I(t)] = E[W(t) + B(t)] = 2/λ = 2 · E[T]!", "#f1f5f9", 7.5, bold=True),
    N(120, 138, "Inspection paradox: fixed time t lands preferentially in larger intervals, doubling expected interval length to 2/λ", 8.5)
]
CARDS.append(make_stoma_card(
    24, 6, "RENEWAL PARADOX",
    "The Inspection Paradox & Length-Biased Sampling",
    svg_32406,
    "A random observation time t falls disproportionately into longer renewal intervals, doubling expected interval length to 2/λ",
    [
        "<strong>Forward & Backward Recurrence Times:</strong> At fixed time $t$, let $W(t)$ be time until next arrival (forward recurrence) and $B(t)$ be time since last arrival (backward recurrence). By memorylessness, $W(t) \\sim \\text{Exp}(\\lambda)$ with $\\mathbb{E}[W(t)] = 1/\\lambda$, and as $t \\to \\infty$, $B(t) \\xrightarrow{d} \\text{Exp}(\\lambda)$.",
        "<strong>The Inspection Paradox:</strong> The total length of the renewal interval covering time $t$ is $I(t) = W(t) + B(t)$. Its asymptotic expectation is $\\mathbb{E}[I(t)] = \\frac{1}{\\lambda} + \\frac{1}{\\lambda} = \\frac{2}{\\lambda} = 2 \\mathbb{E}[T]$, exactly twice the average inter-arrival time!",
        "<strong>Length-Biased Sampling Mechanism:</strong> A randomly selected point $t$ is more likely to fall into an unusually wide inter-arrival gap than a narrow one, creating a length-biased sampling density $f_{\\text{observed}}(x) = \\frac{x f(x)}{\\mathbb{E}[T]} = \\lambda^2 x e^{-\\lambda x}$."
    ],
    r"$$\mathbb{E}[W(t)] = \frac{1}{\lambda}, \quad \mathbb{E}[B(t)] \to \frac{1}{\lambda} \implies \mathbb{E}[I(t)] = \mathbb{E}[W(t) + B(t)] \to \frac{2}{\lambda} = 2 \mathbb{E}[T]$$",
    "Waiting for the bus: commuters arriving at random moments wait 10 minutes on average even when buses run every 10 minutes, because they are more likely to arrive during 20-minute delayed gaps than 5-minute clustered gaps.",
    "Thinking E[W(t) + B(t)] must equal E[T]! An arrival chosen by fixed time t does NOT select an interval uniformly at random. It samples with probability proportional to interval duration x, producing the classic length-biased factor 2!"
))

# ==============================================================================
# TOPIC 25: RANDOM WALK, BROWNIAN MOTION & GAUSSIAN PROCESSES (32501 - 32506)
# ==============================================================================

# Card 32501: Pólya’s Random Walk Theorem
svg_32501 = [
    # 1D, 2D, 3D lattice panels
    R(16, 25, 64, 90, "#f8fafc", 1.4),
    N(48, 38, "1D: Z^1", 9, w="bold"),
    N(48, 55, "P_00^(2n) ~ 1/√n", 7.5),
    N(48, 70, "Σ 1/n^{1/2} = ∞", 7.5),
    N(48, 92, "RECURRENT!", 8, w="bold"),
    N(48, 105, "P(Return) = 1", 7),

    R(88, 25, 64, 90, "#f1f5f9", 1.4),
    N(120, 38, "2D: Z^2", 9, w="bold"),
    N(120, 55, "P_00^(2n) ~ 1/n", 7.5),
    N(120, 70, "Σ 1/n = ∞", 7.5),
    N(120, 92, "RECURRENT!", 8, w="bold"),
    N(120, 105, "P(Return) = 1", 7),

    R(160, 25, 64, 90, "#ffffff", 1.4),
    N(192, 38, "3D: Z^3", 9, w="bold"),
    N(192, 55, "P_00^(2n) ~ 1/n^{1.5}", 7.5),
    N(192, 70, "Σ 1/n^{3/2} < ∞", 7.5),
    N(192, 92, "TRANSIENT!", 8, w="bold"),
    N(192, 105, "P(Return) ≈ 0.34", 7),

    N(120, 138, "Pólya's Theorem: a drunk man (1D/2D) will always return home; a drunk bird (3D) gets lost forever", 8.5)
]
CARDS.append(make_stoma_card(
    25, 1, "POLYA'S THEOREM",
    "Pólya’s Random Walk Recurrence Theorem",
    svg_32501,
    "Simple symmetric random walks are recurrent in dimensions d=1, 2 but transient in dimensions d ≥ 3",
    [
        "<strong>Recurrence Criterion:</strong> By the Borel-Cantelli lemma, state 0 is recurrent if and only if the expected number of returns is infinite: $\\sum_{n=0}^\\infty P_{00}^{(2n)} = \\infty$.",
        "<strong>Dimensional Asymptotics:</strong> By the local central limit theorem, return probabilities scale as $P_{00}^{(2n)} \\sim C_d n^{-d/2}$. In 1D: $\\sum n^{-1/2} = \\infty$ (recurrent). In 2D: $\\sum n^{-1} = \\infty$ (recurrent). In 3D: $\\sum n^{-3/2} < \\infty$ converges, proving transience!",
        "<strong>Pólya's Escape Probability:</strong> On $\\mathbb{Z}^3$, the probability of ever returning to the origin is strictly less than 1: $f_{00} \\approx 0.3405$. A 3D walker escapes to infinity with probability $\\approx 65.95\\%$."
    ],
    r"$$\sum_{n=1}^\infty P_{00}^{(2n)} = \infty \iff d \in \{1, 2\} \ (\text{Recurrent}); \qquad \sum_{n=1}^\infty n^{-d/2} < \infty \iff d \ge 3 \ (\text{Transient})$$",
    "Kakutani's famous aphorism: 'A drunk man will find his way home, but a drunk bird may get lost forever.'",
    "Assuming 2D random walks return quickly because they are recurrent! The 2D return probability is 1, but expected return time μ_00 = ∞ (null recurrent); the walk wanders enormously before returning!"
))

# Card 32502: Standard Brownian Motion Axioms & Donsker’s Invariance
svg_32502 = [
    # Jagged Brownian path
    AX(25, 115, 215, 25),
    N(220, 115, "t", 8), N(20, 22, "B(t)", 8),
    P("M 25,70 L 35,60 L 45,75 L 55,50 L 65,65 L 75,40 L 85,55 L 95,30 L 105,45 L 115,25 L 125,50 L 135,35 L 145,60 L 155,45 L 165,70 L 175,55 L 185,85 L 195,70 L 205,95", fill="none", w=1.6),
    # Axiom summary box
    box(25, 12, 190, 32, "Standard Brownian Motion B(t):\n(1) B(0)=0; (2) Indep. Increments; (3) B(t)-B(s) ~ N(0, t-s)\nSample paths continuous everywhere, nowhere differentiable!", "#f1f5f9", 7.5, bold=True),
    N(120, 138, "Brownian motion: continuous limit of random walks via Donsker's Invariance Principle; jagged everywhere", 8.5)
]
CARDS.append(make_stoma_card(
    25, 2, "BROWNIAN MOTION",
    "Standard Brownian Motion Axioms & Donsker’s Invariance",
    svg_32502,
    "Brownian motion features independent stationary Gaussian increments, continuous paths, and nowhere differentiability",
    [
        "<strong>Axiomatic Characterization:</strong> Standard Brownian motion $\{B(t), t \\ge 0\}$ satisfies: (1) $B(0) = 0$ a.s.; (2) Independent increments; (3) Gaussian stationary increments: $B(t) - B(s) \\sim \\mathcal{N}(0, t-s)$ for $0 \\le s < t$; (4) Continuous sample paths almost surely.",
        "<strong>Donsker’s Invariance Principle:</strong> The scaled random walk $W^{(n)}(t) = \\frac{S_{\\lfloor nt \\rfloor}}{\\sigma \\sqrt{n}}$ converges weakly in distribution to standard Brownian motion $B(t)$ in Skorokhod space $D[0, T]$ as $n \\to \\infty$, universally for any zero-mean finite-variance step distribution.",
        "<strong>Nowhere Differentiability:</strong> As $\\Delta t \\to 0$, the difference quotient $\\frac{B(t+\\Delta t) - B(t)}{\\Delta t} \\sim \\mathcal{N}(0, 1/\\Delta t)$ explodes with variance $1/\\Delta t \\to \\infty$. Sample paths possess infinite velocity at every point and are nowhere differentiable."
    ],
    r"$$B(t) - B(s) \sim \mathcal{N}(0, t - s), \qquad \frac{S_{\lfloor nt \rfloor}}{\sqrt{n}} \xrightarrow{d} B(t), \qquad \lim_{\Delta t \to 0} \operatorname{Var}\left(\frac{\Delta B}{\Delta t}\right) = \infty$$",
    "Microscopic pollen grain jiggling in water: continuous impacts from millions of thermal molecules create erratic, non-smooth Brownian displacement.",
    "Treating Brownian motion paths as differentiable! In classical calculus, dB/dt does not exist as an ordinary function; treating it as such invalidates chain rules and requires Itô calculus!"
))

# Card 32503: Covariance Kernel & Self-Similarity Scaling
svg_32503 = [
    # Covariance 3D-like quadrant
    R(30, 25, 80, 80, "#f8fafc", 1.4),
    L(30, 105, 110, 25, 1.2, d="3 3"), # Diagonal s = t
    N(55, 45, "Cov = s (s < t)", 7.5),
    N(85, 80, "Cov = t (t < s)", 7.5),
    N(70, 118, "Cov(B(t), B(s)) = min(t, s)", 8, w="bold"),

    # Self similarity & Inversion formulas
    box(125, 25, 95, 38, "Self-Similarity Scaling:\nB(ct) =^{d} √c B(t)\nFractal Hurst H = 1/2", "#ffffff", 7.5),
    box(125, 70, 95, 38, "Time Inversion:\nt B(1/t) =^{d} B(t)\nValid BM on t > 0!", "#f1f5f9", 7.5),

    N(120, 138, "Covariance kernel Cov(B(t), B(s)) = min(t, s); invariant under diffusive scaling B(ct) =^{d} √c B(t)", 8.5)
]
CARDS.append(make_stoma_card(
    25, 3, "SCALING & COVARIANCE",
    "Brownian Covariance Kernel & Self-Similarity Scaling",
    svg_32503,
    "The covariance kernel is min(t, s), and Brownian paths exhibit exact fractal self-similarity scaling B(ct) =d √c B(t)",
    [
        "<strong>Covariance Kernel Derivation:</strong> For $s \\le t$, write $B(t) = B(s) + [B(t) - B(s)]$. Since the increment is independent of $B(s)$: $\\operatorname{Cov}(B(t), B(s)) = \\mathbb{E}[B(s)(B(s) + B(t) - B(s))] = \\mathbb{E}[B^2(s)] + 0 = s$. Thus $\\operatorname{Cov}(B(t), B(s)) = \\min(t, s)$.",
        "<strong>Diffusive Self-Similarity:</strong> For any scale $c > 0$, the scaled process $X(t) = \\frac{1}{\\sqrt{c}} B(ct)$ is also a standard Brownian motion: $B(ct) \\stackrel{d}{=} \\sqrt{c} B(t)$. Zooming into time by $c$ magnifies amplitude by $\\sqrt{c}$, confirming Hurst exponent $H = 1/2$.",
        "<strong>Time Inversion Invariance:</strong> The time-inverted process $Y(t) = t B(1/t)$ for $t > 0$ with $Y(0) = 0$ is a standard Brownian motion, establishing deep asymptotic connections between $t \\to 0$ and $t \\to \\infty$."
    ],
    r"$$\operatorname{Cov}(B(t), B(s)) = \min(t, s), \qquad B(ct) \stackrel{d}{=} \sqrt{c} B(t) \quad \forall c > 0, \qquad t B(1/t) \stackrel{d}{=} B(t)$$",
    "Zooming into a coastline: magnifying a Brownian path in time requires scaling amplitude by the square-root of time, maintaining identical statistical jaggedness.",
    "Assuming Cov(B(t), B(s)) = max(t, s) or s·t! For s < t, future innovations B(t) - B(s) are independent of past values, so only the shared past interval [0, s] contributes to covariance!"
))

# Card 32504: Quadratic Variation [B]_t = t & Itô Non-Differentiability
svg_32504 = [
    # Coordinate axes
    AX(25, 115, 215, 25),
    N(220, 115, "t", 8), N(20, 22, "V_2", 8),
    # Deterministic diagonal line [B]_t = t
    L(25, 115, 195, 30, 2.0),
    N(165, 45, "[B]_t = t (Deterministic!)", 8.5, w="bold"),
    # Fluctuating sums converging to line
    P("M 25,115 L 50,90 L 75,95 L 100,75 L 125,72 L 150,58 L 175,44 L 195,30", fill="none", w=1.2, dash="2 2"),
    # Core Itô rule box
    box(25, 15, 110, 26, "Fundamental Itô Rule:\n(dB)² = dt;  dB · dt = 0", "#f1f5f9", 8, bold=True),
    N(120, 138, "Quadratic variation: Σ (ΔB_i)² converges deterministically to t; total variation is infinite", 8.5)
]
CARDS.append(make_stoma_card(
    25, 4, "QUADRATIC VARIATION",
    "Quadratic Variation [B]_t = t & The Fundamental Itô Rule",
    svg_32504,
    "The sum of squared increments converges in mean square to deterministic t, giving rise to (dB)² = dt in Itô calculus",
    [
        "<strong>Quadratic Variation Theorem:</strong> For any partition $\\Pi_n = \\{0 = t_0 < \\dots < t_n = t\\}$ with mesh $\|\Pi_n\| \\to 0$, the quadratic variation converges in $L^2$ to the deterministic value $t$: $[B, B]_t = \\lim_{\\|\Pi_n\\| \\to 0} \\sum_{i=1}^n (B(t_i) - B(t_{i-1}))^2 = t$.",
        "<strong>Zero Asymptotic Variance:</strong> Because $\\Delta B_i \\sim \\mathcal{N}(0, \\Delta t_i)$, $\\operatorname{Var}((\\Delta B_i)^2) = 2(\\Delta t_i)^2$. The total variance $\\sum 2(\\Delta t_i)^2 \\le 2 \\|\\Pi\\| t \\to 0$, causing all random fluctuations to vanish completely in the limit.",
        "<strong>Infinite Total Variation:</strong> Since quadratic variation is finite and non-zero ($t > 0$), the first-order total variation $\\sum |\\Delta B_i|$ diverges to $\\infty$, necessitating the second-order Taylor correction $(dB)^2 = dt$ in Itô's formula."
    ],
    r"$$\lim_{\|\Pi\| \to 0} \sum_{i=1}^n (B(t_i) - B(t_{i-1}))^2 = t \quad \text{in } L^2 \implies (dB)^2 = dt, \quad dB \cdot dt = 0$$",
    "High-frequency stock tick counter: squaring thousands of tiny price wiggles adds up to an exact deterministic cumulative variance clock t.",
    "Applying ordinary chain rule d(f(B)) = f'(B) dB! Because (dB)² = dt ≠ 0, Itô's lemma requires the second-order term: df(B) = f'(B) dB + (1/2) f''(B) dt. Omitting (1/2)f'' dt is the most notorious error in stochastic calculus!"
))

# Card 32505: The Reflection Principle & Running Maximum
svg_32505 = [
    # Coordinate axes
    AX(25, 115, 215, 25),
    N(220, 115, "t", 8),
    # Threshold line a
    L(25, 55, 215, 55, 1.4, d="4 4"), N(200, 50, "Level a", 8, w="bold"),
    # Hitting time τ_a
    L(95, 55, 95, 115, 1.0, d="2 2"), N(95, 125, "τ_a", 8),
    C(95, 55, 3, fill="#000000"),
    # Original path: hits a and goes below
    P("M 25,115 Q 60,90 95,55 Q 120,40 150,75 T 205,95", fill="none", w=1.8),
    # Reflected path: reflected above line a
    P("M 95,55 Q 120,70 150,35 T 205,15", fill="none", w=1.4, dash="3 3"),
    N(180, 20, "Reflected Path", 7.5),
    # Formula box
    box(25, 12, 110, 26, "Reflection Principle:\nP(M(t) ≥ a) = 2 P(B(t) ≥ a)", "#f1f5f9", 7.5, bold=True),
    N(120, 138, "Reflection Principle: every path reaching a that drops below has an equally likely reflected counterpart above a", 8.5)
]
CARDS.append(make_stoma_card(
    25, 5, "REFLECTION PRINCIPLE",
    "The Reflection Principle & Running Maximum Law",
    svg_32505,
    "Reflecting Brownian paths after hitting threshold a doubles tail probability, yielding P(M(t) ≥ a) = 2 P(B(t) ≥ a)",
    [
        "<strong>Reflection Principle Argument:</strong> Let $M(t) = \\max_{0 \\le s \\le t} B(s)$ and $\\tau_a = \\inf\\{s: B(s) = a\\}$. Paths hitting $a$ before $t$ either end above $a$ or below $a$ at time $t$. By the strong Markov property and spatial symmetry at $\\tau_a$, both branches are equally likely, proving $P(M(t) \\ge a) = 2 P(B(t) \\ge a)$.",
        "<strong>Running Maximum Distribution:</strong> Because $B(t) \\sim \\mathcal{N}(0, t)$, the running maximum has CDF $P(M(t) \\le a) = 2\\Phi(a/\\sqrt{t}) - 1$, revealing that $M(t) \\stackrel{d}{=} |B(t)|$ has the folded half-normal distribution.",
        "<strong>Lévy First Passage Density:</strong> Differentiating $P(\\tau_a \\le t) = P(M(t) \\ge a)$ with respect to $t$ yields the heavy-tailed Lévy hitting-time density $f_{\\tau_a}(t) = \\frac{a}{\\sqrt{2\\pi t^3}} e^{-a^2/(2t)}$ with infinite expected hitting time $\\mathbb{E}[\\tau_a] = \\infty$."
    ],
    r"$$P(M(t) \ge a) = 2 P(B(t) \ge a) = 2\left(1 - \Phi\left(\frac{a}{\sqrt{t}}\right)\right); \quad f_{\tau_a}(t) = \frac{a}{\sqrt{2\pi t^3}} e^{-a^2/(2t)}$$",
    "Mirror symmetry in optics: light striking a mirror at angle θ bounces off with equal probability at -θ; Brownian motion restarted at level a bounces symmetrically upward or downward.",
    "Assuming E[τ_a] is finite because P(τ_a < ∞) = 1! Although standard Brownian motion is guaranteed to hit level a eventually with probability 1, the heavy tail t^{-3/2} causes the expected wait time E[τ_a] to diverge to infinity!"
))

# Card 32506: Gaussian Process Regression & Kernels
svg_32506 = [
    # GP regression confidence envelope
    AX(25, 115, 215, 25),
    N(220, 115, "x", 8), N(20, 22, "y", 8),
    # Shaded confidence band (narrow near data, wide far)
    PG("25,45 60,65 90,45 140,25 180,50 215,20 215,70 180,95 140,85 90,95 60,85 25,105", fill="#f1f5f9", w=1.0),
    # Fitted posterior mean line
    P("M 25,75 Q 60,75 90,70 Q 140,55 180,72 T 215,45", fill="none", w=2.0),
    # Training data points
    C(60, 75, 4, fill="#000000"), C(90, 70, 4, fill="#000000"), C(140, 55, 4, fill="#000000"), C(180, 72, 4, fill="#000000"),
    # Posterior formulas
    box(25, 12, 190, 28, "GP Posterior: f_* | X, y ~ N(μ_*, Σ_*)\nμ_* = K_*^T (K + σ²I)^{-1} y;   Σ_* = K_{**} - K_*^T (K + σ²I)^{-1} K_*", "#ffffff", 7),
    N(120, 138, "Gaussian Process regression: kernel K(x, x') defines smooth priors; posterior variance collapses near observations", 8.5)
]
CARDS.append(make_stoma_card(
    25, 6, "GAUSSIAN PROCESSES",
    "Gaussian Process Regression & The Kernel Matrix",
    svg_32506,
    "Gaussian processes define non-parametric Bayesian priors; conditioning collapses posterior variance near observed data points",
    [
        "<strong>Gaussian Process Definition:</strong> A collection of random variables $\\{f(x)\\}$ is a Gaussian Process $f(x) \\sim \\mathcal{GP}(m(x), K(x, x'))$ if every finite subset $(f(x_1), \\dots, f(x_n))$ has a joint multivariate Gaussian distribution.",
        "<strong>Closed-Form Posterior Conditioning:</strong> Given noisy training points $y = f(X) + \\epsilon$ with $\\epsilon \\sim \\mathcal{N}(0, \\sigma^2 I)$, the posterior distribution at test point $x_*$ is Gaussian $\\mathcal{N}(\\mu_*, \\Sigma_*)$ with analytical mean $\\mu_* = K_*^\\top (K + \\sigma^2 I)^{-1} y$ and variance $\\Sigma_* = K_{**} - K_*^\\top (K + \\sigma^2 I)^{-1} K_*$.",
        "<strong>Squared Exponential Kernel:</strong> The ubiquitous RBF kernel $K(x, x') = \\sigma_f^2 \\exp\\left(-\\frac{\|x - x'\|^2}{2\\ell^2}\\right)$ produces infinitely differentiable, smooth sample paths with characteristic length-scale $\\ell$ controlling function wiggliness."
    ],
    r"$$\mu_* = K_*^\top (K + \sigma^2 I)^{-1} y, \qquad \Sigma_* = K_{**} - K_*^\top (K + \sigma^2 I)^{-1} K_*, \qquad K(x, x') = \sigma_f^2 e^{-\frac{\|x-x'\|^2}{2\ell^2}}$$",
    "Flexible metal ruler spline: pinning the ruler at observed data points fixes the elevation, while regions between pins bend smoothly according to elastic tension governed by kernel K.",
    "Forgetting the noise variance regularization σ²I when inverting K! Without σ²I, near-collinear input points cause the kernel matrix K to become numerically singular, destabilizing the matrix inverse (K + σ²I)^{-1}!"
))

if __name__ == "__main__":
    save_stoma_cards(CARDS)
    print("Successfully generated 12 cards for StoMA Topics 24 & 25!")
