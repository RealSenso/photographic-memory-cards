"""StoMA topic 01 (probability spaces) in the CMO card format. Picture: your morning commute to campus by bus.
Ω = all possible mornings; an event is a yes/no question about a morning; P says how likely."""
from commute_lib import *

SUBJECT = "StoMA"

def d1(c):
    return svg(c,
        R(10, 12, 220, 100, "#f8fafc", 1, 6), N(18, 24, "Ω = every possible morning", 7.5, "start"),
        E(80, 66, 46, 30, 0, "#f1f5f9", 1), N(80, 64, "A: late", 7.5), N(80, 74, "A ∈ ℱ", 7.5),
        C(66, 82, 1.8), N(72, 85, "ω", 7, "start"),
        N(80, 106, "Aᶜ: everything outside A, also in ℱ", 6.5, "start"),
        arrow(134, 56, 176, 56, 1), N(155, 50, "ℙ(A)", 8), 
        L(180, 56, 224, 56, 1), N(180, 69, "0", 7), N(224, 69, "1", 7, "end"), C(196, 56, 2.2),
        N(120, 132, "ℙ : ℱ → [0, 1] on (Ω, ℱ)", 8))

def d2(c):
    return svg(c,
        R(10, 12, 220, 100, "#f8fafc", 1, 6), N(18, 24, "Ω", 8, "start"),
        E(60, 66, 32, 26, 0, "#f1f5f9", 1), N(60, 69, "A₁", 8), E(120, 66, 32, 26, 0, "#f1f5f9", 1), N(120, 69, "A₂", 8), E(180, 66, 32, 26, 0, "#f1f5f9", 1), N(180, 69, "A₃", 8),
        N(120, 102, "disjoint: no morning is in two of them", 6.5),
        N(120, 128, "ℙ(A) ≥ 0     ℙ(Ω) = 1     ℙ(⋃Aᵢ) = ∑ℙ(Aᵢ)", 7.5))

def d3(c):
    return svg(c,
        E(120, 60, 84, 44, 0, "#f8fafc", 1), E(120, 60, 64, 33, 0, "#f1f5f9", 1), E(120, 60, 48, 22, 0, "#e5e9f0", 1), E(120, 60, 24, 11, 0, "#d9dee7", 1),
        N(120, 63, "A", 8), N(228, 60, "Bₙ ↓ B", 7.5, "end"), N(20, 60, "Aₙ ↑ A", 7.5, "start"),
        N(120, 122, "ℙ(Aₙ) → ℙ(A) = lim ℙ(Aₙ)", 7.5),
        N(120, 134, "more days checked: the event fills up or shrinks smoothly", 7))

def d4(c):
    return svg(c,
        E(84, 52, 40, 28, 0, "#f1f5f9", 1), E(132, 52, 40, 28, 0, "#f1f5f9", 1), E(108, 88, 40, 28, 0, "#f1f5f9", 1),
        N(62, 48, "A₁", 8), N(154, 48, "A₂", 8), N(108, 104, "A₃", 8),
        N(108, 20, "overlaps counted twice", 7), 
        N(196, 54, "ℙ(⋃Aᵢ)", 8), N(196, 66, "≤ ∑ℙ(Aᵢ)", 8), N(196, 80, "even if they", 6.5), N(196, 89, "overlap", 6.5),
        N(120, 136, "late on day 1, 2 or 3: no more than the three chances added", 6.5))

def d5(c):
    return svg(c,
        E(84, 52, 40, 28, 0, "none", 1), E(132, 52, 40, 28, 0, "none", 1), E(108, 88, 40, 28, 0, "none", 1),
        PG("108,40 96,60 120,60", "#d9dee7", .8),
        N(62, 46, "−ℙ(A₁∩A₂)", 6.5), N(60, 118, "add singles, subtract pairs,", 7, "start"), N(60, 128, "add the triple (−1)ⁿ⁻¹", 7, "start"),
        N(206, 52, "Σℙ(Aᵢ)", 7.5), N(206, 64, "−Σℙ(Aᵢ∩Aⱼ)", 7.5), N(206, 76, "+ℙ(A₁∩A₂∩A₃)", 7.5), N(120, 14, "late on at least one of 3 days", 7.5))

