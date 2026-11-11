"""StoMA topic 08 (order statistics). F1 picture: n cars crossing the line at the end of lap 1, safety cars spread over a race,
cars retiring one by one, and failure modes racing to end Max's race."""
from f1_lib import *

SUBJECT = "StoMA"

def line(y, x0=24, x1=222):
    return L(x0, y, x1, y, 1, ar=True) + N(x1, y + 12, "time", 7, "end")

def pts(y, xs, labs=None, mark=None):
    out = ""
    for i, x in enumerate(xs):
        out += C(x, y, 2.6, "#000000" if mark and i in mark else "#ffffff", 1)
        if labs: out += N(x, y - 7, labs[i], 7)
    return out

def d1(c):
    xs = [60, 96, 128, 150, 196]
    return svg(c, line(60), pts(60, xs, ["X₁", "X₂", "X₃", "X₄", "X₅"], mark=[0, 4]),
        N(60, 76, "X₍₁₎ first", 7.5), N(196, 76, "X₍ₙ₎ last", 7.5),
        N(30, 100, "max ≤ x: all n cars across by x:  [F(x)]ⁿ", 7.5, "start"), N(30, 114, "min > x: none yet:  1 − [1 − F(x)]ⁿ", 7.5, "start"),
        N(120, 22, "n cars finish lap 1, car i at time Xᵢ", 7), N(120, 36, "f of the first = n[1 − F(x)]ⁿ⁻¹ f(x)", 7.5), N(120, 138, "first = survivors multiply; last = finishers multiply", 7))

def d2(c):
    xs = [30, 52, 76, 130, 166, 196]
    return svg(c, line(70), pts(70, xs, mark=[3]),
        R(24, 78, 66, 12, "#f1f5f9", .8), N(57, 87, "k − 1 below", 7),
        R(136, 78, 68, 12, "#f1f5f9", .8), N(170, 87, "n − k above", 7),
        N(130, 56, "X₍ₖ₎ at x", 7.5), L(130, 60, 130, 64, 1),
        N(120, 22, "f(x) = n!/((k−1)!(n−k)!) F(x)ᵏ⁻¹ [1−F(x)]ⁿ⁻ᵏ f(x)", 6.8),
        N(120, 112, "[F(x)]ᵏ⁻¹: k−1 across   [1−F(x)]ⁿ⁻ᵏ: n−k still to come", 6.5), N(120, 126, "f(x) dx: the k-th crosses right at x; n!/(…) chooses who", 6.5))

def d3(c):
    return svg(c, ax(30, 108, 130, 16), N(130, 119, "x₁", 7, "end"), N(32, 12, "x₂", 7, "start"),
        R(30, 18, 90, 90, "#ffffff", 1), PG("30,108 120,108 120,18", "#f1f5f9", 1), PG("30,108 30,18 120,18", "none", 1, "3 2"),
        N(88, 92, "x₁ < x₂", 7.5), N(50, 40, "x₂ < x₁", 7.5),
        N(150, 50, "n! orderings fold", 7.5, "start"), N(150, 62, "onto one ordered cone,", 7.5, "start"), N(150, 74, "so multiply by n!:", 7.5, "start"),
        N(150, 92, "f = n! ∏ f(xᵢ), x₁ < … < xₙ", 7, "start"),
        N(120, 136, "without n! the ordered cone only holds 1/n! of the chance", 7))

def d4(c):
    B = lambda x: 112 - 70 * math.exp(-((x - 100) ** 2) / 1100)
    return svg(c, L(30, 40, 210, 40, 1.2), N(30, 32, "0", 7), N(210, 32, "1", 7, "end"),
        *[C(x, 40, 2.4) for x in (66, 96, 130, 168)],
        *[N(x, 56, "1/(n+1)", 6.5) for x in (48, 81, 113, 149, 189)],
        N(120, 22, "n incidents at uniform times cut the race into n+1 gaps", 7),
        ax(30, 118, 226, 70) if False else "",
        fn(lambda x: 126 - 46 * math.exp(-((x - 100) ** 2) / 1500), 30, 210, 50, 1.1), L(30, 126, 210, 126, 1),
        N(100, 74, "U₍ₖ₎ ~ Beta(k, n − k + 1)", 7.5), N(30, 140, "𝔼[U₍ₖ₎] = k/(n+1)", 7.5, "start"))

