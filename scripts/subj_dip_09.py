"""DIP topic 09 (DCT and KLT). Everyday picture: a street camera on a pole (JPEG blocks of the frame)."""
from street_lib import *
import random

SUBJECT = "DIP"

def d3081(c):
    b = 64
    return svg(c,
        N(14, 12, "one block of the frame, repeated by the DFT", 7.5, "start"),
        L(14, b, 232, b, .5, "1 3"),
        curve(lambda x: b - 6 - 36 * (x - 14) / 72, 14, 86, 20, 1),
        curve(lambda x: b - 6 - 36 * (x - 86) / 72, 86, 158, 20, 1, "3 2"), curve(lambda x: b - 6 - 36 * (x - 158) / 72, 158, 230, 20, 1, "3 2"),
        L(86, b - 44, 86, b - 6, .5, "1 2"), N(88, b + 8, "jump", 7, "start"),
        N(14, 84, "mirrored for the DCT", 7.5, "start"), L(14, 126, 232, 126, .5, "1 3"),
        curve(lambda x: 126 - 6 - 36 * (x - 14) / 72, 14, 86, 20, 1),
        curve(lambda x: 126 - 6 - 36 * (1 - (x - 86) / 72), 86, 158, 20, 1, "3 2"),
        curve(lambda x: 126 - 6 - 36 * (x - 158) / 72, 158, 230, 20, 1, "3 2"),
        N(120, 142, "no jump: only cosines remain", 7.5))

def d3082(c):
    out = [N(56, 12, "8×8 block, after DCT", 7), N(180, 12, "÷ Q, round", 7)]
    for r in range(8):
        for q in range(8):
            sh = "#b8c0cc" if r + q < 3 else ("#e2e6ed" if r + q < 5 else "#ffffff")
            out.append(R(16 + q * 10, 18 + r * 10, 10, 10, sh, .5))
    pts = [(0,0),(0,1),(1,0),(2,0),(1,1),(0,2),(0,3),(1,2),(2,1),(3,0)]
    out.append(poly([(16 + q * 10 + 5, 18 + r * 10 + 5) for r, q in pts], .8))
    out += [arrow(100, 52, 126, 52, 1)]
    for i, v in enumerate([52, -3, 2, 0, 0, 0, 0, 0, 0]):
        out.append(R(130 + i * 11, 40, 11, 14, "#ffffff" if v == 0 else "#e2e6ed", .6)); out.append(N(135.5 + i * 11, 50, str(v), 6.5))
    out += [N(180, 68, "long run of zeros: cheap to code", 7), N(20, 112, "Ĉ(u,v) = round[ C(u,v) / Q(u,v) ]", 7.5, "start"), N(20, 124, "the only lossy step is the rounding", 7.5, "start"), N(20, 136, "DC (top-left) = block average", 7.5, "start")]
    return svg(c, *out)

def d3083(c):
    out = [N(120, 12, "four of the 64 basis images", 7.5)]
    def tile(x, y, kind, lab):
        s = R(x, y, 40, 40, "#ffffff", .8)
        if kind == "dc": s = R(x, y, 40, 40, "#d9dee7", .8)
        elif kind == "u": s += R(x, y, 20, 40, "#b8c0cc", .5)
        elif kind == "v": s += R(x, y, 40, 20, "#b8c0cc", .5)
        else:
            for i in range(4):
                for j in range(4):
                    if (i + j) % 2 == 0: s += R(x + i * 10, y + j * 10, 10, 10, "#b8c0cc", .4)
        return s + N(x + 20, y + 52, lab, 7)
    out += [tile(14, 20, "dc", "(0,0) average"), tile(66, 20, "u", "(1,0)"), tile(118, 20, "v", "(0,1)"), tile(170, 20, "ck", "(3,3) fine")]
    out += [N(120, 92, "C = A f Aᵀ ,   f = Aᵀ C A", 8), N(120, 106, "A Aᵀ = I ⇒ no inverse needed", 7.5), N(120, 120, "Σ f² = Σ C²  (energy kept)", 7.5), N(120, 134, "top-left: smooth, bottom-right: fine bricks", 7.5)]
    return svg(c, *out)

