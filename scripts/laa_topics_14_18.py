import math
from subj_lib import *

card = make_card("LAA")
CARDS = []

def V(x0, y0, x1, y1, w=2.2, d=None):
    return L(x0, y0, x1, y1, w, d=d, ar=True)

# ====================== 14 · POSITIVE OPERATORS & ISOMETRIES ======================
CARDS.append(card(14, 1, "POSITIVE OPERATORS", "Positive Operators: ⟨Tv, v⟩ ≥ 0",
    [box(10, 14, 220, 28, "T positive  ⇔  T = T*  and  ⟨Tv, v⟩ ≥ 0 for all v", "#e2e8f0", 8.5),
     N(120, 62, "equivalent:", 9, w="bold"), N(120, 78, "all eigenvalues of T are ≥ 0", 9.5),
     N(120, 94, "T = S*S for some S", 9.5), N(120, 110, "T = R² for a positive R", 9.5),
     N(120, 130, "positive definite: ⟨Tv,v⟩ > 0 for v ≠ 0 ⇔ λ > 0", 8.5, w="bold")],
    "A positive operator never turns a vector against itself: the quadratic form is never negative",
    ["<strong>Definition:</strong> $T$ is <strong>positive</strong> ($T\\succeq0$) if $T=T^*$ and $\\langle Tv,v\\rangle\\ge0$ for all $v$. It is <strong>positive definite</strong> if the inequality is strict for $v\\ne0$.",
     "<strong>Equivalent forms:</strong> all eigenvalues $\\ge0$; $T=S^*S$ for some $S$; $T=R^2$ for some positive $R$. The matrix $A^*A$ is <strong>always positive</strong> (since $\\langle A^*Av,v\\rangle=\\|Av\\|^2$).",
     "<strong>Geometry:</strong> positive operators stretch along perpendicular axes by non-negative factors and never reflect: they are the operator analogue of non-negative real numbers."],
    r"$$T\succeq0\iff T=T^*,\ \operatorname{spec}(T)\subseteq[0,\infty)\iff T=S^*S,\qquad \langle S^*Sv,v\rangle=\|Sv\|^2\ge0$$",
    "Stretching a rubber sheet without any flipping: every direction is lengthened (or flattened) but never turned inside out.",
    "Positive requires SELF-ADJOINT first. ⟨Tv,v⟩ ≥ 0 for all v over ℂ implies it, but over ℝ a non-symmetric matrix can have ⟨Tv,v⟩ ≥ 0 without being positive."))

CARDS.append(card(14, 2, "POSITIVE OPERATORS", "The Unique Positive Square Root",
    [N(30, 28, "T = Σ λⱼ Pⱼ,  λⱼ ≥ 0", 9.5, "start", "bold"), L(60, 36, 60, 50, 1.4, ar=True), N(30, 66, "√T = Σ √λⱼ Pⱼ", 10.5, "start", "bold"),
     L(30, 82, 210, 82, 0.9), N(120, 100, "(√T)² = T,   √T positive", 9.5, w="bold"),
     N(120, 116, "unique among positive operators", 8.5), N(120, 132, "(many non-positive R with R² = T exist)", 8)],
    "Take the square root of each eigenvalue on the same eigenspaces",
    ["<strong>Existence:</strong> if $T\\succeq0$ with spectral decomposition $T=\\sum\\lambda_jP_j$, define $\\sqrt T=\\sum\\sqrt{\\lambda_j}\\,P_j$. Then $(\\sqrt T)^2=T$ and $\\sqrt T$ is positive.",
     "<strong>Uniqueness:</strong> there is exactly <strong>one positive</strong> $R$ with $R^2=T$. (E.g. $I$ also equals $(-I)^2$, but $-I$ is not positive.)",
     "<strong>Use:</strong> $\\sqrt{T^*T}$ is the 'absolute value' $|T|$, central to the <strong>polar decomposition</strong> and singular values."],
    r"$$T\succeq0\Rightarrow\sqrt T=\sum_j\sqrt{\lambda_j}P_j\ \text{ unique positive with }(\sqrt T)^2=T,\qquad |T|:=\sqrt{T^*T}$$",
    "Halving a recipe along each independent axis: every ingredient is rescaled by its own square root and the proportions stay aligned.",
    "A positive matrix has MANY square roots (±signs on eigenvalues) but only ONE positive square root. Say 'the positive square root'."))

CARDS.append(card(14, 3, "ISOMETRIES", "Isometries: ‖Sv‖ = ‖v‖",
    [C(70, 72, 40, "#f1f5f9", 1.8), V(70, 72, 98, 44, 2.2), L(110, 72, 130, 72, 1.5, ar=True), N(120, 64, "S", 10, "middle", "bold"),
     C(180, 72, 40, "#f1f5f9", 1.8), V(180, 72, 160, 36, 2.2), N(70, 126, "unit ball", 8.5), N(180, 126, "same unit ball", 8.5),
     N(120, 18, "S*S = I   ⇔   ‖Sv‖ = ‖v‖   ⇔   ⟨Su,Sv⟩ = ⟨u,v⟩", 8.5, w="bold")],
    "Isometries rigidly move space: lengths and angles are all preserved",
    ["<strong>Definition:</strong> $S\\in\\mathcal{L}(V,W)$ is an <strong>isometry</strong> if $\\|Sv\\|=\\|v\\|$ for all $v$. Equivalent: $S^*S=I$ (columns orthonormal), and $\\langle Su,Sv\\rangle=\\langle u,v\\rangle$ (preserves angles too).",
     "<strong>Consequences:</strong> an isometry is <strong>injective</strong>; it maps orthonormal lists to orthonormal lists; its eigenvalues have $|\\lambda|=1$.",
     "<strong>Square case:</strong> for an operator on a finite-dimensional space, isometry $\\iff$ <strong>unitary</strong> (real: <strong>orthogonal</strong>): $S^*S=SS^*=I$, $S^{-1}=S^*$."],
    r"$$S^*S=I\iff\|Sv\|=\|v\|\ \forall v\iff\langle Su,Sv\rangle=\langle u,v\rangle$$",
    "Moving a rigid object across a table: rotating or reflecting it never changes any distance or angle on it.",
    "A tall matrix with orthonormal columns is an isometry (Q*Q = I) but NOT unitary (QQ* ≠ I). Square + isometry is what makes it unitary."))

CARDS.append(card(14, 4, "ISOMETRIES", "Unitary and Orthogonal Matrices",
    [C(120, 72, 46, "none", 1.4), L(30, 72, 214, 72, 0.7, d="2 3"), L(120, 20, 120, 124, 0.7, d="2 3"),
     C(166, 72, 3.5), C(120, 26, 3.5), C(87, 105, 3.5), C(87, 39, 3.5),
     N(176, 62, "|λ| = 1", 9.5, "start", "bold"), N(120, 138, "eigenvalues lie ON the unit circle", 8.5, w="bold"),
     N(16, 24, "U*U = I", 10, "start", "bold"), N(16, 38, "|det U| = 1", 9, "start"), N(16, 52, "rows, cols orthonormal", 8.5, "start"), N(16, 66, "‖U‖₂ = 1, κ = 1", 8.5, "start")],
    "All eigenvalues of a unitary matrix sit on the unit circle in the complex plane",
    ["<strong>Definition:</strong> $U^*U=UU^*=I$ (complex) or $Q^TQ=QQ^T=I$ (real). Columns and rows each form an <strong>orthonormal basis</strong>.",
     "<strong>Invariants:</strong> $|\\det U|=1$ (real: $\\det Q=\\pm1$: rotations have $+1$, reflections $-1$), $\\|U\\|_2=1$ and condition number $1$ (numerically perfect).",
     "<strong>Spectrum:</strong> $|\\lambda|=1$. Unitary operators are <strong>normal</strong>, so $U=VDV^*$ with $D$ on the unit circle; a real orthogonal matrix is a mix of $2\\times2$ rotations and $\\pm1$."],
    r"$$U^*U=UU^*=I,\quad |\lambda|=1,\quad |\det U|=1,\quad \kappa_2(U)=1$$",
    "Rotating a globe: positions move around but the shape and all distances stay exactly the same.",
    "Orthogonal matrices have det ±1, not necessarily +1. det = −1 means a reflection (orientation reversal); only det = +1 is a pure rotation."))

