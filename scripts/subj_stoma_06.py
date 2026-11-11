"""StoMA topic 06 (inequalities). F1 picture: how bad can a pit stop or a lap get, using only the average and the spread."""
from f1_lib import *

SUBJECT = "StoMA"

def d1(c):
    out = ax(24, 112, 226, 14) + N(226, 124, "x s", 7, "end")
    out += fn(lambda x: 112 - x * 0 - (x - 24) * 0.46 if False else 112 - 0.5 * (x - 24), 24, 200, 20, 1.1)
    out += N(34, 22, "X", 7.5, "start")
    out += L(130, 112, 130, 56, 1) + dash(130, 56, 24, 56) if False else ""
    out += L(24, 112, 130, 112, 1.6) + L(130, 112, 226, 112, 1.6)
    out += L(130, 112, 130, 52, 1, "4 3") + N(130, 124, "a", 7.5)
    out += L(130, 52, 226, 52, 1.2) + N(222, 46, "a·1{X ≥ a}", 7, "end")
    out += N(34, 38, "line = X", 7, "start") + N(34, 48, "step = a·1{X ≥ a} stays under it", 6.5, "start")
    out += N(120, 138, "ℙ(X ≥ a) ≤ 𝔼[X]/a: only for X ≥ 0", 7.5)
    return svg(c, out)

def d2(c):
    B = lambda x: 112 - 80 * math.exp(-((x - 120) ** 2) / 1200)
    return svg(c, ax(24, 112, 226, 14), N(226, 124, "x", 7, "end"), fn(B, 24, 226, 60, 1.1),
        area(B, 24, 66, 112, 12), area(B, 174, 226, 112, 12),
        dash(120, 112, 120, 30), N(120, 124, "μ", 8), dash(66, 112, 66, 90), dash(174, 112, 174, 90),
        N(66, 124, "μ − ε", 7), N(174, 124, "μ + ε", 7),
        N(120, 22, "ℙ(|X − μ| ≥ ε) ≤ Var(X)/ε²", 7.5),
        N(50, 80, "tail", 7), N(196, 80, "tail", 7),
        N(120, 138, "big spread σ² lets more of the laps reach the tails", 7))

def d3(c):
    h = lambda t: 82 - 0.0045 * (t - 120) ** 2
    return svg(c, ax(24, 112, 226, 14), N(226, 124, "t", 7.5, "end"), N(28, 18, "e^(−ta) M(t)", 7.5, "start"),
        fn(h, 40, 200, 60, 1.1), C(120, 82, 2.4), dash(120, 82, 120, 112), N(120, 124, "t*", 8),
        N(120, 74, "min over t > 0", 7, "middle") if False else N(150, 98, "inf over t > 0", 7, "start"),
        N(30, 40, "every t > 0 gives a valid bound:", 7, "start"), N(30, 50, "keep the smallest", 7, "start"),
        N(120, 138, "ℙ(X ≥ a) ≤ inf e^(−ta) M(t) = e^(−Λ*(a))", 7))

def d4(c):
    g = lambda x: 100 - 0.0038 * (x - 120) ** 2
    xa, xb, xm = 60, 180, 120
    ya, yb = g(xa), g(xb)
    return svg(c, ax(24, 118, 226, 14), N(226, 130, "x", 7, "end"), N(28, 18, "g(x) convex", 7.5, "start"),
        fn(g, 40, 205, 50, 1.1), L(xa, ya, xb, yb, 1, "4 3"), C(xa, ya, 2), C(xb, yb, 2),
        C(xm, ya, 2.4), N(xm + 6, ya - 4, "𝔼[g(X)]", 7.5, "start"),
        C(xm, g(xm), 2.4, "#ffffff"), N(xm + 6, g(xm) + 9, "g(𝔼[X])", 7.5, "start"),
        dash(xm, g(xm), xm, 118), N(xm, 129, "𝔼[X]", 7.5),
        N(30, 40, "convex: the chord lies above the curve", 7, "start"))

def d5(c):
    return svg(c,
        arrow(40, 80, 110, 80, 1), arrow(40, 80, 90, 34, 1), N(112, 84, "X", 8, "start"), N(88, 30, "Y", 8, "end"),
        N(60, 68, "θ", 7), N(40, 106, "|𝔼[XY]| ≤ √(𝔼X² 𝔼Y²)", 7, "start"), N(40, 118, "= cos θ ≤ 1", 7, "start"),
        ax(140, 100, 226, 20), N(226, 112, "t", 7, "end"), N(144, 24, "ℙ(sum ≥ t)", 7, "start"),
        fn(lambda x: 100 - 74 * math.exp(-(x - 140) / 20), 140, 226, 30, 1.1),
        N(184, 50, "≤ exp(−2t²/∑(bᵢ−aᵢ)²)", 6.5, "start") if False else N(226, 62, "exp(−2t²/∑(bᵢ−aᵢ)²)", 6.5, "end"),
        N(120, 138, "angle bound for products; exponential bound for sums of bounded losses", 6.5))

