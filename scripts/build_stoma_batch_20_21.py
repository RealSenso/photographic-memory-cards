"""Build StoMA Topics 20 & 21 (Cards 32001 to 32106).
Dual-coding photographic plates with pure black-and-white vector diagrams.
"""
import sys, os
sys.path.append(os.path.dirname(__file__))
from stoma_lib import (
    T, N, L, V, P, C, R, E, PG, AX, box, svg, make_stoma_card, save_stoma_cards
)

CARDS = []

# ==============================================================================
# TOPIC 20: DTMC STATIONARY DISTRIBUTIONS & LIMITING BEHAVIOR (32001 - 32006)
# ==============================================================================

# Card 32001: Stationary Distribution π & Invariant Measure
svg_32001 = [
    # Left: input distribution vector π
    box(16, 45, 52, 38, "Vector π^T\n(π_1, ..., π_m)", "#ffffff", 8),
    # Arrow into Operator P
    V(68, 64, 98, 64, 1.8),
    # Center: Transition Matrix P
    box(98, 38, 48, 52, "Matrix P\n[P_ij]", "#f1f5f9", 8.5),
    # Arrow out to π
    V(146, 64, 176, 64, 1.8),
    # Right: output distribution vector π
    box(176, 45, 52, 38, "Vector π^T\nUnchanged!", "#ffffff", 8),
    # Mathematical identity below
    N(120, 110, "π^T P = π^T  ⟺  π_j = Σ_i π_i P_ij", 9, w="bold"),
    N(120, 126, "Left Eigenvector: Dominant Perron-Frobenius eigenvalue λ = 1", 7.5),
    N(120, 138, "Stationary distribution: if X_0 ~ π, then X_n ~ π for all n ≥ 1", 8.5)
]
CARDS.append(make_stoma_card(
    20, 1, "INVARIANT MEASURES",
    "Stationary Distribution π & Invariant Probability Measure",
    svg_32001,
    "The stationary distribution π satisfies π^T P = π^T: probability mass distributions remain preserved through state transitions",
    [
        "<strong>Invariant Probability Measure:</strong> A row probability vector $\\pi = (\\pi_i)_{i \\in S}$ is stationary if $\\pi^\\top P = \\pi^\\top$ with $\\pi_i \\ge 0$ and $\\sum_{i \\in S} \\pi_i = 1$. If initial state $X_0 \\sim \\pi$, then $X_n \\sim \\pi$ for all steps $n \\ge 1$ identically.",
        "<strong>Component-wise Inflow Balance:</strong> Expanding $\\pi^\\top P = \\pi^\\top$ yields $\\pi_j = \\sum_{i \\in S} \\pi_i P_{ij}$ for all states $j \\in S$. The stationary probability mass at state $j$ equals the aggregate probability flux entering $j$ from all predecessor states $i$ weighted by steady-state occupancies.",
        "<strong>Left Eigenvector Formulation:</strong> Mathematically, $\\pi^\\top$ is a normalized left eigenvector of transition matrix $P$ corresponding to the dominant Perron-Frobenius eigenvalue $\\lambda_1 = 1$, ensuring non-negativity and existence for finite stochastic matrices."
    ],
    r"$$\pi^\top P = \pi^\top, \quad \sum_{i \in S} \pi_i = 1, \quad \pi_j = \sum_{i \in S} \pi_i P_{ij} \quad \forall j \in S$$",
    "Steady-state fluid flow in closed pipe networks: whatever mass flows into junction j from upstream branches must match the mass residing at j.",
    "Confusing left vs right eigenvectors! π^T P = π^T is a *left* eigenvector equation. The trivial *right* eigenvector with eigenvalue 1 is the vector of all ones P 1 = 1, which represents row-stochasticity, not the stationary distribution!"
))

