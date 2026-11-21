"""DIP Topic 10 statements, line by line (one setup, item or conclusion per line)."""

SUBJECT = "DIP"

FIX = {
    3091: {"statement": r"""<b>Wavelet family and time-frequency tiling.</b>"""
        r"""<span class="ln">From a mother wavelet $\psi$ (of zero mean and finite energy) a wavelet family is formed by dilation and translation,</span>"""
        r"""<span class="ln in">$\psi_{j,k}(x)=2^{j/2}\psi(2^jx-k)$,</span>"""
        r"""<span class="ln">and the wavelet coefficients of $f$ are $c_{j,k}=\langle f,\psi_{j,k}\rangle$.</span>"""
        r"""<span class="ln">Unlike the short-time Fourier transform, which tiles the time-frequency plane with identical rectangles,</span>"""
        r"""<span class="ln in">the wavelet tiles are narrow in position and tall in frequency at high frequencies, and wide and short at low frequencies;</span>"""
        r"""<span class="ln in">every tile has the same area (Heisenberg).</span>"""},
    3092: {"statement": r"""<b>Multiresolution analysis (MRA).</b>"""
        r"""<span class="ln">A nested sequence of closed subspaces $\cdots\subset V_0\subset V_1\subset V_2\subset\cdots$ of $L^2$,</span>"""
        r"""<span class="ln in">where $V_j$ is spanned by integer shifts of $\varphi(2^jx)$ (the scaling function),</span>"""
        r"""<span class="ln in">with $\bigcap V_j=\{0\}$ and $\overline{\bigcup V_j}=L^2$.</span>"""
        r"""<span class="ln">The detail space $W_j$ is the orthogonal complement of $V_j$ in $V_{j+1}$,</span>"""
        r"""<span class="ln in">$V_{j+1}=V_j\oplus W_j$,</span>"""
        r"""<span class="ln in">spanned by the shifts of $\psi(2^jx)$;</span>"""
        r"""<span class="ln in">hence $f=\sum_k c_{J,k}\varphi_{J,k}+\sum_{j\ge J}\sum_k d_{j,k}\psi_{j,k}$.</span>"""},
    3093: {"statement": r"""<b>Two-channel perfect-reconstruction filter bank.</b>"""
        r"""<span class="ln">The analysis bank filters $f$ with a low-pass $h_0$ and a high-pass $h_1$ and downsamples each by 2;</span>"""
        r"""<span class="ln">the synthesis bank upsamples by 2, filters with $g_0,g_1$ and adds.</span>"""
        r"""<span class="ln">The output equals the input (up to delay) if and only if</span>"""
        r"""<span class="ln in">the aliasing term cancels, $G_0(z)H_0(-z)+G_1(z)H_1(-z)=0$,</span>"""
        r"""<span class="ln in">and the distortion term is a pure delay, $G_0(z)H_0(z)+G_1(z)H_1(z)=2z^{-l}$.</span>"""
        r"""<span class="ln">The Haar bank is $a[n]=\frac{f[2n]+f[2n+1]}{\sqrt2}$, $d[n]=\frac{f[2n]-f[2n+1]}{\sqrt2}$.</span>"""},
    3094: {"statement": r"""<b>2D discrete wavelet transform (pyramid).</b>"""
        r"""<span class="ln">Apply the 1D analysis filter bank along the rows and then along the columns of an $M\times N$ image.</span>"""
        r"""<span class="ln">This gives four subbands of size $\frac M2\times\frac N2$:</span>"""
        r"""<span class="ln in">$LL$ (low-low), $HL$, $LH$ and $HH$.</span>"""
        r"""<span class="ln">Repeat on the $LL$ band for $J$ levels;</span>"""
        r"""<span class="ln in">$LL_J$ has size $\frac M{2^J}\times\frac N{2^J}$,</span>"""
        r"""<span class="ln in">and the total number of coefficients stays $MN$ (critical sampling).</span>"""},
    3095: {"statement": r"""<b>Wavelet shrinkage denoising.</b>"""
        r"""<span class="ln">For noisy coefficients $c$ and a threshold $T$:</span>"""
        r"""<span class="ln in">hard thresholding $\hat c=c\,\mathbf 1_{|c|\gt T}$;</span>"""
        r"""<span class="ln in">soft thresholding $\hat c=\operatorname{sign}(c)\,(|c|-T)_+$.</span>"""
        r"""<span class="ln">The universal (VisuShrink) threshold is $T=\sigma_\eta\sqrt{2\ln N}$ for noise level $\sigma_\eta$,</span>"""
        r"""<span class="ln in">often estimated as $\sigma_\eta=\operatorname{median}(|d_1|)/0.6745$ from the finest detail band.</span>"""
        r"""<span class="ln">Only the detail bands are thresholded.</span>"""},
    3096: {"statement": r"""<b>Example.</b>"""
        r"""<span class="ln">Unnormalized Haar transform (average and half-difference) of $f=[4,6,10,12]$.</span>"""
        r"""<span class="ln in">Level 1: $(4,6)\to(5,-1)$, $(10,12)\to(11,-1)$, giving $[5,11\mid-1,-1]$.</span>"""
        r"""<span class="ln in">Level 2 on the averages $(5,11)\to(8,-3)$, giving $[8\mid-3\mid-1,-1]$.</span>"""
        r"""<span class="ln">Reconstruction:</span>"""
        r"""<span class="ln in">$5=8+(-3)$, $11=8-(-3)$,</span>"""
        r"""<span class="ln in">then $4=5+(-1)$, $6=5-(-1)$, $10=11+(-1)$, $12=11-(-1)$.</span>"""},
}
