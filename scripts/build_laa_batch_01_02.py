#!/usr/bin/env python3
"""
Builder script for LAA Practice Cards: Batch 01 (Topics 01 & 02)
Topic 01: Vector Spaces, Subspaces & Direct Sums (Cards 20191, 20192, 20193)
Topic 02: Linear Independence, Bases & Dimension (Cards 20291, 20292, 20293)
"""

import json
import os
import re

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRACTICE_FILE = os.path.join(REPO_DIR, "practice_laa.js")

PRACTICE_LAA_01_02 = [
    # =========================================================================
    # TOPIC 01: Vector Spaces, Subspaces & Direct Sums
    # =========================================================================
    {
        "id": 20191,
        "subject": "LAA",
        "topicId": "01_Vector_Spaces_Subspaces_and_Direct_Sums",
        "topicTitle": "01 · Vector Spaces, Subspaces & Direct Sums",
        "title": "Non-Uniqueness of Direct Sum Complements (IISc Endsem 2024 / Axler 1.C)",
        "kind2": "pyq",
        "source": "IISc Endsem 2024 / Axler Linear Algebra Done Right 1.C",
        "marks": "[6 Marks]",
        "question": """<p>Let $U_1, U_2, U_3$ be subspaces of a vector space $V$.</p>
<p><span class="part">(a)</span> State the definition of the internal direct sum $V = U_1 \\oplus U_2$ in terms of sum existence and uniqueness of representation.</p>
<p><span class="part">(b)</span> Prove or provide a concrete counterexample to the cancellation proposition:
$$\\text{If } U_1 \\oplus U_2 = U_1 \\oplus U_3, \\quad \\text{does it necessarily follow that } U_2 = U_3?$$</p>
<p><span class="part">(c)</span> What does this imply about the geometric uniqueness of subspace complements in linear algebra?</p>""",
        "solution": """<p><span class="part">Part (a): Direct Sum Definition</span><br>
The sum $V = U_1 \\oplus U_2$ is an internal direct sum if and only if:
1. $V = U_1 + U_2$, meaning every vector $v \\in V$ can be written as $v = u_1 + u_2$ with $u_1 \\in U_1, u_2 \\in U_2$.
2. The representation is unique, which is equivalent to <span class=\"ans\">$U_1 \\cap U_2 = \\{0\\}$</span> (or the only way to write $0 = u_1 + u_2$ is $u_1 = 0, u_2 = 0$).</p>

<p><span class="part">Part (b): Cancellation Property Counterexample</span><br>
<span class=\"ans\">The proposition is FALSE: $U_1 \\oplus U_2 = U_1 \\oplus U_3 \\not\\implies U_2 = U_3$.</span><br>
<strong>Counterexample in $V = \\mathbb{R}^2$:</strong><br>
Let $e_1 = (1, 0)^\\top$ and $e_2 = (0, 1)^\\top$. Define three 1D subspaces:
<ul>
  <li>$U_1 = \\operatorname{span}(e_1) = \\{ (x, 0) : x \\in \\mathbb{R} \\}$ (the $x$-axis).</li>
  <li>$U_2 = \\operatorname{span}(e_2) = \\{ (0, y) : y \\in \\mathbb{R} \\}$ (the $y$-axis).</li>
  <li>$U_3 = \\operatorname{span}(e_1 + e_2) = \\{ (z, z) : z \\in \\mathbb{R} \\}$ (the line $y = x$).</li>
</ul>
1. <strong>Verification for $U_1 \\oplus U_2$:</strong>
$$U_1 \\cap U_2 = \\{ (x, 0) \\} \\cap \\{ (0, y) \\} = \\{ (0, 0) \\}$$
$$U_1 + U_2 = \\{ (x, y) : x, y \\in \\mathbb{R} \\} = \\mathbb{R}^2 \\implies U_1 \\oplus U_2 = \\mathbb{R}^2$$
2. <strong>Verification for $U_1 \\oplus U_3$:</strong>
If $(x, 0) = (z, z)$, then $z = 0 \\implies x = 0$, so $U_1 \\cap U_3 = \\{ (0, 0) \\}$.<br>
Any vector $(x, y) \\in \\mathbb{R}^2$ decomposes as:
$$(x, y) = (x - y, 0) + (y, y) \\in U_1 + U_3$$
where $(x - y, 0) \\in U_1$ and $(y, y) \\in U_3$. Thus $U_1 \\oplus U_3 = \\mathbb{R}^2$.<br>
Both direct sums equal $\\mathbb{R}^2$, yet <span class=\"ans\">$U_2 \\ne U_3$</span> (since $(0, 1) \\in U_2$ but $(0, 1) \\notin U_3$).</p>

<p><span class="part">Part (c): Geometric Implication</span><br>
Subspace complements are <strong>not unique</strong>. While the dimension of any complement is invariant ($\\dim U_2 = \\dim U_3 = \\dim V - \\dim U_1$), there exist infinitely many distinct algebraic complements for any proper non-trivial subspace $U_1$. (Uniqueness of complement is restored only when an inner product is introduced and we restrict to the <em>orthogonal complement</em> $U_1^\\perp$).</p>""",
        "takeaway": "Direct sum complements are not unique: U1 ⊕ U2 = U1 ⊕ U3 does NOT imply U2 = U3. Any non-parallel line in R^2 is a valid complement to the x-axis."
    },
    {
        "id": 20192,
        "subject": "LAA",
        "topicId": "01_Vector_Spaces_Subspaces_and_Direct_Sums",
        "topicTitle": "01 · Vector Spaces, Subspaces & Direct Sums",
        "title": "Direct Sum Decomposition of Matrix Space into Symmetric & Skew-Symmetric (IIT Bombay / Stanford EE263)",
        "kind2": "pyq",
        "source": "IIT Bombay CSE Entrance / Stanford EE263 Introduction to Linear Dynamical Systems",
        "marks": "[8 Marks]",
        "question": """<p>Let $V = \\mathbb{R}^{n \\times n}$ be the vector space of all $n \\times n$ real matrices. Define two subsets:
$$U_{\\text{sym}} = \\{ A \\in V : A^\\top = A \\}, \\qquad U_{\\text{skew}} = \\{ A \\in V : A^\\top = -A \\}$$</p>
<p><span class="part">(a)</span> Prove that $U_{\\text{sym}}$ and $U_{\\text{skew}}$ are subspaces of $V$.</p>
<p><span class="part">(b)</span> Prove that $V = U_{\\text{sym}} \\oplus U_{\\text{skew}}$ is a direct sum decomposition.</p>
<p><span class="part">(c)</span> Compute the exact dimensions $\\dim U_{\\text{sym}}$ and $\\dim U_{\\text{skew}}$, and verify that their sum equals $\\dim V = n^2$.</p>""",
        "solution": """<p><span class="part">Part (a): Subspace Verification</span><br>
1. <strong>Zero vector:</strong> $0^\\top = 0$ and $0^\\top = -0$, so $0 \\in U_{\\text{sym}}$ and $0 \\in U_{\\text{skew}}$.<br>
2. <strong>Linear Combinations:</strong> For $A, B \\in U_{\\text{sym}}$ and $\\alpha, \\beta \\in \\mathbb{R}$:
$$(\\alpha A + \\beta B)^\\top = \\alpha A^\\top + \\beta B^\\top = \\alpha A + \\beta B \\in U_{\\text{sym}}$$
For $A, B \\in U_{\\text{skew}}$:
$$(\\alpha A + \\beta B)^\\top = \\alpha (-A) + \\beta (-B) = -(\\alpha A + \\beta B) \\in U_{\\text{skew}}$$
Both subsets are closed under vector addition and scalar multiplication, hence they are valid subspaces.</p>

<p><span class="part">Part (b): Direct Sum Proof</span><br>
1. <strong>Intersection is Trivial ($U_{\\text{sym}} \\cap U_{\\text{skew}} = \\{0\\}$):</strong><br>
Let $A \\in U_{\\text{sym}} \\cap U_{\\text{skew}}$. Then $A^\\top = A$ and $A^\\top = -A$.
$$A = -A \\implies 2A = 0 \\implies <span class=\"ans\">A = 0</span>$$
Thus $U_{\\text{sym}} \\cap U_{\\text{skew}} = \\{0\\}$, establishing that any sum is direct.<br>
2. <strong>Spanning ($V = U_{\\text{sym}} + U_{\\text{skew}}$):</strong><br>
For any arbitrary matrix $A \\in \\mathbb{R}^{n \\times n}$, we can identically write:
<span class=\"ans\">$$A = \\frac{A + A^\\top}{2} + \\frac{A - A^\\top}{2}$$</span>
Let $A_1 = \\frac{A + A^\\top}{2}$: $A_1^\\top = \\frac{A^\\top + (A^\\top)^\\top}{2} = \\frac{A^\\top + A}{2} = A_1 \\implies A_1 \\in U_{\\text{sym}}$.<br>
Let $A_2 = \\frac{A - A^\\top}{2}$: $A_2^\\top = \\frac{A^\\top - A}{2} = -A_2 \\implies A_2 \\in U_{\\text{skew}}$.<br>
Since every $A \\in V$ decomposes into a symmetric and a skew-symmetric part:
<span class=\"ans\">$$V = U_{\\text{sym}} \\oplus U_{\\text{skew}}$$</span></p>

<p><span class="part">Part (c): Dimensions Computation</span><br>
1. <strong>Symmetric Matrices $U_{\\text{sym}}$:</strong><br>
A symmetric matrix is completely determined by its $n$ diagonal entries and its $\\frac{n(n-1)}{2}$ strictly upper triangular entries:
<span class=\"ans\">$$\\dim U_{\\text{sym}} = n + \\frac{n(n-1)}{2} = \\frac{n(n+1)}{2}$$</span>
2. <strong>Skew-Symmetric Matrices $U_{\\text{skew}}$:</strong><br>
For $A^\\top = -A$, diagonal elements satisfy $a_{ii} = -a_{ii} \\implies a_{ii} = 0$. The matrix is completely determined by its strictly upper triangular entries:
<span class=\"ans\">$$\\dim U_{\\text{skew}} = \\frac{n(n-1)}{2}$$</span>
3. <strong>Dimension Check:</strong>
$$\\dim U_{\\text{sym}} + \\dim U_{\\text{skew}} = \\frac{n(n+1)}{2} + \\frac{n(n-1)}{2} = \\frac{n^2 + n + n^2 - n}{2} = \\frac{2n^2}{2} = n^2 = \\dim(\\mathbb{R}^{n \\times n})$$
The dimension sum matches the full space dimension perfectly.</p>""",
        "takeaway": "Any square matrix decomposes uniquely into symmetric and skew-symmetric parts: A = (A + A^T)/2 + (A - A^T)/2. The dimensions n(n+1)/2 and n(n-1)/2 sum directly to n^2."
    },
    {
        "id": 20193,
        "subject": "LAA",
        "topicId": "01_Vector_Spaces_Subspaces_and_Direct_Sums",
        "topicTitle": "01 · Vector Spaces, Subspaces & Direct Sums",
        "title": "Direct Sum Intersection Criterion & Grassmann Dimension Bounds (Generated IISc / MIT 18.06 & Berkeley EECS 127)",
        "kind2": "generated",
        "source": "Generated IISc Midterm / MIT 18.06 (Axler 1.45) & Berkeley EECS 127",
        "marks": "[8 Marks]",
        "question": """<p><span class="part">(a)</span> Let $U_1, \\dots, U_m$ be subspaces of $V$. Prove that $U_1 + \\dots + U_m$ is a direct sum if and only if for each $j \\in \\{1, \\dots, m\\}$:
$$U_j \\cap \\left( \\sum_{k \\ne j} U_k \\right) = \\{0\\}$$
Explain the critical distinction between this necessary and sufficient condition and the pairwise condition $U_i \\cap U_j = \\{0\\}$ for all $i \\ne j$.</p>
<p><span class="part">(b)</span> Let $U_1$ and $U_2$ be two $5$-dimensional subspaces of an $8$-dimensional vector space $V$. Use Grassmann's dimension formula to determine all possible values of $\\dim(U_1 \\cap U_2)$.</p>""",
        "solution": """<p><span class="part">Part (a): Direct Sum Condition Proof & Pairwise Fallacy</span><br>
<strong>Proof:</strong><br>
$(\\implies)$ Suppose the sum is direct. Let $v \\in U_j \\cap \\left(\\sum_{k \\ne j} U_k\\right)$.<br>
Then $v \\in U_j$, and there exist $u_k \\in U_k$ ($k \\ne j$) such that $v = \\sum_{k \\ne j} u_k$.<br>
Rearranging:
$$\\sum_{k \\ne j} u_k - v = 0$$
Here $-v \\in U_j$ and $u_k \\in U_k$. Since the sum is direct, the unique representation of $0$ requires every component to be zero. In particular, $-v = 0 \\implies v = 0$. Hence the intersection is $\\{0\\}$.<br>
$(\\impliedby)$ Suppose $U_j \\cap \\left(\\sum_{k \\ne j} U_k\\right) = \\{0\\}$ for each $j$.<br>
Suppose $u_1 + \\dots + u_m = 0$ with $u_k \\in U_k$. For any fixed $j$:
$$-u_j = \\sum_{k \\ne j} u_k$$
The left side is in $U_j$, and the right side is in $\\sum_{k \\ne j} U_k$.<br>
By hypothesis, $-u_j \\in U_j \\cap \\left(\\sum_{k \\ne j} U_k\\right) = \\{0\\} \\implies u_j = 0$.<br>
Since this holds for all $j \\in \\{1, \\dots, m\\}$, all $u_j = 0$. The sum is direct.<br>
<span class=\"ans\">The Pairwise Fallacy:</span> The condition $U_i \\cap U_j = \\{0\\}$ for all $i \\ne j$ is <strong>insufficient</strong> for $m \\ge 3$.<br>
<em>Counterexample:</em> In $\\mathbb{R}^2$, let $U_1 = \\operatorname{span}(e_1)$, $U_2 = \\operatorname{span}(e_2)$, and $U_3 = \\operatorname{span}(e_1 + e_2)$. Any two intersect only at $\\{0\\}$, but $U_1 + U_2 + U_3 = \\mathbb{R}^2$ is NOT direct since $\\dim U_1 + \\dim U_2 + \\dim U_3 = 3 > 2 = \\dim \\mathbb{R}^2$ (indeed, $e_1 + e_2 - (e_1 + e_2) = 0$ is a non-trivial zero sum).</p>

<p><span class="part">Part (b): Grassmann Dimension Bounds</span><br>
Grassmann's identity for subspace sums states:
$$\\dim(U_1 + U_2) = \\dim U_1 + \\dim U_2 - \\dim(U_1 \\cap U_2)$$
Rearranging for the intersection dimension:
$$\\dim(U_1 \\cap U_2) = \\dim U_1 + \\dim U_2 - \\dim(U_1 + U_2) = 5 + 5 - \\dim(U_1 + U_2) = 10 - \\dim(U_1 + U_2)$$
Since $U_1 + U_2$ is a subspace of $V$ containing $U_1$ and $U_2$:
$$\\max(\\dim U_1, \\dim U_2) \\le \\dim(U_1 + U_2) \\le \\dim V$$
$$5 \\le \\dim(U_1 + U_2) \\le 8$$
Evaluating $\\dim(U_1 \\cap U_2) = 10 - \\dim(U_1 + U_2)$ for each possible sum dimension:
<ul>
  <li>If $\\dim(U_1 + U_2) = 8$: $\\dim(U_1 \\cap U_2) = 10 - 8 = <span class=\"ans\">2</span>$</li>
  <li>If $\\dim(U_1 + U_2) = 7$: $\\dim(U_1 \\cap U_2) = 10 - 7 = <span class=\"ans\">3</span>$</li>
  <li>If $\\dim(U_1 + U_2) = 6$: $\\dim(U_1 \\cap U_2) = 10 - 6 = <span class=\"ans\">4</span>$</li>
  <li>If $\\dim(U_1 + U_2) = 5$: $\\dim(U_1 \\cap U_2) = 10 - 5 = <span class=\"ans\">5</span>$ (occurs when $U_1 = U_2$)</li>
</ul>
<span class=\"ans\">Possible dimensions of $U_1 \\cap U_2$: $\\{2, 3, 4, 5\\}$.</span></p>""",
        "takeaway": "For m >= 3 subspaces, pairwise disjointness U_i ∩ U_j = {0} does NOT guarantee a direct sum; one must check U_j ∩ (sum_{k != j} U_k) = {0}. By Grassmann's identity, two 5D subspaces in an 8D space must intersect in at least 2 dimensions."
    },

    # =========================================================================
    # TOPIC 02: Linear Independence, Bases, and Dimension
    # =========================================================================
    {
        "id": 20291,
        "subject": "LAA",
        "topicId": "02_Linear_Independence_Bases_and_Dimension",
        "topicTitle": "02 · Independence, Bases & Dimension",
        "title": "Direct Sum Dimension Characterization via Trivial Intersection (IISc Midterm 1 / Axler 2.C)",
        "kind2": "pyq",
        "source": "IISc Midterm 1 / Axler Linear Algebra Done Right 2.C",
        "marks": "[6 Marks]",
        "question": """<p>Let $V$ be a finite-dimensional vector space, and let $U_1, U_2$ be subspaces of $V$ such that $V = U_1 + U_2$.</p>
<p><span class="part">(a)</span> State Grassmann's dimension formula relating $\\dim(U_1 + U_2)$, $\\dim U_1$, $\\dim U_2$, and $\\dim(U_1 \\cap U_2)$.</p>
<p><span class="part">(b)</span> Prove rigorously that $\\dim V = \\dim U_1 + \\dim U_2$ if and only if $U_1 \\cap U_2 = \\{0\\}$ (i.e., the sum is direct, $V = U_1 \\oplus U_2$).</p>
<p><span class="part">(c)</span> If $\\dim V = 7$, $\\dim U_1 = 4$, and $\\dim U_2 = 4$, can $V = U_1 \\oplus U_2$? What is the minimum dimension of $U_1 \\cap U_2$?</p>""",
        "solution": """<p><span class="part">Part (a): Grassmann's Dimension Formula</span><br>
For any two finite-dimensional subspaces $U_1, U_2$:
<span class=\"ans\">$$\\dim(U_1 + U_2) = \\dim U_1 + \\dim U_2 - \\dim(U_1 \\cap U_2)$$</span></p>

<p><span class="part">Part (b): If and Only If Proof</span><br>
Since $V = U_1 + U_2$, we have $\\dim(U_1 + U_2) = \\dim V$. Substituting into Grassmann's formula:
$$\\dim V = \\dim U_1 + \\dim U_2 - \\dim(U_1 \\cap U_2)$$
Rearranging:
$$\\dim V - (\\dim U_1 + \\dim U_2) = -\\dim(U_1 \\cap U_2)$$
Therefore:
<span class=\"ans\">$$\\dim V = \\dim U_1 + \\dim U_2 \\iff \\dim(U_1 \\cap U_2) = 0$$</span>
A vector subspace has dimension $0$ if and only if it contains solely the zero vector:
$$\\dim(U_1 \\cap U_2) = 0 \\iff U_1 \\cap U_2 = \\{0\\}$$
Hence, $\\dim V = \\dim U_1 + \\dim U_2 \\iff V = U_1 \\oplus U_2$.</p>

<p><span class="part">Part (c): Numerical Evaluation</span><br>
Given $\\dim V = 7, \\dim U_1 = 4, \\dim U_2 = 4$:
$$\\dim U_1 + \\dim U_2 = 4 + 4 = 8 \\ne 7 = \\dim V$$
<span class=\"ans\">No, $V$ cannot be a direct sum of $U_1$ and $U_2$</span> because $\\dim U_1 + \\dim U_2 > \\dim V$.<br>
By Grassmann's formula:
$$\\dim(U_1 \\cap U_2) = \\dim U_1 + \\dim U_2 - \\dim(U_1 + U_2) = 4 + 4 - \\dim(U_1 + U_2) = 8 - \\dim(U_1 + U_2)$$
Since $U_1 + U_2 \\subseteq V$, $\\dim(U_1 + U_2) \\le \\dim V = 7$:
$$\\dim(U_1 \\cap U_2) = 8 - \\dim(U_1 + U_2) \\ge 8 - 7 = <span class=\"ans\">1</span>$$
The minimum dimension of $U_1 \\cap U_2$ is $1$. The two subspaces must share at least a 1D line.</p>""",
        "takeaway": "When V = U1 + U2, the dimension equality dim V = dim U1 + dim U2 is mathematically equivalent to trivial intersection U1 ∩ U2 = {0}. If dim U1 + dim U2 > dim V, the subspaces MUST overlap."
    },
    {
        "id": 20292,
        "subject": "LAA",
        "topicId": "02_Linear_Independence_Bases_and_Dimension",
        "topicTitle": "02 · Independence, Bases & Dimension",
        "title": "Basis Preservation Under Difference Transformations (Stanford EE263 / MIT 18.06)",
        "kind2": "pyq",
        "source": "Stanford EE263 / MIT 18.06 Linear Algebra",
        "marks": "[6 Marks]",
        "question": """<p>Suppose $(v_1, v_2, v_3, v_4)$ is an ordered basis of a 4-dimensional vector space $V$. Consider the modified list of vectors:
$$(w_1, w_2, w_3, w_4) = (v_1 - v_2, \\; v_2 - v_3, \\; v_3 - v_4, \\; v_4)$$</p>
<p><span class="part">(a)</span> Set up a linear combination $c_1 w_1 + c_2 w_2 + c_3 w_3 + c_4 w_4 = 0$ and express it in terms of the original basis vectors $(v_1, v_2, v_3, v_4)$.</p>
<p><span class="part">(b)</span> Prove that $c_1 = c_2 = c_3 = c_4 = 0$ and conclude that $(w_1, w_2, w_3, w_4)$ is a basis of $V$.</p>
<p><span class="part">(c)</span> Express the change-of-basis matrix $P$ such that $[w_1, w_2, w_3, w_4] = [v_1, v_2, v_3, v_4] P$, and verify that $\\det(P) \\ne 0$.</p>""",
        "solution": """<p><span class="part">Part (a): Linear Combination Regrouping</span><br>
Consider the equation:
$$c_1 (v_1 - v_2) + c_2 (v_2 - v_3) + c_3 (v_3 - v_4) + c_4 v_4 = 0$$
Distributing and grouping coefficients by the original vectors $v_1, v_2, v_3, v_4$:
<span class=\"ans\">$$c_1 v_1 + (c_2 - c_1) v_2 + (c_3 - c_2) v_3 + (c_4 - c_3) v_4 = 0$$</span></p>

<p><span class="part">Part (b): Proof of Linear Independence & Basis Status</span><br>
Since $(v_1, v_2, v_3, v_4)$ is a basis of $V$, it is linearly independent. The only linear combination that equals zero is the trivial one:
$$c_1 = 0$$
$$c_2 - c_1 = 0 \\implies c_2 = c_1 = 0$$
$$c_3 - c_2 = 0 \\implies c_3 = c_2 = 0$$
$$c_4 - c_3 = 0 \\implies c_4 = c_3 = 0$$
Hence:
<span class=\"ans\">$$c_1 = c_2 = c_3 = c_4 = 0$$</span>
This proves that $(w_1, w_2, w_3, w_4)$ is linearly independent.<br>
Since $(w_1, w_2, w_3, w_4)$ is a linearly independent list of length $4$ in a $4$-dimensional space $V$, by the Basis Theorem it spans $V$ and is therefore an authentic <span class=\"ans\">basis of $V$</span>.</p>

<p><span class="part">Part (c): Change-of-Basis Matrix</span><br>
Reading off the coefficients:
$$w_1 = 1 v_1 - 1 v_2 + 0 v_3 + 0 v_4$$
$$w_2 = 0 v_1 + 1 v_2 - 1 v_3 + 0 v_4$$
$$w_3 = 0 v_1 + 0 v_2 + 1 v_3 - 1 v_4$$
$$w_4 = 0 v_1 + 0 v_2 + 0 v_3 + 1 v_4$$
The transformation matrix $P$ is upper bidiagonal:
<span class=\"ans\">$$P = \\begin{pmatrix} 1 & 0 & 0 & 0 \\\\ -1 & 1 & 0 & 0 \\\\ 0 & -1 & 1 & 0 \\\\ 0 & 0 & -1 & 1 \\end{pmatrix}$$</span>
$P$ is lower triangular with all diagonal entries equal to $1$.
$$\\det(P) = 1 \\times 1 \\times 1 \\times 1 = <span class=\"ans\">1 \\ne 0</span>$$
Because $\\det(P) = 1 \\ne 0$, $P$ is invertible, confirming that $(w_1, w_2, w_3, w_4)$ forms a valid basis.</p>""",
        "takeaway": "A list of n vectors in an n-dimensional space is a basis if and only if it is linearly independent (or equivalently, if its change-of-basis matrix has non-zero determinant). Difference telescoping yields a triangular matrix with det = 1."
    },
    {
        "id": 20293,
        "subject": "LAA",
        "topicId": "02_Linear_Independence_Bases_and_Dimension",
        "topicTitle": "02 · Independence, Bases & Dimension",
        "title": "Subspace Equality from Equal Dimensions & Polynomial Evaluation Functionals (Generated IISc / Berkeley EECS 127 & Axler 2.39)",
        "kind2": "generated",
        "source": "Generated IISc Midterm / Berkeley EECS 127 & Axler Linear Algebra Done Right 2.39",
        "marks": "[8 Marks]",
        "question": """<p><span class="part">(a)</span> Suppose $U$ is a subspace of a finite-dimensional vector space $V$ such that $\\dim U = \\dim V$. Prove that $U = V$.</p>
<p><span class="part">(b)</span> Let $\\mathcal{P}_m(\\mathbb{R})$ denote the space of polynomials of degree at most $m$ with real coefficients (which has $\\dim \\mathcal{P}_m(\\mathbb{R}) = m + 1$). Let $p_0, p_1, \\dots, p_m \\in \\mathcal{P}_m(\\mathbb{R})$ be $m + 1$ polynomials that all share a common root at $x = 2$:
$$p_j(2) = 0 \\quad \\text{for all } j \\in \\{0, 1, \\dots, m\\}$$
Define the evaluation functional $\\phi(p) = p(2)$ and apply the Rank-Nullity Theorem to prove that the list $(p_0, p_1, \\dots, p_m)$ must be linearly dependent.</p>""",
        "solution": """<p><span class="part">Part (a): Subspace Equality Proof</span><br>
Let $n = \\dim U = \\dim V < \\infty$.<br>
Let $(u_1, u_2, \\dots, u_n)$ be a basis of $U$.
1. Because $(u_1, \\dots, u_n)$ is a basis of $U$, it is linearly independent in $U$, and hence linearly independent in $V$.
2. In any finite-dimensional space $V$, any linearly independent list whose length equals $\\dim V$ is automatically a basis of $V$ (Basis Theorem). Thus $(u_1, \\dots, u_n)$ is a basis of $V$.
3. Since $(u_1, \\dots, u_n)$ spans $V$, every $v \\in V$ can be written as $v = c_1 u_1 + \\dots + c_n u_n$.
4. Since each $u_i \\in U$ and $U$ is closed under linear combinations, $v \\in U$.
Thus $V \\subseteq U$. Since $U \\subseteq V$ by definition of subspace:
<span class=\"ans\">$$U = V$$</span></p>

<p><span class="part">Part (b): Polynomial Evaluation Functional & Dependence Proof</span><br>
1. <strong>Define Subspace & Linear Functional:</strong><br>
Consider the subset of polynomials vanishing at $2$:
$$U = \\{ p \\in \\mathcal{P}_m(\\mathbb{R}) : p(2) = 0 \\}$$
Define the linear evaluation functional $\\phi: \\mathcal{P}_m(\\mathbb{R}) \\to \\mathbb{R}$ by:
$$\\phi(p) = p(2)$$
$\\phi$ is linear because $\\phi(\\alpha p + \\beta q) = (\\alpha p + \\beta q)(2) = \\alpha p(2) + \\beta q(2) = \\alpha \\phi(p) + \\beta \\phi(q)$.<br>
2. <strong>Rank-Nullity Theorem:</strong>
- The range of $\\phi$ is a subspace of $\\mathbb{R}$. Since non-zero constant polynomials $p(x) = c \\ne 0$ map to $\\phi(p) = c \\in \\mathbb{R}$, $\\phi$ is surjective onto $\\mathbb{R}$. Thus $\\dim(\\operatorname{range}(\\phi)) = 1$.
- The null space of $\\phi$ is precisely $U$: $\\operatorname{null}(\\phi) = \\{ p : \\phi(p) = 0 \\} = U$.<br>
By the Rank-Nullity Theorem:
$$\\dim \\mathcal{P}_m(\\mathbb{R}) = \\dim(\\operatorname{null}(\\phi)) + \\dim(\\operatorname{range}(\\phi))$$
$$(m + 1) = \\dim U + 1 \\implies <span class=\"ans\">\\dim U = m</span>$$
3. <strong>Linear Dependence Conclusion:</strong><br>
We are given $m + 1$ polynomials $p_0, p_1, \\dots, p_m$. All $m + 1$ polynomials satisfy $p_j(2) = 0$, meaning they all belong to the subspace $U$.<br>
In any vector space, the length of any linearly independent list cannot exceed the dimension of the space.<br>
Since the list $(p_0, \\dots, p_m)$ has length $m + 1$, and $\\dim U = m$:
<span class=\"ans\">$$\\text{Length} = m + 1 > m = \\dim U$$</span>
Therefore, the list $(p_0, p_1, \\dots, p_m)$ cannot be linearly independent. It is strictly <strong>linearly dependent</strong>.</p>""",
        "takeaway": "If a subspace U of a finite-dimensional space V has dim U = dim V, then U = V. The space of polynomials of degree <= m with a root at x = 2 has dimension m; any list of m + 1 such polynomials is automatically linearly dependent."
    }
]

def main():
    with open(PRACTICE_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    if "20191" in content:
        print("Batch 01-02 already present in practice_laa.js!")
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
    for card in PRACTICE_LAA_01_02:
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

    print("Successfully added LAA Batch 01-02 (6 cards). Total in file now updated.")

if __name__ == "__main__":
    main()
