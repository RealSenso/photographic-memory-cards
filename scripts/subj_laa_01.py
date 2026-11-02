"""LAA topic 01 (vector spaces, subspaces, direct sums) in the CMO card format.
Everyday picture: a photo on your phone. Vectors are arrows pinned at the photo's centre 0;
a subspace is a line (or flat sheet) of arrows through that pin."""
from laa_lib import *

SUBJECT = "LAA"

def d20101(c):
    O = (64, 96)
    return svg(c,
        sheet([(12, 126), (144, 126), (192, 66), (60, 66)]), N(20, 120, "U (through the pin)", 7, "start"),
        sheet([(100, 56), (214, 56), (234, 22), (120, 22)], "#ffffff", "3 2"), N(126, 32, "W: the same sheet, shifted", 7, "start"), N(126, 42, "0 ∉ W ✗ not a subspace", 7, "start"),
        pin(*O, "0 ∈ U ✓", -6, 12),
        vec(O, (110, 112), "u", 3, 8), vec(O, (94, 74), "v", -4, -2, "end"),
        dash(110, 112, 140, 90), dash(94, 74, 140, 90), vec(O, (140, 90), "αu + βv ∈ U ✓", 5, 4),
        N(120, 140, "U ≤ V ⇔ 0 ∈ U and αu + βv ∈ U", 8, "middle"))

def d20102(c):
    O = (110, 84)
    return svg(c,
        phone(10, 6, 220, 134),
        L(18, 84, 222, 84, 1), N(222, 80, "U₁", 8, "end"),
        L(64, 136, 162, 12, 1), N(166, 20, "U₂", 8, "start"),
        pin(*O, None), N(O[0] + 6, O[1] + 12, "U₁ ∩ U₂ = {0}", 7.5, "start"),
        vec(O, (170, 84), "u₁", -10, 12, "middle"), vec(O, (134, 54), "u₂", -6, -2, "end"),
        dash(170, 84, 194, 54), dash(134, 54, 194, 54), vec(O, (194, 54), "v = u₁ + u₂", 0, -6, "middle"),
        N(18, 20, "only one way to split v", 7.5, "start"), N(18, 30, "⇒ U₁ + U₂ = U₁ ⊕ U₂", 7.5, "start"))

def d20103(c):
    O = (120, 80)
    return svg(c,
        N(120, 12, "can three arrows cancel back to the pin?", 8, "middle"),
        pin(*O, None),
        vec(O, (60, 58), "u₁ ∈ U₁", -6, -2, "end", 7.5), vec(O, (176, 48), "u₂ ∈ U₂", 4, 0, "start", 7.5), vec(O, (128, 124), "u₃ ∈ U₃", 6, 2, "start", 7.5),
        N(12, 108, "u₁ + u₂ + u₃ = 0", 7.5, "start"), N(12, 118, "⇒ u₁ = u₂ = u₃ = 0 ?", 7.5, "start"),
        N(120, 140, "only with all zero ⇔ the sum is direct", 7.5, "middle"))

def d20104(c):
    O = (92, 80)
    return svg(c,
        L(14, 80, 176, 80, 1), N(176, 76, "U₁", 8, "end"), L(92, 14, 92, 140, 1), N(96, 18, "U₂", 8, "start"),
        L(34, 138, 160, 12, 1, "4 3"), N(156, 20, "U₃", 8, "start"),
        pin(*O, None),
        vec(O, (132, 80), "(1,0)", -6, 10, "middle", 7), vec(O, (92, 40), "(0,1)", -6, 6, "end", 7), vec(O, (52, 120), "(−1,−1)", -4, -2, "end", 7),
        N(236, 50, "Uᵢ ∩ Uⱼ = {0} pairwise,", 7.5, "end"), N(236, 61, "but three nonzero", 7.5, "end"), N(236, 71, "arrows sum to 0:", 7.5, "end"),
        N(236, 83, "not direct ✗", 7.5, "end"), N(236, 104, "(1,0) + (0,1) + (−1,−1)", 7, "end"), N(236, 114, "= (0,0)", 7, "end"))

def d20105(c):
    return svg(c,
        E(92, 72, 58, 40, 0, "#f1f5f9", 1), E(148, 72, 58, 40, 0, "none", 1, "4 3"),
        N(54, 72, "dim U₁", 8, "middle"), N(186, 72, "dim U₂", 8, "middle"),
        N(120, 68, "dim", 7.5, "middle"), N(120, 78, "U₁ ∩ U₂", 7.5, "middle"),
        N(120, 14, "count the shared directions once", 8, "middle"),
        N(120, 128, "dim(U₁ + U₂) = dim U₁ + dim U₂ − dim(U₁ ∩ U₂)", 7.5, "middle"),
        N(120, 140, "two sheets in ℝ³: 2 + 2 − 3 ≥ 1 ⇒ they share a line", 7, "middle"))

