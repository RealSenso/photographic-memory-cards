"""CMO review, topics 06-09: fix wrong numbers, simplify, replace formula-box diagrams with pictures."""
import math
from subj_lib import *


def V(x0, y0, x1, y1, w=2.2, d=None):
    return L(x0, y0, x1, y1, w, d=d, ar=True)


# ---------------------------------------------------------------- diagrams
def _cg_finite(cid):
    cg = [(34 + 30 * k, 118 - e) for k, e in enumerate([88, 52, 20, 0, 0, 0, 0])]
    sd = [(34 + 30 * k, 118 - 88 * (0.68 ** k)) for k in range(7)]
    return svg(cid, AX(24, 120, 226, 14), poly(sd, 1.6, "5 3"), poly(cg, 2.4),
               *[C(x, y, 3) for x, y in cg[:4]],
               N(34 + 90, 106, "m = 3", 9, "middle", "bold"), L(124, 118, 124, 62, 1, d="3 3"),
               N(130, 50, "CG: exact after m steps", 8.5, "start", "bold"), N(130, 62, "(m distinct eigenvalues)", 8.5, "start"),
               N(150, 92, "steepest descent", 8.5, "start"), N(150, 104, "never quite arrives", 8.5, "start"),
               N(30, 16, "error", 8.5, "start"), N(120, 136, "iteration k", 8.5))


def _ncg(cid):
    return svg(cid,
               N(60, 14, "typical step", 9, "middle", "bold"), C(30, 80, 3),
               V(30, 80, 100, 80, 2, "4 3"), N(100, 72, "d_k", 8.5, "start"),
               V(30, 80, 62, 118, 2.2), N(66, 126, "−g_{k+1}", 8.5, "start"),
               V(30, 80, 96, 104, 2.6), N(100, 108, "d_{k+1} = −g_{k+1} + β d_k", 8, "start", "bold"),
               L(120, 8, 120, 138, 1, d="3 3"),
               N(180, 14, "progress stalls", 9, "middle", "bold"), C(150, 80, 3),
               V(150, 80, 166, 118, 2.6), N(170, 124, "d_{k+1} ≈ −g_{k+1}", 8, "start", "bold"),
               N(150, 44, "g_{k+1} ≈ g_k ⇒ β_PR ≈ 0", 8.5, "start"), N(150, 58, "automatic restart", 8.5, "start", "bold"),
               N(120, 144, "", 8))


def _cg_worked(cid):
    s = 14.0
    px = lambda x, y: (120 + s * x, 72 - s * y)
    return svg(cid,
               E(120, 72, math.sqrt(20) * s, math.sqrt(5) * s, 0, "none", 1.2), E(120, 72, math.sqrt(8) * s, math.sqrt(2) * s, 0, "none", 1.2),
               E(120, 72, math.sqrt(2) * s, math.sqrt(0.5) * s, 0, "none", 1.2),
               poly([px(4, 1), px(2.4, -0.6), px(0, 0)], 2.4), C(*px(4, 1), 3.5), C(*px(2.4, -0.6), 3.5), C(*px(0, 0), 3.5, "#ffffff"),
               N(px(4, 1)[0], px(4, 1)[1] - 8, "x₀=(4,1)", 8.5, "middle", "bold"), N(px(2.4, -0.6)[0] + 4, px(2.4, -0.6)[1] + 14, "x₁=(2.4,−0.6)", 8.5, "start"),
               N(110, 92, "x₂ = (0,0) = x*", 8.5, "end", "bold"),
               N(120, 140, "two exact line searches, conjugate directions: done in n = 2 steps", 8.5, "middle", "bold"))


def _sr1(cid):
    return svg(cid, C(60, 72, 28, "#ffffff", 1.8), N(60, 120, "B_k", 9, "middle", "bold"),
               L(100, 72, 130, 72, 1.5, ar=True), N(115, 64, "+ u uᵀ/c", 8.5, "middle", "bold"),
               E(180, 72, 52, 28, -30, "#f1f5f9", 1.8), V(180, 72, 214, 50, 2.4), N(216, 46, "u", 10, "start", "bold"),
               N(180, 120, "B_{k+1}", 9, "middle", "bold"),
               N(120, 14, "rank 1: changes the model along ONE direction u only", 8.5, "middle", "bold"),
               N(120, 138, "chosen so that  B_{k+1} s = y", 8.5, "middle"))


def _dfp(cid):
    return svg(cid, C(60, 72, 28, "#ffffff", 1.8), N(60, 120, "H_k", 9, "middle", "bold"),
               L(100, 72, 130, 72, 1.5, ar=True), N(115, 64, "rank 2", 8.5, "middle", "bold"),
               E(180, 72, 54, 24, -15, "#f1f5f9", 1.8), V(180, 72, 228, 62, 2.4), N(206, 52, "s: add", 8.5, "start", "bold"),
               V(180, 72, 160, 100, 2.0), N(156, 112, "H y: remove", 8.5, "end", "bold"),
               N(180, 128, "H_{k+1}", 9, "middle", "bold"),
               N(120, 14, "+ s sᵀ/(sᵀy)   − H y yᵀ H /(yᵀ H y)", 8.5, "middle", "bold"))


