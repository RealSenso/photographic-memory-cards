"""StoMA 3.07-3.13: the named distributions (Bernoulli, Binomial, Geometric, Negative Binomial, Poisson, Uniform, Gamma),
how they connect, and the Binomial -> Poisson limit. Added to topic 03 after the original six cards.
Run from the repo root:  python3 scripts/build_stoma_named_distributions.py
Writes the cards into cards_stoma.js and their story bands into story_stoma.js (both keep every other entry as is)."""
import math, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from stoma_cardkit import T, N, L, V, P, C, R, AX, box, ln, stmt, bars, binom, poi, curve, make, write_cards, write_story

TOPIC = 3


cards = []


def card(k, *args):
    cards.append(make(TOPIC, k, *args))


# ---------- 3.07 Bernoulli & Binomial ----------
n, p = 10, 0.6
bv = [binom(n, p, k) for k in range(n + 1)]
x0, base, step = 34, 112, 17.5
card(7, "CANONICAL DISCRETE", "Bernoulli & Binomial: Counting Wins in n Races",
     [AX(22, base, 228, 12),
      bars(bv, x0, base, step, 340),
      L(x0 + 6 * step, base, x0 + 6 * step, 16, 1, d="4 3"),
      N(x0 + 6 * step + 4, 20, "mean np = 6", 7, a="start"),
      T(26, 18, "ℙ(X = k)", 7.5, a="start"),
      T(228, 134, "k wins in n = 10 races, p = 0.6", 7, a="end"),
      N(28, 46, "each race: win (1)", 6.5, a="start"),
      N(28, 55, "with chance p, else 0", 6.5, a="start")],
     "Binomial(10, 0.6): the chance Max wins exactly k of 10 races when he wins each one with chance 0.6, independently. "
     "The bars peak near the mean np = 6.",
     ["<strong>Bernoulli(p):</strong> one trial, $X\\in\\{0,1\\}$ with $\\mathbb P(X=1)=p$; $\\mathbb E[X]=p$, $\\operatorname{Var}(X)=p(1-p)$.",
      "<strong>Binomial(n, p):</strong> successes in $n$ independent Bernoulli($p$) trials, $p_X(k)=\\binom nk p^k(1-p)^{n-k}$ for $k=0,\\dots,n$.",
      "<strong>Moments by adding:</strong> $X=\\sum_{i=1}^n X_i$, so $\\mathbb E[X]=np$ and $\\operatorname{Var}(X)=np(1-p)$; the MGF is $(1-p+pe^s)^n$."],
     "$$p_X(k)=\\binom nk p^k(1-p)^{n-k},\\qquad \\mathbb E[X]=np,\\qquad \\operatorname{Var}(X)=np(1-p)$$",
     "<strong>Wins in a season.</strong> Say Max wins each race with chance $p=0.6$, independently. Over a 24-race season his "
     "win count is Binomial(24, 0.6): about 14.4 wins on average, give or take $\\sqrt{24\\cdot0.6\\cdot0.4}\\approx2.4$.",
     "Using the Binomial when the trials are not independent or p changes from trial to trial. Drawing without replacement "
     "(e.g. picking 3 of the 10 teams) is Hypergeometric, not Binomial.",
     "DEFINITION",
     stmt("Bernoulli and Binomial distributions.",
          [ln("$X\\sim\\mathrm{Bernoulli}(p)$ takes the value 1 with chance $p$ and 0 with chance $1-p$."),
           ln("$X\\sim\\mathrm{Bin}(n,p)$ counts the successes in $n$ independent Bernoulli($p$) trials:"),
           ln("$p_X(k)=\\binom nk p^k(1-p)^{n-k}$ for $k=0,1,\\dots,n$.", True),
           ln("Writing $X=X_1+\\dots+X_n$ gives"),
           ln("$\\mathbb E[X]=np$ and $\\operatorname{Var}(X)=np(1-p)$.", True)],
          "Ross 4.6"),
     "Max wins each race with chance p, independently. What is the chance he wins exactly k of the n races?",
     ["<strong>$\\binom nk$ = which races he wins.</strong> The number of ways to pick the $k$ winning races out of $n$.",
      "<strong>$p^k(1-p)^{n-k}$ = one such season.</strong> $k$ wins and $n-k$ other results; the races are independent, so the chances multiply.",
      "<strong>$np$ and $np(1-p)$ = $n$ races added up.</strong> Each race adds mean $p$ and variance $p(1-p)$; independent variances add."])

