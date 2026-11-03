"""Topics 11-14: notes, drawings and captions use the symbols of the textbook statement (c_i, lambda_i, L, M, C, P_C(p), ...)."""
from notation_lib import build

SUBS = {
    # ---- 11 ----
    1105: [
        (r"\hat{x}", r"\bar x"), (r"\hat x", r"\bar x"), ("x̂", "x̄"),
        (r"A \bar x = b", r"h(\bar x)=0"), (r"A\bar x=b", r"h(\bar x)=0"), ("Ax̄ = b", "h(x̄) = 0"),
        (r"d^* = p^* \quad (\text{Strong Duality})", r"p^*=d^* \quad (\text{strong duality})"),
        (r"zero duality gap for a convex program", r"zero duality gap for a convex program"),
        (r"$d^*=p^*$", r"$p^*=d^*$"), ("d* = p*", "p* = d*"),
    ],
    # ---- 12 ----
    1201: [
        (r"$d\in M(x^*)$ = the runway", r"$d\in M$ = the runway"),
        (r"$\nabla^2_{xx}\mathcal L$ = the Lagrangian's curvature", r"$\nabla^2_{xx}L$ = the Lagrangian's curvature"),
        (r"$d^\top\nabla^2\mathcal Ld\ge0$", r"$d^\top\nabla^2_{xx}L\,d\ge0$"),
        (r"$d^\top\nabla^2\mathcal L\,d\ge0$", r"$d^\top\nabla^2_{xx}L\,d\ge0$"),
        ("(d ∈ M: ∇hᵀd = 0)", "(d ∈ M: ∇cᵢᵀd = 0)"), ("only for d ∈ M(x*)", "only for d ∈ M"),
        (r"where ∇hᵀd = 0", r"where ∇cᵢᵀd = 0 for active i"),
    ],
    1202: [
        ("∀ d ∈ M ∖ {0}", "∀ d ∈ C ∖ {0}"), ("dᵀ∇²L d", "dᵀ∇²ₓₓL d"),
    ],
    1203: [
        (r"$\nabla^2\mathcal L$", r"$\nabla^2_{xx}L$"), (r"\nabla^2\mathcal L", r"\nabla^2_{xx}L"),
        (r"$\operatorname{sign}\det=(-1)^p$</strong> (for $p$ walls)", r"$\operatorname{sign}\det=(-1)^m$</strong> (for $m$ constraints)"),
        ("sign det B₂ₚ₊ₘ = (−1)ᵖ", "sign det Bₖ = (−1)ᵐ"), ("for m = 1, …, n − p", "last n − m minors"),
        ("∇²L", "∇²ₓₓL"), ("last n − m leading minors", "last n − m minors"),
        ("Check the last n − p leading minors: if sign det B₂ₚ₊ₘ = (−1)ᵖ for m = 1, …, n − p", "Check the last n − m leading principal minors: if sign det Bₖ = (−1)ᵐ for all of them"),
    ],
    1204: [
        (r"($\mu_j\gt0$)", r"($\lambda_i\gt0$)"), (r"($\mu_j=0$)", r"($\lambda_i=0$)"), (r"($\mu\gt0$)", r"($\lambda\gt0$)"),
        ("all μ > 0: pinned", "all λᵢ* > 0: pinned"), ("μ₁, μ₂ > 0", "λ₁*, λ₂* > 0"), ("C = Null[∇h, ∇g𝒜]ᵀ", "C = M"),
        ("μ = 0 : can peel off", "λᵢ* = 0 : can peel off"), ("∇gⱼᵀd ≤ 0", "∇cᵢᵀd ≤ 0"),
        ("μⱼ* > 0, so the plane is pinned and the critical cone is the null space C = Null[∇hᵀ; ∇g𝒜ᵀ]. If some μⱼ = 0", "λᵢ* > 0, so the plane is pinned and the critical cone is the subspace C = M. If some λᵢ* = 0"),
        ("every active wall pushes, μⱼ* > 0", "every active wall pushes, λᵢ* > 0"),
    ],
    1205: [
        ("λ*∇²h: the bank", "λᵢ∇²cᵢ: the bank"), ("Σλᵢ∇²hᵢ", "Σλᵢ∇²cᵢ"),
        (r"equals $\sum\mu_j\nabla g_j^\top\ddot x$", r"equals $-\sum\lambda_i\nabla c_i^\top\ddot x=\sum\lambda_i\,d^\top\nabla^2c_i\,d$"),
        (r"$d^\top[\nabla^2f+\sum\mu_j\nabla^2g_j]d$", r"$d^\top[\nabla^2f+\sum\lambda_i\nabla^2c_i]d$"),
        (r"$\nabla^2 f+\sum\mu_j\nabla^2 g_j$", r"$\nabla^2 f+\sum\lambda_i\nabla^2 c_i$"),
        (r"dᵀ(Σλᵢ∇²hᵢ)d", r"dᵀ(Σλᵢ∇²cᵢ)d"),
    ],
    # ---- 13 ----
    1301: [
        ("<strong>$x-p$ = the vector from the nearest legal spot to the plane.</strong>", "<strong>$p-P_C(p)$ = the vector from the nearest legal spot to the plane.</strong>"),
        (r"<strong>$\langle x-p,y-p\rangle\le0$ for every legal $y$:</strong> the angle at $p$ between", r"<strong>$(p-P_C(p))^\top(y-P_C(p))\le0$ for every legal $y$:</strong> the angle at $P_C(p)$ between"),
        (r"$p\in C$ and the inequality hold iff $p=\Pi_C(x)$.", r"a point $z\in C$ with $(p-z)^\top(y-z)\le0$ for all $y\in C$ must be $P_C(p)$."),
        (">x</text>", ">p</text>"), ("p = Π(x)", "P = Pᴄ(p)"), ("⟨x − p, y − p⟩ ≤ 0", "(p − P)ᵀ(y − P) ≤ 0"),
        ("Project x onto the closed convex set C: p = Π(x) is the nearest legal point. It is characterised by the angle test ⟨x − p, y − p⟩ ≤ 0 for every y ∈ C",
         "Project p onto the closed convex set C: Pᴄ(p) is the nearest legal point. It is characterised by the angle test (p − Pᴄ(p))ᵀ(y − Pᴄ(p)) ≤ 0 for every y ∈ C"),
    ],
    1302: [
        (r"<strong>$\|\Pi x-\Pi y\|^2+\|(I-\Pi)x-(I-\Pi)y\|^2\le\|x-y\|^2$:</strong> the along-the-wall and across-the-wall parts together are at most the original distance squared.",
         r"<strong>$(P(p)-P(q))^\top(p-q)$:</strong> the part of $p-q$ lying along the gap between the two landing spots; firm non-expansiveness says the gap squared is at most this."),
        (r"<strong>Dropping the second (non-negative) term</strong> gives $\|\Pi x-\Pi y\|\le\|x-y\|$.", r"<strong>Cauchy-Schwarz</strong> bounds it by $\|P(p)-P(q)\|\,\|p-q\|$; dividing out gives $\|P(p)-P(q)\|\le\|p-q\|$."),
        ("‖Π(x) − Π(y)‖ ≤ ‖x − y‖", "‖P(p) − P(q)‖ ≤ ‖p − q‖"), ("Π(x)", "P(p)"), ("Π(y)", "P(q)"), ("‖x − y‖", "‖p − q‖"),
        ("Firm non-expansiveness is stronger: the squared shadow distance plus the squared distance of the dropped-off parts is at most ‖x − y‖².",
         "Firm non-expansiveness is stronger: ‖P(p) − P(q)‖² ≤ (P(p) − P(q))ᵀ(p − q)."),
    ],
    1303: [
        (r"$a^\top x-b$ = how far", r"$a^\top p-b$ = how far"),
        ("x − (aᵀx − b)a/‖a‖²", "p − (aᵀp − b)a/‖a‖²"), ("aᵀx > b: drop along a", "aᵀp > b: drop along a"), ("aᵀx ≤ b: max(0, ·) = 0, stays", "aᵀp ≤ b: max(0, ·) = 0, stays"),
        ("Onto the wall aᵀx = b: x − (aᵀx − b)a/‖a‖², a drop along the normal a. Onto the halfspace aᵀx ≤ b: the same drop with max(0, aᵀx − b)",
         "Onto the wall aᵀx = b: P_H(p) = p − (aᵀp − b)a/‖a‖², a drop along the normal a. Onto the halfspace aᵀx ≤ b: the same drop with max(0, aᵀp − b)"),
    ],
    1307: [
        (r"$\min(u_i,\max(l_i,x_i))$ clamps", r"$\min\{u_i,\max\{l_i,p_i\}\}$ clamps"),
        (r"<strong>Ball:</strong> $x/\max(1,\|x\|/R)$ leaves you alone inside the ball and scales you back along the ray to the centre once outside.",
         r"<strong>Ball:</strong> $c+\frac{r}{\max\{r,\|p-c\|\}}(p-c)$ leaves you alone inside the ball and, once outside, pulls you straight back toward the centre $c$ to the rim."),
        ("Π(x)", "P(p)"), ("min(uᵢ, max(lᵢ, xᵢ))", "min(uᵢ, max(lᵢ, pᵢ))"), ("x / max(1, ‖x‖/R)", "c + r(p − c)/max(r, ‖p − c‖)"),
        ("[Π(x)]ᵢ = min(uᵢ, max(lᵢ, xᵢ))", "P(p)ᵢ = min(uᵢ, max(lᵢ, pᵢ))"),
        ("Ball of radius R: a point outside is scaled back to the rim, Π(x) = x / max(1, ‖x‖/R); a point inside stays.",
         "Ball of centre c, radius r: a point outside is pulled back to the rim, P(p) = c + r(p − c)/max(r, ‖p − c‖); a point inside stays."),
    ],
    1304: [
        (r"<strong>$x_1=\Pi_K(x)\in K$:</strong>", r"<strong>$P_K(x)\in K$:</strong>"),
        (r"<strong>$x_2=\Pi_{K^\circ}(x)\in K^\circ$:</strong>", r"<strong>$P_{K^\circ}(x)\in K^\circ$:</strong>"),
        (r"<strong>$\langle x_1,x_2\rangle=0$:</strong> the two parts are perpendicular; in 1D this is $x=x_++x_-$.", r"<strong>$P_K(x)^\top P_{K^\circ}(x)=0$:</strong> the two parts are perpendicular; in 1D this is $x=x_++x_-$."),
        ("x₁ = Πᴋ(x)", "Pᴋ(x)"), ("x₂ = Πᴋ°(x)", "Pᴋ°(x)"), ("x = x₁ + x₂,  ⟨x₁, x₂⟩ = 0", "x = Pᴋ(x) + Pᴋ°(x)"),
        ("any x splits into a part x₁ = Πᴋ(x) in the cone K and a part x₂ = Πᴋ°(x) in its polar cone, with x = x₁ + x₂ and ⟨x₁, x₂⟩ = 0.",
         "any x splits into a part Pᴋ(x) in the cone K and a part Pᴋ°(x) in its polar cone, x = Pᴋ(x) + Pᴋ°(x), and the two parts are perpendicular: Pᴋ(x)ᵀPᴋ°(x) = 0."),
    ],
    1305: [
        (r"<strong>$y_k=\Pi_{C_1}(x_k+p_{k-1})$:</strong> project onto the first airspace, but first add back the correction remembered from last time.", r"<strong>$y_k=P_{C_1}(x_k+p_k)$:</strong> project onto the first airspace, but first add back the correction remembered from last time."),
        (r"<strong>$p_k=x_k+p_{k-1}-y_k$:</strong>", r"<strong>$p_{k+1}=x_k+p_k-y_k$:</strong>"),
        ("Dykstra: true Π", "Dykstra: true P"),
        ("yₖ = Π₁(xₖ + pₖ₋₁),  pₖ = xₖ + pₖ₋₁ − yₖ  (same for C₂ with q)", "yₖ = P₁(xₖ + pₖ),  pₖ₊₁ = xₖ + pₖ − yₖ  (same for C₂ with q)"),
        ("yₖ = Π₁(xₖ + pₖ₋₁) with pₖ = xₖ + pₖ₋₁ − yₖ", "yₖ = P₁(xₖ + pₖ) with pₖ₊₁ = xₖ + pₖ − yₖ"),
    ],
    # ---- 14 ----
    1401: [
        (r"\Pi_\Omega", "P_C"), (r"y\in\Omega", r"y\in C"), (r"$\Pi_\Omega$ = air-traffic", r"$P_C$ = air-traffic"),
        ("Π(·)", "Pᴄ(·)"), ("Π(xₖ", "Pᴄ(xₖ"),
    ],
    1402: [
        (r"\Pi_\Omega", "P_C"), (r"$\Pi_\Omega(\cdot)$", r"$P_C(\cdot)$"), (r"\mathcal{N}_\Omega", r"N_C"),
        (">Π</text>", ">Pᴄ</text>"), ("Π(x*", "Pᴄ(x*"), ("N(x*)", "N_C(x*)".replace("_C", "ᴄ")),
        (r"$-\nabla f(x^*)$ lies in the normal cone, i.e. points straight into the wall", r"$-\nabla f(x^*)$ lies in the normal cone $N_C(x^*)$, i.e. points straight into the wall"),
    ],
    1404: [
        ("α = s, βs, β²s, … slide", "α = ᾱ, ᾱρ, ᾱρ², … slide"),
        ("f(x(α)) ≤ f(xₖ) − (γ/α)‖xₖ − x(α)‖²", "f(x(α)) ≤ f(xₖ) + c₁∇f(xₖ)ᵀ(x(α) − xₖ)"),
        ("Try α = s, βs, β²s, …", "Try α = ᾱ, ᾱρ, ᾱρ², …"),
        (r"<strong>$x(\alpha)=\Pi_\Omega(x_k-\alpha\nabla f(x_k))$ traces", r"<strong>$x(\alpha)=P_C(x_k-\alpha\nabla f(x_k))$ traces"),
        (r"<strong>$\frac\gamma\alpha\|x_k-x(\alpha)\|^2$ is the promised drop:</strong> big for a long actual displacement, scaled by the leash $\frac1\alpha$.", r"<strong>$c_1\nabla f(x_k)^\top(x(\alpha)-x_k)$ is the promised drop:</strong> a fraction $c_1$ of the slope times the displacement you actually made (negative, so the right side is below $f(x_k)$)."),
        (r"<strong>Try $\alpha=s,\beta s,\beta^2s,\dots$ and keep the first that earns it.</strong>", r"<strong>Try $\alpha=\bar\alpha,\bar\alpha\rho,\bar\alpha\rho^2,\dots$ and keep the first that earns it.</strong>"),
    ],
    1405: [
        (r"<strong>$-\nabla h[\nabla h^\top\nabla h]^{-1}h(y)$ = drop along the normal</strong>", r"<strong>$-\nabla h(y)^\top(\nabla h(y)\nabla h(y)^\top)^{-1}h(y)$ = drop along the normal</strong>"),
        ("restore: y − ∇h[∇hᵀ∇h]⁻¹h(y) lands back on h = 0", "restore: y − ∇hᵀ(∇h∇hᵀ)⁻¹h(y) lands on h = 0"),
        ("xₖ₊₁ = y − ∇h(xₖ)[∇h(xₖ)ᵀ∇h(xₖ)]⁻¹h(y)", "xₖ₊₁ = y − ∇h(y)ᵀ(∇h(y)∇h(y)ᵀ)⁻¹h(y)"),
    ],
}

