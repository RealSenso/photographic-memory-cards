"""DIP topic 18 (bag of visual words). Everyday picture: a street camera on a pole ("which street is this?")."""
from street_lib import *
import random

SUBJECT = "DIP"

def d3171(c):
    out = [frame(8, 16, 44, 34), building(12, 20, 18, 26, 2, 1, "#f1f5f9"), person(40, 48, 22)]
    for (x, y) in ((16, 24), (34, 30), (22, 40)): out.append(R(x, y, 8, 8, "none", .8, 0, "2 2"))
    out += [N(30, 62, "keypoints", 7), arrow(56, 34, 72, 34, 1), N(64, 28, "SIFT", 6.5),
            N(94, 30, "d₁ … dₙ", 8), N(94, 42, "128-D each", 6.5), arrow(116, 34, 132, 34, 1), N(124, 46, "nearest word", 5.5, "middle"),
            N(150, 30, "w(dᵢ)", 8)]
    for i, v in enumerate((3, 1, 4, 2)): out.append(R(176 + i * 12, 54 - v * 8, 10, v * 8, "#d9dee7", .8))
    out += [arrow(166, 34, 176, 34, 1), N(200, 66, "h ∈ ℕᴷ", 7.5),
            N(120, 92, "I → {dᵢ} → {w(dᵢ)} → h ,  hₖ = #{ i : w(dᵢ) = k }", 8),
            N(120, 108, "like counting words in a text, order ignored", 7.5), N(120, 122, "same-length signature: easy to compare and index", 7.5),
            N(120, 136, "all geometry is lost (scrambled face, same bag)", 7)]
    return svg(c, *out)

def d3172(c):
    random.seed(7)
    cen = [(40, 40), (96, 74), (80, 28)]
    out = [R(10, 12, 130, 96, "#ffffff", 1)]
    for k, (cx, cy) in enumerate(cen):
        for j in range(7):
            x, y = cx + random.uniform(-16, 16), cy + random.uniform(-14, 14)
            out += [C(f(x), f(y), 1.2), L(f(x), f(y), f(cx), f(cy), .3, "1 2")]
        out += [PG(f"{cx - 3},{cy + 3} {cx + 3},{cy + 3} {cx},{cy - 4}", "#7b8494", 1), N(cx + 6, cy - 4, f"μ{'₁₂₃'[k]}", 7, "start")]
    out += [N(75, 120, "every descriptor dᵢ (128-D, drawn flat)", 6.5),
            R(150, 20, 82, 58, "#f1f5f9", 1), N(191, 34, "1 assign dᵢ to", 7), N(191, 45, "nearest μₖ", 7), N(191, 61, "2 move μₖ to the", 7), N(191, 72, "mean of its members", 7),
            N(120, 134, "min Σᵢ minₖ ‖dᵢ − μₖ‖² ;  μₖ ← mean of Sₖ ; centroid = visual word", 6.5)]
    return svg(c, *out)

def d3173(c):
    out = [axes(14, 70, 150, 10), N(232, 82, "word k", 7, "end"), N(10, 12, "hₖ", 7.5, "end")]
    vals = [10, 3, 0, 7, 2, 0, 5, 1]
    for i, v in enumerate(vals):
        out += [R(20 + i * 16, 70 - v * 5, 12, v * 5, "#f1f5f9", .8), N(26 + i * 16, 80, str(i + 1), 6.5)]
    out += [arrow(154, 44, 170, 44, 1), N(162, 38, "÷ ‖h‖₁", 6.5),
            R(172, 22, 56, 48, "#ffffff", 1), N(200, 38, "ĥ = h / ‖h‖₁", 7.5), N(200, 54, "images with", 6.5), N(200, 64, "any n compare", 6.5),
            N(120, 100, "k(i) = argmin ‖dᵢ − μₖ‖  (hard assignment)", 7.5), N(120, 114, "soft: share a vote over a few near words", 7.5),
            N(120, 128, "compare by cosine, histogram intersection or χ²", 7.5), N(120, 141, "normalise first, or big frames match everything", 7)]
    return svg(c, *out)

