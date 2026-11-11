"""StoMA topic 13 (jointly Gaussian). F1 picture: Max's (sector 1, sector 2) times as a Gaussian cloud; conditioning on sector 1 to predict sector 2; marginally normal is not jointly normal."""
from f1_lib import *

SUBJECT = "StoMA"

def cloud(cx, cy, rx, ry, rot, fill="#f1f5f9"):
    return E(cx, cy, rx, ry, rot, fill, 1.1)

def d1(c):
    return svg(c, ax(24, 112, 150, 14), N(150, 122, "x₁", 7, "end"), N(26, 14, "x₂", 7, "start"),
        cloud(86, 62, 50, 22, -30), C(86, 62, 2.4), N(92, 72, "μ", 8, "start"),
        arrow(86, 62, 118, 40, 1), N(124, 38, "(x − μ)ᵀΣ⁻¹(x − μ) = d²", 6.5, "start") if False else "",
        N(160, 40, "f(x) = exp(−½ d²)", 7.5, "start"), N(160, 52, "/ ((2π)^(n/2) |Σ|^(1/2))", 7, "start"),
        N(160, 70, "d² = Mahalanobis", 7.5, "start"), N(160, 81, "distance: spread-aware", 7, "start"),
        N(160, 98, "Σ ≻ 0 needed", 7, "start"),
        N(120, 136, "the outline of the cloud of (sector 1, sector 2) laps; μ is its centre", 6.5))

def d2(c):
    return svg(c, cloud(76, 56, 46, 20, -30), L(24, 104, 130, 40, 1.1), N(134, 38, "t", 8, "start"),
        arrow(76, 56, 98, 66, 1, "3 2") if False else "",
        ax(130, 118, 226, 70) if False else "",
        L(140, 112, 226, 112, 1), fn(lambda x: 112 - 36 * math.exp(-((x - 184) ** 2) / 500), 140, 226, 40, 1.1),
        N(184, 124, "tᵀX", 7.5), N(184, 64, "𝒩(tᵀμ, tᵀΣt)", 7.5), 
        N(30, 18, "X ~ 𝒩(μ, Σ) ⇔ tᵀX normal for all t", 7.5, "start"), N(120, 140, "any weighted mix of the sectors is a bell, with mean and variance from μ and Σ", 6.5))

def d3(c):
    return svg(c, ax(20, 108, 106, 20), N(60, 120, "uncorrelated", 7.5), cloud(63, 64, 30, 18, 0), N(63, 14, "Cov = 0 ⇒ independent", 7),
        ax(130, 108, 226, 20), N(178, 120, "correlated", 7.5), cloud(178, 64, 34, 14, -35), N(178, 14, "tilt ⇒ dependent", 7),
        N(120, 138, "jointly Gaussian: the cloud's axes line up with x₁, x₂ exactly when Cov = 0", 6.5))

def d4(c):
    return svg(c, ax(24, 112, 130, 16), N(130, 122, "x₂", 7, "end"), N(26, 14, "x₁", 7, "start"),
        cloud(76, 62, 46, 22, -35), L(30, 100, 126, 26, 1.1, "4 3"), L(84, 112, 84, 20, 1, "3 2"), N(84, 124, "x₂", 7),
        fn(lambda y: 84 + 26 * math.exp(-((y - 59) ** 2) / 80), 20, 100, 30, 1.1) if False else "",
        N(156, 36, "X₁ | X₂ = x₂ ~ 𝒩(m, S)", 7.5, "start"), N(156, 50, "m = μ₁ + Σ₁₂Σ₂₂⁻¹(x₂ − μ₂)", 7, "start"),
        N(156, 62, "S = Σ₁₁ − Σ₁₂Σ₂₂⁻¹Σ₂₁", 7, "start"), N(156, 80, "m is the LLSE; S its error:", 7, "start"), N(156, 91, "MMSE = LLSE for Gaussians", 7, "start"),
        N(120, 140, "slice the cloud at x₂: a bell, centred on the line, narrower than the cloud", 6.5))

def d5(c):
    return svg(c, R(20, 36, 70, 40, "#f1f5f9", 1, 3), N(55, 52, "[ a  b ]", 8), N(55, 66, "[ b  c ]", 8), N(55, 30, "−½ zᵀPz in the exponent", 7),
        arrow(96, 56, 134, 56, 1), N(115, 48, "invert", 7.5),
        R(140, 36, 80, 40, "#d9dee7", 1, 3), N(180, 52, "1/(ac−b²) [ c  −b ]", 7.5), N(180, 66, "[ −b   a ]", 7.5), N(180, 30, "Σ = P⁻¹", 7.5),
        N(120, 100, "the matrix in the exponent is the INVERSE covariance", 7.5), N(120, 114, "read variances from Σ = P⁻¹, not from P", 7.5), N(120, 130, "e.g. Var(X) = c/(ac − b²)", 7.5))

