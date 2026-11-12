"""StoMA Topic 18 statements, line by line (one hypothesis or conclusion per line; the source on its own small line)."""

SUBJECT = "StoMA"

FIX = {
    31801: {"statement": r"""<b>Characteristic function.</b>"""
        r"""<span class="ln">For a random variable $X$, $\varphi_X(t)=\mathbb E[e^{itX}]$, $t\in\mathbb R$.</span>"""
        r"""<span class="ln in">It exists for every $X$, $|\varphi_X(t)|\le1$, $\varphi_X(0)=1$,</span>"""
        r"""<span class="ln in">$\varphi_{aX+b}(t)=e^{itb}\varphi_X(at)$,</span>"""
        r"""<span class="ln in">and it determines the law of $X$;</span>"""
        r"""<span class="ln">for independent $X,Y$, $\varphi_{X+Y}=\varphi_X\varphi_Y$.</span>"""
        r"""<span class="src">Grimmett 5.7; Durrett 3.3</span>"""},
    31802: {"statement": r"""<b>Lévy's continuity theorem.</b>"""
        r"""<span class="ln">$X_n\xrightarrow{d}X$ if and only if $\varphi_{X_n}(t)\to\varphi_X(t)$ for every $t\in\mathbb R$.</span>"""
        r"""<span class="ln">More generally, if $\varphi_{X_n}(t)\to\varphi(t)$ pointwise and $\varphi$ is continuous at $0$,</span>"""
        r"""<span class="ln in">then $\varphi$ is the characteristic function of some $X$</span>"""
        r"""<span class="ln in">and $X_n\xrightarrow{d}X$.</span>"""
        r"""<span class="src">Grimmett 5.9; Durrett 3.3</span>"""},
    31803: {"statement": r"""<b>Central limit theorem (Lindeberg–Lévy).</b>"""
        r"""<span class="ln">Let $X_1,X_2,\ldots$ be i.i.d. with mean $\mu$ and variance $\sigma^2\in(0,\infty)$.</span>"""
        r"""<span class="ln in">Then $Z_n=\dfrac{\sum_{i=1}^nX_i-n\mu}{\sigma\sqrt n}\xrightarrow{d}\mathcal N(0,1)$.</span>"""
        r"""<span class="ln">Proof: $\varphi_{Z_n}(t)=\bigl(1-\frac{t^2}{2n}+o(\frac{t^2}n)\bigr)^n\to e^{-t^2/2}$,</span>"""
        r"""<span class="ln in">then Lévy.</span>"""
        r"""<span class="src">Ross 8.3; Grimmett 5.10</span>"""},
    31804: {"statement": r"""<b>Berry–Esseen theorem.</b>"""
        r"""<span class="ln">For i.i.d. $X_i$ with $\mathbb E|X-\mu|^3\lt \infty$,</span>"""
        r"""<span class="ln in">$\sup_x|F_{Z_n}(x)-\Phi(x)|\le\dfrac{C\,\mathbb E|X-\mu|^3}{\sigma^3\sqrt n}$</span>"""
        r"""<span class="ln in">with $C\le0.4748$.</span>"""
        r"""<span class="ln">For integer-valued sums, the continuity correction</span>"""
        r"""<span class="ln in">$\mathbb P(S_n\le k)\approx\Phi\!\left(\frac{k+\frac12-n\mu}{\sigma\sqrt n}\right)$</span>"""
        r"""<span class="ln in">is more accurate.</span>"""
        r"""<span class="src">Grimmett 5.10; Ross 8.3</span>"""},
    31805: {"statement": r"""<b>Lyapunov and Lindeberg CLT.</b>"""
        r"""<span class="ln">Let $X_i$ be independent with means $\mu_i$, variances $\sigma_i^2$ and $s_n^2=\sum_{i\le n}\sigma_i^2$.</span>"""
        r"""<span class="ln">If for some $\delta\gt 0$ (Lyapunov)</span>"""
        r"""<span class="ln in">$\frac1{s_n^{2+\delta}}\sum_{i\le n}\mathbb E|X_i-\mu_i|^{2+\delta}\to0$,</span>"""
        r"""<span class="ln in">then $\frac1{s_n}\sum_{i\le n}(X_i-\mu_i)\xrightarrow{d}\mathcal N(0,1)$.</span>"""
        r"""<span class="ln">Lindeberg's condition</span>"""
        r"""<span class="ln in">$\frac1{s_n^2}\sum\mathbb E[(X_i-\mu_i)^2\mathbf 1_{\{|X_i-\mu_i|\gt \varepsilon s_n\}}]\to0$</span>"""
        r"""<span class="ln in">is weaker and, with $\max_i\sigma_i/s_n\to0$, necessary.</span>"""
        r"""<span class="src">Grimmett 5.10; Durrett 3.4</span>"""},
    31806: {"statement": r"""<b>De Moivre–Laplace.</b>"""
        r"""<span class="ln">Let $S_{100}$ be the number of heads in $100$ fair tosses, so $\mu=50$, $\sigma=5$.</span>"""
        r"""<span class="ln">With the continuity correction,</span>"""
        r"""<span class="ln in">$\mathbb P(45\le S_{100}\le55)\approx\Phi\!\left(\frac{55.5-50}{5}\right)-\Phi\!\left(\frac{44.5-50}{5}\right)$</span>"""
        r"""<span class="ln in">$=2\Phi(1.1)-1\approx0.7286$.</span>"""
        r"""<span class="src">Ross 8.3; Grimmett 5.10</span>"""},
}
