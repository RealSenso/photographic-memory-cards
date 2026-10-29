#!/usr/bin/env python3
"""
Builder script for LAA Practice Cards: Batch 08 (Topics 15 & 16)
Topic 15: Polar Decomposition & Singular Value Decomposition (Cards 21591, 21592, 21593)
Topic 16: Moore-Penrose Pseudoinverse & Least Squares (Cards 21691, 21692, 21693)
"""

import json
import os
import re

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRACTICE_FILE = os.path.join(REPO_DIR, "practice_laa.js")

PRACTICE_LAA_15_16 = [
    # =========================================================================
    # TOPIC 15: Polar Decomposition & Singular Value Decomposition
    # =========================================================================
    {
        "id": 21591,
        "subject": "LAA",
        "topicId": "15_Polar_Decomposition_and_Singular_Value_Decomposition",
        "topicTitle": "15 · Polar Decomposition & SVD",
        "title": "SVD Calculation & Non-Negativity of Singular Values (IISc Endsem 2024 / Axler 7.D)",
        "kind2": "pyq",
        "source": "IISc Endsem 2024 / Axler Linear Algebra Done Right 7.D",
        "marks": "[6 Marks]",
        "question": """<p>Consider the diagonal matrix $A = \\begin{pmatrix} 3 & 0 \\\\ 0 & -2 \\end{pmatrix} \\in \\mathbb{R}^{2 \\times 2}$.</p>
<p><span class="part">(a)</span> Compute the eigenvalues of $A^\\top A$ and explain why the second singular value is $\\sigma_2 = +2$ rather than $-2$.</p>
<p><span class="part">(b)</span> Find the orthonormal right singular vectors $V = [v_1, v_2]$ and left singular vectors $U = [u_1, u_2]$, and construct the full SVD $A = U \\Sigma V^\\top$.</p>
<p><span class="part">(c)</span> Construct the <strong>polar decomposition</strong> $A = S P$, where $S$ is an isometry and $P = \\sqrt{A^\\top A}$ is a positive semidefinite operator, verifying $A = SP$.</p>""",
        "solution": """<p><span class="part">Part (a): Gram Matrix & Non-Negativity of Singular Values</span><br>
Compute the symmetric Gram matrix:
$$A^\\top A = \\begin{pmatrix} 3 & 0 \\\\ 0 & -2 \\end{pmatrix} \\begin{pmatrix} 3 & 0 \\\\ 0 & -2 \\end{pmatrix} = \\begin{pmatrix} 9 & 0 \\\\ 0 & 4 \\end{pmatrix}$$
The eigenvalues of $A^\\top A$ are $\\lambda_1 = 9$ and $\\lambda_2 = 4$.<br>
Singular values are defined as the non-negative square roots of the eigenvalues of $A^\\top A$:
$$\\sigma_1 = \\sqrt{9} = 3, \\qquad \\sigma_2 = \\sqrt{4} = <span class=\"ans\">+2</span>$$
By definition, singular values represent geometric stretch lengths and are <span class=\"ans\">strictly non-negative</span> ($\\sigma_i \\ge 0$). Any negative signs in matrix entries are absorbed by the left singular vectors $U$.</p>

<p><span class="part">Part (b): Singular Vectors and SVD Construction</span><br>
1. <strong>Right singular vectors (eigenvectors of $A^\\top A$):</strong>
$$v_1 = \\begin{pmatrix} 1 \\\\ 0 \\end{pmatrix}, \\qquad v_2 = \\begin{pmatrix} 0 \\\\ 1 \\end{pmatrix} \\implies V = \\begin{pmatrix} 1 & 0 \\\\ 0 & 1 \\end{pmatrix}$$
2. <strong>Left singular vectors ($u_j = \\frac{1}{\\sigma_j} A v_j$):</strong>
$$u_1 = \\frac{1}{3} A v_1 = \\frac{1}{3} \\begin{pmatrix} 3 \\\\ 0 \\end{pmatrix} = \\begin{pmatrix} 1 \\\\ 0 \\end{pmatrix}$$
$$u_2 = \\frac{1}{2} A v_2 = \\frac{1}{2} \\begin{pmatrix} 0 \\\\ -2 \\end{pmatrix} = \\begin{pmatrix} 0 \\\\ -1 \\end{pmatrix}$$
Assemble the SVD matrices:
<span class=\"ans\">$$U = \\begin{pmatrix} 1 & 0 \\\\ 0 & -1 \\end{pmatrix}, \\qquad \\Sigma = \\begin{pmatrix} 3 & 0 \\\\ 0 & 2 \\end{pmatrix}, \\qquad V^\\top = \\begin{pmatrix} 1 & 0 \\\\ 0 & 1 \\end{pmatrix}$$</span>
<strong>Verification:</strong>
$$U \\Sigma V^\\top = \\begin{pmatrix} 1 & 0 \\\\ 0 & -1 \\end{pmatrix} \\begin{pmatrix} 3 & 0 \\\\ 0 & 2 \\end{pmatrix} \\begin{pmatrix} 1 & 0 \\\\ 0 & 1 \\end{pmatrix} = \\begin{pmatrix} 3 & 0 \\\\ 0 & -2 \\end{pmatrix} = A$$</p>

<p><span class="part">Part (c): Polar Decomposition $A = S P$</span><br>
1. <strong>Positive operator $P = \\sqrt{A^\\top A}$:</strong>
$$P = V \\Sigma V^\\top = \\begin{pmatrix} 1 & 0 \\\\ 0 & 1 \\end{pmatrix} \\begin{pmatrix} 3 & 0 \\\\ 0 & 2 \\end{pmatrix} \\begin{pmatrix} 1 & 0 \\\\ 0 & 1 \\end{pmatrix} = <span class=\"ans\">\\begin{pmatrix} 3 & 0 \\\\ 0 & 2 \\end{pmatrix}</span> > 0$$
2. <strong>Isometry $S = U V^\\top$:</strong>
$$S = \\begin{pmatrix} 1 & 0 \\\\ 0 & -1 \\end{pmatrix} \\begin{pmatrix} 1 & 0 \\\\ 0 & 1 \\end{pmatrix} = <span class=\"ans\">\\begin{pmatrix} 1 & 0 \\\\ 0 & -1 \\end{pmatrix}</span>$$
Notice that $S^\\top S = I$ (reflection across the x-axis).<br>
<strong>Verification:</strong>
$$S P = \\begin{pmatrix} 1 & 0 \\\\ 0 & -1 \\end{pmatrix} \\begin{pmatrix} 3 & 0 \\\\ 0 & 2 \\end{pmatrix} = \\begin{pmatrix} 3 & 0 \\\\ 0 & -2 \\end{pmatrix} = A$$</p>""",
        "takeaway": "Singular values are strictly non-negative (sigma_i = sqrt(lambda_i(A^T A)) >= 0). The polar decomposition A = S P factors any linear operator into an isometry S = U V^T and a unique positive semidefinite operator P = V Sigma V^T = sqrt(A^T A)."
    },
    {
        "id": 21592,
        "subject": "LAA",
        "topicId": "15_Polar_Decomposition_and_Singular_Value_Decomposition",
        "topicTitle": "15 · Polar Decomposition & SVD",
        "title": "SVD of Rank-1 Matrix & Dyadic Outer Product Expansion (MIT 18.06 / Strang L29)",
        "kind2": "pyq",
        "source": "MIT 18.06 Linear Algebra / Strang Lecture 29",
        "marks": "[8 Marks]",
        "question": """<p>Consider the rank-1 matrix $A = \\begin{pmatrix} 1 & 1 \\\\ 2 & 2 \\end{pmatrix} \\in \\mathbb{R}^{2 \\times 2}$.</p>
<p><span class="part">(a)</span> Compute the singular values $\\sigma_1, \\sigma_2$ and the orthonormal right singular vectors $v_1, v_2$.</p>
<p><span class="part">(b)</span> Determine the left singular vectors $u_1, u_2$ and express the full SVD $A = U \\Sigma V^\\top$.</p>
<p><span class="part">(c)</span> Express $A$ as the rank-1 dyadic outer product $\\sigma_1 u_1 v_1^\\top$, and identify the four fundamental subspaces of $A$ from the columns of $U$ and $V$.</p>""",
        "solution": """<p><span class="part">Part (a): Gram Matrix & Right Singular Vectors</span><br>
Compute $A^\\top A$:
$$A^\\top A = \\begin{pmatrix} 1 & 2 \\\\ 1 & 2 \\end{pmatrix} \\begin{pmatrix} 1 & 1 \\\\ 2 & 2 \\end{pmatrix} = \\begin{pmatrix} 5 & 5 \\\\ 5 & 5 \\end{pmatrix}$$
Characteristic polynomial:
$$\\det(A^\\top A - \\lambda I) = (5 - \\lambda)^2 - 25 = \\lambda^2 - 10\\lambda = \\lambda(\\lambda - 10) = 0$$
Eigenvalues: $\\lambda_1 = 10, \\lambda_2 = 0$.<br>
Singular values: <span class=\"ans\">$\\sigma_1 = \\sqrt{10}, \\sigma_2 = 0$</span>.<br>
1. <strong>For $\\lambda_1 = 10$:</strong>
$$(A^\\top A - 10I)v_1 = \\begin{pmatrix} -5 & 5 \\\\ 5 & -5 \\end{pmatrix} v_1 = 0 \\implies v_1 = <span class=\"ans\">\\frac{1}{\\sqrt{2}} \\begin{pmatrix} 1 \\\\ 1 \\end{pmatrix}</span>$$
2. <strong>For $\\lambda_2 = 0$:</strong>
$$(A^\\top A)v_2 = \\begin{pmatrix} 5 & 5 \\\\ 5 & 5 \\end{pmatrix} v_2 = 0 \\implies v_2 = <span class=\"ans\">\\frac{1}{\\sqrt{2}} \\begin{pmatrix} 1 \\\\ -1 \\end{pmatrix}</span>$$</p>

<p><span class="part">Part (b): Left Singular Vectors & Full SVD</span><br>
1. Compute active left singular vector $u_1$:
$$u_1 = \\frac{1}{\\sigma_1} A v_1 = \\frac{1}{\\sqrt{10}} \\begin{pmatrix} 1 & 1 \\\\ 2 & 2 \\end{pmatrix} \\frac{1}{\\sqrt{2}} \\begin{pmatrix} 1 \\\\ 1 \\end{pmatrix} = \\frac{1}{\\sqrt{20}} \\begin{pmatrix} 2 \\\\ 4 \\end{pmatrix} = \\frac{1}{2\\sqrt{5}} \\begin{pmatrix} 2 \\\\ 4 \\end{pmatrix} = <span class=\"ans\">\\frac{1}{\\sqrt{5}} \\begin{pmatrix} 1 \\\\ 2 \\end{pmatrix}</span>$$
2. Complete to an orthonormal basis of $\\mathbb{R}^2$ ($u_2 \\perp u_1$):
$$u_2 = <span class=\"ans\">\\frac{1}{\\sqrt{5}} \\begin{pmatrix} -2 \\\\ 1 \\end{pmatrix}</span>$$
Full SVD:
<span class=\"ans\">$$A = \\begin{pmatrix} 1/\\sqrt{5} & -2/\\sqrt{5} \\\\ 2/\\sqrt{5} & 1/\\sqrt{5} \\end{pmatrix} \\begin{pmatrix} \\sqrt{10} & 0 \\\\ 0 & 0 \\end{pmatrix} \\begin{pmatrix} 1/\\sqrt{2} & 1/\\sqrt{2} \\\\ 1/\\sqrt{2} & -1/\\sqrt{2} \\end{pmatrix}$$</span></p>

<p><span class="part">Part (c): Dyadic Form & Four Fundamental Subspaces</span><br>
1. <strong>Dyadic outer product expansion:</strong>
$$A = \\sigma_1 u_1 v_1^\\top = \\sqrt{10} \\left( \\frac{1}{\\sqrt{5}} \\begin{pmatrix} 1 \\\\ 2 \\end{pmatrix} \\right) \\left( \\frac{1}{\\sqrt{2}} \\begin{pmatrix} 1 & 1 \\end{pmatrix} \\right) = \\frac{\\sqrt{10}}{\\sqrt{10}} \\begin{pmatrix} 1 \\\\ 2 \\end{pmatrix} \\begin{pmatrix} 1 & 1 \\end{pmatrix} = <span class=\"ans\">\\begin{pmatrix} 1 & 1 \\\\ 2 & 2 \\end{pmatrix}</span>$$
2. <strong>Four Fundamental Subspaces:</strong>
- $\\operatorname{range}(A) = \\operatorname{span}(u_1) = \\operatorname{span}\\left( \\begin{pmatrix} 1 \\\\ 2 \\end{pmatrix} \\right)$
- $\\operatorname{null}(A^\\top) = \\operatorname{span}(u_2) = \\operatorname{span}\\left( \\begin{pmatrix} -2 \\\\ 1 \\end{pmatrix} \\right)$
- $\\operatorname{range}(A^\\top) = \\operatorname{span}(v_1) = \\operatorname{span}\\left( \\begin{pmatrix} 1 \\\\ 1 \\end{pmatrix} \\right)$
- $\\operatorname{null}(A) = \\operatorname{span}(v_2) = \\operatorname{span}\\left( \\begin{pmatrix} 1 \\\\ -1 \\end{pmatrix} \\right)$</p>""",
        "takeaway": "The SVD decomposes any matrix into a sum of r rank-1 dyadic outer products: A = sum sigma_i u_i v_i^T. The left and right singular vectors provide mutually orthonormal bases for all four fundamental subspaces."
    },
    {
        "id": 21593,
        "subject": "LAA",
        "topicId": "15_Polar_Decomposition_and_Singular_Value_Decomposition",
        "topicTitle": "15 · Polar Decomposition & SVD",
        "title": "Eckart-Young-Mirsky Low-Rank Approximation & Matrix Norms (Generated IISc / Stanford EE263 & Berkeley EECS 127)",
        "kind2": "generated",
        "source": "Generated IISc Midterm / Stanford EE263 & Berkeley EECS 127",
        "marks": "[8 Marks]",
        "question": """<p><span class="part">(a)</span> State the <strong>Eckart-Young-Mirsky Theorem</strong> for optimal low-rank matrix approximation under both the spectral norm $\\|\\cdot\\|_2$ and the Frobenius norm $\\|\\cdot\\|_F$.</p>
<p><span class="part">(b)</span> For the rectangular matrix $A = \\begin{pmatrix} 3 & 2 & 2 \\\\ 2 & 3 & -2 \\end{pmatrix} \\in \\mathbb{R}^{2 \\times 3}$, compute its singular values $\\sigma_1, \\sigma_2$ and find the best rank-1 approximation $A_1 = \\sigma_1 u_1 v_1^\\top$.</p>
<p><span class="part">(c)</span> Calculate the exact approximation errors $\\|A - A_1\\|_2$ and $\\|A - A_1\\|_F$, and prove rigorously that $\\|A\\|_2 = \\sigma_{\\max}(A)$ and $\\|A\\|_F = \\sqrt{\\sum_{i=1}^r \\sigma_i^2}$.</p>""",
        "solution": """<p><span class="part">Part (a): Eckart-Young-Mirsky Theorem</span><br>
<strong>Theorem:</strong> Let $A \\in \\mathbb{R}^{m \\times n}$ have SVD $A = \\sum_{i=1}^r \\sigma_i u_i v_i^\\top$ with $\\sigma_1 \\ge \\dots \\ge \\sigma_r > 0$. For any $k < r$, the truncated SVD sum $A_k = \\sum_{i=1}^k \\sigma_i u_i v_i^\\top$ is the optimal rank-$k$ approximation in both spectral and Frobenius norms:
<span class=\"ans\">$$\\min_{\\operatorname{rank}(B) \\le k} \\|A - B\\|_2 = \\|A - A_k\\|_2 = \\sigma_{k+1}$$</span>
<span class=\"ans\">$$\\min_{\\operatorname{rank}(B) \\le k} \\|A - B\\|_F = \\|A - A_k\\|_F = \\sqrt{\\sum_{i=k+1}^r \\sigma_i^2}$$</span></p>

<p><span class="part">Part (b): Singular Values & Best Rank-1 Approximation</span><br>
Compute $A A^\\top$:
$$A A^\\top = \\begin{pmatrix} 3 & 2 & 2 \\\\ 2 & 3 & -2 \\end{pmatrix} \\begin{pmatrix} 3 & 2 \\\\ 2 & 3 \\\\ 2 & -2 \\end{pmatrix} = \\begin{pmatrix} 9 + 4 + 4 & 6 + 6 - 4 \\\\ 6 + 6 - 4 & 4 + 9 + 4 \\end{pmatrix} = \\begin{pmatrix} 17 & 8 \\\\ 8 & 17 \\end{pmatrix}$$
Eigenvalues:
$$\\det(A A^\\top - \\lambda I) = (17 - \\lambda)^2 - 64 = (\\lambda - 25)(\\lambda - 9) = 0 \\implies \\lambda_1 = 25, \\lambda_2 = 9$$
Singular values: <span class=\"ans\">$\\sigma_1 = 5, \\sigma_2 = 3$</span>.<br>
1. <strong>Left singular vector $u_1$:</strong>
$$(A A^\\top - 25I)u_1 = \\begin{pmatrix} -8 & 8 \\\\ 8 & -8 \\end{pmatrix} u_1 = 0 \\implies u_1 = \\frac{1}{\\sqrt{2}} \\begin{pmatrix} 1 \\\\ 1 \\end{pmatrix}$$
2. <strong>Right singular vector $v_1$:</strong>
$$v_1 = \\frac{1}{\\sigma_1} A^\\top u_1 = \\frac{1}{5} \\begin{pmatrix} 3 & 2 \\\\ 2 & 3 \\\\ 2 & -2 \\end{pmatrix} \\frac{1}{\\sqrt{2}} \\begin{pmatrix} 1 \\\\ 1 \\end{pmatrix} = \\frac{1}{5\\sqrt{2}} \\begin{pmatrix} 5 \\\\ 5 \\\\ 0 \\end{pmatrix} = \\frac{1}{\\sqrt{2}} \\begin{pmatrix} 1 \\\\ 1 \\\\ 0 \\end{pmatrix}$$
3. <strong>Best Rank-1 Approximation $A_1$:</strong>
$$A_1 = 5 \\left( \\frac{1}{\\sqrt{2}} \\begin{pmatrix} 1 \\\\ 1 \\end{pmatrix} \\right) \\left( \\frac{1}{\\sqrt{2}} \\begin{pmatrix} 1 & 1 & 0 \\end{pmatrix} \\right) = \\frac{5}{2} \\begin{pmatrix} 1 & 1 & 0 \\\\ 1 & 1 & 0 \\end{pmatrix} = <span class=\"ans\">\\begin{pmatrix} 2.5 & 2.5 & 0 \\\\ 2.5 & 2.5 & 0 \\end{pmatrix}</span>$$</p>

<p><span class="part">Part (c): Approximation Errors & Norm Proofs</span><br>
1. <strong>Errors:</strong>
$$\\|A - A_1\\|_2 = \\sigma_2 = <span class=\"ans\">3</span>$$
$$\\|A - A_1\\|_F = \\sqrt{\\sigma_2^2} = \\sigma_2 = <span class=\"ans\">3</span>$$
2. <strong>Spectral Norm Proof:</strong>
$$\\|A\\|_2 = \\max_{\\|x\\|=1} \\|U \\Sigma V^\\top x\\|_2 = \\max_{\\|y\\|=1} \\|\\Sigma y\\|_2 = \\max_{\\sum y_i^2 = 1} \\sqrt{\\sum_{i=1}^r \\sigma_i^2 y_i^2} \\le \\sigma_1 \\sqrt{\\sum y_i^2} = \\sigma_1 = <span class=\"ans\">\\sigma_{\\max}</span>$$
Achieved at $y = e_1 \\implies x = v_1$.<br>
3. <strong>Frobenius Norm Proof:</strong>
Using cyclic trace invariance:
$$\\|A\\|_F^2 = \\operatorname{Tr}(A^\\top A) = \\operatorname{Tr}(V \\Sigma^\\top U^\\top U \\Sigma V^\\top) = \\operatorname{Tr}(V \\Sigma^\\top \\Sigma V^\\top) = \\operatorname{Tr}(\\Sigma^\\top \\Sigma V^\\top V) = \\operatorname{Tr}(\\Sigma^\\top \\Sigma) = <span class=\"ans\">\\sum_{i=1}^r \\sigma_i^2</span>$$
Taking square roots yields $\\|A\\|_F = \\sqrt{\\sum_{i=1}^r \\sigma_i^2}$.</p>""",
        "takeaway": "The Eckart-Young-Mirsky Theorem guarantees that truncating the SVD at k terms produces the provably optimal rank-k approximation. The 2-norm error is the first dropped singular value sigma_{k+1}, and the Frobenius error is sqrt(sum_{i=k+1}^r sigma_i^2)."
    },

    # =========================================================================
    # TOPIC 16: Moore-Penrose Pseudoinverse & Least Squares
    # =========================================================================
    {
        "id": 21691,
        "subject": "LAA",
        "topicId": "16_Pseudoinverse_and_Least_Squares",
        "topicTitle": "16 · Pseudoinverse & Least Squares",
        "title": "Moore-Penrose Pseudoinverse & 4 Penrose Conditions (IISc Endsem 2023 / Meyer 5.12)",
        "kind2": "pyq",
        "source": "IISc Endsem 2023 / Meyer Matrix Analysis 5.12",
        "marks": "[6 Marks]",
        "question": """<p>Consider the column vector matrix $A = \\begin{pmatrix} 1 \\\\ 1 \\end{pmatrix} \\in \\mathbb{R}^{2 \\times 1}$.</p>
<p><span class="part">(a)</span> Compute the pseudoinverse $A^+$ using the full column rank left-inverse formula $A^+ = (A^\\top A)^{-1} A^\\top$.</p>
<p><span class="part">(b)</span> Rigorously verify all four Moore-Penrose conditions for $A^+$:
$$\\text{(1) } A A^+ A = A, \\quad \\text{(2) } A^+ A A^+ = A^+, \\quad \\text{(3) } (A A^+)^\\top = A A^+, \\quad \\text{(4) } (A^+ A)^\\top = A^+ A$$</p>
<p><span class="part">(c)</span> Compute $A^+$ using the compact SVD $A = \\sigma_1 u_1 v_1^\\top$ and verify that it matches the result from Part (a).</p>""",
        "solution": """<p><span class="part">Part (a): Pseudoinverse via Full Column Rank Formula</span><br>
Since $A$ has linearly independent columns (rank $r = 1 = n$):
$$A^\\top A = \\begin{pmatrix} 1 & 1 \\end{pmatrix} \\begin{pmatrix} 1 \\\\ 1 \\end{pmatrix} = [2] \\implies (A^\\top A)^{-1} = [1/2]$$
$$A^+ = (A^\\top A)^{-1} A^\\top = \\frac{1}{2} \\begin{pmatrix} 1 & 1 \\end{pmatrix} = <span class=\"ans\">\\begin{pmatrix} 1/2 & 1/2 \\end{pmatrix}</span>$$</p>

<p><span class="part">Part (b): Verification of the Four Moore-Penrose Conditions</span><br>
Compute the outer and inner products:
$$A A^+ = \\begin{pmatrix} 1 \\\\ 1 \\end{pmatrix} \\begin{pmatrix} 1/2 & 1/2 \\end{pmatrix} = \\begin{pmatrix} 1/2 & 1/2 \\\\ 1/2 & 1/2 \\end{pmatrix}$$
$$A^+ A = \\begin{pmatrix} 1/2 & 1/2 \\end{pmatrix} \\begin{pmatrix} 1 \\\\ 1 \\end{pmatrix} = [1/2 + 1/2] = [1]$$
1. <strong>Condition 1 ($A A^+ A = A$):</strong>
$$(A A^+) A = \\begin{pmatrix} 1/2 & 1/2 \\\\ 1/2 & 1/2 \\end{pmatrix} \\begin{pmatrix} 1 \\\\ 1 \\end{pmatrix} = \\begin{pmatrix} 1 \\\\ 1 \\end{pmatrix} = A \\quad \\checkmark$$
2. <strong>Condition 2 ($A^+ A A^+ = A^+$):</strong>
$$(A^+ A) A^+ = 1 \\cdot \\begin{pmatrix} 1/2 & 1/2 \\end{pmatrix} = A^+ \\quad \\checkmark$$
3. <strong>Condition 3 ($(A A^+)^\\top = A A^+$):</strong>
$$(A A^+)^\\top = \\begin{pmatrix} 1/2 & 1/2 \\\\ 1/2 & 1/2 \\end{pmatrix}^\\top = \\begin{pmatrix} 1/2 & 1/2 \\\\ 1/2 & 1/2 \\end{pmatrix} = A A^+ \\quad \\checkmark$$
4. <strong>Condition 4 ($(A^+ A)^\\top = A^+ A$):</strong>
$$(A^+ A)^\\top = [1]^\\top = [1] = A^+ A \\quad \\checkmark$$
All four conditions are strictly satisfied.</p>

<p><span class="part">Part (c): SVD Derivation of $A^+$</span><br>
Singular value: $\\sigma_1 = \\|A\\|_2 = \\sqrt{1^2 + 1^2} = \\sqrt{2}$.<br>
Left singular vector: $u_1 = \\frac{1}{\\sqrt{2}} \\begin{pmatrix} 1 \\\\ 1 \\end{pmatrix}$.<br>
Right singular vector: $v_1 = [1]$.<br>
The compact SVD is $A = \\sqrt{2} u_1 v_1^\\top$.<br>
The pseudoinverse via SVD is:
$$A^+ = \\frac{1}{\\sigma_1} v_1 u_1^\\top = \\frac{1}{\\sqrt{2}} [1] \\left( \\frac{1}{\\sqrt{2}} \\begin{pmatrix} 1 & 1 \\end{pmatrix} \\right) = \\frac{1}{2} \\begin{pmatrix} 1 & 1 \\end{pmatrix} = <span class=\"ans\">\\begin{pmatrix} 1/2 & 1/2 \\end{pmatrix}</span>$$
This identically matches Part (a).</p>""",
        "takeaway": "The Moore-Penrose pseudoinverse A^+ is the unique matrix satisfying all four Penrose conditions. When A has full column rank, A^+ = (A^T A)^(-1) A^T acts as an exact left inverse (A^+ A = I)."
    },
    {
        "id": 21692,
        "subject": "LAA",
        "topicId": "16_Pseudoinverse_and_Least_Squares",
        "topicTitle": "16 · Pseudoinverse & Least Squares",
        "title": "Overdetermined Least-Squares Regression & Normal Equations (MIT 18.06 / Strang L15)",
        "kind2": "pyq",
        "source": "MIT 18.06 Linear Algebra / Strang Lecture 15",
        "marks": "[8 Marks]",
        "question": """<p>Find the best-fit line $y = C + D t$ in the least-squares sense for the three data points $(t_1, y_1) = (0, 1)$, $(t_2, y_2) = (1, 2)$, and $(t_3, y_3) = (2, 4)$.</p>
<p><span class="part">(a)</span> Set up the overdetermined linear system $A x = b$ for the parameter vector $x = \\begin{pmatrix} C \\\\ D \\end{pmatrix}$.</p>
<p><span class="part">(b)</span> Formulate and solve the <strong>normal equations</strong> $A^\\top A x = A^\\top b$ to determine the optimal coefficients $C^*, D^*$.</p>
<p><span class="part">(c)</span> Compute the orthogonal projection vector $p = A x^*$ and the residual error vector $e = b - p$, and verify that $e \\perp \\operatorname{range}(A)$ ($A^\\top e = 0$).</p>""",
        "solution": """<p><span class="part">Part (a): Overdetermined System Formulation</span><br>
Evaluating the model equation $C + D t_i = y_i$ at each point:
$$C + D(0) = 1, \\qquad C + D(1) = 2, \\qquad C + D(2) = 4$$
In matrix form $A x = b$:
<span class=\"ans\">$$A = \\begin{pmatrix} 1 & 0 \\\\ 1 & 1 \\\\ 1 & 2 \\end{pmatrix}, \\qquad x = \\begin{pmatrix} C \\\\ D \\end{pmatrix}, \\qquad b = \\begin{pmatrix} 1 \\\\ 2 \\\\ 4 \\end{pmatrix}$$</span></p>

<p><span class="part">Part (b): Normal Equations Solution</span><br>
Compute the Gram matrix $A^\\top A$:
$$A^\\top A = \\begin{pmatrix} 1 & 1 & 1 \\\\ 0 & 1 & 2 \\end{pmatrix} \\begin{pmatrix} 1 & 0 \\\\ 1 & 1 \\\\ 1 & 2 \\end{pmatrix} = \\begin{pmatrix} 3 & 3 \\\\ 3 & 5 \\end{pmatrix}$$
Compute $A^\\top b$:
$$A^\\top b = \\begin{pmatrix} 1 & 1 & 1 \\\\ 0 & 1 & 2 \\end{pmatrix} \\begin{pmatrix} 1 \\\\ 2 \\\\ 4 \\end{pmatrix} = \\begin{pmatrix} 1 + 2 + 4 \\\\ 0 + 2 + 8 \\end{pmatrix} = \\begin{pmatrix} 7 \\\\ 10 \\end{pmatrix}$$
Invert $A^\\top A$: $\\det(A^\\top A) = 3(5) - 3(3) = 6$.
$$(A^\\top A)^{-1} = \\frac{1}{6} \\begin{pmatrix} 5 & -3 \\\\ -3 & 3 \\end{pmatrix}$$
Solve for $x^*$:
$$x^* = \\frac{1}{6} \\begin{pmatrix} 5 & -3 \\\\ -3 & 3 \\end{pmatrix} \\begin{pmatrix} 7 \\\\ 10 \\end{pmatrix} = \\frac{1}{6} \\begin{pmatrix} 35 - 30 \\\\ -21 + 30 \\end{pmatrix} = \\frac{1}{6} \\begin{pmatrix} 5 \\\\ 9 \\end{pmatrix} = <span class=\"ans\">\\begin{pmatrix} 5/6 \\\\ 3/2 \\end{pmatrix}</span>$$
The optimal least-squares line is:
<span class=\"ans\">$$y = \\frac{5}{6} + \\frac{3}{2} t$$</span></p>

<p><span class="part">Part (c): Projection, Error & Orthogonality Verification</span><br>
1. <strong>Projection vector $p = A x^*$:</strong>
$$p = \\begin{pmatrix} 1 & 0 \\\\ 1 & 1 \\\\ 1 & 2 \\end{pmatrix} \\begin{pmatrix} 5/6 \\\\ 3/2 \\end{pmatrix} = \\begin{pmatrix} 5/6 \\\\ 5/6 + 9/6 \\\\ 5/6 + 18/6 \\end{pmatrix} = <span class=\"ans\">\\begin{pmatrix} 5/6 \\\\ 14/6 \\\\ 23/6 \\end{pmatrix}</span>$$
2. <strong>Residual error vector $e = b - p$:</strong>
$$e = \\begin{pmatrix} 1 \\\\ 2 \\\\ 4 \\end{pmatrix} - \\begin{pmatrix} 5/6 \\\\ 14/6 \\\\ 23/6 \\end{pmatrix} = \\begin{pmatrix} 6/6 - 5/6 \\\\ 12/6 - 14/6 \\\\ 24/6 - 23/6 \\end{pmatrix} = <span class=\"ans\">\\frac{1}{6} \\begin{pmatrix} 1 \\\\ -2 \\\\ 1 \\end{pmatrix}</span>$$
3. <strong>Orthogonality Verification ($A^\\top e = 0$):</strong>
$$A^\\top e = \\begin{pmatrix} 1 & 1 & 1 \\\\ 0 & 1 & 2 \\end{pmatrix} \\frac{1}{6} \\begin{pmatrix} 1 \\\\ -2 \\\\ 1 \\end{pmatrix} = \\frac{1}{6} \\begin{pmatrix} 1 - 2 + 1 \\\\ 0 - 2 + 2 \\end{pmatrix} = <span class=\"ans\">\\begin{pmatrix} 0 \\\\ 0 \\end{pmatrix}</span>$$
The error vector is strictly orthogonal to the column space of $A$.</p>""",
        "takeaway": "The least-squares solution x* = (A^T A)^(-1) A^T b orthogonally projects b onto the column space range(A). The residual error e = b - A x* is strictly orthogonal to range(A), satisfying the normal equations A^T e = 0."
    },
    {
        "id": 21693,
        "subject": "LAA",
        "topicId": "16_Pseudoinverse_and_Least_Squares",
        "topicTitle": "16 · Pseudoinverse & Least Squares",
        "title": "Underdetermined Minimum-Norm Solution & Fundamental Projectors (Generated IISc / Stanford EE263 & Berkeley EECS 127)",
        "kind2": "generated",
        "source": "Generated IISc Midterm / Stanford EE263 & Berkeley EECS 127",
        "marks": "[8 Marks]",
        "question": """<p><span class="part">(a)</span> For an underdetermined linear system $A x = b$ where $A \\in \\mathbb{R}^{m \\times n}$ has full row rank ($m < n$), prove that the right pseudoinverse solution $x_{\\text{LN}} = A^\\top (A A^\\top)^{-1} b$ is the unique solution of <strong>minimal Euclidean norm</strong>.</p>
<p><span class="part">(b)</span> Find the unique minimum-norm solution to the single linear equation:
$$x_1 + 2x_2 + 2x_3 = 9$$
and compute its Euclidean norm $\\|x^*\\|$.</p>
<p><span class="part">(c)</span> Using the Moore-Penrose conditions, prove that $P = A A^+$ is the orthogonal projector onto $\\operatorname{range}(A)$, and that $Q = I - A^+ A$ is the orthogonal projector onto $\\operatorname{null}(A)$.</p>""",
        "solution": """<p><span class="part">Part (a): Proof of Minimum-Norm Optimality</span><br>
By the Fundamental Subspaces Theorem, $\\mathbb{R}^n = \\operatorname{range}(A^\\top) \\oplus \\operatorname{null}(A)$ is an orthogonal direct sum.<br>
Any solution $x$ satisfying $Ax = b$ can be uniquely written as $x = x_r + x_n$ where $x_r \\in \\operatorname{range}(A^\\top)$ and $x_n \\in \\operatorname{null}(A)$.<br>
Since $x_r \\in \\operatorname{range}(A^\\top)$, $x_r = A^\\top z$ for some $z \\in \\mathbb{R}^m$. Substituting into $Ax = b$:
$$b = A(x_r + x_n) = A(A^\\top z) + A x_n = (A A^\\top) z + 0 = (A A^\\top) z$$
Because $A$ has full row rank, $A A^\\top$ is invertible: $z = (A A^\\top)^{-1} b$. Thus:
$$x_r = A^\\top (A A^\\top)^{-1} b = x_{\\text{LN}}$$
By the Pythagorean theorem ($x_r \\perp x_n$):
$$\\|x\\|^2 = \\|x_r + x_n\\|^2 = \\|x_r\\|^2 + \\|x_n\\|^2 = \\|x_{\\text{LN}}\\|^2 + \\|x_n\\|^2 \\ge \\|x_{\\text{LN}}\\|^2$$
Equality holds if and only if $x_n = 0 \\implies x = x_{\\text{LN}}$.<br>
Thus <span class=\"ans\">$x_{\\text{LN}} = A^\\top (A A^\\top)^{-1} b$</span> is the unique solution of strictly minimal Euclidean norm.</p>

<p><span class="part">Part (b): Minimum-Norm Solution Computation</span><br>
The equation is $A x = b$ with $A = \\begin{pmatrix} 1 & 2 & 2 \\end{pmatrix} \\in \\mathbb{R}^{1 \\times 3}$ and $b = [9]$.<br>
Compute $A A^\\top$:
$$A A^\\top = 1^2 + 2^2 + 2^2 = 1 + 4 + 4 = [9] \\implies (A A^\\top)^{-1} = [1/9]$$
Compute $x^* = A^\\top (A A^\\top)^{-1} b$:
$$x^* = \\begin{pmatrix} 1 \\\\ 2 \\\\ 2 \\end{pmatrix} \\left( \\frac{1}{9} \\right) (9) = <span class=\"ans\">\\begin{pmatrix} 1 \\\\ 2 \\\\ 2 \\end{pmatrix}</span>$$
Check: $1(1) + 2(2) + 2(2) = 1 + 4 + 4 = 9$.<br>
Norm:
$$\\|x^*\\| = \\sqrt{1^2 + 2^2 + 2^2} = \\sqrt{1 + 4 + 4} = \\sqrt{9} = <span class=\"ans\">3</span>$$</p>

<p><span class="part">Part (c): Fundamental Orthogonal Projector Proofs</span><br>
1. <strong>Projector $P = A A^+$ onto $\\operatorname{range}(A)$:</strong>
- Idempotence: $P^2 = (A A^+)(A A^+) = (A A^+ A) A^+ = A A^+ = P$ (Penrose condition 1).
- Symmetry: $P^\\top = (A A^+)^\\top = A A^+ = P$ (Penrose condition 3).
- Range: For any $y = Ax \\in \\operatorname{range}(A)$, $P y = A A^+ A x = A x = y$. Thus $\\operatorname{range}(P) = \\operatorname{range}(A)$.<br>
2. <strong>Projector $Q = I - A^+ A$ onto $\\operatorname{null}(A)$:</strong>
- Idempotence: $Q^2 = (I - A^+ A)^2 = I - 2A^+ A + (A^+ A)^2 = I - 2A^+ A + A^+ A = I - A^+ A = Q$ (Penrose condition 2).
- Symmetry: $Q^\\top = (I - A^+ A)^\\top = I - (A^+ A)^\\top = I - A^+ A = Q$ (Penrose condition 4).
- Range: $A Q = A(I - A^+ A) = A - A A^+ A = A - A = 0 \\implies \\operatorname{range}(Q) \\subseteq \\operatorname{null}(A)$. Conversely, if $v \\in \\operatorname{null}(A)$, $Q v = v - A^+ (Av) = v - 0 = v \\implies \\operatorname{null}(A) \\subseteq \\operatorname{range}(Q)$.<br>
Thus <span class=\"ans\">$Q = I - A^+ A$</span> is the orthogonal projector onto $\\operatorname{null}(A)$.</p>""",
        "takeaway": "For underdetermined systems, x_LN = A^T (A A^T)^(-1) b provides the unique solution with minimal Euclidean norm. The pseudoinverse constructs the orthogonal projectors P = A A^+ onto range(A) and Q = I - A^+ A onto null(A)."
    }
]

def main():
    with open(PRACTICE_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    if "21591" in content:
        print("Batch 15-16 already present in practice_laa.js!")
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
    for card in PRACTICE_LAA_15_16:
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

    print("Successfully added LAA Batch 15-16 (6 cards). Total in file now updated.")

if __name__ == "__main__":
    main()
