"""StoMA topic 26 (martingales). F1 picture: Max's live win probability, updated lap by lap, is a fair game; stopping times like the lap he first takes the lead."""
from f1_lib import *
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
    return svg(c, ax(24, 64, 226, 14), N(226, 76, "lap n", 7, "end"), N(28, 14, "Mₙ", 7.5, "start"), poly(pts, 1), L(150, 20, 150, 108, .8, "3 2"),
        N(150, 16, "now: lap n", 7), N(158, 92, "next lap: average", 7, "start"), N(158, 102, "of futures = Mₙ", 7, "start"),
        N(120, 12, "ℱₙ = everything known up to lap n", 7.5) if False else N(90, 12, "ℱₙ = all you know by lap n", 7),
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
    return svg(c, out, N(120, 11, "stop the first lap a rule is met (e.g. Max leads)", 7), N(120, 130, "{τ ≤ n} ∈ ℱₙ: the decision uses only what is known by lap n", 7),
        N(120, 142, "Mₙ∧τ is a martingale and 𝔼[Mₙ∧τ] = 𝔼[M₀]", 8))

def d4(c):
    return svg(c, box(12, 28, 100, 40, "𝔼[M_τ] = 𝔼[M₀]", "#f1f5f9", 8.5, False), box(124, 28, 102, 40, "if  τ ≤ C", "#f1f5f9", 8.5, False),
        box(124, 76, 102, 24, "or |Mₙ∧τ| ≤ K", "#f1f5f9", 7.5, False) if False else "", N(175, 90, "or  |Mₙ∧τ| ≤ K", 8), N(175, 104, "or 𝔼τ < ∞ and |ΔM| ≤ c", 7.5),
        arrow(112, 48, 124, 48, 1), N(120, 14, "when may you stop a fair game?", 7.5),
        N(120, 124, "each condition rules out endless races or unbounded losses", 7), N(120, 136, "(doubling forever breaks it)", 7))

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
        N(120, 122, "Azuma: ℙ(|Mₙ − M₀| ≥ t) ≤ 2 exp(−t² / 2∑cₖ²)", 7.5), N(120, 134, "bounded moves per lap ⇒ it rarely strays far", 7), N(120, 144, "(cₖ = the cap on lap k's move)", 6.5))

