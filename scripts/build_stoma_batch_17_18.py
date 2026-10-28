#!/usr/bin/env python3
"""
build_stoma_batch_17_18.py
Generates 6 flippable practice cards for StoMA Topics 17 and 18:
  Topic 17: Laws of Large Numbers (WLLN and SLLN) (3 cards)
  Topic 18: Characteristic Functions and Central Limit Theorem (3 cards)
"""

import os
import re
import json

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PRACTICE_STOMA_17_18 = [
    # =========================================================================
    # TOPIC 17: Laws of Large Numbers (WLLN & SLLN)
    # =========================================================================
    {
        "id": 31791,
        "subject": "StoMA",
        "topicId": "17_Laws_of_Large_Numbers_WLLN_and_SLLN",
        "topicTitle": "17 · Laws of Large Numbers (WLLN & SLLN)",
        "title": "Monte Carlo Integration & Strong Law of Large Numbers (IISc Test 2)",
        "kind2": "pyq",
        "source": "IISc StoMA Test 2 2024 / Ross Ch 3",
        "marks": "[8 Marks]",
        "question": """<p>Let $f: [0, 1] \\to \\mathbb{R}$ be a continuous function, and let $I = \\int_0^1 f(x) \\, dx$ be its definite integral. Let $U_1, U_2, \\dots$ be independent and identically distributed $\\text{Uniform}(0, 1)$ random variables.</p>
<p>Define the Monte Carlo estimator:
$$I_n = \\frac{1}{n} \\sum_{i=1}^n f(U_i)$$</p>
<p><span class="part">(a)</span> Using Kolmogorov's <strong>Strong Law of Large Numbers (SLLN)</strong>, prove that $I_n \\xrightarrow{a.s.} I$ (converges almost surely to the exact integral).</p>
<p><span class="part">(b)</span> Derive the variance $\\operatorname{Var}(I_n)$ and demonstrate the universal $O(1/\\sqrt{n})$ convergence rate of Monte Carlo estimation.</p>
<p><span class="part">(c)</span> Why is Monte Carlo integration vastly superior to classical grid-based numerical quadrature (trapezoidal rule) in high dimensions $d \\gg 1$?</p>""",
        "solution": """<p><span class="part">Part (a): Almost Sure Convergence via SLLN</span><br>
Let $Y_i = f(U_i)$. Because $U_1, U_2, \\dots$ are i.i.d. $\\text{Uniform}(0, 1)$, the transformed variables $Y_1, Y_2, \\dots$ are mutually independent and identically distributed.<br>
Compute the expectation using the Law of the Unconscious Statistician (LOTUS):
$$\\mathbb{E}[Y_i] = \\mathbb{E}[f(U_i)] = \\int_0^1 f(u) \\cdot 1 \\, du = I$$
Since $f$ is continuous on the compact interval $[0, 1]$, by the Extreme Value Theorem, $f$ is bounded: $|f(u)| \\le M < \\infty$ for all $u \\in [0, 1]$.<br>
Therefore, the first absolute moment is finite:
$$\\mathbb{E}[|Y_i|] \\le M < \\infty$$
By Kolmogorov's Strong Law of Large Numbers (SLLN), the sample average converges almost surely to the theoretical mean:
$$I_n = \\frac{1}{n} \\sum_{i=1}^n Y_i \\xrightarrow{a.s.} \\mathbb{E}[Y_1] = <span class=\"ans\">I</span>$$
<span class=\"ans\">The Monte Carlo estimate converges to the exact integral with probability 1.</span></p>

<p><span class="part">Part (b): Variance and $O(1/\\sqrt{n})$ Convergence Rate</span><br>
Let $\\sigma_f^2 = \\operatorname{Var}(f(U)) = \\int_0^1 (f(u) - I)^2 \\, du < \\infty$.<br>
Since the draws $U_i$ are independent:
$$\\operatorname{Var}(I_n) = \\operatorname{Var}\\left( \\frac{1}{n} \\sum_{i=1}^n Y_i \\right) = \\frac{1}{n^2} \\sum_{i=1}^n \\operatorname{Var}(Y_i) = \\frac{n \\sigma_f^2}{n^2} = <span class=\"ans\">\\frac{\\sigma_f^2}{n}</span>$$
The standard error of the estimator is:
$$\\text{SE}(I_n) = \\sqrt{\\operatorname{Var}(I_n)} = <span class=\"ans\">\\frac{\\sigma_f}{\\sqrt{n}} = O(n^{-1/2})</span>$$
To cut the estimation error in half, one must increase the sample size by a factor of 4.</p>

<p><span class="part">Part (c): High-Dimensional Advantage (Curse of Dimensionality)</span><br>
In dimension $d$:
- <strong>Deterministic Grid Quadrature:</strong> Evaluating on a grid with $k$ points per axis requires $N = k^d$ total points. The integration error scales as $O(k^{-2}) = O(N^{-2/d})$. For $d = 10$, the error is $O(N^{-0.2})$, which is catastrophically slow.<br>
- <strong>Monte Carlo Integration:</strong> The standard error remains strictly $\\frac{\\sigma_f}{\\sqrt{N}} = O(N^{-1/2})$ <strong>regardless of the dimension $d$</strong>!<br>
<span class=\"ans\">Monte Carlo integration breaks the Curse of Dimensionality: its convergence rate is completely immune to the dimensionality of the integration domain.</span></p>""",
        "takeaway": "Kolmogorov's SLLN guarantees almost sure convergence $I_n \\xrightarrow{a.s.} I$ for Monte Carlo integration. Its standard error $\\sigma_f/\\sqrt{n}$ is completely immune to the curse of dimensionality, converging at $O(n^{-1/2})$ in ANY dimension."
    },
    {
        "id": 31792,
        "subject": "StoMA",
        "topicId": "17_Laws_of_Large_Numbers_WLLN_and_SLLN",
        "topicTitle": "17 · Laws of Large Numbers (WLLN & SLLN)",
        "title": "WLLN vs SLLN: Cross-Sectional Probability vs Sample-Path Certainty (Stanford Stats 116)",
        "kind2": "pyq",
        "source": "Stanford Stats 116 / Ross Ch 3",
        "marks": "[10 Marks]",
        "question": """<p><span class="part">(a)</span> State the precise mathematical formulations of the <strong>Weak Law of Large Numbers (WLLN)</strong> and the <strong>Strong Law of Large Numbers (SLLN)</strong> for an i.i.d. sequence $X_1, X_2, \\dots$ with mean $\\mu$.</p>
<p><span class="part">(b)</span> Explain the fundamental conceptual difference between WLLN and SLLN in terms of <strong>sample paths</strong> (individual histories $\\omega \\in \\Omega$ over time) versus <strong>cross-sectional slices</strong> across parallel universes.</p>
<p><span class="part">(c)</span> What minimal moment conditions are required for each theorem (Khinchin vs Kolmogorov)?</p>""",
        "solution": """<p><span class="part">Part (a): Formal Statements</span><br>
Let $X_1, X_2, \\dots$ be i.i.d. random variables with mean $\\mu = \\mathbb{E}[X_i]$, and let $\\bar{X}_n = \\frac{1}{n}\\sum_{i=1}^n X_i$.<br>
- <strong>Weak Law of Large Numbers (WLLN):</strong> Convergence in probability:
$$\\lim_{n \\to \\infty} \\mathbb{P}(|\\bar{X}_n - \\mu| \\ge \\epsilon) = 0 \\quad \\forall \\epsilon > 0$$
- <strong>Strong Law of Large Numbers (SLLN):</strong> Almost sure convergence:
$$\\mathbb{P}\\left( \\lim_{n \\to \\infty} \\bar{X}_n = \\mu \\right) = 1 \\iff \\mathbb{P}(|\\bar{X}_n - \\mu| \\ge \\epsilon \\text{ infinitely often}) = 0$$</p>

<p><span class="part">Part (b): Sample Paths vs Cross-Sectional Geometry</span><br>
- <strong>WLLN (Cross-Sectional / Vertical View):</strong> Fix a very large time $n$. Look across the entire ensemble of all possible universes $\\Omega$. WLLN guarantees that the proportion of universes where $|\\bar{X}_n - \\mu| \\ge \\epsilon$ is vanishingly small. However, WLLN makes <strong>no guarantee about a single timeline over time</strong>: a given universe $\\omega$ could enter the error band at step $n$, leave it at step $n+1$, enter again at step $n+100$, and so forth, oscillating forever!<br>
- <strong>SLLN (Longitudinal / Horizontal Trajectory View):</strong> Pick a single universe $\\omega$ (with probability 1). Track its entire historical trajectory $n \\mapsto \\bar{X}_n(\\omega)$ as time marches to infinity. SLLN guarantees that there exists a finite random time $N_0(\\omega, \\epsilon)$ after which the trajectory enters the corridor $(\\mu - \\epsilon, \\mu + \\epsilon)$ and <strong>never leaves it again</strong>!<br>
<span class=\"ans\">SLLN guarantees that you can trust the long-term empirical average of a single physical experiment.</span></p>

<p><span class="part">Part (c): Minimal Moment Conditions</span><br>
- <strong>WLLN (Khinchin's Theorem):</strong> Requires only that the first moment exists: $\\mathbb{E}[|X|] < \\infty$. (Under finite variance $\\sigma^2 < \\infty$, it follows trivially from Chebyshev).<br>
- <strong>SLLN (Kolmogorov's Criterion):</strong> Kolmogorov proved that $\\mathbb{E}[|X|] < \\infty$ is both <strong>necessary and sufficient</strong> for $\\bar{X}_n \\xrightarrow{a.s.} \\mu$. If $\\mathbb{E}[|X|] = \\infty$ (as in Cauchy), SLLN completely fails.</p>""",
        "takeaway": "WLLN guarantees that at time $n$, almost all universes are close to $\\mu$. SLLN guarantees that a single timeline stays inside $(\\mu-\\epsilon, \\mu+\\epsilon)$ forever after finite time. SLLN eliminates infinite recurring excursions."
    },
    {
        "id": 31793,
        "subject": "StoMA",
        "topicId": "17_Laws_of_Large_Numbers_WLLN_and_SLLN",
        "topicTitle": "17 · Laws of Large Numbers (WLLN & SLLN)",
        "title": "Chebyshev Sample Complexity & WLLN Confidence Bounds (Generated Exam)",
        "kind2": "practice",
        "source": "Berkeley EECS 126 / MIT Benchmark",
        "marks": "[10 Marks]",
        "question": """<p>Let $X_1, X_2, \\dots$ be independent and identically distributed random variables with mean $\\mu$ and variance $\\sigma^2 > 0$. Let $\\bar{X}_n = \\frac{1}{n}\\sum_{i=1}^n X_i$ be the sample mean.</p>
<p><span class="part">(a)</span> Using Chebyshev's inequality, derive the classical non-asymptotic bound for the Weak Law of Large Numbers.</p>
<p><span class="part">(b)</span> Using Chebyshev's bound, determine how many samples $n$ are required to guarantee that the sample mean $\\bar{X}_n$ is within $0.1\\sigma$ of the true mean $\\mu$ with confidence at least $95\\%$ ($\\mathbb{P}(|\\bar{X}_n - \\mu| \\ge 0.1\\sigma) \\le 0.05$).</p>
<p><span class="part">(c)</span> Compare this sample size $n_{\\text{Chebyshev}}$ with the sample size $n_{\\text{CLT}}$ predicted by the asymptotic normal distribution via the Central Limit Theorem ($z_{0.025} \\approx 1.96$).</p>""",
        "solution": """<p><span class="part">Part (a): Chebyshev Proof of WLLN</span><br>
By linearity of expectation, $\\mathbb{E}[\\bar{X}_n] = \\mu$.<br>
Because the variables $X_i$ are pairwise independent, variances add:
$$\\operatorname{Var}(\\bar{X}_n) = \\operatorname{Var}\\left( \\frac{1}{n} \\sum_{i=1}^n X_i \\right) = \\frac{1}{n^2} \\sum_{i=1}^n \\operatorname{Var}(X_i) = \\frac{n\\sigma^2}{n^2} = \\frac{\\sigma^2}{n}$$
Applying Chebyshev's inequality to the random variable $\\bar{X}_n$:
$$\\mathbb{P}(|\\bar{X}_n - \\mu| \\ge \\epsilon) \\le \\frac{\\operatorname{Var}(\\bar{X}_n)}{\\epsilon^2} = <span class=\"ans\">\\frac{\\sigma^2}{n\\epsilon^2}</span>$$
For any fixed $\\epsilon > 0$, taking limits:
$$\\lim_{n \\to \\infty} \\mathbb{P}(|\\bar{X}_n - \\mu| \\ge \\epsilon) \\le \\lim_{n \\to \\infty} \\frac{\\sigma^2}{n\\epsilon^2} = 0 \\implies \\bar{X}_n \\xrightarrow{\\mathbb{P}} \\mu$$</p>

<p><span class="part">Part (b): Chebyshev Sample Size Calculation</span><br>
We require $\\mathbb{P}(|\\bar{X}_n - \\mu| \\ge \\epsilon) \\le \\delta$ with tolerance $\\epsilon = 0.1\\sigma$ and failure probability $\\delta = 0.05$ ($95\\%$ confidence).<br>
Substitute into Chebyshev's bound:
$$\\frac{\\sigma^2}{n\\epsilon^2} \\le \\delta \\implies \\frac{\\sigma^2}{n(0.1\\sigma)^2} \\le 0.05 \\implies \\frac{\\sigma^2}{n(0.01\\sigma^2)} \\le 0.05$$
$$\\frac{100}{n} \\le 0.05 \\implies n \\ge \\frac{100}{0.05} = <span class=\"ans\">2{,}000</span>$$
Chebyshev guarantees that $n \\ge 2{,}000$ samples are sufficient for ANY arbitrary probability distribution.</p>

<p><span class="part">Part (c): Central Limit Theorem Comparison</span><br>
By the CLT, the standardized sample mean converges to standard normal:
$$Z_n = \\frac{\\bar{X}_n - \\mu}{\\sigma/\\sqrt{n}} \\xrightarrow{d} \\mathcal{N}(0, 1)$$
The requirement $|\\bar{X}_n - \\mu| < 0.1\\sigma$ is equivalent to:
$$\\left| \\frac{\\bar{X}_n - \\mu}{\\sigma/\\sqrt{n}} \\right| < 0.1\\sqrt{n} \\implies |Z| < 0.1\\sqrt{n}$$
For $95\\%$ two-sided Gaussian confidence, the critical value is $z_{0.025} \\approx 1.96$:
$$0.1\\sqrt{n} \\ge 1.96 \\implies \\sqrt{n} \\ge 19.6 \\implies n \\ge (19.6)^2 = 384.16 \\implies <span class=\"ans\">n_{\\text{CLT}} \\approx 385</span>$$
<strong>Comparison:</strong>
- $n_{\\text{Chebyshev}} = 2{,}000$
- $n_{\\text{CLT}} = 385$<br>
<span class=\"ans\">Chebyshev is conservative by more than a factor of $5\\times$ ($2000 / 385 \\approx 5.2$) because it must protect against worst-case adversarial distributions, whereas the CLT exploits Gaussian tail decay.</span></p>""",
        "takeaway": "Chebyshev gives rigorous non-asymptotic guarantees for ANY distribution: $n \\ge \\frac{\\sigma^2}{\\epsilon^2 \\delta}$. Because it makes zero distributional assumptions, it requires $\\approx 5\\times$ more samples than the asymptotic Gaussian CLT ($n=2000$ vs $n=385$)."
    },

    # =========================================================================
    # TOPIC 18: Characteristic Functions & CLT
    # =========================================================================
    {
        "id": 31891,
        "subject": "StoMA",
        "topicId": "18_Characteristic_Functions_and_Central_Limit_Theorem",
        "topicTitle": "18 · Characteristic Functions & CLT",
        "title": "CLT with Continuity Correction for Binomial Sums (IISc Test 2)",
        "kind2": "pyq",
        "source": "IISc StoMA Test 2 2024 / Ross Ch 3",
        "marks": "[8 Marks]",
        "question": """<p>A fair coin is tossed $n = 10{,}000$ times. Let $S_{10000}$ denote the total number of heads obtained.</p>
<p><span class="part">(a)</span> Using the De Moivre-Laplace Central Limit Theorem with <strong>continuity correction</strong>, compute the approximate probability of obtaining between $4{,}950$ and $5{,}050$ heads inclusive:
$$\\mathbb{P}(4950 \\le S_{10000} \\le 5050)$$</p>
<p><span class="part">(b)</span> Why is continuity correction essential when approximating discrete lattice variables with a continuous normal distribution?</p>
<p><span class="part">(c)</span> Express the numerical answer using the standard normal cumulative distribution function $\\Phi(z)$ and evaluate it (given $\\Phi(1.01) \\approx 0.84375$).</p>""",
        "solution": """<p><span class="part">Part (a): Binomial Moments and Normal Approximation</span><br>
The number of heads follows $S \\sim \\text{Binomial}(n = 10{,}000, p = 0.5)$.<br>
- Mean: $\\mu = n p = 10{,}000(0.5) = 5{,}000$.<br>
- Variance: $\\sigma^2 = n p (1 - p) = 10{,}000(0.5)(0.5) = 2{,}500$.<br>
- Standard deviation: $\\sigma = \\sqrt{2{,}500} = 50$.</p>

<p><span class="part">Part (b): Principle of Continuity Correction</span><br>
The random variable $S$ is integer-valued (discrete). On a histogram, the integer value $k$ occupies the continuous interval $[k - 0.5, k + 0.5]$.<br>
Therefore, the inclusive event $\\{4950 \\le S \\le 5050\\}$ corresponds to the continuous integration interval:
$$[4950 - 0.5, \\; 5050 + 0.5] = [4949.5, \\; 5050.5]$$
Without continuity correction, the half-width of each boundary histogram bar ($0.5$) would be omitted, introducing a noticeable percentage error.</p>

<p><span class="part">Part (c): Numerical Evaluation</span><br>
Standardize the corrected continuous interval bounds:
$$z_1 = \\frac{4949.5 - 5000}{50} = \\frac{-50.5}{50} = -1.01$$
$$z_2 = \\frac{5050.5 - 5000}{50} = \\frac{+50.5}{50} = +1.01$$
By the Central Limit Theorem:
$$\\mathbb{P}(4950 \\le S \\le 5050) \\approx \\Phi(1.01) - \\Phi(-1.01) = 2\\Phi(1.01) - 1$$
Substituting $\\Phi(1.01) \\approx 0.84375$:
$$\\mathbb{P}(4950 \\le S \\le 5050) \\approx 2(0.84375) - 1 = 1.6875 - 1 = <span class=\"ans\">0.6875 \\quad (68.75\\%)</span>$$
<span class=\"ans\">There is approximately a $68.75\\%$ probability of obtaining between 4,950 and 5,050 heads.</span></p>""",
        "takeaway": "Continuity correction expands discrete integer boundaries by $0.5$ ($[k_1 - 0.5, k_2 + 0.5]$) to enclose full histogram bars. For $10{,}000$ coin tosses, $\\mathbb{P}(4950 \\le S \\le 5050) = 2\\Phi(1.01) - 1 \\approx 68.75\\%$."
    },
    {
        "id": 31892,
        "subject": "StoMA",
        "topicId": "18_Characteristic_Functions_and_Central_Limit_Theorem",
        "topicTitle": "18 · Characteristic Functions & CLT",
        "title": "Laplace Characteristic Function & Second-Order CLT Expansion (Stanford Stats 116)",
        "kind2": "pyq",
        "source": "Stanford Stats 116 / Ross Ch 3",
        "marks": "[10 Marks]",
        "question": """<p>Consider the symmetric Laplace (double exponential) distribution with density:
$$f_X(x) = \\frac{1}{2} e^{-|x|}, \\quad x \\in \\mathbb{R}$$</p>
<p><span class="part">(a)</span> Derive the characteristic function $\\phi_X(t) = \\mathbb{E}[e^{itX}]$ by evaluating the two-sided integral.</p>
<p><span class="part">(b)</span> Using the Taylor series expansion of $\\phi_X(t)$ around $t = 0$:
$$\\phi_X(t) = 1 + it\\mathbb{E}[X] - \\frac{t^2}{2}\\mathbb{E}[X^2] + o(t^2)$$
confirm that $\\mathbb{E}[X] = 0$ and $\\operatorname{Var}(X) = 2$.</p>
<p><span class="part">(c)</span> Let $S_n = \\sum_{k=1}^n X_k$ be the sum of $n$ independent Laplace variables. Prove directly using characteristic functions that $\\frac{S_n}{\\sqrt{2n}} \\xrightarrow{d} \\mathcal{N}(0, 1)$ (the Central Limit Theorem).</p>""",
        "solution": """<p><span class="part">Part (a): Characteristic Function Derivation</span><br>
By definition:
$$\\phi_X(t) = \\int_{-\\infty}^\\infty e^{itx} \\frac{1}{2} e^{-|x|} \\, dx = \\frac{1}{2} \\int_{-\\infty}^0 e^{x(1 + it)} \\, dx + \\frac{1}{2} \\int_0^\\infty e^{-x(1 - it)} \\, dx$$
Evaluate the two improper integrals:
$$\\int_{-\\infty}^0 e^{x(1 + it)} \\, dx = \\left[ \\frac{e^{x(1 + it)}}{1 + it} \\right]_{-\\infty}^0 = \\frac{1}{1 + it}$$
$$\\int_0^\\infty e^{-x(1 - it)} \\, dx = \\left[ -\\frac{e^{-x(1 - it)}}{1 - it} \\right]_0^\\infty = \\frac{1}{1 - it}$$
Adding the two halves:
$$\\phi_X(t) = \\frac{1}{2} \\left( \\frac{1}{1 + it} + \\frac{1}{1 - it} \\right) = \\frac{1}{2} \\left( \\frac{(1 - it) + (1 + it)}{(1 + it)(1 - it)} \\right) = \\frac{1}{2} \\left( \\frac{2}{1 - (it)^2} \\right) = <span class=\"ans\">\\frac{1}{1 + t^2}</span>$$</p>

<p><span class="part">Part (b): Taylor Expansion and Moments</span><br>
Expand $\\phi_X(t) = \\frac{1}{1 + t^2}$ using the geometric series $\\frac{1}{1 + u} = 1 - u + u^2 - \\dots$ with $u = t^2$:
$$\\phi_X(t) = 1 - t^2 + t^4 - t^6 + \\dots$$
Compare with the general moment expansion:
$$\\phi_X(t) = 1 + it\\mathbb{E}[X] - \\frac{t^2}{2}\\mathbb{E}[X^2] - i\\frac{t^3}{6}\\mathbb{E}[X^3] + \\frac{t^4}{24}\\mathbb{E}[X^4] - \\dots$$
- Linear term: $it \\mathbb{E}[X] = 0 \\implies \\mathbb{E}[X] = <span class=\"ans\">0</span>$.<br>
- Quadratic term: $-\\frac{t^2}{2}\\mathbb{E}[X^2] = -t^2 \\implies \\mathbb{E}[X^2] = <span class=\"ans\">2</span>$.<br>
Thus $\\operatorname{Var}(X) = \\mathbb{E}[X^2] - (\\mathbb{E}[X])^2 = 2 - 0 = <span class=\"ans\">2</span>$.</p>

<p><span class="part">Part (c): Proof of Central Limit Theorem</span><br>
Let $Z_n = \\frac{S_n}{\\sqrt{2n}} = \\sum_{k=1}^n \\frac{X_k}{\\sqrt{2n}}$.<br>
Since the $X_k$ are independent:
$$\\phi_{Z_n}(t) = \\left[ \\phi_X\\left( \\frac{t}{\\sqrt{2n}} \\right) \\right]^n = \\left[ \\frac{1}{1 + \\left(\\frac{t}{\\sqrt{2n}}\\right)^2} \\right]^n = \\left( 1 + \\frac{t^2}{2n} \\right)^{-n}$$
Take the limit as $n \\to \\infty$:
$$\\lim_{n \\to \\infty} \\phi_{Z_n}(t) = \\lim_{n \\to \\infty} \\left( 1 + \\frac{t^2/2}{n} \\right)^{-n} = <span class=\"ans\">e^{-t^2/2}</span>$$
Notice that $e^{-t^2/2}$ is uniquely the characteristic function of the standard normal distribution $\\mathcal{N}(0, 1)$.<br>
By <strong>Lévy's Continuity Theorem</strong>, pointwise convergence of characteristic functions to a continuous function implies convergence in distribution:
$$<span class=\"ans\">Z_n = \\frac{S_n}{\\sqrt{2n}} \\xrightarrow{d} \\mathcal{N}(0, 1)</span>$$</p>""",
        "takeaway": "Lévy's Continuity Theorem proves CLT directly: $[1 - \\frac{\\sigma^2 t^2}{2n} + o(1/n)]^n \\to e^{-\\sigma^2 t^2/2}$. For Laplace variables, $\\phi_X(t) = \\frac{1}{1+t^2} \\approx 1 - t^2$, proving convergence to $\\mathcal{N}(0, 1)$."
    },
    {
        "id": 31893,
        "subject": "StoMA",
        "topicId": "18_Characteristic_Functions_and_Central_Limit_Theorem",
        "topicTitle": "18 · Characteristic Functions & CLT",
        "title": "The Delta Method & Variance-Stabilizing Transformation (Generated Exam)",
        "kind2": "practice",
        "source": "Berkeley EECS 126 / MIT Benchmark",
        "marks": "[10 Marks]",
        "question": """<p><span class="part">(a)</span> State and prove the <strong>Delta Method</strong>: If $\\sqrt{n}(\\bar{X}_n - \\mu) \\xrightarrow{d} \\mathcal{N}(0, \\sigma^2)$ and $g: \\mathbb{R} \\to \\mathbb{R}$ is continuously differentiable at $\\mu$ with $g'(\\mu) \\ne 0$, then:
$$\\sqrt{n}(g(\\bar{X}_n) - g(\\mu)) \\xrightarrow{d} \\mathcal{N}\\left(0, \\, [g'(\\mu)]^2 \\sigma^2\\right)$$</p>
<p><span class="part">(b)</span> Let $X_1, \\dots, X_n \\sim \\text{i.i.d. Poisson}(\\lambda)$. Find the asymptotic normal distribution of the transformed estimator $g(\\bar{X}_n) = \\sqrt{\\bar{X}_n}$.</p>
<p><span class="part">(c)</span> Explain why $g(x) = \\sqrt{x}$ is called a <strong>variance-stabilizing transformation</strong> for Poisson data.</p>""",
        "solution": """<p><span class="part">Part (a): Proof of the Delta Method</span><br>
By Taylor's Theorem with remainder for $g$ around $\\mu$:
$$g(\\bar{X}_n) = g(\\mu) + g'(\\mu)(\\bar{X}_n - \\mu) + R_n$$
where the remainder satisfies $\\frac{R_n}{\\bar{X}_n - \\mu} \\xrightarrow{\\mathbb{P}} 0$ as $\\bar{X}_n \\xrightarrow{\\mathbb{P}} \\mu$.<br>
Multiply both sides by $\\sqrt{n}$:
$$\\sqrt{n}(g(\\bar{X}_n) - g(\\mu)) = g'(\\mu) \\sqrt{n}(\\bar{X}_n - \\mu) + \\sqrt{n} R_n$$
Write $\\sqrt{n} R_n = \\left( \\frac{R_n}{\\bar{X}_n - \\mu} \\right) \\sqrt{n}(\\bar{X}_n - \\mu)$.<br>
Since $\\frac{R_n}{\\bar{X}_n - \\mu} \\xrightarrow{\\mathbb{P}} 0$ and $\\sqrt{n}(\\bar{X}_n - \\mu) \\xrightarrow{d} \\mathcal{N}(0, \\sigma^2)$, by Slutsky's theorem:
$$\\sqrt{n} R_n \\xrightarrow{\\mathbb{P}} 0 \\cdot \\mathcal{N}(0, \\sigma^2) = 0$$
Applying Slutsky's theorem to the linear term:
$$\\sqrt{n}(g(\\bar{X}_n) - g(\\mu)) \\xrightarrow{d} g'(\\mu) \\mathcal{N}(0, \\sigma^2) = <span class=\"ans\">\\mathcal{N}\\left(0, \\, [g'(\\mu)]^2 \\sigma^2\\right)</span>$$</p>

<p><span class="part">Part (b): Application to Poisson Distribution</span><br>
For $X \\sim \\text{Poisson}(\\lambda)$: $\\mu = \\lambda$ and $\\sigma^2 = \\operatorname{Var}(X) = \\lambda$.<br>
Let $g(x) = \\sqrt{x}$. Differentiating:
$$g'(x) = \\frac{1}{2\\sqrt{x}} \\implies g'(\\mu) = \\frac{1}{2\\sqrt{\\lambda}}$$
Compute the asymptotic variance:
$$\\sigma_{\\text{asymp}}^2 = [g'(\\mu)]^2 \\sigma^2 = \\left( \\frac{1}{2\\sqrt{\\lambda}} \\right)^2 \\lambda = \\frac{1}{4\\lambda} \\cdot \\lambda = <span class=\"ans\">\\frac{1}{4}</span>$$
Therefore, by the Delta Method:
$$<span class=\"ans\">\\sqrt{n}(\\sqrt{\\bar{X}_n} - \\sqrt{\\lambda}) \\xrightarrow{d} \\mathcal{N}\\left( 0, \\; \\frac{1}{4} \\right)</span>$$</p>

<p><span class="part">Part (c): Concept of Variance Stabilization</span><br>
For raw Poisson data, the variance $\\operatorname{Var}(\\bar{X}_n) = \\frac{\\lambda}{n}$ depends on the unknown mean $\\lambda$ (heteroscedasticity). In contrast, the asymptotic variance of $\\sqrt{\\bar{X}_n}$ is the constant $\\frac{1}{4n}$, <strong>completely independent of $\\lambda$</strong>!<br>
This allows building universal $95\\%$ confidence intervals:
$$\\sqrt{\\bar{X}_n} \\pm 1.96 \\sqrt{\\frac{1}{4n}} = \\sqrt{\\bar{X}_n} \\pm \\frac{0.98}{\\sqrt{n}}$$
without having to plug in an estimate of $\\lambda$ to estimate the standard error.</p>""",
        "takeaway": "The Delta Method propagates CLT through smooth functions: asymptotic variance is multiplied by $[g'(\\mu)]^2$. For Poisson data, $g(x)=\\sqrt{x}$ cancels $\\lambda$, stabilizing variance to the parameter-free constant $1/4$."
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
    for c in PRACTICE_STOMA_17_18:
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
