"""Build StoMA Topics 26 & 27 (Cards 32601 to 32706).
Dual-coding photographic plates with pure black-and-white vector diagrams.
"""
import sys, os
sys.path.append(os.path.dirname(__file__))
from stoma_lib import (
    T, N, L, V, P, C, R, E, PG, AX, box, svg, make_stoma_card, save_stoma_cards
)

CARDS = []

# ==============================================================================
# TOPIC 26: MARTINGALES & OPTIONAL STOPPING THEOREM (32601 - 32606)
# ==============================================================================

# Card 32601: Filtrations & Martingale Definitions
svg_32601 = [
    # Information filtration cones
    P("M 25,65 L 75,35 L 75,95 Z", fill="#f8fafc", w=1.2),
    N(50, 65, "F_0", 8),
    P("M 75,65 L 135,25 L 135,105 Z", fill="#f1f5f9", w=1.2),
    N(105, 65, "F_1", 8),
    P("M 135,65 L 205,15 L 205,115 Z", fill="#ffffff", w=1.2),
    N(170, 65, "F_2", 8),

    # Martingale horizontal trajectory
    L(25, 65, 205, 65, 2.0),
    N(175, 58, "E[M_{n+1}|F_n] = M_n", 7.5, w="bold"),
    # Submartingale (upward)
    P("M 25,65 Q 115,65 205,30", fill="none", w=1.4, dash="3 3"),
    N(175, 24, "Sub (≥)", 7),
    # Supermartingale (downward)
    P("M 25,65 Q 115,65 205,100", fill="none", w=1.4, dash="2 2"),
    N(175, 108, "Super (≤)", 7),

    N(120, 138, "Martingales model fair games: zero drift given history F_n; constant expectation E[M_n] = E[M_0]", 8.5)
]
CARDS.append(make_stoma_card(
    26, 1, "MARTINGALE FOUNDATIONS",
    "Filtrations & The Three Martingale Definitions",
    svg_32601,
    "Martingales represent fair games where the conditional expectation of future value given all past history equals current value",
    [
        "<strong>Filtration & Adapted Process:</strong> A filtration $\\mathbb{F} = \\{\\mathcal{F}_n\\}_{n \\ge 0}$ models increasing historical information over time: $\\mathcal{F}_0 \\subseteq \\mathcal{F}_1 \\subseteq \\dots \\subseteq \\mathcal{F}$. A process $M_n$ is adapted if its value is known by time $n$ ($M_n \\in \\mathcal{F}_n$).",
        "<strong>The Three Drift Regimes:</strong> An integrable adapted process $M_n$ satisfies: (1) **Martingale** (fair game) if $\\mathbb{E}[M_{n+1} \\mid \\mathcal{F}_n] = M_n$; (2) **Submartingale** (favorable game) if $\\mathbb{E}[M_{n+1} \\mid \\mathcal{F}_n] \\ge M_n$; (3) **Supermartingale** (unfavorable game) if $\\mathbb{E}[M_{n+1} \\mid \\mathcal{F}_n] \\le M_n$.",
        "<strong>Conservation of Expected Value:</strong> By the tower property of conditional expectation, every martingale preserves its unconditional expectation across all time: $\\mathbb{E}[M_n] = \\mathbb{E}[\\mathbb{E}[M_n \\mid \\mathcal{F}_0]] = \\mathbb{E}[M_0]$."
    ],
    r"$$\mathbb{E}[M_{n+1} \mid \mathcal{F}_n] = M_n \implies \mathbb{E}[M_n] = \mathbb{E}[M_0] \quad \forall n \ge 0$$",
    "Fair casino betting bankroll: in a fair game without house edge, your expected wealth tomorrow given everything you know today equals exactly what you hold in your pocket right now.",
    "Confusing Submartingale and Supermartingale signs! A *sub*martingale has upward drift (E[X_{n+1}|F_n] >= X_n), while a *super*martingale has downward drift (E[X_{n+1}|F_n] <= X_n). Remember: sub = 'subterranean floor that pushes up'!"
))

