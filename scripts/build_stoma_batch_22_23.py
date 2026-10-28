"""Build StoMA Topics 22 & 23 (Cards 32201 to 32306).
Dual-coding photographic plates with pure black-and-white vector diagrams.
"""
import sys, os
sys.path.append(os.path.dirname(__file__))
from stoma_lib import (
    T, N, L, V, P, C, R, E, PG, AX, box, svg, make_stoma_card, save_stoma_cards
)

CARDS = []

# ==============================================================================
# TOPIC 22: BIRTH-DEATH CHAINS & MCMC (32201 - 32206)
# ==============================================================================

# Card 32201: Birth-Death Chains & Detailed Balance
svg_32201 = [
    # Chain nodes 0, 1, 2, 3
    C(35, 70, 14, fill="#ffffff"), N(35, 73, "0", 9, w="bold"),
    C(90, 70, 14, fill="#ffffff"), N(90, 73, "1", 9, w="bold"),
    C(145, 70, 14, fill="#ffffff"), N(145, 73, "2", 9, w="bold"),
    C(200, 70, 14, fill="#ffffff"), N(200, 73, "3", 9, w="bold"),

    # Forward birth arrows
    P("M 47,60 C 60,45 77,45 80,58", fill="none", w=1.6, ar=True), N(63, 44, "p_0", 7.5),
    P("M 102,60 C 115,45 132,45 135,58", fill="none", w=1.6, ar=True), N(118, 44, "p_1", 7.5),
    P("M 157,60 C 170,45 187,45 190,58", fill="none", w=1.6, ar=True), N(173, 44, "p_2", 7.5),

    # Backward death arrows
    P("M 78,80 C 65,95 48,95 45,82", fill="none", w=1.6, ar=True), N(63, 102, "q_1", 7.5),
    P("M 133,80 C 120,95 103,95 100,82", fill="none", w=1.6, ar=True), N(118, 102, "q_2", 7.5),
    P("M 188,80 C 175,95 158,95 155,82", fill="none", w=1.6, ar=True), N(173, 102, "q_3", 7.5),

    # Formula box
    box(45, 12, 150, 22, "Detailed Balance: π_i p_i = π_{i+1} q_{i+1}", "#f1f5f9", 8, bold=True),
    N(120, 138, "Birth-death chains: transitions occur only to adjacent neighbors; detailed balance holds at every link", 8.5)
]
CARDS.append(make_stoma_card(
    22, 1, "BIRTH-DEATH CHAINS",
    "Birth-Death Chains & Detailed Balance Equations",
    svg_32201,
    "Birth-death chains restrict transitions to nearest neighbors, equating forward and reverse fluxes via detailed balance",
    [
        "<strong>Tridiagonal Transition Structure:</strong> A discrete-time birth-death chain on $\{0, 1, 2, \\dots\}$ only permits transitions to adjacent neighbors: $P_{i, i+1} = p_i$, $P_{i, i-1} = q_i$, and $P_{i, i} = r_i = 1 - p_i - q_i$. Boundary state 0 satisfies $q_0 = 0$.",
        "<strong>Cut Equivalence to Detailed Balance:</strong> Taking the cut between $\{0, 1, \\dots, i\}$ and $\{i+1, \\dots\}$, the only crossing transitions are the birth $i \\to i+1$ and the death $i+1 \\to i$. Flux conservation directly yields pairwise detailed balance: $\\pi_i p_i = \\pi_{i+1} q_{i+1}$.",
        "<strong>Recursive Ratio:</strong> Rearranging gives $\\pi_{i+1} = \\left(\\frac{p_i}{q_{i+1}}\\right) \\pi_i$, transforming the matrix inversion problem $(I - P^\\top)\\pi = 0$ into a simple 1D recursive product."
    ],
    r"$$\pi_i p_i = \pi_{i+1} q_{i+1} \implies \pi_{i+1} = \left(\frac{p_i}{q_{i+1}}\right) \pi_i \quad \forall i \ge 0$$",
    "Two-way revolving door: equilibrium between rooms requires the number of people walking left-to-right each minute to equal the number walking right-to-left.",
    "Applying birth-death formulas to chains with skip transitions! If transitions like i → i+2 or resets to 0 occur, the chain is no longer tridiagonal and simple detailed balance π_i p_i = π_{i+1} q_{i+1} breaks!"
))

