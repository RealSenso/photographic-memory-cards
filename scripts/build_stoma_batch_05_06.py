#!/usr/bin/env python3
"""
build_stoma_batch_05_06.py
Generates 6 flippable practice cards for StoMA Topics 05 and 06:
  Topic 05: Expectation, Variance, Moments and Generating Functions (3 cards)
  Topic 06: Probability Inequalities: Markov, Chebyshev, Chernoff (3 cards)
"""

import os
import re
import json

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PRACTICE_STOMA_05_06 = [
    # =========================================================================
    # TOPIC 05: Expectation, Variance & MGFs
    # =========================================================================
    {
        "id": 30591,
        "subject": "StoMA",
        "topicId": "05_Expectation_Variance_Moments_and_Generating_Functions",
        "topicTitle": "05 · Expectation, Variance & MGFs",
        "title": "Tail Sum Formula & Geometric Expectation (IISc Test 1)",
        "kind2": "pyq",
        "source": "IISc StoMA Test 1 / Ross Ch 2",
        "marks": "[8 Marks]",
        "question": """<p><span class="part">(a)</span> State and prove the <strong>tail sum formula</strong> for the expectation of a non-negative integer-valued random variable $X$:
$$\\mathbb{E}[X] = \\sum_{k=1}^\\infty \\mathbb{P}(X \\ge k)$$</p>
<p><span class="part">(b)</span> Use the tail sum formula to compute the expectation $\\mathbb{E}[X]$ of a Geometric random variable with PMF $\\mathbb{P}(X = k) = (1 - p)^{k-1} p$ for $k = 1, 2, \\dots$.</p>
<p><span class="part">(c)</span> Extend the method to prove $\\mathbb{E}[X^2] = \\sum_{k=1}^\\infty (2k - 1) \\mathbb{P}(X \\ge k)$ and find $\\operatorname{Var}(X)$.</p>""",
        "solution": """<p><span class="part">Part (a): Proof of Tail Sum Formula</span><br>
Express $X$ as a sum of indicator random variables:
$$X = \\sum_{k=1}^\\infty \\mathbf{1}_{\\{X \\ge k\\}}$$
Taking expectations on both sides and interchanging expectation and infinite summation (valid by Fubini-Tonelli since all terms are non-negative):
$$\\mathbb{E}[X] = \\mathbb{E}\\left[ \\sum_{k=1}^\\infty \\mathbf{1}_{\\{X \\ge k\\}} \\right] = \\sum_{k=1}^\\infty \\mathbb{E}[\\mathbf{1}_{\\{X \\ge k\\}}] = <span class=\"ans\">\\sum_{k=1}^\\infty \\mathbb{P}(X \\ge k)</span>$$</p>

<p><span class="part">Part (b): Application to Geometric Distribution</span><br>
For $X \\sim \\text{Geometric}(p)$, the event $\\{X \\ge k\\}$ means the first $k-1$ independent Bernoulli trials all resulted in failure.<br>
Thus:
$$\\mathbb{P}(X \\ge k) = (1 - p)^{k-1} \\quad \\text{for } k \\ge 1$$
Applying the tail sum formula:
$$\\mathbb{E}[X] = \\sum_{k=1}^\\infty (1 - p)^{k-1} = 1 + (1-p) + (1-p)^2 + \\dots = \\frac{1}{1 - (1 - p)} = <span class=\"ans\">\\frac{1}{p}</span>$$</p>

<p><span class="part">Part (c): Second Moment and Variance</span><br>
Notice that $k^2 = \\sum_{j=1}^k (2j - 1)$. Therefore:
$$X^2 = \\sum_{k=1}^\\infty (2k - 1) \\mathbf{1}_{\\{X \\ge k\\}} \\implies \\mathbb{E}[X^2] = \\sum_{k=1}^\\infty (2k - 1) \\mathbb{P}(X \\ge k)$$
For the Geometric distribution:
$$\\mathbb{E}[X^2] = \\sum_{k=1}^\\infty (2k - 1)(1 - p)^{k-1} = 2 \\sum_{k=1}^\\infty k (1-p)^{k-1} - \\sum_{k=1}^\\infty (1-p)^{k-1} = \\frac{2}{p^2} - \\frac{1}{p} = \\frac{2 - p}{p^2}$$
Hence the variance is:
$$\\operatorname{Var}(X) = \\mathbb{E}[X^2] - (\\mathbb{E}[X])^2 = \\frac{2 - p}{p^2} - \\frac{1}{p^2} = <span class=\"ans\">\\frac{1 - p}{p^2}</span>$$</p>""",
        "takeaway": "The tail sum formula replaces calculating $\\sum k p_k$ with summing survival probabilities $\\sum \\mathbb{P}(X \\ge k)$. For geometric and exponential distributions, this transforms tedious series into elementary geometric series."
    },
    {
        "id": 30592,
        "subject": "StoMA",
        "topicId": "05_Expectation_Variance_Moments_and_Generating_Functions",
        "topicTitle": "05 · Expectation, Variance & MGFs",
        "title": "Gaussian MGF & Fourth Central Moment (Stanford Stats 116)",
        "kind2": "pyq",
        "source": "Stanford Stats 116 / Ross 2.6",
        "marks": "[10 Marks]",
        "question": """<p>Let $X \\sim \\mathcal{N}(\\mu, \\sigma^2)$ be a Gaussian random variable.</p>
<p><span class="part">(a)</span> Derive the Moment Generating Function $M_X(t) = \\mathbb{E}[e^{tX}]$ by completing the square in the Gaussian integral.</p>
<p><span class="part">(b)</span> Using the Taylor series expansion of the centered MGF $M_{X-\\mu}(t)$, determine the fourth central moment $\\mu_4 = \\mathbb{E}[(X - \\mu)^4]$.</p>
<p><span class="part">(c)</span> Compute the kurtosis $\\kappa = \\frac{\\mathbb{E}[(X - \\mu)^4]}{\\sigma^4}$ and state Isserlis' theorem for higher even moments of the normal distribution.</p>""",
        "solution": """<p><span class="part">Part (a): Derivation of Gaussian MGF</span><br>
Let $Z = \\frac{X - \\mu}{\\sigma} \\sim \\mathcal{N}(0, 1)$. Compute $M_Z(t)$:
$$M_Z(t) = \\int_{-\\infty}^\\infty e^{tz} \\frac{1}{\\sqrt{2\\pi}} e^{-z^2/2} \\, dz = \\frac{1}{\\sqrt{2\\pi}} \\int_{-\\infty}^\\infty e^{-(z^2 - 2tz)/2} \\, dz$$
Complete the square in the exponent: $z^2 - 2tz = (z - t)^2 - t^2$:
$$M_Z(t) = e^{t^2/2} \\left( \\frac{1}{\\sqrt{2\\pi}} \\int_{-\\infty}^\\infty e^{-(z - t)^2/2} \\, dz \\right) = e^{t^2/2} \\cdot 1 = e^{t^2/2}$$
Using the linear scaling property $M_{aZ + b}(t) = e^{bt} M_Z(at)$:
$$M_X(t) = M_{\\mu + \\sigma Z}(t) = <span class=\"ans\">\\exp\\left( \\mu t + \\frac{1}{2}\\sigma^2 t^2 \\right)</span>$$</p>

<p><span class="part">Part (b): Fourth Central Moment</span><br>
The centered variable $Y = X - \\mu \\sim \\mathcal{N}(0, \\sigma^2)$ has MGF:
$$M_Y(t) = e^{\\sigma^2 t^2/2}$$
Expand this exponential function using its Taylor series:
$$e^{\\sigma^2 t^2/2} = 1 + \\left(\\frac{\\sigma^2 t^2}{2}\\right) + \\frac{1}{2!} \\left(\\frac{\\sigma^2 t^2}{2}\\right)^2 + \\frac{1}{3!} \\left(\\frac{\\sigma^2 t^2}{2}\\right)^3 + \\dots = 1 + \\frac{\\sigma^2}{2} t^2 + \\frac{\\sigma^4}{8} t^4 + \\dots$$
By definition of the MGF expansion:
$$M_Y(t) = \\sum_{n=0}^\\infty \\mathbb{E}[Y^n] \\frac{t^n}{n!} = 1 + \\mathbb{E}[Y] t + \\mathbb{E}[Y^2] \\frac{t^2}{2!} + \\mathbb{E}[Y^3] \\frac{t^3}{3!} + \\mathbb{E}[Y^4] \\frac{t^4}{4!} + \\dots$$
Matching coefficients of $t^4$:
$$\\frac{\\mathbb{E}[Y^4]}{4!} = \\frac{\\sigma^4}{8} \\implies \\mathbb{E}[Y^4] = 24 \\cdot \\frac{\\sigma^4}{8} = <span class=\"ans\">3\\sigma^4</span>$$</p>

<p><span class="part">Part (c): Kurtosis and Isserlis' Theorem</span><br>
The kurtosis is:
$$\\kappa = \\frac{\\mu_4}{\\sigma^4} = \\frac{3\\sigma^4}{\\sigma^4} = <span class=\"ans\">3</span> \\quad (\\text{Excess Kurtosis } \\kappa - 3 = 0)$$
By Isserlis' theorem (Wick's probability theorem), all odd central moments are 0 by symmetry, and all even central moments are given by the double factorial:
$$\\mathbb{E}[(X - \\mu)^{2m}] = (2m - 1)!! \\, \\sigma^{2m} = \\frac{(2m)!}{2^m m!} \\sigma^{2m}$$
For $m=2$: $(3)!! \\sigma^4 = 3\\sigma^4$.</p>""",
        "takeaway": "The Gaussian MGF $e^{\\mu t + \\sigma^2 t^2/2}$ contains purely linear and quadratic exponents. Consequently, all odd central moments vanish, and all even moments are given by $(2m-1)!! \\sigma^{2m}$."
    },
    {
        "id": 30593,
        "subject": "StoMA",
        "topicId": "05_Expectation_Variance_Moments_and_Generating_Functions",
        "topicTitle": "05 · Expectation, Variance & MGFs",
        "title": "Coupon Collector's Problem & Variance via Geometric RVs (Generated Exam)",
        "kind2": "practice",
        "source": "Berkeley EECS 126 / MIT Benchmark",
        "marks": "[10 Marks]",
        "question": """<p>Each box of cereal contains one of $n$ distinct coupons chosen uniformly at random. Let $T$ be the total number of boxes purchased until a complete collection of all $n$ coupons is acquired.</p>
<p><span class="part">(a)</span> Decompose $T = \\sum_{i=1}^n T_i$ into independent geometric stages and find the exact expected value $\\mathbb{E}[T]$ in terms of the Harmonic number $H_n = \\sum_{k=1}^n \\frac{1}{k}$. Determine its asymptotic growth as $n \\to \\infty$.</p>
<p><span class="part">(b)</span> Derive the exact variance $\\operatorname{Var}(T)$ and compute its asymptotic limit as $n \\to \\infty$ using $\\sum_{k=1}^\\infty \\frac{1}{k^2} = \\frac{\\pi^2}{6}$.</p>""",
        "solution": """<p><span class="part">Part (a): Decomposition into Geometric Stages</span><br>
Let $T_i$ be the number of additional boxes purchased to find the $i$-th new coupon, after having already collected $i-1$ distinct coupons.<br>
At this stage, there are $n - (i-1)$ unseen coupons remaining out of $n$.<br>
The probability of obtaining an unseen coupon on any single purchase is:
$$p_i = \\frac{n - (i - 1)}{n} = \\frac{n - i + 1}{n}$$
Since purchases are independent with constant success probability $p_i$, each stage is an independent Geometric random variable:
$$T_i \\sim \\text{Geometric}(p_i) \\implies \\mathbb{E}[T_i] = \\frac{1}{p_i} = \\frac{n}{n - i + 1}$$
The total time is $T = T_1 + T_2 + \\dots + T_n$. By linearity of expectation:
$$\\mathbb{E}[T] = \\sum_{i=1}^n \\mathbb{E}[T_i] = \\sum_{i=1}^n \\frac{n}{n - i + 1} = n \\sum_{k=1}^n \\frac{1}{k} = <span class=\"ans\">n H_n</span>$$
Using the asymptotic expansion $H_n = \\ln n + \\gamma + O(1/n)$ (where $\\gamma \\approx 0.5772$ is the Euler-Mascheroni constant):
$$\\mathbb{E}[T] = n \\ln n + \\gamma n + O(1) \\sim <span class=\"ans\">n \\ln n</span>$$</p>

<p><span class="part">Part (b): Exact Variance and Asymptotics</span><br>
Because the random variables $T_1, \\dots, T_n$ are mutually independent:
$$\\operatorname{Var}(T) = \\sum_{i=1}^n \\operatorname{Var}(T_i) = \\sum_{i=1}^n \\frac{1 - p_i}{p_i^2}$$
Substitute $p_i = \\frac{k}{n}$ where $k = n - i + 1 \\in \\{1, 2, \\dots, n\\}$:
$$\\frac{1 - p_i}{p_i^2} = \\frac{1 - k/n}{(k/n)^2} = \\frac{n^2}{k^2} - \\frac{n}{k}$$
Summing over $k = 1, \\dots, n$:
$$\\operatorname{Var}(T) = \\sum_{k=1}^n \\left( \\frac{n^2}{k^2} - \\frac{n}{k} \\right) = <span class=\"ans\">n^2 \\sum_{k=1}^n \\frac{1}{k^2} - n H_n</span>$$
As $n \\to \\infty$, $\\sum_{k=1}^n \\frac{1}{k^2} \\to \\zeta(2) = \\frac{\\pi^2}{6}$, while $n H_n \\sim n \\ln n = o(n^2)$.<br>
Therefore:
$$\\lim_{n \\to \\infty} \\frac{\\operatorname{Var}(T)}{n^2} = \\frac{\\pi^2}{6} \\implies <span class=\"ans\">\\operatorname{Var}(T) \\sim \\frac{\\pi^2}{6} n^2</span>$$
The standard deviation $\\sigma_T \\approx \\frac{\\pi}{\\sqrt{6}} n \\approx 1.28 n$, which is of order $O(n)$, significantly smaller than the mean $O(n \\ln n)$ (sharp concentration of measure).</p>""",
        "takeaway": "Coupon collection decouples into independent geometric stages $T_i$ with harmonically diminishing probabilities $p_i = k/n$. The expected time is $n H_n \\sim n \\ln n$ and the variance concentrates around $\\frac{\\pi^2}{6} n^2$."
    },

    # =========================================================================
    # TOPIC 06: Probability Inequalities
    # =========================================================================
    {
        "id": 30691,
        "subject": "StoMA",
        "topicId": "06_Probability_Inequalities_Markov_Chebyshev_Chernoff",
        "topicTitle": "06 · Probability Inequalities",
        "title": "Poisson Chernoff Bound & Cramér Transform (IISc Test 1)",
        "kind2": "pyq",
        "source": "IISc StoMA Test 1 / Ross Ch 2",
        "marks": "[8 Marks]",
        "question": """<p>Let $X \\sim \\text{Poisson}(\\lambda)$ with mean $\\lambda > 0$.</p>
<p><span class="part">(a)</span> State the general Chernoff bound for the upper tail $\\mathbb{P}(X \\ge a)$ where $a > \\lambda$.</p>
<p><span class="part">(b)</span> Using the Poisson MGF $M_X(t) = \\exp(\\lambda(e^t - 1))$, derive the optimal Chernoff upper bound on $\\mathbb{P}(X \\ge a)$ for $a > \\lambda$.</p>
<p><span class="part">(c)</span> Compare the asymptotic rate of decay of the Chernoff bound versus Chebyshev's inequality as the threshold $a \\to \\infty$.</p>""",
        "solution": """<p><span class="part">Part (a): General Chernoff Bound</span><br>
For any parameter $t > 0$, the function $x \\mapsto e^{tx}$ is strictly monotonically increasing.<br>
Applying Markov's inequality to the non-negative random variable $e^{tX}$:
$$\\mathbb{P}(X \\ge a) = \\mathbb{P}(e^{tX} \\ge e^{ta}) \\le \\frac{\\mathbb{E}[e^{tX}]}{e^{ta}} = e^{-ta} M_X(t)$$
Since this holds for every $t > 0$, taking the infimum gives the tightest bound:
$$\\mathbb{P}(X \\ge a) \\le \\inf_{t > 0} e^{-ta} M_X(t)$$</p>

<p><span class="part">Part (b): Optimization for Poisson Distribution</span><br>
For $X \\sim \\text{Poisson}(\\lambda)$, $M_X(t) = \\exp(\\lambda(e^t - 1))$. The objective is:
$$g(t) = e^{-ta} M_X(t) = \\exp\\left( -ta + \\lambda(e^t - 1) \\right)$$
To minimize $g(t)$, minimize the exponent $\\psi(t) = -ta + \\lambda(e^t - 1)$:
$$\\psi'(t) = -a + \\lambda e^t = 0 \\implies e^{t^*} = \\frac{a}{\\lambda} \\implies t^* = \\ln\\left(\\frac{a}{\\lambda}\\right)$$
Since $a > \\lambda$, $t^* = \\ln(a/\\lambda) > 0$, so $t^*$ lies strictly in the feasible range $(0, \\infty)$.<br>
Evaluating $\\psi(t^*)$:
$$\\psi(t^*) = -a \\ln\\left(\\frac{a}{\\lambda}\\right) + \\lambda\\left(\\frac{a}{\\lambda} - 1\\right) = -a \\ln\\left(\\frac{a}{\\lambda}\\right) + a - \\lambda$$
Exponentiating:
$$\\mathbb{P}(X \\ge a) \\le \\exp\\left( -a \\ln\\left(\\frac{a}{\\lambda}\\right) + a - \\lambda \\right) = e^{-\\lambda} e^a \\left(\\frac{\\lambda}{a}\\right)^a = <span class=\"ans\">e^{-\\lambda} \\left( \\frac{e\\lambda}{a} \\right)^a</span>$$</p>

<p><span class="part">Part (c): Comparison with Chebyshev's Inequality</span><br>
- <strong>Chebyshev's Inequality:</strong> Since $\\operatorname{Var}(X) = \\lambda$:
$$\\mathbb{P}(X \\ge a) \\le \\mathbb{P}(|X - \\lambda| \\ge a - \\lambda) \\le \\frac{\\operatorname{Var}(X)}{(a - \\lambda)^2} = \\frac{\\lambda}{(a - \\lambda)^2} = O\\left(\\frac{1}{a^2}\\right)$$
Chebyshev decays only <strong>polynomially</strong> ($a^{-2}$).<br>
- <strong>Chernoff Bound:</strong> Decays as $\\left(\\frac{e\\lambda}{a}\\right)^a = e^{-a \\ln(a/(e\\lambda))}$, which is <strong>super-exponential</strong>.<br>
<span class=\"ans\">The Chernoff bound captures the true exponential tail of the Poisson PMF ($e^{-\\lambda}\\lambda^a/a!$), providing an exponentially sharper estimate than Chebyshev.</span></p>""",
        "takeaway": "Chernoff bounding minimizes exponential moments: $\\mathbb{P}(X \\ge a) \\le \\inf_{t>0} e^{-ta} M_X(t)$. For Poisson distributions, the optimal $t^* = \\ln(a/\\lambda)$ produces super-exponential tail decay $e^{-\\lambda}(e\\lambda/a)^a$ matching Stirling's factorial."
    },
    {
        "id": 30692,
        "subject": "StoMA",
        "topicId": "06_Probability_Inequalities_Markov_Chebyshev_Chernoff",
        "topicTitle": "06 · Probability Inequalities",
        "title": "Cantelli's One-Sided Chebyshev Inequality (MIT 6.041 / Bertsekas)",
        "kind2": "pyq",
        "source": "MIT 6.041 / Bertsekas Ch 5",
        "marks": "[10 Marks]",
        "question": """<p>Let $X$ be any random variable with mean $\\mathbb{E}[X] = 0$ and variance $\\operatorname{Var}(X) = \\sigma^2$.</p>
<p><span class="part">(a)</span> Prove <strong>Cantelli's inequality</strong> (the one-sided Chebyshev inequality): for any constant $a > 0$,
$$\\mathbb{P}(X \\ge a) \\le \\frac{\\sigma^2}{\\sigma^2 + a^2}$$</p>
<p><span class="part">(b)</span> Compare Cantelli's bound with the standard two-sided Chebyshev inequality. Why is dividing Chebyshev by 2 mathematically invalid?</p>
<p><span class="part">(c)</span> Prove that Cantelli's bound is <strong>sharp (tight)</strong> by constructing a two-point random variable that achieves exact equality.</p>""",
        "solution": """<p><span class="part">Part (a): Derivation of Cantelli's Inequality</span><br>
For any constant $u > 0$, the event $\\{X \\ge a\\}$ is identical to $\\{X + u \\ge a + u\\}$.<br>
Since $a + u > 0$, $X + u \\ge a + u \\implies (X + u)^2 \\ge (a + u)^2$. Therefore:
$$\\mathbb{P}(X \\ge a) \\le \\mathbb{P}\\left( (X + u)^2 \\ge (a + u)^2 \\right)$$
Applying Markov's inequality to the non-negative random variable $(X + u)^2$:
$$\\mathbb{P}(X \\ge a) \\le \\frac{\\mathbb{E}[(X + u)^2]}{(a + u)^2} = \\frac{\\mathbb{E}[X^2] + 2u\\mathbb{E}[X] + u^2}{(a + u)^2} = \\frac{\\sigma^2 + u^2}{(a + u)^2}$$
To obtain the tightest bound, minimize $h(u) = \\frac{\\sigma^2 + u^2}{(a + u)^2}$ over $u > 0$. Differentiating:
$$h'(u) = \\frac{2u(a + u)^2 - 2(a + u)(\\sigma^2 + u^2)}{(a + u)^4} = \\frac{2(ua - \\sigma^2)}{(a + u)^3} = 0 \\implies u^* = \\frac{\\sigma^2}{a}$$
Evaluating $h(u^*)$ with $u^* = \\sigma^2/a$:
$$h(u^*) = \\frac{\\sigma^2 + \\sigma^4/a^2}{(a + \\sigma^2/a)^2} = \\frac{\\sigma^2 (1 + \\sigma^2/a^2)}{a^2 (1 + \\sigma^2/a^2)^2} = <span class=\"ans\">\\frac{\\sigma^2}{\\sigma^2 + a^2}</span>$$</p>

<p><span class="part">Part (b): Comparison with Chebyshev</span><br>
Standard Chebyshev bounds both tails: $\\mathbb{P}(|X| \\ge a) \\le \\frac{\\sigma^2}{a^2}$.<br>
Dividing by 2 assumes symmetric tails $\\mathbb{P}(X \\ge a) = \\mathbb{P}(X \\le -a)$, which is false for asymmetric distributions.<br>
Cantelli's bound $\\frac{\\sigma^2}{\\sigma^2 + a^2}$ requires <strong>zero symmetry assumptions</strong> and holds universally for all distributions.</p>

<p><span class="part">Part (c): Tightness Construction</span><br>
Define a discrete two-point random variable $X$ taking values $\\{a, -b\\}$:
- $\\mathbb{P}(X = a) = p = \\frac{\\sigma^2}{\\sigma^2 + a^2}$
- $\\mathbb{P}(X = -b) = 1 - p = \\frac{a^2}{\\sigma^2 + a^2}$, where $b = \\frac{\\sigma^2}{a}$<br>
1. Mean: $\\mathbb{E}[X] = a p - b(1-p) = a \\left(\\frac{\\sigma^2}{\\sigma^2 + a^2}\\right) - \\frac{\\sigma^2}{a} \\left(\\frac{a^2}{\\sigma^2 + a^2}\\right) = 0$.<br>
2. Variance: $\\mathbb{E}[X^2] = a^2 p + b^2 (1-p) = a^2 \\frac{\\sigma^2}{\\sigma^2 + a^2} + \\frac{\\sigma^4}{a^2} \\frac{a^2}{\\sigma^2 + a^2} = \\sigma^2$.<br>
3. Tail probability: $\\mathbb{P}(X \\ge a) = \\mathbb{P}(X = a) = <span class=\"ans\">\\frac{\\sigma^2}{\\sigma^2 + a^2}</span>$.<br>
<span class=\"ans\">Exact equality holds, proving that Cantelli's bound cannot be improved without further distributional assumptions.</span></p>""",
        "takeaway": "Cantelli's one-sided Chebyshev bound $\\mathbb{P}(X \\ge a) \\le \\frac{\\sigma^2}{\\sigma^2 + a^2}$ holds for ANY distribution without requiring symmetry. The shifted-square technique $(X+u)^2$ with $u^* = \\sigma^2/a$ produces a provably tight bound."
    },
    {
        "id": 30693,
        "subject": "StoMA",
        "topicId": "06_Probability_Inequalities_Markov_Chebyshev_Chernoff",
        "topicTitle": "06 · Probability Inequalities",
        "title": "AM-GM Inequality via Jensen & Hoeffding Concentration (Generated Exam)",
        "kind2": "practice",
        "source": "Stanford Stats 116 / Berkeley EECS 126 Benchmark",
        "marks": "[10 Marks]",
        "question": """<p><span class="part">(a)</span> State <strong>Jensen's inequality</strong> for convex functions. Apply it to the strictly concave logarithm function $g(x) = \\ln x$ to prove the generalized <strong>Arithmetic-Geometric Mean (AM-GM) inequality</strong> for non-negative numbers $x_1, \\dots, x_n$ with weights $w_i \\ge 0$ ($\\sum_{i=1}^n w_i = 1$):
$$\\prod_{i=1}^n x_i^{w_i} \\le \\sum_{i=1}^n w_i x_i$$
State the exact condition for equality.</p>
<p><span class="part">(b)</span> State <strong>Hoeffding's inequality</strong> for bounded independent random variables. A fair coin is tossed $n = 100$ times. Compute Hoeffding's upper bound on the probability that the empirical proportion of heads $\\hat{p}_n = \\frac{1}{n} \\sum_{i=1}^n X_i$ deviates from $1/2$ by more than $\\epsilon = 0.1$.</p>""",
        "solution": """<p><span class="part">Part (a): AM-GM via Jensen's Inequality</span><br>
<strong>Jensen's Inequality:</strong> If $g: I \\to \\mathbb{R}$ is strictly concave and $X$ is a random variable supported on $I$, then $\\mathbb{E}[g(X)] \\le g(\\mathbb{E}[X])$, with equality if and only if $X$ is almost surely constant.<br>
Since $g(x) = \\ln x$ has second derivative $g''(x) = -1/x^2 < 0$ for all $x > 0$, the natural logarithm is strictly concave on $(0, \\infty)$.<br>
Define a discrete random variable $X$ taking value $x_i$ with probability $w_i = \\mathbb{P}(X = x_i)$.<br>
Then:
$$\\mathbb{E}[X] = \\sum_{i=1}^n w_i x_i$$
$$\\mathbb{E}[\\ln X] = \\sum_{i=1}^n w_i \\ln(x_i) = \\sum_{i=1}^n \\ln(x_i^{w_i}) = \\ln\\left( \\prod_{i=1}^n x_i^{w_i} \\right)$$
Applying Jensen's inequality:
$$\\ln\\left( \\prod_{i=1}^n x_i^{w_i} \\right) \\le \\ln\\left( \\sum_{i=1}^n w_i x_i \\right)$$
Since the exponential function is strictly increasing, exponentiating both sides preserves the inequality:
$$<span class=\"ans\">\\prod_{i=1}^n x_i^{w_i} \\le \\sum_{i=1}^n w_i x_i</span>$$
<span class=\"ans\">Equality holds if and only if $x_1 = x_2 = \\dots = x_n$</span> (the random variable $X$ is constant).</p>

<p><span class="part">Part (b): Hoeffding's Concentration Bound</span><br>
<strong>Hoeffding's Inequality:</strong> Let $X_1, \\dots, X_n$ be independent bounded random variables with $a_i \\le X_i \\le b_i$. Let $S_n = \\sum_{i=1}^n X_i$. For any $\\epsilon > 0$:
$$\\mathbb{P}(|\\bar{X}_n - \\mathbb{E}[\\bar{X}_n]| \\ge \\epsilon) \\le 2 \\exp\\left( -\\frac{2n^2 \\epsilon^2}{\\sum_{i=1}^n (b_i - a_i)^2} \\right)$$
For coin tosses, $X_i \\in \\{0, 1\\}$ so $b_i - a_i = 1 - 0 = 1$. The denominator is $\\sum_{i=1}^n 1 = n$.<br>
Thus:
$$\\mathbb{P}(|\\hat{p}_n - 0.5| \\ge \\epsilon) \\le 2 \\exp(-2n\\epsilon^2)$$
For $n = 100$ and $\\epsilon = 0.1$:
$$-2n\\epsilon^2 = -2(100)(0.1)^2 = -2(100)(0.01) = -2$$
Substituting:
$$\\mathbb{P}(|\\hat{p}_{100} - 0.5| \\ge 0.1) \\le 2 e^{-2} = \\frac{2}{e^2} \\approx <span class=\"ans\">0.27067 \\quad (27.07\\%)</span>$$
The probability that 100 tosses yield fewer than 40 or more than 60 heads is strictly at most $27.07\\%$.</p>""",
        "takeaway": "Jensen's inequality $\\mathbb{E}[g(X)] \\le g(\\mathbb{E}[X])$ for concave $g$ is the algebraic engine behind AM-GM and entropy bounds. Hoeffding's inequality provides non-asymptotic sub-Gaussian tail concentration $2e^{-2n\\epsilon^2}$ for bounded independent variables."
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
    for c in PRACTICE_STOMA_05_06:
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
