import math
from dip_lib import *

CARDS = []

def _poly(pts, w=1.8, dash=None):
    d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    return P(d, w=w, dash=dash)

def _curve(fn, x0, x1, step=3):
    return [(x, fn(x)) for x in range(x0, x1 + 1, step)]

# ============================ 06 · LSI & CONVOLUTION ============================
CARDS.append(card(6, 1, "LSI SYSTEMS", "LSI Systems and the Impulse Response",
    [N(24, 30, "δ", 12, w="bold"), L(24, 62, 24, 40, 2.2, ar=True), L(10, 62, 40, 62, 1.1),
     R(56, 34, 44, 30, "#f1f5f9", 1.8), N(78, 53, "LSI", 10, w="bold"), L(42, 49, 54, 49, 1.3, ar=True), L(102, 49, 128, 49, 1.3, ar=True),
     L(136, 62, 136, 38, 2.2), L(148, 62, 148, 26, 2.2), L(160, 62, 160, 46, 2.2), L(128, 62, 172, 62, 1.1), N(150, 76, "h[x,y]", 9),
     N(24, 100, "f", 11, w="bold"), R(56, 84, 44, 30, "#f1f5f9", 1.8), N(78, 103, "LSI", 10, w="bold"),
     L(38, 99, 54, 99, 1.3, ar=True), L(102, 99, 128, 99, 1.3, ar=True), N(168, 103, "g = f ∗ h", 10, w="bold"),
     N(210, 40, "linear +", 8.5), N(210, 52, "shift-", 8.5), N(210, 64, "invariant", 8.5)],
    "An impulse in gives h out; any image is a sum of shifted impulses, so any output is a sum of shifted h's",
    ["<strong>What:</strong> An <strong>LSI system</strong> obeys superposition (linear) and gives the same response to a shifted input, just shifted (shift-invariant).",
     r"<strong>How:</strong> Feed it a unit impulse and record the output $h$ (the <strong>PSF</strong>). Any $f$ is a weighted sum of shifted impulses, so $g=\sum f(m,n)\,h(x-m,y-n)$.",
     "<strong>Why:</strong> One small array $h$ completely describes the whole system, which is why <strong>convolution kernels</strong> are enough."],
    r"$$g(x,y)=\sum_{m}\sum_{n}f(m,n)\,h(x-m,\,y-n)=(f\ast h)(x,y)$$",
    "Dropping a pebble in a pond: once you know the ripple from one pebble, a rain shower is just many shifted, scaled ripples added up.",
    "A system that is linear but not shift-invariant (like lens blur that varies across the frame) is NOT described by a single convolution kernel."))

CARDS.append(card(6, 2, "LSI SYSTEMS", "Convolution Flips the Kernel; Correlation Doesn't",
    [N(14, 22, "h =", 10, "start", w="bold")] + [GRID(36, 10, [["a", "b", "c"]], cell=22)] +
    [P("M47 36 C47 52 105 52 105 36", w=1.4, ar=True), N(76, 62, "flip", 9),
     N(14, 88, "ĥ =", 10, "start", w="bold"), GRID(36, 76, [["c", "b", "a"]], cell=22),
     N(160, 28, "convolution: use ĥ", 9, "middle", w="bold"), N(160, 42, "g(x)=Σ f(m) h(x−m)", 8.5),
     N(160, 66, "correlation: use h", 9, "middle", w="bold"), N(160, 80, "g(x)=Σ f(m) h(m−x)", 8.5),
     N(120, 124, "same result only if h is symmetric", 9)],
    "Convolution mirrors h before sliding; correlation slides h as it is",
    ["<strong>Convolution</strong> rotates the kernel by 180° (flips every axis) before the sliding-window multiply-add.",
     "<strong>Correlation</strong> uses the kernel unflipped, which is what template matching and most CNN libraries actually compute.",
     "For a <strong>symmetric kernel</strong> (box, Gaussian, Laplacian) both give the same output; for derivative kernels like $[1,0,-1]$ the flip <strong>negates</strong> the result."],
    r"$$(f\ast h)(x)=\sum_m f(m)\,h(x-m),\qquad (f\star h)(x)=\sum_m f(m)\,h(m-x)$$",
    "Reading a word in a mirror versus on paper: same letters, opposite order, and for a palindrome you cannot tell the difference.",
    "Forgetting the flip gives the wrong sign or direction for asymmetric kernels. Check whether a library does convolution or correlation."))

CARDS.append(card(6, 3, "SEPARABLE FILTERS", "Separable Kernels: h = h₁ h₂ᵀ",
    [GRID(10, 20, [[1], [2], [1]], cell=16), N(34, 12, "col", 8), N(50, 50, "×", 14, w="bold"),
     GRID(62, 36, [[1, 2, 1]], cell=16), N(86, 30, "row", 8), N(120, 50, "=", 14, w="bold"),
     GRID(134, 18, [[1, 2, 1], [2, 4, 2], [1, 2, 1]], cell=18),
     N(120, 100, "K×K kernel: K² mults per pixel", 8.5), N(120, 114, "two 1-D passes: 2K mults per pixel", 8.5, w="bold"),
     N(120, 130, "K = 9: 81 → 18, a 4.5× saving", 8.5)],
    "A 3×3 Gaussian-like kernel is the outer product of a column and a row of [1 2 1]",
    ["A kernel is <strong>separable</strong> if it is an outer product $h=\\mathbf{h}_1\\mathbf{h}_2^{T}$, i.e. a rank-1 matrix.",
     "Then 2D convolution factors into <strong>a 1D pass down columns and a 1D pass along rows</strong>, replacing $K^2$ multiplies per pixel by $2K$.",
     "The <strong>Gaussian</strong> (and the box filter) are separable; most Laplacian/Sobel-type kernels are separable as 'smooth × difference' products."],
    r"$$h(x,y)=h_1(x)\,h_2(y)\ \Rightarrow\ f\ast h=(f\ast_y h_2)\ast_x h_1,\qquad G_\sigma(x,y)=G_\sigma(x)G_\sigma(y)$$",
    "Mowing a lawn by rows then by columns instead of tracing every square: two simple sweeps cover the same ground.",
    "Not every 2D kernel is separable. Test the matrix rank: if rank > 1, you can only approximate it (via SVD) with a few separable terms."))

