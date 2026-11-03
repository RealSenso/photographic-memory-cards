"""Worked examples (topics 16-19): question / solution math / breakdown, diagrams drawn from the real numbers."""
import math
from air_lib import *
from dip_lib import E

# the numbers used below, checked here once
_r = (math.sqrt(13) - 1) / 6
_Z = 1 + _r + _r * _r
_P = [1 / _Z, _r / _Z, _r * _r / _Z]
_BETA = -math.log(_r)
assert abs((_P[1] + 2 * _P[2]) - 0.5) < 1e-9


# ---------------- 1606: two-point hard-margin SVM ----------------
def d1606(c):
    X = lambda u: 24 + 24 * u
    Y = lambda v: 108 - 24 * v
    p = ['<clipPath id="cl1606"><rect x="8" y="10" width="112" height="120"/></clipPath>']
    p.append(L(8, 108, 118, 108, 1.0, ar=True) + L(24, 128, 24, 10, 1.0, ar=True))
    strip = [(-2, 2), (6, -6), (10, -6), (-2, 6)]
    p.append('<g clip-path="url(#cl1606)"><polygon points="%s" fill="#e5e7eb"/>' % " ".join(f"{X(a):.1f},{Y(b):.1f}" for a, b in strip))
    for k, dd in ((0, None), (2, "4 3"), (4, None)):
        p.append(L(f(X(-2)), f(Y(k + 2)), f(X(k + 2)), f(Y(-2)), 1.3 if dd is None else 1.0, d=dd))
    p.append("</g>")
    p.append(dot(X(0), Y(0), r=3, ) + dot(X(2), Y(2), r=3))
    p.append(circ(X(0), Y(0), 6, "none", 1.0) + circ(X(2), Y(2), 6, "none", 1.0))
    p.append(N(X(0) + 8, Y(0) + 11, "x₁  (y = −1)", 7.5, "start") + N(X(2) - 8, Y(2) - 8, "x₂  (y = +1)", 7.5, "end"))
    p.append(arrow(X(1), Y(1), X(1.5) - 2, Y(1.5) + 2, 1.4) + N(X(1.5) + 3, Y(1.5) + 8, "w", 8.5, "start"))
    for y, s in ((16, "x₁ = (0,0), y₁ = −1"), (27, "x₂ = (2,2), y₂ = +1"), (41, "Σαᵢyᵢ = 0: α₁ = α₂ = α"), (52, "w = α(2, 2)"),
                 (64, "−b = 1 ⇒ b = −1"), (75, "8α + b = 1 ⇒ α = ¼"), (89, "w = (½, ½),  b = −1"), (100, "margin = 2/‖w‖ = 2√2"), (111, "½‖w‖² = ¼ = Σα − ½‖w‖²")):
        p.append(N(128, y, s, 6.8, "start"))
    p.append(N(70, 138, "w·x + b = 0 (dashed), ±1 (solid)", 7))
    return svg(c, *p)


