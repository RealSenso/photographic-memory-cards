"""One notation across every CMO card (the last layer, so it wins over all earlier passes).

The conventions (they match the exam papers):
  problem      min f(x)  s.t.  h_i(x) = 0 (i = 1..p),  g_j(x) <= 0 (j = 1..m)
  multipliers  lambda_i for equalities (free sign),  mu_j for inequalities (mu_j >= 0)
  Lagrangian   L(x, lambda, mu) = f + lambda^T h + mu^T g          (plain L, never a calligraphic L)
  sets         Omega = feasible set,  A(x) = {j : g_j(x) = 0},  F(x) = linearized cone,  T_Omega(x) = tangent cone,
               M = tangent subspace,  C(x*, mu*) = critical cone
  projection   P_C onto a closed convex set C (topics 13-14), never Pi
  iterations   x_{k+1} = x_k + alpha_k p_k: step alpha_k, search direction p_k (never d_k; d is kept for the
               directions of the cone and second-order cards in topics 9-12)
  QP           1/2 x^T Q x + c^T x (Q, never G)
  Armijo       trial steps alpha = alpha_bar rho^m, sufficient decrease constant c_1

Sublevel sets in topic 1 keep their name L_alpha(f); strong convexity mu and the smoothness constant L of topics 3-5
and 14, and the barrier parameter mu in topics 18-19, are the textbook names and appear only on unconstrained or
barrier cards.
"""
import json, os, re

_here = os.path.dirname(os.path.abspath(__file__))
_t = open(os.path.join(_here, "..", "cards_data.js")).read()
CARDS = {c["id"]: c for c in json.loads(_t[_t.index("["):_t.rindex("]") + 1]) if c["subject"] == "CMO"}
FIELDS = ["statement", "math", "coreTranslation", "breakdown", "drawingCaption", "personalConnection", "examTrap",
          "hint", "drawingSvg", "title"]
topic = lambda cid: cid // 100

SUB_DIGITS = "ₖᵢⱼ₀₁₂₃₄₊₋"


def each(v, fn):
    return [fn(x) for x in v] if isinstance(v, list) else fn(v)


def math_segments(s, fn):
    """apply fn to the inside of every $...$ / $$...$$ segment"""
    return re.sub(r"\$\$.+?\$\$|\$[^$]+\$", lambda m: fn(m.group(0)), s, flags=re.S)


def svg_text(s, fn):
    """apply fn to the visible text of every <text> element of a drawing"""
    return re.sub(r"(<text[^>]*>)(.*?)(</text>)", lambda m: m.group(1) + fn(m.group(2)) + m.group(3), s, flags=re.S)


# ---------------- global rules ----------------
def lagrangian(s):
    s = re.sub(r"(\\[a-zA-Z]+)(?=\\mathcal\{?L)", r"\1 ", s)      # \le\mathcal{L} -> \le L, not \leL
    s = re.sub(r"\\mathcal\{L\}(?!_\\alpha|_\{\\alpha)", "L", s)
    s = re.sub(r"\\mathcal L(?!_\\alpha)", "L", s)
    return s


def projection(s):
    s = re.sub(r"\\Pi_\{?\\Omega\}?", "P_C", s)
    s = re.sub(r"\\Pi_", "P_", s)                    # \Pi_C -> P_C, \Pi_{C_1} -> P_{C_1}, \Pi_K -> P_K
    s = re.sub(r"\\Pi(?![a-zA-Z])", "P_C", s)
    s = re.sub(r"(\\[a-zA-Z]+)(?=P_)", r"\1 ", s)    # \langle P_C, not \langleP_C
    return s.replace("Π(", "P_C(")


def set_C(s):
    s = re.sub(r"(\\[a-zA-Z]+)\\Omega", r"\1 C", s)  # \in C, not \inC
    return s.replace("\\Omega", "C").replace("Ω", "C")


