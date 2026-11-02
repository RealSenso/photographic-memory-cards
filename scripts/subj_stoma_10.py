"""StoMA topic 10 (exchangeable random variables). Commute picture: the commute times of days 1..n; no day is special."""
from commute_lib import *

SUBJECT = "StoMA"

def days(y, labs, x0=40, dx=44, fill="#f1f5f9"):
    out = ""
    for i, s in enumerate(labs):
        out += R(x0 + i * dx, y, 36, 18, fill, 1, 3) + N(x0 + i * dx + 18, y + 12, s, 7.5)
    return out

def d1(c):
    return svg(c, N(120, 14, "days of one commute record, in any order", 7),
        days(24, ["day 1", "day 2", "day 3"]), days(100, ["day 3", "day 1", "day 2"]),
        arrow(58, 46, 58, 98, 1), arrow(102, 46, 146, 98, 1, "3 2"), arrow(146, 46, 102, 98, 1, "3 2") if False else "",
        N(190, 38, "(X₁, X₂, X₃)", 7.5, "start"), N(190, 54, "has the same law as", 7, "start"), N(190, 114, "(X₃, X₁, X₂)", 7.5, "start"),
        N(120, 140, "same joint law for every reshuffling π: i.i.d. ⊂ exchangeable", 7))

def d2(c):
    out = ""
    for i in range(4):
        for j in range(4):
            on = i == j
            out += R(60 + j * 28, 30 + i * 22, 28, 22, "#d9dee7" if on else "#ffffff", 1) + N(74 + j * 28, 44 + i * 22, "σ²" if on else "ρσ²", 7)
    return svg(c, out, N(172, 40, "every day has the", 7, "start") if False else "", N(30, 18, "day 1 … day 4", 7, "start"),
        N(176, 50, "same spread σ²", 7.5, "start"), N(176, 62, "and every pair of", 7.5, "start"), N(176, 74, "days the same", 7.5, "start"), N(176, 86, "correlation ρ", 7.5, "start"),
        N(120, 130, "Σ = σ² [ (1 − ρ) I + ρ 1 1ᵀ ]", 8))

def _bound(c, note1, note2, note3, limit):
    X = lambda n: 24 + (n - 2) * 13
    Y = lambda n: 40 + 70 / (n - 1)
    out = L(24, 40, 226, 40, 1, ar=True) + L(24, 12, 24, 120, 1) + N(226, 32, "n days", 7, "end") + N(30, 14, "ρ = 0", 7, "start")
    out += poly([(X(n / 4 + 2), Y(n / 4 + 2)) for n in range(0, 61)], 1.1)
    out += N(28, 42, "", 7) 
    out += C(X(2), Y(2), 2.2) + N(X(2) + 5, Y(2) - 2, "n = 2: −1", 7, "start")
    out += C(X(3), Y(3), 2.2) + N(X(3) + 5, Y(3) - 2, "n = 3: −½", 7, "start")
    out += N(150, 70, note1, 7.5, "start") + N(150, 82, note2, 7, "start")
    out += N(120, 134, note3, 7)
    return svg(c, out)

def d3(c):
    return _bound(c, "allowed: ρ above the curve", "ρ ≥ −1/(n − 1)", "0 ≤ Var(∑Xᵢ) = nσ² [1 + (n − 1)ρ] ⇒ 1 + (n − 1)ρ ≥ 0", None)

def d4(c):
    return _bound(c, "the bound holds for every n,", "and tends to 0: so ρ ≥ 0", "infinite record: no day can systematically offset the others", None)

def d5(c):
    return svg(c, C(120, 36, 4, "#ffffff", 1), N(120, 20, "Θ: this term's hidden on-time chance", 7.5),
        *[arrow(120, 41, x, 70, 1) for x in (60, 120, 180)],
        *[R(x - 18, 70, 36, 18, "#f1f5f9", 1, 3) + N(x, 82, s, 7.5) for x, s in ((60, "X₁"), (120, "X₂"), (180, "X₃"))],
        N(120, 106, "given Θ = θ: days are i.i.d. Bernoulli(θ)", 7.5), N(120, 120, "ℙ(X₁=x₁…Xₙ=xₙ) = ∫ θ^(∑xᵢ)(1−θ)^(n−∑xᵢ) dF(θ)", 7),
        N(120, 136, "Θ = long-run share of on-time days", 7))

