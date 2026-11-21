"""DIP Topic 08 statements, line by line (one setup, item or conclusion per line)."""

SUBJECT = "DIP"

FIX = {
    3071: {"statement": r"""<b>Spectrum of a sampled signal.</b>"""
        r"""<span class="ln">If $f_\Delta(x)=f(x)\sum_{n}\delta(x-n\Delta)$ is the ideal sampling of $f$ with spacing $\Delta$,</span>"""
        r"""<span class="ln in">then $F_\Delta(u)=\frac1\Delta\sum_{k=-\infty}^{\infty}F\!\big(u-\frac k\Delta\big)$:</span>"""
        r"""<span class="ln">the spectrum of the sampled signal consists of copies of $F$ centred at the multiples of the sampling frequency $1/\Delta$.</span>"""},
    3072: {"statement": r"""<b>Sampling theorem (Shannon–Nyquist).</b>"""
        r"""<span class="ln">If $f$ is bandlimited, $F(u)=0$ for $|u|\gt u_{\max}$,</span>"""
        r"""<span class="ln">and it is sampled with spacing $\Delta$ such that $f_s=1/\Delta\gt 2u_{\max}$,</span>"""
        r"""<span class="ln in">then $f$ is recovered exactly from its samples: $f(x)=\sum_n f(n\Delta)\,\operatorname{sinc}\!\big(\frac{x-n\Delta}{\Delta}\big)$.</span>"""
        r"""<span class="ln">If $f_s\lt2u_{\max}$ the replicas overlap and aliasing occurs.</span>"""
        r"""<span class="ln">At $f_s=2u_{\max}$ recovery still holds unless $F$ has an impulse at $\pm u_{\max}$.</span>"""},
    3073: {"statement": r"""<b>Aliasing.</b>"""
        r"""<span class="ln">A sinusoid of frequency $u_0\gt f_s/2$ sampled at rate $f_s$</span>"""
        r"""<span class="ln in">gives the same samples as a sinusoid of frequency $u_{\rm alias}=|u_0-k f_s|$,</span>"""
        r"""<span class="ln in">where $k$ is the integer for which $u_{\rm alias}\in[0,f_s/2]$ (the nearest multiple of $f_s$, $k=\operatorname{round}(u_0/f_s)$).</span>"""
        r"""<span class="ln">The effect cannot be undone after sampling; it is prevented by low-pass filtering before sampling.</span>"""},
    3074: {"statement": r"""<b>Downsampling (decimation) by $M$.</b>"""
        r"""<span class="ln">$g[n]=f[Mn]$.</span>"""
        r"""<span class="ln">Its spectrum is</span>"""
        r"""<span class="ln in">$G(\omega)=\frac1M\sum_{k=0}^{M-1}F\!\big(\frac{\omega-2\pi k}{M}\big)$:</span>"""
        r"""<span class="ln">the spectrum is stretched by $M$ and $M$ shifted copies are added, so content above $\pi/M$ aliases.</span>"""
        r"""<span class="ln">Decimation therefore applies a low-pass filter with cutoff $\pi/M$ before discarding samples.</span>"""},
    3075: {"statement": r"""<b>Upsampling (interpolation) by $L$.</b>"""
        r"""<span class="ln">The expander is</span>"""
        r"""<span class="ln in">$f_e[n]=f[n/L]$ if $L\mid n$ and $0$ otherwise,</span>"""
        r"""<span class="ln in">with $F_e(\omega)=F(L\omega)$ (the spectrum is compressed by $L$ and $L$ copies appear in $[0,2\pi)$, of which $L-1$ are images).</span>"""
        r"""<span class="ln">An interpolation low-pass filter with cutoff $\pi/L$ and gain $L$ removes the images and fills the zeros.</span>"""
        r"""<span class="ln">Resampling by a rational factor $L/M$ is upsampling by $L$, one low-pass with cutoff $\min(\pi/L,\pi/M)$ and gain $L$, then downsampling by $M$.</span>"""},
    3076: {"statement": r"""<b>Example.</b>"""
        r"""<span class="ln">A $90$ Hz cosine sampled at $f_s=100$ Hz exceeds the Nyquist frequency $f_s/2=50$ Hz.</span>"""
        r"""<span class="ln">With $k=\operatorname{round}(90/100)=1$,</span>"""
        r"""<span class="ln in">$u_{\rm alias}=|90-100|=10$ Hz,</span>"""
        r"""<span class="ln in">and $\cos(2\pi\cdot90\,\tfrac n{100})=\cos(2\pi\cdot10\,\tfrac n{100})$ for every integer $n$.</span>"""
        r"""<span class="ln">Likewise a grating of $0.8$ cycles/pixel aliases to $|0.8-1|=0.2$ cycles/pixel.</span>"""},
}
