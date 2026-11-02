"""LAA topic 08 (nilpotent operators, generalized eigenspaces). Photo picture: a nilpotent
edit flattens the photo one dimension at a time until everything sits on the pin."""
from laa_lib import *

SUBJECT = "LAA"

def chain3(y, labs, tail="0"):
    xs = [14, 72, 130, 188]
    out = []
    for i, lab in enumerate(labs + [tail]):
        out += [R(xs[i], y, 40, 22, "#ffffff" if i < len(labs) else "#d9dee7", 1, 3), N(xs[i] + 20, y + 14, lab, 7.5, "middle")]
        if i: out.append(L(xs[i - 1] + 41, y + 11, xs[i] - 1, y + 11, 1, ar=True))
    return "".join(out)

def d20801(c):
    return svg(c,
        N(120, 12, "each application flattens one more direction", 7.5, "middle"),
        chain3(24, ["e₃", "e₂", "e₁"]), N(51, 60, "N", 7.5, "middle"), N(109, 60, "N", 7.5, "middle"), N(167, 60, "N", 7.5, "middle"),
        N(120, 82, "Nᵏ = 0 ⇒ only eigenvalue 0, and N^dim V = 0", 7.5, "middle"),
        N(120, 98, "Nv = λv ⇒ 0 = Nᵏv = λᵏv ⇒ λ = 0", 7.5, "middle"),
        N(120, 122, "(I − N)⁻¹ = I + N + … + Nᵏ⁻¹", 8, "middle"), N(120, 136, "(the series stops: no infinite sum needed)", 7, "middle"))

def d20802(c):
    return svg(c,
        N(120, 12, "(T − λI) applied again and again", 7.5, "middle"),
        chain3(24, ["v", "(T−λI)v", "(T−λI)²v"]),
        N(14, 66, "eigenvector: dies after 1 step  (k = 1)", 7.5, "start"),
        N(14, 78, "generalized: dies after k steps", 7.5, "start"),
        E(120, 112, 100, 22, 0, "#ffffff", 1), E(120, 112, 46, 14, 0, "#f1f5f9", 1),
        N(120, 115, "E(λ, T)", 7.5, "middle"), N(206, 108, "G(λ, T) =", 7, "end"), N(206, 118, "null(T − λI)ⁿ", 7, "end"))

def d20803(c):
    return svg(c,
        N(120, 12, "V = G(λ₁, T) ⊕ … ⊕ G(λₘ, T) over ℂ", 8, "middle"),
        R(20, 26, 200, 80, "#ffffff", 1, 3),
        R(20, 26, 70, 34, "#d9dee7", 1, 0), N(55, 46, "λ₁I + N₁", 7.5, "middle"),
        R(90, 60, 60, 26, "#d9dee7", 1, 0), N(120, 77, "λ₂I + N₂", 7.5, "middle"),
        R(150, 86, 70, 20, "#d9dee7", 1, 0), N(185, 99, "λ₃I + N₃", 7.5, "middle"),
        N(160, 44, "zeros off the blocks", 7, "middle"),
        N(120, 122, "each block: one stretch λⱼ plus a nilpotent part Nⱼ", 7.5, "middle"),
        N(120, 136, "the blocks never mix (each G(λⱼ) is T-invariant)", 7, "middle"))

def d20804(c):
    rows = [("λ = 2", 3, 2), ("λ = 5", 2, 2)]
    out = [N(120, 12, "dim G(λ) = how often λ is a root of pᴛ", 7.5, "middle")]
    for i, (lab, alg, geo) in enumerate(rows):
        y = 32 + 42 * i
        out += [N(14, y + 12, lab, 8, "start")]
        for k in range(alg):
            out.append(R(56 + 26 * k, y, 22, 20, "#d9dee7" if k < geo else "#ffffff", 1, 2, None if k < geo else "3 2"))
        out += [N(140, y + 8, f"dim G = {alg}", 7.5, "start"), N(140, y + 19, f"dim E = {geo}", 7.5, "start")]
    out += [N(120, 124, "Σ dim G(λⱼ) = dim V; E(λ) ⊆ G(λ)", 7.5, "middle"),
            N(120, 137, "diagonalizable ⇔ E(λ) = G(λ) for every λ", 7.5, "middle")]
    return svg(c, *out)