def d3084(c):
    random.seed(3)
    out = [axes(18, 112, 124, 14), N(124, 122, "x₁", 7, "end"), N(14, 14, "x₂", 7, "end")]
    for i in range(26):
        t = random.uniform(-1, 1); n = random.uniform(-.25, .25)
        out.append(C(f(70 + 30 * t + n * 14), f(66 - 30 * t + n * 14), 1.3))
    out += [E(70, 66, 52, 18, -45, "none", 1, "3 2"), arrow(70, 66, 104, 32, 1), N(106, 28, "φ₁ (λ₁ big)", 7, "start"), arrow(70, 66, 88, 84, 1), N(90, 94, "φ₂", 7, "start"),
            N(180, 44, "Cₓφᵢ = λᵢφᵢ", 8), N(180, 58, "y = Φᵀ(x − μ)", 8), N(180, 72, "Cᵧ = Λ", 8), N(180, 86, "MSEₖ = Σ λᵢ (i > k)", 7.5),
            N(120, 136, "pairs of neighbouring street pixels line up along φ₁", 7.5)]
    return svg(c, *out)

def d3085(c):
    out = [N(52, 12, "C = [ρ^|i−j|]", 7.5)]
    for i in range(6):
        for j in range(6):
            d = abs(i - j)
            out.append(R(14 + j * 13, 18 + i * 13, 13, 13, ["#8b95a5", "#b8c0cc", "#d9dee7", "#e8ebf0", "#f4f6f9", "#ffffff"][d], .4))
    out += [N(52, 108, "neighbours correlate (ρ ≈ 0.95)", 6.5),
            N(170, 12, "eigenvectors ≈ cosines", 7.5), L(110, 36, 232, 36, .5, "1 3"), L(110, 76, 232, 76, .5, "1 3"),
            curve(lambda x: 36 - 10 * math.cos(math.pi * (x - 110) / 122), 110, 232, 40, 1), N(114, 54, "u = 1", 6.5, "start"),
            curve(lambda x: 76 - 10 * math.cos(2 * math.pi * (x - 110) / 122), 110, 232, 50, 1, "3 2"), N(114, 94, "u = 2", 6.5, "start"),
            N(120, 124, "ρ → 1 ⇒ Φ(KLT) ≈ A(DCT)", 8), N(120, 137, "near-optimal, fixed basis, fast algorithm", 7.5)]
    return svg(c, *out)

def d3086(c):
    return svg(c,
        axes(18, 112, 124, 14), N(124, 122, "x₁", 7, "end"), N(14, 14, "x₂", 7, "end"),
        E(70, 66, 40, 20, -45, "#f1f5f9", 1), arrow(70, 66, 100, 36, 1), N(106, 22, "φ₁ = (1,1)/√2", 7, "start"), N(106, 31, "λ₁ = 3", 7, "start"),
        arrow(70, 66, 84, 80, 1), N(88, 92, "φ₂ = (1,−1)/√2, λ₂ = 1", 7, "start"),
        N(190, 24, "C = [[2, 1], [1, 2]]", 7.5), N(190, 38, "(2 − λ)² − 1 = 0", 7.5),
        R(150, 52, 78, 12, "#ffffff", .8), R(150, 52, 58.5, 12, "#d9dee7", .8), N(189, 61, "3 ⇒ 75%", 7), R(150, 68, 78, 12, "#ffffff", .8), R(150, 68, 19.5, 12, "#f1f5f9", .8), N(160, 77, "1", 7),
        N(120, 120, "y₁ = (x₁ + x₂)/√2 (average) , y₂ = (x₁ − x₂)/√2 (difference)", 7),
        N(120, 134, "3 + 1 = 4 = 2 + 2 : the trace is conserved", 7.5))

