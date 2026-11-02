"""LAA topic 03 (linear maps, null space, range, matrices). Photo picture: a linear map T
is an edit applied to every arrow at once (rotate, zoom, stretch, shear, flatten)."""
from laa_lib import *

SUBJECT = "LAA"

def grid(o, a, b, n=3, w=.5):
    p = lambda i, j: (o[0] + i * a[0] + j * b[0], o[1] + i * a[1] + j * b[1])
    return "".join(L(*p(i, 0), *p(i, n), w) for i in range(n + 1)) + "".join(L(*p(0, j), *p(n, j), w) for j in range(n + 1))

def d20301(c):
    A, B = (40, 110), (166, 110)
    return svg(c,
        phone(6, 24, 102, 108, "before"), phone(132, 24, 102, 108, "after T"),
        grid((20, 122), (22, 0), (0, -22)), grid((142, 122), (24, -6), (10, -22)),
        pin(20, 122, None), pin(142, 122, None),
        vec((20, 122), (42, 122), "u", 0, 10, "middle", 7.5), vec((20, 122), (20, 100), "v", -3, 0, "end", 7.5),
        vec((142, 122), (166, 116), "Tu", 2, 10, "middle", 7.5), vec((142, 122), (152, 100), "Tv", -3, 0, "end", 7.5),
        L(110, 76, 130, 76, 1, ar=True), N(120, 70, "T", 8, "middle"),
        N(120, 8, "T(au + bv) = aTu + bTv,  T(0) = 0: the pin stays put", 7.2, "middle"),
        N(120, 142, "grid squares → parallelograms, lines stay straight", 7, "middle"))

def d20302(c):
    return svg(c,
        phone(6, 20, 102, 112, "V"), phone(132, 20, 102, 112, "W"),
        L(14, 118, 100, 34, 1, "3 2"), N(54, 122, "null T: Tv = 0", 7.5, "start"),
        pin(57, 76, None),
        vec((57, 76), (80, 54), "n", 2, 0, "start", 7.5), vec((57, 76), (90, 92), "v", 2, 6, "start", 7.5),
        L(140, 110, 226, 42, 1), N(226, 54, "range T", 7.5, "end"),
        pin(183, 76, None), vec((183, 76), (210, 55), "Tv", 2, 8, "start", 7.5),
        N(120, 12, "the flatten edit: everything along n is squashed to the pin", 7.5, "middle"),
        L(110, 76, 130, 76, 1, ar=True), N(120, 70, "T", 8, "middle"),
        N(120, 142, "null T ⊆ V is lost · range T ⊆ W is what you can get", 7, "middle"))

def d20303(c):
    return svg(c,
        N(120, 14, "dim V = dim null T + dim range T", 8.5, "middle"),
        R(14, 34, 212, 22, "#ffffff", 1, 3), N(120, 49, "basis of V: n arrows", 7.5, "middle"),
        R(14, 72, 70, 22, "#d9dee7", 1, 3), N(49, 87, "null T: k arrows", 7.5, "middle"),
        R(88, 72, 138, 22, "#f1f5f9", 1, 3), N(157, 87, "the rest: n − k arrows", 7.5, "middle"),
        L(49, 96, 49, 112, 1, ar=True), N(49, 124, "→ 0 (squashed)", 7.5, "middle"),
        L(157, 96, 157, 112, 1, ar=True), N(157, 124, "→ a basis of range T", 7.5, "middle"),
        N(120, 140, "m × n matrix: rank A + nullity A = n (columns)", 7.5, "middle"))

def d20304(c):
    return svg(c,
        N(64, 14, "injective", 8, "middle"), N(178, 14, "surjective", 8, "middle"),
        phone(8, 24, 52, 78), phone(76, 24, 52, 78), L(62, 62, 74, 62, 1, ar=True),
        pin(34, 62, None), vec((34, 62), (50, 44), None), pin(102, 62, None), vec((102, 62), (118, 44), None),
        N(64, 116, "null T = {0}", 7.5, "middle"), N(64, 127, "nothing is squashed", 7, "middle"), N(64, 138, "⇒ dim V ≤ dim W", 7, "middle"),
        phone(140, 24, 40, 78), phone(192, 24, 40, 78), L(182, 62, 190, 62, 1, ar=True),
        sheet([(196, 30), (228, 30), (228, 96), (196, 96)], "#f1f5f9"),
        N(178, 116, "range T = W", 7.5, "middle"), N(178, 127, "every target reached", 7, "middle"), N(178, 138, "⇒ dim V ≥ dim W", 7, "middle"))

