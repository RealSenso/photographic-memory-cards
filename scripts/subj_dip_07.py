"""DIP topic 07 (2D Fourier transforms). Everyday picture: a street camera on a pole."""
from street_lib import *

SUBJECT = "DIP"

def stripes(x, y, w, h, n=6):
    out = R(x, y, w, h, "#ffffff", 1)
    for i in range(n):
        out += R(round(x + (2 * i + 1) * w / (2 * n + 1), 1), y, round(w / (2 * n + 1), 1), h, "#b8c0cc", .5)
    return out

def d3061(c):
    return svg(c,
        N(40, 12, "fence in the frame f", 7), stripes(10, 18, 60, 44, 6), N(40, 74, "6 stripes across", 6.5),
        arrow(74, 40, 98, 40, 1), N(86, 34, "DFT", 7),
        N(160, 12, "F(u, v)", 7.5), R(104, 18, 112, 44, "#ffffff", 1),
        C(160, 40, 2, "#000000"), C(184, 40, 2, "#ffffff", 1), C(136, 40, 2, "#ffffff", 1), N(160, 54, "DC", 6.5), N(184, 34, "u = 6", 6.5),
        N(120, 92, "F(u,v) = ΣΣ f(x,y) e^(−j2π(ux/M + vy/N))", 7.5),
        N(120, 106, "kernel = row wave × column wave ⇒ rows, then columns", 7.5),
        N(120, 120, "FFT: O(MN log MN)", 7.5), N(120, 134, "the fence = one pair of bright dots", 7.5))

def d3062(c):
    return svg(c,
        N(50, 12, "as computed", 7), R(14, 18, 72, 60, "#ffffff", 1), L(50, 18, 50, 78, .5, "2 2"), L(14, 48, 86, 48, .5, "2 2"),
        C(18, 22, 2.2), N(20, 90, "DC at the corner", 6.5, "start"), C(82, 22, 1.5), C(18, 74, 1.5), C(82, 74, 1.5),
        arrow(92, 48, 118, 48, 1), N(105, 42, "× (−1)^(x+y)", 6),
        N(172, 12, "centred", 7), R(124, 18, 96, 60, "#ffffff", 1), L(172, 18, 172, 78, .5, "2 2"), L(124, 48, 220, 48, .5, "2 2"),
        C(172, 48, 2.2), N(176, 60, "DC", 6.5, "start"), C(196, 36, 1.8, "#ffffff", 1), C(148, 60, 1.8, "#ffffff", 1), N(200, 33, "F(u,v)", 6.5, "start"), N(144, 72, "F*(−u,−v)", 6.5, "end"),
        N(120, 104, "periodic: F(u + M, v) = F(u, v)", 7.5),
        N(120, 118, "real f ⇒ F(u,v) = F*(−u,−v): half is redundant", 7.5),
        N(120, 132, "ℱ{ f (−1)^(x+y) } = F(u − M/2, v − N/2)", 7.5))

def d3063(c):
    return svg(c,
        N(30, 12, "frame A", 7), frame(8, 16, 44, 34), building(12, 20, 20, 26, 2, 1, "#d9dee7"),
        N(30, 62, "|F| of A", 7),
        N(120, 12, "frame B", 7), frame(98, 16, 44, 34), person(120, 48, 28), N(120, 62, "∠F of B", 7),
        N(66, 34, "+", 10), arrow(150, 33, 172, 33, 1), N(160, 26, "ℱ⁻¹", 7),
        N(204, 12, "result", 7), frame(180, 16, 44, 34), person(202, 48, 28), N(202, 62, "looks like B", 7),
        N(120, 92, "F(u,v) = |F| · e^(j∠F)", 8),
        N(120, 106, "|F| = how much of each frequency", 7.5), N(120, 118, "∠F = where the waves line up (edges, positions)", 7.5),
        N(120, 132, "swap phases ⇒ the picture follows the phase", 7.5))

