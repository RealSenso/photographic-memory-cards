"""StoMA topic 12 (conditional expectation, MMSE). F1 picture: the expected lap time given tyre age; refine with fuel load then average it out; lap-time variance split between compounds; thinning yellow-flag incidents into safety cars."""
from f1_lib import *

SUBJECT = "StoMA"
PTS = [(44, 70), (56, 52), (66, 60), (78, 46), (90, 56), (104, 62), (118, 52), (132, 68), (150, 82), (170, 96), (186, 90)]

def d1(c):
    g = lambda x: 112 - 70 * math.exp(-((x - 100) ** 2) / 2600) + 0 if False else 78 - 40 * math.exp(-((x - 90) ** 2) / 1800) + 0.0016 * (x - 90) ** 2
    out = ax(24, 112, 226, 14) + N(226, 124, "X: tyre age", 7, "end") + N(28, 14, "Y: lap time", 7, "start")
    out += "".join(C(x, y, 1.8) for x, y in PTS) + fn(g, 36, 200, 60, 1.2)
    out += N(150, 66, "𝔼[Y | X]", 8, "start") + N(36, 20, "𝔼[Y | X] = argmin 𝔼[(Y − g(X))²]", 7.5, "start") + N(36, 31, "𝔼[𝔼[Y | X]] = 𝔼[Y]", 7.5, "start")
    out += N(120, 138, "the best guess is the average of Y on each vertical slice", 7)
    return svg(c, out)

def d2(c):
    return svg(c, PG("30,100 150,100 200,70 80,70", "#f1f5f9", 1), N(150, 112, "all functions h(X): L²(σ(X))", 7, "middle"),
        arrow(110, 85, 110, 34, 1, "3 2"), N(116, 60, "Y − 𝔼[Y | X]", 7.5, "start"), N(110, 28, "Y", 8),
        C(110, 85, 2.4), N(118, 90, "𝔼[Y | X]", 7.5, "start"), arrow(80, 94, 110, 86, 1) if False else "",
        L(110, 78, 118, 78, 1) + L(118, 78, 118, 85, 1) if False else "",
        N(120, 12, "𝔼[(Y − 𝔼[Y | X]) h(X)] = 0 for every h", 7.5),
        N(120, 128, "the error is orthogonal to every function of X, not just straight lines", 7),
        N(120, 140, "so it is the nearest point of the whole sheet", 7))

def d3(c):
    out = ""
    for x, lab in [(30, "Y"), (88, "𝔼[Y | X₁, X₂]"), (170, "𝔼[Y | X₁]")]:
        w = 44 if x == 30 else (70 if x == 88 else 56)
        out += R(x, 56, w, 22, "#f1f5f9" if x < 100 else "#d9dee7", 1, 3) + N(x + w / 2, 71, lab, 7)
    return svg(c, out, arrow(76, 67, 88, 67, 1), arrow(158, 67, 170, 67, 1),
        N(82, 50, "know", 6.5), N(164, 50, "forget X₂", 6.5), N(120, 18, "𝔼[𝔼[Y | X₁, X₂] | X₁] = 𝔼[Y | X₁]", 8),
        N(120, 100, "averaging a fine guess back to a coarse guess gives the coarse guess", 7),
        N(120, 116, "𝔼[g(X) Y | X] = g(X) 𝔼[Y | X]: known factors come out", 7), N(120, 132, "(what X already tells you is not random any more)", 7))

def d4(c):
    return svg(c, R(30, 56, 180, 24, "#ffffff", 1), R(30, 56, 120, 24, "#d9dee7", 1), L(150, 56, 150, 80, 1),
        N(90, 72, "Var(𝔼[Y | X]) signal", 7.5), N(180, 72, "𝔼[Var(Y | X)] noise", 7),
        N(120, 100, "Var(Y)", 8), L(30, 92, 210, 92, 1) + L(30, 88, 30, 96, 1) + L(210, 88, 210, 96, 1),
        N(120, 22, "Var(Y) = 𝔼[Var(Y | X)] + Var(𝔼[Y | X])", 8),
        N(120, 128, "MMSE error = the noise part: what knowing X cannot remove", 7))