# Card 32602: Canonical Martingale Families
svg_32602 = [
    # 4 Quadrants of Canonical Martingales
    R(16, 20, 96, 48, "#f8fafc", 1.4),
    N(64, 34, "1. Linear Walk", 8.5, w="bold"),
    N(64, 48, "M_n = S_n - n μ", 8),
    N(64, 60, "(E[X_i] = μ)", 7),

    R(128, 20, 96, 48, "#f1f5f9", 1.4),
    N(176, 34, "2. Variance Martingale", 8.5, w="bold"),
    N(176, 48, "M_n = S_n² - n σ²", 8),
    N(176, 60, "(Zero-mean steps)", 7),

    R(16, 74, 96, 48, "#ffffff", 1.4),
    N(64, 88, "3. Exponential Wald", 8.5, w="bold"),
    N(64, 102, "M_n = e^{θ S_n} / (M_X(θ))ⁿ", 7.5),
    N(64, 114, "(Non-zero θ)", 7),

    R(128, 74, 96, 48, "#f8fafc", 1.4),
    N(176, 88, "4. Doob’s Martingale", 8.5, w="bold"),
    N(176, 102, "M_n = E[Y | F_n]", 8),
    N(176, 114, "(Lévy Forward Theorem)", 7),

    N(120, 138, "Canonical martingales: linear walk, variance compensator, exponential Wald, and Doob conditional expectations", 8.5)
]
CARDS.append(make_stoma_card(
    26, 2, "CANONICAL MARTINGALES",
    "Canonical Martingale Families & Compensators",
    svg_32602,
    "Standard martingales neutralize drift via compensators, enabling exact evaluation of stopping times and tail bounds",
    [
        "<strong>Linear & Variance Compensated Walks:</strong> For i.i.d. increments $X_i$ with mean $\\mu$ and variance $\\sigma^2$: (1) $M_n = S_n - n\\mu$ is a zero-mean martingale; (2) When $\\mu = 0$, $M_n = S_n^2 - n\\sigma^2$ is a variance martingale, neutralizing quadratic growth via compensator $-n\\sigma^2$.",
        "<strong>Exponential Wald Martingale:</strong> For any $\\theta$ where MGF $M_X(\\theta) = \\mathbb{E}[e^{\\theta X}] < \\infty$, the geometric product $M_n = \\frac{e^{\\theta S_n}}{(M_X(\\theta))^n}$ is a positive martingale with $\\mathbb{E}[M_n] = 1$, vital for large deviations and ruin probabilities.",
        "<strong>Doob’s Martingale Construction:</strong> For any integrable random variable $Y$ with $\\mathbb{E}[|Y|] < \\infty$, the sequence of progressive conditional estimates $M_n = \\mathbb{E}[Y \\mid \\mathcal{F}_n]$ is automatically a martingale. As information accumulates ($n \\to \\infty$), $M_n \\to Y$ almost surely."
    ],
    r"$$S_n - n\mu, \qquad S_n^2 - n\sigma^2, \qquad \frac{e^{\theta S_n}}{(M_X(\theta))^n}, \qquad M_n = \mathbb{E}[Y \mid \mathcal{F}_n]$$",
    "Progressive criminal detective investigation: Doob's martingale E[Y | F_n] represents the detective's current estimate of guilt as evidence F_n steadily unfolds, converging to true verdict Y.",
    "Assuming S_n² is a martingale! For zero-mean random walks, E[S_{n+1}² | F_n] = S_n² + σ² > S_n², making S_n² a strict *submartingale*. One must subtract the compensator nσ² to form a true martingale!"
))

# Card 32603: Stopping Times & The Stability Theorem
svg_32603 = [
    # Stochastic process path reaching stopping time τ
    AX(25, 115, 215, 25),
    N(220, 115, "n", 8),
    # Stopping boundary line τ
    L(110, 25, 110, 115, 1.4, d="4 4"),
    N(110, 18, "Stopping Time τ", 8, w="bold"),
    # Path before stopping
    P("M 25,75 L 45,55 L 65,85 L 85,45 L 110,60", fill="none", w=1.8),
    C(110, 60, 4, fill="#000000"),
    # Frozen path after stopping
    L(110, 60, 205, 60, 2.0, d="2 2"),
    N(160, 52, "Frozen: M_{n ∧ τ}", 8, w="bold"),
    # Information criterion box
    box(25, 15, 75, 26, "{τ ≤ n} ∈ F_n\n(No crystal ball!)", "#f1f5f9", 7),
    N(120, 138, "Stopping times: decision to stop depends only on past history; stopped process M_{n ∧ τ} remains a martingale", 8.5)
]
CARDS.append(make_stoma_card(
    26, 3, "STOPPING TIMES",
    "Stopping Times & The Stopped Martingale Theorem",
    svg_32603,
    "Stopping times require non-anticipating rules; freezing a martingale at stopping time τ preserves the martingale property",
    [
        "<strong>Formal Stopping Time Axiom:</strong> A random variable $\\tau \\in \\{0, 1, 2, \\dots\\} \\cup \\{\\infty\\}$ is a stopping time with respect to filtration $\\mathbb{F}$ if the event of stopping by time $n$ is completely determined by history up to time $n$: $\\{\\tau \\le n\\} \\in \\mathcal{F}_n$ for all $n \\ge 0$.",
        "<strong>No Crystal Ball Principle:</strong> A valid stopping rule cannot look into the future. For example, 'stop at the first time wealth hits $\\$100$' is a stopping time; 'stop one step before the maximum wealth' is NOT a stopping time.",
        "<strong>Stability Under Stopping:</strong> If $M_n$ is a martingale and $\\tau$ is a stopping time, the stopped process $M_n^\\tau = M_{n \\wedge \\tau}$ is also a martingale. In particular, $\\mathbb{E}[M_{n \\wedge \\tau}] = \\mathbb{E}[M_0]$ for every finite truncation step $n$."
    ],
    r"$$\{\tau \le n\} \in \mathcal{F}_n \quad \forall n \ge 0 \implies M_{n \wedge \tau} \text{ is a Martingale}, \quad \mathbb{E}[M_{n \wedge \tau}] = \mathbb{E}[M_0]$$",
    "Automatic thermostat emergency shutoff: the heater cuts off the instant temperature exceeds 100°C, a decision based solely on current and past thermometer readings.",
    "Treating the last time a state is visited as a stopping time! The event 'last visit to 0' requires observing the entire infinite future to ensure the process never returns. It is NOT a stopping time!"
))

