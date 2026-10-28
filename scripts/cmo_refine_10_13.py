"""CMO review, topics 10-13: simplify dense statements, redraw formula-box diagrams, split projections card, add numeric Farkas example."""
import math
from subj_lib import *


def V(x0, y0, x1, y1, w=2.2, d=None):
    return L(x0, y0, x1, y1, w, d=d, ar=True)


# ---------------------------------------------------------------- diagrams
def _gordan(cid):
    def ang(cx, cy, deg, ln):
        return cx + ln * math.cos(math.radians(deg)), cy - ln * math.sin(math.radians(deg))
    parts = [N(60, 12, "Ax < 0 has a solution", 9, "middle", "bold"), L(20, 80, 100, 80, 1.2, d="3 3"), C(60, 80, 2.5)]
    for k, a in enumerate([35, 80, 125]):
        x, y = ang(60, 80, a, 38); parts += [V(60, 80, x, y, 2.2), N(x + 2, y - 3, f"a{k+1}", 8.5, "start", "bold")]
    parts += [V(60, 80, 60, 126, 2.6), N(68, 124, "x", 9, "start", "bold"), N(60, 140, "every aᵢ·x < 0", 8.5, "middle")]
    parts += [L(120, 6, 120, 142, 1, d="4 3"), N(180, 12, "or: 0 ∈ conv{aᵢ}", 9, "middle", "bold"), C(180, 80, 2.5)]
    pts = []
    for k, a in enumerate([90, 210, 330]):
        x, y = ang(180, 80, a, 38); pts.append((x, y)); parts += [V(180, 80, x, y, 2.2), N(x + 2, y - 3, f"a{k+1}", 8.5, "start", "bold")]
    parts.append(P("M{:.0f} {:.0f} L{:.0f} {:.0f} L{:.0f} {:.0f} Z".format(*pts[0], *pts[1], *pts[2]), "none", 1.2, "3 3"))
    parts += [N(180, 140, "Aᵀy = 0, y ≥ 0, y ≠ 0", 8.5, "middle")]
    return svg(cid, *parts)


def _cs(cid):
    # left: inactive; right: active
    return svg(cid,
               R(10, 18, 100, 100, "#f1f5f9", 1.6, 10), N(60, 14, "inactive: g < 0", 9, "middle", "bold"),
               C(40, 68, 4), C(40, 68, 16, "none", 1), C(40, 68, 28, "none", 1), N(40, 90, "min of f", 8, "middle"),
               N(60, 104, "wall far away", 8.5, "middle"), N(60, 130, "μ = 0", 11, "middle", "bold"),
               L(120, 8, 120, 142, 1, d="4 3"),
               PG("130,18 200,18 200,118 130,118", "#f1f5f9", 1.6), L(200, 18, 200, 118, 3.2), N(165, 14, "active: g = 0", 9, "middle", "bold"),
               C(200, 68, 4), V(200, 68, 232, 68, 2.4), N(222, 58, "−∇f", 8.5, "end", "bold"), V(200, 68, 172, 68, 2.4, "4 3"), N(176, 58, "wall", 8.5, "end"),
               N(165, 96, "pulls out, wall pushes back", 8, "middle"), N(180, 130, "μ > 0", 11, "middle", "bold"))


def _nonexp(cid):
    return svg(cid,
               E(70, 72, 52, 40, 0, "#f1f5f9", 1.8), N(70, 76, "C", 12, "middle", "bold"),
               C(150, 28, 3.5), N(156, 24, "x", 10, "start", "bold"), C(178, 118, 3.5), N(184, 122, "y", 10, "start", "bold"),
               C(112, 48, 3.5), N(106, 44, "Π(x)", 9, "end", "bold"), C(112, 100, 3.5), N(106, 112, "Π(y)", 9, "end", "bold"),
               L(150, 28, 178, 118, 1.4, d="5 3"), L(112, 48, 112, 100, 2.4), L(150, 28, 112, 48, 1, d="2 2"), L(178, 118, 112, 100, 1, d="2 2"),
               N(214, 76, "‖x−y‖", 8.5, "middle"), N(214, 88, "(long)", 8, "middle"), N(86, 140, "‖Π(x)−Π(y)‖ ≤ ‖x−y‖  (never longer)", 8.5, "start", "bold"))


