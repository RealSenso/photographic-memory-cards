"""LAA topic 15 (polar decomposition, SVD). Photo picture: every edit is rotate → stretch along
perpendicular axes → rotate; a round sticker always becomes an ellipse."""
from laa_lib import *
import math

SUBJECT = "LAA"

def ell(cx, cy, a, b, rot, fill="#f1f5f9"):
    return E(cx, cy, a, b, rot, fill, 1)

def d21501(c):
    return svg(c,
        N(120, 12, "T = S |T|:  stretch first, then rotate", 8, "middle"),
        circ(36, 76, 22, "#ffffff", 1), pin(36, 76, None), N(36, 112, "v", 7.5, "middle"),
        L(62, 76, 78, 76, 1, ar=True), N(70, 70, "|T|", 7.5, "middle"),
        ell(118, 76, 34, 14, 0), pin(118, 76, None), N(118, 112, "|T| = √(T*T) ⪰ 0", 7, "middle"),
        L(156, 76, 172, 76, 1, ar=True), N(164, 70, "S", 7.5, "middle"),
        ell(204, 76, 34, 14, -35), pin(204, 76, None), N(204, 112, "S isometry", 7, "middle"),
        N(120, 136, "‖Tv‖ = ‖ |T|v ‖: the rotation S changes no length", 7, "middle"))

def d21502(c):
    return svg(c,
        N(120, 12, "A = UΣV*: rotate, stretch the axes by σⱼ, rotate", 7.5, "middle"),
        circ(30, 78, 20, "#ffffff", 1), vec((30, 78), (44, 64), "v₁", 2, -2, "start", 7), vec((30, 78), (16, 64), "v₂", -2, -2, "end", 7),
        L(54, 78, 66, 78, 1, ar=True), N(60, 72, "V*", 7, "middle"),
        circ(92, 78, 20, "#ffffff", 1), vec((92, 78), (112, 78), None), vec((92, 78), (92, 58), None),
        L(116, 78, 128, 78, 1, ar=True), N(122, 72, "Σ", 7.5, "middle"),
        ell(160, 78, 30, 12, 0), vec((160, 78), (190, 78), "σ₁", 0, 10, "middle", 7), vec((160, 78), (160, 66), "σ₂", -3, 0, "end", 7),
        L(194, 78, 204, 78, 1, ar=True), N(199, 72, "U", 7, "middle"),
        ell(222, 78, 14, 9, -40, "#d9dee7"),
        N(120, 120, "A = Σ σⱼ uⱼvⱼ*,  σⱼ = √λⱼ(A*A) ≥ 0", 7.5, "middle"),
        N(120, 134, "the unit circle always becomes an ellipse", 7, "middle"))

def d21503(c):
    return svg(c,
        N(120, 12, "recipe for the SVD", 8, "middle"),
        *[R(14, 26 + 26 * i, 212, 20, "#f1f5f9" if i % 2 == 0 else "#ffffff", 1, 3) + N(20, 40 + 26 * i, t, 7.5, "start") for i, t in enumerate([
            "1. diagonalize A*A: A*A vⱼ = σⱼ² vⱼ (positive!)",
            "2. σⱼ = √(eigenvalue) ≥ 0",
            "3. uⱼ = Avⱼ / σⱼ  (orthonormal for σⱼ > 0)",
            "4. A = Σ σⱼ uⱼ vⱼ*"])],
        N(120, 136, "⟨uᵢ, uⱼ⟩ = ⟨A*Avᵢ, vⱼ⟩ / σᵢσⱼ = δᵢⱼ", 7.5, "middle"))

def d21504(c):
    bars = [9, 6, 3, 1.4, .8, .4]
    out = [N(120, 12, "keep the k biggest stretches", 8, "middle"), L(20, 118, 230, 118, .8)]
    for i, h in enumerate(bars):
        x = 30 + 32 * i
        out += [R(x, 118 - 9 * h, 18, 9 * h, "#d9dee7" if i < 2 else "#ffffff", 1, 0, None if i < 2 else "3 2"), N(x + 9, 130, f"σ{'₁₂₃₄₅₆'[i]}", 7.5, "middle")]
    out += [N(236, 40, "Aₖ = Σⱼ≤ₖ σⱼuⱼvⱼ*", 7.5, "end"), N(236, 56, "‖A − Aₖ‖₂ = σₖ₊₁", 7.5, "end"), N(236, 70, "‖A − Aₖ‖F = √Σⱼ>ₖ σⱼ²", 7.5, "end"),
            N(120, 142, "k = 2: shaded kept, dashed dropped", 7, "middle")]
    return svg(c, *out)

