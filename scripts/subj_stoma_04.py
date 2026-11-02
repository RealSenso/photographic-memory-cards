"""StoMA topic 04 (functions of a random variable). Commute picture: ride time X in minutes, speed Y = distance / ride time."""
from commute_lib import *

SUBJECT = "StoMA"

def d1(c):
    g = lambda x: 100 - 0.0075 * (x - 120) ** 2
    r = math.sqrt((100 - 70) / 0.0075)
    return svg(c, ax(24, 112, 226, 14), N(226, 124, "x", 7, "end"), N(28, 18, "y = g(x)", 7.5, "start"),
        fn(g, 40, 200, 50, 1.1), dash(24, 70, 226, 70), N(222, 66, "y", 7.5),
        R(120 - r, 108, 2 * r, 4, "#d9dee7", .8), dash(120 - r, 70, 120 - r, 108), dash(120 + r, 70, 120 + r, 108),
        N(120, 124, "{x : g(x) ≤ y}", 7.5),
        N(30, 34, "F_Y(y) = ℙ(g(X) ≤ y)", 7.5, "start"), N(30, 46, "= ∫ f_X(x) dx over the shaded x", 7, "start"),
        N(120, 138, "ask the question about X, then differentiate in y", 7))

def d2(c):
    g = lambda x: 30 + 72 * math.exp(-(x - 40) / 55)
    xa, xb = 90, 110
    return svg(c, ax(24, 118, 226, 14), N(226, 130, "x (ride min)", 7, "end"), N(28, 18, "y = g(x) speed", 7, "start"),
        fn(g, 40, 220, 50, 1.1),
        dash(xa, 118, xa, g(xa)), dash(xb, 118, xb, g(xb)), dash(24, g(xa), xa, g(xa)), dash(24, g(xb), xb, g(xb)),
        N(100, 130, "dx", 7), N(18, (g(xa) + g(xb)) / 2 + 3, "dy", 7, "end"),
        N(140, 72, "f_Y(y) = f_X(x) |dx/dy|", 7.5, "start"), N(140, 84, "x = g⁻¹(y)", 7, "start"), N(140, 96, "|·| keeps it positive", 6.5, "start"),
        N(140, 108, "same area over dx and dy", 7, "start"))

def d3(c):
    g = lambda x: 100 - 0.0075 * (x - 120) ** 2
    r = math.sqrt((100 - 62) / 0.0075)
    return svg(c, ax(24, 112, 226, 14), N(226, 124, "x", 7, "end"), N(28, 18, "y = g(x)", 7.5, "start"),
        fn(g, 40, 200, 50, 1.1), dash(24, 62, 226, 62), N(222, 58, "y", 7.5),
        dash(120 - r, 62, 120 - r, 112), dash(120 + r, 62, 120 + r, 112),
        N(120 - r, 124, "x₁ = −√y", 7.5), N(120 + r, 124, "x₂ = +√y", 7.5),
        N(120, 34, "two rides give the same y", 7.5), N(120, 138, "f_Y(y) = ∑ f_X(xₖ)/|g′(xₖ)|, one term per branch", 7))

def d4(c):
    F = lambda x: 112 - 84 / (1 + math.exp(-(x - 100) / 20))
    u = 60
    xs = 100 + 20 * math.log((112 - u + 0) / (u - 28)) if False else None
    # solve F(x)=u numerically
    lo, hi = 24.0, 226.0
    for _ in range(40):
        m = (lo + hi) / 2
        if F(m) > u: lo = m
        else: hi = m
    xu = (lo + hi) / 2
    return svg(c, ax(24, 112, 226, 14), N(226, 124, "x", 7, "end"), N(28, 18, "F(x) = U", 7.5, "start"),
        fn(F, 24, 226, 50, 1.1), dash(24, u, xu, u), dash(xu, u, xu, 112),
        arrow(30, u + 14, 30, u + 2, 1) if False else "",
        N(30, u - 4, "U ~ Unif(0,1)", 7.5, "start"), N(xu, 124, "X = F⁻¹(U)", 7.5),
        N(150, 44, "pick U at random,", 7, "start"), N(150, 54, "read across, then down", 7, "start"),
        N(120, 138, "any F: X = F⁻¹(U) has the law F", 7))

