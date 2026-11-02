"""StoMA topic 22 (birth-death chains, MCMC). Commute picture: the number of people waiting at the stop; sampling mornings."""
from commute_lib import *

SUBJECT = "StoMA"

def nd(x, y, lab, r=10, fill="#ffffff"):
    return circ(x, y, r, fill, 1) + N(x, y + 3, lab, 7.5)

def ladder(y=50, labs=("0", "1", "2", "3", "…"), x0=30, dx=42):
    out = ""
    for i, l in enumerate(labs):
        out += nd(x0 + i * dx, y, l)
    for i in range(len(labs) - 1):
        out += arrow(x0 + i * dx + 11, y - 3, x0 + (i + 1) * dx - 11, y - 3, 1) + arrow(x0 + (i + 1) * dx - 11, y + 3, x0 + i * dx + 11, y + 3, 1)
    return out

def d1(c):
    return svg(c, ladder(), N(72, 35, "pᵢ", 7.5), N(72, 70, "qᵢ₊₁", 7.5) if False else N(72, 72, "qᵢ₊₁", 7.5), N(120, 14, "people waiting at the stop: i", 7.5),
        N(120, 100, "up one: pᵢ    down one: qᵢ", 7.5), N(120, 114, "cut between i and i+1: πᵢ pᵢ = πᵢ₊₁ qᵢ₊₁", 7.5), N(120, 128, "πᵢ₊₁ = (pᵢ / qᵢ₊₁) πᵢ", 8))

def d2(c):
    out = ax(24, 100, 226, 20) + N(226, 112, "n waiting", 7, "end") + N(28, 22, "πₙ", 7.5, "start")
    for i in range(9):
        h = 66 * 0.72 ** i
        out += R(34 + i * 20, 100 - h, 14, h, "#f1f5f9", 1)
    return svg(c, out, N(150, 30, "πₙ = π₀ ∏ pₖ / qₖ₊₁", 7.5, "start"), N(150, 42, "normalise: π₀ = (1 + ∑ₙ ∏ …)⁻¹", 7, "start"),
        N(120, 122, "a steady queue exists iff the sum is finite (ratios", 7), N(120, 134, "pₖ/qₖ₊₁ < 1 eventually: arrivals slower than service)", 7))

def d3(c):
    return svg(c, nd(60, 40, "a"), nd(180, 40, "b"), nd(120, 100, "c"), arrow(72, 40, 168, 40, 1), arrow(174, 50, 130, 91, 1), arrow(110, 92, 66, 50, 1),
        N(120, 32, "forward loop", 7), N(120, 14, "P(a,b) P(b,c) P(c,a)", 7.5), N(120, 124, "= P(a,c) P(c,b) P(b,a)  (reverse loop)", 7.5),
        N(120, 137, "πᵢPᵢⱼ = πⱼPⱼᵢ ⇔ every loop has equal chance both ways", 6.5))

def d4(c):
    out = ax(24, 108, 226, 20) + N(226, 120, "x", 7, "end")
    out += fn(lambda x: 108 - 70 * (0.7 * math.exp(-((x - 90) ** 2) / 500) + 0.3 * math.exp(-((x - 170) ** 2) / 300)), 28, 224, 70, 1.2)
    out += C(90, 108 - 70 * .7, 2.6) + C(170, 108 - 70 * .3, 2.6, "#ffffff", 1.1) + arrow(94, 54, 166, 82, 1)
    return svg(c, out, N(80, 38, "x now", 7), N(176, 70, "y proposed", 7, "start"), N(120, 12, "accept with α(x,y) = min(1, π̃(y)q(x|y) / π̃(x)q(y|x))", 7),
        N(120, 128, "balance: π(x)q(y|x)α(x,y) = π(y)q(x|y)α(y,x)", 7), N(120, 140, "so π is stationary; needs π only up to a constant", 7))

