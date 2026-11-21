"""DIP Topic 18 (bag of visual words) statements, line by line."""

SUBJECT = "DIP"

FIX = {
    3171: {"statement": r"""<b>Bag of visual words (BoVW).</b>"""
        r"""<span class="ln">An image $f$ is described by the multiset of its local descriptors $\{d_1,\dots,d_n\}$ (e.g. SIFT).</span>"""
        r"""<span class="ln">Each descriptor is replaced by the index $w(d_i)\in\{1,\dots,K\}$ of its nearest codeword in a learned vocabulary,</span>"""
        r"""<span class="ln">and the image is represented by the histogram</span>"""
        r"""<span class="ln in">$\mathbf h\in\mathbb N^K$, $h_k=\#\{i:w(d_i)=k\}$.</span>"""
        r"""<span class="ln">The representation discards the spatial arrangement of the descriptors.</span>"""},
    3172: {"statement": r"""<b>Visual vocabulary by $k$-means.</b>"""
        r"""<span class="ln">Collect descriptors from many training images and cluster them into $K$ groups by minimizing</span>"""
        r"""<span class="ln in">$\sum_i\min_k\|d_i-\mu_k\|^2$.</span>"""
        r"""<span class="ln">Lloyd's algorithm alternates</span>"""
        r"""<span class="ln in">(1) assign each $d_i$ to its nearest centroid,</span>"""
        r"""<span class="ln in">and (2) update $\mu_k\leftarrow\frac1{|S_k|}\sum_{d_i\in S_k}d_i$,</span>"""
        r"""<span class="ln">until the assignments stop changing.</span>"""
        r"""<span class="ln">The centroids $\mu_k$ are the visual words (the codebook).</span>"""},
    3173: {"statement": r"""<b>Histogram encoding.</b>"""
        r"""<span class="ln">Hard assignment maps each descriptor to</span>"""
        r"""<span class="ln in">$k(i)=\arg\min_k\|d_i-\mu_k\|$;</span>"""
        r"""<span class="ln">the image signature is</span>"""
        r"""<span class="ln in">$h_k=\sum_{i=1}^n\mathbf 1[k(i)=k]$,</span>"""
        r"""<span class="ln">normalized as $\hat{\mathbf h}=\mathbf h/\|\mathbf h\|_1$ (or $\|\cdot\|_2$)</span>"""
        r"""<span class="ln in">so that images with different numbers of keypoints are comparable.</span>"""
        r"""<span class="ln">(Soft assignment distributes each vote over several near words.)</span>"""
        r"""<span class="ln">Signatures are compared by cosine similarity, histogram intersection or $\chi^2$ distance.</span>"""},
    3174: {"statement": r"""<b>TF-IDF weighting and the inverted index.</b>"""
        r"""<span class="ln">For a word $i$ in document (image) $d$ among $N$ database images:</span>"""
        r"""<span class="ln in">$w_i=\underbrace{\dfrac{n_{id}}{n_d}}_{\rm tf}\cdot\underbrace{\log\dfrac N{n_i}}_{\rm idf}$,</span>"""
        r"""<span class="ln">where $n_{id}$ is the number of occurrences of word $i$ in $d$,</span>"""
        r"""<span class="ln in">$n_d$ the number of words in $d$</span>"""
        r"""<span class="ln in">and $n_i$ the number of images containing word $i$.</span>"""
        r"""<span class="ln">An inverted index maps each visual word to the list of images containing it,</span>"""
        r"""<span class="ln in">so a query visits only images sharing at least one word.</span>"""},
    3175: {"statement": r"""<b>Spatial pyramid matching.</b>"""
        r"""<span class="ln">Partition the image into $2^l\times2^l$ cells for $l=0,1,2$ ($1$, $4$ and $16$ cells)</span>"""
        r"""<span class="ln">and compute a BoVW histogram of $K$ words in each cell.</span>"""
        r"""<span class="ln">The descriptor is the concatenation</span>"""
        r"""<span class="ln in">$\mathbf H=\big[\mathbf h^{(0)},\mathbf h^{(1)}_{1..4},\mathbf h^{(2)}_{1..16}\big]$</span>"""
        r"""<span class="ln">of dimension $K\sum_{l}4^l=21K$,</span>"""
        r"""<span class="ln">with finer levels given larger weights;</span>"""
        r"""<span class="ln">it is typically classified with a linear SVM or a histogram-intersection kernel.</span>"""},
    3176: {"statement": r"""<b>Example.</b>"""
        r"""<span class="ln">For $\mathbf h_1=(4,2,3,1)$ and $\mathbf h_2=(2,1,1,6)$ over a 4-word vocabulary:</span>"""
        r"""<span class="ln in">$\mathbf h_1\cdot\mathbf h_2=8+2+3+6=19$,</span>"""
        r"""<span class="ln in">$\|\mathbf h_1\|=\sqrt{30}\approx5.477$,</span>"""
        r"""<span class="ln in">$\|\mathbf h_2\|=\sqrt{42}\approx6.481$,</span>"""
        r"""<span class="ln in">so $\cos\theta=\dfrac{19}{5.477\times6.481}\approx0.535$ ($\theta\approx58^\circ$).</span>"""
        r"""<span class="ln">Cosine similarity ignores vector length.</span>"""},
}
