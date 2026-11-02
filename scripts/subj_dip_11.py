"""DIP topic 11 (restoration: inverse and Wiener). Everyday picture: a street camera on a pole (a blurred number plate)."""
from street_lib import *

SUBJECT = "DIP"

def plate(x, y, w=40, h=18, lab="AB 12", blur=False):
    return R(x, y, w, h, "#ffffff", 1) + N(x + w / 2, y + h / 2 + 3, lab, 8 if not blur else 8)

def d3101(c):
    return svg(c,
        N(34, 12, "f", 8), plate(14, 18, 40, 20, "AB 12"), N(34, 50, "true plate", 6.5),
        arrow(58, 28, 82, 28, 1), R(82, 16, 40, 24, "#f1f5f9", 1), N(102, 26, "h ∗", 8), N(102, 35, "motion", 6.5),
        arrow(122, 28, 140, 28, 1), N(148, 32, "+", 10), arrow(148, 14, 148, 22, 1), N(148, 10, "η", 8),
        arrow(156, 28, 174, 28, 1), N(198, 12, "g", 8), R(178, 18, 42, 20, "#d9dee7", 1), N(199, 31, "A B 1 2", 8), N(199, 50, "what the camera saw", 6.5),
        N(120, 82, "g = h ∗ f + η   ⟷   G = H F + N", 8.5),
        N(120, 98, "noise is added after the blur: it is not blurred", 7.5),
        N(120, 114, "restoration: model the damage, then estimate F̂ = W G", 7.5))

def d3102(c):
    b = 100
    return svg(c,
        axes(16, b, 150, 14), N(150, b + 10, "u", 8, "end"),
        curve(lambda x: b - 70 * math.exp(-((x - 16) / 50) ** 2), 16, 140, 50, 1), N(100, b - 14, "|H|", 8, "start"),
        curve(lambda x: max(14, b - 1.5 / (max(.03, math.exp(-((x - 16) / 50) ** 2))) * 6 - 0), 16, 140, 50, 1, "3 2"), N(120, 24, "1/|H|", 8),
        R(104, 20, 40, 82, "none", .6, 0, "1 3"), N(124, 118, "noise zone", 6.5),
        R(160, 20, 70, 62, "#f1f5f9", 1), N(195, 34, "F̂ = G / H", 8), N(195, 48, "= F + N / H", 8), N(195, 66, "H → 0 ⇒ N/H blows up", 6.5),
        N(120, 138, "the plate turns to snow", 7.5))

def d3103(c):
    b = 100
    return svg(c,
        axes(16, b, 150, 14), N(150, b + 10, "u", 8, "end"),
        curve(lambda x: max(14, b - 6 / max(.04, math.exp(-((x - 16) / 50) ** 2))), 16, 140, 50, 1, "3 2"), N(30, 22, "1/H", 7),
        curve(lambda x: b - 6 * (lambda h: h / (h * h + .05))(math.exp(-((x - 16) / 50) ** 2)) * 2, 16, 140, 50, 1), N(110, 70, "Wiener W", 7, "start"),
        R(160, 20, 70, 76, "#f1f5f9", 1), N(195, 32, "W =", 8), N(195, 46, "H*", 8), L(176, 50, 214, 50, .8), N(195, 62, "|H|² + S_η/S_f".replace("S_η", "Sη").replace("S_f", "Sf"), 7), N(195, 82, "F̂ = W G", 8),
        N(120, 124, "strong |H|: W ≈ 1/H", 7.5), N(120, 137, "weak |H|: W backs off, noise stays quiet", 7.5))

def d3104(c):
    return svg(c,
        axes(18, 106, 130, 14), N(130, 116, "‖g − Hf‖² (misfit)", 7, "end"), N(14, 14, "‖Pf‖² (roughness)", 7, "start"),
        curve(lambda x: 106 - 76 / (1 + ((x - 18) / 24) ** 1.5) if x > 18 else 30, 22, 126, 50, 1),
        dot(62, 66, None, r=2.4), N(66, 62, "γ chosen here (corner)", 7, "start"),
        N(30, 40, "too smooth", 6.5, "start") if False else "",
        R(150, 20, 80, 70, "#f1f5f9", 1), N(190, 33, "min ‖Pf‖²", 7.5), N(190, 45, "s.t. ‖g − Hf‖² = ‖η‖²", 6.5), N(190, 60, "F̂ = H* G /", 7.5), N(190, 72, "(|H|² + γ|P|²)", 7.5), N(190, 84, "P = Laplacian", 6.5),
        N(120, 134, "no power spectra needed: only the noise size", 7.5))

