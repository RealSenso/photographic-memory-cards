import math
from dip_lib import *

CARDS = []

def _poly(pts, w=1.8, dash=None, fill="none"):
    d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    return P(d, fill=fill, w=w, dash=dash)

def STEMS(x0, base, vals, dx=14, scale=3.0, w=2.2):
    out = [L(x0 - 6, base, x0 + dx * len(vals), base, 1.1)]
    for i, v in enumerate(vals):
        out.append(L(x0 + i * dx, base, x0 + i * dx, base - v * scale, w))
        out.append(C(x0 + i * dx, base - v * scale, 2.4))
    return out

def BOX(x, y, w, h, label, fill="#f1f5f9", sz=9, bold=True):
    return R(x, y, w, h, fill, 1.6) + N(x + w / 2, y + h / 2 + 3, label, sz, w="bold" if bold else "normal")

# ============================ 10 · WAVELETS ============================
tiles_stft = [R(14 + i * 24, 20 + j * 24, 24, 24, "#ffffff", 1.2) for i in range(4) for j in range(4)]
tiles_wav = [R(134, 90, 96, 14, "#f1f5f9", 1.2)] + [R(134 + i * 48, 62, 48, 28, "#ffffff", 1.2) for i in range(2)] + \
            [R(134 + i * 24, 20, 24, 42, "#f1f5f9", 1.2) for i in range(4)]
CARDS.append(card(10, 1, "WAVELET BASICS", "Time-Frequency Tiling: STFT vs Wavelets",
    tiles_stft + tiles_wav + [N(62, 124, "STFT: fixed tiles", 8.5, w="bold"), N(182, 124, "wavelet: adaptive tiles", 8.5, w="bold"),
        L(10, 118, 10, 20, 1.2, ar=True), N(6, 15, "freq", 8, "start"), N(62, 14, "time →", 8), N(182, 14, "time →", 8),
        N(240, 46, "", 8)],
    "Wavelets use short windows at high frequency and long windows at low frequency",
    ["The Fourier transform says <strong>which frequencies</strong> but not <strong>where</strong>; the STFT adds position but uses <strong>one fixed window</strong> for all frequencies.",
     r"A wavelet family $\psi_{j,k}(x)=2^{j/2}\psi(2^jx-k)$ is built by <strong>scaling and shifting one mother wavelet</strong>, so high frequencies get narrow windows and low ones get wide windows.",
     "This <strong>multi-resolution</strong> match to natural images (sharp edges + smooth regions) is why wavelets compress and denoise well (JPEG 2000)."],
    r"$$\psi_{j,k}(x)=2^{j/2}\,\psi\!\left(2^{j}x-k\right),\qquad c_{j,k}=\langle f,\psi_{j,k}\rangle$$",
    "Reading with a magnifier: wide lens for the page layout, a close lens for tiny print; the lens size adapts to the detail you want.",
    "Heisenberg still applies: every tile has the same AREA (Δt·Δf ≥ const). Wavelets change the tile shape, not the area."))

CARDS.append(card(10, 2, "WAVELET BASICS", "Multiresolution Analysis: Nested Spaces",
    [E(86, 74, 26, 20, 0, "#e2e8f0", 1.8), E(86, 74, 50, 38, 0, "none", 1.6), E(86, 74, 72, 56, 0, "none", 1.6),
     N(86, 77, "V₀", 11, w="bold"), N(86, 48, "W₀", 10, w="bold"), N(86, 26, "W₁", 10, w="bold"),
     N(100, 144, "", 8), N(196, 36, "V₀ ⊂ V₁ ⊂ V₂", 9, "middle", "bold"), N(196, 54, "Vⱼ₊₁ = Vⱼ ⊕ Wⱼ", 9, "middle", "bold"),
     N(196, 80, "V: smooth", 8.5), N(196, 92, "approximation", 8.5), N(196, 108, "W: detail added", 8.5), N(196, 120, "going finer", 8.5)],
    "Each finer approximation space contains the coarser one plus a detail space",
    ["An <strong>MRA</strong> is a ladder of approximation spaces $\\cdots\\subset V_0\\subset V_1\\subset V_2\\subset\\cdots$ where $V_j$ holds details down to scale $2^{-j}$.",
     "The <strong>detail space</strong> $W_j$ is exactly what must be added to $V_j$ to get $V_{j+1}$: $V_{j+1}=V_j\\oplus W_j$ (orthogonal sum).",
     "A <strong>scaling function</strong> $\\varphi$ spans each $V_j$ and a <strong>wavelet</strong> $\\psi$ spans $W_j$; so any image is coarse approximation plus a stack of details."],
    r"$$V_{j+1}=V_j\oplus W_j,\quad f=\sum_k c_{J,k}\varphi_{J,k}+\sum_{j\ge J}\sum_k d_{j,k}\psi_{j,k}$$",
    "Zooming a map: the city view (V₀) plus extra street detail (W₀) gives the neighborhood view (V₁), and so on down.",
    "W_j is the orthogonal complement of V_j INSIDE V_{j+1}, not the difference of the sets. The sum is direct (⊕), not a union."))

