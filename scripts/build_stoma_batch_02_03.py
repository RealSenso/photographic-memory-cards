"""Build StoMA Topics 02 & 03 (Cards 30201 to 30306).
Dual-coding photographic plates with pure black-and-white vector diagrams.
"""
import sys, os
sys.path.append(os.path.dirname(__file__))
from stoma_lib import (
    T, N, L, V, P, C, R, E, PG, AX, box, svg, make_stoma_card, save_stoma_cards
)

CARDS = []

# ==============================================================================
# TOPIC 02: CONDITIONAL PROBABILITY, BAYES' RULE & INDEPENDENCE (30201 - 30206)
# ==============================================================================

# Card 30201: Conditional Probability & Reduced Sample Space
svg_30201 = [
    # Universe Omega
    R(16, 16, 208, 112, fill="#ffffff", sw=1.4),
    N(28, 28, "Ω", 11, w="bold"),
    # Event B (Reduced Universe) shaded gray
    E(140, 72, 68, 44, fill="#f1f5f9", w=1.6),
    N(180, 50, "B", 11, w="bold"),
    # Event A (dashed boundary)
    E(80, 72, 54, 40, fill="none", w=1.3, d="3 3"),
    N(46, 54, "A", 11, w="bold"),
    # Intersection A cap B shaded darker
    P("M 104,44 A 54,40 0 0,1 126,72 A 54,40 0 0,1 104,100 A 68,44 0 0,1 104,44 Z", fill="#d9dee7", w=1.5),
    N(115, 73, "A ∩ B", 8.5, w="bold"),
    # Annotations
    N(120, 138, "P(A | B) = Area(A ∩ B) / Area(B)", 8.5, w="bold")
]
CARDS.append(make_stoma_card(
    2, 1, "CONDITIONAL PROBABILITY",
    "Conditional Probability & Reduced Sample Space",
    svg_30201,
    "Conditioning on B discards all outcomes outside B and rescales the remaining probability mass by 1/P(B)",
    [
        "<strong>Definition:</strong> For $B \\in \\mathcal{F}$ with $\\mathbb{P}(B) > 0$, the conditional probability of $A$ given $B$ is $\\mathbb{P}(A \\mid B) = \\frac{\\mathbb{P}(A \\cap B)}{\\mathbb{P}(B)}$.",
        "<strong>Bona Fide Measure:</strong> The set function $A \\mapsto \\mathbb{P}(A \\mid B)$ satisfies all Kolmogorov axioms on $(\\Omega, \\mathcal{F})$: $\\mathbb{P}(B \\mid B) = 1$, non-negativity, and countable additivity.",
        "<strong>Scale Normalization:</strong> Conditioning restricts the universe of discourse to $B$, dividing all joint probabilities within $B$ by $\\mathbb{P}(B)$ to preserve their exact relative likelihoods."
    ],
    r"$$\mathbb{P}(A \mid B) = \frac{\mathbb{P}(A \cap B)}{\mathbb{P}(B)}, \quad \mathbb{P}(B) > 0; \qquad \mathbb{P}(\Omega \mid B) = \mathbb{P}(B \mid B) = 1$$",
    "Cropping a digital photograph: zooming into frame B discards all external pixels, re-scaling the cropped region to 100% full screen.",
    "Conditioning on events with P(B) = 0 is undefined in Kolmogorov's elementary setting. Continuous conditioning requires conditional expectation on σ-algebras (Borel-Kolmogorov paradox)."
))