def d20106(c):
    return svg(c,
        R(8, 44, 46, 46, "#ffffff", 1, 3), N(31, 71, "A", 10, "middle"), N(31, 102, "any edit", 7, "middle"), N(31, 111, "matrix", 7, "middle"),
        N(62, 71, "=", 10, "middle"),
        R(72, 44, 66, 46, "#f1f5f9", 1, 3), N(105, 64, "(A + Aᵀ)/2", 8, "middle"), N(105, 77, "∈ 𝒮ₙ", 8, "middle"), N(105, 102, "pure stretch:", 7, "middle"), N(105, 111, "Sᵀ = S", 7, "middle"),
        N(146, 71, "+", 10, "middle"),
        R(156, 44, 76, 46, "#d9dee7", 1, 3), N(194, 64, "(A − Aᵀ)/2", 8, "middle"), N(194, 77, "∈ 𝒜ₙ", 8, "middle"), N(194, 102, "pure spin:", 7, "middle"), N(194, 111, "Kᵀ = −K", 7, "middle"),
        N(120, 18, "Mₙ = 𝒮ₙ ⊕ 𝒜ₙ", 9, "middle"),
        N(120, 134, "𝒮ₙ ∩ 𝒜ₙ: Aᵀ = A = −A ⇒ A = 0", 7.5, "middle"))

