"""LAA topic 18 (Markov chains, consensus). Photo picture: a blur filter. Each pixel's new
brightness is a weighted average of its neighbours (rows of weights sum to 1); blurring again and
again flattens the photo to one shade (consensus), and a drop of ink spreads to a steady pattern."""
from laa_lib import *

SUBJECT = "LAA"

def node(x, y, lab, fill="#ffffff"):
    return C(x, y, 13, fill, 1) + N(x, y + 3, lab, 8, "middle")

def d21801(c):
    return svg(c,
        N(120, 12, "a blur: each pixel keeps 0.9 of itself, passes 0.1 on", 7.5, "middle"),
        node(60, 70, "1"), node(180, 70, "2"),
        P("M 74 62 Q 120 40 166 62", "none", 1, ar=True), N(120, 44, "0.1", 7.5, "middle"),
        P("M 166 78 Q 120 100 74 78", "none", 1, ar=True), N(120 , 106, "0.5", 7.5, "middle"),
        N(30, 70, "0.9", 7.5, "end"), N(210, 70, "0.5", 7.5, "start"),
        N(120, 124, "Pᵢⱼ ≥ 0, every row sums to 1: P1 = 1", 7.5, "middle"),
        N(120, 138, "πₖ₊₁ = πₖP,   every |λ(P)| ≤ 1", 7.5, "middle"))

def d21802(c):
    X = lambda k: 30 + 34 * k
    Y = lambda p: 120 - 90 * p
    a = [1.0]
    for _ in range(6): a.append(.9 * a[-1] + .5 * (1 - a[-1]))
    return svg(c,
        L(20, 120, 232, 120, .8, ar=True), N(232, 132, "k (blurs)", 7, "end"), L(24, 126, 24, 20, .8, ar=True),
        L(24, Y(5 / 6), 232, Y(5 / 6), .8, "3 2"), N(232, Y(5 / 6) - 4, "π₁ = 5/6", 7.5, "end"),
        poly([(X(k), Y(v)) for k, v in enumerate(a)], 1.1), *[C(X(k), Y(v), 1.8) for k, v in enumerate(a)],
        poly([(X(k), Y(1 - v)) for k, v in enumerate(a)], 1.1, "2 2"), N(232, Y(1 / 6) - 4, "π₂ = 1/6", 7.5, "end"),
        N(120, 12, "πP = π, Σπᵢ = 1: the steady pattern", 7.5, "middle"),
        N(120, 24, "irreducible + aperiodic ⇒ Pᵏ → 1π", 7.5, "middle"))

def d21803(c):
    X = lambda k: 30 + 24 * k
    Y = lambda e: 120 - 90 * e
    return svg(c,
        L(20, 120, 232, 120, .8, ar=True), N(232, 132, "k", 7.5, "end"), L(24, 126, 24, 20, .8, ar=True),
        poly([(X(k), Y(.9 ** k)) for k in range(9)], 1.1), N(X(8), Y(.9 ** 8) - 6, "|λ₂| = 0.9: slow", 7, "end"),
        poly([(X(k), Y(.4 ** k)) for k in range(9)], 1.1, "3 2"), N(X(3) + 4, Y(.4 ** 3) - 6, "|λ₂| = 0.4: fast", 7, "start"),
        N(120, 12, "‖π₀Pᵏ − π‖ ≤ C |λ₂|ᵏ", 8.5, "middle"),
        N(236, 34, "mixing time ≈ 1/(1 − |λ₂|)", 7.5, "end"), N(236, 46, "spectral gap 1 − |λ₂|", 7, "end"))

