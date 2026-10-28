import math
from subj_lib import *

card = make_card("LAA")
CARDS = []

def V(x0, y0, x1, y1, w=2.2, d=None):
    return L(x0, y0, x1, y1, w, d=d, ar=True)

# ====================== 02 · INDEPENDENCE, BASES & DIMENSION ======================
CARDS.append(card(2, 1, "LINEAR INDEPENDENCE", "Span & Linear Independence",
    [L(24, 72, 112, 72, 0.8, d="2 3"), L(68, 20, 68, 124, 0.8, d="2 3"),
     V(68, 72, 104, 40), V(68, 72, 34, 50), N(110, 36, "v₁", 10), N(28, 44, "v₂", 10),
     N(68, 138, "independent: a plane", 8.5, w="bold"),
     L(132, 72, 226, 72, 0.8, d="2 3"), V(150, 108, 190, 72), V(150, 108, 210, 48, 1.6, "4 3"),
     N(204, 112, "u₂ = 1.5 u₁", 8.5), N(180, 138, "dependent: a line", 8.5, w="bold")],
    "Independent vectors point in genuinely different directions; dependent ones lie on one line",
    ["<strong>Span:</strong> $\\operatorname{span}(v_1,\\dots,v_m)$ is the set of all linear combinations $a_1v_1+\\dots+a_mv_m$, the smallest subspace containing the list.",
     "<strong>Independence:</strong> the list is independent if the <strong>only</strong> way to make $0$ is with every coefficient zero: $a_1v_1+\\dots+a_mv_m=0\\Rightarrow a_1=\\dots=a_m=0$.",
     "<strong>Meaning:</strong> no vector is redundant, i.e. none lies in the span of the others. Any list containing $0$ or a repeated vector is dependent."],
    r"$$a_1v_1+\cdots+a_mv_m=0\ \Longrightarrow\ a_1=\cdots=a_m=0\quad(\text{independent})$$",
    "A band where every member plays a unique instrument: remove anyone and the sound changes; a duplicate instrument adds nothing new.",
    "Independence is a property of the LIST, not the set of vectors: the list (v, v) is dependent even though the set {v} is not."))

CARDS.append(card(2, 2, "BASES", "Basis = Independent + Spanning (Unique Coordinates)",
    [L(24, 110, 214, 110, 0.8, d="2 3"), L(40, 130, 40, 16, 0.8, d="2 3"),
     V(40, 110, 100, 90, 2.4), V(40, 110, 60, 50, 2.4), N(104, 90, "b₁", 10), N(48, 44, "b₂", 10),
     V(40, 110, 140, 56, 2.0, "5 3"), L(100, 90, 140, 56, 1, d="2 2"), L(60, 50, 140, 56, 1, d="2 2"),
     N(150, 52, "v", 11, "start", "bold"),
     N(150, 126, "v = 2 b₁ + 1.5 b₂ : coordinates (2, 1.5)", 8.5, "middle", "bold"), N(150, 140, "exactly ONE way to reach every v", 8.5, "middle")],
    "Every vector is reached in exactly one way as a combination of basis vectors",
    ["<strong>Basis:</strong> a list that is <strong>both independent and spanning</strong>: no redundancy, and nothing missing.",
     "<strong>Key property:</strong> every $v\\in V$ can be written as $v=a_1b_1+\\dots+a_nb_n$ in <strong>exactly one</strong> way; the $a_j$ are its <strong>coordinates</strong> $[v]_B$.",
     "<strong>Why it matters:</strong> a basis turns an abstract space into $\\mathbb{F}^n$: vectors become columns, linear maps become matrices."],
    r"$$v=\sum_{j=1}^{n}a_jb_j\ \text{ (unique } a_j),\qquad [v]_B=(a_1,\dots,a_n)^T\in\mathbb{F}^n$$",
    "Street addresses: 'two blocks east, one and a half north' pins down a location in exactly one way once the compass directions are fixed.",
    "Coordinates depend on the BASIS (and its ORDER). Reordering the basis permutes the coordinates; changing it changes them entirely."))

CARDS.append(card(2, 3, "DIMENSION", "Steinitz Exchange: Independent Lists Are No Longer Than Spanning Lists",
    [box(20, 20, 90, 26, "spanning list: n vectors", "#f1f5f9", 8.5), box(20, 62, 62, 26, "independent: m", "#ffffff", 8.5),
     L(82, 75, 130, 75, 1.4, ar=True), N(106, 68, "swap one at a time", 7.5), N(180, 79, "m ≤ n", 14, "middle", "bold"),
     N(120, 112, "length of any independent list ≤ length of any spanning list", 8.5, w="bold"),
     N(120, 128, "so every basis of V has the same length", 8.5)],
    "Swap independent vectors into the spanning list one at a time; you can never run out of room",
    ["<strong>Statement:</strong> in a finite-dimensional space, <strong>length of any independent list $\\le$ length of any spanning list</strong>.",
     "<strong>Idea:</strong> put an independent vector $u_1$ into the spanning list, which makes it dependent, so one old vector can be dropped; repeat. If $m>n$ you would run out of old vectors first, a contradiction.",
     "<strong>Consequence:</strong> any two bases have the <strong>same length</strong>, which is what makes <strong>dimension</strong> well defined."],
    r"$$u_1,\dots,u_m\ \text{independent},\quad w_1,\dots,w_n\ \text{span}\ \Longrightarrow\ m\le n$$",
    "Moving boxes into a van one at a time: if every box you bring in pushes one old box out, you can't have brought in more boxes than the van held.",
    "The inequality needs independence on the SHORT side and spanning on the LONG side. A spanning list may be longer than a basis; an independent list may be shorter."))

