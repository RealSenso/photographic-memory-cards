"""LAA topic 16 (least squares, four subspaces, pseudoinverse). Photo picture: when no edit
input hits the target b exactly, aim for b's shadow on the sheet of reachable outputs."""
from laa_lib import *

SUBJECT = "LAA"

def d21601(c):
    O = (64, 102)
    return svg(c,
        sheet([(14, 128), (150, 128), (196, 70), (60, 70)]), N(20, 122, "col A: every Ax", 7, "start"), pin(*O, None),
        vec(O, (150, 28), "b", 4, -2), vec(O, (150, 100), "Ax̂ = Pb", 4, 10), L(150, 28, 150, 100, 1, "3 2"), N(156, 64, "r = b − Ax̂ ⊥ col A", 7, "start"),
        N(12, 14, "min ‖Ax − b‖² ⇔ A*Ax̂ = A*b", 8, "start"),
        N(12, 28, "P = A(A*A)⁻¹A*", 7.5, "start"))

def d21602(c):
    return svg(c,
        phone(6, 22, 104, 96, "ℝⁿ (inputs)"), phone(130, 22, 104, 96, "ℝᵐ (outputs)"),
        L(16, 104, 100, 40, 1), N(98, 52, "row A (r)", 7, "end"), L(28, 36, 92, 108, .9, "3 2"), N(30, 46, "null A (n − r)", 7, "start"),
        L(140, 104, 224, 40, 1), N(222, 52, "col A (r)", 7, "end"), L(152, 36, 216, 108, .9, "3 2"), N(154, 46, "null Aᵀ (m − r)", 7, "start"),
        L(110, 70, 128, 70, 1, ar=True), N(119, 64, "A", 7.5, "middle"),
        N(120, 132, "ℝⁿ = row A ⊕ null A,   ℝᵐ = col A ⊕ null Aᵀ", 7.2, "middle"))

def d21603(c):
    return svg(c,
        N(120, 12, "A⁺ = VΣ⁺U*: undo every stretch you can", 8, "middle"),
        R(14, 28, 100, 44, "#ffffff", 1, 3), N(64, 44, "Σ = diag(σ₁, σ₂, 0)", 7.5, "middle"), N(64, 60, "stretch, stretch, flatten", 7, "middle"),
        L(118, 50, 124, 50, 1, ar=True),
        R(128, 28, 100, 44, "#f1f5f9", 1, 3), N(178, 44, "Σ⁺ = diag(1/σ₁, 1/σ₂, 0)", 7.2, "middle"), N(178, 60, "invert nonzero, keep 0", 7, "middle"),
        N(120, 96, "AA⁺ = projection onto col A", 7.5, "middle"), N(120, 110, "A⁺A = projection onto row A", 7.5, "middle"),
        N(120, 132, "a flattened direction can't be un-flattened", 7, "middle"))

def d21604(c):
    O = (96, 104)
    return svg(c,
        L(14, 104, 230, 104, .9), N(230, 98, "row A", 7.5, "end"),
        L(44, 136, 176, 38, .9, "3 2"), N(236, 64, "x̂ + null A:", 7, "end"), N(236, 74, "all minimizers", 7, "end"),
        pin(*O, None), dot(140, 104, None, r=2.6), N(140, 116, "x⁺ = A⁺b", 7.5, "middle"),
        vec(O, (140, 104), None), dot(100, 74, None, r=2), N(96, 70, "x̂", 7.5, "end"),
        N(12, 14, "every point on the dashed line gives the same Ax", 7, "start"),
        N(12, 26, "the shortest one lies in row A = (null A)⊥", 7, "start"),
        N(236, 136, "x⁺: the shortest minimizer", 7, "end"))

def d21605(c):
    rows = [("1. AXA = A", "X undoes A on its range"), ("2. XAX = X", "A undoes X on its range"),
            ("3. (AX)* = AX", "AX is an orthogonal projection"), ("4. (XA)* = XA", "XA is an orthogonal projection")]
    out = [N(120, 12, "exactly one X satisfies all four: X = A⁺", 8, "middle")]
    for i, (a, b) in enumerate(rows):
        y = 28 + 24 * i
        out += [R(14, y, 212, 20, "#f1f5f9" if i < 2 else "#ffffff", 1, 3), N(20, y + 14, a, 7.5, "start"), N(222, y + 14, b, 7, "end")]
    out.append(N(120, 136, "check a candidate formula against all four", 7, "middle"))
    return svg(c, *out)

