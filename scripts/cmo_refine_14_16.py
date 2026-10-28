"""CMO review, topics 14-16: simplify, redraw weak diagrams, split the SVM card."""
import math
from subj_lib import *


def V(x0, y0, x1, y1, w=2.2, d=None):
    return L(x0, y0, x1, y1, w, d=d, ar=True)


# ---------------------------------------------------------------- diagrams
def _drop(cid):
    return svg(cid,
               PG("10,70 110,70 110,130 10,130", "#ffffff", 0), PG("10,12 110,12 110,70 10,70", "#f1f5f9", 0), L(10, 70, 110, 70, 3.2),
               N(60, 24, "feasible side", 8.5, "middle"), C(60, 70, 4), V(60, 70, 60, 34, 2.6), N(66, 40, "−∇f", 8.5, "start", "bold"),
               N(60, 92, "λ < 0", 11, "middle", "bold"), N(60, 106, "−∇f points INTO", 8.5, "middle"), N(60, 118, "the feasible side", 8.5, "middle"), N(60, 140, "drop the wall ✓", 8.5, "middle", "bold"),
               L(120, 8, 120, 142, 1, d="4 3"),
               PG("130,70 230,70 230,130 130,130", "#ffffff", 0), PG("130,12 230,12 230,70 130,70", "#f1f5f9", 0), L(130, 70, 230, 70, 3.2),
               C(180, 70, 4), V(180, 70, 180, 106, 2.6), N(186, 108, "−∇f", 8.5, "start", "bold"),
               N(180, 40, "λ > 0", 11, "middle", "bold"), N(180, 54, "−∇f pushes INTO the wall", 8.5, "middle"), N(180, 140, "keep the wall (optimal)", 8.5, "middle", "bold"))


def _term(cid):
    steps = [(30, 30), (70, 60), (110, 88), (150, 100), (190, 106)]
    parts = [AX(20, 122, 226, 14)]
    for k, (x, y) in enumerate(steps):
        parts.append(C(x, y, 3.2))
        if k:
            parts.append(L(steps[k - 1][0], steps[k - 1][1], x, y, 1.8))
    parts += [N(52, 26, "W₁", 9, "middle", "bold"), N(92, 56, "W₂", 9, "middle", "bold"), N(132, 82, "W₃", 9, "middle", "bold"), N(190, 94, "W* (optimal)", 8.5, "middle", "bold"),
              N(30, 16, "f(x_k)", 8.5, "start"), N(120, 136, "iteration k:  f strictly decreases at every real step", 8.5, "middle", "bold"),
              N(224, 38, "no working set", 8.5, "end"), N(224, 50, "ever repeats", 8.5, "end", "bold")]
    return svg(cid, *parts)


def _svm_margin(cid):
    return svg(cid,
               L(20, 110, 200, 22, 2.8), L(34, 128, 214, 40, 1.4, d="5 3"), L(6, 92, 186, 4, 1.4, d="5 3"),
               C(52, 52, 4.2), C(84, 40, 4.2), C(110, 52, 4.2), C(30, 74, 4.2), C(60, 62, 4.2),
               R(150, 96, 8, 8, "#ffffff", 1.6), R(176, 78, 8, 8, "#ffffff", 1.6), R(196, 100, 8, 8, "#ffffff", 1.6), R(158, 112, 8, 8, "#ffffff", 1.6),
               V(110, 64, 128, 90, 2.4), N(132, 98, "w", 10, "start", "bold"),
               N(218, 24, "wᵀx + b = +1", 8, "end"), N(228, 130, "wᵀx + b = −1", 8, "end"), N(210, 62, "wᵀx + b = 0", 8, "end", "bold"),
               N(120, 144, "margin width = 2/‖w‖  →  maximize margin = minimize ½‖w‖²", 8.5, "middle", "bold"))


def _svm_dual(cid):
    return svg(cid,
               L(20, 110, 200, 22, 2.8), L(34, 128, 214, 40, 1.2, d="5 3"), L(6, 92, 186, 4, 1.2, d="5 3"),
               C(40, 48, 3.2), C(70, 30, 3.2), C(30, 74, 3.2), C(100, 30, 3.2), C(84, 46, 5, "#ffffff", 2.2), C(60, 64, 5, "#ffffff", 2.2),
               R(160, 108, 8, 8, "#ffffff", 1.2), R(204, 100, 8, 8, "#ffffff", 1.2), R(188, 118, 8, 8, "#ffffff", 1.2), R(150, 100, 10, 10, "#d9dee7", 2.2), R(176, 82, 10, 10, "#d9dee7", 2.2),
               N(84, 38, "α>0", 8.5, "middle", "bold"), N(56, 80, "α>0", 8.5, "middle", "bold"), N(150, 92, "α>0", 8.5, "middle", "bold"),
               N(30, 90, "α = 0", 8, "end"), N(230, 112, "α = 0", 8, "end"),
               N(120, 144, "only the points ON the margin (support vectors) shape w", 8.5, "middle", "bold"))


