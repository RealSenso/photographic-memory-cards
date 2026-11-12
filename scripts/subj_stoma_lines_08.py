"""StoMA Topic 08 statements, line by line (one hypothesis or conclusion per line; the source on its own small line)."""

SUBJECT = "StoMA"

FIX = {
    30801: {"statement": r"""<b>Distribution of the extremes.</b>"""
        r"""<span class="ln">Let $X_1,\ldots,X_n$ be i.i.d. with CDF $F$ and density $f$,</span>"""
        r"""<span class="ln">and let $X_{(1)}\le\cdots\le X_{(n)}$ be their order statistics.</span>"""
        r"""<span class="ln in">Then $F_{X_{(n)}}(x)=[F(x)]^n$ and $F_{X_{(1)}}(x)=1-[1-F(x)]^n$,</span>"""
        r"""<span class="ln in">so $f_{X_{(n)}}(x)=n[F(x)]^{n-1}f(x)$ and $f_{X_{(1)}}(x)=n[1-F(x)]^{n-1}f(x)$.</span>"""
        r"""<span class="src">Ross 6.6; Grimmett 4.14</span>"""},
    30802: {"statement": r"""<b>Density of the $k$-th order statistic.</b>"""
        r"""<span class="ln">For i.i.d. $X_1,\ldots,X_n$ with CDF $F$ and density $f$,</span>"""
        r"""<span class="ln in">$f_{X_{(k)}}(x)=\dfrac{n!}{(k-1)!\,(n-k)!}[F(x)]^{k-1}[1-F(x)]^{n-k}f(x)=k\binom nk[F(x)]^{k-1}[1-F(x)]^{n-k}f(x)$.</span>"""
        r"""<span class="src">Ross 6.6; Grimmett 4.14</span>"""},
    30803: {"statement": r"""<b>Joint density of order statistics.</b>"""
        r"""<span class="ln">For i.i.d. $X_i$ with density $f$, $(X_{(1)},\ldots,X_{(n)})$ has density</span>"""
        r"""<span class="ln in">$n!\prod_{i=1}^nf(x_i)\mathbf 1_{\{x_1\lt \cdots\lt x_n\}}$.</span>"""
        r"""<span class="src">Ross 6.6; Grimmett 4.14</span>"""},
    30804: {"statement": r"""<b>Uniform order statistics.</b>"""
        r"""<span class="ln">If $U_i$ are i.i.d. $\text{Uniform}(0,1)$, then</span>"""
        r"""<span class="ln in">$U_{(k)}\sim\mathrm{Beta}(k,n-k+1)$ with $\mathbb E[U_{(k)}]=\frac{k}{n+1}$.</span>"""
        r"""<span class="ln">The $n+1$ spacings are identically distributed, each of mean $\frac1{n+1}$.</span>"""
        r"""<span class="src">Ross 6.6; Grimmett 4.14</span>"""},
    30805: {"statement": r"""<b>Spacings of exponential order statistics.</b>"""
        r"""<span class="ln">Let $X_1,\ldots,X_n$ be i.i.d. $\mathrm{Exp}(\lambda)$ with $X_{(0)}=0$.</span>"""
        r"""<span class="ln">Then the spacings $W_k=X_{(k)}-X_{(k-1)}$, $k=1,\ldots,n$,</span>"""
        r"""<span class="ln in">are independent with $W_k\sim\mathrm{Exp}\bigl((n-k+1)\lambda\bigr)$.</span>"""
        r"""<span class="ln">Hence $\mathbb E[X_{(n)}]=\dfrac1\lambda\sum_{j=1}^n\dfrac1j$.</span>"""
        r"""<span class="src">Ross 6.6; Grimmett 4.14</span>"""},
    30806: {"statement": r"""<b>Minimum of independent exponentials.</b>"""
        r"""<span class="ln">If $T_1,\ldots,T_n$ are independent with $T_i\sim\mathrm{Exp}(\lambda_i)$, then</span>"""
        r"""<span class="ln in">$T=\min_iT_i\sim\mathrm{Exp}\!\left(\sum_i\lambda_i\right)$, since $\mathbb P(T\gt t)=\prod_ie^{-\lambda_it}$,</span>"""
        r"""<span class="ln in">and $\mathbb P(T_k=\min_iT_i)=\dfrac{\lambda_k}{\sum_i\lambda_i}$.</span>"""
        r"""<span class="ln">A series system of components with these lifetimes fails at time $T$.</span>"""
        r"""<span class="src">Ross 5.5, 6.6</span>"""},
}