def d21606(c):
    X = lambda x: 40 + 70 * x
    Y = lambda y: 128 - 40 * y
    fit = lambda x: 7 / 6 + x / 2
    return svg(c,
        L(20, 128, 230, 128, .8, ar=True), N(230, 140, "x", 7.5, "end"), L(40, 136, 40, 14, .8, ar=True),
        L(X(-.2), Y(fit(-.2)), X(2.6), Y(fit(2.6)), 1.1), N(X(2.6), Y(fit(2.6)) - 4, "ŷ = 7/6 + x/2", 7.5, "end"),
        *[dot(X(x), Y(y), None, r=2.4) + L(X(x), Y(y), X(x), Y(fit(x)), .8, "2 2") for x, y in [(0, 1), (1, 2), (2, 2)]],
        N(X(0) + 4, Y(1) + 10, "(0,1)", 7, "start"), N(X(1), Y(2) - 6, "(1,2)", 7, "middle"), N(X(2) + 4, Y(2) - 6, "(2,2)", 7, "start"),
        N(236, 70, "AᵀA = [3 3; 3 5], Aᵀb = (5, 6)", 7, "end"), N(236, 82, "x̂ = (7/6, 1/2)", 7.5, "end"), N(236, 94, "Aᵀ(b − Ax̂) = 0", 7.5, "end"))

