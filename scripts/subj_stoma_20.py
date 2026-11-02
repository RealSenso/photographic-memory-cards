"""StoMA topic 20 (stationary distributions). Commute picture: long-run share of on-time (O) and late (L) mornings."""
from commute_lib import *

SUBJECT = "StoMA"

def nd(x, y, lab, r=11):
    return circ(x, y, r, "#ffffff", 1) + N(x, y + 3, lab, 8)

def bars(x0, vals, base=100, k=60, fill="#f1f5f9", w=18):
    out = ""
    for i, v in enumerate(vals):
        out += R(x0 + i * (w + 6), base - v * k, w, v * k, fill, 1)
    return out

def d1(c):
    return svg(c, ax(24, 100, 226, 20), bars(50, [2 / 3, 1 / 3]), N(59, 112, "O", 7.5), N(83, 112, "L", 7.5),
        N(59, 56, "π(O)", 7.5), N(83, 78, "π(L)", 7.5), N(170, 40, "one more day:", 7.5, "start"), N(170, 52, "πᵀP = πᵀ", 8, "start"), N(170, 64, "nothing changes", 7, "start"),
        N(120, 12, "the long-run shares of each kind of morning", 7.5),
        N(120, 126, "πⱼ = ∑ᵢ πᵢ Pᵢⱼ,   ∑ᵢ πᵢ = 1", 8), N(120, 138, "O: 0.8·⅔ + 0.4·⅓ = ⅔", 7))

def d2(c):
    out = ax(24, 108, 226, 20) + N(226, 120, "day n", 7, "end") + N(28, 20, "ℙ(on time on day n)", 7, "start")
    out += fn(lambda x: 108 - 60 * (2 / 3 + (1 / 3) * math.exp(-(x - 24) / 40)), 24, 226, 50, 1.1)
    out += fn(lambda x: 108 - 60 * (2 / 3 - (2 / 3) * math.exp(-(x - 24) / 40)), 24, 226, 50, 1.1, "4 3")
    out += L(24, 68, 226, 68, .8, "2 3") + N(224, 62, "πⱼ = 1/μⱼⱼ", 7.5, "end")
    return svg(c, out, N(124, 36, "start on time", 7), N(124, 98, "start late", 7), N(120, 134, "Pᵢⱼ⁽ⁿ⁾ → πⱼ = 1 / 𝔼[return time to j] > 0, whatever i", 7))

def d3(c):
    out = ax(24, 100, 226, 20) + N(226, 112, "i", 7, "end")
    for i in range(1, 8):
        out += R(26 + i * 24, 100 - 30 / i ** .3, 14, 30 / i ** .3, "#f1f5f9", 1) if False else ""
    for i in range(8):
        out += C(40 + i * 24, 100 - 40 * math.exp(-i / 3), 2.2)
    out += fn(lambda x: 100 - 40 * math.exp(-(x - 40) / 72), 40, 208, 40, .9, "3 2")
    return svg(c, out, N(30, 22, "πᵢ", 7.5, "start"), N(150, 34, "positive recurrent:", 7, "start"), N(150, 44, "∑ πᵢ = 1, μᵢᵢ < ∞", 7, "start"),
        N(120, 122, "null recurrent: μᵢᵢ = ∞, πᵢ ≡ 0, no stationary law", 7), N(120, 134, "(e.g. the symmetric walk returns, but too slowly)", 7),
        N(120, 12, "a long-run share needs finite expected return time", 7.5))

def d4(c):
    return svg(c, nd(60, 50, "O"), nd(180, 50, "L"), L(120, 14, 120, 100, 1, "4 3"), arrow(72, 44, 168, 44, 1), arrow(168, 56, 72, 56, 1),
        N(120, 38, "πₒ Pₒₗ", 7.5) if False else N(120, 34, "πₒ Pₒₗ  →", 7), N(120, 74, "←  πₗ Pₗₒ", 7), N(120, 11, "cut A | Aᶜ", 7),
        N(120, 112, "flow across any cut balances: ∑ πᵢPᵢⱼ (i∈A, j∈Aᶜ) = ∑ πⱼPⱼᵢ", 6.5),
        N(120, 124, "detailed balance πᵢPᵢⱼ = πⱼPⱼᵢ ⇒ πᵀP = πᵀ", 7.5), N(120, 136, "(2/3)(0.2) = (1/3)(0.4) = 2/15", 7))

