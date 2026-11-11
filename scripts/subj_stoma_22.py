"""StoMA topic 22 (birth-death chains, MCMC). F1 picture: Max's place in the championship standings, counted as places behind the leader, moves up or down one at a time; Red Bull's set-up engineers propose small set-up changes and accept them by the Metropolis rule; Gibbs tunes the front and rear wing one at a time."""
from f1_lib import *

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
    return svg(c, ladder(), N(72, 35, "pᵢ", 7.5), N(72, 70, "qᵢ₊₁", 7.5) if False else N(72, 72, "qᵢ₊₁", 7.5), N(120, 14, "places behind the leader: i", 7.5),
        N(120, 100, "drop a place: pᵢ    gain a place: qᵢ", 7.5), N(120, 114, "cut between i and i+1: πᵢ pᵢ = πᵢ₊₁ qᵢ₊₁", 7.5), N(120, 128, "πᵢ₊₁ = (pᵢ / qᵢ₊₁) πᵢ", 8))

def d2(c):
    out = ax(24, 100, 226, 20) + N(226, 112, "n places back", 7, "end") + N(28, 22, "πₙ", 7.5, "start")
    for i in range(9):
        h = 66 * 0.72 ** i
        out += R(34 + i * 20, 100 - h, 14, h, "#f1f5f9", 1)
    return svg(c, out, N(150, 30, "πₙ = π₀ ∏ pₖ / qₖ₊₁", 7.5, "start"), N(150, 42, "normalise: π₀ = (1 + ∑ₙ ∏ …)⁻¹", 7, "start"),
        N(120, 122, "a steady law exists iff the sum is finite (ratios", 7), N(120, 134, "pₖ/qₖ₊₁ < 1 eventually: places gained beat places lost)", 7))

def d3(c):
    return svg(c, nd(60, 40, "a"), nd(180, 40, "b"), nd(120, 100, "c"), arrow(72, 40, 168, 40, 1), arrow(174, 50, 130, 91, 1), arrow(110, 92, 66, 50, 1),
        N(120, 32, "forward loop", 7), N(120, 14, "P(a,b) P(b,c) P(c,a)", 7.5), N(120, 124, "= P(a,c) P(c,b) P(b,a)  (reverse loop)", 7.5),
        N(120, 137, "πᵢPᵢⱼ = πⱼPⱼᵢ ⇔ every loop has equal chance both ways", 6.5))

