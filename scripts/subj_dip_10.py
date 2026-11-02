"""DIP topic 10 (wavelets, multiresolution). Everyday picture: a street camera on a pole."""
from street_lib import *

SUBJECT = "DIP"

def d3091(c):
    out = [N(60, 10, "STFT: one window", 7.5), axes(14, 100, 112, 16), N(112, 110, "x", 7, "end"), N(10, 16, "f", 7, "end"), N(60, 124, "same tiles everywhere", 7)]
    for i in range(4):
        for j in range(4):
            out.append(R(18 + i * 23, 16 + j * 21, 23, 21, "#ffffff", .6))
    out += [N(180, 10, "wavelet: scaled tiles", 7.5), axes(134, 100, 232, 16), N(232, 110, "x", 7, "end"), N(130, 16, "f", 7, "end"), N(180, 124, "narrow at high f, wide at low f", 7)]
    for k in range(8): out.append(R(138 + k * 11.5, 16, 11.5, 21, "#f1f5f9", .6))
    for k in range(4): out.append(R(138 + k * 23, 37, 23, 21, "#ffffff", .6))
    for k in range(2): out.append(R(138 + k * 46, 58, 46, 21, "#f1f5f9", .6))
    out.append(R(138, 79, 92, 21, "#ffffff", .6))
    return svg(c, *out)

def d3092(c):
    return svg(c,
        E(120, 62, 100, 46, 0, "#ffffff", 1), E(120, 62, 66, 31, 0, "#f1f5f9", 1), E(120, 62, 34, 16, 0, "#d9dee7", 1),
        N(120, 65, "V₀", 8), N(120, 44, "V₁", 8), N(120, 24, "V₂", 8),
                N(60, 60, "W₁", 8), N(120, 90, "W₀", 8),
        N(120, 12, "ladder of coarse ⊂ fine pictures of the street", 7.5), N(120, 124, "V₁ = V₀ ⊕ W₀   ,   V₂ = V₁ ⊕ W₁", 8),
        N(120, 138, "f = Σ c φ  +  Σ d ψ  (coarse picture + stack of details)", 7))

def d3093(c):
    return svg(c,
        N(14, 54, "x", 8), arrow(22, 50, 40, 30, 1), arrow(22, 50, 40, 70, 1),
        R(40, 22, 28, 16, "#f1f5f9", 1), N(54, 33, "h₀", 7), arrow(68, 30, 82, 30, 1), R(82, 22, 20, 16, "#ffffff", 1), N(92, 33, "↓2", 7), arrow(102, 30, 116, 30, 1), N(122, 34, "a", 8),
        R(40, 62, 28, 16, "#f1f5f9", 1), N(54, 73, "h₁", 7), arrow(68, 70, 82, 70, 1), R(82, 62, 20, 16, "#ffffff", 1), N(92, 73, "↓2", 7), arrow(102, 70, 116, 70, 1), N(122, 74, "d", 8),
        arrow(130, 30, 144, 30, 1), R(144, 22, 20, 16, "#ffffff", 1), N(154, 33, "↑2", 7), arrow(164, 30, 176, 30, 1), R(176, 22, 24, 16, "#f1f5f9", 1), N(188, 33, "g₀", 7),
        arrow(130, 70, 144, 70, 1), R(144, 62, 20, 16, "#ffffff", 1), N(154, 73, "↑2", 7), arrow(164, 70, 176, 70, 1), R(176, 62, 24, 16, "#f1f5f9", 1), N(188, 73, "g₁", 7),
        arrow(200, 30, 214, 48, 1), arrow(200, 70, 214, 52, 1), N(224, 54, "x̂", 8),
        N(120, 100, "Haar: a[n] = (x[2n] + x[2n+1])/√2", 7.5), N(120, 112, "d[n] = (x[2n] − x[2n+1])/√2", 7.5),
        N(120, 126, "G₀H₀ + G₁H₁ = 2 ,  aliases cancel ⇒ x̂ = x", 7.5))

