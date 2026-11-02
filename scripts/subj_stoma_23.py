"""StoMA topic 23 (WSS processes). Commute picture: X(t) = delay on the road at clock time t, a signal through the morning."""
from commute_lib import *
import random
from subj_lib import box

SUBJECT = "StoMA"

def sig(seed, n=48, x0=26, x1=222, y=64, amp=22, smooth=.55):
    r = random.Random(seed)
    pts, v = [], 0
    for i in range(n + 1):
        v = smooth * v + (1 - smooth) * (r.random() - .5) * 2 * amp * 1.8
        pts.append((x0 + (x1 - x0) * i / n, y - v))
    return pts

def d1(c):
    return svg(c, ax(24, 110, 226, 14), N(226, 122, "clock time t", 7, "end"), N(28, 14, "X(t)", 7, "start"), L(24, 62, 226, 62, .8, "3 2"),
        poly(sig(1), 1), poly(sig(7), 1, "3 2"), N(12, 66, "μ", 8),
        N(120, 130, "WSS: 𝔼X(t) = μ and R(t, t+τ) = R(τ) only depend on the lag", 7), N(120, 141, "SSS: every joint law is unchanged by a time shift", 7))

def d2(c):
    out = ax(120, 108, 226, 14) + L(120, 108, 14, 108, 1, ar=False)
    out += fn(lambda x: 108 - 70 * math.exp(-abs(x - 120) / 30) * math.cos(abs(x - 120) / 20) * 1.0 if abs(x - 120) > 0 else 38, 24, 226, 80, 1.1)
    return svg(c, out, N(120, 22, "R(0) = 𝔼X²", 7.5), N(226, 120, "lag τ", 7, "end"), N(120, 120, "0", 7),
        N(120, 132, "R(0) ≥ |R(τ)|, R(−τ) = R(τ), and ∑ cᵢcⱼR(tᵢ − tⱼ) ≥ 0", 7), N(120, 143, "peak at zero lag, mirror-symmetric, non-negative definite", 6.8))

def d3(c):
    return svg(c, ax(24, 100, 120, 24), N(72, 112, "τ", 7), N(28, 20, "R(τ)", 7, "start"),
        fn(lambda x: 100 - 66 * math.exp(-abs(x - 72) / 14), 24, 120, 60, 1.1), ax(134, 100, 226, 24), N(180, 112, "ω", 7), N(138, 20, "S(ω) ≥ 0", 7, "start"),
        fn(lambda x: 100 - 66 / (1 + ((x - 180) / 10) ** 2), 134, 226, 50, 1.1), arrow(112, 60, 138, 60, 1), N(125, 52, "∫", 7),
        N(120, 12, "power spectral density", 7.5), N(120, 126, "S(ω) = ∫ R(τ) e^(−jωτ) dτ ≥ 0,  R(τ) = (1/2π) ∫ S(ω) e^(jωτ) dω", 6.8), N(120, 138, "fast fading correlation ⇒ wide spectrum", 7))

def d4(c):
    out = ax(24, 64, 226, 20) + N(226, 76, "lag τ", 7, "end") + fn(lambda x: 64 - 38 * math.cos((x - 24) / 12), 24, 226, 120, 1.1)
    out += ax(24, 100, 24, 100) if False else ""
    return svg(c, out, N(28, 14, "R(τ)", 7, "start"), N(120, 12, "R(τ) = ½ 𝔼[A²] cos(ω₀τ)", 8), N(120, 124, "needs Θ ~ Unif[−π, π]: otherwise the mean moves with t", 7),
        N(120, 136, "S(ω) = (π𝔼[A²]/2)[δ(ω − ω₀) + δ(ω + ω₀)]: two spikes", 7))

def d5(c):
    return svg(c, box(12, 50, 52, 30, "X(t)", "#f1f5f9", 8, False), box(84, 50, 62, 30, "h(t)  H(ω)", "#f1f5f9", 7.5, False), box(166, 50, 52, 30, "Y(t)", "#f1f5f9", 8, False),
        arrow(64, 65, 84, 65, 1), arrow(146, 65, 166, 65, 1), N(120, 28, "road signal → filter (e.g. phone smoothing) → output", 7),
        N(120, 100, "Sout(ω) = |H(ω)|² Sin(ω)", 8), N(120, 112, "Rout(τ) = Rin(τ) * h(τ) * h(−τ)", 7.5), N(120, 124, "𝔼Y² = (1/2π) ∫ |H(ω)|² Sin(ω) dω", 7.5), N(120, 138, "the filter reweights each frequency by its power gain", 6.8))

