"""StoMA gap cards found by the coverage audit against the practice questions and PYQs:
4.07 lognormal, 5.07 indicator method, 9.07 Beta-Gamma / chi-square / t / F, 23.07 cross-spectra & Wiener filter,
23.08 random telegraph signal, 24.07-24.08 renewal theory, 25.07 Brownian motion with drift & geometric BM,
27.07 Little's law, PASTA & other queues.
Run from the repo root:  python3 scripts/build_stoma_gap_cards.py"""
import math, os, random, sys
sys.path.insert(0, os.path.dirname(__file__))
from stoma_cardkit import T, N, L, V, P, C, R, AX, box, ln, stmt, curve, make, write_cards, write_story

cards = []
card = lambda topic, k, *a: cards.append(make(topic, k, *a))

# ---------- 4.07 Lognormal ----------
mu, sg = 0.0, 0.6
f_ln = lambda y: 0 if y <= 0 else math.exp(-(math.log(y) - mu) ** 2 / (2 * sg * sg)) / (y * sg * math.sqrt(2 * math.pi))
x0, base, sx, sy = 26, 112, 70, 120
xs = lambda y: x0 + y * sx
mode, med, mean = math.exp(mu - sg ** 2), math.exp(mu), math.exp(mu + sg ** 2 / 2)
card(4, 7, "CANONICAL CONTINUOUS", "Lognormal: The Exponential of a Gaussian",
     [AX(22, base, 228, 12),
      P(curve(f_ln, 0.001, 2.85, x0, base, sx, sy, 90), w=1.8),
      L(xs(mode), base, xs(mode), base - f_ln(mode) * sy, 0.9, d="2 2"),
      L(xs(med), base, xs(med), base - f_ln(med) * sy, 1, d="4 3"),
      L(xs(mean), base, xs(mean), base - f_ln(mean) * sy - 14, 1.2),
      N(xs(mode) - 1, base + 9, "mode", 6.3, a="end"), N(xs(med) + 1, base + 9, "median", 6.3, a="start"),
      N(xs(mean) + 3, base - f_ln(mean) * sy - 16, "mean e^(μ+σ²/2)", 6.6, a="start"),
      N(150, 48, "long right tail:", 6.8, a="start"), N(150, 57, "mode < median < mean", 6.8, a="start"),
      N(150, 66, "median = e^μ", 6.8, a="start"), N(150, 75, "ln Y ~ 𝒩(μ, σ²)", 6.8, a="start"),
      T(26, 18, "f(y)", 7.5, a="start"),
      T(228, 134, "y = Max's pace advantage factor, μ = 0, σ = 0.6", 7, a="end")],
     "The lognormal density of Y = e^X with X ~ 𝒩(0, 0.36). It is skewed to the right: the mode, median and mean are in that order, "
     "and the mean e^(μ+σ²/2) is pulled up by the long tail.",
     ["<strong>Definition:</strong> $Y=e^X$ with $X\\sim\\mathcal N(\\mu,\\sigma^2)$; then $\\ln Y\\sim\\mathcal N(\\mu,\\sigma^2)$ and $Y\\gt0$.",
      "<strong>CDF and density:</strong> $F_Y(y)=\\Phi\\!\\left(\\frac{\\ln y-\\mu}\\sigma\\right)$ and $f_Y(y)=\\frac1{y\\sigma\\sqrt{2\\pi}}e^{-(\\ln y-\\mu)^2/2\\sigma^2}$ for $y\\gt0$.",
      "<strong>Moments:</strong> $\\mathbb E[Y^k]=M_X(k)=e^{k\\mu+k^2\\sigma^2/2}$, so $\\mathbb E[Y]=e^{\\mu+\\sigma^2/2}$ and $\\operatorname{Var}(Y)=(e^{\\sigma^2}-1)e^{2\\mu+\\sigma^2}$."],
     "$$f_Y(y)=\\frac{1}{y\\sigma\\sqrt{2\\pi}}e^{-(\\ln y-\\mu)^2/2\\sigma^2},\\qquad \\mathbb E[Y^k]=e^{k\\mu+k^2\\sigma^2/2}$$",
     "<strong>Gains that multiply.</strong> Over a season, each upgrade changes Red Bull's pace advantage by a random percentage. "
     "Percentages multiply, so the log of the final advantage is a sum of many small pieces, roughly normal. The advantage itself "
     "is lognormal: usually modest, now and then huge, with the mean above the median.",
     "E[e^X] ≠ e^(E[X]): the mean is e^(μ+σ²/2), not e^μ (Jensen). Also, all moments exist but the MGF of Y does not: "
     "E[e^(sY)] = ∞ for every s > 0.",
     "THEOREM",
     stmt("Lognormal distribution.",
          [ln("If $X\\sim\\mathcal N(\\mu,\\sigma^2)$, then $Y=e^X$ is lognormal with"),
           ln("$F_Y(y)=\\Phi\\!\\left(\\dfrac{\\ln y-\\mu}\\sigma\\right)$ and $f_Y(y)=\\dfrac1{y\\sigma\\sqrt{2\\pi}}e^{-(\\ln y-\\mu)^2/2\\sigma^2}$ for $y\\gt0$.", True),
           ln("Its moments come from the Gaussian MGF:"),
           ln("$\\mathbb E[Y^k]=e^{k\\mu+k^2\\sigma^2/2}$, so $\\mathbb E[Y]=e^{\\mu+\\sigma^2/2}$ while the median is $e^\\mu$.", True)],
          "Ross 5.7; Grimmett 4.7"),
     "If the log of Max's pace advantage is normal, what is the law of the advantage itself, and what is its mean?",
     ["<strong>$Y=e^X$ = undo the log.</strong> $Y\\le y$ exactly when $X\\le\\ln y$, so $F_Y(y)=\\Phi((\\ln y-\\mu)/\\sigma)$; differentiating gives the extra $1/y$.",
      "<strong>$\\mathbb E[Y^k]=M_X(k)$ = moments for free.</strong> $\\mathbb E[e^{kX}]$ is the Gaussian MGF at $s=k$: $e^{k\\mu+k^2\\sigma^2/2}$.",
      "<strong>Median $e^\\mu$ \\lt mean $e^{\\mu+\\sigma^2/2}$ = the tail pulls the mean up.</strong> The log is symmetric about $\\mu$, but exponentiating stretches the right side."])

