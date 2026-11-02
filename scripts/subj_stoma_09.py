"""StoMA topic 09 (sums and Jacobian transformations). Commute picture: door-to-door time = walk + wait + ride."""
from commute_lib import *

SUBJECT = "StoMA"
HUMP = lambda cx, w=22, h=40, base=100: (lambda x: base - h * math.exp(-((x - cx) ** 2) / (2 * w * w)))

def d1(c):
    base = 100
    fx, fy = HUMP(70), HUMP(120)
    return svg(c, ax(20, base, 226, 18), N(226, 112, "x", 7, "end"),
        fn(fx, 24, 140, 50, 1.1), N(60, 52, "fX(x)", 7.5),
        fn(lambda x: HUMP(120)(x), 70, 190, 50, 1.1, "4 3"), N(150, 52, "fY(z − x), flipped and slid to z", 7, "start"),
        area(lambda x: base - min(40 * math.exp(-((x - 70) ** 2) / 968), 40 * math.exp(-((x - 120) ** 2) / 968)), 70, 120, base, 25),
        dash(120, base, 120, 52), N(120, 112, "z", 7.5),
        N(30, 28, "f(z) = ∫ fX(x) fY(z − x) dx = overlap area at z", 7.5, "start"), N(120, 138, "sum of independent legs: slide one density over the other", 7))

def d2(c):
    return svg(c,
        ax(20, 100, 100, 28), N(100, 112, "u", 7, "end"), N(22, 24, "v", 7, "start"), R(36, 62, 20, 20, "#f1f5f9", 1), N(46, 74, "du dv", 6.5),
        arrow(108, 68, 134, 68, 1), N(121, 62, "x(u,v), y(u,v)", 6, "middle"),
        ax(140, 100, 226, 28), N(226, 112, "x", 7, "end"), N(142, 24, "y", 7, "start"), PG("164,86 192,82 202,56 176,60", "#f1f5f9", 1), N(186, 74, "dx dy", 6.5),
        N(120, 12, "a small box in (u,v) becomes a tilted box in (x,y)", 7),
        N(120, 124, "fU,V(u,v) = fX,Y(x(u,v), y(u,v)) · |det ∂(x,y)/∂(u,v)|", 6.8), N(120, 138, "the determinant is the area-stretch factor", 7))

def d3(c):
    return svg(c, ax(24, 108, 130, 16), N(130, 119, "x", 7, "end"), N(26, 14, "y", 7, "start"),
        L(24, 108, 112, 40, 1, "4 3"), N(114, 38, "slope z = y/x", 7, "start"),
        C(94, 54, 2.6), N(100, 68, "(x, y)", 7, "start"), L(24, 108, 94, 54, 1.1), N(54, 70, "r", 7.5), 
        P("M 46,108 A 22,22 0 0 0 44,92", "none", 1), N(52, 100, "θ", 7.5, "start"),
        N(150, 50, "ratio: Z = Y/X", 7.5, "start"), N(150, 62, "f(z) = ∫ |x| f(x, xz) dx", 7, "start"),
        N(150, 84, "polar: area element r dr dθ", 7.5, "start"), N(150, 96, "f(r, θ) = r f(r cosθ, r sinθ)", 7, "start"),
        N(120, 138, "a line through the origin keeps the ratio fixed; r is the extra stretch", 6.5))

def d4(c):
    return svg(c, ax(24, 108, 130, 16), N(130, 119, "Z₁", 7, "end"), N(26, 14, "Z₂", 7, "start"),
        circ(77, 62, 36, "none", 1, "3 2"), L(77, 62, 106, 40, 1.1), C(106, 40, 2.6), N(112, 36, "(Z₁, Z₂)", 7, "start"),
        L(106, 40, 106, 62, 1, "3 2"), L(77, 62, 106, 62, 1, "3 2"), N(86, 52, "R", 7.5), P("M 91,62 A 14,14 0 0 0 89,53", "none", 1), N(98, 70, "2πU₂", 7, "start"),
        N(150, 44, "R = √(−2 ln U₁)", 7.5, "start"), N(150, 58, "angle = 2πU₂", 7.5, "start"), N(150, 78, "Z₁ = R cos(2πU₂)", 7.5, "start"), N(150, 90, "Z₂ = R sin(2πU₂)", 7.5, "start"),
        N(120, 138, "two uniform random numbers give two independent normals", 7))