def d20305(c):
    return svg(c,
        N(120, 12, "column j of A = where T sends the basis arrow vⱼ", 7.5, "middle"),
        R(80, 26, 80, 64, "#ffffff", 1, 3),
        N(100, 46, "A₁₁", 8, "middle"), N(140, 46, "A₁₂", 8, "middle"), N(100, 74, "A₂₁", 8, "middle"), N(140, 74, "A₂₂", 8, "middle"),
        L(120, 30, 120, 86, .6, "2 2"),
        N(100, 100, "Tv₁", 7.5, "middle"), N(140, 100, "Tv₂", 7.5, "middle"),
        N(74, 60, "A =", 9, "end"),
        N(12, 120, "Tvⱼ = Σᵢ Aᵢⱼ wᵢ", 7.5, "start"), N(12, 132, "[Tv]w = A [v]v", 7.5, "start"),
        N(236, 120, "two edits in a row:", 7.5, "end"), N(236, 132, "ℳ(ST) = ℳ(S) ℳ(T)", 7.5, "end"))

def d20306(c):
    return svg(c,
        N(120, 12, "T(x, y, z) = (x + y, y + z)", 8.5, "middle"),
        R(14, 26, 92, 44, "#ffffff", 1, 3), N(60, 42, "A = [1 1 0]", 8, "middle"), N(60, 56, "      [0 1 1]", 8, "middle"),
        N(130, 34, "Te₁ = (1,0), Te₂ = (1,1)", 7.5, "start"), N(130, 46, "Te₃ = (0,1)", 7.5, "start"), N(130, 58, "columns span ℝ²: rank 2", 7.5, "start"),
        L(20, 118, 110, 82, 1, "3 2"), pin(65, 100, None), vec((65, 100), (91, 90), "(1, −1, 1)", 2, -4, "start", 7.5),
        N(14, 134, "null T = span{(1, −1, 1)}: nullity 1", 7.5, "start"),
        N(236, 116, "3 = 1 + 2 ✓", 8, "end"), N(236, 128, "onto, not one-to-one", 7, "end"))

