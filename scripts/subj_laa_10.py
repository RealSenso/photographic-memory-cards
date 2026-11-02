"""LAA topic 10 (inner products, norms, orthogonality). Photo picture: the inner product
measures how much one arrow points along another (the length of its shadow on it)."""
from laa_lib import *
import math

SUBJECT = "LAA"

def d21001(c):
    O = (60, 104)
    return svg(c,
        pin(*O, None), vec(O, (180, 104), "v", 0, 10, "middle"), vec(O, (130, 50), "u", -4, -2, "end"),
        dash(130, 50, 130, 104), N(130, 116, "shadow of u on v", 7, "middle"),
        N(12, 14, "⟨u, v⟩ = how much u points along v (× |v|)", 7.5, "start"),
        N(236, 40, "⟨u, v⟩ = conj ⟨v, u⟩", 7.5, "end"), N(236, 52, "⟨λu, v⟩ = λ⟨u, v⟩", 7.5, "end"), N(236, 64, "⟨u, λv⟩ = λ̄⟨u, v⟩", 7.5, "end"),
        N(12, 136, "⟨v, v⟩ ≥ 0, = 0 only for v = 0", 7.5, "start"))

def d21002(c):
    O = (50, 110)
    th = math.radians(40)
    u = (O[0] + 110 * math.cos(th), O[1] - 110 * math.sin(th))
    return svg(c,
        pin(*O, None), vec(O, (200, 110), "v", 0, 10, "middle"), vec(O, u, "u", -4, -2, "end"),
        dash(u[0], u[1], u[0], 110), P(f"M {O[0] + 22} {O[1]} A 22 22 0 0 0 {O[0] + 22 * math.cos(th):.1f} {O[1] - 22 * math.sin(th):.1f}", "none", .9),
        N(O[0] + 28, O[1] - 6, "θ", 8, "start"),
        N(u[0], 124, "shadow ≤ |u|", 7, "middle"),
        N(12, 14, "|⟨u, v⟩| ≤ ‖u‖ ‖v‖", 8.5, "start"), N(12, 28, "cos θ = ⟨u, v⟩ / (‖u‖ ‖v‖)", 7.5, "start"),
        N(236, 40, "equality ⇔ u, v on one line", 7, "end"), N(12, 140, "‖v‖ = √⟨v, v⟩: the arrow's length", 7, "start"))

def d21003(c):
    O = (40, 112)
    u, v = (140, 112), (80, 52)
    s = (180, 52)
    return svg(c,
        sheet([O, u, s, v], "#f1f5f9"), pin(*O, None),
        vec(O, u, "u", 0, 10, "middle"), vec(O, v, "v", -4, 0, "end"), vec(O, s, "u + v", 4, -2), arrow(140, 112, 80, 52, 1.1, "3 2"), N(116, 76, "u − v", 7.5, "start"),
        N(236, 20, "‖u + v‖ ≤ ‖u‖ + ‖v‖", 7.5, "end"),
        N(120, 128, "‖u + v‖² + ‖u − v‖² = 2‖u‖² + 2‖v‖²", 7.5, "middle"),
        N(120, 140, "⟨u, v⟩ = ¼(‖u + v‖² − ‖u − v‖²)  (real case)", 7, "middle"))

def d21004(c):
    O = (50, 112)
    return svg(c,
        pin(*O, None), vec(O, (150, 112), "u", 0, 10, "middle"), vec(O, (50, 42), "v", -4, 0, "end"), vec(O, (150, 42), "u + v", 4, -2),
        dash(150, 112, 150, 42), dash(50, 42, 150, 42), R(50, 102, 10, 10, "none", .8),
        N(236, 70, "⟨u, v⟩ = 0", 8, "end"), N(236, 84, "‖u + v‖² = ‖u‖² + ‖v‖²", 7.5, "end"),
        N(120, 14, "‖u + v‖² = ‖u‖² + ‖v‖² + 2 Re⟨u, v⟩", 7.5, "middle"),
        N(236, 128, "the cross term vanishes", 7, "end"))