# ---------- 5.07 Indicator method ----------
grid = [1, 2, 3, 4, 5, 6, 7, 8]
fin = [3, 2, 7, 4, 1, 6, 8, 5]
cx0, dx = 58, 21
parts = [N(30, 30, "grid", 7, a="end"), N(30, 52, "finish", 7, a="end"), N(30, 78, "1{Aᵢ}", 7, a="end")]
for i, (g, f) in enumerate(zip(grid, fin)):
    x = cx0 + i * dx
    hit = g == f
    parts += [R(x - 8, 20, 16, 14, "#f1f5f9", 1), N(x, 30, str(g), 7.5),
              R(x - 8, 42, 16, 14, "#ffffff" if not hit else "#cbd5e1", 1.2 if hit else 1), N(x, 52, str(f), 7.5, w="bold" if hit else "normal"),
              N(x, 78, "1" if hit else "0", 8, w="bold" if hit else "normal")]
parts += [L(cx0 - 10, 86, cx0 + 7 * dx + 10, 86, 1),
          N(cx0 + 7 * dx + 14, 80, "X = 3", 8, a="start", w="bold"),
          N(120, 104, "E[X] = Σ ℙ(Aᵢ) = n · (1/n) = 1", 7.5),
          N(120, 116, "no independence needed", 6.8),
          T(228, 134, "Aᵢ = driver i finishes where they started", 7, a="end")]
card(5, 7, "COUNTING TECHNIQUE", "The Indicator Method: Count with Sums of 0s and 1s",
     parts,
     "A random finishing order for 8 drivers. Each driver gets a 1 if they finish in their grid slot and a 0 otherwise; X is the sum "
     "of the indicators, so E[X] is the sum of their chances, here 8 × 1/8 = 1.",
     ["<strong>Write the count as a sum:</strong> $X=\\sum_i\\mathbf 1_{A_i}$, then $\\mathbb E[X]=\\sum_i\\mathbb P(A_i)$ by linearity, with no independence needed.",
      "<strong>Variance from pairs:</strong> $\\operatorname{Var}(X)=\\sum_i\\mathbb P(A_i)(1-\\mathbb P(A_i))+2\\sum_{i\\lt j}\\bigl(\\mathbb P(A_i\\cap A_j)-\\mathbb P(A_i)\\mathbb P(A_j)\\bigr)$.",
      "<strong>Classics:</strong> matches in a random permutation have mean 1 and variance 1; the coupon collector needs $n\\sum_{k=1}^n\\frac1k\\approx n\\ln n$ draws on average."],
     "$$\\mathbb E\\Big[\\sum_i\\mathbf 1_{A_i}\\Big]=\\sum_i\\mathbb P(A_i),\\qquad \\operatorname{Cov}(\\mathbf 1_{A_i},\\mathbf 1_{A_j})=\\mathbb P(A_i\\cap A_j)-\\mathbb P(A_i)\\mathbb P(A_j)$$",
     "<strong>Finishing where you started.</strong> Shuffle the 20 drivers into a random finishing order. Each driver finishes in their "
     "grid slot with chance 1/20, so on average exactly 1 driver does, whatever the field size. Pairs: $\\mathbb P(\\text{both } i,j)=\\frac1{20\\cdot19}$, "
     "which makes the variance 1 as well.",
     "Trying to find the full distribution of X first when only E[X] is asked: indicators avoid it. For the variance, dropping the "
     "covariance terms is wrong whenever the events depend on each other (matches, sampling without replacement).",
     "THEOREM",
     stmt("The indicator method.",
          [ln("If $X=\\sum_{i=1}^n\\mathbf 1_{A_i}$ counts how many of the events $A_i$ happen, then"),
           ln("$\\mathbb E[X]=\\sum_i\\mathbb P(A_i)$ for any events, dependent or not, and", True),
           ln("$\\operatorname{Var}(X)=\\sum_i\\mathbb P(A_i)\\bigl(1-\\mathbb P(A_i)\\bigr)+2\\sum_{i\\lt j}\\bigl(\\mathbb P(A_i\\cap A_j)-\\mathbb P(A_i)\\mathbb P(A_j)\\bigr)$.", True),
           ln("Example: the number of fixed points of a random permutation of $n$ has mean 1 and variance 1.")],
          "Ross 7.2, 7.4"),
     "In a random finishing order of 20 drivers, how many finish exactly where they started on the grid, on average?",
     ["<strong>$X=\\sum_i\\mathbf 1_{A_i}$ = count with switches.</strong> One 0/1 switch per driver, per pair, per coupon: the count is their sum.",
      "<strong>$\\mathbb E[X]=\\sum_i\\mathbb P(A_i)$ = add the chances.</strong> Linearity works even though the drivers' events depend on each other.",
      "<strong>$\\operatorname{Var}$ needs pairs.</strong> $\\mathbb E[X^2]$ brings in $\\mathbb P(A_i\\cap A_j)$ for every pair, so the covariances decide the spread."])