# Card 32604: The Optional Stopping Theorem (OST)
svg_32604 = [
    # Three regulatory pillars of OST
    R(16, 25, 64, 85, "#f8fafc", 1.4),
    N(48, 38, "Condition 1", 8.5, w="bold"),
    N(48, 52, "Bounded Time", 8, w="bold"),
    N(48, 68, "τ ≤ C a.s.", 8),
    N(48, 85, "Guaranteed finite", 7),
    N(48, 98, "deadline", 7),

    R(88, 25, 64, 85, "#f1f5f9", 1.4),
    N(120, 38, "Condition 2", 8.5, w="bold"),
    N(120, 52, "Bounded Path", 8, w="bold"),
    N(120, 68, "|M_{n∧τ}| ≤ K", 8),
    N(120, 85, "τ < ∞ a.s.", 7),
    N(120, 98, "Two-sided barrier", 7),

    R(160, 25, 64, 85, "#ffffff", 1.4),
    N(192, 38, "Condition 3", 8.5, w="bold"),
    N(192, 52, "Finite E[τ] & Steps", 8, w="bold"),
    N(192, 68, "E[τ] < ∞", 8),
    N(192, 85, "|ΔM_n| ≤ c", 7.5),
    N(192, 98, "Wald condition", 7),

    N(120, 122, "OST: E[M_τ] = E[M_0] if ANY of these 3 conditions holds!", 8.5, w="bold"),
    N(120, 138, "Optional Stopping Theorem: guarantees E[M_τ] = E[M_0]; prevents fraudulent gambling doubling schemes", 8.5)
]
CARDS.append(make_stoma_card(
    26, 4, "OPTIONAL STOPPING",
    "The Optional Stopping Theorem (OST) & Conditions",
    svg_32604,
    "The Optional Stopping Theorem equates E[M_τ] = E[M_0] under any of three standard regularity conditions",
    [
        "<strong>Theorem Statement:</strong> Let $M_n$ be a martingale and $\\tau$ a stopping time. Then the expected stopped value equals the initial value, $\\mathbb{E}[M_\\tau] = \\mathbb{E}[M_0]$, if ANY ONE of the following sufficient conditions holds: (1) $\\tau$ is bounded almost surely ($\\tau \\le C$); (2) $\\tau < \\infty$ a.s. and the stopped process is bounded ($|M_{n \\wedge \\tau}| \\le K$); or (3) $\\mathbb{E}[\\tau] < \\infty$ and step increments are uniformly bounded ($|M_{n+1} - M_n| \\le c$).",
        "<strong>The Martingale Doubling Fallacy:</strong> In a fair coin game, bet $\\$1, \\$2, \\$4, \\dots$ until the first win at $\\tau$. At stopping, profit $M_\\tau = +1$ with probability 1! Yet $\\mathbb{E}[M_0] = 0$. OST fails here because $\\mathbb{E}[\\tau] = \\infty$ and wealth $M_n$ drops without bound ($-\\infty$).",
        "<strong>Dominated Convergence Backbone:</strong> The proof relies on taking the limit of the truncated martingale identity $\\mathbb{E}[M_{n \\wedge \\tau}] = \\mathbb{E}[M_0]$ as $n \\to \\infty$, which requires uniform integrability or dominated convergence to exchange expectation and limit."
    ],
    r"$$\mathbb{E}[M_\tau] = \mathbb{E}[M_0] \quad \text{if } \tau \le C \quad \text{or} \quad |M_{n \wedge \tau}| \le K \quad \text{or} \quad (\mathbb{E}[\tau] < \infty \text{ and } |\Delta M| \le c)$$",
    "Casino betting limit security: table limits prevent the St. Petersburg martingale doubling strategy by enforcing a hard upper bound K on bankroll bets, preserving OST fairness.",
    "Applying OST without checking regulatory conditions! In the classic doubling strategy, M_τ = 1 with probability 1, but E[M_0] = 0. Blindly applying OST produces 1 = 0! Always verify one of the three regulatory conditions!"
))

