"""LAA topic 11 (projections, Gram-Schmidt, QR). Photo picture: projecting is casting an
arrow's shadow onto a line or sheet; Gram-Schmidt straightens a slanted grid into a square one."""
from laa_lib import *

SUBJECT = "LAA"

def d21101(c):
    O = (40, 112)
    return svg(c,
        L(14, 112 + 26 * .2, 230, 112 - 190 * .2, .9), N(230, 68, "line of u", 7, "end"),
        pin(*O, None), vec(O, (90, 102), "u", 0, 12, "middle"),
        vec(O, (130, 40), "v", -4, -2, "end"), vec(O, (146, 91), "Pᵤv", 4, 10, "middle"),
        dash(130, 40, 146, 91), N(142, 58, "v − Pᵤv ⊥ u", 7.5, "start"),
        N(12, 14, "Pᵤv = (⟨v, u⟩ / ⟨u, u⟩) u", 8, "start"),
        N(12, 26, "the shadow is the closest point on the line", 7, "start"))

def d21102(c):
    O = (40, 112)
    return svg(c,
        pin(*O, None),
        vec(O, (120, 112), "v₁ → e₁", 6, 4, "start", 7.5),
        vec(O, (110, 40), "v₂", -4, -2, "end", 7.5), dash(110, 40, 110, 112), N(110, 124, "⟨v₂, e₁⟩e₁", 7, "middle"),
        vec(O, (40, 40), "u₂ = v₂ − ⟨v₂, e₁⟩e₁", 4, -4, "start", 7.5),
        N(236, 70, "e₂ = u₂ / ‖u₂‖", 7.5, "end"),
        N(236, 98, "uₖ = vₖ − Σ ⟨vₖ, eⱼ⟩eⱼ (j < k)", 7.2, "end"),
        N(236, 112, "span(e₁..eₖ) = span(v₁..vₖ)", 7.2, "end"),
        N(12, 14, "remove the shadows on earlier rulers, then normalize", 7.5, "start"))

def d21103(c):
    O = (90, 90)
    return svg(c,
        sheet([(20, 120), (150, 120), (190, 70), (60, 70)]), N(26, 114, "U", 8, "start"),
        L(90, 140, 90, 14, 1), N(94, 20, "U⊥", 8, "start"), pin(*O, None),
        vec(O, (160, 34), "v", 4, 0), vec(O, (160, 90), "Pᵤv", 4, 8), vec(O, (90, 34), None, d="3 2"), N(86, 40, "v − Pᵤv", 7, "end"),
        dash(160, 34, 160, 90), dash(160, 34, 90, 34),
        N(236, 120, "V = U ⊕ U⊥", 8.5, "end"), N(236, 132, "dim U⊥ = dim V − dim U", 7, "end"), N(236, 142, "(U⊥)⊥ = U", 7, "end"))

def d21104(c):
    O = (70, 96)
    return svg(c,
        sheet([(14, 124), (150, 124), (196, 66), (60, 66)]), N(20, 118, "U", 8, "start"), pin(*O, None),
        dot(150, 30, None, r=2.4), N(154, 26, "v", 8, "start"), dot(150, 96, None, r=2.4), N(154, 104, "Pᵤv", 8, "start"),
        L(150, 30, 150, 96, 1, "3 2"), N(156, 62, "shortest", 7, "start"),
        dot(104, 110, None, r=2), L(150, 30, 104, 110, .8, "1 2"), N(98, 116, "any u", 7, "end"),
        N(12, 14, "Pᵤv = Σ ⟨v, eⱼ⟩eⱼ", 8, "start"), N(12, 26, "‖v − Pᵤv‖ = min over u ∈ U of ‖v − u‖", 7.5, "start"),
        N(236, 140, "P² = P = P*", 8, "end"))

