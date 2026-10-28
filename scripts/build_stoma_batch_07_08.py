#!/usr/bin/env python3
"""
build_stoma_batch_07_08.py
Generates 6 flippable practice cards for StoMA Topics 07 and 08:
  Topic 07: Joint Distributions, Marginal and Conditional Distributions (3 cards)
  Topic 08: Multiple Random Variables and Order Statistics (3 cards)
"""

import os
import re
import json

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PRACTICE_STOMA_07_08 = [
    # =========================================================================
    # TOPIC 07: Joint, Marginal & Conditional Distributions
    # =========================================================================
    {
        "id": 30791,
        "subject": "StoMA",
        "topicId": "07_Joint_Distributions_Marginal_and_Conditional_Distributions",
        "topicTitle": "07 · Joint, Marginal & Conditional Distributions",
        "title": "Bivariate Joint Density & Conditional Regression (IISc Test 1)",
        "kind2": "pyq",
        "source": "IISc StoMA Test 1 / Ross Ch 2",
        "marks": "[8 Marks]",
        "question": """<p>Let $(X, Y)$ have the joint probability density function:
$$f_{X,Y}(x, y) = c(x + y), \\quad 0 \\le x \\le 1, \\; 0 \\le y \\le 1$$</p>
<p><span class="part">(a)</span> Determine the normalization constant $c$.</p>
<p><span class="part">(b)</span> Compute the marginal density functions $f_X(x)$ and $f_Y(y)$. Are $X$ and $Y$ independent? Rigorously justify.</p>
<p><span class="part">(c)</span> Find the conditional density $f_{Y|X}(y \\mid x)$ and calculate the regression curve $\\mathbb{E}[Y \\mid X = x]$.</p>""",
        "solution": """<p><span class="part">Part (a): Normalization Constant $c$</span><br>
The joint PDF must integrate to 1 over the unit square $[0, 1] \\times [0, 1]$:
$$\\int_0^1 \\int_0^1 c(x + y) \\, dx \\, dy = c \\int_0^1 \\left[ \\frac{x^2}{2} + xy \\right]_0^1 dy = c \\int_0^1 \\left( \\frac{1}{2} + y \\right) dy = c \\left[ \\frac{y}{2} + \\frac{y^2}{2} \\right]_0^1 = c(1) = 1$$
$$<span class=\"ans\">c = 1</span>$$</p>

<p><span class="part">Part (b): Marginals and Independence Test</span><br>
For $x \\in [0, 1]$, integrate over $y$:
$$f_X(x) = \\int_0^1 (x + y) \\, dy = \\left[ xy + \\frac{y^2}{2} \\right]_0^1 = <span class=\"ans\">x + \\frac{1}{2}</span>$$
By algebraic symmetry between $x$ and $y$:
$$f_Y(y) = y + \\frac{1}{2}, \\quad y \\in [0, 1]$$
<strong>Independence Check:</strong> For $X$ and $Y$ to be independent, we must have $f_{X,Y}(x, y) = f_X(x)f_Y(y)$ for all $x, y \\in [0, 1]$.<br>
Multiplying the marginals:
$$f_X(x)f_Y(y) = \\left(x + \\frac{1}{2}\\right)\\left(y + \\frac{1}{2}\\right) = xy + \\frac{x}{2} + \\frac{y}{2} + \\frac{1}{4} \\ne x + y = f_{X,Y}(x, y)$$
<span class=\"ans\">Since $f_{X,Y}(x, y) \\ne f_X(x)f_Y(y)$, $X$ and $Y$ are NOT independent.</span></p>

<p><span class="part">Part (c): Conditional Density & Regression Function</span><br>
For any $x \\in [0, 1]$, the conditional density is:
$$f_{Y|X}(y \\mid x) = \\frac{f_{X,Y}(x, y)}{f_X(x)} = \\frac{x + y}{x + 1/2} = <span class=\"ans\">\\frac{2(x + y)}{2x + 1}, \\quad 0 \\le y \\le 1</span>$$
The regression curve $\\mathbb{E}[Y \\mid X = x]$ is:
$$\\mathbb{E}[Y \\mid X = x] = \\int_0^1 y f_{Y|X}(y \\mid x) \\, dy = \\frac{2}{2x + 1} \\int_0^1 (xy + y^2) \\, dy = \\frac{2}{2x + 1} \\left[ \\frac{xy^2}{2} + \\frac{y^3}{3} \\right]_0^1 = \\frac{2}{2x + 1} \\left( \\frac{x}{2} + \\frac{1}{3} \\right)$$
$$<span class=\"ans\">\\mathbb{E}[Y \\mid X = x] = \\frac{3x + 2}{6x + 3}</span>$$
Notice that for $x = 0$, $\\mathbb{E}[Y \\mid X = 0] = 2/3$, while for $x = 1$, $\\mathbb{E}[Y \\mid X = 1] = 5/9$. The conditional mean varies with $x$, confirming dependency.</p>""",
        "takeaway": "Factorization $f_{X,Y}(x,y) = f_X(x)f_Y(y)$ is the universal test for independence. An additive coupling $x + y$ produces correlated coordinates and a non-constant regression curve $\\mathbb{E}[Y \\mid X=x] = \\frac{3x+2}{6x+3}$."
    },
    {
        "id": 30792,
        "subject": "StoMA",
        "topicId": "07_Joint_Distributions_Marginal_and_Conditional_Distributions",
        "topicTitle": "07 · Joint, Marginal & Conditional Distributions",
        "title": "Uniform Distribution over a Simplex & Non-Rectangular Support (Stanford Stats 116)",
        "kind2": "pyq",
        "source": "Stanford Stats 116 / Ross 2.5",
        "marks": "[10 Marks]",
        "question": """<p>Let $(X, Y)$ be uniformly distributed over the triangular simplex:
$$\\Omega = \\{ (x, y) \\in \\mathbb{R}^2 : 0 \\le y \\le x \\le 1 \\}$$</p>
<p><span class="part">(a)</span> State the joint probability density function $f_{X,Y}(x, y)$.</p>
<p><span class="part">(b)</span> Derive the marginal densities $f_X(x)$ and $f_Y(y)$.</p>
<p><span class="part">(c)</span> Compute the conditional expectations $\\mathbb{E}[Y \\mid X = x]$ and $\\mathbb{E}[X \\mid Y = y]$.</p>
<p><span class="part">(d)</span> State why non-rectangular support immediately disproves independence without performing any integrations.</p>""",
        "solution": """<p><span class="part">Part (a): Joint Density</span><br>
The region $\\Omega$ is a right triangle with base 1 and height 1. Area:
$$\\text{Area}(\\Omega) = \\frac{1}{2} \\times 1 \\times 1 = \\frac{1}{2}$$
For a uniform distribution, the density is the reciprocal of the area:
$$f_{X,Y}(x, y) = \\begin{cases} <span class=\"ans\">2</span> & \\text{for } 0 \\le y \\le x \\le 1 \\\\ 0 & \\text{otherwise} \\end{cases}$$</p>

<p><span class="part">Part (b): Marginal Densities</span><br>
- For $X$: for a fixed $x \\in [0, 1]$, $y$ ranges from $0$ to $x$:
$$f_X(x) = \\int_0^x 2 \\, dy = <span class=\"ans\">2x, \\quad 0 \\le x \\le 1</span>$$
- For $Y$: for a fixed $y \\in [0, 1]$, $x$ ranges from $y$ to $1$:
$$f_Y(y) = \\int_y^1 2 \\, dx = <span class=\"ans\">2(1 - y), \\quad 0 \\le y \\le 1</span>$$</p>

<p><span class="part">Part (c): Conditional Expectations</span><br>
- Conditioned on $X = x$: $Y$ is uniformly distributed on $[0, x]$ with density $f_{Y|X}(y \\mid x) = \\frac{2}{2x} = \\frac{1}{x}$.<br>
$$<span class=\"ans\">\\mathbb{E}[Y \\mid X = x] = \\frac{x}{2}</span>$$
- Conditioned on $Y = y$: $X$ is uniformly distributed on $[y, 1]$ with density $f_{X|Y}(x \\mid y) = \\frac{2}{2(1-y)} = \\frac{1}{1-y}$.<br>
$$<span class=\"ans\">\\mathbb{E}[X \\mid Y = y] = \\frac{y + 1}{2}</span>$$</p>

<p><span class="part">Part (d): Geometric Criterion for Independence</span><br>
If two continuous random variables $X$ and $Y$ are independent, the support of their joint density MUST be a Cartesian product of sets:
$$\\operatorname{supp}(f_{X,Y}) = \\operatorname{supp}(f_X) \\times \\operatorname{supp}(f_Y)$$
For intervals, this requires the support to be an axis-aligned rectangle $[a, b] \\times [c, d]$.<br>
Here, $\\Omega = \\{0 \\le y \\le x \\le 1\\}$ is triangular: the range of $y$ depends explicitly on the value of $x$.<br>
<span class=\"ans\">Any joint distribution with non-rectangular support cannot be independent.</span></p>""",
        "takeaway": "Geometric test for independence: if the joint support boundary is sloped, curved, or triangular, $X$ and $Y$ can NEVER be independent. Conditioned on $X=x$, $Y \\sim \\text{Uniform}(0, x)$, which directly shrinks with $x$."
    },
    {
        "id": 30793,
        "subject": "StoMA",
        "topicId": "07_Joint_Distributions_Marginal_and_Conditional_Distributions",
        "topicTitle": "07 · Joint, Marginal & Conditional Distributions",
        "title": "Competing Exponentials & Independence of Minimum and Winner (Generated Exam)",
        "kind2": "practice",
        "source": "MIT 6.041 / Berkeley Benchmark",
        "marks": "[10 Marks]",
        "question": """<p>Let $X_1 \\sim \\text{Exp}(\\lambda_1)$ and $X_2 \\sim \\text{Exp}(\\lambda_2)$ be independent exponential random variables.</p>
<p><span class="part">(a)</span> Compute the exact probability $\\mathbb{P}(X_1 < X_2)$ that $X_1$ occurs before $X_2$ (the \"race probability\").</p>
<p><span class="part">(b)</span> Find the distribution of the minimum $Z = \\min(X_1, X_2)$ and identify its rate parameter.</p>
<p><span class="part">(c)</span> Prove that the identity of the winning component $I = \\mathbf{1}_{\\{X_1 < X_2\\}}$ and the first arrival time $Z = \\min(X_1, X_2)$ are <strong>completely independent random variables</strong>.</p>""",
        "solution": """<p><span class="part">Part (a): Race Probability $\\mathbb{P}(X_1 < X_2)$</span><br>
The joint density is $f_{X_1, X_2}(x_1, x_2) = \\lambda_1 e^{-\\lambda_1 x_1} \\lambda_2 e^{-\\lambda_2 x_2}$ for $x_1, x_2 > 0$.<br>
Integrate over the region $x_2 > x_1 > 0$:
$$\\mathbb{P}(X_1 < X_2) = \\int_0^\\infty \\lambda_1 e^{-\\lambda_1 x_1} \\left( \\int_{x_1}^\\infty \\lambda_2 e^{-\\lambda_2 x_2} \\, dx_2 \\right) dx_1 = \\int_0^\\infty \\lambda_1 e^{-\\lambda_1 x_1} e^{-\\lambda_2 x_1} \\, dx_1$$
$$\\mathbb{P}(X_1 < X_2) = \\lambda_1 \\int_0^\\infty e^{-(\\lambda_1 + \\lambda_2)x_1} \\, dx_1 = <span class=\"ans\">\\frac{\\lambda_1}{\\lambda_1 + \\lambda_2}</span>$$</p>

<p><span class="part">Part (b): Distribution of the Minimum $Z = \\min(X_1, X_2)$</span><br>
Using the survival function:
$$\\mathbb{P}(Z > t) = \\mathbb{P}(X_1 > t, X_2 > t) = \\mathbb{P}(X_1 > t)\\mathbb{P}(X_2 > t) = e^{-\\lambda_1 t} e^{-\\lambda_2 t} = e^{-(\\lambda_1 + \\lambda_2)t}$$
Hence:
$$F_Z(t) = 1 - e^{-(\\lambda_1 + \\lambda_2)t}, \\quad t \\ge 0$$
<span class=\"ans\">$Z \\sim \\text{Exp}(\\lambda_1 + \\lambda_2)$ with rate parameter $\\lambda = \\lambda_1 + \\lambda_2$.</span></p>

<p><span class="part">Part (c): Independence of $I = \\mathbf{1}_{\\{X_1 < X_2\\}}$ and $Z$</span><br>
We must show that $\\mathbb{P}(Z > t, X_1 < X_2) = \\mathbb{P}(Z > t) \\mathbb{P}(X_1 < X_2)$ for all $t \\ge 0$.<br>
The event $\\{Z > t, X_1 < X_2\\}$ means $t < X_1 < X_2$. Compute:
$$\\begin{aligned}
\\mathbb{P}(t < X_1 < X_2) &= \\int_t^\\infty \\lambda_1 e^{-\\lambda_1 x_1} \\left( \\int_{x_1}^\\infty \\lambda_2 e^{-\\lambda_2 x_2} \\, dx_2 \\right) dx_1 \\\\
&= \\int_t^\\infty \\lambda_1 e^{-\\lambda_1 x_1} e^{-\\lambda_2 x_1} \\, dx_1 = \\lambda_1 \\int_t^\\infty e^{-(\\lambda_1 + \\lambda_2)x_1} \\, dx_1 \\\\
&= \\lambda_1 \\left[ -\\frac{e^{-(\\lambda_1 + \\lambda_2)x_1}}{\\lambda_1 + \\lambda_2} \\right]_t^\\infty = \\frac{\\lambda_1}{\\lambda_1 + \\lambda_2} e^{-(\\lambda_1 + \\lambda_2)t}
\\end{aligned}$$
Comparing this product:
$$\\mathbb{P}(X_1 < X_2) \\cdot \\mathbb{P}(Z > t) = \\left( \\frac{\\lambda_1}{\\lambda_1 + \\lambda_2} \\right) \\cdot e^{-(\\lambda_1 + \\lambda_2)t} = \\mathbb{P}(Z > t, X_1 < X_2)$$
<span class=\"ans\">Because the joint probability factors identically into the product of marginals for all $t \\ge 0$, the winner $I$ and the time of victory $Z$ are completely independent!</span></p>""",
        "takeaway": "Exponential race theorem: $\\mathbb{P}(X_1 < X_2) = \\frac{\\lambda_1}{\\lambda_1 + \\lambda_2}$ and $\\min(X_1, X_2) \\sim \\text{Exp}(\\lambda_1 + \\lambda_2)$. Crucially, WHO wins the race and WHEN the race finishes are statistically independent random variables."
    },

    # =========================================================================
    # TOPIC 08: Multiple RVs & Order Statistics
    # =========================================================================
    {
        "id": 30891,
        "subject": "StoMA",
        "topicId": "08_Multiple_Random_Variables_and_Order_Statistics",
        "topicTitle": "08 · Multiple RVs & Order Statistics",
        "title": "Uniform Order Statistics & Beta Distribution (IISc Midterm 1)",
        "kind2": "pyq",
        "source": "IISc StoMA Midterm 1 2024 / Ross Ch 2",
        "marks": "[8 Marks]",
        "question": """<p>Let $U_1, U_2, \\dots, U_n$ be independent and identically distributed $\\text{Uniform}(0, 1)$ random variables. Let $U_{(1)} \\le U_{(2)} \\le \\dots \\le U_{(n)}$ denote their order statistics.</p>
<p><span class="part">(a)</span> Using combinatorial multinomial reasoning, derive the probability density function $f_{U_{(k)}}(u)$ of the $k$-th order statistic $U_{(k)}$ for $u \\in [0, 1]$.</p>
<p><span class="part">(b)</span> Identify the distribution of $U_{(k)}$ as a Beta distribution and state its parameters.</p>
<p><span class="part">(c)</span> Compute the expectation $\\mathbb{E}[U_{(k)}]$ and variance $\\operatorname{Var}(U_{(k)})$.</p>""",
        "solution": """<p><span class="part">Part (a): Derivation of Order Statistic PDF</span><br>
Consider an infinitesimal interval $[u, u + du] \\subset [0, 1]$.<br>
For the $k$-th smallest variable $U_{(k)}$ to lie in $[u, u + du]$, the $n$ independent observations must be partitioned into three distinct intervals:
1. Exactly $k - 1$ variables must fall in $[0, u)$ (each with probability $F(u) = u$).<br>
2. Exactly 1 variable must fall in $[u, u + du]$ (with probability $f(u)du = du$).<br>
3. The remaining $n - k$ variables must fall in $(u + du, 1]$ (each with probability $1 - F(u) = 1 - u$).<br>
The number of distinct ways to assign $n$ labeled variables to these three groups is given by the multinomial coefficient:
$$\\frac{n!}{(k - 1)! \\, 1! \\, (n - k)!}$$
Multiplying the probabilities:
$$f_{U_{(k)}}(u) \\, du = \\frac{n!}{(k - 1)!(n - k)!} u^{k - 1} (1 - u)^{n - k} \\, du$$
$$<span class=\"ans\">f_{U_{(k)}}(u) = \\frac{n!}{(k - 1)!(n - k)!} u^{k - 1} (1 - u)^{n - k}, \\quad 0 \\le u \\le 1</span>$$</p>

<p><span class="part">Part (b): Identification as Beta Distribution</span><br>
Recall the $\\text{Beta}(\\alpha, \\beta)$ probability density function:
$$f(u) = \\frac{1}{\\text{B}(\\alpha, \\beta)} u^{\\alpha - 1} (1 - u)^{\\beta - 1} = \\frac{\\Gamma(\\alpha + \\beta)}{\\Gamma(\\alpha)\\Gamma(\\beta)} u^{\\alpha - 1} (1 - u)^{\\beta - 1}$$
Matching exponents:
$$\\alpha - 1 = k - 1 \\implies \\alpha = k$$
$$\\beta - 1 = n - k \\implies \\beta = n - k + 1$$
Since $\\Gamma(n + 1) = n!$, the normalizer matches $\\frac{n!}{(k-1)!(n-k)!}$ exactly.<br>
<span class=\"ans\">Thus $U_{(k)} \\sim \\text{Beta}(\\alpha = k, \\beta = n - k + 1)$.</span></p>

<p><span class="part">Part (c): Expectation and Variance</span><br>
For a $\\text{Beta}(\\alpha, \\beta)$ distribution:
- <strong>Expectation:</strong>
$$\\mathbb{E}[U_{(k)}] = \\frac{\\alpha}{\\alpha + \\beta} = \\frac{k}{k + (n - k + 1)} = <span class=\"ans\">\\frac{k}{n + 1}</span>$$
- <strong>Variance:</strong>
$$\\operatorname{Var}(U_{(k)}) = \\frac{\\alpha \\beta}{(\\alpha + \\beta)^2 (\\alpha + \\beta + 1)} = \\frac{k(n - k + 1)}{(n + 1)^2 (n + 2)} = <span class=\"ans\">\\frac{k(n - k + 1)}{(n + 1)^2 (n + 2)}</span>$$
In particular, the order statistics divide the interval $[0, 1]$ into $n+1$ equal expected intervals of width $\\frac{1}{n+1}$.</p>""",
        "takeaway": "The $k$-th uniform order statistic follows $U_{(k)} \\sim \\text{Beta}(k, n - k + 1)$. The $n$ order statistics divide the unit interval into $n+1$ statistically identical sub-intervals with expected spacing $\\frac{1}{n+1}$."
    },
    {
        "id": 30892,
        "subject": "StoMA",
        "topicId": "08_Multiple_Random_Variables_and_Order_Statistics",
        "topicTitle": "08 · Multiple RVs & Order Statistics",
        "title": "Exponential Order Statistics & Memoryless Spacings (Stanford Stats 116)",
        "kind2": "pyq",
        "source": "Stanford Stats 116 / Ross 2.7",
        "marks": "[10 Marks]",
        "question": """<p>Let $X_1, \\dots, X_n$ be independent and identically distributed $\\text{Exp}(\\lambda)$ random variables, with order statistics $X_{(1)} \\le X_{(2)} \\le \\dots \\le X_{(n)}$.</p>
<p><span class="part">(a)</span> Derive the distribution and expected value of the sample minimum $X_{(1)}$.</p>
<p><span class="part">(b)</span> Define the successive spacings $D_k = X_{(k)} - X_{(k-1)}$ (where $X_{(0)} = 0$). By invoking the memoryless property of the Exponential distribution, prove that $D_1, D_2, \\dots, D_n$ are <strong>mutually independent</strong> and determine the distribution of $D_k$.</p>
<p><span class="part">(c)</span> Use this spacing representation to compute the expectation $\\mathbb{E}[X_{(n)}]$ of the sample maximum.</p>""",
        "solution": """<p><span class="part">Part (a): Distribution of the Minimum $X_{(1)}$</span><br>
The minimum exceeds $t$ if and only if all $n$ independent components survive past $t$:
$$\\mathbb{P}(X_{(1)} > t) = \\prod_{i=1}^n \\mathbb{P}(X_i > t) = [e^{-\\lambda t}]^n = e^{-n\\lambda t}, \\quad t \\ge 0$$
$$<span class=\"ans\">X_{(1)} \\sim \\text{Exp}(n\\lambda) \\implies \\mathbb{E}[X_{(1)}] = \\frac{1}{n\\lambda}</span>$$</p>

<p><span class="part">Part (b): Rényi's Representation via Memoryless Spacings</span><br>
At time $X_{(k-1)}$, exactly $k-1$ components have failed, leaving $n - (k - 1) = n - k + 1$ components operating.<br>
By the <strong>memoryless property</strong>, the remaining lifetime of each of these active components from time $X_{(k-1)}$ onwards is still exponentially distributed with rate $\\lambda$, completely fresh and independent of the past.<br>
The additional time $D_k = X_{(k)} - X_{(k-1)}$ until the next failure is simply the minimum lifetime among the $n - k + 1$ remaining components.<br>
By Part (a), the minimum of $m$ i.i.d. $\\text{Exp}(\\lambda)$ variables is $\\text{Exp}(m\\lambda)$. Setting $m = n - k + 1$:
$$<span class=\"ans\">D_k \\sim \\text{Exp}((n - k + 1)\\lambda), \\quad k = 1, 2, \\dots, n</span>$$
Moreover, because the remaining lifetimes are independent of the past history, the increments $D_1, D_2, \\dots, D_n$ are <strong>mutually independent</strong>.</p>

<p><span class="part">Part (c): Expectation of the Maximum $X_{(n)}$</span><br>
Express the maximum as the telescoping sum of all spacings:
$$X_{(n)} = \\sum_{k=1}^n (X_{(k)} - X_{(k-1)}) = \\sum_{k=1}^n D_k$$
Taking expectations by linearity:
$$\\mathbb{E}[X_{(n)}] = \\sum_{k=1}^n \\mathbb{E}[D_k] = \\sum_{k=1}^n \\frac{1}{(n - k + 1)\\lambda}$$
Substitute index $j = n - k + 1$, which runs from $1$ to $n$:
$$\\mathbb{E}[X_{(n)}] = \\frac{1}{\\lambda} \\sum_{j=1}^n \\frac{1}{j} = <span class=\"ans\">\\frac{H_n}{\\lambda} \\approx \\frac{\\ln n + \\gamma}{\\lambda}</span>$$
The expected maximum grows logarithmically with sample size $n$.</p>""",
        "takeaway": "Rényi's spacing theorem: Exponential order statistics decompose into independent exponential spacings $D_k \\sim \\text{Exp}((n - k + 1)\\lambda)$. The expected maximum is $\\mathbb{E}[X_{(n)}] = \\frac{H_n}{\\lambda} \\sim \\frac{\\ln n}{\\lambda}$."
    },
    {
        "id": 30893,
        "subject": "StoMA",
        "topicId": "08_Multiple_Random_Variables_and_Order_Statistics",
        "topicTitle": "08 · Multiple RVs & Order Statistics",
        "title": "Joint Density of Extrema (Min & Max) & Sample Range (Generated Exam)",
        "kind2": "practice",
        "source": "MIT 6.041 / Berkeley Benchmark",
        "marks": "[10 Marks]",
        "question": """<p>Let $X_1, \\dots, X_n$ be independent continuous random variables with CDF $F(x)$ and PDF $f(x)$. Let $U = X_{(1)}$ be the sample minimum and $V = X_{(n)}$ be the sample maximum.</p>
<p><span class="part">(a)</span> Derive the joint probability density function $f_{U,V}(u, v)$ for $u < v$.</p>
<p><span class="part">(b)</span> For the special case where $X_i \\sim \\text{Uniform}(0, 1)$, derive the probability density function $f_R(r)$ and expected value $\\mathbb{E}[R]$ of the <strong>sample range</strong> $R = V - U = X_{(n)} - X_{(1)}$.</p>""",
        "solution": """<p><span class="part">Part (a): Joint Density of $(X_{(1)}, X_{(n)})$</span><br>
Consider infinitesimal intervals $[u, u + du]$ and $[v, v + dv]$ with $u < v$.<br>
For $X_{(1)} \\in [u, u + du]$ and $X_{(n)} \\in [v, v + dv]$:
1. Exactly one variable must lie in $[u, u + du]$ (probability $f(u)du$).<br>
2. Exactly one variable must lie in $[v, v + dv]$ (probability $f(v)dv$).<br>
3. The remaining $n - 2$ variables must all fall strictly in between, in $(u, v)$ (each with probability $F(v) - F(u)$).<br>
The number of ways to choose which variable is the minimum and which is the maximum is $n(n - 1)$.<br>
Therefore:
$$f_{U,V}(u, v) \\, du \\, dv = n(n - 1) [F(v) - F(u)]^{n - 2} f(u) f(v) \\, du \\, dv$$
$$<span class=\"ans\">f_{U,V}(u, v) = n(n - 1) [F(v) - F(u)]^{n - 2} f(u) f(v), \\quad u < v</span>$$</p>

<p><span class="part">Part (b): Sample Range for Uniform Variables</span><br>
For $X_i \\sim \\text{Uniform}(0, 1)$, $F(x) = x$ and $f(x) = 1$ on $[0, 1]$.<br>
$$f_{U,V}(u, v) = n(n - 1)(v - u)^{n - 2}, \\quad 0 \\le u < v \\le 1$$
Transform variables: $R = V - U$ and $U = U$. The Jacobian determinant is 1.<br>
For a fixed range $R = r \\in [0, 1]$, $u$ ranges from $0$ to $1 - r$ (since $v = u + r \\le 1$).<br>
Integrate out $u$:
$$f_R(r) = \\int_0^{1-r} n(n - 1) r^{n - 2} \\, du = n(n - 1) r^{n - 2} (1 - r), \\quad 0 \\le r \\le 1$$
$$<span class=\"ans\">f_R(r) = n(n - 1) r^{n - 2} (1 - r) \\equiv \\text{Beta}(\\alpha = n - 1, \\beta = 2)</span>$$
Compute the expected range $\\mathbb{E}[R]$:
$$\\mathbb{E}[R] = \\frac{\\alpha}{\\alpha + \\beta} = \\frac{n - 1}{(n - 1) + 2} = <span class=\"ans\">\\frac{n - 1}{n + 1}</span>$$
Alternatively, by linearity:
$$\\mathbb{E}[R] = \\mathbb{E}[X_{(n)}] - \\mathbb{E}[X_{(1)}] = \\frac{n}{n + 1} - \\frac{1}{n + 1} = \\frac{n - 1}{n + 1}$$
As $n \\to \\infty$, $\\mathbb{E}[R] = 1 - \\frac{2}{n+1} \\to 1$.</p>""",
        "takeaway": "The joint density of extrema sandwiches $n-2$ points between $u$ and $v$: $f(u,v) = n(n-1)[F(v)-F(u)]^{n-2}f(u)f(v)$. For uniform variables, the sample range $R = X_{(n)} - X_{(1)}$ is distributed as $\\text{Beta}(n-1, 2)$ with expected value $\\frac{n-1}{n+1}$."
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
    for c in PRACTICE_STOMA_07_08:
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
