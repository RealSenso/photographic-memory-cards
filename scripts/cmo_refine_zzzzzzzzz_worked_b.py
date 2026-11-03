"""Worked examples (topics 1-7): statement = the question, math = the solution, breakdown = reading it; every diagram is drawn from the real numbers."""
import math
from air_lib import *
from dip_lib import E


def P_(pts):
    return pts


def line_pts(f, a, b, n=60):
    return [(a + (b - a) * i / n, f(a + (b - a) * i / n)) for i in range(n + 1)]


# ---------------- 106: coercivity, f = x1^4 + x2^4 - 4 x1 x2 ----------------
def d106(c):
    X = lambda t: 120 + 60 * t
    Y = lambda v: 62 - 12 * v
    p = [L(20, 62, 222, 62, 1.1, ar=True), L(120, 100, 120, 6, 1.1, ar=True)]
    c1 = [(X(t), Y(2 * t ** 4 - 4 * t ** 2)) for t in [-1.6 + 3.2 * i / 80 for i in range(81)]]
    c2 = [(X(s), Y(2 * s ** 4 + 4 * s ** 2)) for s in [-0.9 + 1.8 * i / 60 for i in range(61)]]
    p.append(poly(c1, 1.4) + poly(c2, 1.1, "4 3"))
    p.append(dot(X(1), Y(-2), r=2.8) + dot(X(-1), Y(-2), r=2.8))
    p.append(circ(120, 62, 2.8, "#ffffff", 1.2))
    p.append(N(X(1), 99, "(1,1): f = −2", 7.5) + N(X(-1), 99, "(−1,−1): f = −2", 7.5))
    p.append(N(120, 84, "saddle (0,0): f = 0", 7.5))
    p.append(N(14, 112, "solid: x₁ = x₂ = t, f = 2t⁴ − 4t²", 7, "start") + N(14, 122, "dashed: x₁ = −x₂ = s, f = 2s⁴ + 4s²", 7, "start"))
    p.append(N(212, 32, "f → ∞", 7.5, "end") + N(28, 32, "f → ∞", 7.5, "start"))
    p.append(N(120, 112, "t", 7.5) if False else "")
    p.append(N(120, 138, "coercive, so the lowest point exists and equals −2", 8))
    return svg(c, *p)


# ---------------- 206: Rosenbrock contours near (1,1) ----------------
def d206(c):
    X = lambda u: 22 + 36 * u
    Y = lambda v: 128 - 36 * v
    p = [L(14, 128, 92, 128, 1.1, ar=True), L(22, 134, 22, 8, 1.1, ar=True)]
    p.append(N(92, 138, "x₁", 7.5, "end") + N(28, 14, "x₂", 7.5, "start"))

    def contour(cv, lo=0.0, hi=1.75):
        a, b = max(lo, 1 - math.sqrt(cv)), min(hi, 1 + math.sqrt(cv))
        xs = [a + (b - a) * i / 70 for i in range(71)]
        up = [(X(x), Y(x * x + math.sqrt(max(0, cv - (1 - x) ** 2) / 100))) for x in xs]
        dn = [(X(x), Y(x * x - math.sqrt(max(0, cv - (1 - x) ** 2) / 100))) for x in xs]
        return poly(up, 1.1) + poly(dn, 1.1) + (L(f(up[0][0]), f(up[0][1]), f(dn[0][0]), f(dn[0][1]), 1.1) + L(f(up[-1][0]), f(up[-1][1]), f(dn[-1][0]), f(dn[-1][1]), 1.1) if (b - a) < 1.74 and a > lo and b < hi else "")
    p.append(contour(0.4) + contour(3.0))
    p.append(poly(line_pts(lambda x: 0, 0, 1)[:0] or [(X(x), Y(x * x)) for x in [i * 1.75 / 40 for i in range(41)]], 1.0, "3 2"))
    p.append(dot(X(1), Y(1), r=2.6))
    p.append(arrow(X(1), Y(1), X(1) + 17, Y(1) + 9, 1.2) + arrow(X(1), Y(1), X(1) + 8, Y(1) - 16, 1.2))
    for y, s in ((12, "f = 100(x₂ − x₁²)² + (1 − x₁)²"), (24, "∇f(1,1) = 0"), (42, "∇²f(1,1) = [802 −400; −400 200]"),
                 (54, "det = 400 > 0,  tr = 1002 > 0"), (72, "λ₁ ≈ 1001.6: across the canyon"), (84, "λ₂ ≈ 0.4: along the floor"),
                 (102, "κ = λ₁/λ₂ ≈ 2500"), (116, "dashed: floor x₂ = x₁²"), (128, "contours f = 0.4, 3")):
        p.append(N(98, y, s, 7.5, "start"))
    return svg(c, *p)


