#!/usr/bin/env python3
"""
Builder script for DIP Practice Cards: Batch 09 (Topics 17 & 18)
Topic 17: Scale-Invariant Feature Transform (SIFT) (Cards 41791, 41792, 41793)
Topic 18: Bag of Visual Words Model & Spatial Pyramids (Cards 41891, 41892, 41893)
"""

import json
import os
import re

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRACTICE_FILE = os.path.join(REPO_DIR, "practice_dip.js")

PRACTICE_DIP_17_18 = [
    # =========================================================================
    # TOPIC 17: Scale-Invariant Feature Transform (SIFT)
    # =========================================================================
    {
        "id": 41791,
        "subject": "DIP",
        "topicId": "17_Scale_Invariant_Feature_Transform_SIFT",
        "topicTitle": "17 · SIFT: Scale-Invariant Features",
        "title": "Hessian Principal Curvature Ratio for Edge Response Elimination (IISc Midterm / Lowe IJCV 2004)",
        "kind2": "pyq",
        "source": "IISc Midterm / Lowe (Distinctive Image Features from Scale-Invariant Keypoints / IJCV 2004)",
        "marks": "[8 Marks]",
        "question": """<p>At an extrema candidate keypoint in Difference-of-Gaussians (DoG) scale space, the 2D discrete spatial second derivatives are evaluated as:
$$D_{xx} = 8.0, \\qquad D_{yy} = 0.5, \\qquad D_{xy} = 1.0$$</p>
<p><span class="part">(a)</span> Construct the 2D Hessian matrix $H = \\begin{pmatrix} D_{xx} & D_{xy} \\\\ D_{xy} & D_{yy} \\end{pmatrix}$, and calculate its trace $\\operatorname{Tr}(H)$ and determinant $\\operatorname{Det}(H)$.</p>
<p><span class="part">(b)</span> Formulate the principal curvature eigenvalue ratio metric $\\frac{\\operatorname{Tr}(H)^2}{\\operatorname{Det}(H)}$ in terms of eigenvalue ratio $r = \\frac{\\lambda_1}{\\lambda_2}$.</p>
<p><span class="part">(c)</span> Using Lowe's standard threshold $r_{\\text{threshold}} = 10$ (where $\\frac{(r+1)^2}{r} = 12.1$), determine whether this candidate keypoint is rejected as an unstable edge point or retained as a well-localized corner feature.</p>""",
        "solution": """<p><span class="part">Part (a): Construct Hessian Matrix & Invariants</span><br>
The 2D Hessian of the DoG image is:
<span class=\"ans\">$$H = \\begin{pmatrix} 8.0 & 1.0 \\\\ 1.0 & 0.5 \\end{pmatrix}$$</span>
Trace:
$$\\operatorname{Tr}(H) = D_{xx} + D_{yy} = 8.0 + 0.5 = <span class=\"ans\">8.5</span>$$
Determinant:
$$\\operatorname{Det}(H) = D_{xx} D_{yy} - (D_{xy})^2 = (8.0)(0.5) - (1.0)^2 = 4.0 - 1.0 = <span class=\"ans\">3.0</span>$$
Notice $\\operatorname{Det}(H) = 3.0 > 0$, confirming both eigenvalues have the same sign (an authentic local extremum, not a saddle point).</p>

<p><span class="part">Part (b): Principal Curvature Ratio Derivation</span><br>
Let $\\lambda_1$ be the larger eigenvalue and $\\lambda_2$ be the smaller eigenvalue, with ratio $r = \\lambda_1 / \\lambda_2 \\ge 1$.<br>
Trace: $\\operatorname{Tr}(H) = \\lambda_1 + \\lambda_2 = r\\lambda_2 + \\lambda_2 = (r + 1)\\lambda_2$.<br>
Determinant: $\\operatorname{Det}(H) = \\lambda_1 \\lambda_2 = r \\lambda_2^2$.<br>
Taking the ratio:
$$\\frac{\\operatorname{Tr}(H)^2}{\\operatorname{Det}(H)} = \\frac{[(r + 1)\\lambda_2]^2}{r \\lambda_2^2} = <span class=\"ans\">\\frac{(r + 1)^2}{r}</span>$$
This formula depends purely on eigenvalue ratio $r$ without requiring explicit eigenvalue computation.</p>

<p><span class="part">Part (c): Edge Rejection Decision</span><br>
Evaluating the test metric with our numerical values:
$$\\frac{\\operatorname{Tr}(H)^2}{\\operatorname{Det}(H)} = \\frac{(8.5)^2}{3.0} = \\frac{72.25}{3.0} \\approx <span class=\"ans\">24.083</span>$$
Lowe's threshold for eigenvalue ratio $r \\le 10$ is:
$$\\text{Threshold} = \\frac{(10 + 1)^2}{10} = \\frac{121}{10} = 12.1$$
Comparing:
$$\\frac{\\operatorname{Tr}(H)^2}{\\operatorname{Det}(H)} = 24.083 > 12.1$$
<span class=\"ans\">Decision: REJECTED</span>.<br>
Since $24.083 > 12.1$, the principal curvature across the feature is more than 10 times larger than along the feature ($r \\approx 22.8$). The keypoint is located along an edge ridge with poor localization along the contour direction and is discarded.</p>""",
        "takeaway": "SIFT eliminates unstable edge responses in DoG extrema by testing Tr(H)^2 / Det(H) < (r+1)^2 / r. Points with eigenvalue ratio r > 10 have ill-conditioned localization along one direction and are rejected."
    },
    {
        "id": 41792,
        "subject": "DIP",
        "topicId": "17_Scale_Invariant_Feature_Transform_SIFT",
        "topicTitle": "17 · SIFT: Scale-Invariant Features",
        "title": "Sub-Pixel & Sub-Scale Keypoint Localization via Quadratic Taylor Expansion (IIT Delhi / Brown & Lowe)",
        "kind2": "pyq",
        "source": "IIT Delhi / Brown & Lowe (Invariant Features from Interest Point Groups / BMVC 2002)",
        "marks": "[8 Marks]",
        "question": """<p>Along a discrete scale axis, Difference-of-Gaussians (DoG) responses evaluated at discrete scale indices $s \\in \\{1, 2, 3\\}$ (with uniform spacing $\\Delta s = 1$) are:
$$D(1) = 0.12, \\qquad D(2) = 0.20, \\qquad D(3) = 0.15$$</p>
<p><span class="part">(a)</span> Compute the central-difference approximations for the first derivative $\\frac{\\partial D}{\\partial s}$ and second derivative $\\frac{\\partial^2 D}{\\partial s^2}$ at center sample $s = 2$.</p>
<p><span class="part">(b)</span> Formulate the 2nd-order Taylor series expansion and calculate the continuous sub-pixel scale offset $\\hat{s} = -\\frac{D'}{D''}$. Find the exact continuous scale $s^*$.</p>
<p><span class="part">(c)</span> Compute the interpolated peak magnitude $D(s^*)$ and determine if this keypoint passes Lowe's contrast threshold $|D| \\ge 0.03$.</p>""",
        "solution": """<p><span class="part">Part (a): Compute Discrete Central Derivatives</span><br>
Using grid step $\\Delta s = 1$ at sample $s = 2$:
1. <strong>First derivative $D'(2)$:</strong>
$$D'(2) = \\frac{D(3) - D(1)}{2 \\Delta s} = \\frac{0.15 - 0.12}{2(1)} = \\frac{0.03}{2} = <span class=\"ans\">+0.015</span>$$
2. <strong>Second derivative $D''(2)$:</strong>
$$D''(2) = \\frac{D(3) - 2D(2) + D(1)}{(\\Delta s)^2} = \\frac{0.15 - 2(0.20) + 0.12}{1^2} = \\frac{0.15 - 0.40 + 0.12}{1} = <span class=\"ans\">-0.13</span>$$
Since $D''(2) < 0$, the function is concave downward, confirming a genuine maximum.</p>

<p><span class="part">Part (b): Sub-Scale Offset $\\hat{s}$ and Continuous Scale $s^*$</span><br>
Expanding $D(s)$ via 2nd-order Taylor series around $s_0 = 2$:
$$D(2 + \\hat{s}) \\approx D(2) + D'(2) \\hat{s} + \\frac{1}{2} D''(2) \\hat{s}^2$$
Differentiating with respect to $\\hat{s}$ and equating to zero:
$$\\frac{\\partial D}{\\partial \\hat{s}} = D'(2) + D''(2) \\hat{s} = 0 \\implies \\hat{s} = -\\frac{D'(2)}{D''(2)}$$
Substituting values:
<span class=\"ans\">$$\\hat{s} = -\\frac{0.015}{-0.13} = \\frac{0.015}{0.13} \\approx +0.1154$$</span>
Because $|\\hat{s}| = 0.1154 < 0.5$, the continuous extremum is verified to lie closest to sample $s=2$.<br>
The exact continuous peak scale is:
<span class=\"ans\">$$s^* = s_0 + \\hat{s} = 2 + 0.1154 = 2.1154$$</span></p>

<p><span class="part">Part (c): Interpolated Magnitude & Contrast Threshold</span><br>
Substitute $\\hat{s}$ back into the Taylor expansion:
$$D(s^*) = D(2) + D'(2) \\hat{s} + \\frac{1}{2} D''(2) \\hat{s}^2 = D(2) + \\frac{1}{2} D'(2) \\hat{s}$$
$$D(s^*) = 0.20 + \\frac{1}{2} (0.015)(0.1154) = 0.20 + 0.0008655 = <span class=\"ans\">0.20087</span>$$
<strong>Lowe's Contrast Threshold:</strong><br>
In SIFT, candidate keypoints with low contrast ($|D(s^*)| < 0.03$) are discarded as susceptible to sensor noise.<br>
Here, $|D(s^*)| = 0.20087 \\ge 0.03$. The keypoint <strong>passes with high contrast margin</strong>.</p>""",
        "takeaway": "Taylor series expansion of DoG space enables sub-pixel and sub-scale localization of keypoints (s* = s0 - D'/D'') and refines peak magnitude to eliminate unstable, low-contrast noise extrema (|D| < 0.03)."
    },
    {
        "id": 41793,
        "subject": "DIP",
        "topicId": "17_Scale_Invariant_Feature_Transform_SIFT",
        "topicTitle": "17 · SIFT: Scale-Invariant Features",
        "title": "128D SIFT Descriptor Architecture, Illumination Invariance & Nearest-Neighbor Ratio Test (Generated IISc / Stanford CS231A)",
        "kind2": "generated",
        "source": "Generated IISc Midterm / Stanford CS231A Computer Vision & Lowe (IJCV 2004)",
        "marks": "[8 Marks]",
        "question": """<p><span class="part">(a)</span> For a localized keypoint $(x_0, y_0, \\sigma)$ with canonical orientation $\\theta_0$, detail how the 128-dimensional SIFT feature vector is synthesized. Explain the role of the $16 \\times 16$ sample window, coordinate rotation by $-\\theta_0$, $4 \\times 4$ subregions, 8-bin histograms, Gaussian spatial weighting, and trilinear interpolation.</p>
<p><span class="part">(b)</span> Detail the two-step normalization pipeline ($L_2$ normalization followed by threshold clipping at $0.2$ and re-normalization) and explain how this confers robustness against affine and non-linear illumination changes.</p>
<p><span class="part">(c)</span> In nearest-neighbor feature matching, define Lowe's Ratio Test $\\frac{D_1}{D_2} \\le \\tau$. Explain why a simple Euclidean distance threshold $D_1 \\le \\epsilon$ fails on real-world scenes. Given query distances $D_1 = 0.42$ and $D_2 = 0.45$, determine if this match is accepted or rejected under $\\tau = 0.8$.</p>""",
        "solution": """<p><span class="part">Part (a): 128D SIFT Descriptor Synthesis</span><br>
1. <strong>Canonical Coordinate Rotation:</strong> The sample coordinates around $(x_0, y_0)$ in a $16 \\times 16$ patch (at scale $\\sigma$) are rotated by $-\\theta_0$ so that all spatial measurements align with the keypoint's dominant orientation, ensuring <strong>rotation invariance</strong>.<br>
2. <strong>Subregion Partitioning:</strong> The $16 \\times 16$ pixel region is divided into a $4 \\times 4$ grid of spatial subregions ($4 \\times 4$ sample points per subregion).<br>
3. <strong>8-Bin Orientation Histograms:</strong> In each subregion, local gradient orientations are binned into 8 angular directions ($360^\\circ / 8 = 45^\\circ$ bins). Each gradient vote is weighted by its magnitude $M$ and a Gaussian circular window centered at the keypoint with $\\sigma = 0.5 \\times 16 = 8$.<br>
4. <strong>Trilinear Interpolation:</strong> To avoid boundary discretization artifacts, each gradient vote is distributed smoothly across adjacent spatial subregions and orientation bins via linear interpolation in $x$, $y$, and $\\theta$.<br>
<span class=\"ans\">Total vector length: $4 \\times 4 \\text{ subregions} \\times 8 \\text{ bins} = 128 \\text{ dimensions}$.</span></p>

<p><span class="part">Part (b): Illumination Invariance Pipeline</span><br>
Illumination variations are addressed in two stages:
1. <strong>$L_2$ Normalization:</strong> $\\mathbf{f} \\leftarrow \\mathbf{f} / \\|\\mathbf{f}\\|_2$. Since a uniform contrast change multiplies all image gradients by constant $\\alpha$ ($I \\to \\alpha I \\implies \\nabla I \\to \\alpha \\nabla I$), normalizing by Euclidean norm cancels $\\alpha$, achieving <strong>complete contrast invariance</strong>. Additive brightness offsets ($I \\to I + \\beta$) are eliminated at the outset by derivative computation.<br>
2. <strong>Clipping at $0.2$ and Re-normalization:</strong> Non-linear illumination changes (such as specular reflections, sensor saturation, and 3D surface orientation shifts under directional light) cause large spikes in a few gradient bins without affecting others. Clamping all elements to $\\min(f_i, 0.2)$ and re-normalizing prevents dominant specular highlights from overpowering the descriptor.</p>

<p><span class="part">Part (c): Lowe's Ratio Test vs. Absolute Distance</span><br>
Let $D_1 = \\|\\mathbf{q} - \\mathbf{m}_1\\|_2$ be distance to closest match and $D_2 = \\|\\mathbf{q} - \\mathbf{m}_2\\|_2$ be distance to second closest match.<br>
<span class=\"ans\">Lowe's Ratio Test: $\\frac{D_1}{D_2} \\le \\tau = 0.8$.</span><br>
<strong>Why Absolute Threshold Fails:</strong><br>
In high-dimensional feature space, background regions containing repetitive textures (e.g. grass, foliage, brick patterns) create dense clusters of false matches that have small absolute distances $D_1 < \\epsilon$. Conversely, distinctive keypoints under heavy perspective distortion may have larger $D_1 > \\epsilon$. The ratio $D_1 / D_2$ measures <strong>relative distinctiveness</strong>: an authentic match has no close competitor ($D_1 \\ll D_2$), whereas ambiguous/repetitive features have $D_1 \\approx D_2$.<br>
<strong>Numerical Evaluation:</strong><br>
Given $D_1 = 0.42$ and $D_2 = 0.45$:
$$\\text{Ratio} = \\frac{D_1}{D_2} = \\frac{0.42}{0.45} \\approx <span class=\"ans\">0.9333</span>$$
Since $0.9333 > 0.8$, the match is ambiguous (a near-tie between two unrelated candidates) and is <span class=\"ans\">REJECTED</span>.</p>""",
        "takeaway": "SIFT descriptors assemble 128 dimensions (4x4 spatial grid x 8 orientation bins) with trilinear interpolation and saturation clipping (0.2). Lowe's ratio test D1/D2 <= 0.8 filters out 90% of false matches from repetitive textures while preserving distinctive features."
    },

    # =========================================================================
    # TOPIC 18: Bag of Visual Words (BoVW) & Spatial Pyramids
    # =========================================================================
    {
        "id": 41891,
        "subject": "DIP",
        "topicId": "18_Bag_of_Visual_Words_Model",
        "topicTitle": "18 · BoVW & Spatial Pyramids",
        "title": "K-Means Visual Vocabulary Quantization & Histogram Normalization (IISc Midterm / Csurka ECCV 2004)",
        "kind2": "pyq",
        "source": "IISc Midterm / Csurka et al. (Visual Categorization with Bags of Keypoints / ECCV 2004)",
        "marks": "[8 Marks]",
        "question": """<p>A learned visual vocabulary consists of $K = 3$ cluster centroids in $\\mathbb{R}^2$:
$$\\mathbf{c}_1 = (0, 0), \\qquad \\mathbf{c}_2 = (3, 4), \\qquad \\mathbf{c}_3 = (6, 0)$$
An input image contains 4 extracted feature vectors:
$$\\mathbf{x}_1 = (1, 1), \\quad \\mathbf{x}_2 = (2, 3), \\quad \\mathbf{x}_3 = (5, 1), \\quad \\mathbf{x}_4 = (0.5, 0)$$</p>
<p><span class="part">(a)</span> Quantize each feature descriptor to its nearest visual word index using Euclidean distance.</p>
<p><span class="part">(b)</span> Construct the unnormalized visual word histogram $\\mathbf{h} = [h_1, h_2, h_3]^\\top$.</p>
<p><span class="part">(c)</span> Compute the normalized bag-of-words histograms under both $L_1$ norm and $L_2$ norm.</p>""",
        "solution": """<p><span class="part">Part (a): Euclidean Distance Quantization</span><br>
Compute squared distance $d^2(\\mathbf{x}_i, \\mathbf{c}_k) = \\|\\mathbf{x}_i - \\mathbf{c}_k\\|^2$:
1. <strong>For $\\mathbf{x}_1 = (1, 1)$:</strong >
<ul>
  <li>$d^2(\\mathbf{x}_1, \\mathbf{c}_1) = (1-0)^2 + (1-0)^2 = 1 + 1 = 2$</li>
  <li>$d^2(\\mathbf{x}_1, \\mathbf{c}_2) = (1-3)^2 + (1-4)^2 = 4 + 9 = 13$</li>
  <li>$d^2(\\mathbf{x}_1, \\mathbf{c}_3) = (1-6)^2 + (1-0)^2 = 25 + 1 = 26$</li>
  <li>Closest is $\\mathbf{c}_1 \\implies <span class=\"ans\">w_1 = 1</span>$</li>
</ul>
2. <strong>For $\\mathbf{x}_2 = (2, 3)$:</strong >
<ul>
  <li>$d^2(\\mathbf{x}_2, \\mathbf{c}_1) = 2^2 + 3^2 = 4 + 9 = 13$</li>
  <li>$d^2(\\mathbf{x}_2, \\mathbf{c}_2) = (2-3)^2 + (3-4)^2 = 1 + 1 = 2$</li>
  <li>$d^2(\\mathbf{x}_2, \\mathbf{c}_3) = (2-6)^2 + 3^2 = 16 + 9 = 25$</li>
  <li>Closest is $\\mathbf{c}_2 \\implies <span class=\"ans\">w_2 = 2</span>$</li>
</ul>
3. <strong>For $\\mathbf{x}_3 = (5, 1)$:</strong >
<ul>
  <li>$d^2(\\mathbf{x}_3, \\mathbf{c}_1) = 25 + 1 = 26$</li>
  <li>$d^2(\\mathbf{x}_3, \\mathbf{c}_2) = (5-3)^2 + (1-4)^2 = 4 + 9 = 13$</li>
  <li>$d^2(\\mathbf{x}_3, \\mathbf{c}_3) = (5-6)^2 + (1-0)^2 = 1 + 1 = 2$</li>
  <li>Closest is $\\mathbf{c}_3 \\implies <span class=\"ans\">w_3 = 3</span>$</li>
</ul>
4. <strong>For $\\mathbf{x}_4 = (0.5, 0)$:</strong >
<ul>
  <li>$d^2(\\mathbf{x}_4, \\mathbf{c}_1) = 0.5^2 + 0^2 = 0.25$</li>
  <li>$d^2(\\mathbf{x}_4, \\mathbf{c}_2) = (0.5-3)^2 + (-4)^2 = 6.25 + 16 = 22.25$</li>
  <li>$d^2(\\mathbf{x}_4, \\mathbf{c}_3) = (0.5-6)^2 + 0^2 = 30.25$</li>
  <li>Closest is $\\mathbf{c}_1 \\implies <span class=\"ans\">w_4 = 1</span>$</li>
</ul></p>

<p><span class="part">Part (b): Unnormalized Bag-of-Words Histogram</span><br>
Counting visual word assignments:
- Word 1 assigned to $\\mathbf{x}_1$ and $\\mathbf{x}_4 \\implies h_1 = 2$.
- Word 2 assigned to $\\mathbf{x}_2 \\implies h_2 = 1$.
- Word 3 assigned to $\\mathbf{x}_3 \\implies h_3 = 1$.
The raw visual word frequency histogram is:
<span class=\"ans\">$$\\mathbf{h} = \\begin{pmatrix} 2 \\\\ 1 \\\\ 1 \\end{pmatrix}$$</span></p>

<p><span class="part">Part (c): Histogram Normalization</span><br>
1. <strong>$L_1$ Normalization (Probability Distribution):</strong>
$$\\|\\mathbf{h}\\|_1 = 2 + 1 + 1 = 4$$
<span class=\"ans\">$$\\mathbf{h}_{L_1} = \\frac{1}{4} \\begin{pmatrix} 2 \\\\ 1 \\\\ 1 \\end{pmatrix} = \\begin{pmatrix} 0.50 \\\\ 0.25 \\\\ 0.25 \\end{pmatrix}$$</span>
2. <strong>$L_2$ Normalization (Cosine Similarity / Unit Sphere):</strong>
$$\\|\\mathbf{h}\\|_2 = \\sqrt{2^2 + 1^2 + 1^2} = \\sqrt{4 + 1 + 1} = \\sqrt{6} \\approx 2.4495$$
<span class=\"ans\">$$\\mathbf{h}_{L_2} = \\begin{pmatrix} 2/\\sqrt{6} \\\\ 1/\\sqrt{6} \\\\ 1/\\sqrt{6} \\end{pmatrix} \\approx \\begin{pmatrix} 0.8165 \\\\ 0.4082 \\\\ 0.4082 \\end{pmatrix}$$</span></p>""",
        "takeaway": "Bag of Visual Words (BoVW) maps high-dimensional descriptors to discrete visual vocabulary centroids via nearest neighbor quantization, forming fixed-length frequency histograms that are normalized under L1 or L2 norms."
    },
    {
        "id": 41892,
        "subject": "DIP",
        "topicId": "18_Bag_of_Visual_Words_Model",
        "topicTitle": "18 · BoVW & Spatial Pyramids",
        "title": "TF-IDF Weighting in Visual Search & Stop-Word Down-Weighting (IIT Delhi / Sivic & Zisserman)",
        "kind2": "pyq",
        "source": "IIT Delhi / Sivic & Zisserman (Video Google: A Text Retrieval Approach / ICCV 2003)",
        "marks": "[8 Marks]",
        "question": """<p>An image database contains $N = 10,000$ indexed frames.
<ul>
  <li>Visual word $w_1$ (ubiquitous texture, e.g. blue sky) occurs in $N_1 = 8,000$ database frames.</li>
  <li>Visual word $w_2$ (distinctive product logo corner) occurs in only $N_2 = 20$ database frames.</li>
</ul>
In a query image containing $n_d = 100$ total detected visual words, word $w_1$ appears $n_1 = 40$ times, while word $w_2$ appears $n_2 = 5$ times.</p>
<p><span class="part">(a)</span> Compute the Inverse Document Frequency (IDF) $\\operatorname{idf}_i = \\ln(N / N_i)$ for both visual words.</p>
<p><span class="part">(b)</span> Calculate the Term Frequency-Inverse Document Frequency (TF-IDF) weight $t_i = \\left(\\frac{n_i}{n_d}\\right) \\operatorname{idf}_i$ for each word.</p>
<p><span class="part">(c)</span> Compare the ratio of final TF-IDF weights $t_2 / t_1$ to the raw count ratio $n_2 / n_1$, and explain how TF-IDF naturally eliminates visual 'stop-words'.</p>""",
        "solution": """<p><span class="part">Part (a): Inverse Document Frequency (IDF) Calculation</span><br>
Total documents $N = 10,000$:
1. <strong>For common word $w_1$ ($N_1 = 8,000$):</strong>
$$\\operatorname{idf}_1 = \\ln\\left(\\frac{10,000}{8,000}\\right) = \\ln(1.25) \\approx <span class=\"ans\">0.2231</span>$$
2. <strong>For rare word $w_2$ ($N_2 = 20$):</strong>
$$\\operatorname{idf}_2 = \\ln\\left(\\frac{10,000}{20}\\right) = \\ln(500) \\approx <span class=\"ans\">6.2146</span>$$
The rare word has an IDF weight nearly <strong>28 times higher</strong> ($6.2146 / 0.2231 \\approx 27.85$) than the ubiquitous word.</p>

<p><span class="part">Part (b): TF-IDF Weight Calculation</span><br>
Term frequencies in query:
$$\\text{tf}_1 = \\frac{n_1}{n_d} = \\frac{40}{100} = 0.40, \\qquad \\text{tf}_2 = \\frac{n_2}{n_d} = \\frac{5}{100} = 0.05$$
Computing TF-IDF weights:
$$t_1 = \\text{tf}_1 \\times \\operatorname{idf}_1 = 0.40 \\times 0.2231 \\approx <span class=\"ans\">0.0892</span>$$
$$t_2 = \\text{tf}_2 \\times \\operatorname{idf}_2 = 0.05 \\times 6.2146 \\approx <span class=\"ans\">0.3107</span>$$</p>

<p><span class="part">Part (c): Weight Ratio & Visual Stop-Word Elimination</span><br>
Comparing the ratios:
- Raw frequency ratio: $\\frac{n_2}{n_1} = \\frac{5}{40} = 0.125$ ($w_1$ is 8 times more frequent than $w_2$).
- TF-IDF weight ratio:
<span class=\"ans\">$$\\frac{t_2}{t_1} = \\frac{0.3107}{0.0892} \\approx 3.48$$</span>
<strong>Retrieval Impact:</strong><br>
Despite appearing 8 times less frequently, the rare logo feature $w_2$ is assigned a TF-IDF score <strong>3.5 times higher</strong> than $w_1$.<br>
In large-scale image retrieval, ubiquitous background textures (clear sky, flat road surfaces, water) act as visual 'stop-words'. Because they appear in nearly every image, their IDF approaches zero ($\ln(1) = 0$). TF-IDF automatically suppresses these non-discriminative background features while strongly boosting rare, category-defining visual tokens.</p>""",
        "takeaway": "TF-IDF weighting in visual search suppresses ubiquitous visual 'stop-words' (sky, ground) whose IDF ≈ 0, while amplifying rare, distinctive visual patterns (logos, unique corners) by logarithmic document frequency idf = ln(N / Ni)."
    },
    {
        "id": 41893,
        "subject": "DIP",
        "topicId": "18_Bag_of_Visual_Words_Model",
        "topicTitle": "18 · BoVW & Spatial Pyramids",
        "title": "Spatial Pyramid Matching (SPM) Architecture & Mercer Kernel Proof (Generated IISc / Lazebnik Benchmark)",
        "kind2": "generated",
        "source": "Generated IISc Midterm / Lazebnik, Schmid, Ponce (CVPR 2006) & Barla-Verri (2003)",
        "marks": "[8 Marks]",
        "question": """<p><span class="part">(a)</span> Explain how the <strong>Spatial Pyramid Matching (SPM)</strong> framework of Lazebnik et al. overcomes the standard bag-of-words orderless assumption. For pyramid levels $L=0$ ($1 \\times 1$ global image) and $L=1$ ($2 \\times 2$ quadrants), formulate the pyramid match kernel $\\kappa(A, B) = \\frac{1}{2} \\mathcal{I}_0 + \\frac{1}{2} \\mathcal{I}_1$.</p>
<p><span class="part">(b)</span> Two images $A$ and $B$ have vocabulary size $K = 2$.
Level 0 histograms: $H_A^0 = [4, 4]$, $H_B^0 = [6, 2]$.
Level 1 quadrant histograms ($q \\in \\{1, 2, 3, 4\\}$):
$H_A^{1, 1} = [1, 1], H_B^{1, 1} = [2, 0]$; $H_A^{1, 2} = [1, 1], H_B^{1, 2} = [1, 1]$; $H_A^{1, 3} = [1, 1], H_B^{1, 3} = [2, 0]$; $H_A^{1, 4} = [1, 1], H_B^{1, 4} = [1, 1]$.
Compute $\\mathcal{I}_0$, $\\mathcal{I}_1$, and the total kernel value $\\kappa(A, B)$.</p>
<p><span class="part">(c)</span> Prove rigorously that the 1D histogram intersection function $k(x, y) = \\min(x, y)$ is a positive semi-definite Mercer kernel for $x, y \\ge 0$, and deduce that multi-dimensional histogram intersection $K(\\mathbf{x}, \\mathbf{y}) = \\sum_{i=1}^K \\min(x_i, y_i)$ is valid for Support Vector Machines (SVM).</p>""",
        "solution": """<p><span class="part">Part (a): Spatial Pyramid Matching (SPM) Architecture</span><br>
Standard BoVW collapses an image into a single global histogram, completely discarding spatial layout (an image of the sky at top and grass at bottom yields the identical BoVW representation as grass at top and sky at bottom).<br>
Lazebnik et al. partition the image space into increasingly finer grids at levels $l = 0, 1, \\dots, L$, where level $l$ contains $4^l$ cells.<br>
Let $\\mathcal{I}_l$ be the sum of histogram intersections across all cells at level $l$. The pyramid match kernel assigns higher weights to matches occurring at finer spatial resolutions:
<span class=\"ans\">$$\\kappa_L(A, B) = \\frac{1}{2^L} \\mathcal{I}_0 + \\sum_{l=1}^L \\frac{1}{2^{L-l+1}} \\mathcal{I}_l$$</span>
For $L = 1$: $\\kappa(A, B) = \\frac{1}{2} \\mathcal{I}_0 + \\frac{1}{2} \\mathcal{I}_1$.</p>

<p><span class="part">Part (b): Numerical SPM Kernel Evaluation</span><br>
1. <strong>Level 0 Intersection $\\mathcal{I}_0$ ($1 \\times 1$ global image):</strong>
$$\\mathcal{I}_0 = \\min(4, 6) + \\min(4, 2) = 4 + 2 = <span class=\"ans\">6</span>$$
2. <strong>Level 1 Intersection $\\mathcal{I}_1$ (sum of 4 quadrants):</strong>
<ul>
  <li>Quadrant 1: $\\min(1, 2) + \\min(1, 0) = 1 + 0 = 1$</li>
  <li>Quadrant 2: $\\min(1, 1) + \\min(1, 1) = 1 + 1 = 2$</li>
  <li>Quadrant 3: $\\min(1, 2) + \\min(1, 0) = 1 + 0 = 1$</li>
  <li>Quadrant 4: $\\min(1, 1) + \\min(1, 1) = 1 + 1 = 2$</li>
</ul>
$$\\mathcal{I}_1 = 1 + 2 + 1 + 2 = <span class=\"ans\">6</span>$$
3. <strong>Total SPM Kernel Value:</strong>
$$\\kappa(A, B) = \\frac{1}{2} \\mathcal{I}_0 + \\frac{1}{2} \\mathcal{I}_1 = \\frac{1}{2}(6) + \\frac{1}{2}(6) = 3 + 3 = <span class=\"ans\">6</span>$$</p>

<p><span class="part">Part (c): Proof of Positive Semi-Definiteness (Mercer Kernel)</span><br>
1. <strong>Integral Representation of $\\min(x, y)$ for $x, y \\ge 0$:</strong>
Notice that $\\min(x, y)$ can be written as an inner product of indicator step functions on $[0, \\infty)$:
$$\\min(x, y) = \\int_0^\\infty \\mathbf{1}_{\\{t \\le x\\}} \\mathbf{1}_{\\{t \\le y\\}} dt$$
2. <strong>Quadratic Form for Arbitrary $\{c_i\}_{i=1}^N \\subset \\mathbb{R}$:</strong>
$$\\sum_{i=1}^N \\sum_{j=1}^N c_i c_j k(x_i, x_j) = \\sum_{i=1}^N \\sum_{j=1}^N c_i c_j \\int_0^\\infty \\mathbf{1}_{\\{t \\le x_i\\}} \\mathbf{1}_{\\{t \\le x_j\\}} dt$$
$$= \\int_0^\\infty \\left( \\sum_{i=1}^N c_i \\mathbf{1}_{\\{t \\le x_i\\}} \\right) \\left( \\sum_{j=1}^N c_j \\mathbf{1}_{\\{t \\le x_j\\}} \\right) dt = \\int_0^\\infty \\left| \\sum_{i=1}^N c_i \\mathbf{1}_{\\{t \\le x_i\\}} \\right|^2 dt \\ge 0$$
Because the integral of a squared real-valued function is always non-negative, $k(x, y) = \\min(x, y)$ is strictly positive semi-definite.<br>
3. <strong>Multi-Dimensional Extension:</strong>
$$K(\\mathbf{x}, \\mathbf{y}) = \\sum_{m=1}^K \\min(x_m, y_m) = \\sum_{m=1}^K k(x_m, y_m)$$
The sum of Mercer kernels is a valid Mercer kernel. Thus $K(\\mathbf{x}, \\mathbf{y})$ guarantees that any kernel SVM classifier has a convex objective with a unique global optimum.</p>""",
        "takeaway": "Spatial Pyramid Matching (SPM) restores spatial geometry to BoVW by hierarchically partitioning images and weighting fine-grid histogram matches. The histogram intersection kernel K(x, y) = sum min(xi, yi) is proven to be a valid Mercer kernel via indicator integral representation."
    }
]

def main():
    with open(PRACTICE_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    if "41791" in content:
        print("Batch 17-18 already present in practice_dip.js!")
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
    for card in PRACTICE_DIP_17_18:
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

    print("Successfully added DIP Batch 17-18 (6 cards). Total in file now updated.")

if __name__ == "__main__":
    main()