def d20805(c):
    return svg(c,
        N(120, 12, "a chain: N^(m−1)v ≠ 0, Nᵐv = 0", 7.5, "middle"),
        chain3(26, ["v", "Nv", "N²v"]),
        N(120, 66, "v, Nv, …, N^(m−1)v are independent", 7.5, "middle"),
        R(70, 76, 100, 44, "#ffffff", 1, 3),
        N(120, 92, "0 1 0", 8, "middle"), N(120, 104, "0 0 1", 8, "middle"), N(120, 116, "0 0 0", 8, "middle"),
        N(66, 100, "Jₘ(0) =", 8, "end"),
        N(120, 136, "in the basis N²v, Nv, v: ones above the diagonal", 7, "middle"))

def d20806(c):
    return svg(c,
        N(120, 12, "the shift N: e₃ → e₂ → e₁ → 0", 8, "middle"),
        *[R(20 + 74 * k, 30, 54, 54, "#ffffff", 1, 3) for k in range(3)],
        sheet([(28, 76), (66, 76), (66, 40), (28, 40)], "#f1f5f9"), L(104, 76, 140, 40, 1), C(216, 66, 2.4),
        N(47, 108, "range: a plane", 6.8, "middle"), N(121, 108, "range: a line", 6.8, "middle"), N(195, 108, "range: the pin", 6.8, "middle"),
        N(47, 96, "dim null N = 1", 7, "middle"), N(121, 96, "dim null N² = 2", 7, "middle"), N(195, 96, "dim null N³ = 3", 7, "middle"),
        N(47, 27, "N", 8, "middle"), N(121, 27, "N²", 8, "middle"), N(195, 27, "N³ = 0", 8, "middle"),
        N(120, 124, "increments 1, 1, 1 ⇒ one chain of length 3", 7.5, "middle"),
        N(120, 137, "N is itself the Jordan block J₃(0)", 7.5, "middle"))

