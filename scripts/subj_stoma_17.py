"""StoMA topic 17 (laws of large numbers). Commute picture: the average of your first n commute times."""
from commute_lib import *

SUBJECT = "StoMA"

def wobble(n_pts, amp, decay, mu_y, x0=30, x1=222, seed=3):
    import random
    r = random.Random(seed)
    out = []
    for i in range(n_pts + 1):
        x = x0 + (x1 - x0) * i / n_pts
        out.append((x, mu_y + amp * math.exp(-decay * i / n_pts) * (r.random() - .5) * 2 * (1 if i else 1.4)))
    return out

def d1(c):
    b = 108
    return svg(c, ax(24, b, 226, 18), N(226, 120, "average commute x̄ₙ (min)", 7, "end"),
        fn(lambda x: b - 28 * math.exp(-((x - 124) ** 2) / 2500), 24, 226, 60, 1.1), N(60, 70, "n = 1", 7),
        fn(lambda x: b - 56 * math.exp(-((x - 124) ** 2) / 300), 24, 226, 60, 1.1), N(160, 56, "n = 10", 7, "start"),
        fn(lambda x: b - 84 * math.exp(-((x - 124) ** 2) / 25), 24, 226, 80, 1.1), N(124, 18, "n = 100", 7), dash(124, b, 124, 26), N(124, 120, "μ", 8),
        N(30, 30, "ℙ(|X̄ₙ − μ| ≥ ε) ≤ σ²/(nε²) → 0", 7, "start"), N(120, 138, "the spread of the average collapses like σ²/n", 7))

def d2(c):
    pts = wobble(40, 40, 4.5, 64)
    return svg(c, ax(24, 112, 226, 14), N(226, 124, "n days", 7, "end"), N(28, 14, "x̄ₙ", 7, "start"),
        L(24, 64, 226, 64, 1, "4 3"), N(28, 60, "μ", 8, "start"), L(24, 50, 226, 50, .8, "2 3"), L(24, 78, 226, 78, .8, "2 3"),
        poly(pts, 1.1), N(150, 100, "stays inside ±ε for good", 7, "start"),
        N(120, 138, "ℙ( lim x̄ₙ = μ ) = 1 ⇔ 𝔼|X| < ∞", 7.5))

def d3(c):
    out = ax(24, 100, 226, 20) + N(226, 112, "n", 7, "end") + N(60, 30, "ℙ(|X̄ₙ − μ| ≥ ε)", 7, "start")
    for i in range(10):
        h = 66 / (i + 1) ** 2 * 1.4
        out += R(34 + i * 18, 100 - h, 12, h, "#f1f5f9", 1)
    return svg(c, out, N(120, 11, "𝔼(X̄ₙ − μ)⁴ ≤ C/n²: summable (like 1/n²)", 7.5), N(120, 124, "∑ C/(n²ε⁴) < ∞  ⇒  BC1  ⇒  X̄ₙ → μ a.s.", 7.5),
        N(130, 50, "fourth moment finite", 7, "start"), N(130, 61, "keeps the tail small", 7, "start"), N(120, 138, "(needs 𝔼X⁴ < ∞; the sharp version needs only 𝔼|X| < ∞)", 6.5))

def d4(c):
    xs = [(40, 20), (70, 14), (100, 58), (130, 24), (160, 90), (190, 30), (220, 18)]
    out = ax(24, 112, 226, 14) + N(226, 124, "day n", 7, "end") + N(28, 14, "|Xₙ|", 7, "start")
    out += fn(lambda x: 112 - (x - 24) * 0.45, 24, 226, 20, 1.1, "4 3") + N(60, 40, "cap at n", 7, "start")
    for x, h in xs:
        out += L(x, 112, x, 112 - h, 1) + C(x, 112 - h, 1.8, "#000000" if 112 - h > 112 - (x - 24) * .45 else "#ffffff", 1)
    out += N(120, 130, "Yₙ = Xₙ 1{|Xₙ| ≤ n}: clip the days that exceed the cap", 7)
    out += N(120, 141, "∑ ℙ(Xₙ ≠ Yₙ) ≤ 𝔼|X| < ∞: only finitely many days are clipped", 6.5)
    return svg(c, out)

