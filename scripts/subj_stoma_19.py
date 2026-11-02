"""StoMA topic 19 (discrete-time Markov chains). Commute picture: each morning is on time (O), late (L) or cancelled (C); tomorrow depends on today."""
from commute_lib import *

SUBJECT = "StoMA"

def nd(x, y, lab, r=11):
    return circ(x, y, r, "#ffffff", 1) + N(x, y + 3, lab, 8)

def d1(c):
    return svg(c, nd(50, 50, "O"), nd(130, 50, "L"), nd(210, 50, "C") if False else nd(90, 108, "C"),
        arrow(62, 46, 118, 46, 1), arrow(118, 54, 62, 54, 1), arrow(56, 60, 82, 98, 1), arrow(124, 60, 98, 98, 1),
        N(90, 40, "P(O,L)", 6.5), N(90, 69, "P(L,O)", 6.5), N(36, 14, "tomorrow depends only on today", 7, "start"),
        N(170, 86, "row i of P:", 7.5, "start"), N(170, 97, "∑ⱼ Pᵢⱼ = 1", 8, "start"), N(170, 110, "(tomorrow is certain", 7, "start"), N(170, 120, "to be somewhere)", 7, "start"),
        N(120, 138, "ℙ(Xₙ₊₁ = j | Xₙ = i, …, X₀ = i₀) = Pᵢⱼ", 7.5))

def d2(c):
    return svg(c, nd(40, 60, "i"), nd(120, 36, "k"), nd(120, 90, "k′"), nd(200, 60, "j"),
        arrow(50, 56, 109, 40, 1), arrow(50, 64, 109, 86, 1), arrow(130, 39, 190, 56, 1), arrow(130, 87, 190, 64, 1),
        N(72, 36, "m steps", 7), N(172, 36, "n steps", 7), N(120, 18, "pass through some middle state k", 7),
        N(120, 118, "Pᵢⱼ⁽ᵐ⁺ⁿ⁾ = ∑ₖ Pᵢₖ⁽ᵐ⁾ Pₖⱼ⁽ⁿ⁾  ⇔  P⁽ᵐ⁺ⁿ⁾ = Pᵐ Pⁿ", 7.5), N(120, 132, "p⁽ⁿ⁾ = p⁽⁰⁾ Pⁿ: n-day distribution", 7.5))

def d3(c):
    return svg(c, nd(36, 40, "a"), nd(90, 40, "b"), nd(144, 40, "c"), nd(190, 40, "d", 9) if False else nd(36, 98, "d"), nd(144, 98, "e"),
        arrow(47, 40, 79, 40, 1), arrow(79, 44, 47, 44, 1), arrow(101, 40, 133, 40, 1), arrow(144, 52, 144, 86, 1), arrow(47, 98, 133, 98, 1) if False else "",
        circ(90, 40, 22, "none", .8, "3 2") if False else "", L(20, 69, 226, 69, .8, "3 2"),
        N(63, 22, "class {a, b}", 7), N(180, 28, "c, e reachable", 7, "start") if False else N(196, 40, "c → e: no way back", 7, "start"),
        N(120, 120, "i → j ⇔ Pᵢⱼ⁽ⁿ⁾ > 0 for some n ≥ 0; i ↔ j ⇔ i → j and j → i", 7),
        N(120, 132, "S splits into disjoint communicating classes Cₖ", 7.5))

def d4(c):
    out = ax(24, 100, 226, 20) + N(226, 112, "n", 7, "end") + N(28, 24, "Pᵢᵢ⁽ⁿ⁾", 7, "start")
    for i in range(10):
        out += R(34 + i * 18, 100 - 48 / (1 + i * .05), 12, 48 / (1 + i * .05), "#f1f5f9", 1) if False else ""
    out += fn(lambda x: 100 - 34 / (1 + (x - 24) / 40), 30, 220, 50, 1.1) + N(150, 50, "recurrent: ∑ diverges", 7, "start")
    out += fn(lambda x: 100 - 34 * math.exp(-(x - 24) / 28), 30, 220, 50, 1.1, "4 3") + N(150, 86, "transient: ∑ converges", 7, "start")
    return svg(c, out, N(120, 12, "f = ℙ(ever return to i)", 7.5), N(120, 124, "recurrent ⇔ fᵢᵢ = 1 ⇔ ∑ₙ Pᵢᵢ⁽ⁿ⁾ = ∞", 7.5), N(120, 136, "transient ⇔ fᵢᵢ < 1 ⇔ ∑ₙ Pᵢᵢ⁽ⁿ⁾ < ∞", 7.5))

