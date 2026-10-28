#!/usr/bin/env python3
"""
Builder script for StoMA Practice Cards: Batch 11 (Topics 21 & 22)
Topic 21: Absorption Probabilities and Mean Hitting Times (Cards 32191, 32192, 32193)
Topic 22: Birth-Death Chains and MCMC (Cards 32291, 32292, 32293)
"""

import json
import os
import re

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRACTICE_FILE = os.path.join(REPO_DIR, "practice_stoma.js")

PRACTICE_STOMA_21_22 = [
    # =========================================================================
    # TOPIC 21: Absorption Probabilities and Mean Hitting Times
    # =========================================================================
    {
        "id": 32191,
        "subject": "StoMA",
        "topicId": "21_Absorption_Probabilities_and_Mean_Hitting_Times",
        "topicTitle": "21 · Absorption & Mean Hitting Times",
        "title": "Gambler's Ruin with Drift via First-Step Analysis (IISc Midterm / MIT 18.440)",
        "kind2": "pyq",
        "source": "IISc Midterm / MIT 18.440 Probability",
        "marks": "[8 Marks]",
        "question": """<p>A gambler starts with $\$i$ ($0 \\le i \\le N$) and bets $\$1$ repeatedly until reaching $\$N$ (fortune) or $\$0$ (ruin). In each round, they win $\$1$ with probability $p$ and lose $\$1$ with probability $q = 1 - p \\ne p$ (biased game, $\\rho = q/p \\ne 1$).</p>
<p><span class="part">(a)</span> Set up the first-step difference equation for the probability of ruin $a_i = \\mathbb{P}(\\text{ruin} \\mid X_0 = i)$ and solve for $a_i$ in closed form.</p>
<p><span class="part">(b)</span> Formulate the first-step equation for the expected duration $\\mu_i = \\mathbb{E}[T \\mid X_0 = i]$ until absorption, and solve for $\\mu_i$ explicitly.</p>""",
        "solution": """<p><span class="part">Part (a): Ruin Probability $a_i$</span><br>
Conditioning on the first step:
$$a_i = p a_{i+1} + q a_{i-1}, \\quad 1 \\le i \\le N-1$$
with absorbing boundary conditions:
$$a_0 = 1, \\quad a_N = 0$$
Since $p + q = 1$, rewrite as:
$$p(a_{i+1} - a_i) = q(a_i - a_{i-1}) \\implies a_{i+1} - a_i = \\rho (a_i - a_{i-1}), \\quad \\text{where } \\rho = \\frac{q}{p}$$
Telescoping the geometric progression:
$$a_k - a_{k-1} = \\rho^{k-1}(a_1 - a_0) = \\rho^{k-1}(a_1 - 1)$$
Summing from $k = 1$ to $i$:
$$a_i - 1 = (a_1 - 1) \\sum_{k=1}^i \\rho^{k-1} = (a_1 - 1) \\frac{1 - \\rho^i}{1 - \\rho}$$
Setting $i = N$ with $a_N = 0$:
$$0 - 1 = (a_1 - 1) \\frac{1 - \\rho^N}{1 - \\rho} \\implies a_1 - 1 = -\\frac{1 - \\rho}{1 - \\rho^N}$$
Substituting back into $a_i$:
<span class="ans">$$a_i = 1 - \\frac{1 - \\rho^i}{1 - \\rho^N} = \\frac{\\rho^i - \\rho^N}{1 - \\rho^N} = \\frac{(q/p)^i - (q/p)^N}{1 - (q/p)^N}$$</span></p>

<p><span class="part">Part (b): Expected Duration $\\mu_i$</span><br>
Conditioning on the first transition:
$$\\mu_i = 1 + p \\mu_{i+1} + q \\mu_{i-1}, \\quad \\mu_0 = 0, \\; \\mu_N = 0$$
The homogeneous solution is $C_1 + C_2 \\rho^i$. For the particular solution, try linear ansatz $\\mu_i = c \\cdot i$:
$$c \\cdot i = 1 + p c (i+1) + q c (i-1) = 1 + c \\cdot i + c(p - q) \\implies c(q - p) = 1 \\implies c = \\frac{1}{q - p}$$
General solution:
$$\\mu_i = C_1 + C_2 \\rho^i + \\frac{i}{q - p}$$
Matching boundary conditions:
- $\\mu_0 = 0 \\implies C_1 + C_2 = 0 \\implies C_1 = -C_2$
- $\\mu_N = 0 \\implies C_2(\\rho^N - 1) + \\frac{N}{q - p} = 0 \\implies C_2 = \\frac{N}{(q - p)(1 - \\rho^N)}$
Therefore:
<span class="ans">$$\\mu_i = \\frac{i}{q - p} - \\frac{N}{q - p} \\left(\\frac{1 - \\rho^i}{1 - \\rho^N}\\right) = \\frac{i - N(1 - a_i)}{q - p}$$</span></p>""",
        "takeaway": "First-step analysis converts hitting/absorption problems into linear difference equations: $(I-P)a = 0$ for probabilities with Dirichlet boundary values, and $(I-P)\\mu = \\mathbf{1}$ for expected absorption times."
    },
    {
        "id": 32192,
        "subject": "StoMA",
        "topicId": "21_Absorption_Probabilities_and_Mean_Hitting_Times",
        "topicTitle": "21 · Absorption & Mean Hitting Times",
        "title": "Fundamental Matrix & Absorption Probability in Mutational Dynamics (Stanford CS279 / IIT Bombay)",
        "kind2": "university",
        "source": "Stanford CS279 / IIT Bombay EE",
        "marks": "[8 Marks]",
        "question": """<p>A genetic sequence site transitions among four nucleotides $\{1 (A), 2 (C), 3 (G), 4 (T)\}$. States 1 and 2 are viable transient states, while states 3 and 4 are lethal absorbing states. The transition probability matrix is:
$$P = \\begin{pmatrix}
0.4 & 0.3 & 0.2 & 0.1 \\\\
0.2 & 0.5 & 0.1 & 0.2 \\\\
0 & 0 & 1 & 0 \\\\
0 & 0 & 0 & 1
\\end{pmatrix}$$</p>
<p><span class="part">(a)</span> Partition $P$ into canonical form $\\begin{pmatrix} Q & R \\\\ 0 & I \\end{pmatrix}$ and compute the fundamental matrix $N = (I - Q)^{-1}$.</p>
<p><span class="part">(b)</span> Compute the expected time until absorption starting from state 1 ($A$) and state 2 ($C$).</p>
<p><span class="part">(c)</span> Calculate the absorption probabilities into each absorbing state starting from state 1 ($A$).</p>""",
        "solution": """<p><span class="part">Part (a): Canonical Partition & Fundamental Matrix $N$</span><br>
Transient states $T = \\{1, 2\\}$, absorbing states $A = \\{3, 4\\}$:
$$Q = \\begin{pmatrix} 0.4 & 0.3 \\\\ 0.2 & 0.5 \\end{pmatrix}, \\quad R = \\begin{pmatrix} 0.2 & 0.1 \\\\ 0.1 & 0.2 \\end{pmatrix}$$
Form $I - Q$:
$$I - Q = \\begin{pmatrix} 0.6 & -0.3 \\\\ -0.2 & 0.5 \\end{pmatrix}$$
Determinant: $\\det(I - Q) = (0.6)(0.5) - (-0.3)(-0.2) = 0.30 - 0.06 = 0.24 = \\frac{6}{25}$.<br>
Inverting the $2 \\times 2$ matrix:
$$N = (I - Q)^{-1} = \\frac{1}{0.24} \\begin{pmatrix} 0.5 & 0.3 \\\\ 0.2 & 0.6 \\end{pmatrix} = \\frac{25}{6} \\begin{pmatrix} 1/2 & 3/10 \\\\ 1/5 & 3/5 \\end{pmatrix}$$
<span class="ans">$$N = \\begin{pmatrix} 25/12 & 5/4 \\\\ 5/6 & 5/2 \\end{pmatrix} = \\begin{pmatrix} 2.083 & 1.25 \\\\ 0.833 & 2.50 \\end{pmatrix}$$</span>
Entry $N_{ij}$ represents the expected number of visits to transient state $j$ before absorption, starting from $i$.</p>

<p><span class="part">Part (b): Expected Time to Absorption $\\mathbf{t} = N \\mathbf{1}$</span><br>
The expected number of steps until absorption from state $i$ is the $i$-th row sum of $N$:
$$t_1 = N_{11} + N_{12} = \\frac{25}{12} + \\frac{15}{12} = \\frac{40}{12} = \\frac{10}{3} \\approx <span class=\"ans\">3.333 \\text{ steps}</span>$$
$$t_2 = N_{21} + N_{22} = \\frac{5}{6} + \\frac{15}{6} = \\frac{20}{6} = \\frac{10}{3} \\approx <span class=\"ans\">3.333 \\text{ steps}</span>$$</p>

<p><span class="part">Part (c): Absorption Probabilities $B = N R$</span><br>
Matrix $B_{ij}$ gives the probability of being absorbed into absorbing state $j$ given start in transient state $i$:
$$B = N R = \\begin{pmatrix} 25/12 & 5/4 \\\\ 5/6 & 5/2 \\end{pmatrix} \\begin{pmatrix} 1/5 & 1/10 \\\\ 1/10 & 1/5 \\end{pmatrix}$$
For initial state 1 (row 1):
$$B_{13} = \\left(\\frac{25}{12}\\right)\\left(\\frac{1}{5}\\right) + \\left(\\frac{5}{4}\\right)\\left(\\frac{1}{10}\\right) = \\frac{5}{12} + \\frac{1}{8} = \\frac{10 + 3}{24} = <span class=\"ans\">\\frac{13}{24} \\approx 0.5417</span>$$
$$B_{14} = \\left(\\frac{25}{12}\\right)\\left(\\frac{1}{10}\\right) + \\left(\\frac{5}{4}\\right)\\left(\\frac{1}{5}\\right) = \\frac{5}{24} + \\frac{1}{4} = \\frac{5 + 6}{24} = <span class=\"ans\">\\frac{11}{24} \\approx 0.4583</span>$$
Check: $B_{13} + B_{14} = \\frac{13}{24} + \\frac{11}{24} = 1$ (absorption is certain).</p>""",
        "takeaway": "For any absorbing Markov chain in canonical form: fundamental matrix $N = (I-Q)^{-1}$ counts expected transient visits; mean time to absorption is $\\mathbf{t} = N\\mathbf{1}$; absorption probabilities are $B = NR$."
    },
    {
        "id": 32193,
        "subject": "StoMA",
        "topicId": "21_Absorption_Probabilities_and_Mean_Hitting_Times",
        "topicTitle": "21 · Absorption & Mean Hitting Times",
        "title": "Coin Pattern Waiting Times: $HT$ vs $HH$ Paradox (IISc Endsem / Berkeley EECS 126)",
        "kind2": "generated",
        "source": "IISc Endsem / Berkeley EECS 126 Probability",
        "marks": "[8 Marks]",
        "question": """<p>A fair coin is repeatedly and independently tossed ($P(H) = P(T) = 1/2$).</p>
<p><span class="part">(a)</span> Formulate a DTMC on prefixes to find the expected number of tosses $\\mathbb{E}[T_{HT}]$ until the consecutive pattern $HT$ first appears.</p>
<p><span class="part">(b)</span> Formulate the corresponding DTMC to find $\\mathbb{E}[T_{HH}]$ until $HH$ first appears.</p>
<p><span class="part">(c)</span> Explain intuitively why $\\mathbb{E}[T_{HH}] = 6 > 4 = \\mathbb{E}[T_{HT}]$, despite both two-letter sequences having identical likelihood $(1/2)^2 = 1/4$ at any fixed position.</p>""",
        "solution": """<p><span class="part">Part (a): Expected Tosses for Pattern $HT$</span><br>
Define states tracking the longest prefix of $HT$ currently observed:
- State 0: $\\emptyset$ (no match).
- State 1: $H$ matched.
- State 2: $HT$ completed (absorbing target).

Transitions:
- From state 0: if $T \\to 0$ (prob $1/2$), if $H \\to 1$ (prob $1/2$).
- From state 1: if $H \\to 1$ (prob $1/2$), if $T \\to 2$ (prob $1/2$, target hit!).

Let $\\mu_i = \\mathbb{E}[\\text{steps to target} \\mid X_0 = i]$:
$$\\mu_0 = 1 + \\frac{1}{2}\\mu_0 + \\frac{1}{2}\\mu_1 \\implies \\frac{1}{2}\\mu_0 = 1 + \\frac{1}{2}\\mu_1 \\implies \\mu_0 = 2 + \\mu_1$$
$$\\mu_1 = 1 + \\frac{1}{2}\\mu_1 + \\frac{1}{2}(0) \\implies \\frac{1}{2}\\mu_1 = 1 \\implies \\mu_1 = 2$$
Substituting $\\mu_1 = 2$:
<span class="ans">$$\\mathbb{E}[T_{HT}] = \\mu_0 = 2 + 2 = 4 \\text{ tosses}$$</span></p>

<p><span class="part">Part (b): Expected Tosses for Pattern $HH$</span><br>
States tracking prefix of $HH$:
- State 0: $\\emptyset$.
- State 1: $H$.
- State 2: $HH$ completed (absorbing target).

Transitions:
- From state 0: if $T \\to 0$ (prob $1/2$), if $H \\to 1$ (prob $1/2$).
- From state 1: if $H \\to 2$ (prob $1/2$, target hit!), but if $T \\to 0$ (prob $1/2$, full reset!).

First-step equations:
$$\\mu_0 = 1 + \\frac{1}{2}\\mu_0 + \\frac{1}{2}\\mu_1 \\implies \\mu_0 = 2 + \\mu_1$$
$$\\mu_1 = 1 + \\frac{1}{2}(0) + \\frac{1}{2}\\mu_0 \\implies \\mu_1 = 1 + \\frac{1}{2}\\mu_0$$
Substituting $\\mu_1$ into $\\mu_0$:
$$\\mu_0 = 2 + \\left(1 + \\frac{1}{2}\\mu_0\\right) = 3 + \\frac{1}{2}\\mu_0 \\implies \\frac{1}{2}\\mu_0 = 3 \\implies <span class=\"ans\">\\mathbb{E}[T_{HH}] = \\mu_0 = 6 \\text{ tosses}</span>$$
And $\\mu_1 = 1 + 3 = 4$.</p>

<p><span class="part">Part (c): Overlap / Clumping Asymmetry</span><br>
1. <strong>Self-overlap & clumping:</strong> The pattern $HH$ has self-overlap (the second $H$ can serve as the first $H$ of another occurrence). Hence $HH$ occurrences clump together in runs ($HHH$ contains two $HH$ patterns). Because occurrences clump, the waiting time between non-overlapping clusters must be longer to preserve long-run frequency $\\pi = 1/4$.<br>
2. <strong>Penalty of failure:</strong> When holding prefix $H$:
- For $HT$: a roll of $H$ retains prefix $H$ (cost: 0 lost progress).
- For $HH$: a roll of $T$ wipes all progress, resetting back to $\\emptyset$ (cost: 1 lost step).<br>
<span class=\"ans\">Thus $\\mathbb{E}[T_{HH}] = 6 > 4 = \\mathbb{E}[T_{HT}]$ due to self-overlap clumping and failure penalty.</span></p>""",
        "takeaway": "Self-overlapping patterns ($HH, AAA$) clump together, increasing mean first-hitting time $\\mathbb{E}[T]$, whereas non-overlapping patterns ($HT, AB$) cannot clump and have strictly smaller expected waiting times."
    },

    # =========================================================================
    # TOPIC 22: Birth-Death Chains and MCMC
    # =========================================================================
    {
        "id": 32291,
        "subject": "StoMA",
        "topicId": "22_Birth_Death_Chains_and_MCMC",
        "topicTitle": "22 · Birth-Death Chains & MCMC",
        "title": "Embedded $M/M/1/K$ Birth-Death Queue & Detailed Balance (IISc E1 222 / MIT 6.262)",
        "kind2": "pyq",
        "source": "IISc E1 222 / MIT 6.262 Discrete Stochastic Processes",
        "marks": "[8 Marks]",
        "question": """<p>Consider the embedded discrete-time Markov chain of an $M/M/1/K$ finite-buffer queue with state space $S = \\{0, 1, \\dots, K\\}$ representing customer count. At intermediate states $1 \\le i \\le K-1$, transitions occur with birth probability $p$ (arrival) and death probability $q = 1 - p$ (departure). At boundaries: $P_{01} = 1$ and $P_{K, K-1} = 1$. Let $\\rho = p/q \\ne 1$.</p>
<p><span class="part">(a)</span> Write down the detailed balance equations and derive the stationary distribution $\\pi_i$ for all $0 \\le i \\le K$ in terms of $\\pi_0$.</p>
<p><span class="part">(b)</span> Normalize $\\pi_i$ to find an explicit closed-form expression for $\\pi_0$.</p>
<p><span class="part">(c)</span> Compute the packet loss (blocking) probability $P_{\\text{loss}} = \\pi_K$.</p>""",
        "solution": """<p><span class="part">Part (a): Detailed Balance Equations</span><br>
Any birth-death chain is time-reversible; the stationary distribution satisfies local detailed balance across each cut $(i, i+1)$:
$$\\pi_i P_{i, i+1} = \\pi_{i+1} P_{i+1, i}$$
1. At boundary $i = 0$:
$$\\pi_0 P_{01} = \\pi_1 P_{10} \\implies \\pi_0 (1) = \\pi_1 q \\implies \\pi_1 = \\frac{1}{q} \\pi_0$$
2. For internal states $1 \\le i \\le K-2$:
$$\\pi_i p = \\pi_{i+1} q \\implies \\pi_{i+1} = \\rho \\pi_i, \\quad \\text{where } \\rho = \\frac{p}{q}$$
By induction:
$$\\pi_i = \\rho^{i-1} \\pi_1 = \\frac{\\rho^{i-1}}{q} \\pi_0, \\quad \\text{for } 1 \\le i \\le K-1$$
3. At boundary $i = K-1$:
$$\\pi_{K-1} P_{K-1, K} = \\pi_K P_{K, K-1} \\implies \\pi_{K-1} p = \\pi_K (1) \\implies \\pi_K = p \\pi_{K-1} = p \\left(\\frac{\\rho^{K-2}}{q} \\pi_0\\right) = \\rho^{K-1} \\pi_0$$
<span class="ans">Summary: $\\pi_0 = \\pi_0$, $\\pi_i = \\frac{\\rho^{i-1}}{q}\\pi_0$ ($1 \\le i \\le K-1$), $\\pi_K = \\rho^{K-1}\\pi_0$.</span></p>

<p><span class="part">Part (b): Normalization for $\\pi_0$</span><br>
Using total probability $\\sum_{i=0}^K \\pi_i = 1$:
$$1 = \\pi_0 \\left[ 1 + \\frac{1}{q} \\sum_{i=1}^{K-1} \\rho^{i-1} + \\rho^{K-1} \\right] = \\pi_0 \\left[ 1 + \\frac{1}{q} \\left(\\frac{1 - \\rho^{K-1}}{1 - \\rho}\\right) + \\rho^{K-1} \\right]$$
Since $1 - \\rho = 1 - \\frac{p}{q} = \\frac{q - p}{q}$, we have $\\frac{1}{q(1 - \\rho)} = \\frac{1}{q - p}$. Thus:
$$1 = \\pi_0 \\left[ 1 + \\frac{1 - \\rho^{K-1}}{q - p} + \\rho^{K-1} \\right]$$
<span class="ans">$$\\pi_0 = \\left[ 1 + \\frac{1 - \\rho^{K-1}}{q - p} + \\rho^{K-1} \\right]^{-1}$$</span></p>

<p><span class="part">Part (c): Blocking Probability $P_{\\text{loss}}$</span><br>
Arriving packets find the buffer full when the chain is in state $K$:
<span class="ans">$$P_{\\text{loss}} = \\pi_K = \\rho^{K-1} \\pi_0 = \\frac{\\rho^{K-1}}{1 + \\frac{1 - \\rho^{K-1}}{q - p} + \\rho^{K-1}}$$</span></p>""",
        "takeaway": "Birth-death chains are always time-reversible because their state transition graph is a tree (no cycles). Detailed balance $\\pi_i p_{i, i+1} = \\pi_{i+1} p_{i+1, i}$ gives closed-form geometric product solutions."
    },
    {
        "id": 32292,
        "subject": "StoMA",
        "topicId": "22_Birth_Death_Chains_and_MCMC",
        "topicTitle": "22 · Birth-Death Chains & MCMC",
        "title": "Random-Walk Metropolis-Hastings on Half-Line (IIT Delhi / Stanford CS229)",
        "kind2": "university",
        "source": "IIT Delhi / Stanford CS229 Machine Learning",
        "marks": "[8 Marks]",
        "question": """<p>We wish to draw samples from an exponential distribution with rate $\\lambda > 0$, target density $\\pi(x) = \\lambda e^{-\\lambda x} \\mathbf{1}_{\\{x \\ge 0\\}}$, using a continuous Random-Walk Metropolis-Hastings algorithm. The proposal kernel is symmetric uniform: $q(y \\mid x) \\sim \\text{Uniform}(x - \\delta, x + \\delta)$ for window parameter $\\delta > 0$.</p>
<p><span class="part">(a)</span> Compute the acceptance probability $\\alpha(x, y)$ for proposed state $y \\ge 0$.</p>
<p><span class="part">(b)</span> What is the acceptance probability and chain behavior when the proposal generates $y < 0$?</p>
<p><span class="part">(c)</span> Prove that the resulting Metropolis-Hastings transition kernel satisfies detailed balance with respect to $\\pi(x)$, ensuring $\\pi(x)$ is the exact stationary distribution.</p>""",
        "solution": """<p><span class="part">Part (a): Acceptance Probability for $y \\ge 0$</span><br>
The proposal distribution is symmetric:
$$q(y \\mid x) = \\frac{1}{2\\delta} \\mathbf{1}_{\\{|y - x| \\le \\delta\\}} = q(x \\mid y)$$
Hence the proposal ratio is 1: $\\frac{q(x \\mid y)}{q(y \\mid x)} = 1$.<br>
The Metropolis-Hastings acceptance probability is:
$$\\alpha(x, y) = \\min\\left(1, \\frac{\\pi(y) q(x \\mid y)}{\\pi(x) q(y \\mid x)}\\right) = \\min\\left(1, \\frac{\\pi(y)}{\\pi(x)}\\right)$$
For $x, y \\ge 0$:
$$\\frac{\\pi(y)}{\\pi(x)} = \\frac{\\lambda e^{-\\lambda y}}{\\lambda e^{-\\lambda x}} = e^{-\\lambda(y - x)}$$
Therefore:
<span class="ans">$$\\alpha(x, y) = \\min\\left(1, e^{-\\lambda(y - x)}\\right) = \\begin{cases} 1 & \\text{if } y \\le x \\text{ (moves left towards mode are always accepted)} \\\\ e^{-\\lambda(y - x)} & \\text{if } y > x \\text{ (moves right accepted with probability } e^{-\\lambda(y-x)}) \\end{cases}$$</span></p>

<p><span class="part">Part (b): Boundary Rejection for $y < 0$</span><br>
For $y < 0$, the target density is $\\pi(y) = 0$.
$$\\alpha(x, y) = \\min\\left(1, \\frac{0}{\\pi(x)}\\right) = <span class=\"ans\">0</span>$$
The proposed step into the negative half-line is rejected with probability 1. The chain repeats its current state: $X_{t+1} = X_t$. This creates a positive probability atom of remaining at $x$ when near the boundary $x < \\delta$.</p>

<p><span class="part">Part (c): Proof of Detailed Balance</span><br>
Let $K(x, dy) = q(y \\mid x) \\alpha(x, y) dy + r(x) \\delta_x(dy)$ be the transition kernel. For $x \\ne y$ ($x, y \\ge 0$):
$$\\pi(x) q(y \\mid x) \\alpha(x, y) = \\pi(x) q(y \\mid x) \\min\\left(1, \\frac{\\pi(y)}{\\pi(x)}\\right) = q(y \\mid x) \\min\\left(\\pi(x), \\pi(y)\\right)$$
By symmetry of proposal $q(y \\mid x) = q(x \\mid y)$:
$$q(y \\mid x) \\min\\left(\\pi(x), \\pi(y)\\right) = q(x \\mid y) \\min\\left(\\pi(y), \\pi(x)\\right) = \\pi(y) q(x \\mid y) \\min\\left(1, \\frac{\\pi(x)}{\\pi(y)}\\right) = \\pi(y) q(x \\mid y) \\alpha(y, x)$$
<span class="ans">Thus $\\pi(x) K(x, dy) = \\pi(y) K(y, dx)$ strictly holds for all $x, y$. Detailed balance guarantees that $\\pi(x)$ is the stationary density.</span></p>""",
        "takeaway": "Metropolis-Hastings enforces detailed balance $\\pi(x)P(x,y) = \\pi(y)P(y,x)$ by setting acceptance $\\alpha(x,y) = \\min(1, \\frac{\\pi(y)q(x|y)}{\\pi(x)q(y|x)})$. Boundary violations $\\pi(y)=0$ yield $\\alpha=0$ and are safely rejected."
    },
    {
        "id": 32293,
        "subject": "StoMA",
        "topicId": "22_Birth_Death_Chains_and_MCMC",
        "topicTitle": "22 · Birth-Death Chains & MCMC",
        "title": "Kolmogorov Cycle Criterion & Irreversibility of Circulant Chains (Princeton ORF 524 / IISc Endsem)",
        "kind2": "generated",
        "source": "Princeton ORF 524 / IISc Endsem Stochastic Models",
        "marks": "[8 Marks]",
        "question": """<p><span class="part">(a)</span> State <strong>Kolmogorov's Cycle Criterion</strong> for the time-reversibility of an irreducible Markov chain.</p>
<p><span class="part">(b)</span> Consider a 3-state Markov chain on $S = \\{1, 2, 3\\}$ with transition probability matrix:
$$P = \\begin{pmatrix}
0 & 2/3 & 1/3 \\\\
1/3 & 0 & 2/3 \\\\
2/3 & 1/3 & 0
\\end{pmatrix}$$
Find the stationary distribution $\\pi$ and apply Kolmogorov's Cycle Criterion along cycle $1 \\to 2 \\to 3 \\to 1$ to prove whether the chain is reversible.</p>
<p><span class="part">(c)</span> What is the physical / probabilistic interpretation of a non-reversible stationary chain?</p>""",
        "solution": """<p><span class="part">Part (a): Kolmogorov's Cycle Criterion</span><br>
A stationary Markov chain with transition matrix $P$ is <strong>reversible</strong> (detailed balance $\\pi_i P_{ij} = \\pi_j P_{ji}$ holds for all $i, j$) if and only if for every directed cycle of states $i_1 \\to i_2 \\to \\dots \\to i_m \\to i_1$, the product of transition probabilities in the forward direction equals the product in the reverse direction:
<span class="ans">$$P_{i_1 i_2} P_{i_2 i_3} \\cdots P_{i_{m-1} i_m} P_{i_m i_1} = P_{i_1 i_m} P_{i_m i_{m-1}} \\cdots P_{i_3 i_2} P_{i_2 i_1}$$</span>
Remarkably, this criterion can be verified directly from $P$ <em>without knowing</em> the stationary distribution $\\pi$.</p>

<p><span class="part">Part (b): Testing Matrix $P$</span><br>
1. <strong>Stationary Distribution:</strong> Matrix $P$ is doubly stochastic (all row sums = 1, all column sums: $0 + 1/3 + 2/3 = 1$). Therefore, the stationary distribution is uniform:
$$\\pi = \\begin{pmatrix} 1/3 & 1/3 & 1/3 \\end{pmatrix}$$
2. <strong>Testing Cycle $1 \\to 2 \\to 3 \\to 1$:</strong>
- Forward product (clockwise $1 \\to 2 \\to 3 \\to 1$):
$$\\Pi_{\\text{fwd}} = P_{12} P_{23} P_{31} = \\left(\\frac{2}{3}\\right) \\times \\left(\\frac{2}{3}\\right) \\times \\left(\\frac{2}{3}\\right) = \\frac{8}{27}$$
- Reverse product (counter-clockwise $1 \\to 3 \\to 2 \\to 1$):
$$\\Pi_{\\text{rev}} = P_{13} P_{32} P_{21} = \\left(\\frac{1}{3}\\right) \\times \\left(\\frac{1}{3}\\right) \\times \\left(\\frac{1}{3}\\right) = \\frac{1}{27}$$
3. <strong>Comparison:</strong>
$$\\Pi_{\\text{fwd}} = \\frac{8}{27} \\ne \\frac{1}{27} = \\Pi_{\\text{rev}}$$
<span class="ans">The cycle criterion is violated! Hence, the chain is strictly <strong>not reversible</strong>.</span></p>

<p><span class="part">Part (c): Probabilistic & Physical Interpretation</span><br>
In a reversible Markov chain, the process looks statistically identical run forward or backward in time; net probability current between any two states is zero ($J_{ij} = \\pi_i P_{ij} - \\pi_j P_{ji} = 0$).<br>
In this chain:
$$J_{12} = \\pi_1 P_{12} - \\pi_2 P_{21} = \\left(\\frac{1}{3}\\right)\\left(\\frac{2}{3}\\right) - \\left(\\frac{1}{3}\\right)\\left(\\frac{1}{3}\\right) = \\frac{2}{9} - \\frac{1}{9} = <span class=\"ans\">+\\frac{1}{9} > 0</span>$$
<span class="ans">There is a persistent clockwise probability circulation (current of $+1/9$ circling $1 \\to 2 \\to 3 \\to 1$). A video of the chain running backward would clearly reveal counter-clockwise circulation, breaking time symmetry.</span></p>""",
        "takeaway": "Kolmogorov's Cycle Criterion tests reversibility without computing $\\pi$: clockwise cycle products must equal counter-clockwise products. Doubly stochastic circulant matrices with directional bias create persistent circulation currents."
    }
]