# ---------- 9.07 Beta-Gamma algebra, chi-square, t, F ----------
c3 = math.gamma(2) / (math.sqrt(3 * math.pi) * math.gamma(1.5))
t3 = lambda x: c3 * (1 + x * x / 3) ** -2
nz = lambda x: math.exp(-x * x / 2) / math.sqrt(2 * math.pi)
x0, base, sx, sy = 125, 112, 22, 210
card(9, 7, "SAMPLING DISTRIBUTIONS", "Beta–Gamma Algebra & the χ², t and F Family",
     [L(22, base, 228, base, 1.2, ar=True), L(x0, base, x0, 14, 0.8, d="2 2"),
      P(curve(nz, -4.6, 4.6, x0 - 4.6 * sx, base, sx, sy, 80), w=1.3, dash="4 3"),
      P(curve(t3, -4.6, 4.6, x0 - 4.6 * sx, base, sx, sy, 80), w=2),
      N(x0 + 2 * sx + 4, base - nz(1.2) * sy - 8, "𝒩(0,1)", 7, a="start"),
      N(x0 + 2.6 * sx, base - t3(2.6) * sy - 8, "t₃: heavier tails", 7, a="start", w="bold"),
      N(28, 24, "(X̄ − μ) / (S/√n) ~ tₙ₋₁", 7, a="start"),
      N(28, 34, "(n − 1)S²/σ² ~ χ²ₙ₋₁", 7, a="start"),
      N(28, 44, "X/(X+Y) ~ Beta(α, β)", 7, a="start"),
      N(x0, base + 9, "0", 6.8),
      T(228, 134, "standardised mean of 4 laps, σ unknown", 7, a="end")],
     "The t density with 3 degrees of freedom (solid) against the standard normal (dashed). Estimating σ from only a few laps adds "
     "uncertainty, so the t curve is lower in the middle and heavier in the tails.",
     ["<strong>Beta–Gamma:</strong> for independent $X\\sim\\mathrm{Gamma}(\\alpha,\\lambda)$, $Y\\sim\\mathrm{Gamma}(\\beta,\\lambda)$: $X+Y\\sim\\mathrm{Gamma}(\\alpha+\\beta,\\lambda)$ and $\\frac X{X+Y}\\sim\\mathrm{Beta}(\\alpha,\\beta)$, independent of $X+Y$.",
      "<strong>The normal family:</strong> $\\chi^2_n=Z_1^2+\\dots+Z_n^2=\\mathrm{Gamma}(\\frac n2,\\frac12)$; $t_n=\\frac Z{\\sqrt{V/n}}$ and $F_{m,n}=\\frac{U/m}{V/n}$ with independent $\\chi^2$ parts; $t_n^2\\sim F_{1,n}$.",
      "<strong>Gaussian samples:</strong> $\\bar X$ and $S^2$ are independent, $\\frac{(n-1)S^2}{\\sigma^2}\\sim\\chi^2_{n-1}$ and $\\frac{\\bar X-\\mu}{S/\\sqrt n}\\sim t_{n-1}$."],
     "$$\\frac{X}{X+Y}\\sim\\mathrm{Beta}(\\alpha,\\beta)\\perp X+Y,\\qquad \\frac{\\bar X-\\mu}{S/\\sqrt n}\\sim t_{n-1},\\qquad \\frac{(n-1)S^2}{\\sigma^2}\\sim\\chi^2_{n-1}$$",
     "<strong>Is the new floor faster?</strong> Red Bull runs 4 laps with the new floor. The lap-time spread σ is unknown, so the "
     "engineers divide the mean gain by the spread measured from those same 4 laps. That ratio is $t_3$, not normal: with so few laps "
     "a big-looking gain can still be luck.",
     "Using n instead of n − 1: one degree of freedom goes into estimating the mean, so (n − 1)S²/σ² ~ χ²ₙ₋₁. And X̄ ⟂ S² holds "
     "only for Gaussian samples, not in general.",
     "THEOREM",
     stmt("Beta–Gamma algebra and the normal sampling family.",
          [ln("If $X\\sim\\mathrm{Gamma}(\\alpha,\\lambda)$ and $Y\\sim\\mathrm{Gamma}(\\beta,\\lambda)$ are independent, then"),
           ln("$X+Y\\sim\\mathrm{Gamma}(\\alpha+\\beta,\\lambda)$ and $\\dfrac X{X+Y}\\sim\\mathrm{Beta}(\\alpha,\\beta)$ are independent.", True),
           ln("If $X_1,\\dots,X_n$ are i.i.d. $\\mathcal N(\\mu,\\sigma^2)$ with sample mean $\\bar X$ and sample variance $S^2$, then"),
           ln("$\\bar X\\perp S^2$, $\\dfrac{(n-1)S^2}{\\sigma^2}\\sim\\chi^2_{n-1}$ and $\\dfrac{\\bar X-\\mu}{S/\\sqrt n}\\sim t_{n-1}$.", True)],
          "Casella & Berger 4.6, 5.3"),
     "With only 4 laps on the new floor and σ unknown, how do you judge whether the mean improvement is real?",
     ["<strong>$X/(X+Y)\\sim\\mathrm{Beta}$ = shares ignore the total.</strong> Split a Gamma total into Gamma parts: the share is Beta and tells you nothing about the total (change variables $(X,Y)\\to(X+Y,\\frac X{X+Y})$).",
      "<strong>$\\chi^2_n=\\sum Z_i^2$ = squared normal noise.</strong> It is $\\mathrm{Gamma}(\\frac n2,\\frac12)$; dividing a normal by the root of an independent $\\chi^2_n/n$ gives $t_n$, and a ratio of two scaled $\\chi^2$s gives $F$.",
      "<strong>$t_{n-1}$ = standardise with the estimated spread.</strong> Replacing $\\sigma$ by $S$ fattens the tails; as $n\\to\\infty$, $t_{n-1}\\to\\mathcal N(0,1)$."])

# ---------- 23.07 Cross-correlation, cross-spectrum, Wiener filter ----------
x0, base, sx, sy = 26, 112, 20, 85
Ss = lambda w: 1 / (1 + w * w)
Sn = 0.25
Hw = lambda w: Ss(w) / (Ss(w) + Sn)
card(23, 7, "CROSS-SPECTRA", "Cross-Correlation, Cross-Spectrum & the Wiener Filter",
     [AX(22, base, 228, 12),
      P(curve(Ss, 0, 10, x0, base, sx, sy, 80), w=1.4),
      L(x0, base - Sn * sy, x0 + 10 * sx, base - Sn * sy, 1.2, d="4 3"),
      P(curve(Hw, 0, 10, x0, base, sx, sy, 80), w=2.2),
      L(132, 22, 146, 22, 2.2), N(150, 25, "gain H = signal/(signal + noise)", 6.6, a="start", w="bold"),
      L(132, 33, 146, 33, 1.4), N(150, 36, "signal power", 6.6, a="start"),
      L(132, 44, 146, 44, 1.2, d="4 3"), N(150, 47, "noise power (flat)", 6.6, a="start"),
      N(132, 64, "keep ω where the signal", 6.8, a="start"), N(132, 73, "is stronger than the noise", 6.8, a="start"),
      T(26, 18, "power, gain", 7.5, a="start"),
      T(228, 134, "ω (frequency)", 7, a="end")],
     "The Wiener filter for a radio message S buried in flat noise N. Its gain H(ω) = S_S/(S_S + S_N) is close to 1 where the "
     "message is strong (low frequencies) and falls towards 0 where noise dominates.",
     ["<strong>Cross-correlation:</strong> for jointly WSS $X,Y$, $R_{YX}(\\tau)=\\mathbb E[Y(t+\\tau)X(t)]$, with $R_{XY}(\\tau)=R_{YX}(-\\tau)$; its transform is the cross-spectrum $S_{YX}(\\omega)$, complex in general.",
      "<strong>Through a filter:</strong> if $Y=h*X$, then $R_{YX}=h*R_X$ and $S_{YX}(\\omega)=H(\\omega)S_X(\\omega)$, so $H=S_{YX}/S_X$ keeps the phase that $|H|^2$ loses.",
      "<strong>Wiener filter:</strong> to estimate $S(t)$ from $X=S+N$ with $S,N$ uncorrelated, the best linear (non-causal) filter is $H(\\omega)=\\frac{S_S(\\omega)}{S_S(\\omega)+S_N(\\omega)}$."],
     "$$S_{YX}(\\omega)=H(\\omega)S_X(\\omega),\\qquad S_Y(\\omega)=|H(\\omega)|^2S_X(\\omega),\\qquad H_{\\text{opt}}(\\omega)=\\frac{S_S(\\omega)}{S_S(\\omega)+S_N(\\omega)}$$",
     "<strong>Reading the car from telemetry.</strong> Engineers log Max's steering input $X$ and the car's yaw rate $Y$. Dividing the "
     "cross-spectrum by the steering spectrum, $S_{YX}/S_X$, gives the car's response $H(\\omega)$ at each frequency, delay included. "
     "The same algebra cleans his team radio: keep the frequencies where his voice beats the engine noise.",
     "Cross-correlation is not symmetric: R_XY(τ) = R_YX(−τ), and S_XY = S_YX* (complex conjugate). Using S_Y = |H|²S_X to find H "
     "loses the phase; the cross-spectrum keeps it.",
     "THEOREM",
     stmt("Cross-spectra and the Wiener filter.",
          [ln("Let $X(t)$ be WSS and $Y=h*X$ for a stable LTI filter $H(\\omega)$. Then $X,Y$ are jointly WSS with"),
           ln("$R_{YX}(\\tau)=(h*R_X)(\\tau)$ and $S_{YX}(\\omega)=H(\\omega)S_X(\\omega)$.", True),
           ln("If $X=S+N$ with $S,N$ uncorrelated, zero-mean and WSS, the linear filter minimising $\\mathbb E[(S(t)-\\hat S(t))^2]$ is"),
           ln("$H(\\omega)=\\dfrac{S_S(\\omega)}{S_S(\\omega)+S_N(\\omega)}$.", True)],
          "Papoulis 10, 13"),
     "How can engineers read the car's response H(ω) from logged steering input and yaw rate?",
     ["<strong>$R_{YX}=h*R_X$ = the output remembers the input through $h$.</strong> Correlating $Y(t+\\tau)$ with $X(t)$ smears the input's correlation by the impulse response.",
      "<strong>$S_{YX}=HS_X$ = divide to identify the system.</strong> $H=S_{YX}/S_X$ gives gain and phase; $S_Y=|H|^2S_X$ gives only the gain.",
      "<strong>$S_S/(S_S+S_N)$ = trust each frequency by its signal share.</strong> It is the scalar LLSE weight $\\frac{\\sigma_S^2}{\\sigma_S^2+\\sigma_N^2}$ applied frequency by frequency."])