# ---------- 3.08 Geometric & Negative Binomial ----------
p = 0.3
gv = [(1 - p) ** (k - 1) * p for k in range(1, 10)]
x0, base, step = 38, 112, 20
card(8, "CANONICAL DISCRETE", "Geometric & Negative Binomial: Races Until a Win",
     [AX(22, base, 228, 12),
      bars(gv, x0, base, step, 300, ks=list(range(1, 10))),
      L(x0 + (1 / p - 1) * step, base, x0 + (1 / p - 1) * step, 22, 1, d="4 3"),
      N(x0 + (1 / p - 1) * step + 4, 26, "mean 1/p ≈ 3.3", 7, a="start"),
      T(26, 18, "ℙ(N = k)", 7.5, a="start"),
      N(120, 52, "each bar = (1 − p) × the one before", 6.8, a="start"),
      N(120, 61, "ℙ(N = k) = (1 − p)ᵏ⁻¹ p", 6.8, a="start"),
      T(228, 134, "k = race of the first win, p = 0.3", 7, a="end")],
     "Geometric(0.3): the race N of Max's first win when he wins each race with chance 0.3. Every bar is 0.7 times the one before, "
     "so the chances shrink steadily and the mean is 1/p ≈ 3.3 races.",
     ["<strong>Geometric(p):</strong> the trial $N$ of the first success, $\\mathbb P(N=k)=(1-p)^{k-1}p$ for $k\\ge1$, with tail $\\mathbb P(N\\gt k)=(1-p)^k$.",
      "<strong>Moments and memory:</strong> $\\mathbb E[N]=1/p$, $\\operatorname{Var}(N)=(1-p)/p^2$, and $\\mathbb P(N\\gt m+k\\mid N\\gt m)=\\mathbb P(N\\gt k)$.",
      "<strong>Negative Binomial(r, p):</strong> the trial of the $r$-th success, a sum of $r$ independent Geometric($p$) waits; mean $r/p$, variance $r(1-p)/p^2$."],
     "$$\\mathbb P(N=k)=(1-p)^{k-1}p,\\qquad \\mathbb P(N_r=k)=\\binom{k-1}{r-1}p^r(1-p)^{k-r}$$",
     "<strong>The winless streak.</strong> In a slow car Max wins each race with chance 0.3. His first win comes on average in race "
     "$1/0.3\\approx3.3$, and after five races without a win the wait from there is still 3.3 races on average: the lost races buy "
     "nothing. Three wins take $3/0.3=10$ races on average.",
     "Two conventions: N = trials up to and including the first success (values 1, 2, …, mean 1/p) or failures before it "
     "(values 0, 1, …, mean (1 − p)/p). Check which one the question uses.",
     "DEFINITION",
     stmt("Geometric and Negative Binomial distributions.",
          [ln("In independent trials with success chance $p$, let $N$ be the trial of the first success. Then"),
           ln("$\\mathbb P(N=k)=(1-p)^{k-1}p$ for $k\\ge1$, $\\mathbb P(N\\gt k)=(1-p)^k$,", True),
           ln("$\\mathbb E[N]=1/p$, $\\operatorname{Var}(N)=(1-p)/p^2$, and $N$ is memoryless.", True),
           ln("The trial $N_r$ of the $r$-th success has"),
           ln("$\\mathbb P(N_r=k)=\\binom{k-1}{r-1}p^r(1-p)^{k-r}$ for $k\\ge r$, mean $r/p$.", True)],
          "Ross 4.8.1-4.8.2"),
     "Max wins each race with chance p. How many races until his first win, and until his r-th?",
     ["<strong>$(1-p)^{k-1}p$ = $k-1$ misses, then a win.</strong> The first win in race $k$ needs every earlier race lost.",
      "<strong>$\\mathbb P(N\\gt k)=(1-p)^k$ = no win yet.</strong> Adding these tails gives $\\mathbb E[N]=\\sum_{k\\ge0}(1-p)^k=1/p$, and the tail ratio gives no memory.",
      "<strong>Negative Binomial = $r$ waits in a row.</strong> The last race is the $r$-th win, so choose where the other $r-1$ wins fall among the first $k-1$ races."])

