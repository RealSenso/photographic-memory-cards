"""StoMA topic 18 (characteristic functions, CLT). F1 picture: Max's total race time as a sum of about 57 laps, standardised; his number of wins out of 100 races."""
from f1_lib import *

SUBJECT = "StoMA"

def d1(c):
    out = circ(70, 64, 40, "#f8fafc", 1) + L(26, 64, 114, 64, .8) + L(70, 20, 70, 108, .8)
    for a in (20, 80, 150, 200, 260, 320):
        r = math.radians(a)
        out += C(70 + 40 * math.cos(r), 64 - 40 * math.sin(r), 2)
    out += C(76, 62, 2.8, "#ffffff", 1.2) + N(84, 58, "φ(t)", 7.5, "start")
    return svg(c, out, N(70, 14, "e^(itX) on the unit circle", 7.5),
        N(130, 40, "φ(t) = 𝔼[e^(itX)]", 8, "start"), N(130, 54, "average of points on the circle,", 7, "start"), N(130, 64, "so it lies inside: |φ| ≤ 1", 7, "start"),
        N(130, 82, "φ(aX + b)(t) = e^(itb) φ(at)", 7, "start"), N(120, 126, "exists for every law, even without a mean", 7.5), N(120, 138, "(each lap time is a point on the circle: a turn by t·time)", 6.5))

def d2(c):
    out = ax(24, 100, 226, 20) + N(226, 112, "t", 7, "end") + N(28, 22, "φₙ(t)", 7.5, "start")
    for k, dsh in [(1.6, "2 3"), (1.2, "4 3"), (1.0, None)]:
        out += fn(lambda x, k=k: 100 - 70 * math.exp(-((x - 124) ** 2) / (2 * (28 * k) ** 2)), 30, 220, 60, 1.1, dsh)
    return svg(c, out, N(124, 112, "0", 7), N(224, 36, "φₙ → φ at every t", 7.5, "end"), N(224, 47, "⇔ Xₙ → X in law", 7.5, "end"),
        N(60, 40, "n small", 7), N(120, 30, "n large", 7) if False else "",
        N(120, 126, "Lévy: pointwise convergence of the Fourier transforms", 7), N(120, 138, "is the same as convergence of the laws", 7))

def d3(c):
    out = ax(24, 108, 226, 20) + N(226, 120, "zₙ: standardised race time", 7, "end")
    for i in range(10):
        x = 52 + i * 14
        h = 44 * math.exp(-((x - 120) ** 2) / 1400) + 4
        out += R(x, 108 - h, 12, h, "#f1f5f9", .9)
    out += fn(lambda x: 108 - 56 * math.exp(-((x - 118) ** 2) / 1400), 40, 200, 60, 1.2)
    return svg(c, out, N(30, 22, "Zₙ = (∑Xᵢ − nμ)/(σ√n) → 𝒩(0,1)", 7.5, "start"),
        N(30, 34, "φ(Zₙ)(t) = (1 − t²/2n + o(t²/n))ⁿ → e^(−t²/2)", 7, "start"), N(170, 70, "any lap-law,", 7, "start"), N(170, 80, "same bell", 7, "start"),
        N(120, 138, "the total of many laps is bell-shaped, whatever one lap looks like", 7))