CARDS.append(card(14, 5, "WORKED BENCHMARK", "Worked Benchmark: A = [[2,−1],[−1,2]]",
    [GRID(12, 14, [[2, -1], [-1, 2]], cell=28, sz=12), N(40, 84, "A", 10, w="bold"),
     N(86, 24, "tr = 4, det = 3 ⇒ λ = 3, 1", 8.5, "start", "bold"), N(86, 40, "both > 0 ⇒ positive definite", 8.5, "start", "bold"),
     N(86, 56, "λ=3: (1,−1)/√2     λ=1: (1,1)/√2", 8, "start"),
     N(14, 104, "√A = √3 P₍₃₎ + 1·P₍₁₎", 9, "start", "bold"), N(14, 118, "     = ½[[√3+1, 1−√3],[1−√3, √3+1]]", 8, "start"),
     N(14, 134, "check: (√A)² = A ✓", 8.5, "start", "bold"),
     N(130, 86, "⟨Av,v⟩ = 2x²−2xy+2y²", 8.5, "start"), N(130, 100, "= x² + y² + (x−y)² > 0", 8.5, "start", "bold")],
    "Eigenvalues 3 and 1 are positive, so A is positive definite with a positive square root",
    ["<strong>Eigenvalues:</strong> $\\operatorname{tr}A=4$, $\\det A=3$, so $\\lambda=3,1$ (both $>0$) $\\Rightarrow$ <strong>positive definite</strong>. Also directly: $\\langle Av,v\\rangle=2x^2-2xy+2y^2=x^2+y^2+(x-y)^2>0$.",
     "<strong>Eigenvectors:</strong> $\\lambda=3$ for $(1,-1)/\\sqrt2$, $\\lambda=1$ for $(1,1)/\\sqrt2$ (orthogonal, as for any symmetric matrix).",
     "<strong>Square root:</strong> $\\sqrt A=\\sqrt3P_3+P_1=\\tfrac12\\begin{pmatrix}\\sqrt3+1&1-\\sqrt3\\\\1-\\sqrt3&\\sqrt3+1\\end{pmatrix}$, and squaring gives back $A$ (diagonal entries $\\tfrac{(\\sqrt3+1)^2+(\\sqrt3-1)^2}{4}=2$ ✓)."],
    r"$$\sqrt A=\sqrt3\,P_{(1,-1)}+1\cdot P_{(1,1)},\qquad (\sqrt A)^2=A$$",
    "A springy mattress: pressing down in any direction pushes back (positive); the springs just have different strengths along two perpendicular axes.",
    "Check the TOP-LEFT minors too for a quick test: 2 > 0 and det = 3 > 0 (Sylvester's criterion) confirm positive definiteness without eigenvalues."))

# ====================== 15 · POLAR & SVD ======================
CARDS.append(card(15, 1, "POLAR DECOMPOSITION", "Polar Decomposition: T = S √(T*T)",
    [C(48, 72, 30, "#ffffff", 1.6), L(52, 72, 84, 72, 1.5, ar=True), N(68, 64, "√(T*T)", 8.5, "middle", "bold"),
     E(120, 72, 38, 20, 0, "#f1f5f9", 1.8), L(158, 72, 184, 72, 1.5, ar=True), N(172, 64, "S", 10, "middle", "bold"),
     E(214, 70, 24, 14, -35, "#f1f5f9", 1.8), N(48, 116, "unit disk", 8.5), N(120, 116, "stretch (positive)", 8.5), N(214, 116, "rotate/reflect", 8.5),
     N(120, 18, "T = S |T|     (like z = e^{iθ} |z|)", 10, w="bold"), N(120, 134, "S isometry, |T| = √(T*T) ≥ 0", 8.5)],
    "Every operator is a stretch along perpendicular axes followed by a rotation/reflection",
    ["<strong>Theorem:</strong> every $T\\in\\mathcal{L}(V)$ can be written $T=S\\sqrt{T^*T}$ where $S$ is an <strong>isometry</strong> and $\\sqrt{T^*T}=|T|$ is <strong>positive</strong>.",
     "<strong>Idea:</strong> $\\|Tv\\|=\\|\\sqrt{T^*T}\\,v\\|$ (since $T^*T=(\\sqrt{T^*T})^2$), so $S$ is defined by $S(\\sqrt{T^*T}v)=Tv$; it preserves lengths on the range of $|T|$ and is extended as an isometry.",
     "<strong>Analogy:</strong> a complex number $z=e^{i\\theta}|z|$ is a magnitude (positive) times a phase; here the 'phase' is a unitary and the 'magnitude' is a positive operator."],
    r"$$T=S\sqrt{T^*T},\quad S\ \text{isometry},\quad |T|=\sqrt{T^*T}\succeq0$$",
    "Moving a piece of dough: first stretch it along two perpendicular axes, then rotate or flip the result.",
    "S is unique only when T is invertible. For singular T the isometry part is not unique on the null space (the 'phase' of a zero stretch is arbitrary)."))

def _svg_geom():
    return [C(50, 72, 30, "#ffffff", 1.6), V(50, 72, 80, 72, 1.8), V(50, 72, 50, 42, 1.8), N(50, 118, "unit circle", 8.5),
            L(86, 72, 108, 72, 1.5, ar=True), N(97, 64, "A=UΣV*", 8, "middle", "bold"),
            E(160, 72, 50, 22, -30, "#f1f5f9", 1.8), V(160, 72, 196, 42, 2.4), V(160, 72, 146, 90, 2.0),
            N(200, 36, "σ₁u₁", 9, "start", "bold"), N(146, 100, "σ₂u₂", 9, "end", "bold"), N(160, 126, "image = ellipse", 8.5)]

CARDS.append(card(15, 2, "SVD", "SVD: Circle → Ellipse",
    _svg_geom(),
    "A maps the unit sphere to an ellipsoid whose semi-axes are σⱼ uⱼ",
    ["<strong>Theorem:</strong> every $A\\in\\mathbb{C}^{m\\times n}$ factors as $A=U\\Sigma V^*$ with $U,V$ <strong>unitary</strong> and $\\Sigma$ diagonal, with <strong>singular values</strong> $\\sigma_1\\ge\\sigma_2\\ge\\dots\\ge0$.",
     "<strong>Geometry:</strong> $V^*$ rotates the input; $\\Sigma$ stretches the axes by $\\sigma_j$; $U$ rotates into the output. So the unit sphere becomes an <strong>ellipsoid with semi-axes $\\sigma_ju_j$</strong>.",
     "<strong>Action form:</strong> $Av=\\sum_j\\sigma_j\\langle v,v_j\\rangle u_j$. Works for <strong>every</strong> matrix: rectangular, singular, non-normal."],
    r"$$A=U\Sigma V^*=\sum_{j=1}^{r}\sigma_j\,u_jv_j^*,\qquad \sigma_j=\sqrt{\lambda_j(A^*A)}\ge0$$",
    "Any machine, however twisted, secretly just rotates, stretches along perpendicular axes, then rotates again.",
    "Singular values are the square roots of eigenvalues of A*A; they are NOT the eigenvalues of A (those can be complex or smaller)."))