def direction_latex(m):
    x = m
    x = re.sub(r"(?<![A-PR-Za-z\\])d(?=_)", "p", x)                      # d_k, d_{k+1}, d_i
    x = re.sub(r"(?<![A-PR-Za-z\\])d(?=\s*[\^)\],=+\-|]|\s*\\(?:le|ge|lt|gt|in|ne|top)\b|\s*\$)", "p", x)  # bare d
    x = re.sub(r"\\\|d\\\|", r"\\|p\\|", x)
    x = re.sub(r"(_k|_0|_1|_\{k-1\})d(?=_)", r"\1p", x)              # \alpha_kd_k, \beta_kd_k
    return x


def direction_text(s):
    s = re.sub(r"(?<![A-PR-Za-z])d(?=[" + SUB_DIGITS + "ᵀ])", "p", s)        # dₖ, d₀, dᵢ, dᵀ
    s = re.sub(r"(?<![A-Za-z])d(?=\)| = −| =−| ✓)", "p", s)            # (x + αd), d = −g
    s = s.replace("αd)", "αp)")
    return s


def direction(s, is_svg=False):
    if is_svg:
        return svg_text(s, direction_text)
    s = math_segments(s, direction_latex)
    # text outside $...$ (captions are plain unicode)
    parts = re.split(r"(\$\$.+?\$\$|\$[^$]+\$)", s, flags=re.S)
    return "".join(p if p.startswith("$") else direction_text(p) for p in parts)


def subs(s, pairs):
    for a, b in pairs:
        s = s.replace(a, b)
    return s


# ---------------- per-card substitutions ----------------
INEQ_1006 = [("\\lambda_i", "\\mu_j"), ("\\lambda_1", "\\mu_1"), ("\\lambda_2", "\\mu_2"), ("\\nabla c_i", "\\nabla g_j"),
             ("\\nabla c_1", "\\nabla g_1"), ("\\nabla c_2", "\\nabla g_2"), ("i\\in\\mathcal A", "j\\in\\mathcal A"),
             ("λ₁∇c₁", "μ₁∇g₁"), ("λ₂∇c₂", "μ₂∇g₂"), ("λᵢ ≥ 0, i ∈", "μⱼ ≥ 0, j ∈"), ("λᵢ ≥ 0", "μⱼ ≥ 0"),
             ("∇cᵢ", "∇gⱼ"), ("c₁ ≤ 0", "g₁ ≤ 0"), ("c₂ ≤ 0", "g₂ ≤ 0"), ("wall c₁", "wall g₁"), ("wall c₂", "wall g₂"),
             ("λ₁", "μ₁"), ("λ₂", "μ₂"), ("\\lambda", "\\mu")]