def d21505(c):
    return svg(c,
        ell(70, 76, 50, 16, -20), circ(70, 76, 16, "none", .8, "3 2"), pin(70, 76, None),
        vec((70, 76), (117, 59), "σ₁", 0, -6, "middle", 7.5), vec((70, 76), (75, 91), "σₙ", 4, 6, "start", 7.5),
        N(236, 22, "‖A‖₂ = σ₁ (longest axis)", 7.5, "end"), N(236, 36, "‖A‖F² = Σ σⱼ²", 7.5, "end"),
        N(236, 50, "|det A| = Π σⱼ (area scale)", 7.5, "end"), N(236, 64, "rank = # of σⱼ > 0", 7.5, "end"),
        N(236, 92, "κ₂(A) = σ₁/σₙ", 8.5, "end"), N(236, 104, "how flat the ellipse is", 7, "end"),
        N(14, 134, "big κ: errors along the short axis blow up", 7, "start"))

def d21506(c):
    return svg(c,
        N(120, 12, "A = [3 0; 4 5]", 8.5, "middle"),
        N(14, 32, "AᵀA = [25 20; 20 25]: eigenvalues 45, 5", 7.5, "start"),
        N(14, 46, "σ₁ = √45 = 3√5 ≈ 6.71,  σ₂ = √5 ≈ 2.24", 7.5, "start"),
        N(14, 60, "v₁ = (1,1)/√2,  v₂ = (1,−1)/√2", 7.5, "start"),
        ell(64, 104, 36, 12, -30), circ(64, 104, 12, "none", .8, "3 2"), pin(64, 104, None),
        N(236, 92, "σ₁σ₂ = 15 = |det A| ✓", 7.5, "end"), N(236, 106, "σ₁² + σ₂² = 50 = ‖A‖F² ✓", 7.5, "end"),
        N(236, 120, "κ₂ = σ₁/σ₂ = 3", 7.5, "end"))

