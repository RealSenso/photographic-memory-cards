"""LAA topic 09 (Jordan form, functions of matrices). Photo picture: a Jordan block is a
zoom by λ plus a shear that pushes each grid arrow onto the previous one."""
from laa_lib import *

SUBJECT = "LAA"

def mat(x, y, rows, w=16, h=12, sz=7.5):
    out = [L(x - 3, y - 9, x - 3, y + h * len(rows) - 6, .9), L(x + w * len(rows[0]) - 4, y - 9, x + w * len(rows[0]) - 4, y + h * len(rows) - 6, .9)]
    for i, r in enumerate(rows):
        for j, v in enumerate(r):
            out.append(N(x + w * j + 5, y + h * i, v, sz, "middle"))
    return "".join(out)

def d20901(c):
    O = (50, 108)
    return svg(c,
        N(120, 12, "Jₖ(λ) = λIₖ + Nₖ: zoom by λ plus a shear", 7.5, "middle"),
        mat(20, 34, [["λ", "1", "0"], ["0", "λ", "1"], ["0", "0", "λ"]]),
        pin(*O, None), vec(O, (92, 108), "Je₁ = λe₁", 0, 10, "middle", 7), vec(O, (50, 74), "e₂", -4, 0, "end", 7),
        vec(O, (92, 66), "Je₂ = λe₂ + e₁", 4, -2, "start", 7),
        N(236, 30, "one eigenvector only (e₁)", 7, "end"), N(236, 44, "(J − λI)ᵏ = 0", 7.5, "end"), N(236, 56, "(J − λI)ᵏ⁻¹ ≠ 0", 7.5, "end"),
        N(236, 70, "min. poly (z − λ)ᵏ", 7, "end"))

def d20902(c):
    return svg(c,
        N(120, 12, "every complex edit, in the right grid", 7.5, "middle"),
        R(40, 22, 120, 104, "#ffffff", 1, 3),
        R(40, 22, 48, 48, "#d9dee7", 1, 0), N(64, 50, "J₃(λ₁)", 7.5, "middle"),
        R(88, 70, 32, 32, "#d9dee7", 1, 0), N(104, 90, "J₂(λ₂)", 7, "middle"),
        R(120, 102, 24, 24, "#d9dee7", 1, 0), N(132, 117, "J₁", 7, "middle"),
        N(34, 76, "J =", 9, "end"),
        N(236, 50, "A = PJP⁻¹", 8.5, "end"), N(236, 66, "blocks unique", 7, "end"), N(236, 76, "up to order", 7, "end"),
        N(236, 104, "similar ⇔ same J", 7.5, "end"),
        N(120, 140, "all blocks 1×1 ⇔ diagonalizable", 7.5, "middle"))

def d20903(c):
    rows = [3, 1]
    out = [N(120, 12, "blocks of size ≥ k = dim null(A − λI)ᵏ − dim null(A − λI)ᵏ⁻¹", 7, "middle")]
    for j, n in enumerate(rows):
        for k in range(n):
            out.append(R(26 + 26 * k, 34 + 26 * j, 22, 20, "#d9dee7", 1, 2))
        out.append(N(26 + 26 * 3 + 6, 48 + 26 * j, f"block of size {n}", 7, "start"))
    out += [N(14, 104, "column k counts blocks of size ≥ k:", 7.5, "start"),
            N(14, 116, "k = 1: 2,  k = 2: 1,  k = 3: 1", 7.5, "start"),
            N(14, 130, "number of blocks = dim null(A − λI)", 7.5, "start")]
    return svg(c, *out)

def d20904(c):
    return svg(c,
        N(120, 12, "read both polynomials off the blocks of λ", 7.5, "middle"),
        R(20, 28, 66, 22, "#d9dee7", 1, 2), N(53, 43, "size 3", 7.5, "middle"),
        R(92, 28, 44, 22, "#d9dee7", 1, 2), N(114, 43, "size 2", 7.5, "middle"),
        R(142, 28, 22, 22, "#d9dee7", 1, 2), N(153, 43, "1", 7.5, "middle"),
        N(120, 74, "characteristic: exponent = sum = 3 + 2 + 1 = 6", 7.5, "middle"),
        N(120, 88, "minimal: exponent = largest = 3", 7.5, "middle"),
        N(120, 112, "p = Π (z − λ)^(Σ kᵢ),   q = Π (z − λ)^(max kᵢ)", 7.5, "middle"),
        N(120, 132, "diagonalizable ⇔ every max exponent is 1", 7.5, "middle"))