CARDS.append(card(10, 3, "FILTER BANKS", "Two-Channel Filter Bank & Haar",
    [BOX(28, 14, 28, 24, "h₀"), BOX(66, 14, 28, 24, "↓2", "#ffffff"), BOX(28, 70, 28, 24, "h₁"), BOX(66, 70, 28, 24, "↓2", "#ffffff"),
     N(10, 30, "x", 10), L(14, 26, 26, 26, 1.3, ar=True), L(14, 26, 14, 82, 1.3), L(14, 82, 26, 82, 1.3, ar=True),
     L(58, 26, 64, 26, 1.3, ar=True), L(58, 82, 64, 82, 1.3, ar=True),
     L(96, 26, 118, 26, 1.3, ar=True), L(96, 82, 118, 82, 1.3, ar=True), N(106, 20, "a", 9, w="bold"), N(106, 76, "d", 9, w="bold"),
     BOX(120, 14, 28, 24, "↑2", "#ffffff"), BOX(156, 14, 28, 24, "g₀"), BOX(120, 70, 28, 24, "↑2", "#ffffff"), BOX(156, 70, 28, 24, "g₁"),
     L(150, 26, 154, 26, 1.3, ar=True), L(150, 82, 154, 82, 1.3, ar=True),
     L(186, 26, 204, 26, 1.3), L(186, 82, 204, 82, 1.3), L(204, 26, 204, 82, 1.3), C(204, 54, 7, "#ffffff"), N(204, 57, "+", 10, w="bold"),
     L(211, 54, 228, 54, 1.3, ar=True), N(230, 40, "x̂", 10),
     N(120, 116, "Haar: h₀=[1,1]/√2,  h₁=[1,−1]/√2", 8.5, w="bold"), N(120, 130, "perfect reconstruction: x̂ = x", 8.5)],
    "Analysis splits into a (coarse) and d (detail), synthesis puts them back together",
    ["<strong>Analysis:</strong> a low-pass $h_0$ gives the <strong>approximation</strong>, a high-pass $h_1$ gives the <strong>detail</strong>, each then <strong>downsampled by 2</strong>, so the total sample count is unchanged.",
     r"<strong>Synthesis:</strong> upsample by 2 and filter with $g_0,g_1$, then add. <strong>Perfect reconstruction</strong> needs alias cancellation and no distortion: $G_0H_0+G_1H_1=2$ and $G_0(z)H_0(-z)+G_1(z)H_1(-z)=0$.",
     "<strong>Haar</strong> is the simplest bank: low-pass = pairwise average, high-pass = pairwise difference (scaled by $1/\\sqrt2$)."],
    r"$$a[n]=\frac{x[2n]+x[2n+1]}{\sqrt2},\quad d[n]=\frac{x[2n]-x[2n+1]}{\sqrt2},\quad \text{iterate on } a\ \text{for more levels}$$",
    "A sorting hat for signal parts: slow trends go into one bin, quick wiggles into another, and both bins together rebuild the original.",
    "Each channel is downsampled, so the high-pass band folds (aliases) in the spectrum. PR needs the synthesis filters to cancel that exactly."))

def _dwt_lines():
    out = [R(24, 14, 100, 100, "#ffffff", 1.8), L(24, 64, 124, 64, 1.5), L(74, 14, 74, 114, 1.5),
           R(24, 14, 50, 50, "#ffffff", 0), L(24, 39, 74, 39, 1.3), L(49, 14, 49, 64, 1.3),
           L(24, 26.5, 49, 26.5, 1.1), L(36.5, 14, 36.5, 39, 1.1)]
    labs = [N(36, 28, "LL", 7), N(62, 30, "HL", 8.5), N(36, 54, "LH", 8.5), N(62, 54, "HH", 8.5),
            N(99, 42, "HL", 10, w="bold"), N(49, 92, "LH", 10, w="bold"), N(99, 92, "HH", 10, w="bold")]
    return out + labs

CARDS.append(card(10, 4, "2-D DWT", "2-D DWT Subbands (Pyramid)",
    _dwt_lines() + [N(184, 30, "rows × columns", 8.5, w="bold"), N(184, 44, "LL = smooth", 8.5), N(184, 58, "HL = vertical edges", 8.5),
                    N(184, 72, "LH = horizontal edges", 8.5), N(184, 86, "HH = diagonals", 8.5), N(184, 108, "recurse on LL", 8.5, w="bold")],
    "One level splits into LL, HL, LH, HH; the next level splits only the LL corner again",
    ["A 2D DWT applies the 1D filter bank <strong>along rows, then along columns</strong>, giving four quarter-size subbands: LL (low-low), HL, LH, HH.",
     "<strong>LL</strong> is a half-resolution thumbnail; <strong>HL</strong> responds to vertical edges, <strong>LH</strong> to horizontal edges, <strong>HH</strong> to diagonal detail.",
     "Recurse on the <strong>LL band only</strong> to get a pyramid. Most coefficients in detail bands are tiny, so compression keeps the few big ones (JPEG 2000)."],
    r"$$\text{levels}=J:\quad \text{size}(LL_J)=\tfrac{M}{2^J}\times\tfrac{N}{2^J},\qquad \#\text{coeffs}=MN\ \ (\text{critically sampled})$$",
    "A Russian doll of thumbnails: each doll holds a smaller blurred copy plus a bag of the sharpening details it lost.",
    "Naming differs between books: HL may mean 'high-pass horizontally' or 'vertically'. Check which axis the first letter refers to."))

def _thr():
    cx, cy = 120, 72
    out = [L(30, cy, 214, cy, 1.1, ar=True), L(cx, 130, cx, 14, 1.1, ar=True),
           L(60, 132, 102, 90, 2), L(102, 72, 138, 72, 2), L(138, 54, 180, 12, 2),
           L(102, 90, 102, 72, 1, d="2 2"), L(138, 72, 138, 54, 1, d="2 2"),
           P("M60 114 L102 72 L138 72 L180 30", w=1.8, dash="6 3"),
           N(102, 140, "−T", 9), N(138, 140, "T", 9), N(210, 66, "coef", 8), N(125, 12, "out", 8, "start"),
           N(184, 52, "hard", 9, "start", "bold"), N(184, 40, "", 8), N(60, 100, "soft (dashed)", 8.5, "start")]
    return out

CARDS.append(card(10, 5, "WAVELET DENOISING", "Thresholding: Hard vs Soft Shrinkage",
    _thr(),
    "Hard keeps big coefficients unchanged; soft also shrinks them by T",
    ["<strong>Idea:</strong> real image detail gives a few <strong>large</strong> wavelet coefficients, while white noise spreads into <strong>many small</strong> ones. Zero the small ones.",
     r"<strong>Hard</strong> thresholding keeps $|c|>T$ unchanged; <strong>soft</strong> thresholding shrinks them toward zero by $T$ (continuous, so no jumpy artifacts).",
     r"The <strong>universal (VisuShrink) threshold</strong> is $T=\sigma\sqrt{2\ln N}$ with noise level $\sigma$ (often estimated as median$(|d_1|)/0.6745$)."],
    r"$$\hat c_{\text{hard}}=c\,\mathbb{1}_{|c|>T},\qquad \hat c_{\text{soft}}=\operatorname{sign}(c)\,(|c|-T)_+,\qquad T=\sigma\sqrt{2\ln N}$$",
    "Skimming off cream: noise is thin milk spread across everything, signal is thick cream in a few spots; skim at the right level.",
    "Never threshold the LL (approximation) band, it holds the image itself. And too high a T erases real texture along with the noise."))

