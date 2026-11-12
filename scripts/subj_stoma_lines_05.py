"""StoMA Topic 05 statements, line by line (one hypothesis or conclusion per line; the source on its own small line)."""

SUBJECT = "StoMA"

FIX = {
    30501: {"statement": r"""<b>LOTUS and linearity of expectation.</b>"""
        r"""<span class="ln">If $X$ has density $f_X$ (or pmf $p_X$) and $\mathbb E|g(X)|\lt \infty$, then</span>"""
        r"""<span class="ln in">$\mathbb E[g(X)]=\int_{-\infty}^\infty g(x)f_X(x)\,dx$ (respectively $\sum_xg(x)p_X(x)$).</span>"""
        r"""<span class="ln">For random variables $X_1,\ldots,X_n$ with finite means and constants $c_i$,</span>"""
        r"""<span class="ln in">$\mathbb E\bigl[\sum_ic_iX_i\bigr]=\sum_ic_i\mathbb E[X_i]$,</span>"""
        r"""<span class="ln in">with no independence needed.</span>"""
        r"""<span class="src">Ross 4.4, 7.2; Grimmett 3.3</span>"""},
    30502: {"statement": r"""<b>Tail-sum formula.</b>"""
        r"""<span class="ln">If $X\ge0$ then</span>"""
        r"""<span class="ln in">$\mathbb E[X]=\int_0^\infty\mathbb P(X\gt t)\,dt$.</span>"""
        r"""<span class="ln">If $X$ takes values in $\{0,1,2,\ldots\}$ then</span>"""
        r"""<span class="ln in">$\mathbb E[X]=\sum_{k=1}^\infty\mathbb P(X\ge k)$.</span>"""
        r"""<span class="ln">For general $X$,</span>"""
        r"""<span class="ln in">$\mathbb E[X]=\int_0^\infty\mathbb P(X\gt t)\,dt-\int_{-\infty}^0\mathbb P(X\lt t)\,dt$.</span>"""
        r"""<span class="src">Ross 5.3; Grimmett 4.3</span>"""},
    30503: {"statement": r"""<b>Variance of a sum.</b>"""
        r"""<span class="ln">For $X_1,\ldots,X_n$ with finite second moments,</span>"""
        r"""<span class="ln in">$\operatorname{Var}(\sum_iX_i)=\sum_i\operatorname{Var}(X_i)+2\sum_{i\lt j}\operatorname{Cov}(X_i,X_j)$,</span>"""
        r"""<span class="ln">where $\operatorname{Cov}(X,Y)=\mathbb E[(X-\mathbb EX)(Y-\mathbb EY)]$.</span>"""
        r"""<span class="src">Ross 7.4; Grimmett 3.6</span>"""},
    30504: {"statement": r"""<b>Moment generating function.</b>"""
        r"""<span class="ln">The MGF of $X$ is $M_X(t)=\mathbb E[e^{tX}]$ for $t$ in an interval around $0$ where it is finite.</span>"""
        r"""<span class="ln">Then</span>"""
        r"""<span class="ln in">$M_X(t)=\sum_{k\ge0}\frac{t^k}{k!}\mathbb E[X^k]$,</span>"""
        r"""<span class="ln in">$M_X^{(k)}(0)=\mathbb E[X^k]$,</span>"""
        r"""<span class="ln in">and if $M_X$ is finite near $0$ it determines the law of $X$.</span>"""
        r"""<span class="ln">For independent $X,Y$: $M_{X+Y}(t)=M_X(t)M_Y(t)$.</span>"""
        r"""<span class="src">Ross 7.7; Grimmett 5.1</span>"""},
    30505: {"statement": r"""<b>Probability generating function.</b>"""
        r"""<span class="ln">For $X$ taking values in $\{0,1,2,\ldots\}$,</span>"""
        r"""<span class="ln in">$G_X(s)=\mathbb E[s^X]=\sum_{k\ge0}\mathbb P(X=k)s^k$ for $|s|\le1$.</span>"""
        r"""<span class="ln">Then $G_X(0)=\mathbb P(X=0)$, $G_X(1)=1$, $\mathbb E[X]=G_X'(1)$,</span>"""
        r"""<span class="ln">and for independent $X_i$ with $N$ independent of them,</span>"""
        r"""<span class="ln in">$G_{\sum_{i=1}^NX_i}(s)=G_N\bigl(G_X(s)\bigr)$.</span>"""
        r"""<span class="src">Ross 7.7; Grimmett 5.1</span>"""},
    30506: {"statement": r"""<b>Uncorrelated but dependent.</b>"""
        r"""<span class="ln">Let $X$ be symmetric about $0$ with finite third moment (say uniform on $\{-1,0,1\}$) and $Y=X^2$.</span>"""
        r"""<span class="ln">Then $\mathbb E[X]=\mathbb E[X^3]=0$, so</span>"""
        r"""<span class="ln in">$\operatorname{Cov}(X,Y)=\mathbb E[X^3]-\mathbb E[X]\mathbb E[X^2]=0$,</span>"""
        r"""<span class="ln in">yet $Y$ is a function of $X$.</span>"""
        r"""<span class="ln">For $X$ uniform on $\{-1,0,1\}$:</span>"""
        r"""<span class="ln in">$\mathbb P(X=0,Y=1)=0\ne\tfrac13\cdot\tfrac23=\mathbb P(X=0)\mathbb P(Y=1)$,</span>"""
        r"""<span class="ln in">so $X,Y$ are not independent.</span>"""
        r"""<span class="src">Ross 7.4; Grimmett 3.6</span>"""},
}
