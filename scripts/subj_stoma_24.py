"""StoMA topic 24 (Poisson processes). F1 picture: incidents bringing out yellow flags and safety cars during a race, at random times at rate lambda per hour."""
from f1_lib import *
import random

SUBJECT = "StoMA"

def timeline(y=70, marks=(), x0=24, x1=226, col=1):
    out = L(x0, y, x1, y, 1)
    for m in marks:
        out += L(m, y - 8, m, y + 8, 1)
    return out

def d1(c):
    out = timeline(56, [44, 78, 92, 150, 186])
    return svg(c, out, N(24, 40, "0", 7), N(226, 40, "t", 7, "end"), N(120, 12, "incidents at random times in the race, rate λ", 7.5),
        N(110, 84, "ℙ(an incident in (t, t+h]) = λh + o(h)", 7), N(120, 104, "N(t) ~ Poisson(λt):  ℙ(N(t)=k) = (λt)ᵏ e^(−λt) / k!", 7.5),
        N(120, 120, "𝔼N(t) = Var N(t) = λt", 8), N(120, 136, "independent counts on disjoint intervals; no two incidents at once", 6.8))

def d2(c):
    out = timeline(56, [48, 84, 106, 160, 200])
    for a, b, lab in [(24, 48, "T₁"), (48, 84, "T₂"), (84, 106, "T₃")]:
        out += L(a + 2, 74, b - 2, 74, .8) + N((a + b) / 2, 86, lab, 7)
    out += N(106, 40, "Sₙ", 7.5)
    return svg(c, out, N(120, 12, "gaps are i.i.d. Exp(λ)", 7.5), N(120, 108, "Sₙ = T₁ + … + Tₙ ~ Gamma(n, λ)", 8), N(120, 122, "ℙ(N(t) ≥ n) = ℙ(Sₙ ≤ t)", 8), N(120, 136, "n incidents by time t ⇔ the n-th has happened by t", 7))

def d3(c):
    return svg(c, timeline(60, [44, 90, 130, 170]), L(24, 48, 24, 72, 1), L(210, 48, 210, 72, 1), N(24, 40, "0", 7), N(210, 40, "t", 7),
        N(120, 12, "given n incidents in the race [0, t]", 7.5), N(120, 92, "incident times = n sorted uniform darts on (0, t)", 7.5),
        N(120, 106, "joint density n!/tⁿ on 0 < s₁ < … < sₙ < t", 7.5), N(120, 122, "𝔼[Sₖ | N(t) = n] = k t / (n + 1)", 8), N(120, 136, "the n incidents split the race into n + 1 equal-ish gaps", 7))

def d4(c):
    return svg(c, timeline(30, [40, 70, 110, 150, 190]), N(14, 34, "A", 7, "start") if False else "", L(24, 90, 226, 90, 1), L(24, 110, 226, 110, 1),
        *[L(x, 82, x, 98, 1) for x in (40, 110, 190)], *[L(x, 102, x, 118, 1) for x in (70, 150)],
        N(120, 14, "all incidents, rate λ  (merge: λ₁ + λ₂)", 7), N(120, 78, "safety car: PP(λp)", 7), N(120, 128, "virtual SC: PP(λ(1 − p))", 7),
        N(224, 50, "split: independent", 7, "end"), N(224, 62, "Poisson streams", 7, "end"), arrow(100, 36, 100, 72, 1) if False else "")

def d5(c):
    out = ax(24, 108, 226, 20) + N(226, 120, "race time t", 7, "end") + N(28, 20, "λ(t)", 7, "start")
    out += fn(lambda x: 108 - 20 - 46 * math.exp(-((x - 80) ** 2) / 500) - 30 * math.exp(-((x - 180) ** 2) / 300), 28, 224, 60, 1.1)
    out += area(lambda x: 108 - 20 - 46 * math.exp(-((x - 80) ** 2) / 500) - 30 * math.exp(-((x - 180) ** 2) / 300), 60, 120, 108, 20)
    return svg(c, out, N(90, 119, "s", 7) if False else tick(60, 108, "s"), tick(120, 108, "s + t"), N(120, 12, "rate is high on lap 1 and late in the race", 7.5),
        N(120, 134, "m(t) = ∫₀ᵗ λ(u) du;  N(s+t) − N(s) ~ Poisson(m(s+t) − m(s))", 6.8), N(200, 56, "shaded area = mean", 7, "start") if False else N(224, 32, "shaded area", 7, "end"), N(224, 42, "= expected incidents", 7, "end"))

