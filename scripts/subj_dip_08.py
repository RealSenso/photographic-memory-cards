"""DIP topic 08 (sampling, aliasing, multi-rate). Everyday picture: a street camera on a pole."""
from street_lib import *

SUBJECT = "DIP"

def tri(cx, base, hw, h, d=None, fill="none"):
    return poly([(cx - hw, base), (cx, base - h), (cx + hw, base)], 1, d, fill)

def d3071(c):
    b = 70
    out = [axes(10, b, 232, 14), N(232, b + 10, "u", 8, "end"), N(14, 12, "|F|", 7, "start"),
           tri(40, b, 18, 40, None, "#f1f5f9"), N(40, b + 10, "0", 7)]
    for k, cx in ((1, 112), (2, 184)):
        out += [tri(cx, b, 18, 40, "3 2"), N(cx, b + 10, "1/Δ" if k == 1 else "2/Δ", 7)]
    out += [tri(-32 + 40, b, 0, 0),
            N(120, 100, "sampling the fence frame every Δ", 7.5),
            N(120, 112, "x comb of impulses", 7) if False else "",
            N(120, 114, "FΔ(u) = (1/Δ) Σ F(u − k/Δ)", 8),
            N(120, 128, "copies of the spectrum at every k/Δ = k·fₛ", 7.5)]
    return svg(c, *out)

def d3072(c):
    b1, b2 = 44, 108
    return svg(c,
        N(17, 12, "fₛ > 2 uₘₐₓ", 7.5, "start"),
        axes(10, b1, 232, 12), tri(40, b1, 14, 26, "3 2"), tri(120, b1, 14, 26, None, "#f1f5f9"), tri(200, b1, 14, 26, "3 2"),
        N(120, b1 + 10, "0", 6.5), N(138, b1 + 10, "uₘₐₓ", 6.5), N(228, 12, "gap ⇒ cut out the middle copy", 6.5, "end"),
        N(17, 72, "fₛ < 2 uₘₐₓ", 7.5, "start"),
        axes(10, b2, 232, 74), tri(84, b2, 24, 26, "3 2"), tri(120, b2, 24, 26, None, "#f1f5f9"), tri(156, b2, 24, 26, "3 2"),
        quad([(96, b2), (102, b2 - 6.5), (108, b2)], "#b8c0cc", None, .5), quad([(132, b2), (138, b2 - 6.5), (144, b2)], "#b8c0cc", None, .5),
        L(142, b2 - 5, 176, b2 - 16, .5), N(178, b2 - 16, "overlap", 6.5, "start"), N(120, b2 + 10, "copies overlap ⇒ aliasing", 6.5),
        N(190, 90, "x(t) = Σ x(nΔ) sinc((t−nΔ)/Δ)", 6.5, "middle") if False else "",
        N(180, 28, "no overlap ⇒ sinc interpolation", 6.5, "start") if False else "",
        N(120, 134, "more than two samples per cycle ⇒ exact recovery", 7.5))

def d3073(c):
    out = [L(10, 70, 232, 70, .5, "1 3"), N(12, 12, "wheel spokes seen at 0.9 fₛ", 7.5, "start")]
    out.append(curve(lambda x: 70 - 30 * math.cos(2 * math.pi * (x - 20) / (200 / 9)), 20, 220, 200, .8))
    out.append(curve(lambda x: 70 - 30 * math.cos(2 * math.pi * (x - 20) / 200), 20, 220, 100, 1, "3 2"))
    for k in range(11):
        x = 20 + 20 * k
        out.append(C(f(x), f(70 - 30 * math.cos(2 * math.pi * (x - 20) / 200)), 2, "#ffffff", 1))
    out += [N(120, 112, "same samples, two waves: fast u₀ and its slow alias", 7.5),
            N(120, 124, "alias = |u₀ − k fₛ|", 8), N(120, 136, "0.9 fₛ ⇒ 0.1 fₛ: the wheel crawls slowly", 7.5)]
    return svg(c, *out)

