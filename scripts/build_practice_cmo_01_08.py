#!/usr/bin/env python3
"""
build_practice_cmo_01_08.py
Generates practice questions (flippable cards) for CMO Topics 01 through 08.
Each topic includes:
  - P1: IISc University Exam PYQ (from Midterm 1, Midterm 2, Midterm 3, or Endsem)
  - P2: Stanford / MIT / Berkeley / Boyd / Bertsekas University Exam PYQ
  - P3: Generated Master Exam-Level Problem of the same caliber and depth

All cards follow the photographic memory Sirianni card format with rich KaTeX math,
step-by-step solutions, key takeaways, and question/solution dual faces.
"""

import json
import os

PRACTICE_CARDS = [
    # =========================================================================
    # TOPIC 01: Mathematical Preliminaries & Weierstrass
    # =========================================================================
    {
        "id": 10191,
        "subject": "CMO",
        "topicId": "01_Mathematical_Preliminaries_Topology_and_Weierstrass",
        "topicTitle": "01 · Mathematical Preliminaries & Weierstrass",
        "title": "Coercivity & Weierstrass EVT (IISc Midterm 2024)",
        "kind2": "pyq",
        "source": "IISc Midterm 1 2024 / Luenberger Ch 7",
        "marks": "[8 Marks]",
        "question": """<p><span class="part">(a)</span> Define what it means for a continuous function $f: \\mathbb{R}^n \\to \\mathbb{R}$ to be <strong>coercive</strong>.</p>
<p><span class="part">(b)</span> Consider the polynomial objective:
$$f(x_1, x_2) = x_1^4 + x_2^4 - 4x_1 x_2$$
Prove rigorously that $f$ is coercive on $\\mathbb{R}^2$.</p>
<p><span class="part">(c)</span> Using the Weierstrass Extreme Value Theorem, deduce that $f$ attains a finite global minimum on $\\mathbb{R}^2$.</p>""",
        "solution": """<p><span class="part">Step 1: Definition of Coercivity</span><br>
A continuous function $f: \\mathbb{R}^n \\to \\mathbb{R}$ is coercive if:
$$\\lim_{\\|x\\|_2 \\to \\infty} f(x) = +\\infty$$
Equivalently, for every $M \\in \\mathbb{R}$, there exists an $R > 0$ such that $\\|x\\|_2 > R \\implies f(x) > M$.</p>

<p><span class="part">Step 2: Proof of Coercivity</span><br>
By the arithmetic-geometric mean (AM-GM) inequality or Young's inequality:
$$4|x_1 x_2| \\le 2(x_1^2 + x_2^2) = 2\\|x\\|_2^2$$
Next, by the power-mean / Cauchy-Schwarz inequality on coordinates:
$$x_1^4 + x_2^4 \\ge \\frac{1}{2}(x_1^2 + x_2^2)^2 = \\frac{1}{2}\\|x\\|_2^4$$
Combining these lower bounds:
$$f(x_1, x_2) \\ge \\frac{1}{2}\\|x\\|_2^4 - 2\\|x\\|_2^2 = \\|x\\|_2^2 \\left( \\frac{1}{2}\\|x\\|_2^2 - 2 \\right)$$
As $\\|x\\|_2 \\to \\infty$, the factor $\\left(\\frac{1}{2}\\|x\\|_2^2 - 2\\right) \\to +\\infty$. Therefore:
$$\\lim_{\\|x\\|_2 \\to \\infty} f(x) = +\\infty$$
<span class="ans">Thus $f$ is coercive on $\\mathbb{R}^2$.</span></p>

<p><span class="part">Step 3: Existence of Global Minimum</span><br>
Pick any point $x_0 = (0, 0)$, where $f(0, 0) = 0$. Consider the sublevel set:
$$S_0 = \\{x \\in \\mathbb{R}^2 : f(x) \\le f(x_0) = 0\\}$$
1. Since $f$ is continuous, $S_0 = f^{-1}((-\\infty, 0])$ is <strong>closed</strong>.<br>
2. Since $f$ is coercive, $S_0$ is <strong>bounded</strong> (for $\\|x\\|_2 > 2$, $f(x) > 0$, so $S_0 \\subset B_2(0)$).<br>
By the Heine-Borel Theorem, $S_0$ is <strong>compact</strong>.<br>
By Weierstrass EVT, continuous $f$ attains a minimum $x^*$ on compact $S_0$. Since $f(x) > 0 \\ge f(x^*)$ for all $x \\notin S_0$, $x^*$ is a <span class="ans">global minimum on all of $\\mathbb{R}^2$</span>.</p>""",
        "takeaway": "Coercivity converts an open unconstrained search over $\\mathbb{R}^n$ into an optimization problem over a compact sublevel set $S_0$, where Weierstrass guarantees existence."
    },
    {
        "id": 10192,
        "subject": "CMO",
        "topicId": "01_Mathematical_Preliminaries_Topology_and_Weierstrass",
        "topicTitle": "01 · Mathematical Preliminaries & Weierstrass",
        "title": "Sublevel Set Characterization of Coercivity (Stanford Boyd)",
        "kind2": "pyq",
        "source": "Stanford EE364a / Boyd Ch 3",
        "marks": "[10 Marks]",
        "question": """<p>Let $f: \\mathbb{R}^n \\to \\mathbb{R}$ be a continuous function. For any $\\alpha \\in \\mathbb{R}$, define the $\\alpha$-sublevel set:
$$S_\\alpha = \\{x \\in \\mathbb{R}^n : f(x) \\le \\alpha\\}$$
Prove that $f$ is coercive if and only if for every $\\alpha \\in \\mathbb{R}$, the sublevel set $S_\\alpha$ is compact (closed and bounded in $\\mathbb{R}^n$).</p>""",
        "solution": """<p><span class="part">Preliminary: Closedness</span><br>
For any continuous function $f$, the sublevel set $S_\\alpha = f^{-1}((-\\infty, \\alpha])$ is the preimage of the closed set $(-\\infty, \\alpha] \\subset \\mathbb{R}$, so $S_\\alpha$ is always closed for any $\\alpha \\in \\mathbb{R}$. Thus by Heine-Borel, $S_\\alpha$ is compact $\\iff$ $S_\\alpha$ is bounded.</p>

<p><span class="part">Forward Direction: $(\\implies)$ Assume $f$ is coercive</span><br>
Suppose for contradiction that there exists some $\\hat{\\alpha} \\in \\mathbb{R}$ such that $S_{\\hat{\\alpha}}$ is unbounded.<br>
Then there exists a sequence $\\{x_k\\} \\subset S_{\\hat{\\alpha}}$ such that $\\|x_k\\| \\to \\infty$ as $k \\to \\infty$.<br>
By definition of $S_{\\hat{\\alpha}}$, $f(x_k) \\le \\hat{\\alpha}$ for all $k$.<br>
However, because $f$ is coercive and $\\|x_k\\| \\to \\infty$, we must have:
$$\\lim_{k \\to \\infty} f(x_k) = +\\infty$$
This contradicts $f(x_k) \\le \\hat{\\alpha} < \\infty$ for all $k$.<br>
<span class="ans">Therefore, every sublevel set $S_\\alpha$ must be bounded, and hence compact.</span></p>

<p><span class="part">Reverse Direction: $(\\impliedby)$ Assume every $S_\\alpha$ is compact</span><br>
Let $M \\in \\mathbb{R}$ be arbitrary. Consider the sublevel set $S_M = \\{x : f(x) \\le M\\}$.<br>
By hypothesis, $S_M$ is bounded, so there exists some radius $R_M > 0$ such that:
$$S_M \\subset \\{x \\in \\mathbb{R}^n : \\|x\\| \\le R_M\\}$$
Taking contrapositives:
$$\\|x\\| > R_M \\implies x \\notin S_M \\implies f(x) > M$$
Since for every $M \\in \\mathbb{R}$, there exists $R_M$ such that $\\|x\\| > R_M \\implies f(x) > M$, it follows by definition that:
$$\\lim_{\\|x\\| \\to \\infty} f(x) = +\\infty$$
<span class="ans">Hence $f$ is coercive.</span> $\\blacksquare$</p>""",
        "takeaway": "Coercivity is topological: it means every sublevel set is trapped inside a finite sphere. In convex analysis, sublevel set boundedness is the standard test for well-posedness."
    },
    {
        "id": 10193,
        "subject": "CMO",
        "topicId": "01_Mathematical_Preliminaries_Topology_and_Weierstrass",
        "topicTitle": "01 · Mathematical Preliminaries & Weierstrass",
        "title": "Quadratic Coercivity vs. Singular Solvability (Generated Exam)",
        "kind2": "practice",
        "source": "IISc / Berkeley Benchmark",
        "marks": "[10 Marks]",
        "question": """<p>Let $A \\in \\mathbb{R}^{n \\times n}$ be symmetric positive semidefinite ($A \\succeq 0$), and let $b \\in \\mathbb{R}^n$. Consider the quadratic objective:
$$f(x) = \\frac{1}{2} x^\\top A x - b^\\top x$$
<span class="part">(a)</span> Prove that $f$ is coercive on $\\mathbb{R}^n$ if and only if $A$ is strictly positive definite ($A \\succ 0$).<br>
<span class="part">(b)</span> Suppose $A$ is singular (has at least one zero eigenvalue). Under what exact necessary and sufficient condition on $b$ does $f$ still achieve a finite global minimum on $\\mathbb{R}^n$?</p>""",
        "solution": """<p><span class="part">Part (a): Coercivity $\\iff A \\succ 0$</span><br>
$(\\impliedby)$ If $A \\succ 0$, let $\\lambda_{\\min} > 0$ be the smallest eigenvalue. By Rayleigh quotient and Cauchy-Schwarz:
$$f(x) \\ge \\frac{\\lambda_{\\min}}{2} \\|x\\|_2^2 - \\|b\\|_2 \\|x\\|_2 = \\|x\\|_2 \\left( \\frac{\\lambda_{\\min}}{2}\\|x\\|_2 - \\|b\\|_2 \\right) \\to +\\infty \\text{ as } \\|x\\|_2 \\to \\infty$$
$(\\implies)$ If $A$ is singular, $\\exists v \\ne 0$ with $Av = 0$. Consider the ray $x(t) = tv$ for $t > 0$:
$$f(tv) = \\frac{1}{2} t^2 (v^\\top A v) - t(b^\\top v) = -t(b^\\top v)$$
If $b^\\top v \\ne 0$, choosing $t \\to \\infty$ with appropriate sign gives $f(tv) \\to -\\infty$. If $b^\\top v = 0$, $f(tv) = 0$ for all $t$, which is bounded, not $+\infty$. Thus $f$ is <span class="ans">never coercive if $A$ has a zero eigenvalue</span>.</p>

<p><span class="part">Part (b): Solvability when $A$ is Singular</span><br>
For $f$ to attain a minimum, $f$ must be bounded below along the nullspace $\\ker(A)$.<br>
Along any $v \\in \\ker(A)$, $f(x + tv) = f(x) - t(b^\\top v)$. This linear function is bounded below on $\\mathbb{R}$ if and only if:
$$b^\\top v = 0 \\quad \\forall v \\in \\ker(A)$$
By the Fundamental Theorem of Linear Algebra:
$$\\ker(A)^\\perp = \\operatorname{range}(A^\\top) = \\operatorname{range}(A)$$
Therefore, $b^\\top v = 0 \\; \\forall v \\in \\ker(A) \\iff <span class="ans">b \\in \\operatorname{range}(A)</span>$.</p>

<p><span class="part">Verification of Minimizer:</span><br>
If $b \\in \\operatorname{range}(A)$, there exists $x^* \\in \\mathbb{R}^n$ such that $Ax^* = b$. Then:
$$f(x) - f(x^*) = \\frac{1}{2}(x - x^*)^\\top A (x - x^*) \\ge 0 \\quad (\\text{since } A \\succeq 0)$$
Thus $x^*$ is a finite global minimizer (non-unique; the set of minimizers is $x^* + \\ker(A)$).</p>""",
        "takeaway": "A singular quadratic cannot be coercive, but it still attains a minimum if and only if $b \\in \\operatorname{range}(A)$ (the linear system $Ax = b$ is consistent)."
    },

    # =========================================================================
    # TOPIC 02: Multivariate Taylor Series & Optimality Conditions
    # =========================================================================
    {
        "id": 10291,
        "subject": "CMO",
        "topicId": "02_Multivariate_Taylor_Series_and_Optimality_Conditions",
        "topicTitle": "02 · Multivariate Taylor Series & Optimality",
        "title": "Stationary Point Classification (IISc Midterm 2023)",
        "kind2": "pyq",
        "source": "IISc Midterm 1 2023 / Nocedal & Wright Ch 2",
        "marks": "[10 Marks]",
        "question": """<p>Consider the function $f: \\mathbb{R}^2 \\to \\mathbb{R}$:
$$f(x_1, x_2) = 2x_1^3 + x_1 x_2^2 + 5x_1^2 + x_2^2$$
<span class="part">(a)</span> Compute the gradient $\\nabla f(x)$ and locate all four stationary points of $f$.<br>
<span class="part">(b)</span> Compute the Hessian matrix $\\nabla^2 f(x)$.<br>
<span class="part">(c)</span> Classify each stationary point as a local minimum, local maximum, or saddle point using second-order conditions.</p>""",
        "solution": """<p><span class="part">Step 1: First-Order Necessary Condition (FONC)</span><br>
$$\\nabla f(x) = \\begin{bmatrix} \\frac{\\partial f}{\\partial x_1} \\\\[4pt] \\frac{\\partial f}{\\partial x_2} \\end{bmatrix} = \\begin{bmatrix} 6x_1^2 + x_2^2 + 10x_1 \\\\[4pt] 2x_1 x_2 + 2x_2 \\end{bmatrix} = \\begin{bmatrix} 0 \\\\ 0 \\end{bmatrix}$$
From the second equation: $2x_2(x_1 + 1) = 0 \\implies x_2 = 0 \\text{ or } x_1 = -1$.
<ul>
  <li><strong>Case A:</strong> $x_2 = 0$. First equation becomes $6x_1^2 + 10x_1 = 2x_1(3x_1 + 5) = 0 \\implies x_1 = 0$ or $x_1 = -5/3$.<br>
  Points: <span class="ans">$(0, 0)$</span> and <span class="ans">$(-5/3, 0)$</span>.</li>
  <li><strong>Case B:</strong> $x_1 = -1$. First equation becomes $6(-1)^2 + x_2^2 + 10(-1) = x_2^2 - 4 = 0 \\implies x_2 = \\pm 2$.<br>
  Points: <span class="ans">$(-1, 2)$</span> and <span class="ans">$(-1, -2)$</span>.</li>
</ul></p>

<p><span class="part">Step 2: Hessian Matrix</span><br>
$$\\nabla^2 f(x) = \\begin{bmatrix} 12x_1 + 10 & 2x_2 \\\\ 2x_2 & 2x_1 + 2 \\end{bmatrix}$$</p>

<p><span class="part">Step 3: Classification</span><br>
1. <strong>At $(0, 0)$:</strong> $\\nabla^2 f(0, 0) = \\begin{bmatrix} 10 & 0 \\\\ 0 & 2 \\end{bmatrix} \\succ 0$ (eigenvalues $10, 2 > 0$).<br>
<span class="ans">Strict Local Minimum</span> ($f(0, 0) = 0$).<br>
2. <strong>At $(-5/3, 0)$:</strong> $\\nabla^2 f(-5/3, 0) = \\begin{bmatrix} -10 & 0 \\\\ 0 & -4/3 \\end{bmatrix} \\prec 0$ (eigenvalues $-10, -4/3 < 0$).<br>
<span class="ans">Strict Local Maximum</span> ($f(-5/3, 0) = 125/27$).<br>
3. <strong>At $(-1, 2)$:</strong> $\\nabla^2 f(-1, 2) = \\begin{bmatrix} -2 & 4 \\\\ 4 & 0 \\end{bmatrix}$. Determinant $= 0 - 16 = -16 < 0$. Indefinite.<br>
<span class="ans">Saddle Point</span> ($f(-1, 2) = 3$).<br>
4. <strong>At $(-1, -2)$:</strong> $\\nabla^2 f(-1, -2) = \\begin{bmatrix} -2 & -4 \\\\ -4 & 0 \\end{bmatrix}$. Determinant $= 0 - 16 = -16 < 0$. Indefinite.<br>
<span class="ans">Saddle Point</span> ($f(-1, -2) = 3$).</p>""",
        "takeaway": "Factor the gradient equations completely to avoid missing solutions. A negative Hessian determinant in 2D immediately diagnoses a saddle point without needing to compute eigenvalues."
    },
    {
        "id": 10292,
        "subject": "CMO",
        "topicId": "02_Multivariate_Taylor_Series_and_Optimality_Conditions",
        "topicTitle": "02 · Multivariate Taylor Series & Optimality",
        "title": "Rigorous Proof of SONC (Stanford Boyd)",
        "kind2": "pyq",
        "source": "Stanford EE364a / Boyd Ch 2",
        "marks": "[8 Marks]",
        "question": """<p>Let $f: \\mathbb{R}^n \\to \\mathbb{R}$ be twice continuously differentiable ($C^2$).<br>
Prove the <strong>Second-Order Necessary Condition (SONC)</strong>: if $x^*$ is a local minimizer of $f$, then:
$$\\nabla f(x^*) = 0 \\quad \\text{and} \\quad \\nabla^2 f(x^*) \\succeq 0 \\text{ (positive semidefinite)}$$
Provide a completely rigorous $\\epsilon$-$\\delta$ or limit proof based on multivariate Taylor expansion.</p>""",
        "solution": """<p><span class="part">Step 1: First-Order Condition</span><br>
Since $x^*$ is a local minimizer, along any ray $x(t) = x^* + t d$ ($d \\in \\mathbb{R}^n, t \\in \\mathbb{R}$), the 1D function $g(t) = f(x^* + t d)$ has a local minimum at $t = 0$. Thus $g'(0) = \\nabla f(x^*)^\\top d = 0$. Since this holds for all $d \\in \\mathbb{R}^n$, we must have $\\nabla f(x^*) = 0$.</p>

<p><span class="part">Step 2: Taylor Expansion with Integral Remainder</span><br>
By Taylor's theorem around $x^*$, for any direction $d \\in \\mathbb{R}^n$ and $t > 0$:
$$f(x^* + t d) = f(x^*) + t \\nabla f(x^*)^\\top d + \\frac{t^2}{2} d^\\top \\nabla^2 f(x^*) d + o(t^2)$$
Using $\\nabla f(x^*) = 0$:
$$f(x^* + t d) - f(x^*) = \\frac{t^2}{2} d^\\top \\nabla^2 f(x^*) d + o(t^2)$$</p>

<p><span class="part">Step 3: Isolating Curvature via Limit</span><br>
Since $x^*$ is a local minimizer, there exists $\\epsilon > 0$ such that for all $t \\in (0, \\epsilon)$:
$$f(x^* + t d) - f(x^*) \\ge 0$$
Dividing both sides by $t^2 > 0$:
$$\\frac{f(x^* + t d) - f(x^*)}{t^2} = \\frac{1}{2} d^\\top \\nabla^2 f(x^*) d + \\frac{o(t^2)}{t^2} \\ge 0$$
Taking the limit as $t \\to 0^+$:
$$\\lim_{t \\to 0^+} \\left( \\frac{1}{2} d^\\top \\nabla^2 f(x^*) d + \\frac{o(t^2)}{t^2} \\right) = \\frac{1}{2} d^\\top \\nabla^2 f(x^*) d \\ge 0$$
Multiplying by 2:
$$d^\\top \\nabla^2 f(x^*) d \\ge 0$$
Since direction $d \\in \\mathbb{R}^n$ was arbitrary, this holds for all $d \\in \\mathbb{R}^n$.<br>
<span class="ans">Therefore, $\\nabla^2 f(x^*) \\succeq 0$ (positive semidefinite).</span> $\\blacksquare$</p>""",
        "takeaway": "Dividing the Taylor error by $t^2$ and taking $t \\to 0$ suppresses all higher-order terms, revealing the quadratic curvature must be non-negative."
    },
    {
        "id": 10293,
        "subject": "CMO",
        "topicId": "02_Multivariate_Taylor_Series_and_Optimality_Conditions",
        "topicTitle": "02 · Multivariate Taylor Series & Optimality",
        "title": "Peano Counterexample & Directional Limits (Generated Exam)",
        "kind2": "practice",
        "source": "IISc / Bertsekas Benchmark",
        "marks": "[10 Marks]",
        "question": """<p>Consider Peano's classic polynomial function:
$$f(x_1, x_2) = (x_2 - x_1^2)(x_2 - 2x_1^2)$$
<span class="part">(a)</span> Show that along <em>every straight line</em> passing through the origin $x(t) = (c_1 t, c_2 t)$ ($t \\in \\mathbb{R}$), $t = 0$ is a strict local minimum of $g(t) = f(c_1 t, c_2 t)$.<br>
<span class="part">(b)</span> Prove that $(0, 0)$ is <em>not</em> a local minimum of $f$ on $\\mathbb{R}^2$ by constructing a curved trajectory along which $f(x) < 0$.<br>
<span class="part">(c)</span> Why does this phenomenon not contradict the Second-Order Necessary Condition?</p>""",
        "solution": """<p><span class="part">Part (a): Straight-Line Directional Analysis</span><br>
Substitute $x_1 = c_1 t, x_2 = c_2 t$ into $f$:
$$g(t) = (c_2 t - c_1^2 t^2)(c_2 t - 2c_1^2 t^2)$$
<ul>
  <li><strong>Case 1 ($c_2 \\ne 0$):</strong> Expanding gives $g(t) = c_2^2 t^2 - 3c_1^2 c_2 t^3 + 2c_1^4 t^4$.<br>
  $g'(0) = 0$ and $g''(0) = 2c_2^2 > 0$. By 1D second-order sufficiency, $t = 0$ is a strict local minimum!</li>
  <li><strong>Case 2 ($c_2 = 0$, $x_1$-axis):</strong> $g(t) = (-c_1^2 t^2)(-2c_1^2 t^2) = 2c_1^4 t^4 > 0$ for all $t \\ne 0$. So $t = 0$ is again a strict local minimum!</li>
</ul>
Thus along every straight line through the origin, $(0,0)$ is a strict local minimum.</p>

<p><span class="part">Part (b): Parabolic Counter-Trajectory</span><br>
Notice that $f(x_1, x_2) < 0$ precisely when the two factors have opposite signs:
$$x_1^2 < x_2 < 2x_1^2$$
Consider the parabola running straight down this channel: $x_2 = \\frac{3}{2} x_1^2$.
$$f\\left(x_1, \\frac{3}{2}x_1^2\\right) = \\left(\\frac{3}{2}x_1^2 - x_1^2\\right)\\left(\\frac{3}{2}x_1^2 - 2x_1^2\\right) = \\left(\\frac{1}{2}x_1^2\\right)\\left(-\\frac{1}{2}x_1^2\\right) = -\\frac{1}{4}x_1^4 < 0 \\quad \\forall x_1 \\ne 0$$
Since $f(0, 0) = 0$ and every neighborhood $B_\\epsilon(0, 0)$ contains points on this parabola with $f < 0$, <span class="ans">$(0, 0)$ is a saddle point, NOT a local minimum</span>.</p>

<p><span class="part">Part (c): Reconciling with SONC</span><br>
Computing the Hessian at the origin:
$$\\nabla^2 f(0, 0) = \\begin{bmatrix} 0 & 0 \\\\ 0 & 2 \\end{bmatrix} \\succeq 0$$
The Hessian is positive <em>semidefinite</em> (eigenvalues $0$ and $2$). SONC only says $\\nabla^2 f(x^*) \\succeq 0$ is <em>necessary</em>; it is NOT sufficient when a zero eigenvalue exists!</p>""",
        "takeaway": "Directional derivatives only probe straight lines. When the Hessian is singular, curvature along parabolic curves $x_2 \\propto x_1^2$ can create descent valleys invisible to straight lines."
    },

    # =========================================================================
    # TOPIC 03: Convexity & Strong Convexity
    # =========================================================================
    {
        "id": 10391,
        "subject": "CMO",
        "topicId": "03_Convexity_and_Strong_Convexity",
        "topicTitle": "03 · Convexity & Strong Convexity",
        "title": "Polyak-Łojasiewicz Inequality (IISc Endsem 2023)",
        "kind2": "pyq",
        "source": "IISc Endsem 2023 / Boyd Ch 3",
        "marks": "[10 Marks]",
        "question": """<p>Let $f: \\mathbb{R}^n \\to \\mathbb{R}$ be continuously differentiable and $\\mu$-strongly convex ($\\mu > 0$). Let $x^*$ denote its unique global minimizer.<br>
<span class="part">(a)</span> State the first-order definition of $\\mu$-strong convexity.<br>
<span class="part">(b)</span> Prove the <strong>Polyak-Łojasiewicz (PL) inequality</strong>:
$$\\frac{1}{2\\mu} \\|\\nabla f(x)\\|_2^2 \\ge f(x) - f(x^*) \\quad \\forall x \\in \\mathbb{R}^n$$
<span class="part">(c)</span> Deduce that any stationary point $\\nabla f(\\bar{x}) = 0$ must be the global minimizer.</p>""",
        "solution": """<p><span class="part">Part (a): First-Order Characterization</span><br>
A function $f$ is $\\mu$-strongly convex if for all $x, y \\in \\mathbb{R}^n$:
$$f(y) \\ge f(x) + \\nabla f(x)^\\top (y - x) + \\frac{\\mu}{2} \\|y - x\\|_2^2$$</p>

<p><span class="part">Part (b): Proof of PL Inequality</span><br>
Hold $x$ fixed and consider the right-hand side as a quadratic function of $y$:
$$q(y) = f(x) + \\nabla f(x)^\\top (y - x) + \\frac{\\mu}{2} \\|y - x\\|_2^2$$
To find the minimum of $q(y)$ over all $y \\in \\mathbb{R}^n$, take the gradient with respect to $y$:
$$\\nabla_y q(y) = \\nabla f(x) + \\mu (y - x) = 0 \\implies y^* = x - \\frac{1}{\\mu} \\nabla f(x)$$
Substitute this optimal $y^*$ back into $q(y)$:
$$q(y^*) = f(x) + \\nabla f(x)^\\top \\left(-\\frac{1}{\\mu}\\nabla f(x)\\right) + \\frac{\\mu}{2} \\left\\|-\\frac{1}{\\mu}\\nabla f(x)\\right\\|^2 = f(x) - \\frac{1}{2\\mu} \\|\\nabla f(x)\\|_2^2$$
Since $f(y) \\ge q(y)$ for all $y$, taking the infimum of both sides over $y \\in \\mathbb{R}^n$:
$$\\inf_{y} f(y) \\ge \\min_{y} q(y) \\implies f(x^*) \\ge f(x) - \\frac{1}{2\\mu} \\|\\nabla f(x)\\|_2^2$$
Rearranging terms yields the PL inequality:
$$<span class="ans">f(x) - f(x^*) \\le \\frac{1}{2\\mu} \\|\\nabla f(x)\\|_2^2</span> \\quad \\blacksquare$$</p>

<p><span class="part">Part (c): Stationarity Implies Global Optimality</span><br>
If $\\nabla f(\\bar{x}) = 0$, then:
$$0 \\le f(\\bar{x}) - f(x^*) \\le \\frac{1}{2\\mu} \\|\\nabla f(\\bar{x})\\|_2^2 = \\frac{1}{2\\mu} (0) = 0$$
Hence $f(\\bar{x}) = f(x^*)$, so $\\bar{x}$ must be the global minimizer.</p>""",
        "takeaway": "Minimizing the quadratic lower bound of strong convexity gives the PL inequality, which guarantees that small gradient norm translates directly into near-optimal function value."
    },
    {
        "id": 10392,
        "subject": "CMO",
        "topicId": "03_Convexity_and_Strong_Convexity",
        "topicTitle": "03 · Convexity & Strong Convexity",
        "title": "Pointwise Maximum & Epigraph Geometry (Stanford Boyd)",
        "kind2": "pyq",
        "source": "Stanford EE364a / Boyd Ch 3",
        "marks": "[8 Marks]",
        "question": """<p>Let $f_1, f_2, \\dots, f_m: \\mathbb{R}^n \\to \\mathbb{R}$ be convex functions.<br>
<span class="part">(a)</span> Define the epigraph $\\operatorname{epi}(f)$ of an arbitrary function $f$.<br>
<span class="part">(b)</span> Prove that the epigraph of the pointwise maximum function $f(x) = \\max_{i=1,\\dots,m} f_i(x)$ is the intersection of the epigraphs:
$$\\operatorname{epi}(f) = \\bigcap_{i=1}^m \\operatorname{epi}(f_i)$$
<span class="part">(c)</span> Deduce that $f(x)$ is convex.</p>""",
        "solution": """<p><span class="part">Part (a): Epigraph Definition</span><br>
The epigraph of a function $f: \\mathbb{R}^n \\to \\mathbb{R}$ is the set of points lying on or above its graph:
$$\\operatorname{epi}(f) = \\{(x, t) \\in \\mathbb{R}^n \\times \\mathbb{R} : f(x) \\le t\\}$$</p>

<p><span class="part">Part (b): Epigraph Intersection Identity</span><br>
Let $(x, t) \\in \\mathbb{R}^n \\times \\mathbb{R}$. Then:
$$(x, t) \\in \\operatorname{epi}(f) \\iff f(x) \\le t$$
Since $f(x) = \\max_{i=1,\\dots,m} f_i(x)$, the maximum is $\\le t$ if and only if each individual component is $\\le t$:
$$\\max_{i=1,\\dots,m} f_i(x) \\le t \\iff f_i(x) \\le t \\quad \\forall i \\in \\{1, 2, \\dots, m\\}$$
By definition of epigraph:
$$f_i(x) \\le t \\iff (x, t) \\in \\operatorname{epi}(f_i)$$
Therefore:
$$(x, t) \\in \\operatorname{epi}(f) \\iff (x, t) \\in \\operatorname{epi}(f_i) \\; \\forall i \\iff <span class="ans">(x, t) \\in \\bigcap_{i=1}^m \\operatorname{epi}(f_i)</span>$$
This establishes the set equality $\\operatorname{epi}(f) = \\bigcap_{i=1}^m \\operatorname{epi}(f_i)$.</p>

<p><span class="part">Part (c): Convexity of $f$</span><br>
1. A function is convex if and only if its epigraph is a convex set.<br>
2. Since each $f_i$ is convex, each $\\operatorname{epi}(f_i)$ is a convex set in $\\mathbb{R}^{n+1}$.<br>
3. The intersection of any collection of convex sets is always convex.<br>
Thus $\\operatorname{epi}(f)$ is a convex set, which proves <span class="ans">$f$ is convex</span>. $\\blacksquare$</p>""",
        "takeaway": "Pointwise maximum in function space corresponds to set intersection in epigraph space. Since convexity is preserved under intersection, maximum operations preserve convexity automatically."
    },
    {
        "id": 10393,
        "subject": "CMO",
        "topicId": "03_Convexity_and_Strong_Convexity",
        "topicTitle": "03 · Convexity & Strong Convexity",
        "title": "Co-Coercivity & Baillon-Haddad Theorem (Generated Exam)",
        "kind2": "practice",
        "source": "IISc / Berkeley Benchmark",
        "marks": "[10 Marks]",
        "question": """<p>Let $f: \\mathbb{R}^n \\to \\mathbb{R}$ be continuously differentiable and convex, with $L$-Lipschitz continuous gradient ($\\|\\nabla f(x) - \\nabla f(y)\\| \\le L \\|x - y\\|$).<br>
<span class="part">(a)</span> State the Descent Lemma applied to $f$.<br>
<span class="part">(b)</span> Prove the <strong>Co-coercivity inequality</strong> (also known as the Baillon-Haddad theorem for convex functions):
$$(\\nabla f(x) - \\nabla f(y))^\\top (x - y) \\ge \\frac{1}{L} \\|\\nabla f(x) - \\nabla f(y)\\|_2^2 \\quad \\forall x, y \\in \\mathbb{R}^n$$
<span class="part">(c)</span> Contrast this with standard monotonicity $(\\nabla f(x) - \\nabla f(y))^\\top (x - y) \\ge 0$.</p>""",
        "solution": """<p><span class="part">Part (a): Descent Lemma</span><br>
For any $L$-smooth function $f$:
$$f(y) \\le f(x) + \\nabla f(x)^\\top (y - x) + \\frac{L}{2} \\|y - x\\|_2^2$$</p>

<p><span class="part">Part (b): Proof of Co-coercivity</span><br>
Fix $x \\in \\mathbb{R}^n$. Define the shifted convex function $\\phi(z) = f(z) - \\nabla f(x)^\\top z$.<br>
Notice that $\\nabla \\phi(z) = \\nabla f(z) - \\nabla f(x)$. Hence $\\nabla \\phi(x) = 0$, meaning $z = x$ is a global minimizer of $\\phi$.<br>
Since $\\phi$ also has $L$-Lipschitz gradient, the Descent Lemma applied to $\\phi$ at any point $y$ yields:
$$\\phi(x) = \\min_z \\phi(z) \\le \\phi\\left(y - \\frac{1}{L}\\nabla \\phi(y)\\right) \\le \\phi(y) - \\frac{1}{2L} \\|\\nabla \\phi(y)\\|^2$$
Substitute $\\phi(z) = f(z) - \\nabla f(x)^\\top z$:
$$f(x) - \\nabla f(x)^\\top x \\le f(y) - \\nabla f(x)^\\top y - \\frac{1}{2L} \\|\\nabla f(y) - \\nabla f(x)\\|^2$$
Rearranging:
$$f(y) \\ge f(x) + \\nabla f(x)^\\top (y - x) + \\frac{1}{2L} \\|\\nabla f(x) - \\nabla f(y)\\|^2$$
Now write down the exact same inequality with $x$ and $y$ swapped:
$$f(x) \\ge f(y) + \\nabla f(y)^\\top (x - y) + \\frac{1}{2L} \\|\\nabla f(x) - \\nabla f(y)\\|^2$$
Adding these two inequalities together:
$$0 \\ge (\\nabla f(x) - \\nabla f(y))^\\top (y - x) + \\frac{1}{L} \\|\\nabla f(x) - \\nabla f(y)\\|^2$$
Rearranging gives the co-coercivity formula:
$$<span class="ans">(\\nabla f(x) - \\nabla f(y))^\\top (x - y) \\ge \\frac{1}{L} \\|\\nabla f(x) - \\nabla f(y)\\|_2^2</span> \\quad \\blacksquare$$</p>

<p><span class="part">Part (c): Significance</span><br>
Monotonicity only guarantees $\\ge 0$. Co-coercivity proves the gradient mapping is firmly nonexpansive ($1/L$ contractive), ensuring gradient descent is non-expansive for step size $\\alpha < 2/L$.</p>""",
        "takeaway": "Co-coercivity is the cornerstone of operator splitting (proximal algorithms). It proves the inner product of gradient variation and coordinate variation dominates the squared gradient norm."
    },

    # =========================================================================
    # TOPIC 04: Line Search Methods (Exact, Armijo, Wolfe)
    # =========================================================================
    {
        "id": 10491,
        "subject": "CMO",
        "topicId": "04_Line_Search_Methods_Exact_Armijo_and_Wolfe",
        "topicTitle": "04 · Line Search (Armijo & Wolfe)",
        "title": "Exact Quadratic Line Search (IISc Midterm 2024)",
        "kind2": "pyq",
        "source": "IISc Midterm 2 2024 / Nocedal & Wright Ch 3",
        "marks": "[8 Marks]",
        "question": """<p>Consider the strictly convex quadratic function:
$$f(x) = \\frac{1}{2} x^\\top Q x - b^\\top x$$
where $Q \\in \\mathbb{R}^{n \\times n}$ is symmetric positive definite ($Q \\succ 0$).<br>
<span class="part">(a)</span> For an arbitrary iterate $x_k$ and search direction $p_k$, derive the exact analytic step length $\\alpha_k$ that minimizes the 1D slice $\\phi(\\alpha) = f(x_k + \\alpha p_k)$.<br>
<span class="part">(b)</span> Specialize this formula to the steepest descent direction $p_k = -\\nabla f(x_k) = -g_k$.<br>
<span class="part">(c)</span> Prove that consecutive steepest descent steps with exact line search are strictly orthogonal: $g_{k+1}^\\top g_k = 0$.</p>""",
        "solution": """<p><span class="part">Part (a): Exact Step Length Derivation</span><br>
Expand $\\phi(\\alpha) = f(x_k + \\alpha p_k)$:
$$\\phi(\\alpha) = \\frac{1}{2}(x_k + \\alpha p_k)^\\top Q (x_k + \\alpha p_k) - b^\\top (x_k + \\alpha p_k)$$
$$\\phi(\\alpha) = f(x_k) + \\alpha (Q x_k - b)^\\top p_k + \\frac{1}{2} \\alpha^2 p_k^\\top Q p_k = f(x_k) + \\alpha \\nabla f(x_k)^\\top p_k + \\frac{1}{2} \\alpha^2 p_k^\\top Q p_k$$
Differentiating with respect to $\\alpha$:
$$\\phi'(\\alpha) = \\nabla f(x_k)^\\top p_k + \\alpha p_k^\\top Q p_k = 0 \\implies <span class="ans">\\alpha_k = -\\frac{\\nabla f(x_k)^\\top p_k}{p_k^\\top Q p_k}</span>$$</p>

<p><span class="part">Part (b): Steepest Descent Direction</span><br>
Substituting $p_k = -g_k = -\\nabla f(x_k)$:
$$\\alpha_k = -\\frac{g_k^\\top (-g_k)}{(-g_k)^\\top Q (-g_k)} = <span class="ans">\\frac{g_k^\\top g_k}{g_k^\\top Q g_k}</span>$$</p>

<p><span class="part">Part (c): Orthogonality Proof</span><br>
The gradient at the new iterate $x_{k+1} = x_k + \\alpha_k p_k$ is:
$$g_{k+1} = Q x_{k+1} - b = Q(x_k + \\alpha_k p_k) - b = (Q x_k - b) + \\alpha_k Q p_k = g_k + \\alpha_k Q p_k$$
Take the inner product of $g_{k+1}$ with the search direction $p_k$:
$$g_{k+1}^\\top p_k = g_k^\\top p_k + \\alpha_k p_k^\\top Q p_k = g_k^\\top p_k + \\left(-\\frac{g_k^\\top p_k}{p_k^\\top Q p_k}\\right) p_k^\\top Q p_k = g_k^\\top p_k - g_k^\\top p_k = 0$$
For steepest descent, $p_k = -g_k$. Thus:
$$g_{k+1}^\\top (-g_k) = 0 \\implies <span class="ans">g_{k+1}^\\top g_k = 0</span> \\quad \\blacksquare$$</p>""",
        "takeaway": "Exact line search stops at the tangent point where the line is tangent to the contour ellipse, forcing $g_{k+1} \\perp g_k$. This exact 90-degree orthogonality is the root cause of zig-zagging."
    },
    {
        "id": 10492,
        "subject": "CMO",
        "topicId": "04_Line_Search_Methods_Exact_Armijo_and_Wolfe",
        "topicTitle": "04 · Line Search (Armijo & Wolfe)",
        "title": "Backtracking Armijo Finite Termination (Stanford Boyd)",
        "kind2": "pyq",
        "source": "Stanford EE364a / Boyd Ch 9",
        "marks": "[8 Marks]",
        "question": """<p>Consider the Backtracking Line Search algorithm: given descent direction $p_k$ ($\\nabla f(x_k)^\\top p_k < 0$), start with initial step $\\alpha = 1$, contraction factor $\\rho \\in (0, 1)$, and Armijo parameter $c \\in (0, 1)$.<br>
Repeat $\\alpha \\leftarrow \\rho \\alpha$ until the Armijo condition holds:
$$f(x_k + \\alpha p_k) \\le f(x_k) + c \\alpha \\nabla f(x_k)^\\top p_k$$
Prove that if $f$ is continuously differentiable ($C^1$), this backtracking procedure terminates after a finite number of iterations.</p>""",
        "solution": """<p><span class="part">Step 1: First-Order Taylor Limit</span><br>
By definition of the directional derivative of a $C^1$ function:
$$\\lim_{\\alpha \\to 0^+} \\frac{f(x_k + \\alpha p_k) - f(x_k)}{\\alpha} = \\nabla f(x_k)^\\top p_k$$</p>

<p><span class="part">Step 2: Strict Inequality Threshold</span><br>
Since $c \\in (0, 1)$ and $\\nabla f(x_k)^\\top p_k < 0$, we have:
$$\\nabla f(x_k)^\\top p_k < c \\nabla f(x_k)^\\top p_k$$
Define the strictly positive gap:
$$\\epsilon = (1 - c) |\\nabla f(x_k)^\\top p_k| > 0$$</p>

<p><span class="part">Step 3: Existence of Admissible Interval</span><br>
By the definition of the limit, for this $\\epsilon > 0$, there exists a threshold $\\bar{\\alpha} > 0$ such that for all $\\alpha \\in (0, \\bar{\\alpha})$:
$$\\frac{f(x_k + \\alpha p_k) - f(x_k)}{\\alpha} \\le \\nabla f(x_k)^\\top p_k + \\epsilon = c \\nabla f(x_k)^\\top p_k$$
Multiplying by $\\alpha > 0$:
$$f(x_k + \\alpha p_k) \\le f(x_k) + c \\alpha \\nabla f(x_k)^\\top p_k$$
Thus, the Armijo condition is satisfied for all $\\alpha \\in (0, \\bar{\\alpha})$.</p>

<p><span class="part">Step 4: Finite Iteration Count</span><br>
The backtracking loop tests the sequence of step lengths $\\alpha_m = \\rho^m$ for $m = 0, 1, 2, \\dots$.<br>
Since $\\rho \\in (0, 1)$, $\\lim_{m \\to \\infty} \\rho^m = 0$.<br>
Therefore, there exists a finite smallest integer $m^*$ such that:
$$\\rho^{m^*} < \\bar{\\alpha} \\implies m^* \\le \\left\\lceil \\frac{\\ln \\bar{\\alpha}}{\\ln \\rho} \\right\\rceil < \\infty$$
<span class="ans">Backtracking terminates in at most $m^*$ steps.</span> $\\blacksquare$</p>""",
        "takeaway": "Because the true tangent slope $\\nabla f^\\top p$ is strictly steeper than the Armijo boundary slope $c \\nabla f^\\top p$, the actual curve must plunge below the Armijo line for sufficiently small $\\alpha$."
    },
    {
        "id": 10493,
        "subject": "CMO",
        "topicId": "04_Line_Search_Methods_Exact_Armijo_and_Wolfe",
        "topicTitle": "04 · Line Search (Armijo & Wolfe)",
        "title": "Strong Wolfe Conditions & Parameter Bounds (Generated Exam)",
        "kind2": "practice",
        "source": "IISc / Nocedal & Wright Benchmark",
        "marks": "[10 Marks]",
        "question": """<p>The Strong Wolfe conditions require finding $\\alpha_k > 0$ satisfying:
$$f(x_k + \\alpha_k p_k) \\le f(x_k) + c_1 \\alpha_k \\nabla f(x_k)^\\top p_k \\quad \\text{(Armijo Decrease)}$$
$$|\\nabla f(x_k + \\alpha_k p_k)^\\top p_k| \\le c_2 |\\nabla f(x_k)^\\top p_k| \\quad \\text{(Curvature Condition)}$$
with $0 < c_1 < c_2 < 1$.<br>
<span class="part">(a)</span> Prove that if $f$ is continuously differentiable and bounded below along the ray $\\{x_k + \\alpha p_k : \\alpha > 0\\}$, there exists an interval of step lengths satisfying the Strong Wolfe conditions.<br>
<span class="part">(b)</span> Why is the ordering condition $c_1 < c_2$ mathematically necessary? What breaks if $c_1 \\ge c_2$?</p>""",
        "solution": """<p><span class="part">Part (a): Existence Proof via Mean Value Theorem</span><br>
Let $\\phi(\\alpha) = f(x_k + \\alpha p_k)$. Since $p_k$ is a descent direction, $\\phi'(0) < 0$.<br>
Consider the Armijo line $l(\\alpha) = \\phi(0) + c_1 \\alpha \\phi'(0)$.<br>
Since $c_1 \\phi'(0) < 0$, $l(\\alpha) \\to -\\infty$ as $\\alpha \\to \\infty$. But $f$ is bounded below, so $\\phi(\\alpha)$ is bounded below.<br>
Therefore, $\\phi(\\alpha)$ must cross $l(\\alpha)$ at some point $\\alpha' > 0$ such that $\\phi(\\alpha') = l(\\alpha')$.<br>
Over the interval $[0, \\alpha']$, by the Mean Value Theorem, there exists $\\alpha^* \\in (0, \\alpha')$ such that:
$$\\phi'(\\alpha^*) = \\frac{\\phi(\\alpha') - \\phi(0)}{\\alpha'} = c_1 \\phi'(0)$$
Since $\\phi'(0) < 0$ and $c_1 < c_2 < 1$:
$$c_1 \\phi'(0) > c_2 \\phi'(0) \\implies \\phi'(\\alpha^*) > -c_2 |\\phi'(0)|$$
Also, $\\phi(\\alpha) < l(\\alpha)$ on $(0, \\alpha')$, so $\\alpha^*$ strictly satisfies Armijo decrease.<br>
Since $|\\phi'(\\alpha^*)| = -c_1 \\phi'(0) < c_2 |\\phi'(0)|$, by continuity of $\\phi'$, <span class="ans">an entire open interval around $\\alpha^*$ satisfies the Strong Wolfe conditions</span>.</p>

<p><span class="part">Part (b): Necessity of $c_1 < c_2$</span><br>
If $c_1 \\ge c_2$, the slope requirement of condition 2 requires $|\\phi'(\\alpha)| \\le c_2 |\\phi'(0)| \\le c_1 |\\phi'(0)|$.<br>
For a convex function, $\\phi'(\\alpha)$ is non-decreasing. The point where the slope reaches $c_1 \\phi'(0)$ occurs exactly at or after the point where $\\phi$ crosses above the Armijo line!<br>
Thus, the set of points satisfying Armijo decrease and the set of points satisfying the curvature condition can become <span class="ans">completely disjoint</span>! No step size $\\alpha$ can satisfy both conditions simultaneously when $c_1 \\ge c_2$.</p>""",
        "takeaway": "$0 < c_1 < c_2 < 1$ is required to ensure the Armijo decrease threshold and Wolfe slope flattening threshold overlap in a nonempty admissible set."
    },

    # =========================================================================
    # TOPIC 05: Gradient Descent & Convergence Analysis
    # =========================================================================
    {
        "id": 10591,
        "subject": "CMO",
        "topicId": "05_Gradient_Descent_and_Convergence_Analysis",
        "topicTitle": "05 · Gradient Descent & Convergence",
        "title": "Kantorovich Bound & Zig-Zagging (IISc Endsem 2024)",
        "kind2": "pyq",
        "source": "IISc Endsem 2024 / Luenberger Ch 8",
        "marks": "[10 Marks]",
        "question": """<p>Consider minimizing the quadratic function:
$$f(x_1, x_2) = \\frac{1}{2} x_1^2 + \\frac{50}{2} x_2^2$$
using Gradient Descent with exact line search, starting from $x_0 = (50, 1)^\\top$.<br>
<span class="part">(a)</span> Compute the condition number $\\kappa(Q)$ and the theoretical Kantorovich error reduction factor $r = \\left(\\frac{\\kappa - 1}{\\kappa + 1}\\right)^2$.<br>
<span class="part">(b)</span> Compute the exact coordinates of $x_1$ and $x_2$.<br>
<span class="part">(c)</span> Show that the ratio of components $x_{k,1}/x_{k,2}$ alternates sign while preserving its magnitude, proving endless 90° zig-zagging.</p>""",
        "solution": """<p><span class="part">Part (a): Condition Number & Theoretical Rate</span><br>
$$Q = \\begin{bmatrix} 1 & 0 \\\\ 0 & 50 \\end{bmatrix} \\implies \\lambda_{\\max} = 50, \\quad \\lambda_{\\min} = 1 \\implies <span class="ans">\\kappa(Q) = 50</span>$$
The Kantorovich convergence factor is:
$$r = \\left(\\frac{\\kappa - 1}{\\kappa + 1}\\right)^2 = \\left(\\frac{50 - 1}{50 + 1}\\right)^2 = \\left(\\frac{49}{51}\\right)^2 = \\frac{2401}{2601} \\approx <span class="ans">0.9231</span>$$
Each step reduces the error by at most $7.7\\%$.</p>

<p><span class="part">Part (b): Exact Calculation of $x_1$ and $x_2$</span><br>
At $x_0 = (50, 1)^\\top$:
$$g_0 = Q x_0 = \\begin{bmatrix} 1(50) \\\\ 50(1) \\end{bmatrix} = \\begin{bmatrix} 50 \\\\ 50 \\end{bmatrix}$$
$$\\alpha_0 = \\frac{g_0^\\top g_0}{g_0^\\top Q g_0} = \\frac{50^2 + 50^2}{50^2(1) + 50^2(50)} = \\frac{5000}{2500 + 125000} = \\frac{5000}{127500} = \\frac{2}{51}$$
Update:
$$x_1 = x_0 - \\alpha_0 g_0 = \\begin{bmatrix} 50 \\\\ 1 \\end{bmatrix} - \\frac{2}{51} \\begin{bmatrix} 50 \\\\ 50 \\end{bmatrix} = \\begin{bmatrix} 50(1 - 2/51) \\\\[4pt] 1 - 100/51 \\end{bmatrix} = <span class="ans">\\frac{49}{51} \\begin{bmatrix} 50 \\\\ -1 \\end{bmatrix}</span>$$
For the next iteration, $g_1 = Q x_1 = \\frac{49}{51} \\begin{bmatrix} 50 \\\\ -50 \\end{bmatrix}$.<br>
$$\\alpha_1 = \\frac{g_1^\\top g_1}{g_1^\\top Q g_1} = \\frac{2}{51}$$
$$x_2 = x_1 - \\alpha_1 g_1 = \\left(\\frac{49}{51}\\right)^2 \\begin{bmatrix} 50 \\\\ 1 \\end{bmatrix}$$</p>

<p><span class="part">Part (c): Geometric Zig-Zagging</span><br>
In general: $x_k = \\left(\\frac{49}{51}\\right)^k \\begin{bmatrix} 50 \\\\[2pt] (-1)^k \\end{bmatrix}$.<br>
The ratio $x_{k,1}/x_{k,2} = 50 \\cdot (-1)^k$ strictly alternates sign! Iterates bounce back and forth across the narrow valley walls perpendicular to the valley floor.</p>""",
        "takeaway": "When $\\kappa \\gg 1$, exact line search traps gradient descent into an orthogonal zig-zag where progress along the slow eigenvector is choked by oscillations across the steep eigenvector."
    },
    {
        "id": 10592,
        "subject": "CMO",
        "topicId": "05_Gradient_Descent_and_Convergence_Analysis",
        "topicTitle": "05 · Gradient Descent & Convergence",
        "title": "Descent Lemma Derivation (Stanford Boyd)",
        "kind2": "pyq",
        "source": "Stanford EE364a / Boyd Ch 9",
        "marks": "[8 Marks]",
        "question": """<p>Let $f: \\mathbb{R}^n \\to \\mathbb{R}$ be continuously differentiable with $L$-Lipschitz continuous gradient:
$$\\|\\nabla f(u) - \\nabla f(v)\\|_2 \\le L \\|u - v\\|_2 \\quad \\forall u, v \\in \\mathbb{R}^n$$
Prove the <strong>Descent Lemma</strong> (Quadratic Upper Bound):
$$f(y) \\le f(x) + \\nabla f(x)^\\top (y - x) + \\frac{L}{2} \\|y - x\\|_2^2 \\quad \\forall x, y \\in \\mathbb{R}^n$$</p>""",
        "solution": """<p><span class="part">Step 1: Fundamental Theorem of Calculus</span><br>
Consider the line segment connecting $x$ to $y$, parameterized by $x(t) = x + t(y - x)$ for $t \\in [0, 1]$. By the chain rule:
$$f(y) - f(x) = \\int_0^1 \\frac{d}{dt} f(x + t(y - x)) \\, dt = \\int_0^1 \\nabla f(x + t(y - x))^\\top (y - x) \\, dt$$</p>

<p><span class="part">Step 2: Add and Subtract Reference Gradient</span><br>
Add and subtract $\\nabla f(x)^\\top (y - x)$ inside the integrand:
$$f(y) - f(x) = \\int_0^1 \\nabla f(x)^\\top (y - x) \\, dt + \\int_0^1 [\\nabla f(x + t(y - x)) - \\nabla f(x)]^\\top (y - x) \\, dt$$
The first integral is independent of $t$:
$$f(y) - f(x) = \\nabla f(x)^\\top (y - x) + \\int_0^1 [\\nabla f(x + t(y - x)) - \\nabla f(x)]^\\top (y - x) \\, dt$$</p>

<p><span class="part">Step 3: Cauchy-Schwarz & Lipschitz Bound</span><br>
Apply the Cauchy-Schwarz inequality to the remaining integrand:
$$|[\\nabla f(x + t(y - x)) - \\nabla f(x)]^\\top (y - x)| \\le \\|\\nabla f(x + t(y - x)) - \\nabla f(x)\\|_2 \\|y - x\\|_2$$
By the $L$-Lipschitz property:
$$\\|\\nabla f(x + t(y - x)) - \\nabla f(x)\\|_2 \\le L \\|t(y - x)\\|_2 = L t \\|y - x\\|_2$$
Substitute this bound back into the integral:
$$\\int_0^1 [\\nabla f(x + t(y - x)) - \\nabla f(x)]^\\top (y - x) \\, dt \\le L \\|y - x\\|_2^2 \\int_0^1 t \\, dt = \\frac{L}{2} \\|y - x\\|_2^2$$</p>

<p><span class="part">Step 4: Final Assembly</span><br>
Combining the terms:
$$f(y) - f(x) \\le \\nabla f(x)^\\top (y - x) + \\frac{L}{2} \\|y - x\\|_2^2$$
<span class="ans">$$f(y) \\le f(x) + \\nabla f(x)^\\top (y - x) + \\frac{L}{2} \\|y - x\\|_2^2$$</span> $\\blacksquare$</p>""",
        "takeaway": "The Descent Lemma guarantees that an $L$-smooth function can never bend upwards faster than a paraboloid of curvature $L$. Any step size $\\alpha \\le 1/L$ is guaranteed to decrease the objective."
    },
    {
        "id": 10593,
        "subject": "CMO",
        "topicId": "05_Gradient_Descent_and_Convergence_Analysis",
        "topicTitle": "05 · Gradient Descent & Convergence",
        "title": "Sublinear O(1/T) Rate of Gradient Descent (Generated Exam)",
        "kind2": "practice",
        "source": "IISc / MIT Benchmark",
        "marks": "[10 Marks]",
        "question": """<p>Let $f: \\mathbb{R}^n \\to \\mathbb{R}$ be convex and $L$-smooth with a global minimum $x^*$ ($f^* = f(x^*)$). Consider Gradient Descent with constant step size $\\alpha = 1/L$:
$$x_{k+1} = x_k - \\frac{1}{L} \\nabla f(x_k)$$
<span class="part">(a)</span> Using the Descent Lemma, prove that each iteration guarantees:
$$f(x_{k+1}) \\le f(x_k) - \\frac{1}{2L} \\|\\nabla f(x_k)\\|_2^2$$
<span class="part">(b)</span> Prove the global $\\mathcal{O}(1/T)$ sublinear convergence rate:
$$f(x_T) - f^* \\le \\frac{L \\|x_0 - x^*\\|_2^2}{2T}$$</p>""",
        "solution": """<p><span class="part">Part (a): Per-Step Decrease</span><br>
Substitute $y = x_{k+1} = x_k - \\frac{1}{L} \\nabla f(x_k)$ into the Descent Lemma:
$$f(x_{k+1}) \\le f(x_k) + \\nabla f(x_k)^\\top \\left(-\\frac{1}{L}\\nabla f(x_k)\\right) + \\frac{L}{2} \\left\\|-\\frac{1}{L}\\nabla f(x_k)\\right\\|^2$$
$$f(x_{k+1}) \\le f(x_k) - \\frac{1}{L}\\|\\nabla f(x_k)\\|^2 + \\frac{1}{2L}\\|\\nabla f(x_k)\\|^2 = <span class="ans">f(x_k) - \\frac{1}{2L}\\|\\nabla f(x_k)\\|^2</span>$$</p>

<p><span class="part">Part (b): Global Rate Proof via Telescoping</span><br>
By convexity of $f$:
$$f(x_k) - f^* \\le \\nabla f(x_k)^\\top (x_k - x^*)$$
Now expand the distance to optimum for the next step:
$$\\|x_{k+1} - x^*\\|^2 = \\left\\|x_k - \\frac{1}{L}\\nabla f(x_k) - x^*\\right\\|^2 = \\|x_k - x^*\\|^2 - \\frac{2}{L}\\nabla f(x_k)^\\top(x_k - x^*) + \\frac{1}{L^2}\\|\\nabla f(x_k)\\|^2$$
Substitute $\\nabla f(x_k)^\\top(x_k - x^*) \\ge f(x_k) - f^*$ and $\\frac{1}{L^2}\\|\\nabla f(x_k)\\|^2 \\le \\frac{2}{L}(f(x_k) - f(x_{k+1}))$:
$$\\|x_{k+1} - x^*\\|^2 \\le \\|x_k - x^*\\|^2 - \\frac{2}{L}(f(x_k) - f^*) + \\frac{2}{L}(f(x_k) - f(x_{k+1})) = \\|x_k - x^*\\|^2 - \\frac{2}{L}(f(x_{k+1}) - f^*)$$
Rearranging:
$$f(x_{k+1}) - f^* \\le \\frac{L}{2} (\\|x_k - x^*\\|^2 - \\|x_{k+1} - x^*\\|^2)$$
Sum both sides from $k = 0$ to $T - 1$:
$$\\sum_{k=0}^{T-1} (f(x_{k+1}) - f^*) \\le \\frac{L}{2} \\sum_{k=0}^{T-1} (\\|x_k - x^*\\|^2 - \\|x_{k+1} - x^*\\|^2) = \\frac{L}{2}(\\|x_0 - x^*\\|^2 - \\|x_T - x^*\\|^2) \\le \\frac{L}{2}\\|x_0 - x^*\\|^2$$
Since $f(x_k)$ is non-increasing, $T(f(x_T) - f^*) \\le \\sum_{k=0}^{T-1} (f(x_{k+1}) - f^*)$. Dividing by $T$:
$$<span class="ans">f(x_T) - f^* \\le \\frac{L \\|x_0 - x^*\\|_2^2}{2T}</span> \\quad \\blacksquare$$</p>""",
        "takeaway": "Telescoping the distance-to-optimum sequence is the fundamental proof architecture for establishing $\\mathcal{O}(1/T)$ first-order sublinear rates."
    },

    # =========================================================================
    # TOPIC 06: Newton's Method & Hessian Modifications
    # =========================================================================
    {
        "id": 10691,
        "subject": "CMO",
        "topicId": "06_Newtons_Method_and_Hessian_Modifications",
        "topicTitle": "06 · Newton’s Method & Modifications",
        "title": "Newton Blowup on Rosenbrock (IISc Midterm 2023)",
        "kind2": "pyq",
        "source": "IISc Midterm 2 2023 / Nocedal & Wright Ch 3",
        "marks": "[10 Marks]",
        "question": """<p>Consider the Rosenbrock banana function:
$$f(x_1, x_2) = 100(x_2 - x_1^2)^2 + (1 - x_1)^2$$
Starting from $x_0 = (0, 0)^\\top$:<br>
<span class="part">(a)</span> Compute the gradient $\\nabla f(x_0)$ and the Hessian $\\nabla^2 f(x_0)$.<br>
<span class="part">(b)</span> Compute the pure Newton step $p_0 = -[\\nabla^2 f(x_0)]^{-1} \\nabla f(x_0)$ and the new iterate $x_1 = x_0 + p_0$.<br>
<span class="part">(c)</span> Evaluate $f(x_1)$ and compare it to $f(x_0)$. Explain what failed and why line search is mandatory.</p>""",
        "solution": """<p><span class="part">Part (a): Gradient & Hessian at $x_0 = (0, 0)$</span><br>
Partial derivatives:
$$\\frac{\\partial f}{\\partial x_1} = -400 x_1 (x_2 - x_1^2) - 2(1 - x_1) \\implies \\frac{\\partial f}{\\partial x_1}(0, 0) = -2$$
$$\\frac{\\partial f}{\\partial x_2} = 200(x_2 - x_1^2) \\implies \\frac{\\partial f}{\\partial x_2}(0, 0) = 0$$
$$\\nabla f(0, 0) = \\begin{bmatrix} -2 \\\\ 0 \\end{bmatrix}$$
Second derivatives:
$$\\frac{\\partial^2 f}{\\partial x_1^2} = -400(x_2 - 3x_1^2) + 2 \\implies \\frac{\\partial^2 f}{\\partial x_1^2}(0, 0) = 2$$
$$\\frac{\\partial^2 f}{\\partial x_1 \\partial x_2} = -400 x_1 \\implies \\frac{\\partial^2 f}{\\partial x_1 \\partial x_2}(0, 0) = 0$$
$$\\frac{\\partial^2 f}{\\partial x_2^2} = 200 \\implies \\frac{\\partial^2 f}{\\partial x_2^2}(0, 0) = 200$$
$$\\nabla^2 f(0, 0) = \\begin{bmatrix} 2 & 0 \\\\ 0 & 200 \\end{bmatrix}$$</p>

<p><span class="part">Part (b): Newton Step</span><br>
$$[\\nabla^2 f(0, 0)]^{-1} = \\begin{bmatrix} 1/2 & 0 \\\\ 0 & 1/200 \\end{bmatrix}$$
$$p_0 = - \\begin{bmatrix} 1/2 & 0 \\\\ 0 & 1/200 \\end{bmatrix} \\begin{bmatrix} -2 \\\\ 0 \\end{bmatrix} = \\begin{bmatrix} 1 \\\\ 0 \\end{bmatrix}$$
New iterate:
$$x_1 = x_0 + p_0 = \\begin{bmatrix} 0 \\\\ 0 \\end{bmatrix} + \\begin{bmatrix} 1 \\\\ 0 \\end{bmatrix} = <span class="ans">\\begin{bmatrix} 1 \\\\ 0 \\end{bmatrix}</span>$$</p>

<p><span class="part">Part (c): Value Evaluation & Failure Analysis</span><br>
Initial value: $f(0, 0) = 100(0 - 0)^2 + (1 - 0)^2 = 1$.<br>
New value:
$$f(1, 0) = 100(0 - 1^2)^2 + (1 - 1)^2 = 100(1) + 0 = <span class="ans">100</span>$$
<span class="ans">The objective exploded by a factor of 100 ($1 \\to 100$)!</span><br>
Why: Newton's method assumed the quadratic Taylor model at $(0,0)$ was valid across a distance of $\\|p_0\\| = 1$. But the quadratic model predicted $f(1, 0) \\approx 1 + (-2)(1) + \\frac{1}{2}(2)(1)^2 = 0$. In reality, the quartic term $-400 x_1^3$ dominated outside the neighborhood, wrecking the step. A backtracking line search (damped Newton) is required.</p>""",
        "takeaway": "Pure Newton steps can catastrophically overshoot when the objective contains high-degree nonlinearities. A line search or trust region is indispensable for global convergence."
    },
    {
        "id": 10692,
        "subject": "CMO",
        "topicId": "06_Newtons_Method_and_Hessian_Modifications",
        "topicTitle": "06 · Newton’s Method & Modifications",
        "title": "Quadratic Local Convergence Proof (Stanford Boyd)",
        "kind2": "pyq",
        "source": "Stanford EE364a / Boyd Ch 9",
        "marks": "[10 Marks]",
        "question": """<p>Let $f: \\mathbb{R}^n \\to \\mathbb{R}$ be $C^2$ with $M$-Lipschitz continuous Hessian:
$$\\|\\nabla^2 f(x) - \\nabla^2 f(y)\\|_2 \\le M \\|x - y\\|_2$$
Let $x^*$ be a strict local minimizer with $\\nabla f(x^*) = 0$ and $\\nabla^2 f(x^*) \\succeq \\mu I$ ($\\mu > 0$).<br>
Prove that Newton's method $x_{k+1} = x_k - [\\nabla^2 f(x_k)]^{-1} \\nabla f(x_k)$ converges <strong>quadratically</strong>:
$$\\|x_{k+1} - x^*\\|_2 \\le \\frac{M}{2\\mu} \\|x_k - x^*\\|_2^2$$
for $x_k$ sufficiently close to $x^*$.</p>""",
        "solution": """<p><span class="part">Step 1: Algebraic Error Representation</span><br>
Subtract $x^*$ from the Newton iteration formula:
$$x_{k+1} - x^* = x_k - x^* - [\\nabla^2 f(x_k)]^{-1} \\nabla f(x_k)$$
Factor out $[\\nabla^2 f(x_k)]^{-1}$:
$$x_{k+1} - x^* = [\\nabla^2 f(x_k)]^{-1} \\left( \\nabla^2 f(x_k)(x_k - x^*) - (\\nabla f(x_k) - \\nabla f(x^*)) \\right)$$</p>

<p><span class="part">Step 2: Integral Representation of Gradient Difference</span><br>
By the Fundamental Theorem of Calculus:
$$\\nabla f(x_k) - \\nabla f(x^*) = \\int_0^1 \\nabla^2 f(x^* + t(x_k - x^*)) (x_k - x^*) \\, dt$$
Substitute this into the bracketed error expression:
$$\\nabla^2 f(x_k)(x_k - x^*) - (\\nabla f(x_k) - \\nabla f(x^*)) = \\int_0^1 [\\nabla^2 f(x_k) - \\nabla^2 f(x^* + t(x_k - x^*))] (x_k - x^*) \\, dt$$</p>

<p><span class="part">Step 3: Apply Lipschitz Hessian Continuity</span><br>
$$\\|\\nabla^2 f(x_k) - \\nabla^2 f(x^* + t(x_k - x^*))\\| \\le M \\|x_k - (x^* + t(x_k - x^*))\\| = M(1 - t)\\|x_k - x^*\\|$$
Taking norms of the integral:
$$\\left\\|\\int_0^1 [\\dots] (x_k - x^*) \\, dt\\right\\| \\le M \\|x_k - x^*\\|^2 \\int_0^1 (1 - t) \\, dt = \\frac{M}{2} \\|x_k - x^*\\|^2$$</p>

<p><span class="part">Step 4: Bound on Inverse Hessian Norm</span><br>
By perturbation theory, for $\\|x_k - x^*\\| \\le \\frac{\\mu}{2M}$:
$$\\|[\\nabla^2 f(x_k)]^{-1}\\| \\le \\frac{1}{\\mu - M\\|x_k - x^*\\|} \\le \\frac{1}{\\mu - \\mu/2} = \\frac{2}{\\mu}$$
In the asymptotic limit as $x_k \\to x^*$, $\\|[\\nabla^2 f(x_k)]^{-1}\\| \\to \\frac{1}{\\mu}$. Combining the bounds:
$$\\|x_{k+1} - x^*\\|_2 \\le <span class="ans">\\frac{M}{2\\mu} \\|x_k - x^*\\|_2^2</span> \\quad \\blacksquare$$</p>""",
        "takeaway": "Quadratic convergence means the error is squared at every step: 2 accurate digits become 4, then 8, then 16 in three iterations."
    },
    {
        "id": 10693,
        "subject": "CMO",
        "topicId": "06_Newtons_Method_and_Hessian_Modifications",
        "topicTitle": "06 · Newton’s Method & Modifications",
        "title": "Levenberg-Marquardt Regularization (Generated Exam)",
        "kind2": "practice",
        "source": "IISc / Berkeley Benchmark",
        "marks": "[10 Marks]",
        "question": """<p>When the Hessian $\\nabla^2 f(x_k)$ is indefinite or ill-conditioned, we modify it by adding a multiple of the identity:
$$B_k = \\nabla^2 f(x_k) + \\tau_k I$$
and solve $B_k p_k = -\\nabla f(x_k)$.<br>
Let the eigenvalues of $\\nabla^2 f(x_k)$ be $\\lambda_1 \\le \\lambda_2 \\le \\dots \\le \\lambda_n$.<br>
<span class="part">(a)</span> What is the minimum scalar $\\tau_k \\ge 0$ required to ensure $B_k \\succeq \\delta I$ for some desired $\\delta > 0$?<br>
<span class="part">(b)</span> Show that as $\\tau_k \\to \\infty$, the search direction $p_k$ smoothly transitions into a scaled steepest descent direction.</p>""",
        "solution": """<p><span class="part">Part (a): Minimum Shift Calculation</span><br>
The eigenvalues of the shifted matrix $B_k = \\nabla^2 f(x_k) + \\tau_k I$ are:
$$\\lambda_i(B_k) = \\lambda_i + \\tau_k \\quad (i = 1, \\dots, n)$$
To guarantee that the matrix is strictly positive definite with smallest eigenvalue at least $\\delta > 0$:
$$\\lambda_1 + \\tau_k \\ge \\delta \\implies \\tau_k \\ge \\delta - \\lambda_1$$
Since $\\tau_k$ must be non-negative:
$$<span class="ans">\\tau_k = \\max(0, \\delta - \\lambda_1)</span>$$
If $\\lambda_1 < 0$ (Hessian is indefinite or negative definite), $\\tau_k$ must be at least $|\\lambda_1| + \\delta$, shifting all eigenvalues into the strictly positive domain.</p>

<p><span class="part">Part (b): Asymptotic Limit as $\\tau_k \\to \\infty$</span><br>
Factor out $\\tau_k$ from the inverse:
$$B_k^{-1} = (\\nabla^2 f(x_k) + \\tau_k I)^{-1} = \\frac{1}{\\tau_k} \\left( I + \\frac{1}{\\tau_k} \\nabla^2 f(x_k) \\right)^{-1}$$
Using the Neumann series expansion $(I + E)^{-1} = I - E + E^2 - \\dots$ for small $E = \\frac{1}{\\tau_k}\\nabla^2 f$:
$$B_k^{-1} = \\frac{1}{\\tau_k} \\left( I - \\frac{1}{\\tau_k} \\nabla^2 f(x_k) + \\mathcal{O}\\left(\\frac{1}{\\tau_k^2}\\right) \\right) = \\frac{1}{\\tau_k} I + \\mathcal{O}\\left(\\frac{1}{\\tau_k^2}\\right)$$
The modified Newton direction becomes:
$$p_k = -B_k^{-1} \\nabla f(x_k) = -\\frac{1}{\\tau_k} \\nabla f(x_k) + \\mathcal{O}\\left(\\frac{1}{\\tau_k^2}\\right)$$
<span class="ans">$$p_k \\approx -\\frac{1}{\\tau_k} \\nabla f(x_k)$$</span>
The direction becomes perfectly parallel to the steepest descent direction $-\\nabla f(x_k)$, with step length vanishing as $1/\\tau_k \\to 0$.</p>""",
        "takeaway": "Hessian regularization $\\nabla^2 f + \\tau I$ provides a continuous bridge between fast quadratic Newton optimization (when $\\tau \\to 0$) and guaranteed robust gradient descent (when $\\tau \\to \\infty$)."
    },

    # =========================================================================
    # TOPIC 07: Conjugate Direction & Conjugate Gradient Methods
    # =========================================================================
    {
        "id": 10791,
        "subject": "CMO",
        "topicId": "07_Conjugate_Direction_and_Conjugate_Gradient_Methods",
        "topicTitle": "07 · Conjugate Direction & CG Methods",
        "title": "Manual Execution of Linear CG (IISc Midterm 2024)",
        "kind2": "pyq",
        "source": "IISc Midterm 2 2024 / Nocedal & Wright Ch 5",
        "marks": "[10 Marks]",
        "question": """<p>Consider the objective function:
$$f(x_1, x_2) = \\frac{1}{2} x_1^2 + 2x_2^2 - x_1 - 4x_2$$
Execute the Linear Conjugate Gradient (CG) algorithm starting from $x_0 = (0, 0)^\\top$:<br>
<span class="part">(a)</span> Identify the matrix $A$ and vector $b$, and compute the initial residual $r_0$ and initial search direction $p_0$.<br>
<span class="part">(b)</span> Compute step length $\\alpha_0$ and iterate $x_1$.<br>
<span class="part">(c)</span> Compute residual $r_1$, Gram-Schmidt parameter $\\beta_1$, direction $p_1$, step length $\\alpha_1$, and iterate $x_2$. Verify $x_2$ is the exact minimizer!</p>""",
        "solution": """<p><span class="part">Part (a): Matrix Form & Initial Step</span><br>
Write $f(x) = \\frac{1}{2} x^\\top A x - b^\\top x$:
$$A = \\begin{bmatrix} 1 & 0 \\\\ 0 & 4 \\end{bmatrix}, \\quad b = \\begin{bmatrix} 1 \\\\ 4 \\end{bmatrix}$$
At $x_0 = (0, 0)^\\top$:
$$r_0 = b - A x_0 = \\begin{bmatrix} 1 \\\\ 4 \\end{bmatrix}, \\quad p_0 = r_0 = \\begin{bmatrix} 1 \\\\ 4 \\end{bmatrix}$$</p>

<p><span class="part">Part (b): Iteration 0 $\\to$ Iterate $x_1$</span><br>
$$A p_0 = \\begin{bmatrix} 1 & 0 \\\\ 0 & 4 \\end{bmatrix} \\begin{bmatrix} 1 \\\\ 4 \\end{bmatrix} = \\begin{bmatrix} 1 \\\\ 16 \\end{bmatrix}$$
$$\\alpha_0 = \\frac{r_0^\\top r_0}{p_0^\\top A p_0} = \\frac{1^2 + 4^2}{1(1) + 4(16)} = \\frac{17}{1 + 64} = <span class="ans">\\frac{17}{65}</span>$$
$$x_1 = x_0 + \\alpha_0 p_0 = \\begin{bmatrix} 0 \\\\ 0 \\end{bmatrix} + \\frac{17}{65} \\begin{bmatrix} 1 \\\\ 4 \\end{bmatrix} = <span class="ans">\\begin{bmatrix} 17/65 \\\\ 68/65 \\end{bmatrix}</span>$$</p>

<p><span class="part">Part (c): Iteration 1 $\\to$ Exact Solution $x_2$</span><br>
Residual update:
$$r_1 = r_0 - \\alpha_0 A p_0 = \\begin{bmatrix} 1 \\\\ 4 \\end{bmatrix} - \\frac{17}{65} \\begin{bmatrix} 1 \\\\ 16 \\end{bmatrix} = \\begin{bmatrix} 48/65 \\\\ -12/65 \\end{bmatrix} = \\frac{12}{65} \\begin{bmatrix} 4 \\\\ -1 \\end{bmatrix}$$
$$\\beta_1 = \\frac{r_1^\\top r_1}{r_0^\\top r_0} = \\frac{(48/65)^2 + (-12/65)^2}{17} = \\frac{2304 + 144}{4225 \\times 17} = \\frac{2448}{71825} = \\frac{144}{4225}$$
Conjugate direction:
$$p_1 = r_1 + \\beta_1 p_0 = \\begin{bmatrix} 48/65 \\\\ -12/65 \\end{bmatrix} + \\frac{144}{4225} \\begin{bmatrix} 1 \\\\ 4 \\end{bmatrix} = \\frac{204}{4225} \\begin{bmatrix} 16 \\\\ -1 \\end{bmatrix}$$
Check conjugacy: $p_0^\\top A p_1 \\propto [1, 4] \\begin{bmatrix} 16 \\\\ -4 \\end{bmatrix} = 16 - 16 = 0$! Exact $A$-conjugacy confirmed!<br>
Step length: $\\alpha_1 = \\frac{r_1^\\top r_1}{p_1^\\top A p_1} = \\frac{289}{204}$.<br>
$$x_2 = x_1 + \\alpha_1 p_1 = \\begin{bmatrix} 17/65 \\\\ 68/65 \\end{bmatrix} + \\begin{bmatrix} 48/65 \\\\ -3/65 \\end{bmatrix} = <span class="ans">\\begin{bmatrix} 1 \\\\ 1 \\end{bmatrix} = x^*</span>$$
The algorithm terminates with the EXACT minimizer in $n = 2$ steps!</p>""",
        "takeaway": "On an $n$-dimensional strictly convex quadratic, CG explores expanding Krylov subspaces and hits the exact global minimum in at most $n$ iterations."
    },
    {
        "id": 10792,
        "subject": "CMO",
        "topicId": "07_Conjugate_Direction_and_Conjugate_Gradient_Methods",
        "topicTitle": "07 · Conjugate Direction & CG Methods",
        "title": "Conjugacy Implies Linear Independence (Stanford Boyd)",
        "kind2": "pyq",
        "source": "Stanford EE364a / Boyd Ch 9",
        "marks": "[8 Marks]",
        "question": """<p>Let $A \\in \\mathbb{R}^{n \\times n}$ be symmetric positive definite ($A \\succ 0$). A set of non-zero vectors $\\{p_0, p_1, \\dots, p_k\\} \\subset \\mathbb{R}^n$ ($k < n$) is said to be mutually $A$-conjugate if:
$$p_i^\\top A p_j = 0 \\quad \\forall i \\ne j$$
Prove that the set $\\{p_0, p_1, \\dots, p_k\\}$ is strictly linearly independent.</p>""",
        "solution": """<p><span class="part">Step 1: Set up the Linear Independence Test</span><br>
Consider a linear combination of the vectors set to zero:
$$\\sum_{i=0}^k c_i p_i = 0$$
for some unknown scalar coefficients $c_0, c_1, \\dots, c_k \\in \\mathbb{R}$.</p>

<p><span class="part">Step 2: Isolate an Arbitrary Coefficient via $A$-Inner Product</span><br>
Pick any arbitrary index $j \\in \\{0, 1, \\dots, k\\}$. Premultiply both sides by $p_j^\\top A$:
$$p_j^\\top A \\left( \\sum_{i=0}^k c_i p_i \\right) = p_j^\\top A \\cdot 0 = 0$$</p>

<p><span class="part">Step 3: Expand the Sum and Apply Conjugacy</span><br>
By linearity of matrix multiplication:
$$\\sum_{i=0}^k c_i (p_j^\\top A p_i) = 0$$
By the $A$-conjugacy assumption, $p_j^\\top A p_i = 0$ for every $i \\ne j$. Therefore, all terms in the summation vanish except the single term where $i = j$:
$$c_j (p_j^\\top A p_j) = 0$$</p>

<p><span class="part">Step 4: Use Positive Definiteness</span><br>
Because $A \\succ 0$ is strictly positive definite and the vector $p_j \\ne 0$ is non-zero:
$$p_j^\\top A p_j > 0$$
Dividing by this strictly positive scalar yields:
$$c_j = 0$$
Since index $j \\in \\{0, 1, \\dots, k\\}$ was chosen arbitrarily, this forces:
$$<span class="ans">c_0 = c_1 = \\dots = c_k = 0</span>$$
<span class="ans">Therefore, the set $\\{p_0, p_1, \\dots, p_k\\}$ is linearly independent.</span> $\\blacksquare$</p>""",
        "takeaway": "$A$-conjugacy is ordinary orthogonality under the elliptic metric $\\langle u, v \\rangle_A = u^\\top A v$. Mutual orthogonality under any inner product immediately forces linear independence."
    },
    {
        "id": 10793,
        "subject": "CMO",
        "topicId": "07_Conjugate_Direction_and_Conjugate_Gradient_Methods",
        "topicTitle": "07 · Conjugate Direction & CG Methods",
        "title": "CG Chebyshev Rate vs Gradient Descent (Generated Exam)",
        "kind2": "practice",
        "source": "IISc / Nocedal & Wright Benchmark",
        "marks": "[10 Marks]",
        "question": """<p>Let $A \\succ 0$ have condition number $\\kappa = \\lambda_{\\max}/\\lambda_{\\min}$.<br>
The Conjugate Gradient energy norm error satisfies the Chebyshev polynomial bound:
$$\\|x_k - x^*\\|_A \\le 2 \\left( \\frac{\\sqrt{\\kappa} - 1}{\\sqrt{\\kappa} + 1} \\right)^k \\|x_0 - x^*\\|_A$$
<span class="part">(a)</span> For a problem with $\\kappa = 10000$, calculate the contraction factors for both Gradient Descent and Conjugate Gradient.<br>
<span class="part">(b)</span> Estimate the number of iterations required by each method to reduce the initial error by a factor of $10^{-6}$.<br>
<span class="part">(c)</span> Suppose $A$ has dimension $n = 10000$, but its eigenvalues are clustered into only $3$ distinct values. Exactly how many iterations will CG need to find $x^*$?</p>""",
        "solution": """<p><span class="part">Part (a): Contraction Factors for $\\kappa = 10000$</span><br>
<ul>
  <li><strong>Gradient Descent:</strong>
  $$r_{\\text{GD}} = \\frac{\\kappa - 1}{\\kappa + 1} = \\frac{9999}{10001} \\approx 1 - \\frac{2}{10001} \\approx <span class="ans">0.99980</span>$$</li>
  <li><strong>Conjugate Gradient:</strong>
  $$\\sqrt{\\kappa} = \\sqrt{10000} = 100$$
  $$r_{\\text{CG}} = \\frac{\\sqrt{\\kappa} - 1}{\\sqrt{\\kappa} + 1} = \\frac{99}{101} \\approx 1 - \\frac{2}{101} \\approx <span class="ans">0.98020</span>$$</li>
</ul></p>

<p><span class="part">Part (b): Iterations to Reach $10^{-6}$ Error</span><br>
<ul>
  <li><strong>Gradient Descent:</strong> $(0.9998)^k \\le 10^{-6} \\implies -2 \\times 10^{-4} k \\le -6 \\ln 10 \\approx -13.8155$.
  $$k_{\\text{GD}} \\approx \\frac{13.8155}{2 \\times 10^{-4}} \\approx <span class="ans">69,078 \\text{ iterations}</span>$$</li>
  <li><strong>Conjugate Gradient:</strong> $2 (0.9802)^k \\le 10^{-6} \\implies k \\ln(0.9802) \\le \\ln(0.5 \\times 10^{-6}) \\approx -14.5086$.
  $$k_{\\text{CG}} \\approx \\frac{-14.5086}{\\ln(99/101)} \\approx \\frac{-14.5086}{-0.0200} \\approx <span class="ans">725 \\text{ iterations}</span>$$</li>
</ul>
<span class="ans">Conjugate Gradient is nearly 100 times faster!</span></p>

<p><span class="part">Part (c): Clustered Eigenvalues</span><br>
If $A$ has only $m = 3$ distinct eigenvalues $\\{\\mu_1, \\mu_2, \\mu_3\\}$, its minimal polynomial has degree $3$:
$$p(\\lambda) = (\\lambda - \\mu_1)(\\lambda - \\mu_2)(\\lambda - \\mu_3)$$
Since CG constructs the optimal polynomial of degree $k$ over the spectrum, at step $k = 3$, the polynomial can be chosen to vanish identically on all three eigenvalues simultaneously: $P_3(\\mu_i) = 0$.<br>
<span class="ans">CG terminates in exactly $k = 3$ iterations</span>, despite $n = 10000$!</p>""",
        "takeaway": "CG scales with $\\sqrt{\\kappa}$ rather than $\\kappa$, and its convergence is determined by the number of distinct eigenvalue clusters rather than matrix dimension."
    },

    # =========================================================================
    # TOPIC 08: Quasi-Newton Methods (SR1, DFP, BFGS)
    # =========================================================================
    {
        "id": 10891,
        "subject": "CMO",
        "topicId": "08_Quasi_Newton_Methods_SR1_DFP_and_BFGS",
        "topicTitle": "08 · Quasi-Newton Methods (BFGS)",
        "title": "SR1 Inverse Update & Indefiniteness (IISc Midterm 2024)",
        "kind2": "pyq",
        "source": "IISc Midterm 2 2024 / Nocedal & Wright Ch 6",
        "marks": "[10 Marks]",
        "question": """<p>Let $s_k = x_{k+1} - x_k = \\begin{bmatrix} 1 \\\\ 2 \\end{bmatrix}$ and $y_k = \\nabla f(x_{k+1}) - \\nabla f(x_k) = \\begin{bmatrix} 2 \\\\ 1 \\end{bmatrix}$.<br>
<span class="part">(a)</span> Verify whether the curvature condition $s_k^\\top y_k > 0$ holds.<br>
<span class="part">(b)</span> Using the Symmetric Rank-1 (SR1) formula starting with $H_k = I_2$:
$$H_{k+1} = H_k + \\frac{(s_k - H_k y_k)(s_k - H_k y_k)^\\top}{(s_k - H_k y_k)^\\top y_k}$$
compute the updated inverse Hessian approximation $H_{k+1}$.<br>
<span class="part">(c)</span> Verify the secant equation $H_{k+1} y_k = s_k$, and check whether $H_{k+1}$ is positive definite.</p>""",
        "solution": """<p><span class="part">Part (a): Curvature Condition</span><br>
$$s_k^\\top y_k = 1(2) + 2(1) = 2 + 2 = <span class="ans">4 > 0</span>$$
The curvature condition holds strictly.</p>

<p><span class="part">Part (b): SR1 Update Calculation</span><br>
Compute the discrepancy vector $v = s_k - H_k y_k$ with $H_k = I_2$:
$$v = \\begin{bmatrix} 1 \\\\ 2 \\end{bmatrix} - \\begin{bmatrix} 1 & 0 \\\\ 0 & 1 \\end{bmatrix} \\begin{bmatrix} 2 \\\\ 1 \\end{bmatrix} = \\begin{bmatrix} 1 - 2 \\\\ 2 - 1 \\end{bmatrix} = \\begin{bmatrix} -1 \\\\ 1 \\end{bmatrix}$$
Denominator:
$$v^\\top y_k = \\begin{bmatrix} -1 & 1 \\end{bmatrix} \\begin{bmatrix} 2 \\\\ 1 \\end{bmatrix} = -2 + 1 = -1 \\ne 0$$
Numerator outer product:
$$v v^\\top = \\begin{bmatrix} -1 \\\\ 1 \\end{bmatrix} \\begin{bmatrix} -1 & 1 \\end{bmatrix} = \\begin{bmatrix} 1 & -1 \\\\ -1 & 1 \\end{bmatrix}$$
Rank-1 correction:
$$\\frac{v v^\\top}{v^\\top y_k} = \\frac{1}{-1} \\begin{bmatrix} 1 & -1 \\\\ -1 & 1 \\end{bmatrix} = \\begin{bmatrix} -1 & 1 \\\\ 1 & -1 \\end{bmatrix}$$
Updated matrix:
$$H_{k+1} = H_k + \\frac{v v^\\top}{v^\\top y_k} = \\begin{bmatrix} 1 & 0 \\\\ 0 & 1 \\end{bmatrix} + \\begin{bmatrix} -1 & 1 \\\\ 1 & -1 \\end{bmatrix} = <span class="ans">\\begin{bmatrix} 0 & 1 \\\\ 1 & 0 \\end{bmatrix}</span>$$</p>

<p><span class="part">Part (c): Secant Verification & Indefiniteness</span><br>
Secant check:
$$H_{k+1} y_k = \\begin{bmatrix} 0 & 1 \\\\ 1 & 0 \\end{bmatrix} \\begin{bmatrix} 2 \\\\ 1 \\end{bmatrix} = \\begin{bmatrix} 1 \\\\ 2 \\end{bmatrix} = s_k$$
<span class="ans">The secant equation is satisfied exactly!</span><br>
Positive definiteness:
$$\\det(H_{k+1}) = 0(0) - 1(1) = -1 < 0$$
The eigenvalues are $\\lambda = \\pm 1$. <span class="ans">$H_{k+1}$ is INDEFINITE!</span><br>
Even though $s_k^\\top y_k = 4 > 0$, SR1 produced an indefinite matrix with a zero diagonal! This highlights why SR1 must be paired with trust-region safeguards, unlike BFGS.</p>""",
        "takeaway": "SR1 does NOT preserve positive definiteness, even when $s_k^\\top y_k > 0$. However, its ability to generate indefinite approximations makes it valuable in non-convex trust-region methods."
    },
    {
        "id": 10892,
        "subject": "CMO",
        "topicId": "08_Quasi_Newton_Methods_SR1_DFP_and_BFGS",
        "topicTitle": "08 · Quasi-Newton Methods (BFGS)",
        "title": "BFGS Positive Definiteness Preservation (Stanford Boyd)",
        "kind2": "pyq",
        "source": "Stanford EE364a / Boyd Ch 9",
        "marks": "[10 Marks]",
        "question": """<p>The BFGS inverse Hessian update is given by:
$$H_{k+1} = (I - \\rho_k s_k y_k^\\top) H_k (I - \\rho_k y_k s_k^\\top) + \\rho_k s_k s_k^\\top$$
where $\\rho_k = \\frac{1}{y_k^\\top s_k}$.<br>
<span class="part">(a)</span> Prove that if $H_k \\succ 0$ and the curvature condition $y_k^\\top s_k > 0$ holds, then $H_{k+1} \\succ 0$ strictly.<br>
<span class="part">(b)</span> Prove that the second Wolfe line search condition $\\nabla f(x_{k+1})^\\top p_k \\ge c_2 \\nabla f(x_k)^\\top p_k$ ($c_2 < 1$) automatically guarantees $y_k^\\top s_k > 0$.</p>""",
        "solution": """<p><span class="part">Part (a): Positive Definiteness Proof</span><br>
Let $z \\in \\mathbb{R}^n$ be any non-zero vector ($z \\ne 0$). Evaluate the quadratic form $z^\\top H_{k+1} z$:
$$z^\\top H_{k+1} z = z^\\top (I - \\rho_k s_k y_k^\\top) H_k (I - \\rho_k y_k s_k^\\top) z + \\rho_k z^\\top (s_k s_k^\\top) z$$
Define the auxiliary vector $w = (I - \\rho_k y_k s_k^\\top) z$. Then:
$$z^\\top H_{k+1} z = w^\\top H_k w + \\rho_k (s_k^\\top z)^2$$
Since $H_k \\succ 0$, $w^\\top H_k w \\ge 0$, and since $\\rho_k = \\frac{1}{y_k^\\top s_k} > 0$, $\\rho_k (s_k^\\top z)^2 \\ge 0$.<br>
Thus $z^\\top H_{k+1} z \\ge 0$. Could it equal zero?<br>
For the sum of two non-negative terms to be zero, both must be zero:
1. $\\rho_k (s_k^\\top z)^2 = 0 \\implies s_k^\\top z = 0$.<br>
2. $w^\\top H_k w = 0 \\implies w = 0$ (since $H_k \\succ 0$).<br>
Substitute (1) into the definition of $w$:
$$w = z - \\rho_k y_k (s_k^\\top z) = z - \\rho_k y_k (0) = z$$
Thus $w = 0 \\implies z = 0$. But $z$ was assumed non-zero! Contradiction.<br>
<span class="ans">Therefore, $z^\\top H_{k+1} z > 0$ for all $z \\ne 0$, meaning $H_{k+1} \\succ 0$ strictly.</span> $\\blacksquare$</p>

<p><span class="part">Part (b): Wolfe Condition Implies $y_k^\\top s_k > 0$</span><br>
Since $s_k = \\alpha_k p_k$ with $\\alpha_k > 0$, multiply the Wolfe curvature condition by $\\alpha_k$:
$$\\nabla f(x_{k+1})^\\top s_k \\ge c_2 \\nabla f(x_k)^\\top s_k$$
Subtract $\\nabla f(x_k)^\\top s_k$ from both sides:
$$y_k^\\top s_k = (\\nabla f(x_{k+1}) - \\nabla f(x_k))^\\top s_k \\ge (c_2 - 1) \\nabla f(x_k)^\\top s_k$$
Since $p_k$ is a descent direction, $\\nabla f(x_k)^\\top s_k = \\alpha_k \\nabla f(x_k)^\\top p_k < 0$.<br>
Since $c_2 < 1$, $(c_2 - 1) < 0$.<br>
The product of two negative numbers is strictly positive:
$$<span class="ans">y_k^\\top s_k \\ge (c_2 - 1) \\nabla f(x_k)^\\top s_k > 0</span> \\quad \\blacksquare$$</p>""",
        "takeaway": "Wolfe line search guarantees positive curvature $s_k^\\top y_k > 0$, which mathematically locks BFGS into remaining positive definite forever without any matrix restarts."
    },
    {
        "id": 10893,
        "subject": "CMO",
        "topicId": "08_Quasi_Newton_Methods_SR1_DFP_and_BFGS",
        "topicTitle": "08 · Quasi-Newton Methods (BFGS)",
        "title": "L-BFGS Two-Loop Recursion & Complexity (Generated Exam)",
        "kind2": "practice",
        "source": "IISc / Nocedal & Wright Benchmark",
        "marks": "[10 Marks]",
        "question": """<p>Limited-Memory BFGS (L-BFGS) avoids storing the $n \\times n$ matrix by keeping only the $m$ most recent vector pairs $\\{s_i, y_i\\}_{i=k-m}^{k-1}$.<br>
<span class="part">(a)</span> State the complete <strong>Two-Loop Recursion algorithm</strong> to compute the search direction $r = H_k \\nabla f(x_k)$.<br>
<span class="part">(b)</span> Prove that the computational complexity of L-BFGS is $\\mathcal{O}(m n)$ FLOPs and memory is $\\mathcal{O}(m n)$, compared to $\\mathcal{O}(n^2)$ for standard BFGS.<br>
<span class="part">(c)</span> What base matrix $H_k^{(0)} = \\gamma_k I$ is conventionally used, and what is the optimal formula for $\\gamma_k$?</p>""",
        "solution": """<p><span class="part">Part (a): L-BFGS Two-Loop Recursion Algorithm</span><br>
Given gradient $g_k = \\nabla f(x_k)$ and past $m$ pairs $\\{s_i, y_i\\}$ with $\\rho_i = 1/(y_i^\\top s_i)$:
<ol>
  <li><strong>First Loop (Backward):</strong><br>
  Set $q \\leftarrow g_k$.<br>
  For $i = k - 1, k - 2, \\dots, k - m$:<br>
  &nbsp;&nbsp;&nbsp;&nbsp;$\\alpha_i \\leftarrow \\rho_i s_i^\\top q$<br>
  &nbsp;&nbsp;&nbsp;&nbsp;$q \\leftarrow q - \\alpha_i y_i$</li>
  <li><strong>Base Scaling:</strong><br>
  $r \\leftarrow H_k^{(0)} q = \\gamma_k q$</li>
  <li><strong>Second Loop (Forward):</strong><br>
  For $i = k - m, k - m + 1, \\dots, k - 1$:<br>
  &nbsp;&nbsp;&nbsp;&nbsp;$\\beta \\leftarrow \\rho_i y_i^\\top r$<br>
  &nbsp;&nbsp;&nbsp;&nbsp;$r \\leftarrow r + s_i (\\alpha_i - \\beta)$</li>
  <li><strong>Return Direction:</strong><br>
  $p_k = -r$.</li>
</ol></p>

<p><span class="part">Part (b): Complexity Analysis</span><br>
<ul>
  <li><strong>Operations:</strong> In each loop iteration, we compute one vector dot product ($s_i^\\top q$ or $y_i^\\top r$, taking $2n$ FLOPs) and one vector saxpy update (taking $2n$ FLOPs).<br>
  Total loop FLOPs $= 2 \\times m \\times 4n = <span class="ans">8mn \\text{ FLOPs} = \\mathcal{O}(mn)</span>$.</li>
  <li><strong>Memory:</strong> We store $m$ vectors $s_i$ and $m$ vectors $y_i$, totaling <span class="ans">$2mn \\text{ floats} = \\mathcal{O}(mn)$</span>.</li>
  <li><strong>Comparison:</strong> For $n = 10^6$ and $m = 10$, standard BFGS requires $10^{12}$ floats ($\\approx 8$ Terabytes!). L-BFGS requires only $2 \\times 10 \\times 10^6 = 20 \\times 10^6$ floats ($\\approx 80$ Megabytes!), making Newton-like convergence possible on deep networks.</li>
</ul></p>

<p><span class="part">Part (c): Optimal Initial Scaling Factor $\\gamma_k$</span><br>
The standard initial matrix uses the most recent curvature:
$$<span class="ans">\\gamma_k = \\frac{s_{k-1}^\\top y_{k-1}}{y_{k-1}^\\top y_{k-1}}</span>$$
This represents the inverse of the estimated eigenvalue of the true Hessian along the most recent displacement $s_{k-1}$, ensuring unit step length $\\alpha = 1$ is accepted near the minimum without line search backtracking.</p>""",
        "takeaway": "L-BFGS turns quasi-Newton optimization into a linear-time $\\mathcal{O}(mn)$ algorithm by unrolling the BFGS matrix product into two sequential vector-vector loops."
    }
]

def main():
    out_path = os.path.join(os.path.dirname(__file__), "..", "practice_cmo.js")
    out_path = os.path.abspath(out_path)
    
    # Generate JS file
    js_content = "/* Practice Questions Database for CMO (Topics 01-08) */\n"
    js_content += "window.PRACTICE_DATA = window.PRACTICE_DATA || [];\n\n"
    js_content += "window.PRACTICE_DATA.push(\n"
    js_content += json.dumps(PRACTICE_CARDS, indent=2)
    js_content += "\n);\n"
    
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(js_content)
    
    print(f"Successfully generated {len(PRACTICE_CARDS)} practice cards in {out_path}!")

if __name__ == "__main__":
    main()
