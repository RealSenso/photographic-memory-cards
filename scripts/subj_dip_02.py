"""DIP topic 02 (colour) in the CMO card format. Everyday picture: a street camera on a pole."""
from street_lib import *

SUBJECT = "DIP"

def d3011(c):
    b = 96
    return svg(c,
        axes(14, b, 150, 14), N(150, b + 10, "λ", 8, "end"),
        bell(24, 146, 60, 22, 60, b), N(40, 30, "S", 8), bell(24, 146, 84, 24, 70, b), N(88, 26, "M", 8), bell(24, 146, 104, 24, 66, b), N(122, 34, "L", 8),
        N(80, 110, "three cone-like channels of the camera", 7),
        R(160, 22, 70, 44, "#f1f5f9", 1), N(195, 36, "bus light", 7), N(195, 48, "= R·R + G·G", 7), N(195, 59, "+ B·B", 7),
        R(160, 76, 70, 32, "#ffffff", 1), N(195, 88, "α·C₁ ≡ α·C₂", 7), N(195, 100, "C₁+C₃ ≡ C₂+C₃", 7),
        N(120, 136, "any light ⇒ just three numbers (R, G, B)", 7.5))

def d3012(c):
    b = 90
    return svg(c,
        axes(14, b, 150, 14), N(150, b + 10, "λ", 8, "end"),
        bell(24, 146, 70, 18, 50, b, 1, "3 2"), N(40, 40, "z̄", 8), bell(24, 146, 92, 20, 70, b), N(92, 20, "ȳ", 8), bell(24, 146, 112, 18, 56, b, 1, "1 2"), N(132, 42, "x̄", 8),
        curve(lambda x: 74 - 24 * math.exp(-((x - 92) / 26) ** 2) - 6 * math.exp(-((x - 60) / 18) ** 2), 24, 146, 50, .8, "1 2"), N(28, 66, "P(λ)", 7, "start"),
        R(160, 22, 70, 62, "#f1f5f9", 1), N(195, 36, "X = ∫P·x̄ dλ", 7), N(195, 52, "Y = ∫P·ȳ dλ", 7), N(195, 68, "Z = ∫P·z̄ dλ", 7),
        N(195, 99, "Y alone = brightness", 7), N(120, 130, "the street lamp's spectrum P(λ) weighed three ways", 7.5))

def d3013(c):
    locus = [(.1741,.0050),(.1440,.0297),(.1241,.0578),(.0913,.1327),(.0454,.2950),(.0082,.5384),(.0139,.7502),(.0743,.8338),(.1547,.8059),
             (.2296,.7543),(.3016,.6923),(.3731,.6245),(.4441,.5547),(.5125,.4866),(.5752,.4242),(.6270,.3725),(.6915,.3083),(.7347,.2653)]
    X = lambda x: 18 + x * 150
    Y = lambda y: 122 - y * 118
    pts = lambda L_: " ".join(f"{f(X(a))},{f(Y(b))}" for a, b in L_)
    return svg(c,
        axes(18, 122, 146, 10), N(146, 131, "x", 8, "end"), N(11, 16, "y", 8, "start"),
        PG(pts(locus), "none", 1),
        N(33, 21, "green 520", 6.5, "start"), N(130, 89, "red", 6.5, "start"), N(130, 97, "700", 6.5, "start"), N(44, 131, "violet 380", 6.5),
        PG(pts([(.64,.33),(.30,.60),(.15,.06)]), "none", 1, "3 2"),
        L(96, 44, 88.5, 67, .6), N(92, 41, "screen gamut", 6.5, "start"),
        C(f(X(.3127)), f(Y(.3290)), 1.8, "#ffffff"), N(69, 91, "white", 6.5, "start"),
        R(150, 18, 80, 76, "#f1f5f9", 1), N(190, 32, "x = X/(X+Y+Z)", 7), N(190, 46, "y = Y/(X+Y+Z)", 7), N(190, 60, "z = 1 − x − y", 7), N(190, 78, "no brightness left", 7),
        N(120, 141, "the red bus and its sign live on this map", 7.5))

