"""DIP topic 12 (median, bilateral, non-local means). Everyday picture: a street camera on a pole."""
from street_lib import *

SUBJECT = "DIP"

def d3111(c):
    spikes = {8: 24, 20: -18, 29: 24}
    sig = [(14 + i * 6, 50 - spikes.get(i, 0)) for i in range(37)]
    mean = [(14 + i * 6, 96 - sum(v / 3 for k, v in spikes.items() if abs(k - i) <= 1)) for i in range(37)]
    return svg(c,
        N(12, 12, "one row of the night frame, with salt and pepper", 7, "start"), poly(sig, 1),
        N(12, 70, "mean: each spike smeared over its neighbours", 7, "start"), poly(mean, 1),
        N(12, 112, "median: a spike is never the middle value", 7, "start"), L(14, 126, 230, 126, 1),
        N(120, 140, "x̂(x, y) = median of the window", 7.5))

def d3112(c):
    st = lambda lo, hi, x, x0: lo if x < x0 else hi
    return svg(c,
        N(14, 12, "edge of the kerb", 7, "start"),
        poly([(14, 66), (110, 66), (110, 30), (230, 30)], 1, None), N(14, 76, "f", 7, "start"),
        N(14, 94, "mean over the window", 7, "start"),
        curve(lambda x: 126 - 8 - 36 / (1 + math.exp(-(x - 122) / 9)), 14, 230, 60, 1, "3 2"),
        N(14, 108, "", 6), N(120, 138, "median(2,2,8) = 2 , median(2,8,8) = 8 ; mean(2,2,8) = 4", 7.5),
        N(228, 94, "", 6))