CARDS.append(card(15, 3, "SVD", "Computing the SVD from A*A",
    [box(10, 14, 100, 28, "A*A = V Λ V*", "#f1f5f9", 9.5), L(110, 28, 128, 28, 1.4, ar=True), box(130, 14, 100, 28, "σⱼ = √λⱼ,  vⱼ", "#f1f5f9", 9.5),
     L(180, 42, 180, 58, 1.4, ar=True), box(130, 60, 100, 28, "uⱼ = A vⱼ / σⱼ", "#e2e8f0", 9.5),
     N(60, 74, "right singular vectors", 8.5, w="bold"), N(60, 88, "= eigenvectors of A*A", 8.5),
     N(120, 112, "rank A = # of nonzero σⱼ", 9, w="bold"), N(120, 128, "(complete u's for σ=0 columns using an orthonormal basis)", 8)],
    "Eigendecompose A*A, take square roots, and push the right vectors through A",
    ["<strong>Recipe:</strong> (1) diagonalize the positive matrix $A^*A=V\\Lambda V^*$; (2) $\\sigma_j=\\sqrt{\\lambda_j}$; (3) $u_j=Av_j/\\sigma_j$ for $\\sigma_j>0$; (4) complete $U$ to an orthonormal basis.",
     "<strong>Why it works:</strong> $\\langle u_i,u_j\\rangle=\\frac{\\langle Av_i,Av_j\\rangle}{\\sigma_i\\sigma_j}=\\frac{\\langle A^*Av_i,v_j\\rangle}{\\sigma_i\\sigma_j}=\\delta_{ij}$, so the $u_j$ are automatically orthonormal.",
     "<strong>Facts:</strong> $\\operatorname{rank}A=\\#\\{\\sigma_j>0\\}$; $A^*A$ and $AA^*$ share nonzero eigenvalues; $v_j$ (for $\\sigma_j=0$) span $\\operatorname{null}A$."],
    r"$$A^*A\,v_j=\sigma_j^2v_j,\qquad u_j=\frac{Av_j}{\sigma_j},\qquad A=\sum_{j}\sigma_ju_jv_j^*$$",
    "Reading a machine's behavior by testing it on its own 'natural' input directions, then recording how strongly each is amplified.",
    "Keep the pairing: u_j goes with v_j. Sorting the σ's but not their vectors gives a wrong A. Signs of (u_j, v_j) can flip together, never separately."))

CARDS.append(card(15, 4, "LOW-RANK APPROXIMATION", "Eckart–Young: Best Rank-k Approximation",
    [L(20, 108, 214, 108, 1.2)] + [R(30 + i * 26, 108 - h, 18, h, "#e2e8f0" if i < 3 else "#ffffff", 1.4, 0, None if i < 3 else "3 2") for i, h in enumerate([78, 54, 34, 20, 12, 7, 4])] +
    [N(39 + i * 26, 120, f"σ{i+1}", 8) for i in range(7)] + [L(110, 14, 110, 108, 1.2, d="4 3"), N(100, 18, "keep k = 3", 8.5, "end", "bold"), N(120, 18, "discard", 8.5, "start"),
     N(120, 136, "A_k = Σ_{j≤k} σⱼ uⱼ vⱼ*     ‖A − A_k‖₂ = σ_{k+1}", 8.5, w="bold")],
    "Keep the biggest singular values: no rank-k matrix is closer to A",
    ["<strong>Truncated SVD:</strong> $A_k=\\sum_{j\\le k}\\sigma_ju_jv_j^*$ keeps the $k$ largest components. It has rank $k$.",
     "<strong>Eckart–Young–Mirsky:</strong> $A_k$ is the <strong>best</strong> rank-$k$ approximation: $\\|A-A_k\\|_2=\\sigma_{k+1}$ (smallest possible) and $\\|A-A_k\\|_F^2=\\sum_{j>k}\\sigma_j^2$.",
     "<strong>Applications:</strong> image compression, PCA (principal components are the $v_j$), noise reduction, latent semantic analysis, recommender systems."],
    r"$$\min_{\operatorname{rank}B\le k}\|A-B\|_2=\sigma_{k+1},\qquad \min_{\operatorname{rank}B\le k}\|A-B\|_F=\sqrt{\sum_{j>k}\sigma_j^2}$$",
    "Keeping the loudest k instruments of an orchestra: the sound that remains is as close to the original as k instruments can get.",
    "Best approximation is in the 2-norm AND the Frobenius norm. The decay of the σ's tells you how compressible A is, not its rank alone."))

CARDS.append(card(15, 5, "SVD", "Norms, Rank & Conditioning from Singular Values",
    [box(10, 14, 108, 28, "‖A‖₂ = σ₁ (max stretch)", "#f1f5f9", 9), box(122, 14, 108, 28, "‖A‖_F = √Σσⱼ²", "#f1f5f9", 9),
     box(10, 52, 108, 28, "rank = #{σⱼ > 0}", "#f1f5f9", 9), box(122, 52, 108, 28, "|det A| = Πσⱼ", "#f1f5f9", 9),
     box(10, 90, 108, 28, "κ(A) = σ₁/σ_min", "#e2e8f0", 9), box(122, 90, 108, 28, "‖A⁻¹‖₂ = 1/σ_min", "#f1f5f9", 9),
     N(120, 136, "large κ ⇒ small input errors blow up in the solution", 8.5, w="bold")],
    "One set of numbers answers: how big, what rank, how invertible, how sensitive",
    ["<strong>Norms:</strong> the operator 2-norm is the <strong>largest singular value</strong> $\\sigma_1$; the Frobenius norm is $\\sqrt{\\sum\\sigma_j^2}=\\sqrt{\\operatorname{tr}A^*A}$.",
     "<strong>Rank/determinant:</strong> $\\operatorname{rank}A=$ number of nonzero $\\sigma_j$; for square $A$, $|\\det A|=\\prod\\sigma_j$.",
     "<strong>Conditioning:</strong> $\\kappa_2(A)=\\sigma_1/\\sigma_n$. Solving $Ax=b$ with relative error $\\delta$ in $b$ can produce relative error up to $\\kappa\\delta$ in $x$; $\\kappa=1$ exactly for unitary matrices."],
    r"$$\|A\|_2=\sigma_1,\quad \|A\|_F^2=\sum\sigma_j^2,\quad |\det A|=\prod\sigma_j,\quad \kappa_2(A)=\frac{\sigma_1}{\sigma_n}$$",
    "A measuring stick for a machine: the ratio of its strongest stretch to its weakest squeeze says how fragile solving with it will be.",
    "Singular values ≠ eigenvalues. For a non-normal matrix, ‖A‖₂ can be much larger than the biggest |eigenvalue|."))

CARDS.append(card(15, 6, "WORKED BENCHMARK", "Worked Benchmark: SVD of A = [[3,0],[4,5]]",
    [GRID(10, 14, [[3, 0], [4, 5]], cell=26, sz=12), N(36, 80, "A", 10, w="bold"),
     N(76, 24, "AᵀA = [[25,20],[20,25]]", 8.5, "start", "bold"), N(76, 40, "λ = 45, 5  (tr 50, det 225)", 8.5, "start"),
     N(76, 58, "σ₁ = √45 = 3√5 ≈ 6.71", 9, "start", "bold"), N(76, 74, "σ₂ = √5 ≈ 2.24", 9, "start", "bold"),
     N(14, 98, "check: σ₁σ₂ = 15 = |det A| ✓", 9, "start", "bold"),
     N(14, 114, "σ₁² + σ₂² = 50 = ‖A‖_F² = 9+16+25 ✓", 8.5, "start"),
     N(14, 130, "κ = 3 (= σ₁/σ₂)", 8.5, "start"), N(150, 100, "v₁ = (1,1)/√2", 8.5, "start"), N(150, 114, "v₂ = (1,−1)/√2", 8.5, "start")],
    "σ₁ = 3√5, σ₂ = √5; their product is |det| = 15 and the squares add up to the Frobenius norm squared",
    ["<strong>Step 1:</strong> $A^TA=\\begin{pmatrix}25&20\\\\20&25\\end{pmatrix}$ with eigenvalues $45$ and $5$ (trace $50$, determinant $25\\cdot25-20\\cdot20=225=45\\cdot5$ ✓).",
     "<strong>Singular values:</strong> $\\sigma_1=\\sqrt{45}=3\\sqrt5\\approx6.71$, $\\sigma_2=\\sqrt5\\approx2.24$. Right vectors: $v_1=(1,1)/\\sqrt2$, $v_2=(1,-1)/\\sqrt2$; then $u_j=Av_j/\\sigma_j$.",
     "<strong>Checks:</strong> $\\sigma_1\\sigma_2=15=|\\det A|$ ✓ and $\\sigma_1^2+\\sigma_2^2=50=\\|A\\|_F^2=9+0+16+25$ ✓. Condition number $\\kappa=\\sigma_1/\\sigma_2=3$."],
    r"$$\sigma_1=\sqrt{45}=3\sqrt5,\ \ \sigma_2=\sqrt5;\qquad \sigma_1\sigma_2=15=|\det A|,\ \ \sigma_1^2+\sigma_2^2=50=\|A\|_F^2$$",
    "Pressing a disk of dough through the matrix: it comes out as an ellipse whose long axis is 3√5 and short axis √5.",
    "Eigenvalues of A are 3 and 5 (triangular matrix), nothing like the singular values 6.71 and 2.24. A is not normal, so the two sets differ."))