# ---------------- 1703: min 1/2|x|^2 s.t. x1 + x2 >= 2, and its Wolfe dual ----------------
def d1703(c):
    X = lambda u: 22 + 30 * u
    Y = lambda v: 100 - 30 * v
    p = ['<clipPath id="cl1703"><rect x="10" y="22" width="92" height="84"/></clipPath>']
    p.append('<polygon points="22,40 82,100 22,100" fill="#e5e7eb"/>')
    p.append(L(10, 100, 100, 100, 1.0, ar=True) + L(22, 106, 22, 24, 1.0, ar=True))
    p.append('<g clip-path="url(#cl1703)">' + "".join(circ(X(0), Y(0), 30 * r, "none", 1.0, d=dd) for r, dd in ((1.0, "3 2"), (math.sqrt(2), None), (2.0, "3 2"))) + "</g>")
    p.append(L(14, Y(2.27), 98, Y(-0.27), 1.4) if False else L(f(X(-0.25)), f(Y(2.25)), f(X(2.25)), f(Y(-0.25)), 1.4))
    sx, sy = X(1), Y(1)
    p.append(dot(sx, sy, r=2.8) + arrow(sx, sy, sx + 16, sy - 16, 1.2) + N(sx + 18, sy - 16, "∇f", 8, "start"))
    p.append(N(sx - 6, sy + 14, "x* = (1,1)", 7.5, "end"))
    p.append(N(56, 14, "primal: min ½‖x‖², x₁ + x₂ ≥ 2", 7.5))
    Xd = lambda l: 136 + 34 * l
    Yd = lambda g: 100 - 52 * g
    p.append(L(126, 100, 222, 100, 1.0, ar=True) + L(136, 106, 136, 24, 1.0, ar=True))
    p.append(poly([(Xd(l), Yd(-l * l + 2 * l)) for l in [i * 2.0 / 50 for i in range(51)]], 1.4))
    p.append(dot(Xd(1), Yd(1), r=2.8) + L(f(Xd(1)), f(Yd(1)), f(Xd(1)), 100, 1.0, d="3 2"))
    p.append(N(Xd(1), 112, "λ = 1", 7.5) + N(Xd(1) + 6, Yd(1) - 4, "d* = 1", 7.5, "start") + N(226, 112, "λ", 7.5, "end"))
    p.append(N(176, 14, "dual: max −λ² + 2λ", 7.5))
    p.append(N(120, 128, "x = λ(1,1),  ∇f = λa,  λ* = 1,  p* = d* = 1", 7.5))
    p.append(N(56, 138, "dashed ovals: ½‖x‖² = ½, 2", 6.8))
    return svg(c, *p)


# ---------------- 1706: max entropy with mean energy 0.5 ----------------
def d1706(c):
    base, U = 116, 110
    xs = [30, 64, 98]
    p = [L(14, base, 132, base, 1.1)]
    for x0, v, e in zip(xs, _P, (0, 1, 2)):
        h = v * U
        p.append(R(x0, base - h, 26, h, "#f1f5f9", 1.2))
        p.append(N(x0 + 13, base - h - 3, f"{v:.3f}", 7.5) + N(x0 + 13, base + 10, f"E = {e}", 7.5))
    p.append(L(14, base - U / 3, 132, base - U / 3, 1.0, d="4 3") + N(12, base - U / 3 - 3, "⅓", 7.5, "start"))
    p.append(poly([(43 + 34 * e, base - U * math.exp(-_BETA * e) / _Z) for e in [i * 2.2 / 40 for i in range(41)]], 1.2))
    for y, s in ((16, "max −Σ pᵢ ln pᵢ"), (27, "Σ pᵢ = 1,  Σ pᵢEᵢ = 0.5"), (40, "pᵢ = e^(−βEᵢ)/Z,  r = e^(−β)"), (51, "Ē = (r + 2r²)/(1 + r + r²) = ½"),
                 (62, "3r² + r − 1 = 0"), (73, "r = (√13 − 1)/6 ≈ %.3f" % _r), (84, "β ≈ %.3f" % _BETA), (98, "p ≈ (%.3f, %.3f, %.3f)" % tuple(_P)),
                 (109, "H ≈ 0.90  (uniform: 1.10)")):
        p.append(N(140, y, s, 6.8, "start"))
    p.append(N(70, 138, "bars: the Boltzmann p, curve: e^(−βE)/Z", 7))
    return svg(c, *p)


