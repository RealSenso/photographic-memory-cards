"""StoMA Topic 04 statements, line by line (one hypothesis or conclusion per line; the source on its own small line)."""

SUBJECT = "StoMA"

FIX = {
    30401: {"statement": r"""<b>CDF method.</b>"""
        r"""<span class="ln">Let $X$ be a random variable and $g:\mathbb R\to\mathbb R$ measurable, and put $Y=g(X)$.</span>"""
        r"""<span class="ln">Then</span>"""
        r"""<span class="ln in">$F_Y(y)=\mathbb P(g(X)\le y)=\mathbb P\bigl(X\in\{x:g(x)\le y\}\bigr)$,</span>"""
        r"""<span class="ln in">which equals $\int_{\{x:g(x)\le y\}}f_X(x)\,dx$ when $X$ has density $f_X$.</span>"""
        r"""<span class="ln">If $F_Y$ is differentiable,</span>"""
        r"""<span class="ln in">$f_Y(y)=\dfrac{d}{dy}F_Y(y)$ on the support of $Y$.</span>"""
        r"""<span class="src">Ross 5.7; Grimmett 4.7</span>"""},
    30402: {"statement": r"""<b>Monotone change of variables.</b>"""
        r"""<span class="ln">If $g$ is strictly monotone and differentiable on the support of $X$,</span>"""
        r"""<span class="ln">then $Y=g(X)$ has density</span>"""
        r"""<span class="ln in">$f_Y(y)=f_X(g^{-1}(y))\left|\frac{d}{dy}g^{-1}(y)\right|$</span>"""
        r"""<span class="ln in">for $y\in g(\operatorname{supp}X)$.</span>"""
        r"""<span class="src">Ross 5.7; Grimmett 4.7</span>"""},
    30403: {"statement": r"""<b>Many-to-one transformations.</b>"""
        r"""<span class="ln">Let $g$ be piecewise strictly monotone and differentiable,</span>"""
        r"""<span class="ln">and let $y$ have preimages $x_1,\ldots,x_m$ with $g'(x_k)\ne0$.</span>"""
        r"""<span class="ln">Then</span>"""
        r"""<span class="ln in">$f_Y(y)=\sum_{k}\dfrac{f_X(x_k)}{|g'(x_k)|}$.</span>"""
        r"""<span class="ln">In particular for $Y=X^2$,</span>"""
        r"""<span class="ln in">$f_Y(y)=\dfrac{f_X(\sqrt y)+f_X(-\sqrt y)}{2\sqrt y}\,\mathbf 1_{\{y\gt 0\}}$.</span>"""
        r"""<span class="src">Ross 5.7; Grimmett 4.7</span>"""},
    30404: {"statement": r"""<b>Probability integral transform.</b>"""
        r"""<span class="ln">If $X$ has a continuous CDF $F_X$,</span>"""
        r"""<span class="ln in">then $U=F_X(X)\sim\text{Uniform}(0,1)$.</span>"""
        r"""<span class="ln">Conversely, if $U\sim\text{Uniform}(0,1)$ and $F$ is any CDF with generalised inverse</span>"""
        r"""<span class="ln in">$F^{-1}(u)=\inf\{x:F(x)\ge u\}$,</span>"""
        r"""<span class="ln in">then $X=F^{-1}(U)$ has CDF $F$.</span>"""
        r"""<span class="src">Ross 5.7; Grimmett 4.11</span>"""},
    30405: {"statement": r"""<b>Chi-square with one degree of freedom.</b>"""
        r"""<span class="ln">If $Z\sim\mathcal N(0,1)$ then $Y=Z^2$ has density</span>"""
        r"""<span class="ln in">$f_Y(y)=\dfrac1{\sqrt{2\pi y}}e^{-y/2}\mathbf 1_{\{y\gt 0\}}$,</span>"""
        r"""<span class="ln in">that is $Y\sim\chi^2_1=\mathrm{Gamma}\bigl(\tfrac12,\tfrac12\bigr)$.</span>"""
        r"""<span class="ln">Proof: $F_Y(y)=\mathbb P(-\sqrt y\le Z\le\sqrt y)=2\Phi(\sqrt y)-1$ for $y\gt 0$;</span>"""
        r"""<span class="ln in">differentiate.</span>"""
        r"""<span class="src">Ross 5.7; Grimmett 4.4</span>"""},
    30406: {"statement": r"""<b>Cauchy law from a random angle.</b>"""
        r"""<span class="ln">If $\Theta\sim\text{Uniform}(-\pi/2,\pi/2)$ and $X=\tan\Theta$, then</span>"""
        r"""<span class="ln in">$F_X(x)=\mathbb P(\Theta\le\arctan x)=\tfrac12+\tfrac1\pi\arctan x$</span>"""
        r"""<span class="ln in">and $f_X(x)=\dfrac1{\pi(1+x^2)}$, the standard Cauchy density.</span>"""
        r"""<span class="ln">Its tails are so heavy that $\int|x|f_X(x)\,dx=\infty$,</span>"""
        r"""<span class="ln in">so $\mathbb E[X]$ does not exist.</span>"""
        r"""<span class="src">Ross 5.7; Grimmett 4.4</span>"""},
}
