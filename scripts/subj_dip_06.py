"""DIP topic 06 (LSI systems, convolution, spatial filtering). Everyday picture: a street camera on a pole."""
from street_lib import *

SUBJECT = "DIP"

def row(x, y, vals, cell=16, sz=8, shade=None):
    return pix(x, y, [vals], cell, sz, shade)

def d3051(c):
    return svg(c,
        N(30, 14, "one bright dot", 7), pix(10, 20, [["", "", ""], ["", "1", ""], ["", "", ""]], 14, 8),
        arrow(54, 41, 80, 41, 1), N(67, 34, "LSI", 8), R(82, 22, 30, 38, "#f1f5f9", 1), N(97, 38, "lens", 7), N(97, 48, "system", 7),
        arrow(112, 41, 134, 41, 1), N(176, 14, "h = its response (PSF)", 7), pix(140, 20, [[".05", ".1", ".05"], [".1", ".4", ".1"], [".05", ".1", ".05"]], 20, 7, {(1, 1)}),
        N(120, 100, "any frame f = Σ f(m, n) · (dot at m, n)", 7.5),
        N(120, 113, "g(x, y) = Σ Σ f(m, n) · h(x − m, y − n)", 8),
        N(120, 128, "shift the input ⇒ the output shifts the same way", 7.5))

def d3052(c):
    return svg(c,
        N(10, 16, "f", 8, "start"), row(30, 6, [1, 2, 3, 4], 18),
        N(10, 40, "h", 8, "start"), row(30, 30, [1, 0, -1], 18), N(100, 40, "correlation: as it is", 7, "start"),
        N(10, 64, "flip", 7, "start"), row(30, 54, [-1, 0, 1], 18), N(100, 64, "convolution: turned round first", 7, "start"),
        L(10, 76, 230, 76, .5),
        N(10, 92, "f ∗ h", 8, "start"), row(30, 82, [1, 2, 2, 2, -3, -4], 18, 8, {(0, 2), (0, 3)}),
        N(10, 112, "f ⋆ h", 8, "start"), row(30, 102, [-1, -2, -2, -2, 3, 4], 18, 8),
        N(150, 124, "only the sign flips", 7.5, "start"), N(120, 138, "symmetric kernels: both are the same", 7.5))

def d3053(c):
    return svg(c,
        N(30, 14, "h₁ (down)", 7), pix(18, 20, [["1"], ["2"], ["1"]], 14, 8),
        N(62, 44, "×", 10), N(104, 14, "h₂ᵀ (across)", 7), pix(80, 20, [["1", "2", "1"]], 14, 8),
        N(130, 44, "=", 10), N(188, 14, "h = h₁h₂ᵀ", 7), pix(150, 20, [["1", "2", "1"], ["2", "4", "2"], ["1", "2", "1"]], 14, 8),
        N(120, 82, "f ∗ h = (f ∗ᵧ h₂) ∗ₓ h₁", 8),
        N(120, 96, "one pass along the rows, one down the columns", 7.5),
        N(120, 110, "K² multiplies per pixel → 2K", 8),
        N(120, 126, "separable ⇔ the kernel matrix has rank 1", 7.5))

def d3054(c):
    b = 76
    return svg(c,
        axes(14, b, 110, 14), N(110, b + 10, "x", 8, "end"),
        R(42, b - 36, 36, 36, "none", 1, 0, "3 2"), N(22, b - 40, "box (1/K²)", 7, "start"),
        bell(18, 106, 60, 14, 52, b, 1), N(80, 30, "Gaussian", 7, "start"),
        N(60, b + 10, "σ", 7), L(60, b + 3, 74, b + 3, .8),
        axes(128, b, 232, 14), N(232, b + 10, "x", 8, "end"),
        L(132, b - 8, 178, b - 8, 1), L(178, b - 8, 178, b - 52, 1), L(178, b - 52, 228, b - 52, 1),
        curve(lambda x: b - 8 - 44 / (1 + math.exp(-(x - 178) / 9)), 132, 228, 50, 1, "3 2"), N(180, b - 56, "edge", 7, "start"),
        N(120, 104, "G(x, y) = (1/2πσ²) exp(−(x² + y²)/2σ²)", 8), N(120, 118, "box K×K: noise variance ÷ K²", 7.5), N(120, 132, "bigger kernel: less noise, blurrier street edges", 7.5))

