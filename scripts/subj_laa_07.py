"""LAA topic 07 (invariant subspaces, commuting operators). Photo picture: two edits S, T
commute when doing them in either order gives the same photo."""
from laa_lib import *

SUBJECT = "LAA"

def d20701(c):
    O = (64, 100)
    return svg(c,
        L(14, 124, 150, 52, 1), N(150, 48, "U", 8, "end"),
        pin(*O, None), vec(O, (96, 83), "u", 0, -6, "middle"), vec(O, (124, 68), "Tu ∈ U", 2, 14),
        N(236, 22, "T(U) ⊆ U: arrows on U", 7.5, "end"), N(236, 33, "stay on U", 7.5, "end"),
        N(236, 94, "basis of U first:", 7.5, "end"), N(236, 108, "A = [ T|ᵤ  * ]", 8, "end"), N(236, 120, "      [  0   * ]", 8, "end"),
        N(12, 14, "examples: null T, range T, eigenspaces", 7, "start"))

def d20702(c):
    O = (70, 100)
    return svg(c,
        L(14, 128, 160, 50, 1, "3 2"), N(34, 138, "E(λ, T)", 7.5, "start"),
        pin(*O, None), vec(O, (100, 84), "v", -2, -6, "end"), vec(O, (134, 66), "Sv", 4, -2),
        N(236, 20, "ST = TS, Tv = λv:", 7.5, "end"),
        N(236, 34, "T(Sv) = S(Tv) = λ(Sv)", 7.5, "end"), N(236, 48, "⇒ Sv ∈ E(λ, T)", 7.5, "end"),
        N(236, 120, "S keeps every eigenspace of T", 7, "end"), N(236, 132, "(and vice versa)", 7, "end"))

def d20703(c):
    O = (56, 104)
    a, b = (28, -14), (10, -26)
    p = lambda i, j: (O[0] + i * a[0] + j * b[0], O[1] + i * a[1] + j * b[1])
    g = [L(*p(i, 0), *p(i, 3), .5, "2 2") for i in range(4)] + [L(*p(0, j), *p(3, j), .5, "2 2") for j in range(4)]
    return svg(c, *g, pin(*O, None),
        vec(O, p(1, 0), "v₁", 2, 10, "middle", 7.5), vec(O, p(0, 1), "v₂", -4, 0, "end", 7.5),
        N(236, 20, "one grid for both edits", 7.5, "end"),
        N(236, 42, "P⁻¹SP and P⁻¹TP", 7.5, "end"), N(236, 54, "both diagonal", 7.5, "end"),
        N(236, 84, "⇔ ST = TS", 8.5, "end"),
        N(236, 116, "diagonal matrices commute,", 7, "end"), N(236, 126, "so shared grids force ST = TS", 7, "end"))

def d20704(c):
    O = (70, 100)
    return svg(c,
        pin(*O, None), vec(O, (130, 74), "v", 4, 0),
        N(120, 12, "over ℂ commuting edits share an eigen-arrow", 7.5, "middle"),
        N(236, 104, "Sv = αv,  Tv = βv", 8, "end"),
        N(236, 118, "(S + T)v = (α + β)v", 7.5, "end"), N(236, 130, "(ST)v = αβv", 7.5, "end"),
        N(12, 40, "a nonzero eigenspace of T is S-invariant,", 7, "start"), N(12, 50, "so S has an eigenvector inside it", 7, "start"),
        N(12, 134, "repeat ⇒ both upper-triangular together", 7, "start"))

def d20705(c):
    O = (84, 96)
    s = 14
    P = lambda x, y: (O[0] + s * x, O[1] - s * y)
    return svg(c,
        L(14, 96, 160, 96, .6), L(84, 140, 84, 8, .6), pin(*O, None),
        vec(O, P(1, 1), "(1,1)", -4, -2, "end", 7.5), vec(O, P(3, 3), "B(1,1) = 3(1,1)", 4, 0, "start", 7.5),
        vec(O, P(1, -1), "(1,−1)", 4, 8, "start", 7.5), vec(O, P(-1, 1), "B(1,−1) = −(1,−1)", -2, -4, "end", 7),
        N(236, 112, "A = swap, B = I + 2A", 7.5, "end"), N(236, 124, "Bv = (1 + 2λ)v", 7.5, "end"), N(236, 136, "(1, 3) and (−1, −1)", 7.5, "end"))

