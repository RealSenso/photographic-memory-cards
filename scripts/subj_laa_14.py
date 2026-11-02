"""LAA topic 14 (positive operators, square roots, isometries). Photo picture: a positive edit
stretches along perpendicular axes without flipping; an isometry is the rotate/flip tool."""
from laa_lib import *
import math

SUBJECT = "LAA"

def d21401(c):
    O = (70, 84)
    return svg(c,
        circ(*O, 28, "none", .9, "3 2"), E(*O, 50, 22, -20, "#f1f5f9", 1), pin(*O, None),
        vec(O, (110, 66), "v", 2, -4, "start", 7.5), vec(O, (128, 66), None, d="3 2"), N(132, 72, "Tv", 7.5, "start"),
        N(120, 12, "T ⪰ 0: stretch along ⊥ axes by factors ≥ 0, no flip", 7.5, "middle"),
        N(236, 104, "⟨Tv, v⟩ ≥ 0: Tv never points", 7, "end"), N(236, 114, "away from v", 7, "end"),
        N(12, 128, "T = T*, spec ⊆ [0, ∞) ⇔ T = S*S", 7.5, "start"), N(12, 140, "⟨S*Sv, v⟩ = ‖Sv‖² ≥ 0", 7.5, "start"))

def d21402(c):
    return svg(c,
        N(120, 12, "√T: the unique positive R with R² = T", 8, "middle"),
        R(14, 30, 64, 40, "#f1f5f9", 1, 3), N(46, 48, "T", 9, "middle"), N(46, 62, "×4, ×9", 7.5, "middle"),
        N(90, 52, "=", 10, "middle"),
        R(100, 30, 56, 40, "#ffffff", 1, 3), N(128, 48, "√T", 9, "middle"), N(128, 62, "×2, ×3", 7.5, "middle"),
        N(164, 52, "·", 12, "middle"),
        R(172, 30, 56, 40, "#ffffff", 1, 3), N(200, 48, "√T", 9, "middle"), N(200, 62, "×2, ×3", 7.5, "middle"),
        N(120, 94, "√T = Σ √λⱼ Pⱼ", 8, "middle"),
        N(120, 110, "−√T also squares to T, but is not positive", 7, "middle"),
        N(120, 130, "|T| = √(T*T): the stretch part of any edit", 7.5, "middle"))

def d21403(c):
    O = (64, 96)
    return svg(c,
        circ(*O, 40, "none", .9, "3 2"), pin(*O, None),
        vec(O, (104, 96), "u", 0, 10, "middle", 7.5), vec(O, (84, 62), "v", -4, -2, "end", 7.5),
        vec(O, (92, 124), "Su", 4, 4, "start", 7.5), vec(O, (102, 82), "Sv", 4, 0, "start", 7.5),
        N(120, 12, "S*S = I: the rotate / flip tool keeps lengths and angles", 7.5, "middle"),
        N(236, 50, "‖Sv‖ = ‖v‖", 8, "end"), N(236, 64, "⟨Su, Sv⟩ = ⟨u, v⟩", 8, "end"),
        N(236, 110, "columns orthonormal;", 7, "end"), N(236, 120, "eigenvalues |λ| = 1", 7, "end"))

def d21404(c):
    return svg(c,
        N(64, 14, "rotation: det Q = +1", 7.5, "middle"), N(180, 14, "reflection: det Q = −1", 7.5, "middle"),
        L(120, 22, 120, 140, .6, "3 2"),
        R(40, 50, 34, 34, "#f1f5f9", 1, 0), N(57, 72, "F", 10, "middle"),
        P("M 84 62 A 22 22 0 0 1 84 92", "none", .9, ar=True),
        PG(" ".join(f"{113 + 17 * (x * math.cos(.6) - y * math.sin(.6)):.1f},{77 + 17 * (x * math.sin(.6) + y * math.cos(.6)):.1f}" for x, y in [(-1, -1), (1, -1), (1, 1), (-1, 1)]), "#f1f5f9", 1),
        '<text x="113" y="81" font-size="10" font-family="sans-serif" text-anchor="middle" transform="rotate(34 113 77)">F</text>',
        N(64, 116, "UU* = U*U = I", 7.5, "middle"),
        R(150, 50, 34, 34, "#f1f5f9", 1, 0), N(167, 72, "F", 10, "middle"), L(196, 44, 196, 92, .9, "2 2"),
        R(208, 50, 24, 34, "#f1f5f9", 1, 0), '<text x="-220" y="72" font-size="10" font-family="sans-serif" text-anchor="middle" transform="scale(-1 1)">F</text>',
        N(180, 116, "|λ| = 1, |det U| = 1", 7.5, "middle"),
        N(120, 136, "κ₂(U) = 1: numerically perfect", 7.5, "middle"))

