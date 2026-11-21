"""DIP Topic 02 statements, line by line (one setup, item or conclusion per line)."""

SUBJECT = "DIP"

FIX = {
    3011: {"statement": r"""<b>Trichromacy and Grassmann's laws.</b>"""
        r"""<span class="ln">For normal human vision, any colour stimulus $C$ can be matched by a mixture of three fixed primaries:</span>"""
        r"""<span class="ln in">$C\equiv R\,\mathbf R+G\,\mathbf G+B\,\mathbf B$,</span>"""
        r"""<span class="ln">where $\equiv$ means “looks the same” and an amount may be negative (that primary is then added to the $C$ side).</span>"""
        r"""<span class="ln">Matching is linear (Grassmann):</span>"""
        r"""<span class="ln in">if $C_1\equiv C_2$ then $\alpha C_1\equiv\alpha C_2$ for $\alpha\gt 0$,</span>"""
        r"""<span class="ln in">and $C_1+C_3\equiv C_2+C_3$ for any $C_3$.</span>"""
    },
    3012: {"statement": r"""<b>CIE XYZ tristimulus values.</b>"""
        r"""<span class="ln">The CIE 1931 colour-matching functions $\bar x(\lambda),\bar y(\lambda),\bar z(\lambda)\ge0$ define, for a light with spectral power distribution $P(\lambda)$,</span>"""
        r"""<span class="ln">the tristimulus values</span>"""
        r"""<span class="ln in">$X=\int P(\lambda)\bar x(\lambda)\,d\lambda$,</span>"""
        r"""<span class="ln in">$Y=\int P(\lambda)\bar y(\lambda)\,d\lambda$,</span>"""
        r"""<span class="ln in">$Z=\int P(\lambda)\bar z(\lambda)\,d\lambda$,</span>"""
        r"""<span class="ln">with $\bar y$ equal to the luminous efficiency function, so $Y$ is luminance.</span>"""
    },
    3013: {"statement": r"""<b>CIE chromaticity coordinates.</b>"""
        r"""<span class="ln">For tristimulus values $(X,Y,Z)$ the chromaticity coordinates are</span>"""
        r"""<span class="ln in">$x=\dfrac{X}{X+Y+Z}$, $y=\dfrac{Y}{X+Y+Z}$, $z=1-x-y$.</span>"""
        r"""<span class="ln">The set of $(x,y)$ of monochromatic lights is the spectral locus (a horseshoe);</span>"""
        r"""<span class="ln">the colours reproducible by three primaries are the points inside the triangle of their chromaticities, the gamut,</span>"""
        r"""<span class="ln">and mixtures of two colours lie on the segment joining them.</span>"""
    },
    3014: {"statement": r"""<b>RGB to YCbCr (ITU-R BT.601) and chroma subsampling.</b>"""
        r"""<span class="ln in">$\begin{pmatrix}Y\\C_b\\C_r\end{pmatrix}=\begin{pmatrix}0.299&0.587&0.114\\-0.1687&-0.3313&0.5\\0.5&-0.4187&-0.0813\end{pmatrix}\begin{pmatrix}R\\G\\B\end{pmatrix}$,</span>"""
        r"""<span class="ln">with $128$ added to $C_b,C_r$ for 8-bit storage.</span>"""
        r"""<span class="ln">In 4:2:0 subsampling $Y$ is kept at full resolution</span>"""
        r"""<span class="ln in">while $C_b$ and $C_r$ are each stored at half resolution in both directions.</span>"""
    },
    3015: {"statement": r"""<b>HSI colour model.</b>"""
        r"""<span class="ln">For $R,G,B\in[0,1]$:</span>"""
        r"""<span class="ln in">$I=\frac{R+G+B}{3}$,</span>"""
        r"""<span class="ln in">$S=1-\frac{3\min(R,G,B)}{R+G+B}$,</span>"""
        r"""<span class="ln in">and $H=\theta$ if $B\le G$, $H=360^\circ-\theta$ if $B\gt G$,</span>"""
        r"""<span class="ln in2">where $\theta=\cos^{-1}\!\Big(\frac{\frac12[(R-G)+(R-B)]}{\sqrt{(R-G)^2+(R-B)(G-B)}}\Big)$.</span>"""
        r"""<span class="ln">Hue is undefined when $S=0$, saturation is undefined when $I=0$.</span>"""
    },
    3016: {"statement": r"""<b>Example.</b>"""
        r"""<span class="ln">Convert pure red $(R,G,B)=(255,0,0)$ with the BT.601 matrix:</span>"""
        r"""<span class="ln in">$Y=0.299\cdot255=76.2$,</span>"""
        r"""<span class="ln in">$C_b=-0.1687\cdot255=-43.0$,</span>"""
        r"""<span class="ln in">$C_r=0.5\cdot255=127.5$.</span>"""
        r"""<span class="ln">With the 8-bit offset</span>"""
        r"""<span class="ln in">$C_b=128-43=85$</span>"""
        r"""<span class="ln in">and $C_r=128+127.5=255.5$, clipped to $255$.</span>"""
    },
}