def d5(c):
    xs = [52, 84, 122, 166, 214]
    out = line(60)
    for x in xs: out += C(x, 60, 2.4)
    gaps = ["W₁ ~ Exp(nλ)", "W₂ ~ Exp((n−1)λ)", "W₃", "…"]
    out += L(24, 74, 52, 74, 1) + N(38, 86, "W₁", 7)
    out += L(52, 74, 84, 74, 1) + N(68, 86, "W₂", 7)
    out += L(84, 74, 122, 74, 1) + N(103, 86, "W₃", 7)
    out += L(122, 74, 166, 74, 1) + N(144, 86, "W₄", 7)
    out += L(166, 74, 214, 74, 1) + N(190, 86, "W₅", 7)
    return svg(c, out, N(120, 22, "n cars each retire at rate λ: gaps Wₖ are independent", 7),
        N(120, 38, "Wₖ ~ Exp((n − k + 1)λ): fewer cars left, slower gaps", 7),
        N(120, 108, "𝔼[last] = (1/λ) (1 + ½ + ⅓ + … + 1/n)", 7.5), N(120, 138, "memoryless ⇒ independent gaps, a signature of the exponential", 6.5))

def d6(c):
    out = ""
    for i, (nm, w) in enumerate([("engine: λ₁", 80), ("gearbox: λ₂", 52), ("hydraulics: λ₃", 30)]):
        y = 38 + i * 24
        out += N(20, y + 3, nm, 7, "start") + L(88, y, 88 + w, y, 1) + car(88 + w, y + 5, .6)
    return svg(c, out, N(120, 18, "the first failure ends Max's race", 7),
        N(30, 112, "T = min Tᵢ ~ Exp(λ₁ + λ₂ + λ₃)", 7.5, "start"), N(30, 124, "ℙ(mode k fails first) = λₖ / ∑λᵢ", 7.5, "start"),
        N(120, 138, "survival functions multiply: ℙ(T > t) = ∏ e^(−λᵢt)", 7))

