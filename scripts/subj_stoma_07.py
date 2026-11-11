"""StoMA topic 07 (joint, marginal, conditional). F1 picture: the pit-stop time X and the time lost in traffic Y as a pair; the laps of the first and second stop."""
from f1_lib import *

SUBJECT = "StoMA"

def plane(lab_x="pit stop x", lab_y="traffic y", x0=30, y0=108, x1=130, y1=16):
    return ax(x0, y0, x1, y1) + N(x1, y0 + 11, lab_x, 7, "end") + N(x0 - 2, y1 - 3, lab_y, 7, "start")

def d1(c):
    return svg(c, plane("x", "y", 30, 108, 150, 16),
        R(70, 40, 60, 44, "#d9dee7", 1), tick(70, 108, "a"), tick(130, 108, "b"), ytick(30, 84, "c"), ytick(30, 40, "d"),
        dash(70, 108, 70, 84), dash(130, 108, 130, 84), dash(30, 84, 70, 84), dash(30, 40, 70, 40),
        N(133, 36, "+F(b,d)", 7, "start"), N(133, 92, "−F(b,c)", 7, "start"), N(66, 36, "−F(a,d)", 7, "end"), N(66, 94, "+F(a,c)", 7, "end"),
        N(190, 40, "ℙ(a < X ≤ b,", 7.5, "start"), N(190, 51, "c < Y ≤ d)", 7.5, "start"), N(190, 66, "= four corners", 7, "start"), N(190, 77, "with signs + − − +", 7, "start"),
        N(110, 134, "F(x,y) = ℙ(X ≤ x, Y ≤ y)", 7.5, "middle"))

def d2(c):
    h = lambda x: 100 - 60 * math.exp(-((x - 170) ** 2) / 500)
    return svg(c, plane("x", "y", 20, 108, 120, 20),
        PG("42,84 96,84 104,50 56,46", "#d9dee7", 1), N(76, 72, "A", 9),
        N(70, 130, "region A of (stop, traffic) pairs", 7),
        ax(130, 108, 226, 20) + N(226, 118, "x", 7, "end") + N(136, 24, "f(x, y)", 7.5, "start"),
        fn(h, 130, 226, 40, 1.1), area(h, 150, 190, 108, 20),
        N(180, 130, "volume over A", 7), N(176, 12, "ℙ((X,Y) ∈ A) = ∬ f dx dy", 7))

def d3(c):
    return svg(c, plane("x", "y", 30, 82, 140, 12),
        E(84, 52, 42, 24, -20, "#f1f5f9", 1), R(70, 20, 14, 62, "none", 1, 0, "3 2"), N(77, 14, "slab at x", 7),
        arrow(77, 86, 77, 100, 1), 
        L(30, 124, 140, 124, 1), fn(lambda x: 124 - 18 * math.exp(-((x - 84) ** 2) / 700), 30, 140, 40, 1.1),
        N(150, 118, "fX(x) = ∫ f(x, y) dy", 7.5, "start"), N(150, 62, "add up each slab:", 7, "start"), N(150, 72, "the y direction collapses", 7, "start"),
        N(150, 42, "discrete: pX(x) = ∑ p(x, y)", 7, "start"))

def d4(c):
    return svg(c, plane("x", "y", 20, 108, 120, 14),
        E(70, 62, 36, 26, -25, "#f1f5f9", 1), L(70, 108, 70, 18, 1, "4 3"), N(70, 120, "x fixed", 7),
        ax(150, 108, 226, 26) + N(226, 118, "y", 7, "end"), N(154, 26, "f(y | x)", 7.5, "start"),
        fn(lambda y: 108 - 54 * math.exp(-((y - 190) ** 2) / 400), 150, 226, 40, 1.1), area(lambda y: 108 - 54 * math.exp(-((y - 190) ** 2) / 400), 160, 220, 108, 20),
        N(190, 8, "area = 1", 7), N(120, 134, "f(y | x) = f(x, y) / fX(x): slice, then divide by the slice's area", 6.5))

def d5(c):
    return svg(c, R(16, 28, 80, 70, "#f1f5f9", 1), N(56, 22, "rectangle support", 7), N(56, 112, "f = fX(x) fY(y) ✓", 7.5),
        N(21, 40, "y", 7, "start"), N(90, 94, "x", 7, "end"),
        PG("136,98 216,98 216,28", "#f1f5f9", 1), N(176, 22, "triangle 0 ≤ x ≤ y ≤ 1", 7), N(176, 112, "f = 4xy factorises, but ✗", 7.5),
        N(120, 134, "independent ⇔ factorises AND the support is a product set", 7))