def _halfspace(cid):
    return svg(cid,
               PG("20,128 180,128 180,84 20,84", "#f1f5f9", 0, None), L(10, 100, 200, 60, 2.6), N(204, 58, "aᵀx = b", 8.5, "start", "bold"),
               V(100, 80, 96, 44, 2.0), N(100, 40, "a", 10, "start", "bold"),
               C(70, 32, 3.5), N(76, 28, "x", 10, "start", "bold"), C(66, 76, 3.5), L(70, 32, 66, 76, 1.6, d="4 3"), N(72, 56, "Π(x)", 8.5, "start", "bold"),
               C(150, 112, 3.5), N(156, 114, "inside: stays put", 8.5, "start"),
               N(120, 138, "Π(x) = x − (aᵀx − b)/‖a‖² · a   (only if aᵀx > b)", 8.5, "middle", "bold"))


def _boxball(cid):
    return svg(cid,
               R(20, 36, 70, 60, "#f1f5f9", 1.8), C(114, 20, 3.5), N(120, 18, "x", 9, "start", "bold"), C(90, 36, 3.5), L(114, 20, 90, 36, 1.2, d="3 3"),
               N(55, 70, "box [l, u]", 9, "middle", "bold"), N(60, 112, "clamp each coordinate", 8.5, "middle", "bold"),
               C(180, 66, 34, "#f1f5f9", 1.8), N(180, 70, "‖x‖≤R", 8.5, "middle", "bold"), C(224, 22, 3.5), N(222, 14, "x", 9, "end", "bold"),
               C(180 + 34 * 0.8, 66 - 34 * 0.6, 3.5), L(224, 22, 180 + 34 * 0.8, 66 - 34 * 0.6, 1.2, d="3 3"), L(180, 66, 224, 22, 0.8, d="2 2"),
               N(180, 112, "scale x to length R", 8.5, "middle", "bold"),
               N(120, 138, "also R₊ⁿ: max(0, xᵢ)", 8.5, "middle"))


def _farkas_num(cid):
    o = (60, 100)
    p = lambda x, y: (o[0] + 40 * x, o[1] - 40 * y)
    return svg(cid,
               PG("{},{} {},{} {},{}".format(*o, *p(2.6, 0), *p(2.6, 2.6)), "#f1f5f9", 0),
               L(*o, *p(2.6, 0), 1, d="3 3"), L(*o, *p(2.6, 2.6), 1, d="3 3"),
               V(*o, *p(1, 0), 2.6), N(p(1, 0)[0], p(1, 0)[1] + 12, "a₁", 9, "middle", "bold"), V(*o, *p(1, 1), 2.6), N(p(1, 1)[0] + 4, p(1, 1)[1] - 6, "a₂", 9, "start", "bold"),
               C(*p(2, 1), 4), N(p(2, 1)[0] + 6, p(2, 1)[1] - 2, "b=(2,1) ∈ cone", 8.5, "start", "bold"),
               C(*p(0, 1), 4, "#ffffff"), N(p(0, 1)[0] - 6, p(0, 1)[1] - 4, "b′=(0,1) ∉", 8.5, "end", "bold"),
               V(*o, o[0] + 36, o[1] + 36, 2.2, "4 3"), N(o[0] + 40, o[1] + 46, "y=(1,−1)", 8.5, "start", "bold"),
               L(o[0] - 36, o[1] + 36, o[0] + 60, o[1] - 60, 1.4, d="6 3"),
               N(170, 20, "cone = all x₁a₁ + x₂a₂,", 8.5, "start"), N(170, 32, "x ≥ 0", 8.5, "start"),
               N(170, 124, "y·a₁=1, y·a₂=0 ≥ 0", 8.5, "start", "bold"), N(170, 136, "y·b′ = −1 < 0", 8.5, "start", "bold"))


