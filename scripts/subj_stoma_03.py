"""StoMA topic 03 (random variables, PMF, PDF, exponential, Gaussian, mixed). F1 picture: minutes until the first
safety car, safety cars per race, Max's lap time, time spent behind the safety car."""
from f1_lib import *

SUBJECT = "StoMA"
SIG = lambda x: 112 - 84 / (1 + math.exp(-(x - 110) / 18))
BELL = lambda x, m=120, s=26, h=80: 112 - h * math.exp(-((x - m) ** 2) / (2 * s * s))

def d1(c):
    x0 = 104
    return svg(c, ax(24, 112, 226, 14), N(226, 124, "x min", 7, "end"), N(28, 18, "F(x)", 7.5, "start"),
        dash(24, 28, 226, 28), N(210, 24, "1", 7), N(30, 118, "0", 7),
        fn(SIG, 24, 226, 50, 1.1), dash(x0, 112, x0, SIG(x0)), dash(24, SIG(x0), x0, SIG(x0)),
        C(x0, f(SIG(x0)), 2.4), N(x0 + 4, 124, "x", 7.5, "start"), N(30, SIG(x0) - 4, "F(x) = ℙ(X ≤ x)", 7.5, "start"),
        N(150, 52, "never decreases", 7, "start"), N(150, 62, "→1 as x→∞, →0 as x→−∞", 6.5, "start"),
        N(120, 138, "X = minutes to the first safety car; F(x) = ℙ(one by minute x)", 6.5))

def d2(c):
    out = ax(24, 112, 226, 14) + N(226, 124, "x safety cars", 7, "end") + N(28, 18, "F(x)", 7.5, "start")
    ys = [112, 112 - 36, 112 - 66, 112 - 86, 112 - 96]
    xs = [30, 70, 110, 150, 190]
    for i in range(4):
        out += L(xs[i], ys[i + 1] if i else 112, xs[i + 1], ys[i + 1], 1.1) if False else ""
    out += L(24, 112, 70, 112, 1.1) + L(70, 76, 110, 76, 1.1) + L(110, 46, 150, 46, 1.1) + L(150, 26, 226, 26, 1.1)
    out += dash(70, 112, 70, 76, 1) + dash(110, 76, 110, 46) + dash(150, 46, 150, 26)
    for x, y in [(70, 76), (110, 46), (150, 26)]:
        out += C(x, y, 2.4)
    for x, y in [(70, 112), (110, 76), (150, 46)]:
        out += C(x, y, 2.4, "#ffffff")
    out += tick(70, 112, "0") + tick(110, 112, "1") + tick(150, 112, "2")
    out += N(76, 98, "p(x₁)", 7, "start") + N(116, 64, "p(x₂)", 7, "start") + N(156, 38, "p(x₃)", 7, "start")
    out += N(158, 74, "jump = ℙ(X = xₖ)", 7, "start") + N(158, 84, "∑ jumps = 1", 7, "start")
    return svg(c, out)

def d3(c):
    x0 = 130
    return svg(c, ax(24, 112, 226, 14), N(226, 124, "t min", 7, "end"), N(28, 18, "f(t)", 7.5, "start"),
        fn(lambda x: 112 - 70 * math.exp(-((x - 100) ** 2) / (1800)), 24, 226, 60, 1.1),
        area(lambda x: 112 - 70 * math.exp(-((x - 100) ** 2) / 1800), 40, x0, 112, 30),
        dash(x0, 112, x0, 112 - 70 * math.exp(-((x0 - 100) ** 2) / 1800)), N(x0, 124, "x", 7.5),
        N(78, 100, "F(x) = ∫ f(t) dt", 7.5, "middle"), N(168, 52, "f(x) = F′(x)", 7.5, "start"), N(168, 63, "slope of F", 6.5, "start"),
        N(168, 80, "ℙ(X = c) = 0:", 7, "start"), N(168, 90, "no area at a point", 7, "start"),
        N(120, 138, "minutes to the first safety car X, shaded area = ℙ(X ≤ x)", 6.5))

def d4(c):
    lam = 0.03
    f1 = lambda x: 112 - 80 * math.exp(-lam * (x - 24))
    t0, s0 = 70, 60
    return svg(c, ax(24, 112, 226, 14), N(226, 124, "minutes", 7, "end"), N(30, 18, "λe^(−λt)", 7.5, "start"),
        fn(f1, 24, 226, 50, 1.1), dash(t0, 112, t0, f1(t0)), dash(t0 + s0, 112, t0 + s0, f1(t0 + s0)),
        N(t0, 124, "t", 7.5), N(t0 + s0, 124, "t + s", 7.5), 
        fn(lambda x: 112 - 0.5 * 80 * math.exp(-lam * (x - t0)) * 1.0 if False else f1(x - t0 + 24) + 0 if False else 112 - 50 * math.exp(-lam * (x - t0)), t0, 226, 40, 1.1, "4 3"),
        N(150, 36, "dashed: no safety car for t min", 7, "start"), N(150, 46, "the same shape starts again", 7, "start"),
        N(120, 138, "ℙ(X > t + s | X > t) = e^(−λs) = ℙ(X > s)", 7.5))