# Card 30202: The Multiplication Rule & Probability Chain Rule
svg_30202 = [
    box(16, 24, 52, 28, "A₁", "#ffffff", 10),
    V(68, 38, 92, 38, 1.4),
    N(80, 32, "P(A₁)", 7.5),
    box(92, 24, 62, 28, "A₂ | A₁", "#f1f5f9", 9.5),
    V(154, 38, 178, 38, 1.4),
    N(166, 32, "P(A₂|A₁)", 7.5),
    box(178, 24, 48, 28, "...", "#ffffff", 10),
    V(115, 52, 115, 80, 1.4),
    box(30, 80, 180, 34, "A_n | (A₁ ∩ ... ∩ A_{n-1})", "#e2e8f0", 9.5),
    N(120, 132, "Sequential factorization into 1 marginal and (n - 1) conditionals", 8.5, w="bold")
]
CARDS.append(make_stoma_card(
    2, 2, "CHAIN RULE",
    "The Multiplication Rule & Probability Chain Rule",
    svg_30202,
    "Any joint intersection decomposes sequentially into one marginal factor and n-1 conditional stages",
    [
        "<strong>Two-Event Form:</strong> $\\mathbb{P}(A \\cap B) = \\mathbb{P}(A)\\,\\mathbb{P}(B \\mid A) = \\mathbb{P}(B)\\,\\mathbb{P}(A \\mid B)$.",
        "<strong>General Chain Rule:</strong> For any sequence $A_1, \\dots, A_n$ with $\\mathbb{P}(\\bigcap_{i=1}^{n-1} A_i) > 0$, the joint probability factorizes as $\\mathbb{P}(\\bigcap_{i=1}^n A_i) = \\mathbb{P}(A_1) \\prod_{k=2}^n \\mathbb{P}(A_k \\mid \\bigcap_{j=1}^{k-1} A_j)$.",
        "<strong>Permutation Invariance:</strong> Any permutation of indices yields mathematically identical joint probability, but choosing causal/chronological orders simplifies computation."
    ],
    r"$$\mathbb{P}\left(\bigcap_{i=1}^n A_i\right) = \mathbb{P}(A_1) \prod_{k=2}^n \mathbb{P}\left(A_k \;\middle|\; \bigcap_{j=1}^{k-1} A_j\right)$$",
    "Drawing four consecutive aces from an un-shuffled deck: (4/52) × (3/51) × (2/50) × (1/49). Each card drawn conditions the state of the remaining deck.",
    "Forgetting to check whether intermediate conditioning histories have strictly positive probability: P(A₁ ∩ ... ∩ A_{k-1}) > 0 is mandatory at every step."
))

# Card 30203: Law of Total Probability (Partition Decomposition)
svg_30203 = [
    # Universe rectangle
    R(20, 18, 200, 100, fill="#ffffff", sw=1.5),
    # Vertical partition lines
    L(70, 18, 70, 118, 1.2, d="2 2"),
    L(120, 18, 120, 118, 1.2, d="2 2"),
    L(170, 18, 170, 118, 1.2, d="2 2"),
    N(45, 30, "B₁", 9.5), N(95, 30, "B₂", 9.5), N(145, 30, "B₃", 9.5), N(195, 30, "B₄", 9.5),
    # Event A cutting across all slices
    E(120, 75, 75, 30, fill="#f1f5f9", w=1.6),
    N(120, 75, "Event A = ⋃ (A ∩ Bᵢ)", 9.5, w="bold"),
    N(120, 134, "P(A) = ∑ P(A | Bᵢ) P(Bᵢ)  (pairwise disjoint union)", 8.5, w="bold")
]
CARDS.append(make_stoma_card(
    2, 3, "TOTAL PROBABILITY",
    "Law of Total Probability: Partition Decomposition",
    svg_30203,
    "Partition {Bᵢ} slices event A into disjoint sub-events whose masses sum to the unconditional probability",
    [
        "<strong>Partition Criterion:</strong> Collection $\\{B_1, \\dots, B_n\\}$ partitions $\\Omega$ if $B_i \\cap B_j = \\emptyset$ for $i \\ne j$, $\\bigcup_{i=1}^n B_i = \\Omega$, and $\\mathbb{P}(B_i) > 0$.",
        "<strong>Disjoint Splitting:</strong> Any event $A$ decomposes into mutually exclusive pieces $A = \\bigcup_{i=1}^n (A \\cap B_i)$, yielding $\\mathbb{P}(A) = \\sum_{i=1}^n \\mathbb{P}(A \\mid B_i)\\,\\mathbb{P}(B_i)$.",
        "<strong>Strategic Tool:</strong> Allows computing difficult unconditional probabilities by conditioning on hidden or latent regimes where $\\mathbb{P}(A \\mid B_i)$ is elementary."
    ],
    r"$$\mathbb{P}(A) = \sum_{i=1}^n \mathbb{P}(A \mid B_i)\,\mathbb{P}(B_i) \quad \text{where } \bigcup_{i=1}^n B_i = \Omega, \; B_i \cap B_j = \emptyset$$",
    "Measuring the total timber in a national forest by dividing the map into distinct climatic zones Bᵢ and multiplying area by local tree density.",
    "Overlooking missing partition coverage: if ∑ P(Bᵢ) < 1, the partition has an uncounted gap, strictly underestimating P(A)."
))

