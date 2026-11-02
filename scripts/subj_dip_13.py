"""DIP topic 13 (image quality: MSE, PSNR, SSIM). Everyday picture: a street camera on a pole (original vs compressed frame)."""
from street_lib import *

SUBJECT = "DIP"

def mini(x, y, kind, lab, w=50, h=40):
    out = frame(x, y, w, h) + building(x + 4, y + 6, 16, 28, 2, 1, "#f1f5f9")
    px = x + 36 + (3 if kind == "shift" else 0)
    out += person(px, y + 34, 22)
    if kind == "blur": out += E(px, y + 24, 7, 12, 0, "none", .6, "2 2")
    if kind == "noise":
        for k in range(10): out += C(f(x + 4 + (k * 17) % 44), f(y + 4 + (k * 11) % 32), .8)
    return out + N(x + w / 2, y + h + 10, lab, 6.5)

def d3121(c):
    return svg(c,
        mini(8, 14, "orig", "original"), mini(66, 14, "shift", "shifted"), mini(124, 14, "blur", "blurred"), mini(182, 14, "noise", "noisy"),
        N(120, 84, "all four can have MSE = 100", 8),
        N(120, 100, "MSE = (1/MN) ΣΣ [f(x,y) − f̂(x,y)]²", 7.5),
        N(120, 116, "every pixel error counts the same, wherever it is", 7.5),
        N(120, 130, "the eye sees structure, MSE does not", 7.5))

def d3122(c):
    out = [L(20, 66, 220, 66, 1), N(120, 14, "PSNR = 10 log₁₀ (MAX² / MSE) dB", 8)]
    for i, (db, mse) in enumerate(((18.1, 1000), (28.1, 100), (38.1, 10), (48.1, 1))):
        x = 30 + i * 56
        out += [L(x, 62, x, 70, 1), N(x, 82, f"{db} dB", 7), N(x, 52, f"MSE {mse}", 7)]
    out += [N(75, 36, "÷ 10", 7), N(131, 36, "÷ 10", 7), N(187, 36, "÷ 10", 7),
            N(120, 104, "each +10 dB = MSE ÷ 10", 7.5), N(120, 118, "< 25 dB degraded · 30–40 dB typical lossy · > 40 dB transparent", 7),
            N(120, 132, "MAX = 255 for 8-bit, 1.0 for floats in [0, 1]", 7)]
    return svg(c, *out)

def d3123(c):
    b = 56
    return svg(c,
        N(40, 12, "patch x (original)", 7), frame(14, 16, 52, 30), person(40, 44, 22),
        N(126, 12, "patch y (compressed)", 7), frame(100, 16, 52, 30), person(126, 44, 22),
        N(60, 66, "l: means μₓ, μᵧ (brightness)", 7, "start") if False else "",
        N(14, 66, "l  means μₓ μᵧ  (brightness)", 7, "start"), N(14, 78, "c  spreads σₓ σᵧ  (contrast)", 7, "start"), N(14, 90, "s  correlation σₓᵧ  (structure)", 7, "start"),
        R(168, 18, 62, 36, "#f1f5f9", 1), N(199, 30, "SSIM = 1", 7.5), N(199, 43, "only if identical", 7),
        N(120, 108, "(2μₓμᵧ + C₁)(2σₓᵧ + C₂)", 8), L(70, 112, 170, 112, .8), N(120, 124, "(μₓ² + μᵧ² + C₁)(σₓ² + σᵧ² + C₂)", 8),
        N(120, 138, "C₁ = (0.01L)² , C₂ = (0.03L)² : only keep the ratio defined", 6.5))

def d3124(c):
    out = [N(40, 12, "compressed frame", 7), frame(10, 16, 60, 44), building(14, 22, 22, 32, 2, 1, "#f1f5f9"), R(40, 30, 14, 14, "none", 1, 0, "2 2"), N(47, 70, "window", 6.5),
           arrow(74, 38, 94, 38, 1), N(150, 12, "SSIM map", 7)]
    shade = [["#ffffff"] * 6, ["#ffffff", "#ffffff", "#e8ebf0", "#ffffff", "#ffffff", "#ffffff"], ["#ffffff", "#e8ebf0", "#8b95a5", "#b8c0cc", "#ffffff", "#ffffff"], ["#ffffff", "#ffffff", "#d9dee7", "#ffffff", "#ffffff", "#ffffff"]]
    for r in range(4):
        for q in range(6): out.append(R(100 + q * 14, 16 + r * 12, 14, 12, shade[r][q], .5))
    out += [N(142, 70, "dark = damage is visible there", 6.5), N(120, 92, "MSSIM = (1/W) Σⱼ SSIM(xⱼ, yⱼ)", 8),
            N(120, 106, "11×11 Gaussian window, σ = 1.5", 7.5), N(120, 120, "MS-SSIM: repeat at several downsampled scales", 7.5), N(120, 134, "the map shows where, the mean hides it", 7.5)]
    return svg(c, *out)