CARDS = {
20801: dict(d=d20801, stmtKind="DEFINITION",
  statement=r"<b>Nilpotent operator (Axler 8.8, 8.16, 8.17).</b> $N\in\mathcal L(V)$ is nilpotent if $N^k=0$ for some positive integer $k$. If $N$ is nilpotent then $0$ is its only eigenvalue and $N^{\dim V}=0$. Then $I-N$ is invertible with $(I-N)^{-1}=I+N+\dots+N^{k-1}$.",
  hint="Which edit, repeated a few times, flattens the whole photo to the pin?",
  breakdown=[r"<strong>$N^k=0$</strong> = after $k$ repeats every arrow is on the pin.",
             r"<strong>only eigenvalue $0$</strong> = if $Nv=\lambda v$ then $0=N^kv=\lambda^kv$, so $\lambda=0$; and $N^{\dim V}=0$, so you never need more repeats than the dimension.",
             r"<strong>$(I-N)^{-1}=\sum_{j\lt k}N^j$</strong> = the geometric series stops after $k$ terms, because the later powers are zero."],
  conn=r"<strong>Flatten, flatten, gone.</strong> A filter that sends the depth direction to the vertical, the vertical to the horizontal and the horizontal to nothing: three applications and the photo is a dot.",
  cap="The shift N sends e₃ → e₂ → e₁ → 0, so N³ = 0: its only eigenvalue is 0, and (I − N)⁻¹ = I + N + N²."),
20802: dict(d=d20802, stmtKind="DEFINITION",
  statement=r"<b>Generalized eigenvector (Axler 8.9, 8.11).</b> Let $T\in\mathcal L(V)$ and $\lambda$ an eigenvalue. A vector $v\ne0$ is a generalized eigenvector of $T$ for $\lambda$ if $(T-\lambda I)^kv=0$ for some positive integer $k$. The generalized eigenspace is $G(\lambda,T)=\operatorname{null}(T-\lambda I)^{\dim V}$; it contains $E(\lambda,T)$ and is invariant under $T$.",
  hint="If an arrow isn't stretched by λ exactly, how many more steps until it is?",
  breakdown=[r"<strong>$(T-\lambda I)^kv=0$</strong> = after removing the stretch $\lambda$, a few repeats of what is left kill $v$.",
             r"<strong>$G(\lambda,T)=\operatorname{null}(T-\lambda I)^{\dim V}$</strong> = $\dim V$ repeats are always enough.",
             r"<strong>$\supseteq E(\lambda,T)$</strong> = ordinary eigenvectors are the case $k=1$; the generalized ones fill in when eigenvectors are too few."],
  conn=r"<strong>Stretch plus a little shear.</strong> Under a zoom-and-shear, a sheared arrow is not stretched cleanly, but subtract the zoom and apply the leftover shear twice: it dies. That arrow is a generalized eigenvector.",
  cap="An eigenvector dies after one step of (T − λI); a generalized eigenvector after k steps. G(λ, T) = null(T − λI)ⁿ contains E(λ, T)."),
20803: dict(d=d20803, stmtKind="THEOREM",
  statement=r"<b>Generalized eigenspace decomposition (Axler 8.22).</b> Suppose $V$ is a finite-dimensional complex vector space, $T\in\mathcal L(V)$, and $\lambda_1,\dots,\lambda_m$ are its distinct eigenvalues. Then $V=G(\lambda_1,T)\oplus\dots\oplus G(\lambda_m,T)$, each $G(\lambda_j,T)$ is invariant under $T$, and $(T-\lambda_jI)|_{G(\lambda_j,T)}$ is nilpotent.",
  hint="How does every complex edit split into blocks with a single stretch factor each?",
  breakdown=[r"<strong>$V=\bigoplus_jG(\lambda_j,T)$</strong> = the photo splits into pieces, one per stretch factor, with nothing left over.",
             r"<strong>$T|_{G(\lambda_j)}=\lambda_jI+N_j$</strong> = on each piece the edit is the stretch $\lambda_j$ plus a nilpotent part.",
             r"<strong>block diagonal</strong> = each piece is $T$-invariant, so in an adapted basis the matrix has zeros off the blocks."],
  conn=r"<strong>Every edit is zooms plus collapsing shears.</strong> Over $\mathbb C$, cut the space into pieces; on each piece the edit is one zoom plus a shear that eventually flattens. That is the whole structure of any operator.",
  cap="V splits into G(λ₁) ⊕ G(λ₂) ⊕ G(λ₃); on each block T = λⱼI + Nⱼ with Nⱼ nilpotent, and the blocks do not mix."),
20804: dict(d=d20804, stmtKind="THEOREM",
  statement=r"<b>Multiplicity (Axler 8.26, 8.36).</b> For $T$ on a finite-dimensional complex $V$, the multiplicity of $\lambda$ is $\dim G(\lambda,T)$, and this equals its multiplicity as a zero of the characteristic polynomial. The multiplicities sum to $\dim V$. $T$ is diagonalizable iff $E(\lambda,T)=G(\lambda,T)$ for every eigenvalue $\lambda$.",
  hint="How many directions does each stretch factor really own?",
  breakdown=[r"<strong>$\dim G(\lambda,T)$</strong> = all directions belonging to $\lambda$, including the sheared ones.",
             r"<strong>$=\operatorname{mult}_{p_T}(\lambda)$</strong> = exactly the number of times $\lambda$ is a root.",
             r"<strong>$\sum_j\dim G(\lambda_j)=\dim V$</strong> = the pieces fill the space; diagonalizable means no sheared directions, $E=G$."],
  conn=r"<strong>Owned directions.</strong> If 2 is a triple root, three directions belong to the zoom-by-2 piece; perhaps only two of them are clean eigen-arrows, and the third is sheared.",
  cap="Each eigenvalue owns dim G(λ) = its root multiplicity directions (boxes); shaded boxes are true eigen-arrows, dashed ones are sheared. Σ dim G(λⱼ) = dim V."),
20805: dict(d=d20805, stmtKind="LEMMA",
  statement=r"<b>Nilpotent chains.</b> Let $N\in\mathcal L(V)$ be nilpotent and $v\in V$ with $N^{m-1}v\ne0$, $N^mv=0$. Then $v,Nv,\dots,N^{m-1}v$ is linearly independent, and in the basis $N^{m-1}v,\dots,Nv,v$ of its span the matrix of $N$ is the Jordan block $J_m(0)$. Every nilpotent operator has a basis made of such chains (Axler 8.45).",
  hint="Follow one arrow under a flattening edit. Why are its images independent?",
  breakdown=[r"<strong>$N^{m-1}v\ne0,\ N^mv=0$</strong> = the arrow survives $m-1$ steps and dies at step $m$.",
             r"<strong>independent</strong> = apply $N^{m-1}$ to a relation $\sum a_jN^jv=0$: only $a_0N^{m-1}v$ survives, so $a_0=0$; repeat.",
             r"<strong>$J_m(0)$</strong> = in the reversed chain basis, $N$ moves each vector to the previous one: ones just above the diagonal."],
  conn=r"<strong>A conveyor belt to the pin.</strong> The flatten edit moves each arrow one slot along a belt, and the last slot drops it at the pin. The belt's slots are a basis, and the matrix is just 'move one slot'.",
  cap="The chain v → Nv → N²v → 0 is independent; in the basis N²v, Nv, v the matrix of N is the block J₃(0) with ones above the diagonal."),
20806: dict(d=d20806, stmtKind="WORKED EXAMPLE",
  statement=r"<b>Example.</b> $N=\begin{pmatrix}0&1&0\\0&0&1\\0&0&0\end{pmatrix}$ on $\mathbb C^3$ sends $e_3\mapsto e_2\mapsto e_1\mapsto0$. $N^2\ne0$, $N^3=0$, and $\dim\operatorname{null}N^k=1,2,3$ for $k=1,2,3$. The increments $1,1,1$ show one chain of length 3, so $N=J_3(0)$.",
  hint="How do the null-space sizes of N, N², N³ reveal the chain lengths?",
  breakdown=[r"<strong>$N^2\ne0,\ N^3=0$</strong> = it takes exactly 3 steps to flatten: the index equals $\dim V$.",
             r"<strong>$\dim\operatorname{null}N^k=1,2,3$</strong> = each extra power kills one more direction.",
             r"<strong>increments $1,1,1$</strong> = one chain survives each step, so there is a single chain of length 3."],
  conn=r"<strong>Watching the photo shrink.</strong> After one shift a line is gone, after two a plane is gone, after three everything. One direction lost per step means one long conveyor belt.",
  cap="The null spaces of N, N², N³ have dims 1, 2, 3; the increments 1, 1, 1 mean one chain of length 3, so N = J₃(0)."),
}

