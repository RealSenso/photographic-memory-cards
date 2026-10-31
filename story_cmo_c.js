/* CMO big-picture story, topics 1-3 (the foundations).
   Arc: 1 does a lowest point exist? -> 2 how do the gauges recognise it? -> 3 when is it the global one?
   -> then the algorithms of topics 4-8 hunt for it, and the CG story of topic 7 is the high point. */
window.STORY_DATA = Object.assign(window.STORY_DATA || {}, {
  /* ---- 1 · Does a lowest point exist? ---- */
  "101": { s: "STORY 1 · DOES A BOTTOM EXIST?", b: "Before searching for the lowest point we must know the airfield can hold one. A <b>closed and bounded</b> airfield (fence included, finite size) is the first ingredient.",
    f: [["1906", "end of the course: every method assumes this"]], n: [["102", "the terrain must not have cliff edges"], ["103", "the two ingredients together"]] },
  "102": { s: "STORY 1 · DOES A BOTTOM EXIST?", b: "The terrain's side of the bargain: no sudden upward cliffs that hide the lowest altitude. Lower semicontinuity keeps the altimeter honest at edges.",
    f: [["101", "the airfield"]], n: [["103", "airfield + terrain = Weierstrass"]] },
  "103": { s: "STORY 1 · DOES A BOTTOM EXIST?", b: "Weierstrass: a closed, bounded airfield and a terrain without cliffs guarantee a lowest point the pilot can actually reach.",
    f: [["101", "compact airfield"], ["102", "no cliffs"]], n: [["104", "airfield not bounded?"], ["202", "now: how to recognise the bottom"]] },
  "104": { s: "STORY 1 · DOES A BOTTOM EXIST?", b: "If the airfield is the whole plane, coercivity (the ground rises to infinity) lets us fence it in: search only the sublevel set.",
    f: [["103", "needs a bounded airfield"]], n: [["105", "the shape that makes it easy"], ["106", "worked proof"]] },
  "105": { s: "STORY 1 · DOES A BOTTOM EXIST?", b: "The epigraph is everything on or above the terrain. Convex terrain means a convex epigraph, the picture behind topic 3.",
    f: [["104", "sublevel sets"]], n: [["106", "practise the existence proof"], ["301", "convexity in full"]] },
  "106": { s: "STORY 1 · DOES A BOTTOM EXIST?", b: "Worked proof: coercive plus continuous gives a global minimiser on the whole plane. Foundation complete: the bottom exists.",
    f: [["104", "coercivity"]], n: [["201", "next: instruments that find it"]] },

  /* ---- 2 · Recognising the bottom with gauges ---- */
  "201": { s: "STORY 2 · RECOGNISE THE BOTTOM", b: "The bottom exists; how do we recognise it from the cockpit? Read three gauges near your position: altitude, slope and curvature. That is the Taylor model.",
    f: [["106", "a bottom exists"]], n: [["202", "slope gauge"], ["203", "curvature gauge"]] },
  "202": { s: "STORY 2 · RECOGNISE THE BOTTOM", b: "At a lowest point the slope gauge must read zero. First test, and the stopping rule every method of topics 4-8 uses.",
    f: [["201", "Taylor"]], n: [["203", "second gauge"], ["401", "line search hunts for it"], ["501", "steepest descent hunts for it"]] },
  "203": { s: "STORY 2 · RECOGNISE THE BOTTOM", b: "At a lowest point the curvature gauge must say 'bowl-shaped or flat' in every direction (PSD). A necessary test only.",
    f: [["202", "slope test"]], n: [["204", "the sufficient version"], ["603", "Newton fails when this is violated"]] },
  "204": { s: "STORY 2 · RECOGNISE THE BOTTOM", b: "Slope zero plus strictly bowl-shaped curvature guarantees a strict local minimum: necessary conditions upgraded to a guarantee.",
    f: [["203", "necessary test"]], n: [["205", "all critical points sorted"]] },
  "205": { s: "STORY 2 · RECOGNISE THE BOTTOM", b: "Eigenvalue signs of the Hessian sort every critical point: all positive is a bowl, mixed is a saddle, all negative is a hilltop.",
    f: [["204", "sufficient test"]], n: [["206", "a real example"], ["505", "κ is the ratio of these eigenvalues"]] },
  "206": { s: "STORY 2 · RECOGNISE THE BOTTOM", b: "Rosenbrock: the gauges say $(1,1)$ is a strict minimum even in a bent canyon. The same banana canyon returns as the test for Newton and CG.",
    f: [["205", "classification"]], n: [["301", "local vs global: convexity"], ["606", "Newton on this canyon"]] },

  /* ---- 3 · Local or global: convexity ---- */
  "301": { s: "STORY 3 · LOCAL OR GLOBAL?", b: "The gauges only see locally. If the terrain is convex (the string between two points lies above it), a local bottom is automatically the global one.",
    f: [["206", "local tests"], ["105", "the epigraph picture"]], n: [["302", "tangent plane form"], ["303", "curvature form"]] },
  "302": { s: "STORY 3 · LOCAL OR GLOBAL?", b: "The tangent plane never goes above a convex terrain. This one inequality powers the convergence proofs of topic 5.",
    f: [["301", "secant form"]], n: [["303", "the Hessian test"], ["502", "used to prove the 1/k rate"]] },
  "303": { s: "STORY 3 · LOCAL OR GLOBAL?", b: "Convexity is the same as the Hessian being PSD everywhere: the seat is always pressed up. Easy to test in practice.",
    f: [["302", "gradient form"], ["203", "SONC at a point"]], n: [["304", "stronger: a guaranteed bowl"]] },
  "304": { s: "STORY 3 · LOCAL OR GLOBAL?", b: "Strong convexity guarantees a quadratic bowl under the terrain. It is what turns slow $1/k$ descent into geometric descent.",
    f: [["303", "convex"]], n: [["305", "even weaker works"], ["503", "linear convergence of GD"]] },
  "305": { s: "STORY 3 · LOCAL OR GLOBAL?", b: "PL: the slope is always large when you are high above the floor. Enough for linear convergence without convexity.",
    f: [["304", "strong convexity"]], n: [["306", "separate the levels"]] },
  "306": { s: "STORY 3 · LOCAL OR GLOBAL?", b: "Convex, strictly convex, strongly convex: three nested guarantees. The foundation ends here; the hunt begins with how far to fly.",
    f: [["305", "weakest"], ["304", "strongest"]], n: [["401", "next: line search and the methods that use these guarantees"]] }
});