# ---------- 3.09 Poisson ----------
lam = 1.5
pv = [poi(lam, k) for k in range(7)]
x0, base, step = 40, 112, 26
card(9, "CANONICAL DISCRETE", "Poisson Distribution: Counting Rare Events",
     [AX(22, base, 228, 12),
      bars(pv, x0, base, step, 270),
      L(x0 + lam * step, base, x0 + lam * step, 16, 1, d="4 3"),
      N(x0 + lam * step + 4, 20, "mean = variance = λ = 1.5", 7, a="start"),
      T(26, 18, "ℙ(X = k)", 7.5, a="start"),
      N(x0 + 3.1 * step, 62, "ℙ(X = k) = e^(−λ) λᵏ / k!", 6.8, a="start"),
      N(x0 + 3.1 * step, 71, "ℙ(none) = e^(−1.5) ≈ 0.22", 6.8, a="start"),
      T(228, 134, "k safety cars in a race", 7, a="end")],
     "Poisson(1.5): the number of safety cars in a race when they come at random and average 1.5 per race. "
     "One is the most likely count, and none at all still has chance e^(−1.5) ≈ 0.22.",
     ["<strong>PMF:</strong> $p_X(k)=e^{-\\lambda}\\lambda^k/k!$ for $k=0,1,2,\\dots$; the $\\lambda^k/k!$ terms sum to $e^\\lambda$, so the chances add to 1.",
      "<strong>Mean = variance:</strong> $\\mathbb E[X]=\\operatorname{Var}(X)=\\lambda$; MGF $M_X(s)=e^{\\lambda(e^s-1)}$.",
      "<strong>Sums:</strong> independent $\\mathrm{Pois}(\\lambda)+\\mathrm{Pois}(\\mu)=\\mathrm{Pois}(\\lambda+\\mu)$, since the MGFs multiply."],
     "$$p_X(k)=e^{-\\lambda}\\frac{\\lambda^k}{k!},\\qquad \\mathbb E[X]=\\operatorname{Var}(X)=\\lambda,\\qquad M_X(s)=e^{\\lambda(e^s-1)}$$",
     "<strong>Safety cars in a race.</strong> Incidents are rare and random over the laps, about $\\lambda=1.5$ per race. Then "
     "$\\mathbb P(\\text{none})=e^{-1.5}\\approx0.22$ and $\\mathbb P(\\text{exactly one})=1.5e^{-1.5}\\approx0.33$. Over a 24-race "
     "season the total is Poisson(36).",
     "Using a λ for the wrong window: the rate per race times the number of races. And if the counts vary much more than their "
     "mean, Poisson is the wrong model (mean must equal variance).",
     "DEFINITION",
     stmt("Poisson distribution.",
          [ln("$X\\sim\\mathrm{Pois}(\\lambda)$, $\\lambda\\gt0$, has PMF"),
           ln("$p_X(k)=e^{-\\lambda}\\dfrac{\\lambda^k}{k!}$ for $k=0,1,2,\\dots$", True),
           ln("Then $\\mathbb E[X]=\\operatorname{Var}(X)=\\lambda$ and $M_X(s)=e^{\\lambda(e^s-1)}$."),
           ln("If $X\\sim\\mathrm{Pois}(\\lambda)$ and $Y\\sim\\mathrm{Pois}(\\mu)$ are independent,"),
           ln("then $X+Y\\sim\\mathrm{Pois}(\\lambda+\\mu)$.", True)],
          "Ross 4.7"),
     "A race has 1.5 safety cars on average, coming at random. What is the chance of none at all?",
     ["<strong>$e^{-\\lambda}\\lambda^k/k!$ = exactly $k$ events.</strong> $\\lambda$ is the average count; $e^{-\\lambda}$ is the chance of none.",
      "<strong>$\\mathbb E[X]=\\operatorname{Var}(X)=\\lambda$ = one number sets both.</strong> The mean and the spread are the same, a quick check on whether counts are Poisson.",
      "<strong>$\\mathrm{Pois}(\\lambda)+\\mathrm{Pois}(\\mu)=\\mathrm{Pois}(\\lambda+\\mu)$ = counts add.</strong> Safety cars in two races of 1.5 each: Poisson(3), because $e^{\\lambda(e^s-1)}e^{\\mu(e^s-1)}=e^{(\\lambda+\\mu)(e^s-1)}$."])

