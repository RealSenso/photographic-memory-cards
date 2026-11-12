"""StoMA Topic 01 statements, line by line (one hypothesis or conclusion per line; the source on its own small line)."""

SUBJECT = "StoMA"

FIX = {
    30101: {"statement": r"""<b>Probability space.</b>"""
        r"""<span class="ln">A probability space is a triple $(\Omega,\mathcal F,\mathbb P)$:</span>"""
        r"""<span class="ln in">$\Omega$ is a nonempty set (the sample space);</span>"""
        r"""<span class="ln in">$\mathcal F$ is a $\sigma$-algebra of subsets of $\Omega$, i.e.</span>"""
        r"""<span class="ln in2">$\Omega\in\mathcal F$,</span>"""
        r"""<span class="ln in2">$A\in\mathcal F\Rightarrow A^c\in\mathcal F$, and</span>"""
        r"""<span class="ln in2">$A_1,A_2,\ldots\in\mathcal F\Rightarrow\bigcup_i A_i\in\mathcal F$;</span>"""
        r"""<span class="ln in">and $\mathbb P:\mathcal F\to[0,1]$ is a probability measure.</span>"""
        r"""<span class="src">Ross 2.2; Grimmett 1.2</span>"""},
    30102: {"statement": r"""<b>Kolmogorov's axioms.</b>"""
        r"""<span class="ln">A function $\mathbb P:\mathcal F\to\mathbb R$ on a $\sigma$-algebra $\mathcal F$ of $\Omega$ is a probability measure if</span>"""
        r"""<span class="ln in">(i) $\mathbb P(A)\ge0$ for all $A\in\mathcal F$;</span>"""
        r"""<span class="ln in">(ii) $\mathbb P(\Omega)=1$;</span>"""
        r"""<span class="ln in">(iii) for pairwise disjoint $A_1,A_2,\ldots\in\mathcal F$, $\mathbb P\!\left(\bigcup_{i}A_i\right)=\sum_i\mathbb P(A_i)$.</span>"""
        r"""<span class="src">Ross 2.3; Grimmett 1.3</span>"""},
    30103: {"statement": r"""<b>Continuity of probability.</b>"""
        r"""<span class="ln">Let $(\Omega,\mathcal F,\mathbb P)$ be a probability space.</span>"""
        r"""<span class="ln">If $A_1\subset A_2\subset\cdots$ in $\mathcal F$ and $A=\bigcup_nA_n$ (written $A_n\uparrow A$),</span>"""
        r"""<span class="ln in">then $\mathbb P(A)=\lim_n\mathbb P(A_n)$.</span>"""
        r"""<span class="ln">If $B_1\supset B_2\supset\cdots$ in $\mathcal F$ and $B=\bigcap_nB_n$ ($B_n\downarrow B$),</span>"""
        r"""<span class="ln in">then $\mathbb P(B)=\lim_n\mathbb P(B_n)$.</span>"""
        r"""<span class="src">Ross 2.6; Grimmett 1.3</span>"""},
    30104: {"statement": r"""<b>Boole's inequality (countable subadditivity).</b>"""
        r"""<span class="ln">For any events $A_1,A_2,\ldots\in\mathcal F$, disjoint or not,</span>"""
        r"""<span class="ln in">$\mathbb P\!\left(\bigcup_{i=1}^\infty A_i\right)\le\sum_{i=1}^\infty\mathbb P(A_i)$.</span>"""
        r"""<span class="ln">Truncating inclusion-exclusion gives the Bonferroni bounds, e.g.</span>"""
        r"""<span class="ln in">$\mathbb P(A\cup B)=\mathbb P(A)+\mathbb P(B)-\mathbb P(A\cap B)$.</span>"""
        r"""<span class="src">Ross 2.4; Grimmett 1.3</span>"""},
    30105: {"statement": r"""<b>Inclusion–exclusion.</b>"""
        r"""<span class="ln">For events $A_1,\ldots,A_n$,</span>"""
        r"""<span class="ln in">$\mathbb P(\bigcup_iA_i)=\sum_{k=1}^n(-1)^{k-1}S_k$,</span>"""
        r"""<span class="ln in">where $S_k=\sum_{i_1\lt \cdots\lt i_k}\mathbb P(A_{i_1}\cap\cdots\cap A_{i_k})$.</span>"""
        r"""<span class="ln">Partial sums alternate as upper and lower (Bonferroni) bounds.</span>"""
        r"""<span class="src">Ross 2.4; Grimmett 1.3</span>"""},
    30106: {"statement": r"""<b>Never tails.</b>"""
        r"""<span class="ln">A fair coin is tossed infinitely often.</span>"""
        r"""<span class="ln">Let $B_n=\{\text{first }n\text{ tosses are heads}\}$;</span>"""
        r"""<span class="ln in">then $B_n\downarrow B=\{\text{all tosses heads}\}$.</span>"""
        r"""<span class="ln">By continuity from above,</span>"""
        r"""<span class="ln in">$\mathbb P(B)=\lim_n\mathbb P(B_n)=\lim_n2^{-n}=0$.</span>"""
        r"""<span class="ln">The event $B$ is nonempty (it contains $HHH\cdots$) yet has probability $0$.</span>"""},
}
