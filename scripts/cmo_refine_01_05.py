"""CMO review, topics 01-05: fix errors, simplify the hardest explanations, split broad cards."""
import math
from subj_lib import *

def V(x0, y0, x1, y1, w=2.2, d=None):
    return L(x0, y0, x1, y1, w, d=d, ar=True)

# ------------------------------------------------------------------ fixes
FIX = {
    106: {
        "drawingCaption": "Level sets {f ≤ c} are bounded closed curves; the global minimizers are the two points ±(1, 1)",
        "coreTranslation": [
            "<strong>What:</strong> show that $f(x_1,x_2)=x_1^4+x_2^4-4x_1x_2$ has a global minimum on all of $\\mathbb{R}^2$ (not only on a closed box).",
            "<strong>How:</strong> (1) <em>Coercive:</em> since $4|x_1x_2|\\le2(x_1^2+x_2^2)$, we get $f\\ge x_1^4+x_2^4-2(x_1^2+x_2^2)\\to+\\infty$ as $\\|x\\|\\to\\infty$. (2) <em>Fence it in:</em> take the base point $(0,0)$, where $f=0$; the set $S=\\{f\\le0\\}$ is closed and bounded, so compact. (3) <em>Weierstrass</em> on $S$ gives a minimizer, and it is global because $f>0$ outside $S$.",
            "<strong>Why / where it is:</strong> setting $\\nabla f=0$ gives $x_1^3=x_2$ and $x_2^3=x_1$, so the candidates are $(0,0)$ with $f=0$ (a saddle) and $\\pm(1,1)$ with $f=-2$. The global minimum is $-2$ at $(1,1)$ <em>and</em> $(-1,-1)$ only (note $f(1,-1)=6$)."],
        "math": r"$$f(x)\ge x_1^4+x_2^4-2(x_1^2+x_2^2)\to\infty\ \Rightarrow\ \text{a global min exists;}\quad \min f=f(1,1)=f(-1,-1)=-2$$",
        "personalConnection": "Build a fence first, then search inside it: coercivity guarantees the lowest point can't be outside a big enough fence, so a search inside the fence cannot miss it.",
        "examTrap": "Solving ∇f = 0 does not prove a minimum exists, and the candidates need checking: only (1,1) and (−1,−1) are global minimizers here. (1,−1) and (−1,1) are NOT, since f = 6 there."},
    205: {
        "coreTranslation": [
            "<strong>What:</strong> at a critical point ($\\nabla f=0$) the eigenvalues of the Hessian tell you the shape: all $>0$ is a <strong>bowl</strong> (local min), all $<0$ is a <strong>hill</strong> (local max), mixed signs is a <strong>saddle</strong>.",
            "<strong>How:</strong> each eigenvalue is the curvature along its eigenvector: positive means the ground curves up in that direction, negative means it curves down.",
            "<strong>Why it matters:</strong> at a saddle there is always a way down (an eigenvector $v$ with $v^T\\nabla^2f\\,v<0$), so an algorithm that sees negative curvature can walk off the saddle instead of getting stuck."]},
    305: {
        "coreTranslation": [
            "<strong>What:</strong> the PL inequality says <em>the steeper the slope, the farther you are from the best value</em>: $\\tfrac12\\|\\nabla f(x)\\|^2\\ge\\mu\\,(f(x)-f^*)$.",
            "<strong>How:</strong> a $\\mu$-strongly convex $f$ lies above the bowl $f(x)+\\nabla f^T(y-x)+\\tfrac\\mu2\\|y-x\\|^2$. That bowl's lowest value is $f(x)-\\tfrac1{2\\mu}\\|\\nabla f(x)\\|^2$, and $f^*$ can't be lower than the bowl, so rearranging gives PL.",
            "<strong>Why it matters:</strong> PL alone (no convexity needed) makes gradient descent with step $1/L$ converge <em>linearly</em>: the gap to $f^*$ shrinks by a fixed factor $(1-\\mu/L)$ every step."],
        "math": r"$$\|\nabla f(x)\|^2\ge2\mu\,(f(x)-f^*)\ \Longrightarrow\ f(x_k)-f^*\le\Big(1-\frac{\mu}{L}\Big)^{k}\big(f(x_0)-f^*\big)$$",
        "personalConnection": "A ball on a hillside: wherever the ground is high above the lowest point, it is also steep, so the ball never gets stuck on a flat plateau far from the bottom.",
        "examTrap": "PL is weaker than strong convexity. A non-convex function such as f(x) = x² + 3 sin²x satisfies PL (every stationary point is a global min), so gradient descent still converges linearly on it."},
    401: {
        "personalConnection": "Skiing downhill: the heading of your skis d_k must point down the fall line (∇fᵀd_k < 0), and α_k is how far you glide before looking at the slope again."},
    405: {
        "coreTranslation": [
            "<strong>What:</strong> Zoutendijk's theorem: if every step satisfies the Wolfe conditions, $f$ is bounded below and $\\nabla f$ is Lipschitz, then $\\sum_k\\cos^2\\theta_k\\,\\|\\nabla f(x_k)\\|^2<\\infty$.",
            "<strong>How:</strong> $\\theta_k$ is the angle between your direction $d_k$ and steepest descent $-\\nabla f(x_k)$. A sum that stays finite forces its terms $\\cos^2\\theta_k\\|\\nabla f(x_k)\\|^2$ to go to $0$.",
            "<strong>Why it matters:</strong> if the directions never turn fully sideways ($\\cos\\theta_k\\ge\\delta>0$), then $\\|\\nabla f(x_k)\\|\\to0$: the method reaches a stationary point. This one theorem proves global convergence of steepest descent, CG and BFGS."]},
    504: {
        "coreTranslation": [
            "<strong>What:</strong> steepest descent with exact line search on a quadratic shrinks the error every step by at least the factor $\\left(\\frac{\\kappa-1}{\\kappa+1}\\right)^2$, where $\\kappa=\\lambda_{\\max}/\\lambda_{\\min}$.",
            "<strong>How:</strong> the Kantorovich inequality $\\frac{(x^Tx)^2}{(x^TQx)(x^TQ^{-1}x)}\\ge\\frac{4\\lambda_{\\max}\\lambda_{\\min}}{(\\lambda_{\\max}+\\lambda_{\\min})^2}$ limits how badly the gradient can point away from the axes of the elliptical bowl.",
            "<strong>Why it matters:</strong> $\\kappa=1$ gives $0$ (one step). $\\kappa=100$ gives $(99/101)^2\\approx0.96$ per step, so it takes about 50 steps just to halve the error. The bound is tight: a worst-case start achieves it at every step."]},
}