def d5(c):
    return svg(c, ax(24, 112, 226, 14), N(226, 124, "x", 7.5, "end"),
        fn(BELL, 30, 220, 60, 1.1), dash(120, 112, 120, BELL(120)), N(120, 124, "μ", 8),
        L(120, 100, 146, 100, 1), N(133, 96, "σ", 7.5), dash(146, 112, 146, BELL(146)),
        N(30, 30, "X = lap time ~ 𝒩(μ, σ²)", 7.5, "start"), arrow(168, 70, 196, 70, 1), N(182, 64, "−μ, ÷σ", 7, "middle"),
        N(206, 74, "Z", 8.5), N(206, 84, "~ 𝒩(0,1)", 7, "middle"),
        N(120, 138, "Z = (X − μ)/σ: Φ(−z) = 1 − Φ(z) by symmetry", 7))

def d6(c):
    return svg(c, ax(24, 112, 226, 14), N(226, 124, "seconds behind SC x", 7, "end"), N(28, 18, "F(x)", 7.5, "start"),
        dash(24, 28, 226, 28), N(220, 24, "1", 7),
        L(24, 112, 24, 60, 1.1), C(24, 112, 2.4, "#ffffff"), C(24, 60, 2.4),
        fn(lambda x: 60 - 32 * (1 - math.exp(-0.022 * (x - 24))), 24, 226, 50, 1.1),
        N(30, 80, "jump α = no safety car (0 s)", 7, "start"), N(110, 54, "(1−α)F_cont: behind the SC for x s", 7, "start"),
        N(120, 138, "F = α·F(step) + (1−α)·F(smooth): point mass plus density", 7))

