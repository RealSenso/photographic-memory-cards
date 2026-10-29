#!/usr/bin/env python3
"""
Builder script for LAA Practice Cards: Batch 03 (Topics 05 & 06)
Topic 05: Polynomials & Minimal Polynomial (Cards 20591, 20592, 20593)
Topic 06: Eigenvalues, Eigenvectors & Diagonalization (Cards 20691, 20692, 20693)
"""

import json
import os
import re

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRACTICE_FILE = os.path.join(REPO_DIR, "practice_laa.js")

PRACTICE_LAA_05_06 = [
    # =========================================================================
    # TOPIC 05: Polynomials and Minimal Polynomial
    # =========================================================================
    {
        "id": 20591,
        "subject": "LAA",
        "topicId": "05_Polynomials_and_Minimal_Polynomial",
        "topicTitle": "05 · Polynomials & Minimal Polynomial",
        "title": "Operator Inverse Representation as a Polynomial in T (IISc Midterm 2 / Axler 5.B)",
        "kind2": "pyq",
        "source": "IISc Midterm 2 / Axler Linear Algebra Done Right 5.B",
        "marks": "[6 Marks]",
        "question": """<p>Let $V$ be a finite-dimensional vector space over field $\\mathbb{F}$. Suppose $T \\in \\mathcal{L}(V)$ is an invertible linear operator.</p>
<p><span class="part">(a)</span> State the definition of the minimal polynomial $p_T(z)$ of an operator $T$, and prove why its constant term $c_0 = p_T(0)$ is non-zero when $T$ is invertible.</p>
<p><span class="part">(b)</span> Prove rigorously that there exists a polynomial $q \\in \\mathcal{P}(\\mathbb{F})$ such that $T^{-1} = q(T)$.</p>
<p><span class="part">(c)</span> For an operator $T$ satisfying $T^3 - 4T^2 + 5T - 2I = 0$, express $T^{-1}$ explicitly as a quadratic polynomial in $T$.</p>""",
        "solution": """<p><span class="part">Part (a): Minimal Polynomial & Non-Zero Constant Term</span><br>
The minimal polynomial $p_T(z) = z^m + c_{m-1} z^{m-1} + \\dots + c_1 z + c_0$ is the unique monic polynomial of smallest degree that annihilates $T$, i.e., $p_T(T) = 0$.<br>
The roots of the minimal polynomial over the algebraic closure are precisely the eigenvalues of $T$.<br>
Since $T$ is invertible, $\\operatorname{null}(T) = \\{0\\}$, so $\\lambda = 0$ cannot be an eigenvalue of $T$.<br>
Therefore, $z = 0$ is not a root of $p_T(z)$:
<span class=\"ans\">$$p_T(0) = c_0 \\ne 0$$</span></p>

<p><span class="part">Part (b): Derivation of $T^{-1} = q(T)$</span><br>
Since $p_T(T) = 0$:
$$T^m + c_{m-1} T^{m-1} + \\dots + c_1 T + c_0 I = 0$$
Isolate the identity term $c_0 I$:
$$-c_0 I = T^m + c_{m-1} T^{m-1} + \\dots + c_1 T$$
Factor out $T$ on the right:
$$-c_0 I = T (T^{m-1} + c_{m-1} T^{m-2} + \\dots + c_1 I)$$
Divide both sides by $-c_0 \\ne 0$:
$$I = T \\left[ -\\frac{1}{c_0} (T^{m-1} + c_{m-1} T^{m-2} + \\dots + c_1 I) \\right]$$
Since the inverse of an operator is unique, the bracketed polynomial is $T^{-1}$:
<span class=\"ans\">$$T^{-1} = q(T) \\quad \\text{where } q(z) = -\\frac{1}{c_0} (z^{m-1} + c_{m-1} z^{m-2} + \\dots + c_1)$$</span>
Thus, the inverse of an invertible operator is always a polynomial in the operator of degree at most $\\dim V - 1$.</p>

<p><span class="part">Part (c): Explicit Quadratic Expression</span><br>
Given the annihilating polynomial $T^3 - 4T^2 + 5T - 2I = 0$:
$$2I = T^3 - 4T^2 + 5T = T(T^2 - 4T + 5I)$$
Multiplying both sides by $\\frac{1}{2}$:
$$I = T \\left[ \\frac{1}{2} T^2 - 2T + \\frac{5}{2} I \\right]$$
Therefore:
<span class=\"ans\">$$T^{-1} = \\frac{1}{2} T^2 - 2T + \\frac{5}{2} I$$</span></p>""",
        "takeaway": "If an operator T is invertible, its minimal polynomial has a non-zero constant term c0 != 0. Isolating c0 I allows expressing T^(-1) as a polynomial in T of degree at most deg(p_T) - 1."
    },
    {
        "id": 20592,
        "subject": "LAA",
        "topicId": "05_Polynomials_and_Minimal_Polynomial",
        "topicTitle": "05 · Polynomials & Minimal Polynomial",
        "title": "Minimal Polynomial Computation of Jordan Nilpotent Blocks (Stanford EE263 / Axler 5.25)",
        "kind2": "pyq",
        "source": "Stanford EE263 Introduction to Linear Dynamical Systems / Axler 5.25",
        "marks": "[6 Marks]",
        "question": """<p>Let $T \\in \\mathcal{L}(\\mathbb{R}^3)$ be defined by:
$$T(x, y, z) = (2x + y, \\; 2y + z, \\; 2z)$$</p>
<p><span class="part">(a)</span> Write the matrix representation $A = [T]$ with respect to the standard basis $(e_1, e_2, e_3)$ and determine the only eigenvalue of $T$.</p>
<p><span class="part">(b)</span> Compute powers of the shifted matrix $(A - 2I)$, $(A - 2I)^2$, and $(A - 2I)^3$.</p>
<p><span class="part">(c)</span> Deduce the exact minimal polynomial $p_T(z)$ and evaluate $(T - 2I)^3$.</p>""",
        "solution": """<p><span class="part">Part (a): Matrix Representation & Spectrum</span><br>
Evaluating $T$ on standard basis vectors:
- $T(1, 0, 0) = (2, 0, 0) = 2e_1$
- $T(0, 1, 0) = (1, 2, 0) = e_1 + 2e_2$
- $T(0, 0, 1) = (0, 1, 2) = e_2 + 2e_3$
The matrix representation is an upper triangular Jordan block:
<span class=\"ans\">$$A = \\begin{pmatrix} 2 & 1 & 0 \\\\ 0 & 2 & 1 \\\\ 0 & 0 & 2 \\end{pmatrix}$$</span>
Since $A$ is upper triangular, its eigenvalues are the diagonal entries: $\\lambda = 2$ (with algebraic multiplicity 3).</p>

<p><span class="part">Part (b): Powers of $(A - 2I)$</span><br>
Subtract $2I$ from $A$ to obtain the nilpotent shift operator:
$$(A - 2I) = \\begin{pmatrix} 0 & 1 & 0 \\\\ 0 & 0 & 1 \\\\ 0 & 0 & 0 \\end{pmatrix} \\ne 0$$
Compute $(A - 2I)^2$:
$$(A - 2I)^2 = \\begin{pmatrix} 0 & 1 & 0 \\\\ 0 & 0 & 1 \\\\ 0 & 0 & 0 \\end{pmatrix} \\begin{pmatrix} 0 & 1 & 0 \\\\ 0 & 0 & 1 \\\\ 0 & 0 & 0 \\end{pmatrix} = \\begin{pmatrix} 0 & 0 & 1 \\\\ 0 & 0 & 0 \\\\ 0 & 0 & 0 \\end{pmatrix} \\ne 0$$
Compute $(A - 2I)^3$:
$$(A - 2I)^3 = \\begin{pmatrix} 0 & 0 & 1 \\\\ 0 & 0 & 0 \\\\ 0 & 0 & 0 \\end{pmatrix} \\begin{pmatrix} 0 & 1 & 0 \\\\ 0 & 0 & 1 \\\\ 0 & 0 & 0 \\end{pmatrix} = <span class=\"ans\">\\begin{pmatrix} 0 & 0 & 0 \\\\ 0 & 0 & 0 \\\\ 0 & 0 & 0 \\end{pmatrix} = 0</span>$$</p>

<p><span class="part">Part (c): Minimal Polynomial & Evaluation</span><br>
Since $(A - 2I) \\ne 0$ and $(A - 2I)^2 \\ne 0$, but $(A - 2I)^3 = 0$:
The smallest power of $(z - 2)$ that annihilates $A$ is strictly $3$.<br>
Since the minimal polynomial must be monic, must divide the characteristic polynomial $(z - 2)^3$, and has root $\\lambda = 2$:
<span class=\"ans\">$$p_T(z) = (z - 2)^3 = z^3 - 6z^2 + 12z - 8$$</span>
And:
<span class=\"ans\">$$(T - 2I)^3 = 0$$</span></p>""",
        "takeaway": "For a single Jordan block J_k(lambda), the minimal polynomial equals its characteristic polynomial: p(z) = (z - lambda)^k. The nilpotency index of J_k(lambda) - lambda I is exactly k."
    },
    {
        "id": 20593,
        "subject": "LAA",
        "topicId": "05_Polynomials_and_Minimal_Polynomial",
        "topicTitle": "05 · Polynomials & Minimal Polynomial",
        "title": "Bézout Polynomial Decomposition of Eigenspaces & Idempotent Minimal Polynomial (Generated IISc / MIT 18.06 & Berkeley EECS 127)",
        "kind2": "generated",
        "source": "Generated IISc Midterm / MIT 18.06 (Axler 5.28) & Berkeley EECS 127",
        "marks": "[8 Marks]",
        "question": """<p><span class="part">(a)</span> Suppose $T \\in \\mathcal{L}(V)$ has minimal polynomial $p_T(z) = z^2 - z - 6 = (z - 3)(z + 2)$. Use the Bézout identity for coprime polynomials to prove that:
$$V = \\operatorname{null}(T - 3I) \\oplus \\operatorname{null}(T + 2I)$$</p>
<p><span class="part">(b)</span> Let $P \\in \\mathcal{L}(V)$ satisfy $P^2 = P$ with $P \\ne 0$ and $P \\ne I$. Prove rigorously that the minimal polynomial of $P$ is uniquely:
$$p_P(z) = z(z - 1)$$</p>""",
        "solution": """<p><span class="part">Part (a): Bézout Identity & Eigenspace Decomposition</span><br>
The minimal polynomial factors as $p_T(z) = (z - 3)(z + 2)$.<br>
1. <strong>Bézout Identity:</strong><br>
Since $\\gcd(z - 3, z + 2) = 1$, we write $1$ as a linear combination of the factors:
$$(z + 2) - (z - 3) = 5 \\implies <span class=\"ans\">1 = \\frac{1}{5}(z + 2) - \\frac{1}{5}(z - 3)</span>$$
2. <strong>Operator Identity:</strong><br>
Substitute the operator $T$ into this polynomial relation:
$$I = \\frac{1}{5}(T + 2I) - \\frac{1}{5}(T - 3I)$$
For any arbitrary vector $v \\in V$:
$$v = \\underbrace{\\frac{1}{5}(T + 2I)v}_{v_1} + \\underbrace{-\\frac{1}{5}(T - 3I)v}_{v_2}$$
3. <strong>Verify Subspace Membership:</strong>
$$(T - 3I)v_1 = \\frac{1}{5}(T - 3I)(T + 2I)v = \\frac{1}{5} p_T(T) v = 0 \\implies v_1 \\in \\operatorname{null}(T - 3I)$$
$$(T + 2I)v_2 = -\\frac{1}{5}(T + 2I)(T - 3I)v = -\\frac{1}{5} p_T(T) v = 0 \\implies v_2 \\in \\operatorname{null}(T + 2I)$$
Thus $V = \\operatorname{null}(T - 3I) + \\operatorname{null}(T + 2I)$.<br>
4. <strong>Direct Sum (Trivial Intersection):</strong><br>
Let $u \\in \\operatorname{null}(T - 3I) \\cap \\operatorname{null}(T + 2I)$. Then $Tu = 3u$ and $Tu = -2u$.
$$3u = -2u \\implies 5u = 0 \\implies u = 0$$
Hence $\\operatorname{null}(T - 3I) \\cap \\operatorname{null}(T + 2I) = \\{0\\}$, proving:
<span class=\"ans\">$$V = \\operatorname{null}(T - 3I) \\oplus \\operatorname{null}(T + 2I)$$</span></p>

<p><span class="part">Part (b): Minimal Polynomial of Idempotent Projection</span><br>
The equation $P^2 - P = 0$ means that the polynomial $q(z) = z^2 - z = z(z - 1)$ annihilates $P$.<br>
By the defining property of minimal polynomials, $p_P(z)$ must divide $q(z) = z(z - 1)$.<br>
The monic divisors of $z(z - 1)$ are:
1. $d_1(z) = 1$: degree 0. Cannot annihilate $P$ since $1 \\cdot I = I \\ne 0$.
2. $d_2(z) = z$: degree 1. If $p_P(z) = z$, then $P = 0$, contradicting the hypothesis $P \\ne 0$.
3. $d_3(z) = z - 1$: degree 1. If $p_P(z) = z - 1$, then $P - I = 0 \\implies P = I$, contradicting the hypothesis $P \\ne I$.
4. $d_4(z) = z(z - 1)$: degree 2.<br>
Since no monic polynomial of degree 1 annihilates $P$, the minimal degree polynomial annihilating $P$ is $z(z - 1)$.<br>
Hence:
<span class=\"ans\">$$p_P(z) = z(z - 1)$$</span></p>""",
        "takeaway": "When the minimal polynomial factors into coprime terms p(z) = q1(z) q2(z), the Bézout identity a(z)q1(z) + b(z)q2(z) = 1 decomposes the space into a direct sum V = null(q1(T)) ⊕ null(q2(T)). Any non-trivial projection P^2 = P has minimal polynomial z(z-1)."
    },

    # =========================================================================
    # TOPIC 06: Eigenvalues, Eigenvectors, and Diagonalization
    # =========================================================================
    {
        "id": 20691,
        "subject": "LAA",
        "topicId": "06_Eigenvalues_Eigenvectors_and_Diagonalization",
        "topicTitle": "06 · Eigenvalues & Diagonalization",
        "title": "Diagonalizability Criterion for T^3 = T (IISc Endsem 2024 / Axler 5.D)",
        "kind2": "pyq",
        "source": "IISc Endsem 2024 / Axler Linear Algebra Done Right 5.D",
        "marks": "[6 Marks]",
        "question": """<p>Let $V$ be a finite-dimensional real vector space. Suppose $T \\in \\mathcal{L}(V)$ satisfies the algebraic operator relation:
$$T^3 = T$$</p>
<p><span class="part">(a)</span> Find an annihilating polynomial $q(z)$ for $T$ and factor it completely into irreducible linear terms over $\\mathbb{R}$.</p>
<p><span class="part">(b)</span> State the Diagonalizability Criterion in terms of the minimal polynomial $p_T(z)$.</p>
<p><span class="part">(c)</span> Prove rigorously that $T$ is diagonalizable over $\\mathbb{R}$ and identify the only possible eigenvalues of $T$.</p>""",
        "solution": """<p><span class="part">Part (a): Annihilating Polynomial & Linear Factors</span><br>
The equation $T^3 - T = 0$ means the polynomial $q(z) = z^3 - z$ annihilates $T$:
<span class=\"ans\">$$q(z) = z^3 - z = z(z^2 - 1) = z(z - 1)(z + 1)$$</span>
All three roots $\\{0, 1, -1\\}$ are real and distinct.</p>

<p><span class="part">Part (b): Diagonalizability Criterion</span><br>
<strong>Theorem (Axler 5.44):</strong> A linear operator $T$ on a finite-dimensional vector space is diagonalizable over field $\\mathbb{F}$ if and only if its minimal polynomial $p_T(z)$ factors completely into <strong>distinct linear factors</strong> over $\\mathbb{F}$:
$$p_T(z) = (z - \\lambda_1)(z - \\lambda_2) \\dots (z - \\lambda_k) \\quad \\text{with } \\lambda_i \\ne \\lambda_j \\in \\mathbb{F}$$</p>

<p><span class="part">Part (c): Proof of Diagonalizability</span><br>
1. <strong>Minimal Polynomial Divisibility:</strong><br>
The minimal polynomial $p_T(z)$ must divide $q(z) = z(z - 1)(z + 1)$.<br>
The only monic divisors of $z(z - 1)(z + 1)$ are:
- Degree 1: $z$, $z - 1$, $z + 1$
- Degree 2: $z(z - 1)$, $z(z + 1)$, $(z - 1)(z + 1)$
- Degree 3: $z(z - 1)(z + 1)$<br>
Every single divisor is a product of distinct linear factors with multiplicity 1 over $\\mathbb{R}$.<br>
There are no repeated roots ($(z - \\lambda)^2$) and no irreducible quadratics ($z^2 + 1$).<br>
2. <strong>Conclusion:</strong><br>
By the Diagonalizability Criterion, $T$ is <strong>strictly diagonalizable over $\\mathbb{R}$</strong>.<br>
The only possible eigenvalues of $T$ are the roots of $q(z)$:
<span class=\"ans\">$$\\lambda \\in \\{0, 1, -1\\}$$</span>
Furthermore, $V$ decomposes into the direct sum of its eigenspaces:
$$V = \\operatorname{null}(T) \\oplus \\operatorname{null}(T - I) \\oplus \\operatorname{null}(T + I)$$</p>""",
        "takeaway": "An operator is diagonalizable if and only if its minimal polynomial is a product of distinct linear factors. If T^3 = T, any divisor of z(z-1)(z+1) has no repeated roots, guaranteeing that T is diagonalizable over R."
    },
    {
        "id": 20692,
        "subject": "LAA",
        "topicId": "06_Eigenvalues_Eigenvectors_and_Diagonalization",
        "topicTitle": "06 · Eigenvalues & Diagonalization",
        "title": "Complete Eigendecomposition & Matrix Power A^10 Derivation (MIT 18.06 / Strang L22)",
        "kind2": "pyq",
        "source": "MIT 18.06 Linear Algebra / Strang Lecture 22",
        "marks": "[8 Marks]",
        "question": """<p>Consider the matrix:
$$A = \\begin{pmatrix} 4 & 1 \\\\ 2 & 3 \\end{pmatrix}$$</p>
<p><span class="part">(a)</span> Compute the characteristic polynomial $\\det(A - \\lambda I)$, and find the eigenvalues $\\lambda_1, \\lambda_2$.</p>
<p><span class="part">(b)</span> Find the corresponding eigenvectors $v_1, v_2$, construct the modal matrix $P$ and its inverse $P^{-1}$, and diagonalize $A = P D P^{-1}$.</p>
<p><span class="part">(c)</span> Use the diagonalization to derive an exact closed-form expression for the matrix power $A^{10}$.</p>""",
        "solution": """<p><span class="part">Part (a): Characteristic Polynomial & Eigenvalues</span><br>
$$\\det(A - \\lambda I) = \\det\\begin{pmatrix} 4 - \\lambda & 1 \\\\ 2 & 3 - \\lambda \\end{pmatrix} = (4 - \\lambda)(3 - \\lambda) - 2$$
$$= \\lambda^2 - 7\\lambda + 12 - 2 = \\lambda^2 - 7\\lambda + 10 = (\\lambda - 2)(\\lambda - 5) = 0$$
The eigenvalues are:
<span class=\"ans\">$$\\lambda_1 = 2, \\qquad \\lambda_2 = 5$$</span></p>

<p><span class="part">Part (b): Eigenvectors & Diagonalization $A = P D P^{-1}$</span><br>
1. <strong>For $\\lambda_1 = 2$:</strong>
$$(A - 2I)v_1 = \\begin{pmatrix} 2 & 1 \\\\ 2 & 1 \\end{pmatrix} \\begin{pmatrix} x_1 \\\\ x_2 \\end{pmatrix} = 0 \\implies 2x_1 + x_2 = 0 \\implies v_1 = <span class=\"ans\">\\begin{pmatrix} 1 \\\\ -2 \\end{pmatrix}</span>$$
2. <strong>For $\\lambda_2 = 5$:</strong>
$$(A - 5I)v_2 = \\begin{pmatrix} -1 & 1 \\\\ 2 & -2 \\end{pmatrix} \\begin{pmatrix} x_1 \\\\ x_2 \\end{pmatrix} = 0 \\implies -x_1 + x_2 = 0 \\implies v_2 = <span class=\"ans\">\\begin{pmatrix} 1 \\\\ 1 \\end{pmatrix}</span>$$
3. <strong>Modal Matrix $P$ and $P^{-1}$:</strong>
$$P = \\begin{pmatrix} 1 & 1 \\\\ -2 & 1 \\end{pmatrix}, \\qquad \\det(P) = (1)(1) - (1)(-2) = 1 + 2 = 3$$
$$P^{-1} = \\frac{1}{3} \\begin{pmatrix} 1 & -1 \\\\ 2 & 1 \\end{pmatrix}$$
$$D = \\begin{pmatrix} 2 & 0 \\\\ 0 & 5 \\end{pmatrix}$$
Thus <span class=\"ans\">$A = P D P^{-1}$</span>.</p>

<p><span class="part">Part (c): Matrix Power $A^{10}$</span><br>
$$A^{10} = P D^{10} P^{-1} = \\begin{pmatrix} 1 & 1 \\\\ -2 & 1 \\end{pmatrix} \\begin{pmatrix} 2^{10} & 0 \\\\ 0 & 5^{10} \\end{pmatrix} \\frac{1}{3} \\begin{pmatrix} 1 & -1 \\\\ 2 & 1 \\end{pmatrix}$$
Multiply $P D^{10}$:
$$P D^{10} = \\begin{pmatrix} 1 & 1 \\\\ -2 & 1 \\end{pmatrix} \\begin{pmatrix} 2^{10} & 0 \\\\ 0 & 5^{10} \\end{pmatrix} = \\begin{pmatrix} 2^{10} & 5^{10} \\\\ -2(2^{10}) & 5^{10} \\end{pmatrix}$$
Multiply by $P^{-1}$:
$$A^{10} = \\frac{1}{3} \\begin{pmatrix} 2^{10} & 5^{10} \\\\ -2^{11} & 5^{10} \\end{pmatrix} \\begin{pmatrix} 1 & -1 \\\\ 2 & 1 \\end{pmatrix}$$
<span class=\"ans\">$$A^{10} = \\frac{1}{3} \\begin{pmatrix} 2^{10} + 2 \\cdot 5^{10} & -2^{10} + 5^{10} \\\\ -2^{11} + 2 \\cdot 5^{10} & 2^{11} + 5^{10} \\end{pmatrix}$$</span>
(With $2^{10} = 1024$ and $5^{10} = 9765625$, $A^{10} = \\begin{pmatrix} 6510758 & 3254867 \\\\ 6509734 & 3255891 \\end{pmatrix}$).</p>""",
        "takeaway": "Matrix powers are computed in closed form via eigendecomposition A^k = P D^k P^(-1). The dominant eigenvalue lambda = 5 governs long-term asymptotic behavior."
    },
    {
        "id": 20693,
        "subject": "LAA",
        "topicId": "06_Eigenvalues_Eigenvectors_and_Diagonalization",
        "topicTitle": "06 · Eigenvalues & Diagonalization",
        "title": "Simultaneous Diagonalization of Commuting Operators & Defective Matrix Detection (Generated IISc / Stanford EE263 & IIT Bombay)",
        "kind2": "generated",
        "source": "Generated IISc Midterm / Stanford EE263 (Axler 5.C) & IIT Bombay CSE",
        "marks": "[8 Marks]",
        "question": """<p><span class="part">(a)</span> Suppose $T \\in \\mathcal{L}(V)$ has $n = \\dim V$ distinct eigenvalues. Let $S \\in \\mathcal{L}(V)$ be an operator that commutes with $T$ ($ST = TS$). Prove that $S$ is diagonalizable, and that $S$ and $T$ share a common basis of eigenvectors.</p>
<p><span class="part">(b)</span> Consider the matrix:
$$A = \\begin{pmatrix} 3 & 1 & 0 \\\\ 0 & 3 & 0 \\\\ 0 & 0 & 2 \\end{pmatrix}$$
(i) Compute the algebraic multiplicity of each eigenvalue.
(ii) Compute the geometric multiplicity $\\dim \\operatorname{null}(A - \\lambda I)$ for each eigenvalue.
(iii) State whether $A$ is diagonalizable over $\\mathbb{C}$, and compute the minimal polynomial $p_A(z)$.</p>""",
        "solution": """<p><span class="part">Part (a): Simultaneous Diagonalization of Commuting Operators</span><br>
Let $\\lambda_1, \\dots, \\lambda_n$ be the $n$ distinct eigenvalues of $T$.<br>
1. <strong>1D Eigenspaces:</strong> Because all $n$ eigenvalues are distinct in an $n$-dimensional space, each eigenspace $E(\\lambda_j, T) = \\operatorname{null}(T - \\lambda_j I)$ has dimension strictly $1$:
$$E(\\lambda_j, T) = \\operatorname{span}(v_j) \\quad \\text{with } v_j \\ne 0$$
2. <strong>Invariance under $S$:</strong> Let $v_j$ be an eigenvector of $T$ with $Tv_j = \\lambda_j v_j$. Apply $T$ to $Sv_j$:
$$T(Sv_j) = (TS)v_j = (ST)v_j = S(Tv_j) = S(\\lambda_j v_j) = \\lambda_j (Sv_j)$$
Thus $Sv_j \\in E(\\lambda_j, T)$.<br>
3. <strong>Common Eigenvector:</strong> Since $\\dim E(\\lambda_j, T) = 1$ and $v_j$ spans it, $Sv_j$ must be a scalar multiple of $v_j$:
<span class=\"ans\">$$S v_j = \\mu_j v_j \\quad \\text{for some scalar } \\mu_j \\in \\mathbb{F}$$</span>
This proves that every eigenvector $v_j$ of $T$ is simultaneously an eigenvector of $S$.<br>
Since $(v_1, \\dots, v_n)$ forms a basis of $V$ (eigenvectors corresponding to distinct eigenvalues are linearly independent), this basis simultaneously diagonalizes both $T$ and $S$.</p>

<p><span class="part">Part (b): Defective Matrix Analysis</span><br>
Matrix $A = \\begin{pmatrix} 3 & 1 & 0 \\\\ 0 & 3 & 0 \\\\ 0 & 0 & 2 \\end{pmatrix}$.<br>
1. <strong>Algebraic Multiplicity:</strong><br>
Since $A$ is upper triangular: $\\det(A - \\lambda I) = (3 - \\lambda)^2 (2 - \\lambda) = 0$.
<ul>
  <li>$\\lambda_1 = 3$: <span class=\"ans\">Algebraic Multiplicity = 2</span></li>
  <li>$\\lambda_2 = 2$: <span class=\"ans\">Algebraic Multiplicity = 1</span></li>
</ul>
2. <strong>Geometric Multiplicity:</strong>
- For $\\lambda_1 = 3$:
$$A - 3I = \\begin{pmatrix} 0 & 1 & 0 \\\\ 0 & 0 & 0 \\\\ 0 & 0 & -1 \\end{pmatrix}$$
Rows 1 and 3 are linearly independent, so $\\operatorname{rank}(A - 3I) = 2$.
$$\\text{Geometric Multiplicity} = \\dim \\operatorname{null}(A - 3I) = 3 - \\operatorname{rank}(A - 3I) = 3 - 2 = <span class=\"ans\">1</span>$$
- For $\\lambda_2 = 2$:
$$A - 2I = \\begin{pmatrix} 1 & 1 & 0 \\\\ 0 & 1 & 0 \\\\ 0 & 0 & 0 \\end{pmatrix} \\implies \\operatorname{rank}(A - 2I) = 2 \\implies \\dim \\operatorname{null}(A - 2I) = 1$$
3. <strong>Diagonalizability Verdict & Minimal Polynomial:</strong><br>
For $\\lambda = 3$, $\\text{Geometric Multiplicity } (1) < \\text{Algebraic Multiplicity } (2)$.<br>
There is an eigen-defect (only 2 linearly independent eigenvectors exist for a $3 \\times 3$ matrix).<br>
<span class=\"ans\">$A$ is NOT diagonalizable.</span><br>
Check $(A - 3I)(A - 2I)$:
$$(A - 3I)(A - 2I) = \\begin{pmatrix} 0 & 1 & 0 \\\\ 0 & 0 & 0 \\\\ 0 & 0 & -1 \\end{pmatrix} \\begin{pmatrix} 1 & 1 & 0 \\\\ 0 & 1 & 0 \\\\ 0 & 0 & 0 \\end{pmatrix} = \\begin{pmatrix} 0 & 1 & 0 \\\\ 0 & 0 & 0 \\\\ 0 & 0 & 0 \\end{pmatrix} \\ne 0$$
$$(A - 3I)^2 (A - 2I) = 0$$
The minimal polynomial has a repeated root:
<span class=\"ans\">$$p_A(z) = (z - 3)^2 (z - 2)$$</span></p>""",
        "takeaway": "Commuting operators ST = TS leave each other's eigenspaces invariant; if T has distinct eigenvalues, S and T share a common basis of eigenvectors. A matrix is diagonalizable if and only if geometric multiplicity equals algebraic multiplicity for every eigenvalue (or equivalently, its minimal polynomial has only simple roots)."
    }
]

def main():
    with open(PRACTICE_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    if "20591" in content:
        print("Batch 05-06 already present in practice_laa.js!")
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
    for card in PRACTICE_LAA_05_06:
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

    print("Successfully added LAA Batch 05-06 (6 cards). Total in file now updated.")

if __name__ == "__main__":
    main()
