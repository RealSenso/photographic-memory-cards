"""LAA topic 13 (spectral theorem). Photo picture: every self-adjoint (or, over C, normal)
edit is 'stretch along a square grid of perpendicular rulers'."""
from laa_lib import *

SUBJECT = "LAA"

def square_grid(O, s=22, n=3):
    """a square grid tilted so one ruler points right-up and the other left-up"""
    a, b = (s * .8, -s * .6), (-s * .6, -s * .8)
    p = lambda i, j: (O[0] + i * a[0] + j * b[0], O[1] + i * a[1] + j * b[1])
    return "".join([L(*p(i, 0), *p(i, n), .5, "2 2") for i in range(n + 1)] + [L(*p(0, j), *p(n, j), .5, "2 2") for j in range(n + 1)]), p

def d21301(c):
    g, p = square_grid((60, 124))
    return svg(c, g, pin(60, 124, None),
        vec((60, 124), p(1, 0), "u₁", 2, 10, "middle", 7.5), vec((60, 124), p(0, 1), "u₂", -4, 0, "end", 7.5),
        N(236, 20, "over ℂ:", 7.5, "end"), N(236, 32, "T normal ⇔", 8, "end"), N(236, 44, "orthonormal eigenbasis", 7.5, "end"),
        N(236, 74, "A = UDU*", 8.5, "end"), N(236, 86, "U*U = I (square grid)", 7, "end"), N(236, 98, "D = diag(λ₁, …, λₙ)", 7, "end"),
        N(236, 130, "Schur + normal ⇒ diagonal", 7, "end"))

def d21302(c):
    return svg(c,
        circ(70, 80, 30, "none", .9, "3 2"), E(70, 80, 54, 22, -30, "#f1f5f9", 1), pin(70, 80, None),
        vec((70, 80), (117, 53), "q₁: ×λ₁", 2, -4, "start", 7.5), vec((70, 80), (59, 61), "q₂: ×λ₂", -4, -2, "end", 7.5),
        N(236, 20, "over ℝ:", 7.5, "end"), N(236, 32, "A = Aᵀ ⇔", 8, "end"), N(236, 44, "A = QΛQᵀ", 8.5, "end"),
        N(236, 64, "QᵀQ = I, Λ real diagonal", 7, "end"),
        N(236, 104, "a real self-adjoint edit", 7, "end"), N(236, 114, "always has a real eigenvalue", 7, "end"),
        N(70, 132, "circle → ellipse, axes ⊥", 7, "middle"))

def d21303(c):
    return svg(c,
        N(120, 12, "T = λ₁P₁ + λ₂P₂ + …", 9, "middle"),
        R(14, 30, 64, 50, "#ffffff", 1, 3), N(46, 52, "T", 11, "middle"),
        N(86, 58, "=", 10, "middle"),
        R(96, 30, 56, 50, "#f1f5f9", 1, 3), N(124, 50, "λ₁ · P₁", 8, "middle"), N(124, 66, "shadow on E(λ₁)", 6.8, "middle"),
        N(160, 58, "+", 10, "middle"),
        R(168, 30, 58, 50, "#f1f5f9", 1, 3), N(197, 50, "λ₂ · P₂", 8, "middle"), N(197, 66, "shadow on E(λ₂)", 6.8, "middle"),
        N(120, 104, "Σ Pⱼ = I,   PᵢPⱼ = 0 (i ≠ j),   Pⱼ* = Pⱼ", 7.5, "middle"),
        N(120, 120, "rank-1 form: A = Σ λₖ uₖuₖ*", 7.5, "middle"),
        N(120, 136, "split into shadows, stretch each, add back", 7, "middle"))

def d21304(c):
    return svg(c,
        N(120, 12, "f(T) = Σ f(λⱼ) Pⱼ = U f(D) U*", 8, "middle"),
        R(14, 32, 96, 22, "#f1f5f9", 1, 3), N(62, 47, "T: ×λ₁ on u₁, ×λ₂ on u₂", 7, "middle"),
        L(112, 43, 128, 43, 1, ar=True),
        R(130, 32, 96, 22, "#d9dee7", 1, 3), N(178, 47, "f(T): ×f(λ₁), ×f(λ₂)", 7, "middle"),
        N(14, 78, "e^T = Σ e^(λⱼ) Pⱼ", 7.5, "start"), N(14, 92, "√T = Σ √λⱼ Pⱼ (λⱼ ≥ 0)", 7.5, "start"),
        N(14, 106, "T⁻¹ = Σ (1/λⱼ) Pⱼ (λⱼ ≠ 0)", 7.5, "start"),
        N(236, 132, "same grid, new stretch factors", 7, "end"))

