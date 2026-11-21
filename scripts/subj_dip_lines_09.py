"""DIP Topic 09 statements, line by line (one setup, item or conclusion per line)."""

SUBJECT = "DIP"

FIX = {
    3081: {"statement": r"""<b>Discrete cosine transform (DCT-II).</b>"""
        r"""<span class="ln">For a block $f(0),\dots,f(N-1)$:</span>"""
        r"""<span class="ln in">$C(u)=\alpha(u)\sum_{x=0}^{N-1}f(x)\cos\!\Big[\frac{(2x+1)u\pi}{2N}\Big]$,</span>"""
        r"""<span class="ln in">with $\alpha(0)=\sqrt{1/N}$ and $\alpha(u)=\sqrt{2/N}$ for $u\gt0$.</span>"""
        r"""<span class="ln">It equals the DFT (up to a phase and scale) of the even, mirror-image extension of $f$,</span>"""
        r"""<span class="ln in">so its coefficients are real and there is no boundary discontinuity.</span>"""},
    3082: {"statement": r"""<b>JPEG transform coding.</b>"""
        r"""<span class="ln">Split the image into $8\times8$ blocks,</span>"""
        r"""<span class="ln in">take the 2D DCT $C(u,v)$ of each,</span>"""
        r"""<span class="ln in">quantize $\hat C(u,v)=\operatorname{round}\big[C(u,v)/Q(u,v)\big]$ with a table $Q$ whose entries grow with frequency,</span>"""
        r"""<span class="ln in">scan the coefficients in zig-zag order,</span>"""
        r"""<span class="ln in">and entropy-code the result (run-length for the zero runs, differential coding for DC).</span>"""
        r"""<span class="ln">The DCT is invertible; all loss comes from the rounding.</span>"""},
    3083: {"statement": r"""<b>2D DCT as a separable orthonormal transform.</b>"""
        r"""<span class="ln">The 2D DCT of an $N\times N$ block is</span>"""
        r"""<span class="ln in">$C(u,v)=\alpha(u)\alpha(v)\sum_{x,y}f(x,y)\cos\frac{(2x+1)u\pi}{2N}\cos\frac{(2y+1)v\pi}{2N}$.</span>"""
        r"""<span class="ln">In matrix form $C=AfA^{\top}$ with $A$ orthogonal ($AA^{\top}=I$),</span>"""
        r"""<span class="ln in">so $f=A^{\top}CA$ and $\sum f^2=\sum C^2$ (Parseval).</span>"""},
    3084: {"statement": r"""<b>Karhunen–Loève transform (KLT).</b>"""
        r"""<span class="ln">Let $x$ be a random vector with mean $\mu$ and covariance $C_x$,</span>"""
        r"""<span class="ln">and let $\varphi_i$ be orthonormal eigenvectors of $C_x$ with eigenvalues $\lambda_1\ge\lambda_2\ge\dots$.</span>"""
        r"""<span class="ln">The transform $y=\Phi^{\top}(x-\mu)$</span>"""
        r"""<span class="ln in">has the diagonal covariance $C_y=\Lambda=\operatorname{diag}(\lambda_i)$,</span>"""
        r"""<span class="ln">and among all orthonormal linear transforms,</span>"""
        r"""<span class="ln in">keeping the first $k$ coefficients gives the smallest mean-squared error $\sum_{i\gt k}\lambda_i$.</span>"""},
    3085: {"statement": r"""<b>DCT as an approximate KLT.</b>"""
        r"""<span class="ln">For a first-order Markov process with covariance $C=\big[\rho^{|i-j|}\big]$ and $\rho$ close to 1 (typical of natural images, $\rho\approx0.9$–$0.95$),</span>"""
        r"""<span class="ln in">the KLT basis is approximately the DCT basis: $\Phi_{\rm KLT}\approx A_{\rm DCT}$.</span>"""
        r"""<span class="ln">The DCT is therefore near-optimal for compaction while being data-independent and having a fast algorithm.</span>"""},
    3086: {"statement": r"""<b>Example.</b>"""
        r"""<span class="ln">For $C_x=\begin{pmatrix}2&1\\1&2\end{pmatrix}$:</span>"""
        r"""<span class="ln in">$\det(C_x-\lambda I)=(2-\lambda)^2-1=0$ gives $\lambda_1=3$, $\lambda_2=1$,</span>"""
        r"""<span class="ln in">with eigenvectors $\varphi_1=\tfrac1{\sqrt2}(1,1)$ and $\varphi_2=\tfrac1{\sqrt2}(1,-1)$.</span>"""
        r"""<span class="ln">So $y_1=\frac{x_1+x_2}{\sqrt2}$, $y_2=\frac{x_1-x_2}{\sqrt2}$,</span>"""
        r"""<span class="ln in">and the variance splits $2,2\to3,1$: $y_1$ carries $75\%$ of the total ($\lambda_1+\lambda_2=4=\operatorname{tr}C_x$).</span>"""},
}
