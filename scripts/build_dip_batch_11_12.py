#!/usr/bin/env python3
"""
Builder script for DIP Practice Cards: Batch 06 (Topics 11 & 12)
Topic 11: Image Restoration: Inverse and Wiener Filtering (Cards 41191, 41192, 41193)
Topic 12: Non-Linear Restoration: Median and Bilateral Filters (Cards 41291, 41292, 41293)
"""

import json
import os
import re

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRACTICE_FILE = os.path.join(REPO_DIR, "practice_dip.js")

PRACTICE_DIP_11_12 = [
    # =========================================================================
    # TOPIC 11: Image Restoration: Inverse and Wiener Filtering
    # =========================================================================
    {
        "id": 41191,
        "subject": "DIP",
        "topicId": "11_Image_Restoration_Inverse_and_Wiener_Filtering",
        "topicTitle": "11 · Restoration: Inverse & Wiener",
        "title": "Wiener Filter Derivation via Minimum Mean Square Error (IISc Midterm / Gonzalez & Woods)",
        "kind2": "pyq",
        "source": "IISc Midterm / Gonzalez & Woods Digital Image Processing",
        "marks": "[8 Marks]",
        "question": """<p>Consider the linear image degradation model in the frequency domain:
$$G(u, v) = H(u, v) F(u, v) + N(u, v)$$
where $F(u, v)$ is the original uncorrupted image and $N(u, v)$ is additive noise. Assume $F$ and $N$ are zero-mean independent random processes with Power Spectral Densities $S_f(u, v) = \\mathbb{E}[|F|^2]$ and $S_\\eta(u, v) = \\mathbb{E}[|N|^2]$. We seek an optimal linear filter $\\hat{F}(u, v) = W(u, v) G(u, v)$.</p>
<p><span class="part">(a)</span> Formulate the Mean Squared Error cost function $J(W) = \\mathbb{E}[|F - \\hat{F}|^2]$ and differentiate with respect to $W^*$ to derive the optimal <strong>Wiener Filter</strong> transfer function $W(u, v)$.</p>
<p><span class="part">(b)</span> Express $W(u, v)$ in terms of the unconstrained inverse filter $\\frac{1}{H(u, v)}$ and the Signal-to-Noise Ratio $\\text{SNR}(u, v) = \\frac{S_f(u, v)}{S_\\eta(u, v)}$.</p>
<p><span class="part">(c)</span> Contrast the behavior of the Wiener filter with the direct inverse filter in the two extreme asymptotic regimes: (i) noise-free ($\text{SNR} \\to \\infty$), and (ii) spectral nulls ($|H(u, v)| \\to 0$).</p>""",
        "solution": """<p><span class="part">Part (a): Wiener Filter Derivation via MMSE</span><br>
Expand the error metric:
$$J(W) = \\mathbb{E}[|F - W G|^2] = \\mathbb{E}[(F - W G)(F^* - W^* G^*)]$$
$$= \\mathbb{E}[|F|^2] - W \\mathbb{E}[G F^*] - W^* \\mathbb{E}[F G^*] + |W|^2 \\mathbb{E}[|G|^2]$$
Substitute $G = H F + N$. By independence of signal and noise, $\\mathbb{E}[F N^*] = 0$:
- $\\mathbb{E}[F G^*] = \\mathbb{E}[F (H^* F^* + N^*)] = H^* \\mathbb{E}[|F|^2] = H^* S_f$
- $\\mathbb{E}[G F^*] = H S_f$
- $\\mathbb{E}[|G|^2] = \\mathbb{E}[(H F + N)(H^* F^* + N^*)] = |H|^2 S_f + S_\\eta$<br>
Thus:
$$J(W) = S_f - W H S_f - W^* H^* S_f + W W^* (|H|^2 S_f + S_\\eta)$$
Differentiating with respect to complex conjugate $W^*$ and setting to zero (Wirtinger derivative):
$$\\frac{\\partial J}{\\partial W^*} = -H^* S_f + W (|H|^2 S_f + S_\\eta) = 0$$
Solving for $W(u, v)$:
<span class="ans">$$W(u, v) = \\frac{H^*(u, v) S_f(u, v)}{|H(u, v)|^2 S_f(u, v) + S_\\eta(u, v)} = \\frac{H^*(u, v)}{|H(u, v)|^2 + \\frac{S_\\eta(u, v)}{S_f(u, v)}}$$</span></p>

<p><span class="part">Part (b): Representation via Inverse Filter & SNR</span><br>
Factor out $\\frac{1}{H(u, v)}$ by multiplying and dividing numerator by $H$:
$$W(u, v) = \\frac{H^* H}{H \\left(|H|^2 + \\frac{S_\\eta}{S_f}\\right)} = \\frac{1}{H(u, v)} \\left[ \\frac{|H(u, v)|^2}{|H(u, v)|^2 + \\frac{1}{\\text{SNR}(u, v)}} \\right]$$
<span class="ans">where $\\text{SNR}(u, v) = \\frac{S_f(u, v)}{S_\\eta(u, v)}$.</span> The bracketed term acts as a frequency-dependent attenuation factor in $[0, 1]$.</p>

<p><span class="part">Part (c): Asymptotic Regime Comparison</span><br>
1. <strong>Noise-Free Limit ($\\text{SNR} \\to \\infty \\iff S_\\eta \\to 0$):</strong>
$$\\lim_{\\text{SNR} \\to \\infty} W(u, v) = \\frac{1}{H(u, v)} \\left[ \\frac{|H|^2}{|H|^2 + 0} \\right] = <span class=\"ans\">\\frac{1}{H(u, v)}</span>$$
The Wiener filter converges exactly to the direct inverse filter, achieving complete deconvolution.<br>
2. <strong>Near Spectral Nulls ($|H(u, v)| \\to 0$ with $S_\\eta > 0$):</strong>
- Direct inverse filter: $W_{\\text{inv}} = \\frac{1}{H} \\to \\infty$, catastrophically blowing up high-frequency noise and rendering the restored image useless.
- Wiener filter:
<span class="ans">$$\\lim_{|H| \\to 0} W(u, v) = \\lim_{|H| \\to 0} \\frac{H^*}{|H|^2 + S_\\eta/S_f} = \\frac{0}{0 + S_\\eta/S_f} = 0$$</span>
The Wiener filter smoothly attenuates frequencies where the blur function vanishes, preventing noise explosion.</p>""",
        "takeaway": "Wiener filtering minimizes mean square error: $W = \\frac{H^*}{|H|^2 + 1/\\text{SNR}}$. It acts as an inverse filter $1/H$ where SNR is high, and smoothly shuts down $W \\to 0$ at spectral nulls $|H| \\to 0$, suppressing noise explosion."
    },
    {
        "id": 41192,
        "subject": "DIP",
        "topicId": "11_Image_Restoration_Inverse_and_Wiener_Filtering",
        "topicTitle": "11 · Restoration: Inverse & Wiener",
        "title": "Uniform Motion Blur Transfer Function & Sinc Nulls (IIT Delhi / Bovik)",
        "kind2": "university",
        "source": "IIT Delhi / Bovik Handbook of Image and Video Processing",
        "marks": "[8 Marks]",
        "question": """<p>During a camera shutter exposure duration $T$, planar camera motion causes relative uniform linear displacement between scene and sensor described by velocity vector components:
$$x_0(t) = \\frac{a t}{T}, \\qquad y_0(t) = \\frac{b t}{T}, \\quad 0 \\le t \\le T$$</p>
<p><span class="part">(a)</span> Formulate the degraded blurred image $g(x, y)$ as a continuous time integral of the moving scene $f(x - x_0(t), y - y_0(t))$.</p>
<p><span class="part">(b)</span> Apply the 2D Fourier transform to derive the analytical optical transfer function $H(u, v) = \\mathcal{F}\\{h(x, y)\\}$ in terms of the $\\operatorname{sinc}$ function.</p>
<p><span class="part">(c)</span> For purely horizontal camera shake ($b = 0, a = 10 \\text{ pixels}, T = 1$), find the periodic nulls (zero-crossings) of $H(u, v)$ along the $u$-axis. Why does direct inverse filtering fail completely on motion-blurred images?</p>""",
        "solution": """<p><span class="part">Part (a): Continuous Motion Degradation Integral</span><br>
The captured image is the accumulated sensor irradiance integrated over exposure time $[0, T]$:
<span class="ans">$$g(x, y) = \\frac{1}{T} \\int_0^T f\\left(x - \\frac{a t}{T}, \\; y - \\frac{b t}{T}\\right) dt$$</span></p>

<p><span class="part">Part (b): 2D Fourier Transfer Function Derivation</span><br>
Taking the 2D Fourier transform of $g(x, y)$:
$$G(u, v) = \\int_{-\\infty}^\\infty \\int_{-\\infty}^\\infty \\left[ \\frac{1}{T} \\int_0^T f\\left(x - \\frac{at}{T}, y - \\frac{bt}{T}\\right) dt \\right] e^{-j 2\\pi (ux + vy)} dx dy$$
Interchanging the order of integration and using the spatial shift theorem:
$$G(u, v) = \\frac{1}{T} \\int_0^T \\left[ \\int_{-\\infty}^\\infty \\int_{-\\infty}^\\infty f\\left(x - \\frac{at}{T}, y - \\frac{bt}{T}\\right) e^{-j 2\\pi (ux + vy)} dx dy \\right] dt$$
$$= \\frac{1}{T} \\int_0^T F(u, v) \\exp\\left( -j 2\\pi \\left( u \\frac{at}{T} + v \\frac{bt}{T} \\right) \\right) dt = F(u, v) \\cdot \\frac{1}{T} \\int_0^T e^{-j 2\\pi (ua + vb) \\frac{t}{T}} dt$$
Evaluating the 1D exponential integral:
$$H(u, v) = \\frac{1}{T} \\left[ \\frac{e^{-j 2\\pi (ua + vb) \\frac{t}{T}}}{-j 2\\pi (ua + vb) / T} \\right]_0^T = \\frac{1 - e^{-j 2\\pi (ua + vb)}}{j 2\\pi (ua + vb)}$$
Factoring out symmetric phase $e^{-j \\pi (ua + vb)}$:
$$H(u, v) = \\frac{e^{j \\pi (ua + vb)} - e^{-j \\pi (ua + vb)}}{2j} \\cdot \\frac{e^{-j \\pi (ua + vb)}}{\\pi (ua + vb)} = \\frac{\\sin(\\pi(ua + vb))}{\\pi (ua + vb)} e^{-j \\pi (ua + vb)}$$
<span class="ans">$$H(u, v) = \\operatorname{sinc}(ua + vb) \\exp\\left(-j \\pi (ua + vb)\\right)$$</span></p>

<p><span class="part">Part (c): Sinc Nulls & Failure of Inverse Filtering</span><br>
With $b = 0, a = 10, T = 1$:
$$H(u, v) = \\operatorname{sinc}(10 u) e^{-j 10 \\pi u}$$
Zero-crossings occur wherever the argument of $\\operatorname{sinc}(10u)$ is a nonzero integer:
$$10 u = m \\implies <span class=\"ans\">u = \\pm \\frac{m}{10} = \\pm 0.1, \\; \\pm 0.2, \\; \\pm 0.3, \\; \\dots \\text{ cycles/pixel}</span>$$
<strong>Failure of Direct Inverse Filtering:</strong>
At every periodic frequency null $u = \\pm 0.1 m$, $H(u, v) = 0$.
The inverse filter $W_{\\text{inv}}(u, v) = \\frac{1}{H(u, v)} = \\frac{1}{0} = \\infty$.
Even minuscule sensor noise $N(u, v)$ at these null frequencies is multiplied by $\\infty$, completely destroying the reconstruction. Constrained regularization (Wiener or CLS) is strictly necessary.</p>""",
        "takeaway": "Uniform motion blur has transfer function $H(u, v) = \\operatorname{sinc}(ua + vb)e^{-j\\pi(ua+vb)}$. The periodic nulls at $ua+vb = m$ destroy frequency information, causing direct inverse filtering $1/H$ to diverge."
    },
    {
        "id": 41193,
        "subject": "DIP",
        "topicId": "11_Image_Restoration_Inverse_and_Wiener_Filtering",
        "topicTitle": "11 · Restoration: Inverse & Wiener",
        "title": "Constrained Least Squares (CLS) Regularized Restoration (IISc Endsem / Hunt)",
        "kind2": "generated",
        "source": "IISc Endsem / Hunt IEEE Trans. Computers (1973)",
        "marks": "[8 Marks]",
        "question": """<p>The <strong>Constrained Least Squares (CLS)</strong> restoration algorithm eliminates the need to estimate signal and noise power spectral densities by formulating restoration as an optimization problem:
$$\\min_{\\hat{\\mathbf{f}}} \\|C \\hat{\\mathbf{f}}\\|^2 \\quad \\text{subject to} \\quad \\|\\mathbf{g} - H \\hat{\\mathbf{f}}\\|^2 = \\|\\boldsymbol{\\eta}\\|^2$$
where $\\mathbf{g} = H \\mathbf{f} + \\boldsymbol{\\eta}$ is the lexicographically ordered degraded image, $H$ is the blur matrix, $\\boldsymbol{\\eta}$ is additive noise with known total energy $\\|\\boldsymbol{\\eta}\\|^2$, and $C$ is a high-pass 2D discrete Laplacian smoothness operator.</p>
<p><span class="part">(a)</span> Use the method of Lagrange multipliers to derive the matrix normal equation for $\\hat{\\mathbf{f}}$.</p>
<p><span class="part">(b)</span> Assuming block-circulant matrices diagonalized by the 2D DFT, express the CLS restoration filter $W_{\\text{CLS}}(u, v)$ in the discrete frequency domain.</p>
<p><span class="part">(c)</span> Explain how the regularization parameter $\\gamma$ controls the trade-off between noise amplification and spatial sharpness.</p>""",
        "solution": """<p><span class="part">Part (a): Lagrangian Optimization & Normal Equations</span><br>
Formulate the Lagrangian with Lagrange multiplier $\\lambda > 0$:
$$\\mathcal{L}(\\hat{\\mathbf{f}}, \\lambda) = \\|C \\hat{\\mathbf{f}}\\|^2 + \\lambda \\left( \\|\\mathbf{g} - H \\hat{\\mathbf{f}}\\|^2 - \\|\\boldsymbol{\\eta}\\|^2 \\right)$$
Expanding into matrix vector form:
$$\\mathcal{L}(\\hat{\\mathbf{f}}, \\lambda) = \\hat{\\mathbf{f}}^\\top C^\\top C \\hat{\\mathbf{f}} + \\lambda \\left( \\mathbf{g}^\\top \\mathbf{g} - 2 \\hat{\\mathbf{f}}^\\top H^\\top \\mathbf{g} + \\hat{\\mathbf{f}}^\\top H^\\top H \\hat{\\mathbf{f}} - \\|\\boldsymbol{\\eta}\\|^2 \\right)$$
Taking the vector gradient with respect to $\\hat{\\mathbf{f}}$ and setting to zero:
$$\\nabla_{\\hat{\\mathbf{f}}} \\mathcal{L} = 2 C^\\top C \\hat{\\mathbf{f}} - 2\\lambda H^\\top \\mathbf{g} + 2\\lambda H^\\top H \\hat{\\mathbf{f}} = \\mathbf{0}$$
Dividing by $2\\lambda$ and setting $\\gamma = 1/\\lambda$:
$$\\gamma C^\\top C \\hat{\\mathbf{f}} + H^\\top H \\hat{\\mathbf{f}} = H^\\top \\mathbf{g}$$
<span class="ans">$$\\left( H^\\top H + \\gamma C^\\top C \\right) \\hat{\\mathbf{f}} = H^\\top \\mathbf{g} \\implies \\hat{\\mathbf{f}} = \\left( H^\\top H + \\gamma C^\\top C \\right)^{-1} H^\\top \\mathbf{g}$$</span></p>

<p><span class="part">Part (b): Frequency-Domain CLS Transfer Function</span><br>
Because $H$ and $C$ are block-circulant convolution operators, they are simultaneously diagonalized by the 2D Discrete Fourier Transform matrix $U$:
$$H = U^\\dagger \\Lambda_H U, \\qquad C = U^\\dagger \\Lambda_C U$$
In the frequency domain, the matrix inversion becomes simple scalar division at each frequency coordinate $(u, v)$:
<span class="ans">$$\\hat{F}(u, v) = W_{\\text{CLS}}(u, v) G(u, v) = \\left[ \\frac{H^*(u, v)}{|H(u, v)|^2 + \\gamma |P(u, v)|^2} \\right] G(u, v)$$</span>
where $P(u, v)$ is the 2D Fourier transform of the $3 \\times 3$ discrete Laplacian mask $p = \\begin{pmatrix} 0 & 1 & 0 \\\\ 1 & -4 & 1 \\\\ 0 & 1 & 0 \\end{pmatrix}$.</p>

<p><span class="part">Part (c): Role of Regularization Parameter $\\gamma$</span><br>
- <strong>Small $\\gamma \\to 0$:</strong> Prioritizes data fidelity ($\\|\\mathbf{g} - H\\hat{\\mathbf{f}}\\|^2 \\to 0$). The filter behaves like an unconstrained inverse filter $1/H$, producing sharp deblurring but severe noise amplification.<br>
- <strong>Large $\\gamma \\to \\infty$:</strong> Prioritizes smoothness ($\\|C\\hat{\\mathbf{f}}\\|^2 \\to 0$). Laplacian high frequencies $|P(u, v)|^2$ dominate the denominator, suppressing all noise but creating heavy blurring.<br>
<span class=\"ans\">Optimal $\\gamma$ is uniquely determined by Newton-Raphson iteration so that residual norm $\\|\\mathbf{g} - H\\hat{\\mathbf{f}}\\|^2$ matches the exact known noise variance $\\|\\boldsymbol{\\eta}\\|^2$.</span></p>""",
        "takeaway": "Constrained Least Squares (CLS) minimizes Laplacian roughness $\|C\hat{\mathbf{f}}\|^2$ subject to residual noise constraint, yielding $W_{\\text{CLS}} = \\frac{H^*}{|H|^2 + \\gamma |P|^2}$. This avoids needing signal power spectra while guaranteeing regularized deconvolution."
    },

    # =========================================================================
    # TOPIC 12: Non-Linear Restoration: Median and Bilateral Filters
    # =========================================================================
    {
        "id": 41291,
        "subject": "DIP",
        "topicId": "12_Non_Linear_Restoration_Median_and_Bilateral_Filters",
        "topicTitle": "12 · Median & Bilateral Filters",
        "title": "Median Filter vs Linear Averaging on Impulse Noise (IISc Midterm / Gonzalez & Woods)",
        "kind2": "pyq",
        "source": "IISc Midterm / Gonzalez & Woods Digital Image Processing",
        "marks": "[8 Marks]",
        "question": """<p>A $3 \\times 3$ image neighborhood centered at $(x, y)$ has been corrupted by a pepper noise impulse at the central pixel:
$$I = \\begin{pmatrix}
90 & 92 & 91 \\\\
89 & \\mathbf{0} & 93 \\\\
91 & 90 & 92
\\end{pmatrix}$$</p>
<p><span class="part">(a)</span> Compute the restored central pixel intensity using a $3 \\times 3$ linear arithmetic mean filter.</p>
<p><span class="part">(b)</span> Compute the restored central pixel intensity using a $3 \\times 3$ non-linear median filter.</p>
<p><span class="part">(c)</span> Compare the outputs and explain theoretically why linear LTI filters fail catastrophically on impulse noise (salt-and-pepper) while order-statistic filters excel.</p>""",
        "solution": """<p><span class="part">Part (a): Linear Mean Filter Restoration</span><br>
The arithmetic mean averages all 9 pixels in the $3 \\times 3$ window:
$$\\hat{I}_{\\text{mean}} = \\frac{1}{9} \\sum_{i=1}^3 \\sum_{j=1}^3 I_{ij} = \\frac{90 + 92 + 91 + 89 + 0 + 93 + 91 + 90 + 92}{9} = \\frac{728}{9} \\approx <span class=\"ans\">80.89 \\to 81</span>$$
Notice that the uncorrupted background pixels are clustered around $91$.
The zero impulse drags the linear average down by $10$ full gray levels, replacing the sharp impulse with an obnoxious, blurry dark smudge of radius $1$.</p>

<p><span class="part">Part (b): Median Filter Restoration</span><br>
Collect and sort all 9 neighborhood intensities in ascending rank order:
$$[0, \\quad 89, \\quad 90, \\quad 90, \\quad \\mathbf{91}, \\quad 91, \\quad 92, \\quad 92, \\quad 93]$$
The median is the 5th order statistic:
<span class="ans">$$\\hat{I}_{\\text{median}} = I_{(5)} = 91$$</span>
The pepper noise impulse ($0$) is pushed to the extreme leftmost boundary ($I_{(1)} = 0$) and completely discarded. The median filter reproduces the true uncorrupted background value $91$ with $100\\%$ precision.</p>

<p><span class="part">Part (c): Theoretical Comparison</span><br>
1. <strong>Failure of Linear Filters:</strong> Linear convolution operators $\\sum h(m, n) I(x-m, y-n)$ are non-robust linear combinations. An impulse outlier has high leverage; linear smoothing spreads its corrupted energy over the entire filter support size $K \\times K$, creating blurry halos.<br>
2. <strong>Success of Order-Statistic Filters:</strong> The median filter is a rank-order selector with a <strong>breakdown point of 50%</strong>. As long as fewer than $\\lfloor N/2 \\rfloor = 4$ pixels in a $3 \\times 3$ window are corrupted, the extreme noise spikes reside entirely in the tails ($I_{(1)}, \\dots, I_{(k)}$ or $I_{(N-k)}, \\dots, I_{(N)}$) and have zero influence on the median $I_{(5)}$. Furthermore, since the output is always an existing pixel from the neighborhood, edges are preserved without blurring.</p>""",
        "takeaway": "Linear mean filtering averages outlier impulses into blurry smudges ($0 \\to 81$). Median filtering sorts neighborhood intensities, isolating impulse spikes in the rank extremes to restore the exact true background level ($91$) with 50% breakdown resilience."
    },
    {
        "id": 41292,
        "subject": "DIP",
        "topicId": "12_Non_Linear_Restoration_Median_and_Bilateral_Filters",
        "topicTitle": "12 · Median & Bilateral Filters",
        "title": "Bilateral Filter Edge-Preserving Weights (IISc Midterm / Tomasi & Manduchi 1998)",
        "kind2": "university",
        "source": "IISc Midterm / Tomasi & Manduchi ICCV (1998)",
        "marks": "[8 Marks]",
        "question": """<p>Consider a 1D sharp step edge defined on discrete integer points $x \\in \\mathbb{Z}$:
$$I(x) = \\begin{cases} 100 & \\text{if } x \\le 0 \\\\ 200 & \\text{if } x \\ge 1 \\end{cases}$$
A 1D bilateral filter is centered at pixel $p = 0$ ($I(0) = 100$) with 3-tap neighborhood $q \\in \\{-1, 0, 1\\}$, spatial parameter $\\sigma_s = 1.0$, and range (photometric) parameter $\\sigma_r = 20.0$:</p>
<p><span class="part">(a)</span> Compute the spatial Gaussian weights $w_s(p, q) = \\exp\\left(-\\frac{(p-q)^2}{2\\sigma_s^2}\\right)$ for each neighbor $q \\in \\{-1, 0, 1\\}$.</p>
<p><span class="part">(b)</span> Compute the range (intensity) Gaussian weights $w_r(p, q) = \\exp\\left(-\\frac{(I(p)-I(q))^2}{2\\sigma_r^2}\\right)$ for each neighbor.</p>
<p><span class="part">(c)</span> Compute total combined weights $w(p, q) = w_s \\cdot w_r$, normalization factor $W_p = \\sum_q w(p, q)$, and the restored intensity $I_{\\text{out}}(0)$. Explain why bilateral filtering preserves the step edge without blurring.</p>""",
        "solution": """<p><span class="part">Part (a): Spatial Gaussian Weights</span><br>
With center $p = 0$ and $\\sigma_s = 1.0 \\implies 2\\sigma_s^2 = 2.0$:
- $q = -1$: $w_s(0, -1) = \\exp\\left(-\\frac{(0 - (-1))^2}{2}\\right) = e^{-0.5} \\approx <span class=\"ans\">0.6065</span>$
- $q = 0$: $w_s(0, 0) = \\exp(0) = <span class=\"ans\">1.0000</span>$
- $q = 1$: $w_s(0, 1) = \\exp\\left(-\\frac{(0 - 1)^2}{2}\\right) = e^{-0.5} \\approx <span class=\"ans\">0.6065</span>$</p>

<p><span class="part">Part (b): Photometric Range Weights</span><br>
With $I(0) = 100$ and $\\sigma_r = 20.0 \\implies 2\\sigma_r^2 = 2(400) = 800$:
- $q = -1$: $I(-1) = 100 \\implies \\Delta I = 0$:
$$w_r(0, -1) = \\exp\\left(-\\frac{0^2}{800}\\right) = <span class=\"ans\">1.0000</span>$$
- $q = 0$: $I(0) = 100 \\implies \\Delta I = 0$:
$$w_r(0, 0) = \\exp(0) = <span class=\"ans\">1.0000</span>$$
- $q = 1$: $I(1) = 200 \\implies \\Delta I = 200 - 100 = 100 = 5\\sigma_r$:
$$w_r(0, 1) = \\exp\\left(-\\frac{100^2}{800}\\right) = \\exp\\left(-\\frac{10000}{800}\\right) = e^{-12.5} \\approx <span class=\"ans\">3.727 \\times 10^{-6} \\approx 0.0000</span>$$</p>

<p><span class="part">Part (c): Total Weights & Output Intensity</span><br>
Multiplying spatial and range components $w(p, q) = w_s(p, q) w_r(p, q)$:
- $w(0, -1) = 0.6065 \\times 1.0000 = 0.6065$
- $w(0, 0) = 1.0000 \\times 1.0000 = 1.0000$
- $w(0, 1) = 0.6065 \\times (3.727 \\times 10^{-6}) \\approx 0.0000023 \\approx 0.0000$<br>
Normalization factor:
$$W_p = \\sum_{q=-1}^1 w(p, q) = 0.6065 + 1.0000 + 0.0000023 = <span class=\"ans\">1.6065</span>$$
Normalized output intensity:
$$I_{\\text{out}}(0) = \\frac{0.6065(100) + 1.0000(100) + 0.0000023(200)}{1.6065} = \\frac{60.65 + 100 + 0.00046}{1.6065} = \\frac{160.65}{1.6065} = <span class=\"ans\">100.00</span>$$
<strong>Edge Preservation Mechanism:</strong>
Because pixel $q = 1$ is across the step edge, its photometric difference ($100$) is five standard deviations away ($5\\sigma_r$). The range Gaussian completely zeroes out its weight ($w_r \\approx 0$). The filter averages only pixels on the same side of the edge, achieving full denoising without blurring the boundary.</p>""",
        "takeaway": "The bilateral filter combines spatial distance $w_s = e^{-\\Delta x^2 / 2\\sigma_s^2}$ and photometric similarity $w_r = e^{-\\Delta I^2 / 2\\sigma_r^2}$. Across sharp edges ($|\\Delta I| \\gg \\sigma_r$), $w_r \\to 0$, effectively cutting off cross-boundary averaging."
    },
    {
        "id": 41293,
        "subject": "DIP",
        "topicId": "12_Non_Linear_Restoration_Median_and_Bilateral_Filters",
        "topicTitle": "12 · Median & Bilateral Filters",
        "title": "Alpha-Trimmed Mean Filter for Mixed Gaussian-Impulse Noise (IIT Delhi / Bovik)",
        "kind2": "generated",
        "source": "IIT Delhi / Bovik Handbook of Image and Video Processing",
        "marks": "[8 Marks]",
        "question": """<p>An image corrupted by mixed noise (additive white Gaussian noise plus occasional salt-and-pepper spikes) is processed by an <strong>alpha-trimmed mean filter</strong> over a $3 \\times 3$ window ($N = 9$). The ordered pixel values in the window are:
$$\\mathbf{I}_{(\\cdot)} = [0, \\, 48, \\, 51, \\, 53, \\, 54, \\, 56, \\, 58, \\, 62, \\, 255]$$</p>
<p><span class="part">(a)</span> Compute the alpha-trimmed mean for trimming parameter $d = 4$ (trimming $d/2 = 2$ lowest and $d/2 = 2$ highest values).</p>
<p><span class="part">(b)</span> Compare the result with the standard arithmetic mean ($d = 0$) and standard median ($d = 8$).</p>
<p><span class="part">(c)</span> Why is the alpha-trimmed mean uniquely superior to both pure linear averaging and pure median filtering in mixed noise environments?</p>""",
        "solution": """<p><span class="part">Part (a): Alpha-Trimmed Mean Calculation ($d = 4$)</span><br>
The alpha-trimmed mean deletes $\\frac{d}{2} = 2$ lowest pixels and $\\frac{d}{2} = 2$ highest pixels:
- Trimmed lowest: $0$ (pepper noise) and $48$
- Trimmed highest: $62$ and $255$ (salt noise)<br>
The remaining $N - d = 9 - 4 = 5$ pixels are:
$$[51, \\quad 53, \\quad 54, \\quad 56, \\quad 58]$$
Averaging the retained 5 pixels:
<span class="ans">$$\\hat{I}_{\\alpha} = \\frac{51 + 53 + 54 + 56 + 58}{5} = \\frac{272}{5} = 54.4 \\approx 54$$</span></p>

<p><span class="part">Part (b): Comparison with Mean & Median</span><br>
1. <strong>Arithmetic Mean ($d = 0$):</strong>
$$\\hat{I}_{\\text{mean}} = \\frac{0 + 48 + 51 + 53 + 54 + 56 + 58 + 62 + 255}{9} = \\frac{637}{9} \\approx <span class=\"ans\">70.78 \\to 71</span>$$
Severely biased by the $255$ salt spike (error of $+17$ gray levels).<br>
2. <strong>Standard Median ($d = 8$):</strong>
The central 5th element of the sorted list is:
<span class="ans">$$\\hat{I}_{\\text{median}} = I_{(5)} = 54$$</span>
The alpha-trimmed mean ($54.4$) is remarkably close to the median ($54$), but averages 5 samples instead of picking just 1.</p>

<p><span class="part">Part (c): Superiority in Mixed Noise Environments</span><br>
1. <strong>Pure Arithmetic Mean:</strong> Optimal for Gaussian noise (minimizes variance by factor $1/N$), but fails completely when impulse spikes are present because outliers corrupt the sum.<br>
2. <strong>Pure Median Filter:</strong> Discards impulse outliers effectively, but has relatively poor noise variance reduction for Gaussian noise (variance efficiency is only $\\frac{2}{\\pi} \\approx 64\\%$ of the sample mean).<br>
3. <strong>Alpha-Trimmed Mean:</strong> Provides the optimal compromise. By trimming $d$ outliers, it completely removes extreme salt-and-pepper spikes, while averaging the remaining $N - d$ samples to achieve $\\frac{\\sigma^2}{N - d}$ variance reduction on the Gaussian noise component.</p>""",
        "takeaway": "The alpha-trimmed mean bridges arithmetic mean ($d=0$) and median ($d=N-1$): it trims $d/2$ extreme outliers to eliminate salt-and-pepper spikes, then averages the remaining $N-d$ samples to suppress Gaussian noise."
    }
]

def main():
    with open(PRACTICE_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    if "41191" in content:
        print("Batch 11-12 already present in practice_dip.js!")
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
    for card in PRACTICE_DIP_11_12:
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

    print("Successfully added DIP Batch 11-12 (6 cards). Total in file now updated.")

if __name__ == "__main__":
    main()
