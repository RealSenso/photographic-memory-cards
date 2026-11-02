"""DIP topic 17 (SIFT). Everyday picture: a street camera on a pole (matching the shop front seen from another pole)."""
from street_lib import *

SUBJECT = "DIP"

def d3161(c):
    out = [N(14, 10, "blurred copies L(σ), L(kσ), …", 7, "start")]
    for i, lab in enumerate(("σ", "kσ", "k²σ")):
        x = 12 + i * 26
        out += [R(x, 18 + i * 8, 44, 32, "#ffffff", 1), N(x + 22, 38 + i * 8, lab, 8)]
    out += [arrow(102, 44, 118, 44, 1), N(110, 38, "−", 8),
            R(124, 18, 40, 28, "#f1f5f9", 1), N(144, 36, "D(σ)", 7.5), R(124, 52, 40, 28, "#f1f5f9", 1), N(144, 70, "D(kσ)", 7.5),
            arrow(168, 50, 186, 50, 1), N(180, 42, "↓2", 7), R(190, 34, 22, 18, "#ffffff", 1), N(201, 46, "½", 7), N(201, 64, "next octave", 6.5),
            N(120, 100, "L(x,y,σ) = Gσ ∗ I ,  D = L(kσ) − L(σ)", 8), N(120, 114, "k = 2^(1/s): σ doubles every s layers (one octave)", 7.5),
            N(120, 128, "s + 3 blurred images per octave ⇒ s + 2 DoG layers", 7.5), N(120, 140, "downsample by 2 and repeat: cheap", 7)]
    return svg(c, *out)

def d3162(c):
    out = [N(120, 10, "is the centre larger than all 26 neighbours?", 7.5)]
    for i, lab in enumerate(("layer above (9)", "same layer (8)", "layer below (9)")):
        x = 14 + i * 76
        for r in range(3):
            for q in range(3):
                ctr = (i == 1 and r == 1 and q == 1)
                out.append(R(x + q * 18, 20 + r * 18, 18, 18, "#7b8494" if ctr else "#ffffff", .8))
        out.append(N(x + 27, 84, lab, 6.5))
    out += [N(120, 100, "x̂ = −H⁻¹ ∇D  (sub-pixel, sub-scale)", 8), N(120, 113, "drop if |D(x̂)| < 0.03 (low contrast)", 7.5),
            N(120, 126, "edge test: tr(H)² / det(H) < (r+1)²/r = 12.1, r = 10", 7.5), N(120, 139, "a ratio of curvatures: no units, no scale", 7)]
    return svg(c, *out)

def d3163(c):
    vals = [6, 9, 12, 16, 24, 40, 62, 44, 26, 18, 12, 9, 8, 7, 8, 12, 20, 36, 49, 30, 18, 11, 8, 6, 5, 4, 4, 5, 6, 6, 6, 5, 5, 5, 5, 6]
    out = [axes(14, 70, 232, 10), N(232, 80, "angle θ (36 bins)", 7, "end"), N(10, 12, "Σ m·G", 7, "end")]
    for i, v in enumerate(vals): out.append(R(f(16 + i * 6), f(70 - v * .6), 5, f(v * .6), "#d9dee7" if i not in (6, 18) else "#8b95a5", .5))
    out += [L(14, 70 - 62 * .6 * .8, 232, 70 - 62 * .6 * .8, .6, "3 2"), N(14, 70 - 62 * .6 * .8 - 3, "80% line", 6.5, "start"),
            N(60, 24, "peak 1: the orientation", 7, "start"), N(140, 34, "peak 2 ≥ 80%: extra keypoint", 6.5, "start"),
            N(120, 100, "m = √(Lₓ² + Lᵧ²) ,  θ = atan2(Lᵧ, Lₓ)", 8), N(120, 114, "h[b] = Σ m · Gσ · 1[θ in bin b]", 7.5),
            N(120, 128, "measure everything relative to it: rotation invariant", 7.5), N(120, 140, "keep tied peaks: they help matching", 7)]
    return svg(c, *out)