CARDS.append(card(6, 4, "SPATIAL FILTERS", "Smoothing: Box vs Gaussian",
    [AX(20, 120, 224, 14), P("M30 120 L30 70 L120 70 L120 120", w=1.6, dash="5 3"),
     P(_gauss := "M30 119 C60 118 78 112 90 96 C100 80 108 56 120 52 C132 56 140 80 150 96 C162 112 180 118 210 119", w=2.2),
     N(76, 62, "box: sharp cut-off", 8.5), N(168, 48, "Gaussian: smooth", 8.5, w="bold"),
     N(120, 134, "kernel weight vs distance", 8)],
    "A Gaussian tapers smoothly to zero; a box has a hard edge that rings in frequency",
    ["<strong>What:</strong> Smoothing replaces each pixel by a weighted average of its neighborhood, <strong>suppressing high frequencies and noise</strong>.",
     "<strong>How:</strong> A $K{\\times}K$ <strong>box</strong> filter averages equally (variance reduced by $1/K^2$); a <strong>Gaussian</strong> weights nearby pixels more, and its width is set by $\\sigma$.",
     "<strong>Why Gaussian:</strong> Its Fourier transform is also Gaussian (no ripples), it is separable, and it never creates new extrema when scale increases."],
    r"$$G_\sigma(x,y)=\frac{1}{2\pi\sigma^2}e^{-\frac{x^2+y^2}{2\sigma^2}},\qquad \operatorname{Var}\big[\bar{f}\big]=\frac{\sigma_\eta^2}{K^2}\ \text{(box of size } K\times K)$$",
    "A frosted-glass window: the Gaussian is evenly frosted, while the box is a clear pane with a hard-edged blurry patch.",
    "Smoothing also blurs edges. A bigger kernel removes more noise but also destroys more detail, so there is always a tradeoff."))

def _edge_curves():
    step = P("M20 100 L110 100 L110 50 L220 50", w=1.4, dash="2 3")
    blur = P("M20 100 L70 100 C92 100 96 56 150 50 L220 50", w=1.5, dash="6 3")
    sharp = P("M20 104 L72 104 C84 106 96 108 106 94 L116 42 C124 36 134 40 148 46 L220 50", w=2.4)
    return [AX(14, 126, 226, 14), step, blur, sharp,
            N(34, 94, "f", 9), N(150, 66, "blurred f̄", 8.5, "start"), N(60, 118, "undershoot", 8), N(150, 30, "overshoot", 8, "start"), N(176, 100, "sharpened", 9, "start", "bold")]

CARDS.append(card(6, 5, "SPATIAL FILTERS", "Sharpening: Unsharp Mask & Laplacian",
    _edge_curves(),
    "f + k(f − blur) steepens the edge and adds a halo (undershoot and overshoot) on each side",
    ["<strong>Unsharp masking:</strong> subtract a blurred copy to isolate fine detail, $m=f-\\bar f$, then <strong>add that detail back</strong> times a gain $k$.",
     "<strong>High-boost</strong> ($k>1$) emphasizes edges more; the <strong>Laplacian</strong> version is $g=f-c\\nabla^2 f$ (use $c>0$ when the center coefficient is negative).",
     "Edges become crisper because the profile gains <strong>overshoot on the bright side and undershoot on the dark side</strong>, which the eye reads as sharper."],
    r"$$g=f+k\,(f-\bar f),\qquad g=f-c\,\nabla^2 f,\quad \nabla^2 f=f_{xx}+f_{yy}$$",
    "Tracing a pencil outline over a faded drawing: the outline is exactly the difference between the crisp and the blurry versions.",
    "Sharpening amplifies noise as well as edges. And with a Laplacian whose center is negative you SUBTRACT it; the sign depends on the kernel convention."))

CARDS.append(card(6, 6, "WORKED BENCHMARK", "Worked Benchmark: 1-D Convolution with [1, 0, −1]",
    [N(14, 24, "f", 10, "start", w="bold"), GRID(30, 10, [[1, 2, 3, 4]], cell=22),
     N(14, 62, "h", 10, "start", w="bold"), GRID(30, 48, [[1, 0, -1]], cell=22),
     N(14, 104, "f∗h", 10, "start", w="bold"), GRID(34, 90, [[1, 2, 2, 2, -3, -4]], cell=22, shade={(0, 4), (0, 5)}),
     N(184, 30, "full length", 8.5), N(184, 42, "4 + 3 − 1 = 6", 8.5, w="bold"),
     N(184, 62, "interior = 2", 8.5), N(184, 74, "(a ramp's slope)", 8.5),
     N(120, 137, "grayed ends are boundary transients", 8)],
    "Output of length 4+3−1 = 6: a constant 2 in the middle (the ramp's slope), edge effects at the ends",
    ["<strong>Flip</strong> $h=[1,0,-1]$ to $[-1,0,1]$, then slide it along $f=[1,2,3,4]$ computing the full overlap at every shift.",
     "<strong>Results:</strong> $n=0:1$; $n=1:2$; $n=2:3-1=2$; $n=3:4-2=2$; $n=4:-3$; $n=5:-4$, giving <strong>[1, 2, 2, 2, −3, −4]</strong>.",
     "The middle value <strong>2</strong> is the discrete derivative (here $(f_{x+1}-f_{x-1})$) of a unit-slope ramp; the end values are <strong>zero-padding artifacts</strong>."],
    r"$$f\ast h=[1,\,2,\,2,\,2,\,-3,\,-4],\qquad \text{length}=M+K-1=4+3-1=6$$",
    "Measuring a hill's steepness by comparing the heights two steps ahead and behind: on a steady ramp it gives the same steepness everywhere inside.",
    "With correlation (no flip) you would get the NEGATIVE of the interior result (−2). Always confirm which operation is meant before reading an edge sign."))

