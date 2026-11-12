"""StoMA Topic 06 statements, line by line (one hypothesis or conclusion per line; the source on its own small line)."""

SUBJECT = "StoMA"

FIX = {
    30601: {"statement": r"""<b>Markov's inequality.</b>"""
        r"""<span class="ln">If $X\ge0$ is a random variable with finite mean and $a\gt 0$,</span>"""
        r"""<span class="ln in">then $\mathbb P(X\ge a)\le\dfrac{\mathbb E[X]}{a}$.</span>"""
        r"""<span class="ln">Proof: $a\mathbf 1_{\{X\ge a\}}\le X$ pointwise; take expectations.</span>"""
        r"""<span class="ln">For general $X$, apply the bound to $|X|$, $(X-\mu)^2$ or $e^{tX}$.</span>"""
        r"""<span class="src">Ross 8.2; Grimmett 7.3</span>"""},
    30602: {"statement": r"""<b>Chebyshev's inequality.</b>"""
        r"""<span class="ln">If $X$ has finite mean $\mu$ and variance $\sigma^2$, then for every $\varepsilon\gt 0$,</span>"""
        r"""<span class="ln in">$\mathbb P(|X-\mu|\ge\varepsilon)\le\dfrac{\operatorname{Var}(X)}{\varepsilon^2}$.</span>"""
        r"""<span class="ln">Equivalently $\mathbb P(|X-\mu|\ge k\sigma)\le1/k^2$.</span>"""
        r"""<span class="ln">It is Markov's inequality applied to $(X-\mu)^2$.</span>"""
        r"""<span class="src">Ross 8.2; Grimmett 7.3</span>"""},
    30603: {"statement": r"""<b>Chernoff bound.</b>"""
        r"""<span class="ln">If $M_X(t)=\mathbb E[e^{tX}]$ is finite for some $t\gt 0$, then for every $a$,</span>"""
        r"""<span class="ln in">$\mathbb P(X\ge a)\le\inf_{t\gt 0}e^{-ta}M_X(t)=\exp\bigl(-\sup_{t\gt 0}[ta-\Lambda_X(t)]\bigr)$,</span>"""
        r"""<span class="ln in">where $\Lambda_X=\ln M_X$.</span>"""
        r"""<span class="ln">For the lower tail, use $t\lt 0$.</span>"""
        r"""<span class="src">Ross 8.3; Grimmett 5.11</span>"""},
    30604: {"statement": r"""<b>Jensen's inequality.</b>"""
        r"""<span class="ln">If $g$ is convex and $X$ and $g(X)$ are integrable,</span>"""
        r"""<span class="ln in">then $g(\mathbb E[X])\le\mathbb E[g(X)]$.</span>"""
        r"""<span class="ln">If $g$ is concave, $\mathbb E[g(X)]\le g(\mathbb E[X])$.</span>"""
        r"""<span class="ln">Equality holds for non-degenerate $X$ only if $g$ is affine on the support of $X$.</span>"""
        r"""<span class="ln">For $g=\ln$ this gives the AM–GM inequality.</span>"""
        r"""<span class="src">Ross 8.5; Grimmett 6.6</span>"""},
    30605: {"statement": r"""<b>Cauchy–Schwarz and Hoeffding.</b>"""
        r"""<span class="ln">For $X,Y$ with finite second moments,</span>"""
        r"""<span class="ln in">$|\mathbb E[XY]|^2\le\mathbb E[X^2]\,\mathbb E[Y^2]$.</span>"""
        r"""<span class="ln">If $X_1,\ldots,X_n$ are independent with $a_i\le X_i\le b_i$, then for $t\gt 0$,</span>"""
        r"""<span class="ln in">$\mathbb P\!\left(\sum_{i=1}^n(X_i-\mathbb EX_i)\ge t\right)\le\exp\!\left(-\dfrac{2t^2}{\sum_i(b_i-a_i)^2}\right)$.</span>"""
        r"""<span class="src">Ross 8.5; Grimmett 7.3, 12.2</span>"""},
    30606: {"statement": r"""<b>Chebyshev against Chernoff.</b>"""
        r"""<span class="ln">Let $S_n$ be the number of heads in $n$ tosses of a fair coin.</span>"""
        r"""<span class="ln">Chebyshev gives</span>"""
        r"""<span class="ln in">$\mathbb P(S_n\ge\tfrac34n)\le\mathbb P(|S_n-\tfrac n2|\ge\tfrac n4)\le\dfrac{n/4}{(n/4)^2}=\dfrac4n$.</span>"""
        r"""<span class="ln">Hoeffding (Chernoff) gives</span>"""
        r"""<span class="ln in">$\mathbb P(S_n\ge\tfrac34n)\le\exp\!\bigl(-\tfrac{2(n/4)^2}{n}\bigr)=e^{-n/8}$.</span>"""
        r"""<span class="ln">The second decays exponentially, the first only like $1/n$.</span>"""
        r"""<span class="src">Ross 8.2; Grimmett 7.3</span>"""},
}
