import math
from dip_lib import *

CARDS = []

def _poly(pts, w=1.8, dash=None, fill="none"):
    d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    return P(d, fill=fill, w=w, dash=dash)

def BOX(x, y, w, h, label, fill="#f1f5f9", sz=9, bold=True):
    fw = "bold" if bold else "normal"
    cap = max(4, int(w / (sz * 0.52)))
    if len(label) > cap and " " in label:
        words = label.split(" "); best = None
        for i in range(1, len(words)):
            a, b = " ".join(words[:i]), " ".join(words[i:])
            score = max(len(a), len(b))
            if best is None or score < best[0]: best = (score, a, b)
        _, a, b = best
        return (R(x, y, w, h, fill, 1.6) + N(x + w / 2, y + h / 2 - 1, a, sz, w=fw) + N(x + w / 2, y + h / 2 + sz, b, sz, w=fw))
    return R(x, y, w, h, fill, 1.6) + N(x + w / 2, y + h / 2 + 3, label, sz, w=fw)

# ============================ 14 · EDGE DETECTION ============================
CARDS.append(card(14, 1, "EDGE DETECTION", "Image Gradient: Magnitude and Direction",
    [PG("20,20 150,20 20,126", "#d9dee7", 1.2), PG("150,20 226,20 226,126 20,126", "#ffffff", 1.2),
     L(150, 20, 20, 126, 2.6), L(92, 70, 130, 38, 2, ar=True),
     N(110, 36, "∇f ⟂ edge", 9, "start", "bold"), N(44, 44, "dark", 9), N(176, 100, "bright", 9),
     N(176, 54, "M = ‖∇f‖", 9, "start", "bold"), N(176, 68, "θ = atan2(fᵧ, fₓ)", 8.5, "start")],
    "The gradient points across the edge toward brighter pixels; the edge itself runs perpendicular to it",
    ["<strong>What:</strong> The gradient $\\nabla f=(f_x,f_y)$ points in the direction of <strong>steepest increase</strong>; its length is the <strong>edge strength</strong>.",
     r"<strong>How:</strong> magnitude $M=\sqrt{f_x^2+f_y^2}$ (often approximated by $|f_x|+|f_y|$), direction $\theta=\operatorname{atan2}(f_y,f_x)$, <strong>perpendicular to the edge</strong>.",
     "<strong>Why:</strong> an edge is where intensity changes fast, so large $M$ marks edge pixels; $\\theta$ tells later stages (like NMS) which way to look."],
    r"$$\nabla f=\begin{pmatrix}\partial f/\partial x\\ \partial f/\partial y\end{pmatrix},\quad M=\|\nabla f\|_2,\quad \theta=\operatorname{atan2}\!\left(\tfrac{\partial f}{\partial y},\tfrac{\partial f}{\partial x}\right)$$",
    "Water running down a hillside: the gradient is the downhill-reversed arrow (steepest uphill), and the contour line (the edge) runs sideways to it.",
    "The edge direction is perpendicular to the gradient, not along it. Mixing them up flips every orientation by 90°."))

CARDS.append(card(14, 2, "EDGE DETECTION", "Sobel Kernels and Noise",
    [N(14, 20, "Gₓ", 10, "start", w="bold"), GRID(14, 28, [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], cell=22, sz=10),
     N(100, 20, "Gᵧ", 10, "start", w="bold"), GRID(100, 28, [[1, 2, 1], [0, 0, 0], [-1, -2, -1]], cell=22, sz=10),
     N(196, 44, "= smooth ×", 8.5), N(196, 56, "difference", 8.5), N(196, 78, "[1 2 1]ᵀ ⊗ [−1 0 1]", 8), N(196, 98, "less noisy", 8.5, w="bold"), N(196, 110, "than [−1 1]", 8.5),
     N(58, 118, "vertical edges", 8.5), N(144, 118, "horizontal edges", 8.5)],
    "Each Sobel kernel averages along the edge (the 1-2-1 column) while differencing across it",
    ["<strong>What:</strong> Sobel's two $3{\\times}3$ kernels estimate $f_x$ and $f_y$; $G_x$ reacts to <strong>vertical</strong> edges, $G_y$ to <strong>horizontal</strong> edges.",
     "<strong>How:</strong> each is a <strong>smoothing $[1,2,1]$ times a derivative $[-1,0,1]$</strong> (separable), so noise is averaged along the edge direction.",
     "<strong>Why:</strong> derivatives amplify high-frequency noise; this built-in smoothing makes Sobel more robust than a plain $[-1,1]$ difference. <strong>Prewitt</strong> uses $[1,1,1]$, <strong>Scharr</strong> uses $[3,10,3]$ for better rotational symmetry."],
    r"$$G_x=\begin{pmatrix}1\\2\\1\end{pmatrix}\!\begin{pmatrix}-1&0&1\end{pmatrix},\quad M=\sqrt{(f\ast G_x)^2+(f\ast G_y)^2}$$",
    "Measuring a slope with a wide ruler instead of one pin: the ruler averages out small bumps (noise) before reading the tilt.",
    "Sobel kernels are CORRELATION masks as printed. Doing true convolution flips the sign of Gₓ and G_y, which is harmless for M but flips θ by 180°."))

def _sig(x, c, s): return 1 / (1 + math.exp(-(x - c) / s))

def _fff():
    f = [(x, 38 - 28 * _sig(x, 120, 5)) for x in range(20, 225, 3)]
    d = [(x, 80 - 30 * math.exp(-((x - 120) ** 2) / (2 * 7 ** 2)) * 1.0) for x in range(20, 225, 3)]
    s2 = [(x, 124 + 22 * (-(x - 120) / 7) * math.exp(-((x - 120) ** 2) / (2 * 7 ** 2)) * 1.65 * 1) for x in range(20, 225, 3)]
    return [L(20, 38, 224, 38, 0.6, d="1 4"), _poly(f, 2), N(26, 14, "f", 9, "start", "bold"),
            L(20, 80, 224, 80, 0.6, d="1 4"), _poly(d, 2), N(26, 56, "f′ (peak at edge)", 8.5, "start", "bold"),
            L(20, 124, 224, 124, 0.6, d="1 4"), _poly(s2, 2), N(26, 100, "f″ (zero-crossing at edge)", 8.5, "start", "bold"),
            L(120, 8, 120, 142, 1, d="3 3"), C(120, 124, 3.5, "#ffffff")]

