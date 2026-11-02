"""StoMA topic 25 (random walks, Brownian motion). Commute picture: the accumulated delay, taken in ever smaller steps."""
from commute_lib import *
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
    return svg(c, ax(24, 64, 226, 14), N(226, 76, "step n", 7, "end"), N(28, 14, "position", 7, "start"), poly(walk(5, 60, 26, 222, 64, 3.4), 1),
        N(120, 112, "Σ ℙ(back at 0 at step 2n) = ∞  ⇔  d = 1 or 2: recurrent", 7), N(120, 124, "∑ n^(−d/2) < ∞  ⇔  d ≥ 3: transient", 7.5), N(120, 138, "in the plane you still come home; in 3 dimensions you may not", 6.8))

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
    out = ax(24, 108, 226, 20) + N(226, 120, "x", 7, "end") + N(28, 20, "f(x)", 7, "start")
    for x, y in [(50, 80), (80, 60), (110, 50), (170, 70)]:
        out += C(x, y, 2.4)
    out += fn(lambda x: 108 - 50 - 20 * math.sin((x - 24) / 28), 24, 226, 60, 1.2)
    out += fn(lambda x: 108 - 50 - 20 * math.sin((x - 24) / 28) - 14 * math.exp(-((x - 140) ** 2) / 500), 24, 226, 60, .7, "3 2") + fn(lambda x: 108 - 50 - 20 * math.sin((x - 24) / 28) + 14 * math.exp(-((x - 140) ** 2) / 500), 24, 226, 60, .7, "3 2")
    return svg(c, out, N(120, 12, "a random function: fit through noisy readings", 7.5), N(140, 36, "uncertainty widens", 7, "start") if False else N(224, 28, "wide band: unsure", 7, "end"),
        N(120, 130, "μ* = K*ᵀ (K + σ²I)⁻¹ y,  Σ* = K** − K*ᵀ (K + σ²I)⁻¹ K*", 7), N(120, 142, "K(x, x′) = σf² e^(−‖x − x′‖²/2ℓ²)", 7))

