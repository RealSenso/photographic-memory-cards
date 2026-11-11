"""StoMA topic 21 (absorption). F1 picture: a chase. Each lap the gap from Max to the car ahead shrinks or grows by one step until he overtakes (A) or falls out of DRS range and gives up (B); both ends are absorbing. Pattern waiting times stay coin-based, framed as laps quicker or slower than the last."""
from f1_lib import *

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
    return svg(c, line_chain(), N(116, 30, "gap states", 7), N(36, 78, "out of DRS", 7), N(196, 78, "overtake", 7),
        N(120, 100, "aᵢ = ∑ⱼ Pᵢⱼ aⱼ for i interior; aᵢ = 1 on A, 0 on B", 7.5), N(120, 112, "condition on the first step, then repeat", 7),
        N(120, 128, "aᵢ = ℙ(reach A before B | start at i)", 7.5))

def d2(c):
    return svg(c, line_chain(), N(116, 30, "each step costs one lap", 7), N(120, 98, "μᵢ = 0 on A", 7.5),
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
        N(120, 110, "visits to each gap state × chance of leaving from it,", 6.5), N(120, 122, "summed over all gap states", 6.5))

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
  hint='How do you find the chance that Max overtakes before he drops out of DRS range, by looking one lap ahead?',
  bd=[r"<strong>$a_i=\mathbb P_i(\text{hit }A\text{ before }B)$ = the target chance.</strong> Start in gap state $i$; $a_i$ is the chance he overtakes before he falls back and gives up.",
      r"<strong>$a_i=\sum_jP_{ij}a_j$ = condition on the first step.</strong> After one lap he is in gap state $j$ and the problem starts again from there.",
      '<strong>$a_i=1$ on $A$, $a_i=0$ on $B$ = boundary values.</strong> Already past, success is certain; already out of DRS range, it is impossible.'],
  conn="<strong>Look one lap ahead.</strong> The chance of getting past from gap state 2 is the average of the chances from the states he can be in after one more lap. Solving these linear equations gives every gap state's chance at once.",
  cap='A line of gap states between dropping out of DRS range (B) and the overtake (A). The chance aᵢ of reaching A first satisfies aᵢ = ∑ⱼ Pᵢⱼ aⱼ with aᵢ = 1 on A and 0 on B.'),
32102: dict(d=d2, kind="THEOREM",
  stmt=r"<b>Mean hitting time.</b> Let $\mu_i=\mathbb E_i[\tau_A]$ be the expected number of steps to hit $A$. It is the minimal non-negative solution of $\mu_i=0$ for $i\in A$ and $\mu_i=1+\sum_{j\notin A}P_{ij}\mu_j$ for $i\notin A$; equivalently $(I-Q)\boldsymbol\mu=\mathbf 1$, with $Q$ the transitions among states outside $A$ (Ross 4.5; Grimmett 6.3).",
  hint='How many laps does the chase last on average, counted one lap at a time?',
  bd=[r"<strong>$\mu_i=\mathbb E_i[\tau_A]$ = the average chase length.</strong> The expected number of steps from gap state $i$ until the first arrival in $A$.",
      r"<strong>$\mu_i=1+\sum_jP_{ij}\mu_j$ = pay one step, then continue.</strong> Every lap costs one unit, then he is in state $j$ with $\mu_j$ still to go.",
      r"<strong>$(I-Q)\boldsymbol\mu=\mathbf 1$ = the same in matrix form.</strong> $Q$ is the part of $P$ that stays outside $A$; solving gives all $\mu_i$."],
  conn='<strong>Counting laps to the overtake.</strong> The expected number of laps from a gap state is one lap plus the average of the expected laps from wherever he is next. Solving the system gives the mean number of laps to overtake from every gap.',
  cap='The same line of gap states with a cost of 1 lap for each step. The expected number of laps to the overtake satisfies μᵢ = 1 + ∑ⱼ Pᵢⱼ μⱼ with μ = 0 once he is past.'),