CARDS.append(card(14, 3, "EDGE DETECTION", "Laplacian of Gaussian & Zero-Crossings",
    _fff(),
    "The edge sits at the peak of f′, which is exactly the zero-crossing of f″",
    ["<strong>Idea:</strong> an edge is a maximum of $|f'|$ or, equivalently, a <strong>zero-crossing of the second derivative</strong> $f''$ (Laplacian in 2D).",
     r"<strong>Marr–Hildreth:</strong> smooth first (derivatives are noisy), then take the Laplacian: <strong>$\nabla^2G_\sigma$</strong> (LoG), and mark zero-crossings. Because the operators are linear, you can do it in one step with the LoG kernel.",
     "<strong>Scale knob:</strong> $\\sigma$ sets which edges survive (bigger = only coarse edges). Zero-crossings always form <strong>closed contours</strong>, but they also fire on flat noise-driven wiggles."],
    r"$$\nabla^2G_\sigma(x,y)=\frac{1}{\pi\sigma^4}\left(\frac{x^2+y^2}{2\sigma^2}-1\right)e^{-\frac{x^2+y^2}{2\sigma^2}}$$",
    "Rolling a ball over a ramp: the point where the curvature flips from 'bending up' to 'bending down' is exactly where the slope is steepest.",
    "Zero-crossings need a strict sign change across neighbors, and some are weak. Always add a slope or magnitude test to drop false edges."))

def _log_dog():
    log = []; dog = []
    k = 1.6
    g = lambda x, s: math.exp(-x * x / (2 * s * s)) / s
    d0 = abs(g(0, k) - g(0, 1))
    for x10 in range(-45, 46, 2):
        x = x10 / 10.0
        v1 = -((x * x - 1) * math.exp(-x * x / 2))      # negated LoG
        v2 = -(g(x, k) - g(x, 1)) / d0                    # negated DoG, same center height
        log.append((120 + x * 24, 80 - 40 * v1))
        dog.append((120 + x * 24, 80 - 40 * v2))
    return [L(14, 80, 226, 80, 0.8, d="2 3"), _poly(log, 2.2), _poly(dog, 1.6, "5 3"),
            N(36, 20, "LoG (solid)", 9, "start", "bold"), N(36, 33, "DoG (dashed)", 9, "start"),
            N(190, 26, "G(kσ) − G(σ)", 8.5), N(190, 38, "≈ (k−1)σ² ∇²G", 8.5, w="bold"), N(120, 138, "k ≈ 1.6 matches closely", 8.5)]

CARDS.append(card(14, 4, "EDGE DETECTION", "DoG ≈ LoG",
    _log_dog(),
    "A difference of two Gaussians traces the same 'Mexican hat' as the Laplacian of Gaussian",
    ["<strong>Heat-equation fact:</strong> $\\partial G/\\partial\\sigma=\\sigma\\nabla^2G$, so a finite difference in scale approximates the Laplacian: $G(x,y;k\\sigma)-G(x,y;\\sigma)\\approx(k-1)\\sigma^2\\nabla^2G$.",
     "<strong>Practical gain:</strong> two Gaussian blurs and a subtraction (both separable and reusable across scales) are far cheaper than a dedicated LoG kernel.",
     "<strong>Link to SIFT:</strong> the same DoG construction is how SIFT finds <strong>scale-space extrema</strong>. A ratio of about $k=1.6$ resembles the retina's center-surround response."],
    r"$$G(x,y;k\sigma)-G(x,y;\sigma)\ \approx\ (k-1)\,\sigma^2\,\nabla^2G(x,y;\sigma)$$",
    "Subtracting a blurry photo from a less blurry one to leave only the detail in between: a band-pass made from two low-passes.",
    "The (k−1)σ² factor matters for comparing across scales (scale normalization). Forgetting it makes small-scale responses look artificially strong."))

CARDS.append(card(14, 5, "CANNY DETECTOR", "Canny: Four Stages",
    [BOX(6, 14, 50, 36, "1. Gaussian smooth", "#f1f5f9", 7.5), BOX(64, 14, 50, 36, "2. gradient M, θ", "#f1f5f9", 7.5),
     BOX(122, 14, 50, 36, "3. non-max suppr.", "#f1f5f9", 7.5), BOX(180, 14, 54, 36, "4. hysteresis T_low/T_high", "#f1f5f9", 7),
     L(56, 32, 62, 32, 1.4, ar=True), L(114, 32, 120, 32, 1.4, ar=True), L(172, 32, 178, 32, 1.4, ar=True),
     N(31, 66, "kills noise", 8), N(89, 66, "strength + dir", 8), N(147, 66, "thin to 1 px", 8), N(207, 66, "link strong+weak", 8),
     N(120, 94, "Good detection · Good localization · Single response", 9, w="bold"),
     N(120, 112, "T_high ≈ 2–3 × T_low", 9), N(120, 128, "NMS: keep M only if it beats both neighbors along θ", 8.5)],
    "Smooth, differentiate, thin to single-pixel ridges, then link edges with two thresholds",
    ["<strong>Canny's three criteria:</strong> <strong>good detection</strong> (few misses and false alarms), <strong>good localization</strong> (edge near the true one), <strong>single response</strong> (one hit per edge).",
     "<strong>Pipeline:</strong> (1) Gaussian blur, (2) gradient $M,\\theta$, (3) <strong>non-maximum suppression</strong>: quantize $\\theta$ into 4 sectors (0°, 45°, 90°, 135°) and keep a pixel only if $M$ beats its two neighbors along $\\theta$.",
     "(4) <strong>Hysteresis</strong>: pixels $\\ge T_{\\text{high}}$ are strong seeds; pixels in $[T_{\\text{low}},T_{\\text{high}})$ are kept <strong>only if 8-connected to a strong edge</strong>, giving continuous contours without speckle."],
    r"$$\text{keep } (x,y)\iff M(x,y)\ge M(\text{n}_{+},\text{n}_{-})\ \text{along }\theta;\qquad T_{\text{high}}\approx2\text{–}3\,T_{\text{low}}$$",
    "A road-mapper who first traces only the main highways (strong), then adds side streets only if they link to a highway (weak, connected).",
    "NMS compares along the GRADIENT direction (across the edge), not along the edge. And a weak pixel connected only to other weak pixels is DROPPED."))

_mag = [20, 45, 95, 40, 25, 60, 28]
_keep = [False, True, True, True, False, False, False]
CARDS.append(card(14, 6, "WORKED BENCHMARK", "Worked Benchmark: Hysteresis on a 1-D Edge Profile",
    [L(18, 120, 226, 120, 1.2)] +
    [R(26 + i * 28, 120 - m * 0.9, 22, m * 0.9, "#d9dee7" if _keep[i] else "#ffffff", 1.4, 0, None if _keep[i] else "3 2") for i, m in enumerate(_mag)] +
    [N(37 + i * 28, 120 - m * 0.9 - 4, str(m), 8.5) for i, m in enumerate(_mag)] +
    [L(18, 120 - 90 * 0.9, 226, 120 - 90 * 0.9, 1, d="5 3"), N(20, 120 - 90 * 0.9 - 3, "T_high = 90", 8, "start"),
     L(18, 120 - 30 * 0.9, 226, 120 - 30 * 0.9, 1, d="5 3"), N(20, 120 - 30 * 0.9 - 3, "T_low = 30", 8, "start"),
     N(120, 138, "kept: 45, 95, 40   dropped: 20, 25, 60, 28", 8.5, w="bold")],
    "95 seeds the chain; 45 and 40 join it. The 60 is strong enough to pass T_low but isolated, so it is dropped",
    ["<strong>Magnitudes along an edge:</strong> 20, 45, <strong>95</strong>, 40, 25, 60, 28 with $T_{\\text{high}}=90$, $T_{\\text{low}}=30$.",
     "<strong>Seed:</strong> only 95 ≥ 90 is strong. <strong>Grow:</strong> neighbors 45 and 40 are ≥ 30 and touch the seed, so both are kept; 25 and 20 are below $T_{\\text{low}}$.",
     "<strong>Rejected:</strong> 60 is above $T_{\\text{low}}$ but separated from the chain by 25 (below $T_{\\text{low}}$), so it is not connected to any strong pixel and is <strong>dropped</strong> as noise."],
    r"$$\text{edges}=\{95\}\cup\{45,40\},\qquad 60\notin\text{edges}\ (\text{no path to a strong pixel})$$",
    "A rumor only counts if it can be traced back to a reliable source through a chain of semi-reliable ones; a lone semi-reliable rumor is ignored.",
    "A single threshold at 30 would keep the isolated 60 and 28 (speckle); at 90 it would keep only 95 (broken edge). Hysteresis avoids both."))

