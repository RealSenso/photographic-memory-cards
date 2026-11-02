"""StoMA topic 05 (expectation, variance, moments, generating functions). Commute picture: walk + wait + ride add up to the trip."""
from commute_lib import *

SUBJECT = "StoMA"
BELL = lambda x: 112 - 70 * math.exp(-((x - 110) ** 2) / 1500)

def d1(c):
    return svg(c, ax(24, 84, 226, 14), N(226, 95, "x min", 7, "end"), N(28, 18, "f(x)", 7.5, "start"),
        fn(lambda x: 84 - 60 * math.exp(-((x - 100) ** 2) / 1800), 24, 226, 60, 1.1),
        L(100, 84, 100, 76, 1), N(100, 94, "𝔼[X]", 7.5), 
        N(120, 22, "𝔼[g(X)] = ∫ g(x) f(x) dx", 7.5),
        R(24, 104, 54, 16, "#f1f5f9", 1, 2), N(51, 115, "walk 𝔼[A]", 7), R(78, 104, 66, 16, "#e5e9f0", 1, 2), N(111, 115, "wait 𝔼[W]", 7), R(144, 104, 76, 16, "#d9dee7", 1, 2), N(182, 115, "ride 𝔼[R]", 7),
        N(120, 134, "𝔼[∑cᵢXᵢ] = ∑cᵢ𝔼[Xᵢ]: means add, always", 7))

def d2(c):
    S = lambda x: 112 - 80 * math.exp(-(x - 24) / 60)
    return svg(c, ax(24, 112, 226, 14), N(226, 124, "t min", 7, "end"), N(28, 18, "ℙ(X > t)", 7.5, "start"),
        area(S, 24, 200, 112, 40), fn(S, 24, 226, 50, 1.1),
        N(120, 80, "area = 𝔼[X] = ∫ ℙ(X > t) dt", 7.5, "start"),
        N(150, 44, "∑ ℙ(X ≥ k) for counts", 7, "start"), N(120, 138, "average ride = area under “still riding after t”", 7))

def d3(c):
    return svg(c,
        R(40, 22, 70, 70, "#f1f5f9", 1), R(110, 22, 50, 70, "#e5e9f0", 1), R(40, 92, 70, 50, "#e5e9f0", 1) if False else "",
        N(75, 60, "Var X", 8), N(135, 60, "Cov(X,Y)", 7.5), N(75, 108, "Cov", 7.5), N(135, 108, "Var Y", 8),
        L(110, 22, 110, 120, 1), L(40, 92, 160, 92, 1), R(40, 22, 120, 98, "none", 1),
        N(75, 16, "X: wait", 7), N(135, 16, "Y: ride", 7), N(172, 62, "Var(X+Y)", 7.5, "start"), N(172, 74, "= Var X + Var Y", 7, "start"), N(172, 85, "+ 2 Cov(X,Y)", 7, "start"),
        N(120, 138, "variance of a total = squares plus cross terms", 7))

def d4(c):
    M = lambda t: 112 - 20 * math.exp(1.4 * (t - 120) / 60) * 1.0 + 0
    MM = lambda x: 90 - 14 * (x - 100) / 20 - 0 if False else 112 - 14 * math.exp((x - 90) / 32)
    return svg(c, ax(24, 112, 226, 14), N(226, 124, "t", 7.5, "end"), N(28, 18, "M(t)", 7.5, "start"),
        fn(lambda x: 112 - 24 * math.exp((x - 90) / 40), 24, 200, 50, 1.1), C(90, 88, 2.4), N(90, 124, "0", 7),
        dash(24, 88, 90, 88), N(20, 91, "1", 7, "end"), L(60, 98, 130, 78, 1, "4 3"), 
        N(30, 50, "slope at 0 = 𝔼[X]", 7, "start"), N(30, 62, "curvature at 0 = 𝔼[X²]", 7, "start"),
        N(30, 34, "M(t) = 𝔼[e^(tX)]", 7.5, "start"), N(120, 138, "independent legs: multiply their M(t); M fixes the law", 6.5))

def d5(c):
    G = lambda s: 112 - 84 * (0.2 + 0.5 * (s - 24) / 144 + 0.3 * ((s - 24) / 144) ** 2)
    return svg(c, ax(24, 112, 226, 14), N(226, 124, "s", 7.5, "end"), N(28, 18, "G(s)", 7.5, "start"),
        fn(G, 24, 168, 40, 1.1), C(24, f(G(24)), 2.4), N(30, G(24) + 12, "G(0) = ℙ(X = 0)", 7, "start"),
        C(168, f(G(168)), 2.4), N(168, 124, "1", 7.5), dash(168, 112, 168, G(168)), dash(24, G(168), 168, G(168)),
        N(150, 76, "slope at s = 1:", 7, "start"), N(150, 86, "G′(1) = 𝔼[X]", 7, "start"),
        N(30, 46, "G(s) = 𝔼[s^X] = ∑ ℙ(X = k) sᵏ", 7.5, "start"),
        N(120, 138, "N stops, X boarders each: G(s) = Gₙ(Gₓ(s))", 7))

