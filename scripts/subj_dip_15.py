"""DIP topic 15 (Hough transform). Everyday picture: a street camera on a pole (lane lines and round signs)."""
from street_lib import *

SUBJECT = "DIP"

def d3141(c):
    O = (30, 112)
    th = math.radians(55); rho = 60
    px, py = O[0] + rho * math.cos(th), O[1] - rho * math.sin(th)
    dx, dy = -math.sin(th), -math.cos(th)
    return svg(c,
        axes(O[0], O[1], 150, 14), N(150, 122, "x", 7, "end"), N(24, 14, "y", 7, "end"),
        L(f(px - 80 * dx * -1 * -1), f(py - 80 * dy), f(px + 80 * dx), f(py + 80 * dy), 1.2) if False else L(f(px - 70 * dx), f(py - 70 * dy), f(px + 70 * dx), f(py + 70 * dy), 1),
        N(px + 36 * dx + 6, py + 36 * dy, "lane line", 7, "start"),
        arrow(O[0], O[1], px, py, 1), N(O[0] + 6, O[1] - 38, "ρ", 8, "start"), 
        P(f"M{O[0] + 18},{O[1]} A18,18 0 0 0 {O[0] + 18 * math.cos(th):.1f},{O[1] - 18 * math.sin(th):.1f}", "none", .8), N(O[0] + 22, O[1] - 6, "θ", 8, "start"),
        R(160, 20, 70, 74, "#f1f5f9", 1), N(195, 36, "ρ = x cosθ", 7.5), N(195, 48, "+ y sinθ", 7.5), N(195, 68, "no slope: vertical", 6.5), N(195, 80, "lines are fine", 6.5),
        N(120, 140, "every line is one point (ρ, θ)", 7.5))

def d3142(c):
    pts = ((18, 15), (44, 37), (70, 59))     # the three dots, measured from the origin at (12, 100)
    X0, W, Y0, K = 120, 110, 61, .45
    rho = lambda p, x: Y0 - K * (p[0] * math.cos((x - X0) / W * math.pi) + p[1] * math.sin((x - X0) / W * math.pi))
    th = math.atan2(26, -22)
    xc, yc = X0 + W * th / math.pi, rho(pts[1], X0 + W * th / math.pi)
    return svg(c,
        N(54, 10, "edge points of a lane line", 7), L(12, 100, 100, 26, 1, "3 2"), C(30, 85, 2.2), C(56, 63, 2.2), C(82, 41, 2.2), N(60, 112, "3 edge points", 7),
        N(176, 10, "accumulator A[ρ, θ]", 7), R(120, 16, 110, 90, "#ffffff", 1), N(124, 116, "θ: 0 → 180°", 7, "start"), N(117, 22, "ρ", 7, "end"),
        L(120, Y0, 230, Y0, .4, "1 3"),
        curve(lambda x: rho(pts[0], x), 120, 230, 50, 1, "1 2"), curve(lambda x: rho(pts[1], x), 120, 230, 50, 1, "3 2"), curve(lambda x: rho(pts[2], x), 120, 230, 50, 1),
        C(f(xc), f(yc), 2.6, "#ffffff"), N(xc - 5, yc + 13, "3 votes", 7, "end"),
        N(120, 128, "A[ρ, θ] += 1 for each point and each θ", 7.5), N(120, 140, "sinusoids that cross in one cell ⇒ one line", 7.5))