def d3125(c):
    def row(y, lab, a, b, sub):
        return (N(8, y + 14, lab, 8, "start") + (R(30, y, 56, 22, "#ffffff", 1) + N(58, y + 14, a, 7) if a else "") + (N(95, y + 14, "↔", 9) if a else "")
                + R(104, y, 56, 22, "#f1f5f9", 1) + N(132, y + 14, b, 7) + N(168, y + 14, sub, 6.5, "start"))
    return svg(c,
        row(14, "FR", "original", "test frame", "MSE, PSNR, SSIM"), row(44, "RR", "few numbers", "test frame", "a few features"),
        row(74, "NR", "", "test frame", "learned statistics"),
        N(120, 112, "ground truth: MOS = mean opinion score of viewers", 7.5), N(120, 126, "SROCC = 1 − 6 Σdᵢ² / (n(n² − 1)),  dᵢ = rank gap vs MOS", 7.5),
        N(120, 140, "check the distortion types of the dataset", 7))

def d3126(c):
    b = 100
    out = [axes(24, b, 220, 14), N(222, b + 10, "log MSE", 7, "end"), N(18, 14, "PSNR dB", 7, "end")]
    pts = [(48, 1000, 18.1), (96, 100, 28.1), (144, 10, 38.1), (192, 1, 48.1)]
    ys = [b - (db - 10) * 2 for _, _, db in pts]
    out.append(poly([(p[0], y) for p, y in zip(pts, ys)], 1))
    for (x, m, db), y in zip(pts, ys):
        out += [C(f(x), f(y), 2, "#ffffff"), N(x, b + 10, str(m), 7), N(x, y - 6, f"{db}", 7)]
    out += [N(120, 124, "PSNR = 10 log₁₀(255² / 100) = 10 log₁₀(650.25) ≈ 28.13 dB", 7.5), N(120, 138, "RMS error ÷ √10 buys exactly 10 dB", 7.5)]
    return svg(c, *out)

