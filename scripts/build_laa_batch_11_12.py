#!/usr/bin/env python3
"""
Builder script for LAA Practice Cards: Batch 06 (Topics 11 & 12)
Topic 11: Gram-Schmidt, Orthogonal Projections & QR Decomposition (Cards 21191, 21192, 21193)
Topic 12: Adjoints, Self-Adjoint & Normal Operators (Cards 21291, 21292, 21293)
"""

import json
import os
import re

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRACTICE_FILE = os.path.join(REPO_DIR, "practice_laa.js")

PRACTICE_LAA_11_12 = [
    # =========================================================================
    # TOPIC 11: Gram-Schmidt, Orthogonal Projections, and QR Decomposition
    # =========================================================================
    {
        "id": 21191,
        "subject": "LAA",
        "topicId": "11_Gram_Schmidt_Orthogonal_Projections_and_QR",
        "topicTitle": "11 · Gram-Schmidt & QR Decomposition",
        "title": "Gram-Schmidt Orthogonalization & QR Matrix Factorization (IISc Midterm 2 / MIT 18.06)",
        "kind2": "pyq",
        "source": "IISc Midterm 2 / MIT 18.06 Linear Algebra",
        "marks": "[8 Marks]",
        "question": """<p>Consider the linearly independent column vectors in $\\mathbb{R}^3$:
$$v_1 = \\begin{pmatrix} 1 \\\\ 1 \\\\ 0 \\end{pmatrix}, \\qquad v_2 = \\begin{pmatrix} 1 \\\\ 0 \\\\ 1 \\end{pmatrix}$$</p>
<p><span class="part">(a)</span> Apply the classical Gram-Schmidt orthogonalization process to convert $(v_1, v_2)$ into an orthonormal pair $(e_1, e_2)$.</p>
<p><span class="part">(b)</span> Assemble the matrix $Q = [e_1, e_2] \\in \\mathbb{R}^{3 \\times 2}$ and the upper triangular matrix $R = \\begin{pmatrix} \\langle v_1, e_1 \\rangle & \\langle v_2, e_1 \\rangle \\\\ 0 & \\langle v_2, e_2 \\rangle \\end{pmatrix}$, and verify the QR factorization $A = QR$ where $A = [v_1, v_2]$.</p>
<p><span class="part">(c)</span> Explain why Modified Gram-Schmidt (MGS) is preferred over Classical Gram-Schmidt in floating-point scientific computing.</p>""",
        "solution": """<p><span class="part">Part (a): Gram-Schmidt Orthogonalization</span><br>
1. <strong>First Vector $e_1$:</strong>
$$u_1 = v_1 = \\begin{pmatrix} 1 \\\\ 1 \\\\ 0 \\end{pmatrix}, \\qquad \\|u_1\\| = \\sqrt{1^2 + 1^2 + 0^2} = \\sqrt{2}$$
Normalize:
<span class=\"ans\">$$e_1 = \\frac{u_1}{\\|u_1\\|} = \\frac{1}{\\sqrt{2}} \\begin{pmatrix} 1 \\\\ 1 \\\\ 0 \\end{pmatrix} = \\begin{pmatrix} 1/\\sqrt{2} \\\\ 1/\\sqrt{2} \\\\ 0 \\end{pmatrix}$$</span>
2. <strong>Second Vector $e_2$:</strong><br>
Project $v_2$ onto $e_1$:
$$\\langle v_2, e_1 \\rangle = v_2^\\top e_1 = 1(1/\\sqrt{2}) + 0(1/\\sqrt{2}) + 1(0) = \\frac{1}{\\sqrt{2}}$$
Subtract projection:
$$u_2 = v_2 - \\langle v_2, e_1 \\rangle e_1 = \\begin{pmatrix} 1 \\\\ 0 \\\\ 1 \\end{pmatrix} - \\frac{1}{\\sqrt{2}} \\begin{pmatrix} 1/\\sqrt{2} \\\\ 1/\\sqrt{2} \\\\ 0 \\end{pmatrix} = \\begin{pmatrix} 1 - 1/2 \\\\ 0 - 1/2 \\\\ 1 - 0 \\end{pmatrix} = \\begin{pmatrix} 1/2 \\\\ -1/2 \\\\ 1 \\end{pmatrix}$$
Norm of $u_2$:
$$\\|u_2\\| = \\sqrt{(1/2)^2 + (-1/2)^2 + 1^2} = \\sqrt{1/4 + 1/4 + 1} = \\sqrt{6/4} = \\frac{\\sqrt{6}}{2}$$
Normalize:
<span class=\"ans\">$$e_2 = \\frac{u_2}{\\|u_2\\|} = \\frac{2}{\\sqrt{6}} \\begin{pmatrix} 1/2 \\\\ -1/2 \\\\ 1 \\end{pmatrix} = \\frac{1}{\\sqrt{6}} \\begin{pmatrix} 1 \\\\ -1 \\\\ 2 \\end{pmatrix} = \\begin{pmatrix} 1/\\sqrt{6} \\\\ -1/\\sqrt{6} \\\\ 2/\\sqrt{6} \\end{pmatrix}$$</span>
Verify orthogonality: $\\langle e_1, e_2 \\rangle = \\frac{1}{\\sqrt{12}}(1 - 1 + 0) = 0$.</p>

<p><span class="part">Part (b): QR Factorization Assembly</span><br>
Assemble $Q \\in \\mathbb{R}^{3 \\times 2}$:
<span class=\"ans\">$$Q = \\begin{pmatrix} 1/\\sqrt{2} & 1/\\sqrt{6} \\\\ 1/\\sqrt{2} & -1/\\sqrt{6} \\\\ 0 & 2/\\sqrt{6} \\end{pmatrix}$$</span>
Assemble upper triangular matrix $R$:
- $R_{11} = \\langle v_1, e_1 \\rangle = \\|u_1\\| = \\sqrt{2}$
- $R_{12} = \\langle v_2, e_1 \\rangle = 1/\\sqrt{2}$
- $R_{22} = \\langle v_2, e_2 \\rangle = \\|u_2\\| = \\sqrt{6}/2$
<span class=\"ans\">$$R = \\begin{pmatrix} \\sqrt{2} & 1/\\sqrt{2} \\\\ 0 & \\sqrt{6}/2 \\end{pmatrix}$$</span>
<strong>Verification:</strong>
$$QR = \\begin{pmatrix} 1/\\sqrt{2} & 1/\\sqrt{6} \\\\ 1/\\sqrt{2} & -1/\\sqrt{6} \\\\ 0 & 2/\\sqrt{6} \\end{pmatrix} \\begin{pmatrix} \\sqrt{2} & 1/\\sqrt{2} \\\\ 0 & \\sqrt{6}/2 \\end{pmatrix} = \\begin{pmatrix} 1 + 0 & 1/2 + 1/2 \\\\ 1 + 0 & 1/2 - 1/2 \\\\ 0 + 0 & 0 + 1 \\end{pmatrix} = \\begin{pmatrix} 1 & 1 \\\\ 1 & 0 \\\\ 0 & 1 \\end{pmatrix} = A$$
The decomposition $A = QR$ is verified.</p>

<p><span class="part">Part (c): Classical vs. Modified Gram-Schmidt</span><br>
In Classical Gram-Schmidt (CGS), projections are taken against the original vectors, causing cancellation errors that lead to catastrophic loss of orthogonality when columns are nearly collinear ($Q^\\top Q \\not\\approx I$).<br>
<strong>Modified Gram-Schmidt (MGS)</strong> projects each subsequent vector successively onto newly updated residual vectors. While mathematically identical in exact arithmetic, MGS is numerically far more stable, bounding orthogonality errors to $\\mathcal{O}(\\epsilon_{\\text{mach}} \\kappa(A))$.</p>""",
        "takeaway": "Gram-Schmidt factors an m x n matrix with independent columns into A = Q R, where Q has orthonormal columns and R is upper triangular with R_kk = ||u_k||. Modified Gram-Schmidt (MGS) prevents numerical loss of orthogonality in floating-point arithmetic."
    },
    {
        "id": 21192,
        "subject": "LAA",
        "topicId": "11_Gram_Schmidt_Orthogonal_Projections_and_QR",
        "topicTitle": "11 · Gram-Schmidt & QR Decomposition",
        "title": "Best Approximation Theorem & Subspace Orthogonal Projection (Stanford EE263 / Boyd)",
        "kind2": "pyq",
        "source": "Stanford EE263 Introduction to Linear Dynamical Systems (Boyd)",
        "marks": "[6 Marks]",
        "question": """<p>Let $U = \\operatorname{span}\\left( \\begin{pmatrix} 1 \\\\ 2 \\\\ 2 \\end{pmatrix} \\right) \\subset \\mathbb{R}^3$ be a 1-dimensional subspace. Consider the target point $v = \\begin{pmatrix} 3 \\\\ 0 \\\\ 1 \\end{pmatrix} \\in \\mathbb{R}^3$.</p>
<p><span class="part">(a)</span> State the <strong>Best Approximation Theorem</strong> for orthogonal projections in inner product spaces.</p>
<p><span class="part">(b)</span> Compute the orthogonal projection $P_U v$ onto $U$ to find the point in $U$ closest to $v$.</p>
<p><span class="part">(c)</span> Compute the minimal Euclidean distance $\\|v - P_U v\\|$ from $v$ to the subspace $U$.</p>""",
        "solution": """<p><span class="part">Part (a): Best Approximation Theorem</span><br>
<strong>Theorem:</strong> Let $U$ be a finite-dimensional subspace of an inner product space $V$, and let $v \\in V$. Then the orthogonal projection $P_U v$ is the unique vector in $U$ that minimizes the distance to $v$:
<span class=\"ans\">$$\\|v - P_U v\\| < \\|v - u\\| \\quad \\text{for all } u \\in U \\text{ with } u \\ne P_U v$$</span>
The error vector $e = v - P_U v$ satisfies the orthogonality condition $e \\perp U$ (i.e. $\\langle v - P_U v, u \\rangle = 0$ for all $u \\in U$).</p>

<p><span class="part">Part (b): Orthogonal Projection Calculation</span><br>
Let $u_1 = \\begin{pmatrix} 1 \\\\ 2 \\\\ 2 \\end{pmatrix}$. The projection onto the 1D span is:
$$P_U v = \\frac{\\langle v, u_1 \\rangle}{\\|u_1\\|^2} u_1$$
1. Inner product:
$$\\langle v, u_1 \\rangle = v^\\top u_1 = 3(1) + 0(2) + 1(2) = 3 + 0 + 2 = 5$$
2. Squared norm:
$$\\|u_1\\|^2 = 1^2 + 2^2 + 2^2 = 1 + 4 + 4 = 9$$
3. Projection:
<span class=\"ans\">$$P_U v = \\frac{5}{9} \\begin{pmatrix} 1 \\\\ 2 \\\\ 2 \\end{pmatrix} = \\begin{pmatrix} 5/9 \\\\ 10/9 \\\\ 10/9 \\end{pmatrix}$$</span></p>

<p><span class="part">Part (c): Minimal Distance</span><br>
Compute the orthogonal error vector:
$$v - P_U v = \\begin{pmatrix} 3 \\\\ 0 \\\\ 1 \\end{pmatrix} - \\begin{pmatrix} 5/9 \\\\ 10/9 \\\\ 10/9 \\end{pmatrix} = \\begin{pmatrix} 27/9 - 5/9 \\\\ 0 - 10/9 \\\\ 9/9 - 10/9 \\end{pmatrix} = \\begin{pmatrix} 22/9 \\\\ -10/9 \\\\ -1/9 \\end{pmatrix} = \\frac{1}{9} \\begin{pmatrix} 22 \\\\ -10 \\\\ -1 \\end{pmatrix}$$
Verify orthogonality: $\\langle v - P_U v, u_1 \\rangle = \\frac{1}{9}(22(1) - 10(2) - 1(2)) = \\frac{1}{9}(22 - 20 - 2) = 0$.<br>
Compute the distance:
$$\\|v - P_U v\\| = \\frac{1}{9} \\sqrt{22^2 + (-10)^2 + (-1)^2} = \\frac{1}{9} \\sqrt{484 + 100 + 1} = \\frac{1}{9} \\sqrt{585} = \\frac{3\\sqrt{65}}{9} = <span class=\"ans\">\\frac{\\sqrt{65}}{3} \\approx 2.6874</span>$$</p>""",
        "takeaway": "The Best Approximation Theorem states that the orthogonal projection P_U v minimizes ||v - u|| over all u in U. The residual error v - P_U v is strictly orthogonal to the subspace U."
    },
    {
        "id": 21193,
        "subject": "LAA",
        "topicId": "11_Gram_Schmidt_Orthogonal_Projections_and_QR",
        "topicTitle": "11 · Gram-Schmidt & QR Decomposition",
        "title": "Contractive Projections Are Orthogonal & Projection Matrix Invariants (Generated IISc / IIT Bombay & Berkeley EECS 127)",
        "kind2": "generated",
        "source": "Generated IISc Midterm / IIT Bombay & Berkeley EECS 127 (Axler 6.56)",
        "marks": "[8 Marks]",
        "question": """<p><span class="part">(a)</span> Let $P \\in \\mathcal{L}(V)$ be a projection operator satisfying $P^2 = P$ and the norm contraction condition:
$$\\|Pv\\| \\le \\|v\\| \\quad \\text{for all } v \\in V$$
Prove rigorously that $P$ is an <strong>orthogonal projection</strong> (i.e. $\\operatorname{range}(P) \\perp \\operatorname{null}(P)$).</p>
<p><span class="part">(b)</span> Let $A \\in \\mathbb{R}^{m \\times n}$ have full column rank ($m > n$). Prove that the projection matrix $P = A(A^\\top A)^{-1} A^\\top$ is symmetric ($P^\\top = P$) and idempotent ($P^2 = P$).</p>
<p><span class="part">(c)</span> Determine the eigenvalues, trace, and geometric multiplicities of the projection matrix $P = A(A^\\top A)^{-1} A^\\top$.</p>""",
        "solution": """<p><span class="part">Part (a): Proof that Contractive Projections Are Orthogonal</span><br>
A projection $P^2 = P$ is orthogonal if and only if $\\operatorname{range}(P) \\perp \\operatorname{null}(P)$, which means $\\langle u, w \\rangle = 0$ for all $u \\in \\operatorname{range}(P)$ and $w \\in \\operatorname{null}(P)$.<br>
Let $u \\in \\operatorname{range}(P)$ (so $Pu = u$) and $w \\in \\operatorname{null}(P)$ (so $Pw = 0$).<br>
For any real scalar $c \\in \\mathbb{R}$, evaluate $P(u + c w)$:
$$P(u + c w) = Pu + c Pw = u + 0 = u$$
Applying the contractive hypothesis $\\|P v\\| \\le \\|v\\|$ with $v = u + c w$:
$$\\|u\\|^2 = \\|P(u + c w)\\|^2 \\le \\|u + c w\\|^2 = \\langle u + c w, u + c w \\rangle$$
$$\\|u\\|^2 \\le \\|u\\|^2 + 2c \\operatorname{Re}\\langle u, w \\rangle + c^2 \\|w\\|^2$$
Subtract $\\|u\\|^2$ from both sides:
$$0 \\le 2c \\operatorname{Re}\\langle u, w \\rangle + c^2 \\|w\\|^2 \\quad \\text{for ALL } c \\in \\mathbb{R}$$
The quadratic $f(c) = c^2 \\|w\\|^2 + 2c \\operatorname{Re}\\langle u, w \\rangle$ is non-negative for all $c \\in \\mathbb{R}$.<br>
A parabola with no constant term can remain non-negative for both positive and negative $c$ if and only if its linear coefficient vanishes:
$$\\operatorname{Re}\\langle u, w \\rangle = 0$$
(Over $\\mathbb{C}$, applying the same argument with imaginary scalars $ic$ yields $\\operatorname{Im}\\langle u, w \\rangle = 0$).<br>
Therefore:
<span class=\"ans\">$$\\langle u, w \\rangle = 0 \\implies \\operatorname{range}(P) \\perp \\operatorname{null}(P)$$</span>
Thus $P$ is strictly an <strong>orthogonal projection</strong>.</p>

<p><span class="part">Part (b): Symmetry and Idempotence of Matrix $P$</span><br>
1. <strong>Symmetry:</strong>
$$P^\\top = \\left( A (A^\\top A)^{-1} A^\\top \\right)^\\top = (A^\\top)^\\top \\left( (A^\\top A)^{-1} \\right)^\\top A^\\top = A \\left( (A^\\top A)^\\top \\right)^{-1} A^\\top$$
Since $(A^\\top A)^\\top = A^\\top (A^\\top)^\\top = A^\\top A$:
<span class=\"ans\">$$P^\\top = A (A^\\top A)^{-1} A^\\top = P$$</span>
2. <strong>Idempotence:</strong>
$$P^2 = \\left( A(A^\\top A)^{-1} A^\\top \\right) \\left( A(A^\\top A)^{-1} A^\\top \\right) = A(A^\\top A)^{-1} \\underbrace{(A^\\top A) (A^\\top A)^{-1}}_{I} A^\\top$$
<span class=\"ans\">$$P^2 = A(A^\\top A)^{-1} A^\\top = P$$</span></p>

<p><span class="part">Part (c): Eigenvalues, Trace & Multiplicities</span><br>
1. <strong>Eigenvalues:</strong> Since $P^2 = P$, any eigenvalue satisfies $\\lambda^2 = \\lambda \\implies <span class=\"ans\">\\lambda \\in \\{0, 1\\}</span>$.<br>
2. <strong>Trace via Cyclic Property:</strong>
$$\\operatorname{Tr}(P) = \\operatorname{Tr}\\left( A (A^\\top A)^{-1} A^\\top \\right) = \\operatorname{Tr}\\left( (A^\\top A)^{-1} (A^\\top A) \\right) = \\operatorname{Tr}(I_n) = <span class=\"ans\">n</span>$$
3. <strong>Multiplicities:</strong><br>
Since $P$ is symmetric, it is diagonalizable. The sum of its eigenvalues equals its trace:
- Eigenvalue $\\lambda = 1$ has algebraic and geometric multiplicity equal to <span class=\"ans\">$n$</span> (eigenspace is $\\operatorname{range}(A)$).
- Eigenvalue $\\lambda = 0$ has algebraic and geometric multiplicity equal to <span class=\"ans\">$m - n$</span> (eigenspace is $\\operatorname{null}(A^\\top)$).</p>""",
        "takeaway": "An idempotent operator is an orthogonal projection if and only if it is norm-contractive (||Pv|| <= ||v||). The projection matrix P = A(A^T A)^(-1) A^T is symmetric and idempotent, with trace n and eigenvalues 1 (multiplicity n) and 0 (multiplicity m-n)."
    },

    # =========================================================================
    # TOPIC 12: Adjoints, Self-Adjoint, and Normal Operators
    # =========================================================================
    {
        "id": 21291,
        "subject": "LAA",
        "topicId": "12_Adjoints_Self_Adjoint_and_Normal_Operators",
        "topicTitle": "12 · Adjoints & Normal Operators",
        "title": "Real Eigenvalue Proof for Self-Adjoint Operators (IISc Endsem 2024 / Axler 7.13)",
        "kind2": "pyq",
        "source": "IISc Endsem 2024 / Axler Linear Algebra Done Right 7.13",
        "marks": "[6 Marks]",
        "question": """<p>Let $V$ be a finite-dimensional inner product space over $\\mathbb{C}$, and let $T \\in \\mathcal{L}(V)$ be a self-adjoint operator ($T = T^*$).</p>
<p><span class="part">(a)</span> State the definition of the adjoint operator $T^*$ via the inner product relationship.</p>
<p><span class="part">(b)</span> Let $\\lambda \\in \\mathbb{C}$ be an eigenvalue of $T$ with eigenvector $v \\ne 0$. Evaluate $\\langle Tv, v \\rangle$ in two different ways to prove rigorously that $\\lambda$ must be a real number ($\\lambda \\in \\mathbb{R}$).</p>
<p><span class="part">(c)</span> Prove that eigenvectors of a self-adjoint operator corresponding to distinct eigenvalues are mutually orthogonal.</p>""",
        "solution": """<p><span class="part">Part (a): Definition of Adjoint Operator</span><br>
For any linear operator $T \\in \\mathcal{L}(V)$, the adjoint $T^* \\in \\mathcal{L}(V)$ is the unique operator satisfying:
<span class=\"ans\">$$\\langle Tv, w \\rangle = \\langle v, T^* w \\rangle \\quad \\text{for all } v, w \\in V$$</span>
An operator is <strong>self-adjoint</strong> (Hermitian) if $T = T^*$.</p>

<p><span class="part">Part (b): Proof that Eigenvalues are Strictly Real</span><br>
Let $Tv = \\lambda v$ with $v \\ne 0$. Compute the scalar $\\langle Tv, v \\rangle$:<br>
1. <strong>Direct substitution of $Tv = \\lambda v$:</strong>
$$\\langle Tv, v \\rangle = \\langle \\lambda v, v \\rangle = \\lambda \\langle v, v \\rangle = \\lambda \\|v\\|^2$$
2. <strong>Using the self-adjoint property $T = T^*$:</strong>
$$\\langle Tv, v \\rangle = \\langle v, T^* v \\rangle = \\langle v, Tv \\rangle = \\langle v, \\lambda v \\rangle = \\overline{\\lambda} \\langle v, v \\rangle = \\overline{\\lambda} \\|v\\|^2$$
Equating both expressions:
$$\\lambda \\|v\\|^2 = \\overline{\\lambda} \\|v\\|^2 \\implies (\\lambda - \\overline{\\lambda}) \\|v\\|^2 = 0$$
Since $v$ is an eigenvector, $v \\ne 0 \\implies \\|v\\|^2 > 0$. Therefore:
$$\\lambda - \\overline{\\lambda} = 0 \\implies <span class=\"ans\">\\lambda = \\overline{\\lambda}</span>$$
A complex number equals its complex conjugate if and only if its imaginary part is zero.<br>
Hence:
<span class=\"ans\">$$\\lambda \\in \\mathbb{R}$$</span>
Every eigenvalue of a self-adjoint operator is strictly real.</p>

<p><span class="part">Part (c): Orthogonality of Eigenvectors</span><br>
Suppose $Tu = \\lambda u$ and $Tv = \\mu v$ with $\\lambda \\ne \\mu$ (where $\\lambda, \\mu \\in \\mathbb{R}$).
$$\\langle Tu, v \\rangle = \\langle \\lambda u, v \\rangle = \\lambda \\langle u, v \\rangle$$
Using $T = T^*$:
$$\\langle Tu, v \\rangle = \\langle u, T^* v \\rangle = \\langle u, Tv \\rangle = \\langle u, \\mu v \\rangle = \\overline{\\mu} \\langle u, v \\rangle = \\mu \\langle u, v \\rangle$$
Equating both results:
$$\\lambda \\langle u, v \\rangle = \\mu \\langle u, v \\rangle \\implies (\\lambda - \\mu) \\langle u, v \\rangle = 0$$
Since $\\lambda \\ne \\mu$, we must have:
<span class=\"ans\">$$\\langle u, v \\rangle = 0$$</span>
Eigenvectors corresponding to distinct eigenvalues are mutually orthogonal.</p>""",
        "takeaway": "Self-adjoint operators T = T* have exclusively real eigenvalues (lambda = lambda_bar) and their eigenvectors corresponding to distinct eigenvalues are mutually orthogonal."
    },
    {
        "id": 21292,
        "subject": "LAA",
        "topicId": "12_Adjoints_Self_Adjoint_and_Normal_Operators",
        "topicTitle": "12 · Adjoints & Normal Operators",
        "title": "Normal Operator Conjugate Eigenvalue Identity & Norm Preservation (MIT 18.06 / Axler 7.20)",
        "kind2": "pyq",
        "source": "MIT 18.06 Linear Algebra / Axler Linear Algebra Done Right 7.20",
        "marks": "[8 Marks]",
        "question": """<p>Let $V$ be a finite-dimensional inner product space. A linear operator $T \\in \\mathcal{L}(V)$ is called <strong>normal</strong> if it commutes with its adjoint:
$$T T^* = T^* T$$</p>
<p><span class="part">(a)</span> Prove that $T$ is normal if and only if $\\|Tv\\| = \\|T^* v\\|$ for all $v \\in V$.</p>
<p><span class="part">(b)</span> Prove that if $T$ is normal, the shifted operator $S = T - \\lambda I$ is also normal for any scalar $\\lambda \\in \\mathbb{F}$.</p>
<p><span class="part">(c)</span> Prove that if $v$ is an eigenvector of normal operator $T$ with eigenvalue $\\lambda$ ($Tv = \\lambda v$), then $v$ is automatically an eigenvector of $T^*$ with conjugate eigenvalue $\\bar{\\lambda}$:
$$T^* v = \\overline{\\lambda} v$$</p>""",
        "solution": """<p><span class="part">Part (a): Norm Preservation Characterization of Normality</span><br>
Expand the difference of squared norms:
$$\\|Tv\\|^2 - \\|T^* v\\|^2 = \\langle Tv, Tv \\rangle - \\langle T^* v, T^* v \\rangle = \\langle v, T^* T v \\rangle - \\langle v, (T^*)^* T^* v \\rangle = \\langle v, (T^* T - T T^*) v \\rangle$$
- If $T T^* = T^* T$, then $T^* T - T T^* = 0$, so $\\|Tv\\|^2 - \\|T^* v\\|^2 = \\langle v, 0 \\rangle = 0 \\implies <span class=\"ans\">\\|Tv\\| = \\|T^* v\\|</span>$.<br>
- Conversely, if $\\|Tv\\| = \\|T^* v\\|$ for all $v$, then $\\langle v, (T^* T - T T^*) v \\rangle = 0$ for all $v$. For self-adjoint difference operators, this forces $T^* T - T T^* = 0 \\implies T T^* = T^* T$.</p>

<p><span class="part">Part (b): Normality of Shifted Operator $S = T - \\lambda I$</span><br>
The adjoint of $S$ is $S^* = (T - \\lambda I)^* = T^* - \\overline{\\lambda} I$. Compute $S S^*$:
$$S S^* = (T - \\lambda I)(T^* - \\overline{\\lambda} I) = T T^* - \\overline{\\lambda} T - \\lambda T^* + |\\lambda|^2 I$$
Compute $S^* S$:
$$S^* S = (T^* - \\overline{\\lambda} I)(T - \\lambda I) = T^* T - \\lambda T^* - \\overline{\\lambda} T + |\\lambda|^2 I$$
Since $T$ is normal ($T T^* = T^* T$):
<span class=\"ans\">$$S S^* = S^* S$$</span>
Thus $S = T - \\lambda I$ is strictly normal.</p>

<p><span class="part">Part (c): Conjugate Eigenvalue Proof</span><br>
Apply the norm characterization from Part (a) to the normal operator $S = T - \\lambda I$:
$$\\|S v\\| = \\|S^* v\\| \\iff \\|(T - \\lambda I) v\\| = \\|(T^* - \\overline{\\lambda} I) v\\| \\quad \\text{for all } v \\in V$$
Suppose $v$ is an eigenvector of $T$ with eigenvalue $\\lambda$:
$$(T - \\lambda I)v = 0 \\implies \\|(T - \\lambda I)v\\| = 0$$
By the norm equality:
$$\\|(T^* - \\overline{\\lambda} I)v\\| = \\|(T - \\lambda I)v\\| = 0$$
Since the norm of a vector is zero if and only if the vector itself is zero:
$$(T^* - \\overline{\\lambda} I)v = 0 \\implies <span class=\"ans\">T^* v = \\overline{\\lambda} v</span>$$
The same eigenvector $v$ is an eigenvector of $T^*$ with conjugate eigenvalue $\\overline{\\lambda}$.</p>""",
        "takeaway": "An operator is normal if and only if ||Tv|| = ||T* v|| for all vectors. Consequently, T and T* share the exact same eigenvectors, with corresponding eigenvalues being complex conjugates: Tv = lambda v <=> T* v = lambda_bar v."
    },
    {
        "id": 21293,
        "subject": "LAA",
        "topicId": "12_Adjoints_Self_Adjoint_and_Normal_Operators",
        "topicTitle": "12 · Adjoints & Normal Operators",
        "title": "Fundamental Subspaces of Normal Operators & Spectral Resolution (Generated IISc / Berkeley EECS 127 & Stanford EE263)",
        "kind2": "generated",
        "source": "Generated IISc Midterm / Berkeley EECS 127 & Stanford EE263",
        "marks": "[8 Marks]",
        "question": """<p><span class="part">(a)</span> For any normal operator $T \\in \\mathcal{L}(V)$ on a finite-dimensional inner product space, prove that:
$$\\operatorname{null}(T) = \\operatorname{null}(T^*) \\qquad \\text{and} \\qquad \\operatorname{range}(T) = \\operatorname{range}(T^*)$$</p>
<p><span class="part">(b)</span> For the symmetric matrix $A = \\begin{pmatrix} 1 & 2 \\\\ 2 & 1 \\end{pmatrix}$, compute its eigenvalues $\\lambda_1, \\lambda_2$ and a normalized orthonormal eigenbasis $(u_1, u_2)$.</p>
<p><span class="part">(c)</span> Write the explicit <strong>spectral decomposition</strong> (spectral resolution) of $A$ in terms of outer products $A = \\lambda_1 u_1 u_1^\\top + \\lambda_2 u_2 u_2^\\top$, and verify the matrix sum.</p>""",
        "solution": """<p><span class="part">Part (a): Fundamental Subspace Equalities for Normal Operators</span><br>
1. <strong>Null spaces: $\\operatorname{null}(T) = \\operatorname{null}(T^*)$:</strong><br>
Since $T$ is normal, $\\|Tv\\| = \\|T^* v\\|$ for all $v \\in V$.
$$v \\in \\operatorname{null}(T) \\iff Tv = 0 \\iff \\|Tv\\| = 0 \\iff \\|T^* v\\| = 0 \\iff T^* v = 0 \\iff v \\in \\operatorname{null}(T^*)$$
Therefore:
<span class=\"ans\">$$\\operatorname{null}(T) = \\operatorname{null}(T^*)$$</span>
2. <strong>Ranges: $\\operatorname{range}(T) = \\operatorname{range}(T^*)$:</strong><br>
By the Fundamental Subspace Theorem of linear algebra, for any linear operator:
$$\\operatorname{range}(T) = (\\operatorname{null}(T^*))^\\perp$$
Substituting $\\operatorname{null}(T^*) = \\operatorname{null}(T)$:
$$\\operatorname{range}(T) = (\\operatorname{null}(T))^\\perp$$
Applying the same relation to $T^*$:
$$\\operatorname{range}(T^*) = (\\operatorname{null}((T^*)^*))^\\perp = (\\operatorname{null}(T))^\\perp$$
Comparing both identities:
<span class=\"ans\">$$\\operatorname{range}(T) = \\operatorname{range}(T^*)$$</span></p>

<p><span class="part">Part (b): Eigendecomposition of $A$</span><br>
Matrix $A = \\begin{pmatrix} 1 & 2 \\\\ 2 & 1 \\end{pmatrix}$.
$$\\det(A - \\lambda I) = (1 - \\lambda)^2 - 4 = \\lambda^2 - 2\\lambda - 3 = (\\lambda - 3)(\\lambda + 1) = 0$$
Eigenvalues: $\\lambda_1 = 3, \\lambda_2 = -1$.
1. <strong>For $\\lambda_1 = 3$:</strong>
$$(A - 3I)v_1 = \\begin{pmatrix} -2 & 2 \\\\ 2 & -2 \\end{pmatrix} v_1 = 0 \\implies v_1 = \\begin{pmatrix} 1 \\\\ 1 \\end{pmatrix} \\implies u_1 = <span class=\"ans\">\\frac{1}{\\sqrt{2}} \\begin{pmatrix} 1 \\\\ 1 \\end{pmatrix}</span>$$
2. <strong>For $\\lambda_2 = -1$:</strong>
$$(A + I)v_2 = \\begin{pmatrix} 2 & 2 \\\\ 2 & 2 \\end{pmatrix} v_2 = 0 \\implies v_2 = \\begin{pmatrix} -1 \\\\ 1 \\end{pmatrix} \\implies u_2 = <span class=\"ans\">\\frac{1}{\\sqrt{2}} \\begin{pmatrix} -1 \\\\ 1 \\end{pmatrix}</span>$$
Orthonormality check: $\\|u_1\\| = 1, \\|u_2\\| = 1, u_1^\\top u_2 = \\frac{1}{2}(-1 + 1) = 0$.</p>

<p><span class="part">Part (c): Spectral Resolution Outer Products</span><br>
Compute the rank-1 orthogonal projection operators:
$$P_1 = u_1 u_1^\\top = \\frac{1}{2} \\begin{pmatrix} 1 \\\\ 1 \\end{pmatrix} \\begin{pmatrix} 1 & 1 \\end{pmatrix} = \\frac{1}{2} \\begin{pmatrix} 1 & 1 \\\\ 1 & 1 \\end{pmatrix} = \\begin{pmatrix} 1/2 & 1/2 \\\\ 1/2 & 1/2 \\end{pmatrix}$$
$$P_2 = u_2 u_2^\\top = \\frac{1}{2} \\begin{pmatrix} -1 \\\\ 1 \\end{pmatrix} \\begin{pmatrix} -1 & 1 \\end{pmatrix} = \\frac{1}{2} \\begin{pmatrix} 1 & -1 \\\\ -1 & 1 \\end{pmatrix} = \\begin{pmatrix} 1/2 & -1/2 \\\\ -1/2 & 1/2 \\end{pmatrix}$$
The spectral decomposition is:
<span class=\"ans\">$$A = 3 P_1 - 1 P_2 = 3 \\left( u_1 u_1^\\top \\right) - 1 \\left( u_2 u_2^\\top \\right)$$</span>
<strong>Verification:</strong>
$$3 P_1 - P_2 = \\begin{pmatrix} 3/2 & 3/2 \\\\ 3/2 & 3/2 \\end{pmatrix} - \\begin{pmatrix} 1/2 & -1/2 \\\\ -1/2 & 1/2 \\end{pmatrix} = \\begin{pmatrix} 3/2 - 1/2 & 3/2 - (-1/2) \\\\ 3/2 - (-1/2) & 3/2 - 1/2 \\end{pmatrix} = \\begin{pmatrix} 1 & 2 \\\\ 2 & 1 \\end{pmatrix} = A$$
The matrix sum matches $A$ identically.</p>""",
        "takeaway": "Normal operators satisfy null(T) = null(T*) and range(T) = range(T*). Every real symmetric matrix has a spectral resolution A = sum lambda_i u_i u_i^T into rank-1 orthogonal projections onto its eigenspaces."
    }
]

def main():
    with open(PRACTICE_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    if "21191" in content:
        print("Batch 11-12 already present in practice_laa.js!")
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
    for card in PRACTICE_LAA_11_12:
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

    print("Successfully added LAA Batch 11-12 (6 cards). Total in file now updated.")

if __name__ == "__main__":
    main()