def d20905(c):
    xs = lambda t: 20 + 50 * t
    ys = lambda v: 120 - 16 * v
    return svg(c,
        L(14, 120, 230, 120, .8, ar=True), N(230, 132, "t", 8, "end"), L(20, 126, 20, 20, .8, ar=True),
        poly([(xs(t / 20), ys(1)) for t in range(0, 81)], 1.1, "3 2"), N(220, ys(1) - 4, "e^(λt), λ = 0", 7, "end"),
        poly([(xs(t / 20), ys(1 + t / 20)) for t in range(0, 81)], 1.1), N(220, ys(4.4), "e^(λt)(1 + t)", 7, "end"),
        N(120, 12, "f(Jₖ(λ)) = Σⱼ f⁽ʲ⁾(λ)/j! · Nʲ", 8, "middle"),
        N(30, 36, "e^(tJ) = e^(λt)(I + tN + t²N²/2 + …)", 7.2, "start"),
        N(30, 48, "e^(tA) = P e^(tJ) P⁻¹ solves x′ = Ax", 7.2, "start"),
        N(120, 140, "the shear adds polynomial growth tᵏ⁻¹ to the exponential", 7, "middle"))

def d20906(c):
    return svg(c,
        N(120, 12, "λ = 2, algebraic multiplicity 4", 8, "middle"),
        N(14, 34, "dim null(A − 2I)ᵏ, k = 1, 2, 3:  2, 3, 4", 7.5, "start"),
        N(14, 48, "increments: 2, 1, 1", 7.5, "start"),
        N(14, 62, "⇒ 2 blocks, 1 of size ≥ 2, 1 of size ≥ 3", 7.5, "start"),
        mat(140, 84, [["2", "1", "0", "0"], ["0", "2", "1", "0"], ["0", "0", "2", "0"], ["0", "0", "0", "2"]], 15, 12, 7.5),
        N(132, 102, "J =", 8.5, "end"),
        N(14, 92, "J = J₃(2) ⊕ J₁(2)", 7.5, "start"), N(14, 106, "q = (z − 2)³", 7.5, "start"), N(14, 120, "not diagonalizable", 7.5, "start"))

