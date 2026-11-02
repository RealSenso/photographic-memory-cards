"""DIP topic 16 (corners, Harris). Everyday picture: a street camera on a pole (shop window corners as landmarks)."""
from street_lib import *

SUBJECT = "DIP"

def win(x, y, kind):
    out = R(x, y, 56, 44, "#ffffff", 1)
    if kind == "edge": out += R(x + 28, y, 28, 44, "#d9dee7", .6) + L(x + 28, y, x + 28, y + 44, 1)
    if kind == "corner": out += R(x + 28, y + 22, 28, 22, "#d9dee7", .6) + L(x + 28, y + 22, x + 28, y + 44, 1) + L(x + 28, y + 22, x + 56, y + 22, 1)
    return out + R(x + 16, y + 11, 24, 22, "none", 1, 0, "3 2")

def d3151(c):
    return svg(c,
        win(10, 14, "flat"), N(38, 72, "flat: road", 7), N(38, 84, "E ≈ 0 every way", 6.5),
        win(92, 14, "edge"), N(120, 72, "edge: kerb", 7), N(120, 84, "E ≈ 0 along it", 6.5),
        win(174, 14, "corner"), N(202, 72, "corner: window", 7), N(202, 84, "E big every way", 6.5),
        N(120, 106, "E(u, v) = Σ w(x,y) [I(x+u, y+v) − I(x,y)]²", 7.5),
        N(120, 120, "slide the dashed window by (u, v) and see what changes", 7.5), N(120, 134, "only corners can be pinned down", 7.5))

def d3152(c):
    out = []
    for i, (lab, rx, ry) in enumerate((("flat", 4, 4), ("edge", 30, 6), ("corner", 16, 16))):
        cx = 40 + i * 80
        out += [L(cx - 32, 52, cx + 32, 52, .5, "1 3"), L(cx, 24, cx, 80, .5, "1 3"), E(cx, 52, rx, ry, 0 if i != 1 else 0, "none" if i else "#f1f5f9", 1),
                N(cx, 96, lab, 7.5), N(cx, 108, ["λ₁, λ₂ small", "λ₁ big, λ₂ small", "λ₁, λ₂ big"][i], 6.5)]
    out += [N(120, 12, "E(u, v) = constant is an ellipse (axes ∝ 1/√λ)", 7.5),
            N(120, 126, "E(u, v) ≈ [u v] M [u v]ᵀ ,  M = Σ w [[Iₓ², IₓIᵧ], [IₓIᵧ, Iᵧ²]]", 7.5), N(120, 138, "one pixel's M has rank 1: it needs the window", 7)]
    return svg(c, *out)

def d3153(c):
    return svg(c,
        axes(24, 108, 140, 16), N(140, 118, "λ₁", 8, "end"), N(18, 18, "λ₂", 8, "end"),
        R(24, 62, 20, 46, "#ffffff", .6, 0, "2 2"), R(60, 18, 80, 44, "#d9dee7", .8), N(100, 44, "corner: R ≫ 0", 7.5), N(36, 40, "edge", 7, "middle") if False else "",
        N(80, 96, "edge: R < 0", 7), N(34, 98, "flat", 7, "middle"), N(34, 108, "R ≈ 0", 6.5, "middle") if False else "",
        R(150, 20, 80, 72, "#f1f5f9", 1), N(190, 34, "R = det M − k tr²M", 7), N(190, 48, "= λ₁λ₂ − k(λ₁+λ₂)²", 7), N(190, 66, "k ≈ 0.04 – 0.06", 7), N(190, 82, "Shi–Tomasi: min(λ₁, λ₂)", 6.5),
        N(120, 134, "no eigen-decomposition needed", 7.5))

def d3154(c):
    out = []
    labs = [("1", "Iₓ, Iᵧ"), ("2", "Iₓ², IₓIᵧ, Iᵧ²"), ("3", "Gσ ∗ products"), ("4", "R = det − k tr²"), ("5", "peaks")]
    for i, (a, b) in enumerate(labs):
        x = 6 + i * 47
        out += [R(x, 16, 42, 40, "#f1f5f9", 1), N(x + 21, 28, a, 7.5), N(x + 21, 42, b, 5.5)]
        if i < 4: out.append(arrow(x + 42, 36, x + 47, 36, .8))
    out += [N(120, 76, "M(x, y) = Gσ ∗ [[Iₓ², IₓIᵧ], [IₓIᵧ, Iᵧ²]]", 8),
            N(120, 92, "corners = { R > τ } ∩ local maxima (3×3)", 7.5),
            N(120, 108, "Gaussian window: smooth, the same in every direction", 7.5),
            N(120, 124, "smooth the PRODUCTS, not the image first", 7.5)]
    return svg(c, *out)

