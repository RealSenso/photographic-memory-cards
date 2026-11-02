"""LAA topic 12 (adjoints, self-adjoint and normal operators). Photo picture: the adjoint T*
is the 'measuring partner' of an edit: measuring an edited arrow against w equals measuring
the original arrow against T*w."""
from laa_lib import *

SUBJECT = "LAA"

def d21201(c):
    return svg(c,
        phone(8, 26, 96, 80, "V"), phone(136, 26, 96, 80, "W"),
        pin(30, 90, None), vec((30, 90), (66, 70), "v", 2, 0, "start", 7.5), vec((30, 90), (44, 46), "T*w", 2, -2, "start", 7.5),
        pin(158, 90, None), vec((158, 90), (204, 76), "Tv", 2, 0, "start", 7.5), vec((158, 90), (180, 46), "w", 2, -2, "start", 7.5),
        L(106, 58, 134, 58, 1, ar=True), N(120, 52, "T", 7.5, "middle"), L(134, 76, 106, 76, 1, ar=True), N(120, 88, "T*", 7.5, "middle"),
        N(120, 12, "⟨Tv, w⟩ = ⟨v, T*w⟩", 9, "middle"),
        N(120, 124, "(ST)* = T*S*,  (λT)* = λ̄T*", 7.5, "middle"), N(120, 136, "matrix: conjugate transpose", 7, "middle"))

def d21202(c):
    return svg(c,
        phone(8, 22, 100, 96, "V"), phone(132, 22, 100, 96, "W"),
        L(18, 106, 98, 36, 1), N(96, 48, "null T", 7, "end"), L(26, 40, 96, 104, .9, "3 2"), N(30, 52, "range T*", 7, "start"),
        L(142, 100, 222, 44, 1), N(222, 56, "range T", 7, "end"), L(150, 44, 220, 102, .9, "3 2"), N(154, 56, "null T*", 7, "start"),
        N(120, 12, "null T* = (range T)⊥,  range T* = (null T)⊥", 7.5, "middle"),
        N(120, 136, "rank T* = rank T", 7.5, "middle"))

def d21203(c):
    O = (110, 72)
    return svg(c,
        E(110, 72, 64, 28, -25, "#f1f5f9", 1), pin(*O, None),
        vec(O, (166, 46), "v₁: ×λ₁", 4, -2, "start", 7.5), vec(O, (98, 46), "v₂: ×λ₂", -4, -2, "end", 7.5),
        N(120, 12, "T = T*: a pure stretch along perpendicular axes", 7.5, "middle"),
        N(12, 120, "λ real:  λ‖v‖² = ⟨Tv, v⟩ = ⟨v, Tv⟩ = λ̄‖v‖²", 7.2, "start"),
        N(12, 132, "λ₁ ≠ λ₂ ⇒ v₁ ⊥ v₂;   ⟨Tv, v⟩ ∈ ℝ", 7.2, "start"),
        N(236, 30, "circle → ellipse", 7, "end"))

def d21204(c):
    O = (60, 90)
    return svg(c,
        N(120, 12, "TT* = T*T: the edit and its partner commute", 7.5, "middle"),
        pin(*O, None), vec(O, (100, 64), "Tv", 2, -2, "start", 7.5), vec(O, (100, 116), "T*v", 2, 8, "start", 7.5),
        N(60, 134, "‖Tv‖ = ‖T*v‖", 7.5, "middle"),
        N(236, 50, "Tv = λv ⇔ T*v = λ̄v", 7.5, "end"), N(236, 64, "distinct λ ⇒ ⊥ eigenvectors", 7, "end"),
        N(236, 96, "e.g. rotation (T* = T⁻¹):", 7, "end"), N(236, 108, "turns v one way, T* the other,", 7, "end"), N(236, 120, "same length", 7, "end"))

