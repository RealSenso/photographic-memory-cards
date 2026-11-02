"""StoMA topic 16 (Borel-Cantelli, limsup/liminf). Commute picture: being late on day n, infinitely often or only finitely often."""
from commute_lib import *

SUBJECT = "StoMA"

def days_row(y, flags, x0=28, dx=14, lab=None):
    out = L(x0 - 4, y + 6, x0 + dx * len(flags), y + 6, 1, ar=True)
    for i, f_ in enumerate(flags):
        out += C(x0 + i * dx, y, 2.8, "#000000" if f_ else "#ffffff", 1)
    return out

def d1(c):
    a = [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1]
    b = [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    return svg(c, N(24, 18, "Aₙ = late on day n", 7.5, "start"),
        days_row(40, a), N(24, 58, "keeps coming back: late i.o.  ∈ lim sup Aₙ", 7, "start"),
        days_row(84, b), N(24, 102, "from some day on always late: all but finitely often  ∈ lim inf Aₙ", 6.5, "start"),
        N(120, 122, "lim sup Aₙ = ⋂ₙ ⋃ₖ≥ₙ Aₖ", 8), N(120, 136, "(lim sup Aₙ)ᶜ = lim inf Aₙᶜ", 8))

def d2(c):
    out = ax(24, 100, 226, 20) + N(226, 112, "n", 7, "end") + N(28, 20, "ℙ(Aₙ)", 7, "start")
    for i in range(10):
        h = 60 / (i + 1) ** 2 * 1.2
        out += R(34 + i * 18, 100 - h, 12, h, "#f1f5f9", 1)
    return svg(c, out, N(120, 14, "∑ ℙ(Aₙ) < ∞ (here chances like 1/n²)", 7.5),
        N(120, 124, "the tail ∑ₖ≥ₙ ℙ(Aₖ) → 0, so ℙ(late i.o.) ≤ any tail = 0", 7), N(120, 138, "no independence needed", 7.5),
        N(130, 50, "after some day,", 7, "start"), N(130, 61, "no more lateness", 7, "start"))

def d3(c):
    out = ax(24, 100, 226, 20) + N(226, 112, "n", 7, "end") + N(28, 26, "ℙ(Aₙ)", 7, "start")
    for i in range(10):
        h = 60 / (i + 1)
        out += R(34 + i * 18, 100 - h, 12, h, "#f1f5f9", 1)
    out += fn(lambda x: 100 - 2.0 * (60 * math.log(1 + (x - 34) / 18) / 60) * 12 if False else 100 - 12 * math.log(1 + (x - 34) / 18) * 3, 34, 214, 40, 1.1, "4 3")
    return svg(c, out, N(120, 11, "independent days, ∑ ℙ(Aₙ) = ∞ (chances like 1/n)", 7.5),
        N(120, 124, "∑ diverges (dashed: running total keeps rising) ⇒ ℙ(late i.o.) = 1", 7), N(120, 138, "independence is essential here", 7.5))

def d4(c):
    out = ax(24, 100, 226, 20) + N(226, 112, "days", 7, "end")
    out += R(24, 40, 60, 60, "#d9dee7", 1) + N(54, 68, "first k days:", 7) + N(54, 78, "no effect", 7)
    out += R(84, 40, 140, 60, "#ffffff", 1) + N(154, 66, "tail event E:", 7.5) + N(154, 78, "depends only on the far future", 7)
    return svg(c, out, N(120, 20, "𝒯 = ⋂ₙ σ(Xₙ, Xₙ₊₁, …)", 8), N(120, 32, "E ∈ 𝒯: unchanged by altering any finite number of days", 6.5),
        N(120, 124, "independent days ⇒ ℙ(E) = 0 or 1, never in between", 7.5), N(120, 138, "e.g. “the long-run average exists”: all or nothing", 7))

def d5(c):
    out = ax(24, 100, 226, 20) + N(226, 112, "n", 7, "end") + N(28, 20, "|Xₙ − X|", 7, "start")
    out += fn(lambda x: 100 - 60 * math.exp(-(x - 24) / 50) - 4 * math.sin((x - 24) / 6) ** 2 * math.exp(-(x - 24) / 70), 24, 226, 80, 1.1)
    out += L(24, 80, 226, 80, 1, "4 3") + N(30, 76, "ε", 7.5, "start")
    return svg(c, out, N(150, 40, "only finitely many days", 7, "start"), N(150, 51, "above the ε band", 7, "start"),
        N(120, 124, "∑ ℙ(|Xₙ − X| ≥ ε) < ∞ for every ε ⇒ Xₙ → X a.s.", 7.5), N(120, 138, "first Borel–Cantelli turns summable chances into a.s. convergence", 6.5))

def d6(c):
    seq = "HTHHTHHHTHTTHHHHHTH"
    out = ""
    for i, ch in enumerate(seq):
        out += R(22 + i * 11, 30, 10, 12, "#d9dee7" if ch == "H" else "#ffffff", .8) + N(27 + i * 11, 39, ch, 6.5)
    out += L(22 + 12 * 11, 46, 22 + 17 * 11, 46, 1.2) + N(22 + 15 * 11, 56, "run of Lₖ = 5", 7)
    return svg(c, N(120, 18, "mornings on time (H) or late (T), in a row", 7), out,
        N(120, 82, "runs of length Lₖ: ℙ = 2^(−Lₖ)", 7.5), N(120, 100, "∑ 2^(−Lₖ) < ∞ ⇒ such runs happen finitely often", 7), N(120, 112, "∑ 2^(−Lₖ) = ∞ ⇒ they happen infinitely often (a.s.)", 7),
        N(120, 130, "if Lₖ = log₂ k, ∑ 1/k diverges; if Lₖ = 2 log₂ k, ∑ 1/k² converges", 6.5))

CARDS = {
31601: dict(d=d1, kind="DEFINITION",
  stmt=r"<b>Limsup and liminf of events.</b> For events $A_n$, $\limsup A_n=\bigcap_{n=1}^\infty\bigcup_{k=n}^\infty A_k=\{A_n\text{ infinitely often}\}$ and $\liminf A_n=\bigcup_{n=1}^\infty\bigcap_{k=n}^\infty A_k=\{A_n\text{ for all but finitely many }n\}$. Also $(\limsup A_n)^c=\liminf A_n^c$ (Grimmett 7.3; Durrett 2.3).",
  hint="How do you say 'late on infinitely many days' versus 'late on all but finitely many days' with unions and intersections?",
  bd=[r"<strong>$\bigcup_{k\ge n}A_k$ = late on some day from $n$ on.</strong> Whatever day $n$ you start from, there is still a late day ahead.",
      r"<strong>$\bigcap_n\bigcup_{k\ge n}A_k$ = this holds for every $n$.</strong> There is always a later late day: lateness never stops, that is, infinitely often.",
      r"<strong>$\bigcup_n\bigcap_{k\ge n}A_k$ = always late from some day on.</strong> Past some $n$, every day is late: all but finitely often. Complements swap the two."],
  conn=r"<strong>Does the bad luck ever stop?</strong> “Late infinitely often” means however far into the future you look, another late day awaits. “Late from some day on” means a permanent breakdown starts at some point and never ends.",
  cap="Two records of days (black = late). The top one keeps returning: lim sup, late infinitely often. The bottom is late every day from some point on: lim inf. Complements swap them."),
31602: dict(d=d2, kind="THEOREM",
  stmt=r"<b>First Borel–Cantelli lemma.</b> If $\sum_{n=1}^\infty\mathbb P(A_n)<\infty$, then $\mathbb P(A_n\text{ i.o.})=\mathbb P(\limsup A_n)=0$. No independence is needed. Proof: $\mathbb P(\limsup A_n)\le\mathbb P(\bigcup_{k\ge n}A_k)\le\sum_{k\ge n}\mathbb P(A_k)\to0$ (Grimmett 7.3; Ross 8.2).",
  hint="If the chances of being late on day n add up to a finite number, how often can you be late?",
  bd=[r"<strong>$\sum\mathbb P(A_n)<\infty$ = the chances are summable.</strong> Chances like $1/n^2$ add up to a finite number; the late-day chances die away fast enough.",
      r"<strong>$\sum_{k\ge n}\mathbb P(A_k)\to0$ = the tail of the sum vanishes.</strong> Being late on some day from $n$ on has chance at most this tail, by Boole's inequality.",
      r"<strong>$\mathbb P(\limsup A_n)=0$ = finitely many late days.</strong> This holds for any dependence between days; only the size of the chances matters."],
  conn=r"<strong>Bad luck that fades.</strong> If the chance of lateness on day $n$ shrinks quickly, say like $1/n^2$, then with probability 1 there will be only finitely many late days, however the days are linked.",
  cap="Bars of ℙ(Aₙ) shrinking like 1/n². The sum is finite, so the tail ∑ₖ≥ₙ ℙ(Aₖ) → 0, and ℙ(Aₙ infinitely often) = 0."),
31603: dict(d=d3, kind="THEOREM",
  stmt=r"<b>Second Borel–Cantelli lemma.</b> If $A_1,A_2,\ldots$ are independent and $\sum_{n=1}^\infty\mathbb P(A_n)=\infty$, then $\mathbb P(A_n\text{ i.o.})=1$. Proof: $\mathbb P(\bigcap_{k\ge n}A_k^c)=\prod_{k\ge n}(1-\mathbb P(A_k))\le\exp(-\sum_{k\ge n}\mathbb P(A_k))=0$ (Grimmett 7.3; Ross 8.2).",
  hint="If days are independent and the chances of being late never add up to a finite number, how often are you late?",
  bd=[r"<strong>$\{A_n\}$ independent = days are unrelated.</strong> This is essential: without it, correlated days can make the conclusion fail.",
      r"<strong>$\sum\mathbb P(A_n)=\infty$ = the chances add up to infinity.</strong> Chances like $1/n$ shrink, but not fast enough: the running total keeps rising.",
      r"<strong>$\mathbb P(\limsup A_n)=1$ = late infinitely often, for sure.</strong> The chance of never being late again from day $n$ on is $\prod(1-p_k)\le e^{-\sum p_k}=0$."],
  conn=r"<strong>Bad luck that never quite fades.</strong> If the chance of an incident on day $n$ is $1/n$ and days are independent, you can be certain that incidents never stop, though they become rarer.",
  cap="Bars of ℙ(Aₙ) = 1/n and, dashed, the running total ∑ℙ(Aₖ), which keeps rising without bound. With independence this forces ℙ(Aₙ i.o.) = 1."),
31604: dict(d=d4, kind="THEOREM",
  stmt=r"<b>Kolmogorov's zero–one law.</b> Let $X_1,X_2,\ldots$ be independent and $\mathcal T=\bigcap_{n=1}^\infty\sigma(X_n,X_{n+1},\ldots)$ the tail $\sigma$-algebra. Then $\mathbb P(E)\in\{0,1\}$ for every $E\in\mathcal T$ (Grimmett 7.3; Durrett 2.5).",
  hint="For independent days, which events are decided only by the far future, and what are their possible chances?",
  bd=[r"<strong>$\sigma(X_n,X_{n+1},\ldots)$ = what the days from $n$ on can tell you.</strong> Questions about the record from day $n$ forward.",
      r"<strong>$\bigcap_n$ = questions that survive dropping any finite number of days.</strong> A tail event does not change if you alter the first $k$ days, for any $k$.",
      r"<strong>$\mathbb P(E)\in\{0,1\}$ = all or nothing.</strong> For independent days, a question about the far future is either certain or impossible; for example “the long-run average exists”."],
  conn=r"<strong>The far future is all or nothing.</strong> Whether your long-run average commute settles down cannot depend on any finite number of days, so for independent days it either happens for sure or never happens.",
  cap="The first k days (shaded) cannot affect a tail event E, which depends only on the far future. For independent days, every such event has chance 0 or 1."),
31605: dict(d=d5, kind="THEOREM",
  stmt=r"<b>Almost sure convergence via Borel–Cantelli.</b> If $\sum_{n=1}^\infty\mathbb P(|X_n-X|\ge\varepsilon)<\infty$ for every $\varepsilon>0$, then $X_n\to X$ almost surely. Proof: by the first Borel–Cantelli lemma, $|X_n-X|\ge\varepsilon$ happens only finitely often a.s.; take $\varepsilon=1/m$ and a countable intersection (Grimmett 7.3; Durrett 2.3).",
  hint="How do you turn a summable bound on the chance of a big miss into a.s. convergence?",
  bd=[r"<strong>$\mathbb P(|X_n-X|\ge\varepsilon)$ = the chance of a miss bigger than $\varepsilon$ on day $n$.</strong> Typically bounded by Chebyshev or Markov.",
      r"<strong>$\sum<\infty$ for every $\varepsilon$ = the misses are summable.</strong> Then by Borel–Cantelli I only finitely many days have a miss above $\varepsilon$.",
      r"<strong>$\varepsilon=1/m$ over all $m$ = a countable intersection.</strong> Eventually every day is within $1/m$, for every $m$: $X_n\to X$ almost surely."],
  conn=r"<strong>From rare slips to certainty.</strong> If the chance of straying more than a minute from the long-run value on day $n$ shrinks quickly enough to add up, then each run of mornings eventually stays inside the band for good.",
  cap="The record |Xₙ − X| against the band ε. If ∑ℙ(|Xₙ − X| ≥ ε) < ∞ then only finitely many days leave the band, so Xₙ → X a.s."),
31606: dict(d=d6, kind="WORKED EXAMPLE",
  stmt=r"<b>Head runs.</b> In an infinite sequence of fair coin tosses, let $A_k$ be the event that tosses $k,\ldots,k+L_k-1$ are all heads, so $\mathbb P(A_k)=2^{-L_k}$. If $\sum_k2^{-L_k}<\infty$, the run lengths $L_k$ occur only finitely often (first Borel–Cantelli); if $\sum_k2^{-L_k}=\infty$ and the events are independent (disjoint blocks), they occur infinitely often a.s. (second) (Grimmett 7.3; Durrett 2.3).",
  hint="How long a streak of on-time days can you expect to see somewhere in an infinite record?",
  bd=[r"<strong>$A_k$ = a run of $L_k$ on-time days starting at day $k$.</strong> Each such run has chance $2^{-L_k}$ for a fair coin.",
      r"<strong>$\sum2^{-L_k}<\infty\Rightarrow$ finitely often.</strong> If the required run lengths grow quickly, say $L_k=2\log_2k$, the chances $1/k^2$ are summable.",
      r"<strong>$\sum2^{-L_k}=\infty\Rightarrow$ infinitely often.</strong> If they grow slowly, say $L_k=\log_2k$, the chances $1/k$ diverge: such runs recur for ever (for independent blocks)."],
  conn=r"<strong>The longest winning streak.</strong> In an endless record of days, a streak of about $\log_2k$ on-time days keeps appearing around day $k$, but streaks much longer than $2\log_2k$ stop appearing.",
  cap="A record of on-time days (H) and late days (T) with a run of length Lₖ = 5 marked. A run of length Lₖ has chance 2^(−Lₖ), and its sum decides finitely or infinitely often."),
}

STORY = {
31601: dict(s="STORY 16 · STEP 1 · FOREVER OR ONLY FINITELY OFTEN", b="<b>limsup</b> is “infinitely often” and <b>liminf</b> is “all but finitely often”, built from unions and intersections of events.", f=[["30103", "limits of events"]], n=[["31602", "when infinitely often has chance 0"], ["31603", "when it has chance 1"]]),
31602: dict(s="STORY 16 · STEP 2 · FADING BAD LUCK", b="<b>BC1</b>: summable chances mean only <b>finitely many</b> events happen, with no independence.", f=[["31601", "limsup"], ["30104", "Boole's inequality"]], n=[["31605", "proving a.s. convergence"]]),
31603: dict(s="STORY 16 · STEP 3 · BAD LUCK THAT PERSISTS", b="<b>BC2</b>: independent events with divergent chances happen <b>infinitely often</b>.", f=[["31602", "BC1"], ["30205", "independence"]], n=[["31604", "zero-one behaviour"], ["31606", "a worked example"]]),
31604: dict(s="STORY 16 · STEP 4 · ALL OR NOTHING", b="<b>Kolmogorov's zero–one law</b>: tail events of independent days have chance 0 or 1.", f=[["31603", "BC2"]], n=[["31702", "strong law is a tail event"]]),
31605: dict(s="STORY 16 · STEP 5 · A TOOL", b="Summable miss chances give <b>almost sure convergence</b> through BC1.", f=[["31602", "BC1"], ["31503", "why a.s. needs more"]], n=[["31703", "the fourth-moment strong law"]]),
31606: dict(s="STORY 16 · STEP 6 · STREAKS", b="Both lemmas decide how long a <b>streak</b> can keep recurring in an endless record.", f=[["31602", "BC1"], ["31603", "BC2"]], n=[["31701", "laws of large numbers"]]),
}

FIX = build(CARDS)
