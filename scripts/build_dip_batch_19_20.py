#!/usr/bin/env python3
"""
Builder script for DIP Practice Cards: Batch 10 (Topics 19 & 20)
Topic 19: Face Recognition: Eigenfaces and Viola-Jones (Cards 41991, 41992, 41993)
Topic 20: Deep Learning and CNN Architectures for Images (Cards 42091, 42092, 42093)
"""

import json
import os
import re

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRACTICE_FILE = os.path.join(REPO_DIR, "practice_dip.js")

PRACTICE_DIP_19_20 = [
    # =========================================================================
    # TOPIC 19: Face Recognition: Eigenfaces and Viola-Jones
    # =========================================================================
    {
        "id": 41991,
        "subject": "DIP",
        "topicId": "19_Face_Recognition_Eigenfaces_and_Viola_Jones",
        "topicTitle": "19 · Face: Eigenfaces & Viola-Jones",
        "title": "Snapshot Eigenfaces Derivation & Subspace Projection (IISc Midterm / Turk & Pentland)",
        "kind2": "pyq",
        "source": "IISc Midterm / Turk & Pentland (Eigenfaces for Recognition / J. Cognitive Neuroscience 1991)",
        "marks": "[8 Marks]",
        "question": """<p>Suppose we have $M = 2$ training face image vectors of dimension $D = 4$:
$$\\boldsymbol{\\Gamma}_1 = \\begin{pmatrix} 10 \\\\ 20 \\\\ 10 \\\\ 20 \\end{pmatrix}, \\qquad \\boldsymbol{\\Gamma}_2 = \\begin{pmatrix} 20 \\\\ 10 \\\\ 20 \\\\ 10 \\end{pmatrix}$$</p>
<p><span class="part">(a)</span> Compute the mean face vector $\\boldsymbol{\\Psi}$ and construct the mean-centered data matrix $A = [\\boldsymbol{\\Phi}_1, \\boldsymbol{\\Phi}_2] \\in \\mathbb{R}^{4 \\times 2}$.</p>
<p><span class="part">(b)</span> Rather than computing the intractable $4 \\times 4$ covariance matrix $C = A A^\\top$, compute the $2 \\times 2$ snapshot matrix $L = A^\\top A$. Find its non-zero eigenvalue $\\lambda_1$ and its normalized eigenvector $\\mathbf{v}_1$.</p>
<p><span class="part">(c)</span> Using the snapshot identity $\\mathbf{u}_1 = \\frac{A \\mathbf{v}_1}{\\sqrt{\\lambda_1}}$, compute the primary Eigenface $\\mathbf{u}_1 \\in \\mathbb{R}^4$ and verify that it has unit $L_2$ norm.</p>""",
        "solution": """<p><span class="part">Part (a): Mean Face & Mean-Centered Matrix $A$</span><br>
The mean face vector is:
$$\\boldsymbol{\\Psi} = \\frac{1}{2}(\\boldsymbol{\\Gamma}_1 + \\boldsymbol{\\Gamma}_2) = \\frac{1}{2} \\begin{pmatrix} 10 + 20 \\\\ 20 + 10 \\\\ 10 + 20 \\\\ 20 + 10 \\end{pmatrix} = <span class=\"ans\">\\begin{pmatrix} 15 \\\\ 15 \\\\ 15 \\\\ 15 \\end{pmatrix}</span>$$
Mean-centered vectors $\\boldsymbol{\\Phi}_i = \\boldsymbol{\\Gamma}_i - \\boldsymbol{\\Psi}$:
$$\\boldsymbol{\\Phi}_1 = \\begin{pmatrix} 10 - 15 \\\\ 20 - 15 \\\\ 10 - 15 \\\\ 20 - 15 \\end{pmatrix} = \\begin{pmatrix} -5 \\\\ 5 \\\\ -5 \\\\ 5 \\end{pmatrix}, \\qquad \\boldsymbol{\\Phi}_2 = \\begin{pmatrix} 20 - 15 \\\\ 10 - 15 \\\\ 20 - 15 \\\\ 10 - 15 \\end{pmatrix} = \\begin{pmatrix} 5 \\\\ -5 \\\\ 5 \\\\ -5 \\end{pmatrix}$$
The centered data matrix $A$ is:
<span class=\"ans\">$$A = \\begin{pmatrix} -5 & 5 \\\\ 5 & -5 \\\\ -5 & 5 \\\\ 5 & -5 \\end{pmatrix} \\in \\mathbb{R}^{4 \\times 2}$$</span></p>

<p><span class="part">Part (b): Snapshot Matrix $L = A^\\top A$ and Eigensystem</span><br>
Compute inner products of columns of $A$:
$$L_{11} = \\boldsymbol{\\Phi}_1^\\top \\boldsymbol{\\Phi}_1 = (-5)^2 + 5^2 + (-5)^2 + 5^2 = 25 + 25 + 25 + 25 = 100$$
$$L_{22} = \\boldsymbol{\\Phi}_2^\\top \\boldsymbol{\\Phi}_2 = 100$$
$$L_{12} = L_{21} = \\boldsymbol{\\Phi}_1^\\top \\boldsymbol{\\Phi}_2 = (-5)(5) + (5)(-5) + (-5)(5) + (5)(-5) = -100$$
Thus the $2 \\times 2$ snapshot matrix is:
<span class=\"ans\">$$L = A^\\top A = \\begin{pmatrix} 100 & -100 \\\\ -100 & 100 \\end{pmatrix}$$</span>
Eigenvalues of $L$:
$$\\det(L - \\lambda I) = (100 - \\lambda)^2 - (-100)^2 = \\lambda^2 - 200\\lambda = 0 \\implies <span class=\"ans\">\\lambda_1 = 200, \\quad \\lambda_2 = 0</span>$$
Eigenvector $\\mathbf{v}_1$ corresponding to $\\lambda_1 = 200$:
$$(L - 200 I)\\mathbf{v}_1 = \\begin{pmatrix} -100 & -100 \\\\ -100 & -100 \\end{pmatrix} \\begin{pmatrix} v_{11} \\\\ v_{12} \\end{pmatrix} = 0 \\implies v_{11} + v_{12} = 0$$
Normalizing to unit length $\\|\\mathbf{v}_1\\| = 1$:
<span class=\"ans\">$$\\mathbf{v}_1 = \\frac{1}{\\sqrt{2}} \\begin{pmatrix} 1 \\\\ -1 \\end{pmatrix}$$</span></p>

<p><span class="part">Part (c): Primary Eigenface $\\mathbf{u}_1$</span><br>
Using the Turk-Pentland snapshot theorem ($A A^\\top (A \\mathbf{v}) = A (A^\\top A \\mathbf{v}) = \\lambda (A \\mathbf{v})$):
$$\\mathbf{u}_1 = \\frac{A \\mathbf{v}_1}{\\sqrt{\\lambda_1}}$$
Multiply $A \\mathbf{v}_1$:
$$A \\mathbf{v}_1 = \\frac{1}{\\sqrt{2}} \\begin{pmatrix} -5 & 5 \\\\ 5 & -5 \\\\ -5 & 5 \\\\ 5 & -5 \\end{pmatrix} \\begin{pmatrix} 1 \\\\ -1 \\end{pmatrix} = \\frac{1}{\\sqrt{2}} \\begin{pmatrix} -10 \\\\ 10 \\\\ -10 \\\\ 10 \\end{pmatrix}$$
Scale by $\\frac{1}{\\sqrt{\\lambda_1}} = \\frac{1}{\\sqrt{200}} = \\frac{1}{10\\sqrt{2}}$:
$$\\mathbf{u}_1 = \\frac{1}{10\\sqrt{2}} \\cdot \\frac{1}{\\sqrt{2}} \\begin{pmatrix} -10 \\\\ 10 \\\\ -10 \\\\ 10 \\end{pmatrix} = \\frac{1}{20} \\begin{pmatrix} -10 \\\\ 10 \\\\ -10 \\\\ 10 \\end{pmatrix} = <span class=\"ans\">\\begin{pmatrix} -0.5 \\\\ 0.5 \\\\ -0.5 \\\\ 0.5 \\end{pmatrix}</span>$$
<strong>Unit Norm Verification:</strong>
$$\\|\\mathbf{u}_1\\|^2 = (-0.5)^2 + (0.5)^2 + (-0.5)^2 + (0.5)^2 = 0.25 + 0.25 + 0.25 + 0.25 = 1.0$$
The principal Eigenface $\\mathbf{u}_1$ captures 100% of the variance in this 2-face training set.</p>""",
        "takeaway": "The snapshot method solves the high-dimensional PCA problem for image vectors (D >> M) by finding eigenvectors of the small M x M Gram matrix L = A^T A, mapping them to full Eigenfaces via u = A v / sqrt(lambda)."
    },
    {
        "id": 41992,
        "subject": "DIP",
        "topicId": "19_Face_Recognition_Eigenfaces_and_Viola_Jones",
        "topicTitle": "19 · Face: Eigenfaces & Viola-Jones",
        "title": "Integral Image Construction & Constant-Time O(1) Box Filtering (IIT Delhi / Viola & Jones)",
        "kind2": "pyq",
        "source": "IIT Delhi / Viola & Jones (Rapid Object Detection using a Boosted Cascade of Simple Features / CVPR 2001)",
        "marks": "[8 Marks]",
        "question": """<p>A $4 \\times 4$ grayscale image patch $I(x, y)$ is given by:
$$I = \\begin{pmatrix} 1 & 2 & 3 & 4 \\\\ 2 & 3 & 4 & 5 \\\\ 3 & 4 & 5 & 6 \\\\ 4 & 5 & 6 & 7 \\end{pmatrix}$$</p>
<p><span class="part">(a)</span> Construct the complete $4 \\times 4$ Integral Image $I_{\\text{int}}(x, y) = \\sum_{x' \\le x, y' \\le y} I(x', y')$ using dynamic programming.</p>
<p><span class="part">(b)</span> Using the four-corner lookup formula on $I_{\\text{int}}$, compute the sum of image pixels inside the interior $2 \\times 2$ rectangular sub-window covering rows $2$ to $3$ and columns $2$ to $3$ ($I(2:3, 2:3) = \\begin{pmatrix} 3 & 4 \\\\ 4 & 5 \\end{pmatrix}$).</p>
<p><span class="part">(c)</span> Verify the result by direct pixel summation and contrast the asymptotic computational complexity $\\mathcal{O}(1)$ of evaluating Haar-like features via integral images against spatial 2D convolution.</p>""",
        "solution": """<p><span class="part">Part (a): Dynamic Programming Construction of Integral Image</span><br>
Using the cumulative prefix recurrence:
$$s(x, y) = s(x, y-1) + I(x, y) \\quad (\\text{cumulative row sum})$$
$$I_{\\text{int}}(x, y) = I_{\\text{int}}(x-1, y) + s(x, y)$$
Computing row by row (1-indexed):
<ul>
  <li><strong>Row 1:</strong> $[1, \\; 1+2=3, \\; 3+3=6, \\; 6+4=10]$</li>
  <li><strong>Row 2:</strong>
    <ul>
      <li>$(2, 1): 1 + 2 = 3$</li>
      <li>$(2, 2): 3 + 8 - 1 + 3 = 8$</li>
      <li>$(2, 3): 6 + 15 - 3 = 15$</li>
      <li>$(2, 4): 10 + 24 - 6 = 24$</li>
    </ul>
    <em>Row 2:</em> $[3, 8, 15, 24]$
  </li>
  <li><strong>Row 3:</strong>
    <ul>
      <li>$(3, 1): 3 + 3 = 6$</li>
      <li>$(3, 2): 8 + 6 + 4 - 3 = 15$</li>
      <li>$(3, 3): 15 + 15 + 5 - 8 = 27$</li>
      <li>$(3, 4): 24 + 27 + 6 - 15 = 42$</li>
    </ul>
    <em>Row 3:</em> $[6, 15, 27, 42]$
  </li>
  <li><strong>Row 4:</strong>
    <ul>
      <li>$(4, 1): 6 + 4 = 10$</li>
      <li>$(4, 2): 15 + 10 + 5 - 6 = 24$</li>
      <li>$(4, 3): 27 + 24 + 6 - 15 = 42$</li>
      <li>$(4, 4): 42 + 42 + 7 - 27 = 64$</li>
    </ul>
    <em>Row 4:</em> $[10, 24, 42, 64]$
  </li>
</ul>
The complete Integral Image is:
<span class=\"ans\">$$I_{\\text{int}} = \\begin{pmatrix} 1 & 3 & 6 & 10 \\\\ 3 & 8 & 15 & 24 \\\\ 6 & 15 & 27 & 42 \\\\ 10 & 24 & 42 & 64 \\end{pmatrix}$$</span></p>

<p><span class="part">Part (b): Four-Corner Box Sum Evaluation</span><br>
To sum pixels in rectangle $[r_1:r_2, c_1:c_2]$ where $r_1=2, r_2=3, c_1=2, c_2=3$:
Identify the 4 bounding integral coordinates:
<ul>
  <li>Bottom-Right $D = I_{\\text{int}}(3, 3) = 27$</li>
  <li>Top-Right $B = I_{\\text{int}}(r_1-1, c_2) = I_{\\text{int}}(1, 3) = 6$</li>
  <li>Bottom-Left $C = I_{\\text{int}}(r_2, c_1-1) = I_{\\text{int}}(3, 1) = 6$</li>
  <li>Top-Left $A = I_{\\text{int}}(r_1-1, c_1-1) = I_{\\text{int}}(1, 1) = 1$</li>
</ul>
Applying the inclusion-exclusion formula:
$$\\text{Sum} = D - B - C + A = 27 - 6 - 6 + 1 = <span class=\"ans\">16</span>$$</p>

<p><span class="part">Part (c): Verification & Complexity Comparison</span><br>
Direct addition:
$$\\sum = I(2, 2) + I(2, 3) + I(3, 2) + I(3, 3) = 3 + 4 + 4 + 5 = <span class=\"ans\">16</span>$$
The results match identically.<br>
<strong>Complexity Advantage:</strong><br>
- <strong>Direct Convolution:</strong> Summing an arbitrary $W \\times H$ rectangle requires $\\mathcal{O}(W \\times H)$ operations (e.g. a $40 \\times 40$ window requires $1,600$ additions per location).<br>
- <strong>Integral Image Lookup:</strong> Any rectangular sum is computed using <strong>exactly 4 array lookups and 3 arithmetic operations ($\\mathcal{O}(1)$ time)</strong>, regardless of whether the rectangle is $2 \\times 2$ or $200 \\times 200$. This enables evaluating hundreds of thousands of multi-scale Haar features in real time (over 15 fps in 2001).</p>""",
        "takeaway": "The Integral Image allows computing the sum of pixels in any arbitrary rectangle with exactly 4 array lookups and 3 additions (Sum = D - B - C + A) in O(1) time, independent of box size."
    },
    {
        "id": 41993,
        "subject": "DIP",
        "topicId": "19_Face_Recognition_Eigenfaces_and_Viola_Jones",
        "topicTitle": "19 · Face: Eigenfaces & Viola-Jones",
        "title": "AdaBoost Sample Reweighting & Attentional Cascade False Positive Bounds (Generated IISc / Viola-Jones Benchmark)",
        "kind2": "generated",
        "source": "Generated IISc Midterm / Freund & Schapire (1997) & Viola-Jones (IJCV 2004)",
        "marks": "[8 Marks]",
        "question": """<p><span class="part">(a)</span> In round $t$ of AdaBoost, 4 training examples have uniform sample weights $w_t = [0.25, 0.25, 0.25, 0.25]$ and true labels $y = [+1, +1, -1, -1]$. A candidate weak classifier misclassifies only sample 2 ($y_2 = +1$). Compute the weighted training error $\\epsilon_t$, the classifier voting weight $\\alpha_t = \\frac{1}{2}\\ln\\left(\\frac{1-\\epsilon_t}{\\epsilon_t}\\right)$, and the normalized updated sample weights $w_{t+1}$.</p>
<p><span class="part">(b)</span> An attentional cascade consists of $K = 10$ sequentially arranged classifier stages. Each individual stage $i$ is tuned to achieve:
- Stage detection rate $d_i = 0.99$ ($99\\%$ of genuine faces survive).
- Stage false positive rate $f_i = 0.30$ ($70\\%$ of background sub-windows are eliminated).
Compute the overall detection rate $D_{\\text{overall}} = \\prod_{i=1}^{10} d_i$ and the overall false positive rate $F_{\\text{overall}} = \\prod_{i=1}^{10} f_i$.</p>
<p><span class="part">(c)</span> If an input VGA video frame ($640 \\times 480$) contains approximately $100,000$ candidate sliding sub-windows and a single face, calculate the expected number of false alarms reported by the full 10-stage cascade.</p>""",
        "solution": """<p><span class="part">Part (a): AdaBoost Weight Update Trace</span><br>
1. <strong>Weighted Error $\\epsilon_t$:</strong><br>
Misclassified set is $\{2\}$:
$$\\epsilon_t = \\sum_{i: y_i \\ne h_t(x_i)} w_{t, i} = w_{t, 2} = <span class=\"ans\">0.25</span>$$
2. <strong>Classifier Weight $\\alpha_t$:</strong>
$$\\frac{1 - \\epsilon_t}{\\epsilon_t} = \\frac{1 - 0.25}{0.25} = \\frac{0.75}{0.25} = 3.0$$
$$\\alpha_t = \\frac{1}{2} \\ln(3.0) \\approx \\frac{1}{2}(1.09861) \\approx <span class=\"ans\">0.5493</span>$$
3. <strong>Update & Normalize Sample Weights:</strong><br>
Unnormalized weights: $\\tilde{w}_{t+1, i} = w_{t, i} \\exp(-\\alpha_t y_i h_t(x_i))$:
- For correct samples ($i \\in \\{1, 3, 4\\}$): $y_i h_t = +1$:
$$\\tilde{w}_i = 0.25 \\exp(-0.5493) = 0.25 / \\sqrt{3} \\approx 0.14434$$
- For incorrect sample ($i = 2$): $y_2 h_t = -1$:
$$\\tilde{w}_2 = 0.25 \\exp(+0.5493) = 0.25 \\times \\sqrt{3} \\approx 0.43301$$
Normalization factor $Z_t = 3(0.14434) + 0.43301 = 0.43301 + 0.43301 = 0.86602$.
$$\\text{Correct samples: } w_{t+1, i} = \\frac{0.14434}{0.86602} = \\frac{1}{6} \\approx <span class=\"ans\">0.1667</span>$$
$$\\text{Incorrect sample: } w_{t+1, 2} = \\frac{0.43301}{0.86602} = \\frac{1}{2} = <span class=\"ans\">0.5000</span>$$
The misclassified sample's weight doubled from $0.25$ to $0.50$, forcing the next weak learner to prioritize it.</p>

<p><span class="part">Part (b): Attentional Cascade Performance Bounds</span><br>
1. <strong>Overall Detection Rate $D_{\\text{overall}}$:</strong><br>
Because stages are in series, a face must pass all 10 stages:
$$D_{\\text{overall}} = \\prod_{i=1}^{10} d_i = (0.99)^{10} = e^{10 \\ln(0.99)} \\approx e^{10(-0.01005)} = e^{-0.1005} \\approx <span class=\"ans\">0.9044 \\quad (90.44\\%)</span>$$
2. <strong>Overall False Positive Rate $F_{\\text{overall}}$:</strong><br>
A background sub-window triggers a false detection only if it fools every stage:
$$F_{\\text{overall}} = \\prod_{i=1}^{10} f_i = (0.30)^{10} = 59,049 \\times 10^{-10} \\approx <span class=\"ans\">5.905 \\times 10^{-6}</span>$$
The cascade drives false positives down to less than 6 per million candidate windows.</p>

<p><span class="part">Part (c): Expected False Alarms in Video Frame</span><br>
Given $N_{\\text{windows}} = 100,000 = 10^5$:
$$\\mathbb{E}[\\text{False Alarms}] = N_{\\text{windows}} \\times F_{\\text{overall}} = 10^5 \\times (5.905 \\times 10^{-6}) = <span class=\"ans\">0.5905 \\text{ detections}</span>$$
<span class=\"ans\">Conclusion:</span> On average, only <strong>$\approx 0.59$ false alarms</strong> appear per entire video frame (less than 1 false positive per frame), while preserving over $90\%$ face detection sensitivity. Early stages reject over $50\\%$ of background patches in just 2-3 evaluations, making the system run at 30+ frames per second.</p>""",
        "takeaway": "AdaBoost increases weights of misclassified training samples by exp(alpha) to focus on hard examples. The Viola-Jones attentional cascade chains weak classifiers to achieve exponentially decaying false alarms F = f^K (e.g. 10^-6) while maintaining high true positive recall D = d^K (~90%)."
    },

    # =========================================================================
    # TOPIC 20: Deep Learning and CNN Architectures for Images
    # =========================================================================
    {
        "id": 42091,
        "subject": "DIP",
        "topicId": "20_Deep_Learning_and_CNN_Architectures_for_Images",
        "topicTitle": "20 · Deep Learning & CNNs",
        "title": "Convolutional Layer Tensor Dimensions, Trainable Parameters & MAC Computational Cost (IISc Midterm / Stanford CS231n)",
        "kind2": "pyq",
        "source": "IISc Midterm / Stanford CS231n Convolutional Neural Networks for Visual Recognition",
        "marks": "[8 Marks]",
        "question": """<p>An input feature map tensor to a convolutional layer has dimensions:
$$W_{\\text{in}} \\times H_{\\text{in}} \\times C_{\\text{in}} = 32 \\times 32 \\times 64$$
The convolutional layer employs $C_{\\text{out}} = 128$ filters of spatial kernel size $K = 5 \\times 5$, operated with stride $S = 2$ and zero-padding $P = 2$. Each filter includes one learnable scalar bias parameter.</p>
<p><span class="part">(a)</span> Calculate the spatial width $W_{\\text{out}}$, height $H_{\\text{out}}$, and depth $C_{\\text{out}}$ of the output feature tensor.</p>
<p><span class="part">(b)</span> Calculate the exact total number of learnable parameters (weights and biases) in this layer.</p>
<p><span class="part">(c)</span> Calculate the total number of Multiply-Accumulate (MAC) operations required to perform forward pass inference for a single image.</p>""",
        "solution": """<p><span class="part">Part (a): Output Tensor Spatial Dimensions</span><br>
Using the discrete convolution spatial mapping formula:
$$W_{\\text{out}} = \\left\\lfloor \\frac{W_{\\text{in}} - K + 2P}{S} \\right\\rfloor + 1$$
Substituting $W_{\\text{in}} = 32, K = 5, P = 2, S = 2$:
$$W_{\\text{out}} = \\left\\lfloor \\frac{32 - 5 + 2(2)}{2} \\right\\rfloor + 1 = \\left\\lfloor \\frac{31}{2} \\right\\rfloor + 1 = 15 + 1 = <span class=\"ans\">16</span>$$
By spatial symmetry, $H_{\\text{out}} = 16$.<br>
The number of output channels is governed by the number of filters: $C_{\\text{out}} = 128$.<br>
<span class=\"ans\">Output Feature Tensor Dimensions: $16 \\times 16 \\times 128$</span>.</p>

<p><span class="part">Part (b): Total Trainable Parameters</span><br>
Each convolutional filter operates over all input channels $C_{\\text{in}} = 64$ simultaneously:
$$\\text{Weights per filter} = K \\times K \\times C_{\\text{in}} = 5 \\times 5 \\times 64 = 1,600$$
$$\\text{Biases per filter} = 1$$
$$\\text{Parameters per filter} = 1,600 + 1 = 1,601$$
Across all $C_{\\text{out}} = 128$ output filters:
<span class=\"ans\">$$\\text{Total Parameters} = 128 \\times 1,601 = 204,928$$</span></p>

<p><span class="part">Part (c): Forward Pass MAC Operations</span><br>
Total output activation pixels:
$$N_{\\text{output}} = W_{\\text{out}} \\times H_{\\text{out}} \\times C_{\\text{out}} = 16 \\times 16 \\times 128 = 32,768 \\text{ activations}$$
Each output activation pixel is an inner product of a $5 \\times 5 \\times 64$ kernel volume against the input feature map patch, requiring $5 \\times 5 \\times 64 = 1,600$ multiply-accumulate operations:
$$\\text{Total MACs} = 32,768 \\times 1,600 = <span class=\"ans\">52,428,800 \\text{ MACs} \\approx 52.43 \\text{ MMACs}</span>$$
(In terms of floating-point operations, FLOPs $\\approx 2 \\times \\text{MACs} \\approx 104.86$ MFLOPs).</p>""",
        "takeaway": "Convolutional layer output dimensions follow W_out = floor((W_in - K + 2P)/S) + 1. Total parameters equal C_out x (K^2 C_in + 1), and computational inference cost is W_out x H_out x C_out x K^2 C_in MACs."
    },
    {
        "id": 42092,
        "subject": "DIP",
        "topicId": "20_Deep_Learning_and_CNN_Architectures_for_Images",
        "topicTitle": "20 · Deep Learning & CNNs",
        "title": "Analytical Receptive Field & Cumulative Feature Stride Tracking (IISc Midterm / Berkeley CS280)",
        "kind2": "pyq",
        "source": "IISc Midterm / Berkeley CS280 Computer Vision & Araujo et al. (Distill 2019)",
        "marks": "[8 Marks]",
        "question": """<p>Consider a 4-layer sequential deep convolutional neural network:
<ul>
  <li><strong>Layer 1 (Conv):</strong> Kernel $K_1 = 3$, Stride $S_1 = 1$, Padding $P_1 = 1$</li>
  <li><strong>Layer 2 (MaxPool):</strong> Kernel $K_2 = 2$, Stride $S_2 = 2$, Padding $P_2 = 0$</li>
  <li><strong>Layer 3 (Conv):</strong> Kernel $K_3 = 3$, Stride $S_3 = 1$, Padding $P_3 = 1$</li>
  <li><strong>Layer 4 (Conv):</strong> Kernel $K_4 = 3$, Stride $S_4 = 1$, Padding $P_4 = 1$</li>
</ul>
Let the base input image have receptive field $RF_0 = 1$ and cumulative jump $J_0 = 1$. The recursive update equations across layers are:
$$RF_l = RF_{l-1} + (K_l - 1) J_{l-1}, \\qquad J_l = J_{l-1} \\times S_l$$</p>
<p><span class="part">(a)</span> Compute the cumulative stride (jump) $J_l$ after each of the 4 layers.</p>
<p><span class="part">(b)</span> Compute the receptive field $RF_l$ after each layer and state the final effective receptive field at Layer 4.</p>
<p><span class="part">(c)</span> Explain why stacking two consecutive $3 \\times 3$ convolutions with stride 1 has the same effective receptive field as a single $5 \\times 5$ convolution, but uses fewer parameters and introduces greater non-linearity.</p>""",
        "solution": """<p><span class="part">Part (a): Cumulative Stride (Jump) Tracking</span><br>
Initial conditions: $J_0 = 1, RF_0 = 1$.<br>
Using $J_l = J_{l-1} \\times S_l$:
<ul>
  <li><strong>Layer 1 ($S_1 = 1$):</strong> $J_1 = J_0 \\times S_1 = 1 \\times 1 = <span class=\"ans\">1</span>$</li>
  <li><strong>Layer 2 ($S_2 = 2$):</strong> $J_2 = J_1 \\times S_2 = 1 \\times 2 = <span class=\"ans\">2</span>$</li>
  <li><strong>Layer 3 ($S_3 = 1$):</strong> $J_3 = J_2 \\times S_3 = 2 \\times 1 = <span class=\"ans\">2</span>$</li>
  <li><strong>Layer 4 ($S_4 = 1$):</strong> $J_4 = J_3 \\times S_4 = 2 \\times 1 = <span class=\"ans\">2</span>$</li>
</ul></p>

<p><span class="part">Part (b): Receptive Field Progression</span><br>
Using the recurrence $RF_l = RF_{l-1} + (K_l - 1) J_{l-1}$:
1. <strong>Layer 1 ($K_1 = 3, J_0 = 1$):</strong>
$$RF_1 = RF_0 + (3 - 1) J_0 = 1 + (2)(1) = <span class=\"ans\">3 \\times 3</span>$$
2. <strong>Layer 2 ($K_2 = 2, J_1 = 1$):</strong>
$$RF_2 = RF_1 + (2 - 1) J_1 = 3 + (1)(1) = <span class=\"ans\">4 \\times 4</span>$$
3. <strong>Layer 3 ($K_3 = 3, J_2 = 2$):</strong>
$$RF_3 = RF_2 + (3 - 1) J_2 = 4 + (2)(2) = 4 + 4 = <span class=\"ans\">8 \\times 8</span>$$
4. <strong>Layer 4 ($K_4 = 3, J_3 = 2$):</strong>
$$RF_4 = RF_3 + (K_4 - 1) J_3 = 8 + (3 - 1)(2) = 8 + 4 = <span class=\"ans\">12 \\times 12</span>$$
<span class=\"ans\">Final Receptive Field: $12 \\times 12$ pixels</span>. Every neuron in the Layer 4 feature map observes a $12 \\times 12$ patch of the original input.</p>

<p><span class="part">Part (c): Stacking $3 \\times 3$ Convolutions (VGG Principle)</span><br>
1. <strong>Receptive Field Equivalence:</strong><br>
Two stacked $3 \\times 3$ convolutions ($S=1$) yield:
$$RF_1 = 1 + (3 - 1) = 3, \\qquad RF_2 = 3 + (3 - 1)(1) = 5$$
This spans an identical $5 \\times 5$ spatial receptive field as a single $5 \\times 5$ conv layer.<br>
2. <strong>Parameter Savings:</strong><br>
Assuming $C$ channels:
- Single $5 \\times 5$ layer: $5^2 \\cdot C^2 = 25 C^2$ weights.
- Two stacked $3 \\times 3$ layers: $2 \\cdot (3^2 \\cdot C^2) = 18 C^2$ weights.
<span class=\"ans\">Parameter reduction: $\\frac{25 - 18}{25} = 28\\%$ savings</span>.<br>
3. <strong>Representational Power:</strong><br>
Stacking two layers incorporates two non-linear activation functions (e.g. ReLU) instead of one, enabling the network to learn more discriminative, expressive feature representations.</p>""",
        "takeaway": "Receptive field grows recursively as RF_l = RF_{l-1} + (K_l - 1) J_{l-1} where J_l = prod S_i. Stacking two 3x3 convolutions matches the 5x5 receptive field while cutting parameters by 28% and adding an extra non-linear activation (VGG design principle)."
    },
    {
        "id": 42093,
        "subject": "DIP",
        "topicId": "20_Deep_Learning_and_CNN_Architectures_for_Images",
        "topicTitle": "20 · Deep Learning & CNNs",
        "title": "1x1 Bottleneck Convolutions & U-Net Skip Connection Mechanics (Generated IISc / GoogLeNet & U-Net Benchmark)",
        "kind2": "generated",
        "source": "Generated IISc Midterm / Szegedy et al. (GoogLeNet CVPR 2015) & Ronneberger et al. (U-Net MICCAI 2015)",
        "marks": "[8 Marks]",
        "question": """<p><span class="part">(a)</span> In an Inception block, an input tensor of size $28 \\times 28 \\times 192$ must produce $32$ output channels using $5 \\times 5$ convolutions (with stride 1 and same padding).
(i) Compute the Multiply-Accumulate (MAC) operations for direct convolution without bottleneck.
(ii) A $1 \\times 1$ conv bottleneck is inserted that first compresses $192$ channels down to $16$ channels, followed by the $5 \\times 5$ conv to $32$ channels. Compute the total MACs for the two-stage bottleneck path.
(iii) Calculate the percentage computational savings.</p>
<p><span class="part">(b)</span> Explain the architectural philosophy of the <strong>U-Net</strong> for semantic segmentation. Contrast the role of the Contracting Path (Encoder) with the Expansive Path (Decoder).</p>
<p><span class="part">(c)</span> What fundamental spatial localization degradation occurs if segmentation masks are reconstructed solely from deep bottleneck features without skip connections, and how do lateral skip connections solve this problem?</p>""",
        "solution": """<p><span class="part">Part (a): 1x1 Convolution Bottleneck Computational Analysis</span><br>
Input: $28 \\times 28 \\times 192$. Output spatial size: $28 \\times 28 = 784$ pixels.<br>
1. <strong>Direct $5 \\times 5$ Convolution (No Bottleneck):</strong>
$$\\text{Output activations} = 28 \\times 28 \\times 32 = 25,088$$
$$\\text{MACs per activation} = 5 \\times 5 \\times 192 = 4,800$$
$$\\text{Total MACs}_{\\text{direct}} = 25,088 \\times 4,800 = <span class=\"ans\">120,422,400 \\text{ MACs} \\approx 120.42 \\text{ MMACs}</span>$$
2. <strong>Two-Stage Bottleneck Path ($192 \\to 16 \\to 32$):</strong>
- <em>Stage 1 ($1 \\times 1$ Conv $192 \\to 16$):</em>
$$\\text{MACs}_1 = (28 \\times 28 \\times 16) \\times (1 \\times 1 \\times 192) = 12,544 \\times 192 = 2,408,448$$
- <em>Stage 2 ($5 \\times 5$ Conv $16 \\to 32$):</em>
$$\\text{MACs}_2 = (28 \\times 28 \\times 32) \\times (5 \\times 5 \\times 16) = 25,088 \\times 400 = 10,035,200$$
$$\\text{Total MACs}_{\\text{bottleneck}} = 2,408,448 + 10,035,200 = <span class=\"ans\">12,443,648 \\text{ MACs} \\approx 12.44 \\text{ MMACs}</span>$$
3. <strong>Computational Savings:</strong>
$$\\text{Speedup Factor} = \\frac{120,422,400}{12,443,648} \\approx <span class=\"ans\">9.68\\times</span>$$
$$\\text{Reduction} = \\left(1 - \\frac{12.4436}{120.4224}\\right) \\times 100\\% = <span class=\"ans\">89.67\\% \\text{ reduction}</span>$$
The $1 \\times 1$ bottleneck slashes computational burden by nearly <strong>$90\\%$</strong> while allowing the network to go deeper.</p>

<p><span class="part">Part (b): U-Net Architecture Philosophy</span><br>
U-Net comprises two symmetric, cooperating paths:
<ul>
  <li><strong>Contracting Path (Encoder):</strong> Repeated pairs of $3 \\times 3$ convolutions and $2 \\times 2$ max-pooling downsampling layers. It extracts progressively richer, high-level semantic abstractions answering <em>what</em> category of object is present at the cost of spatial resolution.</li>
  <li><strong>Expansive Path (Decoder):</strong> Repeated upsampling (transposed convolutions) and $3 \\times 3$ convolutions. It maps abstract features back up to the full spatial resolution of the original image, generating pixel-wise probability maps for segmentation.</li>
</ul></p>

<p><span class="part">Part (c): Bottleneck Information Loss & Skip Connections</span><br>
<strong>Why Pure Bottleneck Fails:</strong><br>
Successive downsampling (pooling/strided convs) discards precise high-frequency spatial coordinate details to achieve translation invariance and large receptive field. At the deep bottleneck (e.g. $16 \\times 16$), the network knows semantic identity but has destroyed exact pixel boundaries. Upsampling from this bottleneck alone produces coarse, blurry, rounded segmentations that fail to delineate thin membranes or delicate tissue structures.<br>
<strong>Solution via Lateral Skip Connections:</strong><br>
U-Net copies high-resolution feature maps directly from the contracting path and concatenates them with the corresponding upsampled feature maps in the expansive path.<br>
- These skip connections bypass the lossy bottleneck, directly injecting pristine, uncompressed spatial edge coordinates into the decoder.<br>
- The decoder fuses semantic context (from deep layers) with sharp boundary localization (from skip connections) to synthesize <strong>pixel-exact segmentations</strong>.</p>""",
        "takeaway": "1x1 convolutions act as cross-channel pooling bottlenecks that reduce channel dimensionality prior to expensive spatial convolutions, cutting FLOPs by up to 90% (Inception/ResNet). U-Net skip connections preserve high-frequency boundary coordinates across the hierarchy to enable pixel-precise semantic segmentation."
    }
]

def main():
    with open(PRACTICE_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    if "41991" in content:
        print("Batch 19-20 already present in practice_dip.js!")
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
    for card in PRACTICE_DIP_19_20:
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

    print("Successfully added DIP Batch 19-20 (6 cards). Total in file now updated.")

if __name__ == "__main__":
    main()
