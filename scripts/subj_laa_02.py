"""LAA topic 02 (independence, bases, dimension). Photo picture: a basis is the set of
'slider arrows' you combine to reach every point of the photo."""
from laa_lib import *

SUBJECT = "LAA"

def d20201(c):
    O = (60, 100)
    return svg(c,
        pin(*O, "0", -4, 12),
        vec(O, (110, 100), "v₁", 0, 12, "middle"), vec(O, (84, 62), "v₂", -4, -2, "end"),
        dash(110, 100, 134, 62), dash(84, 62, 134, 62), vec(O, (134, 62), "a₁v₁ + a₂v₂", 4, -4),
        N(150, 96, "span = every mix", 7.5, "start"), N(150, 106, "a₁v₁ + … + aₘvₘ", 7.5, "start"),
        N(12, 14, "independent: a₁v₁ + … + aₘvₘ = 0", 7.5, "start"), N(12, 24, "only with a₁ = … = aₘ = 0", 7.5, "start"),
        N(12, 136, "no arrow is a mix of the others", 7.5, "start"))

def d20202(c):
    O = (40, 118)
    b1, b2 = (34, -8), (12, -26)
    p = lambda a, b: (O[0] + a * b1[0] + b * b2[0], O[1] + a * b1[1] + b * b2[1])
    grid = [L(*p(a, 0), *p(a, 4), .5, "2 2") for a in range(0, 6)] + [L(*p(0, b), *p(5, b), .5, "2 2") for b in range(0, 5)]
    v = p(3, 2)
    return svg(c, *grid, pin(*O, "0", -4, 12),
        vec(O, p(1, 0), "b₁", 2, 10, "middle"), vec(O, p(0, 1), "b₂", -4, 0, "end"),
        vec(O, v, "v = 3b₁ + 2b₂", 4, -4),
        N(236, 112, "[v]ʙ = (3, 2)", 8, "end"), N(236, 124, "one address per point", 7.5, "end"),
        N(12, 14, "basis = independent + spanning", 7.5, "start"), N(12, 24, "v = Σ aⱼbⱼ with unique aⱼ", 7.5, "start"))

def d20203(c):
    return svg(c,
        N(120, 12, "swap independent arrows into a spanning list", 8, "middle"),
        *[R(14 + 30 * i, 30, 26, 20, "#ffffff", 1, 3) + N(27 + 30 * i, 44, f"w{'₁₂₃₄'[i]}", 8, "middle") for i in range(4)],
        N(140, 44, "spanning list, length n", 7.5, "start"),
        *[R(14 + 30 * i, 66, 26, 20, "#d9dee7" if i < 2 else "#ffffff", 1, 3) + N(27 + 30 * i, 80, ["u₁", "u₂", "w₃", "w₄"][i], 8, "middle") for i in range(4)],
        N(140, 80, "after 2 swaps: still spans", 7.5, "start"),
        L(74, 52, 74, 64, 1, ar=True),
        N(12, 108, "each uᵢ pushes out one w", 7.5, "start"),
        N(12, 120, "more u's than w's would run out ⇒ m ≤ n", 7.5, "start"),
        N(12, 136, "so every basis has the same length: dim V", 7.5, "start"))

def d20204(c):
    rows = [("ℝ² photo plane", "2"), ("𝒫ₘ: 1, x, …, xᵐ", "m + 1"), ("𝔽ᵐˣⁿ: one slot per entry", "mn"), ("ℒ(V, W): all edits V → W", "dim V · dim W")]
    out = [N(120, 14, "dimension = how many independent sliders", 8, "middle")]
    for i, (a, b) in enumerate(rows):
        y = 34 + 22 * i
        out += [R(10, y - 11, 150, 18, "#f1f5f9", 1, 3), N(16, y + 1, a, 7.5, "start"), N(166, y + 1, "dim = " + b, 7.5, "start")]
    out += [N(120, 128, "U ⊆ V ⇒ dim U ≤ dim V (equal only if U = V)", 7.5, "middle"),
            N(120, 140, "n independent or n spanning arrows ⇒ a basis", 7.5, "middle")]
    return svg(c, *out)