def d21005(c):
    O = (60, 108)
    v = (150, 48)
    return svg(c,
        pin(*O, None), vec(O, (100, 108), "e₁", 0, 10, "middle"), vec(O, (60, 68), "e₂", -4, 0, "end"), vec(O, v, "v", 4, -2),
        dash(150, 48, 150, 108), dash(150, 48, 60, 48),
        N(150, 120, "⟨v, e₁⟩", 7.5, "middle"), N(56, 48, "⟨v, e₂⟩", 7.5, "end"),
        N(236, 72, "v = Σ ⟨v, eⱼ⟩ eⱼ", 8, "end"), N(236, 86, "‖v‖² = Σ |⟨v, eⱼ⟩|²", 7.5, "end"),
        N(12, 14, "⟨eᵢ, eⱼ⟩ = δᵢⱼ: a square grid of unit rulers", 7.5, "start"),
        N(236, 136, "no system to solve: just read the shadows", 7, "end"))

def d21006(c):
    O = (40, 112)
    s = 26
    P2 = lambda x, y: (O[0] + s * x, O[1] - s * y)
    return svg(c,
        pin(*O, None), vec(O, P2(3, 1), "v = (3,1)", 4, 4), vec(O, P2(1, 2), "u = (1,2)", -2, -4, "end"),
        dash(*P2(1, 2), *P2(1.5, .5)), vec(O, P2(1.5, .5), None, d="3 2"), N(P2(1.5, .5)[0] + 4, P2(1.5, .5)[1] + 12, "proj = (1.5, 0.5)", 7, "start"),
        N(236, 20, "⟨u, v⟩ = 3 + 2 = 5", 7.5, "end"), N(236, 32, "‖u‖ = √5, ‖v‖ = √10", 7.5, "end"),
        N(236, 46, "5 ≤ √50 ≈ 7.07 ✓", 7.5, "end"), N(236, 60, "cos θ = 5/√50 = 1/√2", 7.5, "end"), N(236, 72, "θ = 45°", 8, "end"))

