"""Worked examples (topics 12-15): question / solution math / breakdown, diagrams drawn from the real numbers."""
import math
from air_lib import *
from dip_lib import E


# ---------------- 1206: min x1 + x2 on the unit circle, bordered Hessian ----------------
def d1206(c):
    C0, R = (76, 76), 44
    s2 = math.sqrt(2) / 2
    X = lambda u: C0[0] + R * u
    Y = lambda v: C0[1] - R * v
    p = [L(24, 76, 128, 76, 1.0, ar=True), L(76, 126, 76, 22, 1.0, ar=True)]
    p.append(circ(C0[0], C0[1], R, "#e5e7eb", 1.4))
    for k, dd in ((-math.sqrt(2), None), (0, "3 2"), (math.sqrt(2), None)):
        cx, cy = X(k / 2), Y(k / 2)
        p.append(L(f(cx - 34), f(cy - 34), f(cx + 34), f(cy + 34), 1.0, d=dd))
    sw, ne = (X(-s2), Y(-s2)), (X(s2), Y(s2))
    p.append(dot(*sw, r=2.8) + dot(*ne, r=2.4))
    p.append(arrow(sw[0], sw[1], sw[0] - 20, sw[1] + 20, 1.4) + N(sw[0] - 22, sw[1] + 30, "−∇f = λ∇c", 7.5, "start"))
    p.append(arrow(sw[0], sw[1], sw[0] + 16, sw[1] - 16, 1.0, d="3 2") + N(sw[0] + 20, sw[1] - 10, "∇f", 7.5, "start"))
    p.append(N(sw[0] - 4, sw[1] - 8, "SW", 8, "end") + N(ne[0] + 5, ne[1] - 4, "NE", 8, "start"))
    p.append(plane(sw[0] + 10, sw[1] + 10, -45, .55) if False else "")
    for y, s in ((16, "f = x₁ + x₂"), (26, "c = x₁² + x₂² − 1 = 0"), (40, "∇f + λ∇c = 0 gives"), (50, "x₁ = x₂ = −1/(2λ)"),
                 (66, "SW: λ = 1/√2, f = −√2"), (76, "J = (−√2, −√2)"), (86, "∇²L = √2·I"), (98, "det B = −4√2 < 0"),
                 (108, "= (−1)ᵐ, m = 1: strict min"), (122, "NE: λ = −1/√2,"), (132, "det B = +4√2: a max")):
        p.append(N(140, y, s, 7, "start"))
    return svg(c, *p)


# ---------------- 1306: project p = (1.5, 1.0, 0.5, 0.1) onto the simplex ----------------
def d1306(c):
    vals, base, U = [1.5, 1.0, 0.5, 0.1], 114, 50
    tau = 0.75
    p = []
    xs = [24, 52, 80, 108]
    for x0, v in zip(xs, vals):
        h = v * U
        top = base - h
        p.append(R(x0, top, 20, h, "#f1f5f9", 1.2))
        if v > tau:
            p.append(R(x0, top, 20, (v - tau) * U, "#9ca3af", 1.2))
        p.append(N(x0 + 10, base + 10, f"{v:g}", 7.5))
    p.append(L(14, base, 136, base, 1.1))
    p.append(L(14, base - tau * U, 136, base - tau * U, 1.2, d="5 3") + N(134, base - tau * U - 3, "τ = 0.75", 7.5, "end"))
    p.append(N(76, 138, "tanks p = (1.5, 1.0, 0.5, 0.1)", 7.5))
    for y, s in ((16, "sort: 1.5, 1.0, 0.5, 0.1"), (28, "k = 2: τ = (2.5 − 1)/2 = 0.75"), (40, "p₍₂₎ = 1.0 > τ,  p₍₃₎ = 0.5 ≤ τ"),
                 (56, "P_Δ(p) = max(p − τ1, 0)"), (68, "= (0.75, 0.25, 0, 0)"), (80, "sum = 1 ✓, all ≥ 0 ✓"),
                 (96, "dark = what stays above τ"), (107, "light = shaved off")):
        p.append(N(146 if y > 90 else 142, y, s, 7, "start"))
    return svg(c, *p)


