"""StoMA topic 14 (random sums, Wald). Commute picture: N stops on the route, each adding a random delay Xᵢ."""
from commute_lib import *

SUBJECT = "StoMA"

def d1(c):
    out = ""
    for i in range(4):
        out += R(30 + i * 40, 52, 32, 20, "#f1f5f9", 1, 3) + N(46 + i * 40, 66, f"X{'₁₂₃₄'[i]}", 8)
    out += R(190, 52, 32, 20, "#ffffff", 1, 3, "3 2") + N(206, 66, "X₅", 8) + L(190, 82, 222, 82, 1, "3 2")
    return svg(c, out, N(110, 40, "N = 4 stops this morning (random)", 7.5), N(206, 94, "not reached", 6.5), L(30, 82, 190, 82, 1.1),
        N(110, 96, "S = X₁ + … + X_N = ∑ Xᵢ 1{N ≥ i}", 7.5) if False else N(110, 96, "S = ∑ Xᵢ 1{N ≥ i}", 7.5),
        N(120, 116, "{N ≥ i} is decided before stop i: the indicator is independent of Xᵢ", 6.8), N(120, 130, "(N is a stopping time)", 7))

def d2(c):
    return svg(c, ax(24, 112, 226, 14), N(226, 124, "number of stops", 7, "end"), N(28, 14, "delay per stop", 7, "start"),
        R(24, 52, 110, 60, "#d9dee7", 1), N(79, 86, "area = 𝔼[S]", 8), N(79, 124, "𝔼[N]", 7.5), N(18, 84, "𝔼[X]", 7.5, "end"),
        N(146, 40, "𝔼[S] = 𝔼[N] · 𝔼[X]", 8, "start"), N(146, 54, "needs 𝔼[N] < ∞,", 7, "start"), N(146, 64, "𝔼|X| < ∞", 7, "start"),
        N(146, 82, "N must be a stopping", 7, "start"), N(146, 92, "rule: no peeking ahead", 7, "start"))

def d3(c):
    return svg(c, R(30, 56, 180, 24, "#ffffff", 1), R(30, 56, 100, 24, "#d9dee7", 1), L(130, 56, 130, 80, 1),
        N(80, 72, "𝔼[N] Var(X)", 8), N(170, 72, "(𝔼X)² Var(N)", 8),
        N(80, 96, "noise within each stop", 7), N(170, 96, "noise in how many stops", 7),
        N(120, 22, "Var(S) = 𝔼[N] Var(X) + (𝔼[X])² Var(N)", 8), N(120, 124, "two sources of randomness: stop delays and stop count", 7))

def d4(c):
    out = ""
    for x, lab in [(20, "t"), (88, "M(t) of one stop"), (164, "G(·) of the count")]:
        w = 40 if x == 20 else (62 if x == 88 else 56)
        out += R(x, 56, w + (10 if x == 164 else 0), 22, "#f1f5f9", 1, 3) + N(x + (w + (10 if x == 164 else 0)) / 2, 71, lab, 7)
    return svg(c, out, arrow(60, 67, 88, 67, 1), arrow(150, 67, 164, 67, 1), N(120, 20, "M_S(t) = G_N(M_X(t))", 8) if False else N(120, 20, "MGF of total = G of N applied to the stop MGF", 7.5),
        N(120, 100, "M(S)(t) = G(N)(M(X)(t))     G(S)(s) = G(N)(G(X)(s))", 7) if False else N(120, 100, "𝔼[e^(tS)] = Gₙ(Mₓ(t))   and   𝔼[s^S] = Gₙ(Gₓ(s))", 7.5),
        N(120, 120, "condition on N: the stops multiply, then average the power over N", 7))

def d5(c):
    out = C(40, 74, 3)
    kids = [[(78, 54), (78, 94)], [(116, 40), (116, 66), (116, 90), (116, 112)]]
    for (x, y) in kids[0]: out += L(40, 74, x, y, 1) + C(x, y, 3)
    for (x, y) in kids[1]: out += L(78, 54, x, y, 1) if y < 80 else L(78, 94, x, y, 1)
    for (x, y) in kids[1]: out += C(x, y, 3)
    out += N(40, 90, "Z₀", 7.5) + N(78, 124, "Z₁", 7.5) + N(116, 130, "Z₂", 7.5) + N(70, 24, "each late bus delays ξ others", 7, "start")
    out += ax(150, 112, 226, 40) + N(226, 124, "s", 7, "end") + fn(lambda s: 112 - (0.2 + 0.1 * (s - 150) / 76 + 0.7 * ((s - 150) / 76) ** 2) * 72, 150, 226, 30, 1.1) + L(150, 112, 226, 40, 1, "3 2")
    out += N(176, 34, "π₀ = smallest root of s = G(s)", 7, "start") if False else N(150, 34, "π₀: smallest s with s = G(s)", 7, "start")
    out += N(150, 140, "𝔼[Zₙ] = μⁿ: dies out if μ ≤ 1", 7, "start")
    return svg(c, out)

