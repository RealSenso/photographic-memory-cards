import math
from subj_lib import *

card = make_card("LAA")
CARDS = []

def V(x0, y0, x1, y1, w=2.2, d=None):
    return L(x0, y0, x1, y1, w, d=d, ar=True)

def AXES2(cx=120, cy=72, rx=100, ry=58):
    return [L(cx - rx, cy, cx + rx, cy, 0.8, d="2 3"), L(cx, cy - ry, cx, cy + ry, 0.8, d="2 3")]

# ====================== 06 · EIGENVALUES & DIAGONALIZATION ======================
CARDS.append(card(6, 1, "EIGENVALUES", "Eigenvector: Direction Preserved, Length Scaled",
    AXES2() + [V(120, 72, 150, 52, 2.4), V(120, 72, 196, 22, 2.4, "5 3"), N(150, 46, "v", 10, "start", "bold"), N(198, 20, "Tv = λv", 10, "start", "bold"),
               V(120, 72, 100, 100, 2.0), V(120, 72, 160, 116, 1.8, "5 3"), N(96, 112, "w", 10, "end", "bold"), N(164, 122, "Tw", 10, "start"),
               N(40, 22, "on the same line:", 8.5, "start"), N(40, 34, "EIGENvector", 9, "start", "bold"), N(40, 124, "knocked off its line", 8.5, "start")],
    "An eigenvector stays on its own line; a generic vector gets turned off its line",
    ["<strong>Definition:</strong> a nonzero $v$ with $Tv=\\lambda v$ is an <strong>eigenvector</strong>; the scalar $\\lambda$ is its <strong>eigenvalue</strong>. $0$ is never an eigenvector (but $\\lambda=0$ is allowed).",
     "<strong>Eigenspace:</strong> $E(\\lambda,T)=\\operatorname{null}(T-\\lambda I)$, a subspace consisting of $0$ and all eigenvectors for $\\lambda$.",
     "<strong>Meaning:</strong> $\\lambda$ is an eigenvalue $\\iff T-\\lambda I$ is <strong>not injective</strong> $\\iff T-\\lambda I$ not invertible: along that line $T$ acts as pure scaling."],
    r"$$Tv=\lambda v,\ v\ne0;\qquad E(\lambda,T)=\operatorname{null}(T-\lambda I);\qquad \lambda\ \text{eigenvalue}\iff\det(T-\lambda I)=0$$",
    "A sheet of rubber stretched along one axis: points on that axis only slide along it; everything else is dragged sideways too.",
    "Eigenvectors are NONZERO by definition; eigenvalue 0 is allowed and means T is not injective. Also v and 5v are the same direction, so eigenvectors are only defined up to scale."))

def _cp():
    pts = [(x, 112 - ((x - 120) ** 2 / 9.0 - 36) * 0.5 * -1) for x in range(34, 207, 4)]
    pts = [(x, 40 + ((x - 120) ** 2) / 90.0 * 1.0) for x in range(34, 207, 4)]
    return [L(20, 72, 226, 72, 0.9, ar=True), poly([(x, 40 + ((x - 120) ** 2) / 54.0 * 1.0 + 0) for x in range(30, 211, 4)], 2),
            C(78, 72, 3.5, "#ffffff"), C(162, 72, 3.5, "#ffffff"), N(78, 86, "λ = 2", 9, w="bold"), N(162, 86, "λ = 5", 9, w="bold"),
            N(120, 20, "p(λ) = det(λI − A) = λ² − 7λ + 10", 9, w="bold"), N(120, 112, "= (λ − 2)(λ − 5)", 9.5, w="bold"),
            N(120, 128, "roots of p = eigenvalues", 8.5), N(206, 66, "λ", 9)]

CARDS.append(card(6, 2, "EIGENVALUES", "Characteristic Polynomial & How to Find Eigenvalues",
    _cp(),
    "The eigenvalues are exactly where det(λI − A) crosses zero",
    ["<strong>Recipe:</strong> $\\lambda$ is an eigenvalue $\\iff\\det(\\lambda I-A)=0$. Expanding gives the degree-$n$ <strong>characteristic polynomial</strong> $p_A(\\lambda)$.",
     "<strong>Coefficients:</strong> $p_A(\\lambda)=\\lambda^n-(\\operatorname{tr}A)\\lambda^{n-1}+\\dots+(-1)^n\\det A$, so the eigenvalues <strong>sum to the trace and multiply to the determinant</strong>.",
     "<strong>Then:</strong> for each root $\\lambda$ solve $(A-\\lambda I)v=0$ to get its eigenspace. Over $\\mathbb{C}$ there are always $n$ roots counted with multiplicity."],
    r"$$p_A(\lambda)=\det(\lambda I-A)=\lambda^n-\operatorname{tr}(A)\,\lambda^{n-1}+\cdots+(-1)^n\det A$$",
    "Hunting for the notes a bell rings at: sweep the strike frequency (λ) until the 'silent' determinant hits zero.",
    "Sign convention: det(λI − A) is monic, det(A − λI) has sign (−1)ⁿ. Both give the same roots but different constant terms."))

CARDS.append(card(6, 3, "EIGENVALUES", "Eigenvectors of Distinct Eigenvalues Are Independent",
    AXES2() + [V(120, 72, 190, 28, 2.4), V(120, 72, 70, 112, 2.4), V(120, 72, 176, 112, 2.4),
               N(194, 24, "v₁ (λ₁)", 9, "start", "bold"), N(66, 122, "v₂ (λ₂)", 9, "end", "bold"), N(180, 124, "v₃ (λ₃)", 9, "start", "bold"),
               N(30, 22, "λ₁, λ₂, λ₃ distinct ⇒", 8.5, "start", "bold"), N(30, 34, "v₁, v₂, v₃ independent", 8.5, "start", "bold"),
               N(30, 48, "so ≤ n distinct eigenvalues", 8.5, "start")],
    "Different eigenvalues give genuinely different directions, so they can never be dependent",
    ["<strong>Theorem:</strong> eigenvectors belonging to <strong>distinct eigenvalues</strong> are linearly independent.",
     "<strong>Proof (induction):</strong> if $a_1v_1+\\dots+a_mv_m=0$, apply $T-\\lambda_mI$ to kill the last term; the remaining coefficients $a_j(\\lambda_j-\\lambda_m)$ must vanish, and $\\lambda_j\\ne\\lambda_m$ forces $a_j=0$.",
     "<strong>Consequences:</strong> an operator on an $n$-dim space has <strong>at most $n$ distinct eigenvalues</strong>, and if it has exactly $n$, it is diagonalizable."],
    r"$$\lambda_i\ \text{distinct}\ \Longrightarrow\ v_1,\dots,v_m\ \text{independent};\qquad \#\{\text{distinct }\lambda\}\le\dim V$$",
    "Musicians playing different notes can't cancel each other: each is genuinely independent of the rest.",
    "Independence needs DISTINCT eigenvalues. Two eigenvectors of the SAME eigenvalue can be dependent (e.g. v and 2v)."))