# ---------- 3.10 Uniform ----------
ax0, base = 30, 112
xa, xb = 60, 200          # a and b on screen
xc, xd = 60, 102          # shaded part: before minute 33 (3 of 10 minutes)
top = 52
card(10, "CANONICAL CONTINUOUS", "Uniform Distribution: Every Moment Equally Likely",
     [AX(22, base, 228, 12),
      R(xc, top, xd - xc, base - top, "#e2e8f0", 0.01),
      P(f"M {ax0} {base} L {xa} {base} M {xa} {top} L {xb} {top} M {xb} {base} L 222 {base}", w=1.8),
      L(xa, top, xa, base, 1, d="4 3"), L(xb, top, xb, base, 1, d="4 3"), L(xd, top, xd, base, 1),
      N(xa, base + 9, "a = 30", 6.8), N(xd, base + 9, "33", 6.8), N(xb, base + 9, "b = 40", 6.8),
      N(xa - 4, top + 3, "1/(b − a)", 6.8, a="end"),
      N((xc + xd) / 2, 86, "3/10", 7.5, w="bold"),
      N(150, top - 8, "flat: no moment preferred", 6.8),
      L((xa + xb) / 2, base, (xa + xb) / 2, top, 0.8, d="2 2"),
      N((xa + xb) / 2 + 3, top + 12, "mean 35", 6.8, a="start"),
      T(26, 18, "f(x)", 7.5, a="start"),
      T(228, 134, "x = minute of the pit stop", 7, a="end")],
     "Uniform(30, 40): the pit stop comes at a random minute between 30 and 40, so the density is flat at height 1/10. "
     "The chance of a stop before minute 33 is the shaded area, 3/10.",
     ["<strong>Density:</strong> $f_X(x)=\\dfrac1{b-a}$ on $[a,b]$ and 0 elsewhere; CDF $F_X(x)=\\dfrac{x-a}{b-a}$ for $a\\le x\\le b$.",
      "<strong>Chance = length ratio:</strong> $\\mathbb P(c\\le X\\le d)=\\dfrac{d-c}{b-a}$ for $a\\le c\\le d\\le b$.",
      "<strong>Moments:</strong> $\\mathbb E[X]=\\dfrac{a+b}2$, $\\operatorname{Var}(X)=\\dfrac{(b-a)^2}{12}$; if $U\\sim U(0,1)$ then $a+(b-a)U\\sim U(a,b)$."],
     "$$f_X(x)=\\frac1{b-a}\\mathbf 1_{[a,b]}(x),\\qquad \\mathbb E[X]=\\frac{a+b}2,\\qquad \\operatorname{Var}(X)=\\frac{(b-a)^2}{12}$$",
     "<strong>The pit window.</strong> Red Bull will pit Max at a random moment between minute 30 and minute 40, no moment "
     "preferred. $\\mathbb P(\\text{stop before minute 33})=3/10$. The expected stop is minute 35, give or take "
     "$10/\\sqrt{12}\\approx2.9$ minutes.",
     "The height 1/(b − a) is not a probability and can be bigger than 1: U(0, 0.5) has height 2. Only areas are chances, and "
     "any single moment has chance 0.",
     "DEFINITION",
     stmt("Uniform distribution.",
          [ln("$X\\sim U(a,b)$, $a\\lt b$, has density $f_X(x)=\\dfrac1{b-a}$ for $a\\le x\\le b$ and 0 otherwise."),
           ln("For $a\\le c\\le d\\le b$, $\\mathbb P(c\\le X\\le d)=\\dfrac{d-c}{b-a}$."),
           ln("Its mean and variance are"),
           ln("$\\mathbb E[X]=\\dfrac{a+b}2$ and $\\operatorname{Var}(X)=\\dfrac{(b-a)^2}{12}$.", True)],
          "Ross 5.3"),
     "The stop will come at a random minute between 30 and 40. What is the chance it comes before minute 33?",
     ["<strong>$1/(b-a)$ = a flat height.</strong> The total area must be 1, so a longer window means a lower height.",
      "<strong>$(d-c)/(b-a)$ = chance is the share of the window.</strong> 3 minutes out of 10 gives 3/10.",
      "<strong>$(a+b)/2$ and $(b-a)^2/12$ = middle and spread.</strong> The mean sits in the middle; the variance grows with the square of the window's length."])