def d5(c):
    out = ax(24, 90, 226, 20) + N(226, 102, "x", 7, "end")
    out += fn(lambda x: 90 - 58 * math.exp(-((x - 124) ** 2) / 900), 28, 224, 60, 1.2)
    out += L(100, 90, 118, 90, 1) + N(109, 82, "tiny", 6.5) + L(160, 90, 206, 90, 1) + N(183, 82, "huge", 6.5)
    return svg(c, out, N(120, 12, "α(x,y) = min(1, π(y)/π(x)) for a symmetric proposal", 7.5),
        N(60, 116, "tiny steps: accepted often,", 6.8), N(60, 126, "but you barely move", 6.8), N(180, 116, "huge steps: you move,", 6.8), N(180, 126, "but are mostly rejected", 6.8),
        N(120, 140, "optimal acceptance ≈ 23.4% in high dimension", 7.5))

def d6(c):
    out = ax(24, 108, 226, 20)
    out += poly([(60, 100), (60, 72), (112, 72), (112, 50), (164, 50), (164, 34)], 1.1) + C(60, 100, 2.4) + C(164, 34, 2.4, "#ffffff", 1.1)
    return svg(c, out, N(60, 116, "x₁", 7), N(28, 18, "x₂", 7, "start"), N(224, 100, "one coordinate at a time", 6.8, "end"),
        N(120, 130, "draw Xᵢ ~ p(Xᵢ | X₋ᵢ): always accepted, α ≡ 1", 7.5), N(120, 142, "(the path moves along the axes)", 7))

