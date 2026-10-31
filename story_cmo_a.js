/* CMO big-picture story, topics 4-7 (line search -> gradient descent -> Newton -> conjugate gradient).
   Keyed by card id. s = step tag, b = one-sentence "where we are", f = cards before [id, why], n = cards after [id, why].
   Arc source: "The Evolution of CG" slides (steepest descent zig-zags -> Q-orthogonality -> expanding subspace
   -> CG recurrence -> Krylov / n-step landing -> Polak-Ribiere restarts). */
window.STORY_DATA = Object.assign(window.STORY_DATA || {}, {
  /* ---- 4 · Line search: how far to fly ---- */
  "401": { s: "STORY 4 · HOW FAR TO FLY", b: "Topic 2 told us what the bottom looks like; now we need a flying rule. Every method is <b>pick a heading $d$, then pick a leg length $\\alpha$</b>. This card sets up that vocabulary.",
    f: [["202", "slope gauge reads 0 at the bottom: our target"]], n: [["402", "easiest terrain: exact leg"], ["403", "real terrain: good-enough leg"]] },
  "402": { s: "STORY 4 · HOW FAR TO FLY", b: "On a quadratic valley the best leg length has a closed formula. It is the benchmark that every approximate rule imitates.",
    f: [["401", "$\\alpha$ was the unknown"], ["303", "constant curvature $Q$"]], n: [["403", "no formula on real terrain: settle for 'enough'"], ["508", "this exact leg is what causes the zig-zag"]] },
  "403": { s: "STORY 4 · HOW FAR TO FLY", b: "Real terrain gives no formula, so demand only that the leg <b>earns enough altitude</b>. This is rule 1 of the two Wolfe rules.",
    f: [["402", "exact leg, replaced by 'enough'"]], n: [["404", "rule 2 stops legs that are too short"]] },
  "404": { s: "STORY 4 · HOW FAR TO FLY", b: "Rule 1 alone accepts tiny legs. The curvature condition is rule 2: do not stop while the slope is still steep. Together they are the Wolfe pair.",
    f: [["403", "rule 1 (Armijo)"]], n: [["405", "the pair guarantees the radar reaches 0"], ["805", "BFGS needs Wolfe to stay healthy"]] },
  "405": { s: "STORY 4 · HOW FAR TO FLY", b: "Zoutendijk: if every leg obeys Wolfe and the nose never turns 90° away from downhill, the radar reading must go to zero. This is the safety net under every later method.",
    f: [["404", "Wolfe legs"]], n: [["406", "how to find such a leg cheaply"], ["501", "first method that uses this net"]] },
  "406": { s: "STORY 4 · HOW FAR TO FLY", b: "The cheap implementation: start long and shrink until Armijo holds. Every method in topics 5-8 calls this routine.",
    f: [["403", "the rule it checks"], ["405", "why it is safe"]], n: [["501", "steepest descent uses it"], ["604", "damped Newton uses it"]] },

  /* ---- 5 · Gradient descent: which way to point ---- */
  "501": { s: "STORY 5 · THE ORIGINAL PROBLEM", b: "Point straight downhill. Simple, but it <b>ignores the valley's curvature $Q$</b>: crosswinds push the plane off course. Topics 5-7 are the repair story.",
    f: [["406", "legs come from line search"], ["202", "stops when $\\nabla f=0$"]], n: [["508", "the exact-leg zig-zag"], ["505", "why a thin canyon is worst"]] },
  "508": { s: "STORY 5 · THE ORIGINAL PROBLEM", b: "With exact legs, consecutive headings are perpendicular, so the path bounces from wall to wall. This is the zig-zag every later card tries to remove.",
    f: [["501", "the rule that zig-zags"], ["402", "the exact leg length"]], n: [["505", "how bad it gets with $\\kappa$"], ["701", "cure: Q-orthogonal, not perpendicular"]] },
  "502": { s: "STORY 5 · HOW SLOW IS IT", b: "A first guarantee: with legs of $1/L$ on smooth convex terrain the gap shrinks like $1/k$. Safe, but slow.",
    f: [["302", "tangent plane gives the descent lemma"], ["501", "the method being timed"]], n: [["503", "strong convexity upgrades 1/k to geometric"]] },
  "503": { s: "STORY 5 · HOW SLOW IS IT", b: "With a bowl floor under the terrain, every leg cuts the gap by a fixed fraction: linear convergence, with a ratio that depends on conditioning.",
    f: [["502", "sublinear rate"], ["304", "strong convexity gives the floor"]], n: [["504", "the exact ratio on quadratics"]] },
  "504": { s: "STORY 5 · HOW SLOW IS IT", b: "Kantorovich gives the exact worst-case shrink per leg on a quadratic valley. It depends only on the ratio of the longest to shortest valley axis.",
    f: [["503", "linear rate"], ["508", "the zig-zag it measures"]], n: [["505", "that ratio is $\\kappa$, the culprit"]] },
  "505": { s: "STORY 5 · WHY IT ZIG-ZAGS", b: "Big $\\kappa$ means a long thin canyon, and crosswinds force near-infinite zig-zags. Four repairs follow: smarter legs, momentum, conjugate headings, curvature itself.",
    f: [["504", "the rate bound"]], n: [["506", "smarter leg sizes"], ["507", "momentum"], ["701", "conjugate headings"], ["601", "Newton: use the curvature"]] },
  "506": { s: "STORY 5 · REPAIR 1", b: "Size the next leg from the last two footprints. No line search, and a crude curvature reading enters through the leg length.",
    f: [["505", "zig-zag problem"], ["403", "line search it replaces"]], n: [["507", "also remember the heading"], ["801", "same footprint trick, scaled up to a matrix"]] },
  "507": { s: "STORY 5 · REPAIR 2", b: "A heavy plane keeps rolling down the canyon instead of bouncing. Momentum is a rough memory of the last heading.",
    f: [["506", "leg-size repair"], ["505", "bouncing problem"]], n: [["703", "CG is momentum with the best possible weights"], ["701", "the exact version of this idea"]] },

  /* ---- 6 · Newton: read the curvature directly ---- */
  "601": { s: "STORY 6 · USE THE CURVATURE", b: "Instead of fixing a bad heading, fit a parabola with the Hessian and jump to its bottom. On a quadratic valley this crosses it in one leg.",
    f: [["201", "second-order Taylor model"], ["505", "zig-zag it avoids"]], n: [["602", "how fast near the end"], ["603", "when the parabola lies"]] },
  "602": { s: "STORY 6 · USE THE CURVATURE", b: "Close to the bottom the error is squared each leg: quadratic convergence. The reward for paying for curvature.",
    f: [["601", "the Newton leg"]], n: [["603", "but far away it can fail"]] },
  "603": { s: "STORY 6 · WHEN CURVATURE LIES", b: "If the terrain curves downward (saddle or hill) the parabola has no bottom, and Newton flies toward the wrong point.",
    f: [["602", "the good case"], ["203", "SONC: curvature must be PSD"]], n: [["604", "guard it with line search"], ["605", "or repair the curvature"]] },
  "604": { s: "STORY 6 · MAKE IT SAFE", b: "Take the full Newton leg when it earns enough altitude, otherwise shorten it. The same backtracking routine as topic 4.",
    f: [["603", "failure to guard against"], ["406", "backtracking routine"]], n: [["605", "still fails if $H$ is not positive definite"]] },
  "605": { s: "STORY 6 · MAKE IT SAFE", b: "Shift the curvature by $\\tau I$ until it is positive definite, so the model is always a bowl. A blend between Newton and steepest descent.",
    f: [["604", "damped Newton"], ["205", "eigenvalue signs of $H$"]], n: [["606", "the banana canyon test"], ["701", "avoid forming $H$ at all: CG"], ["801", "or learn $H$ from flight logs: quasi-Newton"]] },
  "606": { s: "STORY 6 · WORKED BENCHMARK", b: "Rosenbrock's banana canyon: Newton crosses it in a leg or two, while gradient descent zig-zags for thousands. But Newton paid for an $n\\times n$ Hessian.",
    f: [["605", "the safe Newton"], ["505", "the zig-zag it beats"]], n: [["701", "cheaper way to beat the zig-zag"], ["801", "or cheaper curvature"]] },

  /* ---- 7 · Conjugate gradient (follows the big-picture slides) ---- */
  "701": { s: "STORY 7 · STEP 1 · FIX THE ZIG-ZAG", b: "Steepest descent zig-zags because perpendicular legs undo each other. Twist the headings by the valley's curvature $Q$ so they follow its natural axes.",
    f: [["508", "the zig-zag to fix"], ["601", "Newton fixes it, but costs $H$"]], n: [["702", "prove the twisted headings really work"]] },
  "702": { s: "STORY 7 · STEP 2 · PROVE IT WORKS", b: "Did Step 1 secure the airspace? Yes: after $k$ legs the slope is flat against <b>every</b> earlier heading, so the plane sits at the lowest point of the whole flight plane.",
    f: [["701", "the Q-conjugate headings"]], n: [["703", "now make it cheap to compute"]] },
  "703": { s: "STORY 7 · STEP 3 · BYPASS SLOW MATH", b: "Computing Q-angles from scratch is too heavy. Cheat: new heading = fresh downhill + a fraction $\\beta$ of the last heading, which is momentum with exactly the right weight.",
    f: [["702", "conjugacy to preserve"], ["507", "the momentum idea"]], n: [["704", "how many legs do we need?"]] },
  "704": { s: "STORY 7 · STEP 4 · GUARANTEE LANDING", b: "Each leg permanently kills one natural axis, so crosswinds run out: the plane lands in at most $n$ legs (fewer if curvature values repeat).",
    f: [["703", "the cheap recurrence"], ["702", "one dimension conquered per leg"]], n: [["705", "reality is not a perfect quadratic"]] },
  "705": { s: "STORY 7 · STEP 5 · SURVIVE REALITY", b: "On bumpy non-quadratic terrain, old momentum can turn toxic. Polak-Ribière adds a restart: if $\\beta$ goes negative, throw the memory away and head straight downhill.",
    f: [["704", "ideal quadratic case"], ["603", "terrain where curvature changes"]], n: [["706", "the clean 2-D flight"], ["801", "or learn curvature as you fly: BFGS"]] },
  "706": { s: "STORY 7 · FLIGHT COMPLETE", b: "Two legs, two natural axes, landed exactly: the whole CG story in one picture, from the zig-zag of steepest descent to the finish.",
    f: [["705", "the full algorithm"], ["508", "the zig-zag we started with"]], n: [["801", "next: learn the curvature instead of avoiding it"]] }
});