def d6(c):
    return svg(c,
        ax(24, 112, 226, 18), N(226, 124, "n days", 7, "end"), N(30, 22, "ℙ(Bₙ)", 7.5, "start"),
        fn(lambda x: 112 - 84 * 0.5 ** ((x - 24) / 28), 24, 226, 40, 1.1),
        dash(24, 112, 226, 112), N(190, 104, "limit = 0", 7.5), N(126, 44, "Bₙ: bus on time n days in a row", 7, "start"), N(126, 55, "(1/2)ⁿ", 8, "start"),
        N(120, 136, "B = never late, ever: ℙ(B) = 0, yet possible", 7))

CARDS = {
30101: dict(d=d1, kind="DEFINITION",
  stmt=r"<b>Probability space.</b> A probability space is a triple $(\Omega,\mathcal F,\mathbb P)$: $\Omega$ is a nonempty set (the sample space); $\mathcal F$ is a $\sigma$-algebra of subsets of $\Omega$, i.e. $\Omega\in\mathcal F$, $A\in\mathcal F\Rightarrow A^c\in\mathcal F$, and $A_1,A_2,\ldots\in\mathcal F\Rightarrow\bigcup_i A_i\in\mathcal F$; and $\mathbb P:\mathcal F\to[0,1]$ is a probability measure (Ross 2.2; Grimmett 1.2).",
  hint="What three things must you fix before you can say how likely it is that you are late?",
  bd=[r"<strong>$\Omega$ = every possible morning.</strong> One point $\omega$ is one complete morning: when the bus came, how long the ride took, what the weather did.",
      r"<strong>$A\in\mathcal F\Rightarrow A^c\in\mathcal F$ = the questions you may ask.</strong> If you can ask “was I late?” you can also ask “was I not late?”; and any countable yes/no combination is allowed.",
      r"<strong>$\mathbb P:\mathcal F\to[0,1]$ = a likelihood for each question.</strong> It scores each allowed question between 0 (never) and 1 (always)."],
  conn=r"<strong>All the mornings there could be.</strong> Before you leave home, the coming morning is one point in the set of all mornings. “Was I late?” marks a region of that set, and $\mathbb P$ says how big a share of the mornings that region is.",
  cap="Ω is the box of all possible mornings and ω one morning in it. The region A (“late”) is an event in ℱ, so its complement Aᶜ is too, and ℙ(A) is a number between 0 and 1."),
30102: dict(d=d2, kind="DEFINITION",
  stmt=r"<b>Kolmogorov's axioms.</b> A function $\mathbb P:\mathcal F\to\mathbb R$ on a $\sigma$-algebra $\mathcal F$ of $\Omega$ is a probability measure if (i) $\mathbb P(A)\ge0$ for all $A\in\mathcal F$; (ii) $\mathbb P(\Omega)=1$; (iii) for pairwise disjoint $A_1,A_2,\ldots\in\mathcal F$, $\mathbb P\!\left(\bigcup_{i}A_i\right)=\sum_i\mathbb P(A_i)$ (Ross 2.3; Grimmett 1.3).",
  hint="Which three rules keep “how likely” honest, even for infinitely many separate mornings?",
  bd=[r"<strong>$\mathbb P(A)\ge0$ = no negative chances.</strong> A morning question cannot be less likely than never.",
      r"<strong>$\mathbb P(\Omega)=1$ = something happens.</strong> Every morning is one of the possible mornings, so all of them together have total chance 1.",
      r"<strong>$\mathbb P(\bigcup A_i)=\sum\mathbb P(A_i)$ = separate cases add up.</strong> If the cases cannot happen on the same morning, the chance of “one of them” is the sum, even for infinitely many cases."],
  conn=r"<strong>Splitting the mornings into cases.</strong> “Late because of rain”, “late because of a breakdown”, “late because I overslept”: no morning is two of these at once, so their chances just add. The third rule says this still works with endlessly many cases.",
  cap="The disjoint events A₁, A₂, A₃ share no morning, so their chances add: ℙ(⋃Aᵢ) = ∑ℙ(Aᵢ). With ℙ(A) ≥ 0 and ℙ(Ω) = 1 these are all the rules."),
30103: dict(d=d3, kind="THEOREM",
  stmt=r"<b>Continuity of probability.</b> Let $(\Omega,\mathcal F,\mathbb P)$ be a probability space. If $A_1\subset A_2\subset\cdots$ in $\mathcal F$ and $A=\bigcup_nA_n$ (written $A_n\uparrow A$), then $\mathbb P(A)=\lim_n\mathbb P(A_n)$. If $B_1\supset B_2\supset\cdots$ in $\mathcal F$ and $B=\bigcap_nB_n$ ($B_n\downarrow B$), then $\mathbb P(B)=\lim_n\mathbb P(B_n)$ (Ross 2.6; Grimmett 1.3).",
  hint="If a sequence of questions keeps growing (or shrinking), does its chance settle at the chance of the limit?",
  bd=[r"<strong>$A_n\uparrow A$ = a growing question.</strong> “Late at least once in the first $n$ days” only grows with $n$; its limit $A$ is “late on some day”.",
      r"<strong>$B_n\downarrow B$ = a shrinking question.</strong> “On time on every one of the first $n$ days” only shrinks; its limit $B$ is “on time every day, forever”.",
      r"<strong>$\mathbb P(\cdot)=\lim\mathbb P(A_n)$ = no jump at infinity.</strong> The chance of the limit event is the limit of the chances, which is exactly what countable additivity buys."],
  conn=r"<strong>Checking more and more days.</strong> The question “have I been late yet?” can only turn from no to yes as days pass. Its chance creeps up, and what it creeps up to is the chance of “late some day”.",
  cap="Nested events: the shrinking family Bₙ ↓ B and the growing family Aₙ ↑ A. The chance ℙ(Aₙ) moves smoothly to ℙ(A), with no jump at the limit."),
30104: dict(d=d4, kind="THEOREM",
  stmt=r"<b>Boole's inequality (countable subadditivity).</b> For any events $A_1,A_2,\ldots\in\mathcal F$, disjoint or not, $\mathbb P\!\left(\bigcup_{i=1}^\infty A_i\right)\le\sum_{i=1}^\infty\mathbb P(A_i)$. Truncating inclusion-exclusion gives the Bonferroni bounds, e.g. $\mathbb P(A\cup B)=\mathbb P(A)+\mathbb P(B)-\mathbb P(A\cap B)$ (Ross 2.4; Grimmett 1.3).",
  hint="When the causes of lateness overlap, is the chance of “any of them” above or below the sum of their chances?",
  bd=[r"<strong>$\sum\mathbb P(A_i)$ = adding every cause's chance separately.</strong> A morning with two causes at once is counted twice.",
      r"<strong>$\mathbb P(\bigcup A_i)$ = the true chance that at least one cause hits.</strong> Each morning counts once, however many causes it has.",
      r"<strong>$\le$ = the sum never undercounts.</strong> No independence or disjointness is assumed, so it is a safe ceiling for any set of events."],
  conn=r"<strong>A safe ceiling on being late.</strong> Rain 10%, a breakdown 5%, a strike 3%: the chance that something goes wrong is at most 18%. It is less if bad days overlap, because the overlap is counted twice in the sum.",
  cap="Three overlapping causes of lateness A₁, A₂, A₃. The chance of the union ℙ(⋃Aᵢ) is at most the sum ∑ℙ(Aᵢ), because the overlaps are counted twice in the sum."),
30105: dict(d=d5, kind="THEOREM",
  stmt=r"<b>Inclusion–exclusion.</b> For events $A_1,\ldots,A_n$, $\mathbb P(\bigcup_iA_i)=\sum_{k=1}^n(-1)^{k-1}S_k$, where $S_k=\sum_{i_1<\cdots<i_k}\mathbb P(A_{i_1}\cap\cdots\cap A_{i_k})$. Partial sums alternate as upper and lower (Bonferroni) bounds (Ross 2.4; Grimmett 1.3).",
  hint="How do you correct the sum of single chances so every morning is counted exactly once?",
  bd=[r"<strong>$\sum\mathbb P(A_i)$ = add every event.</strong> Mornings in two events are counted twice.",
      r"<strong>$-\sum_{i<j}\mathbb P(A_i\cap A_j)$ = subtract the pairs.</strong> Now mornings in three events are counted zero times.",
      r"<strong>$(-1)^{n-1}\mathbb P(\bigcap A_i)$ = alternate to the end.</strong> Add the triples back, subtract the quadruples, until each morning counts once."],
  conn=r"<strong>Counting each late morning once.</strong> Mornings with two causes were counted twice, so subtract them; the rare triple-cause mornings were then removed once too often, so add them back.",
  cap="Three overlapping events: add the singles ∑ℙ(Aᵢ), subtract the pairs ℙ(Aᵢ∩Aⱼ), add back the triple. The shaded centre is the triple overlap, with sign (−1)ⁿ⁻¹."),
30106: dict(d=d6, kind="WORKED EXAMPLE",
  stmt=r"<b>Never tails.</b> A fair coin is tossed infinitely often. Let $B_n=\{\text{first }n\text{ tosses are heads}\}$; then $B_n\downarrow B=\{\text{all tosses heads}\}$. By continuity from above, $\mathbb P(B)=\lim_n\mathbb P(B_n)=\lim_n2^{-n}=0$. The event $B$ is nonempty (it contains $HHH\cdots$) yet has probability $0$.",
  hint="If every day the bus is on time with chance ½, what is the chance it is on time every single day forever?",
  bd=[r"<strong>$B_n$ = on time for the first $n$ days.</strong> Each extra day can only remove mornings, so the events shrink: $B_{n+1}\subset B_n$.",
      r"<strong>$\mathbb P(B_n)=(1/2)^n$ = a half for each further day.</strong> The days are independent, so the chances multiply.",
      r"<strong>$\lim(1/2)^n=0$ = the limit event has chance 0.</strong> By continuity from above, “on time forever” has probability 0, though that morning-sequence still exists in $\Omega$."],
  conn=r"<strong>A perfect streak that never ends.</strong> Each extra on-time day halves your chances. After a year the streak is astronomically unlikely, and “on time forever” has chance exactly 0, yet it is not impossible.",
  cap="The chance ℙ(Bₙ) = (1/2)ⁿ of being on time n days in a row falls to the limit 0, so ℙ(B) = 0 for “on time every day”, a possible but probability-zero morning-sequence."),
}