CARDS = {
21601: dict(d=d21601, stmtKind="THEOREM",
  statement=r"<b>Least squares (Axler 6.58 applied to range $A$).</b> For $A\in\mathbb F^{m\times n}$, $b\in\mathbb F^m$, $\hat x$ minimizes $\|Ax-b\|$ if and only if $A\hat x=P_{\operatorname{col}A}b$, if and only if $A^*A\hat x=A^*b$ (normal equations). If $A$ has independent columns, $\hat x=(A^*A)^{-1}A^*b$ and $P=A(A^*A)^{-1}A^*$.",
  hint="If no input reaches the target b, which output do you aim for?",
  breakdown=[r"<strong>$\min_x\|Ax-b\|^2$</strong> = the outputs $Ax$ form the sheet $\operatorname{col}A$; find the point on it closest to $b$.",
             r"<strong>$A\hat x=Pb$</strong> = that point is $b$'s shadow on the sheet.",
             r"<strong>$A^*A\hat x=A^*b$</strong> = the miss $r=b-A\hat x$ must be perpendicular to every column: $A^*r=0$."],
  conn=r"<strong>Aim for the shadow.</strong> If the edit can only produce pictures on a flat sheet and your target is off it, the best you can do is the target's shadow on the sheet. The miss sticks straight out.",
  cap="b is off the sheet col A; the best Ax̂ is its shadow Pb, and the miss r = b − Ax̂ ⊥ col A gives A*Ax̂ = A*b."),
21602: dict(d=d21602, stmtKind="THEOREM",
  statement=r"<b>Four fundamental subspaces.</b> For $A\in\mathbb R^{m\times n}$ of rank $r$: $\operatorname{row}A=(\operatorname{null}A)^\perp$ and $\mathbb R^n=\operatorname{row}A\oplus\operatorname{null}A$ (dimensions $r$, $n-r$); $\operatorname{col}A=(\operatorname{null}A^\top)^\perp$ and $\mathbb R^m=\operatorname{col}A\oplus\operatorname{null}A^\top$ (dimensions $r$, $m-r$). $A$ maps $\operatorname{row}A$ one-to-one onto $\operatorname{col}A$.",
  hint="How do the four subspaces of an edit split the input and output photos?",
  breakdown=[r"<strong>$\mathbb R^n=\operatorname{row}A\oplus\operatorname{null}A$</strong> = every input is a part that matters plus a part that gets squashed; they are perpendicular.",
             r"<strong>$\mathbb R^m=\operatorname{col}A\oplus\operatorname{null}A^\top$</strong> = every output-side arrow is a reachable part plus an unreachable perpendicular part.",
             r"<strong>dimensions $r,\ n-r,\ r,\ m-r$</strong> = rank–nullity on both sides; $A$ is invertible from row space to column space."],
  conn=r"<strong>The edit's full map.</strong> On the input photo, the edit ignores one perpendicular family of directions and cares about the rest; on the output photo, it can reach one sheet and never the perpendicular rest.",
  cap="Inputs: row A ⊥ null A, ℝⁿ = row A ⊕ null A. Outputs: col A ⊥ null Aᵀ, ℝᵐ = col A ⊕ null Aᵀ."),
21603: dict(d=d21603, stmtKind="DEFINITION",
  statement=r"<b>Moore–Penrose pseudoinverse.</b> If $A=U\Sigma V^*$ is an SVD, $A^+=V\Sigma^+U^*$, where $\Sigma^+$ is the $n\times m$ diagonal matrix with entries $1/\sigma_j$ for $\sigma_j\gt0$ and $0$ otherwise. Then $AA^+$ is the orthogonal projection onto $\operatorname{col}A$ and $A^+A$ the orthogonal projection onto $\operatorname{row}A$; if $A$ is invertible, $A^+=A^{-1}$.",
  hint="How do you 'undo' an edit that flattens some directions?",
  breakdown=[r"<strong>$\Sigma^+$</strong> = undo each stretch by $1/\sigma_j$; a flattened axis ($\sigma_j=0$) stays at 0.",
             r"<strong>$A^+=V\Sigma^+U^*$</strong> = rotate back, un-stretch, rotate back.",
             r"<strong>$AA^+=P_{\operatorname{col}A}$, $A^+A=P_{\operatorname{row}A}$</strong> = the best possible undo: it restores everything that was not flattened."],
  conn=r"<strong>Undo as much as you can.</strong> If an edit flattened the photo's depth, no undo can bring it back. The pseudoinverse undoes all the stretches it can and leaves the flattened part at zero.",
  cap="Σ⁺ inverts the nonzero stretches and keeps the zero, so A⁺ = VΣ⁺U*; AA⁺ and A⁺A are the projections onto col A and row A."),
21604: dict(d=d21604, stmtKind="THEOREM",
  statement=r"<b>Minimum-norm least squares.</b> The set of least-squares solutions of $Ax\approx b$ is $\hat x+\operatorname{null}A$. Among them, $x^+=A^+b$ is the unique one of smallest norm, and it is the unique least-squares solution lying in $\operatorname{row}A=(\operatorname{null}A)^\perp$.",
  hint="Many inputs give the same best output. Which one is the shortest?",
  breakdown=[r"<strong>$\hat x+\operatorname{null}A$</strong> = adding a squashed direction changes nothing in the output, so all these are equally good.",
             r"<strong>$x^+\in\operatorname{row}A$</strong> = drop the part along $\operatorname{null}A$; by Pythagoras that makes it shortest.",
             r"<strong>$x^+=A^+b$</strong> = the pseudoinverse picks exactly that one."],
  conn=r"<strong>The laziest edit that works.</strong> If several inputs give the same best picture, choose the one with no wasted motion: nothing in the directions the edit ignores anyway.",
  cap="All least-squares solutions lie on the dashed line x̂ + null A; the shortest, x⁺ = A⁺b, is the one in row A."),
21605: dict(d=d21605, stmtKind="THEOREM",
  statement=r"<b>Penrose conditions.</b> For $A\in\mathbb F^{m\times n}$ there is exactly one $X\in\mathbb F^{n\times m}$ with (1) $AXA=A$, (2) $XAX=X$, (3) $(AX)^*=AX$, (4) $(XA)^*=XA$; it is $X=A^+$.",
  hint="Which four checks pin down the pseudoinverse uniquely?",
  breakdown=[r"<strong>$AXA=A$, $XAX=X$</strong> = $X$ undoes $A$ on what $A$ can reach, and vice versa (a reflexive generalized inverse).",
             r"<strong>$(AX)^*=AX$, $(XA)^*=XA$</strong> = the round trips are orthogonal (self-adjoint) projections.",
             r"<strong>unique</strong> = the four together leave no freedom: the only such $X$ is $A^+$."],
  conn=r"<strong>Four checks for the best undo.</strong> Edit, undo, edit is the same as editing; undo, edit, undo is the same as undoing; and both round trips are clean shadow projections.",
  cap="The four Penrose conditions: AXA = A, XAX = X, and AX, XA self-adjoint projections. Only X = A⁺ passes all four."),
21606: dict(d=d21606, stmtKind="WORKED EXAMPLE",
  statement=r"<b>Example.</b> Fit $y=a+cx$ to $(0,1),(1,2),(2,2)$: $A=\begin{pmatrix}1&0\\1&1\\1&2\end{pmatrix}$, $b=(1,2,2)$, $A^\top A=\begin{pmatrix}3&3\\3&5\end{pmatrix}$, $A^\top b=(5,6)$. Normal equations give $c=\tfrac12$, $a=\tfrac76$, so $\hat y=\tfrac76+\tfrac12x$, and $A^\top(b-A\hat x)=0$.",
  hint="Which line misses three points by the least total squared error?",
  breakdown=[r"<strong>$A^\top A=\begin{pmatrix}3&3\\3&5\end{pmatrix},\ A^\top b=(5,6)$</strong> = the normal equations $3a+3c=5$, $3a+5c=6$.",
             r"<strong>$\hat x=(7/6,1/2)$</strong> = the best intercept and slope.",
             r"<strong>$A^\top(b-A\hat x)=0$</strong> = the misses are perpendicular to both columns: they sum to zero and are balanced in $x$."],
  conn=r"<strong>A straight trend through dots on a photo.</strong> No line passes through all three dots; the least-squares line is the shadow of the data on the sheet of all possible lines.",
  cap="The best line ŷ = 7/6 + x/2 through (0,1), (1,2), (2,2): from AᵀA x̂ = Aᵀb, with the misses (dashed) satisfying Aᵀ(b − Ax̂) = 0."),
}