def d5(c):
    out = circ(60, 66, 34, "none", .9)
    for k in range(4):
        a = math.radians(90 - 90 * k)
        out += C(60 + 34 * math.cos(a), 66 - 34 * math.sin(a), 3, "#ffffff" if k else "#000000", 1)
    out += N(60, 24, "0", 7) + N(100, 70, "1", 7, "start") + N(60, 114, "2", 7) + N(16, 70, "3", 7)
    return svg(c, out, N(60, 133, "cycle of length 4: d = 4", 7), N(172, 40, "d(i) = gcd{n ≥ 1 : Pᵢᵢ⁽ⁿ⁾ > 0}", 7, "end") if False else N(226, 36, "d(i) = gcd{n : Pᵢᵢ⁽ⁿ⁾ > 0}", 7, "end"),
        N(226, 56, "returns possible at", 7, "end"), N(226, 66, "n = 4, 8, 12, …", 7, "end"), N(226, 86, "i ↔ j ⇒ d(i) = d(j)", 7.5, "end"), N(226, 100, "and both recurrent or", 7, "end"), N(226, 110, "both transient", 7, "end"))

def d6(c):
    pts = []
    import random
    r = random.Random(4)
    y = 70
    for x in range(30, 222, 8):
        y += r.choice([-10, 10])
        y = max(26, min(112, y))
        pts.append((x, y))
    return svg(c, ax(24, 118, 226, 14), N(226, 128, "step n", 7, "end"), N(28, 14, "position", 7, "start"), L(24, 70, 226, 70, .8, "3 2"),
        poly(pts, 1.1), N(40, 24, "start 0 and return: needs equal ups and downs", 6.5, "start") if False else N(226, 24, "back at 0 only at even n", 7, "end"),
        N(120, 132, "P₀₀⁽²ⁿ⁾ ~ (4p(1−p))ⁿ/√(πn):  p = ½ → ∑ = ∞ (recurrent)", 7), N(120, 143, "p ≠ ½ → geometric decay, ∑ < ∞ (transient)", 7))