def d6(c):
    out = circ(60, 56, 32, "#f8fafc", 1)
    for (x, y, f_) in [(46, 46, "#ffffff"), (62, 40, "#ffffff"), (70, 60, "#000000"), (50, 66, "#ffffff"), (64, 76, "#000000"), (74, 48, "#ffffff")]:
        out += C(x, y, 3.2, f_, 1)
    out += N(60, 100, "urn: routes A (white), B (black)", 7)
    return svg(c, out, arrow(100, 56, 140, 56, 1), N(120, 48, "draw one", 7), N(190, 40, "take route A:", 7.5), N(190, 52, "put it back plus", 7.5), N(190, 64, "c more of A", 7.5),
        N(190, 84, "habit grows", 7), N(190, 96, "ℙ(sequence) depends", 7), N(190, 108, "only on counts", 7),
        N(120, 122, "Θ ~ Beta(w/c, b/c) = long-run share of route A", 7), N(120, 134, "exchangeable but not independent", 7))

CARDS = {
31001: dict(d=d1, kind="DEFINITION",
  stmt=r"<b>Exchangeability.</b> Random variables $X_1,\ldots,X_n$ are exchangeable if $(X_1,\ldots,X_n)\overset d=(X_{\pi(1)},\ldots,X_{\pi(n)})$ for every permutation $\pi$ of $\{1,\ldots,n\}$. An infinite sequence is exchangeable if every finite subsequence is. Every i.i.d. sequence is exchangeable, but not conversely (Grimmett 7.2; Durrett 4.1).",
  hint="If the order of your commute days carries no information, what does that say about their joint law?",
  bd=[r"<strong>$(X_1,\ldots,X_n)$ = the commute times of days $1$ to $n$.</strong> One list, one joint law for the whole record.",
      r"<strong>$(X_{\pi(1)},\ldots,X_{\pi(n)})$ = the same days reshuffled.</strong> Relabel the days by any permutation $\pi$, for instance by swapping Tuesday and Friday.",
      r"<strong>$\overset d=$ = nothing changes in law.</strong> No day is special: the joint chances are the same for every reshuffling. Independent identical days satisfy it, but dependent days can too."],
  conn=r"<strong>Days with no calendar.</strong> If you hid the dates, you could not tell which day was which, and every ordering of the same record would look equally plausible. The days can still be linked, for example through the same bus company.",
  cap="The commute record (X₁, X₂, X₃) and the same record in another order (X₃, X₁, X₂). Exchangeable days have the same joint law under every reshuffling."),
31002: dict(d=d2, kind="THEOREM",
  stmt=r"<b>Equal moments.</b> If $X_1,\ldots,X_n$ are exchangeable with finite second moments, then they have a common mean $\mu$ and variance $\sigma^2$, and a common covariance $\operatorname{Cov}(X_i,X_j)=\rho\sigma^2$ for all $i\ne j$. The covariance matrix is $\Sigma=\sigma^2\bigl[(1-\rho)I+\rho\mathbf 1\mathbf 1^\top\bigr]$ (Grimmett 7.2; Ross 7.4).",
  hint="If days can be reshuffled freely, what must the covariance between any two days look like?",
  bd=[r"<strong>$\operatorname{Var}(X_i)=\sigma^2$ = every day has the same spread.</strong> Reshuffling can swap any day with any other, so their marginal laws agree.",
      r"<strong>$\operatorname{Cov}(X_i,X_j)=\rho\sigma^2$ = every pair has the same link.</strong> Any pair of days can be swapped for any other pair, so one number $\rho$ describes all pairs.",
      r"<strong>$(1-\rho)I+\rho\mathbf 1\mathbf 1^\top$ = diagonal plus a constant.</strong> The matrix has $\sigma^2$ on the diagonal and $\rho\sigma^2$ everywhere else."],
  conn=r"<strong>One shared bus company effect.</strong> Every day has the same spread, and any two days are linked by the same amount, because swapping which days you compare changes nothing. A constant off-diagonal is the signature.",
  cap="The covariance matrix of the commute record on four days. The diagonal is the common variance σ², every off-diagonal entry is ρσ², giving Σ = σ²[(1−ρ)I + ρ𝟏𝟏ᵀ]."),
31003: dict(d=d3, kind="THEOREM",
  stmt=r"<b>Correlation bound for finite exchangeable sequences.</b> If $X_1,\ldots,X_n$ are exchangeable with common variance $\sigma^2>0$ and pairwise correlation $\rho$, then $\rho\ge-\dfrac1{n-1}$. Proof: $0\le\operatorname{Var}\bigl(\sum_iX_i\bigr)=n\sigma^2+n(n-1)\rho\sigma^2=n\sigma^2\bigl[1+(n-1)\rho\bigr]$ (Grimmett 7.2).",
  hint="How negatively can n exchangeable days be linked, if their total must have a non-negative variance?",
  bd=[r"<strong>$\operatorname{Var}(\sum X_i)\ge0$ = a variance is never negative.</strong> The total over all days can vary, or not at all, but not less than that.",
      r"<strong>$n\sigma^2[1+(n-1)\rho]$ = the variance of the total.</strong> There are $n$ variances $\sigma^2$ and $n(n-1)$ ordered pairs, each adding $\rho\sigma^2$.",
      r"<strong>$\rho\ge-1/(n-1)$ = days cannot be too negatively linked.</strong> With 2 days they may be perfectly opposed; with more days, less so: they cannot all be below average at the same time."],
  conn=r"<strong>Not everyone can make up for everyone else.</strong> A late Monday can be balanced by an early Tuesday. But with five equal days, each day cannot offset all four others strongly: the average negative link is at best −¼.",
  cap="The smallest allowed correlation −1/(n−1) as the number of days n grows. For n = 2 it is −1, for n = 3 it is −½, and it climbs towards 0 as days are added."),
31004: dict(d=d4, kind="COROLLARY",
  stmt=r"<b>Infinite exchangeability forces non-negative correlation.</b> If $X_1,X_2,\ldots$ is an infinite exchangeable sequence with finite variance, then every pair has $\rho\ge0$. Proof: each finite segment $X_1,\ldots,X_n$ is exchangeable, so $\rho\ge-\frac1{n-1}$ for all $n\ge2$, and letting $n\to\infty$ gives $\rho\ge0$ (Grimmett 7.2).",
  hint="If the record could go on forever, what is the most negative the link between two days can be?",
  bd=[r"<strong>$\rho\ge-\tfrac1{n-1}\ \forall n$ = the bound holds for every length.</strong> Any $n$ days of an infinite exchangeable record are themselves exchangeable.",
      r"<strong>$\lim_{n\to\infty}\bigl(-\tfrac1{n-1}\bigr)=0$ = the bound tends to 0.</strong> A fixed $\rho$ must be at least as large as every term of a sequence whose limit is 0.",
      r"<strong>$\rho\ge0$ = no negative links.</strong> Days in an infinite exchangeable record are never negatively correlated; mixing a hidden common factor creates only positive links."],
  conn=r"<strong>A never-ending record of days.</strong> If the record never ends, you can always ask about more and more days at once, and then no day can systematically make up for the others. The link between days is at least zero.",
  cap="The bound −1/(n−1) must hold for every n. As n grows it approaches 0, so a common correlation ρ of an infinite exchangeable sequence satisfies ρ ≥ 0."),
31005: dict(d=d5, kind="THEOREM",
  stmt=r"<b>de Finetti's theorem.</b> Let $X_1,X_2,\ldots\in\{0,1\}$ be an infinite exchangeable sequence. Then there is a random variable $\Theta\in[0,1]$, $\Theta=\lim_n\frac1n\sum_{i\le n}X_i$ a.s., with law $F_\Theta$, such that $\mathbb P(X_1=x_1,\ldots,X_n=x_n)=\int_0^1\theta^{\sum x_i}(1-\theta)^{n-\sum x_i}\,dF_\Theta(\theta)$: conditionally on $\Theta$, the $X_i$ are i.i.d. Bernoulli($\Theta$) (Grimmett 7.2; Durrett 4.1).",
  hint="Is an exchangeable record of on-time days secretly independent days with a hidden on-time chance?",
  bd=[r"<strong>$\Theta$ = a hidden on-time chance.</strong> Say this term's bus reliability: it is fixed once and for all but unknown to you, and it equals the long-run share of on-time days.",
      r"<strong>$\theta^{\sum x_i}(1-\theta)^{n-\sum x_i}$ = i.i.d. days given $\Theta=\theta$.</strong> Given the hidden chance, each day is an independent on-time/late coin flip.",
      r"<strong>$\int\ldots dF_\Theta(\theta)$ = average over the unknown chance.</strong> Mixing over what $\Theta$ might be gives the exchangeable record: dependent days are independent days with a common hidden cause."],
  conn=r"<strong>The unknown reliability of this bus line.</strong> Before you know how reliable the line is, one day's lateness tells you about the next. If you knew its reliability, days would be independent coin flips. Not knowing it makes the days exchangeable but linked.",
  cap="A hidden on-time chance Θ points at the days X₁, X₂, X₃. Given Θ = θ they are independent Bernoulli(θ) flips, and the joint law averages that product over the law of Θ."),
31006: dict(d=d6, kind="WORKED EXAMPLE",
  stmt=r"<b>Pólya's urn.</b> An urn has $w$ white and $b$ black balls; a ball is drawn and returned with $c$ more of its colour. With $k=\sum x_i$ white draws, $\mathbb P(X_1=x_1,\ldots,X_n=x_n)=\frac{\prod_{j<k}(w+jc)\prod_{j<n-k}(b+jc)}{\prod_{j<n}(w+b+jc)}$, which depends only on $k$: the draws are exchangeable, and $\Theta\sim\mathrm{Beta}(\frac wc,\frac bc)$ (Ross 3.6; Grimmett 7.2).",
  hint="If every time you use a route you make it more likely next time, are the days independent? Exchangeable?",
  bd=[r"<strong>$\prod_{j<k}(w+jc)$ = the white draws.</strong> The $j$-th white draw sees white grown by $jc$, in whatever positions they fall.",
      r"<strong>$\prod_{j<n}(w+b+jc)$ = the growing urn.</strong> Each draw adds $c$ balls, the same for every sequence.",
      r"<strong>$\Theta\sim\mathrm{Beta}(w/c,b/c)$ = the long-run share.</strong> The chance depends on the count $k$, not the order: exchangeable, not independent."],
  conn=r"<strong>Habit builds on itself.</strong> Each time a route works you favour it a bit more; the order of days does not matter, only how often each route was used.",
  cap="An urn of route A (white) and route B (black). After each draw the drawn route is put back with c more of its kind, so the chance of a sequence depends only on counts, and Θ ~ Beta(w/c, b/c) is the long-run share."),
}

