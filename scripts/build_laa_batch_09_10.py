#!/usr/bin/env python3
"""
Builder script for LAA Practice Cards: Batch 05 (Topics 09 & 10)
Topic 09: Jordan Canonical Form & Matrix Functions (Cards 20991, 20992, 20993)
Topic 10: Inner Product Spaces, Norms & Orthogonality (Cards 21091, 21092, 21093)
"""

import json
import os
import re

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRACTICE_FILE = os.path.join(REPO_DIR, "practice_laa.js")

PRACTICE_LAA_09_10 = [
    # =========================================================================
    # TOPIC 09: Jordan Canonical Form and Matrix Functions
    # =========================================================================
    {
        "id": 20991,
        "subject": "LAA",
        "topicId": "09_Jordan_Canonical_Form_and_Matrix_Functions",
        "topicTitle": "09 · Jordan Form & Matrix Functions",
        "title": "Jordan Block Matrix Exponential & Dynamical Flow (IISc Endsem 2024 / Meyer 7.8)",
        "kind2": "pyq",
        "source": "IISc Endsem 2024 / Meyer Matrix Analysis and Applied Linear Algebra 7.8",
        "marks": "[6 Marks]",
        "question": """<p>Consider the defective $2 \\times 2$ matrix:
$$A = \\begin{pmatrix} 2 & 1 \\\\ 0 & 2 \\end{pmatrix}$$</p>
<p><span class="part">(a)</span> Identify the Jordan Canonical Form $J$ and the similarity transformation matrix $P$ such that $A = P J P^{-1}$.</p>
<p><span class="part">(b)</span> Decompose $A = \\lambda I + N$ into a scalar multiple of identity and a nilpotent matrix $N$, and prove that $(\\lambda I)$ and $N$ commute.</p>
<p><span class="part">(c)</span> Use the matrix power series to derive the closed-form matrix exponential $e^{At}$.</p>""",
        "solution": """<p><span class="part">Part (a): Jordan Canonical Form</span><br>
The matrix $A$ is an upper triangular matrix with repeated diagonal entries $\\lambda = 2$ and a superdiagonal $1$:
$$A = \\begin{pmatrix} 2 & 1 \\\\ 0 & 2 \\end{pmatrix}$$
This is already in standard Jordan Canonical Form as a single Jordan block of size 2:
<span class=\"ans\">$$J = J_2(2) = \\begin{pmatrix} 2 & 1 \\\\ 0 & 2 \\end{pmatrix}, \\qquad P = I_2 = \\begin{pmatrix} 1 & 0 \\\\ 0 & 1 \\end{pmatrix}$$</span></p>

<p><span class="part">Part (b): Commuting Nilpotent Decomposition</span><br>
Split $A = 2I + N$ where:
$$N = A - 2I = \\begin{pmatrix} 0 & 1 \\\\ 0 & 0 \\end{pmatrix}$$
Notice that:
$$N^2 = \\begin{pmatrix} 0 & 1 \\\\ 0 & 0 \\end{pmatrix} \\begin{pmatrix} 0 & 1 \\\\ 0 & 0 \\end{pmatrix} = \\begin{pmatrix} 0 & 0 \\\\ 0 & 0 \\end{pmatrix} = 0$$
Thus $N$ is nilpotent of order 2 ($N^2 = 0$).<br>
Since the identity matrix $I$ commutes with every matrix:
$$(2I)N = 2(IN) = 2N = 2(NI) = N(2I)$$
Because $2I$ and $N$ commute, the matrix exponential property $e^{(X+Y)t} = e^{Xt} e^{Yt}$ holds strictly.</p>

<p><span class="part">Part (c): Closed-Form Evaluation of $e^{At}$</span><br>
Using the commutativity from Part (b):
$$e^{At} = e^{(2I + N)t} = e^{2t I} e^{Nt} = (e^{2t} I) e^{Nt}$$
Expand the power series of $e^{Nt}$:
$$e^{Nt} = I + Nt + \\frac{N^2 t^2}{2!} + \\dots$$
Since $N^2 = 0$, all terms of degree $\\ge 2$ vanish identically:
<span class=\"ans\">$$e^{Nt} = I + Nt = \\begin{pmatrix} 1 & 0 \\\\ 0 & 1 \\end{pmatrix} + \\begin{pmatrix} 0 & t \\\\ 0 & 0 \\end{pmatrix} = \\begin{pmatrix} 1 & t \\\\ 0 & 1 \\end{pmatrix}$$</span>
Multiplying by scalar $e^{2t}$:
<span class=\"ans\">$$e^{At} = e^{2t} \\begin{pmatrix} 1 & t \\\\ 0 & 1 \\end{pmatrix} = \\begin{pmatrix} e^{2t} & t e^{2t} \\\\ 0 & e^{2t} \\end{pmatrix}$$</span>
Notice the secular term $t e^{2t}$ that arises on the off-diagonal due to defective Jordan structure.</p>""",
        "takeaway": "For a Jordan block J = lambda I + N, powers of N truncate the Taylor series of any analytic function: e^(Jt) = e^(lambda t) (I + Nt) for size 2. Defective eigenvalues produce secular polynomial terms t^k e^(lambda t) in dynamical systems."
    },
    {
        "id": 20992,
        "subject": "LAA",
        "topicId": "09_Jordan_Canonical_Form_and_Matrix_Functions",
        "topicTitle": "09 · Jordan Form & Matrix Functions",
        "title": "Jordan Structure Reconstruction from Invariant Polynomials & Nullity (MIT 18.06 / Strang L28)",
        "kind2": "pyq",
        "source": "MIT 18.06 Linear Algebra / Strang Lecture 28",
        "marks": "[8 Marks]",
        "question": """<p>A $5 \\times 5$ real matrix $A$ has:
<ul>
  <li>Characteristic polynomial: $p_{\\text{char}}(\\lambda) = (\\lambda - 4)^5$</li>
  <li>Minimal polynomial: $p_{\\text{min}}(\\lambda) = (\\lambda - 4)^3$</li>
  <li>Geometric multiplicity: $\\dim \\operatorname{null}(A - 4I) = 2$</li>
</ul></p>
<p><span class="part">(a)</span> State the algebraic meanings of the powers and dimensions: what do the degree of the characteristic polynomial, the degree of the minimal polynomial, and $\\dim \\operatorname{null}(A - \\lambda I)$ signify about the Jordan blocks?</p>
<p><span class="part">(b)</span> Set up the integer partition problem for the block sizes and determine the unique Jordan block partition of $A$.</p>
<p><span class="part">(c)</span> Write the explicit Jordan Canonical Form matrix $J$.</p>""",
        "solution": """<p><span class="part">Part (a): Invariant Principles of Jordan Structure</span><br>
For a matrix with single eigenvalue $\\lambda$:
1. <strong>Sum of block sizes:</strong> The sum of the sizes of all Jordan blocks equals the algebraic multiplicity (power in characteristic polynomial):
$$\\sum k_i = 5$$
2. <strong>Total number of blocks:</strong> The number of Jordan blocks equals the geometric multiplicity (dimension of eigenspace):
$$\\text{Number of blocks} = \\dim \\operatorname{null}(A - 4I) = 2$$
3. <strong>Size of the largest block:</strong> The size of the largest Jordan block equals the multiplicity of $\\lambda$ in the minimal polynomial:
$$\\max_i(k_i) = 3$$</p>

<p><span class="part">Part (b): Integer Partition Problem</span><br>
We seek a partition of $5$ into exactly $2$ positive integers $(k_1, k_2)$ with maximum equal to $3$:
$$k_1 + k_2 = 5, \\qquad k_1 \\ge k_2 \\ge 1, \\qquad k_1 = 3$$
Substitute $k_1 = 3$:
$$3 + k_2 = 5 \\implies <span class=\"ans\">k_2 = 2</span>$$
The partition is uniquely determined as:
<span class=\"ans\">$$\\{3, \\; 2\\}$$</span>
This corresponds to one Jordan block of size 3 and one Jordan block of size 2.</p>

<p><span class="part">Part (c): Explicit Jordan Canonical Form $J$</span><br>
The Jordan Canonical Form is the block diagonal matrix:
<span class=\"ans\">$$J = \\begin{pmatrix} J_3(4) & 0 \\\\ 0 & J_2(4) \\end{pmatrix} = \\begin{pmatrix} 4 & 1 & 0 & 0 & 0 \\\\ 0 & 4 & 1 & 0 & 0 \\\\ 0 & 0 & 4 & 0 & 0 \\\\ 0 & 0 & 0 & 4 & 1 \\\\ 0 & 0 & 0 & 0 & 4 \\end{pmatrix}$$</span>
Every other property matches:
- $\\operatorname{rank}(J - 4I) = 5 - 2 = 3$ (geometric multiplicity 2).
- $(J - 4I)^3 = 0$ while $(J - 4I)^2 \\ne 0$ (minimal polynomial $(z - 4)^3$).</p>""",
        "takeaway": "The Jordan form of a matrix is uniquely determined by three algebraic invariants: algebraic multiplicity (sum of block sizes), geometric multiplicity (total number of blocks), and minimal polynomial exponent (size of largest block)."
    },
    {
        "id": 20993,
        "subject": "LAA",
        "topicId": "09_Jordan_Canonical_Form_and_Matrix_Functions",
        "topicTitle": "09 · Jordan Form & Matrix Functions",
        "title": "Matrix Taylor Formula on Jordan Blocks & Linear ODE Systems (Generated IISc / Stanford EE263 & IIT Kanpur)",
        "kind2": "generated",
        "source": "Generated IISc Midterm / Stanford EE263 (Boyd) & Meyer Matrix Analysis 7.9",
        "marks": "[8 Marks]",
        "question": """<p><span class="part">(a)</span> Solve the vector initial value problem $\\dot{x}(t) = A x(t)$ with initial state $x(0) = \\begin{pmatrix} 1 \\\\ 2 \\end{pmatrix}$, where:
$$A = \\begin{pmatrix} 1 & 1 \\\\ 0 & 1 \\end{pmatrix}$$</p>
<p><span class="part">(b)</span> For an arbitrary analytic scalar function $f(z)$ and a $2 \\times 2$ Jordan block $J = \\begin{pmatrix} \\lambda & 1 \\\\ 0 & \\lambda \\end{pmatrix}$, prove the <strong>Matrix Taylor Formula</strong>:
$$f(J) = \\begin{pmatrix} f(\\lambda) & f'(\\lambda) \\\\ 0 & f(\\lambda) \\end{pmatrix}$$</p>
<p><span class="part">(c)</span> Apply this formula to compute $J^{50}$ for $J = \\begin{pmatrix} 2 & 1 \\\\ 0 & 2 \\end{pmatrix}$.</p>""",
        "solution": """<p><span class="part">Part (a): Solving Linear ODE via Matrix Exponential</span><br>
The exact analytical solution is $x(t) = e^{At} x(0)$.<br>
Write $A = I + N$ where $N = \\begin{pmatrix} 0 & 1 \\\\ 0 & 0 \\end{pmatrix}$ ($N^2 = 0$).
$$e^{At} = e^t e^{Nt} = e^t (I + Nt) = e^t \\begin{pmatrix} 1 & t \\\\ 0 & 1 \\end{pmatrix} = \\begin{pmatrix} e^t & t e^t \\\\ 0 & e^t \\end{pmatrix}$$
Multiply by the initial condition $x(0) = \\begin{pmatrix} 1 \\\\ 2 \\end{pmatrix}$:
$$x(t) = \\begin{pmatrix} e^t & t e^t \\\\ 0 & e^t \\end{pmatrix} \\begin{pmatrix} 1 \\\\ 2 \\end{pmatrix} = \\begin{pmatrix} 1 \\cdot e^t + 2t e^t \\\\ 0 + 2e^t \\end{pmatrix} = <span class=\"ans\">e^t \\begin{pmatrix} 1 + 2t \\\\ 2 \\end{pmatrix}</span>$$</p>

<p><span class="part">Part (b): Matrix Taylor Formula Derivation</span><br>
Expand $f(z)$ in a Taylor series about $z = \\lambda$:
$$f(z) = f(\\lambda) + f'(\\lambda)(z - \\lambda) + \\frac{f''(\\lambda)}{2!}(z - \\lambda)^2 + \\dots$$
Substitute $z = J = \\begin{pmatrix} \\lambda & 1 \\\\ 0 & \\lambda \\end{pmatrix}$:
$$J - \\lambda I = \\begin{pmatrix} 0 & 1 \\\\ 0 & 0 \\end{pmatrix} = N$$
Notice $(J - \\lambda I)^2 = N^2 = 0$.<br>
Therefore, all higher-order derivative terms $(J - \\lambda I)^k$ for $k \\ge 2$ vanish completely:
$$f(J) = f(\\lambda) I + f'(\\lambda) N + 0 = f(\\lambda) \\begin{pmatrix} 1 & 0 \\\\ 0 & 1 \\end{pmatrix} + f'(\\lambda) \\begin{pmatrix} 0 & 1 \\\\ 0 & 0 \\end{pmatrix}$$
<span class=\"ans\">$$f(J) = \\begin{pmatrix} f(\\lambda) & f'(\\lambda) \\\\ 0 & f(\\lambda) \\end{pmatrix}$$</span>
(For a $k \\times k$ block, derivatives extend up to $\\frac{f^{(k-1)}(\\lambda)}{(k-1)!}$ along the top-right band).</p>

<p><span class="part">Part (c): Computation of $J^{50}$</span><br>
Let $f(z) = z^{50}$ and $\\lambda = 2$:
$$f(2) = 2^{50}$$
$$f'(z) = 50 z^{49} \\implies f'(2) = 50 \\cdot 2^{49} = 25 \\cdot 2^{50}$$
Applying the Matrix Taylor formula from Part (b):
<span class=\"ans\">$$J^{50} = \\begin{pmatrix} 2^{50} & 50 \\cdot 2^{49} \\\\ 0 & 2^{50} \\end{pmatrix} = 2^{49} \\begin{pmatrix} 2 & 50 \\\\ 0 & 2 \\end{pmatrix}$$</span></p>""",
        "takeaway": "Evaluating matrix functions on Jordan blocks truncates the Taylor expansion at the block size: f(J_k(lambda)) has diagonal f(lambda), first superdiagonal f'(lambda), second f''(lambda)/2!, up to f^(k-1)(lambda)/(k-1)!."
    },

    # =========================================================================
    # TOPIC 10: Inner Product Spaces, Norms, and Orthogonality
    # =========================================================================
    {
        "id": 21091,
        "subject": "LAA",
        "topicId": "10_Inner_Product_Spaces_Norms_and_Orthogonality",
        "topicTitle": "10 · Inner Products & Orthogonality",
        "title": "Parallelogram Identity Violation for Non-Euclidean Norms (IISc Midterm 2 / Axler 6.A)",
        "kind2": "pyq",
        "source": "IISc Midterm 2 / Axler Linear Algebra Done Right 6.A",
        "marks": "[6 Marks]",
        "question": """<p>Consider the $\\ell_\\infty$ (Chebyshev / uniform) norm on $\\mathbb{R}^2$:
$$\\|x\\|_\\infty = \\max(|x_1|, |x_2|)$$</p>
<p><span class="part">(a)</span> State the <strong>Parallelogram Identity</strong> and state the Jordan-von Neumann Theorem regarding when a norm originates from an inner product.</p>
<p><span class="part">(b)</span> Choose test vectors $u = (1, 0)^\\top$ and $v = (0, 1)^\\top$, evaluate both sides of the Parallelogram Identity under the $\\ell_\\infty$ norm, and prove that $\\|\\cdot\\|_\\infty$ does NOT arise from any inner product.</p>
<p><span class="part">(c)</span> Geometrically, contrast the unit sphere of an inner product space with the unit sphere of $(\\mathbb{R}^2, \\|\\cdot\\|_\\infty)$.</p>""",
        "solution": """<p><span class="part">Part (a): Parallelogram Identity & Jordan-von Neumann Theorem</span><br>
The Parallelogram Identity states that for any vectors $u, v$:
<span class=\"ans\">$$\\|u + v\\|^2 + \\|u - v\\|^2 = 2\\|u\\|^2 + 2\\|v\\|^2$$</span>
<strong>Theorem (Jordan & von Neumann, 1935):</strong> A norm $\\|\\cdot\\|$ on a real or complex vector space originates from an inner product (via $\\|x\\| = \\sqrt{\\langle x, x \\rangle}$) if and only if it satisfies the Parallelogram Identity for all pairs of vectors.</p>

<p><span class="part">Part (b): Evaluating Parallelogram Identity on $\\ell_\\infty$</span><br>
Choose $u = \\begin{pmatrix} 1 \\\\ 0 \\end{pmatrix}$ and $v = \\begin{pmatrix} 0 \\\\ 1 \\end{pmatrix}$.<br>
1. <strong>Individual Norms:</strong>
$$\\|u\\|_\\infty = \\max(|1|, |0|) = 1 \\implies \\|u\\|_\\infty^2 = 1$$
$$\\|v\\|_\\infty = \\max(|0|, |1|) = 1 \\implies \\|v\\|_\\infty^2 = 1$$
The right-hand side is:
$$\\text{RHS} = 2\\|u\\|_\\infty^2 + 2\\|v\\|_\\infty^2 = 2(1) + 2(1) = <span class=\"ans\">4</span>$$
2. <strong>Sum and Difference Norms:</strong>
$$u + v = \\begin{pmatrix} 1 \\\\ 1 \\end{pmatrix} \\implies \\|u + v\\|_\\infty = \\max(1, 1) = 1 \\implies \\|u + v\\|_\\infty^2 = 1$$
$$u - v = \\begin{pmatrix} 1 \\\\ -1 \\end{pmatrix} \\implies \\|u - v\\|_\\infty = \\max(1, |-1|) = 1 \\implies \\|u - v\\|_\\infty^2 = 1$$
The left-hand side is:
$$\\text{LHS} = \\|u + v\\|_\\infty^2 + \\|u - v\\|_\\infty^2 = 1 + 1 = <span class=\"ans\">2</span>$$
3. <strong>Conclusion:</strong>
$$\\text{LHS} = 2 \\ne 4 = \\text{RHS}$$
<span class=\"ans\">The Parallelogram Identity fails ($2 \\ne 4$).</span> Therefore, the $\\ell_\\infty$ norm cannot arise from any inner product on $\\mathbb{R}^2$.</p>

<p><span class="part">Part (c): Geometric Distinction of Unit Spheres</span><br>
- <strong>Inner Product Spaces:</strong> The unit ball $\\{x : \\|x\\| \\le 1\\}$ is always an ellipsoid (strictly convex with a smooth, differentiable boundary; no flat edges or corners).<br>
- <strong>$\\ell_\\infty$ Space:</strong> The unit ball $\\{x : \\max(|x_1|, |x_2|) \\le 1\\}$ is a <strong>square</strong> with sharp corners at $(\\pm 1, \\pm 1)$ and flat edges. It violates strict convexity, reflecting the failure of inner product geometry.</p>""",
        "takeaway": "A norm arises from an inner product if and only if it satisfies the Parallelogram Identity. The l_infinity norm fails the identity (2 != 4 for coordinate axes), creating a square unit ball with non-smooth corners."
    },
    {
        "id": 21092,
        "subject": "LAA",
        "topicId": "10_Inner_Product_Spaces_Norms_and_Orthogonality",
        "topicTitle": "10 · Inner Products & Orthogonality",
        "title": "Cauchy-Schwarz Inequality & Triangle Inequality with Sharp Equality Conditions (MIT 18.06 / Axler 6.16)",
        "kind2": "pyq",
        "source": "MIT 18.06 Linear Algebra / Axler Linear Algebra Done Right 6.16",
        "marks": "[8 Marks]",
        "question": """<p>Let $V$ be an inner product space over field $\\mathbb{F}$ (where $\\mathbb{F} = \\mathbb{R}$ or $\\mathbb{C}$).</p>
<p><span class="part">(a)</span> State the Cauchy-Schwarz Inequality $|\\langle u, v \\rangle| \\le \\|u\\| \\|v\\|$, and state the exact condition under which equality holds.</p>
<p><span class="part">(b)</span> Prove the <strong>Triangle Inequality</strong> $\\|u + v\\| \\le \\|u\\| + \\|v\\|$ using the Cauchy-Schwarz Inequality.</p>
<p><span class="part">(c)</span> Prove that equality $\\|u + v\\| = \\|u\\| + \\|v\\|$ holds if and only if one of the vectors is a non-negative real scalar multiple of the other ($u = c v$ with $c \\ge 0$).</p>""",
        "solution": """<p><span class="part">Part (a): Cauchy-Schwarz Inequality</span><br>
For all vectors $u, v \\in V$:
<span class=\"ans\">$$|\\langle u, v \\rangle| \\le \\|u\\| \\|v\\|$$</span>
Equality holds if and only if $u$ and $v$ are <strong>linearly dependent</strong> (one vector is a scalar multiple of the other).</p>

<p><span class="part">Part (b): Derivation of the Triangle Inequality</span><br>
Expand the squared norm $\\|u + v\\|^2$:
$$\\|u + v\\|^2 = \\langle u + v, \\; u + v \\rangle = \\langle u, u \\rangle + \\langle u, v \\rangle + \\langle v, u \\rangle + \\langle v, v \\rangle$$
Since $\\langle v, u \\rangle = \\overline{\\langle u, v \\rangle}$:
$$\\langle u, v \\rangle + \\langle v, u \\rangle = 2 \\operatorname{Re}\\langle u, v \\rangle$$
$$\\|u + v\\|^2 = \\|u\\|^2 + 2 \\operatorname{Re}\\langle u, v \\rangle + \\|v\\|^2$$
For any complex number $z$, $\\operatorname{Re}(z) \\le |z|$:
$$\\|u + v\\|^2 \\le \\|u\\|^2 + 2 |\\langle u, v \\rangle| + \\|v\\|^2$$
Apply the Cauchy-Schwarz Inequality $|\\langle u, v \\rangle| \\le \\|u\\| \\|v\\|$:
$$\\|u + v\\|^2 \\le \\|u\\|^2 + 2 \\|u\\| \\|v\\| + \\|v\\|^2 = (\\|u\\| + \\|v\\|)^2$$
Since both sides are non-negative, taking the positive square root gives:
<span class=\"ans\">$$\\|u + v\\| \\le \\|u\\| + \\|v\\|$$</span></p>

<p><span class="part">Part (c): Equality Condition Proof</span><br>
Tracking the equalities in Part (b): $\\|u + v\\|^2 = (\\|u\\| + \\|v\\|)^2$ requires:
1. $\\operatorname{Re}\\langle u, v \\rangle = |\\langle u, v \\rangle|$, which means $\\langle u, v \\rangle$ must be a non-negative real number ($\\langle u, v \\rangle \\ge 0$).
2. $|\\langle u, v \\rangle| = \\|u\\| \\|v\\|$, which requires $u$ and $v$ to be linearly dependent (Cauchy-Schwarz equality condition).<br>
Assuming $v \\ne 0$, linear dependence implies $u = c v$ for some scalar $c \\in \\mathbb{F}$.<br>
Substitute $u = cv$ into condition 1:
$$\\langle c v, v \\rangle = c \\langle v, v \\rangle = c \\|v\\|^2 \\ge 0$$
Since $\\|v\\|^2 > 0$, this requires:
<span class=\"ans\">$$c \\ge 0 \\quad (c \\in \\mathbb{R})$$</span>
Therefore, equality $\\|u + v\\| = \\|u\\| + \\|v\\|$ holds if and only if one vector is a <strong>non-negative real scalar multiple</strong> of the other (vectors point in the identical ray direction from the origin).</p>""",
        "takeaway": "The triangle inequality ||u + v|| <= ||u|| + ||v|| follows from Cauchy-Schwarz, with equality holding if and only if u and v point in the same direction (u = c v with c >= 0)."
    },
    {
        "id": 21093,
        "subject": "LAA",
        "topicId": "10_Inner_Product_Spaces_Norms_and_Orthogonality",
        "topicTitle": "10 · Inner Products & Orthogonality",
        "title": "Double Orthogonal Complement Theorem & Linear Independence of Orthogonal Sets (Generated IISc / Stanford EE263 & Berkeley EECS 127)",
        "kind2": "generated",
        "source": "Generated IISc Midterm / Stanford EE263 (Axler 6.48) & Berkeley EECS 127",
        "marks": "[8 Marks]",
        "question": """<p><span class="part">(a)</span> Let $U$ be a subspace of a finite-dimensional inner product space $V$. Prove rigorously that:
$$(U^\\perp)^\\perp = U$$</p>
<p><span class="part">(b)</span> Let $\\{v_1, v_2, \\dots, v_m\\} \\subset V$ be a collection of non-zero pairwise orthogonal vectors (i.e. $\\langle v_i, v_j \\rangle = 0$ for all $i \\ne j$, and $v_i \\ne 0$). Prove that $\\{v_1, \\dots, v_m\\}$ is linearly independent.</p>
<p><span class="part">(c)</span> Use this to deduce Bessel's Inequality: if $\\{e_1, \\dots, e_m\\}$ is an orthonormal set, then for any $v \\in V$:
$$\\sum_{k=1}^m |\\langle v, e_k \\rangle|^2 \\le \\|v\\|^2$$</p>""",
        "solution": """<p><span class="part">Part (a): Proof that $(U^\\perp)^\\perp = U$</span><br>
1. <strong>Inclusion $U \\subseteq (U^\\perp)^\\perp$:</strong><br>
Let $u \\in U$. By definition of the orthogonal complement:
$$\\langle u, w \\rangle = 0 \\quad \\text{for all } w \\in U^\\perp$$
Now consider the defining condition of $(U^\\perp)^\\perp$:
$$(U^\\perp)^\\perp = \\{ v \\in V : \\langle v, w \\rangle = 0 \\quad \\forall w \\in U^\\perp \\}$$
Since $u$ is orthogonal to every vector in $U^\\perp$, it satisfies the condition:
<span class=\"ans\">$$U \\subseteq (U^\\perp)^\\perp$$</span>
2. <strong>Dimension Equality:</strong><br>
By the Orthogonal Decomposition Theorem applied to $U$:
$$\\dim V = \\dim U + \\dim U^\\perp \\implies \\dim U^\\perp = \\dim V - \\dim U$$
Now apply the same theorem to the subspace $U^\\perp$:
$$\\dim V = \\dim U^\\perp + \\dim (U^\\perp)^\\perp$$
Substitute $\\dim U^\\perp$:
$$\\dim V = (\\dim V - \\dim U) + \\dim (U^\\perp)^\\perp \\implies \\dim (U^\\perp)^\\perp = \\dim U$$
Since $U$ is a subspace of $(U^\\perp)^\\perp$ and both have identical finite dimensions:
<span class=\"ans\">$$(U^\\perp)^\\perp = U$$</span></p>

<p><span class="part">Part (b): Linear Independence of Orthogonal Sets</span><br>
Suppose $\\sum_{i=1}^m a_i v_i = 0$ for scalars $a_1, \\dots, a_m \\in \\mathbb{F}$.<br>
Let $k \\in \\{1, \\dots, m\\}$ be an arbitrary index. Take the inner product of both sides with $v_k$:
$$\\left\\langle \\sum_{i=1}^m a_i v_i, \\; v_k \\right\\rangle = \\langle 0, v_k \\rangle = 0$$
Using linearity in the first argument:
$$\\sum_{i=1}^m a_i \\langle v_i, v_k \\rangle = 0$$
Since vectors are pairwise orthogonal, $\\langle v_i, v_k \\rangle = 0$ for all $i \\ne k$. The sum collapses to a single term:
$$a_k \\langle v_k, v_k \\rangle = 0 \\implies a_k \\|v_k\\|^2 = 0$$
Since $v_k$ is a non-zero vector, $\\|v_k\\|^2 > 0$. Therefore:
<span class=\"ans\">$$a_k = 0$$</span>
Since this holds for every $k \\in \\{1, \\dots, m\\}$, $a_1 = a_2 = \\dots = a_m = 0$.<br>
Hence $\\{v_1, \\dots, v_m\\}$ is strictly <strong>linearly independent</strong>.</p>

<p><span class="part">Part (c): Bessel's Inequality</span><br>
Let $u = \\sum_{k=1}^m \\langle v, e_k \\rangle e_k$ be the orthogonal projection of $v$ onto $U = \\operatorname{span}(e_1, \\dots, e_m)$.<br>
Then $v - u \\in U^\\perp$. By Pythagorean Theorem:
$$\\|v\\|^2 = \\|u\\|^2 + \\|v - u\\|^2 \\ge \\|u\\|^2$$
Expand $\\|u\\|^2$ using orthonormality:
$$\\|u\\|^2 = \\left\\| \\sum_{k=1}^m \\langle v, e_k \\rangle e_k \\right\\|^2 = \\sum_{k=1}^m |\\langle v, e_k \\rangle|^2$$
Substituting into the inequality gives Bessel's Inequality:
<span class=\"ans\">$$\\sum_{k=1}^m |\\langle v, e_k \\rangle|^2 \\le \\|v\\|^2$$</span></p>""",
        "takeaway": "In finite-dimensional inner product spaces, the double orthogonal complement satisfies (U^⊥)^⊥ = U. Any set of non-zero pairwise orthogonal vectors is linearly independent, and projecting onto orthonormal subsets yields Bessel's inequality sum |<v, e_k>|^2 <= ||v||^2."
    }
]

def main():
    with open(PRACTICE_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    if "20991" in content:
        print("Batch 09-10 already present in practice_laa.js!")
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
    for card in PRACTICE_LAA_09_10:
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

    print("Successfully added LAA Batch 09-10 (6 cards). Total in file now updated.")

if __name__ == "__main__":
    main()