def d5(c):
    line = lambda x: 98 - (x - 30) * 0.12
    curve = lambda x: 40 + 0.0042 * (x - 110) ** 2
    return svg(c, ax(24, 112, 226, 14), N(226, 124, "X", 7, "end"), N(28, 14, "Y", 7, "start"),
        "".join(C(x, curve(x) + (6 if i % 2 else -6), 1.8) for i, x in enumerate(range(40, 200, 14))),
        L(36, line(36), 200, line(200), 1.1, "4 3"), fn(curve, 36, 200, 50, 1.2),
        N(150, 36, "𝔼[Y | X] curve", 7.5, "start"), N(150, 92, "LLSE line", 7.5, "start"),
        N(120, 140, "𝔼(Y − 𝔼[Y | X])² ≤ 𝔼(Y − Ŷ)² ≤ Var(Y)", 7.5))

def d6(c):
    out = N(36, 28, "N ~ Pois(λ) incidents in a race", 7.5, "start")
    for i in range(7):
        x = 24 + i * 28
        out += car(x, 64, .8)
        if i in (1, 3, 6):
            out += R(x + 5, 38, 16, 10, "#d9dee7", 1, 2) + N(x + 13, 46, "SC", 6.5)
    out += N(120, 80, "each brings out the safety car with chance p: K = 3 of them", 7)
    return svg(c, out, N(120, 100, "𝔼[K] = λp,  Var(K) = 𝔼[Np(1−p)] + Var(Np)", 7.5), N(120, 114, "= λp(1−p) + λp² = λp", 7.5), N(120, 130, "mean = variance ⇒ K ~ Poisson(λp)", 7.5))

