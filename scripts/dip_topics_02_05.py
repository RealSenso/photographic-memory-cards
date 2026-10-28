import math
from dip_lib import *

CARDS = []

# ============================ 02 · COLOR THEORY ============================
CARDS.append(card(2, 1, "COLOR VISION", "Trichromacy & Grassmann's Laws",
    [AX(20, 125, 225, 14),
     P("M32 125 Q72 22 112 125", w=2), P("M88 125 Q128 22 168 125", w=2, dash="5 3"), P("M110 125 Q150 22 190 125", w=2, dash="2 2"),
     T(72, 38, "S", 11, w="bold"), T(128, 38, "M", 11, w="bold"), T(150, 20, "L", 11, w="bold"),
     N(122, 139, "wavelength λ (nm)", 8), N(20, 12, "cone response", 8, "start")],
    "Three overlapping cone sensitivities (S, M, L): every color becomes just 3 numbers",
    ["Human vision has only <strong>three cone types (L, M, S)</strong>, so any light, however complex its spectrum, is reduced to 3 numbers.",
     r"<strong>Grassmann's laws</strong> make matching linear: scaling ($\alpha C_1 \equiv \alpha C_2$) and additivity ($C_1 + C_3 \equiv C_2 + C_3$) both preserve a perceptual match.",
     "Because matching is linear, all color-space conversions are <strong>3×3 matrix multiplications</strong>, and different spectra can look identical (metamers)."],
    r"$$C \equiv R\,\mathbf{R} + G\,\mathbf{G} + B\,\mathbf{B}, \qquad \alpha C_1 \equiv \alpha C_2,\quad C_1 + C_3 \equiv C_2 + C_3$$",
    "Three radio dials that mix into any station's sound: you never need the full waveform, only where the three dials sit.",
    "Metamers are different spectra with the SAME tristimulus values. Matching is about cone responses, not spectral equality."))

def _bell(c, w, h=100, base=125, n=0):
    return f"M{c-w} {base} Q{c} {base-h*2} {c+w} {base}"

CARDS.append(card(2, 2, "COLORIMETRY", "CIE XYZ & Tristimulus Integrals",
    [AX(20, 125, 225, 14),
     P("M28 125 Q55 35 92 125", w=1.8, dash="2 2"),
     P("M62 125 Q122 -8 190 125", w=2.6),
     P("M82 125 Q96 72 112 88 Q132 66 150 74 Q170 80 186 125", w=1.8, dash="6 3"),
     T(58, 62, "z̄", 11, w="bold"), T(124, 24, "ȳ", 11, w="bold"), T(176, 74, "x̄", 11, w="bold"),
     N(122, 139, "wavelength λ", 8)],
    "x̄(λ), ȳ(λ), z̄(λ): all non-negative; ȳ is also the luminance curve",
    ["The CIE 1931 RGB experiment needed <strong>negative red</strong> to match cyan-greens, so CIE invented <strong>imaginary primaries X, Y, Z</strong> whose matching functions are all ≥ 0.",
     r"A light with spectrum $P(\lambda)$ gets tristimulus values by integrating it against each matching function, so <strong>X, Y, Z are just 3 inner products</strong> with $P$.",
     r"$\bar{y}(\lambda)$ was chosen to equal the eye's luminous efficiency, so <strong>Y alone is brightness</strong>."],
    r"$$X=\int P(\lambda)\bar{x}(\lambda)\,d\lambda,\quad Y=\int P(\lambda)\bar{y}(\lambda)\,d\lambda,\quad Z=\int P(\lambda)\bar{z}(\lambda)\,d\lambda$$",
    "Three different microphones listening to the same sound: each reports one number, and together they pin down how the sound lands on your ear.",
    "X, Y, Z are not physical colors; no real light is the 'Z primary'. Do not plot them as colors, only as coordinates."))

CARDS.append(card(2, 3, "COLORIMETRY", "Chromaticity Diagram (x, y)",
    [L(26, 130, 224, 130, 1.2, ar=True), L(26, 130, 26, 10, 1.2, ar=True),
     P("M62 126 C38 72 52 30 86 22 C118 14 152 46 192 108 Z", fill="#f1f5f9", w=2),
     PG("186,106 82,28 66,118", fill="none", w=1.4, d="4 3"),
     C(112, 80, 3.5), T(124, 84, "W", 10, "start", w="bold"),
     N(86, 15, "520 nm", 7.5), N(204, 118, "700 nm", 7.5), N(48, 136, "380", 7.5),
     N(215, 140, "x", 9), N(14, 18, "y", 9), N(150, 70, "gamut", 8)],
    "Spectral locus (horseshoe), white point W, and a dashed RGB gamut triangle",
    [r"Divide out brightness: <strong>$x = X/(X+Y+Z)$, $y = Y/(X+Y+Z)$</strong>, leaving a 2D map of pure hue and saturation.",
     "The <strong>horseshoe curve (spectral locus)</strong> holds fully saturated monochromatic lights; the straight bottom edge holds purples; white sits near the middle.",
     "A display with three primaries can only make colors <strong>inside the triangle</strong> joining them, which is its gamut."],
    r"$$x=\frac{X}{X+Y+Z},\quad y=\frac{Y}{X+Y+Z},\quad z=1-x-y$$",
    "A map projected from above: you lose altitude (brightness) but keep every landmark's position (hue and saturation).",
    "The (x, y) diagram has NO brightness, so a point is not one color. Also mixing two colors lands on the straight line between them, not a curve."))