# Card 32002: The Fundamental Limit Theorem & Return Time Reciprocal
svg_32002 = [
    # Coordinate axes
    AX(24, 115, 220, 20),
    N(225, 115, "n", 8), N(20, 22, "P_ij^(n)", 8),
    # Trajectories converging to π_j
    P("M 25,35 Q 70,85 120,68 T 215,65", fill="none", w=1.5),
    P("M 25,100 Q 70,45 120,62 T 215,65", fill="none", w=1.5, dash="3 3"),
    P("M 25,75 Q 70,80 120,66 T 215,65", fill="none", w=1.2, dash="2 2"),
    # Asymptotic line π_j
    L(25, 65, 215, 65, 1.2, d="4 4"),
    C(215, 65, 3, fill="#000000"),
    N(180, 56, "Limit π_j = 1/μ_jj", 8.5, w="bold"),
    N(65, 28, "Start i=1", 7), N(65, 110, "Start i=2", 7),
    # Box explaining theorem
    box(24, 12, 105, 22, "Irreducible + Aperiodic\n+ Positive Recurrent", "#f1f5f9", 7.5),
    N(120, 138, "Fundamental Limit Theorem: P_ij^(n) → π_j = 1/E[τ_j | X_0 = j] independent of start state i", 8.5)
]
CARDS.append(make_stoma_card(
    20, 2, "LIMIT THEOREMS",
    "Fundamental Limit Theorem & Return Time Reciprocal",
    svg_32002,
    "Under irreducibility, positive recurrence, and aperiodicity, transition probabilities converge to π_j = 1/μ_jj regardless of initial state i",
    [
        "<strong>Convergence Theorem:</strong> For an irreducible, positive recurrent, and aperiodic DTMC, the $n$-step transition probabilities satisfy $\\lim_{n \\to \\infty} P_{ij}^{(n)} = \\pi_j > 0$ for all initial states $i$ and target states $j$. The asymptotic distribution is independent of starting state $X_0 = i$.",
        "<strong>Kac's Return Time Reciprocal:</strong> The unique invariant probability $\\pi_j$ is precisely the reciprocal of the expected first return time to state $j$: $\\pi_j = \\frac{1}{\\mu_{jj}} = \\frac{1}{\\mathbb{E}[\\tau_j \\mid X_0 = j]}$. Rare states with long expected return times have proportionally tiny steady-state probabilities.",
        "<strong>Coupling Proof Paradigm:</strong> The classical Doeblin coupling runs two independent chain copies $X_n, Y_n$ until they collide at stopping time $T = \\inf\\{n: X_n = Y_n\\}$, proving $|P_{ij}^{(n)} - \\pi_j| \\le P(T > n) \\to 0$ exponentially."
    ],
    r"$$\lim_{n \to \infty} P_{ij}^{(n)} = \pi_j = \frac{1}{\mu_{jj}} = \frac{1}{\mathbb{E}[\tau_j \mid X_0 = j]} > 0$$",
    "Bus stop headway paradox: a commuter waiting for bus route j finds the long-run visit fraction is 1/μ_jj where μ_jj is the average round-trip headway cycle.",
    "Applying the limit theorem to periodic chains! If the chain is bipartite or cyclic (period d > 1), P_ij^(n) does not converge as n → ∞ but oscillates indefinitely, even though a unique stationary distribution π exists!"
))

# Card 32003: Positive vs Null Recurrence & Transience
svg_32003 = [
    # Three regime boxes on a random walk
    R(16, 22, 64, 96, "#f8fafc", 1.4),
    N(48, 35, "p < 1/2", 9, w="bold"),
    N(48, 48, "Pos. Recurrent", 8, w="bold"),
    N(48, 65, "μ_00 < ∞", 8),
    N(48, 80, "π_i > 0", 8),
    N(48, 98, "Σ π_i = 1 (Exists)", 7.5),

    R(88, 22, 64, 96, "#f1f5f9", 1.4),
    N(120, 35, "p = 1/2", 9, w="bold"),
    N(120, 48, "Null Recurrent", 8, w="bold"),
    N(120, 65, "μ_00 = ∞", 8),
    N(120, 80, "f_00 = 1", 8),
    N(120, 98, "π_i = 1/∞ = 0", 7.5),

    R(160, 22, 64, 96, "#ffffff", 1.4),
    N(192, 35, "p > 1/2", 9, w="bold"),
    N(192, 48, "Transient", 8, w="bold"),
    N(192, 65, "f_00 < 1", 8),
    N(192, 80, "Drift to +∞", 8),
    N(192, 98, "Finite Visits", 7.5),

    N(120, 138, "Recurrence taxonomy: positive recurrent (finite μ_ii), null recurrent (infinite μ_ii), transient", 8.5)
]
CARDS.append(make_stoma_card(
    20, 3, "CLASSIFICATION OF STATES",
    "Positive vs Null Recurrence & Random Walk Drift",
    svg_32003,
    "Positive recurrence guarantees a normalizable stationary distribution; null recurrence has probability 1 return but infinite expected return time",
    [
        "<strong>Positive Recurrence Criteria:</strong> An irreducible chain is positive recurrent if and only if $\\mu_{ii} = \\mathbb{E}[\\tau_i \\mid X_0 = i] < \\infty$ for some (and hence all) states $i$. In this case and only this case, a valid normalized probability distribution $\\pi$ exists satisfying $\\sum \\pi_i = 1$.",
        "<strong>Null Recurrence & Mass Dispersion:</strong> A chain is null recurrent if return probability is 1 ($f_{ii} = 1$), but expected return time is infinite ($\\mu_{ii} = \\infty$). Stationary equations $\\pi^\\top P = \\pi^\\top$ have non-trivial non-negative solutions, but their sum is infinite, yielding zero probability $\\pi_i = 1/\\infty = 0$ upon normalization.",
        "<strong>Reflected Random Walk Benchmark:</strong> On $\\mathbb{Z}_+$ with $P_{i, i+1} = p$ and $P_{i, i-1} = 1-p$: positive recurrent if $p < 1/2$ (geometric stationary distribution); null recurrent if $p = 1/2$ (symmetric random walk wanders to infinity); transient if $p > 1/2$."
    ],
    r"$$\mu_{ii} < \infty \iff \text{Pos. Recurrent } (\sum \pi_i = 1); \quad \mu_{ii} = \infty \iff \text{Null Recurrent } (\pi_i \equiv 0)$$",
    "Diffusing gas in an infinite room: molecules return to the origin with probability 1 (recurrence), but take infinite expected time to do so (null recurrence), dissipating density to zero.",
    "Assuming recurrence implies existence of a stationary distribution! On infinite state spaces, symmetric random walks are recurrent (f_00 = 1) but possess NO stationary probability distribution because μ_00 = ∞."
))

