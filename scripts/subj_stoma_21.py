"""StoMA topic 21 (absorption). Commute picture: the bus route has absorbing outcomes: reach campus (A) or give up and go home (B)."""
from commute_lib import *

SUBJECT = "StoMA"

def nd(x, y, lab, r=11, fill="#ffffff"):
    return circ(x, y, r, fill, 1) + N(x, y + 3, lab, 8)

def line_chain(n=5, y=56, x0=36, dx=40, lab=None):
    out = ""
    for i in range(n):
        out += nd(x0 + i * dx, y, (lab or ["B", "1", "2", "3", "A"])[i], 11, "#d9dee7" if i in (0, n - 1) else "#ffffff")
    for i in range(n - 1):
        out += arrow(x0 + i * dx + 12, y - 3, x0 + (i + 1) * dx - 12, y - 3, 1) + arrow(x0 + (i + 1) * dx - 12, y + 3, x0 + i * dx + 12, y + 3, 1)
    return out

def d1(c):
    return svg(c, line_chain(), N(116, 30, "interior stops", 7), N(36, 78, "give up", 7), N(196, 78, "campus", 7),
        N(120, 100, "aᵢ = ∑ⱼ Pᵢⱼ aⱼ for i interior; aᵢ = 1 on A, 0 on B", 7.5), N(120, 112, "condition on the first step, then repeat", 7),
        N(120, 128, "aᵢ = ℙ(reach A before B | start at i)", 7.5))

def d2(c):
    return svg(c, line_chain(), N(116, 30, "each step costs one minute", 7), N(120, 98, "μᵢ = 0 on A", 7.5),
        N(120, 110, "μᵢ = 1 + ∑ⱼ∉A Pᵢⱼ μⱼ elsewhere", 7.5), N(120, 124, "⇔ (I − Q) μ = 1", 8), N(120, 138, "μᵢ = expected steps to hit A", 7))

def d3(c):
    out = R(40, 24, 110, 70, "none", 1)
    out += L(40, 59, 150, 59, .6, "3 2") + L(95, 24, 95, 94, .6, "3 2")
    return svg(c, out, N(67, 44, "Q", 9), N(122, 44, "R", 9), N(67, 80, "0", 9), N(122, 80, "I", 9),
        N(67, 18, "transient", 7), N(122, 18, "absorbing", 7), N(188, 44, "Q: transient →", 7), N(188, 54, "transient", 7), N(188, 70, "R: transient →", 7), N(188, 80, "absorbing", 7),
        N(120, 112, "N = ∑ₖ Qᵏ = (I − Q)⁻¹", 8), N(120, 126, "Nᵢⱼ = expected visits to j starting from i", 7.5))

def d4(c):
    return svg(c, nd(50, 40, "i"), nd(120, 40, "j"), nd(190, 40, "k", 11, "#d9dee7"), arrow(62, 40, 108, 40, 1), arrow(132, 40, 178, 40, 1),
        N(85, 30, "N", 7.5), N(155, 30, "R", 7.5), N(120, 14, "visits, then a jump into the trap", 7),
        N(120, 78, "B = N R:  Bᵢₖ = ℙ(absorbed in k | start at i)", 7.5), N(120, 92, "t = N 1:  tᵢ = 𝔼[time to absorption | start at i]", 7.5),
        N(120, 110, "visits to each interior stop × chance of leaving from it,", 6.5), N(120, 122, "summed over all stops", 6.5))

def d5(c):
    out = ax(24, 108, 226, 20) + N(226, 120, "start i", 7, "end") + N(28, 20, "aᵢ", 7.5, "start")
    out += L(24, 108, 226, 28, 1.1) + N(40, 56, "p = ½ : aᵢ = i/N", 7, "start")
    out += fn(lambda x: 108 - 80 * (1 - math.exp(-.02 * (x - 24))) / (1 - math.exp(-.02 * 202)), 24, 226, 40, 1.1, "4 3") + N(130, 98, "p > ½ : bends up", 7, "start")
    return svg(c, out, N(120, 12, "gambler's ruin on {0, …, N}", 7.5), N(120, 134, "μᵢ = i(N − i) expected rounds when p = ½", 7.5))