def d3155(c):
    return svg(c,
        win(8, 12, "corner"), N(36, 68, "corner", 7), arrow(66, 34, 86, 34, 1), N(76, 28, "rotate", 6.5),
        P("M92,12 L148,12 L148,56 L92,56 Z", "#ffffff", 1) if False else R(92, 12, 56, 44, "#ffffff", 1),
        PG("108,50 108,22 138,22", "none", 1) if False else L(105, 48, 120, 22, 1) + L(120, 22, 138, 36, 1), N(120, 68, "same R", 7),
        N(190, 12, "zoom in:", 7), R(158, 18, 70, 44, "#ffffff", 1), R(193, 18, 35, 44, "#d9dee7", .6), L(193, 18, 193, 62, 1), N(193, 74, "a corner looks like an edge", 6.5),
        N(120, 96, "rotation: eigenvalues of M unchanged ⇒ R unchanged", 7.5),
        N(120, 110, "I → I + b : R same     I → aI : R → a⁴R", 7.5),
        N(120, 124, "scale: R changes ⇒ need scale space", 7.5), N(120, 138, "(Harris–Laplace, SIFT)", 7))

def d3156(c):
    def card(x, lab, M, R_, sub):
        return (R(x, 14, 70, 66, "#f1f5f9", 1) + N(x + 35, 26, lab, 7.5) + N(x + 35, 40, M, 7) + N(x + 35, 54, sub, 6.5) + N(x + 35, 72, R_, 8))
    return svg(c,
        card(8, "corner", "M = diag(10, 10)", "R = 80", "det 100, tr 20"),
        card(86, "edge", "M = diag(10, 0)", "R = −5", "det 0, tr 10"),
        card(164, "flat", "M = 0", "R = 0", "det 0, tr 0"),
        N(120, 100, "R = 100 − 0.05·20² = 80", 7.5), N(120, 112, "R = 0 − 0.05·10² = −5", 7.5), N(120, 124, "k = 0.05 : edge R is negative, flat R ≈ 0", 7.5), N(120, 138, "sign and size of R separate the three cases", 7))