# Card 32605: OST Applications: Wald’s Identities & Gambler’s Ruin
svg_32605 = [
    # Gambler's ruin with two absorbing boundaries
    AX(25, 115, 215, 25),
    N(220, 115, "n", 8),
    # Upper boundary a
    L(25, 45, 215, 45, 1.2, d="3 3"), N(200, 40, "+a (Win)", 8, w="bold"),
    # Lower boundary -b
    L(25, 95, 215, 95, 1.2, d="3 3"), N(200, 102, "-b (Ruin)", 8, w="bold"),
    # Walk trajectory hitting boundary
    P("M 25,70 L 45,60 L 65,75 L 85,55 L 110,65 L 130,45", fill="none", w=1.8),
    C(130, 45, 3, fill="#000000"), N(130, 35, "Hit +a!", 8),

    # Formulas box
    box(25, 12, 160, 26, "OST on S_τ: p_a · a - (1-p_a) · b = 0  ⇒  p_a = b / (a + b)\nOST on S_τ² - τ: E[τ] = a · b  (Fair coin)", "#f1f5f9", 7.2, bold=True),
    N(120, 138, "OST effortlessly solves boundary hitting problems: exit probability p_a = b/(a+b) and duration E[τ] = ab", 8.5)
]
CARDS.append(make_stoma_card(
    26, 5, "OST APPLICATIONS",
    "OST Applications: Gambler’s Ruin & Wald’s Identities",
    svg_32605,
    "Applying OST to linear and quadratic martingales resolves gambler's ruin probabilities and expected exit durations in one step",
    [
        "<strong>Gambler’s Ruin Exit Probability:</strong> For a symmetric random walk starting at 0 with absorption at $+a$ or $-b$, $M_n = S_n$ is a bounded martingale up to stopping time $\\tau$. By OST: $\\mathbb{E}[S_\\tau] = p_a(a) + (1 - p_a)(-b) = S_0 = 0 \\implies p_a = \\frac{b}{a+b}$.",
        "<strong>Expected Game Duration via Variance Martingale:</strong> Applying OST to the variance martingale $M_n = S_n^2 - n$ with stopped value $S_\\tau^2$: $\\mathbb{E}[S_\\tau^2 - \\tau] = 0 \\implies \\mathbb{E}[\\tau] = \\mathbb{E}[S_\\tau^2] = p_a(a^2) + (1-p_a)(-b)^2 = \\frac{b}{a+b}a^2 + \\frac{a}{a+b}b^2 = ab$.",
        "<strong>Wald’s First & Second Identities:</strong> When $\\tau$ is a stopping time with $\\mathbb{E}[\\tau] < \\infty$, applying OST to compensated martingales immediately rederives Wald's equations: $\\mathbb{E}[S_\\tau] = \\mathbb{E}[\\tau]\\mathbb{E}[X]$ and $\\mathbb{E}[(S_\\tau - \\tau\\mu)^2] = \\sigma^2 \\mathbb{E}[\\tau]$ without renewal convolutions."
    ],
    r"$$\mathbb{E}[S_\tau] = 0 \implies p_a = \frac{b}{a+b}; \qquad \mathbb{E}[S_\tau^2 - \tau] = 0 \implies \mathbb{E}[\tau] = ab \quad (\text{Fair Random Walk})$$",
    "A/B testing early stopping rule: monitoring testing metrics with martingales guarantees exact false positive error rate control without p-value snooping inflation.",
    "Applying E[τ] = ab to biased walks! The identity E[S_τ² - τ] = 0 holds ONLY for zero-mean symmetric walks (p = 1/2). For biased walks (p ≠ 1/2), you must use the exponential Wald martingale exp(θ S_n) / (M(θ))^n instead!"
))

# Card 32606: Doob’s Maximal Inequality & Azuma-Hoeffding
svg_32606 = [
    # Running maximum envelope
    AX(25, 115, 215, 25),
    N(220, 115, "n", 8),
    # Threshold λ
    L(25, 45, 215, 45, 1.4, d="3 3"), N(200, 40, "Level λ", 8, w="bold"),
    # Submartingale path
    P("M 25,100 L 50,85 L 75,90 L 100,60 L 125,70 L 150,42 L 175,55 L 205,35", fill="none", w=1.8),
    C(150, 42, 3, fill="#000000"), N(150, 32, "Exceeds λ!", 7.5),
    # Inequalities box
    box(25, 12, 190, 26, "Doob: P(max_{k≤n} X_k ≥ λ) ≤ E[X_n] / λ   (Non-negative submartingale)\nAzuma-Hoeffding: P(|M_n - M_0| ≥ t) ≤ 2 exp(-t² / (2 Σ c_i²))", "#ffffff", 7),
    N(120, 138, "Doob's inequality bounds the entire running trajectory using only terminal expectation E[X_n]", 8.5)
]
CARDS.append(make_stoma_card(
    26, 6, "MAXIMAL INEQUALITIES",
    "Doob’s Maximal Inequality & Azuma-Hoeffding",
    svg_32606,
    "Doob's inequality bounds the supremum of an entire sample path using only the terminal expectation at time n",
    [
        "<strong>Doob’s Submartingale Maximal Inequality:</strong> Let $\{X_n\}$ be a non-negative submartingale. For any threshold $\\lambda > 0$: $P\\left(\\max_{0 \\le k \\le n} X_k \\ge \\lambda\\right) \\le \\frac{\\mathbb{E}[X_n]}{\\lambda}$. This remarkably bounds the entire running maximum envelope using only the final time-$n$ expectation.",
        "<strong>Doob’s $L^p$ Maximal Inequality:</strong> For a martingale $M_n$ with $p > 1$: $\\mathbb{E}\\left[\\left(\\max_{0 \\le k \\le n} |M_k|\\right)^p\\right] \\le \\left(\\frac{p}{p-1}\\right)^p \\mathbb{E}[|M_n|^p]$, showing the running supremum is $L^p$-controlled by terminal value.",
        "<strong>Azuma-Hoeffding Concentration:</strong> If martingale increments are bounded ($|M_k - M_{k-1}| \\le c_k$ a.s.), then $P(|M_n - M_0| \\ge t) \\le 2 \\exp\\left(-\\frac{t^2}{2\\sum_{k=1}^n c_k^2}\\right)$, extending Hoeffding's inequality to dependent stochastic processes."
    ],
    r"$$P\left(\max_{0 \le k \le n} X_k \ge \lambda\right) \le \frac{\mathbb{E}[X_n]}{\lambda}, \qquad P(|M_n - M_0| \ge t) \le 2\exp\left(-\frac{t^2}{2\sum_{k=1}^n c_k^2}\right)$$",
    "Dam flood reservoir control: Doob's maximal inequality guarantees that the maximum water surge over an entire 30-day storm remains within safety levees based only on day-30 expected volume.",
    "Applying Doob's maximal inequality to supermartingales or signed martingales! The classic maximal inequality requires a *non-negative submartingale* (such as |M_n| or M_n^+). For general martingales, apply it to |M_n| or |M_n|^p."
))

# ==============================================================================
# TOPIC 27: CONTINUOUS-TIME MARKOV CHAINS (CTMC) (32701 - 32706)
# ==============================================================================