def d5(c):
    b = 100
    return svg(c, ax(20, b, 226, 18), N(226, 112, "minutes", 7, "end"),
        fn(HUMP(50, 10, 34), 24, 100, 40, 1.1), N(50, 60, "walk", 7), fn(HUMP(90, 12, 30), 40, 150, 40, 1.1), N(92, 66, "wait", 7),
        fn(HUMP(170, 26, 22), 60, 226, 50, 1.1), N(170, 76, "total: wider", 7.5),
        N(30, 24, "𝒩(μ₁,σ₁²) + 𝒩(μ₂,σ₂²) = 𝒩(μ₁+μ₂, σ₁²+σ₂²)", 7, "start"), N(30, 34, "Pois(λ₁) + Pois(λ₂) = Pois(λ₁+λ₂)", 7, "start"),
        N(120, 138, "means add, variances add, and the family stays the same", 7))

def d6(c):
    b = 104
    return svg(c, ax(20, b, 226, 20), N(226, 116, "z", 7, "end"), N(24, 18, "f(z)", 7.5, "start"),
        N(30, 40, "each leg flat on [0, 1]", 7, "start"),
        PG("60,104 120,34 180,104", "#d9dee7", 1.1), N(120, 28, "peak at 1", 7.5), 
        tick(60, 104, "0"), tick(120, 104, "1"), tick(180, 104, "2"),
        N(66, 52, "f = z", 7.5, "end"), N(176, 52, "f = 2 − z", 7.5, "start"),
        N(120, 130, "𝔼[Z] = 1,  Var(Z) = ⅙", 7.5), N(120, 140, "two flat legs add to a tent", 7))

