"""StoMA topic 11 (covariance matrices, LLSE). Commute picture: predict the ride time Y from what the phone shows at the stop."""
from commute_lib import *

SUBJECT = "StoMA"
PTS = [(52, 92), (64, 80), (72, 84), (84, 66), (92, 72), (104, 58), (114, 62), (126, 44), (138, 50), (150, 36)]

def scatter(pts=PTS):
    return "".join(C(x, y, 1.8) for x, y in pts)

def d1(c):
    return svg(c, ax(24, 112, 130, 14), N(130, 122, "wait", 7, "end"), N(26, 14, "ride", 7, "start"),
        E(76, 64, 44, 18, -35, "#f1f5f9", 1), arrow(76, 64, 118, 36, 1), N(120, 32, "v", 8, "start"),
        N(150, 46, "Σ = 𝔼[(X − μ)(X − μ)ᵀ]", 7.5, "start"), N(150, 62, "vᵀΣv = Var(vᵀX) ≥ 0", 7.5, "start"), N(150, 76, "so Σ ⪰ 0", 7.5, "start"),
        N(150, 94, "Σ(AX+b) = A Σ Aᵀ", 7.5, "start"),
        N(120, 138, "any direction v through the cloud has spread ≥ 0", 6.5))

def d2(c):
    return svg(c, L(24, 112, 150, 112, 1.1), N(150, 124, "span of what you see: X", 7, "end"),
        arrow(24, 112, 120, 38, 1), N(124, 34, "Y", 8, "start"),
        arrow(24, 112, 120, 112, 1), N(110, 124, "Ŷ", 8, "start") if False else N(122, 108, "Ŷ", 8, "start"),
        arrow(120, 112, 120, 40, 1, "3 2"), N(124, 46, "Y − Ŷ", 7.5, "start"),
        L(120, 104, 112, 104, 1) + L(112, 104, 112, 112, 1),
        N(134, 60, "𝔼[Y − Ŷ] = 0", 7.5, "start"), N(134, 72, "𝔼[(Y − Ŷ)Xᵀ] = 0", 7.5, "start"), N(134, 90, "error ⟂ the data", 7.5, "start"),
        N(120, 138, "shortest error = perpendicular error: the minimiser", 7))

def d3(c):
    return svg(c, ax(24, 112, 226, 14), N(226, 124, "X: phone ETA", 7, "end"), N(28, 14, "Y: ride", 7, "start"),
        scatter([(x + 12, y + 16) for x, y in PTS][:10]) if False else scatter([(x + 30, y + 18) for x, y in PTS]),
        L(60, 112, 200, 30, 1.2), C(130, 71, 2.8, "#ffffff", 1.2), dash(130, 71, 130, 112), dash(24, 71, 130, 71),
        N(130, 124, "μX", 7.5), N(18, 74, "μY", 7.5, "end"),
        N(36, 28, "Ŷ = μY + K(X − μX)", 7.5, "start"), N(36, 40, "K = ΣYX ΣX⁻¹ = slope", 7.5, "start"),
        N(120, 138, "line through the means, tilted by how X and Y move together", 6.8))

def d4(c):
    return svg(c, ax(24, 112, 226, 14), N(226, 124, "X", 7, "end"), N(28, 14, "Y", 7, "start"),
        scatter([(x + 30, y + 18) for x, y in PTS]), L(60, 112, 200, 30, 1.1),
        L(214, 30, 214, 108, 1.2), N(220, 70, "ΣY", 7.5, "start"), L(206, 30, 222, 30, 1) + L(206, 108, 222, 108, 1),
        L(190, 66, 190, 84, 1.2), N(185, 78, "Σe", 7.5, "end"), L(184, 66, 196, 66, 1) + L(184, 84, 196, 84, 1),
        N(36, 26, "Σe = ΣY − ΣYX ΣX⁻¹ ΣXY ⪯ ΣY", 7, "start"), N(120, 138, "knowing X removes the explained part of the spread", 7))