# Card 32701: Continuous-Time Markov Property & Generator Q
svg_32701 = [
    # State node i with holding time Exp(q_i)
    C(60, 68, 16, fill="#ffffff"), N(60, 71, "State i", 8.5, w="bold"),
    # Holding clock
    box(20, 20, 75, 22, "Holding Time\nT_i ~ Exp(q_i)", "#f8fafc", 7.5, bold=True),
    L(55, 42, 58, 52, 1.2),

    # Transition arrows to j and k
    V(76, 62, 130, 42, 1.8), N(100, 46, "q_{ij}", 8, w="bold"),
    C(145, 38, 14, fill="#f1f5f9"), N(145, 41, "State j", 8),

    V(76, 74, 130, 94, 1.8), N(100, 90, "q_{ik}", 8, w="bold"),
    C(145, 98, 14, fill="#f1f5f9"), N(145, 101, "State k", 8),

    # Generator row-sum zero box
    box(170, 56, 65, 34, "Generator Q:\nq_ii = - Σ_{j≠i} q_{ij}\nQ 1 = 0", "#ffffff", 7, bold=True),
    N(120, 138, "Infinitesimal generator Q: off-diagonals q_{ij} ≥ 0 are rates; diagonals q_{ii} = -q_i make row sums 0", 8.5)
]
CARDS.append(make_stoma_card(
    27, 1, "CTMC GENERATOR",
    "Infinitesimal Generator Q & Exponential Holding Times",
    svg_32701,
    "CTMCs spend Exp(q_i) holding time in state i before jumping to state j with probability q_{ij}/q_i",
    [
        "<strong>Sojourn & Jump Formulation:</strong> In a continuous-time Markov chain, upon entering state $i$, the process remains there for an exponential holding time $T_i \\sim \\text{Exp}(q_i)$ where $q_i = \\sum_{j \\ne i} q_{ij}$. It then transitions to state $j \\ne i$ with jump probability $P_{ij} = \\frac{q_{ij}}{q_i}$.",
        "<strong>Infinitesimal Generator Definition:</strong> The generator matrix $Q = (q_{ij})$ represents transition rates: $q_{ij} = \\lim_{h \\downarrow 0} \\frac{P_{ij}(h) - \\delta_{ij}}{h}$. Thus for small $h$, $P_{ij}(h) = q_{ij} h + o(h)$ for $i \\ne j$, and $P_{ii}(h) = 1 - q_i h + o(h)$.",
        "<strong>Row-Sum Zero Invariant:</strong> Conservation of probability dictates that the diagonal entries must equal the negative sum of off-diagonal entries: $q_{ii} = -q_i = -\\sum_{j \\ne i} q_{ij} \\le 0$, ensuring $Q \\mathbf{1} = \\mathbf{0}$."
    ],
    r"$$q_{ij} = \lim_{h \downarrow 0} \frac{P_{ij}(h)}{h} \ (i \ne j), \qquad q_{ii} = -\sum_{j \ne i} q_{ij}, \qquad Q \mathbf{1} = \mathbf{0}, \qquad T_i \sim \text{Exp}(q_i)$$",
    "Chemical reaction kinetics: an atom vibrates in energy state i until an activation collision occurs after an exponential holding time, jumping to state j with reaction rate q_ij.",
    "Thinking diagonal entries q_{ii} are probabilities! Generator entries q_{ij} are transition *rates* (units 1/time), not probabilities. Diagonals q_{ii} are strictly non-positive (q_{ii} ≤ 0) and can be less than -1!"
))

# Card 32702: Kolmogorov Backward & Forward Differential Equations
svg_32702 = [
    # Backward vs Forward ODE schematic
    R(16, 25, 96, 75, "#f8fafc", 1.4),
    N(64, 38, "Backward Equation", 8.5, w="bold"),
    N(64, 52, "P'(t) = Q P(t)", 8, w="bold"),
    N(64, 68, "Condition on FIRST jump", 7),
    N(64, 82, "at time h: [0, h]", 7),

    R(128, 25, 96, 75, "#f1f5f9", 1.4),
    N(176, 38, "Forward Equation", 8.5, w="bold"),
    N(176, 52, "P'(t) = P(t) Q", 8, w="bold"),
    N(176, 68, "Condition on LAST jump", 7),
    N(176, 82, "at time t: [t, t+h]", 7),

    # Matrix exponential solution
    box(45, 105, 150, 22, "Matrix Exponential Solution: P(t) = e^{Qt} = Σ_{n=0}^∞ (Qt)ⁿ / n!", "#ffffff", 7.5, bold=True),
    N(120, 138, "Kolmogorov equations: Backward P'=QP (first jump) and Forward P'=PQ (last jump) yield P(t) = e^{Qt}", 8.5)
]
CARDS.append(make_stoma_card(
    27, 2, "KOLMOGOROV EQUATIONS",
    "Kolmogorov Backward & Forward Equations & Matrix Exponential",
    svg_32702,
    "Conditioning on the first jump yields Backward ODE P'=QP; conditioning on the last jump yields Forward ODE P'=PQ",
    [
        "<strong>Kolmogorov Backward Equation:</strong> Conditioning on the first transition during $[0, h]$ yields $P_{ij}(t+h) = \\sum_k P_{ik}(h) P_{kj}(t)$. Subtracting $P_{ij}(t)$ and dividing by $h \\to 0$ gives $P'(t) = Q P(t)$ or $P_{ij}'(t) = \\sum_k q_{ik} P_{kj}(t)$. Always valid for all regular CTMCs.",
        "<strong>Kolmogorov Forward Equation:</strong> Conditioning on the final transition during $[t, t+h]$ yields $P_{ij}(t+h) = \\sum_k P_{ik}(t) P_{kj}(h)$, yielding $P'(t) = P(t) Q$ or $P_{ij}'(t) = \\sum_k P_{ik}(t) q_{kj}$. Requires mild regularity conditions to interchange limit and infinite sum.",
        "<strong>Matrix Exponential Solution:</strong> Both differential systems subject to initial condition $P(0) = I$ possess the unique matrix exponential solution: $P(t) = e^{Qt} = \\sum_{n=0}^\\infty \\frac{(Qt)^n}{n!}$ with Chapman-Kolmogorov semigroup property $P(t+s) = P(t)P(s)$."
    ],
    r"$$P'(t) = Q P(t) \quad (\text{Backward}), \qquad P'(t) = P(t) Q \quad (\text{Forward}), \qquad P(t) = e^{Qt} = \sum_{n=0}^\infty \frac{(Qt)^n}{n!}$$",
    "Matrix exponential calculus: just as scalar ODE y' = ay produces y(t) = e^{at}, the matrix vector ODE P'(t) = QP(t) produces operator evolution P(t) = e^{Qt}.",
    "Assuming Forward and Backward equations always hold equally on infinite state spaces! For explosive or non-regular chains, the Backward equation P' = QP always holds, but the Forward equation P' = PQ can fail due to divergent infinite sums!"
))