# ---------------- 306: convex / strictly convex / strongly convex ----------------
def d306(c):
    p = []
    specs = [(40, lambda x: 0.5 * x, "f₁ = x/2", "f₁″ = 0", "flat: convex, not strictly", 62),
             (120, lambda x: x ** 4, "f₂ = x⁴", "f₂″ = 12x², f₂″(0) = 0", "strictly, not strongly", 90),
             (200, lambda x: x ** 2, "f₃ = x²", "f₃″ = 2 = μ", "strongly convex", 90)]
    for cx, fn_, nm, sec, prop, base in specs:
        X = lambda x, cx=cx: cx + 30 * x
        Y = lambda v, base=base: base - 44 * v
        p.append(L(cx - 36, base, cx + 36, base, 1.0, ar=True) + L(cx, base + 4, cx, 22, 1.0, ar=True))
        p.append(poly([(X(x), Y(fn_(x))) for x in [-1 + 2 * i / 50 for i in range(51)]], 1.4))
        p.append(L(f(X(-0.8)), f(Y(fn_(-0.8))), f(X(0.8)), f(Y(fn_(0.8))), 1.0, d="3 2"))
        p.append(dot(X(-0.8), Y(fn_(-0.8)), r=1.8) + dot(X(0.8), Y(fn_(0.8)), r=1.8))
        p.append(N(cx, 14, nm, 8.5, "middle", "bold"))
        p.append(N(cx, 108, sec, 7, "middle") + N(cx, 119, prop, 7, "middle"))
    p.append(N(120, 138, "μ-strongly ⇒ strictly ⇒ convex, none of the arrows reverses", 7.5))
    p.append(N(120, 129, "dashed chord: on the graph (f₁), above it (f₂, f₃)", 7))
    return svg(c, *p)


# ---------------- 606: Rosenbrock at the origin, Newton vs gradient step ----------------
def d606(c):
    X = lambda u: 34 + 56 * u
    Y = lambda v: 104 - 56 * v
    p = [L(20, 104, 126, 104, 1.1, ar=True), L(34, 118, 34, 12, 1.1, ar=True)]
    p.append(N(116, 113, "x₁", 7.5, "end") + N(40, 18, "x₂", 7.5, "start"))
    for cv in (0.2, 1.0, 4.0):
        a, b = max(-0.35, 1 - math.sqrt(cv)), min(1.25, 1 + math.sqrt(cv))
        xs = [a + (b - a) * i / 80 for i in range(81)]
        for sgn in (1, -1):
            pts = [(X(x), Y(x * x + sgn * math.sqrt(max(0, cv - (1 - x) ** 2) / 100))) for x in xs]
            pts = [q for q in pts if 12 <= q[1] <= 118]
            if len(pts) > 1:
                p.append(poly(pts, 1.1))
    p.append(poly([(X(x), Y(x * x)) for x in [i * 1.25 / 40 for i in range(41)]], 1.0, "3 2"))
    p.append(arrow(34, 104, X(1) - 3, 104, 1.5) + dot(X(1), 104, r=2.2) + N(X(1) + 2, 96, "p_N", 8, "start"))
    p.append(L(34, 100, 34, 108, 1.4) + N(40, 120, "GD step < 0.02", 7, "start"))
    p.append(dot(34, 104, r=2.4) + dot(X(1), Y(1), r=2.4) + N(X(1) + 4, Y(1) - 3, "(1,1)", 8, "start"))
    for y, s in ((16, "x = (0,0):  f = 1"), (28, "g = (−2, 0),  H = diag(2, 200)"), (40, "κ = 200/2 = 100"),
                 (58, "Newton:  p_N = −H⁻¹g = (1, 0)"), (76, "gradient descent: p = −αg = (2α, 0)"), (88, "stable only for α < 2/200 = 0.01"),
                 (100, "so ‖p‖ < 0.02: about 50× shorter"), (118, "dashed: floor x₂ = x₁²")):
        p.append(N(118, y, s, 7, "start"))
    return svg(c, *p)