def d3055(c):
    sm = lambda x, lo, hi, x0, w: lo - (lo - hi) / (1 + math.exp(-(x - x0) / w))
    return svg(c,
        N(14, 10, "f", 8, "start"), L(14, 44, 62, 44, 1), L(62, 44, 62, 20, 1), L(62, 20, 110, 20, 1),
        N(122, 10, "f̄ (blurred copy)", 7, "start"), curve(lambda x: sm(x, 44, 20, 176, 8), 122, 230, 50, 1),
        N(14, 62, "f − f̄  (the detail)", 7, "start"), L(14, 84, 110, 84, .5, "1 3"),
        curve(lambda x: 84 + 12 * math.exp(-((x - 52) / 6) ** 2) - 12 * math.exp(-((x - 72) / 6) ** 2), 14, 110, 80, 1),
        N(122, 62, "g = f + k (f − f̄)", 7, "start"),
        curve(lambda x: (100 if x < 176 else 76) + 9 * math.exp(-((x - 170) / 5) ** 2) - 9 * math.exp(-((x - 182) / 5) ** 2), 122, 230, 120, 1),
        N(172, 116, "undershoot", 6.5, "end"), N(184, 70, "overshoot", 6.5, "start") if False else N(186, 72, "overshoot", 6.5, "start"),
        N(120, 126, "Laplacian version: g = f − c ∇²f , ∇²f = fₓₓ + fᵧᵧ", 7.5),
        N(120, 139, "edges look crisper, noise is boosted too", 7.5))

def d3056(c):
    return svg(c,
        N(10, 16, "f", 8, "start"), row(30, 6, [1, 2, 3, 4], 18),
        N(10, 40, "flip h", 7, "start"), row(30, 30, [-1, 0, 1], 18),
        N(110, 20, "slide it along f, add the products", 7, "start"),
        N(110, 40, "n = 2:  3·1 + 1·(−1) = 2", 7, "start"),
        N(110, 52, "n = 4:  4·(−1) = −3 (no 3 to its right)", 7, "start") if False else "",
        N(10, 80, "f ∗ h", 8, "start"), row(30, 70, [1, 2, 2, 2, -3, -4], 22, 9, {(0, 1), (0, 2), (0, 3)}),
        N(30, 100, "end", 6.5), N(52, 100, "", 6),
        N(120, 112, "length = M + K − 1 = 4 + 3 − 1 = 6", 8),
        N(120, 126, "middle value 2 = slope of the ramp; ends = zero-padding", 7.5),
        N(120, 139, "correlation would give −2 inside", 7.5))

