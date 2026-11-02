"""StoMA topic 24 (Poisson processes). Commute picture: buses arriving at the stop at random times, rate lambda per hour."""
from commute_lib import *
import random

SUBJECT = "StoMA"

def timeline(y=70, marks=(), x0=24, x1=226, col=1):
    out = L(x0, y, x1, y, 1)
    for m in marks:
        out += L(m, y - 8, m, y + 8, 1)
    return out

def d1(c):
    out = timeline(56, [44, 78, 92, 150, 186])
    return svg(c, out, N(24, 40, "0", 7), N(226, 40, "t", 7, "end"), N(120, 12, "buses arriving at random times at rate λ", 7.5),
        N(110, 84, "ℙ(a bus in (t, t+h]) = λh + o(h)", 7), N(120, 104, "N(t) ~ Poisson(λt):  ℙ(N(t)=k) = (λt)ᵏ e^(−λt) / k!", 7.5),
        N(120, 120, "𝔼N(t) = Var N(t) = λt", 8), N(120, 136, "independent counts on disjoint intervals; no two buses at once", 6.8))

def d2(c):
    out = timeline(56, [48, 84, 106, 160, 200])
    for a, b, lab in [(24, 48, "T₁"), (48, 84, "T₂"), (84, 106, "T₃")]:
        out += L(a + 2, 74, b - 2, 74, .8) + N((a + b) / 2, 86, lab, 7)
    out += N(106, 40, "Sₙ", 7.5)
    return svg(c, out, N(120, 12, "gaps are i.i.d. Exp(λ)", 7.5), N(120, 108, "Sₙ = T₁ + … + Tₙ ~ Gamma(n, λ)", 8), N(120, 122, "ℙ(N(t) ≥ n) = ℙ(Sₙ ≤ t)", 8), N(120, 136, "n buses by time t ⇔ the n-th bus has arrived by t", 7))

def d3(c):
    return svg(c, timeline(60, [44, 90, 130, 170]), L(24, 48, 24, 72, 1), L(210, 48, 210, 72, 1), N(24, 40, "0", 7), N(210, 40, "t", 7),
        N(120, 12, "given n buses in [0, t]", 7.5), N(120, 92, "arrival times = n sorted uniform draws on (0, t)", 7.5),
        N(120, 106, "joint density n!/tⁿ on 0 < s₁ < … < sₙ < t", 7.5), N(120, 122, "𝔼[Sₖ | N(t) = n] = k t / (n + 1)", 8), N(120, 136, "the n buses split the hour into n + 1 equal-ish gaps", 7))

def d4(c):
    return svg(c, timeline(30, [40, 70, 110, 150, 190]), N(14, 34, "A", 7, "start") if False else "", L(24, 90, 226, 90, 1), L(24, 110, 226, 110, 1),
        *[L(x, 82, x, 98, 1) for x in (40, 110, 190)], *[L(x, 102, x, 118, 1) for x in (70, 150)],
        N(120, 14, "all buses, rate λ  (merge: λ₁ + λ₂)", 7), N(120, 78, "route 1: PP(λp)", 7), N(120, 128, "route 2: PP(λ(1 − p))", 7),
        N(224, 50, "split: independent", 7, "end"), N(224, 62, "Poisson streams", 7, "end"), arrow(100, 36, 100, 72, 1) if False else "")

def d5(c):
    out = ax(24, 108, 226, 20) + N(226, 120, "time of day t", 7, "end") + N(28, 20, "λ(t)", 7, "start")
    out += fn(lambda x: 108 - 20 - 46 * math.exp(-((x - 80) ** 2) / 500) - 30 * math.exp(-((x - 180) ** 2) / 300), 28, 224, 60, 1.1)
    out += area(lambda x: 108 - 20 - 46 * math.exp(-((x - 80) ** 2) / 500) - 30 * math.exp(-((x - 180) ** 2) / 300), 60, 120, 108, 20)
    return svg(c, out, N(90, 119, "s", 7) if False else tick(60, 108, "s"), tick(120, 108, "s + t"), N(120, 12, "rate varies through the morning", 7.5),
        N(120, 134, "m(t) = ∫₀ᵗ λ(u) du;  N(s+t) − N(s) ~ Poisson(m(s+t) − m(s))", 6.8), N(200, 56, "shaded area = mean", 7, "start") if False else N(224, 32, "shaded area", 7, "end"), N(224, 42, "= expected buses", 7, "end"))

