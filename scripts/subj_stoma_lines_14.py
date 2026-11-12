"""StoMA Topic 14 statements, line by line (one hypothesis or conclusion per line; the source on its own small line)."""

SUBJECT = "StoMA"

FIX = {
    31401: {"statement": r"""<b>Random sums.</b>"""
        r"""<span class="ln">Let $X_1,X_2,\ldots$ be i.i.d. and $N\ge0$ integer-valued.</span>"""
        r"""<span class="ln">The random sum is</span>"""
        r"""<span class="ln in">$S_N=\sum_{i=1}^NX_i=\sum_{i=1}^\infty X_i\mathbf 1_{\{N\ge i\}}$.</span>"""
        r"""<span class="ln">If $N$ is a stopping time ($\{N\ge i\}\in\sigma(X_1,\ldots,X_{i-1})$) or independent of $(X_i)$,</span>"""
        r"""<span class="ln in">then $\mathbf 1_{\{N\ge i\}}$ is independent of $X_i$.</span>"""
        r"""<span class="src">Ross 7.5; Grimmett 5.1</span>"""},
    31402: {"statement": r"""<b>Wald's first identity.</b>"""
        r"""<span class="ln">Let $X_1,X_2,\ldots$ be i.i.d. with $\mathbb E|X|\lt \infty$</span>"""
        r"""<span class="ln">and $N$ a stopping time with $\mathbb E[N]\lt \infty$.</span>"""
        r"""<span class="ln in">Then $\mathbb E\bigl[\sum_{i=1}^NX_i\bigr]=\mathbb E[N]\,\mathbb E[X]$.</span>"""
        r"""<span class="src">Ross 7.5; Grimmett 12.5</span>"""},
    31403: {"statement": r"""<b>Wald's second identity.</b>"""
        r"""<span class="ln">If $N$ is independent of the i.i.d. $X_i$ with finite second moments, then</span>"""
        r"""<span class="ln in">$\operatorname{Var}\bigl(\sum_{i=1}^NX_i\bigr)=\mathbb E[N]\operatorname{Var}(X)+(\mathbb E[X])^2\operatorname{Var}(N)$.</span>"""
        r"""<span class="src">Ross 7.5; Grimmett 3.7</span>"""},
    31404: {"statement": r"""<b>Compound generating functions.</b>"""
        r"""<span class="ln">If $N$ is independent of the i.i.d. $X_i$,</span>"""
        r"""<span class="ln in">then $M_{S_N}(t)=G_N\bigl(M_X(t)\bigr)$,</span>"""
        r"""<span class="ln in">and for $X_i\in\{0,1,2,\ldots\}$, $G_{S_N}(s)=G_N\bigl(G_X(s)\bigr)$.</span>"""
        r"""<span class="src">Ross 7.7; Grimmett 5.1</span>"""},
    31405: {"statement": r"""<b>Galton–Watson process.</b>"""
        r"""<span class="ln">Let $Z_0=1$ and $Z_{n+1}=\sum_{i=1}^{Z_n}\xi_{n,i}$</span>"""
        r"""<span class="ln in">with i.i.d. offspring counts $\xi$, mean $\mu$ and PGF $G$.</span>"""
        r"""<span class="ln">Then $\mathbb E[Z_n]=\mu^n$,</span>"""
        r"""<span class="ln">and the extinction probability $\pi_0=\mathbb P(Z_n=0\text{ for some }n)$</span>"""
        r"""<span class="ln in">is the smallest root of $s=G(s)$ in $[0,1]$;</span>"""
        r"""<span class="ln in">$\pi_0=1$ iff $\mu\le1$ (excluding $\xi\equiv1$).</span>"""
        r"""<span class="src">Ross 4.7; Grimmett 5.4</span>"""},
    31406: {"statement": r"""<b>Compound Poisson (Lundberg) model.</b>"""
        r"""<span class="ln">Let $N\sim\mathrm{Poisson}(\lambda)$ be independent of i.i.d. $X_i$ (for example $X_i\sim\mathrm{Exp}(\beta)$)</span>"""
        r"""<span class="ln">and $S=\sum_{i=1}^NX_i$.</span>"""
        r"""<span class="ln in">Then $\mathbb E[S]=\lambda\,\mathbb E[X]$</span>"""
        r"""<span class="ln in">and $\operatorname{Var}(S)=\lambda\,\mathbb E[X^2]$,</span>"""
        r"""<span class="ln in2">which equals $\dfrac{2\lambda}{\beta^2}$ for exponential claims.</span>"""
        r"""<span class="src">Ross 7.5; Grimmett 6.8</span>"""},
}