def d5(c):
    out = nd(70, 60, "O") + nd(160, 60, "L") + arrow(82, 54, 148, 54, 1) + arrow(148, 66, 82, 66, 1)
    return svg(c, out, N(115, 44, "flip every day: period 2", 7), N(115, 90, "Pⁿ never settles:", 7), N(115, 101, "O, L, O, L, …", 7),
        N(120, 12, "(1/N) ∑ₙ Pᵢⱼ⁽ⁿ⁾ → πⱼ even for a periodic chain", 7.5), N(120, 122, "the average over days converges, though the daily chance does not", 7), N(120, 134, "π = (½, ½)", 7.5))

def d6(c):
    import random
    r = random.Random(2)
    out = ax(24, 108, 226, 20) + N(226, 120, "N days", 7, "end") + N(28, 20, "fraction late", 7, "start")
    pts, late, st = [], 0, 0
    for n in range(1, 61):
        st = (1 if r.random() < .2 else 0) if st == 0 else (0 if r.random() < .4 else 1)
        late += st
        pts.append((24 + n * 3.3, 108 - 60 * late / n * 1.0))
    out += L(24, 88, 226, 88, .8, "3 2") + N(224, 82, "π(L) = ⅓", 7.5, "end") + poly(pts, 1.1)
    return svg(c, out, N(120, 134, "(1/N) ∑ f(Xₙ) → ∑ⱼ πⱼ f(j) = 𝔼_π[f]  almost surely", 7.5))

