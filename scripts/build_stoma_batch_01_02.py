#!/usr/bin/env python3
"""
build_stoma_batch_01_02.py
Generates 6 flippable practice cards for StoMA Topics 01 and 02:
  Topic 01: Probability Spaces, Axioms and Continuity of Probability (3 cards)
  Topic 02: Conditional Probability, Bayes' Rule and Independence (3 cards)
"""

import os
import re
import json

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PRACTICE_STOMA_01_02 = [
    # =========================================================================
    # TOPIC 01: Probability Spaces, Axioms & Continuity of Probability
    # =========================================================================
    {
        "id": 30191,
        "subject": "StoMA",
        "topicId": "01_Probability_Spaces_Axioms_and_Continuity_of_Probability",
        "topicTitle": "01 · Probability Spaces & Continuity",
        "title": "Countable Union Bound & Continuity of Measure (IISc Midterm 1)",
        "kind2": "pyq",
        "source": "IISc StoMA Midterm 1 2024 / Ross Ch 1",
        "marks": "[8 Marks]",
        "question": """<p><span class="part">(a)</span> State Kolmogorov's three axioms for a probability space $(\\Omega, \\mathcal{F}, \\mathbb{P})$.</p>
<p><span class="part">(b)</span> Let $(\\Omega, \\mathcal{F}, \\mathbb{P})$ be a probability space. Using the continuity of probability for increasing sequences of events, prove <strong>Boole's inequality</strong> (the countable union bound) for any countably infinite collection of events $\\{A_n\\}_{n=1}^\\infty \\subset \\mathcal{F}$:</p>
$$\\mathbb{P}\\left(\\bigcup_{n=1}^\\infty A_n\\right) \\le \\sum_{n=1}^\\infty \\mathbb{P}(A_n)$$""",
        "solution": """<p><span class="part">Step 1: Kolmogorov's Three Axioms</span><br>
1. <strong>Non-negativity:</strong> For every event $E \\in \\mathcal{F}$, $\\mathbb{P}(E) \\ge 0$.<br>
2. <strong>Normalization:</strong> $\\mathbb{P}(\\Omega) = 1$.<br>
3. <strong>Countable Additivity:</strong> If $\\{E_i\\}_{i=1}^\\infty$ is a sequence of pairwise disjoint events ($E_i \\cap E_j = \\emptyset$ for $i \\ne j$), then:
$$\\mathbb{P}\\left(\\bigcup_{i=1}^\\infty E_i\\right) = \\sum_{i=1}^\\infty \\mathbb{P}(E_i)$$</p>

<p><span class="part">Step 2: Construct an Increasing Sequence of Events</span><br>
For each $n \\ge 1$, define the finite partial union:
$$B_n = \\bigcup_{i=1}^n A_i$$
Clearly, $B_1 \\subseteq B_2 \\subseteq B_3 \\subseteq \\dots$ is a monotone increasing sequence of events whose limit union is:
$$\\bigcup_{n=1}^\\infty B_n = \\bigcup_{n=1}^\\infty \\left(\\bigcup_{i=1}^n A_i\\right) = \\bigcup_{i=1}^\\infty A_i$$
By the <strong>Continuity of Probability from below</strong>:
$$\\mathbb{P}\\left(\\bigcup_{i=1}^\\infty A_i\\right) = \\lim_{n \\to \\infty} \\mathbb{P}(B_n) = \\lim_{n \\to \\infty} \\mathbb{P}\\left(\\bigcup_{i=1}^n A_i\\right)$$</p>

<p><span class="part">Step 3: Finite Induction on Boole's Inequality</span><br>
For $n = 1$, $\\mathbb{P}(A_1) \\le \\mathbb{P}(A_1)$ holds trivially.<br>
Assume it holds for $n$, i.e., $\\mathbb{P}(\\bigcup_{i=1}^n A_i) \\le \\sum_{i=1}^n \\mathbb{P}(A_i)$. For $n+1$:
$$\\mathbb{P}\\left(\\bigcup_{i=1}^{n+1} A_i\\right) = \\mathbb{P}\\left( \\left(\\bigcup_{i=1}^n A_i\\right) \\cup A_{n+1} \\right) = \\mathbb{P}\\left(\\bigcup_{i=1}^n A_i\\right) + \\mathbb{P}(A_{n+1}) - \\mathbb{P}\\left(\\left(\\bigcup_{i=1}^n A_i\\right) \\cap A_{n+1}\\right)$$
Since probability is non-negative, subtracting the intersection term yields:
$$\\mathbb{P}\\left(\\bigcup_{i=1}^{n+1} A_i\\right) \\le \\mathbb{P}\\left(\\bigcup_{i=1}^n A_i\\right) + \\mathbb{P}(A_{n+1}) \\le \\sum_{i=1}^n \\mathbb{P}(A_i) + \\mathbb{P}(A_{n+1}) = \\sum_{i=1}^{n+1} \\mathbb{P}(A_i)$$</p>

<p><span class="part">Step 4: Take Limits as $n \\to \\infty$</span><br>
Taking the limit as $n \\to \\infty$ on both sides:
$$\\mathbb{P}\\left(\\bigcup_{i=1}^\\infty A_i\\right) = \\lim_{n \\to \\infty} \\mathbb{P}\\left(\\bigcup_{i=1}^n A_i\\right) \\le \\lim_{n \\to \\infty} \\sum_{i=1}^n \\mathbb{P}(A_i) = \\sum_{i=1}^\\infty \\mathbb{P}(A_i)$$
<span class="ans">Thus $\\mathbb{P}\\left(\\bigcup_{n=1}^\\infty A_n\\right) \\le \\sum_{n=1}^\\infty \\mathbb{P}(A_n)$.</span> $\\blacksquare$</p>""",
        "takeaway": "Sequential continuity from below bridges finite additivity to countable limits: $\\lim_{n\\to\\infty} \\mathbb{P}(\\bigcup_{i=1}^n A_i) = \\mathbb{P}(\\bigcup_{i=1}^\\infty A_i)$."
    },
    {
        "id": 30192,
        "subject": "StoMA",
        "topicId": "01_Probability_Spaces_Axioms_and_Continuity_of_Probability",
        "topicTitle": "01 · Probability Spaces & Continuity",
        "title": "Sequential Continuity at the Origin (MIT 6.041 / Stanford Stats 116)",
        "kind2": "pyq",
        "source": "MIT 6.041 / Stanford Stats 116",
        "marks": "[10 Marks]",
        "question": """<p><span class="part">(a)</span> Let $X$ be a non-negative random variable ($X \\ge 0$ almost surely). Use the <strong>Continuity of Probability from above</strong> to prove rigorously that:
$$\\mathbb{P}(X = 0) = \\lim_{n \\to \\infty} \\mathbb{P}\\left(X \\le \\frac{1}{n}\\right)$$</p>
<p><span class="part">(b)</span> Does the relation $\\lim_{n \\to \\infty} \\mathbb{P}(X < 1/n) = \\mathbb{P}(X = 0)$ hold if $X$ can take negative values? Justify with a counterexample.</p>""",
        "solution": """<p><span class="part">Part (a): Proof via Continuity from Above</span><br>
For each integer $n \\ge 1$, define the event:
$$B_n = \\left\\{ \\omega \\in \\Omega : X(\\omega) \\le \\frac{1}{n} \\right\\}$$
Since $\\frac{1}{n+1} < \\frac{1}{n}$, any outcome satisfying $X(\\omega) \\le \\frac{1}{n+1}$ also satisfies $X(\\omega) \\le \\frac{1}{n}$.<br>
Therefore, the sequence of events is monotone decreasing:
$$B_1 \\supseteq B_2 \\supseteq B_3 \\supseteq \\dots$$
Now consider the countable intersection of these events:
$$B = \\bigcap_{n=1}^\\infty B_n = \\left\\{ \\omega \\in \\Omega : X(\\omega) \\le \\frac{1}{n} \\text{ for all } n \\ge 1 \\right\\}$$
Because $X(\\omega) \\ge 0$, the only real number satisfying $0 \\le X(\\omega) \\le 1/n$ for every $n \\in \\mathbb{N}$ is $X(\\omega) = 0$.<br>
Hence:
$$B = \\{ \\omega \\in \\Omega : X(\\omega) = 0 \\} = \\{ X = 0 \\}$$
Since $B_n \\downarrow B$, by the <strong>Continuity of Probability for decreasing sequences</strong>:
$$\\mathbb{P}(X = 0) = \\mathbb{P}(B) = \\lim_{n \\to \\infty} \\mathbb{P}(B_n) = <span class=\"ans\">\\lim_{n \\to \\infty} \\mathbb{P}\\left(X \\le \\frac{1}{n}\\right)</span>$$</p>

<p><span class="part">Part (b): Counterexample for General $X$</span><br>
If $X$ can take strictly negative values, the assertion fails.<br>
<strong>Counterexample:</strong> Let $X$ be uniformly distributed on $[-1, 0]$, or simply $\\mathbb{P}(X = -1) = 1$.<br>
Then $\\mathbb{P}(X = 0) = 0$.<br>
However, for all $n \\ge 1$, $-1 < 1/n$, so the event $\\{X < 1/n\\}$ contains $\\{X = -1\\}$ with probability $1$:
$$\\lim_{n \\to \\infty} \\mathbb{P}\\left(X < \\frac{1}{n}\\right) = \\lim_{n \\to \\infty} 1 = 1 \\ne 0 = \\mathbb{P}(X = 0)$$
<span class=\"ans\">The non-negativity constraint $X \\ge 0$ is essential so that $\\bigcap_{n=1}^\\infty \\{X \\le 1/n\\} = \\{X = 0\\}$.</span></p>""",
        "takeaway": "Continuity from above requires nested sets $B_{n+1} \\subseteq B_n$. For $X \\ge 0$, $\\bigcap_{n=1}^\\infty [0, 1/n] = \\{0\\}$, ensuring the limit of probabilities equals the point mass at zero."
    },
    {
        "id": 30193,
        "subject": "StoMA",
        "topicId": "01_Probability_Spaces_Axioms_and_Continuity_of_Probability",
        "topicTitle": "01 · Probability Spaces & Continuity",
        "title": "Finite Additivity + Continuity at ∅ ⟺ Countable Additivity (Generated Exam)",
        "kind2": "practice",
        "source": "Berkeley EECS 126 / Master Exam Benchmark",
        "marks": "[10 Marks]",
        "question": """<p>Let $\\mathcal{F}$ be a $\\sigma$-algebra on $\\Omega$, and let $\\mathbb{P}: \\mathcal{F} \\to [0, 1]$ be a finitely additive set function with $\\mathbb{P}(\\Omega) = 1$.</p>
<p>Prove that $\\mathbb{P}$ is <strong>countably additive</strong> if and only if $\\mathbb{P}$ is <strong>continuous from above at $\\emptyset$</strong> (i.e., for any sequence $\\{A_n\\} \\subset \\mathcal{F}$ such that $A_n \\downarrow \\emptyset$, $\\lim_{n \\to \\infty} \\mathbb{P}(A_n) = 0$).</p>""",
        "solution": """<p><span class="part">Forward Direction: $(\\implies)$ Countable Additivity implies Continuity at $\\emptyset$</span><br>
Let $A_n \\downarrow \\emptyset$, meaning $A_1 \\supseteq A_2 \\supseteq A_3 \\dots$ and $\\bigcap_{n=1}^\\infty A_n = \\emptyset$.<br>
Define the disjoint ring differences $D_k = A_k \\setminus A_{k+1}$ for $k \\ge 1$.<br>
Notice that $A_1 = \\bigcup_{k=1}^\\infty D_k$, where all $D_k$ are pairwise disjoint.<br>
By countable additivity:
$$\\mathbb{P}(A_1) = \\sum_{k=1}^\\infty \\mathbb{P}(D_k) = \\lim_{n \\to \\infty} \\sum_{k=1}^{n-1} \\mathbb{P}(D_k)$$
By finite additivity on the telescope $\\bigcup_{k=1}^{n-1} D_k = A_1 \\setminus A_n$:
$$\\sum_{k=1}^{n-1} \\mathbb{P}(D_k) = \\mathbb{P}(A_1 \\setminus A_n) = \\mathbb{P}(A_1) - \\mathbb{P}(A_n)$$
Taking the limit as $n \\to \\infty$:
$$\\mathbb{P}(A_1) = \\mathbb{P}(A_1) - \\lim_{n \\to \\infty} \\mathbb{P}(A_n) \\implies <span class=\"ans\">\\lim_{n \\to \\infty} \\mathbb{P}(A_n) = 0</span>$$</p>

<p><span class="part">Reverse Direction: $(\\impliedby)$ Finite Additivity + Continuity at $\\emptyset$ implies Countable Additivity</span><br>
Let $\\{E_k\\}_{k=1}^\\infty$ be any sequence of pairwise disjoint events in $\\mathcal{F}$.<br>
Let $A = \\bigcup_{k=1}^\\infty E_k$ be their countable union.<br>
For each finite $n \\ge 1$, let $S_n = \\bigcup_{k=1}^n E_k$. By finite additivity:
$$\\mathbb{P}(S_n) = \\sum_{k=1}^n \\mathbb{P}(E_k)$$
Now define the tail remainder events:
$$R_n = A \\setminus S_n = \\bigcup_{k=n+1}^\\infty E_k$$
Notice that $R_1 \\supseteq R_2 \\supseteq R_3 \\supseteq \\dots$ is a monotone decreasing sequence.<br>
Since the events $E_k$ are pairwise disjoint, any point $\\omega \\in A$ belongs to exactly one $E_{k^*}$, so $\\omega \\notin R_n$ for all $n \\ge k^*$. Thus:
$$\\bigcap_{n=1}^\\infty R_n = \\emptyset \\quad (R_n \\downarrow \\emptyset)$$
By hypothesis (continuity from above at $\\emptyset$):
$$\\lim_{n \\to \\infty} \\mathbb{P}(R_n) = 0$$
Since $A = S_n \\cup R_n$ with $S_n \\cap R_n = \\emptyset$, finite additivity gives:
$$\\mathbb{P}(A) = \\mathbb{P}(S_n) + \\mathbb{P}(R_n) = \\sum_{k=1}^n \\mathbb{P}(E_k) + \\mathbb{P}(R_n)$$
Taking $n \\to \\infty$ on both sides:
$$\\mathbb{P}\\left(\\bigcup_{k=1}^\\infty E_k\\right) = \\lim_{n \\to \\infty} \\left( \\sum_{k=1}^n \\mathbb{P}(E_k) + \\mathbb{P}(R_n) \\right) = \\sum_{k=1}^\\infty \\mathbb{P}(E_k) + 0 = <span class=\"ans\">\\sum_{k=1}^\\infty \\mathbb{P}(E_k)</span>$$
<span class=\"ans\">Hence $\\mathbb{P}$ is countably additive.</span> $\\blacksquare$</p>""",
        "takeaway": "Kolmogorov's countable additivity axiom is logically equivalent to finite additivity combined with continuity at the empty set: $\\mathbb{P}(A_n) \\to 0$ whenever $A_n \\downarrow \\emptyset$."
    },

    # =========================================================================
    # TOPIC 02: Conditional Probability, Bayes' Rule & Independence
    # =========================================================================
    {
        "id": 30291,
        "subject": "StoMA",
        "topicId": "02_Conditional_Probability_Bayes_Rule_and_Independence",
        "topicTitle": "02 · Conditioning, Bayes & Independence",
        "title": "Rare Disease Screening & The Base Rate Fallacy (IISc Test 1)",
        "kind2": "pyq",
        "source": "IISc StoMA Test 1 / Ross Ch 1",
        "marks": "[8 Marks]",
        "question": """<p>A rare disease affects $0.1\\%$ of the population (prevalence $\\mathbb{P}(D) = 0.001$). A laboratory diagnostic test has a false positive rate of $2\\%$ ($\\mathbb{P}(T \\mid D^c) = 0.02$) and a false negative rate of $1\\%$ ($\\mathbb{P}(T^c \\mid D) = 0.01$).</p>
<p><span class="part">(a)</span> A randomly chosen person from the population tests positive ($T$). Find the exact posterior probability $\\mathbb{P}(D \\mid T)$ that the person actually has the disease.</p>
<p><span class="part">(b)</span> Suppose the person is tested a second time using an independent test of the exact same specification, and tests positive again ($T_2$). Assuming the test results are conditionally independent given disease status, compute the updated posterior probability $\\mathbb{P}(D \\mid T_1 \\cap T_2)$.</p>""",
        "solution": """<p><span class="part">Part (a): Single Positive Test</span><br>
Define events: $D$ = patient has disease, $T$ = test positive.<br>
Priors and conditional likelihoods:
- $\\mathbb{P}(D) = 0.001 \\implies \\mathbb{P}(D^c) = 0.999$
- $\\mathbb{P}(T \\mid D) = 1 - 0.01 = 0.99$ (Sensitivity)
- $\\mathbb{P}(T \\mid D^c) = 0.02$ (False Positive Rate)</p>

<p>By the <strong>Law of Total Probability</strong>:
$$\\begin{aligned}
\\mathbb{P}(T) &= \\mathbb{P}(T \\mid D)\\mathbb{P}(D) + \\mathbb{P}(T \\mid D^c)\\mathbb{P}(D^c) \\\\
&= (0.99)(0.001) + (0.02)(0.999) \\\\
&= 0.00099 + 0.01998 = 0.02097
\\end{aligned}$$
Applying <strong>Bayes' Rule</strong>:
$$\\mathbb{P}(D \\mid T) = \\frac{\\mathbb{P}(T \\mid D)\\mathbb{P}(D)}{\\mathbb{P}(T)} = \\frac{0.00099}{0.02097} = \\frac{99}{2097} = \\frac{33}{699} \\approx <span class=\"ans\">0.04721 \\quad (4.72\\%)</span>$$
Despite the test being $99\\%$ sensitive and $98\\%$ specific, a positive test result yields less than a $5\\%$ chance of disease because false positives from the vast healthy population ($99.9\\%$) heavily dominate true positives.</p>

<p><span class="part">Part (b): Second Independent Confirmation</span><br>
Under conditional independence:
$$\\mathbb{P}(T_1 \\cap T_2 \\mid D) = [\\mathbb{P}(T \\mid D)]^2 = (0.99)^2 = 0.9801$$
$$\\mathbb{P}(T_1 \\cap T_2 \\mid D^c) = [\\mathbb{P}(T \\mid D^c)]^2 = (0.02)^2 = 0.0004$$
The total probability of two positive tests is:
$$\\begin{aligned}
\\mathbb{P}(T_1 \\cap T_2) &= (0.9801)(0.001) + (0.0004)(0.999) \\\\
&= 0.0009801 + 0.0003996 = 0.0013797
\\end{aligned}$$
Applying Bayes' Rule with two observations:
$$\\mathbb{P}(D \\mid T_1 \\cap T_2) = \\frac{0.0009801}{0.0013797} = \\frac{9801}{13797} \\approx <span class=\"ans\">0.71037 \\quad (71.04\\%)</span>$$
<span class=\"ans\">A second positive confirmation elevates the posterior from $4.72\\%$ to $71.04\\%$.</span></p>""",
        "takeaway": "The Base Rate Fallacy: when prior probability $\\mathbb{P}(D)$ is extremely small, even a highly accurate test produces far more false positives than true positives. Conditional independence on repeated tests resolves this ambiguity."
    },
    {
        "id": 30292,
        "subject": "StoMA",
        "topicId": "02_Conditional_Probability_Bayes_Rule_and_Independence",
        "topicTitle": "02 · Conditioning, Bayes & Independence",
        "title": "Bernstein's Counterexample: Pairwise vs. Mutual Independence (Stanford Stats 116)",
        "kind2": "pyq",
        "source": "Stanford Stats 116 / Ross 1.5",
        "marks": "[10 Marks]",
        "question": """<p><span class="part">(a)</span> State the precise mathematical definitions of <strong>pairwise independence</strong> versus <strong>mutual (joint) independence</strong> for three events $A_1, A_2, A_3$.</p>
<p><span class="part">(b)</span> Rigorously construct Sergei Bernstein's classic counterexample using two independent fair coin tosses. Show all necessary probability calculations proving that the three events are pairwise independent but <strong>not</strong> mutually independent.</p>
<p><span class="part">(c)</span> Does knowledge of both $A_1$ and $A_2$ provide any information about $A_3$? Explain the conditioning behavior.</p>""",
        "solution": """<p><span class="part">Part (a): Definitions</span><br>
Three events $A_1, A_2, A_3$ are <strong>pairwise independent</strong> if:
$$\\mathbb{P}(A_i \\cap A_j) = \\mathbb{P}(A_i)\\mathbb{P}(A_j) \\quad \\forall i \\ne j$$
They are <strong>mutually (jointly) independent</strong> if in addition to pairwise independence:
$$\\mathbb{P}(A_1 \\cap A_2 \\cap A_3) = \\mathbb{P}(A_1)\\mathbb{P}(A_2)\\mathbb{P}(A_3)$$</p>

<p><span class="part">Part (b): Bernstein's Construction</span><br>
Consider two independent tosses of a fair coin. The sample space is:
$$\\Omega = \\{ HH, HT, TH, TT \\}, \\quad \\mathbb{P}(\\omega) = \\frac{1}{4} \\quad \\forall \\omega \\in \\Omega$$
Define three events:
- $A_1 = \\{HH, HT\\}$ (First toss is Heads)
- $A_2 = \\{HH, TH\\}$ (Second toss is Heads)
- $A_3 = \\{HH, TT\\}$ (Both tosses match: either both Heads or both Tails)</p>

<p><strong>1. Individual Probabilities:</strong>
$$\\mathbb{P}(A_1) = \\frac{2}{4} = \\frac{1}{2}, \\quad \\mathbb{P}(A_2) = \\frac{2}{4} = \\frac{1}{2}, \\quad \\mathbb{P}(A_3) = \\frac{2}{4} = \\frac{1}{2}$$</p>

<p><strong>2. Pairwise Intersections:</strong>
- $A_1 \\cap A_2 = \\{HH\\} \\implies \\mathbb{P}(A_1 \\cap A_2) = \\frac{1}{4} = \\mathbb{P}(A_1)\\mathbb{P}(A_2)$
- $A_1 \\cap A_3 = \\{HH\\} \\implies \\mathbb{P}(A_1 \\cap A_3) = \\frac{1}{4} = \\mathbb{P}(A_1)\\mathbb{P}(A_3)$
- $A_2 \\cap A_3 = \\{HH\\} \\implies \\mathbb{P}(A_2 \\cap A_3) = \\frac{1}{4} = \\mathbb{P}(A_2)\\mathbb{P}(A_3)$<br>
<span class=\"ans\">Thus, all pairs are pairwise independent!</span></p>

<p><strong>3. Joint Triple Intersection:</strong>
$$A_1 \\cap A_2 \\cap A_3 = \\{HH\\} \\implies \\mathbb{P}(A_1 \\cap A_2 \\cap A_3) = \\frac{1}{4}$$
However, the product of the three marginal probabilities is:
$$\\mathbb{P}(A_1)\\mathbb{P}(A_2)\\mathbb{P}(A_3) = \\left(\\frac{1}{2}\\right)\\left(\\frac{1}{2}\\right)\\left(\\frac{1}{2}\\right) = \\frac{1}{8}$$
Since $\\frac{1}{4} \\ne \\frac{1}{8}$, <span class=\"ans\">the events are NOT mutually independent</span>.</p>

<p><span class="part">Part (c): Conditioning and Information Gain</span><br>
Individually: $\\mathbb{P}(A_3 \\mid A_1) = \\mathbb{P}(A_3) = 1/2$ and $\\mathbb{P}(A_3 \\mid A_2) = 1/2$.<br>
However, conditioned on both:
$$\\mathbb{P}(A_3 \\mid A_1 \\cap A_2) = \\frac{\\mathbb{P}(A_1 \\cap A_2 \\cap A_3)}{\\mathbb{P}(A_1 \\cap A_2)} = \\frac{1/4}{1/4} = 1$$
<span class=\"ans\">Knowing both $A_1$ and $A_2$ determines $A_3$ with absolute certainty ($100\\%$ probability)!</span></p>""",
        "takeaway": "Pairwise independence does NOT imply joint independence! Two events can each individually provide 0 bits of information about a third event, yet together determine it with 100% certainty (XOR parity relation)."
    },
    {
        "id": 30293,
        "subject": "StoMA",
        "topicId": "02_Conditional_Probability_Bayes_Rule_and_Independence",
        "topicTitle": "02 · Conditioning, Bayes & Independence",
        "title": "Conditional Independence vs. Marginal Independence (Generated Exam)",
        "kind2": "practice",
        "source": "MIT 6.041 / Berkeley Benchmark",
        "marks": "[10 Marks]",
        "question": """<p><span class="part">(a)</span> Prove that <strong>marginal independence</strong> does NOT imply <strong>conditional independence</strong>: provide a concrete model where $A \\perp B$ marginally, but $A$ and $B$ are strictly dependent given an event $C$ (the \"explaining away\" / collider effect).</p>
<p><span class="part">(b)</span> Prove that <strong>conditional independence</strong> does NOT imply <strong>marginal independence</strong>: provide a concrete two-coin mixture model where $A$ and $B$ are conditionally independent given coin identity $C$, yet are strictly dependent marginally.</p>""",
        "solution": """<p><span class="part">Part (a): Marginal Independence $\\not\\implies$ Conditional Independence</span><br>
Consider two independent tosses of a fair coin: let $A$ = first toss is Heads, $B$ = second toss is Heads.<br>
Since the tosses are independent:
$$\\mathbb{P}(A) = \\frac{1}{2}, \\quad \\mathbb{P}(B) = \\frac{1}{2}, \\quad \\mathbb{P}(A \\cap B) = \\frac{1}{4} = \\mathbb{P}(A)\\mathbb{P}(B) \\implies A \\perp B$$
Now condition on the event $C = \\text{\"at least one toss is Heads\"} = A \\cup B$.<br>
The outcomes in $C$ are $\\{HH, HT, TH\\}$, so $\\mathbb{P}(C) = 3/4$.<br>
Under condition $C$:
$$\\mathbb{P}(A \\mid C) = \\frac{\\mathbb{P}(A \\cap C)}{\\mathbb{P}(C)} = \\frac{2/4}{3/4} = \\frac{2}{3}, \\qquad \\mathbb{P}(B \\mid C) = \\frac{2}{3}$$
$$\\mathbb{P}(A \\cap B \\mid C) = \\frac{\\mathbb{P}(A \\cap B)}{\\mathbb{P}(C)} = \\frac{1/4}{3/4} = \\frac{1}{3}$$
Multiplying the conditional marginals:
$$\\mathbb{P}(A \\mid C) \\mathbb{P}(B \\mid C) = \\left(\\frac{2}{3}\\right)\\left(\\frac{2}{3}\\right) = \\frac{4}{9} \\ne \\frac{1}{3} = \\mathbb{P}(A \\cap B \\mid C)$$
<span class=\"ans\">Thus $A$ and $B$ are conditionally dependent given $C$.</span><br>
(Intuition: if you know at least one coin landed heads, learning that the first coin landed tails forces the second coin to be heads with probability $1$!).</p>

<p><span class="part">Part (b): Conditional Independence $\\not\\implies$ Marginal Independence</span><br>
Consider a factory with two types of coins in equal proportions ($\\mathbb{P}(C_1) = \\mathbb{P}(C_2) = 1/2$):
- Coin 1 is biased heavily towards Heads: $\\mathbb{P}(H \\mid C_1) = 0.9$.
- Coin 2 is biased heavily towards Tails: $\\mathbb{P}(H \\mid C_2) = 0.1$.<br>
A random coin is picked, and tossed twice. Let $A$ = first toss is Heads, $B$ = second toss is Heads.<br>
Given the coin identity, the tosses are conditionally independent:
$$\\mathbb{P}(A \\cap B \\mid C_1) = (0.9)^2 = 0.81, \\qquad \\mathbb{P}(A \\cap B \\mid C_2) = (0.1)^2 = 0.01$$</p>

<p>Compute marginal probabilities using the Law of Total Probability:
$$\\mathbb{P}(A) = \\mathbb{P}(A \\mid C_1)\\mathbb{P}(C_1) + \\mathbb{P}(A \\mid C_2)\\mathbb{P}(C_2) = (0.9)(0.5) + (0.1)(0.5) = 0.5$$
Similarly, $\\mathbb{P}(B) = 0.5$.<br>
The marginal joint probability is:
$$\\mathbb{P}(A \\cap B) = (0.81)(0.5) + (0.01)(0.5) = 0.405 + 0.005 = 0.41$$
Comparing joint to the product of marginals:
$$\\mathbb{P}(A)\\mathbb{P}(B) = (0.5)(0.5) = 0.25 \\ne 0.41 = \\mathbb{P}(A \\cap B)$$
<span class=\"ans\">Thus $A$ and $B$ are strongly dependent marginally ($0.41 > 0.25$).</span><br>
Observing heads on toss 1 drastically increases the probability that the coin is Coin 1, making heads on toss 2 much more likely.</p>""",
        "takeaway": "Marginal independence and conditional independence have zero implication in either direction. Common causes (latent mixtures) induce marginal dependence; colliders (common effects) induce conditional dependence."
    }
]

def append_to_practice_stoma():
    stoma_file = os.path.join(REPO_DIR, "practice_stoma.js")
    
    # Read existing content if file exists
    existing_cards = []
    if os.path.exists(stoma_file):
        with open(stoma_file, "r", encoding="utf-8") as f:
            content = f.read()
        try:
            # extract JSON between window.PRACTICE_DATA.push( and );
            m = re.search(r'window\.PRACTICE_DATA\.push\(\s*(\[[\s\S]*?\])\s*\);', content)
            if m:
                existing_cards = json.loads(m.group(1))
        except Exception as e:
            print(f"Warning: Could not parse existing cards: {e}")

    # Merge cards by ID
    card_dict = {c["id"]: c for c in existing_cards}
    for c in PRACTICE_STOMA_01_02:
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