# ============================ 15 · HOUGH ============================
CARDS.append(card(15, 1, "HOUGH TRANSFORM", "Line in Normal Form: ρ = x cosθ + y sinθ",
    [AX(26, 124, 224, 12), L(26, 124, 200, 40, 2.2), L(26, 124, 108, 84, 1.4, d="4 3"),
     L(108, 84, 118, 80, 1.1), N(78, 96, "ρ", 10, "end", "bold"), P("M52 124 A26 26 0 0 0 48 112", w=1.2), N(58, 108, "θ", 10, "start"),
     N(212, 22, "y", 9), N(222, 134, "x", 9), N(176, 52, "line", 9, "start"),
     N(150, 126, "ρ = x cosθ + y sinθ", 9, "start", "bold"), N(150, 140, "θ ∈ [0, π), ρ ∈ ℝ", 8.5, "start")],
    "The line is described by its perpendicular distance ρ from the origin and the angle θ of that perpendicular",
    ["<strong>Why not $y=mx+b$:</strong> slope blows up for vertical lines. Use the <strong>normal form</strong> instead: a line is the set of points whose projection on the unit vector $(\\cos\\theta,\\sin\\theta)$ equals $\\rho$.",
     "<strong>Parameter space:</strong> every line is one point $(\\rho,\\theta)$ and every line is representable, with $\\theta\\in[0,\\pi)$ and $\\rho\\in\\mathbb{R}$ (or $\\theta\\in[0,2\\pi)$ with $\\rho\\ge0$).",
     "<strong>Duality:</strong> one image point $(x_0,y_0)$ lies on <strong>many lines</strong>, which trace a sinusoid $\\rho(\\theta)=x_0\\cos\\theta+y_0\\sin\\theta$ in parameter space."],
    r"$$\rho=x\cos\theta+y\sin\theta,\qquad \theta\in[0,\pi),\ \rho\in[-D,D],\ D=\sqrt{W^2+H^2}$$",
    "Giving directions to a straight road by 'the shortest path from the town center hits it at distance ρ, heading θ' instead of its slope.",
    "θ and ρ conventions differ (θ from the x-axis vs from the normal, sign of ρ). Check the range and sign before comparing answers."))

def _sinus():
    pts = [(1, 1), (2, 2), (3, 3)]
    curves = []
    for (x0, y0), d in zip(pts, [None, "6 3", "2 2"]):
        cs = [(24 + t / 180.0 * 190, 72 - (x0 * math.cos(math.radians(t)) + y0 * math.sin(math.radians(t))) * 14) for t in range(0, 181, 3)]
        curves.append(_poly(cs, 1.8, d))
    return [L(24, 72, 216, 72, 1, d="2 3"), L(24, 14, 24, 130, 1.2, ar=True)] + curves + [
        C(24 + 135 / 180.0 * 190, 72, 4.5), N(24 + 135 / 180.0 * 190, 92, "(135°, 0)", 8.5, w="bold"),
        N(30, 104, "one sinusoid per point", 8.5, "start"), N(30, 116, "common crossing = line", 8.5, "start", "bold"),
        N(120, 142, "θ (0° → 180°)", 8.5), N(14, 20, "ρ", 9)]

CARDS.append(card(15, 2, "HOUGH TRANSFORM", "Voting in the Accumulator",
    _sinus(),
    "Collinear points give sinusoids that all cross at the same (ρ, θ), the parameters of their line",
    ["<strong>What:</strong> every edge pixel $(x_i,y_i)$ <strong>votes</strong> for all lines passing through it, i.e. it increments every cell on its sinusoid in a 2D <strong>accumulator</strong> $A[\\rho,\\theta]$.",
     "<strong>How:</strong> points that lie on one line produce sinusoids that <strong>intersect at one cell</strong>, so that cell gets many votes while chance cells get few.",
     "<strong>Why:</strong> detecting a line becomes finding <strong>peaks</strong> in $A$, which is robust to gaps and noise because it needs no pixel connectivity."],
    r"$$A[\rho,\theta]\mathrel{+}=1\ \ \text{for each edge point and each }\theta:\ \ \rho=x_i\cos\theta+y_i\sin\theta$$",
    "A show of hands: each person (edge point) votes for every club (line) they could belong to, and the club with the most hands wins.",
    "Bin size matters: too fine and noisy points spread votes over neighboring cells, too coarse and you merge distinct lines."))

CARDS.append(card(15, 3, "HOUGH TRANSFORM", "The Hough Line Algorithm (Step by Step)",
    [BOX(6, 14, 52, 38, "edge map (Canny)", "#f1f5f9", 8), BOX(70, 14, 52, 38, "for each edge px, each θ", "#f1f5f9", 7.5),
     BOX(134, 14, 46, 38, "ρ = x cosθ+y sinθ", "#f1f5f9", 7.5), BOX(190, 14, 44, 38, "A[ρ,θ] += 1", "#f1f5f9", 8),
     L(58, 33, 68, 33, 1.4, ar=True), L(122, 33, 132, 33, 1.4, ar=True), L(180, 33, 188, 33, 1.4, ar=True),
     L(212, 52, 212, 74, 1.4, ar=True), BOX(150, 76, 84, 30, "threshold + NMS on A", "#ffffff", 8.5),
     L(150, 91, 128, 91, 1.4, ar=True), BOX(40, 76, 88, 30, "peaks → lines (ρ,θ)", "#e2e8f0", 8.5),
     N(120, 128, "cost ≈ (#edge px) × (#θ bins)", 9, w="bold")],
    "Edge map in, vote for every θ, then pick local maxima of the accumulator",
    ["<strong>1.</strong> Detect edges (Canny). <strong>2.</strong> For every edge pixel and every discrete $\\theta$, compute $\\rho$ and <strong>increment</strong> $A[\\rho,\\theta]$.",
     "<strong>3.</strong> Smooth/threshold $A$ and keep <strong>local maxima</strong> above a vote threshold. <strong>4.</strong> Convert each peak back to a line; optionally clip to the segment actually supported by edge pixels.",
     "<strong>Speed-up:</strong> use the <strong>gradient direction</strong> $\\theta=\\operatorname{atan2}(f_y,f_x)$ to vote for only one (or a few) $\\theta$ per pixel, cutting the cost by the number of θ bins."],
    r"$$\text{lines}=\{(\rho,\theta):\ A[\rho,\theta]\ge\tau\ \text{and local max}\}$$",
    "Counting the best-attended stalls at a fair: you only need the few highest-traffic spots, not every footprint.",
    "The Hough peak gives an infinite line, not a segment. Two collinear but distant segments vote into the SAME cell and are merged."))

