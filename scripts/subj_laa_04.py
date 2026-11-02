"""LAA topic 04 (invertibility, isomorphisms, change of basis). Photo picture: an invertible
edit can be undone; a change of basis redraws the grid without changing the photo."""
from laa_lib import *

SUBJECT = "LAA"

def d20401(c):
    return svg(c,
        phone(8, 30, 60, 80, "photo"), phone(90, 30, 60, 80, "edited"), phone(172, 30, 60, 80, "photo again"),
        pin(38, 70, None), vec((38, 70), (56, 56), "v", 2, 0, "start", 7.5),
        pin(120, 70, None), vec((120, 70), (128, 46), "Tv", 2, 0, "start", 7.5),
        pin(202, 70, None), vec((202, 70), (220, 56), "v", 2, 0, "start", 7.5),
        L(70, 64, 88, 64, 1, ar=True), N(79, 58, "T", 8, "middle"),
        L(152, 64, 170, 64, 1, ar=True), N(161, 58, "T⁻¹", 8, "middle"),
        N(120, 12, "T invertible ⇔ T bijective (one-to-one and onto)", 7.5, "middle"),
        N(120, 128, "undo two edits in reverse order:", 7.5, "middle"), N(120, 140, "(ST)⁻¹ = T⁻¹S⁻¹", 8, "middle"))

def d20402(c):
    return svg(c,
        R(10, 34, 90, 70, "#ffffff", 1, 6), N(55, 30, "V: quadratics 𝒫₂", 7.5, "middle"),
        N(55, 58, "a + bx + cx²", 8, "middle"), N(55, 78, "dim 3", 7.5, "middle"),
        R(140, 34, 90, 70, "#f1f5f9", 1, 6), N(185, 30, "𝔽³: columns", 7.5, "middle"),
        N(185, 58, "(a, b, c)", 8, "middle"), N(185, 78, "dim 3", 7.5, "middle"),
        L(102, 62, 138, 62, 1, ar=True), L(138, 74, 102, 74, 1, ar=True), N(120, 56, "v ↦ [v]ʙ", 7, "middle"),
        N(120, 14, "V ≅ W ⇔ dim V = dim W", 8.5, "middle"),
        N(120, 124, "any n-dimensional space is 𝔽ⁿ in disguise", 7.5, "middle"),
        N(120, 136, "pick a basis: V ≅ 𝔽ⁿ", 7.5, "middle"))

def d20403(c):
    return svg(c,
        N(120, 12, "T: V → V, dim V finite", 8, "middle"),
        R(16, 30, 64, 30, "#f1f5f9", 1, 4), N(48, 44, "null T = {0}", 7.5, "middle"), N(48, 54, "injective", 7, "middle"),
        R(88, 30, 64, 30, "#f1f5f9", 1, 4), N(120, 44, "range T = V", 7.5, "middle"), N(120, 54, "surjective", 7, "middle"),
        R(160, 30, 64, 30, "#d9dee7", 1, 4), N(192, 44, "T⁻¹ exists", 7.5, "middle"), N(192, 54, "invertible", 7, "middle"),
        N(84, 48, "⇔", 9, "middle"), N(156, 48, "⇔", 9, "middle"),
        N(120, 84, "rank–nullity with dim W = dim V:", 7.5, "middle"),
        N(120, 96, "dim null T = 0 ⇔ dim range T = dim V", 7.5, "middle"),
        N(120, 120, "to show A is invertible, check Ax = 0 ⇒ x = 0", 7.5, "middle"),
        N(120, 132, "and ST = I ⇒ TS = I", 7.5, "middle"))

def d20404(c):
    O = (64, 104)
    p = lambda o, a, b, i, j: (o[0] + i * a[0] + j * b[0], o[1] + i * a[1] + j * b[1])
    a, b = (22, -10), (10, -24)
    g = [L(*p(O, a, b, i, 0), *p(O, a, b, i, 3), .5, "2 2") for i in range(4)] + [L(*p(O, a, b, 0, j), *p(O, a, b, 3, j), .5, "2 2") for j in range(4)]
    return svg(c, *g,
        L(14, 104, 160, 104, .6), L(64, 136, 64, 14, .6), pin(*O, None),
        vec(O, p(O, a, b, 1, 0), "b′₁", 2, 8, "start", 7.5), vec(O, p(O, a, b, 0, 1), "b′₂", -4, 0, "end", 7.5),
        N(236, 20, "same photo, new grid", 7.5, "end"),
        N(236, 40, "[v]ʙ = S [v]ʙ′", 8, "end"), N(236, 52, "S = new arrows as columns", 7, "end"),
        N(236, 84, "same edit T in the new grid:", 7.5, "end"), N(236, 96, "A′ = S⁻¹AS", 8.5, "end"),
        N(236, 126, "goal: pick the grid that", 7, "end"), N(236, 136, "makes A′ simplest", 7, "end"))

