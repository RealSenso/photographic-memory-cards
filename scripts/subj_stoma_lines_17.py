"""StoMA Topic 17 statements, line by line (one hypothesis or conclusion per line; the source on its own small line)."""

SUBJECT = "StoMA"

FIX = {
    31701: {"statement": r"""<b>Weak law of large numbers.</b>"""
        r"""<span class="ln">Let $X_1,X_2,\ldots$ be i.i.d. with mean $\mu$ and finite variance $\sigma^2$.</span>"""
        r"""<span class="ln in">Then $\bar X_n=\frac1n\sum_{i=1}^nX_i\xrightarrow{P}\mu$;</span>"""
        r"""<span class="ln in">indeed $\mathbb P(|\bar X_n-\mu|\ge\varepsilon)\le\dfrac{\sigma^2}{n\varepsilon^2}$.</span>"""
        r"""<span class="src">Ross 8.2; Grimmett 7.4</span>"""},
    31702: {"statement": r"""<b>Strong law of large numbers.</b>"""
        r"""<span class="ln">Let $X_1,X_2,\ldots$ be i.i.d.</span>"""
        r"""<span class="ln in">Then $\mathbb P\bigl(\lim_n\frac1n\sum_{i=1}^nX_i=\mu\bigr)=1$</span>"""
        r"""<span class="ln in">if and only if $\mathbb E|X|\lt \infty$,</span>"""
        r"""<span class="ln in">in which case $\mu=\mathbb E[X]$.</span>"""
        r"""<span class="src">Kolmogorov; Grimmett 7.5; Durrett 2.4</span>"""},
    31703: {"statement": r"""<b>Strong law under a fourth moment.</b>"""
        r"""<span class="ln">If $X_i$ are i.i.d. with $\mathbb E[X^4]\lt \infty$,</span>"""
        r"""<span class="ln in">then $\mathbb E[(\bar X_n-\mu)^4]\le C/n^2$,</span>"""
        r"""<span class="ln in">so $\sum_n\mathbb P(|\bar X_n-\mu|\ge\varepsilon)\le\sum_n\frac{C}{n^2\varepsilon^4}\lt \infty$,</span>"""
        r"""<span class="ln in">and by the first Borel–Cantelli lemma $\bar X_n\to\mu$ almost surely.</span>"""
        r"""<span class="src">Grimmett 7.5; Durrett 2.4</span>"""},
    31704: {"statement": r"""<b>Kolmogorov's SLLN and truncation.</b>"""
        r"""<span class="ln">$\bar X_n\to\mu$ a.s. iff $\mathbb E|X|\lt \infty$.</span>"""
        r"""<span class="ln">Sketch: put $Y_n=X_n\mathbf 1_{\{|X_n|\le n\}}$.</span>"""
        r"""<span class="ln in">Then $\sum_n\mathbb P(X_n\ne Y_n)=\sum_n\mathbb P(|X|\gt n)\le\mathbb E|X|\lt \infty$,</span>"""
        r"""<span class="ln in">so $X_n=Y_n$ eventually (Borel–Cantelli),</span>"""
        r"""<span class="ln in">and the truncated variables have bounded variance sums.</span>"""
        r"""<span class="src">Grimmett 7.5; Durrett 2.4</span>"""},
    31705: {"statement": r"""<b>WLLN versus SLLN.</b>"""
        r"""<span class="ln">The WLLN says $\mathbb P(|\bar X_n-\mu|\ge\varepsilon)\to0$ for each fixed $\varepsilon$</span>"""
        r"""<span class="ln in">(a statement about the law at each time $n$).</span>"""
        r"""<span class="ln">The SLLN says $\mathbb P\bigl(\bigcup_{k\ge n}\{|\bar X_k-\mu|\ge\varepsilon\}\bigr)\to0$ as $n\to\infty$</span>"""
        r"""<span class="ln in">(a statement about the whole path after $n$).</span>"""
        r"""<span class="src">Grimmett 7.2, 7.5</span>"""},
    31706: {"statement": r"""<b>Failure for the Cauchy law.</b>"""
        r"""<span class="ln">If $X_i$ are i.i.d. standard Cauchy, $\varphi_X(t)=e^{-|t|}$,</span>"""
        r"""<span class="ln in">so $\varphi_{\bar X_n}(t)=\bigl[e^{-|t|/n}\bigr]^n=e^{-|t|}$</span>"""
        r"""<span class="ln in">and $\bar X_n\overset d=X_1$ for every $n$.</span>"""
        r"""<span class="ln">Hence $\bar X_n$ does not converge to a constant:</span>"""
        r"""<span class="ln in">the laws of large numbers fail since $\mathbb E|X|=\infty$.</span>"""
        r"""<span class="src">Grimmett 5.10</span>"""},
}