# ============================ 07 · 2D FOURIER ============================
CARDS.append(card(7, 1, "2D FOURIER", "2D DFT Definition & Separability",
    [R(10, 22, 52, 52, "#ffffff", 1.6)] + [L(10, 22 + i * 8.7, 62, 22 + i * 8.7, 1.1) for i in range(1, 6)] +
    [N(36, 90, "f(x,y)", 9), L(66, 48, 96, 48, 1.4, ar=True), N(81, 40, "rows", 8),
     R(100, 22, 52, 52, "#ffffff", 1.6)] + [L(100 + i * 8.7, 22, 100 + i * 8.7, 74, 1.1) for i in range(1, 6)] +
    [N(126, 90, "1-D DFT of rows", 8), L(156, 48, 184, 48, 1.4, ar=True), N(170, 40, "cols", 8),
     R(188, 22, 40, 52, "#f1f5f9", 1.8), N(208, 52, "F(u,v)", 9, w="bold"),
     N(120, 114, "O(MN·(M+N)) instead of O(M²N²)", 9), N(120, 130, "with FFT: O(MN log MN)", 9, w="bold")],
    "A 2D DFT is a 1-D DFT on every row, then a 1-D DFT on every column of the result",
    ["The 2D DFT of an $M\\times N$ image decomposes the image into <strong>2D complex sinusoids</strong> of frequency $(u/M,\\,v/N)$.",
     r"The kernel <strong>factors</strong>: $e^{-j2\pi(ux/M+vy/N)}=e^{-j2\pi ux/M}\,e^{-j2\pi vy/N}$, so compute 1D DFTs along rows, then along columns (in either order).",
     "With the FFT, this costs <strong>O(MN log MN)</strong>, so frequency-domain filtering is practical on large images."],
    r"$$F(u,v)=\sum_{x=0}^{M-1}\sum_{y=0}^{N-1}f(x,y)\,e^{-j2\pi\left(\frac{ux}{M}+\frac{vy}{N}\right)},\quad f(x,y)=\frac{1}{MN}\sum_{u,v}F(u,v)e^{j2\pi\left(\frac{ux}{M}+\frac{vy}{N}\right)}$$",
    "Reading a spreadsheet by first totaling each row, then totaling those totals down the columns: two simple passes build the full picture.",
    "The inverse carries the 1/(MN) factor, but some textbooks put 1/√(MN) on both transforms. State your normalization when comparing numbers."))

CARDS.append(card(7, 2, "2D FOURIER", "Periodicity, Symmetry & Centering the Spectrum",
    [R(14, 26, 70, 70, "#ffffff", 1.6), C(14, 26, 3.5), N(26, 22, "DC", 8, "start"),
     L(14, 61, 84, 61, 1, d="2 2"), L(49, 26, 49, 96, 1, d="2 2"),
     L(90, 61, 134, 61, 1.5, ar=True), N(112, 52, "(−1)^(x+y)", 8),
     R(144, 26, 70, 70, "#f1f5f9", 1.6), C(179, 61, 3.5), N(179, 78, "DC", 8, w="bold"),
     N(49, 110, "uncentered", 8.5), N(179, 110, "centered", 8.5),
     N(120, 130, "F(u,v) = F*(−u,−v) for real f", 9, w="bold")],
    "Multiplying f by (−1)^(x+y) slides the DC term from the corner to the center of the display",
    ["The DFT is <strong>periodic</strong> with period $(M,N)$ in both $u$ and $v$, so the 'corner' spectrum is really four wrapped quadrants.",
     r"Multiplying $f(x,y)$ by $(-1)^{x+y}$ before the transform shifts the spectrum by $(M/2,N/2)$, <strong>placing DC at the center</strong> for easy viewing and filter design.",
     r"For a real image, <strong>conjugate symmetry</strong> $F(u,v)=F^{*}(-u,-v)$ holds, so $|F|$ is symmetric about the origin and half the spectrum is redundant."],
    r"$$\mathcal{F}\{f(x,y)(-1)^{x+y}\}=F\!\left(u-\tfrac M2,\,v-\tfrac N2\right),\qquad F(u,v)=F^{*}(-u,-v)\ \ (f\ \text{real})$$",
    "A clock face whose '12' is printed in the corner of the page: recentering just rotates the picture so 12 sits at the middle.",
    "The (−1)^(x+y) trick works only for even M and N. And it must be applied to f BEFORE the transform (or fftshift AFTER), not both."))

CARDS.append(card(7, 3, "2D FOURIER", "Magnitude vs Phase: Phase Carries Structure",
    [R(10, 24, 100, 90, "#ffffff", 1.6), C(60, 69, 8, "none", 1.2), C(60, 69, 18, "none", 1.2), C(60, 69, 30, "none", 1.2), C(60, 69, 42, "none", 1.2),
     N(60, 126, "|F| only → blobs", 8.5),
     R(130, 24, 100, 90, "#ffffff", 1.6), R(150, 40, 60, 58, "none", 2.2), L(150, 40, 210, 98, 1.6), L(210, 40, 150, 98, 1.6),
     N(180, 126, "∠F only → edges survive", 8.5),
     N(120, 14, "swap them and the picture follows the PHASE", 8.5, w="bold")],
    "Magnitude-only reconstruction loses all shape; phase-only still looks like the image",
    ["<strong>Magnitude</strong> $|F|$ says how much of each frequency is present; <strong>phase</strong> $\\angle F$ says where those sinusoids line up.",
     "<strong>Edges and positions</strong> come from phases lining up; reconstruct from phase only (set $|F|=1$) and the picture is still recognizable.",
     "<strong>Oppenheim's phase-dominance:</strong> swapping the phases of two images makes the result resemble the image that donated the <strong>phase</strong>."],
    r"$$F(u,v)=|F(u,v)|\,e^{j\angle F(u,v)},\qquad \tilde f=\mathcal{F}^{-1}\{e^{j\angle F}\}\ \text{keeps edges};\ \ \mathcal{F}^{-1}\{|F|\}\ \text{does not}$$",
    "A choir's recipe: the volume of each singer (magnitude) matters less than exactly when each one starts singing (phase).",
    "Do not conclude magnitude is useless: it still sets contrast and texture energy. Only that structure, position and edges are carried by phase."))