def d6(c):
    out = ax(24, 100, 226, 20) + N(226, 112, "T", 7, "end") + N(28, 20, "μ̂ᴛ", 7.5, "start")
    r = random.Random(3)
    pts = []
    for i in range(1, 50):
        pts.append((24 + i * 4, 60 + 38 * (r.random() - .5) / (i ** .5)))
    out += L(24, 60, 226, 60, .8, "3 2") + N(224, 54, "μ", 7.5, "end") + poly(pts, 1.1)
    return svg(c, out, N(120, 12, "time average over [−T, T] → μ in mean square", 7.5), N(120, 124, "iff (1/T)∫₀²ᵀ (1 − τ/2T) C(τ) dτ → 0", 7.5), N(120, 136, "correlations must die away fast enough", 7))

CARDS = {
32301: dict(d=d1, kind="DEFINITION",
  stmt=r"<b>Strict-sense and wide-sense stationarity.</b> $X(t)$ is strict-sense stationary if $F_{X(t_1+\tau),\ldots,X(t_k+\tau)}=F_{X(t_1),\ldots,X(t_k)}$ for all $k,t_i,\tau$. It is wide-sense stationary (WSS) if $\mathbb E[X(t)]=\mu$ is constant and $R_X(t,t+\tau)=\mathbb E[X(t)X(t+\tau)]=R_X(\tau)$ depends only on the lag (Papoulis 9; Grimmett 9.1).",
  hint="What does it mean for the road delay signal to look statistically the same at every time of day?",
  bd=[r"<strong>SSS: every joint law is shift-invariant.</strong> Moving the whole picture by $\tau$ leaves all finite-dimensional distributions unchanged.",
      r"<strong>WSS: $\mathbb E[X(t)]=\mu$ = a constant mean.</strong> The average delay does not depend on the clock time.",
      r"<strong>WSS: $R_X(t,t+\tau)=R_X(\tau)$ = correlation by lag only.</strong> How much two times are related depends only on how far apart they are; SSS with finite variance implies WSS."],
  conn=r"<strong>A morning without a rush-hour trend.</strong> If delays look the same at 8am as at 9am, with the same average and the same link between readings 5 minutes apart, the signal is wide-sense stationary.",
  cap="Two runs of the delay signal X(t) with a constant mean μ. WSS asks for a constant mean and a correlation that depends only on the lag; SSS asks for all joint laws to be shift-invariant."),
32302: dict(d=d2, kind="THEOREM",
  stmt=r"<b>Properties of the autocorrelation.</b> For a WSS process, $R_X(0)=\mathbb E[X^2(t)]\ge|R_X(\tau)|$ for all $\tau$, $R_X(-\tau)=R_X(\tau)$, and $R_X$ is non-negative definite: $\sum_{i,j}c_ic_jR_X(t_i-t_j)\ge0$ for all real $c_i$ and times $t_i$ (Papoulis 9; Grimmett 9.1).",
  hint="Which shapes can the link between readings at different lags take, and which cannot?",
  bd=[r"<strong>$R_X(0)\ge|R_X(\tau)|$ = peak at zero lag.</strong> A reading is at least as related to itself as to any other reading (Cauchy–Schwarz); $R_X(0)$ is the average power.",
      r"<strong>$R_X(-\tau)=R_X(\tau)$ = symmetry.</strong> Looking ahead by $\tau$ or back by $\tau$ gives the same link.",
      r"<strong>$\sum c_ic_jR_X(t_i-t_j)\ge0$ = non-negative definite.</strong> It equals $\operatorname{Var}\bigl(\sum c_iX(t_i)\bigr)$ (for zero mean), which cannot be negative."],
  conn=r"<strong>Not every curve is a correlation.</strong> The link between delays must be strongest at the same moment and mirror-symmetric in the lag, and it must never produce a negative variance for any weighted combination of readings.",
  cap="A valid autocorrelation R(τ): maximal at τ = 0 (where it equals the power 𝔼X²), symmetric about 0, and non-negative definite."),
32303: dict(d=d3, kind="THEOREM",
  stmt=r"<b>Wiener–Khinchin.</b> For a WSS process with integrable $R_X$, the power spectral density is the Fourier transform of the autocorrelation: $S_X(\omega)=\int_{-\infty}^{\infty}R_X(\tau)e^{-j\omega\tau}d\tau\ge0$, and $R_X(\tau)=\frac1{2\pi}\int_{-\infty}^{\infty}S_X(\omega)e^{j\omega\tau}d\omega$; in particular $\mathbb E[X^2]=\frac1{2\pi}\int S_X\,d\omega$ (Papoulis 10; Grimmett 9.3).",
  hint="How does a process's correlation over time tell you which frequencies carry its power?",
  bd=[r"<strong>$S_X(\omega)=\int R_X(\tau)e^{-j\omega\tau}d\tau$ = the spectrum.</strong> Transform the lag-correlation to the frequency domain to see where power sits.",
      r"<strong>$S_X(\omega)\ge0$ = power cannot be negative.</strong> This follows from the non-negative definiteness of $R_X$.",
      r"<strong>$R_X(\tau)=\frac1{2\pi}\int S_Xe^{j\omega\tau}d\omega$ = and back.</strong> At $\tau=0$ this says that the total power equals the area under the spectrum."],
  conn=r"<strong>Slow drifts and fast jitters.</strong> A delay signal whose readings stay related over many minutes has its power at low frequencies. One that forgets after seconds has a wide, flat spectrum.",
  cap="A correlation R(τ) that decays quickly (left) and its power spectral density S(ω) ≥ 0 (right), related by the Fourier transform. The area under S gives the total power."),
32304: dict(d=d4, kind="WORKED EXAMPLE",
  stmt=r"<b>Random harmonic process.</b> Let $X(t)=A\cos(\omega_0t+\Theta)$ with $A$ independent of $\Theta$. Then $R_X(\tau)=\frac{\mathbb E[A^2]}2\cos(\omega_0\tau)$ and $\mathbb E[X(t)]=\mathbb E[A]\,\mathbb E[\cos(\omega_0t+\Theta)]=0$ for all $t$ iff $\Theta\sim\operatorname{Unif}[-\pi,\pi]$. Then $S_X(\omega)=\frac{\pi\mathbb E[A^2]}2[\delta(\omega-\omega_0)+\delta(\omega+\omega_0)]$ (Papoulis 9–10; Grimmett 9.3).",
  hint="Why must the starting phase of a daily rhythm be completely random for the signal to be stationary?",
  bd=[r"<strong>$R_X(\tau)=\frac{\mathbb E[A^2]}2\cos(\omega_0\tau)$ = a cosine in the lag.</strong> The product of two shifted cosines averages to half the amplitude-power times $\cos(\omega_0\tau)$.",
      r"<strong>$\Theta\sim\operatorname{Unif}[-\pi,\pi]$ = needed for stationarity.</strong> Only a fully random phase gives a mean that does not move with $t$ and a correlation that depends on $\tau$ alone.",
      r"<strong>$S_X=\frac{\pi\mathbb E[A^2]}2[\delta(\omega-\omega_0)+\delta(\omega+\omega_0)]$ = two spikes.</strong> All the power sits at the frequency $\pm\omega_0$."],
  conn=r"<strong>A daily rhythm with random timing.</strong> A rush-hour wave of fixed period shows up as a single spike in the spectrum, but the wave only counts as stationary if the time you start observing is completely random within a cycle.",
  cap="The correlation of a random cosine: R(τ) = ½𝔼[A²] cos(ω₀τ), oscillating for ever, with a spectrum that is two spikes at ±ω₀. It needs a uniform phase Θ."),
32305: dict(d=d5, kind="THEOREM",
  stmt=r"<b>LTI filtering of a WSS process.</b> If $X(t)$ is WSS with spectrum $S_X$ and passes through a stable LTI system with impulse response $h$ and transfer function $H(\omega)$, then $Y=h*X$ is WSS with $S_Y(\omega)=|H(\omega)|^2S_X(\omega)$, $R_Y(\tau)=R_X(\tau)*h(\tau)*h(-\tau)$ and $\mathbb E[Y^2(t)]=\frac1{2\pi}\int|H(\omega)|^2S_X(\omega)d\omega$ (Papoulis 10; Grimmett 9.3).",
  hint="What does smoothing a noisy signal do to its power at each frequency?",
  bd=[r"<strong>$S_Y(\omega)=|H(\omega)|^2S_X(\omega)$ = reweight each frequency.</strong> A filter multiplies the power at frequency $\omega$ by its squared gain $|H(\omega)|^2$.",
      r"<strong>$R_Y=R_X*h*h(-\cdot)$ = in the lag domain.</strong> The same statement for the correlation, by the inverse Fourier transform.",
      r"<strong>$\mathbb E[Y^2]=\frac1{2\pi}\int|H|^2S_Xd\omega$ = output power.</strong> The total output power is the area under the reweighted spectrum."],
  conn=r"<strong>Smoothing your phone's ETA.</strong> Passing the raw delay signal through a smoother keeps the slow frequencies and damps the jitter. Its effect on the spectrum is just a multiplication by the squared gain.",
  cap="A WSS road signal X(t) through a filter h gives an output Y(t) with S_Y = |H|² S_X. The output power is the area under the reweighted spectrum."),
32306: dict(d=d6, kind="THEOREM",
  stmt=r"<b>Mean ergodicity (Slutsky).</b> For a WSS process with mean $\mu$ and covariance $C_X(\tau)$, $\hat\mu_T=\frac1{2T}\int_{-T}^TX(t)\,dt\to\mu$ in $L^2$ if and only if $\lim_{T\to\infty}\frac1T\int_0^{2T}\bigl(1-\frac{\tau}{2T}\bigr)C_X(\tau)\,d\tau=0$ (Papoulis 13; Grimmett 9.5).",
  hint="When does one long recording of the delay give you the true mean delay?",
  bd=[r"<strong>$\hat\mu_T=\frac1{2T}\int_{-T}^TX(t)dt$ = the time average.</strong> Average one long recording over the window $[-T,T]$.",
      r"<strong>$\hat\mu_T\to\mu$ in $L^2$ = ergodic in the mean.</strong> The mean-square error $\mathbb E|\hat\mu_T-\mu|^2$ goes to zero.",
      r"<strong>$\frac1T\int_0^{2T}(1-\frac\tau{2T})C_X(\tau)d\tau\to0$ = Slutsky's condition.</strong> This is $\operatorname{Var}(\hat\mu_T)$: the covariance must fade fast enough that the long average loses its randomness."],
  conn=r"<strong>One long recording is enough.</strong> If the delay at 8am is eventually unrelated to the delay an hour later, then averaging a single long recording gives the true mean, with no need for many mornings.",
  cap="The time average μ̂ᴛ of a single recording homes in on μ as T grows, provided the covariance C(τ) fades fast enough (Slutsky's condition)."),
}