def _circ():
    out = [C(110, 74, 34, "#ffffff", 2), C(110, 74, 2.5)]
    angs = [20, 110, 200, 290]
    for a in angs:
        x = 110 + 34 * math.cos(math.radians(a)); y = 74 - 34 * math.sin(math.radians(a))
        out += [C(x, y, 3), C(x, y, 34, "none", 1.1)]
    return out + [N(110, 134, "all radius-r circles meet at the center", 8.5, w="bold"),
                  N(204, 36, "3-D accumulator", 8.5), N(204, 48, "A[a, b, r]", 9, w="bold"), N(204, 70, "with gradient θ:", 8.5), N(204, 82, "a = x − r cosθ", 8.5), N(204, 94, "b = y − r sinθ", 8.5), N(204, 106, "→ 2-D per r", 8.5)]

CARDS.append(card(15, 4, "HOUGH TRANSFORM", "Circle Hough: (a, b, r)",
    _circ(),
    "Each boundary point votes for all centers at distance r; the true center collects every vote",
    ["<strong>Parameters:</strong> a circle $(x-a)^2+(y-b)^2=r^2$ has <strong>3 parameters</strong> $(a,b,r)$, so the naive accumulator is <strong>3-dimensional</strong>.",
     "<strong>Voting:</strong> for a fixed radius $r$, each edge point votes for a <strong>circle of candidate centers</strong> of that radius around it; points on a true circle all vote for its center.",
     "<strong>Speed-up:</strong> with the <strong>gradient direction</strong> the center lies along that direction at distance $r$: $a=x-r\\cos\\theta,\\ b=y-r\\sin\\theta$, so each point votes for <strong>one cell per $r$</strong> instead of a whole circle."],
    r"$$(x-a)^2+(y-b)^2=r^2,\qquad a=x-r\cos\theta,\quad b=y-r\sin\theta$$",
    "Standing on the rim of a round pond and dropping a 'string of length r' toward the middle: all strings meet at the pond's center.",
    "Memory is O(W·H·R) for the 3D accumulator. Searching an unknown radius range is the cost driver, so restrict r to a plausible range."))

def _rtab():
    out = [PG("40,100 70,40 120,28 170,50 176,100", "#f1f5f9", 1.8), C(108, 76, 4), N(108, 92, "c", 9, "middle", "bold")]
    for (x, y) in [(70, 40), (120, 28), (170, 50), (176, 100), (40, 100)]:
        out += [L(x, y, 108, 76, 1.2, d="4 3", ar=True), C(x, y, 2.6)]
    out += [N(210, 30, "R-table", 9, "middle", "bold"), N(210, 44, "index: φ", 8.5), N(210, 56, "(edge orientation)", 8),
            N(210, 74, "entries: r vectors", 8.5), N(210, 86, "to the reference", 8.5), N(210, 98, "point c", 8.5),
            N(120, 132, "vote c = p + r(φ) for every r stored under φ(p)", 8.5, w="bold")]
    return out

CARDS.append(card(15, 5, "HOUGH TRANSFORM", "Generalized Hough Transform (R-Table)",
    _rtab(),
    "Every boundary point stores the vector to a reference point, indexed by its edge orientation",
    ["<strong>Offline (train):</strong> pick a reference point $c$. For each boundary point $p$ with orientation $\\phi$, store the vector $r=c-p$ in a table indexed by $\\phi$: the <strong>R-table</strong>.",
     "<strong>Online (detect):</strong> for every edge pixel with orientation $\\phi$, look up all vectors $r$ stored under $\\phi$ and <strong>vote for $c=p+r$</strong>.",
     "<strong>Why:</strong> it finds <strong>arbitrary shapes</strong> with no analytic equation; the peak in the accumulator is the shape's reference location (add axes for scale and rotation)."],
    r"$$c=p+r(\phi),\qquad A[c]\mathrel{+}=1\ \ \forall\, r\in R\text{-table}[\phi(p)]$$",
    "A treasure map by landmarks: each landmark remembers 'the treasure is this far in that direction', and the spot named by many landmarks wins.",
    "Handling scale and rotation adds dimensions to the accumulator (4D for position+scale+rotation). Cost explodes if you vote naively."))

CARDS.append(card(15, 6, "WORKED BENCHMARK", "Worked Benchmark: Points (1,1), (2,2), (3,3)",
    [N(60, 20, "θ = 0°", 9, w="bold"), L(24, 64, 100, 64, 1.1)] +
    [L(40 + 20 * i, 64, 40 + 20 * i, 64 - r * 12, 2.4) for i, r in enumerate([1, 2, 3])] + [N(40 + 20 * i, 78, f"ρ={r}", 8) for i, r in enumerate([1, 2, 3])] +
    [N(60, 100, "three different cells", 8.5), N(60, 112, "→ 3 votes of 1", 8.5),
     N(180, 20, "θ = 135°", 9, w="bold"), L(130, 64, 226, 64, 1.1)] +
    [L(180, 64, 180, 64 - 36, 2.8), N(180, 78, "ρ = 0", 8.5, w="bold"), N(180, 100, "ONE cell", 8.5), N(180, 112, "→ 3 votes", 8.5, w="bold"),
     N(120, 134, "line y = x  ⇔  (ρ, θ) = (0, 135°)", 9, w="bold")],
    "At θ = 135° every point gives ρ = 0, so all three votes land in the same cell",
    ["<strong>Formula:</strong> $\\rho=x\\cos\\theta+y\\sin\\theta$. At $\\theta=0^\\circ$: $\\rho=1,2,3$, so the three points vote for <strong>three different cells</strong> (no agreement).",
     "At $\\theta=135^\\circ$: $\\cos\\theta=-\\tfrac{\\sqrt2}{2},\\ \\sin\\theta=\\tfrac{\\sqrt2}{2}$, so $\\rho=\\tfrac{\\sqrt2}{2}(y-x)=0$ for <strong>all three points</strong>: one cell receives <strong>3 votes</strong>.",
     "Decode: the line is $x\\cos135^\\circ+y\\sin135^\\circ=0$, i.e. <strong>$y=x$</strong>, passing through the origin (distance $\\rho=0$) with its normal pointing at 135°."],
    r"$$\rho(135^\circ)=(1,1)\!\cdot\!\left(-\tfrac{\sqrt2}{2},\tfrac{\sqrt2}{2}\right)=0=\rho_{(2,2)}=\rho_{(3,3)}$$",
    "Three people all saying 'we live exactly at distance zero from the origin along this one heading': their stories agree in exactly one cell.",
    "The same line is also (ρ, θ) = (0, 135°) vs (0, 315°) with opposite signs of ρ in other conventions. Fix the convention before decoding."))