def d6(c):
    pts = [(-3, 9), (-2, 4), (-1, 1), (0, 0), (1, 1), (2, 4), (3, 9)]
    X = lambda v: 120 + v * 22
    Y = lambda v: 112 - v * 9
    out = ax(24, 112, 226, 14) + N(226, 124, "X: minutes off usual", 7, "end") + N(28, 18, "Y = X²", 7.5, "start")
    out += fn(lambda x: Y(((x - 120) / 22) ** 2), 54, 186, 50, 1.1)
    for u, v in pts:
        out += C(X(u), Y(v), 2)
    out += L(40, 80, 200, 80, 1, "4 3") + N(200, 74, "best straight line: flat", 6.5, "end")
    out += N(120, 22, "Cov(X, X²) = 𝔼[X³] − 𝔼[X]𝔼[X²] = 0", 7)
    out += N(120, 138, "ℙ(X=0, Y=1) = 0 ≠ ℙ(X=0)ℙ(Y=1): dependent", 6.5)
    return svg(c, out)

CARDS = {
30501: dict(d=d1, kind="THEOREM",
  stmt=r"<b>LOTUS and linearity of expectation.</b> If $X$ has density $f_X$ (or pmf $p_X$) and $\mathbb E|g(X)|<\infty$, then $\mathbb E[g(X)]=\int_{-\infty}^\infty g(x)f_X(x)\,dx$ (respectively $\sum_xg(x)p_X(x)$). For random variables $X_1,\ldots,X_n$ with finite means and constants $c_i$, $\mathbb E\bigl[\sum_ic_iX_i\bigr]=\sum_ic_i\mathbb E[X_i]$, with no independence needed (Ross 4.4, 7.2; Grimmett 3.3).",
  hint="Can you add the average of the walk, the wait and the ride to get the average trip, and do you need to know the law of the sum?",
  bd=[r"<strong>$\int g(x)f_X(x)\,dx$ = weight each value by its density.</strong> To average a function of the ride time, you do not need the law of $g(X)$: use the density of $X$ itself.",
      r"<strong>$\sum_ic_i\mathbb E[X_i]$ = means add up.</strong> The mean of walk plus wait plus ride is the sum of the three means, whatever the pieces are.",
      r"<strong>No independence needed.</strong> Linearity holds even if a long wait and a long ride tend to come together; only variances care about that link."],
  conn=r"<strong>The average trip is the sum of the average parts.</strong> Average walk, average wait, average ride: add them and you have the average door-to-door time, with no need to know how the three are tangled together.",
  cap="The density f(x) of one leg, with its mean 𝔼[X] marked. Below, the average walk, wait and ride lie end to end: 𝔼[∑cᵢXᵢ] = ∑cᵢ𝔼[Xᵢ]."),
30502: dict(d=d2, kind="THEOREM",
  stmt=r"<b>Tail-sum formula.</b> If $X\ge0$ then $\mathbb E[X]=\int_0^\infty\mathbb P(X>t)\,dt$. If $X$ takes values in $\{0,1,2,\ldots\}$ then $\mathbb E[X]=\sum_{k=1}^\infty\mathbb P(X\ge k)$. For general $X$, $\mathbb E[X]=\int_0^\infty\mathbb P(X>t)\,dt-\int_{-\infty}^0\mathbb P(X<t)\,dt$ (Ross 5.3; Grimmett 4.3).",
  hint="How can the average ride be read as an area under the curve “still on the bus after t minutes”?",
  bd=[r"<strong>$\mathbb P(X>t)$ = chance the ride is still going at minute $t$.</strong> It starts at 1 and falls to 0 as $t$ grows.",
      r"<strong>$\int_0^\infty\ldots dt$ = the area under that curve.</strong> Each minute $t$ contributes the chance that the ride lasts at least that long.",
      r"<strong>$=\mathbb E[X]$ = the area is the mean.</strong> Slicing the ride time into minutes instead of values gives the same average; for counts, $\sum_{k\ge1}\mathbb P(X\ge k)$."],
  conn=r"<strong>Counting rider-minutes.</strong> Each minute of a typical day, you ask whether the ride is still going. Adding up those yes-chances minute by minute gives the average ride length.",
  cap="The survival curve ℙ(X > t) of the ride time. The shaded area under it equals 𝔼[X] = ∫ℙ(X > t)dt; for counts, the sum ∑ℙ(X ≥ k)."),
30503: dict(d=d3, kind="THEOREM",
  stmt=r"<b>Variance of a sum.</b> For $X_1,\ldots,X_n$ with finite second moments, $\operatorname{Var}\!\left(\sum_{i=1}^nX_i\right)=\sum_{i=1}^n\operatorname{Var}(X_i)+2\sum_{i<j}\operatorname{Cov}(X_i,X_j)$, where $\operatorname{Var}(X)=\mathbb E[(X-\mathbb EX)^2]$ and $\operatorname{Cov}(X,Y)=\mathbb E[(X-\mathbb EX)(Y-\mathbb EY)]$. If the $X_i$ are independent (or just uncorrelated) the covariance terms vanish (Ross 7.4; Grimmett 3.6).",
  hint="If your wait and your ride tend to be long on the same mornings, what does the variance of the total look like?",
  bd=[r"<strong>$\sum\operatorname{Var}(X_i)$ = each piece's own spread.</strong> The squares on the diagonal: how much each leg of the trip varies by itself.",
      r"<strong>$\operatorname{Cov}(X_i,X_j)$ = how two legs move together.</strong> Positive if long waits come with long rides, negative if one makes up for the other.",
      r"<strong>$2\sum_{i<j}$ = every pair appears twice.</strong> Expanding $(\sum X_i)^2$ gives each cross term $X_iX_j$ and $X_jX_i$, so the covariances are doubled."],
  conn=r"<strong>A bad morning stacks up.</strong> If rain makes the wait longer and the ride longer, the total trip varies more than the pieces suggest: the covariance term adds to the variance. Independent legs would just add their variances.",
  cap="Expand (X + Y)² as a square of sides X (wait) and Y (ride): Var X, Var Y on the diagonal and Cov(X,Y) twice off it, so Var(X+Y) = Var X + Var Y + 2Cov(X,Y)."),
30504: dict(d=d4, kind="DEFINITION",
  stmt=r"<b>Moment generating function.</b> The MGF of $X$ is $M_X(t)=\mathbb E[e^{tX}]$ for $t$ in an interval around $0$ where it is finite. Then $M_X(t)=\sum_{k\ge0}\frac{t^k}{k!}\mathbb E[X^k]$, $M_X^{(k)}(0)=\mathbb E[X^k]$, and if $M_X$ is finite near $0$ it determines the law of $X$. For independent $X,Y$: $M_{X+Y}(t)=M_X(t)M_Y(t)$ (Ross 7.7; Grimmett 5.1).",
  hint="How can one function of t store every moment of the ride time and turn a sum of independent legs into a product?",
  bd=[r"<strong>$\mathbb E[e^{tX}]$ = the average exponential tilt of the ride.</strong> Weight each ride time by $e^{tx}$ and average: long rides count more as $t$ grows.",
      r"<strong>$\sum\frac{t^k}{k!}\mathbb E[X^k]$ = the moments are the Taylor coefficients.</strong> The slope at $t=0$ is the mean $\mathbb E[X]$ and the curvature gives $\mathbb E[X^2]$.",
      r"<strong>$M_{X+Y}=M_XM_Y$ = sums become products.</strong> For independent legs of the trip, the MGF of the total is the product of the MGFs; it needs to exist near 0 for uniqueness."],
  conn=r"<strong>One curve for the whole ride.</strong> Instead of remembering the average, the spread and every higher feature of the ride time, you keep one curve that holds them all, and for two independent legs you multiply their curves.",
  cap="The MGF M(t) = 𝔼[e^(tX)] passes through 1 at t = 0. Its slope there is 𝔼[X] and its curvature is 𝔼[X²]; for independent legs, M of the total is the product."),
30505: dict(d=d5, kind="DEFINITION",
  stmt=r"<b>Probability generating function.</b> For $X$ taking values in $\{0,1,2,\ldots\}$, $G_X(s)=\mathbb E[s^X]=\sum_{k\ge0}\mathbb P(X=k)s^k$ for $|s|\le1$. Then $G_X(0)=\mathbb P(X=0)$, $G_X(1)=1$, $\mathbb E[X]=G_X'(1)$, and for independent $X_i$ with $N$ independent of them, $G_{\sum_{i=1}^NX_i}(s)=G_N\bigl(G_X(s)\bigr)$ (Ross 7.7; Grimmett 5.1).",
  hint="How can a polynomial in s hold the whole count distribution, and how do you read the average off it?",
  bd=[r"<strong>$\sum\mathbb P(X=k)s^k$ = the count's law as a polynomial.</strong> The coefficient of $s^k$ is the chance of exactly $k$ boarders.",
      r"<strong>$G_X(0)=\mathbb P(X=0)$ and $G_X(1)=1$ = the endpoints.</strong> At $s=0$ only the empty count survives; at $s=1$ the chances add to 1.",
      r"<strong>$\mathbb E[X]=G_X'(1)$ = the mean is the slope at 1.</strong> Differentiate at $s=1$, not at 0; plugging $G_X$ into $G_N$ handles a random number of terms."],
  conn=r"<strong>Counting boarders.</strong> The number of passengers boarding at a stop is a whole number. A polynomial whose coefficients are the chances of 0, 1, 2, ... boarders holds the whole picture; its slope at 1 is the average crowd.",
  cap="The PGF G(s) = ∑ℙ(X = k)sᵏ rises from ℙ(X = 0) at s = 0 to 1 at s = 1. Its slope G′(1) at the right end is 𝔼[X]."),
30506: dict(d=d6, kind="WORKED EXAMPLE",
  stmt=r"<b>Uncorrelated but dependent.</b> Let $X$ be symmetric about $0$ with finite third moment (say uniform on $\{-1,0,1\}$) and $Y=X^2$. Then $\mathbb E[X]=\mathbb E[X^3]=0$, so $\operatorname{Cov}(X,Y)=\mathbb E[X^3]-\mathbb E[X]\mathbb E[X^2]=0$, yet $Y$ is a function of $X$. For $X$ uniform on $\{-1,0,1\}$: $\mathbb P(X=0,Y=1)=0\ne\tfrac13\cdot\tfrac23=\mathbb P(X=0)\mathbb P(Y=1)$, so $X,Y$ are not independent (Ross 7.4; Grimmett 3.6).",
  hint="Can Y be completely determined by X and yet have zero covariance with it?",
  bd=[r"<strong>$\mathbb E[X]=0,\ \mathbb E[X^3]=0$ = the odd moments vanish.</strong> If early and late deviations balance, every odd power averages out to 0.",
      r"<strong>$\operatorname{Cov}(X,X^2)=\mathbb E[X^3]-\mathbb E[X]\mathbb E[X^2]=0$ = no straight-line link.</strong> Covariance only sees how closely the points follow a line; the parabola has a flat best line.",
      r"<strong>$\mathbb P(X=0,X^2=1)=0\ne\tfrac13\cdot\tfrac23$ = still dependent.</strong> Knowing $X=0$ tells you $Y=0$ for certain, so independence fails."],
  conn=r"<strong>Early or late, both are off.</strong> Take minutes away from your usual arrival, and the size of the miss. Being early is as likely as being late, so the two numbers show no straight-line link, though the size is set exactly by the deviation.",
  cap="Points (X, Y = X²) lie on a parabola, yet the best straight line through them is flat, so Cov(X, X²) = 0 although Y is fixed by X."),
}