CARDS.append(card(6, 4, "DIAGONALIZATION", "When Is an Operator Diagonalizable?",
    [box(60, 10, 120, 24, "T diagonalizable", "#e2e8f0", 10),
     box(10, 46, 104, 24, "∃ basis of eigenvectors", "#f1f5f9", 8.5), box(126, 46, 104, 24, "V = E(λ₁) ⊕ … ⊕ E(λ_m)", "#f1f5f9", 8.5),
     box(10, 80, 104, 24, "Σ dim E(λⱼ) = dim V", "#f1f5f9", 8.5), box(126, 80, 104, 24, "min poly: distinct roots", "#f1f5f9", 8.5),
     box(10, 114, 104, 24, "n distinct eigenvalues ⇒", "#ffffff", 8), box(126, 114, 104, 24, "(sufficient, not necessary)", "#ffffff", 8),
     L(120, 34, 120, 44, 1.2)],
    "Five equivalent ways to say the same thing, plus one convenient sufficient condition",
    ["<strong>Equivalent conditions</strong> for $T\\in\\mathcal{L}(V)$, $\\dim V=n$: (a) $T$ has a basis of <strong>eigenvectors</strong>; (b) $V=\\bigoplus E(\\lambda_j)$; (c) $\\sum\\dim E(\\lambda_j)=n$; (d) the <strong>minimal polynomial</strong> has distinct roots.",
     "<strong>Matrix form:</strong> $A=PDP^{-1}$ with $D$ diagonal and the <strong>columns of $P$ the eigenvectors</strong>. Then $A^k=PD^kP^{-1}$, which makes powers trivial.",
     "<strong>Sufficient:</strong> $n$ distinct eigenvalues. Not necessary: $I$ has one repeated eigenvalue yet is diagonal."],
    r"$$A=PDP^{-1},\quad P=[v_1\cdots v_n],\ D=\operatorname{diag}(\lambda_1,\dots,\lambda_n),\qquad A^k=PD^kP^{-1}$$",
    "Rotating your viewpoint until the machine looks like n independent dials: in the right coordinates every step is just 'scale this axis'.",
    "Having n eigenvalues counted with multiplicity is NOT enough: [[2,1],[0,2]] has eigenvalue 2 twice but only one eigenvector direction."))

CARDS.append(card(6, 5, "DIAGONALIZATION", "Algebraic vs Geometric Multiplicity",
    [L(20, 118, 226, 118, 1.2)] + [R(40, 118 - 50, 30, 50, "#f1f5f9", 1.5), R(76, 118 - 25, 30, 25, "#e2e8f0", 1.5),
     R(140, 118 - 50, 30, 50, "#f1f5f9", 1.5), R(176, 118 - 50, 30, 50, "#e2e8f0", 1.5),
     N(55, 132, "alg", 8.5), N(91, 132, "geo", 8.5), N(155, 132, "alg", 8.5), N(191, 132, "geo", 8.5),
     N(73, 18, "[[2,1],[0,2]]", 9, w="bold"), N(73, 30, "geo < alg: DEFECTIVE", 8.5), N(173, 18, "2I", 9, w="bold"), N(173, 30, "geo = alg: fine", 8.5),
     N(120, 144, "1 ≤ geo(λ) ≤ alg(λ)", 9, w="bold")],
    "Geometric multiplicity (eigenspace dimension) can fall short of algebraic multiplicity (root multiplicity)",
    ["<strong>Algebraic</strong> multiplicity $=$ how many times $\\lambda$ is a root of the characteristic polynomial. <strong>Geometric</strong> multiplicity $=\\dim E(\\lambda,T)$.",
     "<strong>Always</strong> $1\\le\\text{geometric}\\le\\text{algebraic}$. The operator is diagonalizable iff they are <strong>equal for every eigenvalue</strong>.",
     "<strong>Defective eigenvalue:</strong> geometric $<$ algebraic. The missing directions are supplied by <strong>generalized eigenvectors</strong> (Jordan chains) instead."],
    r"$$1\le\dim E(\lambda,T)\le\operatorname{mult}_{p_T}(\lambda),\qquad \text{diagonalizable}\iff\text{equal for all }\lambda$$",
    "A company with 2 job openings (algebraic) but only one real applicant type (geometric): one slot can't be filled by an independent person.",
    "Always compute BOTH. Students stop at the characteristic polynomial and wrongly conclude diagonalizability from repeated roots or from distinct-looking factors."))