# Card 30204: Bayes’ Theorem & Bayesian Inversion
svg_30204 = [
    box(24, 20, 80, 32, "Prior: P(B_k)", "#ffffff", 9),
    V(104, 36, 136, 36, 1.4),
    N(120, 28, "Evidence A", 7.5),
    box(136, 20, 80, 32, "Posterior: P(B_k | A)", "#e2e8f0", 9),
    # Fraction illustration
    R(24, 70, 192, 46, fill="#f8fafc", sw=1.3),
    N(120, 84, "P(A | B_k) · P(B_k)   [Likelihood × Prior]", 8.5, w="bold"),
    L(36, 92, 204, 92, 1.4),
    N(120, 106, "∑ P(A | Bᵢ) · P(Bᵢ)   [Total Evidence P(A)]", 8.5),
    N(120, 132, "Posterior ∝ Likelihood × Prior", 8.5, w="bold")
]
CARDS.append(make_stoma_card(
    2, 4, "BAYESIAN INVERSION",
    "Bayes’ Theorem: Inverting Cause and Effect",
    svg_30204,
    "Inverts conditional direction from likelihood P(A|B) to posterior belief P(B|A) given observed evidence",
    [
        "<strong>Formal Statement:</strong> For partition $\\{B_i\\}$ and event $A$ with $\\mathbb{P}(A) > 0$: $\\mathbb{P}(B_k \\mid A) = \\frac{\\mathbb{P}(A \\mid B_k)\\,\\mathbb{P}(B_k)}{\\sum_{i} \\mathbb{P}(A \\mid B_i)\\,\\mathbb{P}(B_i)}$.",
        "<strong>Prior to Posterior:</strong> Updates initial belief $\\mathbb{P}(B_k)$ (prior) through likelihood $\\mathbb{P}(A \\mid B_k)$ upon observing evidence $A$.",
        "<strong>Denominator as Normalizer:</strong> The denominator is the unconditional evidence mass $\\mathbb{P}(A)$, ensuring $\\sum_k \\mathbb{P}(B_k \\mid A) = 1$."
    ],
    r"$$\mathbb{P}(B_k \mid A) = \frac{\mathbb{P}(A \mid B_k)\,\mathbb{P}(B_k)}{\sum_{i=1}^n \mathbb{P}(A \mid B_i)\,\mathbb{P}(B_i)} = \frac{\mathbb{P}(A \mid B_k)\,\mathbb{P}(B_k)}{\mathbb{P}(A)}$$",
    "A medical diagnostic test: observing symptoms A (evidence) and calculating the updated likelihood of underlying illness B_k (cause).",
    "The Base Rate Fallacy: confusing test reliability P(A|B) with disease certainty P(B|A). If the prior P(B) is 0.1%, a 99% accurate test still yields >95% false alarms!"
))