CARDS.append(card(10, 6, "WORKED BENCHMARK", "Worked Benchmark: 3-Level Haar of [4, 6, 10, 12]",
    [N(10, 24, "x", 10, "start", w="bold"), GRID(30, 10, [[4, 6, 10, 12]], cell=24),
     N(10, 62, "L1", 9, "start", w="bold"), GRID(30, 48, [[5, 11, -1, -1]], cell=24, shade={(0, 2), (0, 3)}),
     N(10, 100, "L2", 9, "start", w="bold"), GRID(30, 86, [[8, -3, -1, -1]], cell=24, shade={(0, 1), (0, 2), (0, 3)}),
     N(160, 28, "avg = (a+b)/2", 8.5, "start"), N(160, 42, "det = (a−b)/2", 8.5, "start"),
     N(160, 70, "gray = detail", 8.5, "start"), N(160, 104, "rebuild: a = avg+det", 8.5, "start"), N(160, 118, "b = avg−det", 8.5, "start")],
    "Averages [5, 11] and details [−1, −1]; then average 8 and detail −3: output [8, −3, −1, −1]",
    ["<strong>Level 1:</strong> pair up $(4,6)\\to$ avg 5, detail $(4-6)/2=-1$; $(10,12)\\to$ avg 11, detail $-1$. Result: <strong>[5, 11 | −1, −1]</strong>.",
     "<strong>Level 2</strong> on the averages $(5,11)$: avg <strong>8</strong>, detail <strong>−3</strong>, giving the pyramid <strong>[8 | −3 | −1, −1]</strong>.",
     "<strong>Rebuild</strong> bottom-up: $5=8+(-3)$, $11=8-(-3)$, then $4=5+(-1)$, $6=5-(-1)$, $10=11+(-1)$, $12=11-(-1)$. Perfect reconstruction, and the tiny details compress well."],
    r"$$[4,6,10,12]\ \to\ [8,\,-3,\,-1,\,-1],\qquad \text{(unnormalized Haar: avg/diff by 2)}$$",
    "Reporting a team's results: first the overall average, then how far each half and each pair deviates from it.",
    "With the orthonormal Haar the filters carry 1/√2 instead, so the numbers differ by √2 factors. Match the convention in the question."))

# ============================ 11 · RESTORATION ============================
CARDS.append(card(11, 1, "RESTORATION", "Degradation Model g = h∗f + η",
    [N(12, 44, "f", 11, "start", w="bold"), L(24, 40, 42, 40, 1.4, ar=True), BOX(44, 24, 40, 32, "H(u,v)"),
     L(86, 40, 124, 40, 1.4, ar=True), C(132, 40, 8, "#ffffff"), N(132, 44, "+", 11, w="bold"),
     L(132, 14, 132, 30, 1.4, ar=True), N(132, 10, "η (noise)", 8.5),
     L(142, 40, 172, 40, 1.4, ar=True), N(184, 44, "g", 11, "start", w="bold"),
     L(184, 56, 184, 80, 1.4, ar=True), BOX(150, 82, 64, 30, "restore W(u,v)"), L(150, 97, 120, 97, 1.4, ar=True), N(106, 100, "f̂", 11, w="bold"),
     N(60, 100, "G = HF + N", 10, w="bold"), N(60, 116, "(blur then add noise)", 8.5)],
    "Blur H acts first, noise η is added after; restoration tries to undo both",
    ["The observed image is the true image <strong>blurred</strong> by the system $h$ (point-spread function) and then <strong>corrupted by additive noise</strong> $\\eta$.",
     r"In frequency: <strong>$G(u,v)=H(u,v)F(u,v)+N(u,v)$</strong>, so deblurring is a per-frequency division problem that must also handle $N$.",
     "<strong>Restoration</strong> uses a model of the degradation (unlike enhancement, which is subjective) to build an estimate $\\hat F=W\\,G$."],
    r"$$g(x,y)=(h\ast f)(x,y)+\eta(x,y)\ \ \longleftrightarrow\ \ G(u,v)=H(u,v)F(u,v)+N(u,v)$$",
    "Dictating a message over a bad phone line: the line muffles it (H) and adds crackle (η); restoring means undoing both.",
    "Noise is added AFTER the blur, so it is not blurred. This is exactly why plain inversion by H blows the noise up."))

def _inv():
    h = [(x, 125 - 95 * max(0.0, math.cos(math.pi / 2 * (x - 20) / 130))) for x in range(20, 151, 4)]
    inv = []
    for x in range(20, 147, 3):
        hv = math.cos(math.pi / 2 * (x - 20) / 130)
        inv.append((x, max(14.0, 125 - 30 / max(hv, 0.001) )))
    return [AX(20, 125, 226, 14), _poly(h, 2.2), _poly(inv, 1.6, "5 3"), L(150, 125, 150, 14, 1, d="2 3"),
            N(150, 138, "H = 0", 8.5), N(70, 60, "|H|", 10, "start", "bold"), N(120, 22, "1/|H| → ∞", 9, "start", "bold"), N(96, 138, "", 8)]

CARDS.append(card(11, 2, "RESTORATION", "Inverse Filtering: Noise Blow-Up",
    _inv(),
    "Where |H| falls to zero, 1/|H| explodes and the noise term is amplified without bound",
    [r"<strong>Naive inverse:</strong> $\hat F=G/H=F+N/H$, so with no noise it recovers $F$ exactly.",
     r"<strong>Problem:</strong> real systems have $H\to0$ at high frequencies (and sometimes exact zeros), so the error term <strong>$N/H$ is hugely amplified</strong> there and swamps the picture.",
     "<strong>Fixes:</strong> limit the inverse to frequencies where $|H|$ is large (a pseudo-inverse with a radius cut-off) or use <strong>Wiener / regularized</strong> filters."],
    r"$$\hat F(u,v)=\frac{G(u,v)}{H(u,v)}=F(u,v)+\frac{N(u,v)}{H(u,v)}$$",
    "Turning up the volume to hear a faint voice: you also turn up the hiss by the same factor, until the hiss is all you hear.",
    "If H(u,v) = 0 exactly the inverse is undefined (not just large). The 'N/H' term is the reason inverse filtering fails in noise."))