STORY = {
 21601: dict(s="STORY 16 · STEP 1 · AIM FOR THE SHADOW", b="When $Ax=b$ has no solution, solve the nearest one: project $b$ onto the column space (<b>least squares</b>).",
   f=[["21104", "best approximation"], ["21202", "null T* ⊥ range T"]], n=[["21602", "the four subspaces"], ["21606", "fit a line"]]),
 21602: dict(s="STORY 16 · STEP 2 · THE FULL MAP", b="Row, null, column and left-null spaces split inputs and outputs into <b>perpendicular pairs</b>.",
   f=[["21202", "null and range of T*"], ["20303", "rank–nullity"]], n=[["21603", "undo on the row space"]]),
 21603: dict(s="STORY 16 · STEP 3 · BEST UNDO", b="The <b>pseudoinverse</b> undoes every nonzero stretch and leaves flattened directions at 0.",
   f=[["21502", "SVD"], ["21602", "four subspaces"]], n=[["21604", "the minimum-norm solution"], ["21605", "four conditions"]]),
 21604: dict(s="STORY 16 · STEP 4 · SHORTEST SOLUTION", b="Among all least-squares solutions, $A^+b$ is the <b>shortest</b>: the one in the row space.",
   f=[["21603", "A⁺"], ["21601", "least squares"]], n=[["21605", "characterize A⁺"]]),
 21605: dict(s="STORY 16 · STEP 5 · FOUR CHECKS", b="The <b>Penrose conditions</b> characterize $A^+$ uniquely.",
   f=[["21603", "A⁺"]], n=[["21606", "practice"]]),
 21606: dict(s="STORY 16 · STEP 6 · WITH NUMBERS", b="Fit a straight line to three points with the normal equations.",
   f=[["21601", "normal equations"]], n=[["21701", "next: trace, determinant, volume"]]),
}

FIX = {cid: {"stmtKind": v["stmtKind"], "statement": v["statement"], "hint": v["hint"], "breakdown": v["breakdown"],
             "personalConnection": v["conn"], "drawingSvg": v["d"](cid), "drawingCaption": v["cap"],
             "textbookImg": None, "textbookRef": None} for cid, v in CARDS.items()}