# Card 30205: Independence vs Conditional Independence
svg_30205 = [
    # Marginal independence
    R(16, 18, 98, 98, fill="#ffffff", sw=1.3),
    N(65, 32, "Marginal: A ⊥ B", 8.5, w="bold"),
    E(50, 72, 24, 24, fill="none", w=1.3),
    E(80, 72, 24, 24, fill="none", w=1.3),
    N(42, 74, "A", 9), N(88, 74, "B", 9),
    N(65, 106, "P(A ∩ B) = P(A)P(B)", 7),
    # Conditional independence
    R(126, 18, 98, 98, fill="#f8fafc", sw=1.3),
    N(175, 32, "Conditional: A ⊥ B | C", 8.5, w="bold"),
    box(160, 44, 30, 20, "C", "#d9dee7", 9),
    V(175, 64, 150, 84, 1.2), V(175, 64, 200, 84, 1.2),
    box(136, 84, 28, 20, "A", "#ffffff", 8.5),
    box(186, 84, 28, 20, "B", "#ffffff", 8.5),
    N(175, 110, "P(A∩B|C)=P(A|C)P(B|C)", 6.5),
    N(120, 134, "Marginal independence does NOT imply conditional independence (and vice-versa)", 8)
]
CARDS.append(make_stoma_card(
    2, 5, "INDEPENDENCE",
    "Independence vs Conditional Independence",
    svg_30205,
    "Marginal independence and conditional independence are strictly separate properties with zero automatic implication",
    [
        "<strong>Marginal Independence:</strong> $A \\perp B \\iff \\mathbb{P}(A \\cap B) = \\mathbb{P}(A)\\,\\mathbb{P}(B)$, which is equivalent to $\\mathbb{P}(A \\mid B) = \\mathbb{P}(A)$ when $\\mathbb{P}(B) > 0$.",
        "<strong>Conditional Independence:</strong> $A \\perp B \\mid C \\iff \\mathbb{P}(A \\cap B \\mid C) = \\mathbb{P}(A \\mid C)\\,\\mathbb{P}(B \\mid C)$.",
        "<strong>Zero Implication:</strong> Events independent marginally can become dependent given evidence (collider conditioning); events dependent marginally can become independent given their common cause."
    ],
    r"$$A \perp B \iff \mathbb{P}(A \cap B) = \mathbb{P}(A)\mathbb{P}(B); \qquad A \perp B \mid C \iff \mathbb{P}(A \cap B \mid C) = \mathbb{P}(A \mid C)\mathbb{P}(B \mid C)$$",
    "Reading skill and shoe size in children: strongly dependent. But conditioning on Age (C), reading level and shoe size become conditionally independent.",
    "Berkson's Paradox: conditioning on common success (e.g. college admissions) creates artificial negative correlation between two independent skills."
))

# Card 30206: Worked Benchmark: Bernstein’s Pairwise vs Mutual Independence
svg_30206 = [
    # 4 faces of tetrahedron
    box(16, 20, 48, 40, "Face 1\n(R, G)", "#ffffff", 8),
    box(70, 20, 48, 40, "Face 2\n(R, B)", "#ffffff", 8),
    box(124, 20, 48, 40, "Face 3\n(G, B)", "#ffffff", 8),
    box(178, 20, 48, 40, "Face 4\n(R, G, B)", "#e2e8f0", 8),
    # Pairwise check
    R(16, 72, 210, 48, fill="#f8fafc", sw=1.3),
    N(120, 84, "P(R) = P(G) = P(B) = 2/4 = 1/2", 8.5),
    N(120, 97, "P(R ∩ G) = P(Face 4) + P(Face 1) = 2/4 = 1/4 = P(R)P(G)  [Pairwise OK]", 7.5, w="bold"),
    N(120, 110, "P(R ∩ G ∩ B) = P(Face 4) = 1/4  ≠  P(R)P(G)P(B) = 1/8  [Mutual FAILS!]", 7.5, w="bold"),
    N(120, 134, "Bernstein's classic counterexample: 3 pairwise independent events failing mutual independence", 8)
]
CARDS.append(make_stoma_card(
    2, 6, "WORKED BENCHMARK",
    "Worked Benchmark: Bernstein’s Pairwise vs Mutual Independence",
    svg_30206,
    "Pairwise independence checks (n choose 2) pairs; mutual independence requires all 2^n - n - 1 equations",
    [
        "<strong>Tetrahedron Setup:</strong> 4 faces with equal probability $1/4$: Face 1 has colors $\\{R, G\\}$, Face 2 $\\{R, B\\}$, Face 3 $\\{G, B\\}$, Face 4 $\\{R, G, B\\}$.",
        "<strong>Pairwise Independence Holds:</strong> $\\mathbb{P}(R) = \\mathbb{P}(G) = \\mathbb{P}(B) = 2/4 = 1/2$. For any pair, $\\mathbb{P}(R \\cap G) = 1/4 = \\mathbb{P}(R)\\,\\mathbb{P}(G)$.",
        "<strong>Mutual Independence Fails:</strong> $\\mathbb{P}(R \\cap G \\cap B) = 1/4$ (Face 4), whereas $\\mathbb{P}(R)\\,\\mathbb{P}(G)\\,\\mathbb{P}(B) = (1/2)^3 = 1/8 \\ne 1/4$."
    ],
    r"$$\mathbb{P}(R \cap G) = \frac{1}{4} = \mathbb{P}(R)\mathbb{P}(G), \quad \text{yet} \quad \mathbb{P}(R \cap G \cap B) = \frac{1}{4} \ne \mathbb{P}(R)\mathbb{P}(G)\mathbb{P}(B) = \frac{1}{8}$$",
    "Three secret keys: possessing any two keys tells you nothing about the lock code, but all three together open the lock instantly.",
    "Assuming pairwise independence implies mutual independence! For n events, mutual independence requires verifying all 2^n - n - 1 non-trivial subset intersection equations."
))