CARDS.append(card(2, 4, "DIMENSION", "Dimension Facts You Use Constantly",
    [box(14, 20, 100, 30, "dim V = n", "#e2e8f0", 10), box(14, 66, 100, 26, "U ⊆ V ⇒ dim U ≤ dim V", "#f1f5f9", 8.5),
     box(14, 104, 100, 26, "dim U = dim V ⇒ U = V", "#f1f5f9", 8.5),
     box(130, 20, 96, 40, "any n independent vectors = a basis", "#ffffff", 8.5), box(130, 72, 96, 40, "any n spanning vectors = a basis", "#ffffff", 8.5),
     N(178, 128, "(check one half, get the other)", 8)],
    "With the right count you only need to verify half of 'basis'",
    ["<strong>Subspaces:</strong> if $U\\subseteq V$ then $\\dim U\\le\\dim V$, and <strong>equality forces $U=V$</strong> (finite-dimensional case).",
     "<strong>Half-check:</strong> in an $n$-dimensional space, any <strong>independent list of length $n$</strong> is automatically a basis, and so is any <strong>spanning list of length $n$</strong>.",
     "<strong>Examples:</strong> $\\dim\\mathbb{F}^n=n$, $\\dim\\mathcal{P}_m(\\mathbb{F})=m+1$, $\\dim\\mathbb{F}^{m\\times n}=mn$, $\\dim\\mathcal{L}(V,W)=\\dim V\\cdot\\dim W$."],
    r"$$\dim\mathcal{P}_m=m+1,\quad \dim\mathbb{F}^{m\times n}=mn,\quad \dim\mathcal{L}(V,W)=\dim V\,\dim W$$",
    "A full set of n keys for n locks: if you have n keys and they are all different (independent), you automatically have a complete set.",
    "The half-check works only when the length EQUALS dim V. Three independent vectors in a 4-D space do NOT form a basis."))

CARDS.append(card(2, 5, "BASES", "Reduce a Spanning List, Extend an Independent One",
    [box(10, 16, 100, 30, "spanning list", "#f1f5f9", 9), L(60, 46, 60, 66, 1.4, ar=True), N(116, 60, "delete redundant vectors", 8, "start"),
     box(10, 68, 100, 30, "BASIS", "#e2e8f0", 10), L(60, 98, 60, 118, 1.4, ar=True),
     box(130, 68, 96, 30, "independent list", "#ffffff", 9), L(178, 98, 178, 118, 1.4, ar=True), N(176, 132, "add vectors until it spans", 8),
     N(60, 134, "", 8), L(122, 83, 112, 83, 1.4, ar=True)],
    "From either side you land on a basis: shrink a spanning list, grow an independent one",
    ["<strong>Reduction:</strong> every spanning list contains a <strong>basis</strong>. Scan left to right and delete any vector already in the span of those before it.",
     "<strong>Extension:</strong> every independent list can be <strong>extended to a basis</strong> by adjoining vectors from a basis (or any spanning list) until it spans.",
     "<strong>Subspace complements:</strong> for any subspace $U\\subseteq V$ there is a subspace $W$ with $V=U\\oplus W$ (extend a basis of $U$)."],
    r"$$\text{span list}\ \xrightarrow{\ \text{delete}\ }\ \text{basis}\ \xleftarrow{\ \text{adjoin}\ }\ \text{independent list},\qquad V=U\oplus W$$",
    "Packing a suitcase: from an overstuffed bag you remove duplicates until nothing is repeated; from a nearly empty bag you add items until you are covered.",
    "The complement W of U is NOT unique (only its dimension is). Different extensions of a basis of U give different complements."))

CARDS.append(card(2, 6, "WORKED BENCHMARK", "Worked Benchmark: Independence and Basis in ℝ³",
    [GRID(14, 18, [[1, 2, 1], [2, 4, 0], [3, 6, 1]], cell=24, sz=10, shade={(i, 1) for i in range(3)}),
     N(50, 14, "v₁   v₂   v₃", 9), N(122, 30, "v₂ = 2 v₁", 10, "start", "bold"),
     N(122, 50, "⇒ dependent list", 9, "start"), N(122, 70, "span = span(v₁, v₃)", 9, "start"),
     N(122, 90, "v₁, v₃ independent", 9, "start"), N(122, 110, "basis, dim = 2", 10, "start", "bold"),
     N(14, 108, "columns are the vectors", 8.5, "start")],
    "The middle column is twice the first, so it adds nothing; two columns remain and they are independent",
    ["<strong>Columns:</strong> $v_1=(1,2,3)$, $v_2=(2,4,6)$, $v_3=(1,0,1)$. Clearly $v_2=2v_1$, so $2v_1-v_2+0\\,v_3=0$ is a nontrivial relation: the list is <strong>dependent</strong>.",
     "<strong>Reduce:</strong> drop $v_2$. The remaining pair $v_1,v_3$ is independent because neither is a multiple of the other (compare first coordinates: $1:1$, second: $2:0$).",
     "<strong>Conclusion:</strong> $\\operatorname{span}(v_1,v_2,v_3)=\\operatorname{span}(v_1,v_3)$ is a <strong>plane</strong> with basis $\\{v_1,v_3\\}$ and $\\dim=2$ (so these three vectors do not span $\\mathbb{R}^3$)."],
    r"$$2v_1-v_2+0\,v_3=0,\qquad \operatorname{span}(v_1,v_2,v_3)=\operatorname{span}(v_1,v_3),\quad \dim=2$$",
    "Three roads on a map where one is just the first road traveled twice as far: you really only have two distinct directions.",
    "Three vectors in ℝ³ do not automatically span ℝ³. Count the INDEPENDENT ones (the rank), not the list length."))

# ====================== 03 · LINEAR MAPS ======================
def _grid_warp():
    out = []
    for i in range(0, 5):
        out.append(L(20 + i * 20, 24, 20 + i * 20, 104, 0.8)); out.append(L(20, 24 + i * 20, 100, 24 + i * 20, 0.8))
    out.append(R(20, 24, 80, 80, "none", 1.4))
    out.append(L(108, 64, 128, 64, 1.5, ar=True)); out.append(N(118, 56, "T", 10, w="bold"))
    # sheared/stretched image grid: (x,y) -> (x + 0.5y, y)
    for i in range(0, 5):
        x0 = 140 + i * 20
        out.append(L(x0, 104, x0 + 40, 24, 0.8))
        out.append(L(140 + 0.0 + (4 - i) * 0 + 0, 24 + i * 20, 140 + 0 + 80 + 0, 24 + i * 20, 0.0))
    for i in range(0, 5):
        y = 24 + i * 20
        out.append(L(140 + (104 - y) / 2.0, y, 140 + (104 - y) / 2.0 + 80, y, 0.8))
    out += [N(70, 120, "straight lines stay straight", 8.5, w="bold"), N(180, 120, "parallel stay parallel; 0 ↦ 0", 8.5, w="bold"),
            C(20, 104, 3), C(140, 104, 3)]
    return out

