"""StoMA Topic 22 statements, line by line (one hypothesis or conclusion per line; the source on its own small line)."""

SUBJECT = "StoMA"

FIX = {
    32201: {"statement": r"""<b>Birth–death chains.</b>"""
        r"""<span class="ln">A chain on $\{0,1,2,\ldots\}$ moves only $i\to i\pm1$,</span>"""
        r"""<span class="ln in">with $P_{i,i+1}=p_i$ and $P_{i,i-1}=q_i$.</span>"""
        r"""<span class="ln">A stationary $\pi$ satisfies the detailed balance (cut) equations</span>"""
        r"""<span class="ln in">$\pi_ip_i=\pi_{i+1}q_{i+1}$,</span>"""
        r"""<span class="ln in">so $\pi_{i+1}=\frac{p_i}{q_{i+1}}\pi_i$ for all $i\ge0$.</span>"""
        r"""<span class="src">Ross 4.8; Grimmett 6.5</span>"""},
    32202: {"statement": r"""<b>Birth–death invariant law.</b>"""
        r"""<span class="ln">Solving the recursion,</span>"""
        r"""<span class="ln in">$\pi_n=\pi_0\prod_{k=0}^{n-1}\frac{p_k}{q_{k+1}}$ and</span>"""
        r"""<span class="ln in">$\pi_0=\Bigl(1+\sum_{n\ge1}\prod_{k=0}^{n-1}\frac{p_k}{q_{k+1}}\Bigr)^{-1}$.</span>"""
        r"""<span class="ln">An irreducible birth–death chain is positive recurrent iff this sum is finite.</span>"""
        r"""<span class="src">Ross 4.8; Grimmett 6.5</span>"""},
    32203: {"statement": r"""<b>Reversibility and Kolmogorov's criterion.</b>"""
        r"""<span class="ln">An irreducible stationary chain is reversible, $\pi_iP_{ij}=\pi_jP_{ji}$,</span>"""
        r"""<span class="ln in">if and only if for every cycle</span>"""
        r"""<span class="ln in">$P_{i_0i_1}P_{i_1i_2}\cdots P_{i_ki_0}=P_{i_0i_k}\cdots P_{i_2i_1}P_{i_1i_0}$:</span>"""
        r"""<span class="ln">each loop has the same probability in both directions.</span>"""
        r"""<span class="src">Grimmett 6.5; Kelly, Reversibility</span>"""},
    32204: {"statement": r"""<b>Metropolis–Hastings.</b>"""
        r"""<span class="ln">To sample from $\pi\propto\tilde\pi$, propose $y\sim q(\cdot\mid x)$ and accept with</span>"""
        r"""<span class="ln in">$\alpha(x,y)=\min\bigl(1,\frac{\tilde\pi(y)q(x\mid y)}{\tilde\pi(x)q(y\mid x)}\bigr)$.</span>"""
        r"""<span class="ln">Then $\pi(x)q(y\mid x)\alpha(x,y)=\pi(y)q(x\mid y)\alpha(y,x)$,</span>"""
        r"""<span class="ln in">so detailed balance holds and $\pi$ is stationary.</span>"""
        r"""<span class="src">Robert & Casella 7.3; Grimmett 6.14</span>"""},
    32205: {"statement": r"""<b>Random-walk Metropolis.</b>"""
        r"""<span class="ln">With a symmetric proposal, $q(y\mid x)=q(x\mid y)$,</span>"""
        r"""<span class="ln in">the acceptance is $\alpha(x,y)=\min\bigl(1,\frac{\pi(y)}{\pi(x)}\bigr)$.</span>"""
        r"""<span class="ln">The step size trades off acceptance against movement;</span>"""
        r"""<span class="ln in">for Gaussian-like targets in high dimension the optimal acceptance rate is about $23.4\%$.</span>"""
        r"""<span class="src">Roberts–Gelman–Gilks</span>"""},
    32206: {"statement": r"""<b>Gibbs sampling.</b>"""
        r"""<span class="ln">To sample $p(x_1,\ldots,x_d)$, update one coordinate at a time from its full conditional:</span>"""
        r"""<span class="ln in">$X_i^{(t+1)}\sim p(X_i\mid X_{-i}^{(t)})$.</span>"""
        r"""<span class="ln">This is Metropolis–Hastings with proposal $q(y\mid x)=p(y_i\mid x_{-i})$,</span>"""
        r"""<span class="ln in">for which the acceptance probability is $\alpha(x,y)\equiv1$,</span>"""
        r"""<span class="ln in">so every proposal is accepted.</span>"""
        r"""<span class="src">Robert & Casella 10; Grimmett 6.14</span>"""},
}