# ---------------- 1406: projected gradient on the orthant, f = (x1-2)^2/2 + x2^2 + 3 x2 ----------------
def d1406(c):
    X = lambda u: 34 + 22 * u
    Y = lambda v: 32 - 22 * v
    p = ['<clipPath id="cl1406"><rect x="14" y="6" width="104" height="124"/></clipPath>']
    p.append('<polygon points="34,32 118,32 118,6 34,6" fill="#e5e7eb"/>')
    p.append(L(14, 32, 118, 32, 1.1, ar=True) + L(34, 130, 34, 6, 1.1, ar=True))
    ell = "".join(E(X(2), Y(-1.5), 22 * math.sqrt(2 * r), 22 * math.sqrt(r), 0, "none", 1.0, d=dd) for r, dd in ((2.25, None), (6.75, "3 2")))
    p.append('<g clip-path="url(#cl1406)">' + ell + "</g>")
    x0, g1, x1 = (X(1), Y(1)), (X(2), Y(-4)), (X(2), Y(0))
    p.append(arrow(x0[0], x0[1], g1[0] - 1, g1[1] - 3, 1.2, d="4 3") + arrow(g1[0], g1[1] - 4, x1[0], x1[1] + 3, 1.4))
    p.append(dot(*x0, r=2.6) + dot(*x1, r=2.6) + dot(*g1, r=2.0) + dot(X(2), Y(-1.5), r=1.6))
    p.append(N(x0[0] - 4, x0[1] + 9, "x₀", 8, "end") + N(x1[0] + 5, x1[1] - 4, "x₁", 8, "start") + N(g1[0] + 4, g1[1] + 3, "(2, −4)", 7, "start"))
    p.append(N(X(2) + 5, Y(-1.5) + 2, "unconstr. min", 6.5, "start"))
    p.append(N(112, 14, "C = {x ≥ 0}", 7, "end"))
    for y, s in ((16, "f = ½(x₁ − 2)² + x₂² + 3x₂"), (27, "α = 1,  x₀ = (1, 1)"), (39, "∇f(x₀) = (−1, 5)"), (50, "x₀ − α∇f = (2, −4)"),
                 (62, "P_C = max(·, 0):"), (73, "x₁ = (2, 0)"), (88, "∇f(2, 0) = (0, 3)"), (99, "(2,0) − (0,3) = (2, −3)"), (110, "max(·, 0) = (2, 0) again"), (122, "fixed point ✓")):
        p.append(N(124, y, s, 7, "start"))
    return svg(c, *p)


# ---------------- 1506: active set QP, min 1/2 |x - (4,4)|^2 on [0,2]^2 ----------------
def d1506(c):
    X = lambda u: 22 + 22 * u
    Y = lambda v: 116 - 22 * v
    p = ['<clipPath id="cl1506"><rect x="6" y="12" width="124" height="116"/></clipPath>']
    p.append(L(6, 116, 128, 116, 1.0, ar=True) + L(22, 128, 22, 12, 1.0, ar=True))
    p.append(R(X(0), Y(2), 44, 44, "#e5e7eb", 1.6))
    bx, by = X(4), Y(4)
    circles = "".join(circ(bx, by, 22 * rr, "none", 1.0, d=dd) for rr, dd in ((2 * math.sqrt(2), None), (math.sqrt(20), "3 2"), (math.sqrt(32), "3 2")))
    p.append('<g clip-path="url(#cl1506)">' + circles + "</g>")
    p.append(dot(bx, by, r=2.2) + N(bx - 4, by - 5, "beacon (4,4)", 7, "end"))
    pts = [(X(0), Y(0)), (X(2), Y(0)), (X(2), Y(2))]
    p.append(arrow(pts[0][0] + 2, pts[0][1], pts[1][0] - 3, pts[1][1], 1.6) + arrow(pts[1][0], pts[1][1] - 2, pts[2][0], pts[2][1] + 3, 1.6))
    for q in pts:
        p.append(dot(*q, r=2.6))
    p.append(N(pts[0][0] + 3, pts[0][1] + 10, "x₀", 8, "start") + N(pts[1][0] + 4, pts[1][1] + 10, "x₁", 8, "start") + N(pts[2][0] + 5, pts[2][1] - 3, "x₂ = x*", 8, "start"))
    p.append(N(X(1), Y(0) + 10, "2", 6.5) if False else "")
    p.append(N(X(1), Y(2) - 3, "wall 4", 6.5) + N(X(0) - 2, Y(1), "wall 1", 6.5, "end") + N(X(1), Y(0) - 3, "wall 2", 6.5) + N(X(2) + 2, Y(1) + 2, "wall 3", 6.5, "start") if False else "")
    p.append(plane(X(1) - 2, Y(0) + 0, 0, .0001) if False else "")
    for y, s in ((16, "min ½‖x − (4,4)‖²"), (27, "1: x₁ ≥ 0   2: x₂ ≥ 0"), (37, "3: x₁ ≤ 2   4: x₂ ≤ 2"), (51, "(0,0), W = {1,2}:"), (61, "p = 0, λ̂ = (−4, −4): drop 1"),
                 (73, "slide p = (4,0), α = ½"), (83, "(2,0), W = {2,3}: λ̂₂ = −4,"), (93, "drop 2, p = (0,4), α = ½"), (105, "(2,2), W = {3,4}: p = 0,"), (115, "λ̂ = (2, 2) ≥ 0: optimal ✓")):
        p.append(N(136, y, s, 6.4, "start"))
    return svg(c, *p)