def d6(c):
    out = timeline(54, [30, 70, 100, 190])
    out += L(100, 40, 100, 68, 1, "3 2") if False else ""
    out += C(148, 54, 2.6, "#000000", 1) + N(148, 40, "you tune in", 7) + L(100, 78, 190, 78, 1.1) + N(145, 90, "the quiet spell you land in", 7)
    return svg(c, out, N(120, 12, "you tune in during a longer-than-average quiet spell", 7.5), N(120, 108, "𝔼[time to next W] = 1/λ,  𝔼[time since last B] → 1/λ", 7.5),
        N(120, 122, "𝔼[gap around you] → 2/λ = 2𝔼[T]", 8), N(120, 136, "long spells cover more of the race, so you land in them more", 6.8))

CARDS = {
32401: dict(d=d1, kind="DEFINITION",
  stmt=r"<b>Poisson process.</b> A counting process $N(t)$ with $N(0)=0$, independent increments, stationary increments, $\mathbb P(N(t+h)-N(t)=1)=\lambda h+o(h)$ and $\mathbb P(N(t+h)-N(t)\ge2)=o(h)$ is a Poisson process of rate $\lambda$. Then $\mathbb P(N(t)=k)=\frac{(\lambda t)^ke^{-\lambda t}}{k!}$, $\mathbb E[N(t)]=\operatorname{Var}(N(t))=\lambda t$ (Ross 5.3; Grimmett 6.8).",
  hint='If incidents happen at random during a race at a constant rate, how many come in a stretch of the race?',
  bd=[r"<strong>$\mathbb P(\text{one arrival in }h)=\lambda h+o(h)$ = rate times length.</strong> In a short stretch of racing, an incident happens with chance about $\lambda h$, and two or more at once are negligible.",
      '<strong>Independent, stationary increments = no memory.</strong> Incident counts in separate stretches of the race are independent, and depend only on how long the stretch is.',
      r"<strong>$N(t)\sim\operatorname{Poisson}(\lambda t)$ = the count.</strong> The mean and variance are both $\lambda t$, the expected number of incidents."],
  conn='<strong>Incidents at random.</strong> If races see incidents (a spin, debris, a crash) at 2 an hour at random times, the number in a 1.5-hour Grand Prix is Poisson with mean 3. Its variance is also 3, so some races are calm and some are chaos.',
  cap="Incidents on the race's time line, rate λ. In a short stretch of length h an incident has chance λh. The number of incidents in [0, t] is Poisson(λt)."),
32402: dict(d=d2, kind="THEOREM",
  stmt=r"<b>Inter-arrival and waiting times.</b> For a Poisson process of rate $\lambda$ the inter-arrival times $T_1,T_2,\ldots$ are i.i.d. $\operatorname{Exp}(\lambda)$, the $n$-th arrival time $S_n=\sum_{k=1}^nT_k\sim\operatorname{Gamma}(n,\lambda)$, and $\mathbb P(N(t)\ge n)=\mathbb P(S_n\le t)$ (Ross 5.3; Grimmett 6.8).",
  hint='How long does the race go between incidents, and how long until the n-th one?',
  bd=[r"<strong>$T_k\sim\operatorname{Exp}(\lambda)$ = memoryless gaps.</strong> Each quiet spell between incidents is exponential with mean $1/\lambda$, independently of the others.",
      r"<strong>$S_n=\sum T_k\sim\operatorname{Gamma}(n,\lambda)$ = the $n$-th incident.</strong> Its time is a sum of $n$ independent exponential gaps.",
      r"<strong>$\mathbb P(N(t)\ge n)=\mathbb P(S_n\le t)$ = two views of one event.</strong> At least $n$ incidents by time $t$ iff the $n$-th one has happened by $t$."],
  conn='<strong>Quiet spells and the n-th incident.</strong> With 2 incidents an hour the typical quiet spell is 30 minutes, and the time of the 3rd incident is the sum of three such spells. A safety car is never “due”.',
  cap="Incidents with the gaps T₁, T₂, T₃ marked. The gaps are exponential, the n-th incident time Sₙ is a sum of n of them, and 'N(t) ≥ n' is the same event as 'Sₙ ≤ t'."),
32403: dict(d=d3, kind="THEOREM",
  stmt=r"<b>Order-statistics property.</b> Given $N(t)=n$, the arrival times $(S_1,\ldots,S_n)$ have the law of the order statistics of $n$ i.i.d. $\operatorname{Unif}(0,t)$ variables: the joint density is $\frac{n!}{t^n}$ on $0<s_1<\cdots<s_n<t$, and $\mathbb E[S_k\mid N(t)=n]=\frac{k}{n+1}t$ (Ross 5.3; Grimmett 6.12).",
  hint='If you know exactly n incidents happened in the race, where in the race did they fall?',
  bd=[r"<strong>$\frac{n!}{t^n}$ = uniform on the ordered region.</strong> Given the count, the incident times are spread evenly over $(0,t)$, then put in order.",
      '<strong>Order statistics of $n$ uniforms.</strong> The incident times are just sorted independent uniform points on the race.',
      r"<strong>$\mathbb E[S_k\mid N(t)=n]=\frac k{n+1}t$ = evenly spaced on average.</strong> The $k$-th incident is expected $k/(n+1)$ of the way through the race."],
  conn='<strong>Where did the three incidents fall?</strong> If a race had exactly 3 incidents, their times are like 3 darts thrown uniformly at the race clock; on average the middle one is at half distance.',
  cap='Given N(t) = n, the n incidents are like n uniform points on (0, t), sorted. The k-th incident is on average k/(n + 1) of the way through the race.'),
32404: dict(d=d4, kind="THEOREM",
  stmt=r"<b>Superposition and thinning.</b> If $N_1,N_2$ are independent Poisson processes with rates $\lambda_1,\lambda_2$, then $N_1+N_2$ is Poisson with rate $\lambda_1+\lambda_2$ (merging). If each point of a rate-$\lambda$ Poisson process is independently kept with probability $p$, the kept points $N_1\sim\operatorname{PP}(\lambda p)$ and the rest $N_2\sim\operatorname{PP}(\lambda(1-p))$ are independent (Ross 5.3; Grimmett 6.8).",
  hint='What happens when each incident is either a full safety car or a virtual one, and when you merge two incident streams?',
  bd=[r"<strong>$N_1+N_2\sim\operatorname{PP}(\lambda_1+\lambda_2)$ = merge.</strong> Two independent Poisson streams combine into one Poisson stream whose rate is the sum.",
      r"<strong>$N_1\sim\operatorname{PP}(\lambda p)$ = thin.</strong> Keep each incident independently with chance $p$; the kept stream is Poisson with rate $\lambda p$.",
      r"<strong>$N_1\perp N_2$ = the split streams are independent.</strong> Knowing how many full safety cars came out tells you nothing about the virtual ones."],
  conn='<strong>Safety car or VSC.</strong> If incidents come at 3 an hour and each one is independently a full safety car with chance 1/3, else a virtual safety car, the safety cars form their own random stream of 1 an hour, independent of the VSC stream of 2 an hour.',
  cap='One incident stream of rate λ split by independent coin flips into safety cars at rate λp and virtual safety cars at rate λ(1 − p), which are independent. Merging reverses this.'),
32405: dict(d=d5, kind="DEFINITION",
  stmt=r"<b>Non-homogeneous Poisson process.</b> With a rate function $\lambda(t)\ge0$, let $m(t)=\int_0^t\lambda(u)\,du$. Then $N(t+s)-N(s)\sim\operatorname{Poisson}\bigl(m(t+s)-m(s)\bigr)$, and counts on disjoint intervals are independent (Ross 5.4; Grimmett 6.13).",
  hint='How do you count incidents when the rate changes during the race?',
  bd=[r"<strong>$\lambda(t)$ = the rate at time $t$.</strong> High on lap 1 when the whole field is packed together, lower in the calm middle, up again late in the race.",
      r"<strong>$m(t)=\int_0^t\lambda(u)du$ = the mean count.</strong> The expected number of incidents up to $t$ is the area under the rate curve.",
      r"<strong>$N(t+s)-N(s)\sim\operatorname{Poisson}(m(t+s)-m(s))$ = Poisson on any window.</strong> The mean over a window is the area under the rate over that window."],
  conn='<strong>Lap-one chaos.</strong> More incidents happen on the opening lap than in the middle of the race. The expected number in the first ten minutes is the area under the rate curve there, and the count is still Poisson.',
  cap='A rate curve λ(t) with a bump at the start and another late on. The expected number of incidents in a window is the shaded area m(s+t) − m(s), and the count is Poisson with that mean.'),
32406: dict(d=d6, kind="WORKED EXAMPLE",
  stmt=r"<b>Inspection paradox.</b> For a Poisson process of rate $\lambda$ and a fixed time $t$, the wait $W(t)$ to the next arrival has $\mathbb E[W(t)]=\frac1\lambda$, and the time $B(t)$ since the last one has $\mathbb E[B(t)]\to\frac1\lambda$. So the gap containing $t$ has $\mathbb E[I(t)]=\mathbb E[W+B]\to\frac2\lambda=2\mathbb E[T]$: length-biased sampling (Ross 7.7; Grimmett 10.4).",
  hint='Why does the quiet spell you tune in to tend to be longer than the average quiet spell?',
  bd=[r"<strong>$\mathbb E[W(t)]=\frac1\lambda$ = the time to the next incident.</strong> By memorylessness it is the same as the average gap.",
      r"<strong>$\mathbb E[B(t)]\to\frac1\lambda$ = the time since the last incident.</strong> Looking back from a typical moment, the time since the last one is again exponential in the long run.",
      r"<strong>$\mathbb E[I(t)]\to\frac2\lambda=2\mathbb E[T]$ = a double-length gap.</strong> Long quiet spells cover more of the race, so a random moment lands in them more often."],
  conn='<strong>Why it always looks calm when you tune in.</strong> If the average quiet spell between incidents is 30 minutes, the spell you switch on the TV in averages 60 minutes. The next incident is 30 minutes away on average, and the last one was 30 minutes ago.',
  cap='Incidents on the race clock and the moment you tune in. Long quiet spells are more likely to hold that moment: the spell around you averages 2/λ, twice the typical gap.'),
}

