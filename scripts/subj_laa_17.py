"""LAA topic 17 (trace, determinant, volume). Photo picture: the determinant is how much the
edit scales the area of a sticker (negative if it mirrors the photo)."""
from laa_lib import *

SUBJECT = "LAA"

def d21701(c):
    return svg(c,
        N(120, 12, "tr A = Σ Aᵢᵢ = Σ λⱼ", 9, "middle"),
        R(30, 28, 72, 60, "#ffffff", 1, 3),
        *[R(32 + 23 * i, 30 + 19 * i, 22, 18, "#d9dee7", 0, 0) for i in range(3)],
        N(43, 43, "A₁₁", 7, "middle"), N(66, 62, "A₂₂", 7, "middle"), N(89, 81, "A₃₃", 7, "middle"),
        N(236, 40, "tr(AB) = tr(BA)", 7.5, "end"), N(236, 54, "tr(S⁻¹AS) = tr A", 7.5, "end"),
        N(236, 68, "tr(A*A) = ‖A‖F²", 7.5, "end"),
        N(120, 112, "the diagonal sum equals the sum of the stretch factors", 7.2, "middle"),
        N(120, 128, "whatever grid you use", 7, "middle"))

def d21702(c):
    return svg(c,
        N(120, 12, "det A = Π λⱼ", 9, "middle"),
        R(20, 34, 28, 28, "#ffffff", 1, 0), N(34, 76, "area 1", 7, "middle"),
        L(54, 48, 70, 48, 1, ar=True), N(62, 42, "B", 7.5, "middle"),
        PG("76,62 112,62 122,34 86,34", "#f1f5f9", 1), N(100, 76, "× det B", 7, "middle"),
        L(128, 48, 144, 48, 1, ar=True), N(136, 42, "A", 7.5, "middle"),
        PG("150,64 206,56 222,26 166,34", "#d9dee7", 1), N(188, 76, "× det A det B", 7, "middle"),
        N(120, 100, "det(AB) = det A · det B", 8, "middle"),
        N(120, 116, "det(cA) = cⁿ det A  (each of n axes scales by c)", 7.2, "middle"),
        N(120, 132, "det(A + B) ≠ det A + det B in general", 7.2, "middle"))

def d21703(c):
    return svg(c,
        N(120, 12, "vol(AΩ) = |det A| · vol(Ω)", 8.5, "middle"),
        R(16, 52, 40, 40, "#ffffff", 1, 0), N(36, 104, "unit square", 7, "middle"),
        L(62, 72, 78, 72, 1, ar=True),
        PG("84,92 140,84 158,44 102,52", "#f1f5f9", 1), N(122, 104, "area |det A|", 7, "middle"),
        N(124, 72, "columns of A", 6.8, "middle"),
        L(176, 92, 230, 70, 1.1), N(204, 104, "det A = 0:", 7, "middle"), N(204, 114, "flattened", 7, "middle"),
        N(120, 134, "|det A| = Π σⱼ;  det < 0 ⇒ the photo is mirrored", 7.2, "middle"))

def d21704(c):
    return svg(c,
        N(120, 12, "pᴀ(λ) = λⁿ − (tr A)λⁿ⁻¹ + e₂λⁿ⁻² − … + (−1)ⁿ det A", 7, "middle"),
        R(14, 30, 212, 22, "#f1f5f9", 1, 3), N(120, 45, "e₁ = tr A = Σ λⱼ  (sum of 1×1 diagonal minors)", 7.2, "middle"),
        R(14, 58, 212, 22, "#ffffff", 1, 3), N(120, 73, "e₂ = Σ λᵢλⱼ (sum of 2×2 principal minors)", 7.2, "middle"),
        R(14, 86, 212, 22, "#f1f5f9", 1, 3), N(120, 101, "eₙ = det A = Π λⱼ", 7.2, "middle"),
        N(120, 130, "2×2:  p(λ) = λ² − (tr A)λ + det A", 8, "middle"))

def d21705(c):
    O = (70, 100)
    return svg(c,
        R(70, 76, 24, 24, "none", .8, 0, "3 2"), pin(*O, None),
        PG("70,100 118,76 130,28 82,52", "#f1f5f9", 1),
        vec(O, (118, 76), "A e₁ = (2,1)", 4, 8, "start", 7), vec(O, (82, 52), "A e₂ = (1,3)", -4, -2, "end", 7),
        N(236, 20, "A = [2 1; 1 3]", 8, "end"), N(236, 34, "tr 5, det 5", 7.5, "end"), N(236, 48, "λ² − 5λ + 5 = 0", 7.5, "end"),
        N(236, 62, "λ = (5 ± √5)/2", 7.5, "end"), N(236, 74, "≈ 3.62, 1.38", 7, "end"),
        N(236, 120, "sum 5 = tr ✓, product 5 = det ✓", 7, "end"), N(236, 132, "area scale 5", 7, "end"))