def d6(c):
    pts = [(x, 58 - (x - 120) * 0.7) for x in range(70, 171, 20) if x < 120] + [(x, 58 + (x - 120) * 0.7) for x in range(70, 171, 20) if x < 120]
    out = ax(24, 112, 226, 10) + N(226, 122, "X", 7, "end") + N(28, 10, "Y", 7, "start")
    out += L(60, 22, 180, 100, 1.1) + L(60, 100, 180, 22, 1.1)
    out += "".join(C(x, y, 1.8) for x, y in [(75, 90), (90, 80), (110, 66), (140, 46), (160, 34), (75, 32), (92, 42), (112, 56), (140, 76), (168, 94)])
    out += N(190, 28, "Y = S·X", 7.5, "start") + N(190, 40, "S = ±1 coin", 7, "start") + N(190, 70, "X + Y = 0", 7, "start") + N(190, 80, "half the time", 7, "start")
    out += N(120, 130, "X, Y each 𝒩(0,1) and Cov = 0, yet ℙ(X + Y = 0) = ½:", 6.8) + N(120, 140, "not jointly Gaussian, so uncorrelated ≠ independent", 6.8)
    return svg(c, out)

CARDS = {
31301: dict(d=d1, kind="DEFINITION",
  stmt=r"<b>Multivariate normal density.</b> $X\in\mathbb R^n$ is $\mathcal N(\mu,\Sigma)$ with $\Sigma\succ0$ if it has density $f_X(x)=\dfrac{1}{(2\pi)^{n/2}|\Sigma|^{1/2}}\exp\!\left(-\tfrac12(x-\mu)^\top\Sigma^{-1}(x-\mu)\right)$ (Ross 7.8; Grimmett 4.9).",
  hint='How does a bell curve in many dimensions know the spread and the tilt of the cloud of sector times?',
  bd=[r"<strong>$\mu$ = the centre of the cloud.</strong> Max's average (sector 1, sector 2) times over many laps; the density peaks there.",
      r"<strong>$(x-\mu)^\top\Sigma^{-1}(x-\mu)$ = squared Mahalanobis distance.</strong> Distance from the centre measured in the cloud's own spread and tilt, so tilted stretches count as short.",
      r"<strong>$(2\pi)^{n/2}|\Sigma|^{1/2}$ = the normaliser.</strong> It makes the total volume 1; a larger cloud (bigger $|\Sigma|$) means a lower peak."],
  conn="<strong>A cloud shaped by Σ.</strong> Max's laps scatter around his typical lap in an oval: a slow sector 1 tends to come with a slow sector 2. A lap far along the long axis of the oval counts as normal; the same distance across it (fast sector 1, slow sector 2) counts as strange.",
  cap="The outline of the cloud of (sector 1, sector 2) laps around its centre μ. The density falls with the Mahalanobis distance d² = (x − μ)ᵀΣ⁻¹(x − μ), measured in the cloud's own shape."),
31302: dict(d=d2, kind="THEOREM",
  stmt=r"<b>Linear projections.</b> $X\sim\mathcal N(\mu,\Sigma)$ in $\mathbb R^n$ if and only if for every $t\in\mathbb R^n$, $t^\top X\sim\mathcal N(t^\top\mu,\,t^\top\Sigma t)$. Consequently, $AX+b\sim\mathcal N(A\mu+b,A\Sigma A^\top)$ (Ross 7.8; Grimmett 4.9).",
  hint='What law does any weighted total of jointly Gaussian sector times follow?',
  bd=[r"<strong>$t^\top X$ = a weighted total of the sectors.</strong> For instance sector 1 plus sector 2 plus sector 3, the whole lap: look at the cloud along direction $t$.",
      r"<strong>$t^\top\mu$ = the weighted mean.</strong> Means combine linearly, as always.",
      r"<strong>$t^\top\Sigma t$ = the weighted variance.</strong> Spread along $t$ comes from the covariance table; the shape is still a bell for every $t$."],
  conn='<strong>Every mix is a bell.</strong> Whatever weighted combination of the sector times you take, the full lap or sector 2 minus sector 1, the result has a bell-curve law with a mean and variance you can read off.',
  cap='A cloud X and a direction t. The projection tᵀX onto t is a bell with mean tᵀμ and variance tᵀΣt, and this holds for every direction t.'),
31303: dict(d=d3, kind="THEOREM",
  stmt=r"<b>Uncorrelated implies independent (Gaussian case).</b> If $(X_1,\ldots,X_n)$ is jointly Gaussian, then $X_i,X_j$ with $\operatorname{Cov}(X_i,X_j)=0$ are independent; more generally, the vector splits into independent blocks iff the cross-covariances vanish, because the density factorises (Ross 7.8; Grimmett 4.9).",
  hint='For a jointly Gaussian pair of sector times, what does zero covariance tell you about independence?',
  bd=[r"<strong>$\operatorname{Cov}(X_i,X_j)=0$ = the cloud has no tilt.</strong> Its axes line up with the coordinate directions.",
      r"<strong>$f_X=\prod f_{X_i}$ = the density factorises.</strong> With a diagonal $\Sigma$, the exponent is a sum of separate squares, so the density is a product.",
      '<strong>Only for jointly Gaussian.</strong> For other laws, zero covariance misses non-linear links such as $Y=X^2$.'],
  conn="<strong>No tilt, no link.</strong> If Max's sector 1 and sector 2 times are jointly bell-shaped and uncorrelated, then knowing one tells you nothing about the other; the oval is not tilted.",
  cap='Left: an untilted cloud, Cov = 0, whose density is a product f(x₁)f(x₂): independent. Right: a tilted cloud, Cov ≠ 0: dependent.'),
31304: dict(d=d4, kind="THEOREM",
  stmt=r"<b>Gaussian conditioning.</b> If $(X_1,X_2)\sim\mathcal N(\mu,\Sigma)$ with $\Sigma_{22}\succ0$, then $X_1\mid X_2=x_2\sim\mathcal N\bigl(\mu_1+\Sigma_{12}\Sigma_{22}^{-1}(x_2-\mu_2),\ \Sigma_{11}-\Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21}\bigr)$. So $\mathbb E[X_1\mid X_2]$ equals the LLSE: MMSE $=$ LLSE (Ross 7.8; Grimmett 4.9).",
  hint='Given one jointly Gaussian sector time, what is the law of the other, and how does it compare to the best straight-line guess?',
  bd=[r"<strong>$\mu_1+\Sigma_{12}\Sigma_{22}^{-1}(x_2-\mu_2)$ = the conditional mean.</strong> It is exactly the straight-line LLSE: the guess moves linearly with what you see.",
      r"<strong>$\Sigma_{11}-\Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21}$ = the conditional spread.</strong> The Schur complement; it does not depend on the value $x_2$ you saw.",
      '<strong>Still normal.</strong> Slicing a Gaussian cloud gives a Gaussian slice, so the best guess of any kind is the linear one.'],
  conn="<strong>Slicing the cloud.</strong> Among Max's laps with the same sector 2 time, the sector 1 times form a bell centred on the regression line, narrower than over all laps, and equally wide whatever the sector 2 time was.",
  cap='The cloud sliced at x₂ gives a narrower bell for X₁, centred on the line m = μ₁ + Σ₁₂Σ₂₂⁻¹(x₂ − μ₂) with spread S = Σ₁₁ − Σ₁₂Σ₂₂⁻¹Σ₂₁.'),
31305: dict(d=d5, kind="WORKED EXAMPLE",
  stmt=r"<b>Reading moments from the exponent.</b> If $f(x,y)\propto\exp\!\bigl(-\tfrac12[x\ y]\,P\,[x\ y]^\top\bigr)$ with $P=\begin{bmatrix}a&b\\b&c\end{bmatrix}\succ0$, then $(X,Y)$ is centred Gaussian with $\Sigma=P^{-1}=\dfrac1{ac-b^2}\begin{bmatrix}c&-b\\-b&a\end{bmatrix}$, so $\operatorname{Var}X=\dfrac{c}{ac-b^2}$ (Grimmett 4.9).",
  hint='Given only the quadratic form in the exponent, how do you read off variances and covariance?',
  bd=[r"<strong>$-\tfrac12z^\top Pz$ = the exponent.</strong> The matrix in the exponent is the inverse covariance $P=\Sigma^{-1}$ (the precision matrix).",
      r"<strong>$\Sigma=P^{-1}$ = invert it.</strong> For a $2\times2$ matrix, swap the diagonal, negate the off-diagonal, and divide by the determinant $ac-b^2$.",
      r"<strong>$\operatorname{Var}X=\frac{c}{ac-b^2}$ = not $1/a$.</strong> The variance is read from $\Sigma$, never from the diagonal of $P$; $\operatorname{Cov}=\frac{-b}{ac-b^2}$."],
  conn="<strong>Recipe from the formula.</strong> A Red Bull engineer hands you the exponent of the joint density of Max's two sector times. Invert its matrix and you get the covariances, so you know how the two sectors move together.",
  cap='The matrix P in the exponent, inverted: Σ = P⁻¹ = (1/(ac − b²)) [c, −b; −b, a]. Variances come from Σ, such as Var(X) = c/(ac − b²), not from P directly.'),
31306: dict(d=d6, kind="WORKED EXAMPLE",
  stmt=r"<b>Normal marginals, not jointly normal.</b> Let $X\sim\mathcal N(0,1)$, $S=\pm1$ with probability $\tfrac12$ each, independent of $X$, and $Y=SX$. Then $Y\sim\mathcal N(0,1)$ and $\operatorname{Cov}(X,Y)=\mathbb E[S]\mathbb E[X^2]=0$, but $\mathbb P(X+Y=0)=\mathbb P(S=-1)=\tfrac12$, so $X+Y$ is not normal (a normal law has no atoms): $(X,Y)$ is not jointly Gaussian and $X,Y$ are dependent (Ross 7.8; Grimmett 4.9).",
  hint='Can two bell-shaped variables with zero covariance still be dependent?',
  bd=['<strong>$Y=SX$ = flip the sign at random.</strong> With a fair coin $S$, $Y$ is $X$ or $-X$, which is again a standard normal.',
      r"<strong>$\operatorname{Cov}(X,Y)=0$ = no straight-line link.</strong> The coin makes the covariance average to zero.",
      r"<strong>$\mathbb P(X+Y=0)=\tfrac12$ = a weighted total with an atom.</strong> A jointly Gaussian pair would make $X+Y$ normal, with no atoms, so the pair is not jointly Gaussian."],
  conn="<strong>Each a bell, but a cross, not an oval.</strong> Imagine a timing glitch that flips the sign of Max's sector 2 deviation at random. Sector 1 and sector 2 deviations are each bell-shaped, but their pairs lie on the two diagonals instead of in a cloud.",
  cap='Points (X, Y = SX) of sector deviations lie on the two diagonals instead of an oval cloud. Both X and Y are 𝒩(0,1) with Cov = 0, but ℙ(X + Y = 0) = ½, so the pair is not jointly Gaussian.'),
}