STORY = {
30101: dict(s="STORY 1 · STEP 1 · THE MORNINGS", b="Everything starts by fixing <b>all possible mornings</b> Ω, the questions ℱ we may ask about them, and a chance ℙ for each question.", f=[], n=[["30102", "the rules ℙ must obey"], ["30201", "chances once we know part of the morning"]]),
30102: dict(s="STORY 1 · STEP 2 · THE RULES", b="Three rules keep the chances consistent: no negatives, total 1, and <b>separate cases add up</b>, even infinitely many.", f=[["30101", "the triple (Ω, ℱ, ℙ)"]], n=[["30103", "limits of growing events"], ["30104", "bounding overlapping events"]]),
30103: dict(s="STORY 1 · STEP 3 · LIMITS", b="Because separate cases add up for infinitely many, the chance of a <b>growing or shrinking</b> family of events passes to its limit.", f=[["30102", "countable additivity"]], n=[["30106", "a limit that gives 0"], ["31601", "limsup of events and Borel–Cantelli"]]),
30104: dict(s="STORY 1 · STEP 4 · A SAFE CEILING", b="When events overlap, the sum of their chances is a <b>ceiling</b> for the chance that any of them happens.", f=[["30102", "adding disjoint cases"]], n=[["30105", "the exact count"], ["31602", "first Borel–Cantelli"]]),
30105: dict(s="STORY 1 · STEP 5 · THE EXACT COUNT", b="Adding, subtracting and adding back overlaps gives the <b>exact</b> chance that at least one event happens.", f=[["30104", "the ceiling it sharpens"]], n=[["30202", "overlaps as chained conditionals"]]),
30106: dict(s="STORY 1 · STEP 6 · A PROBABILITY-ZERO MORNING", b="Continuity from above turns “on time every day” into a limit of shrinking events and gives probability 0, <b>without being impossible</b>.", f=[["30103", "continuity from above"]], n=[["31702", "pathwise certainty in the strong law"]]),
}

FIX = build(CARDS)