CARDS = {
20901: dict(d=d20901, stmtKind="DEFINITION",
  statement=r"<b>Jordan block.</b> For $\lambda\in\mathbb F$ and $k\ge1$, $J_k(\lambda)=\lambda I_k+N_k$, where $N_k$ has $1$ on the superdiagonal and $0$ elsewhere. It has the single eigenvalue $\lambda$ with algebraic multiplicity $k$, geometric multiplicity $1$, and $(J_k(\lambda)-\lambda I)^k=0\ne(J_k(\lambda)-\lambda I)^{k-1}$, so its minimal polynomial is $(z-\lambda)^k$.",
  hint="What does the simplest edit look like that is a zoom but can't be made diagonal?",
  breakdown=[r"<strong>$J_k(\lambda)=\lambda I+N_k$</strong> = zoom by $\lambda$, plus a shear that adds each grid arrow to the previous one.",
             r"<strong>$(J-\lambda I)^k=0$</strong> = remove the zoom and the shear flattens everything after $k$ steps.",
             r"<strong>$(J-\lambda I)^{k-1}\ne0$</strong> = and not sooner: one eigen-arrow only, as far from diagonal as possible."],
  conn=r"<strong>Zoom with a lean.</strong> A 2×2 block zooms the photo by $\lambda$ and leans the vertical arrows sideways by one horizontal step. The horizontal arrow is the only one that keeps its direction.",
  cap="J = λI + N zooms e₁ to λe₁ but sends e₂ to λe₂ + e₁ (a lean); (J − λI)ᵏ = 0 while (J − λI)ᵏ⁻¹ ≠ 0."),
20902: dict(d=d20902, stmtKind="THEOREM",
  statement=r"<b>Jordan form (Axler 8.46).</b> Suppose $V$ is a finite-dimensional complex vector space and $T\in\mathcal L(V)$. Then there is a basis of $V$ (a Jordan basis) in which the matrix of $T$ is block diagonal, $J=\operatorname{diag}(J_{k_1}(\lambda_1),\dots,J_{k_r}(\lambda_r))$. The blocks are unique up to order, so two matrices are similar iff they have the same Jordan form.",
  hint="What is the simplest grid you can always find for any complex edit?",
  breakdown=[r"<strong>$A=PJP^{-1}$</strong> = the columns of $P$ are a Jordan basis: chains of generalized eigenvectors.",
             r"<strong>$J=\operatorname{diag}(J_{k_i}(\lambda_i))$</strong> = in that grid the edit is a list of independent zoom-plus-lean blocks.",
             r"<strong>unique up to order</strong> = the block sizes are a complete fingerprint: same $J$ ⇔ similar."],
  conn=r"<strong>The universal recipe card.</strong> Every complex edit, in the right grid, is just a few blocks, each 'zoom by $\lambda$ and lean'. When all blocks are 1×1 there is no lean and the edit is diagonal.",
  cap="In a Jordan basis every complex edit is block diagonal, J = diag(J₃(λ₁), J₂(λ₂), J₁), and A = PJP⁻¹."),
20903: dict(d=d20903, stmtKind="PROPOSITION",
  statement=r"<b>Counting Jordan blocks.</b> For an eigenvalue $\lambda$ of $A$: the number of Jordan blocks for $\lambda$ is $\dim\operatorname{null}(A-\lambda I)$, and the number of blocks of size $\ge k$ is $\dim\operatorname{null}(A-\lambda I)^k-\dim\operatorname{null}(A-\lambda I)^{k-1}$.",
  hint="How can you find the block sizes without computing a Jordan basis?",
  breakdown=[r"<strong>$\dim\operatorname{null}(A-\lambda I)$</strong> = one eigen-arrow per block, so this counts the blocks.",
             r"<strong>difference at step $k$</strong> = each extra power kills one more arrow in every block that is still alive, i.e. every block of size $\ge k$.",
             r"<strong>Procedure:</strong> compute the null-space dimensions until they reach the multiplicity, then read the block sizes off the increments."],
  conn=r"<strong>Counting by flattening.</strong> Apply the leftover shear again and again and count how many new directions disappear each time: long blocks keep contributing, short ones stop early.",
  cap="Blocks of sizes 3 and 1 for λ: the increments of dim null(A − λI)ᵏ are 2, 1, 1, the number of blocks of size ≥ k."),
20904: dict(d=d20904, stmtKind="PROPOSITION",
  statement=r"<b>Polynomials from the Jordan form.</b> If $A$ has Jordan blocks of sizes $k_i(\lambda)$ for each eigenvalue $\lambda$, then $p_A(z)=\prod_\lambda(z-\lambda)^{\sum_ik_i(\lambda)}$ and $q_A(z)=\prod_\lambda(z-\lambda)^{\max_ik_i(\lambda)}$. $A$ is diagonalizable iff every $\max_ik_i(\lambda)=1$.",
  hint="Which block sets the exponent of the characteristic polynomial, and which the minimal one?",
  breakdown=[r"<strong>$\sum_ik_i(\lambda)$</strong> = the characteristic exponent adds the sizes of all blocks for $\lambda$ (algebraic multiplicity).",
             r"<strong>$\max_ik_i(\lambda)$</strong> = the minimal exponent is the size of the largest block, since $(J_k-\lambda)^m=0$ iff $m\ge k$.",
             r"<strong>all max $=1$</strong> = no block is longer than 1, so the edit is diagonal."],
  conn=r"<strong>The longest lean sets the pace.</strong> To wipe out every block you need as many steps as the longest one; the total count of directions is the sum of all.",
  cap="Blocks of sizes 3, 2, 1 for λ: the characteristic exponent is 3 + 2 + 1 = 6, the minimal exponent is max = 3."),
20905: dict(d=d20905, stmtKind="PROPOSITION",
  statement=r"<b>Functions of a Jordan block.</b> For $f$ analytic near $\lambda$, $f(J_k(\lambda))=\sum_{j=0}^{k-1}\frac{f^{(j)}(\lambda)}{j!}N^j$, since $N^k=0$. If $A=PJP^{-1}$ then $f(A)=Pf(J)P^{-1}$. In particular $e^{tJ_k(\lambda)}=e^{\lambda t}\left(I+tN+\dots+\tfrac{t^{k-1}}{(k-1)!}N^{k-1}\right)$, and $x(t)=e^{tA}x_0$ solves $x'=Ax$.",
  hint="Why does a Jordan block make the exponential grow like t·e^(λt)?",
  breakdown=[r"<strong>$\sum_j\frac{f^{(j)}(\lambda)}{j!}N^j$</strong> = Taylor expand $f$ around $\lambda$; the series stops because $N^k=0$.",
             r"<strong>$e^{tJ}=e^{\lambda t}(I+tN+\dots)$</strong> = the zoom gives $e^{\lambda t}$, the lean adds powers of $t$.",
             r"<strong>$e^{tA}=Pe^{tJ}P^{-1}$</strong> = compute in the Jordan grid, then change back."],
  conn=r"<strong>A zoom that keeps leaning.</strong> Play the edit continuously as a video: the zoom grows exponentially, and the lean adds a drift that grows with time, like $t\,e^{\lambda t}$.",
  cap="e^(tJ) = e^(λt)(I + tN + …): with λ = 0 the zoom stays flat (dashed) and the lean adds growth (1 + t) (solid)."),
20906: dict(d=d20906, stmtKind="WORKED EXAMPLE",
  statement=r"<b>Example.</b> Eigenvalue $2$ with algebraic multiplicity $4$, and $\dim\operatorname{null}(A-2I)^k=2,3,4$ for $k=1,2,3$. Increments $2,1,1$: two blocks, one of size $\ge2$, one of size $\ge3$. Hence $J=J_3(2)\oplus J_1(2)$, $q_A=(z-2)^3$, and $A$ is not diagonalizable.",
  hint="From the null-space sizes 2, 3, 4, which blocks does the edit have?",
  breakdown=[r"<strong>$\dim\operatorname{null}(A-2I)=2$</strong> = two blocks.",
             r"<strong>increments $1,1$ at $k=2,3$</strong> = one block survives to size 3; the other stops at size 1.",
             r"<strong>$J_3(2)\oplus J_1(2)$, $q=(z-2)^3$</strong> = sizes $3+1=4$ check out; the largest block gives the minimal exponent."],
  conn=r"<strong>Two zooms by 2, one with a long lean.</strong> One direction is a clean zoom; the other three form a chain that takes three steps to flatten.",
  cap="Increments 2, 1, 1 of dim null(A − 2I)ᵏ give J = J₃(2) ⊕ J₁(2) with q = (z − 2)³."),
}

