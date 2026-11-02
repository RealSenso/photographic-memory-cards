"""StoMA topic 27 (continuous-time Markov chains). Commute picture: the bus is on time (1) or late (2); switches happen at random instants."""
from commute_lib import *

SUBJECT = "StoMA"

def nd(x, y, lab, r=11, fill="#ffffff"):
    return circ(x, y, r, fill, 1) + N(x, y + 3, lab, 8)

def d1(c):
    out = L(24, 46, 226, 46, 1)
    for a, b, lab in [(24, 70, "i"), (70, 130, "j"), (130, 150, "i"), (150, 226, "k")]:
        out += L(a, 36, a, 56, .8) if False else ""
        out += L(a + 2, 38, b - 2, 38, 1.1) + N((a + b) / 2, 30, lab, 7.5)
    return svg(c, out, N(120, 12, "stay in a state for an Exp(qᵢ) time, then jump", 7.5), N(120, 66, "rate of jumping i → j in h: qᵢⱼ h + o(h)", 7.5),
        N(120, 80, "Q: qᵢⱼ ≥ 0 off the diagonal, qᵢᵢ = −∑ⱼ≠ᵢ qᵢⱼ", 7.5), N(120, 94, "Q1 = 0  (each row sums to zero)", 7.5), N(120, 112, "holding time Tᵢ ~ Exp(qᵢ),  qᵢ = −qᵢᵢ", 7.5),
        N(120, 128, "next state j with chance qᵢⱼ / qᵢ", 7.5))

def d2(c):
    return svg(c, nd(50, 40, "i"), nd(120, 40, "k"), nd(190, 40, "j"), arrow(62, 40, 108, 40, 1), arrow(132, 40, 178, 40, 1),
        N(85, 30, "Q", 7.5), N(155, 30, "P(t)", 7.5), N(120, 16, "forward: P′ = P Q   (last step first)", 7),
        nd(50, 82, "i"), nd(120, 82, "k"), nd(190, 82, "j"), arrow(62, 82, 108, 82, 1), arrow(132, 82, 178, 82, 1), N(85, 72, "P(t)", 7.5), N(155, 72, "Q", 7.5),
        N(120, 62, "backward: P′ = Q P   (first step first)", 7), N(120, 118, "P(t) = e^(Qt) = ∑ₙ (Qt)ⁿ / n!", 8), N(120, 132, "semigroup: P(s + t) = P(s) P(t)", 7.5))

def d3(c):
    out = ax(24, 104, 226, 20) + N(226, 116, "t", 7, "end") + N(28, 20, "P₁₁(t)", 7, "start")
    pi = 0.65
    out += fn(lambda x: 104 - 78 * (pi + (1 - pi) * math.exp(-(x - 24) / 40)), 24, 226, 60, 1.1)
    out += L(24, 104 - 78 * pi, 226, 104 - 78 * pi, .8, "3 2") + N(224, 104 - 78 * pi - 5, "π₁ = μ/(λ+μ)", 7.5, "end")
    return svg(c, out, N(110, 40, "decays at rate λ + μ", 7, "start"), N(120, 128, "P₁₁(t) = μ/(λ+μ) + λ/(λ+μ) e^(−(λ+μ)t)", 7.5), N(120, 140, "memory of the start fades at rate λ + μ", 7))

def d4(c):
    return svg(c, nd(60, 50, "1"), nd(180, 50, "2"), arrow(72, 44, 168, 44, 1), arrow(168, 56, 72, 56, 1), N(120, 38, "π₁ q₁₂", 7.5), N(120, 72, "π₂ q₂₁", 7.5),
        N(120, 14, "flow out of a state = flow in", 7.5), N(120, 104, "global: πᵀQ = 0ᵀ, ∑ πᵢ = 1", 8), N(120, 118, "detailed: πᵢ qᵢⱼ = πⱼ qⱼᵢ ⇒ πᵀQ = 0ᵀ", 8),
        N(120, 134, "balance of rates (not chances): no uniformisation needed", 7))

