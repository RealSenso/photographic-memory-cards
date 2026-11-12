"""StoMA Topic 03 statements, line by line (one hypothesis or conclusion per line; the source on its own small line)."""

SUBJECT = "StoMA"

FIX = {
    30301: {"statement": r"""<b>Random variable and CDF.</b>"""
        r"""<span class="ln">A random variable on $(\Omega,\mathcal F,\mathbb P)$ is a function $X:\Omega\to\mathbb R$</span>"""
        r"""<span class="ln in">such that $\{X\le x\}\in\mathcal F$ for all $x$.</span>"""
        r"""<span class="ln">Its cumulative distribution function is $F_X(x)=\mathbb P(X\le x)$.</span>"""
        r"""<span class="ln">Then $F_X$ is non-decreasing and right-continuous,</span>"""
        r"""<span class="ln in">with $F_X(-\infty)=0$ and $F_X(\infty)=1$,</span>"""
        r"""<span class="ln in">and $F_X(x)-F_X(x^-)=\mathbb P(X=x)$.</span>"""
        r"""<span class="src">Ross 4.1; Grimmett 2.1</span>"""},
    30302: {"statement": r"""<b>Discrete random variable and PMF.</b>"""
        r"""<span class="ln">$X$ is discrete if it takes values in a countable set $\{x_k\}$.</span>"""
        r"""<span class="ln">Its probability mass function $p_X(x_k)=\mathbb P(X=x_k)$ satisfies</span>"""
        r"""<span class="ln in">$p_X(x_k)\ge0$ and $\sum_kp_X(x_k)=1$.</span>"""
        r"""<span class="ln">Its CDF is a step function $F_X(x)=\sum_{x_k\le x}p_X(x_k)$</span>"""
        r"""<span class="ln in">with a jump of size $p_X(x_k)$ at each $x_k$.</span>"""
        r"""<span class="src">Ross 4.2; Grimmett 2.1</span>"""},
    30303: {"statement": r"""<b>Continuous random variable and PDF.</b>"""
        r"""<span class="ln">$X$ is continuous if $F_X(x)=\int_{-\infty}^xf_X(t)\,dt$</span>"""
        r"""<span class="ln in">for a function $f_X\ge0$ with $\int_{-\infty}^\infty f_X=1$, the probability density function.</span>"""
        r"""<span class="ln">Then</span>"""
        r"""<span class="ln in">$f_X(x)=F_X'(x)$ at continuity points of $f_X$,</span>"""
        r"""<span class="ln in">$\mathbb P(a\le X\le b)=\int_a^bf_X$,</span>"""
        r"""<span class="ln in">and $\mathbb P(X=c)=0$ for every $c$.</span>"""
        r"""<span class="src">Ross 5.1; Grimmett 4.1</span>"""},
    30304: {"statement": r"""<b>Exponential distribution and memorylessness.</b>"""
        r"""<span class="ln">$X\sim\mathrm{Exp}(\lambda)$ has density $f_X(t)=\lambda e^{-\lambda t}$ for $t\ge0$,</span>"""
        r"""<span class="ln in">so $\mathbb P(X\gt t)=e^{-\lambda t}$.</span>"""
        r"""<span class="ln">Then for all $s,t\ge0$,</span>"""
        r"""<span class="ln in">$\mathbb P(X\gt t+s\mid X\gt t)=\dfrac{e^{-\lambda(t+s)}}{e^{-\lambda t}}=e^{-\lambda s}=\mathbb P(X\gt s)$.</span>"""
        r"""<span class="ln">It is the only continuous distribution on $[0,\infty)$ with this property.</span>"""
        r"""<span class="src">Ross 5.5</span>"""},
    30305: {"statement": r"""<b>Standardisation of the normal law.</b>"""
        r"""<span class="ln">If $X\sim\mathcal N(\mu,\sigma^2)$, with density</span>"""
        r"""<span class="ln in">$f_X(x)=\dfrac1{\sigma\sqrt{2\pi}}e^{-(x-\mu)^2/2\sigma^2}$,</span>"""
        r"""<span class="ln">then $Z=\dfrac{X-\mu}{\sigma}\sim\mathcal N(0,1)$.</span>"""
        r"""<span class="ln">Writing $\Phi$ for the $\mathcal N(0,1)$ CDF,</span>"""
        r"""<span class="ln in">$\mathbb P(X\le x)=\Phi\!\left(\frac{x-\mu}{\sigma}\right)$ and $\Phi(-z)=1-\Phi(z)$.</span>"""
        r"""<span class="src">Ross 5.4; Grimmett 4.4</span>"""},
    30306: {"statement": r"""<b>Mixed random variable.</b>"""
        r"""<span class="ln">A random variable whose CDF has the form $F_X=\alpha F_{\rm disc}+(1-\alpha)F_{\rm cont}$, $0\lt \alpha\lt 1$,</span>"""
        r"""<span class="ln in">with $F_{\rm disc}$ a step function and $F_{\rm cont}$ continuous, is mixed.</span>"""
        r"""<span class="ln">Its mean is</span>"""
        r"""<span class="ln in">$\mathbb E[X]=\sum_kx_k\,\mathbb P(X=x_k)+\int_{-\infty}^\infty x\,f_c(x)\,dx$,</span>"""
        r"""<span class="ln in">the atoms plus the continuous part, where $f_c$ is the density of the continuous part.</span>"""
        r"""<span class="src">Ross 5.1; Grimmett 4.1</span>"""},
}