def d3105(c):
    b = 76
    return svg(c,
        car(10, 40, 34, 14), arrow(46, 34, 82, 34, 1), N(64, 28, "aT", 7), car(86, 40, 34, 14), N(60, 62, "moves aT during the exposure", 6.5),
        axes(132, b, 232, 12), N(232, b + 10, "u", 7, "end"), N(130, 14, "|H|", 7, "end"),
        curve(lambda x: b - 54 * abs(math.sin(math.pi * (x - 132) / 36) / (math.pi * (x - 132) / 36)) if x > 132 else b - 54, 132, 228, 90, 1),
        N(168, b + 10, "1/aT", 6.5), N(204, b + 10, "2/aT", 6.5),
        N(120, 102, "H(u) = sin(πuaT)/(πua) · e^(−jπuaT)", 8), N(120, 116, "zeros at u = k/(aT): that information is gone", 7.5),
        N(120, 130, "Gaussian blur: no exact zeros, fast roll-off", 7.5))

def d3106(c):
    def bar(x, h, lab, v):
        return R(x, 96 - h, 22, h, "#f1f5f9", .8) + N(x + 11, 106, lab, 6.5) + N(x + 11, 92 - h, v, 7)
    return svg(c,
        N(14, 12, "K = Sη/Sf = 0.05", 7.5, "start"), L(14, 96, 232, 96, .8),
        N(60, 24, "weak frequency, H = 0.1", 7), bar(26, 46, "inverse", "10"), bar(60, 8, "Wiener", "1.67"),
        N(176, 24, "strong frequency, H = 1", 7), bar(142, 4.6, "inverse", "1"), bar(176, 4.4, "Wiener", "0.95"),
        N(120, 120, "W(0.1) = 0.1/(0.01 + 0.05) = 1.67", 7.5), N(120, 133, "W(1) = 1/(1 + 0.05) = 0.952", 7.5),
        N(120, 144, "trade a little bias for far less noise", 6.5))