# ---------- 3.11 Gamma ----------
ax0, base, sx, sy = 26, 112, 24, 88
g = [lambda t: math.exp(-t), lambda t: t * math.exp(-t), lambda t: t * t * math.exp(-t) / 2]
card(11, "CANONICAL CONTINUOUS", "Gamma Distribution: Waiting for the r-th Event",
     [AX(22, base, 228, 12),
      P(curve(g[0], 0, 8, ax0, base, sx, sy), w=1.4, dash="4 3"),
      P(curve(g[1], 0, 8, ax0, base, sx, sy), w=1.4),
      P(curve(g[2], 0, 8, ax0, base, sx, sy), w=2.2),
      N(ax0 + 8, base - sy + 6, "r = 1: exponential", 6.8, a="start"),
      N(ax0 + 1 * sx + 6, base - sy * g[1](1) - 4, "r = 2", 6.8, a="start"),
      N(ax0 + 2 * sx + 4, base - sy * g[2](2) - 5, "r = 3", 6.8, a="start", w="bold"),
      N(150, 58, "f(t) = λ^r t^(r−1) e^(−λt) / (r − 1)!", 6.8, a="start"),
      N(150, 67, "mean r/λ, variance r/λ²", 6.8, a="start"),
      N(150, 76, "peak at (r − 1)/λ", 6.8, a="start"),
      T(26, 18, "f(t)", 7.5, a="start"),
      T(228, 134, "t = hours until the r-th safety car, λ = 1", 7, a="end")],
     "Gamma(r, 1) densities for the wait until the r-th safety car. r = 1 is the exponential; for r = 2 and r = 3 the curve "
     "starts at 0 (several events cannot all come at once), rises to a peak at (r − 1)/λ and decays.",
     ["<strong>Sum of exponentials:</strong> if $X_1,\\dots,X_r$ are i.i.d. $\\mathrm{Exp}(\\lambda)$, then $T_r=X_1+\\dots+X_r$ has density $\\dfrac{\\lambda^r t^{r-1}e^{-\\lambda t}}{(r-1)!}$, $t\\ge0$.",
      "<strong>Moments:</strong> $\\mathbb E[T_r]=r/\\lambda$, $\\operatorname{Var}(T_r)=r/\\lambda^2$, MGF $\\left(\\dfrac{\\lambda}{\\lambda-s}\\right)^r$ for $s\\lt\\lambda$.",
      "<strong>General shape $\\alpha\\gt0$:</strong> $f(t)=\\lambda^\\alpha t^{\\alpha-1}e^{-\\lambda t}/\\Gamma(\\alpha)$; $\\mathrm{Gamma}(1,\\lambda)=\\mathrm{Exp}(\\lambda)$ and $\\mathrm{Gamma}(n/2,1/2)=\\chi^2_n$."],
     "$$f_{T_r}(t)=\\frac{\\lambda^r t^{r-1}e^{-\\lambda t}}{(r-1)!},\\qquad \\mathbb P(T_r\\gt t)=\\sum_{k=0}^{r-1}e^{-\\lambda t}\\frac{(\\lambda t)^k}{k!}$$",
     "<strong>The third safety car.</strong> If safety cars come at rate $\\lambda=1$ per hour of racing, the third arrives on "
     "average after 3 hours, longer than a race. $\\mathbb P(\\text{third within 2 hours})=\\mathbb P(\\text{at least 3 in 2 hours})"
     "=1-e^{-2}(1+2+2)\\approx0.32$.",
     "Two parametrisations: rate λ (mean α/λ) or scale θ = 1/λ (mean αθ). Check which one the question uses before quoting the "
     "mean, variance or MGF.",
     "THEOREM",
     stmt("Gamma distribution as a sum of exponentials.",
          [ln("If $X_1,\\dots,X_r$ are i.i.d. $\\mathrm{Exp}(\\lambda)$, then $T_r=X_1+\\dots+X_r\\sim\\mathrm{Gamma}(r,\\lambda)$:"),
           ln("$f_{T_r}(t)=\\dfrac{\\lambda^r t^{r-1}e^{-\\lambda t}}{(r-1)!}$ for $t\\ge0$,", True),
           ln("with $\\mathbb E[T_r]=r/\\lambda$ and $\\operatorname{Var}(T_r)=r/\\lambda^2$."),
           ln("For any $\\alpha\\gt0$, $\\mathrm{Gamma}(\\alpha,\\lambda)$ has density $\\lambda^\\alpha t^{\\alpha-1}e^{-\\lambda t}/\\Gamma(\\alpha)$.")],
          "Ross 5.6.1"),
     "Safety cars come at rate λ. How long until the third one?",
     ["<strong>$T_r=X_1+\\dots+X_r$ = $r$ waits in a row.</strong> Each gap is $\\mathrm{Exp}(\\lambda)$, so the mean $r/\\lambda$ and the variance $r/\\lambda^2$ simply add up.",
      "<strong>$t^{r-1}e^{-\\lambda t}$ = rise, then decay.</strong> For $r\\ge2$ the density starts at 0, because $r$ events need time; it peaks at $(r-1)/\\lambda$.",
      "<strong>$T_r\\gt t$ ⇔ fewer than $r$ events by time $t$.</strong> So the Gamma tail is a sum of Poisson($\\lambda t$) chances."])

