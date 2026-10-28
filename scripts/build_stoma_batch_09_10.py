#!/usr/bin/env python3
"""
build_stoma_batch_09_10.py
Generates 6 flippable practice cards for StoMA Topics 09 and 10:
  Topic 09: Sums of Random Variables and Jacobian Transformations (3 cards)
  Topic 10: Exchangeable Random Variables (3 cards)
"""

import os
import re
import json

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PRACTICE_STOMA_09_10 = [
    # =========================================================================
    # TOPIC 09: Sums & Jacobian Transformations
    # =========================================================================
    {
        "id": 30991,
        "subject": "StoMA",
        "topicId": "09_Sums_of_Random_Variables_and_Jacobian_Transformations",
        "topicTitle": "09 · Sums & Jacobian Transformations",
        "title": "Uniform Sum Convolution & Triangular Distribution (IISc Test 1)",
        "kind2": "pyq",
        "source": "IISc StoMA Test 1 / Ross Ch 2",
        "marks": "[8 Marks]",
        "question": """<p>Let $X, Y \\sim \\text{Uniform}(0, 1)$ be independent random variables.</p>
<p><span class="part">(a)</span> Using the continuous convolution integral $f_Z(z) = \\int_{-\\infty}^\\infty f_X(x) f_Y(z - x) \\, dx$, derive the exact probability density function of the sum $Z = X + Y$.</p>
<p><span class="part">(b)</span> Identify the support of $Z$ and describe the geometric shape of $f_Z(z)$ (the Irwin-Hall distribution for $n=2$).</p>
<p><span class="part">(c)</span> Compute the interval probability $\\mathbb{P}(0.5 \\le Z \\le 1.5)$ directly from the PDF.</p>""",
        "solution": """<p><span class="part">Part (a): Convolution Integral Derivation</span><br>
The marginal densities are $f_X(x) = \\mathbf{1}_{[0, 1]}(x)$ and $f_Y(y) = \\mathbf{1}_{[0, 1]}(y)$.<br>
The convolution formula yields:
$$f_Z(z) = \\int_{-\\infty}^\\infty f_X(x) f_Y(z - x) \\, dx = \\int_{-\\infty}^\\infty \\mathbf{1}_{[0, 1]}(x) \\, \\mathbf{1}_{[0, 1]}(z - x) \\, dx$$
The integrand is 1 when both $0 \\le x \\le 1$ and $0 \\le z - x \\le 1 \\iff z - 1 \\le x \\le z$.<br>
Hence $x$ must lie in the intersection:
$$x \\in [0, 1] \\cap [z - 1, z]$$
We analyze the intersection based on the value of $z$:
1. If $z < 0$ or $z > 2$: the intersection is empty, so $f_Z(z) = 0$.<br>
2. If $0 \\le z \\le 1$: $[0, 1] \\cap [z - 1, z] = [0, z]$. Thus:
$$f_Z(z) = \\int_0^z 1 \\, dx = <span class=\"ans\">z</span>$$
3. If $1 < z \\le 2$: $[0, 1] \\cap [z - 1, z] = [z - 1, 1]$. Thus:
$$f_Z(z) = \\int_{z-1}^1 1 \\, dx = 1 - (z - 1) = <span class=\"ans\">2 - z</span>$$
Combining the piecewise segments:
$$<span class=\"ans\">f_Z(z) = \\begin{cases} z & 0 \\le z \\le 1 \\\\ 2 - z & 1 < z \\le 2 \\\\ 0 & \\text{otherwise} \\end{cases}</span>$$</p>

<p><span class="part">Part (b): Geometric Properties</span><br>
The support is $[0, 2]$. The density is an isosceles <strong>triangular distribution</strong> symmetric about $z = 1$, reaching its peak height $f_Z(1) = 1$. The sum of two flat uniform variables forms a continuous tent function (smoothing effect of convolution).</p>

<p><span class="part">Part (c): Interval Probability</span><br>
By symmetry about the mean $\\mu = 1$:
$$\\mathbb{P}(0.5 \\le Z \\le 1.5) = 1 - \\mathbb{P}(Z < 0.5) - \\mathbb{P}(Z > 1.5) = 1 - 2\\mathbb{P}(Z < 0.5)$$
Integrating on the first ramp $[0, 0.5]$:
$$\\mathbb{P}(Z < 0.5) = \\int_0^{0.5} z \\, dz = \\left[ \\frac{z^2}{2} \\right]_0^{0.5} = \\frac{0.25}{2} = \\frac{1}{8} = 0.125$$
Therefore:
$$\\mathbb{P}(0.5 \\le Z \\le 1.5) = 1 - 2\\left(\\frac{1}{8}\\right) = 1 - \\frac{1}{4} = <span class=\"ans\">\\frac{3}{4} = 0.75</span>$$</p>""",
        "takeaway": "Convolution of two independent uniform indicators $\\mathbf{1}_{[0,1]} * \\mathbf{1}_{[0,1]}$ creates a triangular density on $[0, 2]$ peaking at 1. The central limit theorem begins visibly regularizing distributions already at $n = 2$."
    },
    {
        "id": 30992,
        "subject": "StoMA",
        "topicId": "09_Sums_of_Random_Variables_and_Jacobian_Transformations",
        "topicTitle": "09 · Sums & Jacobian Transformations",
        "title": "Box-Muller Transform & 2D Polar Jacobian (Stanford Stats 116)",
        "kind2": "pyq",
        "source": "Stanford Stats 116 / Ross 2.8",
        "marks": "[10 Marks]",
        "question": """<p>Let $U_1, U_2 \\sim \\text{i.i.d. Uniform}(0, 1)$. Consider the Box-Muller transformation:
$$Z_1 = \\sqrt{-2\\ln U_1}\\cos(2\\pi U_2), \\qquad Z_2 = \\sqrt{-2\\ln U_1}\\sin(2\\pi U_2)$$</p>
<p><span class="part">(a)</span> Define polar coordinates $R = \\sqrt{Z_1^2 + Z_2^2} = \\sqrt{-2\\ln U_1}$ and $\\Theta = 2\\pi U_2$. Determine the joint density $f_{R, \\Theta}(r, \\theta)$.</p>
<p><span class="part">(b)</span> Compute the Jacobian of the transformation from $(R, \\Theta)$ to $(Z_1, Z_2)$ and derive the joint density $f_{Z_1, Z_2}(z_1, z_2)$.</p>
<p><span class="part">(c)</span> Prove that $Z_1$ and $Z_2$ are independent standard normal random variables $\\mathcal{N}(0, 1)$.</p>""",
        "solution": """<p><span class="part">Part (a): Joint Density in Polar Coordinates</span><br>
Since $U_1, U_2 \\sim \\text{i.i.d. Uniform}(0, 1)$, their joint density is $f_{U_1, U_2}(u_1, u_2) = 1$ on $(0, 1)^2$.<br>
- For $\\Theta = 2\\pi U_2$: this is a linear scaling, so $\\Theta \\sim \\text{Uniform}(0, 2\\pi)$ with density $f_\\Theta(\\theta) = \\frac{1}{2\\pi}$.<br>
- For $R = \\sqrt{-2\\ln U_1}$: compute the survival function of $R^2 = -2\\ln U_1$:
$$\\mathbb{P}(R^2 > t) = \\mathbb{P}(-2\\ln U_1 > t) = \\mathbb{P}\\left(U_1 < e^{-t/2}\\right) = e^{-t/2}, \\quad t \\ge 0$$
Thus $R^2 \\sim \\text{Exp}(1/2)$. By 1D transformation, $F_R(r) = 1 - e^{-r^2/2} \\implies f_R(r) = r e^{-r^2/2}$ for $r > 0$.<br>
Because $U_1$ and $U_2$ are independent, $R$ and $\\Theta$ are independent:
$$f_{R, \\Theta}(r, \\theta) = f_R(r) f_\\Theta(\\theta) = <span class=\"ans\">\\frac{1}{2\\pi} r e^{-r^2/2}, \\quad r > 0, \\; 0 \\le \\theta < 2\\pi</span>$$</p>

<p><span class="part">Part (b): 2D Cartesian Jacobian Transformation</span><br>
The mapping from polar $(r, \\theta)$ to Cartesian $(z_1, z_2)$ is:
$$z_1 = r\\cos\\theta, \\qquad z_2 = r\\sin\\theta$$
The Jacobian determinant is:
$$J = \\det \\begin{bmatrix} \\frac{\\partial z_1}{\\partial r} & \\frac{\\partial z_1}{\\partial \\theta} \\\\ \\frac{\\partial z_2}{\\partial r} & \\frac{\\partial z_2}{\\partial \\theta} \\end{bmatrix} = \\det \\begin{bmatrix} \\cos\\theta & -r\\sin\\theta \\\\ \\sin\\theta & r\\cos\\theta \\end{bmatrix} = r(\\cos^2\\theta + \\sin^2\\theta) = r$$
Applying the 2D transformation formula:
$$f_{Z_1, Z_2}(z_1, z_2) = \\frac{f_{R, \\Theta}(r, \\theta)}{|J|} = \\frac{\\frac{1}{2\\pi} r e^{-r^2/2}}{r} = <span class=\"ans\">\\frac{1}{2\\pi} e^{-(z_1^2 + z_2^2)/2}</span>$$
where we substituted $r^2 = z_1^2 + z_2^2$.</p>

<p><span class="part">Part (c): Independence and Marginal Normality</span><br>
Factorize the joint density into product form:
$$f_{Z_1, Z_2}(z_1, z_2) = \\left( \\frac{1}{\\sqrt{2\\pi}} e^{-z_1^2/2} \\right) \\left( \\frac{1}{\\sqrt{2\\pi}} e^{-z_2^2/2} \\right) = f_{Z_1}(z_1) f_{Z_2}(z_2)$$
<span class=\"ans\">Both marginals are standard normal densities $\\mathcal{N}(0, 1)$, and their joint PDF factorizes unconditionally. Thus $Z_1$ and $Z_2$ are independent standard normal random variables!</span></p>""",
        "takeaway": "The Box-Muller transform turns 2 uniforms into 2 independent Gaussians by exploiting rotational symmetry: the angle $\\Theta \\sim \\text{Uniform}(0, 2\\pi)$ and squared radius $R^2 \\sim \\text{Exp}(1/2)$ map through the polar Jacobian $r$ directly into standard normal coordinates."
    },
    {
        "id": 30993,
        "subject": "StoMA",
        "topicId": "09_Sums_of_Random_Variables_and_Jacobian_Transformations",
        "topicTitle": "09 · Sums & Jacobian Transformations",
        "title": "Ratio of Independent Gaussians is Cauchy (Generated Exam)",
        "kind2": "practice",
        "source": "MIT 6.041 / Berkeley Benchmark",
        "marks": "[10 Marks]",
        "question": """<p>Let $X, Y \\sim \\text{i.i.d. } \\mathcal{N}(0, 1)$ be independent standard normal random variables.</p>
<p><span class="part">(a)</span> State the general integral formula for the probability density function of a quotient $Z = Y / X$ of two continuous random variables.</p>
<p><span class="part">(b)</span> Derive the exact PDF $f_Z(z)$ and prove that $Z$ follows the standard Cauchy distribution $\\text{Cauchy}(0, 1)$.</p>
<p><span class="part">(c)</span> Provide a clean geometric interpretation using the rotational invariance of the standard bivariate Gaussian distribution.</p>""",
        "solution": """<p><span class="part">Part (a): General Ratio Density Formula</span><br>
Consider the transformation $Z = Y / X$ and $W = X$.<br>
Inverting: $X = W$ and $Y = WZ$. The Jacobian determinant is:
$$J = \\det \\begin{bmatrix} \\frac{\\partial x}{\\partial z} & \\frac{\\partial x}{\\partial w} \\\\ \\frac{\\partial y}{\\partial z} & \\frac{\\partial y}{\\partial w} \\end{bmatrix} = \\det \\begin{bmatrix} 0 & 1 \\\\ w & z \\end{bmatrix} = -w \\implies |J| = |w| = |x|$$
Integrating out the auxiliary variable $x$:
$$f_Z(z) = \\int_{-\\infty}^\\infty |x| f_{X,Y}(x, xz) \\, dx$$</p>

<p><span class="part">Part (b): Derivation for Independent Gaussians</span><br>
The joint density is $f_{X,Y}(x, y) = \\frac{1}{2\\pi} e^{-(x^2 + y^2)/2}$. Substitute $y = xz$:
$$f_{X,Y}(x, xz) = \\frac{1}{2\\pi} e^{-\\frac{x^2(1 + z^2)}{2}}$$
Evaluating the ratio integral:
$$f_Z(z) = \\int_{-\\infty}^\\infty |x| \\frac{1}{2\\pi} e^{-\\frac{x^2(1 + z^2)}{2}} \\, dx = 2 \\int_0^\\infty x \\frac{1}{2\\pi} e^{-\\frac{x^2(1 + z^2)}{2}} \\, dx$$
Substitute $u = x^2$ with $du = 2x \\, dx$:
$$f_Z(z) = \\frac{1}{2\\pi} \\int_0^\\infty e^{-\\frac{u(1 + z^2)}{2}} \\, du = \\frac{1}{2\\pi} \\left[ -\\frac{2}{1 + z^2} e^{-\\frac{u(1 + z^2)}{2}} \\right]_0^\\infty = \\frac{1}{2\\pi} \\left( \\frac{2}{1 + z^2} \\right)$$
$$<span class=\"ans\">f_Z(z) = \\frac{1}{\\pi(1 + z^2)}, \\quad z \\in \\mathbb{R}</span>$$
<span class=\"ans\">This is precisely the probability density function of the standard Cauchy distribution!</span></p>

<p><span class="part">Part (c): Geometric Intuition via Rotational Symmetry</span><br>
The joint density $f_{X,Y}(x, y) = \\frac{1}{2\\pi} e^{-(x^2 + y^2)/2}$ depends purely on the radial distance $r = \\sqrt{x^2 + y^2}$, making the distribution perfectly rotationally symmetric.<br>
Consequently, the angle $\\Theta = \\arctan(Y/X)$ is <strong>uniformly distributed</strong> over $[-\\pi/2, \\pi/2]$.<br>
The quotient is the slope of the random vector $(X, Y)$:
$$Z = \\frac{Y}{X} = \\tan(\\Theta)$$
When $\\Theta \\sim \\text{Uniform}(-\\pi/2, \\pi/2)$, the transformation $Z = \\tan(\\Theta)$ yields $F_Z(z) = \\mathbb{P}(\\tan \\Theta \\le z) = \\mathbb{P}(\\Theta \\le \\arctan z) = \\frac{\\arctan z - (-\\pi/2)}{\\pi} = \\frac{1}{\\pi}\\arctan z + \\frac{1}{2}$, whose derivative is $\\frac{1}{\\pi(1 + z^2)}$.</p>""",
        "takeaway": "The ratio of two independent standard Gaussians is Cauchy: $Y/X \\sim \\text{Cauchy}(0, 1)$. Because standard bivariate Gaussians are rotationally invariant, the ray angle is uniform, making its slope $\\tan(\\Theta)$ Cauchy."
    },

    # =========================================================================
    # TOPIC 10: Exchangeable Random Variables
    # =========================================================================
    {
        "id": 31091,
        "subject": "StoMA",
        "topicId": "10_Exchangeable_Random_Variables",
        "topicTitle": "10 · Exchangeable Random Variables",
        "title": "Pólya's Urn: Proof of Exchangeability (IISc Test 2)",
        "kind2": "pyq",
        "source": "IISc StoMA Test 2 2024 / Ross Ch 3",
        "marks": "[8 Marks]",
        "question": """<p>An urn initially contains $1$ red ball and $1$ black ball. At each step $i = 1, 2, \\dots$, a ball is drawn uniformly at random, its color recorded, and it is returned to the urn along with $1$ additional ball of the identical color. Let $X_i = 1$ if the $i$-th draw is red, and $X_i = 0$ if black.</p>
<p><span class="part">(a)</span> State the formal definition of <strong>exchangeability</strong> for a sequence of random variables $(X_1, X_2, \\dots, X_n)$.</p>
<p><span class="part">(b)</span> Let $x = (x_1, \\dots, x_n) \\in \\{0, 1\\}^n$ be any binary sequence with exactly $k = \\sum_{i=1}^n x_i$ ones (red balls). Prove that the joint probability is:
$$\\mathbb{P}(X_1 = x_1, \\dots, X_n = x_n) = \\frac{k!(n - k)!}{(n + 1)!} = \\frac{1}{n + 1} \\binom{n}{k}^{-1}$$</p>
<p><span class="part">(c)</span> Conclude that $(X_1, X_2, \\dots, X_n)$ is an exchangeable sequence.</p>""",
        "solution": """<p><span class="part">Part (a): Formal Definition of Exchangeability</span><br>
A finite sequence of random variables $(X_1, X_2, \\dots, X_n)$ is <strong>exchangeable</strong> if for every permutation $\\pi$ of $\\{1, 2, \\dots, n\\}$, the joint distribution is invariant:
$$(X_{\\pi(1)}, X_{\\pi(2)}, \\dots, X_{\\pi(n)}) \\stackrel{d}{=} (X_1, X_2, \\dots, X_n)$$
Equivalently, $\\mathbb{P}(X_{\\pi(1)} = x_1, \\dots, X_{\\pi(n)} = x_n) = \\mathbb{P}(X_1 = x_1, \\dots, X_n = x_n)$ for all $x_1, \\dots, x_n$.</p>

<p><span class="part">Part (b): Joint Probability Calculation</span><br>
At draw $i$, there are $2 + (i - 1) = i + 1$ balls in the urn.<br>
By the chain rule of probability:
$$\\mathbb{P}(X_1 = x_1, \\dots, X_n = x_n) = \\prod_{i=1}^n \\mathbb{P}(X_i = x_i \\mid X_1 = x_1, \\dots, X_{i-1} = x_{i-1})$$
The product of the denominators across all $n$ steps is:
$$\\prod_{i=1}^n (i + 1) = 2 \\times 3 \\times 4 \\times \\dots \\times (n + 1) = (n + 1)!$$
Now consider the numerators:
- Each time a red ball ($x_i = 1$) is drawn, the number of red balls in the urn increases by 1: from 1 to 2, ..., up to $k$. Thus the product of red numerators is $1 \\times 2 \\times \\dots \\times k = k!$.<br>
- Each time a black ball ($x_i = 0$) is drawn, the number of black balls increases: from 1 to 2, ..., up to $n - k$. The product of black numerators is $1 \\times 2 \\times \\dots \\times (n - k) = (n - k)!$.<br>
Because multiplication is commutative, the order in which the $k$ red and $n-k$ black balls appear has zero effect on the final product!
$$\\mathbb{P}(X_1 = x_1, \\dots, X_n = x_n) = \\frac{k!(n - k)!}{(n + 1)!} = \\frac{1}{n + 1} \\frac{1}{\\frac{n!}{k!(n-k)!}} = <span class=\"ans\">\\frac{1}{n + 1} \\binom{n}{k}^{-1}</span>$$</p>

<p><span class="part">Part (c): Deduction of Exchangeability</span><br>
The joint probability depends <strong>exclusively</strong> on the total number of red balls $k = \\sum_{i=1}^n x_i$, and not on their specific positions in the sequence.<br>
Since any permutation $\\pi$ preserves the sum $\\sum_{i=1}^n x_{\\pi(i)} = \\sum_{i=1}^n x_i = k$:
$$\\mathbb{P}(X_{\\pi(1)} = x_1, \\dots, X_{\\pi(n)} = x_n) = \\mathbb{P}(X_1 = x_1, \\dots, X_n = x_n)$$
<span class=\"ans\">Thus $(X_1, \\dots, X_n)$ is strictly exchangeable.</span></p>""",
        "takeaway": "Exchangeability means joint probabilities depend solely on summary counts, not temporal order. In Pólya's urn, positive reinforcement creates strong memory, yet every sequence with $k$ red balls is equally likely: $\\frac{1}{n+1}\\binom{n}{k}^{-1}$."
    },
    {
        "id": 31092,
        "subject": "StoMA",
        "topicId": "10_Exchangeable_Random_Variables",
        "topicTitle": "10 · Exchangeable Random Variables",
        "title": "Pólya's Urn: Uniform Marginals & Limiting Continuous Law (Stanford Stats 116)",
        "kind2": "pyq",
        "source": "Stanford Stats 116 / Ross Ch 3",
        "marks": "[10 Marks]",
        "question": """<p>Consider the Pólya urn process from the previous card. Let $S_n = \\sum_{i=1}^n X_i$ be the total number of red balls drawn in the first $n$ steps.</p>
<p><span class="part">(a)</span> Prove that $S_n$ is <strong>discrete uniformly distributed</strong> on $\\{0, 1, \\dots, n\\}$:
$$\\mathbb{P}(S_n = k) = \\frac{1}{n + 1} \\quad \\forall k \\in \\{0, 1, \\dots, n\\}$$</p>
<p><span class="part">(b)</span> Let $M_n = \\frac{S_n + 1}{n + 2}$ be the fraction of red balls in the urn after step $n$. Prove that as $n \\to \\infty$, $M_n$ converges in distribution to a continuous standard uniform variable:
$$M_n \\xrightarrow{d} \\text{Uniform}(0, 1)$$</p>
<p><span class="part">(c)</span> Explain why this proves that the limiting proportion of red balls is random and path-dependent.</p>""",
        "solution": """<p><span class="part">Part (a): Discrete Uniform Distribution of $S_n$</span><br>
The event $\\{S_n = k\\}$ is the union of all binary sequences of length $n$ containing exactly $k$ ones.<br>
There are exactly $\\binom{n}{k}$ such sequences, and each pair is mutually exclusive.<br>
By Part (b) of the previous problem, every individual sequence has probability $\\frac{1}{n + 1} \\binom{n}{k}^{-1}$.<br>
Summing over all $\\binom{n}{k}$ sequences:
$$\\mathbb{P}(S_n = k) = \\sum_{\\{x : \\sum x_i = k\\}} \\mathbb{P}(X = x) = \\binom{n}{k} \\left[ \\frac{1}{n + 1} \\binom{n}{k}^{-1} \\right] = <span class=\"ans\">\\frac{1}{n + 1}</span>$$
for every $k \\in \\{0, 1, \\dots, n\\}$.<br>
<span class=\"ans\">Thus $S_n \\sim \\text{DiscreteUniform}\\{0, 1, \\dots, n\\}$.</span> Drawing 0 red balls is just as likely as drawing $n/2$ or $n$ red balls!</p>

<p><span class="part">Part (b): Continuous Uniform Limiting Distribution</span><br>
The fraction of red balls in the urn after $n$ steps is $M_n = \\frac{S_n + 1}{n + 2}$.<br>
For any $u \\in (0, 1)$, compute the cumulative distribution function:
$$\\mathbb{P}(M_n \\le u) = \\mathbb{P}\\left( \\frac{S_n + 1}{n + 2} \\le u \\right) = \\mathbb{P}\\left( S_n \\le (n + 2)u - 1 \\right)$$
Since $S_n$ is uniform on $\\{0, 1, \\dots, n\\}$, for any integer $m \\in \\{0, \\dots, n\\}$, $\\mathbb{P}(S_n \\le m) = \\frac{m + 1}{n + 1}$.<br>
Setting $m = \\lfloor (n + 2)u - 1 \\rfloor$:
$$\\mathbb{P}(M_n \\le u) = \\frac{\\lfloor (n + 2)u - 1 \\rfloor + 1}{n + 1} = \\frac{\\lfloor (n + 2)u \\rfloor}{n + 1}$$
Taking the limit as $n \\to \\infty$:
$$\\lim_{n \\to \\infty} \\mathbb{P}(M_n \\le u) = \\lim_{n \\to \\infty} \\frac{(n + 2)u + O(1)}{n + 1} = <span class=\"ans\">u, \\quad \\forall u \\in (0, 1)</span>$$
<span class=\"ans\">Since the limiting CDF is $F(u) = u$, $M_n \\xrightarrow{d} \\text{Uniform}(0, 1)$.</span></p>

<p><span class="part">Part (c): Path Dependence and Lock-in</span><br>
Because $M_n$ is a bounded martingale ($\\mathbb{E}[M_{n+1} \\mid \\mathcal{F}_n] = M_n$), Doob's Martingale Convergence Theorem implies $M_n \\xrightarrow{a.s.} M_\\infty$.<br>
Unlike the Law of Large Numbers (where the sample mean converges to a deterministic constant), here the limit $M_\\infty$ is a <strong>non-degenerate continuous random variable</strong>: every run of the experiment freezes into a different ultimate proportion, chosen uniformly from $[0, 1]$!</p>""",
        "takeaway": "Pólya's urn maintains a completely flat distribution $\\mathbb{P}(S_n = k) = \\frac{1}{n+1}$ at every stage. As $n \\to \\infty$, the proportion of red balls converges almost surely to a random limit $M_\\infty \\sim \\text{Uniform}(0, 1)$, demonstrating path-dependent lock-in."
    },
    {
        "id": 31093,
        "subject": "StoMA",
        "topicId": "10_Exchangeable_Random_Variables",
        "topicTitle": "10 · Exchangeable Random Variables",
        "title": "De Finetti's Theorem & Non-Negative Correlation Limit (Generated Exam)",
        "kind2": "practice",
        "source": "Berkeley EECS 126 / MIT Benchmark",
        "marks": "[10 Marks]",
        "question": """<p><span class="part">(a)</span> Let $X_1, \\dots, X_N$ be a <strong>finite</strong> exchangeable sequence with variance $\\operatorname{Var}(X_i) = \\sigma^2 > 0$ and common pairwise correlation $\\rho = \\operatorname{Corr}(X_i, X_j)$ for $i \\ne j$. By considering the variance of their sum $\\operatorname{Var}(\\sum_{i=1}^N X_i) \\ge 0$, prove the fundamental lower bound:
$$\\rho \\ge -\\frac{1}{N - 1}$$
Give a concrete physical example achieving this minimum.</p>
<p><span class="part">(b)</span> State <strong>De Finetti's Representation Theorem</strong> for an <strong>infinitely exchangeable</strong> sequence $(X_1, X_2, \\dots)$.</p>
<p><span class="part">(c)</span> Use De Finetti's theorem to prove that an infinitely exchangeable sequence can <strong>never</strong> have negative correlation ($\\rho \\ge 0$).</p>""",
        "solution": """<p><span class="part">Part (a): Finite Correlation Lower Bound</span><br>
Let $S_N = \\sum_{i=1}^N X_i$. Compute the variance of $S_N$:
$$\\begin{aligned}
\\operatorname{Var}(S_N) &= \\sum_{i=1}^N \\operatorname{Var}(X_i) + \\sum_{i \\ne j} \\operatorname{Cov}(X_i, X_j) \\\\
&= N\\sigma^2 + N(N - 1)\\rho \\sigma^2 = N\\sigma^2 \\left[ 1 + (N - 1)\\rho \\right]
\\end{aligned}$$
Because the variance of any real random variable is non-negative:
$$\\operatorname{Var}(S_N) \\ge 0 \\implies N\\sigma^2 [1 + (N - 1)\\rho] \\ge 0$$
Since $N > 0$ and $\\sigma^2 > 0$:
$$1 + (N - 1)\\rho \\ge 0 \\implies <span class=\"ans\">\\rho \\ge -\\frac{1}{N - 1}</span>$$
<strong>Concrete Physical Example:</strong> Sampling without replacement from a box containing $N$ distinct tickets $1, 2, \\dots, N$. The sum $S_N = \\sum_{i=1}^N i = \\frac{N(N+1)}{2}$ is constant, so $\\operatorname{Var}(S_N) = 0$. This achieves the absolute minimum correlation $\\rho = -\\frac{1}{N - 1}$ with equality!</p>

<p><span class="part">Part (b): De Finetti's Representation Theorem</span><br>
An infinite sequence of random variables $(X_1, X_2, \\dots)$ is exchangeable if and only if there exists a random probability measure (or latent parameter) $\\Theta$ such that, conditioned on $\\Theta$, the random variables $X_1, X_2, \\dots$ are <strong>conditionally independent and identically distributed</strong>:
$$\\mathbb{P}(X_1 \\le x_1, \\dots, X_n \\le x_n \\mid \\Theta) = \\prod_{i=1}^n F_\\Theta(x_i)$$
Unconditionally, their joint distribution is a mixture of i.i.d. processes.</p>

<p><span class="part">Part (c): Non-Negativity of Infinite Exchangeable Correlation</span><br>
Applying the <strong>Law of Total Covariance</strong> to any pair $X_1, X_2$:
$$\\operatorname{Cov}(X_1, X_2) = \\mathbb{E}[\\operatorname{Cov}(X_1, X_2 \\mid \\Theta)] + \\operatorname{Cov}(\\mathbb{E}[X_1 \\mid \\Theta], \\mathbb{E}[X_2 \\mid \\Theta])$$
1. Under condition $\\Theta$, $X_1$ and $X_2$ are conditionally independent, so:
$$\\operatorname{Cov}(X_1, X_2 \\mid \\Theta) = 0$$
2. Let $\\mu(\\Theta) = \\mathbb{E}[X_1 \\mid \\Theta] = \\mathbb{E}[X_2 \\mid \\Theta]$ denote the conditional mean. Then:
$$\\operatorname{Cov}(\\mathbb{E}[X_1 \\mid \\Theta], \\mathbb{E}[X_2 \\mid \\Theta]) = \\operatorname{Cov}(\\mu(\\Theta), \\mu(\\Theta)) = \\operatorname{Var}(\\mu(\\Theta))$$
Combining both terms:
$$\\operatorname{Cov}(X_1, X_2) = 0 + \\operatorname{Var}(\\mu(\\Theta)) = \\operatorname{Var}(\\mathbb{E}[X_1 \\mid \\Theta]) \\ge 0$$
Dividing by $\\sigma^2$:
$$<span class=\"ans\">\\rho = \\frac{\\operatorname{Var}(\\mathbb{E}[X_1 \\mid \\Theta])}{\\operatorname{Var}(X_1)} \\ge 0</span>$$
<span class=\"ans\">An infinite exchangeable sequence can NEVER exhibit negative correlation: $\\rho \\ge 0$ unconditionally.</span></p>""",
        "takeaway": "Finite exchangeable sequences can be negatively correlated down to $-\\frac{1}{N-1}$ (sampling without replacement). Infinite exchangeable sequences, however, are conditionally i.i.d. mixtures by De Finetti's theorem, which strictly forces $\\operatorname{Cov}(X_1, X_2) = \\operatorname{Var}(\\mathbb{E}[X_1|\\Theta]) \\ge 0$."
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
    for c in PRACTICE_STOMA_09_10:
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