CARDS = {
32001: dict(d=d1, kind="DEFINITION",
  stmt=r"<b>Stationary distribution.</b> A probability vector $\pi$ on $S$ is stationary for $P$ if $\pi^{\top}P=\pi^{\top}$, i.e. $\pi_j=\sum_{i\in S}\pi_iP_{ij}$ for all $j$, with $\pi_i\ge0$ and $\sum_i\pi_i=1$. If $X_0\sim\pi$ then $X_n\sim\pi$ for every $n$ (Ross 4.4; Grimmett 6.4).",
  hint="Which split of on-time and late mornings stays exactly the same from one day to the next?",
  bd=[r"<strong>$\pi_j=\sum_i\pi_iP_{ij}$ = inflow equals share.</strong> The weight of $j$ tomorrow is what flows in from every $i$, weighted by today's share $\pi_i$.",
      r"<strong>$\sum_i\pi_i=1$ = a genuine split.</strong> The shares are probabilities, so they add to one.",
      r"<strong>$\pi^{\top}P=\pi^{\top}$ = left eigenvector for 1.</strong> Start from $\pi$ and one step of the chain returns $\pi$: the law is frozen."],
  conn=r"<strong>The steady mix of mornings.</strong> With $P_{OO}=0.8$ and $P_{LO}=0.4$, a split of $\frac23$ on time and $\frac13$ late reproduces itself: $0.8\cdot\frac23+0.4\cdot\frac13=\frac23$.",
  cap="The stationary split (π on time = ⅔, π late = ⅓) as bars. One more step of the chain leaves the split unchanged, since πᵀP = πᵀ."),
32002: dict(d=d2, kind="THEOREM",
  stmt=r"<b>Fundamental limit theorem.</b> For an irreducible, aperiodic, positive recurrent chain, $\lim_{n\to\infty}P^{(n)}_{ij}=\pi_j=\dfrac1{\mu_{jj}}>0$ for all $i,j$, where $\mu_{jj}=\mathbb E[\tau_j\mid X_0=j]$ is the mean return time to $j$, and $\pi$ is the unique stationary distribution (Ross 4.4; Grimmett 6.4).",
  hint="Why does the chance of a late day settle on one number regardless of how the chain started?",
  bd=[r"<strong>$P^{(n)}_{ij}\to\pi_j$ = the start is forgotten.</strong> After many days the chance of being at $j$ does not depend on $i$.",
      r"<strong>$\pi_j=1/\mu_{jj}$ = share equals one over the gap.</strong> If you return to $j$ every $\mu_{jj}$ days on average, you spend a fraction $1/\mu_{jj}$ of days there.",
      r"<strong>Irreducible, aperiodic, positive recurrent = the conditions.</strong> One class, no rigid rhythm, and finite mean return times."],
  conn=r"<strong>The first day does not matter.</strong> Whether the term began with a bad morning or a good one, in a few weeks the chance that a given day is late is the same $\frac13$, one over the average gap of 3 days between late days.",
  cap="Chance of an on-time morning on day n starting on time (solid) or late (dashed): both converge to the same level π = 1/μ, the start is forgotten."),
32003: dict(d=d3, kind="THEOREM",
  stmt=r"<b>Positive versus null recurrence.</b> A recurrent state $i$ is positive recurrent if $\mu_{ii}=\mathbb E[\tau_i\mid X_0=i]<\infty$ and null recurrent if $\mu_{ii}=\infty$. An irreducible chain has a stationary distribution iff it is positive recurrent; for null recurrent or transient chains $\pi_i\equiv0$ (e.g. the symmetric random walk) (Ross 4.4; Grimmett 6.4).",
  hint="You return for sure, but can the waiting time be so long that no long-run share exists?",
  bd=[r"<strong>$\mu_{ii}<\infty$ = positive recurrent.</strong> The expected time to return is finite, so a positive fraction of days is spent at $i$.",
      r"<strong>$\mu_{ii}=\infty$ = null recurrent.</strong> You return for sure but the expected wait is infinite, so the long-run share is zero.",
      r"<strong>Stationary $\pi$ exists iff positive recurrent.</strong> In the null recurrent case the limits $\pi_i$ are all 0 and cannot add to one."],
  conn=r"<strong>Sure to come back, but too slowly.</strong> A walker on an endless street returns to the start for sure, but the average wait is infinite. So there is no steady share of days at the start, even though it keeps being visited.",
  cap="Shares πᵢ in a positive recurrent chain add to one. For a null recurrent chain, such as the symmetric walk on the line, every πᵢ is 0 and no stationary law exists."),
32004: dict(d=d4, kind="THEOREM",
  stmt=r"<b>Cut equations and detailed balance.</b> If $\pi$ is stationary then for every $A\subset S$, $\sum_{i\in A,\,j\in A^c}\pi_iP_{ij}=\sum_{j\in A^c,\,i\in A}\pi_jP_{ji}$. If $\pi_iP_{ij}=\pi_jP_{ji}$ for all $i,j$ (detailed balance), then $\pi^{\top}P=\pi^{\top}$ and the chain is reversible (Ross 4.8; Grimmett 6.5).",
  hint="How can you find the steady split by balancing the traffic between two groups of mornings?",
  bd=[r"<strong>$\sum_{i\in A,j\in A^c}\pi_iP_{ij}$ = flow out of $A$.</strong> The long-run rate of moves from a set $A$ to its complement.",
      r"<strong>= flow back into $A$.</strong> In a steady state what leaves a set must return at the same rate.",
      r"<strong>$\pi_iP_{ij}=\pi_jP_{ji}$ = detailed balance.</strong> If every pair of states balances individually, summing over $i$ gives $\pi_j=\sum_i\pi_iP_{ij}$."],
  conn=r"<strong>Balance the traffic.</strong> Of all days, $\frac23$ are on time and $\frac15$ of those are followed by a late day, $\frac13$ are late and $\frac25$ of those are followed by an on-time day: both flows are $\frac2{15}$.",
  cap="The cut between on time and late. In steady state the rate on time → late, πₒPₒₗ, equals the rate late → on time, πₗPₗₒ (both 2/15)."),
32005: dict(d=d5, kind="THEOREM",
  stmt=r"<b>Periodic chains and Cesàro limits.</b> For an irreducible positive recurrent chain, periodic or not, $\lim_{N\to\infty}\frac1N\sum_{n=1}^NP^{(n)}_{ij}=\pi_j$. If the chain has period $d>1$, $P^{(n)}_{ij}$ itself does not converge (Ross 4.4; Grimmett 6.4).",
  hint="If the chain flips back and forth with a fixed rhythm, in what sense does it still settle?",
  bd=[r"<strong>$P^{(n)}_{ij}$ may oscillate.</strong> A strictly alternating chain has $P^{(n)}_{ii}=1,0,1,0,\ldots$, with no limit.",
      r"<strong>$\frac1N\sum_{n=1}^NP^{(n)}_{ij}$ = the time average of the chances.</strong> Averaging over the days flattens the oscillation.",
      r"<strong>$\to\pi_j$ = the long-run share still exists.</strong> The Cesàro limit is $\pi_j$ for every irreducible positive recurrent chain."],
  conn=r"<strong>Alternating days still have a share.</strong> If good and bad days strictly alternate, the chance of a good day tomorrow is 0 or 1, never settling. But the fraction of good days among many is steady at one half.",
  cap="A chain that flips O, L, O, L, … has period 2: Pⁿ oscillates for ever, but the average over days converges to π = (½, ½)."),
32006: dict(d=d6, kind="THEOREM",
  stmt=r"<b>Ergodic theorem for Markov chains.</b> For an irreducible positive recurrent chain with stationary $\pi$ and $f$ with $\sum_j\pi_j|f(j)|<\infty$, $\lim_{N\to\infty}\frac1N\sum_{n=1}^Nf(X_n)=\sum_{j\in S}\pi_jf(j)=\mathbb E_\pi[f(X)]$ almost surely, from any starting state (Ross 4.4; Grimmett 6.4).",
  hint="Does one long run of commutes show the steady shares, without averaging over many runs?",
  bd=[r"<strong>$\frac1N\sum_{n\le N}f(X_n)$ = a time average on one run.</strong> Follow one run of days and average a quantity $f$ of each day's state.",
      r"<strong>$\sum_j\pi_jf(j)$ = the average under $\pi$.</strong> The same quantity averaged over the stationary split.",
      r"<strong>almost surely = every run.</strong> This is the strong law for dependent days: time averages equal space averages."],
  conn=r"<strong>One term tells the story.</strong> Keep a tally of how many mornings were late. After a long term, the fraction of late mornings is very close to $\frac13$, just as the steady split says, whatever happened on day one.",
  cap="The fraction of late mornings along one long run converges to π(L) = ⅓: the time average along a single path equals the average under the stationary split."),
}