CARDS = {
30901: dict(d=d1, kind="THEOREM",
  stmt=r"<b>Convolution formula.</b> If $X,Y$ are independent with densities $f_X,f_Y$, then $X+Y$ has density $f_{X+Y}(z)=(f_X*f_Y)(z)=\int_{-\infty}^\infty f_X(x)f_Y(z-x)\,dx=\int_{-\infty}^\infty f_X(z-y)f_Y(y)\,dy$. For independent integer-valued $X,Y$, $p_{X+Y}(z)=\sum_xp_X(x)p_Y(z-x)$ (Ross 6.3; Grimmett 4.8).",
  hint="Walk and wait are independent. How do you get the density of their total from the two densities?",
  bd=[r"<strong>$f_X(x)$ = the chance density of one leg being $x$.</strong> Say the walk takes $x$ minutes.",
      r"<strong>$f_Y(z-x)$ = then the other leg must take $z-x$.</strong> For the total to be $z$, the wait must make up the rest.",
      r"<strong>$\int\ldots dx$ = add over every split of $z$.</strong> Add up all the ways the total $z$ can be split into a walk $x$ and a wait $z-x$; independence lets the two densities multiply."],
  conn=r"<strong>Every way to make 25 minutes.</strong> A door-to-door time of 25 minutes can be 5 + 20, 10 + 15, 12.5 + 12.5, and so on. For each split you multiply the density of the walk and of the wait, then add up all splits.",
  cap="The density fX of one leg and the density fY of the other, flipped and slid so that it sits at z. The shaded overlap is the integral ∫fX(x)fY(z − x)dx, the density of the sum at z."),
30902: dict(d=d2, kind="THEOREM",
  stmt=r"<b>Change of variables in two dimensions.</b> Let $(X,Y)$ have density $f_{X,Y}$ and let $(U,V)=(u(X,Y),v(X,Y))$ be a differentiable one-to-one map with inverse $x(u,v),y(u,v)$ and non-vanishing Jacobian. Then $f_{U,V}(u,v)=f_{X,Y}\bigl(x(u,v),y(u,v)\bigr)\left|\det\dfrac{\partial(x,y)}{\partial(u,v)}\right|$ (Ross 6.7; Grimmett 4.7).",
  hint="If you swap (wait, ride) for new coordinates such as (total, ratio), how does the density change?",
  bd=[r"<strong>$f_{X,Y}(x(u,v),y(u,v))$ = the old density at the matching point.</strong> Find which $(x,y)$ maps to the new coordinates $(u,v)$, and read the old density there.",
      r"<strong>$\partial(x,y)/\partial(u,v)$ = how the box is stretched.</strong> It records how a small box in $(u,v)$ becomes a tilted box in $(x,y)$.",
      r"<strong>$|\det|$ = the area-stretch factor.</strong> The determinant is the area of the tilted box per unit area of the small box; the absolute value keeps densities positive."],
  conn=r"<strong>Changing the coordinates of the morning.</strong> You describe a morning by (wait, ride) or by (total time, share spent waiting). A small box of the second description covers a stretched, tilted box of the first, and the determinant says by how much.",
  cap="A small box du dv in (u,v) maps to a tilted box dx dy in (x,y). The area ratio is |det ∂(x,y)/∂(u,v)|, the factor that converts the density f(x,y) into f(u,v)."),
30903: dict(d=d3, kind="THEOREM",
  stmt=r"<b>Ratios and polar coordinates.</b> If $(X,Y)$ has density $f_{X,Y}$, then $Z=Y/X$ has density $f_Z(z)=\int_{-\infty}^\infty|x|\,f_{X,Y}(x,xz)\,dx$. In polar coordinates $X=R\cos\Theta$, $Y=R\sin\Theta$, the density of $(R,\Theta)$ is $f_{R,\Theta}(r,\theta)=r\,f_{X,Y}(r\cos\theta,r\sin\theta)$ for $r>0$ (Ross 6.7; Grimmett 4.7).",
  hint="How does a ratio of two random times, or a switch to polar coordinates, change the density of the pair?",
  bd=[r"<strong>$Z=Y/X$ = the slope of the ray to the point.</strong> Each value $z$ picks a line through the origin; the density of $Z$ adds up the joint density along that whole line.",
      r"<strong>$|x|$ = the line is stretched.</strong> Moving along the ray at larger $x$ spreads neighbouring slopes farther apart, so the weight grows like $|x|$.",
      r"<strong>$r\,f(r\cos\theta,r\sin\theta)$ = polar area element.</strong> A small piece of area is $r\,dr\,d\theta$: circles at larger radius have more room."],
  conn=r"<strong>Share of the trip versus size of the trip.</strong> The ratio of ride to wait only depends on the direction of the point in the (wait, ride) plane, not on how far from the origin it is. Direction and distance are the polar coordinates.",
  cap="A point (x, y) with ray slope z = y/x, radius r and angle θ. The ratio density adds f along the ray with weight |x|, and the polar density carries the extra factor r."),
30904: dict(d=d4, kind="THEOREM",
  stmt=r"<b>Box–Muller transform.</b> If $U_1,U_2$ are independent $\mathrm{Unif}(0,1)$, then $Z_1=\sqrt{-2\ln U_1}\cos(2\pi U_2)$ and $Z_2=\sqrt{-2\ln U_1}\sin(2\pi U_2)$ are independent $\mathcal N(0,1)$. Proof: $R^2=-2\ln U_1\sim\mathrm{Exp}(1/2)$ and $\Theta=2\pi U_2\sim\mathrm{Unif}(0,2\pi)$ are independent, and the Jacobian of the polar map gives the joint density $\frac1{2\pi}e^{-(z_1^2+z_2^2)/2}$ (Ross 6.7; Grimmett 4.11).",
  hint="How can two uniform random numbers produce two independent normal variables exactly?",
  bd=[r"<strong>$R=\sqrt{-2\ln U_1}$ = a random radius.</strong> The squared radius is exponential with rate $1/2$, which is the radial law of the two-dimensional standard normal.",
      r"<strong>$\Theta=2\pi U_2$ = a uniform angle.</strong> The standard normal pair has no preferred direction, so the angle is uniform on the circle.",
      r"<strong>$(R\cos\Theta,R\sin\Theta)$ = read off the point.</strong> The polar Jacobian $r$ turns this into the density $\frac1{2\pi}e^{-(z_1^2+z_2^2)/2}$: two independent standard normals."],
  conn=r"<strong>Simulating a noisy ride.</strong> A computer wants the usual wobble in the ride time. It draws two ordinary random numbers, treats one as a random distance and one as a random direction, and reads off two perfect bell-curve values.",
  cap="Two uniform numbers give a radius R = √(−2 ln U₁) and an angle 2πU₂. The point at that radius and angle has coordinates (Z₁, Z₂) = (R cos, R sin), two independent standard normals."),
30905: dict(d=d5, kind="THEOREM",
  stmt=r"<b>Closure under independent sums.</b> If $X_i\sim\mathcal N(\mu_i,\sigma_i^2)$ are independent, then $\sum_iX_i\sim\mathcal N\bigl(\sum\mu_i,\sum\sigma_i^2\bigr)$. If $X_i\sim\mathrm{Pois}(\lambda_i)$ are independent, then $\sum_iX_i\sim\mathrm{Pois}\bigl(\sum\lambda_i\bigr)$. If $X_i\sim\mathrm{Gamma}(\alpha_i,\beta)$ are independent (same rate), then $\sum_iX_i\sim\mathrm{Gamma}\bigl(\sum\alpha_i,\beta\bigr)$ (Ross 7.7; Grimmett 4.8, 5.1).",
  hint="Which families stay in the same family when you add independent members, and what happens to the parameters?",
  bd=[r"<strong>$\sum\mu_i,\ \sum\sigma_i^2$ = means add and variances add.</strong> The total of independent normal legs is normal, centred at the total mean, with the variances added (not the spreads).",
      r"<strong>$\mathrm{Pois}(\sum\lambda_i)$ = counts add, rates add.</strong> Independent Poisson counts, such as passengers from different doors, add to a Poisson count with the total rate.",
      r"<strong>Why:</strong> products of MGFs, $M_{X+Y}=M_XM_Y$, have the same form as each one, so the family is closed under adding independent members."],
  conn=r"<strong>Adding legs of the trip.</strong> A normal walk, a normal wait and a normal ride add up to a normal door-to-door time, with the means and the variances added. The family never changes, only its centre and width.",
  cap="Bell curves for the walk and the wait, and the wider bell of their total at the summed centre: 𝒩(μ₁,σ₁²) + 𝒩(μ₂,σ₂²) = 𝒩(μ₁+μ₂, σ₁²+σ₂²). Poisson counts add the same way."),
30906: dict(d=d6, kind="WORKED EXAMPLE",
  stmt=r"<b>Sum of two uniforms.</b> If $X,Y$ are independent $\mathrm{Unif}(0,1)$, the convolution gives $f_{X+Y}(z)=z$ for $0\le z\le1$, $f_{X+Y}(z)=2-z$ for $1<z\le2$, and $0$ otherwise (the triangular density). Hence $\mathbb E[X+Y]=1$ and $\operatorname{Var}(X+Y)=\tfrac1{12}+\tfrac1{12}=\tfrac16$ (Ross 6.3; Grimmett 4.8).",
  hint="Two independent flat delays add. What shape does the total take, and why does it peak in the middle?",
  bd=[r"<strong>$f(z)=z$ for $0\le z\le1$ = the overlap grows.</strong> At small totals $z$, the flat densities overlap on a stretch of length $z$, so the density rises linearly.",
      r"<strong>$f(z)=2-z$ for $1<z\le2$ = the overlap shrinks.</strong> Past the peak at $z=1$, the overlap shortens by the same amount, so the density falls linearly: a tent.",
      r"<strong>$\mathbb E=1$, $\operatorname{Var}=\tfrac16$ = means and variances add.</strong> Each flat leg has mean $\tfrac12$ and variance $\tfrac1{12}$, and independence adds them."],
  conn=r"<strong>Two delays, each equally likely anywhere.</strong> If each of two delays is equally likely to be anything between 0 and 1 minute, a total near 1 minute is the most likely, because there are the most ways to make it, and totals near 0 or 2 are rare.",
  cap="Two flat densities on [0,1] convolve into the tent f(z): rising as z on [0,1], falling as 2 − z on [1,2], with peak at z = 1, mean 1 and variance 1/6."),
}