CARDS.append(card(7, 4, "2D FOURIER", "Convolution Theorem & Zero-Padding",
    [N(14, 24, "f", 10, "start", w="bold"), R(30, 14, 60, 14, "#f1f5f9", 1.5), N(60, 40, "M", 8.5),
     N(14, 62, "h", 10, "start", w="bold"), R(30, 52, 40, 14, "#f1f5f9", 1.5), N(50, 78, "K", 8.5),
     N(14, 104, "f∗h", 10, "start", w="bold"), R(30, 94, 100, 14, "#e2e8f0", 1.5), N(80, 120, "M + K − 1", 8.5, w="bold"),
     L(30, 134, 130, 134, 1.2, ar=True), N(180, 24, "P ≥ M + K − 1", 9.5, w="bold"),
     N(180, 42, "else circular", 8.5), N(180, 54, "convolution wraps", 8.5), N(180, 66, "the tail onto", 8.5), N(180, 78, "the head", 8.5),
     N(180, 100, "F{f ⊛ h} = F·H", 9.5)],
    "Pad both signals to length P ≥ M+K−1 so the circular result equals the linear one",
    [r"<strong>The theorem:</strong> convolution in space is <strong>pointwise multiplication</strong> in frequency, $\mathcal{F}\{f\ast h\}=F\cdot H$. Filtering becomes one multiply per frequency.",
     "<strong>The catch:</strong> the DFT product corresponds to <strong>circular</strong> convolution (the signal wraps around), which pollutes the result with wraparound error.",
     "<strong>The fix:</strong> zero-pad both to $P\\ge M+K-1$ before transforming; then circular and linear convolution agree."],
    r"$$f\circledast h\ \leftrightarrow\ F(u,v)H(u,v),\qquad P\ge M+K-1\ \Rightarrow\ f\circledast h=f\ast h$$",
    "Pouring water into a ring-shaped trough: without extra length the water that overflows the end re-enters at the start.",
    "Forgetting to zero-pad causes wraparound artifacts at the borders. Also both f and h need padding to the SAME size P, in both dimensions."))

CARDS.append(card(7, 5, "2D FOURIER", "Central Slice (Projection-Slice) Theorem",
    [R(10, 22, 90, 90, "#ffffff", 1.6), E(55, 67, 26, 15, -30, "#f1f5f9", 1.6),
     L(24, 14, 24, 22, 1.2, ar=True), L(55, 14, 55, 22, 1.2, ar=True), L(86, 14, 86, 22, 1.2, ar=True),
     N(55, 126, "parallel projection p_θ(t)", 8.5),
     L(116, 68, 132, 68, 1.4, ar=True), N(124, 60, "1-D FT", 8),
     L(140, 112, 140, 20, 1.2, ar=True), L(130, 66, 232, 66, 1.2, ar=True),
     L(150, 100, 224, 36, 2.4), N(228, 26, "F(ρcosθ, ρsinθ)", 8.5, "end", "bold"),
     N(190, 126, "slice through origin at angle θ", 8.5)],
    "The 1-D transform of a projection equals the line through the origin of the 2-D transform at the same angle",
    ["<strong>Projection:</strong> add up the image along parallel rays at angle $\\theta$ to get the 1D profile $p_\\theta(t)$ (what a CT scanner measures).",
     r"<strong>Theorem:</strong> $\mathcal{F}_{1D}\{p_\theta\}(\rho)=F(\rho\cos\theta,\,\rho\sin\theta)$, a <strong>radial slice</strong> of the 2D spectrum.",
     "<strong>Payoff:</strong> collect projections at many angles, fill the 2D frequency plane, invert: <strong>tomographic reconstruction</strong> (CT)."],
    r"$$\int p_\theta(t)\,e^{-j2\pi\rho t}\,dt=F(\rho\cos\theta,\ \rho\sin\theta)$$",
    "Shadow of a sculpture on a wall: the shadow's vibration pattern is exactly one straight cut through the sculpture's frequency 'fingerprint'.",
    "The slice goes through the ORIGIN at the SAME angle θ as the ray direction normal. Mixing up θ with θ+90° rotates the slice."))

CARDS.append(card(7, 6, "WORKED BENCHMARK", "Worked Benchmark: 2×2 DFT of [[1,2],[3,4]]",
    [N(14, 30, "f", 10, "start", w="bold"), GRID(30, 14, [[1, 2], [3, 4]], cell=26),
     L(88, 40, 112, 40, 1.4, ar=True), N(100, 32, "DFT", 8),
     N(124, 30, "F", 10, "start", w="bold"), GRID(138, 14, [[10, -2], [-4, 0]], cell=26, shade={(0, 0)}),
     N(120, 88, "F(u,v) = Σ f(x,y)(−1)^(ux+vy)", 9),
     N(120, 104, "F(0,0)=10 (sum = 4× mean)", 8.5), N(120, 118, "F(0,1)=1+3−2−4=−2", 8.5), N(120, 132, "F(1,0)=1+2−3−4=−4,  F(1,1)=1−2−3+4=0", 8.5)],
    "For N=2, the DFT kernel is just ±1: each F is a signed sum of the four pixels",
    ["For $M=N=2$, $W_2=e^{-j\\pi}=-1$, so $F(u,v)=\\sum f(x,y)\\,(-1)^{ux+vy}$: <strong>only additions and subtractions</strong>.",
     "<strong>$F(0,0)=1+2+3+4=10$</strong> is the DC term (4 × the mean 2.5); $F(0,1)=(1+3)-(2+4)=-2$ measures left-right contrast; $F(1,0)=(1+2)-(3+4)=-4$ measures top-bottom contrast.",
     "<strong>$F(1,1)=1-2-3+4=0$</strong>: the diagonal/checkerboard component vanishes. Inverse: $f=\\tfrac14\\sum F\\,(-1)^{ux+vy}$ recovers the image."],
    r"$$F=\begin{pmatrix}10&-2\\-4&0\end{pmatrix},\qquad f(0,0)=\tfrac14\,(10-2-4+0)=1$$",
    "A 2×2 checker of four coins: the DFT reports the total weight, the left-vs-right tilt, the top-vs-bottom tilt, and the diagonal tilt.",
    "Rows index x (vertical) and columns y here. Swapping the roles of u and v transposes F and flips the −2/−4 entries."))

# ============================ 08 · SAMPLING ============================
def _tri(c, w=22, h=60, base=125):
    return f"M{c-w} {base} L{c} {base-h} L{c+w} {base}"