# Card 32004: Cut Equations & Detailed Balance
svg_32004 = [
    # Partition cut diagram
    R(20, 20, 90, 95, "#f8fafc", 1.5, rx=8),
    N(65, 35, "Set A", 9, w="bold"),
    C(45, 60, 10, fill="#ffffff"), N(45, 63, "i_1", 8),
    C(75, 85, 10, fill="#ffffff"), N(75, 88, "i_2", 8),

    R(130, 20, 90, 95, "#f1f5f9", 1.5, rx=8),
    N(175, 35, "Set A^c", 9, w="bold"),
    C(155, 60, 10, fill="#ffffff"), N(155, 63, "j_1", 8),
    C(185, 85, 10, fill="#ffffff"), N(185, 88, "j_2", 8),

    # Cut line
    L(120, 15, 120, 120, 1.5, d="4 4"),
    N(120, 12, "CUT", 7.5, w="bold"),

    # Forward flux
    V(55, 60, 145, 60, 1.8),
    N(100, 52, "Σ_{i∈A, j∈A^c} π_i P_ij", 7.5),
    # Reverse flux
    V(145, 78, 55, 78, 1.8),
    N(100, 90, "Σ_{j∈A^c, i∈A} π_j P_ji", 7.5),

    N(120, 138, "Cut equations equate aggregate flux across any cut; detailed balance equates pairwise flows", 8.5)
]
CARDS.append(make_stoma_card(
    20, 4, "BALANCE EQUATIONS",
    "Cut Equations & Detailed Balance Equations",
    svg_32004,
    "Steady-state probability flux crossing any partition cut must balance; time-reversible chains satisfy pairwise detailed balance",
    [
        "<strong>Global Cut Conservation Law:</strong> For any partition of state space $S = A \\cup A^c$, the net steady-state probability flux leaving $A$ must equal the flux entering $A$: $\\sum_{i \\in A} \\sum_{j \\in A^c} \\pi_i P_{ij} = \\sum_{j \\in A^c} \\sum_{i \\in A} \\pi_j P_{ji}$. This generalizes component balance.",
        "<strong>Detailed Balance Condition:</strong> A distribution $\\pi$ satisfies detailed balance if $\\pi_i P_{ij} = \\pi_j P_{ji}$ for all pairs $i, j \\in S$. Any non-negative normalized solution to detailed balance automatically satisfies full balance $\\pi^\\top P = \\pi^\\top$, making the Markov chain time-reversible.",
        "<strong>Birth-Death Process Simplification:</strong> In birth-death chains (transitions only to adjacent neighbors $i \\pm 1$), cut equations between $\{0, \\dots, i\}$ and $\{i+1, \\dots\}$ reduce directly to pairwise detailed balance $\\pi_i P_{i, i+1} = \\pi_{i+1} P_{i+1, i}$, bypassing full matrix inversion."
    ],
    r"$$\sum_{i \in A, j \in A^c} \pi_i P_{ij} = \sum_{j \in A^c, i \in A} \pi_j P_{ji}; \quad \text{Detailed Balance: } \pi_i P_{ij} = \pi_j P_{ji} \implies \pi^\top P = \pi^\top$$",
    "Thermodynamic microscopic reversibility: in thermal equilibrium, every individual forward chemical reaction rate equals its reverse reaction rate.",
    "Thinking all Markov chains satisfy detailed balance! Detailed balance only holds for *reversible* chains (such as trees or birth-death chains). Unidirectional cyclic chains (1 → 2 → 3 → 1) satisfy global balance but violate detailed balance!"
))

