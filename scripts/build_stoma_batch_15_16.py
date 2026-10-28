#!/usr/bin/env python3
"""
build_stoma_batch_15_16.py
Generates 6 flippable practice cards for StoMA Topics 15 and 16:
  Topic 15: Modes of Convergence and Relations (3 cards)
  Topic 16: Borel-Cantelli Lemmas and Limsup/Liminf (3 cards)
"""

import os
import re
import json

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PRACTICE_STOMA_15_16 = [
    # =========================================================================
    # TOPIC 15: Modes of Convergence
    # =========================================================================
    {
        "id": 31591,
        "subject": "StoMA",
        "topicId": "15_Modes_of_Convergence_and_Relations",
        "topicTitle": "15 · Modes of Convergence",
        "title": "The Typewriter Sequence: Convergence in Probability vs Almost Surely (IISc Test 2)",
        "kind2": "pyq",
        "source": "IISc StoMA Test 2 2024 / Ross Ch 3",
        "marks": "[8 Marks]",
        "question": """<p>Construct the classic <strong>Typewriter Sequence</strong> of random variables on the probability space $\\Omega = [0, 1]$ equipped with the uniform Lebesgue measure.</p>
<p><span class="part">(a)</span> Rigorously prove that $X_n \\xrightarrow{\\mathbb{P}} 0$ (converges in probability to 0).</p>
<p><span class="part">(b)</span> Prove that $X_n \\not\\xrightarrow{a.s.} 0$ (does not converge almost surely). Show that for every outcome $\\omega \\in [0, 1]$, the numerical sequence $X_n(\\omega)$ oscillates endlessly between 0 and 1.</p>
<p><span class="part">(c)</span> What fundamental theorem guarantees that a subsequence $X_{n_k} \\xrightarrow{a.s.} 0$?</p>""",
        "solution": """<p><span class="part">Part (a): Typewriter Construction & Probability Convergence</span><br>
Let $\\Omega = [0, 1]$ with Lebesgue measure $\\mathbb{P}([a, b]) = b - a$.<br>
For each integer $k \\ge 1$, partition $[0, 1]$ into $k$ equal sub-intervals $I_{k, j} = \\left[ \\frac{j-1}{k}, \\frac{j}{k} \\right]$ for $j = 1, 2, \\dots, k$.<br>
Sequence the intervals by sliding across $[0, 1]$ for $k=1$, then $k=2$, and so forth:
$$I_1 = [0, 1], \\quad I_2 = [0, 1/2], \\; I_3 = [1/2, 1], \\quad I_4 = [0, 1/3], \\; I_5 = [1/3, 2/3], \\; I_6 = [2/3, 1], \\dots$$
Define $X_n(\\omega) = \\mathbf{1}_{I_n}(\\omega)$.<br>
For any $\\epsilon \\in (0, 1)$, $|X_n(\\omega)| > \\epsilon \\iff X_n(\\omega) = 1 \\iff \\omega \\in I_{k, j}$.<br>
The probability of deviation is the interval length:
$$\\mathbb{P}(|X_n| > \\epsilon) = \\mathbb{P}(X_n = 1) = \\lambda(I_{k, j}) = \\frac{1}{k}$$
As $n \\to \\infty$, the generation index $k \\to \\infty$. Therefore:
$$\\lim_{n \\to \\infty} \\mathbb{P}(|X_n| > \\epsilon) = \\lim_{k \\to \\infty} \\frac{1}{k} = 0 \\implies <span class=\"ans\">X_n \\xrightarrow{\\mathbb{P}} 0</span>$$</p>

<p><span class="part">Part (b): Failure of Almost Sure Convergence</span><br>
Fix any point $\\omega \\in [0, 1]$.<br>
In each generation $k \\in \\{1, 2, 3, \\dots\\}$, the intervals $I_{k, 1}, \\dots, I_{k, k}$ cover $[0, 1]$ completely.<br>
Therefore, in every generation $k$:
1. There exists an interval $I_{k, j}$ containing $\\omega$, so $X_n(\\omega) = 1$.<br>
2. For $k \\ge 2$, there exist $k - 1$ intervals that do not contain $\\omega$, where $X_n(\\omega) = 0$.<br>
As $n \\to \\infty$, the value $X_n(\\omega)$ visits 1 infinitely often, and visits 0 infinitely often:
$$\\limsup_{n \\to \\infty} X_n(\\omega) = 1, \\qquad \\liminf_{n \\to \\infty} X_n(\\omega) = 0$$
Since $\\lim_{n \\to \\infty} X_n(\\omega)$ does not exist for ANY point $\\omega \\in [0, 1]$:
$$\\mathbb{P}\\left( \\lim_{n \\to \\infty} X_n = 0 \\right) = <span class=\"ans\">0</span> \\ne 1 \\implies <span class=\"ans\">X_n \\not\\xrightarrow{a.s.} 0</span>$$</p>

<p><span class="part">Part (c): Subsequential Almost Sure Convergence</span><br>
<strong>Riesz's Subsequence Theorem:</strong> If $X_n \\xrightarrow{\\mathbb{P}} X$, then there exists a subsequence $\\{X_{n_k}\\}$ such that $X_{n_k} \\xrightarrow{a.s.} X$.<br>
For the typewriter sequence, selecting only the left-anchored intervals $X_{n_k} = \\mathbf{1}_{[0, 1/k^2]}$ yields:
$$\\sum_{k=1}^\\infty \\mathbb{P}(X_{n_k} = 1) = \\sum_{k=1}^\\infty \\frac{1}{k^2} = \\frac{\\pi^2}{6} < \\infty$$
By the First Borel-Cantelli Lemma, $X_{n_k} = 1$ only finitely many times a.s., ensuring <span class=\"ans\">$X_{n_k} \\xrightarrow{a.s.} 0$</span>.</p>""",
        "takeaway": "Convergence in probability controls the measure of bad events ($\\mathbb{P}(|X_n| > \\epsilon) \\to 0$), but allows that deviation to sweep continuously across all $\\omega \\in \\Omega$. Hence $X_n \\xrightarrow{\\mathbb{P}} 0 \\not\\implies X_n \\xrightarrow{a.s.} 0$."
    },
    {
        "id": 31592,
        "subject": "StoMA",
        "topicId": "15_Modes_of_Convergence_and_Relations",
        "topicTitle": "15 · Modes of Convergence",
        "title": "Convergence in Distribution to a Constant Implies Probability (Stanford Stats 116)",
        "kind2": "pyq",
        "source": "Stanford Stats 116 / Ross Ch 3",
        "marks": "[10 Marks]",
        "question": """<p><span class="part">(a)</span> State the definitions of <strong>convergence in distribution</strong> ($X_n \\xrightarrow{d} X$) and <strong>convergence in probability</strong> ($X_n \\xrightarrow{\\mathbb{P}} X$).</p>
<p><span class="part">(b)</span> Show that convergence in distribution does NOT imply convergence in probability for a general random variable $X$ by constructing a counterexample with a fair coin toss.</p>
<p><span class="part">(c)</span> Prove that if the limit is a <strong>deterministic constant</strong> $c \\in \\mathbb{R}$ ($X_n \\xrightarrow{d} c$), then convergence in distribution implies convergence in probability:
$$X_n \\xrightarrow{d} c \\implies X_n \\xrightarrow{\\mathbb{P}} c$$</p>""",
        "solution": """<p><span class="part">Part (a): Definitions</span><br>
- <strong>Convergence in Distribution:</strong> $X_n \\xrightarrow{d} X \\iff \\lim_{n \\to \\infty} F_{X_n}(x) = F_X(x)$ at every point $x$ where $F_X$ is continuous.<br>
- <strong>Convergence in Probability:</strong> $X_n \\xrightarrow{\\mathbb{P}} X \\iff \\forall \\epsilon > 0, \\; \\lim_{n \\to \\infty} \\mathbb{P}(|X_n - X| > \\epsilon) = 0$.</p>

<p><span class="part">Part (b): Counterexample for Non-Constant Limit</span><br>
Let $X \\sim \\text{Bernoulli}(1/2)$ with $\\mathbb{P}(X = 1) = \\mathbb{P}(X = 0) = 1/2$.<br>
Define $X_n = 1 - X$ for all $n \\ge 1$.<br>
1. <strong>Distribution:</strong> $\\mathbb{P}(X_n = 1) = \\mathbb{P}(X = 0) = 1/2$ and $\\mathbb{P}(X_n = 0) = 1/2$.<br>
Since $X_n$ and $X$ have identical distributions, $F_{X_n}(x) = F_X(x)$ for all $x$, so $X_n \\xrightarrow{d} X$.<br>
2. <strong>Probability Difference:</strong> For every outcome $\\omega$:
$$|X_n(\\omega) - X(\\omega)| = |(1 - X(\\omega)) - X(\\omega)| = |1 - 2X(\\omega)| = 1 \\quad \\text{almost surely}$$
For $\\epsilon = 0.5$:
$$\\mathbb{P}(|X_n - X| > 0.5) = 1 \\ne 0 \\implies <span class=\"ans\">X_n \\not\\xrightarrow{\\mathbb{P}} X</span>$$
Convergence in distribution only checks marginal laws, with zero regard for joint coupling.</p>

<p><span class="part">Part (c): Proof for Deterministic Constant Limit</span><br>
Let $c \\in \\mathbb{R}$ be constant. The degenerate distribution has CDF:
$$F_c(x) = \\begin{cases} 0 & x < c \\\\ 1 & x \\ge c \\end{cases}$$
The only discontinuity of $F_c$ is at $x = c$.<br>
For any $\\epsilon > 0$:
$$\\mathbb{P}(|X_n - c| \\ge \\epsilon) = \\mathbb{P}(X_n \\le c - \\epsilon) + \\mathbb{P}(X_n \\ge c + \\epsilon)$$
Since $\\mathbb{P}(X_n \\ge c + \\epsilon) \\le 1 - F_{X_n}(c + \\epsilon/2)$:
$$\\mathbb{P}(|X_n - c| \\ge \\epsilon) \\le F_{X_n}(c - \\epsilon) + \\left( 1 - F_{X_n}(c + \\epsilon/2) \\right)$$
Notice that $c - \\epsilon < c$ and $c + \\epsilon/2 > c$ are both <strong>points of continuity</strong> of $F_c$.<br>
Since $X_n \\xrightarrow{d} c$, taking limits on both terms:
$$\\lim_{n \\to \\infty} F_{X_n}(c - \\epsilon) = F_c(c - \\epsilon) = 0$$
$$\\lim_{n \\to \\infty} F_{X_n}(c + \\epsilon/2) = F_c(c + \\epsilon/2) = 1$$
Therefore:
$$\\lim_{n \\to \\infty} \\mathbb{P}(|X_n - c| \\ge \\epsilon) \\le 0 + (1 - 1) = 0$$
<span class=\"ans\">Hence $X_n \\xrightarrow{\\mathbb{P}} c$.</span> $\\blacksquare$</p>""",
        "takeaway": "Convergence in distribution checks marginal distributions without coupling: $X_n \\xrightarrow{d} X \\not\\implies X_n \\xrightarrow{\\mathbb{P}} X$. However, when the limit is a constant, the entire probability mass is squeezed into a single point, strictly forcing convergence in probability."
    },
    {
        "id": 31593,
        "subject": "StoMA",
        "topicId": "15_Modes_of_Convergence_and_Relations",
        "topicTitle": "15 · Modes of Convergence",
        "title": "Slutsky's Theorem & Studentized t-Ratio Normality (Generated Exam)",
        "kind2": "practice",
        "source": "Berkeley EECS 126 / MIT Benchmark",
        "marks": "[10 Marks]",
        "question": """<p><span class="part">(a)</span> State <strong>Slutsky's Theorem</strong> for combinations of sequences converging in distribution and probability.</p>
<p><span class="part">(b)</span> Let $X_1, \\dots, X_n$ be i.i.d. random variables with mean $\\mu$ and variance $\\sigma^2 > 0$. By the Central Limit Theorem, $\\sqrt{n}(\\bar{X}_n - \\mu) \\xrightarrow{d} \\mathcal{N}(0, \\sigma^2)$, and by the Law of Large Numbers, the sample standard deviation $S_n = \\sqrt{\\frac{1}{n-1}\\sum_{i=1}^n (X_i - \\bar{X}_n)^2} \\xrightarrow{\\mathbb{P}} \\sigma$.</p>
<p>Use Slutsky's theorem to prove that the studentized statistic converges to a standard normal distribution:
$$T_n = \\frac{\\sqrt{n}(\\bar{X}_n - \\mu)}{S_n} \\xrightarrow{d} \\mathcal{N}(0, 1)$$</p>
<p><span class="part">(c)</span> Why is Slutsky's theorem indispensable for real-world confidence intervals when the true variance $\\sigma^2$ is unknown?</p>""",
        "solution": """<p><span class="part">Part (a): Slutsky's Theorem</span><br>
Let $\\{Y_n\\}$ and $\\{Z_n\\}$ be sequences of random variables such that $Y_n \\xrightarrow{d} Y$ and $Z_n \\xrightarrow{\\mathbb{P}} c$, where $c$ is a deterministic constant. Then:
1. $Y_n + Z_n \\xrightarrow{d} Y + c$
2. $Y_n Z_n \\xrightarrow{d} c Y$
3. $\\frac{Y_n}{Z_n} \\xrightarrow{d} \\frac{Y}{c}$ (provided $c \\ne 0$).</p>

<p><span class="part">Part (b): Studentized Statistic Proof</span><br>
Identify the two components:
1. Numerator: $Y_n = \\sqrt{n}(\\bar{X}_n - \\mu)$. By the CLT, $Y_n \\xrightarrow{d} Y \\sim \\mathcal{N}(0, \\sigma^2)$.<br>
2. Denominator: $Z_n = S_n$. By consistency of sample variance, $S_n^2 \\xrightarrow{\\mathbb{P}} \\sigma^2$.<br>
By the Continuous Mapping Theorem on $g(t) = \\sqrt{t}$, $S_n = \\sqrt{S_n^2} \\xrightarrow{\\mathbb{P}} \\sqrt{\\sigma^2} = \\sigma$.<br>
Notice that $\\sigma > 0$ is a non-zero deterministic constant.<br>
Applying Slutsky's division rule:
$$T_n = \\frac{Y_n}{Z_n} = \\frac{\\sqrt{n}(\\bar{X}_n - \\mu)}{S_n} \\xrightarrow{d} \\frac{Y}{\\sigma}$$
Since $Y \\sim \\mathcal{N}(0, \\sigma^2)$, the linear scale property of Gaussian variables gives:
$$\\frac{Y}{\\sigma} \\sim \\mathcal{N}\\left( 0, \\frac{\\sigma^2}{\\sigma^2} \\right) = <span class=\"ans\">\\mathcal{N}(0, 1)</span>$$
<span class=\"ans\">Thus $T_n \\xrightarrow{d} \\mathcal{N}(0, 1)$.</span> $\\blacksquare$</p>

<p><span class="part">Part (c): Significance in Statistical Inference</span><br>
In practice, the true population variance $\\sigma^2$ is almost never known.<br>
Slutsky's theorem proves that substituting the sample estimate $S_n$ for the unknown $\\sigma$ introduces <strong>zero asymptotic error</strong>:
$$\\mathbb{P}\\left( -1.96 \\le \\frac{\\sqrt{n}(\\bar{X}_n - \\mu)}{S_n} \\le 1.96 \\right) \\to 95\\%$$
This validates the construction of large-sample confidence intervals $\\bar{X}_n \\pm 1.96 \\frac{S_n}{\\sqrt{n}}$ for arbitrary non-Gaussian populations without requiring knowledge of $\\sigma$.</p>""",
        "takeaway": "Slutsky's Theorem allows plugging in consistent parameter estimates $S_n \\xrightarrow{\\mathbb{P}} \\sigma$ into asymptotic distributional limits without distorting the target Gaussian limit: $\\frac{\\sqrt{n}(\\bar{X}_n-\\mu)}{S_n} \\xrightarrow{d} \\mathcal{N}(0, 1)$."
    },

    # =========================================================================
    # TOPIC 16: Borel-Cantelli Lemmas & Limsup/Liminf
    # =========================================================================
    {
        "id": 31691,
        "subject": "StoMA",
        "topicId": "16_Borel_Cantelli_Lemmas_and_Limsup_Liminf",
        "topicTitle": "16 · Borel-Cantelli Lemmas & Limsup/Liminf",
        "title": "Gaussian Extremes & First Borel-Cantelli Lemma (IISc Test 2)",
        "kind2": "pyq",
        "source": "IISc StoMA Test 2 2024 / Ross Ch 3",
        "marks": "[8 Marks]",
        "question": """<p>Let $X_1, X_2, \\dots$ be independent standard normal random variables ($\\mathcal{N}(0, 1)$).</p>
<p><span class="part">(a)</span> State the <strong>First Borel-Cantelli Lemma (BC1)</strong>. Does it require the events to be independent?</p>
<p><span class="part">(b)</span> Using Mill's ratio bound $\\mathbb{P}(X > x) \\le \\frac{1}{x\\sqrt{2\\pi}} e^{-x^2/2}$ for $x > 0$, prove that for any constant $c > 1$:
$$\\mathbb{P}\\left( X_n > c\\sqrt{2\\ln n} \\text{ infinitely often} \\right) = 0$$</p>
<p><span class="part">(c)</span> Deduce that $\\limsup_{n \\to \\infty} \\frac{X_n}{\\sqrt{2\\ln n}} \\le 1$ almost surely.</p>""",
        "solution": """<p><span class="part">Part (a): First Borel-Cantelli Lemma</span><br>
<strong>Theorem (BC1):</strong> Let $\\{A_n\\}_{n=1}^\\infty$ be any sequence of events on a probability space $(\\Omega, \\mathcal{F}, \\mathbb{P})$. If:
$$\\sum_{n=1}^\\infty \\mathbb{P}(A_n) < \\infty$$
then the probability that infinitely many $A_n$ occur is zero:
$$\\mathbb{P}(\\limsup_{n \\to \\infty} A_n) = \\mathbb{P}(A_n \\text{ infinitely often}) = 0$$
<span class=\"ans\">BC1 requires ZERO independence assumptions!</span> It holds unconditionally for arbitrary dependent events.</p>

<p><span class="part">Part (b): Application to Gaussian Tails</span><br>
Let $x_n = c\\sqrt{2\\ln n}$ where $c > 1$. Let $A_n = \\{ X_n > x_n \\}$.<br>
Using Mill's ratio bound:
$$\\mathbb{P}(A_n) \\le \\frac{1}{x_n \\sqrt{2\\pi}} e^{-x_n^2/2}$$
Evaluate the exponential factor:
$$-\\frac{x_n^2}{2} = -\\frac{c^2 (2\\ln n)}{2} = -c^2 \\ln n = \\ln(n^{-c^2}) \\implies e^{-x_n^2/2} = n^{-c^2}$$
Thus:
$$\\mathbb{P}(A_n) \\le \\frac{1}{c\\sqrt{4\\pi \\ln n}} \\frac{1}{n^{c^2}} \\le \\frac{C}{n^{c^2}}$$
Now sum the probabilities across all $n \\ge 2$:
$$\\sum_{n=2}^\\infty \\mathbb{P}(A_n) \\le C \\sum_{n=2}^\\infty \\frac{1}{n^{c^2}}$$
Because $c > 1$, the exponent is $c^2 > 1$. The $p$-series $\\sum_{n=2}^\\infty \\frac{1}{n^p}$ converges for $p > 1$!<br>
Applying BC1:
$$<span class=\"ans\">\\mathbb{P}(X_n > c\\sqrt{2\\ln n} \\text{ infinitely often}) = 0</span>$$</p>

<p><span class="part">Part (c): Limiting Supremum Bound</span><br>
By Part (b), with probability 1, the event $X_n > c\\sqrt{2\\ln n}$ occurs only for finitely many indices $n$.<br>
Therefore, for all sufficiently large $n$:
$$\\frac{X_n}{\\sqrt{2\\ln n}} \\le c \\quad \\text{almost surely} \\implies \\limsup_{n \\to \\infty} \\frac{X_n}{\\sqrt{2\\ln n}} \\le c \\quad \\text{a.s.}$$
Since this holds for every rational $c > 1$, taking the intersection over $c_k = 1 + 1/k$:
$$<span class=\"ans\">\\limsup_{n \\to \\infty} \\frac{X_n}{\\sqrt{2\\ln n}} \\le 1 \\quad \\text{almost surely}</span>$$
(By BC2, the limsup is also $\\ge 1$, so the limit is identically 1 a.s.).</p>""",
        "takeaway": "BC1 requires NO independence: $\\sum \\mathbb{P}(A_n) < \\infty \\implies \\mathbb{P}(A_n \\text{ i.o.}) = 0$. For independent standard Gaussians, tail probabilities decay as $n^{-c^2}$, proving the maximum grows as $\\sqrt{2\\ln n}$ almost surely."
    },
    {
        "id": 31692,
        "subject": "StoMA",
        "topicId": "16_Borel_Cantelli_Lemmas_and_Limsup_Liminf",
        "topicTitle": "16 · Borel-Cantelli Lemmas & Limsup/Liminf",
        "title": "Second Borel-Cantelli Lemma & The Infinite Monkey Theorem (Stanford Stats 116)",
        "kind2": "pyq",
        "source": "Stanford Stats 116 / Ross Ch 3",
        "marks": "[10 Marks]",
        "question": """<p><span class="part">(a)</span> State the <strong>Second Borel-Cantelli Lemma (BC2)</strong> and highlight the vital hypothesis that distinguishes it from BC1.</p>
<p><span class="part">(b)</span> Formulate and prove the <strong>Infinite Monkey Theorem</strong>: A monkey randomly and uniformly strikes keys on a keyboard with $m \\ge 2$ characters independently. Let $S$ be any specified target text (e.g. Hamlet) of length $L$ characters.</p>
<p>By defining non-overlapping disjoint blocks of length $L$, prove using BC2 that with probability 1, the target text $S$ will be typed <strong>infinitely many times</strong>.</p>""",
        "solution": """<p><span class="part">Part (a): Second Borel-Cantelli Lemma</span><br>
<strong>Theorem (BC2):</strong> Let $\\{E_n\\}_{n=1}^\\infty$ be a sequence of <strong>independent</strong> events on a probability space $(\\Omega, \\mathcal{F}, \\mathbb{P})$. If the sum of probabilities diverges:
$$\\sum_{n=1}^\\infty \\mathbb{P}(E_n) = \\infty$$
then the events occur infinitely often with probability 1:
$$\\mathbb{P}(\\limsup_{n \\to \\infty} E_n) = \\mathbb{P}(E_n \\text{ infinitely often}) = 1$$
<span class=\"ans\">The vital hypothesis is INDEPENDENCE: unlike BC1, BC2 is completely false without independence.</span></p>

<p><span class="part">Part (b): Proof of the Infinite Monkey Theorem</span><br>
Let $L$ be the length of text $S$ in characters. Partition the infinite sequence of keystrokes $k = 1, 2, 3, \\dots$ into disjoint consecutive blocks of length $L$:
- Block 1: Keystrokes $1$ through $L$
- Block 2: Keystrokes $L+1$ through $2L$
- Block $j$: Keystrokes $(j-1)L + 1$ through $jL$.<br>
Let $E_j$ be the event that the $j$-th block matches the target text $S$ exactly.<br>
1. <strong>Block Probability:</strong> Since each keystroke is independent and chosen uniformly from the alphabet of size $m$:
$$\\mathbb{P}(E_j) = \\left( \\frac{1}{m} \\right)^L = p > 0$$
Since $m$ and $L$ are finite, $p$ is a strictly positive constant.<br>
2. <strong>Block Independence:</strong> Because the blocks occupy non-overlapping sets of keystroke indices, the events $E_1, E_2, E_3, \\dots$ are <strong>mutually independent</strong>!<br>
3. <strong>Divergence of Probabilities:</strong> Sum the constant probabilities:
$$\\sum_{j=1}^\\infty \\mathbb{P}(E_j) = \\sum_{j=1}^\\infty p = p + p + p + \\dots = +\\infty$$
All hypotheses of the Second Borel-Cantelli Lemma are fully satisfied!<br>
Applying BC2:
$$<span class=\"ans\">\\mathbb{P}(E_j \\text{ infinitely often}) = 1</span>$$
<span class=\"ans\">With probability 1, the monkey will type the complete text $S$ infinitely many times.</span> $\\blacksquare$</p>""",
        "takeaway": "BC2 guarantees that any rare independent event with constant probability $p > 0$ will recur infinitely often: $\\sum p = \\infty \\implies \\mathbb{P}(E_n \\text{ i.o.}) = 1$. Partitioning time into disjoint blocks guarantees mutual independence."
    },
    {
        "id": 31693,
        "subject": "StoMA",
        "topicId": "16_Borel_Cantelli_Lemmas_and_Limsup_Liminf",
        "topicTitle": "16 · Borel-Cantelli Lemmas & Limsup/Liminf",
        "title": "Failure of BC2 under Dependence & Zero-One Laws (Generated Exam)",
        "kind2": "practice",
        "source": "Berkeley EECS 126 / MIT Benchmark",
        "marks": "[10 Marks]",
        "question": """<p><span class="part">(a)</span> Construct an explicit counterexample demonstrating that the <strong>Second Borel-Cantelli Lemma fails completely</strong> when the events are not independent: create a sequence $\\{A_n\\}$ such that $\\sum_{n=1}^\\infty \\mathbb{P}(A_n) = \\infty$, yet $\\mathbb{P}(A_n \\text{ i.o.}) = 0.3$.</p>
<p><span class="part">(b)</span> Prove that for independent events $\\{A_n\\}$, the probability of the tail event $\\mathbb{P}(A_n \\text{ i.o.})$ can ONLY take the values $0$ or $1$ (<strong>Kolmogorov's Zero-One Law</strong>).</p>""",
        "solution": """<p><span class="part">Part (a): Counterexample to BC2 without Independence</span><br>
Let the sample space be $\\Omega = [0, 1]$ equipped with the uniform Lebesgue probability measure $\\mathbb{P}([a, b]) = b - a$.<br>
Fix an event $E = [0, 0.3] \\subset \\Omega$, which has probability $\\mathbb{P}(E) = 0.3$.<br>
Define the sequence of events to be identical for all $n$:
$$A_n = E = [0, 0.3] \\quad \\forall n \\ge 1$$
1. <strong>Sum of Probabilities:</strong>
$$\\sum_{n=1}^\\infty \\mathbb{P}(A_n) = \\sum_{n=1}^\\infty 0.3 = 0.3 + 0.3 + 0.3 + \\dots = +\\infty$$
The sum diverges to infinity, satisfying the first condition of BC2.<br>
2. <strong>Infinitely Often Probability:</strong>
$$\\limsup_{n \\to \\infty} A_n = \\bigcap_{n=1}^\\infty \\bigcup_{k=n}^\\infty A_k = \\bigcap_{n=1}^\\infty E = E$$
Therefore:
$$\\mathbb{P}(A_n \\text{ i.o.}) = \\mathbb{P}(E) = <span class=\"ans\">0.3 \\ne 1</span>$$
<span class=\"ans\">Because the events are completely dependent ($A_n = A_1$), BC2 collapses completely: the probability is 0.3 instead of 1.</span></p>

<p><span class="part">Part (b): Kolmogorov's Zero-One Law Proof</span><br>
The event $A_\\infty = \\limsup_{n \\to \\infty} A_n = \\bigcap_{n=1}^\\infty \\bigcup_{k=n}^\\infty A_k$ is a <strong>tail event</strong> of the independent sequence $\\{A_n\\}_{n=1}^\\infty$.<br>
For any fixed integer $m \\ge 1$:
$$A_\\infty = \\bigcap_{n=m+1}^\\infty \\bigcup_{k=n}^\\infty A_k \\in \\sigma(A_{m+1}, A_{m+2}, \\dots)$$
Thus $A_\\infty$ depends purely on the events after index $m$, so $A_\\infty$ is statistically independent of the finite history $\\mathcal{F}_m = \\sigma(A_1, \\dots, A_m)$ for every $m \\ge 1$.<br>
Since this holds for every $m$, $A_\\infty$ is independent of the entire algebra $\\bigcup_{m=1}^\\infty \\mathcal{F}_m$, and hence independent of the generated $\\sigma$-algebra $\\sigma(A_1, A_2, \\dots)$.<br>
However, $A_\\infty$ is itself a member of $\\sigma(A_1, A_2, \\dots)$!<br>
Therefore, $A_\\infty$ is <strong>independent of itself</strong>:
$$\\mathbb{P}(A_\\infty \\cap A_\\infty) = \\mathbb{P}(A_\\infty) \\mathbb{P}(A_\\infty) \\implies \\mathbb{P}(A_\\infty) = [\\mathbb{P}(A_\\infty)]^2$$
Solving $p = p^2$:
$$p(1 - p) = 0 \\implies <span class=\"ans\">\\mathbb{P}(A_\\infty) = 0 \\quad \\text{or} \\quad \\mathbb{P}(A_\\infty) = 1</span>$$
<span class=\"ans\">No intermediate probabilities (like 0.3) can ever exist for independent events!</span></p>""",
        "takeaway": "Kolmogorov's Zero-One Law: any tail event $\\limsup A_n$ of an independent sequence is independent of itself, strictly forcing $\\mathbb{P}(\\limsup A_n) \\in \\{0, 1\\}$. Without independence, tail probabilities can be any value in $[0, 1]$ (e.g. $0.3$)."
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
    for c in PRACTICE_STOMA_15_16:
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