# Card 32202: Birth-Death Invariant Measure & Ergodicity
svg_32202 = [
    # Geometric decay plot
    AX(25, 115, 215, 25),
    N(220, 115, "n", 8), N(20, 22, "π_n", 8),
    # Bars for decaying distribution
    R(38, 45, 12, 70, "#f8fafc", 1.2), N(44, 40, "π_0", 7.5),
    R(68, 62, 12, 53, "#f1f5f9", 1.2), N(74, 57, "π_1", 7.5),
    R(98, 77, 12, 38, "#f1f5f9", 1.2), N(104, 72, "π_2", 7.5),
    R(128, 90, 12, 25, "#ffffff", 1.2), N(134, 85, "π_3", 7.5),
    R(158, 100, 12, 15, "#ffffff", 1.2),
    # Geometric decay envelope curve
    P("M 44,45 Q 90,75 180,108", fill="none", w=1.6, dash="3 3"),
    # Convergence condition box
    box(115, 20, 100, 32, "Ergodicity Condition:\nΣ_{n=1}^∞ Π_{k=0}^{n-1} (p_k / q_{k+1}) < ∞", "#ffffff", 7),
    N(120, 138, "Birth-death invariant measure: π_n = π_0 Π (p_k / q_{k+1}); normalizable iff the infinite sum converges", 8.5)
]
CARDS.append(make_stoma_card(
    22, 2, "INVARIANT MEASURES",
    "Birth-Death Invariant Distribution & Ergodicity Criteria",
    svg_32202,
    "The stationary distribution has closed form π_n = π_0 Π (p_k / q_{k+1}), normalizable if and only if the series converges",
    [
        "<strong>Product Form Invariant Measure:</strong> Iterating the detailed balance ratio yields $\\pi_n = \\pi_0 \\prod_{k=0}^{n-1} \\frac{p_k}{q_{k+1}}$ for all $n \\ge 1$, where $\\pi_0$ acts as an overall scale factor.",
        "<strong>Normalization Condition:</strong> The chain is positive recurrent (ergodic) if and only if the series converges: $S = \\sum_{n=1}^\\infty \\prod_{k=0}^{n-1} \\frac{p_k}{q_{k+1}} < \\infty$. When $S < \\infty$, $\\pi_0 = \\frac{1}{1 + S} > 0$.",
        "<strong>M/M/1 Queue Benchmark:</strong> With constant rates $p_k = p$ and $q_k = q$, the ratio is constant $\\rho = p/q$. The sum converges iff traffic intensity $\\rho < 1$, yielding the classic geometric distribution $\\pi_n = (1 - \\rho)\\rho^n$ with mean occupancy $\\mathbb{E}[N] = \\frac{\\rho}{1 - \\rho}$."
    ],
    r"$$\pi_n = \pi_0 \prod_{k=0}^{n-1} \frac{p_k}{q_{k+1}}, \qquad \pi_0 = \left(1 + \sum_{n=1}^\infty \prod_{k=0}^{n-1} \frac{p_k}{q_{k+1}}\right)^{-1} > 0 \iff S < \infty$$",
    "Queue buffer stabilizing: if arrival rate is strictly less than service rate (p < q), customer backlog decays exponentially as a geometric distribution.",
    "Assuming traffic intensity ρ = 1 has a stationary distribution! When ρ = p/q = 1, all π_n = π_0 are equal, so the sum diverges. The chain is null recurrent, not positive recurrent!"
))

# Card 32203: Time Reversibility & Kolmogorov’s Cycle Criterion
svg_32203 = [
    # Reversible Cycle: 1 -> 2 -> 3 -> 1
    C(60, 40, 12, fill="#ffffff"), N(60, 43, "1", 9, w="bold"),
    C(120, 40, 12, fill="#ffffff"), N(120, 43, "2", 9, w="bold"),
    C(90, 95, 12, fill="#ffffff"), N(90, 98, "3", 9, w="bold"),

    # Clockwise cycle arrows
    V(74, 38, 106, 38, 1.6), N(90, 30, "P_12", 7.5),
    V(116, 52, 98, 83, 1.6), N(116, 70, "P_23", 7.5),
    V(82, 83, 64, 52, 1.6), N(64, 70, "P_31", 7.5),

    # Kolmogorov criterion box on right
    box(135, 30, 95, 52, "Kolmogorov Criterion:\nP_12 P_23 P_31\n=\nP_13 P_32 P_21\n(No probability vortex!)", "#f1f5f9", 7.5),

    N(120, 122, "Detailed balance π_i P_ij = π_j P_ji ⟺ Time-reversed chain has identical law", 8),
    N(120, 138, "Time-reversibility: Kolmogorov's cycle criterion requires equal cycle products in both directions", 8.5)
]
CARDS.append(make_stoma_card(
    22, 3, "TIME REVERSIBILITY",
    "Time Reversibility & Kolmogorov’s Cycle Criterion",
    svg_32203,
    "A chain is time-reversible iff it satisfies detailed balance, equivalent to Kolmogorov's loop product equality",
    [
        "<strong>Time-Reversed Chain Law:</strong> For a stationary Markov chain $\{X_n\}$, the time-reversed chain $Y_n = X_{-n}$ has transition probabilities $P_{ij}^* = \\frac{\\pi_j P_{ji}}{\\pi_i}$. The chain is reversible if $P_{ij}^* = P_{ij}$ for all $i, j$, which is identical to detailed balance $\\pi_i P_{ij} = \\pi_j P_{ji}$.",
        "<strong>Kolmogorov’s Cycle Criterion:</strong> A stationary Markov chain is reversible if and only if for every closed loop of states $i_0, i_1, \\dots, i_k, i_0$, the product of transition probabilities in the forward direction equals the reverse direction: $\\prod_{m=0}^k P_{i_m, i_{m+1}} = \\prod_{m=0}^k P_{i_{m+1}, i_m}$.",
        "<strong>Vortex Impossibility:</strong> Kolmogorov's criterion checks reversibility directly from the transition matrix $P$ without having to solve for the stationary distribution $\\pi$ first; non-reversible chains contain net directional probability circulation (vortices)."
    ],
    r"$$\pi_i P_{ij} = \pi_j P_{ji} \iff P_{i_0 i_1} P_{i_1 i_2} \cdots P_{i_k i_0} = P_{i_0 i_k} \cdots P_{i_2 i_1} P_{i_1 i_0} \quad \forall \text{ cycles}$$",
    "Playing a movie backwards: if a movie of the chain running in steady state looks statistically indistinguishable when played in reverse, the process is time-reversible.",
    "Assuming every stationary chain is reversible! Cyclic chains (e.g. 1 → 2 → 3 → 1 with probability 1) have stationary distribution π = (1/3, 1/3, 1/3) but reverse direction product is 0 ≠ 1, completely violating reversibility!"
))

