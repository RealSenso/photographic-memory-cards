"""StoMA Topic 02 statements, line by line (one hypothesis or conclusion per line; the source on its own small line)."""

SUBJECT = "StoMA"

FIX = {
    30201: {"statement": r"""<b>Conditional probability.</b>"""
        r"""<span class="ln">Let $B\in\mathcal F$ with $\mathbb P(B)\gt 0$.</span>"""
        r"""<span class="ln">The conditional probability of $A\in\mathcal F$ given $B$ is</span>"""
        r"""<span class="ln in">$\mathbb P(A\mid B)=\dfrac{\mathbb P(A\cap B)}{\mathbb P(B)}$.</span>"""
        r"""<span class="ln">The map $A\mapsto\mathbb P(A\mid B)$ is itself a probability measure on $(\Omega,\mathcal F)$,</span>"""
        r"""<span class="ln in">with $\mathbb P(B\mid B)=1$.</span>"""
        r"""<span class="src">Ross 3.2; Grimmett 1.4</span>"""},
    30202: {"statement": r"""<b>Chain rule.</b>"""
        r"""<span class="ln">For events with $\mathbb P(A_1\cap\cdots\cap A_{n-1})\gt 0$,</span>"""
        r"""<span class="ln in">$\mathbb P(\bigcap_{i=1}^nA_i)=\mathbb P(A_1)\prod_{k=2}^n\mathbb P(A_k\mid\bigcap_{j\lt k}A_j)$.</span>"""
        r"""<span class="ln">For two events,</span>"""
        r"""<span class="ln in">$\mathbb P(A\cap B)=\mathbb P(A)\mathbb P(B\mid A)$.</span>"""
        r"""<span class="src">Ross 3.2; Grimmett 1.4</span>"""},
    30203: {"statement": r"""<b>Law of total probability.</b>"""
        r"""<span class="ln">Let $B_1,\ldots,B_n$ be a partition of $\Omega$</span>"""
        r"""<span class="ln in">($B_i\cap B_j=\emptyset$ for $i\ne j$, $\bigcup_iB_i=\Omega$)</span>"""
        r"""<span class="ln in">with $\mathbb P(B_i)\gt 0$.</span>"""
        r"""<span class="ln">Then for every event $A$,</span>"""
        r"""<span class="ln in">$\mathbb P(A)=\sum_{i=1}^n\mathbb P(A\mid B_i)\,\mathbb P(B_i)$.</span>"""
        r"""<span class="src">Ross 3.3; Grimmett 1.4</span>"""},
    30204: {"statement": r"""<b>Bayes' theorem.</b>"""
        r"""<span class="ln">Let $B_1,\ldots,B_n$ partition $\Omega$ with $\mathbb P(B_i)\gt 0$,</span>"""
        r"""<span class="ln">and let $\mathbb P(A)\gt 0$.</span>"""
        r"""<span class="ln">Then</span>"""
        r"""<span class="ln in">$\mathbb P(B_k\mid A)=\dfrac{\mathbb P(A\mid B_k)\,\mathbb P(B_k)}{\sum_{i=1}^n\mathbb P(A\mid B_i)\,\mathbb P(B_i)}$</span>"""
        r"""<span class="ln in">$=\dfrac{\mathbb P(A\mid B_k)\,\mathbb P(B_k)}{\mathbb P(A)}$.</span>"""
        r"""<span class="src">Ross 3.3; Grimmett 1.4</span>"""},
    30205: {"statement": r"""<b>Independence and conditional independence.</b>"""
        r"""<span class="ln">Events $A,B$ are independent if $\mathbb P(A\cap B)=\mathbb P(A)\mathbb P(B)$</span>"""
        r"""<span class="ln in">(equivalently $\mathbb P(A\mid B)=\mathbb P(A)$ when $\mathbb P(B)\gt 0$).</span>"""
        r"""<span class="ln">Given an event $C$ with $\mathbb P(C)\gt 0$, $A$ and $B$ are conditionally independent given $C$ if</span>"""
        r"""<span class="ln in">$\mathbb P(A\cap B\mid C)=\mathbb P(A\mid C)\mathbb P(B\mid C)$.</span>"""
        r"""<span class="ln">Neither implies the other.</span>"""
        r"""<span class="src">Ross 3.4; Grimmett 1.5</span>"""},
    30206: {"statement": r"""<b>Bernstein's example.</b>"""
        r"""<span class="ln">A tetrahedron has faces coloured $\{R\}$, $\{G\}$, $\{B\}$ and $\{R,G,B\}$,</span>"""
        r"""<span class="ln in">each face rolled with probability $\tfrac14$.</span>"""
        r"""<span class="ln">Then $\mathbb P(R)=\mathbb P(G)=\mathbb P(B)=\tfrac12$</span>"""
        r"""<span class="ln in">and $\mathbb P(R\cap G)=\tfrac14=\mathbb P(R)\mathbb P(G)$ (and likewise for the other pairs),</span>"""
        r"""<span class="ln in">so the events are pairwise independent.</span>"""
        r"""<span class="ln">But $\mathbb P(R\cap G\cap B)=\tfrac14\ne\tfrac18=\mathbb P(R)\mathbb P(G)\mathbb P(B)$,</span>"""
        r"""<span class="ln in">so they are not mutually independent.</span>"""
        r"""<span class="src">Grimmett 1.5</span>"""},
}
