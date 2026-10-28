import math
from dip_lib import *

CARDS = []

def _poly(pts, w=1.8, dash=None, fill="none"):
    d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    return P(d, fill=fill, w=w, dash=dash)

def BOX(x, y, w, h, label, fill="#f1f5f9", sz=9, bold=True):
    fw = "bold" if bold else "normal"
    cap = max(4, int(w / (sz * 0.52)))
    if len(label) > cap and " " in label:
        words = label.split(" "); best = None
        for i in range(1, len(words)):
            a, b = " ".join(words[:i]), " ".join(words[i:])
            score = max(len(a), len(b))
            if best is None or score < best[0]: best = (score, a, b)
        _, a, b = best
        return (R(x, y, w, h, fill, 1.6) + N(x + w / 2, y + h / 2 - 1, a, sz, w=fw) + N(x + w / 2, y + h / 2 + sz, b, sz, w=fw))
    return R(x, y, w, h, fill, 1.6) + N(x + w / 2, y + h / 2 + 3, label, sz, w=fw)

# ============================ 18 · BAG OF VISUAL WORDS ============================
def _bag():
    out = [R(10, 18, 100, 80, "#ffffff", 1.6), N(60, 112, "image", 9)]
    pts = [(24, 30), (50, 52), (80, 34), (36, 72), (70, 78), (94, 62)]
    for (x, y) in pts:
        out.append(R(x, y, 14, 14, "#e2e8f0", 1.3))
    out += [L(114, 58, 138, 58, 1.5, ar=True)]
    out += [P("M144 40 Q150 30 162 34 L196 34 Q208 30 214 40 L218 100 Q216 118 180 118 Q146 118 142 100 Z", "#f1f5f9", 1.8),
            N(180, 30, "bag of words", 8.5, w="bold")]
    for i, (lab, x, y) in enumerate([("w₁", 158, 62), ("w₃", 182, 58), ("w₁", 200, 68), ("w₂", 166, 84), ("w₁", 190, 88), ("w₄", 204, 96)]):
        out.append(N(x, y, lab, 10, w="bold"))
    out += [N(180, 134, "layout is discarded", 8.5, w="bold")]
    return out

CARDS.append(card(18, 1, "BAG OF WORDS", "From Text Bags to Visual Bags",
    _bag(),
    "Local patches become 'words' and the image becomes an unordered bag of them",
    ["<strong>Text analogy:</strong> a document is described by <strong>how often each word appears</strong>, ignoring order. Do the same for images by treating <strong>local descriptors as words</strong>.",
     "<strong>How:</strong> detect keypoints, describe each patch (SIFT, 128-D), then replace each descriptor with the <strong>ID of its nearest visual word</strong> (a cluster center from a learned vocabulary).",
     "<strong>Why:</strong> a fixed-length histogram makes images <strong>easy to compare, index, and classify</strong>, and it tolerates viewpoint change and partial occlusion. Cost: all geometry is lost."],
    r"$$I\ \to\ \{d_1,\dots,d_n\}\ \to\ \{w(d_i)\}\ \to\ \mathbf{h}\in\mathbb{N}^{K},\quad h_k=\#\{i:\ w(d_i)=k\}$$",
    "Judging a book by its word counts: 'whale' and 'harpoon' appear a lot, so it's probably about whaling, no matter which chapter says what.",
    "BoVW throws away spatial layout: a face with its eyes and mouth scrambled gets the same histogram. Add spatial pyramids to partly restore position."))

def _kmeans():
    out = [L(20, 124, 226, 124, 1, d="2 3"), L(20, 124, 20, 14, 1, d="2 3")]
    clusters = [((60, 44), [(48, 38), (70, 36), (58, 56), (74, 52), (52, 50), (66, 44)]),
                ((170, 50), [(158, 40), (182, 44), (170, 62), (190, 58), (160, 54), (176, 36)]),
                ((116, 104), [(100, 98), (126, 92), (112, 116), (132, 108), (106, 108), (122, 100)])]
    for (cx, cy), pts in clusters:
        for (x, y) in pts: out.append(C(x, y, 2.2))
        out.append(P(f"M{cx-6} {cy-6} L{cx+6} {cy+6} M{cx-6} {cy+6} L{cx+6} {cy-6}", w=3))
    out += [L(118, 20, 118, 78, 1, d="5 3"), L(118, 78, 24, 118, 1, d="5 3"), L(118, 78, 220, 118, 1, d="5 3"),
            N(60, 20, "w₁", 10, "middle", "bold"), N(180, 20, "w₂", 10, "middle", "bold"), N(116, 136, "w₃", 10, "middle", "bold"),
            N(228, 74, "× = centroid", 8, "end"), N(228, 86, "= visual word", 8, "end")]
    return out

