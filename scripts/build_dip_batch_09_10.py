#!/usr/bin/env python3
"""
Builder script for DIP Practice Cards: Batch 05 (Topics 09 & 10)
Topic 09: Discrete Cosine Transform (DCT) and Karhunen-Loève Transform (KLT) (Cards 40991, 40992, 40993)
Topic 10: Wavelets and Multiresolution Analysis (Cards 41091, 41092, 41093)
"""

import json
import os
import re

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRACTICE_FILE = os.path.join(REPO_DIR, "practice_dip.js")

PRACTICE_DIP_09_10 = [
    # =========================================================================
    # TOPIC 09: Discrete Cosine Transform (DCT) and Karhunen-Loève Transform (KLT)
    # =========================================================================
    {
        "id": 40991,
        "subject": "DIP",
        "topicId": "09_Discrete_Cosine_Transform_DCT_and_KLT",
        "topicTitle": "09 · DCT & KLT",
        "title": "Karhunen-Loève Transform (KLT / PCA) & Energy Compaction (IISc Midterm / Gonzalez & Woods)",
        "kind2": "pyq",
        "source": "IISc Midterm / Gonzalez & Woods Digital Image Processing",
        "marks": "[8 Marks]",
        "question": """<p>A zero-mean image ensemble produces $2 \\times 1$ feature vectors $\\mathbf{x} = (x_1, x_2)^\\top$ with spatial covariance matrix:
$$\\Sigma_{\\mathbf{x}} = \\begin{pmatrix} 4 & 3 \\\\ 3 & 4 \\end{pmatrix}$$</p>
<p><span class="part">(a)</span> Compute the eigenvalues $\\lambda_1, \\lambda_2$ and orthonormal eigenvectors $\\boldsymbol{\\phi}_1, \\boldsymbol{\\phi}_2$ of $\\Sigma_{\\mathbf{x}}$.</p>
<p><span class="part">(b)</span> Form the forward Karhunen-Loève Transform (KLT) matrix $A = \\begin{pmatrix} \\boldsymbol{\\phi}_1^\\top \\\\ \\boldsymbol{\\phi}_2^\\top \\end{pmatrix}$ and transform sample vector $\\mathbf{x}_0 = (2, -1)^\\top$ into transform coefficients $\\mathbf{y}_0 = A \\mathbf{x}_0$. Verify that the coefficient covariance $\\Sigma_{\\mathbf{y}} = A \\Sigma_{\\mathbf{x}} A^\\top$ is diagonal.</p>
<p><span class="part">(c)</span> If the representation is compressed by keeping only $m = 1$ principal component, reconstruct $\\hat{\\mathbf{x}}_0$ and calculate the theoretical Mean Squared Error (MSE).</p>""",
        "solution": """<p><span class="part">Part (a): Eigenvalues & Orthonormal Eigenvectors</span><br>
The characteristic equation is $\\det(\\Sigma_{\\mathbf{x}} - \\lambda I) = 0$:
$$\\det\\begin{pmatrix} 4 - \\lambda & 3 \\\\ 3 & 4 - \\lambda \\end{pmatrix} = (4 - \\lambda)^2 - 9 = 0 \\implies 4 - \\lambda = \\pm 3$$
The eigenvalues are:
<span class="ans">$$\\lambda_1 = 7, \\qquad \\lambda_2 = 1$$</span>
Total variance is $\\text{Tr}(\\Sigma_{\\mathbf{x}}) = 4 + 4 = 8 = \\lambda_1 + \\lambda_2$.
1. <strong>Eigenvector for $\\lambda_1 = 7$:</strong>
$$(\\Sigma - 7I)\\mathbf{v}_1 = \\begin{pmatrix} -3 & 3 \\\\ 3 & -3 \\end{pmatrix} \\begin{pmatrix} v_{11} \\\\ v_{12} \\end{pmatrix} = \\begin{pmatrix} 0 \\\\ 0 \\end{pmatrix} \\implies v_{11} = v_{12} \\implies \\boldsymbol{\\phi}_1 = <span class=\"ans\">\\frac{1}{\\sqrt{2}}\\begin{pmatrix} 1 \\\\ 1 \\end{pmatrix}</span>$$
2. <strong>Eigenvector for $\\lambda_2 = 1$:</strong>
$$(\\Sigma - 1I)\\mathbf{v}_2 = \\begin{pmatrix} 3 & 3 \\\\ 3 & 3 \\end{pmatrix} \\begin{pmatrix} v_{21} \\\\ v_{22} \\end{pmatrix} = \\begin{pmatrix} 0 \\\\ 0 \\end{pmatrix} \\implies v_{21} = -v_{22} \\implies \\boldsymbol{\\phi}_2 = <span class=\"ans\">\\frac{1}{\\sqrt{2}}\\begin{pmatrix} 1 \\\\ -1 \\end{pmatrix}</span>$$</p>

<p><span class="part">Part (b): KLT Matrix & Coefficient Transformation</span><br>
The KLT matrix aligns rows with the orthonormal eigenvectors:
$$A = \\begin{pmatrix} \\boldsymbol{\\phi}_1^\\top \\\\ \\boldsymbol{\\phi}_2^\\top \\end{pmatrix} = \\frac{1}{\\sqrt{2}} \\begin{pmatrix} 1 & 1 \\\\ 1 & -1 \\end{pmatrix}$$
Transforming $\\mathbf{x}_0 = (2, -1)^\\top$:
<span class="ans">$$\\mathbf{y}_0 = A \\mathbf{x}_0 = \\frac{1}{\\sqrt{2}} \\begin{pmatrix} 1 & 1 \\\\ 1 & -1 \\end{pmatrix} \\begin{pmatrix} 2 \\\\ -1 \\end{pmatrix} = \\frac{1}{\\sqrt{2}} \\begin{pmatrix} 1 \\\\ 3 \\end{pmatrix} = \\begin{pmatrix} 1/\\sqrt{2} \\\\ 3/\\sqrt{2} \\end{pmatrix}$$</span>
Verifying complete decorrelation of transform coefficients:
$$\\Sigma_{\\mathbf{y}} = A \\Sigma_{\\mathbf{x}} A^\\top = \\frac{1}{2} \\begin{pmatrix} 1 & 1 \\\\ 1 & -1 \\end{pmatrix} \\begin{pmatrix} 4 & 3 \\\\ 3 & 4 \\end{pmatrix} \\begin{pmatrix} 1 & 1 \\\\ 1 & -1 \\end{pmatrix} = \\begin{pmatrix} 7 & 0 \\\\ 0 & 1 \\end{pmatrix} = \\text{diag}(\\lambda_1, \\lambda_2)$$
The cross-covariance between $y_1$ and $y_2$ is strictly 0.</p>

<p><span class="part">Part (c): Reconstruction & MSE with $m = 1$ Component</span><br>
Truncating to $m = 1$ retains only $y_{0, 1} = \\frac{1}{\\sqrt{2}}$ along principal axis $\\boldsymbol{\\phi}_1$:
<span class="ans">$$\\hat{\\mathbf{x}}_0 = y_{0, 1} \\boldsymbol{\\phi}_1 = \\left( \\frac{1}{\\sqrt{2}} \\right) \\frac{1}{\\sqrt{2}} \\begin{pmatrix} 1 \\\\ 1 \\end{pmatrix} = \\frac{1}{2} \\begin{pmatrix} 1 \\\\ 1 \\end{pmatrix} = \\begin{pmatrix} 0.5 \\\\ 0.5 \\end{pmatrix}$$</span>
<strong>Theoretical Reconstruction Error:</strong>
In KLT/PCA truncation, the expected MSE equals the sum of discarded eigenvalues:
<span class="ans">$$\\text{MSE} = \\sum_{j=m+1}^2 \\lambda_j = \\lambda_2 = 1.0$$</span>
Retaining just 1 component preserves $\\frac{\\lambda_1}{\\lambda_1 + \\lambda_2} = \\frac{7}{8} = <span class=\"ans\">87.5\\%</span>$ of total signal energy.</p>""",
        "takeaway": "The Karhunen-Loève Transform (KLT/PCA) diagonalizes the covariance matrix $\\Sigma_{\\mathbf{y}} = \\Phi \\Sigma_{\\mathbf{x}} \\Phi^\\top = \\Lambda$, achieving optimal decorrelation and maximum energy compaction. Discarded eigenvalue sum $\\sum_{j>m} \\lambda_j$ yields exact reconstruction MSE."
    },
    {
        "id": 40992,
        "subject": "DIP",
        "topicId": "09_Discrete_Cosine_Transform_DCT_and_KLT",
        "topicTitle": "09 · DCT & KLT",
        "title": "DFT Boundary Discontinuity vs DCT Even Mirroring (IISc Midterm / Jain)",
        "kind2": "university",
        "source": "IISc Midterm / Jain Fundamentals of Digital Image Processing",
        "marks": "[8 Marks]",
        "question": """<p>Consider a 1D discrete signal of length $N = 4$ with linear ramp profile:
$$\\mathbf{x} = [10, \\, 20, \\, 30, \\, 40]$$</p>
<p><span class="part">(a)</span> Sketch the periodic extension of $\\mathbf{x}$ assumed by the <strong>Discrete Fourier Transform (DFT)</strong>. Identify the boundary jump discontinuity magnitude $\\Delta x_{\\text{boundary}}$ between period repetitions.</p>
<p><span class="part">(b)</span> Sketch the even-symmetric periodic extension of length $2N = 8$ assumed by the <strong>Type-II Discrete Cosine Transform (DCT-II)</strong>. Does it contain any boundary jumps?</p>
<p><span class="part">(c)</span> In terms of Fourier decay rates ($\mathcal{O}(1/\\omega)$ vs $\mathcal{O}(1/\\omega^2)$), explain why DCT achieves vastly superior energy compaction for image compression (e.g. JPEG) compared to DFT.</p>""",
        "solution": """<p><span class="part">Part (a): DFT Periodic Extension & Jump Discontinuity</span><br>
The DFT implicitly treats a finite signal as periodically repeating with period $N = 4$:
$$\\tilde{x}_{\\text{DFT}} = [\\dots, \\; 10, 20, 30, \\mathbf{40} \\mid \\mathbf{10}, 20, 30, 40 \\mid 10, 20, 30, 40, \\; \\dots]$$
At the boundary between $x(N-1) = 40$ and $x(0) = 10$:
<span class="ans">$$\\Delta x_{\\text{boundary}} = x(0) - x(N-1) = 10 - 40 = -30$$</span>
Even though the original signal is a smooth linear ramp inside $[0, 3]$, the DFT forces an artificial, razor-sharp step cliff of height $30$ at every period boundary. In the frequency domain, this creates massive high-frequency spectral leakage and the Gibbs phenomenon.</p>

<p><span class="part">Part (b): DCT-II Even-Symmetric Mirror Extension</span><br>
The DCT-II performs symmetric boundary reflection around half-sample boundaries, creating an even-symmetric periodic signal of length $2N = 8$:
$$\\tilde{x}_{\\text{DCT}} = [\\dots, \\; \\mathbf{10}, 20, 30, \\mathbf{40}, \\; \\mathbf{40}, 30, 20, \\mathbf{10} \\mid \\mathbf{10}, 20, 30, \\mathbf{40}, \\; \\mathbf{40}, 30, 20, \\mathbf{10}, \\; \\dots]$$
Boundary transitions:
- Right boundary: $x(3) = 40$ meets reflection $x(4) = 40 \\implies \\Delta x = 40 - 40 = <span class=\"ans\">0</span>$
- Left boundary: $x(0) = 10$ meets reflection $x(7) = 10 \\implies \\Delta x = 10 - 10 = <span class=\"ans\">0</span>$<br>
<span class=\"ans\">There are zero jump discontinuities! The extended waveform is continuous everywhere ($C^0$ continuity).</span></p>

<p><span class="part">Part (c): Spectral Decay Rates & Energy Compaction</span><br>
By standard Fourier transform theory of piecewise smooth functions:
1. <strong>DFT Extension (Jump Discontinuities):</strong> A function with step discontinuities has Fourier coefficients that decay slowly as:
<span class="ans">$$|F_{\\text{DFT}}(k)| = \\mathcal{O}\\left(\\frac{1}{k}\\right)$$</span>
High-frequency coefficients remain large solely to synthesize the artificial boundary steps.
2. <strong>DCT-II Extension (Continuous Waveform):</strong> Because even mirroring eliminates jump discontinuities, the function is continuous ($C^0$). Integrating by parts twice proves that its Fourier coefficients decay at the much faster rate:
<span class="ans">$$|F_{\\text{DCT}}(k)| = \\mathcal{O}\\left(\\frac{1}{k^2}\\right)$$</span>
High-frequency DCT coefficients decay to near-zero rapidly, concentrating over $95\\%$ of signal energy into the lowest 2-3 DCT coefficients. This is why JPEG and video codecs use DCT instead of DFT.</p>""",
        "takeaway": "DFT assumes periodic extension with sharp boundary steps ($O(1/k)$ spectral leakage). DCT-II creates symmetric even mirroring without boundary jumps, achieving rapid $O(1/k^2)$ spectral decay and superior energy compaction."
    },
    {
        "id": 40993,
        "subject": "DIP",
        "topicId": "09_Discrete_Cosine_Transform_DCT_and_KLT",
        "topicTitle": "09 · DCT & KLT",
        "title": "JPEG DCT Quantization & Zigzag Run-Length Coding (IIT Delhi / Pennebaker & Mitchell)",
        "kind2": "generated",
        "source": "IIT Delhi / Pennebaker & Mitchell JPEG Still Image Compression",
        "marks": "[8 Marks]",
        "question": """<p>An $8 \\times 8$ block DCT produces the upper-left $3 \\times 3$ low-frequency transform coefficients:
$$C = \\begin{pmatrix}
-415 & -30 & -14 \\\\
44 & 18 & -8 \\\\
-12 & 6 & 0
\\end{pmatrix}$$
with all remaining coefficients in the $8 \\times 8$ block being zero. The corresponding JPEG standard luminance quantization matrix $Q$ entries are:
$$Q = \\begin{pmatrix}
16 & 11 & 10 \\\\
12 & 12 & 14 \\\\
14 & 13 & 16
\\end{pmatrix}$$</p>
<p><span class="part">(a)</span> Compute the quantized DCT matrix $C_q(u, v) = \\text{round}\\left( \\frac{C(u, v)}{Q(u, v)} \\right)$ for this $3 \\times 3$ sub-block.</p>
<p><span class="part">(b)</span> Perform <strong>zigzag scan ordering</strong> on the $3 \\times 3$ quantized matrix starting from the DC coefficient $(0, 0)$.</p>
<p><span class="part">(c)</span> Convert the zigzag sequence into Run-Length Encoded (RLE) intermediate pairs $(\\text{run}, \\text{level})$ and explain how the End-of-Block (EOB) marker achieves high compression.</p>""",
        "solution": """<p><span class="part">Part (a): Quantization Division & Rounding</span><br>
Evaluate $C_q(u, v) = \\text{round}\\left( \\frac{C(u, v)}{Q(u, v)} \\right)$ element-wise:
- $(0, 0)$: $-415 / 16 = -25.9375 \\to <span class=\"ans\">-26</span>$ (DC coefficient)
- $(0, 1)$: $-30 / 11 = -2.7273 \\to <span class=\"ans\">-3</span>$
- $(0, 2)$: $-14 / 10 = -1.4000 \\to <span class=\"ans\">-1</span>$
- $(1, 0)$: $44 / 12 = +3.6667 \\to <span class=\"ans\">+4</span>$
- $(1, 1)$: $18 / 12 = +1.5000 \\to <span class=\"ans\">+2</span>$
- $(1, 2)$: $-8 / 14 = -0.5714 \\to <span class=\"ans\">-1</span>$
- $(2, 0)$: $-12 / 14 = -0.8571 \\to <span class=\"ans\">-1</span>$
- $(2, 1)$: $6 / 13 = +0.4615 \\to <span class=\"ans\">0</span>$
- $(2, 2)$: $0 / 16 = 0 \\to <span class=\"ans\">0</span>$<br>
<span class="ans">$$C_q = \\begin{pmatrix}
-26 & -3 & -1 \\\\
4 & 2 & -1 \\\\
-1 & 0 & 0
\\end{pmatrix}$$</span></p>

<p><span class="part">Part (b): Zigzag Scanning Order</span><br>
Zigzag traverses diagonally across antidiagonals $u + v = d$:
1. $d = 0$: $(0, 0) = -26$
2. $d = 1$: $(0, 1) = -3 \\to (1, 0) = 4$
3. $d = 2$: $(2, 0) = -1 \\to (1, 1) = 2 \\to (0, 2) = -1$
4. $d = 3$: $(1, 2) = -1 \\to (2, 1) = 0$
5. $d = 4$: $(2, 2) = 0$<br>
Resulting 1D scanned sequence of 9 coefficients:
<span class="ans">$$[-26, \\quad -3, \\quad 4, \\quad -1, \\quad 2, \\quad -1, \\quad -1, \\quad 0, \\quad 0]$$</span>
Since all remaining coefficients in the $8 \\times 8$ block are zero, they append 55 additional trailing zeros.</p>

<p><span class="part">Part (c): Run-Length Encoding & EOB Token</span><br>
In JPEG:
- The DC coefficient $-26$ is encoded separately via Differential Pulse Code Modulation (DPCM) relative to the prior block's DC.
- The AC coefficients are encoded as $(\\text{run of zeros}, \\text{non-zero amplitude})$:
  1. Value $-3$: $(0, -3)$ (zero preceding zeros)
  2. Value $4$: $(0, 4)$
  3. Value $-1$: $(0, -1)$
  4. Value $2$: $(0, 2)$
  5. Value $-1$: $(0, -1)$
  6. Value $-1$: $(0, -1)$
  7. Trailing zeros: all remaining entries in the $8 \\times 8$ block are zero $\\implies$ replaced by a single <span class=\"ans\">\\text{EOB (End-of-Block)}</span> token.<br>
<span class=\"ans\">RLE Stream: $[\\text{DC: } -26], \\; (0, -3), \\; (0, 4), \\; (0, -1), \\; (0, 2), \\; (0, -1), \\; (0, -1), \\; \\text{EOB}$.</span><br>
The zigzag scan groups high-frequency zeros into a contiguous run at the tail, allowing an entire $8 \\times 8$ block of 64 coefficients to be encoded in just 7 tokens plus EOB.</p>""",
        "takeaway": "JPEG quantization divides DCT coefficients by $Q(u, v)$ to induce high-frequency sparsity. Zigzag scan reorders 2D coefficients along increasing spatial frequency, clustering zeros at the tail where a single EOB token terminates the block."
    },

    # =========================================================================
    # TOPIC 10: Wavelets and Multiresolution Analysis
    # =========================================================================
    {
        "id": 41091,
        "subject": "DIP",
        "topicId": "10_Wavelets_and_Multiresolution_Analysis",
        "topicTitle": "10 · Wavelets & Multiresolution",
        "title": "2D Discrete Haar Wavelet Transform (IISc Midterm / Gonzalez & Woods)",
        "kind2": "pyq",
        "source": "IISc Midterm / Gonzalez & Woods Digital Image Processing",
        "marks": "[8 Marks]",
        "question": """<p>The orthonormal 1D Haar analysis filters are given by low-pass scaling filter $\\mathbf{h}_0 = \\frac{1}{\\sqrt{2}}[1, 1]$ and high-pass wavelet filter $\\mathbf{h}_1 = \\frac{1}{\\sqrt{2}}[1, -1]$. Consider the $2 \\times 2$ image patch:
$$f = \\begin{pmatrix} 6 & 8 \\\\ 2 & 4 \\end{pmatrix}$$</p>
<p><span class="part">(a)</span> Apply 1D Haar filtering and decimation along rows to obtain intermediate row low-pass and high-pass coefficients.</p>
<p><span class="part">(b)</span> Filter the columns of the row-transformed result to compute the four subbands: $LL$ (Approximation), $LH$ (Horizontal detail), $HL$ (Vertical detail), and $HH$ (Diagonal detail).</p>
<p><span class="part">(c)</span> Reconstruct the original $2 \\times 2$ block from the subband coefficients using the synthesis filters $\\mathbf{g}_0 = \\mathbf{h}_0^\\top$ and $\\mathbf{g}_1 = \\mathbf{h}_1^\\top$, verifying perfect reconstruction.</p>""",
        "solution": """<p><span class="part">Part (a): Row Filtering & Decimation</span><br>
Convolve each row with $\\mathbf{h}_0$ and $\\mathbf{h}_1$, keeping downsampled output at step 2:
- <strong>Row 1 ($[6, 8]$):</strong>
  - Low-pass: $\\frac{6 + 8}{\\sqrt{2}} = \\frac{14}{\\sqrt{2}} = 7\\sqrt{2}$
  - High-pass: $\\frac{6 - 8}{\\sqrt{2}} = \\frac{-2}{\\sqrt{2}} = -\\sqrt{2}$
- <strong>Row 2 ($[2, 4]$):</strong>
  - Low-pass: $\\frac{2 + 4}{\\sqrt{2}} = \\frac{6}{\\sqrt{2}} = 3\\sqrt{2}$
  - High-pass: $\\frac{2 - 4}{\\sqrt{2}} = \\frac{-2}{\\sqrt{2}} = -\\sqrt{2}$<br>
Row-transformed intermediate matrix:
<span class="ans">$$f_{\\text{row}} = \\begin{pmatrix} 7\\sqrt{2} & -\\sqrt{2} \\\\ 3\\sqrt{2} & -\\sqrt{2} \\end{pmatrix}$$</span></p>

<p><span class="part">Part (b): Column Filtering to Obtain Subbands</span><br>
Filter each column of $f_{\\text{row}}$ with $\\mathbf{h}_0$ and $\\mathbf{h}_1$:
- <strong>Column 1 ($[7\\sqrt{2}, \\; 3\\sqrt{2}]^\\top$):</strong>
  - $LL$ (Approximation): $\\frac{7\\sqrt{2} + 3\\sqrt{2}}{\\sqrt{2}} = 7 + 3 = <span class=\"ans\">10</span>$
  - $LH$ (Horizontal edge): $\\frac{7\\sqrt{2} - 3\\sqrt{2}}{\\sqrt{2}} = 7 - 3 = <span class=\"ans\">4</span>$
- <strong>Column 2 ($[-\\sqrt{2}, \\; -\\sqrt{2}]^\\top$):</strong>
  - $HL$ (Vertical edge): $\\frac{-\\sqrt{2} + (-\\sqrt{2})}{\\sqrt{2}} = -1 - 1 = <span class=\"ans\">-2</span>$
  - $HH$ (Diagonal corner): $\\frac{-\\sqrt{2} - (-\\sqrt{2})}{\\sqrt{2}} = -1 - (-1) = <span class=\"ans\">0</span>$<br>
Assembled 1-level 2D DWT representation:
<span class="ans">$$\\begin{pmatrix} LL & HL \\\\ LH & HH \\end{pmatrix} = \\begin{pmatrix} 10 & -2 \\\\ 4 & 0 \\end{pmatrix}$$</span></p>

<p><span class="part">Part (c): Perfect Synthesis Reconstruction</span><br>
Orthonormal synthesis matrix is $W = \\frac{1}{\\sqrt{2}} \\begin{pmatrix} 1 & 1 \\\\ 1 & -1 \\end{pmatrix}$.
The forward 2D transform is $C = W f W^\\top$.
Because $W$ is orthonormal ($W W^\\top = I$), inverse transform is:
$$f = W^\\top C W = W C W$$
Evaluating:
$$W C = \\frac{1}{\\sqrt{2}} \\begin{pmatrix} 1 & 1 \\\\ 1 & -1 \\end{pmatrix} \\begin{pmatrix} 10 & -2 \\\\ 4 & 0 \\end{pmatrix} = \\frac{1}{\\sqrt{2}} \\begin{pmatrix} 14 & -2 \\\\ 6 & -2 \\end{pmatrix}$$
Multiplying by $W$:
$$f = \\frac{1}{\\sqrt{2}} \\begin{pmatrix} 14 & -2 \\\\ 6 & -2 \\end{pmatrix} \\frac{1}{\\sqrt{2}} \\begin{pmatrix} 1 & 1 \\\\ 1 & -1 \\end{pmatrix} = \\frac{1}{2} \\begin{pmatrix} 14 - 2 & 14 + 2 \\\\ 6 - 2 & 6 + 2 \\end{pmatrix} = \\frac{1}{2} \\begin{pmatrix} 12 & 16 \\\\ 4 & 8 \\end{pmatrix} = \\begin{pmatrix} 6 & 8 \\\\ 2 & 4 \\end{pmatrix}$$
<span class=\"ans\">Reconstructed image identically matches original $f = \\begin{pmatrix} 6 & 8 \\\\ 2 & 4 \\end{pmatrix}$ with zero error.</span></p>""",
        "takeaway": "Separable 2D DWT applies 1D analysis filters $h_0, h_1$ along rows then columns, decomposing the image into 4 subbands: $LL$ (smooth approximation), $LH$ (horizontal edges), $HL$ (vertical edges), and $HH$ (diagonal details)."
    },
    {
        "id": 41092,
        "subject": "DIP",
        "topicId": "10_Wavelets_and_Multiresolution_Analysis",
        "topicTitle": "10 · Wavelets & Multiresolution",
        "title": "Two-Channel Filter Bank & Perfect Reconstruction (MIT 6.341 / Strang & Nguyen)",
        "kind2": "university",
        "source": "MIT 6.341 / Strang & Nguyen Wavelets and Filter Banks",
        "marks": "[8 Marks]",
        "question": """<p>Consider a 2-channel multirate filter bank with analysis filters $H_0(z)$ (low-pass) and $H_1(z)$ (high-pass), factor-2 downsamplers ($\\\\downarrow 2$), factor-2 upsamplers ($\\\\uparrow 2$), and synthesis filters $G_0(z)$ and $G_1(z)$.</p>
<p><span class="part">(a)</span> Derive the $z$-transform expression for the reconstructed output $\\\\hat{X}(z)$ in terms of input $X(z)$ and aliased term $X(-z)$.</p>
<p><span class="part">(b)</span> Derive the <strong>Aliasing Cancellation Condition</strong> and show that setting $G_0(z) = H_1(-z)$ and $G_1(z) = -H_0(-z)$ completely eliminates aliasing.</p>
<p><span class="part">(c)</span> Under aliasing cancellation, state the <strong>No-Distortion (Perfect Reconstruction) Condition</strong> on the product filter $P_0(z) = H_0(z) G_0(z)$.</p>""",
        "solution": """<p><span class="part">Part (a): Signal Flow & Output $z$-Transform</span><br>
1. <strong>Analysis & Downsampling:</strong>
After downsampling by 2 ($\\\\downarrow 2$), the channel signals are:
$$V_0(z) = \\frac{1}{2}\\left[ H_0(z^{1/2}) X(z^{1/2}) + H_0(-z^{1/2}) X(-z^{1/2}) \\right]$$
$$V_1(z) = \\frac{1}{2}\\left[ H_1(z^{1/2}) X(z^{1/2}) + H_1(-z^{1/2}) X(-z^{1/2}) \\right]$$
2. <strong>Upsampling ($\\\\uparrow 2$):</strong>
Upsampling replaces $z \\to z^2$:
$$U_0(z) = V_0(z^2) = \\frac{1}{2}\\left[ H_0(z) X(z) + H_0(-z) X(-z) \\right]$$
$$U_1(z) = V_1(z^2) = \\frac{1}{2}\\left[ H_1(z) X(z) + H_1(-z) X(-z) \\right]$$
3. <strong>Synthesis & Summation:</strong>
Passing through synthesis filters $G_0(z)$ and $G_1(z)$:
$$\\hat{X}(z) = G_0(z) U_0(z) + G_1(z) U_1(z)$$
<span class="ans">$$\\hat{X}(z) = \\frac{1}{2}\\left[ H_0(z)G_0(z) + H_1(z)G_1(z) \\right] X(z) + \\frac{1}{2}\\left[ H_0(-z)G_0(z) + H_1(-z)G_1(z) \\right] X(-z)$$</span>
The second term represents downsampling aliasing.</p>

<p><span class="part">Part (b): Aliasing Cancellation Condition</span><br>
To completely cancel aliasing for all inputs $X(z)$, the coefficient of $X(-z)$ must vanish identically:
<span class="ans">$$H_0(-z) G_0(z) + H_1(-z) G_1(z) = 0$$</span>
A universal cross-multiplying solution is:
<span class="ans">$$G_0(z) = H_1(-z), \\qquad G_1(z) = -H_0(-z)$$</span>
Substituting this into the aliasing term:
$$H_0(-z) [H_1(-z)] + H_1(-z) [-H_0(-z)] = H_0(-z)H_1(-z) - H_1(-z)H_0(-z) = 0$$
Aliasing cancels out perfectly and unconditionally.</p>

<p><span class="part">Part (c): No-Distortion (Perfect Reconstruction)</span><br>
With aliasing eliminated, the transfer function becomes:
$$\\hat{X}(z) = \\frac{1}{2} T(z) X(z), \\quad \\text{where } T(z) = H_0(z)G_0(z) + H_1(z)G_1(z)$$
Substituting $G_1(z) = -H_0(-z)$ and $G_0(z) = H_1(-z) \\implies H_1(z) = G_0(-z)$:
$$T(z) = H_0(z)G_0(z) - H_0(-z)G_0(-z) = P_0(z) - P_0(-z)$$
where $P_0(z) = H_0(z)G_0(z)$ is the product filter.<br>
For <strong>Perfect Reconstruction (PR)</strong>, the output must be an undistorted, scaled delay: $\\hat{X}(z) = c z^{-l} X(z)$.
Thus $T(z) = 2 z^{-l}$ (with $l$ odd):
<span class="ans">$$P_0(z) - P_0(-z) = 2 z^{-l} \\iff P_0(z) \\text{ is a half-band filter}$$</span>
All even powers of $z$ in $P_0(z)$ vanish except the central tap $z^{-l} = 1$.</p>""",
        "takeaway": "Two-channel multirate filter banks achieve alias-free reconstruction when $G_0(z) = H_1(-z)$ and $G_1(z) = -H_0(-z)$. Perfect reconstruction requires product filter $P_0(z) = H_0(z)G_0(z)$ to be half-band: $P_0(z) - P_0(-z) = 2z^{-l}$."
    },
    {
        "id": 41093,
        "subject": "DIP",
        "topicId": "10_Wavelets_and_Multiresolution_Analysis",
        "topicTitle": "10 · Wavelets & Multiresolution",
        "title": "VisuShrink Wavelet Denoising & MAD Noise Estimation (IISc Endsem / Donoho & Johnstone)",
        "kind2": "generated",
        "source": "IISc Endsem / Donoho & Johnstone Biometrika (1994)",
        "marks": "[8 Marks]",
        "question": """<p>A $512 \\times 512$ image ($N = 262{,}144$ pixels) corrupted by additive zero-mean white Gaussian noise $n \\sim \\mathcal{N}(0, \\sigma^2)$ is decomposed using an orthonormal 2D DWT. The sample median of absolute wavelet coefficients in the finest diagonal subband is measured to be:
$$\\text{median}(|HH_1|) = 6.745$$</p>
<p><span class="part">(a)</span> Using the robust <strong>Median Absolute Deviation (MAD)</strong> estimator, compute the estimated noise standard deviation $\\hat{\\sigma}$.</p>
<p><span class="part">(b)</span> Compute the Donoho-Johnstone <strong>Universal Threshold</strong> $\\lambda = \\hat{\\sigma} \\sqrt{2 \\ln N}$.</p>
<p><span class="part">(c)</span> Given three test wavelet coefficients $w_1 = 65.0, w_2 = -32.5, w_3 = 18.0$, compute their denoised values $\\hat{w}$ under <strong>Soft Thresholding</strong> $\\eta_{\\text{soft}}(w, \\lambda) = \\text{sgn}(w)\\max(0, |w| - \\lambda)$.</p>""",
        "solution": """<p><span class="part">Part (a): Robust MAD Noise Estimation</span><br>
Because the finest diagonal subband $HH_1$ consists almost entirely of high-frequency noise with very few true signal edges, it serves as an ideal noise estimator.<br>
For zero-mean Gaussian variable $Z \\sim \\mathcal{N}(0, \\sigma^2)$, the median of its absolute value $|Z|$ satisfies:
$$\\mathbb{P}(|Z| \\le M) = 2\\Phi(M/\\sigma) - 1 = 0.50 \\implies \\Phi(M/\\sigma) = 0.75$$
From standard normal quantiles: $\\Phi^{-1}(0.75) \\approx 0.67449$.
Thus $M = 0.6745 \\sigma \\implies \\sigma = \\frac{M}{0.6745}$.
Evaluating with $M = 6.745$:
<span class="ans">$$\\hat{\\sigma} = \\frac{\\text{median}(|HH_1|)}{0.6745} = \\frac{6.745}{0.6745} = 10.0$$</span>
The estimated noise standard deviation is $\\hat{\\sigma} = 10.0$. The MAD estimator is robust against outliers because extreme true image edges do not shift the median.</p>

<p><span class="part">Part (b): Universal Threshold $\\lambda$</span><br>
The Donoho-Johnstone VisuShrink universal threshold guarantees that with probability approaching 1 as $N \\to \\infty$, all pure noise coefficients fall below $\\lambda$:
$$\\lambda = \\hat{\\sigma} \\sqrt{2 \\ln N}$$
With $N = 512 \\times 512 = 262{,}144$:
$$\\ln(262{,}144) \\approx 12.4766$$
$$\\sqrt{2 \\ln N} = \\sqrt{2 \\times 12.4766} = \\sqrt{24.9533} \\approx 4.9953$$
Multiplying by $\\hat{\\sigma} = 10.0$:
<span class="ans">$$\\lambda = 10.0 \\times 4.9953 = 49.953 \\approx 49.95$$</span></p>

<p><span class="part">Part (c): Soft Thresholding of Test Coefficients</span><br>
Soft thresholding rule: $\\eta_{\\text{soft}}(w, \\lambda) = \\begin{cases} w - \\lambda & \\text{if } w > \\lambda \\\\ w + \\lambda & \\text{if } w < -\\lambda \\\\ 0 & \\text{if } |w| \\le \\lambda \\end{cases}$<br>
With $\\lambda = 49.95$:
1. <strong>For $w_1 = +65.0$:</strong>
Since $65.0 > 49.95$:
$$\\hat{w}_1 = 65.0 - 49.95 = <span class=\"ans\">+15.05</span>$$
2. <strong>For $w_2 = -32.5$:</strong>
Since $|-32.5| = 32.5 \\le 49.95$:
$$\\hat{w}_2 = <span class=\"ans\">0.00</span>$$
(The noise-dominated coefficient is shrunk entirely to zero).
3. <strong>For $w_3 = +18.0$:</strong>
Since $|18.0| = 18.0 \\le 49.95$:
$$\\hat{w}_3 = <span class=\"ans\">0.00</span>$$
Soft thresholding ensures continuity at $\\pm \\lambda$, preventing artificial high-frequency edge ringing associated with hard thresholding.</p>""",
        "takeaway": "VisuShrink estimates noise robustly via MAD: $\\hat{\\sigma} = \\frac{\\text{median}(|HH_1|)}{0.6745}$. The universal threshold $\\lambda = \\hat{\\sigma}\\sqrt{2\\ln N}$ with soft thresholding $\\text{sgn}(w)(|w|-\\lambda)_+$ asymptotically suppresses all Gaussian noise spikes."
    }
]

def main():
    with open(PRACTICE_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    if "40991" in content:
        print("Batch 09-10 already present in practice_dip.js!")
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
    for card in PRACTICE_DIP_09_10:
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

    print("Successfully added DIP Batch 09-10 (6 cards). Total in file now updated.")

if __name__ == "__main__":
    main()