CARDS = {
31901: dict(d=d1, kind="DEFINITION",
  stmt=r"<b>Markov chain.</b> A process $(X_n)_{n\ge0}$ on a countable state space $S$ is a Markov chain with transition matrix $P=(P_{ij})$ if $\mathbb P(X_{n+1}=j\mid X_n=i,X_{n-1}=i_{n-1},\ldots,X_0=i_0)=P_{ij}$ for all $n$ and all histories. Each row sums to one: $\sum_{j\in S}P_{ij}=1$ (Ross 4.1; Grimmett 6.1).",
  hint="If tomorrow's commute depends only on today's, how do you tabulate the chances?",
  bd=[r"<strong>$\mathbb P(X_{n+1}=j\mid X_n=i,\ldots,X_0=i_0)$ = tomorrow, given the whole past.</strong> The chance of state $j$ tomorrow, given every day so far.",
      r"<strong>$=P_{ij}$ = only today matters.</strong> The chance depends on the present state $i$ alone, and not on $n$ or on older days.",
      r"<strong>$\sum_jP_{ij}=1$ = rows add to one.</strong> From state $i$, tomorrow lands somewhere; each row of $P$ is a probability law."],
  conn=r"<strong>Today's mood predicts tomorrow's.</strong> If the day is late, the chance that tomorrow is late too is $P_{LL}$, whatever happened last week. A row of the matrix is the odds for tomorrow, and the odds must add to one.",
  cap="Three kinds of morning: on time O, late L, cancelled C. Arrows carry the one-step chances Pᵢⱼ, each row of P adds to one, and tomorrow depends only on today."),
31902: dict(d=d2, kind="THEOREM",
  stmt=r"<b>Chapman–Kolmogorov.</b> For a Markov chain, $P^{(m+n)}_{ij}=\sum_{k\in S}P^{(m)}_{ik}P^{(n)}_{kj}$, i.e. $P^{(m+n)}=P^mP^n$ and so $P^{(n)}=P^n$. If $\mathbf p^{(0)}$ is the law of $X_0$, then $\mathbf p^{(n)}=\mathbf p^{(0)}P^n$ is the law of $X_n$ (Ross 4.2; Grimmett 6.1).",
  hint="How do you get the chances for n days ahead from the one-day table?",
  bd=[r"<strong>$P^{(m+n)}_{ij}$ = from $i$ to $j$ in $m+n$ days.</strong> The chance of being in $j$ after $m+n$ steps, started at $i$.",
      r"<strong>$\sum_kP^{(m)}_{ik}P^{(n)}_{kj}$ = pass through a middle state.</strong> After $m$ days you are at some $k$; sum over every possible $k$, then continue for $n$ days.",
      r"<strong>$\mathbf p^{(n)}=\mathbf p^{(0)}P^n$ = the law after $n$ days.</strong> Multiply the starting row vector by the matrix $n$ times."],
  conn=r"<strong>Two weeks ahead by squaring.</strong> To predict the day after tomorrow, sum over what tomorrow could be: on time, late or cancelled. That sum is exactly one matrix product, so $n$ days ahead is the $n$-th power of the table.",
  cap="To go from i to j in m + n steps, pass through some state k after m steps and sum over all k. This is the matrix product Pᵐ⁺ⁿ = Pᵐ Pⁿ."),
31903: dict(d=d3, kind="DEFINITION",
  stmt=r"<b>Accessibility and communication.</b> State $j$ is accessible from $i$, $i\to j$, if $P^{(n)}_{ij}>0$ for some $n\ge0$. States communicate, $i\leftrightarrow j$, if $i\to j$ and $j\to i$. Communication is an equivalence relation, so the state space splits into disjoint classes: $S=\bigcup_kC_k$ (Ross 4.3; Grimmett 6.2).",
  hint="Which mornings can lead to which, and which pairs can lead to each other?",
  bd=[r"<strong>$i\to j\iff P^{(n)}_{ij}>0$ for some $n\ge0$ = a path exists.</strong> There is a sequence of possible one-day moves from $i$ to $j$.",
      r"<strong>$i\leftrightarrow j$ = a path both ways.</strong> Each can reach the other; this is reflexive, symmetric and transitive.",
      r"<strong>$S=\bigcup_kC_k$ = classes.</strong> The relation cuts the states into groups that talk among themselves; a class with no exit is closed."],
  conn=r"<strong>Which situations connect.</strong> From on time you can drift to late and back, so those two are one class. A cancelled bus that never returns to normal would sit on its own, reachable but unable to get back.",
  cap="States a and b reach each other: one class. State c is reachable from b but cannot return, so it is its own class. The classes partition the state space."),
31904: dict(d=d4, kind="THEOREM",
  stmt=r"<b>Recurrence and transience.</b> Let $f_{ii}=\mathbb P(X_n=i\text{ for some }n\ge1\mid X_0=i)$. State $i$ is recurrent iff $f_{ii}=1$ iff $\sum_{n\ge1}P^{(n)}_{ii}=\infty$, and transient iff $f_{ii}<1$ iff $\sum_{n\ge1}P^{(n)}_{ii}<\infty$ (Ross 4.3; Grimmett 6.2).",
  hint="Will you return to the same kind of morning for sure, or may you leave and never come back?",
  bd=[r"<strong>$f_{ii}$ = the chance of ever returning to $i$.</strong> Start at $i$; $f_{ii}$ is the probability of being at $i$ again at some later day.",
      r"<strong>$f_{ii}=1$ = recurrent.</strong> You return for sure, hence infinitely often, so the expected number of visits $\sum_nP^{(n)}_{ii}$ is infinite.",
      r"<strong>$f_{ii}<1$ = transient.</strong> Each visit may be the last; the number of visits is geometric, so $\sum_nP^{(n)}_{ii}<\infty$."],
  conn=r"<strong>A normal morning keeps coming back.</strong> A usual on-time morning recurs for ever. But a one-off, like the bus route being scrapped, may happen once and never again, and that state is transient.",
  cap="Return chances Pᵢᵢ⁽ⁿ⁾ against n. For a recurrent state they decay slowly enough to sum to infinity; for a transient state they decay fast and the sum is finite."),
31905: dict(d=d5, kind="DEFINITION",
  stmt=r"<b>Period and class properties.</b> The period of $i$ is $d(i)=\gcd\{n\ge1:P^{(n)}_{ii}>0\}$; $i$ is aperiodic if $d(i)=1$. If $i\leftrightarrow j$ then $d(i)=d(j)$, and $i$ is recurrent iff $j$ is recurrent: period, recurrence and transience are class properties (Ross 4.3; Grimmett 6.2).",
  hint="If you can only be back at the same state every fourth day, what does that tell the rest of the class?",
  bd=[r"<strong>$\{n\ge1:P^{(n)}_{ii}>0\}$ = possible return times.</strong> The numbers of days after which you can be back at $i$.",
      r"<strong>$d(i)=\gcd$ = the period.</strong> The greatest common divisor of those times: returns can only happen at multiples of $d(i)$.",
      r"<strong>$i\leftrightarrow j\Rightarrow d(i)=d(j)$ = shared by the class.</strong> Period, recurrence and transience are the same for all states in a communicating class."],
  conn=r"<strong>A fixed weekly rhythm.</strong> If your cycle is a four-day shift pattern, you can be in the same state only every 4th day, and so can every state in that cycle. Mixing in a pattern of another length breaks the rhythm.",
  cap="A four-state cycle: from state 0 you can be back only at times 4, 8, 12, …, so the period is 4. Every state of the class shares that period."),
31906: dict(d=d6, kind="WORKED EXAMPLE",
  stmt=r"<b>Pólya: the 1D random walk.</b> Step $+1$ with probability $p$, $-1$ with $1-p$. Then $P^{(2n)}_{00}=\binom{2n}n(p(1-p))^n\sim\frac{(4p(1-p))^n}{\sqrt{\pi n}}$. For $p=\tfrac12$ the sum $\sum_nP^{(2n)}_{00}=\infty$ (recurrent); for $p\ne\tfrac12$ it is finite (transient) (Ross 4.3; Grimmett 6.3).",
  hint="Does a fair walk along the street come home for sure, and what if the wind blows one way?",
  bd=[r"<strong>$P^{(2n)}_{00}=\binom{2n}n(p(1-p))^n$ = $n$ ups and $n$ downs.</strong> Back at 0 needs equally many ups and downs, so only at even times.",
      r"<strong>$\sim(4p(1-p))^n/\sqrt{\pi n}$ = Stirling.</strong> For $p=\frac12$ the base is exactly 1, leaving $1/\sqrt{\pi n}$; otherwise $4p(1-p)<1$.",
      r"<strong>$\sum=\infty$ iff $p=\frac12$.</strong> $\sum1/\sqrt n$ diverges (recurrent); a geometric tail is summable (transient)."],
  conn=r"<strong>Wandering to and fro.</strong> If you take random steps up and down the street and each direction is equally likely, you come back to your door for sure. With any bias, you drift away and may never return.",
  cap="A random walk and its return level 0. With p = ½ the return chances ~ 1/√(πn) sum to infinity; with p ≠ ½ they decay geometrically and the sum is finite."),
}

