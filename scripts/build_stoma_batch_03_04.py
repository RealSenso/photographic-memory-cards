#!/usr/bin/env python3
"""
build_stoma_batch_03_04.py
Generates 6 flippable practice cards for StoMA Topics 03 and 04:
  Topic 03: Discrete and Continuous Random Variables (3 cards)
  Topic 04: Transformations and Functions of a Random Variable (3 cards)
"""

import os
import re
import json

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PRACTICE_STOMA_03_04 = [
    # =========================================================================
    # TOPIC 03: Discrete & Continuous Random Variables
    # =========================================================================
    {
        "id": 30391,
        "subject": "StoMA",
        "topicId": "03_Discrete_and_Continuous_Random_Variables",
        "topicTitle": "03 · Discrete & Continuous RVs",
        "title": "Memoryless Property of the Exponential Distribution (IISc Test 1)",
        "kind2": "pyq",
        "source": "IISc StoMA Test 1 2024 / Ross Ch 2",
        "marks": "[8 Marks]",
        "question": """<p><span class="part">(a)</span> Let $X \\sim \\text{Exp}(\\lambda)$ with parameter $\\lambda > 0$. Prove that $X$ satisfies the <strong>memoryless property</strong>: for all $s, t \\ge 0$,
$$\\mathbb{P}(X > s + t \\mid X > s) = \\mathbb{P}(X > t)$$</p>
<p><span class="part">(b)</span> Prove that the Exponential distribution is the <strong>unique</strong> continuous probability distribution supported on $[0, \\infty)$ possessing this property.</p>""",
        "solution": """<p><span class="part">Part (a): Verification for Exponential</span><br>
The probability density function is $f_X(x) = \\lambda e^{-\\lambda x}$ for $x \\ge 0$.<br>
The survival function (tail probability) is:
$$G(t) = \\mathbb{P}(X > t) = \\int_t^\\infty \\lambda e^{-\\lambda u} \\, du = e^{-\\lambda t} \\quad \\text{for } t \\ge 0$$
Using the definition of conditional probability for the event $\\{X > s + t\\} \\cap \\{X > s\\} = \\{X > s + t\\}$:
$$\\mathbb{P}(X > s + t \\mid X > s) = \\frac{\\mathbb{P}(X > s + t)}{\\mathbb{P}(X > s)} = \\frac{e^{-\\lambda(s+t)}}{e^{-\\lambda s}} = e^{-\\lambda t} = <span class=\"ans\">\\mathbb{P}(X > t)</span>$$
<span class=\"ans\">Thus the Exponential distribution is memoryless.</span></p>

<p><span class="part">Part (b): Uniqueness Proof (Cauchy Functional Equation)</span><br>
Let $X$ be any continuous non-negative random variable with survival function $G(t) = \\mathbb{P}(X > t)$ satisfying:
$$\\frac{\\mathbb{P}(X > s + t)}{\\mathbb{P}(X > s)} = \\mathbb{P}(X > t) \\implies G(s + t) = G(s) G(t) \\quad \\forall s, t \\ge 0$$
Note that $G(0) = \\mathbb{P}(X > 0) = 1$ and $0 < G(t) \\le 1$ for all $t \\ge 0$.<br>
For any integer $m \\in \\mathbb{N}$, repeatedly applying the equation gives:
$$G(m) = [G(1)]^m$$
For any positive rational $t = m/n$ where $m, n \\in \\mathbb{N}$:
$$G(1) = G\\left(n \\cdot \\frac{1}{n}\\right) = \\left[G\\left(\\frac{1}{n}\\right)\\right]^n \\implies G\\left(\\frac{1}{n}\\right) = [G(1)]^{1/n}$$
$$G\\left(\\frac{m}{n}\\right) = \\left[G\\left(\\frac{1}{n}\\right)\\right]^m = [G(1)]^{m/n}$$
Thus for all rational $q > 0$:
$$G(q) = [G(1)]^q = e^{-(- \\ln G(1)) q}$$
Since $X$ is a continuous random variable, its CDF $F_X(t) = 1 - G(t)$ is continuous, so $G(t)$ is continuous.<br>
By continuity, extending from rationals to all real numbers $t \\ge 0$:
$$G(t) = e^{-\\lambda t} \\quad \\text{where } \\lambda = -\\ln G(1) > 0$$
Hence $F_X(t) = 1 - e^{-\\lambda t}$, which is uniquely the <span class=\"ans\">Exponential distribution</span>. $\\blacksquare$</p>""",
        "takeaway": "Memorylessness $\\mathbb{P}(X > s + t \\mid X > s) = \\mathbb{P}(X > t)$ means past survival conveys zero information about remaining lifetime. Exponential is the unique continuous distribution, and Geometric is the unique discrete distribution, with this property."
    },
    {
        "id": 30392,
        "subject": "StoMA",
        "topicId": "03_Discrete_and_Continuous_Random_Variables",
        "topicTitle": "03 · Discrete & Continuous RVs",
        "title": "Mixed CDF Discontinuity Jumps & Point Masses (Stanford Stats 116)",
        "kind2": "pyq",
        "source": "Stanford Stats 116 / Ross 2.3",
        "marks": "[10 Marks]",
        "question": """<p>Let $X$ have the mixed discrete-continuous cumulative distribution function:
$$F(x) = \\begin{cases} 
0 & x < 0 \\\\ 
\\frac{x}{2} & 0 \\le x < 1 \\\\ 
\\frac{2}{3} & 1 \\le x < 2 \\\\ 
1 & x \\ge 2 
\\end{cases}$$</p>
<p><span class="part">(a)</span> Compute the point mass probabilities $\\mathbb{P}(X = 1)$ and $\\mathbb{P}(X = 2)$.</p>
<p><span class="part">(b)</span> Compute the interval probabilities $\\mathbb{P}(0.5 < X \\le 1.5)$, $\\mathbb{P}(0.5 \\le X < 1.5)$, and $\\mathbb{P}(X > 1)$.</p>
<p><span class="part">(c)</span> Decompose $F(x)$ into a convex combination of a purely discrete CDF $F_{\\text{disc}}(x)$ and a purely continuous CDF $F_{\\text{cont}}(x)$:
$$F(x) = \\alpha F_{\\text{disc}}(x) + (1 - \\alpha) F_{\\text{cont}}(x)$$</p>""",
        "solution": """<p><span class="part">Part (a): Point Mass Discontinuities</span><br>
For any CDF $F$, the point mass at $x_0$ equals the jump height: $\\mathbb{P}(X = x_0) = F(x_0) - F(x_0^-) = F(x_0) - \\lim_{x \\uparrow x_0} F(x)$.<br>
- At $x = 1$:
$$\\mathbb{P}(X = 1) = F(1) - F(1^-) = \\frac{2}{3} - \\lim_{x \\uparrow 1} \\frac{x}{2} = \\frac{2}{3} - \\frac{1}{2} = <span class=\"ans\">\\frac{1}{6}</span>$$
- At $x = 2$:
$$\\mathbb{P}(X = 2) = F(2) - F(2^-) = 1 - \\frac{2}{3} = <span class=\"ans\">\\frac{1}{3}</span>$$
The total discrete mass is $\\alpha = 1/6 + 1/3 = 1/2$.</p>

<p><span class="part">Part (b): Interval Probabilities</span><br>
- $\\mathbb{P}(0.5 < X \\le 1.5) = F(1.5) - F(0.5) = \\frac{2}{3} - \\frac{0.5}{2} = \\frac{2}{3} - \\frac{1}{4} = <span class=\"ans\">\\frac{5}{12}</span>$<br>
- $\\mathbb{P}(0.5 \\le X < 1.5) = F(1.5^-) - F(0.5^-) = \\frac{2}{3} - \\frac{0.5}{2} = <span class=\"ans\">\\frac{5}{12}</span>$ (since $F$ is continuous at $0.5$ and $1.5$)<br>
- $\\mathbb{P}(X > 1) = 1 - F(1) = 1 - \\frac{2}{3} = <span class=\"ans\">\\frac{1}{3}</span>$</p>

<p><span class="part">Part (c): Mixture Decomposition</span><br>
Total discrete weight: $\\alpha = \\mathbb{P}(X = 1) + \\mathbb{P}(X = 2) = 1/6 + 1/3 = 1/2$.<br>
1. <strong>Discrete CDF $F_{\\text{disc}}$:</strong> has point mass $(1/6)/(1/2) = 1/3$ at $x=1$ and $(1/3)/(1/2) = 2/3$ at $x=2$:
$$F_{\\text{disc}}(x) = \\begin{cases} 0 & x < 1 \\\\ 1/3 & 1 \\le x < 2 \\\\ 1 & x \\ge 2 \\end{cases}$$
2. <strong>Continuous CDF $F_{\\text{cont}}$:</strong> has density on $[0, 1)$ with mass $1/2$ normalized by $(1 - \\alpha) = 1/2$:
$$F_{\\text{cont}}(x) = \\begin{cases} 0 & x < 0 \\\\ x & 0 \\le x < 1 \\\\ 1 & x \\ge 1 \\end{cases}$$
<span class=\"ans\">Thus $F(x) = \\frac{1}{2} F_{\\text{disc}}(x) + \\frac{1}{2} F_{\\text{cont}}(x)$.</span></p>""",
        "takeaway": "CDF right-continuity implies jump heights strictly equal point masses: $\\mathbb{P}(X = c) = F(c) - F(c^-)$. Any mixed CDF uniquely factorizes into a convex sum of a jump step function and an absolutely continuous integral."
    },
    {
        "id": 30393,
        "subject": "StoMA",
        "topicId": "03_Discrete_and_Continuous_Random_Variables",
        "topicTitle": "03 · Discrete & Continuous RVs",
        "title": "The Cauchy Anomaly: Undefined Expectation (Generated Exam)",
        "kind2": "practice",
        "source": "Berkeley EECS 126 / MIT Benchmark",
        "marks": "[10 Marks]",
        "question": """<p>Consider the standard Cauchy distribution with probability density function:
$$f_X(x) = \\frac{1}{\\pi(1 + x^2)}, \\quad x \\in \\mathbb{R}$$</p>
<p><span class="part">(a)</span> Rigorously prove that the expected value $\\mathbb{E}[X]$ is <strong>strictly undefined</strong> (does not exist) in probability theory, rather than equal to $0$.</p>
<p><span class="part">(b)</span> Explain why the Cauchy principal value $\\lim_{R \\to \\infty} \\int_{-R}^R x f_X(x) \\, dx = 0$ is NOT accepted as a valid expectation.</p>
<p><span class="part">(c)</span> What is the distribution of the sample mean $\\bar{X}_n = \\frac{1}{n} \\sum_{i=1}^n X_i$ for $n$ independent Cauchy random variables? How does this contradict the Weak Law of Large Numbers?</p>""",
        "solution": """<p><span class="part">Part (a): Measure-Theoretic Existence of Expectation</span><br>
By definition, for any random variable $X$, $\\mathbb{E}[X] = \\mathbb{E}[X^+] - \\mathbb{E}[X^-]$ exists if and only if at least one of $\\mathbb{E}[X^+]$ or $\\mathbb{E}[X^-]$ is finite (or equivalently, $\\mathbb{E}[|X|] < \\infty$).<br>
Compute the integral of the positive part $X^+ = \\max(X, 0)$:
$$\\mathbb{E}[X^+] = \\int_0^\\infty x \\frac{1}{\\pi(1 + x^2)} \\, dx = \\lim_{M \\to \\infty} \\left[ \\frac{1}{2\\pi} \\ln(1 + x^2) \\right]_0^M = \\lim_{M \\to \\infty} \\frac{1}{2\\pi} \\ln(1 + M^2) = +\\infty$$
By symmetry, the negative part also diverges:
$$\\mathbb{E}[X^-] = \\int_{-\\infty}^0 (-x) \\frac{1}{\\pi(1 + x^2)} \\, dx = +\\infty$$
Thus:
$$\\mathbb{E}[X] = \\mathbb{E}[X^+] - \\mathbb{E}[X^-] = (+\\infty) - (+\\infty) \\quad \\text{--- Indeterminate Form!}$$
<span class=\"ans\">Therefore, $\\mathbb{E}[X]$ does not exist.</span></p>

<p><span class="part">Part (b): Failure of Cauchy Principal Value</span><br>
In probability theory, expectation must be invariant under change of variables and independent of arbitrary summation order (Fubini-Tonelli theorem).<br>
If we evaluate the limit with asymmetric boundaries $a(R) = -R$ and $b(R) = 2R$:
$$\\lim_{R \\to \\infty} \\int_{-R}^{2R} \\frac{x}{\\pi(1 + x^2)} \\, dx = \\lim_{R \\to \\infty} \\frac{1}{2\\pi} [\\ln(1 + 4R^2) - \\ln(1 + R^2)] = \\frac{1}{2\\pi} \\ln(4) = \\frac{\\ln 2}{\\pi} \\ne 0$$
Because the result depends entirely on how fast the boundaries expand to infinity, <span class=\"ans\">it is not a stable Lebesgue integral</span>.</p>

<p><span class="part">Part (c): Distribution of Sample Mean & WLLN Collapse</span><br>
The characteristic function of a standard Cauchy variable is $\\phi_X(t) = \\mathbb{E}[e^{itX}] = e^{-|t|}$.<br>
For the sample mean $\\bar{X}_n = \\frac{1}{n} \\sum_{i=1}^n X_i$:
$$\\phi_{\\bar{X}_n}(t) = \\prod_{i=1}^n \\phi_{X_i}\\left(\\frac{t}{n}\\right) = \\left[ e^{-|t/n|} \\right]^n = e^{-n \\frac{|t|}{n}} = e^{-|t|}$$
<span class=\"ans\">The sample mean $\\bar{X}_n$ is itself exactly $\\text{Cauchy}(0, 1)$ for any $n \\ge 1$!</span><br>
Averaging a million Cauchy random variables provides <strong>zero</strong> noise reduction: the average is just as volatile as a single observation. The WLLN fails because the condition $\\mathbb{E}[|X|] < \\infty$ is violated.</p>""",
        "takeaway": "A symmetric distribution only has mean 0 if $\\mathbb{E}[|X|] < \\infty$. When both tails diverge to $\\infty$, $\\mathbb{E}[X] = \\infty - \\infty$ is undefined. Averaging i.i.d. Cauchy variables fails to concentrate: $\\bar{X}_n$ remains identical in distribution to $X_1$."
    },

    # =========================================================================
    # TOPIC 04: Transformations of Random Variables
    # =========================================================================
    {
        "id": 30491,
        "subject": "StoMA",
        "topicId": "04_Transformations_and_Functions_of_a_Random_Variable",
        "topicTitle": "04 · Transformations of Random Variables",
        "title": "Chi-Square Derivation from Standard Normal (IISc Test 1)",
        "kind2": "pyq",
        "source": "IISc StoMA Test 1 / Ross Ch 2",
        "marks": "[8 Marks]",
        "question": """<p>Let $X \\sim \\mathcal{N}(0, 1)$ be a standard normal random variable with density $f_X(x) = \\frac{1}{\\sqrt{2\\pi}} e^{-x^2/2}$ for $x \\in \\mathbb{R}$.</p>
<p><span class="part">(a)</span> Using the CDF method, derive the probability density function $f_Y(y)$ of the quadratic transformation $Y = X^2$.</p>
<p><span class="part">(b)</span> Identify the distribution of $Y$ as a known member of the Gamma family and specify its parameters $\\alpha$ (shape) and $\\lambda$ (rate).</p>
<p><span class="part">(c)</span> Explain why a direct application of the 1-to-1 Jacobian formula $f_Y(y) = f_X(g^{-1}(y)) |(g^{-1})'(y)|$ produces an incorrect result.</p>""",
        "solution": """<p><span class="part">Part (a): Derivation via CDF Method</span><br>
Since $Y = X^2 \\ge 0$, for $y \\le 0$, $F_Y(y) = 0$.<br>
For $y > 0$:
$$F_Y(y) = \\mathbb{P}(Y \\le y) = \\mathbb{P}(X^2 \\le y) = \\mathbb{P}(-\\sqrt{y} \\le X \\le \\sqrt{y}) = F_X(\\sqrt{y}) - F_X(-\\sqrt{y})$$
By symmetry of the standard normal CDF, $F_X(-\\sqrt{y}) = 1 - F_X(\\sqrt{y})$, so:
$$F_Y(y) = 2F_X(\\sqrt{y}) - 1 = 2 \\int_0^{\\sqrt{y}} \\frac{1}{\\sqrt{2\\pi}} e^{-t^2/2} \\, dt$$
Differentiating with respect to $y$ using the Leibniz Rule / Chain Rule:
$$f_Y(y) = \\frac{d}{dy} F_Y(y) = 2 f_X(\\sqrt{y}) \\cdot \\frac{d}{dy}(\\sqrt{y}) = 2 \\left( \\frac{1}{\\sqrt{2\\pi}} e^{-(\\sqrt{y})^2/2} \\right) \\left( \\frac{1}{2\\sqrt{y}} \\right)$$
$$<span class=\"ans\">f_Y(y) = \\frac{1}{\\sqrt{2\\pi}} y^{-1/2} e^{-y/2}, \\quad y > 0</span>$$</p>

<p><span class="part">Part (b): Identification as Gamma Distribution</span><br>
Recall the Gamma density with shape $\\alpha$ and rate $\\lambda$:
$$f(y) = \\frac{\\lambda^\\alpha}{\\Gamma(\\alpha)} y^{\\alpha - 1} e^{-\\lambda y}, \\quad y > 0$$
Using $\\Gamma(1/2) = \\sqrt{\\pi}$, set $\\alpha = 1/2$ and $\\lambda = 1/2$:
$$f(y) = \\frac{(1/2)^{1/2}}{\\sqrt{\\pi}} y^{-1/2} e^{-y/2} = \\frac{1}{\\sqrt{2\\pi}} y^{-1/2} e^{-y/2}$$
<span class=\"ans\">Thus $Y \\sim \\text{Gamma}(\\alpha = 1/2, \\lambda = 1/2) \\equiv \\chi^2(1)$ (Chi-Square with 1 degree of freedom).</span></p>

<p><span class="part">Part (c): Failure of Monotone Jacobian Formula</span><br>
The function $g(x) = x^2$ is <strong>2-to-1</strong> on $\\mathbb{R}$, not 1-to-1.<br>
For any $y > 0$, there are two pre-images: $x_1 = +\\sqrt{y}$ and $x_2 = -\\sqrt{y}$.<br>
A naive 1-to-1 formula only includes one branch ($x = +\\sqrt{y}$), missing half the probability mass and yielding $f_Y(y) = \\frac{1}{2\\sqrt{2\\pi}} y^{-1/2} e^{-y/2}$ which integrates to $1/2$.<br>
<span class=\"ans\">For multi-to-one maps, one must sum over all pre-image roots: $f_Y(y) = \\sum_i \\frac{f_X(x_i)}{|g'(x_i)|}$.</span></p>""",
        "takeaway": "Sastry's #1 favorite transformation trap: $g(x) = x^2$ is not monotone on $\\mathbb{R}$. Always use the CDF method or sum Jacobians over all pre-images: $f_Y(y) = \\sum_{i} f_X(x_i)/|g'(x_i)|$."
    },
    {
        "id": 30492,
        "subject": "StoMA",
        "topicId": "04_Transformations_and_Functions_of_a_Random_Variable",
        "topicTitle": "04 · Transformations of Random Variables",
        "title": "Inverse Transform Sampling & Probability Integral Transform (Stanford Stats 116)",
        "kind2": "pyq",
        "source": "Stanford Stats 116 / Ross 2.4",
        "marks": "[10 Marks]",
        "question": """<p><span class="part">(a)</span> State and prove the <strong>Probability Integral Transform Theorem</strong>: if $X$ is a continuous random variable with strictly increasing CDF $F_X(x)$, then $U = F_X(X) \\sim \\text{Uniform}(0, 1)$.</p>
<p><span class="part">(b)</span> Let $U \\sim \\text{Uniform}(0, 1)$. Using the Inverse Transform method, find an explicit function $g(u)$ such that $X = g(U)$ follows the standard Cauchy distribution:
$$f_X(x) = \\frac{1}{\\pi(1 + x^2)}, \\quad x \\in \\mathbb{R}$$</p>
<p><span class="part">(c)</span> Explain how this theorem provides the theoretical foundation for pseudo-random variate generation in computer simulations.</p>""",
        "solution": """<p><span class="part">Part (a): Proof of Probability Integral Transform</span><br>
Let $U = F_X(X)$. Since $F_X$ is strictly increasing, its inverse $F_X^{-1}$ exists and is strictly increasing.<br>
The support of $U$ is $[0, 1]$. For any $u \\in (0, 1)$:
$$F_U(u) = \\mathbb{P}(U \\le u) = \\mathbb{P}(F_X(X) \\le u) = \\mathbb{P}(X \\le F_X^{-1}(u)) = F_X(F_X^{-1}(u)) = u$$
Since the CDF of $U$ is $F_U(u) = u$ for $u \\in [0, 1]$, <span class=\"ans\">$U \\sim \\text{Uniform}(0, 1)$</span>. $\\blacksquare$</p>

<p><span class="part">Part (b): Inverse Transform for Cauchy Distribution</span><br>
To generate $X \\sim \\text{Cauchy}$, we must compute $g(u) = F_X^{-1}(u)$.<br>
1. <strong>Find the CDF:</strong>
$$F_X(x) = \\int_{-\\infty}^x \\frac{1}{\\pi(1 + t^2)} \\, dt = \\frac{1}{\\pi} [\\arctan(t)]_{-\\infty}^x = \\frac{1}{\\pi}\\left( \\arctan(x) - \\left(-\\frac{\\pi}{2}\\right) \\right) = \\frac{1}{\\pi}\\arctan(x) + \\frac{1}{2}$$
2. <strong>Invert the CDF:</strong> Set $u = F_X(x)$ and solve for $x$:
$$u = \\frac{1}{\\pi}\\arctan(x) + \\frac{1}{2} \\implies \\pi\\left(u - \\frac{1}{2}\\right) = \\arctan(x)$$
$$<span class=\"ans\">x = g(u) = \\tan\\left( \\pi \\left(u - \\frac{1}{2}\\right) \\right)</span>$$
Thus if $U \\sim \\text{Uniform}(0, 1)$, then $X = \\tan(\\pi(U - 1/2)) \\sim \\text{Cauchy}(0, 1)$.</p>

<p><span class="part">Part (c): Application to Stochastic Simulation</span><br>
Standard computing algorithms generate high-quality pseudo-random uniform variates $U \\in (0, 1)$.<br>
To sample an arbitrary continuous target distribution with invertible CDF $F_X$:
1. Generate $U \\sim \\text{Uniform}(0, 1)$.<br>
2. Return $X = F_X^{-1}(U)$.<br>
By Part (a), $\\mathbb{P}(F_X^{-1}(U) \\le x) = \\mathbb{P}(U \\le F_X(x)) = F_X(x)$, so <span class=\"ans\">$X$ is guaranteed to follow the exact target distribution $F_X$</span>.</p>""",
        "takeaway": "The Probability Integral Transform is bidirectional: any continuous RV transformed by its own CDF becomes uniform ($F_X(X) \\sim \\text{Uniform}(0, 1)$), and feeding uniform bits through an inverse CDF yields that distribution ($F_X^{-1}(U) \\sim F_X$)."
    },
    {
        "id": 30493,
        "subject": "StoMA",
        "topicId": "04_Transformations_and_Functions_of_a_Random_Variable",
        "topicTitle": "04 · Transformations of Random Variables",
        "title": "Periodic Transformation & The Arcsine Law: PDF of Y = sin(X) (Generated Exam)",
        "kind2": "practice",
        "source": "MIT 6.041 / Berkeley Benchmark",
        "marks": "[10 Marks]",
        "question": """<p>Let $X \\sim \\text{Uniform}(0, 2\\pi)$ with density $f_X(x) = \\frac{1}{2\\pi}$ for $x \\in (0, 2\\pi)$. Consider the non-linear transformation:
$$Y = \\sin(X)$$</p>
<p><span class="part">(a)</span> State the support (range) of $Y$. For a given $y$ in the interior of this support, how many pre-image roots exist in $(0, 2\\pi)$?</p>
<p><span class="part">(b)</span> Derive the probability density function $f_Y(y)$ using the multi-root Jacobian formula.</p>
<p><span class="part">(c)</span> Explain why $f_Y(y) \\to \\infty$ as $y \\to \\pm 1$. What is the geometric / physical explanation for this \"U-shaped\" (Arcsine) density?</p>""",
        "solution": """<p><span class="part">Part (a): Support and Pre-Image Counting</span><br>
Since $\\sin(x)$ maps $(0, 2\\pi)$ onto $[-1, 1]$, the support of $Y$ is $[-1, 1]$.<br>
For any $y \\in (-1, 1)$, the equation $\\sin(x) = y$ has exactly <span class=\"ans\">two roots</span> in $(0, 2\\pi)$:
- If $y \\ge 0$: $x_1 = \\arcsin(y) \\in [0, \\pi/2]$ and $x_2 = \\pi - \\arcsin(y) \\in [\\pi/2, \\pi]$.<br>
- If $y < 0$: $x_1 = \\pi - \\arcsin(y) \\in [\\pi, 3\\pi/2]$ and $x_2 = 2\\pi + \\arcsin(y) \\in [3\\pi/2, 2\\pi]$.</p>

<p><span class="part">Part (b): Multi-Root Jacobian Derivation</span><br>
For $g(x) = \\sin(x)$, the derivative is $g'(x) = \\cos(x)$.<br>
At any root $x_k$ where $\\sin(x_k) = y$:
$$|g'(x_k)| = |\\cos(x_k)| = \\sqrt{1 - \\sin^2(x_k)} = \\sqrt{1 - y^2}$$
Applying the multi-root transformation theorem:
$$f_Y(y) = \\sum_{k=1}^2 \\frac{f_X(x_k)}{|g'(x_k)|} = \\frac{f_X(x_1)}{\\sqrt{1 - y^2}} + \\frac{f_X(x_2)}{\\sqrt{1 - y^2}}$$
Since $f_X(x) = \\frac{1}{2\\pi}$ for all $x \\in (0, 2\\pi)$:
$$f_Y(y) = \\frac{1/(2\\pi)}{\\sqrt{1 - y^2}} + \\frac{1/(2\\pi)}{\\sqrt{1 - y^2}} = <span class=\"ans\">\\frac{1}{\\pi \\sqrt{1 - y^2}}, \\quad -1 < y < 1</span>$$
This is the celebrated <strong>Arcsine distribution</strong>.</p>

<p><span class="part">Part (c): Singularity at $y = \\pm 1$ and Physical Meaning</span><br>
As $y \\to \\pm 1$, $\\sqrt{1 - y^2} \\to 0$, causing $f_Y(y) \\to +\\infty$.<br>
<strong>Physical & Geometric Intuition:</strong><br>
Near the extrema $x = \\pi/2$ and $x = 3\\pi/2$, the slope of the sine wave flattens out: $\\frac{d}{dx}\\sin(x) = 0$.<br>
A particle oscillating harmonically ($y = \\sin(x)$) decelerates to zero velocity at the turning points ($y = \\pm 1$) before reversing direction.<br>
Consequently, it spends far more time near the boundaries $y = \\pm 1$ than in the middle $y = 0$, producing infinite density peaks at the turning points while remaining a completely valid probability distribution (integrates to $\\frac{1}{\\pi}[\\arcsin(1) - \\arcsin(-1)] = 1$).</p>""",
        "takeaway": "When $g'(x) = 0$ at stationary turning points of a transformation, the resulting density blows up as an integrable singularity $(1 - y^2)^{-1/2}$. This Arcsine law governs sinusoidal oscillators and random walk excursions."
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
    for c in PRACTICE_STOMA_03_04:
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