CARDS.append(card(2, 4, "COLOR SPACES", "RGB → YCbCr and Chroma Subsampling",
    [R(14, 20, 24, 20), R(14, 62, 24, 20), R(14, 104, 24, 20),
     N(26, 34, "R", 10, w="bold"), N(26, 76, "G", 10, w="bold"), N(26, 118, "B", 10, w="bold"),
     R(70, 38, 44, 68, "#f1f5f9", 1.8), N(92, 74, "3×3", 10, w="bold"), N(92, 88, "matrix", 8),
     L(40, 30, 68, 58, 1.3, ar=True), L(40, 72, 68, 72, 1.3, ar=True), L(40, 114, 68, 86, 1.3, ar=True),
     R(150, 14, 64, 40, "#ffffff", 1.8), N(182, 38, "Y  (full res)", 9, w="bold"),
     R(150, 66, 30, 22, "#f1f5f9", 1.5), N(165, 81, "Cb", 9),
     R(184, 66, 30, 22, "#f1f5f9", 1.5), N(199, 81, "Cr", 9),
     N(182, 104, "Cb, Cr stored at", 8), N(182, 116, "¼ the pixels (4:2:0)", 8),
     L(116, 58, 146, 34, 1.3, ar=True), L(116, 76, 146, 76, 1.3, ar=True)],
    "Luma stays full resolution; the chroma planes are subsampled because the eye is less sensitive to them",
    ["<strong>What:</strong> YCbCr separates brightness <strong>Y</strong> from two color-difference signals <strong>Cb</strong> (blue minus luma) and <strong>Cr</strong> (red minus luma).",
     "<strong>How:</strong> A fixed 3×3 matrix (Rec. 601 weights 0.299, 0.587, 0.114 for R, G, B) turns RGB into Y, Cb, Cr, with +128 added to Cb and Cr for 8-bit storage.",
     "<strong>Why:</strong> Human vision resolves luminance detail much better than color detail, so JPEG/video halve or quarter the chroma planes (4:2:2, 4:2:0) with little visible loss."],
    r"$$\begin{pmatrix}Y\\C_b\\C_r\end{pmatrix}=\begin{pmatrix}0.299&0.587&0.114\\-0.1687&-0.3313&0.5\\0.5&-0.4187&-0.0813\end{pmatrix}\begin{pmatrix}R\\G\\B\end{pmatrix}$$",
    "A photo editor keeping the sharp black-and-white drawing but letting the watercolor wash be blurry: your eye forgives the wash, not the lines.",
    "Subsampling is applied to Cb and Cr only, never to Y. Also Y in Rec. 601 weights green most (0.587), not (R+G+B)/3."))

CARDS.append(card(2, 5, "COLOR SPACES", "HSI / HSV: Hue, Saturation, Intensity",
    [C(78, 74, 52, "#ffffff", 1.8), C(78, 74, 2.5),
     L(78, 74, 130, 74, 1.4, d="3 3"), L(78, 74, 108, 52, 1.8, ar=True), C(108, 52, 3.5),
     P("M104 74 A26 26 0 0 0 100 62", w=1.3), N(112, 70, "H", 10, "start", w="bold"),
     N(98, 58, "S", 9, "end", w="bold"), N(142, 78, "red", 8),
     PG("196,12 170,74 196,136 222,74", "#f1f5f9", 1.6), L(196, 12, 196, 136, 1.2, d="3 3"),
     N(196, 8, "I", 9, w="bold"), N(196, 76, "S", 9)],
    "Hue = angle around the circle, Saturation = distance from the gray axis, Intensity = height",
    [r"<strong>Hue $H$</strong> is the angle on the color wheel (which pure color), <strong>Saturation $S$</strong> is how far from gray (how pure), <strong>Intensity $I$</strong> is how bright.",
     r"The formulas: $I=\frac{R+G+B}{3}$, $S = 1-\frac{3\min(R,G,B)}{R+G+B}$, and $H$ comes from the angle $\theta=\cos^{-1}\!\big(\frac{\tfrac12[(R-G)+(R-B)]}{\sqrt{(R-G)^2+(R-B)(G-B)}}\big)$.",
     "It matches how people name colors, so you can <strong>change brightness without shifting hue</strong>, handy for equalizing only I."],
    r"$$I=\frac{R+G+B}{3},\quad S=1-\frac{3\min(R,G,B)}{R+G+B},\quad H=\begin{cases}\theta & B\le G\\ 360^\circ-\theta & B>G\end{cases}$$",
    "A paint-mixing wheel: pick the pigment (hue), decide how pale (saturation), then choose how much light is on the canvas (intensity).",
    "When S = 0 (gray, R=G=B) the hue is UNDEFINED, and when I = 0 saturation is undefined. Do not treat H = 0 as red in these cases."))

CARDS.append(card(2, 6, "WORKED BENCHMARK", "Worked Benchmark: Pure Red → YCbCr",
    [L(30, 120, 222, 120, 1.2),
     R(48, 120 - 30, 30, 30, "#f1f5f9", 1.6), R(104, 120 - 34, 30, 34, "#f1f5f9", 1.6), R(160, 120 - 102, 30, 102, "#f1f5f9", 1.6),
     N(63, 134, "Y", 10, w="bold"), N(119, 134, "Cb", 10, w="bold"), N(175, 134, "Cr", 10, w="bold"),
     N(63, 86, "76.2", 9), N(119, 82, "85", 9), N(175, 14, "255", 9),
     N(130, 144, "stored values (Cb, Cr include +128)", 7.5)],
    "(R,G,B) = (255, 0, 0): luma ≈ 76, Cb ≈ −43 + 128 = 85, Cr = 127.5 + 128 → clipped to 255",
    ["Plug red into the Rec. 601 rows: <strong>$Y = 0.299\\cdot 255 \\approx 76.2$</strong>, so pure red is fairly dark in luminance.",
     r"<strong>$C_b = -0.1687\cdot255 \approx -43$</strong> (red has little blue, so Cb is below neutral) and <strong>$C_r = 0.5\cdot255 = 127.5$</strong> (the maximum red excess).",
     "After the 8-bit +128 offset, Cb ≈ 85 and Cr ≈ 255 (clipped from 255.5), so <strong>red lives at maximum Cr and low Y</strong>."],
    r"$$Y=0.299(255)=76.2,\quad C_b=-0.1687(255)=-43.0,\quad C_r=0.5(255)=127.5$$",
    "Red is a loud but dim voice: it has huge 'red-ness' (Cr) yet contributes little to overall luminance.",
    "Forgetting the +128 offset makes Cb and Cr look negative. They are stored as unsigned bytes centered at 128."))

