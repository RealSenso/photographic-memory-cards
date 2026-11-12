"""StoMA Topic 24 statements, line by line (one hypothesis or conclusion per line; the source on its own small line)."""

SUBJECT = "StoMA"

FIX = {
    32401: {"statement": r"""<b>Poisson process.</b>"""
        r"""<span class="ln">A counting process $N(t)$ with</span>"""
        r"""<span class="ln in">$N(0)=0$,</span>"""
        r"""<span class="ln in">independent increments, stationary increments,</span>"""
        r"""<span class="ln in">$\mathbb P(N(t+h)-N(t)=1)=\lambda h+o(h)$ and</span>"""
        r"""<span class="ln in">$\mathbb P(N(t+h)-N(t)\ge2)=o(h)$</span>"""
        r"""<span class="ln">is a Poisson process of rate $\lambda$.</span>"""
        r"""<span class="ln in">Then $\mathbb P(N(t)=k)=\frac{(\lambda t)^ke^{-\lambda t}}{k!}$, $\mathbb E[N(t)]=\operatorname{Var}(N(t))=\lambda t$.</span>"""
        r"""<span class="src">Ross 5.3; Grimmett 6.8</span>"""},
    32402: {"statement": r"""<b>Inter-arrival and waiting times.</b>"""
        r"""<span class="ln">For a Poisson process of rate $\lambda$</span>"""
        r"""<span class="ln in">the inter-arrival times $T_1,T_2,\ldots$ are i.i.d. $\operatorname{Exp}(\lambda)$,</span>"""
        r"""<span class="ln in">the $n$-th arrival time $S_n=\sum_{k=1}^nT_k\sim\operatorname{Gamma}(n,\lambda)$, and</span>"""
        r"""<span class="ln in">$\mathbb P(N(t)\ge n)=\mathbb P(S_n\le t)$.</span>"""
        r"""<span class="src">Ross 5.3; Grimmett 6.8</span>"""},
    32403: {"statement": r"""<b>Order-statistics property.</b>"""
        r"""<span class="ln">Given $N(t)=n$, the arrival times $(S_1,\ldots,S_n)$ have the law of the order statistics of $n$ i.i.d. $\text{Uniform}(0,t)$ variables:</span>"""
        r"""<span class="ln in">the joint density is $\frac{n!}{t^n}$ on $0\lt s_1\lt \cdots\lt s_n\lt t$, and</span>"""
        r"""<span class="ln in">$\mathbb E[S_k\mid N(t)=n]=\frac{k}{n+1}t$.</span>"""
        r"""<span class="src">Ross 5.3; Grimmett 6.12</span>"""},
    32404: {"statement": r"""<b>Superposition and thinning.</b>"""
        r"""<span class="ln">If $N_1,N_2$ are independent Poisson processes with rates $\lambda_1,\lambda_2$,</span>"""
        r"""<span class="ln in">then $N_1+N_2$ is Poisson with rate $\lambda_1+\lambda_2$ (merging).</span>"""
        r"""<span class="ln">If each point of a rate-$\lambda$ Poisson process is independently kept with probability $p$,</span>"""
        r"""<span class="ln in">the kept points $N_1\sim\operatorname{PP}(\lambda p)$ and the rest $N_2\sim\operatorname{PP}(\lambda(1-p))$ are independent.</span>"""
        r"""<span class="src">Ross 5.3; Grimmett 6.8</span>"""},
    32405: {"statement": r"""<b>Non-homogeneous Poisson process.</b>"""
        r"""<span class="ln">With a rate function $\lambda(t)\ge0$, let $m(t)=\int_0^t\lambda(u)\,du$.</span>"""
        r"""<span class="ln in">Then $N(t+s)-N(s)\sim\operatorname{Poisson}\bigl(m(t+s)-m(s)\bigr)$,</span>"""
        r"""<span class="ln in">and counts on disjoint intervals are independent.</span>"""
        r"""<span class="src">Ross 5.4; Grimmett 6.13</span>"""},
    32406: {"statement": r"""<b>Inspection paradox.</b>"""
        r"""<span class="ln">For a Poisson process of rate $\lambda$ and a fixed time $t$,</span>"""
        r"""<span class="ln in">the wait $W(t)$ to the next arrival has $\mathbb E[W(t)]=\frac1\lambda$,</span>"""
        r"""<span class="ln in">and the time $B(t)$ since the last one has $\mathbb E[B(t)]\to\frac1\lambda$.</span>"""
        r"""<span class="ln">So the gap containing $t$ has $\mathbb E[I(t)]=\mathbb E[W+B]\to\frac2\lambda=2\mathbb E[T]$:</span>"""
        r"""<span class="ln in">length-biased sampling.</span>"""
        r"""<span class="src">Ross 7.7; Grimmett 10.4</span>"""},
}
