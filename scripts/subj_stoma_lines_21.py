"""StoMA Topic 21 statements, line by line (one hypothesis or conclusion per line; the source on its own small line)."""

SUBJECT = "StoMA"

FIX = {
    32101: {"statement": r"""<b>First-step analysis for absorption.</b>"""
        r"""<span class="ln">Let $A,B\subset S$ be disjoint absorbing sets and $a_i=\mathbb P_i(\text{hit }A\text{ before }B)$.</span>"""
        r"""<span class="ln in">Then $a_i=\sum_{j\in S}P_{ij}a_j$ for $i\notin A\cup B$,</span>"""
        r"""<span class="ln in">with $a_i=1$ for $i\in A$ and $a_i=0$ for $i\in B$.</span>"""
        r"""<span class="ln">The minimal non-negative solution is $a_i$.</span>"""
        r"""<span class="src">Ross 4.5; Grimmett 6.3</span>"""},
    32102: {"statement": r"""<b>Mean hitting time.</b>"""
        r"""<span class="ln">Let $\mu_i=\mathbb E_i[\tau_A]$ be the expected number of steps to hit $A$.</span>"""
        r"""<span class="ln">It is the minimal non-negative solution of</span>"""
        r"""<span class="ln in">$\mu_i=0$ for $i\in A$ and</span>"""
        r"""<span class="ln in">$\mu_i=1+\sum_{j\notin A}P_{ij}\mu_j$ for $i\notin A$;</span>"""
        r"""<span class="ln">equivalently $(I-Q)\boldsymbol\mu=\mathbf 1$, with $Q$ the transitions among states outside $A$.</span>"""
        r"""<span class="src">Ross 4.5; Grimmett 6.3</span>"""},
    32103: {"statement": r"""<b>Canonical form and fundamental matrix.</b>"""
        r"""<span class="ln">Order the states with the transient ones first: $P=\begin{pmatrix}Q&R\\0&I\end{pmatrix}$.</span>"""
        r"""<span class="ln in">Then $P^n=\begin{pmatrix}Q^n&\ast\\0&I\end{pmatrix}$, $Q^n\to0$,</span>"""
        r"""<span class="ln in">and $N=\sum_{k\ge0}Q^k=(I-Q)^{-1}$,</span>"""
        r"""<span class="ln in">where $N_{ij}=\mathbb E_i[\text{number of visits to }j\text{ before absorption}]$.</span>"""
        r"""<span class="src">Grimmett 6.3; Kemeny–Snell</span>"""},
    32104: {"statement": r"""<b>Absorption probabilities and lifetime.</b>"""
        r"""<span class="ln">With $N=(I-Q)^{-1}$,</span>"""
        r"""<span class="ln in">the matrix $B=NR$ has entries $B_{ik}=\mathbb P_i(\text{absorbed in state }k)$,</span>"""
        r"""<span class="ln in">and the vector $\mathbf t=N\mathbf 1$ has $t_i=\mathbb E_i[\tau_{\text{abs}}]$,</span>"""
        r"""<span class="ln in2">the expected time to absorption.</span>"""
        r"""<span class="src">Grimmett 6.3; Kemeny–Snell</span>"""},
    32105: {"statement": r"""<b>Gambler's ruin.</b>"""
        r"""<span class="ln">Win each round with prob. $p$, lose with $q=1-p$, start at $i$, stop at $0$ or $N$.</span>"""
        r"""<span class="ln in">Then $a_i=\mathbb P_i(\text{reach }N)=\dfrac{(q/p)^i-1}{(q/p)^N-1}$ for $p\ne q$</span>"""
        r"""<span class="ln in2">(equivalently $\frac{1-(q/p)^i}{1-(q/p)^N}$ for reaching $0$ with the roles swapped),</span>"""
        r"""<span class="ln in">and $a_i=i/N$ for $p=q=\frac12$, where $\mu_i=i(N-i)$.</span>"""
        r"""<span class="src">Ross 4.5; Grimmett 3.9</span>"""},
    32106: {"statement": r"""<b>Pattern waiting times.</b>"""
        r"""<span class="ln">For fair coin tosses, $\mathbb E[T_{HT}]=4$ but $\mathbb E[T_{HH}]=6$.</span>"""
        r"""<span class="ln">In general, for a pattern $W$ of length $k$,</span>"""
        r"""<span class="ln in">$\mathbb E[T_W]=\sum_{j=1}^kc_j2^j$</span>"""
        r"""<span class="ln in">where $c_j=1$ if the first $j$ letters of $W$ equal its last $j$ letters, and $0$ otherwise.</span>"""
        r"""<span class="src">Conway; Grimmett 6.3</span>"""},
}
