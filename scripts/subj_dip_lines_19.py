"""DIP Topic 19 (eigenfaces and Viola-Jones) statements, line by line."""

SUBJECT = "DIP"

FIX = {
    3181: {"statement": r"""<b>Eigenfaces (PCA on faces).</b>"""
        r"""<span class="ln">Flatten each aligned $w\times h$ face into $x_i\in\mathbb R^d$, $d=wh$.</span>"""
        r"""<span class="ln">With the mean face $\mu=\frac1N\sum_ix_i$</span>"""
        r"""<span class="ln">and centred vectors $\Phi_i=x_i-\mu$,</span>"""
        r"""<span class="ln in">the covariance is $C=\frac1N\sum_i\Phi_i\Phi_i^T$.</span>"""
        r"""<span class="ln">The eigenvectors of $C$ with the largest eigenvalues, reshaped as images, are the eigenfaces;</span>"""
        r"""<span class="ln">they span the low-dimensional face subspace.</span>"""},
    3182: {"statement": r"""<b>Small-sample trick.</b>"""
        r"""<span class="ln">Let $A=[\Phi_1\cdots\Phi_N]$ be $d\times N$ with $N\ll d$.</span>"""
        r"""<span class="ln">If $A^TAv=\lambda v$ with $\lambda\gt0$,</span>"""
        r"""<span class="ln in">then $AA^T(Av)=\lambda(Av)$,</span>"""
        r"""<span class="ln in">so $u=Av/\|Av\|$ is a unit eigenvector of $C=\frac1NAA^T$ with eigenvalue $\lambda/N$.</span>"""
        r"""<span class="ln">Because the mean is removed, $\operatorname{rank}(C)\le N-1$.</span>"""},
    3183: {"statement": r"""<b>Recognition by projection.</b>"""
        r"""<span class="ln">With $U=[u_1\cdots u_k]$ the top eigenfaces,</span>"""
        r"""<span class="ln in">a face $x$ has weights $\Omega=U^T(x-\mu)$.</span>"""
        r"""<span class="ln">The reconstruction error $\varepsilon=\|(x-\mu)-U\Omega\|$</span>"""
        r"""<span class="ln in">tests whether $x$ is a face at all;</span>"""
        r"""<span class="ln">the identity is $\arg\min_c\|\Omega-\Omega_c\|$ over the stored class weights $\Omega_c$.</span>"""
        r"""<span class="ln">Fisherfaces replace PCA by LDA, maximising between-class over within-class scatter.</span>"""},
    3184: {"statement": r"""<b>Integral image and Haar-like features.</b>"""
        r"""<span class="ln">The integral image</span>"""
        r"""<span class="ln in">$ii(x,y)=\sum_{x'\le x,\,y'\le y}f(x',y')$ is computed in one pass,</span>"""
        r"""<span class="ln">and the sum over any rectangle is</span>"""
        r"""<span class="ln in">$D-B-C+A$ in four lookups,</span>"""
        r"""<span class="ln in">where $D$ is $ii$ at its bottom-right pixel and $B$, $C$, $A$ are $ii$ just above its top-right, just left of its bottom-left and diagonally outside its top-left.</span>"""
        r"""<span class="ln">A Haar-like feature is the difference of adjacent rectangle sums,</span>"""
        r"""<span class="ln in">$\sum_{\rm white}-\sum_{\rm black}$;</span>"""
        r"""<span class="ln">a $24\times24$ window has over $160\,000$ of them.</span>"""},
    3185: {"statement": r"""<b>AdaBoost and the cascade.</b>"""
        r"""<span class="ln">AdaBoost forms</span>"""
        r"""<span class="ln in">$H(x)=\operatorname{sign}\big(\sum_{t=1}^T\alpha_th_t(x)\big)$</span>"""
        r"""<span class="ln">from weak classifiers $h_t$ (a Haar feature and a threshold),</span>"""
        r"""<span class="ln">choosing the one with the least weighted error $\epsilon_t$ each round,</span>"""
        r"""<span class="ln in">with $\alpha_t=\tfrac12\ln\frac{1-\epsilon_t}{\epsilon_t}$ and increased weight on misclassified samples.</span>"""
        r"""<span class="ln">A cascade of such stages rejects a window as soon as any stage says no;</span>"""
        r"""<span class="ln">overall rates multiply:</span>"""
        r"""<span class="ln in">$F=\prod f_i$, $D=\prod d_i$.</span>"""},
    3186: {"statement": r"""<b>Example.</b>"""
        r"""<span class="ln">For $f=\begin{pmatrix}1&2&3\\4&5&6\\7&8&9\end{pmatrix}$</span>"""
        r"""<span class="ln">the integral image is $ii=\begin{pmatrix}1&3&6\\5&12&21\\12&27&45\end{pmatrix}$.</span>"""
        r"""<span class="ln">The bottom-right $2\times2$ block $\{5,6,8,9\}$ sums to $28$ directly,</span>"""
        r"""<span class="ln in">and $ii(3,3)-ii(1,3)-ii(3,1)+ii(1,1)=45-6-12+1=28$ (indices are row, column).</span>"""},
}