CARDS = {
3081: dict(d=d3081, stmtKind="DEFINITION",
  statement=r"<b>Discrete cosine transform (DCT-II).</b> For a block $f(0),\dots,f(N-1)$: $C(u)=\alpha(u)\sum_{x=0}^{N-1}f(x)\cos\!\Big[\frac{(2x+1)u\pi}{2N}\Big]$, with $\alpha(0)=\sqrt{1/N}$ and $\alpha(u)=\sqrt{2/N}$ for $u\gt0$. It equals the DFT (up to a phase and scale) of the even, mirror-image extension of $f$, so its coefficients are real and there is no boundary discontinuity.",
  hint="Why does JPEG cut the frame into blocks and use cosines, not the plain DFT?",
  breakdown=[r"<strong>$\cos\big[(2x+1)u\pi/2N\big]$ = a cosine that fits the block.</strong> The $(2x+1)/2$ puts the sample in the middle of its cell, so the wave meets the block ends without a jump.",
             r"<strong>$\sum f(x)\cos[\cdot]$ = how much of that cosine the block has.</strong> A real number for each frequency $u$; $u=0$ is the block average.",
             r"<strong>$\alpha(u)$ = scale factors that make the transform orthonormal.</strong> Without them the basis would have unequal lengths and energy would not be preserved."],
  conn=r"<strong>One block of the street frame.</strong> The recorder cuts the frame into small blocks. The DFT would treat each block as repeating, creating a jump where the right end meets the left; mirroring the block removes that jump.",
  cap="A block of the street frame, repeated by the DFT, jumps where its right end meets the left (dashed). Mirrored for the DCT it is smooth, so only cosines are needed."),
3082: dict(d=d3082, stmtKind="ALGORITHM",
  statement=r"<b>JPEG transform coding.</b> Split the image into $8\times8$ blocks, take the 2D DCT $C(u,v)$ of each, quantize $\hat C(u,v)=\operatorname{round}\big[C(u,v)/Q(u,v)\big]$ with a table $Q$ whose entries grow with frequency, scan the coefficients in zig-zag order, and entropy-code the result (run-length for the zero runs, differential coding for DC). The DCT is invertible; all loss comes from the rounding.",
  hint="After the DCT, where does the energy of a smooth street block end up?",
  breakdown=[r"<strong>Energy in the top-left corner.</strong> A smooth block is mostly its average and a few slow variations, so a handful of low-frequency coefficients hold nearly everything.",
             r"<strong>$\operatorname{round}[C/Q]$ = the lossy step.</strong> Dividing by large numbers at high frequencies and rounding turns the weak coefficients into zeros.",
             r"<strong>Zig-zag order = zeros in one long run.</strong> Walking the block from the top-left corner outward puts the zeros at the end, where run-length coding stores them as one count."],
  conn=r"<strong>Fitting a day of footage on the recorder.</strong> Every $8\times8$ block of the street frame is reduced to a few numbers followed by a long run of zeros. Only the rounding discards information.",
  cap="After the 8×8 DCT the large coefficients sit top-left (DC = block average). Dividing by Q and rounding gives 52, −3, 2, then zeros along the zig-zag scan."),
3083: dict(d=d3083, stmtKind="PROPOSITION",
  statement=r"<b>2D DCT as a separable orthonormal transform.</b> The 2D DCT of an $N\times N$ block is $C(u,v)=\alpha(u)\alpha(v)\sum_{x,y}f(x,y)\cos\frac{(2x+1)u\pi}{2N}\cos\frac{(2y+1)v\pi}{2N}$. In matrix form $C=AfA^{\top}$ with $A$ orthogonal ($AA^{\top}=I$), so $f=A^{\top}CA$ and $\sum f^2=\sum C^2$ (Parseval).",
  hint="Why is inverting the DCT as easy as transposing a matrix?",
  breakdown=[r"<strong>$C=AfA^{\top}$ = rows, then columns.</strong> The 2D transform applies the 1D matrix $A$ down each column and along each row (separability).",
             r"<strong>$AA^{\top}=I$ = orthonormal.</strong> Each basis image has length 1 and is perpendicular to the others, so the inverse is the transpose: $f=A^{\top}CA$.",
             r"<strong>$\sum f^2=\sum C^2$ = no energy gained or lost.</strong> The coefficients are the block rewritten in 64 fixed cosine patterns, from smooth (top-left) to fine checkerboard (bottom-right)."],
  conn=r"<strong>Building a block from patterns.</strong> A block of the shop-front brick wall is a weighted sum of 64 fixed patterns; the coarse ones carry the overall brightness, the fine checkerboards only the brick texture.",
  cap="Four of the 64 basis images: the flat average (0,0), a left-right split (1,0), a top-bottom split (0,1) and a fine checkerboard (3,3). The block is a weighted sum of them: C = A f Aᵀ."),
3084: dict(d=d3084, stmtKind="THEOREM",
  statement=r"<b>Karhunen–Loève transform (KLT).</b> Let $x$ be a random vector with mean $\mu$ and covariance $C_x$, and let $\varphi_i$ be orthonormal eigenvectors of $C_x$ with eigenvalues $\lambda_1\ge\lambda_2\ge\dots$. The transform $y=\Phi^{\top}(x-\mu)$ has the diagonal covariance $C_y=\Lambda=\operatorname{diag}(\lambda_i)$, and among all orthonormal linear transforms, keeping the first $k$ coefficients gives the smallest mean-squared error $\sum_{i\gt k}\lambda_i$.",
  hint="Which axes of a cloud of neighbouring pixel pairs hold the most variance?",
  breakdown=[r"<strong>$C_x\varphi_i=\lambda_i\varphi_i$ = the long and short axes of the cloud.</strong> The eigenvectors point along the directions where the data varies most and least; $\lambda_i$ is the spread along each.",
             r"<strong>$y=\Phi^{\top}(x-\mu)$ = measure along those axes.</strong> Subtract the mean, then project onto the eigenvectors; the new coordinates are uncorrelated.",
             r"<strong>$\mathrm{MSE}_k=\sum_{i\gt k}\lambda_i$ = what dropping the small axes costs.</strong> Keep the top $k$ and the error is the sum of the eigenvalues you dropped, the smallest any orthonormal choice can give."],
  conn=r"<strong>Two neighbouring street pixels.</strong> They are almost always similar, so plotting one against the other makes a cloud along the diagonal. The KLT turns the axes to follow the cloud: one big coefficient (the average), one small (the difference).",
  cap="Pairs of neighbouring pixels (x₁, x₂) form a cloud along the diagonal. The eigenvectors φ₁, φ₂ of the covariance Cₓ are its axes, with spreads λ₁ ≫ λ₂."),
3085: dict(d=d3085, stmtKind="PROPOSITION",
  statement=r"<b>DCT as an approximate KLT.</b> For a first-order Markov process with covariance $C=\big[\rho^{|i-j|}\big]$ and $\rho$ close to 1 (typical of natural images, $\rho\approx0.9$–$0.95$), the KLT basis is approximately the DCT basis: $\Phi_{\rm KLT}\approx A_{\rm DCT}$. The DCT is therefore near-optimal for compaction while being data-independent and having a fast algorithm.",
  hint="Why does JPEG not compute a fresh KLT for every image?",
  breakdown=[r"<strong>$C_{ij}=\rho^{|i-j|}$ = neighbours agree, far pixels forget.</strong> The correlation falls off with distance; for $\rho\approx1$ close pixels are almost equal.",
             r"<strong>$\rho\to1$ = the eigenvectors become cosines.</strong> For this banded matrix the exact eigenvectors approach the DCT basis vectors.",
             r"<strong>$\Phi_{\rm KLT}\approx A_{\rm DCT}$ = the engineering reason for JPEG.</strong> Almost the best compaction, with a fixed basis the decoder already knows and a fast algorithm."],
  conn=r"<strong>The recorder's fixed rulebook.</strong> A street frame is smooth enough that neighbouring pixels correlate strongly, so the same fixed cosine rulebook works on every frame without sending extra information.",
  cap="Neighbouring pixels correlate as ρ^|i−j| (darker = more correlated). The eigenvectors of such a matrix look like cosines of increasing frequency, so the fixed DCT is near the best basis."),
3086: dict(d=d3086, stmtKind="WORKED EXAMPLE",
  statement=r"<b>Example.</b> For $C_x=\begin{pmatrix}2&1\\1&2\end{pmatrix}$: $\det(C_x-\lambda I)=(2-\lambda)^2-1=0$ gives $\lambda_1=3$, $\lambda_2=1$, with eigenvectors $\varphi_1=\tfrac1{\sqrt2}(1,1)$ and $\varphi_2=\tfrac1{\sqrt2}(1,-1)$. So $y_1=\frac{x_1+x_2}{\sqrt2}$, $y_2=\frac{x_1-x_2}{\sqrt2}$, and the variance splits $2,2\to3,1$: $y_1$ carries $75\%$ of the total ($\lambda_1+\lambda_2=4=\operatorname{tr}C_x$).",
  hint="If two neighbouring pixels have variance 2 each and covariance 1, what do the sum and difference carry?",
  breakdown=[r"<strong>$(2-\lambda)^2-1=0\Rightarrow\lambda=3,1$ = the two spreads.</strong> The roots of the characteristic polynomial of the covariance.",
             r"<strong>$\varphi_1=(1,1)/\sqrt2,\ \varphi_2=(1,-1)/\sqrt2$ = average and difference.</strong> Exactly the two-point DCT (Haar) basis.",
             r"<strong>$3+1=4=2+2$ = the total variance is conserved.</strong> Coding only $y_1$ keeps $3/4=75\%$ of it; the trace is a check on the arithmetic."],
  conn=r"<strong>Two neighbouring pixels of the street frame.</strong> Their sum is the big, useful number; their difference is small. Rotating the axes by 45° moves most of the information into one coefficient.",
  cap="The covariance [[2, 1], [1, 2]] gives an ellipse with axes φ₁ = (1,1)/√2 (λ₁ = 3) and φ₂ = (1,−1)/√2 (λ₂ = 1); y₁ keeps 75% of the variance."),
}