def d4(c):
    return svg(c, ax(24, 108, 226, 20), N(226, 120, "x", 7, "end"), N(28, 20, "F(x)", 7.5, "start"),
        fn(lambda x: 108 - 80 / (1 + math.exp(-(x - 124) / 18)), 30, 220, 60, 1.1),
        poly([(30, 108), (60, 108), (60, 104), (80, 104), (80, 96), (96, 96), (96, 86), (114, 86), (114, 70), (132, 70), (132, 52), (152, 52), (152, 40), (172, 40), (172, 34), (190, 34), (190, 30), (220, 30)], 1, "3 2") if False else "",
        poly([(30, 108), (84, 108), (84, 100), (100, 100), (100, 88), (114, 88), (114, 70), (130, 70), (130, 52), (144, 52), (144, 40), (160, 40), (160, 32), (190, 32), (190, 29), (220, 29)], 1.0, "3 2"),
        L(114, 70, 114, 108 - 80 / (1 + math.exp(-(114 - 124) / 18)) + 0, 1.2) if False else "",
        N(160, 62, "dashed: the sum's CDF", 7, "start"), N(160, 73, "solid: Φ", 7, "start"),
        N(30, 34, "sup|F − Φ| ≤ 0.4748 𝔼|X − μ|³ / (σ³ √n)", 7, "start"),
        N(120, 128, "ℙ(Sₙ ≤ k) ≈ Φ((k + ½ − nμ)/(σ√n)): half a step more", 7), N(120, 140, "a step function is read at its middle, not its edge", 7))

def d5(c):
    out = ax(24, 100, 226, 20) + N(226, 112, "lap i", 7, "end") + N(28, 22, "σᵢ²", 7.5, "start")
    for i, h in enumerate([18, 22, 16, 24, 20, 18, 22]):
        out += R(40 + i * 24, 100 - h, 16, h, "#f1f5f9", 1)
    return svg(c, out, N(120, 12, "no single lap dominates the total spread", 7.5), N(120, 124, "Lyapunov: ∑𝔼|Xᵢ − μᵢ|^(2+δ) / (∑σᵢ²)^((2+δ)/2) → 0", 6.8),
        N(120, 136, "⇒ (∑(Xᵢ − μᵢ))/√(∑σᵢ²) → 𝒩(0,1)", 7.5), N(190, 46, "balanced laps: bell", 7, "start") if False else N(196, 40, "balanced: bell", 7))

def d6(c):
    import math as m
    out = ax(24, 108, 226, 20) + N(226, 96, "wins S₁₀₀", 7, "end")
    xs = list(range(40, 61))
    for k in xs:
        x = 24 + (k - 30) * 6.6
        p = m.comb(100, k) / 2 ** 100
        h = p * 700
        fill = "#d9dee7" if 45 <= k <= 55 else "#ffffff"
        out += R(x - 3, 108 - h, 6, h, fill, .6)
    out += fn(lambda x: 108 - 700 * (1 / (5 * math.sqrt(2 * math.pi))) * math.exp(-(((x - 24) / 6.6 + 30 - 50) ** 2) / 50), 30, 226, 60, 1.1)
    out += tick(24 + (45 - 30) * 6.6, 108, "44.5") + tick(24 + (55 - 30) * 6.6, 108, "55.5")
    return svg(c, out, N(30, 22, "ℙ(45 ≤ S₁₀₀ ≤ 55)", 7.5, "start"), N(30, 34, "≈ Φ((55.5 − 50)/5) − Φ((44.5 − 50)/5)", 7, "start"),
        N(30, 46, "= 2Φ(1.1) − 1 ≈ 0.7286", 7.5, "start"), N(120, 136, "wins out of 100 races: the bars follow the bell with mean 50, spread 5", 6.5))

