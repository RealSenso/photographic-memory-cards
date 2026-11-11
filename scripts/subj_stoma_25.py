"""StoMA topic 25 (random walks, Brownian motion). F1 picture: the gap between Max and a rival, lap by lap a random walk, and seen corner by corner a Brownian path."""
from f1_lib import *
import random

SUBJECT = "StoMA"

def walk(seed, n=60, x0=26, x1=222, y=64, k=7, step=1.0):
    r = random.Random(seed)
    pts, v = [], 0
    for i in range(n + 1):
        pts.append((x0 + (x1 - x0) * i / n, max(20, min(y + 36, y - v))))
        v += (k if r.random() < .5 else -k) * step
    return pts

def d1(c):
    return svg(c, ax(24, 64, 226, 14), N(226, 76, "lap n", 7, "end"), N(28, 14, "gap to rival", 7, "start"), poly(walk(5, 60, 26, 222, 64, 3.4), 1),
        N(120, 112, "Σ ℙ(back at 0 at step 2n) = ∞  ⇔  d = 1 or 2: recurrent", 7), N(120, 124, "∑ n^(−d/2) < ∞  ⇔  d ≥ 3: transient", 7.5), N(120, 138, "level with 1 or 2 rivals again for sure; with 3, maybe never", 6.8))

def d2(c):
    return svg(c, ax(24, 64, 226, 14), N(226, 76, "t", 7, "end"), N(28, 14, "B(t)", 7, "start"), poly(walk(2, 40, 26, 222, 64, 3.6), 1), poly(walk(2, 200, 26, 222, 64, 1.6), .8),
        N(120, 112, "B(t) − B(s) ~ 𝒩(0, t − s), independent increments", 7.5), N(120, 124, "Donsker: S⌊nt⌋ / √n → B(t) in law", 7.5), N(120, 138, "paths are continuous but too jagged to have a slope", 7))

def d3(c):
    out = ax(24, 108, 226, 20) + N(226, 120, "s", 7, "end") + N(28, 20, "Cov(B(s), B(t))", 7, "start")
    out += fn(lambda x: 108 - 0.62 * (x - 24), 24, 130, 20, 1.1) + L(130, 108 - 0.62 * 106, 226, 108 - 0.62 * 106, 1.1)
    out += dash(130, 108, 130, 108 - 0.62 * 106) + tick(130, 108, "t")
    return svg(c, out, N(80, 62, "= s for s ≤ t", 7), N(176, 28, "= t for s ≥ t", 7),
        N(120, 128, "Cov(B(t), B(s)) = min(t, s);  B(ct) =ᵈ √c B(t);  tB(1/t) =ᵈ B(t)", 6.8), N(120, 140, "zoom in by c and out by √c: same picture", 7))

def d4(c):
    out = ax(24, 64, 226, 14) + poly(walk(8, 50, 26, 222, 64, 3), 1)
    for x in (26, 76, 124, 174, 222):
        out += L(x, 100, x, 108, .8)
    out += L(26, 104, 222, 104, .8)
    return svg(c, out, N(120, 12, "cut [0, t] into tiny pieces, square each move", 7.5), N(120, 119, "∑ (ΔB)² → t in L²", 8), N(120, 131, "so (dB)² = dt and dB·dt = 0", 8),
        N(120, 143, "the squares add up to the elapsed time, not to 0", 7))

def d5(c):
    out = ax(24, 90, 226, 14) + N(226, 102, "t", 7, "end") + L(24, 40, 226, 40, .8, "4 3") + N(28, 34, "a", 7, "start")
    p1 = walk(4, 40, 26, 200, 90, 8)
    out += poly([(x, max(40 - (y - 40), 14) if False else y) for x, y in p1], .6) if False else ""
    pts = []
    for x, y in [(26, 90), (50, 76), (74, 60), (98, 46), (122, 34), (146, 44), (170, 52), (196, 60)]:
        pts.append((x, y))
    out += poly(pts, 1.1)
    refl = [(122, 34), (146, 24), (170, 16), (196, 20)]
    out += poly([(122, 34)] + [(146, 26), (170, 28), (196, 20)], 1.1, "3 2") if False else poly([(122, 34), (146, 36), (170, 28), (196, 20)], 1.1, "3 2")
    return svg(c, out, N(110, 108, "τₐ", 7.5) if False else tick(122, 90, "τ"), N(210, 66, "path", 7, "start"), N(210, 18, "mirror image", 7, "start"),
        N(120, 12, "reflect after hitting level a", 7.5), N(120, 118, "ℙ(M(t) ≥ a) = 2ℙ(B(t) ≥ a) = 2(1 − Φ(a/√t))", 7), N(120, 130, "f(τₐ)(t) = a / √(2πt³) · e^(−a²/2t)", 7.5), N(120, 142, "hitting time of a has a heavy tail: no mean", 7))