# Card 32703: Two-State CTMC Transient Dynamics
svg_32703 = [
    # Coordinate axes
    AX(25, 115, 215, 25),
    N(220, 115, "t", 8), N(20, 22, "P_ij(t)", 8),
    # P_11(t) decaying from 1 to stationary limit
    P("M 25,30 Q 75,70 120,74 T 215,75", fill="none", w=2.0),
    N(45, 38, "P_11(t)", 8, w="bold"),
    # P_21(t) rising from 0 to stationary limit
    P("M 25,115 Q 75,80 120,76 T 215,75", fill="none", w=1.6, dash="3 3"),
    N(45, 105, "P_21(t)", 8),
    # Steady state limit line
    L(25, 75, 215, 75, 1.2, d="4 4"),
    N(175, 68, "Limit π_1 = μ / (λ + μ)", 8, w="bold"),
    # Analytical formula box
    box(25, 12, 115, 20, "Relaxation Rate: α = λ + μ", "#f1f5f9", 7.5),
    N(120, 138, "Two-state CTMC: P_11(t) = μ/(λ+μ) + [λ/(λ+μ)] e^{-(λ+μ)t}; decays exponentially to steady state", 8.5)
]
CARDS.append(make_stoma_card(
    27, 3, "TWO-STATE TRANSIENT",
    "Two-State CTMC Transient Solutions & Relaxation Rate",
    svg_32703,
    "The 2-state CTMC relaxes exponentially to equilibrium at spectral rate α = λ + μ: P_11(t) = μ/(λ+μ) + [λ/(λ+μ)]e^{-(λ+μ)t}",
    [
        "<strong>Two-State Machine Failure Model:</strong> Let state 1 be Operating (failure rate $\\lambda$) and state 2 be Broken (repair rate $\\mu$). The generator matrix is $Q = \\begin{pmatrix} -\\lambda & \\lambda \\\\ \\mu & -\\mu \\end{pmatrix}$.",
        "<strong>First-Order Differential Solution:</strong> The Kolmogorov forward equation yields $\\frac{d P_{11}(t)}{dt} = \\mu - (\\lambda + \\mu) P_{11}(t)$. With initial condition $P_{11}(0) = 1$, solving via integrating factor $e^{(\\lambda+\\mu)t}$ yields $P_{11}(t) = \\frac{\\mu}{\\lambda + \\mu} + \\frac{\\lambda}{\\lambda + \\mu} e^{-(\\lambda + \\mu)t}$.",
        "<strong>Spectral Gap & Relaxation Time:</strong> The eigenvalues of $Q$ are $\\lambda_1 = 0$ (stationary mode) and $\\lambda_2 = -(\\lambda + \\mu)$ (decay mode). The spectral gap $\\lambda + \\mu$ defines the relaxation rate, with mixing time $\\tau_{\\text{relax}} = \\frac{1}{\\lambda + \\mu}$."
    ],
    r"$$P_{11}(t) = \frac{\mu}{\lambda + \mu} + \frac{\lambda}{\lambda + \mu} e^{-(\lambda + \mu)t}, \qquad \lim_{t \to \infty} P_{11}(t) = \pi_1 = \frac{\mu}{\lambda + \mu}$$",
    "Light bulb failure and replacement: the probability that the room light is working at time t exponentially settles to the duty cycle μ/(λ+μ).",
    "Thinking relaxation rate is min(λ, μ)! The transient exponent is the *sum* of the transition rates, -(λ + μ)t. Transitions in both directions accelerate convergence toward stationary balance."
))