def d3164(c):
    out = [N(60, 10, "16×16 window, rotated to θ", 7)]
    for r in range(4):
        for q in range(4): out.append(R(20 + q * 24, 16 + r * 24, 24, 24, "#ffffff", .8))
    cx, cy = 20 + 24 * 2.5, 16 + 24 * 1.5
    for k in range(8):
        a = math.radians(k * 45); l = 6 + (k % 3) * 2
        out.append(arrow(cx, cy, cx + l * math.cos(a), cy - l * math.sin(a), .7))
    out += [R(130, 24, 100, 40, "#f1f5f9", 1), N(180, 38, "4 × 4 cells × 8 bins", 7.5), N(180, 54, "= 128 numbers", 8),
            N(180, 82, "d ← d/‖d‖  (cancels contrast)", 6.5), N(180, 93, "dᵢ ← min(dᵢ, 0.2)  (tames glare)", 6.5), N(180, 104, "renormalise", 6.5),
            N(120, 124, "each cell: how the edges point inside it", 7.5), N(120, 138, "trilinear interpolation avoids boundary jumps", 7)]
    return svg(c, *out)

def d3165(c):
    return svg(c,
        N(60, 10, "descriptor space", 7), R(12, 16, 110, 82, "#ffffff", 1),
        C(40, 58, 2.6), N(40, 72, "q", 8), C(66, 44, 2.2, "#ffffff"), N(70, 40, "NN₁", 7, "start"), C(94, 78, 2.2, "#ffffff"), N(98, 84, "NN₂", 7, "start"),
        L(40, 58, 66, 44, .8), N(48, 46, "d₁", 7), L(40, 58, 94, 78, .8, "3 2"), N(70, 74, "d₂", 7),
        R(136, 20, 94, 60, "#f1f5f9", 1), N(183, 36, "accept q ↔ NN₁ ⇔", 7), N(183, 52, "d₁ / d₂ < 0.8", 8.5), N(183, 70, "repeats give d₁ ≈ d₂", 7),
        N(120, 112, "then RANSAC: keep matches that fit one transform", 7.5), N(120, 126, "0.8 drops ~90% of false matches, loses < 5% of true ones", 7),
        N(120, 140, "a trade-off, not an exact rule", 7))

def d3166(c):
    def bar(y, lab, d1, d2, ok):
        return (N(8, y + 8, lab, 7, "start") + R(60, y, d1 * 200, 10, "#d9dee7", .8) + N(60 + d1 * 200 + 4, y + 8, f"d₁ = {d1}", 6.5, "start")
                + R(60, y + 14, d2 * 200, 10, "#ffffff", .8) + N(60 + d2 * 200 + 4, y + 22, f"d₂ = {d2}", 6.5, "start"))
    return svg(c,
        bar(14, "accepted", .3, .5, True), N(120, 50, "0.3 / 0.5 = 0.6 < 0.8 ✓", 8, "middle"),
        bar(62, "rejected", .45, .5, False), N(120, 98, "0.45 / 0.5 = 0.9 > 0.8 ✗", 8, "middle"),
        N(120, 112, "(r+1)²/r = 11²/10 = 12.1 for r = 10", 7.5), N(120, 125, "128 = 4·4·8 ,  |D| < 0.03 is low contrast", 7.5), N(120, 138, "on squared distances the threshold is 0.8² = 0.64", 7))