CARDS.append(card(3, 1, "LINEAR MAPS", "What 'Linear' Means Geometrically",
    _grid_warp(),
    "A linear map warps the whole grid but keeps lines straight, parallels parallel, and the origin fixed",
    ["<strong>Definition:</strong> $T:V\\to W$ is linear if $T(u+v)=Tu+Tv$ and $T(\\lambda v)=\\lambda\\,Tv$ (additivity and homogeneity).",
     "<strong>Consequences:</strong> $T(0)=0$, and $T$ is <strong>completely determined by its values on a basis</strong>: $T(\\sum a_jv_j)=\\sum a_jTv_j$.",
     "<strong>Geometry:</strong> lines go to lines (or points), parallel lines stay parallel, the origin is fixed, and grid cells become parallelograms. Maps like $x\\mapsto x+1$ are <strong>not</strong> linear."],
    r"$$T(au+bv)=aTu+bTv,\qquad T(0)=0,\qquad T\Big(\sum a_jv_j\Big)=\sum a_jT(v_j)$$",
    "Stretching a rubber sheet with a drawn grid, pinned at one point: lines may tilt and cells may skew, but no line may bend.",
    "'Linear' in this sense (a linear map) is NOT the same as 'a line y = mx + b'. The map x ↦ 2x + 1 is affine, not linear (T(0) ≠ 0)."))

def _nr():
    return [R(14, 20, 100, 90, "#ffffff", 1.6), R(14, 50, 100, 30, "#d9dee7", 1.4, 0, "4 3"), N(64, 40, "V", 10, w="bold"), N(64, 68, "null T", 9, w="bold"), N(64, 100, "complement", 8),
            R(150, 20, 76, 90, "#ffffff", 1.6), R(150, 50, 76, 32, "#e2e8f0", 1.4), N(188, 40, "W", 10, w="bold"), N(188, 70, "range T", 9, w="bold"),
            L(116, 64, 148, 64, 1.5, ar=True), N(132, 56, "T", 10, w="bold"), C(188, 100, 3.5), N(188, 114, "0", 8),
            P("M114 66 Q132 90 186 100", w=1.3, dash="4 3", ar=True),
            N(120, 132, "", 8)]

CARDS.append(card(3, 2, "LINEAR MAPS", "Null Space and Range",
    _nr(),
    "The null space is the part of V that T crushes to zero; the range is what T actually reaches in W",
    ["<strong>Null space</strong> $\\operatorname{null}T=\\{v\\in V:Tv=0\\}$ is a <strong>subspace of $V$</strong>: the 'lost information'.",
     "<strong>Range</strong> $\\operatorname{range}T=\\{Tv:v\\in V\\}$ is a <strong>subspace of $W$</strong>: everything the map can output (the column space of its matrix).",
     "<strong>Meaning:</strong> $T$ is injective exactly when nothing but $0$ is lost, and surjective exactly when the range fills $W$."],
    r"$$\operatorname{null}T=\{v:Tv=0\}\subseteq V,\qquad \operatorname{range}T=\{Tv:v\in V\}\subseteq W$$",
    "A paper shredder (T): the null space is what comes out as zero pieces of information; the range is the shapes of confetti it can produce.",
    "null T lives in the DOMAIN V, range T lives in the CODOMAIN W. Mixing up where each one lives is the most common slip."))

CARDS.append(card(3, 3, "RANK-NULLITY", "Rank–Nullity Theorem",
    [R(20, 30, 200, 36, "#ffffff", 1.8), R(20, 30, 70, 36, "#d9dee7", 1.8), N(55, 52, "dim null T", 9, w="bold"), N(155, 52, "dim range T", 9, w="bold"),
     N(120, 22, "dim V", 10, w="bold"), L(20, 74, 220, 74, 1.2),
     N(120, 98, "dim V = dim null T + dim range T", 11, w="bold"), N(120, 116, "(nullity + rank = number of columns)", 9), N(120, 132, "", 8)],
    "Every dimension of the domain either gets crushed (nullity) or survives as output (rank)",
    ["<strong>Theorem:</strong> for $T\\in\\mathcal{L}(V,W)$ with $V$ finite-dimensional, <strong>$\\dim V=\\dim\\operatorname{null}T+\\dim\\operatorname{range}T$</strong>.",
     "<strong>Proof idea:</strong> extend a basis of $\\operatorname{null}T$ to a basis of $V$; the added vectors map to a <strong>basis of the range</strong> (independent and spanning).",
     "<strong>Use:</strong> for an $m\\times n$ matrix, <strong>rank + nullity $=n$</strong> (number of columns). It is the single most used dimension-counting tool."],
    r"$$\dim V=\dim\operatorname{null}T+\dim\operatorname{range}T,\qquad \operatorname{rank}A+\operatorname{nullity}A=n$$",
    "A budget: each input dimension is either spent (destroyed by the map) or invested (shows up in the output); the total is fixed.",
    "The count is by COLUMNS (domain dimension), not rows. A tall matrix and its transpose have the same rank but different nullities."))