CARDS = {
3121: dict(d=d3121, stmtKind="DEFINITION",
  statement=r"<b>Mean squared error.</b> For an original image $f$ and a distorted or restored image $\hat f$, both $M\times N$, $\mathrm{MSE}=\frac1{MN}\sum_{x,y}\big[f(x,y)-\hat f(x,y)\big]^2$. It weights every pixel error equally, regardless of position or local structure, so very different distortions (a shift, a blur, noise, a brightness change) can have the same MSE while looking very different to a viewer.",
  hint="Can a shifted, a blurred and a noisy copy of the street frame all score the same error, and look nothing alike?",
  breakdown=[r"<strong>$f-\hat f$ = the error at one pixel.</strong> The recorded value minus the original value, pixel by pixel.",
             r"<strong>$[\cdot]^2$ = big errors count more.</strong> Squaring removes the sign and punishes large errors, and is easy to optimise.",
             r"<strong>$\frac1{MN}\sum$ = average over the frame.</strong> Every pixel counts the same, so MSE cannot tell where the damage is or whether it breaks an edge."],
  conn=r"<strong>Four versions of the same frame.</strong> A slight shift of the person, a blur of the person, speckle over the street and a global brightness change can all have the same MSE. Only some of them make the plate unreadable.",
  cap="The original street frame and a shifted, a blurred and a noisy copy can share one MSE while looking very different, because MSE treats every pixel error alike."),
3122: dict(d=d3122, stmtKind="DEFINITION",
  statement=r"<b>Peak signal-to-noise ratio.</b> $\mathrm{PSNR}=10\log_{10}\dfrac{\mathrm{MAX}^2}{\mathrm{MSE}}=20\log_{10}\dfrac{\mathrm{MAX}}{\sqrt{\mathrm{MSE}}}$ dB, where MAX is the maximum possible pixel value ($255$ for 8-bit images, $1$ for floating point images in $[0,1]$). A rise of 10 dB corresponds to MSE divided by 10.",
  hint="How much does the PSNR of the recorded frame go up each time the error is cut tenfold?",
  breakdown=[r"<strong>$\mathrm{MAX}^2/\mathrm{MSE}$ = signal power over error power.</strong> The largest possible pixel value squared against the average squared error.",
             r"<strong>$10\log_{10}$ = decibels.</strong> A log scale, so every factor of 10 in MSE moves the score by exactly 10 dB; better quality means a larger number.",
             r"<strong>$\mathrm{MAX}$ = the dynamic range of the data.</strong> $255$ for 8-bit; using 255 on data scaled to $[0,1]$ gives nonsense."],
  conn=r"<strong>Comparing recorder settings.</strong> The same camera and codec at higher bit-rates gives a higher PSNR on the same frame: it is a handy ruler for that comparison, though no more informative than the MSE under it.",
  cap="PSNR = 10 log₁₀(MAX²/MSE). Each tenfold drop in MSE (1000 → 100 → 10 → 1) adds 10 dB: 18.1, 28.1, 38.1, 48.1."),
3123: dict(d=d3123, stmtKind="DEFINITION",
  statement=r"<b>Structural similarity index.</b> For two image patches $x,y$ with local means $\mu_x,\mu_y$, variances $\sigma_x^2,\sigma_y^2$ and covariance $\sigma_{xy}$: $\mathrm{SSIM}(x,y)=\dfrac{(2\mu_x\mu_y+C_1)(2\sigma_{xy}+C_2)}{(\mu_x^2+\mu_y^2+C_1)(\sigma_x^2+\sigma_y^2+C_2)}$, with $C_1=(0.01L)^2$, $C_2=(0.03L)^2$ for dynamic range $L$. It is the product of luminance, contrast and structure comparisons, lies in $[-1,1]$ and equals 1 only if $x=y$.",
  hint="Which three things should two patches share for the compressed street patch to look like the original?",
  breakdown=[r"<strong>$2\mu_x\mu_y/(\mu_x^2+\mu_y^2)$ = same brightness.</strong> Compares the average level of the two patches; it is 1 when the means match.",
             r"<strong>$2\sigma_x\sigma_y/(\sigma_x^2+\sigma_y^2)$ = same contrast.</strong> Compares how much each patch varies around its own mean.",
             r"<strong>$\sigma_{xy}$ = same structure.</strong> The correlation of the two patches: do they rise and fall together? $C_1,C_2$ are tiny constants that stop a division by zero."],
  conn=r"<strong>Is the compressed patch still the same patch?</strong> Look at a small window of the original and of the compressed frame: same overall brightness, same amount of texture, and the edges in the same places. SSIM scores all three.",
  cap="Two patches, the original x and the compressed y, are compared on brightness (means μ), contrast (spreads σ) and structure (correlation σₓᵧ). SSIM = 1 only if they are identical."),
3124: dict(d=d3124, stmtKind="ALGORITHM",
  statement=r"<b>SSIM map and mean SSIM.</b> Slide a window (typically an $11\times11$ Gaussian with $\sigma=1.5$) over the two images and compute $\mathrm{SSIM}(x_j,y_j)$ at each of $W$ positions to form a quality map. The mean SSIM is $\mathrm{MSSIM}(X,Y)=\frac1W\sum_{j=1}^{W}\mathrm{SSIM}(x_j,y_j)$. Multi-scale SSIM (MS-SSIM) repeats the comparison over several downsampled scales.",
  hint="Which would you read first to find where the compression hurt, the map or the mean?",
  breakdown=[r"<strong>$\mathrm{SSIM}(x_j,y_j)$ = the score in one window.</strong> A local comparison, so a damaged patch shows up where it is.",
             r"<strong>$\frac1W\sum_j$ = the mean of the map.</strong> One number per frame pair, in $[-1,1]$, handy for ranking.",
             r"<strong>MS-SSIM = several viewing distances.</strong> The comparison is repeated after downsampling, mimicking looking from farther away."],
  conn=r"<strong>Spotting the damaged plate.</strong> The mean SSIM of the compressed frame may be 0.97, but the map has a dark patch exactly over the number plate: the mean hides what the map shows.",
  cap="A window slides over the compressed frame and each position gets a score; the SSIM map is dark where the damage is visible. MSSIM is the average of the map."),
3125: dict(d=d3125, stmtKind="DEFINITION",
  statement=r"<b>Classes of image quality assessment (IQA).</b> Full-reference (FR) methods compare a test image with its pristine original (MSE, PSNR, SSIM, MS-SSIM); reduced-reference (RR) methods use only some features of the original; no-reference (NR, blind) methods use the test image alone, with natural-scene statistics or learned features. They are validated against subjective scores (mean opinion score, MOS) by rank correlation $\mathrm{SROCC}=1-\frac{6\sum d_i^2}{n(n^2-1)}$ and linear correlation (PLCC).",
  hint="What can you still say about a recorded frame when the original is not available?",
  breakdown=[r"<strong>FR and RR = compare with the original.</strong> Full-reference sees the whole pristine frame; reduced-reference sees a few of its numbers, cheap enough to send along.",
             r"<strong>NR = judge from the test frame alone.</strong> Natural frames follow regular statistics; deviations from them (blur, blockiness) signal damage.",
             r"<strong>MOS and SROCC = who is right.</strong> The score people give is the truth; a metric is good if its ranking of frames agrees with the people's ranking."],
  conn=r"<strong>Checking footage with no master copy.</strong> The street camera has no original to compare to, so only a no-reference score can warn that the lens has fogged or the stream is blocky.",
  cap="FR compares the test frame with the original, RR with a few features of it, NR with nothing. All are checked against MOS using SROCC."),
3126: dict(d=d3126, stmtKind="WORKED EXAMPLE",
  statement=r"<b>Example.</b> For an 8-bit image, $\mathrm{MAX}=255$. With $\mathrm{MSE}=100$ (an RMS error of $10$ grey levels), $\mathrm{PSNR}=10\log_{10}\dfrac{255^2}{100}=10\log_{10}(650.25)\approx28.13$ dB. Likewise $\mathrm{MSE}=10\Rightarrow38.1$ dB, $\mathrm{MSE}=1\Rightarrow48.1$ dB, $\mathrm{MSE}=1000\Rightarrow18.1$ dB.",
  hint="If the compressed frame is off by 10 grey levels on average (RMS), what is its PSNR?",
  breakdown=[r"<strong>$255^2/100=650.25$ = signal over error.</strong> The peak squared against an MSE of 100."],
  conn=r"<strong>A frame off by ten grey levels.</strong> Ten levels out of 255 is hard to see on the street; 28 dB is a typical lossy-compression quality. Dividing the error by $\sqrt{10}$ gives 38 dB.",
  cap="PSNR against log MSE: 1000 → 18.1 dB, 100 → 28.1 dB, 10 → 38.1 dB, 1 → 48.1 dB. Each factor of 10 in MSE is 10 dB."),
}
CARDS[3126]["breakdown"] += [r"<strong>$10\log_{10}(650.25)\approx10\times2.813=28.13$ dB.</strong> The log of 650 is about 2.8, and the 10 turns it into decibels.",
                             r"<strong>Use $10\log_{10}$ with $\mathrm{MAX}^2$, or $20\log_{10}$ with $\mathrm{MAX}$.</strong> Mixing the two forms gives an answer a factor of two out in dB."]

