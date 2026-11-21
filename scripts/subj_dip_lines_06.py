"""DIP Topic 06 statements, line by line (one setup, item or conclusion per line)."""

SUBJECT = "DIP"

FIX = {
    3051: {"statement": r"""<b>Convolution representation of an LSI system.</b>"""
        r"""<span class="ln">Let $\mathcal S$ be a linear, shift-invariant system and $h(x,y)=\mathcal S[\delta](x,y)$ its impulse response (point spread function).</span>"""
        r"""<span class="ln">Then for every input $f$ its output is</span>"""
        r"""<span class="ln in">$g(x,y)=\sum_m\sum_n f(m,n)\,h(x-m,\,y-n)=(f\ast h)(x,y)$.</span>"""},
    3052: {"statement": r"""<b>Convolution and correlation.</b>"""
        r"""<span class="ln">For sequences $f,h$:</span>"""
        r"""<span class="ln in">convolution $(f\ast h)(x)=\sum_m f(m)\,h(x-m)$ (the kernel is reflected, then slid),</span>"""
        r"""<span class="ln in">and cross-correlation $(f\star h)(x)=\sum_m f(m)\,h(m-x)$ in which the kernel is not flipped.</span>"""
        r"""<span class="ln">In 2D the reflection is by $180^\circ$.</span>"""
        r"""<span class="ln">They coincide when $h$ is symmetric.</span>"""},
    3053: {"statement": r"""<b>Separable kernels.</b>"""
        r"""<span class="ln">A 2D kernel $h$ is separable if $h(x,y)=h_1(x)\,h_2(y)$,</span>"""
        r"""<span class="ln in">i.e. the kernel matrix equals $\mathbf h_1\mathbf h_2^{\top}$ and has rank 1.</span>"""
        r"""<span class="ln">Then $f\ast h=(f\ast_y h_2)\ast_x h_1$:</span>"""
        r"""<span class="ln in">a convolution with a $K\times K$ kernel costs $2K$ multiplications per pixel instead of $K^2$.</span>"""
        r"""<span class="ln">The Gaussian $G_\sigma(x,y)=G_\sigma(x)G_\sigma(y)$ and the box are separable.</span>"""},
    3054: {"statement": r"""<b>Smoothing filters.</b>"""
        r"""<span class="ln">The $K\times K$ box (mean) filter replaces each pixel by the average of its neighbourhood;</span>"""
        r"""<span class="ln in">for independent zero-mean noise of variance $\sigma_\eta^2$ the variance of the output is $\sigma_\eta^2/K^2$.</span>"""
        r"""<span class="ln">The Gaussian filter has kernel</span>"""
        r"""<span class="ln in">$G_\sigma(x,y)=\frac{1}{2\pi\sigma^2}e^{-(x^2+y^2)/2\sigma^2}$, is separable, and its Fourier transform is also Gaussian.</span>"""},
    3055: {"statement": r"""<b>Unsharp masking and Laplacian sharpening.</b>"""
        r"""<span class="ln">Given an image $f$ and a blurred copy $\bar f$,</span>"""
        r"""<span class="ln in">the mask is $m=f-\bar f$</span>"""
        r"""<span class="ln in">and the sharpened image is $g=f+k\,m$ ($k=1$ unsharp masking, $k\gt1$ high-boost).</span>"""
        r"""<span class="ln">Laplacian sharpening:</span>"""
        r"""<span class="ln in">$g=f-c\,\nabla^2f$</span>"""
        r"""<span class="ln in">where $\nabla^2f=f_{xx}+f_{yy}$ and $c\gt0$ when the Laplacian kernel has a negative centre coefficient.</span>"""},
    3056: {"statement": r"""<b>Example.</b>"""
        r"""<span class="ln">Let $f=[1,2,3,4]$ and $h=[1,0,-1]$.</span>"""
        r"""<span class="ln in">The full convolution has length $M+K-1=6$: $f\ast h=[1,\,2,\,2,\,2,\,-3,\,-4]$.</span>"""
        r"""<span class="ln">Interior values equal $f(n)-f(n-2)$, a central difference equal to twice the ramp's unit slope;</span>"""
        r"""<span class="ln">the end values come from zero-padding.</span>"""
        r"""<span class="ln">Correlation gives the negative of every value.</span>"""},
}