CARDS = {
31201: dict(d=d1, kind="THEOREM",
  stmt=r"<b>Conditional expectation as best guess.</b> If $\mathbb E[Y^2]<\infty$, then $\hat Y=\mathbb E[Y\mid X]$ is the unique (a.s.) function of $X$ minimising $\mathbb E[(Y-g(X))^2]$ over all $g$ with $\mathbb E[g(X)^2]<\infty$, and $\mathbb E[\mathbb E[Y\mid X]]=\mathbb E[Y]$ (Ross 7.5; Grimmett 3.7, 7.9).",
  hint="With no restriction on the form of your guess, which function of the tyre age predicts Max's lap time best?",
  bd=[r"<strong>$\mathbb E[Y\mid X]$ = the average lap time given what you know.</strong> On each value of $X$, take the average of $Y$ over laps with that $X$.",
      r"<strong>$\arg\min_g\mathbb E[(Y-g(X))^2]$ = best of all functions.</strong> No straight-line restriction: the curve through the slice averages wins.",
      r"<strong>$\mathbb E[\mathbb E[Y\mid X]]=\mathbb E[Y]$ = averaging the guesses gives the overall average.</strong> The slice averages, weighted by how common each slice is."],
  conn="<strong>The average of similar laps.</strong> Among all of Max's laps on tyres of the same age, take the average lap time. Doing this for every tyre age gives the best possible guess of the next lap.",
  cap='The scatter of (tyre age X, lap time Y). The curve 𝔼[Y | X] passes through the average of Y on each slice of X and minimises the squared error over all functions of X.'),
31202: dict(d=d2, kind="THEOREM",
  stmt=r"<b>Orthogonality in $L^2$.</b> For $\mathbb E[Y^2]<\infty$, $\hat Y=\mathbb E[Y\mid X]$ is the orthogonal projection of $Y$ onto $L^2(\sigma(X))$: $\mathbb E\bigl[(Y-\mathbb E[Y\mid X])h(X)\bigr]=0$ for all $h$ with $\mathbb E[h(X)^2]<\infty$ (Grimmett 7.9).",
  hint='Which property of the error tells you the conditional average is the nearest possible guess?',
  bd=['<strong>$h(X)$ = any function of what you know.</strong> Not just straight lines: squares, thresholds, anything computed from $X$.',
      r"<strong>$Y-\mathbb E[Y\mid X]$ = what the best guess misses.</strong> The part of the lap time that $X$ does not pin down.",
      r"<strong>$\mathbb E[(\ldots)h(X)]=0$ = the miss is uncorrelated with every function of $X$.</strong> Nothing computed from $X$ can predict the miss."],
  conn='<strong>Nothing left to learn.</strong> After the best guess from tyre age, no trick with the tyre age, however clever, predicts the leftover error: all the information in the tyre age has been used.',
  cap='The sheet of all functions h(X) of what you know. The best guess 𝔼[Y | X] is the foot of the perpendicular from Y, and the error Y − 𝔼[Y | X] is orthogonal to every h(X).'),
31203: dict(d=d3, kind="THEOREM",
  stmt=r"<b>Tower property and taking out what is known.</b> For $\sigma$-algebras $\mathcal G\subset\mathcal H$: $\mathbb E[\mathbb E[Y\mid\mathcal H]\mid\mathcal G]=\mathbb E[Y\mid\mathcal G]$, in particular $\mathbb E[\mathbb E[Y\mid X_1,X_2]\mid X_1]=\mathbb E[Y\mid X_1]$. Also $\mathbb E[g(X)Y\mid X]=g(X)\,\mathbb E[Y\mid X]$ (Ross 7.5; Grimmett 3.7).",
  hint='If you refine a guess with the fuel load and then forget the fuel load again, what do you get back?',
  bd=[r"<strong>$\mathbb E[Y\mid X_1,X_2]$ = the finer guess.</strong> The average lap time given both the tyre age and the fuel load.",
      r"<strong>$\mathbb E[\cdot\mid X_1]$ = then forget the fuel.</strong> Averaging the finer guess over what $X_1$ does not fix lands on the coarser guess.",
      r"<strong>$g(X)\mathbb E[Y\mid X]$ = known factors come out.</strong> Given $X$, $g(X)$ is not random, so it passes through the average."],
  conn='<strong>Refine, then coarsen.</strong> Averaging the detailed forecast (tyre age and fuel load) over the fuel loads you do not know brings you back to the forecast from tyre age alone.',
  cap='Y, then the finer guess 𝔼[Y | X₁, X₂] (tyre age, fuel load), then the coarser 𝔼[Y | X₁]. Forgetting X₂ again gives 𝔼[𝔼[Y | X₁, X₂] | X₁] = 𝔼[Y | X₁].'),
31204: dict(d=d4, kind="THEOREM",
  stmt=r"<b>Law of total variance.</b> If $\mathbb E[Y^2]<\infty$, $\operatorname{Var}(Y)=\mathbb E[\operatorname{Var}(Y\mid X)]+\operatorname{Var}(\mathbb E[Y\mid X])$. Hence the minimum mean squared error of estimating $Y$ from $X$ is $\mathbb E[\operatorname{Var}(Y\mid X)]$ (Ross 7.5; Grimmett 3.7).",
  hint="How does the total spread of Max's lap times split into the part the tyre compound explains and the part that stays noise?",
  bd=[r"<strong>$\operatorname{Var}(\mathbb E[Y\mid X])$ = the signal.</strong> How much the average lap time moves from one compound (soft, medium, hard) to another.",
      r"<strong>$\mathbb E[\operatorname{Var}(Y\mid X)]$ = the noise.</strong> The average leftover spread of lap times within one compound.",
      r"<strong>$=\operatorname{Var}(Y)$ = they add.</strong> The noise part is exactly the minimum mean squared error."],
  conn="<strong>Between compounds and within a compound.</strong> Part of the variation in Max's lap times comes from which compound he is on, and part is lap-to-lap noise on the same compound. Together they make up the total variation, and the noise is your unavoidable error.",
  cap='One bar for Var(Y), split into the signal Var(𝔼[Y | X]) between compounds and the noise 𝔼[Var(Y | X)] within a compound. The noise segment is the minimum mean squared error.'),
31205: dict(d=d5, kind="THEOREM",
  stmt=r"<b>MMSE versus LLSE.</b> For $\mathbb E[Y^2]<\infty$, $\mathbb E[(Y-\mathbb E[Y\mid X])^2]\le\mathbb E[(Y-\hat Y_{\rm LLSE})^2]\le\operatorname{Var}(Y)$, since the linear estimators are a subset of all functions of $X$ and constants are a subset of linear ones. They coincide iff $\mathbb E[Y\mid X]$ is affine in $X$, e.g. jointly Gaussian $(X,Y)$ (Grimmett 7.9).",
  hint='When does a straight-line guess lose to the curve of slice averages, and when do they agree?',
  bd=[r"<strong>$\mathbb E[(Y-\mathbb E[Y\mid X])^2]$ = error of the best curve.</strong> The smallest error over all functions of $X$.",
      r"<strong>$\mathbb E[(Y-\hat Y_{\rm LLSE})^2]$ = error of the best line.</strong> Larger or equal, since lines are a smaller family to choose from.",
      r"<strong>$\le\operatorname{Var}(Y)$ = never worse than ignoring $X$.</strong> The constant guess $\mu_Y$ is itself a linear estimator."],
  conn='<strong>Line versus curve.</strong> Tyres matter in a curved way: the lap time barely moves for 20 laps, then the tyres fall off a cliff. A straight-line rule loses to the curve. If the link were straight, the two would give the same guess.',
  cap="Data around a curved relationship, the best curve 𝔼[Y | X] and the straight LLSE line (dashed). The curve's error is smaller, which in turn is at most Var(Y)."),
31206: dict(d=d6, kind="WORKED EXAMPLE",
  stmt=r"<b>Poisson thinning via Eve's law.</b> Let $N\sim\mathrm{Poisson}(\lambda)$ and, given $N$, $K\sim\mathrm{Bin}(N,p)$. Then $\mathbb E[K]=\mathbb E[Np]=\lambda p$ and $\operatorname{Var}(K)=\mathbb E[Np(1-p)]+\operatorname{Var}(Np)=\lambda p(1-p)+\lambda p^2=\lambda p$. In fact $K\sim\mathrm{Poisson}(\lambda p)$ (Ross 7.5).",
  hint='Of the yellow-flag incidents in a race, a share p bring out the safety car. What are the mean and variance of the number of safety cars?',
  bd=[r"<strong>$\mathbb E[K\mid N]=Np$ = given $N$ incidents, a share $p$ bring a safety car.</strong> Averaging over $N$ gives $\mathbb E[K]=\lambda p$.",
      r"<strong>$\mathbb E[Np(1-p)]=\lambda p(1-p)$ = the noise.</strong> Given $N$, the number of safety cars is binomial with variance $Np(1-p)$.",
      r"<strong>$\operatorname{Var}(Np)=p^2\lambda$ = the signal.</strong> The number of incidents itself varies; the two parts add to $\lambda p$, mean equals variance."],
  conn='<strong>Only the big incidents.</strong> Incidents happen at random during a race, and each is serious enough for a safety car with chance $p$. The safety cars then arrive randomly too, as if only they existed: Poisson with the thinned rate.',
  cap='Poisson(λ) incidents, each bringing out the safety car with chance p: 𝔼[K] = λp. Var(K) = 𝔼[Np(1−p)] + Var(Np) = λp, so mean equals variance, as for a Poisson(λp) count.'),
}