# ---------- 3.12 The family map ----------
bw, bh = 58, 17
X1, X2, X3 = 4, 91, 178
Y1, Y2, Y3 = 8, 58, 108
F = "#f1f5f9"
card(12, "DISTRIBUTION MAP", "The Family Map: How the Named Distributions Connect",
     [box(X1, Y1, bw, bh, "Bernoulli", F, 8), box(X2, Y1, bw, bh, "Binomial", F, 8), box(X3, Y1, bw, bh, "Poisson", F, 8),
      box(X1, Y2, bw, bh, "Geometric", F, 8), box(X2, Y2, bw, bh, "Neg. Binomial", F, 8),
      box(X1, Y3, bw, bh, "Exponential", "#ffffff", 8), box(X2, Y3, bw, bh, "Gamma", "#ffffff", 8),
      box(X3, Y3, bw, bh, "Normal", "#ffffff", 8),
      V(X1 + bw, Y1 + bh / 2, X2 - 2, Y1 + bh / 2, 1.3), N((X1 + bw + X2) / 2, Y1 + bh / 2 - 3, "add n", 6.3),
      V(X2 + bw, Y1 + bh / 2, X3 - 2, Y1 + bh / 2, 1.3), N((X2 + bw + X3) / 2, Y1 + bh / 2 - 3, "n→∞", 6.3),
      N((X2 + bw + X3) / 2, Y1 + bh / 2 + 7, "np = λ", 6.3),
      V(X1 + bw, Y2 + bh / 2, X2 - 2, Y2 + bh / 2, 1.3), N((X1 + bw + X2) / 2, Y2 + bh / 2 - 3, "add r", 6.3),
      V(X1 + bw, Y3 + bh / 2, X2 - 2, Y3 + bh / 2, 1.3), N((X1 + bw + X2) / 2, Y3 + bh / 2 - 3, "add r", 6.3),
      V(X2 + bw, Y3 + bh / 2, X3 - 2, Y3 + bh / 2, 1.3), N((X2 + bw + X3) / 2, Y3 + bh / 2 - 3, "r large", 6.3),
      V(X1 + bw / 2, Y1 + bh, X1 + bw / 2, Y2 - 2, 1.3), N(X1 + bw / 2 + 3, (Y1 + bh + Y2) / 2 + 3, "first 1", 6.3, a="start"),
      V(X1 + bw / 2, Y2 + bh, X1 + bw / 2, Y3 - 2, 1.3), N(X1 + bw / 2 + 3, (Y2 + bh + Y3) / 2 - 1, "shrink", 6.3, a="start"),
      N(X1 + bw / 2 + 3, (Y2 + bh + Y3) / 2 + 7, "the laps", 6.3, a="start"),
      V(X2 + bw - 6, Y1 + bh, X3 + 10, Y3 - 2, 1.3), N(X2 + bw, Y1 + bh + 22, "CLT", 6.3, a="end"),
      P(f"M {X3 + bw / 2} {Y1 + bh} L {X3 + bw / 2} {Y2 + 10}", w=1.1, dash="3 2"),
      N(X3 + bw / 2, Y2 + 20, "gaps are", 6.3), N(X3 + bw / 2, Y2 + 28, "Exponential", 6.3)],
     "Counts on the top two rows, waiting times on the bottom. Adding copies moves right; the Binomial with many trials and a "
     "small chance becomes Poisson; shrinking each race to an instant turns the Geometric wait into the Exponential; big sums become Normal.",
     ["<strong>Adding copies:</strong> $n$ Bernoulli($p$) → Binomial($n,p$); $r$ Geometric($p$) → Negative Binomial($r,p$); $r$ Exp($\\lambda$) → Gamma($r,\\lambda$).",
      "<strong>Limits:</strong> Binomial($n,\\lambda/n$) → Poisson($\\lambda$); $h\\cdot$Geometric($\\lambda h$) → Exp($\\lambda$) as $h\\to0$; large sums → Normal (CLT).",
      "<strong>Other links:</strong> gaps between Poisson events are Exp($\\lambda$); $Z^2\\sim\\chi^2_1=\\mathrm{Gamma}(\\tfrac12,\\tfrac12)$; the $k$-th of $n$ Uniform(0,1) points is Beta($k,n-k+1$)."],
     "$$\\sum_{i=1}^n\\mathrm{Bern}(p)=\\mathrm{Bin}(n,p),\\quad \\mathrm{Bin}(n,\\tfrac\\lambda n)\\to\\mathrm{Pois}(\\lambda),\\quad \\sum_{i=1}^r\\mathrm{Exp}(\\lambda)=\\mathrm{Gamma}(r,\\lambda)$$",
     "<strong>One season, many questions.</strong> Win or not in one race: Bernoulli. Wins in the season: Binomial. Races until "
     "the first win: Geometric. Safety cars in a race: Poisson. Minutes until the first safety car: Exponential; until the third: "
     "Gamma. Points over many seasons: roughly Normal.",
     "The sum rules need independence and the same p or λ: Bin(n, p) + Bin(m, q) is not Binomial when p ≠ q, and "
     "Exp(λ) + Exp(μ) with λ ≠ μ is not Gamma.",
     "THEOREM",
     stmt("Relations between the named distributions.",
          [ln("Independent sums: $\\sum_{i=1}^n\\mathrm{Bern}(p)=\\mathrm{Bin}(n,p)$, $\\sum_{i=1}^r\\mathrm{Geom}(p)=\\mathrm{NegBin}(r,p)$,"),
           ln("$\\sum_{i=1}^r\\mathrm{Exp}(\\lambda)=\\mathrm{Gamma}(r,\\lambda)$, $\\mathrm{Pois}(\\lambda)+\\mathrm{Pois}(\\mu)=\\mathrm{Pois}(\\lambda+\\mu)$.", True),
           ln("Limits: $\\mathrm{Bin}(n,\\lambda/n)\\to\\mathrm{Pois}(\\lambda)$ and $h\\,\\mathrm{Geom}(\\lambda h)\\to\\mathrm{Exp}(\\lambda)$ in distribution;"),
           ln("standardised sums of i.i.d. finite-variance terms $\\to\\mathcal N(0,1)$.", True)],
          "Ross 4.7, 5.6, 6.3"),
     "Which distribution do you get by adding up many copies of another, or by letting the trials get small?",
     ["<strong>Top rows = counts.</strong> Add $n$ Bernoullis for a Binomial; add $r$ Geometric waits for a Negative Binomial.",
      "<strong>Bridges = limits.</strong> Many trials with a small chance each: Binomial → Poisson. Races shrunk to instants: Geometric → Exponential.",
      "<strong>Bottom row = waiting times.</strong> Add $r$ Exponentials for a Gamma; any big sum of independent pieces heads to the Normal."])