def d6(c):
    xs = [(34, 10), (68, 26), (104, 18), (150, 34), (196, 14)]
    out = ax(24, 112, 226, 14) + N(226, 124, "time", 7, "end") + N(28, 14, "total delay S(t)", 7, "start")
    y = 108
    for i, (x, h) in enumerate(xs):
        nx = xs[i + 1][0] if i + 1 < len(xs) else 226
        out += L(x, y, nx, y, 1.2)
        out += L(nx, y, nx, y - (xs[i + 1][1] if i + 1 < len(xs) else 0), 1) if i + 1 < len(xs) else ""
        y -= xs[i + 1][1] if i + 1 < len(xs) else 0
    out += N(30, 58, "Poisson(λ) delay incidents,", 7, "start") + N(30, 69, "sizes Xᵢ ~ Exp(β)", 7, "start")
    out += N(30, 30, "𝔼[S] = λ 𝔼[X]", 7.5, "start") + N(30, 42, "Var(S) = λ 𝔼[X²] = 2λ/β²", 7.5, "start")
    out += N(120, 138, "variance of a compound Poisson uses the SECOND moment of the jumps", 6.5)
    return svg(c, out)

CARDS = {
31401: dict(d=d1, kind="DEFINITION",
  stmt=r"<b>Random sums.</b> Let $X_1,X_2,\ldots$ be i.i.d. and $N\ge0$ integer-valued. The random sum is $S_N=\sum_{i=1}^NX_i=\sum_{i=1}^\infty X_i\mathbf 1_{\{N\ge i\}}$. If $N$ is a stopping time ($\{N\ge i\}\in\sigma(X_1,\ldots,X_{i-1})$) or independent of $(X_i)$, then $\mathbf 1_{\{N\ge i\}}$ is independent of $X_i$ (Ross 7.5; Grimmett 5.1).",
  hint="If the number of stops is itself random, when can you still treat each stop's delay as separate from whether it is reached?",
  bd=[r"<strong>$S_N=\sum_{i=1}^NX_i$ = total delay over $N$ stops.</strong> Both the number of terms and each term are random.",
      r"<strong>$\sum X_i\mathbf 1_{\{N\ge i\}}$ = switch each stop on or off.</strong> Stop $i$ contributes only if you get at least that far; this turns it into an infinite sum with fixed length.",
      r"<strong>$\{N\ge i\}\in\sigma(X_1,\ldots,X_{i-1})$ = decided before stop $i$.</strong> Whether you reach stop $i$ depends only on earlier delays, so the switch is independent of $X_i$."],
  conn=r"<strong>A route with a random number of stops.</strong> You ride until something happens: you reach campus, or the bus breaks. Whether you board stop $i$ is decided by what happened earlier, not by that stop's own delay.",
  cap="N = 4 stops are reached this morning, each adding a delay Xᵢ; X₅ is not reached. S = ∑ Xᵢ 1{N ≥ i}, and the switch 1{N ≥ i} is independent of Xᵢ."),
31402: dict(d=d2, kind="THEOREM",
  stmt=r"<b>Wald's first identity.</b> Let $X_1,X_2,\ldots$ be i.i.d. with $\mathbb E|X|<\infty$ and $N$ a stopping time with $\mathbb E[N]<\infty$. Then $\mathbb E\bigl[\sum_{i=1}^NX_i\bigr]=\mathbb E[N]\,\mathbb E[X]$ (Ross 7.5; Grimmett 12.5).",
  hint="With a random number of stops, what is the average total delay?",
  bd=[r"<strong>$\mathbb E[N]$ = the average number of stops.</strong> How far the typical morning gets.",
      r"<strong>$\mathbb E[X]$ = the average delay at one stop.</strong> The same for every stop, since the delays are identically distributed.",
      r"<strong>$\mathbb E[N]\,\mathbb E[X]$ = the product.</strong> Write $S_N=\sum X_i\mathbf 1_{\{N\ge i\}}$ and take expectations term by term; the switch is independent of $X_i$, so each term is $\mathbb E[X]\mathbb P(N\ge i)$ and $\sum\mathbb P(N\ge i)=\mathbb E[N]$."],
  conn=r"<strong>Average stops times average delay.</strong> If you ride past 6 stops on average and each adds 2 minutes on average, the average total delay is 12 minutes, even though the number of stops is random.",
  cap="A rectangle of width 𝔼[N] (average stops) and height 𝔼[X] (average delay per stop). Its area is 𝔼[S] = 𝔼[N]·𝔼[X]."),
31403: dict(d=d3, kind="THEOREM",
  stmt=r"<b>Wald's second identity.</b> If $N$ is independent of the i.i.d. $X_i$ with finite second moments, then $\operatorname{Var}\bigl(\sum_{i=1}^NX_i\bigr)=\mathbb E[N]\operatorname{Var}(X)+(\mathbb E[X])^2\operatorname{Var}(N)$ (Ross 7.5; Grimmett 3.7).",
  hint="With a random number of stops, where do the two sources of randomness show up in the variance of the total delay?",
  bd=[r"<strong>$\mathbb E[N]\operatorname{Var}(X)$ = randomness of each stop's delay.</strong> On average $\mathbb E[N]$ stops, each adding its own variance.",
      r"<strong>$(\mathbb E[X])^2\operatorname{Var}(N)$ = randomness in how many stops.</strong> A change of one stop shifts the total by $\mathbb E[X]$, so the count's variance is scaled by $(\mathbb E[X])^2$.",
      r"<strong>The sum = Eve's law.</strong> $\mathbb E[\operatorname{Var}(S\mid N)]=\mathbb E[N]\operatorname{Var}(X)$ and $\operatorname{Var}(\mathbb E[S\mid N])=\operatorname{Var}(N\mathbb E[X])$."],
  conn=r"<strong>Two reasons mornings differ.</strong> Some mornings differ because individual stops go well or badly; some because the route is longer or shorter. The total variation adds both reasons.",
  cap="A bar for Var(S) split into 𝔼[N]Var(X), the variation of the delays at each stop, and (𝔼[X])²Var(N), the variation of how many stops there are."),
31404: dict(d=d4, kind="THEOREM",
  stmt=r"<b>Compound generating functions.</b> If $N$ is independent of the i.i.d. $X_i$, then $M_{S_N}(t)=G_N\bigl(M_X(t)\bigr)$, and for $X_i\in\{0,1,2,\ldots\}$, $G_{S_N}(s)=G_N\bigl(G_X(s)\bigr)$ (Ross 7.7; Grimmett 5.1).",
  hint="How do you find the generating function of a random sum from those of the count and of one term?",
  bd=[r"<strong>$M_X(t)$ = the MGF of one stop's delay.</strong> Given $N=n$, independent stops multiply: $\mathbb E[e^{tS}\mid N=n]=M_X(t)^n$.",
      r"<strong>$G_N(u)=\mathbb E[u^N]$ = the count's generating function.</strong> Averaging $u^N$ over $N$, with $u=M_X(t)$.",
      r"<strong>$G_N(M_X(t))$ = compose.</strong> The same works for counts: $G_{S_N}(s)=G_N(G_X(s))$. Differentiating at $s=1$ gives Wald's identities."],
  conn=r"<strong>Plug one into the other.</strong> To describe the total delay, take the description of one stop's delay and feed it into the description of the number of stops. The nesting mirrors the nesting of the randomness.",
  cap="A chain of boxes: the argument t goes into the stop's MGF Mₓ(t), whose value is fed into the count's generating function Gₙ, giving the MGF of the total delay."),
31405: dict(d=d5, kind="THEOREM",
  stmt=r"<b>Galton–Watson process.</b> Let $Z_0=1$ and $Z_{n+1}=\sum_{i=1}^{Z_n}\xi_{n,i}$ with i.i.d. offspring counts $\xi$, mean $\mu$ and PGF $G$. Then $\mathbb E[Z_n]=\mu^n$, and the extinction probability $\pi_0=\mathbb P(Z_n=0\text{ for some }n)$ is the smallest root of $s=G(s)$ in $[0,1]$; $\pi_0=1$ iff $\mu\le1$ (excluding $\xi\equiv1$) (Ross 4.7; Grimmett 5.4).",
  hint="If each late bus delays a random number of the buses behind it, when does the cascade die out for sure?",
  bd=[r"<strong>$Z_{n+1}=\sum_{i\le Z_n}\xi_{n,i}$ = a random sum.</strong> Each of the $Z_n$ late buses in generation $n$ causes its own number of late buses in the next.",
      r"<strong>$\mathbb E[Z_n]=\mu^n$ = Wald, generation by generation.</strong> The expected size is multiplied by $\mu$ each time: it grows if $\mu>1$ and shrinks if $\mu<1$.",
      r"<strong>$\pi_0=G(\pi_0)$ = the extinction chance.</strong> The chain dies out if its first generation's lines all die out: the smallest solution of $s=G(s)$; it is 1 when $\mu\le1$."],
  conn=r"<strong>A delay that spreads.</strong> One late bus makes some following buses late, each of which delays others in turn. If on average a late bus makes at most one other late, the cascade surely dies out; otherwise it may take off.",
  cap="A generation tree Z₀, Z₁, Z₂ of delayed buses, and the PGF G(s) against the line y = s. The extinction probability π₀ is the smallest s where they meet."),
31406: dict(d=d6, kind="WORKED EXAMPLE",
  stmt=r"<b>Compound Poisson (Lundberg) model.</b> Let $N\sim\mathrm{Poisson}(\lambda)$ be independent of i.i.d. $X_i$ (for example $X_i\sim\mathrm{Exp}(\beta)$) and $S=\sum_{i=1}^NX_i$. Then $\mathbb E[S]=\lambda\,\mathbb E[X]$ and $\operatorname{Var}(S)=\lambda\,\mathbb E[X^2]$, which equals $\dfrac{2\lambda}{\beta^2}$ for exponential claims (Ross 7.5; Grimmett 6.8).",
  hint="Delay incidents arrive as a Poisson stream, each adding a random amount. What are the mean and variance of the total?",
  bd=[r"<strong>$\mathbb E[S]=\lambda\mathbb E[X]$ = rate times mean size.</strong> The average number of incidents times the average delay of one.",
      r"<strong>$\operatorname{Var}(S)=\lambda\mathbb E[X^2]$ = rate times the second moment.</strong> Wald II with $\mathbb E[N]=\operatorname{Var}(N)=\lambda$ gives $\lambda\operatorname{Var}X+\lambda(\mathbb EX)^2$.",
      r"<strong>$2\lambda/\beta^2$ = exponential sizes.</strong> For $X\sim\mathrm{Exp}(\beta)$, $\mathbb E[X^2]=2/\beta^2$, so large claims drive the variance."],
  conn=r"<strong>Delay incidents through the day.</strong> Breakdowns and jams arrive at random, each costing some random minutes. The total lost time has an average of rate times average cost, and a spread driven by the big incidents.",
  cap="The total delay S(t) jumps by Xᵢ at each Poisson incident. Its mean is λ𝔼[X] and its variance λ𝔼[X²], which equals 2λ/β² for exponential jump sizes."),
}