def d5(c):
    return svg(c, ax(24, 112, 226, 14), N(226, 124, "y = z²", 7, "end"),
        fn(lambda x: 112 - 80 * 0.2 / math.sqrt(max((x - 24) / 40, 0.04)) * 0.9 if False else 112 - min(90, 16 / math.sqrt(max((x - 24) / 202 * 4, 0.02))) * math.exp(-(x - 24) / 202 * 4 / 2) * 1.0, 28, 226, 80, 1.1),
        N(30, 18, "f_Y(y) = e^(−y/2) / √(2πy)", 7.5, "start"), N(110, 44, "blows up at 0 but still", 7, "start"), N(110, 54, "has total area 1: y^(−½) is integrable", 6.5, "start"),
        N(110, 80, "Y = Z², Z ~ 𝒩(0,1)", 7.5, "start"), N(110, 92, "= χ₁² = Gamma(½, ½)", 7, "start"),
        N(120, 138, "squared deviation from typical ride: both signs fold onto y > 0", 6.5))

def d6(c):
    return svg(c,
        L(20, 40, 220, 40, 1), N(222, 36, "wall: x", 7, "end"), C(120, 112, 2.6), N(120, 124, "you (distance 1)", 7),
        arrow(120, 112, 168, 40, 1), N(144, 82, "Θ", 8, "start"), C(168, 40, 2.2), N(168, 32, "X = tan Θ", 7.5),
        N(30, 70, "ray at a random angle Θ", 7, "start"), N(30, 80, "Θ ~ Unif(−π/2, π/2)", 7, "start"),
        fn(lambda x: 112 - 30 / (1 + ((x - 190) / 14) ** 2), 150, 226, 40, 1.1) if False else "",
        N(30, 18, "f_X(x) = 1/(π(1 + x²))", 7.5, "start"), N(30, 96, "heavy tails: 𝔼[X] does not exist", 7, "start"),
        N(120, 138, "a GPS ping at a random angle lands tan Θ along the wall", 7))

