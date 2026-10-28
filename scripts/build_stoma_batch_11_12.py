#!/usr/bin/env python3
"""
build_stoma_batch_11_12.py
Generates 6 flippable practice cards for StoMA Topics 11 and 12:
  Topic 11: Covariance Matrices and Linear Least Squares Estimation (3 cards)
  Topic 12: Conditional Expectation and MMSE Estimation (3 cards)
"""

import os
import re
import json

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PRACTICE_STOMA_11_12 = [
    # =========================================================================
    # TOPIC 11: Covariance & Linear Least Squares (LLSE)
    # =========================================================================
    {
        "id": 31191,
        "subject": "StoMA",
        "topicId": "11_Covariance_Matrices_and_Linear_Least_Squares_Estimation",
        "topicTitle": "11 · Covariance & Linear Least Squares (LLSE)",
        "title": "Scalar LLSE & Minimum Mean Squared Error (IISc Test 2)",
        "kind2": "pyq",
        "source": "IISc StoMA Test 2 2024 / Ross Ch 3",
        "marks": "[8 Marks]",
        "question": """<p>Let $X$ and $Y$ have means $\\mu_X = 2, \\mu_Y = 5$, variances $\\sigma_X^2 = 4, \\sigma_Y^2 = 9$, and correlation coefficient $\\rho = 0.6$.</p>
<p><span class="part">(a)</span> State the formula for the optimal scalar Linear Least Squares Estimator (LLSE) $\\hat{Y}(X) = a X + b$ minimizing $\\mathbb{E}[(Y - (aX + b))^2]$.</p>
<p><span class="part">(b)</span> Compute the numerical values of the optimal slope $a$ and intercept $b$, and write down the explicit estimator.</p>
<p><span class="part">(c)</span> Compute the resulting Minimum Mean Squared Error (MMSE) and determine what percentage of the variance of $Y$ is explained by $X$.</p>""",
        "solution": """<p><span class="part">Part (a): LLSE Formulation</span><br>
The optimal linear least squares estimator of a scalar random variable $Y$ given $X$ is:
$$\\hat{Y}(X) = \\mu_Y + \\rho \\frac{\\sigma_Y}{\\sigma_X}(X - \\mu_X) = \\mu_Y + \\frac{\\operatorname{Cov}(X, Y)}{\\sigma_X^2}(X - \\mu_X)$$
The optimal parameters are $a = \\rho \\frac{\\sigma_Y}{\\sigma_X}$ and $b = \\mu_Y - a\\mu_X$.</p>

<p><span class="part">Part (b): Parameter Calculation</span><br>
Given values: $\\mu_X = 2, \\mu_Y = 5, \\sigma_X = \\sqrt{4} = 2, \\sigma_Y = \\sqrt{9} = 3, \\rho = 0.6$.
- Slope $a$:
$$a = \\rho \\frac{\\sigma_Y}{\\sigma_X} = (0.6) \\times \\frac{3}{2} = (0.6)(1.5) = <span class=\"ans\">0.9</span>$$
- Intercept $b$:
$$b = \\mu_Y - a \\mu_X = 5 - (0.9)(2) = 5 - 1.8 = <span class=\"ans\">3.2</span>$$
The optimal linear estimator is:
$$<span class=\"ans\">\\hat{Y}(X) = 0.9 X + 3.2</span>$$</p>

<p><span class="part">Part (c): Residual Error Variance and $R^2$</span><br>
The minimum mean squared error achieved by the LLSE is:
$$\\mathbb{E}[(Y - \\hat{Y}(X))^2] = \\sigma_Y^2 (1 - \\rho^2)$$
Substituting $\\sigma_Y^2 = 9$ and $\\rho = 0.6$:
$$\\text{MMSE} = 9(1 - 0.6^2) = 9(1 - 0.36) = 9(0.64) = <span class=\"ans\">5.76</span>$$
The coefficient of determination $R^2$ represents the fraction of total variance explained by the linear model:
$$R^2 = \\rho^2 = (0.6)^2 = 0.36 = <span class=\"ans\">36\\%</span>$$
$36\\%$ of the variation in $Y$ is linearly explained by $X$, leaving $64\\%$ ($5.76 / 9$) as unexplained residual variance.</p>""",
        "takeaway": "Scalar LLSE is $\\hat{Y} = \\mu_Y + \\rho\\frac{\\sigma_Y}{\\sigma_X}(X - \\mu_X)$ with residual error variance $\\sigma_Y^2(1 - \\rho^2)$. The squared correlation $\\rho^2$ is the exact proportion of variance explained by linear regression."
    },
    {
        "id": 31192,
        "subject": "StoMA",
        "topicId": "11_Covariance_Matrices_and_Linear_Least_Squares_Estimation",
        "topicTitle": "11 · Covariance & Linear Least Squares (LLSE)",
        "title": "Orthogonality Principle of LLSE in Hilbert Spaces (Stanford EE263 / Boyd)",
        "kind2": "pyq",
        "source": "Stanford EE263 / Boyd Ch 6",
        "marks": "[10 Marks]",
        "question": """<p>Let $X \\in \\mathbb{R}^n$ and $Y \\in \\mathbb{R}$ be zero-mean random variables with covariance matrix $\\Sigma_{XX} = \\mathbb{E}[XX^\\top] \\succ 0$ and cross-covariance vector $\\Sigma_{XY} = \\mathbb{E}[XY]$.</p>
<p><span class="part">(a)</span> State the <strong>Orthogonality Principle</strong>: prove that the error $Y - a^\\top X$ is orthogonal to the observation vector $X$ (i.e., $\\mathbb{E}[(Y - a^\\top X)X] = 0$) if and only if $a$ minimizes the mean squared error $\\mathbb{E}[(Y - a^\\top X)^2]$.</p>
<p><span class="part">(b)</span> Solve the orthogonality condition to derive the optimal weight vector $a^*$.</p>
<p><span class="part">(c)</span> Prove the <strong>Pythagorean Theorem for random variables</strong>: show that for any other linear estimator $c^\\top X$,
$$\\mathbb{E}[(Y - c^\\top X)^2] = \\mathbb{E}[(Y - a^{*\\top} X)^2] + \\mathbb{E}[(a^{*\\top} X - c^\\top X)^2]$$</p>""",
        "solution": """<p><span class="part">Part (a): Necessity and Sufficiency of Orthogonality</span><br>
Let $e(a) = Y - a^\\top X$ be the estimation error. Let $a^*$ satisfy the orthogonality condition:
$$\\mathbb{E}[(Y - a^{*\\top} X) X] = 0$$
For any arbitrary weight vector $a = a^* + \\Delta a$:
$$e(a) = Y - (a^* + \\Delta a)^\\top X = (Y - a^{*\\top} X) - \\Delta a^\\top X = e(a^*) - \\Delta a^\\top X$$
Expanding the mean squared error:
$$\\mathbb{E}[e(a)^2] = \\mathbb{E}[(e(a^*) - \\Delta a^\\top X)^2] = \\mathbb{E}[e(a^*)^2] - 2 \\Delta a^\\top \\mathbb{E}[e(a^*) X] + \\mathbb{E}[(\\Delta a^\\top X)^2]$$
Notice that by orthogonality, the cross-term vanishes: $\\mathbb{E}[e(a^*) X] = 0$.<br>
Therefore:
$$\\mathbb{E}[e(a)^2] = \\mathbb{E}[e(a^*)^2] + \\Delta a^\\top \\mathbb{E}[X X^\\top] \\Delta a = \\mathbb{E}[e(a^*)^2] + \\Delta a^\\top \\Sigma_{XX} \\Delta a$$
Since $\\Sigma_{XX} \\succ 0$, $\\Delta a^\\top \\Sigma_{XX} \\Delta a > 0$ for all $\\Delta a \\ne 0$.<br>
<span class=\"ans\">Thus $\\mathbb{E}[e(a)^2] > \\mathbb{E}[e(a^*)^2]$ for any $a \\ne a^*$, proving that orthogonality is necessary and sufficient for the global unique minimum!</span></p>

<p><span class="part">Part (b): Explicit Derivation of $a^*$</span><br>
Set the orthogonality condition to zero:
$$\\mathbb{E}[(Y - a^\\top X)X] = \\mathbb{E}[YX] - \\mathbb{E}[XX^\\top] a = \\Sigma_{XY} - \\Sigma_{XX} a = 0$$
$$\\Sigma_{XX} a = \\Sigma_{XY} \\implies <span class=\"ans\">a^* = \\Sigma_{XX}^{-1} \\Sigma_{XY}</span>$$</p>

<p><span class="part">Part (c): Pythagorean Decomposition</span><br>
Decompose the error for an arbitrary linear estimator $c^\\top X$:
$$Y - c^\\top X = (Y - a^{*\\top} X) + (a^{*\\top} X - c^\\top X) = e^* + \\Delta \\hat{Y}$$
where $e^* = Y - a^{*\\top} X$ and $\\Delta \\hat{Y} = (a^* - c)^\\top X$.<br>
Taking the squared expectation:
$$\\mathbb{E}[(Y - c^\\top X)^2] = \\mathbb{E}[(e^* + \\Delta \\hat{Y})^2] = \\mathbb{E}[(e^*)^2] + 2\\mathbb{E}[e^* \\Delta \\hat{Y}] + \\mathbb{E}[(\\Delta \\hat{Y})^2]$$
Evaluate the inner product cross-term:
$$\\mathbb{E}[e^* \\Delta \\hat{Y}] = \\mathbb{E}[e^* (a^* - c)^\\top X] = (a^* - c)^\\top \\mathbb{E}[e^* X] = (a^* - c)^\\top (0) = 0$$
The cross-term is identically zero by orthogonality! Thus:
$$<span class=\"ans\">\\mathbb{E}[(Y - c^\\top X)^2] = \\mathbb{E}[(Y - a^{*\\top} X)^2] + \\mathbb{E}[(a^{*\\top} X - c^\\top X)^2]</span>$$
Geometrically, $Y$ is a vector in $L^2(\\mathbb{P})$, $\\hat{Y}^* = a^{*\\top} X$ is its orthogonal projection onto the linear subspace spanned by $X$, and $e^* \\perp \\text{span}(X)$.</p>""",
        "takeaway": "The Orthogonality Principle states that estimation error must be orthogonal to all observations: $\\mathbb{E}[(Y - \\hat{Y})X] = 0$. In $L^2$ Hilbert space, this is the Pythagorean theorem: any other estimator adds strictly positive orthogonal error $\\|\\hat{Y}^* - c^\\top X\\|^2$."
    },
    {
        "id": 31193,
        "subject": "StoMA",
        "topicId": "11_Covariance_Matrices_and_Linear_Least_Squares_Estimation",
        "topicTitle": "11 · Covariance & Linear Least Squares (LLSE)",
        "title": "Positive Semidefiniteness & Degeneracy of Covariance Matrices (Generated Exam)",
        "kind2": "practice",
        "source": "Berkeley EECS 126 / MIT Benchmark",
        "marks": "[10 Marks]",
        "question": """<p>Let $X = (X_1, X_2, \\dots, X_n)^\\top$ be a random vector with mean $\\mu = \\mathbb{E}[X]$ and covariance matrix $\\Sigma = \\mathbb{E}[(X - \\mu)(X - \\mu)^\\top]$.</p>
<p><span class="part">(a)</span> Rigorously prove that $\\Sigma$ is symmetric and positive semidefinite ($\\Sigma \\succeq 0$): $v^\\top \\Sigma v \\ge 0$ for all $v \\in \\mathbb{R}^n$.</p>
<p><span class="part">(b)</span> Under what exact mathematical condition on the random vector $X$ is $\\Sigma$ singular (i.e., not strictly positive definite, $\\det(\\Sigma) = 0$)?</p>
<p><span class="part">(c)</span> If $\\Sigma$ is singular with nullspace vector $v \\ne 0$ ($v^\\top \\Sigma v = 0$), what geometric structure does the probability distribution of $X$ occupy in $\\mathbb{R}^n$?</p>""",
        "solution": """<p><span class="part">Part (a): Symmetry and Positive Semidefiniteness</span><br>
1. <strong>Symmetry:</strong>
$$\\Sigma^\\top = \\left( \\mathbb{E}[(X - \\mu)(X - \\mu)^\\top] \\right)^\\top = \\mathbb{E}\\left[ \\left( (X - \\mu)(X - \\mu)^\\top \\right)^\\top \\right] = \\mathbb{E}[(X - \\mu)(X - \\mu)^\\top] = \\Sigma$$
2. <strong>Positive Semidefiniteness:</strong> Let $v \\in \\mathbb{R}^n$ be any deterministic vector.
$$v^\\top \\Sigma v = v^\\top \\mathbb{E}[(X - \\mu)(X - \\mu)^\\top] v = \\mathbb{E}\\left[ v^\\top (X - \\mu)(X - \\mu)^\\top v \\right]$$
Notice that $v^\\top (X - \\mu)$ is a scalar random variable, so:
$$v^\\top (X - \\mu)(X - \\mu)^\\top v = \\left( v^\\top (X - \\mu) \\right)^2$$
Therefore:
$$v^\\top \\Sigma v = \\mathbb{E}\\left[ \\left( v^\\top (X - \\mu) \\right)^2 \\right] = \\operatorname{Var}(v^\\top X)$$
Since the square of any real number is non-negative, $\\left(v^\\top (X - \\mu)\\right)^2 \\ge 0$ almost surely.<br>
By monotonicity of expectation:
$$<span class=\"ans\">v^\\top \\Sigma v \\ge 0 \\quad \\forall v \\in \\mathbb{R}^n \\implies \\Sigma \\succeq 0</span>$$</p>

<p><span class="part">Part (b): Condition for Singularity</span><br>
$\\Sigma$ is singular if and only if there exists a non-zero vector $v \\in \\mathbb{R}^n \\setminus \\{0\\}$ such that:
$$v^\\top \\Sigma v = 0 \\iff \\mathbb{E}\\left[ \\left( v^\\top (X - \\mu) \\right)^2 \\right] = 0$$
A non-negative random variable has expectation 0 if and only if it is identically zero almost surely.<br>
Therefore:
$$v^\\top (X - \\mu) = 0 \\quad \\text{a.s.} \\iff <span class=\"ans\">v^\\top X = v^\\top \\mu = c \\quad \\text{almost surely}</span>$$
<span class=\"ans\">$\\Sigma$ is singular if and only if there exists a deterministic linear combination of the components of $X$ that is almost surely constant (the components are affinely dependent).</span></p>

<p><span class="part">Part (c): Geometric Interpretation of Degeneracy</span><br>
The equation $v^\\top X = c$ defines an $(n-1)$-dimensional affine hyperplane in $\\mathbb{R}^n$.<br>
If $\\Sigma$ is singular with rank $r < n$, then $n - r$ independent linear constraints $v_k^\\top X = c_k$ hold almost surely.<br>
Consequently:
- <strong>100% of the probability mass</strong> of $X$ is supported on an $r$-dimensional affine subspace of $\\mathbb{R}^n$.<br>
- The distribution is <strong>degenerate</strong>: it has zero volume (Lebesgue measure zero) in $\\mathbb{R}^n$, meaning no $n$-dimensional joint PDF exists (no Gaussian density formula with $\\det(\\Sigma)^{-1/2}$).</p>""",
        "takeaway": "Every covariance matrix is positive semidefinite $\\Sigma \\succeq 0$ because $v^\\top \\Sigma v = \\operatorname{Var}(v^\\top X) \\ge 0$. It is singular if and only if $X$ is trapped on an affine hyperplane $v^\\top X = c$ a.s., collapsing the distribution into lower dimensions."
    },

    # =========================================================================
    # TOPIC 12: Conditional Expectation & MMSE
    # =========================================================================
    {
        "id": 31291,
        "subject": "StoMA",
        "topicId": "12_Conditional_Expectation_and_MMSE_Estimation",
        "topicTitle": "12 · Conditional Expectation & MMSE",
        "title": "Compound Poisson Revenue & Eve's Law of Total Variance (IISc Midterm 2)",
        "kind2": "pyq",
        "source": "IISc StoMA Midterm 2 2024 / Ross Ch 3",
        "marks": "[8 Marks]",
        "question": """<p>Let $N \\sim \\text{Poisson}(\\lambda)$ be the number of customers entering a store in a day. Each customer $i$ independently spends an amount $X_i$, where $\\{X_i\\}_{i=1}^\\infty$ are i.i.d. positive random variables with mean $\\mu$ and variance $\\sigma^2$, independent of $N$.</p>
<p>Let $S_N = \\sum_{i=1}^N X_i$ be the total daily revenue (with $S_0 = 0$).</p>
<p><span class="part">(a)</span> Using the <strong>Law of Total Expectation</strong> (Tower Property), compute the expected daily revenue $\\mathbb{E}[S_N]$.</p>
<p><span class="part">(b)</span> Using the <strong>Law of Total Variance</strong> (Eve's Law):
$$\\operatorname{Var}(S_N) = \\mathbb{E}[\\operatorname{Var}(S_N \\mid N)] + \\operatorname{Var}(\\mathbb{E}[S_N \\mid N])$$
derive the exact variance $\\operatorname{Var}(S_N)$ in terms of $\\lambda, \\mu, \\sigma^2$.</p>
<p><span class="part">(c)</span> Provide the physical interpretation of each of the two variance components.</p>""",
        "solution": """<p><span class="part">Part (a): Expected Total Revenue via Tower Property</span><br>
Condition on the customer count $N = n$:
$$\\mathbb{E}[S_N \\mid N = n] = \\mathbb{E}\\left[ \\sum_{i=1}^n X_i \\right] = \\sum_{i=1}^n \\mathbb{E}[X_i] = n\\mu$$
Therefore, as a random variable:
$$\\mathbb{E}[S_N \\mid N] = \\mu N$$
Applying the Law of Total Expectation:
$$\\mathbb{E}[S_N] = \\mathbb{E}[\\mathbb{E}[S_N \\mid N]] = \\mathbb{E}[\\mu N] = \\mu \\mathbb{E}[N] = <span class=\"ans\">\\lambda \\mu</span>$$</p>

<p><span class="part">Part (b): Variance via Eve's Law</span><br>
Conditioned on $N = n$, $S_N$ is the sum of $n$ independent random variables with variance $\\sigma^2$:
$$\\operatorname{Var}(S_N \\mid N = n) = \\operatorname{Var}\\left( \\sum_{i=1}^n X_i \\right) = \\sum_{i=1}^n \\operatorname{Var}(X_i) = n\\sigma^2$$
Therefore, the conditional variance as a random variable is:
$$\\operatorname{Var}(S_N \\mid N) = \\sigma^2 N$$
Now evaluate the two terms in Eve's Law:
1. <strong>Expected Conditional Variance:</strong>
$$\\mathbb{E}[\\operatorname{Var}(S_N \\mid N)] = \\mathbb{E}[\\sigma^2 N] = \\sigma^2 \\mathbb{E}[N] = \\lambda \\sigma^2$$
2. <strong>Variance of Conditional Expectation:</strong>
$$\\operatorname{Var}(\\mathbb{E}[S_N \\mid N]) = \\operatorname{Var}(\\mu N) = \\mu^2 \\operatorname{Var}(N) = \\mu^2 \\lambda \\quad (\\text{since } \\operatorname{Var}(N) = \\lambda \\text{ for Poisson})$$
Adding both components:
$$\\operatorname{Var}(S_N) = \\lambda \\sigma^2 + \\lambda \\mu^2 = <span class=\"ans\">\\lambda (\\sigma^2 + \\mu^2) = \\lambda \\mathbb{E}[X^2]</span>$$</p>

<p><span class="part">Part (c): Physical Meaning of the Components</span><br>
- $\\mathbb{E}[\\operatorname{Var}(S_N \\mid N)] = \\lambda \\sigma^2$: represents <strong>within-group variance</strong> (the volatility in individual spending habits among a fixed number of shoppers).<br>
- $\\operatorname{Var}(\\mathbb{E}[S_N \\mid N]) = \\lambda \\mu^2$: represents <strong>between-group variance</strong> (the macro-volatility due to random fluctuations in the total customer footfall $N$).</p>""",
        "takeaway": "Eve's Law $\\operatorname{Var}(Y) = \\mathbb{E}[\\operatorname{Var}(Y|X)] + \\operatorname{Var}(\\mathbb{E}[Y|X])$ cleanly decomposes total variance into within-group spending noise $\\lambda\\sigma^2$ and between-group crowd noise $\\lambda\\mu^2$. For Poisson sums, $\\operatorname{Var}(S_N) = \\lambda \\mathbb{E}[X^2]$."
    },
    {
        "id": 31292,
        "subject": "StoMA",
        "topicId": "12_Conditional_Expectation_and_MMSE_Estimation",
        "topicTitle": "12 · Conditional Expectation & MMSE",
        "title": "Non-Linear MMSE Estimator as Conditional Expectation (Stanford Stats 116)",
        "kind2": "pyq",
        "source": "Stanford Stats 116 / Ross 3.4",
        "marks": "[10 Marks]",
        "question": """<p>Let $(X, Y)$ have the joint probability density function:
$$f_{X,Y}(x, y) = 8xy, \\quad 0 \\le y \\le x \\le 1$$</p>
<p><span class="part">(a)</span> Derive the optimal Minimum Mean Squared Error (MMSE) estimator $\\hat{Y}_{\\text{MMSE}}(X) = \\mathbb{E}[Y \\mid X]$ among ALL possible functions $g(X)$.</p>
<p><span class="part">(b)</span> Compute the resulting minimum mean squared error $\\mathbb{E}[(Y - \\hat{Y}_{\\text{MMSE}}(X))^2]$.</p>
<p><span class="part">(c)</span> Compare this result with the Linear Least Squares Estimator $\\hat{Y}_{\\text{LLSE}}(X)$. When does LLSE coincide with MMSE?</p>""",
        "solution": """<p><span class="part">Part (a): Derivation of MMSE Estimator</span><br>
For a fixed $x \\in [0, 1]$, $y$ ranges from $0$ to $x$. Compute the marginal density $f_X(x)$:
$$f_X(x) = \\int_0^x 8xy \\, dy = 8x \\left[ \\frac{y^2}{2} \\right]_0^x = 4x^3, \\quad 0 \\le x \\le 1$$
The conditional density of $Y$ given $X = x$ is:
$$f_{Y|X}(y \\mid x) = \\frac{f_{X,Y}(x, y)}{f_X(x)} = \\frac{8xy}{4x^3} = \\frac{2y}{x^2}, \\quad 0 \\le y \\le x$$
The MMSE estimator is the conditional expectation:
$$\\hat{Y}_{\\text{MMSE}}(x) = \\mathbb{E}[Y \\mid X = x] = \\int_0^x y \\left( \\frac{2y}{x^2} \\right) dy = \\frac{2}{x^2} \\left[ \\frac{y^3}{3} \\right]_0^x = \\frac{2}{x^2} \\frac{x^3}{3} = <span class=\"ans\">\\frac{2}{3}x</span>$$
Thus $\\hat{Y}_{\\text{MMSE}}(X) = \\frac{2}{3}X$.</p>

<p><span class="part">Part (b): Minimum Mean Squared Error Calculation</span><br>
The residual error variance is $\\mathbb{E}[(Y - \\hat{Y})^2] = \\mathbb{E}[\\operatorname{Var}(Y \\mid X)]$.<br>
Compute the conditional second moment:
$$\\mathbb{E}[Y^2 \\mid X = x] = \\int_0^x y^2 \\left(\\frac{2y}{x^2}\\right) dy = \\frac{2}{x^2} \\left[ \\frac{y^4}{4} \\right]_0^x = \\frac{x^2}{2}$$
The conditional variance is:
$$\\operatorname{Var}(Y \\mid X = x) = \\mathbb{E}[Y^2 \\mid X = x] - (\\mathbb{E}[Y \\mid X = x])^2 = \\frac{x^2}{2} - \\left(\\frac{2x}{3}\\right)^2 = \\frac{x^2}{2} - \\frac{4x^2}{9} = \\frac{x^2}{18}$$
Taking the expectation over $X$:
$$\\text{MMSE} = \\mathbb{E}\\left[ \\frac{X^2}{18} \\right] = \\frac{1}{18} \\int_0^1 x^2 (4x^3) \\, dx = \\frac{4}{18} \\int_0^1 x^5 \\, dx = \\frac{2}{9} \\left[ \\frac{x^6}{6} \\right]_0^1 = \\frac{2}{54} = <span class=\"ans\">\\frac{1}{27} \\approx 0.03704</span>$$</p>

<p><span class="part">Part (c): Comparison with LLSE</span><br>
Notice that the optimal unrestricted MMSE estimator $\\hat{Y}_{\\text{MMSE}}(X) = \\frac{2}{3}X$ is <strong>strictly linear</strong> in $X$!<br>
Because the best possible non-linear function happens to lie in the space of linear functions:
$$\\hat{Y}_{\\text{LLSE}}(X) \\equiv \\hat{Y}_{\\text{MMSE}}(X) = \\frac{2}{3}X$$
<span class=\"ans\">Whenever the conditional expectation $\\mathbb{E}[Y \\mid X]$ is an affine function of $X$ (as in Joint Gaussian distributions or symmetric models), the simple LLSE achieves the exact same performance as the globally optimal non-linear MMSE estimator.</span></p>""",
        "takeaway": "The conditional expectation $\\hat{Y} = \\mathbb{E}[Y|X]$ minimizes MSE across ALL functions (non-linear or linear). Its residual error is the expected conditional variance $\\mathbb{E}[\\operatorname{Var}(Y|X)]$. When $\\mathbb{E}[Y|X]$ is linear, LLSE is globally optimal."
    },
    {
        "id": 31293,
        "subject": "StoMA",
        "topicId": "12_Conditional_Expectation_and_MMSE_Estimation",
        "topicTitle": "12 · Conditional Expectation & MMSE",
        "title": "Tower Property, Nested Conditioning & Orthogonal Projections (Generated Exam)",
        "kind2": "practice",
        "source": "Berkeley EECS 126 / MIT Benchmark",
        "marks": "[10 Marks]",
        "question": """<p>Let $(\\Omega, \\mathcal{F}, \\mathbb{P})$ be a probability space with sub-$\\sigma$-algebras $\\mathcal{H}_1 \\subset \\mathcal{H}_2 \\subset \\mathcal{F}$ representing nested information filtrations (e.g. $\\mathcal{H}_1 = \\sigma(X)$ and $\\mathcal{H}_2 = \\sigma(X, Z)$).</p>
<p><span class="part">(a)</span> State and prove the <strong>Tower Property</strong> of conditional expectation:
$$\\mathbb{E}[\\mathbb{E}[Y \\mid \\mathcal{H}_2] \\mid \\mathcal{H}_1] = \\mathbb{E}[Y \\mid \\mathcal{H}_1]$$</p>
<p><span class="part">(b)</span> Show that the reverse conditioning also satisfies:
$$\\mathbb{E}[\\mathbb{E}[Y \\mid \\mathcal{H}_1] \\mid \\mathcal{H}_2] = \\mathbb{E}[Y \\mid \\mathcal{H}_1]$$
Explain why the \"smaller information set always dominates\".</p>
<p><span class="part">(c)</span> Interpret this identity as successive orthogonal projections $P_1$ and $P_2$ in the Hilbert space $L^2(\\Omega, \\mathcal{F}, \\mathbb{P})$.</p>""",
        "solution": """<p><span class="part">Part (a): Measure-Theoretic Proof of Tower Property</span><br>
Recall Kolmogorov's definition: $W = \\mathbb{E}[Y \\mid \\mathcal{H}_1]$ is the unique $\\mathcal{H}_1$-measurable random variable satisfying:
$$\\int_H W \\, d\\mathbb{P} = \\int_H Y \\, d\\mathbb{P} \\quad \\forall H \\in \\mathcal{H}_1$$
Let $V = \\mathbb{E}[\\mathbb{E}[Y \\mid \\mathcal{H}_2] \\mid \\mathcal{H}_1]$. We verify that $V$ satisfies the definition of $\\mathbb{E}[Y \\mid \\mathcal{H}_1]$:
1. By construction of the outer conditional expectation, $V$ is $\\mathcal{H}_1$-measurable.<br>
2. Let $H \\in \\mathcal{H}_1$ be arbitrary. Since $\\mathcal{H}_1 \\subset \\mathcal{H}_2$, we also have $H \\in \\mathcal{H}_2$.<br>
Applying the definition of conditional expectation with respect to $\\mathcal{H}_1$:
$$\\int_H V \\, d\\mathbb{P} = \\int_H \\mathbb{E}[Y \\mid \\mathcal{H}_2] \\, d\\mathbb{P}$$
Now applying the definition of conditional expectation with respect to $\\mathcal{H}_2$ for the set $H \\in \\mathcal{H}_2$:
$$\\int_H \\mathbb{E}[Y \\mid \\mathcal{H}_2] \\, d\\mathbb{P} = \\int_H Y \\, d\\mathbb{P}$$
Combining these two equalities:
$$\\int_H V \\, d\\mathbb{P} = \\int_H Y \\, d\\mathbb{P} \\quad \\forall H \\in \\mathcal{H}_1$$
By the uniqueness of conditional expectation almost surely:
$$<span class=\"ans\">\\mathbb{E}[\\mathbb{E}[Y \\mid \\mathcal{H}_2] \\mid \\mathcal{H}_1] = \\mathbb{E}[Y \\mid \\mathcal{H}_1]</span>$$</p>

<p><span class="part">Part (b): Reverse Conditioning & Information Coarseness</span><br>
Consider $U = \\mathbb{E}[Y \\mid \\mathcal{H}_1]$. By definition, $U$ is $\\mathcal{H}_1$-measurable.<br>
Since $\\mathcal{H}_1 \\subset \\mathcal{H}_2$, any $\\mathcal{H}_1$-measurable random variable is automatically $\\mathcal{H}_2$-measurable.<br>
Conditioning a random variable on a $\\sigma$-algebra that already contains all of its information leaves it unchanged ($\"\\text{taking out what is known}\"$):
$$\\mathbb{E}[U \\mid \\mathcal{H}_2] = U \\implies <span class=\"ans\">\\mathbb{E}[\\mathbb{E}[Y \\mid \\mathcal{H}_1] \\mid \\mathcal{H}_2] = \\mathbb{E}[Y \\mid \\mathcal{H}_1]</span>$$
<span class=\"ans\">The smaller information set always wins:</span> if you have coarse information $\\mathcal{H}_1$ and fine information $\\mathcal{H}_2$, the joint estimation can never be more informative than the coarser constraint.</p>

<p><span class="part">Part (c): Hilbert Space Projection Interpretation</span><br>
In $L^2(\\Omega, \\mathcal{F}, \\mathbb{P})$, conditional expectation onto a sub-$\\sigma$-algebra $\\mathcal{H}$ is the <strong>orthogonal projection operator</strong> onto the closed subspace $L^2(\\mathcal{H})$.<br>
Since $\\mathcal{H}_1 \\subset \\mathcal{H}_2$, the subspace $L^2(\\mathcal{H}_1)$ is an embedded subspace of $L^2(\\mathcal{H}_2)$:
$$L^2(\\mathcal{H}_1) \\subseteq L^2(\\mathcal{H}_2) \\subseteq L^2(\\mathcal{F})$$
Let $P_1$ and $P_2$ be the orthogonal projection operators onto $L^2(\\mathcal{H}_1)$ and $L^2(\\mathcal{H}_2)$ respectively.<br>
By standard linear algebra of nested orthogonal projections:
$$P_1 P_2 = P_2 P_1 = P_1$$
Projecting a vector $Y$ onto the larger subspace $L^2(\\mathcal{H}_2)$ and subsequently projecting onto the smaller subspace $L^2(\\mathcal{H}_1)$ is identical to projecting directly onto $L^2(\\mathcal{H}_1)$.</p>""",
        "takeaway": "The Tower Property $\\mathbb{E}[\\mathbb{E}[Y|\\mathcal{H}_2]|\\mathcal{H}_1] = \\mathbb{E}[Y|\\mathcal{H}_1]$ for $\\mathcal{H}_1 \\subset \\mathcal{H}_2$ reflects idempotent orthogonal projections: $P_1 P_2 = P_1$. The coarser information set strictly dominates."
    }
]