# ---------- 3.13 Worked benchmark: Binomial -> Poisson ----------
lam, laps = 1.5, 57
bvals = [binom(laps, lam / laps, k) for k in range(6)]
pvals = [poi(lam, k) for k in range(6)]
x0, base, step, sc = 40, 112, 32, 250
legend_y = 30
card(13, "WORKED BENCHMARK", "Worked Benchmark: Binomial → Poisson, the Law of Rare Events",
     [AX(22, base, 228, 12),
      bars(bvals, x0 - 5.5, base, step, sc, w=10, fill="#94a3b8", labels=False),
      bars(pvals, x0 + 5.5, base, step, sc, w=10, fill="#ffffff", labels=False),
      "".join(N(x0 + i * step, base + 9, str(i), 6.8) for i in range(6)),
      R(140, legend_y - 7, 8, 7, "#94a3b8", 1), N(152, legend_y - 1, f"Binomial(57, 1.5/57)", 6.6, a="start"),
      R(140, legend_y + 4, 8, 7, "#ffffff", 1), N(152, legend_y + 10, "Poisson(1.5)", 6.6, a="start"),
      N(140, legend_y + 26, f"ℙ(0): {bvals[0]:.3f} vs {pvals[0]:.3f}", 6.6, a="start"),
      N(140, legend_y + 35, f"ℙ(1): {bvals[1]:.3f} vs {pvals[1]:.3f}", 6.6, a="start"),
      T(26, 18, "ℙ(X = k)", 7.5, a="start"),
      T(228, 134, "k safety cars in a 57-lap race", 7, a="end")],
     f"Safety cars counted lap by lap: Binomial(57, 1.5/57) (grey) next to Poisson(1.5) (white). The bars almost match, because "
     f"there are many laps and a small chance on each.",
     ["<strong>Setup:</strong> $X_n\\sim\\mathrm{Bin}(n,p_n)$ with $np_n=\\lambda$ fixed, so $p_n=\\lambda/n\\to0$.",
      "<strong>Three limits:</strong> $\\dfrac{n(n-1)\\cdots(n-k+1)}{n^k}\\to1$, $\\left(1-\\dfrac\\lambda n\\right)^n\\to e^{-\\lambda}$, $\\left(1-\\dfrac\\lambda n\\right)^{-k}\\to1$.",
      "<strong>Result:</strong> $\\mathbb P(X_n=k)\\to e^{-\\lambda}\\lambda^k/k!$ for every fixed $k$; with 57 laps and $\\lambda=1.5$ the error is under 0.005."],
     "$$\\binom nk\\Big(\\frac\\lambda n\\Big)^k\\Big(1-\\frac\\lambda n\\Big)^{n-k}=\\frac{n(n-1)\\cdots(n-k+1)}{n^k}\\cdot\\frac{\\lambda^k}{k!}\\cdot\\Big(1-\\frac\\lambda n\\Big)^n\\Big(1-\\frac\\lambda n\\Big)^{-k}\\to e^{-\\lambda}\\frac{\\lambda^k}{k!}$$",
     f"<strong>57 laps, a few incidents.</strong> Each lap brings out a safety car with chance $p=1.5/57\\approx0.026$, "
     f"independently. Binomial(57, 0.026) gives $\\mathbb P(\\text{{none}})\\approx{bvals[0]:.3f}$; Poisson(1.5) gives "
     f"${pvals[0]:.3f}$. With many laps and a small chance on each, only the average $\\lambda=np$ matters.",
     "The limit needs np to stay fixed while p → 0. With p fixed and n large, use the Normal (CLT) instead: Binomial(100, 0.5) "
     "has variance 25, but Poisson(50) has variance 50.",
     "WORKED EXAMPLE",
     stmt("Poisson limit of the Binomial (law of rare events).",
          [ln("Let $X_n\\sim\\mathrm{Bin}(n,\\lambda/n)$. For each fixed $k$,"),
           ln("$\\mathbb P(X_n=k)=\\dfrac{n(n-1)\\cdots(n-k+1)}{n^k}\\cdot\\dfrac{\\lambda^k}{k!}\\cdot\\Big(1-\\dfrac\\lambda n\\Big)^{n}\\Big(1-\\dfrac\\lambda n\\Big)^{-k}$.", True),
           ln("As $n\\to\\infty$ the three outer factors tend to $1$, $e^{-\\lambda}$ and $1$, so"),
           ln("$\\mathbb P(X_n=k)\\to e^{-\\lambda}\\dfrac{\\lambda^k}{k!}$.", True)],
          "Ross 4.7"),
     "Each of 57 laps has a small chance of a safety car. Why does the count look Poisson?",
     ["<strong>$n(n-1)\\cdots(n-k+1)/n^k\\to1$ = choosing laps is easy.</strong> With $k$ fixed and $n$ huge, each factor is nearly $n$.",
      "<strong>$(1-\\lambda/n)^n\\to e^{-\\lambda}$ = the chance of no incident.</strong> Many laps, each with a tiny chance, give $e^{-\\lambda}$ for a clean race.",
      "<strong>$(1-\\lambda/n)^{-k}\\to1$ = what is left is Poisson.</strong> Only $e^{-\\lambda}\\lambda^k/k!$ remains, and it depends on $\\lambda=np$ alone."])

