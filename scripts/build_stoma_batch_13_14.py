#!/usr/bin/env python3
"""
build_stoma_batch_13_14.py
Generates 6 flippable practice cards for StoMA Topics 13 and 14:
  Topic 13: Jointly Gaussian Random Variables (3 cards)
  Topic 14: Random Sums and Wald's Equation (3 cards)
"""

import os
import re
import json

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PRACTICE_STOMA_13_14 = [
    # =========================================================================
    # TOPIC 13: Jointly Gaussian Random Variables
    # =========================================================================
    {
        "id": 31391,
        "subject": "StoMA",
        "topicId": "13_Jointly_Gaussian_Random_Variables",
        "topicTitle": "13 · Jointly Gaussian Random Variables",
        "title": "Bivariate Gaussian Matrix Identification & Conditional Slicing (IISc Test 2)",
        "kind2": "pyq",
        "source": "IISc StoMA Test 2 2024 / Ross Ch 3",
        "marks": "[8 Marks]",
        "question": """<p>Let $(X, Y)$ have the joint probability density function:
$$f_{X,Y}(x, y) = c \\exp\\left( -\\frac{1}{2}(2x^2 - 2xy + y^2) \\right)$$
Without evaluating any integrals:</p>
<p><span class="part">(a)</span> Express the quadratic form in matrix notation $z^\\top \\Sigma^{-1} z$ and determine the exact covariance matrix $\\Sigma$.</p>
<p><span class="part">(b)</span> Find the normalization constant $c$, means $\\mu_X, \\mu_Y$, variances $\\sigma_X^2, \\sigma_Y^2$, and the correlation coefficient $\\rho$.</p>
<p><span class="part">(c)</span> Derive the conditional distribution of $X$ given $Y = y$ (conditional mean and conditional variance).</p>""",
        "solution": """<p><span class="part">Part (a): Inverse Covariance Matrix Identification</span><br>
The exponent of a zero-mean bivariate normal distribution is $-\\frac{1}{2} z^\\top \\Sigma^{-1} z$ where $z = \\begin{bmatrix} x \\\\ y \\end{bmatrix}$.<br>
Express the polynomial as a symmetric quadratic form:
$$2x^2 - 2xy + y^2 = \\begin{bmatrix} x & y \\end{bmatrix} \\begin{bmatrix} 2 & -1 \\\\ -1 & 1 \\end{bmatrix} \\begin{bmatrix} x \\\\ y \\end{bmatrix} \\implies \\Sigma^{-1} = \\begin{bmatrix} 2 & -1 \\\\ -1 & 1 \\end{bmatrix}$$
Compute the determinant of $\\Sigma^{-1}$:
$$\\det(\\Sigma^{-1}) = (2)(1) - (-1)^2 = 2 - 1 = 1 \\implies \\det(\\Sigma) = \\frac{1}{\\det(\\Sigma^{-1})} = 1$$
Invert the $2 \\times 2$ matrix:
$$\\Sigma = (\\Sigma^{-1})^{-1} = \\frac{1}{1} \\begin{bmatrix} 1 & 1 \\\\ 1 & 2 \\end{bmatrix} = <span class=\"ans\">\\begin{bmatrix} 1 & 1 \\\\ 1 & 2 \\end{bmatrix}</span>$$</p>

<p><span class="part">Part (b): Parameters from Covariance Matrix</span><br>
- <strong>Means:</strong> Since there are no linear terms in the exponent, $\\mu_X = 0$ and $\\mu_Y = 0$.<br>
- <strong>Variances:</strong>
$$\\sigma_X^2 = \\Sigma_{11} = <span class=\"ans\">1</span>, \\qquad \\sigma_Y^2 = \\Sigma_{22} = <span class=\"ans\">2</span>$$
- <strong>Covariance:</strong> $\\operatorname{Cov}(X, Y) = \\Sigma_{12} = 1$.<br>
- <strong>Correlation:</strong>
$$\\rho = \\frac{\\operatorname{Cov}(X, Y)}{\\sigma_X \\sigma_Y} = \\frac{1}{\\sqrt{1} \\times \\sqrt{2}} = <span class=\"ans\">\\frac{1}{\\sqrt{2}} \\approx 0.7071</span>$$
- <strong>Normalization Constant:</strong>
$$c = \\frac{1}{2\\pi \\sqrt{\\det(\\Sigma)}} = \\frac{1}{2\\pi \\sqrt{1}} = <span class=\"ans\">\\frac{1}{2\\pi}</span>$$</p>

<p><span class="part">Part (c): Conditional Gaussian Slicing</span><br>
For any jointly Gaussian pair, the conditional distribution $X \\mid Y = y$ is Gaussian $\\mathcal{N}(\\mu_{X|Y}, \\sigma_{X|Y}^2)$:
- <strong>Conditional Mean:</strong>
$$\\mu_{X|Y} = \\mu_X + \\rho \\frac{\\sigma_X}{\\sigma_Y}(y - \\mu_Y) = 0 + \\left(\\frac{1}{\\sqrt{2}}\\right)\\left(\\frac{1}{\\sqrt{2}}\\right)(y - 0) = <span class=\"ans\">\\frac{y}{2}</span>$$
- <strong>Conditional Variance:</strong>
$$\\sigma_{X|Y}^2 = \\sigma_X^2 (1 - \\rho^2) = 1 \\left( 1 - \\frac{1}{2} \\right) = <span class=\"ans\">\\frac{1}{2}</span>$$
<span class=\"ans\">Thus $X \\mid Y = y \\sim \\mathcal{N}\\left( \\frac{y}{2}, \\frac{1}{2} \\right)$.</span></p>""",
        "takeaway": "Never integrate Gaussian densities: match the exponent directly to $-\\frac{1}{2}z^\\top \\Sigma^{-1} z$. Inverting $\\Sigma^{-1}$ yields all variances, covariances, and conditional slices $\\mu_{X|Y} = \\frac{\\operatorname{Cov}(X,Y)}{\\sigma_Y^2} y$ immediately."
    },
    {
        "id": 31392,
        "subject": "StoMA",
        "topicId": "13_Jointly_Gaussian_Random_Variables",
        "topicTitle": "13 · Jointly Gaussian Random Variables",
        "title": "Marginally Normal + Uncorrelated ≠ Independent / Jointly Normal (Stanford Stats 116)",
        "kind2": "pyq",
        "source": "Stanford Stats 116 / Ross Ch 3",
        "marks": "[10 Marks]",
        "question": """<p><span class="part">(a)</span> State the definition of a <strong>jointly Gaussian (multivariate normal)</strong> random vector.</p>
<p><span class="part">(b)</span> Construct an explicit counterexample: two random variables $X$ and $Y$ that are individually standard normal ($X, Y \\sim \\mathcal{N}(0, 1)$), completely uncorrelated ($\\operatorname{Cov}(X, Y) = 0$), yet are <strong>strictly dependent</strong> and <strong>not jointly Gaussian</strong>.</p>
<p><span class="part">(c)</span> Prove that their sum $X + Y$ is not normally distributed, violating the fundamental linear combination property of jointly Gaussian variables.</p>""",
        "solution": """<p><span class="part">Part (a): Definition of Jointly Gaussian Vector</span><br>
A random vector $(X_1, \\dots, X_n)$ is <strong>jointly Gaussian</strong> if and only if every linear combination $\\sum_{i=1}^n a_i X_i$ is a one-dimensional Gaussian random variable for all $a \\in \\mathbb{R}^n$.</p>

<p><span class="part">Part (b): Classical Counterexample Construction</span><br>
Let $X \\sim \\mathcal{N}(0, 1)$ be a standard normal random variable.<br>
Let $S$ be an independent Rademacher sign random variable:
$$\\mathbb{P}(S = +1) = \\frac{1}{2}, \\qquad \\mathbb{P}(S = -1) = \\frac{1}{2}, \\qquad S \\perp X$$
Define $Y = S X$.<br>
1. <strong>Marginal Normality of $Y$:</strong> For any $y \\in \\mathbb{R}$:
$$\\begin{aligned}
\\mathbb{P}(Y \\le y) &= \\mathbb{P}(SX \\le y \\mid S = 1)\\mathbb{P}(S = 1) + \\mathbb{P}(SX \\le y \\mid S = -1)\\mathbb{P}(S = -1) \\\\
&= \\frac{1}{2}\\mathbb{P}(X \\le y) + \\frac{1}{2}\\mathbb{P}(-X \\le y) = \\frac{1}{2}\\Phi(y) + \\frac{1}{2}\\Phi(y) = \\Phi(y)
\\end{aligned}$$
where we used the symmetry of the standard normal distribution $\\mathbb{P}(-X \\le y) = \\mathbb{P}(X \\ge -y) = \\Phi(y)$.<br>
Thus <span class=\"ans\">$Y \\sim \\mathcal{N}(0, 1)$ is standard normal!</span><br>
2. <strong>Uncorrelatedness:</strong> $\\mathbb{E}[X] = 0, \\mathbb{E}[Y] = \\mathbb{E}[S]\\mathbb{E}[X] = (0)(0) = 0$.
$$\\operatorname{Cov}(X, Y) = \\mathbb{E}[XY] = \\mathbb{E}[X(SX)] = \\mathbb{E}[S X^2] = \\mathbb{E}[S]\\mathbb{E}[X^2] = (0)(1) = <span class=\"ans\">0</span>$$
3. <strong>Strict Dependence:</strong> $|Y| = |SX| = |S| |X| = |X|$.<br>
Therefore, $Y^2 = X^2$ almost surely: $\\mathbb{P}(Y^2 = X^2) = 1$.<br>
If $X$ and $Y$ were independent continuous random variables, $\\mathbb{P}(Y^2 = X^2) = 0$.<br>
<span class=\"ans\">Knowing $X$ completely determines $|Y|$. Thus $X$ and $Y$ are strongly dependent!</span></p>

<p><span class="part">Part (c): Failure of Linear Combination Normality</span><br>
Consider the sum $Z = X + Y = X + SX = X(1 + S)$:
- With probability $1/2$, $S = -1 \\implies Z = X(1 - 1) = 0$.<br>
- With probability $1/2$, $S = +1 \\implies Z = X(1 + 1) = 2X \\sim \\mathcal{N}(0, 4)$.<br>
Thus $Z$ has a discrete point mass at the origin:
$$\\mathbb{P}(Z = 0) = \\mathbb{P}(S = -1) = \\frac{1}{2}$$
A true continuous Gaussian random variable has zero probability of taking any single point value ($\\mathbb{P}(W = 0) = 0$).<br>
<span class=\"ans\">Because $X + Y$ contains an atom of probability $1/2$ at zero, it is not Gaussian. Hence $(X, Y)$ is NOT jointly Gaussian.</span></p>""",
        "takeaway": "\"Uncorrelated implies independent\" holds ONLY for jointly Gaussian vectors. Two random variables can each be individually standard normal with correlation $\\rho = 0$, yet be completely dependent ($Y = \\pm X$). Joint normality requires all linear combinations $aX+bY$ to be Gaussian."
    },
    {
        "id": 31393,
        "subject": "StoMA",
        "topicId": "13_Jointly_Gaussian_Random_Variables",
        "topicTitle": "13 · Jointly Gaussian Random Variables",
        "title": "Mahalanobis Distance & Chi-Square Distribution (Generated Exam)",
        "kind2": "practice",
        "source": "MIT 6.041 / Berkeley Benchmark",
        "marks": "[10 Marks]",
        "question": """<p>Let $\\mathbf{X} \\sim \\mathcal{N}(\\boldsymbol{\\mu}, \\Sigma)$ be a non-singular Gaussian random vector in $\\mathbb{R}^n$ with $\\Sigma \\succ 0$.</p>
<p><span class="part">(a)</span> Define the squared <strong>Mahalanobis distance</strong> $D^2 = (\\mathbf{X} - \\boldsymbol{\\mu})^\\top \\Sigma^{-1} (\\mathbf{X} - \\boldsymbol{\\mu})$.</p>
<p><span class="part">(b)</span> Using the symmetric matrix square root whitening transform $\\mathbf{Z} = \\Sigma^{-1/2}(\\mathbf{X} - \\boldsymbol{\\mu})$, prove that $D^2$ follows a Chi-Square distribution with $n$ degrees of freedom:
$$D^2 \\sim \\chi_n^2$$</p>
<p><span class="part">(c)</span> Explain how this property is used to construct exact ellipsoidal confidence regions for multivariate anomaly detection.</p>""",
        "solution": """<p><span class="part">Part (a): Mahalanobis Distance Definition</span><br>
The squared Mahalanobis distance measures the statistical distance of a point $\\mathbf{X}$ from the centroid $\\boldsymbol{\\mu}$, weighted inversely by the covariance structure:
$$D^2 = (\\mathbf{X} - \\boldsymbol{\\mu})^\\top \\Sigma^{-1} (\\mathbf{X} - \\boldsymbol{\\mu})$$
Points of constant Mahalanobis distance form concentric hyper-ellipsoids corresponding to level curves of the multivariate normal density.</p>

<p><span class="part">Part (b): Whitening Transform and Chi-Square Proof</span><br>
Since $\\Sigma \\succ 0$ is symmetric positive definite, by the Spectral Theorem $\\Sigma = Q \\Lambda Q^\\top$ where $Q$ is orthogonal and $\\Lambda = \\operatorname{diag}(\\lambda_1, \\dots, \\lambda_n)$ with $\\lambda_i > 0$.<br>
Define the symmetric inverse square root matrix:
$$\\Sigma^{-1/2} = Q \\Lambda^{-1/2} Q^\\top \\implies \\Sigma^{-1/2} \\Sigma \\Sigma^{-1/2} = I_n$$
Define the whitened vector $\\mathbf{Z} = \\Sigma^{-1/2}(\\mathbf{X} - \\boldsymbol{\\mu})$.<br>
Since affine transformations of Gaussian vectors are Gaussian:
- Mean: $\\mathbb{E}[\\mathbf{Z}] = \\Sigma^{-1/2}(\\mathbb{E}[\\mathbf{X}] - \\boldsymbol{\\mu}) = \\mathbf{0}$.<br>
- Covariance:
$$\\operatorname{Cov}(\\mathbf{Z}) = \\Sigma^{-1/2} \\operatorname{Cov}(\\mathbf{X}) \\Sigma^{-1/2} = \\Sigma^{-1/2} \\Sigma \\Sigma^{-1/2} = I_n$$
Thus $\\mathbf{Z} \\sim \\mathcal{N}(\\mathbf{0}, I_n)$, meaning the components $Z_1, Z_2, \\dots, Z_n$ are independent standard normal random variables.<br>
Now express $D^2$ in terms of $\\mathbf{Z}$:
$$D^2 = (\\mathbf{X} - \\boldsymbol{\\mu})^\\top \\Sigma^{-1} (\\mathbf{X} - \\boldsymbol{\\mu}) = (\\Sigma^{-1/2}(\\mathbf{X} - \\boldsymbol{\\mu}))^\\top (\\Sigma^{-1/2}(\\mathbf{X} - \\boldsymbol{\\mu})) = \\mathbf{Z}^\\top \\mathbf{Z} = \\sum_{i=1}^n Z_i^2$$
By definition, the sum of squares of $n$ independent standard normal random variables is a Chi-Square random variable with $n$ degrees of freedom.<br>
<span class=\"ans\">Thus $D^2 = (\\mathbf{X} - \\boldsymbol{\\mu})^\\top \\Sigma^{-1} (\\mathbf{X} - \\boldsymbol{\\mu}) \\sim \\chi_n^2$.</span> $\\blacksquare$</p>

<p><span class="part">Part (c): Application to Anomaly Detection</span><br>
In hypothesis testing and outlier detection, the ellipsoid:
$$\\mathcal{E}_{1-\\alpha} = \\left\\{ x \\in \\mathbb{R}^n : (x - \\boldsymbol{\\mu})^\\top \\Sigma^{-1} (x - \\boldsymbol{\\mu}) \\le \\chi_{n, 1-\\alpha}^2 \\right\\}$$
contains exactly $(1 - \\alpha)$ of the total probability mass (e.g., $95\\%$ or $99\\%$).<br>
- A new observation $x_{\\text{new}}$ is classified as an <strong>anomaly (outlier)</strong> if its Mahalanobis distance exceeds the critical threshold:
$$D^2(x_{\\text{new}}) > \\chi_{n, 1-\\alpha}^2$$
Unlike Euclidean distance, Mahalanobis distance accounts for varying variances along different dimensions and corrects for correlations between features.</p>""",
        "takeaway": "The whitening transform $\\mathbf{Z} = \\Sigma^{-1/2}(\\mathbf{X}-\\boldsymbol{\\mu})$ standardizes arbitrary Gaussian vectors into $\\mathcal{N}(\\mathbf{0}, I_n)$. The squared Mahalanobis distance is the sum of squared standard normals: $D^2 \\sim \\chi_n^2$, defining exact confidence ellipsoids."
    },

    # =========================================================================
    # TOPIC 14: Random Sums & Wald's Identity
    # =========================================================================
    {
        "id": 31491,
        "subject": "StoMA",
        "topicId": "14_Random_Sums_and_Walds_Equation",
        "topicTitle": "14 · Random Sums & Wald’s Identity",
        "title": "Wald's First and Second Equations for Random Sums (IISc Midterm 2)",
        "kind2": "pyq",
        "source": "IISc StoMA Midterm 2 2024 / Ross Ch 3",
        "marks": "[8 Marks]",
        "question": """<p>A fair 6-sided die is rolled. Let $N \\in \\{1, 2, \\dots, 6\\}$ denote the outcome. Then $N$ independent fair coins are tossed. Let $S = \\sum_{i=1}^N X_i$ be the total number of heads obtained (where $X_i \\sim \\text{Bernoulli}(1/2)$).</p>
<p><span class="part">(a)</span> State <strong>Wald's First Equation</strong> for random sums and calculate the expected number of heads $\\mathbb{E}[S]$.</p>
<p><span class="part">(b)</span> State <strong>Wald's Second Equation</strong> for the variance of random sums:
$$\\operatorname{Var}(S_N) = \\mathbb{E}[N]\\operatorname{Var}(X) + (\\mathbb{E}[X])^2 \\operatorname{Var}(N)$$
and calculate the exact numerical variance $\\operatorname{Var}(S)$.</p>""",
        "solution": """<p><span class="part">Part (a): Wald's First Equation & Mean Heads</span><br>
<strong>Wald's First Equation:</strong> If $N$ is independent of the i.i.d. increments $\\{X_i\\}$, the expected sum is the product of expectations:
$$\\mathbb{E}[S_N] = \\mathbb{E}[N] \\mathbb{E}[X]$$
1. <strong>Moments of Die Roll $N$:</strong>
$$\\mathbb{E}[N] = \\frac{1 + 2 + 3 + 4 + 5 + 6}{6} = \\frac{21}{6} = <span class=\"ans\">\\frac{7}{2} = 3.5</span>$$
2. <strong>Moments of Coin Toss $X_i$:</strong>
$$\\mathbb{E}[X] = p = <span class=\"ans\">\\frac{1}{2}</span>, \\qquad \\operatorname{Var}(X) = p(1 - p) = \\left(\\frac{1}{2}\\right)\\left(\\frac{1}{2}\\right) = \\frac{1}{4}$$
Applying Wald's First Equation:
$$\\mathbb{E}[S] = \\mathbb{E}[N] \\mathbb{E}[X] = \\left(\\frac{7}{2}\\right) \\left(\\frac{1}{2}\\right) = <span class=\"ans\">\\frac{7}{4} = 1.75</span>$$</p>

<p><span class="part">Part (b): Wald's Second Equation & Variance</span><br>
First compute the variance of the die roll $N$:
$$\\mathbb{E}[N^2] = \\frac{1^2 + 2^2 + 3^2 + 4^2 + 5^2 + 6^2}{6} = \\frac{1 + 4 + 9 + 16 + 25 + 36}{6} = \\frac{91}{6}$$
$$\\operatorname{Var}(N) = \\mathbb{E}[N^2] - (\\mathbb{E}[N])^2 = \\frac{91}{6} - \\left(\\frac{7}{2}\\right)^2 = \\frac{91}{6} - \\frac{49}{4} = \\frac{182 - 147}{12} = <span class=\"ans\">\\frac{35}{12}</span>$$
Applying Wald's Second Equation:
$$\\operatorname{Var}(S) = \\mathbb{E}[N]\\operatorname{Var}(X) + (\\mathbb{E}[X])^2 \\operatorname{Var}(N)$$
Substitute the computed values:
$$\\operatorname{Var}(S) = \\left(\\frac{7}{2}\\right)\\left(\\frac{1}{4}\\right) + \\left(\\frac{1}{2}\\right)^2 \\left(\\frac{35}{12}\\right) = \\frac{7}{8} + \\frac{1}{4}\\left(\\frac{35}{12}\\right) = \\frac{7}{8} + \\frac{35}{48}$$
Convert to a common denominator of 48:
$$\\operatorname{Var}(S) = \\frac{42}{48} + \\frac{35}{48} = <span class=\"ans\">\\frac{77}{48} \\approx 1.60417</span>$$
Notice that $\\frac{42}{48} = 0.875$ represents the uncertainty from the coin flips, and $\\frac{35}{48} \\approx 0.729$ represents the uncertainty from the die roll.</p>""",
        "takeaway": "Wald's identities compute moments of random sums directly without conditioning manually: $\\mathbb{E}[S_N] = \\mathbb{E}[N]\\mathbb{E}[X]$ and $\\operatorname{Var}(S_N) = \\mathbb{E}[N]\\operatorname{Var}(X) + (\\mathbb{E}[X])^2\\operatorname{Var}(N)$. Volatility comes from both the random count and the individual terms."
    },
    {
        "id": 31492,
        "subject": "StoMA",
        "topicId": "14_Random_Sums_and_Walds_Equation",
        "topicTitle": "14 · Random Sums & Wald’s Identity",
        "title": "Galton-Watson Branching Process & Extinction Probability (Stanford Stats 116)",
        "kind2": "pyq",
        "source": "Stanford Stats 116 / Ross Ch 3",
        "marks": "[10 Marks]",
        "question": """<p>In a Galton-Watson branching process starting with 1 ancestor ($Z_0 = 1$), each individual independently produces $\\xi$ offspring with distribution:
$$p_0 = \\mathbb{P}(\\xi = 0) = \\frac{1}{4}, \\qquad p_1 = \\mathbb{P}(\\xi = 1) = \\frac{1}{2}, \\qquad p_2 = \\mathbb{P}(\\xi = 2) = \\frac{1}{4}$$</p>
<p><span class="part">(a)</span> Compute the mean offspring number $\\mu = \\mathbb{E}[\\xi]$ and find the probability generating function (PGF) $G(s) = \\mathbb{E}[s^\\xi]$ for $s \\in [0, 1]$.</p>
<p><span class="part">(b)</span> Using the fixed-point equation $\\pi_0 = G(\\pi_0)$, determine the ultimate extinction probability $\\pi_0 = \\lim_{n \\to \\infty} \\mathbb{P}(Z_n = 0)$.</p>
<p><span class="part">(c)</span> Suppose the distribution is altered to $p_0 = 1/6, p_1 = 1/2, p_2 = 1/3$. Recompute the mean $\\mu$ and find the new extinction probability $\\pi_0$.</p>""",
        "solution": """<p><span class="part">Part (a): Offspring Mean and PGF</span><br>
The mean offspring number is:
$$\\mu = \\mathbb{E}[\\xi] = 0\\left(\\frac{1}{4}\\right) + 1\\left(\\frac{1}{2}\\right) + 2\\left(\\frac{1}{4}\\right) = 0 + \\frac{1}{2} + \\frac{1}{2} = <span class=\"ans\">1</span>$$
Since $\\mu = 1$, the process is <strong>critical</strong>.<br>
The Probability Generating Function is:
$$G(s) = \\sum_{k=0}^2 p_k s^k = \\frac{1}{4} + \\frac{1}{2}s + \\frac{1}{4}s^2 = \\frac{1}{4}(1 + 2s + s^2) = <span class=\"ans\">\\frac{(1 + s)^2}{4}</span>$$</p>

<p><span class="part">Part (b): Extinction Probability for Critical Process</span><br>
The ultimate extinction probability $\\pi_0$ is the <strong>smallest non-negative root</strong> of the fixed-point equation $s = G(s)$ in $[0, 1]$:
$$s = \\frac{(1 + s)^2}{4} \\implies 4s = 1 + 2s + s^2 \\implies s^2 - 2s + 1 = 0 \\implies (s - 1)^2 = 0$$
The unique root on $[0, 1]$ is:
$$<span class=\"ans\">\\pi_0 = 1</span>$$
<span class=\"ans\">Extinction is guaranteed with probability 1!</span> Even though the population replaces itself on average ($\\mu = 1$), random drift inevitably hits the absorbing zero barrier.</p>

<p><span class="part">Part (c): Supercritical Case</span><br>
For $p_0 = 1/6, p_1 = 1/2, p_2 = 1/3$:
$$\\mu = 0\\left(\\frac{1}{6}\\right) + 1\\left(\\frac{1}{2}\\right) + 2\\left(\\frac{1}{3}\\right) = \\frac{1}{2} + \\frac{2}{3} = <span class=\"ans\">\\frac{7}{6} > 1 \\quad (\\text{Supercritical})</span>$$
The new PGF is $G(s) = \\frac{1}{6} + \\frac{1}{2}s + \\frac{1}{3}s^2$. Solve $s = G(s)$:
$$s = \\frac{1}{6} + \\frac{1}{2}s + \\frac{1}{3}s^2 \\implies 6s = 1 + 3s + 2s^2 \\implies 2s^2 - 3s + 1 = 0$$
Factor the quadratic:
$$(2s - 1)(s - 1) = 0 \\implies s = \\frac{1}{2} \\quad \\text{or} \\quad s = 1$$
The smallest non-negative root on $[0, 1]$ is:
$$<span class=\"ans\">\\pi_0 = \\frac{1}{2} = 50\\%</span>$$
The lineage has a $50\\%$ chance of dying out, and a $50\\%$ chance of surviving forever ($Z_n \\to \\infty$).</p>""",
        "takeaway": "Branching process dichotomy: If $\\mu \\le 1$ (subcritical/critical), extinction is certain ($\\pi_0 = 1$). If $\\mu > 1$ (supercritical), the lineage has positive probability of immortality ($1 - \\pi_0 > 0$), where $\\pi_0$ is the unique root of $s = G(s)$ in $[0, 1)$."
    },
    {
        "id": 31493,
        "subject": "StoMA",
        "topicId": "14_Random_Sums_and_Walds_Equation",
        "topicTitle": "14 · Random Sums & Wald’s Identity",
        "title": "Stopping Times & Failure of Wald's Equation for Dependent Stopping (Generated Exam)",
        "kind2": "practice",
        "source": "Berkeley EECS 126 / MIT Benchmark",
        "marks": "[10 Marks]",
        "question": """<p><span class="part">(a)</span> Define what it means for an integer-valued random variable $N$ to be a <strong>stopping time</strong> with respect to a filtration $\\mathcal{F}_n = \\sigma(X_1, \\dots, X_n)$.</p>
<p><span class="part">(b)</span> State the exact hypotheses under which <strong>Wald's Equation</strong> $\\mathbb{E}[\\sum_{i=1}^N X_i] = \\mathbb{E}[N]\\mathbb{E}[X]$ holds.</p>
<p><span class="part">(c)</span> Construct an explicit counterexample where $N$ depends on future increments (not a stopping time), and show that $\\mathbb{E}[S_N] \\ne \\mathbb{E}[N]\\mathbb{E}[X]$.</p>""",
        "solution": """<p><span class="part">Part (a): Formal Definition of a Stopping Time</span><br>
Let $(\\Omega, \\mathcal{F}, \\mathbb{P})$ be a probability space with a filtration $\\{\\mathcal{F}_n\\}_{n=1}^\\infty$ where $\\mathcal{F}_n = \\sigma(X_1, \\dots, X_n)$.<br>
A random variable $N \\in \\{1, 2, \\dots\\} \\cup \\{\\infty\\}$ is a <strong>stopping time</strong> if for every finite $n \\ge 1$:
$$\\{ N = n \\} \\in \\mathcal{F}_n \\quad (\\text{or equivalently, } \\{ N \\le n \\} \\in \\mathcal{F}_n)$$
Intuitively, the decision to terminate the process at step $n$ must be determined solely by observations up to time $n$, with <strong>zero peeking into future outcomes</strong> $X_{n+1}, X_{n+2}, \\dots$.</p>

<p><span class="part">Part (b): Hypotheses of Wald's Equation</span><br>
Let $\\{X_i\\}_{i=1}^\\infty$ be independent and identically distributed random variables with finite expectation $\\mathbb{E}[|X|] < \\infty$.<br>
Let $N$ be an integer-valued random variable. Wald's Equation holds if either:
1. $N$ is independent of the sequence $\\{X_i\\}$, with $\\mathbb{E}[N] < \\infty$.<br>
2. $N$ is a <strong>stopping time</strong> with respect to $\\{\\mathcal{F}_n\\}$, with $\\mathbb{E}[N] < \\infty$.<br>
Under either hypothesis:
$$\\mathbb{E}\\left[ \\sum_{i=1}^N X_i \\right] = \\mathbb{E}[N] \\mathbb{E}[X]$$</p>

<p><span class="part">Part (c): Counterexample with Looking-Ahead</span><br>
Let $X_1, X_2$ be independent symmetric Rademacher variables:
$$\\mathbb{P}(X_i = +1) = \\frac{1}{2}, \\qquad \\mathbb{P}(X_i = -1) = \\frac{1}{2} \\implies \\mathbb{E}[X] = 0$$
Define the stopping index $N \\in \\{1, 2\\}$ by inspecting the second variable $X_2$ in advance:
$$N = \\begin{cases} 1 & \\text{if } X_2 = +1 \\\\ 2 & \\text{if } X_2 = -1 \\end{cases}$$
1. <strong>Verification of Non-Stopping Time:</strong><br>
$$\\{ N = 1 \\} = \\{ X_2 = +1 \\} \\notin \\mathcal{F}_1 = \\sigma(X_1)$$
To know whether to stop at time 1, one must peek ahead into the future variable $X_2$. Thus $N$ is NOT a stopping time.<br>
2. <strong>Expectation of $N$:</strong>
$$\\mathbb{E}[N] = 1 \\cdot \\mathbb{P}(X_2 = +1) + 2 \\cdot \\mathbb{P}(X_2 = -1) = 1(0.5) + 2(0.5) = 1.5$$
If Wald's equation applied, the expected sum would be $\\mathbb{E}[N]\\mathbb{E}[X] = (1.5)(0) = 0$.<br>
3. <strong>Actual Expectation of $S_N$:</strong>
- When $X_2 = +1$ (prob $1/2$): $N = 1$, so $S_N = X_1$. Since $X_1 \\perp X_2$, $\\mathbb{E}[S_N \\mid X_2 = +1] = \\mathbb{E}[X_1] = 0$.<br>
- When $X_2 = -1$ (prob $1/2$): $N = 2$, so $S_N = X_1 + X_2 = X_1 - 1$. Expectation is $\\mathbb{E}[X_1 - 1 \\mid X_2 = -1] = 0 - 1 = -1$.<br>
Averaging over both scenarios:
$$\\mathbb{E}[S_N] = \\frac{1}{2}(0) + \\frac{1}{2}(-1) = <span class=\"ans\">-\\frac{1}{2} \\ne 0 = \\mathbb{E}[N]\\mathbb{E}[X]</span>$$
<span class=\"ans\">Wald's equation completely fails!</span> By peeking ahead and stopping before negative shocks occur, the stopping policy introduces massive selection bias.</p>""",
        "takeaway": "Wald's equation $\\mathbb{E}[S_N] = \\mathbb{E}[N]\\mathbb{E}[X]$ fundamentally requires $N$ to be a stopping time (no looking ahead). Peeking into future outcomes creates selection bias that violates the martingale property, causing $\\mathbb{E}[S_N] \\ne \\mathbb{E}[N]\\mathbb{E}[X]$."
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
    for c in PRACTICE_STOMA_13_14:
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
