#!/usr/bin/env python3
"""
Builder script for LAA Practice Cards: Batch 07 (Topics 13 & 14)
Topic 13: The Spectral Theorem (Real and Complex) (Cards 21391, 21392, 21393)
Topic 14: Positive Operators and Isometries (Cards 21491, 21492, 21493)
"""

import json
import os
import re

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRACTICE_FILE = os.path.join(REPO_DIR, "practice_laa.js")

PRACTICE_LAA_13_14 = [
    # =========================================================================
    # TOPIC 13: The Spectral Theorem (Real and Complex)
    # =========================================================================
    {
        "id": 21391,
        "subject": "LAA",
        "topicId": "13_The_Spectral_Theorem_Real_and_Complex",
        "topicTitle": "13 · The Spectral Theorem",
        "title": "Symmetric Quadratic Form Vanishing Implies Zero Operator (IISc Endsem 2024 / Axler 7.B)",
        "kind2": "pyq",
        "source": "IISc Endsem 2024 / Axler Linear Algebra Done Right 7.B",
        "marks": "[6 Marks]",
        "question": """<p>Let $A \\in \\mathbb{R}^{n \\times n}$ be a symmetric matrix such that $x^\\top A x = 0$ for all $x \\in \\mathbb{R}^n$.</p>
<p><span class="part">(a)</span> Using the Real Spectral Theorem, prove rigorously that $A = 0$.</p>
<p><span class="part">(b)</span> Show by providing an explicit non-zero counterexample matrix in $\\mathbb{R}^{2 \\times 2}$ that the symmetry assumption is indispensable over the real field $\\mathbb{R}$.</p>
<p><span class="part">(c)</span> Explain why over the complex field $\\mathbb{C}$, the condition $\\langle Tv, v \\rangle = 0$ for all $v \\in V$ forces $T = 0$ even without assuming that $T$ is self-adjoint.</p>""",
        "solution": """<p><span class="part">Part (a): Real Spectral Theorem Proof</span><br>
By the Real Spectral Theorem, any real symmetric matrix $A = A^\\top$ has an orthonormal eigenbasis $(q_1, \\dots, q_n)$ of $\\mathbb{R}^n$ with corresponding real eigenvalues $\\lambda_1, \\dots, \\lambda_n$ such that $A q_i = \\lambda_i q_i$.<br>
Evaluate the quadratic form $x^\\top A x$ at each orthonormal eigenvector $q_i$:
$$0 = q_i^\\top A q_i = q_i^\\top (\\lambda_i q_i) = \\lambda_i \\|q_i\\|^2 = \\lambda_i (1) = \\lambda_i$$
Since every eigenvalue is identically zero ($\\lambda_i = 0$ for all $i \\in \\{1, \\dots, n\\}$), the diagonal eigenvalue matrix is $\\Lambda = 0$.<br>
Since $A$ is orthogonally diagonalizable:
<span class=\"ans\">$$A = Q \\Lambda Q^\\top = Q (0) Q^\\top = 0$$</span></p>

<p><span class="part">Part (b): Non-Symmetric Counterexample over $\\mathbb{R}$</span><br>
Consider the non-zero skew-symmetric matrix:
$$A = \\begin{pmatrix} 0 & 1 \\\\ -1 & 0 \\end{pmatrix} \\ne 0$$
For any arbitrary real vector $x = \\begin{pmatrix} x_1 \\\\ x_2 \\end{pmatrix} \\in \\mathbb{R}^2$:
$$x^\\top A x = \\begin{pmatrix} x_1 & x_2 \\end{pmatrix} \\begin{pmatrix} x_2 \\\\ -x_1 \\end{pmatrix} = x_1 x_2 - x_2 x_1 = 0$$
The quadratic form vanishes identically for every $x \\in \\mathbb{R}^2$, yet $A \\ne 0$.<br>
Hence, <span class=\"ans\">symmetry is strictly indispensable</span> over $\\mathbb{R}$.</p>

<p><span class="part">Part (c): Contrast with Complex Inner Product Spaces</span><br>
Over $\\mathbb{C}$, the inner product satisfies the complex polarization identity:
$$\\langle Tu, w \\rangle = \\frac{1}{4} \\sum_{k=0}^3 i^k \\langle T(u + i^k w), u + i^k w \\rangle$$
If $\\langle Tv, v \\rangle = 0$ for all $v \\in V$, each term in the linear combination vanishes, forcing:
$$\\langle Tu, w \\rangle = 0 \\quad \\text{for all } u, w \\in V$$
Setting $w = Tu$ yields $\\|Tu\\|^2 = 0 \\implies Tu = 0$ for all $u$, so <span class=\"ans\">$T = 0$</span>.<br>
Over $\\mathbb{R}$, polarization only recovers the symmetric part $\\frac{1}{2}(T + T^*)$, so $x^\\top A x = 0$ only guarantees that the skew-symmetric component remains.</p>""",
        "takeaway": "Over the real field, x^T A x = 0 for all x implies A = 0 if and only if A is symmetric. In contrast, over the complex field C, <Tv, v> = 0 for all v implies T = 0 unconditionally via the complex polarization identity."
    },
    {
        "id": 21392,
        "subject": "LAA",
        "topicId": "13_The_Spectral_Theorem_Real_and_Complex",
        "topicTitle": "13 · The Spectral Theorem",
        "title": "Spectral Decomposition & Orthogonal Projectors (MIT 18.06 / Strang L25)",
        "kind2": "pyq",
        "source": "MIT 18.06 Linear Algebra / Strang Lecture 25",
        "marks": "[8 Marks]",
        "question": """<p>Consider the symmetric matrix $A = \\begin{pmatrix} 3 & 1 \\\\ 1 & 3 \\end{pmatrix} \\in \\mathbb{R}^{2 \\times 2}$.</p>
<p><span class="part">(a)</span> Compute the eigenvalues $\\lambda_1, \\lambda_2$ and corresponding orthonormal eigenvectors $q_1, q_2$.</p>
<p><span class="part">(b)</span> Construct the rank-1 orthogonal projection matrices $P_1 = q_1 q_1^\\top$ and $P_2 = q_2 q_2^\\top$, and verify the resolution of identity $P_1 + P_2 = I$ and orthogonality $P_1 P_2 = 0$.</p>
<p><span class="part">(c)</span> Express $A$ as the spectral sum $A = \\lambda_1 P_1 + \\lambda_2 P_2$, and use this decomposition to compute $A^5$ and $A^{-1}$ without direct matrix multiplications or inverses.</p>""",
        "solution": """<p><span class="part">Part (a): Eigensystem Calculation</span><br>
Compute the characteristic polynomial:
$$\\det(A - \\lambda I) = (3 - \\lambda)^2 - 1 = \\lambda^2 - 6\\lambda + 8 = (\\lambda - 4)(\\lambda - 2) = 0$$
Eigenvalues: $\\lambda_1 = 4, \\lambda_2 = 2$.<br>
1. <strong>For $\\lambda_1 = 4$:</strong>
$$(A - 4I)v_1 = \\begin{pmatrix} -1 & 1 \\\\ 1 & -1 \\end{pmatrix} v_1 = 0 \\implies v_1 = \\begin{pmatrix} 1 \\\\ 1 \\end{pmatrix} \\implies q_1 = <span class=\"ans\">\\frac{1}{\\sqrt{2}} \\begin{pmatrix} 1 \\\\ 1 \\end{pmatrix}</span>$$
2. <strong>For $\\lambda_2 = 2$:</strong>
$$(A - 2I)v_2 = \\begin{pmatrix} 1 & 1 \\\\ 1 & 1 \\end{pmatrix} v_2 = 0 \\implies v_2 = \\begin{pmatrix} -1 \\\\ 1 \\end{pmatrix} \\implies q_2 = <span class=\"ans\">\\frac{1}{\\sqrt{2}} \\begin{pmatrix} -1 \\\\ 1 \\end{pmatrix}</span>$$</p>

<p><span class="part">Part (b): Rank-1 Orthogonal Projection Matrices</span><br>
Compute $P_1 = q_1 q_1^\\top$:
$$P_1 = \\frac{1}{2} \\begin{pmatrix} 1 \\\\ 1 \\end{pmatrix} \\begin{pmatrix} 1 & 1 \\end{pmatrix} = <span class=\"ans\">\\begin{pmatrix} 1/2 & 1/2 \\\\ 1/2 & 1/2 \\end{pmatrix}</span>$$
Compute $P_2 = q_2 q_2^\\top$:
$$P_2 = \\frac{1}{2} \\begin{pmatrix} -1 \\\\ 1 \\end{pmatrix} \\begin{pmatrix} -1 & 1 \\end{pmatrix} = <span class=\"ans\">\\begin{pmatrix} 1/2 & -1/2 \\\\ -1/2 & 1/2 \\end{pmatrix}</span>$$
<strong>Verifications:</strong>
$$P_1 + P_2 = \\begin{pmatrix} 1/2 + 1/2 & 1/2 - 1/2 \\\\ 1/2 - 1/2 & 1/2 + 1/2 \\end{pmatrix} = \\begin{pmatrix} 1 & 0 \\\\ 0 & 1 \\end{pmatrix} = <span class=\"ans\">I_2</span>$$
$$P_1 P_2 = \\frac{1}{4} \\begin{pmatrix} 1 & 1 \\\\ 1 & 1 \\end{pmatrix} \\begin{pmatrix} 1 & -1 \\\\ -1 & 1 \\end{pmatrix} = \\frac{1}{4} \\begin{pmatrix} 0 & 0 \\\\ 0 & 0 \\end{pmatrix} = <span class=\"ans\">0</span>$$</p>

<p><span class="part">Part (c): Spectral Sum, Power & Inverse</span><br>
The spectral representation is:
$$A = 4 P_1 + 2 P_2 = 4 \\begin{pmatrix} 1/2 & 1/2 \\\\ 1/2 & 1/2 \\end{pmatrix} + 2 \\begin{pmatrix} 1/2 & -1/2 \\\\ -1/2 & 1/2 \\end{pmatrix} = \\begin{pmatrix} 2 & 2 \\\\ 2 & 2 \\end{pmatrix} + \\begin{pmatrix} 1 & -1 \\\\ -1 & 1 \\end{pmatrix} = \\begin{pmatrix} 3 & 1 \\\\ 1 & 3 \\end{pmatrix}$$
Because $P_i P_j = \\delta_{ij} P_i$, powers and functions of $A$ act directly on the scalars $\\lambda_i$:
1. <strong>Fifth Power $A^5$:</strong>
$$A^5 = 4^5 P_1 + 2^5 P_2 = 1024 P_1 + 32 P_2$$
$$A^5 = 1024 \\begin{pmatrix} 1/2 & 1/2 \\\\ 1/2 & 1/2 \\end{pmatrix} + 32 \\begin{pmatrix} 1/2 & -1/2 \\\\ -1/2 & 1/2 \\end{pmatrix} = <span class=\"ans\">\\begin{pmatrix} 528 & 496 \\\\ 496 & 528 \\end{pmatrix}</span>$$
2. <strong>Inverse $A^{-1}$:</strong>
$$A^{-1} = 4^{-1} P_1 + 2^{-1} P_2 = \\frac{1}{4} \\begin{pmatrix} 1/2 & 1/2 \\\\ 1/2 & 1/2 \\end{pmatrix} + \\frac{1}{2} \\begin{pmatrix} 1/2 & -1/2 \\\\ -1/2 & 1/2 \\end{pmatrix} = <span class=\"ans\">\\begin{pmatrix} 3/8 & -1/8 \\\\ -1/8 & 3/8 \\end{pmatrix}</span>$$</p>""",
        "takeaway": "The Spectral Theorem decomposes a symmetric matrix into mutually orthogonal projection matrices: A = sum lambda_i P_i with sum P_i = I and P_i P_j = delta_ij P_i. Any analytic function evaluates via f(A) = sum f(lambda_i) P_i."
    },
    {
        "id": 21393,
        "subject": "LAA",
        "topicId": "13_The_Spectral_Theorem_Real_and_Complex",
        "topicTitle": "13 · The Spectral Theorem",
        "title": "Rayleigh Quotient Extremum & Commuting Symmetric Matrices (Generated IISc / Stanford EE263 & Berkeley EECS 127)",
        "kind2": "generated",
        "source": "Generated IISc Midterm / Stanford EE263 & Berkeley EECS 127",
        "marks": "[8 Marks]",
        "question": """<p><span class="part">(a)</span> Let $A \\in \\mathbb{R}^{n \\times n}$ be symmetric with sorted eigenvalues $\\lambda_1 \\le \\lambda_2 \\le \\dots \\le \\lambda_n$. Prove that:
$$\\max_{x \\ne 0} \\frac{x^\\top A x}{x^\\top x} = \\lambda_n = \\lambda_{\\max}(A) \\qquad \\text{and} \\qquad \\min_{x \\ne 0} \\frac{x^\\top A x}{x^\\top x} = \\lambda_1 = \\lambda_{\\min}(A)$$
and demonstrate that the extrema are achieved at the corresponding eigenvectors.</p>
<p><span class="part">(b)</span> Let $A, B \\in \\mathbb{R}^{n \\times n}$ be symmetric matrices. Prove that their product $AB$ is symmetric if and only if $A$ and $B$ commute ($AB = BA$).</p>
<p><span class="part">(c)</span> If symmetric matrices $A$ and $B$ commute, prove that they share a simultaneous orthonormal eigenbasis.</p>""",
        "solution": """<p><span class="part">Part (a): Rayleigh Quotient Extremum</span><br>
Let $(q_1, \\dots, q_n)$ be an orthonormal eigenbasis for $A$ with $A q_i = \\lambda_i q_i$.<br>
Any unit vector $x$ ($\\|x\\|^2 = x^\\top x = 1$) expands uniquely as $x = \\sum_{i=1}^n c_i q_i$ with $\\sum_{i=1}^n c_i^2 = 1$.<br>
Evaluate the quadratic form:
$$x^\\top A x = \\left( \\sum_{i=1}^n c_i q_i^\\top \\right) \\left( \\sum_{j=1}^n c_j \\lambda_j q_j \\right) = \\sum_{i=1}^n \\lambda_i c_i^2$$
Since $\\lambda_1 \\le \\lambda_i \\le \\lambda_n$ and $c_i^2 \\ge 0$:
$$\\lambda_1 = \\lambda_1 \\sum_{i=1}^n c_i^2 \\le \\sum_{i=1}^n \\lambda_i c_i^2 \\le \\lambda_n \\sum_{i=1}^n c_i^2 = \\lambda_n$$
- Setting $x = q_n$ gives $c_n = 1$ and $c_i = 0$ for $i < n$, achieving $q_n^\\top A q_n = \\lambda_n = <span class=\"ans\">\\lambda_{\\max}(A)</span>$.<br>
- Setting $x = q_1$ gives $c_1 = 1$ and $c_i = 0$ for $i > 1$, achieving $q_1^\\top A q_1 = \\lambda_1 = <span class=\"ans\">\\lambda_{\\min}(A)</span>$.</p>

<p><span class="part">Part (b): Symmetry of Product Matrix</span><br>
Take the transpose of the product $AB$:
$$(AB)^\\top = B^\\top A^\\top$$
Since $A$ and $B$ are symmetric, $A^\\top = A$ and $B^\\top = B$:
$$(AB)^\\top = BA$$
Hence:
$$(AB)^\\top = AB \\iff <span class=\"ans\">BA = AB \\iff AB = BA</span>$$
The product of two symmetric matrices is symmetric if and only if they commute.</p>

<p><span class="part">Part (c): Simultaneous Orthonormal Eigenbasis</span><br>
By the Real Spectral Theorem, $\\mathbb{R}^n = \\bigoplus_{i=1}^k E(\\mu_i, A)$, where each distinct eigenspace $E(\\mu_i, A)$ is mutually orthogonal.<br>
For any $v \\in E(\\mu_i, A)$, we have $A v = \\mu_i v$. Using the commuting assumption $AB = BA$:
$$A(B v) = B(A v) = B(\\mu_i v) = \\mu_i (B v)$$
Thus $B v \\in E(\\mu_i, A)$, proving that each eigenspace $E(\\mu_i, A)$ is $B$-invariant.<br>
Since $B$ is symmetric on $\\mathbb{R}^n$, the restricted operator $B|_{E(\\mu_i, A)}$ is self-adjoint with respect to the standard inner product on $E(\\mu_i, A)$.<br>
By the Real Spectral Theorem applied to each restricted operator, each $E(\\mu_i, A)$ has an orthonormal basis of eigenvectors of $B$.<br>
Taking the union of these orthonormal bases over all orthogonal subspaces $E(\\mu_i, A)$ yields an orthonormal basis of $\\mathbb{R}^n$ consisting of vectors that are eigenvectors of both $A$ and $B$ simultaneously.</p>""",
        "takeaway": "The Rayleigh quotient x^T A x / x^T x is bounded between lambda_min and lambda_max. Furthermore, two symmetric matrices commute if and only if their product is symmetric, which is geometrically equivalent to possessing a simultaneous orthonormal eigenbasis."
    },

    # =========================================================================
    # TOPIC 14: Positive Operators and Isometries
    # =========================================================================
    {
        "id": 21491,
        "subject": "LAA",
        "topicId": "14_Positive_Operators_and_Isometries",
        "topicTitle": "14 · Positive Operators & Isometries",
        "title": "Gram Operator Positivity & Injectivity Equivalence (IISc Midterm 2 / Axler 7.C)",
        "kind2": "pyq",
        "source": "IISc Midterm 2 / Axler Linear Algebra Done Right 7.C",
        "marks": "[8 Marks]",
        "question": """<p>Let $V$ be a finite-dimensional inner product space and let $T \\in \\mathcal{L}(V)$ be an arbitrary linear operator.</p>
<p><span class="part">(a)</span> Prove that the operator $T^* T$ is self-adjoint and positive semidefinite ($T^* T \\ge 0$).</p>
<p><span class="part">(b)</span> Prove that $T^* T$ is strictly positive definite ($T^* T > 0$) if and only if $T$ is injective.</p>
<p><span class="part">(c)</span> Deduce that $\\operatorname{null}(T^* T) = \\operatorname{null}(T)$ and $\\operatorname{rank}(T^* T) = \\operatorname{rank}(T)$.</p>""",
        "solution": """<p><span class="part">Part (a): Self-Adjointness and Positivity</span><br>
1. <strong>Self-adjointness:</strong>
$$(T^* T)^* = T^* (T^*)^* = T^* T$$
Thus $T^* T$ is self-adjoint.<br>
2. <strong>Positivity:</strong>
For any vector $v \\in V$:
$$\\langle T^* T v, v \\rangle = \\langle Tv, Tv \\rangle = \\|Tv\\|^2$$
Since the norm squared is always non-negative:
$$\\langle T^* T v, v \\rangle = \\|Tv\\|^2 \\ge 0 \\quad \\text{for all } v \\in V$$
Therefore, <span class=\"ans\">$T^* T \\ge 0$</span> (positive semidefinite).</p>

<p><span class="part">Part (b): Strict Positivity Equivalence</span><br>
By definition, $T^* T > 0 \\iff \\langle T^* T v, v \\rangle > 0$ for all $v \\ne 0$.<br>
Using the identity from Part (a):
$$\\|Tv\\|^2 > 0 \\quad \\text{for all } v \\ne 0 \\iff Tv \\ne 0 \\quad \\text{for all } v \\ne 0$$
This is precisely the condition that the null space contains only the zero vector:
$$\\operatorname{null}(T) = \\{0\\} \\iff <span class=\"ans\">T \\text{ is injective}</span>$$
Thus $T^* T > 0$ if and only if $T$ is injective.</p>

<p><span class="part">Part (c): Null Space & Rank Equality</span><br>
1. If $v \\in \\operatorname{null}(T)$, then $Tv = 0 \\implies T^*(Tv) = T^*(0) = 0 \\implies v \\in \\operatorname{null}(T^* T)$. Thus $\\operatorname{null}(T) \\subseteq \\operatorname{null}(T^* T)$.<br>
2. Conversely, suppose $v \\in \\operatorname{null}(T^* T)$, so $T^* T v = 0$. Take the inner product with $v$:
$$\\langle T^* T v, v \\rangle = \\langle 0, v \\rangle = 0 \\implies \\|Tv\\|^2 = 0 \\implies Tv = 0 \\implies v \\in \\operatorname{null}(T)$$
Thus $\\operatorname{null}(T^* T) \\subseteq \\operatorname{null}(T)$.<br>
Combining both directions yields:
<span class=\"ans\">$$\\operatorname{null}(T^* T) = \\operatorname{null}(T)$$</span>
By the Rank-Nullity Theorem:
$$\\operatorname{rank}(T^* T) = \\dim V - \\dim\\operatorname{null}(T^* T) = \\dim V - \\dim\\operatorname{null}(T) = <span class=\"ans\">\\operatorname{rank}(T)</span>$$</p>""",
        "takeaway": "For any linear operator T, the Gram operator T* T is self-adjoint and positive semidefinite. It is strictly positive definite if and only if T is injective, preserving null(T* T) = null(T) and rank(T* T) = rank(T)."
    },
    {
        "id": 21492,
        "subject": "LAA",
        "topicId": "14_Positive_Operators_and_Isometries",
        "topicTitle": "14 · Positive Operators & Isometries",
        "title": "Unique Positive Square Root of Positive Definite Matrix (MIT 18.06 / Strang L26)",
        "kind2": "pyq",
        "source": "MIT 18.06 Linear Algebra / Strang Lecture 26",
        "marks": "[8 Marks]",
        "question": """<p>Consider the matrix $A = \\begin{pmatrix} 5 & 4 \\\\ 4 & 5 \\end{pmatrix} \\in \\mathbb{R}^{2 \\times 2}$.</p>
<p><span class="part">(a)</span> Verify that $A$ is strictly positive definite by computing its eigenvalues and finding an orthonormal eigenbasis.</p>
<p><span class="part">(b)</span> Compute the unique positive definite square root $\\sqrt{A}$ satisfying $(\\sqrt{A})^2 = A$ and $\\sqrt{A} > 0$.</p>
<p><span class="part">(c)</span> Explain why $\\sqrt{A}$ is unique among positive semidefinite matrices, whereas the total number of square roots $X^2 = A$ in $\\mathbb{R}^{2 \\times 2}$ is four.</p>""",
        "solution": """<p><span class="part">Part (a): Eigenvalues and Orthonormal Eigenbasis</span><br>
Characteristic polynomial:
$$\\det(A - \\lambda I) = (5 - \\lambda)^2 - 16 = \\lambda^2 - 10\\lambda + 9 = (\\lambda - 9)(\\lambda - 1) = 0$$
Eigenvalues: $\\lambda_1 = 9 > 0, \\lambda_2 = 1 > 0$. Since all eigenvalues are strictly positive and $A = A^\\top$, $A > 0$.<br>
1. <strong>For $\\lambda_1 = 9$:</strong>
$$(A - 9I)v_1 = \\begin{pmatrix} -4 & 4 \\\\ 4 & -4 \\end{pmatrix} v_1 = 0 \\implies v_1 = \\begin{pmatrix} 1 \\\\ 1 \\end{pmatrix} \\implies q_1 = \\frac{1}{\\sqrt{2}} \\begin{pmatrix} 1 \\\\ 1 \\end{pmatrix}$$
2. <strong>For $\\lambda_2 = 1$:</strong>
$$(A - I)v_2 = \\begin{pmatrix} 4 & 4 \\\\ 4 & 4 \\end{pmatrix} v_2 = 0 \\implies v_2 = \\begin{pmatrix} -1 \\\\ 1 \\end{pmatrix} \\implies q_2 = \\frac{1}{\\sqrt{2}} \\begin{pmatrix} -1 \\\\ 1 \\end{pmatrix}$$
Assemble the orthogonal matrix $Q = \\frac{1}{\\sqrt{2}} \\begin{pmatrix} 1 & -1 \\\\ 1 & 1 \\end{pmatrix}$.</p>

<p><span class="part">Part (b): Computation of Unique Positive Square Root</span><br>
In the eigenbasis of $A$, the square root of the diagonal eigenvalue matrix is:
$$\\sqrt{\\Lambda} = \\begin{pmatrix} \\sqrt{9} & 0 \\\\ 0 & \\sqrt{1} \\end{pmatrix} = \\begin{pmatrix} 3 & 0 \\\\ 0 & 1 \\end{pmatrix}$$
Compute $\\sqrt{A} = Q \\sqrt{\\Lambda} Q^\\top$:
$$\\sqrt{A} = \\frac{1}{2} \\begin{pmatrix} 1 & -1 \\\\ 1 & 1 \\end{pmatrix} \\begin{pmatrix} 3 & 0 \\\\ 0 & 1 \\end{pmatrix} \\begin{pmatrix} 1 & 1 \\\\ -1 & 1 \\end{pmatrix} = \\frac{1}{2} \\begin{pmatrix} 3 & -1 \\\\ 3 & 1 \\end{pmatrix} \\begin{pmatrix} 1 & 1 \\\\ -1 & 1 \\end{pmatrix} = \\frac{1}{2} \\begin{pmatrix} 4 & 2 \\\\ 2 & 4 \\end{pmatrix} = <span class=\"ans\">\\begin{pmatrix} 2 & 1 \\\\ 1 & 2 \\end{pmatrix}</span>$$
<strong>Verification:</strong>
$$\\begin{pmatrix} 2 & 1 \\\\ 1 & 2 \\end{pmatrix} \\begin{pmatrix} 2 & 1 \\\\ 1 & 2 \\end{pmatrix} = \\begin{pmatrix} 4+1 & 2+2 \\\\ 2+2 & 1+4 \\end{pmatrix} = \\begin{pmatrix} 5 & 4 \\\\ 4 & 5 \\end{pmatrix} = A$$</p>

<p><span class="part">Part (c): Uniqueness vs. Total Square Roots</span><br>
Any square root $X$ commuting with $A$ must share its eigenbasis $Q$, so $X = Q \\operatorname{diag}(\\sigma_1, \\sigma_2) Q^\\top$ where:
$$\\sigma_1^2 = 9 \\implies \\sigma_1 = \\pm 3, \\qquad \\sigma_2^2 = 1 \\implies \\sigma_2 = \\pm 1$$
This yields exactly $2 \\times 2 = <span class=\"ans\">4 \\text{ square roots}</span>$:
$$Q \\operatorname{diag}(3, 1) Q^\\top, \\quad Q \\operatorname{diag}(3, -1) Q^\\top, \\quad Q \\operatorname{diag}(-3, 1) Q^\\top, \\quad Q \\operatorname{diag}(-3, -1) Q^\\top$$
However, requiring $X \\ge 0$ (positive semidefinite) forces all eigenvalues to be non-negative real numbers: $\\sigma_1 \\ge 0$ and $\\sigma_2 \\ge 0$.<br>
This uniquely fixes $\\sigma_1 = +3$ and $\\sigma_2 = +1$. Therefore, the <span class=\"ans\">positive square root is strictly unique</span>.</p>""",
        "takeaway": "Every positive semidefinite operator A >= 0 has a unique positive semidefinite square root A^(1/2) >= 0 obtained by taking the non-negative square roots of its eigenvalues. Non-PSD square roots arise from differing sign permutations (+- sqrt(lambda_i))."
    },
    {
        "id": 21493,
        "subject": "LAA",
        "topicId": "14_Positive_Operators_and_Isometries",
        "topicTitle": "14 · Positive Operators & Isometries",
        "title": "Isometries, Trace of PSD Products & Loewner Order (Generated IISc / Stanford EE263 & Berkeley EECS 127)",
        "kind2": "generated",
        "source": "Generated IISc Midterm / Stanford EE263 & Berkeley EECS 127",
        "marks": "[8 Marks]",
        "question": """<p><span class="part">(a)</span> Let $S \\in \\mathcal{L}(V)$ be an isometry on an inner product space ($S^* S = I$). Prove that every eigenvalue $\\lambda \\in \\mathbb{C}$ of $S$ satisfies $|\\lambda| = 1$.</p>
<p><span class="part">(b)</span> Let $A, B \\in \\mathbb{R}^{n \\times n}$ be positive semidefinite matrices ($A \\ge 0, B \\ge 0$). Prove that:
$$\\operatorname{Tr}(AB) \\ge 0$$
and prove that $\\operatorname{Tr}(AB) = 0$ if and only if $AB = 0$.</p>
<p><span class="part">(c)</span> If $A$ and $B$ are symmetric positive definite matrices such that $A > B > 0$ (i.e. $A - B$ is positive definite), prove that $B^{-1} > A^{-1} > 0$ (Loewner order inversion).</p>""",
        "solution": """<p><span class="part">Part (a): Isometry Eigenvalues on Unit Circle</span><br>
Let $v \\ne 0$ be an eigenvector of $S$ with eigenvalue $\\lambda \\in \\mathbb{C}$, so $Sv = \\lambda v$.<br>
Because $S$ is an isometry, it preserves vector norms: $\\|Sv\\| = \\|v\\|$.<br>
Substitute $Sv = \\lambda v$:
$$\\|\\lambda v\\| = \\|v\\| \\implies |\\lambda| \\|v\\| = \\|v\\|$$
Since $v$ is an eigenvector, $v \\ne 0 \\implies \\|v\\| > 0$. Dividing both sides by $\\|v\\|$:
<span class=\"ans\">$$|\\lambda| = 1$$</span>
All eigenvalues of an isometry lie precisely on the complex unit circle.</p>

<p><span class="part">Part (b): PSD Trace Inequality & Equality Condition</span><br>
1. <strong>Inequality:</strong><br>
Since $A \\ge 0$, there exists a unique symmetric positive semidefinite square root $A^{1/2} \\ge 0$ such that $A = A^{1/2} A^{1/2}$.<br>
By the cyclic invariance of the trace:
$$\\operatorname{Tr}(AB) = \\operatorname{Tr}(A^{1/2} A^{1/2} B) = \\operatorname{Tr}(A^{1/2} B A^{1/2})$$
Define the matrix $M = A^{1/2} B A^{1/2}$. For any vector $x \\in \\mathbb{R}^n$:
$$x^\\top M x = x^\\top A^{1/2} B A^{1/2} x = (A^{1/2} x)^\\top B (A^{1/2} x) \\ge 0 \\quad (\\text{since } B \\ge 0)$$
Thus $M$ is symmetric positive semidefinite, so its eigenvalues $\\mu_i(M) \\ge 0$.<br>
$$\\operatorname{Tr}(AB) = \\operatorname{Tr}(M) = \\sum_{i=1}^n \\mu_i(M) \\ge 0$$
2. <strong>Zero Condition:</strong><br>
$\\operatorname{Tr}(M) = 0$ with $\\mu_i(M) \\ge 0$ forces every eigenvalue $\\mu_i(M) = 0 \\implies M = 0 \\implies A^{1/2} B A^{1/2} = 0$.<br>
Since $B \\ge 0$, $B = B^{1/2} B^{1/2}$. Compute the squared Frobenius norm:
$$\\|A^{1/2} B^{1/2}\\|_F^2 = \\operatorname{Tr}\\left( (A^{1/2} B^{1/2})(A^{1/2} B^{1/2})^\\top \\right) = \\operatorname{Tr}(A^{1/2} B A^{1/2}) = \\operatorname{Tr}(M) = 0$$
Since $\\|X\\|_F = 0 \\iff X = 0$, we have $A^{1/2} B^{1/2} = 0$.<br>
Multiplying by $A^{1/2}$ on the left and $B^{1/2}$ on the right:
<span class=\"ans\">$$AB = A^{1/2} (A^{1/2} B^{1/2}) B^{1/2} = 0$$</span></p>

<p><span class="part">Part (c): Loewner Order Inversion Proof</span><br>
Given $A > B > 0$, multiply by $B^{-1/2}$ on both sides (congruence transformation preserves strict positivity):
$$B^{-1/2} (A - B) B^{-1/2} > 0 \\implies B^{-1/2} A B^{-1/2} - I > 0 \\implies B^{-1/2} A B^{-1/2} > I$$
The symmetric matrix $C = B^{-1/2} A B^{-1/2}$ has all eigenvalues $\\lambda_i(C) > 1$.<br>
Taking the matrix inverse:
$$C^{-1} = (B^{-1/2} A B^{-1/2})^{-1} = B^{1/2} A^{-1} B^{1/2}$$
The eigenvalues of $C^{-1}$ are $\\frac{1}{\\lambda_i(C)} < 1$, which means:
$$B^{1/2} A^{-1} B^{1/2} < I$$
Multiply on both sides by $B^{-1/2}$:
$$B^{-1/2} (B^{1/2} A^{-1} B^{1/2}) B^{-1/2} < B^{-1/2} I B^{-1/2} \\implies A^{-1} < B^{-1} \\iff <span class=\"ans\">B^{-1} > A^{-1} > 0</span>$$</p>""",
        "takeaway": "Eigenvalues of isometries have unit magnitude (|lambda| = 1). The trace of the product of two PSD matrices is non-negative and vanishes if and only if AB = 0. Matrix inversion strictly reverses the Loewner partial order: A > B > 0 implies B^(-1) > A^(-1) > 0."
    }
]

def main():
    with open(PRACTICE_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    if "21391" in content:
        print("Batch 13-14 already present in practice_laa.js!")
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
    for card in PRACTICE_LAA_13_14:
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

    print("Successfully added LAA Batch 13-14 (6 cards). Total in file now updated.")

if __name__ == "__main__":
    main()
