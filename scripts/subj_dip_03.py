"""DIP topic 03 (histograms, point operations, Otsu). Everyday picture: a street camera on a pole."""
from street_lib import *

SUBJECT = "DIP"

def hist(x0, base, vals, bw=7, gap=1, fill="#f1f5f9"):
    return bars(x0, base, vals, bw, gap, fill)

def d3021(c):
    return svg(c,
        frame(12, 20, 70, 50, "night frame"), building(18, 28, 30, 36, 2, 1, "#d9dee7"), person(62, 66, 22),
        arrow(84, 46, 104, 46, 1),
        axes(112, 100, 230, 22), N(230, 110, "rₖ", 8, "end"), N(106, 22, "nₖ", 8, "end"),
        hist(118, 100, [70, 62, 40, 22, 10, 6, 4, 8, 14, 8], 9, 2),
        N(130, 14, "dark: mass at left", 7, "start"),
        N(40, 92, "p(rₖ) = nₖ/MN", 8), N(40, 104, "Σ p(rₖ) = 1", 8),
        N(120, 130, "same pixels in any order ⇒ same histogram", 7.5, "middle"), N(120, 140, "(the position of everything is lost)", 7, "middle"))

def d3022(c):
    sx = lambda r: 24 + r * 0.9
    out = [axes(24, 116, 130, 18), N(132, 124, "r", 8, "start"), N(16, 18, "s", 8, "end"), L(24, 116, 114, 26, .6, "2 3"),
           curve(lambda x: 116 - 90 * ((x - 24) / 90) ** .45, 24, 114, 40, 1), N(32, 40, "γ < 1 brightens", 7, "start"),
           curve(lambda x: 116 - 90 * ((x - 24) / 90) ** 2.2, 24, 114, 40, 1, "3 2"), N(100, 88, "γ > 1 darkens", 7, "start"),
           curve(lambda x: 116 - 90 * math.log(1 + 9 * (x - 24) / 90) / math.log(10), 24, 114, 40, .8, "1 2"),
           L(114, 116, 24, 26, .8, None) if False else "",
           R(144, 22, 86, 30, "#f1f5f9", 1), N(187, 34, "s = T(r), same T", 7.5), N(187, 45, "for every pixel", 7.5),
           N(187, 72, "negative: s = L−1−r", 7), N(187, 84, "log: s = c·log(1+r)", 7), N(187, 96, "gamma: s = c·rᵞ", 7),
           N(120, 138, "brighten the night frame, pixel by pixel", 7.5)]
    return svg(c, *out)

def d3023(c):
    b = 90
    return svg(c,
        axes(14, b, 150, 14), N(150, b + 10, "f", 8, "end"),
        curve(lambda x: b - 56 * math.exp(-((x - 46) / 14) ** 2) - 44 * math.exp(-((x - 110) / 14) ** 2), 18, 146, 60, 1),
        N(46, 28, "road", 7), N(110, 38, "person", 7),
        L(80, b, 80, 20, 1, "3 2"), N(80, 16, "T", 8),
        N(46, b + 10, "μ₁", 7), N(110, b + 10, "μ₂", 7), N(80, b + 10, "½(μ₁+μ₂)", 6.5),
        R(164, 20, 66, 46, "#f1f5f9", 1), N(197, 32, "g = 1 if f > T", 7), N(197, 43, "g = 0 if f ≤ T", 7), N(197, 58, "binary mask", 7),
        frame(172, 78, 20, 22, None, "#ffffff"), frame(200, 78, 20, 22, None, "#d9dee7"), person(210, 98, 14), N(182, 112, "f", 7), N(210, 112, "g", 7),
        N(120, 135, "any T in the valley separates people from road", 7.5))

def d3024(c):
    b = 84
    return svg(c,
        axes(14, b, 150, 12), N(150, b + 10, "k", 8, "end"),
        curve(lambda x: b - 50 * math.exp(-((x - 46) / 14) ** 2) - 42 * math.exp(-((x - 108) / 14) ** 2), 18, 146, 60, 1),
        L(78, b, 78, 20, 1, "3 2"), N(78, 16, "k", 8),
        N(46, 30, "ω₀", 8), N(108, 36, "ω₁", 8), dot(46, b + 8, None, r=1.6), dot(108, b + 8, None, r=1.6), N(46, b + 18, "μ₀", 7), N(108, b + 18, "μ₁", 7),
        arrow(46, b + 4, 108, b + 4, .8) if False else "",
        L(46, 116, 108, 116, .8), L(46, 112, 46, 120, .8), L(108, 112, 108, 120, .8), N(77, 128, "μ₀ − μ₁", 7),
        R(164, 20, 66, 62, "#f1f5f9", 1), N(197, 34, "σB²(k) =", 7.5), N(197, 46, "ω₀ ω₁", 7.5), N(197, 58, "(μ₀ − μ₁)²", 7.5), N(197, 74, "big = well split", 7),
        N(197, 100, "k* = argmax σB²", 7.5), N(197, 112, "= min within-class", 7), N(197, 122, "variance", 7))