SUBS = {
    903: [("\\lambda d", "\\theta d"), ("\\lambda\\ge0", "\\theta\\ge0"), ("\\lambda\\ge 0", "\\theta\\ge 0"),
          ("λd with λ ≥ 0", "θd with θ ≥ 0"), ("($\\lambda d$)", "($\\theta d$)")],
    906: [("L_\\Omega", "\\mathcal F"), ("L_{\\Omega}", "\\mathcal F"),
          ("the linearized cone L = {d : ∇gⱼᵀd ≤ 0}", "the linearized cone 𝓕 = {d : ∇gⱼᵀd ≤ 0}"),
          ("With LICQ, T = L.", "With LICQ, T = 𝓕."), ("L = {d : ∇gⱼᵀd ≤ 0}", "𝓕 = {d : ∇gⱼᵀd ≤ 0}"),
          ("L says ok", "𝓕 says ok")],
    1006: INEQ_1006,
    406: [("∇f(x)ᵀd holds", "∇f(x)ᵀp holds")],
    1104: [("Σ λⱼ∇gⱼ", "Σ μⱼ∇gⱼ"), ("the multipliers are λ = (1,1)", "the multipliers are μ = (1,1)"), ("no λ ✗", "no μ ✗"),
           ("Σλⱼ∇gⱼ", "Σμⱼ∇gⱼ")],
    1201: [("∇cᵢᵀd = 0 for active i", "∇hᵢᵀd = 0 and ∇gⱼᵀd = 0 for active j"), ("(d ∈ M: ∇cᵢᵀd = 0)", "(d ∈ M: ∇gⱼᵀd = 0)"),
           ("M(x^*)", "M")],
    1202: [],
    1204: [("\\lambda_i^*", "\\mu_j^*"), ("\\lambda_i", "\\mu_j"), ("\\lambda\\gt0", "\\mu\\gt0"),
           ("λᵢ* > 0", "μⱼ* > 0"), ("λᵢ* = 0", "μⱼ* = 0"), ("λ₁*, λ₂* > 0", "μ₁*, μ₂* > 0"), ("∇cᵢᵀd", "∇gⱼᵀd"),
           ("C(x^*)$ is a CONE", "C(x^*,\\mu^*)$ is a CONE")],
    1205: [("\\nabla^2c_i", "\\nabla^2h_i"), ("\\nabla^2 c_i", "\\nabla^2 h_i"), ("\\nabla c_i", "\\nabla h_i"),
           ("∇²cᵢ", "∇²hᵢ"), ("λᵢ∇²cᵢ", "λᵢ∇²hᵢ")],
    1206: [("($m=1$, $n=2$)", "($p=1$, $n=2$)"), ("\\lt0=(-1)^m", "\\lt0=(-1)^p"), ("with $m=1$ and $n-m=1$", "with $p=1$ and $n-p=1$"),
           ("sign $(-1)^m=-1$", "sign $(-1)^p=-1$"), ("= (−1)ᵐ, m = 1", "= (−1)ᵖ, p = 1"), ("c(x)=x_1^2", "h(x)=x_1^2"), ("\\lambda\\nabla c", "\\lambda\\nabla h"), ("\\nabla c(x^*)", "\\nabla h(x^*)"),
           ("\\nabla c=", "\\nabla h="), ("\\nabla^2c", "\\nabla^2h"), (",\\ c=0", ",\\ h=0"), ("−∇f = λ∇c", "−∇f = λ∇h"),
           ("∇f + λ∇c = 0", "∇f + λ∇h = 0"), ("c = x₁² + x₂² − 1 = 0", "h = x₁² + x₂² − 1 = 0"), ("\\nabla c$", "\\nabla h$")],
    1203: [("with $m$ constraints and Jacobian", "with $p$ equality constraints and Jacobian"),
           ("the last $n-m$ leading", "the last $n-p$ leading"), ("all have sign $(-1)^m$", "all have sign $(-1)^p$"),
           ("\\det B_k=(-1)^m\\ \\text{ for the last } n-m", "\\det B_k=(-1)^p\\ \\text{ for the last } n-p"),
           ("(k=2m+1,\\dots,n+m)", "(k=2p+1,\\dots,n+p)"),
           ("$A=\\nabla h(x^*)^\\top$, form $B=\\begin{bmatrix}0&A\\\\A^\\top&L\\end{bmatrix}$ ($L=\\nabla^2_{xx}L$)",
            "$J=\\nabla h(x^*)^\\top$, form $B=\\begin{bmatrix}0&J\\\\J^\\top&\\nabla^2_{xx}L\\end{bmatrix}$"),
           ("$\\operatorname{sign}\\det=(-1)^m$</strong> (for $m$ constraints)", "$\\operatorname{sign}\\det=(-1)^p$</strong> (for $p$ constraints)"),
           ("last n − m leading", "last n − p leading"), ("sign det Bₖ = (−1)ᵐ", "sign det Bₖ = (−1)ᵖ"), ("last n − m minors", "last n − p minors")],
    1404: [("backtrack $\\alpha=s,\\beta s,\\beta^2s,\\dots$ until the Armijo test along the arc holds: "
            "$f(x(\\alpha))\\le f(x_k)-\\tfrac\\sigma\\alpha\\|x_k-x(\\alpha)\\|^2$.",
            "backtrack $\\alpha=\\bar\\alpha,\\bar\\alpha\\rho,\\bar\\alpha\\rho^2,\\dots$ until the Armijo test along the arc holds: "
            "$f(x(\\alpha))\\le f(x_k)+c_1\\nabla f(x_k)^\\top(x(\\alpha)-x_k)$."),
           ("Π(xₖ − α∇f)", "P_C(xₖ − α∇f)"), ("$P(x_k-\\alpha\\nabla f)$", "$P_C(x_k-\\alpha\\nabla f)$")],
    1703: [("\\lambda", "\\mu"), ("λ", "μ"),
           ("\\max_{x,y}\\ -\\tfrac12x^TQx+b^Ty$ s.t. $Qx-A^Ty+c\\ge0,\\ y\\ge0", "\\max_{x,\\mu}\\ -\\tfrac12x^TQx+b^T\\mu$ s.t. $Qx-A^T\\mu+c\\ge0,\\ \\mu\\ge0"),
           ("-y^\\top(Ax-b)", "-\\mu^\\top(Ax-b)"), ("Qx+c-A^Ty-v=0", "Qx+c-A^T\\mu-v=0"), ("v=Qx+c-A^Ty\\ge0", "v=Qx+c-A^T\\mu\\ge0"),
           ("+b^Ty$", "+b^T\\mu$"), ("bᵀy", "bᵀμ"), ("Aᵀy", "Aᵀμ")],
    1705: [("t_kg(x_k)", "\\alpha_kg(x_k)"), ("step sizes $t_k\\gt 0$", "step sizes $\\alpha_k\\gt 0$"), ("tₖg(xₖ)", "αₖg(xₖ)")],
    1904: [("\\lambda_i^{(k)}", "(\\lambda_k)_i"), ("\\mu_j^{(k)}", "(\\mu_k)_j")],
}