def main():
    with open(PRACTICE_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # Find where cards are defined
    # Check if batch 21-22 already added
    if "32191" in content:
        print("Batch 21-22 already present in practice_stoma.js!")
        return

    # Find the closing bracket of window.PRACTICE_DATA.push([...])
    # StoMA cards are appended to window.PRACTICE_DATA
    # In practice_stoma.js:
    # window.PRACTICE_DATA = window.PRACTICE_DATA || [];
    # window.PRACTICE_DATA.push([ ... cards ... ]);
    
    # We append to the array inside window.PRACTICE_DATA.push
    m = re.search(r"window\.PRACTICE_DATA\.push\(\s*\[\s*(.*?)\s*\]\s*\);", content, re.DOTALL)
    if not m:
        # Check if window.PRACTICE_STOMA is used or direct push
        print("Could not match window.PRACTICE_DATA.push pattern directly. Inspecting...")
        print(content[-300:])
        return

    existing_cards_text = m.group(1).rstrip()
    if existing_cards_text.endswith(","):
        existing_cards_text = existing_cards_text[:-1]

    # Serialize new cards to formatted JS objects
    new_cards_json = []
    for card in PRACTICE_STOMA_21_22:
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

    print(f"Successfully added Batch 21-22 (6 cards). Total in file now updated.")

if __name__ == "__main__":
    main()
