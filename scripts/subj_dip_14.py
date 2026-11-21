"""DIP topic 14 (edge detection). Everyday picture: a street camera on a pole (the shop-front outline)."""
from street_lib import *

SUBJECT = "DIP"

def d3131(c):
    b = 104
    return svg(c,
        N(40, 12, "shop wall | road", 7), R(10, 18, 60, 50, "#d9dee7", 1), R(40, 18, 30, 50, "#ffffff", 1), L(40, 18, 40, 68, 1.2),
        arrow(24, 44, 56, 44, 1), N(28, 38, "∇f", 8, "start"), N(40, 80, "edge", 7), N(24, 78, "θ ⟂ edge", 6.5, "start") if False else "",
        N(160, 12, "f along the row", 7), L(90, 46, 150, 46, 1), L(150, 46, 150, 26, 1), L(150, 26, 230, 26, 1) if False else "",
        poly([(90, 46), (150, 46), (150, 24), (232, 24)], 1),
        N(160, 62, "|f′|", 7), poly([(90, 80), (140, 80), (150, 60), (160, 80), (232, 80)], 1, "3 2") if False else "",
        curve(lambda x: 92 - 24 * math.exp(-((x - 150) / 7) ** 2), 90, 232, 60, 1),
        N(120, 112, "M = √(fₓ² + fᵧ²)  or  |fₓ| + |fᵧ|", 7.5), N(120, 126, "θ = atan2(fᵧ, fₓ)  points across the edge", 7.5),
        N(120, 140, "the edge itself runs perpendicular to ∇f", 7.5))

def d3132(c):
    return svg(c,
        N(20, 12, "smooth", 7), pix(10, 18, [["1"], ["2"], ["1"]], 20, 9), N(52, 52, "×", 10),
        N(96, 12, "derivative", 7), pix(66, 18, [["−1", "0", "1"]], 20, 9), N(134, 52, "=", 10),
        N(176, 12, "Sₓ", 8), pix(146, 18, [["−1", "0", "1"], ["−2", "0", "2"], ["−1", "0", "1"]], 20, 9),
        N(120, 96, "Sₓ reacts to vertical edges, Sᵧ to horizontal ones", 7.5),
        N(120, 110, "slide as masks:  M = √(fₓ² + fᵧ²)", 8),
        N(120, 124, "the [1, 2, 1] smoothing keeps the noise down", 7.5), N(120, 138, "Prewitt [1,1,1] · Scharr [3,10,3]", 7))

def d3133(c):
    return svg(c,
        N(14, 12, "f", 7, "start"), poly([(14, 52), (80, 52), (80, 30), (130, 30)], 1),
        curve(lambda x: 52 - 22 / (1 + math.exp(-(x - 80) / 8)), 14, 130, 50, 1, "3 2"), N(120, 24, "blurred", 6.5),
        L(14, 92, 130, 92, .5, "1 3"), N(14, 66, "f″ of the blurred edge", 7, "start"),
        curve(lambda x: 92 - 16 * (math.exp(-((x - 73) / 7) ** 2) - math.exp(-((x - 87) / 7) ** 2)), 14, 130, 60, 1),
        L(80, 72, 80, 112, .6, "2 2"), N(80, 122, "zero-crossing = edge", 7),
        N(180, 12, "LoG kernel ∇²Gσ", 7.5), L(150, 44, 232, 44, .5, "1 3"),
        curve(lambda x: 44 + 26 * (1 - ((x - 190) / 14) ** 2) * math.exp(-((x - 190) / 14) ** 2 / 2), 152, 230, 60, 1),
        N(190, 90, "σ = scale knob", 7.5), N(190, 102, "bigger σ: coarser edges only", 7))