# ---------------- 706: CG on f = x1^2 + 4 x2^2 from (4,1) ----------------
def d706(c):
    O, U = (26, 76), 18
    X = lambda u: O[0] + U * u
    Y = lambda v: O[1] - U * v
    p = ['<clipPath id="cl706"><rect x="6" y="12" width="108" height="124"/></clipPath>']
    p.append(L(6, O[1], 112, O[1], 1.0, ar=True) + L(O[0], 134, O[0], 14, 1.0, ar=True))
    ell = "".join(E(O[0], O[1], U * math.sqrt(cv), U * math.sqrt(cv) / 2, 0, "none", 1.0) for cv in (1.5, 4, 7.2, 17))
    p.append('<g clip-path="url(#cl706)">' + ell + "</g>")
    x = (4.0, 1.0)
    pts = [x]
    for _ in range(7):
        g = (2 * x[0], 8 * x[1])
        a = (g[0] ** 2 + g[1] ** 2) / (2 * g[0] ** 2 + 8 * g[1] ** 2)
        x = (x[0] - a * g[0], x[1] - a * g[1])
        pts.append(x)
    p.append(poly([(X(a), Y(b)) for a, b in pts], 1.0, "3 2"))
    cg = [(4, 1), (2.4, -0.6), (0, 0)]
    p.append(poly([(X(a), Y(b)) for a, b in cg], 1.6))
    for a, b in cg:
        p.append(dot(X(a), Y(b), r=2.6))
    p.append(N(X(4) + 4, Y(1) - 3, "x₀", 8.5, "start") + N(X(2.4) + 4, Y(-0.6) + 11, "x₁", 8.5, "start") + N(X(0) + 4, Y(0) + 12, "x₂ = x*", 8.5, "start"))
    for y, s in ((16, "f = x₁² + 4x₂²,  Q = diag(2, 8)"), (27, "x₀ = (4, 1),  g₀ = (8, 8)"), (38, "α₀ = 128/640 = 1/5"), (49, "x₁ = (2.4, −0.6)"), (60, "g₁ = (4.8, −4.8)"),
                 (71, "β₀ = 46.08/128 = 0.36"), (82, "d₁ = −g₁ + β₀d₀ = (−7.68, 1.92)"), (93, "α₁ = 46.08/147.456 = 5/16"), (104, "x₂ = x₁ + α₁d₁ = (0, 0)"),
                 (118, "solid: CG, 2 hops"), (129, "dashed: steepest descent, 7 hops")):
        p.append(N(118, y, s, 6.8, "start"))
    return svg(c, *p)