def d6(c):
    out = ax(24, 108, 226, 20) + N(226, 120, "lap x", 7, "end") + N(28, 20, "gap f(x)", 7, "start")
    for x, y in [(50, 80), (80, 60), (110, 50), (170, 70)]:
        out += C(x, y, 2.4)
    out += fn(lambda x: 108 - 50 - 20 * math.sin((x - 24) / 28), 24, 226, 60, 1.2)
    out += fn(lambda x: 108 - 50 - 20 * math.sin((x - 24) / 28) - 14 * math.exp(-((x - 140) ** 2) / 500), 24, 226, 60, .7, "3 2") + fn(lambda x: 108 - 50 - 20 * math.sin((x - 24) / 28) + 14 * math.exp(-((x - 140) ** 2) / 500), 24, 226, 60, .7, "3 2")
    return svg(c, out, N(120, 12, "the gap curve: fit through noisy timing readings", 7.5), N(140, 36, "uncertainty widens", 7, "start") if False else N(224, 28, "wide band: unsure", 7, "end"),
        N(120, 130, "μ* = K*ᵀ (K + σ²I)⁻¹ y,  Σ* = K** − K*ᵀ (K + σ²I)⁻¹ K*", 7), N(120, 142, "K(x, x′) = σf² e^(−‖x − x′‖²/2ℓ²)", 7))

