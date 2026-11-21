"""DIP gap cards from the coverage audit against Problem Set 4 and Midterm 2 (2026):
7.07 DSFT of a short filter, 7.08 the buggy blur (Midterm 2 Q1), 9.07 uniform quantizer, 9.08 quantization MSE,
9.09 entropy and prefix codes, 9.10 Huffman coding (Problem Set 4 Q4-Q5). Every number on the cards is computed or asserted here.
Run from the repo root, then apply the refine layers:
  python3 scripts/build_dip_gap_cards.py && python3 scripts/apply_subj_refine.py dip"""
import heapq, json, math, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from dip_lib import T, N, L, P, C, R, AX, svg, HL, TOPICS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def ln(s, level=0):
    return f'<span class="{["ln", "ln in", "ln in2"][level]}">{s}</span>'


def stmt(head, lines, src):
    return f"<b>{head}</b>" + "".join(lines) + f'<span class="src">{src}</span>'


def make(topic, k, category, title, parts, caption, core, math_, conn, trap, kind, statement, hint, breakdown):
    tid, ttitle = TOPICS[topic]
    cid = 3000 + (topic - 1) * 10 + k
    assert len(core) == 3 and len(breakdown) == 3, cid
    return {"id": cid, "subject": "DIP", "topicId": tid, "topicTitle": ttitle, "cardNumber": f"{k:02d}", "category": category,
            "highlighterClass": HL[(k - 1) % 4], "title": title, "drawingSvg": svg(cid, *parts), "drawingCaption": caption,
            "coreTranslation": core, "math": math_, "personalConnection": conn, "examTrap": trap, "stmtKind": kind,
            "statement": statement, "hint": hint, "breakdown": breakdown, "textbookImg": None, "textbookRef": None}


def plot(fn, x0=24, x1=216, base=104, sy=74, n=120):
    """|H(W)| for W in [-pi, pi]"""
    pts = []
    for i in range(n + 1):
        w = -math.pi + 2 * math.pi * i / n
        pts.append(f"{x0 + (x1 - x0) * i / n:.1f} {base - abs(fn(w)) * sy:.1f}")
    return "M " + " L ".join(pts)


def wx(w, x0=24, x1=216):
    return round(x0 + (x1 - x0) * (w + math.pi) / (2 * math.pi), 1)


def freq_axis(base=104, ticks=((-math.pi, "−π"), (0, "0"), (math.pi, "π"))):
    out = [L(16, base, 228, base, 1.1, ar=True), L(wx(0), base + 2, wx(0), 16, 1, ar=True), T(232, base + 3, "Ω", 8, a="end")]
    for w, s in ticks:
        out += [L(wx(w), base, wx(w), base + 3, 1), N(wx(w), base + 11, s, 6.8)]
    return out


cards = []
card = lambda *a: cards.append(make(*a))

