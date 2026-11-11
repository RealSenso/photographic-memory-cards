"""StoMA topic 20 (stationary distributions). F1 picture: Max's result from race to race is a win (W) or no win (N), with P(W,W) = 0.8 and P(N,W) = 0.4; in the long run he wins two races in three, and the first race of the season is forgotten."""
from f1_lib import *

SUBJECT = "StoMA"

def nd(x, y, lab, r=11):
    return circ(x, y, r, "#ffffff", 1) + N(x, y + 3, lab, 8)

def bars(x0, vals, base=100, k=60, fill="#f1f5f9", w=18):
    out = ""
    for i, v in enumerate(vals):
        out += R(x0 + i * (w + 6), base - v * k, w, v * k, fill, 1)
    return out

def d1(c):
    return svg(c, ax(24, 100, 226, 20), bars(50, [2 / 3, 1 / 3]), N(59, 112, "W", 7.5), N(83, 112, "N", 7.5),
        N(59, 56, "π(W)", 7.5), N(83, 78, "π(N)", 7.5), N(170, 40, "one more race:", 7.5, "start"), N(170, 52, "πᵀP = πᵀ", 8, "start"), N(170, 64, "nothing changes", 7, "start"),
        N(120, 12, "the long-run shares of wins and non-wins", 7.5),
        N(120, 126, "πⱼ = ∑ᵢ πᵢ Pᵢⱼ,   ∑ᵢ πᵢ = 1", 8), N(120, 138, "W: 0.8·⅔ + 0.4·⅓ = ⅔", 7))

def d2(c):
    out = ax(24, 108, 226, 20) + N(226, 120, "race n", 7, "end") + N(28, 20, "ℙ(win in race n)", 7, "start")
    out += fn(lambda x: 108 - 60 * (2 / 3 + (1 / 3) * math.exp(-(x - 24) / 40)), 24, 226, 50, 1.1)
    out += fn(lambda x: 108 - 60 * (2 / 3 - (2 / 3) * math.exp(-(x - 24) / 40)), 24, 226, 50, 1.1, "4 3")
    out += L(24, 68, 226, 68, .8, "2 3") + N(224, 62, "πⱼ = 1/μⱼⱼ", 7.5, "end")
    return svg(c, out, N(124, 36, "first race a win", 7), N(124, 98, "first race not a win", 7), N(120, 134, "Pᵢⱼ⁽ⁿ⁾ → πⱼ = 1 / 𝔼[return time to j] > 0, whatever i", 7))

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
    return svg(c, nd(60, 50, "W"), nd(180, 50, "N"), L(120, 14, 120, 100, 1, "4 3"), arrow(72, 44, 168, 44, 1), arrow(168, 56, 72, 56, 1),
        N(120, 38, "πₒ Pₒₗ", 7.5) if False else N(120, 34, "π(W) P(W,N)  →", 7), N(120, 74, "←  π(N) P(N,W)", 7), N(120, 11, "cut A | Aᶜ", 7),
        N(120, 112, "flow across any cut balances: ∑ πᵢPᵢⱼ (i∈A, j∈Aᶜ) = ∑ πⱼPⱼᵢ", 6.5),
        N(120, 124, "detailed balance πᵢPᵢⱼ = πⱼPⱼᵢ ⇒ πᵀP = πᵀ", 7.5), N(120, 136, "(2/3)(0.2) = (1/3)(0.4) = 2/15", 7))

def d5(c):
    out = nd(70, 60, "W") + nd(160, 60, "N") + arrow(82, 54, 148, 54, 1) + arrow(148, 66, 82, 66, 1)
    return svg(c, out, N(115, 44, "flip every race: period 2", 7), N(115, 90, "Pⁿ never settles:", 7), N(115, 101, "W, N, W, N, …", 7),
        N(120, 12, "(1/N) ∑ₙ Pᵢⱼ⁽ⁿ⁾ → πⱼ even for a periodic chain", 7.5), N(120, 122, "the average over races converges, though each race's chance does not", 7), N(120, 134, "π = (½, ½)", 7.5))

def d6(c):
    import random
    r = random.Random(2)
    out = ax(24, 108, 226, 20) + N(226, 120, "N races", 7, "end") + N(28, 20, "fraction of non-wins", 7, "start")
    pts, late, st = [], 0, 0
    for n in range(1, 61):
        st = (1 if r.random() < .2 else 0) if st == 0 else (0 if r.random() < .4 else 1)
        late += st
        pts.append((24 + n * 3.3, 108 - 60 * late / n * 1.0))
    out += L(24, 88, 226, 88, .8, "3 2") + N(224, 82, "π(N) = ⅓", 7.5, "end") + poly(pts, 1.1)
    return svg(c, out, N(120, 134, "(1/N) ∑ f(Xₙ) → ∑ⱼ πⱼ f(j) = 𝔼_π[f]  almost surely", 7.5))