CARDS = {
32601: dict(d=d1, kind="DEFINITION",
  stmt=r"<b>Filtration and martingale.</b> A filtration $(\mathcal F_n)$ is an increasing sequence of σ-fields. $(M_n)$ is a martingale if $M_n$ is $\mathcal F_n$-measurable, $\mathbb E|M_n|<\infty$ and $\mathbb E[M_{n+1}\mid\mathcal F_n]=M_n$. Then $\mathbb E[M_n]=\mathbb E[M_0]$ for all $n\ge0$; with $\ge$ or $\le$ it is a sub- or supermartingale (Williams 10; Grimmett 12.1).",
  hint="What does it mean for Max's live win probability to be a fair game, given everything seen so far?",
  bd=[r"<strong>$\mathcal F_n$ = what you know by lap $n$.</strong> The information grows lap by lap; $M_n$ can be read off from it.",
      r"<strong>$\mathbb E[M_{n+1}\mid\mathcal F_n]=M_n$ = a fair game.</strong> Given the whole race so far, the expected value after the next lap is the value now: no drift up or down.",
      r"<strong>$\mathbb E[M_n]=\mathbb E[M_0]$ = constant mean.</strong> Taking expectations of the martingale property gives the same expected value on every lap."],
  conn="<strong>A fair win probability.</strong> Let $M_n$ be Max's chance of winning as the TV graphic shows it after lap $n$. If it is honest, its average next lap, given everything so far, is what it says now. So it is a martingale, and on average it ends where it started.",
  cap="Max's live win probability Mₙ and the information up to lap n. A martingale is a fair game: the average of next lap's value given the race so far is the value now, Mₙ."),
32602: dict(d=d2, kind="THEOREM",
  stmt=r"<b>Canonical martingales.</b> For i.i.d. $X_i$ with mean $\mu$, variance $\sigma^2$ and MGF $M_X(\theta)<\infty$, and $S_n=\sum_{i\le n}X_i$: $S_n-n\mu$, $(S_n-n\mu)^2-n\sigma^2$ and $\dfrac{e^{\theta S_n}}{M_X(\theta)^n}$ are martingales. For any integrable $Y$, $M_n=\mathbb E[Y\mid\mathcal F_n]$ is a martingale (Doob) (Williams 10; Grimmett 12.1).",
  hint='Which natural quantities built from lap times are fair games?',
  bd=[r"<strong>$S_n-n\mu$ = the centred total.</strong> Subtract the expected drift $n\mu$; the rest has zero mean increments.",
      r"<strong>$(S_n-n\mu)^2-n\sigma^2$ and $e^{\theta S_n}/M_X(\theta)^n$ = compensated square and exponential.</strong> Subtract the compensator $n\sigma^2$, or divide by the MGF to the $n$.",
      r"<strong>$M_n=\mathbb E[Y\mid\mathcal F_n]$ = Doob martingale.</strong> Your best forecast of the final result, updated as each lap comes in, is a fair game."],
  conn="<strong>Remove the drift.</strong> Max's total race time after $n$ laps grows by about one average lap time per lap; subtract that drift and what is left is a fair game. His live win probability, a forecast of the final result, is also a fair game.",
  cap='Four martingale families: the centred total Sₙ − nμ, the compensated square Sₙ² − nσ², the exponential martingale, and the forecast Mₙ = 𝔼[Y | ℱₙ].'),
32603: dict(d=d3, kind="THEOREM",
  stmt=r"<b>Stopping times and the stopped martingale.</b> A random time $\tau$ is a stopping time if $\{\tau\le n\}\in\mathcal F_n$ for all $n\ge0$. If $(M_n)$ is a martingale then the stopped process $M_{n\wedge\tau}$ is a martingale, so $\mathbb E[M_{n\wedge\tau}]=\mathbb E[M_0]$ for each $n$ (Williams 10; Grimmett 12.4).",
  hint='If you decide when to stop betting using only the laps seen so far, does the bet stay fair?',
  bd=[r"<strong>$\{\tau\le n\}\in\mathcal F_n$ = a decision from the past.</strong> Whether you have stopped by lap $n$ is decided by what you have seen up to lap $n$; no peeking ahead.",
      r"<strong>$M_{n\wedge\tau}$ = the value frozen at $\tau$.</strong> It follows $M$ until the stopping lap and then stays put.",
      r"<strong>$\mathbb E[M_{n\wedge\tau}]=\mathbb E[M_0]$ = still fair.</strong> No rule that uses only the past can turn a fair game into a favourable one, at any fixed lap $n$."],
  conn='<strong>No system beats a fair bet.</strong> “Cash out the first lap Max takes the lead” is a stopping time: you know it when it happens. That rule, or any other based on the race so far, never changes your expected payout at a fixed lap.',
  cap='A fair bet, stopped at the first lap τ a rule is met (say, Max takes the lead). The stopped value Mₙ∧τ follows the path until τ and then stays put; it is still a martingale.'),
32604: dict(d=d4, kind="THEOREM",
  stmt=r"<b>Optional stopping theorem.</b> If $(M_n)$ is a martingale and $\tau$ a stopping time, then $\mathbb E[M_\tau]=\mathbb E[M_0]$ provided one of: (a) $\tau\le C$ a.s.; (b) $\tau<\infty$ a.s. and $|M_{n\wedge\tau}|\le K$; (c) $\mathbb E[\tau]<\infty$ and $|M_{n+1}-M_n|\le c$ (Williams 10.10; Grimmett 12.5).",
  hint='When can you stop a fair bet at a random lap and still expect to leave with what you came with?',
  bd=[r"<strong>$\tau\le C$ = bounded time.</strong> You stop by a fixed lap, say the last lap, so the stopped-martingale theorem applies at $n=C$.",
      r"<strong>$|M_{n\wedge\tau}|\le K$ = bounded value.</strong> The bet's value never exceeds $K$, so passing to the limit $n\to\infty$ is safe (dominated convergence).",
      r"<strong>$\mathbb E[\tau]<\infty$ and $|\Delta M|\le c$ = finite mean stopping time, bounded steps.</strong> Then $|M_{n\wedge\tau}|\le|M_0|+c\tau$, which is integrable."],
  conn='<strong>A doubling system fails.</strong> Betting on Max and doubling the stake after each race he loses, until he wins, seems to guarantee a profit. But it needs unbounded losses on the way, so none of the conditions hold and the expectation is not preserved.',
  cap='The conclusion 𝔼[M_τ] = 𝔼[M₀] holds under any one of the three conditions: bounded stopping time, bounded stopped value, or finite mean stopping time with bounded steps.'),
32605: dict(d=d5, kind="WORKED EXAMPLE",
  stmt=r"<b>Gambler's ruin by OST.</b> For a fair simple random walk $S_n$ started at $0$ and $\tau$ the first exit time from $(-a,b)$: $\mathbb E[S_\tau]=0$ gives $\mathbb P(\text{hit }b\text{ first})=\frac a{a+b}$, and $\mathbb E[S_\tau^2-\tau]=0$ gives $\mathbb E[\tau]=ab$ (Wald's identities) (Ross 6.3; Williams 10.12).",
  hint='In a fair chase, how do two fair games give both the chance that Max breaks clear and how many laps the fight lasts?',
  bd=[r"<strong>$\mathbb E[S_\tau]=0$ = the walk is a martingale.</strong> The stopped value is $b$ with chance $p$ and $-a$ with chance $1-p$, so $pb-(1-p)a=0$.",
      r"<strong>$p=\frac a{a+b}$ = the chance of reaching $+b$ first.</strong> Solving $pb=(1-p)a$ gives the fractional position of the start between the two ends.",
      r"<strong>$\mathbb E[S_\tau^2-\tau]=0\Rightarrow\mathbb E[\tau]=ab$ = expected duration.</strong> $\mathbb E[S_\tau^2]=pb^2+(1-p)a^2=ab$."],
  conn='<strong>The chase.</strong> The gap between Max and a rival moves a fair step each lap. The fight ends when Max is $b$ steps clear or $a$ steps behind. He breaks clear first with chance $a/(a+b)$, and the fight lasts $ab$ laps on average. Two fair games answer both questions.',
  cap='A fair gap walk leaves the band (−a, b) at lap τ. The martingale Sₙ gives ℙ(Max clear by b first) = a/(a+b); the martingale Sₙ² − n gives 𝔼[τ] = ab.'),
32606: dict(d=d6, kind="THEOREM",
  stmt=r"<b>Doob's inequality and Azuma–Hoeffding.</b> For a non-negative submartingale $(X_k)$, $\mathbb P\bigl(\max_{0\le k\le n}X_k\ge\lambda\bigr)\le\frac{\mathbb E[X_n]}\lambda$. For a martingale with $|M_k-M_{k-1}|\le c_k$, $\mathbb P(|M_n-M_0|\ge t)\le2\exp\Bigl(-\frac{t^2}{2\sum_{k=1}^nc_k^2}\Bigr)$ (Williams 14; Grimmett 12.6).",
  hint="How likely is a fair game, like Max's win probability, ever to swing far from where it started?",
  bd=[r"<strong>$\mathbb P(\max_kX_k\ge\lambda)\le\mathbb E[X_n]/\lambda$ = Doob.</strong> Markov's inequality for the whole running maximum, not just the last value.",
      r"<strong>$|M_k-M_{k-1}|\le c_k$ = capped moves per lap.</strong> No single lap can move the value by more than $c_k$.",
      r"<strong>$2\exp(-t^2/2\sum c_k^2)$ = Azuma–Hoeffding.</strong> The value strays by $t$ with chance that falls off as a Gaussian tail in $t/\sqrt{\sum c_k^2}$."],
  conn="<strong>Caps on each lap.</strong> If no single lap can move Max's win probability by more than a little, then the chance that it ends up far from where it started after many laps is very small, like a bell's tail.",
  cap='A non-negative fair game and the level λ: Doob bounds the chance that its running maximum reaches λ. With capped moves per lap, Azuma bounds the chance it strays far.'),
}