FIX = {
    106: {
        "statement": "<b>Question.</b> Show that $f(x)=x_1^4+x_2^4-4x_1x_2$ has a global minimizer on all of $\\mathbb R^2$, then find it.",
        "stmtKind": "WORKED EXAMPLE",
        "math": "$$\\begin{aligned}4|x_1x_2|\\le2(x_1^2+x_2^2)&\\Rightarrow f\\ge x_1^4+x_2^4-2(x_1^2+x_2^2)\\to\\infty\\ \\ (\\text{coercive})\\\\ \\nabla f=0:&\\ x_1^3=x_2,\\ x_2^3=x_1\\Rightarrow(0,0),\\ \\pm(1,1)\\\\ f(0,0)=0,\\ f(\\pm(1,1))=-2&\\Rightarrow\\min f=-2\\ \\text{at}\\ \\pm(1,1)\\end{aligned}$$",
        "breakdown": [
            "<strong>Coercive:</strong> the bound makes $f\\to\\infty$ in every direction, so the set $\\{f\\le f(0,0)\\}$ is closed and bounded; by Weierstrass it has a minimizer, and it is global because $f$ is larger outside.",
            "<strong>Candidates:</strong> $\\nabla f=(4x_1^3-4x_2,\\ 4x_2^3-4x_1)=0$ gives $x_1^9=x_1$, so $x_1\\in\\{0,\\pm1\\}$ and the points $(0,0)$, $(1,1)$, $(-1,-1)$.",
            "<strong>Compare values:</strong> $f(0,0)=0$ is a saddle, while $f(1,1)=f(-1,-1)=-2$ are the two global minima."
        ],
        "drawingSvg": d106("106"),
        "drawingCaption": "Two slices of f. Along x₁ = x₂ = t (solid) f = 2t⁴ − 4t² dips to −2 at t = ±1 and rises to infinity: coercive. Along x₁ = −x₂ = s (dashed) f = 2s⁴ + 4s² only rises, so (0,0) is a saddle with f = 0.",
    },
    206: {
        "statement": "<b>Question.</b> For Rosenbrock's $f(x)=100(x_2-x_1^2)^2+(1-x_1)^2$, find the critical point, decide its type, and measure how ill-conditioned it is.",
        "stmtKind": "WORKED EXAMPLE",
        "math": "$$\\begin{aligned}\\nabla f&=\\big(-400x_1(x_2-x_1^2)-2(1-x_1),\\ 200(x_2-x_1^2)\\big)=0\\Rightarrow x_2=x_1^2,\\ x_1=1\\\\ \\nabla^2f(1,1)&=\\begin{bmatrix}802&-400\\\\-400&200\\end{bmatrix},\\ \\det=400\\gt0,\\ \\operatorname{tr}=1002\\gt0\\Rightarrow\\nabla^2f\\succ0\\\\ \\lambda_{1,2}&\\approx1001.6,\\ 0.4\\Rightarrow\\kappa\\approx2500\\end{aligned}$$",
        "breakdown": [
            "<strong>Gradient $=0$:</strong> the second component forces $x_2=x_1^2$ (the canyon floor), and the first then reduces to $-2(1-x_1)=0$, so $(1,1)$ is the only critical point.",
            "<strong>$\\det\\gt0$ and $\\operatorname{tr}\\gt0$:</strong> for a $2\\times2$ matrix both eigenvalues are positive, so $\\nabla^2f\\succ0$ and $(1,1)$ is a strict local minimizer (global, since $f\\ge0=f(1,1)$).",
            "<strong>Eigenvalues $\\approx1001.6$ and $0.4$:</strong> very steep across the canyon, nearly flat along the floor, so $\\kappa\\approx2500$ and gradient descent crawls."
        ],
        "drawingSvg": d206("206"),
        "drawingCaption": "True level sets f = 0.4 and 3 of Rosenbrock's function. They hug the dashed parabola x₂ = x₁². At (1,1) the Hessian has curvature 1001.6 across the canyon and only 0.4 along the floor, so κ ≈ 2500.",
    },
    306: {
        "statement": "<b>Question.</b> Using $f''$, classify $f_1(x)=x/2$, $f_2(x)=x^4$ and $f_3(x)=x^2$ as convex, strictly convex or $\\mu$-strongly convex.",
        "stmtKind": "WORKED EXAMPLE",
        "math": "$$\\begin{aligned}f_1''=0&:\\ \\text{convex only (a line is flat)}\\\\ f_2''=12x^2\\ge0,\\ f_2''(0)=0&:\\ \\text{strictly convex, but no }\\mu\\gt0\\text{ works}\\\\ f_3''=2\\ge\\mu\\ (\\mu=2)&:\\ \\mu\\text{-strongly convex}\\end{aligned}$$",
        "breakdown": [
            "<strong>$f_1$:</strong> $f''=0\\succeq0$ so it is convex, but the graph is a straight line, so it is not strictly convex.",
            "<strong>$f_2$:</strong> $f''\\ge0$ and there is no flat stretch, so it is strictly convex; yet $f''(0)=0$, so $f''\\ge\\mu$ fails for every $\\mu\\gt0$.",
            "<strong>$f_3$:</strong> $f''=2\\ge\\mu$ with $\\mu=2$ everywhere, so it is strongly convex, hence strictly convex, hence convex."
        ],
        "stmtKind_": "",
        "drawingSvg": d306("306"),
        "drawingCaption": "The three curves on [−1, 1] with a dashed chord between x = ±0.8. For the line the chord lies on the graph (not strictly convex). For x⁴ and x² the chord is strictly above it, but x⁴ is flat at 0 (f″(0) = 0) while x² has f″ = 2 everywhere.",
    },
    606: {
        "statement": "<b>Question.</b> For Rosenbrock's $f(x)=100(x_2-x_1^2)^2+(1-x_1)^2$ at $x=(0,0)$, compute $g$, $H$, the Newton step $p_N=-H^{-1}g$ and compare it with a stable gradient-descent step.",
        "stmtKind": "WORKED EXAMPLE",
        "math": "$$\\begin{aligned}g&=\\nabla f(0,0)=(-2,0),\\quad H=\\operatorname{diag}(2,200),\\quad\\kappa=100\\\\ p_N&=-H^{-1}g=(1,0)\\\\ p_{GD}&=-\\alpha g=(2\\alpha,0),\\ \\ \\alpha\\lt\\tfrac2{200}=0.01\\ \\Rightarrow\\ \\|p_{GD}\\|\\lt0.02\\end{aligned}$$",
        "breakdown": [
            "<strong>$g=(-2,0)$ and $H=\\operatorname{diag}(2,200)$:</strong> the slope points along $x_1$, where the curvature is only $2$, while across the canyon ($x_2$) it is $200$, so $\\kappa=100$.",
            "<strong>Newton divides each slope component by its own curvature:</strong> $p_N=(2/2,\\ 0/200)=(1,0)$, a long move straight along the canyon.",
            "<strong>Gradient descent must keep $\\alpha\\lt2/\\lambda_{\\max}=0.01$ to stay stable,</strong> so its step along the useful direction is under $0.02$: about 50 times shorter."
        ],
        "personalConnection": "<strong>The airplane analogy.</strong> At the canyon mouth the useful heading is along the gentle floor, but the walls are steep, so a plane that only reads the slope must take tiny, careful hops to avoid bouncing off the walls. Newton reads the curvature too and proposes a hop 50 times longer (a line search then keeps it safe).",
        "hint": "How much longer is the Newton hop than a stable gradient hop at the canyon mouth?",
        "drawingSvg": d606("606"),
        "drawingCaption": "True level sets of Rosenbrock's function (f = 0.2, 1, 4) near the origin, where f = 1. The Newton step p_N = (1, 0) follows the canyon direction; a stable gradient step needs α < 0.01, so it is under 0.02 long (the tick at the origin). The dashed curve is the floor x₂ = x₁².",
    },
    706: {
        "statement": "<b>Question.</b> Run conjugate gradient on $f(x)=x_1^2+4x_2^2$ (so $Q=\\operatorname{diag}(2,8)$) from $x_0=(4,1)$ and show that it finishes in $n=2$ steps.",
        "stmtKind": "WORKED EXAMPLE",
        "math": "$$\\begin{aligned}g_0&=Qx_0=(8,8),\\ d_0=-g_0,\\ \\alpha_0=\\tfrac{g_0^\\top g_0}{d_0^\\top Qd_0}=\\tfrac{128}{640}=\\tfrac15\\Rightarrow x_1=(2.4,-0.6),\\ g_1=(4.8,-4.8)\\\\ \\beta_0&=\\tfrac{\\|g_1\\|^2}{\\|g_0\\|^2}=0.36,\\ d_1=-g_1+\\beta_0d_0=(-7.68,\\,1.92),\\ \\alpha_1=\\tfrac{46.08}{d_1^\\top Qd_1}=\\tfrac5{16}\\\\ x_2&=x_1+\\alpha_1d_1=(0,0)=x^*\\end{aligned}$$",
        "breakdown": [
            "<strong>Hop 1 ($\\alpha_0=1/5$):</strong> fly straight downhill along $d_0=-g_0$ until the slope across the path vanishes, landing at $x_1=(2.4,-0.6)$ (check: $g_1^\\top d_0=0$).",
            "<strong>$\\beta_0=0.36$ blends in the memory:</strong> $d_1=-g_1+\\beta_0d_0$ is fresh downhill plus 36% of the old heading, which makes it $Q$-conjugate to $d_0$.",
            "<strong>Hop 2 ($\\alpha_1=5/16$):</strong> flying along $d_1$ removes all the remaining error, so $x_2=x^*=(0,0)$ exactly: two hops for two dimensions."
        ],
        "drawingSvg": d706("706"),
        "drawingCaption": "Level sets of f = x₁² + 4x₂² with the true paths. CG (solid) goes x₀ = (4,1) → x₁ = (2.4,−0.6) → x₂ = (0,0) in two hops. Steepest descent with exact line search (dashed) zig-zags and is still not at the minimum after seven hops.",
    },
}
for _v in FIX.values():
    _v.pop("stmtKind_", None)