CARDS.append(card(18, 2, "BAG OF WORDS", "Building the Vocabulary with k-Means",
    _kmeans(),
    "Cluster the descriptor cloud; each centroid is a visual word and each cell of the partition is its region",
    ["<strong>What:</strong> collect SIFT descriptors from many training images and <strong>cluster them into $K$ groups</strong> with k-means. Each centroid is a <strong>visual word</strong>; the set of centroids is the <strong>codebook</strong>.",
     "<strong>How:</strong> alternate (1) assign each descriptor to its nearest centroid and (2) move each centroid to the mean of its members, until stable.",
     "<strong>Choosing $K$:</strong> small $K$ merges distinct patches (low discrimination); huge $K$ makes the bags sparse and noisy (over-specific). Typical $K$ ranges from hundreds to $10^6$ with hierarchical k-means for speed."],
    r"$$\min_{\{\mu_k\}}\sum_{i}\min_{k}\|d_i-\mu_k\|^2,\qquad \mu_k\leftarrow\frac{1}{|S_k|}\sum_{d_i\in S_k}d_i$$",
    "Sorting a mountain of buttons into K cups by look: each cup's average button becomes the name of that cup.",
    "k-means gives local optima and depends on the initialization (use k-means++ or several restarts). Also it assumes Euclidean, roughly round clusters."))

CARDS.append(card(18, 3, "BAG OF WORDS", "Histogram Encoding",
    [L(20, 108, 224, 108, 1.2)] + [R(40 + i * 44, 108 - n * 18, 30, n * 18, "#f1f5f9", 1.5) for i, n in enumerate([4, 2, 3, 1])] +
    [N(55 + i * 44, 122, f"w{i+1}", 10, w="bold") for i in range(4)] + [N(55 + i * 44, 108 - n * 18 - 4, str(n), 9, w="bold") for i, n in enumerate([4, 2, 3, 1])] +
    [N(120, 18, "10 patches → 4 words", 9, w="bold"), N(120, 134, "h = (4, 2, 3, 1),  L1-normalized: h/10 = (.4, .2, .3, .1)", 8.5)],
    "Assign every patch to its nearest word and count: the histogram is the image's signature",
    ["<strong>Assignment:</strong> each descriptor $d_i$ is mapped to the <strong>nearest centroid</strong> $k(i)=\\arg\\min_k\\|d_i-\\mu_k\\|$ (hard assignment); soft assignment spreads a vote over several nearby words.",
     "<strong>Counting:</strong> the signature is $h_k=\\#\\{i:k(i)=k\\}$, a length-$K$ histogram, then <strong>normalized</strong> (L1 or L2) so that images with different numbers of patches are comparable.",
     "<strong>Comparison:</strong> use the cosine similarity, histogram intersection or $\\chi^2$ distance between signatures."],
    r"$$h_k=\sum_{i=1}^{n}\mathbb{1}[k(i)=k],\qquad \hat{\mathbf h}=\frac{\mathbf h}{\|\mathbf h\|_1}$$",
    "Tallying the colors of ten marbles into four bins and handing over only the tally: you can compare tallies but not rebuild the marble arrangement.",
    "Normalize before comparing images with different numbers of keypoints; otherwise big, textured images always look 'more similar' to everything."))

CARDS.append(card(18, 4, "BAG OF WORDS", "TF-IDF Weighting & the Inverted Index",
    [L(20, 80, 120, 80, 1.2)] + [R(30 + i * 22, 80 - h, 16, h, "#f1f5f9", 1.4) for i, h in enumerate([60, 32, 20, 10])] +
    [N(38 + i * 22, 94, f"w{i+1}", 8.5) for i in range(4)] + [N(70, 20, "raw counts tf", 8.5, w="bold"),
     L(126, 50, 148, 50, 1.4, ar=True), N(137, 42, "× idf", 9, w="bold"),
     L(130, 80, 226, 80, 1.2)] + [R(140 + i * 22, 80 - h, 16, h, "#e2e8f0", 1.4) for i, h in enumerate([14, 22, 30, 24])] +
    [N(148 + i * 22, 94, f"w{i+1}", 8.5) for i in range(4)] + [N(184, 20, "weighted", 8.5, w="bold"),
     N(120, 112, "w common in every image → idf small", 8.5), N(120, 126, "inverted index: word → list of images", 8.5, w="bold")],
    "Frequent, uninformative words are shrunk; rare, discriminative ones are boosted",
    ["<strong>tf:</strong> how often a word appears in this image. <strong>idf:</strong> $\\log(N/n_i)$, large for words that occur in <strong>few</strong> of the $N$ database images ($n_i$ of them contain word $i$).",
     "<strong>Weight:</strong> $w_i=\\text{tf}_i\\cdot\\text{idf}_i$ <strong>down-weights words that appear everywhere</strong> (like 'the') and emphasizes distinctive ones.",
     "<strong>Fast retrieval:</strong> an <strong>inverted index</strong> maps each visual word to the images containing it, so a query only visits images that share at least one word."],
    r"$$w_i=\underbrace{\frac{n_{id}}{n_d}}_{\text{tf}}\cdot\underbrace{\log\frac{N}{n_i}}_{\text{idf}}$$",
    "In a library search, the word 'the' is useless but 'Heine-Borel' narrows the shelf immediately.",
    "A word present in every image has idf = log(1) = 0, so it is erased entirely. Smooth idf if you must keep it."))

def _spm():
    out = []
    out += [R(10, 24, 56, 56, "#ffffff", 1.6), N(38, 94, "level 0: 1×1", 8)]
    out += [R(86, 24, 56, 56, "#ffffff", 1.6), L(114, 24, 114, 80, 1.2), L(86, 52, 142, 52, 1.2), N(114, 94, "level 1: 2×2", 8)]
    out += [R(162, 24, 56, 56, "#ffffff", 1.6)] + [L(162 + 14 * i, 24, 162 + 14 * i, 80, 1) for i in (1, 2, 3)] + [L(162, 24 + 14 * i, 218, 24 + 14 * i, 1) for i in (1, 2, 3)] + [N(190, 94, "level 2: 4×4", 8)]
    out += [N(120, 116, "concatenate every cell's histogram", 9, w="bold"), N(120, 132, "dimension = K(1 + 4 + 16) = 21K", 8.5)]
    return out