# ====================== 16 · PSEUDOINVERSE & LEAST SQUARES ======================
def _lsq():
    return [L(20, 110, 214, 110, 0.8, d="2 3"), PG("30,112 150,112 200,62 80,62", "#f1f5f9", 1.6), N(70, 104, "col(A)", 10, "middle", "bold"),
            C(150, 24, 4, "#ffffff"), N(156, 22, "b", 10, "start", "bold"), L(150, 28, 150, 84, 1.6, d="4 3"), C(150, 88, 4), N(156, 98, "Ax̂ = P b", 9, "start", "bold"),
            R(144, 80, 8, 8, "none", 1), N(160, 54, "residual r ⊥ col(A)", 8.5, "start"), N(120, 134, "AᵀA x̂ = Aᵀ b   (normal equations)", 9, "middle", "bold")]

CARDS.append(card(16, 1, "LEAST SQUARES", "Least Squares = Projection onto the Column Space",
    _lsq(),
    "The closest point Ax̂ to b is its orthogonal projection; the leftover residual is perpendicular to every column",
    ["<strong>Problem:</strong> when $Ax=b$ has no exact solution, minimize $\\|Ax-b\\|_2$. The minimizer $\\hat x$ makes $A\\hat x$ the <strong>projection of $b$ onto $\\operatorname{col}(A)$</strong>.",
     "<strong>Normal equations:</strong> the residual $r=b-A\\hat x$ must be $\\perp$ every column, i.e. $A^*r=0\\iff A^*A\\hat x=A^*b$. If $A$ has independent columns, $\\hat x=(A^*A)^{-1}A^*b$.",
     "<strong>Projector:</strong> $P=A(A^*A)^{-1}A^*$ with $P^2=P=P^*$; error $\\|b-A\\hat x\\|^2=\\|b\\|^2-\\|Pb\\|^2$ (Pythagoras)."],
    r"$$\min_x\|Ax-b\|^2\iff A^*A\hat x=A^*b,\qquad A\hat x=Pb,\quad P=A(A^*A)^{-1}A^*$$",
    "Shadow-matching: you can't hit b exactly, so you land at the point of your reachable plane directly beneath it.",
    "The normal equations can be badly conditioned (κ(AᵀA) = κ(A)²). In practice use QR or SVD instead of forming AᵀA."))

CARDS.append(card(16, 2, "FOUR SUBSPACES", "The Four Fundamental Subspaces",
    [R(14, 16, 98, 50, "#ffffff", 1.6), R(14, 70, 98, 50, "#d9dee7", 1.6), N(63, 36, "row space", 9, w="bold"), N(63, 50, "dim r", 8.5), N(63, 92, "null space", 9, w="bold"), N(63, 106, "dim n − r", 8.5),
     R(128, 16, 98, 50, "#e2e8f0", 1.6), R(128, 70, 98, 50, "#ffffff", 1.6), N(177, 36, "column space", 9, w="bold"), N(177, 50, "dim r", 8.5), N(177, 92, "left null space", 9, w="bold"), N(177, 106, "dim m − r", 8.5),
     L(114, 40, 126, 40, 1.4, ar=True), N(120, 34, "A", 9),
     N(63, 134, "row ⊥ null  (in ℝⁿ)", 8.5, w="bold"), N(177, 134, "col ⊥ left null (in ℝᵐ)", 8.5, w="bold")],
    "Each pair of subspaces is an orthogonal decomposition of its ambient space",
    ["<strong>In the domain $\\mathbb{R}^n$:</strong> $\\operatorname{row}(A)=\\operatorname{null}(A)^\\perp$ and $\\mathbb{R}^n=\\operatorname{row}A\\oplus\\operatorname{null}A$, with dimensions $r$ and $n-r$.",
     "<strong>In the codomain $\\mathbb{R}^m$:</strong> $\\operatorname{col}(A)=\\operatorname{null}(A^T)^\\perp$ and $\\mathbb{R}^m=\\operatorname{col}A\\oplus\\operatorname{null}A^T$, with dimensions $r$ and $m-r$.",
     "<strong>The SVD sees all four at once:</strong> $v_1..v_r$ span the row space, $v_{r+1..n}$ the null space, $u_1..u_r$ the column space, $u_{r+1..m}$ the left null space."],
    r"$$\mathbb{R}^n=\operatorname{row}A\oplus\operatorname{null}A,\qquad \mathbb{R}^m=\operatorname{col}A\oplus\operatorname{null}A^{T},\qquad r=\operatorname{rank}A$$",
    "A house with four rooms: two on the input side, two on the output side, with every pair of rooms meeting at a right angle.",
    "Row space lives in the DOMAIN ℝⁿ; column space lives in the CODOMAIN ℝᵐ. Their dimensions agree (= rank) but they are in different spaces."))

CARDS.append(card(16, 3, "PSEUDOINVERSE", "The Moore–Penrose Pseudoinverse A⁺",
    [box(10, 16, 100, 28, "A = U Σ V*", "#f1f5f9", 11), L(110, 30, 126, 30, 1.4, ar=True), box(128, 16, 102, 28, "A⁺ = V Σ⁺ U*", "#e2e8f0", 11),
     N(120, 66, "Σ⁺: invert the nonzero σⱼ, transpose shape", 9, w="bold"), N(120, 84, "1/σ₁, …, 1/σ_r  (zeros stay zero)", 9),
     N(120, 104, "A⁺A = projection onto row space", 9), N(120, 118, "A A⁺ = projection onto column space", 9), N(120, 134, "A⁺ = A⁻¹ when A is invertible", 8.5, w="bold")],
    "Invert exactly what A can invert; send the rest to zero",
    ["<strong>Definition (via SVD):</strong> if $A=U\\Sigma V^*$ then $A^+=V\\Sigma^+U^*$, where $\\Sigma^+$ inverts the <strong>nonzero</strong> singular values and leaves zeros as zeros (and transposes the shape).",
     "<strong>Projectors:</strong> $AA^+$ is the orthogonal projection onto $\\operatorname{col}(A)$ and $A^+A$ is the orthogonal projection onto $\\operatorname{row}(A)$.",
     "<strong>Special cases:</strong> full column rank: $A^+=(A^*A)^{-1}A^*$ (left inverse); full row rank: $A^+=A^*(AA^*)^{-1}$ (right inverse); square invertible: $A^+=A^{-1}$."],
    r"$$A^+=V\Sigma^+U^*,\quad (\Sigma^+)_{jj}=\begin{cases}1/\sigma_j&\sigma_j>0\\0&\sigma_j=0\end{cases},\quad AA^+=P_{\operatorname{col}A},\ A^+A=P_{\operatorname{row}A}$$",
    "Undoing a scramble as well as you possibly can: where information survived you unscramble exactly, where it was erased you leave a neutral zero.",
    "A⁺ is NOT continuous in A: a tiny perturbation that makes a zero singular value nonzero changes A⁺ drastically (1/σ jumps from 0 to huge)."))

