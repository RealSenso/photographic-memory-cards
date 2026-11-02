"""StoMA topic 02 (conditioning, Bayes, independence). Commute picture: rain / traffic / lateness on a morning."""
from commute_lib import *

SUBJECT = "StoMA"

def d1(c):
    return svg(c,
        R(10, 12, 100, 100, "#f8fafc", 1, 4), N(16, 24, "Ω: all mornings", 7, "start"),
        R(40, 40, 60, 60, "#e5e9f0", 1), N(70, 36, "B: rain", 7.5),
        E(60, 70, 22, 16, 0, "#d9dee7", 1), N(60, 73, "A∩B", 7.5), N(16, 107, "A: late", 7, "start"),
        arrow(116, 62, 140, 62, 1),
        R(146, 24, 80, 76, "#e5e9f0", 1), N(186, 20, "B is the new Ω", 7),
        E(176, 66, 28, 22, 0, "#d9dee7", 1), N(176, 69, "A∩B", 7.5),
        N(186, 116, "ℙ(A|B) = ℙ(A∩B) / ℙ(B)", 7.5), N(120, 136, "given rain, only rainy mornings count", 7))

def d2(c):
    xs = [20, 68, 116, 164]
    out = ""
    for i, x in enumerate(xs[:3]):
        out += R(x, 40, 40, 30, "#f1f5f9", 1, 3) + N(x + 20, 59, ["A₁: leave", "A₂: bus", "A₃: arrive"][i], 7)
    out += arrow(60, 55, 68, 55, 1) + arrow(108, 55, 116, 55, 1)
    out += N(60, 34, "ℙ(A₂|A₁)", 7) + N(108, 34, "ℙ(A₃|A₁∩A₂)", 6.5, "end")
    return svg(c, out, N(120, 20, "ℙ(A₁∩A₂∩A₃) = ℙ(A₁) · ℙ(A₂|A₁) · ℙ(A₃|A₁∩A₂)", 7, "middle"),
        N(120, 100, "each step conditions on everything that has happened so far", 7),
        N(120, 128, "the chance of a whole morning = product of its steps", 7.5))

def d3(c):
    out = R(24, 24, 192, 70, "#f8fafc", 1)
    for i, (x, w, nm) in enumerate([(24, 70, "B₁ dry"), (94, 80, "B₂ rain"), (174, 42, "B₃ storm")]):
        out += L(x, 24, x, 94, 1) + N(x + w / 2, 32, nm, 7)
        out += R(x + 6, 62, w - 12, 26, "#d9dee7", .8) + N(x + w / 2, 79, "A∩B" + "₁₂₃"[i], 6.5)
    return svg(c, out, N(120, 16, "partition of mornings by weather", 7.5),
        N(120, 110, "A = late = (A∩B₁) ∪ (A∩B₂) ∪ (A∩B₃)", 7.5),
        N(120, 126, "ℙ(A) = ∑ ℙ(A|Bᵢ) ℙ(Bᵢ)", 8), N(120, 139, "the Bᵢ must cover Ω with no gap or overlap", 6.5))

def d4(c):
    return svg(c,
        N(36, 20, "causes Bₖ", 7.5), N(36, 36, "B₁ rain", 7.5), N(36, 66, "B₂ breakdown", 7.5), N(36, 96, "B₃ overslept", 7.5),
        arrow(70, 34, 150, 62, 1), arrow(70, 63, 150, 66, 1), arrow(70, 93, 150, 70, 1),
        N(104, 38, "ℙ(A|B₁)", 6.5, "start"), N(104, 60, "ℙ(A|B₂)", 6.5, "start"), N(104, 90, "ℙ(A|B₃)", 6.5, "start"),
        R(152, 52, 56, 24, "#e5e9f0", 1, 4), N(180, 68, "A: late", 8),
        N(120, 116, "reverse: late, so which cause?", 7.5), N(120, 130, "ℙ(Bₖ|A) = ℙ(A|Bₖ) ℙ(Bₖ) / ℙ(A)", 7.5))