CARDS = {
3151: dict(d=d3151, stmtKind="DEFINITION",
  statement=r"<b>Window-shift energy.</b> For a window function $w$ and a shift $(u,v)$, $E(u,v)=\sum_{x,y}w(x,y)\,\big[I(x+u,y+v)-I(x,y)\big]^2$ measures how much the image patch changes when the window moves by $(u,v)$. In a flat region $E\approx0$ for all shifts; at an edge $E$ is large across the edge and $\approx0$ along it (aperture problem); at a corner $E$ is large for every direction of shift.",
  hint="Slide a small window on the street frame: where does it change in every direction?",
  breakdown=[r"<strong>$I(x+u,y+v)-I(x,y)$ = the change at one pixel.</strong> Compare what is under the window now with what is under it after a small slide.",
             r"<strong>$\sum w(x,y)[\cdot]^2$ = add up the change inside the window.</strong> The weight $w$ decides which pixels count; squared so ups and downs both add.",
             r"<strong>Flat, edge, corner = three patterns of $E$.</strong> Road: no change. Kerb: change only across it. Shop-window corner: change whichever way you slide, so the corner can be pinned down."],
  conn=r"<strong>Three places on the street.</strong> On the empty road, nothing changes as the window slides; along the kerb it only changes across; at the shop window's corner it changes whichever way you go. Only the corner is a good landmark.",
  cap="A dashed window on the road (E ≈ 0 in every direction), on the kerb (E ≈ 0 along it) and on the corner of a shop window (E large in every direction)."),
3152: dict(d=d3152, stmtKind="PROPOSITION",
  statement=r"<b>Structure tensor.</b> By a first-order Taylor expansion, $E(u,v)\approx\begin{pmatrix}u&v\end{pmatrix}M\begin{pmatrix}u\\v\end{pmatrix}$ with the structure tensor $M=\sum_{x,y}w(x,y)\begin{pmatrix}I_x^2&I_xI_y\\I_xI_y&I_y^2\end{pmatrix}$. The level sets of $E$ are ellipses with axes proportional to $1/\sqrt{\lambda_{1,2}}$, where $\lambda_1,\lambda_2$ are the eigenvalues of $M$. Both small: flat; one large and one small: edge; both large: corner.",
  hint="What shape does the change E take for the road, the kerb and the window corner?",
  breakdown=[r"<strong>$M=\sum w\,[\,I_x^2,\ I_xI_y;\ I_xI_y,\ I_y^2\,]$ = the window's gradient pattern.</strong> It collects how the gradients inside the window line up, so it needs a whole window, not one pixel.",
             r"<strong>$\lambda_1,\lambda_2$ = change along the two main directions.</strong> The eigenvalues of $M$ are how fast the patch changes along its two principal axes.",
             r"<strong>Ellipse $E=\text{const}$ = the picture.</strong> A flat patch has a huge ellipse (nothing changes), an edge a long thin one, a corner a small round one; both eigenvalues large means a corner."],
  conn=r"<strong>Reading the window's change as a shape.</strong> For the kerb the slide-along direction costs nothing, so the ellipse stretches along the kerb; at the shop window corner it is small and round, so the corner is sharp in every direction.",
  cap="The set E(u, v) = const is an ellipse with axes ∝ 1/√λ: huge for flat (λ₁, λ₂ small), long and thin for an edge, small and round for a corner (λ₁, λ₂ large)."),
3153: dict(d=d3153, stmtKind="DEFINITION",
  statement=r"<b>Harris corner response.</b> $R=\det M-k\,(\operatorname{tr}M)^2=\lambda_1\lambda_2-k(\lambda_1+\lambda_2)^2$, with $k\approx0.04$–$0.06$. $R\gg0$ indicates a corner, $R\lt0$ an edge, and $|R|\approx0$ a flat region. The Shi–Tomasi detector instead uses $\min(\lambda_1,\lambda_2)$ and thresholds it.",
  hint="How can you tell corner, edge and flat without computing eigenvalues?",
  breakdown=[r"<strong>$\det M=\lambda_1\lambda_2$ = both are large.</strong> The product is big only if both eigenvalues are big, which means a corner.",
             r"<strong>$\operatorname{tr}M=\lambda_1+\lambda_2$ = the total change.</strong> An edge has one large eigenvalue, so $\operatorname{tr}^2$ is large and $\det$ is small, making $R$ negative.",
             r"<strong>$k$ = how hard to punish edges.</strong> A bigger $k$ rejects edges more but misses faint corners; there is no single right value. No eigendecomposition is needed."],
  conn=r"<strong>One number for every pixel of the frame.</strong> The shop window's corner scores highly positive, the kerb scores negative, the road near zero; the camera marks the high scores as landmarks for tracking.",
  cap="In the (λ₁, λ₂) plane the shaded region (both large) is a corner with R ≫ 0, the strips along the axes (one small) are edges with R < 0, and the origin is flat."),
3154: dict(d=d3154, stmtKind="ALGORITHM",
  statement=r"<b>Harris corner detector.</b> (1) Compute the image derivatives $I_x,I_y$. (2) Form $I_x^2$, $I_xI_y$, $I_y^2$ at every pixel. (3) Smooth each with a Gaussian window $G_\sigma$ to get $M(x,y)=G_\sigma\ast\begin{pmatrix}I_x^2&I_xI_y\\I_xI_y&I_y^2\end{pmatrix}$. (4) Compute $R=\det M-k(\operatorname{tr}M)^2$. (5) Keep pixels with $R\gt\tau$ that are local maxima in a $3\times3$ neighbourhood.",
  hint="In which order do you take derivatives, multiply and smooth to build the structure tensor?",
  breakdown=[r"<strong>$I_x,I_y$ then $I_x^2,I_xI_y,I_y^2$ = per-pixel gradient products.</strong> Three images, each a different product of the same two derivatives.",
             r"<strong>$G_\sigma\ast(\cdot)$ = the window sum.</strong> Smoothing the three product images with a Gaussian gives $M$ at every pixel; a Gaussian is the same in every direction.",
             r"<strong>$R>\tau$ and local maximum = the corners.</strong> Score each pixel, threshold, then keep only the peak in each $3\times3$ neighbourhood."],
  conn=r"<strong>Marking landmarks on the street frame.</strong> The pipeline turns the frame into a score map; the sharpest peaks sit on the corners of windows, doors and signs. Smoothing the image first would not give the same result.",
  cap="Harris in five steps: derivatives, their products, Gaussian smoothing to M, the response R = det M − k tr²M, and local maxima above a threshold."),
3155: dict(d=d3155, stmtKind="PROPOSITION",
  statement=r"<b>Invariance of the Harris response.</b> $R$ is invariant to rotation (the eigenvalues of $M$ do not change when the image is rotated) and to an additive intensity change $I\to I+b$ (only derivatives enter); under $I\to aI$ it scales as $R\to a^4R$, so thresholds must be relative. It is not invariant to scale: a corner seen at one scale can look like an edge at a larger one.",
  hint="If the camera zooms in on a window corner, does it still look like a corner?",
  breakdown=[r"<strong>Rotation: $R$ unchanged.</strong> Turning the frame turns $M$ but leaves its eigenvalues, so a corner stays a corner."],
  conn=r"<strong>Tilting and brightening the camera.</strong> A window corner is still found when the pole tilts, or when a cloud passes. But zoom in on the same corner and the curve that was a corner can look like a straight edge.",
  cap="The corner is found after the frame is rotated (same R). Zoomed in, the same corner fills the window and looks like an edge: R is not scale invariant."),
3156: dict(d=d3156, stmtKind="WORKED EXAMPLE",
  statement=r"<b>Example.</b> With $k=0.05$: a corner window with $M=\operatorname{diag}(10,10)$ has $\det M=100$, $\operatorname{tr}M=20$ and $R=100-0.05\cdot400=80$. An edge window with $M=\operatorname{diag}(10,0)$ has $\det M=0$, $\operatorname{tr}M=10$ and $R=0-0.05\cdot100=-5$. A flat window with $M=0$ has $R=0$.",
  hint="What are the signs of R for the shop-window corner, the kerb and the empty road?",
  breakdown=[r"<strong>Corner: $\det=100,\ \operatorname{tr}=20$, so $R=80$.</strong> Both eigenvalues are 10: a large positive response."],
  conn=r"<strong>Three numbers for three places.</strong> The shop-window corner scores +80, the kerb −5, the empty road 0. Positive means landmark, negative means line, zero means nothing there.",
  cap="With k = 0.05: corner M = diag(10, 10) gives R = 80; edge M = diag(10, 0) gives R = −5; flat M = 0 gives R = 0."),
}
CARDS[3155]["breakdown"] += [r"<strong>$I\to I+b$: $R$ unchanged; $I\to aI$: $R\to a^4R$.</strong> A constant offset disappears in the derivatives, but a gain multiplies both $I_x$ and $I_y$, so $M$ by $a^2$ and $R$ by $a^4$.",
                             r"<strong>Scale: $R$ changes.</strong> The window sees a different piece of the curve, so a corner can become an edge when zoomed in; this motivates scale-space detection (Harris–Laplace, SIFT)."]
