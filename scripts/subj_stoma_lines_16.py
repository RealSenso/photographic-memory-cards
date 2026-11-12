"""StoMA Topic 16 statements, line by line (one hypothesis or conclusion per line; the source on its own small line)."""

SUBJECT = "StoMA"

FIX = {
    31601: {"statement": r"""<b>Limsup and liminf of events.</b>"""
        r"""<span class="ln">For events $A_n$,</span>"""
        r"""<span class="ln in">$\limsup A_n=\bigcap_{n=1}^\infty\bigcup_{k=n}^\infty A_k=\{A_n\text{ infinitely often}\}$</span>"""
        r"""<span class="ln in">and $\liminf A_n=\bigcup_{n=1}^\infty\bigcap_{k=n}^\infty A_k=\{A_n\text{ for all but finitely many }n\}$.</span>"""
        r"""<span class="ln">Also $(\limsup A_n)^c=\liminf A_n^c$.</span>"""
        r"""<span class="src">Grimmett 7.3; Durrett 2.3</span>"""},
    31602: {"statement": r"""<b>First Borel–Cantelli lemma.</b>"""
        r"""<span class="ln">If $\sum_{n=1}^\infty\mathbb P(A_n)\lt \infty$,</span>"""
        r"""<span class="ln in">then $\mathbb P(A_n\text{ i.o.})=\mathbb P(\limsup A_n)=0$.</span>"""
        r"""<span class="ln">No independence is needed.</span>"""
        r"""<span class="ln">Proof:</span>"""
        r"""<span class="ln in">$\mathbb P(\limsup A_n)\le\mathbb P(\bigcup_{k\ge n}A_k)\le\sum_{k\ge n}\mathbb P(A_k)\to0$.</span>"""
        r"""<span class="src">Grimmett 7.3; Ross 8.2</span>"""},
    31603: {"statement": r"""<b>Second Borel–Cantelli lemma.</b>"""
        r"""<span class="ln">If $A_1,A_2,\ldots$ are independent and $\sum_{n=1}^\infty\mathbb P(A_n)=\infty$,</span>"""
        r"""<span class="ln in">then $\mathbb P(A_n\text{ i.o.})=1$.</span>"""
        r"""<span class="ln">Proof:</span>"""
        r"""<span class="ln in">$\mathbb P(\bigcap_{k\ge n}A_k^c)=\prod_{k\ge n}(1-\mathbb P(A_k))\le\exp(-\sum_{k\ge n}\mathbb P(A_k))=0$.</span>"""
        r"""<span class="src">Grimmett 7.3; Ross 8.2</span>"""},
    31604: {"statement": r"""<b>Kolmogorov's zero–one law.</b>"""
        r"""<span class="ln">Let $X_1,X_2,\ldots$ be independent</span>"""
        r"""<span class="ln">and $\mathcal T=\bigcap_{n=1}^\infty\sigma(X_n,X_{n+1},\ldots)$ the tail $\sigma$-algebra.</span>"""
        r"""<span class="ln in">Then $\mathbb P(E)\in\{0,1\}$ for every $E\in\mathcal T$.</span>"""
        r"""<span class="src">Grimmett 7.3; Durrett 2.5</span>"""},
    31605: {"statement": r"""<b>Almost sure convergence via Borel–Cantelli.</b>"""
        r"""<span class="ln">If $\sum_{n=1}^\infty\mathbb P(|X_n-X|\ge\varepsilon)\lt \infty$ for every $\varepsilon\gt 0$,</span>"""
        r"""<span class="ln in">then $X_n\to X$ almost surely.</span>"""
        r"""<span class="ln">Proof: by the first Borel–Cantelli lemma, $|X_n-X|\ge\varepsilon$ happens only finitely often a.s.;</span>"""
        r"""<span class="ln in">take $\varepsilon=1/m$ and a countable intersection.</span>"""
        r"""<span class="src">Grimmett 7.3; Durrett 2.3</span>"""},
    31606: {"statement": r"""<b>Head runs.</b>"""
        r"""<span class="ln">In an infinite sequence of fair coin tosses,</span>"""
        r"""<span class="ln in">let $A_k$ be the event that tosses $k,\ldots,k+L_k-1$ are all heads, so $\mathbb P(A_k)=2^{-L_k}$.</span>"""
        r"""<span class="ln">If $\sum_k2^{-L_k}\lt \infty$,</span>"""
        r"""<span class="ln in">the run lengths $L_k$ occur only finitely often (first Borel–Cantelli);</span>"""
        r"""<span class="ln">if $\sum_k2^{-L_k}=\infty$ and the events are independent (disjoint blocks),</span>"""
        r"""<span class="ln in">they occur infinitely often a.s. (second).</span>"""
        r"""<span class="src">Grimmett 7.3; Durrett 2.3</span>"""},
}