def _simplex(cid):
    base = 100
    xs = [1.5, 1.0, 0.2, -0.3]
    tau = 0.75
    sc = 50
    parts = [L(14, base, 226, base, 1.2)]
    for i, v in enumerate(xs):
        x0 = 30 + i * 46
        if v >= 0:
            parts.append(R(x0, base - v * sc, 30, v * sc, "#ffffff", 1.4))
            if v > tau:
                parts.append(R(x0, base - v * sc, 30, (v - tau) * sc, "#d9dee7", 1.4))
        else:
            parts.append(R(x0, base, 30, -v * sc, "#ffffff", 1.4, 0, "3 2"))
        parts.append(N(x0 + 15, base + 24 if v >= 0 else base - v * sc + 12, f"x{i+1}={v}", 8.5, "middle"))
    parts += [L(14, base - tau * sc, 226, base - tau * sc, 1.4, d="5 3"), N(224, base - tau * sc - 4, "τ = 0.75", 9, "end", "bold"),
              N(120, 12, "shaded = what survives:  p = (0.75, 0.25, 0, 0),  Σp = 1", 9, "middle", "bold"),
              N(120, 142, "water-level τ: cut every bar at τ, drop what falls below 0", 8.5, "middle")]
    return svg(cid, *parts)


# ---------------------------------------------------------------- fixes
FIX = {
    1001: {
        "coreTranslation": [
            "<strong>What:</strong> two convex sets $A$ and $B$ that do not overlap can always be split by a flat wall (hyperplane): there are $a\\ne0$ and $\\beta$ with $a^Tx\\le\\beta\\le a^Ty$ for all $x\\in A$, $y\\in B$.",
            "<strong>How:</strong> the wall $H=\\{z:a^Tz=\\beta\\}$ puts $A$ in the lower half-space and $B$ in the upper. If $A$ is closed and $B$ is compact, there is a gap and the separation can be strict: $a^Tx<\\beta<a^Ty$.",
            "<strong>Why it matters:</strong> this is the engine behind Farkas' lemma, the KKT conditions and duality: whenever a point is outside a convex set, there is a wall that proves it."]},
    1002: {
        "coreTranslation": [
            "<strong>What:</strong> at every boundary point $x_0$ of a convex set $C$ you can lay a flat wall touching $C$ at $x_0$ with all of $C$ on one side: $a^T(x-x_0)\\le0$ for all $x\\in C$.",
            "<strong>How:</strong> the wall is $H=\\{x:a^Tx=a^Tx_0\\}$ and $a$ is a normal vector pointing away from $C$. At a smooth point $a$ is unique (the gradient direction); at a corner there are many valid $a$ (a whole cone of normals).",
            "<strong>Why it matters:</strong> a closed convex set is exactly the intersection of all its supporting half-spaces, and normal vectors are what become the multipliers in KKT."],
        "examTrap": "At a corner the supporting hyperplane is NOT unique: there is a whole cone of valid normals (the normal cone). Uniqueness holds only at smooth boundary points."},
    1003: {
        "coreTranslation": [
            "<strong>What:</strong> for a matrix $A$ and a vector $b$, <em>exactly one</em> of two statements is true: (1) $b$ is a non-negative combination of the columns of $A$ ($Ax=b,\\ x\\ge0$), or (2) some $y$ has $A^Ty\\ge0$ but $b^Ty<0$.",
            "<strong>How:</strong> the non-negative combinations of the columns form a closed convex cone $K$. If $b\\notin K$, the separating hyperplane theorem gives a wall $y$ with $K$ on its non-negative side and $b$ strictly on the other side.",
            "<strong>Why it matters:</strong> $y$ is a one-line <em>certificate</em> that $b$ is not in the cone. This is the tool that produces KKT multipliers and proves LP duality."]},
    1004: {
        "drawingSvg": _gordan(1004),
        "drawingCaption": "Either some direction x makes every aᵢ·x negative (vectors in a half-plane), or the aᵢ surround the origin",
        "coreTranslation": [
            "<strong>What:</strong> for a matrix $A$ with rows $a_i^T$, exactly one holds: (1) some $x$ has $Ax<0$ (every $a_i^Tx$ is strictly negative), or (2) some $y\\ge0$, $y\\ne0$ has $A^Ty=0$.",
            "<strong>How:</strong> case (1) means all the vectors $a_i$ lie in an open half-plane (you can point $x$ away from all of them). Case (2) means the vectors $a_i$ surround the origin: $0$ is in their convex hull.",
            "<strong>Why it matters:</strong> Gordan is Farkas for strict inequalities. It is used to show 'no descent direction' implies $\\sum y_i\\nabla g_i=0$ (the Fritz-John conditions)."]},
    1101: {
        "coreTranslation": [
            "<strong>What:</strong> for $\\min f(x)$ subject to $h_i(x)=0$ and $g_j(x)\\le0$, a local minimizer that satisfies a constraint qualification (such as LICQ) has multipliers $\\lambda^*,\\mu^*$ making four conditions true.",
            "<strong>How:</strong> (1) <em>Stationarity</em> $\\nabla f+\\sum\\lambda_i\\nabla h_i+\\sum\\mu_j\\nabla g_j=0$; (2) <em>primal feasibility</em> $h=0,\\ g\\le0$; (3) <em>dual feasibility</em> $\\mu\\ge0$; (4) <em>complementary slackness</em> $\\mu_jg_j=0$.",
            "<strong>Why it matters:</strong> these four conditions turn a constrained minimization into a system you can solve by cases. They are necessary at a minimizer, and sufficient when the problem is convex."]},
    1102: {
        "drawingSvg": _cs(1102),
        "drawingCaption": "Wall far away: no force (μ = 0). Standing on the wall: the wall pushes back (μ > 0)",
        "coreTranslation": [
            "<strong>What:</strong> complementary slackness says $\\mu_j\\,g_j(x^*)=0$ for every inequality: for each constraint, either the multiplier is zero or the constraint is active, never a positive multiplier on a slack constraint.",
            "<strong>How:</strong> if $g_j(x^*)<0$ (inside, not touching) then $\\mu_j=0$ because the wall does nothing. If $\\mu_j>0$ then $g_j(x^*)=0$ because the wall only pushes when you are on it.",
            "<strong>Why it matters:</strong> it is an on/off switch that lets you solve KKT by guessing which constraints are active. Both $g_j=0$ and $\\mu_j=0$ can hold at once (weak complementarity, a degenerate case)."]},
    1203: {
        "coreTranslation": [
            "<strong>What:</strong> the second-order test needs $d^T\\nabla^2_{xx}\\mathcal{L}\\,d>0$ only for directions $d$ in the tangent subspace. The bordered Hessian lets you test that without computing a basis of the subspace.",
            "<strong>How:</strong> with $p$ equality constraints and $A=\\nabla h(x^*)^T$, form $B=\\begin{bmatrix}0&A\\\\A^T&L\\end{bmatrix}$ ($L=\\nabla^2_{xx}\\mathcal{L}$). A strict local minimum needs the last $n-p$ leading principal minors of $B$ to all have the sign $(-1)^p$.",
            "<strong>Why it matters:</strong> for one constraint ($p=1$) in 2D you only check one number: $\\det B<0$ means minimum. Students often expect $\\det>0$ because that is the unconstrained rule."]},
    1206: {
        "coreTranslation": [
            "<strong>Problem:</strong> minimize $x_1+x_2$ on the circle $x_1^2+x_2^2=1$. Stationarity $1+2\\lambda x_i=0$ gives $x_1=x_2=-\\tfrac1{2\\lambda}$, so the candidates are $\\pm\\tfrac1{\\sqrt2}(1,1)$; take $x^*=(-\\tfrac1{\\sqrt2},-\\tfrac1{\\sqrt2})$ with $\\lambda^*=\\tfrac1{\\sqrt2}$.",
            "<strong>Second order:</strong> $\\nabla h=(-\\sqrt2,-\\sqrt2)$ and $\\nabla^2_{xx}\\mathcal{L}=2\\lambda^*I=\\sqrt2\\,I$, so $B=\\begin{bmatrix}0&-\\sqrt2&-\\sqrt2\\\\-\\sqrt2&\\sqrt2&0\\\\-\\sqrt2&0&\\sqrt2\\end{bmatrix}$ and $\\det B=-4\\sqrt2<0$, which is the required sign $(-1)^1=-1$. So $x^*$ is a strict local minimum.",
            "<strong>Cross-check:</strong> at the other candidate $+\\tfrac1{\\sqrt2}(1,1)$ we get $\\lambda^*=-\\tfrac1{\\sqrt2}$ and $\\det B=+4\\sqrt2>0$, which has the wrong sign: it is the maximum."]},
    1301: {
        "coreTranslation": [
            "<strong>What:</strong> for a non-empty, closed, convex set $C$ and any point $x$ there is exactly one closest point $\\Pi_C(x)\\in C$.",
            "<strong>How:</strong> $p=\\Pi_C(x)$ exactly when $\\langle x-p,\\ y-p\\rangle\\le0$ for every $y\\in C$: the arrow from $p$ to $x$ makes an obtuse (or right) angle with every arrow from $p$ into the set.",
            "<strong>Why it matters:</strong> this one inequality characterizes projections; it is the backbone of projected gradient, optimality conditions and every fixed-point argument that follows."]},
    1302: {
        "drawingSvg": _nonexp(1302),
        "coreTranslation": [
            "<strong>What:</strong> projecting two points onto a convex set never moves them farther apart: $\\|\\Pi_C(x)-\\Pi_C(y)\\|\\le\\|x-y\\|$ (the projection is 1-Lipschitz, or <em>non-expansive</em>).",
            "<strong>How:</strong> it is even <em>firmly</em> non-expansive: $\\|\\Pi_C(x)-\\Pi_C(y)\\|^2\\le\\langle\\Pi_C(x)-\\Pi_C(y),\\ x-y\\rangle$, which follows by adding the two variational inequalities for $x$ and $y$.",
            "<strong>Why it matters:</strong> projections can never blow errors up, which is why projected gradient and alternating projections are stable. But it is not a strict contraction: points already inside $C$ keep their distance."]},
    1303: {
        "title": "Projection onto a Hyperplane and a Halfspace",
        "drawingSvg": _halfspace(1303),
        "drawingCaption": "Slide the point along the normal a until it lands on the wall; if it is already on the allowed side, do nothing",
        "coreTranslation": [
            "<strong>What:</strong> the hyperplane $\\{x:a^Tx=b\\}$ and the halfspace $\\{x:a^Tx\\le b\\}$ have one-line closed-form projections.",
            "<strong>How (hyperplane):</strong> subtract the part of $x$ that sticks out along the normal: $\\Pi(x)=x-\\frac{a^Tx-b}{\\|a\\|^2}\\,a$. <strong>(Halfspace):</strong> do the same, but only if $a^Tx>b$; otherwise $x$ is already feasible: $\\Pi(x)=x-\\frac{\\max(0,\\,a^Tx-b)}{\\|a\\|^2}\\,a$.",
            "<strong>Why it matters:</strong> these two formulas are the building blocks for projecting onto polyhedra (e.g. by Dykstra) and for constraint-by-constraint methods. Example: $x=(3,1)$, $a=(1,1)$, $b=2$ gives $\\Pi=(3,1)-\\tfrac{4-2}{2}(1,1)=(2,0)$."],
        "math": r"$$\Pi_{\{a^Tx=b\}}(x)=x-\frac{a^Tx-b}{\|a\|^2}a,\qquad \Pi_{\{a^Tx\le b\}}(x)=x-\frac{\max(0,\,a^Tx-b)}{\|a\|^2}a$$",
        "personalConnection": "Dropping a ball straight down onto a tilted table: it lands directly below along the table's normal. If it is already on the table side that you allow, it just stays.",
        "examTrap": "For the halfspace use max(0, aᵀx − b): a feasible point must NOT move. Applying the hyperplane formula to a halfspace wrongly drags inside points onto the boundary."},
    1304: {
        "coreTranslation": [
            "<strong>What:</strong> for a closed convex cone $K$ and its polar cone $K^\\circ$, every vector splits uniquely into $x=\\Pi_K(x)+\\Pi_{K^\\circ}(x)$ with the two pieces perpendicular.",
            "<strong>How:</strong> the polar cone $K^\\circ=\\{y:\\langle y,x\\rangle\\le0\\ \\forall x\\in K\\}$ is the set of vectors at an obtuse (or right) angle to everything in $K$. The pieces satisfy $\\langle\\Pi_K(x),\\Pi_{K^\\circ}(x)\\rangle=0$.",
            "<strong>Why it matters:</strong> it generalizes the split of $\\mathbb{R}^n$ into a subspace plus its orthogonal complement to cones. In 1-D it is just $x=\\max(0,x)+\\min(0,x)$."]},
    1306: {
        "title": "Worked Benchmark: Projecting onto the Simplex",
        "drawingSvg": _simplex(1306),
        "drawingCaption": "Find the water-level τ, cut every coordinate down by τ, and drop what falls below zero",
        "coreTranslation": [
            "<strong>Problem:</strong> project $x=(1.5,\\,1.0,\\,0.2,\\,-0.3)$ onto the simplex $\\{p\\ge0,\\ \\sum p_i=1\\}$. The answer has the form $p_i=\\max(0,\\,x_i-\\tau)$ for a single threshold $\\tau$ with $\\sum p_i=1$.",
            "<strong>Find $\\tau$:</strong> sort descending ($1.5,1.0,0.2,-0.3$). For $k$ active coordinates try $\\tau_k=\\frac{(\\text{sum of top }k)-1}{k}$: $\\tau_1=0.5$, $\\tau_2=\\frac{2.5-1}{2}=0.75$, $\\tau_3=\\frac{2.7-1}{3}\\approx0.57$. Keep the largest $k$ with $x_{(k)}>\\tau_k$: $1.0>0.75$ ✓ but $0.2>0.57$ ✗, so $k=2$, $\\tau=0.75$.",
            "<strong>Result:</strong> $p=(1.5-0.75,\\ 1.0-0.75,\\ 0,\\ 0)=(0.75,\\ 0.25,\\ 0,\\ 0)$. Check: $p\\ge0$ and $\\sum p=1$ ✓."],
        "math": r"$$\Pi_\Delta(x)=\max(0,\,x-\tau\mathbf 1),\quad \tau=\frac{\sum_{i\le k}x_{(i)}-1}{k}=\frac{2.5-1}{2}=0.75\ \Rightarrow\ p=(0.75,\,0.25,\,0,\,0)$$",
        "personalConnection": "Pouring water level τ into uneven terraces: terraces higher than the water keep what sticks out above it, lower ones stay dry, and the total water is exactly 1.",
        "examTrap": "Do not just clip negatives and divide by the sum: that gives (1.5, 1.0, 0.2, 0)/2.7 = (0.56, 0.37, 0.07, 0), which is NOT the Euclidean projection. The threshold τ must be subtracted first. Sorting makes it O(n log n); a median-finding method gets O(n)."},
}