def d3174(c):
    return svg(c,
        N(70, 12, "inverted index", 7.5), R(10, 18, 120, 70, "#ffffff", 1), L(10, 32, 130, 32, .6), L(54, 18, 54, 88, .6),
        N(32, 28, "word", 7), N(92, 28, "images that contain it", 6.5),
        N(32, 44, "w₇", 7), N(92, 44, "2, 9, 31", 7), N(32, 58, "w₈", 7), N(92, 58, "1, 2, 3, … all", 7), N(32, 72, "w₉", 7), N(92, 72, "5", 7),
        R(144, 22, 88, 56, "#f1f5f9", 1), N(188, 36, "wᵢ = tf · idf", 8), N(188, 50, "tf = nᵢd / n_d".replace("n_d", "n𝒹") if False else "tf = nᵢd / nd", 7), N(188, 62, "idf = log(N / nᵢ)", 7.5), N(188, 74, "rare ⇒ heavy", 7),
        N(120, 106, "a word in every image: idf = log 1 = 0, erased", 7.5), N(120, 120, "a query only visits images that share a word", 7.5),
        N(120, 134, "street signs count more than bricks", 7.5))

def d3175(c):
    out = [N(120, 10, "H = [ h⁽⁰⁾ , h⁽¹⁾₁..₄ , h⁽²⁾₁..₁₆ ]", 8)]
    for lv, (n, x0) in enumerate(((1, 10), (2, 86), (4, 162))):
        s = 64
        out.append(R(x0, 20, s, s, "#ffffff", 1))
        for i in range(1, n):
            out += [L(x0 + i * s / n, 20, x0 + i * s / n, 20 + s, .6), L(x0, 20 + i * s / n, x0 + s, 20 + i * s / n, .6)]
        out.append(N(x0 + s / 2, 96, f"level {lv}: {n * n} cell{'s' if n > 1 else ''}", 7))
    out += [N(120, 112, "dim = K (1 + 4 + 16) = 21 K", 8), N(120, 126, "finer levels get larger weights; fed to a linear SVM", 7.5), N(120, 140, "sky on top ≠ sky on the bottom again", 7.5)]
    return svg(c, *out)

def d3176(c):
    out = [N(10, 12, "h₁ = (4, 2, 3, 1)", 7.5, "start"), N(130, 12, "h₂ = (2, 1, 1, 6)", 7.5, "start")]
    for i, v in enumerate((4, 2, 3, 1)): out += [R(12 + i * 24, 60 - v * 8, 18, v * 8, "#f1f5f9", .8), N(21 + i * 24, 70, f"w{'₁₂₃₄'[i]}", 7)]
    for i, v in enumerate((2, 1, 1, 6)): out += [R(132 + i * 24, 60 - v * 6, 18, v * 6, "#d9dee7", .8), N(141 + i * 24, 70, f"w{'₁₂₃₄'[i]}", 7)]
    out += [N(120, 88, "h₁·h₂ = 8 + 2 + 3 + 6 = 19", 8), N(120, 102, "‖h₁‖ = √30 ≈ 5.477 ,  ‖h₂‖ = √42 ≈ 6.481", 7.5),
            N(120, 118, "cos θ = 19 / (5.477 × 6.481) ≈ 0.535  (θ ≈ 58°)", 8), N(120, 133, "image 1 is w₁-heavy, image 2 is w₄-heavy", 7.5)]
    return svg(c, *out)