# Card 32204: The Metropolis-Hastings Algorithm
svg_32204 = [
    # Current state x
    C(45, 65, 14, fill="#ffffff"), N(45, 68, "x", 10, w="bold"),
    # Proposal jump
    P("M 59,58 C 80,35 110,35 130,52", fill="none", w=1.8, ar=True),
    N(95, 32, "Candidate y ~ q(y | x)", 8, w="bold"),
    # Candidate state y
    C(145, 65, 14, fill="#f1f5f9"), N(145, 68, "y", 10, w="bold"),

    # Accept branch
    V(158, 58, 200, 40, 1.6),
    box(200, 28, 35, 20, "Accept", "#f8fafc", 7.5),
    N(178, 38, "α(x, y)", 7),

    # Reject branch
    V(155, 78, 175, 95, 1.6),
    P("M 175,95 C 130,115 80,115 48,82", fill="none", w=1.6, ar=True),
    box(100, 98, 48, 18, "Reject: Stay!", "#ffffff", 7),
    N(165, 84, "1 - α", 7),

    N(120, 138, "Metropolis-Hastings: α(x, y) = min(1, [π(y)q(x|y)] / [π(x)q(y|x)]); normalizer Z cancels completely", 8.5)
]
CARDS.append(make_stoma_card(
    22, 4, "MCMC SAMPLING",
    "The Metropolis-Hastings Algorithm & Acceptance Rule",
    svg_32204,
    "Metropolis-Hastings generates samples from intractable distributions by accepting candidate proposals with probability α",
    [
        "<strong>Algorithm Formulation:</strong> Given an unnormalized target density $\\pi(x) = \\tilde{\\pi}(x)/Z$, at state $X_t = x$, generate candidate $y \\sim q(y \\mid x)$. Accept $X_{t+1} = y$ with probability $\\alpha(x, y) = \\min\\left(1, \\frac{\\pi(y) q(x \\mid y)}{\\pi(x) q(y \\mid x)}\\right)$; otherwise reject and set $X_{t+1} = x$.",
        "<strong>Intractable Normalizer Cancellation:</strong> Because the acceptance ratio contains the ratio $\\frac{\\pi(y)}{\\pi(x)} = \\frac{\\tilde{\\pi}(y)/Z}{\\tilde{\\pi}(x)/Z} = \\frac{\\tilde{\\pi}(y)}{\\tilde{\\pi}(x)}$, the partition function $Z = \\int \\tilde{\\pi}(x) dx$ cancels out entirely, unlocking high-dimensional Bayesian inference.",
        "<strong>Exact Detailed Balance Proof:</strong> Transition kernel $P(x, y) = q(y \\mid x) \\alpha(x, y)$ satisfies $\\pi(x) P(x, y) = \\pi(y) P(y, x)$ identically for all $x \\ne y$, proving target density $\\pi$ is the exact stationary distribution."
    ],
    r"$$\alpha(x, y) = \min\left(1, \frac{\tilde{\pi}(y) q(x \mid y)}{\tilde{\pi}(x) q(y \mid x)}\right) \implies \pi(x) q(y \mid x) \alpha(x, y) = \pi(y) q(x \mid y) \alpha(y, x)$$",
    "Blind mountain climber: proposing a step; if uphill (π(y) > π(x)), accept with probability 1; if downhill, accept with probability proportional to the drop to avoid getting stuck in local traps.",
    "Discarding rejected proposals from the sample history! When a proposal is rejected, the chain *remains* at the current state x, meaning x must be recorded AGAIN as the next sample X_{t+1} = x. Dropping rejections severely biases the empirical distribution!"
))

