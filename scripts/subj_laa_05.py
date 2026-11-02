"""LAA topic 05 (polynomials of an operator, minimal polynomial). Photo picture: Tᵏ is the
edit repeated k times; p(T) mixes repeated edits like a recipe."""
from laa_lib import *

SUBJECT = "LAA"

def chain(xs, y, labs, last=None):
    out = []
    for i, (x, lab) in enumerate(zip(xs, labs)):
        out += [R(x, y, 40, 22, "#ffffff" if i != last else "#d9dee7", 1, 3), N(x + 20, y + 14, lab, 7.5, "middle")]
        if i: out.append(L(xs[i - 1] + 41, y + 11, x - 1, y + 11, 1, ar=True))
    return "".join(out)

def d20501(c):
    O = (30, 112)
    return svg(c,
        N(120, 12, "p(T) = a₀I + a₁T + … + aₘTᵐ: a recipe of repeated edits", 7.5, "middle"),
        chain([12, 70, 128, 186], 24, ["v", "Tv", "T²v", "T³v"]),
        N(120, 62, "T k times = Tᵏ;  (pq)(T) = p(T)q(T) = q(T)p(T)", 7.5, "middle"),
        pin(*O, None), vec(O, (60, 112), "v", 0, 10, "middle"), vec(O, (90, 112), None, d="3 2"), vec(O, (140, 112), "p(T)v = p(λ)v", 0, 10, "middle"),
        N(236, 88, "if Tv = λv, every edit just", 7, "end"), N(236, 98, "rescales v: Tᵏv = λᵏv", 7, "end"))

def d20502(c):
    return svg(c,
        N(120, 12, "n + 1 arrows in an n-dim space must be dependent", 7.5, "middle"),
        chain([8, 66, 124, 182], 24, ["v", "Tv", "…", "Tⁿv"]),
        N(120, 66, "a₀v + a₁Tv + … + aₙTⁿv = 0 ⇒ p(T)v = 0", 7.5, "middle"),
        N(120, 82, "factor over ℂ: p(z) = c(z − λ₁)⋯(z − λₘ)", 7.5, "middle"),
        R(30, 94, 180, 22, "#f1f5f9", 1, 3), N(120, 108, "(T − λ₁I)⋯(T − λₘI) v = 0, v ≠ 0", 7.5, "middle"),
        N(120, 132, "⇒ some T − λⱼI squashes a nonzero arrow: λⱼ is an eigenvalue", 7, "middle"))

def d20503(c):
    return svg(c,
        N(120, 12, "the shortest recipe that wipes every arrow to the pin", 7.5, "middle"),
        R(16, 28, 208, 26, "#d9dee7", 1, 3), N(120, 45, "q(T) = 0,  q monic, lowest degree", 8, "middle"),
        R(16, 66, 208, 26, "#ffffff", 1, 3), N(120, 83, "any other p with p(T) = 0:  p = s·q + r", 7.5, "middle"),
        N(120, 108, "r(T) = 0 with deg r < deg q ⇒ r = 0", 7.5, "middle"),
        N(120, 122, "so p(T) = 0 ⇔ q divides p", 8, "middle"),
        N(120, 138, "deg q ≤ dim V", 7.5, "middle"))

def d20504(c):
    return svg(c,
        E(120, 76, 108, 54, 0, "#ffffff", 1), N(120, 34, "pᴛ: characteristic polynomial", 7.5, "middle"),
        E(120, 84, 64, 34, 0, "#f1f5f9", 1), N(120, 66, "q: minimal polynomial", 7.5, "middle"),
        N(120, 84, "roots of q", 7.5, "middle"), N(120, 96, "= eigenvalues of T", 7.5, "middle"),
        N(120, 12, "Cayley–Hamilton: pᴛ(T) = 0, so q | pᴛ", 8, "middle"),
        N(120, 140, "same roots; q has the smaller exponents", 7.5, "middle"))