CARDS = {
21001: dict(d=d21001, stmtKind="DEFINITION",
  statement=r"<b>Inner product (Axler 6.2).</b> An inner product on $V$ is a function $(u,v)\mapsto\langle u,v\rangle\in\mathbb F$ with: $\langle v,v\rangle\ge0$, and $=0$ only for $v=0$; additivity and homogeneity in the first slot, $\langle u+w,v\rangle=\langle u,v\rangle+\langle w,v\rangle$, $\langle\lambda u,v\rangle=\lambda\langle u,v\rangle$; and conjugate symmetry $\langle u,v\rangle=\overline{\langle v,u\rangle}$. Consequently $\langle u,\lambda v\rangle=\bar\lambda\langle u,v\rangle$.",
  hint="How do you measure how much one arrow points along another?",
  breakdown=[r"<strong>$\langle u,v\rangle=\overline{\langle v,u\rangle}$</strong> = swapping the two arrows conjugates the answer (over $\mathbb R$ it is symmetric).",
             r"<strong>$\langle\lambda u,v\rangle=\lambda\langle u,v\rangle$</strong> = stretch the first arrow and the measurement stretches with it.",
             r"<strong>$\langle u,\lambda v\rangle=\bar\lambda\langle u,v\rangle$</strong> = in the second slot a complex factor comes out conjugated."],
  conn=r"<strong>The shadow ruler.</strong> Shine a light straight down onto the line of $v$: the length of $u$'s shadow, times the length of $v$, is $\langle u,v\rangle$. An arrow's shadow on itself is its length squared, never negative.",
  cap="⟨u, v⟩ measures how much u points along v: the shadow of u on v times |v|. It is conjugate-symmetric and linear in the first slot."),
21002: dict(d=d21002, stmtKind="THEOREM",
  statement=r"<b>Cauchy–Schwarz inequality (Axler 6.14).</b> Suppose $u,v\in V$. Then $|\langle u,v\rangle|\le\|u\|\,\|v\|$, where $\|v\|=\sqrt{\langle v,v\rangle}$. Equality holds if and only if one of $u,v$ is a scalar multiple of the other. Hence for nonzero real vectors $\cos\theta=\frac{\langle u,v\rangle}{\|u\|\|v\|}\in[-1,1]$ defines an angle.",
  hint="Why can a shadow never be longer than the arrow that casts it?",
  breakdown=[r"<strong>$|\langle u,v\rangle|$</strong> = the shadow of $u$ on $v$ (scaled by $\|v\|$).",
             r"<strong>$\le\|u\|\|v\|$</strong> = a shadow is at most as long as the arrow; equality only when $u$ lies on $v$'s line.",
             r"<strong>$\cos\theta=\frac{\langle u,v\rangle}{\|u\|\|v\|}$</strong> = because the ratio is between $-1$ and $1$, it is a genuine cosine: angles make sense in any inner product space."],
  conn=r"<strong>Holding a pen over the photo.</strong> Tilt a pen above a ruler: its shadow is longest when the pen lies flat along the ruler and shrinks to zero when the pen stands perpendicular.",
  cap="The shadow of u on v is at most ‖u‖, so |⟨u, v⟩| ≤ ‖u‖‖v‖, and cos θ = ⟨u, v⟩/(‖u‖‖v‖) defines the angle θ."),
21003: dict(d=d21003, stmtKind="THEOREM",
  statement=r"<b>Triangle inequality, parallelogram equality, polarization (Axler 6.17, 6.21).</b> For $u,v\in V$: $\|u+v\|\le\|u\|+\|v\|$; $\|u+v\|^2+\|u-v\|^2=2(\|u\|^2+\|v\|^2)$; and in a real inner product space $\langle u,v\rangle=\tfrac14(\|u+v\|^2-\|u-v\|^2)$.",
  hint="What do the two diagonals of a parallelogram know about its sides?",
  breakdown=[r"<strong>$\|u+v\|^2+\|u-v\|^2$</strong> = the two diagonals of the parallelogram built on $u$ and $v$.",
             r"<strong>$=2\|u\|^2+2\|v\|^2$</strong> = the cross terms $\pm2\operatorname{Re}\langle u,v\rangle$ cancel; a norm comes from an inner product exactly when this law holds.",
             r"<strong>$\langle u,v\rangle=\tfrac14(\|u+v\|^2-\|u-v\|^2)$</strong> = polarization: lengths alone recover the inner product."],
  conn=r"<strong>Two diagonals of a photo frame.</strong> Squash a rectangular frame into a parallelogram: one diagonal grows, the other shrinks, but the sum of their squares stays twice the sum of the sides' squares. The difference measures how skewed it is: $\langle u,v\rangle$.",
  cap="Sides u, v and diagonals u + v, u − v: ‖u + v‖² + ‖u − v‖² = 2‖u‖² + 2‖v‖², and ⟨u, v⟩ = ¼(‖u + v‖² − ‖u − v‖²)."),
21004: dict(d=d21004, stmtKind="THEOREM",
  statement=r"<b>Pythagorean theorem (Axler 6.12, 6.13).</b> Vectors $u,v$ are orthogonal if $\langle u,v\rangle=0$. In general $\|u+v\|^2=\|u\|^2+\|v\|^2+2\operatorname{Re}\langle u,v\rangle$; hence if $u\perp v$ then $\|u+v\|^2=\|u\|^2+\|v\|^2$. $0$ is the only vector orthogonal to itself.",
  hint="When does the length of a sum come from the lengths alone?",
  breakdown=[r"<strong>$\langle u,v\rangle=0$</strong> = $u$ casts no shadow on $v$: perpendicular.",
             r"<strong>$2\operatorname{Re}\langle u,v\rangle$</strong> = the cross term in $\|u+v\|^2$; it measures how much the arrows overlap.",
             r"<strong>$\|u\|^2+\|v\|^2$</strong> = with the cross term gone, the sides of a right triangle give the hypotenuse."],
  conn=r"<strong>Right and up.</strong> Drag a photo 3 cm right and 4 cm up: it moves 5 cm, because the two moves cast no shadow on each other.",
  cap="u ⊥ v (⟨u, v⟩ = 0), so the cross term 2Re⟨u, v⟩ vanishes and ‖u + v‖² = ‖u‖² + ‖v‖²."),
21005: dict(d=d21005, stmtKind="THEOREM",
  statement=r"<b>Writing a vector in an orthonormal basis (Axler 6.30).</b> A list $e_1,\dots,e_n$ is orthonormal if $\langle e_i,e_j\rangle=\delta_{ij}$; orthonormal lists are linearly independent (6.26). If $e_1,\dots,e_n$ is an orthonormal basis of $V$, then for every $v\in V$: $v=\sum_j\langle v,e_j\rangle e_j$ and $\|v\|^2=\sum_j|\langle v,e_j\rangle|^2$.",
  hint="With a square grid of unit rulers, how do you read an arrow's address?",
  breakdown=[r"<strong>$\langle e_i,e_j\rangle=\delta_{ij}$</strong> = unit-length rulers at right angles to each other.",
             r"<strong>$v=\sum_j\langle v,e_j\rangle e_j$</strong> = each coordinate is just the shadow of $v$ on one ruler; no equations to solve.",
             r"<strong>$\|v\|^2=\sum_j|\langle v,e_j\rangle|^2$</strong> = Pythagoras with $n$ perpendicular pieces (Parseval)."],
  conn=r"<strong>A square grid on the photo.</strong> With perpendicular unit rulers, an arrow's address is read straight off its shadows. With a slanted grid you would have to solve equations instead.",
  cap="With an orthonormal grid e₁, e₂ the coordinates of v are its shadows ⟨v, e₁⟩, ⟨v, e₂⟩: v = Σ⟨v, eⱼ⟩eⱼ and ‖v‖² = Σ|⟨v, eⱼ⟩|²."),
21006: dict(d=d21006, stmtKind="WORKED EXAMPLE",
  statement=r"<b>Example.</b> $u=(1,2)$, $v=(3,1)$: $\langle u,v\rangle=5$, $\|u\|=\sqrt5$, $\|v\|=\sqrt{10}$. Cauchy–Schwarz: $5\le\sqrt{50}$. So $\cos\theta=5/\sqrt{50}=1/\sqrt2$, $\theta=45^\circ$, and $\operatorname{proj}_vu=\frac{\langle u,v\rangle}{\langle v,v\rangle}v=\tfrac12(3,1)=(1.5,0.5)$.",
  hint="What is the angle between (1, 2) and (3, 1), and where does u's shadow land?",
  breakdown=[r"<strong>$\langle u,v\rangle=5$</strong> = $1\cdot3+2\cdot1$.",
             r"<strong>$\cos\theta=1/\sqrt2$</strong> = divide by the lengths $\sqrt5\cdot\sqrt{10}=\sqrt{50}$: the angle is $45^\circ$.",
             r"<strong>$\operatorname{proj}_vu=(1.5,0.5)$</strong> = the shadow of $u$ on $v$: half of $v$, since $\langle u,v\rangle/\langle v,v\rangle=5/10$."],
  conn=r"<strong>Two drags on the photo.</strong> One drag goes $(1,2)$, another $(3,1)$; they are 45° apart, and the first one's shadow on the second is half of it.",
  cap="u = (1,2), v = (3,1): ⟨u, v⟩ = 5, cos θ = 1/√2 so θ = 45°, and the shadow of u on v is proj = (1.5, 0.5)."),
}

