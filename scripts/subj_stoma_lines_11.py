"""StoMA Topic 11 statements, line by line (one hypothesis or conclusion per line; the source on its own small line)."""

SUBJECT = "StoMA"

FIX = {
    31101: {"statement": r"""<b>Covariance matrix.</b>"""
        r"""<span class="ln">For a random vector $X$ with mean $\mu$,</span>"""
        r"""<span class="ln in">$\Sigma_X=\mathbb E[(X-\mu)(X-\mu)^\top]$ is symmetric and positive semidefinite:</span>"""
        r"""<span class="ln in">$v^\top\Sigma_Xv=\operatorname{Var}(v^\top X)\ge0$ for all $v$.</span>"""
        r"""<span class="ln">Also $\Sigma_{AX+b}=A\Sigma_XA^\top$.</span>"""
        r"""<span class="src">Grimmett 3.6; Ross 7.4</span>"""},
    31102: {"statement": r"""<b>Orthogonality principle.</b>"""
        r"""<span class="ln">Among estimators $\hat Y=a+BX$,</span>"""
        r"""<span class="ln in">$\hat Y$ minimises $\mathbb E\|Y-\hat Y\|^2$ iff</span>"""
        r"""<span class="ln in2">$\mathbb E[Y-\hat Y]=0$ and $\mathbb E[(Y-\hat Y)X^\top]=0$:</span>"""
        r"""<span class="ln">the error is orthogonal to the constants and to the observations.</span>"""
        r"""<span class="src">Grimmett 7.9; Papoulis</span>"""},
    31103: {"statement": r"""<b>Linear least squares estimator.</b>"""
        r"""<span class="ln">If $\Sigma_X$ is invertible, the linear estimator of $Y$ from $X$ minimising mean squared error is</span>"""
        r"""<span class="ln in">$\hat Y=\mu_Y+\Sigma_{YX}\Sigma_X^{-1}(X-\mu_X)$,</span>"""
        r"""<span class="ln in">with gain $K=\Sigma_{YX}\Sigma_X^{-1}$.</span>"""
        r"""<span class="src">Grimmett 7.9; Ross 7.4</span>"""},
    31104: {"statement": r"""<b>Error covariance.</b>"""
        r"""<span class="ln">For the LLSE $\hat Y$, the error $e=Y-\hat Y$ has mean $0$ and covariance</span>"""
        r"""<span class="ln in">$\Sigma_e=\Sigma_Y-\Sigma_{YX}\Sigma_X^{-1}\Sigma_{XY}\preceq\Sigma_Y$,</span>"""
        r"""<span class="ln in">the Schur complement of $\Sigma_X$ in the joint covariance.</span>"""
        r"""<span class="src">Grimmett 7.9</span>"""},
    31105: {"statement": r"""<b>Scalar LLSE.</b>"""
        r"""<span class="ln">For scalar $X,Y$ with $\sigma_X\gt 0$,</span>"""
        r"""<span class="ln in">$\hat Y=\mu_Y+\rho\frac{\sigma_Y}{\sigma_X}(X-\mu_X)$ with $\rho=\frac{\operatorname{Cov}(X,Y)}{\sigma_X\sigma_Y}$,</span>"""
        r"""<span class="ln in">and $\mathbb E(Y-\hat Y)^2=\sigma_Y^2(1-\rho^2)$.</span>"""
        r"""<span class="src">Ross 7.4; Grimmett 3.6</span>"""},
    31106: {"statement": r"""<b>Wiener filter (scalar).</b>"""
        r"""<span class="ln">Let $Y=X+W$ with $X,W$ independent, zero mean, variances $\sigma_X^2,\sigma_W^2$.</span>"""
        r"""<span class="ln">Then</span>"""
        r"""<span class="ln in">$\hat X(Y)=\frac{\sigma_X^2}{\sigma_X^2+\sigma_W^2}Y$</span>"""
        r"""<span class="ln in">and $\operatorname{MSE}=\frac{\sigma_X^2\sigma_W^2}{\sigma_X^2+\sigma_W^2}$.</span>"""
        r"""<span class="src">Grimmett 7.9; Ross 7.4</span>"""},
}