def d20405(c):
    return svg(c,
        R(14, 36, 80, 52, "#ffffff", 1, 4), N(54, 32, "grid B", 7.5, "middle"), N(54, 66, "A", 10, "middle"),
        R(146, 36, 80, 52, "#ffffff", 1, 4), N(186, 32, "grid B′", 7.5, "middle"), N(186, 66, "A′ = S⁻¹AS", 8, "middle"),
        L(96, 62, 144, 62, 1, ar=True), L(144, 62, 96, 62, 1), N(120, 56, "same edit", 7, "middle"),
        N(120, 14, "what does not depend on the grid?", 8, "middle"),
        N(120, 108, "tr A′ = tr A,  det A′ = det A,  same char. poly", 7.5, "middle"),
        N(120, 120, "also rank and eigenvalues", 7.5, "middle"),
        N(120, 136, "one invariant differs ⇒ not similar", 7.5, "middle"))

def d20406(c):
    O = (70, 104)
    s = 16
    P = lambda x, y: (O[0] + s * x, O[1] - s * y)
    return svg(c,
        L(14, 104, 160, 104, .6), L(70, 140, 70, 10, .6), pin(*O, None),
        vec(O, P(1, 1), "b₁ = (1,1)", -2, -6, "end", 7.5), vec(O, P(1, -1), "b₂ = (1,−1)", 4, 8, "start", 7.5),
        dash(*P(2, 2), *P(3, 1)), dash(*P(1, -1), *P(3, 1)),
        vec(O, P(2, 2), "2b₁", -4, -2, "end", 7.5), vec(O, P(3, 1), "v = (3,1)", 4, -2, "start", 7.5),
        N(236, 24, "a + b = 3, a − b = 1", 7.5, "end"), N(236, 36, "⇒ a = 2, b = 1", 7.5, "end"),
        N(236, 116, "[v]ʙ = S⁻¹v = (2, 1)", 8, "end"), N(236, 128, "v = 2b₁ + 1b₂", 7.5, "end"))