CARDS = {
20701: dict(d=d20701, stmtKind="DEFINITION",
  statement=r"<b>Invariant subspace (Axler 5.2).</b> Let $T\in\mathcal L(V)$. A subspace $U$ of $V$ is invariant under $T$ if $Tu\in U$ for every $u\in U$; then $T|_U\in\mathcal L(U)$. In a basis of $V$ extending a basis of $U$, the matrix of $T$ is block upper-triangular $\begin{pmatrix}\mathcal M(T|_U)&*\\0&*\end{pmatrix}$.",
  hint="Which lines or sheets does the edit keep inside themselves?",
  breakdown=[r"<strong>$T(U)\subseteq U$</strong> = arrows on $U$ stay on $U$ after the edit.",
             r"<strong>$T|_U$</strong> = restrict the edit to $U$: a smaller edit on a smaller space.",
             r"<strong>block $\begin{pmatrix}A|_U&*\\0&*\end{pmatrix}$</strong> = the zero block says the $U$-part never leaks out, so the big problem splits into smaller ones."],
  conn=r"<strong>A line the edit keeps.</strong> A horizontal stretch keeps the horizontal line through the pin: horizontal arrows stay horizontal. A 1-D invariant line is exactly an eigen-arrow's line.",
  cap="Arrows on U stay on U: T(U) ⊆ U. With a basis of U first, the matrix has the block form [T|ᵤ *; 0 *]."),
20702: dict(d=d20702, stmtKind="PROPOSITION",
  statement=r"<b>Commuting operators preserve eigenspaces (Axler 5.75).</b> Suppose $S,T\in\mathcal L(V)$ commute and $\lambda\in\mathbb F$. Then $E(\lambda,T)$ is invariant under $S$: if $Tv=\lambda v$ then $T(Sv)=\lambda(Sv)$.",
  hint="If two edits commute, what does one do to the other's eigen-arrows?",
  breakdown=[r"<strong>$ST=TS$</strong> = doing the edits in either order gives the same photo.",
             r"<strong>$T(Sv)=S(Tv)=\lambda(Sv)$</strong> = after $S$, the arrow $Sv$ is still stretched by $\lambda$ under $T$.",
             r"<strong>so $S$ maps $E(\lambda,T)$ into itself</strong> = look for $S$'s eigen-arrows inside each eigenspace of $T$; they are eigen-arrows of both."],
  conn=r"<strong>Zoom then rotate, rotate then zoom.</strong> A uniform zoom commutes with everything, and every arrow is its eigen-arrow. Two edits that commute respect each other's special directions.",
  cap="If ST = TS and v ∈ E(λ, T), then T(Sv) = S(Tv) = λ(Sv), so Sv stays in E(λ, T)."),
20703: dict(d=d20703, stmtKind="THEOREM",
  statement=r"<b>Simultaneous diagonalizability (Axler 5.76).</b> Two diagonalizable operators on the same vector space have diagonal matrices with respect to the same basis if and only if the two operators commute.",
  hint="When can one grid make two edits pure stretches at the same time?",
  breakdown=[r"<strong>$P^{-1}SP,\ P^{-1}TP$ diagonal</strong> = one grid of arrows that both edits only stretch.",
             r"<strong>$\Leftarrow ST=TS$</strong> = split $V$ into eigenspaces of $T$; each is $S$-invariant, and $S$ is still diagonalizable there, so diagonalize it inside each one.",
             r"<strong>$\Rightarrow$</strong> = diagonal matrices commute, so $S=PD_1P^{-1}$ and $T=PD_2P^{-1}$ commute."],
  conn=r"<strong>One grid, two filters.</strong> A horizontal stretch and a vertical squash share the grid of horizontal and vertical lines, and doing them in either order gives the same photo. A stretch and a rotation share no grid and do not commute.",
  cap="One eigen-grid v₁, v₂ makes both edits diagonal: P⁻¹SP and P⁻¹TP. This happens exactly when ST = TS."),
20704: dict(d=d20704, stmtKind="THEOREM",
  statement=r"<b>Common eigenvector (Axler 5.78, 5.80).</b> Every pair of commuting operators on a finite-dimensional, nonzero, complex vector space has a common eigenvector. Commuting operators on such a space are simultaneously upper-triangularizable, and then the eigenvalues of $S+T$ and $ST$ are $\alpha_j+\beta_j$ and $\alpha_j\beta_j$.",
  hint="Two commuting edits on a complex space: is there always an arrow both only stretch?",
  breakdown=[r"<strong>$Sv=\alpha v,\ Tv=\beta v$</strong> = one arrow stretched by both edits, by $\alpha$ and $\beta$.",
             r"<strong>Why it exists:</strong> an eigenspace of $T$ is $S$-invariant, and over $\mathbb C$ the restricted $S$ has an eigenvector there.",
             r"<strong>$\operatorname{spec}(S+T)=\{\alpha_j+\beta_j\}$</strong> = in the shared triangular grid the diagonals add and multiply entry by entry."],
  conn=r"<strong>A shared fixed direction.</strong> Even if two commuting edits can't both be made diagonal, there is always a direction neither one turns. Build the grid from it and both become triangular together.",
  cap="Commuting S and T on ℂⁿ share an eigen-arrow v: Sv = αv and Tv = βv, so (S + T)v = (α + β)v and (ST)v = αβv."),
20705: dict(d=d20705, stmtKind="WORKED EXAMPLE",
  statement=r"<b>Example.</b> $A=\begin{pmatrix}0&1\\1&0\end{pmatrix}$, $B=\begin{pmatrix}1&2\\2&1\end{pmatrix}=I+2A$, so $AB=BA$. Eigenvectors of $A$: $(1,1)$ with $1$ and $(1,-1)$ with $-1$. Then $Bv=(1+2\lambda)v$, giving eigenvalues $3$ and $-1$ on the same vectors; $P=\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ diagonalizes both.",
  hint="B is built from A. Why must it have the same eigen-arrows?",
  breakdown=[r"<strong>$B=I+2A$</strong> = $B$ is a polynomial in $A$, so it commutes with $A$.",
             r"<strong>$Bv=(1+2\lambda)v$</strong> = on each eigen-arrow of $A$, $B$ stretches by $1+2\lambda$.",
             r"<strong>$(1,3)$ and $(-1,-1)$</strong> = the pairs (eigenvalue of $A$, of $B$) on $(1,1)$ and $(1,-1)$."],
  conn=r"<strong>A filter built from a filter.</strong> $A$ mirrors the photo across the diagonal. $B$ is 'leave it, then add two mirrors'; it can only stretch the arrows the mirror keeps.",
  cap="B = I + 2A stretches (1,1) by 3 and flips (1,−1) (factor −1): the same eigen-arrows as the swap A, with Bv = (1 + 2λ)v."),
}