def d3025(c):
    b = 100
    return svg(c,
        axes(18, b, 150, 14), N(150, b + 10, "k", 8, "end"),
        curve(lambda x: b - 78 * (1 / (1 + math.exp(-(x - 70) / 8))) * 0.6 - 30 * (1 / (1 + math.exp(-(x - 110) / 6))), 22, 146, 60, 1),
        N(26, 38, "ω(k) = Σ pᵢ", 7, "start"), 
        L(84, b, 84, 30, 1, "3 2"), N(84, b + 10, "k", 8), dot(84, 54, None, r=1.8), N(88, 52, "μ(k)", 7, "start"),
        L(18, 24, 146, 24, .6, "1 3"), N(24, 20, "μT", 7, "start"),
        R(162, 20, 68, 70, "#f1f5f9", 1), N(196, 34, "σB²(k) =", 7.5), N(196, 46, "[μT·ω − μ]²", 7.5), L(170, 51, 222, 51, .8), N(196, 62, "ω (1 − ω)", 7.5), N(196, 80, "one pass: O(L)", 7),
        N(120, 128, "running totals along the histogram of the frame", 7.5))

def d3026(c):
    b = 88
    vals = {1: 4, 2: 1, 6: 2, 7: 3}
    out = [axes(14, b, 226, 14)]
    for k in range(8):
        h = vals.get(k, 0) * 11
        if h: out.append(R(40 + k * 22, b - h, 16, h, "#f1f5f9", .8))
        out.append(N(48 + k * 22, b + 10, str(k), 7))
    out += [L(104, b, 104, 16, 1, "3 2"), N(104, 12, "k = 2", 7.5),
            N(40, 22, "ω₀ = 0.5", 7, "start"), N(40, 32, "μ₀ = 1.2", 7, "start"), N(160, 24, "ω₁ = 0.5", 7, "start"), N(160, 34, "μ₁ = 6.6", 7, "start"),
            R(108, 60, 44, 12, "none", .8, 0, "2 2"), N(130, 69, "empty", 6.5),
            N(120, 112, "σB²(2) = 0.5·0.5·(6.6 − 1.2)² = 7.29", 7.5),
            N(120, 125, "k = 2, 3, 4, 5 tie ⇒ take the middle, ≈ 3.5", 7.5)]
    return svg(c, *out)