CARDS.append(card(8, 1, "SAMPLING THEORY", "Sampling Replicates the Spectrum",
    [L(14, 125, 226, 125, 1.2, ar=True), P(_tri(120), "#f1f5f9", 2), P(_tri(60), "#ffffff", 1.6, dash="4 3"), P(_tri(180), "#ffffff", 1.6, dash="4 3"),
     L(120, 125, 120, 135, 1.2), L(60, 125, 60, 135, 1.2), L(180, 125, 180, 135, 1.2),
     N(120, 143, "0", 8.5), N(60, 143, "−1/Δ", 8.5), N(180, 143, "1/Δ", 8.5),
     N(120, 52, "baseband", 8.5), N(120, 20, "S(u) = (1/Δ) Σ F(u − k/Δ)", 9, w="bold")],
    "Sampling in space makes copies of the spectrum, centered at every multiple of the sampling rate 1/Δ",
    ["<strong>What:</strong> Sampling multiplies the image by a comb of impulses spaced $\\Delta$ apart.",
     "<strong>How:</strong> Multiplication in space becomes <strong>convolution with a comb in frequency</strong>, so the spectrum $F(u)$ is copied at every $k/\\Delta$.",
     "<strong>Why:</strong> To recover the original, you must be able to cut out just the baseband copy with a low-pass filter, which needs the copies <strong>not to overlap</strong>."],
    r"$$f_s(x)=f(x)\sum_n\delta(x-n\Delta)\ \Rightarrow\ F_s(u)=\frac{1}{\Delta}\sum_{k}F\!\left(u-\frac{k}{\Delta}\right)$$",
    "A copy machine stamping the same picture side by side at fixed intervals: if the copies are far enough apart you can isolate one cleanly.",
    "Copies repeat at multiples of the SAMPLING FREQUENCY 1/Δ, not 2/Δ. And in 2D they tile in both u and v, giving a lattice of replicas."))

CARDS.append(card(8, 2, "SAMPLING THEORY", "Nyquist: f_s ≥ 2 f_max",
    [L(14, 60, 226, 60, 1.2, ar=True), P(_tri(120, 22, 38, 60), "#f1f5f9", 2), P(_tri(60, 22, 38, 60), "#ffffff", 1.6, dash="4 3"), P(_tri(180, 22, 38, 60), "#ffffff", 1.6, dash="4 3"),
     N(120, 12, "f_s > 2 f_max: gaps → recoverable", 8.5, w="bold"),
     L(14, 128, 226, 128, 1.2, ar=True), P(_tri(120, 40, 38, 128), "#f1f5f9", 2), P(_tri(80, 40, 38, 128), "#ffffff", 1.6, dash="4 3"), P(_tri(160, 40, 38, 128), "#ffffff", 1.6, dash="4 3"),
     N(120, 82, "f_s < 2 f_max: overlap → aliasing", 8.5, w="bold")],
    "Top: replicas separated, a low-pass can isolate the original. Bottom: replicas overlap and cannot be undone",
    ["<strong>Condition:</strong> an image bandlimited to $|u|\\le u_{\\max}$ must be sampled at <strong>$f_s\\ge 2u_{\\max}$</strong> (Nyquist rate) in each direction: $\\Delta x\\le\\frac1{2u_{\\max}}$.",
     "<strong>If it holds</strong> the replicas don't touch and an ideal LPF (sinc interpolation) <strong>reconstructs the original exactly</strong>.",
     "<strong>If it fails</strong> the replicas overlap and high frequencies masquerade as low ones: <strong>aliasing</strong>, an irreversible loss."],
    r"$$f_s\ge 2f_{\max},\qquad f(x)=\sum_n f(n\Delta)\,\operatorname{sinc}\!\left(\frac{x-n\Delta}{\Delta}\right)$$",
    "Filming a spinning wheel: at 24 frames/s you can follow it if it turns slowly, but past half the frame rate it appears to spin backward.",
    "Nyquist rate is 2·f_max, while the Nyquist FREQUENCY is f_s/2. And the condition is for bandlimited signals; real images are not exactly bandlimited, hence prefiltering."))

def _alias():
    hi = [(x, 72 - 40 * math.sin(2 * math.pi * 0.9 * (x - 20) / 20)) for x in range(20, 221, 1)]
    lo = [(x, 72 + 40 * math.sin(2 * math.pi * 0.1 * (x - 20) / 20)) for x in range(20, 221, 2)]
    dots = [C(20 + 20 * n, 72 + 40 * math.sin(2 * math.pi * 0.1 * n), 3) for n in range(0, 11)]
    return [L(14, 72, 228, 72, 1, d="2 3"), _poly(hi, 1.2), _poly(lo, 1.8, "6 3")] + dots + [
        N(120, 134, "0.9 cycles/sample  looks like  0.1 cycles/sample", 8.5, w="bold"), N(40, 20, "true", 8.5, "start"), N(40, 32, "alias (dashed)", 8.5, "start")]

CARDS.append(card(8, 3, "SAMPLING THEORY", "Aliasing: A Fast Wave Disguised as a Slow One",
    _alias(),
    "The same sample dots lie on both the fast sinusoid and a slow impostor",
    ["When $f>f_s/2$ the samples <strong>cannot tell</strong> the fast sinusoid from a slower one that passes through the same points.",
     r"The apparent frequency <strong>folds</strong> about $f_s/2$: $f_{\text{alias}}=|f-k f_s|$ for the integer $k$ that brings it into $[0,f_s/2]$. In images this is the <strong>moiré pattern</strong> on fine fabrics or screens.",
     "<strong>Defense:</strong> low-pass (anti-alias) filter the image BEFORE sampling or downsampling, because aliasing cannot be removed afterward."],
    r"$$f_{\text{alias}}=|f-k\,f_s|,\quad k=\operatorname{round}(f/f_s),\qquad \text{e.g. } f=0.9f_s\ \Rightarrow\ 0.1f_s$$",
    "Wagon-wheel effect in old films: spokes turning too fast for the frame rate seem to creep slowly or even backward.",
    "Aliasing happens at SAMPLING time, so filtering after the fact is useless. Also a pure rescale with nearest-neighbor can alias heavily."))