CARDS.append(card(18, 5, "BAG OF WORDS", "Spatial Pyramid Matching",
    _spm(),
    "Histograms are computed per cell at several grid resolutions and concatenated",
    ["<strong>Weakness of plain BoVW:</strong> it ignores <strong>where</strong> words occur, so sky-on-top and sky-on-bottom look the same.",
     "<strong>Fix (SPM):</strong> partition the image into $1\\times1$, $2\\times2$, $4\\times4$ grids and compute a <strong>BoVW histogram per cell</strong>; concatenate them, giving finer levels larger weights.",
     "<strong>Result:</strong> a coarse-to-fine layout descriptor of dimension $K\\sum_l4^l$ ($=21K$ for 3 levels), typically fed to a <strong>linear SVM</strong> or a histogram-intersection kernel."],
    r"$$\mathbf{H}=\big[\,\mathbf{h}^{(0)},\ \mathbf{h}^{(1)}_{1..4},\ \mathbf{h}^{(2)}_{1..16}\big],\qquad \dim=K\,(1+4+16)$$",
    "Instead of one headcount of the whole stadium, count every section separately: you also learn who sits where.",
    "Higher levels have more cells but each cell has fewer patches, so counts are noisier. Weighting finer levels more is a deliberate tradeoff."))

def _cos():
    return [AX(24, 124, 224, 14),
            L(24, 124, 150, 40, 2.4, ar=True), L(24, 124, 60, 30, 2.4, d="5 3", ar=True),
            P("M70 112 A52 52 0 0 0 58 96", w=1.2), N(80, 98, "θ", 10, w="bold"),
            N(156, 34, "h₁ = (4,2,3,1)", 8.5, "start", "bold"), N(66, 26, "h₂ = (2,1,1,6)", 8.5, "start", "bold"),
            N(150, 70, "cos θ = h₁·h₂ / (‖h₁‖‖h₂‖)", 8.5, "start"), N(150, 84, "= 19 / (√30·√42)", 8.5, "start"), N(150, 98, "≈ 0.535", 10, "start", "bold"),
            N(130, 138, "(illustrated in 2-D; real vectors are K-D)", 7.5)]

CARDS.append(card(18, 6, "WORKED BENCHMARK", "Worked Benchmark: Cosine Similarity of Two Histograms",
    _cos(),
    "Dot product 19, norms √30 and √42, so the angle between the signatures gives cos θ ≈ 0.535",
    ["<strong>Two signatures:</strong> $h_1=(4,2,3,1)$ and $h_2=(2,1,1,6)$ over a 4-word vocabulary.",
     "<strong>Dot product:</strong> $4\\cdot2+2\\cdot1+3\\cdot1+1\\cdot6=8+2+3+6=\\mathbf{19}$. <strong>Norms:</strong> $\\|h_1\\|=\\sqrt{30}\\approx5.477$, $\\|h_2\\|=\\sqrt{42}\\approx6.481$.",
     "<strong>Similarity:</strong> $\\cos\\theta=19/(5.477\\times6.481)\\approx\\mathbf{0.535}$ (θ ≈ 58°): moderately dissimilar, because image 2 is dominated by word $w_4$ while image 1 is dominated by $w_1$."],
    r"$$\cos\theta=\frac{\mathbf h_1\!\cdot\!\mathbf h_2}{\|\mathbf h_1\|\,\|\mathbf h_2\|}=\frac{19}{\sqrt{30}\sqrt{42}}\approx0.535$$",
    "Two shopping baskets: the more they overlap in the same kinds of goods, the smaller the angle between them.",
    "Cosine similarity ignores vector length, so a big and a small image with the same word proportions look identical. Often that is exactly what you want."))

# ============================ 19 · EIGENFACES & VIOLA-JONES ============================
def _flat():
    out = [R(10, 22, 68, 68, "#ffffff", 1.6)]
    for i in range(1, 5):
        out += [L(10 + i * 13.6, 22, 10 + i * 13.6, 90, 0.8), L(10, 22 + i * 13.6, 78, 22 + i * 13.6, 0.8)]
    out += [R(36, 40, 16, 16, "#d9dee7", 0.8), N(44, 106, "w × h image", 8.5), L(84, 56, 112, 56, 1.5, ar=True), N(98, 48, "flatten", 8)]
    out += [R(122, 12, 22, 120, "#ffffff", 1.6)] + [L(122, 12 + i * 12, 144, 12 + i * 12, 0.7) for i in range(1, 10)]
    out += [N(133, 142, "x ∈ ℝᵈ", 9), N(190, 40, "d = w·h", 8.5), N(190, 54, "e.g. 100×100", 8.5), N(190, 66, "→ d = 10,000", 8.5),
            N(190, 88, "face = one point", 8.5, w="bold"), N(190, 100, "in ℝᵈ", 8.5, w="bold")]
    return out