CARDS = {
32201: dict(d=d1, kind="THEOREM",
  stmt=r"<b>Birth–death chains.</b> A chain on $\{0,1,2,\ldots\}$ moves only $i\to i\pm1$, with $P_{i,i+1}=p_i$ and $P_{i,i-1}=q_i$. A stationary $\pi$ satisfies the detailed balance (cut) equations $\pi_ip_i=\pi_{i+1}q_{i+1}$, so $\pi_{i+1}=\frac{p_i}{q_{i+1}}\pi_i$ for all $i\ge0$ (Ross 4.8; Grimmett 6.5).",
  hint="If the queue only grows or shrinks by one, how do the steady shares of neighbouring queue lengths compare?",
  bd=[r"<strong>$P_{i,i+1}=p_i,\ P_{i,i-1}=q_i$ = one step up or down.</strong> One person arrives or one leaves; nothing jumps further.",
      r"<strong>$\pi_ip_i=\pi_{i+1}q_{i+1}$ = balance across a cut.</strong> The flow from $i$ up to $i+1$ equals the flow from $i+1$ back down.",
      r"<strong>$\pi_{i+1}=\frac{p_i}{q_{i+1}}\pi_i$ = a recursion.</strong> Each share is the previous share times (up chance over down chance)."],
  conn=r"<strong>A queue at the stop.</strong> If the chance of one more person arriving is larger than the chance one leaves, longer queues stay likely; the ratio of neighbouring shares is exactly that up/down ratio.",
  cap="The number waiting at the stop as a ladder 0, 1, 2, …. Steady flow up across each rung equals flow down: πᵢpᵢ = πᵢ₊₁qᵢ₊₁."),
32202: dict(d=d2, kind="THEOREM",
  stmt=r"<b>Birth–death invariant law.</b> Solving the recursion, $\pi_n=\pi_0\prod_{k=0}^{n-1}\frac{p_k}{q_{k+1}}$ and $\pi_0=\Bigl(1+\sum_{n\ge1}\prod_{k=0}^{n-1}\frac{p_k}{q_{k+1}}\Bigr)^{-1}$. An irreducible birth–death chain is positive recurrent iff this sum is finite (Ross 4.8; Grimmett 6.5).",
  hint="For which queues does a steady length distribution exist, and what does it look like?",
  bd=[r"<strong>$\pi_n=\pi_0\prod_{k<n}\frac{p_k}{q_{k+1}}$ = multiply the ratios.</strong> Each step up multiplies the weight by up-over-down.",
      r"<strong>$\pi_0=\bigl(1+\sum_n\prod\bigr)^{-1}$ = normalise.</strong> The weights must add to one, which fixes the constant.",
      r"<strong>The sum must be finite.</strong> If the ratios stay at or above 1, the sum diverges: no steady law, and the queue is not positive recurrent."],
  conn=r"<strong>Does the queue settle?</strong> If buses clear the stop faster than people arrive, the share of mornings with a long queue falls geometrically. If people arrive faster, the queue just keeps growing.",
  cap="Steady shares πₙ of n waiting, decaying geometrically when service beats arrivals (ratio < 1). They normalise only if ∑ ∏ pₖ/qₖ₊₁ is finite."),
32203: dict(d=d3, kind="THEOREM",
  stmt=r"<b>Reversibility and Kolmogorov's criterion.</b> An irreducible stationary chain is reversible, $\pi_iP_{ij}=\pi_jP_{ji}$, if and only if for every cycle $P_{i_0i_1}P_{i_1i_2}\cdots P_{i_ki_0}=P_{i_0i_k}\cdots P_{i_2i_1}P_{i_1i_0}$: each loop has the same probability in both directions (Grimmett 6.5; Kelly, Reversibility).",
  hint="How can you tell, from the one-step chances alone, that the chain looks the same run backwards?",
  bd=[r"<strong>$\pi_iP_{ij}=\pi_jP_{ji}$ = reversible.</strong> In steady state, the film run backwards has the same law as the film run forwards.",
      r"<strong>$P_{i_0i_1}\cdots P_{i_ki_0}$ = chance of a loop forwards.</strong> Multiply the one-step chances around a closed cycle of states.",
      r"<strong>$=P_{i_0i_k}\cdots P_{i_1i_0}$ = same loop backwards.</strong> Reversibility holds exactly when this equality holds for every cycle, with no need to know $\pi$."],
  conn=r"<strong>Does the film make sense in reverse?</strong> If going round a loop of commute states has the same chance in either direction, a recording of long-run mornings played backwards is statistically identical.",
  cap="A cycle a → b → c → a and its reverse. The chain is reversible iff the products of the one-step chances around every such loop agree in both directions."),
32204: dict(d=d4, kind="THEOREM",
  stmt=r"<b>Metropolis–Hastings.</b> To sample from $\pi\propto\tilde\pi$, propose $y\sim q(\cdot\mid x)$ and accept with $\alpha(x,y)=\min\bigl(1,\frac{\tilde\pi(y)q(x\mid y)}{\tilde\pi(x)q(y\mid x)}\bigr)$. Then $\pi(x)q(y\mid x)\alpha(x,y)=\pi(y)q(x\mid y)\alpha(y,x)$, so detailed balance holds and $\pi$ is stationary (Robert & Casella 7.3; Grimmett 6.14).",
  hint="How do you sample typical mornings from a law you can only compute up to a constant?",
  bd=[r"<strong>$y\sim q(\cdot\mid x)$ = propose a move.</strong> From the current state $x$, suggest a candidate $y$.",
      r"<strong>$\alpha=\min\bigl(1,\frac{\tilde\pi(y)q(x\mid y)}{\tilde\pi(x)q(y\mid x)}\bigr)$ = accept or stay.</strong> Moves to likelier states are always accepted; to less likely ones, with the ratio of weights.",
      r"<strong>Detailed balance holds.</strong> The constant cancels in the ratio, so $\pi$ is stationary and the chain's time averages estimate expectations under $\pi$."],
  conn=r"<strong>Wander towards the likely mornings.</strong> Propose a different morning; if it is more typical, move there; if less typical, move only sometimes. The path then visits mornings in proportion to how typical they are.",
  cap="A two-bump target. From x propose y; accept with probability α = min(1, ratio of weights). The accepted moves satisfy detailed balance, so π is stationary."),
32205: dict(d=d5, kind="WORKED EXAMPLE",
  stmt=r"<b>Random-walk Metropolis.</b> With a symmetric proposal, $q(y\mid x)=q(x\mid y)$, the acceptance is $\alpha(x,y)=\min\bigl(1,\frac{\pi(y)}{\pi(x)}\bigr)$. The step size trades off acceptance against movement; for Gaussian-like targets in high dimension the optimal acceptance rate is about $23.4\%$ (Roberts–Gelman–Gilks).",
  hint="How big should a proposed step be: small and safe, or large and risky?",
  bd=[r"<strong>$q(y\mid x)=q(x\mid y)$ = symmetric proposal.</strong> A step of a given size forwards is as likely as backwards, so the $q$ factors cancel.",
      r"<strong>$\alpha=\min(1,\pi(y)/\pi(x))$ = compare weights only.</strong> Always go uphill; go downhill with the ratio of heights.",
      r"<strong>$\approx23.4\%$ = the optimal acceptance.</strong> Tiny steps are accepted but barely move; huge steps move but are rejected; the best compromise accepts about one in four."],
  conn=r"<strong>Choosing the step.</strong> Trying a tiny change to your departure time is almost always accepted but explores slowly. A wild change is almost always rejected. A medium change explores best.",
  cap="The target and two step sizes: tiny steps are accepted but crawl, huge steps are rejected. The best compromise accepts about 23.4% of proposals."),
32206: dict(d=d6, kind="THEOREM",
  stmt=r"<b>Gibbs sampling.</b> To sample $p(x_1,\ldots,x_d)$, update one coordinate at a time from its full conditional: $X_i^{(t+1)}\sim p(X_i\mid X_{-i}^{(t)})$. This is Metropolis–Hastings with proposal $q(y\mid x)=p(y_i\mid x_{-i})$, for which the acceptance probability is $\alpha(x,y)\equiv1$, so every proposal is accepted (Robert & Casella 10; Grimmett 6.14).",
  hint="Can you sample a joint law by redrawing one variable at a time, never rejecting?",
  bd=[r"<strong>$X_i\sim p(X_i\mid X_{-i})$ = redraw one coordinate.</strong> Hold all the others fixed and resample from the exact conditional law.",
      r"<strong>$\alpha(x,y)=\min\bigl(1,\frac{p(y)p(x_i\mid x_{-i})}{p(x)p(y_i\mid x_{-i})}\bigr)$ = the MH ratio.</strong> Since $y_{-i}=x_{-i}$ and $p(y)=p(y_i\mid x_{-i})p(x_{-i})$, the ratio equals 1.",
      r"<strong>$\alpha\equiv1$ = never rejected.</strong> Each update is a valid move of a chain with stationary law $p$."],
  conn=r"<strong>Fix one, redraw the other.</strong> Given the wait time, redraw the ride time from its conditional law; then given the ride time, redraw the wait. Alternating the two samples the pair jointly, with nothing thrown away.",
  cap="A Gibbs path moves along the axes: update x₁ given x₂, then x₂ given x₁. Each update is a draw from a full conditional and is always accepted (α ≡ 1)."),
}