CARDS = {
21501: dict(d=d21501, stmtKind="THEOREM",
  statement=r"<b>Polar decomposition (Axler 7.45).</b> Suppose $T\in\mathcal L(V)$. Then there exists an isometry $S\in\mathcal L(V)$ such that $T=S\sqrt{T^*T}$. Here $|T|=\sqrt{T^*T}$ is positive and $\|Tv\|=\||T|v\|$ for every $v$.",
  hint="How does every edit split into a pure stretch followed by a rotation?",
  breakdown=[r"<strong>$|T|=\sqrt{T^*T}\succeq0$</strong> = the stretch part: positive, along perpendicular axes.",
             r"<strong>$S$ isometry</strong> = the rotate/flip part: it changes no length.",
             r"<strong>$T=S|T|$</strong> = since $\|Tv\|=\||T|v\|$, define $S(|T|v)=Tv$; it keeps lengths, so it is an isometry (extended on the rest)."],
  conn=r"<strong>Stretch, then rotate.</strong> Any edit you make with two fingers is the same as first pulling the photo along two perpendicular axes, then rotating it. Like writing a complex number as $re^{i\theta}$.",
  cap="Every T = S|T|: the positive part |T| = √(T*T) stretches a circle into an ellipse, then the isometry S rotates it."),
21502: dict(d=d21502, stmtKind="THEOREM",
  statement=r"<b>Singular value decomposition (Axler 7.70, 7.93).</b> Every $A\in\mathbb F^{m\times n}$ can be written $A=U\Sigma V^*$ with $U\in\mathbb F^{m\times m}$, $V\in\mathbb F^{n\times n}$ unitary and $\Sigma$ diagonal (rectangular) with entries $\sigma_1\ge\sigma_2\ge\dots\ge0$, the singular values, $\sigma_j=\sqrt{\lambda_j(A^*A)}$. Equivalently $A=\sum_{j=1}^r\sigma_ju_jv_j^*$ with $r=\operatorname{rank}A$.",
  hint="What does any edit do to a round sticker?",
  breakdown=[r"<strong>$V^*$</strong> = rotate the input so the special axes $v_j$ line up with the grid.",
             r"<strong>$\Sigma$</strong> = stretch each axis by $\sigma_j\ge0$, where $\sigma_j^2$ are the eigenvalues of $A^*A$.",
             r"<strong>$U$</strong> = rotate into the output directions $u_j$. In sum, $A=\sum\sigma_ju_jv_j^*$: one rank-1 piece per axis."],
  conn=r"<strong>Rotate, stretch, rotate.</strong> Every photo edit, however strange, turns a round sticker into an ellipse. The ellipse's axes are the $\sigma_j$, and the SVD tells you which way the sticker was turned before and after.",
  cap="V* rotates v₁, v₂ to the grid, Σ stretches the axes by σ₁, σ₂, U rotates into the output: the circle becomes an ellipse, A = Σσⱼuⱼvⱼ*."),
21503: dict(d=d21503, stmtKind="ALGORITHM",
  statement=r"<b>Computing an SVD.</b> (1) Find an orthonormal eigenbasis $v_1,\dots,v_n$ of the positive operator $A^*A$, $A^*Av_j=\sigma_j^2v_j$ with $\sigma_1\ge\dots\ge0$. (2) For $\sigma_j\gt0$ set $u_j=Av_j/\sigma_j$; these are orthonormal. (3) Extend to an orthonormal basis of $\mathbb F^m$. Then $A=\sum_j\sigma_ju_jv_j^*$.",
  hint="Which positive matrix hides the stretch factors of A?",
  breakdown=[r"<strong>$A^*Av_j=\sigma_j^2v_j$</strong> = $A^*A$ is positive, so the spectral theorem gives perpendicular axes and nonnegative factors.",
             r"<strong>$u_j=Av_j/\sigma_j$</strong> = push each axis through $A$ and rescale to unit length.",
             r"<strong>why orthonormal:</strong> $\langle u_i,u_j\rangle=\langle A^*Av_i,v_j\rangle/(\sigma_i\sigma_j)=\delta_{ij}$."],
  conn=r"<strong>Edit, then partner.</strong> Doing the edit and then its measuring partner is a pure stretch; its axes and factors are exactly what you need. The output directions come from pushing those axes through the edit.",
  cap="Diagonalize A*A to get vⱼ and σⱼ², set uⱼ = Avⱼ/σⱼ (orthonormal), and A = Σσⱼuⱼvⱼ*."),
21504: dict(d=d21504, stmtKind="THEOREM",
  statement=r"<b>Eckart–Young–Mirsky.</b> Let $A=\sum_j\sigma_ju_jv_j^*$ and $A_k=\sum_{j\le k}\sigma_ju_jv_j^*$. Then for every $B$ with $\operatorname{rank}B\le k$: $\|A-B\|_2\ge\sigma_{k+1}=\|A-A_k\|_2$ and $\|A-B\|_F\ge\sqrt{\sum_{j\gt k}\sigma_j^2}=\|A-A_k\|_F$.",
  hint="If you may keep only k pieces of an edit, which do you keep?",
  breakdown=[r"<strong>$A_k=\sum_{j\le k}\sigma_ju_jv_j^*$</strong> = keep the $k$ biggest stretches, drop the rest.",
             r"<strong>$\|A-A_k\|_2=\sigma_{k+1}$</strong> = the error is the biggest stretch you dropped; no rank-$k$ matrix does better.",
             r"<strong>$\|A-A_k\|_F=\sqrt{\sum_{j\gt k}\sigma_j^2}$</strong> = in the Frobenius norm the error is all dropped stretches together."],
  conn=r"<strong>Compressing a photo.</strong> Write a photo as a matrix, keep only its few biggest singular pieces, and you get a blurry but recognizable picture using a fraction of the numbers.",
  cap="Bars are σ₁ ≥ σ₂ ≥ …; keeping k = 2 gives Aₖ with errors ‖A − Aₖ‖₂ = σₖ₊₁ and ‖A − Aₖ‖F = √Σⱼ>ₖσⱼ²."),
21505: dict(d=d21505, stmtKind="PROPOSITION",
  statement=r"<b>Singular values and matrix quantities.</b> For $A$ with singular values $\sigma_1\ge\dots\ge\sigma_n$: $\|A\|_2=\sigma_1$, $\|A\|_F^2=\sum\sigma_j^2=\operatorname{tr}A^*A$, $\operatorname{rank}A=\#\{\sigma_j\gt0\}$; for square $A$, $|\det A|=\prod\sigma_j$ and, if invertible, $\kappa_2(A)=\sigma_1/\sigma_n$.",
  hint="What can you read off the ellipse an edit makes?",
  breakdown=[r"<strong>$\|A\|_2=\sigma_1$</strong> = the longest axis: the most any arrow can be stretched.",
             r"<strong>$|\det A|=\prod\sigma_j$</strong> = the area of the ellipse relative to the circle.",
             r"<strong>$\kappa_2(A)=\sigma_1/\sigma_n$</strong> = how flat the ellipse is: a flat ellipse means small input errors along the short axis are hugely amplified when you undo the edit."],
  conn=r"<strong>Reading the ellipse.</strong> Its longest axis is the norm, its area is the determinant, the number of non-flat axes is the rank, and its flatness is how dangerous the edit is to undo.",
  cap="The ellipse's long axis σ₁ is ‖A‖₂, its area is |det A| = Πσⱼ, its flatness is κ₂ = σ₁/σₙ."),
21506: dict(d=d21506, stmtKind="WORKED EXAMPLE",
  statement=r"<b>Example.</b> $A=\begin{pmatrix}3&0\\4&5\end{pmatrix}$: $A^\top A=\begin{pmatrix}25&20\\20&25\end{pmatrix}$ has eigenvalues $45,5$, so $\sigma_1=3\sqrt5$, $\sigma_2=\sqrt5$, with $v_1=\tfrac1{\sqrt2}(1,1)$, $v_2=\tfrac1{\sqrt2}(1,-1)$. Checks: $\sigma_1\sigma_2=15=|\det A|$ and $\sigma_1^2+\sigma_2^2=50=\|A\|_F^2$.",
  hint="Find the stretch factors of this edit and check them two ways.",
  breakdown=[r"<strong>$A^\top A$ eigenvalues $45,5$</strong> = trace 50, determinant $625-400=225=45\cdot5$.",
             r"<strong>$\sigma_1=3\sqrt5,\ \sigma_2=\sqrt5$</strong> = square roots of those.",
             r"<strong>checks:</strong> product $15=|\det A|$ (area), sum of squares $50=\|A\|_F^2$ (all entries squared: $9+16+25$)."],
  conn=r"<strong>The sticker test.</strong> This edit turns a round sticker into an ellipse about 3 times longer than it is wide, with 15 times the area.",
  cap="AᵀA has eigenvalues 45 and 5, so σ₁ = 3√5, σ₂ = √5; σ₁σ₂ = 15 = |det A| and σ₁² + σ₂² = 50 = ‖A‖F²."),
}