# ============================ 16 · HARRIS ============================
def _three():
    out = []
    for i, (lab, kind) in enumerate([("flat", 0), ("edge", 1), ("corner", 2)]):
        x0 = 8 + i * 78
        out.append(R(x0, 20, 66, 66, "#ffffff", 1.6))
        if kind == 1:
            out.append(PG(f"{x0},20 {x0+66},20 {x0+66},50 {x0},50", "#d9dee7", 0))
        if kind == 2:
            out.append(PG(f"{x0+30},50 {x0+66},50 {x0+66},86 {x0+30},86", "#d9dee7", 0))
        out.append(R(x0 + 18, 38, 30, 30, "none", 2, 0, "4 3"))
        out.append(N(x0 + 33, 102, lab, 9.5, w="bold"))
        if kind == 0: out.append(N(x0 + 33, 116, "no change", 8)); out.append(N(x0 + 33, 128, "anywhere", 8))
        if kind == 1: out.append(N(x0 + 33, 116, "changes ⟂ edge", 8)); out.append(N(x0 + 33, 128, "only", 8))
        if kind == 2: out.append(N(x0 + 33, 116, "changes in", 8)); out.append(N(x0 + 33, 128, "ALL directions", 8))
    return out

CARDS.append(card(16, 1, "CORNER DETECTION", "Flat, Edge, Corner: Shift a Window",
    _three(),
    "A corner is the only case where shifting the window in any direction changes it",
    ["<strong>Idea:</strong> slide a small window by $(u,v)$ and measure the change $E(u,v)=\\sum w(x,y)[I(x+u,y+v)-I(x,y)]^2$.",
     "<strong>Flat region:</strong> $E\\approx0$ for every shift. <strong>Edge:</strong> $E$ is large across the edge but <strong>≈ 0 along it</strong> (aperture problem). <strong>Corner:</strong> $E$ is large for <strong>every</strong> direction.",
     "<strong>Why corners:</strong> they are the only <strong>localizable</strong> points, which is why they work as anchors for matching and tracking."],
    r"$$E(u,v)=\sum_{x,y}w(x,y)\,\big[I(x+u,y+v)-I(x,y)\big]^2$$",
    "Wiggling a magnifying glass over a map: on blank paper nothing changes, along a road it changes only sideways, at a crossroads it changes whichever way you wiggle.",
    "The aperture problem: along an edge you cannot tell how far you slid. So edges are poor tracking points, corners are good."))

CARDS.append(card(16, 2, "CORNER DETECTION", "Structure Tensor M and Its Ellipse",
    [L(120, 72, 120, 12, 0.8, d="2 3"), L(24, 72, 216, 72, 0.8, d="2 3"),
     E(120, 72, 70, 26, -25, "#f1f5f9", 2), L(120, 72, 182, 46, 1.6, ar=True), L(120, 72, 108, 96, 1.6, ar=True),
     N(188, 40, "λ_max^(−½)", 8.5, "start"), N(100, 112, "λ_min^(−½)", 8.5, "end"),
     N(120, 134, "[u v] M [u v]ᵀ = const", 9, w="bold"), N(40, 28, "ellipse", 9, "start"), N(40, 40, "axes ∝ 1/√λ", 8.5, "start")],
    "Directions with large eigenvalue change fast (short ellipse axis); small eigenvalue = slow change",
    [r"Taylor-expanding gives $E(u,v)\approx[u\ v]\,M\,[u\ v]^T$ with the <strong>structure tensor</strong> $M=\sum w\begin{pmatrix}I_x^2&I_xI_y\\ I_xI_y&I_y^2\end{pmatrix}$.",
     r"Its eigenvalues $\lambda_1,\lambda_2$ measure the change along the two principal directions; the <strong>level set $E=$ const is an ellipse</strong> whose axes are $\propto1/\sqrt{\lambda}$.",
     "<strong>Classification:</strong> both $\\lambda$ small = flat; one large, one small = edge; <strong>both large = corner</strong>."],
    r"$$M=\sum_{x,y}w(x,y)\begin{pmatrix}I_x^2&I_xI_y\\I_xI_y&I_y^2\end{pmatrix},\qquad E(u,v)\approx\begin{pmatrix}u&v\end{pmatrix}M\begin{pmatrix}u\\v\end{pmatrix}$$",
    "The covariance of gradients: it asks 'in which directions do the gradient arrows point?' and the answer's spread tells you edge or corner.",
    "M is built from gradient products summed over the window, so it uses the window w, not a single pixel. A single pixel's M has rank 1 (always an 'edge')."))

CARDS.append(card(16, 3, "CORNER DETECTION", "Harris Response R = det M − k·trace²M",
    [L(24, 126, 224, 126, 1.2, ar=True), L(24, 126, 24, 12, 1.2, ar=True), N(222, 138, "λ₁", 9), N(14, 18, "λ₂", 9),
     PG("100,126 224,126 224,26 100,60", "#e2e8f0", 0),
     P("M90 126 Q96 74 150 68 Q210 62 224 34", w=2), L(24, 126, 224, 26, 1, d="3 3"),
     N(176, 88, "corner", 10, "middle", "bold"), N(176, 100, "R > 0 large", 8.5), N(52, 44, "edge", 10, "middle", "bold"), N(52, 56, "R < 0", 8.5),
     N(54, 110, "flat", 10, "middle", "bold"), N(54, 122, "|R| small", 8.5)],
    "In the (λ₁, λ₂) plane the Harris response splits the space into flat, edge and corner regions",
    ["<strong>Avoid eigen-decomposition:</strong> $\\det M=\\lambda_1\\lambda_2$ and $\\operatorname{tr}M=\\lambda_1+\\lambda_2$, so $R=\\lambda_1\\lambda_2-k(\\lambda_1+\\lambda_2)^2$ with $k\\approx0.04$–$0.06$.",
     "<strong>Reading $R$:</strong> $R\\gg0$ corner (both large); $R<0$ edge (one large, one tiny); $|R|\\approx0$ flat.",
     "<strong>Shi–Tomasi</strong> instead uses $\\min(\\lambda_1,\\lambda_2)$ directly: simpler and often more stable, needing the smaller eigenvalue to exceed a threshold."],
    r"$$R=\det M-k\,(\operatorname{tr}M)^2=\lambda_1\lambda_2-k(\lambda_1+\lambda_2)^2$$",
    "A two-judge panel: a corner needs BOTH judges to vote 'big change'; if only one does, it's just an edge.",
    "k is a sensitivity knob: bigger k penalizes edges more but misses faint corners. There is no 'correct' k."))