# ============================ 03 · HISTOGRAMS & OTSU ============================
CARDS.append(card(3, 1, "HISTOGRAMS", "Image Histogram: What It Hides",
    [AX(20, 125, 225, 14), BARS(30, 125, [96, 70, 48, 30, 20, 10, 6, 2], bw=20, gap=4, scale=0.95),
     N(122, 139, "gray level r_k  (0 … L−1)", 8), N(18, 12, "p(r_k)", 8, "start"), N(118, 22, "dark image: mass piled at left", 8.5)],
    "p(r_k) = n_k / MN: a dark image has its histogram piled against the left wall",
    [r"The <strong>histogram</strong> counts how many pixels have each gray level, $h(r_k)=n_k$; dividing by $MN$ gives the probability $p(r_k)=n_k/MN$.",
     "Its <strong>shape reveals exposure and contrast</strong>: mass at left means dark, at right means bright, a narrow bump means low contrast, two bumps suggest object plus background.",
     "It <strong>discards all spatial information</strong>: every rearrangement of the same pixels gives the same histogram."],
    r"$$p(r_k)=\frac{n_k}{MN},\qquad \sum_{k=0}^{L-1}p(r_k)=1$$",
    "A grade distribution for the class: you can tell if the exam was hard, but not which student sits where.",
    "Two completely different images can share one histogram. Never use the histogram alone to claim two images are the same."))

CARDS.append(card(3, 2, "POINT OPERATIONS", "Point Operations: s = T(r)",
    [L(40, 125, 40, 18, 1.2, ar=True), L(40, 125, 140, 125, 1.2, ar=True),
     L(40, 125, 130, 35, 1.2, d="4 3"), P("M40 125 Q52 48 130 35", w=2), L(40, 35, 130, 125, 1.8),
     N(86, 138, "input r", 8), N(32, 20, "s", 9), N(122, 52, "γ<1", 8.5, "start"), N(70, 112, "negative", 8.5, "start"),
     N(186, 40, "s = c·r^γ", 9), N(186, 58, "γ<1 brightens", 8), N(186, 72, "γ>1 darkens", 8),
     N(186, 94, "s = c·log(1+r)", 9), N(186, 108, "expands darks", 8)],
    "Identity (dashed), gamma brightening (curve), negative (down-sloping line)",
    ["A <strong>point operation</strong> maps every pixel through the same function $s=T(r)$, ignoring its neighbors.",
     r"<strong>Negative</strong> $s=L-1-r$, <strong>log</strong> $s=c\log(1+r)$ stretches dark detail, and <strong>power-law (gamma)</strong> $s=c\,r^{\gamma}$ brightens ($\gamma<1$) or darkens ($\gamma>1$).",
     "<strong>Contrast stretching</strong> uses a piecewise-linear $T$ to spread a narrow gray range across the full scale."],
    r"$$s=T(r),\quad s=c\,r^{\gamma},\quad s=c\log(1+r),\quad s=\frac{r-r_{\min}}{r_{\max}-r_{\min}}(L-1)$$",
    "A tone-curve slider in a photo app: every pixel is pushed through the same dial, and the shape of the curve decides who gets brighter.",
    "Normalize r to [0, 1] before applying a gamma, or c must absorb the (L−1)^(1−γ) scale. Also a point operation can never recover detail already clipped to one level."))

def _gauss(c, s, a, base=125, x0=20, x1=225):
    pts = []
    for x in range(x0, x1 + 1, 5):
        y = base - a * math.exp(-((x - c) ** 2) / (2 * s * s))
        pts.append(f"{x},{y:.1f}")
    return "M" + " L".join(pts)

CARDS.append(card(3, 3, "THRESHOLDING", "Global Thresholding on a Bimodal Histogram",
    [AX(20, 125, 225, 14), P(_gauss(75, 18, 80), "#f1f5f9", 1.8), P(_gauss(165, 20, 62), "#ffffff", 1.8),
     L(118, 125, 118, 22, 1.8, d="5 3"), N(118, 17, "T", 10, w="bold"),
     N(75, 40, "background", 8.5), N(168, 56, "object", 8.5), N(122, 139, "gray level", 8)],
    "Two humps with a valley between them: the threshold T sits in the valley",
    ["If an image is <strong>object + background</strong>, its histogram usually has two humps; any T in the valley separates them.",
     r"The mapping is $g(x,y)=1$ if $f(x,y)>T$ and $0$ otherwise, producing a <strong>binary mask</strong>.",
     "The <strong>iterative method</strong> starts at the global mean, averages the two class means, and repeats $T\\leftarrow\\tfrac12(\\mu_1+\\mu_2)$ until it stops moving."],
    r"$$g(x,y)=\begin{cases}1 & f(x,y)>T\\0 & f(x,y)\le T\end{cases},\qquad T_{k+1}=\tfrac12(\mu_1(T_k)+\mu_2(T_k))$$",
    "Drawing a waterline across two islands: set it in the channel between them and the islands separate cleanly.",
    "A single global T fails under uneven illumination (shadow across the page). Use local or adaptive thresholds there."))

