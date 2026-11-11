"""StoMA topic 02 (conditioning, Bayes, independence). F1 picture: pole position, the kind of circuit, and the reasons Max does not win."""
from f1_lib import *

SUBJECT = "StoMA"

def d1(c):
    return svg(c,
        R(10, 12, 100, 100, "#f8fafc", 1, 4), N(16, 24, "Ω: all races", 7, "start"),
        R(40, 40, 60, 60, "#e5e9f0", 1), N(70, 36, "B: Max on pole", 7),
        E(60, 70, 22, 16, 0, "#d9dee7", 1), N(60, 73, "A∩B", 7.5), N(16, 107, "A: Max wins", 7, "start"),
        arrow(116, 62, 140, 62, 1),
        R(146, 24, 80, 76, "#e5e9f0", 1), N(186, 20, "B is the new Ω", 7),
        E(176, 66, 28, 22, 0, "#d9dee7", 1), N(176, 69, "A∩B", 7.5),
        N(186, 116, "ℙ(A|B) = ℙ(A∩B) / ℙ(B)", 7.5), N(120, 136, "starting from pole: only those races count", 7))

def d2(c):
    xs = [20, 68, 116, 164]
    out = ""
    for i, x in enumerate(xs[:3]):
        out += R(x, 40, 40, 30, "#f1f5f9", 1, 3) + N(x + 20, 52, ["A₁: pole", "A₂: leads", "A₃: wins"][i], 7) + N(x + 20, 63, ["position", "lap 1", "the race"][i], 6.5)
    out += arrow(60, 55, 68, 55, 1) + arrow(108, 55, 116, 55, 1)
    out += N(60, 34, "ℙ(A₂|A₁)", 7) + N(108, 34, "ℙ(A₃|A₁∩A₂)", 6.5, "end")
    return svg(c, out, N(120, 20, "ℙ(A₁∩A₂∩A₃) = ℙ(A₁) · ℙ(A₂|A₁) · ℙ(A₃|A₁∩A₂)", 7, "middle"),
        N(120, 100, "each step conditions on everything that has happened so far", 7),
        N(120, 128, "the chance of a whole weekend = product of its steps", 7.5))

def d3(c):
    out = R(24, 24, 192, 70, "#f8fafc", 1)
    for i, (x, w, nm) in enumerate([(24, 70, "B₁ high-speed"), (94, 80, "B₂ mixed"), (174, 42, "B₃ street")]):
        out += L(x, 24, x, 94, 1) + N(x + w / 2, 32, nm, 7)
        out += R(x + 6, 62, w - 12, 26, "#d9dee7", .8) + N(x + w / 2, 79, "A∩B" + "₁₂₃"[i], 6.5)
    return svg(c, out, N(120, 16, "partition of races by type of circuit", 7.5),
        N(120, 110, "A = Max wins = (A∩B₁) ∪ (A∩B₂) ∪ (A∩B₃)", 7.5),
        N(120, 126, "ℙ(A) = ∑ ℙ(A|Bᵢ) ℙ(Bᵢ)", 8), N(120, 139, "the Bᵢ must cover Ω with no gap or overlap", 6.5))

def d4(c):
    return svg(c,
        N(36, 20, "causes Bₖ", 7.5), N(36, 36, "B₁ engine issue", 7), N(36, 66, "B₂ slow pit stop", 7), N(36, 96, "B₃ rain gamble", 7),
        arrow(72, 34, 150, 62, 1), arrow(72, 63, 150, 66, 1), arrow(72, 93, 150, 70, 1),
        N(104, 38, "ℙ(A|B₁)", 6.5, "start"), N(104, 60, "ℙ(A|B₂)", 6.5, "start"), N(104, 90, "ℙ(A|B₃)", 6.5, "start"),
        R(152, 52, 64, 24, "#e5e9f0", 1, 4), N(184, 68, "A: no win", 8),
        N(120, 116, "reverse: Max did not win, so which cause?", 7.5), N(120, 130, "ℙ(Bₖ|A) = ℙ(A|Bₖ) ℙ(Bₖ) / ℙ(A)", 7.5))