def d3113(c):
    out = [N(120, 10, "window grows until the median is not an impulse", 7.5)]
    for i, (s, x) in enumerate(((14, 14), (28, 40), (42, 78))):
        out.append(R(x, 56 - s // 2, s, s, "#ffffff", .8)); out.append(N(x + s / 2, 56 + s / 2 + 10, f"{3 + 2 * i}×{3 + 2 * i}", 6.5))
    out += [R(130, 22, 100, 34, "#f1f5f9", 1), N(180, 34, "Level A: z_min < z_med < z_max ?".replace("z_min", "zmin").replace("z_med", "zmed").replace("z_max", "zmax"), 6.5), N(180, 47, "no ⇒ bigger window", 6.5),
            R(130, 64, 100, 34, "#f1f5f9", 1), N(180, 76, "Level B: zmin < zxy < zmax ?", 6.5), N(180, 89, "yes ⇒ keep zxy, no ⇒ zmed", 6.5),
            arrow(180, 56, 180, 64, 1),
            N(120, 114, "light noise: small window, detail kept", 7.5), N(120, 126, "dense noise: window grows up to Smax", 7.5), N(120, 138, "at Smax output zmed (stops the loop)", 7.5)]
    return svg(c, *out)

def d3114(c):
    return svg(c,
        N(14, 12, "pixel p on the near side of an edge", 7, "start"),
        poly([(14, 60), (100, 60), (100, 28), (226, 28)], 1), C(64, 60, 2.2), N(64, 72, "p", 7),
        bell(14, 114, 64, 24, 20, 96, 1, "3 2"), N(30, 86, "Gσₛ(‖p−q‖)", 6.5, "start"),
        bell(14, 114, 64, 14, 20, 120, 1), N(30, 106, "Gσᵣ(|Iₚ−I_q|)".replace("I_q", "Iq"), 6.5, "start"),
        L(100, 14, 100, 60, .5, "2 2"), N(106, 48, "far side: range weight ≈ 0", 6.5, "start"),
        N(176, 90, "weight = spatial × range", 7.5), N(176, 104, "÷ Wₚ (so they add to 1)", 7.5),
        N(120, 138, "flat areas smoothed, the edge stays sharp", 7.5))

def d3115(c):
    out = [N(14, 12, "street frame", 7, "start"), R(14, 18, 130, 80, "#ffffff", 1)]
    for i in range(6):
        for j in range(4): out.append(R(24 + i * 20, 24 + j * 18, 10, 8, "#d9dee7", .5))
    out += [R(24, 24, 20, 18, "none", 1), N(34, 54, "Pₚ", 7), R(84, 60, 20, 18, "none", 1, 0, "3 2"), N(94, 90, "P_q1".replace("_q1", "q"), 7), R(44, 78, 20, 14, "none", 1, 0, "1 2")]
    out += [N(190, 24, "weight", 7.5), N(190, 38, "exp(−‖Pₚ − P_q‖² / h²)".replace("P_q", "Pq"), 7), L(172, 44, 222, 44, .5),
            N(190, 58, "similar patch ⇒ weight ≈ 1", 7), N(190, 70, "different patch ⇒ ≈ 0", 7),
            N(190, 88, "Î(p) = Σ w I(q) / Σ w", 7),
            N(120, 118, "average the pixels whose surroundings look alike,", 7.5), N(120, 130, "wherever they are in the frame", 7.5),
            N(120, 142, "compare patches, not single pixels", 7)]
    return svg(c, *out)

def d3116(c):
    return svg(c,
        pix(14, 14, [[10, 12, 200], [11, 13, 9], [12, 10, 11]], 24, 9, {(0, 2)}), N(50, 98, "3×3 window, 200 = salt", 6.5),
        N(168, 24, "mean = 288/9 = 32", 8), N(168, 38, "(pulled up by 21)", 7),
        N(168, 60, "sorted: 9 10 10 11", 7.5), N(168, 72, "11 12 12 13 200", 7.5), N(168, 86, "5th value = 11", 8),
        N(120, 120, "median ≈ the clean neighbourhood (~11)", 8), N(120, 134, "use odd windows: an even one has no single middle", 7.5))

CARDS = {
3111: dict(d=d3111, stmtKind="DEFINITION",
  statement=r"<b>Median filter.</b> The median filter replaces each pixel by the median of the grey levels in its neighbourhood $S_{xy}$: $\hat f(x,y)=\operatorname{median}\{f(s,t)\mid(s,t)\in S_{xy}\}$. It is non-linear. It removes impulse (salt-and-pepper) noise: an isolated extreme value is never the median, and a $K\times K$ median removes impulse groups of fewer than $K^2/2$ pixels.",
  hint="Why does averaging smear a stuck white pixel into its neighbours, while taking the middle value removes it?",
  breakdown=[r"<strong>$S_{xy}$ = the little window around the pixel.</strong> The same neighbourhood a smoothing filter would use.",
             r"<strong>$\operatorname{median}\{\cdot\}$ = sort the window and take the middle.</strong> An outlier lands at one end of the sorted list and is never picked, so it is thrown away, not averaged in.",
             r"<strong>Fewer than $K^2/2$ bad pixels = removed.</strong> If most of the window is clean, the middle is clean; a larger cluster of impulses starts to take over the middle."],
  conn=r"<strong>Dead pixels on the night frame.</strong> A hot pixel on the sensor appears as a white dot on the dark road. An average spreads it into a grey blotch; the median simply replaces it with its neighbours' typical value.",
  cap="A row of the night frame with salt (up) and pepper (down) spikes. The mean spreads each spike into its neighbours; the median never picks a spike as the middle value."),
3112: dict(d=d3112, stmtKind="PROPOSITION",
  statement=r"<b>Edge preservation of the median filter.</b> For a step edge, any window centred near the edge contains a majority of pixels from one side, so the median equals that side's value and the step is preserved exactly, whereas the mean creates intermediate values: e.g. $\operatorname{median}(2,2,8)=2$, $\operatorname{median}(2,8,8)=8$, $\operatorname{mean}(2,2,8)=4$. A signal unchanged by the median filter is a root signal; repeated filtering converges to a root in finitely many steps. Thin lines and sharp corners narrower than half the window are removed.",
  hint="Why does the kerb stay sharp after a median but go soft after a mean?",
  breakdown=[r"<strong>$\operatorname{median}(2,2,8)=2$ = most of the window is on the dark side.</strong> The odd one out is ignored, so the pixel keeps its side's value.",
             r"<strong>$\operatorname{mean}(2,2,8)=4$ = a value that was never there.</strong> The mean mixes both sides, so a sharp step turns into a ramp.",
             r"<strong>Root signals and thin lines.</strong> After a few passes the signal stops changing. But a line thinner than half the window is outvoted, just like an impulse."],
  conn=r"<strong>The kerb in the night footage.</strong> Median-filtering the frame keeps the kerb's edge exactly where it was while calming the speckle; averaging would give it a soft grey border. A single thin wire, however, would be removed too.",
  cap="A step edge f. The mean (dashed) turns it into a ramp with new in-between values; the median keeps the step exactly: median(2,2,8) = 2, median(2,8,8) = 8."),
3113: dict(d=d3113, stmtKind="ALGORITHM",
  statement=r"<b>Adaptive median filter.</b> At each pixel with window $S_{xy}$ (initially $3\times3$, up to $S_{\max}$) let $z_{\min},z_{\max},z_{\rm med}$ be the minimum, maximum and median in the window and $z_{xy}$ the pixel. Level A: if $z_{\min}\lt z_{\rm med}\lt z_{\max}$ go to Level B; otherwise enlarge the window, and if $S_{xy}\le S_{\max}$ repeat A, else output $z_{\rm med}$. Level B: if $z_{\min}\lt z_{xy}\lt z_{\max}$ output $z_{xy}$, otherwise output $z_{\rm med}$.",
  hint="How can the filter leave good pixels alone and only fix the impulses, however dense the noise?",
  breakdown=[r"<strong>$z_{\min}\lt z_{\rm med}\lt z_{\max}$ = the median is not itself an impulse.</strong> If it equals the window's min or max, the window is too noisy to trust, so the window grows and tries again.",
             r"<strong>$z_{\min}\lt z_{xy}\lt z_{\max}$ = the pixel itself is not an impulse.</strong> If so, keep it untouched, which preserves detail.",
             r"<strong>Otherwise output $z_{\rm med}$, and stop at $S_{\max}$.</strong> Only impulses are replaced; at the largest window the loop must end by outputting the median."],
  conn=r"<strong>Light and heavy speckle in one frame.</strong> Over the bright shopfront there are only a few white dots; over the dark far street there are many. The window stays small where it can and grows only where the dots crowd.",
  cap="Windows of 3×3, 5×5 and 7×7 are tried in turn. Level A asks whether the median is itself an impulse; Level B asks whether the pixel is. Detail pixels are kept."),
3114: dict(d=d3114, stmtKind="DEFINITION",
  statement=r"<b>Bilateral filter.</b> For an image $I$ and pixel $p$: $BF[I]_p=\frac1{W_p}\sum_{q\in S}G_{\sigma_s}(\|p-q\|)\,G_{\sigma_r}(|I_p-I_q|)\,I_q$, where $G_\sigma$ is a Gaussian and $W_p=\sum_{q}G_{\sigma_s}(\|p-q\|)G_{\sigma_r}(|I_p-I_q|)$ normalizes the weights. A neighbour counts only if it is near (spatial term) and similar in value (range term). It is non-linear and not separable.",
  hint="How can a blur skip the pixels on the other side of an edge?",
  breakdown=[r"<strong>$G_{\sigma_s}(\|p-q\|)$ = near pixels count more.</strong> The ordinary Gaussian blur weight; $\sigma_s$ sets how far to look.",
             r"<strong>$G_{\sigma_r}(|I_p-I_q|)$ = similar pixels count more.</strong> A pixel across the edge has a very different value, so its weight is nearly zero and the edge is not mixed in; $\sigma_r$ sets what is similar.",
             r"<strong>$1/W_p$ = make the weights add up to 1.</strong> The result is an average that smooths flat areas but not across edges. A very large $\sigma_r$ makes the range term 1 and gives back a plain Gaussian blur."],
  conn=r"<strong>Smoothing the road but not the kerb.</strong> Pixels of the road average with the road; the kerb's grey is far away in value, so it is hardly counted. The speckle goes, the edge stays.",
  cap="A pixel p on the dark side of an edge. The spatial weight Gσₛ falls with distance; the range weight Gσᵣ falls with difference in value, so pixels beyond the edge get almost no weight."),
3115: dict(d=d3115, stmtKind="DEFINITION",
  statement=r"<b>Non-local means.</b> $\hat I(p)=\frac1{Z_p}\sum_{q}w(p,q)\,I(q)$ with $w(p,q)=\exp\!\Big(-\frac{\|P_p-P_q\|_2^2}{h^2}\Big)$ and $Z_p=\sum_qw(p,q)$, where $P_p$ is the patch of pixels centred at $p$ (e.g. $7\times7$) and $h$ is the filtering strength. The sum runs over pixels $q$ anywhere in the image (or a large search window), not just near $p$.",
  hint="Why average pixels from far away in the frame if their surroundings look alike?",
  breakdown=[r"<strong>$\|P_p-P_q\|^2$ = how different the two surroundings are.</strong> Compare small patches pixel by pixel; a patch that looks the same gives a small number.",
             r"<strong>$\exp(-\cdot/h^2)$ = the weight.</strong> Close to 1 for matching patches, close to 0 for different ones; $h$ sets how strict to be.",
             r"<strong>$1/Z_p\sum w\,I(q)$ = a weighted average over the whole frame.</strong> Repeating structure (bricks, windows, lane dashes) is averaged together, so noise cancels and structure stays."],
  conn=r"<strong>The shop's brick wall.</strong> Every brick looks like the others, so a noisy brick can be cleaned by averaging with all the other bricks in the frame, wherever they are. A lone person gets no help from the bricks.",
  cap="The patch Pₚ around p is compared with patches elsewhere: the lookalike Pq gets weight ≈ 1, a different patch ≈ 0. Î(p) averages the centre pixels of the matching patches."),
3116: dict(d=d3116, stmtKind="WORKED EXAMPLE",
  statement=r"<b>Example.</b> A $3\times3$ window holds $10,12,200,11,13,9,12,10,11$ (the 200 is a salt pixel). The mean is $288/9=32$; sorted, the values are $9,10,10,11,11,12,12,13,200$ and the median (5th of 9) is $11$.",
  hint="With one salt pixel in nine, which is closer to the clean neighbourhood, the mean or the median?",
  breakdown=[r"<strong>Mean $=288/9=32$.</strong> The single 200 drags the output about 20 grey levels above the true neighbourhood level of about 11."],
  conn=r"<strong>One hot pixel in a 3×3 patch of road.</strong> The road is about 11; one pixel reads 200. The mean reports 32, a grey smudge; the median reports 11, the road.",
  cap="A 3×3 window with one salt pixel (200). The mean is 32; sorting the nine values puts the median at 11, the clean level."),
}
CARDS[3116]["breakdown"] += [r"<strong>Sorted: $9,10,10,11,\mathbf{11},12,12,13,200$.</strong> The 200 goes to the far end of the list and is never the middle.",
                             r"<strong>5th value $=11$ = the clean level.</strong> Use an odd window; with an even size the 'middle' is the average of two values and is ambiguous."]

STORY = {
 3111: dict(s="STORY 5 · STEP 7 · SPECKLE", b="Isolated bright and dark pixels are not helped by blurring. The <b>median</b> never picks an outlier.",
   f=[["3054", "averaging smears it"], ["3106", "linear restoration"]], n=[["3112", "what it does to edges"], ["3113", "any noise density"]]),
 3112: dict(s="STORY 5 · STEP 8 · EDGES", b="The median keeps a step edge <b>exactly sharp</b>, but removes lines thinner than half the window.",
   f=[["3111", "median"]], n=[["3113", "adapt the window"], ["3114", "weights instead of ranks"]]),
 3113: dict(s="STORY 5 · STEP 9 · ADAPT THE WINDOW", b="Grow the window only where the noise needs it, and <b>leave good pixels alone</b>.",
   f=[["3112", "median"]], n=[["3114", "smooth with edge awareness"]]),
 3114: dict(s="STORY 5 · STEP 10 · SMOOTH, KEEP EDGES", b="The <b>bilateral filter</b> multiplies a spatial weight by a range weight so edges are not blurred.",
   f=[["3054", "the Gaussian"], ["3112", "edge preservation"]], n=[["3115", "look farther away"]]),
 3115: dict(s="STORY 5 · STEP 11 · LOOK ALIKE", b="<b>Non-local means</b> averages pixels whose <b>patches</b> look alike, anywhere in the frame.",
   f=[["3114", "similar-value weights"]], n=[["3116", "numbers"], ["3121", "how to score the result"]]),
 3116: dict(s="STORY 5 · STEP 12 · CHECK BY HAND", b="One salt pixel: mean $32$, median $11$.",
   f=[["3111", "median"]], n=[["3121", "next: how good is the cleaned frame"]]),
}
FIX = build_fix(CARDS)
