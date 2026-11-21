"""DIP Topic 15 (Hough transform) statements, line by line. After this file exists, change a statement only here."""

SUBJECT = "DIP"

FIX = {
    3141: {"statement": r"""<b>Normal form of a line.</b>"""
        r"""<span class="ln">A line in the image plane can be written</span>"""
        r"""<span class="ln in">$\rho=x\cos\theta+y\sin\theta$,</span>"""
        r"""<span class="ln">where $\rho$ is its signed distance from the origin and $\theta$ is the angle of its unit normal $(\cos\theta,\sin\theta)$.</span>"""
        r"""<span class="ln">With $\theta\in[0,\pi)$ and $\rho\in[-D,D]$, $D=\sqrt{M^2+N^2}$ for an $M\times N$ image,</span>"""
        r"""<span class="ln in">every line (including vertical ones) corresponds to exactly one point $(\rho,\theta)$.</span>"""
        r"""<span class="ln">A fixed image point $(x_0,y_0)$ lies on the lines</span>"""
        r"""<span class="ln in">$\rho(\theta)=x_0\cos\theta+y_0\sin\theta$, a sinusoid in the $(\rho,\theta)$ plane.</span>"""},
    3142: {"statement": r"""<b>Hough accumulator voting.</b>"""
        r"""<span class="ln">Quantize the $(\rho,\theta)$ plane into an accumulator array $A[\rho,\theta]$ initialized to zero.</span>"""
        r"""<span class="ln">For each edge pixel $(x_i,y_i)$ and each discrete $\theta$,</span>"""
        r"""<span class="ln in">compute $\rho=x_i\cos\theta+y_i\sin\theta$ and increment $A[\rho,\theta]$.</span>"""
        r"""<span class="ln">Points lying on a common line produce sinusoids meeting at a single cell,</span>"""
        r"""<span class="ln in">so lines correspond to peaks of $A$.</span>"""},
    3143: {"statement": r"""<b>Hough transform for lines.</b>"""
        r"""<span class="ln in">(1) Detect edge pixels (e.g. Canny).</span>"""
        r"""<span class="ln in">(2) For each edge pixel and each discrete $\theta$, compute $\rho$ and increment $A[\rho,\theta]$.</span>"""
        r"""<span class="ln in">(3) Smooth or threshold $A$ and keep the local maxima with $A[\rho,\theta]\ge\tau$.</span>"""
        r"""<span class="ln in">(4) Convert each peak back to a line, optionally clipped to the segment supported by edge pixels.</span>"""
        r"""<span class="ln">Using the gradient direction $\theta=\operatorname{atan2}(f_y,f_x)$ lets each pixel vote for one (or a few) $\theta$ only.</span>"""},
    3144: {"statement": r"""<b>Circle Hough transform.</b>"""
        r"""<span class="ln">A circle $(x-a)^2+(y-b)^2=r^2$ has three parameters $(a,b,r)$,</span>"""
        r"""<span class="ln in">so the accumulator is three-dimensional.</span>"""
        r"""<span class="ln">For a fixed $r$, each edge point votes for the circle of centres of radius $r$ around it.</span>"""
        r"""<span class="ln">With the gradient direction $\theta$ at the edge pixel, the centre lies on that line at distance $r$:</span>"""
        r"""<span class="ln in">$a=x\mp r\cos\theta$, $b=y\mp r\sin\theta$,</span>"""
        r"""<span class="ln in2">with $-$ for a disc darker than its background ($\nabla f$ points outward)</span>"""
        r"""<span class="ln in2">and $+$ for a brighter one ($\nabla f$ points inward).</span>"""
        r"""<span class="ln">Each pixel then votes for one cell per radius, or two if the polarity is unknown.</span>"""},
    3145: {"statement": r"""<b>Generalized Hough transform.</b>"""
        r"""<span class="ln">Training: choose a reference point $c$ for the shape;</span>"""
        r"""<span class="ln in">for each boundary point $p$ with orientation $\phi(p)$, store $r=c-p$ in the R-table entry for $\phi$.</span>"""
        r"""<span class="ln">Detection: for every edge pixel $p$ with orientation $\phi$ and every $r$ in the R-table entry for $\phi$,</span>"""
        r"""<span class="ln in">increment $A[p+r]$.</span>"""
        r"""<span class="ln">The peak of $A$ is the location of the shape's reference point.</span>"""
        r"""<span class="ln">Scale and rotation add dimensions to $A$.</span>"""},
    3146: {"statement": r"""<b>Example.</b>"""
        r"""<span class="ln">The points $(1,1),(2,2),(3,3)$ with $\rho=x\cos\theta+y\sin\theta$.</span>"""
        r"""<span class="ln">At $\theta=0^\circ$: $\rho=1,2,3$, three different cells, so no agreement.</span>"""
        r"""<span class="ln">At $\theta=135^\circ$: $\cos\theta=-\frac{\sqrt2}2$, $\sin\theta=\frac{\sqrt2}2$,</span>"""
        r"""<span class="ln in">so $\rho=\frac{\sqrt2}2(y-x)=0$ for all three points:</span>"""
        r"""<span class="ln in">one cell $(0,135^\circ)$ gets 3 votes.</span>"""
        r"""<span class="ln">The line is $x\cos135^\circ+y\sin135^\circ=0$, i.e. $y=x$.</span>"""},
}