STORY = {
 20701: dict(s="STORY 7 · STEP 1 · SUBSPACES IT KEEPS", b="An edit may keep some lines or sheets inside themselves; these <b>invariant subspaces</b> split the edit into smaller pieces.",
   f=[["20601", "eigen-lines are 1-D invariant subspaces"]], n=[["20702", "commuting edits keep each other's"], ["20803", "the big split into generalized eigenspaces"]]),
 20702: dict(s="STORY 7 · STEP 2 · RESPECT", b="If two edits commute, each one <b>keeps the other's eigenspaces</b>.",
   f=[["20701", "invariant subspaces"]], n=[["20703", "one grid for both"]]),
 20703: dict(s="STORY 7 · STEP 3 · ONE GRID FOR TWO", b="Two diagonalizable edits share an eigen-grid <b>exactly when they commute</b>.",
   f=[["20702", "eigenspaces are kept"], ["20604", "diagonalization"]], n=[["20704", "even without diagonalizing"], ["21305", "commuting ⇔ normal in the spectral world"]]),
 20704: dict(s="STORY 7 · STEP 4 · A SHARED DIRECTION", b="Over $\\mathbb C$ commuting edits always share an eigen-arrow, and can be made triangular together.",
   f=[["20703", "simultaneous diagonalization"], ["20502", "eigenvalues exist over ℂ"]], n=[["20705", "an example"]]),
 20705: dict(s="STORY 7 · STEP 5 · WITH NUMBERS", b="A polynomial in $A$ commutes with $A$ and shares its eigen-arrows.",
   f=[["20704", "common eigenvector"], ["20501", "p(A)v = p(λ)v"]], n=[["20801", "edits that eventually flatten everything"]]),
}

FIX = {cid: {"stmtKind": v["stmtKind"], "statement": v["statement"], "hint": v["hint"], "breakdown": v["breakdown"],
             "personalConnection": v["conn"], "drawingSvg": v["d"](cid), "drawingCaption": v["cap"],
             "textbookImg": None, "textbookRef": None} for cid, v in CARDS.items()}