CARDS.append(card(3, 4, "LINEAR MAPS", "Injective & Surjective: The Dimension Tests",
    [box(10, 16, 104, 34, "injective ⇔ null T = {0}", "#f1f5f9", 9), box(126, 16, 104, 34, "surjective ⇔ range T = W", "#f1f5f9", 9),
     box(10, 64, 104, 34, "injective ⇒ dim V ≤ dim W", "#ffffff", 8.5), box(126, 64, 104, 34, "surjective ⇒ dim V ≥ dim W", "#ffffff", 8.5),
     N(120, 120, "dim V > dim W ⇒ some nonzero v ↦ 0", 8.5, w="bold"), N(120, 134, "dim V < dim W ⇒ cannot be onto", 8.5, w="bold")],
    "Injectivity needs the domain to be no bigger than the codomain; surjectivity needs it to be no smaller",
    ["<strong>Injective</strong> $\\iff\\operatorname{null}T=\\{0\\}$ (a linear map is one-to-one exactly when only $0$ maps to $0$): you never have to compare pairs of points.",
     "<strong>Surjective</strong> $\\iff\\operatorname{range}T=W$. By rank–nullity, injective forces $\\dim V\\le\\dim W$ and surjective forces $\\dim V\\ge\\dim W$.",
     "<strong>Consequence:</strong> a linear system with <strong>more unknowns than equations</strong> ($\\dim V>\\dim W$) always has a nonzero solution of the homogeneous system, so solutions are never unique."],
    r"$$T\ \text{injective}\iff\operatorname{null}T=\{0\},\qquad T\ \text{surjective}\iff\operatorname{range}T=W$$",
    "Parking cars in spots: more cars than spots means two must share (not injective); more spots than cars means some stay empty (not surjective).",
    "The dimension tests are NECESSARY conditions only. dim V ≤ dim W does not by itself make T injective (the zero map is a counterexample)."))

def _matcols():
    return [N(14, 22, "T v₁", 9, "start"), N(14, 36, "T v₂", 9, "start"),
            GRID(80, 14, [["a₁₁", "a₁₂", "a₁₃"], ["a₂₁", "a₂₂", "a₂₃"]], cell=34, sz=9, shade={(0, 0), (1, 0)}),
            N(97, 96, "col 1 =", 8.5), N(97, 108, "coords of T v₁", 8.5), N(97, 120, "in basis of W", 8.5),
            N(170, 96, "col j =", 8.5), N(170, 108, "[T v_j]_{w}", 9, w="bold"), N(170, 124, "(m × n matrix)", 8.5),
            L(97, 80, 97, 86, 1.1), N(14, 54, "", 8)]

CARDS.append(card(3, 5, "MATRICES", "The Matrix of a Linear Map",
    _matcols(),
    "Column j of the matrix lists the coordinates of T(v_j) in the target basis",
    ["<strong>Build:</strong> pick a basis $v_1..v_n$ of $V$ and $w_1..w_m$ of $W$. Express each $Tv_j=\\sum_i A_{ij}w_i$; the numbers $A_{ij}$ form the matrix $\\mathcal{M}(T)$ ($m\\times n$).",
     "<strong>Act:</strong> then $[Tv]_{w}=\\mathcal{M}(T)\\,[v]_{v}$: applying $T$ is multiplying coordinates by the matrix. The matrix <strong>depends on both bases</strong>.",
     "<strong>Dictionary:</strong> $\\mathcal{M}(S+T)=\\mathcal{M}(S)+\\mathcal{M}(T)$, $\\mathcal{M}(\\lambda T)=\\lambda\\mathcal{M}(T)$, and $\\mathcal{M}(ST)=\\mathcal{M}(S)\\mathcal{M}(T)$: <strong>matrix multiplication is composition</strong>."],
    r"$$Tv_j=\sum_{i=1}^{m}A_{ij}\,w_i,\qquad [Tv]_w=A\,[v]_v,\qquad \mathcal{M}(ST)=\mathcal{M}(S)\,\mathcal{M}(T)$$",
    "A recipe card for a machine: each column says what the machine does to one standard input, and everything else is a mix of those.",
    "Rows are indexed by the TARGET basis, columns by the SOURCE basis. And the composition ST means T acts first, so M(ST) = M(S)M(T) in that order."))

CARDS.append(card(3, 6, "WORKED BENCHMARK", "Worked Benchmark: T(x,y,z) = (x+y, y+z)",
    [GRID(14, 18, [[1, 1, 0], [0, 1, 1]], cell=30, sz=11), N(60, 90, "A  (columns = T e₁, T e₂, T e₃)", 8.5),
     N(122, 30, "null T: x+y=0, y+z=0", 8.5, "start"), N(122, 44, "⇒ (x,y,z) = t(1,−1,1)", 9, "start", "bold"),
     N(122, 64, "nullity = 1", 9, "start"), N(122, 78, "range T = ℝ² (rank 2)", 9, "start", "bold"),
     N(122, 98, "check: 3 = 1 + 2 ✓", 10, "start", "bold"), N(122, 116, "T is onto but not injective", 8.5, "start")],
    "One free direction is crushed (nullity 1) and the plane ℝ² is fully hit (rank 2)",
    ["<strong>Matrix:</strong> $T e_1=(1,0)$, $Te_2=(1,1)$, $Te_3=(0,1)$, so $A=\\begin{pmatrix}1&1&0\\\\0&1&1\\end{pmatrix}$.",
     "<strong>Null space:</strong> $x+y=0$ and $y+z=0$ give $(x,y,z)=t(1,-1,1)$, a line, so <strong>nullity $=1$</strong>.",
     "<strong>Rank:</strong> the columns $(1,0)$ and $(1,1)$ already span $\\mathbb{R}^2$, so rank $=2$ and $T$ is surjective. <strong>Check:</strong> $\\dim V=3=1+2$ ✓. $T$ is not injective because $\\operatorname{null}T\\ne\\{0\\}$."],
    r"$$\operatorname{null}T=\operatorname{span}\{(1,-1,1)\},\quad \operatorname{rank}=2,\quad 3=1+2$$",
    "A scanner projecting a 3-D object onto a 2-D screen: one whole line of depth collapses onto a single point of the screen.",
    "Surjective does not mean injective. Here the map covers all of ℝ² and still loses a whole direction because dim V > dim W."))

