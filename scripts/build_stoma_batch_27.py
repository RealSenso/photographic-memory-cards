#!/usr/bin/env python3
"""
Builder script for StoMA Practice Cards: Batch 14 (Topic 27 - FINAL StoMA Topic)
Topic 27: Continuous-Time Markov Chains (Cards 32791, 32792, 32793)
"""

import json
import os
import re

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRACTICE_FILE = os.path.join(REPO_DIR, "practice_stoma.js")

PRACTICE_STOMA_27 = [
    # =========================================================================
    # TOPIC 27: Continuous-Time Markov Chains (CTMC)
    # =========================================================================
    {
        "id": 32791,
        "subject": "StoMA",
        "topicId": "27_Continuous_Time_Markov_Chains",
        "topicTitle": "27 · Continuous-Time Markov Chains (CTMC)",
        "title": "2-State Machine Availability via Kolmogorov Forward Equations (IISc Midterm / MIT 6.262)",
        "kind2": "pyq",
        "source": "IISc Midterm / MIT 6.262 Discrete Stochastic Processes",
        "marks": "[8 Marks]",
        "question": """<p>A machine alternates between an operational state (state 1) and a broken state (state 2). While operational, failure occurs with transition rate $\\lambda > 0$. While broken, repair completes with transition rate $\\mu > 0$.</p>
<p><span class="part">(a)</span> Write down the infinitesimal generator matrix $Q$ of the Continuous-Time Markov Chain (CTMC).</p>
<p><span class="part">(b)</span> Set up the <strong>Kolmogorov Forward Differential Equation</strong> for $P_{11}(t) = \\mathbb{P}(X(t) = 1 \\mid X(0) = 1)$ and solve it analytically subject to $P_{11}(0) = 1$.</p>
<p><span class="part">(c)</span> Compute the asymptotic availability $A(\\infty) = \\lim_{t \\to \\infty} P_{11}(t)$ and verify that it matches the stationary distribution $\\pi$ obtained from $\\boldsymbol{\\pi}^\\top Q = \\mathbf{0}^\\top$.</p>""",
        "solution": """<p><span class="part">Part (a): Infinitesimal Generator Matrix $Q$</span><br>
From state 1: transitions to state 2 at rate $\\lambda \\implies q_{12} = \\lambda, q_{11} = -\\lambda$.<br>
From state 2: transitions to state 1 at rate $\\mu \\implies q_{21} = \\mu, q_{22} = -\\mu$.<br>
All row sums must equal zero ($\sum_j q_{ij} = 0$):
<span class="ans">$$Q = \\begin{pmatrix} -\\lambda & \\lambda \\\\ \\mu & -\\mu \\end{pmatrix}$$</span></p>

<p><span class="part">Part (b): Kolmogorov Forward Equation & Solution</span><br>
The Kolmogorov forward matrix equation is $P'(t) = P(t)Q$. For the $(1, 1)$ entry:
$$P'_{11}(t) = P_{11}(t) q_{11} + P_{12}(t) q_{21} = -\\lambda P_{11}(t) + \\mu P_{12}(t)$$
Using conservation of total probability $P_{11}(t) + P_{12}(t) = 1 \\implies P_{12}(t) = 1 - P_{11}(t)$:
$$P'_{11}(t) = -\\lambda P_{11}(t) + \\mu(1 - P_{11}(t)) = \\mu - (\\lambda + \\mu)P_{11}(t)$$
Rewriting as a first-order linear ODE:
$$\\frac{d P_{11}(t)}{dt} + (\\lambda + \\mu) P_{11}(t) = \\mu$$
Multiplying by integrating factor $e^{(\\lambda + \\mu)t}$:
$$\\frac{d}{dt}\\left[ e^{(\\lambda + \\mu)t} P_{11}(t) \\right] = \\mu e^{(\\lambda + \\mu)t}$$
Integrating both sides:
$$e^{(\\lambda + \\mu)t} P_{11}(t) = \\frac{\\mu}{\\lambda + \\mu} e^{(\\lambda + \\mu)t} + C \\implies P_{11}(t) = \\frac{\\mu}{\\lambda + \\mu} + C e^{-(\\lambda + \\mu)t}$$
Applying initial condition $P_{11}(0) = 1$:
$$1 = \\frac{\\mu}{\\lambda + \\mu} + C \\implies C = 1 - \\frac{\\mu}{\\lambda + \\mu} = \\frac{\\lambda}{\\lambda + \\mu}$$
Therefore:
<span class="ans">$$P_{11}(t) = \\frac{\\mu}{\\lambda + \\mu} + \\frac{\\lambda}{\\lambda + \\mu} e^{-(\\lambda + \\mu)t}$$</span>
And $P_{12}(t) = 1 - P_{11}(t) = \\frac{\\lambda}{\\lambda + \\mu} - \\frac{\\lambda}{\\lambda + \\mu} e^{-(\\lambda + \\mu)t}$.</p>

<p><span class="part">Part (c): Limiting Availability & Stationary Balance</span><br>
1. <strong>Asymptotic limit:</strong>
$$\\lim_{t \\to \\infty} P_{11}(t) = \\frac{\\mu}{\\lambda + \\mu} + 0 = <span class=\"ans\">\\frac{\\mu}{\\lambda + \\mu}</span>$$
2. <strong>Verification via global balance $\\boldsymbol{\\pi}^\\top Q = \\mathbf{0}^\\top$:</strong>
$$\\begin{pmatrix} \\pi_1 & \\pi_2 \\end{pmatrix} \\begin{pmatrix} -\\lambda & \\lambda \\\\ \\mu & -\\mu \\end{pmatrix} = \\begin{pmatrix} 0 & 0 \\end{pmatrix} \\implies -\\lambda \\pi_1 + \\mu \\pi_2 = 0 \\implies \\pi_2 = \\frac{\\lambda}{\\mu} \\pi_1$$
Normalizing with $\\pi_1 + \\pi_2 = 1$:
$$\\pi_1\\left(1 + \\frac{\\lambda}{\\mu}\\right) = 1 \\implies \\pi_1 = \\frac{\\mu}{\\lambda + \\mu}, \\quad \\pi_2 = \\frac{\\lambda}{\\lambda + \\mu}$$
<span class=\"ans\">The transient probability $P_{11}(t)$ exponentially converges to the stationary probability $\\pi_1 = \\frac{\\mu}{\\lambda + \\mu}$ at spectral gap rate $\\lambda + \\mu$.</span></p>""",
        "takeaway": "Kolmogorov forward equations $P'(t) = P(t)Q$ describe CTMC transient dynamics. For the two-state chain, $P_{11}(t) = \\pi_1 + (1-\\pi_1)e^{-(\\lambda+\\mu)t}$, showing exponential relaxation to steady-state availability at rate $\\lambda+\\mu$."
    },
    {
        "id": 32792,
        "subject": "StoMA",
        "topicId": "27_Continuous_Time_Markov_Chains",
        "topicTitle": "27 · Continuous-Time Markov Chains (CTMC)",
        "title": "Continuous-Time $M/M/c$ Multi-Server Queue & Erlang C (IIT Delhi / Stanford MS&E 220)",
        "kind2": "university",
        "source": "IIT Delhi / Stanford MS&E 220 Queueing Theory",
        "marks": "[8 Marks]",
        "question": """<p>Consider an $M/M/c$ queuing system with arrival rate $\\lambda$ and $c$ identical servers, each providing independent exponentially distributed service with rate $\\mu$. When $k$ customers are in the system, service proceeds at aggregate rate $\\mu_k = \\min(k, c)\\mu$. Assume traffic intensity $\\rho = \\frac{\\lambda}{c\\mu} < 1$. Let offered load be $r = \\frac{\\lambda}{\\mu} = c\\rho$.</p>
<p><span class="part">(a)</span> Write the birth-death transition rate equations for CTMC state $k$ ($k \\ge 0$).</p>
<p><span class="part">(b)</span> Derive the stationary probability distribution $\\pi_k$ in terms of $\\pi_0$ for both $k \\le c$ and $k > c$.</p>
<p><span class="part">(c)</span> State <strong>Erlang's C Formula</strong> $C(c, r) = \\mathbb{P}(\\text{Customer must wait in queue})$ in terms of $\\pi_0, c, r, \\rho$.</p>""",
        "solution": """<p><span class="part">Part (a): Birth-Death Transition Rates</span><br>
State $k$ is the total count of customers in the system (in service + waiting):
- Birth rates: $\\lambda_k = \\lambda$ for all $k \\ge 0$.
- Death rates:
$$\\mu_k = \\begin{cases} k \\mu & \\text{if } 1 \\le k \\le c \\text{ (all } k \\text{ servers busy)} \\\\ c \\mu & \\text{if } k > c \\text{ (all } c \\text{ servers saturated, remaining in queue)} \\end{cases}$$</p>

<p><span class="part">Part (b): Stationary Distribution $\\pi_k$</span><br>
By detailed balance $\\pi_k \\lambda_k = \\pi_{k+1} \\mu_{k+1}$:
1. <strong>For $0 \\le k < c$:</strong>
$$\\pi_k \\lambda = \\pi_{k+1} (k+1)\\mu \\implies \\pi_{k+1} = \\frac{\\lambda}{(k+1)\\mu} \\pi_k$$
By induction, letting $r = \\lambda / \\mu$:
<span class="ans">$$\\pi_k = \\frac{r^k}{k!} \\pi_0 = \\frac{(c\\rho)^k}{k!} \\pi_0, \\quad 0 \\le k \\le c$$</span>
2. <strong>For $k \\ge c$:</strong>
$$\\pi_k \\lambda = \\pi_{k+1} c\\mu \\implies \\pi_{k+1} = \\frac{\\lambda}{c\\mu} \\pi_k = \\rho \\pi_k$$
By geometric induction starting from $\\pi_c$:
<span class="ans">$$\\pi_k = \\rho^{k - c} \\pi_c = \\rho^{k - c} \\frac{r^c}{c!} \\pi_0 = \\frac{r^k}{c! c^{k - c}} \\pi_0, \\quad k \\ge c$$</span>
3. <strong>Normalization for $\\pi_0$:</strong>
$$\\sum_{k=0}^\\infty \\pi_k = 1 \\implies \\pi_0 = \\left[ \\sum_{k=0}^{c-1} \\frac{r^k}{k!} + \\frac{r^c}{c!} \\sum_{j=0}^\\infty \\rho^j \\right]^{-1} = \\left[ \\sum_{k=0}^{c-1} \\frac{r^k}{k!} + \\frac{r^c}{c!(1 - \\rho)} \\right]^{-1}$$</p>

<p><span class="part">Part (c): Erlang's C Formula</span><br>
An arriving customer must wait if and only if all $c$ servers are busy upon arrival ($k \\ge c$). By PASTA (Poisson Arrivals See Time Averages):
$$P_{\\text{wait}} = \\sum_{k=c}^\\infty \\pi_k = \\pi_c \\sum_{j=0}^\\infty \\rho^j = \\frac{\\pi_c}{1 - \\rho} = \\frac{r^c \\pi_0}{c!(1 - \\rho)}$$
Substituting $\\pi_0$:
<span class="ans">$$C(c, r) = \\frac{\\frac{r^c}{c!(1 - \\rho)}}{\\sum_{k=0}^{c-1} \\frac{r^k}{k!} + \\frac{r^c}{c!(1 - \\rho)}} = \\frac{\\frac{(c\\rho)^c}{c!(1 - \\rho)}}{\\sum_{k=0}^{c-1} \\frac{(c\\rho)^k}{k!} + \\frac{(c\\rho)^c}{c!(1 - \\rho)}}$$</span>
This is the celebrated <strong>Erlang C Formula</strong> governing multi-server call center waiting times.</p>""",
        "takeaway": "In the $M/M/c$ queue, states below $c$ follow Poisson-like terms $\\pi_k = \\frac{r^k}{k!}\\pi_0$, while states above $c$ decay geometrically $\\pi_k = \\rho^{k-c}\\pi_c$. Erlang C gives the exact queuing delay probability."
    },
    {
        "id": 32793,
        "subject": "StoMA",
        "topicId": "27_Continuous_Time_Markov_Chains",
        "topicTitle": "27 · Continuous-Time Markov Chains (CTMC)",
        "title": "Jensen's Uniformization (Randomization) Method (IISc Endsem / Berkeley EECS 126)",
        "kind2": "generated",
        "source": "IISc Endsem / Berkeley EECS 126 Stochastic Systems",
        "marks": "[8 Marks]",
        "question": """<p>Consider a 3-state CTMC with generator matrix:
$$Q = \\begin{pmatrix}
-3 & 2 & 1 \\\\
1 & -4 & 3 \\\\
2 & 2 & -4
\\end{pmatrix}$$</p>
<p><span class="part">(a)</span> State the principle of <strong>Uniformization (Jensen's Method)</strong>. Choose an optimal uniformization rate $\\nu$ and derive the equivalent discrete transition matrix $K = I + \\frac{1}{\\nu} Q$.</p>
<p><span class="part">(b)</span> Express the transition probability matrix $P(t) = e^{Qt}$ as an explicit Poisson mixture of powers of $K$.</p>
<p><span class="part">(c)</span> Truncate the series at $n = 2$ Poisson transitions to compute an accurate numerical approximation of $P_{11}(0.1)$.</p>""",
        "solution": """<p><span class="part">Part (a): Uniformization Rate $\\nu$ & Discrete Transition Matrix $K$</span><br>
The diagonal rates are $q_1 = 3, q_2 = 4, q_3 = 4$.
To ensure all self-transition probabilities in $K$ are non-negative ($K_{ii} = 1 - q_i/\\nu \\ge 0$), we select:
$$\\nu \\ge \\max_{i} q_i = \\max(3, 4, 4) = 4$$
Setting $\\nu = 4$:
$$K = I + \\frac{1}{\\nu} Q = \\begin{pmatrix} 1 & 0 & 0 \\\\ 0 & 1 & 0 \\\\ 0 & 0 & 1 \\end{pmatrix} + \\frac{1}{4} \\begin{pmatrix} -3 & 2 & 1 \\\\ 1 & -4 & 3 \\\\ 2 & 2 & -4 \\end{pmatrix}$$
<span class="ans">$$K = \\begin{pmatrix}
1/4 & 1/2 & 1/4 \\\\
1/4 & 0 & 3/4 \\\\
1/2 & 1/2 & 0
\\end{pmatrix}$$</span>
Check: $K_{ij} \\ge 0$ for all $i, j$, and row sums $\\sum_j K_{ij} = 1$. $K$ is a valid DTMC transition matrix with virtual self-transitions.</p>

<p><span class="part">Part (b): Poisson Mixture Representation</span><br>
Since $Q = \\nu(K - I)$ and $\\nu K$ commutes with $-\\nu I$:
$$P(t) = e^{Qt} = e^{\\nu t(K - I)} = e^{-\\nu t} e^{\\nu t K} = e^{-\\nu t} \\sum_{n=0}^\\infty \\frac{(\\nu t)^n}{n!} K^n$$
<span class="ans">$$P(t) = \\sum_{n=0}^\\infty \\frac{(\\nu t)^n e^{-\\nu t}}{n!} K^n = e^{-4t} \\sum_{n=0}^\\infty \\frac{(4t)^n}{n!} K^n$$</span>
Physical interpretation: transitions occur according to a Poisson process with rate $\\nu = 4$, and at each Poisson tick, state transitions are governed by discrete matrix $K$.</p>

<p><span class="part">Part (c): Numerical Approximation for $P_{11}(0.1)$</span><br>
For $t = 0.1$: $\\nu t = 4 \\times 0.1 = 0.4$.
Poisson weights: $e^{-0.4} \\approx 0.67032$.
1. <strong>$n = 0$:</strong> $K^0 = I \\implies K_{11}^0 = 1$.
$$\\text{Weight: } e^{-0.4} \\approx 0.67032$$
2. <strong>$n = 1$:</strong> $K_{11}^1 = 1/4 = 0.25$.
$$\\text{Weight: } (0.4) e^{-0.4} \\approx 0.4 \\times 0.67032 = 0.26813$$
3. <strong>$n = 2$:</strong> Compute entry $(K^2)_{11}$ (dot product of row 1 and column 1 of $K$):
$$(K^2)_{11} = K_{11}K_{11} + K_{12}K_{21} + K_{13}K_{31} = \\left(\\frac{1}{4}\\right)\\left(\\frac{1}{4}\\right) + \\left(\\frac{1}{2}\\right)\\left(\\frac{1}{4}\\right) + \\left(\\frac{1}{4}\\right)\\left(\\frac{1}{2}\\right) = \\frac{1}{16} + \\frac{1}{8} + \\frac{1}{8} = \\frac{5}{16} = 0.3125$$
$$\\text{Weight: } \\frac{(0.4)^2}{2!} e^{-0.4} = 0.08 \\times 0.67032 \\approx 0.05363$$
Summing the truncated terms:
$$P_{11}(0.1) \\approx e^{-0.4}\\left[ 1 \\cdot (1) + 0.4 \\cdot (0.25) + \\frac{0.16}{2} \\cdot (0.3125) \\right] = 0.67032 \\left[ 1 + 0.10 + 0.025 \\right] = 0.67032 \\times 1.125$$
<span class=\"ans\">$$P_{11}(0.1) \\approx 0.75411 \\text{ (75.41%)}$$</span>
(The remaining tail error $\\sum_{n=3}^\\infty \\frac{(0.4)^n e^{-0.4}}{n!} \\le 0.0079$ is under 0.8%).</p>""",
        "takeaway": "Uniformization represents continuous-time dynamics $e^{Qt}$ as a Poisson-weighted sum $\\sum_{n=0}^\\infty \\frac{(\\nu t)^n e^{-\\nu t}}{n!} K^n$ where $K = I + Q/\\nu$. This avoids matrix ODE integration and enables stable, numerically exact CTMC computation."
    }
]

def main():
    with open(PRACTICE_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    if "32791" in content:
        print("Batch 27 already present in practice_stoma.js!")
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
    for card in PRACTICE_STOMA_27:
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

    print("Successfully added Batch 27 (3 cards). Total in file now updated.")

if __name__ == "__main__":
    main()