def d21405(c):
    O = (80, 92)
    s = 16
    P2 = lambda x, y: (O[0] + s * x, O[1] - s * y)
    return svg(c,
        L(14, 92, 160, 92, .6), L(80, 140, 80, 8, .6), pin(*O, None),
        vec(O, P2(.71, -.71), "(1,−1)/√2", 4, 8, "start", 7), vec(O, P2(2.12, -2.12), "×3", 4, 6, "start", 7.5),
        vec(O, P2(.71, .71), "(1,1)/√2: ×1", -2, -4, "end", 7),
        N(236, 20, "A = [2 −1; −1 2]", 8, "end"), N(236, 32, "λ = 3, 1 > 0 ⇒ A ≻ 0", 7.5, "end"),
        N(236, 50, "⟨Av, v⟩ = x² + y² + (x − y)²", 7, "end"),
        N(236, 112, "√A = √3 P(1,−1) + 1·P(1,1)", 7.2, "end"), N(236, 126, "(√A)² = A", 7.5, "end"))

CARDS = {
21401: dict(d=d21401, stmtKind="THEOREM",
  statement=r"<b>Characterizations of positive operators (Axler 7.35, 7.38).</b> $T\in\mathcal L(V)$ is positive if $T$ is self-adjoint and $\langle Tv,v\rangle\ge0$ for all $v$. The following are equivalent: $T$ is positive; $T$ is self-adjoint with all eigenvalues nonnegative; $T$ has a positive square root; $T=R^2$ for some self-adjoint $R$; $T=S^*S$ for some $S\in\mathcal L(V)$.",
  hint="Which stretch edits never point an arrow away from where it started?",
  breakdown=[r"<strong>$T=T^*$, $\operatorname{spec}(T)\subseteq[0,\infty)$</strong> = a pure stretch along perpendicular axes with nonnegative factors: nothing is flipped.",
             r"<strong>$T=S^*S$</strong> = every 'edit followed by its partner' is positive.",
             r"<strong>$\langle S^*Sv,v\rangle=\|Sv\|^2\ge0$</strong> = the reason: the measurement is a squared length."],
  conn=r"<strong>Stretch but never flip.</strong> A positive edit can pull the photo wider or squash it, but never mirrors it: every arrow still points into its own half-plane after the edit.",
  cap="A positive T stretches along perpendicular axes by factors ≥ 0, so ⟨Tv, v⟩ ≥ 0; every S*S is positive since ⟨S*Sv, v⟩ = ‖Sv‖²."),
21402: dict(d=d21402, stmtKind="THEOREM",
  statement=r"<b>Each positive operator has a unique positive square root (Axler 7.39).</b> If $T\in\mathcal L(V)$ is positive, there is exactly one positive $R$ with $R^2=T$, written $\sqrt T$. If $T=\sum_j\lambda_jP_j$ then $\sqrt T=\sum_j\sqrt{\lambda_j}P_j$. For any $T$, $|T|=\sqrt{T^*T}$ is positive.",
  hint="What edit, done twice, gives 'stretch ×4 and ×9'?",
  breakdown=[r"<strong>$\sqrt T=\sum\sqrt{\lambda_j}P_j$</strong> = keep the axes, take the square root of each stretch factor.",
             r"<strong>unique positive</strong> = other square roots exist ($-\sqrt T$, or flips on some axes), but only one has all factors $\ge0$.",
             r"<strong>$|T|=\sqrt{T^*T}$</strong> = the pure-stretch part of any edit; it reappears in the polar decomposition."],
  conn=r"<strong>Half of a stretch.</strong> If an edit stretches by 4 one way and 9 the other, doing 'stretch by 2 and 3' twice gives the same result. That half-edit is its positive square root.",
  cap="T stretches by 4 and 9; √T stretches by 2 and 3 along the same axes, and √T·√T = T."),
21403: dict(d=d21403, stmtKind="THEOREM",
  statement=r"<b>Characterizations of isometries (Axler 7.42, 7.43).</b> $S\in\mathcal L(V,W)$ is an isometry if $\|Sv\|=\|v\|$ for all $v$. Equivalently: $S^*S=I$; $\langle Su,Sv\rangle=\langle u,v\rangle$ for all $u,v$; $S$ maps every orthonormal list to an orthonormal list. An isometry is injective, and its eigenvalues have $|\lambda|=1$.",
  hint="Which edits keep every arrow's length the same?",
  breakdown=[r"<strong>$\|Sv\|=\|v\|$</strong> = no arrow gets longer or shorter.",
             r"<strong>$S^*S=I$</strong> = the partner undoes the edit; the columns are orthonormal.",
             r"<strong>$\langle Su,Sv\rangle=\langle u,v\rangle$</strong> = by polarization, keeping lengths also keeps angles."],
  conn=r"<strong>The rotate tool.</strong> Rotating or flipping a photo changes where things point, but every distance and every angle stays the same. Those are the isometries.",
  cap="An isometry rotates u, v to Su, Sv on the same circle: ‖Sv‖ = ‖v‖ and ⟨Su, Sv⟩ = ⟨u, v⟩, equivalently S*S = I."),
21404: dict(d=d21404, stmtKind="DEFINITION",
  statement=r"<b>Unitary and orthogonal matrices.</b> $U\in\mathbb C^{n\times n}$ is unitary if $U^*U=UU^*=I$; $Q\in\mathbb R^{n\times n}$ is orthogonal if $Q^\top Q=QQ^\top=I$. Rows and columns are orthonormal bases, $|\lambda|=1$ for every eigenvalue, $|\det U|=1$ ($\det Q=\pm1$), $\|U\|_2=1$ and $\kappa_2(U)=1$.",
  hint="What separates a rotation from a reflection, if both keep lengths?",
  breakdown=[r"<strong>$U^*U=UU^*=I$</strong> = square isometries: invertible, with the partner as the inverse.",
             r"<strong>$|\lambda|=1$</strong> = stretch factors on the unit circle: nothing grows or shrinks.",
             r"<strong>$\det Q=\pm1$</strong> = $+1$ for rotations, $-1$ for reflections (a flip mirrors the photo). Condition number 1: no rounding error is amplified."],
  conn=r"<strong>Rotate versus flip.</strong> Both keep the photo's size; rotating keeps its handedness (det +1), flipping mirrors the letters (det −1).",
  cap="Left: a rotation (det Q = +1). Right: a reflection mirrors F (det Q = −1). Both satisfy UU* = I, |λ| = 1, |det U| = 1."),
21405: dict(d=d21405, stmtKind="WORKED EXAMPLE",
  statement=r"<b>Example.</b> $A=\begin{pmatrix}2&-1\\-1&2\end{pmatrix}$: $\lambda=3$ on $(1,-1)/\sqrt2$, $\lambda=1$ on $(1,1)/\sqrt2$, both $\gt0$, so $A$ is positive definite; also $\langle Av,v\rangle=x^2+y^2+(x-y)^2\gt0$. Then $\sqrt A=\sqrt3P_{(1,-1)}+P_{(1,1)}$ and $(\sqrt A)^2=A$.",
  hint="Is this edit positive, and what is its square root?",
  breakdown=[r"<strong>$\lambda=3,1\gt0$</strong> = trace 4, determinant 3: both factors positive.",
             r"<strong>$\langle Av,v\rangle=x^2+y^2+(x-y)^2$</strong> = a direct check: a sum of squares, zero only at $v=0$.",
             r"<strong>$\sqrt A=\sqrt3P_{(1,-1)}+P_{(1,1)}$</strong> = square-root each factor on its own axis."],
  conn=r"<strong>Stretch across the diagonal.</strong> This edit triples arrows along $(1,-1)$ and leaves $(1,1)$ alone; its square root stretches by $\sqrt3$ instead.",
  cap="A stretches (1,−1)/√2 by 3 and keeps (1,1)/√2: positive definite, with √A = √3P(1,−1) + P(1,1)."),
}