# ---------- 7.07 DSFT of a short filter ----------
H121 = lambda w: (1 + math.cos(w)) / 2
Hhp = lambda w: (1 - math.cos(w)) / 2
assert abs(H121(0) - 1) < 1e-12 and abs(H121(math.pi)) < 1e-12 and abs(Hhp(math.pi) - 1) < 1e-12
card(7, 7, "FILTER IN FREQUENCY", "DSFT of a Short Filter",
     freq_axis() + [P(plot(H121), w=1.7), P(plot(Hhp), w=1.4, dash="4 3"),
                    N(120, 125, "solid ¼[1 2 1]: low-pass   dashed ¼[−1 2 −1]: high-pass", 6.5),
                    N(120, 134, "H(0) = sum of taps", 6.8), N(120, 143, "H(π) = alternating sum of taps", 6.8)],
     "Magnitude responses of two three-tap filters over one period. The smoothing kernel keeps Ω = 0 and removes Ω = π; the difference kernel does the opposite.",
     ["<strong>The recipe:</strong> $H(\\Omega)=\\sum_n h[n]e^{-j\\Omega n}$. Each tap contributes one complex exponential, and the result repeats every $2\\pi$.",
      "<strong>Symmetric taps give cosines:</strong> if $h[-n]=h[n]$, then $H(\\Omega)=h[0]+2\\sum_{n\\ge1}h[n]\\cos(n\\Omega)$, which is real.",
      "<strong>Two quick checks:</strong> $H(0)=\\sum_n h[n]$ and $H(\\pi)=\\sum_n(-1)^nh[n]$."],
     "$$H(\\Omega)=\\sum_n h[n]e^{-j\\Omega n},\\qquad h[-n]=h[n]\\Rightarrow H(\\Omega)=h[0]+2\\sum_{n\\ge1}h[n]\\cos(n\\Omega)$$",
     "<strong>Read a filter before running it.</strong> Slow changes along the road are low $\\Omega$; the fence, alternating post and gap from pixel to pixel, is $\\Omega=\\pi$. Plugging those two values into $H$ tells you whether the camera's filter keeps the road and removes the fence.",
     "H(Ω) is continuous and has period 2π, while the DFT H[k] is its samples at Ω = 2πk/N. A shift of the taps changes only the phase, so |H(Ω)| stays the same. Plot |H|: a negative H is drawn upward.",
     "DEFINITION",
     stmt("Frequency response of an FIR filter.",
          [ln("For an impulse response $h[n]$, the DSFT is"),
           ln("$H(\\Omega)=\\sum_n h[n]e^{-j\\Omega n}$, with period $2\\pi$.", 1),
           ln("If $h[-n]=h[n]$, it is real:"),
           ln("$H(\\Omega)=h[0]+2\\sum_{n\\ge1}h[n]\\cos(n\\Omega)$.", 1),
           ln("At the two ends of the band,"),
           ln("$H(0)=\\sum_n h[n]$ and $H(\\pi)=\\sum_n(-1)^nh[n]$.", 1),
           ln("Input $e^{j\\Omega_0 n}$ leaves as $H(\\Omega_0)e^{j\\Omega_0 n}$.")],
          "E9 241 DSFT & DFT slides"),
     "Given only three filter taps, how can you tell what the filter does to the road and to the fence?",
     ["<strong>$H(\\Omega)=\\sum_n h[n]e^{-j\\Omega n}$ = one term per tap.</strong> For $\\frac14[1\\;2\\;1]$: $\\frac14(e^{j\\Omega}+2+e^{-j\\Omega})=\\frac12(1+\\cos\\Omega)=\\cos^2(\\Omega/2)$.",
      "<strong>$e^{j\\Omega}+e^{-j\\Omega}=2\\cos\\Omega$ = why symmetry helps.</strong> Taps at $\\pm n$ pair into a real cosine, so the phase disappears.",
      "<strong>$H(0)$ and $H(\\pi)$ = low-pass or high-pass.</strong> Low-pass needs $|H(0)|$ well above $|H(\\pi)|$. For 2D separable kernels, $H(\\omega_1,\\omega_2)=H_1(\\omega_1)H_2(\\omega_2)$."])

