"""StoMA topic 15 (modes of convergence). F1 picture: Max's running win rate and lap-time estimates settling race after race; the sliding window and the escaping spike told with laps across all possible races."""
from f1_lib import *

SUBJECT = "StoMA"

def bx(x, y, w, h, s, fill="#f1f5f9"):
    return R(x, y, w, h, fill, 1, 3) + N(x + w / 2, y + h / 2 + 2.5, s, 7.5)

def d1(c):
    return svg(c, bx(20, 30, 54, 24, "a.s."), bx(98, 30, 54, 24, "in prob."), bx(176, 30, 50, 24, "in law"),
        arrow(74, 42, 98, 42, 1), arrow(152, 42, 176, 42, 1),
        bx(20, 80, 54, 24, "Lᵖ"), bx(98, 80, 54, 24, "Lʳ (r < p)"), arrow(74, 92, 98, 92, 1), arrow(125, 80, 125, 56, 1),
        N(120, 18, "the four modes of Xₙ → X", 7.5), N(120, 124, "stronger → weaker; the reverse arrows fail in general", 7),
        N(120, 138, "each mode asks something different of the race-by-race record", 7))

def d2(c):
    return svg(c, ax(24, 112, 226, 14), N(226, 124, "x", 7, "end"),
        fn(lambda x: 112 - 24 * math.exp(-((x - 90) ** 2) / 800), 30, 220, 40, 1.1) if False else "",
        fn(lambda x: 112 - 22 * math.exp(-((x - 120) ** 2) / 1600), 30, 220, 40, 1.0, "4 3"),
        fn(lambda x: 112 - 40 * math.exp(-((x - 120) ** 2) / 500), 30, 220, 40, 1.0),
        fn(lambda x: 112 - 60 * math.exp(-((x - 120) ** 2) / 90), 30, 220, 60, 1.1),
        N(120, 124, "c", 8), N(160, 52, "law piles up at c", 7, "start"),
        N(30, 24, "Xₙ → c in law ⇔ Xₙ → c in probability (c constant)", 7, "start"),
        N(30, 36, "Xₙ → X in prob ⇒ some subsequence → X a.s.", 7, "start"),
        N(120, 140, "a constant limit leaves nothing to couple", 7))

def d3(c):
    out = N(120, 12, "lap n question: is the warning light on (Xₙ = 1)?", 7)
    rows = [(1, 0, 1), (2, 0, .5), (2, .5, .5), (3, 0, .25), (3, .25, .25), (3, .5, .25), (3, .75, .25)]
    for i, (k, a, w) in enumerate(rows):
        y = 26 + i * 12
        out += L(30, y + 8, 210, y + 8, 1) + R(30 + a * 180, y, w * 180, 8, "#d9dee7", 1)
        out += N(24, y + 7, f"X{'₁₂₃₄₅₆₇'[i]}", 6, "end")
    return svg(c, out, N(120, 118, "ℙ(Xₙ = 1) = width → 0 ⇒ Xₙ → 0 in probability", 7.5), N(120, 130, "but every ω is covered again and again: no a.s. limit", 7.5),
        N(120, 141, "lim sup Xₙ(ω) = 1 for every ω", 7))

def d4(c):
    out = ax(20, 112, 226, 14) + N(226, 12, "ω ∈ [0,1]", 7, "end") + N(24, 12, "Xₙ(ω)", 7, "start")
    for i, (n, x0) in enumerate([(1, 30), (2, 76), (3, 122), (4, 168)]):
        w = 40 / n
        h = 20 * n
        out += R(x0, 112 - h, w, h, "#d9dee7", 1) + N(x0 + 20, 124, f"n = {n}", 6.5)
    return svg(c, out, N(30, 20, "spike of height n² on [0, 1/n]", 7, "start") if False else N(120, 14, "spike of height n² on [0, 1/n]", 7),
        N(120, 134, "any fixed ω ends up outside the spike: Xₙ(ω) → 0 a.s.", 7), N(30, 44, "but 𝔼|Xₙ| = n", 7.5, "start"), N(30, 56, "→ ∞: no L¹ limit", 7.5, "start"))

def d5(c):
    return svg(c, ax(24, 100, 226, 20), N(226, 112, "x", 7, "end"),
        fn(lambda x: 100 - 50 * math.exp(-((x - 80) ** 2) / 500), 30, 220, 50, 1.1), N(80, 38, "Xₙ → X", 7.5),
        fn(lambda x: 100 - 28 * math.exp(-((x - 160) ** 2) / 1600), 30, 220, 50, 1.1, "4 3"), N(160, 62, "cX (c = 2)", 7.5),
        N(30, 20, "Xₙ → X in law, Yₙ → c in prob.", 7, "start"), N(120, 124, "Xₙ Yₙ → cX   and   Xₙ/Yₙ → X/c  (c ≠ 0)", 7.5),
        N(120, 138, "in-law limits can be rescaled by a probability limit", 7))