# ---------------------------------------------------------------- fixes
FIX = {
    1401: {
        "coreTranslation": [
            "<strong>What:</strong> projected gradient minimizes $f$ over a closed convex set $\\Omega$ by taking an ordinary gradient step and then snapping back onto $\\Omega$: $x_{k+1}=\\Pi_\\Omega\\big(x_k-\\alpha_k\\nabla f(x_k)\\big)$.",
            "<strong>How:</strong> equivalently, $x_{k+1}$ minimizes the local model $\\nabla f(x_k)^T(y-x_k)+\\tfrac1{2\\alpha_k}\\|y-x_k\\|^2$ over $y\\in\\Omega$. When $\\Omega$ is simple (a box, a ball) the projection is a cheap formula.",
            "<strong>Why it matters:</strong> it is as easy as gradient descent but never leaves the feasible set. On curved constraint surfaces Luenberger splits it into a tangent step followed by a restoration step back onto the surface."]},
    1402: {
        "coreTranslation": [
            "<strong>What:</strong> $x^*$ is a stationary point of $\\min_{x\\in\\Omega}f$ exactly when a gradient step followed by projection leaves it where it is: $x^*=\\Pi_\\Omega\\big(x^*-\\alpha\\nabla f(x^*)\\big)$ (for any $\\alpha>0$).",
            "<strong>How:</strong> define the gradient mapping $G_\\alpha(x)=\\frac1\\alpha\\big(x-\\Pi_\\Omega(x-\\alpha\\nabla f(x))\\big)$. Then $x^*$ is stationary iff $G_\\alpha(x^*)=0$, iff $-\\nabla f(x^*)$ points into the normal cone of $\\Omega$ at $x^*$.",
            "<strong>Why it matters:</strong> $\\|G_\\alpha(x_k)\\|\\le\\epsilon$ is the correct stopping test for constrained problems, because $\\nabla f$ itself does not vanish on the boundary."]},
    1404: {
        "coreTranslation": [
            "<strong>What:</strong> a straight ray $x_k-\\alpha\\nabla f(x_k)$ leaves $\\Omega$, so the line search must follow the bent path $x(\\alpha)=\\Pi_\\Omega\\big(x_k-\\alpha\\nabla f(x_k)\\big)$, the <em>projection arc</em>.",
            "<strong>How:</strong> backtrack $\\alpha=s,\\beta s,\\beta^2s,\\dots$ until the Armijo test along the arc holds: $f(x(\\alpha))\\le f(x_k)-\\tfrac\\sigma\\alpha\\|x_k-x(\\alpha)\\|^2$.",
            "<strong>Why it matters:</strong> the test measures progress with the displacement actually taken, $x_k-x(\\alpha)$, not with $-\\alpha\\nabla f$. The arc can bend along several faces of $\\Omega$, so many bound constraints can become active in one iteration."]},
    1405: {
        "coreTranslation": [
            "<strong>What:</strong> on a curved constraint surface $h(x)=0$ a step along the tangent plane lands slightly off the surface, so each iteration is a <em>tangent step</em> followed by a <em>restoration step</em>.",
            "<strong>How:</strong> (1) tangent step $y=x_k-\\alpha P_k\\nabla f(x_k)$ with $P_k$ the projector onto the tangent plane; (2) restoration: Newton-correct $y$ back to feasibility along the normal: $x_{k+1}=y-\\nabla h\\,[\\nabla h^T\\nabla h]^{-1}h(y)$.",
            "<strong>Why it matters:</strong> this is how gradient projection extends from simple sets to nonlinear equality constraints. If $\\alpha$ is too large, $y$ is too far from the surface and restoration may fail or land on a different branch."]},
    1406: {
        "coreTranslation": [
            "<strong>Problem:</strong> minimize $f=\\tfrac12x_1^2+x_2^2-2x_1+3x_2$ over $x_1,x_2\\ge0$, starting at $x_0=(1,1)$ with step $\\alpha=1$. Gradient: $\\nabla f=(x_1-2,\\ 2x_2+3)$, so $\\nabla f(x_0)=(-1,5)$.",
            "<strong>One iteration:</strong> unconstrained step $y=x_0-\\nabla f=(2,\\,-4)$; project onto $\\mathbb{R}^2_+$ by clipping negatives: $x_1=(2,\\,0)$. The second coordinate hit its wall in a single step.",
            "<strong>Check optimality:</strong> at $(2,0)$, $\\nabla f=(0,3)$. A step gives $y=(2,-3)$, which projects back to $(2,0)$: a <strong>fixed point</strong>, so $(2,0)$ is optimal ($x_2$ would like to go negative but the wall stops it)."],
        "math": r"$$x_1=\max\!\Big(0,\ \begin{bmatrix}1\\1\end{bmatrix}-\begin{bmatrix}-1\\5\end{bmatrix}\Big)=\begin{bmatrix}2\\0\end{bmatrix},\qquad \max\!\Big(0,\begin{bmatrix}2\\0\end{bmatrix}-\begin{bmatrix}0\\3\end{bmatrix}\Big)=\begin{bmatrix}2\\0\end{bmatrix}\ \ (\text{fixed point})$$"},
    1502: {
        "coreTranslation": [
            "<strong>What:</strong> the equality subproblem proposes a full step $p_k$; if $x_k+p_k$ breaks an inactive constraint, you can only go part of the way and must stop at the wall you hit.",
            "<strong>How:</strong> only constraints with $a_i^Tp_k<0$ (moving toward the forbidden side) can block. The allowed fraction is $\\alpha_k=\\min\\big(1,\\ \\min_{i\\notin\\mathcal{W}_k,\\ a_i^Tp_k<0}\\frac{b_i-a_i^Tx_k}{a_i^Tp_k}\\big)$.",
            "<strong>Why it matters:</strong> the constraint that attains the minimum is the <em>blocking constraint</em>: set $x_{k+1}=x_k+\\alpha_kp_k$ and add it to the working set."]},
    1503: {
        "drawingSvg": _drop(1503),
        "drawingCaption": "Sign of the multiplier tells you whether the wall is helping (λ > 0) or just in the way (λ < 0)",
        "coreTranslation": [
            "<strong>What:</strong> when the equality subproblem gives $p_k=0$ you are at the minimum on the current working surface. Now ask: is leaving that surface worthwhile?",
            "<strong>How:</strong> compute the multipliers $\\lambda_i$ of the working constraints. If all $\\lambda_i\\ge0$, the KKT conditions hold and you are done. If some $\\lambda_j<0$, then $-\\nabla f$ points <em>into</em> the feasible side of wall $j$, so dropping it lets you decrease $f$.",
            "<strong>Why it matters:</strong> drop the constraint with the most negative multiplier. Drop only when $p_k=0$; dropping while $p_k\\ne0$ can cause cycling."]},
    1504: {
        "drawingSvg": _term(1504),
        "drawingCaption": "Each real step lowers f, so the algorithm can never return to an earlier working set and must finish",
        "coreTranslation": [
            "<strong>What:</strong> for a strictly convex QP ($Q\\succ0$) with no degeneracy (every step length $\\alpha_k>0$), the active-set method reaches the exact optimum in a finite number of iterations.",
            "<strong>How:</strong> there are at most $2^m$ possible working sets, and each real step (a full step or a move after dropping a constraint) strictly lowers $f$. So no working set can ever be visited twice.",
            "<strong>Why it matters:</strong> it is an <em>exact</em> method: no tolerance, no infinite convergence. The one danger is degeneracy, where a zero-length step leaves $f$ unchanged."]},
    1506: {
        "coreTranslation": [
            "<strong>Problem:</strong> minimize $(x_1-3)^2+(x_2-3)^2$ on the box $0\\le x_1,x_2\\le2$. The unconstrained minimum $(3,3)$ is outside, so expect the answer at the corner nearest to it, $(2,2)$.",
            "<strong>Step 1:</strong> start at $x_0=(0,0)$ with $\\mathcal{W}=\\{x_1=0,\\ x_2=0\\}$; both multipliers are $-6<0$, so drop $x_1=0$. Move along the bottom edge toward $x_1=3$; the wall $x_1\\le2$ blocks at $\\alpha=\\tfrac23$, giving $(2,0)$. <strong>Step 2:</strong> at $(2,0)$ the multiplier of $x_2=0$ is $-6<0$, so drop it and move up the right edge; the wall $x_2\\le2$ blocks at $(2,2)$.",
            "<strong>Step 3:</strong> at $(2,2)$ the working constraints are $x_1=2,\\ x_2=2$ and both multipliers equal $2>0$. All multipliers non-negative means KKT holds, so $x^*=(2,2)$ is optimal."],
        "personalConnection": "Walking toward a beacon outside a square room: you slide along a wall until another wall stops you, then slide along that wall, and finish in the corner nearest the beacon.",
        "examTrap": "Drop a constraint only after checking its multiplier is negative, and then check that the new direction really moves INTO the freed side (aⱼᵀp > 0). Otherwise you re-enter the forbidden region."},
    1601: {
        "coreTranslation": [
            "<strong>What:</strong> the primal function $\\omega(z)=\\inf\\{f(x):g(x)\\le z\\}$ is a 'price list': it is the best cost you can get if the constraint is relaxed to $g(x)\\le z$. The real problem's answer is $\\omega(0)=f^*$.",
            "<strong>How:</strong> take a hyperplane with normal $(\\mu,1)$ lying below the graph of $\\omega$. Its height at $z=0$ is $\\phi(\\mu)=\\inf_x\\{f(x)+\\mu^Tg(x)\\}$, the <em>dual function</em>.",
            "<strong>Why it matters:</strong> maximizing the dual means lifting that supporting hyperplane as high as possible. If $\\omega$ is convex, the highest one touches $\\omega$ at $z=0$, so the gap vanishes (strong duality)."]},
    1602: {
        "coreTranslation": [
            "<strong>What:</strong> for <em>any</em> problem, convex or not, the dual optimum never exceeds the primal optimum: $d^*\\le p^*$. The difference $p^*-d^*\\ge0$ is the <em>duality gap</em>.",
            "<strong>How:</strong> for any feasible $x$ and any $\\mu\\ge0$: $q(\\lambda,\\mu)=\\inf_{\\tilde x}\\mathcal{L}\\le\\mathcal{L}(x,\\lambda,\\mu)=f(x)+\\lambda^Th+\\mu^Tg\\le f(x)$, because $h=0$ and $\\mu^Tg\\le0$. Take sup on the left and inf on the right.",
            "<strong>Why it matters:</strong> every dual feasible point gives a certified lower bound on the best cost. It needs no assumption at all; closing the gap (strong duality) is what needs convexity and Slater."]},
    1605: {
        "coreTranslation": [
            "<strong>What:</strong> the multiplier $\\mu_j^*$ is the <em>price</em> of constraint $j$: the rate at which the optimal cost drops when you relax the constraint to $g_j(x)\\le z_j$.",
            "<strong>How:</strong> if strong duality holds, $p^*(z)\\ge p^*(0)-\\mu^{*T}z$, so $\\mu^*$ is a (negative) slope of the optimal-value curve at $z=0$: $\\partial p^*/\\partial z_j=-\\mu_j^*$ (and $-\\lambda_i^*$ for equalities).",
            "<strong>Why it matters:</strong> a multiplier of 50 means an extra unit of that resource saves about 50 in cost, and $\\mu_j^*=0$ means that constraint isn't limiting you at all."]},
    1606: {
        "title": "SVM: Margin, Primal Problem and Lagrangian",
        "drawingSvg": _svm_margin(1606),
        "drawingCaption": "The widest street between the two classes has width 2/‖w‖, so maximizing the margin means minimizing ‖w‖",
        "coreTranslation": [
            "<strong>What:</strong> a support vector machine separates two classes ($y_i=\\pm1$) with the line $w^Tx+b=0$ so that the empty 'street' around it is as wide as possible.",
            "<strong>How:</strong> require every point to be outside the street, $y_i(w^Tx_i+b)\\ge1$. The street's width is $2/\\|w\\|$, so the widest street comes from the convex QP $\\min_{w,b}\\tfrac12\\|w\\|^2$ subject to those $N$ inequalities.",
            "<strong>Why it matters:</strong> one multiplier $\\alpha_i\\ge0$ per point gives the Lagrangian $\\mathcal{L}=\\tfrac12\\|w\\|^2-\\sum_i\\alpha_i\\big[y_i(w^Tx_i+b)-1\\big]$. Stationarity in $w$ and $b$ then gives $w=\\sum\\alpha_iy_ix_i$ and $\\sum\\alpha_iy_i=0$ (next card)."],
        "math": r"$$\min_{w,b}\ \tfrac12\|w\|^2\ \ \text{s.t.}\ \ y_i(w^Tx_i+b)\ge1,\qquad \text{margin}=\frac{2}{\|w\|}$$",
        "personalConnection": "Building the widest possible road between two towns: the road must not touch any house, so the houses closest to the road decide how wide it can be.",
        "examTrap": "The constraints are y_i(wᵀx_i + b) ≥ 1, not ≥ 0. The 1 sets the scale of w and is what makes the margin exactly 2/‖w‖."},
    1701: {
        "coreTranslation": [
            "<strong>What:</strong> the Wolfe dual of a convex differentiable problem $\\min f$ s.t. $g\\le0$, $h=0$ is $\\max_{x,\\lambda,\\mu}\\mathcal{L}(x,\\lambda,\\mu)$ subject to $\\nabla_x\\mathcal{L}=0$ and $\\mu\\ge0$.",
            "<strong>How:</strong> in ordinary Lagrange duality the dual function is $\\inf_x\\mathcal{L}$, which needs the minimizing $x$ in closed form. For a convex $\\mathcal{L}$ that infimum sits exactly where $\\nabla_x\\mathcal{L}=0$, so Wolfe just imposes that equation as a constraint and treats $x$ as a variable.",
            "<strong>Why it matters:</strong> you never have to eliminate $x$ by hand. Note that $x$ in the Wolfe dual need not be primal feasible; only $\\nabla_x\\mathcal{L}=0$ and $\\mu\\ge0$ are required."]},
    1703: {
        "personalConnection": "Two sides of one trade: the primal minimizes a risk x^T Q x / 2, the dual hedges it with resources b and pays the same risk with the opposite sign. Their totals meet at the optimum.",
        "examTrap": "The dual objective is −½ xᵀQx + bᵀy (note the MINUS). It comes from ½xᵀQx − xᵀQx = −½xᵀQx after using stationarity xᵀ(Qx + c − Aᵀy − v) = 0."},
}