# ---------- 7.08 the buggy blur (Midterm 2 2026 Q1) ----------
Hok = lambda w: (1 + 2 * math.cos(w)) / 3
Hbug = lambda w: 2 * math.cos(w) / 3
assert abs(abs(Hbug(math.pi)) - 2 / 3) < 1e-12 and abs(Hbug(math.pi / 2)) < 1e-12 and abs(Hok(2 * math.pi / 3)) < 1e-12 and abs(abs(Hok(math.pi)) - 1 / 3) < 1e-12
xs = [(-1) ** n for n in range(-3, 4)]
assert all(abs((xs[i - 1] + xs[i + 1]) / 3 + 2 / 3 * xs[i]) < 1e-12 for i in range(1, 6))   # alternating input comes back at -2/3
card(7, 8, "WORKED BENCHMARK", "Worked Benchmark: The Blur That Forgot Its Centre",
     freq_axis(ticks=((-math.pi, "−π"), (-math.pi / 2, "−π/2"), (0, "0"), (math.pi / 2, "π/2"), (math.pi, "π")))
     + [P(plot(Hok), w=1.2, dash="4 3"), P(plot(Hbug), w=1.8),
        L(24, 104 - 2 / 3 * 74, 216, 104 - 2 / 3 * 74, .5, d="1 2"),
        N(120, 125, "dashed: intended ⅓[1 1 1]   solid: bug ⅔|cos Ω|", 6.5),
        N(120, 134, "|Hₑ(0)| = |Hₑ(π)| = ⅔, and Hₑ(π/2) = 0", 6.8), N(120, 143, "not low-pass: the finest detail passes like DC", 6.8)],
     "The intended average has its first zero at 2π/3 and only 1/3 left at π. Dropping the centre tap gives (2/3)|cos Ω|: as large at π as at 0, with a zero at π/2.",
     ["<strong>The bug:</strong> the centre tap is missing, so $h_e[n]=\\frac13[1\\;\\;0\\;\\;1]$ with the $0$ at $n=0$.",
      "<strong>Its DSFT:</strong> $H_e(\\Omega)=\\frac13(e^{j\\Omega}+e^{-j\\Omega})=\\frac23\\cos\\Omega$.",
      "<strong>Verdict:</strong> $|H_e(0)|=|H_e(\\pi)|=\\frac23$, so it is <strong>not</strong> low-pass."],
     "$$h_e[n]=\\tfrac13[1\\;\\;0\\;\\;1]\\ \\Rightarrow\\ H_e(\\Omega)=\\tfrac23\\cos\\Omega,\\qquad |H_e(0)|=|H_e(\\pi)|=\\tfrac23,\\quad H_e(\\pi/2)=0$$",
     "<strong>The fence survives the blur.</strong> For a fence alternating $+1,-1$ along a row, each pixel's two neighbours are both the opposite value. Their average flips the pattern and keeps $\\frac23$ of its contrast, so the fence that a blur should erase is still there, inverted.",
     "Do not call it low-pass because it averages. Compare |H(0)| with |H(π)|. Also keep the 1/3: the buggy code still divides by 3, so its DC gain is 2/3 and the whole frame gets darker.",
     "EXAMPLE",
     stmt("A blur with a missing centre sample.",
          [ln("The intended filter is $h[n]=\\frac13[1\\;\\;1\\;\\;1]$, centred at $n=0$."),
           ln("A bug leaves the centre out of the sum, so"),
           ln("$h_e[n]=\\frac13\\big(\\delta[n+1]+\\delta[n-1]\\big)$.", 1),
           ln("Its DSFT is"),
           ln("$H_e(\\Omega)=\\frac13(e^{j\\Omega}+e^{-j\\Omega})=\\frac23\\cos\\Omega$.", 1),
           ln("Since $|H_e(0)|=|H_e(\\pi)|=\\frac23$ and $H_e(\\pi/2)=0$,"),
           ln("the filter is not low-pass.", 1)],
          "E9 241 Midterm 2 (2026), Problem 1"),
     "If a pixel is replaced by the average of its two neighbours only, what happens to a pattern that alternates every pixel?",
     ["<strong>$\\delta[n\\pm1]\\to e^{\\mp j\\Omega}$ = each tap is a shift.</strong> Adding the two shifts gives $2\\cos\\Omega$, and the factor $\\frac13$ makes it $\\frac23\\cos\\Omega$.",
      "<strong>$|H_e|=\\frac23|\\cos\\Omega|$ = the plot.</strong> It peaks at $\\Omega=0,\\pm\\pi$ and is zero at $\\pm\\pi/2$. The intended filter $\\frac13(1+2\\cos\\Omega)$ has $|H(\\pi)|=\\frac13$.",
      "<strong>$H_e(\\pi)=-\\frac23$ = inverted, not removed.</strong> The input $(-1)^n$ comes out as $-\\frac23(-1)^n$, so high frequencies are not attenuated relative to low ones."])

