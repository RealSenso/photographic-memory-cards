"""DIP Topic 14 (edge detection) statements, line by line. After this file exists, change a statement only here."""

SUBJECT = "DIP"

FIX = {
    3131: {"statement": r"""<b>Image gradient.</b>"""
        r"""<span class="ln">For an image $f(x,y)$ the gradient is $\nabla f=\begin{pmatrix}\partial f/\partial x\\ \partial f/\partial y\end{pmatrix}$.</span>"""
        r"""<span class="ln">It points in the direction of steepest increase;</span>"""
        r"""<span class="ln in">its magnitude $M=\lvert\nabla f\rvert=\sqrt{f_x^2+f_y^2}$ (often approximated by $|f_x|+|f_y|$) measures edge strength,</span>"""
        r"""<span class="ln in">and its direction $\theta=\operatorname{atan2}(f_y,f_x)$ is perpendicular to the edge.</span>"""},
    3132: {"statement": r"""<b>Sobel operator.</b>"""
        r"""<span class="ln">The Sobel kernels</span>"""
        r"""<span class="ln in">$S_x=\begin{pmatrix}1\\2\\1\end{pmatrix}\begin{pmatrix}-1&0&1\end{pmatrix}=\begin{pmatrix}-1&0&1\\-2&0&2\\-1&0&1\end{pmatrix}$</span>"""
        r"""<span class="ln">and $S_y=S_x^{\top}$, slid over the image as masks (correlation), estimate the partial derivatives $f_x,f_y$;</span>"""
        r"""<span class="ln">$S_x$ responds to vertical edges and $S_y$ to horizontal ones.</span>"""
        r"""<span class="ln in">The edge magnitude is $M=\sqrt{f_x^2+f_y^2}$.</span>"""
        r"""<span class="ln">Each kernel is a smoothing $[1,2,1]$ times a derivative $[-1,0,1]$, so noise is averaged along the edge.</span>"""},
    3133: {"statement": r"""<b>Marr–Hildreth (Laplacian of Gaussian) edge detector.</b>"""
        r"""<span class="ln">Edges are the zero-crossings of the second derivative of the smoothed image.</span>"""
        r"""<span class="ln">Convolve with</span>"""
        r"""<span class="ln in">$\nabla^2G_\sigma(x,y)=\frac1{\pi\sigma^4}\Big(\frac{x^2+y^2}{2\sigma^2}-1\Big)e^{-\frac{x^2+y^2}{2\sigma^2}}$ (since $f\ast\nabla^2G_\sigma=\nabla^2(G_\sigma\ast f)$),</span>"""
        r"""<span class="ln">and mark the points where the result changes sign, with a slope or magnitude test to discard weak ones.</span>"""
        r"""<span class="ln">$\sigma$ sets the scale of the edges found.</span>"""},
    3134: {"statement": r"""<b>Difference of Gaussians approximates the Laplacian of Gaussian.</b>"""
        r"""<span class="ln">Since $\partial G_\sigma/\partial\sigma=\sigma\nabla^2G_\sigma$, a finite difference in scale gives</span>"""
        r"""<span class="ln in">$G_{k\sigma}(x,y)-G_\sigma(x,y)\approx(k-1)\,\sigma^2\,\nabla^2G_\sigma(x,y)$.</span>"""
        r"""<span class="ln">A ratio $k\approx1.6$ resembles the centre-surround response of the retina,</span>"""
        r"""<span class="ln">and the same construction is used by SIFT to find scale-space extrema.</span>"""},
    3135: {"statement": r"""<b>Canny edge detector.</b>"""
        r"""<span class="ln">Designed for good detection, good localization and a single response per edge:</span>"""
        r"""<span class="ln in">(1) smooth with a Gaussian;</span>"""
        r"""<span class="ln in">(2) compute the gradient magnitude $M$ and direction $\theta$;</span>"""
        r"""<span class="ln in">(3) non-maximum suppression:</span>"""
        r"""<span class="ln in2">quantize $\theta$ to $0^\circ,45^\circ,90^\circ,135^\circ$ and keep $(x,y)$ only if $M(x,y)$ is at least its two neighbours along $\theta$;</span>"""
        r"""<span class="ln in">(4) hysteresis thresholding with $T_{\rm high}\approx2$–$3\,T_{\rm low}$:</span>"""
        r"""<span class="ln in2">pixels $\ge T_{\rm high}$ are edges,</span>"""
        r"""<span class="ln in2">pixels in $[T_{\rm low},T_{\rm high})$ are kept only if 8-connected to an edge.</span>"""},
    3136: {"statement": r"""<b>Example.</b>"""
        r"""<span class="ln">Gradient magnitudes along an edge are $20,45,95,40,25,60,28$ with $T_{\rm high}=90$ and $T_{\rm low}=30$.</span>"""
        r"""<span class="ln">Only $95\ge T_{\rm high}$ is a strong seed.</span>"""
        r"""<span class="ln">Its neighbours $45$ and $40$ are $\ge T_{\rm low}$ and connected to it, so they are kept:</span>"""
        r"""<span class="ln in">edges $=\{45,95,40\}$.</span>"""
        r"""<span class="ln">The $60$ is above $T_{\rm low}$ but is separated from the chain by $25\lt T_{\rm low}$, so it is dropped;</span>"""
        r"""<span class="ln">$20,25,28$ are below $T_{\rm low}$.</span>"""},
}