STORY = {
30501: dict(s="STORY 5 · STEP 1 · THE AVERAGE", b="The <b>mean</b> weights each value by its density, and <b>means always add</b>, whatever the dependence between the pieces.", f=[["30303", "the density"], ["30306", "atoms and densities together"]], n=[["30502", "reading the mean as an area"], ["30503", "how spreads add"]]),
30502: dict(s="STORY 5 · STEP 2 · THE MEAN AS AN AREA", b="The mean of a non-negative quantity is the <b>area under its survival curve</b>.", f=[["30501", "expectation"]], n=[["30601", "Markov's inequality"]]),
30503: dict(s="STORY 5 · STEP 3 · SPREAD", b="Variances add only up to <b>cross terms</b>: covariance measures how legs move together.", f=[["30501", "linearity of means"]], n=[["30506", "zero covariance is not independence"], ["30602", "Chebyshev"], ["31101", "covariance matrices"]]),
30504: dict(s="STORY 5 · STEP 4 · ONE FUNCTION FOR ALL MOMENTS", b="The <b>MGF</b> stores every moment and turns independent sums into products.", f=[["30501", "moments from expectations"]], n=[["30603", "Chernoff bound"], ["31404", "MGF of a random sum"]]),
30505: dict(s="STORY 5 · STEP 5 · COUNTS", b="For whole-number counts, the <b>PGF</b> is the same idea: a polynomial whose coefficients are the chances.", f=[["30302", "the PMF"], ["30504", "the MGF idea"]], n=[["31404", "composition for random sums"], ["31405", "branching processes"]]),
30506: dict(s="STORY 5 · STEP 6 · THE TRAP", b="<b>Uncorrelated does not mean independent</b>: Y = X² is fixed by X yet has zero covariance with it.", f=[["30503", "covariance"]], n=[["31303", "where it does hold: jointly Gaussian"]]),
}

FIX = build(CARDS)
