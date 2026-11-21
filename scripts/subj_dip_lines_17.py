"""DIP Topic 17 (SIFT) statements, line by line."""

SUBJECT = "DIP"

FIX = {
    3161: {"statement": r"""<b>Scale space and difference-of-Gaussians pyramid (SIFT).</b>"""
        r"""<span class="ln">The scale space of an image $f$ is $L(x,y,\sigma)=G_\sigma\ast f$.</span>"""
        r"""<span class="ln">The difference-of-Gaussians function is</span>"""
        r"""<span class="ln in">$D(x,y,\sigma)=L(x,y,k\sigma)-L(x,y,\sigma)\approx(k-1)\sigma^2\nabla^2G_\sigma\ast f$,</span>"""
        r"""<span class="ln">computed with $k=2^{1/s}$ so that $\sigma$ doubles over $s$ intervals (an octave).</span>"""
        r"""<span class="ln">After each octave the image is downsampled by 2.</span>"""
        r"""<span class="ln">For $s$ intervals per octave, $s+3$ blurred images are produced, giving $s+2$ DoG images.</span>"""},
    3162: {"statement": r"""<b>SIFT keypoint detection.</b>"""
        r"""<span class="ln">A DoG sample is a candidate keypoint if it is larger or smaller than all 26 neighbours</span>"""
        r"""<span class="ln in">(8 in its own layer, 9 above, 9 below).</span>"""
        r"""<span class="ln">Its position is refined by a quadratic fit,</span>"""
        r"""<span class="ln in">$\hat x=-H_3^{-1}\nabla D$ (sub-pixel and sub-scale),</span>"""
        r"""<span class="ln in">where $H_3$ is the $3\times3$ Hessian of $D$ in $(x,y,\sigma)$;</span>"""
        r"""<span class="ln">candidates with $|D(\hat x)|\lt0.03$ (pixel values in $[0,1]$) are discarded as low contrast;</span>"""
        r"""<span class="ln">and edge-like candidates are rejected unless</span>"""
        r"""<span class="ln in">$\det(H)\gt0$ and $\dfrac{\operatorname{tr}(H)^2}{\det(H)}\lt\dfrac{(r+1)^2}{r}$ with $r=10$ (i.e. $\lt12.1$),</span>"""
        r"""<span class="ln in">where $H$ is the $2\times2$ spatial Hessian of $D$.</span>"""},
    3163: {"statement": r"""<b>SIFT orientation assignment.</b>"""
        r"""<span class="ln">Around each keypoint, at its scale, compute</span>"""
        r"""<span class="ln in">gradient magnitudes $m=\sqrt{L_x^2+L_y^2}$</span>"""
        r"""<span class="ln in">and orientations $\theta=\operatorname{atan2}(L_y,L_x)$</span>"""
        r"""<span class="ln">and accumulate a 36-bin orientation histogram</span>"""
        r"""<span class="ln in">$h[b]=\sum m\cdot G_\sigma\cdot\mathbf 1[\theta\in\text{bin }b]$ (Gaussian-weighted).</span>"""
        r"""<span class="ln">The highest peak (refined by a parabola fit) gives the keypoint orientation,</span>"""
        r"""<span class="ln">and every other peak of at least $80\%$ of it creates an additional keypoint at the same location and scale with that orientation.</span>"""},
    3164: {"statement": r"""<b>SIFT descriptor.</b>"""
        r"""<span class="ln">Take a $16\times16$ window around the keypoint, rotated to the keypoint orientation, scaled to its $\sigma$ and weighted by a Gaussian.</span>"""
        r"""<span class="ln">Divide it into a $4\times4$ grid of cells, each holding an 8-bin gradient orientation histogram (with trilinear interpolation),</span>"""
        r"""<span class="ln in">giving $\mathbf d\in\mathbb R^{4\cdot4\cdot8}=\mathbb R^{128}$.</span>"""
        r"""<span class="ln">Normalize $\mathbf d\leftarrow\mathbf d/\|\mathbf d\|$ (contrast invariance),</span>"""
        r"""<span class="ln in">clip $d_i\leftarrow\min(d_i,0.2)$ (non-linear illumination),</span>"""
        r"""<span class="ln in">and renormalize.</span>"""},
    3165: {"statement": r"""<b>Descriptor matching with Lowe's ratio test.</b>"""
        r"""<span class="ln">For each descriptor $q$ in image A find its nearest neighbour $\mathrm{NN}_1$ and second nearest $\mathrm{NN}_2$ in image B (Euclidean distance).</span>"""
        r"""<span class="ln">Accept the match $q\leftrightarrow\mathrm{NN}_1$</span>"""
        r"""<span class="ln in">only if $\dfrac{\|q-\mathrm{NN}_1\|}{\|q-\mathrm{NN}_2\|}\lt0.8$.</span>"""
        r"""<span class="ln">The remaining matches are verified geometrically,</span>"""
        r"""<span class="ln in">e.g. by fitting an affine transform or homography with RANSAC and keeping the inliers.</span>"""},
    3166: {"statement": r"""<b>Example.</b>"""
        r"""<span class="ln">Ratio test with $d_1=0.3$, $d_2=0.5$:</span>"""
        r"""<span class="ln in">$0.3/0.5=0.6\lt0.8$, accepted.</span>"""
        r"""<span class="ln">With $d_1=0.45$, $d_2=0.5$:</span>"""
        r"""<span class="ln in">$0.45/0.5=0.9\ge0.8$, rejected.</span>"""
        r"""<span class="ln">Numbers to remember:</span>"""
        r"""<span class="ln in">descriptor length $4\cdot4\cdot8=128$;</span>"""
        r"""<span class="ln in">edge-rejection bound $\frac{(r+1)^2}{r}=\frac{11^2}{10}=12.1$ for $r=10$;</span>"""
        r"""<span class="ln in">low-contrast threshold $|D(\hat x)|\lt0.03$.</span>"""
        r"""<span class="ln">Lowe's ratio is stated on distances; on squared distances the equivalent threshold is $0.8^2=0.64$.</span>"""},
}
