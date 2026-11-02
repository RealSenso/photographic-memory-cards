"""DIP topic 05 (histogram equalization). Everyday picture: a street camera on a pole."""
from street_lib import *

SUBJECT = "DIP"

def d3041(c):
    b = 92
    return svg(c,
        N(56, 14, "night frame: crowded left", 7), axes(14, b, 108, 22), hist_(18, b, [64, 54, 36, 20, 10, 6, 4, 3]), N(110, b + 10, "r", 8, "end"),
        arrow(114, 56, 134, 56, 1), N(124, 48, "T = CDF", 7),
        N(184, 14, "after: spread flat", 7), axes(140, b, 234, 22), hist_(144, b, [30, 30, 32, 30, 31, 30, 32, 30]), N(232, b + 10, "s", 8, "end"),
        N(120, 118, "s = T(r) = (L − 1) Σ p(rⱼ)", 8), N(120, 132, "every grey level is used about equally often", 7.5))

def hist_(x0, base, vals, bw=9, gap=2):
    return bars(x0, base, vals, bw, gap)

def d3042(c):
    return svg(c,
        axes(18, 112, 130, 14), N(130, 122, "r", 8, "end"), N(14, 18, "s", 8, "end"),
        curve(lambda x: 112 - 92 / (1 + math.exp(-(x - 70) / 12)), 22, 126, 50, 1),
        L(70, 112, 70, 66, .6, "2 3"), L(18, 66, 70, 66, .6, "2 3"),
        N(78, 56, "slope = (L−1)·p(r)", 7, "start"), N(70, 122, "r", 7), 
        bell(22, 126, 70, 18, 20, 112, .8, "2 2"), N(44, 98, "p(r)", 7),
        R(148, 20, 82, 74, "#f1f5f9", 1), N(189, 34, "ds/dr = (L−1)·p(r)", 7), N(189, 50, "p(s) = p(r)·|dr/ds|", 7), N(189, 66, "= 1/(L−1)", 8), N(189, 84, "flat ✓", 7.5),
        N(120, 138, "busy grey levels get a steep slope: they spread out", 7.5))

def d3043(c):
    p = [.19, .25, .21, .16, .08, .06, .03, .02]
    out = [N(14, 16, "r", 7, "start"), N(14, 30, "p(r)", 7, "start"), N(14, 44, "CDF", 7, "start"), N(14, 58, "×7", 7, "start"), N(14, 72, "round", 7, "start")]
    cum = 0
    for i, v in enumerate(p):
        cum += v; x = 56 + i * 22
        out += [N(x, 16, str(i), 7.5), N(x, 30, f"{v:.2f}", 6.5), N(x, 44, f"{cum:.2f}", 6.5), N(x, 58, f"{7 * cum:.1f}", 6.5), N(x, 72, str(round(7 * cum)), 8)]
    out += [L(10, 22, 232, 22, .5), L(10, 78, 232, 78, .5),
            N(120, 96, "s = round[(L−1) · Σ nⱼ/MN]", 8),
            N(120, 112, "levels 3, 4 merge (→ 6)  ·  levels 5, 6, 7 merge (→ 7)", 7.5),
            N(120, 126, "output cannot invent levels: the result is only roughly flat", 7.5)]
    return svg(c, *out)

def d3044(c):
    return svg(c,
        axes(16, 112, 112, 16), N(114, 122, "r , z", 7, "end"), N(10, 18, "level", 7, "start"),
        curve(lambda x: 112 - 88 * ((x - 16) / 96) ** .55, 16, 112, 40, 1), N(24, 40, "T(r) (input CDF)", 7, "start"),
        curve(lambda x: 112 - 88 * ((x - 16) / 96) ** 2, 16, 112, 40, 1, "3 2"), N(76, 100, "G(z) (target CDF)", 7, "start"),
        dot(60, 64, None, r=1.8), arrow(60, 112, 60, 68, .8), N(60, 122, "r", 7),
        arrow(60, 64, 98, 64, .8), dash(98, 64, 98, 112, .8, "1 2"), dot(98, 64, None, r=1.8), N(98, 122, "z", 7),
        R(130, 20, 100, 70, "#f1f5f9", 1), N(180, 34, "s = T(r)", 7.5), N(180, 48, "v = G(z)", 7.5), N(180, 64, "set s = v ⇒", 7.5), N(180, 80, "z = G⁻¹[T(r)]", 8),
        N(180, 108, "match one frame's look", 7), N(180, 119, "to another's", 7), N(120, 138, "G is a staircase: take the z with G(z) closest to s", 7))