def d21804(c):
    out = [N(120, 12, "x(k+1) = W x(k): each pixel averages its neighbours", 7.5, "middle")]
    for r, row in enumerate([[9, 1, 5], [5, 5, 5], [5, 5, 5]][:2]):
        y = 36 + 44 * r
        for i, v in enumerate(row):
            sh = ["#ffffff", "#f1f5f9", "#d9dee7", "#9ca3af"][min(3, v // 3)]
            out += [R(40 + 34 * i, y, 30, 30, sh, 1, 0), N(55 + 34 * i, y + 19, str(v), 8, "middle")]
        out.append(N(150, y + 19, ["x(0)", "x(k) → x̄ 1"][r], 7.5, "start"))
    out += [L(90, 68, 90, 78, 1, ar=True), N(96, 76, "blur again and again", 7, "start"),
            N(120, 128, "doubly stochastic W ⇒ x̄ = (1/n) Σ xᵢ(0) = 5", 7.5, "middle"),
            N(120, 140, "row-stochastic only ⇒ weighted average πx(0)", 7, "middle")]
    return svg(c, *out)

def d21805(c):
    pts = [(40, 60), (90, 30), (90, 92), (150, 60), (200, 60)]
    edges = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4)]
    return svg(c,
        *[L(*pts[a], *pts[b], 1) for a, b in edges], *[C(x, y, 8, "#ffffff", 1) for x, y in pts],
        N(120, 12, "L = D − A,   xᵀLx = Σ over edges (xᵢ − xⱼ)²", 7.5, "middle"),
        N(14, 118, "L1 = 0: a flat photo has no edges", 7.5, "start"),
        N(14, 130, "λ₂(L) > 0 ⇔ connected", 7.5, "start"),
        N(236, 118, "small λ₂: a weak link", 7, "end"), N(236, 130, "(the bridge 3–4)", 7, "end"))

def d21806(c):
    return svg(c,
        node(54, 66, "1", "#d9dee7"), node(150, 66, "2"),
        P("M 67 58 Q 102 40 137 58", "none", 1, ar=True), N(102, 44, "0.1", 7.5, "middle"),
        P("M 137 74 Q 102 92 67 74", "none", 1, ar=True), N(102, 98, "0.5", 7.5, "middle"),
        N(24, 66, "0.9", 7.5, "end"), N(178, 66, "0.5", 7.5, "start"),
        N(236, 20, "πP = π:", 7.5, "end"), N(236, 32, "0.5π₂ = 0.1π₁", 7.5, "end"), N(236, 44, "π = (5/6, 1/6)", 8, "end"),
        N(120, 118, "λ₂ = tr P − 1 = 0.4", 7.5, "middle"), N(120, 132, "error shrinks like 0.4ᵏ", 7.5, "middle"))