# ====================== 04 · INVERTIBILITY, ISOMORPHISMS, CHANGE OF BASIS ======================
CARDS.append(card(4, 1, "INVERTIBILITY", "Invertible = Bijective (and the Inverse is Linear)",
    [R(14, 28, 70, 70, "#ffffff", 1.6), R(156, 28, 70, 70, "#ffffff", 1.6)] +
    [C(34, 46 + 20 * i, 3) for i in range(3)] + [C(206, 46 + 20 * i, 3) for i in range(3)] +
    [L(38, 46 + 20 * i, 202, 46 + 20 * i, 1.2, ar=True) for i in range(3)] +
    [N(120, 40, "T", 10, w="bold"), N(120, 112, "T⁻¹ goes back along every arrow", 8.5),
     N(49, 114, "V", 10, w="bold"), N(191, 114, "W", 10, w="bold"), N(120, 130, "one-to-one AND onto", 9, w="bold")],
    "Each point of W is hit exactly once, so the arrows can be reversed",
    ["<strong>Invertible</strong> means there is $S$ with $ST=I_V$ and $TS=I_W$. This holds <strong>iff $T$ is bijective</strong> (injective and surjective).",
     "<strong>Linearity is free:</strong> the inverse of a linear bijection is automatically linear. Also $(ST)^{-1}=T^{-1}S^{-1}$ (reverse order).",
     "<strong>Test:</strong> $T$ is invertible $\\iff\\operatorname{null}T=\\{0\\}$ and $\\operatorname{range}T=W$; for matrices, $A$ is invertible $\\iff\\det A\\ne0\\iff$ columns are a basis."],
    r"$$T\ \text{invertible}\iff T\ \text{bijective},\qquad (ST)^{-1}=T^{-1}S^{-1}$$",
    "Putting on socks then shoes: to undo it you remove the shoes first, then the socks (reverse order).",
    "(ST)⁻¹ is T⁻¹S⁻¹, NOT S⁻¹T⁻¹. Matrix products do not commute, so the order matters."))

CARDS.append(card(4, 2, "ISOMORPHISMS", "Isomorphic ⇔ Same Dimension",
    [box(14, 24, 70, 36, "V (dim n)", "#f1f5f9", 9), box(156, 24, 70, 36, "𝔽ⁿ", "#f1f5f9", 11), L(86, 42, 154, 42, 1.6, ar=True), L(154, 42, 86, 42, 1.6, ar=True),
     N(120, 34, "coordinates [·]_B", 8.5), box(14, 84, 70, 34, "dim V = n", "#ffffff", 9), box(156, 84, 70, 34, "dim W = n", "#ffffff", 9),
     L(86, 101, 154, 101, 1.4), N(120, 96, "≅", 14, w="bold"), N(120, 132, "same dimension ⇒ the spaces are structurally identical", 8.5, w="bold")],
    "Any n-dimensional space over 𝔽 is just a relabeled 𝔽ⁿ",
    ["<strong>Isomorphism:</strong> an invertible linear map $V\\to W$. Isomorphic spaces behave identically as vector spaces.",
     "<strong>Theorem:</strong> finite-dimensional $V\\cong W\\iff\\dim V=\\dim W$. Choosing a basis gives the isomorphism $v\\mapsto[v]_B\\in\\mathbb{F}^n$.",
     "<strong>Payoff:</strong> every finite-dimensional question can be moved to $\\mathbb{F}^n$ and answered with matrices. Dimension is the <strong>only</strong> invariant of a vector space up to isomorphism."],
    r"$$V\cong W\iff\dim V=\dim W,\qquad V\cong\mathbb{F}^{n}\ \ (n=\dim V)$$",
    "Translating the same book into different languages: the plot (structure) is identical; only the words (basis choice) change.",
    "Isomorphic does not mean equal. The space of 2×2 matrices, P₃ and ℝ⁴ are isomorphic, but the isomorphism depends on a chosen basis."))

def _cyc():
    return [box(76, 12, 88, 30, "injective", "#f1f5f9", 10), box(14, 92, 88, 30, "surjective", "#f1f5f9", 10), box(138, 92, 88, 30, "invertible", "#e2e8f0", 10),
            L(130, 42, 168, 90, 1.5, ar=True), L(100, 107, 136, 107, 1.5, ar=True), L(54, 90, 90, 44, 1.5, ar=True),
            N(120, 138, "operators on a finite-dimensional V (same space in and out)", 8)]

CARDS.append(card(4, 3, "INVERTIBILITY", "Operators: Injective ⇔ Surjective ⇔ Invertible",
    _cyc(),
    "For a map from a finite-dimensional space to itself, any one of the three properties gives the other two",
    ["<strong>Theorem:</strong> if $T\\in\\mathcal{L}(V)$ and $\\dim V<\\infty$, then <strong>injective $\\iff$ surjective $\\iff$ invertible</strong>.",
     "<strong>Why:</strong> rank–nullity with $\\dim V=\\dim W$: $\\operatorname{null}T=\\{0\\}$ forces $\\dim\\operatorname{range}T=\\dim V$, so the range is all of $V$ (and conversely).",
     "<strong>Shortcut:</strong> to prove $A$ is invertible, <strong>show only $Ax=0\\Rightarrow x=0$</strong>. Also $ST=I\\Rightarrow TS=I$ for operators: a one-sided inverse is two-sided."],
    r"$$T\in\mathcal{L}(V),\ \dim V<\infty:\quad \operatorname{null}T=\{0\}\iff\operatorname{range}T=V\iff T^{-1}\ \text{exists}$$",
    "A full theater where the number of seats equals the number of guests: if no two guests share a seat, no seat is empty.",
    "This FAILS in infinite dimensions (e.g. the right shift is injective but not surjective) and for maps between spaces of different dimension."))