CARDS = {
3161: dict(d=d3161, stmtKind="DEFINITION",
  statement=r"<b>Scale space and difference-of-Gaussians pyramid (SIFT).</b> The scale space of an image $I$ is $L(x,y,\sigma)=G_\sigma\ast I$. The difference-of-Gaussians function is $D(x,y,\sigma)=L(x,y,k\sigma)-L(x,y,\sigma)\approx(k-1)\sigma^2\nabla^2G\ast I$, computed with $k=2^{1/s}$ so that $\sigma$ doubles over $s$ intervals (an octave). After each octave the image is downsampled by 2. For $s$ intervals per octave, $s+3$ blurred images are produced, giving $s+2$ DoG images.",
  hint="How can the same shopfront be recognised when it appears bigger or smaller in another camera's frame?",
  breakdown=[r"<strong>$L(x,y,\sigma)=G_\sigma\ast I$ = the frame at blur level $\sigma$.</strong> A stack of copies, from sharp to very soft; a larger $\sigma$ shows only coarse structure.",
             r"<strong>$D=L(k\sigma)-L(\sigma)$ = what lives at that scale.</strong> Subtracting neighbouring blurs keeps only features about the size of $\sigma$, approximately the scale-normalised Laplacian.",
             r"<strong>$k=2^{1/s}$ and downsampling = an octave is cheap.</strong> $\sigma$ doubles every $s$ layers; then the frame is halved and the blurring starts again, so the whole pyramid costs little."],
  conn=r"<strong>Seeing the shop at every distance.</strong> From a far pole the shop sign is a few pixels wide; from the near pole it fills the frame. The blur stack looks for the sign at every size at once, so both cameras find the same feature.",
  cap="The frame is blurred to σ, kσ, k²σ and neighbouring blurs are subtracted to give D(σ), D(kσ). After an octave the frame is halved (↓2) and the process repeats."),
3162: dict(d=d3162, stmtKind="ALGORITHM",
  statement=r"<b>SIFT keypoint detection.</b> A DoG sample is a candidate keypoint if it is larger or smaller than all 26 neighbours (8 in its own layer, 9 above, 9 below). Its position is refined by a quadratic fit, $\hat x=-H^{-1}\nabla D$ (sub-pixel and sub-scale); candidates with $|D(\hat x)|\lt0.03$ are discarded as low contrast; and edge-like candidates are rejected unless $\dfrac{\operatorname{tr}(H)^2}{\det(H)}\lt\dfrac{(r+1)^2}{r}$ with $r=10$ (i.e. $\lt12.1$), where $H$ is the $2\times2$ Hessian of $D$.",
  hint="Why does SIFT throw away spots on an edge even when they are strong?",
  breakdown=[r"<strong>26 neighbours = the cube around a sample.</strong> Eight in its own layer, nine above and nine below; a keypoint is the largest (or smallest) in position and in scale."],
  conn=r"<strong>Picking the sign's best spot.</strong> The detector picks the pixel and scale at which the shop sign's blob is strongest, polishes it to a fraction of a pixel, and drops anything faint or lying along a straight edge of the building.",
  cap="The centre sample (dark) is compared with its 8 neighbours in the same DoG layer and 9 in each adjacent layer: 26 in all. Refine with x̂ = −H⁻¹∇D, then drop low-contrast and edge-like points."),
3163: dict(d=d3163, stmtKind="ALGORITHM",
  statement=r"<b>SIFT orientation assignment.</b> Around each keypoint, at its scale, compute gradient magnitudes $m=\sqrt{L_x^2+L_y^2}$ and orientations $\theta=\operatorname{atan2}(L_y,L_x)$ and accumulate a 36-bin orientation histogram $h[b]=\sum m\cdot G_\sigma\cdot\mathbf 1[\theta\in\text{bin }b]$ (Gaussian-weighted). The highest peak (refined by a parabola fit) gives the keypoint orientation, and every other peak of at least $80\%$ of it creates an additional keypoint at the same location and scale with that orientation.",
  hint="How does SIFT recognise the sign when the other camera is tilted?",
  breakdown=[r"<strong>$m,\theta$ = how strong and which way the edges point.</strong> The gradient magnitude and angle at each pixel around the keypoint.",
             r"<strong>$h[b]=\sum m\,G_\sigma\mathbf 1[\theta\in b]$ = a vote count by angle.</strong> Each pixel votes for its angle bin with its edge strength, weighted so pixels near the keypoint count more.",
             r"<strong>The tallest peak = the keypoint's own 'up'.</strong> Everything measured afterwards is relative to it; peaks above 80% make extra keypoints, which help matching."],
  conn=r"<strong>The sign seen sideways.</strong> The strokes of the sign mostly point one way; that dominant direction becomes the sign's own 'up', so the tilted view and the straight view give the same description.",
  cap="A 36-bin histogram of edge angles around the keypoint, weighted by gradient magnitude m. The highest peak sets the orientation; a second peak above 80% makes an extra keypoint."),
3164: dict(d=d3164, stmtKind="DEFINITION",
  statement=r"<b>SIFT descriptor.</b> Take a $16\times16$ window around the keypoint, rotated to the keypoint orientation, scaled to its $\sigma$ and weighted by a Gaussian. Divide it into a $4\times4$ grid of cells, each holding an 8-bin gradient orientation histogram (with trilinear interpolation), giving $\mathbf d\in\mathbb R^{4\cdot4\cdot8}=\mathbb R^{128}$. Normalize $\mathbf d\leftarrow\mathbf d/\|\mathbf d\|$ (contrast invariance), clip $d_i\leftarrow\min(d_i,0.2)$ (non-linear illumination), and renormalize.",
  hint="Why does SIFT summarise a patch as 16 small histograms instead of its raw pixels?",
  breakdown=[r"<strong>$4\times4$ cells $\times$ 8 bins $=128$ = a patch described by edge directions.</strong> Each of the 16 cells records how the edges point inside it, so small shifts do not change much."],
  conn=r"<strong>A fingerprint of the sign.</strong> The sign's patch becomes 128 numbers that describe how its strokes point; a darker or glarier view changes pixels but hardly changes these numbers.",
  cap="A rotated 16×16 window becomes a 4×4 grid of cells; each cell holds 8 orientation bins (arrows), giving 128 numbers, then normalised, clipped at 0.2 and renormalised."),
3165: dict(d=d3165, stmtKind="ALGORITHM",
  statement=r"<b>Descriptor matching with Lowe's ratio test.</b> For each descriptor $q$ in image A find its nearest neighbour $\mathrm{NN}_1$ and second nearest $\mathrm{NN}_2$ in image B (Euclidean distance). Accept the match $q\leftrightarrow\mathrm{NN}_1$ only if $\dfrac{\|q-\mathrm{NN}_1\|}{\|q-\mathrm{NN}_2\|}\lt0.8$. The remaining matches are verified geometrically, e.g. by fitting an affine transform or homography with RANSAC and keeping the inliers.",
  hint="How can SIFT tell a confident match from a lucky one, when the wall's bricks all look alike?",
  breakdown=[r"<strong>$\|q-\mathrm{NN}_1\|$ = distance to the best candidate.</strong> The closest fingerprint in the other camera's frame."],
  conn=r"<strong>Matching the shop sign across two poles.</strong> The sign's fingerprint has one clear twin in the other frame, and passes. A brick's fingerprint has dozens of near-twins, ties, and is rejected before it can give a false match.",
  cap="The query q has nearest neighbour NN₁ at distance d₁ and runner-up NN₂ at d₂. Accept only if d₁/d₂ < 0.8; repeated textures have d₁ ≈ d₂ and are dropped."),
3166: dict(d=d3166, stmtKind="WORKED EXAMPLE",
  statement=r"<b>Example.</b> Ratio test with $d_1=0.3$, $d_2=0.5$: $0.3/0.5=0.6\lt0.8$, accepted. With $d_1=0.45$, $d_2=0.5$: $0.45/0.5=0.9\ge0.8$, rejected. Numbers to remember: descriptor length $4\cdot4\cdot8=128$; edge-rejection bound $\frac{(r+1)^2}{r}=\frac{11^2}{10}=12.1$ for $r=10$; low-contrast threshold $|D(\hat x)|\lt0.03$. Lowe's ratio is stated on distances; on squared distances the equivalent threshold is $0.8^2=0.64$.",
  hint="Which of the two candidate matches is clearly better than its runner-up?",
  breakdown=[r"<strong>$0.3/0.5=0.6\lt0.8$ = accepted.</strong> The best candidate is much closer than the second best, so the match is trustworthy."],
  conn=r"<strong>Two matches from the shop front.</strong> The sign's corner has one very close twin and a distant second: accepted. A brick has two near-identical twins: rejected as ambiguous.",
  cap="Two matches: d₁ = 0.3 and d₂ = 0.5 give 0.6 and pass; d₁ = 0.45 and d₂ = 0.5 give 0.9 and fail the 0.8 test."),
}
CARDS[3162]["breakdown"] += [r"<strong>$\hat x=-H^{-1}\nabla D$ = fit a bowl through the samples.</strong> The true extremum lies between samples; this gives its position to a fraction of a pixel and of a scale step, and $|D(\hat x)|\lt0.03$ drops faint ones.",
                             r"<strong>$\operatorname{tr}(H)^2/\det(H)\lt12.1$ = reject edges.</strong> It is the ratio of the two curvatures: a high ratio means one large and one small curvature (an edge), whose position slides along the edge."]
