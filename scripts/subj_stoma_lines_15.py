"""StoMA Topic 15 statements, line by line (one hypothesis or conclusion per line; the source on its own small line)."""

SUBJECT = "StoMA"

FIX = {
    31501: {"statement": r"""<b>Modes of convergence.</b>"""
        r"""<span class="ln">For random variables $X_n,X$: $X_n\to X$</span>"""
        r"""<span class="ln in">almost surely if $\mathbb P(X_n\to X)=1$;</span>"""
        r"""<span class="ln in">in probability if $\mathbb P(|X_n-X|\gt \varepsilon)\to0$ for all $\varepsilon\gt 0$;</span>"""
        r"""<span class="ln in">in $L^p$ if $\mathbb E|X_n-X|^p\to0$;</span>"""
        r"""<span class="ln in">in distribution if $F_{X_n}(x)\to F_X(x)$ at continuity points of $F_X$.</span>"""
        r"""<span class="ln">Then a.s. $\Rightarrow$ in probability $\Rightarrow$ in distribution,</span>"""
        r"""<span class="ln">and $L^p\Rightarrow L^r\Rightarrow$ in probability for $p\gt r\ge1$.</span>"""
        r"""<span class="src">Grimmett 7.2; Ross 8.2</span>"""},
    31502: {"statement": r"""<b>Partial converses.</b>"""
        r"""<span class="ln">(i) If $c$ is a constant, $X_n\xrightarrow{d}c$ iff $X_n\xrightarrow{P}c$.</span>"""
        r"""<span class="ln">(ii) If $X_n\xrightarrow{P}X$, there is a subsequence $n_k$ with $X_{n_k}\xrightarrow{a.s.}X$.</span>"""
        r"""<span class="ln">(iii) If $X_n\xrightarrow{P}X$ and $|X_n|\le Y$ with $\mathbb E[Y]\lt \infty$,</span>"""
        r"""<span class="ln in">then $X_n\xrightarrow{L^1}X$.</span>"""
        r"""<span class="src">Grimmett 7.3; Ross 8.2</span>"""},
    31503: {"statement": r"""<b>Sliding typewriter.</b>"""
        r"""<span class="ln">On $\Omega=[0,1]$ with Lebesgue measure,</span>"""
        r"""<span class="ln in">enumerate intervals of length $1/k$ sweeping $[0,1]$ for $k=1,2,\ldots$,</span>"""
        r"""<span class="ln in">and let $X_n=\mathbf 1_{I_n}$ for the $n$-th interval.</span>"""
        r"""<span class="ln">Then $\mathbb P(X_n=1)=1/k\to0$, so $X_n\xrightarrow{P}0$,</span>"""
        r"""<span class="ln">but each $\omega$ lies in infinitely many $I_n$, so $\limsup X_n(\omega)=1$ for all $\omega$:</span>"""
        r"""<span class="ln in">$X_n\not\to0$ a.s.</span>"""
        r"""<span class="src">Grimmett 7.2; Durrett 2.3</span>"""},
    31504: {"statement": r"""<b>Escaping spike.</b>"""
        r"""<span class="ln">On $[0,1]$ with Lebesgue measure let $X_n=n^2\mathbf 1_{(0,1/n)}$.</span>"""
        r"""<span class="ln">For each fixed $\omega$, $X_n(\omega)=0$ once $n\gt 1/\omega$,</span>"""
        r"""<span class="ln in">so $X_n\to0$ a.s.,</span>"""
        r"""<span class="ln">but $\mathbb E|X_n|=n^2\cdot\frac1n=n\to\infty$,</span>"""
        r"""<span class="ln in">so $X_n\not\to0$ in $L^1$.</span>"""
        r"""<span class="src">Grimmett 7.2; Durrett 2.3</span>"""},
    31505: {"statement": r"""<b>Slutsky's theorem.</b>"""
        r"""<span class="ln">If $X_n\xrightarrow{d}X$ and $Y_n\xrightarrow{P}c$ for a constant $c$, then</span>"""
        r"""<span class="ln in">$X_n+Y_n\xrightarrow{d}X+c$,</span>"""
        r"""<span class="ln in">$X_nY_n\xrightarrow{d}cX$,</span>"""
        r"""<span class="ln in">and $X_n/Y_n\xrightarrow{d}X/c$ if $c\ne0$.</span>"""
        r"""<span class="ln">The continuous mapping theorem: if $g$ is continuous a.e. under the law of $X$ and $X_n\xrightarrow{d}X$,</span>"""
        r"""<span class="ln in">then $g(X_n)\xrightarrow{d}g(X)$.</span>"""
        r"""<span class="src">Ross 8.3; Grimmett 7.2</span>"""},
    31506: {"statement": r"""<b>Asymptotic normality of the $t$-statistic.</b>"""
        r"""<span class="ln">For i.i.d. $X_i$ with mean $\mu$, variance $\sigma^2\in(0,\infty)$ and sample variance $S_n^2$:</span>"""
        r"""<span class="ln in">$\sqrt n(\bar X_n-\mu)/\sigma\xrightarrow{d}\mathcal N(0,1)$ (CLT)</span>"""
        r"""<span class="ln in">and $S_n/\sigma\xrightarrow{P}1$ (LLN),</span>"""
        r"""<span class="ln">so by Slutsky $T_n=\frac{\sqrt n(\bar X_n-\mu)}{S_n}\xrightarrow{d}\mathcal N(0,1)$.</span>"""
        r"""<span class="src">Grimmett 5.10</span>"""},
}
