"""StoMA topic 26 (martingales). Commute picture: your running tally of minutes gained or lost against the schedule: a fair game."""
from commute_lib import *
import random
from subj_lib import box

SUBJECT = "StoMA"

def walk(seed, n=40, x0=26, x1=222, y=64, k=4, lo=20, hi=108):
    r = random.Random(seed)
    pts, v = [], 0
    for i in range(n + 1):
        pts.append((x0 + (x1 - x0) * i / n, max(lo, min(hi, y - v))))
        v += k if r.random() < .5 else -k
    return pts

def d1(c):
    pts = walk(3, 12, 26, 150, 64, 8)
    return svg(c, ax(24, 64, 226, 14), N(226, 76, "day n", 7, "end"), N(28, 14, "Mₙ", 7.5, "start"), poly(pts, 1), L(150, 20, 150, 108, .8, "3 2"),
        N(150, 16, "today n", 7), N(158, 92, "tomorrow: average", 7, "start"), N(158, 102, "of futures = Mₙ", 7, "start"),
        N(120, 12, "ℱₙ = everything known up to day n", 7.5) if False else N(90, 12, "ℱₙ = all you know by day n", 7),
        N(120, 132, "𝔼[Mₙ₊₁ | ℱₙ] = Mₙ  ⇒  𝔼[Mₙ] = 𝔼[M₀]", 8), N(120, 143, "a fair game: no drift up or down, on average", 7))

def d2(c):
    return svg(c, box(14, 18, 96, 28, "Sₙ − nμ", "#f1f5f9", 8, False), box(130, 18, 96, 28, "Sₙ² − nσ²", "#f1f5f9", 8, False),
        box(14, 64, 96, 28, "e^(θSₙ) / M(θ)ⁿ", "#f1f5f9", 7.5, False), box(130, 64, 96, 28, "Mₙ = 𝔼[Y | ℱₙ]", "#f1f5f9", 7.5, False),
        N(62, 106, "centred total", 7), N(178, 106, "centred square", 7), N(120, 124, "each subtracts off its predictable drift (the compensator)", 7),
        N(120, 137, "what is left is a fair game", 7.5))

def d3(c):
    pts = walk(6, 30, 26, 222, 64, 4)
    cut = 14
    out = ax(24, 64, 226, 14) + poly(pts, 1)
    tx = pts[cut][0]
    out += L(tx, 18, tx, 108, .8, "3 2") + C(tx, pts[cut][1], 2.6, "#000000", 1) + N(tx, 118, "τ", 8)
    out += poly([(x, pts[cut][1]) for x in (tx, 222)], 1, "2 2")
    return svg(c, out, N(120, 11, "stop when the delay first hits a rule", 7), N(120, 130, "{τ ≤ n} ∈ ℱₙ: the decision uses only what is known by day n", 7),
        N(120, 142, "Mₙ∧τ is a martingale and 𝔼[Mₙ∧τ] = 𝔼[M₀]", 8))

def d4(c):
    return svg(c, box(12, 28, 100, 40, "𝔼[M_τ] = 𝔼[M₀]", "#f1f5f9", 8.5, False), box(124, 28, 102, 40, "if  τ ≤ C", "#f1f5f9", 8.5, False),
        box(124, 76, 102, 24, "or |Mₙ∧τ| ≤ K", "#f1f5f9", 7.5, False) if False else "", N(175, 90, "or  |Mₙ∧τ| ≤ K", 8), N(175, 104, "or 𝔼τ < ∞ and |ΔM| ≤ c", 7.5),
        arrow(112, 48, 124, 48, 1), N(120, 14, "when may you stop a fair game?", 7.5),
        N(120, 124, "each condition rules out infinite waiting or unbounded losses", 7), N(120, 136, "(doubling forever breaks it)", 7))