CARDS.append(card(6, 6, "WORKED BENCHMARK", "Worked Benchmark: Diagonalize A = [[4,1],[2,3]]",
    [GRID(14, 18, [[4, 1], [2, 3]], cell=26, sz=11), N(40, 86, "A", 10, w="bold"),
     N(90, 22, "tr = 7, det = 10", 9, "start", "bold"), N(90, 36, "λ² − 7λ + 10 = 0 ⇒ λ = 2, 5", 8.5, "start"),
     N(90, 54, "λ=5: (A−5I)v=0: v=(1,1)", 8.5, "start"), N(90, 68, "λ=2: (A−2I)v=0: v=(1,−2)", 8.5, "start"),
     N(90, 88, "check: A(1,1)=(5,5) ✓", 8.5, "start"), N(90, 100, "A(1,−2)=(2,−4)=2(1,−2) ✓", 8.5, "start"),
     N(14, 112, "P = [[1,1],[1,−2]],  D = diag(5, 2)", 9, "start", "bold"), N(14, 128, "A = P D P⁻¹,   A¹⁰ = P D¹⁰ P⁻¹", 9, "start")],
    "Two distinct eigenvalues (5 and 2) give two independent eigenvectors, so A diagonalizes",
    ["<strong>Eigenvalues:</strong> trace $7$ and determinant $10$ give $\\lambda^2-7\\lambda+10=(\\lambda-2)(\\lambda-5)$, so $\\lambda\\in\\{5,2\\}$ (distinct, hence diagonalizable).",
     "<strong>Eigenvectors:</strong> $A-5I=\\begin{pmatrix}-1&1\\\\2&-2\\end{pmatrix}$ gives $(1,1)$; $A-2I=\\begin{pmatrix}2&1\\\\2&1\\end{pmatrix}$ gives $(1,-2)$. Verified: $A(1,1)=(5,5)$ and $A(1,-2)=(2,-4)$.",
     "<strong>Factorization:</strong> $P=\\begin{pmatrix}1&1\\\\1&-2\\end{pmatrix}$, $D=\\operatorname{diag}(5,2)$, $A=PDP^{-1}$. Then $A^{k}$ has eigenvalues $5^k,2^k$ (so the dominant eigenvalue $5$ controls growth)."],
    r"$$A=\begin{pmatrix}1&1\\1&-2\end{pmatrix}\begin{pmatrix}5&0\\0&2\end{pmatrix}\begin{pmatrix}1&1\\1&-2\end{pmatrix}^{-1}$$",
    "Finding the two special directions of a machine; after rotating to them, repeating the machine 10 times is just 5¹⁰ and 2¹⁰ on those axes.",
    "Order matters: the i-th column of P must pair with the i-th diagonal entry of D. Swap one and you get a wrong factorization."))

# ====================== 07 · COMMUTING OPERATORS ======================
CARDS.append(card(7, 1, "INVARIANT SUBSPACES", "Invariant Subspaces & Restriction",
    [PG("30,110 150,110 200,60 80,60", "#f1f5f9", 1.6), N(110, 100, "U", 11, "middle", "bold"),
     C(100, 86, 3.5), V(100, 86, 150, 74, 2), N(154, 72, "Tu ∈ U", 9, "start", "bold"),
     C(80, 36, 3.5, "#ffffff"), V(80, 36, 150, 20, 2, "5 3"), N(154, 18, "Tw leaves U", 9, "start"),
     N(190, 108, "T(U) ⊆ U", 10, "middle", "bold"), N(190, 122, "⇒ T|_U ∈ 𝓛(U)", 9, "middle"), N(60, 130, "eigenlines are 1-D invariant subspaces", 8.5, "start")],
    "U is invariant when T never pushes a vector of U out of U",
    ["<strong>Definition:</strong> $U$ is <strong>invariant</strong> under $T$ if $T(U)\\subseteq U$, so the <strong>restriction</strong> $T|_U\\in\\mathcal{L}(U)$ is a smaller operator in its own right.",
     "<strong>Examples:</strong> $\\{0\\}$, $V$, $\\operatorname{null}T$, $\\operatorname{range}T$, every eigenspace, and the span of any eigenvector (a <strong>1-D invariant subspace</strong>).",
     "<strong>Why it matters:</strong> invariant subspaces split a big problem into smaller blocks; the matrix becomes <strong>block triangular</strong> (or block diagonal if the complement is invariant too)."],
    r"$$T(U)\subseteq U,\qquad A=\begin{pmatrix}A|_U&*\\0&*\end{pmatrix}\ \text{in a basis extending a basis of }U$$",
    "A fenced pasture: whatever the machine does to animals inside the fence leaves them inside the fence.",
    "Invariant is not the same as 'T = identity on U'. T may move every vector of U, as long as the results stay in U."))

CARDS.append(card(7, 2, "COMMUTING OPERATORS", "If ST = TS, Eigenspaces of T Are Invariant Under S",
    [E(120, 72, 80, 50, 0, "#ffffff", 1.6), E(120, 72, 40, 26, 0, "#e2e8f0", 1.8), N(120, 76, "E(λ, T)", 10, "middle", "bold"),
     C(110, 70, 3), V(110, 70, 135, 78, 1.8), N(140, 86, "Sv", 9, "start"),
     N(120, 22, "v ∈ E(λ,T): Tv = λv", 9, w="bold"), N(120, 124, "T(Sv) = S(Tv) = S(λv) = λ(Sv)", 9, w="bold"), N(120, 138, "so Sv ∈ E(λ,T)", 9)],
    "S cannot push an eigenvector of T out of its eigenspace if S and T commute",
    ["<strong>Claim:</strong> if $ST=TS$ and $v\\in E(\\lambda,T)$, then $Sv\\in E(\\lambda,T)$.",
     "<strong>Proof:</strong> $T(Sv)=S(Tv)=S(\\lambda v)=\\lambda(Sv)$. So each eigenspace of $T$ is <strong>invariant under $S$</strong>, and vice versa.",
     "<strong>Use:</strong> restrict $S$ to each eigenspace of $T$ and look for its eigenvectors there; they are then <strong>common eigenvectors</strong> of both."],
    r"$$ST=TS,\ \ Tv=\lambda v\ \Longrightarrow\ T(Sv)=\lambda(Sv)$$",
    "Two machines on one assembly line that don't interfere: whatever the first sorts into a bin, the second leaves inside that bin.",
    "Commuting is symmetric but this uses it in one direction at a time. Without commuting, S can easily move v out of E(λ,T)."))

CARDS.append(card(7, 3, "COMMUTING OPERATORS", "Simultaneous Diagonalization",
    [box(14, 14, 90, 30, "S, T diagonalizable", "#f1f5f9", 8.5), box(14, 54, 90, 30, "ST = TS", "#f1f5f9", 10), L(60, 44, 60, 52, 1.3),
     L(108, 52, 132, 52, 1.6, ar=True), box(134, 24, 92, 56, "ONE basis diagonalizes both", "#e2e8f0", 9),
     N(120, 106, "S = PD₁P⁻¹,   T = PD₂P⁻¹", 9.5, w="bold"), N(120, 124, "(converse: sharing an eigenbasis ⇒ commute)", 8.5), N(120, 138, "diagonal matrices always commute", 8.5)],
    "Commuting + diagonalizable ⇔ a single eigenbasis works for every operator in the family",
    ["<strong>Theorem:</strong> two diagonalizable operators on $V$ are <strong>simultaneously diagonalizable</strong> (share an eigenbasis) $\\iff ST=TS$.",
     "<strong>Idea:</strong> decompose $V$ into eigenspaces of $T$; each is $S$-invariant and $S|_{E}$ is still diagonalizable, so diagonalize it there; the resulting basis diagonalizes both.",
     "<strong>Converse is easy:</strong> if $S=PD_1P^{-1}$ and $T=PD_2P^{-1}$ then $ST=PD_1D_2P^{-1}=TS$ since diagonal matrices commute. This extends to any commuting family."],
    r"$$ST=TS,\ \ S,T\ \text{diagonalizable}\iff\ \exists P:\ P^{-1}SP,\ P^{-1}TP\ \text{both diagonal}$$",
    "Two instruments that can be tuned to the same set of strings: once they share the strings, playing one never disturbs the other.",
    "BOTH operators must be diagonalizable. Commuting alone only gives common eigenvectors (and simultaneous triangularization over ℂ), not diagonalization."))

