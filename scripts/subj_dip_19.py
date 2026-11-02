"""DIP topic 19 (eigenfaces, Viola-Jones). Everyday picture: a street camera on a pole spotting passers-by."""
from street_lib import *

SUBJECT = "DIP"

def face(x, y, s=1, fill="#ffffff"):
    return [C(x, y, 10 * s, fill, 1), C(x - 3.5 * s, y - 2 * s, 1.2 * s), C(x + 3.5 * s, y - 2 * s, 1.2 * s), L(x, y - 1 * s, x, y + 2 * s, .6), L(x - 3 * s, y + 5 * s, x + 3 * s, y + 5 * s, .8)]

def d3181(c):
    out = face(30, 36) + [N(30, 62, "w × h pixels", 6.5), arrow(46, 36, 62, 36, 1), N(54, 30, "flatten", 6, "middle")]
    for i in range(6): out.append(R(70, 18 + i * 8, 14, 7, "#f1f5f9", .7))
    out += [N(77, 72, "x ∈ ℝᵈ", 7.5), N(96, 40, "− μ", 8), R(116, 14, 120, 78, "#ffffff", 1)]
    for (x, y) in ((140, 56), (150, 50), (160, 44), (170, 38), (180, 32), (190, 28), (145, 42), (165, 56), (185, 48)): out.append(C(x, y, 1.6))
    out += [L(130, 70, 214, 22, .9), N(196, 22, "face subspace", 6.5, "start"), N(176, 86, "ℝᵈ, d = 10 000", 6.5),
            N(120, 108, "Φᵢ = xᵢ − μ ,   C = (1/N) Σ Φᵢ Φᵢᵀ", 8), N(120, 122, "directions of largest variance = eigenfaces", 7.5), N(120, 136, "align and size-normalise first", 7.5)]
    return svg(c, *out)

def d3182(c):
    return svg(c,
        R(12, 14, 98, 56, "#f1f5f9", 1), N(61, 30, "C = AAᵀ / N", 8), N(61, 44, "d × d", 8), N(61, 58, "10⁴ × 10⁴ : too big", 6.5),
        R(130, 14, 98, 56, "#ffffff", 1), N(179, 30, "AᵀA", 8), N(179, 44, "N × N", 8), N(179, 58, "small: solve this", 6.5),
        arrow(110, 42, 130, 42, 1), N(120, 36, "swap", 5.5, "middle"),
        N(120, 90, "AᵀA v = λ v  ⇒  AAᵀ (A v) = λ (A v)", 8), N(120, 104, "u = A v / ‖A v‖  is an eigenvector of C", 7.5),
        N(120, 118, "rank C ≤ N − 1  (mean removed)", 7.5), N(120, 132, "u = Av is not unit length: divide by ‖Av‖", 7))

def d3183(c):
    out = face(26, 34) + [N(26, 56, "x", 7.5), arrow(42, 34, 58, 34, 1), N(50, 28, "Uᵀ(x−μ)", 5.5, "middle")]
    for i, v in enumerate((9, 5, 7, 2, 4)): out.append(R(64 + i * 11, 44 - v * 3.6, 8, v * 3.6, "#d9dee7", .8))
    out += [N(88, 54, "Ω (k numbers)", 6.5), arrow(120, 34, 136, 34, 1), N(128, 28, "U Ω", 6, "middle")]
    out += face(160, 34) + [N(160, 56, "x̂ (rebuilt)", 6.5), N(206, 30, "ε = ‖x−μ−UΩ‖", 6.5, "middle"), N(206, 42, "small ⇒ a face", 6.5, "middle"),
            N(120, 80, "who:  argmin_c ‖Ω − Ω_c‖  (nearest stored person)", 7.5), N(120, 96, "is it a face:  ε small ?", 7.5), N(120, 112, "need both: a cat can land near a known Ω", 7.5), N(120, 128, "Fisherfaces (LDA): between / within scatter", 7.5)]
    return svg(c, *out)

