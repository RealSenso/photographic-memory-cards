"""Topics 15-19: notes, drawings and captions use the symbols of the textbook statement (G, W_k, \\hat\\lambda, q, theta, t_k, mu, Q(x;c), ...)."""
from notation_lib import build

W_SUBS = [(r"\mathcal{W}", "W"), (r"\mathcal W", "W"), ("𝒲", "W")]

SUBS = {
    1501: W_SUBS + [
        (r"<strong>$A_{\mathcal W}p=0$:</strong>", r"<strong>$A_{W_k}p=0$</strong> (rows $a_i^\top$, $i\in W_k$)<strong>:</strong>"),
        (r"<strong>$Qp+g=A_{\mathcal W}^\top\lambda$:</strong>", r"<strong>$Gp+g_k=A_{W_k}^\top\hat\lambda$:</strong>"),
        (r"$A_{\mathcal W}p=0$", r"$A_{W_k}p=0$"),
        ("[Q  A𝒲ᵀ; A𝒲  0][p; −λ] = [−∇f; 0]", "[G  AWᵀ; AW  0][p; −λ̂] = [−g; 0]"), ("A𝒲p = 0", "AW p = 0"),
    ],
    1502: W_SUBS + [("Wₖ₊₁ = Wₖ ∪ {i}", "Wₖ₊₁ = Wₖ ∪ {i}")],
    1503: W_SUBS + [
        (r"$\lambda_j\lt0$", r"$\hat\lambda_j\lt0$"), (r"Drop the most negative $\lambda_j$", r"Drop the most negative $\hat\lambda_j$"),
        ("λⱼ &lt; 0: the wall", "λ̂ⱼ &lt; 0: the wall"), ("some multiplier λⱼ < 0", "some multiplier λ̂ⱼ < 0"),
    ],
    1504: W_SUBS + [(r"$Q\succ0$", r"$G\succ0$"), ("Q ≻ 0", "G ≻ 0")],
    1505: W_SUBS,
    1601: [
        (r"\phi(\mu)", "q(\\mu)"), (r"$\phi(\mu)$", r"$q(\mu)$"), ("φ(μ)", "q(μ)"),
    ],
    1605: [
        (r"<strong>$p^*(z)$ = lowest legal altitude after moving the wall by $z$.</strong>", r"<strong>$\omega(z)$ = lowest legal altitude after moving the wall by $z$.</strong>"),
        (r"<strong>$p^*(z)\ge p^*(0)-\mu^{*\top}z$:</strong>", r"<strong>$\omega(z)\ge\omega(0)-\mu^{*\top}z$:</strong>"),
        (r"<strong>So $\nabla_zp^*(0)=-\mu^*$:</strong>", r"<strong>So $\mu_j^*=-\dfrac{\partial\omega}{\partial z_j}(0)$:</strong>"),
        ("p*(z) drops by μ*·Δz", "ω(z) drops by μ*·Δz"), ("∇p*(0) = −μ*: shadow price", "∂ω/∂zⱼ(0) = −μⱼ*: shadow price"),
        ("p*(z) ≥ p*(0) − μ*ᵀz, and ∇p*(0) = −μ*", "ω(z) ≥ ω(0) − μ*ᵀz, and μⱼ* = −∂ω/∂zⱼ(0)"),
        ("best altitude drops by about μ*: p*(z)", "best altitude drops by about μ*: ω(z)"),
    ],
    1701: [
        (r"\mathcal L", "L"), (r"\mathcal{L}", "L"), (r"over $(x,\lambda,\mu)$", r"over $(x,\mu)$"),
        ("∇f + ∇hλ + ∇gμ = 0: balance", "∇f + Σμⱼ∇gⱼ = 0: balance"), ("max f + λᵀh + μᵀg, μ ≥ 0", "max f + μᵀg, μ ≥ 0"),
        ("∇f(x) + ∇h(x)λ + ∇g(x)μ = 0. Among them, with μ ≥ 0, it maximises the Lagrangian f(x) + λᵀh(x) + μᵀg(x).",
         "∇ₓL(x, μ) = 0. Among them, with μ ≥ 0, it maximises the Lagrangian L(x, μ) = f(x) + μᵀg(x)."),
    ],
    1702: [
        (r"\mathcal L(x,\lambda,\mu)", "L(x,\\mu)"), (r"\mathcal L", "L"),
        (r"<strong>$f,g_j$ convex and $h_i$ affine:</strong>", r"<strong>$f,g$ convex ($C^1$):</strong>"),
        ("(f, gⱼ convex, hᵢ affine)", "(f, g convex)"),
    ],
    1704: [(r"\mathcal L", "L")],
    1705: [
        (r"$x(\mu_k)=\arg\min\mathcal L(x,\mu_k)$:", r"$x_k\in\arg\min_xL(x,\mu_k)$:"),
        (r"$g(x(\mu_k))$ = violation:", r"$g(x_k)$ = violation:"), (r"$\alpha_kg$ is the subgradient step", r"$t_kg(x_k)$ is the subgradient step"),
        (r"$\mu_{k+1}=\max(0,\mu_k+\alpha g_j(x_k))$", r"$\mu_{k+1}=\max(0,\mu_k+t_kg(x_k))$"),
        ("g(x(μₖ)) > 0:", "g(xₖ) > 0:"), ("μₖ₊₁ = μₖ + αₖg ↑", "μₖ₊₁ = μₖ + tₖg(xₖ) ↑"),
        ("For the current price μₖ, solve x(μₖ) = argmin L(x, μₖ). If it breaks the wall (g > 0), raise the price; if there is slack (g < 0), lower it, never below zero: μₖ₊₁ = max(0, μₖ + αₖg(x(μₖ))).",
         "For the current price μₖ, solve xₖ ∈ argmin L(x, μₖ). If it breaks the wall (g > 0), raise the price; if there is slack (g < 0), lower it, never below zero: μₖ₊₁ = max(0, μₖ + tₖg(xₖ))."),
    ],
    1703: [],
    1803: [
        (r"A_{\cdot j}^T", r"a_j^\top"), (r"A_{i \cdot} x^*", r"a_i^\top x^*"),
        (r"$x_j(c_j-A_j^\top y)=0$:", r"$x_j(c_j-a_j^\top y)=0$:"), (r"$y_i(A_ix-b_i)=0$:", r"$y_i(a_i^\top x-b_i)=0$:"),
        (r"($c_j\gt A_j^\top y$)", r"($c_j\gt a_j^\top y$)"), ("Aⱼᵀy", "aⱼᵀy"), ("Aᵢx − bᵢ", "aᵢᵀx − bᵢ"),
    ],
    1804: [("Aᵀy ≥ 0, bᵀy &lt; 0", "Aᵀȳ ≥ 0, bᵀȳ &lt; 0"), ("bᵀ(y₀ + td) → +∞", "bᵀ(y₀ + ty) → +∞")],
    1805: [
        (r"<strong>Reduced cost $c_N^\top-c_B^\top B^{-1}N$:</strong>", r"<strong>Reduced cost $\bar c_j=c_j-a_j^\top y$, $y^\top=c_B^\top B^{-1}$:</strong>"),
        ("stop when cɴᵀ − cʙᵀB⁻¹N ≥ 0", "stop when all c̄ⱼ = cⱼ − aⱼᵀy ≥ 0"),
        ("every reduced cost c_Nᵀ − c_BᵀB⁻¹N is ≥ 0", "every reduced cost c̄ⱼ = cⱼ − aⱼᵀy (with yᵀ = c_BᵀB⁻¹) is ≥ 0"),
    ],
    1901: [
        ("q = f + (c/2)·max(0, g)²", "Q = f + (c/2)·max(0, g)²"),
        ("q(c, x) = f(x) + (c/2)Σ hᵢ² + (c/2)Σ max(0, gⱼ)²", "Q(x; c) = f(x) + (c/2)(‖h(x)‖² + ‖max(0, g(x))‖²)"),
    ],
    1902: [
        ("1/c big", "μ big"), ("1/c medium", "μ medium"), ("1/c small", "μ small"),
        ("B(x) = −Σ ln(−gⱼ(x)) → +∞ at the wall", "−μΣ log(−gⱼ) → +∞ at the wall"),
        ("x(c) = argmin f + B/c: c ↑ ⇒ creeps closer", "x(μ) = argmin B(x; μ): μ ↓ ⇒ creeps closer"),
        ("The barrier B(x) = −Σ ln(−gⱼ(x)) blows up at the wall, so the plane never touches it. Minimising f + B/c with larger and larger c lets it creep closer: x(c) → x*.",
         "The barrier −μΣ log(−gⱼ(x)) blows up at the wall, so the plane never touches it. Minimising B(x; μ) = f(x) − μΣ log(−gⱼ(x)) with smaller and smaller μ lets it creep closer: x(μ) → x*."),
    ],
    1903: [(r"\nabla^2 q(c, x)", r"\nabla^2Q"), (r"\nabla^2q", r"\nabla^2Q")],
    1904: [
        (r"<strong>$h_i(x(c_k))$ = how far the plane sinks into the forbidden zone.</strong>", r"<strong>$h(x_k)$ = how far the plane sinks into the forbidden zone.</strong>"),
        (r"like a spring: $\lambda_i^{(k)}=c_kh_i$.", r"like a spring: $\lambda_k=c_kh(x_k)$."),
        (r"the product converges to the true multiplier $\lambda^*_i$.", r"the product converges to the true multiplier $\lambda^*$."),
        ("λ⁽ᵏ⁾ = cₖh → λ*", "λₖ = cₖh → λ*"),
        ("by h(x(cₖ)). That small miss times the fine is the multiplier estimate: λ⁽ᵏ⁾ = cₖh(x(cₖ)) → λ* (and μ⁽ᵏ⁾ = cₖ max(0, g) → μ*).",
         "by h(xₖ). That small miss times the fine is the multiplier estimate: λₖ = cₖh(xₖ) → λ*."),
    ],
}