# whole-field rewrites where c_i (one name for every constraint) has to be split into h_i and g_j
EXPLICIT = {
    901: {"statement": r"For $\Omega=\{x: h_i(x)=0\ (i=1,\dots,p),\ g_j(x)\le0\ (j=1,\dots,m)\}$, the <b>active set</b> at a feasible $x$ is $\mathcal A(x)=\{j: g_j(x)=0\}$ (the equalities hold at every feasible point, so they always count as touched). An inequality with $g_j(x)\lt0$ is <b>inactive</b>."},
    906: {"statement": r"The <b>linearized cone</b> is $\mathcal F(x)=\{d:\nabla h_i(x)^\top d=0\ \forall i,\ \nabla g_j(x)^\top d\le0\ \forall j\in\mathcal A(x)\}$. Always $T_\Omega(x)\subseteq\mathcal F(x)$. <b>LICQ</b> holds at $x$ if the gradients $\nabla h_i(x)$ (all $i$) and $\nabla g_j(x)$ ($j\in\mathcal A(x)$) are linearly independent, and then $T_\Omega(x)=\mathcal F(x)$.",
          "math": r"$$\text{LICQ holds}\implies T_\Omega(x^*)=\mathcal F(x^*)=\{d:\nabla h_i^\top d=0,\ \nabla g_j^\top d\le0\ (j\in\mathcal A)\}$$"},
    1006: {"statement": r"<b>Question.</b> Let $x^*$ be a local minimizer of $f$ subject to $g_j(x)\le0$, with $T_\Omega(x^*)=\mathcal F(x^*)$ (e.g. under LICQ). Show there are multipliers $\mu_j\ge0$ with $\nabla f(x^*)+\sum_{j\in\mathcal A(x^*)}\mu_j\nabla g_j(x^*)=0$."},
    1201: {"statement": r"<b>Second-order necessary conditions.</b> Let $x^*$ be a local minimizer with LICQ, KKT multipliers $(\lambda^*,\mu^*)$ and strict complementarity. Then $d^\top\nabla_{xx}^2L(x^*,\lambda^*,\mu^*)\,d\ge0$ for all $d$ in the tangent subspace $M=\{d:\nabla h_i(x^*)^\top d=0\ \forall i,\ \nabla g_j(x^*)^\top d=0\ \forall j\in\mathcal A(x^*)\}$.",
           "math": r"$$d^\top\nabla_{xx}^2L(x^*,\lambda^*,\mu^*)\,d\ge0\quad\forall\,d\in M=\{d:\nabla h_i(x^*)^\top d=0,\ \nabla g_j(x^*)^\top d=0\ (j\in\mathcal A(x^*))\}$$"},
    1202: {"statement": r"<b>Second-order sufficient conditions.</b> If $(x^*,\lambda^*,\mu^*)$ satisfies KKT and $d^\top\nabla_{xx}^2L(x^*,\lambda^*,\mu^*)\,d\gt 0$ for all nonzero $d$ in the critical cone $C(x^*,\mu^*)$, then $x^*$ is a strict local minimizer.",
           "math": r"$$d^\top\nabla_{xx}^2L(x^*,\lambda^*,\mu^*)\,d\gt0\quad\forall\,d\in C(x^*,\mu^*)\setminus\{0\}\implies x^*\text{ is a strict local min}$$"},
    1204: {"statement": r"The <b>critical cone</b> is $C(x^*,\mu^*)=\{d\in\mathcal F(x^*): \nabla g_j(x^*)^\top d=0$ for every active $j$ with $\mu_j^*\gt 0\}$. Under strict complementarity ($\mu_j^*\gt 0$ for every $j\in\mathcal A(x^*)$) it equals the subspace $M$; otherwise it is a polyhedral cone.",
           "math": r"$$\mu_j^*\gt0\ \ \forall\,j\in\mathcal A(x^*)\implies C(x^*,\mu^*)=M=\{d:\nabla h_i(x^*)^\top d=0,\ \nabla g_j(x^*)^\top d=0\ (j\in\mathcal A(x^*))\}$$"},
}