def d20205(c):
    out = [N(120, 12, "trim a spanning list · grow an independent list", 8, "middle")]
    for i, (lab, keep) in enumerate([("v₁", 1), ("v₂ = 2v₁", 0), ("v₃", 1), ("v₄ ∈ span", 0)]):
        x = 10 + 56 * i
        out += [R(x, 28, 50, 18, "#ffffff", 1, 3, None if keep else "3 2"), N(x + 25, 41, lab, 7.2, "middle")]
        if not keep: out.append(L(x + 4, 30, x + 46, 44, .8))
    out += [N(120, 60, "delete what is already in the span ⇒ basis", 7.5, "middle")]
    for i, (lab, new) in enumerate([("u₁", 0), ("u₂", 0), ("+ w₁", 1), ("+ w₂", 1)]):
        x = 10 + 56 * i
        out += [R(x, 76, 50, 18, "#d9dee7" if new else "#f1f5f9", 1, 3), N(x + 25, 89, lab, 7.5, "middle")]
    out += [N(120, 108, "adjoin vectors until it spans ⇒ basis", 7.5, "middle"),
            N(120, 126, "U = span(u's), W = span(added w's)", 7.5, "middle"), N(120, 138, "⇒ V = U ⊕ W", 8, "middle")]
    return svg(c, *out)

def d20206(c):
    O = (60, 104)
    return svg(c,
        sheet([(14, 132), (150, 132), (196, 60), (60, 60)]), N(22, 126, "span = a plane, dim 2", 7, "start"),
        pin(*O, None),
        vec(O, (92, 84), "v₁", -2, -4, "end"), vec(O, (124, 64), "v₂ = 2v₁", 4, -2),
        vec(O, (110, 112), "v₃", 4, 8),
        N(236, 20, "v₁ = (1,2,3)", 7.5, "end"), N(236, 30, "v₂ = (2,4,6)", 7.5, "end"), N(236, 40, "v₃ = (1,0,1)", 7.5, "end"),
        N(236, 98, "2v₁ − v₂ + 0v₃ = 0", 7.5, "end"), N(236, 108, "drop v₂: basis {v₁, v₃}", 7.5, "end"))