CARDS = {
3051: dict(d=d3051, stmtKind="THEOREM",
  statement=r"<b>Convolution representation of an LSI system.</b> Let $\mathcal S$ be a linear, shift-invariant system and $h(x,y)=\mathcal S[\delta](x,y)$ its impulse response (point spread function). Then for every input $f$ its output is $g(x,y)=\sum_m\sum_n f(m,n)\,h(x-m,\,y-n)=(f\ast h)(x,y)$.",
  hint="If you know what one bright dot becomes in the street frame, what do you know about every other frame?",
  breakdown=[r"<strong>$h$ = what a single bright dot becomes.</strong> Send one point of light through the lens and record the smear: that small array is the whole system.",
             r"<strong>$f(m,n)$ = how bright the dot at $(m,n)$ is.</strong> Any frame is a sum of such dots, each scaled by its own brightness (linearity).",
             r"<strong>$h(x-m,\,y-n)$ = the same smear, moved to where the dot sits.</strong> Shift-invariance means each dot makes the same smear, placed at its own position; adding them all gives $g$."],
  conn=r"<strong>One bright lamp tells the whole lens.</strong> Film a single far-away lamp through the street camera's lens: the smear it makes is $h$. If the lens treats every part of the frame the same way, that one smear predicts what every other pixel of the street becomes.",
  cap="One bright dot goes through the lens system and comes out as the smear h (the PSF). A frame f is a sum of weighted dots, so the output g(x, y) = Σ f(m, n) h(x−m, y−n)."),
3052: dict(d=d3052, stmtKind="DEFINITION",
  statement=r"<b>Convolution and correlation.</b> For sequences $f,h$: convolution $(f\ast h)(x)=\sum_m f(m)\,h(x-m)$ (the kernel is reflected, then slid), and cross-correlation $(f\star h)(x)=\sum_m f(m)\,h(m-x)$ in which the kernel is not flipped. In 2D the reflection is by $180^\circ$. They coincide when $h$ is symmetric.",
  hint="Why does the same edge kernel give the opposite sign if you forget to turn it round?",
  breakdown=[r"<strong>$h(x-m)$ = the kernel turned round.</strong> The minus sign flips the kernel before it is slid; this is what makes convolution commute and match LSI systems.",
             r"<strong>$h(m-x)$ = the kernel as written.</strong> This is template matching, and what most deep-learning libraries compute under the name 'convolution'.",
             r"<strong>Symmetric $h$ gives the same answer; $[1,0,-1]$ gives the negative.</strong> Only a flip-sensitive (odd) kernel makes the difference visible."],
  conn=r"<strong>Reading a kerb edge's sign.</strong> A rising brightness edge in the street frame gives a positive response with one convention and a negative with the other, so always check which one the tool uses.",
  cap="The same kernel h = [1, 0, −1] slid along f: convolution turns it round first, correlation uses it as written, and the two outputs differ only in sign."),
3053: dict(d=d3053, stmtKind="PROPOSITION",
  statement=r"<b>Separable kernels.</b> A 2D kernel $h$ is separable if $h(x,y)=h_1(x)\,h_2(y)$, i.e. the kernel matrix equals $\mathbf h_1\mathbf h_2^{\top}$ and has rank 1. Then $f\ast h=(f\ast_y h_2)\ast_x h_1$: a convolution with a $K\times K$ kernel costs $2K$ multiplications per pixel instead of $K^2$. The Gaussian $G_\sigma(x,y)=G_\sigma(x)G_\sigma(y)$ and the box are separable.",
  hint="How can you blur the frame with two small passes instead of one big one?",
  breakdown=[r"<strong>$\mathbf h_1\mathbf h_2^{\top}$ = a column times a row.</strong> Each entry of the kernel is the product of a vertical weight and a horizontal weight.",
             r"<strong>$(f\ast_y h_2)\ast_x h_1$ = two 1D passes.</strong> Blur along each row, then blur the result down each column; the order does not matter.",
             r"<strong>$2K$ instead of $K^2$ = the saving.</strong> For a $15\times15$ blur this is 30 multiplies per pixel instead of 225. Only rank-1 kernels qualify."],
  conn=r"<strong>Blurring the 1920×1080 street frame in real time.</strong> A Gaussian blur done as a pass along the rows and a pass down the columns is what makes it cheap enough to run on every frame of the camera.",
  cap="A 3×3 kernel h is a column h₁ times a row h₂ᵀ, so f ∗ h is one pass along the rows and one down the columns, 2K multiplies instead of K²."),
3054: dict(d=d3054, stmtKind="DEFINITION",
  statement=r"<b>Smoothing filters.</b> The $K\times K$ box (mean) filter replaces each pixel by the average of its neighbourhood; for independent zero-mean noise of variance $\sigma_\eta^2$ the variance of the output is $\sigma_\eta^2/K^2$. The Gaussian filter has kernel $G_\sigma(x,y)=\frac{1}{2\pi\sigma^2}e^{-(x^2+y^2)/2\sigma^2}$, is separable, and its Fourier transform is also Gaussian.",
  hint="Why is the Gaussian preferred over the plain box for blurring the street frame?",
  breakdown=[r"<strong>$\sigma_\eta^2/K^2$ = what averaging does to noise.</strong> Averaging $K^2$ noisy pixels divides the noise variance by $K^2$, but a bigger window also blurs the real edges.",
             r"<strong>$e^{-(x^2+y^2)/2\sigma^2}$ = weights that fade smoothly.</strong> Near pixels count more, far ones almost nothing, with no hard cut like a box.",
             r"<strong>$1/2\pi\sigma^2$ = keep the total weight at 1.</strong> The average brightness of the frame does not change. $\sigma$ sets how wide the blur is."],
  conn=r"<strong>Calming the grain at night.</strong> The camera's night footage is full of speckle. A Gaussian average over a few pixels calms it, at the price of softening the edge of the kerb and the shop sign.",
  cap="In one dimension a box (dashed) and a Gaussian of width σ average the neighbourhood; on the right, a step edge in the street frame gets blurred. A bigger kernel means less noise but a softer edge."),
3055: dict(d=d3055, stmtKind="ALGORITHM",
  statement=r"<b>Unsharp masking and Laplacian sharpening.</b> Given an image $f$ and a blurred copy $\bar f$, the mask is $m=f-\bar f$ and the sharpened image is $g=f+k\,m$ ($k=1$ unsharp masking, $k\gt1$ high-boost). Laplacian sharpening: $g=f-c\,\nabla^2f$ where $\nabla^2f=f_{xx}+f_{yy}$ and $c\gt0$ when the Laplacian kernel has a negative centre coefficient.",
  hint="If you subtract a blurred copy from the frame, what is left, and what happens when you add it back?",
  breakdown=[r"<strong>$m=f-\bar f$ = the fine detail.</strong> The frame minus its blur keeps only edges and small features.",
             r"<strong>$f+k\,m$ = put the detail back, stronger.</strong> A gain $k\gt1$ exaggerates edges and gives overshoot on the bright side and undershoot on the dark side.",
             r"<strong>$-c\,\nabla^2f$ = the Laplacian does the same.</strong> $\nabla^2f$ is large at edges, so subtracting it (for a negative-centre kernel) steepens them."],
  conn=r"<strong>Reading the shop sign.</strong> A slightly soft frame of the sign gets crisper when the blurred copy is subtracted and the detail added back. The same step also boosts the noise in the dark street.",
  cap="A step edge f and its blurred copy f̄; the difference f − f̄ is the detail. Adding k times it gives g, which overshoots on the bright side and undershoots on the dark side."),
3056: dict(d=d3056, stmtKind="WORKED EXAMPLE",
  statement=r"<b>Example.</b> Let $f=[1,2,3,4]$ and $h=[1,0,-1]$. The full convolution has length $M+K-1=6$: $f\ast h=[1,\,2,\,2,\,2,\,-3,\,-4]$. Interior values equal $f(n)-f(n-2)$, the discrete derivative of the ramp; the end values come from zero-padding. Correlation gives the negative of the interior values.",
  hint="Which entries of f ∗ h are real slope, and which come from running off the ends?",
  breakdown=[r"<strong>Flip $h$ to $[-1,0,1]$.</strong> Convolution turns the kernel round before sliding it along $f=[1,2,3,4]$.",
             r"<strong>$n=2:\ 3-1=2$, $n=3:\ 4-2=2$ = the slope of the ramp.</strong> Each interior value is a difference of two pixels, which for a unit ramp is 2.",
             r"<strong>Length $4+3-1=6$ and ends $1,2,-3,-4$ = zero-padding.</strong> At the ends the kernel hangs off the data, so those entries are not real slope."],
  conn=r"<strong>A strip of four pixels across the kerb.</strong> The brightness rises 1, 2, 3, 4. The derivative kernel reports a steady slope of 2 inside and false jumps at the ends of the strip.",
  cap="The four pixels f = [1, 2, 3, 4] with the flipped kernel [−1, 0, 1] slid along them give [1, 2, 2, 2, −3, −4]: a steady 2 inside and zero-padding values at the ends."),
}

