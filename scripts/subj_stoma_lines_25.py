"""StoMA Topic 25 statements, line by line (one hypothesis or conclusion per line; the source on its own small line)."""

SUBJECT = "StoMA"

FIX = {
    32501: {"statement": r"""<b>Pólya's recurrence theorem.</b>"""
        r"""<span class="ln">The simple symmetric random walk on $\mathbb Z^d$ satisfies</span>"""
        r"""<span class="ln in">$\sum_{n\ge1}P^{(2n)}_{00}=\infty$ iff $d\in\{1,2\}$, in which case it is recurrent.</span>"""
        r"""<span class="ln">For $d\ge3$, $P^{(2n)}_{00}\asymp n^{-d/2}$ is summable ($\sum n^{-d/2}\lt \infty$)</span>"""
        r"""<span class="ln in">and the walk is transient.</span>"""
        r"""<span class="src">Grimmett 5.10; Ross 4.3</span>"""},
    32502: {"statement": r"""<b>Standard Brownian motion.</b>"""
        r"""<span class="ln">$B(0)=0$;</span>"""
        r"""<span class="ln">independent increments;</span>"""
        r"""<span class="ln">$B(t)-B(s)\sim\mathcal N(0,t-s)$ for $s\lt t$;</span>"""
        r"""<span class="ln">continuous paths.</span>"""
        r"""<span class="ln">Donsker's theorem: for a simple random walk $S_n$,</span>"""
        r"""<span class="ln in">$\frac{S_{\lfloor nt\rfloor}}{\sqrt n}\xrightarrow{d}B(t)$ as a process.</span>"""
        r"""<span class="ln">Paths are nowhere differentiable:</span>"""
        r"""<span class="ln in">$\operatorname{Var}\bigl(\frac{\Delta B}{\Delta t}\bigr)=\frac1{\Delta t}\to\infty$.</span>"""
        r"""<span class="src">Ross 10.1; Durrett 8</span>"""},
    32503: {"statement": r"""<b>Brownian covariance and scaling.</b>"""
        r"""<span class="ln">$\operatorname{Cov}(B(t),B(s))=\min(t,s)$.</span>"""
        r"""<span class="ln">For every $c\gt 0$, $B(ct)\overset d=\sqrt c\,B(t)$ (self-similarity),</span>"""
        r"""<span class="ln">and $tB(1/t)\overset d=B(t)$ (time inversion, with value $0$ at $t=0$).</span>"""
        r"""<span class="src">Ross 10.1; Durrett 8</span>"""},
    32504: {"statement": r"""<b>Quadratic variation and Itô's rule.</b>"""
        r"""<span class="ln">For partitions $\Pi$ of $[0,t]$,</span>"""
        r"""<span class="ln in">$\lim_{\|\Pi\|\to0}\sum_i\bigl(B(t_i)-B(t_{i-1})\bigr)^2=t$ in $L^2$, i.e. $[B]_t=t$.</span>"""
        r"""<span class="ln">Formally $(dB)^2=dt$ and $dB\,dt=0$, which gives Itô's formula</span>"""
        r"""<span class="ln in">$df(B)=f'(B)dB+\frac12f''(B)dt$.</span>"""
        r"""<span class="src">Øksendal 4; Durrett 8</span>"""},
    32505: {"statement": r"""<b>Reflection principle.</b>"""
        r"""<span class="ln">Let $M(t)=\max_{s\le t}B(s)$ and $\tau_a=\inf\{t:B(t)=a\}$, $a\gt 0$.</span>"""
        r"""<span class="ln in">Then $\mathbb P(M(t)\ge a)=\mathbb P(\tau_a\le t)=2\mathbb P(B(t)\ge a)=2\bigl(1-\Phi(a/\sqrt t)\bigr)$,</span>"""
        r"""<span class="ln in">and $\tau_a$ has density $f_{\tau_a}(t)=\frac{a}{\sqrt{2\pi t^3}}e^{-a^2/(2t)}$.</span>"""
        r"""<span class="src">Ross 10.2; Durrett 8</span>"""},
    32506: {"statement": r"""<b>Gaussian-process regression.</b>"""
        r"""<span class="ln">Place a Gaussian-process prior with kernel $K(x,x')=\sigma_f^2e^{-\|x-x'\|^2/(2\ell^2)}$ on $f$</span>"""
        r"""<span class="ln">and observe $y=f(X)+\varepsilon$, $\varepsilon\sim\mathcal N(0,\sigma^2I)$.</span>"""
        r"""<span class="ln in">The posterior at $x_*$ is Gaussian with</span>"""
        r"""<span class="ln in2">$\mu_*=K_*^{\top}(K+\sigma^2I)^{-1}y$ and</span>"""
        r"""<span class="ln in2">$\Sigma_*=K_{**}-K_*^{\top}(K+\sigma^2I)^{-1}K_*$.</span>"""
        r"""<span class="src">Rasmussen–Williams 2</span>"""},
}