def _cob():
    return [box(14, 14, 78, 30, "[v]_B", "#f1f5f9", 11), box(148, 14, 78, 30, "[v]_{B′}", "#f1f5f9", 11),
            L(94, 29, 146, 29, 1.5, ar=True), N(120, 22, "S⁻¹", 10, w="bold"),
            box(14, 78, 78, 30, "[Tv]_B", "#ffffff", 11), box(148, 78, 78, 30, "[Tv]_{B′}", "#ffffff", 11),
            L(53, 46, 53, 76, 1.5, ar=True), N(36, 64, "A", 10, w="bold"), L(187, 46, 187, 76, 1.5, ar=True), N(208, 64, "A′", 10, w="bold"),
            L(94, 93, 146, 93, 1.5, ar=True), N(120, 86, "S⁻¹", 10, w="bold"),
            N(120, 128, "A′ = S⁻¹ A S", 12, w="bold"), N(120, 142, "S = columns are the new basis in old coordinates", 7.5)]

CARDS.append(card(4, 4, "CHANGE OF BASIS", "Change of Basis & Similarity",
    _cob(),
    "Go to the new basis, apply the matrix in the old basis, come back: A′ = S⁻¹AS",
    ["<strong>Change-of-basis matrix:</strong> if $B'=(b_1',\\dots,b_n')$ and $S$ has these vectors (written in basis $B$) as columns, then $[v]_B=S\\,[v]_{B'}$.",
     "<strong>Operators:</strong> the matrix of the same $T$ in the new basis is $A'=S^{-1}AS$. Matrices related this way are called <strong>similar</strong>.",
     "<strong>Goal of the course:</strong> pick the basis that makes $A'$ as simple as possible (diagonal, Jordan, or orthonormal-diagonal)."],
    r"$$[v]_B=S\,[v]_{B'},\qquad A'=S^{-1}AS\ \ (\text{operator}),\qquad A'=Q^{-1}AP\ \ (\text{map, two bases})$$",
    "Reading a map in kilometers versus miles: the territory is the same, but the numbers you write down change by a fixed conversion.",
    "S has the NEW basis vectors as columns (in old coordinates). Using S instead of S⁻¹ (or the reverse) is the usual sign error."))

CARDS.append(card(4, 5, "CHANGE OF BASIS", "What Similar Matrices Share",
    [box(14, 14, 100, 28, "trace  tr A = tr A′", "#f1f5f9", 9), box(126, 14, 100, 28, "determinant", "#f1f5f9", 9),
     box(14, 52, 100, 28, "eigenvalues", "#f1f5f9", 9), box(126, 52, 100, 28, "characteristic poly", "#f1f5f9", 9),
     box(14, 90, 100, 28, "rank & nullity", "#f1f5f9", 9), box(126, 90, 100, 28, "min polynomial", "#f1f5f9", 9),
     N(120, 134, "invariants of the OPERATOR, not of the basis", 9, w="bold")],
    "Everything that describes the operator itself survives a change of basis",
    ["<strong>Same operator, different clothes:</strong> if $A'=S^{-1}AS$ then $A$ and $A'$ have the same <strong>trace, determinant, rank, eigenvalues (with multiplicity), characteristic and minimal polynomials</strong>.",
     "<strong>Quick proof:</strong> $\\det(\\lambda I-S^{-1}AS)=\\det(S^{-1}(\\lambda I-A)S)=\\det(\\lambda I-A)$, and $\\operatorname{tr}(S^{-1}AS)=\\operatorname{tr}(ASS^{-1})=\\operatorname{tr}A$.",
     "<strong>Use:</strong> to show two matrices are <strong>not</strong> similar, find one invariant that differs. The converse is false in general: equal invariants do not guarantee similarity."],
    r"$$A'=S^{-1}AS\Rightarrow\ \operatorname{tr}A'=\operatorname{tr}A,\ \ \det A'=\det A,\ \ p_{A'}=p_A$$",
    "Two photos of the same sculpture from different angles: the angles differ, but the sculpture's weight and volume do not.",
    "Same characteristic polynomial does NOT imply similar. [[0,1],[0,0]] and the zero matrix share eigenvalues but have different ranks."))

CARDS.append(card(4, 6, "WORKED BENCHMARK", "Worked Benchmark: Coordinates in the Basis {(1,1), (1,−1)}",
    [L(26, 72, 214, 72, 0.8, d="2 3"), L(120, 12, 120, 132, 0.8, d="2 3"),
     V(120, 72, 160, 32, 2.4), V(120, 72, 160, 112, 2.4), N(168, 30, "b₁=(1,1)", 8.5, "start"), N(168, 120, "b₂=(1,−1)", 8.5, "start"),
     V(120, 72, 200, 56, 2, "5 3"), N(204, 54, "v=(3,1)", 8.5, "start", "bold"),
     N(30, 22, "a(1,1)+b(1,−1) = (3,1)", 8.5, "start"), N(30, 36, "a+b=3, a−b=1", 8.5, "start"), N(30, 50, "⇒ a=2, b=1", 9, "start", "bold"),
     N(30, 116, "S = [[1,1],[1,−1]]", 8.5, "start"), N(30, 128, "[v]_B = S⁻¹v = (2, 1)", 8.5, "start", "bold")],
    "(3,1) = 2·(1,1) + 1·(1,−1): its coordinates in the new basis are (2, 1)",
    ["<strong>Basis:</strong> $B=\\{(1,1),(1,-1)\\}$, so $S=\\begin{pmatrix}1&1\\\\1&-1\\end{pmatrix}$ (columns = basis vectors in standard coordinates).",
     "<strong>Solve</strong> $a(1,1)+b(1,-1)=(3,1)$: $a+b=3$ and $a-b=1$, giving <strong>$a=2,\\ b=1$</strong>, so $[v]_B=(2,1)$.",
     "<strong>Check with the matrix:</strong> $S^{-1}=\\tfrac12\\begin{pmatrix}1&1\\\\1&-1\\end{pmatrix}$ and $S^{-1}(3,1)^T=\\tfrac12(4,2)^T=(2,1)^T$ ✓."],
    r"$$[v]_B=S^{-1}v=\tfrac12\begin{pmatrix}1&1\\1&-1\end{pmatrix}\begin{pmatrix}3\\1\end{pmatrix}=\begin{pmatrix}2\\1\end{pmatrix}$$",
    "Giving someone directions along the diagonal streets of a city instead of the north-south grid: the same spot, new street names.",
    "To go from standard coordinates to the new basis you apply S⁻¹ (not S). S converts the other way, from new coordinates to standard."))