CARDS[3164]["breakdown"] += [r"<strong>Rotated to $\theta$ and scaled to $\sigma$ = the same patch from any view.</strong> The grid is laid out along the keypoint's own orientation and size, which is what makes the 128 numbers invariant.",
                             r"<strong>Normalise, clip at 0.2, renormalise = steady under lighting.</strong> The first scaling cancels contrast, the clip tames a few huge glare gradients, and the second normalisation restores unit length."]
CARDS[3165]["breakdown"] += [r"<strong>$d_1/d_2\lt0.8$ = clearly the best.</strong> A true match has a close twin and a far runner-up; a repeated texture has $d_1\approx d_2$ and is dropped. Lowe reports it removes about 90% of false matches and loses under 5% of true ones.",
                             r"<strong>RANSAC = keep what agrees on one transform.</strong> The remaining matches may still hold outliers, so fit a homography or affine map and keep only the inliers."]
CARDS[3166]["breakdown"] += [r"<strong>$0.45/0.5=0.9\ge0.8$ = rejected.</strong> Nearly a tie between the two best candidates: ambiguous.",
                             r"<strong>$128$, $12.1$, $0.03$ = the three numbers to remember.</strong> Descriptor length, the edge-test bound for $r=10$, and the contrast threshold; the ratio is on distances, so on squared distances use $0.64$."]