# ==============================================================================
# TOPIC 03: DISCRETE & CONTINUOUS RANDOM VARIABLES (30301 - 30306)
# ==============================================================================

# Card 30301: The Random Variable & CDF Axioms
svg_30301 = [
    AX(24, 115, 220, 20),
    # S-shaped CDF curve
    P("M 24,114 L 60,114 C 90,114 110,80 130,55 C 150,30 170,26 210,26", fill="none", w=2.0),
    # Asymptote line y=1
    L(24, 26, 215, 26, 0.8, d="3 3"),
    N(16, 28, "1", 9, w="bold"),
    N(16, 115, "0", 9, w="bold"),
    N(130, 16, "F_X(x) = P(X ≤ x)", 9.5, w="bold"),
    # Point evaluation
    L(130, 55, 130, 115, 1.0, d="2 2"),
    C(130, 55, 3, fill="#000000"),
    N(130, 126, "x", 9),
    N(120, 138, "Non-decreasing, right-continuous, limits 0 and 1", 8.5)
]
CARDS.append(make_stoma_card(
    3, 1, "FOUNDATIONAL RV & CDF",
    "The Random Variable & Cumulative Distribution Function (CDF)",
    svg_30301,
    "The CDF F_X(x) completely characterizes any random variable's law and is always non-decreasing and right-continuous",
    [
        "<strong>Measurable Mapping:</strong> A random variable $X: \\Omega \\to \\mathbb{R}$ is a measurable function satisfying $\\{\\omega : X(\\omega) \\le x\\} \\in \\mathcal{F}$ for all $x \\in \\mathbb{R}$.",
        "<strong>CDF Definition:</strong> $F_X(x) \\triangleq \\mathbb{P}(X \\le x) = \\mathbb{P}(\\{\\omega \\in \\Omega : X(\\omega) \\le x\\})$.",
        "<strong>Four Invariants:</strong> (1) Non-decreasing: $x_1 \\le x_2 \\implies F(x_1) \\le F(x_2)$; (2) Right-continuous: $\\lim_{h \\downarrow 0} F(x+h) = F(x)$; (3) $\\lim_{x \\to -\\infty} F(x) = 0$; (4) $\\lim_{x \\to \\infty} F(x) = 1$."
    ],
    r"$$F_X(x) = \mathbb{P}(X \le x), \quad \lim_{h \downarrow 0} F_X(x+h) = F_X(x), \quad F_X(-\infty) = 0, \quad F_X(\infty) = 1$$",
    "A cumulative water reservoir gauge reading total liters accumulated up to ground elevation x: it cannot drain backwards, and fills to 100%.",
    "Assuming CDFs must be continuous everywhere. Jump discontinuities F(x) - F(x⁻) = P(X = x) occur at every discrete atom; only RIGHT-continuity is universally guaranteed!"
))