def d5(c):
    return svg(c,
        R(14, 20, 100, 70, "#f8fafc", 1, 4), N(64, 14, "A ⊥ B: ℙ(A∩B) = ℙ(A) ℙ(B)", 7),
        R(26, 36, 46, 38, "#f1f5f9", 1), R(50, 36, 40, 38, "none", 1, 0, "3 2"), N(38, 54, "A", 8), N(80, 54, "B", 8),
        R(126, 20, 100, 70, "#f8fafc", 1, 4), N(176, 14, "A ⊥ B | C: inside C only", 7),
        R(136, 30, 80, 52, "#e5e9f0", .8, 0, "3 2"), N(206, 40, "C", 7.5, "end"),
        E(160, 58, 14, 12, 0, "#f1f5f9", 1), E(188, 58, 14, 12, 0, "#f1f5f9", 1), N(160, 61, "A", 7.5), N(188, 61, "B", 7.5),
        N(120, 112, "A: Max on the podium   B: Checo on the podium", 7), N(120, 124, "dependent in general, independent given C: the car is fast", 6.5))

def d6(c):
    out = ""
    for i, (x, nm) in enumerate([(20, "1: R S"), (68, "2: R F"), (116, "3: S F"), (164, "4: R S F")]):
        out += R(x, 36, 44, 30, "#f1f5f9", 1, 3) + N(x + 22, 53, nm, 7)
    return svg(c, out, N(120, 24, "4 equally likely kinds of race, each ¼", 7.5),
        N(120, 82, "R rain · S safety car · F red flag, each in 2 of 4: ℙ = ½", 6.5),
        N(120, 96, "pairs: ℙ(R∩S) = ¼ = ½·½ ✓", 7.5),
        N(120, 110, "triple: ℙ(R∩S∩F) = ¼ ≠ ⅛ ✗", 7.5), N(120, 132, "pairwise independent, not mutually", 7.5))