CARDS = {
30801: dict(d=d1, kind="THEOREM",
  stmt=r"<b>Distribution of the extremes.</b> Let $X_1,\ldots,X_n$ be i.i.d. with CDF $F$ and density $f$, and let $X_{(1)}\le\cdots\le X_{(n)}$ be their order statistics. Then $F_{X_{(n)}}(x)=[F(x)]^n$ and $F_{X_{(1)}}(x)=1-[1-F(x)]^n$, so $f_{X_{(n)}}(x)=n[F(x)]^{n-1}f(x)$ and $f_{X_{(1)}}(x)=n[1-F(x)]^{n-1}f(x)$ (Ross 6.6; Grimmett 4.14).",
  hint='With n cars finishing lap 1 independently, how do you get the law of the first one across the line and of the last?',
  bd=['<strong>$[F(x)]^n$ = all $n$ have crossed by $x$.</strong> The last car is across by $x$ exactly when every car is; independent chances multiply.',
      '<strong>$1-[1-F(x)]^n$ = at least one has crossed by $x$.</strong> The first car is later than $x$ only if all $n$ are: $[1-F(x)]^n$, so subtract it from 1.',
      "<strong>$n[1-F(x)]^{n-1}f(x)$ = the first one's density.</strong> Differentiate; the inner derivative of $1-F$ is $-f$, which cancels the leading minus sign."],
  conn="<strong>Who is first across the line?</strong> With many cars on track, the leader's time is the shortest of several times: it is short unless every car is slow. The last car's time is long unless every car is quick.",
  cap='n lap-1 times Xᵢ on a time line, with the first X₍₁₎ and the last X₍ₙ₎ marked. The last is at most x if all have crossed, [F(x)]ⁿ; the first exceeds x if none have, [1 − F(x)]ⁿ.'),
30802: dict(d=d2, kind="THEOREM",
  stmt=r"<b>Density of the $k$-th order statistic.</b> For i.i.d. $X_1,\ldots,X_n$ with CDF $F$ and density $f$, $f_{X_{(k)}}(x)=\dfrac{n!}{(k-1)!\,(n-k)!}[F(x)]^{k-1}[1-F(x)]^{n-k}f(x)=k\binom nk[F(x)]^{k-1}[1-F(x)]^{n-k}f(x)$ (Ross 6.6; Grimmett 4.14).",
  hint='For the k-th car to cross the line exactly at time x, what must the other n − 1 cars be doing?',
  bd=['<strong>$[F(x)]^{k-1}$ = $k-1$ cars have already crossed.</strong> Each of those crossed before $x$, with chance $F(x)$ each.',
      '<strong>$[1-F(x)]^{n-k}$ = $n-k$ cars are still to come.</strong> Each of those is later than $x$, with chance $1-F(x)$ each.',
      r"<strong>$\frac{n!}{(k-1)!(n-k)!}f(x)$ = choose who, and put one exactly at $x$.</strong> The multinomial coefficient picks which car is the $k$-th, and $f(x)$ is the density of that car being at $x$. Without it you only have a probability, not a density."],
  conn='<strong>Third of five across the line.</strong> For the third of five cars to cross at time $x$, two cars must already be across, one must cross right at $x$, and two must still be to come. Count the ways to assign roles and multiply the chances.',
  cap='Six lap times with the k-th at x: k − 1 sit below it with chance F(x) each, n − k above with chance 1 − F(x) each, and the multinomial factor n!/((k−1)!(n−k)!) chooses who is who.'),
30803: dict(d=d3, kind="THEOREM",
  stmt=r"<b>Joint density of order statistics.</b> For i.i.d. $X_i$ with density $f$, $(X_{(1)},\ldots,X_{(n)})$ has density $n!\prod_{i=1}^nf(x_i)\mathbf 1_{\{x_1<\cdots<x_n\}}$ (Ross 6.6; Grimmett 4.14).",
  hint='If you sort n lap times, why is the joint density of the sorted list n! times the product of the densities?',
  bd=[r"<strong>$\prod f(x_i)$ = one particular unsorted list.</strong> Independent cars' times multiply.",
      r"<strong>$\mathbf 1_{\{x_1<\cdots<x_n\}}$ = only sorted lists.</strong> The timing screen shows times in order: the sorted vector lives on one cone, and other orderings fold onto it.",
      '<strong>$n!$ = every ordering gives the same sorted list.</strong> Without it the density integrates to $1/n!$.'],
  conn='<strong>Sorting the timing screen.</strong> Many car-by-car assignments of times lead to the same sorted timing screen; collecting them multiplies the chance by $n!$.',
  cap='For n = 2: the unit square splits into the cone x₁ < x₂ and its mirror image. Folding the mirror onto the cone gives the sorted density 2! f(x₁)f(x₂), that is n! ∏f(xᵢ).'),
30804: dict(d=d4, kind="THEOREM",
  stmt=r"<b>Uniform order statistics.</b> If $U_i$ are i.i.d. $\mathrm{Unif}(0,1)$, then $U_{(k)}\sim\mathrm{Beta}(k,n-k+1)$ with $\mathbb E[U_{(k)}]=\frac{k}{n+1}$. The $n+1$ spacings are identically distributed, each of mean $\frac1{n+1}$ (Ross 6.6; Grimmett 4.14).",
  hint='If n incidents fall at random times in a race, where does the k-th one sit on average, and how big are the gaps?',
  bd=[r"<strong>$\mathrm{Beta}(k,n-k+1)$ = the $k$-th incident's law.</strong> A bump with $k-1$ incidents to its left and $n-k$ to its right.",
      r"<strong>$\mathbb E[U_{(k)}]=\frac k{n+1}$ = evenly spread on average.</strong> $n$ incidents cut the race into $n+1$ gaps; the $k$-th sits $k$ gaps along.",
      '<strong>All $n+1$ spacings alike.</strong> The gaps to the start and to the flag behave exactly like the interior gaps.'],
  conn='<strong>Incidents spread across the race.</strong> With four incidents at random moments in a race, the first comes after about a fifth of the race, and every gap between them averages the same.',
  cap='n incidents cut the race [0,1] into n+1 gaps of mean 1/(n+1). The bump below is the Beta(k, n − k + 1) density of the k-th incident, with mean 𝔼[U₍ₖ₎] = k/(n+1).'),
30805: dict(d=d5, kind="THEOREM",
  stmt=r"<b>Spacings of exponential order statistics.</b> Let $X_1,\ldots,X_n$ be i.i.d. $\mathrm{Exp}(\lambda)$ with $X_{(0)}=0$. Then the spacings $W_k=X_{(k)}-X_{(k-1)}$, $k=1,\ldots,n$, are independent with $W_k\sim\mathrm{Exp}\bigl((n-k+1)\lambda\bigr)$. Hence $\mathbb E[X_{(n)}]=\dfrac1\lambda\sum_{j=1}^n\dfrac1j$ (Ross 6.6; Grimmett 4.14).",
  hint="After the first car has retired, how long until the next, if every car's time to failure is memoryless?",
  bd=['<strong>$W_k=X_{(k)}-X_{(k-1)}$ = the gap between consecutive retirements.</strong> The time from the $(k-1)$-th retirement to the $k$-th.',
      r"<strong>$\mathrm{Exp}((n-k+1)\lambda)$ = a race among the cars still running.</strong> By memorylessness the $n-k+1$ remaining times restart afresh; the first of them has rate $(n-k+1)\lambda$.",
      r"<strong>$\mathbb E[X_{(n)}]=\frac1\lambda\sum1/j$ = the last car.</strong> Add the mean gaps $\frac1{n\lambda},\frac1{(n-1)\lambda},\ldots,\frac1\lambda$: a harmonic sum. Independence of gaps is special to the exponential."],
  conn='<strong>The field thins out.</strong> With twenty cars running, the first retirement comes quickly because twenty cars could fail. Once it is gone, nineteen remain, so the next gap is a little longer, and the last car standing has the slowest gap of all.',
  cap='Retirement times of n cars on a time line, with gaps W₁, W₂, … below. Gap Wₖ has rate (n − k + 1)λ, getting slower as cars drop out, and the gaps are independent.'),
30806: dict(d=d6, kind="WORKED EXAMPLE",
  stmt=r"<b>Minimum of independent exponentials.</b> If $T_1,\ldots,T_n$ are independent with $T_i\sim\mathrm{Exp}(\lambda_i)$, then $T=\min_iT_i\sim\mathrm{Exp}\!\left(\sum_i\lambda_i\right)$, since $\mathbb P(T>t)=\prod_ie^{-\lambda_it}$, and $\mathbb P(T_k=\min_iT_i)=\dfrac{\lambda_k}{\sum_i\lambda_i}$. A series system of components with these lifetimes fails at time $T$ (Ross 5.5, 6.6).",
  hint="Engine, gearbox and hydraulics race to fail first. How long until Max's race ends, and which part breaks?",
  bd=[r"<strong>$\mathbb P(T>t)=\prod_ie^{-\lambda_it}$ = nothing has failed yet.</strong> The first failure is later than $t$ only if every part survives past $t$; survival chances multiply.",
      r"<strong>$\mathrm{Exp}(\sum\lambda_i)$ = rates add.</strong> The product is $e^{-(\sum\lambda_i)t}$, an exponential with the summed rate: more ways to fail, an earlier first failure.",
      r"<strong>$\lambda_k/\sum\lambda_i$ = the culprit is proportional to rate.</strong> The chance that part $k$ fails first is its share of the total rate."],
  conn='<strong>Three parts race to fail.</strong> A fragile part is more likely to be the one that ends the race, in proportion to its failure rate, and having three ways to fail makes the first failure come sooner than any one part alone.',
  cap='Three failure modes with rates λ₁ (engine), λ₂ (gearbox), λ₃ (hydraulics) racing. The first failure T = min Tᵢ is exponential with rate ∑λᵢ, and part k fails first with chance λₖ/∑λᵢ.'),
}