def d21205(c):
    cx, cy, r = 150, 78, 44
    return svg(c,
        L(90, cy, 214, cy, .8, ar=True), N(214, cy + 12, "Re", 7, "end"), L(cx, 136, cx, 18, .8, ar=True), N(cx + 4, 24, "Im", 7, "start"),
        circ(cx, cy, r, "none", 1, "3 2"),
        L(102, cy, 200, cy, 2), N(108, cy - 6, "T = T*: λ ∈ ℝ", 7, "start"),
        dot(cx + r * .6, cy - r * .8, None, r=2.2), N(cx + r * .6 + 4, cy - r * .8 - 4, "T*T = I: |λ| = 1", 7, "start"),
        L(cx, 30, cx, 126, 2), N(cx - 4, 132, "T* = −T: λ ∈ iℝ", 7, "end"),
        N(12, 20, "all three are normal", 7.5, "start"), N(12, 32, "⇒ orthonormal eigenbasis", 7.5, "start"),
        N(12, 60, "they differ only in", 7, "start"), N(12, 70, "where λ lives", 7, "start"))

def d21206(c):
    return svg(c,
        N(120, 12, "A = [1 i; −i 1]", 8.5, "middle"),
        N(14, 34, "A* = conj(A)ᵀ = A: self-adjoint", 7.5, "start"),
        N(14, 50, "tr A = 2, det A = 1 − 1 = 0", 7.5, "start"), N(14, 64, "λ² − 2λ = 0 ⇒ λ = 0, 2 (real)", 7.5, "start"),
        R(14, 80, 212, 22, "#f1f5f9", 1, 3), N(120, 95, "⟨(1, −i), (1, i)⟩ = 1 + (−i)·conj(i) = 1 + (−i)(−i) = 0", 7, "middle"),
        N(14, 120, "eigenvectors: (1, i) for 2 and (1, −i) for 0", 7.5, "start"),
        N(14, 134, "orthogonal, as the theorem promises", 7.5, "start"))