# Card 32205: Symmetric Random Walk Metropolis & Step Tuning
svg_32205 = [
    # Bell curve target
    P("M 25,105 Q 85,105 105,70 Q 120,25 125,25 Q 130,25 145,70 Q 165,105 225,105", fill="none", w=1.8),
    N(125, 18, "Target π(x)", 8.5, w="bold"),
    # Current point x
    C(110, 52, 3, fill="#000000"), N(110, 62, "x", 8),
    # Proposal window [x - δ, x + δ]
    L(70, 115, 150, 115, 1.5),
    L(70, 110, 70, 120, 1.5), L(150, 110, 150, 120, 1.5),
    N(110, 125, "Window 2δ", 8),
    # Tradeoff notes
    box(20, 25, 75, 40, "Small δ:\nHigh accept (95%)\nSlow exploration!", "#f8fafc", 7),
    box(150, 25, 75, 40, "Large δ:\nLow accept (5%)\nStuck in place!", "#f8fafc", 7),
    N(120, 138, "Random-walk Metropolis: q(y|x) = q(x|y) simplifies α = min(1, π(y)/π(x)); optimal acceptance ~23.4%", 8.5)
]
CARDS.append(make_stoma_card(
    22, 5, "MCMC TUNING",
    "Random Walk Metropolis & The Proposal Tuning Dilemma",
    svg_32205,
    "Symmetric proposals reduce acceptance to the likelihood ratio; proposal variance must balance exploration speed against rejection rate",
    [
        "<strong>Symmetric Proposal Simplification:</strong> When proposal distribution is symmetric ($q(y \\mid x) = q(x \\mid y)$, e.g., Gaussian $y \\sim \\mathcal{N}(x, \\sigma^2)$ or Uniform $y \\sim \\text{Unif}[x-\\delta, x+\\delta]$), the proposal density ratio equals 1, yielding classic Metropolis: $\\alpha(x, y) = \\min\\left(1, \\frac{\\pi(y)}{\\pi(x)}\\right)$.",
        "<strong>Step-Size Goldilocks Dilemma:</strong> If proposal step $\\delta$ is too small, nearly all moves are accepted but the chain diffuses sluggishly (high autocorrelation). If $\\delta$ is too large, proposed jumps land in low-probability tails and are overwhelmingly rejected, trapping the chain.",
        "<strong>Optimal Acceptance Rate Benchmark:</strong> For high-dimensional Gaussian targets ($d \\to \\infty$), Gelman, Roberts & Gilks proved the optimal acceptance rate that maximizes asymptotic diffusion efficiency is approximately $23.4\\%$ (and $\\approx 44\\%$ in 1D)."
    ],
    r"$$\alpha(x, y) = \min\left(1, \frac{\pi(y)}{\pi(x)}\right) \quad (\text{Symmetric: } q(y \mid x) = q(x \mid y)); \quad \text{Optimal Accept Rate} \approx 23.4\%$$",
    "Thermostat dial tuning: turning the temperature knob too gently barely changes room temperature; turning it too aggressively causes severe overshoots and safety cutoffs.",
    "Assuming an acceptance rate near 100% indicates superior MCMC performance! A near-100% acceptance rate usually means the proposal step size is infinitesimally tiny, leaving the sampler trapped in a microscopic corner of the state space!"
))

# Card 32206: Gibbs Sampling & Full Conditional Updates
svg_32206 = [
    # 2D contour ellipses
    E(120, 70, 60, 35, rot=-30, fill="#f8fafc", w=1.2),
    E(120, 70, 35, 20, rot=-30, fill="#f1f5f9", w=1.4),
    # Gibbs orthogonal steps
    # Point 0
    C(80, 95, 3, fill="#000000"), N(75, 105, "(x_0, y_0)", 7.5),
    # Step 1: Vertical move (sample Y | X)
    V(80, 95, 80, 55, 1.8),
    C(80, 55, 3, fill="#000000"), N(65, 50, "(x_0, y_1)", 7.5),
    # Step 2: Horizontal move (sample X | Y)
    V(80, 55, 125, 55, 1.8),
    C(125, 55, 3, fill="#000000"), N(138, 50, "(x_1, y_1)", 7.5),
    # Step 3: Vertical move
    V(125, 55, 125, 75, 1.8),
    C(125, 75, 3, fill="#000000"),

    # Formula box
    box(140, 92, 90, 26, "Gibbs: Accept Rate α ≡ 1\nX_i ~ p(X_i | X_{-i})", "#ffffff", 7.5),
    N(120, 138, "Gibbs sampling: updates one coordinate at a time via full conditionals; acceptance probability is identically 1", 8.5)
]
CARDS.append(make_stoma_card(
    22, 6, "GIBBS SAMPLING",
    "Gibbs Sampling & Full Conditional Updates",
    svg_32206,
    "Gibbs sampling updates coordinates individually from full conditional distributions, guaranteeing an acceptance rate of 100%",
    [
        "<strong>Coordinate-Wise Iteration:</strong> To sample from joint distribution $p(x_1, \\dots, x_d)$, Gibbs sampling updates each variable sequentially by sampling from its full conditional distribution: $X_i^{(t+1)} \\sim p(X_i \\mid X_1^{(t+1)}, \\dots, X_{i-1}^{(t+1)}, X_{i+1}^{(t)}, \\dots, X_d^{(t)})$.",
        "<strong>Special Case of Metropolis-Hastings:</strong> Gibbs sampling is mathematically a Metropolis-Hastings algorithm where proposal is the exact conditional $q(y \\mid x) = p(y_i \\mid x_{-i})$. Substituting this proposal into the M-H ratio yields an acceptance probability of identically 1: $\\alpha(x, y) = \\min(1, 1) = 1$.",
        "<strong>AR(1) Dynamics in Gaussian Models:</strong> When applying Gibbs sampling to standard bivariate Gaussian $(X, Y)$ with correlation $\rho$, each variable is updated as $X_{t+1} = \\rho^2 X_t + \\sqrt{1 - \\rho^4} Z_t$, establishing an exact AR(1) process with convergence speed determined by $\\rho^2$."
    ],
    r"$$X_i^{(t+1)} \sim p(X_i \mid X_{-i}^{(t)}) \implies \alpha(x, y) = \min\left(1, \frac{p(y) p(x_i \mid x_{-i})}{p(x) p(y_i \mid x_{-i})}\right) \equiv 1$$",
    "Manhattan taxi grid navigation: moving only north-south or east-west along coordinate axes, yet covering the entire 2D urban landscape seamlessly.",
    "Applying Gibbs sampling when full conditionals are not analytically standard! Gibbs sampling requires easy sampling from 1D full conditionals p(X_i | X_{-i}). If conditionals are intractable, Metropolis-within-Gibbs must be used instead."
))