CARDS.append(card(19, 1, "EIGENFACES", "A Face is a Point in ℝᵈ",
    _flat(),
    "Stack the pixels of a w×h face into one tall vector; every face becomes one point in d dimensions",
    ["<strong>Represent:</strong> flatten each $w\\times h$ face image into a vector $x\\in\\mathbb{R}^{d}$ with $d=wh$ (e.g. $10{,}000$). Align and size-normalize faces first.",
     r"<strong>Observation:</strong> faces occupy a <strong>tiny low-dimensional subspace</strong> of $\mathbb{R}^d$ (they share structure: two eyes, a nose, a mouth), so most of the $d$ dimensions are wasted.",
     "<strong>Plan:</strong> subtract the <strong>mean face</strong> $\\mu$, then find the directions of maximum variance (PCA): these principal components are the <strong>eigenfaces</strong>."],
    r"$$x_i\in\mathbb{R}^{d},\qquad \mu=\frac1N\sum_i x_i,\qquad \Phi_i=x_i-\mu,\qquad C=\frac1N\sum_i\Phi_i\Phi_i^{T}$$",
    "Filing every person under 10,000 numbers sounds hopeless, but faces cluster so tightly that a few dozen numbers suffice.",
    "Eigenfaces are sensitive to lighting, pose and alignment, which dominate pixel-level variance. Normalize first or the top eigenvectors will model lighting, not identity."))

def _trick():
    return [R(14, 20, 24, 80, "#f1f5f9", 1.6), N(26, 112, "A", 10, w="bold"), N(26, 124, "d × N", 8),
            N(52, 62, "·", 14, w="bold"), R(62, 20, 80, 24, "#f1f5f9", 1.6), N(102, 56, "Aᵀ", 10, w="bold"),
            N(150, 62, "→", 12, w="bold"),
            R(166, 28, 60, 60, "#ffffff", 1.6, 0, "4 3"), N(196, 62, "AAᵀ", 10, w="bold"), N(196, 100, "d × d  (huge)", 8.5),
            R(62, 80, 24, 24, "#e2e8f0", 1.8), N(74, 94, "AᵀA", 7), N(100, 98, "N × N (small)", 8.5, "start", "bold"),
            N(120, 124, "AᵀA v = λ v   ⇒   AAᵀ (A v) = λ (A v)", 9, w="bold"), N(120, 138, "eigenface u = A v", 8.5)]

CARDS.append(card(19, 2, "EIGENFACES", "The Small-Sample Trick (AᵀA vs AAᵀ)",
    _trick(),
    "Eigen-decompose the small N×N matrix and lift the eigenvectors back with A",
    [r"<strong>Problem:</strong> with $A=[\Phi_1\cdots\Phi_N]$ ($d\times N$), the covariance $C=AA^{T}/N$ is $d\times d$ (about $10^4\times10^4$), far too big to eigen-decompose.",
     r"<strong>Trick:</strong> when $N\ll d$, solve the small $N\times N$ problem $A^{T}Av=\lambda v$. Multiply by $A$: $AA^{T}(Av)=\lambda(Av)$, so <strong>$u=Av$ is an eigenvector of $C$ with the same eigenvalue</strong>.",
     "<strong>Rank fact:</strong> $C$ has at most $N-1$ nonzero eigenvalues (the mean was removed), so normalize $u$ to unit length and keep the top $k$ eigenfaces."],
    r"$$A^{T}A\,v_i=\lambda_i v_i\ \Rightarrow\ u_i=\frac{A v_i}{\|A v_i\|},\quad AA^{T}u_i=\lambda_i u_i,\quad \operatorname{rank}(C)\le N-1$$",
    "Instead of interviewing all 10,000 people about a few dozen friends, you interview the few dozen friends and infer everyone else's view.",
    "u = Av is NOT automatically unit length. Divide by its norm. And the eigenvalues of AᵀA and AAᵀ match only for the nonzero ones."))

def _proj():
    return [PG("30,110 168,110 216,66 78,66", "#f1f5f9", 1.6), N(196, 100, "face space", 8.5, "middle", "bold"),
            C(120, 90, 3.5), N(128, 100, "Ωx", 8.5, "start"),
            C(120, 30, 4, "#ffffff"), L(120, 34, 120, 86, 1.4, d="4 3", ar=True), N(130, 56, "ε (distance", 8.5, "start"), N(130, 68, "from face space)", 8.5, "start"),
            C(176, 88, 3.5), C(70, 96, 3.5), L(120, 90, 176, 88, 1, d="2 2"), N(176, 80, "known", 8, "middle"), N(70, 108, "known", 8, "middle"),
            N(46, 24, "Ω = Uᵀ(x − μ)", 9.5, "start", "bold"), N(46, 38, "x̂ = μ + UΩ", 9.5, "start"), N(120, 136, "ε large: not a face;  small ε + near class: match", 8.5, "middle")]