def d3045(c):
    b = 80
    out = []
    for i in range(3):
        for j in range(3):
            out.append(R(10 + i * 22, 20 + j * 22, 22, 22, "#ffffff" if (i + j) % 2 else "#f1f5f9", .8))
    out += [N(43, 14, "equalise each tile", 7), N(43, 96, "blend neighbours", 7),
            axes(104, b, 232, 14), N(232, b + 10, "k", 8, "end"), N(100, 18, "h(k)", 7, "end"),
            bell(110, 228, 140, 10, 62, b, 1),
            L(110, 36, 228, 36, .8, "3 2"), N(228, 46, "β (clip)", 7, "end"),
            R(131, 24, 18, 12, "#d9dee7", .6), N(158, 26, "excess ⇒ spread", 7, "start"), N(176, 36, "over all bins", 7, "start") if False else "",
            N(120, 112, "h_clip(k) = min(h(k), β)", 8), N(120, 126, "excess = Σ (h(k) − β)⁺ , redistributed evenly", 7.5),
            N(120, 140, "without the clip, flat tiles turn into noise", 7)]
    return svg(c, *out)

def d3046(c):
    p = [.19, .25, .21, .16, .08, .06, .03, .02]
    out = [axes(14, 90, 150, 14), N(150, 100, "r", 8, "end")]
    for i, v in enumerate(p):
        out += [R(22 + i * 16, 90 - v * 200, 12, v * 200, "#f1f5f9", .8), N(28 + i * 16, 100, str(i), 7)]
    out += [N(18, 12, "p(r)", 7, "start"),
            R(168, 14, 62, 90, "#ffffff", 1)]
    for i in range(8):
        out.append(N(180, 26 + i * 10.5, f"{i} →", 7, "end"))
        out.append(N(190, 26 + i * 10.5, str([1, 3, 5, 6, 6, 7, 7, 7][i]), 7.5, "start"))
    out += [N(215, 26, "merged", 6.5, "start") if False else "", L(204, 70, 204, 100, .6), N(214, 86, "merge", 6.5, "start"), L(204, 46, 204, 56, .6),
            N(100, 120, "round(7 × 0.19) = 1, round(7 × 0.44) = 3, round(7 × 0.65) = 5", 7.5),
            N(100, 134, "only five output levels: 1, 3, 5, 6, 7", 7.5)]
    return svg(c, *out)