# ------------------------------------------------------------------ new cards from splitting 506
def _bb_svg(cid):
    return svg(cid, AX(24, 124, 224, 14),
               poly([(30 + t * 6, 118 - (2.2 * t + 0.03 * t * t)) for t in range(0, 33)], 2.2),
               C(90, 93, 3.5), C(162, 55, 3.5),
               L(60, 109, 200, 35, 1.4, d="5 3"),
               N(86, 108, "x_{k−1}", 8.5, "end"), N(166, 70, "x_k", 8.5, "start"),
               N(30, 16, "gradient g along the path", 8.5, "start"),
               N(120, 138, "secant slope ≈ curvature h  ⇒  step α = 1/h", 8.5, "middle", "bold"),
               N(222, 100, "BB1: α = sᵀs / sᵀy", 8.5, "end"), N(222, 112, "no line search", 8.5, "end", "bold"))

def _hb_svg(cid):
    return svg(cid, E(120, 72, 100, 34, 0, "none", 1.3), E(120, 72, 66, 22, 0, "none", 1.3), E(120, 72, 32, 11, 0, "none", 1.3),
               poly([(26, 38), (48, 103), (74, 44), (94, 94), (108, 56), (114, 80), (120, 72)], 1.5, "4 3"),
               P("M26 38 Q60 118 120 72", w=2.6, ar=True), C(120, 72, 3.2),
               N(60, 24, "plain GD zig-zags (dashed)", 8.5, "start"), N(152, 126, "momentum glides (solid)", 8.5, "start", "bold"),
               N(120, 142, "x_{k+1} = x_k − α∇f + β (x_k − x_{k−1})", 8.5, "middle", "bold"))