# Card 32005: Periodic Chains & Cesàro Limits
svg_32005 = [
    # Top: 2-state periodic cycle
    C(50, 45, 14, fill="#f1f5f9"), N(50, 48, "0", 10, w="bold"),
    C(190, 45, 14, fill="#f1f5f9"), N(190, 48, "1", 10, w="bold"),
    P("M 64,40 C 100,20 140,20 176,40", fill="none", w=1.8, ar=True),
    N(120, 22, "P_01 = 1", 8),
    P("M 176,50 C 140,70 100,70 64,50", fill="none", w=1.8, ar=True),
    N(120, 72, "P_10 = 1", 8),

    # Bottom: Cesàro damping vs Oscillation
    AX(30, 122, 215, 80),
    # Oscillating sequence 0, 1, 0, 1
    P("M 35,122 L 55,85 L 75,122 L 95,85 L 115,122 L 135,85 L 155,122 L 175,85 L 195,122 L 210,85", fill="none", w=1.2, dash="2 2"),
    # Cesaro curve converging to 1/2
    P("M 35,122 Q 60,95 100,103 T 210,103", fill="none", w=2.0),
    L(30, 103, 215, 103, 1.0, d="3 3"),
    N(180, 98, "Cesàro Limit = 1/2", 8, w="bold"),
    N(120, 138, "Periodic DTMC: P^(n) oscillates forever, but Cesàro time-average (1/N) Σ P^(n) → π = (1/2, 1/2)", 8.5)
]
CARDS.append(make_stoma_card(
    20, 5, "PERIODICITY & ERGODICITY",
    "Periodic DTMCs & Cesàro Time-Average Convergence",
    svg_32005,
    "While periodic chains oscillate without a pointwise limit, their Cesàro time average converges unconditionally to π",
    [
        "<strong>Failure of Pointwise Limits:</strong> For an irreducible positive-recurrent chain with period $d > 1$, the state space partitions into cyclic classes $C_0, \\dots, C_{d-1}$. The sequence of transition probabilities $P_{ij}^{(n)}$ oscillates periodically and fails to converge to any single constant.",
        "<strong>Cesàro Limit Universality:</strong> Even when periodicity destroys the ordinary limit, the Cesàro time-average limit always exists and equals the unique stationary distribution: $\\lim_{N \\to \\infty} \\frac{1}{N} \\sum_{n=1}^N P_{ij}^{(n)} = \\pi_j$ for all states $i, j$.",
        "<strong>Stationary Vector Invariance:</strong> The stationary vector $\\pi$ satisfying $\\pi^\\top P = \\pi^\\top$ remains completely valid and unique for periodic positive recurrent chains; periodicity affects pathwise synchronization, not steady-state invariant measures."
    ],
    r"$$\lim_{N \to \infty} \frac{1}{N} \sum_{n=1}^N P_{ij}^{(n)} = \pi_j \quad (\text{holds for both periodic and aperiodic positive recurrent chains})$$",
    "Traffic light cycle: red and green states oscillate deterministically every 60 seconds (no point limit), yet the long-run fraction of time spent in red is exactly 1/2.",
    "Claiming a periodic chain has no stationary distribution! Periodicity only prevents pointwise convergence lim_{n → ∞} P_ij^(n); the stationary distribution π still exists and satisfies π^T P = π^T uniquely!"
))

# Card 32006: Ergodic Theorem for Markov Chains
svg_32006 = [
    # Trajectory of reward function
    AX(25, 115, 220, 20),
    N(225, 115, "N", 8), N(20, 22, "f(X_n)", 8),
    # Fluctuating path
    P("M 25,95 L 45,45 L 65,100 L 85,35 L 105,75 L 125,50 L 145,80 L 165,60 L 185,72 L 210,68", fill="none", w=1.2),
    # Running average curve
    P("M 25,95 Q 65,70 120,68 T 215,68", fill="none", w=2.0),
    # Horizontal line E_π[f]
    L(25, 68, 215, 68, 1.2, d="4 4"),
    N(175, 60, "E_π[f(X)] = Σ π_j f(j)", 8.5, w="bold"),
    box(25, 15, 110, 24, "Ergodic Equality (a.s.):\nTime Average = Space Average", "#f1f5f9", 7.5),
    N(120, 138, "Ergodic Theorem: (1/N) Σ_{n=1}^N f(X_n) → E_π[f(X)] almost surely for any bounded function f", 8.5)
]
CARDS.append(make_stoma_card(
    20, 6, "ERGODIC THEORY",
    "Ergodic Theorem & Strong Law for DTMCs",
    svg_32006,
    "The long-run time average along a single sample path converges almost surely to the stationary ensemble expectation",
    [
        "<strong>Strong Law for DTMCs:</strong> Let $\{X_n\}$ be an irreducible positive-recurrent Markov chain with stationary distribution $\\pi$. For any function $f: S \\to \\mathbb{R}$ with $\\sum_i |f(i)| \\pi_i < \\infty$, the sample path time average converges almost surely: $\\lim_{N \\to \\infty} \\frac{1}{N} \\sum_{n=1}^N f(X_n) = \\sum_{i \\in S} f(i) \\pi_i$.",
        "<strong>Occupancy Fraction Representation:</strong> Setting indicator reward $f(k) = \\mathbf{1}_{\\{k = j\\}}$, the Ergodic Theorem establishes that the empirical fraction of time spent in state $j$ converges almost surely to $\\pi_j$: $\\lim_{N \\to \\infty} \\frac{1}{N} \\sum_{n=1}^N \\mathbf{1}_{\\{X_n = j\\}} = \\pi_j$.",
        "<strong>Long-Run Cost Evaluation:</strong> In queuing and buffer engineering, long-run packet drop rates, average buffer occupancy $\\mathbb{E}[L]$, and operational running costs are computed directly via stationary expectations $\\sum_i f(i) \\pi_i$ without tracking transient distributions."
    ],
    r"$$\lim_{N \to \infty} \frac{1}{N} \sum_{n=1}^N f(X_n) = \sum_{j \in S} \pi_j f(j) = \mathbb{E}_\pi[f(X)] \quad \text{almost surely}$$",
    "Monte Carlo MCMC sampling: walking along a Markov chain trajectory and averaging sample outputs produces exact target ensemble expectations.",
    "Applying the Ergodic Theorem to reducible chains! If the chain has multiple communicating recurrent classes, the long-run average lim (1/N) Σ f(X_n) is a random variable dependent on which class the chain was absorbed into, not a single constant!"
))