def d6(c):
    return svg(c, ax(30, 108, 132, 16), N(132, 119, "x", 7, "end"), N(32, 14, "y", 7, "start"),
        PG("30,108 112,108 112,26", "#d9dee7", 1), N(88, 94, "f = 2", 8), N(40, 52, "y ≤ x", 7, "start"),
        L(150, 52, 226, 52, 1), L(150, 52, 226, 24, 1.1), N(188, 64, "fX(x) = 2x rises", 7),
        L(150, 112, 226, 112, 1), L(150, 80, 226, 112, 1.1), N(188, 124, "fY(y) = 2(1 − y) falls", 7),
        N(120, 140, "f(y | x) = 1/x on 0 ≤ y ≤ x: flat on the slice", 7))

CARDS = {
30701: dict(d=d1, kind="DEFINITION",
  stmt=r"<b>Joint CDF.</b> For random variables $X,Y$ on the same space, $F_{X,Y}(x,y)=\mathbb P(X\le x,\,Y\le y)$. It is non-decreasing in each variable, right-continuous, tends to $0$ as either argument $\to-\infty$ and to $1$ as both $\to\infty$, and for $a<b$, $c<d$: $\mathbb P(a<X\le b,\,c<Y\le d)=F_{X,Y}(b,d)-F_{X,Y}(a,d)-F_{X,Y}(b,c)+F_{X,Y}(a,c)\ge0$ (Ross 6.1; Grimmett 4.5).",
  hint='Pit stop and traffic together: how do you get the chance of a rectangle of (stop, traffic) pairs from the joint CDF alone?',
  bd=[r"<strong>$F_{X,Y}(x,y)=\mathbb P(X\le x,Y\le y)$ = both at most their limits.</strong> The chance that the stop takes at most $x$ seconds and the time lost in traffic is at most $y$ at once.",
      '<strong>$F(b,d)-F(a,d)-F(b,c)+F(a,c)$ = the rectangle by inclusion–exclusion.</strong> Take the big corner, remove the two strips beyond $a$ and $c$, and add back the doubly removed corner.',
      r"<strong>$\ge0$ = the rectangle rule is part of the definition.</strong> Being increasing in each variable is not enough; this four-corner combination must be non-negative."],
  conn="<strong>Stop and traffic on one plane.</strong> Each race is one point: how long Max's stop took and how much time he then lost in traffic. The CDF at a point says how much of the plane lies to its lower left; a rectangle of pairs needs four such corners.",
  cap='The (pit stop x, traffic y) plane. The shaded rectangle (a, b] × (c, d] has chance F(b,d) − F(a,d) − F(b,c) + F(a,c): the corner values with signs + − − +.'),
30702: dict(d=d2, kind="DEFINITION",
  stmt=r"<b>Joint density.</b> $X,Y$ are jointly continuous if there is $f_{X,Y}\ge0$ with $\mathbb P((X,Y)\in A)=\iint_Af_{X,Y}(x,y)\,dx\,dy$ for all (Borel) sets $A\subset\mathbb R^2$; then $f_{X,Y}(x,y)=\dfrac{\partial^2F_{X,Y}(x,y)}{\partial x\,\partial y}$ where it exists, and $\iint f_{X,Y}=1$ (Ross 6.1; Grimmett 4.5).",
  hint='How do you turn a region of (stop, traffic) pairs into a chance when both can be any real value?',
  bd=['<strong>$f_{X,Y}(x,y)$ = chance per unit area of the plane.</strong> A high spot means that combination of stop time and traffic loss is common.',
      r"<strong>$\iint_Af_{X,Y}\,dx\,dy$ = the volume above $A$.</strong> The chance of landing in a region is the volume under the surface over that region.",
      r"<strong>$\partial^2F/\partial x\,\partial y$ = recover the density.</strong> Differentiate the joint CDF once in each variable; the total volume is 1."],
  conn='<strong>A hill over the plane.</strong> Over the stop-and-traffic plane stands a hill whose height says how common each pair is. The chance of a set of pairs, such as “a quick stop but a lot of traffic”, is the volume of hill above that set.',
  cap='Left: a region A of (pit stop, traffic) pairs. Right: a slice of the density f(x,y) over A. The volume under f above A is ℙ((X,Y) ∈ A) = ∬f dx dy.'),
30703: dict(d=d3, kind="DEFINITION",
  stmt=r"<b>Marginal distributions.</b> If $(X,Y)$ has joint density $f_{X,Y}$, then $X$ has density $f_X(x)=\int_{-\infty}^\infty f_{X,Y}(x,y)\,dy$, and likewise $f_Y(y)=\int f_{X,Y}(x,y)\,dx$; in the discrete case $p_X(x)=\sum_yp_{X,Y}(x,y)$. If the support depends on $x$, the limits of the inner integral are those of the section at $x$ (Ross 6.1; Grimmett 3.6, 4.5).",
  hint='If you only care about the pit-stop time, how do you remove the traffic from the joint picture?',
  bd=['<strong>$f_{X,Y}(x,y)$ = the joint hill.</strong> The chance density of the pair (stop $x$, traffic $y$).',
      r"<strong>$\int f_{X,Y}(x,y)\,dy$ = add up the whole slab at $x$.</strong> Fix the stop time $x$ and sum over every possible traffic loss; the traffic direction collapses.",
      "<strong>$f_X(x)$ = the stop time's own density.</strong> For a triangular support the limits of $y$ depend on $x$; integrating over the whole line would be wrong."],
  conn='<strong>Forget the traffic.</strong> Of all races with a stop of exactly $x$ seconds, whatever happened in traffic, add up their chance. Doing this for every $x$ gives the curve of stop times alone, as if the traffic had never been timed.',
  cap='The joint blob of (pit stop x, traffic y). For each x the slab at x is added up over y, which collapses the y direction into the marginal curve fX(x) = ∫f(x,y)dy.'),
30704: dict(d=d4, kind="DEFINITION",
  stmt=r"<b>Conditional density.</b> If $f_X(x)>0$, the conditional density of $Y$ given $X=x$ is $f_{Y\mid X}(y\mid x)=\dfrac{f_{X,Y}(x,y)}{f_X(x)}$. For each such $x$, $f_{Y\mid X}(\cdot\mid x)$ is a density: $\int f_{Y\mid X}(y\mid x)\,dy=1$, and $f_{X,Y}(x,y)=f_X(x)f_{Y\mid X}(y\mid x)$ (Ross 6.5; Grimmett 4.6).",
  hint='You know the stop took exactly x seconds. How do you slice the joint hill to get the law of the time lost in traffic?',
  bd=['<strong>$f_{X,Y}(x,y)$ = the cut through the hill at $x$.</strong> Hold the stop time fixed and read the height along the traffic direction.',
      '<strong>$f_X(x)$ = the area of that cut.</strong> It is the marginal density of the stop time: the total weight of the slice.',
      r"<strong>$\int f_{Y\mid X}\,dy=1$ = renormalise.</strong> Dividing the slice by its area turns it into a proper density for the traffic loss, given this stop."],
  conn='<strong>Given a stop of exactly x seconds.</strong> Of the races with that stop, you ask how the time lost in traffic is spread. You slice the joint picture at that stop time and rescale the slice so that it has total chance 1.',
  cap='Slicing the joint blob at a fixed stop time x gives the curve f(y|x) on the right, with area 1: f(y|x) = f(x,y)/fX(x), the slice divided by its own area.'),
30705: dict(d=d5, kind="THEOREM",
  stmt=r"<b>Independence via densities.</b> Jointly continuous $X,Y$ are independent iff $f_{X,Y}(x,y)=f_X(x)f_Y(y)$ for all $(x,y)$. This forces the support of $(X,Y)$ to be a product set $S_X\times S_Y$; a density like $4xy$ on the triangle $0\le x\le y\le1$ factorises as a formula, but the coupled support makes $X,Y$ dependent (Ross 6.2; Grimmett 4.5).",
  hint='The formula for the density splits into an x part and a y part. Is that enough for independence?',
  bd=['<strong>$f_{X,Y}=f_Xf_Y$ = the joint is the product of the marginals.</strong> Knowing one leaves the law of the other unchanged.',
      r"<strong>$\forall(x,y)\in S_X\times S_Y$ = the support is a rectangle.</strong> Every value of one must be allowed with every value of the other, so the allowed region is a product set.",
      r"<strong>The coupled triangle fails.</strong> If $x\le y$ is required, a large $x$ rules out small $y$, so the two are tied even when the formula factorises."],
  conn='<strong>One stop says something about the other.</strong> If the lap of the first stop never changes which laps are possible for the second, they could be independent. But the second stop must come after the first: pitting late the first time rules out an early second stop, so the support is tied and they are not.',
  cap='Left: a rectangular support where f = fX(x)fY(y) holds. Right: a triangular support 0 ≤ x ≤ y ≤ 1 (first stop x before second stop y), where f = 4xy factorises but the coupled limits break independence.'),
30706: dict(d=d6, kind="WORKED EXAMPLE",
  stmt=r"<b>Uniform on a triangle.</b> Let $(X,Y)$ have density $f_{X,Y}=2$ on $T=\{0\le y\le x\le1\}$ and $0$ elsewhere. Then $f_X(x)=\int_0^x2\,dy=2x$ on $[0,1]$, $f_Y(y)=\int_y^12\,dx=2(1-y)$ on $[0,1]$, and $f_{Y\mid X}(y\mid x)=\dfrac2{2x}=\dfrac1x\mathbf 1_{\{0\le y\le x\}}$, a uniform law on $[0,x]$. Since $f_{X,Y}\ne f_Xf_Y$, $X,Y$ are dependent (Ross 6.1).",
  hint='Why do the marginals of a flat density on a triangle depend on x and y, and what is the law of y given x?',
  bd=[r"<strong>$f_X(x)=\int_0^x2\,dy=2x$ = the slab at $x$ has height $x$.</strong> Integrating $y$ only from $0$ to $x$ (the triangle's limits) gives a rising line, not a constant.",
      r"<strong>$f_Y(y)=2(1-y)$ = the slab at $y$ has length $1-y$.</strong> The marginal of $Y$ falls from $2$ to $0$.",
      r"<strong>$f_{Y\mid X}=1/x$ on $[0,x]$ = flat on the slice.</strong> Given $X=x$, $Y$ is uniform on $[0,x]$, and this depends on $x$, so they are dependent."],
  conn='<strong>The first stop comes before the second.</strong> Let Y be the first stop and X the second, as fractions of the race, with all such pairs equally likely in this toy model. Then late second stops are more common, and given the second stop, the first is uniform up to it.',
  cap='The triangle 0 ≤ y ≤ x ≤ 1 (first stop y before second stop x) with constant density 2. The marginal fX(x) = 2x rises along x, fY(y) = 2(1−y) falls along y, and the slice at x is flat with height 1/x.'),
}