NEW = [
    (506, {
        "id": 507, "title": "Heavy-Ball Momentum & Nesterov",
        "category": "ACCELERATED METHODS",
        "drawingSvg": _hb_svg(507),
        "drawingCaption": "Momentum carries you down the valley floor instead of bouncing between its walls",
        "coreTranslation": [
            "<strong>What:</strong> add a fraction $\\beta$ of the previous step to the gradient step: $x_{k+1}=x_k-\\alpha\\nabla f(x_k)+\\beta\\,(x_k-x_{k-1})$.",
            "<strong>How:</strong> the wall-to-wall bounces cancel out because they flip sign every step, while the steady motion along the valley adds up. It is a heavy ball rolling with inertia.",
            "<strong>Why it matters:</strong> with the best $\\alpha,\\beta$ on a quadratic, the rate improves from $\\frac{\\kappa-1}{\\kappa+1}$ to $\\frac{\\sqrt\\kappa-1}{\\sqrt\\kappa+1}$. For $\\kappa=100$ that is $0.98\\to0.82$ per step, about <strong>10× fewer iterations</strong>."],
        "math": r"$$x_{k+1}=x_k-\alpha\nabla f(x_k)+\beta(x_k-x_{k-1}),\qquad \text{rate}\ \ \frac{\sqrt\kappa-1}{\sqrt\kappa+1}\ \text{ vs }\ \frac{\kappa-1}{\kappa+1}$$",
        "personalConnection": "A heavy bowling ball rolling down a washboard road: its inertia lets it ignore the small bumps and keep rolling along the road instead of rattling into the side ditches.",
        "examTrap": "Heavy ball's speed-up is proven for quadratics. For general convex functions use Nesterov's version, which takes the gradient at the look-ahead point $x_k+\\beta(x_k-x_{k-1})$ and has the optimal $O(1/k^2)$ guarantee."}),
]

# 506 itself becomes "Barzilai-Borwein step sizes"
FIX[506] = {
    "title": "Barzilai–Borwein Step Sizes (No Line Search)",
    "category": "STEP-SIZE RULES",
    "drawingSvg": _bb_svg(506),
    "drawingCaption": "Fit a secant to the last two gradients; its slope estimates the curvature, and the step is 1/slope",
    "coreTranslation": [
        "<strong>What:</strong> choose the step size from the last two iterates instead of running a line search.",
        "<strong>How:</strong> let $s=x_k-x_{k-1}$ and $y=g_k-g_{k-1}$. Pretend the Hessian is $\\approx hI$ and fit the secant $hs\\approx y$; then the step is $\\alpha=1/h$, giving $\\alpha^{BB1}=\\frac{s^Ts}{s^Ty}$ (long step) or $\\alpha^{BB2}=\\frac{s^Ty}{y^Ty}$ (short step).",
        "<strong>Why it matters:</strong> BB steps are cheap (no function evaluations) and converge dramatically faster than fixed steps on ill-conditioned problems. The price: the objective is <em>not</em> decreased at every step."],
    "math": r"$$\alpha_k^{BB1}=\frac{s_{k}^{T}s_{k}}{s_{k}^{T}y_{k}},\qquad \alpha_k^{BB2}=\frac{s_{k}^{T}y_{k}}{y_{k}^{T}y_{k}},\qquad s_k=x_k-x_{k-1},\ \ y_k=g_k-g_{k-1}$$",
    "personalConnection": "Judging how steep a path is by comparing your two last footprints with how much the slope changed between them, and sizing your next stride to match.",
    "examTrap": "BB iterations are non-monotone: f can go up for a few steps and that is expected. Forcing a strict descent line search on top destroys the speed-up. Also check sᵀy > 0 before dividing."
}