def d3014(c):
    return svg(c,
        frame(14, 22, 44, 32, "frame"), N(36, 42, "R G B", 7),
        arrow(60, 38, 82, 38, 1), R(82, 22, 40, 32, "#f1f5f9", 1), N(102, 36, "3×3", 8), N(102, 46, "matrix", 6.5),
        arrow(122, 38, 140, 38, 1), frame(140, 14, 40, 32, None, "#d9dee7"), N(160, 33, "Y", 8), frame(190, 14, 20, 16), N(200, 25, "C_b".replace("_b", "ᵦ") if False else "Cb", 6.5), frame(190, 34, 20, 16), N(200, 45, "Cr", 6.5),
        N(160, 62, "full size", 6.5), N(200, 62, "half size", 6.5),
        L(14, 80, 226, 80, .6, "1 3"),
        N(120, 96, "Y = 0.299 R + 0.587 G + 0.114 B", 7.5),
        N(120, 108, "Cb = −0.169 R − 0.331 G + 0.5 B", 7.5), N(120, 120, "Cr = 0.5 R − 0.419 G − 0.081 B", 7.5),
        N(120, 136, "keep every Y pixel, share the colour (4:2:0)", 7.5))

def d3015(c):
    cx, cy, r = 70, 76, 48
    out = [circ(cx, cy, r, "none", 1), circ(cx, cy, 3, "#ffffff", 1)]
    for a, lab, lx, ly, anc in ((0, "R 0°", 120, 72, "start"), (120, "G 120°", 42, 32, "end"), (240, "B 240°", 42, 126, "end")):
        x, y = cx + r * math.cos(math.radians(a)), cy - r * math.sin(math.radians(a))
        out += [L(f(cx), f(cy), f(x), f(y), .6, "1 3"), N(lx, ly, lab, 7, anc)]
    h = math.radians(50)
    px, py = cx + 34 * math.cos(h), cy - 34 * math.sin(h)
    ax, ay = cx + 16 * math.cos(h), cy - 16 * math.sin(h)
    out += [arrow(cx, cy, px, py, 1), C(f(px), f(py), 2), N(px + 4, py - 2, "colour", 7, "start"),
            P(f"M{cx + 16},{cy} A16,16 0 0 0 {f(ax)},{f(ay)}", "none", .8), N(cx + 19, cy - 5, "H", 8, "start"),
            N(cx + 5, cy + 13, "S = arrow length", 6.5, "start"),
            R(138, 20, 90, 24, "#f1f5f9", 1), N(183, 36, "I = (R+G+B)/3", 7.5),
            R(138, 52, 90, 24, "#f1f5f9", 1), N(183, 68, "S = 1 − 3·min/(R+G+B)", 6.5),
            R(138, 84, 90, 24, "#f1f5f9", 1), N(183, 100, "H = angle θ (or 360° − θ)", 6.5),
            N(120, 138, "grey ⇒ S = 0 ⇒ hue undefined", 7.5)]
    return svg(c, *out)

def d3016(c):
    return svg(c,
        R(10, 18, 40, 34, "#d9dee7", 1), N(30, 38, "pure", 7), N(30, 47, "red", 7), N(30, 14, "(255, 0, 0)", 6.5),
        arrow(52, 35, 70, 35, 1),
        R(72, 26, 46, 18, "#f1f5f9", 1), N(95, 38, "Y = 76.2", 7), R(124, 26, 46, 18, "#f1f5f9", 1), N(147, 38, "Cb = −43", 7), R(176, 26, 52, 18, "#f1f5f9", 1), N(202, 38, "Cr = 127.5", 7),
        N(120, 62, "+128 for 8-bit storage", 7.5),
        L(40, 122, 226, 122, 1), N(40, 134, "0", 7), N(226, 134, "255", 7, "end"),
        R(40, 76, 55, 10, "#d9dee7", .8), N(100, 85, "Y ≈ 76", 7, "start"),
        R(40, 90, 62, 10, "#f1f5f9", .8), N(107, 99, "Cb ≈ 85", 7, "start"),
        R(40, 104, 186, 10, "#d9dee7", .8), N(44, 113, "Cr ≈ 255 (clipped)", 7, "start"))