CARDS = {
21201: dict(d=d21201, stmtKind="DEFINITION",
  statement=r"<b>Adjoint (Axler 7.2, 7.5, 7.9).</b> For $T\in\mathcal L(V,W)$ between finite-dimensional inner product spaces, the adjoint $T^*\in\mathcal L(W,V)$ is the unique function with $\langle Tv,w\rangle=\langle v,T^*w\rangle$ for all $v\in V$, $w\in W$. Then $(S+T)^*=S^*+T^*$, $(\lambda T)^*=\bar\lambda T^*$, $(ST)^*=T^*S^*$, and in orthonormal bases $\mathcal M(T^*)$ is the conjugate transpose of $\mathcal M(T)$.",
  hint="Measuring an edited arrow against w gives the same number as measuring the original against what?",
  breakdown=[r"<strong>$\langle Tv,w\rangle=\langle v,T^*w\rangle$</strong> = edit first and measure, or measure against the partner-edited $w$: the same number.",
             r"<strong>$(ST)^*=T^*S^*$</strong> = partners of two edits come in reverse order.",
             r"<strong>$(\lambda T)^*=\bar\lambda T^*$</strong> = a complex factor gets conjugated; in an orthonormal grid the matrix is the conjugate transpose."],
  conn=r"<strong>The measuring partner.</strong> Instead of editing the photo and then measuring with a ruler $w$, you can leave the photo alone and edit the ruler with $T^*$. For a rotation, the partner is the opposite rotation.",
  cap="T sends v to Tv in W; T* sends w back to T*w in V, so that ⟨Tv, w⟩ = ⟨v, T*w⟩."),
21202: dict(d=d21202, stmtKind="THEOREM",
  statement=r"<b>Null space and range of $T^*$ (Axler 7.6).</b> For $T\in\mathcal L(V,W)$: $\operatorname{null}T^*=(\operatorname{range}T)^\perp$, $\operatorname{range}T^*=(\operatorname{null}T)^\perp$, $\operatorname{null}T=(\operatorname{range}T^*)^\perp$, $\operatorname{range}T=(\operatorname{null}T^*)^\perp$. In particular $\operatorname{rank}T^*=\operatorname{rank}T$.",
  hint="Which arrows does the partner T* squash, and how do they sit relative to T's outputs?",
  breakdown=[r"<strong>$\operatorname{null}T^*=(\operatorname{range}T)^\perp$</strong> = $T^*w=0\iff\langle Tv,w\rangle=0$ for all $v$: $w$ is perpendicular to every output of $T$.",
             r"<strong>$\operatorname{range}T^*=(\operatorname{null}T)^\perp$</strong> = the row space is perpendicular to the null space.",
             r"<strong>$\operatorname{rank}T^*=\operatorname{rank}T$</strong> = row rank equals column rank."],
  conn=r"<strong>Four lines in two photos.</strong> In the input photo, what $T$ squashes is perpendicular to what $T^*$ produces; in the output photo, what $T^*$ squashes is perpendicular to what $T$ produces.",
  cap="In V, null T ⊥ range T*; in W, range T ⊥ null T*. So null T* = (range T)⊥ and range T* = (null T)⊥, and rank T* = rank T."),
21203: dict(d=d21203, stmtKind="THEOREM",
  statement=r"<b>Self-adjoint operators (Axler 7.11, 7.13, 7.14).</b> $T\in\mathcal L(V)$ is self-adjoint if $T=T^*$. Every eigenvalue of a self-adjoint operator is real, and eigenvectors for distinct eigenvalues are orthogonal. Over $\mathbb C$, $T$ is self-adjoint iff $\langle Tv,v\rangle\in\mathbb R$ for every $v$.",
  hint="What kind of edit is its own measuring partner?",
  breakdown=[r"<strong>$T=T^*$</strong> = the edit is its own partner: a symmetric (Hermitian) matrix.",
             r"<strong>$\lambda\in\mathbb R$</strong> = $\lambda\|v\|^2=\langle Tv,v\rangle=\langle v,Tv\rangle=\bar\lambda\|v\|^2$: no complex stretch factors.",
             r"<strong>$\lambda_1\ne\lambda_2\Rightarrow v_1\perp v_2$</strong> = the stretch axes are perpendicular, so a circle becomes an ellipse with perpendicular axes."],
  conn=r"<strong>A pure stretch.</strong> A self-adjoint edit stretches the photo along two perpendicular axes, by real factors, with no rotation. A round sticker becomes an ellipse.",
  cap="A self-adjoint edit stretches along perpendicular axes v₁ ⊥ v₂ by real factors λ₁, λ₂: a circle becomes an ellipse."),
21204: dict(d=d21204, stmtKind="PROPOSITION",
  statement=r"<b>Normal operators (Axler 7.18, 7.20, 7.21, 7.22).</b> $T\in\mathcal L(V)$ is normal if $TT^*=T^*T$. $T$ is normal iff $\|Tv\|=\|T^*v\|$ for all $v$. If $T$ is normal then $Tv=\lambda v\iff T^*v=\bar\lambda v$, and eigenvectors for distinct eigenvalues are orthogonal.",
  hint="When does an edit commute with its measuring partner?",
  breakdown=[r"<strong>$TT^*=T^*T$</strong> = applying the edit and its partner in either order gives the same result.",
             r"<strong>$\|Tv\|=\|T^*v\|$</strong> = the edit and its partner change every arrow's length the same way, since $\|Tv\|^2-\|T^*v\|^2=\langle(T^*T-TT^*)v,v\rangle$.",
             r"<strong>$T^*v=\bar\lambda v$</strong> = the partner has the same eigen-arrows with conjugated factors."],
  conn=r"<strong>Rotation and its partner.</strong> A rotation's partner is the opposite rotation; they commute and change no lengths. A shear's partner leans the other way, and they do not commute.",
  cap="For a normal T, Tv and T*v always have the same length: ‖Tv‖ = ‖T*v‖, and Tv = λv ⇔ T*v = λ̄v."),
21205: dict(d=d21205, stmtKind="PROPOSITION",
  statement=r"<b>Special normal operators.</b> Self-adjoint ($T^*=T$), skew-adjoint ($T^*=-T$) and unitary ($T^*T=I$) operators are normal. Their eigenvalues lie respectively on $\mathbb R$, on $i\mathbb R$, and on the unit circle $|\lambda|=1$.",
  hint="Where in the complex plane do the stretch factors of these three kinds of edit live?",
  breakdown=[r"<strong>$T=T^*\Rightarrow\lambda\in\mathbb R$</strong> = pure stretches: factors on the real line.",
             r"<strong>$T^*T=I\Rightarrow|\lambda|=1$</strong> = length-preserving edits (rotations, reflections): factors on the unit circle.",
             r"<strong>$T^*=-T\Rightarrow\lambda\in i\mathbb R$</strong> = infinitesimal spins: purely imaginary factors."],
  conn=r"<strong>Stretch, rotate, spin.</strong> The three tools in a basic editor are all normal: a stretch has real factors, a rotation keeps lengths (unit factors), and the spin rate of a rotation is imaginary.",
  cap="Self-adjoint: λ on the real axis. Unitary: |λ| = 1 on the circle. Skew-adjoint: λ on the imaginary axis. All are normal."),
21206: dict(d=d21206, stmtKind="WORKED EXAMPLE",
  statement=r"<b>Example.</b> $A=\begin{pmatrix}1&i\\-i&1\end{pmatrix}$: $A^*=\bar A^\top=A$, so $A$ is self-adjoint. $\operatorname{tr}A=2$, $\det A=0$, so $\lambda\in\{0,2\}$ (real). Eigenvectors $(1,i)$ for $2$ and $(1,-i)$ for $0$ are orthogonal: $\langle(1,-i),(1,i)\rangle=1\cdot\bar1+(-i)\bar i=1+(-i)(-i)=0$.",
  hint="Check that this complex matrix is its own partner, then find its stretch factors.",
  breakdown=[r"<strong>$A^*=A$</strong> = conjugate and transpose: you get $A$ back.",
             r"<strong>$\lambda\in\{0,2\}$</strong> = trace 2, determinant 0: real, as promised.",
             r"<strong>$\langle(1,-i),(1,i)\rangle=0$</strong> = with complex numbers remember to conjugate the second slot."],
  conn=r"<strong>A pure stretch in disguise.</strong> Even with $i$ in it, this edit is a stretch along two perpendicular (complex) axes: one by 2, one flattened to 0.",
  cap="A = [1 i; −i 1] equals its conjugate transpose, has real eigenvalues 0 and 2, and orthogonal eigenvectors (1, i), (1, −i)."),
}