# Card 32704: Stationary Distributions & Global vs Detailed Balance
svg_32704 = [
    # Balance diagram at node j
    C(120, 65, 18, fill="#ffffff"), N(120, 68, "State j", 9, w="bold"),
    # Influx arrows
    V(45, 35, 104, 55, 1.8), N(65, 38, "π_i q_{ij}", 7.5),
    V(45, 95, 104, 75, 1.8), N(65, 92, "π_k q_{kj}", 7.5),
    # Outflux arrows
    V(136, 55, 195, 35, 1.8), N(175, 38, "π_j q_{ji}", 7.5),
    V(136, 75, 195, 95, 1.8), N(175, 92, "π_j q_{jk}", 7.5),

    # Balance equations
    box(25, 110, 85, 22, "Global: π^T Q = 0^T", "#f8fafc", 7.5, bold=True),
    box(130, 110, 85, 22, "Detailed: π_i q_ij = π_j q_ji", "#f1f5f9", 7.5, bold=True),

    N(120, 138, "Stationary CTMC: global balance π^T Q = 0^T equates total flow in and out; detailed balance holds for reversible chains", 8.5)
]
CARDS.append(make_stoma_card(
    27, 4, "STATIONARY DISTRIBUTIONS",
    "Stationary Distribution π & Global vs Detailed Balance",
    svg_32704,
    "Steady-state distributions satisfy π^T Q = 0; time-reversible chains satisfy pairwise detailed balance π_i q_{ij} = π_j q_{ji}",
    [
        "<strong>Global Balance Invariant:</strong> A probability vector $\\pi$ is stationary for a CTMC if $\\pi^\\top P(t) = \\pi^\\top$ for all $t \\ge 0$. Differentiating at $t=0$ yields $\\pi^\\top Q = \\mathbf{0}^\\top$ subject to $\\sum_i \\pi_i = 1$ and $\\pi_i > 0$.",
        "<strong>Component-wise Inflow = Outflow:</strong> Expanding $\\pi^\\top Q = \\mathbf{0}^\\top$ yields $\\sum_{i \\ne j} \\pi_i q_{ij} = \\pi_j q_j = \\pi_j \\sum_{k \\ne j} q_{jk}$ for every state $j$. Total rate of probability flow entering state $j$ equals total rate leaving state $j$.",
        "<strong>Continuous Detailed Balance:</strong> If a distribution satisfies pairwise detailed balance $\\pi_i q_{ij} = \\pi_j q_{ji}$ for all $i \\ne j$, then summing over $i$ immediately satisfies global balance $\\pi^\\top Q = \\mathbf{0}^\\top$. Reversible CTMCs (like birth-death processes) satisfy detailed balance."
    ],
    r"$$\pi^\top Q = \mathbf{0}^\top, \quad \sum_{i \in S} \pi_i = 1; \qquad \text{Detailed Balance: } \pi_i q_{ij} = \pi_j q_{ji} \implies \pi^\top Q = \mathbf{0}^\top$$",
    "Thermal circuit heat balance: in steady thermal equilibrium, the total heat conductively entering node j equals the total heat dissipating out of node j.",
    "Using π^T Q = π^T instead of π^T Q = 0^T! In DTMC, π^T P = π^T. But in CTMC, generator Q has zero row sums, so the stationary equation is π^T Q = 0^T!"
))

# Card 32705: Continuous-Time Birth-Death Queues (M/M/1 & M/M/c)
svg_32705 = [
    # Queuing chain 0, 1, 2, 3
    C(35, 70, 14, fill="#ffffff"), N(35, 73, "0", 9, w="bold"),
    C(90, 70, 14, fill="#ffffff"), N(90, 73, "1", 9, w="bold"),
    C(145, 70, 14, fill="#ffffff"), N(145, 73, "2", 9, w="bold"),
    C(200, 70, 14, fill="#ffffff"), N(200, 73, "3", 9, w="bold"),

    # Forward arrival rates λ
    P("M 47,60 C 60,45 77,45 80,58", fill="none", w=1.6, ar=True), N(63, 44, "λ", 8),
    P("M 102,60 C 115,45 132,45 135,58", fill="none", w=1.6, ar=True), N(118, 44, "λ", 8),
    P("M 157,60 C 170,45 187,45 190,58", fill="none", w=1.6, ar=True), N(173, 44, "λ", 8),

    # Backward service rates μ
    P("M 78,80 C 65,95 48,95 45,82", fill="none", w=1.6, ar=True), N(63, 102, "μ", 8),
    P("M 133,80 C 120,95 103,95 100,82", fill="none", w=1.6, ar=True), N(118, 102, "2μ", 8),
    P("M 188,80 C 175,95 158,95 155,82", fill="none", w=1.6, ar=True), N(173, 102, "cμ", 8),

    # M/M/1 formula box
    box(30, 12, 180, 24, "M/M/1 Queue: π_n = (1 - ρ) ρⁿ  with  ρ = λ/μ < 1;   E[L] = ρ / (1 - ρ)", "#f1f5f9", 7.5, bold=True),
    N(120, 138, "Continuous birth-death queues: M/M/1 geometric occupancy π_n = (1-ρ)ρⁿ; M/M/c multi-server service rate min(k, c)μ", 8.5)
]
CARDS.append(make_stoma_card(
    27, 5, "BIRTH-DEATH QUEUES",
    "Continuous Birth-Death Processes & M/M/1 / M/M/c Queues",
    svg_32705,
    "Queuing systems model birth-death CTMCs with arrival rate λ and service rates μ_k, yielding geometric steady-state backlogs",
    [
        "<strong>Continuous Birth-Death Model:</strong> A CTMC with state space $\{0, 1, 2, \\dots\}$ where transitions occur only between adjacent states: birth rate $q_{k, k+1} = \\lambda_k$ and death rate $q_{k, k-1} = \\mu_k$. Detailed balance gives $\\pi_k \\lambda_k = \\pi_{k+1} \\mu_{k+1}$.",
        "<strong>M/M/1 Queue Steady State:</strong> With constant arrival rate $\\lambda$ and single server rate $\\mu$, traffic intensity is $\\rho = \\lambda/\\mu < 1$. Detailed balance yields $\\pi_n = \\rho^n \\pi_0$, producing the geometric distribution $\\pi_n = (1 - \\rho)\\rho^n$ with average customer backlog $\\mathbb{E}[L] = \\frac{\\rho}{1 - \\rho}$.",
        "<strong>M/M/c Multi-Server Queue:</strong> With $c$ servers, service rate scales as $\\mu_k = \\min(k, c)\\mu$. Erlang's C formula gives the probability of queuing delay: $P(\\text{Wait} > 0) = \\frac{\\frac{(c\\rho)^c}{c!(1-\\rho)}}{\\sum_{k=0}^{c-1} \\frac{(c\\rho)^k}{k!} + \\frac{(c\\rho)^c}{c!(1-\\rho)}}$ where $\\rho = \\lambda/(c\\mu) < 1$."
    ],
    r"$$\pi_n = (1 - \rho)\rho^n \quad (\text{M/M/1, } \rho = \frac{\lambda}{\mu} < 1); \qquad \mathbb{E}[L] = \frac{\rho}{1 - \rho}, \qquad W = \frac{1}{\mu - \lambda}$$",
    "Supermarket checkout lines: when arrival rate approaches checkout speed (ρ → 1), queue length E[L] explodes to infinity non-linearly.",
    "Applying M/M/1 formulas when ρ ≥ 1! When arrival rate λ exceeds service rate μ (ρ ≥ 1), no stationary distribution exists, and the queue backlog explodes to +∞ with probability 1."
))