CARDS = {
3011: dict(d=d3011, stmtKind="THEOREM",
  statement=r"<b>Trichromacy and Grassmann's laws.</b> For normal human vision, any colour stimulus $C$ can be matched by a mixture of three fixed primaries: $C\equiv R\,\mathbf R+G\,\mathbf G+B\,\mathbf B$, where $\equiv$ means “looks the same” and an amount may be negative (that primary is then added to the $C$ side). Matching is linear (Grassmann): if $C_1\equiv C_2$ then $\alpha C_1\equiv\alpha C_2$ for $\alpha\gt 0$, and $C_1+C_3\equiv C_2+C_3$ for any $C_3$.",
  hint="Why can a red bus and a differently-made red light look identical to the street camera?",
  breakdown=[r"<strong>$R\,\mathbf R+G\,\mathbf G+B\,\mathbf B$ = three dials.</strong> Whatever the light, the camera's three channels report one amount for each primary; those three amounts are all it keeps.",
             r"<strong>$\alpha C_1\equiv\alpha C_2$ = turning the light up keeps a match.</strong> If two lights match, making both twice as bright still matches.",
             r"<strong>$C_1+C_3\equiv C_2+C_3$ = adding the same light to both keeps a match.</strong> Together these make colour mixing linear, so every colour-space change is a $3\times3$ matrix."],
  conn=r"<strong>The red bus and its sign.</strong> The bus paint and the traffic sign send very different spectra to the camera, but the three channels give the same three numbers, so the frame stores them as the same red. Same numbers, different spectra: a metamer.",
  cap="The camera's three channels S, M, L weigh the bus light's spectrum into three numbers R, G, B. Scaling (αC₁ ≡ αC₂) and adding a common light (C₁+C₃ ≡ C₂+C₃) keep a match."),
3012: dict(d=d3012, stmtKind="DEFINITION",
  statement=r"<b>CIE XYZ tristimulus values.</b> The CIE 1931 colour-matching functions $\bar x(\lambda),\bar y(\lambda),\bar z(\lambda)\ge0$ define, for a light with spectral power distribution $P(\lambda)$, the tristimulus values $X=\int P(\lambda)\bar x(\lambda)\,d\lambda$, $Y=\int P(\lambda)\bar y(\lambda)\,d\lambda$, $Z=\int P(\lambda)\bar z(\lambda)\,d\lambda$, with $\bar y$ equal to the luminous efficiency function, so $Y$ is luminance.",
  hint="Why did the CIE invent three imaginary primaries instead of using the red, green and blue lamps they had?",
  breakdown=[r"<strong>$P(\lambda)$ = the lamp's spectrum.</strong> How much power the street lamp, bus or sign sends out at each wavelength.",
             r"<strong>$\bar x,\bar y,\bar z$ = three fixed weighing curves.</strong> They are never negative (real red-green-blue lamps needed a negative red), which is why the primaries are imaginary.",
             r"<strong>$\int P\,\bar y\,d\lambda=Y$ = brightness.</strong> Each of $X,Y,Z$ is just an inner product of the spectrum with one curve; $\bar y$ was chosen to match how bright the eye finds each wavelength."],
  conn=r"<strong>Weighing the street lamp three ways.</strong> The lamp's spectrum is laid over three curves and each total is one number. The second curve is the eye's brightness curve, so that total says how bright the lamp looks on the camera's frame.",
  cap="The lamp spectrum P(λ) is weighed against three curves x̄, ȳ, z̄ to give X, Y, Z. The middle total Y alone is the brightness."),
3013: dict(d=d3013, stmtKind="DEFINITION",
  statement=r"<b>CIE chromaticity coordinates.</b> For tristimulus values $(X,Y,Z)$ the chromaticity coordinates are $x=\dfrac{X}{X+Y+Z}$, $y=\dfrac{Y}{X+Y+Z}$, $z=1-x-y$. The set of $(x,y)$ of monochromatic lights is the spectral locus (a horseshoe); the colours reproducible by three primaries are the points inside the triangle of their chromaticities, the gamut, and mixtures of two colours lie on the segment joining them.",
  hint="After you divide out brightness, what is left on the map, and where does the screen's gamut sit?",
  breakdown=[r"<strong>$x=X/(X+Y+Z),\ y=Y/(X+Y+Z)$ = the colour's share of each primary.</strong> Dividing by the total throws brightness away, leaving pure hue and purity.",
             r"<strong>$z=1-x-y$ = the third share.</strong> The three shares add to 1, so two numbers are enough to place the colour on a flat map.",
             r"<strong>The triangle inside the horseshoe = the screen's gamut.</strong> Three primaries can only make colours inside the triangle joining them, and a mix of two lies on the straight line between them.",
             r"<strong>$\mathbf c_m=\frac{S_1\mathbf c_1+S_2\mathbf c_2}{S_1+S_2}$, $S_i=X_i+Y_i+Z_i$ = where a mixture lands.</strong> Tristimulus values add, so the mixture's chromaticity is a weighted average of the two: it lies on the segment joining them, pulled toward the source with the larger total $S$."],
  conn=r"<strong>Which reds the camera can show.</strong> The bus red and the sign red are two points on this map. The monitor showing the street frame can only reproduce points inside its triangle, so a very saturated colour on the street may be pulled inward.",
  cap="The horseshoe is the spectral locus on the (x, y) map; x = X/(X+Y+Z), y = Y/(X+Y+Z). The dashed triangle is the screen's gamut and white sits near the middle."),
3014: dict(d=d3014, stmtKind="ALGORITHM",
  statement=r"<b>RGB to YCbCr (ITU-R BT.601) and chroma subsampling.</b> $\begin{pmatrix}Y\\C_b\\C_r\end{pmatrix}=\begin{pmatrix}0.299&0.587&0.114\\-0.1687&-0.3313&0.5\\0.5&-0.4187&-0.0813\end{pmatrix}\begin{pmatrix}R\\G\\B\end{pmatrix}$, with $128$ added to $C_b,C_r$ for 8-bit storage. In 4:2:0 subsampling $Y$ is kept at full resolution while $C_b$ and $C_r$ are each stored at half resolution in both directions.",
  hint="Which part of the street frame must stay sharp, and which part can be stored at half size without anyone noticing?",
  breakdown=[r"<strong>$Y$ row $(0.299,0.587,0.114)$ = the brightness picture.</strong> Green is weighted most because the eye finds it brightest; this plane alone is the black-and-white frame.",
             r"<strong>$C_b,C_r$ rows = blue-minus-brightness and red-minus-brightness.</strong> Each row sums to zero, so a grey pixel gives $C_b=C_r=0$ (128 after the offset).",
             r"<strong>Half-size $C_b,C_r$ = the saving.</strong> The eye sees fine detail in brightness but not in colour, so the recorder keeps every $Y$ pixel and shares each colour sample among four.",
             r"<strong>$4+1+1=6$ samples per $2\times2$ block, against $12$ = the 4:2:0 saving.</strong> That is 12 bits per pixel instead of 24, a 50% reduction at any frame size."],
  conn=r"<strong>Fitting more street on the recorder.</strong> The camera's recorder stores the black-and-white picture at full detail and the two colour pictures at half size. The shop sign stays crisp; only the colour fringes on its edges are coarser.",
  cap="The R, G, B frame goes through a 3×3 matrix to a full-size Y plane and two half-size colour planes Cb, Cr (4:2:0)."),
3015: dict(d=d3015, stmtKind="DEFINITION",
  statement=r"<b>HSI colour model.</b> For $R,G,B\in[0,1]$: $I=\frac{R+G+B}{3}$, $S=1-\frac{3\min(R,G,B)}{R+G+B}$, and $H=\theta$ if $B\le G$, $H=360^\circ-\theta$ if $B\gt G$, where $\theta=\cos^{-1}\!\Big(\frac{\frac12[(R-G)+(R-B)]}{\sqrt{(R-G)^2+(R-B)(G-B)}}\Big)$. Hue is undefined when $S=0$, saturation is undefined when $I=0$.",
  hint="If you make the night frame brighter, which of hue, saturation and intensity should not move?",
  breakdown=[r"<strong>$I=(R+G+B)/3$ = brightness.</strong> The plain average of the three channels, the grey level of the pixel.",
             r"<strong>$S=1-3\min(R,G,B)/(R+G+B)$ = distance from grey.</strong> Take away the grey part (the smallest channel) and see how much is left: a grey pixel has $S=0$.",
             r"<strong>$H=\theta$ or $360^\circ-\theta$ = the angle on the colour wheel.</strong> It names which pure colour (red, green, blue, ...) and does not change when brightness changes.",
             r"<strong>$(R,G,B)\to\alpha(R,G,B)$ leaves $H,S$ unchanged.</strong> In $\theta$ the top and bottom both scale by $\alpha$, and in $S$ so do $\min(R,G,B)$ and $R+G+B$; only $I$ becomes $\alpha I$."],
  conn=r"<strong>Brighten the night frame, keep the bus red.</strong> Work on $I$ alone: the dim bus gets brighter and stays the same red, because hue and saturation are not touched.",
  cap="A colour on the wheel: the arrow's angle is the hue H and its length is the saturation S; I = (R+G+B)/3 is the brightness. Grey has S = 0, so its hue is undefined."),
3016: dict(d=d3016, stmtKind="WORKED EXAMPLE",
  statement=r"<b>Example.</b> Convert pure red $(R,G,B)=(255,0,0)$ with the BT.601 matrix: $Y=0.299\cdot255=76.2$, $C_b=-0.1687\cdot255=-43.0$, $C_r=0.5\cdot255=127.5$. With the 8-bit offset $C_b=128-43=85$ and $C_r=128+127.5=255.5$, clipped to $255$.",
  hint="Where does the red bus land on the Y, Cb, Cr scales?",
  breakdown=[r"<strong>$Y=0.299\cdot255\approx76.2$ = red is a dark-ish grey.</strong> Only 30% of its weight goes to brightness; most of the pixel's story is in the colour planes.",
             r"<strong>$C_b=-0.1687\cdot255\approx-43$ = no blue.</strong> Below the neutral 0, so after the offset it is about 85.",
             r"<strong>$C_r=0.5\cdot255=127.5$ = the most red anyone can have.</strong> The top of the scale, so red sits at the maximum of $C_r$ (255 once stored)."],
  conn=r"<strong>The red bus in the recorder.</strong> Its Y value is mid-low, its Cb is low and its Cr is at the ceiling. A dim red bus at night has all three scaled down: $C_r$ stays above the neutral 128, but by less.",
  cap="The bus red (255, 0, 0) becomes Y = 76.2, Cb = −43, Cr = 127.5; adding 128 for storage gives Cb ≈ 85 and Cr ≈ 255."),
}