STORY = {
 3051: dict(s="STORY 3 · STEP 1 · THE LENS AS A SYSTEM", b="A lens that treats every part of the frame alike is <b>linear and shift-invariant</b>, so one smear $h$ describes it and the output is a convolution.",
   f=[["3046", "from single-pixel curves to neighbourhoods"], ["40105", "the frame"]], n=[["3052", "the flip"], ["3053", "cheap kernels"], ["3101", "undoing the blur"]]),
 3052: dict(s="STORY 3 · STEP 2 · THE FLIP", b="<b>Convolution</b> flips the kernel; <b>correlation</b> does not. Symmetric kernels hide the difference.",
   f=[["3051", "convolution"]], n=[["3053", "kernel structure"], ["3056", "a small example"]]),
 3053: dict(s="STORY 3 · STEP 3 · CHEAP KERNELS", b="A rank-1 kernel splits into a row pass and a column pass: <b>$2K$ instead of $K^2$</b>.",
   f=[["3051", "the sum over a kernel"]], n=[["3054", "the Gaussian is separable"], ["3133", "LoG"]]),
 3054: dict(s="STORY 3 · STEP 4 · SMOOTH", b="<b>Averaging</b> removes noise but blurs edges; the Gaussian averages smoothly and is separable.",
   f=[["3053", "separable"]], n=[["3055", "the opposite: sharpen"], ["3132", "Sobel's smoothing"], ["3161", "scale space"]]),
 3055: dict(s="STORY 3 · STEP 5 · SHARPEN", b="Subtract a blur to find the detail, then <b>add it back stronger</b>: unsharp mask and Laplacian.",
   f=[["3054", "the blur"]], n=[["3056", "a small example"], ["3133", "Laplacian of Gaussian"]]),
 3056: dict(s="STORY 3 · STEP 6 · CHECK BY HAND", b="A four-pixel strip through a derivative kernel: <b>steady slope inside, padding at the ends</b>.",
   f=[["3052", "the flip"]], n=[["3061", "next: the same filters in the frequency view"]]),
}
FIX = build_fix(CARDS)