def d6(c):
    return svg(c, nd(40, 40, "∅"), nd(100, 40, "H"), nd(160, 40, "HT", 12, "#d9dee7"), arrow(52, 40, 88, 40, 1), arrow(112, 40, 148, 40, 1),
        nd(40, 100, "∅"), nd(100, 100, "H"), nd(160, 100, "HH", 12, "#d9dee7"), arrow(52, 100, 88, 100, 1), arrow(112, 100, 148, 100, 1), curve([(104, 111), (100, 124), (94, 111)], 1) if False else "",
        N(190, 38, "𝔼[T] = 4", 8, "start"), N(190, 100, "𝔼[T] = 6", 8, "start"), N(120, 128, "𝔼[T_W] = ∑ⱼ cⱼ 2ʲ, summed over self-overlaps", 7), N(120, 140, "(Conway: the overlapping pattern waits longer)", 7))

CARDS = {
32101: dict(d=d1, kind="THEOREM",
  stmt=r"<b>First-step analysis for absorption.</b> Let $A,B\subset S$ be disjoint absorbing sets and $a_i=\mathbb P_i(\text{hit }A\text{ before }B)$. Then $a_i=\sum_{j\in S}P_{ij}a_j$ for $i\notin A\cup B$, with $a_i=1$ for $i\in A$ and $a_i=0$ for $i\in B$. The minimal non-negative solution is $a_i$ (Ross 4.5; Grimmett 6.3).",
  hint="How do you find the chance of reaching campus before giving up by looking one stop ahead?",
  bd=[r"<strong>$a_i=\mathbb P_i(\text{hit }A\text{ before }B)$ = the target chance.</strong> Start at stop $i$; $a_i$ is the chance you reach campus before turning back.",
      r"<strong>$a_i=\sum_jP_{ij}a_j$ = condition on the first step.</strong> After one move you are at $j$ and the problem starts afresh from there.",
      r"<strong>$a_i=1$ on $A$, $a_i=0$ on $B$ = boundary values.</strong> Already at campus, success is certain; already home, it is impossible."],
  conn=r"<strong>Look one stop ahead.</strong> The chance of reaching campus from stop 2 is the average of the chances from the stops you may move to. Solving these linear equations gives every stop's chance at once.",
  cap="A line of stops between giving up (B) and campus (A). The chance aᵢ of reaching A first satisfies aᵢ = ∑ⱼ Pᵢⱼ aⱼ with aᵢ = 1 on A and 0 on B."),
32102: dict(d=d2, kind="THEOREM",
  stmt=r"<b>Mean hitting time.</b> Let $\mu_i=\mathbb E_i[\tau_A]$ be the expected number of steps to hit $A$. It is the minimal non-negative solution of $\mu_i=0$ for $i\in A$ and $\mu_i=1+\sum_{j\notin A}P_{ij}\mu_j$ for $i\notin A$; equivalently $(I-Q)\boldsymbol\mu=\mathbf 1$, with $Q$ the transitions among states outside $A$ (Ross 4.5; Grimmett 6.3).",
  hint="How many minutes does the trip take on average, counted one step at a time?",
  bd=[r"<strong>$\mu_i=\mathbb E_i[\tau_A]$ = the average journey time.</strong> The expected number of steps from stop $i$ until the first arrival in $A$.",
      r"<strong>$\mu_i=1+\sum_jP_{ij}\mu_j$ = pay one step, then continue.</strong> Every step costs one unit, then you are at $j$ with $\mu_j$ left to go.",
      r"<strong>$(I-Q)\boldsymbol\mu=\mathbf 1$ = the same in matrix form.</strong> $Q$ is the part of $P$ that stays outside $A$; solving gives all $\mu_i$."],
  conn=r"<strong>Counting minutes to campus.</strong> The expected time from a stop is one minute plus the average of the expected times from where you land. Solving the system gives the expected trip time from every stop.",
  cap="The same line of stops with a cost of 1 for each step. The expected time to reach campus satisfies μᵢ = 1 + ∑ⱼ Pᵢⱼ μⱼ with μ = 0 at campus."),
32103: dict(d=d3, kind="DEFINITION",
  stmt=r"<b>Canonical form and fundamental matrix.</b> Order the states with the transient ones first: $P=\begin{pmatrix}Q&R\\0&I\end{pmatrix}$. Then $P^n=\begin{pmatrix}Q^n&\ast\\0&I\end{pmatrix}$, $Q^n\to0$, and $N=\sum_{k\ge0}Q^k=(I-Q)^{-1}$, where $N_{ij}=\mathbb E_i[\text{number of visits to }j\text{ before absorption}]$ (Grimmett 6.3; Kemeny–Snell).",
  hint="How can the whole absorbing chain be packaged into one matrix that counts visits?",
  bd=[r"<strong>$Q$ and $R$ = stay or leave.</strong> $Q$ holds transitions among transient stops and $R$ those from a transient stop into an absorbing state.",
      r"<strong>$N=\sum_kQ^k$ = add up visits step by step.</strong> $(Q^k)_{ij}$ is the chance to be at $j$ at step $k$, so the sum is the expected number of visits.",
      r"<strong>$N=(I-Q)^{-1}$ = the geometric series.</strong> It converges because $Q^n\to0$: absorption eventually happens for sure."],
  conn=r"<strong>A visit counter for the route.</strong> Entry $N_{ij}$ tells you how many times, on average, you will pass stop $j$ before the trip ends if you start at stop $i$.",
  cap="Canonical form of an absorbing chain: transient block Q, exits R, absorbing identity I. The fundamental matrix N = (I − Q)⁻¹ gives expected visits Nᵢⱼ."),
32104: dict(d=d4, kind="THEOREM",
  stmt=r"<b>Absorption probabilities and lifetime.</b> With $N=(I-Q)^{-1}$, the matrix $B=NR$ has entries $B_{ik}=\mathbb P_i(\text{absorbed in state }k)$, and the vector $\mathbf t=N\mathbf 1$ has $t_i=\mathbb E_i[\tau_{\text{abs}}]$, the expected time to absorption (Grimmett 6.3; Kemeny–Snell).",
  hint="Where do you end up, and how long does it take, from the fundamental matrix alone?",
  bd=[r"<strong>$B=NR$ = visits times exit chances.</strong> Visit each transient stop $j$ $N_{ij}$ times on average, and each visit exits to $k$ with chance $R_{jk}$.",
      r"<strong>$B_{ik}=\mathbb P_i(\text{absorbed in }k)$ = the destination law.</strong> Each row of $B$ adds to one.",
      r"<strong>$\mathbf t=N\mathbf 1$ = total visits = total time.</strong> Every step is a visit to some transient state, so summing a row of $N$ counts the steps."],
  conn=r"<strong>Destination and duration.</strong> From the visit counter you read both the chance of finishing at campus rather than at home, and the expected length of the whole trip.",
  cap="From stop i, N counts visits to each transient stop j and R gives the jump into an absorbing state k. So B = NR gives destinations and t = N1 the expected trip length."),
32105: dict(d=d5, kind="WORKED EXAMPLE",
  stmt=r"<b>Gambler's ruin.</b> Win each round with prob. $p$, lose with $q=1-p$, start at $i$, stop at $0$ or $N$. Then $a_i=\mathbb P_i(\text{reach }N)=\dfrac{(q/p)^i-1}{(q/p)^N-1}$ for $p\ne q$ (equivalently $\frac{1-(q/p)^i}{1-(q/p)^N}$ for reaching $0$ with the roles swapped), and $a_i=i/N$ for $p=q=\frac12$, where $\mu_i=i(N-i)$ (Ross 4.5; Grimmett 3.9).",
  hint="With a fair or biased step each way, how likely is it to reach the far end before hitting the near one?",
  bd=[r"<strong>$p=q=\frac12$: $a_i=i/N$ = linear.</strong> The chance of reaching $N$ before $0$ is the fraction of the way you already are.",
      r"<strong>$p\ne q$: $\frac{(q/p)^i-1}{(q/p)^N-1}$ = bends with the drift.</strong> A drift towards $N$ makes the chance rise faster than linear.",
      r"<strong>$\mu_i=i(N-i)$ = expected rounds when $p=\frac12$.</strong> Longest in the middle, and zero at both ends."],
  conn=r"<strong>Reaching the far stop first.</strong> On a street of $N$ stops with a fair coin for each step, the chance of getting to the far end before the near end is just your fractional position. A tailwind bends the line upwards.",
  cap="Chance of hitting N before 0 as a function of the start i. A fair walk gives the straight line i/N; a drift bends the curve. Expected duration is i(N − i) for p = ½."),
32106: dict(d=d6, kind="WORKED EXAMPLE",
  stmt=r"<b>Pattern waiting times.</b> For fair coin tosses, $\mathbb E[T_{HT}]=4$ but $\mathbb E[T_{HH}]=6$. In general, for a pattern $W$ of length $k$, $\mathbb E[T_W]=\sum_{j=1}^kc_j2^j$ where $c_j=1$ if the first $j$ letters of $W$ equal its last $j$ letters, and $0$ otherwise (Conway; Grimmett 6.3).",
  hint="Why does waiting for two heads in a row take longer than waiting for heads then tails?",
  bd=[r"<strong>$\mathbb E[T_{HT}]=4$ = no overlap.</strong> After an H you are one toss from success; a wrong toss just restarts with a partial match.",
      r"<strong>$\mathbb E[T_{HH}]=6$ = self-overlap.</strong> After H then T you lose all progress; failing at HH costs more than failing at HT.",
      r"<strong>$\sum_jc_j2^j$ = Conway's formula.</strong> Sum $2^j$ over each prefix $j$ equal to the same-length suffix; here $HH$ gives $2+4=6$, and $HT$ gives only $4$."],
  conn=r"<strong>Waiting for a pattern of days.</strong> Waiting for two late days in a row takes longer, on average, than waiting for late then on time, because the second ‘late’ in a failed attempt can't be reused as the start of a new one.",
  cap="Two absorbing chains of partial matches: ∅ → H → HT and ∅ → H → HH. Self-overlap makes HH slower: 𝔼[T] = 6 compared with 4."),
}