CARDS.append(card(16, 4, "PSEUDOINVERSE", "x = A⁺b: The Minimum-Norm Least-Squares Solution",
    [L(20, 118, 214, 118, 0.8, d="2 3"), L(60, 120, 190, 40, 1.8), N(60, 134, "all least-squares solutions", 8.5, "start"),
     C(110, 88, 4), L(110, 88, 70, 96, 1, d="3 3"), N(100, 78, "x⁺ = A⁺b", 9, "end", "bold"), C(70, 96, 3, "#ffffff"), N(52, 90, "0", 8.5, "end"),
     N(158, 30, "x⁺ ⊥ null(A)", 9, "start", "bold"), N(158, 44, "(row space)", 8.5, "start"), N(158, 64, "shortest vector on", 8.5, "start"), N(158, 76, "the solution line", 8.5, "start")],
    "Among all least-squares solutions, A⁺b is the one closest to the origin",
    ["<strong>Solution set:</strong> if $A$ is rank-deficient, there are infinitely many minimizers of $\\|Ax-b\\|$: $\\hat x+\\operatorname{null}A$. All give the same $A\\hat x=Pb$.",
     "<strong>Unique minimum-norm choice:</strong> $x^+=A^+b$ is the minimizer lying in $\\operatorname{row}(A)=\\operatorname{null}(A)^\\perp$, hence <strong>the one with smallest $\\|x\\|$</strong>.",
     "<strong>Why it matters:</strong> in underdetermined or ill-posed problems (wide matrices, duplicate features), $A^+b$ is the canonical, stable answer (also the limit of ridge regression $\\lambda\\to0$)."],
    r"$$x^+=A^+b=\arg\min\{\|x\|:\ x\in\arg\min_z\|Az-b\|\},\qquad x^+\in\operatorname{row}A$$",
    "Among all equally good answers on a straight road of solutions, you choose the one nearest to home (the origin).",
    "x⁺ is the shortest of the BEST fits. If Ax = b is consistent it is the shortest exact solution; if not, it is the shortest least-squares one."))

CARDS.append(card(16, 5, "PSEUDOINVERSE", "The Four Penrose Conditions",
    [box(10, 14, 108, 28, "A A⁺ A = A", "#f1f5f9", 11), box(122, 14, 108, 28, "A⁺ A A⁺ = A⁺", "#f1f5f9", 11),
     box(10, 56, 108, 28, "(A A⁺)* = A A⁺", "#f1f5f9", 11), box(122, 56, 108, 28, "(A⁺ A)* = A⁺ A", "#f1f5f9", 11),
     N(120, 108, "exactly ONE matrix X satisfies all four:  X = A⁺", 9, w="bold"), N(120, 124, "(the last two say the products are orthogonal projections)", 8.5)],
    "Four equations pin down the pseudoinverse uniquely, with no mention of the SVD",
    ["<strong>Conditions:</strong> (1) $AXA=A$, (2) $XAX=X$, (3) $(AX)^*=AX$, (4) $(XA)^*=XA$. There is <strong>exactly one</strong> $X$ satisfying all four, called $A^+$.",
     "<strong>Meaning:</strong> (1)–(2) say $X$ is a generalized (reflexive) inverse; (3)–(4) say $AX$ and $XA$ are <strong>orthogonal</strong> (self-adjoint) projections onto the column and row spaces.",
     "<strong>Use:</strong> to prove a formula equals $A^+$, check the four identities; e.g. $(A^+)^+=A$, $(A^*)^+=(A^+)^*$ and $A^+=(A^*A)^+A^*$."],
    r"$$AXA=A,\quad XAX=X,\quad (AX)^*=AX,\quad (XA)^*=XA\ \Longleftrightarrow\ X=A^+$$",
    "Four house rules a unique tenant must obey: do the job (1,2) and stay square to the floor plan (3,4).",
    "Condition 3 and 4 are what make A⁺ the ORTHOGONAL generalized inverse. Dropping them leaves many generalized inverses that give non-orthogonal projections."))

CARDS.append(card(16, 6, "WORKED BENCHMARK", "Worked Benchmark: Best-Fit Line Through (0,1), (1,2), (2,2)",
    [L(20, 118, 214, 118, 0.8), L(30, 118, 30, 16, 0.8), C(52, 88, 3.5), C(100, 60, 3.5), C(148, 60, 3.5),
     L(40, 94, 190, 52, 1.8), L(52, 88, 52, 91, 1.2), L(100, 60, 100, 70, 1.2), L(148, 60, 148, 56, 1.2),
     N(34, 130, "x=0", 8), N(100, 130, "1", 8), N(148, 130, "2", 8),
     N(150, 22, "ŷ = 7/6 + x/2", 9.5, "start", "bold"), N(150, 36, "AᵀA = [[3,3],[3,5]]", 8.5, "start"), N(150, 98, "Aᵀb = (5, 6)", 8.5, "start"),
     N(124, 110, "residuals (−1/6, 1/3, −1/6)", 8.5, "start", "bold")],
    "The least-squares line is y = 7/6 + x/2; its residuals sum to zero and are orthogonal to the column (1,1,1) and (0,1,2)",
    ["<strong>Setup:</strong> $A=\\begin{pmatrix}1&0\\\\1&1\\\\1&2\\end{pmatrix}$, $b=(1,2,2)^T$, so $A^TA=\\begin{pmatrix}3&3\\\\3&5\\end{pmatrix}$ and $A^Tb=(5,6)^T$.",
     "<strong>Normal equations:</strong> $3a+3c=5$, $3a+5c=6\\Rightarrow c=\\tfrac12$, $a=\\tfrac76$. Fit: $\\hat y=\\tfrac76+\\tfrac12x$, giving $\\hat b=(\\tfrac76,\\tfrac53,\\tfrac{13}{6})$.",
     "<strong>Residual</strong> $r=b-\\hat b=(-\\tfrac16,\\tfrac13,-\\tfrac16)$. Check $A^Tr=0$: sum $=0$ ✓ and $0\\cdot(-\\tfrac16)+1\\cdot\\tfrac13+2\\cdot(-\\tfrac16)=0$ ✓: <strong>the residual is orthogonal to the columns</strong>."],
    r"$$\hat x=(A^TA)^{-1}A^Tb=\begin{pmatrix}7/6\\1/2\end{pmatrix},\qquad A^T(b-A\hat x)=0$$",
    "Hanging a straight stick between three pegs of different heights: it settles where the up and down tugs cancel exactly.",
    "Always verify AᵀR = 0 at the end. It catches arithmetic slips in solving the normal equations immediately."))

# ====================== 17 · TRACE, DETERMINANT & VOLUME ======================
CARDS.append(card(17, 1, "TRACE", "Trace: Sum of Diagonal = Sum of Eigenvalues",
    [GRID(14, 18, [["a", "", ""], ["", "b", ""], ["", "", "c"]], cell=26, sz=12, shade={(0, 0), (1, 1), (2, 2)}), N(54, 106, "tr A = a + b + c", 9.5, "middle", "bold"),
     N(150, 28, "tr A = Σ λⱼ", 11, "start", "bold"), N(150, 46, "tr(AB) = tr(BA)", 10, "start", "bold"), N(150, 64, "tr(S⁻¹AS) = tr A", 9.5, "start"),
     N(150, 82, "linear: tr(A+B) = trA + trB", 8.5, "start"), N(150, 100, "NOT multiplicative:", 8.5, "start"), N(150, 112, "tr(AB) ≠ trA trB", 8.5, "start")],
    "The trace equals the sum of the eigenvalues and is unchanged by any change of basis",
    ["<strong>Definition:</strong> $\\operatorname{tr}A=\\sum A_{ii}$. It is <strong>linear</strong> and satisfies $\\operatorname{tr}(AB)=\\operatorname{tr}(BA)$ (even for non-square $A,B$ when the products make sense).",
     "<strong>Basis independence:</strong> $\\operatorname{tr}(S^{-1}AS)=\\operatorname{tr}(ASS^{-1})=\\operatorname{tr}A$, so the trace is a property of the <strong>operator</strong>; it equals the sum of eigenvalues counted with algebraic multiplicity.",
     "<strong>Use:</strong> $\\operatorname{tr}(A^*A)=\\sum|a_{ij}|^2=\\|A\\|_F^2$, the Frobenius inner product $\\langle A,B\\rangle=\\operatorname{tr}(A^*B)$, and trace of a projection = its rank."],
    r"$$\operatorname{tr}A=\sum_iA_{ii}=\sum_j\lambda_j,\qquad \operatorname{tr}(AB)=\operatorname{tr}(BA),\qquad \operatorname{tr}(A^*A)=\|A\|_F^2$$",
    "The total 'weight' of a machine's stretching: it doesn't matter which way you tilt the camera to look at it, the total stays the same.",
    "tr(ABC) = tr(BCA) = tr(CAB) (cyclic) but NOT tr(BAC). The cyclic property does not allow arbitrary reordering."))

