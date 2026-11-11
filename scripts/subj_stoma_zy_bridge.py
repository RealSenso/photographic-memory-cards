"""StoMA bridge facts (12 Nov 2026): steps the practice questions need that no card stated.
Each is added as an extra breakdown bullet on the card where it belongs (run as a POST pass, before the notation pass)."""

SUBJECT = "StoMA"
FIX = {}

BRIDGE = {
    # Cantelli's one-sided Chebyshev (practice 30692)
    30602: r"<strong>$\mathbb P(X-\mu\ge a)\le\dfrac{\sigma^2}{\sigma^2+a^2}$ = one side only (Cantelli).</strong> For laps slower than average by at least $a$, shift by any $u\ge0$: $\mathbb P(X-\mu\ge a)\le\mathbb P\big((X-\mu+u)^2\ge(a+u)^2\big)\le\frac{\sigma^2+u^2}{(a+u)^2}$, and $u=\sigma^2/a$ gives the bound. Halving Chebyshev is not valid.",
    # chi-square with n degrees of freedom (practice 31393, Mahalanobis distance)
    30905: r"<strong>$Z_1^2+\cdots+Z_n^2\sim\chi^2_n=\mathrm{Gamma}(\tfrac n2,\tfrac12)$ = squared normals add up.</strong> Each $Z_i^2$ is $\chi^2_1=\mathrm{Gamma}(\frac12,\frac12)$ (4.05), so $n$ independent ones add to $\mathrm{Gamma}(\frac n2,\frac12)$, with mean $n$ and variance $2n$.",
    # delta method (practice 31893)
    31505: r"<strong>$\sqrt n\,(g(\bar X_n)-g(\mu))\xrightarrow{d}\mathcal N(0,g'(\mu)^2\sigma^2)$ = the delta method.</strong> Taylor: $g(\bar X_n)-g(\mu)=g'(\xi_n)(\bar X_n-\mu)$ with $\xi_n$ between them, so $g'(\xi_n)\xrightarrow{P}g'(\mu)$ and Slutsky multiplies the CLT limit by $g'(\mu)$ (needs $g'$ continuous at $\mu$, $g'(\mu)\ne0$).",
    # martingale convergence (practice 32693)
    32606: r"<strong>$\sup_n\mathbb E|M_n|\lt\infty\Rightarrow M_n\to M_\infty$ a.s. = martingales settle (Doob's convergence theorem).</strong> A martingale that stays bounded in mean, for instance one in $[0,1]$ like Max's live win probability, converges almost surely; bounded ones also converge in $L^1$, so $\mathbb E[M_\infty]=\mathbb E[M_0]$.",
}


def POST(c):
    """add the bridge bullet once (idempotent: the bullet is matched by its opening)"""
    b = BRIDGE.get(c["id"])
    if b and isinstance(c.get("breakdown"), list) and not any(x[:60] == b[:60] for x in c["breakdown"]):
        c["breakdown"] = c["breakdown"] + [b]