CARDS.append(card(3, 4, "THRESHOLDING", "Otsu: Maximize Between-Class Variance",
    [AX(20, 125, 225, 14), P(_gauss(70, 17, 78), "#e2e8f0", 1.8), P(_gauss(165, 20, 60), "#ffffff", 1.8),
     L(118, 125, 118, 30, 1.6, d="5 3"), L(70, 128, 70, 120, 2), L(165, 128, 165, 120, 2),
     L(72, 110, 163, 110, 1.4, ar=True), L(163, 110, 72, 110, 1.4, ar=True),
     T(70, 138, "μ₀", 10), T(165, 138, "μ₁", 10), N(118, 105, "μ₁ − μ₀", 8.5), N(118, 22, "k*", 10, w="bold")],
    "Otsu picks the threshold that pushes the two class means as far apart as possible",
    ["Split the histogram at a trial level $k$ into class 0 (≤ k) and class 1 (> k) with probabilities $\\omega_0,\\omega_1$ and means $\\mu_0,\\mu_1$.",
     r"<strong>Between-class variance</strong> $\sigma_B^2(k)=\omega_0\omega_1(\mu_0-\mu_1)^2$ is large when the classes are well separated and balanced.",
     "Since total variance is fixed, <strong>maximizing $\\sigma_B^2$ is the same as minimizing the within-class variance</strong>. Pick $k^*$ with the largest value."],
    r"$$k^*=\arg\max_k\ \sigma_B^2(k),\qquad \sigma_B^2(k)=\omega_0(k)\,\omega_1(k)\,\big[\mu_0(k)-\mu_1(k)\big]^2$$",
    "Choosing where to cut a rope so the two halves hang as differently as possible: a clean cut leaves two distinct clumps.",
    "Otsu assumes roughly two classes of comparable size. With one tiny object on a big background, or a unimodal histogram, it gives a bad threshold."))

CARDS.append(card(3, 5, "THRESHOLDING", "Computing Otsu with Cumulative Sums",
    [AX(20, 125, 225, 14), P("M25 118 C60 114 72 44 100 40 L140 40 C170 44 182 114 215 118", w=2),
     L(120, 125, 120, 40, 1.4, d="4 3"), N(120, 30, "k*", 10, w="bold"), N(120, 138, "k", 9),
     N(120, 78, "plateau: ties across the gap", 8), N(28, 12, "σ_B²(k)", 8.5, "start"),
     C(100, 40, 3), C(140, 40, 3)],
    "σ_B²(k) rises, flat-tops across empty bins, then falls; take the middle of the plateau",
    [r"Precompute cumulative <strong>$\omega(k)=\sum_{i\le k}p_i$</strong> and <strong>$\mu(k)=\sum_{i\le k}i\,p_i$</strong>, with total mean $\mu_T=\mu(L-1)$.",
     r"Then $\sigma_B^2(k)=\dfrac{[\mu_T\omega(k)-\mu(k)]^2}{\omega(k)[1-\omega(k)]}$ costs only <strong>O(L)</strong>: one pass over the histogram.",
     "If several $k$ tie (empty histogram bins between modes), <strong>average the tied $k$ values</strong> to get the threshold."],
    r"$$\sigma_B^2(k)=\frac{\big[\mu_T\,\omega(k)-\mu(k)\big]^2}{\omega(k)\,[1-\omega(k)]},\quad k^*=\arg\max_k\sigma_B^2(k)$$",
    "Walking along a ridge: you do not rebuild the hill at each step, you just update running totals as you move.",
    "Divide-by-zero at ω(k) = 0 or 1: skip those k. And report the middle of a plateau, not just the first maximum."))

CARDS.append(card(3, 6, "WORKED BENCHMARK", "Worked Benchmark: Otsu on a 10-Pixel Histogram",
    [L(22, 125, 224, 125, 1.2)] +
    [R(30 + i * 24, 125 - n * 20, 18, n * 20, "#f1f5f9" if i < 3 else "#ffffff", 1.4) for i, n in enumerate([0, 4, 1, 0, 0, 0, 2, 3]) if n] +
    [N(39 + i * 24, 138, str(i), 8.5) for i in range(8)] +
    [N(39 + i * 24, 125 - n * 20 - 4, str(n), 8.5) for i, n in enumerate([0, 4, 1, 0, 0, 0, 2, 3]) if n] +
    [L(100, 125, 100, 30, 1.6, d="5 3"), N(100, 24, "T ∈ [2, 5]", 9, w="bold"),
     N(60, 40, "ω₀ = 0.5, μ₀ = 1.2", 8.5), N(184, 40, "ω₁ = 0.5, μ₁ = 6.6", 8.5)],
    "Counts at levels 1, 2, 6, 7 are 4, 1, 2, 3: the best split is any k in 2…5 with σ_B² = 7.29",
    ["Ten pixels: <strong>level 1 ×4, level 2 ×1, level 6 ×2, level 7 ×3</strong>, so $\\mu_T = (4+2+12+21)/10 = 3.9$.",
     r"Split at $k=2$: $\omega_0=0.5,\ \mu_0=1.2$ and $\omega_1=0.5,\ \mu_1=6.6$, giving $\sigma_B^2 = 0.25(5.4)^2 = \mathbf{7.29}$. At $k=1$ it is only 5.6 and at $k=6$ only 4.1.",
     "Levels 3, 4, 5 are empty, so $k=2,3,4,5$ all tie at 7.29: <strong>Otsu returns any value in the gap; take the middle (≈ 3.5)</strong>."],
    r"$$\sigma_B^2(2)=0.5\cdot0.5\,(6.6-1.2)^2=7.29,\quad \sigma_B^2(1)\approx5.6,\ \sigma_B^2(6)\approx4.1$$",
    "Two clumps of people far apart in a field: any fence put in the empty middle separates them equally well.",
    "Reporting the first argmax (k=2) can misclassify future pixels near the gap. State the plateau and pick its midpoint."))