def d6(c):
    return svg(c, ax(24, 112, 226, 14), N(226, 124, "n races", 7, "end"), N(28, 18, "bound on ℙ(Sₙ ≥ ¾n)", 7, "start"),
        fn(lambda x: 112 - min(88, 4 / (1 + (x - 24) / 5.4) * 15.5), 28, 226, 80, 1.1), N(120, 40, "4/n Chebyshev", 7.5, "start"),
        fn(lambda x: 112 - 84 * math.exp(-(x - 24) / 40), 24, 226, 60, 1.1, "4 3"), N(120, 94, "e^(−n/8) Chernoff", 7.5, "start"),
        N(120, 138, "the exponential bound wins as the races pile up", 7))

CARDS = {
30601: dict(d=d1, kind="THEOREM",
  stmt=r"<b>Markov's inequality.</b> If $X\ge0$ is a random variable with finite mean and $a>0$, then $\mathbb P(X\ge a)\le\dfrac{\mathbb E[X]}{a}$. Proof: $a\mathbf 1_{\{X\ge a\}}\le X$ pointwise; take expectations. For general $X$, apply the bound to $|X|$, $(X-\mu)^2$ or $e^{tX}$ (Ross 8.2; Grimmett 7.3).",
  hint='Knowing only the average pit-stop time, what is the most you can say about the chance of a really slow stop?',
  bd=[r"<strong>$a\mathbf 1_{\{X\ge a\}}\le X$ = a step stays under the line.</strong> The step is $0$ for stops under $a$ seconds and $a$ for stops of at least $a$; the stop time $X$ itself lies above both pieces.",
      r"<strong>$\mathbb E[X]$ = the average stop.</strong> Taking the average of both sides gives $a\,\mathbb P(X\ge a)\le\mathbb E[X]$: the step's average is $a$ times the tail chance.",
      r"<strong>$\mathbb P(X\ge a)\le\mathbb E[X]/a$ = a slow stop cannot be common.</strong> At most a share $\mathbb E[X]/a$ of stops reach $a$ seconds, whatever the shape of the law (it needs $X\ge0$)."],
  conn="<strong>Slow stops cannot be everywhere.</strong> If Red Bull's stops average 2.5 seconds, at most one stop in three can take 7.5 seconds or more, however the rest are spread. It is a crude but always valid ceiling.",
  cap='The line y = X and the step a·1{X ≥ a}, which stays under it, for the pit-stop time X. Averaging both gives a·ℙ(X ≥ a) ≤ 𝔼[X], so ℙ(X ≥ a) ≤ 𝔼[X]/a.'),
30602: dict(d=d2, kind="THEOREM",
  stmt=r"<b>Chebyshev's inequality.</b> If $X$ has finite mean $\mu$ and variance $\sigma^2$, then for every $\varepsilon>0$, $\mathbb P(|X-\mu|\ge\varepsilon)\le\dfrac{\operatorname{Var}(X)}{\varepsilon^2}$. Equivalently $\mathbb P(|X-\mu|\ge k\sigma)\le1/k^2$. It is Markov's inequality applied to $(X-\mu)^2$ (Ross 8.2; Grimmett 7.3).",
  hint="Knowing the average and the spread of Max's lap time, how likely is a lap far from the average?",
  bd=[r"<strong>$|X-\mu|\ge\varepsilon$ = the lap is far from usual.</strong> More than $\varepsilon$ seconds off the average, faster or slower: the two shaded tails.",
      r"<strong>$\operatorname{Var}(X)$ = the spread.</strong> A bigger variance means more laps reach the tails, so the bound is larger.",
      r"<strong>$1/\varepsilon^2$ = farther is rarer.</strong> Doubling the distance cuts the bound by four: it is Markov on $(X-\mu)^2$, with no shape assumed."],
  conn='<strong>How far from a typical lap.</strong> With an average of 92.0 s and a spread of 0.3 s, a lap more than 0.9 s off (three spreads) happens on at most a ninth of laps, whatever the shape.',
  cap='A lap-time distribution with centre μ. The two tails beyond μ ± ε are the laps with |X − μ| ≥ ε, and their total chance is at most Var(X)/ε².'),
30603: dict(d=d3, kind="THEOREM",
  stmt=r"<b>Chernoff bound.</b> If $M_X(t)=\mathbb E[e^{tX}]$ is finite for some $t>0$, then for every $a$, $\mathbb P(X\ge a)\le\inf_{t>0}e^{-ta}M_X(t)=\exp\bigl(-\sup_{t>0}[ta-\Lambda_X(t)]\bigr)$, where $\Lambda_X=\ln M_X$. For the lower tail, use $t<0$ (Ross 8.3; Grimmett 5.11).",
  hint="How do you squeeze the best possible bound on a very slow pit stop out of Markov's inequality?",
  bd=[r"<strong>$e^{-ta}M_X(t)$ = Markov applied to $e^{tX}$.</strong> The event $X\ge a$ is the same as $e^{tX}\ge e^{ta}$ for $t>0$, so Markov gives this bound for each $t$.",
      r"<strong>$\inf_{t>0}$ = keep the best $t$.</strong> Every $t>0$ gives a valid bound; the smallest one is the tightest, at the bottom of the bowl.",
      r"<strong>$\exp(-\sup[ta-\Lambda_X(t)])$ = the exponential rate.</strong> The tail falls exponentially, at a rate set by the log-MGF; $t>0$ is needed for an upper tail."],
  conn='<strong>Tuning the ceiling.</strong> The engineers try different ways of weighing slow stops in the average, each giving a valid ceiling on “a stop this slow”. The smallest ceiling over all weights is the one they keep, and it often shrinks exponentially.',
  cap="The bound e^(−ta)M(t) as a function of t is a bowl. Each t > 0 is a valid ceiling on ℙ(X ≥ a), and the Chernoff bound is the minimum at t*."),
30604: dict(d=d4, kind="THEOREM",
  stmt=r"<b>Jensen's inequality.</b> If $g$ is convex and $X$ and $g(X)$ are integrable, then $g(\mathbb E[X])\le\mathbb E[g(X)]$. If $g$ is concave, $\mathbb E[g(X)]\le g(\mathbb E[X])$. Equality holds for non-degenerate $X$ only if $g$ is affine on the support of $X$. For $g=\ln$ this gives the AM–GM inequality (Ross 8.5; Grimmett 6.6).",
  hint='Is the average of a convex function of the lap time bigger or smaller than the function of the average lap?',
  bd=[r"<strong>$g(\mathbb E[X])$ = apply $g$ after averaging.</strong> The point on the curve above the average lap time.",
      r"<strong>$\mathbb E[g(X)]$ = average after applying $g$.</strong> This is a point on the chord between the values: for a convex curve the chord lies above the curve.",
      r"<strong>$\le$ = convex curves lie below their chords.</strong> Spread pushes the average of $g(X)$ up; for a concave $g$ like $\ln$ the direction flips."],
  conn='<strong>Averages do not pass through curves.</strong> The average of the squared seconds off the pace is bigger than the square of the average seconds off, because the very bad laps are weighted extra by the squaring.',
  cap='A convex curve g and two lap times with the chord between them. The point 𝔼[g(X)] on the chord lies above g(𝔼[X]) on the curve.'),
30605: dict(d=d5, kind="THEOREM",
  stmt=r"<b>Cauchy–Schwarz and Hoeffding.</b> For $X,Y$ with finite second moments, $|\mathbb E[XY]|^2\le\mathbb E[X^2]\,\mathbb E[Y^2]$. If $X_1,\ldots,X_n$ are independent with $a_i\le X_i\le b_i$, then for $t>0$, $\mathbb P\!\left(\sum_{i=1}^n(X_i-\mathbb EX_i)\ge t\right)\le\exp\!\left(-\dfrac{2t^2}{\sum_i(b_i-a_i)^2}\right)$ (Ross 8.5; Grimmett 7.3, 12.2).",
  hint='How do you bound the average of a product, and the chance that a sum of bounded losses strays far above its mean?',
  bd=[r"<strong>$|\mathbb E[XY]|^2\le\mathbb E[X^2]\mathbb E[Y^2]$ = the inner product is at most the product of lengths.</strong> Random variables act as vectors, and the cosine of the angle between them is at most 1.",
      "<strong>$b_i-a_i$ = the range of loss $i$.</strong> Each lap's time lost in traffic is confined to an interval of that width.",
      r"<strong>$\exp(-2t^2/\sum(b_i-a_i)^2)$ = an exponential bound for the sum.</strong> Independent bounded losses can only add up to a large excess with exponentially small chance."],
  conn='<strong>Many small, bounded losses.</strong> If each lap in traffic costs Max between 0 and 0.2 seconds and the laps are independent, the total loss rarely ends far above its average: the chance falls off exponentially with the excess.',
  cap="Left: random variables X and Y as arrows at angle θ, so |𝔼[XY]| is at most the product of their lengths. Right: Hoeffding's exponential bound on ℙ(sum − mean ≥ t)."),
30606: dict(d=d6, kind="WORKED EXAMPLE",
  stmt=r"<b>Chebyshev against Chernoff.</b> Let $S_n$ be the number of heads in $n$ tosses of a fair coin. Chebyshev gives $\mathbb P(S_n\ge\tfrac34n)\le\mathbb P(|S_n-\tfrac n2|\ge\tfrac n4)\le\dfrac{n/4}{(n/4)^2}=\dfrac4n$. Hoeffding (Chernoff) gives $\mathbb P(S_n\ge\tfrac34n)\le\exp\!\bigl(-\tfrac{2(n/4)^2}{n}\bigr)=e^{-n/8}$. The second decays exponentially, the first only like $1/n$ (Ross 8.2; Grimmett 7.3).",
  hint='Over a long run of races, which bound on a freak run of wins shrinks faster: the 1/n or the exponential one?',
  bd=[r"<strong>$\mathbb P(S_n\ge\tfrac34n)$ = a freak run.</strong> Over $n$ races, $S_n$ counts the wins of a driver who wins each race with chance $\tfrac12$; the event is far more wins than the half you expect.",
      '<strong>$4/n$ = Chebyshev, from the variance alone.</strong> It uses only the mean and spread, so it falls slowly, like one over the number of races.',
      '<strong>$e^{-n/8}$ = Chernoff/Hoeffding, using the whole MGF.</strong> It exploits that independent races partly cancel, and shrinks exponentially.'],
  conn="<strong>How rare is a freak season?</strong> For a driver who wins half his races, after 100 races Chebyshev says winning three quarters of them has chance at most 4%, while the exponential bound says about one in a quarter of a million. More information gives a much sharper ceiling, which is why runs like Max's 2023 season say the car is genuinely faster.",
  cap='The bounds on ℙ(Sₙ ≥ ¾n) as the number of races n grows. The Chebyshev bound 4/n falls slowly, the Chernoff bound e^(−n/8) (dashed) falls exponentially.'),
}