def d5(c):
    out = ax(24, 90, 226, 20) + N(226, 102, "n", 7, "end")
    pts = walk(9, 36, 26, 190, 66, 5, 28, 104)
    out += poly(pts, 1) + L(24, 38, 226, 38, 1, "4 3") + L(24, 100, 226, 100, 1, "4 3") + N(28, 32, "+b", 7, "start") + N(28, 114, "−a", 7, "start") + L(24, 66, 226, 66, .6, "2 3") if False else ""
    out += poly(pts, 1) + L(24, 34, 226, 34, 1, "4 3") + L(24, 104, 226, 104, 1, "4 3") + N(224, 28, "+b", 7, "end") + N(224, 114, "−a", 7, "end")
    return svg(c, out, N(30, 14, "Sₙ", 7, "start"), N(120, 124, "𝔼[S_τ] = 0 ⇒ ℙ(hit +b first) = a/(a + b)", 7), N(120, 134, "𝔼[S_τ² − τ] = 0 ⇒ 𝔼[τ] = ab", 7.5), N(120, 144, "(fair walk between −a and +b)", 6.5))

def d6(c):
    out = ax(24, 100, 226, 20) + N(226, 112, "n", 7, "end")
    pts = walk(12, 30, 26, 222, 64, 3.6, 28, 100)
    out += poly(pts, 1) + L(24, 40, 226, 40, 1, "4 3") + N(28, 34, "λ", 7.5, "start")
    return svg(c, out, N(120, 11, "Doob: ℙ(max Xₖ ≥ λ) ≤ 𝔼[Xₙ]/λ  (non-negative submartingale)", 7),
        N(120, 122, "Azuma: ℙ(|Mₙ − M₀| ≥ t) ≤ 2 exp(−t² / 2∑cₖ²)", 7.5), N(120, 134, "bounded daily moves ⇒ the total rarely strays far", 7), N(120, 144, "(cₖ = the cap on day k's move)", 6.5))