# Card 30302: Discrete RVs, PMF & Step CDF
svg_30302 = [
    AX(24, 115, 220, 25),
    # Step function
    L(24, 114, 60, 114, 2.0),
    L(60, 114, 60, 85, 1.0, d="2 2"),
    C(60, 85, 3, fill="#000000"),
    C(60, 114, 2.5, fill="#ffffff"),
    L(60, 85, 110, 85, 2.0),
    L(110, 85, 110, 48, 1.0, d="2 2"),
    C(110, 48, 3, fill="#000000"),
    C(110, 85, 2.5, fill="#ffffff"),
    L(110, 48, 170, 48, 2.0),
    L(170, 48, 170, 26, 1.0, d="2 2"),
    C(170, 26, 3, fill="#000000"),
    C(170, 48, 2.5, fill="#ffffff"),
    L(170, 26, 215, 26, 2.0),
    N(60, 126, "x₁", 8.5), N(110, 126, "x₂", 8.5), N(170, 126, "x₃", 8.5),
    N(76, 70, "jump = p(x₁)", 7),
    N(126, 36, "jump = p(x₂)", 7),
    N(120, 138, "Staircase CDF: jump height equals PMF probability mass", 8.5)
]
CARDS.append(make_stoma_card(
    3, 2, "DISCRETE RVs",
    "Discrete Random Variables, PMF & Step CDF",
    svg_30302,
    "The CDF of a discrete random variable is a pure step staircase whose jump heights equal PMF values p_X(x_k)",
    [
        "<strong>Countable Support:</strong> $X$ takes values in countable set $\\{x_1, x_2, \\dots\\}$, characterized by PMF $p_X(x) = \\mathbb{P}(X = x) \\ge 0$ with $\\sum_k p_X(x_k) = 1$.",
        "<strong>Staircase CDF:</strong> $F_X(x) = \\sum_{x_k \\le x} p_X(x_k)$. Jumps occur precisely at atoms: $F_X(x_k) - F_X(x_k^-) = p_X(x_k)$.",
        "<strong>Canonical Roster:</strong> $\\text{Bernoulli}(p)$, $\\text{Binomial}(n, p)$, $\\text{Geometric}(p)$, $\\text{Poisson}(\\lambda)$, $\\text{Negative Binomial}(r, p)$, $\\text{Hypergeometric}$."
    ],
    r"$$p_X(x_k) \ge 0, \quad \sum_{k} p_X(x_k) = 1, \qquad F_X(x_k) - \lim_{\epsilon \downarrow 0} F_X(x_k - \epsilon) = \mathbb{P}(X = x_k)$$",
    "Depositing cash into a vending machine in discrete coin increments: account balance rises in sharp vertical leaps with every coin.",
    "Interval evaluation traps: P(a < X ≤ b) = F(b) - F(a), whereas P(a ≤ X ≤ b) = F(b) - F(a) + P(X = a). With discrete variables, strict vs weak inequalities drastically change the answer!"
))

# Card 30303: Continuous RVs, PDF & Radon-Nikodym
svg_30303 = [
    AX(24, 115, 220, 20),
    # Smooth bell density
    P("M 24,114 Q 80,114 100,90 Q 120,25 130,25 Q 140,25 160,90 Q 180,114 215,114", fill="none", w=2.0),
    # Shaded integral area from a to b
    P("M 100,90 Q 120,25 130,25 Q 140,25 150,62 L 150,114 L 100,114 Z", fill="#d9dee7", w=1.2),
    L(100, 90, 100, 114, 1.0, d="2 2"),
    L(150, 62, 150, 114, 1.0, d="2 2"),
    N(100, 126, "a", 9), N(150, 126, "b", 9),
    N(125, 80, "P(a ≤ X ≤ b)", 8, w="bold"),
    N(120, 138, "Continuous density: Area under curve = probability; single points have probability 0", 8.5)
]
CARDS.append(make_stoma_card(
    3, 3, "CONTINUOUS RVs",
    "Continuous Random Variables & Probability Density Function (PDF)",
    svg_30303,
    "Probabilities correspond to areas under the PDF curve; single real points have exactly zero probability mass",
    [
        "<strong>Absolute Continuity:</strong> $X$ is continuous if there exists non-negative integrable $f_X(x)$ such that $F_X(x) = \\int_{-\\infty}^x f_X(t)\\,dt$ for all $x$.",
        "<strong>Calculus Fundamental:</strong> $f_X(x) = \\frac{d}{dx} F_X(x)$ almost everywhere, with $\\int_{-\\infty}^\\infty f_X(x)\\,dx = 1$.",
        "<strong>Point Mass Zero:</strong> $\\mathbb{P}(X = c) = \\int_c^c f_X(t)\\,dt = 0$ for every single $c \\in \\mathbb{R}$. Probabilities are only non-zero over intervals of positive length."
    ],
    r"$$F_X(x) = \int_{-\infty}^x f_X(t)\,dt, \quad f_X(x) = F_X'(x), \quad \mathbb{P}(X = c) = 0 \quad \forall c \in \mathbb{R}$$",
    "Linear density of a thin steel rod: an infinitesimally thin point slice has 0 grams of mass, but integrating density over any segment yields positive weight.",
    "Believing probability density f_X(x) cannot exceed 1! Densities can be arbitrarily large (e.g. Uniform[0, 0.1] has f(x) = 10). Only PROBABILITIES are bounded by 1."
))