def d3143(c):
    out = []
    labs = [("1 edges", "Canny"), ("2 vote", "A[ρ,θ]++"), ("3 peaks", "A ≥ τ"), ("4 lines", "(ρ, θ) → y")]
    for i, (a, b) in enumerate(labs):
        x = 8 + i * 58
        out += [R(x, 14, 50, 36, "#f1f5f9", 1), N(x + 25, 28, a, 7), N(x + 25, 42, b, 6.5)]
        if i < 3: out.append(arrow(x + 50, 32, x + 58, 32, 1))
    out += [N(120, 74, "lines = { (ρ, θ) : A[ρ, θ] ≥ τ and a local maximum }", 7.5),
            N(120, 90, "speed-up: use the gradient angle, vote for one θ per pixel", 7.5),
            N(120, 108, "a peak is an endless line, not a segment", 7.5), N(120, 122, "two far-apart collinear pieces share one cell", 7.5),
            N(120, 138, "robust to gaps and noise: no connectivity needed", 7.5)]
    return svg(c, *out)

def d3144(c):
    cx, cy, r = 70, 58, 20
    out = [circ(cx, cy, r, "#d9dee7", 1), C(f(cx), f(cy), 2.4), N(cx, cy + 12, "(a, b)", 7)]
    for a in (20, 110, 200, 290):
        x, y = cx + r * math.cos(math.radians(a)), cy - r * math.sin(math.radians(a))
        out += [C(f(x), f(y), 1.8), circ(x, y, r, "none", .5, "2 3")]
    x, y = cx + r * math.cos(math.radians(20)), cy - r * math.sin(math.radians(20))
    out += [arrow(x, y, x + 16 * math.cos(math.radians(20)), y - 16 * math.sin(math.radians(20)), 1), N(x + 17, y - 11, "∇f", 7, "start"),
            N(70, 112, "dark disc: ∇f points out", 7), N(70, 122, "each rim point votes for a ring", 7),
            R(140, 16, 90, 78, "#f1f5f9", 1), N(185, 29, "(x−a)² + (y−b)² = r²", 7), N(185, 44, "a = x ∓ r cosθ", 7.5), N(185, 56, "b = y ∓ r sinθ", 7.5), N(185, 70, "−: dark disc", 6.5), N(185, 80, "+: bright disc", 6.5),
            N(185, 106, "gradient: one cell", 7), N(185, 116, "per radius", 7), N(120, 138, "memory O(M·N·R): limit the radius range", 7)]
    return svg(c, *out)

def d3145(c):
    out = [N(52, 10, "train: shape + reference point c", 7), PG("20,80 42,40 80,36 96,70 70,96", "#f1f5f9", 1), C(58, 62, 2.4), N(62, 68, "c", 8, "start")]
    for (px, py) in ((20, 80), (42, 40), (96, 70)):
        out += [arrow(px, py, 58, 62, .7), C(f(px), f(py), 1.6)]
    out += [N(42, 34, "p, φ", 7, "end"), N(70, 112, "store r = c − p", 7), N(70, 122, "in a table indexed by φ", 7),
            R(140, 20, 90, 54, "#ffffff", 1), L(140, 34, 230, 34, .6), L(176, 20, 176, 74, .6), N(158, 30, "φ", 7), N(203, 30, "vectors r", 7),
            N(158, 46, "0°", 6.5), N(203, 46, "r₁, r₂", 6.5), N(158, 58, "45°", 6.5), N(203, 58, "r₃", 6.5), N(158, 70, "…", 6.5),
            N(185, 92, "detect: A[p + r] += 1 for every r in R[φ(p)]", 6.5), N(185, 108, "peak = where the shape is", 7), N(120, 138, "scale and rotation add dimensions to A", 7)]
    return svg(c, *out)