def d5(c):
    return svg(c,
        R(14, 20, 100, 70, "#f8fafc", 1, 4), N(64, 14, "A ⊥ B: ℙ(A∩B) = ℙ(A) ℙ(B)", 7),
        R(26, 36, 46, 38, "#f1f5f9", 1), R(50, 36, 40, 38, "none", 1, 0, "3 2"), N(38, 54, "A", 8), N(80, 54, "B", 8),
        R(126, 20, 100, 70, "#f8fafc", 1, 4), N(176, 14, "A ⊥ B | C: inside C only", 7),
        R(136, 30, 80, 52, "#e5e9f0", .8, 0, "3 2"), N(206, 40, "C", 7.5, "end"),
        E(160, 58, 14, 12, 0, "#f1f5f9", 1), E(188, 58, 14, 12, 0, "#f1f5f9", 1), N(160, 61, "A", 7.5), N(188, 61, "B", 7.5),
        N(120, 112, "A: I'm late   B: my friend is late", 7), N(120, 124, "dependent in general, independent given C: same jam", 7))

def d6(c):
    out = ""
    for i, (x, nm) in enumerate([(20, "1: R G"), (68, "2: R B"), (116, "3: G B"), (164, "4: R G B")]):
        out += R(x, 36, 44, 30, "#f1f5f9", 1, 3) + N(x + 22, 53, nm, 7)
    return svg(c, out, N(120, 24, "4 equally likely kinds of morning, each ¼", 7.5),
        N(120, 82, "R rain · G gridlock · B breakdown, each in 2 of 4: ℙ = ½", 7),
        N(120, 96, "pairs: ℙ(R∩G) = ¼ = ½·½ ✓", 7.5),
        N(120, 110, "triple: ℙ(R∩G∩B) = ¼ ≠ ⅛ ✗", 7.5), N(120, 132, "pairwise independent, not mutually", 7.5))