STORY = {
32601: dict(s='STORY 26 · STEP 1 · A FAIR GAME', b='A <b>martingale</b> is a fair game: the expected value after the next lap, given the race so far, is the value now.', f=[["31201", "conditional expectation"], ["32501", "walks"]], n=[["32602", "examples"]]),
32602: dict(s="STORY 26 · STEP 2 · REMOVE THE DRIFT", b="Centred sums, compensated squares and forecasts are <b>martingales</b>.", f=[["32601", "definition"], ["30503", "variance of a sum"]], n=[["32603", "stopping"]]),
32603: dict(s="STORY 26 · STEP 3 · STOPPING", b="Stopping with <b>only the past</b> leaves a fair game fair at every fixed time.", f=[["32602", "families of martingales"]], n=[["32604", "stopping at a random time"]]),
32604: dict(s="STORY 26 · STEP 4 · WHEN YOU MAY STOP", b="<b>Optional stopping</b>: 𝔼[M_τ] = 𝔼[M₀] under boundedness conditions.", f=[["32603", "stopped martingale"]], n=[["32605", "applications"]]),
32605: dict(s='STORY 26 · STEP 5 · THE CHASE', b="<b>Wald/OST</b> gives a/(a + b) and ab for the fair walk.", f=[["32604", "OST"], ["32105", "gambler's ruin by equations"]], n=[["32606", "tail bounds"]]),
32606: dict(s="STORY 26 · STEP 6 · STAYING CLOSE", b="<b>Doob</b> and <b>Azuma–Hoeffding</b> bound how far a martingale strays.", f=[["30601", "Markov's inequality"], ["32602", "capped moves"]], n=[["32701", "continuous time"]]),
}

FIX = build(CARDS)