CARDS = {
32001: dict(d=d1, kind="DEFINITION",
  stmt=r"<b>Stationary distribution.</b> A probability vector $\pi$ on $S$ is stationary for $P$ if $\pi^{\top}P=\pi^{\top}$, i.e. $\pi_j=\sum_{i\in S}\pi_iP_{ij}$ for all $j$, with $\pi_i\ge0$ and $\sum_i\pi_i=1$. If $X_0\sim\pi$ then $X_n\sim\pi$ for every $n$ (Ross 4.4; Grimmett 6.4).",
  hint='Which split of wins and non-wins stays exactly the same from one race to the next?',
  bd=[r"<strong>$\pi_j=\sum_i\pi_iP_{ij}$ = inflow equals share.</strong> The weight of $j$ next race is what flows in from every $i$, weighted by this race's share $\pi_i$.",
      r"<strong>$\sum_i\pi_i=1$ = a genuine split.</strong> The shares are probabilities, so they add to one.",
      r"<strong>$\pi^{\top}P=\pi^{\top}$ = left eigenvector for 1.</strong> Start from $\pi$ and one step of the chain gives back $\pi$: the law is frozen."],
  conn=r"<strong>Max's steady win rate.</strong> Say after a win he wins again with chance $0.8$, and after a non-win he wins with chance $0.4$. Then a split of $\frac23$ wins and $\frac13$ non-wins reproduces itself: $0.8\cdot\frac23+0.4\cdot\frac13=\frac23$.",
  cap='The stationary split (π win = ⅔, π no win = ⅓) as bars. One more race leaves the split unchanged, since πᵀP = πᵀ.'),
32002: dict(d=d2, kind="THEOREM",
  stmt=r"<b>Fundamental limit theorem.</b> For an irreducible, aperiodic, positive recurrent chain, $\lim_{n\to\infty}P^{(n)}_{ij}=\pi_j=\dfrac1{\mu_{jj}}>0$ for all $i,j$, where $\mu_{jj}=\mathbb E[\tau_j\mid X_0=j]$ is the mean return time to $j$, and $\pi$ is the unique stationary distribution (Ross 4.4; Grimmett 6.4).",
  hint="Why does Max's chance of winning a race far into the season settle on one number, however the season began?",
  bd=[r"<strong>$P^{(n)}_{ij}\to\pi_j$ = the start is forgotten.</strong> After many races the chance of being at $j$ does not depend on $i$.",
      r"<strong>$\pi_j=1/\mu_{jj}$ = share equals one over the gap.</strong> If he comes back to $j$ every $\mu_{jj}$ races on average, a fraction $1/\mu_{jj}$ of races are at $j$.",
      '<strong>Irreducible, aperiodic, positive recurrent = the conditions.</strong> One class, no rigid rhythm, and finite mean return times.'],
  conn=r"<strong>The first race of the season does not matter.</strong> Whether Max won the opener or not, by mid-season the chance he wins a given race is the same $\frac23$. That is one over the mean return time to a win: on average the next win comes $1/\pi_W=1.5$ races later.",
  cap='Chance that Max wins race n when the first race was a win (solid) or not a win (dashed): both settle at the same level π = 1/μ, so the start is forgotten.'),
32003: dict(d=d3, kind="THEOREM",
  stmt=r"<b>Positive versus null recurrence.</b> A recurrent state $i$ is positive recurrent if $\mu_{ii}=\mathbb E[\tau_i\mid X_0=i]<\infty$ and null recurrent if $\mu_{ii}=\infty$. An irreducible chain has a stationary distribution iff it is positive recurrent; for null recurrent or transient chains $\pi_i\equiv0$ (e.g. the symmetric random walk) (Ross 4.4; Grimmett 6.4).",
  hint='He comes back for sure, but can the average time to come back be so long that no long-run share exists?',
  bd=[r"<strong>$\mu_{ii}<\infty$ = positive recurrent.</strong> The expected time to return is finite, so a positive fraction of races is spent at $i$.",
      r"<strong>$\mu_{ii}=\infty$ = null recurrent.</strong> The return is sure but the expected time is infinite, so the long-run share is zero.",
      r"<strong>Stationary $\pi$ exists iff positive recurrent.</strong> In the null recurrent case the limits $\pi_i$ are all 0 and cannot add to one."],
  conn='<strong>Sure to be level again, but too slowly.</strong> If two equally quick cars swap a tenth back and forth each lap with no limit on the gap, they are sure to be level again, but the average time until then is infinite. So there is no steady share of laps spent level, even though it keeps happening.',
  cap='Shares πᵢ in a positive recurrent chain add to one. For a null recurrent chain, such as the fair walk of the gap on the whole line, every πᵢ is 0 and no stationary law exists.'),
32004: dict(d=d4, kind="THEOREM",
  stmt=r"<b>Cut equations and detailed balance.</b> If $\pi$ is stationary then for every $A\subset S$, $\sum_{i\in A,\,j\in A^c}\pi_iP_{ij}=\sum_{j\in A^c,\,i\in A}\pi_jP_{ji}$. If $\pi_iP_{ij}=\pi_jP_{ji}$ for all $i,j$ (detailed balance), then $\pi^{\top}P=\pi^{\top}$ and the chain is reversible (Ross 4.8; Grimmett 6.5).",
  hint='How can you find the steady split by balancing the moves between two groups of results?',
  bd=[r"<strong>$\sum_{i\in A,j\in A^c}\pi_iP_{ij}$ = flow out of $A$.</strong> The long-run rate of moves from a set $A$ to its complement.",
      '<strong>= flow back into $A$.</strong> In a steady state what leaves a set must come back at the same rate.',
      r"<strong>$\pi_iP_{ij}=\pi_jP_{ji}$ = detailed balance.</strong> If every pair of states balances on its own, adding over $i$ gives $\pi_j=\sum_i\pi_iP_{ij}$."],
  conn=r"<strong>Balance the flow.</strong> Of all races, $\frac23$ are wins and $\frac15$ of those are followed by a non-win; $\frac13$ are non-wins and $\frac25$ of those are followed by a win. Both flows are $\frac2{15}$ of all races: the streaks that end match the streaks that start.",
  cap='The cut between win and no win. In steady state the rate win → no win, π(W)P(W,N), equals the rate no win → win, π(N)P(N,W) (both 2/15).'),
32005: dict(d=d5, kind="THEOREM",
  stmt=r"<b>Periodic chains and Cesàro limits.</b> For an irreducible positive recurrent chain, periodic or not, $\lim_{N\to\infty}\frac1N\sum_{n=1}^NP^{(n)}_{ij}=\pi_j$. If the chain has period $d>1$, $P^{(n)}_{ij}$ itself does not converge (Ross 4.4; Grimmett 6.4).",
  hint="If Max's results flip back and forth in a fixed rhythm, in what sense do they still settle?",
  bd=[r"<strong>$P^{(n)}_{ij}$ may oscillate.</strong> A strictly alternating chain has $P^{(n)}_{ii}=1,0,1,0,\ldots$, with no limit.",
      r"<strong>$\frac1N\sum_{n=1}^NP^{(n)}_{ij}$ = the time average of the chances.</strong> Averaging over the races flattens the oscillation.",
      r"<strong>$\to\pi_j$ = the long-run share still exists.</strong> The Cesàro limit is $\pi_j$ for every irreducible positive recurrent chain."],
  conn='<strong>Strictly alternating results still have a share.</strong> If Max won exactly every other race, the chance he wins race $n$ is 0 or 1 and never settles. But the fraction of wins over many races is steady at one half.',
  cap='A chain that flips W, N, W, N, … has period 2: Pⁿ oscillates for ever, but the average over races converges to π = (½, ½).'),
32006: dict(d=d6, kind="THEOREM",
  stmt=r"<b>Ergodic theorem for Markov chains.</b> For an irreducible positive recurrent chain with stationary $\pi$ and $f$ with $\sum_j\pi_j|f(j)|<\infty$, $\lim_{N\to\infty}\frac1N\sum_{n=1}^Nf(X_n)=\sum_{j\in S}\pi_jf(j)=\mathbb E_\pi[f(X)]$ almost surely, from any starting state (Ross 4.4; Grimmett 6.4).",
  hint='Does one long career show the steady shares, without averaging over many imagined seasons?',
  bd=[r"<strong>$\frac1N\sum_{n\le N}f(X_n)$ = a time average on one run.</strong> Follow one run of races and average a quantity $f$ of each race's result.",
      r"<strong>$\sum_j\pi_jf(j)$ = the average under $\pi$.</strong> The same quantity averaged over the stationary split.",
      '<strong>almost surely = every run.</strong> This is the strong law for dependent races: time averages equal space averages.'],
  conn=r"<strong>One career tells the story.</strong> Keep a tally of how many races Max did not win. Over a long career that fraction gets very close to $\frac13$, just as the steady split says, whatever happened in his first race. Points work the same way: average points per race tend to $\sum_j\pi_jf(j)$.",
  cap='The fraction of non-wins along one long run of races converges to π(N) = ⅓: the time average along a single path equals the average under the stationary split.'),
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
