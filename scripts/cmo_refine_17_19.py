"""CMO review, topics 17-19: simplify duality/LP/penalty cards, correct the augmented-Lagrangian example, split broad LP cards."""
import math
from subj_lib import *


def V(x0, y0, x1, y1, w=2.2, d=None):
    return L(x0, y0, x1, y1, w, d=d, ar=True)


POLY = "50,112 90,36 150,22 210,60 196,112"
VERTS = [(50, 112), (90, 36), (150, 22), (210, 60), (196, 112)]


# ---------------------------------------------------------------- diagrams
def _bfs(cid):
    return svg(cid, PG(POLY, "#f1f5f9", 1.8), *[C(x, y, 4) for x, y in VERTS],
               N(120, 76, "feasible set", 9, "middle", "bold"),
               N(46, 126, "each corner = a BFS:", 8.5, "start", "bold"), N(46, 138, "choose m basic columns, set the other n−m variables to 0", 8, "start"),
               N(150, 14, "n − m walls meet", 8.5, "middle"))


def _simplex(cid):
    return svg(cid, PG(POLY, "#f1f5f9", 1.6), *[C(x, y, 3.5) for x, y in VERTS],
               poly([VERTS[0], VERTS[1], VERTS[2]], 3.0), V(VERTS[1][0], VERTS[1][1], VERTS[2][0] - 2, VERTS[2][1] + 1, 3.0),
               N(VERTS[0][0], VERTS[0][1] + 14, "start", 8.5, "middle"), N(VERTS[2][0], VERTS[2][1] - 6, "x* (optimum)", 8.5, "middle", "bold"),
               L(120, 8, 170, 8, 0, None), N(120, 138, "walks from corner to adjacent corner along EDGES", 8.5, "middle", "bold"),
               N(214, 94, "each pivot swaps", 8, "end"), N(214, 106, "one basic variable", 8, "end"))


def _ipm(cid):
    return svg(cid, PG(POLY, "#f1f5f9", 1.6), *[C(x, y, 3) for x, y in VERTS],
               P("M96 96 C110 78 124 60 134 44 C140 36 144 30 148 26", w=3.0, ar=True),
               C(96, 96, 3.5), N(90, 106, "start (interior)", 8.5, "end"), C(150, 22, 4), N(150, 14, "x*", 9, "middle", "bold"),
               N(120, 138, "follows the smooth central path x(μ) through the INTERIOR", 8.5, "middle", "bold"),
               N(214, 94, "μ → 0", 9, "end", "bold"))


def _unbdd(cid):
    return svg(cid, PG("30,128 30,50 70,34 120,50 200,128", "#f1f5f9", 1.6),
               V(110, 64, 196, 22, 2.8), N(200, 20, "d = −y: Aᵀd ≤ 0", 8.5, "start", "bold"),
               N(200, 32, "bᵀd > 0", 8.5, "start", "bold"),
               N(80, 100, "dual feasible set", 8.5, "middle", "bold"),
               N(120, 138, "primal infeasible ⇒ dual can run to +∞ along d", 8.5, "middle", "bold"))


def _al(cid):
    ts = [2 / 3, 8 / 9, 26 / 27, 1.0]
    labs = ["x⁽⁰⁾ 0.67", "x⁽¹⁾ 0.89", "x⁽²⁾ 0.96", "x* = 1"]
    parts = [L(20, 110, 226, 110, 1.2, ar=True)]
    for i, t in enumerate(ts):
        x = 30 + (t - 0.6) / 0.4 * 170
        parts += [C(x, 110, 4, "#000000" if i < 3 else "#ffffff"), N(x, 96 - (i % 2) * 14, labs[i], 8.5, "middle", "bold")]
    parts += [N(24, 20, "error shrinks by 1/3 at every update:", 8.5, "start", "bold"), N(24, 34, "1/3, 1/9, 1/27, ...", 8.5, "start"),
              N(24, 48, "penalty weight c stays at 2 (no blow-up)", 8.5, "start"),
              N(120, 136, "iterates x₁ = x₂ = t on the line x₁ = x₂ approach (1,1)", 8, "middle")]
    return svg(cid, *parts)


