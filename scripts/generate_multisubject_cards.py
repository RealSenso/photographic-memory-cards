import json

# Load existing pristine CMO cards from cards_data.js
with open('/Users/senso/Projects/photographic-memory-cards/cards_data.js') as f:
    text = f.read()

start = text.find('[')
end = text.rfind(']') + 1
loaded = json.loads(text[start:end])
existing_cmo = [c for c in loaded if c.get('subject') == 'CMO']

# Load newly built CMO cards (Topics 06, 07, 08, 10)
with open('/Users/senso/Projects/photographic-memory-cards/scripts/new_cmo_cards.json') as f:
    new_cmo = json.load(f)

# Load newly built CMO cards (Topics 11 through 19)
for t_num in range(11, 20):
    with open(f'/Users/senso/Projects/photographic-memory-cards/scripts/cmo_topic{t_num}.json') as f:
        new_cmo.extend(json.load(f))

cmo_dict = {c['id']: c for c in existing_cmo}
for c in new_cmo:
    cmo_dict[c['id']] = c

# Sort all CMO cards strictly by (topicId, cardNumber)
all_cards = sorted(cmo_dict.values(), key=lambda c: (c['topicId'], c['cardNumber']))

# =============================================================================
# LAA (Linear Algebra and Applications - E0 219)
# =============================================================================
laa_cards = [
    {
        "id": 20101,
        "subject": "LAA",
        "topicId": "01_Vector_Spaces_Subspaces_and_Direct_Sums",
        "topicTitle": "01 · Vector Spaces, Subspaces & Direct Sums",
        "cardNumber": "01",
        "category": "VECTOR SPACE FOUNDATIONS",
        "highlighterClass": "highlight-cyan",
        "title": "Subspace 3-Step Verification Test",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-laa1" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- Ambient Box -->
  <rect x="25" y="20" width="190" height="105" rx="8" fill="none" stroke="#000000" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="35" y="34" fill="#000000" font-size="8.5" font-family="serif" font-style="italic">Ambient V = ℝ³</text>
  <!-- Subspace Plane Passing through Origin -->
  <polygon points="45,105 110,35 195,45 130,115" fill="#f1f5f9" stroke="#000000" stroke-width="1.8"/>
  <!-- Origin 0 -->
  <circle cx="120" cy="75" r="3.5" fill="#000000"/>
  <text x="120" y="65" fill="#000000" font-size="9" font-family="serif" font-style="italic" font-weight="bold" text-anchor="middle">0 ∈ U</text>
  <!-- Vectors u and v -->
  <line x1="120" y1="75" x2="160" y2="58" stroke="#000000" stroke-width="1.8" marker-end="url(#arr-laa1)"/>
  <text x="165" y="56" fill="#000000" font-size="9" font-family="serif" font-style="italic">u</text>
  <line x1="120" y1="75" x2="95" y2="98" stroke="#000000" stroke-width="1.8" marker-end="url(#arr-laa1)"/>
  <text x="88" y="106" fill="#000000" font-size="9" font-family="serif" font-style="italic">v</text>
  <!-- Sum vector u + v -->
  <line x1="120" y1="75" x2="140" y2="82" stroke="#000000" stroke-width="2" marker-end="url(#arr-laa1)"/>
  <text x="145" y="94" fill="#000000" font-size="9" font-family="serif" font-style="italic" font-weight="bold">u + v ∈ U</text>
  <text x="120" y="134" fill="#000000" font-size="8.5" font-family="sans-serif" text-anchor="middle">Plane U passes through 0 and is closed under addition &amp; scaling</text>
</svg>""",
        "drawingCaption": "Subspace Test: Plane U must pass through the origin 0 and be closed under vector addition and scaling",
        "coreTranslation": [
            "A subset $U \\subset V$ of a vector space over field $\\mathbb{F}$ is a <strong>Subspace</strong> if and only if it satisfies the <strong>3-Step Test</strong>:",
            "<strong>1. Additive Identity:</strong> $0 \\in U$. (If the origin is missing, $U$ fails immediately).",
            "<strong>2. Closure under Addition:</strong> $u, v \\in U \\implies u + v \\in U$. <strong>3. Closure under Scalar Mult:</strong> $u \\in U, c \\in \\mathbb{F} \\implies c u \\in U$."
        ],
        "math": "$$U \\le V \\iff 0 \\in U \\quad \\text{and} \\quad \\alpha u + \\beta v \\in U \\quad \\forall \\, u, v \\in U, \\; \\alpha, \\beta \\in \\mathbb{F}$$",
        "personalConnection": "A flat sheet of glass slicing through 3D space: it is only a valid subspace if the exact origin $(0, 0, 0)$ is drilled through the glass. An affine plane displaced by even $10^{-6}$ fails the zero test.",
        "examTrap": "Testing if an affine plane (e.g. $W = \\{(x, y, z) : x + 2y - z = 4\\}$) is a subspace. Answer: NO! $(0,0,0) \\notin W$. It is an affine manifold, not a linear subspace."
    },
    {
        "id": 20102,
        "subject": "LAA",
        "topicId": "01_Vector_Spaces_Subspaces_and_Direct_Sums",
        "topicTitle": "01 · Vector Spaces, Subspaces & Direct Sums",
        "cardNumber": "02",
        "category": "DIRECT SUMS",
        "highlighterClass": "highlight-amber",
        "title": "Sum of Subspaces vs. Direct Sum U₁ ⊕ U₂",
        "textbookImg": "assets/meyer_fig5_13_1.png",
        "textbookRef": "Carl Meyer, Matrix Analysis, Fig. 5.13.1 (p. 438)",
        "drawingCaption": "Meyer Fig. 5.13.1: Unique direct sum decomposition v = m + n where m ∈ M and n ∈ M^⊥",
        "drawingSvg": "",
        "coreTranslation": [
            "The <strong>Sum of Subspaces</strong> is $U_1 + \\dots + U_m = \\{u_1 + \\dots + u_m : u_i \\in U_i\\}$. It is the smallest subspace containing all $U_i$.",
            "The sum is called a <strong>Direct Sum</strong>, written $U_1 \\oplus \\dots \\oplus U_m$, if every vector $v \\in U_1 + \\dots + U_m$ can be written as $v = u_1 + \\dots + u_m$ in <strong>EXACTLY ONE UNIQUE WAY</strong>.",
            "<strong>Two Subspaces ($m = 2$):</strong> The sum $U_1 + U_2$ is direct if and only if their intersection is trivial: $U_1 \\cap U_2 = \\{0\\}$."
        ],
        "math": "$$U_1 + U_2 = U_1 \\oplus U_2 \\iff U_1 \\cap U_2 = \\{\\mathbf{0}\\}$$",
        "personalConnection": "Coordinate axes in 2D space: the x-axis and y-axis share ONLY the origin $(0,0)$. Every point $(x, y)$ decomposes uniquely into an x-component and a y-component.",
        "examTrap": "The intersection condition $U_i \\cap U_j = \\{0\\}$ ONLY works for $m=2$ subspaces! For 3 or more subspaces, pairwise trivial intersection does NOT guarantee a direct sum."
    },
    {
        "id": 20103,
        "subject": "LAA",
        "topicId": "01_Vector_Spaces_Subspaces_and_Direct_Sums",
        "topicTitle": "01 · Vector Spaces, Subspaces & Direct Sums",
        "cardNumber": "03",
        "category": "DIRECT SUM CRITERION",
        "highlighterClass": "highlight-emerald",
        "title": "Fundamental Direct Sum Zero-Vector Criterion",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-laa3" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- 3 independent axes meeting strictly at origin -->
  <line x1="120" y1="75" x2="195" y2="75" stroke="#000000" stroke-width="2" marker-end="url(#arr-laa3)"/>
  <text x="200" y="78" fill="#000000" font-size="9" font-family="serif" font-style="italic">u₁ ∈ U₁</text>
  <line x1="120" y1="75" x2="120" y2="18" stroke="#000000" stroke-width="2" marker-end="url(#arr-laa3)"/>
  <text x="120" y="14" fill="#000000" font-size="9" font-family="serif" font-style="italic" text-anchor="middle">u₂ ∈ U₂</text>
  <line x1="120" y1="75" x2="60" y2="120" stroke="#000000" stroke-width="2" marker-end="url(#arr-laa3)"/>
  <text x="45" y="125" fill="#000000" font-size="9" font-family="serif" font-style="italic">u₃ ∈ U₃</text>
  <!-- Origin -->
  <circle cx="120" cy="75" r="4" fill="#000000"/>
  <text x="120" y="93" fill="#000000" font-size="9" font-family="serif" font-style="italic" font-weight="bold" text-anchor="middle">u₁ + u₂ + u₃ = 0 ⇒ u₁ = u₂ = u₃ = 0</text>
  <text x="120" y="136" fill="#000000" font-size="8.5" font-family="sans-serif" text-anchor="middle">Zero-Vector Test: Unique representation of 0 guarantees direct sum</text>
</svg>""",
        "drawingCaption": "Zero-Vector Test: The only way to sum components to zero is if each individual component is zero",
        "coreTranslation": [
            "<strong>Master Theorem (Axler 1.44):</strong> The sum $U_1 + \\dots + U_m$ is a direct sum if and only if the only way to write the zero vector as a sum $u_1 + \\dots + u_m = 0$ (with $u_i \\in U_i$) is: $u_1 = u_2 = \\dots = u_m = 0$.",
            "<strong>Proof $(\\implies)$:</strong> If the sum is direct, representation of 0 is unique. Since $0 + \\dots + 0 = 0$, this must be the only representation.",
            "<strong>Proof $(\\impliedby)$:</strong> If $v = u_1 + \\dots + u_m = w_1 + \\dots + w_m$, subtracting gives $(u_1 - w_1) + \\dots + (u_m - w_m) = 0$. By hypothesis, each $u_i - w_i = 0 \\implies u_i = w_i$."
        ],
        "math": "$$U_1 \\oplus \\dots \\oplus U_m \\iff \\left( \\sum_{i=1}^m u_i = 0, \\; u_i \\in U_i \\implies u_1 = \\dots = u_m = 0 \\right)$$",
        "personalConnection": "Linear independence scaled up to entire rooms: no room's contents can be combined with other rooms to cancel out and leave an empty house.",
        "examTrap": "Always use the zero-vector criterion when testing 3 or more subspaces! It is universal, completely immune to pairwise intersection traps, and matches the definition of linear independence."
    },
    {
        "id": 20104,
        "subject": "LAA",
        "topicId": "01_Vector_Spaces_Subspaces_and_Direct_Sums",
        "topicTitle": "01 · Vector Spaces, Subspaces & Direct Sums",
        "cardNumber": "04",
        "category": "COUNTEREXAMPLE TRAPS",
        "highlighterClass": "highlight-rose",
        "title": "Exam Trap: Pairwise Disjoint ≠ Direct Sum",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <!-- 3 coplanar lines in R² -->
  <line x1="25" y1="75" x2="215" y2="75" stroke="#000000" stroke-width="1.8"/>
  <text x="215" y="87" fill="#000000" font-size="8.5" font-family="serif" font-style="italic">U₁ (x-axis)</text>
  <line x1="120" y1="130" x2="120" y2="18" stroke="#000000" stroke-width="1.8"/>
  <text x="120" y="14" fill="#000000" font-size="8.5" font-family="serif" font-style="italic" text-anchor="middle">U₂ (y-axis)</text>
  <line x1="50" y1="125" x2="190" y2="25" stroke="#000000" stroke-width="1.8" stroke-dasharray="4,3"/>
  <text x="195" y="25" fill="#000000" font-size="8.5" font-family="serif" font-style="italic">U₃ (y = x)</text>
  <circle cx="120" cy="75" r="4" fill="#000000"/>
  <text x="120" y="98" fill="#000000" font-size="8.5" font-family="sans-serif" font-weight="bold" text-anchor="middle">U_i ∩ U_j = {0} pair-wise, BUT sum is NOT direct!</text>
  <text x="120" y="138" fill="#000000" font-size="8.5" font-family="monospace" text-anchor="middle">(1,0) + (0,1) + (-1,-1) = (0,0)</text>
</svg>""",
        "drawingCaption": "Classic IISc Trap: Three lines in R² have pairwise trivial intersections, yet (1,1) + (-1,0) + (0,-1) = 0",
        "coreTranslation": [
            "<strong>The Classic Trap:</strong> In $\\mathbb{R}^2$, consider three distinct lines through the origin: $U_1 = \\{(x, 0)\\}$, $U_2 = \\{(0, y)\\}$, $U_3 = \\{(x, x)\\}$.",
            "Notice that $U_1 \\cap U_2 = \\{0\\}$, $U_1 \\cap U_3 = \\{0\\}$, and $U_2 \\cap U_3 = \\{0\\}$. They are strictly pairwise disjoint at the origin!",
            "YET $U_1 + U_2 + U_3$ is <strong>NOT a direct sum</strong>: $(1, 0) + (0, 1) + (-1, -1) = (0, 0)$ with non-zero vectors! Representation of zero is not unique."
        ],
        "math": "$$U_i \\cap U_j = \\{0\\} \\, (\\forall i \\ne j) \\; \\not\\!\\!\\implies U_1 + \\dots + U_m \\text{ is direct for } m \\ge 3$$",
        "personalConnection": "Three tripod legs that lie completely flat on the kitchen floor: each leg points in a different direction, but because they are all in the same 2D floor, they cannot support a 3D table.",
        "examTrap": "The correct intersection condition for $m \\ge 3$ subspaces is: $U_j \\cap \\left( \\sum_{i \\ne j} U_i \\right) = \\{0\\}$ for each $j$. Each subspace must intersect the sum of ALL other subspaces trivially."
    },
    {
        "id": 20105,
        "subject": "LAA",
        "topicId": "01_Vector_Spaces_Subspaces_and_Direct_Sums",
        "topicTitle": "01 · Vector Spaces, Subspaces & Direct Sums",
        "cardNumber": "05",
        "category": "DIMENSION THEOREMS",
        "highlighterClass": "highlight-violet",
        "title": "Dimension Formula for Subspace Sums",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <!-- Venn Subspace Dimension Overlap -->
  <circle cx="95" cy="65" r="45" fill="#f8fafc" stroke="#000000" stroke-width="1.8"/>
  <circle cx="145" cy="65" r="45" fill="#f8fafc" stroke="#000000" stroke-width="1.8"/>
  <!-- Overlap Region -->
  <path d="M 120 28 A 45 45 0 0 0 120 102 A 45 45 0 0 0 120 28 Z" fill="#e2e8f0" stroke="none"/>
  <circle cx="95" cy="65" r="45" fill="none" stroke="#000000" stroke-width="1.8"/>
  <circle cx="145" cy="65" r="45" fill="none" stroke="#000000" stroke-width="1.8"/>
  <text x="75" y="68" fill="#000000" font-size="9" font-family="serif" font-style="italic">dim U₁</text>
  <text x="165" y="68" fill="#000000" font-size="9" font-family="serif" font-style="italic">dim U₂</text>
  <text x="120" y="68" fill="#000000" font-size="8" font-family="serif" font-style="italic" text-anchor="middle">dim(U₁∩U₂)</text>
  <text x="120" y="125" fill="#000000" font-size="9" font-family="serif" font-style="italic" font-weight="bold" text-anchor="middle">dim(U₁ + U₂) = dim U₁ + dim U₂ - dim(U₁ ∩ U₂)</text>
</svg>""",
        "drawingCaption": "Dimension Formula: Overlap dim(U₁ ∩ U₂) is subtracted once to avoid double-counting basis elements",
        "coreTranslation": [
            "<strong>Theorem:</strong> For finite-dimensional subspaces $U_1, U_2 \\le V$: $\\dim(U_1 + U_2) = \\dim U_1 + \\dim U_2 - \\dim(U_1 \\cap U_2)$.",
            "<strong>Direct Sum Characterization:</strong> The sum is direct ($U_1 \\oplus U_2$) if and only if $\\dim(U_1 \\cap U_2) = 0$, which yields the additive formula: $\\dim(U_1 \\oplus U_2) = \\dim U_1 + \\dim U_2$.",
            "<strong>Proof Mechanism:</strong> Start with basis $\\{v_1, \\dots, v_k\\}$ of $U_1 \\cap U_2$. Extend to basis of $U_1$ and basis of $U_2$. The union of these extended bases forms a basis of $U_1 + U_2$."
        ],
        "math": "$$\\dim(U_1 + U_2) = \\dim U_1 + \\dim U_2 - \\dim(U_1 \\cap U_2) \\le \\dim U_1 + \\dim U_2$$",
        "personalConnection": "Inclusion-Exclusion for sets: $|A \\cup B| = |A| + |B| - |A \\cap B|$. If the sets share zero common elements, the total size is simply the sum of their individual sizes.",
        "examTrap": "If $\\dim(U_1) + \\dim(U_2) > \\dim(V)$, the subspaces MUST have a non-trivial intersection! E.g., two 2D planes in $\\mathbb{R}^3$ must intersect in at least a line: $\\dim(U_1 \\cap U_2) \\ge 2 + 2 - 3 = 1$."
    },
    {
        "id": 20106,
        "subject": "LAA",
        "topicId": "01_Vector_Spaces_Subspaces_and_Direct_Sums",
        "topicTitle": "01 · Vector Spaces, Subspaces & Direct Sums",
        "cardNumber": "06",
        "category": "WORKED BENCHMARK",
        "highlighterClass": "highlight-indigo",
        "title": "Worked Benchmark: Symmetric ⊕ Skew-Symmetric",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <rect x="25" y="20" width="190" height="105" rx="8" fill="#f8fafc" stroke="#000000" stroke-width="1.5"/>
  <text x="120" y="38" fill="#000000" font-size="10" font-family="serif" font-style="italic" font-weight="bold" text-anchor="middle">M_{n×n}(ℝ) = 𝒮_n ⊕ 𝒜_n</text>
  <!-- Matrix decomposition boxes -->
  <rect x="40" y="52" width="70" height="45" rx="4" fill="#f1f5f9" stroke="#000000" stroke-width="1.2"/>
  <text x="75" y="70" fill="#000000" font-size="8.5" font-family="sans-serif" font-weight="bold" text-anchor="middle">Symmetric</text>
  <text x="75" y="84" fill="#000000" font-size="8" font-family="serif" font-style="italic" text-anchor="middle">½(A + Aᵀ)</text>
  <text x="120" y="78" fill="#000000" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">⊕</text>
  <rect x="130" y="52" width="70" height="45" rx="4" fill="#f1f5f9" stroke="#000000" stroke-width="1.2"/>
  <text x="165" y="70" fill="#000000" font-size="8.5" font-family="sans-serif" font-weight="bold" text-anchor="middle">Skew-Symm</text>
  <text x="165" y="84" fill="#000000" font-size="8" font-family="serif" font-style="italic" text-anchor="middle">½(A - Aᵀ)</text>
  <text x="120" y="115" fill="#000000" font-size="8.5" font-family="monospace" text-anchor="middle">𝒮_n ∩ 𝒜_n = {0} ⇒ Direct Sum</text>
</svg>""",
        "drawingCaption": "Canonical Matrix Direct Sum: Every square matrix splits uniquely into symmetric and skew-symmetric parts",
        "coreTranslation": [
            "<strong>Problem:</strong> Prove $M_{n \\times n}(\\mathbb{R}) = \\mathcal{S}_n \\oplus \\mathcal{A}_n$, where $\\mathcal{S}_n = \\{A : A^T = A\\}$ and $\\mathcal{A}_n = \\{A : A^T = -A\\}$.",
            "<strong>Step 1 (Existence):</strong> For any $A \\in M_{n \\times n}$, write: $A = \\frac{A + A^T}{2} + \\frac{A - A^T}{2}$. $\\frac{A + A^T}{2} \\in \\mathcal{S}_n$ and $\\frac{A - A^T}{2} \\in \\mathcal{A}_n$. Thus $M_{n \\times n} = \\mathcal{S}_n + \\mathcal{A}_n$.",
            "<strong>Step 2 (Uniqueness / Intersection):</strong> Let $A \\in \\mathcal{S}_n \\cap \\mathcal{A}_n$. Then $A^T = A$ and $A^T = -A \\implies A = -A \\implies 2A = 0 \\implies A = 0$. Hence $\\mathcal{S}_n \\cap \\mathcal{A}_n = \\{0\\}$, proving direct sum!"
        ],
        "math": "$$A = \\underbrace{\\frac{A + A^T}{2}}_{\\in \\mathcal{S}_n} + \\underbrace{\\frac{A - A^T}{2}}_{\\in \\mathcal{A}_n}, \\quad \\mathcal{S}_n \\cap \\mathcal{A}_n = \\{0\\} \\implies M_n = \\mathcal{S}_n \\oplus \\mathcal{A}_n$$",
        "personalConnection": "Decomposing any musical sound wave into an even symmetric cosine wave and an odd antisymmetric sine wave. Both components are completely orthogonal and span the full sound space.",
        "examTrap": "Check the dimensions: $\\dim \\mathcal{S}_n = \\frac{n(n+1)}{2}$, $\\dim \\mathcal{A}_n = \\frac{n(n-1)}{2}$. Their sum is $\\frac{n(n+1)}{2} + \\frac{n(n-1)}{2} = n^2 = \\dim M_{n \\times n}$, confirming the direct sum dimension theorem."
    }
]

# =============================================================================
# StoMA (Stochastic Models and Applications - E0 226)
# =============================================================================
stoma_cards = [
    {
        "id": 30101,
        "subject": "StoMA",
        "topicId": "01_Probability_Spaces_Axioms_and_Continuity_of_Probability",
        "topicTitle": "01 · Probability Spaces & Continuity",
        "cardNumber": "01",
        "category": "MEASURE & PROBABILITY",
        "highlighterClass": "highlight-cyan",
        "title": "Probability Space Triple (Ω, F, P)",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-stoma1" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- Sample Space Universe Omega -->
  <rect x="25" y="20" width="190" height="105" rx="8" fill="#f8fafc" stroke="#000000" stroke-width="1.5"/>
  <text x="35" y="36" fill="#000000" font-size="10" font-family="serif" font-style="italic" font-weight="bold">Sample Space Ω</text>
  <!-- Sigma-algebra Event A -->
  <ellipse cx="90" cy="75" rx="45" ry="30" fill="#f1f5f9" stroke="#000000" stroke-width="1.8"/>
  <text x="90" y="78" fill="#000000" font-size="9" font-family="serif" font-style="italic" font-weight="bold" text-anchor="middle">Event A ∈ ℱ</text>
  <!-- Probability Measure P Arrow to [0, 1] -->
  <line x1="140" y1="75" x2="185" y2="75" stroke="#000000" stroke-width="1.8" marker-end="url(#arr-stoma1)"/>
  <text x="162" y="68" fill="#000000" font-size="9" font-family="serif" font-style="italic" text-anchor="middle">ℙ(A)</text>
  <text x="195" y="78" fill="#000000" font-size="9" font-family="sans-serif">[0, 1]</text>
  <text x="120" y="136" fill="#000000" font-size="8.5" font-family="sans-serif" text-anchor="middle">Probability Triple: (Ω, ℱ, ℙ)</text>
</svg>""",
        "drawingCaption": "Probability Triple: Sample space Ω, σ-algebra of observable events F, and measure P mapping to [0, 1]",
        "coreTranslation": [
            "A <strong>Probability Space</strong> is a rigorous mathematical triple $(\\Omega, \\mathcal{F}, \\mathbb{P})$:",
            "<strong>1. Sample Space $\\Omega$:</strong> The set of all possible outcomes of an experiment.",
            "<strong>2. $\\sigma$-Algebra $\\mathcal{F}$ (Events):</strong> A collection of subsets of $\\Omega$ containing $\\emptyset$, closed under complements ($A \\in \\mathcal{F} \\implies A^c \\in \\mathcal{F}$), and closed under <strong>countable unions</strong> ($A_i \\in \\mathcal{F} \\implies \\bigcup_{i=1}^\\infty A_i \\in \\mathcal{F}$).",
            "<strong>3. Probability Measure $\\mathbb{P}$:</strong> A function $\\mathbb{P}: \\mathcal{F} \\to [0, 1]$ satisfying Kolmogorov's axioms."
        ],
        "math": "$$\\mathbb{P}: \\mathcal{F} \\to [0, 1] \\quad \\text{on } (\\Omega, \\mathcal{F}), \\quad \\Omega \\in \\mathcal{F}, \\quad A \\in \\mathcal{F} \\implies A^c \\in \\mathcal{F}$$",
        "personalConnection": "A dartboard: $\\Omega$ is the wooden board. $\\mathcal{F}$ is the rulebook defining which regions you can score points on (bullseye, rings). $\\mathbb{P}(A)$ is your probability of hitting area $A$.",
        "examTrap": "Why do we need a $\\sigma$-algebra rather than the entire power set $2^\\Omega$? Because on uncountably infinite spaces (like $\\mathbb{R}$), non-measurable sets (e.g. Vitali sets) exist where probabilities CANNOT be consistently assigned!"
    },
    {
        "id": 30102,
        "subject": "StoMA",
        "topicId": "01_Probability_Spaces_Axioms_and_Continuity_of_Probability",
        "topicTitle": "01 · Probability Spaces & Continuity",
        "cardNumber": "02",
        "category": "KOLMOGOROV AXIOMS",
        "highlighterClass": "highlight-amber",
        "title": "Kolmogorov’s Three Axioms of Probability",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <!-- 3 disjoint event bubbles -->
  <circle cx="60" cy="65" r="25" fill="#f1f5f9" stroke="#000000" stroke-width="1.8"/>
  <text x="60" y="68" fill="#000000" font-size="9" font-family="serif" font-style="italic" text-anchor="middle">A₁</text>
  <circle cx="120" cy="65" r="25" fill="#f1f5f9" stroke="#000000" stroke-width="1.8"/>
  <text x="120" y="68" fill="#000000" font-size="9" font-family="serif" font-style="italic" text-anchor="middle">A₂</text>
  <circle cx="180" cy="65" r="25" fill="#f1f5f9" stroke="#000000" stroke-width="1.8"/>
  <text x="180" y="68" fill="#000000" font-size="9" font-family="serif" font-style="italic" text-anchor="middle">A₃</text>
  <text x="120" y="115" fill="#000000" font-size="9" font-family="serif" font-style="italic" font-weight="bold" text-anchor="middle">Countable Additivity: ℙ(⋃ A_i) = ∑ ℙ(A_i)</text>
  <text x="120" y="134" fill="#000000" font-size="8.5" font-family="sans-serif" text-anchor="middle">Pairwise disjoint events: A_i ∩ A_j = ∅ (i ≠ j)</text>
</svg>""",
        "drawingCaption": "Axiom 3: For mutually disjoint events A_i ∩ A_j = ∅, the probability of the union equals the sum of probabilities",
        "coreTranslation": [
            "<strong>Axiom 1 (Non-negativity):</strong> For every event $A \\in \\mathcal{F}$, $\\mathbb{P}(A) \\ge 0$.",
            "<strong>Axiom 2 (Normalization):</strong> The entire sample space has certainty: $\\mathbb{P}(\\Omega) = 1$.",
            "<strong>Axiom 3 (Countable Additivity):</strong> For any sequence of pairwise disjoint events $A_1, A_2, \\dots$ ($A_i \\cap A_j = \\emptyset$ for $i \\ne j$): $\\mathbb{P}\\left( \\bigcup_{i=1}^\\infty A_i \\right) = \\sum_{i=1}^\\infty \\mathbb{P}(A_i)$.",
        ],
        "math": "$$\\mathbb{P}(A) \\ge 0, \\quad \\mathbb{P}(\\Omega) = 1, \\quad \\mathbb{P}\\left(\\bigcup_{i=1}^\\infty A_i\\right) = \\sum_{i=1}^\\infty \\mathbb{P}(A_i) \\; (A_i \\cap A_j = \\emptyset)$$",
        "personalConnection": "Pouring a litre bottle of milk into mutually separate teacups: the total volume of milk across all cups is the sum of the volumes in each cup; no milk is created or destroyed.",
        "examTrap": "FINITE additivity ($\\mathbb{P}(A \\cup B) = \\mathbb{P}(A) + \\mathbb{P}(B)$) is NOT enough! Countable additivity is strictly required to prove limit theorems and continuity of probability."
    },
    {
        "id": 30103,
        "subject": "StoMA",
        "topicId": "01_Probability_Spaces_Axioms_and_Continuity_of_Probability",
        "topicTitle": "01 · Probability Spaces & Continuity",
        "cardNumber": "03",
        "category": "LIMIT THEOREMS",
        "highlighterClass": "highlight-emerald",
        "title": "Continuity of Probability (Up & Down Limits)",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <!-- Concentric expanding rings A_n -->
  <circle cx="120" cy="65" r="18" fill="none" stroke="#000000" stroke-width="1.2"/>
  <text x="120" y="68" fill="#000000" font-size="8" font-family="serif" font-style="italic" text-anchor="middle">A₁</text>
  <circle cx="120" cy="65" r="32" fill="none" stroke="#000000" stroke-width="1.5"/>
  <text x="120" y="44" fill="#000000" font-size="8" font-family="serif" font-style="italic" text-anchor="middle">A₂</text>
  <circle cx="120" cy="65" r="48" fill="none" stroke="#000000" stroke-width="1.8"/>
  <text x="120" y="28" fill="#000000" font-size="8.5" font-family="serif" font-style="italic" font-weight="bold" text-anchor="middle">A_n ↑ A</text>
  <text x="120" y="125" fill="#000000" font-size="9" font-family="serif" font-style="italic" font-weight="bold" text-anchor="middle">Continuity: lim ℙ(A_n) = ℙ(lim A_n)</text>
  <text x="120" y="138" fill="#000000" font-size="8.5" font-family="sans-serif" text-anchor="middle">Increasing sequence: A₁ ⊂ A₂ ⊂ A₃ ...</text>
</svg>""",
        "drawingCaption": "Continuity from below: Expanding sequence of events A₁ ⊂ A₂ ⊂ ... whose probabilities limit to P(A)",
        "coreTranslation": [
            "<strong>Continuity from Below:</strong> If $A_1 \\subset A_2 \\subset A_3 \\subset \\dots$ is an increasing sequence of events with limit $A = \\bigcup_{n=1}^\\infty A_n$ (denoted $A_n \\uparrow A$), then: $\\lim_{n \\to \\infty} \\mathbb{P}(A_n) = \\mathbb{P}(A)$.",
            "<strong>Continuity from Above:</strong> If $B_1 \\supset B_2 \\supset B_3 \\dots$ is a decreasing sequence of events with limit $B = \\bigcap_{n=1}^\\infty B_n$ (denoted $B_n \\downarrow B$), then: $\\lim_{n \\to \\infty} \\mathbb{P}(B_n) = \\mathbb{P}(B)$.",
            "<strong>Proof Core:</strong> Partition $A$ into disjoint rings: $C_1 = A_1$, $C_k = A_k \\setminus A_{k-1}$. Then apply Kolmogorov's countable additivity to the disjoint sum: $\\mathbb{P}(A) = \\sum_{k=1}^\\infty \\mathbb{P}(C_k) = \\lim_{n\\to\\infty} \\sum_{k=1}^n \\mathbb{P}(C_k) = \\lim \\mathbb{P}(A_n)$."
        ],
        "math": "$$A_n \\uparrow A \\implies \\mathbb{P}(A) = \\lim_{n\\to\\infty} \\mathbb{P}(A_n), \\quad B_n \\downarrow B \\implies \\mathbb{P}(B) = \\lim_{n\\to\\infty} \\mathbb{P}(B_n)$$",
        "personalConnection": "Blowing air into a spherical balloon: as the volume of air inside the balloon expands smoothly toward its maximum burst capacity, the surface area approaches the limit continuously without teleporting.",
        "examTrap": "Continuity of probability is mathematically EQUIVALENT to countable additivity (assuming finite additivity). If a measure fails countable additivity, continuity of probability fails immediately."
    },
    {
        "id": 30104,
        "subject": "StoMA",
        "topicId": "01_Probability_Spaces_Axioms_and_Continuity_of_Probability",
        "topicTitle": "01 · Probability Spaces & Continuity",
        "cardNumber": "04",
        "category": "PROBABILITY INEQUALITIES",
        "highlighterClass": "highlight-violet",
        "title": "Boole’s Inequality & Bonferroni Bounds",
        "textbookImg": "assets/stoma_fig2_venn.png",
        "textbookRef": "Hoel, Port, Stone, Intro to Probability, Fig. 2 (p. 23)",
        "drawingCaption": "Hoel-Port-Stone Fig. 2: Partition of A ∪ B into disjoint regions A ∩ Bᶜ, A ∩ B, Aᶜ ∩ B",
        "drawingSvg": "",
        "coreTranslation": [
            "<strong>Boole's Inequality (Countable Subadditivity):</strong> For ANY sequence of events $A_1, A_2, \\dots$ (disjoint or overlapping): $\\mathbb{P}\\left( \\bigcup_{i=1}^\\infty A_i \\right) \\le \\sum_{i=1}^\\infty \\mathbb{P}(A_i)$.",
            "<strong>Bonferroni Bounds:</strong> Truncating the inclusion-exclusion series produces alternating upper and lower bounds:",
            "$\\mathbb{P}\\left( \\bigcup_{i=1}^n A_i \\right) \\ge \\sum \\mathbb{P}(A_i) - \\sum_{i < j} \\mathbb{P}(A_i \\cap A_j)$, and $\\le$ the 3-term sum."
        ],
        "math": "$$\\mathbb{P}\\left( \\bigcup_{i=1}^\\infty A_i \\right) \\le \\sum_{i=1}^\\infty \\mathbb{P}(A_i), \\quad \\mathbb{P}(A \\cup B) = \\mathbb{P}(A) + \\mathbb{P}(B) - \\mathbb{P}(A \\cap B)$$",
        "personalConnection": "Purchasing multiple lottery tickets: your probability of winning on AT LEAST one ticket cannot exceed the sum of the individual ticket winning probabilities, because overlapping wins don't multiply your chances.",
        "examTrap": "Boole's inequality requires NO assumption of independence or disjointness! It holds universally for arbitrary events, making it the most versatile bounding tool in proof questions."
    },
    {
        "id": 30105,
        "subject": "StoMA",
        "topicId": "01_Probability_Spaces_Axioms_and_Continuity_of_Probability",
        "topicTitle": "01 · Probability Spaces & Continuity",
        "cardNumber": "05",
        "category": "INCLUSION-EXCLUSION",
        "highlighterClass": "highlight-indigo",
        "title": "General Inclusion-Exclusion Principle",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <!-- 3-set Venn Diagram -->
  <circle cx="100" cy="55" r="32" fill="#f8fafc" stroke="#000000" stroke-width="1.5"/>
  <circle cx="140" cy="55" r="32" fill="#f8fafc" stroke="#000000" stroke-width="1.5"/>
  <circle cx="120" cy="85" r="32" fill="#f8fafc" stroke="#000000" stroke-width="1.5"/>
  <circle cx="120" cy="65" r="4" fill="#000000"/>
  <text x="120" y="68" fill="#ffffff" font-size="6" font-family="monospace" text-anchor="middle">+</text>
  <text x="80" y="48" fill="#000000" font-size="8" font-family="serif" font-style="italic">A₁</text>
  <text x="155" y="48" fill="#000000" font-size="8" font-family="serif" font-style="italic">A₂</text>
  <text x="120" y="110" fill="#000000" font-size="8" font-family="serif" font-style="italic" text-anchor="middle">A₃</text>
  <text x="120" y="128" fill="#000000" font-size="8.5" font-family="sans-serif" font-weight="bold" text-anchor="middle">Alternating signs: + Singles - Pairs + Triples</text>
  <text x="120" y="139" fill="#000000" font-size="8" font-family="monospace" text-anchor="middle">ℙ(∪ A_i) = S₁ - S₂ + S₃ - ...</text>
</svg>""",
        "drawingCaption": "3-Set Inclusion-Exclusion: Add single probabilities, subtract double intersections, add triple intersection back",
        "coreTranslation": [
            "For $n$ arbitrary events $A_1, \\dots, A_n$, the probability of their union is given by the exact alternating sum:",
            "$$\\mathbb{P}\\left( \\bigcup_{i=1}^n A_i \\right) = \\sum_{k=1}^n (-1)^{k-1} S_k, \\quad \\text{where } S_k = \\sum_{1 \\le i_1 < \\dots < i_k \\le n} \\mathbb{P}(A_{i_1} \\cap \\dots \\cap A_{i_k})$$",
            "For $n = 3$: $\\mathbb{P}(A_1 \\cup A_2 \\cup A_3) = \\sum \\mathbb{P}(A_i) - \\sum \\mathbb{P}(A_i \\cap A_j) + \\mathbb{P}(A_1 \\cap A_2 \\cap A_3)$."
        ],
        "math": "$$\\mathbb{P}\\left(\\bigcup_{i=1}^n A_i\\right) = \\sum_{i} \\mathbb{P}(A_i) - \\sum_{i<j} \\mathbb{P}(A_i \\cap A_j) + \\dots + (-1)^{n-1} \\mathbb{P}\\left(\\bigcap_{i=1}^n A_i\\right)$$",
        "personalConnection": "Adjusting accounting ledger double-counts: adding items from all departments overcounts shared projects, so you subtract joint projects, but now projects shared by three groups were removed too many times, so you add them back.",
        "examTrap": "Remember that the sign of the full intersection $\\mathbb{P}(\\bigcap_{i=1}^n A_i)$ is $(-1)^{n-1}$. For $n=2$, it's negative $(-)$; for $n=3$, it's positive $(+)$; for $n=4$, it's negative $(-)$."
    },
    {
        "id": 30106,
        "subject": "StoMA",
        "topicId": "01_Probability_Spaces_Axioms_and_Continuity_of_Probability",
        "topicTitle": "01 · Probability Spaces & Continuity",
        "cardNumber": "06",
        "category": "WORKED BENCHMARK",
        "highlighterClass": "highlight-rose",
        "title": "Worked Benchmark: Infinite Coin Toss Limit",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-stoma6" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <line x1="25" y1="75" x2="215" y2="75" stroke="#000000" stroke-width="1.2" marker-end="url(#arr-stoma6)"/>
  <text x="215" y="88" fill="#000000" font-size="9" font-family="serif" font-style="italic">n</text>
  <!-- Decreasing probabilities -->
  <circle cx="50" cy="75" r="3.5" fill="#000000"/>
  <text x="50" y="60" fill="#000000" font-size="8.5" font-family="monospace" text-anchor="middle">(½)¹</text>
  <circle cx="90" cy="75" r="3.5" fill="#000000"/>
  <text x="90" y="60" fill="#000000" font-size="8.5" font-family="monospace" text-anchor="middle">(½)²</text>
  <circle cx="130" cy="75" r="3.5" fill="#000000"/>
  <text x="130" y="60" fill="#000000" font-size="8.5" font-family="monospace" text-anchor="middle">(½)³</text>
  <circle cx="175" cy="75" r="3.5" fill="#000000"/>
  <text x="175" y="60" fill="#000000" font-size="8.5" font-family="monospace" text-anchor="middle">(½)ⁿ → 0</text>
  <text x="120" y="115" fill="#000000" font-size="9" font-family="serif" font-style="italic" font-weight="bold" text-anchor="middle">ℙ(Never Toss Tails) = lim (½)ⁿ = 0</text>
  <text x="120" y="132" fill="#000000" font-size="8.5" font-family="sans-serif" text-anchor="middle">Decreasing sequence of events: B_n ↓ ∅</text>
</svg>""",
        "drawingCaption": "Worked Continuity Proof: Decreasing event sequence B_n = {First n tosses are all Heads} limits to probability 0",
        "coreTranslation": [
            "<strong>Problem:</strong> A fair coin is tossed infinitely many times. Prove that the probability of NEVER getting Tails is 0.",
            "<strong>Step 1 (Formulate Events):</strong> Let $B_n = \\{\\text{first } n \\text{ tosses are all Heads}\\}$. Clearly $B_{n+1} \\subset B_n$, so $\\{B_n\\}$ is a decreasing sequence.",
            "<strong>Step 2 (Intersection Event):</strong> The event $B = \\bigcap_{n=1}^\\infty B_n = \\{\\text{all infinite tosses are Heads}\\}$.",
            "<strong>Step 3 (Continuity from Above):</strong> $\\mathbb{P}(B) = \\lim_{n\\to\\infty} \\mathbb{P}(B_n) = \\lim_{n\\to\\infty} (1/2)^n = 0$. Hence almost surely, Tails will eventually appear!"
        ],
        "math": "$$B_n \\downarrow B \\implies \\mathbb{P}(B) = \\lim_{n\\to\\infty} \\mathbb{P}(B_n) = \\lim_{n\\to\\infty} \\left(\\frac{1}{2}\\right)^n = 0$$",
        "personalConnection": "Rolling a die repeatedly: the probability of rolling forever without ever seeing a 6 is an infinite decreasing chain $(5/6)^n$, which decays to zero with absolute certainty.",
        "examTrap": "An event having probability 0 does NOT mean it is impossible! Flipping infinite heads is an element of $\\Omega$ (it is a valid sequence $HHHH\\dots$), but its measure $\\mathbb{P}$ is zero."
    }
]