def _wien():
    K = 0.04
    inv = [(x, max(14.0, 125 - 10 / max(math.cos(math.pi / 2 * (x - 20) / 130), 0.001))) for x in range(20, 147, 3)]
    wn = []
    for x in range(20, 151, 3):
        H = math.cos(math.pi / 2 * (x - 20) / 130)
        wn.append((x, 125 - 16 * (H / (H * H + K))))
    return [AX(20, 125, 226, 14), _poly(inv, 1.6, "5 3"), _poly(wn, 2.4), L(150, 125, 150, 14, 1, d="2 3"),
            N(70, 60, "inverse 1/H", 8.5, "start"), N(160, 64, "Wiener H*/(|H|²+K)", 8.5, "start", "bold"),
            N(160, 78, "rolls off to 0", 8.5, "start"), N(122, 138, "frequency →", 8)]

CARDS.append(card(11, 3, "RESTORATION", "Wiener Filter: Don't Divide by Noise",
    _wien(),
    "The Wiener gain follows 1/H where the signal dominates, then rolls off where noise would win",
    [r"<strong>Goal:</strong> choose $W$ to minimize the mean-squared error $E\|f-\hat f\|^2$ given the noise-to-signal power ratio $S_\eta/S_f$.",
     r"<strong>Result:</strong> $W=\dfrac{H^{*}}{|H|^{2}+S_\eta/S_f}$. Where $|H|^{2}\gg S_\eta/S_f$ it acts like <strong>$1/H$</strong>; where $|H|$ is tiny it <strong>suppresses</strong> instead of exploding.",
     "<strong>Practical form:</strong> replace $S_\\eta/S_f$ by a constant $K$ tuned by eye. $K=0$ gives the inverse filter; larger $K$ gives smoother, blurrier output."],
    r"$$W(u,v)=\frac{H^{*}(u,v)}{|H(u,v)|^{2}+\dfrac{S_\eta(u,v)}{S_f(u,v)}},\qquad \hat F=W\,G$$",
    "A hearing aid with a smart gain: boost faint speech where it's above the hiss, but refuse to amplify frequencies that are only hiss.",
    "Wiener assumes known power spectra of signal and noise. Using the wrong K gives either ringing/noise (K too small) or over-blur (K too large)."))

def _lcurve():
    return [AX(24, 124, 224, 14), P("M30 20 C34 70 44 100 80 108 C120 114 170 116 218 118", w=2.2), C(62, 104, 4), N(76, 98, "best γ (corner)", 8.5, "start", "bold"),
            N(28, 14, "smoothness ‖Pf̂‖²", 8.5, "start"), N(120, 138, "data misfit ‖g − Hf̂‖²", 8.5),
            N(46, 44, "γ large", 8, "start"), N(160, 108, "γ small", 8, "start")]

CARDS.append(card(11, 4, "RESTORATION", "Constrained Least Squares (Regularization)",
    _lcurve(),
    "Trade data fit against smoothness; the corner of the L-curve is a good γ",
    ["<strong>Idea:</strong> minimize a <strong>smoothness measure</strong> $\\|Pf\\|^2$ (with $P$ a Laplacian) subject to the data constraint $\\|g-Hf\\|^2=\\|\\eta\\|^2$, which does not need the power spectra.",
     r"<strong>Solution:</strong> $\hat F=\dfrac{H^{*}}{|H|^{2}+\gamma|P|^{2}}G$, which looks just like Wiener but with a <strong>smoothness penalty weight $\gamma$</strong>.",
     "<strong>Choose $\\gamma$</strong> by iterating until $\\|g-H\\hat f\\|^2\\approx\\|\\eta\\|^2$, or at the corner of the <strong>L-curve</strong> (misfit vs. smoothness)."],
    r"$$\min_f\ \|Pf\|^2\ \text{s.t.}\ \|g-Hf\|^2=\|\eta\|^2\ \Rightarrow\ \hat F=\frac{H^{*}}{|H|^{2}+\gamma\,|P(u,v)|^{2}}\,G$$",
    "Tuning a sketch: make it fit the reference photo, but not so tightly that you trace every speck of film grain.",
    "Tikhonov/CLS and Wiener coincide only when γ|P|² equals S_η/S_f. In general they are different recipes with different knobs."))

def _sinc():
    pts = []
    for x in range(20, 223, 2):
        a = (x - 20) / 40.0
        v = 1.0 if a == 0 else abs(math.sin(math.pi * a) / (math.pi * a))
        pts.append((x, 120 - 90 * v))
    z = [C(20 + 40 * k, 120, 3, "#ffffff") for k in range(1, 6)]
    return [AX(20, 120, 226, 14), _poly(pts, 2)] + z + [
        N(60, 136, "1/(aT)", 8), N(100, 136, "2/(aT)", 8), N(140, 136, "3/(aT)", 8),
        N(150, 36, "zeros of |H|:", 8.5, "start", "bold"), N(150, 50, "inverse undefined", 8.5, "start"), N(60, 28, "|H(u)|", 9, "start", "bold")]

CARDS.append(card(11, 5, "RESTORATION", "Estimating H: Motion Blur & Zeros",
    _sinc(),
    "A uniform motion blur has a sinc transfer function with exact zeros, so those frequencies are lost",
    [r"<strong>Motion blur</strong> over displacement $aT$ gives $H(u)=\dfrac{\sin(\pi u a T)}{\pi u a}e^{-j\pi uaT}$, a <strong>sinc</strong> that crosses zero at $u=k/(aT)$.",
     "<strong>Defocus</strong> gives a disk (pillbox) PSF, <strong>Gaussian</strong> blur gives a Gaussian $H$ with no exact zeros but a rapid roll-off; atmospheric turbulence is also Gaussian-like.",
     "<strong>Identify $H$</strong> by observation (a known point source or sharp edge), experiment, or mathematical modeling; blind deconvolution estimates it from $g$ alone."],
    r"$$H(u)=\frac{\sin(\pi uaT)}{\pi ua}\,e^{-j\pi uaT},\qquad H(u)=0\ \text{ at }\ u=\frac{k}{aT}$$",
    "A photo taken while the camera swept sideways: certain stripe patterns are averaged out entirely and can never be recovered.",
    "At the exact zeros the information is destroyed. No linear filter can restore those frequencies, so ringing near sharp edges is expected."))