CARDS.append(card(17, 2, "DETERMINANT", "Determinant: Product of Eigenvalues, and Multiplicative",
    [box(10, 14, 100, 28, "det A = Π λⱼ", "#e2e8f0", 11), box(130, 14, 100, 28, "det(AB) = det A det B", "#f1f5f9", 8.5),
     box(10, 56, 100, 28, "det Aᵀ = det A", "#f1f5f9", 10), box(130, 56, 100, 28, "det A⁻¹ = 1/det A", "#f1f5f9", 9.5),
     box(10, 98, 100, 28, "det(cA) = cⁿ det A", "#f1f5f9", 9.5), box(130, 98, 100, 28, "det ≠ 0 ⇔ invertible", "#f1f5f9", 9.5)],
    "The determinant multiplies along composition, equals the product of the eigenvalues, and detects invertibility",
    ["<strong>Meaning:</strong> $\\det A=\\prod\\lambda_j$ (with multiplicity) and $A$ is invertible $\\iff\\det A\\ne0\\iff0$ is not an eigenvalue.",
     "<strong>Rules:</strong> $\\det(AB)=\\det A\\det B$, $\\det A^T=\\det A$, $\\det A^{-1}=1/\\det A$, $\\det(cA)=c^n\\det A$ (not $c\\det A$!), and swapping two rows flips the sign.",
     "<strong>Basis independence:</strong> $\\det(S^{-1}AS)=\\det A$, so the determinant belongs to the operator. A block-triangular matrix has $\\det=\\det(\\text{blocks})$."],
    r"$$\det A=\prod_j\lambda_j,\quad \det(AB)=\det A\,\det B,\quad \det(cA)=c^n\det A,\quad \det(A+B)\ne\det A+\det B$$",
    "A compound interest factor: composing two machines multiplies their overall scaling factors, which is exactly what det does.",
    "det is multiplicative, NOT additive: det(A + B) ≠ det A + det B. And det(cA) scales by cⁿ, a common sign/scale slip."))

CARDS.append(card(17, 3, "VOLUME", "|det A| = Volume Scaling Factor",
    [L(20, 118, 100, 118, 0.8, ar=True), L(20, 118, 20, 38, 0.8, ar=True), R(20, 78, 40, 40, "#f1f5f9", 1.8), N(40, 100, "area 1", 9, "middle", "bold"),
     L(108, 98, 130, 98, 1.5, ar=True), N(119, 90, "A", 10, "middle", "bold"),
     PG("140,118 190,108 210,70 160,80", "#e2e8f0", 1.8), N(176, 100, "|det A|", 9.5, "middle", "bold"),
     V(140, 118, 190, 108, 1.6), V(140, 118, 160, 80, 1.6), N(196, 114, "Ae₁", 8.5, "start"), N(138, 78, "Ae₂", 8.5, "end"),
     N(120, 138, "sign of det = orientation (flip if negative)", 8.5, w="bold"), N(120, 14, "area(image) = |det A| · area(original)", 9, w="bold")],
    "A maps the unit square to the parallelogram spanned by its columns; the area scales by |det A|",
    ["<strong>Geometry:</strong> for $A\\in\\mathbb{R}^{n\\times n}$, the image of the unit cube is the parallelepiped spanned by the columns; its <strong>volume is $|\\det A|$</strong>, and every region's volume is multiplied by $|\\det A|$.",
     "<strong>Sign:</strong> $\\det A<0$ means $A$ <strong>reverses orientation</strong> (a reflection component); $\\det A=0$ flattens space onto a lower dimension (volume $0$).",
     "<strong>Via SVD:</strong> $|\\det A|=\\prod\\sigma_j$ because $U,V$ preserve volume and $\\Sigma$ stretches axes by $\\sigma_j$. This is why $|\\det|$ appears in the change-of-variables (Jacobian) formula."],
    r"$$\operatorname{vol}(A\Omega)=|\det A|\operatorname{vol}(\Omega),\qquad |\det A|=\prod_j\sigma_j,\qquad \det A=0\Rightarrow\text{flattened}$$",
    "A photocopier with a zoom: area changes by the zoom squared, and a mirror setting (negative det) also flips left to right.",
    "Volume uses |det|. The signed det carries orientation. For Jacobians in integrals always use the ABSOLUTE value."))

CARDS.append(card(17, 4, "CHARACTERISTIC POLYNOMIAL", "Coefficients of the Characteristic Polynomial",
    [N(120, 24, "p(λ) = det(λI − A)", 10.5, "middle", "bold"), N(120, 46, "= λⁿ − (tr A) λⁿ⁻¹ + … + (−1)ⁿ det A", 9.5, "middle"),
     L(30, 56, 210, 56, 0.9), N(60, 76, "λ⁽ⁿ⁻¹⁾ coeff", 8.5), N(60, 92, "= − Σ λⱼ", 9.5, w="bold"), N(180, 76, "constant term", 8.5), N(180, 92, "= (−1)ⁿ Π λⱼ", 9.5, w="bold"),
     N(120, 116, "2×2: λ² − tr(A) λ + det(A)", 10, w="bold"), N(120, 132, "the whole polynomial = elementary symmetric functions of eigenvalues", 8, w="normal")],
    "The first and last coefficients are the trace and the determinant: for 2×2 that is everything you need",
    ["<strong>Expansion:</strong> $p_A(\\lambda)=\\lambda^n-e_1\\lambda^{n-1}+e_2\\lambda^{n-2}-\\dots+(-1)^ne_n$, where $e_k$ is the <strong>sum of all $k\\times k$ principal minors</strong> = the $k$-th elementary symmetric function of the eigenvalues.",
     "<strong>Special coefficients:</strong> $e_1=\\operatorname{tr}A$ and $e_n=\\det A$. For $2\\times2$: <strong>$p(\\lambda)=\\lambda^2-\\operatorname{tr}(A)\\lambda+\\det A$</strong>.",
     "<strong>Check:</strong> the roots must sum to the trace and multiply to the determinant. If your eigenvalues violate either, the arithmetic is wrong."],
    r"$$p_A(\lambda)=\lambda^n-\operatorname{tr}(A)\lambda^{n-1}+\cdots+(-1)^n\det A,\qquad p_{2\times2}=\lambda^2-\operatorname{tr}A\,\lambda+\det A$$",
    "A fingerprint made of symmetric sums of the eigenvalues: the first digit is their total and the last is their product (with a sign).",
    "The sign of the constant term is (−1)ⁿ det A. For odd n it is −det A, which students often get wrong when expanding det(λI − A)."))