CARDS = {
32601: dict(d=d1, kind="DEFINITION",
  stmt=r"<b>Filtration and martingale.</b> A filtration $(\mathcal F_n)$ is an increasing sequence of σ-fields. $(M_n)$ is a martingale if $M_n$ is $\mathcal F_n$-measurable, $\mathbb E|M_n|<\infty$ and $\mathbb E[M_{n+1}\mid\mathcal F_n]=M_n$. Then $\mathbb E[M_n]=\mathbb E[M_0]$ for all $n\ge0$; with $\ge$ or $\le$ it is a sub- or supermartingale (Williams 10; Grimmett 12.1).",
  hint="What does it mean for a running tally to be a fair game given everything known so far?",
  bd=[r"<strong>$\mathcal F_n$ = what you know by day $n$.</strong> The information grows with $n$; $M_n$ is known from it.",
      r"<strong>$\mathbb E[M_{n+1}\mid\mathcal F_n]=M_n$ = a fair game.</strong> Given the whole past, the expected tally tomorrow is today's tally: no drift up or down.",
      r"<strong>$\mathbb E[M_n]=\mathbb E[M_0]$ = constant mean.</strong> Taking expectations of the martingale property gives a constant expected value for all $n$."],
  conn=r"<strong>A fair tally.</strong> Count minutes gained or lost against the schedule. If on average tomorrow's tally equals today's, whatever has happened, it is a martingale, and on average you end where you started.",
  cap="A running tally Mₙ and the information up to day n. A martingale is a fair game: the average of tomorrow's tally given the past is today's value Mₙ."),
32602: dict(d=d2, kind="THEOREM",
  stmt=r"<b>Canonical martingales.</b> For i.i.d. $X_i$ with mean $\mu$, variance $\sigma^2$ and MGF $M_X(\theta)<\infty$, and $S_n=\sum_{i\le n}X_i$: $S_n-n\mu$, $(S_n-n\mu)^2-n\sigma^2$ and $\dfrac{e^{\theta S_n}}{M_X(\theta)^n}$ are martingales. For any integrable $Y$, $M_n=\mathbb E[Y\mid\mathcal F_n]$ is a martingale (Doob) (Williams 10; Grimmett 12.1).",
  hint="Which natural quantities built from sums of days are fair games?",
  bd=[r"<strong>$S_n-n\mu$ = the centred total.</strong> Subtract the expected drift $n\mu$; the rest has zero mean increments.",
      r"<strong>$(S_n-n\mu)^2-n\sigma^2$ and $e^{\theta S_n}/M_X(\theta)^n$ = compensated square and exponential.</strong> Subtract the compensator $n\sigma^2$, or divide by the MGF to the $n$.",
      r"<strong>$M_n=\mathbb E[Y\mid\mathcal F_n]$ = Doob martingale.</strong> Your best forecast of a final outcome, updated as news arrives, is a fair game."],
  conn=r"<strong>Remove the drift.</strong> The total delay over $n$ days drifts up at the average rate; subtract that drift and you have a fair game. Your forecast of the day's final delay is also a fair game as news arrives.",
  cap="Four martingale families: the centred total Sₙ − nμ, the compensated square Sₙ² − nσ², the exponential martingale, and the forecast Mₙ = 𝔼[Y | ℱₙ]."),
32603: dict(d=d3, kind="THEOREM",
  stmt=r"<b>Stopping times and the stopped martingale.</b> A random time $\tau$ is a stopping time if $\{\tau\le n\}\in\mathcal F_n$ for all $n\ge0$. If $(M_n)$ is a martingale then the stopped process $M_{n\wedge\tau}$ is a martingale, so $\mathbb E[M_{n\wedge\tau}]=\mathbb E[M_0]$ for each $n$ (Williams 10; Grimmett 12.4).",
  hint="If you decide when to stop using only what you know so far, does the game stay fair?",
  bd=[r"<strong>$\{\tau\le n\}\in\mathcal F_n$ = a decision from the past.</strong> Whether you have stopped by day $n$ is determined by the information up to day $n$; no peeking ahead.",
      r"<strong>$M_{n\wedge\tau}$ = the tally frozen at $\tau$.</strong> It follows $M$ until the stopping time and then stays put.",
      r"<strong>$\mathbb E[M_{n\wedge\tau}]=\mathbb E[M_0]$ = still fair.</strong> No rule that uses only the past can turn a fair game into a favourable one, at any fixed horizon $n$."],
  conn=r"<strong>No system beats a fair game.</strong> Leaving the first time the tally hits +10 minutes, or whenever you like based on the past, never changes your expected tally at a fixed day.",
  cap="A tally, stopped at the first time τ a rule is met. The stopped tally Mₙ∧τ follows the path until τ and then stays put; it is still a martingale."),
32604: dict(d=d4, kind="THEOREM",
  stmt=r"<b>Optional stopping theorem.</b> If $(M_n)$ is a martingale and $\tau$ a stopping time, then $\mathbb E[M_\tau]=\mathbb E[M_0]$ provided one of: (a) $\tau\le C$ a.s.; (b) $\tau<\infty$ a.s. and $|M_{n\wedge\tau}|\le K$; (c) $\mathbb E[\tau]<\infty$ and $|M_{n+1}-M_n|\le c$ (Williams 10.10; Grimmett 12.5).",
  hint="When can you stop a fair game at a random time and still expect to leave with what you came with?",
  bd=[r"<strong>$\tau\le C$ = bounded time.</strong> You stop by a fixed deadline, so the stopped-martingale theorem applies at $n=C$.",
      r"<strong>$|M_{n\wedge\tau}|\le K$ = bounded tally.</strong> The tally never exceeds $K$, so passing to the limit $n\to\infty$ is safe (dominated convergence).",
      r"<strong>$\mathbb E[\tau]<\infty$ and $|\Delta M|\le c$ = finite wait, bounded steps.</strong> Then $|M_{n\wedge\tau}|\le|M_0|+c\tau$, which is integrable."],
  conn=r"<strong>A doubling system fails.</strong> Betting double each time until the first win seems to guarantee a profit, but it needs unbounded losses on the way, so none of the conditions hold and the expectation is not preserved.",
  cap="The conclusion 𝔼[M_τ] = 𝔼[M₀] holds under any one of the three conditions: bounded stopping time, bounded stopped tally, or finite mean wait with bounded steps."),
32605: dict(d=d5, kind="WORKED EXAMPLE",
  stmt=r"<b>Gambler's ruin by OST.</b> For a fair simple random walk $S_n$ started at $0$ and $\tau$ the first exit time from $(-a,b)$: $\mathbb E[S_\tau]=0$ gives $\mathbb P(\text{hit }b\text{ first})=\frac a{a+b}$, and $\mathbb E[S_\tau^2-\tau]=0$ gives $\mathbb E[\tau]=ab$ (Wald's identities) (Ross 6.3; Williams 10.12).",
  hint="How do the two fair-game tallies give the chance of success and the expected duration at once?",
  bd=[r"<strong>$\mathbb E[S_\tau]=0$ = the walk is a martingale.</strong> The stopped value is $b$ with chance $p$ and $-a$ with chance $1-p$, so $pb-(1-p)a=0$.",
      r"<strong>$p=\frac a{a+b}$ = the chance of reaching $+b$ first.</strong> Solving $pb=(1-p)a$ gives the fractional position of the start between the two ends.",
      r"<strong>$\mathbb E[S_\tau^2-\tau]=0\Rightarrow\mathbb E[\tau]=ab$ = expected duration.</strong> $\mathbb E[S_\tau^2]=pb^2+(1-p)a^2=ab$."],
  conn=r"<strong>The corridor.</strong> A fair walker between a door at $-a$ and a door at $+b$ reaches the far door with chance $a/(a+b)$, and takes $ab$ steps on average. Two fair-game tallies answer both questions.",
  cap="A fair walk exits the corridor (−a, b) at τ. The martingale Sₙ gives ℙ(hit +b) = a/(a+b); the martingale Sₙ² − n gives 𝔼[τ] = ab."),
32606: dict(d=d6, kind="THEOREM",
  stmt=r"<b>Doob's inequality and Azuma–Hoeffding.</b> For a non-negative submartingale $(X_k)$, $\mathbb P\bigl(\max_{0\le k\le n}X_k\ge\lambda\bigr)\le\frac{\mathbb E[X_n]}\lambda$. For a martingale with $|M_k-M_{k-1}|\le c_k$, $\mathbb P(|M_n-M_0|\ge t)\le2\exp\Bigl(-\frac{t^2}{2\sum_{k=1}^nc_k^2}\Bigr)$ (Williams 14; Grimmett 12.6).",
  hint="How likely is a fair tally ever to get far from its start, in one day or at any time?",
  bd=[r"<strong>$\mathbb P(\max_kX_k\ge\lambda)\le\mathbb E[X_n]/\lambda$ = Doob.</strong> Markov's inequality for the whole running maximum, not just the last value.",
      r"<strong>$|M_k-M_{k-1}|\le c_k$ = capped daily moves.</strong> No single day can move the tally by more than $c_k$.",
      r"<strong>$2\exp(-t^2/2\sum c_k^2)$ = Azuma–Hoeffding.</strong> The tally strays by $t$ with chance that falls off as a Gaussian tail in $t/\sqrt{\sum c_k^2}$."],
  conn=r"<strong>Caps on bad days.</strong> If no single day can add more than a few minutes to the tally, then the chance that the total is far from its start after many days is very small, like a bell's tail.",
  cap="A non-negative tally and the level λ: Doob bounds the chance that its running maximum reaches λ. With capped moves, Azuma bounds the chance the total strays far."),
}

