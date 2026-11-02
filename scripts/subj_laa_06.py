"""LAA topic 06 (eigenvalues, eigenvectors, diagonalization). Photo picture: an eigenvector
is an arrow the edit only stretches (or flips), never turns."""
from laa_lib import *

SUBJECT = "LAA"

def d20601(c):
    O = (70, 100)
    return svg(c,
        sheet([(20, 130), (120, 130), (150, 60), (50, 60)], "#ffffff", "3 2"),
        pin(*O, None),
        vec(O, (96, 84), "v", -2, -4, "end"), vec(O, (140, 58), "Tv = λv", 4, 0),
        vec(O, (40, 70), "u", -4, 0, "end", 8, "3 2"), vec(O, (24, 108), "Tu: turned", -4, 10, "start", 7.5, "3 2"),
        N(236, 92, "E(λ, T) = null(T − λI)", 7.5, "end"), N(236, 104, "= the line of v (plus 0)", 7, "end"),
        N(236, 124, "λ eigenvalue ⇔", 7.5, "end"), N(236, 136, "det(T − λI) = 0", 7.5, "end"),
        N(120, 12, "v ≠ 0 keeps its direction; only its length changes by λ", 7.5, "middle"))

def d20602(c):
    xs = lambda z: 30 + 36 * z
    p = lambda z: (z - 2) * (z - 5)
    y = lambda z: 92 - 9 * p(z)
    return svg(c,
        L(14, 92, 236, 92, .8, ar=True), N(236, 102, "λ", 8, "end"),
        poly([(xs(z / 10), y(z / 10)) for z in range(0, 60)], 1.1),
        dot(xs(2), 92, None, r=2.4), dot(xs(5), 92, None, r=2.4), N(xs(2), 104, "λ = 2", 7.5, "middle"), N(xs(5), 104, "λ = 5", 7.5, "middle"),
        N(120, 12, "pᴀ(λ) = det(λI − A) = λⁿ − (tr A)λⁿ⁻¹ + … + (−1)ⁿ det A", 7, "middle"),
        N(120, 124, "roots = eigenvalues:  Σλᵢ = tr A,  Πλᵢ = det A", 7.5, "middle"),
        N(120, 138, "then solve (A − λI)v = 0 for each root", 7, "middle"))

def d20603(c):
    O = (70, 100)
    return svg(c,
        pin(*O, None),
        vec(O, (110, 100), "v₁ (λ₁)", 0, 10, "middle", 7.5), vec(O, (90, 64), "v₂ (λ₂)", -4, -2, "end", 7.5),
        N(236, 30, "a₁v₁ + a₂v₂ = 0", 7.5, "end"), N(236, 42, "apply T − λ₂I:", 7.5, "end"), N(236, 54, "a₁(λ₁ − λ₂)v₁ = 0", 7.5, "end"),
        N(236, 66, "λ₁ ≠ λ₂ ⇒ a₁ = 0, then a₂ = 0", 7.5, "end"),
        N(236, 102, "distinct λ ⇒ independent", 7.5, "end"), N(236, 114, "at most dim V distinct λ", 7.5, "end"),
        N(12, 14, "different stretch factors, different directions", 7.5, "start"))

def d20604(c):
    O = (56, 104)
    a, b = (28, -14), (10, -26)
    p = lambda i, j: (O[0] + i * a[0] + j * b[0], O[1] + i * a[1] + j * b[1])
    g = [L(*p(i, 0), *p(i, 3), .5, "2 2") for i in range(4)] + [L(*p(0, j), *p(3, j), .5, "2 2") for j in range(4)]
    return svg(c, *g, pin(*O, None),
        vec(O, p(1, 0), "v₁", 2, 10, "middle", 7.5), vec(O, p(0, 1), "v₂", -4, 0, "end", 7.5),
        N(236, 20, "a grid of eigen-arrows", 7.5, "end"),
        N(236, 40, "A = PDP⁻¹", 8.5, "end"), N(236, 52, "P = [v₁ ⋯ vₙ]", 7.5, "end"), N(236, 64, "D = diag(λ₁, …, λₙ)", 7.5, "end"),
        N(236, 88, "in this grid the edit", 7, "end"), N(236, 98, "is a pure stretch", 7, "end"),
        N(236, 120, "Aᵏ = PDᵏP⁻¹", 8.5, "end"), N(236, 132, "repeat k times: λᵢᵏ", 7, "end"))