CARDS.append(card(17, 5, "WORKED BENCHMARK", "Worked Benchmark: A = [[2,1],[1,3]]",
    [GRID(12, 16, [[2, 1], [1, 3]], cell=28, sz=12), N(40, 82, "A", 10, w="bold"),
     N(86, 28, "tr A = 5,  det A = 5", 9.5, "start", "bold"), N(86, 46, "λ² − 5λ + 5 = 0", 9.5, "start"), N(86, 64, "λ = (5 ± √5)/2 ≈ 3.62, 1.38", 9, "start", "bold"),
     N(14, 104, "sum:  (5+√5)/2 + (5−√5)/2 = 5 = tr ✓", 8.5, "start"), N(14, 118, "product: (25 − 5)/4 = 5 = det ✓", 8.5, "start"),
     N(14, 134, "area scales by 5; orientation preserved (det > 0)", 8.5, "start", "bold")],
    "Two eigenvalues (5±√5)/2 sum to the trace 5 and multiply to the determinant 5",
    ["<strong>Basics:</strong> $\\operatorname{tr}A=2+3=5$ and $\\det A=6-1=5$, so $p(\\lambda)=\\lambda^2-5\\lambda+5$.",
     "<strong>Roots:</strong> $\\lambda=\\frac{5\\pm\\sqrt{25-20}}{2}=\\frac{5\\pm\\sqrt5}{2}\\approx3.62,\\ 1.38$. Sum $=5$ ✓ (trace) and product $=\\frac{25-5}{4}=5$ ✓ (determinant).",
     "<strong>Geometry:</strong> $\\det A=5>0$: <strong>areas are multiplied by $5$</strong> and orientation is preserved. $A$ is symmetric, so the eigenvectors are perpendicular and the singular values equal the eigenvalues."],
    r"$$\lambda=\tfrac{5\pm\sqrt5}{2},\qquad \lambda_1+\lambda_2=5=\operatorname{tr}A,\qquad \lambda_1\lambda_2=5=\det A$$",
    "A quick sanity check for any 2×2: whatever eigenvalues you find must add to the sum of the diagonal and multiply to the cross-difference.",
    "A symmetric matrix has real eigenvalues even when they are irrational. Don't stop at 'discriminant not a perfect square' and conclude no real eigenvalues."))

# ====================== 18 · MARKOV CHAINS & CONSENSUS ======================
def _chain(a="0.9", b="0.5"):
    return [C(60, 72, 24, "#ffffff", 1.8), N(60, 76, "1", 11, "middle", "bold"), C(180, 72, 24, "#ffffff", 1.8), N(180, 76, "2", 11, "middle", "bold"),
            P("M82 62 Q120 38 158 62", w=1.6, ar=True), N(120, 40, "0.1", 9, "middle", "bold"),
            P("M158 82 Q120 106 82 82", w=1.6, ar=True), N(120, 112, b, 9, "middle", "bold"),
            P("M48 52 Q34 28 62 48", w=1.5, ar=True), N(34, 34, a, 9, "middle", "bold"),
            P("M192 52 Q208 28 182 48", w=1.5, ar=True), N(208, 34, "0.5", 9, "middle", "bold")]

CARDS.append(card(18, 1, "MARKOV CHAINS", "Stochastic Matrices: Rows Sum to 1",
    _chain() + [N(120, 134, "P = [[0.9, 0.1],[0.5, 0.5]]   P·1 = 1", 9, w="bold"), N(120, 144, "", 8)],
    "Each row of P is a probability distribution over next states, so P times the all-ones vector is itself",
    ["<strong>Definition:</strong> a <strong>(row-)stochastic</strong> matrix has non-negative entries and each row sums to $1$; $P_{ij}$ is the probability of moving from state $i$ to state $j$.",
     "<strong>Eigenvalue 1:</strong> $P\\mathbf{1}=\\mathbf{1}$, so $\\lambda=1$ is always an eigenvalue (right eigenvector $\\mathbf{1}$) and every eigenvalue satisfies $|\\lambda|\\le1$.",
     "<strong>Evolution:</strong> a row distribution $\\pi_k$ evolves by $\\pi_{k+1}=\\pi_kP$, so $\\pi_k=\\pi_0P^k$: <strong>powers of $P$</strong> describe the future."],
    r"$$P_{ij}\ge0,\ \ P\mathbf 1=\mathbf 1,\qquad \pi_{k+1}=\pi_kP,\qquad |\lambda(P)|\le1$$",
    "A map of one-way streets with probabilities on each: starting anywhere, your location after k steps is described by the k-th power of the map.",
    "Row vs column convention: with row-stochastic P you multiply a ROW vector on the left (πP). Mixing conventions transposes everything."))

CARDS.append(card(18, 2, "MARKOV CHAINS", "Stationary Distribution & Perron–Frobenius",
    [N(120, 18, "irreducible + aperiodic (primitive)", 9.5, "middle", "bold"), L(120, 24, 120, 38, 1.4, ar=True),
     box(20, 42, 200, 32, "unique π > 0 with πP = π,  Σπᵢ = 1", "#e2e8f0", 9.5),
     N(120, 94, "Pᵏ → 𝟙π   (every row converges to π)", 10, "middle", "bold"), N(120, 112, "π = left eigenvector for λ = 1", 9), N(120, 128, "initial state is forgotten in the long run", 8.5)],
    "A well-connected chain forgets its start and settles to one distribution π",
    ["<strong>Perron–Frobenius:</strong> for an <strong>irreducible, aperiodic</strong> stochastic $P$ the eigenvalue $1$ is simple, there is a unique positive stationary row vector $\\pi=\\pi P$ ($\\sum\\pi_i=1$), and every other eigenvalue has $|\\lambda|<1$.",
     "<strong>Convergence:</strong> $\\pi_0P^k\\to\\pi$ for <strong>every</strong> starting distribution, i.e. $P^k\\to\\mathbf 1\\pi$ (all rows converge to $\\pi$).",
     "<strong>Interpretation:</strong> $\\pi_i$ is the long-run fraction of time in state $i$; for a doubly stochastic $P$, $\\pi$ is uniform."],
    r"$$\pi P=\pi,\ \ \sum\pi_i=1\ \Rightarrow\ P^k\to\mathbf 1\pi\quad(\text{irreducible},\ \text{aperiodic})$$",
    "Stirring cream into coffee: after enough stirs the mixture looks the same wherever you started.",
    "Both conditions are needed: periodic chains oscillate (never converge) and reducible chains can have several stationary distributions."))

def _rate():
    pts = [(24 + k * 24, 118 - 90 * (0.6 ** k)) for k in range(0, 8)]
    pts2 = [(24 + k * 24, 118 - 90 * (0.9 ** k)) for k in range(0, 8)]
    return [AX(24, 120, 222, 14), poly([(x, 120 - (120 - y)) for x, y in pts], 2.2), poly(pts2, 1.8, "5 3"),
            N(150, 70, "|λ₂| = 0.6: fast", 9, "start", "bold"), N(150, 100, "|λ₂| = 0.9: slow", 9, "start"),
            N(30, 16, "‖πₖ − π‖", 8.5, "start"), N(120, 138, "error ≈ C |λ₂|ᵏ  (steps k →)", 8.5)]

CARDS.append(card(18, 3, "CONVERGENCE RATE", "Second Eigenvalue Sets the Mixing Speed",
    [L(24, 120, 222, 120, 1, ar=True), L(24, 120, 24, 14, 1, ar=True)] +
    [poly([(24 + k * 24, 120 - 90 * (0.6 ** k)) for k in range(0, 8)], 2.2),
     poly([(24 + k * 24, 120 - 90 * (0.9 ** k)) for k in range(0, 8)], 1.8, "5 3")] +
    [N(120, 22, "|λ₂| = 0.9 (slow, dashed)", 8.5, "start"), N(120, 34, "|λ₂| = 0.6 (fast, solid)", 8.5, "start", "bold"),
     N(30, 16, "‖πₖ − π‖", 8.5, "start"), N(120, 138, "error ≈ C·|λ₂|ᵏ    (steps k →)", 8.5)],
    "The farther |λ₂| is below 1, the faster the distribution converges to π",
    ["<strong>Decay:</strong> write $P=\\mathbf 1\\pi+\\sum_{j\\ge2}\\lambda_jP_j$ (diagonalizable case); then $P^k-\\mathbf 1\\pi=\\sum_{j\\ge2}\\lambda_j^kP_j$ and the slowest term is $|\\lambda_2|^k$.",
     "<strong>Spectral gap:</strong> $1-|\\lambda_2|$ governs convergence: error $\\approx C|\\lambda_2|^k$, mixing time $\\sim1/(1-|\\lambda_2|)$. A larger gap means faster mixing.",
     "<strong>Same idea for consensus</strong> and for power iteration: the second-largest eigenvalue modulus is the convergence factor."],
    r"$$\|\pi_0P^k-\pi\|\le C\,|\lambda_2|^k,\qquad \text{mixing time}\approx\frac{1}{1-|\lambda_2|}$$",
    "Ripples on a pond: the slowest ripple (second eigenvalue) determines how long the pond takes to go flat.",
    "|λ₂| is the second largest eigenvalue MODULUS (complex eigenvalues count), not the second largest real value."))

