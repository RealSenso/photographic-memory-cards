#!/usr/bin/env python3
"""
build_practice_cmo_13_14.py
Appends practice questions (flippable cards) for CMO Topics 13 & 14 to practice_cmo.js.
  Topic 13: Projections onto Convex Sets
  Topic 14: Gradient Projection Algorithm and Convergence
"""

import json
import os

NEW_CARDS = [
    # =========================================================================
    # TOPIC 13: Projections onto Convex Sets
    # =========================================================================
    {
        "id": 11391,
        "subject": "CMO",
        "topicId": "13_Projections_onto_Convex_Sets",
        "topicTitle": "13 · Projections onto Convex Sets",
        "title": "Hyperplane Projection (IISc Endsem 2024)",
        "kind2": "pyq",
        "source": "IISc Endsem 2024 / Bertsekas Ch 2",
        "marks": "[8 Marks]",
        "question": """<p>Consider the hyperplane in $\\mathbb{R}^3$:
$$H = \\{x \\in \\mathbb{R}^3 : x_1 + 2x_2 + 2x_3 = 6\\}$$
<span class="part">(a)</span> Derive the general closed-form formula for the orthogonal projection $\\Pi_H(y)$ of an arbitrary point $y \\in \\mathbb{R}^n$ onto a hyperplane $H = \\{x : a^\\top x = b\\}$.<br>
<span class="part">(b)</span> Find the exact coordinates of the projection of the point $y = (3, 4, 5)^\\top$ onto $H$.<br>
<span class="part">(c)</span> Calculate the minimum distance $\\operatorname{dist}(y, H) = \\|y - \\Pi_H(y)\\|_2$.</p>""",
        "solution": """<p><span class="part">Part (a): Hyperplane Projection Derivation</span><br>
The projection problem is $\\min_{x} \\frac{1}{2}\\|x - y\\|_2^2$ subject to $a^\\top x = b$.<br>
The Lagrangian is $\\mathcal{L}(x, \\lambda) = \\frac{1}{2}\\|x - y\\|^2 + \\lambda (a^\\top x - b)$.<br>
Stationarity:
$$\\nabla_x \\mathcal{L} = (x - y) + \\lambda a = 0 \\implies x = y - \\lambda a$$
Substitute into the hyperplane constraint $a^\\top x = b$:
$$a^\\top (y - \\lambda a) = b \\implies a^\\top y - \\lambda \\|a\\|_2^2 = b \\implies \\lambda^* = \\frac{a^\\top y - b}{\\|a\\|_2^2}$$
Substitute $\\lambda^*$ back into $x$:
$$<span class="ans">\\Pi_H(y) = y - \\frac{a^\\top y - b}{\\|a\\|_2^2} a</span>$$</p>

<p><span class="part">Part (b): Exact Numerical Calculation</span><br>
Given $a = \\begin{bmatrix} 1 \\\\ 2 \\\\ 2 \\end{bmatrix}$, $b = 6$, $y = \\begin{bmatrix} 3 \\\\ 4 \\\\ 5 \\end{bmatrix}$:
<ul>
  <li>$a^\\top y = 1(3) + 2(4) + 2(5) = 3 + 8 + 10 = 21$.</li>
  <li>$\\|a\\|_2^2 = 1^2 + 2^2 + 2^2 = 1 + 4 + 4 = 9$.</li>
  <li>Scalar multiplier: $\\lambda^* = \\frac{21 - 6}{9} = \\frac{15}{9} = \\frac{5}{3}$.</li>
</ul>
Projection:
$$\\Pi_H(y) = \\begin{bmatrix} 3 \\\\ 4 \\\\ 5 \\end{bmatrix} - \\frac{5}{3} \\begin{bmatrix} 1 \\\\ 2 \\\\ 2 \\end{bmatrix} = \\begin{bmatrix} 3 - 5/3 \\\\[2pt] 4 - 10/3 \\\\[2pt] 5 - 10/3 \\end{bmatrix} = <span class="ans">\\begin{bmatrix} 4/3 \\\\ 2/3 \\\\ 5/3 \\end{bmatrix}</span>$$
Check feasibility: $1(4/3) + 2(2/3) + 2(5/3) = \\frac{4 + 4 + 10}{3} = \\frac{18}{3} = 6$. Verified!</p>

<p><span class="part">Part (c): Distance to Hyperplane</span><br>
$$\\operatorname{dist}(y, H) = \\|y - \\Pi_H(y)\\|_2 = \\left\\|\\frac{5}{3} a\\right\\| = \\frac{5}{3} \\|a\\|_2 = \\frac{5}{3} \\sqrt{9} = \\frac{5}{3} \\times 3 = <span class="ans">5</span>$$</p>""",
        "takeaway": "Projection onto a hyperplane is an exact 1D displacement along the normal vector $a$ scaled by the signed residual distance $(a^\\top y - b)/\\|a\\|^2$."
    },
    {
        "id": 11392,
        "subject": "CMO",
        "topicId": "13_Projections_onto_Convex_Sets",
        "topicTitle": "13 · Projections onto Convex Sets",
        "title": "Box Projection & Component Decoupling (Stanford Boyd)",
        "kind2": "pyq",
        "source": "Stanford EE364a / Boyd Ch 8",
        "marks": "[8 Marks]",
        "question": """<p>Consider the $n$-dimensional box (hyper-rectangle):
$$C = \\{x \\in \\mathbb{R}^n : l_i \\le x_i \\le u_i, \\quad i = 1, \\dots, n\\}$$
where $l_i < u_i$ for all $i$.<br>
<span class="part">(a)</span> Formulate the projection problem $\\min_{x \\in C} \\frac{1}{2}\\|x - y\\|_2^2$ and prove that it decouples into $n$ independent 1D problems.<br>
<span class="part">(b)</span> Derive the componentwise projection operator $[\Pi_C(y)]_i$.<br>
<span class="part">(c)</span> For $l = (-1, 0, 2)^\\top$, $u = (2, 3, 5)^\\top$, find the projection of $y = (-3, 5, 4)^\\top$.</p>""",
        "solution": """<p><span class="part">Part (a): Problem Decoupling</span><br>
The projection problem is:
$$\\min_{x \\in C} \\frac{1}{2} \\|x - y\\|_2^2 = \\min_{l_i \\le x_i \\le u_i} \\frac{1}{2} \\sum_{i=1}^n (x_i - y_i)^2$$
Notice that:
<ol>
  <li>The objective function is a sum of terms where each term $\\frac{1}{2}(x_i - y_i)^2$ depends solely on $x_i$.</li>
  <li>The constraint set $C = [l_1, u_1] \\times [l_2, u_2] \\times \\dots \\times [l_n, u_n]$ is a Cartesian product of independent 1D intervals with no coupling across variables.</li>
</ol>
Therefore:
$$\\min_{x \\in C} \\frac{1}{2}\\|x - y\\|^2 = \\sum_{i=1}^n \\min_{l_i \\le x_i \\le u_i} \\frac{1}{2}(x_i - y_i)^2$$
The problem decouples completely into $n$ separate scalar minimizations.</p>

<p><span class="part">Part (b): 1D Solution & Clipping Operator</span><br>
For each coordinate $i$, the 1D function $\\phi(x_i) = \\frac{1}{2}(x_i - y_i)^2$ is strictly convex with global unconstrained minimum at $x_i = y_i$:
<ul>
  <li>If $y_i < l_i$, the unconstrained minimizer lies to the left of the interval, so the closest feasible point is $l_i$.</li>
  <li>If $y_i > u_i$, the unconstrained minimizer lies to the right, so the closest point is $u_i$.</li>
  <li>If $l_i \\le y_i \\le u_i$, $y_i$ is already feasible, so $[\Pi_C(y)]_i = y_i$.</li>
</ul>
Combining into the standard clamp/clip function:
$$<span class="ans">[\\Pi_C(y)]_i = \\operatorname{clip}(y_i, l_i, u_i) = \\min(u_i, \\max(l_i, y_i))</span>$$</p>

<p><span class="part">Part (c): Numerical Example</span><br>
Given $y = (-3, 5, 4)^\\top$, $l = (-1, 0, 2)^\\top$, $u = (2, 3, 5)^\\top$:
<ul>
  <li>Coordinate 1: $y_1 = -3 < l_1 = -1 \\implies [\\Pi_C(y)]_1 = -1$.</li>
  <li>Coordinate 2: $y_2 = 5 > u_2 = 3 \\implies [\\Pi_C(y)]_2 = 3$.</li>
  <li>Coordinate 3: $l_3 = 2 \\le y_3 = 4 \\le u_3 = 5 \\implies [\\Pi_C(y)]_3 = 4$.</li>
</ul>
<span class="ans">$$\\Pi_C(y) = \\begin{bmatrix} -1 \\\\ 3 \\\\ 4 \\end{bmatrix}$$</span></p>""",
        "takeaway": "Separable constraints enable coordinate-wise projections in $\\mathcal{O}(n)$ time. Box projection is simply componentwise saturation clipping."
    },
    {
        "id": 11393,
        "subject": "CMO",
        "topicId": "13_Projections_onto_Convex_Sets",
        "topicTitle": "13 · Projections onto Convex Sets",
        "title": "Firm Non-Expansiveness of Projections (Generated Exam)",
        "kind2": "practice",
        "source": "IISc / Bertsekas Benchmark",
        "marks": "[10 Marks]",
        "question": """<p>Let $C \\subset \\mathbb{R}^n$ be a non-empty closed convex set and let $\\Pi_C: \\mathbb{R}^n \\to C$ denote the projection operator.<br>
<span class="part">(a)</span> State the fundamental variational inequality characterization of $\\Pi_C(x)$.<br>
<span class="part">(b)</span> Prove that $\\Pi_C$ is <strong>firmly non-expansive</strong>:
$$\\|\\Pi_C(x) - \\Pi_C(y)\\|_2^2 \\le \\langle \\Pi_C(x) - \\Pi_C(y), \\; x - y \\rangle \\quad \\forall x, y \\in \\mathbb{R}^n$$
<span class="part">(c)</span> Deduce that $\\Pi_C$ is Lipschitz continuous with constant $L = 1$ (i.e. non-expansive: $\\|\\Pi_C(x) - \\Pi_C(y)\\|_2 \\le \\|x - y\\|_2$).</p>""",
        "solution": """<p><span class="part">Part (a): Variational Characterization</span><br>
A point $u \\in C$ is the projection $u = \\Pi_C(x)$ if and only if:
$$\\langle x - u, \\; z - u \\rangle \\le 0 \\quad \\forall z \\in C$$
Equivalently:
$$\\langle u - x, \\; u - z \\rangle \\le 0 \\quad \\forall z \\in C$$</p>

<p><span class="part">Part (b): Proof of Firm Non-Expansiveness</span><br>
Let $u = \\Pi_C(x) \\in C$ and $v = \\Pi_C(y) \\in C$.
<ol>
  <li>Apply the variational inequality for $u = \\Pi_C(x)$ with test point $z = v \\in C$:
  $$\\langle u - x, \\; u - v \\rangle \\le 0$$</li>
  <li>Apply the variational inequality for $v = \\Pi_C(y)$ with test point $z = u \\in C$:
  $$\\langle v - y, \\; v - u \\rangle \\le 0 \\iff \\langle y - v, \\; u - v \\rangle \\ge 0 \\iff \\langle v - y, \\; u - v \\rangle \\le 0$$</li>
</ol>
Add the two inequalities together:
$$\\langle (u - x) + (y - v), \\; u - v \\rangle \\le 0$$
Group the terms inside the first argument:
$$\\langle (u - v) - (x - y), \\; u - v \\rangle \\le 0$$
Expand by linearity of the inner product:
$$\\langle u - v, \\; u - v \\rangle - \\langle x - y, \\; u - v \\rangle \\le 0$$
$$\\|u - v\\|_2^2 \\le \\langle u - v, \\; x - y \\rangle$$
Substitute back $u = \\Pi_C(x)$ and $v = \\Pi_C(y)$:
$$<span class="ans">\\|\\Pi_C(x) - \\Pi_C(y)\\|_2^2 \\le \\langle \\Pi_C(x) - \\Pi_C(y), \\; x - y \\rangle</span> \\quad \\blacksquare$$</p>

<p><span class="part">Part (c): Standard Non-Expansiveness</span><br>
By Cauchy-Schwarz:
$$\\langle \\Pi_C(x) - \\Pi_C(y), \\; x - y \\rangle \\le \\|\\Pi_C(x) - \\Pi_C(y)\\|_2 \\|x - y\\|_2$$
Combining with firm non-expansiveness:
$$\\|\\Pi_C(x) - \\Pi_C(y)\\|_2^2 \\le \\|\\Pi_C(x) - \\Pi_C(y)\\|_2 \\|x - y\\|_2$$
Divide both sides by $\\|\\Pi_C(x) - \\Pi_C(y)\\|_2 > 0$:
$$<span class="ans">\\|\\Pi_C(x) - \\Pi_C(y)\\|_2 \\le \\|x - y\\|_2</span>$$
Thus $\\Pi_C$ is non-expansive (Lipschitz with $L = 1$). Firm non-expansiveness is strictly stronger, ensuring $\\Pi_C$ is a $1/2$-averaged operator.</p>""",
        "takeaway": "Firm non-expansiveness is the defining metric property of projections. It guarantees that projected gradient and proximal point iterations never blow up."
    },

    # =========================================================================
    # TOPIC 14: Gradient Projection Algorithm and Convergence
    # =========================================================================
    {
        "id": 11491,
        "subject": "CMO",
        "topicId": "14_Gradient_Projection_Algorithm_and_Convergence",
        "topicTitle": "14 · Gradient Projection Algorithm",
        "title": "Manual Gradient Projection Iteration (IISc Midterm 2024)",
        "kind2": "pyq",
        "source": "IISc Midterm 3 2024 / Bertsekas Ch 2",
        "marks": "[10 Marks]",
        "question": """<p>Consider the constrained quadratic minimization problem:
$$\\min f(x_1, x_2) = (x_1 - 2)^2 + (x_2 - 3)^2 \\quad \\text{subject to} \\quad x_1 \\ge 0, \\quad x_2 \\ge 0$$
Using the Gradient Projection algorithm with constant step size $\\alpha = 0.5$ starting from the origin $x_0 = (0, 0)^\\top$:<br>
<span class="part">(a)</span> Compute the gradient $\\nabla f(x_0)$ and the unprojected point $y_0 = x_0 - \\alpha \\nabla f(x_0)$.<br>
<span class="part">(b)</span> Project $y_0$ onto $C = \\mathbb{R}_+^2$ to obtain $x_1$.<br>
<span class="part">(c)</span> Perform the second iteration to find $x_2$. Show that the algorithm terminates exactly at the global minimum $x^*$.</p>""",
        "solution": """<p><span class="part">Part (a): Iteration 0 Unprojected Point</span><br>
$$\\nabla f(x) = \\begin{bmatrix} 2(x_1 - 2) \\\\[2pt] 2(x_2 - 3) \\end{bmatrix}$$
At $x_0 = (0, 0)^\\top$:
$$\\nabla f(0, 0) = \\begin{bmatrix} 2(0 - 2) \\\\[2pt] 2(0 - 3) \\end{bmatrix} = \\begin{bmatrix} -4 \\\\ -6 \\end{bmatrix}$$
Unprojected gradient step with $\\alpha = 0.5$:
$$y_0 = x_0 - \\alpha \\nabla f(x_0) = \\begin{bmatrix} 0 \\\\ 0 \\end{bmatrix} - 0.5 \\begin{bmatrix} -4 \\\\ -6 \\end{bmatrix} = <span class="ans">\\begin{bmatrix} 2 \\\\ 3 \\end{bmatrix}</span>$$</p>

<p><span class="part">Part (b): Projection onto $C = \\mathbb{R}_+^2$</span><br>
The projection onto the non-negative quadrant is $[\\Pi_C(y)]_i = \\max(0, y_i)$.
$$x_1 = \\Pi_C(y_0) = \\begin{bmatrix} \\max(0, 2) \\\\[2pt] \\max(0, 3) \\end{bmatrix} = <span class="ans">\\begin{bmatrix} 2 \\\\ 3 \\end{bmatrix}</span>$$</p>

<p><span class="part">Part (c): Iteration 1 and Termination</span><br>
Evaluate gradient at $x_1 = (2, 3)^\\top$:
$$\\nabla f(2, 3) = \\begin{bmatrix} 2(2 - 2) \\\\[2pt] 2(3 - 3) \\end{bmatrix} = \\begin{bmatrix} 0 \\\\ 0 \\end{bmatrix}$$
Unprojected point:
$$y_1 = x_1 - 0.5 \\nabla f(x_1) = \\begin{bmatrix} 2 \\\\ 3 \\end{bmatrix} - 0.5 \\begin{bmatrix} 0 \\\\ 0 \\end{bmatrix} = \\begin{bmatrix} 2 \\\\ 3 \\end{bmatrix}$$
Projecting gives:
$$x_2 = \\Pi_C(y_1) = \\begin{bmatrix} 2 \\\\ 3 \\end{bmatrix} = x_1$$
Since $x_2 = x_1$ and $\\nabla f(x_1) = 0$, $x_1 = (2, 3)^\\top$ is a fixed point:
$$x^* = \\Pi_C(x^* - \\alpha \\nabla f(x^*))$$
<span class="ans">The algorithm converges to the exact global minimizer $x^* = (2, 3)^\\top$ in just one step!</span></p>""",
        "takeaway": "Gradient projection seamlessly identifies when constraints are inactive: the unconstrained step lands directly in the interior, requiring zero boundary projection."
    },
    {
        "id": 11492,
        "subject": "CMO",
        "topicId": "14_Gradient_Projection_Algorithm_and_Convergence",
        "topicTitle": "14 · Gradient Projection Algorithm",
        "title": "Fixed-Point Characterization of Optimality (Stanford Boyd)",
        "kind2": "pyq",
        "source": "Stanford EE364a / Boyd Ch 9",
        "marks": "[8 Marks]",
        "question": """<p>Let $f: \\mathbb{R}^n \\to \\mathbb{R}$ be continuously differentiable and let $C \\subset \\mathbb{R}^n$ be a closed convex set.<br>
Prove that $x^* \\in C$ is a constrained stationary point:
$$\\nabla f(x^*)^\\top (x - x^*) \\ge 0 \\quad \\forall x \\in C$$
if and only if $x^*$ is a fixed point of the projected gradient operator for any scalar $\\alpha > 0$:
$$x^* = \\Pi_C(x^* - \\alpha \\nabla f(x^*))$$</p>""",
        "solution": """<p><span class="part">Step 1: Variational Characterization of Projections</span><br>
Recall that for any vector $z \\in \\mathbb{R}^n$, $u = \\Pi_C(z)$ if and only if $u \\in C$ and:
$$\\langle z - u, \\; x - u \\rangle \\le 0 \\quad \\forall x \\in C$$</p>

<p><span class="part">Step 2: Apply to the Projected Gradient Mapping</span><br>
Set $z = x^* - \\alpha \\nabla f(x^*)$ and test whether $u = x^*$ satisfies the projection condition.<br>
Evaluate the displacement $z - u$:
$$z - u = (x^* - \\alpha \\nabla f(x^*)) - x^* = -\\alpha \\nabla f(x^*)$$
Substitute this into the projection variational condition:
$$\\langle -\\alpha \\nabla f(x^*), \\; x - x^* \\rangle \\le 0 \\quad \\forall x \\in C$$</p>

<p><span class="part">Step 3: Factor out the Positive Step Size $\\alpha > 0$</span><br>
$$-\\alpha \\nabla f(x^*)^\\top (x - x^*) \\le 0 \\quad \\forall x \\in C$$
Since $\\alpha > 0$, divide both sides by $-\\alpha$ (which reverses the inequality):
$$<span class="ans">\\nabla f(x^*)^\\top (x - x^*) \\ge 0 \\quad \\forall x \\in C</span>$$
This is the First-Order Necessary Condition (FONC) for constrained optimality over a convex set.</p>

<p><span class="part">Conclusion:</span><br>
Since every step in the equivalence chain is bidirectional:
$$x^* = \\Pi_C(x^* - \\alpha \\nabla f(x^*)) \\iff \\nabla f(x^*)^\\top (x - x^*) \\ge 0 \\quad \\forall x \\in C$$
<span class="ans">A point is constrained stationary $\\iff$ it is a fixed point of the projected gradient operator.</span> $\\blacksquare$</p>""",
        "takeaway": "Constrained optimality is equivalent to a fixed point: $x^* = \\Pi_C(x^* - \\alpha \\nabla f(x^*))$. This enables testing convergence via the residual norm $\\|x_k - \\Pi_C(x_k - \\alpha \\nabla f(x_k))\\| < \\epsilon$."
    },
    {
        "id": 11493,
        "subject": "CMO",
        "topicId": "14_Gradient_Projection_Algorithm_and_Convergence",
        "topicTitle": "14 · Gradient Projection Algorithm",
        "title": "Projected Descent Lemma & Active Set Identification (Generated Exam)",
        "kind2": "practice",
        "source": "IISc / Bertsekas Benchmark",
        "marks": "[10 Marks]",
        "question": """<p>Let $f: \\mathbb{R}^n \\to \\mathbb{R}$ be continuously differentiable with $L$-Lipschitz continuous gradient on a closed convex set $C$.<br>
Consider the Projected Gradient iteration $x_{k+1} = \\Pi_C(x_k - \\alpha_k \\nabla f(x_k))$.<br>
<span class="part">(a)</span> Prove the <strong>Projected Descent Lemma</strong>:
$$f(x_{k+1}) \\le f(x_k) - \\left( \\frac{1}{\\alpha_k} - \\frac{L}{2} \\right) \\|x_{k+1} - x_k\\|_2^2$$
<span class="part">(b)</span> What is the maximum admissible constant step size $\\alpha$ that guarantees monotonic descent?<br>
<span class="part">(c)</span> Explain why Gradient Projection has the <strong>Finite Active Set Identification property</strong>, unlike interior-point methods.</p>""",
        "solution": """<p><span class="part">Part (a): Proof of Projected Descent Lemma</span><br>
By the Descent Lemma for $L$-smooth functions:
$$f(x_{k+1}) \\le f(x_k) + \\nabla f(x_k)^\\top (x_{k+1} - x_k) + \\frac{L}{2} \\|x_{k+1} - x_k\\|^2$$
We bound the inner product $\\nabla f(x_k)^\\top (x_{k+1} - x_k)$.<br>
By definition, $x_{k+1} = \\Pi_C(y_k)$ where $y_k = x_k - \\alpha_k \\nabla f(x_k)$.<br>
By the variational inequality of projections, for any $z \\in C$:
$$\\langle y_k - x_{k+1}, \\; z - x_{k+1} \\rangle \\le 0$$
Substitute $z = x_k \\in C$:
$$\\langle (x_k - \\alpha_k \\nabla f(x_k)) - x_{k+1}, \\; x_k - x_{k+1} \\rangle \\le 0$$
$$\\|x_k - x_{k+1}\\|^2 - \\alpha_k \\langle \\nabla f(x_k), \\; x_k - x_{k+1} \\rangle \\le 0$$
$$\\|x_{k+1} - x_k\\|^2 \\le \\alpha_k \\nabla f(x_k)^\\top (x_k - x_{k+1}) = -\\alpha_k \\nabla f(x_k)^\\top (x_{k+1} - x_k)$$
Divide by $\\alpha_k > 0$:
$$\\nabla f(x_k)^\\top (x_{k+1} - x_k) \\le -\\frac{1}{\\alpha_k} \\|x_{k+1} - x_k\\|^2$$
Substitute this bound back into the Descent Lemma:
$$f(x_{k+1}) \\le f(x_k) - \\frac{1}{\\alpha_k} \\|x_{k+1} - x_k\\|^2 + \\frac{L}{2} \\|x_{k+1} - x_k\\|^2 = <span class="ans">f(x_k) - \\left( \\frac{1}{\\alpha_k} - \\frac{L}{2} \\right) \\|x_{k+1} - x_k\\|^2</span> \\quad \\blacksquare$$</p>

<p><span class="part">Part (b): Admissible Step Size</span><br>
For strict descent, we require $\\frac{1}{\\alpha} - \\frac{L}{2} > 0 \\implies <span class="ans">0 < \\alpha < \\frac{2}{L}</span>$.<br>
The standard choice is $\\alpha = 1/L$, which yields guaranteed decrease $\\frac{L}{2}\\|x_{k+1} - x_k\\|^2$.</p>

<p><span class="part">Part (c): Finite Active Set Identification</span><br>
Under strict complementarity (for bound constraints $x_i \\ge 0$, $\\mu_i^* = \\nabla f(x^*)_i > 0$ for all $i \\in \\mathcal{A}(x^*)$):<br>
Near $x^*$, for $i \\in \\mathcal{A}(x^*)$:
$$x_{k, i} - \\alpha \\nabla f(x_k)_i \\approx 0 - \\alpha \\mu_i^* < 0$$
Since this unprojected value is strictly negative, the projection operator $\\Pi_C$ clips it to exactly zero:
$$x_{k+1, i} = \\max(0, x_{k, i} - \\alpha \\nabla f(x_k)_i) = 0$$
<span class="ans">All true active constraints become exact equalities in a finite number of iterations!</span><br>
Once identified, the algorithm can switch to an unconstrained Newton method on the subspace for quadratic convergence.</p>""",
        "takeaway": "Projected gradient drops onto the true active constraint manifold in a finite number of steps, enabling rapid two-phase acceleration algorithms."
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
    
    js_content = "/* Practice Questions Database for CMO (Topics 01-14) */\n"
    js_content += "window.PRACTICE_DATA = window.PRACTICE_DATA || [];\n\n"
    js_content += "window.PRACTICE_DATA.push(\n"
    js_content += json.dumps(combined, indent=2)
    js_content += "\n);\n"
    
    with open(target_file, "w", encoding="utf-8") as f:
        f.write(js_content)
        
    print(f"Successfully updated {target_file}! Total practice cards: {len(combined)}")

if __name__ == "__main__":
    main()