CARDS = {
30301: dict(d=d1, kind="DEFINITION",
  stmt=r"<b>Random variable and CDF.</b> A random variable on $(\Omega,\mathcal F,\mathbb P)$ is a function $X:\Omega\to\mathbb R$ such that $\{X\le x\}\in\mathcal F$ for all $x$. Its cumulative distribution function is $F_X(x)=\mathbb P(X\le x)$. Then $F_X$ is non-decreasing and right-continuous, with $F_X(-\infty)=0$ and $F_X(\infty)=1$, and $F_X(x)-F_X(x^-)=\mathbb P(X=x)$ (Ross 4.1; Grimmett 2.1).",
  hint='How do you turn the minutes until the first safety car into one curve that answers “by minute x?” for every x?',
  bd=[r"<strong>$X:\Omega\to\mathbb R$ = a number read off each race.</strong> The minutes until the first safety car: each point of $\Omega$ is sent to that number.",
      r"<strong>$F_X(x)=\mathbb P(X\le x)$ = chance of a safety car by minute $x$.</strong> It collects all races whose first safety car comes at or before $x$.",
      r"<strong>$F_X(-\infty)=0,\ F_X(\infty)=1$ = it climbs from nothing to everything.</strong> It never decreases, and it is right-continuous: a jump is exactly the chance of one exact value."],
  conn='<strong>The first safety car as a number per race.</strong> Each race gets the minute its first safety car comes out. The CDF then answers “in what share of races is there a safety car by minute 30?” for every minute at once, a curve that only goes up.',
  cap='The CDF F(x) climbs from 0 to 1 as x (minutes until the first safety car) grows. The marked point shows F(x) = ℙ(X ≤ x) read off at one x.'),
30302: dict(d=d2, kind="DEFINITION",
  stmt=r"<b>Discrete random variable and PMF.</b> $X$ is discrete if it takes values in a countable set $\{x_k\}$. Its probability mass function $p_X(x_k)=\mathbb P(X=x_k)$ satisfies $p_X(x_k)\ge0$ and $\sum_kp_X(x_k)=1$. Its CDF is a step function $F_X(x)=\sum_{x_k\le x}p_X(x_k)$ with a jump of size $p_X(x_k)$ at each $x_k$ (Ross 4.2; Grimmett 2.1).",
  hint='If you count the safety cars in a race, what does the CDF look like, and what is the size of each step?',
  bd=[r"<strong>$p_X(x_k)\ge0$ = a chance for each count.</strong> 0, 1, 2 or 3 safety cars in a race each have their own chance.",
      r"<strong>$\sum_kp_X(x_k)=1$ = the chances use up everything.</strong> Every race has some number of safety cars.",
      r"<strong>$F_X(x_k)-F_X(x_k^-)=\mathbb P(X=x_k)$ = the jump is the chance.</strong> The CDF is flat between counts and jumps at each count by exactly its chance."],
  conn='<strong>Counting safety cars.</strong> A race has 0, 1, 2 or 3 safety cars. The chances of these counts must add to 1, and the running total, the CDF, climbs in steps whose heights are those chances.',
  cap='The step CDF of X = safety cars in a race. At each count xₖ it jumps by p(xₖ), a filled dot where it lands and an open dot where it left, and the jumps add up to 1.'),
30303: dict(d=d3, kind="DEFINITION",
  stmt=r"<b>Continuous random variable and PDF.</b> $X$ is continuous if $F_X(x)=\int_{-\infty}^xf_X(t)\,dt$ for a function $f_X\ge0$ with $\int_{-\infty}^\infty f_X=1$, the probability density function. Then $f_X(x)=F_X'(x)$ at continuity points of $f_X$, $\mathbb P(a\le X\le b)=\int_a^bf_X$, and $\mathbb P(X=c)=0$ for every $c$ (Ross 5.1; Grimmett 4.1).",
  hint='If the first safety car can come at any instant, how do chances become areas?',
  bd=['<strong>$f_X(t)$ = density, chance per minute.</strong> A tall spot of the curve means first safety cars near minute $t$ are common. It is not a chance itself and may exceed 1.',
      r"<strong>$F_X(x)=\int_{-\infty}^xf_X(t)\,dt$ = area up to $x$.</strong> The shaded area under the curve to the left of $x$ is the chance the first safety car comes by minute $x$.",
      r"<strong>$\mathbb P(X=c)=0$ = a single exact value has no area.</strong> Only stretches of minutes carry chance; and $f_X=F_X'$ recovers the curve from the CDF."],
  conn='<strong>The safety car at any instant.</strong> A safety car at exactly 27.000… minutes has chance 0; “between minute 25 and 30” has the area of the curve over that stretch. The curve is high where first safety cars usually come.',
  cap='The density f(t) of the minute X of the first safety car. The shaded area up to x is F(x) = ∫f(t)dt, f is the slope of F, and a single instant carries no area, so ℙ(X = c) = 0.'),
30304: dict(d=d4, kind="THEOREM",
  stmt=r"<b>Exponential distribution and memorylessness.</b> $X\sim\mathrm{Exp}(\lambda)$ has density $f_X(t)=\lambda e^{-\lambda t}$ for $t\ge0$, so $\mathbb P(X>t)=e^{-\lambda t}$. Then for all $s,t\ge0$, $\mathbb P(X>t+s\mid X>t)=\dfrac{e^{-\lambda(t+s)}}{e^{-\lambda t}}=e^{-\lambda s}=\mathbb P(X>s)$. It is the only continuous distribution on $[0,\infty)$ with this property (Ross 5.5).",
  hint='There has been no safety car for t minutes. What is the chance there is none for s more?',
  bd=[r"<strong>$\lambda e^{-\lambda t}$ = the waiting-time curve.</strong> Early incidents are most likely, and $\lambda$ is how many safety cars per minute come on average.",
      r"<strong>$\mathbb P(X>t)=e^{-\lambda t}$ = still no safety car after $t$.</strong> Each extra minute multiplies this chance by the same factor.",
      r"<strong>$\mathbb P(X>t+s\mid X>t)=\mathbb P(X>s)$ = no memory.</strong> A clean first hour changes nothing: the remaining wait for a safety car has the same law as at lights out."],
  conn='<strong>A safety car is never “due”.</strong> Forty clean laps and the strategists say a safety car must be coming, so Red Bull waits to pit. If incidents happen at random, the next one is no closer than at the start: the clean laps buy you nothing.',
  cap='The density λe^(−λt) of the wait for a safety car. After t clean minutes, the dashed curve beyond t has the same shape: ℙ(X > t+s | X > t) = e^(−λs) = ℙ(X > s).'),
30305: dict(d=d5, kind="THEOREM",
  stmt=r"<b>Standardisation of the normal law.</b> If $X\sim\mathcal N(\mu,\sigma^2)$, with density $f_X(x)=\dfrac1{\sigma\sqrt{2\pi}}e^{-(x-\mu)^2/2\sigma^2}$, then $Z=\dfrac{X-\mu}{\sigma}\sim\mathcal N(0,1)$. Writing $\Phi$ for the $\mathcal N(0,1)$ CDF, $\mathbb P(X\le x)=\Phi\!\left(\frac{x-\mu}{\sigma}\right)$ and $\Phi(-z)=1-\Phi(z)$ (Ross 5.4; Grimmett 4.4).",
  hint='How do you answer any normal question using the single table for mean 0 and variance 1?',
  bd=[r"<strong>$\mu$ = the centre.</strong> Max's typical lap time on this circuit, where the bell curve peaks.",
      r"<strong>$\sigma$ = the spread.</strong> How far a lap usually strays from $\mu$; a small $\sigma$ gives a narrow bell.",
      r"<strong>$Z=(X-\mu)/\sigma$ = measure in standard units.</strong> Shift by $\mu$ and divide by $\sigma$ to get the standard bell, so only $\Phi$ is needed; $\Phi(-z)=1-\Phi(z)$ by symmetry."],
  conn=r"<strong>Tenths away from typical.</strong> “That lap was 0.8 s slower than usual” means little unless you compare it to how much Max's laps normally vary. Dividing by $\sigma$ turns it into “how many usual spreads off the pace that lap was”.",
  cap="A bell curve for Max's lap time X with centre μ and spread σ. Subtracting μ and dividing by σ turns it into the standard bell Z = (X − μ)/σ ~ 𝒩(0,1)."),
30306: dict(d=d6, kind="WORKED EXAMPLE",
  stmt=r"<b>Mixed random variable.</b> A random variable whose CDF has the form $F_X=\alpha F_{\rm disc}+(1-\alpha)F_{\rm cont}$, $0<\alpha<1$, with $F_{\rm disc}$ a step function and $F_{\rm cont}$ continuous, is mixed. Its mean is $\mathbb E[X]=\sum_kx_k\,\mathbb P(X=x_k)+\int_{-\infty}^\infty x\,f_c(x)\,dx$, the atoms plus the continuous part, where $f_c$ is the density of the continuous part (Ross 5.1; Grimmett 4.1).",
  hint='With some chance there is no safety car, otherwise Max spends a continuous time behind it. How does that shape the CDF?',
  bd=[r"<strong>$\alpha F_{\rm disc}$ = no safety car.</strong> With chance $\alpha$ the time behind the safety car is exactly 0, so the CDF jumps at 0 by $\alpha$.",
      r"<strong>$(1-\alpha)F_{\rm cont}$ = otherwise a continuous time behind it.</strong> With chance $1-\alpha$ the time has a density and the CDF rises smoothly.",
      r"<strong>$\sum x_k\mathbb P(X=x_k)+\int xf_c$ = the mean has two parts.</strong> The atom contributes value times mass and the continuous part contributes the integral; dropping the atom gives a wrong mean."],
  conn='<strong>Behind the safety car.</strong> In some races there is no safety car at all: 0 seconds behind it. In the others Max spends a random time behind it. The time is part “exactly 0” and part “any positive amount”.',
  cap='The CDF of the time Max spends behind a safety car: a jump of size α at 0 (no safety car), then a smooth rise F_cont weighted by 1 − α up to 1.'),
}