STORY = {
30601: dict(s="STORY 6 · STEP 1 · THE CEILING FROM THE MEAN", b="Knowing only the average, <b>Markov</b> caps the chance of an extreme: it cannot be common.", f=[["30502", "the mean as an area"]], n=[["30602", "adding the spread"]]),
30602: dict(s="STORY 6 · STEP 2 · ADD THE SPREAD", b="With the variance too, <b>Chebyshev</b> caps the chance of being far from the average.", f=[["30601", "Markov"], ["30503", "variance"]], n=[["30603", "using the whole MGF"], ["31701", "the weak law"]]),
30603: dict(s="STORY 6 · STEP 3 · TIGHTEN WITH THE MGF", b="Applying Markov to the exponential tilt and picking the best t gives the exponentially small <b>Chernoff bound</b>.", f=[["30504", "the MGF"], ["30601", "Markov"]], n=[["30605", "bounded losses"], ["30606", "against Chebyshev"]]),
30604: dict(s="STORY 6 · STEP 4 · CURVES AND AVERAGES", b="<b>Jensen</b>: averaging does not commute with a curve, and the direction is set by convexity.", f=[["30501", "expectation of g(X)"]], n=[["31205", "MMSE beats LLSE"], ["32604", "submartingales"]]),
30605: dict(s="STORY 6 · STEP 5 · PRODUCTS AND SUMS", b="<b>Cauchy–Schwarz</b> bounds a product's average; <b>Hoeffding</b> bounds a sum of bounded independent losses exponentially.", f=[["30603", "Chernoff"]], n=[["32606", "Azuma-Hoeffding"], ["31102", "orthogonality in estimation"]]),
30606: dict(s="STORY 6 · STEP 6 · THE COMPARISON", b="On coin flips, the <b>exponential bound beats Chebyshev</b> once many races are in.", f=[["30602", "Chebyshev"], ["30603", "Chernoff"]], n=[["31803", "the CLT as the exact picture"]]),
}

FIX = build(CARDS)