def d3074(c):
    b = 62
    def clipped(cx, base, hw, h, d):   # a neighbouring copy, cut off at the edge of the plot
        lo, hi = max(134, cx - hw), min(230, cx + hw)
        return poly([(x, base - h * (1 - abs(x - cx) / hw)) for x in (lo, cx, hi)] if lo < cx < hi else [(lo, base - h * (1 - abs(lo - cx) / hw)), (hi, base - h * (1 - abs(hi - cx) / hw))], 1, d)
    return svg(c,
        N(14, 10, "before", 7, "start"), axes(10, b, 112, 14), tri(61, b, 28, 34, None, "#f1f5f9"), N(21, b + 9, "−π", 6.5), N(61, b + 9, "0", 6.5), N(101, b + 9, "π", 6.5), N(92, 26, "band 0.7π", 6.5),
        arrow(116, 40, 130, 40, 1), N(122, 32, "↓M", 7),
        N(136, 10, "after (M = 2)", 7, "start"), axes(132, b, 232, 14), clipped(134, b, 34, 17, "3 2"), clipped(230, b, 34, 17, "3 2"), tri(182, b, 34, 17, None, "#d9dee7"),
        N(158, b + 9, "−π", 6.5), N(182, b + 9, "0", 6.5), N(206, b + 9, "π", 6.5), N(182, 30, "stretched copies overlap", 6.5),
        N(120, 92, "g[n] = f[Mn]", 8), N(120, 105, "G(ω) = (1/M) Σ F((ω − 2πk)/M)", 7.5),
        N(120, 120, "filter first: low-pass with cutoff π/M", 7.5), N(120, 133, "then drop frames: every M-th frame kept", 7.5))

def d3075(c):
    return svg(c,
        N(8, 18, "f[n]", 7.5, "start"), pix(36, 6, [[3, 5, 2, 4]], 18, 8),
        N(8, 48, "fₑ[n]", 7.5, "start"), pix(36, 36, [[3, 0, 5, 0, 2, 0, 4, 0]], 18, 8),
        arrow(184, 42, 204, 42, 1), N(194, 34, "LPF", 7), N(218, 46, "gain L", 7),
        N(120, 66, "insert L − 1 zeros between samples (L = 2)", 7.5),
        N(120, 84, "Fₑ(ω) = F(Lω): spectrum squeezed, L copies appear", 7.5),
        N(120, 98, "low-pass: cutoff π/L, gain L", 7.5),
        N(120, 114, "gain L keeps the picture as bright as before", 7.5),
        N(120, 130, "L/M rate: upsample, filter, downsample", 7.5))

def d3076(c):
    return svg(c,
        L(14, 60, 226, 60, 1), L(14, 56, 14, 64, 1), L(226, 56, 226, 64, 1), N(14, 74, "0", 7), N(226, 74, "100 Hz = fₛ", 7, "end"),
        L(120, 52, 120, 68, 1, "3 2"), N(120, 82, "50 = fₛ/2", 7),
        C(204.8, 60, 2.4), N(204.8, 50, "90", 7), C(35.2, 60, 2.4), N(35.2, 74, "10", 7),
        P("M203,52 Q120,12 38,54", "none", 1, None, True), N(120, 24, "fold about fₛ/2", 7.5),
        N(120, 102, "cos(2π·90·n/100) = cos(2π·10·n/100)", 8),
        N(120, 115, "k = round(90/100) = 1 ⇒ |90 − 100| = 10 Hz", 7.5),
        N(120, 129, "wheel at 0.8 cycles/pixel ⇒ |0.8 − 1| = 0.2 (moiré)", 7.5))