STORY = {
30301: dict(s='STORY 3 · STEP 1 · A NUMBER PER RACE', b='A <b>random variable</b> reads one number off each race, and its <b>CDF</b> says how likely it is to be at most x.', f=[["30102", "chances obeying the axioms"]], n=[["30302", "countable values"], ["30303", "any real value"]]),
30302: dict(s="STORY 3 · STEP 2 · COUNTING", b="When the number is a count, the CDF is a staircase and each step's height is the <b>probability mass</b>.", f=[["30301", "the CDF"]], n=[["30303", "the smooth version"], ["30505", "generating functions for counts"]]),
30303: dict(s="STORY 3 · STEP 3 · SMOOTH", b="For any real value, chances become <b>areas under a density</b>; one exact value has probability 0.", f=[["30301", "the CDF"], ["30302", "the discrete version"]], n=[["30304", "the waiting-time density"], ["30305", "the bell curve"]]),
30304: dict(s="STORY 3 · STEP 4 · THE FORGETFUL WAIT", b="The <b>exponential</b> is the waiting time with no memory: the time already waited does not shorten the rest.", f=[["30303", "a density for a waiting time"]], n=[["30806", "the earliest of several waits"], ["32402", "gaps between Poisson arrivals"]]),
30305: dict(s="STORY 3 · STEP 5 · THE BELL", b="The <b>normal</b> law is measured in standard units, so one table covers every mean and spread.", f=[["30303", "a density with a centre and spread"]], n=[["30405", "its square"], ["31301", "several normals together"], ["31803", "why sums become normal"]]),
30306: dict(s="STORY 3 · STEP 6 · BOTH AT ONCE", b='A time can be <b>part exactly 0 and part continuous</b>: the CDF jumps and then rises, and the mean needs both parts.', f=[["30302", "jumps"], ["30303", "density"]], n=[["30501", "the mean of any random variable"]]),
}

FIX = build(CARDS)
