DOC = """StoMA topic 08 (order statistics). F1 picture: n cars crossing the line at the end of lap 1, safety cars spread over a race,
cars retiring one by one, and failure modes racing to end Max's race."""
DRAW = {
'd6': '''def d6(c):
    out = ""
    for i, (nm, w) in enumerate([("engine: λ₁", 80), ("gearbox: λ₂", 52), ("hydraulics: λ₃", 30)]):
        y = 38 + i * 24
        out += N(20, y + 3, nm, 7, "start") + L(88, y, 88 + w, y, 1) + car(88 + w, y + 5, .6)
    return svg(c, out, N(120, 18, "the first failure ends Max's race", 7),
        N(30, 112, "T = min Tᵢ ~ Exp(λ₁ + λ₂ + λ₃)", 7.5, "start"), N(30, 124, "ℙ(mode k fails first) = λₖ / ∑λᵢ", 7.5, "start"),
        N(120, 138, "survival functions multiply: ℙ(T > t) = ∏ e^(−λᵢt)", 7))''',
}
SUBS = [
 ('N(30, 100, "max ≤ x: all n arrive by x:  [F(x)]ⁿ", 7.5, "start")', 'N(30, 100, "max ≤ x: all n cars across by x:  [F(x)]ⁿ", 7.5, "start")'),
 ('N(120, 22, "n buses on different routes, each arrival time Xᵢ", 7)', 'N(120, 22, "n cars finish lap 1, car i at time Xᵢ", 7)'),
 ('"first = survivors multiply; last = arrivals multiply"', '"first = survivors multiply; last = finishers multiply"'),
 ('"[F(x)]ᵏ⁻¹: k−1 arrived   [1−F(x)]ⁿ⁻ᵏ: n−k still to come"', '"[F(x)]ᵏ⁻¹: k−1 across   [1−F(x)]ⁿ⁻ᵏ: n−k still to come"'),
 ('"f(x) dx: the k-th arrives right at x; n!/(…) chooses who"', '"f(x) dx: the k-th crosses right at x; n!/(…) chooses who"'),
 ('"n uniform arrivals cut [0,1] into n+1 equal-length gaps"', '"n incidents at uniform times cut the race into n+1 gaps"'),
 ('"n buses arrive at rate λ each: gaps Wₖ are independent"', '"n cars each retire at rate λ: gaps Wₖ are independent"'),
 ('"Wₖ ~ Exp((n − k + 1)λ): fewer buses left, slower gaps"', '"Wₖ ~ Exp((n − k + 1)λ): fewer cars left, slower gaps"'),
]
CARDS = {
30801: dict(hint="With n cars finishing lap 1 independently, how do you get the law of the first one across the line and of the last?",
  bd=[r"<strong>$[F(x)]^n$ = all $n$ have crossed by $x$.</strong> The last car is across by $x$ exactly when every car is; independent chances multiply.",
      r"<strong>$1-[1-F(x)]^n$ = at least one has crossed by $x$.</strong> The first car is later than $x$ only if all $n$ are: $[1-F(x)]^n$, so subtract it from 1.",
      r"<strong>$n[1-F(x)]^{n-1}f(x)$ = the first one's density.</strong> Differentiate; the inner derivative of $1-F$ is $-f$, which cancels the leading minus sign."],
  conn=r"<strong>Who is first across the line?</strong> With many cars on track, the leader's time is the shortest of several times: it is short unless every car is slow. The last car's time is long unless every car is quick.",
  cap="n lap-1 times Xᵢ on a time line, with the first X₍₁₎ and the last X₍ₙ₎ marked. The last is at most x if all have crossed, [F(x)]ⁿ; the first exceeds x if none have, [1 − F(x)]ⁿ."),
30802: dict(hint="For the k-th car to cross the line exactly at time x, what must the other n − 1 cars be doing?",
  bd=[r"<strong>$[F(x)]^{k-1}$ = $k-1$ cars have already crossed.</strong> Each of those crossed before $x$, with chance $F(x)$ each.",
      r"<strong>$[1-F(x)]^{n-k}$ = $n-k$ cars are still to come.</strong> Each of those is later than $x$, with chance $1-F(x)$ each.",
      r"<strong>$\frac{n!}{(k-1)!(n-k)!}f(x)$ = choose who, and put one exactly at $x$.</strong> The multinomial coefficient picks which car is the $k$-th, and $f(x)$ is the density of that car being at $x$. Without it you only have a probability, not a density."],
  conn=r"<strong>Third of five across the line.</strong> For the third of five cars to cross at time $x$, two cars must already be across, one must cross right at $x$, and two must still be to come. Count the ways to assign roles and multiply the chances.",
  cap="Six lap times with the k-th at x: k − 1 sit below it with chance F(x) each, n − k above with chance 1 − F(x) each, and the multinomial factor n!/((k−1)!(n−k)!) chooses who is who."),
30803: dict(hint="If you sort n lap times, why is the joint density of the sorted list n! times the product of the densities?",
  bd=[r"<strong>$\prod f(x_i)$ = one particular unsorted list.</strong> Independent cars' times multiply.",
      r"<strong>$\mathbf 1_{\{x_1<\cdots<x_n\}}$ = only sorted lists.</strong> The timing screen shows times in order: the sorted vector lives on one cone, and other orderings fold onto it.",
      r"<strong>$n!$ = every ordering gives the same sorted list.</strong> Without it the density integrates to $1/n!$."],
  conn=r"<strong>Sorting the timing screen.</strong> Many car-by-car assignments of times lead to the same sorted timing screen; collecting them multiplies the chance by $n!$.",
  cap="For n = 2: the unit square splits into the cone x₁ < x₂ and its mirror image. Folding the mirror onto the cone gives the sorted density 2! f(x₁)f(x₂), that is n! ∏f(xᵢ)."),
30804: dict(hint="If n incidents fall at random times in a race, where does the k-th one sit on average, and how big are the gaps?",
  bd=[r"<strong>$\mathrm{Beta}(k,n-k+1)$ = the $k$-th incident's law.</strong> A bump with $k-1$ incidents to its left and $n-k$ to its right.",
      r"<strong>$\mathbb E[U_{(k)}]=\frac k{n+1}$ = evenly spread on average.</strong> $n$ incidents cut the race into $n+1$ gaps; the $k$-th sits $k$ gaps along.",
      r"<strong>All $n+1$ spacings alike.</strong> The gaps to the start and to the flag behave exactly like the interior gaps."],
  conn=r"<strong>Incidents spread across the race.</strong> With four incidents at random moments in a race, the first comes after about a fifth of the race, and every gap between them averages the same.",
  cap="n incidents cut the race [0,1] into n+1 gaps of mean 1/(n+1). The bump below is the Beta(k, n − k + 1) density of the k-th incident, with mean 𝔼[U₍ₖ₎] = k/(n+1)."),
30805: dict(hint="After the first car has retired, how long until the next, if every car's time to failure is memoryless?",
  bd=[r"<strong>$W_k=X_{(k)}-X_{(k-1)}$ = the gap between consecutive retirements.</strong> The time from the $(k-1)$-th retirement to the $k$-th.",
      r"<strong>$\mathrm{Exp}((n-k+1)\lambda)$ = a race among the cars still running.</strong> By memorylessness the $n-k+1$ remaining times restart afresh; the first of them has rate $(n-k+1)\lambda$.",
      r"<strong>$\mathbb E[X_{(n)}]=\frac1\lambda\sum1/j$ = the last car.</strong> Add the mean gaps $\frac1{n\lambda},\frac1{(n-1)\lambda},\ldots,\frac1\lambda$: a harmonic sum. Independence of gaps is special to the exponential."],
  conn=r"<strong>The field thins out.</strong> With twenty cars running, the first retirement comes quickly because twenty cars could fail. Once it is gone, nineteen remain, so the next gap is a little longer, and the last car standing has the slowest gap of all.",
  cap="Retirement times of n cars on a time line, with gaps W₁, W₂, … below. Gap Wₖ has rate (n − k + 1)λ, getting slower as cars drop out, and the gaps are independent."),
30806: dict(hint="Engine, gearbox and hydraulics race to fail first. How long until Max's race ends, and which part breaks?",
  bd=[r"<strong>$\mathbb P(T>t)=\prod_ie^{-\lambda_it}$ = nothing has failed yet.</strong> The first failure is later than $t$ only if every part survives past $t$; survival chances multiply.",
      r"<strong>$\mathrm{Exp}(\sum\lambda_i)$ = rates add.</strong> The product is $e^{-(\sum\lambda_i)t}$, an exponential with the summed rate: more ways to fail, an earlier first failure.",
      r"<strong>$\lambda_k/\sum\lambda_i$ = the culprit is proportional to rate.</strong> The chance that part $k$ fails first is its share of the total rate."],
  conn=r"<strong>Three parts race to fail.</strong> A fragile part is more likely to be the one that ends the race, in proportion to its failure rate, and having three ways to fail makes the first failure come sooner than any one part alone.",
  cap="Three failure modes with rates λ₁ (engine), λ₂ (gearbox), λ₃ (hydraulics) racing. The first failure T = min Tᵢ is exponential with rate ∑λᵢ, and part k fails first with chance λₖ/∑λᵢ."),
}
STORY = {
30801: dict(b="With several competing times, the <b>first</b> and <b>last</b> have simple laws from products of CDFs and survival functions."),
30802: dict(b="The <b>k-th car</b> needs k−1 before, n−k after, and one right at x."),
30805: dict(b="Exponential failure times have <b>independent</b> gaps whose rates drop as cars drop out."),
}