CARDS = {
3041: dict(d=d3041, stmtKind="DEFINITION",
  statement=r"<b>Histogram equalization.</b> For a discrete image with $L$ grey levels and normalized histogram $p_r(r_j)$, the equalization transformation is $s_k=T(r_k)=(L-1)\sum_{j=0}^{k}p_r(r_j)$. It is monotonically non-decreasing and maps $[0,L-1]$ to $[0,L-1]$; the transformed image has a histogram that is approximately uniform.",
  hint="If the night frame only uses the darkest few levels, which curve spreads them over the whole scale automatically?",
  breakdown=[r"<strong>$p_r(r_j)$ = how crowded level $r_j$ is.</strong> The share of the frame's pixels at that grey level, from the histogram."
             ,
             r"<strong>$\sum_{j\le k}p_r(r_j)$ = the running total (the CDF).</strong> It climbs steeply where the levels are crowded and flatly where they are empty.",
             r"<strong>$(L-1)\times$ = scale to the full range.</strong> Multiplying the CDF by $L-1$ turns it into a ready-made curve from black to white, with no parameters to tune."],
  conn=r"<strong>Rescuing the night frame.</strong> Almost every pixel of the dark street sits in a few dark levels. Equalization uses the frame's own running total as the brightening curve, so the crowded dark levels are pulled apart and the empty bright levels squeezed.",
  cap="The night frame's histogram is crowded on the left. Passing every level r through T = (L−1)·CDF gives s with a histogram that is spread flat across all levels."),
3042: dict(d=d3042, stmtKind="THEOREM",
  statement=r"<b>Equalization gives a uniform density (probability integral transform).</b> Let $r\in[0,L-1]$ have a continuous density $p_r$ with strictly increasing CDF, and let $s=T(r)=(L-1)\int_0^r p_r(w)\,dw$. Then $s$ is uniformly distributed on $[0,L-1]$: $p_s(s)=\frac1{L-1}$.",
  hint="Why does pushing the grey levels through their own running total flatten the histogram?",
  breakdown=[r"<strong>$ds/dr=(L-1)\,p_r(r)$ = the slope of the curve is the crowding.</strong> Where many pixels sit, the curve is steep and pulls those levels apart.",
             r"<strong>$p_s(s)=p_r(r)\,|dr/ds|$ = the change-of-variables rule.</strong> Density in the new variable is the old density divided by the stretch.",
             r"<strong>$p_r\cdot\dfrac1{(L-1)p_r}=\dfrac1{L-1}$ = the crowding cancels.</strong> Crowded parts are stretched exactly as much as they were crowded, so the output has equal density everywhere."],
  conn=r"<strong>Why the lamp area is not overstretched.</strong> The curve is steepest where the night frame has most pixels and gentle where it has few, so crowded dark levels get as much room as the sparse bright ones.",
  cap="The S-curve s = T(r) is the running total of p(r). Its slope (L−1)·p(r) is steep where the histogram is tall, which cancels the crowding and makes p(s) = 1/(L−1)."),
3043: dict(d=d3043, stmtKind="ALGORITHM",
  statement=r"<b>Discrete equalization.</b> Given an $M\times N$ image with $n_j$ pixels at level $r_j$: (1) compute $p_r(r_j)=n_j/MN$; (2) accumulate the cumulative sums $\sum_{j\le k}p_r(r_j)$; (3) set $s_k=\operatorname{round}\!\big[(L-1)\sum_{j\le k}n_j/MN\big]$; (4) replace each pixel of level $r_k$ by $s_k$. The mapping is monotone, may merge levels, and cannot create levels with no input pixels.",
  hint="Why do two neighbouring grey levels sometimes end up as the same level after equalizing?",
  breakdown=[r"<strong>$\sum_{j\le k}n_j/MN$ = the CDF at level $k$.</strong> The share of the frame at that level or darker.",
             r"<strong>$(L-1)\times$ and round = the new level.</strong> Scale to the full range and round to a whole level.",
             r"<strong>Rounding merges neighbours.</strong> Two close CDF values can round to the same output level, so the output is only approximately flat and can have gaps."],
  conn=r"<strong>The recorder's lookup table.</strong> The camera builds an 8-entry table from one frame's histogram: input level on the left, output level on the right. Then every pixel is looked up.",
  cap="For a 3-bit frame the table reads p(r) → running total → ×7 → round. Levels 3 and 4 both become 6, and levels 5, 6, 7 all become 7."),
3044: dict(d=d3044, stmtKind="ALGORITHM",
  statement=r"<b>Histogram specification (matching).</b> Given an input with equalizing map $s=T(r)=(L-1)\sum p_r$ and a desired density $p_z$ with $G(z)=(L-1)\sum p_z$: compute $T$; compute $G$; for each $r$ output $z=G^{-1}\big(T(r)\big)$ (for a staircase $G$, the $z$ whose $G(z)$ is closest to $s$). The result has a histogram close to $p_z$.",
  hint="If flat is not what you want, how do you aim the output at the look of a different frame?",
  breakdown=[r"<strong>$s=T(r)$ = equalize the input.</strong> Send the frame to the flat middle ground first.",
             r"<strong>$G(z)$ = equalize the target.</strong> The same trip for the histogram shape you want.",
             r"<strong>$z=G^{-1}(T(r))$ = go in with $T$, come out with $G^{-1}$.</strong> Both sides pass through the same flat middle ground, so joining them matches the shapes."],
  conn=r"<strong>Making night footage look like a good daytime frame.</strong> Take the daytime frame's histogram as the target and push each night pixel through $T$ and then back out through $G^{-1}$.",
  cap="A pixel r goes up through the input CDF T to a level s, then across and down through the target CDF G (inverted) to z. The result z = G⁻¹[T(r)] has the target's histogram."),
3045: dict(d=d3045, stmtKind="ALGORITHM",
  statement=r"<b>Local equalization and CLAHE.</b> Local histogram equalization divides the image into tiles and equalizes each tile separately. Contrast-limited adaptive HE (CLAHE) clips each tile's histogram at a limit $\beta$: $h_{\rm clip}(k)=\min(h(k),\beta)$, redistributes the total excess $\sum_k(h(k)-\beta)^+$ uniformly over all bins, equalizes with the clipped histogram, and bilinearly interpolates between neighbouring tiles' mappings to remove tile seams.",
  hint="Why does equalizing each little tile of the frame turn flat sky into noise unless you cap the histogram?",
  breakdown=[r"<strong>Tiles = equalize locally.</strong> Each patch of the frame gets its own curve, so local contrast, such as a dark alley, is boosted.",
             r"<strong>$h_{\rm clip}=\min(h,\beta)$ = cap the tall bars.</strong> A tall narrow bar (a flat wall) would give a very steep curve that magnifies noise; clipping limits the slope.",
             r"<strong>Redistribute the excess, blend the tiles.</strong> The clipped mass is spread over all bins so no pixels are lost, and blending neighbours hides the tile edges."],
  conn=r"<strong>Dark alley, bright shopfront.</strong> One curve for the whole frame cannot serve both. Tiles fix that; the clip stops the blank wall of the building from turning into grain.",
  cap="Each tile of the frame has its own histogram h(k). Bars above the clip limit β are cut and the excess is spread over all bins; neighbouring tiles are then blended."),
3046: dict(d=d3046, stmtKind="WORKED EXAMPLE",
  statement=r"<b>Example.</b> A 3-bit image ($L=8$) with $4096$ pixels has $p_r=(0.19,0.25,0.21,0.16,0.08,0.06,0.03,0.02)$. The cumulative sums are $0.19,0.44,0.65,0.81,0.89,0.95,0.98,1.00$; times 7 they give $1.33,3.08,4.55,5.67,6.23,6.65,6.86,7$; rounded: $r=0,\dots,7\mapsto1,3,5,6,6,7,7,7$. The output uses five distinct levels $\{1,3,5,6,7\}$.",
  hint="After equalizing, how many distinct grey levels does the street frame actually use?",
  breakdown=[r"<strong>$s_0=\operatorname{round}(7\cdot0.19)=1$.</strong> The darkest level is lifted off black because 19% of the frame sits there.",
             r"<strong>$s_1=\operatorname{round}(7\cdot0.44)=3,\ s_2=5$.</strong> Each level moves up by the share of the frame at or below it.",
             r"<strong>Levels 3, 4 merge and 5, 6, 7 merge.</strong> Their running totals round to the same number, so only five output levels remain; the histogram cannot be exactly flat."],
  conn=r"<strong>A tiny frame, a small table.</strong> Eight dark-to-bright levels become five. The crowded dark ones spread out; the sparse bright ones collapse together.",
  cap="The eight input levels and their equalized outputs: 0→1, 1→3, 2→5, 3 and 4→6, 5, 6 and 7→7. Merged levels are why only five levels remain."),
}