CARDS.append(card(7, 4, "COMMUTING OPERATORS", "Commuting Operators Share an Eigenvector (⇒ Triangularization)",
    [GRID(10, 18, [["*", "*", "*"], ["0", "*", "*"], ["0", "0", "*"]], cell=22, sz=11, shade={(1, 0), (2, 0), (2, 1)}),
     N(43, 100, "upper triangular", 8.5, w="bold"), N(84, 30, "over ℂ, commuting S, T:", 8.5, "start", "bold"),
     N(84, 46, "a common eigenvector v", 8.5, "start"), N(84, 62, "induct on V / span(v)", 8.5, "start"),
     N(84, 78, "one basis makes", 8.5, "start"), N(84, 90, "BOTH triangular", 8.5, "start", "bold"),
     N(10, 126, "eigenvalues of S+T, ST = sums, products on the diagonal", 8, "start")],
    "Over ℂ, any commuting family can be made upper triangular in one basis",
    ["<strong>Common eigenvector:</strong> a nonzero eigenspace of $T$ is $S$-invariant, so $S$ restricted to it has an eigenvector over $\\mathbb{C}$. That vector is an eigenvector of <strong>both</strong>.",
     "<strong>Induction:</strong> quotient by the common eigenvector and repeat: commuting operators on a complex space are <strong>simultaneously upper-triangularizable</strong>.",
     "<strong>Payoff:</strong> eigenvalues of $S+T$ are sums, and of $ST$ are products, of the matched diagonal entries (eigenvalues pair up along a common triangularizing basis)."],
    r"$$ST=TS\ (\mathbb{C})\ \Rightarrow\ \exists\,v:\ Sv=\alpha v,\ Tv=\beta v;\qquad \operatorname{spec}(S+T)=\{\alpha_j+\beta_j\}$$",
    "Two co-workers sharing one office: because their schedules don't clash, there is always at least one room they both can sit in.",
    "Without commuting, S and T can have NO common eigenvector (a rotation and a reflection in the plane), so the eigenvalues of S+T are not simply sums."))

CARDS.append(card(7, 5, "COMMUTING OPERATORS", "Worked Benchmark: A, B = I + 2A Share Eigenvectors",
    [GRID(10, 14, [[0, 1], [1, 0]], cell=24, sz=11), N(34, 76, "A", 10, w="bold"), GRID(76, 14, [[1, 2], [2, 1]], cell=24, sz=11), N(100, 76, "B = I+2A", 9, w="bold"),
     N(134, 24, "AB = BA ✓", 10, "start", "bold"), N(134, 40, "(1,1): A→1, B→3", 8.5, "start"), N(134, 54, "(1,−1): A→−1, B→−1", 8.5, "start"),
     N(134, 76, "P = [[1,1],[1,−1]]", 9, "start", "bold"), N(134, 90, "P⁻¹AP = diag(1,−1)", 8.5, "start"), N(134, 102, "P⁻¹BP = diag(3,−1)", 8.5, "start"),
     N(10, 114, "B is a polynomial in A, so A's eigenbasis", 8.5, "start"), N(10, 128, "diagonalizes B automatically", 8.5, "start")],
    "B = I + 2A is a polynomial in A, so the eigenbasis of A diagonalizes B too",
    ["<strong>Matrices:</strong> $A=\\begin{pmatrix}0&1\\\\1&0\\end{pmatrix}$ (swap), $B=\\begin{pmatrix}1&2\\\\2&1\\end{pmatrix}=I+2A$. Clearly $AB=A+2A^2=BA$, so they commute.",
     "<strong>Eigenvectors of $A$:</strong> $(1,1)$ with $\\lambda=1$ and $(1,-1)$ with $\\lambda=-1$. Because $B=I+2A$, $Bv=(1+2\\lambda)v$: eigenvalues $3$ and $-1$ on the <strong>same</strong> vectors.",
     "<strong>Result:</strong> with $P=\\begin{pmatrix}1&1\\\\1&-1\\end{pmatrix}$, $P^{-1}AP=\\operatorname{diag}(1,-1)$ and $P^{-1}BP=\\operatorname{diag}(3,-1)$: simultaneous diagonalization."],
    r"$$B=I+2A\ \Rightarrow\ Bv=(1+2\lambda)v:\quad (\lambda_A,\lambda_B)=(1,3)\ \text{and}\ (-1,-1)$$",
    "Two knobs on the same dial: B is just a rescaled, shifted version of A, so any direction A cares about, B cares about in a matching way.",
    "Eigenvalue pairs must be matched along the SAME eigenvector: (1, 3) and (−1, −1). Listing the eigenvalues of A and B separately loses that pairing."))