STORY = {
32301: dict(s="STORY 23 · STEP 1 · A STEADY SIGNAL", b="<b>Wide-sense stationary</b>: constant mean, correlation depending only on the lag.", f=[["31901", "a process whose law is steady"], ["32001", "stationary law"]], n=[["32302", "which correlations are legal"]]),
32302: dict(s="STORY 23 · STEP 2 · LEGAL CORRELATIONS", b="An autocorrelation peaks at zero lag, is symmetric, and is <b>non-negative definite</b>.", f=[["32301", "WSS"], ["30605", "Cauchy–Schwarz"]], n=[["32303", "its spectrum"]]),
32303: dict(s="STORY 23 · STEP 3 · POWER BY FREQUENCY", b="<b>Wiener–Khinchin</b>: the power spectrum is the Fourier transform of the autocorrelation.", f=[["32302", "non-negative definite R"], ["31801", "characteristic function (a Fourier transform)"]], n=[["32304", "a pure rhythm"], ["32305", "through a filter"]]),
32304: dict(s="STORY 23 · STEP 4 · A PURE RHYTHM", b="A <b>random cosine</b> has two spectral spikes, and needs a uniform phase to be stationary.", f=[["32303", "spectrum"]], n=[["32305", "filtering"]]),
32305: dict(s="STORY 23 · STEP 5 · THROUGH A FILTER", b="A <b>linear filter</b> multiplies the spectrum by |H(ω)|².", f=[["32303", "spectrum"], ["32304", "spikes pass or die"]], n=[["32306", "estimating from one run"]]),
32306: dict(s="STORY 23 · STEP 6 · ONE RECORDING", b="<b>Mean ergodicity</b>: a time average equals the mean if the covariance fades.", f=[["32006", "ergodic theorem"], ["31701", "law of large numbers"]], n=[["32401", "counting arrivals"]]),
}

FIX = build(CARDS)
