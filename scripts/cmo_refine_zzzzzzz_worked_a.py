"""Worked-example cards (topics 10-11): statement = the question, math = the solution, breakdown = reading the solution; diagrams drawn to scale."""
import math
from air_lib import *
from dip_lib import E

# ---------- 1007: Farkas with real numbers (drawn to scale: 38 px per unit) ----------
def d1007(c):
    O, U = (46, 100), 38
    X = lambda u: O[0] + U * u
    Y = lambda v: O[1] - U * v
    p = []
    p.append('<polygon points="46,100 176,100 176,10 136,10" fill="#e5e7eb"/>')
    p.append(L(34, 100, 178, 100, 1.1) + L(46, 110, 46, 10, 1.1))
    p.append(L(34, 112, 136, 10, 1.1, d="4 3"))
    for u in (1, 2, 3):
        p.append(L(X(u), 97, X(u), 103, 1.0) + N(X(u), 111, str(u), 7))
    for v in (1, 2):
        p.append(L(43, Y(v), 49, Y(v), 1.0) + N(40, Y(v) + 2.5, str(v), 7, "end"))
    p.append(arrow(46, 100, X(1) - 3, 100, 1.2) + it(X(1) - 2, 91, "a₁", 9.5, "end"))
    p.append(arrow(46, 100, X(1) - 2, Y(1) + 2, 1.2) + it(X(1) - 4, Y(1) - 2, "a₂", 9.5, "end"))
    p.append(arrow(46, 100, X(2) - 3, Y(1) + 1.5, 1.2) + dot(X(2), Y(1), r=2.6) + it(X(2) + 4, Y(1) - 3, "b ✓", 9, "start"))
    p.append(dot(46, Y(1), r=2.6) + it(46, Y(1) - 7, "b′ ✗", 9, "middle"))
    p.append(arrow(46, 100, X(0.6), Y(-0.6) - 2, 1.2) + it(X(0.6) + 4, Y(-0.6) + 3, "y = (1,−1)", 9, "start"))
    p.append(dot(46, 100, r=2.2))
    p.append(N(148, 66, "cone(a₁, a₂)", 7.5) + N(148, 78, "y·x ≥ 0 side", 7.5))
    p.append(N(54, 36, "y·x < 0 side", 7.5, "start") + N(172, 111, "x₁", 7.5, "end") + N(52, 14, "x₂", 7.5, "start"))
    p.append(N(236, 134, "y·a₁ = 1, y·a₂ = 0, y·b′ = −1", 7.5, "end"))
    p.append(N(236, 124, "b = (2,1), b′ = (0,1)", 7.5, "end"))
    return svg(c, *p)

# ---------- 1006: KKT from Farkas at a corner ----------
def d1006(c):
    Px, Py = 120, 88
    n2 = (0.447, -0.894)
    p = ['<polygon points="120,88 120,138 20,138 20,38" fill="#e5e7eb"/>']
    p.append(wall(Px, Py, Px, 138, -1, 0, 6, 6, 1.2))
    p.append(wall(Px, Py, 20, 38, -n2[0], -n2[1], 8, 6, 1.2))
    l1 = (30, 0)
    l2 = (16, -32)
    tot = (l1[0] + l2[0], l1[1] + l2[1])
    p.append(dash(Px + l1[0], Py, Px + tot[0], Py + tot[1]) + dash(Px + l2[0], Py + l2[1], Px + tot[0], Py + tot[1]))
    p.append(arrow(Px, Py, Px + l1[0] - 2, Py, 1.2) + it(Px + l1[0] + 3, Py + 3, "λ₁∇c₁", 9, "start"))
    p.append(arrow(Px, Py, Px + l2[0] - 1, Py + l2[1] + 2, 1.2) + it(Px + l2[0] - 4, Py + l2[1] - 4, "λ₂∇c₂", 9, "end"))
    p.append(arrow(Px, Py, Px + tot[0] - 2, Py + tot[1] + 1.5, 1.6) + it(Px + tot[0] + 3, Py + tot[1] - 2, "−∇f", 9.5, "start"))
    p.append(plane(Px - 10, Py + 7, -35, .6) + dot(Px, Py, r=2.6) + it(Px + 5, Py + 15, "x*", 9.5, "start"))
    p.append(N(66, 122, "feasible: c₁ ≤ 0, c₂ ≤ 0", 7.5) + N(66, 132, "no downhill heading here", 7.5))
    p.append(N(Px + 6, 134, "wall c₁", 7.5, "start") + N(26, 32, "wall c₂", 7.5, "start"))
    p.append(N(180, 119, "−∇f = λ₁∇c₁ + λ₂∇c₂", 8.5) + N(180, 130, "λᵢ ≥ 0, i ∈ 𝒜(x*)", 8))
    return svg(c, *p)

