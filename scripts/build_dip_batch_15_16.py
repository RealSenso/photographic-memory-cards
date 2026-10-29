#!/usr/bin/env python3
"""
Builder script for DIP Practice Cards: Batch 08 (Topics 15 & 16)
Topic 15: Hough Transform for Lines and Circles (Cards 41591, 41592, 41593)
Topic 16: Corner Detection and Harris Detector (Cards 41691, 41692, 41693)
"""

import json
import os
import re

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRACTICE_FILE = os.path.join(REPO_DIR, "practice_dip.js")

PRACTICE_DIP_15_16 = [
    # =========================================================================
    # TOPIC 15: Hough Transform for Lines and Circles
    # =========================================================================
    {
        "id": 41591,
        "subject": "DIP",
        "topicId": "15_Hough_Transform_for_Lines_and_Circles",
        "topicTitle": "15 · Hough Transform: Lines & Circles",
        "title": "Hough Transform Normal Line Parameterization & Collinear Accumulator Peak (IISc Midterm / Gonzalez & Woods)",
        "kind2": "pyq",
        "source": "IISc Midterm / Gonzalez & Woods Digital Image Processing Ch. 10",
        "marks": "[8 Marks]",
        "question": """<p>Three binary edge pixels are detected at Cartesian coordinates:
$$P_1 = (1, 1), \\qquad P_2 = (2, 2), \\qquad P_3 = (3, 3)$$
Consider the standard normal parametrization for straight lines:
$$\\rho = x \\cos\\theta + y \\sin\\theta$$</p>
<p><span class="part">(a)</span> Evaluate the distance parameter $\\rho$ for each of the three points across candidate orientation angles $\\theta \\in \\{0^\\circ, 45^\\circ, 90^\\circ, 135^\\circ\\}$.</p>
<p><span class="part">(b)</span> Construct the discrete $(\\rho, \\theta)$ accumulator table, accumulate votes from all three points, and identify the winning parameter cell $(\\rho^*, \\theta^*)$.</p>
<p><span class="part">(c)</span> Transform the winning parameter pair into standard Cartesian slope-intercept form and verify the geometric alignment with the three points.</p>""",
        "solution": """<p><span class="part">Part (a): Evaluate $\\rho = x\\cos\\theta + y\\sin\\theta$ for Candidate Angles</span><br>
Trigonometric values:
<ul>
  <li>$\\theta = 0^\\circ$: $\\cos 0^\\circ = 1, \\sin 0^\\circ = 0 \\implies \\rho = x$</li>
  <li>$\\theta = 45^\\circ$: $\\cos 45^\\circ = \\frac{\\sqrt{2}}{2} \\approx 0.7071, \\sin 45^\\circ \\approx 0.7071 \\implies \\rho = 0.7071(x + y)$</li>
  <li>$\\theta = 90^\\circ$: $\\cos 90^\\circ = 0, \\sin 90^\\circ = 1 \\implies \\rho = y$</li>
  <li>$\\theta = 135^\\circ$: $\\cos 135^\\circ = -\\frac{\\sqrt{2}}{2} \\approx -0.7071, \\sin 135^\\circ \\approx 0.7071 \\implies \\rho = 0.7071(y - x)$</li>
</ul>
Computing $\\rho$ for each point:
1. <strong>For $P_1 = (1, 1)$ ($y - x = 0$):</strong><br>
$\\theta=0^\\circ: \\rho = 1$; $\\theta=45^\\circ: \\rho = \\sqrt{2} \\approx 1.414$; $\\theta=90^\\circ: \\rho = 1$; <span class=\"ans\">$\\theta=135^\\circ: \\rho = 0.7071(1 - 1) = 0$</span>.<br>
2. <strong>For $P_2 = (2, 2)$ ($y - x = 0$):</strong><br>
$\\theta=0^\\circ: \\rho = 2$; $\\theta=45^\\circ: \\rho = 2\\sqrt{2} \\approx 2.828$; $\\theta=90^\\circ: \\rho = 2$; <span class=\"ans\">$\\theta=135^\\circ: \\rho = 0.7071(2 - 2) = 0$</span>.<br>
3. <strong>For $P_3 = (3, 3)$ ($y - x = 0$):</strong><br>
$\\theta=0^\\circ: \\rho = 3$; $\\theta=45^\\circ: \\rho = 3\\sqrt{2} \\approx 4.243$; $\\theta=90^\\circ: \\rho = 3$; <span class=\"ans\">$\\theta=135^\\circ: \\rho = 0.7071(3 - 3) = 0$</span>.</p>

<p><span class="part">Part (b): Accumulator Voting Table</span><br>
Mapping the votes to an accumulator table $A(\\rho, \\theta)$:
<table style=\"border-collapse: collapse; margin: 10px 0;\">
  <tr style=\"border-bottom: 2px solid #555;\"><th style=\"padding: 4px 12px;\">$\\rho$</th><th style=\"padding: 4px 12px;\">$\\theta = 0^\\circ$</th><th style=\"padding: 4px 12px;\">$\\theta = 45^\\circ$</th><th style=\"padding: 4px 12px;\">$\\theta = 90^\\circ$</th><th style=\"padding: 4px 12px;\">$\\theta = 135^\\circ$</th></tr>
  <tr><td style=\"padding: 4px 12px;\"><strong>0</strong></td><td>0</td><td>0</td><td>0</td><td style=\"background:#d4edda; font-weight:bold;\">3 (P1, P2, P3)</td></tr>
  <tr><td style=\"padding: 4px 12px;\">1</td><td>1 (P1)</td><td>0</td><td>1 (P1)</td><td>0</td></tr>
  <tr><td style=\"padding: 4px 12px;\">$\\sqrt{2}$</td><td>0</td><td>1 (P1)</td><td>0</td><td>0</td></tr>
  <tr><td style=\"padding: 4px 12px;\">2</td><td>1 (P2)</td><td>0</td><td>1 (P2)</td><td>0</td></tr>
  <tr><td style=\"padding: 4px 12px;\">3</td><td>1 (P3)</td><td>0</td><td>1 (P3)</td><td>0</td></tr>
</table>
<span class=\"ans\">Winning accumulator peak: $(\\rho^*, \\theta^*) = (0, 135^\\circ)$ with 3 unanimous votes.</span></p>

<p><span class="part">Part (c): Cartesian Line Equation</span><br>
Substitute $(\\rho^*, \\theta^*) = (0, 135^\\circ)$ into the normal equation:
$$0 = x \\cos(135^\\circ) + y \\sin(135^\\circ) = -\\frac{\\sqrt{2}}{2} x + \\frac{\\sqrt{2}}{2} y$$
Multiply both sides by $\\sqrt{2}$:
$$-x + y = 0 \\implies <span class=\"ans\">y = x</span>$$
The line $y = x$ has slope $m = 1$ and intercept $c = 0$, passing through all three collinear points $(1, 1), (2, 2), (3, 3)$ with zero error.</p>""",
        "takeaway": "The normal parametrization ρ = x cos θ + y sin θ maps image points to sinusoidal curves in (ρ, θ) parameter space. The intersection of these sinusoids yields an accumulator peak identifying the line passing through all collinear edge points."
    },
    {
        "id": 41592,
        "subject": "DIP",
        "topicId": "15_Hough_Transform_for_Lines_and_Circles",
        "topicTitle": "15 · Hough Transform: Lines & Circles",
        "title": "Gradient-Directed Circular Hough Transform & Center Localization (IIT Delhi / Ballard)",
        "kind2": "pyq",
        "source": "IIT Delhi / Ballard (Computer Vision / Generalizing the Hough Transform 1981)",
        "marks": "[8 Marks]",
        "question": """<p>An edge detector detects an isolated edge pixel at coordinate $(x_0, y_0) = (15, 20)$ with spatial gradient vector $\\nabla f = (G_x, G_y) = (6, 8)$. We are detecting circular objects of known radius $R = 10$.</p>
<p><span class="part">(a)</span> Compute the unit gradient direction normal vector $\\hat{\\mathbf{n}}$.</p>
<p><span class="part">(b)</span> Assuming the circular object is brighter than the surrounding background (such that $\\nabla f$ points inward toward the center), determine the candidate center coordinate $(a, b)$.</p>
<p><span class="part">(c)</span> Compare the accumulator voting complexity and memory footprint of this gradient-directed circle detection against the standard undirected circular Hough Transform.</p>""",
        "solution": """<p><span class="part">Part (a): Compute Unit Gradient Normal Vector</span><br>
Given gradient components $G_x = 6$ and $G_y = 8$:
$$\\|\\nabla f\\| = \\sqrt{G_x^2 + G_y^2} = \\sqrt{6^2 + 8^2} = \\sqrt{36 + 64} = \\sqrt{100} = 10$$
The normalized unit normal vector is:
<span class=\"ans\">$$\\hat{\\mathbf{n}} = \\left(\\frac{G_x}{\\|\\nabla f\\|}, \\frac{G_y}{\\|\\nabla f\\|}\\right) = \\left(\\frac{6}{10}, \\frac{8}{10}\\right) = (0.6, 0.8)$$</span></p>

<p><span class="part">Part (b): Candidate Circle Center $(a, b)$</span><br>
The gradient vector points in the direction of steepest intensity increase. Since the object interior is brighter than the background, the gradient vector at the perimeter points radially <strong>inward toward the center</strong>.<br>
Therefore, the center $(a, b)$ is located at distance $R = 10$ along direction $\\hat{\\mathbf{n}}$ from $(x_0, y_0)$:
$$a = x_0 + R \\cdot \\hat{n}_x = 15 + 10(0.6) = 15 + 6 = <span class=\"ans\">21</span>$$
$$b = y_0 + R \\cdot \\hat{n}_y = 20 + 10(0.8) = 20 + 8 = <span class=\"ans\">28</span>$$
The candidate circle center is located at <span class=\"ans\">$(a, b) = (21, 28)$</span>.<br>
(Note: If polarity were ambiguous, two candidate centers $(x_0 \\pm R \\hat{n}_x, y_0 \\pm R \\hat{n}_y)$ would be voted on).</p>

<p><span class="part">Part (c): Voting Complexity Comparison</span><br>
1. <strong>Standard Undirected Circular Hough Transform:</strong><br>
Without gradient orientation, a detected edge point $(x_0, y_0)$ can belong to a circle whose center lies in any direction at distance $R$:
$$(a - 15)^2 + (b - 20)^2 = 10^2$$
Discretizing the circle at $1^\\circ$ angular intervals requires casting <strong>360 votes</strong> across a circular locus in the $(a, b)$ accumulator array.<br>
2. <strong>Gradient-Directed Circular Hough Transform:</strong><br>
Using the local edge gradient $\\nabla f$, the direction is uniquely pinned down to the normal ray. The edge point casts <strong>exactly 1 vote</strong> (or 2 votes if contrast sign is unknown) at the specific cell $(21, 28)$.<br>
<span class=\"ans\">Speedup & Clutter:</span> Gradient guidance reduces accumulator voting traffic by $360 \\times$ ($\approx 99.7\\%$ reduction), drastically diminishes spurious background clutter, and accelerates computation by orders of magnitude.</p>""",
        "takeaway": "Using edge gradient direction in the circular Hough Transform restricts the search for the circle center from an entire 360° ring of radius R to a single point along the gradient vector, reducing accumulator clutter and voting complexity by 360x."
    },
    {
        "id": 41593,
        "subject": "DIP",
        "topicId": "15_Hough_Transform_for_Lines_and_Circles",
        "topicTitle": "15 · Hough Transform: Lines & Circles",
        "title": "Generalized Hough Transform (GHT) R-Table Mechanics & Randomized Hough (Generated IISc / Ballard Benchmark)",
        "kind2": "generated",
        "source": "Generated IISc Midterm / D. Ballard (Pattern Recognition 1981) & Bovik Handbook",
        "marks": "[8 Marks]",
        "question": """<p><span class="part">(a)</span> Explain the Generalized Hough Transform (GHT) for detecting an arbitrary non-analytical shape. Describe the construction of the offline <strong>R-table</strong> indexed by gradient direction $\\phi$, and specify the online voting equation for candidate reference points $(x_c, y_c)$.</p>
<p><span class="part">(b)</span> Formulate the modified voting equation when the query object undergoes both scale change $s$ and planar rotation $\\theta$. What is the dimensionality of the resulting accumulator array?</p>
<p><span class="part">(c)</span> In practical edge maps, discretization noise causes a single straight line to produce a cluster of adjacent votes (peak splitting). Contrast two techniques for resolving this: (i) accumulator Gaussian smoothing, and (ii) the Randomized Hough Transform (RHT).</p>""",
        "solution": """<p><span class="part">Part (a): Generalized Hough Transform (GHT) & R-Table</span><br>
For arbitrary 2D shapes without an analytical formula (e.g. industrial templates):
1. <strong>Offline Training (R-Table Construction):</strong>
<ul>
  <li>Select an internal centroid/reference point $\\mathbf{x}_c = (x_c, y_c)$.</li>
  <li>For each boundary point $\\mathbf{x}_i = (x_i, y_i)$, compute the gradient angle $\\phi_i = \\operatorname{atan2}(G_y, G_x)$.</li>
  <li>Compute displacement vector $\\mathbf{r}_i = \\mathbf{x}_c - \\mathbf{x}_i$ in polar form $(r_i, \\alpha_i)$ where $r_i = \\|\\mathbf{r}_i\\|$ and $\\alpha_i = \\operatorname{atan2}(y_c - y_i, x_c - x_i)$.</li>
  <li>Store $(r_i, \\alpha_i)$ in the R-table under row index $\\phi_i$.</li>
</ul>
2. <strong>Online Recognition & Voting:</strong><br>
For each edge point $(x, y)$ in the query image with gradient angle $\\phi$:
Retrieve all stored pairs $(r_k, \\alpha_k)$ in row $\\phi$ of the R-table. Compute candidate center coordinates:
<span class=\"ans\">$$x_c = x + r_k \\cos(\\alpha_k), \\qquad y_c = y + r_k \\sin(\\alpha_k)$$</span>
Increment $A(x_c, y_c) \\leftarrow A(x_c, y_c) + 1$. A sharp peak in $A$ detects the object reference point.</p>

<p><span class="part">Part (b): Handling Scale and Rotation in 4D Parameter Space</span><br>
If the object is scaled by $s$ and rotated by angle $\\theta$:
The local gradient angle shifts: $\\phi' = \\phi + \\theta \\implies \\phi = \\phi' - \\theta$.<br>
The displacement vector rotates by $\\theta$ and scales by $s$:
<span class=\"ans\">$$x_c = x + s \\cdot r_k \\cos(\\alpha_k + \\theta), \\qquad y_c = y + s \\cdot r_k \\sin(\\alpha_k + \\theta)$$</span>
The parameter space expands to <strong>4 dimensions: $(x_c, y_c, s, \\theta)$</strong>.<br>
Accumulator storage scales as $\\mathcal{O}(N_x N_y N_s N_\\theta)$, requiring hierarchical coarse-to-fine pyramids to maintain tractable memory usage.</p>

<p><span class="part">Part (c): Peak Splitting Mitigation: Gaussian Smoothing vs. RHT</span><br>
Due to spatial rasterization and edge localization noise, sinusoids intersect across several adjacent accumulator bins rather than a single ideal point.<br>
1. <strong>Accumulator Gaussian Smoothing:</strong><br>
Convolving the discrete accumulator $A(\\rho, \\theta)$ with a small $3 \\times 3$ or $5 \\times 5$ Gaussian kernel fuses the split fragment peaks into a single smooth mode, allowing clean peak extraction via Non-Maximum Suppression (NMS).<br>
2. <strong>Randomized Hough Transform (RHT):</strong><br>
Instead of mapping every edge point to a continuous curve over all $\\theta$:
- Randomly pick a pair of edge pixels $(p_1, p_2)$. Exactly one line passes through two points: $(\\rho, \\theta)$ is uniquely computed in $\\mathcal{O}(1)$ time.
- Cast a single vote into an adaptive hash table.
- Once a hash bin crosses threshold, verify the candidate line in the image and remove matched pixels.
RHT eliminates the giant static accumulator array ($\mathcal{O}(1)$ dynamic storage) and runs up to $100\\times$ faster.</p>""",
        "takeaway": "The Generalized Hough Transform (GHT) enables invariant recognition of arbitrary non-analytical shapes via an offline R-table indexed by gradient angle. The Randomized Hough Transform (RHT) avoids large accumulator tables by sampling pixel pairs to solve line parameters in O(1) time."
    },

    # =========================================================================
    # TOPIC 16: Corner Detection and Harris Detector
    # =========================================================================
    {
        "id": 41691,
        "subject": "DIP",
        "topicId": "16_Corner_Detection_and_Harris_Detector",
        "topicTitle": "16 · Corners: Harris-Stephens",
        "title": "Structure Tensor Eigenvalue Derivation & Harris Response (IISc Midterm / Harris & Stephens)",
        "kind2": "pyq",
        "source": "IISc Midterm / Harris & Stephens (Alvey Vision Conf. 1988)",
        "marks": "[8 Marks]",
        "question": """<p>Over a local $3 \\times 3$ neighborhood window, spatial derivatives $(I_x, I_y)$ are evaluated with uniform window weights $w(x, y) = 1$:
$$I_x = \\begin{pmatrix} 2 & 2 & 2 \\\\ 2 & 2 & 2 \\\\ 2 & 2 & 2 \\end{pmatrix}, \\qquad I_y = \\begin{pmatrix} 1 & 1 & 1 \\\\ 1 & 1 & 1 \\\\ 1 & 1 & 1 \\end{pmatrix}$$</p>
<p><span class="part">(a)</span> Compute the $2 \\times 2$ second moment matrix (structure tensor) $M = \\begin{pmatrix} \\sum I_x^2 & \\sum I_x I_y \\\\ \\sum I_x I_y & \\sum I_y^2 \\end{pmatrix}$.</p>
<p><span class="part">(b)</span> Calculate the exact eigenvalues $\\lambda_1, \\lambda_2$ of $M$.</p>
<p><span class="part">(c)</span> For sensitivity parameter $k = 0.05$, compute the Harris corner response $R = \\det(M) - k (\\operatorname{trace}(M))^2$ and definitively classify the region as flat, edge, or corner.</p>""",
        "solution": """<p><span class="part">Part (a): Compute Structure Tensor $M$</span><br>
The $3 \\times 3$ window contains $N = 9$ pixels. For every pixel, $I_x = 2$ and $I_y = 1$:
<ul>
  <li>$\\sum I_x^2 = 9 \\times (2^2) = 9 \\times 4 = 36$</li>
  <li>$\\sum I_y^2 = 9 \\times (1^2) = 9 \\times 1 = 9$</li>
  <li>$\\sum I_x I_y = 9 \\times (2 \\times 1) = 9 \\times 2 = 18$</li>
</ul>
The structure tensor is:
<span class=\"ans\">$$M = \\begin{pmatrix} 36 & 18 \\\\ 18 & 9 \\end{pmatrix}$$</span></p>

<p><span class="part">Part (b): Eigenvalues of $M$</span><br>
The characteristic equation is $\\det(M - \\lambda I) = 0$:
$$\\det\\begin{pmatrix} 36 - \\lambda & 18 \\\\ 18 & 9 - \\lambda \\end{pmatrix} = (36 - \\lambda)(9 - \\lambda) - 18^2 = 0$$
$$\\lambda^2 - 45 \\lambda + 324 - 324 = 0 \\implies \\lambda^2 - 45 \\lambda = 0 \\implies \\lambda(\\lambda - 45) = 0$$
The eigenvalues are:
<span class=\"ans\">$$\\lambda_1 = 45, \\qquad \\lambda_2 = 0$$</span></p>

<p><span class="part">Part (c): Harris Response & Classification</span><br>
Compute determinant and trace:
$$\\det(M) = \\lambda_1 \\lambda_2 = 45 \\times 0 = 0 \\quad (\\text{or } 36 \\times 9 - 18^2 = 324 - 324 = 0)$$
$$\\operatorname{trace}(M) = \\lambda_1 + \\lambda_2 = 45 + 0 = 45$$
Evaluate Harris response with $k = 0.05$:
$$R = \\det(M) - k (\\operatorname{trace}(M))^2 = 0 - 0.05(45^2) = -0.05(2025) = <span class=\"ans\">-101.25</span>$$
<strong>Classification Criteria:</strong>
<ul>
  <li>Flat region: $\\lambda_1 \\approx 0, \\lambda_2 \\approx 0 \\implies |R| \\approx 0$.</li>
  <li>Corner: $\\lambda_1 \\gg 0, \\lambda_2 \\gg 0 \\implies R > 0$ (large positive).</li>
  <li>Edge: $\\lambda_1 \\gg \\lambda_2 \\approx 0 \\implies R < 0$ (large negative).</li>
</ul>
<span class=\"ans\">Classification: EDGE</span>. Since $\\lambda_1 = 45 \\gg \\lambda_2 = 0$ and $R = -101.25$ is strongly negative, the region is an edge oriented with normal angle $\\theta = \\operatorname{atan2}(1, 2) \\approx 26.57^\\circ$.</p>""",
        "takeaway": "The Harris structure tensor characterizes local image patches via eigenvalues: flat regions have λ1 ≈ λ2 ≈ 0 (R ≈ 0), edges have λ1 >> λ2 ≈ 0 (R < 0), and corners have λ1 ≈ λ2 >> 0 (R > 0)."
    },
    {
        "id": 41692,
        "subject": "DIP",
        "topicId": "16_Corner_Detection_and_Harris_Detector",
        "topicTitle": "16 · Corners: Harris-Stephens",
        "title": "Shi-Tomasi Minimum Eigenvalue Criterion vs. Harris Response (IIT Delhi / CVPR 1994)",
        "kind2": "pyq",
        "source": "IIT Delhi / Shi & Tomasi (Good Features to Track / CVPR 1994)",
        "marks": "[8 Marks]",
        "question": """<p>J. Shi and C. Tomasi proposed tracking features using the minimum eigenvalue criterion $R_{\\text{ST}} = \\min(\\lambda_1, \\lambda_2)$. A candidate interest point produces structure tensor:
$$M = \\begin{pmatrix} 50 & 10 \\\\ 10 & 40 \\end{pmatrix}$$</p>
<p><span class="part">(a)</span> Compute the exact eigenvalues $\\lambda_1, \\lambda_2$ of $M$.</p>
<p><span class="part">(b)</span> Evaluate the Shi-Tomasi corner response $R_{\\text{ST}}$.</p>
<p><span class="part">(c)</span> Evaluate the Harris corner response $R$ for $k = 0.04$, and show that both detectors concur on classifying this point as an authentic corner.</p>""",
        "solution": """<p><span class="part">Part (a): Compute Eigenvalues of $M$</span><br>
The characteristic polynomial is:
$$\\det(M - \\lambda I) = (50 - \\lambda)(40 - \\lambda) - 10^2 = 0$$
$$\\lambda^2 - 90 \\lambda + 2000 - 100 = 0 \\implies \\lambda^2 - 90 \\lambda + 1900 = 0$$
Using the quadratic formula:
$$\\lambda = \\frac{90 \\pm \\sqrt{90^2 - 4(1)(1900)}}{2} = \\frac{90 \\pm \\sqrt{8100 - 7600}}{2} = \\frac{90 \\pm \\sqrt{500}}{2}$$
$$\\sqrt{500} = 10\\sqrt{5} \\approx 22.3607$$
$$\\lambda_1 = \\frac{90 + 22.3607}{2} = <span class=\"ans\">56.18</span>$$
$$\\lambda_2 = \\frac{90 - 22.3607}{2} = <span class=\"ans\">33.82</span>$$</p>

<p><span class="part">Part (b): Shi-Tomasi Response</span><br>
The Shi-Tomasi measure selects the smaller principal curvature:
$$R_{\\text{ST}} = \\min(\\lambda_1, \\lambda_2) = \\min(56.18, 33.82) = <span class=\"ans\">33.82</span>$$
Since $R_{\\text{ST}} = 33.82 > 0$ is well above typical noise detection thresholds (typically $T \\approx 5$), Shi-Tomasi decisively identifies a <strong>strong corner</strong> (stable for optical flow tracking).</p>

<p><span class="part">Part (c): Harris Corner Response</span><br>
Trace and Determinant:
$$\\operatorname{trace}(M) = 50 + 40 = 90$$
$$\\det(M) = (50)(40) - 10^2 = 2000 - 100 = 1900 \\quad (\\text{or } 56.18 \\times 33.82 \\approx 1900)$$
Evaluating Harris response with $k = 0.04$:
$$R = \\det(M) - k (\\operatorname{trace}(M))^2 = 1900 - 0.04(90^2) = 1900 - 0.04(8100)$$
$$R = 1900 - 324 = <span class=\"ans\">+1576.0</span>$$
<span class=\"ans\">Both Detectors Concur:</span><br>
- Shi-Tomasi: $\\min(\\lambda_1, \\lambda_2) = 33.82 > 0$<br>
- Harris: $R = +1576.0 \\gg 0$<br>
Both eigenvalues are large and positive ($\lambda_1 = 56.18, \lambda_2 = 33.82$), proving that image gradient energy is dispersed in two orthogonal directions, the hallmark of an authentic 2D corner feature.</p>""",
        "takeaway": "Shi-Tomasi corner detection uses min(λ1, λ2) as the direct quality metric for cornerness, avoiding the empirical tuning parameter k required by the Harris response R = det(M) - k trace(M)^2."
    },
    {
        "id": 41693,
        "subject": "DIP",
        "topicId": "16_Corner_Detection_and_Harris_Detector",
        "topicTitle": "16 · Corners: Harris-Stephens",
        "title": "Rotation Invariance Proof & Scale-Space Harris-Laplace Extension (Generated IISc / Stanford & Oxford Benchmark)",
        "kind2": "generated",
        "source": "Generated IISc Midterm / Stanford CS231A & Mikolajczyk-Schmid (IJCV 2004)",
        "marks": "[8 Marks]",
        "question": """<p><span class="part">(a)</span> Let an image undergo 2D in-plane rotation by angle $\\theta$: $\\mathbf{x}' = R_\\theta \\mathbf{x}$. Prove mathematically that the structure tensor transforms as $M' = R_\\theta M R_\\theta^\\top$, and deduce that the eigenvalues and the Harris corner response $R$ are strictly rotation invariant.</p>
<p><span class="part">(b)</span> Explain analytically why the standard Harris corner detector is NOT scale invariant. Describe how scaling an image by factor $s > 1$ can cause a genuine corner to be misclassified as an edge.</p>
<p><span class="part">(c)</span> Formulate the <strong>Harris-Laplace</strong> detector of Mikolajczyk and Schmid. Explain how scale-space extrema of the scale-normalized Laplacian $\\sigma^2 |\\nabla^2 I(\\mathbf{x}, \\sigma)|$ are combined with multi-scale Harris points to achieve true scale invariance.</p>""",
        "solution": """<p><span class="part">Part (a): Proof of Strict Rotation Invariance</span><br>
Let rotated coordinates be $\\mathbf{x}' = R_\\theta \\mathbf{x} \\iff \\mathbf{x} = R_\\theta^\\top \\mathbf{x}'$ with $R_\\theta = \\begin{pmatrix} \\cos\\theta & -\\sin\\theta \\\\ \\sin\\theta & \\cos\\theta \\end{pmatrix}$ ($R_\\theta^\\top R_\\theta = I$).<br>
1. <strong>Gradient Transformation:</strong> By the multivariate chain rule:
$$\\nabla_{\\mathbf{x}'} I' = \\left(\\frac{\\partial \\mathbf{x}}{\\partial \\mathbf{x}'}\\right)^\\top \\nabla_{\\mathbf{x}} I = (R_\\theta^\\top)^\\top \\nabla I = R_\\theta \\nabla I$$
2. <strong>Structure Tensor Transformation:</strong>
$$M' = \\sum w (\\nabla_{\\mathbf{x}'} I') (\\nabla_{\\mathbf{x}'} I')^\\top = \\sum w (R_\\theta \\nabla I) (R_\\theta \\nabla I)^\\top = R_\\theta \\left[\\sum w \\nabla I \\nabla I^\\top\\right] R_\\theta^\\top$$
<span class=\"ans\">$$M' = R_\\theta M R_\\theta^\\top$$</span>
This is an orthogonal similarity transformation.<br>
3. <strong>Invariance of Trace, Determinant, and $R$:</strong>
$$\\operatorname{trace}(M') = \\operatorname{trace}(R_\\theta M R_\\theta^\\top) = \\operatorname{trace}(R_\\theta^\\top R_\\theta M) = \\operatorname{trace}(M)$$
$$\\det(M') = \\det(R_\\theta) \\det(M) \\det(R_\\theta^\\top) = (1) \\det(M) (1) = \\det(M)$$
Since eigenvalues and $R = \\det(M) - k \\operatorname{trace}(M)^2$ depend solely on the trace and determinant:
<span class=\"ans\">$$R' = R$$</span>
The Harris corner response is <strong>strictly invariant under 2D planar rotation</strong>.</p>

<p><span class="part">Part (b): Why Harris is NOT Scale Invariant</span><br>
The structure tensor integration window $w(x, y; \\sigma_I)$ has a fixed spatial aperture:
<ul>
  <li><strong>At small scale (coarse resolution / distant object):</strong> The integration window covers both branches of a sharp $90^\\circ$ wedge. Gradient vectors point in two orthogonal directions, generating $\\lambda_1 \\gg 0, \\lambda_2 \\gg 0$ (detected as a <strong>corner</strong>).</li>
  <li><strong>At large scale (zoomed in by factor $s = 5$):</strong> The same physical window size now covers only a flat, linear segment along one of the two edges. Gradient vectors point in a single direction ($\lambda_1 \gg 0, \lambda_2 \approx 0$). The point is misclassified as an <strong>edge</strong>!</li>
</ul>
Because the window radius does not adapt to the image scale, classical Harris lacks scale invariance.</p>

<p><span class="part">Part (c): Harris-Laplace Scale-Space Formulation</span><br>
Mikolajczyk & Schmid (2004) solved this using scale-space theory:
1. <strong>Multi-Scale Structure Tensor:</strong>
$$M(\\mathbf{x}; \\sigma_I, \\sigma_D) = \\sigma_D^2 g(\\sigma_I) ** \\begin{pmatrix} I_x^2(\\sigma_D) & I_x I_y(\\sigma_D) \\\\ I_x I_y(\\sigma_D) & I_y^2(\\sigma_D) \\end{pmatrix}$$
where $\\sigma_I$ is integration scale and $\\sigma_D$ is differentiation scale ($\sigma_I = 1.4 \\sigma_D$).<br>
2. <strong>Spatial Extrema:</strong> At each discrete scale $\\sigma_n$, candidate corner locations $\\mathbf{x}_0$ are found via spatial local maxima of the multi-scale Harris measure $R(\\mathbf{x}, \\sigma_n)$.<br>
3. <strong>Scale Selection via Normalized Laplacian:</strong> Across the scale axis $\\sigma$, evaluate the scale-normalized Laplacian:
<span class=\"ans\">$$F(\\mathbf{x}_0, \\sigma) = \\sigma^2 |\\nabla^2 I(\\mathbf{x}_0, \\sigma)|$$</span>
A point is accepted as a scale-invariant corner at characteristic scale $\\sigma^*$ if and only if $\\sigma^*$ is a local maximum of $F(\\mathbf{x}_0, \\sigma)$ over neighboring scales $\\sigma_{n-1}$ and $\\sigma_{n+1}$.</p>""",
        "takeaway": "The Harris detector is strictly invariant to 2D rotation due to similarity transformation of the structure tensor M' = R M R^T. However, it lacks scale invariance; the Harris-Laplace detector achieves scale invariance by combining multi-scale Harris corners with scale-normalized Laplacian extrema σ^2 |∇^2 I|."
    }
]

def main():
    with open(PRACTICE_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    if "41591" in content:
        print("Batch 15-16 already present in practice_dip.js!")
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
    for card in PRACTICE_DIP_15_16:
        formatted = json.dumps(card, indent=4, ensure_ascii=False)
        new_cards_json.append(formatted)

    new_cards_str = ",\n".join(new_cards_json)
    
    if existing_cards_text:
        updated_cards_text = existing_cards_text + ",\n" + new_cards_str
    else:
        updated_cards_text = new_cards_str

    updated_content = f"/* Practice Questions Database for DIP (Digital Image Processing) */\nwindow.PRACTICE_DATA = window.PRACTICE_DATA || [];\n\nwindow.PRACTICE_DATA.push([\n{updated_cards_text}\n]);\n"

    with open(PRACTICE_FILE, "w", encoding="utf-8") as f:
        f.write(updated_content)

    print("Successfully added DIP Batch 15-16 (6 cards). Total in file now updated.")

if __name__ == "__main__":
    main()