STORY = {
 21501: dict(s="STORY 15 · STEP 1 · STRETCH THEN ROTATE", b="Now <b>any</b> edit, not just normal ones: it is a positive stretch followed by an isometry, $T=S|T|$.",
   f=[["21402", "|T| = √(T*T)"], ["21403", "isometries"]], n=[["21502", "the SVD"]]),
 21502: dict(s="STORY 15 · STEP 2 · CIRCLE TO ELLIPSE", b="The <b>SVD</b>: rotate, stretch the axes by $\\sigma_j$, rotate. Every edit turns circles into ellipses.",
   f=[["21501", "polar decomposition"], ["21302", "spectral theorem for A*A"]], n=[["21503", "compute it"], ["21504", "compress with it"]]),
 21503: dict(s="STORY 15 · STEP 3 · COMPUTE IT", b="Diagonalize $A^*A$, take square roots, push the axes through $A$.",
   f=[["21502", "SVD"]], n=[["21506", "a full example"]]),
 21504: dict(s="STORY 15 · STEP 4 · COMPRESS", b="Keeping the biggest singular pieces gives the <b>best low-rank approximation</b>.",
   f=[["21502", "A = Σσⱼuⱼvⱼ*"]], n=[["21505", "what else σ tells you"]]),
 21505: dict(s="STORY 15 · STEP 5 · READ THE ELLIPSE", b="Norm, rank, determinant and condition number are all <b>read off the singular values</b>.",
   f=[["21504", "truncation"]], n=[["21603", "invert the nonzero σ: pseudoinverse"], ["21703", "|det| as volume"]]),
 21506: dict(s="STORY 15 · STEP 6 · WITH NUMBERS", b="An SVD by hand, checked with the determinant and the Frobenius norm.",
   f=[["21503", "recipe"]], n=[["21601", "next: solving the unsolvable"]]),
}

FIX = {cid: {"stmtKind": v["stmtKind"], "statement": v["statement"], "hint": v["hint"], "breakdown": v["breakdown"],
             "personalConnection": v["conn"], "drawingSvg": v["d"](cid), "drawingCaption": v["cap"],
             "textbookImg": None, "textbookRef": None} for cid, v in CARDS.items()}