CARDS = {
31801: dict(d=d1, kind="DEFINITION",
  stmt=r"<b>Characteristic function.</b> For a random variable $X$, $\varphi_X(t)=\mathbb E[e^{itX}]$, $t\in\mathbb R$. It exists for every $X$, $|\varphi_X(t)|\le1$, $\varphi_X(0)=1$, $\varphi_{aX+b}(t)=e^{itb}\varphi_X(at)$, and it determines the law of $X$; for independent $X,Y$, $\varphi_{X+Y}=\varphi_X\varphi_Y$ (Grimmett 5.7; Durrett 3.3).",
  hint='Which transform of a lap-time law always exists, even for laws with no mean?',
  bd=['<strong>$e^{itX}$ = a point on the unit circle.</strong> Each lap time $X$ becomes an angle $tX$ and a point on a circle of radius 1.',
      r"<strong>$\varphi_X(t)=\mathbb E[e^{itX}]$ = the average of those points.</strong> An average of points on the circle lies inside it, so $|\varphi_X(t)|\le1$ and it always exists.",
      r"<strong>$\varphi_{aX+b}(t)=e^{itb}\varphi_X(at)$ and $\varphi_{X+Y}=\varphi_X\varphi_Y$.</strong> Shifts rotate, scalings stretch $t$, and independent sums multiply; this is the Fourier dual of the law."],
  conn="<strong>Wrapping the lap time around a circle.</strong> Each possible lap time becomes a direction on a circle. The average direction, over all of Max's laps, is a point inside the circle that encodes the whole law of his lap time.",
  cap='Samples of e^(itX) are points on the unit circle. Their average φ(t) = 𝔼[e^(itX)] lies inside the circle, so |φ| ≤ 1 always; it encodes the whole law.'),
31802: dict(d=d2, kind="THEOREM",
  stmt=r"<b>Lévy's continuity theorem.</b> $X_n\xrightarrow{d}X$ if and only if $\varphi_{X_n}(t)\to\varphi_X(t)$ for every $t\in\mathbb R$. More generally, if $\varphi_{X_n}(t)\to\varphi(t)$ pointwise and $\varphi$ is continuous at $0$, then $\varphi$ is the characteristic function of some $X$ and $X_n\xrightarrow{d}X$ (Grimmett 5.9; Durrett 3.3).",
  hint='How can you check that a sequence of laws settles by looking at their transforms only?',
  bd=[r"<strong>$\varphi_{X_n}(t)$ = the transform of the $n$-th law.</strong> One function of $t$ for each $n$.",
      r"<strong>$\lim\varphi_{X_n}(t)=\varphi_X(t)$ for every $t$ = pointwise convergence.</strong> At each fixed frequency $t$, the values settle on those of the limit.",
      r"<strong>$\iff X_n\xrightarrow{d}X$ = it is the same statement.</strong> Convergence of the transforms is equivalent to convergence of the laws, and continuity at 0 guarantees a limit law exists."],
  conn="<strong>Judging the shape by its fingerprint.</strong> Instead of watching the histogram of Max's total race time change with the number of laps $n$, you watch its transform at each frequency; when every frequency has settled, the shape has settled.",
  cap='Characteristic functions φₙ(t) for increasing n converging pointwise to φ(t). Pointwise convergence of φₙ at every t is equivalent to Xₙ → X in distribution.'),
31803: dict(d=d3, kind="THEOREM",
  stmt=r"<b>Central limit theorem (Lindeberg–Lévy).</b> Let $X_1,X_2,\ldots$ be i.i.d. with mean $\mu$ and variance $\sigma^2\in(0,\infty)$. Then $Z_n=\dfrac{\sum_{i=1}^nX_i-n\mu}{\sigma\sqrt n}\xrightarrow{d}\mathcal N(0,1)$. Proof: $\varphi_{Z_n}(t)=\bigl(1-\frac{t^2}{2n}+o(\frac{t^2}n)\bigr)^n\to e^{-t^2/2}$, then Lévy (Ross 8.3; Grimmett 5.10).",
  hint='Why does the total of many independent laps look like a bell, whatever one lap looks like?',
  bd=[r"<strong>$\sum X_i-n\mu$ = the total, centred.</strong> Subtract the expected race time, so the leftover has mean 0.",
      r"<strong>$\div\,\sigma\sqrt n$ = rescale by the spread.</strong> The total has standard deviation $\sigma\sqrt n$; dividing by it gives a variable with variance 1.",
      r"<strong>$\bigl(1-\frac{t^2}{2n}+o\bigr)^n\to e^{-t^2/2}$ = the transform of a bell.</strong> Only the mean and variance survive the $n$-th power; the limit is the standard normal's transform."],
  conn="<strong>A whole race is a bell.</strong> Whatever shape one lap time has (a few slow laps in traffic make it lopsided), Max's total time over 57 laps, measured in standard units, has a bell-shaped histogram. Only the average and the spread of one lap matter.",
  cap='Histogram of the standardised race time Zₙ and the standard bell 𝒩(0,1). The transform (1 − t²/2n + o(t²/n))ⁿ tends to e^(−t²/2), which proves it.'),
31804: dict(d=d4, kind="THEOREM",
  stmt=r"<b>Berry–Esseen theorem.</b> For i.i.d. $X_i$ with $\mathbb E|X-\mu|^3<\infty$, $\sup_x|F_{Z_n}(x)-\Phi(x)|\le\dfrac{C\,\mathbb E|X-\mu|^3}{\sigma^3\sqrt n}$ with $C\le0.4748$. For integer-valued sums, the continuity correction $\mathbb P(S_n\le k)\approx\Phi\!\left(\frac{k+\frac12-n\mu}{\sigma\sqrt n}\right)$ is more accurate (Grimmett 5.10; Ross 8.3).",
  hint="How far from a perfect bell is a sum of n terms, like Max's wins in a season, and how do you handle that counts come in whole numbers?",
  bd=[r"<strong>$\sup_x|F_{Z_n}(x)-\Phi(x)|$ = the largest gap between CDFs.</strong> The worst disagreement, anywhere, between the standardised total and the bell.",
      r"<strong>$\frac{C\,\mathbb E|X-\mu|^3}{\sigma^3\sqrt n}$ = it shrinks like $1/\sqrt n$.</strong> The skewness of one term sets the constant; more races make the bell fit better.",
      r"<strong>$k+\frac12$ = the continuity correction.</strong> A whole-number total has a CDF that is a staircase; evaluating the bell half a step further reads it at the middle of the step."],
  conn="<strong>How good is the bell for one season?</strong> Max's number of wins in a 24-race season is a whole-number count. A lopsided win chance needs more races before the count looks like a bell. And to ask for “at most 15 wins”, ask the bell up to 15.5.",
  cap='The staircase CDF of the win count (dashed) and the smooth bell CDF Φ. The largest gap is at most 0.4748 𝔼|X−μ|³/(σ³√n), and reading the bell at k + ½ matches the middle of a step.'),
31805: dict(d=d5, kind="THEOREM",
  stmt=r"<b>Lyapunov and Lindeberg CLT.</b> Let $X_i$ be independent with means $\mu_i$, variances $\sigma_i^2$ and $s_n^2=\sum_{i\le n}\sigma_i^2$. If for some $\delta>0$ (Lyapunov) $\frac1{s_n^{2+\delta}}\sum_{i\le n}\mathbb E|X_i-\mu_i|^{2+\delta}\to0$, then $\frac1{s_n}\sum_{i\le n}(X_i-\mu_i)\xrightarrow{d}\mathcal N(0,1)$. Lindeberg's condition $\frac1{s_n^2}\sum\mathbb E[(X_i-\mu_i)^2\mathbf 1_{\{|X_i-\mu_i|>\varepsilon s_n\}}]\to0$ is weaker and, with $\max_i\sigma_i/s_n\to0$, necessary (Grimmett 5.10; Durrett 3.4).",
  hint='If the laps are not identical, what stops a single one from spoiling the bell?',
  bd=[r"<strong>$s_n^2=\sum\sigma_i^2$ = the total variance.</strong> The sum of every lap's variance.",
      r"<strong>$\sum\mathbb E|X_i-\mu_i|^{2+\delta}\big/s_n^{2+\delta}\to0$ = no lap dominates.</strong> The (2+δ)-th moments are small compared with the total spread, so no single big jump drives the sum.",
      r"<strong>Lindeberg = the weaker, sharper version.</strong> Only the tails beyond $\varepsilon s_n$ are required to contribute nothing in the limit; Lyapunov implies Lindeberg."],
  conn='<strong>Many different laps.</strong> A race is made of different laps (the start, laps on fresh and on worn tyres, the pit-stop lap, laps behind the safety car), each with its own spread. It still adds up to a bell, as long as no single lap is so big or so wild that it dominates the total.',
  cap='Variances σᵢ² of seven different laps. If they are balanced and no lap dominates, the Lyapunov ratio tends to 0 and the standardised total is asymptotically 𝒩(0,1).'),
31806: dict(d=d6, kind="WORKED EXAMPLE",
  stmt=r"<b>De Moivre–Laplace.</b> Let $S_{100}$ be the number of heads in $100$ fair tosses, so $\mu=50$, $\sigma=5$. With the continuity correction, $\mathbb P(45\le S_{100}\le55)\approx\Phi\!\left(\frac{55.5-50}{5}\right)-\Phi\!\left(\frac{44.5-50}{5}\right)=2\Phi(1.1)-1\approx0.7286$ (Ross 8.3; Grimmett 5.10).",
  hint='If Max wins each of 100 independent races with chance ½, how likely is it that he wins between 45 and 55 of them?',
  bd=[r"<strong>$\mu=50,\ \sigma=\sqrt{100\cdot\frac14}=5$ = centre and spread.</strong> The count of wins has mean $np$ and standard deviation $\sqrt{np(1-p)}$.",
      r"<strong>$44.5$ and $55.5$ = the continuity correction.</strong> The whole numbers $45,\ldots,55$ cover the interval from $44.5$ to $55.5$, so these are the bell's cut-offs.",
      r"<strong>$2\Phi(1.1)-1\approx0.7286$ = a symmetric interval.</strong> $\frac{55.5-50}5=1.1$ and $\frac{44.5-50}5=-1.1$, so the answer is $\Phi(1.1)-\Phi(-1.1)$."],
  conn='<strong>About half the races won.</strong> If Max wins each race with chance ½, then over 100 races he wins between 45 and 55 of them about 73% of the time. The bars of the exact counts follow the bell of mean 50 and spread 5.',
  cap='Exact binomial bars for the number of wins in 100 races, with the bell of mean 50 and spread 5. The shaded bars 45 to 55 are cut at 44.5 and 55.5, giving ≈ 0.7286.'),
}