CARDS = {
20301: dict(d=d20301, stmtKind="DEFINITION",
  statement=r"<b>Linear map (Axler 3.2).</b> A linear map from $V$ to $W$ is a function $T:V\to W$ with additivity $T(u+v)=Tu+Tv$ and homogeneity $T(\lambda v)=\lambda(Tv)$ for all $u,v\in V$, $\lambda\in\mathbb F$. Then $T(0)=0$ (3.10), and $T$ is determined by its values on a basis: $T(\sum a_jv_j)=\sum a_jTv_j$ (3.4).",
  hint="Which photo edits are 'linear', and what must happen to the centre pin?",
  breakdown=[r"<strong>$T(au+bv)=aTu+bTv$</strong> = editing a mix of arrows gives the same mix of the edited arrows: you can edit first or mix first.",
             r"<strong>$T(0)=0$</strong> = the pin never moves. Sliding the whole photo ($x\mapsto x+1$) is not linear.",
             r"<strong>$T(\sum a_jv_j)=\sum a_jTv_j$</strong> = know where the basis arrows go and you know the whole edit."],
  conn=r"<strong>Edits that keep the grid straight.</strong> Rotate, zoom, stretch, shear or flatten a photo about its centre: straight lines stay straight, parallel lines stay parallel and the centre stays put. Those are exactly the linear edits.",
  cap="The edit T turns the square grid into a grid of parallelograms. Arrows u, v become Tu, Tv, and T(au + bv) = aTu + bTv, with the pin fixed: T(0) = 0."),
20302: dict(d=d20302, stmtKind="DEFINITION",
  statement=r"<b>Null space and range (Axler 3.11, 3.18).</b> For $T\in\mathcal L(V,W)$, $\operatorname{null}T=\{v\in V:Tv=0\}$ and $\operatorname{range}T=\{Tv:v\in V\}$. These are subspaces of $V$ and $W$ respectively (3.14, 3.19). $T$ is injective $\iff\operatorname{null}T=\{0\}$ (3.16).",
  hint="When you flatten a photo, which arrows disappear and which pictures can you still get?",
  breakdown=[r"<strong>$\operatorname{null}T=\{v:Tv=0\}$</strong> = arrows the edit squashes onto the pin: information lost.",
             r"<strong>$\operatorname{range}T=\{Tv\}$</strong> = every output the edit can produce (the column space of its matrix).",
             r"<strong>Both are subspaces</strong>, through the pin of $V$ and of $W$, because $T$ respects mixing."],
  conn=r"<strong>The flatten filter.</strong> Squash a photo onto one line: everything perpendicular to that line collapses to the pin (null space), and the only pictures you can still make lie on that line (range).",
  cap="Left: the dashed line null T is squashed to the pin (Tv = 0). Right: range T is everything the edit can output."),
20303: dict(d=d20303, stmtKind="THEOREM",
  statement=r"<b>Fundamental theorem of linear maps (Axler 3.21).</b> If $V$ is finite-dimensional and $T\in\mathcal L(V,W)$, then $\operatorname{range}T$ is finite-dimensional and $\dim V=\dim\operatorname{null}T+\dim\operatorname{range}T$. For an $m\times n$ matrix: $\operatorname{rank}A+\operatorname{nullity}A=n$.",
  hint="Every direction of the photo is either squashed or survives. How do the counts add up?",
  breakdown=[r"<strong>$\dim\operatorname{null}T$</strong> = how many independent directions the edit squashes to the pin.",
             r"<strong>$\dim\operatorname{range}T$</strong> = how many independent directions survive in the output.",
             r"<strong>They add to $\dim V$:</strong> extend a basis of the null space to a basis of $V$; the extra arrows map to a basis of the range."],
  conn=r"<strong>Nothing disappears without being counted.</strong> Flatten a 3D scene to a 2D photo: 1 direction (depth) is lost, 2 survive, $1+2=3$.",
  cap="A basis of V splits into k arrows in null T, which go to 0, and n − k arrows, which go to a basis of range T: dim V = dim null T + dim range T."),
20304: dict(d=d20304, stmtKind="THEOREM",
  statement=r"<b>Injective and surjective (Axler 3.16, 3.22, 3.24).</b> For $T\in\mathcal L(V,W)$: $T$ is injective $\iff\operatorname{null}T=\{0\}$; $T$ is surjective $\iff\operatorname{range}T=W$. If $\dim V>\dim W$ no linear map $V\to W$ is injective; if $\dim V\lt\dim W$ none is surjective.",
  hint="Can you tell an edit is one-to-one by checking just one arrow?",
  breakdown=[r"<strong>injective $\iff\operatorname{null}T=\{0\}$</strong> = only the zero arrow lands on the pin. If $Tu=Tv$ then $T(u-v)=0$, so one check covers all pairs.",
             r"<strong>surjective $\iff\operatorname{range}T=W$</strong> = every picture in $W$ can be produced.",
             r"<strong>Dimension limits:</strong> by rank–nullity, injective needs $\dim V\le\dim W$ and surjective needs $\dim V\ge\dim W$. More unknowns than equations always gives a nonzero solution."],
  conn=r"<strong>Can you undo the edit?</strong> If no arrow is squashed to the pin, no two arrows end up on top of each other, so nothing is lost. But a 3D scene can never fit one-to-one into a flat photo.",
  cap="Injective: null T = {0}, nothing is squashed (needs dim V ≤ dim W). Surjective: range T = W, every target is reached (needs dim V ≥ dim W)."),
20305: dict(d=d20305, stmtKind="DEFINITION",
  statement=r"<b>Matrix of a linear map (Axler 3.30).</b> Let $T\in\mathcal L(V,W)$, $v_1,\dots,v_n$ a basis of $V$, $w_1,\dots,w_m$ a basis of $W$. The matrix $\mathcal M(T)$ is the $m\times n$ matrix $A$ with $Tv_k=\sum_{j=1}^m A_{j,k}w_j$. Then $\mathcal M(Tv)=\mathcal M(T)\mathcal M(v)$ (3.65) and $\mathcal M(ST)=\mathcal M(S)\mathcal M(T)$ (3.43).",
  hint="How do you write a photo edit as a grid of numbers?",
  breakdown=[r"<strong>$Tv_j=\sum_iA_{ij}w_i$</strong> = column $j$ holds the address of where the edit sends basis arrow $v_j$.",
             r"<strong>$[Tv]_w=A[v]_v$</strong> = to edit any arrow, multiply its address by the matrix.",
             r"<strong>$\mathcal M(ST)=\mathcal M(S)\mathcal M(T)$</strong> = doing edit $T$ then edit $S$ is multiplying their matrices (right one first)."],
  conn=r"<strong>The edit's recipe card.</strong> Your app stores an edit as a few numbers: where the 'right' arrow and the 'up' arrow end up. Those two columns are the matrix, and stacking two edits multiplies their recipe cards.",
  cap="Column j of A is the address of Tvⱼ, so Tvⱼ = Σᵢ Aᵢⱼ wᵢ and [Tv]w = A[v]v; two edits in a row multiply: ℳ(ST) = ℳ(S)ℳ(T)."),
20306: dict(d=d20306, stmtKind="WORKED EXAMPLE",
  statement=r"<b>Example.</b> $T:\mathbb R^3\to\mathbb R^2$, $T(x,y,z)=(x+y,y+z)$, with $A=\begin{pmatrix}1&1&0\\0&1&1\end{pmatrix}$. Then $\operatorname{null}T=\operatorname{span}\{(1,-1,1)\}$ (nullity 1), $\operatorname{range}T=\mathbb R^2$ (rank 2), and $3=1+2$. $T$ is surjective but not injective.",
  hint="This edit squashes a 3D scene onto a 2D photo. Which direction is lost?",
  breakdown=[r"<strong>$\operatorname{null}T=\operatorname{span}\{(1,-1,1)\}$</strong> = solve $x+y=0,\ y+z=0$: one line of arrows is squashed.",
             r"<strong>$\operatorname{rank}=2$</strong> = the columns $(1,0),(1,1)$ already span $\mathbb R^2$, so every 2D picture is reachable.",
             r"<strong>$3=1+2$</strong> = rank–nullity checks out; $\operatorname{null}T\ne\{0\}$ means it is not one-to-one."],
  conn=r"<strong>Taking a photo of a 3D scene.</strong> The camera keeps two directions and loses one: every point along the direction $(1,-1,1)$ lands on the same pixel.",
  cap="A has columns (1,0), (1,1), (0,1), so rank 2; null T = span{(1, −1, 1)}, nullity 1; 3 = 1 + 2."),
}

