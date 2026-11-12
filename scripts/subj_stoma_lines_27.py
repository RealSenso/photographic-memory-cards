"""StoMA Topic 27 statements, line by line (one hypothesis or conclusion per line; the source on its own small line)."""

SUBJECT = "StoMA"

FIX = {
    32701: {"statement": r"""<b>Generator of a CTMC.</b>"""
        r"""<span class="ln">A continuous-time Markov chain on $S$ has transition functions $P_{ij}(t)$ and generator $Q$ with</span>"""
        r"""<span class="ln in">$q_{ij}=\lim_{h\downarrow0}\frac{P_{ij}(h)}h\ (i\ne j)$, $q_{ii}=-\sum_{j\ne i}q_{ij}$,</span>"""
        r"""<span class="ln in">so $Q\mathbf 1=\mathbf 0$.</span>"""
        r"""<span class="ln">The holding time in $i$ is $T_i\sim\operatorname{Exp}(q_i)$, $q_i=-q_{ii}$,</span>"""
        r"""<span class="ln in">and the next state is $j$ with probability $q_{ij}/q_i$.</span>"""
        r"""<span class="src">Ross 6.2; Grimmett 6.9</span>"""},
    32702: {"statement": r"""<b>Kolmogorov equations.</b>"""
        r"""<span class="ln">For a (non-explosive) CTMC with generator $Q$,</span>"""
        r"""<span class="ln in">$P'(t)=QP(t)$ (backward) and $P'(t)=P(t)Q$ (forward), $P(0)=I$.</span>"""
        r"""<span class="ln">For a finite state space the solution is</span>"""
        r"""<span class="ln in">$P(t)=e^{Qt}=\sum_{n\ge0}\frac{(Qt)^n}{n!}$, and $P(s+t)=P(s)P(t)$.</span>"""
        r"""<span class="src">Ross 6.4; Grimmett 6.9</span>"""},
    32703: {"statement": r"""<b>Two-state chain.</b>"""
        r"""<span class="ln">States $1\to2$ at rate $\lambda$ and $2\to1$ at rate $\mu$.</span>"""
        r"""<span class="ln in">Then $P_{11}(t)=\dfrac\mu{\lambda+\mu}+\dfrac\lambda{\lambda+\mu}e^{-(\lambda+\mu)t}$,</span>"""
        r"""<span class="ln in">and $\lim_{t\to\infty}P_{11}(t)=\pi_1=\frac\mu{\lambda+\mu}$.</span>"""
        r"""<span class="ln">The memory of the start decays at rate $\lambda+\mu$.</span>"""
        r"""<span class="src">Ross 6.4; Grimmett 6.9</span>"""},
    32704: {"statement": r"""<b>Stationary distribution of a CTMC.</b>"""
        r"""<span class="ln">A probability vector $\pi$ is stationary if</span>"""
        r"""<span class="ln in">$\pi^\top Q=\mathbf 0^\top$ (global balance), $\sum_i\pi_i=1$,</span>"""
        r"""<span class="ln in">equivalently $\pi^\top P(t)=\pi^\top$ for all $t$.</span>"""
        r"""<span class="ln">If $\pi_iq_{ij}=\pi_jq_{ji}$ for all $i,j$ (detailed balance),</span>"""
        r"""<span class="ln in">then $\pi^\top Q=\mathbf 0^\top$.</span>"""
        r"""<span class="src">Ross 6.5; Grimmett 6.9</span>"""},
    32705: {"statement": r"""<b>M/M/1 queue.</b>"""
        r"""<span class="ln">Arrivals at rate $\lambda$, service at rate $\mu$, one server; $\rho=\lambda/\mu\lt 1$.</span>"""
        r"""<span class="ln in">The number in system is a birth–death chain with $\pi_n=(1-\rho)\rho^n$,</span>"""
        r"""<span class="ln in">mean $\mathbb E[L]=\frac\rho{1-\rho}$</span>"""
        r"""<span class="ln in">and mean time in system $W=\frac1{\mu-\lambda}$ (Little's law $L=\lambda W$).</span>"""
        r"""<span class="ln">For M/M/c, $\rho=\frac\lambda{c\mu}\lt 1$.</span>"""
        r"""<span class="src">Ross 8.3; Grimmett 11.2</span>"""},
    32706: {"statement": r"""<b>Uniformization (Jensen).</b>"""
        r"""<span class="ln">Pick $\nu\ge\max_iq_i$ and let $K=I+\frac1\nu Q$, a stochastic matrix.</span>"""
        r"""<span class="ln in">Then $P(t)=\sum_{n\ge0}\frac{(\nu t)^ne^{-\nu t}}{n!}K^n$:</span>"""
        r"""<span class="ln">the chain is a discrete chain with transition matrix $K$ observed at the ticks of a rate-$\nu$ Poisson clock.</span>"""
        r"""<span class="src">Ross 6.7; Grimmett 6.9</span>"""},
}