def d5(c):
    pts = wobble(30, 36, 3.5, 66, 112, 222, 5)
    return svg(c, N(60, 14, "WLLN: snapshot at one n", 7), L(24, 112, 100, 112, 1, ar=True), L(60, 112, 60, 20, 1, "3 2"),
        fn(lambda y: 60 + 10 * math.exp(-((y - 66) ** 2) / 600) * 2.4, 24, 110, 40, 1) if False else "",
        *[C(60 + dx, 66 + dy, 1.6) for dx, dy in [(-3, 12), (4, -10), (-5, -2), (2, 20), (6, 4), (-2, -18), (0, 6), (5, 26)]],
        N(60, 124, "n fixed", 7), N(170, 14, "SLLN: whole path after n", 7), ax(112, 112, 226, 20), L(112, 66, 226, 66, 1, "4 3"),
        poly(pts, 1.1), L(150, 112, 150, 20, 1, "3 2"), N(150, 124, "n", 7),
        N(120, 138, "SLLN controls the whole tail ∪ₖ≥ₙ at once: a path property", 7))

def d6(c):
    import random
    r = random.Random(11)
    pts, s = [], 0
    for i in range(1, 41):
        v = math.tan(math.pi * (r.random() - .5))
        s += v
        pts.append((24 + i * 5, 64 - max(-50, min(50, s / i * 6))))
    return svg(c, ax(24, 112, 226, 14), N(226, 124, "n", 7, "end"), N(28, 14, "x̄ₙ", 7, "start"), L(24, 64, 226, 64, 1, "4 3"),
        poly(pts, 1.1), N(30, 28, "Cauchy days: no mean exists", 7, "start"),
        N(120, 130, "φ(X̄ₙ)(t) = [e^(−|t|/n)]ⁿ = e^(−|t|): X̄ₙ has the same law as X₁", 7), N(120, 141, "averaging never helps: the average never settles", 7))