CARDS = {
3071: dict(d=d3071, stmtKind="THEOREM",
  statement=r"<b>Spectrum of a sampled signal.</b> If $f_\Delta(x)=f(x)\sum_{n}\delta(x-n\Delta)$ is the ideal sampling of $f$ with spacing $\Delta$, then $F_\Delta(u)=\frac1\Delta\sum_{k=-\infty}^{\infty}F\!\big(u-\frac k\Delta\big)$: the spectrum of the sampled signal consists of copies of $F$ centred at the multiples of the sampling frequency $1/\Delta$.",
  hint="When the camera records a frame every Δ, how many copies of the street's spectrum appear?",
  breakdown=[r"<strong>$\sum_n\delta(x-n\Delta)$ = the camera only looks at every $\Delta$-th spot.</strong> Sampling multiplies the scene by a comb of spikes.",
             r"<strong>$F(u-k/\Delta)$ = a copy of the spectrum moved to $k/\Delta$.</strong> A product in space is a convolution in frequency, and convolving with a comb pastes the spectrum at every tooth.",
             r"<strong>$1/\Delta$ = the sampling frequency.</strong> The copies sit one sampling frequency apart; to recover the original, one low-pass filter must cut out the middle copy alone."],
  conn=r"<strong>The camera's sensor grid.</strong> A pixel every $\Delta$ is the same as repeating the street's spectrum along the frequency axis. As long as the copies do not touch, the original is still in there.",
  cap="The street's spectrum F(u) (shaded) is pasted at every multiple k/Δ of the sampling frequency when the camera samples every Δ: FΔ(u) = (1/Δ) Σ F(u − k/Δ)."),
3072: dict(d=d3072, stmtKind="THEOREM",
  statement=r"<b>Sampling theorem (Shannon–Nyquist).</b> If $f$ is bandlimited, $F(u)=0$ for $|u|\gt u_{\max}$, and it is sampled with spacing $\Delta$ such that $f_s=1/\Delta\gt 2u_{\max}$, then $f$ is recovered exactly from its samples: $f(x)=\sum_n f(n\Delta)\,\operatorname{sinc}\!\big(\frac{x-n\Delta}{\Delta}\big)$. If $f_s\lt2u_{\max}$ the replicas overlap and aliasing occurs. At $f_s=2u_{\max}$ recovery still holds unless $F$ has an impulse at $\pm u_{\max}$.",
  hint="How many samples per cycle of the fence's finest stripes do you need?",
  breakdown=[r"<strong>$f_s\gt2u_{\max}$ = more than two samples per cycle.</strong> The spectrum copies must sit more than twice the highest frequency apart, so they do not overlap. Exactly two can fail: $\sin(2\pi u_{\max}x)$ sampled at its zeros gives all zeros."],
  conn=r"<strong>How many pixels the fence needs.</strong> The finest stripes of the fence need more than two pixels per stripe pair. Fewer, and the camera cannot tell them from something coarser.",
  cap="Top: the copies of the spectrum stay apart when fₛ > 2 uₘₐₓ and the middle copy can be cut out. Bottom: for fₛ < 2 uₘₐₓ the copies overlap and cause aliasing."),
3073: dict(d=d3073, stmtKind="DEFINITION",
  statement=r"<b>Aliasing.</b> A sinusoid of frequency $u_0\gt f_s/2$ sampled at rate $f_s$ gives the same samples as a sinusoid of frequency $u_{\rm alias}=|u_0-k f_s|$, where $k$ is the integer for which $u_{\rm alias}\in[0,f_s/2]$ (the nearest multiple of $f_s$, $k=\operatorname{round}(u_0/f_s)$). The effect cannot be undone after sampling; it is prevented by low-pass filtering before sampling.",
  hint="Why does a fast-spinning wheel in the street frame look slow, or even run backwards?",
  breakdown=[r"<strong>$u_0\gt f_s/2$ = too fast for the frame rate.</strong> Fewer than two samples per cycle: the samples cannot tell the fast wave from a slower one that goes through the same points."],
  conn=r"<strong>The spinning wheel of a passing car.</strong> The camera takes a frame, the spokes move almost a full turn, the next frame shows them slightly behind: the wheel appears to crawl, or to roll backwards.",
  cap="A fast wave at 0.9 fₛ and a slow wave at 0.1 fₛ pass through exactly the same samples (circles), so the camera sees the slow one, at the alias frequency |u₀ − k fₛ|."),
3074: dict(d=d3074, stmtKind="DEFINITION",
  statement=r"<b>Downsampling (decimation) by $M$.</b> $g[n]=f[Mn]$. Its spectrum is $G(\omega)=\frac1M\sum_{k=0}^{M-1}F\!\big(\frac{\omega-2\pi k}{M}\big)$: the spectrum is stretched by $M$ and $M$ shifted copies are added, so content above $\pi/M$ aliases. Decimation therefore applies a low-pass filter with cutoff $\pi/M$ before discarding samples.",
  hint="Why must the frame be blurred a little before you throw away every other frame or pixel?",
  breakdown=[r"<strong>$g[n]=f[Mn]$ = keep one sample in $M$.</strong> The signal or frame shrinks by $M$, which is the same as sampling again at a lower rate.",
             r"<strong>$F((\omega-2\pi k)/M)$ = $M$ stretched copies.</strong> Each copy is spread out by $M$ and moved by a multiple of $2\pi$; the $M$ copies add together.",
             r"<strong>Cutoff $\pi/M$ = keep only what survives.</strong> After the stretch only the band up to $\pi/M$ fits without overlapping; the low-pass removes the rest first."],
  conn=r"<strong>Making a thumbnail of the street frame.</strong> Blur first, then keep every second pixel. Keeping every second pixel of the sharp frame turns the fine brick pattern into false coarse stripes.",
  cap="A spectrum before and after dropping every other sample (M = 2): the stretched copies overlap and add, so the content beyond π/M aliases; filter first."),
3075: dict(d=d3075, stmtKind="DEFINITION",
  statement=r"<b>Upsampling (interpolation) by $L$.</b> The expander is $f_e[n]=f[n/L]$ if $L\mid n$ and $0$ otherwise, with $F_e(\omega)=F(L\omega)$ (the spectrum is compressed by $L$ and $L$ copies appear in $[0,2\pi)$, of which $L-1$ are images). An interpolation low-pass filter with cutoff $\pi/L$ and gain $L$ removes the images and fills the zeros. Resampling by a rational factor $L/M$ is upsampling by $L$, one low-pass with cutoff $\min(\pi/L,\pi/M)$ and gain $L$, then downsampling by $M$.",
  hint="After you stuff zeros between the pixels of a frame, what must you do to make it a smooth bigger frame?",
  breakdown=[r"<strong>$f_e[n]=f[n/L]$ or $0$ = zeros in between.</strong> Stretching the frame by $L$ leaves $L-1$ blank pixels between the real ones."],
  conn=r"<strong>Zooming in on the number plate.</strong> Stuffing zeros makes a speckled frame; the low-pass (with gain) fills the holes with smooth values and restores the brightness.",
  cap="f[n] gets L − 1 zeros between samples to give fₑ[n]; a low-pass of cutoff π/L and gain L removes the extra spectrum copies and fills the zeros."),
3076: dict(d=d3076, stmtKind="WORKED EXAMPLE",
  statement=r"<b>Example.</b> A $90$ Hz cosine sampled at $f_s=100$ Hz exceeds the Nyquist frequency $f_s/2=50$ Hz. With $k=\operatorname{round}(90/100)=1$, $u_{\rm alias}=|90-100|=10$ Hz, and $\cos(2\pi\cdot90\,\tfrac n{100})=\cos(2\pi\cdot10\,\tfrac n{100})$ for every integer $n$. Likewise a grating of $0.8$ cycles/pixel aliases to $|0.8-1|=0.2$ cycles/pixel.",
  hint="Where does 90 Hz land when the camera only takes 100 frames a second?",
  breakdown=[r"<strong>$u_0=90\gt f_s/2=50$ = past the fold.</strong> Above half the frame rate, so Nyquist is violated."],
  conn=r"<strong>A wheel spinning at 90 turns a second.</strong> Filmed at 100 frames a second it looks like it turns at 10 the other way, like a slow wheel rolling backwards. The 0.8 cycles/pixel brick pattern looks like a coarse band.",
  cap="The frequency axis from 0 to fₛ = 100 Hz folds about fₛ/2 = 50 Hz: 90 Hz lands on 10 Hz, and 0.8 cycles/pixel lands on 0.2."),
}
# the bullets that were left as one entry get their remaining two
CARDS[3072]["breakdown"] += [r"<strong>$\operatorname{sinc}\!\big(\frac{x-n\Delta}{\Delta}\big)$ = the ideal rebuilding bump, with $\operatorname{sinc}w=\frac{\sin\pi w}{\pi w}$.</strong> Putting one at each sample, scaled by the sample value, and adding gives the original exactly.",
                             r"<strong>$f_s\lt2u_{\max}$ = overlap.</strong> The copies of the spectrum touch, high frequencies pretend to be low ones and the loss cannot be undone."]