CARDS.append(card(19, 3, "EIGENFACES", "Recognition by Projection & Reconstruction Error",
    _proj(),
    "Project onto face space, then (1) is it near the space? (2) which known face is it near?",
    ["<strong>Project:</strong> weights $\\Omega=U^{T}(x-\\mu)$ with $U=[u_1\\cdots u_k]$: a compact $k$-D code (e.g. $k\\approx50$) for the face.",
     r"<strong>Decide:</strong> (1) reconstruction error $\varepsilon=\|(x-\mu)-U\Omega\|$ says <strong>is this a face at all</strong>; (2) nearest-neighbor distance between $\Omega$ and stored class weights says <strong>whose face</strong>.",
     "<strong>Beyond PCA:</strong> <strong>Fisherfaces (LDA)</strong> maximize between-person variance over within-person variance, which handles lighting/pose variation better than variance-based PCA."],
    r"$$\Omega=U^{T}(x-\mu),\qquad \varepsilon=\|(x-\mu)-U\,\Omega\|,\qquad \text{identity}=\arg\min_c\|\Omega-\Omega_c\|$$",
    "A coat check that compares a short ticket number (weights) rather than the whole coat: a near-miss ticket tells you the coat was probably a different one.",
    "Both tests are needed: a non-face (a cat) can project close to a known face's weights, so check the reconstruction error ε too."))

def _ii():
    return [N(14, 18, "f", 10, "start", w="bold"), GRID(14, 26, [[1, 2, 3], [4, 5, 6], [7, 8, 9]], cell=22, sz=10),
            L(88, 60, 112, 60, 1.4, ar=True), N(100, 52, "Σ", 10),
            N(120, 18, "ii", 10, "start", w="bold"), GRID(120, 26, [[1, 3, 6], [5, 12, 21], [12, 27, 45]], cell=22, sz=10),
            N(120, 112, "ii(x,y) = Σ_{x′≤x, y′≤y} f(x′,y′)", 8.5, "start", "bold"), N(14, 128, "any rectangle sum = 4 look-ups, O(1)", 8.5, "start", "bold")]

CARDS.append(card(19, 4, "VIOLA-JONES", "Integral Image & Haar-like Features",
    _ii(),
    "Every cell of ii holds the sum of all pixels above-left of it, so any rectangle sum needs just four reads",
    ["<strong>Integral image:</strong> $ii(x,y)=\\sum_{x'\\le x,\\,y'\\le y}f(x',y')$ is computed in <strong>one pass</strong>. A rectangle's sum is then $ii(D)-ii(B)-ii(C)+ii(A)$: <strong>four lookups, constant time</strong>, regardless of size.",
     "<strong>Haar-like features</strong> are differences between adjacent rectangle sums (two-rectangle edge, three-rectangle line, four-rectangle diagonal): $f=\\sum_{\\text{white}}-\\sum_{\\text{black}}$.",
     "<strong>Why it matters:</strong> a 24×24 window holds over <strong>160,000</strong> such features; the integral image makes <strong>evaluating every one cheap</strong> at any scale."],
    r"$$ii(x,y)=\sum_{x'\le x}\sum_{y'\le y}f(x',y'),\qquad \text{rect sum}=ii(D)-ii(B)-ii(C)+ii(A)$$",
    "A running odometer for a 2-D map: the distance in any box is the difference of four odometer readings, no matter how big the box.",
    "Inclusion-exclusion needs the four corners just OUTSIDE the rectangle at its top and left edges. Off-by-one at the border is the classic bug."))

def _cascade():
    out = [N(14, 20, "all sub-windows", 8.5, "start", "bold"), L(24, 28, 24, 44, 1.4, ar=True)]
    xs = [20, 78, 136, 194]
    for i, x in enumerate(xs):
        out += [R(x, 46, 40, 30, "#f1f5f9", 1.6), N(x + 20, 65, f"stage {i+1}" if i < 3 else "… N", 9, w="bold")]
        if i < 3: out += [L(x + 40, 61, xs[i + 1], 61, 1.4, ar=True), N(x + 49, 55, "pass", 7.5)]
        out += [L(x + 20, 76, x + 20, 100, 1.3, ar=True), N(x + 20, 112, "reject", 8)]
    out += [L(234, 61, 236, 61, 1, ), N(120, 134, "faces survive all stages; non-faces die early", 8.5, w="bold")]
    return out

CARDS.append(card(19, 5, "VIOLA-JONES", "AdaBoost & the Attentional Cascade",
    _cascade(),
    "Cheap early stages reject most windows; only promising windows reach the expensive stages",
    ["<strong>AdaBoost</strong> builds a <strong>strong classifier</strong> as a weighted vote of many <strong>weak classifiers</strong> (each a single Haar feature plus a threshold): $H(x)=\\operatorname{sign}\\big(\\sum_t\\alpha_th_t(x)\\big)$.",
     "<strong>Boosting step:</strong> pick the weak learner with the lowest weighted error $\\epsilon_t$, set $\\alpha_t=\\tfrac12\\ln\\frac{1-\\epsilon_t}{\\epsilon_t}$, then <strong>raise the weights of misclassified examples</strong> and repeat. This also performs <strong>feature selection</strong> among the 160,000 candidates.",
     "<strong>Cascade:</strong> chain increasingly complex classifiers; <strong>any stage can reject a window immediately</strong>, so the average cost per window is tiny. Early stages are tuned for ≈ 100% recall and ~50% false positives."],
    r"$$H(x)=\operatorname{sign}\!\Big(\sum_{t=1}^{T}\alpha_t h_t(x)\Big),\qquad \alpha_t=\tfrac12\ln\frac{1-\epsilon_t}{\epsilon_t},\qquad F=\prod_i f_i,\ \ D=\prod_i d_i$$",
    "Airport security: a quick glance clears nearly everyone, and only the rare suspicious bag goes through the slow, thorough scan.",
    "Overall false-positive rate is the PRODUCT of per-stage rates, so 10 stages at 50% give 0.5¹⁰ ≈ 0.001. But overall detection rate also multiplies, so each stage needs ~99.9% recall."))