# ====================== 05 · POLYNOMIALS & MINIMAL POLYNOMIAL ======================
CARDS.append(card(5, 1, "POLYNOMIALS OF OPERATORS", "p(T): Plugging an Operator into a Polynomial",
    [box(14, 14, 100, 28, "p(z) = z² − 3z + 2", "#f1f5f9", 9), L(114, 28, 136, 28, 1.5, ar=True),
     box(138, 14, 88, 28, "p(T) = T² − 3T + 2I", "#e2e8f0", 9),
     N(120, 66, "p(z) = (z−1)(z−2)", 9.5, w="bold"), L(120, 72, 120, 82, 1.3, ar=True), N(120, 96, "p(T) = (T − I)(T − 2I) = (T − 2I)(T − I)", 9, w="bold"),
     N(120, 116, "polynomials in ONE operator always commute", 8.5), N(120, 132, "constant term c ↦ c·I", 8.5)],
    "The factoring identities of ordinary polynomials survive when z is replaced by an operator",
    ["<strong>Definition:</strong> for $p(z)=a_0+a_1z+\\dots+a_mz^m$ set $p(T)=a_0I+a_1T+\\dots+a_mT^m$ (the constant term becomes $a_0I$).",
     "<strong>Algebra:</strong> $(pq)(T)=p(T)\\,q(T)=q(T)\\,p(T)$, so <strong>polynomials in a single $T$ commute</strong> and factor like numbers.",
     "<strong>Spectral link:</strong> if $Tv=\\lambda v$ then $p(T)v=p(\\lambda)v$: eigenvalues of $p(T)$ are $p(\\lambda)$."],
    r"$$p(T)=\sum a_kT^k,\quad (pq)(T)=p(T)q(T),\qquad Tv=\lambda v\Rightarrow p(T)v=p(\lambda)v$$",
    "Taking a recipe written for numbers and cooking it with a machine instead: the steps compose in the same order and give the same algebra.",
    "Polynomials in the SAME operator commute. Polynomials in two different operators S and T generally do not."))

CARDS.append(card(5, 2, "EIGENVALUE EXISTENCE", "Every Complex Operator Has an Eigenvalue",
    [N(120, 18, "dim V = n ≥ 1, 𝔽 = ℂ", 9, w="bold"), N(120, 40, "v, Tv, T²v, …, Tⁿv   (n+1 vectors in dim n)", 9),
     L(120, 46, 120, 58, 1.3, ar=True), N(120, 72, "dependent ⇒ a₀v + a₁Tv + … + aₙTⁿv = 0", 9),
     L(120, 78, 120, 90, 1.3, ar=True), N(120, 104, "p(T)v = 0, p factors over ℂ:", 9), N(120, 118, "p(z) = c(z−λ₁)…(z−λ_m)", 9),
     N(120, 134, "some (T − λⱼI) is not injective ⇒ λⱼ is an eigenvalue", 8.5, w="bold")],
    "A dependent list v, Tv, …, Tⁿv forces a factor (T − λI) to be non-injective",
    ["<strong>Theorem:</strong> every operator on a <strong>nonzero finite-dimensional complex</strong> vector space has an eigenvalue.",
     "<strong>Proof:</strong> pick $v\\ne0$; the $n+1$ vectors $v,Tv,\\dots,T^nv$ are dependent, giving a nonzero $p$ with $p(T)v=0$. Factor $p$ over $\\mathbb{C}$ into linear terms.",
     "<strong>Why a product of non-injective maps is non-injective:</strong> $(T-\\lambda_1I)\\cdots(T-\\lambda_mI)$ sends the nonzero $v$ to $0$, so at least one factor has a nonzero null vector: an eigenvector."],
    r"$$p(T)v=0,\ \ p(z)=c\prod(z-\lambda_j)\ \Rightarrow\ \exists j:\ T-\lambda_jI\ \text{not injective}$$",
    "A chain of locked doors that a person walked through: at least one lock must have been open, or they could not have gotten through.",
    "This is false over ℝ (rotation by 90° in the plane has no real eigenvalue) and for infinite-dimensional spaces. It needs algebraic closure (ℂ)."))

CARDS.append(card(5, 3, "MINIMAL POLYNOMIAL", "The Minimal Polynomial",
    [N(120, 18, "annihilating polynomials of T:  {p : p(T) = 0}", 8.5, w="bold"),
     R(30, 28, 180, 44, "#ffffff", 1.6), N(120, 48, "(z−1)(z−2)(z−3)     (z−1)²(z−2)(z−3)  …", 8.5), N(120, 64, "all multiples of the minimal one", 8),
     L(120, 72, 120, 86, 1.3, ar=True), box(60, 88, 120, 28, "min poly q: monic, smallest degree", "#e2e8f0", 8.5),
     N(120, 134, "q divides EVERY annihilating polynomial", 9, w="bold")],
    "The minimal polynomial is the smallest-degree monic polynomial that kills T, and it divides all others",
    ["<strong>Definition:</strong> the <strong>minimal polynomial</strong> $q$ of $T$ is the monic polynomial of <strong>least degree</strong> with $q(T)=0$. It exists since $I,T,\\dots,T^{n^2}$ are dependent.",
     "<strong>Divisibility:</strong> if $p(T)=0$ then <strong>$q$ divides $p$</strong> (divide with remainder; the remainder would be a smaller annihilator unless it is $0$).",
     "<strong>Degree bound:</strong> $\\deg q\\le n=\\dim V$ (Cayley–Hamilton) and $q$ is unique."],
    r"$$q(T)=0,\quad q\ \text{monic, minimal degree};\qquad p(T)=0\iff q\mid p$$",
    "The shortest rope that still ties the knot: any longer rope that works must contain the short one.",
    "Minimal polynomial is monic. And p(T) = 0 is an identity of OPERATORS, not of numbers: it does not mean p has T as a root of a scalar equation."))