CARDS.append(card(11, 6, "WORKED BENCHMARK", "Worked Benchmark: Inverse vs Wiener Gain",
    [L(20, 120, 222, 120, 1.2), R(36, 120 - 80, 28, 80, "#ffffff", 1.6), R(72, 120 - 13.4, 28, 13.4, "#f1f5f9", 1.6),
     R(130, 120 - 8, 28, 8, "#ffffff", 1.6), R(166, 120 - 7.6, 28, 7.6, "#f1f5f9", 1.6),
     N(50, 112 - 80 + 0, "10", 9, w="bold"), N(86, 100, "1.67", 9, w="bold"), N(144, 110, "1", 9, w="bold"), N(180, 110, "0.95", 9, w="bold"),
     N(50, 134, "1/H", 8.5), N(86, 134, "Wiener", 8.5), N(144, 134, "1/H", 8.5), N(180, 134, "Wiener", 8.5),
     N(68, 18, "H = 0.1  (weak freq)", 9, w="bold"), N(162, 18, "H = 1  (strong freq)", 9, w="bold"), L(112, 24, 112, 130, 1, d="3 3")],
    "At a weak frequency Wiener cuts the gain from 10 to 1.67; at a strong one it barely changes it",
    ["Take $K=S_\\eta/S_f=0.05$. At a <strong>weak</strong> frequency $H=0.1$: inverse gain $1/H=\\mathbf{10}$ (noise power amplified $100\\times$), Wiener gain $=0.1/(0.01+0.05)=\\mathbf{1.67}$.",
     "At a <strong>strong</strong> frequency $H=1$: inverse gain $=1$, Wiener gain $=1/(1+0.05)=\\mathbf{0.95}$. So <strong>Wiener ≈ inverse where the signal is strong</strong>.",
     "The 6× lower gain at the weak frequency is the whole point: <strong>it trades a little bias for a huge cut in noise variance</strong>."],
    r"$$W(0.1)=\frac{0.1}{0.1^2+0.05}=1.67,\qquad W(1)=\frac{1}{1^2+0.05}=0.952$$",
    "A bouncer who trusts loud, clear voices but ignores whispers that could just be background chatter.",
    "H must be real here (no phase). With complex H use H* in the numerator and |H|² in the denominator, not H² or 1/H."))