CARDS.append(card(19, 6, "WORKED BENCHMARK", "Worked Benchmark: Rectangle Sum from the Integral Image",
    [N(14, 18, "ii", 10, "start", w="bold"),
     GRID(14, 26, [[1, 3, 6], [5, 12, 21], [12, 27, 45]], cell=26, sz=11, shade={(0, 0), (0, 2), (2, 0), (2, 2)}),
     N(120, 40, "target: bottom-right 2×2", 9, "start", "bold"), N(120, 54, "(values 5, 6, 8, 9)", 8.5, "start"),
     N(120, 74, "sum = ii(3,3) − ii(1,3)", 9, "start"), N(120, 88, "      − ii(3,1) + ii(1,1)", 9, "start"),
     N(120, 106, "= 45 − 6 − 12 + 1", 10, "start", "bold"), N(120, 124, "= 28  ✓ (5+6+8+9)", 10, "start", "bold")],
    "The four shaded corners give the 2×2 sum with no loop over its pixels: 45 − 6 − 12 + 1 = 28",
    ["<strong>Image:</strong> $f=\\begin{pmatrix}1&2&3\\\\4&5&6\\\\7&8&9\\end{pmatrix}$ gives integral image $ii=\\begin{pmatrix}1&3&6\\\\5&12&21\\\\12&27&45\\end{pmatrix}$ (each cell sums everything above-left).",
     "<strong>Target:</strong> the bottom-right $2\\times2$ block $\\{5,6,8,9\\}$, which sums to <strong>28</strong> directly.",
     "<strong>With ii:</strong> $ii(3,3)-ii(1,3)-ii(3,1)+ii(1,1)=45-6-12+1=\\mathbf{28}$. <strong>Four reads</strong> replace four additions here, but for a $100\\times100$ box it is still four reads instead of 10,000."],
    r"$$28=ii(3,3)-ii(1,3)-ii(3,1)+ii(1,1)=45-6-12+1$$",
    "Adding the whole warehouse then subtracting the two strips you don't want, and adding back the corner you subtracted twice.",
    "Don't forget to ADD BACK the corner (inclusion-exclusion): omitting +ii(1,1) gives 27, one too few."))

# ============================ 20 · CNNs ============================
def _conv():
    return [R(10, 28, 70, 70, "#ffffff", 1.6), R(26, 44, 24, 24, "#d9dee7", 1.8), N(45, 22, "input H×W×C", 8.5), N(38, 58, "K×K", 8, w="bold"),
            L(52, 56, 94, 62, 1.3, d="3 3"), N(60, 112, "slide with stride S", 8.5),
            R(96, 40, 44, 44, "#e2e8f0", 1.6), C(112, 56, 3), N(118, 34, "feature map", 8.5), N(118, 98, "H′×W′×F", 8.5),
            N(150, 40, "H′=⌊(H−K+2P)/S⌋+1", 8, "start", "bold"), N(150, 58, "params = K²·C·F + F", 8, "start"), N(150, 76, "shared weights", 8.5, "start"), N(150, 90, "local connectivity", 8.5, "start"), N(150, 104, "translation-equivariant", 8.5, "start")]

CARDS.append(card(20, 1, "CNN BASICS", "The Convolution Layer",
    _conv(),
    "One small kernel is slid across the image; the same weights are reused at every position",
    ["<strong>Local connectivity:</strong> each output neuron looks at only a <strong>$K\\times K$ patch</strong> of the input, not the whole image.",
     "<strong>Weight sharing:</strong> the <strong>same filter</strong> is applied at every location, so the layer detects the same pattern anywhere (translation equivariance) with very few parameters: $K^2CF+F$ for $F$ filters.",
     "<strong>Output size:</strong> $H'=\\lfloor(H-K+2P)/S\\rfloor+1$ with padding $P$ and stride $S$. A fully connected layer on a $224{\\times}224{\\times}3$ image would instead need ~150 thousand weights per neuron."],
    r"$$H'=\left\lfloor\frac{H-K+2P}{S}\right\rfloor+1,\qquad \#\text{params}=K^2\,C_{\text{in}}\,F+F$$",
    "A stamp pressed at every spot on a page: one small carved stamp finds the same shape wherever it appears.",
    "A CNN 'convolution' is really cross-correlation (no kernel flip). It does not change what is learned, but matters if you compare to signal-processing definitions."))

def _rf():
    out = []
    ys = [110, 74, 38]
    for li, y in enumerate(ys):
        n = [9, 5, 3][li]
        xs = [30 + i * (160 / (n - 1)) for i in range(n)]
        for x in xs: out.append(C(x, y, 3.8, "#ffffff"))
        out.append(N(222, y + 3, ["input", "conv 1", "conv 2"][li], 8.5, "end"))
    out += [C(110, 38, 4)]
    for x in [30 + 1 * 40, 30 + 2 * 40, 30 + 3 * 40]:
        out.append(L(110, 38, x, 74, 1.3))
    for cx in [70, 110, 150]:
        for dx in (-20, 0, 20):
            out.append(L(cx, 74, cx + dx, 110, 0.9, d="2 2"))
    out += [N(120, 136, "two 3-tap layers see 5 input pixels", 8.5, w="bold"), N(120, 18, "stack small kernels, see a large context", 8.5)]
    return out