# Card 30304: Exponential Distribution & Memoryless Invariance
svg_30304 = [
    AX(24, 115, 220, 20),
    # Exponential curve
    P("M 24,30 Q 60,90 120,108 Q 170,113 215,114", fill="none", w=2.0),
    N(16, 30, "λ", 9, w="bold"),
    # Split points t and t+s
    L(70, 80, 70, 114, 1.0, d="2 2"),
    L(130, 106, 130, 114, 1.0, d="2 2"),
    N(70, 125, "t", 8.5), N(130, 125, "t + s", 8.5),
    N(160, 50, "P(X > t + s | X > t) = P(X > s)", 8.5, w="bold"),
    N(160, 68, "e^{-λ(t+s)} / e^{-λt} = e^{-λs}", 8),
    N(120, 138, "Exponential is the ONLY continuous distribution with the memoryless property", 8.5)
]
CARDS.append(make_stoma_card(
    3, 4, "CANONICAL CONTINUOUS",
    "Exponential Distribution & Memoryless Invariance",
    svg_30304,
    "The exponential distribution forgets all past elapsed waiting time, maintaining a constant hazard rate",
    [
        "<strong>Density & Survival:</strong> $f_X(t) = \\lambda e^{-\\lambda t} \\mathbf{1}_{\\{t \\ge 0\\}}$ with survival function $\\mathbb{P}(X > t) = e^{-\\lambda t}$. Mean $\\mathbb{E}[X] = 1/\\lambda$, variance $\\operatorname{Var}(X) = 1/\\lambda^2$.",
        "<strong>Memoryless Invariant:</strong> $\\mathbb{P}(X > t + s \\mid X > t) = \\mathbb{P}(X > s)$ for all $s, t \\ge 0$. The item does not age or wear out over time.",
        "<strong>Unique Characterization:</strong> The Exponential distribution is the ONLY continuous distribution on $[0, \\infty)$ possessing memoryless property (Geometric is the only discrete one)."
    ],
    r"$$\mathbb{P}(X > t + s \mid X > t) = \frac{e^{-\lambda(t+s)}}{e^{-\lambda t}} = e^{-\lambda s} = \mathbb{P}(X > s)$$",
    "A brand new lightbulb with constant microscopic failure rate: having operated for 200 hours without failing gives zero evidence that it will burn out any sooner in the next hour.",
    "Applying the memoryless property to aging physical machinery (car engines, human organs). Most real systems exhibit wear-out (Weibull with shape k > 1), where hazard rate strictly increases."
))

# Card 30305: Gaussian (Normal) Distribution & Invariants
svg_30305 = [
    AX(24, 115, 220, 20),
    # Gaussian bell
    P("M 30,114 Q 80,114 100,85 Q 120,25 125,25 Q 130,25 150,85 Q 170,114 220,114", fill="none", w=2.0),
    # Center mean
    L(125, 25, 125, 114, 1.2, d="2 2"),
    N(125, 125, "μ", 10, w="bold"),
    # Inflection points μ - σ and μ + σ
    L(100, 85, 100, 114, 0.8, d="2 2"),
    L(150, 85, 150, 114, 0.8, d="2 2"),
    N(100, 125, "μ - σ", 8), N(150, 125, "μ + σ", 8),
    N(125, 65, "68.3% mass", 8, w="bold"),
    N(120, 138, "Symmetric around mean μ, inflection points at μ ± σ, standard CDF Φ(z)", 8.5)
]
CARDS.append(make_stoma_card(
    3, 5, "GAUSSIAN FOUNDATION",
    "Gaussian (Normal) Distribution & Canonical Standardization",
    svg_30305,
    "The bell curve is completely governed by mean μ and variance σ², standardizing via Z = (X - μ)/σ",
    [
        "<strong>Density Form:</strong> $f_X(x) = \\frac{1}{\\sqrt{2\\pi}\\sigma} \\exp\\left(-\\frac{(x - \\mu)^2}{2\\sigma^2}\\right)$ on $\\mathbb{R}$. Inflection points occur exactly at $x = \\mu \\pm \\sigma$.",
        "<strong>Z-Score Standardization:</strong> If $X \\sim \\mathcal{N}(\\mu, \\sigma^2)$, then $Z = \\frac{X - \\mu}{\\sigma} \\sim \\mathcal{N}(0, 1)$, with CDF $\\Phi(z) = \\frac{1}{\\sqrt{2\\pi}}\\int_{-\\infty}^z e^{-u^2/2}du$.",
        "<strong>Symmetry & Tail:</strong> $\\Phi(-z) = 1 - \\Phi(z)$. The tail satisfies Mill's ratio bound: $\\left(\\frac{1}{z} - \\frac{1}{z^3}\\right) \\frac{e^{-z^2/2}}{\\sqrt{2\\pi}} < 1 - \\Phi(z) < \\frac{1}{z} \\frac{e^{-z^2/2}}{\\sqrt{2\\pi}}$."
    ],
    r"$$X \sim \mathcal{N}(\mu, \sigma^2) \implies Z = \frac{X - \mu}{\sigma} \sim \mathcal{N}(0, 1), \quad \Phi(-z) = 1 - \Phi(z)$$",
    "Random microscopic measurement errors in high-precision laboratory balances: countless independent micro-disturbances sum to a perfect symmetric bell curve.",
    "Attempting to evaluate Φ(z) symbolically by elementary integration. The integral has no closed-form elementary antiderivative; express solutions strictly in terms of Φ(z) or Q(z)."
))