def d6(c):
    return svg(c, ax(24, 90, 110, 24), N(110, 102, "numerator", 7, "end"), fn(lambda x: 90 - 50 * math.exp(-((x - 66) ** 2) / 300), 30, 108, 40, 1.1),
        N(66, 38, "√n(X̄ − μ)/σ → 𝒩(0,1)", 6.5),
        ax(124, 90, 226, 24), N(226, 102, "Sₙ/σ", 7, "end"), fn(lambda x: 90 - 60 * math.exp(-((x - 170) ** 2) / 40), 130, 222, 40, 1.1), N(190, 24, "→ 1 in prob.", 7),
        N(66, 114, "÷", 9), N(120, 126, "Tₙ → 𝒩(0,1)/1 = 𝒩(0,1)", 8), N(120, 140, "Slutsky: unknown σ replaced by Sₙ costs nothing in the limit", 6.8))

CARDS = {
31501: dict(d=d1, kind="DEFINITION",
  stmt=r"<b>Modes of convergence.</b> For random variables $X_n,X$: $X_n\to X$ almost surely if $\mathbb P(X_n\to X)=1$; in probability if $\mathbb P(|X_n-X|>\varepsilon)\to0$ for all $\varepsilon>0$; in $L^p$ if $\mathbb E|X_n-X|^p\to0$; in distribution if $F_{X_n}(x)\to F_X(x)$ at continuity points of $F_X$. Then a.s. $\Rightarrow$ in probability $\Rightarrow$ in distribution, and $L^p\Rightarrow L^r\Rightarrow$ in probability for $p>r\ge1$ (Grimmett 7.2; Ross 8.2).",
  hint="What are the four different things “Max's running win rate settles down” can mean, and which imply which?",
  bd=[r"<strong>a.s. $\mathbb P(X_n\to X)=1$ = every typical record settles.</strong> Follow one endless run of races: with probability 1, it converges.",
      '<strong>in probability / $L^p$ = each race count is close, on average.</strong> After race $n$ a big miss is rare; or the average size of the miss shrinks.',
      '<strong>in distribution = only the shape of the law settles.</strong> The histogram of $X_n$ converges, even if the actual records never agree.'],
  conn="<strong>Four kinds of “settling down”.</strong> Watch Max's win rate race after race. You could demand that every run of races homes in; that after race $n$ it is rarely far off; that the typical size of the error shrinks; or just that its histogram stops changing.",
  cap='Boxes: a.s. ⇒ in probability ⇒ in law, and Lᵖ ⇒ Lʳ ⇒ in probability. Stronger modes sit to the left; the reverse arrows fail in general.'),
31502: dict(d=d2, kind="THEOREM",
  stmt=r"<b>Partial converses.</b> (i) If $c$ is a constant, $X_n\xrightarrow{d}c$ iff $X_n\xrightarrow{P}c$. (ii) If $X_n\xrightarrow{P}X$, there is a subsequence $n_k$ with $X_{n_k}\xrightarrow{a.s.}X$. (iii) If $X_n\xrightarrow{P}X$ and $|X_n|\le Y$ with $\mathbb E[Y]<\infty$, then $X_n\xrightarrow{L^1}X$ (Grimmett 7.3; Ross 8.2).",
  hint='When do the weaker modes imply the stronger ones after all?',
  bd=[r"<strong>$X_n\xrightarrow{d}c\iff X_n\xrightarrow{P}c$ = a constant limit.</strong> If the histogram piles up at a single value $c$, then $X_n$ is within $\varepsilon$ of $c$ with chance tending to 1.",
      r"<strong>$\exists\,n_k$ with a.s. convergence = pick a thin enough subsequence.</strong> If $X_n\to X$ in probability, pick races where the miss chance is summable; Borel–Cantelli then finishes the job.",
      '<strong>Domination = no mass escapes.</strong> A fixed integrable cap $Y$ keeps the average error from hiding in rare huge values.'],
  conn="<strong>When the end result is a number.</strong> If the histogram of Max's estimated average lap time piles up at one number, then after a typical race count the estimate is close to it; and a thinned-out set of races will settle in the strong sense.",
  cap='Histograms of Xₙ sharpening around the constant c. A law that piles up at a point is the same as convergence in probability; thinning out the races then gives a.s. convergence.'),
31503: dict(d=d3, kind="WORKED EXAMPLE",
  stmt=r"<b>Sliding typewriter.</b> On $\Omega=[0,1]$ with Lebesgue measure, enumerate intervals of length $1/k$ sweeping $[0,1]$ for $k=1,2,\ldots$, and let $X_n=\mathbf 1_{I_n}$ for the $n$-th interval. Then $\mathbb P(X_n=1)=1/k\to0$, so $X_n\xrightarrow{P}0$, but each $\omega$ lies in infinitely many $I_n$, so $\limsup X_n(\omega)=1$ for all $\omega$: $X_n\not\to0$ a.s. (Grimmett 7.2; Durrett 2.3).",
  hint='Can a warning light be almost surely off on any given lap, and yet never stay off in any single race?',
  bd=[r"<strong>$\mathbb P(X_n=1)=1/k\to0$ = a shrinking block.</strong> On lap $n$ the light is on only for a block of races of width $1/k$, whose chance goes to zero.",
      r"<strong>$\limsup X_n(\omega)=1$ = every race is hit again.</strong> Each sweep of the blocks passes over every race $\omega$, so in every race the light comes on infinitely often.",
      r"<strong>$\not\to0$ a.s. = no race settles.</strong> In each race the light flips between 0 and 1 forever, so a.s. convergence fails though convergence in probability holds."],
  conn="<strong>A warning light that wanders.</strong> Picture an endless race. On each lap, a small and shrinking slice of all possible races gets a warning light on Max's steering wheel. On any one lap he is almost surely fine, yet in every possible race the light comes on again and again.",
  cap='Rows are laps X₁, X₂, …: a block of width 1/k sweeping across [0,1], the set of all races. The block shrinks, so ℙ(Xₙ = 1) → 0, but it keeps sweeping, so no single race ω has a limit.'),
31504: dict(d=d4, kind="WORKED EXAMPLE",
  stmt=r"<b>Escaping spike.</b> On $[0,1]$ with Lebesgue measure let $X_n=n^2\mathbf 1_{(0,1/n)}$. For each fixed $\omega$, $X_n(\omega)=0$ once $n>1/\omega$, so $X_n\to0$ a.s., but $\mathbb E|X_n|=n^2\cdot\frac1n=n\to\infty$, so $X_n\not\to0$ in $L^1$ (Grimmett 7.2; Durrett 2.3).",
  hint='Can the time lost settle to zero in every single race while its average size blows up?',
  bd=[r"<strong>$X_n=n^2\mathbf 1_{(0,1/n)}$ = a tall spike on a thin window.</strong> On lap $n$, a loss of $n^2$ seconds in the first $1/n$ of the races, zero elsewhere.",
      r"<strong>$X_n(\omega)=0$ for $n>1/\omega$ = every race escapes the spike.</strong> The window shrinks to zero length, so each fixed race $\omega$ falls outside it eventually: a.s. convergence to 0.",
      r"<strong>$\mathbb E|X_n|=n\to\infty$ = the area grows.</strong> Height times width is $n^2\cdot\frac1n=n$: a rare, huge loss dominates the average."],
  conn='<strong>Rare disasters.</strong> In any given race Max eventually stops losing time, but the rare disaster (a spin, a puncture) gets so costly when it does strike that its share of the average grows without bound.',
  cap='Spikes of height n² on [0, 1/n] for laps n = 1, 2, 3, 4. Any fixed race ω escapes eventually (Xₙ → 0 a.s.), but the area under each spike is n, so 𝔼|Xₙ| → ∞.'),
31505: dict(d=d5, kind="THEOREM",
  stmt=r"<b>Slutsky's theorem.</b> If $X_n\xrightarrow{d}X$ and $Y_n\xrightarrow{P}c$ for a constant $c$, then $X_n+Y_n\xrightarrow{d}X+c$, $X_nY_n\xrightarrow{d}cX$, and $X_n/Y_n\xrightarrow{d}X/c$ if $c\ne0$. The continuous mapping theorem: if $g$ is continuous a.e. under the law of $X$ and $X_n\xrightarrow{d}X$, then $g(X_n)\xrightarrow{d}g(X)$ (Ross 8.3; Grimmett 7.2).",
  hint='If one estimate settles in shape and another settles to a number, how does their product behave?',
  bd=[r"<strong>$X_n\xrightarrow{d}X$ = the first quantity settles in shape.</strong> Its histogram converges, say to a bell.",
      r"<strong>$Y_n\xrightarrow{P}c$ = the second settles to a number.</strong> It is close to the constant $c$ with chance tending to 1.",
      r"<strong>$X_nY_n\xrightarrow{d}cX$ = rescale the limit.</strong> Multiply the limit law by the constant; likewise dividing by $Y_n$ divides by $c$ (needs $c\ne0$)."],
  conn="<strong>A constant comes along for free.</strong> Say the error in Max's estimated lap time, in seconds, has a limiting bell shape, and the estimate of his speed settles to a constant. Then the error in metres (seconds times speed) has the same bell shape, scaled by that constant.",
  cap='The limit law X of Xₙ and, dashed, the law of cX when Yₙ → c in probability: Xₙ·Yₙ → cX and Xₙ/Yₙ → X/c.'),
31506: dict(d=d6, kind="WORKED EXAMPLE",
  stmt=r"<b>Asymptotic normality of the $t$-statistic.</b> For i.i.d. $X_i$ with mean $\mu$, variance $\sigma^2\in(0,\infty)$ and sample variance $S_n^2$: $\sqrt n(\bar X_n-\mu)/\sigma\xrightarrow{d}\mathcal N(0,1)$ (CLT) and $S_n/\sigma\xrightarrow{P}1$ (LLN), so by Slutsky $T_n=\frac{\sqrt n(\bar X_n-\mu)}{S_n}\xrightarrow{d}\mathcal N(0,1)$ (Grimmett 5.10).",
  hint='If you do not know the spread of the lap-time gap between Max and Checo and use the sample spread, does the bell shape survive?',
  bd=[r"<strong>$\sqrt n(\bar X_n-\mu)/\sigma\xrightarrow{d}\mathcal N(0,1)$ = the numerator.</strong> The standardised average lap-time gap over $n$ laps tends to a standard bell (CLT).",
      r"<strong>$S_n/\sigma\xrightarrow{P}1$ = the denominator.</strong> The sample spread settles to the true spread (law of large numbers).",
      r"<strong>$\mathcal N(0,1)/1$ = Slutsky.</strong> Dividing a bell-shaped limit by a quantity tending to 1 leaves the bell unchanged: the $t$-statistic is asymptotically standard normal."],
  conn='<strong>Not knowing the spread costs nothing.</strong> After enough laps the engineers can replace the true spread of the gap between Max and Checo by the sample spread, and the bell-curve answer for the average gap stays the same.',
  cap='A numerator that tends to the standard bell and a denominator Sₙ/σ that tends to 1. Slutsky divides one by the other: Tₙ → 𝒩(0,1)/1 = 𝒩(0,1).'),
}