def _bfgs(cid):
    return svg(cid, V(30, 110, 70, 50, 2.6), N(74, 46, "y = g_{k+1} − g_k", 8.5, "start", "bold"),
               L(104, 80, 134, 80, 1.6, ar=True), N(119, 70, "H_{k+1}", 9, "middle", "bold"),
               V(150, 110, 220, 90, 2.6), N(222, 86, "s = x_{k+1} − x_k", 8.5, "end", "bold"),
               N(120, 20, "BFGS builds H_{k+1} so that it MAPS y TO s", 9, "middle", "bold"),
               N(120, 134, "H_{k+1} y = s  (the secant equation)", 8.5, "middle"),
               N(120, 146, "", 8))


# ---------------------------------------------------------------- fixes
FIX = {
    601: {
        "coreTranslation": [
            "<strong>What:</strong> Newton's method replaces $f$ near $x_k$ by its best-fitting parabola (the second-order Taylor model) and jumps straight to the bottom of that parabola.",
            "<strong>How:</strong> the model is $q(p)=f(x_k)+\\nabla f(x_k)^Tp+\\tfrac12p^T\\nabla^2f(x_k)\\,p$. Setting $\\nabla q=0$ gives the linear system $\\nabla^2f(x_k)\\,p_k=-\\nabla f(x_k)$, and then $x_{k+1}=x_k+p_k$.",
            "<strong>Why it matters:</strong> on a quadratic it lands on the exact minimum in one step, and near a minimum it converges extremely fast. It is also <em>affine invariant</em>: rescaling the coordinates does not change its path, unlike gradient descent."]},
    602: {
        "coreTranslation": [
            "<strong>What:</strong> near a strict local minimum, Newton's error is <em>squared</em> at every step: $\\|x_{k+1}-x^*\\|\\le\\frac{L}{2m}\\|x_k-x^*\\|^2$.",
            "<strong>How:</strong> it needs three things: $\\nabla^2f(x^*)\\succeq mI$ with $m>0$, a Hessian that is $L$-Lipschitz near $x^*$, and a start close enough that $\\frac{L}{2m}\\|x_0-x^*\\|<1$.",
            "<strong>Why it matters:</strong> squaring the error doubles the number of correct digits each step: $10^{-1}\\to10^{-2}\\to10^{-4}\\to10^{-8}$. It is called <em>quadratic</em> convergence, and it is faster than superlinear."]},
    603: {
        "coreTranslation": [
            "<strong>What:</strong> Newton's step is only guaranteed to go downhill when the Hessian is positive definite.",
            "<strong>How:</strong> $p=-H^{-1}g$ has slope $g^Tp=-g^TH^{-1}g$. If $H$ has a negative eigenvalue this number can be <em>positive</em> (the step goes uphill). If $H$ is singular there is no step at all. And near a saddle or a maximum Newton happily converges to it, because it only looks for $\\nabla f=0$.",
            "<strong>Why it matters:</strong> pure Newton needs safeguards: a line search (damped Newton) and a fix for the Hessian (add $\\tau I$), covered in the next two cards."],
        "examTrap": "Pure Newton on f(x) = x³ − 3x started at x₀ = −0.5 runs UPHILL: x goes −0.5 → −1.25 → −1.025 → −1 and f rises 1.375 → 1.80 → 2.00, converging to the local MAXIMUM at x = −1 (where f″ = −6 < 0)."},
    604: {
        "coreTranslation": [
            "<strong>What:</strong> damped Newton takes a shortened step $x_{k+1}=x_k+\\alpha_kp_k$, with $p_k$ the Newton direction and $\\alpha_k\\in(0,1]$ chosen by backtracking.",
            "<strong>How:</strong> start at $\\alpha=1$ and shrink ($\\alpha\\leftarrow\\tfrac12\\alpha$) until the Armijo test $f(x_k+\\alpha p_k)\\le f(x_k)+c_1\\alpha\\nabla f(x_k)^Tp_k$ holds.",
            "<strong>Why it matters:</strong> far from the solution the shrinking guarantees descent; near the solution the full step $\\alpha=1$ is always accepted (if $c_1<\\tfrac12$), so the method <em>automatically</em> switches back to fast quadratic convergence."]},
    605: {
        "personalConnection": "Building on soft ground: where the soil is firm (H positive definite) you use the natural shape of the ground (Newton); where it is soft or uneven you drive extra pilings (τI) until the foundation is firm."},
    606: {
        "drawingCaption": "Gradient descent zig-zags across the narrow valley; Newton rescales the valley into a bowl and jumps along it",
        "coreTranslation": [
            "<strong>What:</strong> compare gradient descent (GD) and Newton on Rosenbrock $f=100(x_2-x_1^2)^2+(1-x_1)^2$, starting at the origin.",
            "<strong>GD:</strong> there $\\nabla^2f=\\mathrm{diag}(2,200)$, so $\\kappa=100$ and each step only shrinks the error by about $\\left(\\tfrac{99}{101}\\right)^2\\approx0.96$. It zig-zags across the valley and needs hundreds of steps.",
            "<strong>Newton:</strong> $\\nabla f(0,0)=(-2,0)$ and $H^{-1}=\\mathrm{diag}(\\tfrac12,\\tfrac1{200})$, so $p=-H^{-1}g=(1,0)$: one step to $(1,0)$. Dividing by the Hessian rescales the squeezed valley into a round bowl, and a few more steps land on $(1,1)$."],
        "math": r"$$\nabla f(0,0)=\begin{bmatrix}-2\\0\end{bmatrix},\ \ H=\begin{bmatrix}2&0\\0&200\end{bmatrix}\ \Rightarrow\ p_N=-H^{-1}g=\begin{bmatrix}1\\0\end{bmatrix},\qquad \kappa=100$$"},
    704: {"drawingSvg": _cg_finite(704),
          "drawingCaption": "With only m = 3 distinct eigenvalues, CG's error hits exactly zero after 3 steps"},
    705: {"drawingSvg": _ncg(705),
          "drawingCaption": "When progress stalls, β_PR ≈ 0, so the next direction is simply steepest descent: an automatic restart"},
    706: {
        "drawingSvg": _cg_worked(706),
        "drawingCaption": "Conjugate Gradient reaches the exact minimum of a 2-D quadratic in exactly 2 steps",
        "coreTranslation": [
            "<strong>Problem:</strong> minimize $f=x_1^2+4x_2^2$ (so $Q=\\mathrm{diag}(2,8)$) from $x_0=(4,1)$. First step is steepest descent: $g_0=(8,8)$, $d_0=-g_0$.",
            "<strong>Step 1:</strong> $\\alpha_0=\\frac{g_0^Tg_0}{d_0^TQd_0}=\\frac{128}{640}=\\frac15$, so $x_1=(2.4,\\,-0.6)$ and $g_1=(4.8,-4.8)$. Check: $g_1^Td_0=-38.4+38.4=0$ ✓.",
            "<strong>Step 2:</strong> $\\beta_0=\\frac{\\|g_1\\|^2}{\\|g_0\\|^2}=\\frac{46.08}{128}=0.36$, $d_1=-g_1+\\beta_0d_0=(-7.68,\\,1.92)$, $\\alpha_1=\\frac{46.08}{d_1^TQd_1}=\\frac{46.08}{147.456}=\\frac5{16}$, giving $x_2=(0,0)$ exactly."],
        "math": r"$$x_0=\begin{bmatrix}4\\1\end{bmatrix}\xrightarrow{\ \alpha_0=1/5\ }x_1=\begin{bmatrix}2.4\\-0.6\end{bmatrix}\xrightarrow{\ \beta_0=0.36,\ \alpha_1=5/16\ }x_2=\begin{bmatrix}0\\0\end{bmatrix}=x^*$$",
        "personalConnection": "Two cuts finish the job: the first cut removes the error along one conjugate direction, the second removes the rest, and the first cut is never spoiled.",
        "examTrap": "Always check the two identities: g₁ᵀd₀ = 0 (exact line search) and d₁ᵀQd₀ = 0 (conjugacy). Here d₀ᵀQd₁ = 2(−8)(−7.68) + 8(−8)(1.92) = 122.88 − 122.88 = 0 ✓."},
    802: {"drawingSvg": _sr1(802),
          "drawingCaption": "SR1 adds a rank-1 term: the curvature model changes along a single direction u"},
    803: {"drawingSvg": _dfp(803),
          "drawingCaption": "DFP is rank 2: it adds curvature information along s and removes the old guess along H y"},
    804: {"drawingSvg": _bfgs(804),
          "drawingCaption": "BFGS builds the new inverse-Hessian estimate so that it maps the gradient change y to the step s"},
    905: {
        "coreTranslation": [
            "<strong>What:</strong> if $x^*$ is a local minimizer over $\\Omega$, then $f$ cannot decrease to first order in any feasible direction: $\\nabla f(x^*)^Td\\ge0$ for every $d\\in T_\\Omega(x^*)$.",
            "<strong>How:</strong> moving a little along a feasible direction $d$ changes $f$ by about $\\nabla f(x^*)^Td$; if this were negative you would find a feasible point with smaller $f$.",
            "<strong>Why it matters:</strong> in cone language, $\\nabla f(x^*)$ lies in the dual cone $T_\\Omega(x^*)^*$ (equivalently $-\\nabla f(x^*)$ lies in the polar cone). This is the general first-order condition from which KKT is derived."],
        "examTrap": "This is a NECESSARY condition only. It also holds at constrained saddle points and maxima. For a convex f over a convex Ω it becomes sufficient."},
}
