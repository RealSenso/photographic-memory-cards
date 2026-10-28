#!/usr/bin/env python3
"""
Builder script for DIP Practice Cards: Batch 01 (Topics 01 & 02)
Topic 01: Image Formation, Camera Geometry and Transformations (Cards 40191, 40192, 40193)
Topic 02: Color Theory and Color Spaces (Cards 40291, 40292, 40293)
"""

import json
import os
import re

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRACTICE_FILE = os.path.join(REPO_DIR, "practice_dip.js")

PRACTICE_DIP_01_02 = [
    # =========================================================================
    # TOPIC 01: Image Formation, Camera Geometry & Geometric Transformations
    # =========================================================================
    {
        "id": 40191,
        "subject": "DIP",
        "topicId": "01_Image_Formation_Camera_Geometry_and_Transformations",
        "topicTitle": "01 · Image Formation & Transformations",
        "title": "Planar Homography Estimation via DLT & SVD (IISc Midterm / Stanford CS231A)",
        "kind2": "pyq",
        "source": "IISc Midterm / Stanford CS231A Computer Vision",
        "marks": "[8 Marks]",
        "question": """<p>Given four planar point correspondences $\\mathbf{x}_i = (x_i, y_i, 1)^\\top \\leftrightarrow \\mathbf{x}_i' = (x_i', y_i', 1)^\\top$ ($i = 1, \\dots, 4$) across two camera views related by an unknown $3 \\times 3$ homography matrix $H$ with $\\mathbf{x}_i' \\sim H \\mathbf{x}_i$.</p>
<p><span class="part">(a)</span> Using the collinearity cross product $\\mathbf{x}_i' \\times (H \\mathbf{x}_i) = \\mathbf{0}$, reformulate the projective relation into a linear system $A_i \\mathbf{h} = \\mathbf{0}$, where $\\mathbf{h} = \\text{vec}(H^\\top) \\in \\mathbb{R}^9$.</p>
<p><span class="part">(b)</span> Write the explicit $2 \\times 9$ coefficient matrix $A_i$ contributed by correspondence $i$. Explain why the third row is linearly dependent.</p>
<p><span class="part">(c)</span> How is the assembled $8 \\times 9$ system $A \\mathbf{h} = \\mathbf{0}$ solved using <strong>Singular Value Decomposition (SVD)</strong> to obtain a non-trivial solution?</p>""",
        "solution": """<p><span class="part">Part (a): Cross-Product Linearization (DLT)</span><br>
Because homogeneous vectors $\\mathbf{x}_i'$ and $H \\mathbf{x}_i$ represent the same projective point, they are collinear:
$$\\mathbf{x}_i' \\times (H \\mathbf{x}_i) = \\mathbf{0}$$
Let $H$ be written in terms of its row vectors:
$$H = \\begin{pmatrix} \\mathbf{h}_1^\\top \\\\ \\mathbf{h}_2^\\top \\\\ \\mathbf{h}_3^\\top \\end{pmatrix} \\implies H \\mathbf{x}_i = \\begin{pmatrix} \\mathbf{h}_1^\\top \\mathbf{x}_i \\\\ \\mathbf{h}_2^\\top \\mathbf{x}_i \\\\ \\mathbf{h}_3^\\top \\mathbf{x}_i \\end{pmatrix}$$
Expanding the 3D cross product $\\begin{pmatrix} x_i' \\\\ y_i' \\\\ w_i' \\end{pmatrix} \\times \\begin{pmatrix} \\mathbf{h}_1^\\top \\mathbf{x}_i \\\\ \\mathbf{h}_2^\\top \\mathbf{x}_i \\\\ \\mathbf{h}_3^\\top \\mathbf{x}_i \\end{pmatrix} = \\mathbf{0}$:
$$\\begin{pmatrix} y_i' (\\mathbf{h}_3^\\top \\mathbf{x}_i) - w_i' (\\mathbf{h}_2^\\top \\mathbf{x}_i) \\\\ w_i' (\\mathbf{h}_1^\\top \\mathbf{x}_i) - x_i' (\\mathbf{h}_3^\\top \\mathbf{x}_i) \\\\ x_i' (\\mathbf{h}_2^\\top \\mathbf{x}_i) - y_i' (\\mathbf{h}_1^\\top \\mathbf{x}_i) \\end{pmatrix} = \\begin{pmatrix} 0 \\\\ 0 \\\\ 0 \\end{pmatrix}$$
With normalized coordinates $w_i' = 1$, each point pair yields 3 linear equations in the entries of $\\mathbf{h}$.</p>

<p><span class="part">Part (b): Explicit $2 \\times 9$ Matrix $A_i$</span><br>
The third equation is a linear combination of the first two ($x_i' \\cdot \\text{eq}_1 + y_i' \\cdot \\text{eq}_2 = 0$). Thus only the first two equations are linearly independent. Arranging into matrix form $A_i \\mathbf{h} = \\mathbf{0}$ where $\\mathbf{h} = (h_{11}, h_{12}, h_{13}, h_{21}, h_{22}, h_{23}, h_{31}, h_{32}, h_{33})^\\top$:
<span class="ans">$$A_i = \\begin{pmatrix}
\\mathbf{0}^\\top & -w_i' \\mathbf{x}_i^\\top & y_i' \\mathbf{x}_i^\\top \\\\
w_i' \\mathbf{x}_i^\\top & \\mathbf{0}^\\top & -x_i' \\mathbf{x}_i^\\top
\\end{pmatrix} = \\begin{pmatrix}
0 & 0 & 0 & -x_i & -y_i & -1 & y_i' x_i & y_i' y_i & y_i' \\\\
x_i & y_i & 1 & 0 & 0 & 0 & -x_i' x_i & -x_i' y_i & -x_i'
\\end{pmatrix}$$</span>
Since each point correspondence provides 2 independent constraints and $H$ has 8 degrees of freedom (up to scale), exactly 4 point correspondences (in general position, no 3 collinear) uniquely determine $H$.</p>

<p><span class="part">Part (c): SVD Solution</span><br>
Stacking $A_i$ for $i = 1, \\dots, 4$ forms an $8 \\times 9$ matrix $A$. To avoid the trivial solution $\\mathbf{h} = \\mathbf{0}$, we solve the constrained optimization problem:
$$\\min_{\\|\\mathbf{h}\\| = 1} \\|A \\mathbf{h}\\|^2$$
Compute the SVD of $A$:
$$A = U \\Sigma V^\\top$$
where $\\Sigma = \\text{diag}(\\sigma_1, \\sigma_2, \\dots, \\sigma_8, \\sigma_9)$ with singular values in descending order.<br>
<span class=\"ans\">The optimal solution $\\mathbf{h}^*$ is the right singular vector $\\mathbf{v}_9$ (the 9th column of $V$) corresponding to the smallest singular value $\\sigma_9$.</span> Reshaping $\\mathbf{v}_9$ into a $3 \\times 3$ matrix and dividing by $h_{33}$ yields the estimated homography matrix $H$.</p>""",
        "takeaway": "Direct Linear Transformation (DLT) uses cross-product linearization $\\mathbf{x}' \\times H\\mathbf{x} = \\mathbf{0}$ to form $A\\mathbf{h} = \\mathbf{0}$. Each point match gives 2 independent constraints; 4 points yield 8 equations for 8 DOF, solved via SVD."
    },
    {
        "id": 40192,
        "subject": "DIP",
        "topicId": "01_Image_Formation_Camera_Geometry_and_Transformations",
        "topicTitle": "01 · Image Formation & Transformations",
        "title": "Vanishing Points & Camera Calibration via Absolute Conic (IISc Midterm / Oxford Vision)",
        "kind2": "university",
        "source": "IISc Midterm / Oxford Computer Vision",
        "marks": "[8 Marks]",
        "question": """<p>Consider a 3D line parameterized by $\\mathbf{X}(\\lambda) = \\mathbf{X}_0 + \\lambda \\mathbf{d}$, where $\\mathbf{d} = (d_X, d_Y, d_Z)^\\top$ is its direction vector and $\\mathbf{X}_0 \\in \\mathbb{R}^3$. Under perspective projection $P = K [R \\mid \\mathbf{t}]$, where $K$ is the internal calibration matrix and $(R, \\mathbf{t})$ is camera pose:</p>
<p><span class="part">(a)</span> Compute the vanishing point $\\mathbf{v}$ on the image plane as $\\lambda \\to \\infty$.</p>
<p><span class="part">(b)</span> Prove that the vanishing point depends only on camera rotation $R$ and line direction $\\mathbf{d}$, and is completely invariant to camera translation $\\mathbf{t}$ and line origin $\\mathbf{X}_0$.</p>
<p><span class="part">(c)</span> For two mutually orthogonal 3D directions $\\mathbf{d}_1 \\perp \\mathbf{d}_2$, derive the geometric constraint on their vanishing points $\\mathbf{v}_1, \\mathbf{v}_2$ and the Image of the Absolute Conic (IAC) $\\omega = (K K^\\top)^{-1}$.</p>""",
        "solution": """<p><span class="part">Part (a): Vanishing Point Derivation</span><br>
In homogeneous coordinates, the 3D line point is $\\tilde{\\mathbf{X}}(\\lambda) = \\begin{pmatrix} \\mathbf{X}_0 + \\lambda \\mathbf{d} \\\\ 1 \\end{pmatrix}$.
Projecting onto the image plane:
$$\\mathbf{x}(\\lambda) \\sim P \\tilde{\\mathbf{X}}(\\lambda) = K [R \\mid \\mathbf{t}] \\begin{pmatrix} \\mathbf{X}_0 + \\lambda \\mathbf{d} \\\\ 1 \\end{pmatrix} = K (R \\mathbf{X}_0 + \\mathbf{t} + \\lambda R \\mathbf{d})$$
Dividing by scalar $\\lambda$ and taking the limit as $\\lambda \\to \\infty$:
$$\\mathbf{v} = \\lim_{\\lambda \\to \\infty} \\frac{1}{\\lambda} \\mathbf{x}(\\lambda) = \\lim_{\\lambda \\to \\infty} K \\left( \\frac{R \\mathbf{X}_0 + \\mathbf{t}}{\\lambda} + R \\mathbf{d} \\right) = K R \\mathbf{d}$$
<span class="ans">$$\\mathbf{v} \\sim K R \\mathbf{d}$$</span></p>

<p><span class="part">Part (b): Invariance to Translation & Position</span><br>
Notice that $\\mathbf{X}_0$ and $\\mathbf{t}$ completely vanish in the limit $\\lambda \\to \\infty$.<br>
- Since $\\mathbf{v}$ depends only on $\\mathbf{d}$ and $R$, <strong>any family of parallel lines</strong> sharing direction $\\mathbf{d}$ projects to the exact same vanishing point $\\mathbf{v}$, regardless of where they are positioned in 3D space.<br>
- Furthermore, camera translation $\\mathbf{t}$ has zero effect on vanishing points; only camera orientation (rotation $R$) changes $\\mathbf{v}$.</p>

<p><span class="part">Part (c): Orthogonality & Image of the Absolute Conic (IAC)</span><br>
Invert the vanishing point relation: $\\mathbf{d} \\sim R^\\top K^{-1} \\mathbf{v}$.<br>
For two orthogonal directions, $\\mathbf{d}_1^\\top \\mathbf{d}_2 = 0$:
$$\\mathbf{d}_1^\\top \\mathbf{d}_2 = (R^\\top K^{-1} \\mathbf{v}_1)^\\top (R^\\top K^{-1} \\mathbf{v}_2) = \\mathbf{v}_1^\\top (K^{-1})^\\top R R^\\top K^{-1} \\mathbf{v}_2 = 0$$
Since $R$ is an orthonormal rotation matrix, $R R^\\top = I$:
$$\\mathbf{v}_1^\\top (K K^\\top)^{-1} \\mathbf{v}_2 = 0$$
Defining the <strong>Image of the Absolute Conic (IAC)</strong> $\\omega = (K K^\\top)^{-1}$:
<span class="ans">$$\\mathbf{v}_1^\\top \\omega \\mathbf{v}_2 = 0$$</span>
Each pair of orthogonal vanishing points provides one linear constraint on $\\omega$. With three orthogonal vanishing points (e.g. from the corner of a building or room), one obtains three constraints, enabling full internal calibration of $K$ without any calibration grid!</p>""",
        "takeaway": "Vanishing points represent intersections at infinity $\\mathbf{v} \\sim KR\\mathbf{d}$, invariant to camera translation and line positions. Orthogonal 3D directions satisfy $\\mathbf{v}_1^\\top \\omega \\mathbf{v}_2 = 0$, where $\\omega = (KK^\\top)^{-1}$ enables self-calibration."
    },
    {
        "id": 40193,
        "subject": "DIP",
        "topicId": "01_Image_Formation_Camera_Geometry_and_Transformations",
        "topicTitle": "01 · Image Formation & Transformations",
        "title": "Backward Mapping & Bilinear Interpolation (IIT Madras / Berkeley EECS)",
        "kind2": "generated",
        "source": "IIT Madras / Berkeley EECS Image Processing",
        "marks": "[8 Marks]",
        "question": """<p>An image is rotated counter-clockwise by $\\theta = 45^\\circ$ around the origin $(0, 0)$ using backward (inverse) mapping:
$$\\begin{pmatrix} x \\\\ y \\end{pmatrix} = \\begin{pmatrix} \\cos\\theta & \\sin\\theta \\\\ -\\sin\\theta & \\cos\\theta \\end{pmatrix} \\begin{pmatrix} x' \\\\ y' \\end{pmatrix}$$</p>
<p><span class="part">(a)</span> For target output pixel $(x', y') = (2, 1)$, compute the exact subpixel coordinates $(x, y)$ in the source image.</p>
<p><span class="part">(b)</span> Given the four surrounding integer pixel intensities:
$$I(2, -1) = 20, \\quad I(3, -1) = 60, \\quad I(2, 0) = 40, \\quad I(3, 0) = 80$$
Find the output intensity $I'(2, 1)$ using <strong>nearest-neighbor interpolation</strong>.</p>
<p><span class="part">(c)</span> Compute the output intensity $I'(2, 1)$ using <strong>bilinear interpolation</strong> and compare the visual artifacts produced by both methods.</p>""",
        "solution": """<p><span class="part">Part (a): Inverse Coordinate Mapping</span><br>
For $\\theta = 45^\\circ$, $\\cos 45^\\circ = \\sin 45^\\circ = \\frac{\\sqrt{2}}{2} \\approx 0.7071$:
$$x = x' \\cos 45^\\circ + y' \\sin 45^\\circ = 2(0.7071) + 1(0.7071) = 3(0.7071) = <span class=\"ans\">2.1213</span>$$
$$y = -x' \\sin 45^\\circ + y' \\cos 45^\\circ = -2(0.7071) + 1(0.7071) = -1(0.7071) = <span class=\"ans\">-0.7071</span>$$
The target pixel maps to continuous source coordinates $(x, y) = (2.1213, -0.7071)$.</p>

<p><span class="part">Part (b): Nearest-Neighbor Interpolation</span><br>
Rounding $(x, y)$ to the nearest integer grid point:
- $\\text{round}(2.1213) = 2$
- $\\text{round}(-0.7071) = -1$<br>
The nearest integer pixel is $(2, -1)$.
<span class="ans">$$I'_{\\text{NN}}(2, 1) = I(2, -1) = 20$$</span></p>

<p><span class="part">Part (c): Bilinear Interpolation</span><br>
The four surrounding integer grid neighbors bounding $(x, y)$ are:
- $(x_0, y_0) = (2, -1)$ with $I_{00} = 20$
- $(x_1, y_0) = (3, -1)$ with $I_{10} = 60$
- $(x_0, y_1) = (2, 0)$ with $I_{01} = 40$
- $(x_1, y_1) = (3, 0)$ with $I_{11} = 80$

Fractional distances from $(x_0, y_0)$:
$$\\Delta x = x - x_0 = 2.1213 - 2 = 0.1213$$
$$\\Delta y = y - y_0 = -0.7071 - (-1) = 0.2929$$
The bilinear interpolation formula is:
$$I_{\\text{bilinear}} = (1 - \\Delta x)(1 - \\Delta y) I_{00} + \\Delta x (1 - \\Delta y) I_{10} + (1 - \\Delta x) \\Delta y I_{01} + \\Delta x \\Delta y I_{11}$$
Evaluating weights:
- $(1 - \\Delta x)(1 - \\Delta y) = (0.8787)(0.7071) = 0.6213$
- $\\Delta x (1 - \\Delta y) = (0.1213)(0.7071) = 0.0858$
- $(1 - \\Delta x) \\Delta y = (0.8787)(0.2929) = 0.2574$
- $\\Delta x \\Delta y = (0.1213)(0.2929) = 0.0355$

Multiplying by intensities:
$$I_{\\text{bilinear}} = 0.6213(20) + 0.0858(60) + 0.2574(40) + 0.0355(80)$$
$$= 12.426 + 5.148 + 10.296 + 2.840 = <span class=\"ans\">30.71</span>$$
<strong>Visual comparison:</strong> Nearest-neighbor produces prominent blocky/staircasing artifacts along edges, whereas bilinear interpolation performs separable linear blending, producing smooth grayscale transitions without aliasing.</p>""",
        "takeaway": "Geometric image transformations require backward mapping $(x, y) = T^{-1}(x', y')$ to prevent holes. Bilinear interpolation computes a weighted average of the 4 bounding neighbors using separable linear weights $(1-\\Delta x)(1-\\Delta y)$."
    },

    # =========================================================================
    # TOPIC 02: Color Theory and Color Spaces
    # =========================================================================
    {
        "id": 40291,
        "subject": "DIP",
        "topicId": "02_Color_Theory_and_Color_Spaces",
        "topicTitle": "02 · Color Theory & Color Spaces",
        "title": "CIE XYZ Tristimulus & Chromaticity Mixing (IISc Midterm / Stanford CS178)",
        "kind2": "pyq",
        "source": "IISc Midterm / Stanford CS178 Digital Photography",
        "marks": "[8 Marks]",
        "question": """<p>A light source has spectral power distribution $P_1(\\lambda)$ and measured CIE XYZ tristimulus values:
$$X_1 = 80, \\quad Y_1 = 100, \\quad Z_1 = 20$$</p>
<p><span class="part">(a)</span> Compute the CIE $(x, y, z)$ chromaticity coordinates of this source.</p>
<p><span class="part">(b)</span> A second light source has tristimulus values $(X_2, Y_2, Z_2) = (40, 20, 60)$. When mixed in equal power ($1:1$), compute the tristimulus values and chromaticity coordinates of the mixture.</p>
<p><span class="part">(c)</span> Prove that on the $(x, y)$ chromaticity diagram, the mixture chromaticity $\\mathbf{c}_m = (x_m, y_m)$ lies strictly on the straight line segment joining $\\mathbf{c}_1 = (x_1, y_1)$ and $\\mathbf{c}_2 = (x_2, y_2)$ (Grassmann's Additivity Law).</p>""",
        "solution": """<p><span class="part">Part (a): Chromaticity Coordinates of Source 1</span><br>
The sum of tristimulus values is $S_1 = X_1 + Y_1 + Z_1 = 80 + 100 + 20 = 200$.
The normalized chromaticity coordinates are:
$$x_1 = \\frac{X_1}{S_1} = \\frac{80}{200} = <span class=\"ans\">0.40</span>$$
$$y_1 = \\frac{Y_1}{S_1} = \\frac{100}{200} = <span class=\"ans\">0.50</span>$$
$$z_1 = \\frac{Z_1}{S_1} = \\frac{20}{200} = <span class=\"ans\">0.10</span>$$
Check: $x_1 + y_1 + z_1 = 0.40 + 0.50 + 0.10 = 1.00$.</p>

<p><span class="part">Part (b): Equal Mixture Chromaticity</span><br>
By Grassmann's Additivity Law, tristimulus values add linearly:
$$X_m = X_1 + X_2 = 80 + 40 = 120$$
$$Y_m = Y_1 + Y_2 = 100 + 20 = 120$$
$$Z_m = Z_1 + Z_2 = 20 + 60 = 80$$
Sum of mixture tristimulus values: $S_m = 120 + 120 + 80 = 320$.
Mixture chromaticity coordinates:
$$x_m = \\frac{X_m}{S_m} = \\frac{120}{320} = <span class=\"ans\">0.375</span>$$
$$y_m = \\frac{Y_m}{S_m} = \\frac{120}{320} = <span class=\"ans\">0.375</span>$$
$$z_m = \\frac{Z_m}{S_m} = \\frac{80}{320} = <span class=\"ans\">0.250</span>$$</p>

<p><span class="part">Part (c): Proof of Collinearity</span><br>
Let $S_1 = X_1 + Y_1 + Z_1$ and $S_2 = X_2 + Y_2 + Z_2 = 40 + 20 + 60 = 120$.
The total mixture sum is $S_m = S_1 + S_2$.
Now express mixture chromaticity $x_m$:
$$x_m = \\frac{X_1 + X_2}{S_1 + S_2} = \\frac{S_1 \\left(\\frac{X_1}{S_1}\\right) + S_2 \\left(\\frac{X_2}{S_2}\\right)}{S_1 + S_2} = \\left(\\frac{S_1}{S_1 + S_2}\\right) x_1 + \\left(\\frac{S_2}{S_1 + S_2}\\right) x_2$$
Defining the barycentric mixing weight $w = \\frac{S_1}{S_1 + S_2} = \\frac{200}{320} = \\frac{5}{8} = 0.625$:
$$x_m = w x_1 + (1 - w) x_2, \\quad y_m = w y_1 + (1 - w) y_2$$
<span class=\"ans\">Since $0 < w < 1$, $\\mathbf{c}_m$ is a convex combination of $\\mathbf{c}_1$ and $\\mathbf{c}_2$. Hence, the mixture point lies strictly on the line segment connecting the two sources on the $(x, y)$ chromaticity chart.</span></p>""",
        "takeaway": "Grassmann's Laws ensure that tristimulus values add linearly ($X_m = X_1 + X_2$). On the chromaticity diagram, additive mixtures lie along the straight line connecting the primaries, weighted by their total tristimulus sums."
    },
    {
        "id": 40292,
        "subject": "DIP",
        "topicId": "02_Color_Theory_and_Color_Spaces",
        "topicTitle": "02 · Color Theory & Color Spaces",
        "title": "RGB to YCbCr Conversion & 4:2:0 Chroma Subsampling (IIT Delhi / Berkeley EECS 126)",
        "kind2": "university",
        "source": "IIT Delhi / Berkeley EECS 126 Video Systems",
        "marks": "[8 Marks]",
        "question": """<p>A pixel has 8-bit RGB color coordinates $(R, G, B) = (200, 100, 50)$ on $[0, 255]$.</p>
<p><span class="part">(a)</span> Compute its luminance and chrominance coordinates $(Y, C_b, C_r)$ using the standard ITU-R BT.601 transformation matrix.</p>
<p><span class="part">(b)</span> Explain the physiological basis of the <strong>Human Visual System (HVS)</strong> that permits $4:2:0$ chroma subsampling in JPEG and H.264/H.265 compression without visible loss.</p>
<p><span class="part">(c)</span> For an uncompressed $1920 \\times 1080$ frame at 24 bits/pixel, calculate the exact bandwidth/storage reduction percentage achieved by converting to $4:2:0$ format.</p>""",
        "solution": """<p><span class="part">Part (a): ITU-R BT.601 YCbCr Conversion</span><br>
The standard BT.601 transformation equations are:
$$Y = 0.299 R + 0.587 G + 0.114 B$$
$$C_b = -0.1687 R - 0.3313 G + 0.5000 B + 128$$
$$C_r = 0.5000 R - 0.4187 G - 0.0813 B + 128$$
Substituting $(R, G, B) = (200, 100, 50)$:
1. <strong>Luminance $Y$:</strong>
$$Y = 0.299(200) + 0.587(100) + 0.114(50) = 59.80 + 58.70 + 5.70 = <span class=\"ans\">124.2 \\approx 124</span>$$
2. <strong>Blue difference $C_b$:</strong>
$$C_b = -0.1687(200) - 0.3313(100) + 0.5000(50) + 128 = -33.74 - 33.13 + 25.00 + 128 = <span class=\"ans\">86.13 \\approx 86</span>$$
3. <strong>Red difference $C_r$:</strong>
$$C_r = 0.5000(200) - 0.4187(100) - 0.0813(50) + 128 = 100.00 - 41.87 - 4.065 + 128 = <span class=\"ans\">182.07 \\approx 182</span>$$
<span class=\"ans\">$(Y, C_b, C_r) = (124, 86, 182)$</span></p>

<p><span class="part">Part (b): HVS Contrast Sensitivity & Rod/Cone Distribution</span><br>
1. <strong>Spatial acuity difference:</strong> The human retina contains $\\approx 120$ million rod cells (luminance sensitivity) but only $\\approx 6$ million cone cells (color sensitivity).<br>
2. <strong>Contrast Sensitivity Function (CSF):</strong> Human visual psychophysics shows that spatial frequency cutoffs for chromatic channels ($C_b, C_r$) are approximately 4 times lower than that of luminance ($Y$). The eye cannot resolve fine color variations; blurring or downsampling chroma by $2\\times$ horizontally and $2\\times$ vertically is virtually imperceptible.</p>

<p><span class="part">Part (c): Bitrate & Bandwidth Reduction</span><br>
In a $2 \\times 2$ block of 4 pixels:
- <strong>RGB (4:4:4):</strong> 4 pixels $\\times 24$ bits = 96 bits ($24$ bits/pixel).
- <strong>YCbCr 4:2:0:</strong>
  - 4 luminance samples ($Y$): $4 \\times 8 = 32$ bits
  - 1 subsampled $C_b$: $1 \\times 8 = 8$ bits
  - 1 subsampled $C_r$: $1 \\times 8 = 8$ bits
  - Total for 4 pixels: $32 + 8 + 8 = 48$ bits ($12$ bits/pixel).<br>
Data size ratio:
$$\\text{Reduction} = 1 - \\frac{12}{24} = 1 - 0.50 = <span class=\"ans\">50\\% \\text{ reduction}</span>$$
For a $1920 \\times 1080$ frame, size drops from $6.22 \\text{ MB}$ to $3.11 \\text{ MB}$ per frame.</p>""",
        "takeaway": "ITU-R BT.601 decorrelates luminance $Y$ from chrominance $(C_b, C_r)$. Because human spatial acuity for chrominance is much lower than for luminance, 4:2:0 subsampling cuts raw data rate by 50% without perceived loss."
    },
    {
        "id": 40293,
        "subject": "DIP",
        "topicId": "02_Color_Theory_and_Color_Spaces",
        "topicTitle": "02 · Color Theory & Color Spaces",
        "title": "HSI Color Space Decomposition & Illumination Invariance (IISc Midterm / Gonzalez & Woods)",
        "kind2": "generated",
        "source": "IISc Midterm / Gonzalez & Woods Digital Image Processing",
        "marks": "[8 Marks]",
        "question": """<p>For normalized RGB coordinates on $[0, 1]$:</p>
<p><span class="part">(a)</span> State the mathematical formulations for Intensity ($I$), Saturation ($S$), and Hue ($H$) in the HSI color space.</p>
<p><span class="part">(b)</span> For an olive green pixel with $(R, G, B) = (0.5, 0.5, 0)$, calculate the exact $(H, S, I)$ values.</p>
<p><span class="part">(c)</span> Suppose scene lighting changes uniformly by scaling all channels by $\\alpha > 0$ such that $(R', G', B') = \\alpha (R, G, B)$. Prove that $H$ and $S$ remain strictly invariant to this illumination variation.</p>""",
        "solution": """<p><span class="part">Part (a): HSI Color Space Definitions</span><br>
- <strong>Intensity ($I$):</strong>
$$I = \\frac{R + G + B}{3}$$
- <strong>Saturation ($S$):</strong>
$$S = 1 - \\frac{3}{R + G + B} \\min(R, G, B)$$
- <strong>Hue ($H$):</strong>
$$\\theta = \\arccos\\left( \\frac{\\frac{1}{2}[(R - G) + (R - B)]}{\\sqrt{(R - G)^2 + (R - B)(G - B)}} \\right), \\quad H = \\begin{cases} \\theta & \\text{if } B \\le G \\\\ 360^\\circ - \\theta & \\text{if } B > G \\end{cases}$$</p>

<p><span class="part">Part (b): Calculation for Olive Green $(0.5, 0.5, 0)$</span><br>
1. <strong>Intensity $I$:</strong>
$$I = \\frac{0.5 + 0.5 + 0}{3} = \\frac{1.0}{3} \\approx <span class=\"ans\">0.3333</span>$$
2. <strong>Saturation $S$:</strong>
Since $\\min(0.5, 0.5, 0) = 0$:
$$S = 1 - \\frac{3}{1.0}(0) = <span class=\"ans\">1.000 \\text{ (purely saturated)}</span>$$
3. <strong>Hue $H$:</strong>
- Numerator: $\\frac{1}{2}[(0.5 - 0.5) + (0.5 - 0)] = \\frac{1}{2}(0.5) = 0.25$
- Denominator: $\\sqrt{(0.5 - 0.5)^2 + (0.5 - 0)(0.5 - 0)} = \\sqrt{0 + 0.25} = 0.50$
$$\\cos\\theta = \\frac{0.25}{0.50} = 0.5 \\implies \\theta = \\arccos(0.5) = 60^\\circ$$
Since $B = 0 \\le G = 0.5$, $H = \\theta = <span class=\"ans\">60^\\circ \\text{ (Yellow/Olive)}</span>$.<br>
<span class=\"ans\">$(H, S, I) = (60^\\circ, 1.0, 0.3333)$</span></p>

<p><span class="part">Part (c): Proof of Illumination Invariance</span><br>
Under uniform scaling $(R', G', B') = \\alpha (R, G, B)$ for $\\alpha > 0$:
1. <strong>Saturation:</strong>
$$S' = 1 - \\frac{3}{\\alpha R + \\alpha G + \\alpha B} \\min(\\alpha R, \\alpha G, \\alpha B) = 1 - \\frac{3 \\alpha}{\\alpha (R + G + B)} \\min(R, G, B) = S$$
2. <strong>Hue:</strong>
In both numerator and denominator, every term is homogeneous of degree 1:
$$\\text{Num}' = \\alpha \\cdot \\text{Num}, \\quad \\text{Den}' = \\sqrt{\\alpha^2 \\cdot \\text{Den}^2} = \\alpha \\cdot \\text{Den}$$
$$\\cos\\theta' = \\frac{\\alpha \\cdot \\text{Num}}{\\alpha \\cdot \\text{Den}} = \\frac{\\text{Num}}{\\text{Den}} = \\cos\\theta \\implies H' = H$$
<span class=\"ans\">Both $H$ and $S$ are perfectly scale-invariant. Only intensity $I' = \\alpha I$ scales. This decoupling makes HSI ideal for color segmentation and shadow-invariant object recognition.</span></p>""",
        "takeaway": "HSI separates chromaticity $(H, S)$ from luminance $I$. Under uniform lighting variations $(R', G', B') = \\alpha(R, G, B)$, hue $H$ and saturation $S$ are completely invariant, making HSI superior for color segmentation."
    }
]

def main():
    with open(PRACTICE_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    if "40191" in content:
        print("Batch 01-02 already present in practice_dip.js!")
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
    for card in PRACTICE_DIP_01_02:
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

    print("Successfully added DIP Batch 01-02 (6 cards). Total in file now updated.")

if __name__ == "__main__":
    main()