def d3146(c):
    O = (30, 112)
    s = 30
    return svg(c,
        axes(O[0], O[1], 130, 16), N(130, 122, "x", 7, "end"), N(24, 18, "y", 7, "end"),
        L(30, 112, 120, 22, 1, "3 2"), N(72, 56, "y = x", 7, "end"),
        C(60, 82, 2.4), C(90, 52, 2.4), C(120, 22, 2.4), N(66, 90, "(1,1)", 7, "start"), N(96, 60, "(2,2)", 7, "start"), N(113, 24, "(3,3)", 7, "end"),
        C(f(O[0] + 3 * 20 + 0), f(O[1] - 3 * 20), 2.4) if False else "",
        R(144, 16, 88, 46, "#f1f5f9", 1), N(188, 30, "θ = 0°: ρ = 1, 2, 3", 7), N(188, 42, "3 different cells", 7), N(188, 56, "no agreement", 7),
        R(144, 68, 88, 46, "#d9dee7", 1), N(188, 82, "θ = 135°: ρ = (y − x)/√2", 7), N(188, 94, "= 0 for all three", 7), N(188, 108, "one cell, 3 votes", 7),
        N(120, 130, "line: x cos135° + y sin135° = 0, i.e. y = x", 7.5), N(120, 142, "ρ = 0 , normal at 135°", 7))