STORY = {
30801: dict(s="STORY 8 · STEP 1 · FIRST AND LAST", b='With several competing times, the <b>first</b> and <b>last</b> have simple laws from products of CDFs and survival functions.', f=[["30301", "the CDF"], ["30705", "independent variables multiply"]], n=[["30802", "any rank k"], ["30806", "minimum of exponentials"]]),
30802: dict(s="STORY 8 · STEP 2 · ANY RANK", b='The <b>k-th car</b> needs k−1 before, n−k after, and one right at x.', f=[["30801", "extremes"]], n=[["30803", "all ranks together"], ["30804", "the uniform case"]]),
30803: dict(s="STORY 8 · STEP 3 · SORTED TOGETHER", b="The whole sorted list has density <b>n! times the product</b> on the ordered cone.", f=[["30802", "single ranks"]], n=[["30804", "Beta marginals"], ["32403", "Poisson arrival times given the count"]]),
30804: dict(s="STORY 8 · STEP 4 · THE UNIFORM CASE", b="Uniform points give <b>Beta</b> ranks and equal-mean gaps.", f=[["30803", "joint order density"]], n=[["32403", "arrival times are uniform order statistics"]]),
30805: dict(s="STORY 8 · STEP 5 · THE EXPONENTIAL CASE", b='Exponential failure times have <b>independent</b> gaps whose rates drop as cars drop out.', f=[["30304", "memorylessness"], ["30803", "joint order density"]], n=[["30806", "the first arrival"]]),
30806: dict(s="STORY 8 · STEP 6 · THE RACE", b="The minimum of independent exponentials is exponential with <b>summed rates</b>, and the winner is picked in proportion to rate.", f=[["30801", "extremes"], ["30805", "exponential gaps"]], n=[["32404", "merging Poisson streams"], ["32701", "competing exponential clocks in CTMCs"]]),
}

FIX = build(CARDS)