# ---------- 1106: minimise x1^2 + 4 x2^2 subject to x1 + x2 >= 1 (to scale: 72 px per unit) ----------
def d1106(c):
    X = lambda u: 34 + 72 * u
    Y = lambda v: 98 - 72 * v
    p = ['<clipPath id="cl1106"><rect x="20" y="10" width="130" height="108"/></clipPath>']
    p.append('<polygon points="20,12 126,118 20,118" fill="#e5e7eb"/>')
    p.append(L(20, 98, 150, 98, 1.1, ar=True) + L(34, 118, 34, 10, 1.1, ar=True))
    p.append(L(20, 12, 126, 118, 1.2))
    p.append('<g clip-path="url(#cl1106)">' + "".join(E(34, 98, 72 * math.sqrt(k), 36 * math.sqrt(k), 0, "none", 1.0, d=dd) for k, dd in ((0.2, "3 2"), (0.8, None), (1.8, "3 2"))) + "</g>")
    p.append(dot(34, 98, r=2.4) + N(28, 94, "O", 8, "end"))
    sx, sy = X(0.8), Y(0.2)
    p.append(arrow(sx, sy, sx - 22, sy + 22, 1.4) + N(sx - 24, sy + 30, "−∇f", 8, "end"))
    p.append(arrow(X(0.5), Y(0.5), X(0.5) - 14, Y(0.5) + 14, 1.2) + N(X(0.5) - 16, Y(0.5) + 4, "∇g", 8, "end"))
    p.append(dot(sx, sy, r=2.8) + plane(sx + 9, sy - 9, 135, .55))
    p.append(N(148, 108, "x₁", 7.5, "end") + N(40, 18, "x₂", 7.5, "start"))
    for y, s in ((26, "f = x₁² + 4x₂²"), (36, "(ovals = level sets)"), (52, "g = 1 − x₁ − x₂ ≤ 0"), (62, "wall: x₁ + x₂ = 1"),
                 (78, "x* = (4/5, 1/5)"), (88, "μ* = 8/5 > 0 ✓"), (104, "O: g = 1 > 0 ✗")):
        p.append(N(156, y, s, 7, "start"))
    p.append(N(120, 138, "Case 2: oval f = 4/5 just touches the wall", 8))
    return svg(c, *p)

