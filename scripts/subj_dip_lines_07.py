"""DIP Topic 07 statements, line by line (one setup, item or conclusion per line)."""

SUBJECT = "DIP"

FIX = {
    3061: {"statement": r"""<b>2D discrete Fourier transform.</b>"""
        r"""<span class="ln">For an $M\times N$ image $f(x,y)$,</span>"""
        r"""<span class="ln in">$F(u,v)=\sum_{x=0}^{M-1}\sum_{y=0}^{N-1}f(x,y)\,e^{-j2\pi(ux/M+vy/N)}$,</span>"""
        r"""<span class="ln">with inverse</span>"""
        r"""<span class="ln in">$f(x,y)=\frac1{MN}\sum_{u,v}F(u,v)\,e^{j2\pi(ux/M+vy/N)}$.</span>"""
        r"""<span class="ln">The kernel is separable, so $F$ is computed by 1D DFTs along the rows and then along the columns, and with the FFT in $O(MN\log MN)$ operations.</span>"""},
    3062: {"statement": r"""<b>Periodicity, symmetry and centring.</b>"""
        r"""<span class="ln">$F(u,v)$ is periodic:</span>"""
        r"""<span class="ln in">$F(u+M,v)=F(u,v+N)=F(u,v)$.</span>"""
        r"""<span class="ln">For real $f$,</span>"""
        r"""<span class="ln in">$F(u,v)=F^*(-u,-v)$, so $|F|$ is symmetric about the origin.</span>"""
        r"""<span class="ln">For even $M,N$,</span>"""
        r"""<span class="ln in">$\mathcal F\{f(x,y)(-1)^{x+y}\}=F(u-\tfrac M2,v-\tfrac N2)$, which moves the zero-frequency term to the centre of the array.</span>"""},
    3063: {"statement": r"""<b>Magnitude and phase.</b>"""
        r"""<span class="ln">Writing $F(u,v)=|F(u,v)|\,e^{j\angle F(u,v)}$,</span>"""
        r"""<span class="ln in">the magnitude gives the amplitude of each frequency component and the phase gives its alignment.</span>"""
        r"""<span class="ln">Reconstruction from the phase alone, $\mathcal F^{-1}\{e^{j\angle F}\}$, retains the edges and structure of $f$,</span>"""
        r"""<span class="ln">while reconstruction from the magnitude alone, $\mathcal F^{-1}\{|F|\}$, does not;</span>"""
        r"""<span class="ln">exchanging the phases of two images makes each result resemble the image that supplied the phase.</span>"""},
    3064: {"statement": r"""<b>Convolution theorem.</b>"""
        r"""<span class="ln">For the DFT,</span>"""
        r"""<span class="ln in">$\mathcal F\{f\circledast h\}=F(u,v)\,H(u,v)$,</span>"""
        r"""<span class="ln in">where $\circledast$ is circular convolution of period $(P,Q)$.</span>"""
        r"""<span class="ln">If $f$ has size $M$ and $h$ size $K$ (in each dimension) and both are zero-padded to $P\ge M+K-1$,</span>"""
        r"""<span class="ln in">then the circular convolution equals the linear convolution $f\ast h$.</span>"""},
    3065: {"statement": r"""<b>Central slice (projection-slice) theorem.</b>"""
        r"""<span class="ln">Let $p_\theta(t)=\int f(t\cos\theta-s\sin\theta,\ t\sin\theta+s\cos\theta)\,ds$</span>"""
        r"""<span class="ln in">be the projection of $f$ along rays perpendicular to the direction $\theta$ (the Radon transform).</span>"""
        r"""<span class="ln">Then $\int p_\theta(t)\,e^{-j2\pi\rho t}\,dt=F(\rho\cos\theta,\rho\sin\theta)$:</span>"""
        r"""<span class="ln in">the 1D Fourier transform of the projection is the slice of the 2D transform through the origin at angle $\theta$.</span>"""},
    3066: {"statement": r"""<b>Example.</b>"""
        r"""<span class="ln">For $f=\begin{pmatrix}1&2\\3&4\end{pmatrix}$ ($M=N=2$, $e^{-j\pi}=-1$):</span>"""
        r"""<span class="ln in">$F(u,v)=\sum_{x,y}f(x,y)(-1)^{ux+vy}$,</span>"""
        r"""<span class="ln in">giving $F=\begin{pmatrix}10&-2\\-4&0\end{pmatrix}$,</span>"""
        r"""<span class="ln">and the inverse $f(x,y)=\tfrac14\sum F(u,v)(-1)^{ux+vy}$ returns $f(0,0)=\tfrac14(10-2-4+0)=1$.</span>"""},
}