STORY = {
 21401: dict(s="STORY 14 · STEP 1 · STRETCH, NO FLIP", b="Among self-adjoint edits, the <b>positive</b> ones never flip: all stretch factors $\\ge0$, and every $S^*S$ is one.",
   f=[["21302", "spectral theorem"]], n=[["21402", "square roots"], ["21501", "polar decomposition"]]),
 21402: dict(s="STORY 14 · STEP 2 · HALF A STRETCH", b="A positive edit has a unique <b>positive square root</b>; $|T|=\\sqrt{T^*T}$ is the stretch part of any edit.",
   f=[["21401", "positive"], ["21304", "f(T)"]], n=[["21501", "T = S|T|"]]),
 21403: dict(s="STORY 14 · STEP 3 · THE ROTATE TOOL", b="<b>Isometries</b> keep lengths and angles: $S^*S=I$.",
   f=[["21205", "unitary operators"]], n=[["21404", "unitary matrices"], ["21501", "the rotation part"]]),
 21404: dict(s="STORY 14 · STEP 4 · ROTATE OR FLIP", b="Unitary and orthogonal matrices: $|\\lambda|=1$, $\\det=\\pm1$, perfectly conditioned.",
   f=[["21403", "isometries"]], n=[["21405", "a positive example"], ["21701", "det as volume"]]),
 21405: dict(s="STORY 14 · STEP 5 · WITH NUMBERS", b="Check positive definiteness two ways and take the square root.",
   f=[["21401", "positive"], ["21402", "square root"]], n=[["21501", "next: every edit = rotate × stretch"]]),
}

FIX = {cid: {"stmtKind": v["stmtKind"], "statement": v["statement"], "hint": v["hint"], "breakdown": v["breakdown"],
             "personalConnection": v["conn"], "drawingSvg": v["d"](cid), "drawingCaption": v["cap"],
             "textbookImg": None, "textbookRef": None} for cid, v in CARDS.items()}