# ==============================================================================
# TOPIC 23: RANDOM PROCESSES: STATIONARITY & ERGODICITY (32301 - 32306)
# ==============================================================================

# Card 32301: Strict-Sense vs Wide-Sense Stationarity
svg_32301 = [
    # Venn diagram: SSS inside WSS
    E(120, 68, 95, 45, fill="#f8fafc", w=1.6),
    N(120, 32, "Wide-Sense Stationary (WSS)", 9, w="bold"),
    N(120, 44, "E[X(t)] = μ (const), R_X(t, t+τ) = R_X(τ)", 7.5),

    E(120, 80, 55, 26, fill="#f1f5f9", w=1.6),
    N(120, 74, "Strict-Sense Stationary (SSS)", 8.5, w="bold"),
    N(120, 86, "All joint CDFs invariant to shift τ", 7.5),

    # Gaussian equivalence note
    box(25, 95, 75, 25, "Gaussian Process:\nWSS  ⟺  SSS!", "#ffffff", 7.5, bold=True),
    N(120, 138, "Stationarity hierarchy: SSS implies WSS (if finite variance); WSS implies SSS only for Gaussian processes", 8.5)
]
CARDS.append(make_stoma_card(
    23, 1, "STATIONARITY TYPES",
    "Strict-Sense vs Wide-Sense Stationarity",
    svg_32301,
    "SSS requires all joint distributions to be shift-invariant; WSS requires only constant mean and lag-dependent autocorrelation",
    [
        "<strong>Strict-Sense Stationarity (SSS):</strong> A random process $\{X(t)\}$ is SSS if all finite-dimensional distributions are invariant under time shifts: $(X(t_1), \\dots, X(t_k)) \\stackrel{d}{=} (X(t_1+\\tau), \\dots, X(t_k+\\tau))$ for all lags $\\tau$ and choices of time indices.",
        "<strong>Wide-Sense Stationarity (WSS):</strong> A process is WSS (weakly stationary) if: (1) $\\mathbb{E}[X(t)] = \\mu$ is constant for all $t$; (2) $\\mathbb{E}[X^2(t)] < \\infty$; and (3) Autocorrelation $R_X(t, t+\\tau) = \\mathbb{E}[X(t)X(t+\\tau)] = R_X(\\tau)$ depends only on lag $\\tau$.",
        "<strong>Gaussian Equivalence:</strong> Because a Gaussian process is completely specified by its mean function and covariance function, for Gaussian processes Wide-Sense Stationarity is mathematically equivalent to Strict-Sense Stationarity: $\\text{WSS} \\iff \\text{SSS}$."
    ],
    r"$$\text{SSS}: F_{X(t_1+\tau), \dots, X(t_k+\tau)} = F_{X(t_1), \dots, X(t_k)}; \quad \text{WSS}: \mathbb{E}[X(t)] = \mu, \ R_X(t, t+\tau) = R_X(\tau)$$",
    "Photographic film exposure: SSS means the entire statistical texture of the image is invariant under translation; WSS means only the average brightness and 2-point pixel contrast are invariant.",
    "Assuming WSS implies SSS! Consider independent X_n with mean 0 and variance 1 where X_n ~ N(0, 1) for even n and X_n ~ Uniform[-√3, √3] for odd n. It is WSS, but its 4th moment changes with parity, violating SSS!"
))