# ---------- 23.08 Worked benchmark: random telegraph signal ----------
ts = [1.1, 2.6, 3.4, 5.0, 6.5, 7.2, 8.4]   # swap times (a Poisson-looking sample, picked to be easy to redraw)
x0, sx, yh, yl = 26, 21, 40, 84
d, s, xprev, lvl = "", 1, 0, yh
d = f"M {x0} {yh}"
for tt in ts:
    xx = x0 + tt * sx
    d += f" L {xx:.1f} {lvl} "
    lvl = yl if lvl == yh else yh
    d += f"L {xx:.1f} {lvl}"
d += f" L {x0 + 9.2 * sx:.1f} {lvl}"
card(23, 8, "WORKED BENCHMARK", "Worked Benchmark: The Random Telegraph Signal",
     [L(22, 62, 228, 62, 1, ar=True), L(x0, 104, x0, 20, 1, ar=True),
      P(d, w=1.8),
      "".join(C(x0 + tt * sx, 62, 1.6) for tt in ts),
      N(x0 - 3, yh + 3, "+1", 7, a="end"), N(x0 - 3, yl + 3, "−1", 7, a="end"),
      N(x0 + 4, 28, "+1 = Max leads, −1 = Lando leads", 6.8, a="start"),
      N(x0 + 4, 100, "dots: swaps at Poisson(λ) times", 6.8, a="start"),
      N(226, 100, "R(τ) = e^(−2λ|τ|)", 7.5, a="end", w="bold"),
      T(228, 134, "t (minutes)", 7, a="end")],
     "The leader flips between Max (+1) and Lando (−1) at the times of a Poisson process (dots). Two moments τ apart agree when an "
     "even number of swaps falls between them, which makes the correlation e^(−2λ|τ|).",
     ["<strong>Model:</strong> $X(t)=X(0)(-1)^{N(t)}$ with $N$ a Poisson process of rate $\\lambda$ and $X(0)=\\pm1$ with chance $\\frac12$ each, independent of $N$.",
      "<strong>Key step:</strong> $\\mathbb E[(-1)^{N(\\tau)}]=\\sum_k e^{-\\lambda\\tau}\\frac{(-\\lambda\\tau)^k}{k!}=e^{-2\\lambda\\tau}$ for $\\tau\\ge0$.",
      "<strong>Result:</strong> $\\mathbb E[X(t)]=0$, $R_X(\\tau)=e^{-2\\lambda|\\tau|}$, so $X$ is WSS with $S_X(\\omega)=\\frac{4\\lambda}{4\\lambda^2+\\omega^2}$."],
     "$$R_X(\\tau)=\\mathbb E\\big[X(t)X(t+\\tau)\\big]=\\mathbb E\\big[(-1)^{N(t+\\tau)-N(t)}\\big]=e^{-\\lambda\\tau}\\sum_{k\\ge0}\\frac{(-\\lambda\\tau)^k}{k!}=e^{-2\\lambda\\tau}$$",
     "<strong>The fight for the lead.</strong> Max and Lando swap the lead whenever something random happens (a mistake, a slow stop, "
     "a safety car), at about $\\lambda=0.5$ times a minute. The chance the same driver leads at two moments $\\tau$ minutes apart "
     "is $\\frac12(1+e^{-\\tau})$: after a few minutes, knowing today's leader says almost nothing.",
     "Without the random start X(0) = ±1, the mean is X(0)e^(−2λt), which depends on t, so the process is not WSS. And the decay "
     "rate is 2λ, not λ: each swap flips the sign, so (−1)^N averages to e^(−2λτ).",
     "WORKED EXAMPLE",
     stmt("The random telegraph signal.",
          [ln("Let $N(t)$ be a Poisson process of rate $\\lambda$ and $X(0)=\\pm1$ with chance $\\frac12$ each, independent of $N$."),
           ln("Set $X(t)=X(0)(-1)^{N(t)}$. Then $\\mathbb E[X(t)]=0$ and, for $\\tau\\ge0$,"),
           ln("$\\mathbb E[X(t)X(t+\\tau)]=\\mathbb E[(-1)^{N(t+\\tau)-N(t)}]=\\displaystyle\\sum_{k\\ge0}e^{-\\lambda\\tau}\\frac{(-\\lambda\\tau)^k}{k!}=e^{-2\\lambda\\tau}$.", True),
           ln("So $X$ is WSS with $R_X(\\tau)=e^{-2\\lambda|\\tau|}$ and $S_X(\\omega)=\\dfrac{4\\lambda}{4\\lambda^2+\\omega^2}$.")],
          "Papoulis 9; Ross 10.7"),
     "The lead swaps between Max and Lando at random Poisson moments. How alike are the leaders τ minutes apart?",
     ["<strong>$X(t)X(t+\\tau)=(-1)^{\\#\\text{swaps}}$ = same leader iff an even number of swaps.</strong> $X(0)^2=1$, so only the swaps in between matter, and they are Poisson($\\lambda\\tau$).",
      "<strong>$\\sum_k e^{-\\lambda\\tau}(-\\lambda\\tau)^k/k!=e^{-2\\lambda\\tau}$ = the Poisson series with a sign.</strong> It is the Poisson PGF $e^{\\lambda\\tau(z-1)}$ at $z=-1$.",
      "<strong>$S_X=\\frac{4\\lambda}{4\\lambda^2+\\omega^2}$ = a low-pass spectrum.</strong> The Fourier transform of $e^{-2\\lambda|\\tau|}$: more swaps (larger $\\lambda$) push power to higher frequencies."])