CARDS = {
32501: dict(d=d1, kind="THEOREM",
  stmt=r"<b>Pólya's recurrence theorem.</b> The simple symmetric random walk on $\mathbb Z^d$ satisfies $\sum_{n\ge1}P^{(2n)}_{00}=\infty$ iff $d\in\{1,2\}$, in which case it is recurrent. For $d\ge3$, $P^{(2n)}_{00}\asymp n^{-d/2}$ is summable ($\sum n^{-d/2}<\infty$) and the walk is transient (Grimmett 5.10; Ross 4.3).",
  hint='If the gap to a rival goes up or down a bit each lap at random, are they sure to be level again? What about with two or three rivals at once?',
  bd=[r"<strong>$P^{(2n)}_{00}\asymp n^{-d/2}$ = return chance at step $2n$.</strong> The gaps are all back to zero at lap $2n$ with chance of order $n^{-d/2}$, where $d$ is how many gaps you track.",
      r"<strong>$\sum n^{-d/2}=\infty$ for $d\le2$ = recurrent.</strong> The exponent $d/2\le1$ gives a divergent sum: the cars are level again infinitely often.",
      r"<strong>$\sum n^{-d/2}<\infty$ for $d\ge3$ = transient.</strong> The sum converges, so with positive chance the gaps never all close again."],
  conn="<strong>Back level with the rival.</strong> If Max's gap to one rival moves a random step each lap, it is sure to hit zero again, though it can take very long. The same holds for the pair of gaps to two rivals. With three rivals' gaps tracked at once, all three may never be zero together again.",
  cap='The gap as a random walk, lap by lap, and its returns to 0. The return chance at lap 2n is of order n^(−d/2): the sum diverges for d = 1, 2 (recurrent) and converges for d ≥ 3 (transient).'),
32502: dict(d=d2, kind="DEFINITION",
  stmt=r"<b>Standard Brownian motion.</b> $B(0)=0$; independent increments; $B(t)-B(s)\sim\mathcal N(0,t-s)$ for $s<t$; continuous paths. Donsker's theorem: for a simple random walk $S_n$, $\frac{S_{\lfloor nt\rfloor}}{\sqrt n}\xrightarrow{d}B(t)$ as a process. Paths are nowhere differentiable: $\operatorname{Var}\bigl(\frac{\Delta B}{\Delta t}\bigr)=\frac1{\Delta t}\to\infty$ (Ross 10.1; Durrett 8).",
  hint='What continuous wander appears if you measure the gap more and more often, in smaller and smaller random steps?',
  bd=[r"<strong>$B(t)-B(s)\sim\mathcal N(0,t-s)$ = Gaussian increments.</strong> The change in the gap over a stretch of the race is normal with variance equal to the length of the stretch, and independent for separate stretches.",
      r"<strong>$S_{\lfloor nt\rfloor}/\sqrt n\to B(t)$ = Donsker.</strong> Rescaled random walks converge to Brownian motion, the continuous-time version of the CLT.",
      r"<strong>$\operatorname{Var}(\Delta B/\Delta t)=1/\Delta t\to\infty$ = no slope.</strong> The paths are continuous but have no derivative anywhere."],
  conn='<strong>The gap through a microscope.</strong> Lap by lap the gap is a coarse random walk. Measured at every corner from telemetry, the many tiny random nudges make one continuous jagged path. Zooming in does not smooth it.',
  cap='A coarse random walk (gap per lap) and a fine one (gap per corner) converge to the same continuous path B(t). Changes over separate stretches are independent normal variables with variance equal to the length.'),
32503: dict(d=d3, kind="THEOREM",
  stmt=r"<b>Brownian covariance and scaling.</b> $\operatorname{Cov}(B(t),B(s))=\min(t,s)$. For every $c>0$, $B(ct)\overset d=\sqrt c\,B(t)$ (self-similarity), and $tB(1/t)\overset d=B(t)$ (time inversion, with value $0$ at $t=0$) (Ross 10.1; Durrett 8).",
  hint='How are the gap at half distance and the gap at the flag related, and what happens when you zoom in or out?',
  bd=[r"<strong>$\operatorname{Cov}(B(t),B(s))=\min(t,s)$ = shared history.</strong> For $s\le t$, $B(t)=B(s)+(\text{independent increment})$, so the covariance is $\operatorname{Var}B(s)=s$.",
      r"<strong>$B(ct)\overset d=\sqrt cB(t)$ = scaling.</strong> Speeding up time by $c$ and shrinking the gap scale by $\sqrt c$ gives the same law.",
      r"<strong>$tB(1/t)\overset d=B(t)$ = time inversion.</strong> It has the same covariance, so the same law as a Gaussian process."],
  conn='<strong>The final gap contains the halfway gap.</strong> The gap at the chequered flag is the gap at half distance plus whatever happened after. So how the two relate is set by the earlier time, and a zoomed-out view of the gap looks like the original.',
  cap='The covariance min(s, t) as a function of s for a fixed t: it rises like s until t and then stays at t. Self-similarity: time scaled by c, the gap by √c.'),
32504: dict(d=d4, kind="THEOREM",
  stmt=r"<b>Quadratic variation and Itô's rule.</b> For partitions $\Pi$ of $[0,t]$, $\lim_{\|\Pi\|\to0}\sum_i\bigl(B(t_i)-B(t_{i-1})\bigr)^2=t$ in $L^2$, i.e. $[B]_t=t$. Formally $(dB)^2=dt$ and $dB\,dt=0$, which gives Itô's formula $df(B)=f'(B)dB+\frac12f''(B)dt$ (Øksendal 4; Durrett 8).",
  hint='Why do the squared little changes in a jagged gap curve add up to the race time elapsed rather than to zero?',
  bd=[r"<strong>$\sum(\Delta B)^2$ = add up the squared moves.</strong> Chop $[0,t]$ into tiny pieces and square each piece's change in the gap.",
      r"<strong>$\to t$ in $L^2$ = the time elapsed.</strong> Each square has mean $\Delta t$, and the variance of the sum goes to 0 as the pieces shrink.",
      r"<strong>$(dB)^2=dt$ and $dB\,dt=0$ = the Itô rule.</strong> The second-order term $\frac12f''\,dt$ appears in the change of $f(B)$."],
  conn='<strong>The jitter does not cancel.</strong> The little squared wiggles in the gap, corner after corner, add up to a fixed amount equal to the race time elapsed. A smooth gap curve would give zero, which is why a new calculus is needed.',
  cap="A partition of [0, t] and the gap's changes. The sum of squared changes tends to t: this is the quadratic variation [B]ₜ = t, the origin of the extra term in Itô's formula."),
32505: dict(d=d5, kind="THEOREM",
  stmt=r"<b>Reflection principle.</b> Let $M(t)=\max_{s\le t}B(s)$ and $\tau_a=\inf\{t:B(t)=a\}$, $a>0$. Then $\mathbb P(M(t)\ge a)=\mathbb P(\tau_a\le t)=2\mathbb P(B(t)\ge a)=2\bigl(1-\Phi(a/\sqrt t)\bigr)$, and $\tau_a$ has density $f_{\tau_a}(t)=\frac{a}{\sqrt{2\pi t^3}}e^{-a^2/(2t)}$ (Ross 10.2; Durrett 8).",
  hint="What is the chance that Max's lead ever reaches a seconds before time t?",
  bd=[r"<strong>$\mathbb P(M(t)\ge a)=\mathbb P(\tau_a\le t)$ = reaching the level.</strong> The biggest lead so far is at least $a$ iff the lead first hit $a$ by time $t$.",
      r"<strong>$=2\mathbb P(B(t)\ge a)$ = reflect after hitting.</strong> After $\tau_a$ the path is symmetric about $a$, so ending above $a$ is half as likely as hitting it.",
      r"<strong>$f_{\tau_a}(t)=\frac a{\sqrt{2\pi t^3}}e^{-a^2/2t}$ = the hitting time.</strong> It decays like $t^{-3/2}$, a heavy tail with infinite mean."],
  conn="<strong>Will the lead ever reach 5 seconds?</strong> The chance that Max's biggest lead so far has reached 5 seconds is twice the chance that his lead right now is above 5 seconds, because every path that touched 5 has a mirror twin that ends below it.",
  cap='The gap hits level a at time τ. Reflecting the rest of the path about a gives a mirror path, so ℙ(M(t) ≥ a) = 2ℙ(B(t) ≥ a), where M(t) is the biggest lead so far. The hitting time has a heavy tail.'),
32506: dict(d=d6, kind="WORKED EXAMPLE",
  stmt=r"<b>Gaussian-process regression.</b> Place a Gaussian-process prior with kernel $K(x,x')=\sigma_f^2e^{-\|x-x'\|^2/(2\ell^2)}$ on $f$ and observe $y=f(X)+\varepsilon$, $\varepsilon\sim\mathcal N(0,\sigma^2I)$. The posterior at $x_*$ is Gaussian with $\mu_*=K_*^{\top}(K+\sigma^2I)^{-1}y$ and $\Sigma_*=K_{**}-K_*^{\top}(K+\sigma^2I)^{-1}K_*$ (Rasmussen–Williams 2).",
  hint='How do you fit a gap curve through a few noisy timing readings and say how sure you are between them?',
  bd=[r"<strong>$K(x,x')=\sigma_f^2e^{-\|x-x'\|^2/2\ell^2}$ = similarity.</strong> The gaps at nearby laps are strongly related; $\ell$ sets how many laps the relation reaches.",
      r"<strong>$\mu_*=K_*^{\top}(K+\sigma^2I)^{-1}y$ = the predicted curve.</strong> A weighted combination of the measured gaps, weighted by similarity and corrected for noise.",
      r"<strong>$\Sigma_*=K_{**}-K_*^{\top}(K+\sigma^2I)^{-1}K_*$ = the uncertainty.</strong> The prior variance minus what the data explains; wide far from any reading."],
  conn='<strong>Predicting the gap between readings.</strong> Given the gap to the rival at laps 10, 20 and 45, you can predict lap 30 by leaning on the nearby readings, and you are much less sure about lap 60, far from any reading.',
  cap='Four noisy gap readings, the posterior mean gap curve and a band of uncertainty. The band is narrow near the readings and widens away from them.'),
}

