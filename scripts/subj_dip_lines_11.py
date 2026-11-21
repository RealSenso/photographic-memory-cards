"""DIP Topic 11 statements, line by line (one setup, item or conclusion per line)."""

SUBJECT = "DIP"

FIX = {
    3101: {"statement": r"""<b>Image degradation model.</b>"""
        r"""<span class="ln">The observed image is $g(x,y)=(h\ast f)(x,y)+\eta(x,y)$,</span>"""
        r"""<span class="ln in">where $f$ is the true image, $h$ the point spread function of a linear shift-invariant degradation and $\eta$ additive noise.</span>"""
        r"""<span class="ln">In the frequency domain $G(u,v)=H(u,v)F(u,v)+N(u,v)$.</span>"""
        r"""<span class="ln">Restoration seeks an estimate $\hat F=W\,G$ of $F$ using a model of $h$ and $\eta$.</span>"""},
    3102: {"statement": r"""<b>Inverse filtering.</b>"""
        r"""<span class="ln">Given $G=HF+N$,</span>"""
        r"""<span class="ln in">the inverse filter estimate is $\hat F(u,v)=\dfrac{G(u,v)}{H(u,v)}=F(u,v)+\dfrac{N(u,v)}{H(u,v)}$.</span>"""
        r"""<span class="ln">Where $H(u,v)\to0$ (typically at high frequencies, and exactly zero for some blurs)</span>"""
        r"""<span class="ln in">the term $N/H$ is arbitrarily large, so the estimate is dominated by amplified noise.</span>"""
        r"""<span class="ln">The remedy is to restrict the division to frequencies where $|H|$ is large, or to use Wiener or regularized filters.</span>"""},
    3103: {"statement": r"""<b>Wiener filter.</b>"""
        r"""<span class="ln">For $g=h\ast f+\eta$ with $f,\eta$ zero-mean, uncorrelated and wide-sense stationary with power spectra $S_f,S_\eta$,</span>"""
        r"""<span class="ln">the linear filter minimizing $\mathbb E\|f-\hat f\|^2$ is</span>"""
        r"""<span class="ln in">$W(u,v)=\dfrac{H^*(u,v)}{|H(u,v)|^2+S_\eta(u,v)/S_f(u,v)}$,</span>"""
        r"""<span class="ln in">with $\hat F=W\,G$.</span>"""
        r"""<span class="ln">In practice $S_\eta/S_f$ is replaced by a constant $K$ chosen by eye:</span>"""
        r"""<span class="ln in">$K=0$ gives the inverse filter.</span>"""},
    3104: {"statement": r"""<b>Constrained least-squares (CLS) restoration.</b>"""
        r"""<span class="ln">Minimize the roughness $\|Pf\|^2$ ($P$ the Laplacian operator)</span>"""
        r"""<span class="ln in">subject to $\|g-Hf\|^2=\|\eta\|^2$.</span>"""
        r"""<span class="ln">The solution in the frequency domain is</span>"""
        r"""<span class="ln in">$\hat F(u,v)=\dfrac{H^*(u,v)}{|H(u,v)|^2+\gamma\,|P(u,v)|^2}\,G(u,v)$,</span>"""
        r"""<span class="ln">where the Lagrange parameter $\gamma$ is adjusted iteratively until $\|g-H\hat f\|^2\approx\|\eta\|^2$ (or chosen at the corner of the L-curve).</span>"""},
    3105: {"statement": r"""<b>Motion-blur transfer function.</b>"""
        r"""<span class="ln">For uniform linear motion with displacement $aT$ during the exposure,</span>"""
        r"""<span class="ln in">$H(u)=\dfrac{\sin(\pi u aT)}{\pi u a}\,e^{-j\pi uaT}$,</span>"""
        r"""<span class="ln in">which is zero at $u=\dfrac{k}{aT}$, $k=1,2,\dots$.</span>"""
        r"""<span class="ln">Defocus gives a pillbox (disk) PSF;</span>"""
        r"""<span class="ln">Gaussian and turbulence blurs give a Gaussian $H$ with no exact zeros.</span>"""
        r"""<span class="ln">$H$ may be found by observing a point source or sharp edge, by experiment or by modelling;</span>"""
        r"""<span class="ln in">blind deconvolution estimates it from $g$ alone.</span>"""},
    3106: {"statement": r"""<b>Example.</b>"""
        r"""<span class="ln">Take $K=S_\eta/S_f=0.05$ and real $H$.</span>"""
        r"""<span class="ln">At a weak frequency $H=0.1$</span>"""
        r"""<span class="ln in">the inverse filter has gain $1/H=10$ (noise power $\times100$)</span>"""
        r"""<span class="ln in">while the Wiener gain is $W=\dfrac{0.1}{0.1^2+0.05}=1.67$.</span>"""
        r"""<span class="ln">At a strong frequency $H=1$</span>"""
        r"""<span class="ln in">the inverse gain is $1$</span>"""
        r"""<span class="ln in">and $W=\dfrac1{1+0.05}\approx0.952$.</span>"""},
}
