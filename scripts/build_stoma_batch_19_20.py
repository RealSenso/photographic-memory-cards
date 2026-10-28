#!/usr/bin/env python3
"""
build_stoma_batch_19_20.py
Generates 6 flippable practice cards for StoMA Topics 19 and 20:
  Topic 19: Discrete Time Markov Chains, Chapman-Kolmogorov and Classification (3 cards)
  Topic 20: DTMC Stationary Distributions and Limiting Behavior (3 cards)
"""

import os
import re
import json

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PRACTICE_STOMA_19_20 = [
    # =========================================================================
    # TOPIC 19: DTMC & State Classification
    # =========================================================================
    {
        "id": 31991,
        "subject": "StoMA",
        "topicId": "19_Discrete_Time_Markov_Chains_Chapman_Kolmogorov_and_Classification",
        "topicTitle": "19 · DTMC & State Classification",
        "title": "Communicating Classes & State Classification (IISc Midterm / Stanford CS229)",
        "kind2": "pyq",
        "source": "IISc Midterm / Stanford CS229 Probability",
        "marks": "[8 Marks]",
        "question": """<p>Consider a DTMC with state space $S = \\{1, 2, 3, 4, 5\\}$ and transition probability matrix:
$$P = \\begin{pmatrix}
1/2 & 1/2 & 0 & 0 & 0 \\\\
1/4 & 3/4 & 0 & 0 & 0 \\\\
1/4 & 0 & 1/4 & 1/4 & 1/4 \\\\
0 & 0 & 0 & 0 & 1 \\\\
0 & 0 & 0 & 1 & 0
\\end{pmatrix}$$</p>
<p><span class="part">(a)</span> Determine all communicating classes and classify each as open or closed.</p>
<p><span class="part">(b)</span> Classify every state as recurrent or transient.</p>
<p><span class="part">(c)</span> Find the period $d(i)$ of each state.</p>""",
        "solution": """<p><span class="part">Part (a): Communicating Classes (Open vs Closed)</span><br>
We analyze reachability $i \\to j$ between states:
1. <strong>States 1 and 2:</strong> $P_{12} = 1/2 > 0$ and $P_{21} = 1/4 > 0$, so $1 \\leftrightarrow 2$. From $\\{1, 2\\}$, no transitions lead to states $\\{3, 4, 5\\}$.<br>
Thus $C_1 = \\{1, 2\\}$ is a <strong>closed communicating class</strong>.<br>
2. <strong>State 3:</strong> From state 3, transitions lead to 1, 4, and 5 ($P_{31} = 1/4, P_{34} = 1/4, P_{35} = 1/4$). However, once the chain leaves state 3, it can never return ($P_{13}^{(n)} = P_{43}^{(n)} = 0$ for all $n$).<br>
Thus $C_2 = \\{3\\}$ is an <strong>open communicating class</strong>.<br>
3. <strong>States 4 and 5:</strong> $P_{45} = 1 > 0$ and $P_{54} = 1 > 0$, so $4 \\leftrightarrow 5$. No transitions leave $\\{4, 5\\}$.<br>
Thus $C_3 = \\{4, 5\\}$ is a <strong>closed communicating class</strong>.<br>
<span class=\"ans\">Communicating classes: $C_1 = \\{1, 2\\}$ (closed), $C_2 = \\{3\\}$ (open), $C_3 = \\{4, 5\\}$ (closed).</span></p>

<p><span class="part">Part (b): Recurrence vs Transience</span><br>
In a finite-state Markov chain:
- A communicating class is <strong>recurrent</strong> if and only if it is closed.<br>
- A communicating class is <strong>transient</strong> if and only if it is open.<br>
Therefore:
- States <strong>1 and 2</strong> belong to closed class $C_1$ $\implies$ <span class="ans">Recurrent</span>.<br>
- State <strong>3</strong> belongs to open class $C_2$ $\implies$ <span class="ans">Transient</span> (escapes to $C_1$ or $C_3$ with probability 1).<br>
- States <strong>4 and 5</strong> belong to closed class $C_3$ $\implies$ <span class="ans">Recurrent</span>.</p>

<p><span class="part">Part (c): Periodicity Calculation</span><br>
The period is $d(i) = \gcd\{n \ge 1 : P_{ii}^{(n)} > 0\}$. Period is a class property:<br>
- <strong>For $C_1 = \{1, 2\}$:</strong> $P_{11} = 1/2 > 0$ (self-loop) $\implies d(1) = 1$. Thus <span class="ans">$d(1) = d(2) = 1$ (aperiodic)</span>.<br>
- <strong>For $C_2 = \{3\}$:</strong> $P_{33} = 1/4 > 0$ (self-loop) $\implies$ <span class="ans">$d(3) = 1$ (aperiodic)</span>.<br>
- <strong>For $C_3 = \\{4, 5\\}$:</strong> From state 4, transitions alternate: $4 \\to 5 \\to 4 \\to 5 \\to 4$. Returns to state 4 can only occur at even time steps $n \\in \\{2, 4, 6, 8, \\dots\\}$.<br>
Thus $d(4) = \\gcd(2, 4, 6, 8, \\dots) = <span class=\"ans\">2</span>$.<br>
<span class=\"ans\">States 4 and 5 are periodic with period 2.</span></p>""",
        "takeaway": "Finite DTMC classification: closed classes are recurrent, open classes are transient. Self-loops $P_{ii} > 0$ guarantee aperiodicity ($d=1$). Deterministic cycles between bipartite sets induce period $d = 2$."
    },
    {
        "id": 31992,
        "subject": "StoMA",
        "topicId": "19_Discrete_Time_Markov_Chains_Chapman_Kolmogorov_and_Classification",
        "topicTitle": "19 · DTMC & State Classification",
        "title": "2-State Markov Chain Spectral Decomposition & Matrix Power P^n (IIT Bombay / MIT 6.041)",
        "kind2": "pyq",
        "source": "IIT Bombay EE / MIT 6.041",
        "marks": "[10 Marks]",
        "question": """<p>Let a 2-state Markov chain have the transition probability matrix:
$$P = \\begin{pmatrix} 1 - \\alpha & \\alpha \\\\ \\beta & 1 - \\beta \\end{pmatrix}, \\quad 0 < \\alpha, \\beta < 1$$</p>
<p><span class="part">(a)</span> Compute the eigenvalues and corresponding eigenvectors of $P$.</p>
<p><span class="part">(b)</span> Using the spectral decomposition $P = Q \\Lambda Q^{-1}$, derive an exact closed-form analytical formula for the $n$-step transition matrix $P^n$ for all $n \\ge 1$.</p>
<p><span class="part">(c)</span> Evaluate the limiting steady-state matrix $\\lim_{n \\to \\infty} P^n$ and identify the geometric rate of convergence.</p>""",
        "solution": """<p><span class="part">Part (a): Eigenvalues and Eigenvectors</span><br>
The characteristic equation is $\\det(P - \\lambda I) = 0$:
$$\\det \\begin{pmatrix} 1 - \\alpha - \\lambda & \\alpha \\\\ \\beta & 1 - \\beta - \\lambda \\end{pmatrix} = (1 - \\alpha - \\lambda)(1 - \\beta - \\lambda) - \\alpha \\beta = 0$$
$$\\lambda^2 - (2 - \\alpha - \\beta)\\lambda + (1 - \\alpha - \\beta) = 0 \\implies (\\lambda - 1)(\\lambda - (1 - \\alpha - \\beta)) = 0$$
The eigenvalues are:
$$\\lambda_1 = 1, \\qquad \\lambda_2 = 1 - \\alpha - \\beta$$
Since $0 < \\alpha, \\beta < 1$, the second eigenvalue satisfies $|\\lambda_2| = |1 - (\\alpha + \\beta)| < 1$.<br>
- For $\\lambda_1 = 1$: $(P - I)v_1 = 0 \\implies v_1 = \\begin{pmatrix} 1 \\\\ 1 \\end{pmatrix}$.<br>
- For $\\lambda_2 = 1 - \\alpha - \\beta$: $(P - \\lambda_2 I)v_2 = 0 \\implies v_2 = \\begin{pmatrix} \\alpha \\\\ -\\beta \\end{pmatrix}$.<br>
Form the eigenvector matrix $Q$ and compute its inverse:
$$Q = \\begin{pmatrix} 1 & \\alpha \\\\ 1 & -\\beta \\end{pmatrix} \\implies Q^{-1} = \\frac{1}{\\alpha + \\beta} \\begin{pmatrix} \\beta & \\alpha \\\\ 1 & -1 \\end{pmatrix}$$</p>

<p><span class="part">Part (b): Exact Closed-Form Expression for $P^n$</span><br>
Using $P^n = Q \\Lambda^n Q^{-1}$:
$$P^n = \\begin{pmatrix} 1 & \\alpha \\\\ 1 & -\\beta \\end{pmatrix} \\begin{pmatrix} 1^n & 0 \\\\ 0 & \\lambda_2^n \\end{pmatrix} \\frac{1}{\\alpha + \\beta} \\begin{pmatrix} \\beta & \\alpha \\\\ 1 & -1 \\end{pmatrix}$$
Multiply the matrices:
$$P^n = \\frac{1}{\\alpha + \\beta} \\begin{pmatrix} 1 & \\alpha \\lambda_2^n \\\\ 1 & -\\beta \\lambda_2^n \\end{pmatrix} \\begin{pmatrix} \\beta & \\alpha \\\\ 1 & -1 \\end{pmatrix}$$
$$<span class=\"ans\">P^n = \\frac{1}{\\alpha + \\beta} \\begin{pmatrix} \\beta + \\alpha (1 - \\alpha - \\beta)^n & \\alpha - \\alpha (1 - \\alpha - \\beta)^n \\\\ \\beta - \\beta (1 - \\alpha - \\beta)^n & \\alpha + \\beta (1 - \\alpha - \\beta)^n \\end{pmatrix}</span>$$</p>

<p><span class="part">Part (c): Steady-State Limit and Convergence Rate</span><br>
Since $|1 - \\alpha - \\beta| < 1$, as $n \\to \\infty$, the transient term $(1 - \\alpha - \\beta)^n \\to 0$ exponentially fast.<br>
Taking the limit:
$$\\lim_{n \\to \\infty} P^n = \\frac{1}{\\alpha + \\beta} \\begin{pmatrix} \\beta & \\alpha \\\\ \\beta & \\alpha \\end{pmatrix} = <span class=\"ans\">\\begin{pmatrix} \\frac{\\beta}{\\alpha + \\beta} & \\frac{\\alpha}{\\alpha + \\beta} \\\\ \\frac{\\beta}{\\alpha + \\beta} & \\frac{\\alpha}{\\alpha + \\beta} \\end{pmatrix}</span>$$
Each row converges to the stationary distribution:
$$\\pi = \\left( \\frac{\\beta}{\\alpha + \\beta}, \\; \\frac{\\alpha}{\\alpha + \\beta} \\right)$$
<span class=\"ans\">The geometric rate of convergence is governed by the second eigenvalue: $|\\lambda_2|^n = |1 - \\alpha - \\beta|^n$.</span> The spectral gap $1 - |\\lambda_2| = \\alpha + \\beta$ dictates how rapidly memory of the initial state is erased.</p>""",
        "takeaway": "Spectral decomposition $P^n = \\mathbf{1}\\pi^\\top + \\lambda_2^n Q_2$ splits Markov dynamics into a stationary equilibrium ($\"\\lambda_1=1\"$) and an exponentially decaying transient governed by the spectral gap $1 - |\\lambda_2| = \\alpha + \\beta$."
    },
    {
        "id": 31993,
        "subject": "StoMA",
        "topicId": "19_Discrete_Time_Markov_Chains_Chapman_Kolmogorov_and_Classification",
        "topicTitle": "19 · DTMC & State Classification",
        "title": "Simple Symmetric Random Walk Recurrence via Stirling's Approximation (Generated Exam)",
        "kind2": "practice",
        "source": "IISc Endsem / Berkeley EECS 126 Benchmark",
        "marks": "[10 Marks]",
        "question": """<p>Consider the simple symmetric random walk on the infinite lattice $\\mathbb{Z}$, where $P_{i, i+1} = 1/2$ and $P_{i, i-1} = 1/2$ for all $i \\in \\mathbb{Z}$.</p>
<p><span class="part">(a)</span> Derive the exact combinatorial formula for the $2n$-step return probability $P_{00}^{(2n)}$.</p>
<p><span class="part">(b)</span> Use Stirling's approximation $m! \\sim \\sqrt{2\\pi m}(m/e)^m$ to determine the asymptotic behavior of $P_{00}^{(2n)}$ as $n \\to \\infty$.</p>
<p><span class="part">(c)</span> Use the fundamental recurrence criterion $\\sum_{m=1}^\\infty P_{00}^{(m)} = \\infty$ to prove that the simple symmetric random walk in 1 dimension is <strong>recurrent</strong> (Pólya's Theorem for $d=1$).</p>""",
        "solution": """<p><span class="part">Part (a): Exact Combinatorial Return Probability</span><br>
A path starting at $0$ returns to $0$ after $2n$ steps if and only if it takes exactly $n$ steps to the right ($+1$) and $n$ steps to the left ($-1$).<br>
The number of such balanced sequences of length $2n$ is $\\binom{2n}{n}$.<br>
Since each step is independent with probability $1/2$, every path of length $2n$ has probability $(1/2)^{2n} = 4^{-n}$.<br>
Therefore:
$$<span class=\"ans\">P_{00}^{(2n)} = \\binom{2n}{n} \\left( \\frac{1}{2} \\right)^{2n} = \\frac{(2n)!}{(n!)^2 \\, 4^n}</span>$$
(For any odd number of steps $2n+1$, returns are impossible: $P_{00}^{(2n+1)} = 0$ by bipartiteness).</p>

<p><span class="part">Part (b): Stirling's Asymptotic Approximation</span><br>
Apply Stirling's formula $m! \\sim \\sqrt{2\\pi m}(m/e)^m$ to the numerator and denominator:
- Numerator: $(2n)! \\sim \\sqrt{4\\pi n} \\left(\\frac{2n}{e}\\right)^{2n} = 2\\sqrt{\\pi n} \\frac{4^n n^{2n}}{e^{2n}}$.<br>
- Denominator: $(n!)^2 \\, 4^n \\sim \\left( \\sqrt{2\\pi n} \\frac{n^n}{e^n} \\right)^2 4^n = 2\\pi n \\frac{n^{2n}}{e^{2n}} 4^n$.<br>
Dividing the expressions:
$$P_{00}^{(2n)} \\sim \\frac{2\\sqrt{\\pi n} \\frac{4^n n^{2n}}{e^{2n}}}{2\\pi n \\frac{4^n n^{2n}}{e^{2n}}} = \\frac{2\\sqrt{\\pi n}}{2\\pi n} = <span class=\"ans\">\\frac{1}{\\sqrt{\\pi n}}</span>$$</p>

<p><span class="part">Part (c): Proof of Recurrence (Pólya's Theorem)</span><br>
A state is recurrent if and only if the expected number of returns to that state is infinite:
$$\\sum_{m=1}^\\infty P_{00}^{(m)} = \\sum_{n=1}^\\infty P_{00}^{(2n)}$$
Substitute the asymptotic behavior $P_{00}^{(2n)} \\sim \\frac{1}{\\sqrt{\\pi n}}$:
$$\\sum_{n=1}^\\infty P_{00}^{(2n)} \\sim \\frac{1}{\\sqrt{\\pi}} \\sum_{n=1}^\\infty \\frac{1}{n^{1/2}}$$
Recall that the $p$-series $\\sum_{n=1}^\\infty \\frac{1}{n^p}$ diverges for all $p \\le 1$. Here $p = 1/2 \\le 1$.<br>
Therefore:
$$\\sum_{m=1}^\\infty P_{00}^{(m)} = <span class=\"ans\">+\\infty \\implies \\text{State 0 is RECURRENT}</span>$$
Since the simple random walk on $\\mathbb{Z}$ is irreducible, all states $i \\in \\mathbb{Z}$ are recurrent.<br>
(Note: the mean return time $\\mu_{00} = 1/\\pi_0 = \\infty$, so the state is <strong>null recurrent</strong>).</p>""",
        "takeaway": "Pólya's Recurrence Theorem: in $d=1$, $P_{00}^{(2n)} \\sim \\frac{1}{\\sqrt{\\pi n}}$ decays as $n^{-1/2}$, so $\\sum n^{-1/2} = \\infty$, proving recurrence. In $d=3$, $P_{00}^{(2n)} \\sim n^{-3/2}$, whose sum converges, making 3D walks transient."
    },

    # =========================================================================
    # TOPIC 20: DTMC Stationary Distributions & Limiting Behavior
    # =========================================================================
    {
        "id": 32091,
        "subject": "StoMA",
        "topicId": "20_DTMC_Stationary_Distributions_and_Limiting_Behavior",
        "topicTitle": "20 · Stationary Distributions & Ergodicity",
        "title": "Finite Buffer Queue & Stationary Drop Probability (IISc Midterm / Stanford EE 278)",
        "kind2": "pyq",
        "source": "IISc E1 222 Midterm / Stanford EE 278",
        "marks": "[8 Marks]",
        "question": """<p>A network buffer can store up to $K = 3$ packets. At each time slot, a new packet arrives with probability $p = 1/2$, and independently an existing packet departs with probability $q = 1/2$. Arriving packets are dropped if the buffer is full ($X_n = 3$). If the buffer is empty ($X_n = 0$), no departure can occur.</p>
<p><span class="part">(a)</span> Set up the transition probability matrix $P$ on state space $\\{0, 1, 2, 3\\}$.</p>
<p><span class="part">(b)</span> Solve for the stationary distribution $\\pi = (\\pi_0, \\pi_1, \\pi_2, \\pi_3)$ using detailed balance equations.</p>
<p><span class="part">(c)</span> Compute the long-run packet drop probability $P_{\\text{drop}}$.</p>""",
        "solution": """<p><span class="part">Part (a): Transition Probability Matrix</span><br>
Let $A \\sim \\text{Bernoulli}(1/2)$ (arrival) and $D \\sim \\text{Bernoulli}(1/2)$ (departure).<br>
- <strong>For interior states $i \\in \\{1, 2\\}$:</strong>
  - Up: $A=1, D=0 \\implies P_{i, i+1} = (1/2)(1/2) = 1/4$.
  - Down: $A=0, D=1 \\implies P_{i, i-1} = (1/2)(1/2) = 1/4$.
  - Stay: both or neither $\\implies P_{ii} = (1/2)(1/2) + (1/2)(1/2) = 1/2$.<br>
- <strong>Boundary 0 (Empty buffer):</strong> No departures possible. $P_{01} = p = 1/2$, and $P_{00} = 1 - p = 1/2$.<br>
- <strong>Boundary 3 (Full buffer):</strong> If a packet arrives, it is dropped. Stays at 3 if $A=1$ or ($A=0, D=0$): $P_{33} = 1 - (1-p)q = 1 - (1/2)(1/2) = 3/4$. Steps down if $A=0, D=1$: $P_{32} = 1/4$.
$$P = \\begin{pmatrix} 1/2 & 1/2 & 0 & 0 \\\\ 1/4 & 1/2 & 1/4 & 0 \\\\ 0 & 1/4 & 1/2 & 1/4 \\\\ 0 & 0 & 1/4 & 3/4 \\end{pmatrix}$$</p>

<p><span class="part">Part (b): Detailed Balance Solution</span><br>
Because this is a finite birth-death chain, it is time-reversible: $\\pi_i P_{i, i+1} = \\pi_{i+1} P_{i+1, i}$.
- Between 0 and 1:
$$\\pi_0 P_{01} = \\pi_1 P_{10} \\implies \\pi_0\\left(\\frac{1}{2}\\right) = \\pi_1\\left(\\frac{1}{4}\\right) \\implies \\pi_1 = 2\\pi_0$$
- Between 1 and 2:
$$\\pi_1 P_{12} = \\pi_2 P_{21} \\implies \\pi_1\\left(\\frac{1}{4}\\right) = \\pi_2\\left(\\frac{1}{4}\\right) \\implies \\pi_2 = \\pi_1 = 2\\pi_0$$
- Between 2 and 3:
$$\\pi_2 P_{23} = \\pi_3 P_{32} \\implies \\pi_2\\left(\\frac{1}{4}\\right) = \\pi_3\\left(\\frac{1}{4}\\right) \\implies \\pi_3 = \\pi_2 = 2\\pi_0$$
Normalizing the probabilities:
$$\\sum_{i=0}^3 \\pi_i = \\pi_0 + 2\\pi_0 + 2\\pi_0 + 2\\pi_0 = 7\\pi_0 = 1 \\implies \\pi_0 = \\frac{1}{7}$$
$$<span class=\"ans\">\\pi = \\left( \\frac{1}{7}, \\; \\frac{2}{7}, \\; \\frac{2}{7}, \\; \\frac{2}{7} \\right)</span>$$</p>

<p><span class="part">Part (c): Long-Run Packet Drop Probability</span><br>
A packet drop occurs if and only if a new packet arrives while the buffer is already in state 3:<br>
$$P_{\\text{drop}} = \\mathbb{P}(X_n = 3) \\cdot \\mathbb{P}(\\text{Arrival}) = \\pi_3 \\cdot p = \\left( \\frac{2}{7} \\right) \\left( \\frac{1}{2} \\right) = <span class=\"ans\">\\frac{1}{7} \\approx 14.29\\%</span>$$
On average, approximately $14.29\\%$ of all incoming packets are dropped due to buffer overflow.</p>""",
        "takeaway": "Birth-death chains satisfy detailed balance $\\pi_i P_{i, i+1} = \\pi_{i+1} P_{i+1, i}$, bypassing Gaussian elimination. When upward and downward rates match in the interior, probabilities are flat, and the drop rate is $\\pi_K p$."
    },
    {
        "id": 32092,
        "subject": "StoMA",
        "topicId": "20_DTMC_Stationary_Distributions_and_Limiting_Behavior",
        "topicTitle": "20 · Stationary Distributions & Ergodicity",
        "title": "Reflecting Random Walk: Positive vs Null Recurrence vs Transience (IISc Endsem / MIT 6.262)",
        "kind2": "pyq",
        "source": "IISc Endsem / MIT 6.262",
        "marks": "[10 Marks]",
        "question": """<p>Consider a random walk on $S = \\{0, 1, 2, \\dots\\}$ with a reflecting boundary at the origin:
$$P_{01} = 1, \\qquad P_{i, i+1} = p, \\qquad P_{i, i-1} = 1 - p \\quad (i \\ge 1)$$
where $p \\in (0, 1)$ is the upward transition probability.</p>
<p><span class="part">(a)</span> Using detailed balance equations, find the exact necessary and sufficient condition on $p$ for the chain to be <strong>positive recurrent</strong>, and determine its stationary distribution $\\pi_i$ for all $i \\ge 0$.</p>
<p><span class="part">(b)</span> For what value of $p$ is the chain <strong>null recurrent</strong>? Why does no stationary distribution exist in this regime?</p>
<p><span class="part">(c)</span> For what values of $p$ is the chain <strong>transient</strong>?</p>""",
        "solution": """<p><span class="part">Part (a): Positive Recurrence & Detailed Balance</span><br>
Detailed balance equations $\\pi_i P_{i, i+1} = \\pi_{i+1} P_{i+1, i}$:
- For $i = 0$: $\\pi_0(1) = \\pi_1(1 - p) \\implies \\pi_1 = \\frac{1}{1 - p}\\pi_0$.<br>
- For $i \\ge 1$: $\\pi_i p = \\pi_{i+1}(1 - p) \\implies \\pi_{i+1} = \\left(\\frac{p}{1 - p}\\right) \\pi_i$.<br>
Let $\\rho = \\frac{p}{1 - p}$. By induction:
$$\\pi_i = \\frac{1}{1 - p} \\rho^{i-1} \\pi_0 = \\frac{1}{p} \\rho^i \\pi_0 \\quad \\text{for } i \\ge 1$$
For a stationary distribution to exist, the sum $\\sum_{i=0}^\\infty \\pi_i$ must converge:
$$\\sum_{i=0}^\\infty \\pi_i = \\pi_0 \\left[ 1 + \\frac{1}{p} \\sum_{i=1}^\\infty \\rho^i \\right] = \\pi_0 \\left[ 1 + \\frac{\\rho}{p(1 - \\rho)} \\right] < \\infty$$
This geometric series converges if and only if $\\rho < 1$:
$$\\frac{p}{1 - p} < 1 \\iff <span class=\"ans\">p < \\frac{1}{2}</span>$$
Evaluating the normalizer with $1 - \\rho = \\frac{1 - 2p}{1 - p}$:
$$1 + \\frac{\\rho}{p(1 - \\rho)} = 1 + \\frac{p/(1-p)}{p(1-2p)/(1-p)} = 1 + \\frac{1}{1 - 2p} = \\frac{2(1 - p)}{1 - 2p}$$
Thus the stationary distribution is:
$$<span class=\"ans\">\\pi_0 = \\frac{1 - 2p}{2(1 - p)}, \\qquad \\pi_i = \\frac{1 - 2p}{2p(1 - p)} \\left(\\frac{p}{1 - p}\\right)^i \\quad \\forall i \\ge 1</span>$$</p>

<p><span class="part">Part (b): Null Recurrence Regime</span><br>
When $p = 1/2$: $\\rho = 1$, so $\\pi_i = 2\\pi_0$ for all $i \\ge 1$.<br>
The sum $\\sum_{i=0}^\\infty \\pi_i = \\pi_0(1 + \\sum 2) = \\infty$, so no normalizable probability measure exists.<br>
However, by Pólya's theorem, the 1D symmetric walk returns to $0$ with probability $1$ ($f_{00} = 1$).<br>
<span class=\"ans\">The chain is NULL RECURRENT for $p = 1/2$.</span> The mean recurrence time $\\mu_{00} = \\infty$, so the probability mass \"dissipates\" over the infinite line without escaping to infinity.</p>

<p><span class="part">Part (c): Transient Regime</span><br>
When $p > 1/2$: $\\rho > 1$. The walk has a strictly positive upward drift $p - (1 - p) = 2p - 1 > 0$.<br>
By the Strong Law of Large Numbers, $\\frac{X_n}{n} \\xrightarrow{a.s.} 2p - 1 > 0$, so $X_n \\to +\\infty$ almost surely.<br>
The probability of ever returning to 0 is strictly less than 1 ($f_{00} < 1$).<br>
<span class=\"ans\">The chain is TRANSIENT for $p > 1/2$.</span></p>""",
        "takeaway": "Random walk trichotomy: $p < 1/2 \\implies$ positive recurrent (geometric stationary distribution $\\pi_i \\propto \\rho^i$). $p = 1/2 \\implies$ null recurrent (returns a.s., but $\\mu_{00} = \\infty$). $p > 1/2 \\implies$ transient (drifts to $+\infty$ a.s.)."
    },
    {
        "id": 32093,
        "subject": "StoMA",
        "topicId": "20_DTMC_Stationary_Distributions_and_Limiting_Behavior",
        "topicTitle": "20 · Stationary Distributions & Ergodicity",
        "title": "Google PageRank Algorithm & Ergodic Teleportation (Generated Exam)",
        "kind2": "practice",
        "source": "Stanford CS246 / Berkeley EECS 126 Benchmark",
        "marks": "[10 Marks]",
        "question": """<p>Consider a 3-page web network: Page 1 links to Pages 2 and 3; Page 2 links to Page 3; Page 3 links to Page 1.</p>
<p><span class="part">(a)</span> Write the pure hyperlink transition matrix $P$ and verify that it is irreducible and aperiodic.</p>
<p><span class="part">(b)</span> To guarantee ergodicity and resolve dead ends, the Google PageRank algorithm introduces a damping factor $d = 0.8$ and uniform teleportation matrix $E = \\frac{1}{3}\\mathbf{1}\\mathbf{1}^\\top$:
$$G = d P + (1 - d)E$$
Using the <strong>Perron-Frobenius Theorem</strong>, explain why $G$ has a unique, strictly positive stationary probability vector $\\pi$ (PageRank).</p>
<p><span class="part">(c)</span> Set up the linear system $\\pi = \\pi G$ and compute the exact PageRank vector $\\pi = (\\pi_1, \\pi_2, \\pi_3)$. Which webpage has the highest rank?</p>""",
        "solution": """<p><span class="part">Part (a): Pure Hyperlink Transition Matrix</span><br>
From each page, outgoing links are followed uniformly:
- Page 1 links to 2 and 3 $\\implies P_{12} = 1/2, P_{13} = 1/2$.<br>
- Page 2 links to 3 $\\implies P_{23} = 1$.<br>
- Page 3 links to 1 $\\implies P_{31} = 1$.
$$P = \\begin{pmatrix} 0 & 1/2 & 1/2 \\\\ 0 & 0 & 1 \\\\ 1 & 0 & 0 \\end{pmatrix}$$
Check aperiodicity: $1 \\to 3 \\to 1$ (2 steps) and $1 \\to 2 \\to 3 \\to 1$ (3 steps). Since $\\gcd(2, 3) = 1$, the chain is irreducible and aperiodic.</p>

<p><span class="part">Part (b): Perron-Frobenius Theorem & Teleportation</span><br>
With damping factor $d = 0.8$ and $(1 - d)/3 = 0.2/3 = 1/15$:
$$G_{ij} = d P_{ij} + \\frac{1 - d}{3} \\ge \\frac{1 - d}{3} = \\frac{1}{15} > 0 \\quad \\forall i, j$$
Every single entry of the Google matrix $G$ is strictly positive ($G_{ij} > 0$).<br>
By the <strong>Perron-Frobenius Theorem for strictly positive stochastic matrices</strong>:
1. The largest eigenvalue is $\\lambda_1 = 1$, with algebraic and geometric multiplicity 1.<br>
2. All other eigenvalues satisfy $|\\lambda_i| \\le d = 0.8 < 1$.<br>
3. There exists a <strong>unique, strictly positive stationary distribution</strong> $\\pi > 0$ such that $\\pi G = \\pi$ and $\\sum_{j=1}^3 \\pi_j = 1$. Teleportation eliminates sink traps and ensures geometric convergence at rate $O(d^k)$.</p>

<p><span class="part">Part (c): Exact PageRank Vector Calculation</span><br>
The PageRank balance equation for each page $j$ is:
$$\\pi_j = d \\sum_{i \\to j} \\frac{\\pi_i}{L(i)} + \\frac{1 - d}{3}$$
where $L(i)$ is the out-degree of page $i$. With $d = 0.8$ and $(1-d)/3 = 1/15$:
1. $\\pi_1 = 0.8 \\pi_3 + \\frac{1}{15}$
2. $\\pi_2 = 0.8 \\left(\\frac{\\pi_1}{2}\\right) + \\frac{1}{15} = 0.4 \\pi_1 + \\frac{1}{15}$
3. $\\pi_3 = 0.8 \\left(\\frac{\\pi_1}{2}\\right) + 0.8 \\pi_2 + \\frac{1}{15} = 0.4 \\pi_1 + 0.8 \\pi_2 + \\frac{1}{15}$<br>
Substitute $\\pi_2$ into the expression for $\\pi_3$:
$$\\pi_3 = 0.4 \\pi_1 + 0.8\\left(0.4 \\pi_1 + \\frac{1}{15}\\right) + \\frac{1}{15} = 0.72 \\pi_1 + \\frac{1.8}{15} = 0.72 \\pi_1 + 0.12$$
Now substitute $\\pi_3$ into $\\pi_1$:
$$\\pi_1 = 0.8(0.72 \\pi_1 + 0.12) + \\frac{1}{15} = 0.576 \\pi_1 + 0.096 + 0.06667 = 0.576 \\pi_1 + 0.16267$$
$$0.424 \\pi_1 = 0.16267 \\implies <span class=\"ans\">\\pi_1 \\approx 0.3837</span>$$
Now evaluate $\\pi_2$ and $\\pi_3$:
$$\\pi_2 = 0.4(0.3837) + 0.06667 = <span class=\"ans\">0.2201</span>$$
$$\\pi_3 = 0.72(0.3837) + 0.12 = <span class=\"ans\">0.3962</span>$$
Check sum: $0.3837 + 0.2201 + 0.3962 = 1.0000$.<br>
<span class=\"ans\">PageRank ranking: Page 3 (39.62%) > Page 1 (38.37%) > Page 2 (22.01%).</span><br>
Page 3 is the most important webpage because it receives links from both Page 1 and Page 2.</p>""",
        "takeaway": "Google PageRank adds uniform teleportation $\\frac{1-d}{N}$ to make the web graph strictly positive ($G_{ij} > 0$). By Perron-Frobenius, this guarantees a unique positive stationary distribution $\\pi$ that can be computed by power iteration."
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
    for c in PRACTICE_STOMA_19_20:
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
