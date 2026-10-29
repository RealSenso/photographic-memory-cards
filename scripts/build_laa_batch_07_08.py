#!/usr/bin/env python3
"""
Builder script for LAA Practice Cards: Batch 04 (Topics 07 & 08)
Topic 07: Commuting Operators & Simultaneous Diagonalization (Cards 20791, 20792, 20793)
Topic 08: Generalized Eigenspaces & Nilpotent Operators (Cards 20891, 20892, 20893)
"""

import json
import os
import re

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRACTICE_FILE = os.path.join(REPO_DIR, "practice_laa.js")

PRACTICE_LAA_07_08 = [
    # =========================================================================
    # TOPIC 07: Commuting Operators & Simultaneous Diagonalization
    # =========================================================================
    {
        "id": 20791,
        "subject": "LAA",
        "topicId": "07_Commuting_Operators_and_Simultaneous_Diagonalization",
        "topicTitle": "07 · Commuting & Simultaneous Diag",
        "title": "Existence of Common Eigenvector for Commuting Operators on Complex Spaces (IISc Endsem 2023 / Axler 5.E)",
        "kind2": "pyq",
        "source": "IISc Endsem 2023 / Axler Linear Algebra Done Right 5.E",
        "marks": "[8 Marks]",
        "question": """<p>Let $A, B \\in \\mathbb{C}^{n \\times n}$ be linear operators on a finite-dimensional complex vector space such that they commute:
$$AB = BA$$</p>
<p><span class="part">(a)</span> Let $\\lambda \\in \\mathbb{C}$ be an eigenvalue of $A$ with eigenspace $E(\\lambda, A) = \\operatorname{null}(A - \\lambda I)$. Prove that $E(\\lambda, A)$ is invariant under $B$.</p>
<p><span class="part">(b)</span> Apply the Fundamental Theorem of Algebra to the restricted operator $B|_{E(\\lambda, A)}$ to prove that $A$ and $B$ share at least one common eigenvector $u \\in \\mathbb{C}^n$.</p>
<p><span class="part">(c)</span> Does this guarantee that $A$ and $B$ share a common basis of eigenvectors (i.e., are simultaneously diagonalizable)? Explain the condition required.</p>""",
        "solution": """<p><span class="part">Part (a): Invariance of Eigenspace $E(\\lambda, A)$ under $B$</span><br>
Let $v \\in E(\\lambda, A)$, which means $Av = \\lambda v$.<br>
Apply $A$ to the vector $Bv$:
$$A(Bv) = (AB)v$$
Since $AB = BA$:
$$A(Bv) = (BA)v = B(Av) = B(\\lambda v) = \\lambda (Bv)$$
This shows that $Bv$ satisfies $A(Bv) = \\lambda (Bv)$.<br>
Therefore:
<span class=\"ans\">$$Bv \\in E(\\lambda, A)$$</span>
Hence, the eigenspace $E(\\lambda, A)$ is strictly <strong>invariant under $B$</strong>.</p>

<p><span class="part">Part (b): Existence of a Common Eigenvector</span><br>
Since the underlying scalar field is $\\mathbb{C}$, the characteristic polynomial of $A$ has at least one complex root, so $A$ possesses at least one eigenvalue $\\lambda \\in \\mathbb{C}$ with $\\dim E(\\lambda, A) \\ge 1$.<br>
Consider the restriction of $B$ to this invariant subspace:
$$B_0 = B|_{E(\\lambda, A)}: E(\\lambda, A) \\to E(\\lambda, A)$$
Because $E(\\lambda, A)$ is a non-trivial finite-dimensional complex vector space, by the Fundamental Theorem of Algebra, the characteristic polynomial of $B_0$ factors completely over $\\mathbb{C}$.<br>
Hence $B_0$ has at least one eigenvalue $\\mu \\in \\mathbb{C}$ and an associated non-zero eigenvector $u \\in E(\\lambda, A)$:
$$B_0 u = \\mu u \\implies <span class=\"ans\">Bu = \\mu u</span>$$
At the same time, because $u \\in E(\\lambda, A)$ by construction:
<span class=\"ans\">$$Au = \\lambda u$$</span>
Therefore, $u \\ne 0$ is a <strong>simultaneous (common) eigenvector</strong> of both $A$ and $B$.</p>

<p><span class="part">Part (c): Condition for Simultaneous Diagonalizability</span><br>
<span class=\"ans\">No, a single common eigenvector does not guarantee simultaneous diagonalizability.</span><br>
Commuting matrices $A$ and $B$ are simultaneously diagonalizable if and only if <strong>both $A$ and $B$ are individually diagonalizable</strong>.<br>
If either matrix has non-trivial Jordan blocks (is defective, e.g. $A = \\begin{pmatrix} 0 & 1 \\\\ 0 & 0 \\end{pmatrix}$ and $B = I$), they commute and share eigenvectors, but cannot be diagonalized together because no basis of eigenvectors exists for $A$.</p>""",
        "takeaway": "Commuting operators on complex vector spaces always share at least one common eigenvector, because eigenspaces of one operator are invariant under the other. However, simultaneous diagonalization requires both operators to be individually diagonalizable."
    },
    {
        "id": 20792,
        "subject": "LAA",
        "topicId": "07_Commuting_Operators_and_Simultaneous_Diagonalization",
        "topicTitle": "07 · Commuting & Simultaneous Diag",
        "title": "Simultaneous Modal Matrix Construction for Commuting Symmetric Matrices (Stanford EE263 / MIT 18.06)",
        "kind2": "pyq",
        "source": "Stanford EE263 Introduction to Linear Dynamical Systems / MIT 18.06",
        "marks": "[8 Marks]",
        "question": """<p>Consider the two matrices:
$$A = \\begin{pmatrix} 1 & 2 \\\\ 2 & 1 \\end{pmatrix}, \\qquad B = \\begin{pmatrix} 3 & 4 \\\\ 4 & 3 \\end{pmatrix}$$</p>
<p><span class="part">(a)</span> Compute the matrix products $AB$ and $BA$, and verify that $A$ and $B$ commute.</p>
<p><span class="part">(b)</span> Compute the eigenvalues and eigenvectors of $A$, and verify that the same eigenvectors diagonalize $B$.</p>
<p><span class="part">(c)</span> Construct an invertible modal matrix $P$ and verify that $P^{-1} A P$ and $P^{-1} B P$ are simultaneously diagonal.</p>""",
        "solution": """<p><span class="part">Part (a): Commutativity Check</span><br>
Compute $AB$:
$$AB = \\begin{pmatrix} 1 & 2 \\\\ 2 & 1 \\end{pmatrix} \\begin{pmatrix} 3 & 4 \\\\ 4 & 3 \\end{pmatrix} = \\begin{pmatrix} 1(3) + 2(4) & 1(4) + 2(3) \\\\ 2(3) + 1(4) & 2(4) + 1(3) \\end{pmatrix} = <span class=\"ans\">\\begin{pmatrix} 11 & 10 \\\\ 10 & 11 \\end{pmatrix}</span>$$
Compute $BA$:
$$BA = \\begin{pmatrix} 3 & 4 \\\\ 4 & 3 \\end{pmatrix} \\begin{pmatrix} 1 & 2 \\\\ 2 & 1 \\end{pmatrix} = \\begin{pmatrix} 3(1) + 4(2) & 3(2) + 4(1) \\\\ 4(1) + 3(2) & 4(2) + 3(1) \\end{pmatrix} = <span class=\"ans\">\\begin{pmatrix} 11 & 10 \\\\ 10 & 11 \\end{pmatrix}</span>$$
Since $AB = BA$, the matrices <strong>commute</strong>.</p>

<p><span class="part">Part (b): Eigensystem of $A$ and Verification on $B$</span><br>
1. <strong>Characteristic polynomial of $A$:</strong>
$$\\det(A - \\lambda I) = (1 - \\lambda)^2 - 4 = \\lambda^2 - 2\\lambda - 3 = (\\lambda - 3)(\\lambda + 1) = 0$$
Eigenvalues of $A$: $\\lambda_1 = 3, \\lambda_2 = -1$.
- For $\\lambda_1 = 3$:
$$(A - 3I)v_1 = \\begin{pmatrix} -2 & 2 \\\\ 2 & -2 \\end{pmatrix} \\begin{pmatrix} x_1 \\\\ x_2 \\end{pmatrix} = 0 \\implies v_1 = <span class=\"ans\">\\begin{pmatrix} 1 \\\\ 1 \\end{pmatrix}</span>$$
- For $\\lambda_2 = -1$:
$$(A + I)v_2 = \\begin{pmatrix} 2 & 2 \\\\ 2 & 2 \\end{pmatrix} \\begin{pmatrix} x_1 \\\\ x_2 \\end{pmatrix} = 0 \\implies v_2 = <span class=\"ans\">\\begin{pmatrix} 1 \\\\ -1 \\end{pmatrix}</span>$$
2. <strong>Testing $v_1, v_2$ on $B$:</strong>
$$B v_1 = \\begin{pmatrix} 3 & 4 \\\\ 4 & 3 \\end{pmatrix} \\begin{pmatrix} 1 \\\\ 1 \\end{pmatrix} = \\begin{pmatrix} 7 \\\\ 7 \\end{pmatrix} = <span class=\"ans\">7 v_1</span> \\implies \\mu_1 = 7$$
$$B v_2 = \\begin{pmatrix} 3 & 4 \\\\ 4 & 3 \\end{pmatrix} \\begin{pmatrix} 1 \\\\ -1 \\end{pmatrix} = \\begin{pmatrix} -1 \\\\ 1 \\end{pmatrix} = <span class=\"ans\">-1 v_2</span> \\implies \\mu_2 = -1$$
$v_1$ and $v_2$ are simultaneously eigenvectors of $B$.</p>

<p><span class="part">Part (c): Simultaneous Diagonalization</span><br>
Assemble eigenvectors into modal matrix $P$:
<span class=\"ans\">$$P = \\begin{pmatrix} 1 & 1 \\\\ 1 & -1 \\end{pmatrix}$$</span>
Determinant: $\\det(P) = -1 - 1 = -2$. Inverse:
$$P^{-1} = -\\frac{1}{2} \\begin{pmatrix} -1 & -1 \\\\ -1 & 1 \\end{pmatrix} = \\frac{1}{2} \\begin{pmatrix} 1 & 1 \\\\ 1 & -1 \\end{pmatrix}$$
Verify diagonal forms:
<span class=\"ans\">$$P^{-1} A P = \\begin{pmatrix} 3 & 0 \\\\ 0 & -1 \\end{pmatrix}, \\qquad P^{-1} B P = \\begin{pmatrix} 7 & 0 \\\\ 0 & -1 \\end{pmatrix}$$</span>
Both matrices are diagonalized by the identical transformation $P$.</p>""",
        "takeaway": "Commuting symmetric matrices AB = BA share a common orthonormal basis of eigenvectors, allowing simultaneous diagonalization P^(-1) A P = D_A and P^(-1) B P = D_B."
    },
    {
        "id": 20793,
        "subject": "LAA",
        "topicId": "07_Commuting_Operators_and_Simultaneous_Diagonalization",
        "topicTitle": "07 · Commuting & Simultaneous Diag",
        "title": "Lagrange Polynomial Representation of Commuting Matrices & Defective Counterexamples (Generated IISc / IIT Madras & Princeton MAT 217)",
        "kind2": "generated",
        "source": "Generated IISc Midterm / IIT Madras CSE & Princeton MAT 217",
        "marks": "[8 Marks]",
        "question": """<p><span class="part">(a)</span> Suppose $A \\in \\mathbb{C}^{n \\times n}$ has $n$ distinct eigenvalues $\\lambda_1, \\dots, \\lambda_n$. Prove that any matrix $B \\in \\mathbb{C}^{n \\times n}$ that commutes with $A$ ($AB = BA$) must be a polynomial in $A$ of degree at most $n - 1$:
$$B = c_0 I + c_1 A + \\dots + c_{n-1} A^{n-1}$$</p>
<p><span class="part">(b)</span> Provide a concrete counterexample of two $2 \\times 2$ matrices $A$ and $B$ that commute ($AB = BA$), yet are <strong>NOT simultaneously diagonalizable</strong>. Explain the precise structural defect that prevents simultaneous diagonalization.</p>""",
        "solution": """<p><span class="part">Part (a): Commuting Matrix as a Polynomial via Lagrange Interpolation</span><br>
Let $(v_1, \\dots, v_n)$ be the eigenvectors corresponding to the $n$ distinct eigenvalues $\\lambda_1, \\dots, \\lambda_n$ of $A$.<br>
Since all eigenvalues are distinct, $(v_1, \\dots, v_n)$ forms a basis of $\\mathbb{C}^n$.<br>
Because $AB = BA$, each eigenspace $E(\\lambda_j, A) = \\operatorname{span}(v_j)$ is 1-dimensional and invariant under $B$.<br>
Therefore, each $v_j$ is also an eigenvector of $B$:
$$B v_j = \\mu_j v_j \\quad \\text{for some } \\mu_j \\in \\mathbb{C}$$
Now construct the Lagrange interpolating polynomial $p(z) \\in \\mathcal{P}_{n-1}(\\mathbb{C})$ passing through $( \\lambda_j, \\mu_j )$:
$$p(z) = \\sum_{j=1}^n \\mu_j \\prod_{k \\ne j} \\frac{z - \\lambda_k}{\\lambda_j - \\lambda_k} = c_0 + c_1 z + \\dots + c_{n-1} z^{n-1}$$
By construction, $p(\\lambda_j) = \\mu_j$ for all $j \\in \\{1, \\dots, n\\}$.<br>
Now evaluate the matrix polynomial $p(A)$ on each basis vector $v_j$:
$$p(A) v_j = p(\\lambda_j) v_j = \\mu_j v_j = B v_j$$
Since the linear maps $p(A)$ and $B$ agree on every vector of a basis of $\\mathbb{C}^n$, they are identical:
<span class=\"ans\">$$B = p(A) = c_0 I + c_1 A + \\dots + c_{n-1} A^{n-1}$$</span></p>

<p><span class="part">Part (b): Commuting Defective Counterexample</span><br>
Consider the two nilpotent Jordan matrices:
<span class=\"ans\">$$A = \\begin{pmatrix} 0 & 1 \\\\ 0 & 0 \\end{pmatrix}, \\qquad B = \\begin{pmatrix} 0 & 2 \\\\ 0 & 0 \\end{pmatrix}$$</span>
1. <strong>Commutativity Check:</strong>
$$AB = \\begin{pmatrix} 0 & 1 \\\\ 0 & 0 \\end{pmatrix} \\begin{pmatrix} 0 & 2 \\\\ 0 & 0 \\end{pmatrix} = \\begin{pmatrix} 0 & 0 \\\\ 0 & 0 \\end{pmatrix}$$
$$BA = \\begin{pmatrix} 0 & 2 \\\\ 0 & 0 \\end{pmatrix} \\begin{pmatrix} 0 & 1 \\\\ 0 & 0 \\end{pmatrix} = \\begin{pmatrix} 0 & 0 \\\\ 0 & 0 \\end{pmatrix}$$
$AB = BA = 0$, so they <strong>commute</strong>.<br>
2. <strong>Defect Analysis:</strong><br>
The characteristic polynomial of $A$ is $\\lambda^2 = 0 \\implies \\lambda = 0$ with algebraic multiplicity 2.<br>
The eigenspace of $A$ is:
$$E(0, A) = \\operatorname{null}\\begin{pmatrix} 0 & 1 \\\\ 0 & 0 \\end{pmatrix} = \\operatorname{span}\\left( \\begin{pmatrix} 1 \\\\ 0 \\end{pmatrix} \\right)$$
$\\dim E(0, A) = 1 < 2$. $A$ has only 1 linearly independent eigenvector.<br>
<span class=\"ans\">Structural Defect:</span> $A$ is defective and is <strong>not even individually diagonalizable</strong>. Because no invertible matrix $P$ can diagonalize $A$ alone, there cannot exist any basis that simultaneously diagonalizes both $A$ and $B$.</p>""",
        "takeaway": "If A has n distinct eigenvalues, any matrix B commuting with A is uniquely a polynomial B = p(A) of degree <= n-1. Commuting matrices fail to be simultaneously diagonalizable if one or both are defective (possessing non-trivial Jordan blocks)."
    },

    # =========================================================================
    # TOPIC 08: Generalized Eigenspaces and Nilpotent Operators
    # =========================================================================
    {
        "id": 20891,
        "subject": "LAA",
        "topicId": "08_Generalized_Eigenspaces_and_Nilpotent_Operators",
        "topicTitle": "08 · Generalized Eigenspaces & Nilpotence",
        "title": "Nilpotency Index Upper Bound via Ascending Null Space Chains (IISc Midterm 2 / Axler 8.A)",
        "kind2": "pyq",
        "source": "IISc Midterm 2 / Axler Linear Algebra Done Right 8.A",
        "marks": "[6 Marks]",
        "question": """<p>Let $V$ be an $n$-dimensional vector space over field $\\mathbb{F}$. A linear operator $N \\in \\mathcal{L}(V)$ is called <strong>nilpotent</strong> if $N^k = 0$ for some positive integer $k$.</p>
<p><span class="part">(a)</span> Consider the ascending chain of null spaces:
$$\\{0\\} = \\operatorname{null}(N^0) \\subseteq \\operatorname{null}(N^1) \\subseteq \\operatorname{null}(N^2) \\subseteq \\dots \\subseteq \\operatorname{null}(N^k) \\subseteq \\dots$$
Prove that if $\\operatorname{null}(N^k) = \\operatorname{null}(N^{k+1})$ for some integer $k$, then $\\operatorname{null}(N^{k+m}) = \\operatorname{null}(N^k)$ for all $m \\ge 1$.</p>
<p><span class="part">(b)</span> Prove rigorously using the pigeonhole principle on subspace dimensions that:
$$N^n = 0$$
(i.e., the nilpotency index cannot exceed the dimension of the space).</p>
<p><span class="part">(c)</span> What is the only eigenvalue of a nilpotent operator $N$?</p>""",
        "solution": """<p><span class="part">Part (a): Chain Stabilization Proof</span><br>
Suppose $\\operatorname{null}(N^k) = \\operatorname{null}(N^{k+1})$. We prove $\\operatorname{null}(N^{k+2}) = \\operatorname{null}(N^{k+1})$ by induction.<br>
Clearly $\\operatorname{null}(N^{k+1}) \\subseteq \\operatorname{null}(N^{k+2})$ always holds.<br>
For the reverse inclusion, let $v \\in \\operatorname{null}(N^{k+2})$.
$$N^{k+2} v = 0 \\implies N^{k+1} (Nv) = 0 \\implies Nv \\in \\operatorname{null}(N^{k+1})$$
By hypothesis, $\\operatorname{null}(N^{k+1}) = \\operatorname{null}(N^k)$, so:
$$Nv \\in \\operatorname{null}(N^k) \\implies N^k(Nv) = 0 \\implies N^{k+1} v = 0 \\implies v \\in \\operatorname{null}(N^{k+1})$$
Thus $\\operatorname{null}(N^{k+2}) = \\operatorname{null}(N^{k+1}) = \\operatorname{null}(N^k)$.<br>
By induction on $m$:
<span class=\"ans\">$$\\operatorname{null}(N^{k+m}) = \\operatorname{null}(N^k) \\quad \\text{for all } m \\ge 1$$</span>
Once the chain stabilizes at any step, it remains permanently constant.</p>

<p><span class="part">Part (b): Proof that $N^n = 0$</span><br>
Suppose for contradiction that $N^n \\ne 0$.<br>
Then $\\operatorname{null}(N^n) \\ne V$.<br>
By Part (a), if equality had occurred at any step $k < n$, the chain would have stabilized at step $k$, meaning $\\operatorname{null}(N^k) = \\operatorname{null}(N^n) = V$ (since $N$ is nilpotent and must eventually equal $V$), contradicting $N^n \\ne 0$.<br>
Therefore, every inclusion up to step $n$ must be <strong>strictly proper</strong>:
$$\\{0\\} \\subsetneq \\operatorname{null}(N^1) \\subsetneq \\operatorname{null}(N^2) \\subsetneq \\dots \\subsetneq \\operatorname{null}(N^n) \\subsetneq \\operatorname{null}(N^{n+1}) \\subseteq V$$
Each strictly proper inclusion between subspaces forces a dimension increase of at least 1:
$$0 < \\dim \\operatorname{null}(N^1) < \\dim \\operatorname{null}(N^2) < \\dots < \\dim \\operatorname{null}(N^n) < \\dim \\operatorname{null}(N^{n+1}) \\le \\dim V = n$$
This sequence consists of $n + 2$ strictly increasing non-negative integers bounded between $0$ and $n$:
$$\\dim \\operatorname{null}(N^{n+1}) \\ge n + 1 > n = \\dim V$$
This is an absolute impossibility since no subspace can have dimension exceeding $\\dim V = n$.<br>
Contradiction! Hence the chain must have stabilized at or before step $n$:
<span class=\"ans\">$$\\operatorname{null}(N^n) = V \\implies N^n v = 0 \\quad \\forall v \\in V \\implies N^n = 0$$</span></p>

<p><span class="part">Part (c): Eigenvalues of Nilpotent Operators</span><br>
Let $\\lambda$ be an eigenvalue of $N$ with eigenvector $v \\ne 0$: $Nv = \\lambda v$.<br>
Then $N^n v = \\lambda^n v$. Since $N^n = 0$:
$$0 = \\lambda^n v \\implies \\lambda^n = 0 \\implies <span class=\"ans\">\\lambda = 0</span>$$
The only eigenvalue of a nilpotent operator is $\\lambda = 0$ (with algebraic multiplicity $n$).</p>""",
        "takeaway": "Strictly ascending null space chains {0} ⊊ null(N) ⊊ null(N^2) ⊊ ... cannot have length exceeding n = dim V by the pigeonhole principle. Hence N^n = 0 for any nilpotent operator, and its only eigenvalue is 0."
    },
    {
        "id": 20892,
        "subject": "LAA",
        "topicId": "08_Generalized_Eigenspaces_and_Nilpotent_Operators",
        "topicTitle": "08 · Generalized Eigenspaces & Nilpotence",
        "title": "Generalized Eigenspace Computation & Direct Sum Decomposition (MIT 18.06 / Stanford EE263)",
        "kind2": "pyq",
        "source": "MIT 18.06 Linear Algebra / Stanford EE263 Introduction to Linear Dynamical Systems",
        "marks": "[8 Marks]",
        "question": """<p>Consider the matrix:
$$A = \\begin{pmatrix} 2 & 1 & 0 \\\\ 0 & 2 & 0 \\\\ 0 & 0 & 3 \\end{pmatrix}$$</p>
<p><span class="part">(a)</span> State the definition of the generalized eigenspace $G(\\lambda, A) = \\operatorname{null}(A - \\lambda I)^n$ for an $n \\times n$ matrix.</p>
<p><span class="part">(b)</span> Compute $(A - 2I)^3$ and find a basis for $G(2, A)$.</p>
<p><span class="part">(c)</span> Compute $(A - 3I)^3$ and find a basis for $G(3, A)$, and verify that $\\mathbb{R}^3 = G(2, A) \\oplus G(3, A)$.</p>""",
        "solution": """<p><span class="part">Part (a): Generalized Eigenspace Definition</span><br>
For an operator $A$ on an $n$-dimensional space, the generalized eigenspace corresponding to eigenvalue $\\lambda$ is:
<span class=\"ans\">$$G(\\lambda, A) = \\operatorname{null}(A - \\lambda I)^n$$</span>
Vectors in $G(\\lambda, A)$ satisfy $(A - \\lambda I)^k v = 0$ for some $k \\ge 1$. The chain stabilizes by step $n = \\dim V$, so setting $k = n$ captures all generalized eigenvectors.</p>

<p><span class="part">Part (b): Computation of $G(2, A)$</span><br>
Here $n = 3$. Compute powers of $(A - 2I)$:
$$A - 2I = \\begin{pmatrix} 0 & 1 & 0 \\\\ 0 & 0 & 0 \\\\ 0 & 0 & 1 \\end{pmatrix}$$
$$(A - 2I)^2 = \\begin{pmatrix} 0 & 0 & 0 \\\\ 0 & 0 & 0 \\\\ 0 & 0 & 1 \\end{pmatrix}, \\qquad (A - 2I)^3 = \\begin{pmatrix} 0 & 0 & 0 \\\\ 0 & 0 & 0 \\\\ 0 & 0 & 1 \\end{pmatrix}$$
Set $(A - 2I)^3 x = 0$:
$$\\begin{pmatrix} 0 & 0 & 0 \\\\ 0 & 0 & 0 \\\\ 0 & 0 & 1 \\end{pmatrix} \\begin{pmatrix} x_1 \\\\ x_2 \\\\ x_3 \\end{pmatrix} = \\begin{pmatrix} 0 \\\\ 0 \\\\ 0 \\end{pmatrix} \\implies x_3 = 0, \\quad x_1, x_2 \\in \\mathbb{R} \\text{ free}$$
A basis for $G(2, A)$ is:
<span class=\"ans\">$$G(2, A) = \\operatorname{span}\\left( \\begin{pmatrix} 1 \\\\ 0 \\\\ 0 \\end{pmatrix}, \\; \\begin{pmatrix} 0 \\\\ 1 \\\\ 0 \\end{pmatrix} \\right) = \\operatorname{span}(e_1, e_2), \\qquad \\dim G(2, A) = 2$$</span></p>

<p><span class="part">Part (c): Computation of $G(3, A)$ and Direct Sum</span><br>
Compute $(A - 3I)$:
$$A - 3I = \\begin{pmatrix} -1 & 1 & 0 \\\\ 0 & -1 & 0 \\\\ 0 & 0 & 0 \\end{pmatrix}$$
$$(A - 3I)^2 = \\begin{pmatrix} 1 & -2 & 0 \\\\ 0 & 1 & 0 \\\\ 0 & 0 & 0 \\end{pmatrix}, \\qquad (A - 3I)^3 = \\begin{pmatrix} -1 & 3 & 0 \\\\ 0 & -1 & 0 \\\\ 0 & 0 & 0 \\end{pmatrix}$$
Set $(A - 3I)^3 x = 0$:
$$-x_1 + 3x_2 = 0 \\quad \\text{and} \\quad -x_2 = 0 \\implies x_1 = 0, x_2 = 0, \\quad x_3 \\in \\mathbb{R} \\text{ free}$$
A basis for $G(3, A)$ is:
<span class=\"ans\">$$G(3, A) = \\operatorname{span}\\left( \\begin{pmatrix} 0 \\\\ 0 \\\\ 1 \\end{pmatrix} \\right) = \\operatorname{span}(e_3), \\qquad \\dim G(3, A) = 1$$</span>
<strong>Direct Sum Verification:</strong><br>
The union of bases is $\\{e_1, e_2, e_3\\}$, which is the standard basis of $\\mathbb{R}^3$.
$$G(2, A) \\cap G(3, A) = \\{0\\}, \\qquad \\dim G(2, A) + \\dim G(3, A) = 2 + 1 = 3 = \\dim \\mathbb{R}^3$$
Therefore:
<span class=\"ans\">$$\\mathbb{R}^3 = G(2, A) \\oplus G(3, A)$$</span>
The dimension of each generalized eigenspace equals the algebraic multiplicity of its eigenvalue.</p>""",
        "takeaway": "Every operator on a complex vector space decomposes the space into a direct sum of its generalized eigenspaces: V = G(lambda_1, T) ⊕ ... ⊕ G(lambda_m, T), where dim G(lambda_i, T) equals the algebraic multiplicity."
    },
    {
        "id": 20893,
        "subject": "LAA",
        "topicId": "08_Generalized_Eigenspaces_and_Nilpotent_Operators",
        "topicTitle": "08 · Generalized Eigenspaces & Nilpotence",
        "title": "Neumann Polynomial Invertibility of I + N & Strict Eigenspace Containment (Generated IISc / Berkeley EECS 127 & IIT Delhi)",
        "kind2": "generated",
        "source": "Generated IISc Midterm / Berkeley EECS 127 & IIT Delhi (Axler 8.B)",
        "marks": "[8 Marks]",
        "question": """<p><span class="part">(a)</span> Let $N \\in \\mathcal{L}(V)$ be a nilpotent operator on an $n$-dimensional vector space ($N^n = 0$). Prove that $(I + N)$ is invertible, and express $(I + N)^{-1}$ as a finite polynomial in $N$.</p>
<p><span class="part">(b)</span> For an arbitrary operator $T \\in \\mathcal{L}(V)$ and eigenvalue $\\lambda$, prove that $\\operatorname{null}(T - \\lambda I) \\subseteq G(\\lambda, T)$.</p>
<p><span class="part">(c)</span> Provide an explicit $2 \\times 2$ matrix example where the containment is strict: $\\operatorname{null}(T - \\lambda I) \\subsetneq G(\\lambda, T)$.</p>""",
        "solution": """<p><span class="part">Part (a): Invertibility of $I + N$ & Neumann Polynomial</span><br>
Since $N$ is nilpotent on an $n$-dimensional space, $N^n = 0$.<br>
Consider the algebraic factorization identity for geometric polynomials:
$$(I + N)(I - N + N^2 - N^3 + \\dots + (-1)^{n-1} N^{n-1}) = I + (-1)^{n-1} N^n$$
Since $N^n = 0$, the right-hand side simplifies identically to:
<span class=\"ans\">$$(I + N)(I - N + N^2 - N^3 + \\dots + (-1)^{n-1} N^{n-1}) = I$$</span>
Since $(I + N)$ has a two-sided inverse in finite dimensions, it is invertible, with inverse:
<span class=\"ans\">$$(I + N)^{-1} = \\sum_{k=0}^{n-1} (-1)^k N^k = I - N + N^2 - N^3 + \\dots + (-1)^{n-1} N^{n-1}$$</span></p>

<p><span class="part">Part (b): Proof of Containment $\\operatorname{null}(T - \\lambda I) \\subseteq G(\\lambda, T)$</span><br>
Let $v \\in \\operatorname{null}(T - \\lambda I)$. By definition:
$$(T - \\lambda I)v = 0$$
Apply $(T - \\lambda I)^{n-1}$ to both sides (where $n = \\dim V \\ge 1$):
$$(T - \\lambda I)^n v = (T - \\lambda I)^{n-1} [(T - \\lambda I) v] = (T - \\lambda I)^{n-1} (0) = 0$$
Since $(T - \\lambda I)^n v = 0$, by definition $v \\in \\operatorname{null}(T - \\lambda I)^n = G(\\lambda, T)$.<br>
Therefore:
<span class=\"ans\">$$\\operatorname{null}(T - \\lambda I) \\subseteq G(\\lambda, T)$$</span></p>

<p><span class="part">Part (c): Strict Containment Example</span><br>
Let $A = \\begin{pmatrix} 0 & 1 \\\\ 0 & 0 \\end{pmatrix} \\in \\mathbb{R}^{2 \\times 2}$. The only eigenvalue is $\\lambda = 0$.
1. <strong>Standard Eigenspace:</strong>
$$\\operatorname{null}(A - 0I) = \\operatorname{null}\\begin{pmatrix} 0 & 1 \\\\ 0 & 0 \\end{pmatrix} = \\left\\{ \\begin{pmatrix} x_1 \\\\ 0 \\end{pmatrix} : x_1 \\in \\mathbb{R} \\right\\} = \\operatorname{span}(e_1)$$
$\\dim \\operatorname{null}(A) = 1$.
2. <strong>Generalized Eigenspace:</strong>
Compute $A^2$:
$$A^2 = \\begin{pmatrix} 0 & 1 \\\\ 0 & 0 \\end{pmatrix} \\begin{pmatrix} 0 & 1 \\\\ 0 & 0 \\end{pmatrix} = \\begin{pmatrix} 0 & 0 \\\\ 0 & 0 \\end{pmatrix} = 0$$
$$G(0, A) = \\operatorname{null}(A^2) = \\operatorname{null}\\begin{pmatrix} 0 & 0 \\\\ 0 & 0 \\end{pmatrix} = \\mathbb{R}^2$$
$\\dim G(0, A) = 2$.<br>
Notice that $e_2 = \\begin{pmatrix} 0 \\\\ 1 \\end{pmatrix} \\in G(0, A)$ because $A^2 e_2 = 0$, but $e_2 \\notin \\operatorname{null}(A)$ because $A e_2 = e_1 \\ne 0$.<br>
Hence:
<span class=\"ans\">$$\\operatorname{null}(A) \\subsetneq G(0, A) \\quad (1 < 2)$$</span>
The containment is strictly proper.</p>""",
        "takeaway": "If N is nilpotent with N^n = 0, (I + N) is invertible with inverse given by the truncated Neumann polynomial sum_{k=0}^{n-1} (-1)^k N^k. The standard eigenspace is strictly contained in the generalized eigenspace whenever an operator has defective Jordan blocks."
    }
]

def main():
    with open(PRACTICE_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    if "20791" in content:
        print("Batch 07-08 already present in practice_laa.js!")
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
    for card in PRACTICE_LAA_07_08:
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

    print("Successfully added LAA Batch 07-08 (6 cards). Total in file now updated.")

if __name__ == "__main__":
    main()