# ---------------------------------------------------------------- fixes
FIX = {
    1702: {
        "coreTranslation": [
            "<strong>What:</strong> for a convex differentiable problem, if $x^*$ is optimal and has KKT multipliers $(\\lambda^*,\\mu^*)$, then $(x^*,\\lambda^*,\\mu^*)$ is optimal for the Wolfe dual.",
            "<strong>How:</strong> the KKT conditions say exactly that $(x^*,\\lambda^*,\\mu^*)$ is Wolfe-feasible ($\\nabla_x\\mathcal{L}=0$, $\\mu\\ge0$), and complementary slackness gives $\\mathcal{L}(x^*,\\lambda^*,\\mu^*)=f(x^*)$. Weak duality then says no Wolfe-feasible point beats it.",
            "<strong>Why it matters:</strong> primal minimum $=$ Wolfe dual maximum, with zero gap. Solve either problem and you get the other's value for free."]},
    1703: {
        "coreTranslation": [
            "<strong>What:</strong> for the QP $\\min\\tfrac12x^TQx+c^Tx$ s.t. $Ax\\ge b,\\ x\\ge0$ ($Q\\succ0$) the Wolfe dual is again a QP: $\\max_{x,y}\\ -\\tfrac12x^TQx+b^Ty$ s.t. $Qx-A^Ty+c\\ge0,\\ y\\ge0$.",
            "<strong>How:</strong> write $\\mathcal{L}=\\tfrac12x^TQx+c^Tx-y^T(Ax-b)-v^Tx$. Stationarity gives $Qx+c-A^Ty-v=0$, so $v=Qx+c-A^Ty\\ge0$ (that is the dual constraint). Substituting, the linear terms combine into $-x^TQx$, leaving $-\\tfrac12x^TQx+b^Ty$.",
            "<strong>Why it matters:</strong> the quadratic term flips sign and the roles of $b$ and $c$ swap, so you can check a QP solution by evaluating both objectives (they must agree)."]},
    1704: {
        "coreTranslation": [
            "<strong>What:</strong> the Wolfe dual is only valid for convex problems. For $\\min f(x)=-x^2$ the primal value is $-\\infty$.",
            "<strong>How:</strong> the Wolfe dual is $\\max f(x)$ s.t. $f'(x)=-2x=0$, whose only point is $x=0$ with value $0$. So $d^*=0>-\\infty=p^*$: weak duality fails.",
            "<strong>Why it happens:</strong> $\\nabla_x\\mathcal{L}=0$ only identifies the minimum of $\\mathcal{L}$ when $\\mathcal{L}$ is convex in $x$. In general it also finds maxima and saddles, giving false bounds."],
        "examTrap": "If a question gives a NON-convex problem and asks what the Wolfe dual says, the answer is: nothing reliable (it can exceed the primal value). Use ordinary Lagrangian duality, which always gives a valid lower bound."},
    1705: {
        "coreTranslation": [
            "<strong>What:</strong> the dual function $q(\\mu)$ is concave but often has kinks, so ordinary gradient ascent doesn't apply. The <em>subgradient method</em> maximizes it anyway.",
            "<strong>How:</strong> for the current $\\mu_k$ find $x(\\mu_k)=\\arg\\min_x\\mathcal{L}(x,\\mu_k)$; the constraint violation $g(x(\\mu_k))$ is a subgradient of $q$ at $\\mu_k$. Update $\\mu_{k+1}=\\big[\\mu_k+\\alpha_kg(x(\\mu_k))\\big]_+$ (project onto $\\mu\\ge0$).",
            "<strong>Why it matters:</strong> it works like a price adjustment: a violated constraint ($g_j>0$) gets a higher price $\\mu_j$. With steps $\\sum\\alpha_k=\\infty$, $\\sum\\alpha_k^2<\\infty$ it converges to the dual optimum, but $q(\\mu_k)$ is <em>not</em> monotone: keep the best iterate."]},
    1706: {
        "coreTranslation": [
            "<strong>What:</strong> minimize the negative entropy $\\sum x_i\\ln x_i$ subject to linear constraints $Ax=b$, $x>0$. Its dual turns out to be a smooth, unconstrained problem.",
            "<strong>How:</strong> $\\mathcal{L}=\\sum x_i\\ln x_i+\\lambda^T(b-Ax)$. Stationarity $\\ln x_i+1-(A^T\\lambda)_i=0$ gives $x_i=e^{(A^T\\lambda)_i-1}$ (automatically positive). Substituting, each term collapses to $-x_i$, so $q(\\lambda)=b^T\\lambda-\\sum_ie^{(A^T\\lambda)_i-1}$.",
            "<strong>Why it matters:</strong> you replace a constrained problem in $x$ by an unconstrained concave maximization in $\\lambda$, and the optimal $x$ has the exponential (Boltzmann) form."]},
    1801: {
        "coreTranslation": [
            "<strong>What:</strong> the standard-form LP $\\min c^Tx$ s.t. $Ax=b,\\ x\\ge0$ has the dual $\\max b^Ty$ s.t. $A^Ty\\le c$ ($y$ free).",
            "<strong>How (the dictionary):</strong> each primal <em>equality</em> row becomes a free dual variable $y_i$; each primal <em>non-negative variable</em> $x_j$ becomes a dual <em>inequality</em> $(A^Ty)_j\\le c_j$; $c$ and $b$ swap roles; and the dual of the dual is the primal.",
            "<strong>Why it matters:</strong> if the primal has $Ax\\ge b,\\ x\\ge0$, the dual is $\\max b^Ty$ s.t. $A^Ty\\le c,\\ y\\ge0$ (inequality rows give sign-restricted dual variables). Example: min $x_1+2x_2$ s.t. $x_1+x_2\\ge3$ has dual $\\max3y$ s.t. $y\\le1,\\ y\\le2,\\ y\\ge0$, both with value $3$."]},
    1802: {
        "title": "Fundamental Theorem of LP: The Optimum Is at a Vertex",
        "coreTranslation": [
            "<strong>What:</strong> for the standard LP $\\min c^Tx$ s.t. $Ax=b,\\ x\\ge0$: if a feasible point exists then a basic feasible solution (vertex) exists, and if an optimal point exists then an <em>optimal vertex</em> exists.",
            "<strong>How:</strong> a linear objective has no curvature, so from any non-vertex optimal point you can slide along the face without getting worse until you hit a vertex (the objective is constant or improves in at least one direction).",
            "<strong>Why it matters:</strong> you only need to search the finitely many vertices, which is what the simplex method does. A degenerate vertex (some basic variable equals 0) can make simplex pivot without moving."],
        "examTrap": "'An optimal vertex exists' does not mean every optimum is a vertex: when the objective is parallel to a face, the whole face is optimal. And a vertex is guaranteed to exist only if the feasible set has no line inside it (true when x ≥ 0)."},
    1804: {
        "title": "From Farkas to LP Duality: Infeasible Primal ⇒ Unbounded Dual",
        "drawingSvg": _unbdd(1804),
        "drawingCaption": "If Ax = b, x ≥ 0 is infeasible, Farkas hands you a direction d along which the dual objective grows forever",
        "math": r"$$A^Ty\ge0,\ b^Ty<0\ \Rightarrow\ d=-y:\ A^Td\le0,\ b^Td>0\ \Rightarrow\ b^T(y_0+td)\to+\infty\ \ (t\to\infty)$$",
        "coreTranslation": [
            "<strong>What:</strong> Farkas' lemma says exactly one of (1) $Ax=b,\\ x\\ge0$ and (2) $A^Ty\\ge0,\\ b^Ty<0$ holds. For an LP, (1) is <em>primal feasibility</em>, and (2) is the <em>certificate</em> that it is infeasible.",
            "<strong>How:</strong> let $y$ solve (2) and put $d=-y$. Then $A^Td\\le0$ and $b^Td>0$. So if some $y_0$ is dual feasible ($A^Ty_0\\le c$), so is $y_0+td$ for every $t\\ge0$, and the dual objective $b^T(y_0+td)\\to+\\infty$.",
            "<strong>Why it matters:</strong> this is the proof that 'primal infeasible and dual feasible' forces 'dual unbounded'. Together with the symmetric case it gives the four outcomes of LP duality: both optimal with equal values, or one unbounded and the other infeasible, or both infeasible."]},
    1805: {
        "title": "The Simplex Method: Walking Along the Edges",
        "drawingSvg": _simplex(1805),
        "drawingCaption": "Simplex hops from vertex to an adjacent, better vertex until no neighbor improves",
        "coreTranslation": [
            "<strong>What:</strong> Dantzig's simplex method (1947) moves along the 1-dimensional <em>edges</em> of the feasible polyhedron from one vertex (BFS) to an adjacent vertex with a better objective value.",
            "<strong>How:</strong> each <em>pivot</em> brings one non-basic variable into the basis and removes one basic variable. It stops when no neighbor improves the objective: that vertex is optimal.",
            "<strong>Why it matters:</strong> it returns an <em>exact</em> vertex solution and is superb in practice (typically linear in the number of constraints). Its worst case is exponential, as the Klee-Minty cube shows."],
        "math": r"$$x_B=B^{-1}b\ \ge0,\ \ x_N=0;\quad \text{optimal if all reduced costs}\ \ c_N^T-c_B^TB^{-1}N\ \ge\ 0$$",
        "personalConnection": "Hiking along the ridge-lines of a mountain: at every summit-corner you look at the neighboring corners and walk to one that is higher, until none is.",
        "examTrap": "A degenerate vertex (a basic variable equals 0) lets simplex pivot without moving and, in rare cases, cycle. Bland's rule prevents that."},
    1806: {
        "drawingCaption": "Primal max 3x₁ + 2x₂ = 12 at (2,3) matches dual min 5y₁ + 7y₂ = 12 at (1,1)",
        "coreTranslation": [
            "<strong>Problem:</strong> maximize $3x_1+2x_2$ s.t. $x_1+x_2\\le5,\\ 2x_1+x_2\\le7,\\ x\\ge0$. The best vertex is $x^*=(2,3)$, value $3(2)+2(3)=12$ (both constraints are tight there).",
            "<strong>Dual:</strong> minimize $5y_1+7y_2$ s.t. $y_1+2y_2\\ge3,\\ y_1+y_2\\ge2,\\ y\\ge0$. Complementary slackness: since $x_1^*,x_2^*>0$ both dual constraints must be equalities: $y_1+2y_2=3,\\ y_1+y_2=2$, so $y_2=1,\\ y_1=1$ (both $\\ge0$ ✓).",
            "<strong>Check:</strong> dual value $5(1)+7(1)=12$ equals the primal value, which proves $x^*$ is optimal. Both primal constraints are tight and both $y_i>0$, consistent with $y_i(\\text{slack}_i)=0$."]},
    1901: {},
    1903: {
        "coreTranslation": [
            "<strong>What:</strong> as the penalty weight $c\\to\\infty$, the penalty function becomes extremely ill-conditioned: its Hessian is $\\nabla^2f+c\\sum\\nabla h_i\\nabla h_i^T+c\\sum h_i\\nabla^2h_i$.",
            "<strong>How:</strong> the $p$ directions normal to the constraints get curvature that grows like $c$, while the $n-p$ tangent directions keep $O(1)$ curvature. So $\\kappa=\\lambda_{\\max}/\\lambda_{\\min}\\sim O(c)\\to\\infty$: a long, narrow canyon.",
            "<strong>Why it matters:</strong> gradient descent zig-zags and Newton systems lose accuracy. So raise $c$ gradually (e.g. $c_{k+1}=10c_k$) and warm-start each subproblem from the previous solution."]},
    1904: {
        "coreTranslation": [
            "<strong>What:</strong> even though penalty iterates are slightly infeasible, they hand you good estimates of the Lagrange multipliers for free: $\\lambda_i^{(k)}=c_k\\,h_i(x_k)$.",
            "<strong>How:</strong> at the minimizer $x_k$ of $q(c_k,x)=f+\\tfrac{c_k}2\\sum h_i^2$, $\\nabla f(x_k)+\\sum[c_kh_i(x_k)]\\nabla h_i(x_k)=0$. Compare with KKT, $\\nabla f+\\sum\\lambda_i^*\\nabla h_i=0$: the bracket plays the role of $\\lambda_i$. For inequalities, $\\mu_j^{(k)}=c_k\\max(0,g_j(x_k))$.",
            "<strong>Why it matters:</strong> since $\\lambda^{(k)}\\to\\lambda^*$ (finite) while $c_k\\to\\infty$, the constraint violation is $h_i(x_k)\\approx\\lambda_i^*/c_k$: it shrinks like $1/c_k$. This is also the idea behind the augmented Lagrangian."]},
    1905: {
        "coreTranslation": [
            "<strong>What:</strong> the augmented Lagrangian $\\mathcal{L}_c(x,\\lambda)=f+\\lambda^Th+\\tfrac c2\\|h\\|^2$ (Hestenes–Powell) adds a multiplier term to the quadratic penalty.",
            "<strong>How:</strong> alternate (1) minimize $\\mathcal{L}_c(x,\\lambda_k)$ over $x$; (2) update the multiplier by $\\lambda_{k+1}=\\lambda_k+c\\,h(x_k)$ (gradient <em>ascent</em> on the dual, with a plus sign).",
            "<strong>Why it matters:</strong> the multiplier does most of the work of balancing $-\\nabla f$, so $c$ only has to be large enough to make $\\mathcal{L}_c$ locally convex, a <em>finite</em> value. No $c\\to\\infty$ means no ill-conditioning."]},
    1906: {
        "drawingSvg": _al(1906),
        "drawingCaption": "With c fixed at 2, each multiplier update cuts the error by a factor of 3",
        "coreTranslation": [
            "<strong>Problem:</strong> minimize $x_1^2+x_2^2$ s.t. $h(x)=x_1+x_2-2=0$ (solution $x^*=(1,1)$, $\\lambda^*=-2$). Use $\\mathcal{L}_c=x_1^2+x_2^2+\\lambda h+\\tfrac c2h^2$ with $c=2$, $\\lambda_0=0$. By symmetry set $x_1=x_2=t$: $\\partial_x\\mathcal{L}=2t+\\lambda+2(2t-2)=0\\Rightarrow t=\\frac{4-\\lambda}{6}$.",
            "<strong>Iteration 1:</strong> $\\lambda_0=0$ gives $t=\\tfrac23$, so $h=-\\tfrac23$ and $\\lambda_1=0+2(-\\tfrac23)=-\\tfrac43$. <strong>Iteration 2:</strong> $t=\\frac{4+4/3}{6}=\\tfrac89$, $h=-\\tfrac29$, $\\lambda_2=-\\tfrac43-\\tfrac49=-\\tfrac{16}9$. <strong>Iteration 3:</strong> $t=\\tfrac{26}{27}$.",
            "<strong>Pattern:</strong> $x^{(k)}=1-3^{-(k+1)}$ and $\\lambda_k-\\lambda^*=-2\\cdot3^{-k}$: the error drops by a factor of 3 each update while $c$ stays at 2."],
        "math": r"$$\lambda_0=0\to x^{(0)}=\Big(\tfrac23,\tfrac23\Big);\ \ \lambda_1=-\tfrac43\to x^{(1)}=\Big(\tfrac89,\tfrac89\Big);\ \ \lambda_2=-\tfrac{16}9\to x^{(2)}=\Big(\tfrac{26}{27},\tfrac{26}{27}\Big)\to(1,1),\ \lambda^*=-2$$",
        "examTrap": "Compare with the plain quadratic penalty, whose minimizer is x = c/(1+c)·(1,1): the error is 1/(1+c), so 1% accuracy needs c ≈ 100 (and a terribly conditioned Hessian). The augmented Lagrangian reaches 0.4% with c = 2 after 4 multiplier updates."},
}
del FIX[1901]