CARDS = {
3141: dict(d=d3141, stmtKind="DEFINITION",
  statement=r"<b>Normal form of a line.</b> A line in the image plane can be written $\rho=x\cos\theta+y\sin\theta$, where $\rho$ is its signed distance from the origin and $\theta$ is the angle of its unit normal $(\cos\theta,\sin\theta)$. With $\theta\in[0,\pi)$ and $\rho\in[-D,D]$, $D=\sqrt{M^2+N^2}$ for an $M\times N$ image, every line (including vertical ones) corresponds to exactly one point $(\rho,\theta)$. A fixed image point $(x_0,y_0)$ lies on the lines $\rho(\theta)=x_0\cos\theta+y_0\sin\theta$, a sinusoid in the $(\rho,\theta)$ plane.",
  hint="How do you describe a vertical lane line, where the slope of y = mx + b is infinite?",
  breakdown=[r"<strong>$\rho$ = the shortest distance from the origin to the line.</strong> Drop a perpendicular from the corner of the frame to the lane line; its length is $\rho$.",
             r"<strong>$\theta$ = the direction of that perpendicular.</strong> The angle of the unit normal $(\cos\theta,\sin\theta)$; a vertical line simply has $\theta=0$.",
             r"<strong>$x\cos\theta+y\sin\theta=\rho$ = the points whose shadow on the normal is $\rho$.</strong> One point $(\rho,\theta)$ names one line, and one image point sits on a whole sinusoid of lines.",
             r"<strong>$y=mx+b$ form: a point gives the line $b=y-mx$ in $(m,b)$ space.</strong> Collinear points give lines meeting at one $(m,b)$, but a vertical line needs $m=\infty$, which is why the normal form is used."],
  conn=r"<strong>Naming a lane marking.</strong> Instead of 'how steep is it', say 'how far from the corner of the frame, and at what angle to it'. A vertical post and a slanted lane line are named in the same way.",
  cap="A lane line with its perpendicular from the origin of length ρ at angle θ: all its points satisfy ρ = x cosθ + y sinθ, so the whole line is the single pair (ρ, θ)."),
3142: dict(d=d3142, stmtKind="ALGORITHM",
  statement=r"<b>Hough accumulator voting.</b> Quantize the $(\rho,\theta)$ plane into an accumulator array $A[\rho,\theta]$ initialized to zero. For each edge pixel $(x_i,y_i)$ and each discrete $\theta$, compute $\rho=x_i\cos\theta+y_i\sin\theta$ and increment $A[\rho,\theta]$. Points lying on a common line produce sinusoids meeting at a single cell, so lines correspond to peaks of $A$.",
  hint="If every edge point votes for all lines through it, which line collects the most votes?",
  breakdown=[r"<strong>Each edge pixel $(x_i,y_i)$ votes for every line through it.</strong> That is one vote for every $\theta$, at the matching $\rho$: a sinusoid of votes in $A$.",
             r"<strong>$A[\rho,\theta]\mathrel{+}=1$ = tally on a grid of $(\rho,\theta)$ cells.</strong> Cells are small bins: too fine and noisy points spread their votes, too coarse and different lines merge.",
             r"<strong>Sinusoids crossing in one cell = a line.</strong> Edge points on the same lane line all vote for its $(\rho,\theta)$, which therefore collects many votes while chance cells get few."],
  conn=r"<strong>Voting for the lane line.</strong> Each bright dash of paint says 'a line passes through here, at one of these angles'. Only the line that all the dashes agree on gets a large tally, even if some dashes are missing.",
  cap="Three edge points on a lane line each trace a sinusoid in the accumulator A[ρ, θ]. The curves cross in one cell, which collects 3 votes: that cell is the line."),
3143: dict(d=d3143, stmtKind="ALGORITHM",
  statement=r"<b>Hough transform for lines.</b> (1) Detect edge pixels (e.g. Canny). (2) For each edge pixel and each discrete $\theta$, compute $\rho$ and increment $A[\rho,\theta]$. (3) Smooth or threshold $A$ and keep the local maxima with $A[\rho,\theta]\ge\tau$. (4) Convert each peak back to a line, optionally clipped to the segment supported by edge pixels. Using the gradient direction $\theta=\operatorname{atan2}(f_y,f_x)$ lets each pixel vote for one (or a few) $\theta$ only.",
  hint="Why does the Hough peak give you an endless line, and not a segment?",
  breakdown=[r"<strong>Edges, then votes.</strong> Only edge pixels vote, so the edge detector fixes how much work there is; each vote is a pair $(\rho,\theta)$."],
  conn=r"<strong>Finding the lanes in the frame.</strong> Run Canny on the street frame, let every edge pixel vote, and the two strongest peaks are the lane lines. Painted dashes broken by shadows still add up to a peak.",
  cap="The four steps: Canny edges, vote A[ρ, θ]++, keep peaks A ≥ τ, turn each peak (ρ, θ) back into a line."),
3144: dict(d=d3144, stmtKind="ALGORITHM",
  statement=r"<b>Circle Hough transform.</b> A circle $(x-a)^2+(y-b)^2=r^2$ has three parameters $(a,b,r)$, so the accumulator is three-dimensional. For a fixed $r$, each edge point votes for the circle of centres of radius $r$ around it. With the gradient direction $\theta$ at the edge pixel, the centre lies on that line at distance $r$: $a=x\mp r\cos\theta$, $b=y\mp r\sin\theta$, with $-$ for a disc darker than its background ($\nabla f$ points outward) and $+$ for a brighter one ($\nabla f$ points inward). Each pixel then votes for one cell per radius, or two if the polarity is unknown.",
  hint="If every point of a round sign votes for possible centres, where do the votes pile up?",
  breakdown=[r"<strong>$(a,b)$ = the centre of the sign, $r$ its radius.</strong> Three numbers describe it, so the voting grid has three axes.",
             r"<strong>A ring of candidate centres per edge point.</strong> For a known $r$, the sign's centre must be $r$ away from each point of its rim; the rings of all rim points meet at the real centre.",
             r"<strong>$(a,b)=(x,y)\mp r\,\nabla f/\lvert\nabla f\rvert$ = shortcut with the gradient.</strong> The gradient runs along the radius and points toward the brighter side, so a bright disc uses $+$ and a dark disc uses $-$. One vote replaces a whole ring."],
  conn=r"<strong>Finding round signs and wheels.</strong> Each point on the rim of a speed-limit sign votes for centres a radius away; they all agree on one spot. Searching an unknown radius multiplies the memory, so only a plausible range of radii is tried.",
  cap="Edge points on a round sign each vote for a ring of centres of radius r; the rings meet at the sign's centre (a, b). The gradient lies along the radius: outward for this dark disc, so the centre is at distance r against it."),
3145: dict(d=d3145, stmtKind="ALGORITHM",
  statement=r"<b>Generalized Hough transform.</b> Training: choose a reference point $c$ for the shape; for each boundary point $p$ with orientation $\phi(p)$, store $r=c-p$ in the R-table entry for $\phi$. Detection: for every edge pixel $p$ with orientation $\phi$ and every $r$ in the R-table entry for $\phi$, increment $A[p+r]$. The peak of $A$ is the location of the shape's reference point. Scale and rotation add dimensions to $A$.",
  hint="How can the voting find a shape that has no formula, like the bus stop's outline?",
  breakdown=[r"<strong>$r=c-p$ = the arrow from a boundary point to the shape's reference point.</strong> Recorded once, offline, for the shape you want to find."],
  conn=r"<strong>Finding the bus shelter in the frame.</strong> Teach the table once from a picture of the shelter: 'a boundary point sloping at 45° has the centre this far that way'. Then every edge pixel in a new frame votes for where the centre could be.",
  cap="Training: arrows r = c − p from boundary points p (with orientation φ) to the reference point c, filed in an R-table by φ. Detection: each edge pixel votes for p + r."),
3146: dict(d=d3146, stmtKind="WORKED EXAMPLE",
  statement=r"<b>Example.</b> The points $(1,1),(2,2),(3,3)$ with $\rho=x\cos\theta+y\sin\theta$. At $\theta=0^\circ$: $\rho=1,2,3$, three different cells, so no agreement. At $\theta=135^\circ$: $\cos\theta=-\frac{\sqrt2}2$, $\sin\theta=\frac{\sqrt2}2$, so $\rho=\frac{\sqrt2}2(y-x)=0$ for all three points: one cell $(0,135^\circ)$ gets 3 votes. The line is $x\cos135^\circ+y\sin135^\circ=0$, i.e. $y=x$.",
  hint="At which angle do three points of a diagonal lane marking all land in the same cell?",
  breakdown=[r"<strong>$\theta=0^\circ$: $\rho=1,2,3$.</strong> Looking along $x$, each point is at a different distance, so the three votes scatter."],
  conn=r"<strong>Three paint dashes on a diagonal lane line.</strong> From the angle straight along the road they look unrelated; from the right angle (135°) they all lie the same distance (zero) from the corner of the frame.",
  cap="Points (1,1), (2,2), (3,3) lie on y = x. At θ = 0° they vote for three different ρ; at θ = 135° all give ρ = 0 and one cell collects 3 votes."),
}
CARDS[3143]["breakdown"] += [r"<strong>$A[\rho,\theta]\ge\tau$ and a local maximum = a line.</strong> Smooth the tally, keep the peaks above a vote threshold; each peak $(\rho,\theta)$ is converted back to a line.",
                             r"<strong>The result is an infinite line.</strong> Two collinear pieces far apart vote into the same cell and are merged; clip to where edge pixels exist if a segment is needed.",
                             r"<strong>Split peaks and the randomized Hough transform.</strong> Rounding spreads votes over nearby cells, so smooth $A$ to merge them. The randomized version instead picks two edge points, which fix one $(\rho,\theta)$, and casts a single vote in a hash table."]
