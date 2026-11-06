"""Practice-question audit of 6 Nov 2026: the content every Topic 10-19 question assumes must be visible on a card face.

G1  a Lagrangian card in Topic 11 right after the four KKT conditions (definition, gradient, Hessian, sign rules)
G2  two convexity closure facts on 3C1
G3  concave minimisation at vertices on the fundamental-theorem-of-LP card
G4  projection onto {Ax = b} on the hyperplane-projection card
G5  the descent lemma stated on the O(1/k) card
G6  the exact l1 penalty on the quadratic-penalty card
G7  exam-critical text that lived only in hidden fields (sufficiency proof, Klee-Minty) moved onto the card face
"""
from air_lib import *
from cmo_refine_zzzzzzzzzz_diagrams import tx

# ---------- 1107: the Lagrangian. At x* on a wall, grad f and mu grad g cancel ----------
def d1107(c):
    p = []
    p.append('<rect x="14" y="24" width="136" height="98" fill="#f1f3f5"/>')
    for r in (30, 50):
        p.append(f'<circle cx="200" cy="72" r="{r}" fill="none" stroke="#000000" stroke-width="0.9" stroke-dasharray="3 2"/>')
    p.append(C("200", "72", 1.8))
    p.append(tx(200, 66, [("f", 2), (" lower", 0)], 6.5))
    p.append(wall(150, 24, 150, 122, 1, 0, n=7, w=1.2))
    p.append(tx(80, 36, [("legal side: g ≤ 0", 0)], 7.5))
    p.append(plane(84, 96, -20, 0.75))
    p.append(arrow(150, 72, 120, 72, 1.2) + tx(118, 66, [("∇", 0), ("f", 2)], 8.5, "end"))
    p.append(arrow(150, 72, 180, 72, 1.2) + tx(176, 86, [("μ∇g", 0)], 8, "middle"))
    p.append(dot(150, 72, r=2.6) + tx(146, 84, [("x*", 2)], 8.5, "end"))
    p.append(tx(222, 128, [("contours of ", 0), ("f", 2)], 6.5, "end"))
    p.append(tx(120, 14, [("L(x, λ, μ) = ", 0), ("f", 2), (" + λ", 0), ("T", 3), ("h + μ", 0), ("T", 3), ("g", 0)], 8.5))
    p.append(tx(120, 140, [("∇", 0), ("x", 1), ("L = ∇", 0), ("f", 2), (" + μ∇g = 0,   μ ≥ 0", 0)], 8.5))
    return svg(c, *p)