def d6(c):
    out = timeline(54, [30, 70, 100, 190])
    out += L(100, 40, 100, 68, 1, "3 2") if False else ""
    out += C(148, 54, 2.6, "#000000", 1) + N(148, 40, "you arrive", 7) + L(100, 78, 190, 78, 1.1) + N(145, 90, "the gap that holds you", 7)
    return svg(c, out, N(120, 12, "you land in a longer-than-average gap", 7.5), N(120, 108, "𝔼[wait W] = 1/λ,  𝔼[time since last B] → 1/λ", 7.5),
        N(120, 122, "𝔼[gap around you] → 2/λ = 2𝔼[T]", 8), N(120, 136, "long gaps cover more of the clock, so you land in them more", 6.8))

CARDS = {
32401: dict(d=d1, kind="DEFINITION",
  stmt=r"<b>Poisson process.</b> A counting process $N(t)$ with $N(0)=0$, independent increments, stationary increments, $\mathbb P(N(t+h)-N(t)=1)=\lambda h+o(h)$ and $\mathbb P(N(t+h)-N(t)\ge2)=o(h)$ is a Poisson process of rate $\lambda$. Then $\mathbb P(N(t)=k)=\frac{(\lambda t)^ke^{-\lambda t}}{k!}$, $\mathbb E[N(t)]=\operatorname{Var}(N(t))=\lambda t$ (Ross 5.3; Grimmett 6.8).",
  hint="If buses arrive at random with a constant rate, how many come in a stretch of time?",
  bd=[r"<strong>$\mathbb P(\text{one arrival in }h)=\lambda h+o(h)$ = rate times length.</strong> In a short interval, a bus comes with chance about $\lambda h$ and two or more are negligible.",
      r"<strong>Independent, stationary increments = no memory.</strong> Counts on disjoint intervals are independent, and depend only on the length of the interval.",
      r"<strong>$N(t)\sim\operatorname{Poisson}(\lambda t)$ = the count.</strong> The mean and variance are both $\lambda t$, the expected number of arrivals."],
  conn=r"<strong>Buses at random.</strong> If a stop gets 6 buses an hour at random times, the number in the next 30 minutes is Poisson with mean 3. Its spread is also 3: the count is quite uneven.",
  cap="Arrivals on a time line, rate λ. In a short interval of length h an arrival has chance λh. The number of arrivals in [0, t] is Poisson(λt)."),
32402: dict(d=d2, kind="THEOREM",
  stmt=r"<b>Inter-arrival and waiting times.</b> For a Poisson process of rate $\lambda$ the inter-arrival times $T_1,T_2,\ldots$ are i.i.d. $\operatorname{Exp}(\lambda)$, the $n$-th arrival time $S_n=\sum_{k=1}^nT_k\sim\operatorname{Gamma}(n,\lambda)$, and $\mathbb P(N(t)\ge n)=\mathbb P(S_n\le t)$ (Ross 5.3; Grimmett 6.8).",
  hint="How long do you wait between buses, and how long until the n-th one?",
  bd=[r"<strong>$T_k\sim\operatorname{Exp}(\lambda)$ = memoryless gaps.</strong> Each gap between consecutive buses is exponential with mean $1/\lambda$, independently of the others.",
      r"<strong>$S_n=\sum T_k\sim\operatorname{Gamma}(n,\lambda)$ = the $n$-th arrival.</strong> A sum of $n$ independent exponential gaps.",
      r"<strong>$\mathbb P(N(t)\ge n)=\mathbb P(S_n\le t)$ = two views of one event.</strong> At least $n$ buses by time $t$ iff the $n$-th has come by $t$."],
  conn=r"<strong>Gaps and the n-th bus.</strong> With 6 buses an hour the typical gap is 10 minutes, and the wait for the 3rd bus is the sum of three such gaps.",
  cap="Arrivals with the gaps T₁, T₂, T₃ marked. The gaps are exponential, the n-th arrival Sₙ is a sum of n of them, and 'N(t) ≥ n' is the same event as 'Sₙ ≤ t'."),
32403: dict(d=d3, kind="THEOREM",
  stmt=r"<b>Order-statistics property.</b> Given $N(t)=n$, the arrival times $(S_1,\ldots,S_n)$ have the law of the order statistics of $n$ i.i.d. $\operatorname{Unif}(0,t)$ variables: the joint density is $\frac{n!}{t^n}$ on $0<s_1<\cdots<s_n<t$, and $\mathbb E[S_k\mid N(t)=n]=\frac{k}{n+1}t$ (Ross 5.3; Grimmett 6.12).",
  hint="If you know exactly n buses came in the hour, where in the hour did they fall?",
  bd=[r"<strong>$\frac{n!}{t^n}$ = uniform on the ordered region.</strong> Given the count, the times are exchangeable and spread evenly over $(0,t)$, then sorted.",
      r"<strong>Order statistics of $n$ uniforms.</strong> The arrival times are just sorted independent uniform points.",
      r"<strong>$\mathbb E[S_k\mid N(t)=n]=\frac k{n+1}t$ = evenly spaced on average.</strong> The $k$-th arrival is expected $k/(n+1)$ of the way through."],
  conn=r"<strong>Where did the three buses fall?</strong> If exactly 3 buses came in an hour, they are like 3 darts thrown uniformly at the hour; on average the middle one is at 30 minutes.",
  cap="Given N(t) = n, the n arrivals are like n uniform points on (0, t), sorted. The k-th arrival is on average k/(n + 1) of the way through."),
32404: dict(d=d4, kind="THEOREM",
  stmt=r"<b>Superposition and thinning.</b> If $N_1,N_2$ are independent Poisson processes with rates $\lambda_1,\lambda_2$, then $N_1+N_2$ is Poisson with rate $\lambda_1+\lambda_2$ (merging). If each point of a rate-$\lambda$ Poisson process is independently kept with probability $p$, the kept points $N_1\sim\operatorname{PP}(\lambda p)$ and the rest $N_2\sim\operatorname{PP}(\lambda(1-p))$ are independent (Ross 5.3; Grimmett 6.8).",
  hint="What happens when two bus streams merge, or when one stream is split among two routes?",
  bd=[r"<strong>$N_1+N_2\sim\operatorname{PP}(\lambda_1+\lambda_2)$ = merge.</strong> Two independent Poisson streams combine into one Poisson stream whose rate is the sum.",
      r"<strong>$N_1\sim\operatorname{PP}(\lambda p)$ = thin.</strong> Keep each arrival independently with chance $p$; the kept stream is Poisson with rate $\lambda p$.",
      r"<strong>$N_1\perp N_2$ = the split streams are independent.</strong> Knowing how many buses took route 1 tells you nothing about route 2."],
  conn=r"<strong>Routes of one line.</strong> If 6 buses an hour are each independently route A with chance 1/3, route A buses form their own random stream of 2 an hour, independent of the route B stream of 4.",
  cap="One stream of rate λ split by independent coin flips into route 1 with rate λp and route 2 with rate λ(1 − p), which are independent. Merging reverses this."),
32405: dict(d=d5, kind="DEFINITION",
  stmt=r"<b>Non-homogeneous Poisson process.</b> With a rate function $\lambda(t)\ge0$, let $m(t)=\int_0^t\lambda(u)\,du$. Then $N(t+s)-N(s)\sim\operatorname{Poisson}\bigl(m(t+s)-m(s)\bigr)$, and counts on disjoint intervals are independent (Ross 5.4; Grimmett 6.13).",
  hint="How do you count arrivals when the rate changes through the morning?",
  bd=[r"<strong>$\lambda(t)$ = the rate at time $t$.</strong> Higher in the rush hour, lower off-peak.",
      r"<strong>$m(t)=\int_0^t\lambda(u)du$ = the mean count.</strong> The expected number of arrivals up to $t$ is the area under the rate curve.",
      r"<strong>$N(t+s)-N(s)\sim\operatorname{Poisson}(m(t+s)-m(s))$ = Poisson on any window.</strong> The mean over a window is the area under the rate over that window."],
  conn=r"<strong>Rush hour.</strong> More buses come at 8am than at 10am. The expected number in the window 8:00–8:30 is the area under the rate curve there, and the count is still Poisson.",
  cap="A rate curve λ(t) with a rush-hour bump. The expected number of arrivals in a window is the shaded area m(s+t) − m(s), and the count is Poisson with that mean."),
32406: dict(d=d6, kind="WORKED EXAMPLE",
  stmt=r"<b>Inspection paradox.</b> For a Poisson process of rate $\lambda$ and a fixed time $t$, the wait $W(t)$ to the next arrival has $\mathbb E[W(t)]=\frac1\lambda$, and the time $B(t)$ since the last one has $\mathbb E[B(t)]\to\frac1\lambda$. So the gap containing $t$ has $\mathbb E[I(t)]=\mathbb E[W+B]\to\frac2\lambda=2\mathbb E[T]$: length-biased sampling (Ross 7.7; Grimmett 10.4).",
  hint="Why does the gap you happen to arrive in tend to be longer than the average gap?",
  bd=[r"<strong>$\mathbb E[W(t)]=\frac1\lambda$ = the wait for the next bus.</strong> By memorylessness it is the same as the average gap.",
      r"<strong>$\mathbb E[B(t)]\to\frac1\lambda$ = the time since the last bus.</strong> Looking backwards from a typical time, the age is again exponential in the long run.",
      r"<strong>$\mathbb E[I(t)]\to\frac2\lambda=2\mathbb E[T]$ = a double-length gap.</strong> Long gaps cover more of the clock, so a random arrival time lands in them more often."],
  conn=r"<strong>Why you always wait.</strong> If the average gap between buses is 10 minutes, the gap you walk into averages 20 minutes. You wait 10 minutes on average, and your last bus left 10 minutes ago.",
  cap="Buses on a time line and your arrival time inside a gap. Long gaps are more likely to hold your arrival: the gap around you averages 2/λ, twice the typical gap."),
}