CARDS[3073]["breakdown"] += [r"<strong>$|u_0-kf_s|$ = fold back into the band.</strong> Subtract the nearest multiple of the sampling frequency; $0.9f_s$ lands on $0.1f_s$.",
                             r"<strong>Low-pass before sampling = the only defence.</strong> Once the samples are taken the fast and slow waves are identical, so no later filter can separate them."]
CARDS[3075]["breakdown"] += [r"<strong>$F_e(\omega)=F(L\omega)$ = the spectrum shrinks and repeats.</strong> $L$ copies now fit between $0$ and $2\pi$.",
                             r"<strong>Cutoff $\pi/L$ and gain $L$ = keep one copy at full brightness.</strong> The zeros lowered the average by $L$, so the gain puts it back."]
CARDS[3076]["breakdown"] += [r"<strong>$u_{\rm alias}=|90-100|=10$ Hz = the nearest multiple of $f_s$.</strong> The sampled sequence is identical to that of a 10 Hz cosine.",
                             r"<strong>Use the nearest multiple, not always $k=1$.</strong> For $u_0=160$ at $f_s=100$ the fold gives $|160-200|=40$ Hz, not 60."]

# bridge facts the practice questions and PYQs rely on

CARDS[3073]["breakdown"] += [r"""<strong>2D: alias each axis with its sign, $u_a=u_0-\operatorname{round}(u_0/f_{sx})f_{sx}$, same for $v_a$.</strong> $(60,80)$ at $f_s=100$ gives $(-40,-20)\equiv(40,20)$, so the grating changes both frequency and angle, from $\arctan\frac{80}{60}=53.1^\circ$ to $\arctan\frac{20}{40}=26.6^\circ$."""]
CARDS[3074]["breakdown"] += [r"""<strong>Gaussian pyramid = blur with $w=[c,b,a,b,c]$, keep every second pixel, repeat.</strong> Unit gain $a+2b+2c=1$ and equal contribution $a+2c=2b$ force $b=\tfrac14,\ c=\tfrac14-\tfrac a2$; $a=0.4$ gives $[0.05,0.25,0.4,0.25,0.05]$."""]
CARDS[3075]["breakdown"] += [r"""<strong>Laplacian pyramid: $L_l=G_l-\operatorname{Expand}(G_{l+1})$.</strong> Blend two images band by band with the mask's Gaussian pyramid: $L_{{\rm blend},l}=G_{M,l}L_{A,l}+(1-G_{M,l})L_{B,l}$, then collapse. Fine bands join narrowly (no ghosts), coarse bands broadly (no seam)."""]