# ---------- 24.07 Renewal processes ----------
S = [0, 1.6, 2.4, 4.3, 5.0, 6.9, 8.3]
x0, base, sx, sy = 26, 112, 22, 13
mu_gap = 8.3 / 6
pts = f"M {x0} {base}"
for i in range(1, len(S)):
    pts += f" L {x0 + S[i] * sx:.1f} {base - (i - 1) * sy} L {x0 + S[i] * sx:.1f} {base - i * sy}"
pts += f" L {x0 + 9.2 * sx:.1f} {base - (len(S) - 1) * sy}"
card(24, 7, "RENEWAL THEORY", "Renewal Processes & the Elementary Renewal Theorem",
     [AX(22, base, 228, 12),
      P(pts, w=1.8),
      L(x0, base, x0 + 9.2 * sx, base - 9.2 / mu_gap * sy, 1, d="4 3"),
      "".join(C(x0 + s_ * sx, base, 1.8) for s_ in S[1:]),
      N(x0 + S[1] * sx, base + 9, "S₁", 6.6), N(x0 + S[2] * sx, base + 9, "S₂", 6.6), N(x0 + S[3] * sx, base + 9, "S₃", 6.6),
      N(x0 + (S[2] + S[3]) / 2 * sx, base - 4, "T₃", 6.3),
      N(x0 + 7.3 * sx, base - 9.6 / mu_gap * sy, "slope 1/μ", 7, a="start"),
      N(x0 + 4, 28, "N(t) ≥ n ⇔ Sₙ ≤ t", 7, a="start", w="bold"),
      N(x0 + 4, 38, "N(t)/t → 1/μ", 7, a="start"),
      T(x0 + 4, 18, "N(t) = stops so far", 7.5, a="start"),
      T(228, 134, "t (laps); gaps Tᵢ i.i.d. with mean μ", 7, a="end")],
     "The renewal counting process N(t) steps up at each renewal S₁, S₂, … where the gaps Tᵢ are i.i.d. with mean μ. "
     "In the long run the staircase hugs the dashed line of slope 1/μ.",
     ["<strong>Setup:</strong> i.i.d. gaps $T_i\\ge0$ with mean $\\mu$, renewal times $S_n=T_1+\\dots+T_n$, and $N(t)=\\max\\{n:S_n\\le t\\}$. Poisson is the case $T_i\\sim\\mathrm{Exp}(\\lambda)$.",
      "<strong>Duality:</strong> $\\{N(t)\\ge n\\}=\\{S_n\\le t\\}$, so $\\mathbb P(N(t)\\ge n)=\\mathbb P(S_n\\le t)$ and $m(t)=\\mathbb E[N(t)]=\\sum_{n\\ge1}\\mathbb P(S_n\\le t)$.",
      "<strong>Limits:</strong> $N(t)/t\\to1/\\mu$ a.s., $m(t)/t\\to1/\\mu$ (elementary renewal theorem), and $N(t)\\approx\\mathcal N\\big(\\frac t\\mu,\\frac{t\\sigma^2}{\\mu^3}\\big)$ for large $t$."],
     "$$S_{N(t)}\\le t\\lt S_{N(t)+1}\\ \\Rightarrow\\ \\frac{S_{N(t)}}{N(t)}\\le\\frac t{N(t)}\\lt\\frac{S_{N(t)+1}}{N(t)+1}\\cdot\\frac{N(t)+1}{N(t)}\\ \\Rightarrow\\ \\frac{N(t)}t\\to\\frac1\\mu$$",
     "<strong>Pit stops over a long season.</strong> Each set of tyres lasts a random number of laps, about 20 on average, and a fresh "
     "set starts the clock again. Over 1,000 laps Red Bull makes about $1000/20=50$ stops, whatever the shape of the tyre-life "
     "distribution; only the mean matters in the long run.",
     "E[N(t)] = t/μ holds exactly only for the Poisson process; in general it is only the long-run slope. And the gap that covers a "
     "fixed time t is longer than average, with mean E[T²]/E[T] ≥ μ (inspection paradox).",
     "THEOREM",
     stmt("Renewal process and the elementary renewal theorem.",
          [ln("Let $T_1,T_2,\\dots\\ge0$ be i.i.d. with mean $\\mu\\in(0,\\infty]$, $S_n=T_1+\\dots+T_n$ and $N(t)=\\max\\{n:S_n\\le t\\}$."),
           ln("Then $\\{N(t)\\ge n\\}=\\{S_n\\le t\\}$, and as $t\\to\\infty$"),
           ln("$\\dfrac{N(t)}t\\to\\dfrac1\\mu$ almost surely and $\\dfrac{\\mathbb E[N(t)]}t\\to\\dfrac1\\mu$.", True)],
          "Ross 7.1–7.3; Grimmett 10.1–10.2"),
     "Each tyre set lasts a random number of laps averaging 20. Roughly how many stops does Red Bull make in 1,000 laps?",
     ["<strong>$\\{N(t)\\ge n\\}=\\{S_n\\le t\\}$ = counts and sums are two views.</strong> At least $n$ stops by lap $t$ means the $n$-th stop came by lap $t$.",
      "<strong>$S_{N(t)}\\le t\\lt S_{N(t)+1}$ = a sandwich.</strong> Divide by $N(t)$ and use the SLLN $S_n/n\\to\\mu$ on both sides: $t/N(t)\\to\\mu$.",
      "<strong>Only $\\mu$ survives.</strong> The long-run rate $1/\\mu$ ignores the gap distribution; the spread of $N(t)$ uses $\\sigma^2$ too."])