STORY = {
30701: dict(s="STORY 7 · STEP 1 · TWO NUMBERS AT ONCE", b="Pit-stop time and traffic together live on a plane; the <b>joint CDF</b> gives the chance of a lower-left quadrant, and four corners give a rectangle.", f=[["30301", "the one-variable CDF"]], n=[["30702", "the joint density"]]),
30702: dict(s="STORY 7 · STEP 2 · THE HILL", b="Chances over the plane are <b>volumes under a density surface</b>.", f=[["30303", "area under a density"], ["30701", "the joint CDF"]], n=[["30703", "collapse a dimension"], ["30902", "change of variables in 2D"]]),
30703: dict(s="STORY 7 · STEP 3 · FORGET ONE", b="Adding up all values of one variable gives the <b>marginal</b> of the other.", f=[["30702", "the joint density"], ["30203", "total probability, in continuous form"]], n=[["30704", "fixing instead of forgetting"]]),
30704: dict(s="STORY 7 · STEP 4 · GIVEN THE OTHER", b="Slice the joint at a known value and renormalise: the <b>conditional density</b>.", f=[["30703", "the marginal as normaliser"], ["30201", "conditional probability"]], n=[["30705", "when slicing changes nothing"], ["31201", "conditional expectation"]]),
30705: dict(s="STORY 7 · STEP 5 · NO LINK", b="<b>Independent</b> means the joint factorises <b>and</b> the support is a product set.", f=[["30704", "slices all alike"], ["30205", "independent events"]], n=[["30706", "a worked dependent case"], ["30901", "sums of independent variables"]]),
30706: dict(s="STORY 7 · STEP 6 · A WORKED CASE", b="A flat density on a triangle shows marginals, slices and dependence in one picture.", f=[["30703", "marginals"], ["30705", "support test"]], n=[["31104", "error covariance for estimates"]]),
}

FIX = build(CARDS)