def d21105(c):
    return svg(c,
        N(120, 12, "Gram–Schmidt on the columns of A, kept as a recipe", 7.5, "middle"),
        R(14, 30, 50, 60, "#ffffff", 1, 3), N(39, 64, "A", 10, "middle"), N(39, 102, "columns aₖ", 7, "middle"),
        N(72, 64, "=", 10, "middle"),
        R(82, 30, 50, 60, "#f1f5f9", 1, 3), N(107, 64, "Q", 10, "middle"), N(107, 102, "orthonormal qₖ", 7, "middle"), N(107, 112, "Q*Q = I", 7, "middle"),
        PG("142,30 192,30 192,90", "#d9dee7", 1), R(142, 30, 50, 60, "none", 1, 0), N(178, 54, "R", 10, "middle"),
        N(167, 102, "upper triangular", 7, "middle"), N(167, 112, "Rⱼₖ = ⟨aₖ, qⱼ⟩", 7, "middle"),
        N(120, 134, "Ax = b ⇔ Rx = Q*b (back-substitute)", 7.5, "middle"))

def d21106(c):
    O = (60, 108)
    return svg(c,
        pin(*O, None),
        vec(O, (130, 108), "v₁ = (1,1,0)", 4, 4, "start", 7.5),
        vec(O, (124, 48), "v₂ = (1,0,1)", 4, -2, "start", 7.5), dash(124, 48, 95, 108), N(95, 120, "½(1,1,0)", 7, "middle"),
        vec(O, (89, 48), "u₂ = (½, −½, 1)", -4, -4, "end", 7.5),
        N(12, 20, "e₁ = (1,1,0)/√2", 7.5, "start"), N(12, 32, "e₂ = (1,−1,2)/√6", 7.5, "start"),
        N(236, 128, "⟨e₁, e₂⟩ = (1 − 1 + 0)/√12 = 0 ✓", 7.2, "end"))

