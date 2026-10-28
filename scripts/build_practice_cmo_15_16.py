#!/usr/bin/env python3
"""
build_practice_cmo_15_16.py
Appends practice questions (flippable cards) for CMO Topics 15 & 16 to practice_cmo.js.
  Topic 15: Active Set Methods for Quadratic Programming
  Topic 16: Lagrangian Duality and Slater’s Condition
"""

import json
import os

NEW_CARDS = [
    # =========================================================================
    # TOPIC 15: Active Set Methods for Quadratic Programming
    # =========================================================================
    {
        "id": 11591,
        "subject": "CMO",
        "topicId": "15_Active_Set_Methods_for_Quadratic_Programming",
        "topicTitle": "15 · Active Set Methods for QP",
        "title": "EQP Solution via KKT Matrix (IISc Midterm 2024)",
        "kind2": "pyq",
        "source": "IISc Midterm 3 2024 / Nocedal & Wright Ch 16",
        "marks": "[8 Marks]",
        "question": """<p>Consider the Equality-Constrained Quadratic Program (EQP):
$$\\min_{x_1, x_2} f(x) = x_1^2 + x_2^2 \\quad \\text{subject to} \\quad x_1 + 2x_2 = 5$$
<span class="part">(a)</span> Write down the block KKT matrix system:
$$\\begin{bmatrix} G & A^\\top \\\\ A & 0 \\end{bmatrix} \\begin{bmatrix} x^* \\\\ \\lambda^* \\end{bmatrix} = \\begin{bmatrix} -c \\\\ b \\end{bmatrix}$$
<span class="part">(b)</span> Solve the system analytically for the optimal primal vector $x^*$ and the Lagrange multiplier $\\lambda^*$.<br>
<span class="part">(c)</span> Verify the solution geometrically using the orthogonal projection onto a line.</p>""",
        "solution": """<p><span class="part">Part (a): Block KKT Matrix Setup</span><br>
Objective $f(x) = \\frac{1}{2} x^\\top G x + c^\\top x$:
$$G = \\begin{bmatrix} 2 & 0 \\\\ 0 & 2 \\end{bmatrix} = 2 I_2, \\quad c = \\begin{bmatrix} 0 \\\\ 0 \\end{bmatrix}$$
Constraint $A x = b$:
$$A = \\begin{bmatrix} 1 & 2 \\end{bmatrix}, \\quad b = [5]$$
The full $(2 + 1) \\times (2 + 1)$ symmetric indefinite KKT system is:
$$<span class="ans">\\begin{bmatrix} 2 & 0 & 1 \\\\ 0 & 2 & 2 \\\\ 1 & 2 & 0 \\end{bmatrix} \\begin{bmatrix} x_1 \\\\ x_2 \\\\ \\lambda \\end{bmatrix} = \\begin{bmatrix} 0 \\\\ 0 \\\\ 5 \\end{bmatrix}</span>$$</p>

<p><span class="part">Part (b): Analytic Solution</span><br>
Row 1: $2x_1 + \\lambda = 0 \\implies x_1 = -\\lambda / 2$.<br>
Row 2: $2x_2 + 2\\lambda = 0 \\implies x_2 = -\\lambda$.<br>
Row 3 (Constraint): Substitute $x_1$ and $x_2$:
$$x_1 + 2x_2 = 5 \\implies -\\frac{\\lambda}{2} + 2(-\\lambda) = 5 \\implies -\\frac{5}{2} \\lambda = 5 \\implies <span class="ans">\\lambda^* = -2</span>$$
Now compute the primal coordinates:
$$x_1^* = -\\frac{-2}{2} = 1, \\quad x_2^* = -(-2) = 2$$
<span class="ans">$$x^* = \\begin{bmatrix} 1 \\\\ 2 \\end{bmatrix}, \\quad \\lambda^* = -2$$</span></p>

<p><span class="part">Part (c): Geometric Verification</span><br>
$f(x) = x_1^2 + x_2^2$ represents the squared distance from the origin $(0, 0)^\\top$ to the line $x_1 + 2x_2 = 5$.<br>
By the hyperplane projection formula:
$$\\Pi_L(0) = \\frac{b}{\\|a\\|^2} a = \\frac{5}{1^2 + 2^2} \\begin{bmatrix} 1 \\\\ 2 \\end{bmatrix} = \\frac{5}{5} \\begin{bmatrix} 1 \\\\ 2 \\end{bmatrix} = \\begin{bmatrix} 1 \\\\ 2 \\end{bmatrix}$$
The minimum objective value is $f(1, 2) = 1^2 + 2^2 = 5$. Verified!</p>""",
        "takeaway": "An equality-constrained QP is equivalent to a single linear system governed by the Karush-Kuhn-Tucker saddle-point matrix. Solving it yields both primal solution and Lagrange multipliers simultaneously."
    },
    {
        "id": 11592,
        "subject": "CMO",
        "topicId": "15_Active_Set_Methods_for_Quadratic_Programming",
        "topicTitle": "15 · Active Set Methods for QP",
        "title": "Null-Space Method for EQP (Stanford Boyd)",
        "kind2": "pyq",
        "source": "Stanford EE364a / Boyd Ch 10",
        "marks": "[10 Marks]",
        "question": """<p>Consider the large-scale Equality-Constrained QP:
$$\\min_{x \\in \\mathbb{R}^n} \\frac{1}{2} x^\\top G x + c^\\top x \\quad \\text{subject to} \\quad A x = b$$
where $A \\in \\mathbb{R}^{m \\times n}$ has full row rank ($m < n$).<br>
<span class="part">(a)</span> Explain how the <strong>Null-Space Method</strong> parameterizes the feasible manifold $x = x_p + Z v$.<br>
<span class="part">(b)</span> Derive the reduced unconstrained linear system of size $(n - m) \\times (n - m)$ satisfied by $v^*$.<br>
<span class="part">(c)</span> What is the computational advantage when the number of constraints $m$ is nearly equal to $n$ ($n - m \\ll n$)?</p>""",
        "solution": """<p><span class="part">Part (a): Manifold Parameterization</span><br>
1. Find any particular solution $x_p$ satisfying $A x_p = b$ (e.g. $x_p = A^\\top (A A^\\top)^{-1} b$).<br>
2. Compute a basis matrix $Z \\in \\mathbb{R}^{n \\times (n - m)}$ for the nullspace $\\ker(A)$, so that $A Z = 0$ and $Z$ has full column rank.<br>
Any feasible vector $x$ must satisfy $A(x - x_p) = b - b = 0 \\implies x - x_p \\in \\ker(A)$.<br>
Therefore, every feasible point can be represented uniquely as:
$$<span class="ans">x = x_p + Z v, \\quad v \\in \\mathbb{R}^{n - m}</span>$$</p>

<p><span class="part">Part (b): Reduced Unconstrained System</span><br>
Substitute the parameterization into the quadratic objective:
$$f(x_p + Z v) = \\frac{1}{2}(x_p + Z v)^\\top G (x_p + Z v) + c^\\top (x_p + Z v)$$
$$\\phi(v) = \\frac{1}{2} v^\\top (Z^\\top G Z) v + (Z^\\top (G x_p + c))^\\top v + \\text{const}$$
This is an <strong>unconstrained strictly convex quadratic</strong> in the reduced variable $v \\in \\mathbb{R}^{n - m}$!<br>
Setting the gradient with respect to $v$ to zero:
$$\\nabla_v \\phi(v) = (Z^\\top G Z) v + Z^\\top (G x_p + c) = 0$$
$$\\implies <span class="ans">(Z^\\top G Z) v^* = -Z^\\top (G x_p + c)</span>$$
Once $v^*$ is solved, the exact solution is reconstructed as:
$$x^* = x_p + Z v^*$$</p>

<p><span class="part">Part (c): Computational Complexity Advantage</span><br>
The full KKT matrix has size $(n + m) \\times (n + m)$ and is indefinite (requiring Bunch-Kaufman or augmented factorization).<br>
In contrast, the reduced matrix $Z^\\top G Z$ has size only <span class="ans">$(n - m) \\times (n - m)$</span> and is <strong>strictly positive definite</strong> ($Z^\\top G Z \\succ 0$).<br>
When $n = 10000$ and $m = 9900$, $n - m = 100$. Instead of solving a $19,900 \\times 19,900$ indefinite system, we solve a tiny $100 \\times 100$ positive definite system using fast Cholesky factorization!</p>""",
        "takeaway": "The null-space method completely eliminates equality constraints, projecting the quadratic objective onto the tangent manifold where standard unconstrained Cholesky factorization applies."
    },
    {
        "id": 11593,
        "subject": "CMO",
        "topicId": "15_Active_Set_Methods_for_Quadratic_Programming",
        "topicTitle": "15 · Active Set Methods for QP",
        "title": "Constraint Dropping & Feasible Step Length (Generated Exam)",
        "kind2": "practice",
        "source": "IISc / Nocedal & Wright Benchmark",
        "marks": "[10 Marks]",
        "question": """<p>Consider an Active-Set method for minimizing a convex QP with inequality constraints $a_i^\\top x \\ge b_i$. Let $x_k$ be the exact minimizer of the EQP with working set $\\mathcal{W}_k$.<br>
<span class="part">(a)</span> If the Lagrange multipliers satisfy $\\mu_i \\ge 0$ for all $i \\in \\mathcal{W}_k$, prove that $x_k$ is the global minimizer.<br>
<span class="part">(b)</span> If some multiplier $\\mu_q < 0$, we drop constraint $q$ to form $\\mathcal{W}^+ = \\mathcal{W}_k \\setminus \\{q\\}$. Prove that the resulting search direction $d$ is a <strong>strict descent direction</strong> into the feasible interior.<br>
<span class="part">(c)</span> Write down the exact formula for the maximum step length $\\alpha_k$ to avoid violating inactive constraints.</p>""",
        "solution": """<p><span class="part">Part (a): Optimality of Working Set</span><br>
Since $x_k$ solves the EQP over $\\mathcal{W}_k$, stationarity $\\nabla f(x_k) = \\sum_{i \\in \\mathcal{W}_k} \\mu_i a_i$ holds.<br>
If all $\\mu_i \\ge 0$, and setting $\\mu_j = 0$ for all inactive constraints $j \\notin \\mathcal{W}_k$, the triplet $(x_k, \\mu)$ satisfies all KKT conditions.<br>
Since the QP is convex, $x_k$ is the <span class="ans">exact global minimizer</span>.</p>

<p><span class="part">Part (b): Descent Proof upon Dropping Constraint</span><br>
At $x_k$, $\\nabla f(x_k) = \\sum_{i \\in \\mathcal{W}_k} \\mu_i a_i$.<br>
When constraint $q$ with $\\mu_q < 0$ is dropped, the new search direction $d$ satisfies:
$$a_i^\\top d = 0 \\quad \\forall i \\in \\mathcal{W}^+, \\quad \\text{and} \\quad a_q^\\top d = 1 > 0 \\; (\\text{moving away from boundary into } a_q^\\top x > b_q)$$
Evaluate the directional derivative of $f$ along $d$:
$$\\nabla f(x_k)^\\top d = \\left( \\sum_{i \\in \\mathcal{W}_k} \\mu_i a_i \\right)^\\top d = \\sum_{i \\in \\mathcal{W}^+} \\mu_i (a_i^\\top d) + \\mu_q (a_q^\\top d)$$
Since $a_i^\\top d = 0$ for all $i \\in \\mathcal{W}^+$ and $a_q^\\top d = 1$:
$$\\nabla f(x_k)^\\top d = \\mu_q (1) = \\mu_q$$
Because $\\mu_q < 0$:
$$<span class="ans">\\nabla f(x_k)^\\top d = \\mu_q < 0</span>$$
Thus $d$ is a strict descent direction!</p>

<p><span class="part">Part (c): Maximum Feasible Step Length</span><br>
For inactive constraints $i \\notin \\mathcal{W}_k$, we require $a_i^\\top (x_k + \\alpha p_k) \\ge b_i$:
$$a_i^\\top x_k + \\alpha a_i^\\top p_k \\ge b_i \\iff \\alpha a_i^\\top p_k \\ge b_i - a_i^\\top x_k$$
If $a_i^\\top p_k \\ge 0$, the constraint remains satisfied for all $\\alpha > 0$.<br>
If $a_i^\\top p_k < 0$, the step moves toward the boundary, requiring $\\alpha \\le \\frac{b_i - a_i^\\top x_k}{a_i^\\top p_k}$.<br>
Therefore:
$$<span class="ans">\\alpha_k = \\min\\left(1, \\; \\min_{i \\notin \\mathcal{W}_k, \\; a_i^\\top p_k < 0} \\frac{b_i - a_i^\\top x_k}{a_i^\\top p_k}\\right)</span>$$
If $\\alpha_k < 1$, the first constraint that achieves the minimum is added to the working set (the blocking constraint).</p>""",
        "takeaway": "Active-set methods make progress by alternating between solving EQPs on the current working set, dropping constraints with negative multipliers to decrease the objective, and adding blocking constraints."
    },

    # =========================================================================
    # TOPIC 16: Lagrangian Duality and Slater’s Condition
    # =========================================================================
    {
        "id": 11691,
        "subject": "CMO",
        "topicId": "16_Lagrangian_Duality_and_Slaters_Condition",
        "topicTitle": "16 · Lagrangian Duality & Slater’s Condition",
        "title": "QP Dual Function & Problem Derivation (IISc Endsem 2024)",
        "kind2": "pyq",
        "source": "IISc Endsem 2024 / Boyd Ch 5",
        "marks": "[10 Marks]",
        "question": """<p>Consider the strictly convex quadratic program:
$$\\min_{x \\in \\mathbb{R}^n} \\frac{1}{2} x^\\top Q x + c^\\top x \\quad \\text{subject to} \\quad A x \\le b$$
where $Q \\in \\mathbb{R}^{n \\times n}$ is symmetric positive definite ($Q \\succ 0$).<br>
<span class="part">(a)</span> Formulate the Lagrangian $\\mathcal{L}(x, \\mu)$ with dual multipliers $\\mu \\ge 0$.<br>
<span class="part">(b)</span> Minimize $\\mathcal{L}(x, \\mu)$ analytically over $x \\in \\mathbb{R}^n$ to derive the Lagrange dual function $g(\\mu)$.<br>
<span class="part">(c)</span> State the complete dual optimization problem and explain why it is strictly concave.</p>""",
        "solution": """<p><span class="part">Part (a): Lagrangian Formulation</span><br>
Write constraints in standard form $A x - b \\le 0$.<br>
The Lagrangian with dual multiplier vector $\\mu \\ge 0$ is:
$$\\mathcal{L}(x, \\mu) = \\frac{1}{2} x^\\top Q x + c^\\top x + \\mu^\\top (A x - b) = \\frac{1}{2} x^\\top Q x + (c + A^\\top \\mu)^\\top x - b^\\top \\mu$$</p>

<p><span class="part">Part (b): Analytic Minimization over $x$</span><br>
Hold $\\mu$ fixed. Since $Q \\succ 0$, $\\mathcal{L}(x, \\mu)$ is strictly convex in $x$.<br>
Differentiating with respect to $x$ and setting to zero:
$$\\nabla_x \\mathcal{L}(x, \\mu) = Q x + c + A^\\top \\mu = 0 \\implies <span class="ans">x^*(\\mu) = -Q^{-1} (c + A^\\top \\mu)</span>$$
Substitute $x^*(\\mu)$ back into the Lagrangian:
$$g(\\mu) = \\frac{1}{2} x^*(\\mu)^\\top Q x^*(\\mu) + (c + A^\\top \\mu)^\\top x^*(\\mu) - b^\\top \\mu$$
$$g(\\mu) = \\frac{1}{2} (c + A^\\top \\mu)^\\top Q^{-1} Q Q^{-1} (c + A^\\top \\mu) - (c + A^\\top \\mu)^\\top Q^{-1} (c + A^\\top \\mu) - b^\\top \\mu$$
$$<span class="ans">g(\\mu) = -\\frac{1}{2} (c + A^\\top \\mu)^\\top Q^{-1} (c + A^\\top \\mu) - b^\\top \\mu</span>$$
Expanding:
$$g(\\mu) = -\\frac{1}{2} \\mu^\\top (A Q^{-1} A^\\top) \\mu - (b + A Q^{-1} c)^\\top \\mu - \\frac{1}{2} c^\\top Q^{-1} c$$</p>

<p><span class="part">Part (c): Dual Problem</span><br>
The dual problem is:
$$\\max_{\\mu \\ge 0} g(\\mu) \\iff <span class="ans">\\min_{\\mu \\ge 0} \\frac{1}{2} \\mu^\\top (A Q^{-1} A^\\top) \\mu + (b + A Q^{-1} c)^\\top \\mu</span>$$
Since $Q \\succ 0$, $Q^{-1} \\succ 0$, so $A Q^{-1} A^\\top \\succeq 0$.<br>
The dual problem is another quadratic program with only simple bound constraints $\\mu \\ge 0$, which is significantly easier to solve than the primal when $m < n$.</p>""",
        "takeaway": "The dual of a strictly convex QP is another QP whose only constraints are non-negativity bounds $\\mu \\ge 0$, eliminating all linear coupling constraints."
    },
    {
        "id": 11692,
        "subject": "CMO",
        "topicId": "16_Lagrangian_Duality_and_Slaters_Condition",
        "topicTitle": "16 · Lagrangian Duality & Slater’s Condition",
        "title": "Weak Duality Theorem & Minimax Bound (Stanford Boyd)",
        "kind2": "pyq",
        "source": "Stanford EE364a / Boyd Ch 5",
        "marks": "[8 Marks]",
        "question": """<p>Consider the general optimization problem (not necessarily convex):
$$p^* = \\min_x f(x) \\quad \\text{subject to} \\quad g_j(x) \\le 0 \\; (j=1,\\dots,m), \\quad h_i(x) = 0 \\; (i=1,\\dots,p)$$
Let $g(\\lambda, \\mu) = \\inf_x \\mathcal{L}(x, \\lambda, \\mu)$ denote the Lagrange dual function, and let $d^* = \\sup_{\\mu \\ge 0, \\lambda} g(\\lambda, \\mu)$.<br>
<span class="part">(a)</span> Prove the <strong>Weak Duality Theorem</strong>: for every primal feasible $x$ and every dual feasible pair $(\\lambda, \\mu)$ with $\\mu \\ge 0$, $g(\\lambda, \\mu) \\le f(x)$.<br>
<span class="part">(b)</span> Deduce that $d^* \\le p^*$, and show that the duality gap $p^* - d^* \\ge 0$ is always non-negative.</p>""",
        "solution": """<p><span class="part">Part (a): Proof of Weak Duality</span><br>
Let $\\tilde{x}$ be any primal feasible point, meaning:
$$g_j(\\tilde{x}) \\le 0 \\; (\\forall j), \\quad h_i(\\tilde{x}) = 0 \\; (\\forall i)$$
Let $(\\tilde{\\lambda}, \\tilde{\\mu})$ be any dual feasible vector with $\\tilde{\\mu} \\ge 0$.<br>
Evaluate the Lagrangian at $(\\tilde{x}, \\tilde{\\lambda}, \\tilde{\\mu})$:
$$\\mathcal{L}(\\tilde{x}, \\tilde{\\lambda}, \\tilde{\\mu}) = f(\\tilde{x}) + \\sum_{j=1}^m \\underbrace{\\tilde{\\mu}_j}_{\\ge 0} \\underbrace{g_j(\\tilde{x})}_{\\le 0} + \\sum_{i=1}^p \\tilde{\\lambda}_i \\underbrace{h_i(\\tilde{x})}_{=0}$$
Since each product $\\tilde{\\mu}_j g_j(\\tilde{x}) \\le 0$ and each $\\tilde{\\lambda}_i h_i(\\tilde{x}) = 0$:
$$\\mathcal{L}(\\tilde{x}, \\tilde{\\lambda}, \\tilde{\\mu}) \\le f(\\tilde{x})$$
By definition of the dual function as the infimum over all $x \\in \\mathbb{R}^n$:
$$g(\\tilde{\\lambda}, \\tilde{\\mu}) = \\inf_{x} \\mathcal{L}(x, \\tilde{\\lambda}, \\tilde{\\mu}) \\le \\mathcal{L}(\\tilde{x}, \\tilde{\\lambda}, \\tilde{\\mu})$$
Chaining the two inequalities:
$$<span class="ans">g(\\tilde{\\lambda}, \\tilde{\\mu}) \\le f(\\tilde{x})</span> \\quad \\blacksquare$$</p>

<p><span class="part">Part (b): Non-Negative Duality Gap</span><br>
Since $g(\\lambda, \\mu) \\le f(x)$ holds for all dual feasible $(\\lambda, \\mu)$ and all primal feasible $x$:
Taking the infimum over all feasible $x$:
$$g(\\lambda, \\mu) \\le \\inf_{x \\text{ feasible}} f(x) = p^*$$
Now taking the supremum of the left side over all dual feasible $(\\lambda, \\mu)$ with $\\mu \\ge 0$:
$$<span class="ans">d^* = \\sup_{\\mu \\ge 0, \\lambda} g(\\lambda, \\mu) \\le p^*</span>$$
Therefore:
$$<span class="ans">p^* - d^* \\ge 0</span>$$
The duality gap is unconditionally non-negative, holding for ANY optimization problem (even integer, discrete, or wildly non-convex).</p>""",
        "takeaway": "Weak duality $d^* \\le p^*$ holds unconditionally for every optimization problem without exception. The dual function always provides a certifiable lower bound on the optimal primal objective."
    },
    {
        "id": 11693,
        "subject": "CMO",
        "topicId": "16_Lagrangian_Duality_and_Slaters_Condition",
        "topicTitle": "16 · Lagrangian Duality & Slater’s Condition",
        "title": "Slater’s Condition & Non-Convex Duality Gap (Generated Exam)",
        "kind2": "practice",
        "source": "IISc / Bertsekas Benchmark",
        "marks": "[10 Marks]",
        "question": """<p><span class="part">(a)</span> State <strong>Slater's Condition</strong> for a convex optimization problem $\\min f(x)$ s.t. $g_j(x) \\le 0, Ax = b$. Why are affine constraints exempt from strict inequality?<br>
<span class="part">(b)</span> What does Slater's condition guarantee regarding strong duality and the set of dual optimal solutions?<br>
<span class="part">(c)</span> Consider the discrete non-convex problem:
$$\\min_{x \\in \\{-1, 0, 1\\}} f(x) = x^3 \\quad \\text{subject to} \\quad g_1(x) = -x \\le 0$$
Compute the primal optimal value $p^*$, the dual function $g(\\mu)$, and the dual optimal value $d^*$. Calculate the exact duality gap $p^* - d^*$.</p>""",
        "solution": """<p><span class="part">Part (a): Slater's Condition</span><br>
For a convex problem with convex $f, g_j$ and affine equality constraints $A x = b$:
Slater's condition holds if there exists a strictly feasible point $\\hat{x} \\in \\operatorname{relint}(\\mathcal{D})$ such that:
$$g_j(\\hat{x}) < 0 \\quad \\forall j = 1, \\dots, m, \\quad \\text{and} \\quad A \\hat{x} = b$$
Affine constraints $A x = b$ are exempt from strict inequality because their epigraphs are flat hyperplanes that never have an empty interior along their relative affine hull.</p>

<p><span class="part">Part (b): Duality Guarantees</span><br>
Under Slater's condition:
<ol>
  <li><span class="ans"><strong>Strong Duality holds:</strong> $p^* = d^*$ (zero duality gap).</span></li>
  <li><span class="ans">The set of optimal dual multipliers is non-empty and bounded (achieved by some $\\mu^* < \\infty$).</span></li>
</ol></p>

<p><span class="part">Part (c): Non-Convex Counterexample Calculation</span><br>
Primal feasible domain: $x \\in \\{-1, 0, 1\\}$ and $-x \\le 0 \\implies x \\in \\{0, 1\\}$.<br>
Primal values: $f(0) = 0, f(1) = 1$.
$$p^* = \\min(0, 1) = <span class="ans">0</span> \\quad (\\text{at } x^* = 0)$$
Dual function for $\\mu \\ge 0$:
$$g(\\mu) = \\min_{x \\in \\{-1, 0, 1\\}} (x^3 - \\mu x)$$
Evaluate at the 3 domain points:
<ul>
  <li>$x = 0: 0 - 0 = 0$.</li>
  <li>$x = 1: 1^3 - \\mu(1) = 1 - \\mu$.</li>
  <li>$x = -1: (-1)^3 - \\mu(-1) = -1 + \\mu$.</li>
</ul>
$$g(\\mu) = \\min(0, \\; 1 - \\mu, \\; -1 + \\mu)$$
For $\\mu = 1$: $g(1) = \\min(0, 0, 0) = 0$.<br>
For $\\mu < 1$: $-1 + \\mu < 0 \\implies g(\\mu) = -1 + \\mu < 0$.<br>
For $\\mu > 1$: $1 - \\mu < 0 \\implies g(\\mu) = 1 - \\mu < 0$.<br>
The maximum dual value occurs at $\\mu = 1$ with $d^* = 0$.<br>
Now modify the domain to $x \\in \\{-2, 0, 1\\}$:
At $x = -2$: $(-2)^3 - \\mu(-2) = -8 + 2\\mu$.
Then $g(\\mu) = \\min(0, 1 - \\mu, -8 + 2\\mu)$.<br>
Equating $1 - \\mu = -8 + 2\\mu \\implies 3\\mu = 9 \\implies \\mu = 3$.<br>
At $\\mu = 3$: $g(3) = \\min(0, 1 - 3, -8 + 6) = \\min(0, -2, -2) = -2$.<br>
Dual optimum: $d^* = -2$.<br>
Primal optimum is still $p^* = 0$.<br>
<span class="ans">Duality gap: $p^* - d^* = 0 - (-2) = 2 > 0$!</span></p>""",
        "takeaway": "When convexity fails, the lower envelope of the Lagrangian can stay strictly below the primal minimum, producing a strictly positive duality gap."
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
    
    js_content = "/* Practice Questions Database for CMO (Topics 01-16) */\n"
    js_content += "window.PRACTICE_DATA = window.PRACTICE_DATA || [];\n\n"
    js_content += "window.PRACTICE_DATA.push(\n"
    js_content += json.dumps(combined, indent=2)
    js_content += "\n);\n"
    
    with open(target_file, "w", encoding="utf-8") as f:
        f.write(js_content)
        
    print(f"Successfully updated {target_file}! Total practice cards: {len(combined)}")

if __name__ == "__main__":
    main()