def d4(c):
    out = ax(24, 108, 226, 20) + N(226, 120, "x", 7, "end")
    out += fn(lambda x: 108 - 70 * (0.7 * math.exp(-((x - 90) ** 2) / 500) + 0.3 * math.exp(-((x - 170) ** 2) / 300)), 28, 224, 70, 1.2)
    out += C(90, 108 - 70 * .7, 2.6) + C(170, 108 - 70 * .3, 2.6, "#ffffff", 1.1) + arrow(94, 54, 166, 82, 1)
    return svg(c, out, N(80, 38, "set-up x now", 7), N(176, 70, "y proposed", 7, "start"), N(120, 12, "accept with α(x,y) = min(1, π̃(y)q(x|y) / π̃(x)q(y|x))", 7),
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
    return svg(c, out, N(60, 116, "x₁ front wing", 7), N(28, 18, "x₂ rear wing", 7, "start"), N(224, 100, "one coordinate at a time", 6.8, "end"),
        N(120, 130, "draw Xᵢ ~ p(Xᵢ | X₋ᵢ): always accepted, α ≡ 1", 7.5), N(120, 142, "(the path moves along the axes)", 7))

CARDS = {
32201: dict(d=d1, kind="THEOREM",
  stmt=r"<b>Birth–death chains.</b> A chain on $\{0,1,2,\ldots\}$ moves only $i\to i\pm1$, with $P_{i,i+1}=p_i$ and $P_{i,i-1}=q_i$. A stationary $\pi$ satisfies the detailed balance (cut) equations $\pi_ip_i=\pi_{i+1}q_{i+1}$, so $\pi_{i+1}=\frac{p_i}{q_{i+1}}\pi_i$ for all $i\ge0$ (Ross 4.8; Grimmett 6.5).",
  hint="If Max's championship place only moves one at a time, how do the steady shares of neighbouring places compare?",
  bd=[r"<strong>$P_{i,i+1}=p_i,\ P_{i,i-1}=q_i$ = one step up or down.</strong> After a race he drops one place or gains one; nothing jumps further.",
      r"<strong>$\pi_ip_i=\pi_{i+1}q_{i+1}$ = balance across a cut.</strong> The flow from $i$ back to $i+1$ equals the flow from $i+1$ forward to $i$.",
      r"<strong>$\pi_{i+1}=\frac{p_i}{q_{i+1}}\pi_i$ = a recursion.</strong> Each share is the one before times (chance to drop over chance to gain)."],
  conn='<strong>A ladder of championship places.</strong> Count how many places Max is behind the leader: 0 means he leads. If gaining a place is likelier than dropping one, being far back is rare; the ratio of neighbouring shares is exactly the drop/gain ratio.',
  cap='Places behind the leader as a ladder 0, 1, 2, …. In steady state the flow back across each rung equals the flow forward: πᵢpᵢ = πᵢ₊₁qᵢ₊₁.'),
32202: dict(d=d2, kind="THEOREM",
  stmt=r"<b>Birth–death invariant law.</b> Solving the recursion, $\pi_n=\pi_0\prod_{k=0}^{n-1}\frac{p_k}{q_{k+1}}$ and $\pi_0=\Bigl(1+\sum_{n\ge1}\prod_{k=0}^{n-1}\frac{p_k}{q_{k+1}}\Bigr)^{-1}$. An irreducible birth–death chain is positive recurrent iff this sum is finite (Ross 4.8; Grimmett 6.5).",
  hint="When does Max's championship place have a steady law, and what does it look like?",
  bd=[r"<strong>$\pi_n=\pi_0\prod_{k<n}\frac{p_k}{q_{k+1}}$ = multiply the ratios.</strong> Each rung further back multiplies the weight by drop-over-gain.",
      r"<strong>$\pi_0=\bigl(1+\sum_n\prod\bigr)^{-1}$ = normalise.</strong> The weights must add to one, which fixes the constant.",
      '<strong>The sum must be finite.</strong> If the ratios stay at or above 1, the sum diverges: no steady law, and the chain is not positive recurrent.'],
  conn='<strong>Does he stay near the top?</strong> If Max gains places more easily than he loses them, the share of time spent $n$ places back falls off geometrically, and he is mostly leading. If he loses places more easily, he just keeps sliding back and there is no steady law.',
  cap='Steady shares πₙ of being n places behind the leader, falling geometrically when gaining beats dropping (ratio < 1). They add to one only if ∑ ∏ pₖ/qₖ₊₁ is finite.'),
32203: dict(d=d3, kind="THEOREM",
  stmt=r"<b>Reversibility and Kolmogorov's criterion.</b> An irreducible stationary chain is reversible, $\pi_iP_{ij}=\pi_jP_{ji}$, if and only if for every cycle $P_{i_0i_1}P_{i_1i_2}\cdots P_{i_ki_0}=P_{i_0i_k}\cdots P_{i_2i_1}P_{i_1i_0}$: each loop has the same probability in both directions (Grimmett 6.5; Kelly, Reversibility).",
  hint='How can you tell, from the one-step chances alone, that the chain looks the same run backwards?',
  bd=[r"<strong>$\pi_iP_{ij}=\pi_jP_{ji}$ = reversible.</strong> In steady state, the film run backwards has the same law as the film run forwards.",
      r"<strong>$P_{i_0i_1}\cdots P_{i_ki_0}$ = chance of a loop forwards.</strong> Multiply the one-step chances around a closed cycle of states.",
      r"<strong>$=P_{i_0i_k}\cdots P_{i_1i_0}$ = same loop backwards.</strong> Reversibility holds exactly when this equality holds for every cycle, with no need to know $\pi$."],
  conn="<strong>Does the season make sense in reverse?</strong> Take three results, win, podium and off the podium. If going round the loop win → podium → off → win has the same chance as going round the other way, then a highlight reel of Max's long-run results played backwards looks just as believable.",
  cap='A cycle a → b → c → a and its reverse. The chain is reversible iff the products of the one-step chances around every such loop agree in both directions.'),
32204: dict(d=d4, kind="THEOREM",
  stmt=r"<b>Metropolis–Hastings.</b> To sample from $\pi\propto\tilde\pi$, propose $y\sim q(\cdot\mid x)$ and accept with $\alpha(x,y)=\min\bigl(1,\frac{\tilde\pi(y)q(x\mid y)}{\tilde\pi(x)q(y\mid x)}\bigr)$. Then $\pi(x)q(y\mid x)\alpha(x,y)=\pi(y)q(x\mid y)\alpha(y,x)$, so detailed balance holds and $\pi$ is stationary (Robert & Casella 7.3; Grimmett 6.14).",
  hint='How do the engineers sample good car set-ups from a law they can only compute up to a constant?',
  bd=[r"<strong>$y\sim q(\cdot\mid x)$ = propose a move.</strong> From the current set-up $x$, suggest a candidate $y$.",
      r"<strong>$\alpha=\min\bigl(1,\frac{\tilde\pi(y)q(x\mid y)}{\tilde\pi(x)q(y\mid x)}\bigr)$ = accept or stay.</strong> Moves to likelier states are always accepted; to less likely ones, with the ratio of weights.",
      r"<strong>Detailed balance holds.</strong> The constant cancels in the ratio, so $\pi$ is stationary and the chain's time averages estimate expectations under $\pi$."],
  conn="<strong>Red Bull's set-up engineers.</strong> They propose a small change to the set-up. If the simulator says it is better, they take it; if worse, they take it only sometimes, with the ratio of scores. Over a long session they visit set-ups in proportion to how good they are, and never need the total of all scores.",
  cap='A two-bump target over set-ups. From set-up x propose y; accept with chance α = min(1, ratio of weights). The accepted moves satisfy detailed balance, so π is stationary.'),
32205: dict(d=d5, kind="WORKED EXAMPLE",
  stmt=r"<b>Random-walk Metropolis.</b> With a symmetric proposal, $q(y\mid x)=q(x\mid y)$, the acceptance is $\alpha(x,y)=\min\bigl(1,\frac{\pi(y)}{\pi(x)}\bigr)$. The step size trades off acceptance against movement; for Gaussian-like targets in high dimension the optimal acceptance rate is about $23.4\%$ (Roberts–Gelman–Gilks).",
  hint='How big should each proposed set-up change be: small and safe, or large and risky?',
  bd=[r"<strong>$q(y\mid x)=q(x\mid y)$ = symmetric proposal.</strong> A step of a given size forwards is as likely as backwards, so the $q$ factors cancel.",
      r"<strong>$\alpha=\min(1,\pi(y)/\pi(x))$ = compare weights only.</strong> Always go uphill; go downhill with the ratio of heights.",
      r"<strong>$\approx23.4\%$ = the optimal acceptance.</strong> Tiny steps are accepted but barely move; huge steps move but are rejected; the best compromise accepts about one in four."],
  conn='<strong>Choosing the step.</strong> Moving the rear wing by a hair is almost always accepted, but the engineers learn little. A wild change is almost always rejected. A medium change explores the set-ups best.',
  cap='The target and two step sizes: tiny set-up changes are accepted but crawl, huge ones are rejected. The best compromise accepts about 23.4% of proposals.'),
32206: dict(d=d6, kind="THEOREM",
  stmt=r"<b>Gibbs sampling.</b> To sample $p(x_1,\ldots,x_d)$, update one coordinate at a time from its full conditional: $X_i^{(t+1)}\sim p(X_i\mid X_{-i}^{(t)})$. This is Metropolis–Hastings with proposal $q(y\mid x)=p(y_i\mid x_{-i})$, for which the acceptance probability is $\alpha(x,y)\equiv1$, so every proposal is accepted (Robert & Casella 10; Grimmett 6.14).",
  hint='Can you sample a joint law by redrawing one variable at a time, never rejecting?',
  bd=[r"<strong>$X_i\sim p(X_i\mid X_{-i})$ = redraw one coordinate.</strong> Hold all the others fixed and draw again from the exact conditional law.",
      r"<strong>$\alpha(x,y)=\min\bigl(1,\frac{p(y)p(x_i\mid x_{-i})}{p(x)p(y_i\mid x_{-i})}\bigr)$ = the MH ratio.</strong> Since $y_{-i}=x_{-i}$ and $p(y)=p(y_i\mid x_{-i})p(x_{-i})$, the ratio equals 1.",
      r"<strong>$\alpha\equiv1$ = never rejected.</strong> Each update is a valid move of a chain with stationary law $p$."],
  conn='<strong>Front wing, then rear wing.</strong> With the rear wing fixed, pick a new front wing angle from its conditional law; then, with that front wing fixed, pick a new rear wing angle. Alternating the two samples the pair together, with nothing thrown away.',
  cap='A Gibbs path moves along the axes: update the front wing x₁ given the rear wing x₂, then x₂ given x₁. Each update is a draw from a full conditional and is always accepted (α ≡ 1).'),
}

STORY = {
32201: dict(s='STORY 22 · STEP 1 · A LADDER OF PLACES', b="In a <b>birth–death chain</b> the flow up each rung balances the flow down.", f=[["32004", "cut equations"], ["32001", "stationary law"]], n=[["32202", "the steady queue"]]),
32202: dict(s='STORY 22 · STEP 2 · DOES HE STAY NEAR THE TOP', b="The steady law is a <b>product of up/down ratios</b>, and exists iff their sum is finite.", f=[["32201", "balance recursion"]], n=[["32203", "reversibility"], ["32705", "continuous-time queues"]]),
32203: dict(s="STORY 22 · STEP 3 · THE FILM RUN BACKWARDS", b="<b>Kolmogorov's criterion</b>: reversible iff every loop has equal chance both ways.", f=[["32004", "detailed balance"]], n=[["32204", "building reversible samplers"]]),
32204: dict(s="STORY 22 · STEP 4 · SAMPLING BY A CHAIN", b="<b>Metropolis–Hastings</b> accepts moves so that detailed balance holds for the target.", f=[["32203", "reversibility"], ["32002", "convergence to π"]], n=[["32205", "tuning"], ["32206", "never rejecting"]]),
32205: dict(s="STORY 22 · STEP 5 · THE STEP SIZE", b="<b>Random-walk Metropolis</b> trades acceptance against movement; aim near 23.4%.", f=[["32204", "MH"]], n=[["32206", "Gibbs"]]),
32206: dict(s="STORY 22 · STEP 6 · ONE COORDINATE AT A TIME", b="<b>Gibbs sampling</b> redraws from full conditionals; every move is accepted.", f=[["32204", "MH with α ≡ 1"], ["30704", "conditional laws"]], n=[["32301", "stationary random signals"]]),
}

FIX = build(CARDS)
