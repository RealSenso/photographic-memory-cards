#!/usr/bin/env python3
"""
build_practice_cmo_17_19.py
Appends practice questions (flippable cards) for CMO Topics 17, 18 & 19 to practice_cmo.js.
  Topic 17: Wolfe Duality
  Topic 18: Linear Programming Duality and Polyhedral Geometry
  Topic 19: Penalty and Barrier Methods
"""

import json
import os

NEW_CARDS = [
    # =========================================================================
    # TOPIC 17: Wolfe Duality
    # =========================================================================
    {
        "id": 11791,
        "subject": "CMO",
        "topicId": "17_Wolfe_Duality",
        "topicTitle": "17 · Wolfe Duality",
        "title": "Wolfe Dual Formulation (IISc Endsem 2024)",
        "kind2": "pyq",
        "source": "IISc Endsem 2024 / Luenberger Ch 14",
        "marks": "[10 Marks]",
        "question": """<p>Consider the convex minimization problem:
$$\\min_{x_1, x_2} e^{x_1} + e^{x_2} \\quad \\text{subject to} \\quad x_1 + x_2 \\ge 2$$
<span class="part">(a)</span> State the definition of the Wolfe dual problem in terms of $(x, \\mu)$.<br>
<span class="part">(b)</span> Use the stationarity condition $\\nabla_x \\mathcal{L}(x, \\mu) = 0$ to eliminate $x$ and obtain an explicit 1D concave maximization problem in the multiplier $\\mu$.<br>
<span class="part">(c)</span> Solve for the optimal dual multiplier $\\mu^*$, reconstruct the optimal primal point $x^*$, and verify that strong duality holds.</p>""",
        "solution": """<p><span class="part">Part (a): Wolfe Dual Definition</span><br>
Standard form constraint: $g(x) = 2 - x_1 - x_2 \\le 0$.<br>
The Lagrangian is:
$$\\mathcal{L}(x, \\mu) = e^{x_1} + e^{x_2} + \\mu (2 - x_1 - x_2)$$
The Wolfe dual problem is:
$$\\max_{x, \\mu} \\mathcal{L}(x, \\mu) \\quad \\text{subject to} \\quad \\nabla_x \\mathcal{L}(x, \\mu) = 0, \\quad \\mu \\ge 0$$</p>

<p><span class="part">Part (b): Eliminating $x$</span><br>
Compute the gradient with respect to $x$:
$$\\frac{\\partial \\mathcal{L}}{\\partial x_1} = e^{x_1} - \\mu = 0 \\implies e^{x_1} = \\mu \\implies x_1 = \\ln \\mu$$
$$\\frac{\\partial \\mathcal{L}}{\\partial x_2} = e^{x_2} - \\mu = 0 \\implies e^{x_2} = \\mu \\implies x_2 = \\ln \\mu$$
For a real solution to exist, we must have $\\mu > 0$.<br>
Substitute $x_1 = \\ln \\mu$ and $x_2 = \\ln \\mu$ into the Lagrangian:
$$\\psi(\\mu) = \\mathcal{L}(x(\\mu), \\mu) = e^{\\ln \\mu} + e^{\\ln \\mu} + \\mu (2 - \\ln \\mu - \\ln \\mu) = 2\\mu + \\mu (2 - 2\\ln \\mu)$$
$$<span class="ans">\\psi(\\mu) = 4\\mu - 2\\mu \\ln \\mu</span>$$
The 1D Wolfe dual problem is:
$$\\max_{\\mu > 0} (4\\mu - 2\\mu \\ln \\mu)$$</p>

<p><span class="part">Part (c): Optimal Solution & Strong Duality</span><br>
Differentiating $\\psi(\\mu)$:
$$\\psi'(\\mu) = 4 - 2(\\ln \\mu + 1) = 2 - 2\\ln \\mu = 0 \\implies \\ln \\mu = 1 \\implies <span class="ans">\\mu^* = e</span>$$
Check concavity: $\\psi''(\\mu) = -2/\\mu < 0$ for all $\\mu > 0$ (strictly concave).<br>
Optimal dual objective:
$$d^* = \\psi(e) = 4e - 2e \\ln e = 4e - 2e = <span class="ans">2e</span>$$
Reconstruct primal variables:
$$x_1^* = \\ln \\mu^* = \\ln e = 1, \\quad x_2^* = \\ln \\mu^* = \\ln e = 1$$
Primal objective value:
$$p^* = f(1, 1) = e^1 + e^1 = <span class="ans">2e</span>$$
<span class="ans">Strong duality holds exactly: $p^* = d^* = 2e$.</span></p>""",
        "takeaway": "Wolfe duality embeds the first-order stationarity condition directly as an explicit equality constraint, transforming an unconstrained infimum into an algebraic substitution."
    },
    {
        "id": 11792,
        "subject": "CMO",
        "topicId": "17_Wolfe_Duality",
        "topicTitle": "17 · Wolfe Duality",
        "title": "SVM Wolfe Dual & Kernel Trick (Stanford Boyd)",
        "kind2": "pyq",
        "source": "Stanford EE364a / Boyd Ch 8",
        "marks": "[10 Marks]",
        "question": """<p>Consider the hard-margin Support Vector Machine (SVM) training problem:
$$\\min_{w \\in \\mathbb{R}^d, \\; b \\in \\mathbb{R}} \\frac{1}{2} \\|w\\|_2^2 \\quad \\text{subject to} \\quad y_i (w^\\top x_i + b) \\ge 1 \\quad (i = 1, \\dots, N)$$
where $x_i \\in \\mathbb{R}^d$ are training vectors and $y_i \\in \\{-1, +1\\}$ are class labels.<br>
<span class="part">(a)</span> Set up the Lagrangian with multipliers $\\alpha_i \\ge 0$.<br>
<span class="part">(b)</span> Derive the stationarity conditions with respect to $w$ and $b$.<br>
<span class="part">(c)</span> Derive the classic <strong>SVM Wolfe Dual Problem</strong> and explain how it enables the <strong>Kernel Trick</strong>.</p>""",
        "solution": """<p><span class="part">Part (a): Lagrangian Setup</span><br>
Writing constraints as $1 - y_i(w^\\top x_i + b) \\le 0$:
$$\\mathcal{L}(w, b, \\alpha) = \\frac{1}{2} \\|w\\|_2^2 + \\sum_{i=1}^N \\alpha_i \\left( 1 - y_i (w^\\top x_i + b) \\right)$$</p>

<p><span class="part">Part (b): Stationarity Conditions</span><br>
<ol>
  <li>With respect to $w$:
  $$\\nabla_w \\mathcal{L} = w - \\sum_{i=1}^N \\alpha_i y_i x_i = 0 \\implies <span class="ans">w = \\sum_{i=1}^N \\alpha_i y_i x_i</span>$$</li>
  <li>With respect to $b$:
  $$\\frac{\\partial \\mathcal{L}}{\\partial b} = -\\sum_{i=1}^N \\alpha_i y_i = 0 \\implies <span class="ans">\\sum_{i=1}^N \\alpha_i y_i = 0</span>$$</li>
</ol></p>

<p><span class="part">Part (c): Wolfe Dual & The Kernel Trick</span><br>
Substitute $w = \\sum_{i=1}^N \\alpha_i y_i x_i$ into $\\mathcal{L}$:
$$\\frac{1}{2} \\|w\\|^2 = \\frac{1}{2} \\sum_{i=1}^N \\sum_{j=1}^N \\alpha_i \\alpha_j y_i y_j (x_i^\\top x_j)$$
$$-\\sum_{i=1}^N \\alpha_i y_i (w^\\top x_i) = -\\sum_{i=1}^N \\sum_{j=1}^N \\alpha_i \\alpha_j y_i y_j (x_i^\\top x_j)$$
$$-b \\sum_{i=1}^N \\alpha_i y_i = 0 \\quad (\\text{vanishes identically!})$$
Combining terms:
$$<span class="ans">\\max_{\\alpha} \\sum_{i=1}^N \\alpha_i - \\frac{1}{2} \\sum_{i=1}^N \\sum_{j=1}^N \\alpha_i \\alpha_j y_i y_j (x_i^\\top x_j) \\quad \\text{s.t.} \\quad \\sum_{i=1}^N \\alpha_i y_i = 0, \\; \\alpha_i \\ge 0</span>$$
<strong>The Kernel Trick:</strong> The training data appears EXCLUSIVELY through pairwise inner products $x_i^\\top x_j$. By replacing $x_i^\\top x_j$ with a positive definite kernel function $K(x_i, x_j) = \\phi(x_i)^\\top \\phi(x_j)$ (such as an RBF Gaussian kernel), SVM learns non-linear decision boundaries in infinite-dimensional Hilbert spaces with zero extra computational complexity!</p>""",
        "takeaway": "Wolfe duality turns the $d$-dimensional primal SVM into an $N$-dimensional dual quadratic program where data appears exclusively through dot products, unlocking the Kernel Trick."
    },
    {
        "id": 11793,
        "subject": "CMO",
        "topicId": "17_Wolfe_Duality",
        "topicTitle": "17 · Wolfe Duality",
        "title": "Wolfe vs Lagrange Duality & Non-Convex Pitfalls (Generated Exam)",
        "kind2": "practice",
        "source": "IISc / Bertsekas Benchmark",
        "marks": "[10 Marks]",
        "question": """<p>Let $f: \\mathbb{R}^n \\to \\mathbb{R}$ be continuously differentiable and let $g_j(x) \\le 0$ ($j = 1, \\dots, m$) be convex constraints.<br>
<span class="part">(a)</span> Prove that if $f$ is convex, the Wolfe dual problem:
$$\\max_{x, \\mu} \\mathcal{L}(x, \\mu) \\quad \\text{subject to} \\quad \\nabla_x \\mathcal{L}(x, \\mu) = 0, \\quad \\mu \\ge 0$$
is mathematically equivalent to the standard Lagrange dual problem $\\max_{\\mu \\ge 0} \\inf_x \\mathcal{L}(x, \\mu)$.<br>
<span class="part">(b)</span> Explain what goes catastrophically wrong with Wolfe duality when $f$ is non-convex by constructing an explicit 1D counterexample.</p>""",
        "solution": """<p><span class="part">Part (a): Equivalence Proof for Convex $f$</span><br>
In standard Lagrangian duality:
$$g(\\mu) = \\inf_{x \\in \\mathbb{R}^n} \\mathcal{L}(x, \\mu)$$
When $f$ is convex and $g_j$ are convex, for any fixed $\\mu \\ge 0$, the Lagrangian $\\mathcal{L}(x, \\mu) = f(x) + \\sum \\mu_j g_j(x)$ is a convex differentiable function of $x$.<br>
For a convex differentiable function on an open domain, the unconstrained infimum is attained if and only if the gradient vanishes:
$$\\inf_x \\mathcal{L}(x, \\mu) = \\mathcal{L}(\\hat{x}, \\mu) \\iff \\nabla_x \\mathcal{L}(\\hat{x}, \\mu) = 0$$
Thus, searching over all pairs $(x, \\mu)$ satisfying $\\nabla_x \\mathcal{L}(x, \\mu) = 0$ is exactly equivalent to evaluating $\\inf_x \\mathcal{L}(x, \\mu)$.<br>
<span class="ans">The Wolfe dual is identical to the Lagrange dual for convex problems.</span> $\\blacksquare$</p>

<p><span class="part">Part (b): Non-Convex Pathology</span><br>
When $f$ is non-convex, $\\nabla_x \\mathcal{L}(x, \\mu) = 0$ identifies local minima, saddle points, AND <strong>local maxima</strong> of the Lagrangian!<br>
<strong>Concrete Counterexample:</strong><br>
Consider $\\min f(x) = -x^2$ subject to $x \\le 1$ on the interval $[-2, 2]$.<br>
Primal minimum is $x^* = \\pm 2$ with $f = -4$.<br>
Lagrangian: $\\mathcal{L}(x, \\mu) = -x^2 + \\mu(x - 1)$.<br>
Stationarity condition:
$$\\nabla_x \\mathcal{L} = -2x + \\mu = 0 \\implies x = \\frac{\\mu}{2}$$
Notice that $x = \\mu/2$ is a local MAXIMUM of $\\mathcal{L}$ with respect to $x$ (since $\\nabla_{xx}^2 \\mathcal{L} = -2 < 0$)!<br>
Substitute $x = \\mu/2$ into the Wolfe objective:
$$\\mathcal{L}(\\mu/2, \\mu) = -\\left(\\frac{\\mu}{2}\\right)^2 + \\mu \\left( \\frac{\\mu}{2} - 1 \\right) = -\\frac{\\mu^2}{4} + \\frac{\\mu^2}{2} - \\mu = \\frac{\\mu^2}{4} - \\mu$$
Now the Wolfe dual maximizes this with respect to $\\mu \\ge 0$:
$$\\max_{\\mu \\ge 0} \\left( \\frac{\\mu^2}{4} - \\mu \\right) = +\\infty!$$
<span class="ans">The Wolfe dual is unbounded ($+\\infty$), while the primal has a finite minimum ($-4$)!</span><br>
Weak duality fails completely because the stationary point was a maximum, not an infimum.</p>""",
        "takeaway": "Wolfe duality is strictly invalid for non-convex problems because $\\nabla_x \\mathcal{L} = 0$ can capture local maxima or saddles, causing the dual to explode to $+\\infty$."
    },

    # =========================================================================
    # TOPIC 18: Linear Programming Duality & Polyhedral Geometry
    # =========================================================================
    {
        "id": 11891,
        "subject": "CMO",
        "topicId": "18_Linear_Programming_Duality_and_Polyhedral_Geometry",
        "topicTitle": "18 · LP Duality & Polyhedral Geometry",
        "title": "LP Dual & Complementary Slackness (IISc Endsem 2024)",
        "kind2": "pyq",
        "source": "IISc Endsem 2024 / Luenberger Ch 4",
        "marks": "[10 Marks]",
        "question": """<p>Consider the Linear Program:
$$\\max 3x_1 + 2x_2 \\quad \\text{subject to} \\quad 2x_1 + x_2 \\le 4, \\quad 2x_1 + 3x_2 \\le 6, \\quad x_1 \\ge 0, \\quad x_2 \\ge 0$$
<span class="part">(a)</span> Formulate the dual linear program.<br>
<span class="part">(b)</span> Solve the primal LP graphically to identify the optimal vertex $x^*$.<br>
<span class="part">(c)</span> Use the <strong>Complementary Slackness Theorem</strong> to determine the exact optimal dual multipliers $y^*$, and verify that the primal and dual optimal values match.</p>""",
        "solution": """<p><span class="part">Part (a): Dual Linear Program</span><br>
Primal in matrix form: $\\max c^\\top x$ s.t. $A x \\le b, x \\ge 0$, where:
$$c = \\begin{bmatrix} 3 \\\\ 2 \\end{bmatrix}, \\quad A = \\begin{bmatrix} 2 & 1 \\\\ 2 & 3 \\end{bmatrix}, \\quad b = \\begin{bmatrix} 4 \\\\ 6 \\end{bmatrix}$$
The dual LP is $\\min b^\\top y$ s.t. $A^\\top y \\ge c, y \\ge 0$:
$$<span class="ans">\\min 4y_1 + 6y_2 \\quad \\text{subject to} \\quad 2y_1 + 2y_2 \\ge 3, \\quad y_1 + 3y_2 \\ge 2, \\quad y_1 \\ge 0, \\; y_2 \\ge 0</span>$$</p>

<p><span class="part">Part (b): Primal Graphical Solution</span><br>
Evaluate all boundary corner vertices of the feasible polygon:
<ul>
  <li>$(0, 0)^\\top \\implies 3(0) + 2(0) = 0$.</li>
  <li>$(2, 0)^\\top \\implies 3(2) + 2(0) = 6$.</li>
  <li>$(0, 2)^\\top \\implies 3(0) + 2(2) = 4$.</li>
  <li>Intersection of lines $2x_1 + x_2 = 4$ and $2x_1 + 3x_2 = 6$:<br>
  Subtracting equations: $2x_2 = 2 \\implies x_2 = 1$.<br>
  $2x_1 + 1 = 4 \\implies 2x_1 = 3 \\implies x_1 = 1.5$.<br>
  Vertex: <span class="ans">$x^* = (1.5, 1)^\\top$</span>.<br>
  Objective value: $3(1.5) + 2(1) = 4.5 + 2 = <span class="ans">6.5</span>$.</li>
</ul>
The optimal primal solution is $x^* = (1.5, 1)^\\top$ with $p^* = 6.5$.</p>

<p><span class="part">Part (c): Complementary Slackness for Dual Variables</span><br>
By the Complementary Slackness Theorem:
$$x_j^* > 0 \\implies (A^\\top y^*)_j = c_j$$
Since $x_1^* = 1.5 > 0$ and $x_2^* = 1 > 0$, both dual constraints must hold as <strong>exact equalities</strong>:
$$2y_1 + 2y_2 = 3$$
$$y_1 + 3y_2 = 2$$
Multiply the second equation by 2:
$$2y_1 + 6y_2 = 4$$
Subtract the first equation:
$$4y_2 = 1 \\implies <span class="ans">y_2^* = 1/4 = 0.25</span>$$
Substitute into $2y_1 + 2(0.25) = 3 \\implies 2y_1 = 2.5 \\implies <span class="ans">y_1^* = 5/4 = 1.25</span>$.<br>
Evaluate dual objective value:
$$d^* = 4(1.25) + 6(0.25) = 5 + 1.5 = <span class="ans">6.5</span>$$
<span class="ans">Primal value $p^* = 6.5 = d^*$ dual value! Strong duality confirmed.</span></p>""",
        "takeaway": "Complementary slackness turns dual optimization into solving a square linear system: positive primal variables turn dual inequalities into active linear equations."
    },
    {
        "id": 11892,
        "subject": "CMO",
        "topicId": "18_Linear_Programming_Duality_and_Polyhedral_Geometry",
        "topicTitle": "18 · LP Duality & Polyhedral Geometry",
        "title": "Complementary Slackness Theorem for LP (Stanford Boyd)",
        "kind2": "pyq",
        "source": "Stanford EE364a / Boyd Ch 5",
        "marks": "[8 Marks]",
        "question": """<p>Consider the primal LP in standard form:
$$\\min c^\\top x \\quad \\text{subject to} \\quad A x = b, \\quad x \\ge 0$$
and its dual:
$$\\max b^\\top y \\quad \\text{subject to} \\quad A^\\top y \\le c$$
Prove the <strong>Complementary Slackness Theorem</strong>: feasible vectors $x$ and $y$ are simultaneously optimal if and only if:
$$x_j (c_j - A_{\\cdot j}^\\top y) = 0 \\quad \\forall j = 1, \\dots, n$$</p>""",
        "solution": """<p><span class="part">Step 1: Express the Duality Gap</span><br>
Let $x$ be primal feasible ($Ax = b, x \\ge 0$) and $y$ be dual feasible ($A^\\top y \\le c$).<br>
Compute the duality gap between primal and dual objective values:
$$c^\\top x - b^\\top y = c^\\top x - (A x)^\\top y$$
Using the transpose identity $(Ax)^\\top y = x^\\top A^\\top y$:
$$c^\\top x - b^\\top y = c^\\top x - x^\\top (A^\\top y) = x^\\top (c - A^\\top y) = \\sum_{j=1}^n x_j (c - A^\\top y)_j$$</p>

<p><span class="part">Step 2: Sign of Individual Terms</span><br>
Notice that:
<ol>
  <li>Primal feasibility requires $x_j \\ge 0$ for all $j = 1, \\dots, n$.</li>
  <li>Dual feasibility requires $A^\\top y \\le c \\implies (c - A^\\top y)_j \\ge 0$ for all $j = 1, \\dots, n$.</li>
</ol>
The product of two non-negative numbers is always non-negative:
$$x_j (c - A^\\top y)_j \\ge 0 \\quad \\forall j = 1, \\dots, n$$
Therefore, the duality gap is a sum of non-negative terms:
$$c^\\top x - b^\\top y = \\sum_{j=1}^n x_j (c - A^\\top y)_j \\ge 0$$</p>

<p><span class="part">Step 3: Condition for Zero Duality Gap</span><br>
By the Strong Duality Theorem of Linear Programming, feasible $x$ and $y$ are optimal if and only if the duality gap is zero:
$$c^\\top x - b^\\top y = 0$$
A sum of non-negative real numbers is equal to zero if and only if EVERY individual term in the summation is zero:
$$\\sum_{j=1}^n x_j (c - A^\\top y)_j = 0 \\iff <span class="ans">x_j (c_j - A_{\\cdot j}^\\top y) = 0 \\quad \\forall j = 1, \\dots, n</span>$$
<span class="ans">This completes the proof.</span> $\\blacksquare$</p>""",
        "takeaway": "Complementary slackness in LP means: if a primal variable is positive ($x_j > 0$), the corresponding dual constraint must be tight ($A_{\\cdot j}^\\top y = c_j$). If a dual constraint is loose ($A_{\\cdot j}^\\top y < c_j$), the primal variable must be zero ($x_j = 0$)."
    },
    {
        "id": 11893,
        "subject": "CMO",
        "topicId": "18_Linear_Programming_Duality_and_Polyhedral_Geometry",
        "topicTitle": "18 · LP Duality & Polyhedral Geometry",
        "title": "Basic Feasible Solutions & Extreme Points (Generated Exam)",
        "kind2": "practice",
        "source": "IISc / Bertsekas Benchmark",
        "marks": "[10 Marks]",
        "question": """<p>Consider the polyhedron in standard form:
$$P = \\{x \\in \\mathbb{R}^n : A x = b, \\quad x \\ge 0\\}$$
where $A \\in \\mathbb{R}^{m \\times n}$ has full row rank $m$.<br>
<span class="part">(a)</span> State the algebraic definition of a <strong>Basic Feasible Solution (BFS)</strong>.<br>
<span class="part">(b)</span> Prove that $x$ is a BFS if and only if the set of columns $\\{A_{\\cdot j} : x_j > 0\\}$ is <strong>linearly independent</strong>.<br>
<span class="part">(c)</span> Prove that every BFS corresponds geometrically to an <strong>extreme point (vertex)</strong> of $P$.</p>""",
        "solution": """<p><span class="part">Part (a): Algebraic Definition of a BFS</span><br>
A vector $x \\in \\mathbb{R}^n$ is a Basic Feasible Solution (BFS) if $x \\in P$ and there exists an index subset $B \\subset \\{1, \\dots, n\\}$ of size $|B| = m$ such that:
<ol>
  <li>The basis submatrix $A_B \\in \\mathbb{R}^{m \\times m}$ is non-singular (invertible).</li>
  <li>All non-basic variables are zero: $x_N = 0$ for all $j \\notin B$.</li>
  <li>The basic variables satisfy $x_B = A_B^{-1} b \\ge 0$.</li>
</ol></p>

<p><span class="part">Part (b): Column Independence Characterization</span><br>
Let $J = \\{j : x_j > 0\\}$ be the support of $x$.<br>
$(\\implies)$ If $x$ is a BFS, $J \\subseteq B$. Since $A_B$ is invertible, its columns are linearly independent. Any subset of linearly independent columns is linearly independent, so $\\{A_{\\cdot j} : j \\in J\\}$ is linearly independent.<br>
$(\\impliedby)$ If $\\{A_{\\cdot j} : j \\in J\\}$ is linearly independent, since $|J| \\le m$ and $\\operatorname{rank}(A) = m$, by the Steinitz exchange lemma we can extend $J$ to a set of $m$ linearly independent columns $B$. Setting $x_N = 0$ for $j \\notin B$ reproduces the BFS structure.</p>

<p><span class="part">Part (c): Equivalence with Geometric Extreme Points</span><br>
An extreme point of $P$ is a point that cannot be written as a strict convex combination $x = \\frac{1}{2} u + \\frac{1}{2} v$ of two distinct points $u, v \\in P$ ($u \\ne v$).<br>
$(\\implies)$ Assume $x$ is a BFS. Suppose $x = \\frac{1}{2} u + \\frac{1}{2} v$ for $u, v \\in P$.<br>
For any non-basic index $j \\notin B$, $x_j = 0$.<br>
Since $u_j \\ge 0$ and $v_j \\ge 0$:
$$\\frac{1}{2} u_j + \\frac{1}{2} v_j = 0 \\implies u_j = 0 \\text{ and } v_j = 0 \\quad \\forall j \\notin B$$
Both $u$ and $v$ have zeros on all non-basic coordinates.<br>
Now evaluate $Au = b$ and $Av = b$:
$$A_B u_B = b \\implies u_B = A_B^{-1} b = x_B$$
$$A_B v_B = b \\implies v_B = A_B^{-1} b = x_B$$
Thus $u = v = x$. <span class="ans">$x$ cannot be decomposed into distinct points; it is an extreme point!</span><br>
$(\\impliedby)$ If $x$ were not a BFS, columns $\\{A_{\\cdot j} : j \\in J\\}$ would be linearly dependent, allowing constructing a non-zero perturbation vector $d$ such that $x \\pm \\epsilon d \\in P$, proving $x$ is not an extreme point. $\\blacksquare$</p>""",
        "takeaway": "The fundamental theorem of LP states that optimal solutions always occur at extreme points (vertices), which algebraically correspond to Basic Feasible Solutions."
    },

    # =========================================================================
    # TOPIC 19: Penalty and Barrier Methods
    # =========================================================================
    {
        "id": 11991,
        "subject": "CMO",
        "topicId": "19_Penalty_and_Barrier_Methods",
        "topicTitle": "19 · Penalty & Barrier Methods",
        "title": "Quadratic Penalty Convergence & Multipliers (IISc Endsem 2024)",
        "kind2": "pyq",
        "source": "IISc Endsem 2024 / Nocedal & Wright Ch 17",
        "marks": "[10 Marks]",
        "question": """<p>Consider the equality constrained problem:
$$\\min_{x_1, x_2} f(x) = \\frac{1}{2}(x_1^2 + x_2^2) \\quad \\text{subject to} \\quad h(x) = x_1 + x_2 - 2 = 0$$
<span class="part">(a)</span> Formulate the quadratic penalty function $Q(x; \\rho)$ for penalty parameter $\\rho > 0$.<br>
<span class="part">(b)</span> Find the exact analytic unconstrained minimizer $x^*(\\rho)$.<br>
<span class="part">(c)</span> Compute the Lagrange multiplier estimate $\\lambda(\\rho) = \\rho h(x^*(\\rho))$ and evaluate the limits of $x^*(\\rho)$ and $\\lambda(\\rho)$ as $\\rho \\to \\infty$.</p>""",
        "solution": """<p><span class="part">Part (a): Quadratic Penalty Formulation</span><br>
$$<span class="ans">Q(x; \\rho) = \\frac{1}{2}(x_1^2 + x_2^2) + \\frac{\\rho}{2}(x_1 + x_2 - 2)^2</span>$$</p>

<p><span class="part">Part (b): Exact Minimizer $x^*(\\rho)$</span><br>
Take partial derivatives and set to zero:
$$\\frac{\\partial Q}{\\partial x_1} = x_1 + \\rho(x_1 + x_2 - 2) = 0$$
$$\\frac{\\partial Q}{\\partial x_2} = x_2 + \\rho(x_1 + x_2 - 2) = 0$$
By symmetry, $x_1 = x_2$. Substitute $x_2 = x_1$:
$$x_1 + \\rho(2x_1 - 2) = 0 \\implies x_1(1 + 2\\rho) = 2\\rho \\implies <span class="ans">x_1^*(\\rho) = x_2^*(\\rho) = \\frac{2\\rho}{1 + 2\\rho}</span>$$</p>

<p><span class="part">Part (c): Multiplier Estimate and Asymptotic Limits</span><br>
Evaluate the constraint violation:
$$h(x^*(\\rho)) = x_1^* + x_2^* - 2 = 2\\left(\\frac{2\\rho}{1 + 2\\rho}\\right) - 2 = \\frac{4\\rho - 2(1 + 2\\rho)}{1 + 2\\rho} = <span class="ans">-\\frac{2}{1 + 2\\rho}</span>$$
The penalty multiplier estimate is:
$$\\lambda(\\rho) = -\\rho h(x^*(\\rho)) = -\\rho \\left(-\\frac{2}{1 + 2\\rho}\\right) = \\frac{2\\rho}{1 + 2\\rho}$$
(or in KKT convention $\\nabla f + \\lambda \\nabla h = 0$: $\\lambda = -\\frac{2\\rho}{1 + 2\\rho}$).<br>
Evaluate limits as $\\rho \\to \\infty$:
$$\\lim_{\\rho \\to \\infty} x_1^*(\\rho) = \\lim_{\\rho \\to \\infty} \\frac{2\\rho}{1 + 2\\rho} = 1, \\quad \\lim_{\\rho \\to \\infty} x_2^*(\\rho) = 1$$
$$\\lim_{\\rho \\to \\infty} \\lambda(\\rho) = \\lim_{\\rho \\to \\infty} -\\frac{2\\rho}{1 + 2\\rho} = -1$$
Check true KKT: $\\nabla f(1, 1) = \\begin{bmatrix} 1 \\\\ 1 \\end{bmatrix}$, $\\nabla h(1, 1) = \\begin{bmatrix} 1 \\\\ 1 \\end{bmatrix}$.<br>
$$\\begin{bmatrix} 1 \\\\ 1 \\end{bmatrix} + (-1) \\begin{bmatrix} 1 \\\\ 1 \\end{bmatrix} = 0$$
<span class="ans">The penalty path converges exactly to the true minimizer $x^* = (1, 1)^\\top$ and true KKT multiplier $\\lambda^* = -1$.</span></p>""",
        "takeaway": "As $\\rho \\to \\infty$, the penalty minimizers approach the feasible boundary from the exterior, while the product $\\rho h(x)$ converges directly to the true Lagrange multiplier."
    },
    {
        "id": 11992,
        "subject": "CMO",
        "topicId": "19_Penalty_and_Barrier_Methods",
        "topicTitle": "19 · Penalty & Barrier Methods",
        "title": "Log-Barrier Central Path Duality (Stanford Boyd)",
        "kind2": "pyq",
        "source": "Stanford EE364a / Boyd Ch 11",
        "marks": "[10 Marks]",
        "question": """<p>Consider the inequality-constrained convex problem $\\min f(x)$ subject to $g_j(x) \\le 0$ ($j = 1, \\dots, m$).<br>
Define the Logarithmic Barrier function for barrier parameter $\\mu > 0$:
$$B(x; \\mu) = f(x) - \\mu \\sum_{j=1}^m \\log(-g_j(x))$$
<span class="part">(a)</span> Compute the stationarity condition for the central path minimizer $x^*(\\mu)$.<br>
<span class="part">(b)</span> Define dual variables $\\lambda_j^*(\\mu) = -\\frac{\\mu}{g_j(x^*(\\mu))}$ and prove that $\\lambda^*(\\mu)$ is strictly dual feasible.<br>
<span class="part">(c)</span> Prove that the duality gap at the central path point satisfies:
$$f(x^*(\\mu)) - p^* \\le m \\mu$$
and explain how this dictates the stopping criterion in Interior-Point Methods.</p>""",
        "solution": """<p><span class="part">Part (a): Central Path Stationarity</span><br>
Differentiating $B(x; \\mu)$ with respect to $x$:
$$\\nabla B(x; \\mu) = \\nabla f(x) - \\mu \\sum_{j=1}^m \\frac{1}{-g_j(x)} (-\\nabla g_j(x)) = \\nabla f(x) - \\mu \\sum_{j=1}^m \\frac{1}{g_j(x)} \\nabla g_j(x) = 0$$
$$<span class="ans">\\nabla f(x^*(\\mu)) + \\sum_{j=1}^m \\left( -\\frac{\\mu}{g_j(x^*(\\mu))} \\right) \\nabla g_j(x^*(\\mu)) = 0</span>$$</p>

<p><span class="part">Part (b): Dual Feasibility Proof</span><br>
Define $\\lambda_j^*(\\mu) = -\\frac{\\mu}{g_j(x^*(\\mu))} = \\frac{\\mu}{-g_j(x^*(\\mu))}$.
<ul>
  <li>Since $x^*(\\mu)$ is in the strictly feasible interior, $g_j(x^*(\\mu)) < 0 \\implies -g_j(x^*(\\mu)) > 0$.</li>
  <li>Since $\\mu > 0$, the ratio $\\frac{\\mu}{-g_j(x^*(\\mu))} > 0$ strictly.</li>
</ul>
<span class="ans">Thus $\\lambda^*(\\mu) > 0$ is strictly dual feasible!</span><br>
Moreover, stationarity matches the Lagrangian gradient:
$$\\nabla_x \\mathcal{L}(x^*(\\mu), \\lambda^*(\\mu)) = \\nabla f(x^*(\\mu)) + \\sum_{j=1}^m \\lambda_j^*(\\mu) \\nabla g_j(x^*(\\mu)) = 0$$</p>

<p><span class="part">Part (c): Duality Gap & Interior-Point Stopping</span><br>
By convexity, $x^*(\\mu)$ minimizes the Lagrangian $\\mathcal{L}(x, \\lambda^*(\\mu))$.<br>
Evaluate the dual function:
$$g(\\lambda^*(\\mu)) = \\mathcal{L}(x^*(\\mu), \\lambda^*(\\mu)) = f(x^*(\\mu)) + \\sum_{j=1}^m \\lambda_j^*(\\mu) g_j(x^*(\\mu))$$
Substitute $\\lambda_j^*(\\mu) = -\\mu / g_j(x^*(\\mu))$:
$$\\sum_{j=1}^m \\lambda_j^*(\\mu) g_j(x^*(\\mu)) = \\sum_{j=1}^m \\left( -\\frac{\\mu}{g_j(x^*(\\mu))} \\right) g_j(x^*(\\mu)) = \\sum_{j=1}^m (-\\mu) = -m \\mu$$
Thus:
$$g(\\lambda^*(\\mu)) = f(x^*(\\mu)) - m \\mu$$
By weak duality, $g(\\lambda^*) \\le p^*$:
$$f(x^*(\\mu)) - m \\mu \\le p^* \\implies <span class="ans">f(x^*(\\mu)) - p^* \\le m \\mu</span>$$
<strong>Interior-Point Stopping Criterion:</strong> To achieve an $\\epsilon$-optimal solution $f(x) - p^* \\le \\epsilon$, the algorithm simply decreases $\\mu$ until $\\mu \\le \\frac{\\epsilon}{m}$.</p>""",
        "takeaway": "Each point on the central path provides an exact certificate of suboptimality: the duality gap is precisely $m\\mu$, allowing interior-point methods to terminate with rigorous accuracy."
    },
    {
        "id": 11993,
        "subject": "CMO",
        "topicId": "19_Penalty_and_Barrier_Methods",
        "topicTitle": "19 · Penalty & Barrier Methods",
        "title": "Penalty Ill-Conditioning vs Augmented Lagrangian (Generated Exam)",
        "kind2": "practice",
        "source": "IISc / Bertsekas Benchmark",
        "marks": "[10 Marks]",
        "question": """<p>Consider minimizing $f(x)$ subject to equality constraint $h(x) = 0$.<br>
<span class="part">(a)</span> Write down the Hessian of the Quadratic Penalty function $Q(x; \\rho) = f(x) + \\frac{\\rho}{2} h(x)^2$.<br>
<span class="part">(b)</span> Prove that as $\\rho \\to \\infty$, the condition number $\\kappa(\\nabla^2 Q(x; \\rho)) \\to \\infty$ grows as $\\mathcal{O}(\\rho)$, causing severe numerical breakdown.<br>
<span class="part">(c)</span> State the <strong>Augmented Lagrangian</strong> function $\\mathcal{L}_A(x, \\lambda; \\rho)$ and explain how it solves this problem without requiring $\\rho \\to \\infty$.</p>""",
        "solution": """<p><span class="part">Part (a): Penalty Hessian</span><br>
Gradient: $\\nabla Q(x; \\rho) = \\nabla f(x) + \\rho h(x) \\nabla h(x)$.<br>
Hessian:
$$<span class="ans">\\nabla^2 Q(x; \\rho) = \\nabla^2 f(x) + \\rho \\nabla h(x) \\nabla h(x)^\\top + \\rho h(x) \\nabla^2 h(x)</span>$$</p>

<p><span class="part">Part (b): Ill-Conditioning Proof</span><br>
At the minimizer $x^*(\\rho)$, as $\\rho \\to \\infty$, $\\rho h(x^*(\\rho)) \\to \\lambda^*$.
$$\\nabla^2 Q(x^*(\\rho); \\rho) \\approx \\nabla_{xx}^2 \\mathcal{L}(x^*, \\lambda^*) + \\rho \\nabla h(x^*) \\nabla h(x^*)^\\top$$
Let $w$ be any tangent vector ($\\|w\\| = 1$) along the constraint manifold: $\\nabla h(x^*)^\\top w = 0$.
$$w^\\top \\nabla^2 Q w = w^\\top \\nabla_{xx}^2 \\mathcal{L} w + \\rho (0) = w^\\top \\nabla_{xx}^2 \\mathcal{L} w = \\mathcal{O}(1)$$
Now let $v = \\frac{\\nabla h(x^*)}{\\|\\nabla h(x^*)\\|}$ be the unit normal vector perpendicular to the constraint:
$$v^\\top \\nabla^2 Q v = v^\\top \\nabla_{xx}^2 \\mathcal{L} v + \\rho \\|\\nabla h(x^*)\\|^2 = \\mathcal{O}(\\rho)$$
Therefore, the Hessian possesses eigenvalues of order $\\mathcal{O}(1)$ along tangent directions, and eigenvalues of order $\\mathcal{O}(\\rho)$ along normal directions.<br>
Condition number:
$$<span class="ans">\\kappa(\\nabla^2 Q) = \\frac{\\lambda_{\\max}}{\\lambda_{\\min}} \\approx \\frac{\\mathcal{O}(\\rho)}{\\mathcal{O}(1)} = \\mathcal{O}(\\rho) \\to \\infty</span>$$
For $\\rho = 10^8$, $\\kappa \\approx 10^8$, causing double-precision truncation errors and catastrophic solver breakdown!</p>

<p><span class="part">Part (c): Augmented Lagrangian Resolution</span><br>
The Augmented Lagrangian (Method of Multipliers) adds an explicit Lagrange multiplier term:
$$<span class="ans">\\mathcal{L}_A(x, \\lambda; \\rho) = f(x) + \\lambda^\\top h(x) + \\frac{\\rho}{2} \\|h(x)\\|^2</span>$$
Multiplier update:
$$\\lambda_{k+1} = \\lambda_k + \\rho h(x_k)$$
<strong>Resolution:</strong> Because $\\lambda_k$ converges to the exact true multiplier $\\lambda^*$, the exact constrained minimum $x^*$ is a strict unconstrained local minimizer of $\\mathcal{L}_A(x, \\lambda^*; \\rho)$ for a <span class="ans">FINITE, MODEST $\\rho > \\rho^*$</span>! We NEVER need $\\rho \\to \\infty$, keeping $\\kappa(\\nabla^2 \\mathcal{L}_A)$ perfectly bounded and well-conditioned.</p>""",
        "takeaway": "Quadratic penalty fails numerically because forcing feasibility requires $\\rho \\to \\infty$, which explodes the condition number. Augmented Lagrangian shifts the burden to the multiplier $\\lambda_k$, converging for finite $\\rho$."
    }
]

def main():
    target_file = os.path.join(os.path.dirname(__file__), "..", "practice_cmo.js")
    target_file = os.path.abspath(target_file)
    
    with open(target_file, "r", encoding="utf-8") as f:
        txt = f.read()
    
    pfx = "window.PRACTICE_DATA.push(\n"
    start = txt.find(pfx)
    end = txt.rfind("\n);")
    cards = json.loads(txt[start+len(pfx):end])
    
    new_ids = {c["id"] for c in NEW_CARDS}
    existing = [c for c in cards if c["id"] not in new_ids]
    combined = existing + NEW_CARDS
    
    js_content = "/* Practice Questions Database for CMO (Topics 01-19) */\n"
    js_content += "window.PRACTICE_DATA = window.PRACTICE_DATA || [];\n\n"
    js_content += "window.PRACTICE_DATA.push(\n"
    js_content += json.dumps(combined, indent=2)
    js_content += "\n);\n"
    
    with open(target_file, "w", encoding="utf-8") as f:
        f.write(js_content)
        
    print(f"Successfully updated {target_file}! Total practice cards: {len(combined)}")

if __name__ == "__main__":
    main()