def d3064(c):
    def seq(y, vals, lab, shade=()):
        return N(8, y + 11, lab, 7, "start") + pix(40, y, [vals], 13, 7, set((0, i) for i in shade))
    return svg(c,
        seq(6, [1, 2, 3, 4, "", "", ""], "f (M=4)", ()), seq(26, [1, 0, -1, "", "", "", ""], "h (K=3)"),
        N(142, 20, "← zero-padded to", 7, "start") if False else "",
        N(138, 16, "P = 7 ≥ M + K − 1 = 6", 7, "start") if False else "",
        N(200, 16, "P ≥ M+K−1", 7, "start") if False else "",
        N(140, 12, "pad both to P:", 7, "start"), N(140, 22, "P ≥ M+K−1", 7, "start"),
        L(8, 48, 232, 48, .5),
        N(8, 62, "F · H", 7.5, "start"), N(46, 62, "= ℱ{ f ⊛ h }  (circular)", 7.5, "start"),
        N(8, 82, "no padding: the tail wraps round to the start", 7.5, "start"),
        pix(40, 90, [[-2, 2, 2, 2, -3, -4]], 14, 7, {(0, 0), (0, 1)}), N(128, 100, "← wrap ✗", 7, "start") if False else N(132, 101, "wrapped ends ✗", 7, "start"),
        N(8, 124, "with padding: circular = linear (f ∗ h)", 7.5, "start"),
        N(120, 138, "padding the same size P in both dimensions", 7))

def d3065(c):
    cx, cy = 56, 58
    return svg(c,
        N(56, 10, "street slice f(x, y)", 7), circ(cx, cy, 20, "#f1f5f9", 1), 
        *[L(f(cx - 40 + k * 10), f(cy - 28 + k * 7), f(cx + 40 + k * 10 - 20 * 0), f(cy - 28 + k * 7 + 0), .5) for k in range(0)],
        *[arrow(34 + k * 11, 14, 34 + k * 11, 100 - 0, .6) if False else L(f(34 + k * 11), 16, f(34 + k * 11), 92, .5, "2 3") for k in range(5)],
        N(20, 108, "p_θ(t) = sum along each ray".replace("p_θ", "pθ"), 7, "start"),
        curve(lambda x: 124 - 10 * math.exp(-((x - 56) / 14) ** 2), 20, 92, 40, 1), N(56, 136, "t", 7),
        arrow(116, 62, 136, 62, 1), N(126, 54, "1D DFT", 6.5),
        R(140, 20, 90, 84, "#ffffff", 1), L(185, 20, 185, 104, .5, "2 2"), L(140, 62, 230, 62, .5, "2 2"),
        L(185, 62, 222, 40, 1), C(185, 62, 2), N(214, 34, "ρ", 7), N(196, 52, "θ", 7, "start"),
        N(185, 116, "F(ρ cosθ, ρ sinθ)", 7.5), N(185, 130, "a slice through the origin", 7))

def d3066(c):
    return svg(c,
        N(40, 12, "f", 8), pix(14, 18, [[1, 2], [3, 4]], 26, 10),
        arrow(70, 44, 92, 44, 1), N(81, 38, "DFT", 7),
        N(130, 12, "F", 8), pix(100, 18, [[10, -2], [-4, 0]], 26, 10),
        N(172, 26, "DC = 10", 7, "start"), N(172, 40, "−2  left/right", 7, "start"), N(172, 54, "−4  top/bottom", 7, "start"), N(172, 68, "0  checkerboard", 7, "start"),
        N(120, 96, "F(u,v) = Σ f(x,y)(−1)^(ux+vy)  (W₂ = −1)", 7.5),
        N(120, 110, "f(0,0) = ¼(10 − 2 − 4 + 0) = 1", 8),
        N(120, 126, "only additions and subtractions", 7.5))