# ---------- 9.07 uniform quantizer ----------
A, K = 1.5, 4
D = 2 * A / K
levels = [-A + D * (i + .5) for i in range(K)]
Q = lambda x: levels[min(K - 1, int((x + A) // D))]
seq = [1.4, -1.1, .2, -.8, .3, 1.2]
assert D == .75 and levels == [-1.125, -.375, .375, 1.125] and [Q(x) for x in seq] == [1.125, -1.125, .375, -1.125, .375, 1.125]
stair = "M 32 118"
x0, sx, y0, sy = 120, 56, 62, 34
pts = []
for i, l in enumerate(levels):
    a, b = -A + i * D, -A + (i + 1) * D
    pts.append(L(round(x0 + a * sx, 1), round(y0 - l * sy, 1), round(x0 + b * sx, 1), round(y0 - l * sy, 1), 2))
    if i < K - 1:
        pts.append(L(round(x0 + b * sx, 1), round(y0 - l * sy, 1), round(x0 + b * sx, 1), round(y0 - levels[i + 1] * sy, 1), .7, d="2 2"))
    pts.append(N(round(x0 + (a + b) / 2 * sx, 1), round(y0 - l * sy - 3, 1), f"{l:+.3f}".replace("-", "−"), 5.8))
card(9, 7, "COMPRESSION", "The Uniform Quantizer",
     [L(30, y0, 214, y0, 1, ar=True), L(x0, 120, x0, 8, 1, ar=True), T(218, y0 + 3, "x", 8, a="end"), T(x0 + 5, 14, "Q(x)", 7.5, a="start")] + pts
     + [N(round(x0 - A * sx, 1), y0 + 10, "−1.5", 6.2), N(round(x0 + A * sx, 1), y0 + 10, "1.5", 6.2), N(round(x0 + .375 * sx, 1), y0 + 10, "Δ = 0.75", 6.2),
        N(120, 130, "4 levels: mid-riser, no level at 0", 7), N(120, 141, "1.4, −1.1, 0.2 → 1.125, −1.125, 0.375", 7)],
     "A 4-level uniform quantizer on [−1.5, 1.5]. Each interval has width Δ = 0.75 and every value in it is replaced by the interval's midpoint.",
     ["<strong>Staircase:</strong> $Q(x)=x_i$ for $x$ in interval $I_i$. The decoder knows the codebook, so only the index $i$ is sent.",
      "<strong>Uniform spacing:</strong> on $[-A,A]$ with $N$ intervals, $\\Delta=2A/N$ and each level is its interval's midpoint.",
      "<strong>Two shapes:</strong> mid-riser has an even number of levels and no zero level; mid-tread has an odd number and a level at $0$."],
     "$$\\Delta=\\frac{2A}{N},\\qquad Q(x)=x_i\\ \\text{ if }\\ x\\in\\Big[x_i-\\frac\\Delta2,\\ x_i+\\frac\\Delta2\\Big)$$",
     "<strong>Fewer grey shades for the frame.</strong> To save storage, the street camera rounds each value to the nearest allowed shade and sends only the shade's number. The rounding is the one step of compression that cannot be undone.",
     "N here is the number of intervals, not bits: r bits give N = 2ʳ. Levels are interval midpoints, so with 4 levels on [−1.5, 1.5] they are ±0.375 and ±1.125, not the edges ±0.75. Inputs beyond the range are overload.",
     "DEFINITION",
     stmt("Uniform quantizer.",
          [ln("A quantizer maps $x$ to a codebook value:"),
           ln("$Q(x)=x_i\\in\\{x_0,\\ldots,x_{N-1}\\}$.", 1),
           ln("It is uniform if $x_i-x_{i-1}=\\Delta$ for all $i$, and"),
           ln("$x\\in[x_i-\\frac\\Delta2,\\ x_i+\\frac\\Delta2)\\Rightarrow Q(x)=x_i$.", 1),
           ln("For the range $[-A,A]$ with $N$ intervals, $\\Delta=2A/N$."),
           ln("Mid-riser: even $N$, no zero level. Mid-tread: odd $N$, a level at $0$.")],
          "E9 241 Compression slides; Problem Set 4, Q4"),
     "With four shades on [−1.5, 1.5], which value should 0.2 become, and what does the decoder actually receive?",
     ["<strong>$\\Delta=(1.5-(-1.5))/4=0.75$ = interval width.</strong> The intervals start at $-1.5,-0.75,0,0.75$, so the levels are $-1.125,-0.375,0.375,1.125$.",
      "<strong>$1.4,-1.1,0.2,-0.8,0.3,1.2\\to1.125,-1.125,0.375,-1.125,0.375,1.125$ = the worked sequence.</strong> Note that $-0.8$ lies in $[-1.5,-0.75)$.",
      "<strong>A zero level = why mid-tread exists.</strong> Prediction residues and high DCT coefficients are near zero, and a level at $0$ sends them to exactly zero."])

# ---------- 9.08 quantization MSE ----------
card(9, 8, "COMPRESSION", "Quantization Error: Why MSE Is a Twelfth of Step Squared",
     [L(24, 96, 112, 96, 1, ar=True), L(68, 104, 68, 24, 1, ar=True), P("M 34 40 Q 68 128 102 40", w=1.6), L(34, 96, 34, 92, 1), L(102, 96, 102, 92, 1),
      N(34, 105, "−Δ/2", 6.4), N(102, 105, "Δ/2", 6.4), N(68, 20, "(x − xᵢ)²", 6.8), N(68, 116, "average over one cell", 6.6), N(68, 127, "= Δ²/12", 8, w="bold"),
      R(134, 26, 92, 15, "#ffffff", 1), R(157, 26, 46, 15, "#d9dee7", .8), N(180, 22, "right range [−A, A]", 6.3), N(180, 53, "Δ = 2A/N", 7),
      R(134, 70, 92, 15, "#ffffff", 1), R(157, 70, 46, 15, "#d9dee7", .8), L(180, 70, 180, 85, 1), N(180, 66, "wrong range [−2A, 2A]", 6.3), N(180, 97, "Δ = 4A/N, half the levels used", 6.2),
      N(180, 116, "MSE × 4 (−6 dB)", 7.5, w="bold"), N(180, 127, "same as losing one bit", 6.6)],
     "Inside one small cell the error is spread evenly over ±Δ/2, so its mean square is Δ²/12. Designing for twice the true range doubles Δ, so the MSE becomes four times larger.",
     ["<strong>High-resolution idea:</strong> with many levels, $f_X$ is nearly constant in a cell, so the error is uniform on $[-\\Delta/2,\\Delta/2]$.",
      "<strong>The integral:</strong> $\\frac1\\Delta\\int_{-\\Delta/2}^{\\Delta/2}s^2ds=\\frac{\\Delta^2}{12}$, the same for every cell of a uniform quantizer.",
      "<strong>Design:</strong> for unequal cells, $D=\\sum_iP_i\\Delta_i^2/12$, so put narrow cells where the probability is high."],
     "$$D=\\frac{\\Delta^2}{12},\\qquad \\Delta=\\frac{2A}{N}\\Rightarrow D=\\frac{A^2}{3N^2};\\qquad \\Delta=\\frac{4A}{N}\\Rightarrow D=\\frac{4A^2}{3N^2}$$",
     "<strong>Setting the range for the wrong street.</strong> If the camera's quantizer is set for brightness twice as wide as the street ever shows, half its shades are never used. The remaining shades are twice as far apart, and the rounding error power is four times larger.",
     "The answer has N², not N: (2A/N)²/12 = A²/(3N²). The handwritten Problem Set 4 solution drops the square in parts (b) and (c). Also, MSE depends on Δ, so a wider design range hurts even though no input overloads.",
     "THEOREM",
     stmt("High-resolution quantizer distortion.",
          [ln("If $f_X$ is nearly constant on each cell $I_i$ of width $\\Delta_i$, then"),
           ln("$D=\\mathbb E[(X-Q(X))^2]\\approx\\sum_iP_i\\dfrac{\\Delta_i^2}{12}$, with $P_i=\\mathbb P(X\\in I_i)$.", 1),
           ln("For a uniform quantizer with no overload,"),
           ln("$D\\approx\\dfrac{\\Delta^2}{12}$.", 1),
           ln("On $[-A,A]$ with $N$ intervals,"),
           ln("$\\Delta=\\dfrac{2A}N$ and $D\\approx\\dfrac{A^2}{3N^2}$.", 1)],
          "E9 241 Compression slides; Problem Set 4, Q4"),
     "If you design the quantizer for twice the real range, how many times larger does the error become?",
     ["<strong>$D_i=\\frac1\\Delta\\int_{-\\Delta/2}^{\\Delta/2}s^2ds=\\frac{\\Delta^2}{12}$ = error in one cell.</strong> Substitute $s=x-x_i$; the weights $P_i$ then add up to $1$.",
      "<strong>$[-2A,2A]\\Rightarrow\\Delta=4A/N,\\ D=\\frac{4A^2}{3N^2}$ = the misinformed engineer.</strong> The step doubles, so $D$ is $4$ times larger, a loss of $10\\log_{10}4\\approx6\\text{ dB}$.",
      "<strong>$N=2^r$ = about $6\\text{ dB}$ per bit.</strong> For $X$ uniform on $[-A,A]$, signal power is $A^2/3$, so $\\text{SNR}=N^2$, or $6.02\\,r\\text{ dB}$."])

# ---------- 9.09 entropy ----------
p = {"a0": .1, "a1": .07, "a2": .71, "a3": .09, "a4": .03}
Hx = -sum(v * math.log2(v) for v in p.values())
assert abs(sum(p.values()) - 1) < 1e-12 and abs(Hx - 1.416) < .001
bx = lambda v: -v * math.log2(v)
parts = []
for i, (a, v) in enumerate(sorted(p.items(), key=lambda kv: -kv[1])):
    x, h = 22 + i * 25, v * 78
    parts += [R(x, round(104 - h, 1), 17, round(h, 1), "#d9dee7", 1), N(x + 8.5, 113, a.replace("a", "a"), 6.5), N(x + 8.5, round(100 - h, 1), f"{v:.2f}", 5.8)]
parts += [L(16, 104, 150, 104, 1), N(82, 20, "p(a): one symbol dominates", 6.6),
          N(196, 34, "H = Σ p log₂(1/p)", 6.8), N(196, 50, f"≈ {Hx:.3f} bits", 8, w="bold"), N(196, 68, "fixed length:", 6.5), N(196, 78, "⌈log₂ 5⌉ = 3 bits", 7),
          N(196, 96, "best code:", 6.5), N(196, 106, "H ≤ ℓ̄ < H + 1", 7.2), N(120, 130, "a rare symbol carries more information", 7), N(120, 141, "so it can afford a longer codeword", 7)]
card(9, 9, "COMPRESSION", "Entropy: The Floor for Lossless Coding",
     parts,
     "The Problem Set 4 source has five symbols, with a2 at 0.71. Its entropy is about 1.416 bits per symbol, well below the 3 bits a fixed-length code would use.",
     ["<strong>Information of one symbol:</strong> $\\log_2\\frac1{p(x)}$. A rare symbol tells you more.",
      "<strong>Entropy:</strong> $H(X)=\\sum_xp(x)\\log_2\\frac1{p(x)}$ is the average information per symbol, in bits.",
      "<strong>Sandwich:</strong> every uniquely decodable code has $\\bar\\ell\\ge H$, and the best one has $\\bar\\ell_{\\text{opt}}\\lt H+1$."],
     "$$H(X)=\\sum_{x}p(x)\\log_2\\frac1{p(x)},\\qquad H\\le\\bar\\ell_{\\text{opt}}\\lt H+1$$",
     "<strong>A quiet street is cheap to describe.</strong> If most quantized DCT values from the camera are the same value, seeing one more tells you little. A busy scene with evenly spread values has higher entropy and needs more bits.",
     "Use log base 2 for bits. Entropy depends only on the probabilities, not on the symbols' values. H is a lower bound on the average length; an individual codeword can be shorter or longer than log₂(1/p). Prefix is sufficient for unique decodability, not necessary.",
     "THEOREM",
     stmt("Entropy and the lossless coding bounds.",
          [ln("For $X$ on a finite alphabet $\\mathcal A$,"),
           ln("$H(X)=\\sum_{x\\in\\mathcal A}p(x)\\log_2\\dfrac1{p(x)}$ bits.", 1),
           ln("A code has average length $\\bar\\ell=\\sum_ap(a)\\ell(a)$."),
           ln("Any uniquely decodable code has $\\bar\\ell\\ge H(X)$."),
           ln("The best one satisfies $H\\le\\bar\\ell_{\\text{opt}}\\lt H+1$."),
           ln("Prefix condition: no codeword begins another, which is enough for unique decoding.")],
          "E9 241 Compression slides (Shannon, 1948)"),
     "Why can a source with five symbols need far fewer than log₂ 5 bits per symbol on average?",
     ["<strong>$p\\log_2(1/p)$ = each symbol's share.</strong> For Problem Set 4: "
      + "$" + "+".join(f"{bx(v):.3f}" for v in p.values()) + f"\\approx{Hx:.3f}$ bits.",
      "<strong>$H\\le\\log_2|\\mathcal A|$ = uniform is the worst case.</strong> Equality holds only when all symbols are equally likely; here $\\log_25\\approx2.32$.",
      "<strong>Prefix code = decode as bits arrive.</strong> With $0,10,110,111$, the stream $01010111$ can only be $a_0a_1a_1a_3$. The code $0,10,101,0101$ is ambiguous."])

# ---------- 9.10 Huffman ----------
code = {"a0": "100", "a1": "110", "a2": "0", "a3": "101", "a4": "111"}
lbar = sum(p[a] * len(c) for a, c in code.items())
assert abs(lbar - 1.58) < 1e-12 and abs(lbar - Hx - .164) < .001
assert all(not (a != b and code[b].startswith(code[a])) for a in code for b in code)
inv = {c: a for a, c in code.items()}
bits, out, cur = "10100100111110110", [], ""
for b in bits:
    cur += b
    if cur in inv:
        out.append(inv[cur]); cur = ""
assert out == ["a3", "a2", "a2", "a0", "a4", "a1", "a1"] and cur == ""
heap = [(v, i, [a]) for i, (a, v) in enumerate(p.items())]
heapq.heapify(heap); ln_h = dict.fromkeys(p, 0); nxt = len(heap)
while len(heap) > 1:
    a, b = heapq.heappop(heap), heapq.heappop(heap)
    for s in a[2] + b[2]:
        ln_h[s] += 1
    heapq.heappush(heap, (a[0] + b[0], nxt, a[2] + b[2])); nxt += 1
assert abs(sum(p[a] * ln_h[a] for a in p) - 1.58) < 1e-12     # an independent Huffman run reaches the same average length
alt = {"a2": 1, "a0": 2, "a3": 3, "a1": 4, "a4": 4}
assert abs(sum(p[a] * alt[a] for a in p) - 1.58) < 1e-12      # the other tie-break
leaf = {"a0": 30, "a3": 72, "a1": 114, "a4": 156, "a2": 204}
ny = 96
tree = [L(30, ny, 51, 72, 1), L(72, ny, 51, 72, 1), L(114, ny, 135, 72, 1), L(156, ny, 135, 72, 1), L(51, 72, 93, 46, 1), L(135, 72, 93, 46, 1), L(93, 46, 148, 22, 1), L(204, ny, 148, 22, 1),
        C(51, 72, 2), C(135, 72, 2), C(93, 46, 2), C(148, 22, 2),
        N(36, 84, "0", 6), N(67, 84, "1", 6), N(120, 84, "0", 6), N(150, 84, "1", 6), N(67, 58, "0", 6), N(119, 58, "1", 6), N(116, 32, "1", 6), N(181, 56, "0", 6),
        N(51, 67, ".19", 6), N(135, 67, ".10", 6), N(93, 41, ".29", 6), N(148, 17, "1", 6)]
for a, x in leaf.items():
    tree += [R(x - 15, ny, 30, 25, "#ffffff", .9), N(x, ny + 8, f"{a} ({p[a]:.2f})".replace("0.", "."), 5.4), N(x, ny + 19, code[a], 7, w="bold")]
tree += [N(120, 134, f"ℓ̄ = 0.71(1) + 0.29(3) = 1.58 bits", 7), N(120, 143, f"H ≈ {Hx:.3f}, redundancy ≈ {lbar - Hx:.3f}", 6.6)]
card(9, 10, "WORKED BENCHMARK", "Worked Benchmark: Building a Huffman Code",
     tree,
     "Merge the two least likely nodes until one remains, then read each codeword from the root. The common symbol a2 gets one bit and the rest get three.",
     ["<strong>Merge:</strong> repeatedly join the two least probable nodes into a parent whose probability is their sum.",
      "<strong>Read back:</strong> label the two branches of every merge $0$ and $1$; a symbol's codeword is the path from root to leaf.",
      "<strong>Result:</strong> Huffman gives the smallest $\\bar\\ell$ of any symbol-by-symbol prefix code."],
     "$$\\bar\\ell=\\sum_ap(a)\\ell(a)=0.71(1)+0.29(3)=1.58,\\qquad \\bar\\ell-H\\approx0.164\\text{ bits}$$",
     "<strong>The usual shade gets the short name.</strong> After quantizing, the camera's most common value gets the single bit $0$, while rare values get three bits. Over a whole frame, the file is about half the size of a fixed 3-bit code.",
     "When probabilities tie, the tree can differ: another valid code here has lengths 1, 2, 3, 4, 4. The average length is still 1.58. To decode, use the same codebook as the encoder, because the codewords depend on the tie-breaks.",
     "EXAMPLE",
     stmt("Huffman code for a 5-letter source.",
          [ln("$p(a_0,\\ldots,a_4)=(0.1,\\ 0.07,\\ 0.71,\\ 0.09,\\ 0.03)$."),
           ln("Merges: $.03+.07=.10$, $\\ .09+.10=.19$, $\\ .10+.19=.29$, $\\ .29+.71=1$."),
           ln("One optimal code:"),
           ln("$a_0{:}\\,100,\\ \\ a_1{:}\\,110,\\ \\ a_2{:}\\,0,\\ \\ a_3{:}\\,101,\\ \\ a_4{:}\\,111$.", 1),
           ln(f"$\\bar\\ell=1.58$ bits, $H\\approx{Hx:.3f}$ bits, redundancy $\\approx{lbar - Hx:.3f}$ bits."),
           ln("The bits $10100100111110110$ decode to"),
           ln("$a_3\\,a_2\\,a_2\\,a_0\\,a_4\\,a_1\\,a_1$.", 1)],
          "Problem Set 4, Q5"),
     "Which two symbols do you merge first, and how do you read the codewords once the tree is built?",
     ["<strong>Two smallest first = the optimal structure.</strong> The two rarest symbols have the longest codewords, of equal length, so they can be sibling leaves.",
      "<strong>$\\bar\\ell-H\\approx0.164$ = the redundancy left.</strong> It is above $0$ because a codeword needs a whole number of bits, while $\\log_2(1/0.71)\\approx0.49$.",
      "<strong>$101\\,|\\,0\\,|\\,0\\,|\\,100\\,|\\,111\\,|\\,110\\,|\\,110$ = decoding.</strong> Read until a codeword completes, output it and restart. The prefix property means no cut is ambiguous."])

# ---------- write ----------
path = os.path.join(ROOT, "cards_dip.js")
text = open(path, encoding="utf-8").read()
i, j = re.search(r"\[\s*\{", text).start(), text.rindex("]") + 1
m = {c["id"]: c for c in json.loads(text[i:j])}
m.update({c["id"]: c for c in cards})
out_cards = sorted(m.values(), key=lambda c: c["id"])
open(path, "w", encoding="utf-8").write(text[:i] + json.dumps(out_cards, indent=2) + text[j:])
print(f"cards_dip.js: {len(out_cards)} cards ({len(cards)} written)")