# =============================================================================
# DIP (Digital Image Processing - E9 241)
# =============================================================================
dip_cards = [
    {
        "id": 40101,
        "subject": "DIP",
        "topicId": "01_Image_Formation_Camera_Geometry_and_Transformations",
        "topicTitle": "01 · Image Formation & Transformations",
        "cardNumber": "01",
        "category": "CAMERA GEOMETRY",
        "highlighterClass": "highlight-cyan",
        "title": "Pinhole Camera Model & Perspective",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-dip1" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- Optical Axis -->
  <line x1="20" y1="75" x2="220" y2="75" stroke="#000000" stroke-width="1.2" stroke-dasharray="3,3"/>
  <!-- Pinhole Barrier with aperture C -->
  <line x1="120" y1="20" x2="120" y2="70" stroke="#000000" stroke-width="2.5"/>
  <line x1="120" y1="80" x2="120" y2="130" stroke="#000000" stroke-width="2.5"/>
  <circle cx="120" cy="75" r="3.5" fill="#000000"/>
  <text x="120" y="65" fill="#000000" font-size="8.5" font-family="serif" font-style="italic" text-anchor="middle">Pinhole C</text>
  <!-- 3D Object Point (X, Y, Z) -->
  <line x1="200" y1="75" x2="200" y2="35" stroke="#000000" stroke-width="2.2" marker-end="url(#arr-dip1)"/>
  <circle cx="200" cy="35" r="3" fill="#000000"/>
  <text x="200" y="28" fill="#000000" font-size="8.5" font-family="serif" font-style="italic" text-anchor="middle">(X, Y, Z)</text>
  <!-- Ray through pinhole -->
  <line x1="200" y1="35" x2="40" y2="115" stroke="#000000" stroke-width="1.2" stroke-dasharray="2,2"/>
  <!-- Inverted Image Plane -->
  <line x1="40" y1="75" x2="40" y2="115" stroke="#000000" stroke-width="2.2" marker-end="url(#arr-dip1)"/>
  <circle cx="40" cy="115" r="3" fill="#000000"/>
  <text x="40" y="128" fill="#000000" font-size="8.5" font-family="serif" font-style="italic" text-anchor="middle">(-f X/Z)</text>
  <text x="80" y="87" fill="#000000" font-size="8.5" font-family="serif" font-style="italic">f</text>
  <text x="160" y="87" fill="#000000" font-size="8.5" font-family="serif" font-style="italic">Z</text>
</svg>""",
        "drawingCaption": "Pinhole Model: Similar triangles project 3D point (X, Y, Z) into inverted 2D image coordinates x = -f(X/Z)",
        "coreTranslation": [
            "In the standard pinhole camera, light rays pass through optical center $C = (0, 0, 0)$ and intersect an image plane located at distance $f$ (focal length).",
            "<strong>Similar Triangles Geometry:</strong> By geometry of similar triangles, a 3D point $(X, Y, Z)$ projects to inverted image coordinates: $x = -f \\frac{X}{Z}, \\quad y = -f \\frac{Y}{Z}$.",
            "In virtual camera models, the image plane is placed in FRONT of the pinhole at $+f$ to eliminate the negative sign, yielding the standard non-inverted projection: $x = f \\frac{X}{Z}$."
        ],
        "math": "$$x = f \\frac{X}{Z}, \\quad y = f \\frac{Y}{Z} \\quad (\\text{Perspective Division by Depth } Z)$$",
        "personalConnection": "Holding your thumb in front of your face: the closer your thumb is to your eye (small depth $Z$), the more massive it appears, completely blocking a building in the distance.",
        "examTrap": "Perspective projection is NON-LINEAR in Cartesian coordinates because of the division by $Z$! To make it linear, we MUST convert to <strong>homogeneous coordinates</strong>."
    },
    {
        "id": 40102,
        "subject": "DIP",
        "topicId": "01_Image_Formation_Camera_Geometry_and_Transformations",
        "topicTitle": "01 · Image Formation & Transformations",
        "cardNumber": "02",
        "category": "PROJECTIVE GEOMETRY",
        "highlighterClass": "highlight-amber",
        "title": "Camera Matrix: x = K [R | t] X",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-dip2" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- Flow: World -> Camera -> Pixel -->
  <rect x="25" y="45" width="55" height="50" rx="6" fill="#f8fafc" stroke="#000000" stroke-width="1.5"/>
  <text x="52" y="66" fill="#000000" font-size="8.5" font-family="sans-serif" font-weight="bold" text-anchor="middle">World 3D</text>
  <text x="52" y="82" fill="#000000" font-size="8" font-family="serif" font-style="italic" text-anchor="middle">X_w ∈ ℝ⁴</text>
  <line x1="80" y1="70" x2="105" y2="70" stroke="#000000" stroke-width="1.8" marker-end="url(#arr-dip2)"/>
  <text x="92" y="62" fill="#000000" font-size="8" font-family="serif" font-style="italic" text-anchor="middle">[R|t]</text>
  <rect x="105" y="45" width="55" height="50" rx="6" fill="#f1f5f9" stroke="#000000" stroke-width="1.5"/>
  <text x="132" y="66" fill="#000000" font-size="8.5" font-family="sans-serif" font-weight="bold" text-anchor="middle">Camera 3D</text>
  <text x="132" y="82" fill="#000000" font-size="8" font-family="serif" font-style="italic" text-anchor="middle">X_c ∈ ℝ³</text>
  <line x1="160" y1="70" x2="185" y2="70" stroke="#000000" stroke-width="1.8" marker-end="url(#arr-dip2)"/>
  <text x="172" y="62" fill="#000000" font-size="8" font-family="serif" font-style="italic" text-anchor="middle">K</text>
  <rect x="185" y="45" width="45" height="50" rx="6" fill="#ffffff" stroke="#000000" stroke-width="1.8"/>
  <text x="207" y="66" fill="#000000" font-size="8.5" font-family="sans-serif" font-weight="bold" text-anchor="middle">Pixel</text>
  <text x="207" y="82" fill="#000000" font-size="8" font-family="serif" font-style="italic" text-anchor="middle">x ∈ ℝ³</text>
  <text x="120" y="125" fill="#000000" font-size="9" font-family="serif" font-style="italic" font-weight="bold" text-anchor="middle">x = K [R | t] X  (Extrinsics then Intrinsics)</text>
</svg>""",
        "drawingCaption": "Full Projection Pipeline: Extrinsics [R|t] map world to camera; Intrinsics K map camera to 2D pixels",
        "coreTranslation": [
            "In homogeneous coordinates, perspective projection is represented by a single $3 \\times 4$ projection matrix $P$:",
            "$$\\mathbf{x} = P \\mathbf{X} = K [R \\mid t] \\mathbf{X}, \\quad \\text{where } \\mathbf{x} = [u, v, 1]^T, \\; \\mathbf{X} = [X, Y, Z, 1]^T$$",
            "<strong>Extrinsic Matrix $[R \\mid t]$ ($3 \\times 4$):</strong> Represents the rigid body camera pose (rotation $R \\in SO(3)$ and translation $t \\in \\mathbb{R}^3$) relative to the world frame.",
            "<strong>Intrinsic Matrix $K$ ($3 \\times 3$):</strong> Encodes the internal geometric calibration of the optical sensor."
        ],
        "math": "$$\\begin{bmatrix} u \\\\ v \\\\ 1 \\end{bmatrix} \\sim \\begin{bmatrix} f_x & s & c_x \\\\ 0 & f_y & c_y \\\\ 0 & 0 & 1 \\end{bmatrix} \\begin{bmatrix} r_{11} & r_{12} & r_{13} & t_x \\\\ r_{21} & r_{22} & r_{23} & t_y \\\\ r_{31} & r_{32} & r_{33} & t_z \\end{bmatrix} \\begin{bmatrix} X \\\\ Y \\\\ Z \\\\ 1 \\end{bmatrix}$$",
        "personalConnection": "Filming a movie scene: the tripod position and swivel angle are the extrinsic parameters $[R|t]$. The lens choice (wide-angle vs telephoto) and camera sensor resolution are the intrinsic parameters $K$.",
        "examTrap": "The equality holds UP TO SCALE (indicated by $\\sim$)! You must divide the resulting homogeneous vector by its third coordinate: $u = \\tilde{u}/\\tilde{w}, v = \\tilde{v}/\\tilde{w}$ to obtain actual pixel coordinates."
    },
    {
        "id": 40103,
        "subject": "DIP",
        "topicId": "01_Image_Formation_Camera_Geometry_and_Transformations",
        "topicTitle": "01 · Image Formation & Transformations",
        "cardNumber": "03",
        "category": "CAMERA INTRINSICS",
        "highlighterClass": "highlight-emerald",
        "title": "Intrinsic Calibration Matrix K",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <!-- Sensor array rectangle with principal point -->
  <rect x="40" y="25" width="160" height="90" rx="4" fill="#f8fafc" stroke="#000000" stroke-width="1.8"/>
  <!-- Sensor pixel grid ticks -->
  <line x1="40" y1="70" x2="200" y2="70" stroke="#000000" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="120" y1="25" x2="120" y2="115" stroke="#000000" stroke-width="1" stroke-dasharray="3,3"/>
  <!-- Principal Point (c_x, c_y) -->
  <circle cx="135" cy="75" r="4" fill="#000000"/>
  <text x="145" y="88" fill="#000000" font-size="8.5" font-family="serif" font-style="italic">(c_x, c_y) Principal Point</text>
  <!-- Focal lengths f_x and f_y -->
  <line x1="40" y1="125" x2="100" y2="125" stroke="#000000" stroke-width="2"/>
  <text x="70" y="137" fill="#000000" font-size="8.5" font-family="serif" font-style="italic" text-anchor="middle">f_x = f · m_x</text>
</svg>""",
        "drawingCaption": "Sensor Geometry: Focal lengths f_x, f_y in pixels and optical center (c_x, c_y) offset from sensor corner",
        "coreTranslation": [
            "The upper-triangular <strong>Intrinsic Calibration Matrix $K$</strong> has 5 degrees of freedom:",
            "$$K = \\begin{bmatrix} f_x & s & c_x \\\\ 0 & f_y & c_y \\\\ 0 & 0 & 1 \\end{bmatrix}$$",
            "<strong>Focal Lengths $f_x, f_y$:</strong> $f_x = f \\cdot m_x, f_y = f \\cdot m_y$, where $m_x, m_y$ are pixels per millimeter. For square pixels, $f_x = f_y$.",
            "<strong>Principal Point $(c_x, c_y)$:</strong> Pixel coordinates where the camera's optical axis pierces the sensor. <strong>Skew $s$:</strong> Non-zero only if sensor axes are not orthogonal (usually $s = 0$)."
        ],
        "math": "$$K = \\begin{bmatrix} f_x & 0 & c_x \\\\ 0 & f_y & c_y \\\\ 0 & 0 & 1 \\end{bmatrix} \\quad (5 \\text{ Intrinsic Parameters for General CCD})$$",
        "personalConnection": "Measuring a printed photo with a misaligned ruler: $f_x, f_y$ scale millimeter distances into pixel tick marks, while $(c_x, c_y)$ shifts the ruler's zero-mark to the center of the photo.",
        "examTrap": "Never assume the principal point is at $(0, 0)$! In image coordinates, $(0,0)$ is the TOP-LEFT corner of the image. For a $1920 \\times 1080$ sensor, the principal point is approximately $(960, 540)$."
    },
    {
        "id": 40104,
        "subject": "DIP",
        "topicId": "01_Image_Formation_Camera_Geometry_and_Transformations",
        "topicTitle": "01 · Image Formation & Transformations",
        "cardNumber": "04",
        "category": "2D TRANSFORMATIONS",
        "highlighterClass": "highlight-violet",
        "title": "2D Transformation Hierarchy: Euclidean to Projective",
        "textbookImg": "assets/dip_table2_3_affine.png",
        "textbookRef": "Gonzalez & Woods (4th ed), Table 2.3 (p. 104)",
        "drawingCaption": "Gonzalez & Woods Table 2.3: Affine Transformation Matrices (Identity, Scaling, Rotation, Translation, Shear)",
        "drawingSvg": "",
        "coreTranslation": [
            "<strong>1. Euclidean (Isometry, 3 DOF):</strong> Rotation + Translation ($R, t$). Preserves lengths, angles, and area.",
            "<strong>2. Similarity (4 DOF):</strong> Euclidean + Uniform Scale ($s R, t$). Preserves angles (shapes) and length ratios.",
            "<strong>3. Affine (6 DOF):</strong> Parallelism preserved; lines remain parallel. Preserves ratio of areas and parallel lengths.",
            "<strong>4. Projective (Homography, 8 DOF):</strong> Collinearity preserved (straight lines remain straight). Parallel lines converge to vanishing points!"
        ],
        "math": "$$H_{\\text{proj}} = \\begin{bmatrix} h_{11} & h_{12} & h_{13} \\\\ h_{21} & h_{22} & h_{23} \\\\ h_{31} & h_{32} & h_{33} \\end{bmatrix} \\quad (8 \\text{ Degrees of Freedom Up to Scale})$$",
        "personalConnection": "Looking at train tracks: in world coordinates, the tracks are Euclidean (parallel). In the camera's photo, perspective homography causes the parallel rails to intersect at a vanishing point on the horizon.",
        "examTrap": "An Affine transformation has $h_{31} = 0, h_{32} = 0, h_{33} = 1$. The bottom row $[0, 0, 1]$ is what preserves parallel lines! When $[h_{31}, h_{32}] \\ne [0, 0]$, lines converge."
    },
    {
        "id": 40105,
        "subject": "DIP",
        "topicId": "01_Image_Formation_Camera_Geometry_and_Transformations",
        "topicTitle": "01 · Image Formation & Transformations",
        "cardNumber": "05",
        "category": "IMAGE WARPING",
        "highlighterClass": "highlight-indigo",
        "title": "Forward vs. Inverse Warping & Bilinear Interpolation",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-dip5" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- Forward Warping Grid with Holes -->
  <rect x="25" y="30" width="80" height="70" fill="none" stroke="#000000" stroke-width="1.2" stroke-dasharray="3,3"/>
  <circle cx="45" cy="50" r="3" fill="#000000"/>
  <circle cx="85" cy="60" r="3" fill="#000000"/>
  <circle cx="65" cy="85" r="3" fill="#000000"/>
  <text x="65" y="115" fill="#000000" font-size="8.5" font-family="sans-serif" text-anchor="middle">Forward: Holes &amp; Clumping</text>
  <!-- Inverse Warping Grid -->
  <rect x="135" y="30" width="80" height="70" fill="#f1f5f9" stroke="#000000" stroke-width="1.5"/>
  <circle cx="175" cy="65" r="3.5" fill="#000000"/>
  <path d="M 175 65 Q 140 35 100 45" fill="none" stroke="#000000" stroke-width="1.5" marker-end="url(#arr-dip5)"/>
  <text x="175" y="115" fill="#000000" font-size="8.5" font-family="sans-serif" font-weight="bold" text-anchor="middle">Inverse: Pull via H⁻¹</text>
  <text x="120" y="135" fill="#000000" font-size="8.5" font-family="sans-serif" text-anchor="middle">Guarantees every output pixel is interpolated</text>
</svg>""",
        "drawingCaption": "Warping: Forward mapping leaves unsightly holes and moiré artifacts; Inverse mapping guarantees every output pixel is filled",
        "coreTranslation": [
            "<strong>Forward Mapping:</strong> Iterates over input pixels $(x, y)$, computing destination $(x', y') = T(x, y)$. Since $(x', y')$ are floating-point numbers, rounding causes <strong>holes (unassigned pixels)</strong> and overlap collisions.",
            "<strong>Inverse Mapping (Standard):</strong> Iterates over every discrete destination pixel $(x', y')$, querying source position $(x, y) = T^{-1}(x', y')$.",
            "<strong>Bilinear Interpolation:</strong> Because $(x, y)$ falls between integer coordinates, its intensity is interpolated using a weighted average of its 4 nearest neighbors: $f(x, y) = (1-a)(1-b) f_{00} + a(1-b) f_{10} + (1-a)b f_{01} + ab f_{11}$."
        ],
        "math": "$$I_{\\text{dest}}(x', y') = I_{\\text{src}}(T^{-1}(x', y')) \\quad \\text{via Bilinear 4-Neighbor Interpolation}$$",
        "personalConnection": "Filling an ice cube tray: forward mapping is splashing water randomly from across the room (many cells stay dry). Inverse mapping is inspecting each cell directly and filling it from the pitcher.",
        "examTrap": "Forward mapping requires expensive splatting algorithms to avoid gaps. All production computer vision and DIP pipelines strictly use INVERSE warping with $T^{-1}$."
    },
    {
        "id": 40106,
        "subject": "DIP",
        "topicId": "01_Image_Formation_Camera_Geometry_and_Transformations",
        "topicTitle": "01 · Image Formation & Transformations",
        "cardNumber": "06",
        "category": "WORKED BENCHMARK",
        "highlighterClass": "highlight-rose",
        "title": "Worked Benchmark: 4-Point Homography via DLT",
        "drawingSvg": """<svg viewBox="0 0 240 145" class="w-full h-full">
  <defs>
    <marker id="arr-dip6" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>
  <!-- 4 matching points between two quadrilaterals -->
  <polygon points="30,40 75,30 85,90 25,95" fill="#f8fafc" stroke="#000000" stroke-width="1.5"/>
  <circle cx="30" cy="40" r="3" fill="#000000"/>
  <circle cx="75" cy="30" r="3" fill="#000000"/>
  <circle cx="85" cy="90" r="3" fill="#000000"/>
  <circle cx="25" cy="95" r="3" fill="#000000"/>
  <!-- Arrow H -->
  <line x1="95" y1="65" x2="140" y2="65" stroke="#000000" stroke-width="2" marker-end="url(#arr-dip6)"/>
  <text x="117" y="58" fill="#000000" font-size="9" font-family="serif" font-style="italic" font-weight="bold" text-anchor="middle">H (8 DOF)</text>
  <!-- Target Rectified Quad -->
  <rect x="150" y="35" width="65" height="60" fill="#f1f5f9" stroke="#000000" stroke-width="1.5"/>
  <circle cx="150" cy="35" r="3" fill="#000000"/>
  <circle cx="215" cy="35" r="3" fill="#000000"/>
  <circle cx="215" cy="95" r="3" fill="#000000"/>
  <circle cx="150" cy="95" r="3" fill="#000000"/>
  <text x="120" y="125" fill="#000000" font-size="9" font-family="serif" font-style="italic" font-weight="bold" text-anchor="middle">4 Point Matches ⇒ 8 Equations (Ah = 0)</text>
</svg>""",
        "drawingCaption": "Direct Linear Transformation: 4 coplanar point correspondences provide 8 independent equations to solve 3×3 matrix H",
        "coreTranslation": [
            "<strong>Problem:</strong> How many point correspondences are needed to estimate a 2D homography $H$, and how is it computed?",
            "<strong>Degree of Freedom Count:</strong> A $3 \\times 3$ homography matrix has 9 elements, but overall scale is arbitrary $\\implies$ <strong>8 Degrees of Freedom</strong>.",
            "Each point match $(x_i, y_i) \\leftrightarrow (x_i', y_i')$ gives 2 independent linear equations: $x_i' (h_{31} x_i + h_{32} y_i + h_{33}) = h_{11} x_i + h_{12} y_i + h_{13}$.",
            "Therefore, exactly <strong>4 point correspondences</strong> (no three collinear) yield 8 equations $A h = 0$. The solution is the eigenvector of $A^T A$ corresponding to the smallest eigenvalue (SVD)."
        ],
        "math": "$$A h = \\mathbf{0}, \\quad A \\in \\mathbb{R}^{8 \\times 9}, \\quad h = \\arg\\min_{\\|h\\|=1} \\|A h\\| \\implies h = v_9 \\text{ of } \\operatorname{SVD}(A)$$",
        "personalConnection": "Scanning a document with your phone from an angle: the phone finds the 4 corners of the paper and applies the 4-point homography $H$ to un-skew the rectangular page flat on your screen.",
        "examTrap": "Collinear points trap: If any 3 of the 4 points lie on a straight line, the rows of matrix $A$ become linearly dependent, causing SVD estimation to fail completely."
    }
]

master_all = all_cards + laa_cards + stoma_cards + dip_cards

with open('/Users/senso/Projects/photographic-memory-cards/cards_data.js', 'w') as f:
    f.write('/* Master Multi-Subject Cards Database for CMO, LAA, StoMA, DIP */\n')
    f.write('window.MASTER_CARDS_DATA = ')
    json.dump(master_all, f, indent=2)
    f.write(';\n')

print(f"Total cards across all 4 subjects: {len(master_all)}")
for sub in ['CMO', 'LAA', 'StoMA', 'DIP']:
    count = len([c for c in master_all if c.get('subject') == sub])
    print(f"  {sub}: {count} cards")