STORY = {
32501: dict(s='STORY 25 · STEP 1 · BACK LEVEL', b="<b>Pólya</b>: a symmetric walk returns for sure in 1D and 2D, but not in 3D.", f=[["31906", "the 1D walk"], ["31904", "recurrence"]], n=[["32502", "the continuous limit"]]),
32502: dict(s="STORY 25 · STEP 2 · SMALLER STEPS", b="<b>Brownian motion</b> is the limit of rescaled random walks (Donsker).", f=[["31803", "the CLT"], ["32501", "random walks"]], n=[["32503", "its covariance"]]),
32503: dict(s="STORY 25 · STEP 3 · SHARED HISTORY", b="Covariance is <b>min(s, t)</b>, and the path is self-similar.", f=[["32502", "Brownian motion"]], n=[["32504", "jitter adds up"], ["32505", "reaching a level"]]),
32504: dict(s="STORY 25 · STEP 4 · JITTER ADDS UP", b="<b>Quadratic variation</b> [B]ₜ = t gives Itô's rule (dB)² = dt.", f=[["32503", "scaling"]], n=[["32505", "hitting levels"]]),
32505: dict(s="STORY 25 · STEP 5 · HITTING A LEVEL", b="The <b>reflection principle</b>: ℙ(M(t) ≥ a) = 2ℙ(B(t) ≥ a).", f=[["32504", "path properties"], ["32105", "gambler's ruin"]], n=[["32506", "Gaussian processes"], ["32601", "martingales"]]),
32506: dict(s="STORY 25 · STEP 6 · PREDICTING A CURVE", b="A <b>Gaussian process</b> gives a mean curve and an uncertainty band from noisy readings.", f=[["32503", "covariance kernels"]], n=[["32601", "martingales"]]),
}

FIX = build(CARDS)
