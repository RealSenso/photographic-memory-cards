"""StoMA Topic 26 statements, line by line (one hypothesis or conclusion per line; the source on its own small line)."""

SUBJECT = "StoMA"

FIX = {
    32601: {"statement": r"""<b>Filtration and martingale.</b>"""
        r"""<span class="ln">A filtration $(\mathcal F_n)$ is an increasing sequence of σ-fields.</span>"""
        r"""<span class="ln">$(M_n)$ is a martingale if</span>"""
        r"""<span class="ln in">$M_n$ is $\mathcal F_n$-measurable, $\mathbb E|M_n|\lt \infty$ and $\mathbb E[M_{n+1}\mid\mathcal F_n]=M_n$.</span>"""
        r"""<span class="ln">Then $\mathbb E[M_n]=\mathbb E[M_0]$ for all $n\ge0$;</span>"""
        r"""<span class="ln">with $\ge$ or $\le$ it is a sub- or supermartingale.</span>"""
        r"""<span class="src">Williams 10; Grimmett 12.1</span>"""},
    32602: {"statement": r"""<b>Canonical martingales.</b>"""
        r"""<span class="ln">For i.i.d. $X_i$ with mean $\mu$, variance $\sigma^2$ and MGF $M_X(\theta)\lt \infty$, and $S_n=\sum_{i\le n}X_i$:</span>"""
        r"""<span class="ln in">$S_n-n\mu$, $(S_n-n\mu)^2-n\sigma^2$ and $\dfrac{e^{\theta S_n}}{M_X(\theta)^n}$ are martingales.</span>"""
        r"""<span class="ln">For any integrable $Y$, $M_n=\mathbb E[Y\mid\mathcal F_n]$ is a martingale (Doob).</span>"""
        r"""<span class="src">Williams 10; Grimmett 12.1</span>"""},
    32603: {"statement": r"""<b>Stopping times and the stopped martingale.</b>"""
        r"""<span class="ln">A random time $\tau$ is a stopping time if $\{\tau\le n\}\in\mathcal F_n$ for all $n\ge0$.</span>"""
        r"""<span class="ln">If $(M_n)$ is a martingale</span>"""
        r"""<span class="ln in">then the stopped process $M_{n\wedge\tau}$ is a martingale,</span>"""
        r"""<span class="ln in">so $\mathbb E[M_{n\wedge\tau}]=\mathbb E[M_0]$ for each $n$.</span>"""
        r"""<span class="src">Williams 10; Grimmett 12.4</span>"""},
    32604: {"statement": r"""<b>Optional stopping theorem.</b>"""
        r"""<span class="ln">If $(M_n)$ is a martingale and $\tau$ a stopping time,</span>"""
        r"""<span class="ln in">then $\mathbb E[M_\tau]=\mathbb E[M_0]$ provided one of:</span>"""
        r"""<span class="ln in2">(a) $\tau\le C$ a.s.;</span>"""
        r"""<span class="ln in2">(b) $\tau\lt \infty$ a.s. and $|M_{n\wedge\tau}|\le K$;</span>"""
        r"""<span class="ln in2">(c) $\mathbb E[\tau]\lt \infty$ and $|M_{n+1}-M_n|\le c$.</span>"""
        r"""<span class="src">Williams 10.10; Grimmett 12.5</span>"""},
    32605: {"statement": r"""<b>Gambler's ruin by OST.</b>"""
        r"""<span class="ln">For a fair simple random walk $S_n$ started at $0$ and $\tau$ the first exit time from $(-a,b)$:</span>"""
        r"""<span class="ln in">$\mathbb E[S_\tau]=0$ gives $\mathbb P(\text{hit }b\text{ first})=\frac a{a+b}$,</span>"""
        r"""<span class="ln in">and $\mathbb E[S_\tau^2-\tau]=0$ gives $\mathbb E[\tau]=ab$</span>"""
        r"""<span class="ln">(Wald's identities).</span>"""
        r"""<span class="src">Ross 6.3; Williams 10.12</span>"""},
    32606: {"statement": r"""<b>Doob's inequality and Azuma–Hoeffding.</b>"""
        r"""<span class="ln">For a non-negative submartingale $(X_k)$,</span>"""
        r"""<span class="ln in">$\mathbb P\bigl(\max_{0\le k\le n}X_k\ge\lambda\bigr)\le\frac{\mathbb E[X_n]}\lambda$.</span>"""
        r"""<span class="ln">For a martingale with $|M_k-M_{k-1}|\le c_k$,</span>"""
        r"""<span class="ln in">$\mathbb P(|M_n-M_0|\ge t)\le2\exp\Bigl(-\frac{t^2}{2\sum_{k=1}^nc_k^2}\Bigr)$.</span>"""
        r"""<span class="src">Williams 14; Grimmett 12.6</span>"""},
}