STORY = {
32001: dict(s="STORY 20 · STEP 1 · THE STEADY SPLIT", b="A <b>stationary distribution</b> is a split of states that one step of the chain leaves unchanged.", f=[["31902", "one-step update pᵀP"]], n=[["32002", "does the chain converge to it"], ["32004", "finding it by balance"]]),
32002: dict(s="STORY 20 · STEP 2 · THE START IS FORGOTTEN", b="Under irreducibility, aperiodicity and positive recurrence, <b>Pⁿ → π</b> and π = 1/(mean return time).", f=[["32001", "stationary law"], ["31905", "aperiodicity"], ["31904", "recurrence"]], n=[["32003", "when it fails"], ["32005", "periodic chains"]]),
32003: dict(s="STORY 20 · STEP 3 · SURE TO RETURN, TOO SLOWLY", b="<b>Null recurrent</b> states return for sure but with infinite mean time: no steady share.", f=[["32002", "limit theorem"], ["31906", "the symmetric walk"]], n=[["32004", "what balance needs"]]),
32004: dict(s="STORY 20 · STEP 4 · BALANCE THE FLOW", b="<b>Cut equations</b> and <b>detailed balance</b> find π by balancing flows.", f=[["32001", "stationary law"]], n=[["32204", "MCMC uses detailed balance"]]),
32005: dict(s="STORY 20 · STEP 5 · RHYTHM STILL AVERAGES", b="With a fixed rhythm, Pⁿ oscillates but its <b>Cesàro average</b> still converges to π.", f=[["32002", "limit theorem"], ["31905", "period"]], n=[["32006", "time averages"]]),
32006: dict(s="STORY 20 · STEP 6 · ONE RUN IS ENOUGH", b="The <b>ergodic theorem</b>: time averages along one run equal averages under π.", f=[["32005", "Cesàro limit"], ["31702", "the strong law"]], n=[["32101", "chains that end in absorption"]]),
}

FIX = build(CARDS)