# ==============================================================================
# TOPIC 21: ABSORPTION PROBABILITIES & MEAN HITTING TIMES (32101 - 32106)
# ==============================================================================

# Card 32101: First-Step Analysis for Absorption
svg_32101 = [
    # Center node i
    C(70, 70, 14, fill="#ffffff"), N(70, 73, "i", 10, w="bold"),
    # Outgoing branches
    V(82, 62, 130, 35, 1.8),
    N(102, 42, "P_{iA}", 8),
    box(132, 22, 60, 24, "Target A (a=1)", "#f8fafc", 8),

    V(84, 70, 130, 70, 1.8),
    N(105, 64, "P_ij", 8),
    C(142, 70, 12, fill="#f1f5f9"), N(142, 73, "j (a_j)", 8),

    V(82, 78, 130, 105, 1.8),
    N(102, 98, "P_{iB}", 8),
    box(132, 95, 60, 24, "Target B (a=0)", "#f8fafc", 8),

    # Balance formula
    box(15, 15, 80, 22, "a_i = Σ_j P_ij a_j", "#f1f5f9", 8.5),
    N(120, 138, "First-step analysis: decompose absorption probability by conditioning on the first step X_1", 8.5)
]
CARDS.append(make_stoma_card(
    21, 1, "ABSORPTION ANALYSIS",
    "First-Step Analysis for Absorption Probabilities",
    svg_32101,
    "Absorption probabilities satisfy linear first-step equations a_i = Σ_j P_ij a_j anchored by boundary target conditions",
    [
        "<strong>Total Probability Decomposition:</strong> To find absorption probability $a_i = P(\\tau_A < \\tau_B \\mid X_0 = i)$, condition on the very first jump $X_1 = j$. By the Markov property, the process restarts from state $j$, yielding linear balance $a_i = \\sum_{j \\in S} P_{ij} a_j$.",
        "<strong>Boundary Pinning Conditions:</strong> The linear system requires explicit boundary values: $a_i = 1$ for all target states $i \\in A$, and $a_i = 0$ for all competing absorbing states $i \\in B$. For transient states $i \\notin A \\cup B$, $a_i$ lies strictly in $(0, 1)$.",
        "<strong>Uniqueness via Maximum Principle:</strong> In finite state spaces where absorption occurs with probability 1 from all transient states, the linear system $(I - Q) a = R_A$ has a unique solution because all eigenvalues of sub-stochastic matrix $Q$ satisfy $|\\lambda| < 1$."
    ],
    r"$$a_i = \sum_{j \in S} P_{ij} a_j \quad (i \notin A \cup B), \quad a_i = 1 \ (i \in A), \quad a_i = 0 \ (i \in B)$$",
    "Branching game tree: calculating probability of winning a chess endgame by weighting winning probabilities of all immediate legal first moves.",
    "Forgetting to check boundary conditions! If boundary states a_i = 1 are omitted, the trivial all-zero vector a_i ≡ 0 solves the unconstrained system a = P a. Always specify boundary conditions on absorbing sets!"
))

# Card 32102: Mean Hitting Times & First-Step Systems
svg_32102 = [
    # State node i with clock +1 step
    C(60, 68, 14, fill="#ffffff"), N(60, 71, "i", 10, w="bold"),
    # Clock box "+1 step"
    box(20, 22, 60, 24, "Cost: +1 step", "#f1f5f9", 8, bold=True),
    L(50, 46, 55, 56, 1.2),

    # Transition arrows
    V(74, 58, 125, 40, 1.8),
    N(98, 44, "P_ij", 8),
    C(138, 38, 12, fill="#f1f5f9"), N(138, 41, "μ_j", 8.5),

    V(74, 78, 125, 95, 1.8),
    N(98, 92, "P_ik", 8),
    C(138, 98, 12, fill="#f1f5f9"), N(138, 101, "μ_k", 8.5),

    # Target A node
    box(170, 56, 56, 26, "Target A\nμ_A = 0", "#ffffff", 8),
    V(150, 42, 170, 62, 1.5, d="2 2"),
    V(150, 94, 170, 74, 1.5, d="2 2"),

    N(120, 138, "Mean hitting times: μ_i = 1 + Σ_{j ∉ A} P_ij μ_j for i ∉ A, with absorbing boundary μ_A = 0", 8.5)
]
CARDS.append(make_stoma_card(
    21, 2, "HITTING TIMES",
    "Mean Hitting Time First-Step Equations",
    svg_32102,
    "Mean hitting times accumulate a +1 cost for the initial step plus weighted downstream expectations: (I - Q) μ = 1",
    [
        "<strong>First-Step Time Accumulation:</strong> The expected hitting time to target set $A$, $\\mu_i = \\mathbb{E}[\\tau_A \\mid X_0 = i]$, satisfies $\\mu_i = 1 + \\sum_{j \\in S} P_{ij} \\mu_j$ for $i \\notin A$. The constant '$+1$' accounts for elapsed time of the initial transition step.",
        "<strong>Target Boundary Condition:</strong> By definition, if the chain begins already inside target set $A$, zero additional steps are required: $\\mu_i = 0$ for all $i \\in A$. This provides essential non-homogeneous anchoring for the linear equation system.",
        "<strong>Matrix Formulation:</strong> In vector form over transient states $T$, the system is $\\boldsymbol{\\mu} = \\mathbf{1} + Q \\boldsymbol{\\mu}$, which yields $(I - Q) \\boldsymbol{\\mu} = \\mathbf{1} \\implies \\boldsymbol{\\mu} = (I - Q)^{-1} \\mathbf{1}$, identifying mean hitting time as the row sum of the fundamental matrix."
    ],
    r"$$\mu_i = \begin{cases} 0 & i \in A \\ 1 + \sum_{j \notin A} P_{ij} \mu_j & i \notin A \end{cases} \iff (I - Q) \boldsymbol{\mu} = \mathbf{1}$$",
    "GPS navigation rerouting: expected arrival time from intersection i equals 1 minute to traverse the intersection plus the weighted expected arrival time from neighboring intersections.",
    "Omitting the +1 in hitting time calculations! Without +1, the equation becomes μ = Qμ, which gives the useless trivial solution μ = 0. In contrast, absorption probabilities do NOT have +1."
))