def d3134(c):
    g = lambda s: (lambda x: 80 - 64 * math.exp(-((x - 120) / s) ** 2))
    b = 112
    return svg(c,
        N(14, 12, "two blurs of the same frame", 7, "start"),
        curve(lambda x: 56 - 36 * math.exp(-((x - 60) / 10) ** 2), 14, 106, 50, 1), N(60, 70, "Gσ", 7),
        curve(lambda x: 56 - 22 * math.exp(-((x - 60) / 16) ** 2), 14, 106, 50, 1, "3 2"), N(96, 40, "Gkσ", 7),
        N(120, 76, "subtract", 7.5), 
        L(130, 50, 232, 50, .5, "1 3"),
        curve(lambda x: 50 + 26 * (1 - ((x - 180) / 12) ** 2) * math.exp(-((x - 180) / 12) ** 2 / 2), 134, 228, 60, 1),
        N(180, 96, "DoG ≈ LoG", 7.5),
        N(120, 112, "Gkσ − Gσ ≈ (k − 1) σ² ∇²Gσ", 8), N(120, 126, "two blurs and a subtraction beat a LoG kernel", 7.5), N(120, 139, "same trick finds scale extrema in SIFT", 7.5))

def d3135(c):
    out = []
    labs = [("1 blur", "Gσ"), ("2 gradient", "M, θ"), ("3 thin", "NMS"), ("4 link", "hysteresis")]
    for i, (a, b) in enumerate(labs):
        x = 8 + i * 58
        out += [R(x, 14, 50, 36, "#f1f5f9", 1), N(x + 25, 28, a, 7), N(x + 25, 42, b, 7)]
        if i < 3: out.append(arrow(x + 50, 32, x + 58, 32, 1))
    out += [N(40, 66, "keep a pixel only if M beats", 7, "start"), N(40, 77, "its two neighbours along θ", 7, "start"),
            R(150, 62, 80, 22, "#ffffff", 1)]
    for k, v in enumerate((8, 14, 24, 14, 8)):
        out.append(R(150 + k * 16, 84 - v, 16, v, "#d9dee7" if k == 2 else "#f1f5f9", .6))
    out += [N(190, 96, "across the edge", 6.5), N(120, 112, "Thigh ≈ 2–3 · Tlow", 8), N(120, 126, "strong seeds, weak kept only if 8-connected to one", 7.5),
            N(120, 139, "good detection · good localisation · single response", 7)]
    return svg(c, *out)

def d3136(c):
    vals = [20, 45, 95, 40, 25, 60, 28]
    out = [L(14, 100, 232, 100, 1)]
    for i, v in enumerate(vals):
        x = 22 + i * 30
        sh = "#b8c0cc" if i in (1, 2, 3) else "#ffffff"
        out += [R(x, 100 - v * .8, 22, v * .8, sh, .8), N(x + 11, 96 if v == 20 else 94 - v * .8, str(v), 7)]
    out += [L(14, 100 - 90 * .8, 232, 100 - 90 * .8, .6, "3 2"), N(230, 100 - 90 * .8 - 3, "Thigh = 90", 7, "end"),
            L(14, 100 - 30 * .8, 232, 100 - 30 * .8, .6, "3 2"), N(14, 100 - 30 * .8 - 10, "Tlow = 30", 7, "start"),
            N(93, 112, "kept: 45, 95, 40", 7.5), N(126, 124, "60: above Tlow but cut off by 25 ⇒ dropped", 7.5),
            N(120, 138, "one threshold: speckle (30) or a broken edge (90)", 7)]
    return svg(c, *out)