def d21305(c):
    O = (60, 92)
    return svg(c,
        N(120, 12, "ℝ: A = QΛQᵀ ⇔ symmetric;  ℂ: A = UDU* ⇔ normal", 7.2, "middle"),
        circ(*O, 32, "none", .9, "3 2"), pin(*O, None),
        vec(O, (92, 92), "v", 0, 10, "middle", 7.5), vec(O, (60, 60), "Av", -4, 0, "end", 7.5),
        P(f"M {O[0] + 20} {O[1]} A 20 20 0 0 0 {O[0]} {O[1] - 20}", "none", .9, ar=True),
        N(60, 140, "A = [0 −1; 1 0]: rotate 90°", 7, "middle"),
        N(236, 50, "normal but not symmetric", 7.5, "end"), N(236, 62, "λ = ±i: no real eigen-arrow", 7.5, "end"),
        N(236, 96, "over ℝ: 2×2 rotation blocks", 7, "end"), N(236, 108, "over ℂ: diagonal UDU*", 7, "end"))

def d21306(c):
    O = (80, 96)
    s = 18
    P2 = lambda x, y: (O[0] + s * x, O[1] - s * y)
    return svg(c,
        L(14, 96, 160, 96, .6), L(80, 140, 80, 10, .6), pin(*O, None),
        vec(O, P2(.71, .71), "u₁", -4, -2, "end", 7.5), vec(O, P2(2.12, 2.12), "×3", 4, 0, "start", 7.5),
        vec(O, P2(.71, -.71), "u₂: ×1", 4, 8, "start", 7.5),
        N(236, 20, "A = [2 1; 1 2]", 8, "end"), N(236, 32, "λ = 3, 1", 7.5, "end"),
        N(236, 56, "A = 3P₁ + 1·P₂", 8, "end"), N(236, 70, "√A = √3 P₁ + P₂", 7.5, "end"), N(236, 84, "Aᵏ = 3ᵏP₁ + P₂", 7.5, "end"),
        N(236, 122, "P₁ = ½[1 1; 1 1]", 7, "end"), N(236, 134, "P₂ = ½[1 −1; −1 1]", 7, "end"))