CARDS = {
3061: dict(d=d3061, stmtKind="DEFINITION",
  statement=r"<b>2D discrete Fourier transform.</b> For an $M\times N$ image $f(x,y)$, $F(u,v)=\sum_{x=0}^{M-1}\sum_{y=0}^{N-1}f(x,y)\,e^{-j2\pi(ux/M+vy/N)}$, with inverse $f(x,y)=\frac1{MN}\sum_{u,v}F(u,v)\,e^{j2\pi(ux/M+vy/N)}$. The kernel is separable, so $F$ is computed by 1D DFTs along the rows and then along the columns, and with the FFT in $O(MN\log MN)$ operations.",
  hint="Which two bright dots would the fence's stripes put in the frequency picture?",
  breakdown=[r"<strong>$e^{-j2\pi(ux/M+vy/N)}$ = a wave of frequency $(u,v)$.</strong> A stripe pattern across the frame; $u$ counts stripes along $x$, $v$ along $y$.",
             r"<strong>$\sum\sum f(x,y)\,e^{-j2\pi(\cdot)}$ = how much of that wave the frame contains.</strong> Multiply the frame by the wave and add up: a big total means the frame has that stripe pattern.",
             r"<strong>Separable kernel = rows, then columns.</strong> The 2D wave is a product of a row wave and a column wave, so two sweeps of the 1D FFT give $F$ cheaply."],
  conn=r"<strong>The fence in the street.</strong> A fence with six stripes across the frame shows up as one pair of bright dots at $u=\pm6$: the DFT says how much of each stripe pattern the frame holds, and nothing about where the fence is.",
  cap="A fence of 6 stripes across the street frame f gives F(u, v) with a bright dot at the origin (DC) and a pair at u = ±6. F(u,v) = ΣΣ f(x,y)·e^(−j2π(ux/M + vy/N))."),
3062: dict(d=d3062, stmtKind="PROPOSITION",
  statement=r"<b>Periodicity, symmetry and centring.</b> $F(u,v)$ is periodic: $F(u+M,v)=F(u,v+N)=F(u,v)$. For real $f$, $F(u,v)=F^*(-u,-v)$, so $|F|$ is symmetric about the origin. For even $M,N$, $\mathcal F\{f(x,y)(-1)^{x+y}\}=F(u-\tfrac M2,v-\tfrac N2)$, which moves the zero-frequency term to the centre of the array.",
  hint="Why does the raw spectrum show its brightest dot in a corner, and how do you move it to the middle?",
  breakdown=[r"<strong>$F(u+M,v)=F(u,v)$ = the spectrum repeats.</strong> The four corners of the array are really one blob wrapped round, which is why DC sits in a corner.",
             r"<strong>$F(u,v)=F^*(-u,-v)$ = real frames have a mirror-image spectrum.</strong> The magnitude at $(u,v)$ equals the magnitude at $(-u,-v)$, so half of it is redundant.",
             r"<strong>$(-1)^{x+y}$ before the transform = slide DC to the centre.</strong> Multiplying the frame by a checkerboard of $\pm1$ shifts the spectrum by half its size."],
  conn=r"<strong>Reading the street spectrum.</strong> After centring, low frequencies (soft shapes) cluster in the middle and the fence or brick stripes sit symmetrically on either side, so filters can be drawn as circles around the centre.",
  cap="The spectrum as computed has DC (the dot at the origin) in a corner and four wrapped quadrants. Multiplying f by (−1)^(x+y) moves DC to the middle, where F(u,v) and F*(−u,−v) mirror each other."),
3063: dict(d=d3063, stmtKind="PROPOSITION",
  statement=r"<b>Magnitude and phase.</b> Writing $F(u,v)=|F(u,v)|\,e^{j\angle F(u,v)}$, the magnitude gives the amplitude of each frequency component and the phase gives its alignment. Reconstruction from the phase alone, $\mathcal F^{-1}\{e^{j\angle F}\}$, retains the edges and structure of $f$, while reconstruction from the magnitude alone, $\mathcal F^{-1}\{|F|\}$, does not; exchanging the phases of two images makes each result resemble the image that supplied the phase.",
  hint="If you swap the phase of the shop frame into the person frame, which one does the result look like?",
  breakdown=[r"<strong>$|F|$ = how much of each stripe pattern.</strong> It sets contrast and texture energy but does not say where anything is.",
             r"<strong>$\angle F$ = where the stripes line up.</strong> Edges are places where many waves line up at once, so phase carries the street's shapes and positions.",
             r"<strong>$\mathcal F^{-1}\{e^{j\angle F}\}$ = phase only.</strong> Setting every magnitude to 1 and transforming back still shows the outline of the scene."],
  conn=r"<strong>Mixing the shop frame and the person frame.</strong> Take the amplitudes of one and the alignments of the other: the result looks like the frame that gave the alignments. The picture is carried by where the waves line up.",
  cap="Frame A gives |F| and frame B gives ∠F. The inverse transform looks like B: the person's edges come from the phase, not the magnitude."),
3064: dict(d=d3064, stmtKind="THEOREM",
  statement=r"<b>Convolution theorem.</b> For the DFT, $\mathcal F\{f\circledast h\}=F(u,v)\,H(u,v)$, where $\circledast$ is circular convolution of period $(P,Q)$. If $f$ has size $M$ and $h$ size $K$ (in each dimension) and both are zero-padded to $P\ge M+K-1$, then the circular convolution equals the linear convolution $f\ast h$.",
  hint="Why does multiplying the two spectra give the wrong border pixels unless you pad first?",
  breakdown=[r"<strong>$F\cdot H$ = filtering is one multiply per frequency.</strong> Instead of sliding a kernel over the frame, multiply the two spectra and invert.",
             r"<strong>$\circledast$ = the frame wraps round.</strong> The DFT treats the frame as one tile of an endless repeating pattern, so the kernel pulls in pixels from the opposite border.",
             r"<strong>$P\ge M+K-1$ = enough zeros to stop the wrap.</strong> Pad both $f$ and $h$ to the same size $P$ in each dimension; then the tail lands in empty space, and circular equals linear."],
  conn=r"<strong>Blurring the street frame through the spectrum.</strong> Without padding the right edge of the frame leaks into the left edge and a bright shopfront bleeds across the border. Pad first and the blur matches the sliding-kernel result.",
  cap="Signal f (M = 4) and kernel h (K = 3) multiplied in frequency. Without padding the tail wraps to the start (circular); padding both to P ≥ M + K − 1 = 6 gives the true linear f ∗ h."),
3065: dict(d=d3065, stmtKind="THEOREM",
  statement=r"<b>Central slice (projection-slice) theorem.</b> Let $p_\theta(t)=\int f(t\cos\theta-s\sin\theta,\ t\sin\theta+s\cos\theta)\,ds$ be the projection of $f$ along rays perpendicular to the direction $\theta$ (the Radon transform). Then $\int p_\theta(t)\,e^{-j2\pi\rho t}\,dt=F(\rho\cos\theta,\rho\sin\theta)$: the 1D Fourier transform of the projection is the slice of the 2D transform through the origin at angle $\theta$.",
  hint="If a scanner adds up the street along parallel rays, which line of the 2D spectrum do you get?",
  breakdown=[r"<strong>$p_\theta(t)$ = the sum along each parallel ray.</strong> A one-dimensional shadow profile of the scene, as a scanner measures it.",
             r"<strong>$\int p_\theta(t)\,e^{-j2\pi\rho t}dt$ = the 1D transform of that profile.</strong> One frequency number $\rho$ for each point along the profile.",
             r"<strong>$F(\rho\cos\theta,\rho\sin\theta)$ = a line through the middle of the 2D spectrum</strong> at angle $\theta$. Many angles fill the plane, and inverting gives the image back."],
  conn=r"<strong>Many shadows of the street.</strong> Looking at the street from many directions and summing along each ray gives many profiles; each fills one spoke of the spectrum, which is how a scanner rebuilds the image.",
  cap="Parallel rays at angle θ sum the frame f into the profile pθ(t). Its 1D transform is the line F(ρ cosθ, ρ sinθ) through the origin of the 2D spectrum."),
3066: dict(d=d3066, stmtKind="WORKED EXAMPLE",
  statement=r"<b>Example.</b> For $f=\begin{pmatrix}1&2\\3&4\end{pmatrix}$ ($M=N=2$, $e^{-j\pi}=-1$): $F(u,v)=\sum_{x,y}f(x,y)(-1)^{ux+vy}$, giving $F=\begin{pmatrix}10&-2\\-4&0\end{pmatrix}$, and the inverse $f(x,y)=\tfrac14\sum F(u,v)(-1)^{ux+vy}$ returns $f(0,0)=\tfrac14(10-2-4+0)=1$.",
  hint="With only four pixels, which entry of F is the average brightness and which is the checkerboard?",
  breakdown=[r"<strong>$F(0,0)=1+2+3+4=10$ = the DC term.</strong> The sum of all pixels, four times the average brightness 2.5.",
             r"<strong>$F(0,1)=-2,\ F(1,0)=-4$ = the left/right and top/bottom contrast.</strong> Each is one half of the frame minus the other half.",
             r"<strong>$F(1,1)=1-2-3+4=0$ = the checkerboard part.</strong> It is zero because the diagonal pixels cancel; the inverse adds the four terms back to recover each pixel."],
  conn=r"<strong>A four-pixel patch of the frame.</strong> One total for the overall brightness and three for how it tilts left-right, up-down and diagonally. Nothing more is needed to rebuild the patch.",
  cap="The 2×2 patch f = [[1, 2], [3, 4]] gives F = [[10, −2], [−4, 0]]: DC = 10, left/right contrast −2, top/bottom contrast −4, checkerboard 0."),
}