CARDS = {
3131: dict(d=d3131, stmtKind="DEFINITION",
  statement=r"<b>Image gradient.</b> For an image $f(x,y)$ the gradient is $\nabla f=\begin{pmatrix}\partial f/\partial x\\ \partial f/\partial y\end{pmatrix}$. It points in the direction of steepest increase; its magnitude $M=\lvert\nabla f\rvert=\sqrt{f_x^2+f_y^2}$ (often approximated by $|f_x|+|f_y|$) measures edge strength, and its direction $\theta=\operatorname{atan2}(f_y,f_x)$ is perpendicular to the edge.",
  hint="Along which direction does the shop wall's outline run, compared with the way the gradient points?",
  breakdown=[r"<strong>$\nabla f=(f_x,f_y)$ = how fast brightness changes along each axis.</strong> At an edge, brightness jumps from the wall to the road.",
             r"<strong>$M=\sqrt{f_x^2+f_y^2}$ = how strong the edge is.</strong> The size of the steepest change; large $M$ marks edge pixels.",
             r"<strong>$\theta=\operatorname{atan2}(f_y,f_x)$ = which way the jump goes.</strong> It points across the edge, so the edge itself runs perpendicular to $\theta$."],
  conn=r"<strong>Finding the shop front in the frame.</strong> Along a row across the wall's edge the brightness steps up; the change is large exactly at the outline. The gradient's arrow points straight across the outline, not along it.",
  cap="Across the wall-road edge f steps and |f′| peaks. The gradient ∇f points across the edge with strength M and angle θ; the edge runs perpendicular to it."),
3132: dict(d=d3132, stmtKind="DEFINITION",
  statement=r"<b>Sobel operator.</b> The Sobel kernels $S_x=\begin{pmatrix}1\\2\\1\end{pmatrix}\begin{pmatrix}-1&0&1\end{pmatrix}=\begin{pmatrix}-1&0&1\\-2&0&2\\-1&0&1\end{pmatrix}$ and $S_y=S_x^{\top}$, slid over the image as masks (correlation), estimate the partial derivatives $f_x,f_y$; $S_x$ responds to vertical edges and $S_y$ to horizontal ones. The edge magnitude is $M=\sqrt{f_x^2+f_y^2}$. Each kernel is a smoothing $[1,2,1]$ times a derivative $[-1,0,1]$, so noise is averaged along the edge.",
  hint="Why does Sobel average three rows before taking the difference?",
  breakdown=[r"<strong>$[-1,0,1]$ = the derivative.</strong> The pixel on the right minus the pixel on the left: large when brightness changes across the pixel.",
             r"<strong>$[1,2,1]^{\top}$ = smoothing along the edge.</strong> The difference is averaged over three rows with the middle row counted twice, which calms the speckle.",
             r"<strong>$\sqrt{f_x^2+f_y^2}$ = combine both directions.</strong> Vertical and horizontal responses give the total edge strength.",
             r"<strong>Mask slid without flipping = right minus left.</strong> This is correlation. True convolution flips the kernel, which changes the sign of $f_x,f_y$ and turns $\theta$ by $180^\circ$, but leaves $M$ the same.",
             r"<strong>Entries sum to $0$ = no response on a flat patch.</strong> Every derivative filter has this property, and Sobel is also separable: a column times a row."],
  conn=r"<strong>Night footage speckle.</strong> A bare pixel difference jumps at every speckle; Sobel's three-row average ignores most of it, and still lights up the shop front's outline.",
  cap="The Sobel kernel Sₓ is a smoothing column [1, 2, 1] times a derivative row [−1, 0, 1]. It responds to vertical edges and is steadier against noise than a plain difference."),
3133: dict(d=d3133, stmtKind="ALGORITHM",
  statement=r"<b>Marr–Hildreth (Laplacian of Gaussian) edge detector.</b> Edges are the zero-crossings of the second derivative of the smoothed image. Convolve with $\nabla^2G_\sigma(x,y)=\frac1{\pi\sigma^4}\Big(\frac{x^2+y^2}{2\sigma^2}-1\Big)e^{-\frac{x^2+y^2}{2\sigma^2}}$ (since $f\ast\nabla^2G_\sigma=\nabla^2(G_\sigma\ast f)$), and mark the points where the result changes sign, with a slope or magnitude test to discard weak ones. $\sigma$ sets the scale of the edges found.",
  hint="Where does the second derivative of a blurred step cross zero?",
  breakdown=[r"<strong>$G_\sigma$ = blur first.</strong> Derivatives amplify noise, so smooth by $\sigma$ before differentiating.",
             r"<strong>$\nabla^2$ = the second derivative.</strong> At a step edge the second derivative goes up, then down, crossing zero exactly where the slope is steepest.",
             r"<strong>$\nabla^2G_\sigma$ = both in one kernel.</strong> Because both operations are linear, the 'Mexican hat' kernel does the blur and the Laplacian at once; larger $\sigma$ keeps only coarse edges.",
             r"<strong>$\nabla^2G_\sigma=0$ at $r=\sqrt{x^2+y^2}=\sqrt2\,\sigma$.</strong> The bracket vanishes when $r^2=2\sigma^2$. The centre value is $-1/(\pi\sigma^4)$, so $\nabla^2G_\sigma$ has a negative centre and a positive ring; the 'Mexican hat' is its negative."],
  conn=r"<strong>Outline of the shop at different zoom levels.</strong> A small $\sigma$ finds every brick; a large $\sigma$ finds only the building's outline. The zero-crossings link into closed contours.",
  cap="A step edge f, its blurred version, and f″ of the blurred edge: the zero-crossing sits at the edge. The LoG kernel (right, negative centre) does blur and Laplacian in one; σ is the scale knob."),
3134: dict(d=d3134, stmtKind="PROPOSITION",
  statement=r"<b>Difference of Gaussians approximates the Laplacian of Gaussian.</b> Since $\partial G_\sigma/\partial\sigma=\sigma\nabla^2G_\sigma$, a finite difference in scale gives $G_{k\sigma}(x,y)-G_\sigma(x,y)\approx(k-1)\,\sigma^2\,\nabla^2G_\sigma(x,y)$. A ratio $k\approx1.6$ resembles the centre-surround response of the retina, and the same construction is used by SIFT to find scale-space extrema.",
  hint="Why subtract two blurs instead of building a Laplacian kernel?",
  breakdown=[r"<strong>$G_{k\sigma}-G_\sigma$ = two blurs and a subtraction.</strong> A wide blur minus a narrow blur is a difference of two bells, which has the same shape as the LoG: a negative centre and a positive ring.",
             r"<strong>$\partial G_\sigma/\partial\sigma=\sigma\nabla^2G_\sigma$ = why it works.</strong> Blurring a little more is a diffusion, and diffusion is governed by the Laplacian; a finite step in $\sigma$ approximates it.",
             r"<strong>$(k-1)\sigma^2$ = scale normalisation for free.</strong> $\sigma^2\nabla^2G_\sigma$ is the scale-normalised LoG, so with a fixed $k$ the DoG can be compared across scales directly. A bare $\nabla^2G_\sigma$ shrinks as $\sigma$ grows and makes small scales look artificially strong."],
  conn=r"<strong>Cheap outline of the shop front.</strong> The camera already has blurred copies of the frame at several widths; subtracting two neighbouring copies gives the edge map at no extra cost.",
  cap="A narrow blur Gσ (solid) and a wider blur Gkσ (dashed) are subtracted; the result (right) has the LoG shape, a negative centre with a positive ring: Gkσ − Gσ ≈ (k−1)σ²∇²Gσ."),
3135: dict(d=d3135, stmtKind="ALGORITHM",
  statement=r"<b>Canny edge detector.</b> Designed for good detection, good localization and a single response per edge: (1) smooth with a Gaussian; (2) compute the gradient magnitude $M$ and direction $\theta$; (3) non-maximum suppression: quantize $\theta$ to $0^\circ,45^\circ,90^\circ,135^\circ$ and keep $(x,y)$ only if $M(x,y)$ is at least its two neighbours along $\theta$; (4) hysteresis thresholding with $T_{\rm high}\approx2$–$3\,T_{\rm low}$: pixels $\ge T_{\rm high}$ are edges, pixels in $[T_{\rm low},T_{\rm high})$ are kept only if 8-connected to an edge.",
  hint="After the gradient, how do you thin a thick edge to one pixel and keep it unbroken?",
  breakdown=[r"<strong>Blur, then $M,\theta$.</strong> The Gaussian removes speckle, and the gradient gives each pixel an edge strength and a direction.",
             r"<strong>$M(x,y)\ge M(n_+),M(n_-)$ along $\theta$ = thinning.</strong> Compare with the two neighbours across the edge (along the gradient) and keep only the peak, so each edge is one pixel wide.",
             r"<strong>$T_{\rm high},T_{\rm low}$ = hysteresis.</strong> Strong pixels are seeds; weak ones survive only when they connect to a seed, giving continuous contours with no isolated speckle.",
             r"<strong>$\theta\bmod180^\circ$ to the nearest of $0,45,90,135$ picks the two neighbours.</strong> $0^\circ$ compares left and right, $90^\circ$ above and below, and $45^\circ,135^\circ$ a diagonal pair; for example $93^\circ\to90^\circ$.",
             r"<strong>Canny is nonlinear; raising either threshold breaks edges.</strong> Suppression and thresholding are not linear filters. A higher $T_{\rm high}$ leaves fewer seeds, and a higher $T_{\rm low}$ leaves fewer weak pixels to link them."],
  conn=r"<strong>A clean outline of the shop front, not a smear.</strong> The raw gradient lights up a thick band along the wall; Canny reduces it to a single thin line, and keeps the faint stretch where the wall is in shadow because it is joined to a strong stretch.",
  cap="Canny's four stages: blur, gradient (M, θ), non-maximum suppression (keep only the peak across the edge), and hysteresis with thresholds Thigh ≈ 2–3 Tlow."),
3136: dict(d=d3136, stmtKind="WORKED EXAMPLE",
  statement=r"<b>Example.</b> Gradient magnitudes along an edge are $20,45,95,40,25,60,28$ with $T_{\rm high}=90$ and $T_{\rm low}=30$. Only $95\ge T_{\rm high}$ is a strong seed. Its neighbours $45$ and $40$ are $\ge T_{\rm low}$ and connected to it, so they are kept: edges $=\{45,95,40\}$. The $60$ is above $T_{\rm low}$ but is separated from the chain by $25\lt T_{\rm low}$, so it is dropped; $20,25,28$ are below $T_{\rm low}$.",
  hint="Which of the two medium-strength pixels, 45 or 60, survives hysteresis, and why?",
  breakdown=[r"<strong>$95\ge T_{\rm high}=90$ = the seed.</strong> The only pixel strong enough to be an edge on its own."],
  conn=r"<strong>One bright stretch and a lone smudge.</strong> The shop's outline has a strong middle and faded ends; the faded ends stay because they touch the strong part. A lone grey smudge farther along has no such link and is rejected.",
  cap="Magnitudes 20, 45, 95, 40, 25, 60, 28 against Thigh = 90 and Tlow = 30. The strong 95 pulls in 45 and 40; 60 is cut off by 25 and is dropped."),
}
CARDS[3136]["breakdown"] += [r"<strong>$45,40\ge T_{\rm low}=30$ and touching 95 = grown into the edge.</strong> They are weak on their own but joined to the seed, so they belong to the same edge.",
                             r"<strong>$60\notin$ edges = no path to a strong pixel.</strong> A single threshold at 30 would keep the isolated 60 (speckle); one at 90 would keep only 95 (a broken edge). Hysteresis avoids both.",
                             r"<strong>Linking grows through weak pixels.</strong> A weak pixel joined to a kept weak pixel is kept too, so one seed can pull in a whole 8-connected chain."]