CARDS.append(card(20, 2, "CNN BASICS", "Receptive Field & Pooling",
    _rf(),
    "Each deeper unit sees a wider window of the input",
    ["<strong>Receptive field (RF):</strong> the input region that influences one unit. Stacking $L$ layers of $3\\times3$ stride-1 convolutions gives an RF of $(2L+1)\\times(2L+1)$.",
     "<strong>Pooling</strong> (max or average, e.g. $2\\times2$ stride 2) halves the spatial size, <strong>doubling the RF growth</strong> and adding a little translation invariance; max pooling keeps the strongest response.",
     "<strong>Design rule:</strong> two stacked $3\\times3$ convs give the RF of one $5\\times5$ conv with <strong>fewer parameters</strong> ($2\\cdot9C^2$ vs $25C^2$) and an extra nonlinearity. This is why VGG uses only 3×3 filters."],
    r"$$\text{RF}_l=\text{RF}_{l-1}+(K_l-1)\prod_{i<l}S_i,\qquad 2\cdot(3\!\times\!3)\ \text{conv}\equiv\ 5\!\times\!5\ \text{RF}$$",
    "Pyramid of lookouts: each tier sees a wider horizon because it can ask the tier below for their views.",
    "Stride and pooling multiply the RF growth of every later layer. Count the product of earlier strides, not just kernel sizes."))

def _act():
    relu = [(x, 80 - max(0, (x - 120)) * 0.8) for x in range(30, 211, 4)]
    sig = [(x, 80 - 56 / (1 + math.exp(-(x - 120) / 14)) + 28) for x in range(30, 211, 3)]
    tanh = [(x, 80 - 36 * math.tanh((x - 120) / 28)) for x in range(30, 211, 3)]
    return [L(30, 80, 214, 80, 1, ar=True), L(120, 126, 120, 14, 1, ar=True), _poly(relu, 2.6), _poly(sig, 1.8, "6 3"), _poly(tanh, 1.6, "2 2"),
            N(196, 28, "ReLU", 9, "end", "bold"), N(208, 100, "sigmoid (dashed)", 8.5, "end"), N(208, 112, "tanh (dotted)", 8.5, "end"),
            N(30, 134, "saturates → gradient ≈ 0", 8.5, "start"), N(30, 146, "ReLU: gradient 1 for x > 0", 8.5, "start", "bold")]

CARDS.append(card(20, 3, "CNN BASICS", "Activations & Gradient Flow",
    _act(),
    "Sigmoid and tanh flatten out where gradients vanish; ReLU keeps a unit gradient for positive inputs",
    ["<strong>Why a nonlinearity:</strong> without one, stacked convolutions collapse into a single linear map. Activations let the network model <strong>non-linear</strong> functions.",
     "<strong>ReLU</strong> $\\max(0,x)$ has gradient 1 for $x>0$, so it <strong>does not saturate</strong> and trains deep nets faster; its risk is 'dead' units whose input is always negative. Variants: Leaky ReLU, GELU.",
     "<strong>Sigmoid</strong> has derivative $\\sigma(1-\\sigma)\\le0.25$, so gradients shrink at every layer (<strong>vanishing gradients</strong>); it is kept for output probabilities."],
    r"$$\mathrm{ReLU}(x)=\max(0,x),\quad \sigma'(x)=\sigma(x)(1-\sigma(x))\le\tfrac14,\quad \frac{\partial L}{\partial W_l}=\delta_l\,a_{l-1}^{T}$$",
    "A garden hose: sigmoid pinches the hose at both ends (flow dies), ReLU is a straight open pipe for anything positive.",
    "ReLU's derivative at exactly 0 is undefined (use 0 or 1 by convention). Also initialization (He init) matters, or half the units start dead."))

def _tl():
    out = [L(14, 76, 226, 76, 1.2, ar=True)]
    items = [(30, "LeNet", "1998", "5"), (78, "AlexNet", "2012", "8"), (126, "VGG", "2014", "16-19"), (174, "GoogLeNet", "2014", "22"), (214, "ResNet", "2015", "152")]
    for i, (x, nm, yr, dp) in enumerate(items):
        y = 76
        out += [C(x, y, 4), N(x, y - 14 - (i % 2) * 20, nm, 9, w="bold"), N(x, y + 16, yr, 8.5), N(x, y + 28, dp + " layers", 8)]
    out += [N(120, 126, "3×3 stacks · 1×1 bottlenecks · skip links", 8.5, w="bold"),
            N(120, 140, "ImageNet top-5 error: ~26% (2011) → 3.6% (2015)", 8)]
    return out

CARDS.append(card(20, 4, "ARCHITECTURES", "From LeNet to ResNet",
    _tl(),
    "Each landmark network added one idea that let depth keep paying off",
    ["<strong>LeNet-5 (1998)</strong> established conv + pooling + FC for digits. <strong>AlexNet (2012)</strong> scaled it up with ReLU, dropout and GPUs and won ImageNet by a wide margin.",
     "<strong>VGG (2014)</strong> showed depth with only $3\\times3$ convs; <strong>GoogLeNet/Inception (2014)</strong> used parallel branches and <strong>$1\\times1$ convolutions</strong> to cut parameters.",
     "<strong>ResNet (2015)</strong> added <strong>identity skip connections</strong> that made 50–152-layer networks trainable, giving ImageNet top-5 error of about 3.6% with an ensemble."],
    r"$$\text{depth}:\ 5\ \to\ 8\ \to\ 16\text{–}19\ \to\ 22\ \to\ 152,\qquad 1\times1\ \text{conv: } C_{\text{in}}\to C_{\text{out}}\ \text{channel mixing}$$",
    "Building a taller skyscraper: each generation invented a better elevator (ReLU, 1×1, skip links) so people could actually reach the top floors.",
    "Depth alone did not help until skip connections: plain deeper nets got WORSE training error (the 'degradation problem'), not just worse test error."))