# ---------------- 1806: LP and its dual, both solved graphically ----------------
def d1806(c):
    X = lambda u: 14 + 18 * u
    Y = lambda v: 116 - 18 * v
    Xd = lambda u: 130 + 18 * u
    p = ['<clipPath id="cl1806a"><rect x="10" y="12" width="96" height="108"/></clipPath><clipPath id="cl1806b"><rect x="126" y="12" width="100" height="108"/></clipPath>']
    p.append(L(10, 116, 104, 116, 1.0, ar=True) + L(14, 120, 14, 12, 1.0, ar=True) + L(126, 116, 224, 116, 1.0, ar=True) + L(130, 120, 130, 12, 1.0, ar=True))
    prim = [(0, 0), (3.5, 0), (2, 3), (0, 5)]
    p.append('<polygon points="%s" fill="#e5e7eb" stroke="#000000" stroke-width="1.2"/>' % " ".join(f"{X(a):.1f},{Y(b):.1f}" for a, b in prim))
    p.append('<g clip-path="url(#cl1806a)">' + L(f(X(0)), f(Y(6)), f(X(4)), f(Y(0)), 1.0, d="4 3") + "</g>")
    p.append(dot(X(2), Y(3), r=2.8) + N(X(2) + 4, Y(3) - 4, "x* = (2,3)", 7.5, "start"))
    dual = [(0, 3), (1, 1), (3, 0), (4.5, 0), (4.5, 5.5), (0, 5.5)]
    p.append('<g clip-path="url(#cl1806b)"><polygon points="%s" fill="#e5e7eb" stroke="#000000" stroke-width="1.2"/>' % " ".join(f"{Xd(a):.1f},{Y(b):.1f}" for a, b in dual)
             + L(f(Xd(0)), f(Y(12 / 7)), f(Xd(2.4)), f(Y(0)), 1.0, d="4 3") + "</g>")
    p.append(dot(Xd(1), Y(1), r=2.8) + N(Xd(1) + 4, Y(1) + 11, "y* = (1,1)", 7.5, "start"))
    p.append(N(56, 24, "primal (max)", 8) + N(176, 24, "dual (min)", 8))
    p.append(N(70, 133, "x₁ + x₂ ≤ 5,  2x₁ + x₂ ≤ 7", 6.8) + N(176, 133, "y₁ + 2y₂ ≥ 3,  y₁ + y₂ ≥ 2", 6.8))
    p.append(N(70, 142, "3x₁ + 2x₂ = 12 (dashed)", 6.8) + N(176, 142, "5y₁ + 7y₂ = 12 (dashed)", 6.8))
    p.append(N(120, 10, "c·x* = b·y* = 12", 8))
    return svg(c, *p)


# ---------------- 1906: augmented Lagrangian on min x1^2 + x2^2, x1 + x2 = 2, c = 2 ----------------
def d1906(c):
    X = lambda u: 20 + 70 * u
    Y = lambda v: 126 - 70 * v
    p = ['<clipPath id="cl1906"><rect x="14" y="10" width="130" height="118"/></clipPath>']
    p.append(L(14, 126, 142, 126, 1.0, ar=True) + L(20, 128, 20, 10, 1.0, ar=True))
    p.append('<g clip-path="url(#cl1906)">' + circ(X(0), Y(0), 70 * math.sqrt(2), "none", 1.0, d="3 2") + L(f(X(0)), f(Y(2)), f(X(2)), f(Y(0)), 1.4)
             + L(f(X(0)), f(Y(0)), f(X(1.6)), f(Y(1.6)), 1.0, d="2 3") + "</g>")
    its = [2 / 3, 8 / 9, 26 / 27, 1.0]
    for t in its[:-1]:
        p.append(dot(X(t), Y(t), r=2.4))
    p.append(dot(X(1), Y(1), r=3.2))
    p.append(poly([(X(t), Y(t)) for t in its], 1.3))
    p.append(N(X(2 / 3) - 4, Y(2 / 3) + 10, "x⁽⁰⁾ = (2/3, 2/3)", 6.8, "start") if False else N(X(2 / 3) + 4, Y(2 / 3) + 11, "t = 2/3", 7, "start"))
    p.append(N(X(1) + 6, Y(1) + 12, "x* = (1,1)", 7.5, "start") + N(X(0.1), Y(1.9) - 3, "x₁ + x₂ = 2", 7, "start"))
    for y, s in ((14, "min x₁² + x₂²"), (24, "h = x₁ + x₂ − 2,  c = 2"), (38, "x = (t, t),"), (48, "t = (8 − 2λ)/12"), (62, "λ₀ = 0:       t = 2/3"), (73, "λ₁ = −4/3:  t = 8/9"),
                 (84, "λ₂ = −16/9: t = 26/27"), (98, "λₖ → λ* = −2"), (109, "xₖ → (1, 1)"), (122, "λₖ₊₁ = λₖ + c·h(xₖ)")):
        p.append(N(150, y, s, 6.8, "start"))
    return svg(c, *p)