CARDS = {
21701: dict(d=d21701, stmtKind="PROPOSITION",
  statement=r"<b>Trace (Axler 8.47–8.52).</b> For $A\in\mathbb F^{n\times n}$, $\operatorname{tr}A=\sum_iA_{ii}$. Then $\operatorname{tr}(AB)=\operatorname{tr}(BA)$, so $\operatorname{tr}(S^{-1}AS)=\operatorname{tr}A$ and the trace of an operator is well defined; over $\mathbb C$ it equals the sum of the eigenvalues with multiplicity. Also $\operatorname{tr}(A^*A)=\|A\|_F^2$.",
  hint="Why does the sum of the diagonal not depend on the grid?",
  breakdown=[r"<strong>$\sum_iA_{ii}=\sum_j\lambda_j$</strong> = the diagonal sum equals the sum of the stretch factors.",
             r"<strong>$\operatorname{tr}(AB)=\operatorname{tr}(BA)$</strong> = the key identity; it gives $\operatorname{tr}(S^{-1}AS)=\operatorname{tr}(ASS^{-1})$, grid independence.",
             r"<strong>$\operatorname{tr}(A^*A)=\|A\|_F^2$</strong> = the sum of the squares of all entries."],
  conn=r"<strong>Total stretch.</strong> Add up the stretch factors of an edit and you get the diagonal sum in any grid. For a small edit $I+\varepsilon A$, the trace is how fast the area grows: $\det(I+\varepsilon A)\approx1+\varepsilon\operatorname{tr}A$.",
  cap="The trace adds the diagonal entries A₁₁ + A₂₂ + A₃₃ = Σλⱼ, and tr(AB) = tr(BA) makes it independent of the grid."),
21702: dict(d=d21702, stmtKind="PROPOSITION",
  statement=r"<b>Determinant (Axler 9.49, 9.42, 9.62).</b> For $A\in\mathbb F^{n\times n}$: $\det(AB)=\det A\det B$, $\det A^\top=\det A$, $\det(cA)=c^n\det A$, swapping two rows changes the sign, and $A$ is invertible iff $\det A\ne0$. Over $\mathbb C$, $\det A=\prod\lambda_j$ with multiplicity. In general $\det(A+B)\ne\det A+\det B$.",
  hint="Two edits in a row: how do their area scales combine?",
  breakdown=[r"<strong>$\det A=\prod\lambda_j$</strong> = multiply the stretch factors; zero iff some direction is squashed.",
             r"<strong>$\det(AB)=\det A\det B$</strong> = area scales multiply when you stack edits.",
             r"<strong>$\det(cA)=c^n\det A$</strong> = zooming by $c$ scales each of the $n$ axes, not just one."],
  conn=r"<strong>Area scale of an edit.</strong> Zoom by 2 in a photo and the area grows by 4, not 2. Do two edits and the area scales multiply.",
  cap="Edit B scales the unit square's area by det B, then A by det A: det(AB) = det A · det B; zooming by c gives cⁿ."),
21703: dict(d=d21703, stmtKind="THEOREM",
  statement=r"<b>Determinant as volume (Axler 9.60).</b> For $A\in\mathbb R^{n\times n}$ and a region $\Omega\subseteq\mathbb R^n$, $\operatorname{vol}(A\Omega)=|\det A|\operatorname{vol}(\Omega)$. The image of the unit cube is the parallelepiped spanned by the columns of $A$, of volume $|\det A|=\prod_j\sigma_j$. $\det A\lt0$ means orientation is reversed; $\det A=0$ means space is flattened.",
  hint="How big is the image of a unit square after the edit?",
  breakdown=[r"<strong>$\operatorname{vol}(A\Omega)=|\det A|\operatorname{vol}(\Omega)$</strong> = every region's area is multiplied by the same number.",
             r"<strong>$|\det A|=\prod\sigma_j$</strong> = the circle-to-ellipse area ratio from the SVD (rotations do not change area).",
             r"<strong>sign</strong> = negative if the edit mirrors the photo; zero if it flattens it onto a line."],
  conn=r"<strong>The sticker's area.</strong> Put a 1 cm² sticker on the photo and edit: its new area is $|\det A|$ cm². If the sticker comes out mirror-image, $\det A$ is negative.",
  cap="The unit square becomes the parallelogram spanned by the columns of A, with area |det A| = Πσⱼ; det A = 0 flattens it onto a line."),
21704: dict(d=d21704, stmtKind="PROPOSITION",
  statement=r"<b>Coefficients of the characteristic polynomial.</b> $p_A(\lambda)=\det(\lambda I-A)=\lambda^n-e_1\lambda^{n-1}+e_2\lambda^{n-2}-\dots+(-1)^ne_n$, where $e_k$ is the sum of the $k\times k$ principal minors of $A$, equal to the $k$-th elementary symmetric polynomial of the eigenvalues. In particular $e_1=\operatorname{tr}A$, $e_n=\det A$; for $2\times2$, $p(\lambda)=\lambda^2-(\operatorname{tr}A)\lambda+\det A$.",
  hint="Which coefficients of the characteristic polynomial are the trace and the determinant?",
  breakdown=[r"<strong>$e_1=\operatorname{tr}A$</strong> = the $\lambda^{n-1}$ coefficient: sum of the eigenvalues.",
             r"<strong>$e_2=\sum_{i\lt j}\lambda_i\lambda_j$</strong> = sum of the $2\times2$ principal minors.",
             r"<strong>$e_n=\det A$</strong> = the constant term (with sign $(-1)^n$): product of the eigenvalues."],
  conn=r"<strong>Two numbers for a 2×2 edit.</strong> Total stretch (trace) and area scale (determinant) are all you need to write down its characteristic polynomial.",
  cap="pᴀ(λ) = λⁿ − (tr A)λⁿ⁻¹ + e₂λⁿ⁻² − … + (−1)ⁿ det A: e₁ = trace, eₙ = determinant, e₂ = 2×2 minors."),
21705: dict(d=d21705, stmtKind="WORKED EXAMPLE",
  statement=r"<b>Example.</b> $A=\begin{pmatrix}2&1\\1&3\end{pmatrix}$: $\operatorname{tr}A=5$, $\det A=5$, so $p(\lambda)=\lambda^2-5\lambda+5$ and $\lambda=\tfrac{5\pm\sqrt5}2\approx3.62,1.38$. Check: $\lambda_1+\lambda_2=5$, $\lambda_1\lambda_2=\tfrac{25-5}4=5$. Areas are multiplied by $5$.",
  hint="Read the eigenvalues of this edit from two numbers.",
  breakdown=[r"<strong>$\operatorname{tr}A=5,\ \det A=5$</strong> = diagonal sum and area scale.",
             r"<strong>$\lambda=\frac{5\pm\sqrt5}2$</strong> = roots of $\lambda^2-5\lambda+5$.",
             r"<strong>checks</strong> = the roots add to the trace and multiply to the determinant."],
  conn=r"<strong>A sticker five times bigger.</strong> This edit turns the unit square into a parallelogram of area 5; its two stretch factors are about 3.6 and 1.4.",
  cap="The unit square (dashed) becomes the parallelogram spanned by Ae₁ = (2,1), Ae₂ = (1,3) with area det A = 5; λ = (5 ± √5)/2."),
}