CARDS = {
31701: dict(d=d1, kind="THEOREM",
  stmt=r"<b>Weak law of large numbers.</b> Let $X_1,X_2,\ldots$ be i.i.d. with mean $\mu$ and finite variance $\sigma^2$. Then $\bar X_n=\frac1n\sum_{i=1}^nX_i\xrightarrow{P}\mu$; indeed $\mathbb P(|\bar X_n-\mu|\ge\varepsilon)\le\dfrac{\sigma^2}{n\varepsilon^2}$ (Ross 8.2; Grimmett 7.4).",
  hint="Why does the average of many commute times home in on the true mean?",
  bd=[r"<strong>$\bar X_n$ = the average of the first $n$ days.</strong> Its mean is $\mu$ for every $n$.",
      r"<strong>$\operatorname{Var}(\bar X_n)=\sigma^2/n$ = the spread shrinks.</strong> Independent days average out: the variance of the average falls like $1/n$.",
      r"<strong>$\le\sigma^2/(n\varepsilon^2)\to0$ = Chebyshev.</strong> The chance that the average is off by $\varepsilon$ or more shrinks to zero."],
  conn=r"<strong>Averaging smooths out the days.</strong> One commute can be anything. The average of 100 commutes is rarely more than a minute from your true typical commute: the bell around the mean gets narrower and narrower.",
  cap="The law of the average X̄ₙ for n = 1, 10, 100: a bell around μ that narrows like σ²/n. By Chebyshev, ℙ(|X̄ₙ − μ| ≥ ε) ≤ σ²/(nε²) → 0."),
31702: dict(d=d2, kind="THEOREM",
  stmt=r"<b>Strong law of large numbers.</b> Let $X_1,X_2,\ldots$ be i.i.d. Then $\mathbb P\bigl(\lim_n\frac1n\sum_{i=1}^nX_i=\mu\bigr)=1$ if and only if $\mathbb E|X|<\infty$, in which case $\mu=\mathbb E[X]$ (Kolmogorov; Grimmett 7.5; Durrett 2.4).",
  hint="Not just any snapshot: does a single endless run of commutes settle at the mean for sure?",
  bd=[r"<strong>$\frac1n\sum X_i$ = the running average along one run of days.</strong> Follow a single infinite sequence of mornings.",
      r"<strong>$\mathbb P(\lim\ldots=\mu)=1$ = this run settles at $\mu$ with probability 1.</strong> Almost every run of days has a running average that converges to the true mean.",
      r"<strong>$\iff\mathbb E|X|<\infty$ = exactly when a mean exists.</strong> If $\mathbb E|X|=\infty$ the running average fails to converge a.s."],
  conn=r"<strong>Your own average commute settles.</strong> Keep a running average of your commute. With probability 1, it ends up within any tiny band around the true mean and stays there for ever.",
  cap="One infinite run: the running average x̄ₙ wobbles, then enters the band μ ± ε and stays there. The SLLN says this happens for almost every run when 𝔼|X| < ∞."),
31703: dict(d=d3, kind="THEOREM",
  stmt=r"<b>Strong law under a fourth moment.</b> If $X_i$ are i.i.d. with $\mathbb E[X^4]<\infty$, then $\mathbb E[(\bar X_n-\mu)^4]\le C/n^2$, so $\sum_n\mathbb P(|\bar X_n-\mu|\ge\varepsilon)\le\sum_n\frac{C}{n^2\varepsilon^4}<\infty$, and by the first Borel–Cantelli lemma $\bar X_n\to\mu$ almost surely (Grimmett 7.5; Durrett 2.4).",
  hint="How does a finite fourth moment make the chances of missing the mean add up to a finite number?",
  bd=[r"<strong>$\mathbb E[(\bar X_n-\mu)^4]\le C/n^2$ = the fourth moment of the average.</strong> Expanding the fourth power, only $O(n^2)$ products of centred terms survive, out of $n^4$, and dividing by $n^4$ leaves $C/n^2$.",
      r"<strong>$\mathbb P(|\bar X_n-\mu|\ge\varepsilon)\le\frac{C}{n^2\varepsilon^4}$ = Markov on the fourth power.</strong> A fourth-moment bound turns into a bound on the chance of a miss.",
      r"<strong>$\sum1/n^2<\infty\Rightarrow$ BC1 $\Rightarrow$ a.s.</strong> Summable chances give finitely many misses, so the running average converges a.s."],
  conn=r"<strong>Why misses stop for good.</strong> The chance that day $n$'s average is off by a minute shrinks like $1/n^2$. Those chances add up to a finite number, so there is a last day on which you are off by that much.",
  cap="The bound ℙ(|X̄ₙ − μ| ≥ ε) ≤ C/(n²ε⁴), drawn as bars shrinking like 1/n². The sum is finite, so Borel–Cantelli gives X̄ₙ → μ almost surely."),
31704: dict(d=d4, kind="THEOREM",
  stmt=r"<b>Kolmogorov's SLLN and truncation.</b> $\bar X_n\to\mu$ a.s. iff $\mathbb E|X|<\infty$. Sketch: put $Y_n=X_n\mathbf 1_{\{|X_n|\le n\}}$. Then $\sum_n\mathbb P(X_n\ne Y_n)=\sum_n\mathbb P(|X|>n)\le\mathbb E|X|<\infty$, so $X_n=Y_n$ eventually (Borel–Cantelli), and the truncated variables have bounded variance sums (Grimmett 7.5; Durrett 2.4).",
  hint="How do you tame an unbounded day by clipping it, and why do only finitely many days get clipped?",
  bd=[r"<strong>$Y_n=X_n\mathbf 1_{\{|X_n|\le n\}}$ = clip the big days.</strong> Replace a day by 0 if it exceeds a cap that grows with $n$.",
      r"<strong>$\sum\mathbb P(X_n\ne Y_n)\le\mathbb E|X|$ = few days are clipped.</strong> The chances $\mathbb P(|X|>n)$ sum to at most $\mathbb E|X|$, which is finite.",
      r"<strong>Borel–Cantelli = finitely many clipped days.</strong> After some day $X_n=Y_n$, so the clipped and original averages have the same limit."],
  conn=r"<strong>Ignore the freak days.</strong> Cap each morning's delay at a level that grows slowly with the day number. Only finitely many days ever exceed their cap, so capping does not change where the running average ends up.",
  cap="Each day's |Xₙ| and the growing cap n. Days above the cap are clipped (open dots): Yₙ = Xₙ1{|Xₙ| ≤ n}. Only finitely many days are clipped since ∑ℙ(Xₙ ≠ Yₙ) ≤ 𝔼|X|."),
31705: dict(d=d5, kind="THEOREM",
  stmt=r"<b>WLLN versus SLLN.</b> The WLLN says $\mathbb P(|\bar X_n-\mu|\ge\varepsilon)\to0$ for each fixed $\varepsilon$ (a statement about the law at each time $n$). The SLLN says $\mathbb P\bigl(\bigcup_{k\ge n}\{|\bar X_k-\mu|\ge\varepsilon\}\bigr)\to0$ as $n\to\infty$ (a statement about the whole path after $n$) (Grimmett 7.2, 7.5).",
  hint="What does a law about one day say, compared with a law about the whole future of a run?",
  bd=[r"<strong>$\mathbb P(|\bar X_n-\mu|\ge\varepsilon)\to0$ = a snapshot.</strong> On any chosen day $n$, a miss is unlikely; different days may have different unlucky runs.",
      r"<strong>$\bigcup_{k\ge n}\{|\bar X_k-\mu|\ge\varepsilon\}$ = any miss from day $n$ on.</strong> The union of all later misses is the event that the path ever leaves the band again.",
      r"<strong>$\to0$ = the path stays inside.</strong> Even the chance of ever leaving the band after day $n$ goes to 0: stronger than the snapshot."],
  conn=r"<strong>One day versus the rest of your life.</strong> The weak law promises that on day 1000 your average is almost surely close. The strong law promises that from some day on it is close on every later day too.",
  cap="Left: the weak law is a statement about the spread of values on one fixed day n. Right: the strong law is about a whole path, which must stay in the band for all days after n."),
31706: dict(d=d6, kind="WORKED EXAMPLE",
  stmt=r"<b>Failure for the Cauchy law.</b> If $X_i$ are i.i.d. standard Cauchy, $\phi_X(t)=e^{-|t|}$, so $\phi_{\bar X_n}(t)=\bigl[e^{-|t|/n}\bigr]^n=e^{-|t|}$ and $\bar X_n\overset d=X_1$ for every $n$. Hence $\bar X_n$ does not converge to a constant: the laws of large numbers fail since $\mathbb E|X|=\infty$ (Grimmett 5.10).",
  hint="What happens to the average if single days can be so extreme that no mean exists?",
  bd=[r"<strong>$\phi_{\bar X_n}(t)=\bigl[\phi_X(t/n)\bigr]^n$ = the average's characteristic function.</strong> Independence turns the sum into a product of $n$ equal factors.",
      r"<strong>$\bigl[e^{-|t|/n}\bigr]^n=e^{-|t|}$ = nothing changes.</strong> The $n$ factors combine exactly back to $e^{-|t|}$, the characteristic function of one day.",
      r"<strong>$\bar X_n\overset d=X_1$ = averaging does not help.</strong> The average of $n$ days is as wild as one day, so it never settles."],
  conn=r"<strong>Days with freak outliers.</strong> If occasionally a day is so extreme that it dwarfs everything before it, the running average keeps being thrown off, however many days you average.",
  cap="The running average of Cauchy days keeps jumping instead of settling at a mean, because φ(X̄ₙ)(t) = e^(−|t|) for every n: the average is no tamer than one day."),
}