CARDS = {
21101: dict(d=d21101, stmtKind="PROPOSITION",
  statement=r"<b>Orthogonal decomposition (Axler 6.13).</b> Suppose $u,v\in V$ with $u\ne0$. Set $P_uv=\frac{\langle v,u\rangle}{\|u\|^2}u$. Then $\langle v-P_uv,u\rangle=0$, so $v=P_uv+(v-P_uv)$ splits $v$ into a part along $u$ and a part orthogonal to $u$; and $P_uv$ is the multiple of $u$ closest to $v$.",
  hint="Where does an arrow's shadow land on a line, and why is it the closest point?",
  breakdown=[r"<strong>$P_uv=\frac{\langle v,u\rangle}{\langle u,u\rangle}u$</strong> = the shadow of $v$ on the line of $u$; dividing by $\langle u,u\rangle$ makes it independent of $u$'s length.",
             r"<strong>$v-P_uv\perp u$</strong> = what is left over drops straight down onto the line.",
             r"<strong>closest point</strong> = by Pythagoras every other point on the line is farther from $v$."],
  conn=r"<strong>Noon shadow.</strong> Hold an arrow above a line drawn on the photo with the light straight overhead. Its shadow is the projection, and the drop from its tip to the shadow is perpendicular.",
  cap="The shadow of v on the line of u is Pᵤv = (⟨v, u⟩/⟨u, u⟩)u; the drop v − Pᵤv is perpendicular to u."),
21102: dict(d=d21102, stmtKind="ALGORITHM",
  statement=r"<b>Gram–Schmidt procedure (Axler 6.32).</b> Let $v_1,\dots,v_m$ be linearly independent. Set $e_1=v_1/\|v_1\|$ and for $k=2,\dots,m$: $u_k=v_k-\sum_{j\lt k}\langle v_k,e_j\rangle e_j$, $e_k=u_k/\|u_k\|$. Then $e_1,\dots,e_m$ is orthonormal and $\operatorname{span}(e_1,\dots,e_k)=\operatorname{span}(v_1,\dots,v_k)$ for each $k$.",
  hint="How do you turn a slanted set of rulers into a square one, one ruler at a time?",
  breakdown=[r"<strong>$u_k=v_k-\sum_{j\lt k}\langle v_k,e_j\rangle e_j$</strong> = subtract the shadows of $v_k$ on all the rulers already made.",
             r"<strong>$e_k=u_k/\|u_k\|$</strong> = scale what is left to unit length.",
             r"<strong>same spans</strong> = each new ruler only uses the first $k$ old arrows, so nothing is lost and the relation is triangular (this is QR)."],
  conn=r"<strong>Straightening a crooked grid.</strong> Keep the first ruler. For the second, remove the part that lies along the first, then cut it to unit length. Every new ruler is made perpendicular to all earlier ones.",
  cap="u₂ = v₂ − ⟨v₂, e₁⟩e₁ removes v₂'s shadow on e₁; normalizing gives e₂ ⊥ e₁ with the same span."),
21103: dict(d=d21103, stmtKind="THEOREM",
  statement=r"<b>Orthogonal complement (Axler 6.46, 6.47, 6.50, 6.51).</b> For $U\subseteq V$, $U^\perp=\{w\in V:\langle w,u\rangle=0\ \forall u\in U\}$ is a subspace and $U\cap U^\perp=\{0\}$. If $U$ is finite-dimensional then $V=U\oplus U^\perp$; if $V$ is finite-dimensional then $\dim U^\perp=\dim V-\dim U$ and $(U^\perp)^\perp=U$.",
  hint="Every arrow splits into a part on the sheet and a part sticking straight out of it. Why uniquely?",
  breakdown=[r"<strong>$U^\perp$</strong> = all arrows perpendicular to the whole sheet $U$.",
             r"<strong>$V=U\oplus U^\perp$</strong> = every $v$ is its shadow $P_Uv$ plus a perpendicular part, in one way only.",
             r"<strong>$\dim U^\perp=\dim V-\dim U$, $(U^\perp)^\perp=U$</strong> = the two pieces share out the dimensions, and taking perpendiculars twice brings you back."],
  conn=r"<strong>Floor and pole.</strong> In a 3D scene the floor $U$ is a plane and its perpendicular is the vertical pole. Every arrow is a floor part plus a pole part.",
  cap="v splits into Pᵤv in the sheet U and v − Pᵤv in U⊥: V = U ⊕ U⊥, with dim U⊥ = dim V − dim U."),
21104: dict(d=d21104, stmtKind="THEOREM",
  statement=r"<b>Minimizing distance to a subspace (Axler 6.58, 6.61).</b> Let $U$ be finite-dimensional with orthonormal basis $e_1,\dots,e_m$. Then $P_Uv=\sum_j\langle v,e_j\rangle e_j$, and $\|v-P_Uv\|\le\|v-u\|$ for all $u\in U$, with equality only for $u=P_Uv$. $P_U$ satisfies $P_U^2=P_U=P_U^*$.",
  hint="Which point of the sheet is closest to an arrow's tip?",
  breakdown=[r"<strong>$P_Uv=\sum_j\langle v,e_j\rangle e_j$</strong> = add up the shadows on each ruler of $U$.",
             r"<strong>$\|v-P_Uv\|=\min_{u\in U}\|v-u\|$</strong> = the straight drop is the shortest way to the sheet (best approximation).",
             r"<strong>$P^2=P=P^*$</strong> = projecting twice changes nothing, and the projection is self-adjoint."],
  conn=r"<strong>Closest legal edit.</strong> If only edits in a certain sheet are allowed, the best one is the shadow of what you wanted. Projecting a shadow again leaves it where it is.",
  cap="Pᵤv is where v drops straight onto the sheet U, the closest point: ‖v − Pᵤv‖ = min ‖v − u‖. Also P² = P = P*."),
21105: dict(d=d21105, stmtKind="THEOREM",
  statement=r"<b>QR factorization (Axler 7.58).</b> If $A\in\mathbb F^{m\times n}$ has linearly independent columns $a_1,\dots,a_n$, then $A=QR$ where $Q$ has orthonormal columns ($Q^*Q=I$) and $R$ is upper triangular with positive diagonal, $R_{jk}=\langle a_k,q_j\rangle$. Then $Ax=b$ (or its least-squares version) reduces to $Rx=Q^*b$.",
  hint="What record does Gram–Schmidt leave behind when it straightens the columns?",
  breakdown=[r"<strong>$Q$</strong> = the straightened, unit-length columns $q_k$ that Gram–Schmidt produces.",
             r"<strong>$R_{jk}=\langle a_k,q_j\rangle$</strong> = how much of each old column lies along each new ruler; triangular because $a_k$ only uses $q_1,\dots,q_k$.",
             r"<strong>$Rx=Q^*b$</strong> = multiply by $Q^*$ and the system becomes triangular: solve by back-substitution."],
  conn=r"<strong>Square grid plus a conversion chart.</strong> $Q$ is a square grid of rulers, $R$ is the chart that rebuilds the original slanted columns from it.",
  cap="Gram–Schmidt on the columns gives A = QR: Q has orthonormal columns (Q*Q = I), R is upper triangular with Rⱼₖ = ⟨aₖ, qⱼ⟩."),
21106: dict(d=d21106, stmtKind="WORKED EXAMPLE",
  statement=r"<b>Example.</b> $v_1=(1,1,0)$, $v_2=(1,0,1)$. $e_1=\tfrac1{\sqrt2}(1,1,0)$; $\langle v_2,e_1\rangle=\tfrac1{\sqrt2}$, so $u_2=v_2-\tfrac12(1,1,0)=(\tfrac12,-\tfrac12,1)$, $\|u_2\|=\sqrt{3/2}$, $e_2=\tfrac1{\sqrt6}(1,-1,2)$. Check: $\langle e_1,e_2\rangle=0$.",
  hint="Straighten (1,0,1) against (1,1,0). What is left?",
  breakdown=[r"<strong>$e_1=\tfrac1{\sqrt2}(1,1,0)$</strong> = the first ruler is just $v_1$ at unit length.",
             r"<strong>$u_2=(\tfrac12,-\tfrac12,1)$</strong> = remove $v_2$'s shadow $\tfrac12(1,1,0)$ on the first ruler.",
             r"<strong>$e_2=\tfrac1{\sqrt6}(1,-1,2)$</strong> = normalize; the dot product with $e_1$ is $0$."],
  conn=r"<strong>Fixing a crooked second ruler.</strong> The second arrow leans half-way along the first; take that lean away and you get a ruler at right angles.",
  cap="u₂ = v₂ − ½(1,1,0) = (½, −½, 1), giving e₁ = (1,1,0)/√2 and e₂ = (1,−1,2)/√6 with ⟨e₁, e₂⟩ = 0."),
}