# Card 32103: Canonical Form & The Fundamental Matrix
svg_32103 = [
    # Canonical matrix partition
    R(25, 20, 85, 85, "#ffffff", 1.8),
    # Q block
    R(25, 20, 50, 50, "#f8fafc", 1.4), N(50, 48, "Q (t×t)", 9, w="bold"),
    # R block
    R(75, 20, 35, 50, "#f1f5f9", 1.4), N(92, 48, "R (t×r)", 9, w="bold"),
    # 0 block
    R(25, 70, 50, 35, "#ffffff", 1.4), N(50, 90, "0", 9),
    # I block
    R(75, 70, 35, 35, "#f1f5f9", 1.4), N(92, 90, "I_r", 9, w="bold"),

    # Arrow to fundamental matrix N
    V(115, 62, 142, 62, 1.8),

    # Fundamental matrix box
    box(145, 28, 80, 70, "Fundamental Matrix\nN = (I - Q)^{-1}\n= I + Q + Q^2 + ...\nN_ij = E[visits to j]", "#ffffff", 7.5),
    N(120, 122, "Q^n → 0 as n → ∞: transient states are abandoned with probability 1", 8),
    N(120, 138, "Canonical form partitions P into transient block Q and absorbing block R; N = (I - Q)^(-1)", 8.5)
]
CARDS.append(make_stoma_card(
    21, 3, "FUNDAMENTAL MATRIX",
    "Canonical Form & Fundamental Matrix N = (I-Q)^{-1}",
    svg_32103,
    "The fundamental matrix N = (I - Q)^{-1} sums the geometric series of transient transitions, tallying expected visit counts",
    [
        "<strong>Canonical Partitioning:</strong> Reordering states into $t$ transient states followed by $r$ absorbing states formats transition matrix $P$ as $P = \\begin{pmatrix} Q & R \\\\ 0 & I_r \\end{pmatrix}$, where $Q$ governs internal transient jumps and $R$ governs transitions into absorbing sinks.",
        "<strong>Fundamental Matrix Definition:</strong> Because transient states are eventually abandoned ($Q^n \\to 0$ as $n \\to \\infty$), the matrix Neumann series converges: $N = \\sum_{k=0}^\\infty Q^k = (I - Q)^{-1}$, termed the Fundamental Matrix of the absorbing chain.",
        "<strong>Occupancy Counting Meaning:</strong> Entry $N_{ij}$ equals the exact expected number of visits to transient state $j$ prior to absorption, given the process initialized in transient state $i$: $N_{ij} = \\mathbb{E}\\left[\\sum_{n=0}^\\infty \\mathbf{1}_{\\{X_n = j\\}} \\,\\middle|\\, X_0 = i\\right]$."
    ],
    r"$$P = \begin{pmatrix} Q & R \\ 0 & I \end{pmatrix} \implies N = \sum_{k=0}^\infty Q^k = (I - Q)^{-1}, \quad N_{ij} = \mathbb{E}[\text{Visits to } j \mid X_0 = i]$$",
    "Video game replay counter: N_ij records how many times a player passes through checkpoint j on attempts originating from stage i before reaching game over or victory.",
    "Forgetting that N_ii ≥ 1 always! When starting in state i, step n=0 counts as a visit to state i (1_{X_0=i} = 1), so the diagonal entries of N are always at least 1, even if Q_ii = 0."
))