# ============================ 04 · BINARY MORPHOLOGY ============================
CARDS.append(card(4, 1, "MORPHOLOGY", "Erosion A ⊖ B",
    [R(30, 24, 112, 88, "#f1f5f9", 1.8, 6), R(50, 44, 72, 48, "#ffffff", 1.6, 2, "5 3"),
     R(32, 26, 20, 20, "#ffffff", 1.4, 0), N(42, 40, "B", 9, w="bold"),
     N(86, 72, "A ⊖ B", 10, w="bold"), N(86, 16, "A (object)", 9),
     N(188, 40, "A ⊖ B = {z : B_z ⊆ A}", 8.5), N(188, 58, "B slides inside A;", 8.5), N(188, 70, "its center marks", 8.5), N(188, 82, "the survivors", 8.5)],
    "The dashed inner region is where the structuring element B still fits entirely inside A",
    ["<strong>What:</strong> A <strong>structuring element</strong> B (a small probe) is slid over the image; erosion keeps only positions where B fits <strong>completely inside</strong> the object.",
     "<strong>How:</strong> The output is the set of B's center points that satisfy $B_z\\subseteq A$, so object boundaries <strong>shrink inward</strong> by the radius of B.",
     "<strong>Why:</strong> It deletes specks smaller than B, separates thinly joined blobs, and shrinks everything else."],
    r"$$A\ominus B=\{z\mid (B)_z\subseteq A\}=\bigcap_{b\in B}A_{-b}$$",
    "A cookie cutter you may only press where it fits entirely inside the dough: edges and thin strands of dough get lost.",
    "Erosion shrinks ALL objects, not just noise. Also if B's origin is not at its center, the result is shifted. Check the origin convention."))

CARDS.append(card(4, 2, "MORPHOLOGY", "Dilation A ⊕ B and Duality",
    [R(62, 44, 60, 40, "#f1f5f9", 1.8, 4), R(44, 26, 96, 76, "#ffffff", 1.6, 8, "5 3"),
     N(92, 68, "A", 11, w="bold"), N(92, 18, "A ⊕ B", 10, w="bold"),
     R(40, 22, 14, 14, "#f1f5f9", 1.4, 0), N(47, 33, "B", 8, w="bold"),
     N(188, 40, "A ⊕ B = ∪ A_b", 8.5), N(188, 58, "(A ⊖ B)ᶜ = Aᶜ ⊕ B̂", 8.5), N(188, 78, "grows, bridges gaps", 8.5)],
    "Dilation grows A outward by B (dashed outline); it is the dual of erosion on the complement",
    ["<strong>What:</strong> Dilation <strong>adds</strong> B at every object pixel, so objects <strong>grow</strong> and small gaps and holes close.",
     r"<strong>How:</strong> $A\oplus B=\bigcup_{b\in B}A_b$, the union of A translated by every point of B.",
     r"<strong>Why:</strong> It is the <strong>dual</strong> of erosion, $(A\ominus B)^c=A^c\oplus\hat B$ (reflected B), so every erosion fact has a dilation twin."],
    r"$$A\oplus B=\{z\mid (\hat B)_z\cap A\ne\emptyset\}=\bigcup_{b\in B}A_b,\qquad (A\ominus B)^c=A^c\oplus\hat B$$",
    "Spreading ink on wet paper: every dot blooms to the size of the brush, merging dots that were close.",
    "Erosion and dilation are NOT inverses: erode then dilate does not always return A. Duality involves the complement AND the reflection of B."))

CARDS.append(card(4, 3, "MORPHOLOGY", "Opening and Closing",
    [R(12, 60, 52, 48, "#f1f5f9", 1.6), R(36, 40, 4, 20, "#f1f5f9", 1.4), R(26, 78, 10, 10, "#ffffff", 1.2),
     R(94, 60, 52, 48, "#f1f5f9", 1.6), R(108, 78, 10, 10, "#ffffff", 1.2),
     R(176, 60, 52, 48, "#f1f5f9", 1.6), R(200, 40, 4, 20, "#f1f5f9", 1.4),
     L(66, 84, 92, 84, 1.3, ar=True), L(148, 84, 174, 84, 1.3, ar=True),
     N(38, 124, "A (spur + hole)", 8), N(120, 124, "A ∘ B", 9, w="bold"), N(202, 124, "A • B", 9, w="bold"),
     N(120, 22, "opening removes", 8.5), N(120, 34, "spurs, specks", 8.5), N(202, 22, "closing fills", 8.5), N(202, 34, "small holes", 8.5)],
    "Opening deletes the spur but keeps the hole; closing fills the hole but keeps the spur",
    ["<strong>Opening</strong> $A\\circ B=(A\\ominus B)\\oplus B$: erode away small stuff, then dilate to restore the surviving shapes to near-original size.",
     r"<strong>Closing</strong> $A\bullet B=(A\oplus B)\ominus B$: dilate to close gaps and holes, then erode to restore the outer boundary.",
     "Both are <strong>idempotent</strong>: applying the same opening (or closing) again changes nothing."],
    r"$$A\circ B=(A\ominus B)\oplus B,\qquad A\bullet B=(A\oplus B)\ominus B,\qquad (A\circ B)\circ B=A\circ B$$",
    "Opening is a sieve that lets only big rocks stay; closing is grout that fills every crack smaller than the trowel.",
    "Opening removes objects smaller than B (white specks); closing removes holes smaller than B (black specks). Students swap which one fixes which defect."))