def d20605(c):
    return svg(c,
        N(120, 12, "1 ≤ geometric ≤ algebraic", 8.5, "middle"),
        R(16, 28, 96, 22, "#f1f5f9", 1, 3), N(64, 43, "λ root twice: alg = 2", 7.2, "middle"),
        R(128, 28, 96, 22, "#f1f5f9", 1, 3), N(176, 43, "λ root twice: alg = 2", 7.2, "middle"),
        pin(64, 104, None), vec((64, 104), (98, 104), None), vec((64, 104), (64, 70), None),
        N(64, 122, "dim E(λ) = 2", 7.5, "middle"), N(64, 134, "equal ✓ diagonalizable", 7, "middle"),
        pin(176, 104, None), vec((176, 104), (210, 104), None),
        N(176, 122, "dim E(λ) = 1 < 2", 7.5, "middle"), N(176, 134, "defective ✗", 7, "middle"))

def d20606(c):
    O = (80, 92)
    s = 8
    P = lambda x, y: (O[0] + s * x, O[1] - s * y)
    return svg(c,
        L(14, 92, 150, 92, .6), L(80, 140, 80, 6, .6), pin(*O, None),
        vec(O, P(1, 1), "(1,1)", -2, -4, "end", 7.5), vec(O, P(5, 5), "A(1,1) = (5,5)", 4, 0, "start", 7.5),
        vec(O, P(1, -2), "(1,−2)", -4, 8, "end", 7.5), vec(O, P(2, -4), "A(1,−2) = (2,−4)", 4, 8, "start", 7.5),
        N(236, 20, "A = [4 1; 2 3]", 8, "end"), N(236, 32, "tr 7, det 10", 7.5, "end"), N(236, 44, "λ² − 7λ + 10 = 0", 7.5, "end"),
        N(236, 56, "λ = 5, 2", 7.5, "end"),
        N(236, 70, "A = PDP⁻¹, D = diag(5, 2)", 7.2, "end"), N(236, 82, "P = [(1,1) (1,−2)]", 7.2, "end"))