CARDS = {
3021: dict(d=d3021, stmtKind="DEFINITION",
  statement=r"<b>Image histogram.</b> For a digital image of size $M\times N$ with gray levels $r_0,\dots,r_{L-1}$, the histogram is $h(r_k)=n_k$, the number of pixels with level $r_k$, and the normalized histogram $p(r_k)=n_k/MN$ estimates the probability of level $r_k$, with $\sum_{k=0}^{L-1}p(r_k)=1$. The histogram carries no spatial information.",
  hint="If you shuffle every pixel of the night frame, which picture of it does not change?",
  breakdown=[r"<strong>$n_k$ = how many pixels have grey level $r_k$.</strong> One bar of the tally per level, from black to white.",
             r"<strong>$p(r_k)=n_k/MN$ = the share of the frame at that level.</strong> Dividing by the total pixel count turns counts into probabilities.",
             r"<strong>$\sum p(r_k)=1$ = nothing is left out.</strong> Every pixel is in exactly one bar, so the shares add to one."],
  conn=r"<strong>A night frame piles up on the left.</strong> The street at night is mostly dark, so the bars crowd near black with a small bump for the lamps. The tally says nothing about where the lamp or the person is.",
  cap="A dark night frame and its histogram: nₖ pixels at each grey level rₖ, p(rₖ) = nₖ/MN, all the bars adding to 1. Shuffling the pixels leaves the bars unchanged."),
3022: dict(d=d3022, stmtKind="DEFINITION",
  statement=r"<b>Point (intensity) transformation.</b> A point operation replaces each pixel value $r$ by $s=T(r)$, with the same function $T$ for every pixel and independent of neighbours. Standard choices on $[0,L-1]$: negative $s=L-1-r$; log $s=c\log(1+r)$; power law $s=c\,r^{\gamma}$ ($\gamma\lt1$ brightens, $\gamma\gt1$ darkens); contrast stretching $s=\frac{r-r_{\min}}{r_{\max}-r_{\min}}(L-1)$.",
  hint="Which curve would you bend to lift the dark street without touching the lamps?",
  breakdown=[r"<strong>$s=T(r)$ = one rule for every pixel.</strong> Each pixel looks only at its own value; its neighbours play no part.",
             r"<strong>$c\,r^{\gamma}$ and $c\log(1+r)$ = lift the dark end.</strong> For $\gamma\lt1$ and the log, dark values are spread out and bright ones are squeezed together.",
             r"<strong>$\frac{r-r_{\min}}{r_{\max}-r_{\min}}(L-1)$ = stretch the used range.</strong> Move the darkest value in the frame to 0 and the brightest to $L-1$."],
  conn=r"<strong>Brightening the night footage.</strong> Run every pixel of the dim street frame through the same bent curve: shadows lift, the lamp stays bright. A pixel that was already black cannot be recovered, because the curve only moves values.",
  cap="Curves s = T(r) on the street frame: γ < 1 and the log lift dark pixels, γ > 1 darkens, the negative flips the scale. Every pixel uses the same curve."),
3023: dict(d=d3023, stmtKind="ALGORITHM",
  statement=r"<b>Global thresholding (iterative).</b> To segment an image $f$ whose histogram has two modes: choose an initial $T$ (the mean of $f$); split pixels into $G_1=\{f\gt T\}$ and $G_2=\{f\le T\}$; compute their means $\mu_1,\mu_2$; set $T\leftarrow\frac12(\mu_1+\mu_2)$; repeat until $T$ changes by less than a tolerance. Then $g(x,y)=1$ if $f(x,y)\gt T$ and $0$ otherwise.",
  hint="When the frame has road and people, where on the histogram should the cut go?",
  breakdown=[r"<strong>$g=1$ if $f\gt T$, else $0$ = a yes/no mask.</strong> Every pixel above the cut becomes object, every pixel at or below it becomes background.",
             r"<strong>$\mu_1,\mu_2$ = the average brightness of each side.</strong> Where the two humps of the histogram are centred.",
             r"<strong>$T\leftarrow\frac12(\mu_1+\mu_2)$ = move the cut to the middle.</strong> Repeating this settles the cut in the valley between the humps."],
  conn=r"<strong>People on a dark road.</strong> The road makes one hump, the lit passers-by another. Drawing the cut in the valley between them gives a mask where the people are white. A shadow across half the road would drag one hump over and break a single cut.",
  cap="A two-hump histogram of the street frame: road and person. The cut T sits in the valley, halfway between the means μ₁ and μ₂, and gives the binary mask g."),
3024: dict(d=d3024, stmtKind="ALGORITHM",
  statement=r"<b>Otsu's method.</b> For a normalized histogram $p_i$ and a trial threshold $k$, let $\omega_0(k)=\sum_{i\le k}p_i$, $\omega_1=1-\omega_0$, with class means $\mu_0(k),\mu_1(k)$. The between-class variance is $\sigma_B^2(k)=\omega_0\omega_1(\mu_0-\mu_1)^2$. Otsu's threshold is $k^*=\arg\max_k\sigma_B^2(k)$, which also minimizes the within-class variance because the total variance is fixed.",
  hint="Which cut makes the two groups of pixels as far apart and as balanced as possible?",
  breakdown=[r"<strong>$\omega_0,\omega_1$ = how many pixels are on each side of the cut.</strong> The two shares of the frame, adding to 1.",
             r"<strong>$(\mu_0-\mu_1)^2$ = how far apart the two groups are.</strong> The squared gap between their average brightnesses.",
             r"<strong>$\arg\max_k\,\omega_0\omega_1(\mu_0-\mu_1)^2$ = the best cut.</strong> A big gap and balanced groups give a large value; the cut with the largest value wins."],
  conn=r"<strong>Let the frame choose its own cut.</strong> Instead of guessing a brightness, try every cut on the street histogram and keep the one that separates road from people best. It fails when one side is tiny, like a single far-away person.",
  cap="A cut k splits the street histogram into classes with weights ω₀, ω₁ and means μ₀, μ₁. Otsu picks the k with the largest ω₀ω₁(μ₀ − μ₁)²."),
3025: dict(d=d3025, stmtKind="PROPOSITION",
  statement=r"<b>Otsu with cumulative sums.</b> Let $\omega(k)=\sum_{i\le k}p_i$, $\mu(k)=\sum_{i\le k}i\,p_i$ and $\mu_T=\mu(L-1)$. Then $\sigma_B^2(k)=\dfrac{[\mu_T\,\omega(k)-\mu(k)]^2}{\omega(k)\,[1-\omega(k)]}$ for $0\lt\omega(k)\lt1$, so all $L$ values are computed in one pass, and $k^*=\arg\max_k\sigma_B^2(k)$; if several $k$ tie, their average is taken.",
  hint="How can you score every possible cut by sweeping once along the histogram?",
  breakdown=[r"<strong>$\omega(k)$ = running share of pixels up to $k$.</strong> The fraction of the frame at or below the cut.",
             r"<strong>$\mu(k)$ = running sum of level × share.</strong> With $\mu_T$ (the whole frame's mean) it gives both class means without a second pass.",
             r"<strong>$\omega(1-\omega)$ in the denominator = the balance term.</strong> It is zero when one class is empty, so those $k$ are skipped."],
  conn=r"<strong>One sweep along the night histogram.</strong> Keep two running totals as you walk from black to white and read the score of every cut off them, instead of recomputing the two groups each time.",
  cap="Walking along the street histogram we keep ω(k) (running share) and μ(k) (running mean); with the total mean μT they give σB²(k) in one pass."),
3026: dict(d=d3026, stmtKind="WORKED EXAMPLE",
  statement=r"<b>Example.</b> A 10-pixel image has grey levels $1,1,1,1,2,6,6,7,7,7$, so $\mu_T=3.9$. At $k=2$: $\omega_0=\omega_1=0.5$, $\mu_0=1.2$, $\mu_1=6.6$ and $\sigma_B^2(2)=0.5\cdot0.5\,(6.6-1.2)^2=7.29$, while $\sigma_B^2(1)\approx5.6$ and $\sigma_B^2(6)\approx4.1$. Levels 3, 4, 5 are empty, so $k=2,3,4,5$ all give 7.29 and the threshold reported is the middle, about 3.5.",
  hint="When several cuts tie in the empty gap, which value do you report?",
  breakdown=[r"<strong>$\mu_0=1.2,\ \mu_1=6.6$ = the dark and bright groups.</strong> Dark: four 1s and one 2. Bright: two 6s and three 7s.",
             r"<strong>$0.5\cdot0.5\,(5.4)^2=7.29$ = the score of the cut.</strong> Balanced halves and a wide gap give the best score.",
             r"<strong>$k=2,\dots,5$ tie = empty levels in the gap.</strong> No pixel lies there, so moving the cut through the gap changes nothing; report the middle."],
  conn=r"<strong>Ten pixels of a tiny frame.</strong> Four dark road pixels, one dim, and five bright pixels of a person. Any cut in the empty gap separates them equally, so the safe answer is the gap's middle, where future pixels are least likely to be misplaced.",
  cap="A 10-pixel histogram with levels 1, 2, 6, 7. The cut k = 2 gives μ₀ = 1.2 and μ₁ = 6.6, and σB² = 7.29; the empty levels 3 to 5 tie, so the middle (3.5) is reported."),
}