STORY = {
32101: dict(s="STORY 21 · STEP 1 · REACH IT FIRST", b="<b>First-step analysis</b>: condition on the next move to get a linear system for the chance of absorption.", f=[["31902", "chances over steps"], ["30201", "conditioning"]], n=[["32102", "how long it takes"]]),
32102: dict(s="STORY 21 · STEP 2 · HOW LONG", b="<b>Mean hitting times</b> satisfy μ = 1 + Qμ: pay one step, then continue.", f=[["32101", "first-step equations"]], n=[["32103", "all at once with a matrix"]]),
32103: dict(s="STORY 21 · STEP 3 · A VISIT COUNTER", b="The <b>fundamental matrix</b> N = (I − Q)⁻¹ counts expected visits before absorption.", f=[["32102", "hitting times"]], n=[["32104", "destinations and durations"]]),
32104: dict(s="STORY 21 · STEP 4 · DESTINATION AND DURATION", b="<b>B = NR</b> gives where you end up; <b>t = N1</b> how long it takes.", f=[["32103", "fundamental matrix"]], n=[["32105", "gambler's ruin"]]),
32105: dict(s="STORY 21 · STEP 5 · THE FAIR STREET", b="<b>Gambler's ruin</b>: linear for a fair walk, bent by drift; the duration is i(N − i).", f=[["32101", "boundary equations"], ["31906", "the random walk"]], n=[["32106", "patterns"], ["32201", "birth–death chains"]]),
32106: dict(s="STORY 21 · STEP 6 · WAITING FOR A PATTERN", b="Self-overlapping patterns take <b>longer</b> to appear: Conway's formula.", f=[["32102", "mean hitting time"]], n=[["32201", "chains with a one-step ladder"]]),
}

FIX = build(CARDS)