CARDS = {
21801: dict(d=d21801, stmtKind="DEFINITION",
  statement=r"<b>Stochastic matrix.</b> $P\in\mathbb R^{n\times n}$ is (row-)stochastic if $P_{ij}\ge0$ and every row sums to $1$, i.e. $P\mathbf1=\mathbf1$; $P_{ij}$ is the probability of moving from state $i$ to state $j$, and distributions evolve by $\pi_{k+1}=\pi_kP$. Then $1$ is an eigenvalue and every eigenvalue satisfies $|\lambda|\le1$.",
  hint="Why does a blur filter never make the photo brighter overall?",
  breakdown=[r"<strong>$P_{ij}\ge0,\ P\mathbf1=\mathbf1$</strong> = each pixel hands out its brightness in nonnegative shares that add to 1.",
             r"<strong>$\pi_{k+1}=\pi_kP$</strong> = a drop of ink (probability) spreads one step per blur.",
             r"<strong>$|\lambda(P)|\le1$</strong> = averaging never amplifies; $\lambda=1$ belongs to the flat photo $\mathbf1$."],
  conn=r"<strong>A blur filter.</strong> Each pixel keeps 90% of itself and passes 10% on, or keeps half and passes half. The weights in each row add to 1, so no light is created or lost.",
  cap="Pixel 1 keeps 0.9 and passes 0.1; pixel 2 keeps 0.5 and passes 0.5. Rows sum to 1 (P1 = 1), πₖ₊₁ = πₖP, and |λ| ≤ 1."),
21802: dict(d=d21802, stmtKind="THEOREM",
  statement=r"<b>Perron–Frobenius for stochastic matrices.</b> If $P$ is stochastic, irreducible and aperiodic, then $1$ is a simple eigenvalue, there is a unique stationary distribution $\pi$ with $\pi P=\pi$, $\pi_i\gt0$, $\sum\pi_i=1$, every other eigenvalue has $|\lambda|\lt1$, and $\pi_0P^k\to\pi$ for every initial distribution, i.e. $P^k\to\mathbf1\pi$.",
  hint="Blur a drop of ink again and again. Where does it settle?",
  breakdown=[r"<strong>$\pi P=\pi,\ \sum\pi_i=1$</strong> = a pattern of ink the blur leaves unchanged: a left eigenvector for $\lambda=1$.",
             r"<strong>irreducible, aperiodic</strong> = every pixel can reach every other, without a fixed rhythm.",
             r"<strong>$P^k\to\mathbf1\pi$</strong> = whatever you start with, many blurs give the same steady pattern."],
  conn=r"<strong>Ink that settles.</strong> Drop ink on pixel 1 and blur repeatedly: the share on each pixel settles to $5/6$ and $1/6$, the same as if you had started on pixel 2.",
  cap="Starting from all ink on pixel 1, repeated blurs drive the shares to the steady pattern π = (5/6, 1/6) with πP = π."),
21803: dict(d=d21803, stmtKind="PROPOSITION",
  statement=r"<b>Rate of convergence.</b> If $P$ is a diagonalizable stochastic matrix satisfying Perron–Frobenius, with second-largest eigenvalue modulus $|\lambda_2|$, then $P^k-\mathbf1\pi=\sum_{j\ge2}\lambda_j^kP_j$, so $\|\pi_0P^k-\pi\|\le C|\lambda_2|^k$. The spectral gap $1-|\lambda_2|$ sets the mixing time, roughly $1/(1-|\lambda_2|)$.",
  hint="What decides how many blurs it takes to settle?",
  breakdown=[r"<strong>$\sum_{j\ge2}\lambda_j^kP_j$</strong> = everything except the steady pattern decays geometrically.",
             r"<strong>$C|\lambda_2|^k$</strong> = the slowest-decaying piece wins; $|\lambda_2|$ near 1 means slow settling.",
             r"<strong>mixing time $\approx1/(1-|\lambda_2|)$</strong> = a bigger spectral gap means faster mixing."],
  conn=r"<strong>Fast and slow blurs.</strong> A strong blur settles in a few passes ($|\lambda_2|=0.4$); a weak one that barely moves ink needs many ($|\lambda_2|=0.9$).",
  cap="The distance to π shrinks like |λ₂|ᵏ: fast for |λ₂| = 0.4 (dashed), slow for |λ₂| = 0.9 (solid); mixing time ≈ 1/(1 − |λ₂|)."),
21804: dict(d=d21804, stmtKind="THEOREM",
  statement=r"<b>Averaging consensus.</b> Let $W$ be row-stochastic and primitive (irreducible and aperiodic), and $x(k+1)=Wx(k)$. Then $x(k)\to(\pi x(0))\mathbf1$, where $\pi$ is the stationary distribution of $W$. If $W$ is doubly stochastic, $\pi=\tfrac1n\mathbf1^\top$ and $x(k)\to\bar x\mathbf1$ with $\bar x=\tfrac1n\sum_ix_i(0)$.",
  hint="Blur a photo forever. What single shade does it become?",
  breakdown=[r"<strong>$x(k+1)=Wx(k)$</strong> = each pixel's new value is a weighted average of its neighbours.",
             r"<strong>$x(k)\to(\pi x(0))\mathbf1$</strong> = all pixels end up the same shade: a weighted average of the start.",
             r"<strong>doubly stochastic $\Rightarrow\bar x$</strong> = if columns also sum to 1, the final shade is the plain average."],
  conn=r"<strong>Blur until flat.</strong> Keep blurring a photo and every pixel becomes the same grey; with a symmetric blur, that grey is the photo's average brightness.",
  cap="Pixels 9, 1, 5 become 5, 5, 5 after many blurs: x(k) → x̄1 with x̄ = (1/n)Σxᵢ(0) for a doubly stochastic W."),
21805: dict(d=d21805, stmtKind="PROPOSITION",
  statement=r"<b>Graph Laplacian.</b> For a graph with degree matrix $D$ and adjacency matrix $A$, $L=D-A$ is symmetric positive semidefinite with $x^\top Lx=\sum_{(i,j)\in E}(x_i-x_j)^2$ and $L\mathbf1=0$. Its eigenvalues $0=\lambda_1\le\lambda_2\le\dots$ satisfy: $\lambda_2\gt0$ iff the graph is connected; the multiplicity of $0$ is the number of components.",
  hint="How does a matrix measure how 'edgy' a pattern on a network is?",
  breakdown=[r"<strong>$x^\top Lx=\sum(x_i-x_j)^2$</strong> = total squared jump across all links: zero only for a flat pattern on each piece.",
             r"<strong>$L\mathbf1=0$</strong> = a flat photo has no edges, so $\lambda_1=0$.",
             r"<strong>$\lambda_2\gt0\iff$ connected</strong> = algebraic connectivity: small $\lambda_2$ signals a weak bridge."],
  conn=r"<strong>Edges in a photo.</strong> On a pixel grid, $x^\top Lx$ adds up the squared brightness jumps between neighbours: large for a sharp photo, zero for a flat one. Blurring reduces it.",
  cap="L = D − A on a small network: xᵀLx sums (xᵢ − xⱼ)² over the links, L1 = 0, and λ₂(L) > 0 because the graph is connected."),
21806: dict(d=d21806, stmtKind="WORKED EXAMPLE",
  statement=r"<b>Example.</b> $P=\begin{pmatrix}0.9&0.1\\0.5&0.5\end{pmatrix}$: $\pi P=\pi$ gives $0.5\pi_2=0.1\pi_1$, so $\pi=(\tfrac56,\tfrac16)$. Eigenvalues: $1$ and $\lambda_2=\operatorname{tr}P-1=0.4$, so $\|\pi_0P^k-\pi\|\propto0.4^k$.",
  hint="Where does the ink settle under this blur, and how fast?",
  breakdown=[r"<strong>$\pi=(5/6,1/6)$</strong> = balance the flows: $0.1$ of pixel 1's share leaves, $0.5$ of pixel 2's share returns.",
             r"<strong>$\lambda_2=\operatorname{tr}P-1=0.4$</strong> = the eigenvalues add to the trace $1.4$, one of them is $1$.",
             r"<strong>$0.4^k$</strong> = the error shrinks by a factor $0.4$ per blur: very fast."],
  conn=r"<strong>Sunny stays sunny.</strong> The same matrix is a weather model: 'sunny stays sunny 90% of the time'. In the long run 5 days out of 6 are sunny, whatever today is.",
  cap="π = (5/6, 1/6) from πP = π; λ₂ = tr P − 1 = 0.4, so the error shrinks like 0.4ᵏ."),
}