FIX = {
    1007: {
        "statement": "<b>Question.</b> The walls have normals $a_1=(1,0)$ and $a_2=(1,1)$, so $A=\\begin{pmatrix}1&1\\\\0&1\\end{pmatrix}$. Is $b=(2,1)$ in $\\operatorname{cone}(a_1,a_2)$? Is $b'=(0,1)$? If not, find the Farkas certificate $y$.",
        "stmtKind": "WORKED EXAMPLE",
        "math": "$$\\begin{aligned}b=(2,1):&\\ x_1+x_2=2,\\ x_2=1\\Rightarrow x=(1,1)\\ge0\\ \\checkmark\\\\ b'=(0,1):&\\ x_1+x_2=0,\\ x_2=1\\Rightarrow x_1=-1\\lt0\\ \\times\\\\ \\text{Certificate } y=(1,-1):&\\ A^\\top y=(1,0)\\ge0,\\ \\ b'^\\top y=-1\\lt0\\end{aligned}$$",
        "breakdown": [
            "<strong>Test $b$:</strong> solving $Ax=b$ gives $x=(1,1)\\ge0$, so $b=a_1+a_2$ is inside the cone and no certificate can exist.",
            "<strong>Test $b'$:</strong> the equations force $x_1=-1\\lt0$, so $b'$ is outside the cone and Farkas says some $y$ must exist.",
            "<strong>Find $y$:</strong> take $y$ perpendicular to the cone edge $a_2$, pointing into the cone: $y=(1,-1)$ has $a_1^\\top y=1$, $a_2^\\top y=0$, yet $b'^\\top y=-1\\lt0$."
        ],
        "drawingSvg": d1007("1007"),
        "drawingCaption": "Drawn to scale. The shaded wedge is cone(a₁, a₂). b = (2,1) = a₁ + a₂ lies inside it. The dashed line is y·x = 0 for y = (1,−1): it runs along a₂, the cone is on its y·x ≥ 0 side, and b′ = (0,1) is on the other side because b′ᵀy = −1 < 0.",
    },
    1006: {
        "statement": "<b>Question.</b> Let $x^*$ be a local minimizer with $T_\\Omega(x^*)=\\mathcal F(x^*)$ (e.g. under LICQ). Show there are multipliers $\\lambda_i$ ($\\lambda_i\\ge0$ for active inequalities) with $\\nabla f(x^*)+\\sum_{i\\in\\mathcal A(x^*)}\\lambda_i\\nabla c_i(x^*)=0$.",
        "stmtKind": "WORKED EXAMPLE",
        "math": "$$\\begin{aligned}x^*\\text{ local min}&\\Rightarrow\\nabla f(x^*)^\\top d\\ge0\\ \\ \\forall d\\in\\mathcal F(x^*)\\\\&\\Rightarrow\\nexists\\,d:\\ \\nabla f(x^*)^\\top d\\lt0,\\ \\nabla c_i(x^*)^\\top d\\le0,\\ i\\in\\mathcal A(x^*)\\\\&\\Rightarrow(\\text{Farkas})\\ \\ -\\nabla f(x^*)=\\sum_{i\\in\\mathcal A(x^*)}\\lambda_i\\nabla c_i(x^*),\\ \\lambda_i\\ge0\\end{aligned}$$",
        "breakdown": [
            "<strong>Local minimum:</strong> no feasible direction goes downhill, so $\\nabla f(x^*)^\\top d\\ge0$ for every $d$ with $\\nabla c_i(x^*)^\\top d\\le0$ (this is where $T_\\Omega=\\mathcal F$ is used).",
            "<strong>Rewrite as a failed system:</strong> that says no $d$ has $\\nabla f^\\top d\\lt0$ together with all $\\nabla c_i^\\top d\\le0$; this is exactly alternative (ii) of Farkas failing.",
            "<strong>So alternative (i) holds:</strong> $-\\nabla f(x^*)$ lies in the cone of the active normals $\\nabla c_i(x^*)$, which is the KKT balance with $\\lambda_i\\ge0$."
        ],
        "drawingSvg": d1006("1006"),
        "drawingCaption": "The shaded wedge is the feasible set near x* (c₁ ≤ 0 and c₂ ≤ 0). Every wall normal ∇cᵢ points out of it. No feasible heading goes downhill, so −∇f is trapped in the cone of the normals: −∇f = λ₁∇c₁ + λ₂∇c₂, the diagonal of the dashed parallelogram, with λᵢ ≥ 0.",
    },
    1106: {
        "statement": "<b>Question.</b> Minimize $f(x)=x_1^2+4x_2^2$ subject to $g(x)=1-x_1-x_2\\le0$. Find the KKT point by trying the two active sets: wall inactive ($\\mu=0$) and wall active ($g=0$).",
        "stmtKind": "WORKED EXAMPLE",
        "math": "$$\\begin{aligned}\\mu=0:&\\ \\nabla f=(2x_1,8x_2)=0\\Rightarrow x=(0,0),\\ g(0,0)=1\\gt0\\ \\times\\\\ g=0:&\\ 2x_1-\\mu=0,\\ 8x_2-\\mu=0,\\ x_1+x_2=1\\Rightarrow\\tfrac{5\\mu}{8}=1\\\\ &\\mu^*=\\tfrac85\\gt0,\\ \\ x^*=\\left(\\tfrac45,\\tfrac15\\right),\\ \\ f(x^*)=\\tfrac45\\ \\checkmark\\end{aligned}$$",
        "breakdown": [
            "<strong>Case $\\mu=0$:</strong> with the wall switched off, $\\nabla f=0$ puts you at the origin, but $g(0,0)=1\\gt0$ breaks the constraint, so this case is rejected.",
            "<strong>Case $g=0$:</strong> stationarity $\\nabla f+\\mu\\nabla g=0$ gives $x_1=\\mu/2$ and $x_2=\\mu/8$; putting them on the wall $x_1+x_2=1$ gives $\\mu^*=8/5$ and $x^*=(4/5,1/5)$.",
            "<strong>Check:</strong> $\\mu^*\\gt0$ (dual feasibility), $g(x^*)=0$ (primal feasibility and complementary slackness), and $f$ is convex, so $x^*$ is the global minimum."
        ],
        "drawingSvg": d1106("1106"),
        "drawingCaption": "Drawn to scale. The ovals are level sets of f = x₁² + 4x₂². The shaded side of the line x₁ + x₂ = 1 is illegal (g > 0) and contains the origin, the Case 1 answer. The oval f = 4/5 just touches the wall at x* = (4/5, 1/5), where −∇f = (8/5)∇g.",
    },
}