def d5(c):
    out = ""
    for i in range(5):
        out += nd(34 + i * 42, 44, str(i) if i < 4 else "…", 10)
    for i in range(4):
        x1 = 34 + i * 42
        out += arrow(x1 + 11, 40, x1 + 31, 40, 1) + arrow(x1 + 31, 48, x1 + 11, 48, 1) + N(x1 + 21, 30, "λ", 7) + N(x1 + 21, 62, "μ", 7)
    return svg(c, out, N(120, 14, "n people at the stop: arrivals λ, service μ", 7.5), N(120, 88, "M/M/1, ρ = λ/μ < 1:  πₙ = (1 − ρ) ρⁿ", 8),
        N(120, 102, "𝔼[L] = ρ / (1 − ρ)", 8), N(120, 116, "W = 1 / (μ − λ)", 8), N(120, 132, "ρ → 1: both blow up", 7))

def d6(c):
    out = L(24, 50, 226, 50, 1)
    for x in (44, 66, 100, 118, 150, 190):
        out += L(x, 44, x, 56, 1)
    for x in (66, 118, 190):
        out += C(x, 50, 2.6, "#000000", 1)
    return svg(c, out, N(120, 12, "ticks at rate ν ≥ maxᵢ qᵢ (Poisson clock)", 7.5), N(120, 34, "each tick: move by K = I + Q/ν (some ticks do nothing)", 7),
        N(120, 80, "K = I + Q/ν", 8), N(120, 94, "P(t) = ∑ₙ (νt)ⁿ e^(−νt)/n!  Kⁿ", 8), N(120, 110, "a discrete chain run at Poisson(νt) clock ticks", 7), N(120, 128, "sum is a probability mixture: stable to compute", 7))