STORY = {
31801: dict(s="STORY 18 · STEP 1 · A TRANSFORM THAT ALWAYS EXISTS", b="The <b>characteristic function</b> is the average of points on a circle: it exists for every law and multiplies over independent sums.", f=[["30504", "the MGF, which may not exist"], ["30905", "sums of independent variables"]], n=[["31802", "convergence through transforms"], ["31706", "the Cauchy case used it"]]),
31802: dict(s="STORY 18 · STEP 2 · SETTLING VIA TRANSFORMS", b="<b>Lévy</b>: laws converge exactly when their transforms converge pointwise.", f=[["31801", "characteristic function"], ["31501", "convergence in distribution"]], n=[["31803", "the central limit theorem"]]),
31803: dict(s="STORY 18 · STEP 3 · THE BELL", b='The <b>CLT</b>: the standardised total of many independent laps tends to the bell, whatever one lap looks like.', f=[["31802", "Lévy continuity"], ["31701", "law of large numbers"], ["30305", "the bell curve"]], n=[['31804',
      'how fast'],
      ['31805',
      'non-identical laps']]),
31804: dict(s="STORY 18 · STEP 4 · HOW FAST", b="<b>Berry–Esseen</b>: the gap to the bell shrinks like 1/√n; use a continuity correction for counts.", f=[["31803", "the CLT"]], n=[["31806", "a worked example"]]),
31805: dict(s='STORY 18 · STEP 5 · DIFFERENT LAPS', b='The CLT holds for non-identical laps as long as <b>no lap dominates</b> (Lyapunov, Lindeberg).', f=[["31803", "the CLT"]], n=[["32502", "Brownian motion as the limit of random walks"]]),
31806: dict(s="STORY 18 · STEP 6 · A COUNT", b='<b>De Moivre–Laplace</b>: the bell approximates the count of wins among 100 races.', f=[["31804", "continuity correction"]], n=[['31901',
      'chains of dependent races']]),
}

FIX = build(CARDS)