CARDS = {
21301: dict(d=d21301, stmtKind="THEOREM",
  statement=r"<b>Complex spectral theorem (Axler 7.31).</b> Suppose $\mathbb F=\mathbb C$ and $T\in\mathcal L(V)$. The following are equivalent: $T$ is normal; $V$ has an orthonormal basis consisting of eigenvectors of $T$; $T$ has a diagonal matrix with respect to some orthonormal basis of $V$. In matrix form: $A$ normal $\iff A=UDU^*$ with $U$ unitary and $D$ diagonal.",
  hint="Which complex edits are 'just stretches' along a square grid?",
  breakdown=[r"<strong>$T$ normal</strong> = the edit commutes with its measuring partner, $TT^*=T^*T$.",
             r"<strong>$U^*U=I$</strong> = the eigen-arrows form a square (orthonormal) grid, the columns of $U$.",
             r"<strong>$D=\operatorname{diag}(\lambda_j)$</strong> = in that grid the edit only stretches. Proof idea: Schur makes it triangular in a square grid, and normality kills the off-diagonal part."],
  conn=r"<strong>The perfect grid.</strong> For a normal edit you can always draw a square grid of rulers such that the edit only stretches each ruler. Nothing is leaned or sheared.",
  cap="A normal T has an orthonormal eigen-grid u₁, u₂: A = UDU* with U*U = I and D = diag(λⱼ)."),
21302: dict(d=d21302, stmtKind="THEOREM",
  statement=r"<b>Real spectral theorem (Axler 7.29).</b> Suppose $\mathbb F=\mathbb R$ and $T\in\mathcal L(V)$. The following are equivalent: $T$ is self-adjoint; $V$ has an orthonormal basis consisting of eigenvectors of $T$; $T$ has a diagonal matrix with respect to some orthonormal basis. In matrix form: $A=A^\top\iff A=Q\Lambda Q^\top$ with $Q^\top Q=I$ and $\Lambda$ real diagonal.",
  hint="Why is every symmetric real edit a stretch along perpendicular axes?",
  breakdown=[r"<strong>$A=A^\top$</strong> = the edit is its own partner.",
             r"<strong>$Q^\top Q=I$</strong> = perpendicular unit eigen-arrows; the key step is that a real self-adjoint edit always has a real eigenvalue (maximize $\langle Tv,v\rangle$ on the unit circle).",
             r"<strong>$\Lambda$ real diagonal</strong> = in that grid the edit stretches each axis by a real factor."],
  conn=r"<strong>Circle to ellipse.</strong> A symmetric edit turns a round sticker into an ellipse whose axes are perpendicular: those axes are the eigen-arrows, and the stretch along each is the eigenvalue.",
  cap="A symmetric edit turns the dashed circle into an ellipse with perpendicular axes q₁, q₂, stretched by λ₁, λ₂: A = QΛQᵀ."),
21303: dict(d=d21303, stmtKind="THEOREM",
  statement=r"<b>Spectral decomposition.</b> If $T$ is normal (over $\mathbb C$) or self-adjoint (over $\mathbb R$) with distinct eigenvalues $\lambda_1,\dots,\lambda_m$, and $P_j$ is the orthogonal projection onto $E(\lambda_j,T)$, then $T=\sum_j\lambda_jP_j$, $\sum_jP_j=I$, $P_iP_j=0$ for $i\ne j$, and $P_j^*=P_j$. Equivalently $A=\sum_k\lambda_ku_ku_k^*$ over an orthonormal eigenbasis.",
  hint="How can you rebuild the edit from shadows and stretch factors?",
  breakdown=[r"<strong>$P_j$</strong> = cast the shadow of an arrow onto the eigenspace $E(\lambda_j)$.",
             r"<strong>$\lambda_jP_j$</strong> = stretch that shadow by its factor, then add all the pieces: $T=\sum\lambda_jP_j$.",
             r"<strong>$\sum P_j=I,\ P_iP_j=0$</strong> = the shadows rebuild the whole arrow, and different eigenspaces do not overlap."],
  conn=r"<strong>Split, stretch, add back.</strong> Break an arrow into its shadows on the perpendicular eigen-rulers, stretch each shadow by its own factor, and add them up. That is the whole edit.",
  cap="T = λ₁P₁ + λ₂P₂: shadows on the eigenspaces, each stretched by its factor, with ΣPⱼ = I and PᵢPⱼ = 0."),
21304: dict(d=d21304, stmtKind="DEFINITION",
  statement=r"<b>Functional calculus.</b> For $T=\sum_j\lambda_jP_j$ normal (or self-adjoint) and a function $f$ defined on its eigenvalues, $f(T)=\sum_jf(\lambda_j)P_j=Uf(D)U^*$. For polynomials this agrees with substituting $T$; it defines $e^{T}$, $\sqrt T$ (for $\lambda_j\ge0$), and $T^{-1}$ (for $\lambda_j\ne0$).",
  hint="How do you take the square root or the exponential of a stretch edit?",
  breakdown=[r"<strong>$f(T)=\sum_jf(\lambda_j)P_j$</strong> = keep the same square grid, change each stretch factor $\lambda_j$ to $f(\lambda_j)$.",
             r"<strong>$=Uf(D)U^*$</strong> = rotate to the grid, apply $f$ to the diagonal, rotate back.",
             r"<strong>$e^T,\ \sqrt T,\ T^{-1}$</strong> = all come for free this way."],
  conn=r"<strong>Half the stretch.</strong> The square root of 'stretch by 4 horizontally and 9 vertically' is 'stretch by 2 and 3'. Same axes, new factors.",
  cap="f(T) keeps the eigen-grid and replaces each factor λⱼ by f(λⱼ): f(T) = Σ f(λⱼ)Pⱼ = Uf(D)U*."),
21305: dict(d=d21305, stmtKind="WORKED EXAMPLE",
  statement=r"<b>Counterexample.</b> $A=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$ is normal ($AA^\top=A^\top A=I$) but not symmetric, and has eigenvalues $\pm i$. Over $\mathbb C$ it is unitarily diagonalizable; over $\mathbb R$ it has no eigenvector. Over $\mathbb R$ a normal operator is block diagonal with $1\times1$ and $2\times2$ rotation-scaling blocks.",
  hint="Which normal edit has no real eigen-arrow at all?",
  breakdown=[r"<strong>Over $\mathbb R$: $A=Q\Lambda Q^\top\iff A=A^\top$</strong> = real diagonalization in a square grid needs symmetry.",
             r"<strong>Over $\mathbb C$: $A=UDU^*\iff AA^*=A^*A$</strong> = complex diagonalization needs only normality.",
             r"<strong>$\lambda=\pm i$</strong> = a 90° rotation turns every real arrow, so no real eigen-arrow exists."],
  conn=r"<strong>The rotate tool.</strong> Rotating a photo by 90° keeps all lengths and commutes with its partner, but every arrow turns. It is diagonal only if you allow complex arrows.",
  cap="A = [0 −1; 1 0] rotates every arrow by 90°: it is normal but not symmetric, with λ = ±i and no real eigen-arrow."),
21306: dict(d=d21306, stmtKind="WORKED EXAMPLE",
  statement=r"<b>Example.</b> $A=\begin{pmatrix}2&1\\1&2\end{pmatrix}$ has $\lambda=3,1$ with $u_1=\tfrac1{\sqrt2}(1,1)$, $u_2=\tfrac1{\sqrt2}(1,-1)$. $P_1=u_1u_1^\top=\tfrac12\begin{pmatrix}1&1\\1&1\end{pmatrix}$, $P_2=\tfrac12\begin{pmatrix}1&-1\\-1&1\end{pmatrix}$. Then $A=3P_1+P_2$, $\sqrt A=\sqrt3P_1+P_2$, $A^k=3^kP_1+P_2$.",
  hint="Split this edit into two shadow-stretches. What are √A and Aᵏ?",
  breakdown=[r"<strong>$A=3P_1+1\cdot P_2$</strong> = stretch the diagonal shadow by 3, leave the anti-diagonal shadow alone.",
             r"<strong>$\sqrt A=\sqrt3P_1+P_2$</strong> = same shadows, square-rooted factors.",
             r"<strong>$A^k=3^kP_1+P_2$</strong> = repeating the edit only powers the factors."],
  conn=r"<strong>Stretch along the diagonal.</strong> This edit triples arrows along $(1,1)$ and leaves arrows along $(1,-1)$ unchanged.",
  cap="A stretches u₁ = (1,1)/√2 by 3 and keeps u₂ = (1,−1)/√2: A = 3P₁ + P₂, √A = √3P₁ + P₂, Aᵏ = 3ᵏP₁ + P₂."),
}