def d3184(c):
    out = [R(12, 12, 100, 70, "#ffffff", 1)]
    for i, v in enumerate(("A", "B", "C", "D")):
        pass
    out += [R(40, 30, 42, 28, "#d9dee7", .9), N(30, 24, "A", 7.5), N(92, 24, "B", 7.5), N(30, 68, "C", 7.5), N(92, 68, "D", 7.5),
            N(61, 46, "rect", 7), N(130, 16, "ii(x,y) = Σ f(x′,y′)", 7, "start"),
            N(190, 36, "Σ = D − B − C + A", 8), N(190, 50, "four lookups", 7.5), N(190, 62, "any size", 7.5)]
    out += [R(124, 72, 28, 14, "#f1f5f9", .8), R(152, 72, 28, 14, "#33384a", .8), R(188, 72, 14, 14, "#f1f5f9", .8), R(202, 72, 14, 14, "#33384a", .8), R(216, 72, 14, 14, "#f1f5f9", .8),
            N(120, 104, "Haar feature = Σ white − Σ black", 8), N(120, 118, "24 × 24 window: over 160 000 features", 7.5), N(120, 132, "ii: each costs about four reads", 7.5)]
    return svg(c, *out)

def d3185(c):
    out = [N(40, 12, "weak h_t", 7.5)]
    for i in range(3): out += [R(12, 18 + i * 14, 56, 11, "#f1f5f9", .8), N(40, 26 + i * 14, f"h{'₁₂₃'[i]}  α{'₁₂₃'[i]}", 6.5)]
    out += [N(40, 66, "H = sign Σ αₜ hₜ", 7), arrow(72, 40, 88, 40, 1)]
    for i, lab in enumerate(("1", "2", "3")):
        x = 92 + i * 38
        out += [R(x, 28, 28, 24, "#ffffff", 1), N(x + 14, 43, f"stage {lab}", 6.5)]
        if i < 2: out.append(arrow(x + 28, 40, x + 38, 40, 1))
        out.append(L(x + 14, 52, x + 14, 66, .8))
        out.append(N(x + 14, 74, "reject", 6, "middle"))
    out += [N(120, 94, "αₜ = ½ ln((1 − εₜ)/εₜ) ;  raise weights of mistakes", 7.5), N(120, 108, "F = Π fᵢ ,  D = Π dᵢ", 8),
            N(120, 122, "10 stages × 50% false hits: 0.5¹⁰ ≈ 0.001", 7.5), N(120, 136, "but D multiplies too: each stage needs ~99.9%", 7)]
    return svg(c, *out)

def d3186(c):
    out = [N(34, 12, "f", 8), N(120, 12, "ii", 8)]
    f = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]; ii = [[1, 3, 6], [5, 12, 21], [12, 27, 45]]
    for r in range(3):
        for k in range(3):
            hl = r > 0 and k > 0
            out += [R(14 + k * 22, 18 + r * 20, 20, 18, "#d9dee7" if hl else "#ffffff", .8), N(24 + k * 22, 30 + r * 20, str(f[r][k]), 8),
                    R(100 + k * 22, 18 + r * 20, 20, 18, "#ffffff", .8), N(110 + k * 22, 30 + r * 20, str(ii[r][k]), 8)]
    out += [arrow(82, 46, 98, 46, 1), N(176, 12, "target {5,6,8,9}", 6.5, "start"), N(176, 28, "= 28 directly", 7.5, "start"), N(176, 46, "ii(3,3) = 45", 7, "start"), N(176, 58, "ii(1,3) = 6", 7, "start"), N(176, 70, "ii(3,1) = 12", 7, "start"),
            N(120, 100, "28 = 45 − 6 − 12 + 1", 9), N(120, 116, "omit the + ii(1,1) and you get 27", 7.5), N(120, 132, "a 100 × 100 box is still four reads", 7.5)]
    return svg(c, *out)