# Card 30306: Worked Benchmark: Mixed Random Variable & Jump Analysis
svg_30306 = [
    AX(24, 115, 220, 20),
    # Mixed CDF with jumps at 0 and 1
    L(24, 114, 60, 114, 2.0),
    L(60, 114, 60, 85, 1.0, d="2 2"),
    C(60, 85, 3, fill="#000000"),
    C(60, 114, 2.5, fill="#ffffff"),
    N(60, 126, "0", 9, w="bold"),
    N(40, 95, "jump = 0.3", 7, w="bold"),
    # Linear continuous segment
    L(60, 85, 160, 50, 2.0),
    # Jump at 1
    L(160, 50, 160, 26, 1.0, d="2 2"),
    C(160, 26, 3, fill="#000000"),
    C(160, 50, 2.5, fill="#ffffff"),
    N(160, 126, "1", 9, w="bold"),
    N(185, 38, "jump = 0.3", 7, w="bold"),
    L(160, 26, 215, 26, 2.0),
    N(120, 138, "E[X] = ∑ xᵢ P(X=xᵢ) + ∫ x f_c(x) dx = 0(0.3) + 1(0.3) + ∫ 0.4x dx = 0.5", 8)
]
CARDS.append(make_stoma_card(
    3, 6, "WORKED BENCHMARK",
    "Worked Benchmark: Mixed Random Variable & Lebesgue Splitting",
    svg_30306,
    "Mixed random variables possess both jump atoms and continuous densities; expectations sum discrete and integral parts",
    [
        "<strong>Problem Setup:</strong> Waiting time $X$ has point mass $\\mathbb{P}(X=0) = 0.3$, point mass $\\mathbb{P}(X=1) = 0.3$, and uniform density $f_c(x) = 0.4$ for $x \\in (0, 1)$.",
        "<strong>CDF Structure:</strong> $F_X(x)$ jumps from 0 to 0.3 at $x=0$, rises linearly with slope 0.4 to 0.7 at $x=1^-$, then jumps by 0.3 to 1.0 at $x=1$.",
        "<strong>Expectation Evaluation:</strong> $\\mathbb{E}[X] = \\sum_k x_k \\mathbb{P}(X=x_k) + \\int_0^1 x f_c(x)\\,dx = 0(0.3) + 1(0.3) + \\int_0^1 0.4 x\\,dx = 0.3 + 0.2 = 0.5$."
    ],
    r"$$F_X(x) = \alpha F_{\text{disc}}(x) + (1-\alpha) F_{\text{cont}}(x), \quad \mathbb{E}[X] = \sum_k x_k \mathbb{P}(X=x_k) + \int x f_c(x)\,dx$$",
    "An insurance claim policy with a $500 deductible and a $10,000 maximum cap: exact 0 payout for minor damage, continuous claims in between, and a lump spike at $10,000.",
    "Applying ∫ x f(x)dx alone without accounting for point mass jumps! Disregarding atoms F(x) - F(x⁻) completely invalidates expected values and variances."
))

# Save cards to cards_stoma.js
save_stoma_cards(CARDS)
print(f"Successfully generated {len(CARDS)} cards for StoMA Topics 02 & 03!")