CARDS = {
20101: dict(d=d20101, stmtKind="DEFINITION",
  statement=r"<b>Subspace.</b> A subset $U$ of a vector space $V$ over $\mathbb F$ is a subspace of $V$ if $U$ is itself a vector space with the same addition and scalar multiplication. Equivalently (Axler 1.34): $0\in U$; $u,w\in U\Rightarrow u+w\in U$; and $\lambda\in\mathbb F,\ u\in U\Rightarrow\lambda u\in U$.",
  hint="Which three checks does a set of arrows need before it counts as a subspace?",
  breakdown=[r"<strong>$0\in U$ = the set contains the pin itself.</strong> The zero arrow (no movement) must be in it; a sheet that misses the pin fails at once.",
             r"<strong>$\alpha u+\beta v\in U$ = mixing arrows keeps you inside.</strong> Stretch $u$, stretch $v$, add them tip to tail: still in $U$. This is closure under addition and scaling in one line.",
             r"<strong>Why only these:</strong> the other vector-space rules (associativity, distributivity) are inherited from $V$, so these are the only things that can break."],
  conn=r"<strong>A sheet through the pin.</strong> Put your fingers on the photo and drag: every arrow starts at the centre pin. A flat sheet through the pin is a subspace, because any mix of two of its arrows stays in the sheet. Slide the sheet off the pin and the zero arrow is no longer in it.",
  cap="The shaded sheet U goes through the centre pin 0, and any mix αu + βv of two of its arrows stays in it. The dashed sheet W is shifted off the pin, so 0 ∉ W and it fails."),
20102: dict(d=d20102, stmtKind="DEFINITION",
  statement=r"<b>Sum and direct sum.</b> For subspaces $U_1,\dots,U_m$ of $V$, $U_1+\dots+U_m=\{u_1+\dots+u_m: u_i\in U_i\}$. The sum is a direct sum, written $U_1\oplus\dots\oplus U_m$, if each element of it can be written in only one way as $u_1+\dots+u_m$ with $u_i\in U_i$. For two subspaces (Axler 1.46): $U_1+U_2$ is direct $\iff U_1\cap U_2=\{0\}$.",
  hint="When can every arrow be split into a U₁ part and a U₂ part in exactly one way?",
  breakdown=[r"<strong>$U_1+U_2$ = every arrow you can build</strong> by adding an arrow along $U_1$ to an arrow along $U_2$.",
             r"<strong>$U_1\oplus U_2$ = the split is unique.</strong> Each arrow $v$ has only one pair $(u_1,u_2)$.",
             r"<strong>$U_1\cap U_2=\{0\}$ = the two lines share only the pin.</strong> If they shared a direction, you could move some of it from one part to the other and get a second split."],
  conn=r"<strong>Swipe right, swipe up.</strong> Every drag on the photo is some amount sideways plus some amount up, and there is only one way to say it, because the sideways line and the up line meet only at the pin.",
  cap="The lines U₁ and U₂ meet only at the pin (U₁ ∩ U₂ = {0}), so the arrow v = u₁ + u₂ splits into a U₁ part and a U₂ part in exactly one way."),
20103: dict(d=d20103, stmtKind="THEOREM",
  statement=r"<b>Condition for a direct sum (Axler 1.45).</b> Let $U_1,\dots,U_m$ be subspaces of $V$. Then $U_1+\dots+U_m$ is a direct sum if and only if the only way to write $0$ as $u_1+\dots+u_m$, with each $u_i\in U_i$, is by taking every $u_i=0$.",
  hint="Instead of checking every arrow, which single arrow is enough to test?",
  breakdown=[r"<strong>$\sum u_i=0$ with $u_i\in U_i$</strong> = arrows from different subspaces that, added tip to tail, bring you back to the pin.",
             r"<strong>$\Rightarrow u_1=\dots=u_m=0$</strong> = the only way back to the pin is to not move at all. Then 0 has one representation.",
             r"<strong>Why 0 is enough:</strong> two splits of the same $v$ subtract to a split of 0, so uniqueness at 0 gives uniqueness everywhere."],
  conn=r"<strong>Three drags that undo each other.</strong> If you can drag the photo along three different lines and end exactly where you started, the lines are tangled and the sum is not direct. A direct sum means the only way back is to not drag at all.",
  cap="Three arrows u₁, u₂, u₃ from three subspaces. The sum is direct exactly when u₁ + u₂ + u₃ = 0 forces u₁ = u₂ = u₃ = 0."),
20104: dict(d=d20104, stmtKind="WORKED EXAMPLE",
  statement=r"<b>Counterexample.</b> In $\mathbb R^2$ let $U_1=\{(x,0)\}$, $U_2=\{(0,y)\}$, $U_3=\{(x,x)\}$. Then $U_i\cap U_j=\{0\}$ for all $i\ne j$, but $U_1+U_2+U_3$ is not a direct sum, since $(1,0)+(0,1)+(-1,-1)=(0,0)$. For $m\ge3$ the correct test is $U_j\cap\sum_{i\ne j}U_i=\{0\}$ for every $j$.",
  hint="Three lines meet only at the pin. Why can three nonzero arrows still cancel?",
  breakdown=[r"<strong>$U_i\cap U_j=\{0\}$ for each pair</strong> = any two of the three lines meet only at the pin.",
             r"<strong>$(1,0)+(0,1)+(-1,-1)=0$</strong> = three nonzero arrows, one on each line, that bring you back, so 0 has two representations.",
             r"<strong>Why pairs are not enough:</strong> $U_3$ already lies inside $U_1+U_2$ (the whole photo). Each subspace must avoid the sum of all the others."],
  conn=r"<strong>Three drags on a flat photo.</strong> Drag right, then up, then diagonally back: you are where you started. Each pair of lines crosses only at the pin, but the photo is only 2D, so a third line adds nothing new.",
  cap="Lines U₁, U₂, U₃ in ℝ² meet pairwise only at the pin, yet (1,0) + (0,1) + (−1,−1) = (0,0) with three nonzero arrows, so the sum is not direct."),
20105: dict(d=d20105, stmtKind="THEOREM",
  statement=r"<b>Dimension of a sum (Axler 2.43).</b> If $V_1$ and $V_2$ are subspaces of a finite-dimensional vector space, then $\dim(V_1+V_2)=\dim V_1+\dim V_2-\dim(V_1\cap V_2)$. In particular, the sum is direct $\iff\dim(V_1+V_2)=\dim V_1+\dim V_2$.",
  hint="Two subspaces share some directions. How many independent directions does their sum really have?",
  breakdown=[r"<strong>$\dim U_1+\dim U_2$</strong> = add up the independent directions of each subspace.",
             r"<strong>$-\dim(U_1\cap U_2)$</strong> = the shared directions were counted twice, so remove them once (like $|A\cup B|=|A|+|B|-|A\cap B|$).",
             r"<strong>Consequence:</strong> if $\dim U_1+\dim U_2>\dim V$ they must share a direction, e.g. two planes in $\mathbb R^3$ share at least a line."],
  conn=r"<strong>Two editing sliders that overlap.</strong> One tool moves the photo left–right and up–down, another moves it up–down and in–out. Together they give 3 directions, not 4: the shared up–down is counted once.",
  cap="Subspaces U₁ and U₂ overlap in U₁ ∩ U₂. dim(U₁ + U₂) = dim U₁ + dim U₂ − dim(U₁ ∩ U₂): the shared directions are counted once."),
20106: dict(d=d20106, stmtKind="WORKED EXAMPLE",
  statement=r"<b>Claim.</b> $M_{n\times n}(\mathbb R)=\mathcal S_n\oplus\mathcal A_n$, where $\mathcal S_n=\{A:A^\top=A\}$ and $\mathcal A_n=\{A:A^\top=-A\}$. Proof: $A=\tfrac12(A+A^\top)+\tfrac12(A-A^\top)$ gives the sum, and $A\in\mathcal S_n\cap\mathcal A_n\Rightarrow A=-A\Rightarrow A=0$ gives directness. Also $\dim\mathcal S_n+\dim\mathcal A_n=\tfrac{n(n+1)}2+\tfrac{n(n-1)}2=n^2$.",
  hint="How does any photo edit matrix split into a pure-stretch part and a pure-spin part?",
  breakdown=[r"<strong>$\tfrac12(A+A^\top)\in\mathcal S_n$</strong> = average $A$ with its mirror image: the result equals its own transpose (a stretch along fixed axes).",
             r"<strong>$\tfrac12(A-A^\top)\in\mathcal A_n$</strong> = half the difference: its transpose is its negative (an infinitesimal spin).",
             r"<strong>$\mathcal S_n\cap\mathcal A_n=\{0\}$</strong> = a matrix that is both has $A=A^\top=-A$, so it is zero, and the split is unique."],
  conn=r"<strong>Stretch plus spin.</strong> Any small edit you make with two fingers is part stretch (pull the fingers apart along some axes) and part spin (twist them). A move that is both a pure stretch and a pure spin is no move at all.",
  cap="Any matrix A splits as (A + Aᵀ)/2 in 𝒮ₙ (stretch) plus (A − Aᵀ)/2 in 𝒜ₙ (spin), and 𝒮ₙ ∩ 𝒜ₙ = {0}, so Mₙ = 𝒮ₙ ⊕ 𝒜ₙ."),
}