# Card 32104: Absorption Matrix B = NR & Expected Time t = N1
svg_32104 = [
    # Vector schematic connecting N, R, and B
    box(15, 30, 55, 45, "Transient Start\nState i\n(Vector e_i)", "#f8fafc", 7.5),
    V(70, 52, 95, 52, 1.8),
    box(95, 25, 55, 55, "Matrix N\nTransient\nVisits\n(t × t)", "#ffffff", 8),
    V(150, 52, 175, 52, 1.8),
    box(175, 25, 52, 55, "Matrix R\nEscape Jumps\n(t × r)", "#f1f5f9", 8),

    # Resulting equations
    R(25, 92, 90, 26, "#ffffff", 1.4),
    N(70, 108, "B = N R (Absorption)", 8.5, w="bold"),

    R(125, 92, 90, 26, "#ffffff", 1.4),
    N(170, 108, "t = N 1 (Time Vector)", 8.5, w="bold"),

    N(120, 138, "Complete absorption calculus: B = NR yields destination probabilities; t = N1 yields expected lifetimes", 8.5)
]
CARDS.append(make_stoma_card(
    21, 4, "MATRIX ABSORPTION CALCULUS",
    "Absorption Probabilities B = NR & Lifetime Vector",
    svg_32104,
    "Matrix multiplication resolves all absorption destinations simultaneously: B = NR and total lifetime t = N1",
    [
        "<strong>Destination Matrix Product $B = NR$:</strong> The $(t \\times r)$ matrix $B$ provides exact absorption probabilities: $B_{ik} = P(\\text{absorbed in state } k \\mid X_0 = i) = (NR)_{ik}$. Every row of $B$ sums to 1 if absorption occurs with probability 1 from all transient states.",
        "<strong>Expected Time to Absorption Vector:</strong> The total duration spent wandering through all transient states before absorption is obtained by summing expected visits across all transient states: $t_i = \\sum_{j \\in T} N_{ij} = (N \\mathbf{1})_i$.",
        "<strong>Direct Computational Advantage:</strong> Inverting a single $(t \\times t)$ matrix $(I - Q)$ simultaneously evaluates absorption probabilities into all sinks and expected lifetimes from all starting states, eliminating piecemeal linear equations."
    ],
    r"$$B = N R \implies B_{ik} = P(\text{Absorbed into } k \mid X_0 = i); \quad \mathbf{t} = N \mathbf{1} \implies t_i = \mathbb{E}[\tau_{\text{abs}} \mid X_0 = i]$$",
    "Hospital patient triage: N tracks average visits to medical wards, R represents discharge vs mortality rates, and NR computes overall survival probability from admission.",
    "Multiplying RN instead of NR! The dimensions must align: N is (t × t) and R is (t × r), so NR produces a (t × r) matrix mapping transient starting states to absorbing destinations. RN is undefined!"
))

# Card 32105: Gambler's Ruin Closed-Form Solution
svg_32105 = [
    # Gambler's ruin chain
    AX(25, 115, 215, 25),
    N(220, 115, "i", 8), N(20, 22, "a_i", 8),
    # State ticks
    C(25, 30, 4, fill="#000000"), N(25, 126, "0 (Ruin)", 8),
    C(210, 115, 4, fill="#000000"), N(210, 126, "N (Win)", 8),
    # Curves for p < 1/2, p = 1/2, p > 1/2
    # Fair p = 1/2: linear
    L(25, 30, 210, 115, 1.8),
    N(145, 75, "p = 1/2 (Linear)", 7.5),
    # Unfavorable p < 1/2: convex down / stay near 1
    P("M 25,30 Q 140,40 210,115", fill="none", w=1.5, dash="3 3"),
    N(80, 48, "p < 1/2 (High ruin)", 7.5),
    # Favorable p > 1/2: concave
    P("M 25,30 Q 60,110 210,115", fill="none", w=1.5, dash="2 2"),
    N(100, 105, "p > 1/2 (Low ruin)", 7.5),

    N(120, 138, "Gambler's ruin: linear a_i = 1 - i/N for fair coin; exponential a_i = (ρ^i - ρ^N)/(1 - ρ^N) with ρ = q/p", 8.5)
]
CARDS.append(make_stoma_card(
    21, 5, "GAMBLER'S RUIN",
    "Gambler’s Ruin: Difference Equations & Drift Regimes",
    svg_32105,
    "Second-order difference equations yield exact closed-form ruin probabilities across fair and asymmetric coin tosses",
    [
        "<strong>Difference Equation Formulation:</strong> Let $a_i$ be the probability of ruin starting with $\$i$. First-step conditioning gives $a_i = p a_{i+1} + q a_{i-1}$ with boundary conditions $a_0 = 1$ and $a_N = 0$. The characteristic ratio is $\\rho = q/p$.",
        "<strong>Closed-Form Ruin Probability:</strong> Solving the homogeneous difference equation yields $a_i = \\frac{\\rho^i - \\rho^N}{1 - \\rho^N}$ when $p \\ne q$. In a fair game ($p = q = 1/2$, $\\rho = 1$), L'Hôpital's limit yields the linear ruin probability $a_i = 1 - \\frac{i}{N}$.",
        "<strong>Expected Game Duration:</strong> The mean time until the game ends is $\\mu_i = \\frac{i}{q - p} - \\frac{N}{q - p} \\left(\\frac{1 - \\rho^i}{1 - \\rho^N}\\right)$ for $p \\ne q$, simplifying to parabolic duration $\\mu_i = i(N - i)$ for a fair coin ($p = 1/2$)."
    ],
    r"$$a_i = \begin{cases} \frac{(q/p)^i - (q/p)^N}{1 - (q/p)^N} & p \ne q \\ 1 - \frac{i}{N} & p = q = \frac{1}{2} \end{cases}; \quad \mu_i = i(N - i) \quad (\text{if } p = 1/2)$$",
    "Casino betting bankroll: even with a slight house edge (p = 0.49), the exponential ruin formula demonstrates near certainty of bankruptcy before doubling a stake.",
    "Using the biased formula when p = 1/2! Substituting p = q = 1/2 into (ρ^i - ρ^N)/(1 - ρ^N) gives indeterminate 0/0. For p = 1/2, the solution is linear a_i = 1 - i/N, not exponential!"
))