STORY = {
31501: dict(s="STORY 15 · STEP 1 · FOUR WAYS TO SETTLE", b="Convergence of random variables has <b>four modes</b> in a fixed hierarchy: a.s. and L^p are strongest, in law is weakest.", f=[["30301", "random variables"], ["30602", "Chebyshev, for in-probability"]], n=[["31502", "partial converses"], ["31701", "laws of large numbers"]]),
31502: dict(s="STORY 15 · STEP 2 · WHEN THE REVERSE HOLDS", b="With a <b>constant limit</b>, law and probability agree, and a <b>subsequence</b> of a probability limit converges a.s.", f=[["31501", "the hierarchy"]], n=[["31503", "why not in general"], ["31605", "proving a.s. via Borel–Cantelli"]]),
31503: dict(s="STORY 15 · STEP 3 · PROBABILITY IS NOT A.S.", b="The <b>sliding typewriter</b>: always shrinking, never settling for any one run.", f=[["31502", "the reverse that does hold"]], n=[["31504", "the other failure"], ["31602", "first Borel–Cantelli to repair it"]]),
31504: dict(s="STORY 15 · STEP 4 · A.S. IS NOT L^p", b="The <b>escaping spike</b>: every run settles, yet the averages blow up.", f=[["31503", "probability vs a.s."]], n=[["31505", "limits in law and their algebra"]]),
31505: dict(s="STORY 15 · STEP 5 · ALGEBRA OF LIMITS", b="<b>Slutsky</b>: sums, products and ratios of an in-law limit with an in-probability constant.", f=[["31501", "modes"]], n=[["31506", "the t-statistic"], ["31803", "CLT"]]),
31506: dict(s="STORY 15 · STEP 6 · NOT KNOWING THE SPREAD", b="The <b>t-statistic</b> is asymptotically normal: Slutsky and the CLT together.", f=[["31505", "Slutsky"]], n=[["31701", "the law of large numbers for the denominator"]]),
}

FIX = build(CARDS)