32103: dict(d=d3, kind="DEFINITION",
  stmt=r"<b>Canonical form and fundamental matrix.</b> Order the states with the transient ones first: $P=\begin{pmatrix}Q&R\\0&I\end{pmatrix}$. Then $P^n=\begin{pmatrix}Q^n&\ast\\0&I\end{pmatrix}$, $Q^n\to0$, and $N=\sum_{k\ge0}Q^k=(I-Q)^{-1}$, where $N_{ij}=\mathbb E_i[\text{number of visits to }j\text{ before absorption}]$ (Grimmett 6.3; Kemeny–Snell).",
  hint='How can the whole chase be packed into one matrix that counts visits to each gap?',
  bd=['<strong>$Q$ and $R$ = stay or leave.</strong> $Q$ holds the moves between gap states and $R$ the moves from a gap state into an absorbing end.',
      r"<strong>$N=\sum_kQ^k$ = add up visits step by step.</strong> $(Q^k)_{ij}$ is the chance to be at $j$ after $k$ steps, so the sum is the expected number of visits.",
      r"<strong>$N=(I-Q)^{-1}$ = the geometric series.</strong> It converges because $Q^n\to0$: the chase ends for sure."],
  conn='<strong>A lap counter for each gap.</strong> Entry $N_{ij}$ tells you how many laps, on average, Max spends at gap $j$ before the chase ends, if it starts at gap $i$.',
  cap='Canonical form of an absorbing chain: block Q for moves between gap states, exits R, and the identity I for the ends. The fundamental matrix N = (I − Q)⁻¹ gives the expected visits Nᵢⱼ.'),
32104: dict(d=d4, kind="THEOREM",
  stmt=r"<b>Absorption probabilities and lifetime.</b> With $N=(I-Q)^{-1}$, the matrix $B=NR$ has entries $B_{ik}=\mathbb P_i(\text{absorbed in state }k)$, and the vector $\mathbf t=N\mathbf 1$ has $t_i=\mathbb E_i[\tau_{\text{abs}}]$, the expected time to absorption (Grimmett 6.3; Kemeny–Snell).",
  hint='How does the lap counter alone tell you how the chase ends, and how long it takes?',
  bd=['<strong>$B=NR$ = visits times exit chances.</strong> He visits each gap state $j$ $N_{ij}$ times on average, and each visit exits to $k$ with chance $R_{jk}$.',
      r"<strong>$B_{ik}=\mathbb P_i(\text{absorbed in }k)$ = the destination law.</strong> Each row of $B$ adds to one.",
      r"<strong>$\mathbf t=N\mathbf 1$ = total visits = total time.</strong> Every step is a visit to some transient state, so adding up a row of $N$ counts the steps."],
  conn='<strong>How it ends and how long.</strong> From the lap counter you read both the chance that the chase ends in an overtake rather than a give-up, and the expected number of laps the whole chase lasts.',
  cap='From gap i, N counts the visits to each gap state j and R gives the jump into an end k. So B = NR gives how the chase ends and t = N1 how many laps it lasts on average.'),
32105: dict(d=d5, kind="WORKED EXAMPLE",
  stmt=r"<b>Gambler's ruin.</b> Win each round with prob. $p$, lose with $q=1-p$, start at $i$, stop at $0$ or $N$. Then $a_i=\mathbb P_i(\text{reach }N)=\dfrac{(q/p)^i-1}{(q/p)^N-1}$ for $p\ne q$ (equivalently $\frac{1-(q/p)^i}{1-(q/p)^N}$ for reaching $0$ with the roles swapped), and $a_i=i/N$ for $p=q=\frac12$, where $\mu_i=i(N-i)$ (Ross 4.5; Grimmett 3.9).",
  hint='With a fair or a biased step each lap, how likely is Max to reach the far end before the near one?',
  bd=[r"<strong>$p=q=\frac12$: $a_i=i/N$ = linear.</strong> The chance of reaching $N$ before $0$ is the fraction of the way he already is.",
      r"<strong>$p\ne q$: $\frac{(q/p)^i-1}{(q/p)^N-1}$ = bends with the drift.</strong> A drift towards $N$ makes the chance rise faster than linear.",
      r"<strong>$\mu_i=i(N-i)$ = expected rounds when $p=\frac12$.</strong> Longest in the middle, and zero at both ends."],
  conn=r"<strong>The faster car.</strong> In the chase with $N$ steps, if Max gains or loses a step on each lap with equal chance, his chance of getting past is just how far along he already is. If his car is faster ($p>\frac12$), the line bends upwards: even from far back he usually gets there.",
  cap='Chance of hitting N before 0 against the start i. Equal cars give the straight line i/N; a faster car (p > ½) bends the curve up. The expected length is i(N − i) laps for p = ½.'),