# ====================== 08 · GENERALIZED EIGENSPACES & NILPOTENT ======================
CARDS.append(card(8, 1, "NILPOTENT OPERATORS", "Nilpotent Operators: N^k = 0",
    [box(14, 20, 40, 26, "v", "#f1f5f9", 11), L(54, 33, 76, 33, 1.5, ar=True), N(65, 27, "N", 9),
     box(78, 20, 40, 26, "Nv", "#f1f5f9", 10), L(118, 33, 140, 33, 1.5, ar=True), N(129, 27, "N", 9),
     box(142, 20, 40, 26, "N²v", "#f1f5f9", 10), L(182, 33, 204, 33, 1.5, ar=True), N(193, 27, "N", 9), N(214, 37, "0", 11, "middle", "bold"),
     N(120, 74, "every vector eventually dies", 9, w="bold"), N(120, 92, "only eigenvalue is 0", 9), N(120, 108, "N^dim V = 0 always", 9), N(120, 124, "char poly of N = λⁿ", 9)],
    "Repeatedly applying a nilpotent operator pushes everything down to zero in at most dim V steps",
    ["<strong>Definition:</strong> $N\\in\\mathcal{L}(V)$ is <strong>nilpotent</strong> if $N^k=0$ for some $k$. Example: the shift $e_3\\to e_2\\to e_1\\to0$.",
     "<strong>Facts:</strong> $0$ is the <strong>only eigenvalue</strong> (if $Nv=\\lambda v$ then $0=N^kv=\\lambda^kv$), so $p_N(\\lambda)=\\lambda^n$ and $N^{\\dim V}=0$.",
     "<strong>Matrix form:</strong> strictly upper triangular in a suitable basis; $I+N$ is always <strong>invertible</strong> with inverse $I-N+N^2-\\cdots$."],
    r"$$N^{k}=0\ \Rightarrow\ \operatorname{spec}(N)=\{0\},\quad N^{\dim V}=0,\quad (I-N)^{-1}=\sum_{j<k}N^{j}$$",
    "A countdown timer: each application removes one level, and after a bounded number of steps nothing is left.",
    "Nilpotent does NOT mean N = 0. The shift operator is nonzero but its powers eventually vanish. And N+M is not nilpotent in general unless they commute."))

CARDS.append(card(8, 2, "GENERALIZED EIGENSPACES", "Generalized Eigenvectors",
    [box(14, 18, 52, 26, "v ≠ 0", "#f1f5f9", 10), L(66, 31, 84, 31, 1.4, ar=True), box(86, 18, 56, 26, "(T−λ)v", "#f1f5f9", 9),
     L(142, 31, 160, 31, 1.4, ar=True), box(162, 18, 56, 26, "(T−λ)²v = 0", "#e2e8f0", 8.5),
     N(120, 68, "eigenvector:  (T−λI)v = 0   (one step)", 9, w="bold"), N(120, 84, "generalized:  (T−λI)^k v = 0   (some k)", 9, w="bold"),
     N(120, 104, "G(λ,T) = null (T−λI)^{dim V}", 10, w="bold"), N(120, 122, "eigenspace ⊆ generalized eigenspace", 8.5)],
    "A generalized eigenvector is killed by some power of (T − λI), not necessarily the first",
    ["<strong>Definition:</strong> $v\\ne0$ is a <strong>generalized eigenvector</strong> for $\\lambda$ if $(T-\\lambda I)^kv=0$ for some $k\\ge1$. Eigenvectors are the case $k=1$.",
     "<strong>Generalized eigenspace:</strong> $G(\\lambda,T)=\\operatorname{null}(T-\\lambda I)^{\\dim V}$, which contains $E(\\lambda,T)$ and is <strong>invariant under $T$</strong>.",
     "<strong>Why bother:</strong> when eigenvectors are too few to span $V$ (defective $T$), the generalized ones always do: <strong>nothing is lost</strong> over $\\mathbb{C}$."],
    r"$$G(\lambda,T)=\operatorname{null}(T-\lambda I)^{\dim V}\ \supseteq\ E(\lambda,T)=\operatorname{null}(T-\lambda I)$$",
    "A relay chain: one pass might not finish the job (not an eigenvector), but after k handoffs the baton reaches zero.",
    "The exponent needed is at most dim V, so you never need to check beyond null (T−λI)^{dim V}. Using exponent 1 gives only the ordinary eigenspace."))

CARDS.append(card(8, 3, "GENERALIZED EIGENSPACES", "V = ⊕ G(λⱼ, T) over ℂ",
    [R(14, 18, 212, 44, "#ffffff", 1.8), R(14, 18, 70, 44, "#f1f5f9", 1.4), R(84, 18, 90, 44, "#e2e8f0", 1.4), R(174, 18, 52, 44, "#f1f5f9", 1.4),
     N(49, 44, "G(λ₁)", 10, w="bold"), N(129, 44, "G(λ₂)", 10, w="bold"), N(200, 44, "G(λ₃)", 10, w="bold"),
     N(120, 14, "V", 10, w="bold"), N(120, 88, "block diagonal: T = T|_{G(λ₁)} ⊕ T|_{G(λ₂)} ⊕ …", 9, w="bold"),
     N(120, 106, "each block has the single eigenvalue λⱼ", 8.5), N(120, 124, "(T − λⱼ) restricted to G(λⱼ) is nilpotent", 8.5)],
    "Over ℂ the whole space splits into T-invariant generalized eigenspaces, one per eigenvalue",
    ["<strong>Theorem:</strong> for $T$ on a finite-dimensional <strong>complex</strong> space with distinct eigenvalues $\\lambda_1,\\dots,\\lambda_m$: $V=G(\\lambda_1,T)\\oplus\\cdots\\oplus G(\\lambda_m,T)$, each summand $T$-invariant.",
     "<strong>Matrix form:</strong> in a basis adapted to this decomposition, $T$ is <strong>block diagonal</strong>, with block $j$ having the single eigenvalue $\\lambda_j$.",
     "<strong>Structure:</strong> $T|_{G(\\lambda_j)}=\\lambda_jI+N_j$ where $N_j$ is <strong>nilpotent</strong>. So every operator = (scalar) + (nilpotent) on each block: the stepping stone to Jordan form."],
    r"$$V=\bigoplus_{j=1}^{m}G(\lambda_j,T),\qquad T|_{G(\lambda_j)}=\lambda_jI+N_j,\ \ N_j\ \text{nilpotent}$$",
    "Sorting a mixed bag of coins by country: each pile is self-contained (invariant), and within a pile all the 'currencies' share one rate.",
    "Over ℝ the splitting needs all eigenvalues real. Complex eigenvalues come in conjugate pairs and require a different (real) block structure."))