STORY = {
 21301: dict(s="STORY 13 · STEP 1 · THE PERFECT GRID (ℂ)", b="The highlight of the course: <b>normal</b> edits are exactly the ones that are pure stretches in a <b>square grid</b>.",
   f=[["21204", "normal operators"], ["20604", "diagonalization"]], n=[["21302", "the real version"], ["21303", "as a sum of shadows"]]),
 21302: dict(s="STORY 13 · STEP 2 · THE PERFECT GRID (ℝ)", b="Over $\\mathbb R$ the condition is <b>symmetry</b>: $A=Q\\Lambda Q^\\top$.",
   f=[["21203", "self-adjoint"]], n=[["21303", "spectral decomposition"], ["21305", "the trap"]]),
 21303: dict(s="STORY 13 · STEP 3 · SHADOWS AND FACTORS", b="Equivalently, $T=\\sum\\lambda_jP_j$: shadows on the eigenspaces, each stretched.",
   f=[["21301", "orthonormal eigenbasis"], ["21104", "projections"]], n=[["21304", "functions of T"], ["21306", "an example"]]),
 21304: dict(s="STORY 13 · STEP 4 · NEW FACTORS", b="Any function of the edit is the <b>same grid with new stretch factors</b> $f(\\lambda_j)$.",
   f=[["21303", "spectral decomposition"]], n=[["21402", "the square root"], ["20905", "functions via Jordan form"]]),
 21305: dict(s="STORY 13 · STEP 5 · THE TRAP", b="Normal is enough over $\\mathbb C$, but over $\\mathbb R$ you need <b>symmetric</b>: a rotation is the classic counterexample.",
   f=[["21301", "complex version"], ["21302", "real version"]], n=[["21403", "rotations are isometries"]]),
 21306: dict(s="STORY 13 · STEP 6 · WITH NUMBERS", b="A full spectral decomposition, with $\\sqrt A$ and $A^k$.",
   f=[["21303", "decomposition"], ["21304", "f(A)"]], n=[["21401", "positive edits"]]),
}

FIX = {cid: {"stmtKind": v["stmtKind"], "statement": v["statement"], "hint": v["hint"], "breakdown": v["breakdown"],
             "personalConnection": v["conn"], "drawingSvg": v["d"](cid), "drawingCaption": v["cap"],
             "textbookImg": None, "textbookRef": None} for cid, v in CARDS.items()}
