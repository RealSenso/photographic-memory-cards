#!/usr/bin/env python3
"""
Builder script for StoMA Practice Cards: Batch 13 (Topics 25 & 26)
Topic 25: Random Walk, Brownian Motion and Gaussian Processes (Cards 32591, 32592, 32593)
Topic 26: Martingales and Optional Stopping Theorem (Cards 32691, 32692, 32693)
"""

import json
import os
import re

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRACTICE_FILE = os.path.join(REPO_DIR, "practice_stoma.js")

PRACTICE_STOMA_25_26 = [
    # =========================================================================
    # TOPIC 25: Random Walk, Brownian Motion and Gaussian Processes
    # =========================================================================
    {
        "id": 32591,
        "subject": "StoMA",
        "topicId": "25_Random_Walk_Brownian_Motion_and_Gaussian_Processes",
        "topicTitle": "25 · Random Walk & Brownian Motion",
        "title": "Brownian Hitting Time & Reflection Principle (IISc Endsem / Stanford Math 236)",
        "kind2": "pyq",
        "source": "IISc Endsem / Stanford Math 236 Stochastic Analysis",
        "marks": "[8 Marks]",
        "question": """<p>Let $\{B(t), t \ge 0\}$ be a standard 1D Brownian motion ($B(0) = 0$). For threshold $a > 0$, define the first hitting time:
$$\\tau_a = \\inf\\{t \\ge 0 : B(t) = a\\}$$</p>
<p><span class="part">(a)</span> Using the <strong>Reflection Principle</strong>, show that $\\mathbb{P}(\\tau_a \\le t) = 2\\mathbb{P}(B(t) \\ge a)$ and derive the probability density function $f_{\\tau_a}(t)$ (the Lévy distribution).</p>
<p><span class="part">(b)</span> Prove that $\\mathbb{P}(\\tau_a < \\infty) = 1$, yet the expected hitting time is infinite: $\\mathbb{E}[\\tau_a] = \\infty$.</p>
<p><span class="part">(c)</span> Use the exponential martingale $M(t) = \\exp(\\theta B(t) - \\frac{\\theta^2}{2}t)$ to evaluate the Laplace transform $\\mathbb{E}[e^{-s \\tau_a}]$ for $s > 0$.</p>""",
        "solution": """<p><span class="part">Part (a): Reflection Principle & Lévy PDF</span><br>
Let $M(t) = \\max_{0 \\le s \\le t} B(s)$ be the running maximum. Notice that $\\{\\tau_a \\le t\\} \\iff \\{M(t) \\ge a\\}$.<br>
By the <strong>Reflection Principle</strong>: conditional on reaching $a$ at time $\\tau_a \\le t$, the path after $\\tau_a$ is equally likely to end up above $a$ or below $a$ at time $t$ by Brownian symmetry.
$$\\mathbb{P}(M(t) \\ge a) = 2 \\mathbb{P}(B(t) \\ge a) = 2\\left[1 - \\Phi\\left(\\frac{a}{\\sqrt{t}}\\right)\\right] = 2 \\int_{a/\\sqrt{t}}^\\infty \\frac{1}{\\sqrt{2\\pi}} e^{-u^2/2} du$$
Differentiating with respect to $t$ using the Leibniz rule:
$$f_{\\tau_a}(t) = \\frac{d}{dt} \\mathbb{P}(\\tau_a \\le t) = -2 \\frac{1}{\\sqrt{2\\pi}} e^{-(a/\\sqrt{t})^2 / 2} \\frac{d}{dt}\\left(\\frac{a}{\\sqrt{t}}\\right) = -\\sqrt{\\frac{2}{\\pi}} e^{-a^2/(2t)} \\left(-\\frac{a}{2 t^{3/2}}\\right)$$
<span class="ans">$$f_{\\tau_a}(t) = \\frac{a}{\\sqrt{2\\pi t^3}} \\exp\\left(-\\frac{a^2}{2t}\\right), \\quad t > 0 \\quad \\text{(Lévy Distribution)}$$</span></p>

<p><span class="part">Part (b): Certain Absorption but Infinite Mean</span><br>
1. <strong>Total probability:</strong>
$$\\mathbb{P}(\\tau_a < \\infty) = \\lim_{t \\to \\infty} \\mathbb{P}(\\tau_a \\le t) = \\lim_{t \\to \\infty} 2\\left[1 - \\Phi\\left(\\frac{a}{\\sqrt{t}}\\right)\\right] = 2[1 - \\Phi(0)] = 2\\left(1 - \\frac{1}{2}\\right) = <span class=\"ans\">1</span>$$
Brownian motion is recurrent in 1D; it is guaranteed to hit $a$ eventually with probability 1.<br>
2. <strong>Expected hitting time:</strong>
$$\\mathbb{E}[\\tau_a] = \\int_0^\\infty t f_{\\tau_a}(t) dt = \\int_0^\\infty \\frac{a}{\\sqrt{2\\pi t}} e^{-a^2/(2t)} dt$$
As $t \\to \\infty$, the integrand decays as $O(t^{-1/2})$, whose integral $\\int^\\infty t^{-1/2} dt = \\infty$ diverges.<br>
<span class=\"ans\">$$\\mathbb{E}[\\tau_a] = \\infty$$</span></p>

<p><span class="part">Part (c): Laplace Transform via Wald's Martingale</span><br>
For $\\theta > 0$, $M(t) = \\exp\\left(\\theta B(t) - \\frac{\\theta^2}{2}t\\right)$ is a martingale with $M(0) = 1$.<br>
Applying Optional Stopping Theorem at stopping time $\\tau_a$:
$$\\mathbb{E}[M(\\tau_a)] = \\mathbb{E}\\left[\\exp\\left(\\theta B(\\tau_a) - \\frac{\\theta^2}{2}\\tau_a\\right)\\right] = M(0) = 1$$
Since $B(\\tau_a) = a$ identically:
$$e^{\\theta a} \\mathbb{E}\\left[\\exp\\left(-\\frac{\\theta^2}{2}\\tau_a\\right)\\right] = 1 \\implies \\mathbb{E}\\left[e^{-\\frac{\\theta^2}{2}\\tau_a}\\right] = e^{-\\theta a}$$
Setting $s = \\theta^2 / 2 \\implies \\theta = \\sqrt{2s}$:
<span class="ans">$$\\mathbb{E}[e^{-s \\tau_a}] = \\exp(-a \\sqrt{2s})$$</span></p>""",
        "takeaway": "Brownian hitting time has the heavy-tailed Lévy density $f_{\\tau_a}(t) \\propto t^{-3/2} e^{-a^2/2t}$, guaranteeing almost sure absorption $\\mathbb{P}(\\tau_a < \\infty)=1$ with infinite expectation $\\mathbb{E}[\\tau_a]=\\infty$."
    },
    {
        "id": 32592,
        "subject": "StoMA",
        "topicId": "25_Random_Walk_Brownian_Motion_and_Gaussian_Processes",
        "topicTitle": "25 · Random Walk & Brownian Motion",
        "title": "Quadratic Variation of Brownian Motion (MIT 18.440 / Berkeley EECS 126)",
        "kind2": "university",
        "source": "MIT 18.440 / Berkeley EECS 126 Probability",
        "marks": "[8 Marks]",
        "question": """<p>Let $\\Pi_n = \\{0 = t_0 < t_1 < \\dots < t_n = t\\}$ be a deterministic sequence of partitions of $[0, t]$ whose mesh size $\\|\\Pi_n\\| = \\max_{1 \\le i \\le n} (t_i - t_{i-1}) \\to 0$ as $n \\to \\infty$. Define the sample quadratic variation:
$$V_2(\\Pi_n) = \\sum_{i=1}^n (B(t_i) - B(t_{i-1}))^2$$</p>
<p><span class="part">(a)</span> Compute $\\mathbb{E}[V_2(\\Pi_n)]$ and $\\operatorname{Var}(V_2(\\Pi_n))$.</p>
<p><span class="part">(b)</span> Prove that $V_2(\\Pi_n) \\xrightarrow{L^2} t$ in mean square as $\\|\\Pi_n\\| \\to 0$.</p>
<p><span class="part">(c)</span> What does this imply for the total variation $V_1([0, t])$ and differentiability of Brownian sample paths?</p>""",
        "solution": """<p><span class="part">Part (a): Mean and Variance of $V_2(\\Pi_n)$</span><br>
Let $\\Delta B_i = B(t_i) - B(t_{i-1})$ and $\\Delta t_i = t_i - t_{i-1}$.<br>
By independent Gaussian increments: $\\Delta B_i \\sim \\mathcal{N}(0, \\Delta t_i)$.
1. <strong>Expected Value:</strong>
$$\\mathbb{E}[(\\Delta B_i)^2] = \\operatorname{Var}(\\Delta B_i) = \\Delta t_i \\implies \\mathbb{E}[V_2(\\Pi_n)] = \\sum_{i=1}^n \\mathbb{E}[(\\Delta B_i)^2] = \\sum_{i=1}^n \\Delta t_i = <span class=\"ans\">t</span>$$
2. <strong>Variance:</strong> Because increments are independent, the squared increments $(\\Delta B_i)^2$ are mutually independent:
$$\\operatorname{Var}(V_2(\\Pi_n)) = \\sum_{i=1}^n \\operatorname{Var}\\left((\\Delta B_i)^2\\right)$$
For $Z \\sim \\mathcal{N}(0, \\sigma^2)$, $\\mathbb{E}[Z^4] = 3\\sigma^4$, so $\\operatorname{Var}(Z^2) = 3\\sigma^4 - (\\sigma^2)^2 = 2\\sigma^4 = 2(\\Delta t_i)^2$.
$$\\operatorname{Var}(V_2(\\Pi_n)) = \\sum_{i=1}^n 2(\\Delta t_i)^2 \\le 2\\|\\Pi_n\\| \\sum_{i=1}^n \\Delta t_i = <span class=\"ans\">2 \\|\\Pi_n\\| t</span>$$</p>

<p><span class="part">Part (b): Mean-Square Convergence $V_2(\\Pi_n) \\xrightarrow{L^2} t$</span><br>
The $L^2$ error is:
$$\\mathbb{E}[(V_2(\\Pi_n) - t)^2] = \\operatorname{Var}(V_2(\\Pi_n)) \\le 2 \\|\\Pi_n\\| t$$
As partition mesh $\\|\\Pi_n\\| \\to 0$:
<span class="ans">$$\\lim_{\\|\\Pi_n\\| \\to 0} \\mathbb{E}[(V_2(\\Pi_n) - t)^2] = 0 \\implies V_2(\\Pi_n) \\xrightarrow{L^2} t$$</span>
Symbolically, this establishes the foundational Itô calculus rule:
$$(dB(t))^2 = dt$$</p>

<p><span class="part">Part (c): Infinite Total Variation & Non-Differentiability</span><br>
Recall total variation $V_1(\\Pi_n) = \\sum_{i=1}^n |\\Delta B_i|$.
$$V_2(\\Pi_n) = \\sum_{i=1}^n |\\Delta B_i|^2 \\le \\left(\\max_{1 \\le i \\le n} |\\Delta B_i|\\right) \\sum_{i=1}^n |\\Delta B_i| = \\left(\\max_i |\\Delta B_i|\\right) V_1(\\Pi_n)$$
Since $B(t)$ is almost surely continuous, $\\max_i |\\Delta B_i| \\xrightarrow{a.s.} 0$.<br>
If $V_1([0, t])$ were finite, the product would tend to 0, which contradicts $V_2(\\Pi_n) \\to t > 0$.<br>
<span class=\"ans\">Therefore, $V_1([0, t]) = \\infty$ almost surely. Any function with infinite total variation cannot be of bounded variation and is nowhere differentiable almost surely.</span></p>""",
        "takeaway": "Brownian motion has deterministic quadratic variation $[B, B]_t = t$, which gives $(dB_t)^2 = dt$ in Itô calculus. A nonzero quadratic variation forces the total variation to be infinite, making Brownian sample paths nowhere differentiable."
    },
    {
        "id": 32593,
        "subject": "StoMA",
        "topicId": "25_Random_Walk_Brownian_Motion_and_Gaussian_Processes",
        "topicTitle": "25 · Random Walk & Brownian Motion",
        "title": "Gaussian Process Regression with RBF Kernel (Stanford CS229 / IISc AI Endsem)",
        "kind2": "generated",
        "source": "Stanford CS229 / IISc AI Endsem Machine Learning",
        "marks": "[8 Marks]",
        "question": """<p>Consider a zero-mean Gaussian Process prior $f(x) \\sim \\mathcal{GP}(0, k(x, x'))$ with squared-exponential (RBF) covariance kernel:
$$k(x, x') = \\exp\\left(-\\frac{(x - x')^2}{2}\\right)$$
We collect noisy scalar observations $y_i = f(x_i) + \\epsilon_i$ with i.i.d. Gaussian noise $\\epsilon_i \\sim \\mathcal{N}(0, \\sigma_n^2 = 0.1)$. Two training points are observed: $x_1 = 0$ with $y_1 = 1$, and $x_2 = 1$ with $y_2 = 2$.</p>
<p><span class="part">(a)</span> Compute the noisy training covariance matrix $K_y = K(X, X) + \\sigma_n^2 I$ and its inverse $K_y^{-1}$.</p>
<p><span class="part">(b)</span> Find the cross-covariance vector $\\mathbf{k}_*$ between test input $x_* = 0.5$ and training set $X$.</p>
<p><span class="part">(c)</span> Compute the posterior predictive mean $\\bar{f}_*$ and posterior predictive variance $\\operatorname{Var}(f_*)$ at $x_* = 0.5$.</p>""",
        "solution": """<p><span class="part">Part (a): Covariance Matrix $K_y$ and Inverse</span><br>
Evaluate kernel entries between training points $X = [0, 1]^\\top$:
- $k(0, 0) = e^0 = 1$
- $k(1, 1) = e^0 = 1$
- $k(0, 1) = k(1, 0) = \\exp\\left(-\\frac{(0 - 1)^2}{2}\\right) = e^{-0.5} \\approx 0.6065$
With observation noise $\\sigma_n^2 = 0.1$:
$$K_y = \\begin{pmatrix} 1 & 0.6065 \\\\ 0.6065 & 1 \\end{pmatrix} + \\begin{pmatrix} 0.1 & 0 \\\\ 0 & 0.1 \\end{pmatrix} = \\begin{pmatrix} 1.10 & 0.6065 \\\\ 0.6065 & 1.10 \\end{pmatrix}$$
Determinant: $\\det(K_y) = (1.10)^2 - (0.6065)^2 = 1.2100 - 0.3678 = 0.8422$.<br>
Matrix inverse:
<span class="ans">$$K_y^{-1} = \\frac{1}{0.8422} \\begin{pmatrix} 1.10 & -0.6065 \\\\ -0.6065 & 1.10 \\end{pmatrix} \\approx \\begin{pmatrix} 1.3061 & -0.7201 \\\\ -0.7201 & 1.3061 \\end{pmatrix}$$</span></p>

<p><span class="part">Part (b): Test Cross-Covariance Vector $\\mathbf{k}_*$</span><br>
At test location $x_* = 0.5$:
- $k(x_*, x_1) = k(0.5, 0) = \\exp\\left(-\\frac{(0.5 - 0)^2}{2}\\right) = e^{-0.125} \\approx 0.8825$
- $k(x_*, x_2) = k(0.5, 1) = \\exp\\left(-\\frac{(0.5 - 1)^2}{2}\\right) = e^{-0.125} \\approx 0.8825$
<span class="ans">$$\\mathbf{k}_* = \\begin{pmatrix} 0.8825 \\\\ 0.8825 \\end{pmatrix}$$</span>
Prior self-variance is $k(x_*, x_*) = e^0 = 1$.</p>

<p><span class="part">Part (c): Posterior Predictive Mean & Variance</span><br>
1. <strong>Predictive Mean $\\bar{f}_* = \\mathbf{k}_*^\\top K_y^{-1} \\mathbf{y}$:</strong>
$$\\mathbf{k}_*^\\top K_y^{-1} = \\begin{pmatrix} 0.8825 & 0.8825 \\end{pmatrix} \\begin{pmatrix} 1.3061 & -0.7201 \\\\ -0.7201 & 1.3061 \\end{pmatrix} = \\begin{pmatrix} 0.5171 & 0.5171 \\end{pmatrix}$$
Multiplying by targets $\\mathbf{y} = [1, 2]^\\top$:
<span class="ans">$$\\bar{f}_* = 0.5171 \\times 1 + 0.5171 \\times 2 = 0.5171 \\times 3 = 1.5513$$</span>
By symmetry, the predicted mean is exactly centered between $y_1 = 1$ and $y_2 = 2$.<br>
2. <strong>Predictive Variance $\\operatorname{Var}(f_*) = k(x_*, x_*) - \\mathbf{k}_*^\\top K_y^{-1} \\mathbf{k}_*$:</strong>
$$\\operatorname{Var}(f_*) = 1 - \\begin{pmatrix} 0.5171 & 0.5171 \\end{pmatrix} \\begin{pmatrix} 0.8825 \\\\ 0.8825 \\end{pmatrix} = 1 - 2(0.5171 \\times 0.8825) = 1 - 0.9127$$
<span class="ans">$$\\operatorname{Var}(f_*) = 0.0873 \\implies \\sigma_* = \\sqrt{0.0873} \\approx 0.2955$$</span>
Observing data at $x=0$ and $x=1$ reduced prior uncertainty from $1.0$ down to $0.0873$.</p>""",
        "takeaway": "GPR analytic posterior: $\\bar{f}_* = \\mathbf{k}_*^\\top (K+\\sigma_n^2 I)^{-1} \\mathbf{y}$ and $\\operatorname{Var}(f_*) = k(x_*, x_*) - \\mathbf{k}_*^\\top (K+\\sigma_n^2 I)^{-1} \\mathbf{k}_*$. Nearby observations exponentially contract posterior predictive variance."
    },

    # =========================================================================
    # TOPIC 26: Martingales and Optional Stopping Theorem
    # =========================================================================
    {
        "id": 32691,
        "subject": "StoMA",
        "topicId": "26_Martingales_and_Optional_Stopping_Theorem",
        "topicTitle": "26 · Martingales & Optional Stopping",
        "title": "Biased Gambler's Ruin via Optional Stopping Theorem (IISc Midterm / MIT 18.440)",
        "kind2": "pyq",
        "source": "IISc Midterm / MIT 18.440 Martingale Methods",
        "marks": "[8 Marks]",
        "question": """<p>Let $S_n = x_0 + \\sum_{i=1}^n X_i$, where $X_i \\in \\{-1, +1\\}$ are i.i.d. with $\\mathbb{P}(X_i = +1) = p$ and $\\mathbb{P}(X_i = -1) = q = 1 - p \\ne 1/2$. A gambler starts with initial fortune $x_0$ ($0 < x_0 < N$) and stops at:
$$\\tau = \\inf\\{n \\ge 0 : S_n = 0 \\text{ or } S_n = N\\}$$</p>
<p><span class="part">(a)</span> Prove that $M_n = (q/p)^{S_n}$ is a martingale with respect to natural filtration $\\mathcal{F}_n$.</p>
<p><span class="part">(b)</span> Check the conditions of <strong>Doob's Optional Stopping Theorem (OST)</strong> and compute the exact ruin probability $a_{x_0} = \\mathbb{P}(S_\\tau = 0)$.</p>
<p><span class="part">(c)</span> Use Wald's martingale $Y_n = S_n - n(p - q)$ and the OST to compute the expected duration $\\mathbb{E}[\\tau]$.</p>""",
        "solution": """<p><span class="part">Part (a): Martingale Verification</span><br>
Let $\\phi = q/p$. Then $M_{n+1} = \\phi^{S_n + X_{n+1}} = M_n \\phi^{X_{n+1}}$.
$$\\mathbb{E}[M_{n+1} \\mid \\mathcal{F}_n] = M_n \\mathbb{E}[\\phi^{X_{n+1}}] = M_n \\left[ p \\phi^{+1} + q \\phi^{-1} \\right] = M_n \\left[ p \\left(\\frac{q}{p}\\right) + q \\left(\\frac{p}{q}\\right) \\right] = M_n [q + p] = M_n$$
<span class="ans">Thus $\\mathbb{E}[M_{n+1} \\mid \\mathcal{F}_n] = M_n$, confirming $M_n = (q/p)^{S_n}$ is a martingale.</span></p>

<p><span class="part">Part (b): OST Application for Ruin Probability</span><br>
1. <strong>Boundedness condition:</strong> For all $n$, the stopped process satisfies $0 \\le S_{n \\wedge \\tau} \\le N$, so:
$$M_{n \\wedge \\tau} \\le \\max\\left(1, (q/p)^N\\right) < \\infty$$
Since the stopped martingale is uniformly bounded, Doob's OST applies:
$$\\mathbb{E}[M_\\tau] = \\mathbb{E}[M_0] = (q/p)^{x_0}$$
2. <strong>Evaluation at stopping time:</strong> $S_\\tau \\in \\{0, N\\}$:
$$\\mathbb{E}[M_\\tau] = a_{x_0} (q/p)^0 + (1 - a_{x_0}) (q/p)^N = a_{x_0} + (1 - a_{x_0}) (q/p)^N$$
Equating:
$$(q/p)^{x_0} = a_{x_0} [1 - (q/p)^N] + (q/p)^N$$
<span class="ans">$$a_{x_0} = \\frac{(q/p)^{x_0} - (q/p)^N}{1 - (q/p)^N}$$</span>
This reproduces the first-step difference equation solution instantaneously with zero algebra!</p>

<p><span class="part">Part (c): Expected Duration $\\mathbb{E}[\\tau]$ via Wald's Martingale</span><br>
Consider $Y_n = S_n - n(p - q)$.
$$\\mathbb{E}[Y_{n+1} - Y_n \\mid \\mathcal{F}_n] = \\mathbb{E}[X_{n+1} - (p - q)] = (p - q) - (p - q) = 0 \\implies Y_n \\text{ is a martingale}$$
By OST for Wald's equation: $\\mathbb{E}[Y_\\tau] = Y_0 = x_0$.
$$\\mathbb{E}[S_\\tau] - (p - q)\\mathbb{E}[\\tau] = x_0 \\implies \\mathbb{E}[\\tau] = \\frac{\\mathbb{E}[S_\\tau] - x_0}{p - q}$$
Evaluating $\\mathbb{E}[S_\\tau] = 0 \\cdot a_{x_0} + N \\cdot (1 - a_{x_0}) = N(1 - a_{x_0})$:
<span class="ans">$$\\mathbb{E}[\\tau] = \\frac{N(1 - a_{x_0}) - x_0}{p - q} = \\frac{x_0}{q - p} - \\frac{N(1 - a_{x_0})}{q - p}$$</span></p>""",
        "takeaway": "Doob's Optional Stopping Theorem $\\mathbb{E}[M_\\tau] = \\mathbb{E}[M_0]$ bypasses difference equations: exponential martingale $(q/p)^{S_n}$ yields absorption probabilities, while Wald's martingale $S_n - n\\mu$ yields expected stopping time."
    },
    {
        "id": 32692,
        "subject": "StoMA",
        "topicId": "26_Martingales_and_Optional_Stopping_Theorem",
        "topicTitle": "26 · Martingales & Optional Stopping",
        "title": "The ABRACADABRA Monkey Typing Problem (Stanford Stat 310A / IISc Endsem)",
        "kind2": "university",
        "source": "Stanford Stat 310A / IISc Endsem Advanced Probability",
        "marks": "[8 Marks]",
        "question": """<p>A monkey types letters independently and uniformly at random from a 26-letter alphabet $\{A, B, \\dots, Z\}$. Let $\\tau$ be the number of keystrokes until the monkey types the word $\\text{ABRACADABRA}$ (length 11) for the first time.</p>
<p><span class="part">(a)</span> Construct an unfair casino martingale argument to formalize the game.</p>
<p><span class="part">(b)</span> Identify all self-overlapping prefixes/suffixes of $\\text{ABRACADABRA}$.</p>
<p><span class="part">(c)</span> Apply Doob's Optional Stopping Theorem to determine the exact value of $\\mathbb{E}[\\tau]$.</p>""",
        "solution": """<p><span class="part">Part (a): Casino Martingale Construction</span><br>
Imagine an open casino where at each keystroke $n = 1, 2, \\dots$:
1. A new gambler enters and bets $\$1$ that keystroke $n$ is letter $A$. The game is fair: the probability is $1/26$, so if correct the casino pays $\$26$; else the gambler loses $\$1$.<br>
2. If winning $\$26$, the gambler bets the entire $\$26$ that keystroke $n+1$ is $B$, returning $\$26^2$ if correct.<br>
3. The gambler continues betting all accumulated wealth on successive letters of $\\text{ABRACADABRA}$ ($A, B, R, A, C, A, D, A, B, R, A$). If any letter fails, they lose everything and leave.<br>
Since every individual bet is fair, each gambler's net profit is a martingale. Hence the casino's net profit:
$$M_n = n - \\sum_{k=1}^n (\\text{wealth of gambler } k \\text{ after step } n)$$
is a zero-mean martingale with $M_0 = 0$.</p>

<p><span class="part">Part (b): Self-Overlapping Suffixes</span><br>
The word $\\text{ABRACADABRA}$ has length $L = 11$.<br>
At stopping time $\\tau$, the last 11 characters typed are precisely $\\text{ABRACADABRA}$.<br>
Which gamblers are still active and holding money at time $\\tau$?
- <strong>Gambler who started at $\\tau - 11 + 1$:</strong> Completed the entire word $\\text{ABRACADABRA}$ (length 11). Current wealth: <span class=\"ans\">$\$26^{11}$</span>.
- <strong>Gambler who started at $\\tau - 4 + 1$:</strong> Typed $\\text{ABRA}$ (length 4), which matches the first 4 letters of the target. Current wealth: <span class=\"ans\">$\$26^4$</span>.
- <strong>Gambler who started at $\\tau$:</strong> Typed $A$ (length 1), which matches the first letter of the target. Current wealth: <span class=\"ans\">$\$26^1$</span>.
- All other gamblers bet on letters that did not match the required sequence and left with $\$0$.</p>

<p><span class="part">Part (c): Expected Waiting Time $\\mathbb{E}[\\tau]$ via OST</span><br>
By Doob's Optional Stopping Theorem, $\\mathbb{E}[M_\\tau] = M_0 = 0$:
$$\\mathbb{E}[\\tau - (26^{11} + 26^4 + 26^1)] = 0$$
$$\\mathbb{E}[\\tau] = 26^{11} + 26^4 + 26^1$$
Evaluating powers of 26:
- $26^1 = 26$
- $26^4 = 456{,}976$
- $26^{11} = 3{,}670{,}344{,}486{,}987{,}424$
Summing:
$$\\mathbb{E}[\\tau] = 3{,}670{,}344{,}486{,}987{,}424 + 456{,}976 + 26 = <span class=\"ans\">3{,}670{,}344{,}486{,}994{,}426 \\text{ keystrokes}</span>$$
($\\approx 3.67 \\times 10^{15}$ keystrokes).</p>""",
        "takeaway": "Casino martingale for pattern matching: $\\mathbb{E}[\\tau] = \\sum_{k \\in \\text{overlaps}} |\\Sigma|^k$. Every non-trivial prefix that is also a suffix of the pattern contributes an extra $|\\Sigma|^k$ to the expected waiting time."
    },
    {
        "id": 32693,
        "subject": "StoMA",
        "topicId": "26_Martingales_and_Optional_Stopping_Theorem",
        "topicTitle": "26 · Martingales & Optional Stopping",
        "title": "Pólya Urn Martingale & Almost Sure Beta Convergence (Berkeley Stat 205 / IIT Madras)",
        "kind2": "generated",
        "source": "Berkeley Stat 205 / IIT Madras Advanced Probability",
        "marks": "[8 Marks]",
        "question": """<p>An urn initially contains $w$ white balls and $b$ black balls. At each discrete round $n = 1, 2, \\dots$, a ball is drawn uniformly at random, its color inspected, and it is returned to the urn along with $c$ additional balls of the same color. Let $W_n$ denote the number of white balls after $n$ rounds, and let:
$$X_n = \\frac{W_n}{w + b + n c}$$
denote the proportion of white balls in the urn.</p>
<p><span class="part">(a)</span> Prove that $\{X_n, n \\ge 0\}$ is a bounded martingale with respect to its natural filtration.</p>
<p><span class="part">(b)</span> Use <strong>Doob's Forward Martingale Convergence Theorem</strong> to prove that $X_n \\xrightarrow{a.s.} X_\\infty$ for some limiting random variable $X_\\infty \\in [0, 1]$.</p>
<p><span class="part">(c)</span> For the special symmetric case $w = 1, b = 1, c = 1$, find the exact distribution of $X_\\infty$.</p>""",
        "solution": """<p><span class="part">Part (a): Martingale Property</span><br>
Let $T_n = w + b + nc$ be the total ball count after $n$ draws. At step $n+1$:
- White ball drawn with probability $X_n = W_n / T_n \\implies W_{n+1} = W_n + c$.
- Black ball drawn with probability $1 - X_n \\implies W_{n+1} = W_n$.<br>
Conditional expectation of $W_{n+1}$:
$$\\mathbb{E}[W_{n+1} \\mid \\mathcal{F}_n] = (W_n + c) X_n + W_n (1 - X_n) = W_n + c X_n = W_n + c \\frac{W_n}{T_n} = W_n \\left(1 + \\frac{c}{T_n}\\right) = W_n \\frac{T_n + c}{T_n} = W_n \\frac{T_{n+1}}{T_n}$$
Dividing both sides by total count $T_{n+1}$:
$$\\mathbb{E}[X_{n+1} \\mid \\mathcal{F}_n] = \\frac{\\mathbb{E}[W_{n+1} \\mid \\mathcal{F}_n]}{T_{n+1}} = \\frac{W_n}{T_n} = X_n$$
<span class=\"ans\">Thus $\\mathbb{E}[X_{n+1} \\mid \\mathcal{F}_n] = X_n$. Since $0 \\le X_n \\le 1$ for all $n$, $\{X_n\}$ is a strictly bounded martingale.</span></p>

<p><span class="part">Part (b): Almost Sure Convergence via Doob's Theorem</span><br>
By <strong>Doob's Martingale Convergence Theorem</strong>: any martingale bounded in $L^1$ (here $\\sup_n \\mathbb{E}[|X_n|] \\le 1 < \\infty$) converges almost surely and in $L^1$:
<span class="ans">$$X_n \\xrightarrow{a.s.} X_\\infty \\quad \\text{and} \\quad X_n \\xrightarrow{L^1} X_\\infty$$</span>
where $X_\\infty$ is a random variable supported on $[0, 1]$ with $\\mathbb{E}[X_\\infty] = \\mathbb{E}[X_0] = \\frac{w}{w+b}$.</p>

<p><span class="part">Part (c): Distribution for $w = 1, b = 1, c = 1$</span><br>
When $w = 1, b = 1, c = 1$, total balls at step $n$ is $T_n = 2 + n$.<br>
By exchangeability of Pólya urn draws, any specific sequence containing $k$ white and $n - k$ black draws has identical probability $\\frac{1}{n+1}$.
$$\\mathbb{P}(W_n = 1 + k) = \\frac{1}{n+1}, \\quad k \\in \\{0, 1, \\dots, n\\}$$
Thus the proportion $X_n = \\frac{1 + k}{n + 2}$ is uniformly spread across $(0, 1)$.<br>
For any $x \\in (0, 1)$:
$$\\lim_{n \\to \\infty} \\mathbb{P}(X_n \\le x) = \\lim_{n \\to \\infty} \\frac{\\lfloor x(n+2) \\rfloor}{n+1} = x$$
<span class="ans">$$X_\\infty \\sim \\text{Uniform}(0, 1) = \\text{Beta}(1, 1)$$</span>
In the general case with parameters $w, b, c$, the limit is $X_\\infty \\sim \\text{Beta}\\left(\\frac{w}{c}, \\frac{b}{c}\\right)$.</p>""",
        "takeaway": "The Pólya urn white proportion $X_n = W_n / T_n$ is a bounded martingale converging almost surely to a $\\text{Beta}(w/c, b/c)$ random variable. Exchangeability makes standard $w=1, b=1, c=1$ draws converge to $\\text{Uniform}(0, 1)$."
    }
]