CARDS[3145]["breakdown"] += [r"<strong>R-table indexed by $\phi$ = look up the arrows for this edge angle.</strong> Boundary points with the same orientation share a list of possible arrows to the centre.",
                             r"<strong>$A[p+r]\mathrel{+}=1$ = vote for where the centre would be.</strong> Points of the real shape agree on one cell; adding scale and rotation adds axes to $A$ and the cost grows.",
                             r"<strong>Scale $s$, rotation $\alpha$: look up $\phi-\alpha$, vote at $p+s\,Q_\alpha r$.</strong> $Q_\alpha$ is the $2\times2$ rotation matrix. The accumulator becomes four-dimensional, $(c_x,c_y,s,\alpha)$."]
CARDS[3146]["breakdown"] += [r"<strong>$\theta=135^\circ$: $\rho=\frac{\sqrt2}2(y-x)=0$.</strong> Every point of $y=x$ is the same distance from the origin measured along the normal: all three votes land in one cell.",
                             r"<strong>Decode $(0,135^\circ)$ = the line $y=x$.</strong> It passes through the origin ($\rho=0$) with normal at 135°; check the book's convention for the sign of $\rho$ and the range of $\theta$."]

STORY = {
 3141: dict(s="STORY 6 · STEP 7 · NAMING A LINE", b="A line is named by $(\\rho,\\theta)$: its distance from the origin and the angle of its normal; vertical lines are no problem.",
   f=[["3135", "edge points"], ["3065", "the same $(\\rho,\\theta)$ slice picture"]], n=[["3142", "voting"]]),
 3142: dict(s="STORY 6 · STEP 8 · VOTE", b="Each edge point votes for every line through it; <b>sinusoids cross</b> at the true line.",
   f=[["3141", "the parameters"]], n=[["3143", "the full algorithm"], ["3144", "circles"]]),
 3143: dict(s="STORY 6 · STEP 9 · THE ALGORITHM", b="Edges, vote, find peaks, draw lines: robust to gaps because <b>no connectivity is needed</b>.",
   f=[["3142", "accumulator"], ["3135", "Canny edges"]], n=[["3144", "other shapes"], ["3146", "numbers"]]),
 3144: dict(s="STORY 6 · STEP 10 · CIRCLES", b="A circle has three parameters; the gradient direction cuts the voting to <b>one cell per radius</b>.",
   f=[["3143", "line Hough"], ["3131", "gradient direction"]], n=[["3145", "any shape"]]),
 3145: dict(s="STORY 6 · STEP 11 · ANY SHAPE", b="The <b>R-table</b> stores arrows to a reference point, so any shape can vote for its location.",
   f=[["3144", "circles"]], n=[["3146", "numbers"], ["3151", "finding points instead of shapes"]]),
 3146: dict(s="STORY 6 · STEP 12 · CHECK BY HAND", b="Three diagonal points agree only at $\\theta=135^\\circ$.",
   f=[["3142", "voting"]], n=[["3151", "next: corners as landmarks"]]),
}
FIX = build_fix(CARDS)