# Card 32106: Pattern Hitting Times & The Overlap Paradox
svg_32106 = [
    # Top: HT automata
    N(25, 35, "HT:", 9, w="bold"),
    C(50, 32, 10, fill="#ffffff"), N(50, 35, "∅", 8),
    V(60, 32, 85, 32, 1.5), N(72, 26, "H", 7),
    C(95, 32, 10, fill="#ffffff"), N(95, 35, "H", 8),
    V(105, 32, 130, 32, 1.5), N(117, 26, "T", 7),
    box(130, 20, 36, 24, "HT", "#f1f5f9", 8, bold=True),
    # HT self loop on H
    P("M 95,22 C 90,8 100,8 97,20", fill="none", w=1.2, ar=True), N(95, 6, "H", 6.5),
    N(190, 32, "E[T_HT] = 4", 9, w="bold"),

    # Bottom: HH automata
    N(25, 90, "HH:", 9, w="bold"),
    C(50, 87, 10, fill="#ffffff"), N(50, 90, "∅", 8),
    V(60, 87, 85, 87, 1.5), N(72, 81, "H", 7),
    C(95, 87, 10, fill="#ffffff"), N(95, 90, "H", 8),
    V(105, 87, 130, 87, 1.5), N(117, 81, "H", 7),
    box(130, 75, 36, 24, "HH", "#f1f5f9", 8, bold=True),
    # HH reset on T back to empty!
    P("M 95,97 C 80,120 65,120 52,99", fill="none", w=1.2, ar=True), N(75, 122, "T (Full reset!)", 7),
    N(190, 87, "E[T_HH] = 6", 9, w="bold"),

    N(120, 138, "Pattern waiting time paradox: E[T_HH] = 6 > E[T_HT] = 4 due to destructive resets upon mismatch", 8.5)
]
CARDS.append(make_stoma_card(
    21, 6, "PATTERN WAITING TIMES",
    "Pattern Waiting Times & The Self-Overlap Paradox",
    svg_32106,
    "Destructive prefix resets cause equal-probability patterns to exhibit radically different expected arrival times",
    [
        "<strong>Prefix State Automata:</strong> Model the occurrence of sequence pattern $W$ as hitting time of an absorbing Markov chain whose states represent the longest matched prefix of $W$. Transitions follow incoming coin tosses.",
        "<strong>The $HT$ vs $HH$ Paradox:</strong> In fair coin tosses, $\\mathbb{E}[T_{HT}] = 4$ whereas $\\mathbb{E}[T_{HH}] = 6$. For $HT$: if an $H$ is followed by $H$, the match prefix remains length 1 ($H$), maintaining forward readiness. For $HH$: if $H$ is followed by $T$, the prefix collapses completely to $\\emptyset$.",
        "<strong>Conway’s Pattern Leading Number Rule:</strong> The expected waiting time for any binary pattern $W$ of length $k$ is $\\mathbb{E}[T_W] = \\sum_{j=1}^k c_j 2^j$, where $c_j = 1$ if the prefix of length $j$ matches the suffix of length $j$ (self-overlap), and 0 otherwise."
    ],
    r"$$\mathbb{E}[T_{HT}] = 4 \quad \text{vs} \quad \mathbb{E}[T_{HH}] = 6; \quad \mathbb{E}[T_W] = \sum_{j=1}^k c_j 2^j \quad (\text{Conway's Theorem})$$",
    "DNA sequence motif search: searching for repetitive sequences like 'AAA' takes significantly longer than non-overlapping motifs 'ATG' due to wasted partial matches resetting upon mismatches.",
    "Assuming equally likely sequences have equal expected waiting times! At any two consecutive flips, P(HT) = P(HH) = 1/4, but waiting times differ fundamentally due to renewal regeneration: after seeing HH, another H immediately completes the next HH in 1 flip, clustering occurrences together!"
))

if __name__ == "__main__":
    save_stoma_cards(CARDS)
    print("Successfully generated 12 cards for StoMA Topics 20 & 21!")