FIX = {
    1606: {
        "statement": "<b>Question.</b> Two points: $x_1=(0,0)$ with $y_1=-1$ and $x_2=(2,2)$ with $y_2=+1$. Find the hard-margin SVM $(w,b)$, the multipliers $\\alpha_i$ and the margin.",
        "stmtKind": "WORKED EXAMPLE",
        "math": "$$\\begin{aligned}\\textstyle\\sum_i\\alpha_iy_i=0\\Rightarrow\\alpha_1=\\alpha_2=\\alpha,&\\ \\ w=\\sum_i\\alpha_iy_ix_i=\\alpha(2,2)\\\\ y_1(w^\\top x_1+b)=1\\Rightarrow b=-1,&\\ \\ y_2(w^\\top x_2+b)=8\\alpha-1=1\\Rightarrow\\alpha=\\tfrac14\\\\ w=\\left(\\tfrac12,\\tfrac12\\right),\\ b=-1,&\\ \\ \\text{margin}=\\tfrac{2}{\\|w\\|}=2\\sqrt2,\\ \\ \\tfrac12\\|w\\|^2=\\tfrac14\\end{aligned}$$",
        "breakdown": [
            "<strong>Both points are support vectors:</strong> each must touch its edge of the strip, so $y_i(w^\\top x_i+b)=1$ for both, and the dual constraint $\\sum\\alpha_iy_i=0$ forces $\\alpha_1=\\alpha_2=\\alpha$.",
            "<strong>$w=\\sum\\alpha_iy_ix_i=\\alpha(x_2-x_1)=\\alpha(2,2)$:</strong> the strip's normal points from $x_1$ to $x_2$. The first point gives $b=-1$, the second gives $8\\alpha-1=1$, so $\\alpha=\\frac14$.",
            "<strong>$w=(\\tfrac12,\\tfrac12)$:</strong> the margin $2/\\|w\\|=2\\sqrt2$ equals the distance between the two points, and primal $\\tfrac12\\|w\\|^2=\\tfrac14$ equals the dual value $\\sum\\alpha_i-\\tfrac12\\|w\\|^2=\\tfrac14$."
        ],
        "drawingSvg": d1606("1606"),
        "drawingCaption": "Drawn to scale. The dashed line x₁ + x₂ = 2 is w·x + b = 0 and the solid lines x₁ + x₂ = 0 and 4 are w·x + b = ∓1. Both points sit on the edges (support vectors, α = ¼ each), and the strip between the solid lines is the margin 2/‖w‖ = 2√2.",
    },
    1703: {
        "statement": "<b>Question.</b> Take $Q=I$, $c=0$, $A=(1\\ \\ 1)$, $b=2$: $\\min\\tfrac12\\|x\\|^2$ s.t. $x_1+x_2\\ge2$. Write the Wolfe dual, solve both problems and compare the values.",
        "stmtKind": "WORKED EXAMPLE",
        "math": "$$\\begin{aligned}\\text{primal: }&x^*=(1,1),\\ p^*=1\\\\ \\text{dual: }&\\max_{x,\\lambda}-\\tfrac12x^\\top Qx+b^\\top\\lambda\\ \\ \\text{s.t.}\\ Qx+c-A^\\top\\lambda=0,\\ \\lambda\\ge0\\\\ &x=\\lambda(1,1)\\Rightarrow-\\lambda^2+2\\lambda,\\ \\ \\max_{\\lambda\\ge0}=1\\ \\text{at}\\ \\lambda^*=1\\ \\Rightarrow\\ d^*=p^*=1\\end{aligned}$$",
        "breakdown": [
            "<strong>Primal:</strong> the closest point to the origin on or above the line $x_1+x_2=2$ is $(1,1)$, with $\\tfrac12\\|x\\|^2=1$.",
            "<strong>Dual constraint $Qx+c-A^\\top\\lambda=0$:</strong> here $x=\\lambda(1,1)$, the equilibrium where the slope $\\nabla f=x$ equals the wall push $\\lambda a$ with $a=(1,1)$.",
            "<strong>Substituting gives $-\\lambda^2+2\\lambda$,</strong> maximised at $\\lambda^*=1$ with value $1$: the same quadratic with the opposite sign plus the resource value, and $d^*=p^*$."
        ],
        "drawingSvg": d1703("1703"),
        "drawingCaption": "Left: drawn to scale, the ovals ½‖x‖² = ½, 1, 2 and the wall x₁ + x₂ = 2. The oval through (1,1) just touches the wall, where ∇f = (1,1) = λa with λ = 1. Right: the dual function −λ² + 2λ peaks at λ = 1 with value 1 = p*.",
    },
    1706: {
        "statement": "<b>Question.</b> Three energy levels $E=(0,1,2)$ with mean energy $\\bar E=0.5$. Find the distribution $p$ that maximises $-\\sum_ip_i\\log p_i$ subject to $\\sum_ip_i=1$ and $\\sum_ip_iE_i=\\bar E$.",
        "stmtKind": "WORKED EXAMPLE",
        "math": "$$\\begin{aligned}p_i&=\\frac{e^{-\\beta E_i}}{\\sum_je^{-\\beta E_j}}=\\frac{(1,\\ r,\\ r^2)_i}{1+r+r^2},\\ \\ r=e^{-\\beta}\\\\ \\bar E&=\\frac{r+2r^2}{1+r+r^2}=\\tfrac12\\Rightarrow3r^2+r-1=0,\\ \\ r=\\tfrac{\\sqrt{13}-1}{6}\\approx0.434\\\\ p&\\approx(0.616,\\ 0.268,\\ 0.116),\\ \\ \\beta\\approx0.834\\end{aligned}$$",
        "breakdown": [
            "<strong>Stationarity of the Lagrangian</strong> gives $-\\log p_i-1-\\nu-\\beta E_i=0$, so $p_i\\propto e^{-\\beta E_i}$: exponential in the energy, the Boltzmann form, with $\\beta$ the multiplier of the energy constraint.",
            "<strong>Fix $\\beta$ with the energy budget:</strong> write $r=e^{-\\beta}$, then $\\bar E=\\frac{r+2r^2}{1+r+r^2}=\\frac12$ reduces to $3r^2+r-1=0$, so $r=\\frac{\\sqrt{13}-1}6\\approx0.434$ and $\\beta=-\\ln r\\approx0.834$.",
            "<strong>Read off $p$:</strong> $(1,r,r^2)/(1+r+r^2)\\approx(0.616,0.268,0.116)$, which has mean energy $0.5$; the unconstrained maximum would be the uniform $(\\tfrac13,\\tfrac13,\\tfrac13)$ with mean $1$."
        ],
        "drawingSvg": d1706("1706"),
        "drawingCaption": "Bars drawn to scale: the entropy-maximising p = (0.616, 0.268, 0.116) at E = 0, 1, 2. They sit on the exponential curve e^(−βE)/Z with β ≈ 0.834. The dashed line is the uniform 1/3, which would have mean energy 1, not 0.5.",
    },
    1806: {
        "statement": "<b>Question.</b> Solve the LP $\\max\\ 3x_1+2x_2$ s.t. $x_1+x_2\\le5$, $2x_1+x_2\\le7$, $x\\ge0$ graphically. Then solve its dual $\\min\\ 5y_1+7y_2$ s.t. $y_1+2y_2\\ge3$, $y_1+y_2\\ge2$, $y\\ge0$ and compare the optimal values.",
        "stmtKind": "WORKED EXAMPLE",
        "math": "$$\\begin{aligned}\\text{primal vertices }(0,0),(3.5,0),(2,3),(0,5)&:\\ c^\\top x=0,\\ 10.5,\\ 12,\\ 10\\Rightarrow x^*=(2,3)\\\\ \\text{dual vertices }(0,3),(1,1),(3,0)&:\\ b^\\top y=21,\\ 12,\\ 15\\Rightarrow y^*=(1,1)\\\\ c^\\top x^*&=3(2)+2(3)=12=5(1)+7(1)=b^\\top y^*\\end{aligned}$$",
        "breakdown": [
            "<strong>Primal:</strong> the feasible polygon has four corners; the objective $3x_1+2x_2$ is largest at $(2,3)$, where both walls $x_1+x_2=5$ and $2x_1+x_2=7$ are tight, with value $12$.",
            "<strong>Dual:</strong> the feasible region is unbounded with corners $(0,3)$, $(1,1)$, $(3,0)$; the objective $5y_1+7y_2$ is smallest at $(1,1)$, with value $12$.",
            "<strong>Equal values:</strong> $c^\\top x^*=b^\\top y^*=12$, as LP duality guarantees. Complementary slackness explains it: $x^*_1,x^*_2\\gt0$ make both dual constraints tight at $y^*$, and $y^*_1,y^*_2\\gt0$ make both primal walls tight at $x^*$."
        ],
        "drawingSvg": d1806("1806"),
        "drawingCaption": "Drawn to scale. Left: the primal polygon with corners (0,0), (3.5,0), (2,3), (0,5); the dashed line 3x₁ + 2x₂ = 12 touches it only at (2,3). Right: the dual region (unbounded); the dashed line 5y₁ + 7y₂ = 12 touches it only at (1,1). Both optimal values are 12.",
    },
    1906: {
        "statement": "<b>Question.</b> Take $\\min x_1^2+x_2^2$ s.t. $h(x)=x_1+x_2-2=0$ with $c=2$ and $\\lambda_0=0$. Run three outer iterations of $x_k\\in\\arg\\min L_c(x,\\lambda_k)$, $\\lambda_{k+1}=\\lambda_k+c\\,h(x_k)$.",
        "stmtKind": "WORKED EXAMPLE",
        "math": "$$\\begin{aligned}x_k=(t,t),&\\ \\ t=\\frac{4c-2\\lambda_k}{4+4c}=\\frac{8-2\\lambda_k}{12},\\quad\\lambda_{k+1}=\\lambda_k+c\\,h(x_k)\\\\ \\lambda_0=0&:\\ t=\\tfrac23,\\ \\lambda_1=-\\tfrac43;\\ \\ t=\\tfrac89,\\ \\lambda_2=-\\tfrac{16}9;\\ \\ t=\\tfrac{26}{27}\\\\ \\lambda_k&\\to\\lambda^*=-2,\\ \\ x_k\\to(1,1)\\end{aligned}$$",
        "breakdown": [
            "<strong>One inner solve:</strong> by symmetry $x=(t,t)$, and setting the derivative of $2t^2+\\lambda(2t-2)+\\frac c2(2t-2)^2$ to zero gives $t=\\frac{4c-2\\lambda}{4+4c}$. With $c=2$, $\\lambda_0=0$: $t=\\frac23$, so $h=-\\frac23$.",
            "<strong>Multiplier update:</strong> $\\lambda_1=0+2(-\\tfrac23)=-\\tfrac43$ gives $t=\\frac89$; then $\\lambda_2=-\\tfrac43+2(-\\tfrac29)=-\\tfrac{16}9$ gives $t=\\frac{26}{27}$. Each update closes a fixed fraction of the remaining gap.",
            "<strong>Limit:</strong> $\\lambda_k\\to\\lambda^*=-2$ and $x_k\\to(1,1)$, the true constrained minimizer, with the penalty $c=2$ held fixed."
        ],
        "drawingSvg": d1906("1906"),
        "drawingCaption": "Drawn to scale. Each outer iterate lies on the diagonal x₁ = x₂ at t = 2/3, 8/9, 26/27 and creeps onto the constraint x₁ + x₂ = 2, reaching the constrained minimizer (1,1) on the dashed circle x₁² + x₂² = 2, while λₖ climbs 0, −4/3, −16/9, … → −2.",
    },
}