STORY = {
 3011: dict(s="STORY 1 · STEP 7 · SEEING COLOUR", b="Every pixel the street camera saves is <b>three numbers</b>, because only three channels weigh the light and matching them is linear.",
   f=[["40106", "after geometry: what each pixel holds"]], n=[["3012", "a standard set of three weights"], ["3014", "turn them into brightness and colour"]]),
 3012: dict(s="STORY 1 · STEP 8 · A STANDARD RULER", b="The CIE gives three fixed weighing curves, so any lamp spectrum becomes <b>X, Y, Z</b>, with Y the brightness.",
   f=[["3011", "three channels"]], n=[["3013", "drop the brightness to get a colour map"]]),
 3013: dict(s="STORY 1 · STEP 9 · THE COLOUR MAP", b="Dividing by $X+Y+Z$ leaves a flat map of <b>pure colour</b>, and a screen's gamut is a triangle on it.",
   f=[["3012", "X, Y, Z"]], n=[["3014", "a practical split of brightness and colour"], ["3015", "the colour wheel view"]]),
 3014: dict(s="STORY 1 · STEP 10 · BRIGHTNESS VS COLOUR", b="A fixed matrix splits the frame into a sharp <b>Y</b> plane and two colour planes that can be stored at half size.",
   f=[["3011", "linear mixing"]], n=[["3016", "a worked number"], ["3022", "brightness work on Y only"], ["3082", "JPEG uses this split"]]),
 3015: dict(s="STORY 1 · STEP 11 · NAMING COLOUR", b="The HSI view says <b>which colour, how pure, how bright</b>, so brightness can be changed alone.",
   f=[["3013", "pure colour"]], n=[["3041", "equalise only the intensity I"]]),
 3016: dict(s="STORY 1 · STEP 12 · ONE NUMBER CHECK", b="Pure red worked through the matrix: <b>low Y, low Cb, maximum Cr</b>.",
   f=[["3014", "the matrix"]], n=[["3021", "next: the brightness histogram of the frame"]]),
}
FIX = build_fix(CARDS)