CARDS = {
20401: dict(d=d20401, stmtKind="THEOREM",
  statement=r"<b>Invertibility (Axler 3.53, 3.56, 3.59).</b> $T\in\mathcal L(V,W)$ is invertible if there is $S\in\mathcal L(W,V)$ with $ST=I_V$ and $TS=I_W$; this $S$ is unique and written $T^{-1}$. $T$ is invertible if and only if it is injective and surjective. If $S,T$ are invertible then $(ST)^{-1}=T^{-1}S^{-1}$.",
  hint="When can an edit be undone, and in which order do you undo two edits?",
  breakdown=[r"<strong>$T$ invertible</strong> = there is an undo edit $T^{-1}$ that brings every arrow back.",
             r"<strong>$\iff$ bijective</strong> = nothing is squashed (one-to-one) and every picture is reachable (onto). The undo is automatically linear.",
             r"<strong>$(ST)^{-1}=T^{-1}S^{-1}$</strong> = undo the last edit first, like taking off socks after shoes."],
  conn=r"<strong>Ctrl-Z on your phone.</strong> Rotate then zoom: to get the original back you un-zoom first, then un-rotate. A flatten filter has no undo, because squashed arrows are gone.",
  cap="T edits the photo and T⁻¹ restores it; this needs T to be one-to-one and onto. Two edits are undone in reverse order: (ST)⁻¹ = T⁻¹S⁻¹."),
20402: dict(d=d20402, stmtKind="THEOREM",
  statement=r"<b>Dimension shows whether spaces are isomorphic (Axler 3.70, 3.71).</b> An isomorphism is an invertible linear map. Two finite-dimensional vector spaces over $\mathbb F$ are isomorphic if and only if they have the same dimension. In particular, if $\dim V=n$ then $V\cong\mathbb F^n$ via $v\mapsto[v]_B$ for any basis $B$.",
  hint="Why is every 3-dimensional space secretly just columns of 3 numbers?",
  breakdown=[r"<strong>$V\cong W$</strong> = there is an undoable edit between them, so they behave identically as vector spaces.",
             r"<strong>$\iff\dim V=\dim W$</strong> = dimension is the only thing that matters; send a basis of one to a basis of the other.",
             r"<strong>$V\cong\mathbb F^n$</strong> = choosing a basis turns every vector into its address column, so every question becomes a matrix question."],
  conn=r"<strong>Same photo, different file format.</strong> A quadratic $a+bx+cx^2$ and the column $(a,b,c)$ carry exactly the same information, so you can edit either and convert back without loss.",
  cap="𝒫₂ and 𝔽³ both have dim 3, so v ↦ [v]ʙ is an isomorphism: V ≅ W ⇔ dim V = dim W."),
20403: dict(d=d20403, stmtKind="THEOREM",
  statement=r"<b>Injectivity is equivalent to surjectivity in finite dimensions (Axler 3.65).</b> Suppose $V$ is finite-dimensional and $T\in\mathcal L(V)$. Then the following are equivalent: $T$ is invertible; $T$ is injective; $T$ is surjective. Moreover, for square matrices (or operators), $ST=I$ implies $TS=I$.",
  hint="For an edit from the photo to itself, why is one check enough to know it can be undone?",
  breakdown=[r"<strong>$\operatorname{null}T=\{0\}$</strong> = nothing is squashed to the pin.",
             r"<strong>$\iff\operatorname{range}T=V$</strong> = by rank–nullity with $\dim W=\dim V$, no lost directions means every direction survives, so the range is everything.",
             r"<strong>$\iff T^{-1}$ exists</strong> = so to prove $A$ invertible, just show $Ax=0\Rightarrow x=0$. A one-sided inverse is two-sided."],
  conn=r"<strong>Same-size canvas.</strong> If an edit of a photo onto a same-size photo never squashes anything, it must fill the whole frame, and it can be undone.",
  cap="For T: V → V in finite dimensions, null T = {0} ⇔ range T = V ⇔ T⁻¹ exists, by rank–nullity."),
20404: dict(d=d20404, stmtKind="THEOREM",
  statement=r"<b>Change of basis (Axler 3.84).</b> Let $T\in\mathcal L(V)$, and $B$, $B'$ bases of $V$. Let $S=\mathcal M(I,B',B)$, whose columns are the vectors of $B'$ written in $B$. Then $[v]_B=S[v]_{B'}$ and $\mathcal M(T,B')=S^{-1}\mathcal M(T,B)S$. Matrices related by $A'=S^{-1}AS$ are called similar.",
  hint="If you redraw the grid on the photo, what happens to the edit's matrix?",
  breakdown=[r"<strong>$[v]_B=S[v]_{B'}$</strong> = $S$ translates new-grid addresses into old-grid addresses; its columns are the new arrows in old coordinates.",
             r"<strong>$A'=S^{-1}AS$</strong> = translate to the old grid ($S$), edit there ($A$), translate back ($S^{-1}$).",
             r"<strong>Goal of the course:</strong> choose the grid that makes $A'$ simplest: diagonal, Jordan, or diagonal in an orthonormal grid."],
  conn=r"<strong>Same edit, new grid.</strong> The photo and the edit do not change when you draw a slanted grid on top; only the numbers describing them change. A clever grid can turn a messy matrix into a diagonal one.",
  cap="A new grid b′₁, b′₂ gives new addresses [v]ʙ = S[v]ʙ′, and the same edit T has the matrix A′ = S⁻¹AS in the new grid."),
20405: dict(d=d20405, stmtKind="PROPOSITION",
  statement=r"<b>Similarity invariants.</b> If $A'=S^{-1}AS$ with $S$ invertible, then $\operatorname{tr}A'=\operatorname{tr}A$, $\det A'=\det A$, $\operatorname{rank}A'=\operatorname{rank}A$, and $A,A'$ have the same characteristic polynomial (hence the same eigenvalues with multiplicities) and the same minimal polynomial.",
  hint="Which numbers about an edit stay the same whatever grid you use?",
  breakdown=[r"<strong>$\operatorname{tr}A'=\operatorname{tr}A$</strong> = $\operatorname{tr}(S^{-1}AS)=\operatorname{tr}(ASS^{-1})$: the sum of the eigenvalues does not care about the grid.",
             r"<strong>$\det A'=\det A$</strong> = $\det S^{-1}\det A\det S=\det A$: the area scale factor is the same.",
             r"<strong>$p_{A'}=p_A$</strong> = $\det(\lambda I-S^{-1}AS)=\det(S^{-1}(\lambda I-A)S)$: same eigenvalues. One mismatch proves two matrices are not similar."],
  conn=r"<strong>Properties of the edit, not the grid.</strong> How much an edit scales area, and which arrows it only stretches, are facts about the edit itself. Redrawing the grid cannot change them.",
  cap="The same edit has matrix A in grid B and A′ = S⁻¹AS in grid B′; trace, determinant and characteristic polynomial p are the same in both."),
20406: dict(d=d20406, stmtKind="WORKED EXAMPLE",
  statement=r"<b>Example.</b> In $\mathbb R^2$ take $B=\{(1,1),(1,-1)\}$, so $S=\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ and $S^{-1}=\tfrac12\begin{pmatrix}1&1\\1&-1\end{pmatrix}$. For $v=(3,1)$: $[v]_B=S^{-1}v=(2,1)$, i.e. $v=2(1,1)+1(1,-1)$.",
  hint="Where is the point (3, 1) in the diagonal grid made of (1, 1) and (1, −1)?",
  breakdown=[r"<strong>$S$ = the new arrows as columns</strong>: $(1,1)$ and $(1,-1)$ written in ordinary coordinates.",
             r"<strong>$S^{-1}v$</strong> = convert the ordinary address $(3,1)$ into the new grid: solve $a+b=3,\ a-b=1$.",
             r"<strong>$(2,1)$</strong> = two steps along $(1,1)$ and one along $(1,-1)$ land exactly on $v$."],
  conn=r"<strong>Reading a slanted grid.</strong> Tilt the grid by 45° on your photo. The point that was '3 right, 1 up' is now '2 along the first diagonal, 1 along the second'.",
  cap="v = (3,1) = 2b₁ + 1b₂ with b₁ = (1,1), b₂ = (1,−1), so [v]ʙ = S⁻¹v = (2, 1)."),
}