NEW = [
    (1801, {
        "id": 1807, "title": "Basic Feasible Solutions = Vertices",
        "category": "POLYHEDRAL GEOMETRY",
        "drawingSvg": _bfs(1807),
        "drawingCaption": "Every corner of the feasible polyhedron is a basic feasible solution, found by zeroing n − m variables",
        "coreTranslation": [
            "<strong>What:</strong> in the standard form $\\{x:Ax=b,\\ x\\ge0\\}$ with $A$ of size $m\\times n$ (full row rank), the <em>corners</em> of the feasible region are exactly the <strong>basic feasible solutions (BFS)</strong>.",
            "<strong>How:</strong> choose $m$ columns forming an invertible basis $B$, set the other $n-m$ variables to $0$ (so $n-m$ constraints $x_j\\ge0$ are tight), and solve $x_B=B^{-1}b$. It is a BFS if $x_B\\ge0$.",
            "<strong>Why it matters:</strong> there are at most $\\binom nm$ vertices, a finite list. A BFS with some $x_B$ entry equal to $0$ is <em>degenerate</em>: more than $n-m$ walls meet there."],
        "math": r"$$x=\begin{bmatrix}x_B\\x_N\end{bmatrix}=\begin{bmatrix}B^{-1}b\\\mathbf 0\end{bmatrix},\quad B\ \text{invertible},\ \ x_B\ge0\iff x\ \text{is a vertex of}\ \{Ax=b,\ x\ge0\}$$",
        "personalConnection": "Pinning a tent to the ground at its corners: each corner is where enough walls meet that there is nowhere to slide, and the tent's lowest points are always at corners.",
        "examTrap": "A vertex is not 'any point with m non-zeros'. It needs the columns of the non-zero entries to be linearly independent. Two different bases can describe the same degenerate vertex."}),
    (1805, {
        "id": 1808, "title": "Interior-Point Methods: The Central Path",
        "category": "LP ALGORITHMS",
        "drawingSvg": _ipm(1808),
        "drawingCaption": "Interior-point methods follow a smooth curve through the middle of the polyhedron toward the optimum",
        "coreTranslation": [
            "<strong>What:</strong> instead of walking along the edges, interior-point methods (Karmarkar 1984) stay <em>strictly inside</em> the feasible set and follow the <strong>central path</strong> $x(\\mu)$ as a barrier parameter $\\mu\\to0$.",
            "<strong>How:</strong> for each $\\mu>0$ solve $\\min c^Tx-\\mu\\sum_j\\ln x_j$ s.t. $Ax=b$. The log term repels the walls; shrinking $\\mu$ lets the iterate approach the optimal vertex. Primal-dual versions solve for $x$ and $y$ together by Newton's method.",
            "<strong>Why it matters:</strong> they take a few dozen iterations even for huge problems and have polynomial worst-case complexity $O(\\sqrt nL)$ iterations. The answer is only $\\epsilon$-optimal, so an exact vertex needs a 'crossover' step."],
        "math": r"$$x(\mu)=\arg\min_{Ax=b,\ x>0}\Big\{c^Tx-\mu\sum_{j=1}^n\ln x_j\Big\}\ \xrightarrow{\ \mu\to0\ }\ x^*$$",
        "personalConnection": "Driving down the middle of a wide boulevard toward a destination at the far end instead of scraping along the curbs at every corner.",
        "examTrap": "Simplex returns an exact vertex; interior-point methods return a point inside the polyhedron within ε of optimal. Know which one a question's 'basic solution' wording requires."}),
]