def d5(c):
    return svg(c, L(40, 106, 170, 106, 1.2), L(170, 106, 170, 40, 1.2), L(40, 106, 170, 40, 1.2),
        N(105, 120, "ρσY (explained)", 7.5), N(212, 76, "σY√(1 − ρ²) (error)", 7.5, "end"), N(92, 66, "σY", 8, "end"),
        L(158, 106, 158, 94, 1) + L(158, 94, 170, 94, 1),
        N(36, 22, "σY² = ρ²σY² + σY²(1 − ρ²)", 7.5, "start"), N(36, 34, "MSE = σY²(1 − ρ²)", 7.5, "start"),
        N(120, 138, "Ŷ = μY + ρ(σY/σX)(X − μX): the slope is ρ in standard units", 6.8))

def d6(c):
    return svg(c, L(24, 70, 226, 70, 1, ar=True), N(226, 82, "minutes off usual", 7, "end"),
        L(124, 66, 124, 74, 1) + N(124, 84, "0", 7),
        C(174, 70, 3), N(174, 58, "Y (what the phone says)", 7, "middle"),
        C(154, 70, 3, "#ffffff"), N(154, 98, "X̂ = shrink Y", 7.5), L(124, 44, 174, 44, 1.1) + N(150, 38, "Y = X + W", 7.5),
        N(30, 18, "X̂ = σX²/(σX² + σW²) · Y", 7.5, "start"),
        N(120, 116, "MSE = σX²σW² / (σX² + σW²)", 7.5), N(120, 130, "trust the phone only as much as signal outweighs noise", 7), N(120, 141, "SNR = σX²/σW²", 7))

