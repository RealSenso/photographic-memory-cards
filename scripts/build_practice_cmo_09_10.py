#!/usr/bin/env python3
"""
build_practice_cmo_09_10.py
Appends practice questions (flippable cards) for CMO Topics 09 & 10 to practice_cmo.js.
  Topic 09: Geometry of Constrained Optimization, Tangent Cone and LICQ
  Topic 10: Separating Hyperplanes and Farkas' Lemma
"""

import json
import os

NEW_CARDS = [
    # =========================================================================
    # TOPIC 09: Geometry of Constrained Optimization, Tangent Cone and LICQ
    # =========================================================================
    {
        "id": 10991,
        "subject": "CMO",
        "topicId": "09_Geometry_of_Constrained_Optimization_Tangent_Cone_and_LICQ",
        "topicTitle": "09 · Constrained Geometry, Tangent Cone & LICQ",
        "title": "Tangent Cone vs Linearized Cone & LICQ (IISc Midterm 2024)",
        "kind2": "pyq",
        "source": "IISc Midterm 3 2024 / Nocedal & Wright Ch 12",
        "marks": "[10 Marks]",
        "question": """<p>Consider the constraint region in $\\mathbb{R}^2$:
$$\\Omega = \\{(x_1, x_2) \\in \\mathbb{R}^2 : (1 - x_1)^3 - x_2 \\ge 0, \\quad x_2 \\ge 0\\}$$
At the feasible boundary point $x^* = (1, 0)^\\top$:<br>
<span class="part">(a)</span> Express the constraints in standard form $g_i(x) \\le 0$ and determine the active constraint set $\\mathcal{A}(x^*)$.<br>
<span class="part">(b)</span> Compute the constraint gradients at $x^*$ and test whether the Linear Independence Constraint Qualification (LICQ) holds.<br>
<span class="part">(c)</span> Compute the linearized cone $T_{\\text{lin}}(x^*)$ and the geometric tangent cone $T_\\Omega(x^*)$. Show that $T_\\Omega(x^*) \\subsetneq T_{\\text{lin}}(x^*)$ strictly.</p>""",
        "solution": """<p><span class="part">Part (a): Standard Form & Active Constraints</span><br>
Write constraints as $g_j(x) \\le 0$:
$$g_1(x) = x_2 - (1 - x_1)^3 \\le 0, \\quad g_2(x) = -x_2 \\le 0$$
At $x^* = (1, 0)^\\top$:
$$g_1(1, 0) = 0 - (1 - 1)^3 = 0 \\quad (\\text{Active})$$
$$g_2(1, 0) = -0 = 0 \\quad (\\text{Active})$$
The active index set is <span class="ans">$\\mathcal{A}(x^*) = \\{1, 2\\}$</span>.</p>

<p><span class="part">Part (b): Gradient Computation & LICQ Check</span><br>
$$\\nabla g_1(x) = \\begin{bmatrix} 3(1 - x_1)^2 \\\\[2pt] 1 \\end{bmatrix} \\implies \\nabla g_1(1, 0) = \\begin{bmatrix} 0 \\\\ 1 \\end{bmatrix}$$
$$\\nabla g_2(x) = \\begin{bmatrix} 0 \\\\[2pt] -1 \\end{bmatrix} \\implies \\nabla g_2(1, 0) = \\begin{bmatrix} 0 \\\\ -1 \\end{bmatrix}$$
Notice that:
$$\\nabla g_1(x^*) + \\nabla g_2(x^*) = \\begin{bmatrix} 0 \\\\ 1 \\end{bmatrix} + \\begin{bmatrix} 0 \\\\ -1 \\end{bmatrix} = \\begin{bmatrix} 0 \\\\ 0 \\end{bmatrix}$$
The active constraint gradients are anti-parallel and linearly dependent. <span class="ans">LICQ FAILS!</span></p>

<p><span class="part">Part (c): Linearized Cone vs. Geometric Tangent Cone</span><br>
1. <strong>Linearized Cone $T_{\\text{lin}}(x^*)$:</strong><br>
$$d = (d_1, d_2)^\\top \\in T_{\\text{lin}}(x^*) \\iff \\nabla g_1(x^*)^\\top d \\le 0 \\text{ and } \\nabla g_2(x^*)^\\top d \\le 0$$
$$d_2 \\le 0 \\quad \\text{and} \\quad -d_2 \\le 0 \\implies d_2 = 0$$
There is NO restriction on $d_1$!
$$<span class="ans">T_{\\text{lin}}(x^*) = \\{ (d_1, 0)^\\top : d_1 \\in \\mathbb{R} \\} = \\text{entire } x_1\\text{-axis}</span>$$

2. <strong>Geometric Tangent Cone $T_\\Omega(x^*)$:</strong><br>
For any feasible point $(x_1, x_2) \\in \\Omega$: $0 \\le x_2 \\le (1 - x_1)^3$.<br>
This requires $(1 - x_1)^3 \\ge 0 \\implies 1 - x_1 \\ge 0 \\implies x_1 \\le 1$.<br>
Any feasible curve approaching $(1, 0)$ must stay within $x_1 \\le 1$, which forces $d_1 = \\lim_{t \\to 0} \\frac{x_1(t) - 1}{t} \\le 0$.<br>
$$<span class="ans">T_\\Omega(x^*) = \\{ (d_1, 0)^\\top : d_1 \\le 0 \\} = \\text{negative } x_1\\text{-axis}</span>$$
Thus $T_\\Omega(x^*) \\subsetneq T_{\\text{lin}}(x^*)$ strictly! The linearized cone contains spurious directions ($d_1 > 0$) that are physically infeasible.</p>""",
        "takeaway": "When LICQ fails, the linearized cone can be strictly larger than the true geometric tangent cone, allowing KKT stationarity to fail even at a true local minimum."
    },
    {
        "id": 10992,
        "subject": "CMO",
        "topicId": "09_Geometry_of_Constrained_Optimization_Tangent_Cone_and_LICQ",
        "topicTitle": "09 · Constrained Geometry, Tangent Cone & LICQ",
        "title": "MFCQ vs LICQ & Multiplier Boundedness (Stanford Boyd)",
        "kind2": "pyq",
        "source": "Stanford EE364a / Boyd Ch 5",
        "marks": "[8 Marks]",
        "question": """<p>Consider the general nonlinear program:
$$\\min f(x) \\quad \\text{s.t.} \\quad g_j(x) \\le 0 \\; (j=1,\\dots,m), \\quad h_i(x) = 0 \\; (i=1,\\dots,p)$$
<span class="part">(a)</span> State the <strong>Mangasarian-Fromovitz Constraint Qualification (MFCQ)</strong> at a feasible point $x^*$.<br>
<span class="part">(b)</span> Compare MFCQ with LICQ. Why is MFCQ strictly weaker than LICQ?<br>
<span class="part">(c)</span> What is the fundamental duality consequence: what does LICQ guarantee about the Lagrange multipliers versus what MFCQ guarantees?</p>""",
        "solution": """<p><span class="part">Part (a): Definition of MFCQ</span><br>
MFCQ holds at $x^*$ if:
<ol>
  <li>The equality constraint gradients $\\{\\nabla h_i(x^*)\\}_{i=1}^p$ are <strong>linearly independent</strong>.</li>
  <li>There exists a direction $d \\in \\mathbb{R}^n$ such that:
  $$\\nabla h_i(x^*)^\\top d = 0 \\quad \\forall i = 1, \\dots, p$$
  $$\\nabla g_j(x^*)^\\top d < 0 \\quad \\forall j \\in \\mathcal{A}(x^*) \\quad \\text{(strictly negative for all active inequalities!)}$$
  </li>
</ol></p>

<p><span class="part">Part (b): Comparison with LICQ</span><br>
<ul>
  <li><strong>LICQ</strong> requires the combined set $\\{\\nabla h_i(x^*)\\} \\cup \\{\\nabla g_j(x^*)\\}_{j \\in \\mathcal{A}(x^*)}$ to be mutually linearly independent.</li>
  <li><strong>MFCQ</strong> does NOT require the active inequality gradients to be linearly independent! It only requires the existence of a single common strictly interior direction $d$.</li>
  <li>If LICQ holds, we can always solve the linear system $\\nabla g_j^\\top d = -1 < 0$ and $\\nabla h_i^\\top d = 0$, so <strong>LICQ implies MFCQ</strong>. The converse is false.</li>
</ul></p>

<p><span class="part">Part (c): Multiplier Boundedness vs Uniqueness</span><br>
<ul>
  <li><span class="ans"><strong>Gauvin's Theorem:</strong> MFCQ holds $\\iff$ the set of KKT Lagrange multipliers $\\Lambda(x^*)$ is non-empty and <strong>compact (bounded)</strong>.</span></li>
  <li><span class="ans"><strong>LICQ holds $\\iff$</strong> the Lagrange multiplier vector $\\lambda^*$ is <strong>unique</strong>.</span></li>
</ul>
MFCQ is the exact necessary and sufficient condition for dual multiplier stability and penalty convergence without requiring uniqueness.</p>""",
        "takeaway": "LICQ guarantees multiplier uniqueness. MFCQ is strictly weaker and guarantees multiplier boundedness, which is essential for numerical dual convergence."
    },
    {
        "id": 10993,
        "subject": "CMO",
        "topicId": "09_Geometry_of_Constrained_Optimization_Tangent_Cone_and_LICQ",
        "topicTitle": "09 · Constrained Geometry, Tangent Cone & LICQ",
        "title": "Normal Cone & Variational FONC (Generated Exam)",
        "kind2": "practice",
        "source": "IISc / Bertsekas Benchmark",
        "marks": "[10 Marks]",
        "question": """<p>Let $\\Omega = \\{x \\in \\mathbb{R}^2 : x_1 \\ge 0, \\; x_2 \\ge 0, \\; x_1 + x_2 \\le 1\\}$.<br>
<span class="part">(a)</span> At the corner point $x^* = (0, 0)^\\top$, derive the cone of feasible directions $\\mathcal{F}(x^*)$ and the normal cone $N_\\Omega(x^*)$.<br>
<span class="part">(b)</span> Prove that for any continuously differentiable function $f$, a necessary condition for $x^*$ to be a local minimizer of $f$ over $\\Omega$ is:
$$-\\nabla f(x^*) \\in N_\\Omega(x^*)$$
<span class="part">(c)</span> For $f(x) = 2x_1 + 3x_2$, verify whether $x^* = (0, 0)^\\top$ is a local minimizer using this condition.</p>""",
        "solution": """<p><span class="part">Part (a): Feasible Cone & Normal Cone at the Origin</span><br>
At $x^* = (0, 0)^\\top$:
<ul>
  <li>Active constraints: $g_1(x) = -x_1 \\le 0$ and $g_2(x) = -x_2 \\le 0$.</li>
  <li>Cone of feasible directions:
  $$\\mathcal{F}(x^*) = \\{ d \\in \\mathbb{R}^2 : -d_1 \\le 0, -d_2 \\le 0 \\} = <span class="ans">\\mathbb{R}_+^2 = \\{ (d_1, d_2) : d_1 \\ge 0, d_2 \\ge 0 \\}</span>$$
  (The entire first quadrant).</li>
  <li>Normal cone (polar of $\\mathcal{F}(x^*)$):
  $$N_\\Omega(x^*) = \\{ v \\in \\mathbb{R}^2 : v^\\top d \\le 0 \\; \\forall d \\in \\mathcal{F}(x^*) \\}$$
  For $v_1 d_1 + v_2 d_2 \\le 0$ for all $d_1 \\ge 0, d_2 \\ge 0$, we must have $v_1 \\le 0$ and $v_2 \\le 0$.
  $$<span class="ans">N_\\Omega(x^*) = -\\mathbb{R}_+^2 = \\{ (v_1, v_2) : v_1 \\le 0, v_2 \\le 0 \\}</span>$$
  (The entire third quadrant).</li>
</ul></p>

<p><span class="part">Part (b): Proof of Variational FONC</span><br>
If $x^*$ is a local minimizer over $\\Omega$, there cannot exist any feasible descent direction.<br>
For any feasible direction $d \\in \\mathcal{F}(x^*)$, the directional derivative must be non-negative:
$$\\nabla f(x^*)^\\top d = \\lim_{t \\to 0^+} \\frac{f(x^* + t d) - f(x^*)}{t} \\ge 0$$
Multiplying by $-1$:
$$(-\\nabla f(x^*))^\\top d \\le 0 \\quad \\forall d \\in \\mathcal{F}(x^*)$$
By the definition of the normal cone $N_\\Omega(x^*)$, any vector whose inner product with every feasible direction is non-positive belongs to $N_\\Omega(x^*)$.<br>
<span class="ans">Therefore, $-\\nabla f(x^*) \\in N_\\Omega(x^*)$.</span> $\\blacksquare$</p>

<p><span class="part">Part (c): Verification for $f(x) = 2x_1 + 3x_2$</span><br>
Gradient: $\\nabla f(x^*) = \\begin{bmatrix} 2 \\\\ 3 \\end{bmatrix}$.<br>
Negative gradient:
$$-\\nabla f(x^*) = \\begin{bmatrix} -2 \\\\ -3 \\end{bmatrix}$$
Check membership in normal cone:
$$-2 \\le 0 \\quad \\text{and} \\quad -3 \\le 0 \\implies \\begin{bmatrix} -2 \\\\ -3 \\end{bmatrix} \\in -\\mathbb{R}_+^2 = N_\\Omega(x^*)$$
<span class="ans">The condition is satisfied! $x^* = (0, 0)^\\top$ is indeed the global minimizer</span> (minimum value $f(0, 0) = 0$).</p>""",
        "takeaway": "Constrained optimality states $-\\nabla f(x^*) \\in N_\\Omega(x^*)$: the negative gradient (steepest descent) points directly outward into the normal cone, so no feasible movement can decrease $f$."
    },

    # =========================================================================
    # TOPIC 10: Separating Hyperplanes and Farkas' Lemma
    # =========================================================================
    {
        "id": 11091,
        "subject": "CMO",
        "topicId": "10_Separating_Hyperplanes_and_Farkas_Lemma",
        "topicTitle": "10 · Separating Hyperplanes & Farkas’ Lemma",
        "title": "Farkas’ Lemma Alternative Certificate (IISc Endsem 2024)",
        "kind2": "pyq",
        "source": "IISc Endsem 2024 / Luenberger Ch 4",
        "marks": "[10 Marks]",
        "question": """<p>Consider the matrix and vector:
$$A = \\begin{bmatrix} 1 & 1 \\\\ 2 & 1 \\end{bmatrix}, \\quad b = \\begin{bmatrix} 2 \\\\ 5 \\end{bmatrix}$$
Farkas' Lemma states that for any $A \\in \\mathbb{R}^{m \\times n}$ and $b \\in \\mathbb{R}^m$, exactly one of the following two systems has a solution:
$$\\text{System 1: } A x = b, \\quad x \\ge 0$$
$$\\text{System 2: } A^\\top y \\ge 0, \\quad b^\\top y < 0$$
<span class="part">(a)</span> Solve the linear system $A x = b$ and determine whether System 1 has a solution.<br>
<span class="part">(b)</span> Since System 1 fails, find an explicit certificate vector $y \\in \\mathbb{R}^2$ that solves System 2.</p>""",
        "solution": """<p><span class="part">Part (a): Testing System 1</span><br>
Set up the linear system:
$$\\begin{bmatrix} 1 & 1 \\\\ 2 & 1 \\end{bmatrix} \\begin{bmatrix} x_1 \\\\ x_2 \\end{bmatrix} = \\begin{bmatrix} 2 \\\\ 5 \\end{bmatrix}$$
Row 1: $x_1 + x_2 = 2 \\implies x_2 = 2 - x_1$.<br>
Row 2: $2x_1 + x_2 = 5 \\implies 2x_1 + (2 - x_1) = 5 \\implies x_1 = 3$.<br>
Then $x_2 = 2 - 3 = -1$.<br>
The unique linear solution is:
$$x = \\begin{bmatrix} 3 \\\\ -1 \\end{bmatrix}$$
However, $x_2 = -1 < 0$, which <span class="ans">violates $x \\ge 0$</span>.<br>
Since $A$ is invertible, $x$ is unique, so System 1 has <strong>NO solution</strong> in the non-negative orthant.</p>

<p><span class="part">Part (b): Finding Separating Certificate $y$ for System 2</span><br>
By Farkas' Lemma, System 2 must have a solution:
$$A^\\top y = \\begin{bmatrix} 1 & 2 \\\\ 1 & 1 \\end{bmatrix} \\begin{bmatrix} y_1 \\\\ y_2 \\end{bmatrix} = \\begin{bmatrix} y_1 + 2y_2 \\\\[2pt] y_1 + y_2 \\end{bmatrix} \\ge \\begin{bmatrix} 0 \\\\ 0 \\end{bmatrix}$$
$$b^\\top y = 2y_1 + 5y_2 < 0$$
From the boundary of the cone, set $y_1 + 2y_2 = 0 \\implies y_1 = -2y_2$.<br>
Substitute into the second constraint:
$$y_1 + y_2 = -2y_2 + y_2 = -y_2 \\ge 0 \\implies y_2 \\le 0$$
Substitute into the objective $b^\\top y$:
$$b^\\top y = 2(-2y_2) + 5y_2 = y_2 < 0$$
Pick $y_2 = -1$. Then $y_1 = -2(-1) = 2$.<br>
Vector: <span class="ans">$y = \\begin{bmatrix} 2 \\\\ -1 \\end{bmatrix}$</span>.<br>
Let us verify both conditions explicitly:
<ol>
  <li>$A^\\top y = \\begin{bmatrix} 2 + 2(-1) \\\\ 2 + (-1) \\end{bmatrix} = \\begin{bmatrix} 0 \\\\ 1 \\end{bmatrix} \\ge \\begin{bmatrix} 0 \\\\ 0 \\end{bmatrix}$ &nbsp; (Satisfied!)</li>
  <li>$b^\\top y = 2(2) + 5(-1) = 4 - 5 = -1 < 0$ &nbsp; (Satisfied!)</li>
</ol>
<span class="ans">$y = \\begin{bmatrix} 2 \\\\ -1 \\end{bmatrix}$ is the valid Farkas separating hyperplane certificate.</span></p>""",
        "takeaway": "Farkas' Lemma is the algebraic engine of linear duality: if a vector $b$ lies outside the polyhedral cone generated by $A$'s columns, there exists a hyperplane $y$ separating $b$ from the entire cone."
    },
    {
        "id": 11092,
        "subject": "CMO",
        "topicId": "10_Separating_Hyperplanes_and_Farkas_Lemma",
        "topicTitle": "10 · Separating Hyperplanes & Farkas’ Lemma",
        "title": "Gordan’s Transposition Theorem (Stanford Boyd)",
        "kind2": "pyq",
        "source": "Stanford EE364a / Boyd Ch 2",
        "marks": "[8 Marks]",
        "question": """<p>Gordan's Theorem of the Alternative states that for any matrix $A \\in \\mathbb{R}^{m \\times n}$, exactly one of the following two systems has a solution:
$$\\text{System 1: } A x < 0 \\quad \\text{for some } x \\in \\mathbb{R}^n \\; (\\text{strict inequality})$$
$$\\text{System 2: } A^\\top y = 0, \\quad y \\ge 0, \\quad y \\ne 0 \\quad \\text{for some } y \\in \\mathbb{R}^m$$
<span class="part">(a)</span> Prove that Systems 1 and 2 cannot be simultaneously solvable (Weak Alternative).<br>
<span class="part">(b)</span> Prove that if System 1 has no solution, then System 2 must have a solution (Strong Alternative via Farkas' Lemma / Separation Theorem).</p>""",
        "solution": """<p><span class="part">Part (a): Mutual Exclusivity (Weak Alternative)</span><br>
Suppose for contradiction that both systems have solutions $x$ and $y$.<br>
Since $y \\ge 0$ and $y \\ne 0$, at least one component $y_i > 0$.<br>
Since $A x < 0$, each component $(A x)_i < 0$.<br>
Take the inner product $y^\\top (A x)$:
$$y^\\top (A x) = \\sum_{i=1}^m y_i (A x)_i$$
Because every term $y_i (A x)_i \\le 0$ and for the index where $y_i > 0$, $y_i (A x)_i < 0$, the sum is strictly negative:
$$y^\\top (A x) < 0$$
On the other hand, using associativity:
$$y^\\top (A x) = (A^\\top y)^\\top x$$
From System 2, $A^\\top y = 0$. Therefore:
$$(A^\\top y)^\\top x = 0^\\top x = 0$$
This implies $0 < 0$, an impossible contradiction! <span class="ans">Both systems cannot hold simultaneously.</span></p>

<p><span class="part">Part (b): Strong Alternative via Separation</span><br>
Assume System 1 has no solution: there is no $x \\in \\mathbb{R}^n$ with $A x < 0$.<br>
Consider the range space $\\mathcal{R} = \\{ A x : x \\in \\mathbb{R}^n \\} \\subset \\mathbb{R}^m$ and the open negative orthant $\\mathcal{K} = \\{ z \\in \\mathbb{R}^m : z < 0 \\}$.<br>
Since System 1 has no solution, $\\mathcal{R} \\cap \\mathcal{K} = \\emptyset$.<br>
Both $\\mathcal{R}$ (a subspace) and $\\mathcal{K}$ (an open convex cone) are convex sets. By the Separating Hyperplane Theorem, there exists a non-zero normal vector $y \\in \\mathbb{R}^m$ ($y \\ne 0$) and $\\alpha \\in \\mathbb{R}$ such that:
$$y^\\top z \\le \\alpha \\le y^\\top (A x) \\quad \\forall z \\in \\mathcal{K}, \\; \\forall x \\in \\mathbb{R}^n$$
1. Since $\\mathcal{R}$ is a subspace, $y^\\top A x$ is bounded below for all $x \\in \\mathbb{R}^n$ only if $y^\\top A x = 0$ for all $x$, which means <span class="ans">$A^\\top y = 0$</span> (and $\\alpha = 0$).<br>
2. For $y^\\top z \\le 0$ for all $z < 0$, taking limits toward coordinate directions requires <span class="ans">$y_i \\ge 0$</span> for all $i = 1, \\dots, m$.<br>
Since $y \\ne 0$, this construct exactly solves System 2! $\\blacksquare$</p>""",
        "takeaway": "Gordan's theorem is Farkas' lemma for strict inequalities: a set of linear open halfspaces has no common intersection if and only if zero lies in the convex cone of their outward normals."
    },
    {
        "id": 11093,
        "subject": "CMO",
        "topicId": "10_Separating_Hyperplanes_and_Farkas_Lemma",
        "topicTitle": "10 · Separating Hyperplanes & Farkas’ Lemma",
        "title": "Strict Hyperplane Separation via Projection (Generated Exam)",
        "kind2": "practice",
        "source": "IISc / Boyd Benchmark",
        "marks": "[10 Marks]",
        "question": """<p>Let $C \\subset \\mathbb{R}^n$ be a non-empty closed convex set and let $y \\notin C$.<br>
<span class="part">(a)</span> Prove that there exists a unique closest point $x^* = \\Pi_C(y) \\in C$ minimizing $\\|x - y\\|_2$.<br>
<span class="part">(b)</span> Prove the fundamental <strong>Variational Inequality of Projections</strong>:
$$(y - x^*)^\\top (x - x^*) \\le 0 \\quad \\forall x \\in C$$
<span class="part">(c)</span> Using $a = y - x^*$, construct an explicit hyperplane that <em>strictly separates</em> $y$ from $C$.</p>""",
        "solution": """<p><span class="part">Part (a): Existence & Uniqueness of Projection</span><br>
The projection problem is $\\min_{x \\in C} \\frac{1}{2}\\|x - y\\|_2^2$.
<ul>
  <li>The objective $f(x) = \\frac{1}{2}\\|x - y\\|^2$ is continuous and coercive ($\\lim_{\\|x\\| \\to \\infty} f(x) = \\infty$). Since $C$ is non-empty and closed, a minimizer $x^*$ exists by the Weierstrass Coercive Theorem.</li>
  <li>Because $f(x)$ is strictly convex and $C$ is a convex set, the minimizer $x^*$ is strictly unique.</li>
</ul></p>

<p><span class="part">Part (b): Variational Inequality Proof</span><br>
Let $x \\in C$ be any arbitrary point. Since $C$ is convex, the line segment between $x^*$ and $x$ belongs to $C$:
$$x_\\alpha = x^* + \\alpha (x - x^*) \\in C \\quad \\forall \\alpha \\in [0, 1]$$
Since $x^*$ minimizes the distance to $y$:
$$\\|x^* - y\\|^2 \\le \\|x_\\alpha - y\\|^2 = \\|(x^* - y) + \\alpha(x - x^*)\\|^2$$
Expand the squared Euclidean norm:
$$\\|x^* - y\\|^2 \\le \\|x^* - y\\|^2 + 2\\alpha (x^* - y)^\\top (x - x^*) + \\alpha^2 \\|x - x^*\\|^2$$
Subtract $\\|x^* - y\\|^2$ from both sides and divide by $\\alpha > 0$:
$$0 \\le 2(x^* - y)^\\top (x - x^*) + \\alpha \\|x - x^*\\|^2$$
Taking the limit as $\\alpha \\downarrow 0$:
$$(x^* - y)^\\top (x - x^*) \\ge 0$$
Multiplying by $-1$ flips the inequality:
$$<span class="ans">(y - x^*)^\\top (x - x^*) \\le 0 \\quad \\forall x \\in C</span> \\quad \\blacksquare$$</p>

<p><span class="part">Part (c): Construction of Strictly Separating Hyperplane</span><br>
Define the normal vector $a = y - x^*$. Since $y \\notin C$, $a \\ne 0$.<br>
From Part (b):
$$a^\\top (x - x^*) \\le 0 \\implies a^\\top x \\le a^\\top x^* \\quad \\forall x \\in C$$
Now evaluate the linear function at the point $y$:
$$a^\\top y = a^\\top (x^* + a) = a^\\top x^* + \\|a\\|_2^2$$
Since $a \\ne 0$, $\\|a\\|_2^2 > 0$, so $a^\\top y > a^\\top x^*$.<br>
Choose the midpoint threshold:
$$\\gamma = a^\\top x^* + \\frac{1}{2}\\|a\\|_2^2$$
Then:
$$a^\\top x \\le a^\\top x^* < \\gamma < a^\\top x^* + \\|a\\|_2^2 = a^\\top y$$
<span class="ans">The hyperplane $\\{z \\in \\mathbb{R}^n : a^\\top z = \\gamma\\}$ strictly separates $y$ from $C$.</span></p>""",
        "takeaway": "The projection vector $y - \\Pi_C(y)$ serves as the normal vector to a strictly separating hyperplane between any external point $y$ and a closed convex set $C$."
    }
]

def main():
    target_file = os.path.join(os.path.dirname(__file__), "..", "practice_cmo.js")
    target_file = os.path.abspath(target_file)
    
    with open(target_file, "r", encoding="utf-8") as f:
        txt = f.read()
    
    # parse existing cards
    pfx = "window.PRACTICE_DATA.push(\n"
    start = txt.find(pfx)
    end = txt.rfind("\n);")
    cards = json.loads(txt[start+len(pfx):end])
    
    # filter out existing IDs if already present
    new_ids = {c["id"] for c in NEW_CARDS}
    existing = [c for c in cards if c["id"] not in new_ids]
    combined = existing + NEW_CARDS
    
    js_content = "/* Practice Questions Database for CMO (Topics 01-10) */\n"
    js_content += "window.PRACTICE_DATA = window.PRACTICE_DATA || [];\n\n"
    js_content += "window.PRACTICE_DATA.push(\n"
    js_content += json.dumps(combined, indent=2)
    js_content += "\n);\n"
    
    with open(target_file, "w", encoding="utf-8") as f:
        f.write(js_content)
        
    print(f"Successfully updated {target_file}! Total practice cards: {len(combined)}")

if __name__ == "__main__":
    main()
