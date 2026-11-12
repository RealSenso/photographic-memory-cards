"""StoMA Topic 10 statements, line by line (one hypothesis or conclusion per line; the source on its own small line)."""

SUBJECT = "StoMA"

FIX = {
    31001: {"statement": r"""<b>Exchangeability.</b>"""
        r"""<span class="ln">Random variables $X_1,\ldots,X_n$ are exchangeable if</span>"""
        r"""<span class="ln in">$(X_1,\ldots,X_n)\overset d=(X_{\pi(1)},\ldots,X_{\pi(n)})$ for every permutation $\pi$ of $\{1,\ldots,n\}$.</span>"""
        r"""<span class="ln">An infinite sequence is exchangeable if every finite subsequence is.</span>"""
        r"""<span class="ln">Every i.i.d. sequence is exchangeable, but not conversely.</span>"""
        r"""<span class="src">Grimmett 7.2; Durrett 4.1</span>"""},
    31002: {"statement": r"""<b>Equal moments.</b>"""
        r"""<span class="ln">If $X_1,\ldots,X_n$ are exchangeable with finite second moments, then they have</span>"""
        r"""<span class="ln in">a common mean $\mu$ and variance $\sigma^2$,</span>"""
        r"""<span class="ln in">and a common covariance $\operatorname{Cov}(X_i,X_j)=\rho\sigma^2$ for all $i\ne j$.</span>"""
        r"""<span class="ln">The covariance matrix is</span>"""
        r"""<span class="ln in">$\Sigma=\sigma^2\bigl[(1-\rho)I+\rho\mathbf 1\mathbf 1^\top\bigr]$.</span>"""
        r"""<span class="src">Grimmett 7.2; Ross 7.4</span>"""},
    31003: {"statement": r"""<b>Correlation bound for finite exchangeable sequences.</b>"""
        r"""<span class="ln">If $X_1,\ldots,X_n$ are exchangeable with common variance $\sigma^2\gt 0$ and pairwise correlation $\rho$,</span>"""
        r"""<span class="ln in">then $\rho\ge-\dfrac1{n-1}$.</span>"""
        r"""<span class="ln">Proof:</span>"""
        r"""<span class="ln in">$0\le\operatorname{Var}\bigl(\sum_iX_i\bigr)=n\sigma^2+n(n-1)\rho\sigma^2=n\sigma^2\bigl[1+(n-1)\rho\bigr]$.</span>"""
        r"""<span class="src">Grimmett 7.2</span>"""},
    31004: {"statement": r"""<b>Infinite exchangeability forces non-negative correlation.</b>"""
        r"""<span class="ln">If $X_1,X_2,\ldots$ is an infinite exchangeable sequence with finite variance,</span>"""
        r"""<span class="ln in">then every pair has $\rho\ge0$.</span>"""
        r"""<span class="ln">Proof: each finite segment $X_1,\ldots,X_n$ is exchangeable,</span>"""
        r"""<span class="ln in">so $\rho\ge-\frac1{n-1}$ for all $n\ge2$,</span>"""
        r"""<span class="ln in">and letting $n\to\infty$ gives $\rho\ge0$.</span>"""
        r"""<span class="src">Grimmett 7.2</span>"""},
    31005: {"statement": r"""<b>de Finetti's theorem.</b>"""
        r"""<span class="ln">Let $X_1,X_2,\ldots\in\{0,1\}$ be an infinite exchangeable sequence.</span>"""
        r"""<span class="ln">Then there is a random variable $\Theta\in[0,1]$,</span>"""
        r"""<span class="ln in">$\Theta=\lim_n\frac1n\sum_{i\le n}X_i$ a.s., with law $F_\Theta$, such that</span>"""
        r"""<span class="ln in">$\mathbb P(X_1=x_1,\ldots,X_n=x_n)=\int_0^1\theta^{\sum x_i}(1-\theta)^{n-\sum x_i}\,dF_\Theta(\theta)$:</span>"""
        r"""<span class="ln">conditionally on $\Theta$, the $X_i$ are i.i.d. Bernoulli($\Theta$).</span>"""
        r"""<span class="src">Grimmett 7.2; Durrett 4.1</span>"""},
    31006: {"statement": r"""<b>Pólya's urn.</b>"""
        r"""<span class="ln">An urn has $w$ white and $b$ black balls;</span>"""
        r"""<span class="ln in">a ball is drawn and returned with $c$ more of its colour.</span>"""
        r"""<span class="ln">With $k=\sum x_i$ white draws,</span>"""
        r"""<span class="ln in">$\mathbb P(X_1=x_1,\ldots,X_n=x_n)=\frac{\prod_{j\lt k}(w+jc)\prod_{j\lt n-k}(b+jc)}{\prod_{j\lt n}(w+b+jc)}$,</span>"""
        r"""<span class="ln in">which depends only on $k$:</span>"""
        r"""<span class="ln">the draws are exchangeable, and $\Theta\sim\mathrm{Beta}(\frac wc,\frac bc)$.</span>"""
        r"""<span class="src">Ross 3.6; Grimmett 7.2</span>"""},
}
