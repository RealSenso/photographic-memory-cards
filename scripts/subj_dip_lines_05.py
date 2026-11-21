"""DIP Topic 05 statements, line by line (one setup, item or conclusion per line)."""

SUBJECT = "DIP"

FIX = {
    3041: {"statement": r"""<b>Histogram equalization.</b>"""
        r"""<span class="ln">For a discrete image with $L$ grey levels and normalized histogram $p_r(r_j)$, the equalization transformation is</span>"""
        r"""<span class="ln in">$s_k=T(r_k)=(L-1)\sum_{j=0}^{k}p_r(r_j)$.</span>"""
        r"""<span class="ln">It is monotonically non-decreasing and maps $[0,L-1]$ to $[0,L-1]$;</span>"""
        r"""<span class="ln">the transformed image has a histogram that is approximately uniform.</span>"""},
    3042: {"statement": r"""<b>Equalization gives a uniform density (probability integral transform).</b>"""
        r"""<span class="ln">Let $r\in[0,L-1]$ have a continuous density $p_r$ with strictly increasing CDF,</span>"""
        r"""<span class="ln">and let $s=T(r)=(L-1)\int_0^r p_r(w)\,dw$.</span>"""
        r"""<span class="ln">Then $s$ is uniformly distributed on $[0,L-1]$:</span>"""
        r"""<span class="ln in">$p_s(s)=\frac1{L-1}$.</span>"""},
    3043: {"statement": r"""<b>Discrete equalization.</b>"""
        r"""<span class="ln">Given an $M\times N$ image with $n_j$ pixels at level $r_j$:</span>"""
        r"""<span class="ln in">(1) compute $p_r(r_j)=n_j/MN$;</span>"""
        r"""<span class="ln in">(2) accumulate the cumulative sums $\sum_{j\le k}p_r(r_j)$;</span>"""
        r"""<span class="ln in">(3) set $s_k=\operatorname{round}\!\big[(L-1)\sum_{j\le k}n_j/MN\big]$;</span>"""
        r"""<span class="ln in">(4) replace each pixel of level $r_k$ by $s_k$.</span>"""
        r"""<span class="ln">The mapping is monotone, may merge levels, and cannot create levels with no input pixels.</span>"""},
    3044: {"statement": r"""<b>Histogram specification (matching).</b>"""
        r"""<span class="ln">Given an input with equalizing map $s=T(r)=(L-1)\sum p_r$ and a desired density $p_z$ with $G(z)=(L-1)\sum p_z$:</span>"""
        r"""<span class="ln in">compute $T$;</span>"""
        r"""<span class="ln in">compute $G$;</span>"""
        r"""<span class="ln in">for each $r$ output $z=G^{-1}\big(T(r)\big)$ (for a staircase $G$, the $z$ whose $G(z)$ is closest to $s$).</span>"""
        r"""<span class="ln">The result has a histogram close to $p_z$.</span>"""},
    3045: {"statement": r"""<b>Local equalization and CLAHE.</b>"""
        r"""<span class="ln">Local histogram equalization divides the image into tiles and equalizes each tile separately.</span>"""
        r"""<span class="ln">Contrast-limited adaptive HE (CLAHE) clips each tile's histogram at a limit $\beta$:</span>"""
        r"""<span class="ln in">$h_{\rm clip}(k)=\min(h(k),\beta)$,</span>"""
        r"""<span class="ln in">redistributes the total excess $\sum_k(h(k)-\beta)^+$ uniformly over all bins,</span>"""
        r"""<span class="ln in">equalizes with the clipped histogram,</span>"""
        r"""<span class="ln in">and bilinearly interpolates between neighbouring tiles' mappings to remove tile seams.</span>"""},
    3046: {"statement": r"""<b>Example.</b>"""
        r"""<span class="ln">A 3-bit image ($L=8$) with $4096$ pixels has $p_r=(0.19,0.25,0.21,0.16,0.08,0.06,0.03,0.02)$.</span>"""
        r"""<span class="ln in">The cumulative sums are $0.19,0.44,0.65,0.81,0.89,0.95,0.98,1.00$;</span>"""
        r"""<span class="ln in">times 7 they give $1.33,3.08,4.55,5.67,6.23,6.65,6.86,7$;</span>"""
        r"""<span class="ln in">rounded: $r=0,\dots,7\mapsto1,3,5,6,6,7,7,7$.</span>"""
        r"""<span class="ln">The output uses five distinct levels $\{1,3,5,6,7\}$.</span>"""},
}