def d20505(c):
    return svg(c,
        N(64, 14, "q = (z − 2)(z − 3): distinct", 7.5, "middle"), N(178, 14, "q = (z − 2)²: repeated", 7.5, "middle"),
        L(120, 22, 120, 140, .6, "3 2"),
        pin(60, 96, None), vec((60, 96), (100, 96), "e₁ ↦ 2e₁", 0, 10, "middle", 7), vec((60, 96), (60, 40), "e₂ ↦ 3e₂", 4, 4, "start", 7),
        N(64, 126, "eigen-arrows fill the photo", 7, "middle"), N(64, 136, "⇒ diagonalizable ✓", 7, "middle"),
        pin(160, 96, None), vec((160, 96), (196, 96), "e₁", 0, 10, "middle", 7), vec((160, 96), (186, 50), "e₂ ↦ 2e₂ + e₁", -6, -4, "start", 7),
        N(178, 126, "e₂ needs (T − 2I)² to vanish", 7, "middle"), N(178, 136, "⇒ not diagonalizable ✗", 7, "middle"))

def d20506(c):
    return svg(c,
        N(120, 12, "same char. poly (z − 2)², different minimal polynomials", 7.5, "middle"),
        R(14, 26, 98, 46, "#ffffff", 1, 3), N(63, 42, "A = [2 1; 0 2]", 8, "middle"), N(63, 58, "a shear + zoom ×2", 7, "middle"),
        R(128, 26, 98, 46, "#ffffff", 1, 3), N(177, 42, "2I", 8, "middle"), N(177, 58, "a pure zoom ×2", 7, "middle"),
        N(63, 88, "A − 2I = [0 1; 0 0] ≠ 0", 7.5, "middle"), N(63, 100, "(A − 2I)² = 0", 7.5, "middle"),
        N(63, 116, "q = (z − 2)²", 8, "middle"), N(63, 130, "not diagonalizable", 7, "middle"),
        N(177, 88, "2I − 2I = 0 already", 7.5, "middle"), N(177, 116, "q = z − 2", 8, "middle"), N(177, 130, "diagonal", 7, "middle"))