STORY = {
31301: dict(s="STORY 13 · STEP 1 · THE BELL IN MANY DIMENSIONS", b="The <b>multivariate normal</b> is a cloud whose density falls with the spread-aware distance from the centre.", f=[["31101", "the covariance matrix"], ["30305", "the one-dimensional bell"]], n=[["31302", "its linear mixes"], ["31305", "reading Σ from the exponent"]]),
31302: dict(s="STORY 13 · STEP 2 · EVERY MIX IS A BELL", b='Every <b>weighted total</b> of jointly Gaussian sector times is normal, with mean and variance from μ and Σ.', f=[["31301", "the joint density"], ["30905", "sums of normals"]], n=[["31303", "zero covariance"], ["31304", "conditioning"]]),
31303: dict(s="STORY 13 · STEP 3 · NO TILT", b="For jointly Gaussian pairs, <b>uncorrelated means independent</b>.", f=[["31302", "linear projections"], ["30506", "the general failure"]], n=[["31306", "when joint Gaussianity fails"]]),
31304: dict(s="STORY 13 · STEP 4 · SLICING", b="Slicing a Gaussian cloud gives a Gaussian whose mean is the <b>LLSE</b>: <b>MMSE = LLSE</b>.", f=[["31103", "the LLSE"], ["31205", "line versus curve"]], n=[["32506", "Gaussian process regression"]]),
31305: dict(s="STORY 13 · STEP 5 · A RECIPE", b="The matrix in the exponent is the <b>inverse</b> covariance: invert it to read variances.", f=[["31301", "the density"]], n=[["32506", "kernel matrices"]]),
31306: dict(s="STORY 13 · STEP 6 · THE TRAP", b="Normal marginals do <b>not</b> make a normal pair: a random sign gives a cross-shaped cloud.", f=[["31303", "uncorrelated vs independent"]], n=[["31502", "convergence in distribution is only marginal"]]),
}

FIX = build(CARDS)