CARDS[3156]["breakdown"] += [r"<strong>Edge: $\det=0,\ \operatorname{tr}=10$, so $R=-5$.</strong> One eigenvalue is 0 and the squared trace is penalised: a negative number.",
                             r"<strong>Flat: $M=0$, so $R=0$.</strong> Corner is large positive, edge negative, flat near zero: the sign and size of $R$ separate the three cases."]

STORY = {
 3151: dict(s="STORY 6 · STEP 13 · LANDMARKS", b="Slide a small window: only at a <b>corner</b> does it change in every direction, so only corners can be pinned down.",
   f=[["3131", "edges"], ["3146", "lines"]], n=[["3152", "the shape of the change"]]),
 3152: dict(s="STORY 6 · STEP 14 · THE SHAPE OF CHANGE", b="The window-shift energy is an <b>ellipse</b> set by the eigenvalues of the structure tensor $M$.",
   f=[["3151", "window shift"], ["3084", "eigenvectors"]], n=[["3153", "a score"]]),
 3153: dict(s="STORY 6 · STEP 15 · ONE SCORE", b="<b>$R=\\det M-k\\,\\mathrm{tr}^2M$</b> separates corner, edge, flat without eigenvalues.",
   f=[["3152", "the ellipse"]], n=[["3154", "the whole pipeline"]]),
 3154: dict(s="STORY 6 · STEP 16 · THE PIPELINE", b="Gradients, products, Gaussian smoothing, response, local maxima.",
   f=[["3153", "R"], ["3054", "Gaussian smoothing"]], n=[["3155", "what it survives"]]),
 3155: dict(s="STORY 6 · STEP 17 · WHAT IT SURVIVES", b="Rotation and brightness offset: yes. <b>Scale</b>: no, so we need scale space.",
   f=[["3154", "the detector"]], n=[["3156", "numbers"], ["3161", "SIFT adds scale"]]),
 3156: dict(s="STORY 6 · STEP 18 · CHECK BY HAND", b="$R=80$ (corner), $-5$ (edge), $0$ (flat).",
   f=[["3153", "R"]], n=[["3161", "next: landmarks at every scale"]]),
}
FIX = build_fix(CARDS)