CARDS = {
30201: dict(d=d1, kind="DEFINITION",
  stmt=r"<b>Conditional probability.</b> Let $B\in\mathcal F$ with $\mathbb P(B)>0$. The conditional probability of $A\in\mathcal F$ given $B$ is $\mathbb P(A\mid B)=\dfrac{\mathbb P(A\cap B)}{\mathbb P(B)}$. The map $A\mapsto\mathbb P(A\mid B)$ is itself a probability measure on $(\Omega,\mathcal F)$, with $\mathbb P(B\mid B)=1$ (Ross 3.2; Grimmett 1.4).",
  hint='If you already know Max starts from pole, which races are still in play, and what is his chance of winning among them?',
  bd=[r"<strong>$\mathbb P(A\cap B)$ = races Max started from pole and won.</strong> This is the part of the pole positions that he also turned into a win.",
      r"<strong>$\mathbb P(B)>0$ = the condition must be possible.</strong> It is the size of the new, smaller set of races; dividing by it rescales that set to total 1.",
      r"<strong>$\mathbb P(B\mid B)=1$ = the new universe is certain.</strong> Once you know he is on pole, only those races remain, and they now have total chance 1."],
  conn='<strong>Qualifying is done.</strong> Max on pole throws away every race where he starts further back. Among the races that are left, you ask what share of them he wins. Same races, smaller universe, rescaled to 1.',
  cap='Left: all races Ω, with B (Max on pole) and A (Max wins) overlapping in A∩B. Right: after learning B, only B remains, and ℙ(A|B) is the share of B taken by A∩B.'),
30202: dict(d=d2, kind="THEOREM",
  stmt=r"<b>Chain rule.</b> For events with $\mathbb P(A_1\cap\cdots\cap A_{n-1})>0$, $\mathbb P(\bigcap_{i=1}^nA_i)=\mathbb P(A_1)\prod_{k=2}^n\mathbb P(A_k\mid\bigcap_{j<k}A_j)$. For two events, $\mathbb P(A\cap B)=\mathbb P(A)\mathbb P(B\mid A)$ (Ross 3.2; Grimmett 1.4).",
  hint='How do you get the chance of a whole race weekend going a certain way from the chances of its steps?',
  bd=[r"<strong>$\mathbb P(A_1)$ = the first step.</strong> For instance, taking pole position in qualifying.",
      r"<strong>$\mathbb P(A_k\mid\bigcap_{j<k}A_j)$ = each step given the whole past.</strong> The chance of leading after lap 1 depends on how the weekend has gone so far.",
      r"<strong>$\prod_k$ = multiply the steps.</strong> The chance that everything happens is the product of the stepwise chances."],
  conn='<strong>A weekend built step by step.</strong> Take pole, keep the lead through turn 1, hold it to the chequered flag: first chance, times second given first, times third given both.',
  cap='Three steps A₁ (pole), A₂ (leads lap 1), A₃ (wins). ℙ(A₁∩A₂∩A₃) is ℙ(A₁) times ℙ(A₂|A₁) times ℙ(A₃|A₁∩A₂), each conditioned on the whole past.'),
30203: dict(d=d3, kind="THEOREM",
  stmt=r"<b>Law of total probability.</b> Let $B_1,\ldots,B_n$ be a partition of $\Omega$ ($B_i\cap B_j=\emptyset$ for $i\ne j$, $\bigcup_iB_i=\Omega$) with $\mathbb P(B_i)>0$. Then for every event $A$, $\mathbb P(A)=\sum_{i=1}^n\mathbb P(A\mid B_i)\,\mathbb P(B_i)$ (Ross 3.3; Grimmett 1.4).",
  hint="If the circuit is high-speed, mixed or a street track, how do you build Max's chance of winning from his chance on each?",
  bd=[r"<strong>$B_i$ = the kinds of circuit.</strong> Every race is on exactly one kind: they cover $\Omega$ and do not overlap.",
      r"<strong>$\mathbb P(A\mid B_i)$ = chance of winning on one kind of circuit.</strong> This is the easier question, asked inside one case.",
      r"<strong>$\sum\ldots\mathbb P(B_i)$ = weighted average.</strong> Weight each case's chance by how often the calendar has that kind of circuit, then add: wins are split by circuit and counted once."],
  conn='<strong>Wins on each kind of track.</strong> You know how often Max wins on high-speed, mixed and street circuits, and how many of each the calendar has. His overall chance of winning is the average of the three, weighted by how often each kind comes up.',
  cap='Races split into B₁ high-speed, B₂ mixed, B₃ street circuits. The winning part A∩Bᵢ sits in each block, and ℙ(A) = ∑ℙ(A|Bᵢ)ℙ(Bᵢ) adds them up.'),
30204: dict(d=d4, kind="THEOREM",
  stmt=r"<b>Bayes' theorem.</b> Let $B_1,\ldots,B_n$ partition $\Omega$ with $\mathbb P(B_i)>0$, and let $\mathbb P(A)>0$. Then $\mathbb P(B_k\mid A)=\dfrac{\mathbb P(A\mid B_k)\,\mathbb P(B_k)}{\sum_{i=1}^n\mathbb P(A\mid B_i)\,\mathbb P(B_i)}=\dfrac{\mathbb P(A\mid B_k)\,\mathbb P(B_k)}{\mathbb P(A)}$ (Ross 3.3; Grimmett 1.4).",
  hint='Max did not win. How do you turn “how often does each cause cost him the win” into “which cause was it?”',
  bd=[r"<strong>$\mathbb P(B_k)$ = prior, how common the cause is.</strong> An engine issue, a slow pit stop and a failed rain gamble each happen with some base frequency.",
      r"<strong>$\mathbb P(A\mid B_k)$ = likelihood, how often the cause costs the win.</strong> An engine issue almost always does; a slow stop sometimes only costs a few seconds.",
      r"<strong>$\mathbb P(A)$ = normaliser.</strong> The total chance of not winning, summed over all causes, so that the chances of the causes given the result add to 1."],
  conn='<strong>No win, so why?</strong> After the chequered flag the question flips from “what does each problem do to Max” to “which problem did this”. A rare problem that nearly always costs the win, like an engine issue, can still be the likeliest explanation.',
  cap='Arrows run from the causes B₁ (engine issue), B₂ (slow pit stop), B₃ (rain gamble) to the effect A (Max did not win), labelled ℙ(A|Bₖ). Bayes runs backwards: ℙ(Bₖ|A) = ℙ(A|Bₖ)ℙ(Bₖ)/ℙ(A).'),
30205: dict(d=d5, kind="DEFINITION",
  stmt=r"<b>Independence and conditional independence.</b> Events $A,B$ are independent if $\mathbb P(A\cap B)=\mathbb P(A)\mathbb P(B)$ (equivalently $\mathbb P(A\mid B)=\mathbb P(A)$ when $\mathbb P(B)>0$). Given an event $C$ with $\mathbb P(C)>0$, $A$ and $B$ are conditionally independent given $C$ if $\mathbb P(A\cap B\mid C)=\mathbb P(A\mid C)\mathbb P(B\mid C)$. Neither implies the other (Ross 3.4; Grimmett 1.5).",
  hint='When does learning that B happened tell you nothing about A, and how can a third fact change that?',
  bd=[r"<strong>$\mathbb P(A\cap B)=\mathbb P(A)\mathbb P(B)$ = knowing B leaves A unchanged.</strong> The joint chance is just the product of the two separate chances.",
      r"<strong>$\mathbb P(A\cap B\mid C)$ = the same test inside the case $C$.</strong> It asks whether $A$ and $B$ still tell you nothing about each other once you know $C$.",
      r"<strong>Neither way implies the other.</strong> Two events can be dependent overall and independent given $C$ (a shared cause), or independent overall and dependent given $C$."],
  conn="<strong>Two Red Bulls on the same weekend.</strong> Whether Max and his team-mate Checo reach the podium are linked, because they drive the same car: a fast car lifts both. Once you know the car is fast this weekend, Max's podium says nothing more about Checo's.",
  cap='Left: A and B with ℙ(A∩B) = ℙ(A)ℙ(B). Right: inside the case C (the car is fast this weekend), A (Max on the podium) and B (Checo on the podium) satisfy ℙ(A∩B|C) = ℙ(A|C)ℙ(B|C), though they are dependent overall.'),
30206: dict(d=d6, kind="WORKED EXAMPLE",
  stmt=r"<b>Bernstein's example.</b> A tetrahedron has faces coloured $\{R,G\}$, $\{R,B\}$, $\{G,B\}$ and $\{R,G,B\}$, each face rolled with probability $\tfrac14$. Then $\mathbb P(R)=\mathbb P(G)=\mathbb P(B)=\tfrac12$ and $\mathbb P(R\cap G)=\tfrac14=\mathbb P(R)\mathbb P(G)$ (and likewise for the other pairs), so the events are pairwise independent. But $\mathbb P(R\cap G\cap B)=\tfrac14\ne\tfrac18=\mathbb P(R)\mathbb P(G)\mathbb P(B)$, so they are not mutually independent (Grimmett 1.5).",
  hint='Can three events be independent in every pair, yet fail to be independent together?',
  bd=[r"<strong>$\mathbb P(R)=\tfrac12$ = each colour is on two of the four equally likely faces.</strong> Say R is rain, S a safety car, F a red flag, each present in two of four kinds of race.",
      r"<strong>$\mathbb P(R\cap G)=\tfrac14=\mathbb P(R)\mathbb P(G)$ = every pair multiplies.</strong> Each pair of colours shares exactly one face, so every pair is independent.",
      r"<strong>$\mathbb P(R\cap G\cap B)=\tfrac14\ne\tfrac18$ = the triple does not multiply.</strong> Only face 4 has all three, so mutual independence needs more equations than the pairs."],
  conn='<strong>Four kinds of race.</strong> Imagine only four equally likely races, each with a different mix of rain, safety car and red flag. Any two of the three look unrelated, but all three together happen far more often than independence would give.',
  cap='Four equally likely races with R (rain), S (safety car), F (red flag). Every pair has ℙ = ¼ = ½·½, but ℙ(R∩S∩F) = ¼ ≠ ⅛, so pairwise independence is not mutual independence.'),
}

