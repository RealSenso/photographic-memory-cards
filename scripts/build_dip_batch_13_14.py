#!/usr/bin/env python3
"""
Builder script for DIP Practice Cards: Batch 07 (Topics 13 & 14)
Topic 13: Image Quality Assessment: MSE, PSNR, and SSIM (Cards 41391, 41392, 41393)
Topic 14: Edge Detection: Gradients, LoG, and Canny (Cards 41491, 41492, 41493)
"""

import json
import os
import re

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRACTICE_FILE = os.path.join(REPO_DIR, "practice_dip.js")

PRACTICE_DIP_13_14 = [
    # =========================================================================
    # TOPIC 13: Image Quality Assessment: MSE, PSNR, and SSIM
    # =========================================================================
    {
        "id": 41391,
        "subject": "DIP",
        "topicId": "13_Image_Quality_Assessment_MSE_PSNR_and_SSIM",
        "topicTitle": "13 · Quality: MSE, PSNR & SSIM",
        "title": "SSIM vs. MSE Perception Discrepancy: Luminance Shift vs Contrast Halving (IISc Midterm / Wang & Bovik)",
        "kind2": "pyq",
        "source": "IISc Midterm / Wang & Bovik (IEEE TIP 2004)",
        "marks": "[8 Marks]",
        "question": """<p>Let a reference image patch $\\mathbf{x}$ have mean $\\mu_x = 100$ and variance $\\sigma_x^2 = 200$. Consider two degraded patches:</p>
<ul>
  <li><strong>Patch A (Luminance shift):</strong> $\\mathbf{y}_A = \\mathbf{x} + 20$.</li>
  <li><strong>Patch B (Contrast reduction):</strong> $\\mathbf{y}_B = 0.5 \\mathbf{x} + 50$.</li>
</ul>
<p><span class="part">(a)</span> Compute the Mean Squared Error (MSE) and Peak Signal-to-Noise Ratio (PSNR in dB, assuming standard 8-bit dynamic range $\\text{MAX} = 255$) for both Patch A and Patch B.</p>
<p><span class="part">(b)</span> Using stability constants $C_1 = 6.5$ and $C_2 = 58.5$, compute the Structural Similarity Index $\\operatorname{SSIM}(\\mathbf{x}, \\mathbf{y}_A)$.</p>
<p><span class="part">(c)</span> Compute $\\operatorname{SSIM}(\\mathbf{x}, \\mathbf{y}_B)$ and contrast which metric (MSE vs. SSIM) aligns with human visual perception.</p>""",
        "solution": """<p><span class="part">Part (a): Compute MSE and PSNR for Patches A and B</span><br>
1. <strong>Patch A ($\mathbf{y}_A = \mathbf{x} + 20$):</strong><br>
The difference at every pixel is $y_{A,i} - x_i = 20$.
$$\\text{MSE}_A = \\frac{1}{N} \\sum (x_i - (x_i + 20))^2 = 20^2 = <span class=\"ans\">400</span>$$
$$\\text{PSNR}_A = 10 \\log_{10}\\left(\\frac{255^2}{400}\\right) = 10 \\log_{10}\\left(\\frac{65025}{400}\\right) = 10 \\log_{10}(162.56) \\approx <span class=\"ans\">22.11 \\text{ dB}</span>$$

2. <strong>Patch B ($\mathbf{y}_B = 0.5 \\mathbf{x} + 50$):</strong><br>
Mean of B: $\\mu_B = 0.5(100) + 50 = 100$.<br>
Pixel difference: $y_{B,i} - x_i = 0.5 x_i + 50 - x_i = 50 - 0.5 x_i = -0.5(x_i - 100)$.
$$\\text{MSE}_B = \\mathbb{E}[(y_B - x)^2] = 0.25 \\mathbb{E}[(x - 100)^2] = 0.25 \\sigma_x^2 = 0.25(200) = <span class=\"ans\">50</span>$$
$$\\text{PSNR}_B = 10 \\log_{10}\\left(\\frac{65025}{50}\\right) = 10 \\log_{10}(1300.5) \\approx <span class=\"ans\">31.14 \\text{ dB}</span>$$
Notice: MSE ranks Patch B as <strong>8 times superior</strong> to Patch A ($31.14 \\text{ dB}$ vs. $22.11 \\text{ dB}$).</p>

<p><span class="part">Part (b): Compute SSIM for Patch A</span><br>
For Patch A: $\\mu_A = 120$, $\\sigma_A^2 = \\sigma_x^2 = 200$, and cross-covariance $\\sigma_{xA} = \\operatorname{Cov}(\\mathbf{x}, \\mathbf{x} + 20) = \\sigma_x^2 = 200$.
$$\\operatorname{SSIM}(\\mathbf{x}, \\mathbf{y}_A) = \\frac{(2 \\mu_x \\mu_A + C_1)(2 \\sigma_{xA} + C_2)}{(\\mu_x^2 + \\mu_A^2 + C_1)(\\sigma_x^2 + \\sigma_A^2 + C_2)}$$
$$= \\frac{(2(100)(120) + 6.5)(2(200) + 58.5)}{(100^2 + 120^2 + 6.5)(200 + 200 + 58.5)} = \\frac{(24006.5)(458.5)}{(24406.5)(458.5)} = \\frac{24006.5}{24406.5} \\approx <span class=\"ans\">0.9836</span>$$
The structural similarity is virtually perfect ($0.984$), correctly reflecting that image structure, contours, and contrast are 100% intact.</p>

<p><span class="part">Part (c): Compute SSIM for Patch B and Perceptual Alignment</span><br>
For Patch B: $\\mu_B = 100$, $\\sigma_B^2 = (0.5)^2 \\sigma_x^2 = 0.25(200) = 50$, and $\\sigma_{xB} = \\operatorname{Cov}(\\mathbf{x}, 0.5\\mathbf{x} + 50) = 0.5 \\sigma_x^2 = 100$.
$$\\operatorname{SSIM}(\\mathbf{x}, \\mathbf{y}_B) = \\frac{(2(100)(100) + 6.5)(2(100) + 58.5)}{(100^2 + 100^2 + 6.5)(200 + 50 + 58.5)} = \\frac{(20006.5)(258.5)}{(20006.5)(308.5)} = \\frac{258.5}{308.5} \\approx <span class=\"ans\">0.8379</span>$$
<strong>Human Visual System Alignment:</strong><br>
- A uniform DC brightness increase (Patch A) is immediately adapted to by the retina (Weber-Fechner luminance adaptation); the visual structure is crystal clear.<br>
- A 50% loss of contrast (Patch B) heavily washes out details, destroys dynamic range, and appears severely degraded to human observers.<br>
<span class="ans">SSIM correctly rates Patch A ($0.984$) far superior to Patch B ($0.838$)</span>, completely overturning the erroneous conclusion of MSE/PSNR.</p>""",
        "takeaway": "MSE assumes pixel errors are independent and penalizes global DC luminance offsets far too harshly while ignoring severe contrast attenuation. SSIM factorizes image quality into luminance, contrast, and structure, matching human visual perception."
    },
    {
        "id": 41392,
        "subject": "DIP",
        "topicId": "13_Image_Quality_Assessment_MSE_PSNR_and_SSIM",
        "topicTitle": "13 · Quality: MSE, PSNR & SSIM",
        "title": "Analytical Evaluation of Luminance, Contrast & Structure SSIM Triplets (IIT Madras / Bovik IQA)",
        "kind2": "pyq",
        "source": "IIT Madras / Bovik Handbook of Image and Video Processing",
        "marks": "[8 Marks]",
        "question": """<p>Two $4 \\times 4$ grayscale image blocks $X$ and $Y$ are given by:
$$X = \\begin{pmatrix} 10 & 20 & 10 & 20 \\\\ 20 & 10 & 20 & 10 \\\\ 10 & 20 & 10 & 20 \\\\ 20 & 10 & 20 & 10 \\end{pmatrix}, \\qquad Y = \\begin{pmatrix} 12 & 18 & 12 & 18 \\\\ 18 & 12 & 18 & 12 \\\\ 12 & 18 & 12 & 18 \\\\ 18 & 12 & 18 & 12 \\end{pmatrix}$$</p>
<p><span class="part">(a)</span> Compute sample means $\\mu_x$ and $\\mu_y$, sample variances $\\sigma_x^2$ and $\\sigma_y^2$, and sample cross-covariance $\\sigma_{xy}$.</p>
<p><span class="part">(b)</span> With stabilization constants $C_1 = 1.0$, $C_2 = 1.0$, and $C_3 = C_2 / 2 = 0.5$, calculate the three individual SSIM components: luminance $l(x, y)$, contrast $c(x, y)$, and structure $s(x, y)$.</p>
<p><span class="part">(c)</span> Calculate the combined index $\\operatorname{SSIM}(X, Y)$ and compute the sample Pearson correlation coefficient $r_{xy}$.</p>""",
        "solution": """<p><span class="part">Part (a): Compute Means, Variances, and Cross-Covariance</span><br>
Both $4 \\times 4$ blocks contain $N = 16$ pixels (eight pixels of low value, eight of high value).<br>
1. <strong>Means:</strong>
$$\\mu_x = \\frac{8(10) + 8(20)}{16} = \\frac{240}{16} = <span class=\"ans\">15.0</span>$$
$$\\mu_y = \\frac{8(12) + 8(18)}{16} = \\frac{240}{16} = <span class=\"ans\">15.0</span>$$
2. <strong>Variances:</strong>
$$\\sigma_x^2 = \\frac{1}{16} [8(10 - 15)^2 + 8(20 - 15)^2] = \\frac{8(25) + 8(25)}{16} = <span class=\"ans\">25.0</span> \\implies \\sigma_x = 5.0$$
$$\\sigma_y^2 = \\frac{1}{16} [8(12 - 15)^2 + 8(18 - 15)^2] = \\frac{8(9) + 8(9)}{16} = <span class=\"ans\">9.0</span> \\implies \\sigma_y = 3.0$$
3. <strong>Cross-Covariance $\\sigma_{xy}$:</strong><br>
Where $x_i = 10$, $y_i = 12 \\implies (x_i - \\mu_x)(y_i - \\mu_y) = (-5)(-3) = +15$.<br>
Where $x_i = 20$, $y_i = 18 \\implies (x_i - \\mu_x)(y_i - \\mu_y) = (+5)(+3) = +15$.
$$\\sigma_{xy} = \\frac{1}{16} [8(15) + 8(15)] = <span class=\"ans\">15.0</span>$$</p>

<p><span class="part">Part (b): Compute the Three Constituent Components</span><br>
1. <strong>Luminance Comparison $l(x, y)$ ($C_1 = 1.0$):</strong>
$$l(x, y) = \\frac{2\\mu_x\\mu_y + C_1}{\\mu_x^2 + \\mu_y^2 + C_1} = \\frac{2(15)(15) + 1}{15^2 + 15^2 + 1} = \\frac{451}{451} = <span class=\"ans\">1.000</span>$$
2. <strong>Contrast Comparison $c(x, y)$ ($C_2 = 1.0$):</strong>
$$c(x, y) = \\frac{2\\sigma_x\\sigma_y + C_2}{\\sigma_x^2 + \\sigma_y^2 + C_2} = \\frac{2(5)(3) + 1}{25 + 9 + 1} = \\frac{31}{35} \\approx <span class=\"ans\">0.8857</span>$$
3. <strong>Structure Comparison $s(x, y)$ ($C_3 = 0.5$):</strong>
$$s(x, y) = \\frac{\\sigma_{xy} + C_3}{\\sigma_x\\sigma_y + C_3} = \\frac{15 + 0.5}{(5)(3) + 0.5} = \\frac{15.5}{15.5} = <span class=\"ans\">1.000</span>$$</p>

<p><span class="part">Part (c): Total SSIM & Pearson Correlation Coefficient</span><br>
Combining the components:
$$\\operatorname{SSIM}(X, Y) = [l(x, y)] \\cdot [c(x, y)] \\cdot [s(x, y)] = 1.000 \\times 0.8857 \\times 1.000 = <span class=\"ans\">0.8857</span>$$
The Pearson correlation coefficient is:
$$r_{xy} = \\frac{\\sigma_{xy}}{\\sigma_x \\sigma_y} = \\frac{15}{(5)(3)} = <span class=\"ans\">1.000</span>$$
Notice: Structure correlation is mathematically perfect ($r_{xy} = 1.0, s = 1.0$). The only distortion is contrast scaling (the dynamic range was scaled from $\\pm 5$ down to $\\pm 3$), which is isolated completely into the contrast term $c(x, y) = 0.8857$.</p>""",
        "takeaway": "SSIM factorizes cleanly into three physically meaningful, orthogonal terms: luminance comparison l(x,y) (DC match), contrast comparison c(x,y) (variance match), and structural correlation s(x,y) (normalized Pearson cross-correlation)."
    },
    {
        "id": 41393,
        "subject": "DIP",
        "topicId": "13_Image_Quality_Assessment_MSE_PSNR_and_SSIM",
        "topicTitle": "13 · Quality: MSE, PSNR & SSIM",
        "title": "Multi-Scale SSIM (MS-SSIM) Architecture & Video Codec Rate-Distortion Bounds (Generated IISc / IEEE Benchmark)",
        "kind2": "generated",
        "source": "Generated IISc Midterm / IEEE Asilomar (Wang, Simoncelli, Bovik 2003) & ITU-T H.264/HEVC Standards",
        "marks": "[8 Marks]",
        "question": """<p><span class="part">(a)</span> Formulate the Multi-Scale SSIM ($\\text{MS-SSIM}$) index across $M$ dyadic scale levels. Explain why luminance comparison is computed exclusively at the coarsest scale $M$, while contrast and structure are evaluated at every scale $j \\in \\{1, \\dots, M\\}$.</p>
<p><span class="part">(b)</span> In a 5-scale evaluation ($M=5$), the psychophysically calibrated weights are $(\\beta_1, \\beta_2, \\beta_3, \\beta_4, \\beta_5) = (0.0448, 0.2856, 0.3001, 0.2363, 0.1333)$. Relate this distribution of weights to the Human Visual System Contrast Sensitivity Function (CSF).</p>
<p><span class="part">(c)</span> In an HEVC 1080p stream ($1920 \\times 1080$ pixels), the sum of squared differences is $\\text{SSD} = 41,472,000$. Compute the frame MSE and PSNR (for 8-bit depth). Prove analytically that if quantization parameter (QP) adjustments double the MSE, the PSNR drops by exactly $10 \\log_{10}(2) \\approx 3.01 \\text{ dB}$, and state the practical $\\Delta \\text{QP} = +6$ rule.</p>""",
        "solution": """<p><span class="part">Part (a): MS-SSIM Definition & Coarse Luminance Justification</span><br>
Starting from original resolution images at Scale 1, images are recursively low-pass filtered and subsampled by 2 up to scale $M$. The Multi-Scale SSIM index is:
<span class=\"ans\">$$\\text{MS-SSIM}(\\mathbf{x}, \\mathbf{y}) = [l_M(\\mathbf{x}, \\mathbf{y})]^{\\alpha_M} \\cdot \\prod_{j=1}^M [c_j(\\mathbf{x}, \\mathbf{y})]^{\\beta_j} \\cdot [s_j(\\mathbf{x}, \\mathbf{y})]^{\\gamma_j}$$</span>
<strong>Why Luminance only at scale $M$:</strong><br>
Luminance $l(x, y)$ measures difference in mean intensity $\\mu$. Because downsampling preserves local and global mean intensity, calculating luminance comparisons at fine scales yields redundant information. Perception of ambient illumination is an inherently low-spatial-frequency phenomenon best captured at the coarsest pyramid scale. Conversely, fine textures and sharp contours are scale-specific, requiring contrast $c_j$ and structure $s_j$ to be probed across all resolution levels.</p>

<p><span class="part">Part (b): CSF Alignment of 5-Scale Weights</span><br>
In standard MS-SSIM, $\\beta_j = \\gamma_j$ and $\\alpha_5 = \\beta_5 = \\gamma_5$.<br>
The weights peak at intermediate scales 2 and 3:
$$\\beta_1 = 0.0448 < \\beta_5 = 0.1333 < \\beta_4 = 0.2363 < \\beta_2 = 0.2856 < \\beta_3 = 0.3001$$
This mirrors the human visual system's <strong>Contrast Sensitivity Function (CSF)</strong>: the eye acts as a spatial bandpass filter with peak sensitivity at intermediate spatial frequencies (around 4 to 8 cycles/degree), attenuating both very low frequencies (due to neural lateral inhibition) and very high frequencies (due to corneal/lens optical limits and photoreceptor density).</p>

<p><span class="part">Part (c): PSNR Derivation & Codec QP Scaling</span><br>
Total pixels $N = 1920 \\times 1080 = 2,073,600$.
$$\\text{MSE} = \\frac{\\text{SSD}}{N} = \\frac{41,472,000}{2,073,600} = <span class=\"ans\">20.0</span>$$
$$\\text{PSNR} = 10 \\log_{10}\\left(\\frac{255^2}{\\text{MSE}}\\right) = 10 \\log_{10}\\left(\\frac{65025}{20}\\right) = 10 \\log_{10}(3251.25) \\approx <span class=\"ans\">35.12 \\text{ dB}</span>$$
<strong>Effect of Doubling MSE:</strong><br>
If $\\text{MSE}' = 2 \\cdot \\text{MSE}$:
$$\\text{PSNR}' = 10 \\log_{10}\\left(\\frac{255^2}{2 \\cdot \\text{MSE}}\\right) = 10 \\log_{10}\\left(\\frac{255^2}{\\text{MSE}}\\right) - 10 \\log_{10}(2) = \\text{PSNR} - 3.0103 \\text{ dB}$$
<span class=\"ans\">PSNR drops by exactly $3.01 \\text{ dB}$.</span><br>
<strong>Codec Rule of Thumb:</strong> In modern codecs (H.264 / HEVC / VVC), the quantization step size doubles every 6 QP steps ($Q_{\\text{step}} \\propto 2^{\\text{QP}/6}$). Therefore, increasing $\\text{QP}$ by $+6$ roughly <strong>halves the bitrate</strong> (50% compression savings) while causing a predictable <strong>$\\approx 3 \\text{ to } 4 \\text{ dB}$ drop</strong> in PSNR.</p>""",
        "takeaway": "MS-SSIM evaluates multi-resolution structural similarity to account for viewing distance variability, weighted by the human Contrast Sensitivity Function. In video coding, ΔQP = +6 doubles quantization step size, halving bitrate while reducing PSNR by ~3.01 dB."
    },

    # =========================================================================
    # TOPIC 14: Edge Detection: Gradients, LoG, and Canny
    # =========================================================================
    {
        "id": 41491,
        "subject": "DIP",
        "topicId": "14_Edge_Detection_Gradients_LoG_and_Canny",
        "topicTitle": "14 · Edges: Gradients, LoG & Canny",
        "title": "Laplacian of Gaussian (LoG) Derivation & Zero-Crossing Radius (IISc Midterm / Marr & Hildreth)",
        "kind2": "pyq",
        "source": "IISc Midterm / Marr & Hildreth (Proc. R. Soc. Lond. B 1980)",
        "marks": "[8 Marks]",
        "question": """<p>Starting from the continuous 2D circular Gaussian smoothing function:
$$G(x, y; \\sigma) = \\frac{1}{2\\pi \\sigma^2} \\exp\\left(-\\frac{x^2 + y^2}{2\\sigma^2}\\right)$$</p>
<p><span class="part">(a)</span> Compute the first partial derivatives $\\frac{\\partial G}{\\partial x}$ and $\\frac{\\partial G}{\\partial y}$.</p>
<p><span class="part">(b)</span> Compute the second partial derivatives $\\frac{\\partial^2 G}{\\partial x^2}$ and $\\frac{\\partial^2 G}{\\partial y^2}$, and sum them to obtain the analytical expression for the <strong>Laplacian of Gaussian</strong> $\\nabla^2 G(x, y; \\sigma)$.</p>
<p><span class="part">(c)</span> Determine the exact radius $r = \\sqrt{x^2 + y^2}$ at which the zero-crossing of $\\nabla^2 G$ occurs in terms of $\\sigma$, and explain the Mexican-hat profile geometry.</p>""",
        "solution": """<p><span class="part">Part (a): First Partial Derivatives</span><br>
Let $r^2 = x^2 + y^2$. Differentiating with respect to $x$:
$$\\frac{\\partial G}{\\partial x} = \\frac{1}{2\\pi \\sigma^2} e^{-\\frac{x^2+y^2}{2\\sigma^2}} \\left(-\\frac{2x}{2\\sigma^2}\\right) = <span class=\"ans\">-\\frac{x}{2\\pi \\sigma^4} \\exp\\left(-\\frac{x^2 + y^2}{2\\sigma^2}\\right)</span>$$
By radial symmetry, differentiating with respect to $y$ gives:
$$\\frac{\\partial G}{\\partial y} = <span class=\"ans\">-\\frac{y}{2\\pi \\sigma^4} \\exp\\left(-\\frac{x^2 + y^2}{2\\sigma^2}\\right)</span>$$</p>

<p><span class="part">Part (b): Second Partial Derivatives & Laplacian of Gaussian</span><br>
Apply the product rule to $\\frac{\\partial G}{\\partial x}$:
$$\\frac{\\partial^2 G}{\\partial x^2} = \\frac{\\partial}{\\partial x}\\left[ -\\frac{x}{2\\pi \\sigma^4} e^{-\\frac{r^2}{2\\sigma^2}} \\right] = -\\frac{1}{2\\pi \\sigma^4} e^{-\\frac{r^2}{2\\sigma^2}} - \\frac{x}{2\\pi \\sigma^4} \\left(-\\frac{x}{\\sigma^2}\\right) e^{-\\frac{r^2}{2\\sigma^2}}$$
$$= \\frac{1}{2\\pi \\sigma^4} \\left(\\frac{x^2}{\\sigma^2} - 1\\right) e^{-\\frac{x^2+y^2}{2\\sigma^2}}$$
Similarly for $y$:
$$\\frac{\\partial^2 G}{\\partial y^2} = \\frac{1}{2\\pi \\sigma^4} \\left(\\frac{y^2}{\\sigma^2} - 1\\right) e^{-\\frac{x^2+y^2}{2\\sigma^2}}$$
Summing the two second derivatives gives the 2D Laplacian:
$$\\nabla^2 G(x, y; \\sigma) = \\frac{\\partial^2 G}{\\partial x^2} + \\frac{\\partial^2 G}{\\partial y^2} = \\frac{1}{2\\pi \\sigma^4} \\left[ \\frac{x^2 + y^2}{\\sigma^2} - 2 \\right] e^{-\\frac{x^2+y^2}{2\\sigma^2}}$$
<span class=\"ans\">$$\\nabla^2 G(x, y; \\sigma) = \\frac{1}{\\pi \\sigma^4} \\left[ \\frac{x^2 + y^2}{2\\sigma^2} - 1 \\right] \\exp\\left(-\\frac{x^2 + y^2}{2\\sigma^2}\\right)$$</span>
(Note: Often defined with an inverted negative sign $-\\nabla^2 G$ to produce a positive central peak).</p>

<p><span class="part">Part (c): Zero-Crossing Radius & Profile Geometry</span><br>
The zero-crossing occurs where $\\nabla^2 G(x, y; \\sigma) = 0$:
$$\\frac{x^2 + y^2}{2\\sigma^2} - 1 = 0 \\implies x^2 + y^2 = 2\\sigma^2 \\implies <span class=\"ans\">r = \\sqrt{2}\\sigma \\approx 1.414 \\sigma</span>$$
<strong>Mexican-Hat Profile:</strong><br>
- At the origin $r = 0$, $-\\nabla^2 G(0, 0) = \\frac{1}{\\pi \\sigma^4} > 0$ (sharp positive center).<br>
- The profile decays radially, crossing zero at exactly $r = \\sqrt{2}\\sigma$.<br>
- For $r > \\sqrt{2}\\sigma$, it forms a negative circular valley reaching a minimum before decaying asymptotically to zero.<br>
This isotropic center-surround receptive field detects edges precisely at zero-crossing locations with rotational invariance.</p>""",
        "takeaway": "The Laplacian of Gaussian (LoG) is an isotropic second-order edge operator whose zero-crossings locate edge inflection points. Its zero-crossing radius is precisely r = √2 σ."
    },
    {
        "id": 41492,
        "subject": "DIP",
        "topicId": "14_Edge_Detection_Gradients_LoG_and_Canny",
        "topicTitle": "14 · Edges: Gradients, LoG & Canny",
        "title": "Non-Maximum Suppression (NMS) Direction Quantization & Edge Thinning (IISc Midterm / Stanford CS231A)",
        "kind2": "pyq",
        "source": "IISc Midterm / Stanford CS231A Computer Vision",
        "marks": "[8 Marks]",
        "question": """<p>In Canny edge detection, gradient magnitude $M(x, y)$ and continuous gradient orientation $\\theta(x, y)$ (in degrees) are given for a $3 \\times 3$ image patch:
$$M = \\begin{pmatrix} 40 & 75 & 30 \\\\ 50 & \\mathbf{80} & 45 \\\\ 20 & 70 & 25 \\end{pmatrix}, \\qquad \\theta = \\begin{pmatrix} 85^\\circ & 92^\\circ & 88^\\circ \\\\ 91^\\circ & \\mathbf{93^\\circ} & 89^\\circ \\\\ 87^\\circ & 90^\\circ & 94^\\circ \\end{pmatrix}$$</p>
<p><span class="part">(a)</span> Quantize the gradient direction of the center pixel $(1, 1)$ where $\\theta = 93^\\circ$ into one of the 4 canonical Canny edge sectors ($0^\\circ, 45^\\circ, 90^\\circ, 135^\\circ$).</p>
<p><span class="part">(b)</span> Identify the two neighboring pixels along the gradient normal that must be checked for local maximum status.</p>
<p><span class="part">(c)</span> Execute the Non-Maximum Suppression (NMS) comparison: state whether the center pixel survives as a candidate edge or is suppressed to zero, and explain why NMS is essential for 1-pixel-thick boundaries.</p>""",
        "solution": """<p><span class="part">Part (a): Quantize Gradient Direction</span><br>
The gradient direction represents the direction of maximum intensity change. The 4 canonical angular sectors (exploiting $180^\\circ$ edge symmetry) are:
<ul>
  <li><strong>Sector 0 ($0^\\circ$, Horizontal gradient / Vertical edge):</strong> $[-22.5^\\circ, 22.5^\\circ) \\cup [157.5^\\circ, 202.5^\\circ)$</li>
  <li><strong>Sector 1 ($45^\\circ$, Diagonal gradient):</strong> $[22.5^\\circ, 67.5^\\circ) \\cup [202.5^\\circ, 247.5^\\circ)$</li>
  <li><strong>Sector 2 ($90^\\circ$, Vertical gradient / Horizontal edge):</strong> $[67.5^\\circ, 112.5^\\circ) \\cup [247.5^\\circ, 292.5^\\circ)$</li>
  <li><strong>Sector 3 ($135^\\circ$, Anti-diagonal gradient):</strong> $[112.5^\\circ, 157.5^\\circ) \\cup [292.5^\\circ, 337.5^\\circ)$</li>
</ul>
Since $\\theta(1, 1) = 93^\\circ \\in [67.5^\\circ, 112.5^\\circ)$, the center pixel is assigned to <span class=\"ans\">Sector 2 ($90^\\circ$, Vertical gradient)</span>.</p>

<p><span class="part">Part (b): Neighbor Pixels along Gradient Normal</span><br>
A vertical gradient ($90^\\circ$) indicates that the image changes intensity vertically along the $y$-axis (meaning the physical edge contour runs horizontally along the $x$-axis).<br>
To verify if $(1, 1)$ is the ridge crest along this normal, we inspect its <strong>top neighbor</strong> and <strong>bottom neighbor</strong>:
<ul>
  <li>Top neighbor at $(0, 1)$: $M(0, 1) = 75$</li>
  <li>Bottom neighbor at $(2, 1)$: $M(2, 1) = 70$</li>
</ul></p>

<p><span class="part">Part (c): NMS Comparison & Decision</span><br>
Center magnitude is $M(1, 1) = 80$. Comparing with the two neighbors along the gradient normal:
$$M(1, 1) = 80 > M(0, 1) = 75 \\quad \\text{and} \\quad M(1, 1) = 80 > M(2, 1) = 70$$
Since $M(1, 1)$ is strictly greater than both neighbors along the direction of maximum gradient, it is a local maximum.<br>
<span class=\"ans\">The center pixel survives NMS: $M_{\\text{NMS}}(1, 1) = 80$.</span><br>
<strong>Why NMS is Essential:</strong><br>
Linear gradient operators (Sobel, Prewitt) produce broad, blurry gradient ridges spanning 3 to 7 pixels across due to spatial smoothing. Non-Maximum Suppression suppresses all non-crest pixels orthogonal to the edge, thinning the blurry response down to an exact <strong>1-pixel-thick candidate boundary</strong>.</p>""",
        "takeaway": "Non-Maximum Suppression (NMS) quantizes gradient directions into 4 sectors (0°, 45°, 90°, 135°) and suppresses any pixel that is not a local maximum along its gradient normal, thinning wide fuzzy gradient ridges into 1-pixel-wide contours."
    },
    {
        "id": 41493,
        "subject": "DIP",
        "topicId": "14_Edge_Detection_Gradients_LoG_and_Canny",
        "topicTitle": "14 · Edges: Gradients, LoG & Canny",
        "title": "Canny Hysteresis Edge Tracking & Heat Equation Equivalence of DoG (Generated IISc / MIT 6.869)",
        "kind2": "generated",
        "source": "Generated IISc Midterm / Canny (IEEE TPAMI 1986) & Lowe / MIT 6.869",
        "marks": "[8 Marks]",
        "question": """<p><span class="part">(a)</span> After Non-Maximum Suppression, a $4 \\times 4$ candidate edge map has gradient magnitudes:
$$M_{\\text{NMS}} = \\begin{pmatrix} 0 & 85 & 0 & 0 \\\\ 0 & 45 & 50 & 0 \\\\ 0 & 0 & 42 & 0 \\\\ 0 & 0 & 0 & 48 \\end{pmatrix}$$
Using hysteresis thresholds $T_{\\text{high}} = 70$ and $T_{\\text{low}} = 40$, trace the complete 8-connected edge tracking algorithm starting from the strong edge seeds and construct the final binary edge map $E(x, y)$.</p>
<p><span class="part">(b)</span> Prove using the heat diffusion equation $\\frac{\\partial G}{\\partial \\sigma} = \\sigma \\nabla^2 G$ that the Difference of Gaussians (DoG) satisfies:
$$G(x, y; k\\sigma) - G(x, y; \\sigma) \\approx (k - 1) \\sigma^2 \\nabla^2 G(x, y; \\sigma)$$</p>
<p><span class="part">(c)</span> Explain why this DoG relationship is computationally decisive in multiscale scale-space feature detection compared to direct LoG filtering.</p>""",
        "solution": """<p><span class="part">Part (a): Hysteresis Edge Tracking Algorithm</span><br>
1. <strong>Pixel Classification ($T_{\\text{high}} = 70, T_{\\text{low}} = 40$):</strong>
<ul>
  <li><strong>Strong edges ($M \\ge 70$):</strong> Pixel $(0, 1)$ with $M = 85$.</li>
  <li><strong>Weak edges ($40 \\le M < 70$):</strong> $(1, 1)$ with $45$, $(1, 2)$ with $50$, $(2, 2)$ with $42$, and $(3, 3)$ with $48$.</li>
  <li><strong>Suppressed background ($M < 40$):</strong> All remaining pixels are $0$.</li>
</ul>
2. <strong>8-Connected Breadth-First Search (BFS) from Strong Seed:</strong>
- Push strong seed $(0, 1)$ to queue $Q$, set $E(0, 1) = 1$.<br>
- Pop $(0, 1)$: Check 8-neighbors. Found weak pixels $(1, 1)$ ($M=45$) and $(1, 2)$ ($M=50$). Both $\\ge T_{\\text{low}}$. Mark $E(1, 1) = 1, E(1, 2) = 1$; push both to $Q$.<br>
- Pop $(1, 1)$: 8-neighbors contain $(2, 2)$ ($M=42 \\ge T_{\\text{low}}$). Mark $E(2, 2) = 1$; push to $Q$.<br>
- Pop $(1, 2)$: 8-neighbors include $(2, 2)$ (already marked).<br>
- Pop $(2, 2)$: Diagonal 8-neighbor is $(3, 3)$ ($M=48 \\ge T_{\\text{low}}$). Mark $E(3, 3) = 1$; push to $Q$.<br>
- Pop $(3, 3)$: No further unvisited weak neighbors. Queue empty.<br>
<span class=\"ans\">Final Binary Edge Map:
$$E = \\begin{pmatrix} 0 & 1 & 0 & 0 \\\\ 0 & 1 & 1 & 0 \\\\ 0 & 0 & 1 & 0 \\\\ 0 & 0 & 0 & 1 \\end{pmatrix}$$</span>
All 4 weak pixels are rescued because a continuous 8-connected path links them to the strong edge seed $(0, 1)$.</p>

<p><span class="part">Part (b): Heat Diffusion Equation Derivation for DoG</span><br>
Let $G(x, y; \\sigma) = \\frac{1}{2\\pi \\sigma^2} e^{-\\frac{r^2}{2\\sigma^2}}$. Differentiating with respect to scale $\\sigma$:
$$\\frac{\\partial G}{\\partial \\sigma} = -\\frac{2}{2\\pi \\sigma^3} e^{-\\frac{r^2}{2\\sigma^2}} + \\frac{1}{2\\pi \\sigma^2} e^{-\\frac{r^2}{2\\sigma^2}} \\left(\\frac{r^2}{\\sigma^3}\\right) = \\frac{1}{2\\pi \\sigma^3} \\left[\\frac{r^2}{\\sigma^2} - 2\\right] e^{-\\frac{r^2}{2\\sigma^2}}$$
Factor out $\\sigma$:
$$\\frac{\\partial G}{\\partial \\sigma} = \\sigma \\left( \\frac{1}{2\\pi \\sigma^4} \\left[\\frac{r^2}{\\sigma^2} - 2\\right] e^{-\\frac{r^2}{2\\sigma^2}} \\right) = <span class=\"ans\">\\sigma \\nabla^2 G(x, y; \\sigma)</span>$$
Using a finite forward difference with scale step $\\Delta \\sigma = k\\sigma - \\sigma = (k - 1)\\sigma$:
$$\\frac{\\partial G}{\\partial \\sigma} \\approx \\frac{G(x, y; k\\sigma) - G(x, y; \\sigma)}{(k - 1)\\sigma}$$
Equating to $\\sigma \\nabla^2 G$:
$$\\frac{G(x, y; k\\sigma) - G(x, y; \\sigma)}{(k - 1)\\sigma} \\approx \\sigma \\nabla^2 G$$
Multiplying both sides by $(k - 1)\\sigma$:
<span class=\"ans\">$$G(x, y; k\\sigma) - G(x, y; \\sigma) \\approx (k - 1) \\sigma^2 \\nabla^2 G(x, y; \\sigma)$$</span>
The constant scale factor $(k - 1)$ does not shift zero-crossing or extrema coordinates.</p>

<p><span class="part">Part (c): Computational Decisiveness in Multiscale Pyramids</span><br>
Direct LoG requires convolving images at multiple scales with large, non-separable 2D second-derivative kernels ($O(K^2 N)$ operations per scale).<br>
In multiscale pyramids (such as SIFT), smoothed Gaussian images $L(x, y, \\sigma) = f * G_\\sigma$ are already computed using fast 1D separable Gaussian filters.<br>
The Difference of Gaussians requires <strong>zero additional convolutions</strong>; it is computed by a single element-wise image subtraction:
$$D(x, y, \\sigma) = L(x, y, k\\sigma) - L(x, y, \\sigma)$$
This provides a huge 10x-50x speedup while yielding scale-normalized Laplacian responses.</p>""",
        "takeaway": "Hysteresis edge tracking uses dual thresholds to eliminate isolated noise while preventing genuine contours from fracturing. Difference of Gaussians (DoG) approximates the scale-normalized LoG via simple subtraction of adjacent blurred images, avoiding expensive 2D LoG convolutions."
    }
]

def main():
    with open(PRACTICE_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    if "41391" in content:
        print("Batch 13-14 already present in practice_dip.js!")
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
    for card in PRACTICE_DIP_13_14:
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

    print("Successfully added DIP Batch 13-14 (6 cards). Total in file now updated.")

if __name__ == "__main__":
    main()