STORY = {
31001: dict(s="STORY 10 · STEP 1 · NO CALENDAR", b="<b>Exchangeable</b> days have a joint law that ignores their order: weaker than independence, but still a symmetry.", f=[["30206", "independence is not the only structure"], ["30705", "i.i.d. as the special case"]], n=[["31002", "what the symmetry forces on moments"]]),
31002: dict(s="STORY 10 · STEP 2 · EQUAL MOMENTS", b="Reshuffling forces <b>one variance and one correlation</b> for all pairs.", f=[["31001", "exchangeability"], ["30503", "covariance"]], n=[["31003", "a limit on negative links"]]),
31003: dict(s="STORY 10 · STEP 3 · A LIMIT ON NEGATIVE LINKS", b="A non-negative variance of the total gives <b>ρ ≥ −1/(n−1)</b>.", f=[["31002", "equal correlation"], ["30503", "variance of a sum"]], n=[["31004", "taking n to infinity"]]),
31004: dict(s="STORY 10 · STEP 4 · FOREVER", b="Letting n grow forces <b>ρ ≥ 0</b>: an infinite exchangeable record has no negative links.", f=[["31003", "the finite bound"]], n=[["31005", "the hidden common cause"]]),
31005: dict(s="STORY 10 · STEP 5 · THE HIDDEN CAUSE", b="<b>de Finetti</b>: an infinite exchangeable record is i.i.d. given a hidden random parameter.", f=[["31004", "non-negative links"], ["30203", "mixing over cases"]], n=[["31006", "a concrete example"], ["31701", "laws of large numbers"]]),
31006: dict(s="STORY 10 · STEP 6 · HABIT", b="<b>Pólya's urn</b>: reinforcement makes the draws exchangeable but dependent, with a Beta-distributed hidden share.", f=[["31005", "de Finetti"]], n=[["31901", "chains with memory"]]),
}

FIX = build(CARDS)