STORY = {
30201: dict(s="STORY 2 · STEP 1 · KNOWING SOMETHING", b='Learning part of the race <b>shrinks the universe</b> to B and rescales it to total 1: that is a conditional chance.', f=[["30101", "the probability space it conditions"]], n=[["30202", "chaining the steps"], ["30203", "splitting by cases"]]),
30202: dict(s="STORY 2 · STEP 2 · STEP BY STEP", b='Rearranging the definition gives the <b>chain rule</b>: the chance of a whole race weekend is the product of its stepwise conditional chances.', f=[["30201", "conditional probability"], ["30105", "overlaps of several events"]], n=[["30203", "the same product, cut by cases"], ["31901", "Markov chains drop the long history"]]),
30203: dict(s="STORY 2 · STEP 3 · CASE BY CASE", b='Cut the races into <b>cases</b> that cover everything without overlap, solve each case, and add them back weighted.', f=[["30202", "multiplying through the steps"]], n=[["30204", "running it backwards"], ["31204", "the same split for variance"]]),
30204: dict(s="STORY 2 · STEP 4 · BACKWARDS", b='Bayes <b>reverses the arrow</b>: from the effect (no win) back to the cause (engine, pit stop, rain gamble).', f=[["30203", "the total chance as normaliser"]], n=[["30205", "when evidence changes nothing"], ["31201", "conditional expectation"]]),
30205: dict(s="STORY 2 · STEP 5 · NOTHING LEARNED", b="Two events are <b>independent</b> when one tells you nothing about the other, and a third fact can create or remove that.", f=[["30204", "updating on evidence"]], n=[["30206", "pairs versus all together"], ["30705", "independent random variables"]]),
30206: dict(s="STORY 2 · STEP 6 · THE TRAP", b='Independence in every pair does <b>not</b> give independence of all together: four kinds of race show it.', f=[["30205", "independence"]], n=[["31001", "exchangeability, a weaker symmetry"]]),
}

FIX = build(CARDS)