CARDS = {
3171: dict(d=d3171, stmtKind="DEFINITION",
  statement=r"<b>Bag of visual words (BoVW).</b> An image $I$ is described by the multiset of its local descriptors $\{d_1,\dots,d_n\}$ (e.g. SIFT). Each descriptor is replaced by the index $w(d_i)\in\{1,\dots,K\}$ of its nearest codeword in a learned vocabulary, and the image is represented by the histogram $\mathbf h\in\mathbb N^K$, $h_k=\#\{i:w(d_i)=k\}$. The representation discards the spatial arrangement of the descriptors.",
  hint="How can a street frame be summarised as a count of words, the way a book is summarised by word counts?",
  breakdown=[r"<strong>$\{d_1,\dots,d_n\}$ = the patches the camera sees.</strong> Each keypoint on the frame gives one 128-number description, one 'word' in the raw."],
  conn=r"<strong>Which street is this?</strong> The camera finds patches of the shop sign, a lamp, a bus, a window and counts how often each kind of patch appears. Two frames of the same street have similar counts, even if the bus has moved.",
  cap="A frame gives keypoints, each described by SIFT (dᵢ). Each is replaced by the nearest visual word w(dᵢ) and counted in a histogram h ∈ ℕᴷ."),
3172: dict(d=d3172, stmtKind="ALGORITHM",
  statement=r"<b>Visual vocabulary by $k$-means.</b> Collect descriptors from many training images and cluster them into $K$ groups by minimizing $\sum_i\min_k\|d_i-\mu_k\|^2$. Lloyd's algorithm alternates (1) assign each $d_i$ to its nearest centroid, and (2) update $\mu_k\leftarrow\frac1{|S_k|}\sum_{d_i\in S_k}d_i$, until the assignments stop changing. The centroids $\mu_k$ are the visual words (the codebook).",
  hint="How are the 'words' of the street vocabulary chosen in the first place?",
  breakdown=[r"<strong>$\min_k\|d_i-\mu_k\|^2$ = each descriptor goes to its nearest word.</strong> The squared distance to the closest centroid is how badly that word describes the patch."],
  conn=r"<strong>Learning the street's words.</strong> Thousands of patches from many frames are sorted into piles by similarity; each pile's average is a word, such as 'lamp-post top', 'window corner' or 'tyre edge'.",
  cap="Descriptors (dots) are grouped around centroids μ₁, μ₂, μ₃. Each centroid moves to the mean of its group; the centroids are the visual words."),
3173: dict(d=d3173, stmtKind="DEFINITION",
  statement=r"<b>Histogram encoding.</b> Hard assignment maps each descriptor to $k(i)=\arg\min_k\|d_i-\mu_k\|$; the image signature is $h_k=\sum_{i=1}^n\mathbf 1[k(i)=k]$, normalized as $\hat{\mathbf h}=\mathbf h/\|\mathbf h\|_1$ (or $\|\cdot\|_2$) so that images with different numbers of keypoints are comparable. (Soft assignment distributes each vote over several near words.) Signatures are compared by cosine similarity, histogram intersection or $\chi^2$ distance.",
  hint="Why must you divide the histogram by its total before comparing two frames?",
  breakdown=[r"<strong>$k(i)=\arg\min\|d_i-\mu_k\|$ = the patch's word.</strong> The nearest centroid; soft assignment would share the vote among a few close ones."],
  conn=r"<strong>Counting words in a frame.</strong> A busy daytime frame has hundreds of patches, a dark night frame only a few. Dividing by the total turns both into proportions, so they can be compared.",
  cap="The counts hₖ of each visual word k in the frame form a histogram; dividing by ‖h‖₁ gives ĥ, comparable across frames with different numbers of keypoints."),
3174: dict(d=d3174, stmtKind="ALGORITHM",
  statement=r"<b>TF-IDF weighting and the inverted index.</b> For a word $i$ in document (image) $d$ among $N$ database images: $w_i=\underbrace{\dfrac{n_{id}}{n_d}}_{\rm tf}\cdot\underbrace{\log\dfrac N{n_i}}_{\rm idf}$, where $n_{id}$ is the number of occurrences of word $i$ in $d$, $n_d$ the number of words in $d$ and $n_i$ the number of images containing word $i$. An inverted index maps each visual word to the list of images containing it, so a query visits only images sharing at least one word.",
  hint="Why should a word that appears in every street frame count for nothing?",
  breakdown=[r"<strong>$n_{id}/n_d$ = how often the word occurs here.</strong> The term frequency: a word that fills the frame matters more."],
  conn=r"<strong>Searching a library of street frames.</strong> The bus-stop sign appears in few frames and says a lot; the grey road texture appears in all of them and says nothing. The index jumps straight to the frames that share a word with the query.",
  cap="An inverted index lists, for each visual word, the images containing it. The weight wᵢ = tf · idf is large for words in few images and zero for words in all of them."),
3175: dict(d=d3175, stmtKind="ALGORITHM",
  statement=r"<b>Spatial pyramid matching.</b> Partition the image into $2^l\times2^l$ cells for $l=0,1,2$ ($1$, $4$ and $16$ cells) and compute a BoVW histogram of $K$ words in each cell. The descriptor is the concatenation $\mathbf H=\big[\mathbf h^{(0)},\mathbf h^{(1)}_{1..4},\mathbf h^{(2)}_{1..16}\big]$ of dimension $K\sum_{l}4^l=21K$, with finer levels given larger weights; it is typically classified with a linear SVM or a histogram-intersection kernel.",
  hint="How can the bag of words remember that the sky is at the top of the frame?",
  breakdown=[r"<strong>$\mathbf h^{(0)}$ = the whole frame as one bag.</strong> The plain BoVW histogram: what is there, but not where."],
  conn=r"<strong>Sky above, road below.</strong> A frame with the sky on top and one with it at the bottom have the same bag; with a pyramid the top-row cells and bottom-row cells keep their own counts, so the two are different.",
  cap="Level 0 is the whole frame, level 1 four cells, level 2 sixteen cells; each cell has its own histogram, concatenated into H of dimension K(1 + 4 + 16) = 21K."),
3176: dict(d=d3176, stmtKind="WORKED EXAMPLE",
  statement=r"<b>Example.</b> For $\mathbf h_1=(4,2,3,1)$ and $\mathbf h_2=(2,1,1,6)$ over a 4-word vocabulary: $\mathbf h_1\cdot\mathbf h_2=8+2+3+6=19$, $\|\mathbf h_1\|=\sqrt{30}\approx5.477$, $\|\mathbf h_2\|=\sqrt{42}\approx6.481$, so $\cos\theta=\dfrac{19}{5.477\times6.481}\approx0.535$ ($\theta\approx58^\circ$). Cosine similarity ignores vector length.",
  hint="With two frames that use the words in different proportions, how similar are they?",
  breakdown=[r"<strong>$\mathbf h_1\cdot\mathbf h_2=4\cdot2+2\cdot1+3\cdot1+1\cdot6=19$ = the overlap.</strong> Multiply the two counts of each word and add: large when both frames use the same words a lot."],
  conn=r"<strong>Two street frames.</strong> Frame 1 is mostly word 1 (the sign), frame 2 mostly word 4 (the bus). The similarity of 0.535 says they share something but are not the same street view.",
  cap="Two histograms over 4 words: h₁ = (4,2,3,1) and h₂ = (2,1,1,6). Their dot product is 19 and cos θ ≈ 0.535: image 1 is w₁-heavy, image 2 is w₄-heavy."),
}
CARDS[3171]["breakdown"] += [r"<strong>$w(d_i)$ = replace each patch by its nearest word.</strong> A learned vocabulary of $K$ cluster centres turns every 128-number patch into one whole-number word ID.",
                             r"<strong>$h_k=\#\{i:w(d_i)=k\}$ = count the words.</strong> A length-$K$ histogram that is easy to compare and index, tolerates viewpoint change and occlusion, and forgets all geometry."]