CARDS = {
20601: dict(d=d20601, stmtKind="DEFINITION",
  statement=r"<b>Eigenvalue and eigenvector (Axler 5.5, 5.8, 5.52).</b> For $T\in\mathcal L(V)$, $\lambda\in\mathbb F$ is an eigenvalue of $T$ if there is $v\ne0$ with $Tv=\lambda v$; such $v$ is an eigenvector. The eigenspace is $E(\lambda,T)=\operatorname{null}(T-\lambda I)$. For finite-dimensional $V$: $\lambda$ is an eigenvalue $\iff T-\lambda I$ is not invertible $\iff\det(T-\lambda I)=0$.",
  hint="Which arrows does an edit leave pointing the same way?",
  breakdown=[r"<strong>$Tv=\lambda v,\ v\ne0$</strong> = the edit does not turn $v$; it only stretches it by $\lambda$ (or flips it if $\lambda\lt0$).",
             r"<strong>$E(\lambda,T)=\operatorname{null}(T-\lambda I)$</strong> = all arrows stretched by the same $\lambda$, plus the pin: a subspace.",
             r"<strong>$\det(T-\lambda I)=0$</strong> = subtracting the stretch leaves an edit that squashes $v$, so it is not invertible."],
  conn=r"<strong>The directions a stretch filter leaves alone.</strong> Stretch a photo horizontally: horizontal arrows stay horizontal (eigenvalue 2), vertical arrows stay vertical (eigenvalue 1), and diagonal arrows get turned.",
  cap="The edit sends v to Tv = λv along the same line, while u is turned. E(λ, T) = null(T − λI), and λ is an eigenvalue ⇔ det(T − λI) = 0."),
20602: dict(d=d20602, stmtKind="PROPOSITION",
  statement=r"<b>Characteristic polynomial.</b> For $A\in\mathbb F^{n\times n}$, $p_A(\lambda)=\det(\lambda I-A)$ is monic of degree $n$ with $p_A(\lambda)=\lambda^n-(\operatorname{tr}A)\lambda^{n-1}+\dots+(-1)^n\det A$. The eigenvalues of $A$ are its roots; over $\mathbb C$ (with multiplicity) they sum to $\operatorname{tr}A$ and multiply to $\det A$.",
  hint="How do you find the stretch factors of an edit with a pencil?",
  breakdown=[r"<strong>$\det(\lambda I-A)$</strong> = zero exactly when $\lambda I-A$ squashes some arrow, i.e. when $\lambda$ is a stretch factor.",
             r"<strong>$-\operatorname{tr}(A)\lambda^{n-1}$</strong> = the second coefficient: the eigenvalues add up to the trace.",
             r"<strong>$(-1)^n\det A$</strong> = the constant term: the eigenvalues multiply to the determinant (the area scale)."],
  conn=r"<strong>Checking your answer quickly.</strong> For a 2×2 edit, the two stretch factors must add to the trace and multiply to the area scale. That is all you need to write $\lambda^2-(\operatorname{tr})\lambda+\det=0$.",
  cap="pᴀ(λ) = det(λI − A) crosses zero at the eigenvalues (here 2 and 5); its coefficients give Σλᵢ = tr A and Πλᵢ = det A."),
20603: dict(d=d20603, stmtKind="THEOREM",
  statement=r"<b>Linearly independent eigenvectors (Axler 5.11, 5.12).</b> Let $T\in\mathcal L(V)$. Eigenvectors corresponding to distinct eigenvalues of $T$ are linearly independent. Hence each operator on $V$ has at most $\dim V$ distinct eigenvalues.",
  hint="Why can't two arrows with different stretch factors point along the same line?",
  breakdown=[r"<strong>$\lambda_i$ distinct</strong> = each arrow is stretched by its own factor.",
             r"<strong>$\Rightarrow v_1,\dots,v_m$ independent</strong> = suppose a mix gives 0; apply $T-\lambda_mI$ to kill the last arrow, and the factors $\lambda_j-\lambda_m\ne0$ force every coefficient to vanish (induction).",
             r"<strong>$\#\{\lambda\}\le\dim V$</strong> = independent arrows cannot outnumber the dimension."],
  conn=r"<strong>One line, one stretch.</strong> An arrow on a line is stretched by one fixed factor. Two arrows stretched by different factors must lie on different lines, and arrows with all-different factors never tangle.",
  cap="v₁ and v₂ have different stretch factors λ₁ ≠ λ₂; applying T − λ₂I to a₁v₁ + a₂v₂ = 0 forces a₁ = a₂ = 0, so they are independent."),
20604: dict(d=d20604, stmtKind="THEOREM",
  statement=r"<b>Conditions equivalent to diagonalizability (Axler 5.55, 5.58).</b> For $T\in\mathcal L(V)$, $\dim V=n$, with distinct eigenvalues $\lambda_1,\dots,\lambda_m$, the following are equivalent: $T$ is diagonalizable; $V$ has a basis of eigenvectors of $T$; $V=E(\lambda_1,T)\oplus\dots\oplus E(\lambda_m,T)$; $n=\sum_j\dim E(\lambda_j,T)$. In matrix form $A=PDP^{-1}$ and $A^k=PD^kP^{-1}$. If $T$ has $n$ distinct eigenvalues it is diagonalizable.",
  hint="When can you draw a grid in which the edit is just a stretch along each grid line?",
  breakdown=[r"<strong>$P=[v_1\cdots v_n]$</strong> = the eigen-arrows as the new grid.",
             r"<strong>$D=\operatorname{diag}(\lambda_1,\dots,\lambda_n)$</strong> = in that grid, the edit stretches each grid direction by its own factor.",
             r"<strong>$A^k=PD^kP^{-1}$</strong> = repeating the edit $k$ times just raises each stretch factor to the $k$-th power."],
  conn=r"<strong>The best grid.</strong> Find enough arrows that the edit only stretches, use them as your grid, and the messy edit becomes 'stretch this way by 5, that way by 2'. Repeating it 100 times is then trivial.",
  cap="Eigen-arrows v₁, v₂ make a grid in which the edit is a pure stretch: A = PDP⁻¹ with P = [v₁ v₂], D = diag(λᵢ), and Aᵏ = PDᵏP⁻¹."),
20605: dict(d=d20605, stmtKind="PROPOSITION",
  statement=r"<b>Multiplicities.</b> For an eigenvalue $\lambda$ of $T\in\mathcal L(V)$, the algebraic multiplicity is its multiplicity as a root of the characteristic polynomial and the geometric multiplicity is $\dim E(\lambda,T)$. Always $1\le\dim E(\lambda,T)\le$ algebraic multiplicity; $T$ is diagonalizable iff equality holds for every eigenvalue.",
  hint="A stretch factor appears twice in the polynomial. Are there always two eigen-arrows for it?",
  breakdown=[r"<strong>algebraic multiplicity</strong> = how many times $\lambda$ is a root of $p_T$.",
             r"<strong>$\dim E(\lambda,T)$</strong> = how many independent arrows the edit actually stretches by $\lambda$.",
             r"<strong>equal for all $\lambda$ ⇔ diagonalizable</strong> = if some $\lambda$ is short of eigen-arrows (defective), the gap is filled by generalized eigenvectors."],
  conn=r"<strong>Promised versus delivered.</strong> The polynomial promises two directions stretched by 2. A pure zoom delivers both; a zoom with a shear delivers only one, and the photo cannot be gridded by eigen-arrows.",
  cap="Both edits have λ as a double root (alg = 2). Left: dim E(λ) = 2, diagonalizable. Right: dim E(λ) = 1 < 2, defective."),
20606: dict(d=d20606, stmtKind="WORKED EXAMPLE",
  statement=r"<b>Example.</b> $A=\begin{pmatrix}4&1\\2&3\end{pmatrix}$: $\operatorname{tr}A=7$, $\det A=10$, so $\lambda^2-7\lambda+10=(\lambda-5)(\lambda-2)$. Eigenvectors: $(1,1)$ for $5$ and $(1,-2)$ for $2$. Hence $A=PDP^{-1}$ with $P=\begin{pmatrix}1&1\\1&-2\end{pmatrix}$, $D=\operatorname{diag}(5,2)$.",
  hint="Which two arrows does this edit only stretch, and by how much?",
  breakdown=[r"<strong>$\lambda^2-7\lambda+10$</strong> = trace 7, determinant 10, roots 5 and 2 (distinct, so diagonalizable).",
             r"<strong>$A(1,1)=(5,5)$, $A(1,-2)=(2,-4)$</strong> = each eigen-arrow just gets longer by its factor.",
             r"<strong>$P$, $D$</strong> = the eigen-arrows as columns of $P$, the factors on the diagonal of $D$."],
  conn=r"<strong>Finding the grid by hand.</strong> This edit stretches the diagonal $(1,1)$ by 5 and the arrow $(1,-2)$ by 2. In the grid made of those two arrows, it is just two stretches.",
  cap="A stretches (1,1) to (5,5) and (1,−2) to (2,−4), so A = PDP⁻¹ with D = diag(5, 2)."),
}