CARDS = {
20501: dict(d=d20501, stmtKind="DEFINITION",
  statement=r"<b>Polynomial applied to an operator (Axler 5.16, 5.20).</b> For $T\in\mathcal L(V)$ and $p(z)=a_0+a_1z+\dots+a_mz^m$, define $p(T)=a_0I+a_1T+\dots+a_mT^m$. Then $(pq)(T)=p(T)q(T)=q(T)p(T)$. If $Tv=\lambda v$ then $p(T)v=p(\lambda)v$.",
  hint="What does it mean to plug a photo edit into a polynomial?",
  breakdown=[r"<strong>$p(T)=\sum a_kT^k$</strong> = a recipe: do the edit $k$ times ($T^k$), weight by $a_k$, and add. The constant $a_0$ becomes $a_0I$.",
             r"<strong>$(pq)(T)=p(T)q(T)$</strong> = recipes built from the same edit multiply like numbers and commute.",
             r"<strong>$Tv=\lambda v\Rightarrow p(T)v=p(\lambda)v$</strong> = on an arrow the edit only stretches, the whole recipe just stretches it by $p(\lambda)$."],
  conn=r"<strong>Running the same filter again.</strong> Apply a zoom twice and you zoom by the square. Any mix of repeated zooms acts on an arrow by the same mix of numbers, so a polynomial of the edit behaves like a polynomial of its stretch factor.",
  cap="Repeating the edit gives v, Tv, T²v, …; p(T) mixes them. On an eigen-arrow (Tv = λv) the recipe just rescales: p(T)v = p(λ)v."),
20502: dict(d=d20502, stmtKind="THEOREM",
  statement=r"<b>Existence of eigenvalues (Axler 5.19).</b> Every operator on a finite-dimensional, nonzero, complex vector space has an eigenvalue.",
  hint="Why must some arrow be only stretched by any edit of a complex photo space?",
  breakdown=[r"<strong>$v,Tv,\dots,T^nv$</strong> = $n+1$ arrows in an $n$-dimensional space, so some nonzero recipe $p$ gives $p(T)v=0$.",
             r"<strong>$p(z)=c\prod(z-\lambda_j)$</strong> = over $\mathbb C$ every polynomial factors into linear pieces.",
             r"<strong>$T-\lambda_jI$ not injective</strong> = the product of the pieces squashes $v\ne0$, so at least one piece squashes some nonzero arrow: $\lambda_j$ is an eigenvalue."],
  conn=r"<strong>Too many repeats.</strong> Keep applying the same edit to one arrow; eventually the results are tangled, and untangling the recipe shows some direction the edit only stretches. Over the reals this can fail: a 90° rotation stretches no arrow.",
  cap="The n + 1 arrows v, …, Tⁿv are dependent, so p(T)v = 0; factoring p over ℂ shows some T − λⱼI squashes a nonzero arrow."),
20503: dict(d=d20503, stmtKind="DEFINITION",
  statement=r"<b>Minimal polynomial (Axler 5.24, 5.29).</b> For $T\in\mathcal L(V)$ with $V$ finite-dimensional, there is a unique monic polynomial $q$ of smallest degree with $q(T)=0$; it is the minimal polynomial of $T$, and $\deg q\le\dim V$. If $p\in\mathcal P(\mathbb F)$ then $p(T)=0$ if and only if $q$ divides $p$.",
  hint="What is the shortest recipe of repeated edits that sends every arrow to the pin?",
  breakdown=[r"<strong>$q(T)=0$, monic, minimal degree</strong> = the shortest edit recipe that wipes every arrow to the pin.",
             r"<strong>$p(T)=0\iff q\mid p$</strong> = divide $p$ by $q$; the remainder would be a shorter wiping recipe, so it must be zero.",
             r"<strong>Why it matters:</strong> $q$ is a fingerprint of the edit; its roots and their powers reveal whether the edit can be made diagonal."],
  conn=r"<strong>The fewest steps to undo everything.</strong> A reflection twice is the identity, so $T^2-I=0$: the recipe $z^2-1$ wipes everything, and nothing shorter does unless the reflection is trivial.",
  cap="q is the lowest-degree monic recipe with q(T) = 0; any other wiping recipe p is a multiple of q: p(T) = 0 ⇔ q | p."),
20504: dict(d=d20504, stmtKind="THEOREM",
  statement=r"<b>Cayley–Hamilton and the zeros of the minimal polynomial (Axler 8.37, 5.27).</b> Over $\mathbb C$, if $p_T$ is the characteristic polynomial of $T$ then $p_T(T)=0$; hence the minimal polynomial $q$ divides $p_T$. The zeros of $q$ are exactly the eigenvalues of $T$.",
  hint="Which recipe always wipes the photo, and where do its roots sit?",
  breakdown=[r"<strong>$p_T(T)=0$</strong> = every edit satisfies its own characteristic polynomial.",
             r"<strong>$q\mid p_T$</strong> = so the minimal polynomial is a factor of it, with the same or smaller exponents.",
             r"<strong>roots of $q$ = eigenvalues</strong> = if $Tv=\lambda v$ then $q(\lambda)v=q(T)v=0$, so $q(\lambda)=0$; and every root is an eigenvalue."],
  conn=r"<strong>Two fingerprints of the same edit.</strong> The characteristic polynomial counts every stretch factor with full multiplicity; the minimal polynomial is the trimmed version that still wipes the photo. Both list the same stretch factors.",
  cap="Cayley–Hamilton: pᴛ(T) = 0, so q divides pᴛ. The roots of q are exactly the eigenvalues of T."),
20505: dict(d=d20505, stmtKind="THEOREM",
  statement=r"<b>Diagonalizability via the minimal polynomial (Axler 5.62).</b> $T\in\mathcal L(V)$ is diagonalizable if and only if its minimal polynomial equals $(z-\lambda_1)\cdots(z-\lambda_m)$ for some list of distinct $\lambda_1,\dots,\lambda_m\in\mathbb F$.",
  hint="How can the minimal polynomial tell you if a grid of eigen-arrows exists?",
  breakdown=[r"<strong>$q(z)=\prod(z-\lambda_j)$ distinct</strong> = each factor appears once.",
             r"<strong>⇒ diagonalizable</strong> = then $V$ splits into the eigenspaces $\operatorname{null}(T-\lambda_jI)$, so a grid of eigen-arrows exists.",
             r"<strong>repeated factor</strong> = some arrow needs $(T-\lambda I)^2$ to vanish: it is tilted by the edit, not just stretched (a Jordan chain)."],
  conn=r"<strong>Stretch only, or a hidden shear?</strong> If one application of each $(T-\lambda I)$ is enough to kill every arrow, the edit is a pure stretch along some grid. If you need a square, a shear is hiding inside.",
  cap="Left: q has distinct roots, eigen-arrows fill the photo, diagonalizable. Right: q = (z − 2)², e₂ is sheared, not diagonalizable."),
20506: dict(d=d20506, stmtKind="WORKED EXAMPLE",
  statement=r"<b>Example.</b> $A=\begin{pmatrix}2&1\\0&2\end{pmatrix}$ and $2I$ both have characteristic polynomial $(z-2)^2$. Since $A-2I\ne0$ but $(A-2I)^2=0$, $q_A=(z-2)^2$, so $A$ is not diagonalizable; $q_{2I}=z-2$, so $2I$ is diagonalizable.",
  hint="Two edits both stretch by 2. Why is only one of them a pure zoom?",
  breakdown=[r"<strong>$A-2I=\begin{pmatrix}0&1\\0&0\end{pmatrix}\ne0$</strong> = after removing the zoom, a shear is left.",
             r"<strong>$(A-2I)^2=0$</strong> = the shear dies on the second application, so $q_A=(z-2)^2$ (repeated root).",
             r"<strong>$q_{2I}=z-2$</strong> = a pure zoom is wiped by one factor: distinct roots, diagonal."],
  conn=r"<strong>Zoom versus zoom-and-shear.</strong> Both edits make everything twice as big, so their characteristic polynomials agree. Only the minimal polynomial notices the extra shear hiding in $A$.",
  cap="A = [2 1; 0 2] has (A − 2I)² = 0 but A − 2I ≠ 0, so qᴀ = (z − 2)²; 2I has q = z − 2."),
}