# ---------- story bands ----------
STORY = {
    "30307": ("STORY 3 · STEP 7 · WIN OR NOT", "Count the <b>wins in n independent races</b>: the Binomial, a sum of n Bernoulli coin flips.",
              [["30302", "a PMF for counts"]], [["30308", "waiting for the first win"], ["30313", "many races, small chance"]]),
    "30308": ("STORY 3 · STEP 8 · THE WINLESS STREAK", "Count the <b>races until the first win</b>: the Geometric, the counting version of a wait with no memory.",
              [["30307", "independent races"]], [["30304", "the continuous memoryless wait"], ["30312", "how the families connect"]]),
    "30309": ("STORY 3 · STEP 9 · RARE EVENTS", "Count <b>rare, random events</b> such as safety cars: the Poisson, where one number λ is both the mean and the variance.",
              [["30302", "a PMF for counts"]], [["30313", "where the Poisson comes from"], ["32401", "the Poisson process"]]),
    "30310": ("STORY 3 · STEP 10 · FLAT", "When <b>no moment is preferred</b>, the density is flat and a chance is just a share of the window.",
              [["30303", "a density"]], [["30404", "uniform to any law by the inverse CDF"], ["30804", "uniform order statistics"]]),
    "30311": ("STORY 3 · STEP 11 · THE r-TH WAIT", "Add r exponential waits to get the <b>Gamma</b>: the time until the r-th event.",
              [["30304", "one exponential wait"]], [["30309", "counts of the same events"], ["30901", "sums by convolution"]]),
    "30312": ("STORY 3 · STEP 12 · THE FAMILY MAP", "The named laws are one family: <b>add copies, take limits</b>, and you move from one to the next.",
              [["30307", "Binomial"], ["30311", "Gamma"]], [["30313", "Binomial → Poisson in detail"], ["31803", "the CLT"]]),
    "30313": ("STORY 3 · STEP 13 · RARE-EVENT LIMIT", "Many laps, each with a <b>small chance</b>: the Binomial count turns into a Poisson count with λ = np.",
              [["30307", "Binomial"], ["30309", "Poisson"]], [["30501", "the mean of any random variable"]]),
}


if __name__ == "__main__":
    write_cards(cards)
    write_story(STORY, add_links=[("30306", ["30307", "the named distributions"])])