STORY = {
 3041: dict(s="STORY 2 · STEP 13 · FLATTEN THE HISTOGRAM", b="A dark frame crowds a few levels. <b>Equalization</b> uses the frame's own running total as the curve, spreading the levels.",
   f=[["3022", "a point operation"], ["3021", "the histogram"], ["3015", "work on intensity only"]], n=[["3042", "why it flattens"], ["3043", "the real discrete recipe"]]),
 3042: dict(s="STORY 2 · STEP 14 · WHY IT WORKS", b="The curve's slope is the crowding, so crowding cancels and the output density is flat: a <b>probability integral transform</b>.",
   f=[["3041", "the CDF curve"]], n=[["3043", "the discrete case"]]),
 3043: dict(s="STORY 2 · STEP 15 · THE RECIPE", b="Cumulate, multiply by $L-1$, round: a <b>lookup table</b> that may merge levels.",
   f=[["3042", "the idea"]], n=[["3044", "aim at a chosen histogram"], ["3046", "numbers"]]),
 3044: dict(s="STORY 2 · STEP 16 · AIM THE HISTOGRAM", b="<b>Specification</b> equalizes both the input and a target, then joins them: $z=G^{-1}(T(r))$.",
   f=[["3043", "T from equalization"]], n=[["3045", "do it locally"]]),
 3045: dict(s="STORY 2 · STEP 17 · DO IT LOCALLY", b="<b>CLAHE</b> equalizes tiles with a clipped histogram so local contrast improves without amplifying noise.",
   f=[["3044", "matching"], ["3043", "equalization"]], n=[["3046", "numbers"]]),
 3046: dict(s="STORY 2 · STEP 18 · CHECK BY HAND", b="A 3-bit frame worked through: eight levels become five.",
   f=[["3043", "the recipe"]], n=[["3051", "next: look at neighbouring pixels, not one pixel"]]),
}
FIX = build_fix(CARDS)
