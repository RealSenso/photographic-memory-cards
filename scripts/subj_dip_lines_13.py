"""DIP Topic 13 (image quality) statements, line by line. After this file exists, change a statement only here."""

SUBJECT = "DIP"

FIX = {
    3121: {"statement": r"""<b>Mean squared error.</b>"""
        r"""<span class="ln">For an original image $f$ and a distorted or restored image $\hat f$, both $M\times N$,</span>"""
        r"""<span class="ln in">$\mathrm{MSE}=\frac1{MN}\sum_{x,y}\big[f(x,y)-\hat f(x,y)\big]^2$.</span>"""
        r"""<span class="ln">It weights every pixel error equally, regardless of position or local structure,</span>"""
        r"""<span class="ln">so very different distortions (a shift, a blur, noise, a brightness change) can have the same MSE while looking very different to a viewer.</span>"""},
    3122: {"statement": r"""<b>Peak signal-to-noise ratio.</b>"""
        r"""<span class="ln in">$\mathrm{PSNR}=10\log_{10}\dfrac{\mathrm{MAX}^2}{\mathrm{MSE}}=20\log_{10}\dfrac{\mathrm{MAX}}{\sqrt{\mathrm{MSE}}}$ dB,</span>"""
        r"""<span class="ln">where MAX is the maximum possible pixel value ($255$ for 8-bit images, $1$ for floating point images in $[0,1]$).</span>"""
        r"""<span class="ln">A rise of 10 dB corresponds to MSE divided by 10.</span>"""},
    3123: {"statement": r"""<b>Structural similarity index.</b>"""
        r"""<span class="ln">For two image patches $f,g$</span>"""
        r"""<span class="ln">with local means $\mu_f,\mu_g$, variances $\sigma_f^2,\sigma_g^2$ and covariance $\sigma_{fg}$:</span>"""
        r"""<span class="ln in">$\mathrm{SSIM}(f,g)=\dfrac{(2\mu_f\mu_g+C_1)(2\sigma_{fg}+C_2)}{(\mu_f^2+\mu_g^2+C_1)(\sigma_f^2+\sigma_g^2+C_2)}$,</span>"""
        r"""<span class="ln">with $C_1=(0.01L)^2$, $C_2=(0.03L)^2$ for dynamic range $L$.</span>"""
        r"""<span class="ln">With $C_3=C_2/2$ it is the product of luminance, contrast and structure comparisons,</span>"""
        r"""<span class="ln in">lies in $[-1,1]$ and equals 1 only if $f=g$.</span>"""},
    3124: {"statement": r"""<b>SSIM map and mean SSIM.</b>"""
        r"""<span class="ln">Slide a window (typically an $11\times11$ Gaussian with $\sigma=1.5$) over the two images</span>"""
        r"""<span class="ln">and compute $\mathrm{SSIM}(f_j,g_j)$ at each of $W$ positions to form a quality map.</span>"""
        r"""<span class="ln in">The mean SSIM is $\mathrm{MSSIM}(f,g)=\frac1W\sum_{j=1}^{W}\mathrm{SSIM}(f_j,g_j)$.</span>"""
        r"""<span class="ln">Multi-scale SSIM (MS-SSIM) repeats the comparison over several downsampled scales.</span>"""},
    3125: {"statement": r"""<b>Classes of image quality assessment (IQA).</b>"""
        r"""<span class="ln">Full-reference (FR) methods compare a test image with its pristine original (MSE, PSNR, SSIM, MS-SSIM);</span>"""
        r"""<span class="ln">reduced-reference (RR) methods use only some features of the original;</span>"""
        r"""<span class="ln">no-reference (NR, blind) methods use the test image alone, with natural-scene statistics or learned features.</span>"""
        r"""<span class="ln">They are validated against subjective scores (mean opinion score, MOS)</span>"""
        r"""<span class="ln in">by rank correlation $\mathrm{SROCC}=1-\frac{6\sum\nolimits d_i^2}{n(n^2-1)}$</span>"""
        r"""<span class="ln in">and linear correlation (PLCC).</span>"""},
    3126: {"statement": r"""<b>Example.</b>"""
        r"""<span class="ln">For an 8-bit image, $\mathrm{MAX}=255$.</span>"""
        r"""<span class="ln">With $\mathrm{MSE}=100$ (an RMS error of $10$ grey levels),</span>"""
        r"""<span class="ln in">$\mathrm{PSNR}=10\log_{10}\dfrac{255^2}{100}=10\log_{10}(650.25)\approx28.13$ dB.</span>"""
        r"""<span class="ln">Likewise $\mathrm{MSE}=10\Rightarrow38.1$ dB, $\mathrm{MSE}=1\Rightarrow48.1$ dB, $\mathrm{MSE}=1000\Rightarrow18.1$ dB.</span>"""},
}