CARDS = {
30201: dict(d=d1, kind="DEFINITION",
  stmt=r"<b>Conditional probability.</b> Let $B\in\mathcal F$ with $\mathbb P(B)>0$. The conditional probability of $A\in\mathcal F$ given $B$ is $\mathbb P(A\mid B)=\dfrac{\mathbb P(A\cap B)}{\mathbb P(B)}$. The map $A\mapsto\mathbb P(A\mid B)$ is itself a probability measure on $(\Omega,\mathcal F)$, with $\mathbb P(B\mid B)=1$ (Ross 3.2; Grimmett 1.4).",
  hint="If you already know it is raining, which mornings are still in play, and what is your chance of being late among them?",
  bd=[r"<strong>$\mathbb P(A\cap B)$ = mornings that are both late and rainy.</strong> This is the part of the rainy mornings in which you were also late.",
      r"<strong>$\mathbb P(B)>0$ = the condition must be possible.</strong> It is the size of the new, smaller set of mornings; dividing by it rescales that set to total 1.",
      r"<strong>$\mathbb P(B\mid B)=1$ = the new universe is certain.</strong> Once you know it rains, only rainy mornings remain, and they now have total chance 1."],
  conn=r"<strong>Looking out of the window.</strong> Seeing rain throws away every dry morning. Among the rainy mornings that are left, you ask what share of them ends late. Same mornings, smaller universe, rescaled to 1.",
  cap="Left: all mornings Ω, with the rain region B and the late region A overlapping in A∩B. Right: after learning B, only B remains, and ℙ(A|B) is the share of B taken by A∩B."),
30202: dict(d=d2, kind="THEOREM",
  stmt=r"<b>Multiplication rule (chain rule).</b> For events $A_1,\ldots,A_n$ with $\mathbb P(A_1\cap\cdots\cap A_{n-1})>0$, $\mathbb P\!\left(\bigcap_{i=1}^nA_i\right)=\mathbb P(A_1)\prod_{k=2}^n\mathbb P\!\left(A_k\,\middle|\,\bigcap_{j=1}^{k-1}A_j\right)$. For two events, $\mathbb P(A\cap B)=\mathbb P(A)\mathbb P(B\mid A)$ (Ross 3.2; Grimmett 1.4).",
  hint="How do you get the chance of a whole morning going a certain way from the chances of its steps?",
  bd=[r"<strong>$\mathbb P(A_1)$ = how likely the first step is.</strong> For instance, leaving the house on time.",
      r"<strong>$\mathbb P(A_k\mid\bigcap_{j<k}A_j)$ = each next step given the whole past.</strong> The chance the bus comes depends on what has happened so far this morning.",
      r"<strong>$\prod_k$ = multiply the steps.</strong> The chance that everything happens is the product of these stepwise chances; every earlier history must have positive probability."],
  conn=r"<strong>A morning built step by step.</strong> Out of the door on time, bus within five minutes, no jam on the bridge: the chance of all three is the chance of the first, times the chance of the second given the first, times the third given both.",
  cap="Three steps A₁ (leave), A₂ (bus), A₃ (arrive). ℙ(A₁∩A₂∩A₃) is ℙ(A₁) times ℙ(A₂|A₁) times ℙ(A₃|A₁∩A₂), each conditioned on the whole past."),
30203: dict(d=d3, kind="THEOREM",
  stmt=r"<b>Law of total probability.</b> Let $B_1,\ldots,B_n$ be a partition of $\Omega$ ($B_i\cap B_j=\emptyset$ for $i\ne j$, $\bigcup_iB_i=\Omega$) with $\mathbb P(B_i)>0$. Then for every event $A$, $\mathbb P(A)=\sum_{i=1}^n\mathbb P(A\mid B_i)\,\mathbb P(B_i)$ (Ross 3.3; Grimmett 1.4).",
  hint="If the weather is dry, rainy or stormy, how do you build the chance of being late from the chance in each weather?",
  bd=[r"<strong>$B_i$ = the weather types.</strong> Every morning is exactly one of them: they cover $\Omega$ and do not overlap.",
      r"<strong>$\mathbb P(A\mid B_i)$ = chance of being late within one weather type.</strong> This is the easier question, asked inside one case.",
      r"<strong>$\sum\ldots\mathbb P(B_i)$ = weighted average.</strong> Weight each case's chance by how often that weather happens, then add: late mornings are split by weather and counted once."],
  conn=r"<strong>Late in each kind of weather.</strong> You know how often you are late when it is dry, rainy and stormy, and how often each weather occurs. The overall chance of being late is the average of the three, weighted by the weather's frequency.",
  cap="Mornings split into B₁ dry, B₂ rain, B₃ storm. The late part A∩Bᵢ sits in each block, and ℙ(A) = ∑ℙ(A|Bᵢ)ℙ(Bᵢ) adds them up."),
30204: dict(d=d4, kind="THEOREM",
  stmt=r"<b>Bayes' theorem.</b> Let $B_1,\ldots,B_n$ partition $\Omega$ with $\mathbb P(B_i)>0$, and let $\mathbb P(A)>0$. Then $\mathbb P(B_k\mid A)=\dfrac{\mathbb P(A\mid B_k)\,\mathbb P(B_k)}{\sum_{i=1}^n\mathbb P(A\mid B_i)\,\mathbb P(B_i)}=\dfrac{\mathbb P(A\mid B_k)\,\mathbb P(B_k)}{\mathbb P(A)}$ (Ross 3.3; Grimmett 1.4).",
  hint="You arrive late. How do you turn “how often does each cause make me late” into “which cause was it?”",
  bd=[r"<strong>$\mathbb P(B_k)$ = prior, how common the cause is.</strong> Rain, breakdown and oversleeping each happen with some base frequency.",
      r"<strong>$\mathbb P(A\mid B_k)$ = likelihood, how often the cause makes you late.</strong> A breakdown almost always makes you late; light rain rarely does.",
      r"<strong>$\mathbb P(A)$ = normaliser.</strong> The total chance of being late, summed over all causes, so that the chances of the causes given lateness add to 1."],
  conn=r"<strong>Late, so why?</strong> You walk into class late and the question flips from “what does each cause do to me” to “which cause did this”. A rare cause that nearly always makes you late can still be the likeliest explanation.",
  cap="Arrows run from the causes B₁, B₂, B₃ to the effect A (late), labelled ℙ(A|Bₖ). Bayes runs backwards: ℙ(Bₖ|A) = ℙ(A|Bₖ)ℙ(Bₖ)/ℙ(A)."),
30205: dict(d=d5, kind="DEFINITION",
  stmt=r"<b>Independence and conditional independence.</b> Events $A,B$ are independent if $\mathbb P(A\cap B)=\mathbb P(A)\mathbb P(B)$ (equivalently $\mathbb P(A\mid B)=\mathbb P(A)$ when $\mathbb P(B)>0$). Given an event $C$ with $\mathbb P(C)>0$, $A$ and $B$ are conditionally independent given $C$ if $\mathbb P(A\cap B\mid C)=\mathbb P(A\mid C)\mathbb P(B\mid C)$. Neither implies the other (Ross 3.4; Grimmett 1.5).",
  hint="When does learning that B happened tell you nothing about A, and how can a third fact change that?",
  bd=[r"<strong>$\mathbb P(A\cap B)=\mathbb P(A)\mathbb P(B)$ = knowing B leaves A unchanged.</strong> The joint chance is just the product of the two separate chances.",
      r"<strong>$\mathbb P(A\cap B\mid C)$ = the same test inside the case $C$.</strong> It asks whether $A$ and $B$ still tell you nothing about each other once you know $C$.",
      r"<strong>Neither way implies the other.</strong> Two events can be dependent overall and independent given $C$ (a shared cause), or independent overall and dependent given $C$."],
  conn=r"<strong>Two people late on the same bus.</strong> Whether you and a friend on the same route are late are linked, because of the jam. Once you know there was a jam, your lateness says nothing more about theirs.",
  cap="Left: A and B with ℙ(A∩B) = ℙ(A)ℙ(B). Right: inside the case C (a jam), A and B satisfy ℙ(A∩B|C) = ℙ(A|C)ℙ(B|C), though they may be dependent overall."),
30206: dict(d=d6, kind="WORKED EXAMPLE",
  stmt=r"<b>Bernstein's example.</b> A tetrahedron has faces coloured $\{R,G\}$, $\{R,B\}$, $\{G,B\}$ and $\{R,G,B\}$, each face rolled with probability $\tfrac14$. Then $\mathbb P(R)=\mathbb P(G)=\mathbb P(B)=\tfrac12$ and $\mathbb P(R\cap G)=\tfrac14=\mathbb P(R)\mathbb P(G)$ (and likewise for the other pairs), so the events are pairwise independent. But $\mathbb P(R\cap G\cap B)=\tfrac14\ne\tfrac18=\mathbb P(R)\mathbb P(G)\mathbb P(B)$, so they are not mutually independent (Grimmett 1.5).",
  hint="Can three events be independent in every pair, yet fail to be independent together?",
  bd=[r"<strong>$\mathbb P(R)=\tfrac12$ = each colour is on two of the four equally likely faces.</strong> Say R is rain, G gridlock, B breakdown, each present on two of four kinds of morning.",
      r"<strong>$\mathbb P(R\cap G)=\tfrac14=\mathbb P(R)\mathbb P(G)$ = every pair multiplies.</strong> Each pair of colours shares exactly one face, so every pair is independent.",
      r"<strong>$\mathbb P(R\cap G\cap B)=\tfrac14\ne\tfrac18$ = the triple does not multiply.</strong> Only face 4 has all three, so mutual independence needs more equations than the pairs."],
  conn=r"<strong>Four kinds of morning.</strong> Imagine only four equally likely mornings, each showing a different mix of rain, gridlock and breakdown. Any two of the three troubles look unrelated, but all three together happen far more often than independence would give.",
  cap="Four equally likely mornings with troubles R, G, B. Every pair has ℙ = ¼ = ½·½, but ℙ(R∩G∩B) = ¼ ≠ ⅛, so pairwise independence is not mutual independence."),
}