STORY = {
30901: dict(s="STORY 9 · STEP 1 · ADDING LEGS", b="The density of a sum of independent legs is a <b>convolution</b>: add over every split of the total.", f=[["30705", "independence as factorising"], ["30703", "marginals"]], n=[["30902", "changing coordinates"], ["30905", "families closed under sums"]]),
30902: dict(s="STORY 9 · STEP 2 · NEW COORDINATES", b="Changing coordinates multiplies the density by the <b>area-stretch factor</b> |det|.", f=[["30402", "the one-dimensional stretch"], ["30702", "joint density"]], n=[["30903", "ratio and polar"], ["31301", "the Gaussian density"]]),
30903: dict(s="STORY 9 · STEP 3 · RATIOS AND POLAR", b="A ratio keeps only the <b>direction</b> of a point; polar coordinates add the factor r.", f=[["30902", "the Jacobian"]], n=[["30904", "Box–Muller"]]),
30904: dict(s="STORY 9 · STEP 4 · SIMULATING A NORMAL", b="A random radius and a uniform angle through the polar Jacobian give <b>exact normal samples</b>.", f=[["30903", "polar coordinates"], ["30404", "inverse-CDF sampling"]], n=[["32502", "Brownian increments are normal"]]),
30905: dict(s="STORY 9 · STEP 5 · FAMILIES THAT STAY", b="<b>Normal, Poisson and Gamma</b> stay in their family under independent sums: only the parameters add.", f=[["30901", "convolution"], ["30504", "MGF products"]], n=[["31302", "linear combinations of Gaussians"], ["32404", "merging Poisson streams"]]),
30906: dict(s="STORY 9 · STEP 6 · THE TENT", b="Two flat legs add into a <b>triangle</b>: a first look at how sums get bell-shaped.", f=[["30901", "convolution"]], n=[["31803", "the central limit theorem"]]),
}

FIX = build(CARDS)