STORY = {
31401: dict(s="STORY 14 · STEP 1 · A RANDOM NUMBER OF STOPS", b="A <b>random sum</b> adds a random number of random terms; switching terms on and off turns it into a fixed-length sum.", f=[["30501", "linearity of expectation"], ["30505", "counts"]], n=[["31402", "its mean"], ["31403", "its variance"]]),
31402: dict(s="STORY 14 · STEP 2 · THE MEAN", b="<b>Wald I</b>: the mean of a random sum is mean count times mean term.", f=[["31401", "random sums"]], n=[["31403", "the variance"], ["32605", "Wald from optional stopping"]]),
31403: dict(s="STORY 14 · STEP 3 · THE VARIANCE", b="<b>Wald II</b>: two sources of randomness, the terms and the count.", f=[["31402", "Wald I"], ["31204", "Eve's law"]], n=[["31404", "the whole distribution"]]),
31404: dict(s="STORY 14 · STEP 4 · THE WHOLE LAW", b="Generating functions of random sums are <b>compositions</b> G_N(M_X(t)).", f=[["30504", "MGFs"], ["30505", "PGFs"]], n=[["31405", "iterating the composition"], ["31406", "the Poisson case"]]),
31405: dict(s="STORY 14 · STEP 5 · CASCADES", b="Iterating random sums gives <b>branching</b>: extinction is the smallest root of s = G(s).", f=[["31404", "composition of PGFs"]], n=[["31901", "chains as dynamic processes"]]),
31406: dict(s="STORY 14 · STEP 6 · INCIDENTS", b="A Poisson count of random costs gives the <b>compound Poisson</b> total, with variance from the second moment.", f=[["31403", "Wald II"], ["30304", "exponential sizes"]], n=[["32404", "thinning and superposition"]]),
}

FIX = build(CARDS)