STORY = {
 20601: dict(s="STORY 6 · STEP 1 · ARROWS THAT DON'T TURN", b="The key idea of the course: look for arrows the edit only <b>stretches</b>. Those are eigenvectors, and their stretch factors are eigenvalues.",
   f=[["20502", "they exist over ℂ"], ["20403", "not invertible ⇔ squashes something"]], n=[["20602", "find the factors"], ["20603", "they never tangle"]]),
 20602: dict(s="STORY 6 · STEP 2 · FIND THE FACTORS", b="The <b>characteristic polynomial</b> finds the stretch factors; trace and determinant check them.",
   f=[["20601", "eigenvalues"], ["20405", "trace and det are grid-free"]], n=[["20603", "independence"], ["20606", "do it by hand"]]),
 20603: dict(s="STORY 6 · STEP 3 · THEY NEVER TANGLE", b="Arrows with <b>different stretch factors are independent</b>, so there are at most $n$ factors.",
   f=[["20601", "eigenvectors"], ["20201", "independence"]], n=[["20604", "enough of them make a grid"]]),
 20604: dict(s="STORY 6 · STEP 4 · THE BEST GRID", b="When the eigen-arrows fill the space, use them as the grid: the edit becomes a <b>diagonal</b> stretch, $A=PDP^{-1}$.",
   f=[["20603", "independent eigenvectors"], ["20404", "change of basis"]], n=[["20605", "when there are too few"], ["20703", "two edits, one grid"]]),
 20605: dict(s="STORY 6 · STEP 5 · TOO FEW ARROWS", b="Sometimes the polynomial promises more eigen-arrows than exist: <b>geometric &lt; algebraic</b> multiplicity, and no eigen-grid exists.",
   f=[["20604", "diagonalizable"], ["20505", "the minimal-polynomial test"]], n=[["20802", "generalized eigenvectors fill the gap"]]),
 20606: dict(s="STORY 6 · STEP 6 · WITH NUMBERS", b="A full diagonalization by hand.",
   f=[["20602", "characteristic polynomial"], ["20604", "PDP⁻¹"]], n=[["20701", "subspaces an edit keeps"]]),
}

FIX = {cid: {"stmtKind": v["stmtKind"], "statement": v["statement"], "hint": v["hint"], "breakdown": v["breakdown"],
             "personalConnection": v["conn"], "drawingSvg": v["d"](cid), "drawingCaption": v["cap"],
             "textbookImg": None, "textbookRef": None} for cid, v in CARDS.items()}