STORY = {
 20401: dict(s="STORY 4 · STEP 1 · UNDO", b="An edit that loses nothing and reaches everything can be <b>undone</b>; the undo is linear too.",
   f=[["20304", "one-to-one and onto"]], n=[["20402", "spaces that are secretly the same"], ["20403", "square edits: one check suffices"]]),
 20402: dict(s="STORY 4 · STEP 2 · SAME SPACE, NEW NAME", b="An undoable edit between two spaces means they are the same space in disguise; only the <b>dimension</b> matters.",
   f=[["20401", "invertible maps"], ["20202", "coordinates"]], n=[["20404", "the coordinate map in action"]]),
 20403: dict(s="STORY 4 · STEP 3 · ONE CHECK", b="For an edit of a space to itself, <b>one-to-one, onto and invertible are the same thing</b>.",
   f=[["20303", "rank–nullity"], ["20401", "invertible"]], n=[["20601", "λ is an eigenvalue ⇔ T − λI is not invertible"]]),
 20404: dict(s="STORY 4 · STEP 4 · REDRAW THE GRID", b="Changing the grid changes the matrix to $S^{-1}AS$ but not the edit. The rest of the course looks for the <b>grid that makes the matrix simple</b>.",
   f=[["20305", "matrix of a map"], ["20402", "coordinates"]], n=[["20405", "what stays the same"], ["20606", "diagonalize: the best grid"]]),
 20405: dict(s="STORY 4 · STEP 5 · INVARIANTS", b="Trace, determinant, rank and eigenvalues belong to the edit itself, so <b>similar matrices share them</b>.",
   f=[["20404", "similarity"]], n=[["20406", "practise a change of grid"], ["20501", "the edit's polynomial"]]),
 20406: dict(s="STORY 4 · STEP 6 · WITH NUMBERS", b="A worked change of basis: read the point $(3,1)$ in a 45° grid.",
   f=[["20404", "change of basis"]], n=[["20501", "next: polynomials of an edit"]]),
}

FIX = {cid: {"stmtKind": v["stmtKind"], "statement": v["statement"], "hint": v["hint"], "breakdown": v["breakdown"],
             "personalConnection": v["conn"], "drawingSvg": v["d"](cid), "drawingCaption": v["cap"],
             "textbookImg": None, "textbookRef": None} for cid, v in CARDS.items()}