EXPLICIT = {
    1105: {"math": r"$$\exists\,\bar x:\ g_j(\bar x)\lt0\ (j=1,\dots,m),\ h(\bar x)=0\implies p^*=d^*\ \ (\text{strong duality})$$"},
    1201: {"math": r"$$d^\top\nabla_{xx}^2L(x^*,\lambda^*)\,d\ge0\quad\forall\,d\in M=\{d:\nabla c_i(x^*)^\top d=0,\ i\in\mathcal A(x^*)\}$$"},
    1202: {"math": r"$$d^\top\nabla_{xx}^2L(x^*,\lambda^*)\,d\gt0\quad\forall\,d\in C(x^*,\lambda^*)\setminus\{0\}\implies x^*\text{ is a strict local minimizer}$$"},
    1203: {"math": r"$$\operatorname{sign}\det B_k=(-1)^m\ \text{ for the last } n-m \text{ leading principal minors }(k=2m+1,\dots,n+m)$$"},
    1204: {"math": r"$$\lambda_i^*\gt0\ \ \forall\,i\in\mathcal A(x^*)\ (\text{inequalities})\implies C(x^*,\lambda^*)=M=\{d:\nabla c_i(x^*)^\top d=0,\ i\in\mathcal A(x^*)\}$$"},
    1205: {"math": r"$$\frac{d^2}{dt^2}f(x(t))\Big|_{t=0}=d^\top\nabla^2f(x^*)\,d+\nabla f(x^*)^\top\ddot x(0)=d^\top\Big[\nabla^2f(x^*)+\sum_i\lambda_i^*\nabla^2c_i(x^*)\Big]d,\quad d=\dot x(0)$$"},
    1301: {"math": r"$$P_C(p)\in C\quad\text{and}\quad\big(p-P_C(p)\big)^\top\big(y-P_C(p)\big)\le0\quad\forall\,y\in C$$"},
    1302: {"math": r"$$\|P(p)-P(q)\|^2\le\big(P(p)-P(q)\big)^\top(p-q)\implies\|P(p)-P(q)\|\le\|p-q\|$$"},
    1303: {"math": r"$$P_H(p)=p-\frac{a^\top p-b}{\|a\|^2}\,a,\qquad P(p)=p-\frac{\max\{0,\,a^\top p-b\}}{\|a\|^2}\,a$$"},
    1307: {"math": r"$$P(p)_i=\min\{u_i,\max\{l_i,p_i\}\},\qquad P(p)=c+\frac{r}{\max\{r,\|p-c\|\}}(p-c)$$"},
    1304: {"math": r"$$x=P_K(x)+P_{K^\circ}(x),\qquad P_K(x)^\top P_{K^\circ}(x)=0$$"},
    1305: {"math": r"$$y_k=P_{C_1}(x_k+p_k),\ p_{k+1}=x_k+p_k-y_k,\quad x_{k+1}=P_{C_2}(y_k+q_k),\ q_{k+1}=y_k+q_k-x_{k+1}$$"},
    1401: {"math": r"$$x_{k+1}=P_C\big(x_k-\alpha_k\nabla f(x_k)\big)=\arg\min_{y\in C}\Big\{\nabla f(x_k)^\top(y-x_k)+\frac1{2\alpha_k}\|y-x_k\|^2\Big\}$$"},
    1402: {"math": r"$$\nabla f(x^*)^\top(x-x^*)\ge0\ \ \forall x\in C\iff x^*=P_C\big(x^*-\alpha\nabla f(x^*)\big)\iff-\nabla f(x^*)\in N_C(x^*)$$"},
    1403: {"math": r"$$f(x_k)-f^*\le\frac{L\|x_0-x^*\|^2}{2k},\qquad\|x_k-x^*\|\le\Big(1-\frac{\mu}{L}\Big)^{k/2}\|x_0-x^*\|$$",
           "breakdown": [r"<strong>Convex, smooth terrain:</strong> $\frac{L\|x_0-x^*\|^2}{2k}$, the gap shrinks like $1/k$ (sublinear).",
                         r"<strong>Strongly convex terrain:</strong> $(1-\mu/L)^{k/2}\|x_0-x^*\|$, a fixed fraction of the distance removed each hop (linear).",
                         r"<strong>The walls do not change either rate:</strong> projection is non-expansive, so it never undoes progress."],
           "drawingSvg_sub": [("c·ρᵏ: strongly convex", "(1 − μ/L)^(k/2): strongly convex")]},
    1404: {"math": r"$$f(x(\alpha))\le f(x_k)+c_1\nabla f(x_k)^\top\big(x(\alpha)-x_k\big),\quad x(\alpha)=P_C\big(x_k-\alpha\nabla f(x_k)\big),\ \alpha\in\{\bar\alpha\rho^m\}$$"},
    1405: {"math": r"$$y=x_k-\alpha P_k\nabla f(x_k),\qquad x_{k+1}=y-\nabla h(y)^\top\big(\nabla h(y)\nabla h(y)^\top\big)^{-1}h(y)\quad(\text{restoration})$$"},
}
# 1403: a few extra replacements done after build (the SVG label and caption)
_extra = EXPLICIT[1403].pop("drawingSvg_sub")

FIX = build(SUBS, EXPLICIT, normalise_ids=(1101, 1102, 1103, 1104))
from notation_lib import CARDS
_c = CARDS[1403]
FIX[1403]["drawingSvg"] = _c["drawingSvg"].replace(*_extra[0])
FIX[1403]["drawingCaption"] = ("Merely convex: the gap f(xₖ) − f* shrinks like L‖x₀ − x*‖²/2k, sublinear. Strongly convex: the distance shrinks like (1 − μ/L)^(k/2)‖x₀ − x*‖, linear, "
                               "which is a straight line on a log scale.")