CARDS = {
20201: dict(d=d20201, stmtKind="DEFINITION",
  statement=r"<b>Span and linear independence (Axler 2.4, 2.15).</b> The span of $v_1,\dots,v_m\in V$ is $\operatorname{span}(v_1,\dots,v_m)=\{a_1v_1+\dots+a_mv_m: a_i\in\mathbb F\}$, the smallest subspace containing the list. The list is linearly independent if the only choice of $a_1,\dots,a_m\in\mathbb F$ with $a_1v_1+\dots+a_mv_m=0$ is $a_1=\dots=a_m=0$.",
  hint="When is one of your slider arrows wasted because the others can already reach it?",
  breakdown=[r"<strong>$a_1v_1+\dots+a_mv_m$ = a mix of slider arrows.</strong> Each $a_j$ says how far you push slider $j$; the span is every point those pushes can reach.",
             r"<strong>$=0\Rightarrow a_1=\dots=a_m=0$ = no combination brings you back to the pin</strong> unless you push nothing. Then no arrow is a mix of the others.",
             r"<strong>Why it matters:</strong> a list with $0$ in it, or a repeated arrow, always fails, because you can cancel it."],
  conn=r"<strong>Editing sliders that overlap.</strong> If one slider in your app does exactly what two others do together, it is redundant: you can move the photo and bring it back with a nonzero mix. Independent sliders each add a genuinely new direction.",
  cap="The span of v₁, v₂ is every mix a₁v₁ + a₂v₂ from the pin. They are independent because a₁v₁ + a₂v₂ = 0 only when a₁ = a₂ = 0."),
20202: dict(d=d20202, stmtKind="THEOREM",
  statement=r"<b>Criterion for a basis (Axler 2.29).</b> A basis of $V$ is a list of vectors in $V$ that is linearly independent and spans $V$. A list $v_1,\dots,v_n$ is a basis of $V$ if and only if every $v\in V$ can be written uniquely as $v=a_1v_1+\dots+a_nv_n$ with $a_1,\dots,a_n\in\mathbb F$; then $[v]_B=(a_1,\dots,a_n)^\top$ are its coordinates.",
  hint="What do you need so that every point of the photo has exactly one address?",
  breakdown=[r"<strong>$v=\sum_j a_jb_j$ = reach $v$ with the basis sliders.</strong> Spanning means every point can be reached.",
             r"<strong>unique $a_j$ = only one way to get there.</strong> Independence means no second recipe exists.",
             r"<strong>$[v]_B\in\mathbb F^n$ = the address.</strong> The numbers $(a_1,\dots,a_n)$ turn an abstract vector into a column of numbers, so maps become matrices."],
  conn=r"<strong>Grid lines on the photo.</strong> Draw a slanted grid from two arrows $b_1,b_2$. Every point is '3 steps along $b_1$, 2 steps along $b_2$', and that address is unique. Change the grid and the same point gets a new address.",
  cap="Two basis arrows b₁, b₂ lay a grid over the photo. The point v = 3b₁ + 2b₂ has the unique address [v]ʙ = (3, 2)."),
20203: dict(d=d20203, stmtKind="LEMMA",
  statement=r"<b>Length of linearly independent list $\le$ length of spanning list (Axler 2.22).</b> In a finite-dimensional vector space, if $u_1,\dots,u_m$ is linearly independent and $w_1,\dots,w_n$ spans $V$, then $m\le n$. Consequently any two bases of $V$ have the same length (Axler 2.34).",
  hint="Why can't five independent arrows live in a photo that three sliders already cover?",
  breakdown=[r"<strong>$u_1,\dots,u_m$ independent</strong> = arrows that each add a new direction.",
             r"<strong>$w_1,\dots,w_n$ span</strong> = sliders that already reach every point.",
             r"<strong>$m\le n$:</strong> insert each $u_i$ into the spanning list; it becomes dependent, so one $w$ can be removed. If $m>n$ you would run out of $w$'s first, a contradiction."],
  conn=r"<strong>Swapping sliders one at a time.</strong> Replace your app's sliders by new independent ones, one by one, and the set still reaches every point. You can swap in at most as many new sliders as there were old ones.",
  cap="Each independent uᵢ swapped into the spanning list w₁, …, wₙ pushes out one w and the list still spans, so m ≤ n and all bases have the same length."),
20204: dict(d=d20204, stmtKind="PROPOSITION",
  statement=r"<b>Dimension facts.</b> For finite-dimensional $V$: if $U$ is a subspace then $\dim U\le\dim V$, with equality only if $U=V$ (Axler 2.37–2.39). Every independent list of length $\dim V$, and every spanning list of length $\dim V$, is a basis (2.38, 2.42). Also $\dim\mathbb F^n=n$, $\dim\mathcal P_m(\mathbb F)=m+1$, $\dim\mathbb F^{m\times n}=mn$, $\dim\mathcal L(V,W)=(\dim V)(\dim W)$ (3.61).",
  hint="How many independent sliders does each familiar space need?",
  breakdown=[r"<strong>$\dim\mathcal P_m=m+1$</strong> = the sliders $1,x,\dots,x^m$; one per coefficient.",
             r"<strong>$\dim\mathbb F^{m\times n}=mn$</strong> = one slider per matrix entry.",
             r"<strong>$\dim\mathcal L(V,W)=\dim V\dim W$</strong> = an edit is fixed by where it sends each of the $\dim V$ basis arrows, each a point of $W$."],
  conn=r"<strong>Counting the knobs.</strong> A photo plane needs two knobs, a quadratic curve tool needs three (constant, slope, bend), and an edit from a 2D photo to a 3D scene needs $2\times3=6$ numbers. Once you have the right number of independent knobs, you have them all.",
  cap="Dimension counts the independent sliders: 2 for the photo plane, m + 1 for 𝒫ₘ, mn for 𝔽ᵐˣⁿ, dim V · dim W for ℒ(V, W)."),
20205: dict(d=d20205, stmtKind="THEOREM",
  statement=r"<b>Reduce and extend (Axler 2.31, 2.32, 2.33).</b> In a finite-dimensional $V$: every spanning list can be reduced to a basis of $V$; every linearly independent list can be extended to a basis of $V$. Consequently every subspace $U$ of $V$ has a complement: a subspace $W$ with $V=U\oplus W$.",
  hint="How do you turn a messy slider list into a basis, and how do you finish a short one?",
  breakdown=[r"<strong>delete</strong> = go left to right and drop every arrow already in the span of the ones before it. What stays is independent and still spans.",
             r"<strong>adjoin</strong> = add arrows from any spanning list that are not yet in the span, until everything is reached.",
             r"<strong>$V=U\oplus W$</strong> = extend a basis of $U$; the added arrows span the complement $W$."],
  conn=r"<strong>Cleaning up your toolbar.</strong> Remove every tool that only repeats what earlier tools do, and you are left with a basis. If your toolbar can't reach some edit yet, add tools until it can; the new tools form the complement.",
  cap="Top: delete arrows already in the span to reduce a spanning list to a basis. Bottom: adjoin new arrows to extend an independent list; U = span(u's) and the added W give V = U ⊕ W."),
20206: dict(d=d20206, stmtKind="WORKED EXAMPLE",
  statement=r"<b>Example.</b> $v_1=(1,2,3)$, $v_2=(2,4,6)$, $v_3=(1,0,1)$ in $\mathbb R^3$. Since $2v_1-v_2+0v_3=0$ the list is dependent. Removing $v_2$ leaves $v_1,v_3$, independent (not multiples of each other), so $\operatorname{span}(v_1,v_2,v_3)=\operatorname{span}(v_1,v_3)$ has dimension 2.",
  hint="Which of the three arrows is wasted, and what shape do the other two span?",
  breakdown=[r"<strong>$2v_1-v_2+0v_3=0$</strong> = a nonzero recipe that returns to the pin, so the list is dependent.",
             r"<strong>$\operatorname{span}(v_1,v_2,v_3)=\operatorname{span}(v_1,v_3)$</strong> = $v_2$ only repeats $v_1$ (twice as long), so dropping it loses nothing.",
             r"<strong>$\dim=2$</strong> = $v_1$ and $v_3$ point in different directions, so they span a plane through the pin."],
  conn=r"<strong>A duplicate slider.</strong> One tool moves the photo by $(1,2,3)$, another by exactly double that. The second is useless; together with the third tool they only sweep a flat sheet, not the whole space.",
  cap="v₂ = 2v₁ points along v₁, so 2v₁ − v₂ + 0v₃ = 0. Dropping v₂ leaves the basis {v₁, v₃} of a plane: dim = 2."),
}