CARDS = {
3181: dict(d=d3181, stmtKind="DEFINITION",
  statement=r"<b>Eigenfaces (PCA on faces).</b> Flatten each aligned $w\times h$ face into $x_i\in\mathbb R^d$, $d=wh$. With the mean face $\mu=\frac1N\sum_ix_i$ and centred vectors $\Phi_i=x_i-\mu$, the covariance is $C=\frac1N\sum_i\Phi_i\Phi_i^T$. The eigenvectors of $C$ with the largest eigenvalues, reshaped as images, are the <i>eigenfaces</i>; they span the low-dimensional face subspace.",
  hint="Why is a 10 000-pixel face really described by only a few dozen numbers?",
  breakdown=[r"<strong>$x_i\in\mathbb R^d$ = a face as one long vector.</strong> Every pixel is one coordinate, so a $100\times100$ crop is a point in 10 000 dimensions."],
  conn=r"<strong>Faces the street camera sees.</strong> Every cropped passer-by has two eyes, a nose and a mouth in the same places, so the crops are all squeezed into a thin slice of the space of all possible pictures.",
  cap="Each face is flattened into a point x in ℝᵈ. After subtracting the mean μ, the cloud of faces lies near a thin subspace, whose axes are the eigenfaces."),
3182: dict(d=d3182, stmtKind="THEOREM",
  statement=r"<b>Small-sample trick.</b> Let $A=[\Phi_1\cdots\Phi_N]$ be $d\times N$ with $N\ll d$. If $A^TAv=\lambda v$ with $\lambda\gt0$, then $AA^T(Av)=\lambda(Av)$, so $u=Av/\|Av\|$ is a unit eigenvector of $C=\frac1NAA^T$ with eigenvalue $\lambda/N$. Because the mean is removed, $\operatorname{rank}(C)\le N-1$.",
  hint="How do you find the eigenvectors of a 10 000 × 10 000 matrix without ever building it?",
  breakdown=[r"<strong>$A^TAv=\lambda v$ = the small problem.</strong> An $N\times N$ matrix (one row per training face) is cheap to diagonalise."],
  conn=r"<strong>Few faces, many pixels.</strong> The camera has stored a few hundred faces of 10 000 pixels each. Solving a few hundred by a few hundred problem and then mapping back with $A$ gives the same directions.",
  cap="The huge d × d matrix AAᵀ is replaced by the small N × N matrix AᵀA. Its eigenvector v is mapped to u = Av, then normalised."),
3183: dict(d=d3183, stmtKind="ALGORITHM",
  statement=r"<b>Recognition by projection.</b> With $U=[u_1\cdots u_k]$ the top eigenfaces, a face $x$ has weights $\Omega=U^T(x-\mu)$. The reconstruction error $\varepsilon=\|(x-\mu)-U\Omega\|$ tests whether $x$ is a face at all; the identity is $\arg\min_c\|\Omega-\Omega_c\|$ over the stored class weights $\Omega_c$. Fisherfaces replace PCA by LDA, maximising between-class over within-class scatter.",
  hint="How does the camera decide both 'is this a face?' and 'whose face?' from the same k numbers?",
  breakdown=[r"<strong>$\Omega=U^T(x-\mu)$ = the face as $k$ numbers.</strong> The weight on each eigenface, a compact code such as $k\approx50$."],
  conn=r"<strong>Who just walked past?</strong> The camera projects the crop onto the eigenfaces and looks for the closest known person. If the rebuilt picture is far from the crop, it was not a face at all, perhaps a bag or a dog.",
  cap="The face x is projected to weights Ω, then rebuilt as UΩ. A small error ε says it is a face; the nearest stored Ω_c says whose."),
3184: dict(d=d3184, stmtKind="DEFINITION",
  statement=r"<b>Integral image and Haar-like features.</b> The integral image $ii(x,y)=\sum_{x'\le x,\,y'\le y}f(x',y')$ is computed in one pass, and the sum over any rectangle with corner values $A,B,C,D$ is $D-B-C+A$ in four lookups. A Haar-like feature is the difference of adjacent rectangle sums, $\sum_{\rm white}-\sum_{\rm black}$; a $24\times24$ window has over $160\,000$ of them.",
  hint="How can the camera test 160 000 features on every window in real time?",
  breakdown=[r"<strong>$ii(x,y)$ = the sum of everything above and left.</strong> One pass over the frame fills it in."],
  conn=r"<strong>Dark eyes, bright cheeks.</strong> A face window has a dark band over a bright one. A Haar feature measures exactly that with two rectangle sums, found from four corner lookups each.",
  cap="A rectangle sum equals D − B − C + A from four corners of the integral image. A Haar feature is the white sum minus the black sum."),
3185: dict(d=d3185, stmtKind="ALGORITHM",
  statement=r"<b>AdaBoost and the cascade.</b> AdaBoost forms $H(x)=\operatorname{sign}\big(\sum_{t=1}^T\alpha_th_t(x)\big)$ from weak classifiers $h_t$ (a Haar feature and a threshold), choosing the one with the least weighted error $\epsilon_t$ each round, with $\alpha_t=\tfrac12\ln\frac{1-\epsilon_t}{\epsilon_t}$ and increased weight on misclassified samples. A cascade of such stages rejects a window as soon as any stage says no; overall rates multiply: $F=\prod f_i$, $D=\prod d_i$.",
  hint="Why do most windows of a street frame cost almost nothing to reject?",
  breakdown=[r"<strong>$H=\operatorname{sign}\sum\alpha_th_t$ = a weighted vote.</strong> Each weak feature is barely better than a coin; the weights $\alpha_t$ reward the better ones."],
  conn=r"<strong>Most of the street is not a face.</strong> Road, wall and sky fail the first cheap stage and are dropped at once. Only the few windows that look like faces reach the expensive stages.",
  cap="Weak classifiers h_t with weights α_t are combined into H. Cascade stages 1, 2, 3, … reject most windows early, so the average cost per window is tiny."),
3186: dict(d=d3186, stmtKind="WORKED EXAMPLE",
  statement=r"<b>Example.</b> For $f=\begin{pmatrix}1&2&3\\4&5&6\\7&8&9\end{pmatrix}$ the integral image is $ii=\begin{pmatrix}1&3&6\\5&12&21\\12&27&45\end{pmatrix}$. The bottom-right $2\times2$ block $\{5,6,8,9\}$ sums to $28$ directly, and $ii(3,3)-ii(1,3)-ii(3,1)+ii(1,1)=45-6-12+1=28$.",
  hint="Check the four-corner formula on a 3 × 3 patch you can add up by eye.",
  breakdown=[r"<strong>$ii=\begin{pmatrix}1&3&6\\5&12&21\\12&27&45\end{pmatrix}$ = running sums.</strong> Each cell adds everything above and to its left; the bottom-right is the total 45."],
  conn=r"<strong>A tiny window of the frame.</strong> Nine pixel values stand for a patch of the street. Four lookups give the sum of its bottom-right block without adding the pixels again.",
  cap="Left: the 3 × 3 patch f with the target block shaded. Right: its integral image ii. 45 − 6 − 12 + 1 = 28, the sum of 5, 6, 8, 9."),
}
CARDS[3181]["breakdown"] += [r"<strong>$\mu$ and $\Phi_i=x_i-\mu$ = the average face and each person's difference.</strong> Centring puts the origin at the mean face so variance measures how faces differ.",
                             r"<strong>$C=\frac1N\sum\Phi_i\Phi_i^T$ = the spread of faces.</strong> Its top eigenvectors are the eigenfaces; lighting and pose dominate the pixel variance, so normalise first."]