CARDS = {
3101: dict(d=d3101, stmtKind="DEFINITION",
  statement=r"<b>Image degradation model.</b> The observed image is $g(x,y)=(h\ast f)(x,y)+\eta(x,y)$, where $f$ is the true image, $h$ the point spread function of a linear shift-invariant degradation and $\eta$ additive noise. In the frequency domain $G(u,v)=H(u,v)F(u,v)+N(u,v)$. Restoration seeks an estimate $\hat F=W\,G$ of $F$ using a model of $h$ and $\eta$.",
  hint="When a moving car's plate is blurred by the camera, where in the formula is the noise added?",
  breakdown=[r"<strong>$h\ast f$ = the blur.</strong> What the exposure does to the true plate: each point is smeared by the point spread function.",
             r"<strong>$+\,\eta$ = noise added afterwards.</strong> Sensor noise lands on the already-blurred frame, so it is not blurred itself.",
             r"<strong>$G=HF+N$ = the same in frequency.</strong> The convolution turns into a product, so each frequency of the plate is multiplied by $H(u,v)$ and noise is added; restoration has to undo $H$ without boosting $N$."],
  conn=r"<strong>The blurred number plate.</strong> A car drives past the pole camera during the exposure: the plate is smeared sideways (the $h$), and the night sensor adds speckle on top (the $\eta$). Reading the plate means undoing the first without amplifying the second.",
  cap="The true plate f is blurred by h (the car moving) and then speckle η is added, giving the recorded frame g = h ∗ f + η, or G = H F + N in frequency."),
3102: dict(d=d3102, stmtKind="PROPOSITION",
  statement=r"<b>Inverse filtering.</b> Given $G=HF+N$, the inverse filter estimate is $\hat F(u,v)=\dfrac{G(u,v)}{H(u,v)}=F(u,v)+\dfrac{N(u,v)}{H(u,v)}$. Where $H(u,v)\to0$ (typically at high frequencies, and exactly zero for some blurs) the term $N/H$ is arbitrarily large, so the estimate is dominated by amplified noise. The remedy is to restrict the division to frequencies where $|H|$ is large, or to use Wiener or regularized filters.",
  hint="Why does dividing by the blur give back the plate when there is no noise, and snow when there is?",
  breakdown=[r"<strong>$G/H=F+N/H$ = the right answer plus an error.</strong> With no noise the division cancels $H$ exactly and gives $F$ back.",
             r"<strong>$H\to0$ at high frequencies = the blur has wiped them out.</strong> Fine detail was nearly erased by the blur, so $|H|$ is tiny there.",
             r"<strong>$N/H$ = noise divided by something tiny.</strong> The tiny numbers are exactly where only noise is left, and dividing by them makes it huge: the plate drowns in snow."],
  conn=r"<strong>Sharpening the plate too hard.</strong> Undoing the blur frequency by frequency works until the blur has erased a frequency: there the camera only recorded speckle, and dividing by almost zero multiplies that speckle until it covers the plate.",
  cap="The blur |H| falls toward 0 at high u. The inverse 1/|H| (dashed) shoots up there, multiplying the noise: F̂ = G/H = F + N/H."),
3103: dict(d=d3103, stmtKind="THEOREM",
  statement=r"<b>Wiener filter.</b> For $g=h\ast f+\eta$ with $f,\eta$ uncorrelated wide-sense stationary with power spectra $S_f,S_\eta$, the linear filter minimizing $E\|f-\hat f\|^2$ is $W(u,v)=\dfrac{H^*(u,v)}{|H(u,v)|^2+S_\eta(u,v)/S_f(u,v)}$, with $\hat F=W\,G$. In practice $S_\eta/S_f$ is replaced by a constant $K$ chosen by eye: $K=0$ gives the inverse filter.",
  hint="How should a restoring filter act where the blur has nearly erased the plate's frequencies?",
  breakdown=[r"<strong>$H^*/|H|^2$ = the inverse where the signal is strong.</strong> When $|H|^2$ is much larger than the noise ratio, $W\approx1/H$ and the blur is undone.",
             r"<strong>$S_\eta/S_f$ in the denominator = a safety margin.</strong> Where $|H|$ is tiny, the margin dominates and $W$ shrinks towards zero instead of exploding.",
             r"<strong>$K$ = one knob by eye.</strong> $K=0$ is the inverse filter (snow); a larger $K$ gives a calmer but blurrier plate."],
  conn=r"<strong>Know when the camera has no information.</strong> The Wiener filter sharpens the plate's strokes where the sensor recorded them clearly, and simply stays quiet at the frequencies the blur has buried in speckle.",
  cap="The inverse 1/H (dashed) explodes at high u. The Wiener filter W = H*/(|H|² + Sη/Sf) follows it where |H| is large and bends down where |H| is small."),
3104: dict(d=d3104, stmtKind="ALGORITHM",
  statement=r"<b>Constrained least-squares (CLS) restoration.</b> Minimize the roughness $\|Pf\|^2$ ($P$ the Laplacian operator) subject to $\|g-Hf\|^2=\|\eta\|^2$. The solution in the frequency domain is $\hat F(u,v)=\dfrac{H^*(u,v)}{|H(u,v)|^2+\gamma\,|P(u,v)|^2}\,G(u,v)$, where the Lagrange parameter $\gamma$ is adjusted iteratively until $\|g-H\hat f\|^2\approx\|\eta\|^2$ (or chosen at the corner of the L-curve).",
  hint="If you do not know the signal's power spectrum, what can you ask the restored plate to be instead?",
  breakdown=[r"<strong>$\|Pf\|^2$ = how rough the plate estimate is.</strong> The Laplacian $P$ is large on jagged edges and noise, so a small value means a smooth estimate.",
             r"<strong>$\|g-Hf\|^2=\|\eta\|^2$ = it must explain the frame up to the noise.</strong> Re-blurring the estimate must give back the recorded frame to within the size of the noise, only knowing $\|\eta\|^2$.",
             r"<strong>$\gamma|P|^2$ = the smoothness price.</strong> Like Wiener's $K$, but weighted more at high frequencies; $\gamma$ is tuned until the fit equals the noise level."],
  conn=r"<strong>Smoothest plate that explains the footage.</strong> Of all the sharp-looking plates that blur into the recorded frame, pick the least jagged one, and accept a fit no better than the noise allows.",
  cap="The L-curve plots roughness ‖Pf‖² against misfit ‖g − Hf‖²; γ is chosen at the corner, where the restored plate fits the frame to within the noise ‖η‖²."),
3105: dict(d=d3105, stmtKind="PROPOSITION",
  statement=r"<b>Motion-blur transfer function.</b> For uniform linear motion with displacement $aT$ during the exposure, $H(u)=\dfrac{\sin(\pi u aT)}{\pi u a}\,e^{-j\pi uaT}$, which is zero at $u=\dfrac{k}{aT}$, $k=1,2,\dots$. Defocus gives a pillbox (disk) PSF; Gaussian and turbulence blurs give a Gaussian $H$ with no exact zeros. $H$ may be found by observing a point source or sharp edge, by experiment or by modelling; blind deconvolution estimates it from $g$ alone.",
  hint="At which frequencies has the passing car's blur destroyed all information about the plate?",
  breakdown=[r"<strong>$\sin(\pi uaT)/(\pi ua)$ = a sinc.</strong> A box-shaped smear of length $aT$ has a sinc transform: strong at low $u$ and then ringing up and down.",
             r"<strong>Zeros at $u=k/(aT)$ = erased frequencies.</strong> A stripe pattern whose period fits the smear a whole number of times averages to nothing, so no linear filter can bring it back.",
             r"<strong>$e^{-j\pi uaT}$ = the shift.</strong> A pure delay of half the smear; it does not change the strength of any frequency."],
  conn=r"<strong>The car's speed sets the plate's fate.</strong> The faster the car, the longer the smear $aT$ and the lower the first zero. Strokes of the plate whose width fits the smear exactly are wiped out.",
  cap="A car moving aT during the exposure smears the plate. Its transfer function is a sinc with zeros at u = k/(aT): the information there is gone."),
3106: dict(d=d3106, stmtKind="WORKED EXAMPLE",
  statement=r"<b>Example.</b> Take $K=S_\eta/S_f=0.05$ and real $H$. At a weak frequency $H=0.1$ the inverse filter has gain $1/H=10$ (noise power $\times100$) while the Wiener gain is $W=\dfrac{0.1}{0.1^2+0.05}=1.67$. At a strong frequency $H=1$ the inverse gain is $1$ and $W=\dfrac1{1+0.05}\approx0.952$.",
  hint="How much quieter does the Wiener filter make the noise at a frequency where the blur left almost nothing?",
  breakdown=[r"<strong>$W(0.1)=0.1/(0.01+0.05)=1.67$ vs inverse $10$.</strong> At the weak frequency the Wiener gain is six times smaller, so the amplified noise power is about 36 times smaller than with the inverse."],
  conn=r"<strong>Two plate strokes.</strong> A coarse stroke the camera recorded well and a fine stroke it nearly lost. The Wiener filter treats the first like the inverse does and refuses to shout at the second.",
  cap="With K = 0.05: at weak H = 0.1 the inverse gain is 10 but Wiener only 1.67; at strong H = 1 they are almost equal (1 and 0.95)."),
}
CARDS[3106]["breakdown"] += [r"<strong>$W(1)=1/(1+0.05)=0.952$ vs inverse $1$.</strong> Where the signal is strong the two filters are almost the same: Wiener is about the inverse there.",
                             r"<strong>The 6× lower gain is the point.</strong> It gives up a little accuracy (bias) to cut a huge amount of noise (variance); for complex $H$ use $H^*$ on top and $|H|^2$ below, not $1/H$."]