# Fields the card builder above does not set (notation and corrections).
EXTRA = {
    3141: {"math": "$$\\rho=x\\cos\\theta+y\\sin\\theta,\\qquad \\theta\\in[0,\\pi),\\ \\rho\\in[-D,D],\\ D=\\sqrt{M^2+N^2}$$"},
    3144: {"coreTranslation": ["<strong>Parameters:</strong> a circle $(x-a)^2+(y-b)^2=r^2$ has <strong>3 parameters</strong> $(a,b,r)$, so the naive accumulator is <strong>3-dimensional</strong>.", "<strong>Voting:</strong> for a fixed radius $r$, each edge point votes for a <strong>circle of candidate centers</strong> of that radius around it; points on a true circle all vote for its center.", "<strong>Speed-up:</strong> with the <strong>gradient direction</strong> the center lies on that line at distance $r$: $a=x\\mp r\\cos\\theta,\\ b=y\\mp r\\sin\\theta$ ($-$ for a dark disc, $+$ for a bright one), so each point votes for <strong>one cell per $r$</strong> (two if the polarity is unknown) instead of a whole circle."], "math": "$$(x-a)^2+(y-b)^2=r^2,\\qquad a=x\\mp r\\cos\\theta,\\quad b=y\\mp r\\sin\\theta$$", "examTrap": "Memory is O(M·N·R) for the 3D accumulator. Searching an unknown radius range is the cost driver, so restrict r to a plausible range."},
    3146: {"examTrap": "The same line is both (ρ, θ) and (−ρ, θ + 180°), so here (0, 135°) and (0, 315°) name one line. Fix the convention before decoding."},
}
for _cid, _fields in EXTRA.items():
    FIX[_cid].update(_fields)