STORY = {
32601: dict(s="STORY 26 · STEP 1 · A FAIR TALLY", b="A <b>martingale</b> is a fair game: the expected next value, given the past, is today's.", f=[["31201", "conditional expectation"], ["32501", "walks"]], n=[["32602", "examples"]]),
32602: dict(s="STORY 26 · STEP 2 · REMOVE THE DRIFT", b="Centred sums, compensated squares and forecasts are <b>martingales</b>.", f=[["32601", "definition"], ["30503", "variance of a sum"]], n=[["32603", "stopping"]]),
32603: dict(s="STORY 26 · STEP 3 · STOPPING", b="Stopping with <b>only the past</b> leaves a fair game fair at every fixed time.", f=[["32602", "families of martingales"]], n=[["32604", "stopping at a random time"]]),
32604: dict(s="STORY 26 · STEP 4 · WHEN YOU MAY STOP", b="<b>Optional stopping</b>: 𝔼[M_τ] = 𝔼[M₀] under boundedness conditions.", f=[["32603", "stopped martingale"]], n=[["32605", "applications"]]),
32605: dict(s="STORY 26 · STEP 5 · THE CORRIDOR", b="<b>Wald/OST</b> gives a/(a + b) and ab for the fair walk.", f=[["32604", "OST"], ["32105", "gambler's ruin by equations"]], n=[["32606", "tail bounds"]]),
32606: dict(s="STORY 26 · STEP 6 · STAYING CLOSE", b="<b>Doob</b> and <b>Azuma–Hoeffding</b> bound how far a martingale strays.", f=[["30601", "Markov's inequality"], ["32602", "capped moves"]], n=[["32701", "continuous time"]]),
}

FIX = build(CARDS)