CARDS[3182]["breakdown"] += [r"<strong>$u=Av$ = map back to pixel space.</strong> Multiplying by $A$ turns a small eigenvector into an eigenvector of the large $C$ with the same eigenvalue.",
                             r"<strong>$\operatorname{rank}C\le N-1$ = at most $N-1$ useful faces.</strong> Normalise $u$ to unit length (it is not automatically) and keep the top $k$."]
CARDS[3183]["breakdown"] += [r"<strong>$\varepsilon=\|(x-\mu)-U\Omega\|$ = is it a face?</strong> What the eigenfaces cannot rebuild; large means the crop is not in the face subspace.",
                             r"<strong>$\arg\min_c\|\Omega-\Omega_c\|$ = whose face?</strong> The nearest stored person in weight space. Fisherfaces use LDA to cope with lighting and pose better."]
CARDS[3184]["breakdown"] += [r"<strong>$D-B-C+A$ = any rectangle in four reads.</strong> Add the big corner, subtract the two overlaps, add back the doubly-subtracted corner. Mind the off-by-one at the border.",
                             r"<strong>$\sum_{\rm white}-\sum_{\rm black}$ = a Haar feature.</strong> Two-, three- and four-rectangle patterns detect edges, lines and diagonals at any scale at the same cost."]