def _res():
    return [N(20, 72, "x", 11, "start", w="bold"), L(30, 68, 52, 68, 1.4, ar=True),
            BOX(54, 50, 44, 36, "conv, BN, ReLU", "#f1f5f9", 8), L(98, 68, 106, 68, 1.4, ar=True),
            BOX(108, 50, 44, 36, "conv, BN", "#f1f5f9", 8), L(152, 68, 170, 68, 1.4, ar=True),
            C(178, 68, 8, "#ffffff"), N(178, 72, "+", 11, w="bold"), L(186, 68, 204, 68, 1.4, ar=True), N(212, 72, "ReLU", 8.5, "start"),
            L(36, 68, 36, 22, 1.5), L(36, 22, 178, 22, 1.5), L(178, 22, 178, 58, 1.5, ar=True), N(108, 16, "identity skip: x", 9, w="bold"),
            N(120, 112, "y = F(x) + x", 11, w="bold"), N(120, 128, "∂y/∂x = ∂F/∂x + I   (gradient highway)", 9)]

CARDS.append(card(20, 5, "ARCHITECTURES", "ResNet: Learn the Residual",
    _res(),
    "The block learns only the change F(x) and adds the input back through an identity shortcut",
    ["<strong>Idea:</strong> instead of learning the full mapping $H(x)$, learn the <strong>residual</strong> $F(x)=H(x)-x$ and output $y=F(x)+x$. If identity is best, the block only has to push $F\\to0$.",
     "<strong>Gradient highway:</strong> $\\dfrac{\\partial y}{\\partial x}=\\dfrac{\\partial F}{\\partial x}+I$, so gradients always have a direct path <strong>back through the $+I$ term</strong>, so they do not vanish with depth.",
     "<strong>Details:</strong> the shortcut is identity when shapes match, or a $1\\times1$ conv when channels or stride change; <strong>bottleneck</strong> blocks (1×1, 3×3, 1×1) keep very deep nets affordable."],
    r"$$y=\mathcal{F}(x,\{W_i\})+x,\qquad \frac{\partial L}{\partial x}=\frac{\partial L}{\partial y}\left(1+\frac{\partial\mathcal F}{\partial x}\right)$$",
    "Editing a draft instead of rewriting it: you only write the corrections, so a perfect draft costs you nothing.",
    "The shortcut and F(x) must have the SAME shape before adding. A mismatch means a 1×1 projection on the shortcut, not on F(x)."))

CARDS.append(card(20, 6, "WORKED BENCHMARK", "Worked Benchmark: ResNet Stem Conv",
    [R(14, 28, 56, 56, "#ffffff", 1.8), N(42, 22, "224 × 224 × 3", 8.5), R(30, 44, 14, 14, "#d9dee7", 1.6), N(36, 98, "7×7, S=2, P=3", 8.5, w="bold"),
     L(76, 56, 112, 56, 1.5, ar=True), R(118, 40, 28, 28, "#e2e8f0", 1.8), N(132, 34, "112×112×64", 8), N(132, 82, "64 filters", 8),
     N(198, 36, "⌊(224 − 7 + 6)/2⌋ + 1", 8.5, "middle", "bold"), N(198, 50, "= ⌊223/2⌋ + 1", 8.5), N(198, 64, "= 111 + 1 = 112", 9, "middle", "bold"),
     N(198, 88, "params = 7·7·3·64 + 64", 8.5, "middle", "bold"), N(198, 102, "= 9,408 + 64 = 9,472", 9, "middle", "bold"),
     N(120, 130, "weights are shared across all positions", 8.5)],
    "224 → 112 spatially, 3 → 64 channels, with only 9,472 parameters",
    ["<strong>Setup:</strong> input $224\\times224\\times3$, kernel $7\\times7$, stride $2$, padding $3$, $F=64$ filters (the ResNet stem).",
     "<strong>Output size:</strong> $\\lfloor(224-7+2\\cdot3)/2\\rfloor+1=\\lfloor223/2\\rfloor+1=111+1=\\mathbf{112}$, so the map is $112\\times112\\times64$.",
     "<strong>Parameters:</strong> $7\\cdot7\\cdot3\\cdot64+64=9{,}408+64=\\mathbf{9{,}472}$. Weight sharing means this count does not depend on the image size."],
    r"$$H'=\left\lfloor\tfrac{224-7+6}{2}\right\rfloor+1=112,\qquad \#\text{params}=7^2\cdot3\cdot64+64=9472$$",
    "A 64-stamp set, each stamp 7×7 across three color layers, stepped two pixels at a time: a small toolbox that scans a whole large photo.",
    "Parameters do NOT depend on H and W. Counting H·W in the parameter total is a common mistake. Also remember +F for the biases."))