CARDS = {
30401: dict(d=d1, kind="THEOREM",
  stmt=r"<b>CDF method.</b> Let $X$ be a random variable and $g:\mathbb R\to\mathbb R$ measurable, and put $Y=g(X)$. Then $F_Y(y)=\mathbb P(g(X)\le y)=\mathbb P\bigl(X\in\{x:g(x)\le y\}\bigr)$, which equals $\int_{\{x:g(x)\le y\}}f_X(x)\,dx$ when $X$ has density $f_X$. If $F_Y$ is differentiable, $f_Y(y)=\dfrac{d}{dy}F_Y(y)$ on the support of $Y$ (Ross 5.7; Grimmett 4.7).",
  hint="How do you find the law of a new quantity built from the ride time, without any formula to memorise?",
  bd=[r"<strong>$\{x:g(x)\le y\}$ = the rides that give a small enough $Y$.</strong> Turn the question about $Y$ into a question about which ride times $x$ qualify.",
      r"<strong>$\int_{\{x:g(x)\le y\}}f_X(x)\,dx$ = add up their chance.</strong> The shaded part of the ride-time axis carries its area under $f_X$.",
      r"<strong>$f_Y=\dfrac{d}{dy}F_Y$ = differentiate for the density.</strong> Do it only on the values $y$ that $Y$ can really take."],
  conn=r"<strong>From ride time to something else.</strong> Whatever you compute from the ride (speed, fare, minutes late), ask which ride times make it at most $y$, add up their chance, and you have the CDF of the new quantity.",
  cap="The curve y = g(x) and a level y. The shaded stretch of the x-axis is {x : g(x) ≤ y}, and the chance of that stretch under f_X is F_Y(y) = ℙ(g(X) ≤ y)."),
30402: dict(d=d2, kind="THEOREM",
  stmt=r"<b>Monotone change of variables.</b> If $g$ is strictly monotone and differentiable on the support of $X$, then $Y=g(X)$ has density $f_Y(y)=f_X(g^{-1}(y))\left|\frac{d}{dy}g^{-1}(y)\right|$ for $y\in g(\operatorname{supp}X)$ (Ross 5.7; Grimmett 4.7).",
  hint="If speed is distance over ride time, how does the density of the ride time turn into the density of the speed?",
  bd=[r"<strong>$f_X(g^{-1}(y))$ = density at the ride time that gives $y$.</strong> Undo $g$ to find which ride time $x$ produces speed $y$.",
      r"<strong>$|\frac{d}{dy}g^{-1}(y)|$ = how the axis stretches.</strong> A band $dy$ of speeds comes from a band $dx$ of ride times.",
      r"<strong>$|\cdot|$ = widths are positive.</strong> For decreasing $g$, $dx/dy$ is negative; the absolute value keeps the density non-negative."],
  conn=r"<strong>Minutes into speed.</strong> The chance in a band of ride times is the same chance in the matching band of speeds; the density changes by the stretch factor.",
  cap="A decreasing map y = g(x) from ride time x to speed y. A band dx at x maps to a band dy, and the same chance sits over both: f_Y(y) = f_X(x) |dx/dy| with x = g⁻¹(y)."),
30403: dict(d=d3, kind="THEOREM",
  stmt=r"<b>Many-to-one transformations.</b> Let $g$ be piecewise strictly monotone and differentiable, and let $y$ have preimages $x_1,\ldots,x_m$ with $g'(x_k)\ne0$. Then $f_Y(y)=\sum_{k}\dfrac{f_X(x_k)}{|g'(x_k)|}$. In particular for $Y=X^2$, $f_Y(y)=\dfrac{f_X(\sqrt y)+f_X(-\sqrt y)}{2\sqrt y}\,\mathbf 1_{\{y>0\}}$ (Ross 5.7; Grimmett 4.7).",
  hint="If two different values of X give the same Y, how do you count the chance at that Y?",
  bd=[r"<strong>$x_k\in g^{-1}(y)$ = every input that lands on $y$.</strong> For $Y=X^2$ both $+\sqrt y$ and $-\sqrt y$ do; one must find every real root.",
      r"<strong>$f_X(x_k)/|g'(x_k)|$ = one branch's contribution.</strong> Each branch is the one-dimensional change-of-variables term for that piece of $g$.",
      r"<strong>$\sum_k$ = add the branches.</strong> The chance at $y$ is the sum over branches; missing one gives a density that does not integrate to 1."],
  conn=r"<strong>Two ways to the same number.</strong> Deviation from the usual ride time: running 5 minutes early or 5 minutes late both give a squared deviation of 25. The chance of that squared value counts both.",
  cap="A U-shaped g(x). The level y is reached at two points x₁ = −√y and x₂ = +√y, and f_Y(y) adds one term f_X(xₖ)/|g′(xₖ)| for each branch."),
30404: dict(d=d4, kind="THEOREM",
  stmt=r"<b>Probability integral transform.</b> If $X$ has a continuous CDF $F_X$, then $U=F_X(X)\sim\mathrm{Unif}(0,1)$. Conversely, if $U\sim\mathrm{Unif}(0,1)$ and $F$ is any CDF with generalised inverse $F^{-1}(u)=\inf\{x:F(x)\ge u\}$, then $X=F^{-1}(U)$ has CDF $F$ (Ross 5.7; Grimmett 4.11).",
  hint="How can a computer generate ride times with a given law using only a uniform random number?",
  bd=[r"<strong>$U=F_X(X)$ = the CDF reading of a ride.</strong> Feed the ride time through its own CDF: the output is the share of mornings that were no longer than this one.",
      r"<strong>$U\sim\mathrm{Unif}(0,1)$ = that share is evenly spread.</strong> A randomly chosen morning is equally likely to be at any percentile (needs $F_X$ continuous, not discrete).",
      r"<strong>$X=F_X^{-1}(U)$ = run it backwards to simulate.</strong> Draw a uniform $U$, find the ride time at that percentile, and it has exactly the law $F_X$."],
  conn=r"<strong>Percentiles of the ride.</strong> A ride at the 80th percentile is longer than 80% of rides. Pick a random percentile, read off the ride time at it, and you have a simulated ride with the right law.",
  cap="Pick U at height on the y-axis, read across to the CDF F, then down to the x-axis: X = F⁻¹(U). A uniform U gives an X with the law F."),
30405: dict(d=d5, kind="THEOREM",
  stmt=r"<b>Chi-square with one degree of freedom.</b> If $Z\sim\mathcal N(0,1)$ then $Y=Z^2$ has density $f_Y(y)=\dfrac1{\sqrt{2\pi y}}e^{-y/2}\mathbf 1_{\{y>0\}}$, that is $Y\sim\chi^2_1=\mathrm{Gamma}\bigl(\tfrac12,\tfrac12\bigr)$. Proof: $F_Y(y)=\mathbb P(-\sqrt y\le Z\le\sqrt y)=2\Phi(\sqrt y)-1$ for $y>0$; differentiate (Ross 5.7; Grimmett 4.4).",
  hint="What law does the squared deviation of a standardised ride time follow, and why does its density blow up at zero?",
  bd=[r"<strong>$F_Y(y)=2\Phi(\sqrt y)-1$ = the middle strip of the bell.</strong> $Z^2\le y$ means $Z$ lies between $-\sqrt y$ and $\sqrt y$; both sides of the bell count.",
      r"<strong>$e^{-y/2}$ = the bell's fall-off.</strong> Large squared deviations are rare, and the bell curve cuts them off exponentially.",
      r"<strong>$1/\sqrt{2\pi y}$ = a pole at 0, but integrable.</strong> Small $y$ come from the dense centre of the bell, so the density is high near 0, yet the area is still 1."],
  conn=r"<strong>How far off, squared.</strong> Take the standardised deviation of your ride from usual and square it. Early or late both count as the same squared distance, so everything folds onto positive values, with a pile-up of near-zero deviations.",
  cap="The density f_Y(y) = e^(−y/2)/√(2πy) of Y = Z². It rises steeply towards y = 0 and decays exponentially, with total area 1: this is χ₁²."),
30406: dict(d=d6, kind="WORKED EXAMPLE",
  stmt=r"<b>Cauchy law from a random angle.</b> If $\Theta\sim\mathrm{Unif}(-\pi/2,\pi/2)$ and $X=\tan\Theta$, then $F_X(x)=\mathbb P(\Theta\le\arctan x)=\tfrac12+\tfrac1\pi\arctan x$ and $f_X(x)=\dfrac1{\pi(1+x^2)}$, the standard Cauchy density. Its tails are so heavy that $\int|x|f_X(x)\,dx=\infty$, so $\mathbb E[X]$ does not exist (Ross 5.7; Grimmett 4.4).",
  hint="If a ray leaves you at a uniformly random angle, where does it hit a wall, and why is its average undefined?",
  bd=[r"<strong>$\Theta\sim\mathrm{Unif}(-\pi/2,\pi/2)$ = a random direction.</strong> Every direction facing the wall is equally likely.",
      r"<strong>$X=\tan\Theta$ = where the ray meets the wall.</strong> With the wall at distance 1, the hit point is $\tan\Theta$ along it; near the sideways angles it shoots off to $\pm\infty$.",
      r"<strong>$f_X(x)=\frac{1}{\pi(1+x^2)}$ = heavy tails.</strong> The tails fall only like $1/x^2$, so the positive and negative halves of $\int xf_X$ are $+\infty$ and $-\infty$, and the mean is undefined."],
  conn=r"<strong>A GPS ping at a random angle.</strong> A ping that points anywhere in the half-circle ahead lands somewhere along the street wall. Most land near you, but a few land absurdly far away, and these far pings ruin any average.",
  cap="From you at distance 1, a ray at random angle Θ hits the wall at X = tan Θ. The resulting density 1/(π(1+x²)) has heavy tails, so 𝔼[X] does not exist."),
}