CARDS.append(card(18, 4, "CONSENSUS", "Averaging Consensus: x(k+1) = W x(k)",
    [C(50, 40, 12, "#ffffff", 1.6), C(170, 40, 12, "#ffffff", 1.6), C(110, 100, 12, "#ffffff", 1.6),
     L(62, 40, 158, 40, 1.4), L(56, 52, 104, 90, 1.4), L(164, 52, 116, 90, 1.4),
     N(50, 44, "x₁", 9, "middle", "bold"), N(170, 44, "x₂", 9, "middle", "bold"), N(110, 104, "x₃", 9, "middle", "bold"),
     N(210, 100, "→ x̄·𝟙", 10, "start", "bold"), N(14, 126, "W row-stochastic: each node averages its neighbors", 8.5, "start"),
     N(14, 140, "W also column-stochastic ⇒ converges to the average", 8.5, "start", "bold")],
    "Repeated local averaging drives every node to the same value",
    ["<strong>Algorithm:</strong> each node replaces its value by a weighted average of its neighbors' values: $x(k+1)=Wx(k)$ with $W$ <strong>row-stochastic</strong> and supported on the graph.",
     "<strong>Convergence:</strong> if $W$ is primitive, $x(k)\\to(\\pi x(0))\\mathbf 1$: <strong>all nodes agree</strong> on a weighted average. If $W$ is also <strong>column-stochastic (doubly stochastic)</strong> then $\\pi=\\mathbf 1^T/n$ and the consensus value is the exact <strong>average</strong> $\\frac1n\\sum x_i(0)$.",
     "<strong>Rate:</strong> geometric, with factor $|\\lambda_2(W)|$; a better-connected graph gives smaller $|\\lambda_2|$ and faster agreement."],
    r"$$x(k+1)=Wx(k)\ \Rightarrow\ x(k)\to(\pi x(0))\,\mathbf 1;\quad W\ \text{doubly stochastic}\Rightarrow\ \to\bar x\,\mathbf 1,\ \bar x=\tfrac1n\textstyle\sum x_i(0)$$",
    "A room of people who keep adjusting their opinion to the average of whoever they talk to: gradually the room agrees.",
    "Row-stochastic gives consensus, but the value is a WEIGHTED average. Only doubly stochastic W preserves the sum and yields the plain average."))

CARDS.append(card(18, 5, "CONSENSUS", "Graph Laplacian & Algebraic Connectivity",
    [C(40, 40, 11, "#ffffff", 1.6), C(120, 40, 11, "#ffffff", 1.6), C(200, 40, 11, "#ffffff", 1.6), C(120, 100, 11, "#ffffff", 1.6),
     L(51, 40, 109, 40, 1.4), L(131, 40, 189, 40, 1.4), L(120, 51, 120, 89, 1.4),
     N(14, 76, "L = D − A  (PSD)", 9.5, "start", "bold"), N(14, 92, "L𝟙 = 0", 9, "start"), N(14, 108, "ẋ = −Lx  ⇒  x → x̄𝟙", 9, "start", "bold"),
     N(150, 82, "connected ⇔ λ₂(L) > 0", 9, "start", "bold"), N(150, 98, "(algebraic connectivity)", 8.5, "start"), N(150, 114, "rate = e^{−λ₂ t}", 9, "start"), N(14, 134, "# of zero eigenvalues = # of connected components", 8.5, "start")],
    "The second-smallest Laplacian eigenvalue is positive exactly when the graph is connected, and it sets the consensus speed",
    ["<strong>Laplacian:</strong> $L=D-A$ ($D$ = degree matrix, $A$ = adjacency). It is symmetric <strong>positive semidefinite</strong> with $x^TLx=\\sum_{(i,j)\\in E}(x_i-x_j)^2$, so $L\\mathbf 1=0$.",
     "<strong>Algebraic connectivity:</strong> $0=\\lambda_1\\le\\lambda_2\\le\\cdots$; $\\lambda_2>0\\iff$ the graph is <strong>connected</strong> (the multiplicity of $0$ counts connected components).",
     "<strong>Continuous consensus:</strong> $\\dot x=-Lx$ has solution $x(t)=e^{-Lt}x(0)\\to\\bar x\\mathbf 1$ for connected graphs, with error decaying like $e^{-\\lambda_2t}$."],
    r"$$x^TLx=\sum_{(i,j)\in E}(x_i-x_j)^2\ge0,\qquad L\mathbf 1=0,\qquad \text{connected}\iff\lambda_2(L)>0$$",
    "A network of springs between nodes: the energy is the total stretch, and the slowest relaxing mode is governed by λ₂.",
    "Laplacian eigenvalues are ≥ 0 with the all-ones vector at 0. The discrete update uses W = I − εL with ε small enough that W stays stochastic (ε ≤ 1/d_max)."))

CARDS.append(card(18, 6, "WORKED BENCHMARK", "Worked Benchmark: P = [[0.9, 0.1],[0.5, 0.5]]",
    [N(14, 22, "stationary: π = (a, b),  a + b = 1", 9, "start", "bold"), N(14, 40, "πP = π:  0.9a + 0.5b = a", 9, "start"), N(14, 54, "⇒ 0.5b = 0.1a ⇒ a = 5b", 9, "start"),
     N(14, 72, "⇒ π = (5/6, 1/6)", 11, "start", "bold"),
     N(14, 94, "eigenvalues: 1 and tr − 1 = 1.4 − 1 = 0.4", 8.5, "start", "bold"), N(14, 108, "|λ₂| = 0.4 ⇒ error shrinks 0.4ᵏ", 8.5, "start"),
     N(14, 124, "P² ≈ [[.86, .14],[.70, .30]] → rows → (.83, .17)", 8.5, "start"), N(14, 138, "after k = 5: 0.4⁵ ≈ 0.01 off π", 8.5, "start"),
     C(190, 60, 20, "#ffffff", 1.6), N(190, 64, "1", 10, "middle", "bold"), C(190, 110, 20, "#ffffff", 1.6), N(190, 114, "2", 10, "middle", "bold"),
     L(190, 80, 190, 90, 1.3, ar=True), N(222, 88, "0.1", 8, "middle")],
    "Long-run fractions are 5/6 and 1/6; the second eigenvalue 0.4 means the chain mixes in a few steps",
    ["<strong>Stationary:</strong> solve $\\pi P=\\pi$: $0.9a+0.5b=a\\Rightarrow0.5b=0.1a\\Rightarrow a=5b$, with $a+b=1$ gives <strong>$\\pi=(5/6,\\,1/6)$</strong>. Check column 2: $0.1a+0.5b=\\tfrac{0.5}{6}+\\tfrac{0.5}{6}=\\tfrac16$ ✓.",
     "<strong>Eigenvalues:</strong> $\\lambda_1=1$ and $\\lambda_2=\\operatorname{tr}P-1=1.4-1=\\mathbf{0.4}$ (also $\\det P=0.45-0.05=0.4$ ✓).",
     "<strong>Mixing:</strong> $\\pi_0P^k-\\pi\\sim0.4^k$, so after $5$ steps it is within about $1\\%$ of $\\pi$; e.g. $P^2\\approx\\begin{pmatrix}0.86&0.14\\\\0.70&0.30\\end{pmatrix}$ already has rows near $(0.83,0.17)$."],
    r"$$\pi=\big(\tfrac56,\tfrac16\big),\qquad \lambda_2=\operatorname{tr}P-1=0.4,\qquad \|\pi_0P^k-\pi\|\propto0.4^k$$",
    "A weather model that says 'sunny stays sunny 90% of the time': in the long run about 5 of every 6 days are sunny, wherever you start.",
    "π is a LEFT eigenvector (πP = π). Solving Pv = v instead gives the all-ones vector, which is not the stationary distribution."))