STORY = {
32401: dict(s="STORY 24 · STEP 1 · BUSES AT RANDOM", b="A <b>Poisson process</b> counts arrivals: independent, stationary, rate λ, Poisson(λt) in [0, t].", f=[["30302", "counting laws"], ["30304", "the exponential law"]], n=[["32402", "the gaps"]]),
32402: dict(s="STORY 24 · STEP 2 · THE GAPS", b="Gaps are <b>i.i.d. exponential</b>, so the n-th arrival is Gamma(n, λ).", f=[["32401", "the process"]], n=[["32403", "where arrivals fall"]]),
32403: dict(s="STORY 24 · STEP 3 · WHERE THEY FALL", b="Given n arrivals, they are <b>uniform order statistics</b>.", f=[["32402", "gaps and arrival times"]], n=[["32404", "splitting and merging"]]),
32404: dict(s="STORY 24 · STEP 4 · SPLIT AND MERGE", b="<b>Thinning</b> gives independent Poisson streams; <b>merging</b> adds rates.", f=[["32403", "uniform positions"]], n=[["32405", "a changing rate"]]),
32405: dict(s="STORY 24 · STEP 5 · RUSH HOUR", b="A <b>non-homogeneous</b> process has mean count m(t) = area under the rate.", f=[["32401", "constant rate"], ["32404", "thinning with time-varying p"]], n=[["32406", "a surprising gap"]]),
32406: dict(s="STORY 24 · STEP 6 · THE LONGER GAP", b="The <b>inspection paradox</b>: the gap you arrive in is twice the average gap.", f=[["32402", "exponential gaps"], ["31706", "long tails"]], n=[["32501", "walks"]]),
}

FIX = build(CARDS)