STORY = {
 20301: dict(s="STORY 3 · STEP 1 · THE EDIT", b="Now the main character arrives: a <b>linear map</b>, an edit applied to every arrow at once that keeps the pin fixed and respects mixing.",
   f=[["20206", "the canvas and its bases"]], n=[["20302", "what an edit loses and what it reaches"], ["20305", "write the edit as a matrix"]]),
 20302: dict(s="STORY 3 · STEP 2 · LOST AND REACHED", b="Every edit has a <b>null space</b> (arrows squashed to the pin) and a <b>range</b> (pictures it can produce).",
   f=[["20301", "linear maps"]], n=[["20303", "count them"], ["20304", "one-to-one and onto"]]),
 20303: dict(s="STORY 3 · STEP 3 · THE COUNT", b="<b>Rank–nullity</b>: squashed directions plus surviving directions equal all directions.",
   f=[["20302", "null space and range"], ["20205", "extending a basis"]], n=[["20304", "dimension tests"], ["20403", "square edits: one-to-one ⇔ onto"]]),
 20304: dict(s="STORY 3 · STEP 4 · CAN IT BE UNDONE?", b="One-to-one means only the zero arrow is squashed; onto means the range is everything. Dimensions limit both.",
   f=[["20303", "rank–nullity"]], n=[["20401", "both together: invertible"]]),
 20305: dict(s="STORY 3 · STEP 5 · THE RECIPE CARD", b="With bases on both sides, an edit becomes a <b>matrix</b>: column $j$ is where basis arrow $j$ goes, and composing edits multiplies matrices.",
   f=[["20202", "addresses"], ["20301", "linear maps"]], n=[["20306", "compute one"], ["20404", "change the grid, change the matrix"]]),
 20306: dict(s="STORY 3 · STEP 6 · WITH NUMBERS", b="A full example: matrix, null space, rank, and the rank–nullity check.",
   f=[["20303", "rank–nullity"], ["20305", "the matrix"]], n=[["20401", "when can an edit be undone?"]]),
}

FIX = {cid: {"stmtKind": v["stmtKind"], "statement": v["statement"], "hint": v["hint"], "breakdown": v["breakdown"],
             "personalConnection": v["conn"], "drawingSvg": v["d"](cid), "drawingCaption": v["cap"],
             "textbookImg": None, "textbookRef": None} for cid, v in CARDS.items()}