# ---------- 24.08 Renewal-reward & alternating renewal ----------
U = [2.2, 1.8, 2.6, 1.5]
D = [0.6, 0.9, 0.5, 0.7]
x0, sx, y = 24, 21, 50
parts, t = [], 0.0
for u, dd in zip(U, D):
    parts += [R(round(x0 + t * sx, 1), y, round(u * sx, 1), 16, "#cbd5e1", 1.1)]
    t += u
    parts += [R(round(x0 + t * sx, 1), y, round(dd * sx, 1), 16, "#ffffff", 1.1)]
    t += dd
c1 = U[0] + D[0]
parts += [L(x0, y + 26, x0 + c1 * sx, y + 26, 1, ar=True), L(x0 + c1 * sx, y + 26, x0, y + 26, 1, ar=True),
          N(x0 + c1 * sx / 2, y + 36, "one cycle", 6.8),
          N(x0 + U[0] * sx / 2, y + 11, "up", 7), N(x0 + (U[0] + D[0] / 2) * sx, y - 4, "down", 6.6),
          L(22, y + 16, 228, y + 16, 1, ar=True),
          N(120, 26, "long-run fraction up = E[U] / (E[U] + E[D])", 7.2, w="bold"),
          N(120, 108, "reward rate = E[reward per cycle] / E[cycle length]", 7),
          T(228, 134, "time; up spells Uᵢ, repairs Dᵢ, i.i.d. cycles", 7, a="end")]
card(24, 8, "RENEWAL THEORY", "Renewal-Reward & Alternating Renewal: Long-Run Averages",
     parts,
     "A power unit alternates between running (grey, length U) and repair (white, length D). Each up-then-down cycle starts the "
     "process afresh, so the long-run fraction of time running is E[U]/(E[U] + E[D]).",
     ["<strong>Renewal-reward:</strong> i.i.d. cycles $(T_i,R_i)$ with $\\mathbb E[T]\\lt\\infty$, $\\mathbb E|R|\\lt\\infty$; the total reward by time $t$ satisfies $\\frac{R(t)}t\\to\\frac{\\mathbb E[R]}{\\mathbb E[T]}$ a.s. and in mean.",
      "<strong>Alternating renewal:</strong> cycles of up time $U_i$ then down time $D_i$; the long-run fraction of time up (the availability) is $\\frac{\\mathbb E[U]}{\\mathbb E[U]+\\mathbb E[D]}$.",
      "<strong>Uses:</strong> long-run cost per unit time of a replacement policy, availability of a machine, and average queue quantities via Little's law."],
     "$$\\lim_{t\\to\\infty}\\frac{R(t)}t=\\frac{\\mathbb E[R]}{\\mathbb E[T]},\\qquad \\lim_{t\\to\\infty}\\frac{1}{t}\\int_0^t\\mathbf 1\\{\\text{up at }s\\}ds=\\frac{\\mathbb E[U]}{\\mathbb E[U]+\\mathbb E[D]}$$",
     "<strong>Engine availability.</strong> On the dyno, a power unit runs on average 9 hours before it fails and a repair takes 1 hour "
     "on average. In the long run it is running $9/(9+1)=90\\%$ of the time. Tyre cost works the same way: a set costing 2,000 that "
     "lasts 20 laps on average costs 100 per lap in the long run.",
     "E[R/T] ≠ E[R]/E[T]: the long-run rate is the ratio of the means, not the mean of the per-cycle ratios. Pick the cycle so that "
     "the process really restarts at its end.",
     "THEOREM",
     stmt("Renewal-reward theorem.",
          [ln("Let the cycles $(T_i,R_i)$ be i.i.d., with $T_i\\ge0$, $\\mathbb E[T_i]\\lt\\infty$ and $\\mathbb E|R_i|\\lt\\infty$, and let"),
           ln("$R(t)=\\sum_{i=1}^{N(t)}R_i$ be the reward earned by time $t$. Then", True),
           ln("$\\dfrac{R(t)}t\\to\\dfrac{\\mathbb E[R]}{\\mathbb E[T]}$ almost surely, and $\\dfrac{\\mathbb E[R(t)]}t\\to\\dfrac{\\mathbb E[R]}{\\mathbb E[T]}$.", True),
           ln("With reward = up time in each cycle, the long-run fraction up is $\\mathbb E[U]/(\\mathbb E[U]+\\mathbb E[D])$.")],
          "Ross 7.4–7.5"),
     "An engine runs 9 hours on average between failures and a repair takes 1 hour. What fraction of the time is it running?",
     ["<strong>$R(t)/t\\to\\mathbb E[R]/\\mathbb E[T]$ = reward per cycle over cycle length.</strong> $R(t)/t=\\frac{R(t)}{N(t)}\\cdot\\frac{N(t)}t\\to\\mathbb E[R]\\cdot\\frac1{\\mathbb E[T]}$ by the SLLN twice.",
      "<strong>$\\mathbb E[U]/(\\mathbb E[U]+\\mathbb E[D])$ = reward is the up time.</strong> Each cycle earns its up time $U$ and lasts $U+D$.",
      "<strong>Only means enter.</strong> The distributions of $U$ and $D$ do not matter for long-run averages, as long as the cycles are i.i.d."])

# ---------- 25.07 Brownian motion with drift, geometric BM ----------
random.seed(11)
x0, base0, sx, k = 26, 52, 2.0, 6
mu_, sig = -0.1, 0.3
pts, xv = [f"M {x0} {base0}"], 0.0
for i in range(1, 96):
    xv += mu_ + sig * random.gauss(0, 1)
    pts.append(f"L {x0 + i * sx:.1f} {base0 - xv * k:.1f}")
