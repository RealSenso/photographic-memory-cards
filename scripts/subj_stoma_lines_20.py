"""StoMA Topic 20 statements, line by line (one hypothesis or conclusion per line; the source on its own small line)."""

SUBJECT = "StoMA"

FIX = {
    32001: {"statement": r"""<b>Stationary distribution.</b>"""
        r"""<span class="ln">A probability vector $\pi$ on $S$ is stationary for $P$ if $\pi^{\top}P=\pi^{\top}$,</span>"""
        r"""<span class="ln in">i.e. $\pi_j=\sum_{i\in S}\pi_iP_{ij}$ for all $j$,</span>"""
        r"""<span class="ln in">with $\pi_i\ge0$ and $\sum_i\pi_i=1$.</span>"""
        r"""<span class="ln">If $X_0\sim\pi$ then $X_n\sim\pi$ for every $n$.</span>"""
        r"""<span class="src">Ross 4.4; Grimmett 6.4</span>"""},
    32002: {"statement": r"""<b>Fundamental limit theorem.</b>"""
        r"""<span class="ln">For an irreducible, aperiodic, positive recurrent chain,</span>"""
        r"""<span class="ln in">$\lim_{n\to\infty}P^{(n)}_{ij}=\pi_j=\dfrac1{\mu_{jj}}\gt 0$ for all $i,j$,</span>"""
        r"""<span class="ln in">where $\mu_{jj}=\mathbb E[\tau_j\mid X_0=j]$ is the mean return time to $j$,</span>"""
        r"""<span class="ln in">and $\pi$ is the unique stationary distribution.</span>"""
        r"""<span class="src">Ross 4.4; Grimmett 6.4</span>"""},
    32003: {"statement": r"""<b>Positive versus null recurrence.</b>"""
        r"""<span class="ln">A recurrent state $i$ is</span>"""
        r"""<span class="ln in">positive recurrent if $\mu_{ii}=\mathbb E[\tau_i\mid X_0=i]\lt \infty$</span>"""
        r"""<span class="ln in">and null recurrent if $\mu_{ii}=\infty$.</span>"""
        r"""<span class="ln">An irreducible chain has a stationary distribution iff it is positive recurrent;</span>"""
        r"""<span class="ln in">for null recurrent or transient chains $\pi_i\equiv0$ (e.g. the symmetric random walk).</span>"""
        r"""<span class="src">Ross 4.4; Grimmett 6.4</span>"""},
    32004: {"statement": r"""<b>Cut equations and detailed balance.</b>"""
        r"""<span class="ln">If $\pi$ is stationary then for every $A\subset S$,</span>"""
        r"""<span class="ln in">$\sum_{i\in A,\,j\in A^c}\pi_iP_{ij}=\sum_{j\in A^c,\,i\in A}\pi_jP_{ji}$.</span>"""
        r"""<span class="ln">If $\pi_iP_{ij}=\pi_jP_{ji}$ for all $i,j$ (detailed balance),</span>"""
        r"""<span class="ln in">then $\pi^{\top}P=\pi^{\top}$ and the chain is reversible.</span>"""
        r"""<span class="src">Ross 4.8; Grimmett 6.5</span>"""},
    32005: {"statement": r"""<b>Periodic chains and Cesàro limits.</b>"""
        r"""<span class="ln">For an irreducible positive recurrent chain, periodic or not,</span>"""
        r"""<span class="ln in">$\lim_{N\to\infty}\frac1N\sum_{n=1}^NP^{(n)}_{ij}=\pi_j$.</span>"""
        r"""<span class="ln">If the chain has period $d\gt 1$,</span>"""
        r"""<span class="ln in">$P^{(n)}_{ij}$ itself does not converge.</span>"""
        r"""<span class="src">Ross 4.4; Grimmett 6.4</span>"""},
    32006: {"statement": r"""<b>Ergodic theorem for Markov chains.</b>"""
        r"""<span class="ln">For an irreducible positive recurrent chain with stationary $\pi$</span>"""
        r"""<span class="ln">and $f$ with $\sum_j\pi_j|f(j)|\lt \infty$,</span>"""
        r"""<span class="ln in">$\lim_{N\to\infty}\frac1N\sum_{n=1}^Nf(X_n)=\sum_{j\in S}\pi_jf(j)=\mathbb E_\pi[f(X)]$</span>"""
        r"""<span class="ln in">almost surely, from any starting state.</span>"""
        r"""<span class="src">Ross 4.4; Grimmett 6.4</span>"""},
}
