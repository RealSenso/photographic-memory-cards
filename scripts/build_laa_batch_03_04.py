#!/usr/bin/env python3
"""
Builder script for LAA Practice Cards: Batch 02 (Topics 03 & 04)
Topic 03: Linear Maps, Null Space, Range & Matrices (Cards 20391, 20392, 20393)
Topic 04: Invertibility, Isomorphisms & Change of Basis (Cards 20491, 20492, 20493)
"""

import json
import os
import re

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRACTICE_FILE = os.path.join(REPO_DIR, "practice_laa.js")

PRACTICE_LAA_03_04 = [
    # =========================================================================
    # TOPIC 03: Linear Maps, Null Space, Range, and Matrices
    # =========================================================================
    {
        "id": 20391,
        "subject": "LAA",
        "topicId": "03_Linear_Maps_Null_Space_Range_and_Matrices",
        "topicTitle": "03 · Linear Maps, Null Space & Range",
        "title": "Subadditivity of Null Space Dimensions for Composed Linear Maps (IISc Endsem 2023 / Axler 3.B)",
        "kind2": "pyq",
        "source": "IISc Endsem 2023 / Axler Linear Algebra Done Right 3.B",
        "marks": "[8 Marks]",
        "question": """<p>Let $V, W, U$ be finite-dimensional vector spaces. Suppose $T \\in \\mathcal{L}(V, W)$ and $S \\in \\mathcal{L}(W, U)$ are linear transformations.</p>
<p><span class="part">(a)</span> Define the restricted linear map $T_0 = T|_{\\operatorname{null}(ST)}: \\operatorname{null}(ST) \\to W$ and state the Rank-Nullity Theorem applied to $T_0$.</p>
<p><span class="part">(b)</span> Characterize $\\operatorname{null}(T_0)$ and $\\operatorname{range}(T_0)$, and prove the fundamental null-space subadditivity inequality:
$$\\dim \\operatorname{null}(ST) \\le \\dim \\operatorname{null}(S) + \\dim \\operatorname{null}(T)$$</p>
<p><span class="part">(c)</span> Under what condition on $\\operatorname{range}(T)$ does equality hold?</p>""",
        "solution": """<p><span class="part">Part (a): Restricted Operator & Rank-Nullity Setup</span><br>
Consider the restriction of $T$ to the subspace $\\operatorname{null}(ST) \\subseteq V$, denoted:
$$T_0 = T|_{\\operatorname{null}(ST)}: \\operatorname{null}(ST) \\to W$$
Applying the Rank-Nullity Theorem directly to $T_0$:
<span class=\"ans\">$$\\dim \\operatorname{null}(ST) = \\dim \\operatorname{null}(T_0) + \\dim \\operatorname{range}(T_0)$$</span></p>

<p><span class="part">Part (b): Null Space and Range Bounds Proof</span><br>
1. <strong>Characterize $\\operatorname{null}(T_0)$:</strong>
$$v \\in \\operatorname{null}(T_0) \\iff v \\in \\operatorname{null}(ST) \\text{ and } T v = 0$$
Since $T v = 0$ automatically implies $(ST)v = S(0) = 0$, the condition $v \\in \\operatorname{null}(ST)$ is redundant. Thus:
$$\\operatorname{null}(T_0) = \\operatorname{null}(T) \\implies <span class=\"ans\">\\dim \\operatorname{null}(T_0) = \\dim \\operatorname{null}(T)</span>$$
2. <strong>Characterize $\\operatorname{range}(T_0)$:</strong><br>
For any $v \\in \\operatorname{null}(ST)$, by definition $(ST)v = S(T v) = 0$.<br>
Therefore, the output vector $T v$ lies in $\\operatorname{null}(S)$.
$$\\operatorname{range}(T_0) \\subseteq \\operatorname{null}(S) \\implies <span class=\"ans\">\\dim \\operatorname{range}(T_0) \\le \\dim \\operatorname{null}(S)</span>$$
3. <strong>Synthesizing the Bound:</strong><br>
Substituting both terms into the Rank-Nullity expansion from Part (a):
$$\\dim \\operatorname{null}(ST) = \\dim \\operatorname{null}(T) + \\dim \\operatorname{range}(T_0) \\le \\dim \\operatorname{null}(T) + \\dim \\operatorname{null}(S)$$
<span class=\"ans\">$$\\dim \\operatorname{null}(ST) \\le \\dim \\operatorname{null}(S) + \\dim \\operatorname{null}(T)$$</span></p>

<p><span class="part">Part (c): Condition for Equality</span><br>
Equality holds if and only if $\\dim \\operatorname{range}(T_0) = \\dim \\operatorname{null}(S)$, which occurs when $\\operatorname{range}(T_0) = \\operatorname{null}(S)$.<br>
Since $\\operatorname{range}(T_0) = T(\\operatorname{null}(ST)) = \\operatorname{range}(T) \\cap \\operatorname{null}(S)$, equality holds if and only if:
<span class=\"ans\">$$\\operatorname{null}(S) \\subseteq \\operatorname{range}(T)$$</span>
(i.e., every vector in the kernel of $S$ is reachable by $T$).</p>""",
        "takeaway": "The null space dimension of composed operators is subadditive: dim null(ST) <= dim null(S) + dim null(T), proved by applying Rank-Nullity to the restriction of T on null(ST)."
    },
    {
        "id": 20392,
        "subject": "LAA",
        "topicId": "03_Linear_Maps_Null_Space_Range_and_Matrices",
        "topicTitle": "03 · Linear Maps, Null Space & Range",
        "title": "Sylvester's Rank Inequality Derivation via Range Restrictions (MIT 18.06 / Stanford EE263)",
        "kind2": "pyq",
        "source": "MIT 18.06 Linear Algebra / Stanford EE263 Introduction to Linear Dynamical Systems",
        "marks": "[8 Marks]",
        "question": """<p>Let $A \\in \\mathbb{R}^{m \\times n}$ and $B \\in \\mathbb{R}^{n \\times p}$ be real matrices representing linear transformations.</p>
<p><span class="part">(a)</span> State the Rank-Nullity Theorem for matrix $A$ in terms of its columns $n$, $\\operatorname{rank}(A)$, and $\\dim \\operatorname{null}(A)$.</p>
<p><span class="part">(b)</span> Restrict the linear map $x \\mapsto Ax$ to the subspace $\\operatorname{range}(B) \\subseteq \\mathbb{R}^n$, and use the dimension theorem to derive <strong>Sylvester's Rank Inequality</strong>:
$$\\operatorname{rank}(AB) \\ge \\operatorname{rank}(A) + \\operatorname{rank}(B) - n$$</p>
<p><span class="part">(c)</span> For $A \\in \\mathbb{R}^{4 \\times 5}$ of rank 4 and $B \\in \\mathbb{R}^{5 \\times 4}$ of rank 4, determine the exact bounds on $\\operatorname{rank}(AB)$.</p>""",
        "solution": """<p><span class="part">Part (a): Rank-Nullity Theorem</span><br>
For $A \\in \\mathbb{R}^{m \\times n}$, the domain is $\\mathbb{R}^n$:
<span class=\"ans\">$$\\operatorname{rank}(A) + \\dim \\operatorname{null}(A) = n \\implies \\dim \\operatorname{null}(A) = n - \\operatorname{rank}(A)$$</span></p>

<p><span class="part">Part (b): Derivation of Sylvester's Rank Inequality</span><br>
Define the linear map $T_A: \\mathbb{R}^n \\to \\mathbb{R}^m$ given by $T_A(x) = Ax$.<br>
Restrict $T_A$ to the subspace $V_B = \\operatorname{range}(B) \\subseteq \\mathbb{R}^n$:
$$T_A|_{V_B}: \\operatorname{range}(B) \\to \\mathbb{R}^m$$
Applying Rank-Nullity to this restricted operator:
$$\\dim(\\operatorname{range}(B)) = \\dim(\\operatorname{range}(T_A|_{V_B})) + \\dim(\\operatorname{null}(T_A|_{V_B}))$$
Identify each term:
1. $\\dim(\\operatorname{range}(B)) = \\operatorname{rank}(B)$.
2. $\\operatorname{range}(T_A|_{V_B}) = \\{ A(By) : y \\in \\mathbb{R}^p \\} = \\operatorname{range}(AB) \\implies \\dim(\\operatorname{range}(T_A|_{V_B})) = \\operatorname{rank}(AB)$.
3. $\\operatorname{null}(T_A|_{V_B}) = \\{ x \\in \\operatorname{range}(B) : Ax = 0 \\} = \\operatorname{range}(B) \\cap \\operatorname{null}(A) \\subseteq \\operatorname{null}(A)$.<br>
Therefore:
$$\\dim(\\operatorname{null}(T_A|_{V_B})) \\le \\dim(\\operatorname{null}(A)) = n - \\operatorname{rank}(A)$$
Substitute this inequality into the dimension equation:
$$\\operatorname{rank}(B) \\le \\operatorname{rank}(AB) + (n - \\operatorname{rank}(A))$$
Rearranging gives Sylvester's Rank Inequality:
<span class=\"ans\">$$\\operatorname{rank}(AB) \\ge \\operatorname{rank}(A) + \\operatorname{rank}(B) - n$$</span></p>

<p><span class="part">Part (c): Numerical Evaluation</span><br>
Given $A \\in \\mathbb{R}^{4 \\times 5}$ with $\\operatorname{rank}(A) = 4$, $B \\in \\mathbb{R}^{5 \\times 4}$ with $\\operatorname{rank}(B) = 4$, and inner dimension $n = 5$:<br>
1. <strong>Lower bound from Sylvester's Inequality:</strong>
$$\\operatorname{rank}(AB) \\ge \\operatorname{rank}(A) + \\operatorname{rank}(B) - n = 4 + 4 - 5 = <span class=\"ans\">3</span>$$
2. <strong>Upper bound from sub-multiplicativity:</strong>
$$\\operatorname{rank}(AB) \\le \\min(\\operatorname{rank}(A), \\operatorname{rank}(B)) = \\min(4, 4) = <span class=\"ans\">4</span>$$
The product matrix $AB \\in \\mathbb{R}^{4 \\times 4}$ must have:
<span class=\"ans\">$$3 \\le \\operatorname{rank}(AB) \\le 4$$</span></p>""",
        "takeaway": "Sylvester's rank inequality rank(AB) >= rank(A) + rank(B) - n provides a sharp lower bound on matrix product rank, derived by restricting the linear map of A to the range of B."
    },
    {
        "id": 20393,
        "subject": "LAA",
        "topicId": "03_Linear_Maps_Null_Space_Range_and_Matrices",
        "topicTitle": "03 · Linear Maps, Null Space & Range",
        "title": "Idempotent Projection Direct Sum Decomposition & Injectivity Dimension Bottleneck (Generated IISc / Princeton MAT 217)",
        "kind2": "generated",
        "source": "Generated IISc Midterm / Princeton MAT 217 & Axler Linear Algebra Done Right 3.23",
        "marks": "[8 Marks]",
        "question": """<p><span class="part">(a)</span> A linear operator $P \\in \\mathcal{L}(V)$ is called a <strong>projection</strong> (or idempotent) if $P^2 = P$. Prove rigorously that:
$$V = \\operatorname{null}(P) \\oplus \\operatorname{range}(P)$$</p>
<p><span class="part">(b)</span> Let $V$ and $W$ be finite-dimensional vector spaces with $\\dim V > \\dim W$. Prove using the Rank-Nullity Theorem that no linear map $T \\in \\mathcal{L}(V, W)$ can be injective.</p>
<p><span class="part">(c)</span> Dually, if $\\dim V < \\dim W$, prove that no linear map $T \\in \\mathcal{L}(V, W)$ can be surjective.</p>""",
        "solution": """<p><span class="part">Part (a): Idempotent Projection Direct Sum Decomposition</span><br>
1. <strong>Spanning: $V = \\operatorname{null}(P) + \\operatorname{range}(P)$:</strong><br>
For any arbitrary vector $v \\in V$, express it identically as:
<span class=\"ans\">$$v = (v - Pv) + Pv$$</span>
- Check first term: $P(v - Pv) = Pv - P^2 v = Pv - Pv = 0 \\implies (v - Pv) \\in \\operatorname{null}(P)$.<br>
- Check second term: By definition, $Pv \\in \\operatorname{range}(P)$.<br>
Since every $v \\in V$ is the sum of a vector in $\\operatorname{null}(P)$ and a vector in $\\operatorname{range}(P)$, $V = \\operatorname{null}(P) + \\operatorname{range}(P)$.<br>
2. <strong>Trivial Intersection: $\\operatorname{null}(P) \\cap \\operatorname{range}(P) = \\{0\\}$:</strong><br>
Let $u \\in \\operatorname{null}(P) \\cap \\operatorname{range}(P)$.
- Since $u \\in \\operatorname{null}(P)$, $Pu = 0$.
- Since $u \\in \\operatorname{range}(P)$, there exists some $w \\in V$ such that $u = Pw$.<br>
Applying $P$ to $u$:
$$Pu = P(Pw) = P^2 w = Pw = u$$
Equating both expressions for $Pu$:
$$0 = u \\implies <span class=\"ans\">u = 0</span>$$
Thus $\\operatorname{null}(P) \\cap \\operatorname{range}(P) = \\{0\\}$.<br>
Combining both results proves <span class=\"ans\">$V = \\operatorname{null}(P) \\oplus \\operatorname{range}(P)$</span>.</p>

<p><span class="part">Part (b): Injectivity Dimension Bottleneck</span><br>
Let $T \\in \\mathcal{L}(V, W)$ with $\\dim V > \\dim W$.<br>
By the Rank-Nullity Theorem:
$$\\dim V = \\dim \\operatorname{null}(T) + \\dim \\operatorname{range}(T)$$
Since $\\operatorname{range}(T) \\subseteq W$, we have $\\dim \\operatorname{range}(T) \\le \\dim W$.
$$\\dim \\operatorname{null}(T) = \\dim V - \\dim \\operatorname{range}(T) \\ge \\dim V - \\dim W$$
Since $\\dim V > \\dim W$, we have $\\dim V - \\dim W \\ge 1$, which implies:
<span class=\"ans\">$$\\dim \\operatorname{null}(T) \\ge 1 > 0 \\implies \\operatorname{null}(T) \\ne \\{0\\}$$</span>
A linear map is injective if and only if its null space contains only the zero vector. Since $\\operatorname{null}(T)$ contains non-zero vectors, <span class=\"ans\">$T$ cannot be injective</span>.</p>

<p><span class="part">Part (c): Surjectivity Dimension Bottleneck</span><br>
Let $T \\in \\mathcal{L}(V, W)$ with $\\dim V < \\dim W$.<br>
By the Rank-Nullity Theorem:
$$\\dim \\operatorname{range}(T) = \\dim V - \\dim \\operatorname{null}(T) \\le \\dim V$$
Since $\\dim V < \\dim W$:
<span class=\"ans\">$$\\dim \\operatorname{range}(T) \\le \\dim V < \\dim W$$</span>
A linear map is surjective if and only if $\\dim \\operatorname{range}(T) = \\dim W$. Because $\\dim \\operatorname{range}(T)$ is strictly bounded below $\\dim W$, $\\operatorname{range}(T)$ cannot equal $W$. Thus <span class=\"ans\">$T$ cannot be surjective</span>.</p>""",
        "takeaway": "An idempotent projection operator P^2 = P always induces the direct sum decomposition V = null(P) ⊕ range(P). If dim V > dim W, no linear map can be injective; if dim V < dim W, no linear map can be surjective."
    },

    # =========================================================================
    # TOPIC 04: Invertibility, Isomorphisms, and Change of Basis
    # =========================================================================
    {
        "id": 20491,
        "subject": "LAA",
        "topicId": "04_Invertibility_Isomorphisms_and_Change_of_Basis",
        "topicTitle": "04 · Invertibility & Change of Basis",
        "title": "One-Sided vs. Two-Sided Inverses in Finite Dimensions (IISc Midterm 1 / Axler 3.D)",
        "kind2": "pyq",
        "source": "IISc Midterm 1 / Axler Linear Algebra Done Right 3.D",
        "marks": "[8 Marks]",
        "question": """<p>Let $V$ be a finite-dimensional vector space over field $\\mathbb{F}$, and let $S, T \\in \\mathcal{L}(V)$ be linear operators.</p>
<p><span class="part">(a)</span> Prove that $ST = I$ if and only if $TS = I$.</p>
<p><span class="part">(b)</span> Explain why this equivalence relies fundamentally on the finite dimensionality of $V$, and provide a standard counterexample on the infinite-dimensional sequence space $\\ell^2$ (or polynomial space $\\mathcal{P}(\\mathbb{R})$) where $ST = I$ but $TS \\ne I$.</p>
<p><span class="part">(c)</span> State the four fundamental matrix invertibility equivalences for a square matrix $A \\in \\mathbb{R}^{n \\times n}$.</p>""",
        "solution": """<p><span class="part">Part (a): Proof that $ST = I \\iff TS = I$ in Finite Dimensions</span><br>
$(\\implies)$ Suppose $ST = I$.<br>
1. <strong>Show $T$ is injective:</strong><br>
Suppose $Tv = 0$ for some $v \\in V$. Applying $S$ to both sides:
$$S(Tv) = S(0) = 0$$
Since $ST = I$, the left side is $(ST)v = Iv = v$. Thus $v = 0$.<br>
Therefore $\\operatorname{null}(T) = \\{0\\}$, proving $T$ is <strong>injective</strong>.<br>
2. <strong>Injective $\\implies$ Invertible in Finite Dimensions:</strong><br>
By the Rank-Nullity Theorem: $\\dim V = \\dim \\operatorname{null}(T) + \\dim \\operatorname{range}(T) = 0 + \\dim \\operatorname{range}(T) = \\dim \\operatorname{range}(T)$.<br>
Since $\\operatorname{range}(T) \\subseteq V$ and has equal dimension, $\\operatorname{range}(T) = V$, so $T$ is surjective.<br>
Being injective and surjective, $T$ is invertible with two-sided inverse $T^{-1}$.<br>
3. <strong>Multiply by $T^{-1}$:</strong>
$$(ST) T^{-1} = I T^{-1} \\implies S(T T^{-1}) = T^{-1} \\implies S = T^{-1}$$
Therefore:
<span class=\"ans\">$$TS = T T^{-1} = I$$</span>
$(\\impliedby)$ The reverse direction is identical by swapping the roles of $S$ and $T$.</p>

<p><span class="part">Part (b): Infinite-Dimensional Counterexample</span><br>
On infinite-dimensional spaces, injectivity does NOT imply surjectivity.<br>
<strong>Counterexample on sequence space $\\ell^2$:</strong><br>
Let $T$ be the right shift operator: $T(x_1, x_2, x_3, \\dots) = (0, x_1, x_2, x_3, \\dots)$.<br>
Let $S$ be the left shift operator: $S(y_1, y_2, y_3, \\dots) = (y_2, y_3, y_4, \\dots)$.<br>
- <strong>Compute $ST$:</strong>
$$ST(x_1, x_2, \\dots) = S(0, x_1, x_2, \\dots) = (x_1, x_2, \\dots) = I$$
So $ST = I$ (left inverse exists).<br>
- <strong>Compute $TS$:</strong>
$$TS(y_1, y_2, \\dots) = T(y_2, y_3, \\dots) = (0, y_2, y_3, \\dots) \\ne (y_1, y_2, y_3, \\dots)$$
<span class=\"ans\">$TS \\ne I$</span> because the first component $y_1$ is erased and set to 0. Thus $T$ has a left inverse but is NOT invertible.</p>

<p><span class="part">Part (c): Invertibility Equivalences for Square Matrix $A \\in \\mathbb{R}^{n \\times n}$</span><br>
The following are mathematically equivalent:
1. $A$ is invertible (has two-sided inverse $A^{-1}$).
2. $\\operatorname{null}(A) = \\{0\\}$ (the columns of $A$ are linearly independent).
3. $\\operatorname{range}(A) = \\mathbb{R}^n$ (the columns of $A$ span $\\mathbb{R}^n$).
4. $\\det(A) \\ne 0$ (all eigenvalues $\\lambda_i \\ne 0$).</p>""",
        "takeaway": "For operators on finite-dimensional spaces, a one-sided inverse is automatically a two-sided inverse (ST = I <=> TS = I). In infinite-dimensional spaces, this fails (e.g. shift operators on sequences where left-shift o right-shift = I, but right-shift o left-shift != I)."
    },
    {
        "id": 20492,
        "subject": "LAA",
        "topicId": "04_Invertibility_Isomorphisms_and_Change_of_Basis",
        "topicTitle": "04 · Invertibility & Change of Basis",
        "title": "Coordinate Transformation & Change-of-Basis Matrix Inversion (Stanford EE263 / Meyer 3.4)",
        "kind2": "pyq",
        "source": "Stanford EE263 Introduction to Linear Dynamical Systems / Meyer Matrix Analysis 3.4",
        "marks": "[8 Marks]",
        "question": """<p>Consider two ordered bases of $\\mathbb{R}^2$:
$$B_1 = \\left\\{ v_1 = \\begin{pmatrix} 1 \\\\ 1 \\end{pmatrix}, \\; v_2 = \\begin{pmatrix} 1 \\\\ -1 \\end{pmatrix} \\right\\}, \\qquad B_2 = \\left\\{ u_1 = \\begin{pmatrix} 1 \\\\ 2 \\end{pmatrix}, \\; u_2 = \\begin{pmatrix} 3 \\\\ 4 \\end{pmatrix} \\right\\}$$</p>
<p><span class="part">(a)</span> Define the basis matrices $V_B = [v_1, v_2]$ and $U = [u_1, u_2]$, and write the relationship between coordinate vectors $[x]_{B_1}$ and $[x]_{B_2}$ for an arbitrary vector $x \\in \\mathbb{R}^2$.</p>
<p><span class="part">(b)</span> Compute the matrix inverse $U^{-1}$ explicitly.</p>
<p><span class="part">(c)</span> Compute the transition matrix $P$ such that $[x]_{B_2} = P [x]_{B_1}$, and find the coordinates of vector $x = \\begin{pmatrix} 4 \\\\ 2 \\end{pmatrix}$ with respect to both bases.</p>""",
        "solution": """<p><span class="part">Part (a): Basis Matrix Coordinate Formulation</span><br>
Assemble basis vectors into column matrices:
$$V_B = \\begin{pmatrix} 1 & 1 \\\\ 1 & -1 \\end{pmatrix}, \\qquad U = \\begin{pmatrix} 1 & 3 \\\\ 2 & 4 \\end{pmatrix}$$
Any vector $x \\in \\mathbb{R}^2$ expands as:
$$x = V_B [x]_{B_1} = U [x]_{B_2}$$
Multiplying on the left by $U^{-1}$:
<span class=\"ans\">$$[x]_{B_2} = U^{-1} V_B [x]_{B_1} = P [x]_{B_1} \\quad \\text{where } P = U^{-1} V_B$$</span></p>

<p><span class="part">Part (b): Explicit Matrix Inverse $U^{-1}$</span><br>
Determinant of $U$:
$$\\det(U) = (1)(4) - (3)(2) = 4 - 6 = -2$$
Using the $2 \\times 2$ matrix inverse formula $\\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix}^{-1} = \\frac{1}{ad-bc} \\begin{pmatrix} d & -b \\\\ -c & a \\end{pmatrix}$:
<span class=\"ans\">$$U^{-1} = -\\frac{1}{2} \\begin{pmatrix} 4 & -3 \\\\ -2 & 1 \\end{pmatrix} = \\begin{pmatrix} -2 & 3/2 \\\\ 1 & -1/2 \\end{pmatrix}$$</span></p>

<p><span class="part">Part (c): Transition Matrix $P$ and Coordinate Evaluation</span><br>
Compute $P = U^{-1} V_B$:
$$P = \\begin{pmatrix} -2 & 3/2 \\\\ 1 & -1/2 \\end{pmatrix} \\begin{pmatrix} 1 & 1 \\\\ 1 & -1 \\end{pmatrix} = \\begin{pmatrix} -2(1) + \\frac{3}{2}(1) & -2(1) + \\frac{3}{2}(-1) \\\\ 1(1) - \\frac{1}{2}(1) & 1(1) - \\frac{1}{2}(-1) \\end{pmatrix}$$
<span class=\"ans\">$$P = \\begin{pmatrix} -1/2 & -7/2 \\\\ 1/2 & 3/2 \\end{pmatrix}$$</span>
<strong>Evaluating coordinates for $x = \\begin{pmatrix} 4 \\\\ 2 \\end{pmatrix}$:</strong><br>
1. With respect to $B_1$:
$$V_B [x]_{B_1} = \\begin{pmatrix} 4 \\\\ 2 \\end{pmatrix} \\implies \\begin{pmatrix} c_1 + c_2 \\\\ c_1 - c_2 \\end{pmatrix} = \\begin{pmatrix} 4 \\\\ 2 \\end{pmatrix} \\implies 2c_1 = 6 \\implies c_1 = 3, c_2 = 1$$
<span class=\"ans\">$$[x]_{B_1} = \\begin{pmatrix} 3 \\\\ 1 \\end{pmatrix}$$</span>
2. With respect to $B_2$ via transition matrix $P$:
$$[x]_{B_2} = P [x]_{B_1} = \\begin{pmatrix} -1/2 & -7/2 \\\\ 1/2 & 3/2 \\end{pmatrix} \\begin{pmatrix} 3 \\\\ 1 \\end{pmatrix} = \\begin{pmatrix} -3/2 - 7/2 \\\\ 3/2 + 3/2 \\end{pmatrix} = <span class=\"ans\">\\begin{pmatrix} -5 \\\\ 3 \\end{pmatrix}</span>$$
<em>Verification:</em> $-5 u_1 + 3 u_2 = -5 \\begin{pmatrix} 1 \\\\ 2 \\end{pmatrix} + 3 \\begin{pmatrix} 3 \\\\ 4 \\end{pmatrix} = \\begin{pmatrix} -5 + 9 \\\\ -10 + 12 \\end{pmatrix} = \\begin{pmatrix} 4 \\\\ 2 \\end{pmatrix} = x$. Perfect match.</p>""",
        "takeaway": "Change of basis from B1 to B2 follows [x]_B2 = P [x]_B1 where P = U^(-1) V_B. The columns of P are the coordinates of the old basis vectors expanded in the new basis."
    },
    {
        "id": 20493,
        "subject": "LAA",
        "topicId": "04_Invertibility_Isomorphisms_and_Change_of_Basis",
        "topicTitle": "04 · Invertibility & Change of Basis",
        "title": "Subspace Annihilator Operator Dimensions & All-Ones Spectrum (Generated IISc / IIT Kanpur & MIT 18.06)",
        "kind2": "generated",
        "source": "Generated IISc Midterm / IIT Kanpur & MIT 18.06 (Axler 3.E & 3.60)",
        "marks": "[8 Marks]",
        "question": """<p><span class="part">(a)</span> Let $V$ and $W$ be finite-dimensional vector spaces, and let $E$ be a subspace of $V$. Define the set of linear maps that annihilate $E$:
$$U = \\{ T \\in \\mathcal{L}(V, W) : Te = 0 \\quad \\text{for all } e \\in E \\}$$
Prove that $U$ is a subspace of $\\mathcal{L}(V, W)$, and derive its exact dimension in terms of $\\dim V$, $\\dim E$, and $\\dim W$.</p>
<p><span class="part">(b)</span> Let $A = \\mathbf{1}\\mathbf{1}^\\top \\in \\mathbb{R}^{n \\times n}$ ($n \\ge 2$) be the rank-1 matrix with every entry equal to 1.
(i) Determine the rank and nullity of $A$, and prove whether $A$ is invertible.
(ii) Find all eigenvalues of $A$ along with their algebraic and geometric multiplicities.</p>""",
        "solution": """<p><span class="part">Part (a): Subspace Annihilator Proof & Dimension</span><br>
1. <strong>Subspace Verification:</strong>
- <em>Zero element:</em> The zero map $0 \\in \\mathcal{L}(V, W)$ satisfies $0(e) = 0$ for all $e \\in E$, so $0 \\in U$.
- <em>Closure:</em> If $S, T \\in U$ and $\\alpha, \\beta \\in \\mathbb{F}$, then for any $e \\in E$:
$$(\\alpha S + \\beta T)(e) = \\alpha S(e) + \\beta T(e) = \\alpha(0) + \\beta(0) = 0 \\implies (\\alpha S + \\beta T) \\in U$$
Thus $U$ is a valid subspace of $\\mathcal{L}(V, W)$.<br>
2. <strong>Dimension Derivation:</strong><br>
Let $n = \\dim V, k = \\dim E$, and $m = \\dim W$.<br>
Choose a basis $(e_1, \\dots, e_k)$ for $E$, and extend it to a basis $(e_1, \\dots, e_k, v_{k+1}, \\dots, v_n)$ for $V$.<br>
A linear map $T \\in \\mathcal{L}(V, W)$ is uniquely and freely determined by specifying its values on a basis of $V$:
- For $T \\in U$, we must have $Te_1 = 0, \\dots, Te_k = 0$. These $k$ vector images are strictly fixed to zero (0 degrees of freedom).
- The remaining $n - k$ basis vectors $v_{k+1}, \\dots, v_n$ can be mapped to <em>arbitrary, independent vectors</em> in $W$.
For each of the $n - k$ basis vectors, there are $\\dim W = m$ degrees of freedom.<br>
Therefore:
<span class=\"ans\">$$\\dim U = (n - k) \\cdot m = (\\dim V - \\dim E) \\dim W$$</span>
(Note: $U$ is canonically isomorphic to $\\mathcal{L}(V/E, W)$).</p>

<p><span class="part">Part (b): All-Ones Matrix Spectrum & Invertibility</span><br>
Matrix $A = \\mathbf{1}\\mathbf{1}^\\top = \\begin{pmatrix} 1 & 1 & \\dots & 1 \\\\ \\vdots & \\vdots & \\ddots & \\vdots \\\\ 1 & 1 & \\dots & 1 \\end{pmatrix} \\in \\mathbb{R}^{n \\times n}$ ($n \\ge 2$).<br>
1. <strong>Rank and Invertibility:</strong>
- Every column of $A$ is identical to $\\mathbf{1} = [1, 1, \\dots, 1]^\\top$. Thus $\\operatorname{range}(A) = \\operatorname{span}(\\mathbf{1})$, so $\\operatorname{rank}(A) = 1$.
- By Rank-Nullity: $\\dim \\operatorname{null}(A) = n - \\operatorname{rank}(A) = n - 1$.
- Since $n \\ge 2$, $\\dim \\operatorname{null}(A) = n - 1 \\ge 1$. $A$ has a non-trivial kernel ($\det(A) = 0$).<br>
<span class=\"ans\">$A$ is NOT invertible.</span><br>
2. <strong>Eigenvalues & Multiplicities:</strong>
- <em>Eigenvalue $\\lambda = 0$:</em> The null space $\\operatorname{null}(A)$ has dimension $n - 1$. Thus $\\lambda = 0$ is an eigenvalue with geometric multiplicity $n - 1$ and algebraic multiplicity $n - 1$.
- <em>Eigenvalue $\\lambda = n$:</em> Multiply $A$ by the vector $\\mathbf{1}$:
$$A \\mathbf{1} = (\\mathbf{1}\\mathbf{1}^\\top)\\mathbf{1} = \\mathbf{1}(\\mathbf{1}^\\top \\mathbf{1}) = \\mathbf{1}(n) = n \\mathbf{1}$$
Thus $\\lambda = n$ is an eigenvalue with eigenvector $\\mathbf{1}$.<br>
Trace check: $\\operatorname{Tr}(A) = \\sum_{i=1}^n 1 = n = (n - 1)(0) + 1(n)$. Matches trace identically.<br>
<span class=\"ans\">Eigenvalues: $\\lambda = 0$ (multiplicity $n-1$) and $\\lambda = n$ (multiplicity 1).</span></p>""",
        "takeaway": "Linear maps annihilating subspace E have dimension (dim V - dim E) dim W. The all-ones matrix A = 1 1^T has rank 1, nullity n-1, eigenvalues 0 (multiplicity n-1) and n (multiplicity 1), and is non-invertible for n >= 2."
    }
]

def main():
    with open(PRACTICE_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    if "20391" in content:
        print("Batch 03-04 already present in practice_laa.js!")
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
    for card in PRACTICE_LAA_03_04:
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

    print("Successfully added LAA Batch 03-04 (6 cards). Total in file now updated.")

if __name__ == "__main__":
    main()