CARDS = {
32701: dict(d=d1, kind="DEFINITION",
  stmt=r"<b>Generator of a CTMC.</b> A continuous-time Markov chain on $S$ has transition functions $P_{ij}(t)$ and generator $Q$ with $q_{ij}=\lim_{h\downarrow0}\frac{P_{ij}(h)}h\ (i\ne j)$, $q_{ii}=-\sum_{j\ne i}q_{ij}$, so $Q\mathbf 1=\mathbf 0$. The holding time in $i$ is $T_i\sim\operatorname{Exp}(q_i)$, $q_i=-q_{ii}$, and the next state is $j$ with probability $q_{ij}/q_i$ (Ross 6.2; Grimmett 6.9).",
  hint="If the bus can change state at any instant, what takes the place of the one-day table?",
  bd=[r"<strong>$q_{ij}=\lim P_{ij}(h)/h$ = jump rates.</strong> In a short time $h$ the chance of moving from $i$ to $j$ is about $q_{ij}h$.",
      r"<strong>$q_{ii}=-\sum_{j\ne i}q_{ij}$ and $Q\mathbf 1=\mathbf 0$ = rows sum to zero.</strong> The diagonal is minus the total rate of leaving $i$.",
      r"<strong>$T_i\sim\operatorname{Exp}(q_i)$ = the holding time.</strong> You stay for an exponential time, then jump to $j$ with probability $q_{ij}/q_i$."],
  conn=r"<strong>Switching at random instants.</strong> The bus goes from on time to late at a rate of, say, 2 per hour. It stays on time for an exponential time with mean 30 minutes, then switches.",
  cap="A path of the chain: exponential holding times, then jumps. The generator Q holds the jump rates qᵢⱼ, and each row sums to zero."),
32702: dict(d=d2, kind="THEOREM",
  stmt=r"<b>Kolmogorov equations.</b> For a (non-explosive) CTMC with generator $Q$, $P'(t)=QP(t)$ (backward) and $P'(t)=P(t)Q$ (forward), $P(0)=I$. For a finite state space the solution is $P(t)=e^{Qt}=\sum_{n\ge0}\frac{(Qt)^n}{n!}$, and $P(s+t)=P(s)P(t)$ (Ross 6.4; Grimmett 6.9).",
  hint="How do you get the chance of being in each state at time t from the rates alone?",
  bd=[r"<strong>$P'(t)=QP(t)$ = backward equation.</strong> Condition on the first short step from the start: move by $Q$, then continue for $t$.",
      r"<strong>$P'(t)=P(t)Q$ = forward equation.</strong> Condition on the last short step: be at $k$ at time $t$, then jump to $j$ at rate $q_{kj}$.",
      r"<strong>$P(t)=e^{Qt}$ = matrix exponential.</strong> Both equations are solved by the series $\sum(Qt)^n/n!$; the semigroup property is Chapman–Kolmogorov."],
  conn=r"<strong>Rates give chances.</strong> From the table of switching rates alone, you can compute the chance that the bus is on time in exactly 20 minutes, by exponentiating the rate table times 20 minutes.",
  cap="Backward equation: first step first, P′ = QP. Forward equation: last step last, P′ = PQ. Both give P(t) = e^(Qt), with P(s + t) = P(s)P(t)."),
32703: dict(d=d3, kind="WORKED EXAMPLE",
  stmt=r"<b>Two-state chain.</b> States $1\to2$ at rate $\lambda$ and $2\to1$ at rate $\mu$. Then $P_{11}(t)=\dfrac\mu{\lambda+\mu}+\dfrac\lambda{\lambda+\mu}e^{-(\lambda+\mu)t}$, and $\lim_{t\to\infty}P_{11}(t)=\pi_1=\frac\mu{\lambda+\mu}$. The memory of the start decays at rate $\lambda+\mu$ (Ross 6.4; Grimmett 6.9).",
  hint="How quickly does a bus that starts on time forget that it started on time?",
  bd=[r"<strong>$\pi_1=\frac\mu{\lambda+\mu}$ = the long-run share in state 1.</strong> Time in 1 is proportional to $1/\lambda$, in 2 to $1/\mu$; the share is $\mu/(\lambda+\mu)$.",
      r"<strong>$\frac\lambda{\lambda+\mu}e^{-(\lambda+\mu)t}$ = the transient.</strong> The extra chance of still being in 1 because you started there, which decays exponentially.",
      r"<strong>$\lambda+\mu$ = the relaxation rate.</strong> The chain forgets its start on a time scale $1/(\lambda+\mu)$."],
  conn=r"<strong>Forgetting the start.</strong> If the bus goes late at 2 per hour and recovers at 4 per hour, a bus that began on time is on time with chance close to $\frac23$ after about 10 minutes, whatever the start.",
  cap="P₁₁(t) starts at 1 and decays exponentially, at rate λ + μ, to its limit π₁ = μ/(λ + μ), the long-run share of time in state 1."),
32704: dict(d=d4, kind="THEOREM",
  stmt=r"<b>Stationary distribution of a CTMC.</b> A probability vector $\pi$ is stationary if $\pi^\top Q=\mathbf 0^\top$ (global balance), $\sum_i\pi_i=1$, equivalently $\pi^\top P(t)=\pi^\top$ for all $t$. If $\pi_iq_{ij}=\pi_jq_{ji}$ for all $i,j$ (detailed balance), then $\pi^\top Q=\mathbf 0^\top$ (Ross 6.5; Grimmett 6.9).",
  hint="Which split of time between states is unchanged by the switching?",
  bd=[r"<strong>$\pi^\top Q=\mathbf 0^\top$ = global balance.</strong> For each state, the rate of flow in, $\sum_i\pi_iq_{ij}$, equals the rate of flow out, $\pi_jq_j$.",
      r"<strong>$\sum_i\pi_i=1$ = a split of time.</strong> $\pi_i$ is the long-run fraction of time in state $i$.",
      r"<strong>$\pi_iq_{ij}=\pi_jq_{ji}$ = detailed balance.</strong> If every pair of states balances individually, summing over $i$ gives global balance."],
  conn=r"<strong>Balance the rates.</strong> If the bus is on time for $\frac23$ of the time and goes late at rate 2, while being late for $\frac13$ of the time and recovering at rate 4, both flows are $\frac43$ an hour: balanced.",
  cap="Flow between two states: rate out of 1 is π₁q₁₂ and rate into 1 is π₂q₂₁. At the stationary law they are equal, which is detailed balance."),
32705: dict(d=d5, kind="WORKED EXAMPLE",
  stmt=r"<b>M/M/1 queue.</b> Arrivals at rate $\lambda$, service at rate $\mu$, one server; $\rho=\lambda/\mu<1$. The number in system is a birth–death chain with $\pi_n=(1-\rho)\rho^n$, mean $\mathbb E[L]=\frac\rho{1-\rho}$ and mean time in system $W=\frac1{\mu-\lambda}$ (Little's law $L=\lambda W$). For M/M/c, $\rho=\frac\lambda{c\mu}<1$ (Ross 8.3; Grimmett 11.2).",
  hint="How long is the queue at the stop in the long run, and how long do you wait?",
  bd=[r"<strong>$\pi_n=(1-\rho)\rho^n$ = geometric queue length.</strong> Detailed balance $\pi_n\lambda=\pi_{n+1}\mu$ gives a geometric law, normalised by $1-\rho$.",
      r"<strong>$\mathbb E[L]=\frac\rho{1-\rho}$ = the mean queue.</strong> The mean of the geometric law; it blows up as $\rho\to1$.",
      r"<strong>$W=\frac1{\mu-\lambda}$ = the mean time in system.</strong> By Little's law $W=\mathbb E[L]/\lambda$; it also blows up as $\mu-\lambda\to0$."],
  conn=r"<strong>Why the stop clogs.</strong> If buses clear people at 6 an hour and 5 arrive an hour, the mean queue is 5 people and the mean time in the system is 1 hour. At 5.9 arrivals an hour, the queue is 59.",
  cap="Queue-length ladder with arrivals at rate λ and service at rate μ. For ρ = λ/μ < 1 the long-run length is geometric, mean ρ/(1 − ρ), and it explodes as ρ → 1."),
32706: dict(d=d6, kind="THEOREM",
  stmt=r"<b>Uniformization (Jensen).</b> Pick $\nu\ge\max_iq_i$ and let $K=I+\frac1\nu Q$, a stochastic matrix. Then $P(t)=\sum_{n\ge0}\frac{(\nu t)^ne^{-\nu t}}{n!}K^n$: the chain is a discrete chain with transition matrix $K$ observed at the ticks of a rate-$\nu$ Poisson clock (Ross 6.7; Grimmett 6.9).",
  hint="Can a continuous-time chain be run as a discrete one, on the ticks of a clock?",
  bd=[r"<strong>$K=I+Q/\nu$ = a one-tick transition matrix.</strong> With $\nu\ge\max_iq_i$ all entries are in $[0,1]$ and rows add to 1; some ticks leave you in place.",
      r"<strong>$\frac{(\nu t)^ne^{-\nu t}}{n!}$ = the number of ticks.</strong> By time $t$ a rate-$\nu$ Poisson clock has ticked $n$ times with this probability.",
      r"<strong>$P(t)=\sum_n\ldots K^n$ = a mixture.</strong> Weight the $n$-step matrices by the Poisson tick probabilities: a stable way to compute $e^{Qt}$."],
  conn=r"<strong>A clock ticks, the chain may move.</strong> Fix a fast clock that ticks at least as often as any switch could happen. At each tick, the bus switches with the right small chance, or stays as it is.",
  cap="A Poisson clock ticks at rate ν. At each tick the chain moves by K = I + Q/ν (some ticks leave it in place). So P(t) is a Poisson mixture of the matrix powers Kⁿ."),
}