STORY = {
 21201: dict(s="STORY 12 · STEP 1 · THE PARTNER", b="Every edit has a <b>measuring partner</b> $T^*$: measuring after the edit equals measuring against the partner-edited ruler.",
   f=[["21001", "inner products"], ["20305", "matrices"]], n=[["21202", "its null space and range"], ["21203", "edits that are their own partner"]]),
 21202: dict(s="STORY 12 · STEP 2 · FOUR SUBSPACES", b="The partner's null space and range are the <b>perpendiculars</b> of the edit's range and null space.",
   f=[["21201", "adjoint"], ["21103", "orthogonal complements"]], n=[["21602", "normal equations"]]),
 21203: dict(s="STORY 12 · STEP 3 · PURE STRETCH", b="A <b>self-adjoint</b> edit has real stretch factors along perpendicular axes.",
   f=[["21201", "adjoint"], ["20106", "symmetric matrices"]], n=[["21302", "real spectral theorem"], ["21401", "positive edits"]]),
 21204: dict(s="STORY 12 · STEP 4 · COMMUTES WITH ITS PARTNER", b="A <b>normal</b> edit commutes with its partner; its eigen-arrows are perpendicular.",
   f=[["21201", "adjoint"], ["20702", "commuting edits"]], n=[["21205", "the zoo"], ["21301", "complex spectral theorem"]]),
 21205: dict(s="STORY 12 · STEP 5 · THE ZOO", b="Self-adjoint, unitary and skew edits are all normal; they differ in <b>where the eigenvalues live</b>.",
   f=[["21204", "normal"]], n=[["21206", "an example"], ["21403", "isometries"]]),
 21206: dict(s="STORY 12 · STEP 6 · WITH NUMBERS", b="A complex self-adjoint matrix with real eigenvalues and orthogonal eigenvectors.",
   f=[["21203", "self-adjoint"]], n=[["21301", "the spectral theorem"]]),
}

FIX = {cid: {"stmtKind": v["stmtKind"], "statement": v["statement"], "hint": v["hint"], "breakdown": v["breakdown"],
             "personalConnection": v["conn"], "drawingSvg": v["d"](cid), "drawingCaption": v["cap"],
             "textbookImg": None, "textbookRef": None} for cid, v in CARDS.items()}