CARDS.append(card(8, 4, "MULTI-RATE", "Downsampling by M (Decimation)",
    [N(14, 36, "x[n]", 10, "start", w="bold"), L(36, 32, 54, 32, 1.4, ar=True),
     R(56, 16, 56, 32, "#f1f5f9", 1.8), N(84, 36, "LPF  π/M", 9, w="bold"), L(112, 32, 128, 32, 1.4, ar=True),
     R(130, 16, 36, 32, "#ffffff", 1.8), N(148, 36, "↓M", 11, w="bold"), L(166, 32, 184, 32, 1.4, ar=True), N(204, 36, "y[n]", 10, w="bold"),
     N(120, 70, "y[n] = x[Mn]", 10, w="bold"),
     N(120, 88, "Y(ω) = (1/M) Σ_{k=0}^{M−1} X((ω − 2πk)/M)", 8.5),
     N(120, 106, "spectrum is STRETCHED by M and M copies add", 8.5),
     N(120, 122, "without the LPF the copies overlap → aliasing", 8.5, w="bold")],
    "Low-pass first, then keep every Mth sample",
    ["<strong>What:</strong> Downsampling keeps every $M$-th sample, shrinking the image (or signal) by $M$.",
     "<strong>Spectral effect:</strong> the spectrum is <strong>stretched by M</strong> and $M$ shifted copies add together, so any content above $\\pi/M$ aliases into the baseband.",
     "<strong>Recipe:</strong> always apply an LPF with cutoff $\\pi/M$ first. This pair is called <strong>decimation</strong>."],
    r"$$y[n]=x[Mn],\qquad Y(\omega)=\frac1M\sum_{k=0}^{M-1}X\!\left(\frac{\omega-2\pi k}{M}\right)$$",
    "Shrinking a photo for a thumbnail: blur first, then discard pixels; discarding raw pixels gives jagged, sparkly edges.",
    "Dropping samples without the LPF is the textbook aliasing mistake. Also downsampling is NOT shift-invariant (time-varying)."))

CARDS.append(card(8, 5, "MULTI-RATE", "Upsampling by L (Interpolation)",
    [L(10, 40, 90, 40, 1.1)] + [L(14 + 20 * i, 40, 14 + 20 * i, 40 - h, 2) for i, h in enumerate([20, 28, 14, 24])] +
    [N(50, 56, "x[n]", 9, w="bold"), L(96, 40, 114, 40, 1.4, ar=True), N(105, 32, "↑L", 9),
     L(120, 40, 226, 40, 1.1)] + [L(124 + 8 * i, 40, 124 + 8 * i, 40 - h, 2) for i, h in
                                 [(0, 20), (3, 28), (6, 14), (9, 24)]] +
    [N(172, 56, "zero-stuffing (L=3)", 8.5), L(14, 98, 226, 98, 1.1),
     P("M14 78 C44 62 62 60 80 70 C100 82 110 76 130 74 C160 70 190 80 226 72", w=2, dash="6 3"),
     N(120, 120, "LPF (cutoff π/L, gain L) fills in the zeros", 8.5, w="bold"),
     N(120, 136, "X(ω) → X(Lω): L spectral images to remove", 8.5)],
    "Insert zeros, then low-pass to remove the spectral images and fill the gaps",
    ["<strong>What:</strong> To enlarge by $L$, insert $L-1$ zeros between samples (<strong>expansion</strong>), giving $x_e[n]=x[n/L]$ or 0.",
     "<strong>Spectral effect:</strong> the spectrum is <strong>compressed by L</strong> and $L$ copies (images) appear in $[0,2\\pi]$; the spectrum itself is X(Lω).",
     "<strong>Fix:</strong> an interpolation LPF with <strong>cutoff $\\pi/L$ and gain $L$</strong> keeps only the baseband copy and fills the zeros; a rational rate $L/M$ is upsample, filter, downsample."],
    r"$$x_e[n]=\begin{cases}x[n/L]&L\mid n\\0&\text{else}\end{cases},\qquad X_e(\omega)=X(L\omega),\qquad h_{\text{LPF}}:\ \text{cutoff }\pi/L,\ \text{gain }L$$",
    "Enlarging a stairway by adding blank steps between each real step, then sanding it into a smooth ramp.",
    "Forgetting the gain L makes the interpolated image too dark (zero-stuffing lowers the average by L). And zero-stuffing alone makes images, not a smooth upscale."))

CARDS.append(card(8, 6, "WORKED BENCHMARK", "Worked Benchmark: 90 Hz Sampled at 100 Hz",
    [L(20, 80, 224, 80, 1.3, ar=True)] + [L(20 + i * 40.8, 76, 20 + i * 40.8, 86, 1.2) for i in range(6)] +
    [N(20 + i * 40.8, 98, str(v), 8.5) for i, v in enumerate([0, 20, 40, 60, 80, 100])] +
    [N(222, 74, "Hz", 8.5, "end"),
     P("M193 70 C170 40 110 30 37 66", w=1.8, ar=True), C(193, 80, 3.5), C(37, 80, 3.5, "#ffffff"),
     N(193, 60, "90", 9, w="bold"), N(37, 56, "10", 9, w="bold"),
     N(120, 22, "fold about f_s/2 = 50 Hz", 9, w="bold"), N(120, 120, "f_alias = |90 − 100| = 10 Hz", 10, w="bold"), N(120, 136, "indistinguishable from a true 10 Hz tone", 8.5)],
    "A 90 Hz tone sampled at 100 Hz lands on 10 Hz after folding",
    ["A <strong>90 Hz</strong> cosine sampled at $f_s=100$ Hz has $f>f_s/2=50$ Hz, so it violates Nyquist.",
     "<strong>Fold it:</strong> $k=\\operatorname{round}(90/100)=1$, so $f_{\\text{alias}}=|90-100|=\\mathbf{10\\ Hz}$. The sampled sequence is <strong>identical</strong> to that of a 10 Hz cosine.",
     r"<strong>Image version:</strong> a sinusoidal grating at 0.8 cycles/pixel (above 0.5) aliases to $|0.8-1|=0.2$ cycles/pixel, visible as a coarse moiré band."],
    r"$$\cos(2\pi\cdot90\,\tfrac{n}{100})=\cos(2\pi\cdot(-10)\,\tfrac{n}{100})=\cos(2\pi\cdot10\,\tfrac{n}{100})$$",
    "A fan blade whirring at 90 rotations per camera-click-100: the camera only sees it nudge 10 steps per click.",
    "The alias frequency uses the NEAREST multiple of f_s, not always k = 1. For f = 160 at f_s = 100: |160 − 200| = 40 Hz, not 60."))