FIX = {
    1206: {
        "statement": "<b>Question.</b> Minimize $f(x)=x_1+x_2$ subject to $c(x)=x_1^2+x_2^2-1=0$. Find the KKT point and use the bordered Hessian ($m=1$, $n=2$) to decide whether it is a strict local minimizer.",
        "stmtKind": "WORKED EXAMPLE",
        "math": "$$\\begin{aligned}\\nabla f+\\lambda\\nabla c=0&:\\ x_1=x_2=-\\tfrac1{2\\lambda},\\ c=0\\Rightarrow x^*=-\\tfrac1{\\sqrt2}(1,1),\\ \\lambda=\\tfrac1{\\sqrt2}\\\\ J=\\nabla c(x^*)^\\top=(-\\sqrt2,-\\sqrt2),&\\ \\nabla^2_{xx}L=\\sqrt2\\,I\\\\ \\det B=\\det\\begin{bmatrix}0&-\\sqrt2&-\\sqrt2\\\\-\\sqrt2&\\sqrt2&0\\\\-\\sqrt2&0&\\sqrt2\\end{bmatrix}&=-4\\sqrt2\\lt0=(-1)^m\\Rightarrow\\text{strict local min}\\end{aligned}$$",
        "breakdown": [
            "<strong>KKT first:</strong> $\\nabla f=(1,1)$ and $\\nabla c=(2x_1,2x_2)$ must cancel, which forces $x_1=x_2$ and puts the candidates on the ring at $\\pm\\frac1{\\sqrt2}(1,1)$; the south-west point has $\\lambda=1/\\sqrt2$.",
            "<strong>Build $B$:</strong> the border is $J=\\nabla c(x^*)^\\top$ and the inner block is $\\nabla^2_{xx}L=\\nabla^2f+\\lambda\\nabla^2c=\\sqrt2\\,I$.",
            "<strong>Read the sign:</strong> with $m=1$ and $n-m=1$ minor to check, $\\det B=-4\\sqrt2$ has sign $(-1)^m=-1$: a strict local minimum, $f=-\\sqrt2$. At the north-east point ($\\lambda=-1/\\sqrt2$) $\\det B=+4\\sqrt2$, a maximum."
        ],
        "drawingSvg": d1206("1206"),
        "drawingCaption": "Drawn to scale. The lines x₁ + x₂ = −√2, 0, √2 are level sets of f. The lowest one touches the unit circle at the south-west point, where −∇f = λ∇c with λ = 1/√2. Moving along the ring from there only climbs, which is what det B = −4√2 < 0 confirms.",
    },
    1306: {
        "statement": "<b>Question.</b> Project $p=(1.5,\\ 1.0,\\ 0.5,\\ 0.1)$ onto the simplex $\\Delta=\\{x\\ge0,\\ \\mathbf 1^\\top x=1\\}$.",
        "stmtKind": "WORKED EXAMPLE",
        "math": "$$\\begin{aligned}\\text{sorted: }&p_{(1)}=1.5,\\ p_{(2)}=1.0,\\ p_{(3)}=0.5,\\ p_{(4)}=0.1\\\\ k=2:&\\ \\tau=\\frac{\\sum_{i\\le k}p_{(i)}-1}{k}=\\frac{2.5-1}{2}=0.75,\\ \\ p_{(2)}\\gt\\tau\\ge p_{(3)}\\\\ P_\\Delta(p)&=\\max\\{p-\\tau\\mathbf 1,\\,0\\}=(0.75,\\ 0.25,\\ 0,\\ 0)\\end{aligned}$$",
        "breakdown": [
            "<strong>Sort and try $k$:</strong> $k$ is the number of tanks that stay above the level. For $k=3$ the level would be $\\frac{3.0-1}{3}=0.67\\gt p_{(3)}=0.5$, so the third tank would go dry: $k=2$.",
            "<strong>$\\tau=\\frac{2.5-1}{2}=0.75$:</strong> the extra over 1 in the two largest tanks, shared equally; it satisfies $p_{(2)}=1.0\\gt\\tau\\ge p_{(3)}=0.5$.",
            "<strong>$\\max\\{p-\\tau\\mathbf 1,0\\}=(0.75,0.25,0,0)$:</strong> the last two tanks are clipped to empty, the rest sum to $1$, so this is the nearest point of the simplex."
        ],
        "drawingSvg": d1306("1306"),
        "drawingCaption": "Bars drawn to scale (50 px per unit). The dashed line is the common level τ = 0.75. The dark parts above it, 0.75 and 0.25, are what remains, and the two short tanks are clipped to empty, so P_Δ(p) = (0.75, 0.25, 0, 0) sums to 1.",
    },
    1406: {
        "statement": "<b>Question.</b> Take $f(x)=\\tfrac12(x_1-2)^2+x_2^2+3x_2$ on $C=\\{x\\ge0\\}$ with $\\alpha=1$. Run projected gradient from $x_0=(1,1)$ and decide whether the method stops.",
        "stmtKind": "WORKED EXAMPLE",
        "math": "$$\\begin{aligned}\\nabla f(x_0)=(-1,5):&\\ x_0-\\alpha\\nabla f(x_0)=(2,-4)\\Rightarrow x_1=P_C=\\max\\{(2,-4),0\\}=(2,0)\\\\ \\nabla f(x_1)=(0,3):&\\ x_1-\\alpha\\nabla f(x_1)=(2,-3)\\Rightarrow x_2=\\max\\{(2,-3),0\\}=(2,0)=x_1\\end{aligned}$$",
        "breakdown": [
            "<strong>$x_0-\\alpha\\nabla f(x_0)=(1,1)-(-1,5)=(2,-4)$:</strong> the plain downhill step dives below the ground ($x_2\\lt0$), outside $C$.",
            "<strong>$\\max\\{\\cdot,0\\}$ clamps the negative coordinate:</strong> the plane lands on the ground at $x_1=(2,0)$; the coordinate $2$ was already legal and is untouched.",
            "<strong>The next step gives $(2,0)$ again:</strong> $x_1=P_C(x_1-\\alpha\\nabla f(x_1))$ is a fixed point, which is exactly the optimality condition (the unconstrained minimum $(2,-1.5)$ lies outside $C$)."
        ],
        "drawingSvg": d1406("1406"),
        "drawingCaption": "Drawn to scale. The ovals are level sets of f, centred at the unconstrained minimum (2, −1.5), which is outside the shaded orthant. From x₀ = (1,1) the gradient step lands at (2, −4), below the ground; clamping brings it to (2, 0), and one more step returns to the same point.",
    },
    1506: {
        "statement": "<b>Question.</b> Run the active-set method on $\\min\\tfrac12\\|x-(4,4)\\|^2$ subject to $x_1\\ge0$, $x_2\\ge0$, $-x_1\\ge-2$, $-x_2\\ge-2$ (constraints $1,2,3,4$), starting at $x_0=(0,0)$ with $W_0=\\{1,2\\}$.",
        "stmtKind": "WORKED EXAMPLE",
        "math": "$$\\begin{aligned}x_0=(0,0),\\ W=\\{1,2\\}&:\\ p=0,\\ \\hat\\lambda=(-4,-4)\\Rightarrow\\text{drop }1\\\\ W=\\{2\\}&:\\ p=(4,0),\\ \\alpha=\\min\\{1,\\tfrac24\\}=\\tfrac12\\Rightarrow x_1=(2,0),\\ W=\\{2,3\\}\\\\ x_1:&\\ p=0,\\ \\hat\\lambda_2=-4\\lt0\\Rightarrow\\text{drop }2;\\ p=(0,4),\\ \\alpha=\\tfrac12\\Rightarrow x_2=(2,2),\\ W=\\{3,4\\}\\\\ x_2:&\\ p=0,\\ \\hat\\lambda=(2,2)\\ge0\\Rightarrow x^*=(2,2)\\end{aligned}$$",
        "breakdown": [
            "<strong>At $(0,0)$ both walls $x_1\\ge0$, $x_2\\ge0$ are in $W$:</strong> $p=0$ and the multipliers are $\\hat\\lambda=(-4,-4)\\lt0$, so gravity wants you off them; drop wall 1.",
            "<strong>Slide along $x_2=0$:</strong> the step $p=(4,0)$ would reach $x_1=4$, but wall 3 ($x_1\\le2$) blocks at $\\alpha=\\frac24=\\frac12$; stop at $(2,0)$ and add wall 3. There wall 2 has $\\hat\\lambda_2=-4\\lt0$, so drop it and slide up to wall 4 the same way.",
            "<strong>At $(2,2)$ with $W=\\{3,4\\}$:</strong> $p=0$ and $\\hat\\lambda=(2,2)\\ge0$, so no wall wants to be dropped: the optimum, the legal point nearest the beacon $(4,4)$."
        ],
        "drawingSvg": d1506("1506"),
        "drawingCaption": "Drawn to scale. The shaded square is the legal region 0 ≤ x ≤ 2. The ovals are circles around the beacon (4,4) through (2,2), (2,0) and (0,0). The plane slides (0,0) → (2,0) → (2,2); each hop is stopped by a wall and ends at the legal point nearest the beacon.",
    },
}