STORY = {
32701: dict(s="STORY 27 · STEP 1 · RATES NOT CHANCES", b="The <b>generator Q</b> holds jump rates; holding times are exponential.", f=[["31901", "the discrete chain"], ["32402", "exponential gaps"]], n=[["32702", "chances from rates"]]),
32702: dict(s="STORY 27 · STEP 2 · CHANCES FROM RATES", b="<b>Kolmogorov's equations</b> give P(t) = e^(Qt).", f=[["32701", "generator"], ["31902", "Chapman–Kolmogorov"]], n=[["32703", "a worked case"], ["32706", "computing it"]]),
32703: dict(s="STORY 27 · STEP 3 · TWO STATES", b="A two-state chain <b>forgets its start</b> at rate λ + μ.", f=[["32702", "matrix exponential"]], n=[["32704", "the long-run split"]]),
32704: dict(s="STORY 27 · STEP 4 · BALANCE OF RATES", b="The stationary law solves <b>πQ = 0</b>; detailed balance is a sufficient shortcut.", f=[["32703", "limit π₁"], ["32001", "stationary law, discrete time"]], n=[["32705", "queues"]]),
32705: dict(s="STORY 27 · STEP 5 · THE QUEUE", b="The <b>M/M/1 queue</b> is geometric with mean ρ/(1 − ρ).", f=[["32704", "balance"], ["32202", "birth–death chains"]], n=[["32706", "simulation by clock"]]),
32706: dict(s="STORY 27 · STEP 6 · A CLOCK AND A CHAIN", b="<b>Uniformization</b>: run a discrete chain on Poisson clock ticks.", f=[["32702", "e^(Qt)"], ["32401", "Poisson process"]], n=[]),
}

FIX = build(CARDS)