CARDS[3185]["breakdown"] += [r"<strong>$\alpha_t=\tfrac12\ln\frac{1-\epsilon_t}{\epsilon_t}$ = trust in a weak feature.</strong> Low error gives large weight; misclassified windows are then up-weighted, which also selects features.",
                             r"<strong>$F=\prod f_i,\ D=\prod d_i$ = rates multiply.</strong> Ten stages at 50% false hits give $0.5^{10}\approx0.001$, but each stage needs about 99.9% recall to keep $D$ high."]
CARDS[3186]["breakdown"] += [r"<strong>$45-6-12+1$ = inclusion-exclusion.</strong> $ii(3,3)$ is everything; subtract the strip above and the strip to the left, which both contain the corner $ii(1,1)$.",
                             r"<strong>Forgetting $+ii(1,1)$ gives 27.</strong> The corner was removed twice. For a $100\times100$ box it is still four reads instead of 10 000 additions."]

STORY = {
 3181: dict(s="STORY 7 · STEP 13 · A FACE IS A POINT", b="Crops of passers-by lie near a <b>low-dimensional subspace</b>: PCA finds it.",
   f=[["3171", "descriptors and bags"], ["3084", "KLT is PCA"]], n=[["3182", "computing it cheaply"]]),
 3182: dict(s="STORY 7 · STEP 14 · THE SMALL PROBLEM", b="Solve the <b>N × N</b> problem and map back with $A$.",
   f=[["3181", "covariance of faces"]], n=[["3183", "using the eigenfaces"]]),
 3183: dict(s="STORY 7 · STEP 15 · WHO IS IT?", b="Project, rebuild, compare: <b>ε says face, nearest Ω says whose</b>.",
   f=[["3182", "the eigenfaces"]], n=[["3184", "finding faces in the frame"]]),
 3184: dict(s="STORY 7 · STEP 16 · FAST FEATURES", b="The <b>integral image</b> makes every rectangle sum four reads.",
   f=[["3183", "the face test"]], n=[["3185", "choose and chain them"], ["3186", "numbers"]]),
 3185: dict(s="STORY 7 · STEP 17 · BOOST AND CASCADE", b="<b>AdaBoost</b> picks the best features; a <b>cascade</b> rejects non-faces early.",
   f=[["3184", "Haar features"]], n=[["3191", "learned features instead"]]),
 3186: dict(s="STORY 7 · STEP 18 · CHECK BY HAND", b="$45-6-12+1=28$.",
   f=[["3184", "four lookups"]], n=[["3191", "next: deep nets"]]),
}
FIX = build_fix(CARDS)