CARDS.append(card(8, 4, "GENERALIZED EIGENSPACES", "dim G(λ) = Algebraic Multiplicity",
    [box(14, 14, 100, 34, "dim G(λ,T)", "#e2e8f0", 10), N(130, 36, "=", 14, "middle", "bold"), box(142, 14, 84, 34, "mult of λ in p_T", "#e2e8f0", 9),
     N(120, 74, "Σⱼ dim G(λⱼ) = dim V", 10, w="bold"), N(120, 92, "Σⱼ (alg multiplicity) = n", 9.5, w="bold"),
     N(120, 112, "also  dim E(λ) ≤ dim G(λ)", 9), N(120, 128, "equal for every λ ⇔ diagonalizable", 8.5)],
    "The size of the generalized eigenspace is the root multiplicity in the characteristic polynomial",
    ["<strong>Theorem:</strong> $\\dim G(\\lambda,T)$ equals the <strong>multiplicity of $\\lambda$ as a root of the characteristic polynomial</strong>.",
     "<strong>Consistency:</strong> since $V=\\bigoplus G(\\lambda_j)$, the algebraic multiplicities sum to $n=\\dim V$, matching the degree of $p_T$.",
     "<strong>Diagonalizability test:</strong> $E(\\lambda)\\subseteq G(\\lambda)$ always; $T$ is diagonalizable iff $E(\\lambda)=G(\\lambda)$ for every $\\lambda$ (geometric = algebraic)."],
    r"$$\dim G(\lambda,T)=\operatorname{mult}_{p_T}(\lambda),\qquad \sum_j\dim G(\lambda_j,T)=\dim V$$",
    "A hotel booked for exactly n guests: the char poly says how many rooms each wing has, and the generalized eigenspaces are those wings.",
    "It is the GENERALIZED eigenspace (not the eigenspace) whose dimension equals algebraic multiplicity. Eigenspace dimension is only a lower bound."))

CARDS.append(card(8, 5, "NILPOTENT OPERATORS", "Nilpotent Chains: v, Nv, …, N^{m−1}v",
    [box(12, 40, 36, 26, "v", "#f1f5f9", 11), L(48, 53, 68, 53, 1.4, ar=True), box(70, 40, 36, 26, "Nv", "#f1f5f9", 10), L(106, 53, 126, 53, 1.4, ar=True),
     box(128, 40, 40, 26, "N²v", "#f1f5f9", 10), L(168, 53, 188, 53, 1.4, ar=True), N(200, 58, "0", 11, "middle", "bold"),
     N(120, 20, "N³ = 0 but N²v ≠ 0  (chain length 3)", 9, w="bold"), N(120, 92, "v, Nv, N²v are a BASIS of a 3-D invariant subspace", 9, w="bold"),
     N(120, 110, "matrix of N in this basis: 1s on the superdiagonal", 8.5), N(120, 128, "= Jordan block J₃(0)", 9, w="bold")],
    "If N^{m−1}v ≠ 0 but N^m v = 0, the m vectors v, Nv, …, N^{m−1}v are independent",
    ["<strong>Chain:</strong> take $v$ with $N^{m-1}v\\ne0$ and $N^mv=0$. Then $v,Nv,\\dots,N^{m-1}v$ is <strong>linearly independent</strong> (apply $N^{m-1}$ to a relation to kill all but the first coefficient).",
     "<strong>Block:</strong> in the reversed basis $N^{m-1}v,\\dots,Nv,v$ the matrix of $N$ is the <strong>Jordan block $J_m(0)$</strong> (ones above the diagonal).",
     "<strong>Theorem preview:</strong> every nilpotent operator has a basis made of such chains: $V$ splits into a direct sum of <strong>cyclic subspaces</strong>."],
    r"$$N^{m-1}v\ne0,\ N^mv=0\ \Rightarrow\ \{v,Nv,\dots,N^{m-1}v\}\ \text{independent};\quad [N]=J_m(0)$$",
    "A row of dominoes: tipping the first one in sequence knocks over exactly m of them, one at a time, and then there is nothing left to fall.",
    "The longest chain is where N^{m−1} ≠ 0; chains can have different lengths in the same space. The number and lengths of chains determine the whole structure."))

CARDS.append(card(8, 6, "WORKED BENCHMARK", "Worked Benchmark: N = shift on ℂ³",
    [GRID(12, 14, [[0, 1, 0], [0, 0, 1], [0, 0, 0]], cell=24, sz=11, shade={(0, 1), (1, 2)}), N(48, 100, "N", 10, w="bold"),
     N(100, 22, "N e₂ = e₁,  N e₃ = e₂,  N e₁ = 0", 8.5, "start"), N(100, 38, "N² e₃ = e₁ ≠ 0,  N³ = 0", 8.5, "start", "bold"),
     N(100, 60, "dim ker N = 1", 9, "start"), N(100, 74, "dim ker N² = 2", 9, "start"), N(100, 88, "dim ker N³ = 3", 9, "start", "bold"),
     N(100, 108, "one chain of length 3", 8.5, "start"), N(100, 122, "single Jordan block J₃(0)", 8.5, "start", "bold"),
     N(12, 128, "kernel grows by 1 each step", 8, "start")],
    "The kernels grow 1, 2, 3 as the power increases: a single chain of length 3",
    ["<strong>Operator:</strong> $N=\\begin{pmatrix}0&1&0\\\\0&0&1\\\\0&0&0\\end{pmatrix}$ sends $e_3\\mapsto e_2\\mapsto e_1\\mapsto0$.",
     "<strong>Powers:</strong> $N^2=E_{13}\\ne0$ and $N^3=0$, so the nilpotency index is $3=\\dim V$ (the maximum possible).",
     "<strong>Kernel sizes:</strong> $\\dim\\ker N=1,\\ \\dim\\ker N^2=2,\\ \\dim\\ker N^3=3$. The increments $1,1,1$ say there is <strong>one chain of length 3</strong>: $N$ is itself the Jordan block $J_3(0)$."],
    r"$$N^2=\begin{pmatrix}0&0&1\\0&0&0\\0&0&0\end{pmatrix}\ne0,\quad N^3=0,\quad (\dim\ker N^k)_{k=1,2,3}=(1,2,3)$$",
    "A single three-link chain: pull the last link and you move all three, yet only the first link can ever be 'free' (killed at once).",
    "A nilpotent matrix of index n has exactly ONE chain. Two chains of shorter length (e.g. 2 + 1) also give N³ = 0 but different kernel dimensions."))

