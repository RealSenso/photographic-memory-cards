#!/usr/bin/env python3
"""
Builder script for DIP Practice Cards: Batch 03 (Topics 05 & 06)
Topic 05: Histogram Equalization and Specification (Cards 40591, 40592, 40593)
Topic 06: LSI Systems, 2D Convolution and Spatial Filtering (Cards 40691, 40692, 40693)
"""

import json
import os
import re

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRACTICE_FILE = os.path.join(REPO_DIR, "practice_dip.js")

PRACTICE_DIP_05_06 = [
    # =========================================================================
    # TOPIC 05: Histogram Equalization and Specification
    # =========================================================================
    {
        "id": 40591,
        "subject": "DIP",
        "topicId": "05_Histogram_Equalization_and_Specification",
        "topicTitle": "05 · Histogram Equalization & Specification",
        "title": "Continuous Histogram Equalization for Exponential Distribution (IISc Midterm / Stanford CS231A)",
        "kind2": "pyq",
        "source": "IISc Midterm / Stanford CS231A Image Processing",
        "marks": "[8 Marks]",
        "question": """<p>An analog image has continuous normalized intensity $r \\in [0, 1]$ governed by the truncated exponential Probability Density Function (PDF):
$$p_r(r) = \\frac{\\lambda e^{-\\lambda r}}{1 - e^{-\\lambda}}, \\quad 0 \\le r \\le 1, \\quad \\lambda > 0$$</p>
<p><span class="part">(a)</span> Derive the continuous histogram equalization transformation $s = T(r)$ mapping $r \\in [0, 1]$ monotonically into $s \\in [0, 1]$. Verify boundary conditions $T(0) = 0$ and $T(1) = 1$.</p>
<p><span class="part">(b)</span> Using the fundamental transformation of random variables $p_s(s) = p_r(r) \\left| \\frac{dr}{ds} \\right|$, prove that the transformed output PDF is strictly uniform: $p_s(s) = 1$ for all $s \\in [0, 1]$.</p>
<p><span class="part">(c)</span> Derive the inverse transformation $r = T^{-1}(s)$ needed for histogram specification.</p>""",
        "solution": """<p><span class="part">Part (a): Equalization Transformation $s = T(r)$</span><br>
Continuous histogram equalization sets the transformation equal to the scaled cumulative distribution function (CDF):
$$s = T(r) = (L - 1) \\int_0^r p_r(w) dw$$
With normalized output range $[0, 1]$, $L - 1 = 1$:
$$s = T(r) = \\int_0^r \\frac{\\lambda e^{-\\lambda w}}{1 - e^{-\\lambda}} dw = \\frac{1}{1 - e^{-\\lambda}} \\left[ -e^{-\\lambda w} \\right]_0^r = \\frac{1 - e^{-\\lambda r}}{1 - e^{-\\lambda}}$$
Checking boundary conditions:
- At $r = 0$: $T(0) = \\frac{1 - e^0}{1 - e^{-\\lambda}} = \\frac{1 - 1}{1 - e^{-\\lambda}} = 0$
- At $r = 1$: $T(1) = \\frac{1 - e^{-\\lambda}}{1 - e^{-\\lambda}} = 1$<br>
<span class="ans">$$s = T(r) = \\frac{1 - e^{-\\lambda r}}{1 - e^{-\\lambda}}$$</span></p>

<p><span class="part">Part (b): Proof of Uniform Output Distribution</span><br>
Differentiating $s$ with respect to $r$:
$$\\frac{ds}{dr} = \\frac{d}{dr}\\left( \\frac{1 - e^{-\\lambda r}}{1 - e^{-\\lambda}} \\right) = \\frac{\\lambda e^{-\\lambda r}}{1 - e^{-\\lambda}} = p_r(r) > 0$$
Since $T(r)$ is strictly monotonically increasing, $\\frac{dr}{ds} = \\frac{1}{p_r(r)}$.<br>
Applying the probability density transformation formula:
$$p_s(s) = p_r(r) \\left| \\frac{dr}{ds} \\right| = p_r(r) \\cdot \\frac{1}{p_r(r)} = <span class=\"ans\">1, \\quad \\forall s \\in [0, 1]</span>$$
<span class=\"ans\">The output distribution is identically $\\text{Uniform}[0, 1]$. Histogram equalization maximizes differential entropy: $H(s) = -\\int_0^1 1 \\ln(1) ds = 0$.</span></p>

<p><span class="part">Part (c): Inverse Mapping $r = T^{-1}(s)$</span><br>
Solving $s = \\frac{1 - e^{-\\lambda r}}{1 - e^{-\\lambda}}$ for $r$:
$$s(1 - e^{-\\lambda}) = 1 - e^{-\\lambda r} \\implies e^{-\\lambda r} = 1 - s(1 - e^{-\\lambda})$$
Taking the natural logarithm:
$$-\\lambda r = \\ln\\left[ 1 - s(1 - e^{-\\lambda}) \\right]$$
<span class="ans">$$r = T^{-1}(s) = -\\frac{1}{\\lambda} \\ln\\left[ 1 - s(1 - e^{-\\lambda}) \\right]$$</span></p>""",
        "takeaway": "Continuous histogram equalization $s = T(r) = \\int_0^r p_r(w)dw$ transforms any continuous PDF into a strictly uniform distribution $\\text{Uniform}[0, 1]$ by matching the Jacobian $\\frac{ds}{dr} = p_r(r)$."
    },
    {
        "id": 40592,
        "subject": "DIP",
        "topicId": "05_Histogram_Equalization_and_Specification",
        "topicTitle": "05 · Histogram Equalization & Specification",
        "title": "Discrete Histogram Equalization on 8 Gray Levels (IIT Delhi / Gonzalez & Woods)",
        "kind2": "university",
        "source": "IIT Delhi / Gonzalez & Woods Digital Image Processing",
        "marks": "[8 Marks]",
        "question": """<p>A $64 \\times 64$ grayscale image (total $N = 4096$ pixels) has 8 discrete intensity levels $r_k \\in \\{0, 1, \\dots, 7\\}$ with pixel count distribution:
$$\\mathbf{n} = [790, \\, 1023, \\, 850, \\, 656, \\, 329, \\, 245, \\, 122, \\, 81]$$</p>
<p><span class="part">(a)</span> Compute normalized probabilities $p_r(r_k) = n_k / N$ and the cumulative distribution function $\\text{CDF}(k)$.</p>
<p><span class="part">(b)</span> Compute the equalized output intensity levels $s_k = \\text{round}\\left( (L - 1) \\times \\text{CDF}(k) \\right)$ with $L = 8$.</p>
<p><span class="part">(c)</span> Construct the output equalized histogram $\\mathbf{n}_{\\text{out}}(s)$ and explain why discrete histogram equalization can never produce a perfectly flat uniform histogram.</p>""",
        "solution": """<p><span class="part">Part (a): Probability Vector & CDF</span><br>
With total pixels $N = 4096$:
1. $k = 0$: $p(0) = 790/4096 \\approx 0.1929 \\implies \\text{CDF}(0) = 0.1929$
2. $k = 1$: $p(1) = 1023/4096 \\approx 0.2498 \\implies \\text{CDF}(1) = 0.1929 + 0.2498 = 0.4426$
3. $k = 2$: $p(2) = 850/4096 \\approx 0.2075 \\implies \\text{CDF}(2) = 0.4426 + 0.2075 = 0.6501$
4. $k = 3$: $p(3) = 656/4096 \\approx 0.1602 \\implies \\text{CDF}(3) = 0.6501 + 0.1602 = 0.8103$
5. $k = 4$: $p(4) = 329/4096 \\approx 0.0803 \\implies \\text{CDF}(4) = 0.8103 + 0.0803 = 0.8906$
6. $k = 5$: $p(5) = 245/4096 \\approx 0.0598 \\implies \\text{CDF}(5) = 0.8906 + 0.0598 = 0.9504$
7. $k = 6$: $p(6) = 122/4096 \\approx 0.0298 \\implies \\text{CDF}(6) = 0.9504 + 0.0298 = 0.9802$
8. $k = 7$: $p(7) = 81/4096 \\approx 0.0198 \\implies \\text{CDF}(7) = 0.9802 + 0.0198 = 1.0000$</p>

<p><span class="part">Part (b): Equalized Levels $s_k = \\text{round}(7 \\times \\text{CDF}(k))$</span><br>
- $s_0 = \\text{round}(7 \\times 0.1929) = \\text{round}(1.350) = <span class=\"ans\">1</span>$
- $s_1 = \\text{round}(7 \\times 0.4426) = \\text{round}(3.098) = <span class=\"ans\">3</span>$
- $s_2 = \\text{round}(7 \\times 0.6501) = \\text{round}(4.551) = <span class=\"ans\">5</span>$
- $s_3 = \\text{round}(7 \\times 0.8103) = \\text{round}(5.672) = <span class=\"ans\">6</span>$
- $s_4 = \\text{round}(7 \\times 0.8906) = \\text{round}(6.234) = <span class=\"ans\">6</span>$
- $s_5 = \\text{round}(7 \\times 0.9504) = \\text{round}(6.653) = <span class=\"ans\">7</span>$
- $s_6 = \\text{round}(7 \\times 0.9802) = \\text{round}(6.861) = <span class=\"ans\">7</span>$
- $s_7 = \\text{round}(7 \\times 1.0000) = \\text{round}(7.000) = <span class=\"ans\">7</span>$<br>
<span class=\"ans\">Mapping: $r \\to s = [0 \\to 1, \\; 1 \\to 3, \\; 2 \\to 5, \\; 3 \\to 6, \\; 4 \\to 6, \\; 5 \\to 7, \\; 6 \\to 7, \\; 7 \\to 7]$</span></p>

<p><span class="part">Part (c): Output Histogram & Discreteness Limitation</span><br>
Grouping mapped pixel counts:
- $s = 0$: $0$ pixels
- $s = 1$: $n(0) = 790$ pixels
- $s = 2$: $0$ pixels
- $s = 3$: $n(1) = 1023$ pixels
- $s = 4$: $0$ pixels
- $s = 5$: $n(2) = 850$ pixels
- $s = 6$: $n(3) + n(4) = 656 + 329 = 985$ pixels
- $s = 7$: $n(5) + n(6) + n(7) = 245 + 122 + 81 = 448$ pixels<br>
<span class=\"ans\">$$\\mathbf{n}_{\\text{out}} = [0, \\, 790, \\, 0, \\, 1023, \\, 0, \\, 850, \\, 985, \\, 448]$$</span>
<strong>Why Discrete HE is Not Flat:</strong> In digital images, pixel intensities are discrete integers. A point operation maps all pixels with input intensity $r_k$ to a single output value $s_k$; it <em>cannot split</em> identical pixels into different bins. Consequently, multiple bins merge ($3, 4 \\to 6$ and $5, 6, 7 \\to 7$), leaving empty gaps (bins 0, 2, 4 have 0 count) and preventing a perfectly uniform distribution.</p>""",
        "takeaway": "Discrete histogram equalization uses $s_k = \\text{round}((L-1)\\text{CDF}(k))$. Because point operations cannot split pixels belonging to the same gray level, bins merge and gaps emerge, creating an approximately spread but never perfectly flat histogram."
    },
    {
        "id": 40593,
        "subject": "DIP",
        "topicId": "05_Histogram_Equalization_and_Specification",
        "topicTitle": "05 · Histogram Equalization & Specification",
        "title": "Histogram Specification / Matching via CDF Inversion (IISc Midterm / Berkeley EECS)",
        "kind2": "generated",
        "source": "IISc Midterm / Berkeley EECS Image Processing",
        "marks": "[8 Marks]",
        "question": """<p>We wish to transform the equalized image from Problem 2 (with mapping $s = [1, 3, 5, 6, 6, 7, 7, 7]$) to match a desired target histogram on $z \\in \\{0, 1, \\dots, 7\\}$:
$$\\mathbf{p}_z = [0.00, \\, 0.00, \\, 0.00, \\, 0.15, \\, 0.20, \\, 0.30, \\, 0.20, \\, 0.15]$$</p>
<p><span class="part">(a)</span> Compute the target cumulative distribution $G(z_q) = \\sum_{j=0}^q p_z(z_j)$ and scale by $L - 1 = 7$: $v_q = \\text{round}(7 \\times G(z_q))$.</p>
<p><span class="part">(b)</span> For each original level $r_k \\in \\{0, 1, \\dots, 7\\}$, use the minimum-distance rule $|v_q - s_k|$ to determine the specified target level $z_k = G^{-1}(s_k)$.</p>
<p><span class="part">(c)</span> State the final lookup table $r_k \\mapsto z_k$ and the resulting pixel counts in the specified image.</p>""",
        "solution": """<p><span class="part">Part (a): Scaled Target CDF $v_q = \\text{round}(7 \\times G(z_q))$</span><br>
Evaluating cumulative sums and rounding:
- $q = 0$: $G(0) = 0.00 \\implies 7 \\times 0.00 = 0 \\implies v_0 = <span class=\"ans\">0</span>$
- $q = 1$: $G(1) = 0.00 \\implies 7 \\times 0.00 = 0 \\implies v_1 = <span class=\"ans\">0</span>$
- $q = 2$: $G(2) = 0.00 \\implies 7 \\times 0.00 = 0 \\implies v_2 = <span class=\"ans\">0</span>$
- $q = 3$: $G(3) = 0.15 \\implies 7 \\times 0.15 = 1.05 \\implies v_3 = <span class=\"ans\">1</span>$
- $q = 4$: $G(4) = 0.15 + 0.20 = 0.35 \\implies 7 \\times 0.35 = 2.45 \\implies v_4 = <span class=\"ans\">2</span>$
- $q = 5$: $G(5) = 0.35 + 0.30 = 0.65 \\implies 7 \\times 0.65 = 4.55 \\implies v_5 = <span class=\"ans\">5</span>$
- $q = 6$: $G(6) = 0.65 + 0.20 = 0.85 \\implies 7 \\times 0.85 = 5.95 \\implies v_6 = <span class=\"ans\">6</span>$
- $q = 7$: $G(7) = 1.00 \\implies 7 \\times 1.00 = 7.00 \\implies v_7 = <span class=\"ans\">7</span>$<br>
Target discrete levels: $\\mathbf{v} = [0, 0, 0, 1, 2, 5, 6, 7]$.</p>

<p><span class="part">Part (b): Minimum-Distance Matching $s_k \\to z_q$</span><br>
Recall from Problem 2: $s = [1, 3, 5, 6, 6, 7, 7, 7]$. For each $s_k$, find $z_q$ minimizing $|v_q - s_k|$:
- $r_0 \\implies s_0 = 1$: $v_3 = 1$ is exact match $\\implies z = <span class=\"ans\">3</span>$
- $r_1 \\implies s_1 = 3$: distances to $v$: $|0-3|=3, |1-3|=2, |2-3|=1$ (at $z=4$), $|5-3|=2$. Closest is $v_4 = 2 \\implies z = <span class=\"ans\">4</span>$
- $r_2 \\implies s_2 = 5$: $v_5 = 5$ is exact match $\\implies z = <span class=\"ans\">5</span>$
- $r_3 \\implies s_3 = 6$: $v_6 = 6$ is exact match $\\implies z = <span class=\"ans\">6</span>$
- $r_4 \\implies s_4 = 6$: $v_6 = 6$ is exact match $\\implies z = <span class=\"ans\">6</span>$
- $r_5 \\implies s_5 = 7$: $v_7 = 7$ is exact match $\\implies z = <span class=\"ans\">7</span>$
- $r_6 \\implies s_6 = 7$: $v_7 = 7$ is exact match $\\implies z = <span class=\"ans\">7</span>$
- $r_7 \\implies s_7 = 7$: $v_7 = 7$ is exact match $\\implies z = <span class=\"ans\">7</span>$</p>

<p><span class="part">Part (c): Final Lookup Table & Specified Histogram</span><br>
Direct composite lookup table $r_k \\mapsto z$:
<span class="ans">$$[0 \\mapsto 3, \\quad 1 \\mapsto 4, \\quad 2 \\mapsto 5, \\quad 3 \\mapsto 6, \\quad 4 \\mapsto 6, \\quad 5 \\mapsto 7, \\quad 6 \\mapsto 7, \\quad 7 \\mapsto 7]$$</span>
Final pixel counts:
- $z \\in \\{0, 1, 2\\}$: $0$ pixels (matches target $p_z = 0$)
- $z = 3$: $n_0 = 790$ pixels ($19.29\\%$, target $15.0\\%$)
- $z = 4$: $n_1 = 1023$ pixels ($24.98\\%$, target $20.0\\%$)
- $z = 5$: $n_2 = 850$ pixels ($20.75\\%$, target $30.0\\%$)
- $z = 6$: $n_3 + n_4 = 656 + 329 = 985$ pixels ($24.05\\%$, target $20.0\\%$)
- $z = 7$: $n_5 + n_6 + n_7 = 245 + 122 + 81 = 448$ pixels ($10.94\\%$, target $15.0\\%$)
Total $= 4096$ pixels. The specified output closely mimics the desired unimodal high-brightness shape.</p>""",
        "takeaway": "Histogram specification matches histograms via intermediate uniform space: $r \\xrightarrow{T} s \\xrightarrow{G^{-1}} z$. Finding $z_q$ whose scaled target CDF $v_q$ is closest to equalized level $s_k$ produces a direct $O(L)$ lookup table."
    },

    # =========================================================================
    # TOPIC 06: LSI Systems, 2D Convolution and Spatial Filtering
    # =========================================================================
    {
        "id": 40691,
        "subject": "DIP",
        "topicId": "06_LSI_Systems_2D_Convolution_and_Spatial_Filtering",
        "topicTitle": "06 · LSI Systems, Convolution & Filtering",
        "title": "Filter Separability & Computational Complexity (IISc Midterm / Stanford CS231A)",
        "kind2": "pyq",
        "source": "IISc Midterm / Stanford CS231A Computer Vision",
        "marks": "[8 Marks]",
        "question": """<p>Consider two $3 \\times 3$ spatial filtering masks:
$$H_A = \\begin{pmatrix} 1 & 2 & 1 \\\\ 2 & 4 & 2 \\\\ 1 & 2 & 1 \\end{pmatrix}, \\qquad H_B = \\begin{pmatrix} 0 & 1 & 0 \\\\ 1 & -4 & 1 \\\\ 0 & 1 & 0 \\end{pmatrix}$$</p>
<p><span class="part">(a)</span> Compute the matrix rank of $H_A$ and $H_B$. State the criterion for a 2D filter mask to be <strong>separable</strong>.</p>
<p><span class="part">(b)</span> For the separable filter, decompose it into the outer product of two 1D filters $\\mathbf{u} \\mathbf{v}^\\top$.</p>
<p><span class="part">(c)</span> For an $M \\times N$ image filtered by a $K \\times K$ kernel, compare the number of multiplications required for direct 2D convolution versus separable 1D convolution. What is the percentage speedup for $K = 15$?</p>""",
        "solution": """<p><span class="part">Part (a): Rank & Separability Criterion</span><br>
A 2D filter kernel $H$ is <strong>separable</strong> if and only if it has matrix rank 1:
$$\\operatorname{rank}(H) = 1 \\iff H = \\mathbf{u} \\mathbf{v}^\\top$$
1. <strong>For $H_A$:</strong>
Row 2 is $2 \\times \\text{Row 1}$, and Row 3 is $1 \\times \\text{Row 1}$. All rows are linearly dependent scalar multiples of $(1, 2, 1)$.
<span class="ans">$$\\operatorname{rank}(H_A) = 1 \\implies H_A \\text{ is separable}$$</span>
2. <strong>For $H_B$:</strong>
Compute $\\det(H_B) = 0(16-1) - 1(0-0) + 0(1+0) = 0$. However, rows 1 and 2 are linearly independent, and row 3 is not a combination of rows 1 and 2. The upper-left $2 \\times 2$ submatrix has $\\det = -1 \\ne 0$.
<span class="ans">$$\\operatorname{rank}(H_B) = 3 \\implies H_B \\text{ is NOT separable}$$</span>
The standard 4-neighbor Laplacian cannot be decomposed into a single separable pass.</p>

<p><span class="part">Part (b): Outer Product Decomposition of $H_A$</span><br>
$$H_A = \\begin{pmatrix} 1 & 2 & 1 \\\\ 2 & 4 & 2 \\\\ 1 & 2 & 1 \\end{pmatrix} = \\begin{pmatrix} 1 \\\\ 2 \\\\ 1 \\end{pmatrix} \\begin{pmatrix} 1 & 2 & 1 \\end{pmatrix}$$
<span class="ans">$$\\mathbf{u} = \\begin{pmatrix} 1 \\\\ 2 \\\\ 1 \\end{pmatrix}, \\quad \\mathbf{v} = \\begin{pmatrix} 1 \\\\ 2 \\\\ 1 \\end{pmatrix}$$</span>
Applying $H_A$ to an image $f$ is equivalent to convolving along columns with $\\mathbf{u}$, then along rows with $\\mathbf{v}^\\top$:
$$f ** H_A = (f * \\mathbf{u}) * \\mathbf{v}^\\top$$</p>

<p><span class="part">Part (c): Computational Complexity & Speedup</span><br>
For an $M \\times N$ image:
- <strong>Direct 2D convolution:</strong> Each output pixel requires $K^2$ multiplications.
$$\\text{Total multiplications} = M N K^2$$
- <strong>Separable convolution:</strong> Vertical pass takes $M N K$ mults; horizontal pass takes $M N K$ mults.
$$\\text{Total multiplications} = M N(2K) = 2 M N K$$
Efficiency ratio:
$$\\text{Speedup Factor} = \\frac{K^2}{2K} = \\frac{K}{2}$$
For kernel size $K = 15$:
$$\\text{Ratio} = \\frac{2K}{K^2} = \\frac{2(15)}{225} = \\frac{30}{225} = \\frac{2}{15} \\approx 13.33\\%$$
<span class="ans">Operations drop from 225 down to 30 multiplications/pixel, yielding an $86.67\\%$ reduction in computation time (speedup of $7.5\\times$).</span></p>""",
        "takeaway": "A 2D filter kernel is separable if and only if $\\operatorname{rank}(H)=1$ ($H = \\mathbf{u}\\mathbf{v}^\\top$). Separable convolution replaces a 2D $K \\times K$ filter with two successive 1D passes, reducing operations from $O(K^2)$ to $O(2K)$."
    },
    {
        "id": 40692,
        "subject": "DIP",
        "topicId": "06_LSI_Systems_2D_Convolution_and_Spatial_Filtering",
        "topicTitle": "06 · LSI Systems, Convolution & Filtering",
        "title": "2D Spatial Convolution vs Cross-Correlation (IIT Delhi / Berkeley EECS)",
        "kind2": "university",
        "source": "IIT Delhi / Berkeley EECS Digital Signals and Images",
        "marks": "[8 Marks]",
        "question": """<p>Consider the image patch $f$ and filtering mask $h$:</p>
$$f = \\begin{pmatrix}
10 & 20 & 30 \\\\
40 & 50 & 60 \\\\
70 & 80 & 90
\\end{pmatrix}, \\qquad h = \\begin{pmatrix}
-1 & 0 & 1 \\\\
-2 & 0 & 2 \\\\
-1 & 0 & 1
\\end{pmatrix}$$
<p><span class="part">(a)</span> State the mathematical difference between 2D <strong>spatial convolution</strong> $g = f ** h$ and 2D <strong>cross-correlation</strong> $g = f \\star h$. Flip $h$ by $180^\\circ$ to obtain convolution impulse response $h_{\\text{rot}}$.</p>
<p><span class="part">(b)</span> Compute the central filtered pixel value under cross-correlation $(f \\star h)(1, 1)$.</p>
<p><span class="part">(c)</span> Compute the central filtered pixel value under true convolution $(f ** h)(1, 1)$. Explain the sign inversion.</p>""",
        "solution": """<p><span class="part">Part (a): Mathematical Difference & 180° Rotation</span><br>
- <strong>2D Cross-correlation ($f \\star h$):</strong> Template matching without rotation:
$$(f \\star h)(x, y) = \\sum_{m=-1}^1 \\sum_{n=-1}^1 f(x+m, y+n) h(m, n)$$
- <strong>2D Convolution ($f ** h$):</strong> System response with kernel rotated by $180^\\circ$:
$$(f ** h)(x, y) = \\sum_{m=-1}^1 \\sum_{n=-1}^1 f(x-m, y-n) h(m, n) = \\sum_{m=-1}^1 \\sum_{n=-1}^1 f(x+m, y+n) h(-m, -n)$$
Flipping kernel $h$ horizontally and vertically:
$$h = \\begin{pmatrix} -1 & 0 & 1 \\\\ -2 & 0 & 2 \\\\ -1 & 0 & 1 \\end{pmatrix} \\xrightarrow{\\text{flip horiz}} \\begin{pmatrix} 1 & 0 & -1 \\\\ 2 & 0 & -2 \\\\ 1 & 0 & -1 \\end{pmatrix} \\xrightarrow{\\text{flip vert}} h_{\\text{rot}} = \\begin{pmatrix} 1 & 0 & -1 \\\\ 2 & 0 & -2 \\\\ 1 & 0 & -1 \\end{pmatrix}$$
<span class="ans">$$h_{\\text{rot}} = -h$$</span>
Because $h$ is anti-symmetric in its columns and symmetric in its rows, rotating by $180^\\circ$ negates the matrix: $h(-m, -n) = -h(m, n)$.</p>

<p><span class="part">Part (b): Central Pixel Cross-Correlation $(f \\star h)(1, 1)$</span><br>
Perform element-wise multiplication between patch $f$ and unrotated mask $h$:
$$(f \\star h)(1, 1) = \\sum_{i=1}^3 \\sum_{j=1}^3 f_{ij} h_{ij}$$
Evaluating column-by-column:
- Column 1: $10(-1) + 40(-2) + 70(-1) = -10 - 80 - 70 = -160$
- Column 2: $20(0) + 50(0) + 80(0) = 0$
- Column 3: $30(1) + 60(2) + 90(1) = 30 + 120 + 90 = +240$
Summing all elements:
<span class="ans">$$(f \\star h)(1, 1) = -160 + 0 + 240 = +80$$</span>
This measures the positive horizontal gradient $\\frac{\\partial f}{\\partial x} > 0$ (intensities increase from left to right: $10 \\to 30$).</p>

<p><span class="part">Part (c): Central Pixel Convolution $(f ** h)(1, 1)$</span><br>
True convolution applies the $180^\\circ$-rotated kernel $h_{\\text{rot}} = -h$:
$$(f ** h)(1, 1) = \\sum_{i=1}^3 \\sum_{j=1}^3 f_{ij} (h_{\\text{rot}})_{ij} = -\\sum_{i=1}^3 \\sum_{j=1}^3 f_{ij} h_{ij} = -(+80) = <span class=\"ans\">-80</span>$$
<strong>Explanation:</strong> Because convolution reflects the coordinate axes to ensure associativity $(f ** g) ** h = f ** (g ** h)$, an anti-symmetric gradient kernel yields opposite signs under convolution versus correlation. Deep learning libraries frequently implement cross-correlation while naming it 'Conv2D'.</p>""",
        "takeaway": "Convolution flips the kernel by 180° ($h(-m,-n)$) to preserve associative and commutative algebraic properties, whereas cross-correlation slides the kernel unrotated. For anti-symmetric kernels like Sobel, convolution and correlation differ by a minus sign."
    },
    {
        "id": 40693,
        "subject": "DIP",
        "topicId": "06_LSI_Systems_2D_Convolution_and_Spatial_Filtering",
        "topicTitle": "06 · LSI Systems, Convolution & Filtering",
        "title": "Unsharp Masking & High-Boost Spatial Filter (IISc Midterm / Gonzalez & Woods)",
        "kind2": "generated",
        "source": "IISc Midterm / Gonzalez & Woods Digital Image Processing",
        "marks": "[8 Marks]",
        "question": """<p>Unsharp masking enhances fine details by subtracting a blurred version of the image from itself:
$$g_{\\text{mask}}(x, y) = f(x, y) - \\bar{f}(x, y)$$
where $\\bar{f} = f ** h_{\\text{blur}}$. High-boost filtering generalizes this via:
$$g(x, y) = f(x, y) + k \\cdot g_{\\text{mask}}(x, y), \\quad k \\ge 1$$</p>
<p><span class="part">(a)</span> For a $3 \\times 3$ averaging box filter $h_{\\text{blur}} = \\frac{1}{9}\\mathbf{1}\\mathbf{1}^\\top$, derive the single equivalent $3 \\times 3$ convolution kernel $h_{\\text{HB}}$ for $k = 1$ (unsharp masking) and $k = 2$ (high-boost).</p>
<p><span class="part">(b)</span> Prove that the DC gain (sum of kernel weights) of $h_{\\text{HB}}$ is identically 1 for all $k$, preserving average image brightness.</p>
<p><span class="part">(c)</span> Analyze the behavior for $k < 1$, $k = 1$, and $k > 1$ in terms of frequency response and edge ringing.</p>""",
        "solution": """<p><span class="part">Part (a): Equivalent Convolution Kernels</span><br>
Rewrite the high-boost operation in terms of LTI convolution:
$$g = f + k(f - f ** h_{\\text{blur}}) = (1 + k)f - k(f ** h_{\\text{blur}}) = f ** \\left[ (1 + k)\\delta - k h_{\\text{blur}} \\right]$$
The discrete impulse (identity filter) is $\\delta = \\begin{pmatrix} 0 & 0 & 0 \\\\ 0 & 1 & 0 \\\\ 0 & 0 & 0 \\end{pmatrix}$.
$$h_{\\text{HB}} = (1 + k)\\begin{pmatrix} 0 & 0 & 0 \\\\ 0 & 1 & 0 \\\\ 0 & 0 & 0 \\end{pmatrix} - \\frac{k}{9}\\begin{pmatrix} 1 & 1 & 1 \\\\ 1 & 1 & 1 \\\\ 1 & 1 & 1 \\end{pmatrix}$$
1. <strong>For $k = 1$ (Standard Unsharp Masking):</strong>
$$h_{\\text{HB}} = 2\\begin{pmatrix} 0 & 0 & 0 \\\\ 0 & 1 & 0 \\\\ 0 & 0 & 0 \\end{pmatrix} - \\frac{1}{9}\\begin{pmatrix} 1 & 1 & 1 \\\\ 1 & 1 & 1 \\\\ 1 & 1 & 1 \\end{pmatrix} = \\frac{1}{9}\\begin{pmatrix} -1 & -1 & -1 \\\\ -1 & 18-1 & -1 \\\\ -1 & -1 & -1 \\end{pmatrix} = <span class=\"ans\">\\frac{1}{9}\\begin{pmatrix} -1 & -1 & -1 \\\\ -1 & 17 & -1 \\\\ -1 & -1 & -1 \\end{pmatrix}</span>$$
2. <strong>For $k = 2$ (High-Boost Filtering):</strong>
$$h_{\\text{HB}} = 3\\begin{pmatrix} 0 & 0 & 0 \\\\ 0 & 1 & 0 \\\\ 0 & 0 & 0 \\end{pmatrix} - \\frac{2}{9}\\begin{pmatrix} 1 & 1 & 1 \\\\ 1 & 1 & 1 \\\\ 1 & 1 & 1 \\end{pmatrix} = \\frac{1}{9}\\begin{pmatrix} -2 & -2 & -2 \\\\ -2 & 27-2 & -2 \\\\ -2 & -2 & -2 \\end{pmatrix} = <span class=\"ans\">\\frac{1}{9}\\begin{pmatrix} -2 & -2 & -2 \\\\ -2 & 25 & -2 \\\\ -2 & -2 & -2 \\end{pmatrix}</span>$$</p>

<p><span class="part">Part (b): Proof of Unit DC Gain</span><br>
The DC gain corresponds to the frequency response at $(u, v) = (0, 0)$, given by the sum of kernel weights:
$$\\sum_{m, n} h_{\\text{HB}}(m, n) = (1 + k) \\sum_{m, n} \\delta(m, n) - k \\sum_{m, n} h_{\\text{blur}}(m, n)$$
Since $\\sum \\delta = 1$ and the box filter is normalized $\\sum h_{\\text{blur}} = 1$:
<span class="ans">$$\\sum_{m, n} h_{\\text{HB}}(m, n) = (1 + k)(1) - k(1) = 1 + k - k = 1, \\quad \\forall k$$</span>
Check for $k = 1$: $\\frac{17 - 8(1)}{9} = \\frac{9}{9} = 1$. Check for $k = 2$: $\\frac{25 - 8(2)}{9} = \\frac{25 - 16}{9} = \\frac{9}{9} = 1$. The overall average image luminance is perfectly preserved.</p>

<p><span class="part">Part (c): Filter Regime Analysis</span><br>
In frequency domain: $H_{\\text{HB}}(u, v) = 1 + k(1 - H_{\\text{LP}}(u, v)) = 1 + k H_{\\text{HP}}(u, v)$.
- <strong>$k < 1$:</strong> De-emphasis; mild edge enhancement without noise amplification.
- <strong>$k = 1$:</strong> Standard unsharp masking; adds true high-pass Laplacian edges to original image, sharpening visual boundaries.
- <strong>$k > 1$:</strong> High-boost; the high-frequency edge component is magnified $k$-fold relative to the base image, overcoming severe blur but potentially introducing halo ringing and amplifying high-frequency sensor noise.</p>""",
        "takeaway": "High-boost filtering $h_{\\text{HB}} = (1+k)\\delta - k h_{\\text{blur}}$ amplifies high-frequency edge detail while strictly maintaining unit DC gain ($\\sum h_{\\text{HB}} = 1$), keeping mean image luminance intact."
    }
]

def main():
    with open(PRACTICE_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    if "40591" in content:
        print("Batch 05-06 already present in practice_dip.js!")
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
    for card in PRACTICE_DIP_05_06:
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

    print("Successfully added DIP Batch 05-06 (6 cards). Total in file now updated.")

if __name__ == "__main__":
    main()