STORY = {
 3121: dict(s="STORY 5 · STEP 13 · HOW GOOD IS THE FRAME", b="After cleaning or compressing, we need a score. <b>MSE</b> is simple but blind to structure.",
   f=[["3082", "compression"], ["3106", "restoration"], ["3116", "denoising"]], n=[["3122", "a log scale"], ["3123", "a perceptual score"]]),
 3122: dict(s="STORY 5 · STEP 14 · A RULER IN dB", b="<b>PSNR</b> puts the error on a log scale: $+10$ dB means $\\mathrm{MSE}\\div10$.",
   f=[["3121", "MSE"]], n=[["3126", "numbers"]]),
 3123: dict(s="STORY 5 · STEP 15 · LOOK LIKE A PERSON", b="<b>SSIM</b> compares brightness, contrast and structure in each patch.",
   f=[["3121", "MSE's blind spot"], ["3054", "local means and variances"]], n=[["3124", "a map of where"]]),
 3124: dict(s="STORY 5 · STEP 16 · WHERE IS THE DAMAGE", b="The <b>SSIM map</b> shows where distortion is visible; its mean ranks frames.",
   f=[["3123", "SSIM"]], n=[["3125", "when there is no original"]]),
 3125: dict(s="STORY 5 · STEP 17 · NO ORIGINAL", b="<b>FR, RR, NR</b> metrics, all validated against human scores.",
   f=[["3124", "FR metrics"]], n=[["3126", "numbers"]]),
 3126: dict(s="STORY 5 · STEP 18 · CHECK BY HAND", b="MSE $100$ at 8-bit is $28.13$ dB.",
   f=[["3122", "PSNR"]], n=[["3131", "next: find the edges in the frame"]]),
}
FIX = build_fix(CARDS)
