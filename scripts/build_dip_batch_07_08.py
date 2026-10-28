#!/usr/bin/env python3
"""
Builder script for DIP Practice Cards: Batch 04 (Topics 07 & 08)
Topic 07: 2D Fourier Transforms (CSFT, DSFT, DFT) (Cards 40791, 40792, 40793)
Topic 08: Sampling Theorem, Aliasing, and Multi-Rate Conversion (Cards 40891, 40892, 40893)
"""

import json
import os
import re

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRACTICE_FILE = os.path.join(REPO_DIR, "practice_dip.js")

PRACTICE_DIP_07_08 = [
    # =========================================================================
    # TOPIC 07: 2D Fourier Transforms (CSFT, DSFT, DFT)
    # =========================================================================
    {
        "id": 40791,
        "subject": "DIP",
        "topicId": "07_2D_Fourier_Transforms_CSFT_DSFT_and_DFT",
        "topicTitle": "07 · 2D Fourier Transforms (CSFT, DSFT, DFT)",
        "title": "2D Fourier Transform of Rectangular Aperture & Scaling (IISc Midterm / MIT 6.011)",
        "kind2": "pyq",
        "source": "IISc Midterm / MIT 6.011 Signals and Systems",
        "marks": "[8 Marks]",
        "question": """<p>A continuous 2D rectangular aperture is defined on $\\mathbb{R}^2$ by:
$$f(x, y) = \\operatorname{rect}\\left(\\frac{x}{a}\\right) \\operatorname{rect}\\left(\\frac{y}{b}\\right) = \\begin{cases} 1 & \\text{if } |x| \\le a/2 \\text{ and } |y| \\le b/2 \\\\ 0 & \\text{otherwise} \\end{cases}$$</p>
<p><span class="part">(a)</span> Derive its 2D Continuous-Space Fourier Transform (CSFT) $F(u, v)$ in terms of the $\\operatorname{sinc}$ function, where $\\operatorname{sinc}(w) = \\frac{\\sin(\\pi w)}{\\pi w}$.</p>
<p><span class="part">(b)</span> Find the exact spatial frequency coordinates $(u, v)$ of the spectral nulls (zero-crossings) along the $u$ and $v$ axes.</p>
<p><span class="part">(c)</span> State the <strong>scaling property</strong> and <strong>rotation property</strong> of the 2D Fourier transform. If the slit width $a$ is halved, what happens to the spectral main-lobe width?</p>""",
        "solution": """<p><span class="part">Part (a): 2D CSFT Derivation</span><br>
Because $f(x, y)$ is separable ($f(x, y) = f_1(x) f_2(y)$), the 2D Fourier integral factors into two independent 1D transforms:
$$F(u, v) = \\int_{-\\infty}^\\infty \\int_{-\\infty}^\\infty f(x, y) e^{-j 2\\pi (ux + vy)} dx dy = \\left( \\int_{-a/2}^{a/2} e^{-j 2\\pi ux} dx \\right) \\left( \\int_{-b/2}^{b/2} e^{-j 2\\pi vy} dy \\right)$$
Evaluating the $x$-integral:
$$\\int_{-a/2}^{a/2} e^{-j 2\\pi ux} dx = \\left[ \\frac{e^{-j 2\\pi ux}}{-j 2\\pi u} \\right]_{-a/2}^{a/2} = \\frac{e^{j \\pi ua} - e^{-j \\pi ua}}{j 2\\pi u} = \\frac{\\sin(\\pi ua)}{\\pi u} = a \\operatorname{sinc}(ua)$$
By symmetry, the $y$-integral evaluates to $b \\operatorname{sinc}(vb)$.
Multiplying the two factors:
<span class="ans">$$F(u, v) = a b \\operatorname{sinc}(ua) \\operatorname{sinc}(vb) = a b \\left( \\frac{\\sin(\\pi ua)}{\\pi ua} \\right) \\left( \\frac{\\sin(\\pi vb)}{\\pi vb} \\right)$$</span></p>

<p><span class="part">Part (b): Spectral Nulls (Zero-Crossings)</span><br>
The function $\\operatorname{sinc}(w) = 0 \\iff w = \\pm 1, \\pm 2, \\pm 3, \\dots$ ($w \\in \\mathbb{Z} \\setminus \\{0\\}$).
- Along the $u$-axis ($v = 0$): nulls occur when $ua = m \\implies <span class=\"ans\">u = \\pm \\frac{m}{a}, \\; m \\in \\{1, 2, 3, \\dots\\}</span>$
- Along the $v$-axis ($u = 0$): nulls occur when $vb = n \\implies <span class=\"ans\">v = \\pm \\frac{n}{b}, \\; n \\in \\{1, 2, 3, \\dots\\}</span>$<br>
The central main-lobe has full width $\\Delta u = \\frac{2}{a}$ horizontally and $\\Delta v = \\frac{2}{b}$ vertically.</p>

<p><span class="part">Part (c): Scaling & Rotation Properties</span><br>
1. <strong>Scaling Property (Uncertainty Principle):</strong>
$$f\\left(\\frac{x}{a}, \\frac{y}{b}\\right) \\stackrel{\\mathcal{F}}{\\longleftrightarrow} |ab| F(au, bv)$$
Narrowing the aperture width by half ($a \\to a/2$) doubles the frequency main-lobe width: $\\Delta u = \\frac{2}{a/2} = \\frac{4}{a}$ (<span class=\"ans\">spectral main-lobe width doubles</span>). Spatial compression causes spectral dilation.<br>
2. <strong>Rotation Property:</strong>
Rotating the spatial domain image by angle $\\theta$ rotates its 2D Fourier transform by the <em>exact same angle</em> $\\theta$ in the frequency plane:
$$f(x\\cos\\theta - y\\sin\\theta, \\, x\\sin\\theta + y\\cos\\theta) \\stackrel{\\mathcal{F}}{\\longleftrightarrow} F(u\\cos\\theta - v\\sin\\theta, \\, u\\sin\\theta + v\\cos\\theta)$$</p>""",
        "takeaway": "The 2D Fourier transform of a rectangular aperture $\\text{rect}(x/a)\\text{rect}(y/b)$ is $ab\\operatorname{sinc}(ua)\\operatorname{sinc}(vb)$. Space-frequency scaling is reciprocal: narrowing an aperture in space spreads its diffraction spectrum in frequency."
    },
    {
        "id": 40792,
        "subject": "DIP",
        "topicId": "07_2D_Fourier_Transforms_CSFT_DSFT_and_DFT",
        "topicTitle": "07 · 2D Fourier Transforms (CSFT, DSFT, DFT)",
        "title": "Phase Dominance in 2D Images (MIT 6.341 / Stanford EE 261)",
        "kind2": "university",
        "source": "MIT 6.341 / Stanford EE 261 Fourier Analysis",
        "marks": "[8 Marks]",
        "question": """<p>Let $F_A(u, v) = M_A(u, v) e^{j \\phi_A(u, v)}$ and $F_B(u, v) = M_B(u, v) e^{j \\phi_B(u, v)}$ be the 2D Discrete Fourier Transforms of two distinct natural grayscale images $A$ (e.g., Einstein) and $B$ (e.g., Marilyn Monroe). A hybrid image is synthesized by combining the magnitude of $B$ with the phase of $A$:
$$F_{\\text{hybrid}}(u, v) = M_B(u, v) e^{j \\phi_A(u, v)}$$</p>
<p><span class="part">(a)</span> Which image's visual semantic features (edges, structural contours, facial identity) will be perceived in the inverse transform $g(x, y) = \\mathcal{F}^{-1}\\{F_{\\text{hybrid}}\\}$?</p>
<p><span class="part">(b)</span> Provide the rigorous mathematical explanation for why the Fourier <strong>phase spectrum</strong> $\\phi(u, v)$ dominates human visual perception over the magnitude spectrum $M(u, v)$.</p>
<p><span class="part">(c)</span> What is observed if an image is reconstructed from its phase alone: $F_{\\text{phase}}(u, v) = 1 \\cdot e^{j \\phi_A(u, v)}$?</p>""",
        "solution": """<p><span class="part">Part (a): Visual Perception of Hybrid Image</span><br>
The spatial reconstruction $g(x, y) = \\mathcal{F}^{-1}\\{F_{\\text{hybrid}}\\}$ will be unmistakably perceived as <span class=\"ans\">Image A (Einstein)</span>.<br>
Image B (Marilyn) contributes only subtle contrast variations and low-frequency shading, but all recognizable geometric features, boundaries, and facial identity belong entirely to Image A.</p>

<p><span class="part">Part (b): Mathematical Reason for Phase Dominance</span><br>
1. <strong>Phase Encodes Spatial Coherence:</strong>
By the Fourier shift theorem:
$$f(x - x_0, y - y_0) \\stackrel{\\mathcal{F}}{\\longleftrightarrow} F(u, v) e^{-j 2\\pi (ux_0 + vy_0)}$$
Translations and spatial positions do not alter magnitude $|F(u, v)|$; they are encoded <em>strictly in the linear phase gradient</em>.<br>
2. <strong>Constructive Interference at Edges:</strong>
Sharp visual boundaries (step edges, lines, corners) are formed when sinusoids across many different frequencies align in phase at a specific coordinate $(x_0, y_0)$ to produce <strong>constructive interference</strong>. Disrupting the phase scrambles where constructive interference occurs, obliterating all edges.<br>
3. <strong>Universality of Natural Image Magnitudes:</strong>
Almost all natural photographs exhibit the same power-law power spectral density:
$$M(u, v) \\approx \\frac{C}{(u^2 + v^2)^{\\alpha/2}}, \\quad \\alpha \\approx 2$$
Because all natural images have nearly identical magnitude spectra (smooth $1/f^2$ energy decay), magnitude carries virtually zero discriminating structural information.</p>

<p><span class="part">Part (c): Reconstruction from Phase Alone</span><br>
Setting magnitude to constant $M(u, v) = 1$:
$$F_{\\text{phase}}(u, v) = e^{j \\phi_A(u, v)} = \\frac{F_A(u, v)}{|F_A(u, v)|}$$
In the spatial domain, dividing by $|F_A(u, v)| \\propto 1/f$ acts as a powerful <strong>high-pass / whitening filter</strong> ($F \\times f$).<br>
<span class=\"ans\">Reconstructing from phase alone yields a pristine edge map (high-frequency line drawing) of Image A with all outlines intact, proving that phase alone contains the complete structural geometry of an image.</span></p>""",
        "takeaway": "Fourier phase $\\phi(u, v)$ dictates edge locations and geometric structure via constructive interference. Natural images share similar $1/f^2$ magnitude spectra, making phase the primary carrier of visual intelligibility."
    },
    {
        "id": 40793,
        "subject": "DIP",
        "topicId": "07_2D_Fourier_Transforms_CSFT_DSFT_and_DFT",
        "topicTitle": "07 · 2D Fourier Transforms (CSFT, DSFT, DFT)",
        "title": "Fourier Slice (Projection-Slice) Theorem & CT Reconstruction (IISc Endsem / Kak & Slaney)",
        "kind2": "generated",
        "source": "IISc Endsem / Kak & Slaney Principles of Tomographic Imaging",
        "marks": "[8 Marks]",
        "question": """<p>In medical Computed Tomography (CT), an X-ray projection at projection angle $\\theta$ along line parameter $r$ is modeled by the <strong>Radon Transform</strong>:
$$p_\\theta(r) = \\int_{-\\infty}^\\infty \\int_{-\\infty}^\\infty f(x, y) \\, \\delta(x\\cos\\theta + y\\sin\\theta - r) \\, dx dy$$</p>
<p><span class="part">(a)</span> State the <strong>Fourier Slice Theorem</strong> (Projection-Slice Theorem).</p>
<p><span class="part">(b)</span> Prove line-by-line that the 1D Continuous Fourier Transform of the projection $P_\\theta(\\omega) = \\mathcal{F}_{1D}\\{p_\\theta(r)\\}$ equals the 2D Fourier Transform $F(u, v)$ evaluated along a radial line at angle $\\theta$:
$$P_\\theta(\\omega) = F(\\omega\\cos\\theta, \\; \\omega\\sin\\theta)$$</p>
<p><span class="part">(c)</span> Explain why this theorem forms the mathematical foundation of <strong>Filtered Backprojection (FBP)</strong> reconstruction.</p>""",
        "solution": """<p><span class="part">Part (a): Statement of the Fourier Slice Theorem</span><br>
The 1D Fourier Transform of a parallel-beam projection $p_\\theta(r)$ of an image $f(x, y)$ taken at angle $\\theta$ is exactly equal to a 1D slice of the 2D Fourier Transform $F(u, v)$ of the image passing through the origin at orientation angle $\\theta$:
<span class="ans">$$P_\\theta(\\omega) = F(u = \\omega\\cos\\theta, \\; v = \\omega\\sin\\theta)$$</span></p>

<p><span class="part">Part (b): Step-by-Step Proof</span><br>
1. <strong>Rotate spatial coordinates:</strong>
Define rotated coordinates $(r, s)$ where $r$ is perpendicular to the projection rays and $s$ is along the ray:
$$\\begin{pmatrix} r \\\\ s \\end{pmatrix} = \\begin{pmatrix} \\cos\\theta & \\sin\\theta \\\\ -\\sin\\theta & \\cos\\theta \\end{pmatrix} \\begin{pmatrix} x \\\\ y \\end{pmatrix} \\implies \\begin{cases} x = r\\cos\\theta - s\\sin\\theta \\\\ y = r\\sin\\theta + s\\cos\\theta \\end{cases}$$
The Jacobian determinant is 1 ($dx dy = dr ds$). In this frame, the projection simplifies to:
$$p_\\theta(r) = \\int_{-\\infty}^\\infty f(r\\cos\\theta - s\\sin\\theta, \\; r\\sin\\theta + s\\cos\\theta) \\, ds$$
2. <strong>Take 1D Fourier transform of $p_\\theta(r)$:</strong>
$$P_\\theta(\\omega) = \\int_{-\\infty}^\\infty p_\\theta(r) e^{-j 2\\pi \\omega r} dr = \\int_{-\\infty}^\\infty \\left[ \\int_{-\\infty}^\\infty f(r\\cos\\theta - s\\sin\\theta, \\; r\\sin\\theta + s\\cos\\theta) ds \\right] e^{-j 2\\pi \\omega r} dr$$
3. <strong>Substitute back $r = x\\cos\\theta + y\\sin\\theta$:</strong>
Since $dr ds = dx dy$:
$$P_\\theta(\\omega) = \\int_{-\\infty}^\\infty \\int_{-\\infty}^\\infty f(x, y) \\exp\\left( -j 2\\pi \\omega (x\\cos\\theta + y\\sin\\theta) \\right) dx dy$$
Regrouping terms in the exponential:
$$P_\\theta(\\omega) = \\int_{-\\infty}^\\infty \\int_{-\\infty}^\\infty f(x, y) \\exp\\left( -j 2\\pi [(\\omega\\cos\\theta) x + (\\omega\\sin\\theta) y] \\right) dx dy$$
Recalling the definition of the 2D CSFT $F(u, v) = \\iint f(x, y) e^{-j 2\\pi (ux + vy)} dx dy$:
<span class="ans">$$P_\\theta(\\omega) = F(\\omega\\cos\\theta, \\; \\omega\\sin\\theta)$$</span></p>

<p><span class="part">Part (c): Foundation of Filtered Backprojection (FBP)</span><br>
Inverting $F(u, v)$ in polar coordinates $(u = \\omega\\cos\\theta, v = \\omega\\sin\\theta)$ with area element $du dv = |\\omega| d\\omega d\\theta$:
$$f(x, y) = \\int_0^\\pi \\int_{-\\infty}^\\infty F(\\omega\\cos\\theta, \\omega\\sin\\theta) |\\omega| e^{j 2\\pi \\omega (x\\cos\\theta + y\\sin\\theta)} d\\omega d\\theta$$
Substituting $F(\\omega\\cos\\theta, \\omega\\sin\\theta) = P_\\theta(\\omega)$:
<span class="ans">$$f(x, y) = \\int_0^\\pi \\underbrace{\\left[ \\int_{-\\infty}^\\infty P_\\theta(\\omega) |\\omega| e^{j 2\\pi \\omega r} d\\omega \\right]}_{\\text{Ramp-Filtered Projection } \\tilde{p}_\\theta(r)} d\\theta$$</span>
This proves that 2D image reconstruction decomposes into: (1) 1D ramp filtering ($|\\omega|$) of each projection angle, followed by (2) backprojection (integration over all angles $\\theta$).</p>""",
        "takeaway": "The Fourier Slice Theorem $P_\\theta(\\omega) = F(\\omega\\cos\\theta, \\omega\\sin\\theta)$ connects 1D Radon projection transforms to radial 2D frequency slices. The polar Jacobian $|\\omega|$ yields the Ram-Lak filter in Filtered Backprojection."
    },

    # =========================================================================
    # TOPIC 08: Sampling Theorem, Aliasing, and Multi-Rate Conversion
    # =========================================================================
    {
        "id": 40891,
        "subject": "DIP",
        "topicId": "08_Sampling_Theorem_Aliasing_and_Multi_Rate_Conversion",
        "topicTitle": "08 · Sampling, Aliasing & Multi-Rate",
        "title": "2D Sampling Theorem, Nyquist Rates & Moiré Aliasing (IISc Midterm / Stanford EE 261)",
        "kind2": "pyq",
        "source": "IISc Midterm / Stanford EE 261 Fourier Transforms",
        "marks": "[8 Marks]",
        "question": """<p>A continuous 2D test pattern is described by:
$$f(x, y) = \\cos\\left(2\\pi(60 x + 80 y)\\right)$$
where spatial coordinates $(x, y)$ are measured in millimeters. The image is digitized using a flatbed scanner with horizontal and vertical sampling rates:
$$f_{sx} = 100 \\text{ samples/mm}, \\qquad f_{sy} = 100 \\text{ samples/mm}$$</p>
<p><span class="part">(a)</span> Determine the true continuous spatial frequencies $(u_0, v_0)$ and state the minimum horizontal and vertical Nyquist sampling rates required to avoid aliasing.</p>
<p><span class="part">(b)</span> Calculate the apparent aliased spatial frequencies $(u_a, v_a)$ observed in the baseband digital image $[-f_s/2, f_s/2]$.</p>
<p><span class="part">(c)</span> Write the equation of the reconstructed aliased continuous image $f_{\\text{alias}}(x, y)$. Compare the true wave orientation angle $\\theta_0$ with the aliased orientation angle $\\theta_a$.</p>""",
        "solution": """<p><span class="part">Part (a): True Frequencies & Nyquist Limits</span><br>
Comparing with $\\cos(2\\pi(u_0 x + v_0 y))$:
- True horizontal frequency: $u_0 = <span class=\"ans\">60 \\text{ cycles/mm}</span>$
- True vertical frequency: $v_0 = <span class=\"ans\">80 \\text{ cycles/mm}</span>$<br>
By the 2D Shannon-Nyquist Sampling Theorem, sampling rates must strictly exceed twice the highest spatial frequency:
$$f_{sx} \\ge 2 u_0 = 2(60) = <span class=\"ans\">120 \\text{ samples/mm}</span>$$
$$f_{sy} \\ge 2 v_0 = 2(80) = <span class=\"ans\">160 \\text{ samples/mm}</span>$$
Since the actual sampling rates are $f_{sx} = 100 < 120$ and $f_{sy} = 100 < 160$, the Nyquist criterion is violated in both dimensions. Severe 2D aliasing occurs.</p>

<p><span class="part">Part (b): Aliased Baseband Frequencies</span><br>
Sampling creates spectral replicas at $(u_0 + m f_{sx}, \\; v_0 + n f_{sy})$ for integers $m, n \\in \\mathbb{Z}$.<br>
The principal baseband region is $[-f_s/2, f_s/2] = [-50, 50]$ cycles/mm:
- <strong>Horizontal alias ($m = -1$):</strong>
$$u_a = u_0 - f_{sx} = 60 - 100 = -40 \\in [-50, 50] \\implies |u_a| = 40 \\text{ cycles/mm}$$
- <strong>Vertical alias ($n = -1$):</strong>
$$v_a = v_0 - f_{sy} = 80 - 100 = -20 \\in [-50, 50] \\implies |v_a| = 20 \\text{ cycles/mm}$$
<span class=\"ans\">Apparent aliased frequencies: $(u_a, v_a) = (-40, -20) \\equiv (40, 20)$ cycles/mm.</span></p>

<p><span class="part">Part (c): Aliased Image & Orientation Distortion</span><br>
The reconstructed waveform from ideal low-pass interpolation is:
$$f_{\\text{alias}}(x, y) = \\cos(2\\pi(-40 x - 20 y)) = \\cos(2\\pi(40 x + 20 y))$$
1. <strong>True Wave Orientation:</strong>
$$\\theta_0 = \\arctan\\left(\\frac{v_0}{u_0}\\right) = \\arctan\\left(\\frac{80}{60}\\right) = \\arctan(1.333) \\approx <span class=\"ans\">53.13^\\circ</span>$$
2. <strong>Aliased Wave Orientation:</strong>
$$\\theta_a = \\arctan\\left(\\frac{v_a}{u_a}\\right) = \\arctan\\left(\\frac{20}{40}\\right) = \\arctan(0.500) \\approx <span class=\"ans\">26.57^\\circ</span>$$
<span class=\"ans\">The high-frequency diagonal grating (magnitude $\\sqrt{60^2+80^2} = 100$) aliases down to a much coarser pattern (magnitude $\\sqrt{40^2+20^2} \\approx 44.72$), and its angle rotates from $53.13^\\circ$ down to $26.57^\\circ$, producing visual Moiré fringes.</span></p>""",
        "takeaway": "2D aliasing folds frequencies outside the Nyquist box $[-f_s/2, f_s/2]$: $u_a = u_0 - f_{sx}$. Aliasing distorts both spatial frequency magnitude and wave propagation angle $\\theta = \\arctan(v/u)$, generating Moiré artifacts."
    },
    {
        "id": 40892,
        "subject": "DIP",
        "topicId": "08_Sampling_Theorem_Aliasing_and_Multi_Rate_Conversion",
        "topicTitle": "08 · Sampling, Aliasing & Multi-Rate",
        "title": "Burt-Adelson 5-Tap Gaussian Pyramid Filter Derivation (IISc Midterm / Burt & Adelson 1983)",
        "kind2": "university",
        "source": "IISc Midterm / Burt & Adelson IEEE Trans. Comm. (1983)",
        "marks": "[8 Marks]",
        "question": """<p>The Burt-Adelson Gaussian pyramid uses a symmetric 1D 5-tap generating kernel $\\mathbf{w} = [c, b, a, b, c]$ centered at $n = 0$ for multiresolution downsampling by factor 2.</p>
<p><span class="part">(a)</span> State the three axiomatic mathematical constraints imposed on $\\mathbf{w}$:</p>
<ol>
<li>Symmetry: $w(n) = w(-n)$</li>
<li>Unit DC gain (Normalization): $\\sum_{n=-2}^2 w(n) = 1$</li>
<li>Equal contribution condition (each pixel at level $l$ contributes equally to level $l+1$)</li>
</ol>
<p><span class="part">(b)</span> Solve for filter weights $b$ and $c$ in terms of the central tap parameter $a$.</p>
<p><span class="part">(c)</span> For the canonical Burt-Adelson choice $a = 0.40$, evaluate the exact numerical tap weights and explain why $a = 0.40$ provides the closest approximation to a continuous Gaussian filter.</p>""",
        "solution": """<p><span class="part">Part (a): The Three Axiomatic Constraints</span><br>
1. <strong>Symmetry:</strong> $w(-1) = w(1) = b$ and $w(-2) = w(2) = c$, yielding $\\mathbf{w} = [c, b, a, b, c]$.<br>
2. <strong>Normalization (Unit DC Gain):</strong>
$$c + b + a + b + c = 1 \\implies a + 2b + 2c = 1$$
3. <strong>Equal Contribution Condition:</strong>
When downsampling by 2 ($g_{l+1}(i) = \\sum_m w(m) g_l(2i + m)$), even-positioned pixels in $g_l$ are weighted by even taps ($a$ and $c$), while odd-positioned pixels are weighted by odd taps ($b$). For all pixels to contribute identical total weight across levels:
$$\\sum_{\\text{even } n} w(n) = \\sum_{\\text{odd } n} w(n) \\implies a + 2c = 2b$$</p>

<p><span class="part">Part (b): Solution for $b$ and $c$ in terms of $a$</span><br>
Substitute the equal contribution constraint $a + 2c = 2b$ into the normalization condition $a + 2b + 2c = 1$:
$$(a + 2c) + 2b = 1 \\implies 2b + 2b = 1 \\implies 4b = 1$$
<span class="ans">$$b = \\frac{1}{4} = 0.25$$</span>
Remarkably, $b = 0.25$ is universally fixed for <em>any</em> valid Burt-Adelson filter!<br>
Now solve for $c$:
$$2c = 2b - a = 2(0.25) - a = 0.50 - a$$
<span class="ans">$$c = \\frac{1}{4} - \\frac{a}{2} = 0.25 - 0.50 a$$</span></p>

<p><span class="part">Part (c): Canonical Weights for $a = 0.40$</span><br>
With $a = 0.40$:
- $b = 0.25$
- $c = 0.25 - 0.50(0.40) = 0.25 - 0.20 = 0.05$<br>
The discrete 5-tap kernel is:
<span class="ans">$$\\mathbf{w} = [0.05, \\, 0.25, \\, 0.40, \\, 0.25, \\, 0.05]$$</span>
<strong>Gaussian Approximation Rationale:</strong>
- If $a = 0.50 \\implies c = 0$, the filter degenerates into a 3-tap triangle $[0.25, 0.50, 0.25]$ (too narrow, insufficient anti-aliasing).
- If $a = 0.30 \\implies c = 0.10$, the filter becomes overly broad and flat.
- At $a = 0.40$, the ratio $\\frac{w(0)}{w(1)} = \\frac{0.40}{0.25} = 1.60$ and $\\frac{w(1)}{w(2)} = \\frac{0.25}{0.05} = 5.00$ closely match the exponential decay of a continuous Gaussian bell curve $e^{-x^2 / (2\\sigma^2)}$ with $\\sigma \\approx 1.0$, providing optimal anti-aliasing before downsampling.</p>""",
        "takeaway": "The Burt-Adelson equal-contribution constraint $a+2c=2b$ uniquely fixes $b=0.25$ and $c=0.25-a/2$. The canonical parameter $a=0.40$ gives $\\mathbf{w}=[0.05, 0.25, 0.40, 0.25, 0.05]$, forming a nearly ideal Gaussian pyramid."
    },
    {
        "id": 40893,
        "subject": "DIP",
        "topicId": "08_Sampling_Theorem_Aliasing_and_Multi_Rate_Conversion",
        "topicTitle": "08 · Sampling, Aliasing & Multi-Rate",
        "title": "Multi-Band Laplacian Pyramid Image Blending (MIT 6.869 / Burt & Adelson)",
        "kind2": "generated",
        "source": "MIT 6.869 / Burt & Adelson ACM Trans. Graphics",
        "marks": "[8 Marks]",
        "question": """<p>Two images $A$ and $B$ are to be seamlessly joined along a seam boundary defined by a binary transition mask $M$ ($M(x, y) = 1$ for image $A$, $M(x, y) = 0$ for image $B$). Direct spatial alpha-blending $I = M \\odot A + (1 - M) \\odot B$ causes visible edge seams if the transition is narrow, and severe ghosting (double exposure) if the transition is wide.</p>
<p><span class="part">(a)</span> Formulate the step-by-step algorithm for <strong>Multi-Band Laplacian Pyramid Blending</strong>.</p>
<p><span class="part">(b)</span> Write the explicit mathematical blending equation for the combined Laplacian pyramid $L_{\\text{blend}, l}$ at octave scale level $l \\in \\{0, 1, \\dots, N\\}$.</p>
<p><span class="part">(c)</span> Explain why decomposing images into bandpass octaves simultaneously eliminates edge boundaries and ghosting artifacts.</p>""",
        "solution": """<p><span class="part">Part (a): Step-by-Step Multi-Band Blending Algorithm</span><br>
1. <strong>Construct Gaussian Pyramids:</strong>
Build Gaussian pyramids $G_{A, l}$ for image $A$, $G_{B, l}$ for image $B$, and $G_{M, l}$ for binary mask $M$ across levels $l = 0, \\dots, N$ using Burt-Adelson $\\text{Reduce}$ operations.<br>
2. <strong>Construct Laplacian Pyramids:</strong>
Compute bandpass detail images for $A$ and $B$:
$$L_{A, l} = G_{A, l} - \\text{Expand}(G_{A, l+1}), \\qquad L_{B, l} = G_{B, l} - \\text{Expand}(G_{B, l+1})$$
with base residual $L_{A, N} = G_{A, N}$ and $L_{B, N} = G_{B, N}$.<br>
3. <strong>Multi-Band Masked Splicing:</strong>
At each level $l$, blend the bandpass details using the corresponding blurred mask $G_{M, l}$.<br>
4. <strong>Pyramid Reconstruction (Collapse):</strong>
Reconstruct the blended composite from the coarsest level $N$ down to level 0:
$$I_N = L_{\\text{blend}, N}, \\qquad I_l = L_{\\text{blend}, l} + \\text{Expand}(I_{l+1})$$
The final blended image is $I_0$.</p>

<p><span class="part">Part (b): Blending Equation at Octave Level $l$</span><br>
At octave level $l$:
<span class="ans">$$L_{\\text{blend}, l}(x, y) = G_{M, l}(x, y) \\odot L_{A, l}(x, y) + \\left(1 - G_{M, l}(x, y)\\right) \\odot L_{B, l}(x, y)$$</span>
where $\\odot$ denotes pixel-wise Hadamard product.<br>
At the coarsest base level $l = N$:
$$G_{\\text{blend}, N}(x, y) = G_{M, N}(x, y) \\odot G_{A, N}(x, y) + \\left(1 - G_{M, N}(x, y)\\right) \\odot G_{B, N}(x, y)$$</p>

<p><span class="part">Part (c): Why Multi-Band Blending Eliminates Ghosting & Seams</span><br>
At scale level $l$, the spatial transition width of mask $G_{M, l}$ is proportional to $2^l$ pixels:
1. <strong>Fine High Frequencies ($l = 0, 1$):</strong> The mask transition zone is narrow (1 to 2 pixels). Fine textures, sharp edges, and skin pores transition abruptly across the seam, preventing two different high-frequency patterns from overlapping and causing <strong>ghosting / double exposure</strong>.<br>
2. <strong>Coarse Low Frequencies ($l = N-1, N$):</strong> The mask transition zone is very wide ($2^N$ pixels, tens or hundreds of pixels wide). Broad lighting gradients, skin tone variations, and illumination smoothly cross-fade over a broad region, completely hiding <strong>brightness seams and color mismatches</strong>.<br>
<span class=\"ans\">Matching transition zone width to spatial frequency wavelength ($\\Delta x \\sim \\lambda$) guarantees that every spatial scale blends over its natural spatial extent, producing seamless photomontages.</span></p>""",
        "takeaway": "Laplacian pyramid blending splices bandpass details with matching mask scales: $L_{\\text{blend}, l} = G_{M, l} L_A + (1-G_{M, l})L_B$. High frequencies blend narrowly to avoid ghosting, while low frequencies blend broadly to eliminate illumination seams."
    }
]

def main():
    with open(PRACTICE_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    if "40791" in content:
        print("Batch 07-08 already present in practice_dip.js!")
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
    for card in PRACTICE_DIP_07_08:
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

    print("Successfully added DIP Batch 07-08 (6 cards). Total in file now updated.")

if __name__ == "__main__":
    main()