STORY = {
 3161: dict(s="STORY 7 · STEP 1 · EVERY SIZE AT ONCE", b="Harris is not scale invariant, so SIFT looks for features in a <b>stack of blurs</b> and their differences (DoG).",
   f=[["3155", "scale is a problem"], ["3134", "DoG ≈ LoG"], ["3074", "downsample each octave"]], n=[["3162", "pick the keypoints"]]),
 3162: dict(s="STORY 7 · STEP 2 · PICK THE SPOTS", b="Keep the extremum among 26 neighbours, refine it, and reject faint and <b>edge-like</b> points.",
   f=[["3161", "the DoG stack"], ["3152", "edges have one large curvature"]], n=[["3163", "give each spot an orientation"]]),
 3163: dict(s="STORY 7 · STEP 3 · A SENSE OF UP", b="The dominant gradient direction becomes the keypoint's orientation: <b>rotation invariance</b>.",
   f=[["3162", "keypoints"], ["3131", "gradient direction"]], n=[["3164", "describe the patch"]]),
 3164: dict(s="STORY 7 · STEP 4 · A FINGERPRINT", b="A rotated patch becomes <b>128 numbers</b> (4×4 cells × 8 orientation bins), normalised for lighting.",
   f=[["3163", "orientation"]], n=[["3165", "match them"], ["3171", "bag of words uses these"]]),
 3165: dict(s="STORY 7 · STEP 5 · MATCH", b="Match by nearest neighbour, accept with the <b>ratio test</b>, verify with RANSAC.",
   f=[["3164", "descriptors"], ["40106", "homography from matches"]], n=[["3166", "numbers"], ["3171", "matching without geometry"]]),
 3166: dict(s="STORY 7 · STEP 6 · CHECK BY HAND", b="$0.6$ passes, $0.9$ fails; remember $128$, $12.1$, $0.03$.",
   f=[["3165", "ratio test"]], n=[["3171", "next: the whole frame as a bag of visual words"]]),
}
FIX = build_fix(CARDS)
