"""StoMA Topic 19 statements, line by line (one hypothesis or conclusion per line; the source on its own small line)."""

SUBJECT = "StoMA"

FIX = {
    31901: {"statement": r"""<b>Markov chain.</b>"""
        r"""<span class="ln">A process $(X_n)_{n\ge0}$ on a countable state space $S$ is a Markov chain with transition matrix $P=(P_{ij})$ if</span>"""
        r"""<span class="ln in">$\mathbb P(X_{n+1}=j\mid X_n=i,X_{n-1}=i_{n-1},\ldots,X_0=i_0)=P_{ij}$</span>"""
        r"""<span class="ln in">for all $n$ and all histories.</span>"""
        r"""<span class="ln">Each row sums to one: $\sum_{j\in S}P_{ij}=1$.</span>"""
        r"""<span class="src">Ross 4.1; Grimmett 6.1</span>"""},
    31902: {"statement": r"""<b>Chapman–Kolmogorov.</b>"""
        r"""<span class="ln">For a Markov chain,</span>"""
        r"""<span class="ln in">$P^{(m+n)}_{ij}=\sum_{k\in S}P^{(m)}_{ik}P^{(n)}_{kj}$,</span>"""
        r"""<span class="ln in">i.e. $P^{(m+n)}=P^mP^n$ and so $P^{(n)}=P^n$.</span>"""
        r"""<span class="ln">If $\mathbf p^{(0)}$ is the law of $X_0$,</span>"""
        r"""<span class="ln in">then $\mathbf p^{(n)}=\mathbf p^{(0)}P^n$ is the law of $X_n$.</span>"""
        r"""<span class="src">Ross 4.2; Grimmett 6.1</span>"""},
    31903: {"statement": r"""<b>Accessibility and communication.</b>"""
        r"""<span class="ln">State $j$ is accessible from $i$, $i\to j$, if $P^{(n)}_{ij}\gt 0$ for some $n\ge0$.</span>"""
        r"""<span class="ln">States communicate, $i\leftrightarrow j$, if $i\to j$ and $j\to i$.</span>"""
        r"""<span class="ln">Communication is an equivalence relation,</span>"""
        r"""<span class="ln in">so the state space splits into disjoint classes: $S=\bigcup_kC_k$.</span>"""
        r"""<span class="src">Ross 4.3; Grimmett 6.2</span>"""},
    31904: {"statement": r"""<b>Recurrence and transience.</b>"""
        r"""<span class="ln">Let $f_{ii}=\mathbb P(X_n=i\text{ for some }n\ge1\mid X_0=i)$.</span>"""
        r"""<span class="ln">State $i$ is</span>"""
        r"""<span class="ln in">recurrent iff $f_{ii}=1$ iff $\sum_{n\ge1}P^{(n)}_{ii}=\infty$,</span>"""
        r"""<span class="ln in">and transient iff $f_{ii}\lt 1$ iff $\sum_{n\ge1}P^{(n)}_{ii}\lt \infty$.</span>"""
        r"""<span class="src">Ross 4.3; Grimmett 6.2</span>"""},
    31905: {"statement": r"""<b>Period and class properties.</b>"""
        r"""<span class="ln">The period of $i$ is $d(i)=\gcd\{n\ge1:P^{(n)}_{ii}\gt 0\}$;</span>"""
        r"""<span class="ln in">$i$ is aperiodic if $d(i)=1$.</span>"""
        r"""<span class="ln">If $i\leftrightarrow j$</span>"""
        r"""<span class="ln in">then $d(i)=d(j)$, and $i$ is recurrent iff $j$ is recurrent:</span>"""
        r"""<span class="ln">period, recurrence and transience are class properties.</span>"""
        r"""<span class="src">Ross 4.3; Grimmett 6.2</span>"""},
    31906: {"statement": r"""<b>Pólya: the 1D random walk.</b>"""
        r"""<span class="ln">Step $+1$ with probability $p$, $-1$ with $1-p$.</span>"""
        r"""<span class="ln in">Then $P^{(2n)}_{00}=\binom{2n}n(p(1-p))^n\sim\frac{(4p(1-p))^n}{\sqrt{\pi n}}$.</span>"""
        r"""<span class="ln">For $p=\tfrac12$ the sum $\sum_nP^{(2n)}_{00}=\infty$ (recurrent);</span>"""
        r"""<span class="ln">for $p\ne\tfrac12$ it is finite (transient).</span>"""
        r"""<span class="src">Ross 4.3; Grimmett 6.3</span>"""},
}