# Card 32302: Properties of the Autocorrelation Function
svg_32302 = [
    # Coordinate axes
    AX(24, 115, 220, 20),
    N(222, 115, "τ", 8), N(20, 22, "R_X(τ)", 8),
    # Upper bound line R(0)
    L(24, 35, 215, 35, 1.0, d="2 2"), N(200, 30, "R_X(0) = E[X²]", 7.5),
    # Lower bound line -R(0)
    L(24, 115, 215, 115, 1.0),
    # Symmetric even curve peaked at origin
    P("M 25,105 Q 80,105 110,65 Q 120,35 125,35 Q 130,35 140,65 Q 170,105 225,105", fill="none", w=2.0),
    C(125, 35, 3, fill="#000000"), N(125, 126, "τ = 0", 8, w="bold"),
    # Symmetry note
    N(70, 75, "R_X(-τ)", 8), N(180, 75, "R_X(τ)", 8),
    box(25, 12, 85, 20, "Even: R_X(-τ) = R_X(τ)", "#f1f5f9", 7.5),
    N(120, 138, "Autocorrelation properties: peak at origin |R_X(τ)| ≤ R_X(0), even symmetry R_X(-τ) = R_X(τ), positive semi-definite", 8.5)
]
CARDS.append(make_stoma_card(
    23, 2, "AUTOCORRELATION",
    "Properties of the Autocorrelation Function R_X(τ)",
    svg_32302,
    "The autocorrelation function is symmetric, maximized at the origin, and represents average process power at zero lag",
    [
        "<strong>Maximum at the Origin:</strong> By the Cauchy-Schwarz inequality, $|R_X(\\tau)| = |\\mathbb{E}[X(t)X(t+\\tau)]| \\le \\sqrt{\\mathbb{E}[X^2(t)]\\mathbb{E}[X^2(t+\\tau)]} = R_X(0)$. The maximum correlation always occurs at zero lag $\\tau = 0$, representing average total power.",
        "<strong>Even Symmetry:</strong> Setting $u = t + \\tau$: $R_X(-\\tau) = \\mathbb{E}[X(u)X(u-\\tau)] = \\mathbb{E}[X(t+\\tau)X(t)] = R_X(\\tau)$. The autocorrelation function is universally real and even.",
        "<strong>Positive Semi-Definiteness:</strong> For any coefficients $a_1, \\dots, a_n$ and time points $t_1, \\dots, t_n$, $\\mathbb{E}\\left[\\left(\\sum a_i X(t_i)\\right)^2\\right] = \\sum_{i,j} a_i a_j R_X(t_i - t_j) \\ge 0$, guaranteeing non-negative Fourier spectrum."
    ],
    r"$$R_X(0) = \mathbb{E}[X^2(t)] \ge |R_X(\tau)|, \qquad R_X(-\tau) = R_X(\tau), \qquad \sum_{i,j} c_i c_j R_X(t_i - t_j) \ge 0$$",
    "Acoustic echo reflection: the sound waveform correlates most strongly with itself at zero delay (τ = 0); delayed echoes have strictly lower correlation amplitude.",
    "Assuming any even function can serve as an autocorrelation function! R_X(τ) must be positive semi-definite (its Fourier transform S_X(ω) must be non-negative everywhere). A function like a square pulse is even but has negative Fourier lobes!"
))

# Card 32303: The Wiener-Khinchin Theorem & PSD
svg_32303 = [
    # Time domain: R_X(τ)
    box(15, 25, 85, 80, "Time Domain\nAutocorrelation\nR_X(τ)\nEven, peak at 0", "#f8fafc", 8),
    P("M 25,90 Q 57,45 60,45 Q 63,45 95,90", fill="none", w=1.6),

    # Bidirectional Fourier bridge
    V(103, 55, 137, 55, 1.8), N(120, 48, "Fourier F", 7.5, w="bold"),
    V(137, 75, 103, 75, 1.8), N(120, 85, "Inverse F^{-1}", 7.5, w="bold"),

    # Frequency domain: S_X(ω)
    box(140, 25, 85, 80, "Frequency Domain\nPower Spectral\nDensity S_X(ω)\nS_X(ω) ≥ 0 ∀ω", "#f1f5f9", 8),
    P("M 150,90 Q 182,45 185,45 Q 188,45 220,90", fill="none", w=1.6),

    N(120, 122, "Average Total Power: E[X²] = R_X(0) = (1/2π) ∫ S_X(ω) dω", 8),
    N(120, 138, "Wiener-Khinchin Theorem: PSD S_X(ω) is the Fourier transform of autocorrelation R_X(τ); S_X(ω) ≥ 0", 8.5)
]
CARDS.append(make_stoma_card(
    23, 3, "SPECTRAL DENSITY",
    "The Wiener-Khinchin Theorem & Power Spectral Density",
    svg_32303,
    "The power spectral density S_X(ω) and autocorrelation R_X(τ) form an exact Fourier transform pair",
    [
        "<strong>Wiener-Khinchin Formulation:</strong> For a WSS process, the Power Spectral Density (PSD) $S_X(\\omega)$ is the Fourier transform of the autocorrelation function: $S_X(\\omega) = \\int_{-\\infty}^\\infty R_X(\\tau) e^{-j\\omega \\tau} d\\tau$.",
        "<strong>Non-Negativity Axiom:</strong> The PSD represents physical power distribution across frequencies and is strictly non-negative: $S_X(\\omega) \\ge 0$ for all $\\omega \\in \\mathbb{R}$.",
        "<strong>Total Power Conservation:</strong> The inverse Fourier transform evaluates autocorrelation: $R_X(\\tau) = \\frac{1}{2\\pi} \\int_{-\\infty}^\\infty S_X(\\omega) e^{j\\omega \\tau} d\\omega$. Evaluating at lag $\\tau = 0$ yields the average total power: $\\mathbb{E}[X^2(t)] = R_X(0) = \\frac{1}{2\\pi} \\int_{-\\infty}^\\infty S_X(\\omega) d\\omega$."
    ],
    r"$$S_X(\omega) = \int_{-\infty}^\infty R_X(\tau) e^{-j\omega \tau} d\tau \ge 0, \qquad R_X(\tau) = \frac{1}{2\pi} \int_{-\infty}^\infty S_X(\omega) e^{j\omega \tau} d\omega$$",
    "Optical prism spectrometer: dispersing white light into its spectral color frequencies reveals the power content at each wavelength band.",
    "Forgetting the 1/(2π) factor in the inverse Fourier transform! When integrating S_X(ω) over angular frequency dω to compute total power, omitting 1/(2π) inflates the calculated power by a factor of ~6.28!"
))