STORY = {
 3101: dict(s="STORY 5 · STEP 1 · THE DAMAGE", b="The recorded frame is the true scene <b>blurred</b> and then <b>noisy</b>: $g=h\\ast f+\\eta$. Restoration needs a model of both.",
   f=[["3051", "convolution is the blur"], ["3064", "product in frequency"]], n=[["3102", "the naive fix"], ["3105", "what $H$ looks like"]]),
 3102: dict(s="STORY 5 · STEP 2 · THE NAIVE FIX", b="Dividing by $H$ undoes the blur but turns the noise into snow where $H\\to0$.",
   f=[["3101", "the model"]], n=[["3103", "a safer fix"]]),
 3103: dict(s="STORY 5 · STEP 3 · THE SAFE FIX", b="The <b>Wiener filter</b> acts like $1/H$ where the signal is strong and backs off where the noise would win.",
   f=[["3102", "inverse filtering"]], n=[["3104", "without power spectra"], ["3106", "by numbers"]]),
 3104: dict(s="STORY 5 · STEP 4 · THE SMOOTH FIX", b="<b>CLS</b> asks for the smoothest estimate that explains the frame to within the noise.",
   f=[["3103", "Wiener"]], n=[["3105", "what H is"]]),
 3105: dict(s="STORY 5 · STEP 5 · KNOWING H", b="Motion blur gives a sinc with <b>zeros</b>: some information is lost forever.",
   f=[["3101", "the model"]], n=[["3106", "worked example"], ["3111", "non-linear alternatives"]]),
 3106: dict(s="STORY 5 · STEP 6 · CHECK BY HAND", b="At a weak frequency Wiener's gain is $1.67$ against the inverse's $10$.",
   f=[["3103", "Wiener"]], n=[["3111", "next: noise that blurring cannot fix"]]),
}
FIX = build_fix(CARDS)