NEW = [
    (1101, {
        "id": 1107,
        "category": "Lagrangian Function",
        "title": "The Lagrangian: One Function Holds the Whole Problem",
        "stmtKind": "DEFINITION",
        "statement": "<b>Lagrangian.</b> For $\\min f(x)$ s.t. $h_i(x)=0$ ($i=1,\\dots,p$), $g_j(x)\\le0$ ($j=1,\\dots,m$), the Lagrangian is $L(x,\\lambda,\\mu)=f(x)+\\lambda^\\top h(x)+\\mu^\\top g(x)=f(x)+\\sum_i\\lambda_ih_i(x)+\\sum_j\\mu_jg_j(x)$. KKT stationarity is exactly $\\nabla_xL(x^*,\\lambda^*,\\mu^*)=0$.",
        "math": "$$\\begin{aligned}L(x,\\lambda,\\mu)&=f(x)+\\textstyle\\sum_i\\lambda_ih_i(x)+\\sum_j\\mu_jg_j(x)\\\\ \\nabla_xL&=\\nabla f+\\textstyle\\sum_i\\lambda_i\\nabla h_i+\\sum_j\\mu_j\\nabla g_j\\\\ \\nabla^2_{xx}L&=\\nabla^2f+\\textstyle\\sum_i\\lambda_i\\nabla^2h_i+\\sum_j\\mu_j\\nabla^2g_j\\end{aligned}$$",
        "breakdown": [
            "<strong>$\\nabla_xL=0$ is the stationarity condition of 11C1:</strong> build $L$ once, differentiate in $x$ only, set it to zero.",
            "<strong>$\\nabla^2_{xx}L$ is the Hessian in $x$ with $\\lambda,\\mu$ held fixed:</strong> it is the curvature the second-order tests of Topic 12 check.",
            "<strong>Sign rules:</strong> $g_j\\le0\\Rightarrow\\mu_j\\ge0$; a constraint $g_j\\ge0$ is flipped to $-g_j\\le0$ first (equivalently $L=f-\\mu^\\top g$); equality multipliers $\\lambda_i$ are free in sign; to maximise $f$, minimise $-f$."
        ],
        "hint": "Which single function has the KKT stationarity equation as its $x$-gradient?",
        "personalConnection": "<strong>The airplane analogy.</strong> $L$ is the plane's total bill: altitude $f$, plus a fee $\\mu_j$ for every unit you lean into wall $j$, plus a fee $\\lambda_i$ for drifting off each painted lane $h_i=0$. Parking where the bill is flat in every direction ($\\nabla_xL=0$) is the KKT balance. Wall fees are never negative ($\\mu\\ge0$) because walls only push; lane fees can be either sign because a lane can be left on either side.",
        "drawingSvg": d1107("1107"),
        "drawingCaption": "x* sits on the wall g = 0 with the legal side g ≤ 0 shaded. The contours of f get lower to the right, so ∇f points left, away from the low side; the wall's normal ∇g points out of the legal side. With μ ≥ 0 they cancel: ∇ₓL = ∇f + μ∇g = 0.",
        "coreTranslation": [
            "<strong>What:</strong> the Lagrangian $L(x,\\lambda,\\mu)=f+\\lambda^\\top h+\\mu^\\top g$ adds each constraint to the objective, weighted by its multiplier.",
            "<strong>How:</strong> stationarity is $\\nabla_xL=0$; second-order tests use $\\nabla^2_{xx}L$; signs: $\\mu\\ge0$ for $g\\le0$, flip $g\\ge0$ first, $\\lambda$ free, max becomes min of $-f$.",
            "<strong>Why it matters:</strong> the same function drives KKT (Topic 11), second-order conditions (Topic 12), the dual function $q(\\lambda,\\mu)=\\inf_xL$ (Topic 16) and the penalty and augmented-Lagrangian methods (Topic 19)."
        ],
        "examTrap": "Orientation decides the sign: with $g_j\\le0$ use $L=f+\\mu^\\top g$ and $\\mu\\ge0$. With $g_j\\ge0$ either negate the constraint or write $L=f-\\mu^\\top g$. Equality multipliers have no sign restriction.",
    }),
]

