"""StoMA Topic 12 statements, line by line (one hypothesis or conclusion per line; the source on its own small line)."""

SUBJECT = "StoMA"

FIX = {
    31201: {"statement": r"""<b>Conditional expectation as best guess.</b>"""
        r"""<span class="ln">If $\mathbb E[Y^2]\lt \infty$,</span>"""
        r"""<span class="ln in">then $\hat Y=\mathbb E[Y\mid X]$ is the unique (a.s.) function of $X$ minimising $\mathbb E[(Y-g(X))^2]$</span>"""
        r"""<span class="ln in2">over all $g$ with $\mathbb E[g(X)^2]\lt \infty$,</span>"""
        r"""<span class="ln in">and $\mathbb E[\mathbb E[Y\mid X]]=\mathbb E[Y]$.</span>"""
        r"""<span class="src">Ross 7.5; Grimmett 3.7, 7.9</span>"""},
    31202: {"statement": r"""<b>Orthogonality in $L^2$.</b>"""
        r"""<span class="ln">For $\mathbb E[Y^2]\lt \infty$,</span>"""
        r"""<span class="ln in">$\hat Y=\mathbb E[Y\mid X]$ is the orthogonal projection of $Y$ onto $L^2(\sigma(X))$:</span>"""
        r"""<span class="ln in">$\mathbb E\bigl[(Y-\mathbb E[Y\mid X])h(X)\bigr]=0$</span>"""
        r"""<span class="ln in2">for all $h$ with $\mathbb E[h(X)^2]\lt \infty$.</span>"""
        r"""<span class="src">Grimmett 7.9</span>"""},
    31203: {"statement": r"""<b>Tower property and taking out what is known.</b>"""
        r"""<span class="ln">For $\sigma$-algebras $\mathcal G\subset\mathcal H$:</span>"""
        r"""<span class="ln in">$\mathbb E[\mathbb E[Y\mid\mathcal H]\mid\mathcal G]=\mathbb E[Y\mid\mathcal G]$,</span>"""
        r"""<span class="ln in">in particular $\mathbb E[\mathbb E[Y\mid X_1,X_2]\mid X_1]=\mathbb E[Y\mid X_1]$.</span>"""
        r"""<span class="ln">Also $\mathbb E[g(X)Y\mid X]=g(X)\,\mathbb E[Y\mid X]$.</span>"""
        r"""<span class="src">Ross 7.5; Grimmett 3.7</span>"""},
    31204: {"statement": r"""<b>Law of total variance.</b>"""
        r"""<span class="ln">If $\mathbb E[Y^2]\lt \infty$,</span>"""
        r"""<span class="ln in">$\operatorname{Var}(Y)=\mathbb E[\operatorname{Var}(Y\mid X)]+\operatorname{Var}(\mathbb E[Y\mid X])$.</span>"""
        r"""<span class="ln">Hence the minimum mean squared error of estimating $Y$ from $X$ is $\mathbb E[\operatorname{Var}(Y\mid X)]$.</span>"""
        r"""<span class="src">Ross 7.5; Grimmett 3.7</span>"""},
    31205: {"statement": r"""<b>MMSE versus LLSE.</b>"""
        r"""<span class="ln">For $\mathbb E[Y^2]\lt \infty$,</span>"""
        r"""<span class="ln in">$\mathbb E[(Y-\mathbb E[Y\mid X])^2]\le\mathbb E[(Y-\hat Y_{\rm LLSE})^2]\le\operatorname{Var}(Y)$,</span>"""
        r"""<span class="ln in">since the linear estimators are a subset of all functions of $X$ and constants are a subset of linear ones.</span>"""
        r"""<span class="ln">They coincide iff $\mathbb E[Y\mid X]$ is affine in $X$,</span>"""
        r"""<span class="ln in">e.g. jointly Gaussian $(X,Y)$.</span>"""
        r"""<span class="src">Grimmett 7.9</span>"""},
    31206: {"statement": r"""<b>Poisson thinning via Eve's law.</b>"""
        r"""<span class="ln">Let $N\sim\mathrm{Poisson}(\lambda)$ and, given $N$, $K\sim\mathrm{Bin}(N,p)$.</span>"""
        r"""<span class="ln in">Then $\mathbb E[K]=\mathbb E[Np]=\lambda p$</span>"""
        r"""<span class="ln in">and $\operatorname{Var}(K)=\mathbb E[Np(1-p)]+\operatorname{Var}(Np)=\lambda p(1-p)+\lambda p^2=\lambda p$.</span>"""
        r"""<span class="ln">In fact $K\sim\mathrm{Poisson}(\lambda p)$.</span>"""
        r"""<span class="src">Ross 7.5</span>"""},
}