CARDS.append(card(16, 4, "CORNER DETECTION", "Harris Pipeline",
    [BOX(6, 14, 50, 34, "I_x, I_y (Sobel)", "#f1f5f9", 7.5), BOX(64, 14, 52, 34, "I_x², I_xI_y, I_y²", "#f1f5f9", 7.5),
     BOX(124, 14, 50, 34, "Gaussian window → M", "#f1f5f9", 7.5), BOX(182, 14, 52, 34, "R per pixel", "#f1f5f9", 8),
     L(56, 31, 62, 31, 1.4, ar=True), L(116, 31, 122, 31, 1.4, ar=True), L(174, 31, 180, 31, 1.4, ar=True),
     L(208, 48, 208, 70, 1.4, ar=True), BOX(150, 72, 84, 30, "threshold R > τ + 3×3 NMS", "#e2e8f0", 8),
     L(150, 87, 126, 87, 1.4, ar=True), BOX(40, 72, 84, 30, "corner list (x, y)", "#ffffff", 8.5),
     N(120, 122, "products first, THEN smooth", 9, w="bold"), N(120, 136, "(smoothing gradients first would lose the tensor)", 8)],
    "Compute gradients, form the three products, window-average them into M, score with R, then suppress non-maxima",
    ["<strong>Steps:</strong> (1) gradients $I_x,I_y$; (2) products $I_x^2,\\ I_xI_y,\\ I_y^2$; (3) <strong>Gaussian-weight and sum</strong> them over a window to form $M$ at every pixel.",
     "(4) Score with $R=\\det M-k\\operatorname{tr}^2M$; (5) keep pixels with $R>\\tau$ that are <strong>local maxima</strong> in a $3\\times3$ neighborhood (NMS).",
     "<strong>Window choice:</strong> a Gaussian window (not a box) makes the response <strong>isotropic and smooth</strong>, helping rotation invariance."],
    r"$$M(x,y)=G_\sigma\ast\begin{pmatrix}I_x^2&I_xI_y\\I_xI_y&I_y^2\end{pmatrix},\qquad \text{corners}=\{R>\tau\}\ \cap\ \text{local maxima}$$",
    "A security system: cameras (gradients), then a log of motion patterns (products), averaged per zone (window), then alerts only above a threshold.",
    "Smoothing the image and then multiplying gradients is NOT the same as multiplying gradients and then smoothing. Harris smooths the PRODUCTS."))

CARDS.append(card(16, 5, "CORNER DETECTION", "Invariance: Rotation Yes, Scale No",
    [P("M20 96 L20 36 L76 36", w=3), R(20, 36, 40, 40, "none", 1.6, 0, "4 3"), N(48, 112, "small window sees", 8.5), N(48, 124, "a corner", 8.5, w="bold"),
     P("M120 20 L120 112", w=3), R(106, 56, 40, 40, "none", 1.6, 0, "4 3"), N(133, 128, "zoomed in: only", 8.5), N(133, 140, "an edge", 8.5, w="bold"),
     P("M180 100 Q180 40 230 40", w=3), R(166, 22, 56, 56, "none", 1.6, 0, "4 3"),
     N(200, 94, "rounded corner:", 8, "middle"), N(200, 106, "window must", 8), N(200, 118, "match its scale", 8)],
    "The same structure can look like a corner at one window size and an edge at another",
    ["<strong>Rotation:</strong> M's eigenvalues do not change when the image rotates, so $R$ is <strong>rotation invariant</strong>.",
     "<strong>Intensity:</strong> invariant to additive shifts $I\\to I+b$ (only derivatives matter); a gain $I\\to aI$ scales $R$ by $a^4$, so thresholds must be relative.",
     "<strong>Scale:</strong> NOT invariant. A curve that looks like a corner at one scale looks like an edge when zoomed in. This motivates <strong>scale-space detection</strong> (Harris–Laplace, SIFT)."],
    r"$$I\to I+b:\ R\text{ unchanged};\quad I\to aI:\ R\to a^4R;\quad \text{scale }s:\ R\text{ changes}$$",
    "A road bend looks sharp on a satellite map but dead-straight when you stand on it: the answer depends on the zoom.",
    "Harris is affine-intensity invariant only partially (gain changes R). Say 'invariant to rotation and brightness offset', not 'to everything'."))

CARDS.append(card(16, 6, "WORKED BENCHMARK", "Worked Benchmark: R for Three Windows",
    [L(24, 76, 224, 76, 1.2), R(46, 76 - 40, 34, 40, "#d9dee7", 1.6), R(106, 76, 34, 2.5, "#ffffff", 1.6), R(166, 76, 34, 0.5, "#ffffff", 1.6),
     N(63, 32, "R = 80", 9, w="bold"), N(63, 94, "corner", 9, w="bold"), N(123, 70, "R = −5", 9, w="bold"), N(123, 94, "edge", 9, w="bold"),
     N(183, 70, "R = 0", 9, w="bold"), N(183, 94, "flat", 9, w="bold"),
     N(120, 112, "k = 0.05:  R = λ₁λ₂ − k(λ₁+λ₂)²", 8.5), N(120, 126, "M_c = diag(10,10), M_e = diag(10,0), M_f = 0", 8.5)],
    "With k = 0.05: corner R = 80, edge R = −5, flat R = 0",
    ["<strong>Corner:</strong> $M=\\operatorname{diag}(10,10)$, so $\\det=100$, $\\operatorname{tr}=20$, giving $R=100-0.05(400)=\\mathbf{80}$.",
     "<strong>Edge:</strong> $M=\\operatorname{diag}(10,0)$, so $\\det=0$, $\\operatorname{tr}=10$, giving $R=0-0.05(100)=\\mathbf{-5}$ (negative).",
     "<strong>Flat:</strong> $M=0$ so $R=0$. The <strong>sign and size</strong> of $R$ cleanly separates the three cases."],
    r"$$R_{\text{corner}}=100-0.05(20)^2=80,\quad R_{\text{edge}}=0-0.05(10)^2=-5,\quad R_{\text{flat}}=0$$",
    "A scoreboard where only 'both judges excited' earns big points, 'one excited' costs you a little, and 'none excited' scores zero.",
    "Edge R is NEGATIVE, flat R ≈ 0. Students often say 'edges give small positive R'. Check the sign convention with k > 0."))

