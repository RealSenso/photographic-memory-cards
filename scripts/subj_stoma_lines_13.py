"""StoMA Topic 13 statements, line by line (one hypothesis or conclusion per line; the source on its own small line)."""

SUBJECT = "StoMA"

FIX = {
    31301: {"statement": r"""<b>Multivariate normal density.</b>"""
        r"""<span class="ln">$X\in\mathbb R^n$ is $\mathcal N(\mu,\Sigma)$ with $\Sigma\succ0$ if it has density</span>"""
        r"""<span class="ln in">$f_X(x)=\dfrac{1}{(2\pi)^{n/2}|\Sigma|^{1/2}}\exp\!\left(-\tfrac12(x-\mu)^\top\Sigma^{-1}(x-\mu)\right)$.</span>"""
        r"""<span class="src">Ross 7.8; Grimmett 4.9</span>"""},
    31302: {"statement": r"""<b>Linear projections.</b>"""
        r"""<span class="ln">$X\sim\mathcal N(\mu,\Sigma)$ in $\mathbb R^n$</span>"""
        r"""<span class="ln in">if and only if for every $t\in\mathbb R^n$, $t^\top X\sim\mathcal N(t^\top\mu,\,t^\top\Sigma t)$.</span>"""
        r"""<span class="ln">Consequently, $AX+b\sim\mathcal N(A\mu+b,A\Sigma A^\top)$.</span>"""
        r"""<span class="src">Ross 7.8; Grimmett 4.9</span>"""},
    31303: {"statement": r"""<b>Uncorrelated implies independent (Gaussian case).</b>"""
        r"""<span class="ln">If $(X_1,\ldots,X_n)$ is jointly Gaussian,</span>"""
        r"""<span class="ln in">then $X_i,X_j$ with $\operatorname{Cov}(X_i,X_j)=0$ are independent;</span>"""
        r"""<span class="ln in">more generally, the vector splits into independent blocks iff the cross-covariances vanish,</span>"""
        r"""<span class="ln in">because the density factorises.</span>"""
        r"""<span class="src">Ross 7.8; Grimmett 4.9</span>"""},
    31304: {"statement": r"""<b>Gaussian conditioning.</b>"""
        r"""<span class="ln">If $(X_1,X_2)\sim\mathcal N(\mu,\Sigma)$ with $\Sigma_{22}\succ0$, then</span>"""
        r"""<span class="ln in">$X_1\mid X_2=x_2\sim\mathcal N\bigl(\mu_1+\Sigma_{12}\Sigma_{22}^{-1}(x_2-\mu_2),\ \Sigma_{11}-\Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21}\bigr)$.</span>"""
        r"""<span class="ln">So $\mathbb E[X_1\mid X_2]$ equals the LLSE: MMSE $=$ LLSE.</span>"""
        r"""<span class="src">Ross 7.8; Grimmett 4.9</span>"""},
    31305: {"statement": r"""<b>Reading moments from the exponent.</b>"""
        r"""<span class="ln">If $f(x,y)\propto\exp\!\bigl(-\tfrac12[x\ y]\,P\,[x\ y]^\top\bigr)$</span>"""
        r"""<span class="ln in">with $P=\begin{bmatrix}a&b\\b&c\end{bmatrix}\succ0$,</span>"""
        r"""<span class="ln">then $(X,Y)$ is centred Gaussian with</span>"""
        r"""<span class="ln in">$\Sigma=P^{-1}=\dfrac1{ac-b^2}\begin{bmatrix}c&-b\\-b&a\end{bmatrix}$,</span>"""
        r"""<span class="ln in">so $\operatorname{Var}X=\dfrac{c}{ac-b^2}$.</span>"""
        r"""<span class="src">Grimmett 4.9</span>"""},
    31306: {"statement": r"""<b>Normal marginals, not jointly normal.</b>"""
        r"""<span class="ln">Let $X\sim\mathcal N(0,1)$, $S=\pm1$ with probability $\tfrac12$ each, independent of $X$, and $Y=SX$.</span>"""
        r"""<span class="ln in">Then $Y\sim\mathcal N(0,1)$ and $\operatorname{Cov}(X,Y)=\mathbb E[S]\mathbb E[X^2]=0$,</span>"""
        r"""<span class="ln in">but $\mathbb P(X+Y=0)=\mathbb P(S=-1)=\tfrac12$,</span>"""
        r"""<span class="ln in2">so $X+Y$ is not normal (a normal law has no atoms):</span>"""
        r"""<span class="ln">$(X,Y)$ is not jointly Gaussian and $X,Y$ are dependent.</span>"""
        r"""<span class="src">Ross 7.8; Grimmett 4.9</span>"""},
}