STORY = {
 3131: dict(s="STORY 6 · STEP 1 · WHERE THINGS CHANGE", b="An edge is where brightness changes fast: the <b>gradient</b> gives its strength $M$ and its direction $\\theta$.",
   f=[["3055", "derivatives sharpen"], ["3034", "mask outlines"]], n=[["3132", "a practical kernel"]]),
 3132: dict(s="STORY 6 · STEP 2 · A STEADY DERIVATIVE", b="<b>Sobel</b> = smoothing times a difference, so noise is averaged along the edge.",
   f=[["3131", "the gradient"], ["3053", "separable kernels"]], n=[["3133", "second derivative"], ["3135", "Canny's gradient stage"]]),
 3133: dict(s="STORY 6 · STEP 3 · ZERO-CROSSINGS", b="Blur then take the Laplacian: edges are the <b>zero-crossings</b>; $\\sigma$ picks the scale.",
   f=[["3132", "first derivatives"], ["3054", "Gaussian"]], n=[["3134", "a cheaper form"]]),
 3134: dict(s="STORY 6 · STEP 4 · TWO BLURS", b="<b>DoG</b> $\\approx$ LoG: subtract two Gaussian blurs.",
   f=[["3133", "LoG"]], n=[["3135", "Canny"], ["3161", "SIFT's scale space"]]),
 3135: dict(s="STORY 6 · STEP 5 · THE FULL DETECTOR", b="<b>Canny</b>: blur, gradient, thin by non-maximum suppression, link by hysteresis.",
   f=[["3132", "gradient"], ["3134", "scale"]], n=[["3136", "hysteresis by hand"], ["3141", "lines from edge points"]]),
 3136: dict(s="STORY 6 · STEP 6 · CHECK BY HAND", b="Hysteresis keeps $45,95,40$ and drops the lone $60$.",
   f=[["3135", "Canny"]], n=[["3141", "next: turn edge points into lines"]]),
}
FIX = build_fix(CARDS)