STORY = {
 20501: dict(s="STORY 5 · STEP 1 · REPEAT THE EDIT", b="To understand one edit deeply, apply it again and again: <b>polynomials of $T$</b> are recipes of repeated edits.",
   f=[["20405", "the edit itself, independent of the grid"]], n=[["20502", "repeats force an eigenvalue"], ["20503", "the shortest wiping recipe"]]),
 20502: dict(s="STORY 5 · STEP 2 · SOME ARROW ONLY STRETCHES", b="Over $\\mathbb C$ repeated edits must become dependent, and factoring the recipe forces an <b>eigenvalue</b> to exist.",
   f=[["20501", "p(T)"], ["20201", "dependence"]], n=[["20601", "eigenvectors in detail"]]),
 20503: dict(s="STORY 5 · STEP 3 · THE FINGERPRINT", b="The <b>minimal polynomial</b> is the shortest recipe that wipes everything; every other wiping recipe is a multiple of it.",
   f=[["20501", "recipes"]], n=[["20504", "Cayley–Hamilton"], ["20505", "diagonalizable test"]]),
 20504: dict(s="STORY 5 · STEP 4 · TWO FINGERPRINTS", b="The characteristic polynomial also wipes the edit, so the minimal polynomial divides it, and <b>both have the eigenvalues as roots</b>.",
   f=[["20503", "minimal polynomial"]], n=[["20602", "compute the characteristic polynomial"], ["20904", "read both off the Jordan form"]]),
 20505: dict(s="STORY 5 · STEP 5 · THE TEST", b="An edit is a pure stretch along some grid exactly when its minimal polynomial has <b>no repeated root</b>.",
   f=[["20503", "minimal polynomial"]], n=[["20506", "an example of each"], ["20604", "diagonalizability in other words"]]),
 20506: dict(s="STORY 5 · STEP 6 · WITH NUMBERS", b="Same characteristic polynomial, different minimal polynomials: only one of the two edits is diagonal.",
   f=[["20505", "the test"]], n=[["20601", "now: arrows the edit only stretches"]]),
}

FIX = {cid: {"stmtKind": v["stmtKind"], "statement": v["statement"], "hint": v["hint"], "breakdown": v["breakdown"],
             "personalConnection": v["conn"], "drawingSvg": v["d"](cid), "drawingCaption": v["cap"],
             "textbookImg": None, "textbookRef": None} for cid, v in CARDS.items()}