STORY = {
30201: dict(s="STORY 2 · STEP 1 · KNOWING SOMETHING", b="Learning part of the morning <b>shrinks the universe</b> to B and rescales it to total 1: that is a conditional chance.", f=[["30101", "the probability space it conditions"]], n=[["30202", "chaining the steps"], ["30203", "splitting by cases"]]),
30202: dict(s="STORY 2 · STEP 2 · STEP BY STEP", b="Rearranging the definition gives the <b>chain rule</b>: the chance of a whole morning is the product of its stepwise conditional chances.", f=[["30201", "conditional probability"], ["30105", "overlaps of several events"]], n=[["30203", "the same product, cut by cases"], ["31901", "Markov chains drop the long history"]]),
30203: dict(s="STORY 2 · STEP 3 · CASE BY CASE", b="Cut the mornings into <b>cases</b> that cover everything without overlap, solve each case, and add them back weighted.", f=[["30202", "multiplying through the steps"]], n=[["30204", "running it backwards"], ["31204", "the same split for variance"]]),
30204: dict(s="STORY 2 · STEP 4 · BACKWARDS", b="Bayes <b>reverses the arrow</b>: from the effect (late) back to the cause (rain, breakdown, oversleeping).", f=[["30203", "the total chance as normaliser"]], n=[["30205", "when evidence changes nothing"], ["31201", "conditional expectation"]]),
30205: dict(s="STORY 2 · STEP 5 · NOTHING LEARNED", b="Two events are <b>independent</b> when one tells you nothing about the other, and a third fact can create or remove that.", f=[["30204", "updating on evidence"]], n=[["30206", "pairs versus all together"], ["30705", "independent random variables"]]),
30206: dict(s="STORY 2 · STEP 6 · THE TRAP", b="Independence in every pair does <b>not</b> give independence of all together: four mornings show it.", f=[["30205", "independence"]], n=[["31001", "exchangeability, a weaker symmetry"]]),
}

FIX = build(CARDS)