# Fields the card builder above does not set (notation and corrections).
EXTRA = {
    3131: {"math": "$$\\nabla f=\\begin{pmatrix}\\partial f/\\partial x\\\\ \\partial f/\\partial y\\end{pmatrix},\\quad M=\\lvert\\nabla f\\rvert,\\quad \\theta=\\operatorname{atan2}\\!\\left(\\tfrac{\\partial f}{\\partial y},\\tfrac{\\partial f}{\\partial x}\\right)$$"},
    3132: {"coreTranslation": ["<strong>What:</strong> Sobel's two $3{\\times}3$ kernels estimate $f_x$ and $f_y$; $S_x$ reacts to <strong>vertical</strong> edges, $S_y$ to <strong>horizontal</strong> edges.", "<strong>How:</strong> each is a <strong>smoothing $[1,2,1]$ times a derivative $[-1,0,1]$</strong> (separable), so noise is averaged along the edge direction.", "<strong>Why:</strong> derivatives amplify high-frequency noise; this built-in smoothing makes Sobel more robust than a plain $[-1,1]$ difference. <strong>Prewitt</strong> uses $[1,1,1]$, <strong>Scharr</strong> uses $[3,10,3]$ for better rotational symmetry."], "math": "$$S_x=\\begin{pmatrix}1\\\\2\\\\1\\end{pmatrix}\\!\\begin{pmatrix}-1&0&1\\end{pmatrix},\\quad M=\\sqrt{f_x^2+f_y^2}$$", "examTrap": "Sobel kernels are CORRELATION masks as printed. Doing true convolution flips the sign of fₓ and fᵧ, which is harmless for M but flips θ by 180°."},
    3134: {"coreTranslation": ["<strong>Heat-equation fact:</strong> $\\partial G_\\sigma/\\partial\\sigma=\\sigma\\nabla^2G_\\sigma$, so a finite difference in scale approximates the Laplacian: $G_{k\\sigma}(x,y)-G_\\sigma(x,y)\\approx(k-1)\\sigma^2\\nabla^2G_\\sigma$.", "<strong>Practical gain:</strong> two Gaussian blurs and a subtraction (both separable and reusable across scales) are far cheaper than a dedicated LoG kernel.", "<strong>Link to SIFT:</strong> the same DoG construction is how SIFT finds <strong>scale-space extrema</strong>. A ratio of about $k=1.6$ resembles the retina's center-surround response."], "math": "$$G_{k\\sigma}(x,y)-G_\\sigma(x,y)\\ \\approx\\ (k-1)\\,\\sigma^2\\,\\nabla^2G_\\sigma(x,y)$$", "examTrap": "The σ² in (k−1)σ² is scale normalization, so a DoG with fixed k compares across scales directly. A bare LoG needs multiplying by σ², or small scales look artificially strong."},
    3135: {"examTrap": "NMS compares along the GRADIENT direction (across the edge), not along the edge. And a chain of weak pixels with no strong pixel in it is DROPPED."},
    3136: {"examTrap": "A single threshold at 30 would keep the isolated 60 (speckle); at 90 it would keep only 95 (broken edge). Hysteresis avoids both."},
}
for _cid, _fields in EXTRA.items():
    FIX[_cid].update(_fields)