STORY = {
 21001: dict(s="STORY 10 · STEP 1 · MEASURING", b="So far arrows had no length or angle. The <b>inner product</b> adds a ruler: how much one arrow points along another.",
   f=[["20906", "the algebra of edits is done"]], n=[["21002", "lengths and angles"], ["21004", "perpendicular"]]),
 21002: dict(s="STORY 10 · STEP 2 · SHADOWS ARE SHORTER", b="<b>Cauchy–Schwarz</b>: a shadow is never longer than its arrow, so angles make sense.",
   f=[["21001", "inner product"]], n=[["21003", "triangle and parallelogram"], ["21006", "compute an angle"]]),
 21003: dict(s="STORY 10 · STEP 3 · TRIANGLES AND FRAMES", b="The triangle inequality, the parallelogram law, and recovering $\\langle u,v\\rangle$ from lengths.",
   f=[["21002", "Cauchy–Schwarz"]], n=[["21004", "the right-angle case"]]),
 21004: dict(s="STORY 10 · STEP 4 · RIGHT ANGLES", b="When $\\langle u,v\\rangle=0$ the cross term disappears: <b>Pythagoras</b> in any inner product space.",
   f=[["21003", "the general identity"]], n=[["21005", "a grid of right angles"]]),
 21005: dict(s="STORY 10 · STEP 5 · A SQUARE GRID", b="With an <b>orthonormal basis</b>, coordinates are just shadows: no equations to solve.",
   f=[["21004", "orthogonality"], ["20202", "coordinates"]], n=[["21101", "shadows on a line"], ["21102", "build such a grid"]]),
 21006: dict(s="STORY 10 · STEP 6 · WITH NUMBERS", b="Inner product, lengths, angle and a shadow for two concrete arrows.",
   f=[["21002", "angle formula"]], n=[["21101", "projection in general"]]),
}

FIX = {cid: {"stmtKind": v["stmtKind"], "statement": v["statement"], "hint": v["hint"], "breakdown": v["breakdown"],
             "personalConnection": v["conn"], "drawingSvg": v["d"](cid), "drawingCaption": v["cap"],
             "textbookImg": None, "textbookRef": None} for cid, v in CARDS.items()}