def append_to_practice_stoma():
    stoma_file = os.path.join(REPO_DIR, "practice_stoma.js")
    existing_cards = []
    if os.path.exists(stoma_file):
        with open(stoma_file, "r", encoding="utf-8") as f:
            content = f.read()
        try:
            m = re.search(r'window\.PRACTICE_DATA\.push\(\s*(\[[\s\S]*?\])\s*\);', content)
            if m:
                existing_cards = json.loads(m.group(1))
        except Exception as e:
            print(f"Warning: Could not parse existing cards: {e}")

    card_dict = {c["id"]: c for c in existing_cards}
    for c in PRACTICE_STOMA_11_12:
        card_dict[c["id"]] = c
    merged_cards = sorted(card_dict.values(), key=lambda x: x["id"])

    js_code = "/* Practice Questions Database for StoMA (Stochastic Models & Applications) */\n"
    js_code += "window.PRACTICE_DATA = window.PRACTICE_DATA || [];\n\n"
    js_code += "window.PRACTICE_DATA.push(\n"
    js_code += json.dumps(merged_cards, indent=2, ensure_ascii=False)
    js_code += "\n);\n"

    with open(stoma_file, "w", encoding="utf-8") as f:
        f.write(js_code)

    print(f"Successfully wrote {len(merged_cards)} cards to {stoma_file}")

if __name__ == "__main__":
    append_to_practice_stoma()