STORY = {
 3021: dict(s="STORY 2 · STEP 1 · COUNT THE LEVELS", b="Before changing the frame we tally how many pixels sit at each grey level: the <b>histogram</b>. It shows exposure but forgets where things are.",
   f=[["3016", "pixels hold numbers"]], n=[["3022", "bend the levels with a curve"], ["3023", "split by level"], ["3041", "flatten the histogram"]]),
 3022: dict(s="STORY 2 · STEP 2 · BEND THE LEVELS", b="A <b>point operation</b> pushes every pixel through the same curve $T$: brighten, darken, stretch.",
   f=[["3021", "read the histogram"]], n=[["3023", "a step curve gives a mask"], ["3043", "the best curve is the CDF"]]),
 3023: dict(s="STORY 2 · STEP 3 · SPLIT BY A CUT", b="If the histogram has two humps, a single cut $T$ in the valley turns the frame into a <b>binary mask</b>.",
   f=[["3022", "a point operation"], ["3021", "two humps"]], n=[["3024", "choose the cut automatically"], ["3031", "clean the mask with morphology"]]),
 3024: dict(s="STORY 2 · STEP 4 · THE BEST CUT", b="<b>Otsu</b> tries every cut and keeps the one that separates the two groups best (largest between-class variance).",
   f=[["3023", "a cut"]], n=[["3025", "compute it fast"]]),
 3025: dict(s="STORY 2 · STEP 5 · ONE PASS", b="Running totals $\\omega(k),\\mu(k)$ give every cut's score in <b>one sweep</b> over the histogram.",
   f=[["3024", "Otsu's score"]], n=[["3026", "a worked example"]]),
 3026: dict(s="STORY 2 · STEP 6 · CHECK BY HAND", b="Ten pixels worked through: the best cut sits in the <b>empty gap</b>, so report the middle of the tie.",
   f=[["3025", "the formula"]], n=[["3031", "next: clean up the mask"]]),
}
FIX = build_fix(CARDS)