def d3094(c):
    out = [R(20, 12, 96, 96, "#ffffff", 1), L(68, 12, 68, 108, .8), L(20, 60, 116, 60, .8),
           R(20, 12, 48, 48, "#f1f5f9", .8), L(44, 12, 44, 60, .6), L(20, 36, 68, 36, .6),
           N(32, 28, "LL₂", 7), N(56, 28, "HL₂", 7), N(32, 52, "LH₂", 7), N(56, 52, "HH₂", 7),
           N(92, 38, "HL₁", 8), N(44, 88, "LH₁", 8), N(92, 88, "HH₁", 8),
           N(176, 20, "LL = thumbnail", 7.5), N(176, 36, "HL = vertical edges", 7.5), N(176, 52, "LH = horizontal edges", 7.5), N(176, 68, "HH = diagonals", 7.5),
           N(176, 90, "recurse on LL only", 7.5), N(176, 104, "size(LL_J) = M/2ᴶ × N/2ᴶ".replace("LL_J", "LLⱼ"), 7)]
    out.append(N(120, 132, "total coefficients = MN: critically sampled", 7.5))
    return svg(c, *out)

def d3095(c):
    return svg(c,
        N(64, 10, "hard", 8), axes(14, 100, 114, 14), N(114, 110, "c", 7, "end"), N(10, 16, "ĉ", 7, "end"),
        L(14, 100, 114, 14, .5, "1 3"), L(64, 100, 64, 100, 1), L(14, 100, 54, 100, 1), L(54, 100, 54, 62, .6), L(54, 62, 114, 14, 1),
        L(14, 100, 74, 100, 1) if False else "", N(54, 110, "T", 7),
        N(176, 10, "soft", 8), axes(126, 100, 226, 14), N(226, 110, "c", 7, "end"),
        L(126, 100, 166, 100, 1), L(166, 100, 226, 40, 1), N(166, 110, "T", 7), L(126, 100, 226, 14, .5, "1 3"),
        N(120, 128, "ĉ(hard) = c · 1(|c| > T)", 7.5), N(120, 140, "ĉ(soft) = sign(c)(|c| − T)₊ ,  T = σ√(2 ln N)", 7.5))

def d3096(c):
    return svg(c,
        N(10, 14, "street row", 7, "start"), pix(70, 6, [[4, 6, 10, 12]], 25, 8),
        arrow(120, 34, 120, 44, 1), N(128, 42, "pairs: average, half-difference", 6.5, "start"),
        N(10, 62, "level 1", 7, "start"), pix(70, 48, [[5, 11, -1, -1]], 25, 8, {(0, 2), (0, 3)}),
        arrow(95, 76, 95, 86, 1), N(103, 84, "again on the averages", 6.5, "start"),
        N(10, 104, "level 2", 7, "start"), pix(70, 90, [[8, -3, -1, -1]], 25, 8, {(0, 1), (0, 2), (0, 3)}),
        N(120, 128, "rebuild: 5 = 8 + (−3) , 11 = 8 − (−3)", 7.5), N(120, 140, "4 = 5 + (−1) , 6 = 5 − (−1) , 10 = 11 + (−1) , 12 = 11 − (−1)", 7))