NEW = [
    (1003, {
        "id": 1007, "title": "Worked Example: Farkas with Real Numbers",
        "category": "THEOREMS OF THE ALTERNATIVE",
        "drawingSvg": _farkas_num(1007),
        "drawingCaption": "b = (2,1) is inside the cone of a₁, a₂; b′ = (0,1) is outside, and y = (1,−1) is a wall that proves it",
        "coreTranslation": [
            "<strong>Setup:</strong> columns $a_1=(1,0)$ and $a_2=(1,1)$, so $A=\\begin{pmatrix}1&1\\\\0&1\\end{pmatrix}$. Is $b=(2,1)$ a non-negative combination of them? Is $b'=(0,1)$?",
            "<strong>$b=(2,1)$:</strong> solve $x_1+x_2=2$, $x_2=1$, so $x=(1,1)\\ge0$ ✓: system 1 holds (and so system 2 must fail). <strong>$b'=(0,1)$:</strong> $x_2=1$ and $x_1+x_2=0$ force $x_1=-1<0$, so system 1 has no solution.",
            "<strong>Certificate for $b'$:</strong> take $y=(1,-1)$. Then $A^Ty=(y\\cdot a_1,\\ y\\cdot a_2)=(1,\\ 0)\\ge0$ and $b'^Ty=-1<0$. This proves in one line that $b'$ is not in the cone: system 2 holds."],
        "math": r"$$A^Ty=\begin{pmatrix}1\\0\end{pmatrix}\ge0,\quad b'^Ty=-1<0\ \Rightarrow\ b'\notin\operatorname{cone}(a_1,a_2)$$",
        "personalConnection": "Fencing a field: if a stray sheep (b′) is outside the pen, you can show it with a single wall (y) that has the whole pen on one side and the sheep on the other.",
        "examTrap": "To prove 'b is NOT a non-negative combination' do not try all x. Exhibit one y with Aᵀy ≥ 0 and bᵀy < 0. Check both inequalities, including the sign of bᵀy."}),
    (1303, {
        "id": 1307, "title": "Projection onto a Box and a Ball",
        "category": "CLOSED-FORM PROJECTIONS",
        "drawingSvg": _boxball(1307),
        "drawingCaption": "Box: clamp each coordinate to its interval. Ball: shrink the point radially onto the sphere",
        "coreTranslation": [
            "<strong>What:</strong> boxes (including the non-negative orthant) and Euclidean balls also have simple closed-form projections.",
            "<strong>How (box $[l,u]$):</strong> project each coordinate separately: $[\\Pi(x)]_i=\\min(u_i,\\max(l_i,x_i))$. For $\\mathbb{R}^n_+$ this is $\\max(0,x_i)$, the ReLU. <strong>(Ball $\\|x\\|\\le R$):</strong> keep $x$ if it is inside, otherwise scale it to length $R$: $\\Pi(x)=x\\cdot\\min(1,R/\\|x\\|)$.",
            "<strong>Why it matters:</strong> these cost only $O(n)$, which is why projected gradient is so cheap for bound constraints. Not every set is this easy: the simplex needs a sort (see the worked benchmark)."],
        "math": r"$$[\Pi_{[l,u]}(x)]_i=\min\big(u_i,\max(l_i,x_i)\big),\qquad \Pi_{\mathcal B(0,R)}(x)=\frac{x}{\max(1,\ \|x\|/R)}$$",
        "personalConnection": "An audio limiter clamps every sample to ±1 (box); a volume knob turns the whole signal down until its peak fits (ball).",
        "examTrap": "Clamping works coordinate by coordinate only for BOXES (the constraints separate). It is wrong for the ball and for the simplex, where you cannot treat coordinates independently."}),
]