NEW = [
    (1606, {
        "id": 1608, "title": "SVM Dual: Support Vectors and the Kernel Trick",
        "category": "DUALITY IN PRACTICE",
        "drawingSvg": _svm_dual(1608),
        "drawingCaption": "Only points that touch the margin have α > 0; every other point has α = 0 and could be deleted",
        "coreTranslation": [
            "<strong>What:</strong> substituting $w=\\sum\\alpha_iy_ix_i$ back into the Lagrangian gives the SVM dual: $\\max_\\alpha\\ \\sum_i\\alpha_i-\\tfrac12\\sum_{i,j}\\alpha_i\\alpha_jy_iy_j\\,x_i^Tx_j$ subject to $\\alpha_i\\ge0$, $\\sum\\alpha_iy_i=0$.",
            "<strong>How:</strong> complementary slackness $\\alpha_i[y_i(w^Tx_i+b)-1]=0$ says $\\alpha_i>0$ only for points exactly on the margin. These <em>support vectors</em> alone determine $w$; deleting any other point changes nothing.",
            "<strong>Why it matters:</strong> the data enter only through inner products $x_i^Tx_j$, so you may replace them by a kernel $K(x_i,x_j)$ and get a curved boundary at no extra cost (<em>kernel trick</em>). <strong>Check on two points:</strong> $x_1=(1,1),y_1=+1$ and $x_2=(-1,-1),y_2=-1$ give $\\alpha_1=\\alpha_2=\\tfrac14$, $w=(\\tfrac12,\\tfrac12)$, and dual value $\\tfrac14=\\tfrac12\\|w\\|^2$ (no gap)."],
        "math": r"$$\max_{\alpha\ge0,\ \sum\alpha_iy_i=0}\ \sum_i\alpha_i-\tfrac12\sum_{i,j}\alpha_i\alpha_jy_iy_j\,x_i^Tx_j,\qquad w^*=\sum_i\alpha_i^*y_ix_i,\ \ \alpha_i^*>0\Rightarrow\text{support vector}$$",
        "personalConnection": "A bridge held up by a few cables: only the cables that carry load (support vectors) have tension; the rest of the landscape beneath carries none and can be removed without the bridge noticing.",
        "examTrap": "α_i > 0 means the point is exactly ON the margin, but a point on the margin can still have α_i = 0 (a degenerate case). 'Support vector ⇒ α > 0' is the safe direction; 'on the margin ⇒ α > 0' is not."}),
]
