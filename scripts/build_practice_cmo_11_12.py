#!/usr/bin/env python3
"""
build_practice_cmo_11_12.py
Appends practice questions (flippable cards) for CMO Topics 11 & 12 to practice_cmo.js.
  Topic 11: Karush-Kuhn-Tucker Conditions, FONC and Sufficiency
  Topic 12: Second-Order Optimality Conditions in Constrained Optimization
"""

import json
import os

NEW_CARDS = [
    # =========================================================================
    # TOPIC 11: Karush-Kuhn-Tucker Conditions, FONC and Sufficiency
    # =========================================================================
    {
        "id": 11191,
        "subject": "CMO",
        "topicId": "11_Karush_Kuhn_Tucker_Conditions_FONC_and_Sufficiency",
        "topicTitle": "11 · KKT Conditions & Sufficiency",
        "title": "Complete Manual KKT Solution (IISc Midterm 2024)",
        "kind2": "pyq",
        "source": "IISc Midterm 3 2024 / Nocedal & Wright Ch 12",
        "marks": "[10 Marks]",
        "question": """<p>Consider the constrained optimization problem:
$$\\min_{x_1, x_2} f(x) = (x_1 - 1)^2 + (x_2 - 2)^2 \\quad \\text{subject to} \\quad x_1 + x_2 \\le 1, \\quad x_1 \\ge 0, \\quad x_2 \\ge 0$$
<span class="part">(a)</span> State the complete Karush-Kuhn-Tucker (KKT) conditions in standard form.<br>
<span class="part">(b)</span> Show that the unconstrained minimizer is infeasible, and solve for the active constraints and optimal Lagrange multipliers.<br>
<span class="part">(c)</span> State the optimal solution $x^*$ and minimum value, explaining why KKT conditions are sufficient here.</p>""",
        "solution": """<p><span class="part">Part (a): KKT System in Standard Form</span><br>
Constraints: $g_1(x) = x_1 + x_2 - 1 \\le 0, \\; g_2(x) = -x_1 \\le 0, \\; g_3(x) = -x_2 \\le 0$.
<ol>
  <li><strong>Stationarity:</strong>
  $$\\begin{bmatrix} 2(x_1 - 1) \\\\ 2(x_2 - 2) \\end{bmatrix} + \\mu_1 \\begin{bmatrix} 1 \\\\ 1 \\end{bmatrix} + \\mu_2 \\begin{bmatrix} -1 \\\\ 0 \\end{bmatrix} + \\mu_3 \\begin{bmatrix} 0 \\\\ -1 \\end{bmatrix} = \\begin{bmatrix} 0 \\\\ 0 \\end{bmatrix}$$</li>
  <li><strong>Primal Feasibility:</strong> $x_1 + x_2 \\le 1, \\; x_1 \\ge 0, \\; x_2 \\ge 0$.</li>
  <li><strong>Dual Feasibility:</strong> $\\mu_1 \\ge 0, \\; \\mu_2 \\ge 0, \\; \\mu_3 \\ge 0$.</li>
  <li><strong>Complementary Slackness:</strong> $\\mu_1(x_1 + x_2 - 1) = 0, \\; \\mu_2 x_1 = 0, \\; \\mu_3 x_2 = 0$.</li>
</ol></p>

<p><span class="part">Part (b): Solving the KKT System</span><br>
Unconstrained minimizer is $(1, 2)^\\top$, which gives $1 + 2 = 3 > 1$ (infeasible). Thus at least one constraint is active.<br>
Test active constraint $g_1(x) = 0 \\implies x_1 + x_2 = 1$.<br>
Assume $x_1 > 0, x_2 > 0 \\implies \\mu_2 = \\mu_3 = 0$.
$$2(x_1 - 1) + \\mu_1 = 0 \\implies \\mu_1 = 2(1 - x_1)$$
$$2(x_2 - 2) + \\mu_1 = 0 \\implies \\mu_1 = 2(2 - x_2) = 2(2 - (1 - x_1)) = 2(1 + x_1)$$
Equating gives $2(1 - x_1) = 2(1 + x_1) \\implies 2x_1 = 0 \\implies x_1 = 0$.<br>
Then $x_2 = 1 - 0 = 1$, which hits the boundary $x_1 = 0$, so $g_2$ is ALSO active!<br>
At $x^* = (0, 1)^\\top$:
<ul>
  <li>$g_1$ active, $g_2$ active, $g_3$ inactive ($x_2 = 1 > 0 \\implies \\mu_3 = 0$).</li>
  <li>Equation 2: $2(1 - 2) + \\mu_1 = 0 \\implies -2 + \\mu_1 = 0 \\implies <span class="ans">\\mu_1 = 2 \\ge 0</span>$.</li>
  <li>Equation 1: $2(0 - 1) + \\mu_1 - \\mu_2 = 0 \\implies -2 + 2 - \\mu_2 = 0 \\implies <span class="ans">\\mu_2 = 0 \\ge 0</span>$.</li>
</ul>
All primal, dual, and complementary slackness conditions hold strictly!</p>

<p><span class="part">Part (c): Global Optimality & Sufficiency</span><br>
The objective $f$ is strictly convex and all constraint functions $g_j$ are linear (hence convex).<br>
By the KKT Convex Sufficiency Theorem, any KKT point of a convex program is a guaranteed global minimizer.<br>
<span class="ans">Unique global minimizer: $x^* = (0, 1)^\\top$ with minimum objective value $f(0, 1) = (0 - 1)^2 + (1 - 2)^2 = 2$.</span></p>""",
        "takeaway": "Complementary slackness allows systematically checking candidate active sets. For convex programs, any point satisfying KKT conditions is automatically a global minimum without needing second-order tests."
    },
    {
        "id": 11192,
        "subject": "CMO",
        "topicId": "11_Karush_Kuhn_Tucker_Conditions_FONC_and_Sufficiency",
        "topicTitle": "11 · KKT Conditions & Sufficiency",
        "title": "Water-Filling Algorithm via KKT (Stanford Boyd)",
        "kind2": "pyq",
        "source": "Stanford EE364a / Boyd Ch 5",
        "marks": "[10 Marks]",
        "question": """<p>Consider the classic convex communication/resource allocation problem:
$$\\min_{x \\in \\mathbb{R}^n} -\\sum_{i=1}^n \\log(\\alpha_i + x_i) \\quad \\text{subject to} \\quad \\sum_{i=1}^n x_i = 1, \\quad x_i \\ge 0 \\; (i = 1, \\dots, n)$$
where $\\alpha_i > 0$ represents the background noise power in channel $i$.<br>
<span class="part">(a)</span> Formulate the Lagrangian and derive the KKT optimality conditions.<br>
<span class="part">(b)</span> Derive the analytic <strong>water-filling solution</strong>:
$$x_i^* = \\max\\left(0, \\; \\frac{1}{\\nu^*} - \\alpha_i\\right)$$
where $1/\\nu^*$ represents the common water level.<br>
<span class="part">(c)</span> Explain how the water level $1/\\nu^*$ is uniquely determined.</p>""",
        "solution": """<p><span class="part">Part (a): Lagrangian & KKT Conditions</span><br>
$$\\mathcal{L}(x, \\nu, \\lambda) = -\\sum_{i=1}^n \\log(\\alpha_i + x_i) + \\nu \\left( \\sum_{i=1}^n x_i - 1 \\right) - \\sum_{i=1}^n \\lambda_i x_i$$
KKT Conditions:
<ol>
  <li><strong>Stationarity:</strong> $\\frac{\\partial \\mathcal{L}}{\\partial x_i} = -\\frac{1}{\\alpha_i + x_i} + \\nu - \\lambda_i = 0 \\implies \\nu - \\lambda_i = \\frac{1}{\\alpha_i + x_i}$.</li>
  <li><strong>Primal Feasibility:</strong> $\\sum_{i=1}^n x_i = 1$ and $x_i \\ge 0$ for all $i$.</li>
  <li><strong>Dual Feasibility:</strong> $\\lambda_i \\ge 0$ (equality multiplier $\\nu \\in \\mathbb{R}$ is unrestricted).</li>
  <li><strong>Complementary Slackness:</strong> $\\lambda_i x_i = 0$ for all $i = 1, \\dots, n$.</li>
</ol></p>

<p><span class="part">Part (b): Water-Filling Formula Derivation</span><br>
Consider each coordinate $i$:
<ul>
  <li><strong>Case 1 ($x_i > 0$):</strong> By complementary slackness, $\\lambda_i = 0$.<br>
  Then $\\nu = \\frac{1}{\\alpha_i + x_i} \\implies \\alpha_i + x_i = \\frac{1}{\\nu} \\implies x_i = \\frac{1}{\\nu} - \\alpha_i$.<br>
  Since $x_i > 0$, this occurs whenever $\\frac{1}{\\nu} > \\alpha_i$.</li>
  <li><strong>Case 2 ($x_i = 0$):</strong> $\\lambda_i \\ge 0$.<br>
  Then $\\nu = \\frac{1}{\\alpha_i} + \\lambda_i \\ge \\frac{1}{\\alpha_i} \\implies \\frac{1}{\\nu} \\le \\alpha_i$.</li>
</ul>
Combining both cases into a single compact expression:
$$<span class="ans">x_i^* = \\max\\left(0, \\; \\frac{1}{\\nu^*} - \\alpha_i\\right) = \\left( \\frac{1}{\\nu^*} - \\alpha_i \\right)_+</span>$$</p>

<p><span class="part">Part (c): Determining the Water Level $1/\\nu^*$</span><br>
Substitute the solution into the total resource constraint:
$$\\sum_{i=1}^n \\max\\left(0, \\; \\frac{1}{\\nu} - \\alpha_i\\right) = 1$$
Define $g(w) = \\sum_{i=1}^n (w - \\alpha_i)_+$ where $w = 1/\\nu$.<br>
$g(w)$ is a continuous, piecewise-linear, strictly monotonically increasing function for $w > \\min_i \\alpha_i$.<br>
As $w \\to \\infty$, $g(w) \\to \\infty$, and for $w \\le \\min_i \\alpha_i$, $g(w) = 0$.<br>
By the Intermediate Value Theorem, there exists a <span class="ans">strictly unique root $w^* = 1/\\nu^*$</span> satisfying $g(w^*) = 1$. It can be solved exactly in $\\mathcal{O}(n \\log n)$ time by sorting $\\alpha_i$.</p>""",
        "takeaway": "The water-filling solution allocates power only to low-noise channels where the common water level exceeds the noise floor ($1/\\nu^* > \\alpha_i$), starving noisy channels ($x_i^* = 0$)."
    },
    {
        "id": 11193,
        "subject": "CMO",
        "topicId": "11_Karush_Kuhn_Tucker_Conditions_FONC_and_Sufficiency",
        "topicTitle": "11 · KKT Conditions & Sufficiency",
        "title": "KKT Convex Sufficiency Theorem (Generated Exam)",
        "kind2": "practice",
        "source": "IISc / Bertsekas Benchmark",
        "marks": "[10 Marks]",
        "question": """<p>Consider the general optimization problem:
$$\\min_{x \\in \\mathbb{R}^n} f(x) \\quad \\text{subject to} \\quad g_j(x) \\le 0 \\; (j=1,\\dots,m), \\quad h_i(x) = 0 \\; (i=1,\\dots,p)$$
Assume that $f$ and all $g_j$ are convex, and all $h_i$ are affine ($h_i(x) = a_i^\\top x - b_i$).<br>
<span class="part">(a)</span> State the complete KKT conditions for a triplet $(x^*, \\lambda^*, \\mu^*)$.<br>
<span class="part">(b)</span> Prove that if $(x^*, \\lambda^*, \\mu^*)$ satisfies the KKT conditions, then $x^*$ is a <strong>global minimizer</strong> of the problem.<br>
<span class="part">(c)</span> Does this sufficiency result require any constraint qualification (such as Slater's condition or LICQ)?</p>""",
        "solution": """<p><span class="part">Part (a): KKT Conditions</span><br>
1. $\\nabla f(x^*) + \\sum_{j=1}^m \\mu_j^* \\nabla g_j(x^*) + \\sum_{i=1}^p \\lambda_i^* \\nabla h_i(x^*) = 0$<br>
2. $g_j(x^*) \\le 0 \\; (\\forall j), \\quad h_i(x^*) = 0 \\; (\\forall i)$<br>
3. $\\mu_j^* \\ge 0 \\; (\\forall j)$<br>
4. $\\mu_j^* g_j(x^*) = 0 \\; (\\forall j)$</p>

<p><span class="part">Part (b): Proof of Global Optimality</span><br>
Let $x$ be any arbitrary feasible point: $g_j(x) \\le 0$ and $h_i(x) = 0$.<br>
By convexity of $f$, for any $x$:
$$f(x) \\ge f(x^*) + \\nabla f(x^*)^\\top (x - x^*)$$
Substitute $\\nabla f(x^*)$ from the stationarity condition:
$$\\nabla f(x^*) = -\\sum_{j=1}^m \\mu_j^* \\nabla g_j(x^*) - \\sum_{i=1}^p \\lambda_i^* \\nabla h_i(x^*)$$
This gives:
$$f(x) \\ge f(x^*) - \\sum_{j=1}^m \\mu_j^* \\nabla g_j(x^*)^\\top (x - x^*) - \\sum_{i=1}^p \\lambda_i^* \\nabla h_i(x^*)^\\top (x - x^*)$$
1. Since $g_j$ is convex: $g_j(x) \\ge g_j(x^*) + \\nabla g_j(x^*)^\\top (x - x^*)$.<br>
Since $\\mu_j^* \\ge 0$:
$$-\\mu_j^* \\nabla g_j(x^*)^\\top (x - x^*) \\ge \\mu_j^* [g_j(x^*) - g_j(x)] = \\mu_j^* g_j(x^*) - \\mu_j^* g_j(x)$$
By complementary slackness, $\\mu_j^* g_j(x^*) = 0$. Since $x$ is feasible, $g_j(x) \\le 0$, so $-\\mu_j^* g_j(x) \\ge 0$.<br>
Thus: $-\\mu_j^* \\nabla g_j(x^*)^\\top (x - x^*) \\ge 0$.<br>
2. Since $h_i$ is affine ($h_i(x) = a_i^\\top x - b_i$): $\\nabla h_i(x^*)^\\top (x - x^*) = a_i^\\top (x - x^*) = h_i(x) - h_i(x^*) = 0 - 0 = 0$.<br>
Combining these inequalities:
$$f(x) \\ge f(x^*) + 0 + 0 = f(x^*)$$
Since this holds for every feasible $x$, <span class="ans">$x^*$ is a global minimizer</span>. $\\blacksquare$</p>

<p><span class="part">Part (c): Independence from Constraint Qualifications</span><br>
<span class="ans">NO constraint qualifications are needed for sufficiency!</span><br>
Constraint qualifications (Slater, LICQ) are only needed for KKT to be <em>necessary</em> (i.e. to guarantee that multipliers exist). Once multipliers are found that satisfy KKT for a convex problem, optimality is mathematically guaranteed regardless of LICQ or Slater.</p>""",
        "takeaway": "KKT sufficiency requires only convexity of $f$ and $g_j$, and affinity of $h_i$. Constraint qualifications are entirely irrelevant for sufficiency."
    },

    # =========================================================================
    # TOPIC 12: Second-Order Optimality Conditions in Constrained Optimization
    # =========================================================================
    {
        "id": 11291,
        "subject": "CMO",
        "topicId": "12_Second_Order_Optimality_Conditions_in_Constrained_Optimization",
        "topicTitle": "12 · Second-Order Constrained Optimality (SOSC)",
        "title": "Critical Cone & SOSC Classification (IISc Midterm 2024)",
        "kind2": "pyq",
        "source": "IISc Midterm 3 2024 / Nocedal & Wright Ch 12",
        "marks": "[10 Marks]",
        "question": """<p>Consider the constrained problem:
$$\\min_{x_1, x_2} f(x) = x_1^2 - x_2^2 \\quad \\text{subject to} \\quad h_1(x) = x_1^2 + x_2^2 - 1 = 0$$
<span class="part">(a)</span> Find all four KKT stationary points and their corresponding Lagrange multipliers $\\lambda$.<br>
<span class="part">(b)</span> Formulate the Hessian of the Lagrangian $\\nabla_{xx}^2 \\mathcal{L}(x, \\lambda)$.<br>
<span class="part">(c)</span> For each KKT point, compute the critical cone and evaluate second-order conditions (SOSC/SONC) to classify the points as strict local minima, local maxima, or saddle points.</p>""",
        "solution": """<p><span class="part">Part (a): KKT Points & Multipliers</span><br>
Lagrangian: $\\mathcal{L}(x, \\lambda) = x_1^2 - x_2^2 + \\lambda (x_1^2 + x_2^2 - 1)$.<br>
Stationarity:
$$\\nabla_x \\mathcal{L} = \\begin{bmatrix} 2x_1 + 2\\lambda x_1 \\\\[2pt] -2x_2 + 2\\lambda x_2 \\end{bmatrix} = \\begin{bmatrix} 2x_1(1 + \\lambda) \\\\[2pt] 2x_2(-1 + \\lambda) \\end{bmatrix} = \\begin{bmatrix} 0 \\\\ 0 \\end{bmatrix}$$
Constraint: $x_1^2 + x_2^2 = 1$.
<ul>
  <li><strong>Case 1 ($x_2 = 0 \\implies x_1 = \\pm 1$):</strong><br>
  $2x_1(1 + \\lambda) = 0 \\implies \\lambda = -1$.<br>
  Points: <span class="ans">$P_1 = (1, 0)^\\top, \\lambda = -1$</span> and <span class="ans">$P_2 = (-1, 0)^\\top, \\lambda = -1$</span>.</li>
  <li><strong>Case 2 ($x_1 = 0 \\implies x_2 = \\pm 1$):</strong><br>
  $2x_2(-1 + \\lambda) = 0 \\implies \\lambda = 1$.<br>
  Points: <span class="ans">$P_3 = (0, 1)^\\top, \\lambda = 1$</span> and <span class="ans">$P_4 = (0, -1)^\\top, \\lambda = 1$</span>.</li>
</ul></p>

<p><span class="part">Part (b): Hessian of the Lagrangian</span><br>
$$\\nabla_{xx}^2 \\mathcal{L}(x, \\lambda) = \\begin{bmatrix} 2 + 2\\lambda & 0 \\\\ 0 & -2 + 2\\lambda \\end{bmatrix}$$</p>

<p><span class="part">Part (c): Second-Order Classification</span><br>
1. <strong>At $P_1 = (1, 0)^\\top, \\lambda = -1$:</strong><br>
$\\nabla h_1(1, 0) = \\begin{bmatrix} 2 \\\\ 0 \\end{bmatrix}$. Tangent critical cone: $\\nabla h_1^\\top w = 0 \\implies 2w_1 = 0 \\implies w = (0, w_2)^\\top$.<br>
Hessian: $\\nabla_{xx}^2 \\mathcal{L} = \\begin{bmatrix} 0 & 0 \\\\ 0 & -4 \\end{bmatrix}$.<br>
Curvature on critical subspace ($w_2 \\ne 0$):
$$w^\\top \\nabla_{xx}^2 \\mathcal{L} w = \\begin{bmatrix} 0 & w_2 \\end{bmatrix} \\begin{bmatrix} 0 & 0 \\\\ 0 & -4 \\end{bmatrix} \\begin{bmatrix} 0 \\\\ w_2 \\end{bmatrix} = -4 w_2^2 < 0$$
SONC is violated! <span class="ans">$P_1, P_2$ are strict local maxima</span> ($f(1, 0) = 1$).<br><br>
2. <strong>At $P_3 = (0, 1)^\\top, \\lambda = 1$:</strong><br>
$\\nabla h_1(0, 1) = \\begin{bmatrix} 0 \\\\ 2 \\end{bmatrix}$. Tangent critical cone: $\\nabla h_1^\\top w = 0 \\implies 2w_2 = 0 \\implies w = (w_1, 0)^\\top$.<br>
Hessian: $\\nabla_{xx}^2 \\mathcal{L} = \\begin{bmatrix} 4 & 0 \\\\ 0 & 0 \\end{bmatrix}$.<br>
Curvature on critical subspace ($w_1 \\ne 0$):
$$w^\\top \\nabla_{xx}^2 \\mathcal{L} w = \\begin{bmatrix} w_1 & 0 \\end{bmatrix} \\begin{bmatrix} 4 & 0 \\\\ 0 & 0 \\end{bmatrix} \\begin{bmatrix} w_1 \\\\ 0 \\end{bmatrix} = 4 w_1^2 > 0$$
SOSC is satisfied strictly! <span class="ans">$P_3, P_4$ are strict local minima</span> ($f(0, 1) = -1$).</p>""",
        "takeaway": "SOSC tests curvature ONLY on the tangent nullspace of active constraints ($w^\\top \\nabla_{xx}^2 \\mathcal{L} w > 0$). The unconstrained eigenvalues of the Hessian are completely misleading."
    },
    {
        "id": 11292,
        "subject": "CMO",
        "topicId": "12_Second_Order_Optimality_Conditions_in_Constrained_Optimization",
        "topicTitle": "12 · Second-Order Constrained Optimality (SOSC)",
        "title": "Concave Objective with Valid SOSC Minimum (Stanford Boyd)",
        "kind2": "pyq",
        "source": "Stanford EE364a / Boyd Ch 5",
        "marks": "[10 Marks]",
        "question": """<p>Consider minimizing the strictly concave objective:
$$f(x_1, x_2) = -x_1^2 - 2x_2^2 \\quad (\\text{notice } \\nabla^2 f = \\operatorname{diag}(-2, -4) \\prec 0)$$
subject to the unit circle constraint $h_1(x) = x_1^2 + x_2^2 - 1 = 0$.<br>
<span class="part">(a)</span> Explain why testing $\\nabla^2 f(x^*) \\succ 0$ is conceptually flawed in constrained optimization.<br>
<span class="part">(b)</span> Show that $x^* = (0, 1)^\\top$ is a KKT point with multiplier $\\lambda^* = 2$.<br>
<span class="part">(c)</span> Compute the Hessian of the Lagrangian and prove that Second-Order Sufficient Conditions (SOSC) are strictly satisfied at $x^*$, verifying that $x^*$ is a strict local minimum despite $f$ being concave everywhere!</p>""",
        "solution": """<p><span class="part">Part (a): Flaw of Objective Hessian Alone</span><br>
In constrained optimization, any movement along the feasible manifold forces the trajectory to curve with the constraint boundary.<br>
The rate of change of the gradient along a curved curve $x(t)$ with $\\dot{x}(0) = w$ and $\\ddot{x}(0) = v$ satisfies:
$$\\frac{d^2}{dt^2} f(x(t)) = w^\\top \\nabla^2 f(x^*) w + \\nabla f(x^*)^\\top v$$
Since $h(x(t)) = 0$, differentiating twice gives $w^\\top \\nabla^2 h(x^*) w + \\nabla h(x^*)^\\top v = 0$.<br>
Substituting $\\nabla f(x^*) = -\\lambda^* \\nabla h(x^*)$ yields:
$$\\frac{d^2}{dt^2} f(x(t)) = w^\\top (\\nabla^2 f(x^*) + \\lambda^* \\nabla^2 h(x^*)) w = w^\\top \\nabla_{xx}^2 \\mathcal{L}(x^*, \\lambda^*) w$$
<span class="ans">The constraint curvature $\\lambda^* \\nabla^2 h$ directly transfers into the effective second derivative!</span></p>

<p><span class="part">Part (b): KKT Stationarity at $x^* = (0, 1)^\\top$</span><br>
$$\\nabla f(0, 1) = \\begin{bmatrix} -2(0) \\\\ -4(1) \\end{bmatrix} = \\begin{bmatrix} 0 \\\\ -4 \\end{bmatrix}, \\quad \\nabla h(0, 1) = \\begin{bmatrix} 2(0) \\\\ 2(1) \\end{bmatrix} = \\begin{bmatrix} 0 \\\\ 2 \\end{bmatrix}$$
$$\\nabla f(x^*) + \\lambda \\nabla h(x^*) = \\begin{bmatrix} 0 \\\\ -4 \\end{bmatrix} + \\lambda \\begin{bmatrix} 0 \\\\ 2 \\end{bmatrix} = \\begin{bmatrix} 0 \\\\ 0 \\end{bmatrix} \\implies <span class="ans">\\lambda^* = 2</span>$$</p>

<p><span class="part">Part (c): Lagrangian Hessian & SOSC Verification</span><br>
$$\\nabla^2 f(x) = \\begin{bmatrix} -2 & 0 \\\\ 0 & -4 \\end{bmatrix}, \\quad \\nabla^2 h(x) = \\begin{bmatrix} 2 & 0 \\\\ 0 & 2 \\end{bmatrix}$$
$$\\nabla_{xx}^2 \\mathcal{L}(x^*, \\lambda^*) = \\begin{bmatrix} -2 & 0 \\\\ 0 & -4 \\end{bmatrix} + 2 \\begin{bmatrix} 2 & 0 \\\\ 0 & 2 \\end{bmatrix} = \\begin{bmatrix} -2 + 4 & 0 \\\\[2pt] 0 & -4 + 4 \\end{bmatrix} = <span class="ans">\\begin{bmatrix} 2 & 0 \\\\ 0 & 0 \\end{bmatrix}</span>$$
The tangent space at $(0, 1)^\\top$ is $\\nabla h^\\top w = 2w_2 = 0 \\implies w = (w_1, 0)^\\top$.<br>
For any non-zero tangent vector $w \\ne 0$ ($w_1 \\ne 0$):
$$w^\\top \\nabla_{xx}^2 \\mathcal{L} w = \\begin{bmatrix} w_1 & 0 \\end{bmatrix} \\begin{bmatrix} 2 & 0 \\\\ 0 & 0 \\end{bmatrix} \\begin{bmatrix} w_1 \\\\ 0 \\end{bmatrix} = <span class="ans">2 w_1^2 > 0</span>$$
<span class="ans">SOSC is strictly satisfied!</span> The outward curvature of the unit circle contributes $+4I$, completely overpowering the concave objective curvature $-2I$, creating a valid strict local minimum!</p>""",
        "takeaway": "Constraint curvature $\\lambda^* \\nabla^2 h(x^*)$ can turn a strictly concave objective into a strictly convex constrained problem along the feasible manifold."
    },
    {
        "id": 11293,
        "subject": "CMO",
        "topicId": "12_Second_Order_Optimality_Conditions_in_Constrained_Optimization",
        "topicTitle": "12 · Second-Order Constrained Optimality (SOSC)",
        "title": "Strict Complementarity & Reduced Hessian (Generated Exam)",
        "kind2": "practice",
        "source": "IISc / Nocedal & Wright Benchmark",
        "marks": "[10 Marks]",
        "question": """<p>Consider the inequality constrained problem $\\min f(x)$ subject to $g_j(x) \\le 0$ ($j = 1, \\dots, m$). Let $(x^*, \\mu^*)$ be a KKT point with active set $\\mathcal{A}(x^*)$.<br>
<span class="part">(a)</span> Define <strong>Strict Complementarity</strong> and write down the general definition of the critical cone $\\mathcal{C}(x^*, \\mu^*)$.<br>
<span class="part">(b)</span> Prove that under Strict Complementarity, the critical cone collapses into a flat linear subspace:
$$\\mathcal{C}(x^*, \\mu^*) = \\{ w \\in \\mathbb{R}^n : \\nabla g_j(x^*)^\\top w = 0 \\; \\forall j \\in \\mathcal{A}(x^*) \\}$$
<span class="part">(c)</span> Let the columns of $Z \\in \\mathbb{R}^{n \\times (n - |\\mathcal{A}|)}$ form an orthonormal basis for this subspace. Show how the Second-Order Sufficient Condition can be tested via the <strong>Reduced Hessian</strong> $H_R = Z^\\top \\nabla_{xx}^2 \\mathcal{L}(x^*, \\mu^*) Z$.</p>""",
        "solution": """<p><span class="part">Part (a): Definitions</span><br>
<ul>
  <li><strong>Strict Complementarity</strong> holds at a KKT pair $(x^*, \\mu^*)$ if every active inequality constraint has a strictly positive Lagrange multiplier:
  $$\\mu_j^* > 0 \\quad \\forall j \\in \\mathcal{A}(x^*) = \\{ j : g_j(x^*) = 0 \\}$$</li>
  <li><strong>General Critical Cone $\\mathcal{C}(x^*, \\mu^*)$:</strong>
  $$\\mathcal{C}(x^*, \\mu^*) = \\left\\{ w \\in \\mathbb{R}^n : \\begin{array}{ll} \\nabla g_j(x^*)^\\top w = 0 & \\text{if } j \\in \\mathcal{A}(x^*) \\text{ and } \\mu_j^* > 0 \\\\[4pt] \\nabla g_j(x^*)^\\top w \\le 0 & \\text{if } j \\in \\mathcal{A}(x^*) \\text{ and } \\mu_j^* = 0 \\end{array} \\right\\}$$</li>
</ul></p>

<p><span class="part">Part (b): Collapse to a Linear Subspace</span><br>
Under strict complementarity, there are NO active constraints with $\\mu_j^* = 0$.<br>
Every active index $j \\in \\mathcal{A}(x^*)$ has $\\mu_j^* > 0$.<br>
Therefore, the inequality condition $\\nabla g_j(x^*)^\\top w \\le 0$ is never triggered!<br>
The critical cone definition simplifies entirely to equality constraints:
$$<span class="ans">\\mathcal{C}(x^*, \\mu^*) = \\{ w \\in \\mathbb{R}^n : \\nabla g_j(x^*)^\\top w = 0 \\; \\forall j \\in \\mathcal{A}(x^*) \\} = \\ker(A_\\mathcal{A}(x^*))</span>$$
where $A_\\mathcal{A}(x^*)$ is the Jacobian matrix of active constraints. A cone defined purely by linear equalities is a <span class="ans">linear subspace</span>.</p>

<p><span class="part">Part (c): Reduced Hessian Formulation</span><br>
Any vector $w$ in the nullspace $\\ker(A_\\mathcal{A}(x^*))$ can be parameterized uniquely as:
$$w = Z v \\quad \\text{for some } v \\in \\mathbb{R}^{n - |\\mathcal{A}|}$$
The second-order curvature condition requires $w^\\top \\nabla_{xx}^2 \\mathcal{L} w > 0$ for all $w \\in \\mathcal{C} \\setminus \\{0\\}$.<br>
Substituting $w = Z v$:
$$w^\\top \\nabla_{xx}^2 \\mathcal{L} w = (Z v)^\\top \\nabla_{xx}^2 \\mathcal{L} (Z v) = v^\\top (Z^\\top \\nabla_{xx}^2 \\mathcal{L} Z) v > 0 \\quad \\forall v \\ne 0$$
Define the <strong>Reduced Hessian</strong>:
$$<span class="ans">H_R = Z^\\top \\nabla_{xx}^2 \\mathcal{L}(x^*, \\mu^*) Z \\in \\mathbb{R}^{(n - |\\mathcal{A}|) \\times (n - |\\mathcal{A}|)}</span>$$
The SOSC is strictly satisfied if and only if the smaller $(n - |\\mathcal{A}|) \\times (n - |\\mathcal{A}|)$ symmetric matrix $H_R$ is strictly positive definite:
$$<span class="ans">H_R \\succ 0</span>$$
This can be verified by computing the Cholesky factorization of $H_R$.</p>""",
        "takeaway": "Strict complementarity eliminates boundary ambiguity, transforming the critical cone into a linear subspace where constrained SOSC reduces to the positive definiteness of the Reduced Hessian $Z^\\top \\nabla_{xx}^2 \\mathcal{L} Z$."
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
    
    js_content = "/* Practice Questions Database for CMO (Topics 01-12) */\n"
    js_content += "window.PRACTICE_DATA = window.PRACTICE_DATA || [];\n\n"
    js_content += "window.PRACTICE_DATA.push(\n"
    js_content += json.dumps(combined, indent=2)
    js_content += "\n);\n"
    
    with open(target_file, "w", encoding="utf-8") as f:
        f.write(js_content)
        
    print(f"Successfully updated {target_file}! Total practice cards: {len(combined)}")

if __name__ == "__main__":
    main()