STORY = {
 20101: dict(s="STORY 1 · STEP 1 · THE CANVAS", b="Before any edit can act we need the canvas it acts on: a <b>vector space</b> of arrows pinned at the centre, and inside it the <b>subspaces</b>, sheets through the pin that are closed under mixing arrows.",
   f=[], n=[["20102", "join two subspaces"], ["20201", "how many arrows build a subspace"]]),
 20102: dict(s="STORY 1 · STEP 2 · JOIN SUBSPACES", b="Two subspaces together reach every added-up arrow. When they share only the pin, every arrow splits into one piece from each: a <b>direct sum</b>.",
   f=[["20101", "what a subspace is"]], n=[["20103", "a test for many subspaces"], ["20105", "counting the directions"]]),
 20103: dict(s="STORY 1 · STEP 3 · ONE TEST FOR ALL", b="Checking uniqueness for every arrow is too much work: checking that <b>only the zero trip</b> returns to the pin is enough, for any number of subspaces.",
   f=[["20102", "direct sum of two"]], n=[["20104", "why pairwise checks fail"], ["20201", "the same test for vectors: independence"]]),
 20104: dict(s="STORY 1 · STEP 4 · THE TRAP", b="With three or more subspaces, meeting pairwise only at the pin is <b>not</b> enough: use the zero test.",
   f=[["20103", "the zero test"]], n=[["20105", "count dimensions to spot it"]]),
 20105: dict(s="STORY 1 · STEP 5 · COUNT DIRECTIONS", b="Dimension counts the independent directions; for a sum, the <b>shared directions are counted once</b>.",
   f=[["20102", "sum of subspaces"], ["20104", "an overlap that hides"]], n=[["20106", "a split where the count adds up"], ["20203", "what dimension really is"]]),
 20106: dict(s="STORY 1 · STEP 6 · A REAL SPLIT", b="A full example: every matrix splits uniquely into a <b>stretch + spin</b> (symmetric + skew), and the dimensions add up to $n^2$.",
   f=[["20105", "the dimension count"], ["20102", "direct sum"]], n=[["21201", "symmetric edits return as self-adjoint"]]),
}

FIX = {cid: {"stmtKind": v["stmtKind"], "statement": v["statement"], "hint": v["hint"], "breakdown": v["breakdown"],
             "personalConnection": v["conn"], "drawingSvg": v["d"](cid), "drawingCaption": v["cap"],
             "textbookImg": None, "textbookRef": None} for cid, v in CARDS.items()}