CARDS = {
3091: dict(d=d3091, stmtKind="DEFINITION",
  statement=r"<b>Wavelet family and time-frequency tiling.</b> From a mother wavelet $\psi$ (of zero mean and finite energy) a wavelet family is formed by dilation and translation, $\psi_{j,k}(x)=2^{j/2}\psi(2^jx-k)$, and the wavelet coefficients of $f$ are $c_{j,k}=\langle f,\psi_{j,k}\rangle$. Unlike the short-time Fourier transform, which tiles the time-frequency plane with identical rectangles, the wavelet tiles are narrow in position and tall in frequency at high frequencies, and wide and short at low frequencies; every tile has the same area (Heisenberg).",
  hint="Why use narrow windows for a sharp kerb edge and wide windows for the smooth road?",
  breakdown=[r"<strong>$\psi(2^jx-k)$ = the same wave, squeezed by $2^j$ and moved to $k$.</strong> One mother shape, copied at every scale and position.",
             r"<strong>$2^{j/2}$ = keep the length the same.</strong> Squeezing shrinks the energy, so this factor makes every copy the same size in energy terms.",
             r"<strong>$c_{j,k}=\langle f,\psi_{j,k}\rangle$ = how much of that copy the frame contains.</strong> It says which scale ($j$) and where ($k$): the tile in the plane."],
  conn=r"<strong>Sharp edge, smooth road.</strong> The kerb edge needs a tiny, quick wave that pins down exactly where it is; the long smooth road is described by a wide, slow wave. A wavelet uses both automatically, the fixed STFT window cannot.",
  cap="Left: the STFT cuts the position–frequency plane into equal tiles. Right: wavelet tiles are narrow at high frequency and wide at low frequency, all with the same area."),
3092: dict(d=d3092, stmtKind="DEFINITION",
  statement=r"<b>Multiresolution analysis (MRA).</b> A nested sequence of closed subspaces $\cdots\subset V_0\subset V_1\subset V_2\subset\cdots$ of $L^2$, where $V_j$ is spanned by integer shifts of $\varphi(2^jx)$ (the scaling function), with $\bigcap V_j=\{0\}$ and $\overline{\bigcup V_j}=L^2$. The detail space $W_j$ is the orthogonal complement of $V_j$ in $V_{j+1}$, $V_{j+1}=V_j\oplus W_j$, spanned by the shifts of $\psi(2^jx)$; hence $f=\sum_k c_{J,k}\varphi_{J,k}+\sum_{j\ge J}\sum_k d_{j,k}\psi_{j,k}$.",
  hint="Which part do you add to a coarse picture of the street to get the next finer one?",
  breakdown=[r"<strong>$V_j\subset V_{j+1}$ = each finer picture contains the coarser one.</strong> $V_j$ holds the frame down to detail size $2^{-j}$.",
             r"<strong>$V_{j+1}=V_j\oplus W_j$ = the next picture is the old one plus new details.</strong> $W_j$ is exactly what is new, perpendicular to $V_j$, not a set difference.",
             r"<strong>$f=\sum c\,\varphi+\sum d\,\psi$ = a coarse picture plus a stack of details.</strong> The scaling function $\varphi$ builds each $V_j$ and the wavelet $\psi$ builds each $W_j$."],
  conn=r"<strong>Zooming the street out and in.</strong> A thumbnail of the street is the coarsest picture; each zoom step adds only the new fine details. The sum of the thumbnail and all the detail layers is the full frame.",
  cap="Nested pictures V₀ ⊂ V₁ ⊂ V₂ of the street. W₀ is what V₁ has beyond V₀ and W₁ what V₂ has beyond V₁: V₂ = V₀ ⊕ W₀ ⊕ W₁."),
3093: dict(d=d3093, stmtKind="THEOREM",
  statement=r"<b>Two-channel perfect-reconstruction filter bank.</b> The analysis bank filters $x$ with a low-pass $h_0$ and a high-pass $h_1$ and downsamples each by 2; the synthesis bank upsamples by 2, filters with $g_0,g_1$ and adds. The output equals the input (up to delay) if and only if the aliasing term cancels, $G_0(z)H_0(-z)+G_1(z)H_1(-z)=0$, and the distortion term is a pure delay, $G_0(z)H_0(z)+G_1(z)H_1(z)=2z^{-l}$. The Haar bank is $a[n]=\frac{x[2n]+x[2n+1]}{\sqrt2}$, $d[n]=\frac{x[2n]-x[2n+1]}{\sqrt2}$.",
  hint="After keeping half the samples in each channel, how can you still rebuild every pixel?",
  breakdown=[r"<strong>$h_0$ then $\downarrow2$ = the coarse half.</strong> A low-pass keeps the smooth part, and halving the samples makes it a half-size picture.",
             r"<strong>$h_1$ then $\downarrow2$ = the detail half.</strong> A high-pass keeps the edges; together the two halves have as many samples as the original.",
             r"<strong>Haar: average and difference.</strong> $(x_{2n}+x_{2n+1})/\sqrt2$ and $(x_{2n}-x_{2n+1})/\sqrt2$. The synthesis filters are chosen so the aliasing from the downsampling cancels exactly."],
  conn=r"<strong>Splitting a row of the street frame in two.</strong> Take neighbouring pixels in pairs: their average goes into a half-size thumbnail row, their difference into a detail row. Nothing is lost because the pair can be rebuilt from the two numbers.",
  cap="The input x splits into approximation a (low-pass h₀, keep every second sample) and detail d (high-pass h₁). Upsampling and g₀, g₁ then rebuild x̂ = x."),
3094: dict(d=d3094, stmtKind="ALGORITHM",
  statement=r"<b>2D discrete wavelet transform (pyramid).</b> Apply the 1D analysis filter bank along the rows and then along the columns of an $M\times N$ image. This gives four subbands of size $\frac M2\times\frac N2$: $LL$ (low-low), $HL$, $LH$ and $HH$. Repeat on the $LL$ band for $J$ levels; $LL_J$ has size $\frac M{2^J}\times\frac N{2^J}$, and the total number of coefficients stays $MN$ (critical sampling).",
  hint="Which subband of the street frame holds the thumbnail, and which holds the horizontal edges?",
  breakdown=[r"<strong>LL = low-pass both ways.</strong> A half-size thumbnail of the frame, which is split again at the next level.",
             r"<strong>HL, LH = one high-pass, one low-pass.</strong> They respond to edges in one direction each: vertical edges in HL and horizontal edges in LH, in the usual naming.",
             r"<strong>HH = high-pass both ways.</strong> Diagonal detail and noise. Only $LL$ is split again, so the result is a pyramid whose detail bands are mostly tiny numbers."],
  conn=r"<strong>The street frame as a pyramid.</strong> The thumbnail sits in the corner and the building's horizontal window ledges, vertical poles and diagonal wires fall into three different detail bands.",
  cap="Level 1 splits the frame into LL, HL, LH, HH; level 2 splits only LL again, giving LL₂, HL₂, LH₂, HH₂. The thumbnail LLⱼ is M/2ᴶ × N/2ᴶ."),
3095: dict(d=d3095, stmtKind="ALGORITHM",
  statement=r"<b>Wavelet shrinkage denoising.</b> For noisy coefficients $c$ and a threshold $T$: hard thresholding $\hat c=c\,\mathbf 1_{|c|\gt T}$; soft thresholding $\hat c=\operatorname{sign}(c)\,(|c|-T)_+$. The universal (VisuShrink) threshold is $T=\sigma\sqrt{2\ln N}$ for noise level $\sigma$, often estimated as $\sigma=\operatorname{median}(|d_1|)/0.6745$ from the finest detail band. Only the detail bands are thresholded.",
  hint="Why can you zero the tiny detail coefficients of a noisy night frame without losing the shapes?",
  breakdown=[r"<strong>Few big, many small.</strong> The real edges of the street give a few large detail coefficients; white noise spreads into many small ones.",
             r"<strong>$c\,\mathbf 1_{|c|\gt T}$ = hard: keep or kill.</strong> A coefficient above $T$ is kept as it is, anything below is set to zero; the jump at $T$ can leave visible artifacts.",
             r"<strong>$\operatorname{sign}(c)(|c|-T)_+$ = soft: shrink by $T$.</strong> Survivors are pulled toward zero, so the map is continuous. $T=\sigma\sqrt{2\ln N}$ sets the cut from the noise level."],
  conn=r"<strong>Cleaning the night footage.</strong> Transform the noisy frame, zero the small detail coefficients, keep the thumbnail band untouched, and transform back: the speckle goes, the edges of the building stay.",
  cap="Hard thresholding keeps coefficients above T unchanged and zeroes the rest; soft thresholding also shrinks the survivors by T. Dotted: no change."),
3096: dict(d=d3096, stmtKind="WORKED EXAMPLE",
  statement=r"<b>Example.</b> Unnormalized Haar transform (average and half-difference) of $x=[4,6,10,12]$. Level 1: $(4,6)\to(5,-1)$, $(10,12)\to(11,-1)$, giving $[5,11\mid-1,-1]$. Level 2 on the averages $(5,11)\to(8,-3)$, giving $[8\mid-3\mid-1,-1]$. Reconstruction: $5=8+(-3)$, $11=8-(-3)$, then $4=5+(-1)$, $6=5-(-1)$, $10=11+(-1)$, $12=11-(-1)$.",
  hint="After two levels of pairing, which numbers are the thumbnail and which are the details?",
  breakdown=[r"<strong>Level 1: $(4,6)\to5,\,-1$ and $(10,12)\to11,\,-1$.</strong> The average of each pair and half their difference: $[5,11\mid-1,-1]$.",
             r"<strong>Level 2 on $(5,11)$: average $8$, detail $-3$.</strong> The averages are split again, and the pyramid is $[8\mid-3\mid-1,-1]$.",
             r"<strong>Rebuild: sum and difference back.</strong> $5=8+(-3)$, $11=8-(-3)$, then each pair from its average and detail: perfect reconstruction, and the small details compress well."],
  conn=r"<strong>Four pixels across the kerb.</strong> The 8 is the overall brightness, the −3 says the second half is brighter, and the two −1s say each pair rises slightly: the same numbers rebuilt exactly. ",
  cap="Four pixels [4, 6, 10, 12] become [5, 11 | −1, −1] and then [8 | −3 | −1, −1]. Averages go on to the next level; details stay."),
}