STORY = {
30401: dict(s="STORY 4 · STEP 1 · A NEW QUANTITY", b="To find the law of something <b>built from the ride time</b>, ask which ride times make it at most y, add their chance, then differentiate.", f=[["30301", "the CDF"], ["30303", "the density"]], n=[["30402", "a shortcut for one-to-one maps"], ["30404", "the CDF as a transformation"]]),
30402: dict(s="STORY 4 · STEP 2 · ONE TO ONE", b="When the map is strictly monotone, the CDF method collapses to <b>density times the stretch factor</b>.", f=[["30401", "the CDF method"]], n=[["30403", "when the map folds"], ["30902", "the same stretch in 2D"]]),
30403: dict(s="STORY 4 · STEP 3 · FOLDED MAPS", b="If several inputs give the same output, the density is a <b>sum over branches</b>.", f=[["30402", "one branch"]], n=[["30405", "the square of a normal"]]),
30404: dict(s="STORY 4 · STEP 4 · THE UNIFORM KEY", b="Every continuous law is the <b>uniform law pushed through F⁻¹</b>, which is how simulation works.", f=[["30401", "the CDF method"]], n=[["30904", "Box–Muller simulation"], ["32204", "accept–reject style sampling"]]),
30405: dict(s="STORY 4 · STEP 5 · SQUARED DEVIATION", b="Squaring a standard normal folds both signs together and gives the <b>χ² density</b>.", f=[["30305", "the standard normal"], ["30403", "folded maps"]], n=[["30905", "sums of squares stay in the family"]]),
30406: dict(s="STORY 4 · STEP 6 · A DENSITY WITH NO MEAN", b="A random angle through tan gives the <b>Cauchy law</b>, with tails so heavy that the mean does not exist.", f=[["30402", "monotone transformation"]], n=[["31706", "the law of large numbers fails for Cauchy"]]),
}

FIX = build(CARDS)