# ============================ 17 · SIFT ============================
def _scale():
    out = []
    for i in range(4):
        out.append(R(12, 12 + i * 26, 56, 20, "#ffffff", 1.4)); out.append(N(40, 26 + i * 26, f"L(σ·k^{i})", 8))
    for i in range(3):
        out.append(R(104, 24 + i * 26, 56, 20, "#e2e8f0", 1.4)); out.append(N(132, 38 + i * 26, f"D{i+1}", 8, w="bold"))
        out.append(L(70, 22 + i * 26, 102, 34 + i * 26, 1, d="2 2")); out.append(L(70, 44 + i * 26, 102, 34 + i * 26, 1, d="2 2"))
    out += [N(40, 6, "blur", 8.5, w="bold"), N(132, 6, "DoG = diff", 8.5, w="bold"),
            N(196, 30, "octave:", 8.5, w="bold"), N(196, 44, "σ doubles,", 8.5), N(196, 56, "then image", 8.5), N(196, 68, "halved", 8.5),
            N(196, 92, "k = 2^(1/s)", 8.5, w="bold"), N(196, 106, "s+3 blurs → s+2 DoG", 8)]
    return out

CARDS.append(card(17, 1, "SIFT", "Scale Space & the DoG Pyramid",
    _scale(),
    "Blur repeatedly, subtract adjacent blurs to get DoG layers; after each octave halve the image",
    [r"<strong>Scale space:</strong> $L(x,y,\sigma)=G(x,y,\sigma)\ast I(x,y)$, a stack of progressively blurrier images (larger $\sigma$ = coarser structure).",
     r"<strong>DoG:</strong> $D(x,y,\sigma)=L(x,y,k\sigma)-L(x,y,\sigma)\approx(k-1)\sigma^2\nabla^2G\ast I$, a cheap blob/scale detector, with $k=2^{1/s}$ so that $\sigma$ doubles every $s$ layers (one <strong>octave</strong>).",
     "<strong>Efficiency:</strong> after each octave, <strong>downsample by 2</strong> and start again, so the pyramid costs little more than a single full-resolution blur."],
    r"$$L(x,y,\sigma)=G_\sigma\ast I,\qquad D(x,y,\sigma)=L(x,y,k\sigma)-L(x,y,\sigma),\quad k=2^{1/s}$$",
    "A set of focus rings on a lens: each setting shows the world at a different blur, and the difference between two settings highlights features of that exact size.",
    "You need s+3 blurred images per octave to get s+2 DoG layers and still have s layers with both neighbors for extremum tests."))

def _cube():
    out = []
    for lvl, (dx, dy) in enumerate([(0, 18), (14, 9), (28, 0)]):
        for r in range(3):
            for c in range(3):
                shade = "#e2e8f0" if (lvl == 1 and r == 1 and c == 1) else "#ffffff"
                out.append(R(24 + dx + c * 18, 30 + dy + r * 18, 18, 18, shade, 1.1))
    out += [C(24 + 14 + 27, 30 + 9 + 27, 3.2), N(40, 118, "scale σ/k", 8, "start"), N(72, 100, "scale σ", 8, "start"), N(100, 22, "scale kσ", 8, "start"),
            N(184, 40, "extremum if the", 8.5), N(184, 52, "center beats all", 8.5), N(184, 64, "8 + 9 + 9 = 26", 9, w="bold"), N(184, 76, "neighbors", 8.5),
            N(184, 98, "then sub-pixel fit:", 8.5), N(184, 110, "x̂ = −H⁻¹∇D", 9, w="bold")]
    return out

CARDS.append(card(17, 2, "SIFT", "Keypoint Detection: 26-Neighbor Extrema",
    _cube(),
    "A keypoint is a DoG sample larger (or smaller) than all 26 neighbors in x, y and scale",
    ["<strong>Detect:</strong> compare each DoG sample with its <strong>8 neighbors in the same layer plus 9 above and 9 below</strong> (26 total); keep it if it is the max or the min.",
     r"<strong>Refine:</strong> fit a quadratic (Taylor expansion of $D$) to get the <strong>sub-pixel, sub-scale</strong> location $\hat x=-H^{-1}\nabla D$; drop low-contrast points ($|D(\hat x)|<0.03$).",
     r"<strong>Edge rejection:</strong> a blob is fine but an edge is not stable, so require the 2D Hessian ratio $\dfrac{\operatorname{tr}(H)^2}{\det(H)}<\dfrac{(r+1)^2}{r}$ with $r=10$ (i.e. $<12.1$)."],
    r"$$\hat x=-H^{-1}\nabla D,\qquad \frac{\operatorname{tr}(H)^2}{\det(H)}<\frac{(r+1)^2}{r}=12.1\ \ (r=10)$$",
    "Finding the true summit among nearby peaks in three dimensions: compare with every neighboring ridge, then fit a bowl to pin the peak between sample points.",
    "Edge rejection uses the RATIO of eigenvalues, so it is scale-free. A high ratio means one large curvature (edge), which makes localization unstable."))

def _orient():
    out = [L(20, 118, 224, 118, 1.2)]
    hs = [10, 14, 18, 26, 44, 90, 62, 34, 22, 16, 12, 10, 12, 14, 18, 22, 18, 14, 12, 10, 8, 10, 12, 14, 12, 10, 8, 10, 12, 14, 12, 10, 8, 8, 8, 8]
    for i, h in enumerate(hs):
        out.append(R(22 + i * 5.4, 118 - h * 0.9, 4.6, h * 0.9, "#f1f5f9" if h < 70 else "#d9dee7", 0.9))
    out += [L(20, 118 - 72 * 0.9, 224, 118 - 72 * 0.9, 1, d="4 3"), N(222, 118 - 72 * 0.9 - 3, "80% of peak", 8, "end"),
            N(22 + 5 * 5.4 + 2, 22, "dominant peak", 8.5, "start", "bold"), N(122, 134, "36 bins × 10°  (0° … 360°)", 8.5),
            N(190, 60, "peak → θ", 8.5, w="bold"), N(190, 74, "other bins ≥ 80%", 8), N(190, 86, "→ extra keypoints", 8)]
    return out

CARDS.append(card(17, 3, "SIFT", "Orientation Assignment (Rotation Invariance)",
    _orient(),
    "A 36-bin gradient-orientation histogram: the tallest bar fixes the keypoint's canonical direction",
    ["<strong>Build:</strong> around each keypoint (at its scale) accumulate gradient orientations in a <strong>36-bin histogram</strong>, each vote weighted by gradient magnitude and a Gaussian window.",
     "<strong>Assign:</strong> the <strong>highest peak</strong> gives the keypoint's orientation (refined by a parabola fit); any other peak ≥ 80% of it creates an <strong>extra keypoint</strong> at the same place.",
     "<strong>Payoff:</strong> measuring everything <strong>relative to this orientation</strong> makes the descriptor rotation invariant."],
    r"$$m=\sqrt{L_x^2+L_y^2},\quad \theta=\operatorname{atan2}(L_y,L_x),\quad h[b]=\sum m\cdot G_\sigma\cdot\mathbb{1}[\theta\in\text{bin }b]$$",
    "Turning the map so 'north' is whichever way the local road points: every landmark is then described relative to the road, not to the page.",
    "Orientation ties (≥ 80% peaks) produce multiple keypoints at one location. Do not de-duplicate them: they improve matching robustness."))