CARDS[3172]["breakdown"] += [r"<strong>$\mu_k\leftarrow\frac1{|S_k|}\sum d_i$ = move each word to the middle of its patches.</strong> Assign and update, again and again, until nothing changes.",
                             r"<strong>$K$ = how many words.</strong> Too small merges different patches; too large makes sparse, over-specific bags. k-means can land in local optima, so start it carefully (k-means++)."]
CARDS[3173]["breakdown"] += [r"<strong>$h_k=\sum_i\mathbf 1[k(i)=k]$ = a length-$K$ count.</strong> One bin per visual word.",
                             r"<strong>$\mathbf h/\|\mathbf h\|_1$ = proportions.</strong> Normalising makes frames with different numbers of keypoints comparable; without it, big textured frames look similar to everything."]
CARDS[3174]["breakdown"] += [r"<strong>$\log(N/n_i)$ = how rare the word is.</strong> Large for words found in few images, zero for a word in every image (it is erased).",
                             r"<strong>Inverted index = jump to the right frames.</strong> Each word lists the images that contain it, so a query only looks at images that share a word with it."]
CARDS[3175]["breakdown"] += [r"<strong>$\mathbf h^{(1)}_{1..4},\mathbf h^{(2)}_{1..16}$ = a bag for every cell.</strong> The $2\times2$ and $4\times4$ grids record which words occur in which part of the frame.",
                             r"<strong>$\dim=K(1+4+16)=21K$ = the price.</strong> Finer levels weigh more but each cell has fewer patches, so counts are noisier: a deliberate trade-off."]