CARDS = {
31101: dict(d=d1, kind="THEOREM",
  stmt=r"<b>Covariance matrix.</b> For a random vector $X$ with mean $\mu$, $\Sigma_X=\mathbb E[(X-\mu)(X-\mu)^\top]$ is symmetric and positive semidefinite: $v^\top\Sigma_Xv=\operatorname{Var}(v^\top X)\ge0$ for all $v$. Also $\Sigma_{AX+b}=A\Sigma_XA^\top$ (Grimmett 3.6; Ross 7.4).",
  hint="Why can a table of covariances between wait, ride and delay never have a negative direction?",
  bd=[r"<strong>$\Sigma_X=\mathbb E[(X-\mu)(X-\mu)^\top]$ = all variances and covariances in one table.</strong> Entry $(i,j)$ is how leg $i$ and leg $j$ move together.",
      r"<strong>$v^\top\Sigma_Xv=\operatorname{Var}(v^\top X)$ = the spread along direction $v$.</strong> Any weighted mix of the legs has a variance, which cannot be negative.",
      r"<strong>$\Sigma_{AX+b}=A\Sigma_XA^\top$ = how the table transforms.</strong> Shifting by $b$ changes nothing; mixing by $A$ sandwiches $\Sigma$."],
  conn=r"<strong>The cloud of mornings.</strong> Plot each morning as (wait, ride). The cloud has a shape, and along any direction you cut it, its spread is a variance: zero or more.",
  cap="The cloud of (wait, ride) mornings, its tilted outline, and a direction v. The spread of the projection onto v is vᵀΣv = Var(vᵀX), never negative, so Σ ⪰ 0."),
31102: dict(d=d2, kind="THEOREM",
  stmt=r"<b>Orthogonality principle.</b> Among estimators $\hat Y=a+BX$, $\hat Y$ minimises $\mathbb E\|Y-\hat Y\|^2$ iff $\mathbb E[Y-\hat Y]=0$ and $\mathbb E[(Y-\hat Y)X^\top]=0$: the error is orthogonal to the constants and to the observations (Grimmett 7.9; Papoulis).",
  hint="Among all straight-line guesses from what you see, which one leaves the smallest squared error?",
  bd=[r"<strong>$\hat Y$ = a guess built linearly from $X$.</strong> It lies in the flat set of things you can compute from what you observe.",
      r"<strong>$\mathbb E[Y-\hat Y]=0$ = no bias.</strong> The error averages to zero: you are neither too early nor too late on average.",
      r"<strong>$\mathbb E[(Y-\hat Y)X^\top]=0$ = error orthogonal to the data.</strong> If any leftover linked to $X$, you could use it to improve the guess."],
  conn=r"<strong>The shortest miss.</strong> Like dropping a perpendicular from a point to a floor, the best guess from what you see is where the remaining error points straight away from everything you observed.",
  cap="The ride Y as an arrow and the flat set of linear guesses from X. The best guess Ŷ is the foot of the perpendicular, and the error Y − Ŷ is orthogonal to X."),
31103: dict(d=d3, kind="THEOREM",
  stmt=r"<b>Linear least squares estimator.</b> If $\Sigma_X$ is invertible, the linear estimator of $Y$ from $X$ minimising mean squared error is $\hat Y=\mu_Y+\Sigma_{YX}\Sigma_X^{-1}(X-\mu_X)$, with gain $K=\Sigma_{YX}\Sigma_X^{-1}$ (Grimmett 7.9; Ross 7.4).",
  hint="What is the best straight-line prediction of the ride from the phone's ETA, using only means and covariances?",
  bd=[r"<strong>$\mu_Y+\ldots$ = start from the average ride.</strong> With no information, the best guess is the mean.",
      r"<strong>$X-\mu_X$ = how unusual the signal is.</strong> The ETA's deviation from its own average is the news you add.",
      r"<strong>$K=\Sigma_{YX}\Sigma_X^{-1}$ = the gain.</strong> How much of the ETA's surprise to pass on: covariance with the ride, divided by the ETA's own spread."],
  conn=r"<strong>Reading the phone.</strong> The phone says 4 minutes more than usual. If its surprises usually carry over to the ride, you pass most of them on; if not, you add little to your usual guess.",
  cap="The scatter of (ETA X, ride Y). The best straight line passes through the means (μX, μY) with slope K = ΣYX ΣX⁻¹: Ŷ = μY + K(X − μX)."),
31104: dict(d=d4, kind="THEOREM",
  stmt=r"<b>Error covariance.</b> For the LLSE $\hat Y$, the error $e=Y-\hat Y$ has mean $0$ and covariance $\Sigma_e=\Sigma_Y-\Sigma_{YX}\Sigma_X^{-1}\Sigma_{XY}\preceq\Sigma_Y$, the Schur complement of $\Sigma_X$ in the joint covariance (Grimmett 7.9).",
  hint="How much of the ride's spread is left after you use the phone's reading?",
  bd=[r"<strong>$\Sigma_Y$ = spread with no information.</strong> The total variation of the ride across mornings.",
      r"<strong>$\Sigma_{YX}\Sigma_X^{-1}\Sigma_{XY}$ = the explained part.</strong> The share of the spread that moves in step with the ETA.",
      r"<strong>$\Sigma_e\preceq\Sigma_Y$ = never worse.</strong> What remains is what the signal cannot explain; extra data can only shrink it."],
  conn=r"<strong>What the phone cannot tell you.</strong> Even with the ETA, some mornings surprise you. The leftover spread is the total spread minus the part the ETA explains.",
  cap="The vertical spread ΣY of the rides, and the smaller spread Σe around the regression line. Σe = ΣY − ΣYX ΣX⁻¹ ΣXY is what is left after using X."),
31105: dict(d=d5, kind="THEOREM",
  stmt=r"<b>Scalar LLSE.</b> For scalar $X,Y$ with $\sigma_X>0$, $\hat Y=\mu_Y+\rho\frac{\sigma_Y}{\sigma_X}(X-\mu_X)$ with $\rho=\frac{\operatorname{Cov}(X,Y)}{\sigma_X\sigma_Y}$, and $\mathbb E(Y-\hat Y)^2=\sigma_Y^2(1-\rho^2)$ (Ross 7.4; Grimmett 3.6).",
  hint="How does one number, the correlation, set both the slope of the prediction and how good it is?",
  bd=[r"<strong>$\rho=\frac{\operatorname{Cov}(X,Y)}{\sigma_X\sigma_Y}$ = covariance in standard units.</strong> A pure number between $-1$ and $1$: how tightly the ETA and ride move together.",
      r"<strong>$\rho\frac{\sigma_Y}{\sigma_X}$ = the slope.</strong> A one-spread surprise in the ETA predicts a $\rho$-spread surprise in the ride.",
      r"<strong>$\sigma_Y^2(1-\rho^2)$ = the error.</strong> A share $\rho^2$ of the ride's variance is explained; the rest is left."],
  conn=r"<strong>How much to believe the ETA.</strong> If ETA and ride have correlation 0.9, the ETA explains 81% of how the ride varies; with correlation 0 it explains nothing and you stay with the average.",
  cap="A right triangle: hypotenuse σY (total spread), one leg ρσY (explained by X), the other σY√(1 − ρ²) (error). Pythagoras gives MSE = σY²(1 − ρ²)."),
31106: dict(d=d6, kind="WORKED EXAMPLE",
  stmt=r"<b>Wiener filter (scalar).</b> Let $Y=X+W$ with $X,W$ independent, zero mean, variances $\sigma_X^2,\sigma_W^2$. Then $\hat X(Y)=\frac{\sigma_X^2}{\sigma_X^2+\sigma_W^2}Y$ and $\operatorname{MSE}=\frac{\sigma_X^2\sigma_W^2}{\sigma_X^2+\sigma_W^2}$ (Grimmett 7.9; Ross 7.4).",
  hint="The phone shows ride plus noise. How much of what it shows should you trust?",
  bd=[r"<strong>$Y=X+W$ = the true ride plus phone noise.</strong> What you see is the signal $X$ blurred by independent error $W$.",
      r"<strong>$\frac{\sigma_X^2}{\sigma_X^2+\sigma_W^2}$ = the trust factor.</strong> Close to 1 if the signal's spread dominates, close to 0 if the noise does; the estimate shrinks $Y$ toward 0.",
      r"<strong>$\frac{\sigma_X^2\sigma_W^2}{\sigma_X^2+\sigma_W^2}$ = the error left.</strong> It is smaller than both $\sigma_X^2$ and $\sigma_W^2$: combining knowledge helps."],
  conn=r"<strong>A noisy ETA.</strong> The phone says 10 minutes more than usual. If its numbers are very noisy, you shade that down to a fraction; if it is accurate, you take it almost at face value.",
  cap="The reading Y = X + W on a line of minutes off usual, and the estimate X̂ pulled toward 0 by the trust factor σX²/(σX² + σW²), with the leftover error σX²σW²/(σX² + σW²)."),
}