a_lvl = 2.0
card(25, 7, "BROWNIAN MOTION", "Brownian Motion with Drift & Geometric Brownian Motion",
     [L(22, base0, 228, base0, 1, ar=True), L(x0, 128, x0, 12, 1, ar=True),
      L(x0, base0 - a_lvl * k, 224, base0 - a_lvl * k, 1.2, d="4 3"),
      L(x0, base0, x0 + 95 * sx, base0 + 95 * 0.1 * k, 1, d="2 2"),
      P(" ".join(pts), w=1.4),
      N(224, base0 - a_lvl * k - 4, "a = 2 s: Lando catches Max", 6.8, a="end"),
      N(x0 + 4, 125, "dashed: drift μt, μ = −0.1 s/lap, σ = 0.3", 6.8, a="start"),
      N(x0 + 4, 106, "ℙ(ever reach a) = e^(2μa/σ²) ≈ 0.012", 7, a="start", w="bold"),
      T(x0 + 4, 115, "X(t) = μt + σB(t)", 7, a="start"),
      T(228, base0 - 4, "laps", 7, a="end")],
     "Lando's gain on Max as Brownian motion with drift μ = −0.1 s per lap and σ = 0.3. The path wanders, but the dashed drift line "
     "pulls it down, so the chance of ever reaching +2 s is only e^(2μa/σ²) ≈ 0.012.",
     ["<strong>Drift:</strong> $X(t)=\\mu t+\\sigma B(t)$ has independent $\\mathcal N(\\mu s,\\sigma^2s)$ increments over time $s$.",
      "<strong>Hitting via a martingale:</strong> $e^{-2\\mu X(t)/\\sigma^2}$ is a martingale, so by optional stopping $\\mathbb P(\\text{hit }a\\text{ before }-b)=\\frac{e^{2\\mu b/\\sigma^2}-1}{e^{2\\mu b/\\sigma^2}-e^{-2\\mu a/\\sigma^2}}$; for $\\mu\\lt0$, $\\mathbb P(\\text{ever hit }a)=e^{2\\mu a/\\sigma^2}$.",
      "<strong>Geometric BM:</strong> $S(t)=S(0)e^{(\\mu-\\sigma^2/2)t+\\sigma B(t)}$ is lognormal with $\\mathbb E[S(t)]=S(0)e^{\\mu t}$; its log is BM with drift $\\mu-\\sigma^2/2$."],
     "$$\\mathbb E\\big[e^{\\theta X(t)}\\big]=e^{(\\theta\\mu+\\theta^2\\sigma^2/2)t},\\qquad \\theta=-\\frac{2\\mu}{\\sigma^2}\\ \\Rightarrow\\ e^{-2\\mu X(t)/\\sigma^2}\\text{ is a martingale}$$",
     "<strong>Can Lando close the gap?</strong> Max pulls away by 0.1 s a lap on average, with lap-to-lap noise $\\sigma=0.3$ s. "
     "Lando is 2 s behind; to catch Max he must gain 2 s at some point: $\\mathbb P=e^{2(-0.1)(2)/0.09}=e^{-4.4}\\approx0.012$. "
     "A steady drift beats noise in the long run.",
     "For geometric BM the log grows at μ − σ²/2, not μ (Itô correction): the median grows at rate μ − σ²/2 while the mean grows at "
     "rate μ. And with a drift away from a, the chance of ever hitting a is below 1.",
     "THEOREM",
     stmt("Brownian motion with drift: hitting probabilities.",
          [ln("Let $X(t)=\\mu t+\\sigma B(t)$ with $\\mu\\ne0$, and $a,b\\gt0$. Since $e^{-2\\mu X(t)/\\sigma^2}$ is a martingale,"),
           ln("$\\mathbb P(X\\text{ hits }a\\text{ before }-b)=\\dfrac{e^{2\\mu b/\\sigma^2}-1}{e^{2\\mu b/\\sigma^2}-e^{-2\\mu a/\\sigma^2}}$,", True),
           ln("and for $\\mu\\lt0$, $\\mathbb P(\\sup_tX(t)\\ge a)=e^{2\\mu a/\\sigma^2}$."),
           ln("Geometric BM $S(t)=S(0)e^{(\\mu-\\sigma^2/2)t+\\sigma B(t)}$ has $\\mathbb E[S(t)]=S(0)e^{\\mu t}$.")],
          "Ross 10.3; Karlin & Taylor 7.5"),
     "Max pulls away by 0.1 s a lap on average, with noise. What is the chance Lando, 2 s behind, ever catches him?",
     ["<strong>$X(t)=\\mu t+\\sigma B(t)$ = trend plus noise.</strong> Over $t$ laps the mean moves by $\\mu t$ but the noise only grows like $\\sigma\\sqrt t$, so the trend wins.",
      "<strong>$e^{-2\\mu X/\\sigma^2}$ = a martingale that cancels the drift.</strong> Choose $\\theta$ with $\\theta\\mu+\\theta^2\\sigma^2/2=0$; optional stopping at the first exit from $(-b,a)$ gives the hitting chances.",
      "<strong>$S=S(0)e^{X}$ = growth by percentages.</strong> Geometric BM is $e^{\\text{BM with drift}}$: lognormal at each time, with mean $S(0)e^{\\mu t}$."])

# ---------- 27.07 Little's law, PASTA, other queues ----------
arr = [0.5, 1.4, 2.0, 3.6, 4.4, 6.0]
dep = [1.6, 2.7, 3.3, 4.9, 5.7, 7.1]
x0, base, sx, sy = 26, 112, 26, 13


def stair(ts):
    d = f"M {x0} {base}"
    for i, tt in enumerate(ts):
        d += f" L {x0 + tt * sx:.1f} {base - i * sy} L {x0 + tt * sx:.1f} {base - (i + 1) * sy}"
    return d + f" L {x0 + 7.6 * sx:.1f} {base - len(ts) * sy}"


fill = f"M {x0 + arr[0] * sx} {base} " + " ".join(
    f"L {x0 + arr[i] * sx:.1f} {base - (i + 1) * sy} L {x0 + (arr[i + 1] * sx if i + 1 < len(arr) else 7.6 * sx):.1f} {base - (i + 1) * sy}" for i in range(len(arr)))