STORY = {
 21101: dict(s="STORY 11 · STEP 1 · SHADOW ON A LINE", b="With a ruler we can cast <b>shadows</b>: the projection onto a line is the closest point on it.",
   f=[["21005", "shadows give coordinates"]], n=[["21102", "straighten a grid"], ["21104", "shadow on a sheet"]]),
 21102: dict(s="STORY 11 · STEP 2 · STRAIGHTEN THE GRID", b="<b>Gram–Schmidt</b> removes earlier shadows one ruler at a time, turning any basis into an orthonormal one.",
   f=[["21101", "projection on a line"]], n=[["21105", "keep the recipe: QR"], ["21106", "do it by hand"]]),
 21103: dict(s="STORY 11 · STEP 3 · SHEET AND POLE", b="Every subspace has a perpendicular partner $U^\\perp$, and $V=U\\oplus U^\\perp$.",
   f=[["21102", "orthonormal bases exist"], ["20102", "direct sums"]], n=[["21104", "the closest point"], ["21202", "null T* ⊥ range T"]]),
 21104: dict(s="STORY 11 · STEP 4 · CLOSEST POINT", b="The projection onto a subspace is the <b>best approximation</b>: the straight drop is the shortest.",
   f=[["21103", "U ⊕ U⊥"]], n=[["21601", "least squares = project b"], ["21105", "QR"]]),
 21105: dict(s="STORY 11 · STEP 5 · QR", b="Gram–Schmidt as a factorization: $A=QR$, which makes solving systems triangular.",
   f=[["21102", "Gram–Schmidt"]], n=[["21603", "least squares via QR"]]),
 21106: dict(s="STORY 11 · STEP 6 · WITH NUMBERS", b="Gram–Schmidt on two concrete arrows in $\\mathbb R^3$.",
   f=[["21102", "the algorithm"]], n=[["21201", "next: the adjoint edit"]]),
}

FIX = {cid: {"stmtKind": v["stmtKind"], "statement": v["statement"], "hint": v["hint"], "breakdown": v["breakdown"],
             "personalConnection": v["conn"], "drawingSvg": v["d"](cid), "drawingCaption": v["cap"],
             "textbookImg": None, "textbookRef": None} for cid, v in CARDS.items()}
