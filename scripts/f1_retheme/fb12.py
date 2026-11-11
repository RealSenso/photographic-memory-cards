DOC = """StoMA topic 12 (conditional expectation, MMSE). F1 picture: the expected lap time given tyre age; refine with fuel load then average it out; lap-time variance split between compounds; thinning yellow-flag incidents into safety cars."""
DRAW = {
'd6': '''def d6(c):
    out = N(36, 28, "N ~ Pois(λ) incidents in a race", 7.5, "start")
    for i in range(7):
        x = 24 + i * 28
        out += car(x, 64, .8)
        if i in (1, 3, 6):
            out += R(x + 5, 38, 16, 10, "#d9dee7", 1, 2) + N(x + 13, 46, "SC", 6.5)
    out += N(120, 80, "each brings out the safety car with chance p: K = 3 of them", 7)
    return svg(c, out, N(120, 100, "𝔼[K] = λp,  Var(K) = 𝔼[Np(1−p)] + Var(Np)", 7.5), N(120, 114, "= λp(1−p) + λp² = λp", 7.5), N(120, 130, "mean = variance ⇒ K ~ Poisson(λp)", 7.5))''',
}
SUBS = [
 ('"X: what you know"', '"X: tyre age"'),
 ('"Y: ride"', '"Y: lap time"'),
]
CARDS = {
31201: dict(hint="With no restriction on the form of your guess, which function of the tyre age predicts Max's lap time best?",
  bd=[r"<strong>$\mathbb E[Y\mid X]$ = the average lap time given what you know.</strong> On each value of $X$, take the average of $Y$ over laps with that $X$.",
      r"<strong>$\arg\min_g\mathbb E[(Y-g(X))^2]$ = best of all functions.</strong> No straight-line restriction: the curve through the slice averages wins.",
      r"<strong>$\mathbb E[\mathbb E[Y\mid X]]=\mathbb E[Y]$ = averaging the guesses gives the overall average.</strong> The slice averages, weighted by how common each slice is."],
  conn=r"<strong>The average of similar laps.</strong> Among all of Max's laps on tyres of the same age, take the average lap time. Doing this for every tyre age gives the best possible guess of the next lap.",
  cap="The scatter of (tyre age X, lap time Y). The curve 𝔼[Y | X] passes through the average of Y on each slice of X and minimises the squared error over all functions of X."),
31202: dict(hint="Which property of the error tells you the conditional average is the nearest possible guess?",
  bd=[r"<strong>$h(X)$ = any function of what you know.</strong> Not just straight lines: squares, thresholds, anything computed from $X$.",
      r"<strong>$Y-\mathbb E[Y\mid X]$ = what the best guess misses.</strong> The part of the lap time that $X$ does not pin down.",
      r"<strong>$\mathbb E[(\ldots)h(X)]=0$ = the miss is uncorrelated with every function of $X$.</strong> Nothing computed from $X$ can predict the miss."],
  conn=r"<strong>Nothing left to learn.</strong> After the best guess from tyre age, no trick with the tyre age, however clever, predicts the leftover error: all the information in the tyre age has been used.",
  cap="The sheet of all functions h(X) of what you know. The best guess 𝔼[Y | X] is the foot of the perpendicular from Y, and the error Y − 𝔼[Y | X] is orthogonal to every h(X)."),
31203: dict(hint="If you refine a guess with the fuel load and then forget the fuel load again, what do you get back?",
  bd=[r"<strong>$\mathbb E[Y\mid X_1,X_2]$ = the finer guess.</strong> The average lap time given both the tyre age and the fuel load.",
      r"<strong>$\mathbb E[\cdot\mid X_1]$ = then forget the fuel.</strong> Averaging the finer guess over what $X_1$ does not fix lands on the coarser guess.",
      r"<strong>$g(X)\mathbb E[Y\mid X]$ = known factors come out.</strong> Given $X$, $g(X)$ is not random, so it passes through the average."],
  conn=r"<strong>Refine, then coarsen.</strong> Averaging the detailed forecast (tyre age and fuel load) over the fuel loads you do not know brings you back to the forecast from tyre age alone.",
  cap="Y, then the finer guess 𝔼[Y | X₁, X₂] (tyre age, fuel load), then the coarser 𝔼[Y | X₁]. Forgetting X₂ again gives 𝔼[𝔼[Y | X₁, X₂] | X₁] = 𝔼[Y | X₁]."),
31204: dict(hint="How does the total spread of Max's lap times split into the part the tyre compound explains and the part that stays noise?",
  bd=[r"<strong>$\operatorname{Var}(\mathbb E[Y\mid X])$ = the signal.</strong> How much the average lap time moves from one compound (soft, medium, hard) to another.",
      r"<strong>$\mathbb E[\operatorname{Var}(Y\mid X)]$ = the noise.</strong> The average leftover spread of lap times within one compound.",
      r"<strong>$=\operatorname{Var}(Y)$ = they add.</strong> The noise part is exactly the minimum mean squared error."],
  conn=r"<strong>Between compounds and within a compound.</strong> Part of the variation in Max's lap times comes from which compound he is on, and part is lap-to-lap noise on the same compound. Together they make up the total variation, and the noise is your unavoidable error.",
  cap="One bar for Var(Y), split into the signal Var(𝔼[Y | X]) between compounds and the noise 𝔼[Var(Y | X)] within a compound. The noise segment is the minimum mean squared error."),
31205: dict(hint="When does a straight-line guess lose to the curve of slice averages, and when do they agree?",
  bd=[r"<strong>$\mathbb E[(Y-\mathbb E[Y\mid X])^2]$ = error of the best curve.</strong> The smallest error over all functions of $X$.",
      r"<strong>$\mathbb E[(Y-\hat Y_{\rm LLSE})^2]$ = error of the best line.</strong> Larger or equal, since lines are a smaller family to choose from.",
      r"<strong>$\le\operatorname{Var}(Y)$ = never worse than ignoring $X$.</strong> The constant guess $\mu_Y$ is itself a linear estimator."],
  conn=r"<strong>Line versus curve.</strong> Tyres matter in a curved way: the lap time barely moves for 20 laps, then the tyres fall off a cliff. A straight-line rule loses to the curve. If the link were straight, the two would give the same guess.",
  cap="Data around a curved relationship, the best curve 𝔼[Y | X] and the straight LLSE line (dashed). The curve's error is smaller, which in turn is at most Var(Y)."),
31206: dict(hint="Of the yellow-flag incidents in a race, a share p bring out the safety car. What are the mean and variance of the number of safety cars?",
  bd=[r"<strong>$\mathbb E[K\mid N]=Np$ = given $N$ incidents, a share $p$ bring a safety car.</strong> Averaging over $N$ gives $\mathbb E[K]=\lambda p$.",
      r"<strong>$\mathbb E[Np(1-p)]=\lambda p(1-p)$ = the noise.</strong> Given $N$, the number of safety cars is binomial with variance $Np(1-p)$.",
      r"<strong>$\operatorname{Var}(Np)=p^2\lambda$ = the signal.</strong> The number of incidents itself varies; the two parts add to $\lambda p$, mean equals variance."],
  conn=r"<strong>Only the big incidents.</strong> Incidents happen at random during a race, and each is serious enough for a safety car with chance $p$. The safety cars then arrive randomly too, as if only they existed: Poisson with the thinned rate.",
  cap="Poisson(λ) incidents, each bringing out the safety car with chance p: 𝔼[K] = λp. Var(K) = 𝔼[Np(1−p)] + Var(Np) = λp, so mean equals variance, as for a Poisson(λp) count."),
}
STORY = {}