STORY = {
32201: dict(s="STORY 22 · STEP 1 · A LADDER OF QUEUE LENGTHS", b="In a <b>birth–death chain</b> the flow up each rung balances the flow down.", f=[["32004", "cut equations"], ["32001", "stationary law"]], n=[["32202", "the steady queue"]]),
32202: dict(s="STORY 22 · STEP 2 · DOES THE QUEUE SETTLE", b="The steady law is a <b>product of up/down ratios</b>, and exists iff their sum is finite.", f=[["32201", "balance recursion"]], n=[["32203", "reversibility"], ["32705", "continuous-time queues"]]),
32203: dict(s="STORY 22 · STEP 3 · THE FILM RUN BACKWARDS", b="<b>Kolmogorov's criterion</b>: reversible iff every loop has equal chance both ways.", f=[["32004", "detailed balance"]], n=[["32204", "building reversible samplers"]]),
32204: dict(s="STORY 22 · STEP 4 · SAMPLING BY A CHAIN", b="<b>Metropolis–Hastings</b> accepts moves so that detailed balance holds for the target.", f=[["32203", "reversibility"], ["32002", "convergence to π"]], n=[["32205", "tuning"], ["32206", "never rejecting"]]),
32205: dict(s="STORY 22 · STEP 5 · THE STEP SIZE", b="<b>Random-walk Metropolis</b> trades acceptance against movement; aim near 23.4%.", f=[["32204", "MH"]], n=[["32206", "Gibbs"]]),
32206: dict(s="STORY 22 · STEP 6 · ONE COORDINATE AT A TIME", b="<b>Gibbs sampling</b> redraws from full conditionals; every move is accepted.", f=[["32204", "MH with α ≡ 1"], ["30704", "conditional laws"]], n=[["32301", "stationary random signals"]]),
}

FIX = build(CARDS)