STORY = {
 20801: dict(s="STORY 8 · STEP 1 · EDITS THAT FLATTEN", b="When eigen-arrows run out, a new ingredient appears: <b>nilpotent</b> edits that flatten everything after a few repeats.",
   f=[["20605", "too few eigen-arrows"]], n=[["20802", "arrows that die after k steps"], ["20805", "follow one arrow"]]),
 20802: dict(s="STORY 8 · STEP 2 · ALMOST EIGEN", b="A <b>generalized eigenvector</b> is killed by a few repeats of $T-\\lambda I$; they fill in for missing eigenvectors.",
   f=[["20801", "nilpotent"], ["20601", "eigenvectors"]], n=[["20803", "they fill the whole space"]]),
 20803: dict(s="STORY 8 · STEP 3 · THE BIG SPLIT", b="Over $\\mathbb C$ the space splits into <b>generalized eigenspaces</b>; on each, the edit is a stretch plus a nilpotent part.",
   f=[["20802", "generalized eigenspaces"], ["20701", "invariant subspaces"]], n=[["20804", "how big each piece is"], ["20902", "Jordan form"]]),
 20804: dict(s="STORY 8 · STEP 4 · HOW BIG", b="Each generalized eigenspace has dimension equal to the <b>root multiplicity</b>; diagonalizable means $E=G$ everywhere.",
   f=[["20803", "decomposition"], ["20605", "algebraic multiplicity"]], n=[["20805", "chains inside each piece"]]),
 20805: dict(s="STORY 8 · STEP 5 · CHAINS", b="Inside a nilpotent piece, follow one arrow: its images form a <b>chain</b>, and the matrix is a Jordan block.",
   f=[["20801", "nilpotent"]], n=[["20806", "count chains"], ["20901", "the Jordan block"]]),
 20806: dict(s="STORY 8 · STEP 6 · WITH NUMBERS", b="Read chain lengths from the null-space sizes of $N,N^2,N^3$.",
   f=[["20805", "chains"]], n=[["20903", "the same counting for Jordan blocks"]]),
}

FIX = {cid: {"stmtKind": v["stmtKind"], "statement": v["statement"], "hint": v["hint"], "breakdown": v["breakdown"],
             "personalConnection": v["conn"], "drawingSvg": v["d"](cid), "drawingCaption": v["cap"],
             "textbookImg": None, "textbookRef": None} for cid, v in CARDS.items()}