# Card 32706: Uniformization (Jensen’s Method)
svg_32706 = [
    # Continuous timeline modulated by Poisson ticks
    L(20, 65, 220, 65, 1.8, ar=True), N(225, 65, "t", 8),
    # Poisson clock ticks
    C(60, 65, 3, fill="#000000"), N(60, 78, "Tick 1", 7),
    C(105, 65, 3, fill="#000000"), N(105, 78, "Tick 2", 7),
    C(160, 65, 3, fill="#000000"), N(160, 78, "Tick 3", 7),
    C(195, 65, 3, fill="#000000"), N(195, 78, "Tick 4", 7),

    # Discrete DTMC matrix K box
    box(25, 15, 190, 34, "Poisson Clock Rate ν ≥ max_i q_i:\nDiscrete Matrix: K = I + (1/ν) Q\nP(t) = Σ_{n=0}^∞ [(νt)ⁿ e^{-νt} / n!] Kⁿ", "#f1f5f9", 7.5, bold=True),

    N(120, 115, "Jensen's method: converts CTMC ODEs into Poisson-randomized DTMC powers Kⁿ", 8),
    N(120, 138, "Uniformization (Jensen's Method): transforms continuous CTMC into a discrete chain K driven by rate-ν Poisson clock", 8.5)
]
CARDS.append(make_stoma_card(
    27, 6, "UNIFORMIZATION",
    "Uniformization (Jensen’s Method) & Poisson Randomization",
    svg_32706,
    "Uniformization converts continuous CTMC transition matrices into Poisson-weighted mixtures of discrete-time powers Kⁿ",
    [
        "<strong>Uniformization Rate Selection:</strong> Let $\\nu \\ge \\max_i q_i < \\infty$ be a uniform rate dominating all state departure rates. Define the discrete-time transition probability matrix $K = I + \\frac{1}{\\nu} Q$.",
        "<strong>Valid DTMC Stochasticity:</strong> Because off-diagonals $K_{ij} = \\frac{q_{ij}}{\\nu} \\ge 0$ and diagonals $K_{ii} = 1 - \\frac{q_i}{\\nu} \\ge 0$ with row sums $\\sum_j K_{ij} = 1 + \\frac{1}{\\nu}\\sum_j q_{ij} = 1$, $K$ is a valid row-stochastic matrix with self-loops representing fictitious null transitions.",
        "<strong>Poisson Mixture Expansion:</strong> Rewriting the matrix exponential $P(t) = e^{Qt} = e^{\\nu t(K - I)} = \\sum_{n=0}^\\infty \\frac{(\\nu t)^n e^{-\\nu t}}{n!} K^n$. Continuous CTMC transitions reduce to a standard Poisson counting clock $N(t) \\sim \\text{Poisson}(\\nu t)$ governing discrete matrix multiplications $K^n$."
    ],
    r"$$K = I + \frac{1}{\nu} Q, \qquad P(t) = \sum_{n=0}^\infty \frac{(\nu t)^n e^{-\nu t}}{n!} K^n \quad (\nu \ge \max_i q_i)$$",
    "Digital metronome sampling: driving an irregular asynchronous machine with a high-frequency master clock ν; ticks where no real event occurs simply execute dummy no-op cycles (self-loops).",
    "Choosing ν smaller than max_i q_i! If ν < q_i for some state i, the diagonal entry K_{ii} = 1 - q_i/ν becomes negative, invalidating K as a probability matrix and causing uniformization to blow up!"
))

if __name__ == "__main__":
    save_stoma_cards(CARDS)
    print("Successfully generated 12 cards for StoMA Topics 26 & 27!")