def main():
    with open(PRACTICE_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    if "32591" in content:
        print("Batch 25-26 already present in practice_stoma.js!")
        return

    m = re.search(r"window\.PRACTICE_DATA\.push\(\s*\[\s*(.*?)\s*\]\s*\);", content, re.DOTALL)
    if not m:
        print("Could not match window.PRACTICE_DATA.push pattern. Inspecting tail...")
        print(content[-300:])
        return

    existing_cards_text = m.group(1).rstrip()
    if existing_cards_text.endswith(","):
        existing_cards_text = existing_cards_text[:-1]

    new_cards_json = []
    for card in PRACTICE_STOMA_25_26:
        formatted = json.dumps(card, indent=4, ensure_ascii=False)
        new_cards_json.append(formatted)

    new_cards_str = ",\n".join(new_cards_json)
    
    if existing_cards_text:
        updated_cards_text = existing_cards_text + ",\n" + new_cards_str
    else:
        updated_cards_text = new_cards_str

    updated_content = f"window.PRACTICE_DATA = window.PRACTICE_DATA || [];\nwindow.PRACTICE_DATA.push([\n{updated_cards_text}\n]);\n"

    with open(PRACTICE_FILE, "w", encoding="utf-8") as f:
        f.write(updated_content)

    print("Successfully added Batch 25-26 (6 cards). Total in file now updated.")

if __name__ == "__main__":
    main()