INEQ_QP = [("\\hat\\lambda", "\\hat\\mu"), ("λ̂", "μ̂"), ("\\lambda_i", "\\mu_i"), ("\\lambda_j", "\\mu_j"), ("\\lambda_k", "\\mu_k"),
           ("-\\lambda", "-\\mu"), ("\\lambda", "\\mu")]


def qp_G(s):
    s = math_segments(s, lambda m: re.sub(r"(?<![A-Za-z\\])G(?![A-Za-z])", "Q", m))
    s = s.replace("[G ", "[Q ")
    return re.sub(r"\[G A_|G ≻ 0|\bG\b(?= ≻)", lambda m: m.group(0).replace("G", "Q"), s)


FIX = {}
for cid, c in CARDS.items():
    t = topic(cid)
    out = {}
    for fld in FIELDS:
        v = c.get(fld)
        if v is None:
            continue
        is_svg = fld == "drawingSvg"

        def fn(s):
            if t != 1:
                s = lagrangian(s)
            if t in (13, 14):
                s = svg_text(s, projection) if is_svg else projection(s)
                s = s.replace("P_2(P_1(P_2(x)))", "P_{C_2}(P_{C_1}(P_{C_2}(x)))")
            if t == 14:
                s = set_C(s)
            if t in (4, 5, 6, 7, 8):
                s = direction(s, is_svg)
            if t == 15:
                s = subs(s, INEQ_QP)
                s = svg_text(s, qp_G) if is_svg else qp_G(s)
            s = re.sub(r"L\(x\^\*,\s?\\lambda\^\*\)", r"L(x^*,\\lambda^*,\\mu^*)", s)
            s = re.sub(r"C\(x\^\*,\s?\\lambda\^\*\)", r"C(x^*,\\mu^*)", s)
            s = subs(s, SUBS.get(cid, []))
            s = s.replace("x^{(k)}", "x_k").replace("\\notinW", "\\notin W")
            return s

        out[fld] = each(v, fn)          # always written: earlier layers re-set these fields on every run
    out.update(EXPLICIT.get(cid, {}))
    if out:
        FIX[cid] = out