# ============================ 09 · DCT & KLT ============================
CARDS.append(card(9, 1, "TRANSFORM CODING", "DCT = DFT of a Mirror-Extended Signal",
    [L(14, 54, 226, 54, 1, d="2 3"), _poly([(20, 74), (80, 34), (80, 74), (140, 34), (140, 74), (200, 34), (200, 74)], 2),
     L(80, 34, 80, 74, 1.2, d="3 3"), L(140, 34, 140, 74, 1.2, d="3 3"),
     N(120, 20, "DFT: periodic copy → JUMPS", 9, w="bold"),
     _poly([(20, 130), (80, 96), (140, 130), (200, 96), (260, 130)][:4] + [(200, 96)], 2),
     N(120, 144, "DCT: mirror extension → continuous", 9, w="bold")],
    "The periodic extension (top) jumps at the seams; the even extension (bottom) is continuous there",
    ["<strong>What:</strong> The DCT-II treats the block as if it were <strong>mirrored</strong> at its ends, then takes a DFT of that even-symmetric extension, so only cosines remain.",
     "<strong>Why it matters:</strong> A plain DFT assumes the block repeats, creating a <strong>boundary jump</strong> that leaks energy across all frequencies; mirroring removes the jump.",
     "<strong>Result:</strong> <strong>real</strong> coefficients with far better energy compaction at block edges, which is why JPEG uses it."],
    r"$$C(u)=\alpha(u)\sum_{x=0}^{N-1}f(x)\cos\!\left[\frac{(2x+1)u\pi}{2N}\right],\quad \alpha(0)=\sqrt{\tfrac1N},\ \alpha(u>0)=\sqrt{\tfrac2N}$$",
    "Hanging a banner: tiled copies leave a visible seam, but a mirrored print has no seam at the join.",
    "The DCT is NOT the real part of the DFT. It is a different (half-sample-shifted, even-extension) transform with the factor (2x+1)/2N."))

def _zig(n=8, x0=16, y0=14, s=13):
    pts, r, c, d = [], 0, 0, 1
    for _ in range(n * n):
        pts.append((x0 + c * s + s / 2, y0 + r * s + s / 2))
        nr, nc = r - d, c + d
        if 0 <= nr < n and 0 <= nc < n: r, c = nr, nc
        else:
            if d == 1: r, c = (r, c + 1) if c + 1 < n else (r + 1, c)
            else: r, c = (r + 1, c) if r + 1 < n else (r, c + 1)
            d = -d
    return pts

CARDS.append(card(9, 2, "TRANSFORM CODING", "Energy Compaction & the JPEG Zig-Zag",
    [PG(f"16,14 16,{14+13*4} {16+13*4},14", "#e2e8f0", 0)] + [L(16 + i * 13, 14, 16 + i * 13, 118, 0.6) for i in range(9)] + [L(16, 14 + i * 13, 120, 14 + i * 13, 0.6) for i in range(9)] +
    [R(16, 14, 104, 104, "none", 1.6), _poly(_zig()[:34], 1.4),
     N(146, 24, "DC", 9, "start", w="bold"), L(142, 22, 126, 18, 1.2, ar=True),
     N(146, 52, "low freq → large", 8.5, "start"), N(146, 66, "high freq → ≈ 0", 8.5, "start"),
     N(146, 86, "quantize, then", 8.5, "start"), N(146, 98, "zig-zag → long", 8.5, "start"), N(146, 110, "zero runs (RLE)", 8.5, "start")],
    "Most energy sits in the top-left; the zig-zag scan lines the small coefficients up at the end",
    ["<strong>What:</strong> Natural image blocks are smooth, so after the 8×8 DCT <strong>nearly all the energy lands in a few low-frequency coefficients</strong> (top-left, with DC the block average).",
     "<strong>How (JPEG):</strong> transform each 8×8 block, <strong>divide by a quantization table</strong> (big divisors at high frequencies, rounding to integers), then scan in zig-zag order.",
     "<strong>Why:</strong> Quantization zeros the weak high frequencies, so the zig-zag creates <strong>long runs of zeros</strong> that run-length and entropy coding squeeze efficiently. Quantization is the only lossy step."],
    r"$$\hat C(u,v)=\operatorname{round}\!\left[\frac{C(u,v)}{Q(u,v)}\right],\qquad \text{lossy step} = \text{quantization}$$",
    "Packing a suitcase by weight: keep the few heavy items (low-frequency energy) and let the lint (high-frequency detail) fall away.",
    "Compression loss comes ONLY from quantization, not from the DCT itself (it is invertible). Also DC is coded differentially across blocks."))

def _basis():
    out = []
    s = 40
    for i in range(3):
        for j in range(3):
            x0, y0 = 14 + j * 46, 14 + i * 40
            out.append(R(x0, y0, 38, 34, "#ffffff", 1.2))
            for k in range(1, i + 1):
                out.append(L(x0, y0 + k * 34 / (i + 1), x0 + 38, y0 + k * 34 / (i + 1), 1.6))
            for k in range(1, j + 1):
                out.append(L(x0 + k * 38 / (j + 1), y0, x0 + k * 38 / (j + 1), y0 + 34, 1.6))
    return out

CARDS.append(card(9, 3, "TRANSFORM CODING", "2-D DCT Basis Images",
    _basis() + [N(186, 40, "tile (u,v):", 8.5, "start", "bold"), N(186, 54, "u = vertical,", 8.5, "start"), N(186, 66, "v = horizontal", 8.5, "start"),
                N(186, 84, "separable:", 8.5, "start", "bold"), N(186, 98, "C = A f Aᵀ", 9, "start"), N(186, 114, "A orthonormal", 8.5, "start")],
    "Each tile is one 2D cosine: more bars mean a higher frequency",
    ["The 2D DCT writes a block as a <strong>weighted sum of 64 fixed cosine patterns</strong> $\\cos\\frac{(2x+1)u\\pi}{2N}\\cos\\frac{(2y+1)v\\pi}{2N}$.",
     "It is <strong>separable and orthonormal</strong>: $C=AfA^{T}$ with $A$ an orthogonal matrix, so the inverse is simply $f=A^{T}CA$ and <strong>energy is preserved</strong> (Parseval).",
     "Top-left patterns are smooth gradients, bottom-right ones are fine checkerboards, so <strong>frequency tells you scale of detail</strong>."],
    r"$$C=A\,f\,A^{T},\quad f=A^{T}CA,\quad A A^{T}=I,\qquad \sum f^2=\sum C^2$$",
    "A set of 64 stencil patterns: any 8×8 patch of the picture is a recipe of 'a bit of stencil 1, a lot of stencil 7, ...'.",
    "Orthonormality means A⁻¹ = Aᵀ, so DCT inversion needs no matrix inverse. Without the α(u) scale factors the matrix is NOT orthonormal."))