# ====================== 09 · JORDAN FORM ======================
CARDS.append(card(9, 1, "JORDAN FORM", "The Jordan Block J_k(λ)",
    [GRID(20, 14, [["λ", "1", "0", "0"], ["0", "λ", "1", "0"], ["0", "0", "λ", "1"], ["0", "0", "0", "λ"]], cell=26, sz=11, shade={(i, i) for i in range(4)}),
     N(72, 126, "J₄(λ) = λI + N", 10, w="bold"), N(150, 28, "λ on the diagonal", 9, "start", "bold"), N(150, 46, "1s just above it", 9, "start", "bold"),
     N(150, 68, "one eigenvector: e₁", 8.5, "start"), N(150, 80, "geo = 1, alg = 4", 8.5, "start"), N(150, 98, "(J−λ)⁴ = 0, (J−λ)³ ≠ 0", 8, "start"),
     N(150, 114, "min poly (z−λ)⁴", 8.5, "start")],
    "A single chain: the eigenvalue λ along the diagonal with 1s on the superdiagonal",
    ["<strong>Block:</strong> $J_k(\\lambda)=\\lambda I_k+N_k$ where $N_k$ has ones on the superdiagonal. It has the single eigenvalue $\\lambda$ with <strong>algebraic multiplicity $k$</strong>.",
     "<strong>Only one eigenvector</strong> ($e_1$): $\\dim\\ker(J_k(\\lambda)-\\lambda I)=1$, so the block is as far from diagonalizable as possible. Powers: $(J-\\lambda I)^j=N_k^j$.",
     "<strong>Minimal polynomial</strong> of the block is $(z-\\lambda)^k$, the largest possible for size $k$."],
    r"$$J_k(\lambda)=\lambda I_k+N_k,\qquad (J_k(\lambda)-\lambda I)^{k}=0,\quad (J_k(\lambda)-\lambda I)^{k-1}\ne0$$",
    "A single conveyor belt of k stations: the item can only enter at the first station and every later stage waits on the one before it.",
    "Jordan blocks put the 1s ABOVE the diagonal in the standard (Axler/Horn–Johnson) convention. Some texts use below. Match your course's convention."))

CARDS.append(card(9, 2, "JORDAN FORM", "The Jordan Canonical Form Theorem",
    [GRID(14, 14, [["J", "", "", ""], ["", "J", "", ""], ["", "", "J", ""], ["", "", "", "J"]], cell=24, sz=11),
     N(62, 118, "block diagonal of Jordan blocks", 8.5, w="bold"), N(118, 24, "Every complex operator", 8.5, "start", "bold"), N(118, 38, "has a basis giving a", 8.5, "start", "bold"),
     N(118, 52, "sum of Jordan blocks", 8.5, "start", "bold"), N(118, 74, "unique up to the", 8.5, "start"), N(118, 86, "order of the blocks", 8.5, "start"),
     N(118, 108, "A = P J P⁻¹", 11, "start", "bold"), N(118, 124, "similar ⇔ same Jordan form", 8.5, "start")],
    "Every complex matrix is similar to a block-diagonal matrix of Jordan blocks, uniquely up to block order",
    ["<strong>Theorem:</strong> if $V$ is a finite-dimensional complex space and $T\\in\\mathcal{L}(V)$, there is a basis in which the matrix of $T$ is <strong>block diagonal with Jordan blocks</strong> $J_{k}(\\lambda)$ on the diagonal.",
     "<strong>Uniqueness:</strong> the multiset of pairs $(\\lambda,k)$ is determined by $T$ (up to permuting blocks). Two matrices are <strong>similar iff they have the same Jordan form</strong>.",
     "<strong>Special cases:</strong> all blocks of size $1$ $\\iff$ diagonalizable; a single eigenvalue and one block $\\iff$ $T-\\lambda I$ is nilpotent of full index."],
    r"$$A=PJP^{-1},\qquad J=\operatorname{diag}\big(J_{k_1}(\lambda_1),\dots,J_{k_r}(\lambda_r)\big)$$",
    "The periodic table of operators: every operator is a combination of elements (blocks), and the list of elements identifies it completely.",
    "Jordan form is over ℂ (or any algebraically closed field); a real matrix may need complex eigenvalues. Also computing the transition matrix P is much harder than finding J."))

CARDS.append(card(9, 3, "JORDAN FORM", "Counting Blocks from Kernel Dimensions",
    [L(20, 108, 220, 108, 1.2)] + [R(34, 108 - 40, 28, 40, "#f1f5f9", 1.4), R(90, 108 - 60, 28, 60, "#f1f5f9", 1.4), R(146, 108 - 70, 28, 70, "#f1f5f9", 1.4), R(190, 108 - 70, 28, 70, "#f1f5f9", 1.4),
     N(48, 122, "k=1", 8.5), N(104, 122, "k=2", 8.5), N(160, 122, "k=3", 8.5), N(204, 122, "k=4", 8.5),
     N(48, 56, "2", 9, w="bold"), N(104, 36, "3", 9, w="bold"), N(160, 26, "4", 9, w="bold"), N(204, 26, "4", 9, w="bold"),
     N(120, 14, "dim ker (A − λI)^k", 9, w="bold"), N(120, 138, "increments 2,1,1,0 ⇒ blocks ≥1: 2, ≥2: 1, ≥3: 1", 8.5, w="bold")],
    "The increments of dim ker (A − λI)^k reveal how many blocks have size at least k",
    ["<strong>Number of blocks</strong> for $\\lambda$ $=\\dim\\ker(A-\\lambda I)$ (one eigenvector per block).",
     "<strong>Number of blocks of size $\\ge k$</strong> $=\\dim\\ker(A-\\lambda I)^k-\\dim\\ker(A-\\lambda I)^{k-1}$. The increments are non-increasing; differences of increments count blocks of <strong>exact</strong> size.",
     "<strong>Procedure:</strong> compute the kernel dimensions of $(A-\\lambda I)^k$ until they reach the algebraic multiplicity, then read off the block sizes."],
    r"$$\#\{\text{blocks of size}\ge k\}=\dim\ker(A-\lambda I)^k-\dim\ker(A-\lambda I)^{k-1}$$",
    "Counting how many stacks of cups reach height k by checking, layer by layer, how many are still standing.",
    "The increments count blocks of size AT LEAST k, not exactly k. Exactly-k = (increment at k) − (increment at k+1)."))