STORY = {
31101: dict(s="STORY 11 · STEP 1 · THE TABLE OF SPREADS", b="All variances and covariances live in one <b>covariance matrix</b>, and every direction's spread is non-negative.", f=[["30503", "covariance of a sum"]], n=[["31102", "using it to estimate"], ["31301", "the Gaussian density"]]),
31102: dict(s="STORY 11 · STEP 2 · THE SHORTEST MISS", b="The best linear guess is the one whose <b>error is orthogonal</b> to everything observed.", f=[["31101", "covariances as inner products"], ["30605", "Cauchy–Schwarz geometry"]], n=[["31103", "the formula"], ["31202", "the nonlinear version"]]),
31103: dict(s="STORY 11 · STEP 3 · THE FORMULA", b="Orthogonality gives the <b>LLSE</b>: the mean plus a gain times the surprise.", f=[["31102", "orthogonality"]], n=[["31104", "how good it is"], ["31105", "the scalar case"]]),
31104: dict(s="STORY 11 · STEP 4 · WHAT IS LEFT", b="The error covariance is the total spread <b>minus the explained part</b> (a Schur complement).", f=[["31103", "the LLSE"]], n=[["31304", "Gaussian conditioning gives the same"]]),
31105: dict(s="STORY 11 · STEP 5 · ONE NUMBER", b="In one dimension, <b>correlation ρ</b> sets both the slope and the error 1 − ρ².", f=[["31103", "LLSE"]], n=[["31106", "a noisy measurement"], ["32502", "kernels for Brownian paths"]]),
31106: dict(s="STORY 11 · STEP 6 · NOISY READING", b="The <b>Wiener filter</b> shrinks a noisy reading by signal over signal-plus-noise.", f=[["31105", "scalar LLSE"]], n=[["31201", "the unconstrained best guess"], ["32506", "Gaussian process regression"]]),
}

FIX = build(CARDS)
