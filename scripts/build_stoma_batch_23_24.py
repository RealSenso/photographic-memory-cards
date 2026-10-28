#!/usr/bin/env python3
"""
Builder script for StoMA Practice Cards: Batch 12 (Topics 23 & 24)
Topic 23: Random Processes, Stationarity and Ergodicity (Cards 32391, 32392, 32393)
Topic 24: Poisson Processes, Properties and Extensions (Cards 32491, 32492, 32493)
"""

import json
import os
import re

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRACTICE_FILE = os.path.join(REPO_DIR, "practice_stoma.js")

PRACTICE_STOMA_23_24 = [
    # =========================================================================
    # TOPIC 23: Random Processes, Stationarity and Ergodicity
    # =========================================================================
    {
        "id": 32391,
        "subject": "StoMA",
        "topicId": "23_Random_Processes_Stationarity_and_Ergodicity",
        "topicTitle": "23 · Random Processes & Wide-Sense Stationarity",
        "title": "Harmonic Process Stationarity & Random Phase (IISc Midterm / Stanford EE 278)",
        "kind2": "pyq",
        "source": "IISc Midterm / Stanford EE 278 Stochastic Systems",
        "marks": "[8 Marks]",
        "question": """<p>Consider the continuous-time random process:
$$X(t) = A \\cos(\\omega_0 t + \\Theta)$$
where $\\omega_0$ is a fixed nonzero constant, $A$ is a random variable with mean $\\mu_A$ and finite second moment $\\mathbb{E}[A^2] = \\sigma_A^2 + \\mu_A^2$, and $\\Theta \\sim \\text{Uniform}[-\\pi, \\pi]$ is independent of $A$.</p>
<p><span class="part">(a)</span> Determine whether $X(t)$ is Wide-Sense Stationary (WSS). Compute its mean $\\mathbb{E}[X(t)]$ and autocorrelation function $R_X(\\tau)$.</p>
<p><span class="part">(b)</span> Find the Power Spectral Density (PSD) $S_X(\\omega)$ using the Wiener-Khinchin theorem.</p>
<p><span class="part">(c)</span> Suppose instead that $\\Theta \\sim \\text{Uniform}[0, \\pi/2]$. Is the process still WSS? Justify.</p>""",
        "solution": """<p><span class="part">Part (a): Mean and Autocorrelation (WSS Check)</span><br>
1. <strong>Mean function:</strong> By independence of $A$ and $\\Theta$:
$$\\mathbb{E}[X(t)] = \\mathbb{E}[A] \\mathbb{E}[\\cos(\\omega_0 t + \\Theta)] = \\mu_A \\left[ \\frac{1}{2\\pi} \\int_{-\\pi}^\\pi \\cos(\\omega_0 t + \\theta) d\\theta \\right] = \\mu_A \\cdot 0 = <span class=\"ans\">0</span>$$
The mean is constant for all $t$.<br>
2. <strong>Autocorrelation function:</strong>
$$R_X(t, t+\\tau) = \\mathbb{E}[X(t)X(t+\\tau)] = \\mathbb{E}[A^2] \\mathbb{E}\\left[\\cos(\\omega_0 t + \\Theta) \\cos(\\omega_0(t+\\tau) + \\Theta)\\right]$$
Using trigonometric identity $\\cos(\\alpha)\\cos(\\beta) = \\frac{1}{2}[\\cos(\\beta - \\alpha) + \\cos(\\alpha + \\beta)]$:
$$R_X(t, t+\\tau) = \\frac{\\mathbb{E}[A^2]}{2} \\left[ \\cos(\\omega_0 \\tau) + \\mathbb{E}[\\cos(2\\omega_0 t + \\omega_0 \\tau + 2\\Theta)] \\right]$$
Because $\\Theta \\sim \\text{Uniform}[-\\pi, \\pi]$, $2\\Theta$ covers a full $4\\pi$ interval uniformly, so $\\mathbb{E}[\\cos(2\\omega_0 t + \\omega_0 \\tau + 2\\Theta)] = 0$.<br>
Thus:
<span class="ans">$$R_X(\\tau) = \\frac{\\mathbb{E}[A^2]}{2} \\cos(\\omega_0 \\tau)$$</span>
Since the mean is constant and $R_X(t, t+\\tau)$ depends only on the lag $\\tau$, <span class="ans">$X(t)$ is strictly Wide-Sense Stationary (WSS)</span>.</p>

<p><span class="part">Part (b): Power Spectral Density $S_X(\\omega)$</span><br>
By the Wiener-Khinchin theorem, $S_X(\\omega) = \\mathcal{F}\\{R_X(\\tau)\\}$:
$$\\mathcal{F}\\{\\cos(\\omega_0 \\tau)\\} = \\pi [\\delta(\\omega - \\omega_0) + \\delta(\\omega + \\omega_0)]$$
Therefore:
<span class="ans">$$S_X(\\omega) = \\frac{\\pi \\mathbb{E}[A^2]}{2} \\left[ \\delta(\\omega - \\omega_0) + \\delta(\\omega + \\omega_0) \\right]$$</span>
Total average power is $\\frac{1}{2\\pi}\\int_{-\\infty}^\\infty S_X(\\omega) d\\omega = R_X(0) = \\frac{\\mathbb{E}[A^2]}{2}$.</p>

<p><span class="part">Part (c): Non-uniform Phase $\\Theta \\sim \\text{Uniform}[0, \\pi/2]$</span><br>
If $\\Theta \\sim \\text{Uniform}[0, \\pi/2]$:
$$\\mathbb{E}[\\cos(2\\omega_0 t + \\omega_0 \\tau + 2\\Theta)] = \\frac{2}{\\pi} \\int_0^{\\pi/2} \\cos(2\\omega_0 t + \\omega_0 \\tau + 2\\theta) d\\theta = -\\frac{2}{\\pi} \\sin(2\\omega_0 t + \\omega_0 \\tau) \\ne 0$$
This term explicitly depends on absolute time $t$.<br>
<span class="ans">Therefore, when $\\Theta \\not\\sim \\text{Uniform}[-\\pi, \\pi]$, $R_X(t, t+\\tau)$ is not time-shift invariant, and the process is NOT WSS.</span></p>""",
        "takeaway": "A single cosine carrier $A \\cos(\\omega_0 t + \\Theta)$ is WSS if and only if phase $\\Theta \\sim \\text{Uniform}[-\\pi, \\pi]$. Uniform random phase cancels out time dependence in the second-order cross product."
    },
    {
        "id": 32392,
        "subject": "StoMA",
        "topicId": "23_Random_Processes_Stationarity_and_Ergodicity",
        "topicTitle": "23 · Random Processes & Wide-Sense Stationarity",
        "title": "White Gaussian Noise Through RC Low-Pass Filter (IIT Madras / MIT 6.011)",
        "kind2": "university",
        "source": "IIT Madras / MIT 6.011 Signals and Systems",
        "marks": "[8 Marks]",
        "question": """<p>Zero-mean white Gaussian noise $W(t)$ with continuous-time autocorrelation function $R_W(\\tau) = \\frac{N_0}{2} \\delta(\\tau)$ (flat two-sided PSD $S_W(\\omega) = \\frac{N_0}{2}$) is passed through an analog RC low-pass filter with transfer function:
$$H(\\omega) = \\frac{1}{1 + j\\omega RC}$$</p>
<p><span class="part">(a)</span> Compute the Power Spectral Density $S_Y(\\omega)$ of the output process $Y(t)$.</p>
<p><span class="part">(b)</span> Using the inverse Fourier transform, derive the output autocorrelation function $R_Y(\\tau)$.</p>
<p><span class="part">(c)</span> Calculate the total output average noise power $\\mathbb{E}[Y^2(t)]$.</p>""",
        "solution": """<p><span class="part">Part (a): Output PSD $S_Y(\\omega)$</span><br>
For an LTI system driven by a WSS input process, output PSD is given by:
$$S_Y(\\omega) = |H(\\omega)|^2 S_W(\\omega)$$
The squared magnitude response of the RC filter is:
$$|H(\\omega)|^2 = \\left| \\frac{1}{1 + j\\omega RC} \\right|^2 = \\frac{1}{1 + (\\omega RC)^2}$$
Therefore:
<span class="ans">$$S_Y(\\omega) = \\frac{N_0 / 2}{1 + (\\omega RC)^2}$$</span></p>

<p><span class="part">Part (b): Output Autocorrelation $R_Y(\\tau)$</span><br>
By the Wiener-Khinchin theorem:
$$R_Y(\\tau) = \\mathcal{F}^{-1}\\{S_Y(\\omega)\\} = \\frac{1}{2\\pi} \\int_{-\\infty}^\\infty \\frac{N_0/2}{1 + (\\omega RC)^2} e^{j\\omega \\tau} d\\omega$$
Rewrite into canonical Cauchy form with $a = \\frac{1}{RC}$:
$$S_Y(\\omega) = \\frac{N_0}{2(RC)^2} \\frac{1}{\\omega^2 + a^2}$$
Using the standard Fourier transform pair $\\mathcal{F}\\{e^{-a|\\tau|}\\} = \\frac{2a}{\\omega^2 + a^2} \\implies \\mathcal{F}^{-1}\\left\\{\\frac{1}{\\omega^2 + a^2}\\right\\} = \\frac{1}{2a} e^{-a|\\tau|}$:
$$R_Y(\\tau) = \\frac{N_0}{2(RC)^2} \\cdot \\frac{1}{2(1/RC)} e^{-|\\tau| / (RC)} = \\frac{N_0}{4RC} e^{-|\\tau| / (RC)}$$
<span class="ans">$$R_Y(\\tau) = \\frac{N_0}{4RC} \\exp\\left(-\\frac{|\\tau|}{RC}\\right)$$</span>
The output is an <strong>Ornstein-Uhlenbeck process</strong> with exponential autocorrelation.</p>

<p><span class="part">Part (c): Output Average Power $\\mathbb{E}[Y^2(t)]$</span><br>
Evaluating the autocorrelation at lag $\\tau = 0$:
<span class="ans">$$\\mathbb{E}[Y^2(t)] = R_Y(0) = \\frac{N_0}{4RC}$$</span>
Notice that as bandwidth $B = \\frac{1}{2\\pi RC} \\to \\infty$ (i.e. $RC \\to 0$), noise power diverges to $\\infty$, reflecting the infinite power of ideal white noise.</p>""",
        "takeaway": "LTI filtering of white noise acts in the frequency domain as $S_Y(\\omega) = |H(\\omega)|^2 S_W(\\omega)$. A first-order RC filter converts delta-correlated white noise into an Ornstein-Uhlenbeck process with exponential correlation $R_Y(\\tau) \\propto e^{-|\\tau|/RC}$."
    },
    {
        "id": 32393,
        "subject": "StoMA",
        "topicId": "23_Random_Processes_Stationarity_and_Ergodicity",
        "topicTitle": "23 · Random Processes & Wide-Sense Stationarity",
        "title": "Mean-Square Ergodicity of Ornstein-Uhlenbeck Process (IISc Endsem / Berkeley EECS 126)",
        "kind2": "generated",
        "source": "IISc Endsem / Berkeley EECS 126 Stochastic Systems",
        "marks": "[8 Marks]",
        "question": """<p>Let $X(t)$ be a zero-mean, continuous-time WSS process with exponential autocovariance:
$$C_X(\\tau) = \\sigma^2 e^{-\\alpha |\\tau|}, \\quad \\alpha > 0$$
To estimate the true mean $\\mu = 0$ from a single sample path, we form the finite-time time-average estimator:
$$\\hat{\\mu}_T = \\frac{1}{2T} \\int_{-T}^T X(t) dt$$</p>
<p><span class="part">(a)</span> Show that $\\hat{\\mu}_T$ is an unbiased estimator: $\\mathbb{E}[\\hat{\\mu}_T] = 0$.</p>
<p><span class="part">(b)</span> Derive an exact closed-form expression for the variance $\\operatorname{Var}(\\hat{\\mu}_T)$ as a function of the observation window half-width $T$.</p>
<p><span class="part">(c)</span> Prove that $X(t)$ is <strong>mean-square ergodic</strong>: $\\lim_{T \\to \\infty} \\operatorname{Var}(\\hat{\\mu}_T) = 0$.</p>""",
        "solution": """<p><span class="part">Part (a): Unbiasedness</span><br>
Using Fubini's theorem to interchange expectation and integration:
$$\\mathbb{E}[\\hat{\\mu}_T] = \\frac{1}{2T} \\int_{-T}^T \\mathbb{E}[X(t)] dt = \\frac{1}{2T} \\int_{-T}^T 0 \\, dt = <span class=\"ans\">0</span>$$
Hence $\\hat{\\mu}_T$ is strictly unbiased for all $T > 0$.</p>

<p><span class="part">Part (b): Exact Variance Formula</span><br>
Because $\\mathbb{E}[\\hat{\\mu}_T] = 0$:
$$\\operatorname{Var}(\\hat{\\mu}_T) = \\mathbb{E}[(\\hat{\\mu}_T)^2] = \\frac{1}{4T^2} \\int_{-T}^T \\int_{-T}^T \\mathbb{E}[X(t_1) X(t_2)] dt_1 dt_2 = \\frac{1}{4T^2} \\int_{-T}^T \\int_{-T}^T C_X(t_1 - t_2) dt_1 dt_2$$
Using the standard triangular convolution identity for double integrals over squares:
$$\\operatorname{Var}(\\hat{\\mu}_T) = \\frac{1}{2T} \\int_{-2T}^{2T} \\left(1 - \\frac{|\\tau|}{2T}\\right) C_X(\\tau) d\\tau = \\frac{1}{T} \\int_0^{2T} \\left(1 - \\frac{\\tau}{2T}\\right) \\sigma^2 e^{-\\alpha \\tau} d\\tau$$
Evaluating the two parts:
1. $\\int_0^{2T} e^{-\\alpha \\tau} d\\tau = \\frac{1 - e^{-2\\alpha T}}{\\alpha}$
2. $\\int_0^{2T} \\tau e^{-\\alpha \\tau} d\\tau = \\left[-\\frac{\\tau e^{-\\alpha \\tau}}{\\alpha}\\right]_0^{2T} + \\frac{1}{\\alpha} \\int_0^{2T} e^{-\\alpha \\tau} d\\tau = -\\frac{2T e^{-2\\alpha T}}{\\alpha} + \\frac{1 - e^{-2\\alpha T}}{\\alpha^2}$<br>
Combining and simplifying:
<span class="ans">$$\\operatorname{Var}(\\hat{\\mu}_T) = \\frac{\\sigma^2}{\\alpha T} \\left[ 1 - \\frac{1 - e^{-2\\alpha T}}{2\\alpha T} \\right]$$</span></p>

<p><span class="part">Part (c): Proof of Mean-Square Ergodicity</span><br>
Taking the asymptotic limit as window length $T \\to \\infty$:
$$\\lim_{T \\to \\infty} \\operatorname{Var}(\\hat{\\mu}_T) = \\lim_{T \\to \\infty} \\frac{\\sigma^2}{\\alpha T} [1 - 0] = \\lim_{T \\to \\infty} O\\left(\\frac{1}{T}\\right) = <span class=\"ans\">0</span>$$
By Chebyshev's inequality, for any $\\epsilon > 0$:
$$\\mathbb{P}(|\\hat{\\mu}_T - 0| \\ge \\epsilon) \\le \\frac{\\operatorname{Var}(\\hat{\\mu}_T)}{\\epsilon^2} \\xrightarrow{T \\to \\infty} 0$$
<span class=\"ans\">Thus $\\hat{\\mu}_T \\xrightarrow{L^2} 0$ (and $\\hat{\\mu}_T \\xrightarrow{p} 0$). The time average converges to the ensemble mean, proving mean-square ergodicity.</span></p>""",
        "takeaway": "A WSS process is mean-ergodic if its covariance decay satisfies Slutsky's condition $\\lim_{T \\to \\infty} \\frac{1}{T} \\int_0^{2T} C_X(\\tau) d\\tau = 0$. Exponential covariance yields variance $O(1/T)$, ensuring mean-square convergence."
    },

    # =========================================================================
    # TOPIC 24: Poisson Processes, Properties and Extensions
    # =========================================================================
    {
        "id": 32491,
        "subject": "StoMA",
        "topicId": "24_Poisson_Processes_Properties_and_Extensions",
        "topicTitle": "24 · Poisson Processes & Extensions",
        "title": "Inspection Paradox & Waiting Time Duality (IISc Midterm / MIT 6.041)",
        "kind2": "pyq",
        "source": "IISc Midterm / MIT 6.041 Probabilistic Systems Analysis",
        "marks": "[8 Marks]",
        "question": """<p>Buses arrive at a station according to a homogeneous Poisson process with rate $\\lambda$. A passenger arrives at the bus stop at a deterministic fixed time $t > 0$.</p>
<p><span class="part">(a)</span> Find the distribution and expected value of the forward recurrence time (waiting time until the next bus) $W(t) = A(t) - t$.</p>
<p><span class="part">(b)</span> Find the distribution and expected value of the backward recurrence time (elapsed time since the last bus) $B(t) = t - L(t)$, noting the boundary at 0.</p>
<p><span class="part">(c)</span> Compute the expected length of the inter-arrival interval containing $t$, $\\mathbb{E}[I(t)] = \\mathbb{E}[A(t) - L(t)]$. Explain why this resolves the famous <strong>Inspection (Waiting-Time) Paradox</strong>.</p>""",
        "solution": """<p><span class="part">Part (a): Forward Recurrence Time $W(t)$</span><br>
The event $W(t) > w$ means zero buses arrive in the future interval $(t, t+w]$.<br>
By independent and stationary increments of the Poisson process:
$$\\mathbb{P}(W(t) > w) = \\mathbb{P}(N(t+w) - N(t) = 0) = e^{-\\lambda w}, \\quad w \\ge 0$$
<span class="ans">$$W(t) \\sim \\text{Exp}(\\lambda), \\quad \\mathbb{E}[W(t)] = \\frac{1}{\\lambda}$$</span>
Due to the memoryless property, the remaining wait time is completely independent of when the last bus arrived or how long the stop has operated.</p>

<p><span class="part">Part (b): Backward Recurrence Time $B(t)$</span><br>
The event $B(t) > b$ means zero buses arrived in the past interval $(t - b, t]$.
- For $0 \\le b < t$:
$$\\mathbb{P}(B(t) > b) = \\mathbb{P}(N(t) - N(t-b) = 0) = e^{-\\lambda b}$$
- For $b \\ge t$: $B(t)$ cannot exceed $t$ (since the process started at time 0). Thus $\\mathbb{P}(B(t) = t) = \\mathbb{P}(N(t) = 0) = e^{-\\lambda t}$.<br>
Using the tail integral formula for non-negative random variables:
$$\\mathbb{E}[B(t)] = \\int_0^t \\mathbb{P}(B(t) > b) db = \\int_0^t e^{-\\lambda b} db = <span class=\"ans\">\\frac{1 - e^{-\\lambda t}}{\\lambda}</span>$$
As $t \\to \\infty$, $B(t) \\xrightarrow{d} \\text{Exp}(\\lambda)$ and $\\mathbb{E}[B(t)] \\to 1/\\lambda$.</p>

<p><span class="part">Part (c): The Inspection Paradox</span><br>
The covering interval containing time $t$ is $I(t) = W(t) + B(t)$.
$$\\mathbb{E}[I(t)] = \\mathbb{E}[W(t)] + \\mathbb{E}[B(t)] = \\frac{1}{\\lambda} + \\frac{1 - e^{-\\lambda t}}{\\lambda} = <span class=\"ans\">\\frac{2 - e^{-\\lambda t}}{\\lambda}</span>$$
As $t \\to \\infty$:
<span class="ans">$$\\lim_{t \\to \\infty} \\mathbb{E}[I(t)] = \\frac{2}{\\lambda} = 2 \\times \\mathbb{E}[\\text{interarrival time}]$$</span>
<strong>Resolution of the Paradox:</strong> Arriving at a fixed time $t$ is an <em>inspection mechanism</em> that samples time intervals with probability proportional to their length (<strong>length-biased sampling</strong>). Longer intervals occupy a larger fraction of the time axis and are twice as likely to trap the observer, explaining why $\\mathbb{E}[I(t)] = 2/\\lambda$ even though individual interarrival intervals average $1/\\lambda$.</p>""",
        "takeaway": "The Inspection Paradox: sampling an interval at a fixed time $t$ performs length-biased sampling ($f_I(x) \\propto x f(x)$). For Poisson processes, $\\mathbb{E}[W(t)] = 1/\\lambda$ and $\\mathbb{E}[B(t)] \\to 1/\\lambda$, yielding a covering interval of $2/\\lambda$."
    },
    {
        "id": 32492,
        "subject": "StoMA",
        "topicId": "24_Poisson_Processes_Properties_and_Extensions",
        "topicTitle": "24 · Poisson Processes & Extensions",
        "title": "Uniform Order Statistics & Accumulated Shopping Time (Stanford MS&E 220 / IISc Endsem)",
        "kind2": "university",
        "source": "Stanford MS&E 220 / IISc Endsem Probabilistic Analysis",
        "marks": "[8 Marks]",
        "question": """<p>Customers enter a superstore according to a Poisson process $N(t)$ with rate $\\lambda$. The store closes at time $T$. Each customer arriving at epoch $S_i < T$ spends the remaining duration $T - S_i$ inside the store before checkout at closing time. Let:
$$W = \\sum_{i=1}^{N(T)} (T - S_i)$$
denote the total cumulative customer-hours spent in the store.</p>
<p><span class="part">(a)</span> Using the uniform order statistics property of the Poisson process, compute $\\mathbb{E}[W \\mid N(T) = n]$.</p>
<p><span class="part">(b)</span> Find the unconditional expectation $\\mathbb{E}[W]$ using Adam's Law.</p>
<p><span class="part">(c)</span> Compute the total variance $\\operatorname{Var}(W)$ using Eve's Law (Law of Total Variance).</p>""",
        "solution": """<p><span class="part">Part (a): Conditional Expectation via Order Statistics</span><br>
By the <strong>Uniform Order Statistics Theorem</strong>: conditioned on $N(T) = n$, the joint distribution of arrival times $(S_1, \\dots, S_n)$ is identical to the order statistics of $n$ i.i.d. random variables $U_1, \\dots, U_n \\sim \\text{Uniform}[0, T]$.<br>
Because the sum $\\sum_{i=1}^n (T - S_i)$ is symmetric with respect to all arrival times:
$$\\sum_{i=1}^n (T - S_i) = \\sum_{i=1}^n (T - U_i)$$
where $U_i$ are unordered i.i.d. $\\text{Uniform}[0, T]$.<br>
Taking expectation given $N(T) = n$:
$$\\mathbb{E}[W \\mid N(T) = n] = \\sum_{i=1}^n \\mathbb{E}[T - U_i] = n \\left(T - \\frac{T}{2}\\right) = <span class=\"ans\">\\frac{n T}{2}</span>$$</p>

<p><span class="part">Part (b): Unconditional Mean $\\mathbb{E}[W]$</span><br>
By Adam's Law (Law of Total Expectation):
$$\\mathbb{E}[W] = \\mathbb{E}\\left[\\mathbb{E}[W \\mid N(T)]\\right] = \\mathbb{E}\\left[\\frac{N(T) T}{2}\\right] = \\frac{T}{2} \\mathbb{E}[N(T)] = \\frac{T}{2} (\\lambda T) = <span class=\"ans\">\\frac{\\lambda T^2}{2}</span>$$</p>

<p><span class="part">Part (c): Variance via Eve's Law</span><br>
By Eve's Law:
$$\\operatorname{Var}(W) = \\mathbb{E}[\\operatorname{Var}(W \\mid N(T))] + \\operatorname{Var}(\\mathbb{E}[W \\mid N(T)])$$
1. <strong>Conditional variance:</strong> Given $N(T) = n$, $T - U_i$ are i.i.d. uniform random variables with $\\operatorname{Var}(T - U_i) = \\operatorname{Var}(U_i) = \\frac{T^2}{12}$.
$$\\operatorname{Var}(W \\mid N(T) = n) = \\sum_{i=1}^n \\operatorname{Var}(T - U_i) = n \\frac{T^2}{12}$$
Taking expectation over $N(T) \\sim \\text{Poisson}(\\lambda T)$:
$$\\mathbb{E}[\\operatorname{Var}(W \\mid N(T))] = \\mathbb{E}\\left[N(T) \\frac{T^2}{12}\\right] = (\\lambda T) \\frac{T^2}{12} = \\frac{\\lambda T^3}{12}$$
2. <strong>Variance of conditional expectation:</strong>
$$\\operatorname{Var}(\\mathbb{E}[W \\mid N(T)]) = \\operatorname{Var}\\left(\\frac{N(T) T}{2}\\right) = \\frac{T^2}{4} \\operatorname{Var}(N(T)) = \\frac{T^2}{4} (\\lambda T) = \\frac{\\lambda T^3}{4}$$
3. <strong>Summing both terms:</strong>
$$\\operatorname{Var}(W) = \\frac{\\lambda T^3}{12} + \\frac{\\lambda T^3}{4} = \\frac{\\lambda T^3 + 3\\lambda T^3}{12} = <span class=\"ans\">\\frac{\\lambda T^3}{3}</span>$$</p>""",
        "takeaway": "Conditioned on $N(T) = n$, Poisson arrival epochs behave as order statistics of i.i.d. $\\text{Uniform}[0, T]$ variables. Eve's Law $\\operatorname{Var}(W) = \\mathbb{E}[\\operatorname{Var}(W|N)] + \\operatorname{Var}(\\mathbb{E}[W|N])$ combines intra-group and inter-group uncertainty."
    },
    {
        "id": 32493,
        "subject": "StoMA",
        "topicId": "24_Poisson_Processes_Properties_and_Extensions",
        "topicTitle": "24 · Poisson Processes & Extensions",
        "title": "Poisson Thinning & Multi-Class QoS Routing (IIT Delhi / Berkeley EECS 126)",
        "kind2": "generated",
        "source": "IIT Delhi / Berkeley EECS 126 Stochastic Systems",
        "marks": "[8 Marks]",
        "question": """<p>Data packets arrive at an edge router according to a Poisson process with aggregate rate $\\lambda = 10$ packets/ms. Each arriving packet is independently classified into one of three traffic classes:
- Class 1 (Voice / Priority): probability $p_1 = 0.20$
- Class 2 (Video streaming): probability $p_2 = 0.50$
- Class 3 (Background / Best-effort): probability $p_3 = 0.30$</p>
<p><span class="part">(a)</span> State the <strong>Poisson Splitting Theorem</strong> and write the joint probability that during a 1 ms window, exactly 2 voice packets, 4 video packets, and 3 background packets arrive.</p>
<p><span class="part">(b)</span> What is the probability that the first voice packet arrives before any background packet?</p>
<p><span class="part">(c)</span> Given that a total of 10 packets arrived in a 1 ms window, find the conditional distribution and conditional expectation of the number of voice packets.</p>""",
        "solution": """<p><span class="part">Part (a): Poisson Splitting & Joint Probability</span><br>
<strong>Poisson Splitting Theorem:</strong> If a Poisson process with rate $\\lambda$ is independently thinned into $K$ streams with routing probabilities $p_1, \\dots, p_K$ (where $\\sum p_k = 1$), the resulting streams $N_1(t), \\dots, N_K(t)$ are <strong>completely mutually independent Poisson processes</strong> with rates $\\lambda_k = \\lambda p_k$.<br>
Here:
$$\\lambda_1 = 10 \\times 0.2 = 2 \\text{ pkts/ms}, \\quad \\lambda_2 = 10 \\times 0.5 = 5 \\text{ pkts/ms}, \\quad \\lambda_3 = 10 \\times 0.3 = 3 \\text{ pkts/ms}$$
For duration $t = 1$ ms: $N_1 \\sim \\text{Poisson}(2), N_2 \\sim \\text{Poisson}(5), N_3 \\sim \\text{Poisson}(3)$. By mutual independence:
$$\\mathbb{P}(N_1(1)=2, N_2(1)=4, N_3(1)=3) = \\mathbb{P}(N_1=2) \\times \\mathbb{P}(N_2=4) \\times \\mathbb{P}(N_3=3)$$
$$= \\left(\\frac{2^2 e^{-2}}{2!}\\right) \\left(\\frac{5^4 e^{-5}}{4!}\\right) \\left(\\frac{3^3 e^{-3}}{3!}\\right) = \\left(2 e^{-2}\\right) \\left(\\frac{625}{24} e^{-5}\\right) \\left(\\frac{9}{2} e^{-3}\\right)$$
$$= \\frac{2 \\times 625 \\times 9}{48} e^{-10} = \\frac{1875}{8} e^{-10} \\approx <span class=\"ans\">234.375 \\times 4.54 \\times 10^{-5} \\approx 0.01064 \\text{ (1.06%)}</span>$$</p>

<p><span class="part">Part (b): Competing Exponentials Race</span><br>
Let $T_1 \\sim \\text{Exp}(\\lambda_1 = 2)$ and $T_3 \\sim \\text{Exp}(\\lambda_3 = 3)$ be the arrival times of the first Class 1 and Class 3 packets.<br>
By the property of competing independent exponential clocks:
<span class="ans">$$\\mathbb{P}(T_1 < T_3) = \\frac{\\lambda_1}{\\lambda_1 + \\lambda_3} = \\frac{2}{2 + 3} = \\frac{2}{5} = 0.40$$</span>
Equivalently: each packet that is either Class 1 or Class 3 is Class 1 with probability $\\frac{p_1}{p_1 + p_3} = \\frac{0.2}{0.5} = 0.40$.</p>

<p><span class="part">Part (c): Conditional Distribution given Total Count</span><br>
Conditioned on total count $N(1) = N_1(1) + N_2(1) + N_3(1) = 10$:<br>
Each of the 10 packets independently belongs to Class 1 with probability $p_1 = 0.20$.<br>
Therefore:
<span class="ans">$$N_1(1) \\mid \\{N(1) = 10\\} \\sim \\text{Binomial}(n = 10, p = 0.20)$$</span>
The conditional expectation is:
<span class="ans">$$\\mathbb{E}[N_1(1) \\mid N(1) = 10] = 10 \\times 0.20 = 2 \\text{ packets}$$</span></p>""",
        "takeaway": "Poisson splitting yields mutually independent Poisson streams with rates $\\lambda_k = \\lambda p_k$. Conditioned on aggregate arrival count $N(t)=n$, the distribution of split counts is $\\text{Multinomial}(n, p_1, \\dots, p_K)$."
    }
]

def main():
    with open(PRACTICE_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    if "32391" in content:
        print("Batch 23-24 already present in practice_stoma.js!")
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
    for card in PRACTICE_STOMA_23_24:
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

    print("Successfully added Batch 23-24 (6 cards). Total in file now updated.")

if __name__ == "__main__":
    main()