STORY = {
31901: dict(s="STORY 19 · STEP 1 · TOMORROW FROM TODAY", b="A <b>Markov chain</b> remembers only today; its rows of chances add to one.", f=[["30201", "conditional probability"], ["31806", "a count of independent days"]], n=[["31902", "many days ahead"]]),
31902: dict(s="STORY 19 · STEP 2 · MANY DAYS AHEAD", b="<b>Chapman–Kolmogorov</b>: n-day chances are the n-th power of the one-day table.", f=[["31901", "transition matrix"], ["30203", "total probability"]], n=[["31903", "which states connect"], ["32001", "the long run"]]),
31903: dict(s="STORY 19 · STEP 3 · WHO CONNECTS", b="States that reach each other form a <b>class</b>; the state space splits into classes.", f=[["31902", "n-step chances"]], n=[["31904", "return or not"]]),
31904: dict(s="STORY 19 · STEP 4 · RETURN OR VANISH", b="A state is <b>recurrent</b> if you return for sure, <b>transient</b> otherwise.", f=[["31903", "classes"], ["31605", "Borel–Cantelli"]], n=[["31905", "rhythm of returns"], ["31906", "the random walk"]]),
31905: dict(s="STORY 19 · STEP 5 · RHYTHM", b="The <b>period</b> is the gcd of return times; it is shared by the whole class.", f=[["31904", "recurrence"]], n=[["32002", "convergence needs aperiodicity"]]),
31906: dict(s="STORY 19 · STEP 6 · A WALK", b="The fair 1D walk is <b>recurrent</b>; any bias makes it transient.", f=[["31904", "return sums"], ["31806", "binomial counts"]], n=[["32501", "random walks and Brownian motion"]]),
}

FIX = build(CARDS)