STORY = {
31701: dict(s="STORY 17 · STEP 1 · THE SPREAD COLLAPSES", b="The <b>weak law</b>: the average of many independent days has variance σ²/n, so it concentrates at μ.", f=[["30602", "Chebyshev"], ["30503", "variance of a sum"], ["31501", "convergence in probability"]], n=[["31702", "a statement about whole runs"], ["31705", "snapshot versus path"]]),
31702: dict(s="STORY 17 · STEP 2 · EVERY RUN SETTLES", b="The <b>strong law</b>: almost every infinite run's running average converges to the mean.", f=[["31701", "weak law"], ["31605", "limits of events"]], n=[["31703", "a proof from the fourth moment"], ["31704", "the sharp condition"]]),
31703: dict(s="STORY 17 · STEP 3 · A PROOF", b="A fourth moment gives <b>summable</b> miss chances, and BC1 converts them into a.s. convergence.", f=[["31605", "a.s. via Borel–Cantelli"], ["30601", "Markov's inequality"]], n=[["31704", "removing the fourth-moment assumption"]]),
31704: dict(s="STORY 17 · STEP 4 · THE SHARP LAW", b="<b>Truncation</b> shows the strong law holds exactly when 𝔼|X| is finite.", f=[["31703", "the fourth-moment proof"], ["31602", "first Borel–Cantelli"]], n=[["31706", "what fails without it"]]),
31705: dict(s="STORY 17 · STEP 5 · SNAPSHOT VERSUS TRAJECTORY", b="Weak is about <b>each day separately</b>, strong is about the <b>whole future path</b>.", f=[["31701", "WLLN"], ["31702", "SLLN"], ["31503", "probability versus a.s."]], n=[["31706", "failure case"]]),
31706: dict(s="STORY 17 · STEP 6 · WHEN AVERAGING FAILS", b="For the <b>Cauchy</b> law the average has the same law as one day: no law of large numbers.", f=[["30406", "the Cauchy law"], ["31704", "needing 𝔼|X| < ∞"]], n=[["31801", "characteristic functions"]]),
}

FIX = build(CARDS)
