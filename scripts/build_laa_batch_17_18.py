#!/usr/bin/env python3
"""
Builder script for LAA Practice Cards: Batch 09 (Topics 17 & 18 - FINAL LAA BATCH)
Topic 17: Trace, Determinants & Volume (Cards 21791, 21792, 21793)
Topic 18: Markov Chains & Consensus Algorithms (Cards 21891, 21892, 21893)
"""

import json
import os
import re

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRACTICE_FILE = os.path.join(REPO_DIR, "practice_laa.js")

PRACTICE_LAA_17_18 = [
    # =========================================================================
    # TOPIC 17: Trace, Determinants, and Volume
    # =========================================================================
    {
        "id": 21791,
        "subject": "LAA",
        "topicId": "17_Trace_Determinants_and_Volume",
        "topicTitle": "17 · Trace, Determinant & Volume",
        "title": "Non-Existence of Commutator Identity AB - BA = I & Trace Invariance (IISc Endsem 2024 / Axler 8.D)",
        "kind2": "pyq",
        "source": "IISc Endsem 2024 / Axler Linear Algebra Done Right 8.D",
        "marks": "[6 Marks]",
        "question": """<p><span class="part">(a)</span> Prove that for any matrices $A \\in \\mathbb{C}^{m \\times n}$ and $B \\in \\mathbb{C}^{n \\times m}$, the cyclic trace property holds:
$$\\operatorname{Tr}(AB) = \\operatorname{Tr}(BA)$$</p>
<p><span class="part">(b)</span> Prove rigorously that there do NOT exist finite-dimensional matrices $A, B \\in \\mathbb{C}^{n \\times n}$ such that:
$$AB - BA = I_n$$</p>
<p><span class="part">(c)</span> Demonstrate that on infinite-dimensional vector spaces, this commutation relation CAN hold by evaluating the commutator $[D, M_x] = D M_x - M_x D$ on the space of polynomials $\\mathcal{P}(\\mathbb{R})$, where $D = \\frac{d}{dx}$ and $M_x f(x) = x f(x)$ (Heisenberg canonical commutation relation).</p>""",
        "solution": """<p><span class="part">Part (a): Cyclic Trace Invariance Proof</span><br>
Expand the diagonal entries of the matrix product $AB \\in \\mathbb{C}^{m \\times m}$:
$$\\operatorname{Tr}(AB) = \\sum_{i=1}^m (AB)_{ii} = \\sum_{i=1}^m \\sum_{j=1}^n A_{ij} B_{ji}$$
Since scalars commute in $\\mathbb{C}$, swap $A_{ij}$ and $B_{ji}$ and exchange the order of finite sums:
$$\\operatorname{Tr}(AB) = \\sum_{j=1}^n \\sum_{i=1}^m B_{ji} A_{ij} = \\sum_{j=1}^n (BA)_{jj} = <span class=\"ans\">\\operatorname{Tr}(BA)</span>$$</p>

<p><span class="part">Part (b): Commutator Impossibility Proof</span><br>
Suppose for contradiction that there exist matrices $A, B \\in \\mathbb{C}^{n \\times n}$ such that:
$$AB - BA = I_n$$
Apply the trace linear functional to both sides of the equation:
$$\\operatorname{Tr}(AB - BA) = \\operatorname{Tr}(I_n)$$
By linearity of the trace:
$$\\operatorname{Tr}(AB) - \\operatorname{Tr}(BA) = \\operatorname{Tr}(I_n)$$
By the cyclic property from Part (a), $\\operatorname{Tr}(AB) = \\operatorname{Tr}(BA)$, so the left-hand side is:
$$\\operatorname{Tr}(AB) - \\operatorname{Tr}(BA) = 0$$
On the other hand, the trace of the $n \\times n$ identity matrix is:
$$\\operatorname{Tr}(I_n) = \\sum_{i=1}^n 1 = n$$
Equating both sides yields:
<span class=\"ans\">$$0 = n$$</span>
This is an outright contradiction since $n \\ge 1$ for any non-trivial finite-dimensional space.<br>
Therefore, <span class=\"ans\">no such finite-dimensional matrices $A, B$ can exist</span>.</p>

<p><span class="part">Part (c): Infinite-Dimensional Canonical Commutation</span><br>
On the infinite-dimensional polynomial vector space $\\mathcal{P}(\\mathbb{R})$, let $f(x) \\in \\mathcal{P}(\\mathbb{R})$ be an arbitrary test polynomial.<br>
Apply the product rule:
$$[D, M_x] f(x) = D(M_x f(x)) - M_x (D f(x)) = \\frac{d}{dx}(x f(x)) - x \\frac{df}{dx}$$
$$[D, M_x] f(x) = \\left( f(x) + x \\frac{df}{dx} \\right) - x \\frac{df}{dx} = f(x) = I f(x)$$
Thus on $\\mathcal{P}(\\mathbb{R})$:
<span class=\"ans\">$$D M_x - M_x D = I$$</span>
The trace contradiction does not apply because differential operators on infinite-dimensional function spaces do not admit a well-defined finite trace.</p>""",
        "takeaway": "The cyclic property Tr(AB) = Tr(BA) implies Tr(AB - BA) = 0, proving AB - BA = I is impossible for any finite-dimensional matrices because Tr(I_n) = n != 0. In contrast, on infinite-dimensional spaces, operators like position and momentum satisfy [D, X] = I."
    },
    {
        "id": 21792,
        "subject": "LAA",
        "topicId": "17_Trace_Determinants_and_Volume",
        "topicTitle": "17 · Trace, Determinant & Volume",
        "title": "Determinant of Perturbed All-Ones Matrix via Rank-1 Shift (MIT 18.06 / Strang L18)",
        "kind2": "pyq",
        "source": "MIT 18.06 Linear Algebra / Strang Lecture 18",
        "marks": "[8 Marks]",
        "question": """<p>Consider the symmetric $n \\times n$ matrix with perturbed diagonal:
$$A = \\begin{pmatrix} 1 + a & 1 & \\dots & 1 \\\\ 1 & 1 + a & \\dots & 1 \\\\ \\vdots & \\vdots & \\ddots & \\vdots \\\\ 1 & 1 & \\dots & 1 + a \\end{pmatrix} \\in \\mathbb{R}^{n \\times n}$$</p>
<p><span class="part">(a)</span> Express $A$ as the sum of a scalar multiple of the identity matrix $I_n$ and the rank-1 matrix $\\mathbf{1}\\mathbf{1}^\\top$, where $\\mathbf{1} = (1, 1, \\dots, 1)^\\top$.</p>
<p><span class="part">(b)</span> Find all eigenvalues of $\\mathbf{1}\\mathbf{1}^\\top$ and their algebraic multiplicities. Use these to deduce the exact $n$ eigenvalues of $A$.</p>
<p><span class="part">(c)</span> Compute the determinant $\\det(A)$ as the product of its eigenvalues, and verify the formula using the <strong>Matrix Determinant Lemma</strong> $\\det(I_n + u v^\\top) = 1 + v^\\top u$.</p>""",
        "solution": """<p><span class="part">Part (a): Rank-1 Perturbation Representation</span><br>
Notice that every off-diagonal element is $1$ and every diagonal element is $1 + a = a + 1$.<br>
Let $\\mathbf{1} = (1, 1, \\dots, 1)^\\top \\in \\mathbb{R}^n$. The all-ones matrix is $\\mathbf{1}\\mathbf{1}^\\top$.<br>
Therefore:
<span class=\"ans\">$$A = a I_n + \\mathbf{1}\\mathbf{1}^\\top$$</span></p>

<p><span class="part">Part (b): Eigensystem of Rank-1 Shift</span><br>
1. <strong>Eigenvalues of $R = \\mathbf{1}\\mathbf{1}^\\top$:</strong>
- Since $\\operatorname{rank}(R) = 1$, the null space $\\operatorname{null}(R) = \\mathbf{1}^\\perp$ has dimension $n - \\operatorname{rank}(R) = n - 1$.
Therefore, $\\lambda = 0$ is an eigenvalue of $R$ with multiplicity <span class=\"ans\">$n - 1$</span>.
- The single non-zero eigenvalue corresponds to the eigenvector $\\mathbf{1}$:
$$R \\mathbf{1} = (\\mathbf{1}\\mathbf{1}^\\top) \\mathbf{1} = \\mathbf{1}(\\mathbf{1}^\\top \\mathbf{1}) = n \\mathbf{1}$$
Therefore, $\\lambda = n$ is an eigenvalue of $R$ with multiplicity <span class=\"ans\">$1$</span>.<br>
2. <strong>Eigenvalues of $A = a I_n + R$:</strong><br>
Adding $a I_n$ shifts every eigenvalue of $R$ by scalar $a$:
- <span class=\"ans\">$\\lambda_1 = a + n$</span> (multiplicity 1, eigenvector $\\mathbf{1}$).
- <span class=\"ans\">$\\lambda_2 = \\dots = \\lambda_n = a + 0 = a$</span> (multiplicity $n - 1$, eigenspace $\\mathbf{1}^\\perp$).</p>

<p><span class="part">Part (c): Determinant Calculation & Verification</span><br>
1. <strong>Product of eigenvalues:</strong>
$$\\det(A) = \\prod_{i=1}^n \\lambda_i = (a + n) \\cdot \\underbrace{a \\cdot a \\dots a}_{n-1 \\text{ times}} = <span class=\"ans\">a^{n-1} (a + n)</span>$$
2. <strong>Verification via Matrix Determinant Lemma:</strong><br>
For $a \\ne 0$, factor out $a$:
$$A = a \\left( I_n + \\frac{1}{a} \\mathbf{1}\\mathbf{1}^\\top \\right)$$
Taking determinants:
$$\\det(A) = \\det\\left( a \\left( I_n + \\mathbf{1} \\left( \\frac{1}{a} \\mathbf{1} \\right)^\\top \\right) \\right) = a^n \\det\\left( I_n + \\mathbf{1} \\left( \\frac{1}{a} \\mathbf{1} \\right)^\\top \\right)$$
By the Matrix Determinant Lemma $\\det(I + u v^\\top) = 1 + v^\\top u$:
$$\\det(A) = a^n \\left( 1 + \\left( \\frac{1}{a} \\mathbf{1} \\right)^\\top \\mathbf{1} \\right) = a^n \\left( 1 + \\frac{n}{a} \\right) = a^n \\left( \\frac{a + n}{a} \\right) = <span class=\"ans\">a^{n-1} (a + n)</span>$$
Both methods match identically.</p>""",
        "takeaway": "The rank-1 outer product 1 1^T has eigenvalues n (multiplicity 1) and 0 (multiplicity n-1). Perturbing by a I shifts the spectrum to a + n and a (multiplicity n-1), giving det(a I + 1 1^T) = a^(n-1)(a + n)."
    },
    {
        "id": 21793,
        "subject": "LAA",
        "topicId": "17_Trace_Determinants_and_Volume",
        "topicTitle": "17 · Trace, Determinant & Volume",
        "title": "Block Determinants, Geometric Volume & Jacobi's Formula (Generated IISc / Stanford EE263 & Berkeley EECS 127)",
        "kind2": "generated",
        "source": "Generated IISc Midterm / Stanford EE263 & Berkeley EECS 127",
        "marks": "[8 Marks]",
        "question": """<p><span class="part">(a)</span> For block matrices $A, B \\in \\mathbb{R}^{n \\times n}$, prove using determinant-preserving block elementary operations that:
$$\\det \\begin{pmatrix} A & B \\\\ B & A \\end{pmatrix} = \\det(A + B) \\det(A - B)$$</p>
<p><span class="part">(b)</span> Let $v_1, \\dots, v_n \\in \\mathbb{R}^n$ be the spanning edge vectors of an $n$-dimensional parallelotope $\\mathcal{P}$. Prove that the volume is given by $\\operatorname{Vol}(\\mathcal{P}) = |\\det(V)|$, where $V = [v_1, \\dots, v_n]$, by connecting to the Gram matrix $\\det(V^\\top V)$.</p>
<p><span class="part">(c)</span> State and derive <strong>Jacobi's formula</strong> for the derivative of a matrix determinant:
$$\\frac{d}{dt} \\det(A(t)) = \\operatorname{Tr}\\left( \\operatorname{adj}(A(t)) \\frac{dA(t)}{dt} \\right) = \\det(A(t)) \\operatorname{Tr}\\left( A(t)^{-1} \\frac{dA(t)}{dt} \\right)$$</p>""",
        "solution": """<p><span class="part">Part (a): Block Elementary Operations</span><br>
Perform block row and column operations that preserve determinants:
1. Add the second block row to the first block row:
$$\\det \\begin{pmatrix} A & B \\\\ B & A \\end{pmatrix} = \\det \\begin{pmatrix} A + B & B + A \\\\ B & A \\end{pmatrix}$$
2. Subtract the first block column from the second block column:
$$\\det \\begin{pmatrix} A + B & A + B \\\\ B & A \\end{pmatrix} = \\det \\begin{pmatrix} A + B & (A + B) - (A + B) \\\\ B & A - B \\end{pmatrix} = \\det \\begin{pmatrix} A + B & 0 \\\\ B & A - B \\end{pmatrix}$$
3. The resulting matrix is block lower-triangular. The determinant of a block triangular matrix is the product of the determinants of its diagonal blocks:
$$\\det \\begin{pmatrix} A + B & 0 \\\\ B & A - B \\end{pmatrix} = <span class=\"ans\">\\det(A + B) \\det(A - B)</span>$$</p>

<p><span class="part">Part (b): Geometric Volume & Gram Matrix</span><br>
Let $V = [v_1, \\dots, v_n] \\in \\mathbb{R}^{n \\times n}$.<br>
Compute the QR factorization $V = Q R$, where $Q$ is orthogonal ($Q^\\top Q = I \\implies |\\det(Q)| = 1$) and $R$ is upper triangular.<br>
In $R$, each diagonal entry $|R_{ii}|$ represents the orthogonal height $h_i$ of the vector $v_i$ projected perpendicular to the subspace $\\operatorname{span}(v_1, \\dots, v_{i-1})$.<br>
The geometric volume of the parallelotope is base $\\times$ successive orthogonal heights:
$$\\operatorname{Vol}(\\mathcal{P}) = \\prod_{i=1}^n h_i = \\prod_{i=1}^n |R_{ii}| = |\\det(R)|$$
Using $|\\det(Q)| = 1$:
$$\\operatorname{Vol}(\\mathcal{P}) = |\\det(Q) \\det(R)| = |\\det(QR)| = <span class=\"ans\">|\\det(V)|</span>$$
Furthermore, $\\operatorname{Vol}(\\mathcal{P})^2 = (\\det(V))^2 = \\det(V^\\top) \\det(V) = \\det(V^\\top V) = \\det(G)$, where $G$ is the Gram matrix.</p>

<p><span class="part">Part (c): Jacobi's Formula Derivation</span><br>
By Laplace cofactor expansion along the $i$-th row:
$$\\det(A) = \\sum_{j=1}^n A_{ij} C_{ij}$$
where $C_{ij} = (\\operatorname{adj}(A))_{ji}$ is the cofactor. Differentiating with respect to the matrix entry $A_{ij}$:
$$\\frac{\\partial \\det(A)}{\\partial A_{ij}} = C_{ij} = (\\operatorname{adj}(A))_{ji}$$
Using the multivariable chain rule for $A(t)$:
$$\\frac{d}{dt} \\det(A(t)) = \\sum_{i=1}^n \\sum_{j=1}^n \\frac{\\partial \\det(A)}{\\partial A_{ij}} \\frac{d A_{ij}}{dt} = \\sum_{i=1}^n \\sum_{j=1}^n (\\operatorname{adj}(A))_{ji} \\left( \\frac{dA}{dt} \\right)_{ij}$$
This double sum is precisely the matrix trace:
<span class=\"ans\">$$\\frac{d}{dt} \\det(A(t)) = \\operatorname{Tr}\\left( \\operatorname{adj}(A(t)) \\frac{dA(t)}{dt} \\right)$$</span>
When $A(t)$ is invertible, substitute $\\operatorname{adj}(A) = \\det(A) A^{-1}$:
<span class=\"ans\">$$\\frac{d}{dt} \\det(A(t)) = \\det(A(t)) \\operatorname{Tr}\\left( A(t)^{-1} \\frac{dA(t)}{dt} \\right)$$</span></p>""",
        "takeaway": "Block elimination proves det([[A,B],[B,A]]) = det(A+B)det(A-B). The geometric volume of an n-dimensional parallelotope is |det(V)| = sqrt(det(V^T V)). Jacobi's formula relates determinant differentiation directly to trace: d/dt(det A) = det(A) Tr(A^(-1) dA/dt)."
    },

    # =========================================================================
    # TOPIC 18: Markov Chains and Consensus Algorithms
    # =========================================================================
    {
        "id": 21891,
        "subject": "LAA",
        "topicId": "18_Markov_Chains_and_Consensus_Algorithms",
        "topicTitle": "18 · Markov Chains & Consensus",
        "title": "Stationary Distribution & Asymptotic Power of Transition Matrix (IISc Endsem 2024 / Lecture Slides)",
        "kind2": "pyq",
        "source": "IISc Endsem 2024 / Network Consensus Lecture Slides",
        "marks": "[6 Marks]",
        "question": """<p>Consider the row-stochastic transition matrix of a 2-state discrete-time Markov chain:
$$P = \\begin{pmatrix} 0.8 & 0.2 \\\\ 0.3 & 0.7 \\end{pmatrix}$$</p>
<p><span class="part">(a)</span> Compute the unique stationary probability distribution $\\pi = (\\pi_1, \\pi_2)^\\top$ satisfying $\\pi^\\top P = \\pi^\\top$ and $\\pi_1 + \\pi_2 = 1$.</p>
<p><span class="part">(b)</span> Compute the eigenvalues $\\lambda_1, \\lambda_2$ of $P$.</p>
<p><span class="part">(c)</span> Using the spectral projector representation, evaluate the asymptotic matrix limit $\\lim_{k \\to \\infty} P^k = \\mathbf{1} \\pi^\\top$ and explain its physical significance.</p>""",
        "solution": """<p><span class="part">Part (a): Stationary Distribution Calculation</span><br>
The stationary distribution is the left eigenvector of $P$ with eigenvalue 1:
$$\\begin{pmatrix} \\pi_1 & \\pi_2 \\end{pmatrix} \\begin{pmatrix} 0.8 & 0.2 \\\\ 0.3 & 0.7 \\end{pmatrix} = \\begin{pmatrix} \\pi_1 & \\pi_2 \\end{pmatrix}$$
Multiply out the first column equation:
$$0.8 \\pi_1 + 0.3 \\pi_2 = \\pi_1 \\implies 0.3 \\pi_2 = 0.2 \\pi_1 \\implies 2 \\pi_1 = 3 \\pi_2 \\implies \\pi_1 = 1.5 \\pi_2$$
Substitute into the normalization constraint $\\pi_1 + \\pi_2 = 1$:
$$1.5 \\pi_2 + \\pi_2 = 1 \\implies 2.5 \\pi_2 = 1 \\implies \\pi_2 = \\frac{1}{2.5} = <span class=\"ans\">0.4</span>$$
$$\\pi_1 = 1 - 0.4 = <span class=\"ans\">0.6</span>$$
Thus $\\pi = \\begin{pmatrix} 0.6 \\\\ 0.4 \\end{pmatrix}$.</p>

<p><span class="part">Part (b): Eigenvalues of $P$</span><br>
Since $P$ is row-stochastic ($P \\mathbf{1} = \\mathbf{1}$), $\\lambda_1 = 1$ is guaranteed with right eigenvector $\\mathbf{1} = \\begin{pmatrix} 1 \\\\ 1 \\end{pmatrix}$.<br>
Using the trace invariant:
$$\\operatorname{Tr}(P) = 0.8 + 0.7 = 1.5$$
$$\\lambda_1 + \\lambda_2 = 1.5 \\implies 1 + \\lambda_2 = 1.5 \\implies <span class=\"ans\">\\lambda_2 = 0.5</span>$$
Eigenvalues are $\\lambda_1 = 1$ and $\\lambda_2 = 0.5$.</p>

<p><span class="part">Part (c): Asymptotic Limit Matrix</span><br>
Spectral expansion of $P^k$:
$$P^k = 1^k \\frac{\\mathbf{1} \\pi^\\top}{\\pi^\\top \\mathbf{1}} + (0.5)^k Q_2 = \\mathbf{1} \\pi^\\top + (0.5)^k Q_2$$
Since $|0.5| < 1$, as $k \\to \\infty$, $(0.5)^k \\to 0$.<br>
Therefore:
<span class=\"ans\">$$\\lim_{k \\to \\infty} P^k = \\mathbf{1} \\pi^\\top = \\begin{pmatrix} 1 \\\\ 1 \\end{pmatrix} \\begin{pmatrix} 0.6 & 0.4 \\end{pmatrix} = \\begin{pmatrix} 0.6 & 0.4 \\\\ 0.6 & 0.4 \\end{pmatrix}$$</span>
<strong>Physical significance:</strong> Every row of $\\lim P^k$ is identical to $\\pi^\\top$. Regardless of whether the system starts in state 1 ($[1, 0]$) or state 2 ($[0, 1]$), the probability distribution converges to $\\pi = [0.6, 0.4]$ as the Markov chain forgets its initial condition.</p>""",
        "takeaway": "For an ergodic Markov chain, the stationary distribution is the normalized left eigenvector pi^T P = pi^T. Because subdominant eigenvalues satisfy |lambda_2| < 1, the transition powers converge exponentially to the rank-1 matrix lim P^k = 1 pi^T."
    },
    {
        "id": 21892,
        "subject": "LAA",
        "topicId": "18_Markov_Chains_and_Consensus_Algorithms",
        "topicTitle": "18 · Markov Chains & Consensus",
        "title": "Graph Laplacian Positive Semidefiniteness & Algebraic Connectivity (Stanford EE263 / Boyd)",
        "kind2": "pyq",
        "source": "Stanford EE263 Introduction to Linear Dynamical Systems (Boyd)",
        "marks": "[8 Marks]",
        "question": """<p>Let $G = (V, E)$ be an undirected graph on $n$ vertices with degree matrix $D = \\operatorname{diag}(d_1, \\dots, d_n)$ and symmetric adjacency matrix $A$. The <strong>graph Laplacian</strong> is defined as $L = D - A$.</p>
<p><span class="part">(a)</span> Prove that the quadratic form satisfies:
$$x^\\top L x = \\sum_{(i,j) \\in E} (x_i - x_j)^2$$
and deduce that $L$ is positive semidefinite ($L \\ge 0$).</p>
<p><span class="part">(b)</span> Prove that the multiplicity of the eigenvalue $\\lambda = 0$ of $L$ is equal to the number of connected components of $G$.</p>
<p><span class="part">(c)</span> Define the <strong>algebraic connectivity</strong> (Fiedler eigenvalue $\\lambda_2(L)$) of a connected graph, and explain why $\\lambda_2(L) > 0$ governs the exponential convergence rate in continuous-time consensus dynamics $\\dot{x}(t) = -L x(t)$.</p>""",
        "solution": """<p><span class="part">Part (a): Quadratic Form & Positive Semidefiniteness</span><br>
Expand $x^\\top L x = x^\\top D x - x^\\top A x$:
$$x^\\top D x = \\sum_{i=1}^n d_i x_i^2 = \\sum_{i=1}^n \\left( \\sum_{j: (i,j) \\in E} 1 \\right) x_i^2 = \\sum_{(i,j) \\in E} (x_i^2 + x_j^2)$$
$$x^\\top A x = \\sum_{i=1}^n \\sum_{j=1}^n A_{ij} x_i x_j = 2 \\sum_{(i,j) \\in E} x_i x_j$$
Subtracting the two expressions:
$$x^\\top L x = \\sum_{(i,j) \\in E} (x_i^2 - 2 x_i x_j + x_j^2) = <span class=\"ans\">\\sum_{(i,j) \\in E} (x_i - x_j)^2</span>$$
Since each term is a squared real number, $x^\\top L x \\ge 0$ for all $x \\in \\mathbb{R}^n$.<br>
Therefore, <span class=\"ans\">$L \\ge 0$</span> (positive semidefinite).</p>

<p><span class="part">Part (b): Null Space Multiplicity & Connected Components</span><br>
$$L x = 0 \\iff x^\\top L x = 0 \\iff \\sum_{(i,j) \\in E} (x_i - x_j)^2 = 0$$
Since each term is non-negative, the sum is zero if and only if:
$$x_i = x_j \\quad \\text{for every edge } (i,j) \\in E$$
This requires $x$ to be constant across each connected component of $G$.<br>
If $G$ has $k$ connected components $C_1, \\dots, C_k$, the indicator vectors $\\mathbf{1}_{C_1}, \\dots, \\mathbf{1}_{C_k}$ form an orthogonal basis for $\\operatorname{null}(L)$.<br>
Therefore, $\\dim\\operatorname{null}(L) = k$.<br>
Since $L$ is symmetric, geometric multiplicity equals algebraic multiplicity.<br>
Thus the <span class=\"ans\">multiplicity of $\\lambda = 0$ is exactly the number of connected components $k$</span>.</p>

<p><span class="part">Part (c): Algebraic Connectivity & Consensus Convergence</span><br>
For a connected graph ($k = 1$), the eigenvalues satisfy:
$$0 = \\lambda_1(L) < \\lambda_2(L) \\le \\lambda_3(L) \\le \\dots \\le \\lambda_n(L)$$
The second eigenvalue <span class=\"ans\">$\\lambda_2(L)$</span> is the <strong>Fiedler eigenvalue</strong> (algebraic connectivity).<br>
For the consensus system $\\dot{x}(t) = -L x(t)$, expand $x(t)$ in the orthonormal eigenbasis $(q_1, \\dots, q_n)$ of $L$ (where $q_1 = \\frac{1}{\\sqrt{n}} \\mathbf{1}$):
$$x(t) = \\left( q_1^\\top x(0) \\right) q_1 + \\sum_{i=2}^n \\left( q_i^\\top x(0) \\right) e^{-\\lambda_i t} q_i = \\bar{x}_{\\text{avg}} \\mathbf{1} + \\sum_{i=2}^n c_i e^{-\\lambda_i t} q_i$$
Since $\\lambda_i \\ge \\lambda_2(L) > 0$ for all $i \\ge 2$, all non-consensus error modes decay exponentially.<br>
The slowest decaying mode decays as <span class=\"ans\">$e^{-\\lambda_2(L) t}$</span>.<br>
Thus, $\\lambda_2(L)$ strictly dictates the asymptotic consensus convergence rate.</p>""",
        "takeaway": "The graph Laplacian L = D - A is positive semidefinite with x^T L x = sum_{(i,j) in E} (x_i - x_j)^2. The multiplicity of lambda = 0 equals the number of connected components. The Fiedler eigenvalue lambda_2(L) governs the exponential convergence speed of network consensus."
    },
    {
        "id": 21893,
        "subject": "LAA",
        "topicId": "18_Markov_Chains_and_Consensus_Algorithms",
        "topicTitle": "18 · Markov Chains & Consensus",
        "title": "Doubly Stochastic State Invariance & Consensus Convergence Rate (Generated IISc / MIT 18.06 & Berkeley EECS 127)",
        "kind2": "generated",
        "source": "Generated IISc Midterm / MIT 18.06 & Berkeley EECS 127",
        "marks": "[8 Marks]",
        "question": """<p><span class="part">(a)</span> Let $W \\in \\mathbb{R}^{n \\times n}$ be a doubly stochastic matrix ($W \\mathbf{1} = \\mathbf{1}$ and $\\mathbf{1}^\\top W = \\mathbf{1}^\\top$). For the discrete-time consensus dynamics $x(k+1) = W x(k)$, prove that the average state $\\bar{x}(k) = \\frac{1}{n} \\sum_{i=1}^n x_i(k)$ is strictly invariant for all iterations $k \\ge 0$.</p>
<p><span class="part">(b)</span> Consider a 3-agent line network $1 - 2 - 3$ with consensus weight matrix:
$$W = \\begin{pmatrix} 1/2 & 1/2 & 0 \\\\ 1/4 & 1/2 & 1/4 \\\\ 0 & 1/2 & 1/2 \\end{pmatrix}$$
Verify that $W$ is row-stochastic, find all eigenvalues $\\lambda_1, \\lambda_2, \\lambda_3$, and determine the <strong>Second Largest Eigenvalue Modulus (SLEM)</strong>.</p>
<p><span class="part">(c)</span> Using the SLEM, establish the geometric error contraction bound on the consensus disagreement vector $e(k) = x(k) - \\bar{x}\\mathbf{1}$.</p>""",
        "solution": """<p><span class="part">Part (a): Invariant Average Proof</span><br>
Express the average state as an inner product:
$$\\bar{x}(k) = \\frac{1}{n} \\mathbf{1}^\\top x(k)$$
Compute the average state at step $k+1$:
$$\\bar{x}(k+1) = \\frac{1}{n} \\mathbf{1}^\\top x(k+1) = \\frac{1}{n} \\mathbf{1}^\\top (W x(k)) = \\frac{1}{n} (\\mathbf{1}^\\top W) x(k)$$
Because $W$ is doubly stochastic, $\\mathbf{1}^\\top W = \\mathbf{1}^\\top$:
$$\\bar{x}(k+1) = \\frac{1}{n} \\mathbf{1}^\\top x(k) = \\bar{x}(k)$$
By mathematical induction, <span class=\"ans\">$\\bar{x}(k) = \\bar{x}(0)$</span> for all $k \\ge 0$.<br>
The mean state is an exact conserved quantity of the dynamics.</p>

<p><span class="part">Part (b): Eigenvalues & SLEM Calculation</span><br>
1. <strong>Row-stochastic check:</strong>
Row sums: $1/2 + 1/2 + 0 = 1$, $1/4 + 1/2 + 1/4 = 1$, $0 + 1/2 + 1/2 = 1$. Thus $W \\mathbf{1} = \\mathbf{1}$, so $\\lambda_1 = 1$.<br>
2. <strong>Characteristic equation $\\det(W - \\lambda I) = 0$:</strong>
$$\\det \\begin{pmatrix} 1/2 - \\lambda & 1/2 & 0 \\\\ 1/4 & 1/2 - \\lambda & 1/4 \\\\ 0 & 1/2 & 1/2 - \\lambda \\end{pmatrix} = 0$$
Let $\\mu = 1/2 - \\lambda$:
$$\\det = \\mu \\left( \\mu^2 - \\frac{1}{8} \\right) - \\frac{1}{2} \\left( \\frac{\\mu}{4} \\right) = \\mu^3 - \\frac{\\mu}{8} - \\frac{\\mu}{8} = \\mu^3 - \\frac{\\mu}{4} = \\mu \\left( \\mu^2 - \\frac{1}{4} \\right) = 0$$
Roots for $\\mu$:
- $\\mu = 0 \\implies 1/2 - \\lambda = 0 \\implies \\lambda_2 = <span class=\"ans\">1/2</span>$
- $\\mu = 1/2 \\implies 1/2 - \\lambda = 1/2 \\implies \\lambda_3 = <span class=\"ans\">0</span>$
- $\\mu = -1/2 \\implies 1/2 - \\lambda = -1/2 \\implies \\lambda_1 = <span class=\"ans\">1</span>$<br>
Eigenvalues: $\\lambda_1 = 1, \\lambda_2 = 1/2, \\lambda_3 = 0$.<br>
3. <strong>SLEM:</strong>
<span class=\"ans\">$$\\text{SLEM} = \\max_{|\\lambda_i| < 1} |\\lambda_i| = |\\lambda_2| = \\frac{1}{2}$$</span></p>

<p><span class="part">Part (c): Geometric Error Contraction</span><br>
The disagreement vector $e(k) = x(k) - \\bar{x} \\mathbf{1}$ satisfies $\\mathbf{1}^\\top e(k) = 0$, so $e(k) \\in \\mathbf{1}^\\perp$.<br>
The dynamics of the error are $e(k+1) = W e(k)$.<br>
Restricted to the invariant orthogonal complement subspace $\\mathbf{1}^\\perp$, the spectral radius is:
$$\\rho(W|_{\\mathbf{1}^\\perp}) = \\text{SLEM} = \\frac{1}{2}$$
Therefore, the Euclidean distance to consensus satisfies the geometric contraction bound:
<span class=\"ans\">$$\\|x(k) - \\bar{x}\\mathbf{1}\\|_2 \\le C \\left( \\frac{1}{2} \\right)^k \\|x(0) - \\bar{x}\\mathbf{1}\\|_2$$</span>
Each discrete time step contracts the network disagreement by at least a factor of $2$.</p>""",
        "takeaway": "Doubly stochastic weight matrices preserve the average state across iterations (bar{x}(k) = bar{x}(0)). The asymptotic convergence rate to consensus is determined by the Second Largest Eigenvalue Modulus (SLEM), contracting the error by (SLEM)^k per step."
    }
]

def main():
    with open(PRACTICE_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    if "21791" in content:
        print("Batch 17-18 already present in practice_laa.js!")
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
    for card in PRACTICE_LAA_17_18:
        formatted = json.dumps(card, indent=4, ensure_ascii=False)
        new_cards_json.append(formatted)

    new_cards_str = ",\n".join(new_cards_json)
    
    if existing_cards_text:
        updated_cards_text = existing_cards_text + ",\n" + new_cards_str
    else:
        updated_cards_text = new_cards_str

    updated_content = f"/* Practice Questions Database for LAA (Linear Algebra and Applications) */\nwindow.PRACTICE_DATA = window.PRACTICE_DATA || [];\n\nwindow.PRACTICE_DATA.push([\n{updated_cards_text}\n]);\n"

    with open(PRACTICE_FILE, "w", encoding="utf-8") as f:
        f.write(updated_content)

    print("Successfully added LAA Batch 17-18 (6 cards). Total in file now updated.")

if __name__ == "__main__":
    main()