STORY = {
 3091: dict(s="STORY 4 · STEP 7 · SEVERAL SCALES AT ONCE", b="Fourier says <i>which</i> frequencies, not <i>where</i>. <b>Wavelets</b> use tiles that are narrow for fine detail and wide for smooth areas.",
   f=[["3061", "Fourier"], ["3081", "block transforms"]], n=[["3092", "the ladder of pictures"]]),
 3092: dict(s="STORY 4 · STEP 8 · THE LADDER", b="Each finer picture is the coarser one plus <b>new details</b>: $V_{j+1}=V_j\\oplus W_j$.",
   f=[["3091", "scaled wavelets"]], n=[["3093", "the filters that do it"]]),
 3093: dict(s="STORY 4 · STEP 9 · THE FILTER BANK", b="A low-pass and a high-pass, each followed by $\\downarrow2$, split the signal; the synthesis bank <b>cancels the aliasing</b> and rebuilds it.",
   f=[["3092", "MRA"], ["3074", "downsampling"], ["3075", "upsampling"]], n=[["3094", "in two dimensions"], ["3096", "by hand"]]),
 3094: dict(s="STORY 4 · STEP 10 · IN 2D", b="Rows then columns give <b>LL, HL, LH, HH</b>; recurse on LL for a pyramid.",
   f=[["3093", "1D bank"]], n=[["3095", "clean the detail bands"]]),
 3095: dict(s="STORY 4 · STEP 11 · DENOISE", b="Real edges are <b>few and large</b>, noise is <b>many and small</b>: threshold the detail bands.",
   f=[["3094", "subbands"]], n=[["3101", "noise in restoration"], ["3111", "other ways to clean noise"]]),
 3096: dict(s="STORY 4 · STEP 12 · CHECK BY HAND", b="Four pixels through two Haar levels and back.",
   f=[["3093", "Haar"]], n=[["3101", "next: undo a blur"]]),
}
FIX = build_fix(CARDS)