CARDS.append(card(4, 4, "MORPHOLOGY", "Boundary Extraction β(A) = A − (A ⊖ B)",
    [R(52, 22, 100, 90, "#ffffff", 3.4), R(60, 30, 84, 74, "#e2e8f0", 1.2, 0, "4 3"),
     N(102, 72, "A ⊖ B", 10, w="bold"), N(102, 14, "A", 10, w="bold"),
     L(180, 28, 154, 28, 1.3, ar=True), N(190, 32, "β(A) =", 8.5, "start"), N(190, 46, "A − (A ⊖ B)", 8.5, "start"),
     N(190, 74, "thick ring =", 8.5, "start"), N(190, 86, "boundary", 8.5, "start")],
    "Subtract the eroded core from the object and only a one-pixel-thick rim remains",
    ["<strong>What:</strong> The boundary is the part of A that is NOT in its eroded copy: <strong>$\\beta(A)=A-(A\\ominus B)$</strong>.",
     "<strong>How:</strong> A 3×3 square B gives an 8-connected boundary one pixel thick; a plus-shaped (cross) B gives a thicker 4-connected boundary.",
     "<strong>Why:</strong> The same idea powers hole filling, thinning, and the <strong>hit-or-miss</strong> transform that finds exact local patterns."],
    r"$$\beta(A)=A-(A\ominus B),\qquad A\circledast B=(A\ominus B_1)\cap(A^c\ominus B_2)$$",
    "Peeling an orange: erode away the fruit and what you subtract off is the peel, the boundary.",
    "The 3×3 square vs cross choice changes boundary thickness and connectivity. State which structuring element was used."))

_lab = [[1, 0, 0, 0, 0, 1, 1], [0, 1, 0, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 0]]
CARDS.append(card(4, 5, "CONNECTED COMPONENTS", "Connectivity & Two-Pass Labeling",
    [GRID(14, 18, _lab, cell=19, shade={(r, c) for r in range(4) for c in range(7) if _lab[r][c]}, sz=8),
     N(70, 106, "4-conn: 5 components", 8.5),
     N(70, 120, "8-conn: 3 components", 8.5),
     N(186, 24, "two-pass:", 8.5, w="bold"), N(186, 38, "1. scan, label,", 8.5), N(186, 50, "record equivalences", 8.5),
     N(186, 66, "2. union–find, relabel", 8.5), N(186, 90, "pair rule: 8 for", 8.5), N(186, 102, "object, 4 for", 8.5), N(186, 114, "background", 8.5)],
    "The diagonal chain is ONE object under 8-connectivity but three under 4-connectivity",
    ["<strong>4-connected</strong> neighbors share an edge; <strong>8-connected</strong> neighbors also include diagonals. The choice changes what counts as 'one object'.",
     "<strong>Two-pass labeling:</strong> scan, give each pixel the smallest neighboring label (or a new one), note equivalent labels, then <strong>resolve with union–find</strong> and relabel.",
     "Use <strong>8-connectivity for the foreground and 4 for the background</strong> (or vice versa) to avoid the connectivity paradox where a closed curve fails to enclose a region."],
    r"$$N_4(p)=\{(x\pm1,y),(x,y\pm1)\},\qquad N_8(p)=N_4(p)\cup\{(x\pm1,y\pm1)\}$$",
    "Stepping stones across a pond: a diagonal hop counts if you may use 8 moves, but with only 4 moves you are stuck on each stone.",
    "Using 8-connectivity for BOTH object and background creates the paradox (a ring that is both connected and encloses nothing). Pair 8 with 4."))

_g = [[1 if 1 <= r <= 5 and 1 <= c <= 5 else 0 for c in range(8)] for r in range(7)]
_g[3][6] = 1
_sh = {(r, c) for r in range(7) for c in range(8) if _g[r][c]}
CARDS.append(card(4, 6, "WORKED BENCHMARK", "Worked Benchmark: Opening a 5×5 Square with a Spur",
    [GRID(10, 14, [["" for _ in range(8)] for _ in range(7)], cell=13, shade=_sh),
     R(10 + 2 * 13, 14 + 2 * 13, 3 * 13, 3 * 13, "none", 2.4),
     N(172, 30, "B = 3×3 square", 8.5), N(172, 50, "A ⊖ B  = 3×3", 9, w="bold"), N(172, 64, "(inner box)", 8),
     N(172, 84, "(A ⊖ B) ⊕ B", 8.5), N(172, 98, "= 5×5 square", 9, w="bold"), N(172, 114, "spur is gone", 8.5)],
    "Erosion leaves the 3×3 core (bold box); dilating it back restores the 5×5 square without the spur",
    ["The shape is a <strong>5×5 filled square plus a 1-pixel spur</strong>; structuring element B is a 3×3 square.",
     "<strong>Erosion:</strong> only the inner 3×3 block can fit B entirely, and the spur cannot fit at all, so the spur vanishes.",
     "<strong>Dilation:</strong> growing the 3×3 core by B restores the <strong>5×5 square</strong>, so $A\\circ B$ = square, spur removed, and corners kept (a 3×3 square B does not round them)."],
    r"$$|A|=25+1,\quad |A\ominus B|=9,\quad |(A\ominus B)\oplus B|=25$$",
    "Pressure-washing a fence: the thick posts survive and the loose thread hanging off them is blasted away.",
    "Opening does NOT recover exactly the original A in general, only the union of B-shaped pieces that fit inside A. Here it happens to recover the square."))

