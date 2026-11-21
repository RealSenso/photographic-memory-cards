"""DIP Topic 03 statements, line by line (one setup, item or conclusion per line)."""

SUBJECT = "DIP"

FIX = {
    3021: {"statement": r"""<b>Image histogram.</b>"""
        r"""<span class="ln">For a digital image of size $M\times N$ with gray levels $r_0,\dots,r_{L-1}$,</span>"""
        r"""<span class="ln">the histogram is $h(r_k)=n_k$, the number of pixels with level $r_k$,</span>"""
        r"""<span class="ln">and the normalized histogram $p(r_k)=n_k/MN$ estimates the probability of level $r_k$,</span>"""
        r"""<span class="ln in">with $\sum_{k=0}^{L-1}p(r_k)=1$.</span>"""
        r"""<span class="ln">The histogram carries no spatial information.</span>"""
    },
    3022: {"statement": r"""<b>Point (intensity) transformation.</b>"""
        r"""<span class="ln">A point operation replaces each pixel value $r$ by $s=T(r)$, with the same function $T$ for every pixel and independent of neighbours.</span>"""
        r"""<span class="ln">Standard choices on $[0,L-1]$:</span>"""
        r"""<span class="ln in">negative $s=L-1-r$;</span>"""
        r"""<span class="ln in">log $s=c\log(1+r)$;</span>"""
        r"""<span class="ln in">power law $s=c\,r^{\gamma}$ ($\gamma\lt1$ brightens, $\gamma\gt1$ darkens);</span>"""
        r"""<span class="ln in">contrast stretching $s=\frac{r-r_{\min}}{r_{\max}-r_{\min}}(L-1)$.</span>"""
    },
    3023: {"statement": r"""<b>Global thresholding (iterative).</b>"""
        r"""<span class="ln">To segment an image $f$ whose histogram has two modes:</span>"""
        r"""<span class="ln in">choose an initial $T$ (the mean of $f$);</span>"""
        r"""<span class="ln in">split pixels into $G_1=\{f\gt T\}$ and $G_2=\{f\le T\}$;</span>"""
        r"""<span class="ln in">compute their means $\mu_1,\mu_2$;</span>"""
        r"""<span class="ln in">set $T\leftarrow\frac12(\mu_1+\mu_2)$;</span>"""
        r"""<span class="ln in">repeat until $T$ changes by less than a tolerance.</span>"""
        r"""<span class="ln">Then $g(x,y)=1$ if $f(x,y)\gt T$ and $0$ otherwise.</span>"""
    },
    3024: {"statement": r"""<b>Otsu's method.</b>"""
        r"""<span class="ln">For a normalized histogram $p_i$ and a trial threshold $k$,</span>"""
        r"""<span class="ln">let $\omega_0(k)=\sum_{i\le k}p_i$, $\omega_1=1-\omega_0$, with class means $\mu_0(k),\mu_1(k)$.</span>"""
        r"""<span class="ln">The between-class variance is $\sigma_B^2(k)=\omega_0\omega_1(\mu_0-\mu_1)^2$.</span>"""
        r"""<span class="ln">Otsu's threshold is $k^*=\arg\max_k\sigma_B^2(k)$,</span>"""
        r"""<span class="ln in">which also minimizes the within-class variance because the total variance is fixed.</span>"""
    },
    3025: {"statement": r"""<b>Otsu with cumulative sums.</b>"""
        r"""<span class="ln">Let $\omega(k)=\sum_{i\le k}p_i$, $\mu(k)=\sum_{i\le k}i\,p_i$ and $\mu_T=\mu(L-1)$.</span>"""
        r"""<span class="ln in">Then $\sigma_B^2(k)=\dfrac{[\mu_T\,\omega(k)-\mu(k)]^2}{\omega(k)\,[1-\omega(k)]}$ for $0\lt\omega(k)\lt1$,</span>"""
        r"""<span class="ln">so all $L$ values are computed in one pass,</span>"""
        r"""<span class="ln in">and $k^*=\arg\max_k\sigma_B^2(k)$;</span>"""
        r"""<span class="ln">if several $k$ tie, their average is taken.</span>"""
    },
    3026: {"statement": r"""<b>Example.</b>"""
        r"""<span class="ln">A 10-pixel image has grey levels $1,1,1,1,2,6,6,7,7,7$, so $\mu_T=3.9$.</span>"""
        r"""<span class="ln">At $k=2$:</span>"""
        r"""<span class="ln in">$\omega_0=\omega_1=0.5$, $\mu_0=1.2$, $\mu_1=6.6$</span>"""
        r"""<span class="ln in">and $\sigma_B^2(2)=0.5\cdot0.5\,(6.6-1.2)^2=7.29$,</span>"""
        r"""<span class="ln in">while $\sigma_B^2(1)\approx5.6$ and $\sigma_B^2(6)\approx4.1$.</span>"""
        r"""<span class="ln">Levels 3, 4, 5 are empty, so $k=2,3,4,5$ all give 7.29 and the threshold reported is the middle, about 3.5.</span>"""
    },
}