CARDS.append(card(5, 4, "MINIMAL POLYNOMIAL", "Cayley–Hamilton & Roots = Eigenvalues",
    [box(14, 14, 100, 34, "char poly p_T(λ) = det(λI − T)", "#f1f5f9", 8), box(126, 14, 100, 34, "min poly q(λ)", "#e2e8f0", 9),
     L(120, 62, 120, 80, 1.4, ar=True), N(120, 72, "q | p_T", 10, "middle", "bold"),
     N(120, 98, "p_T(T) = 0   (Cayley–Hamilton)", 9.5, w="bold"), N(120, 114, "roots of q = roots of p_T = eigenvalues", 9),
     N(120, 130, "different multiplicities possible", 8.5)],
    "Same roots, but the minimal polynomial may have smaller multiplicities",
    ["<strong>Cayley–Hamilton:</strong> every operator satisfies its own characteristic polynomial, $p_T(T)=0$, so the minimal polynomial <strong>divides</strong> $p_T$ and $\\deg q\\le n$.",
     "<strong>Roots:</strong> the zeros of $q$ are <strong>exactly the eigenvalues</strong> of $T$ (if $Tv=\\lambda v$ then $q(\\lambda)v=q(T)v=0$; conversely every root is an eigenvalue).",
     "<strong>Difference:</strong> $p_T$ records <strong>algebraic multiplicity</strong> (size of the generalized eigenspace); $q$ records the <strong>largest Jordan block</strong> for each eigenvalue."],
    r"$$p_T(T)=0,\quad q\mid p_T,\quad \{\text{roots of }q\}=\{\text{eigenvalues}\}$$",
    "The full guest list (char poly) versus the shortest invitation that still reaches every distinct guest (min poly).",
    "A matrix can satisfy a polynomial of degree less than n. Do not assume q = p_T. Equality happens for operators with a single Jordan block per eigenvalue."))

CARDS.append(card(5, 5, "MINIMAL POLYNOMIAL", "Diagonalizable ⇔ Minimal Polynomial Has Distinct Roots",
    [box(14, 20, 100, 38, "q(z) = (z−λ₁)(z−λ₂)…", "#e2e8f0", 8.5), N(64, 74, "no repeated factors", 8.5, w="bold"),
     L(116, 39, 138, 39, 1.6, ar=True), box(140, 20, 86, 38, "diagonalizable", "#f1f5f9", 9.5),
     box(14, 92, 100, 38, "q(z) = (z−λ)²…", "#ffffff", 8.5), N(64, 144, "repeated factor", 8.5, w="bold"),
     L(116, 111, 138, 111, 1.6, ar=True), box(140, 92, 86, 38, "NOT diagonalizable", "#ffffff", 9)],
    "A repeated factor in the minimal polynomial signals a Jordan block and blocks diagonalization",
    ["<strong>Theorem:</strong> $T$ is diagonalizable $\\iff$ its minimal polynomial has <strong>no repeated roots</strong> (equals $(z-\\lambda_1)\\cdots(z-\\lambda_m)$ with distinct $\\lambda_j$).",
     "<strong>Why:</strong> a squarefree $q$ splits $V$ into the eigenspaces $\\operatorname{null}(T-\\lambda_jI)$; a repeated factor means some vector needs $(T-\\lambda I)^2$ to be killed, i.e. a Jordan chain.",
     "<strong>Shortcut:</strong> if $T$ has $n$ distinct eigenvalues then $q$ has $n$ distinct roots, so $T$ is diagonalizable. If you find a polynomial with distinct roots that annihilates $T$, you're done."],
    r"$$T\ \text{diagonalizable}\iff q(z)=\prod_{j=1}^{m}(z-\lambda_j)\ \text{(distinct }\lambda_j)$$",
    "A team where each job has exactly one owner is easy to split; a job that needs a chain of two people in sequence cannot be handed out in parallel.",
    "It is the MINIMAL polynomial, not the characteristic one, that must be squarefree. The char poly can have repeated roots and the operator can still be diagonalizable (e.g. I)."))

CARDS.append(card(5, 6, "WORKED BENCHMARK", "Worked Benchmark: [[2,1],[0,2]] vs 2I",
    [GRID(14, 18, [[2, 1], [0, 2]], cell=30, sz=12), N(44, 94, "A", 10, w="bold"), GRID(110, 18, [[2, 0], [0, 2]], cell=30, sz=12), N(140, 94, "2I", 10, w="bold"),
     N(20, 112, "p_A = (z−2)²", 9, "start"), N(20, 126, "A − 2I ≠ 0 ⇒ q = (z−2)²", 8.5, "start", "bold"),
     N(112, 112, "p = (z−2)²", 9, "start"), N(112, 126, "2I − 2I = 0 ⇒ q = z−2", 8.5, "start", "bold"),
     N(210, 40, "A: Jordan block", 8.5), N(210, 52, "not diagonal.", 8.5), N(210, 78, "2I: already", 8.5), N(210, 90, "diagonal", 8.5)],
    "Same characteristic polynomial (z−2)², but different minimal polynomials and different behavior",
    ["<strong>Both</strong> matrices have characteristic polynomial $(z-2)^2$ and the single eigenvalue $2$.",
     "<strong>For $A$:</strong> $A-2I=\\begin{pmatrix}0&1\\\\0&0\\end{pmatrix}\\ne0$, but $(A-2I)^2=0$, so the minimal polynomial is $\\mathbf{(z-2)^2}$, which has a repeated root: <strong>$A$ is not diagonalizable</strong>.",
     "<strong>For $2I$:</strong> $2I-2I=0$ already, so the minimal polynomial is $\\mathbf{z-2}$ (squarefree): <strong>diagonalizable</strong> (it is diagonal)."],
    r"$$(A-2I)^2=\begin{pmatrix}0&1\\0&0\end{pmatrix}^{2}=0\ \Rightarrow\ q_A=(z-2)^2,\qquad q_{2I}=z-2$$",
    "Two clocks with the same number of gears (char poly) but one has gears that must turn in sequence (a chain) while the other's all run independently.",
    "Equal characteristic polynomials do not mean similar. The minimal polynomial (or Jordan structure) is what distinguishes A from 2I."))