# ============================ 05 · HISTOGRAM EQUALIZATION ============================
CARDS.append(card(5, 1, "HISTOGRAM EQUALIZATION", "Goal: A Flat Output Histogram",
    [BARS(18, 112, [74, 58, 38, 22, 12, 6, 3, 1], bw=11, gap=2, scale=0.95), L(14, 112, 120, 112, 1.2),
     L(126, 62, 150, 62, 1.6, ar=True), N(138, 55, "T(r)", 8.5, w="bold"),
     BARS(158, 112, [26, 26, 26, 26, 26, 26, 26, 26], bw=8, gap=1, scale=1.0), L(154, 112, 232, 112, 1.2),
     N(66, 128, "skewed input", 8.5), N(194, 128, "≈ uniform output", 8.5)],
    "Spread crowded gray levels apart so the whole range is used evenly",
    ["<strong>What:</strong> Histogram equalization remaps gray levels so the output histogram is as flat as possible, <strong>using every level about equally often</strong>.",
     "<strong>How:</strong> The mapping is the image's own <strong>cumulative distribution function</strong>, which stretches crowded ranges and squeezes sparse ones.",
     "<strong>Why:</strong> It maximizes contrast automatically with <strong>no parameters</strong> to tune."],
    r"$$s_k=T(r_k)=(L-1)\sum_{j=0}^{k}p_r(r_j)$$",
    "Redistributing seats in a crowded hall: wherever people are packed together, add more rows so everyone has similar room.",
    "Equalization is NOT always better. It can over-enhance noise and wash out an image whose histogram is already well spread."))

CARDS.append(card(5, 2, "HISTOGRAM EQUALIZATION", "Why the CDF Makes the Histogram Uniform",
    [AX(26, 125, 224, 14), P("M26 125 C64 122 76 56 110 48 C150 42 176 32 214 28", w=2),
     L(88, 125, 88, 66, 1.2, d="3 3"), L(26, 66, 88, 66, 1.2, d="3 3"),
     N(88, 138, "r", 9), N(14, 68, "s", 9), N(160, 66, "slope = (L−1)·p_r(r)", 8.5), N(160, 80, "steep where p_r is high", 8.5),
     N(120, 138, "", 8)],
    "T(r) is steep where many pixels live, so it stretches exactly those crowded levels",
    [r"Let $s=T(r)=(L-1)\int_0^r p_r(w)\,dw$. This $T$ is <strong>monotonically increasing</strong> and maps $[0,L-1]$ onto itself.",
     r"By the change-of-variables rule, $p_s(s)=p_r(r)\left|\dfrac{dr}{ds}\right|$ and $\dfrac{ds}{dr}=(L-1)p_r(r)$, so <strong>$p_s(s)=\dfrac{1}{L-1}$</strong>: uniform.",
     "In words: the transform is the 'probability integral transform'; pushing a random variable through its own CDF yields a uniform one."],
    r"$$\frac{ds}{dr}=(L-1)\,p_r(r)\ \Rightarrow\ p_s(s)=p_r(r)\Big|\frac{dr}{ds}\Big|=\frac{1}{L-1}$$",
    "A queue with a fast lane for the busiest hour: stretching the busiest times flattens how long anyone waits.",
    "The proof needs a continuous, strictly increasing CDF. The discrete version is only an approximation and never gives a perfectly flat histogram."))

_cdf = [0.19, 0.44, 0.65, 0.81, 0.89, 0.95, 0.98, 1.0]
_pts = "M30 125"
for _k, _v in enumerate(_cdf):
    _x = 30 + _k * 24; _y = 125 - _v * 100
    _pts += f" L{_x} {_y:.1f} L{_x + 24} {_y:.1f}"
CARDS.append(card(5, 3, "HISTOGRAM EQUALIZATION", "Discrete Equalization: round((L−1)·CDF)",
    [AX(26, 125, 224, 14), P(_pts, w=2), N(120, 138, "r_k", 9), N(26, 12, "cdf", 8.5, "start"),
     N(190, 40, "s_k = round((L−1)·cdf)", 8.5), N(190, 54, "monotone, many-to-one", 8.5), N(190, 68, "no new gray levels", 8.5)],
    "The staircase CDF scaled by (L−1) and rounded gives the new gray levels",
    ["<strong>Steps:</strong> compute $p_r(r_k)=n_k/MN$, accumulate the CDF, multiply by $L-1$, <strong>round to the nearest integer</strong>.",
     "Because of rounding, <strong>several input levels can merge</strong> into one output level; the result is only approximately flat.",
     "The mapping is monotone (order preserved) and <strong>cannot create gray levels that have no input pixels</strong>, so it can leave gaps."],
    r"$$s_k=\operatorname{round}\!\Big[(L-1)\sum_{j=0}^{k}\frac{n_j}{MN}\Big]$$",
    "Rounding prices to whole dollars: several slightly different prices collapse onto the same tag, and the shelf of tags is never perfectly even.",
    "Using floor instead of round, or (L) instead of (L−1), shifts every level. Also equalizing twice does nothing extra (it is nearly idempotent)."))