STORY = {
 21801: dict(s="STORY 18 · STEP 1 · THE BLUR", b="The final application: a <b>stochastic matrix</b> is a blur filter that moves ink (probability) between pixels without creating or losing any.",
   f=[["20601", "eigenvalues"], ["21705", "trace and determinant"]], n=[["21802", "where the ink settles"], ["21804", "blur until flat"]]),
 21802: dict(s="STORY 18 · STEP 2 · STEADY PATTERN", b="<b>Perron–Frobenius</b>: repeated blurs converge to a unique steady pattern $\\pi$.",
   f=[["21801", "stochastic matrices"]], n=[["21803", "how fast"], ["21806", "compute one"]]),
 21803: dict(s="STORY 18 · STEP 3 · HOW FAST", b="The <b>second eigenvalue</b> decides how many blurs it takes to settle.",
   f=[["21802", "convergence"], ["20604", "diagonalization"]], n=[["21804", "consensus"]]),
 21804: dict(s="STORY 18 · STEP 4 · CONSENSUS", b="Blur forever and every pixel agrees on one shade: the <b>average</b> if the blur is symmetric.",
   f=[["21802", "Pᵏ → 1π"]], n=[["21805", "the Laplacian view"]]),
 21805: dict(s="STORY 18 · STEP 5 · MEASURING EDGES", b="The <b>graph Laplacian</b> measures how edgy a pattern is; $\\lambda_2$ says how well connected the network is.",
   f=[["21804", "consensus"], ["21401", "positive semidefinite"]], n=[["21806", "a full example"]]),
 21806: dict(s="STORY 18 · STEP 6 · WITH NUMBERS", b="A two-state chain: stationary distribution and mixing rate.",
   f=[["21802", "πP = π"], ["21803", "λ₂"]], n=[["20101", "back to the start: it all began with arrows on a canvas"]]),
}

FIX = {cid: {"stmtKind": v["stmtKind"], "statement": v["statement"], "hint": v["hint"], "breakdown": v["breakdown"],
             "personalConnection": v["conn"], "drawingSvg": v["d"](cid), "drawingCaption": v["cap"],
             "textbookImg": None, "textbookRef": None} for cid, v in CARDS.items()}