CARDS = {
32501: dict(d=d1, kind="THEOREM",
  stmt=r"<b>Pólya's recurrence theorem.</b> The simple symmetric random walk on $\mathbb Z^d$ satisfies $\sum_{n\ge1}P^{(2n)}_{00}=\infty$ iff $d\in\{1,2\}$, in which case it is recurrent. For $d\ge3$, $P^{(2n)}_{00}\asymp n^{-d/2}$ is summable ($\sum n^{-d/2}<\infty$) and the walk is transient (Grimmett 5.10; Ross 4.3).",
  hint="Does a random walker in one, two or three dimensions come home for sure?",
  bd=[r"<strong>$P^{(2n)}_{00}\asymp n^{-d/2}$ = return chance at step $2n$.</strong> The walk is at the origin at time $2n$ with chance of order $n^{-d/2}$.",
      r"<strong>$\sum n^{-d/2}=\infty$ for $d\le2$ = recurrent.</strong> The exponent $d/2\le1$ gives a divergent sum: the origin is visited infinitely often.",
      r"<strong>$\sum n^{-d/2}<\infty$ for $d\ge3$ = transient.</strong> The sum converges, so with positive probability the walker never returns."],
  conn=r"<strong>Lost in a city.</strong> A random walker on a street (1D) or a flat grid (2D) always gets home, though it can take very long. In three dimensions, such as a building with floors, they may drift away for good.",
  cap="A random walk and its returns to 0. The return chance at step 2n is of order n^(−d/2): the sum diverges for d = 1, 2 (recurrent) and converges for d ≥ 3 (transient)."),
32502: dict(d=d2, kind="DEFINITION",
  stmt=r"<b>Standard Brownian motion.</b> $B(0)=0$; independent increments; $B(t)-B(s)\sim\mathcal N(0,t-s)$ for $s<t$; continuous paths. Donsker's theorem: for a simple random walk $S_n$, $\frac{S_{\lfloor nt\rfloor}}{\sqrt n}\xrightarrow{d}B(t)$ as a process. Paths are nowhere differentiable: $\operatorname{Var}\bigl(\frac{\Delta B}{\Delta t}\bigr)=\frac1{\Delta t}\to\infty$ (Ross 10.1; Durrett 8).",
  hint="What continuous wander appears if you take smaller and smaller random steps?",
  bd=[r"<strong>$B(t)-B(s)\sim\mathcal N(0,t-s)$ = Gaussian increments.</strong> The change over a time span is normal with variance equal to the span, and independent for disjoint spans.",
      r"<strong>$S_{\lfloor nt\rfloor}/\sqrt n\to B(t)$ = Donsker.</strong> Rescaled random walks converge to Brownian motion, the continuous-time version of the CLT.",
      r"<strong>$\operatorname{Var}(\Delta B/\Delta t)=1/\Delta t\to\infty$ = no slope.</strong> The paths are continuous but have no derivative anywhere."],
  conn=r"<strong>Delay seen through a microscope.</strong> The accumulated delay made of many tiny random nudges looks like one continuous jagged path. Zooming in does not smooth it.",
  cap="A coarse random walk and a fine one converge to the same continuous path B(t). Increments over disjoint spans are independent normal variables with variance equal to the span."),
32503: dict(d=d3, kind="THEOREM",
  stmt=r"<b>Brownian covariance and scaling.</b> $\operatorname{Cov}(B(t),B(s))=\min(t,s)$. For every $c>0$, $B(ct)\overset d=\sqrt c\,B(t)$ (self-similarity), and $tB(1/t)\overset d=B(t)$ (time inversion, with value $0$ at $t=0$) (Ross 10.1; Durrett 8).",
  hint="How are the delay now and the delay later related, and what happens when you zoom in or out?",
  bd=[r"<strong>$\operatorname{Cov}(B(t),B(s))=\min(t,s)$ = shared history.</strong> For $s\le t$, $B(t)=B(s)+(\text{independent increment})$, so the covariance is $\operatorname{Var}B(s)=s$.",
      r"<strong>$B(ct)\overset d=\sqrt cB(t)$ = scaling.</strong> Speeding up time by $c$ and shrinking space by $\sqrt c$ gives the same law.",
      r"<strong>$tB(1/t)\overset d=B(t)$ = time inversion.</strong> It has the same covariance, so the same law as a Gaussian process."],
  conn=r"<strong>Delay builds up and is shared.</strong> The delay at the end of the trip includes everything accumulated at the halfway mark. How the two relate is set by the earlier time, and a zoomed-out view looks like the original.",
  cap="The covariance min(s, t) as a function of s for a fixed t: it rises like s until t and then stays at t. Self-similarity: time scaled by c, space by √c."),
32504: dict(d=d4, kind="THEOREM",
  stmt=r"<b>Quadratic variation and Itô's rule.</b> For partitions $\Pi$ of $[0,t]$, $\lim_{\|\Pi\|\to0}\sum_i\bigl(B(t_i)-B(t_{i-1})\bigr)^2=t$ in $L^2$, i.e. $[B]_t=t$. Formally $(dB)^2=dt$ and $dB\,dt=0$, which gives Itô's formula $df(B)=f'(B)dB+\frac12f''(B)dt$ (Øksendal 4; Durrett 8).",
  hint="Why do the squared little moves of a jagged path add up to the elapsed time rather than to zero?",
  bd=[r"<strong>$\sum(\Delta B)^2$ = add up the squared moves.</strong> Chop $[0,t]$ into tiny pieces and square each piece's change.",
      r"<strong>$\to t$ in $L^2$ = the time elapsed.</strong> Each square has mean $\Delta t$, and the variance of the sum goes to 0 as the mesh shrinks.",
      r"<strong>$(dB)^2=dt$ and $dB\,dt=0$ = the Itô rule.</strong> The second-order term $\frac12f''\,dt$ appears in the change of $f(B)$."],
  conn=r"<strong>Jitter does not cancel.</strong> The little squared wiggles in your delay add up to a fixed amount equal to the elapsed time. An ordinary smooth path would give zero, which is why a new calculus is needed.",
  cap="A partition of [0, t] and the path's increments. The sum of squared increments tends to t: this is the quadratic variation [B]ₜ = t, the origin of the extra term in Itô's formula."),
32505: dict(d=d5, kind="THEOREM",
  stmt=r"<b>Reflection principle.</b> Let $M(t)=\max_{s\le t}B(s)$ and $\tau_a=\inf\{t:B(t)=a\}$, $a>0$. Then $\mathbb P(M(t)\ge a)=\mathbb P(\tau_a\le t)=2\mathbb P(B(t)\ge a)=2\bigl(1-\Phi(a/\sqrt t)\bigr)$, and $\tau_a$ has density $f_{\tau_a}(t)=\frac{a}{\sqrt{2\pi t^3}}e^{-a^2/(2t)}$ (Ross 10.2; Durrett 8).",
  hint="What is the chance that the wander ever reaches a level a before time t?",
  bd=[r"<strong>$\mathbb P(M(t)\ge a)=\mathbb P(\tau_a\le t)$ = reaching the level.</strong> The running maximum is at least $a$ iff the level $a$ was hit by time $t$.",
      r"<strong>$=2\mathbb P(B(t)\ge a)$ = reflect after hitting.</strong> After $\tau_a$ the path is symmetric about $a$, so ending above $a$ is half as likely as hitting it.",
      r"<strong>$f_{\tau_a}(t)=\frac a{\sqrt{2\pi t^3}}e^{-a^2/2t}$ = the hitting time.</strong> It decays like $t^{-3/2}$, a heavy tail with infinite mean."],
  conn=r"<strong>Will the delay ever hit the limit?</strong> The chance that your accumulated delay touches a level at some point is twice the chance that it ends above that level, because every such path has a mirror twin.",
  cap="A path hits level a at time τ. Reflecting the rest of the path about a gives a mirror path, so ℙ(M(t) ≥ a) = 2ℙ(B(t) ≥ a). The hitting time has a heavy tail."),
32506: dict(d=d6, kind="WORKED EXAMPLE",
  stmt=r"<b>Gaussian-process regression.</b> Place a Gaussian-process prior with kernel $K(x,x')=\sigma_f^2e^{-\|x-x'\|^2/(2\ell^2)}$ on $f$ and observe $y=f(X)+\varepsilon$, $\varepsilon\sim\mathcal N(0,\sigma^2I)$. The posterior at $x_*$ is Gaussian with $\mu_*=K_*^{\top}(K+\sigma^2I)^{-1}y$ and $\Sigma_*=K_{**}-K_*^{\top}(K+\sigma^2I)^{-1}K_*$ (Rasmussen–Williams 2).",
  hint="How do you fit a curve through noisy delay readings and say how sure you are?",
  bd=[r"<strong>$K(x,x')=\sigma_f^2e^{-\|x-x'\|^2/2\ell^2}$ = similarity.</strong> Inputs that are close have strongly related values; $\ell$ sets how far the relation reaches.",
      r"<strong>$\mu_*=K_*^{\top}(K+\sigma^2I)^{-1}y$ = the predicted curve.</strong> A weighted combination of the observed values, weighted by similarity and corrected for noise.",
      r"<strong>$\Sigma_*=K_{**}-K_*^{\top}(K+\sigma^2I)^{-1}K_*$ = the uncertainty.</strong> The prior variance minus what the data explains; wide away from data."],
  conn=r"<strong>Predicting a delay from a few readings.</strong> Given the delay at 8:00, 8:10 and 8:45, you can predict 8:20 by leaning on nearby readings, and you are less sure at 9:30, far from any reading.",
  cap="Four noisy readings, the posterior mean curve and a band of uncertainty. The band is narrow near the data and widens away from it."),
}