_p = [(30, 36, 18), (92, 84, 18), (154, 66, 18)]
CARDS.append(card(5, 4, "HISTOGRAM SPECIFICATION", "Histogram Specification (Matching)",
    [R(8, 40, 52, 36, "#ffffff", 1.6), N(34, 62, "p_r(r)", 9), L(62, 58, 86, 58, 1.4, ar=True), N(74, 52, "T", 9, w="bold"),
     R(88, 40, 52, 36, "#f1f5f9", 1.6), N(114, 62, "uniform s", 8.5), L(142, 58, 166, 58, 1.4, ar=True), N(154, 52, "G⁻¹", 9, w="bold"),
     R(168, 40, 60, 36, "#ffffff", 1.6), N(198, 62, "target p_z(z)", 8.5),
     N(34, 92, "r", 9), N(114, 92, "s", 9), N(198, 92, "z", 9),
     N(120, 116, "z = G⁻¹( T(r) )", 10, w="bold"), N(120, 130, "equalize both, then invert the target", 8)],
    "Equalize the input, then push through the inverse of the target's equalizing map",
    ["<strong>What:</strong> Instead of a flat output, you force the histogram to match a <strong>chosen target shape</strong> $p_z(z)$.",
     r"<strong>How:</strong> Equalize the input ($s=T(r)$) and equalize the target ($v=G(z)$); since both give uniform histograms, set $s=v$ and invert: <strong>$z=G^{-1}[T(r)]$</strong>.",
     "<strong>Why:</strong> It lets you match one image's look to another or shape contrast for a specific display."],
    r"$$s=T(r)=(L-1)\sum p_r,\qquad G(z)=(L-1)\sum p_z,\qquad z=G^{-1}\big(T(r)\big)$$",
    "Two people converting currency through a common middleman: convert to the neutral currency first, then out to the one you want.",
    "G is a staircase, so G⁻¹ is not exact: pick the z whose G(z) is closest to s (and handle ties consistently)."))

CARDS.append(card(5, 5, "ADAPTIVE METHODS", "Local HE and CLAHE (Clip Limit)",
    [L(20, 118, 120, 118, 1.2), BARS(26, 118, [30, 92, 52, 22, 10, 6], bw=12, gap=3, scale=0.95),
     L(20, 62, 122, 62, 1.5, d="5 3"), N(70, 54, "clip limit", 8.5), N(70, 132, "tile histogram", 8.5),
     L(128, 80, 158, 80, 1.4, ar=True), N(143, 72, "redistribute", 7.5),
     L(164, 118, 232, 118, 1.2), BARS(170, 118, [36, 62, 48, 36, 30, 28], bw=9, gap=2, scale=0.95),
     N(200, 132, "clipped + spread", 8.5)],
    "Clip tall histogram peaks and spread the excess so noise isn't over-amplified",
    ["<strong>Local (adaptive) HE</strong> equalizes each small tile separately, boosting <strong>local contrast</strong> that global HE misses.",
     "Plain local HE <strong>amplifies noise</strong> in flat tiles because a tall narrow peak maps to a steep slope.",
     "<strong>CLAHE</strong> clips the histogram at a limit, spreads the clipped excess across all bins, and <strong>bilinearly blends neighboring tiles</strong> to hide seams."],
    r"$$h_{\text{clip}}(k)=\min\big(h(k),\,\beta\big),\qquad \text{excess}=\sum_k\big(h(k)-\beta\big)^+\ \text{redistributed uniformly}$$",
    "A photographer evening out exposure region by region, but refusing to crank up the gain on a flat gray wall.",
    "Without the clip limit, local equalization turns uniform regions into noise. The clip limit is what makes CLAHE usable."))

_nk = [790, 1023, 850, 656, 329, 245, 122, 81]
CARDS.append(card(5, 6, "WORKED BENCHMARK", "Worked Benchmark: 3-bit, 4096-Pixel Equalization",
    [L(20, 108, 224, 108, 1.2)] +
    [R(26 + i * 25, 108 - n * 0.075, 20, n * 0.075, "#f1f5f9", 1.3) for i, n in enumerate(_nk)] +
    [N(36 + i * 25, 120, str(i), 8.5) for i in range(8)] +
    [N(36 + i * 25, 132, str(v), 9, w="bold") for i, v in enumerate([1, 3, 5, 6, 6, 7, 7, 7])] +
    [N(14, 120, "r", 8), N(14, 132, "s", 8), N(120, 14, "n_k: 790 1023 850 656 329 245 122 81", 8.5)],
    "n_k → cdf (.19 .44 .65 .81 .89 .95 .98 1) → s_k = round(7·cdf) = 1, 3, 5, 6, 6, 7, 7, 7",
    ["<strong>Counts</strong> $n_k$ over 4096 pixels give $p_r=0.19,\\,0.25,\\,0.21,\\,0.16,\\,0.08,\\,0.06,\\,0.03,\\,0.02$.",
     r"<strong>Cumulative sums</strong> are $0.19,\ 0.44,\ 0.65,\ 0.81,\ 0.89,\ 0.95,\ 0.98,\ 1.00$, and multiplying by $L-1=7$ gives $1.33,\ 3.08,\ 4.55,\ 5.67,\ 6.23,\ 6.65,\ 6.86,\ 7$.",
     "<strong>Rounded:</strong> $r=0\\to1,\\ 1\\to3,\\ 2\\to5,\\ 3\\to6,\\ 4\\to6,\\ 5\\to7,\\ 6\\to7,\\ 7\\to7$. Note <strong>levels 3 and 4 merge, and 5, 6, 7 merge</strong>, so the output only has five distinct levels."],
    r"$$s_0=\operatorname{round}(7\cdot0.19)=1,\quad s_1=\operatorname{round}(7\cdot0.44)=3,\quad s_2=\operatorname{round}(7\cdot0.65)=5$$",
    "Re-seating a hall: the crowded left rows get spread out, while the nearly empty right rows are squeezed together into one block.",
    "The output has only 5 distinct levels (1, 3, 5, 6, 7), never all 8. Equalization on few levels cannot create a perfectly flat histogram."))