STORY = {
32401: dict(s='STORY 24 · STEP 1 · INCIDENTS AT RANDOM', b="A <b>Poisson process</b> counts arrivals: independent, stationary, rate λ, Poisson(λt) in [0, t].", f=[["30302", "counting laws"], ["30304", "the exponential law"]], n=[["32402", "the gaps"]]),
32402: dict(s="STORY 24 · STEP 2 · THE GAPS", b="Gaps are <b>i.i.d. exponential</b>, so the n-th arrival is Gamma(n, λ).", f=[["32401", "the process"]], n=[["32403", "where arrivals fall"]]),
32403: dict(s="STORY 24 · STEP 3 · WHERE THEY FALL", b="Given n arrivals, they are <b>uniform order statistics</b>.", f=[["32402", "gaps and arrival times"]], n=[["32404", "splitting and merging"]]),
32404: dict(s="STORY 24 · STEP 4 · SPLIT AND MERGE", b="<b>Thinning</b> gives independent Poisson streams; <b>merging</b> adds rates.", f=[["32403", "uniform positions"]], n=[["32405", "a changing rate"]]),
32405: dict(s='STORY 24 · STEP 5 · LAP-ONE CHAOS', b="A <b>non-homogeneous</b> process has mean count m(t) = area under the rate.", f=[["32401", "constant rate"], ["32404", "thinning with time-varying p"]], n=[["32406", "a surprising gap"]]),
32406: dict(s="STORY 24 · STEP 6 · THE LONGER GAP", b='The <b>inspection paradox</b>: the quiet spell you tune in to is twice the average gap.', f=[["32402", "exponential gaps"], ["31706", "long tails"]], n=[["32501", "walks"]]),
}

FIX = build(CARDS)
