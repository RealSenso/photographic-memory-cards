"""StoMA Topic 09 statements, line by line (one hypothesis or conclusion per line; the source on its own small line)."""

SUBJECT = "StoMA"

FIX = {
    30901: {"statement": r"""<b>Convolution formula.</b>"""
        r"""<span class="ln">If $X,Y$ are independent with densities $f_X,f_Y$, then $X+Y$ has density</span>"""
        r"""<span class="ln in">$f_{X+Y}(z)=(f_X*f_Y)(z)=\int_{-\infty}^\infty f_X(x)f_Y(z-x)\,dx=\int_{-\infty}^\infty f_X(z-y)f_Y(y)\,dy$.</span>"""
        r"""<span class="ln">For independent integer-valued $X,Y$,</span>"""
        r"""<span class="ln in">$p_{X+Y}(z)=\sum_xp_X(x)p_Y(z-x)$.</span>"""
        r"""<span class="src">Ross 6.3; Grimmett 4.8</span>"""},
    30902: {"statement": r"""<b>Change of variables in two dimensions.</b>"""
        r"""<span class="ln">Let $(X,Y)$ have density $f_{X,Y}$</span>"""
        r"""<span class="ln">and let $(U,V)=(u(X,Y),v(X,Y))$ be a differentiable one-to-one map</span>"""
        r"""<span class="ln in">with inverse $x(u,v),y(u,v)$ and non-vanishing Jacobian.</span>"""
        r"""<span class="ln">Then</span>"""
        r"""<span class="ln in">$f_{U,V}(u,v)=f_{X,Y}\bigl(x(u,v),y(u,v)\bigr)\left|\det\dfrac{\partial(x,y)}{\partial(u,v)}\right|$.</span>"""
        r"""<span class="src">Ross 6.7; Grimmett 4.7</span>"""},
    30903: {"statement": r"""<b>Ratios and polar coordinates.</b>"""
        r"""<span class="ln">If $(X,Y)$ has density $f_{X,Y}$, then $Z=Y/X$ has density</span>"""
        r"""<span class="ln in">$f_Z(z)=\int_{-\infty}^\infty|x|\,f_{X,Y}(x,xz)\,dx$.</span>"""
        r"""<span class="ln">In polar coordinates $X=R\cos\Theta$, $Y=R\sin\Theta$, the density of $(R,\Theta)$ is</span>"""
        r"""<span class="ln in">$f_{R,\Theta}(r,\theta)=r\,f_{X,Y}(r\cos\theta,r\sin\theta)$ for $r\gt 0$.</span>"""
        r"""<span class="src">Ross 6.7; Grimmett 4.7</span>"""},
    30904: {"statement": r"""<b>Box–Muller transform.</b>"""
        r"""<span class="ln">If $U_1,U_2$ are independent $\text{Uniform}(0,1)$, then</span>"""
        r"""<span class="ln in">$Z_1=\sqrt{-2\ln U_1}\cos(2\pi U_2)$ and $Z_2=\sqrt{-2\ln U_1}\sin(2\pi U_2)$</span>"""
        r"""<span class="ln in">are independent $\mathcal N(0,1)$.</span>"""
        r"""<span class="ln">Proof: $R^2=-2\ln U_1\sim\mathrm{Exp}(1/2)$ and $\Theta=2\pi U_2\sim\text{Uniform}(0,2\pi)$ are independent,</span>"""
        r"""<span class="ln in">and the Jacobian of the polar map gives the joint density $\frac1{2\pi}e^{-(z_1^2+z_2^2)/2}$.</span>"""
        r"""<span class="src">Ross 6.7; Grimmett 4.11</span>"""},
    30905: {"statement": r"""<b>Closure under independent sums.</b>"""
        r"""<span class="ln">If $X_i\sim\mathcal N(\mu_i,\sigma_i^2)$ are independent,</span>"""
        r"""<span class="ln in">then $\sum_iX_i\sim\mathcal N\bigl(\sum\mu_i,\sum\sigma_i^2\bigr)$.</span>"""
        r"""<span class="ln">If $X_i\sim\mathrm{Pois}(\lambda_i)$ are independent,</span>"""
        r"""<span class="ln in">then $\sum_iX_i\sim\mathrm{Pois}\bigl(\sum\lambda_i\bigr)$.</span>"""
        r"""<span class="ln">If $X_i\sim\mathrm{Gamma}(\alpha_i,\beta)$ are independent (same rate),</span>"""
        r"""<span class="ln in">then $\sum_iX_i\sim\mathrm{Gamma}\bigl(\sum\alpha_i,\beta\bigr)$.</span>"""
        r"""<span class="src">Ross 7.7; Grimmett 4.8, 5.1</span>"""},
    30906: {"statement": r"""<b>Sum of two uniforms.</b>"""
        r"""<span class="ln">If $X,Y$ are independent $\text{Uniform}(0,1)$, then</span>"""
        r"""<span class="ln in">$f_{X+Y}(z)=z$ on $[0,1]$, $2-z$ on $(1,2]$, and $0$ otherwise (the triangular law);</span>"""
        r"""<span class="ln in">$\mathbb E[X+Y]=1$, $\operatorname{Var}(X+Y)=\frac16$.</span>"""
        r"""<span class="src">Ross 6.3; Grimmett 4.8</span>"""},
}