CARDS.append(card(9, 4, "JORDAN FORM", "Minimal Polynomial from Jordan Form",
    [GRID(14, 14, [["2", "1", "", ""], ["", "2", "", ""], ["", "", "2", ""], ["", "", "", "3"]], cell=24, sz=11),
     N(62, 118, "J₂(2) ⊕ J₁(2) ⊕ J₁(3)", 8.5, w="bold"), N(150, 26, "exponent of (z − λ) =", 8.5, "start", "bold"), N(150, 40, "size of the LARGEST", 8.5, "start", "bold"), N(150, 54, "block for λ", 8.5, "start", "bold"),
     N(150, 78, "q(z) = (z−2)²(z−3)", 10, "start", "bold"), N(150, 98, "p_A(z) = (z−2)³(z−3)", 9.5, "start"), N(150, 118, "alg mult = SUM of block sizes", 8.5, "start")],
    "Characteristic polynomial multiplies all blocks; minimal polynomial keeps only the biggest block per eigenvalue",
    ["<strong>Char poly:</strong> the exponent of $(z-\\lambda)$ is the <strong>sum</strong> of the sizes of all blocks with eigenvalue $\\lambda$ (algebraic multiplicity).",
     "<strong>Min poly:</strong> the exponent of $(z-\\lambda)$ is the <strong>size of the largest</strong> block for $\\lambda$, since $(J_k(\\lambda)-\\lambda)^m=0$ iff $m\\ge k$.",
     "<strong>So:</strong> the Jordan structure tells you at once whether $A$ is diagonalizable (all exponents $1$) and what $q(A)=0$ requires."],
    r"$$p_A(z)=\prod_\lambda(z-\lambda)^{\sum k_i(\lambda)},\qquad q_A(z)=\prod_\lambda(z-\lambda)^{\max_i k_i(\lambda)}$$",
    "A rope made of segments: the total length (char poly) is the sum of segments; the longest straight stretch (min poly) is the longest segment.",
    "Same characteristic AND minimal polynomial do not always mean similar: with an eigenvalue of multiplicity 6, blocks 3+3 and 3+2+1 both have min poly (z−λ)³. Compare the kernel dimensions."))

CARDS.append(card(9, 5, "MATRIX FUNCTIONS", "f(J) and e^{tJ}",
    [GRID(14, 14, [["e^λ", "e^λ", "e^λ/2"], ["", "e^λ", "e^λ"], ["", "", "e^λ"]], cell=34, sz=9),
     N(62, 126, "e^{J₃(λ)} = e^λ (I + N + N²/2)", 8.5, w="bold"),
     N(160, 28, "f(J_k(λ)) =", 9, "start", "bold"), N(160, 42, "Σ_j f^{(j)}(λ)/j! · N^j", 8.5, "start"),
     N(160, 64, "finite sum: N^k = 0", 8.5, "start"), N(160, 84, "A = PJP⁻¹ ⇒", 9, "start"), N(160, 98, "f(A) = P f(J) P⁻¹", 9, "start", "bold"),
     N(160, 118, "e^{tA} solves x′ = Ax", 8.5, "start")],
    "For a Jordan block, f(J) is a finite Taylor sum because N^k = 0",
    ["<strong>Block formula:</strong> $J=\\lambda I+N$ with $N^k=0$, so $f(J)=\\sum_{j=0}^{k-1}\\frac{f^{(j)}(\\lambda)}{j!}N^j$. Example: $e^{tJ}=e^{\\lambda t}\\left(I+tN+\\tfrac{t^2}{2}N^2+\\dots\\right)$.",
     "<strong>General matrix:</strong> if $A=PJP^{-1}$ then $f(A)=Pf(J)P^{-1}$, with $f$ applied blockwise (diagonal case: just $f(\\lambda_i)$ on the diagonal).",
     "<strong>Applications:</strong> $e^{tA}$ solves $x'=Ax$; polynomial growth $t^{k-1}e^{\\lambda t}$ appears exactly when there is a <strong>Jordan block of size $k$</strong> (resonance); $A^m$ has entries like $\\binom{m}{j}\\lambda^{m-j}$."],
    r"$$f(J_k(\lambda))=\sum_{j=0}^{k-1}\frac{f^{(j)}(\lambda)}{j!}N^{j},\qquad e^{tA}=P\,e^{tJ}P^{-1}$$",
    "Applying a rule to a machine by reading off the rule's value and its first few slopes: the nilpotent part only needs finitely many derivatives.",
    "For a non-diagonalizable A, f(A) needs the DERIVATIVES of f at the eigenvalues, not just f(λ). Using only f(λ) on the diagonal is wrong."))

CARDS.append(card(9, 6, "WORKED BENCHMARK", "Worked Benchmark: Reading Jordan Form from Kernel Dimensions",
    [N(120, 18, "λ = 2 has algebraic multiplicity 4", 9.5, w="bold"),
     N(14, 40, "dim ker(A−2I)   = 2", 9.5, "start"), N(14, 58, "dim ker(A−2I)²  = 3", 9.5, "start"), N(14, 76, "dim ker(A−2I)³  = 4", 9.5, "start", "bold"),
     N(14, 98, "increments: 2, 1, 1", 9, "start", "bold"),
     N(130, 40, "#blocks            = 2", 9, "start"), N(130, 56, "#blocks size ≥ 2 = 1", 9, "start"), N(130, 72, "#blocks size ≥ 3 = 1", 9, "start"),
     N(130, 94, "sizes: 3 and 1", 10, "start", "bold"), N(130, 112, "J = J₃(2) ⊕ J₁(2)", 10, "start", "bold"), N(130, 128, "q(z) = (z − 2)³", 9, "start")],
    "Kernel dimensions 2, 3, 4 mean one block of size 3 and one of size 1",
    ["<strong>Given:</strong> eigenvalue $2$ with algebraic multiplicity $4$, and $\\dim\\ker(A-2I)=2$, $\\dim\\ker(A-2I)^2=3$, $\\dim\\ker(A-2I)^3=4$.",
     "<strong>Increments:</strong> $2,1,1$. So there are $2$ blocks in total, $1$ block of size $\\ge2$, and $1$ block of size $\\ge3$. Hence the sizes are <strong>3 and 1</strong> (sum $=4$ ✓).",
     "<strong>Result:</strong> $J=J_3(2)\\oplus J_1(2)$, minimal polynomial $(z-2)^3$, and $A$ is not diagonalizable (largest block 3)."],
    r"$$J=J_3(2)\oplus J_1(2)=\begin{pmatrix}2&1&0&0\\0&2&1&0\\0&0&2&0\\0&0&0&2\end{pmatrix},\quad q_A=(z-2)^3$$",
    "Reading a stack of coins by weighing: heavier increments show tall stacks, and the number of times the weight increases tells you how many stacks reach each height.",
    "Check the total: the block sizes must add up to the algebraic multiplicity (3 + 1 = 4). If your sizes don't sum correctly, you miscounted an increment."))