EXPLICIT = {
    1501: {"drawingCaption": "Walls in the working set Wₖ act as rails: the step must keep A_{Wₖ} p = 0 (rows aᵢᵀ, i ∈ Wₖ). Solving the KKT system [G A_{Wₖ}ᵀ; A_{Wₖ} 0][p; −λ̂] = [−gₖ; 0] gives the best step along the corridor and the walls' multipliers λ̂.",
           "math": r"$$\begin{bmatrix}G&A_{W_k}^\top\\A_{W_k}&0\end{bmatrix}\begin{bmatrix}p_k\\-\hat\lambda_k\end{bmatrix}=\begin{bmatrix}-g_k\\0\end{bmatrix}\quad(\text{KKT system for the equality QP})$$"},
    1502: {"math": r"$$\alpha_k=\min\Big\{1,\ \min_{i\notin W_k,\ a_i^\top p_k\lt0}\frac{b_i-a_i^\top x_k}{a_i^\top p_k}\Big\},\qquad W_{k+1}=W_k\cup\{i_{\text{blocking}}\}$$"},
    1503: {"math": r"$$p_k=0\ \text{ and }\ \hat\lambda_j=\min_{i\in W_k}\hat\lambda_i\lt0\implies W_{k+1}=W_k\setminus\{j\}$$"},
    1504: {"math": r"$$G\succ0\ \text{ and }\ \alpha_k\gt0\implies f(x_{k+1})\lt f(x_k)\implies\text{terminates in}\le2^m\text{ steps}$$"},
    1601: {"math": r"$$\omega(z)=\inf\{f(x):g(x)\le z\},\qquad q(\mu)=\inf_z\{\omega(z)+\mu^\top z\}=\inf_x\{f(x)+\mu^\top g(x)\}$$"},
    1604: {"math": r"$$q\big(\theta(\lambda_1,\mu_1)+(1-\theta)(\lambda_2,\mu_2)\big)\ge\theta\,q(\lambda_1,\mu_1)+(1-\theta)\,q(\lambda_2,\mu_2),\quad\theta\in[0,1]$$",
           "breakdown": [r"<strong>For a fixed plan $x$, $f(x)+\lambda^\top h(x)+\mu^\top g(x)$ is a straight line in $(\lambda,\mu)$.</strong>",
                         r"<strong>$q$ is the lowest of all those lines</strong> (a pointwise infimum).",
                         r"<strong>A pointwise minimum of straight lines bends only one way:</strong> $q$ is concave, whether or not $f,g,h$ are convex."]},
    1605: {"math": r"$$\omega(z)\ge\omega(0)-\mu^{*\top}z\ \ \forall z\implies\mu_j^*=-\frac{\partial\omega}{\partial z_j}(0)$$"},
    1701: {"math": r"$$\max_{x,\mu}\ L(x,\mu)=f(x)+\mu^\top g(x)\quad\text{subject to}\quad\nabla_xL(x,\mu)=0,\ \ \mu\ge0$$"},
    1702: {"math": r"$$f,g\ \text{convex},\ C^1\implies\max_{(x,\mu)\in\text{Wolfe}}L(x,\mu)=f(x^*)=\min_{g(x)\le0}f(x)\quad(\text{zero gap})$$"},
    1705: {"math": r"$$x_k\in\arg\min_xL(x,\mu_k),\qquad\mu_{k+1}=\max\{0,\ \mu_k+t_kg(x_k)\}$$"},
    1803: {"math": r"$$x^*,y^*\text{ optimal}\iff x_j^*\big(c_j-a_j^\top y^*\big)=0\ (\forall j)\ \text{ and }\ y_i^*\big(a_i^\top x^*-b_i\big)=0\ (\forall i)$$"},
    1804: {"math": r"$$\nexists\,x\ge0:\ Ax=b\ \Rightarrow\ \exists\,y:\ A^\top y\le0,\ b^\top y\gt0\ \Rightarrow\ b^\top(y_0+ty)\to+\infty\ \ (t\to\infty)$$",
           "breakdown": [r"<strong>Farkas:</strong> $Ax=b,\ x\ge0$ has no solution, so some $\bar y$ has $A^\top\bar y\ge0$ and $b^\top\bar y\lt0$: the walls cannot hold gravity.",
                         r"<strong>Flip the sign, $y=-\bar y$:</strong> $A^\top y\le0$ and $b^\top y\gt0$, a direction that keeps the dual feasible and raises its objective.",
                         r"<strong>$b^\top(y_0+ty)\to\infty$:</strong> for any dual-feasible $y_0$ the dual is unbounded."],
           "drawingCaption": "If no legal plan exists, b is outside the cone of A's columns and Farkas gives ȳ with Aᵀȳ ≥ 0, bᵀȳ < 0. Flip it to y = −ȳ: Aᵀy ≤ 0, bᵀy > 0, so adding ty to any dual-feasible y₀ keeps it feasible while bᵀ(y₀ + ty) → +∞."},
    1805: {"math": r"$$x_B=B^{-1}b\ge0,\ x_N=0;\quad\bar c_j=c_j-a_j^\top y\ \ (y^\top=c_B^\top B^{-1});\quad\text{optimal if all }\bar c_j\ge0$$"},
    1901: {"math": r"$$Q(x;c)=f(x)+\frac c2\Big(\|h(x)\|^2+\|\max(0,g(x))\|^2\Big),\qquad x_k\in\arg\min_xQ(x;c_k)\to x^*\ \ (c_k\to\infty)$$"},
    1902: {"math": r"$$B(x;\mu)=f(x)-\mu\sum_j\log(-g_j(x))\to+\infty\ \text{ as }g_j\to0^-,\qquad x(\mu)\to x^*\ \ (\mu\downarrow0)$$",
           "breakdown": [r"<strong>$-\log(-g_j)$ is finite inside</strong> ($g_j\lt0$) and $\to+\infty$ as $g_j\to0^-$.",
                         r"<strong>The term $-\mu\sum_j\log(-g_j)$ keeps the plane strictly inside;</strong> as $\mu\downarrow0$ the barrier weakens and the plane approaches the boundary from inside.",
                         r"<strong>Needs a strict interior:</strong> that is Slater's condition again."]},
    1903: {"math": r"$$\kappa(\nabla^2Q)=\frac{\lambda_{\max}}{\lambda_{\min}}=O(c)\to\infty\quad(c\to\infty)\implies\text{ill-conditioned}$$"},
    1904: {"math": r"$$\lambda_k=c_kh(x_k)\to\lambda^*\qquad(x_k\to x^*\ \text{regular},\ x_k\in\arg\min_xQ(x;c_k))$$"},
    1905: {"math": r"$$L_c(x,\lambda)=f(x)+\lambda^\top h(x)+\tfrac c2\|h(x)\|^2;\quad x_k\in\arg\min_xL_{c_k}(x,\lambda_k),\ \ \lambda_{k+1}=\lambda_k+c_kh(x_k)$$"},
}

FIX = build(SUBS, EXPLICIT, normalise_ids=(1505, 1602, 1603, 1606, 1608, 1801, 1807, 1802, 1808))
FIX[1604]["drawingCaption"] = ("For each fixed plan x, f(x) + μᵀg(x) is a straight line in μ. The dual function q is the lowest of all these lines, so it is concave: "
                               "q(θy₁ + (1−θ)y₂) ≥ θq(y₁) + (1−θ)q(y₂) with y = (λ, μ), whether or not the problem is convex.")