card(27, 7, "QUEUEING", "Little's Law, PASTA & Queues Beyond M/M/1",
     [AX(22, base, 228, 12),
      P(stair(arr), w=2), P(stair(dep), w=1.4, dash="4 3"),
      L(x0 + arr[2] * sx, base - 2.5 * sy, x0 + dep[2] * sx, base - 2.5 * sy, 1, ar=True),
      N(x0 + arr[2] * sx - 3, base - 2.5 * sy + 2, "Wᵢ", 6.8, a="end"),
      L(x0 + 4.65 * sx, base - 3 * sy, x0 + 4.65 * sx, base - 5 * sy, 1, ar=True),
      N(x0 + 5.1 * sx, base - 4 * sy - 3, "L(t)", 6.8, a="start"),
      N(x0 + 5.6 * sx, base - 6.2 * sy - 2, "A(t) arrivals", 6.8, a="start"),
      N(x0 + 6.0 * sx, base - 3.6 * sy, "D(t) departures", 6.8, a="start"),
      N(x0 + 4, 22, "area between = Σ Wᵢ = ∫ L(t) dt", 7, a="start"),
      N(x0 + 4, 32, "⇒ L = λW", 7.5, a="start", w="bold"),
      T(228, 134, "t: cars entering and leaving the pit lane", 7, a="end")],
     "Arrivals A(t) (solid) and departures D(t) (dashed). The horizontal gap is a car's time in the system Wᵢ, the vertical gap is "
     "the number inside L(t), and the area between them counts both ways: that is Little's law L = λW.",
     ["<strong>Little's law:</strong> for any stable system, long-run averages satisfy $L=\\lambda W$ (and $L_Q=\\lambda W_Q$), whatever the arrival and service laws.",
      "<strong>PASTA and finite buffers:</strong> Poisson arrivals see time averages, so an arrival finds $n$ customers with chance $\\pi_n$. M/M/1/K: $\\pi_n=\\frac{(1-\\rho)\\rho^n}{1-\\rho^{K+1}}$, $n\\le K$, a fraction $\\pi_K$ is turned away, and Little uses $\\lambda(1-\\pi_K)$.",
      "<strong>Infinite servers:</strong> in M/M/∞ and M/G/∞ the number in the system is Poisson with mean $\\lambda\\,\\mathbb E[S]$, for any service law $S$."],
     "$$L=\\lambda W,\\qquad \\pi_n^{\\text{M/M/1/K}}=\\frac{(1-\\rho)\\rho^n}{1-\\rho^{K+1}},\\qquad N_{\\text{M/G/}\\infty}\\sim\\mathrm{Pois}(\\lambda\\,\\mathbb E[S])$$",
     "<strong>Cars in the pit lane.</strong> In the pit window cars enter at about 2 a minute and each spends about 25 s in the lane. "
     "Little's law gives $L=2\\times\\frac{25}{60}\\approx0.83$ cars in the lane on average, and since every car is served at once "
     "(M/G/∞) the count is Poisson(0.83) whatever the spread of pit times. A box that can stack only $K$ cars behaves like M/M/1/K.",
     "With a finite buffer, Little's law must use the accepted rate λ(1 − π_K), not λ. And PASTA needs Poisson arrivals: in a D/D/1 "
     "queue where each car arrives just after the previous one leaves, arrivals always see an empty box.",
     "THEOREM",
     stmt("Little's law and PASTA.",
          [ln("If the long-run arrival rate $\\lambda$, mean number in system $L$ and mean time in system $W$ exist and are finite, then"),
           ln("$L=\\lambda W$.", True),
           ln("If arrivals are Poisson and do not anticipate the future, the fraction of arrivals finding $n$ in the system"),
           ln("equals the long-run fraction of time $\\pi_n$ with $n$ in the system (PASTA).", True),
           ln("In M/G/∞, the number in the system at time $t$ (empty at 0) is $\\mathrm{Pois}\\big(\\lambda\\int_0^t\\mathbb P(S\\gt s)ds\\big)\\to\\mathrm{Pois}(\\lambda\\,\\mathbb E[S])$.")],
          "Ross 8.2–8.4; Ross 5.3"),
     "Cars enter the pit lane at 2 a minute and each spends 25 s in it. How many are in the pit lane at a typical moment?",
     ["<strong>$L=\\lambda W$ = the area counted two ways.</strong> Summing each car's time $W_i$ (horizontally) equals integrating the number inside $L(t)$ (vertically).",
      "<strong>PASTA = Poisson arrivals are fair samplers.</strong> They come at moments independent of the queue's past, so they see the time-average state.",
      "<strong>M/M/1/K and M/G/∞ = cut off, or never wait.</strong> A buffer of $K$ truncates the geometric law; infinitely many servers make the count Poisson($\\lambda\\mathbb E[S]$)."])

STORY = {
    "30407": ("STORY 4 · STEP 7 · GAINS THAT MULTIPLY", "Exponentiate a normal and you get the <b>lognormal</b>: skewed right, with a mean above its median.",
              [["30402", "a monotone change of variables"], ["30305", "the bell"]], [["32507", "geometric Brownian motion"]]),
    "30507": ("STORY 5 · STEP 7 · COUNT WITH SWITCHES", "Write a count as a <b>sum of 0/1 indicators</b>: its mean is the sum of the chances, even for dependent events.",
              [["30501", "linearity of expectation"], ["30503", "variance of a sum"]], [["30307", "the Binomial as a sum of indicators"]]),
    "30907": ("STORY 9 · STEP 7 · SHARES AND SAMPLES", "Gamma parts split into a <b>Beta share</b> and a Gamma total; squared normals give χ², and from them t and F.",
              [["30311", "the Gamma"], ["30905", "sums that stay in the family"]], [["31506", "the t-statistic for large samples"]]),
    "32307": ("STORY 23 · STEP 7 · TWO SIGNALS AT ONCE", "The <b>cross-spectrum</b> of input and output reveals the filter, phase included, and gives the Wiener filter.",
              [["32305", "filtering a WSS process"]], [["31106", "the scalar Wiener filter"], ["32308", "a worked spectrum"]]),
    "32308": ("STORY 23 · STEP 8 · THE TELEGRAPH", "A ±1 signal that flips at Poisson times is WSS with <b>R(τ) = e^(−2λ|τ|)</b>.",
              [["32401", "the Poisson process"], ["32302", "autocorrelation"]], [["32303", "its power spectrum"]]),
    "32407": ("STORY 24 · STEP 7 · ANY GAPS", "Let the gaps have <b>any i.i.d. law</b>: the count still grows like t/μ, only the mean gap matters.",
              [["32402", "exponential gaps"], ["31702", "the strong law"]], [["32408", "rewards per cycle"], ["32406", "the longer gap"]]),
    "32408": ("STORY 24 · STEP 8 · PER CYCLE", "Long-run reward rate = <b>reward per cycle ÷ cycle length</b>; up time ÷ cycle gives availability.",
              [["32407", "renewal processes"]], [["32707", "Little's law"]]),
    "32507": ("STORY 25 · STEP 7 · A DRIFTING GAP", "Add a <b>drift</b> to Brownian motion; an exponential martingale gives the chance of ever reaching a level.",
              [["32502", "standard Brownian motion"], ["32605", "optional stopping"]], [["30407", "the lognormal"]]),
    "32707": ("STORY 27 · STEP 7 · BEYOND M/M/1", "<b>L = λW</b> for any stable queue; Poisson arrivals see time averages; buffers truncate, infinite servers give Poisson.",
              [["32705", "M/M/1 and M/M/c"], ["32408", "renewal-reward"]], []),
}

if __name__ == "__main__":
    write_cards(cards)
    write_story(STORY, add_links=[("30406", ["30407", "the lognormal"]), ("30506", ["30507", "the indicator method"]),
                                  ("30906", ["30907", "Beta, χ², t and F"]), ("32306", ["32307", "two signals at once"]),
                                  ("32406", ["32407", "renewal processes"]), ("32506", ["32507", "Brownian motion with drift"]),
                                  ("32706", ["32707", "Little's law and other queues"])])
