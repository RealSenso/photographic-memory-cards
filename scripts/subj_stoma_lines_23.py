"""StoMA Topic 23 statements, line by line (one hypothesis or conclusion per line; the source on its own small line)."""

SUBJECT = "StoMA"

FIX = {
    32301: {"statement": r"""<b>Strict-sense and wide-sense stationarity.</b>"""
        r"""<span class="ln">$X(t)$ is strict-sense stationary if</span>"""
        r"""<span class="ln in">$F_{X(t_1+\tau),\ldots,X(t_k+\tau)}=F_{X(t_1),\ldots,X(t_k)}$ for all $k,t_i,\tau$.</span>"""
        r"""<span class="ln">It is wide-sense stationary (WSS) if</span>"""
        r"""<span class="ln in">$\mathbb E[X(t)]=\mu$ is constant and</span>"""
        r"""<span class="ln in">$R_X(t,t+\tau)=\mathbb E[X(t)X(t+\tau)]=R_X(\tau)$ depends only on the lag.</span>"""
        r"""<span class="src">Papoulis 9; Grimmett 9.1</span>"""},
    32302: {"statement": r"""<b>Properties of the autocorrelation.</b>"""
        r"""<span class="ln">For a WSS process,</span>"""
        r"""<span class="ln in">$R_X(0)=\mathbb E[X^2(t)]\ge|R_X(\tau)|$ for all $\tau$,</span>"""
        r"""<span class="ln in">$R_X(-\tau)=R_X(\tau)$, and</span>"""
        r"""<span class="ln in">$R_X$ is non-negative definite: $\sum_{i,j}c_ic_jR_X(t_i-t_j)\ge0$ for all real $c_i$ and times $t_i$.</span>"""
        r"""<span class="src">Papoulis 9; Grimmett 9.1</span>"""},
    32303: {"statement": r"""<b>Wiener–Khinchin.</b>"""
        r"""<span class="ln">For a WSS process with integrable $R_X$, the power spectral density is the Fourier transform of the autocorrelation:</span>"""
        r"""<span class="ln in">$S_X(\omega)=\int_{-\infty}^{\infty}R_X(\tau)e^{-j\omega\tau}d\tau\ge0$, and</span>"""
        r"""<span class="ln in">$R_X(\tau)=\frac1{2\pi}\int_{-\infty}^{\infty}S_X(\omega)e^{j\omega\tau}d\omega$;</span>"""
        r"""<span class="ln">in particular $\mathbb E[X^2]=\frac1{2\pi}\int S_X\,d\omega$.</span>"""
        r"""<span class="src">Papoulis 10; Grimmett 9.3</span>"""},
    32304: {"statement": r"""<b>Random harmonic process.</b>"""
        r"""<span class="ln">Let $X(t)=A\cos(\omega_0t+\Theta)$ with $A$ independent of $\Theta$.</span>"""
        r"""<span class="ln in">Then $R_X(\tau)=\frac{\mathbb E[A^2]}2\cos(\omega_0\tau)$ and</span>"""
        r"""<span class="ln in">$\mathbb E[X(t)]=\mathbb E[A]\,\mathbb E[\cos(\omega_0t+\Theta)]=0$ for all $t$ iff $\Theta\sim\text{Uniform}(-\pi,\pi)$.</span>"""
        r"""<span class="ln">Then $S_X(\omega)=\frac{\pi\mathbb E[A^2]}2[\delta(\omega-\omega_0)+\delta(\omega+\omega_0)]$.</span>"""
        r"""<span class="src">Papoulis 9–10; Grimmett 9.3</span>"""},
    32305: {"statement": r"""<b>LTI filtering of a WSS process.</b>"""
        r"""<span class="ln">If $X(t)$ is WSS with spectrum $S_X$ and passes through a stable LTI system with impulse response $h$ and transfer function $H(\omega)$,</span>"""
        r"""<span class="ln in">then $Y=h*X$ is WSS with</span>"""
        r"""<span class="ln in2">$S_Y(\omega)=|H(\omega)|^2S_X(\omega)$,</span>"""
        r"""<span class="ln in2">$R_Y(\tau)=R_X(\tau)*h(\tau)*h(-\tau)$ and</span>"""
        r"""<span class="ln in2">$\mathbb E[Y^2(t)]=\frac1{2\pi}\int|H(\omega)|^2S_X(\omega)d\omega$.</span>"""
        r"""<span class="src">Papoulis 10; Grimmett 9.3</span>"""},
    32306: {"statement": r"""<b>Mean ergodicity (Slutsky).</b>"""
        r"""<span class="ln">For a WSS process with mean $\mu$ and covariance $C_X(\tau)$,</span>"""
        r"""<span class="ln in">$\hat\mu_T=\frac1{2T}\int_{-T}^TX(t)\,dt\to\mu$ in $L^2$</span>"""
        r"""<span class="ln in">if and only if $\lim_{T\to\infty}\frac1T\int_0^{2T}\bigl(1-\frac{\tau}{2T}\bigr)C_X(\tau)\,d\tau=0$.</span>"""
        r"""<span class="src">Papoulis 13; Grimmett 9.5</span>"""},
}