# Card 32304: Random Harmonic Processes
svg_32304 = [
    # Sinusoidal waveforms with phase shift
    AX(25, 115, 215, 25),
    N(220, 115, "t", 8), N(20, 22, "X(t)", 8),
    P("M 25,70 Q 55,25 85,70 Q 115,115 145,70 Q 175,25 205,70", fill="none", w=1.6),
    P("M 25,45 Q 55,90 85,45 Q 115,0 145,45 Q 175,90 205,45", fill="none", w=1.2, dash="3 3"),
    # Phase requirement box
    box(25, 12, 105, 24, "X(t) = A cos(ω_0 t + Θ)\nΘ ~ Uniform[-π, π]", "#f1f5f9", 7.5, bold=True),
    # PSD delta spikes on right
    box(145, 12, 75, 35, "PSD: Two Dirac Deltas\nS_X(ω) = (π E[A²]/2) ×\n[δ(ω-ω_0) + δ(ω+ω_0)]", "#ffffff", 6.8),
    N(120, 138, "Random harmonic process: WSS iff phase Θ is uniformly distributed over 2π; R_X(τ) = (E[A²]/2) cos(ω_0 τ)", 8.5)
]
CARDS.append(make_stoma_card(
    23, 4, "HARMONIC PROCESSES",
    "Random Harmonic Processes & Uniform Phase Necessity",
    svg_32304,
    "A sinusoidal process X(t) = A cos(ω_0 t + Θ) is WSS if and only if phase Θ is uniformly distributed over a full 2π interval",
    [
        "<strong>Harmonic Process Model:</strong> Consider $X(t) = A \\cos(\\omega_0 t + \\Theta)$ where amplitude $A$ and phase $\\Theta$ are independent, and $\\omega_0$ is carrier frequency. For $X(t)$ to be WSS, its mean and autocorrelation must be time-invariant.",
        "<strong>Uniform Phase Requirement:</strong> The expected mean is $\\mathbb{E}[X(t)] = \\mathbb{E}[A]\\mathbb{E}[\\cos(\\omega_0 t + \\Theta)]$. This is constant (and equal to 0) for all $t$ if and only if $\\Theta \\sim \\text{Uniform}[-\\pi, \\pi]$ (or any length $2\\pi$ interval).",
        "<strong>Pure Periodic Autocorrelation & PSD Spikes:</strong> When $\\Theta \\sim \\text{Unif}[-\\pi, \\pi]$, $R_X(\\tau) = \\frac{\\mathbb{E}[A^2]}{2} \\cos(\\omega_0 \\tau)$, which does not decay to zero as $\\tau \\to \\infty$. Its PSD consists of two discrete Dirac delta functions at $\\pm \\omega_0$: $S_X(\\omega) = \\frac{\\pi \\mathbb{E}[A^2]}{2}[\\delta(\\omega - \\omega_0) + \\delta(\\omega + \\omega_0)]$."
    ],
    r"$$R_X(\tau) = \frac{\mathbb{E}[A^2]}{2} \cos(\omega_0 \tau) \iff \Theta \sim \text{Unif}[-\pi, \pi]; \quad S_X(\omega) = \frac{\pi \mathbb{E}[A^2]}{2} [\delta(\omega - \omega_0) + \delta(\omega + \omega_0)]$$",
    "Unsynchronized AC power generator: randomly starting the generator sets a random initial rotor angle, making the voltage waveform stationary to an outside observer.",
    "Assuming X(t) = cos(ω_0 t) without random phase is WSS! A deterministic cosine has E[X(t)] = cos(ω_0 t), which oscillates with time t. It is NOT stationary; random phase uniform over [-π, π] is strictly required!"
))

