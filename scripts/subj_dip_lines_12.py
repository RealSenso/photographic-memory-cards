"""DIP Topic 12 statements, line by line (one setup, item or conclusion per line)."""

SUBJECT = "DIP"

FIX = {
    3111: {"statement": r"""<b>Median filter.</b>"""
        r"""<span class="ln">The median filter replaces each pixel by the median of the grey levels in its neighbourhood $S_{xy}$:</span>"""
        r"""<span class="ln in">$\hat f(x,y)=\operatorname{median}\{f(s,t)\mid(s,t)\in S_{xy}\}$.</span>"""
        r"""<span class="ln">It is non-linear.</span>"""
        r"""<span class="ln">It removes impulse (salt-and-pepper) noise:</span>"""
        r"""<span class="ln in">an isolated extreme value is never the median,</span>"""
        r"""<span class="ln in">and a $K\times K$ median removes impulse groups of fewer than $K^2/2$ pixels.</span>"""},
    3112: {"statement": r"""<b>Edge preservation of the median filter.</b>"""
        r"""<span class="ln">For a step edge, any window centred near the edge contains a majority of pixels from one side,</span>"""
        r"""<span class="ln in">so the median equals that side's value and the step is preserved exactly,</span>"""
        r"""<span class="ln">whereas the mean creates intermediate values:</span>"""
        r"""<span class="ln in">e.g. $\operatorname{median}(2,2,8)=2$, $\operatorname{median}(2,8,8)=8$, $\operatorname{mean}(2,2,8)=4$.</span>"""
        r"""<span class="ln">A signal unchanged by the median filter is a root signal;</span>"""
        r"""<span class="ln in">repeated filtering converges to a root in finitely many steps.</span>"""
        r"""<span class="ln">Thin lines and sharp corners narrower than half the window are removed.</span>"""},
    3113: {"statement": r"""<b>Adaptive median filter.</b>"""
        r"""<span class="ln">At each pixel with window $S_{xy}$ (initially $3\times3$, up to $S_{\max}$)</span>"""
        r"""<span class="ln in">let $z_{\min},z_{\max},z_{\rm med}$ be the minimum, maximum and median in the window and $z_{xy}$ the pixel.</span>"""
        r"""<span class="ln">Level A:</span>"""
        r"""<span class="ln in">if $z_{\min}\lt z_{\rm med}\lt z_{\max}$ go to Level B;</span>"""
        r"""<span class="ln in">otherwise enlarge the window, and if $S_{xy}\le S_{\max}$ repeat A, else output $z_{\rm med}$.</span>"""
        r"""<span class="ln">Level B:</span>"""
        r"""<span class="ln in">if $z_{\min}\lt z_{xy}\lt z_{\max}$ output $z_{xy}$,</span>"""
        r"""<span class="ln in">otherwise output $z_{\rm med}$.</span>"""},
    3114: {"statement": r"""<b>Bilateral filter.</b>"""
        r"""<span class="ln">For an image $f$ and pixel $p$:</span>"""
        r"""<span class="ln in">$BF[f]_p=\frac1{W_p}\sum_{q\in S}G_{\sigma_s}(\|p-q\|)\,G_{\sigma_r}(|f_p-f_q|)\,f_q$,</span>"""
        r"""<span class="ln in">where $G_\sigma$ is a Gaussian and $W_p=\sum_{q}G_{\sigma_s}(\|p-q\|)G_{\sigma_r}(|f_p-f_q|)$ normalizes the weights.</span>"""
        r"""<span class="ln">A neighbour counts only if it is near (spatial term) and similar in value (range term).</span>"""
        r"""<span class="ln">It is non-linear and not separable.</span>"""},
    3115: {"statement": r"""<b>Non-local means.</b>"""
        r"""<span class="ln in">$\hat f(p)=\frac1{Z_p}\sum_{q}w(p,q)\,f(q)$</span>"""
        r"""<span class="ln in">with $w(p,q)=\exp\!\Big(-\frac{\|P_p-P_q\|_2^2}{h^2}\Big)$</span>"""
        r"""<span class="ln in">and $Z_p=\sum_qw(p,q)$,</span>"""
        r"""<span class="ln">where $P_p$ is the patch of pixels centred at $p$ (e.g. $7\times7$) and $h$ is the filtering strength.</span>"""
        r"""<span class="ln">The sum runs over pixels $q$ anywhere in the image (or a large search window), not just near $p$.</span>"""},
    3116: {"statement": r"""<b>Example.</b>"""
        r"""<span class="ln">A $3\times3$ window holds $10,12,200,11,13,9,12,10,11$ (the 200 is a salt pixel).</span>"""
        r"""<span class="ln in">The mean is $288/9=32$;</span>"""
        r"""<span class="ln in">sorted, the values are $9,10,10,11,11,12,12,13,200$</span>"""
        r"""<span class="ln in">and the median (5th of 9) is $11$.</span>"""},
}