STORY = {
 3061: dict(s="STORY 3 · STEP 7 · THE FREQUENCY VIEW", b="The <b>DFT</b> rewrites the frame as stripe patterns of every frequency; a fence is just a pair of bright dots.",
   f=[["3051", "filters seen in space"]], n=[["3062", "how to read the spectrum"], ["3064", "filtering by multiplying"]]),
 3062: dict(s="STORY 3 · STEP 8 · READING THE SPECTRUM", b="The spectrum repeats and mirrors for real frames; <b>centring</b> puts DC in the middle.",
   f=[["3061", "the DFT"]], n=[["3063", "magnitude and phase"]]),
 3063: dict(s="STORY 3 · STEP 9 · WHAT CARRIES THE PICTURE", b="<b>Phase</b> carries edges and positions; magnitude carries how much of each frequency.",
   f=[["3062", "the spectrum"]], n=[["3064", "using the spectrum to filter"], ["3141", "lines have frequency-plane fingerprints"]]),
 3064: dict(s="STORY 3 · STEP 10 · FILTER BY MULTIPLYING", b="Convolution becomes <b>multiplication</b>, as long as you <b>zero-pad</b> to stop the wraparound.",
   f=[["3061", "the DFT"], ["3051", "convolution"]], n=[["3065", "another use of the spectrum"], ["3103", "restoration filters"]]),
 3065: dict(s="STORY 3 · STEP 11 · SCANNER VIEW", b="The sum along parallel rays is one <b>slice</b> of the 2D spectrum; many angles rebuild the frame.",
   f=[["3061", "the DFT"]], n=[["3066", "a small calculation"], ["3141", "Hough also votes over angles"]]),
 3066: dict(s="STORY 3 · STEP 12 · CHECK BY HAND", b="A $2\\times2$ patch worked through: DC and three contrasts.",
   f=[["3061", "the DFT"]], n=[["3071", "next: what happens when the frame is only sampled"]]),
}
FIX = build_fix(CARDS)