STORY = {
 20201: dict(s="STORY 2 · STEP 1 · SLIDERS", b="To describe every arrow on the canvas we need a few <b>slider arrows</b> to mix; the useful ones are <b>independent</b>: none is a mix of the others.",
   f=[["20103", "the same zero test for subspaces"]], n=[["20202", "independent and spanning"], ["20206", "spot a dependence"]]),
 20202: dict(s="STORY 2 · STEP 2 · ADDRESSES", b="A <b>basis</b> reaches every point in exactly one way, giving every arrow an address $[v]_B$: this is how arrows become columns of numbers.",
   f=[["20201", "independence and span"]], n=[["20203", "all bases have the same size"], ["20305", "edits become matrices"]]),
 20203: dict(s="STORY 2 · STEP 3 · SAME SIZE", b="Swapping argument: an independent list is never longer than a spanning list, so <b>every basis has the same length</b>.",
   f=[["20202", "what a basis is"]], n=[["20204", "dimension of familiar spaces"]]),
 20204: dict(s="STORY 2 · STEP 4 · COUNT THE KNOBS", b="That common length is the <b>dimension</b>; for the usual spaces it is easy to count.",
   f=[["20203", "why dimension is well defined"], ["20105", "dimension of a sum"]], n=[["20205", "build a basis"], ["20303", "rank–nullity counts with it"]]),
 20205: dict(s="STORY 2 · STEP 5 · BUILD A BASIS", b="Trim a spanning list or grow an independent one: either way you get a basis, and every subspace gets a <b>complement</b>.",
   f=[["20204", "dimension"], ["20102", "direct sums"]], n=[["20206", "do it with numbers"], ["20303", "proof of rank–nullity"]]),
 20206: dict(s="STORY 2 · STEP 6 · WITH NUMBERS", b="A worked example: find the dependence, drop the redundant arrow, read off a basis and the dimension.",
   f=[["20205", "reducing a list"]], n=[["20301", "now let an edit act on the arrows"]]),
}

FIX = {cid: {"stmtKind": v["stmtKind"], "statement": v["statement"], "hint": v["hint"], "breakdown": v["breakdown"],
             "personalConnection": v["conn"], "drawingSvg": v["d"](cid), "drawingCaption": v["cap"],
             "textbookImg": None, "textbookRef": None} for cid, v in CARDS.items()}