STORY = {
31201: dict(s="STORY 12 · STEP 1 · THE BEST GUESS", b="With no restriction on form, the best guess is <b>the average of Y on each slice of X</b>.", f=[["31103", "the best line"], ["30704", "conditional density"]], n=[["31202", "why it is best"], ["31205", "line versus curve"]]),
31202: dict(s="STORY 12 · STEP 2 · THE SHORTEST MISS, AGAIN", b="The error is orthogonal to <b>every function</b> of X, not just lines.", f=[["31102", "linear orthogonality"], ["31201", "conditional expectation"]], n=[["31203", "rules for computing"]]),
31203: dict(s="STORY 12 · STEP 3 · RULES", b="Refining then forgetting information returns the coarse guess; <b>known factors come out</b>.", f=[["31202", "projection onto information"]], n=[["31204", "splitting the variance"], ["32601", "martingales"]]),
31204: dict(s="STORY 12 · STEP 4 · SIGNAL AND NOISE", b="<b>Eve's law</b>: total variance is the noise within slices plus the variance of the slice averages.", f=[["31203", "the tower property"], ["30503", "variance"]], n=[["31205", "comparing estimators"], ["31403", "variance of random sums"]]),
31205: dict(s="STORY 12 · STEP 5 · LINE OR CURVE", b="The best curve beats the best line, which beats ignoring X; they agree for <b>Gaussian</b> pairs.", f=[["31201", "MMSE"], ["31103", "LLSE"]], n=[["31304", "Gaussian conditioning"], ["31206", "an example using Eve's law"]]),
31206: dict(s="STORY 12 · STEP 6 · THINNING", b="Eve's law gives mean = variance for a <b>thinned Poisson</b> count.", f=[["31204", "total variance"]], n=[["31402", "Wald's identities"], ["32404", "Poisson thinning in processes"]]),
}

FIX = build(CARDS)