CARDS.append(card(9, 4, "KLT / PCA", "KLT: Eigenvectors of the Covariance",
    [L(120, 72, 120, 10, 0.8, d="2 3"), L(120, 72, 120, 134, 0.8, d="2 3"), L(20, 72, 222, 72, 0.8, d="2 3"),
     E(120, 72, 78, 28, -40, "#f1f5f9", 1.8), L(120, 72, 176, 18, 2, ar=True), L(120, 72, 98, 94, 1.8, ar=True),
     N(184, 16, "φ₁ (λ₁ big)", 9, "start", "bold"), N(70, 108, "φ₂ (λ₂ small)", 8.5, "end"),
     N(22, 24, "x₁", 9), N(224, 66, "x₂", 9), N(16, 134, "data cloud, mean removed", 8, "start")],
    "The KLT rotates axes to the principal directions of the cloud, decorrelating the coordinates",
    ["<strong>What:</strong> Treat pixels (or blocks) as random vectors; the <strong>KLT/PCA</strong> basis is the set of eigenvectors of their covariance matrix $C_x$.",
     "<strong>How:</strong> Coefficients $y=\\Phi^{T}(x-\\mu)$ have a <strong>diagonal covariance</strong> $\\Lambda$ (decorrelated) and the largest variances come first.",
     "<strong>Why:</strong> Keeping the top $k$ coefficients minimizes mean-squared reconstruction error among all linear orthonormal transforms. But it depends on the data and has no fast algorithm."],
    r"$$C_x\,\varphi_i=\lambda_i\varphi_i,\quad y=\Phi^{T}(x-\mu),\quad C_y=\Lambda,\quad \text{MSE}_k=\sum_{i>k}\lambda_i$$",
    "Standing the long axis of a cigar-shaped crowd along your measuring stick: the first number tells you most about where each person is.",
    "KLT is data-dependent: the decoder must also know the basis (extra overhead), unlike the DCT's fixed basis. Always subtract the mean first."))

CARDS.append(card(9, 5, "KLT / PCA", "DCT Approximates the KLT for Markov-1 Images",
    [GRID(14, 18, [["1", "ρ", "ρ²", "ρ³"], ["ρ", "1", "ρ", "ρ²"], ["ρ²", "ρ", "1", "ρ"], ["ρ³", "ρ²", "ρ", "1"]], cell=26, shade={(i, i) for i in range(4)}),
     N(66, 130, "C = [ρ^|i−j|]  (Toeplitz)", 8.5), L(124, 66, 148, 66, 1.4, ar=True), N(136, 58, "eig", 8),
     P("M156 72 Q170 24 184 72 T212 72", w=2), P("M156 96 Q166 70 176 96 T196 96 T216 96", w=1.6, dash="4 3"),
     N(186, 114, "cosine-like", 8.5), N(186, 128, "eigenvectors as ρ → 1", 8.5)],
    "For highly correlated neighbors, the KLT eigenvectors look like DCT cosines",
    [r"Model image rows as a <strong>first-order Markov</strong> process: neighboring pixels correlate as $C_{ij}=\rho^{|i-j|}$ with $\rho$ near 1 (typical of natural images, ≈ 0.9–0.95).",
     "For such a Toeplitz covariance, <strong>the eigenvectors are nearly DCT basis vectors</strong>, so the DCT is nearly the optimal KLT but data-independent.",
     "This is the engineering argument for DCT in JPEG/MPEG: <strong>near-KLT performance with a fixed basis and a fast algorithm</strong>."],
    r"$$C=\big[\rho^{|i-j|}\big],\qquad \rho\to1\ \Longrightarrow\ \Phi_{\text{KLT}}\approx A_{\text{DCT}}$$",
    "A dependable tailor who cuts a standard pattern that nearly fits everyone, instead of custom-measuring each customer.",
    "The match is approximate and holds for high ρ. For low-correlation data (noise-like) the DCT is no better than any other transform."))

CARDS.append(card(9, 6, "WORKED BENCHMARK", "Worked Benchmark: 2-Point KLT",
    [R(14, 18, 80, 56, "#f1f5f9", 1.6), N(54, 42, "C = [2 1; 1 2]", 10, w="bold"), N(54, 60, "λ = 3, 1", 9),
     N(120, 40, "φ₁ = (1,1)/√2", 9, "start"), N(120, 56, "φ₂ = (1,−1)/√2", 9, "start"),
     L(16, 126, 224, 126, 1.2), R(40, 126 - 40, 24, 40, "#f1f5f9", 1.5), R(72, 126 - 40, 24, 40, "#f1f5f9", 1.5), N(68, 140, "before (2, 2)", 8),
     L(106, 100, 128, 100, 1.4, ar=True),
     R(142, 126 - 60, 24, 60, "#e2e8f0", 1.5), R(174, 126 - 20, 24, 20, "#ffffff", 1.5), N(170, 140, "after (3, 1)", 8),
     N(210, 100, "75%", 9, "start", "bold"), N(210, 112, "in 1 coeff", 8, "start")],
    "The same 45° rotation is both the KLT and the 2-point DCT/Haar; variance (2,2) → (3,1)",
    ["<strong>Covariance</strong> $C=\\begin{pmatrix}2&1\\\\1&2\\end{pmatrix}$ has eigenvalues $\\lambda=3,1$ (characteristic polynomial $(2-\\lambda)^2-1=0$).",
     "<strong>Eigenvectors</strong> are $\\varphi_1=(1,1)/\\sqrt2$ (the average) and $\\varphi_2=(1,-1)/\\sqrt2$ (the difference), exactly the <strong>2-point DCT/Haar</strong> basis.",
     "Energy goes from an even (2, 2) split to <strong>(3, 1)</strong>: the first coefficient carries <strong>75%</strong> of the variance, so you could code it alone with 25% energy loss."],
    r"$$\det(C-\lambda I)=0\ \Rightarrow\ \lambda\in\{3,1\},\qquad y_1=\tfrac{x_1+x_2}{\sqrt2},\ y_2=\tfrac{x_1-x_2}{\sqrt2}$$",
    "Two well-matched twins: their sum is big and informative, their difference is small and boring, so you mostly keep the sum.",
    "Eigenvalues sum to the trace: 3 + 1 = 4 = 2 + 2, so total variance is preserved. If your eigenvalues don't add up to the trace, you made an error."))
