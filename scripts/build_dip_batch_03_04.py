#!/usr/bin/env python3
"""
Builder script for DIP Practice Cards: Batch 02 (Topics 03 & 04)
Topic 03: Histograms, Point Operations, and Thresholding (Otsu) (Cards 40391, 40392, 40393)
Topic 04: Binary Morphology and Connected Components (Cards 40491, 40492, 40493)
"""

import json
import os
import re

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRACTICE_FILE = os.path.join(REPO_DIR, "practice_dip.js")

PRACTICE_DIP_03_04 = [
    # =========================================================================
    # TOPIC 03: Histograms, Point Operations, and Thresholding (Otsu)
    # =========================================================================
    {
        "id": 40391,
        "subject": "DIP",
        "topicId": "03_Histograms_Point_Operations_and_Thresholding_Otsu",
        "topicTitle": "03 · Histograms, Point Ops & Otsu",
        "title": "Otsu's Thresholding Variance Equivalence Proof (IISc Midterm / Gonzalez & Woods)",
        "kind2": "pyq",
        "source": "IISc Midterm / Gonzalez & Woods Digital Image Processing",
        "marks": "[8 Marks]",
        "question": """<p>In Otsu's global thresholding method, an image histogram with gray levels $\{0, 1, \\dots, L-1\}$ is partitioned by threshold $k$ into two classes: $C_0 = \\{0, \\dots, k\\}$ and $C_1 = \\{k+1, \\dots, L-1\\}$. Between-class variance is defined as:
$$\\sigma_B^2(k) = \\omega_0(k)(\\mu_0(k) - \\mu_T)^2 + \\omega_1(k)(\\mu_1(k) - \\mu_T)^2$$
where $\\omega_0, \\omega_1$ are class probabilities, $\\mu_0, \\mu_1$ are class means, and $\\mu_T$ is the global mean.</p>
<p><span class="part">(a)</span> Prove rigorously that $\\sigma_B^2(k) = \\omega_0(k) \\omega_1(k) (\\mu_0(k) - \\mu_1(k))^2$.</p>
<p><span class="part">(b)</span> Show that it can be simplified to the fast computation formula:
$$\\sigma_B^2(k) = \\frac{[\\mu_T \\omega_0(k) - \\mu(k)]^2}{\\omega_0(k)(1 - \\omega_0(k))}$$
where $\\mu(k) = \\sum_{i=0}^k i p_i$ is the cumulative first-order moment.</p>
<p><span class="part">(c)</span> Prove that maximizing between-class variance $\\sigma_B^2(k)$ is mathematically identical to minimizing within-class variance $\\sigma_W^2(k) = \\omega_0 \\sigma_0^2 + \\omega_1 \\sigma_1^2$.</p>""",
        "solution": """<p><span class="part">Part (a): Factoring Between-Class Variance</span><br>
By total expectation:
$$\\mu_T = \\sum_{i=0}^{L-1} i p_i = \\sum_{i=0}^k i p_i + \\sum_{i=k+1}^{L-1} i p_i = \\omega_0 \\mu_0 + \\omega_1 \\mu_1$$
Using $\\omega_0 + \\omega_1 = 1 \\implies 1 - \\omega_0 = \\omega_1$:
$$\\mu_0 - \\mu_T = \\mu_0 - (\\omega_0 \\mu_0 + \\omega_1 \\mu_1) = \\mu_0(1 - \\omega_0) - \\omega_1 \\mu_1 = \\omega_1(\\mu_0 - \\mu_1)$$
Similarly:
$$\\mu_1 - \\mu_T = \\mu_1 - (\\omega_0 \\mu_0 + \\omega_1 \\mu_1) = \\mu_1(1 - \\omega_1) - \\omega_0 \\mu_0 = -\\omega_0(\\mu_0 - \\mu_1)$$
Substitute these differences into the definition of $\\sigma_B^2(k)$:
$$\\sigma_B^2(k) = \\omega_0 [\\omega_1(\\mu_0 - \\mu_1)]^2 + \\omega_1 [-\\omega_0(\\mu_0 - \\mu_1)]^2 = \\omega_0 \\omega_1^2 (\\mu_0 - \\mu_1)^2 + \\omega_1 \\omega_0^2 (\\mu_0 - \\mu_1)^2$$
Factoring out common terms:
<span class="ans">$$\\sigma_B^2(k) = \\omega_0 \\omega_1 (\\omega_1 + \\omega_0) (\\mu_0 - \\mu_1)^2 = \\omega_0(k) \\omega_1(k) (\\mu_0(k) - \\mu_1(k))^2$$</span></p>

<p><span class="part">Part (b): Fast Cumulative Moment Formulation</span><br>
Recall $\\mu(k) = \\sum_{i=0}^k i p_i = \\omega_0(k) \\mu_0(k)$.
Using $\\mu_T = \\mu(k) + \\omega_1 \\mu_1 \\implies \\mu_1(k) = \\frac{\\mu_T - \\mu(k)}{\\omega_1(k)} = \\frac{\\mu_T - \\mu(k)}{1 - \\omega_0(k)}$.
Compute the mean separation:
$$\\mu_0 - \\mu_1 = \\frac{\\mu(k)}{\\omega_0} - \\frac{\\mu_T - \\mu(k)}{1 - \\omega_0} = \\frac{\\mu(k)(1 - \\omega_0) - \\omega_0(\\mu_T - \\mu(k))}{\\omega_0(1 - \\omega_0)} = \\frac{\\mu(k) - \\omega_0 \\mu_T}{\\omega_0(1 - \\omega_0)}$$
Substituting back into $\\sigma_B^2(k) = \\omega_0(1 - \\omega_0)(\\mu_0 - \\mu_1)^2$:
$$\\sigma_B^2(k) = \\omega_0(1 - \\omega_0) \\left( \\frac{\\mu(k) - \\omega_0 \\mu_T}{\\omega_0(1 - \\omega_0)} \\right)^2 = \\frac{[\\mu_T \\omega_0(k) - \\mu(k)]^2}{\\omega_0(k)(1 - \\omega_0(k))}$$
<span class="ans">This eliminates the need to compute class variances $\\sigma_0^2, \\sigma_1^2$ or recompute means from scratch, allowing $O(L)$ linear-time evaluation via running cumulative sums.</span></p>

<p><span class="part">Part (c): Equivalence of $\\max \\sigma_B^2$ and $\\min \\sigma_W^2$</span><br>
By the total variance decomposition theorem:
$$\\sigma_T^2 = \\sum_{i=0}^{L-1} (i - \\mu_T)^2 p_i = \\sigma_W^2(k) + \\sigma_B^2(k)$$
Because $\\sigma_T^2$ is the variance of the entire image and is completely independent of the threshold $k$:
<span class="ans">$$\\sigma_W^2(k) = \\sigma_T^2 - \\sigma_B^2(k) \\implies \\arg\\min_k \\sigma_W^2(k) = \\arg\\max_k \\sigma_B^2(k)$$</span>
Minimizing within-class spread (compact clusters) is mathematically identical to maximizing between-class separation.</p>""",
        "takeaway": "Otsu's threshold maximizes between-class variance $\\sigma_B^2(k) = \\frac{[\\mu_T \\omega_0(k) - \\mu(k)]^2}{\\omega_0(k)(1-\\omega_0(k))}$, which strictly minimizes within-class variance $\\sigma_W^2(k) = \\sigma_T^2 - \\sigma_B^2(k)$ in $O(L)$ cumulative operations."
    },
    {
        "id": 40392,
        "subject": "DIP",
        "topicId": "03_Histograms_Point_Operations_and_Thresholding_Otsu",
        "topicTitle": "03 · Histograms, Point Ops & Otsu",
        "title": "Numerical Trace of Otsu's Global Thresholding (IISc Midterm / Stanford CS231A)",
        "kind2": "university",
        "source": "IISc Midterm / Stanford CS231A Computer Vision",
        "marks": "[8 Marks]",
        "question": """<p>An 8-bit quantized image has 6 active gray levels $\{0, 1, 2, 3, 4, 5\}$ with normalized histogram probability vector:
$$\\mathbf{p} = [0.10, \\, 0.20, \\, 0.40, \\, 0.10, \\, 0.10, \\, 0.10]$$</p>
<p><span class="part">(a)</span> Compute the global mean intensity $\\mu_T$.</p>
<p><span class="part">(b)</span> For each candidate threshold $k \\in \\{0, 1, 2, 3, 4\\}$, evaluate cumulative probability $\\omega_0(k)$, cumulative mean $\\mu(k)$, and between-class variance $\\sigma_B^2(k)$.</p>
<p><span class="part">(c)</span> Determine the optimal Otsu threshold $k^*$ and specify the resulting binary segmentation rule.</p>""",
        "solution": """<p><span class="part">Part (a): Global Mean $\\mu_T$</span><br>
$$\\mu_T = \\sum_{i=0}^5 i p_i = 0(0.10) + 1(0.20) + 2(0.40) + 3(0.10) + 4(0.10) + 5(0.10)$$
$$= 0 + 0.20 + 0.80 + 0.30 + 0.40 + 0.50 = <span class=\"ans\">2.20</span>$$</p>

<p><span class="part">Part (b): Step-by-Step Variance Evaluation</span><br>
Using $\\sigma_B^2(k) = \\frac{[2.20 \\,\\omega_0(k) - \\mu(k)]^2}{\\omega_0(k)(1 - \\omega_0(k))}$:
1. <strong>$k = 0$:</strong>
- $\\omega_0(0) = 0.10 \\implies \\omega_1 = 0.90$. Denominator $= 0.10 \\times 0.90 = 0.090$.
- $\\mu(0) = 0(0.10) = 0$.
- Numerator $= [2.20(0.10) - 0]^2 = [0.22]^2 = 0.0484$.
<span class="ans">$$\\sigma_B^2(0) = \\frac{0.0484}{0.090} \\approx 0.5378$$</span>
2. <strong>$k = 1$:</strong>
- $\\omega_0(1) = 0.10 + 0.20 = 0.30 \\implies \\omega_1 = 0.70$. Denom $= 0.30 \\times 0.70 = 0.210$.
- $\\mu(1) = 0 + 1(0.20) = 0.20$.
- Numerator $= [2.20(0.30) - 0.20]^2 = [0.66 - 0.20]^2 = [0.46]^2 = 0.2116$.
<span class="ans">$$\\sigma_B^2(1) = \\frac{0.2116}{0.210} \\approx 1.0076$$</span>
3. <strong>$k = 2$:</strong>
- $\\omega_0(2) = 0.30 + 0.40 = 0.70 \\implies \\omega_1 = 0.30$. Denom $= 0.70 \\times 0.30 = 0.210$.
- $\\mu(2) = 0.20 + 2(0.40) = 1.00$.
- Numerator $= [2.20(0.70) - 1.00]^2 = [1.54 - 1.00]^2 = [0.54]^2 = 0.2916$.
<span class="ans">$$\\sigma_B^2(2) = \\frac{0.2916}{0.210} \\approx 1.3886$$</span>
4. <strong>$k = 3$:</strong>
- $\\omega_0(3) = 0.70 + 0.10 = 0.80 \\implies \\omega_1 = 0.20$. Denom $= 0.80 \\times 0.20 = 0.160$.
- $\\mu(3) = 1.00 + 3(0.10) = 1.30$.
- Numerator $= [2.20(0.80) - 1.30]^2 = [1.76 - 1.30]^2 = [0.46]^2 = 0.2116$.
<span class="ans">$$\\sigma_B^2(3) = \\frac{0.2116}{0.160} \\approx 1.3225$$</span>
5. <strong>$k = 4$:</strong>
- $\\omega_0(4) = 0.80 + 0.10 = 0.90 \\implies \\omega_1 = 0.10$. Denom $= 0.90 \\times 0.10 = 0.090$.
- $\\mu(4) = 1.30 + 4(0.10) = 1.70$.
- Numerator $= [2.20(0.90) - 1.70]^2 = [1.98 - 1.70]^2 = [0.28]^2 = 0.0784$.
<span class="ans">$$\\sigma_B^2(4) = \\frac{0.0784}{0.090} \\approx 0.8711$$</span></p>

<p><span class="part">Part (c): Optimal Threshold Selection</span><br>
Comparing variance values:
$$\\sigma_B^2 = [0.5378, \\; 1.0076, \\; \\mathbf{1.3886}, \\; 1.3225, \\; 0.8711]$$
The global maximum is reached at $k = 2$.
<span class="ans">Optimal Otsu Threshold: $k^* = 2$.</span><br>
Segmentation rule:
$$g(x, y) = \\begin{cases} 0 \\text{ (Background)} & \\text{if } f(x, y) \\le 2 \\\\ 1 \\text{ (Foreground)} & \\text{if } f(x, y) > 2 \\end{cases}$$
Classes: Background $C_0 = \\{0, 1, 2\\}$ (70% of pixels), Foreground $C_1 = \\{3, 4, 5\\}$ (30% of pixels).</p>""",
        "takeaway": "Evaluating Otsu thresholding over a 6-bin histogram identifies $k^* = 2$ as the variance maximizer ($\\sigma_B^2 = 1.3886$). Precomputing running sums $\\omega(k)$ and $\\mu(k)$ makes search strictly $O(L)$."
    },
    {
        "id": 40393,
        "subject": "DIP",
        "topicId": "03_Histograms_Point_Operations_and_Thresholding_Otsu",
        "topicTitle": "03 · Histograms, Point Ops & Otsu",
        "title": "Gamma Correction & Dynamic Range Stretching (IIT Bombay / Gonzalez & Woods)",
        "kind2": "generated",
        "source": "IIT Bombay / Gonzalez & Woods Digital Image Processing",
        "marks": "[8 Marks]",
        "question": """<p>In a low-dose medical X-ray scan with normalized intensities $r \\in [0, 1]$, soft tissue details are compressed into the narrow dark range $[r_1, r_2] = [0.05, 0.20]$.</p>
<p><span class="part">(a)</span> A power-law (gamma) transformation $s = r^\\gamma$ with $\\gamma = 0.40$ is applied. Compute the output intensity range $[s_1, s_2]$ and percentage expansion of the dynamic range.</p>
<p><span class="part">(b)</span> Calculate the local derivative gain $\\frac{ds}{dr}$ at input intensity $r = 0.10$. What does $\\frac{ds}{dr} > 1$ indicate for local contrast?</p>
<p><span class="part">(c)</span> Compare gamma transformation with linear piecewise contrast stretching $s = \\frac{r - 0.05}{0.15}$ in terms of boundary clipping and bone saturation.</p>""",
        "solution": """<p><span class="part">Part (a): Dynamic Range Expansion under $\\gamma = 0.40$</span><br>
For input boundaries $r_1 = 0.05$ and $r_2 = 0.20$:
$$s_1 = (0.05)^{0.40} = \\exp(0.40 \\ln 0.05) = \\exp(0.40 \\times (-2.9957)) = \\exp(-1.1983) \\approx <span class=\"ans\">0.3017</span>$$
$$s_2 = (0.20)^{0.40} = \\exp(0.40 \\ln 0.20) = \\exp(0.40 \\times (-1.6094)) = \\exp(-0.6438) \\approx <span class=\"ans\">0.5253</span>$$
Output dynamic range width:
$$\\Delta s = s_2 - s_1 = 0.5253 - 0.3017 = 0.2236$$
Input dynamic range width:
$$\\Delta r = r_2 - r_1 = 0.20 - 0.05 = 0.1500$$
Expansion ratio:
<span class="ans">$$\\frac{\\Delta s}{\\Delta r} = \\frac{0.2236}{0.1500} \\approx 1.491 \\implies 49.1\\% \\text{ expansion}$$</span></p>

<p><span class="part">Part (b): Local Derivative Gain at $r = 0.10$</span><br>
The derivative of power law transformation $s = r^\\gamma$ is:
$$\\frac{ds}{dr} = \\gamma r^{\\gamma - 1} = 0.40 \\, r^{-0.60}$$
At $r = 0.10$:
$$\\frac{ds}{dr}\\bigg|_{r=0.10} = 0.40 \\times (0.10)^{-0.60} = 0.40 \\times 10^{0.60} = 0.40 \\times 3.9811 \\approx <span class=\"ans\">1.5924</span>$$
<strong>Interpretation:</strong> Since $\\frac{ds}{dr} = 1.59 > 1$, local intensity differences around $r = 0.10$ are amplified by $\\approx 59.2\\%$, significantly boosting soft tissue edge sharpness and visibility.</p>

<p><span class="part">Part (c): Gamma vs Piecewise Linear Stretching</span><br>
1. <strong>Piecewise linear stretching $s = \\frac{r - 0.05}{0.15}$:</strong> Expands $[0.05, 0.20]$ to full range $[0, 1]$ with maximum slope $1/0.15 = 6.67$. However, all pixels with $r < 0.05$ clip to 0 (loss of dark background texture), and all bright pixels $r > 0.20$ clip to 1.0 (severe bone saturation / blowout).<br>
2. <strong>Gamma correction $s = r^{0.40}$:</strong> Strictly monotonic map over the entire interval $[0, 1]$ ($0 \\mapsto 0$ and $1 \\mapsto 1$). It smoothly expands dark regions while compressing highlights $[0.8, 1.0]$ without any hard clipping or lost information.<br>
<span class=\"ans\">Gamma correction preserves global dynamic range continuity while amplifying dark-region local contrast.</span></p>""",
        "takeaway": "Gamma correction $s = r^\\gamma$ with $\\gamma < 1$ expands dark regions ($\\frac{ds}{dr} > 1$) and compresses highlights smoothly across $[0, 1]$ without hard clipping, unlike linear window-level stretching."
    },

    # =========================================================================
    # TOPIC 04: Binary Morphology and Connected Components
    # =========================================================================
    {
        "id": 40491,
        "subject": "DIP",
        "topicId": "04_Binary_Morphology_and_Connected_Components",
        "topicTitle": "04 · Binary Morphology & Connected Components",
        "title": "Morphological Boundaries & Duality Theorems (IISc Midterm / Gonzalez & Woods)",
        "kind2": "pyq",
        "source": "IISc Midterm / Gonzalez & Woods Digital Image Processing",
        "marks": "[8 Marks]",
        "question": """<p>Let $A$ be a binary foreground object and $B$ be a $3 \\times 3$ square structuring element centered at $(0, 0)$.</p>
<p><span class="part">(a)</span> Define the <strong>inner boundary</strong> $\\beta_{\\text{inner}}(A)$, <strong>outer boundary</strong> $\\beta_{\\text{outer}}(A)$, and <strong>morphological gradient</strong> $\\beta(A)$ in terms of erosion and dilation.</p>
<p><span class="part">(b)</span> Prove the fundamental <strong>Duality Theorem</strong> between erosion and dilation: $(A \\ominus B)^c = A^c \\oplus \\hat{B}$, where $\\hat{B} = \\{-b : b \\in B\\}$.</p>
<p><span class="part">(c)</span> For a $6 \\times 6$ solid square object $A$, calculate the exact pixel counts of $A$, eroded set $A \\ominus B$, inner boundary $\\beta_{\\text{inner}}(A)$, and outer boundary $\\beta_{\\text{outer}}(A)$.</p>""",
        "solution": """<p><span class="part">Part (a): Morphological Boundary Formulations</span><br>
- <strong>Inner boundary:</strong> $\\beta_{\\text{inner}}(A) = A \\setminus (A \\ominus B) = A \\cap (A \\ominus B)^c$<br>
- <strong>Outer boundary:</strong> $\\beta_{\\text{outer}}(A) = (A \\oplus B) \\setminus A = (A \\oplus B) \\cap A^c$<br>
- <strong>Morphological gradient (thick boundary):</strong> $\\beta(A) = (A \\oplus B) \\setminus (A \\ominus B) = \\beta_{\\text{inner}}(A) \\cup \\beta_{\\text{outer}}(A)$</p>

<p><span class="part">Part (b): Proof of Erosion-Dilation Duality</span><br>
By definition of erosion:
$$A \\ominus B = \\{z \\in \\mathbb{Z}^2 : B_z \\subseteq A\\}$$
Taking the complement:
$$(A \\ominus B)^c = \\{z : B_z \\not\\subseteq A\\} = \\{z : B_z \\cap A^c \\ne \\emptyset\\}$$
The translated structuring element is $B_z = \\{b + z : b \\in B\\}$. The intersection $B_z \\cap A^c \\ne \\emptyset$ means there exists $b \\in B$ such that $b + z \\in A^c$. Let $a = b + z \\implies z = a - b = a + (-b)$.<br>
Since $-b \\in \\hat{B}$:
$$\\{z : B_z \\cap A^c \\ne \\emptyset\\} = \\{a + \\hat{b} : a \\in A^c, \\hat{b} \\in \\hat{B}\\} = A^c \\oplus \\hat{B}$$
<span class=\"ans\">$$(A \\ominus B)^c = A^c \\oplus \\hat{B}$$</span>
Erosion of foreground is mathematically equivalent to dilation of background with reflected structuring element.</p>

<p><span class="part">Part (c): Pixel Counts for $6 \\times 6$ Square</span><br>
1. <strong>Original Object $A$:</strong> Solid square of size $6 \\times 6$:
$$|A| = 6 \\times 6 = <span class=\"ans\">36 \\text{ pixels}</span>$$
2. <strong>Erosion $A \\ominus B$:</strong> $B$ is a $3 \\times 3$ square SE. Center pixel $z$ survives erosion if and only if its entire $3 \\times 3$ neighborhood lies inside $A$, peeling away a 1-pixel perimeter:
$$|A \\ominus B| = (6 - 2) \\times (6 - 2) = 4 \\times 4 = <span class=\"ans\">16 \\text{ pixels}</span>$$
3. <strong>Inner Boundary $\\beta_{\\text{inner}}(A)$:</strong>
$$|\\beta_{\\text{inner}}(A)| = |A| - |A \\ominus B| = 36 - 16 = <span class=\"ans\">20 \\text{ pixels}</span>$$
(Perimeter calculation: $4 \\times 6 - 4 \\text{ corners} = 20$).<br>
4. <strong>Outer Boundary $\\beta_{\\text{outer}}(A)$:</strong> Dilation expands $A$ by 1 pixel in all directions, creating an $8 \\times 8$ square:
$$|A \\oplus B| = 8 \\times 8 = 64 \\text{ pixels}$$
$$|\\beta_{\\text{outer}}(A)| = |A \\oplus B| - |A| = 64 - 36 = <span class=\"ans\">28 \\text{ pixels}</span>$$</p>""",
        "takeaway": "Inner boundary $\\beta_{\\text{inner}} = A \\setminus (A \\ominus B)$ extracts perimeter pixels from within the object. Erosion-dilation duality $(A \\ominus B)^c = A^c \\oplus \\hat{B}$ establishes that background dilation performs foreground erosion."
    },
    {
        "id": 40492,
        "subject": "DIP",
        "topicId": "04_Binary_Morphology_and_Connected_Components",
        "topicTitle": "04 · Binary Morphology & Connected Components",
        "title": "Hit-or-Miss Transform for Corner Detection (IIT Madras / MIT 6.869)",
        "kind2": "university",
        "source": "IIT Madras / MIT 6.869 Computer Vision",
        "marks": "[8 Marks]",
        "question": """<p>The <strong>Hit-or-Miss Transform (HMT)</strong> is a fundamental morphological tool for exact template shape matching:
$$A \\circledast B = (A \\ominus B_1) \\cap (A^c \\ominus B_2)$$
where $B = (B_1, B_2)$ is a composite structuring element with foreground template $B_1$ and disjoint background template $B_2$ ($B_1 \\cap B_2 = \\emptyset$).</p>
<p><span class="part">(a)</span> Design the explicit $3 \\times 3$ foreground template $B_1$ and background template $B_2$ centered at $(0, 0)$ to detect <strong>top-right convex corners</strong> of binary objects.</p>
<p><span class="part">(b)</span> Show the combined ternary structuring element representation using entries $\{1, 0, \\times\}$, where $\\times$ represents 'don't care'.</p>
<p><span class="part">(c)</span> Apply your designed HMT to the $4 \\times 4$ binary patch:
$$A = \\begin{pmatrix}
0 & 0 & 0 & 0 \\\\
0 & 1 & 1 & 0 \\\\
0 & 1 & 1 & 0 \\\\
0 & 0 & 0 & 0
\\end{pmatrix}$$
Identify the exact coordinate detected as the top-right corner.</p>""",
        "solution": """<p><span class="part">Part (a): Design of $B_1$ and $B_2$</span><br>
Let coordinate $(0, 0)$ be the candidate corner pixel.
1. <strong>Foreground Template $B_1$:</strong> For a top-right convex corner, foreground (1 in $A$) must exist at the corner $(0, 0)$, its left neighbor $(-1, 0)$, and its bottom neighbor $(0, -1)$:
$$B_1 = \\begin{pmatrix}
0 & 0 & 0 \\\\
1 & 1 & 0 \\\\
0 & 1 & 0
\\end{pmatrix}$$
2. <strong>Background Template $B_2$:</strong> To guarantee convexity, pixels outside the corner must be strictly background (0 in $A$, hence 1 in $A^c$): immediately top $(0, 1)$, immediately right $(1, 0)$, and top-right diagonal $(1, 1)$:
$$B_2 = \\begin{pmatrix}
0 & 1 & 1 \\\\
0 & 0 & 1 \\\\
0 & 0 & 0
\\end{pmatrix}$$</p>

<p><span class="part">Part (b): Ternary Structuring Element $B = (B_1, B_2)$</span><br>
Combining $B_1$ (requires 1), $B_2$ (requires 0), and unconstrained locations (don't care $\\times$):
<span class="ans">$$B = \\begin{pmatrix}
\\times & 0 & 0 \\\\
1 & 1 & 0 \\\\
\\times & 1 & \\times
\\end{pmatrix}$$</span>
Here, the center element is 1 (corner itself), right and top are 0 (empty exterior), left and bottom are 1 (solid interior), and $\\times$ positions can be either 0 or 1.</p>

<p><span class="part">Part (c): Application to $4 \\times 4$ Square</span><br>
In patch $A$, the $2 \\times 2$ solid square occupies rows 2-3 and columns 2-3 (1-indexed):
$$A = \\begin{pmatrix}
0 & 0 & 0 & 0 \\\\
0 & 1 & 1 & 0 \\\\
0 & 1 & 1 & 0 \\\\
0 & 0 & 0 & 0
\\end{pmatrix}$$
Let us test candidate pixel $(r, c) = (2, 3)$:
- Center $(2, 3) = 1$ (matches $B_1$)
- Left $(2, 2) = 1$ (matches $B_1$)
- Down $(3, 3) = 1$ (matches $B_1$) $\\implies (2, 3) \\in (A \\ominus B_1)$
- Top $(1, 3) = 0$ (matches $B_2$)
- Right $(2, 4) = 0$ (matches $B_2$)
- Top-right $(1, 4) = 0$ (matches $B_2$) $\\implies (2, 3) \\in (A^c \\ominus B_2)$<br>
Both conditions hold simultaneously:
$$(2, 3) \\in (A \\ominus B_1) \\cap (A^c \\ominus B_2)$$
For all other pixels in $A$, at least one foreground or background condition fails.<br>
<span class=\"ans\">The Hit-or-Miss transform outputs an isolated single pixel at row 2, column 3: $(A \\circledast B)_{2, 3} = 1$, correctly identifying the unique top-right corner.</span></p>""",
        "takeaway": "Hit-or-Miss transform $A \\circledast B = (A \\ominus B_1) \\cap (A^c \\ominus B_2)$ simultaneously matches foreground ($B_1$) and background ($B_2$). Unconstrained entries are designated 'don't care' ($\\times$)."
    },
    {
        "id": 40493,
        "subject": "DIP",
        "topicId": "04_Binary_Morphology_and_Connected_Components",
        "topicTitle": "04 · Binary Morphology & Connected Components",
        "title": "Two-Pass Connected Component Labeling with Union-Find (IISc Midterm / Stanford CS231A)",
        "kind2": "generated",
        "source": "IISc Midterm / Stanford CS231A Computer Vision",
        "marks": "[8 Marks]",
        "question": """<p>Consider the following $4 \\times 5$ binary image with <strong>4-connectivity</strong>:
$$A = \\begin{pmatrix}
1 & 1 & 0 & 1 & 1 \\\\
1 & 0 & 0 & 0 & 1 \\\\
0 & 0 & 1 & 0 & 0 \\\\
1 & 1 & 1 & 0 & 1
\\end{pmatrix}$$</p>
<p><span class="part">(a)</span> Trace the <strong>First Pass</strong> of the classical 2-pass labeling algorithm (raster scan row-by-row, top-to-bottom, left-to-right), assigning provisional labels and recording equivalence pairs.</p>
<p><span class="part">(b)</span> Resolve label equivalences using the <strong>Disjoint-Set (Union-Find)</strong> data structure to find connected components.</p>
<p><span class="part">(c)</span> Write down the final labeled matrix after the <strong>Second Pass</strong> and determine the total number of connected components.</p>""",
        "solution": """<p><span class="part">Part (a): First Pass Raster Scan</span><br>
For pixel $p$ at $(r, c)$, 4-connectivity inspects top neighbor $T = (r-1, c)$ and left neighbor $L = (r, c-1)$:
- <strong>Row 1:</strong>
  - $(1, 1)=1$: No top/left $\\to$ new label <span class=\"ans\">1</span>
  - $(1, 2)=1$: Left is 1 $\\to$ copy label <span class=\"ans\">1</span>
  - $(1, 3)=0$: background
  - $(1, 4)=1$: No top/left $\\to$ new label <span class=\"ans\">2</span>
  - $(1, 5)=1$: Left is 2 $\\to$ copy label <span class=\"ans\">2</span><br>
  <em>Row 1:</em> $[1, 1, 0, 2, 2]$
- <strong>Row 2:</strong>
  - $(2, 1)=1$: Top is 1 $\\to$ copy label <span class=\"ans\">1</span>
  - $(2, 2)=0, (2, 3)=0, (2, 4)=0$: background
  - $(2, 5)=1$: Top is 2 $\\to$ copy label <span class=\"ans\">2</span><br>
  <em>Row 2:</em> $[1, 0, 0, 0, 2]$
- <strong>Row 3:</strong>
  - $(3, 1)=0, (3, 2)=0$: background
  - $(3, 3)=1$: Top is 0, left is 0 $\\to$ new label <span class=\"ans\">3</span>
  - $(3, 4)=0, (3, 5)=0$: background<br>
  <em>Row 3:</em> $[0, 0, 3, 0, 0]$
- <strong>Row 4:</strong>
  - $(4, 1)=1$: Top is 0, left is 0 $\\to$ new label <span class=\"ans\">4</span>
  - $(4, 2)=1$: Left is 4 $\\to$ copy label <span class=\"ans\">4</span>
  - $(4, 3)=1$: Top is 3, left is 4! Both neighbors are labeled and distinct ($3 \\ne 4$). Copy $\\min(3, 4) = 3$ and record equivalence: <span class=\"ans\">$3 \\equiv 4$</span>
  - $(4, 4)=0$: background
  - $(4, 5)=1$: Top is 0, left is 0 $\\to$ new label <span class=\"ans\">5</span><br>
  <em>Row 4:</em> $[4, 4, 3, 0, 5]$</p>

<p><span class="part">Part (b): Equivalence Resolution via Union-Find</span><br>
Equivalence table contains: $\\{3 \\equiv 4\\}$.<br>
Disjoint set forest:
- Set 1: $\\{1\\} \\to$ canonical root <strong>1</strong>
- Set 2: $\\{2\\} \\to$ canonical root <strong>2</strong>
- Set 3: $\\{3, 4\\} \\to$ merged with canonical root <strong>3</strong>
- Set 4: $\\{5\\} \\to$ canonical root <strong>4</strong> (compacted label index)</p>

<p><span class="part">Part (c): Second Pass & Final Labeled Matrix</span><br>
Replace every provisional label by its canonical root ($1 \\mapsto 1, 2 \\mapsto 2, 3 \\mapsto 3, 4 \\mapsto 3, 5 \\mapsto 4$):
<span class="ans">$$L = \\begin{pmatrix}
1 & 1 & 0 & 2 & 2 \\\\
1 & 0 & 0 & 0 & 2 \\\\
0 & 0 & 3 & 0 & 0 \\\\
3 & 3 & 3 & 0 & 4
\\end{pmatrix}$$</span>
<span class="ans">Total number of connected components = 4.</span><br>
(Component 1: top-left corner of 3 pixels; Component 2: top-right corner of 3 pixels; Component 3: inverted T-structure of 4 pixels; Component 4: isolated bottom-right pixel).</p>""",
        "takeaway": "Two-pass connected component labeling scans raster order: Pass 1 assigns provisional labels and logs neighbor conflicts $L_1 \\equiv L_2$ into a Union-Find table; Pass 2 flattens equivalence trees to assign consecutive canonical IDs."
    }
]

def main():
    with open(PRACTICE_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    if "40391" in content:
        print("Batch 03-04 already present in practice_dip.js!")
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
    for card in PRACTICE_DIP_03_04:
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

    print("Successfully added DIP Batch 03-04 (6 cards). Total in file now updated.")

if __name__ == "__main__":
    main()