# Card 32305: LTI System Filtering of WSS Processes
svg_32305 = [
    # Input X(t)
    box(15, 45, 55, 38, "WSS Input\nX(t)\nPSD S_X(ω)", "#ffffff", 8),
    V(70, 64, 98, 64, 1.8),
    # LTI Filter box
    box(98, 38, 48, 52, "LTI Filter\nH(ω)\nh(t)", "#f1f5f9", 8.5, bold=True),
    V(146, 64, 174, 64, 1.8),
    # Output Y(t)
    box(174, 45, 55, 38, "WSS Output\nY(t)\nPSD S_Y(ω)", "#ffffff", 8),

    # Formulas below
    N(120, 108, "S_Y(ω) = |H(ω)|² S_X(ω)", 9, w="bold"),
    N(120, 122, "R_Y(τ) = R_X(τ) * h(τ) * h(-τ)", 8),
    N(120, 138, "LTI filtering: output PSD is scaled by filter power gain |H(ω)|²; white noise through RC yields exponential ACF", 8.5)
]
CARDS.append(make_stoma_card(
    23, 5, "LTI FILTERING",
    "LTI Filtering of WSS Processes & Power Transfer",
    svg_32305,
    "Passing a WSS process through an LTI filter scales its PSD by |H(ω)|² and convolves autocorrelation with h(τ)*h(-τ)",
    [
        "<strong>Output Stationarity:</strong> When a WSS process $X(t)$ is applied to a stable LTI system with impulse response $h(t)$, the output $Y(t) = X(t) * h(t) = \\int_{-\\infty}^\\infty h(s)X(t-s)ds$ is also Wide-Sense Stationary.",
        "<strong>Power Spectral Transfer Law:</strong> The output PSD satisfies the fundamental multiplicative relationship: $S_Y(\\omega) = |H(\\omega)|^2 S_X(\\omega)$, where $|H(\\omega)|^2$ is the filter power transfer function.",
        "<strong>RC Low-Pass Filter Benchmark:</strong> When white noise $W(t)$ with PSD $S_W(\\omega) = N_0/2$ drives an RC filter $H(\\omega) = \\frac{1}{1 + j\\omega RC}$, the output PSD is $S_Y(\\omega) = \\frac{N_0/2}{1 + (\\omega RC)^2}$, yielding exponential autocorrelation $R_Y(\\tau) = \\frac{N_0}{4RC} e^{-|\\tau|/RC}$."
    ],
    r"$$S_Y(\omega) = |H(\omega)|^2 S_X(\omega), \qquad R_Y(\tau) = R_X(\tau) * h(\tau) * h(-\tau), \qquad \mathbb{E}[Y^2(t)] = \frac{1}{2\pi}\int_{-\infty}^\infty |H(\omega)|^2 S_X(\omega) d\omega$$",
    "Audio equalizer bass booster: multiplying the incoming sound spectrum by an amplification curve |H(ω)|² reshapes the acoustic power density without altering stationarity.",
    "Using H(ω) instead of |H(ω)|² for power spectral density! PSD represents power (quadratic in amplitude), so it scales with the magnitude-squared |H(ω)|², not the linear frequency response H(ω)."
))

# Card 32306: Mean-Ergodicity & Slutsky’s Integral Test
svg_32306 = [
    # Coordinate axes
    AX(25, 115, 215, 25),
    N(220, 115, "T", 8), N(20, 22, "Var(μ̂_T)", 8),
    # Variance decay curve
    P("M 35,35 Q 65,85 120,105 T 215,114", fill="none", w=2.0),
    L(25, 114, 215, 114, 1.0, d="2 2"),
    N(180, 104, "Var → 0 (Ergodic!)", 8, w="bold"),
    # Slutsky condition box
    box(25, 15, 120, 28, "Slutsky's Mean-Ergodicity Test:\nlim_{T→∞} (1/T) ∫_0^{2T} (1 - τ/2T) C_X(τ) dτ = 0", "#f1f5f9", 7),
    N(120, 138, "Mean-ergodicity: time average (1/2T) ∫ X(t) dt converges in L² to ensemble mean μ iff variance collapses to 0", 8.5)
]
CARDS.append(make_stoma_card(
    23, 6, "ERGODICITY OF PROCESSES",
    "Mean-Ergodicity & Slutsky’s Integral Condition",
    svg_32306,
    "A process is mean-ergodic if its temporal average converges in mean-square to the ensemble mean as time horizon T → ∞",
    [
        "<strong>Temporal Mean Estimator:</strong> For a WSS process, the time average over $[-T, T]$ is $\\hat{\\mu}_T = \\frac{1}{2T} \\int_{-T}^T X(t) dt$. By linearity of expectation, $\\mathbb{E}[\\hat{\\mu}_T] = \\mu$, making $\\hat{\\mu}_T$ an unbiased estimator of ensemble mean $\\mu$.",
        "<strong>Variance Decomposition & Slutsky’s Condition:</strong> The variance is $\\operatorname{Var}(\\hat{\\mu}_T) = \\frac{1}{T} \\int_0^{2T} \\left(1 - \\frac{\\tau}{2T}\\right) C_X(\\tau) d\\tau$. The process is mean-ergodic in mean-square ($\\hat{\\mu}_T \\xrightarrow{L^2} \\mu$) if and only if $\\lim_{T \\to \\infty} \\operatorname{Var}(\\hat{\\mu}_T) = 0$.",
        "<strong>Sufficient Covariance Decay Condition:</strong> If the autocovariance decays asymptotically to zero, $\\lim_{\\tau \\to \\infty} C_X(\\tau) = 0$ (or $\\int_0^\\infty |C_X(\\tau)| d\\tau < \\infty$), then by the dominated convergence theorem $\\operatorname{Var}(\\hat{\\mu}_T) \\to 0$, guaranteeing mean-ergodicity."
    ],
    r"$$\hat{\mu}_T = \frac{1}{2T}\int_{-T}^T X(t) dt \xrightarrow{L^2} \mu \iff \lim_{T \to \infty} \frac{1}{T}\int_0^{2T}\left(1 - \frac{\tau}{2T}\right) C_X(\tau) d\tau = 0$$",
    "Measuring ocean water salinity: taking water samples continuously across a single 10-year voyage gives the exact global ocean mean salinity because water parcels mix and decorrelate over time.",
    "Assuming all WSS processes are mean-ergodic! Consider X(t) = A where A ~ N(0, 1) is a single random variable frozen across all time. It is WSS with C_X(τ) = 1, but μ̂_T = A ≠ 0 for any single realization, so Var(μ̂_T) = 1 does not decay to 0!"
))

if __name__ == "__main__":
    save_stoma_cards(CARDS)
    print("Successfully generated 12 cards for StoMA Topics 22 & 23!")