CARDS[3176]["breakdown"] += [r"<strong>$\|\mathbf h_1\|=\sqrt{30},\ \|\mathbf h_2\|=\sqrt{42}$ = the lengths.</strong> Dividing by them leaves only the direction, the mix of words.",
                             r"<strong>$\cos\theta\approx0.535$ = moderately alike.</strong> Frame 2 is dominated by $w_4$ and frame 1 by $w_1$. Cosine ignores size, so a big and a small frame with the same proportions score 1."]

STORY = {
 3171: dict(s="STORY 7 · STEP 7 · A BAG OF WORDS", b="Describe a frame by <b>which visual words it contains</b>, ignoring where: a signature that is easy to compare and search.",
   f=[["3164", "SIFT descriptors are the words"]], n=[["3172", "where the words come from"], ["3173", "counting"]]),
 3172: dict(s="STORY 7 · STEP 8 · THE VOCABULARY", b="<b>k-means</b> clusters thousands of descriptors; each centroid is a visual word.",
   f=[["3171", "bag of words"]], n=[["3173", "assign and count"]]),
 3173: dict(s="STORY 7 · STEP 9 · COUNT THEM", b="Map each patch to its nearest word, count, and <b>normalise</b> so frames compare fairly.",
   f=[["3172", "the codebook"]], n=[["3174", "weight the words"], ["3176", "numbers"]]),
 3174: dict(s="STORY 7 · STEP 10 · WEIGHT AND SEARCH", b="<b>TF-IDF</b> down-weights words found everywhere; an <b>inverted index</b> finds candidate frames fast.",
   f=[["3173", "histograms"]], n=[["3175", "put position back"]]),
 3175: dict(s="STORY 7 · STEP 11 · WHERE THE WORDS ARE", b="A <b>spatial pyramid</b> keeps a bag per cell, partly restoring layout.",
   f=[["3174", "weighted bags"]], n=[["3176", "numbers"], ["3181", "faces as points in a space"]]),
 3176: dict(s="STORY 7 · STEP 12 · CHECK BY HAND", b="Two bags: dot product $19$, cosine $\\approx0.535$.",
   f=[["3173", "comparing"]], n=[["3181", "next: recognising a face"]]),
}
FIX = build_fix(CARDS)