FIX = {
    # G2 · 3C1
    301: {"breakdown": [
        "<strong>$\\theta x+(1-\\theta)y$</strong> is a point on the straight flight path between $x$ and $y$.",
        "<strong>$\\theta f(x)+(1-\\theta)f(y)$</strong> is the height of the straight string stretched between the two altitudes.",
        "<strong>The inequality says the terrain never rises above the string,</strong> which is convexity.",
        "<strong>Two closure facts:</strong> (i) if $f_1,\\dots,f_k$ are convex and $w_i\\ge0$, then $\\sum_iw_if_i$ is convex; (ii) every sublevel set $\\{x:f(x)\\le c\\}$ of a convex $f$ is convex, since $f(x),f(y)\\le c$ gives $f(\\theta x+(1-\\theta)y)\\le\\theta f(x)+(1-\\theta)f(y)\\le c$."]},
    # G5 · 5C3
    502: {
        "statement": "Let $f$ be convex and differentiable with $L$-Lipschitz gradient, and let $x^*$ be a minimizer. <b>Descent lemma:</b> $f(y)\\le f(x)+\\nabla f(x)^\\top(y-x)+\\tfrac L2\\|y-x\\|^2$ for all $x,y$. Gradient descent with constant step $1/L$ satisfies $f(x_k)-f^*\\le\\dfrac{L\\|x_0-x^*\\|^2}{2k}$ for all $k\\ge1$.",
        "breakdown": [
            "<strong>$L$ = the sharpest bend anywhere.</strong> The ground can never curve back up faster than $L$, so a hop of $1/L$ is a safe distance everywhere.",
            "<strong>Descent lemma $f(y)\\le f(x)+\\nabla f(x)^\\top(y-x)+\\tfrac L2\\|y-x\\|^2$:</strong> the ground never rises above this upward parabola. With $y=x-\\tfrac1L\\nabla f(x)$ it gives $f(x_{k+1})\\le f(x_k)-\\tfrac1{2L}\\|\\nabla f(x_k)\\|^2$.",
            "<strong>$\\|x_0-x^*\\|^2$ = how far away you start.</strong> A bigger first cliff means a bigger gap to close.",
            "<strong>Dividing by $2k$:</strong> each extra hop trims only a shrinking share of what is left, so the error falls like $1/k$ (sublinear), not geometrically."]},
    # G7 · the sufficiency proof, previously only in the hidden core text
    1103: {"breakdown": [
        "<strong>$f,g_j$ convex and $h_i$ affine:</strong> a convex valley with convex airspace.",
        "<strong>KKT then says a balanced point</strong> beats every other legal point: $f(x^*)\\le f(x)$.",
        "<strong>Proof:</strong> with $\\mu^*\\ge0$, $L(\\cdot,\\lambda^*,\\mu^*)$ is a nonnegative sum of convex functions plus affine terms, so it is convex; $\\nabla_xL(x^*)=0$ makes $x^*$ its global minimizer. For feasible $x$: $f(x)\\ge L(x,\\lambda^*,\\mu^*)\\ge L(x^*,\\lambda^*,\\mu^*)=f(x^*)$, using $h=0$, $\\mu^{*\\top}g\\le0$ and complementary slackness."]},
    # G4 · 13C3
    1303: {
        "statement": "For the hyperplane $H=\\{x:a^\\top x=b\\}$, $P_H(p)=p-\\dfrac{a^\\top p-b}{\\|a\\|^2}a$. For the halfspace $\\{x:a^\\top x\\le b\\}$, $P(p)=p-\\dfrac{\\max\\{0,a^\\top p-b\\}}{\\|a\\|^2}a$. For the affine set $\\{x:Ax=b\\}$ with $A$ of full row rank, $P(p)=p-A^\\top(AA^\\top)^{-1}(Ap-b)$.",
        "breakdown": [
            "<strong>$a^\\top p-b$ = how far past the wall the plane is,</strong> measured along the normal direction (in units of $\\|a\\|$).",
            "<strong>Dividing by $\\|a\\|^2$ and multiplying by $a$</strong> turns that signed excess into the displacement back along the normal.",
            "<strong>The half-space version has $\\max(0,\\cdot)$:</strong> if you are already on the legal side, the excess is 0 and you stay put.",
            "<strong>Several equality walls at once, $Ax=b$:</strong> $P(p)=p-A^\\top(AA^\\top)^{-1}(Ap-b)$. With one row $A=a^\\top$ this is the hyperplane formula again."]},
    # G3 · 18C3
    1802: {"breakdown": [
        "<strong>The altitude is linear,</strong> so there are no hills or valleys inside the polygon.",
        "<strong>Moving along any direction raises or lowers the altitude at a constant rate,</strong> so you can keep going until you hit a wall, then slide, until a corner.",
        "<strong>So an optimum can always be found among the finitely many basic feasible solutions.</strong>",
        "<strong>Concave objectives too:</strong> a concave function on a compact polytope attains its minimum at an extreme point, since $x=\\sum\\theta_kv_k$ gives $f(x)\\ge\\sum\\theta_kf(v_k)\\ge\\min_kf(v_k)$."]},
    # G7 · Klee-Minty, previously only in the hidden core text
    1805: {"breakdown": [
        "<strong>$x_B=B^{-1}b\\ge0,\\ x_N=0$:</strong> the current corner.",
        "<strong>Reduced cost $\\bar c_j=c_j-a_j^\\top y$, $y^\\top=c_B^\\top B^{-1}$:</strong> how the objective changes per unit of moving along each edge.",
        "<strong>If all reduced costs are $\\ge0$, no neighbouring corner is lower,</strong> so this corner is optimal.",
        "<strong>Worst case:</strong> on the Klee-Minty cube in $\\mathbb R^n$ the classic pivot rule visits all $2^n$ vertices, so simplex is exponential in the worst case though fast in practice; interior-point methods (18C7) are polynomial."]},
    # G6 · 19C1
    1901: {"breakdown": [
        "<strong>$\\max(0,g_j)^2$:</strong> no fine inside the airspace, a quadratic fine outside; squaring keeps it smooth at the wall.",
        "<strong>$\\tfrac{c_k}2h_i^2$:</strong> equality walls are fined for any deviation in either direction.",
        "<strong>As $c_k\\to\\infty$ the fine becomes so steep</strong> that the unconstrained minimiser is forced onto the boundary.",
        "<strong>Exact ($\\ell_1$) penalty:</strong> $P_1(x;c)=f(x)+c\\big(\\sum_i|h_i(x)|+\\sum_j\\max(0,g_j(x))\\big)$ is non-smooth but exact: if $x^*$ satisfies the second-order sufficient conditions with multipliers $\\lambda^*,\\mu^*$, it is a local minimizer of $P_1$ for every finite $c\\gt\\max_{i,j}\\{|\\lambda_i^*|,\\mu_j^*\\}$."]},
}