STORY = {
 20901: dict(s="STORY 9 · STEP 1 · ZOOM WITH A LEAN", b="The building block of every complex edit: a <b>Jordan block</b>, a zoom by $\\lambda$ plus a lean.",
   f=[["20805", "chains give Jordan blocks"]], n=[["20902", "every edit is made of them"]]),
 20902: dict(s="STORY 9 · STEP 2 · THE UNIVERSAL GRID", b="<b>Jordan form</b>: in a suitable grid every complex edit is a list of Jordan blocks, unique up to order.",
   f=[["20803", "generalized eigenspaces"], ["20901", "Jordan blocks"]], n=[["20903", "count the blocks"], ["20905", "functions of the edit"]]),
 20903: dict(s="STORY 9 · STEP 3 · COUNT THE BLOCKS", b="Block sizes come from the <b>null-space dimensions</b> of powers of $A-\\lambda I$.",
   f=[["20902", "Jordan form"], ["20806", "chain counting"]], n=[["20904", "the polynomials"], ["20906", "do it with numbers"]]),
 20904: dict(s="STORY 9 · STEP 4 · THE POLYNOMIALS", b="Characteristic exponent = <b>sum</b> of block sizes; minimal exponent = <b>largest</b> block.",
   f=[["20903", "block sizes"], ["20504", "two fingerprints"]], n=[["20905", "functions of matrices"]]),
 20905: dict(s="STORY 9 · STEP 5 · PLAY IT AS A VIDEO", b="Functions like $e^{tA}$ are computed block by block; the lean adds powers of $t$.",
   f=[["20902", "A = PJP⁻¹"]], n=[["20906", "practice"], ["21001", "next: measuring lengths and angles"]]),
 20906: dict(s="STORY 9 · STEP 6 · WITH NUMBERS", b="Read a Jordan form straight from kernel dimensions.",
   f=[["20903", "block counting"]], n=[["21001", "angles and lengths enter the story"]]),
}

FIX = {cid: {"stmtKind": v["stmtKind"], "statement": v["statement"], "hint": v["hint"], "breakdown": v["breakdown"],
             "personalConnection": v["conn"], "drawingSvg": v["d"](cid), "drawingCaption": v["cap"],
             "textbookImg": None, "textbookRef": None} for cid, v in CARDS.items()}