32106: dict(d=d6, kind="WORKED EXAMPLE",
  stmt=r"<b>Pattern waiting times.</b> For fair coin tosses, $\mathbb E[T_{HT}]=4$ but $\mathbb E[T_{HH}]=6$. In general, for a pattern $W$ of length $k$, $\mathbb E[T_W]=\sum_{j=1}^kc_j2^j$ where $c_j=1$ if the first $j$ letters of $W$ equal its last $j$ letters, and $0$ otherwise (Conway; Grimmett 6.3).",
  hint='Why does waiting for two quicker laps in a row take longer than waiting for a quicker lap then a slower one?',
  bd=[r"<strong>$\mathbb E[T_{HT}]=4$ = no overlap.</strong> After an H you are one lap from success; a wrong lap just restarts with a partial match.",
      r"<strong>$\mathbb E[T_{HH}]=6$ = self-overlap.</strong> After H then T you lose all progress; failing at HH costs more than failing at HT.",
      r"<strong>$\sum_jc_j2^j$ = Conway's formula.</strong> Add $2^j$ over each start $j$ that equals the end of the same length; here $HH$ gives $2+4=6$, and $HT$ gives only $4$."],
  conn='<strong>Waiting for a pattern of laps.</strong> Say each lap is a fair coin: quicker than the lap before (H) or not (T). The strategist waits for a pattern before calling Max in. Two quicker laps in a row take 6 laps on average, but quicker then slower only 4. Chasing H H, a slower lap after an H throws away all progress; chasing H T, another quicker lap still leaves you one lap from done.',
  cap='Two absorbing chains of partial matches: ∅ → H → HT and ∅ → H → HH, with H a lap quicker than the last. Self-overlap makes HH slower: 𝔼[T] = 6 laps compared with 4.'),
}

STORY = {
32101: dict(s="STORY 21 · STEP 1 · REACH IT FIRST", b='<b>First-step analysis</b>: condition on the next lap to get a linear system for the chance of absorption.', f=[["31902", "chances over steps"], ["30201", "conditioning"]], n=[["32102", "how long it takes"]]),
32102: dict(s="STORY 21 · STEP 2 · HOW LONG", b="<b>Mean hitting times</b> satisfy μ = 1 + Qμ: pay one step, then continue.", f=[["32101", "first-step equations"]], n=[["32103", "all at once with a matrix"]]),
32103: dict(s="STORY 21 · STEP 3 · A VISIT COUNTER", b="The <b>fundamental matrix</b> N = (I − Q)⁻¹ counts expected visits before absorption.", f=[["32102", "hitting times"]], n=[["32104", "destinations and durations"]]),
32104: dict(s="STORY 21 · STEP 4 · DESTINATION AND DURATION", b="<b>B = NR</b> gives where you end up; <b>t = N1</b> how long it takes.", f=[["32103", "fundamental matrix"]], n=[["32105", "gambler's ruin"]]),
32105: dict(s='STORY 21 · STEP 5 · THE FASTER CAR', b="<b>Gambler's ruin</b>: linear for equal cars, bent by drift; the duration is i(N − i).", f=[["32101", "boundary equations"], ["31906", "the random walk"]], n=[["32106", "patterns"], ["32201", "birth–death chains"]]),
32106: dict(s="STORY 21 · STEP 6 · WAITING FOR A PATTERN", b="Self-overlapping patterns take <b>longer</b> to appear: Conway's formula.", f=[["32102", "mean hitting time"]], n=[["32201", "chains with a one-step ladder"]]),
}

FIX = build(CARDS)