STORY = {
 3071: dict(s="STORY 3 · STEP 13 · THE CAMERA SAMPLES", b="Recording a frame every $\\Delta$ <b>pastes copies of the spectrum</b> at every multiple of the sampling frequency.",
   f=[["3061", "the spectrum"], ["40103", "the pixel grid"]], n=[["3072", "when the copies stay apart"]]),
 3072: dict(s="STORY 3 · STEP 14 · HOW FINE IS FINE ENOUGH", b="If the copies do not overlap ($f_s\\gt2u_{\\max}$) the frame can be rebuilt exactly with a <b>sinc</b>.",
   f=[["3071", "copies"]], n=[["3073", "when they overlap"]]),
 3073: dict(s="STORY 3 · STEP 15 · WHEN THEY OVERLAP", b="Too few samples: a fast wave <b>masquerades as a slow one</b> (the crawling wheel, moiré).",
   f=[["3072", "the limit"]], n=[["3074", "shrinking the frame safely"], ["3076", "a number"]]),
 3074: dict(s="STORY 3 · STEP 16 · SHRINK SAFELY", b="<b>Decimation</b> = low-pass, then keep every $M$-th sample.",
   f=[["3073", "aliasing"], ["3054", "the blur"]], n=[["3075", "enlarging"], ["3161", "scale pyramids"]]),
 3075: dict(s="STORY 3 · STEP 17 · ENLARGE SAFELY", b="<b>Interpolation</b> = insert zeros, then low-pass with gain $L$.",
   f=[["3074", "shrinking"], ["40105", "blending when warping"]], n=[["3076", "a number"], ["3093", "two-channel filter banks use both"]]),
 3076: dict(s="STORY 3 · STEP 18 · CHECK BY HAND", b="90 Hz at 100 Hz folds to 10 Hz: the <b>nearest multiple</b> of $f_s$ sets the alias.",
   f=[["3073", "aliasing"]], n=[["3081", "next: compress the frame"]]),
}
FIX = build_fix(CARDS)