STORY = {
 21701: dict(s="STORY 17 · STEP 1 · TOTAL STRETCH", b="Two numbers summarize an edit regardless of the grid. The first: the <b>trace</b>, the sum of the stretch factors.",
   f=[["20405", "similarity invariants"]], n=[["21702", "the determinant"], ["21704", "both in the polynomial"]]),
 21702: dict(s="STORY 17 · STEP 2 · PRODUCT OF STRETCHES", b="The second: the <b>determinant</b>, the product of the stretch factors; it multiplies when edits are stacked.",
   f=[["21701", "trace"], ["20602", "characteristic polynomial"]], n=[["21703", "it is a volume"]]),
 21703: dict(s="STORY 17 · STEP 3 · AREA OF THE STICKER", b="$|\\det A|$ is the <b>area (volume) scale factor</b>; its sign says whether the photo was mirrored.",
   f=[["21702", "determinant"], ["21505", "|det| = Πσ"]], n=[["21704", "back to the polynomial"]]),
 21704: dict(s="STORY 17 · STEP 4 · THE COEFFICIENTS", b="Trace and determinant are the first and last coefficients of the <b>characteristic polynomial</b>.",
   f=[["21701", "trace"], ["21702", "determinant"]], n=[["21705", "an example"]]),
 21705: dict(s="STORY 17 · STEP 5 · WITH NUMBERS", b="Eigenvalues of a 2×2 edit from its trace and determinant.",
   f=[["21704", "p(λ) = λ² − trλ + det"]], n=[["21801", "last: edits that move probability"]]),
}

FIX = {cid: {"stmtKind": v["stmtKind"], "statement": v["statement"], "hint": v["hint"], "breakdown": v["breakdown"],
             "personalConnection": v["conn"], "drawingSvg": v["d"](cid), "drawingCaption": v["cap"],
             "textbookImg": None, "textbookRef": None} for cid, v in CARDS.items()}
