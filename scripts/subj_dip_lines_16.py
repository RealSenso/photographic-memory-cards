"""DIP Topic 16 (corners and Harris) statements, line by line. After this file exists, change a statement only here."""

SUBJECT = "DIP"

FIX = {
    3151: {"statement": r"""<b>Window-shift energy.</b>"""
        r"""<span class="ln">For a window function $w$ and a shift $(u,v)$,</span>"""
        r"""<span class="ln in">$E(u,v)=\sum_{x,y}w(x,y)\,\big[f(x+u,y+v)-f(x,y)\big]^2$</span>"""
        r"""<span class="ln">measures how much the image patch changes when the window moves by $(u,v)$.</span>"""
        r"""<span class="ln in">In a flat region $E\approx0$ for all shifts;</span>"""
        r"""<span class="ln in">at an edge $E$ is large across the edge and $\approx0$ along it (aperture problem);</span>"""
        r"""<span class="ln in">at a corner $E$ is large for every direction of shift.</span>"""},
    3152: {"statement": r"""<b>Structure tensor.</b>"""
        r"""<span class="ln">By a first-order Taylor expansion,</span>"""
        r"""<span class="ln in">$E(u,v)\approx\begin{pmatrix}u&v\end{pmatrix}M\begin{pmatrix}u\\v\end{pmatrix}$</span>"""
        r"""<span class="ln">with the structure tensor</span>"""
        r"""<span class="ln in">$M=\sum_{x,y}w(x,y)\begin{pmatrix}f_x^2&f_xf_y\\f_xf_y&f_y^2\end{pmatrix}$.</span>"""
        r"""<span class="ln">The level sets of $E$ are ellipses with axes proportional to $1/\sqrt{\lambda_{1,2}}$,</span>"""
        r"""<span class="ln">where $\lambda_1,\lambda_2$ are the eigenvalues of $M$.</span>"""
        r"""<span class="ln in">Both small: flat;</span>"""
        r"""<span class="ln in">one large and one small: edge;</span>"""
        r"""<span class="ln in">both large: corner.</span>"""},
    3153: {"statement": r"""<b>Harris corner response.</b>"""
        r"""<span class="ln in">$R=\det M-k\,(\operatorname{tr}M)^2=\lambda_1\lambda_2-k(\lambda_1+\lambda_2)^2$,</span>"""
        r"""<span class="ln">with $k\approx0.04$–$0.06$.</span>"""
        r"""<span class="ln in">$R\gg0$ indicates a corner,</span>"""
        r"""<span class="ln in">$R\lt0$ an edge,</span>"""
        r"""<span class="ln in">and $|R|\approx0$ a flat region.</span>"""
        r"""<span class="ln">The Shi–Tomasi detector instead uses $\min(\lambda_1,\lambda_2)$ and thresholds it.</span>"""},
    3154: {"statement": r"""<b>Harris corner detector.</b>"""
        r"""<span class="ln in">(1) Compute the image derivatives $f_x,f_y$.</span>"""
        r"""<span class="ln in">(2) Form $f_x^2$, $f_xf_y$, $f_y^2$ at every pixel.</span>"""
        r"""<span class="ln in">(3) Smooth each with a Gaussian window $G_\sigma$ to get $M(x,y)=G_\sigma\ast\begin{pmatrix}f_x^2&f_xf_y\\f_xf_y&f_y^2\end{pmatrix}$.</span>"""
        r"""<span class="ln in">(4) Compute $R=\det M-k(\operatorname{tr}M)^2$.</span>"""
        r"""<span class="ln in">(5) Keep pixels with $R\gt\tau$ that are local maxima in a $3\times3$ neighbourhood.</span>"""},
    3155: {"statement": r"""<b>Invariance of the Harris response.</b>"""
        r"""<span class="ln">$R$ is invariant to rotation (the eigenvalues of $M$ do not change when the image is rotated)</span>"""
        r"""<span class="ln">and to an additive intensity change $f\to f+b$ (only derivatives enter);</span>"""
        r"""<span class="ln">under $f\to af$ it scales as $R\to a^4R$, so thresholds must be relative.</span>"""
        r"""<span class="ln">It is not invariant to scale: a corner seen at one scale can look like an edge at a larger one.</span>"""},
    3156: {"statement": r"""<b>Example.</b>"""
        r"""<span class="ln">With $k=0.05$:</span>"""
        r"""<span class="ln in">a corner window with $M=\operatorname{diag}(10,10)$ has $\det M=100$, $\operatorname{tr}M=20$ and $R=100-0.05\cdot400=80$.</span>"""
        r"""<span class="ln in">An edge window with $M=\operatorname{diag}(10,0)$ has $\det M=0$, $\operatorname{tr}M=10$ and $R=0-0.05\cdot100=-5$.</span>"""
        r"""<span class="ln in">A flat window with $M=0$ has $R=0$.</span>"""},
}