def _desc():
    out = []
    for r in range(4):
        for c in range(4):
            x0, y0 = 24 + c * 28, 14 + r * 28
            out.append(R(x0, y0, 28, 28, "#ffffff", 1.1))
            cx, cy = x0 + 14, y0 + 14
            for a in range(0, 360, 45):
                ln = 5 + ((r * 3 + c * 5 + a // 45) % 5) * 1.7
                out.append(L(cx, cy, cx + ln * math.cos(math.radians(a)), cy - ln * math.sin(math.radians(a)), 1.1, ar=False))
    out += [N(170, 40, "4 × 4 cells", 9, "start", "bold"), N(170, 54, "× 8 orientations", 9, "start", "bold"), N(170, 70, "= 128-D vector", 10, "start", "bold"),
            N(170, 92, "normalize → clip 0.2", 8.5, "start"), N(170, 104, "→ renormalize", 8.5, "start"), N(124, 134, "16×16 patch rotated to θ, Gaussian-weighted", 8, "middle")]
    return out

CARDS.append(card(17, 4, "SIFT", "The 128-Dimensional Descriptor",
    _desc(),
    "Sixteen cells each hold an 8-bin orientation histogram; stacked together they form a 128-vector",
    ["<strong>Patch:</strong> take a $16\\times16$ window around the keypoint, <strong>rotated to its orientation</strong> and scaled to its σ, weighted by a Gaussian.",
     "<strong>Descriptor:</strong> split into a $4\\times4$ grid of cells; each cell has an <strong>8-bin gradient-orientation histogram</strong>: $4\\times4\\times8=\\mathbf{128}$ numbers (with trilinear interpolation to avoid boundary effects).",
     "<strong>Illumination robustness:</strong> normalize to unit length (cancels contrast), <strong>clip entries at 0.2</strong> (tames saturated gradients), then renormalize."],
    r"$$\mathbf{d}\in\mathbb{R}^{4\cdot4\cdot8}=\mathbb{R}^{128},\quad \mathbf{d}\leftarrow\frac{\mathbf{d}}{\|\mathbf{d}\|},\ \ d_i\leftarrow\min(d_i,0.2),\ \ \text{renormalize}$$",
    "Describing a face by a 4×4 grid of tiny compasses: each cell reports which way edges lean, so lighting changes don't change the story.",
    "Both normalizations matter. Normalizing once cancels contrast, the clip handles non-linear lighting, and the second normalization restores unit length."))

def _ratio():
    out = [C(60, 74, 5, "#ffffff", 2), N(60, 94, "query q", 9, w="bold"),
           C(98, 66, 4), N(98, 56, "NN₁", 8.5, "middle", "bold"), C(140, 100, 4, "#ffffff"), N(150, 116, "NN₂", 8.5, "start", "bold"),
           L(64, 72, 94, 67, 1.6), L(64, 76, 136, 99, 1.2, d="4 3"),
           N(80, 62, "d₁", 8.5, "middle", "bold"), N(100, 92, "d₂", 8.5, "middle", "bold"),
           N(190, 36, "d₁/d₂ < 0.8", 10, "middle", "bold"), N(190, 52, "→ accept", 9), N(190, 74, "d₁/d₂ ≥ 0.8", 10, "middle", "bold"), N(190, 90, "→ reject", 9),
           N(120, 134, "ambiguous: the best match isn't clearly best", 8.5)]
    return out

CARDS.append(card(17, 5, "SIFT", "Matching & Lowe's Ratio Test",
    _ratio(),
    "Accept a match only if the nearest neighbor is clearly closer than the second nearest",
    ["<strong>Match:</strong> for each descriptor in image A, find the nearest descriptor (Euclidean distance) in image B.",
     "<strong>Ratio test:</strong> also find the second nearest. Keep the match only if <strong>$d_1/d_2<0.8$</strong> (Lowe). Repeated textures give $d_1\\approx d_2$, which is flagged as ambiguous and dropped.",
     "<strong>Verify geometry:</strong> remaining matches still contain outliers, so fit a transform with <strong>RANSAC</strong> (affine/homography) and keep the inliers."],
    r"$$\text{accept } (q\leftrightarrow\text{NN}_1)\iff \frac{\|q-\text{NN}_1\|}{\|q-\text{NN}_2\|}<0.8$$",
    "A witness who points to one suspect and says 'definitely him' is credible; one who says 'it's one of these two' is not.",
    "The threshold 0.8 is a tradeoff: Lowe's paper reports it discards ~90% of false matches while losing <5% of correct ones. Mention the tradeoff, not 'it is exact'."))

CARDS.append(card(17, 6, "WORKED BENCHMARK", "Worked Benchmark: Ratio Test & Edge Test Numbers",
    [L(24, 56, 224, 56, 1.4, ar=True)] + [L(24 + 200 * v, 50, 24 + 200 * v, 62, 1.3) for v in [0, 0.2, 0.4, 0.6, 0.8, 1.0]] +
    [N(24 + 200 * v, 76, str(v), 8.5) for v in [0, 0.2, 0.4, 0.6, 0.8, 1.0]] +
    [L(24 + 200 * 0.8, 24, 24 + 200 * 0.8, 62, 1.6, d="4 3"), N(184, 18, "threshold 0.8", 8.5, "middle", "bold"),
     C(24 + 200 * 0.6, 56, 5), N(100, 40, "0.3/0.5 = 0.6 ✓", 9, "middle", "bold"),
     C(24 + 200 * 0.9, 56, 5, "#ffffff"), N(204, 40, "0.45/0.5 = 0.9 ✗", 8.5, "middle", "bold"),
     N(120, 98, "descriptor length: 4 × 4 × 8 = 128", 9, w="bold"), N(120, 114, "edge test: (10+1)²/10 = 12.1", 9, w="bold"), N(120, 130, "tr²/det < 12.1 keeps blobs, drops edges", 8.5)],
    "d₁/d₂ = 0.6 is accepted, 0.9 is rejected; r = 10 gives the edge-test bound 12.1",
    ["<strong>Accepted match:</strong> $d_1=0.3,\\ d_2=0.5\\Rightarrow$ ratio $=0.6<0.8$, so the nearest neighbor is clearly better than the runner-up.",
     "<strong>Rejected match:</strong> $d_1=0.45,\\ d_2=0.5\\Rightarrow$ ratio $=0.9\\ge0.8$: nearly a tie, so it is ambiguous and dropped.",
     "<strong>Counts to remember:</strong> descriptor length $4\\cdot4\\cdot8=128$; edge-rejection bound $(r+1)^2/r=(11)^2/10=12.1$ for $r=10$; contrast threshold $|D|<0.03$."],
    r"$$\tfrac{0.3}{0.5}=0.6<0.8\ \checkmark,\qquad \tfrac{0.45}{0.5}=0.9>0.8\ \times,\qquad \tfrac{(10+1)^2}{10}=12.1$$",
    "A quiz where 'clearly first place' counts but a photo-finish does not.",
    "The ratio uses distances, not squared distances, in Lowe's original. If you use squared distance the equivalent threshold is 0.8² = 0.64."))