STORY = {
 3081: dict(s="STORY 4 · STEP 1 · COSINES FOR BLOCKS", b="To store the street frame in small blocks, mirror each block and use <b>cosines</b>: no jump at the edges, real coefficients.",
   f=[["3061", "the DFT"], ["3014", "work on the Y plane"]], n=[["3082", "JPEG"], ["3083", "the 64 patterns"]]),
 3082: dict(s="STORY 4 · STEP 2 · JPEG", b="Smooth blocks put their energy in a few low coefficients; <b>quantizing</b> and zig-zag scanning leave long runs of zeros.",
   f=[["3081", "the DCT"]], n=[["3083", "the basis images"], ["3121", "how much quality is lost"]]),
 3083: dict(s="STORY 4 · STEP 3 · THE 64 PATTERNS", b="The 2D DCT is <b>orthonormal</b>: $C=AfA^\\top$, inverse is the transpose, energy is kept.",
   f=[["3081", "the 1D DCT"]], n=[["3084", "a data-driven basis"]]),
 3084: dict(s="STORY 4 · STEP 4 · THE BEST BASIS", b="The <b>KLT</b> uses the eigenvectors of the data's covariance: the best compaction, but it depends on the data.",
   f=[["3083", "a fixed basis"]], n=[["3085", "the DCT is nearly as good"], ["3181", "eigenfaces use the same idea"]]),
 3085: dict(s="STORY 4 · STEP 5 · WHY THE DCT", b="For smooth images ($\\rho\\approx1$) the KLT basis is nearly the DCT: <b>fixed basis, near-best compaction</b>.",
   f=[["3084", "KLT"]], n=[["3086", "two-pixel example"]]),
 3086: dict(s="STORY 4 · STEP 6 · CHECK BY HAND", b="Two pixels: the sum and difference are the KLT, with $75\\%$ of the variance in the first.",
   f=[["3084", "KLT"]], n=[["3091", "next: look at several scales at once"]]),
}
FIX = build_fix(CARDS)