STORY = {
32501: dict(s="STORY 25 · STEP 1 · COMING HOME", b="<b>Pólya</b>: a symmetric walk returns for sure in 1D and 2D, but not in 3D.", f=[["31906", "the 1D walk"], ["31904", "recurrence"]], n=[["32502", "the continuous limit"]]),
32502: dict(s="STORY 25 · STEP 2 · SMALLER STEPS", b="<b>Brownian motion</b> is the limit of rescaled random walks (Donsker).", f=[["31803", "the CLT"], ["32501", "random walks"]], n=[["32503", "its covariance"]]),
32503: dict(s="STORY 25 · STEP 3 · SHARED HISTORY", b="Covariance is <b>min(s, t)</b>, and the path is self-similar.", f=[["32502", "Brownian motion"]], n=[["32504", "jitter adds up"], ["32505", "reaching a level"]]),
32504: dict(s="STORY 25 · STEP 4 · JITTER ADDS UP", b="<b>Quadratic variation</b> [B]ₜ = t gives Itô's rule (dB)² = dt.", f=[["32503", "scaling"]], n=[["32505", "hitting levels"]]),
32505: dict(s="STORY 25 · STEP 5 · HITTING A LEVEL", b="The <b>reflection principle</b>: ℙ(M(t) ≥ a) = 2ℙ(B(t) ≥ a).", f=[["32504", "path properties"], ["32105", "gambler's ruin"]], n=[["32506", "Gaussian processes"], ["32601", "martingales"]]),
32506: dict(s="STORY 25 · STEP 6 · PREDICTING A CURVE", b="A <b>Gaussian process</b> gives a mean curve and an uncertainty band from noisy readings.", f=[["32503", "covariance kernels"]], n=[["32601", "martingales"]]),
}

FIX = build(CARDS)