# ============================ 12 · NON-LINEAR ============================
CARDS.append(card(12, 1, "ORDER STATISTICS", "Median vs Mean on Impulse Noise",
    STEMS(20, 40, [3, 3, 3, 3, 3, 12, 3, 3, 3, 3, 3], 14, 2.8) + [N(20, 52, "input", 8.5, "start", "bold")] +
    STEMS(20, 88, [3, 3, 3, 3, 6, 6, 6, 3, 3, 3, 3], 14, 2.8) + [N(20, 100, "3-pt mean", 8.5, "start", "bold")] +
    STEMS(20, 136, [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 14, 2.8) + [N(20, 144, "3-pt median", 8.5, "start", "bold")],
    "The mean smears the spike into a 3-sample bump; the median removes it completely",
    ["<strong>Impulse (salt-and-pepper) noise</strong> sets isolated pixels to extreme values, which a <strong>linear averaging</strong> filter spreads into neighbors instead of removing.",
     "The <strong>median filter</strong> replaces each pixel by the median of its window; an outlier is never the middle value, so it is <strong>discarded outright</strong>.",
     "Rule of thumb: a $K{\\times}K$ median removes impulse clusters smaller than <strong>half the window area</strong> (fewer than $K^2/2$ pixels)."],
    r"$$\hat f(x,y)=\operatorname{median}\{f(s,t)\mid (s,t)\in S_{xy}\}$$",
    "Asking a panel of neighbors the price of bread: the one person shouting an absurd number can't sway the middle answer, but would wreck the average.",
    "The median is NOT linear (median of a sum ≠ sum of medians), so convolution theory and the frequency domain do not apply."))

CARDS.append(card(12, 2, "ORDER STATISTICS", "Median Filter Preserves Edges",
    STEMS(20, 40, [2, 2, 2, 2, 8, 8, 8, 8], 22, 3.2) + [N(20, 52, "step edge", 8.5, "start", "bold")] +
    STEMS(20, 88, [2, 2, 2, 4, 6, 8, 8, 8], 22, 3.2) + [N(20, 100, "3-pt mean: ramp", 8.5, "start", "bold")] +
    STEMS(20, 136, [2, 2, 2, 2, 8, 8, 8, 8], 22, 3.2) + [N(20, 144, "3-pt median: sharp", 8.5, "start", "bold")],
    "The mean blurs the step into a ramp; the median keeps it a perfect step",
    ["At a step edge, any window straddling it contains <strong>mostly one side</strong>, so the median picks that side's value and the step stays <strong>exactly sharp</strong>.",
     "A mean mixes both sides and <strong>creates intermediate values</strong> that did not exist (edge blur).",
     "<strong>Root signals:</strong> a signal unchanged by the median is its own 'root'; repeated filtering converges to a root in a finite number of passes."],
    r"$$\operatorname{median}(2,2,8)=2,\quad \operatorname{median}(2,8,8)=8,\quad \text{but}\ \ \operatorname{mean}(2,2,8)=4$$",
    "A fence-sitter vote: the majority side wins entirely, so a border between two camps stays a crisp line instead of a gradient.",
    "The median shrinks thin lines and sharp corners (thinner than half the window) just as it removes impulses. It is not edge-safe for thin structures."))

CARDS.append(card(12, 3, "ADAPTIVE FILTERS", "Adaptive Median Filter (Variable Window)",
    [BOX(10, 14, 100, 34, "A: zmin < zmed < zmax ?", "#f1f5f9", 8.5), BOX(130, 14, 100, 34, "B: zmin < z_xy < zmax ?", "#f1f5f9", 8.5),
     L(110, 31, 128, 31, 1.4, ar=True), N(119, 25, "yes", 8),
     BOX(130, 66, 46, 26, "output z_xy", "#ffffff", 8), BOX(184, 66, 46, 26, "output z_med", "#ffffff", 8),
     L(170, 48, 154, 64, 1.3, ar=True), L(192, 48, 206, 64, 1.3, ar=True), N(150, 58, "yes", 8), N(210, 58, "no", 8),
     L(60, 48, 60, 66, 1.4, ar=True), N(72, 60, "no", 8), BOX(10, 68, 100, 30, "grow window S ≤ S_max", "#ffffff", 8),
     L(60, 98, 60, 112, 1.3), L(60, 112, 6, 112, 1.3), L(6, 112, 6, 30, 1.3), L(6, 30, 8, 30, 1.3, ar=True),
     N(150, 118, "window maxed: output z_med", 8.5, "start"), N(150, 132, "keeps non-noisy pixels intact", 8.5, "start")],
    "Level A decides if the median itself is an impulse; Level B decides if the center pixel is",
    ["<strong>Problem:</strong> a fixed median over-smooths when noise is light and fails when noise is dense. The adaptive version <strong>changes the window size</strong> $S_{xy}\\le S_{\\max}$.",
     "<strong>Level A:</strong> if $z_{\\min}<z_{\\text{med}}<z_{\\max}$ the median is not an impulse (go to B); else <strong>grow the window</strong> and repeat.",
     "<strong>Level B:</strong> if $z_{\\min}<z_{xy}<z_{\\max}$ keep the original pixel $z_{xy}$ (it is fine); otherwise output $z_{\\text{med}}$. This <strong>preserves detail</strong> while removing impulses."],
    r"$$z_{\min}<z_{\mathrm{med}}<z_{\max}\ \Rightarrow\ \text{Level B};\qquad z_{\min}<z_{xy}<z_{\max}\ \Rightarrow\ \text{output } z_{xy},\ \text{else } z_{\mathrm{med}}$$",
    "A doctor who touches only the swollen spots: healthy tissue is left alone, and only diseased pixels are replaced.",
    "If S_max is reached and A still fails, output z_med (no further growth). Forgetting this termination rule makes the loop infinite."))

def _bilat():
    cx = 100
    step = _poly([(20, 112), (120, 112), (120, 82), (225, 82)], 2)
    sp = [(x, 70 - 34 * math.exp(-((x - cx) ** 2) / (2 * 28 ** 2))) for x in range(24, 224, 4)]
    pr = [(x, 70 - 34 * math.exp(-((x - cx) ** 2) / (2 * 28 ** 2)) * (1.0 if x <= 118 else 0.04)) for x in range(24, 224, 4)]
    return [L(20, 70, 226, 70, 0.8, d="2 3"), step, _poly(sp, 1.4, "4 3"), _poly(pr, 2.4), C(cx, 112, 3.5),
            N(cx, 128, "p", 9, w="bold"), N(120, 138, "edge", 8, "start"), N(128, 30, "dashed: spatial only", 8, "start"),
            N(128, 42, "solid: × range", 8, "start", "bold"), N(150, 100, "far side gets", 8, "start"), N(150, 112, "≈ 0 weight", 8, "start")]

CARDS.append(card(12, 4, "EDGE-PRESERVING", "Bilateral Filter: Spatial × Range Weights",
    _bilat(),
    "Pixels across the edge look different from p, so the range Gaussian kills their weight",
    [r"<strong>What:</strong> a Gaussian blur that also checks <strong>intensity similarity</strong>: neighbors count only if they are both <strong>near</strong> $p$ (spatial) and <strong>similar</strong> in value (range).",
     r"<strong>How:</strong> weight $=G_{\sigma_s}(\|p-q\|)\cdot G_{\sigma_r}(|I_p-I_q|)$, normalized by $W_p$. Across an edge the range term is ≈ 0, so the edge is <strong>not blurred</strong>.",
     "<strong>Why:</strong> it smooths flat areas and keeps edges, but is nonlinear and <strong>$O(K^2)$ per pixel</strong>; $\\sigma_r$ sets what counts as 'similar', $\\sigma_s$ the neighborhood size."],
    r"$$BF[I]_p=\frac{1}{W_p}\sum_{q\in S}G_{\sigma_s}(\|p-q\|)\,G_{\sigma_r}(|I_p-I_q|)\,I_q$$",
    "Asking only the neighbors who live nearby AND have a similar income about local prices: the rich neighbor across the tracks is politely ignored.",
    "Large σ_r makes the range term ≈ 1 everywhere and the filter degrades to plain Gaussian blur. It also isn't separable."))

def _nlm():
    out = [R(18, 14, 150, 112, "#ffffff", 1.6)]
    out += [R(34, 70, 22, 22, "#e2e8f0", 1.8), N(45, 105, "p", 9, w="bold")]
    for (x, y, lab) in [(100, 28, "w₁"), (120, 90, "w₂"), (66, 28, "w₃")]:
        out += [R(x, y, 22, 22, "#f1f5f9", 1.5)]
    out += [L(56, 76, 100, 44, 1.3, d="4 3"), L(56, 82, 120, 98, 1.3, d="4 3"), L(46, 70, 70, 50, 1.3, d="4 3"),
            N(210, 38, "weights depend", 8.5), N(210, 50, "on PATCH", 8.5), N(210, 62, "similarity,", 8.5), N(210, 74, "not distance", 8.5),
            N(210, 98, "w = e^(−d²/h²)", 8)]
    return out

CARDS.append(card(12, 5, "EDGE-PRESERVING", "Non-Local Means (Patch Similarity)",
    _nlm(),
    "Average pixels whose surrounding PATCHES look alike, wherever they are in the image",
    ["<strong>What:</strong> instead of averaging nearby pixels, average pixels whose <strong>neighborhood patches</strong> look similar, anywhere in the image.",
     r"<strong>How:</strong> weight $w(p,q)=\exp\!\big(-\|P_p-P_q\|^2/h^2\big)$, then $\hat I(p)=\sum_q w(p,q)I(q)/\sum_q w(p,q)$.",
     "<strong>Why:</strong> natural images are <strong>self-similar</strong> (repeating textures and edges), so noise averages out while structure is preserved. Cost: heavy computation; $h$ controls strength."],
    r"$$\hat I(p)=\frac{1}{Z_p}\sum_{q}\exp\!\left(-\frac{\|P_p-P_q\|_2^2}{h^2}\right)I(q)$$",
    "Proofreading by finding the same word elsewhere in a document: copies of the same pattern vote on what the smudged one should be.",
    "Compare PATCHES (e.g. 7×7), not single pixels. Pixel-wise similarity is exactly what the bilateral filter does, and is less robust to noise."))

CARDS.append(card(12, 6, "WORKED BENCHMARK", "Worked Benchmark: Median vs Mean on a 3×3 Window",
    [GRID(24, 20, [[10, 12, 200], [11, 13, 9], [12, 10, 11]], cell=26, shade={(0, 2)}, sz=10),
     N(63, 108, "salt pixel: 200", 8.5), L(110, 58, 138, 58, 1.4, ar=True),
     N(184, 30, "sorted:", 9, w="bold"), N(184, 44, "9 10 10 11", 9), N(184, 56, "11 12 12 13 200", 9),
     N(184, 78, "median = 11", 10, w="bold"), N(184, 98, "mean = 288/9 = 32", 10), N(184, 114, "(skewed by 200)", 8.5)],
    "The outlier 200 drags the mean to 32 but leaves the median at 11",
    ["<strong>Window values:</strong> 10, 12, <strong>200</strong>, 11, 13, 9, 12, 10, 11 (the 200 is a salt-noise pixel).",
     "<strong>Mean</strong> $=288/9=32$: one bad pixel moves the output by 20 gray levels away from the true neighborhood level (~11).",
     "<strong>Median:</strong> sort to 9, 10, 10, 11, <strong>11</strong>, 12, 12, 13, 200; the 5th value is <strong>11</strong>, right where the clean neighborhood sits."],
    r"$$\text{mean}=\frac{288}{9}=32,\qquad \text{median}=11\ \ (5\text{th of } 9)$$",
    "Nine people in a room, one of them a billionaire: the average income is meaningless, but the middle person still tells you what a typical neighbor earns.",
    "The median of an even-sized window is ambiguous (average of the two middle values). Use odd window sizes to avoid this."))

# ============================ 13 · IQA ============================
CARDS.append(card(13, 1, "IMAGE QUALITY", "MSE's Blind Spot",
    [R(14, 28, 54, 54, "#ffffff", 3), N(41, 98, "reference", 8.5),
     R(92, 28, 54, 54, "#ffffff", 1.6, 0, "2 2"), R(96, 32, 46, 46, "none", 1.1, 0, "2 2"), R(100, 36, 38, 38, "none", 0.8, 0, "2 2"), N(119, 98, "blurred", 8.5),
     R(184, 28, 54, 54, "#ffffff", 0.8, 0, "2 2"), R(190, 34, 54, 54, "none", 3), N(212, 98, "shifted", 8.5),
     N(120, 120, "all three can have the SAME MSE", 9.5, w="bold"), N(120, 134, "but look very different to a person", 8.5)],
    "MSE counts squared pixel errors but knows nothing about structure",
    [r"<strong>MSE</strong> $=\frac1{MN}\sum(f-\hat f)^2$ is simple, differentiable and easy to optimize, but it treats <strong>every pixel error equally</strong>.",
     "<strong>Failure:</strong> a slight global shift, a brightness change, a blur and noise can all give the same MSE while looking <strong>very different</strong> to a human.",
     "<strong>Why:</strong> the eye cares about <strong>structure</strong> (edges, textures) and local context, which MSE ignores. That motivates perceptual metrics like SSIM."],
    r"$$\mathrm{MSE}=\frac{1}{MN}\sum_{x,y}\big[f(x,y)-\hat f(x,y)\big]^2$$",
    "Grading an essay by counting letters that differ from the answer key: a one-letter shift of every word ruins the count but not the meaning.",
    "Equal MSE does NOT mean equal quality. Never compare MSE across different distortion types, only within one."))

CARDS.append(card(13, 2, "IMAGE QUALITY", "PSNR in Decibels",
    [L(24, 74, 224, 74, 1.4), ] + [L(24 + i * 40, 68, 24 + i * 40, 80, 1.4) for i in range(6)] +
    [N(24 + i * 40, 94, str(v), 9) for i, v in enumerate([10, 20, 30, 40, 50, 60])] + [N(224, 62, "dB", 8.5, "end"),
     L(64, 60, 144, 60, 4, ), N(104, 50, "typical lossy range", 8.5, w="bold"), N(64, 30, "poor", 8.5), N(184, 40, "near-lossless", 8.5),
     N(120, 116, "PSNR = 10 log₁₀( MAX² / MSE )", 10, w="bold"), N(120, 132, "+10 dB  =  MSE ÷ 10", 8.5)],
    "Every 10 dB is a factor of 10 in MSE; 30–40 dB is the usual lossy-compression range",
    [r"<strong>PSNR</strong> expresses MSE on a log scale relative to the peak value: $10\log_{10}(\text{MAX}^2/\text{MSE})$ with MAX $=255$ for 8-bit images.",
     "<strong>Rule of thumb:</strong> below ~25 dB is clearly degraded, 30–40 dB is typical lossy compression, above ~40–50 dB is visually transparent. Each <strong>+10 dB = MSE ÷ 10</strong>.",
     "It inherits MSE's weaknesses, but is <strong>useful for comparing the same codec at different bit-rates</strong>."],
    r"$$\mathrm{PSNR}=10\log_{10}\frac{\mathrm{MAX}^2}{\mathrm{MSE}}=20\log_{10}\frac{\mathrm{MAX}}{\sqrt{\mathrm{MSE}}}\ \ \mathrm{dB}$$",
    "The Richter scale for errors: each step up is ten times less error energy, not a little bit less.",
    "MAX is the dynamic range (255 for 8-bit, 1.0 for normalized floats, 65535 for 16-bit). Using 255 on 0–1 data gives a nonsense answer."))

CARDS.append(card(13, 3, "IMAGE QUALITY", "SSIM: Luminance × Contrast × Structure",
    [BOX(10, 38, 62, 44, "l(x,y)", "#f1f5f9", 10), N(41, 96, "mean (brightness)", 8), N(81, 64, "×", 14, w="bold"),
     BOX(90, 38, 62, 44, "c(x,y)", "#f1f5f9", 10), N(121, 96, "variance (contrast)", 8), N(161, 64, "×", 14, w="bold"),
     BOX(170, 38, 62, 44, "s(x,y)", "#f1f5f9", 10), N(201, 96, "correlation (structure)", 8),
     N(120, 20, "SSIM = l · c · s", 11, w="bold"),
     N(120, 124, "(2μₓμ_y + C₁)(2σ_xy + C₂) / ((μₓ²+μ_y²+C₁)(σₓ²+σ_y²+C₂))", 7.5)],
    "SSIM compares local mean, local contrast and local correlation, then multiplies the three",
    ["<strong>l</strong> compares local <strong>means</strong> (brightness), <strong>c</strong> compares local <strong>standard deviations</strong> (contrast), and <strong>s</strong> measures the <strong>correlation</strong> between the two patches (structure).",
     "With the common simplification, $\\mathrm{SSIM}=\\dfrac{(2\\mu_x\\mu_y+C_1)(2\\sigma_{xy}+C_2)}{(\\mu_x^2+\\mu_y^2+C_1)(\\sigma_x^2+\\sigma_y^2+C_2)}$, $C_1=(0.01L)^2$, $C_2=(0.03L)^2$ to avoid division by zero.",
     "It equals <strong>1 only if the patches are identical</strong>, lies in $[-1,1]$, and it tracks human judgments better than MSE."],
    r"$$\mathrm{SSIM}(x,y)=\frac{(2\mu_x\mu_y+C_1)(2\sigma_{xy}+C_2)}{(\mu_x^2+\mu_y^2+C_1)(\sigma_x^2+\sigma_y^2+C_2)}$$",
    "Judging a copied painting by three questions: is it as bright, as punchy, and are the shapes in the same places?",
    "C₁, C₂ are tiny stabilizers, not tuning knobs. And SSIM is computed over LOCAL windows, so a single global SSIM is not the standard definition."))

CARDS.append(card(13, 4, "IMAGE QUALITY", "SSIM Map and Mean SSIM",
    [R(14, 20, 90, 70, "#ffffff", 1.6), R(30, 36, 30, 30, "none", 2, 0, "4 3"), R(52, 52, 30, 30, "none", 1.2, 0, "2 3"),
     N(59, 104, "image pair", 8.5), L(110, 55, 132, 55, 1.4, ar=True), N(121, 48, "window", 8),
     R(136, 20, 90, 70, "#e2e8f0", 1.6), N(181, 60, "SSIM map", 9, w="bold"), N(181, 104, "values in [−1, 1]", 8.5),
     N(120, 124, "MSSIM = mean of the map", 10, w="bold"), N(120, 138, "(11×11 Gaussian window, σ = 1.5)", 8)],
    "Slide a window over both images, compute SSIM locally, then average the map",
    ["Compute SSIM in a <strong>sliding window</strong> (typically an 11×11 Gaussian with $\\sigma=1.5$) to get a <strong>quality map</strong> showing where distortion is visible.",
     "<strong>Mean SSIM</strong> (MSSIM) is the average of that map, giving one score per image pair in $[-1,1]$.",
     "<strong>MS-SSIM</strong> repeats the comparison over several downsampled scales to mimic viewing distance and resolution."],
    r"$$\mathrm{MSSIM}(X,Y)=\frac{1}{W}\sum_{j=1}^{W}\mathrm{SSIM}(x_j,y_j)$$",
    "A teacher marking every paragraph and then averaging, instead of reading the whole essay once and giving a gut score.",
    "The SSIM map is more informative than the single mean, since it shows WHERE the damage is. A high mean can hide a badly corrupted patch."))

CARDS.append(card(13, 5, "IMAGE QUALITY", "Full-, Reduced- & No-Reference IQA",
    [BOX(80, 12, 80, 24, "Image quality", "#e2e8f0", 9),
     L(120, 36, 40, 56, 1.3), L(120, 36, 120, 56, 1.3), L(120, 36, 200, 56, 1.3),
     BOX(6, 56, 68, 26, "Full-ref (FR)", "#f1f5f9", 8.5), BOX(86, 56, 68, 26, "Reduced (RR)", "#f1f5f9", 8.5), BOX(166, 56, 68, 26, "No-ref (NR)", "#f1f5f9", 8.5),
     N(40, 98, "MSE, PSNR, SSIM", 8), N(40, 110, "needs the original", 8), N(120, 98, "a few features", 8), N(120, 110, "of the original", 8),
     N(200, 98, "blind: natural", 8), N(200, 110, "scene statistics", 8), N(120, 132, "validate against MOS (SROCC, PLCC)", 8.5, w="bold")],
    "How much of the original you have decides which metric family you can use",
    ["<strong>Full-reference (FR):</strong> compares against the pristine original (MSE, PSNR, SSIM, MS-SSIM). <strong>Reduced-reference (RR):</strong> uses a few features of the original.",
     "<strong>No-reference (NR/blind):</strong> judges quality from the test image alone, using models of <strong>natural-scene statistics</strong> or learned features.",
     "<strong>Ground truth</strong> is subjective <strong>MOS</strong> (mean opinion score); metrics are validated by rank correlation (SROCC) and linear correlation (PLCC) with MOS."],
    r"$$\text{SROCC}=1-\frac{6\sum d_i^2}{n(n^2-1)}\ \ (d_i=\text{rank difference between metric and MOS})$$",
    "Judging a wine: with the original bottle to compare (FR), with only the label's notes (RR), or by taste alone (NR).",
    "A metric that matches MOS on one distortion type may not match on another. Always check the dataset and the distortion types."))

def _psnr():
    pts = [(24 + (math.log10(m) + 0) * 50, 125 - (10 * math.log10(255 ** 2 / m) - 10) * 2.3) for m in [1, 10, 100, 1000]]
    return [AX(24, 125, 226, 14), L(*pts[0], *pts[-1], 2.2), C(*pts[2], 4),
            N(24, 138, "1", 8.5), N(74, 138, "10", 8.5), N(124, 138, "100", 8.5), N(174, 138, "1000", 8.5), N(210, 138, "MSE", 8.5),
            N(pts[2][0] + 8, pts[2][1] - 8, "28.13 dB", 9, "start", "bold"), N(30, 20, "PSNR (dB)", 8.5, "start"), N(160, 40, "−10 dB per decade", 8.5, "start")]

CARDS.append(card(13, 6, "WORKED BENCHMARK", "Worked Benchmark: PSNR at MSE = 100",
    _psnr(),
    "On a log-MSE axis PSNR is a straight line of slope −10 dB per decade",
    ["<strong>Given:</strong> 8-bit image, so $\\text{MAX}=255$ and $\\text{MAX}^2=65025$; measured $\\text{MSE}=100$ (RMS error of 10 gray levels).",
     "<strong>Compute:</strong> $\\text{PSNR}=10\\log_{10}(65025/100)=10\\log_{10}(650.25)\\approx10\\times2.813=\\mathbf{28.13\\ dB}$.",
     "<strong>Sensitivity:</strong> MSE 10 → 38.1 dB, MSE 1 → 48.1 dB, MSE 1000 → 18.1 dB. Cutting RMS error by √10 buys exactly <strong>10 dB</strong>."],
    r"$$\mathrm{PSNR}=10\log_{10}\frac{255^2}{100}=10\log_{10}(650.25)\approx 28.13\ \text{dB}$$",
    "A thermostat dial in tenths: each 10-degree step changes the error by a factor of ten, not by ten units.",
    "Using MAX instead of MAX² inside the log needs 20·log10 instead of 10·log10. Mixing the two forms gives answers off by a factor of 2 in dB."))
