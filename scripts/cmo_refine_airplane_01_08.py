"""One running airplane analogy for CMO topics 01-08 (concept study only, no assignment code).
Pilot flies in fog: f = altitude (lower is better), gradient = slope gauge, Hessian = curvature gauge,
step alpha = how far you fly before checking the radar again."""
import math
from air_lib import *
from dip_lib import E

A = "<strong>The airplane analogy.</strong> "

# ---------------------------------------------------------------- drawings for the rewritten steepest-descent cards
def d501(c):
    cx, cy = 150, 72
    parts = [E(cx, cy, r * 2, r, 0, "none", 1.3) for r in (14, 28, 42)]
    x0 = (92, 52)
    gx, gy = (x0[0] - cx) / 4.0, (x0[1] - cy) * 4.0      # gradient of  x^2/4... direction perpendicular to contour
    n = math.hypot(gx, gy); ux, uy = -gx / n, -gy / n
    parts += [plane(*x0, math.degrees(math.atan2(uy, ux)), .8), arrow(x0[0], x0[1], x0[0] + 44 * ux, x0[1] + 44 * uy, 2.8),
              N(x0[0] + 44 * ux + 6, x0[1] + 44 * uy + 10, "d = −∇f", 9, "start", "bold"),
              dash(x0[0], x0[1], x0[0] - 30 * ux, x0[1] - 30 * uy, 1.2, "3 3"), N(30, 24, "steepest UP", 8.5, "start"),
              dot(cx, cy, None, r=2.6), N(cx, cy + 14, "lowest", 8, "middle"),
              N(120, 140, "fly opposite to the steepest upward slope", 8.5, "middle", "bold")]
    return svg(c, *parts)

def d508(c):
    kappa = 4.0
    sc, cx, cy = 9.0, 150, 72
    x = [-8.0, 2.5]
    pts = [x[:]]
    for _ in range(6):
        g = [x[0], kappa * x[1]]
        a = (g[0] ** 2 + g[1] ** 2) / (g[0] ** 2 + kappa * g[1] ** 2)
        x = [x[0] - a * g[0], x[1] - a * g[1]]
        pts.append(x[:])
    sp = [(cx + sc * p[0], cy - sc * p[1]) for p in pts]
    parts = [E(cx, cy, math.sqrt(c0) * sc, math.sqrt(c0 / kappa) * sc, 0, "none", 1.1) for c0 in (4, 16, 40, 89)]
    parts += [poly(sp, 2.4), plane(sp[0][0], sp[0][1] - 12, 0, .65)]
    for p in sp[:5]:
        parts.append(dot(p[0], p[1], None, r=2.2))
    parts += [N(150, 14, "right angle at every turn", 8.5, "middle", "bold"), N(212, 112, "zig-zag", 8.5, "end"),
              N(120, 140, "α = −gᵀu / uᵀQu : slope over brakes", 8.5, "middle", "bold")]
    return svg(c, *parts)

# ---------------------------------------------------------------- steepest descent: card 501 rewritten + new card 508
FIX = {
    501: {
        "textbookImg": "", "textbookRef": "",
        "drawingSvg": d501(501),
        "drawingCaption": "Contour lines of the terrain: the pilot points the nose exactly opposite to the steepest upward slope, perpendicular to the contour.",
        "title": "Method of Steepest Descent: The Pilot's Rule",
        "coreTranslation": [
            "<strong>The pilot's rule:</strong> steepest descent points the plane exactly opposite to the steepest upward slope, $d_k=-\\nabla f(x_k)$. Update: $x_{k+1}=x_k-\\alpha_k\\nabla f(x_k)$, where $\\alpha_k$ is how far the plane flies before checking the radar again.",
            "<strong>Directional optimality:</strong> $-\\nabla f(x_k)$ is the direction that maximises the instantaneous rate of decrease per unit Euclidean step: $\\arg\\min_{\\|d\\|\\le1}\\nabla f(x_k)^\\top d=-\\dfrac{\\nabla f(x_k)}{\\|\\nabla f(x_k)\\|}$.",
            "<strong>Relative stop:</strong> the algorithm stops when the current slope is a tiny fraction of the starting cliff, $\\|g_k\\|\\le\\text{tol}\\cdot\\|g_0\\|$, rather than waiting for mathematically perfect flat ground."],
        "math": r"$$x_{k+1}=x_k-\alpha_k\nabla f(x_k),\quad d_k=-\nabla f(x_k),\quad \|g_k\|\le\text{tol}\cdot\|g_0\|$$",
        "personalConnection": A + "Fly with the nose pointing exactly opposite to the steepest upward slope under your wings. Pour a drop of water on a steep roof and gravity makes it trace the same line at every millisecond. You stop when the slope gauge reads only a tiny fraction of what it read at the start (the relative stop), not when it reads exactly zero.",
        "examTrap": "Steepest descent is only steepest locally in the EUCLIDEAN norm! Changing coordinates or using a Mahalanobis norm changes the gradient direction entirely (which is why Newton's method is superior).",
    },
}
NEW = [(501, {
    "id": 508, "category": "STEEPEST DESCENT", "highlighterClass": "highlight-amber",
    "title": "Exact Line Search, Step Size & the Zig-Zag",
    "drawingSvg": d508(508),
    "drawingCaption": "Under exact line search every turn is a right angle: the path zig-zags across the contour lines toward the lowest point.",
    "coreTranslation": [
        "<strong>Exact line search:</strong> the pilot flies perfectly straight until the altitude stops dropping and begins to curve back up.",
        "<strong>The zig-zag:</strong> because of this, consecutive search directions are perpendicular, $(x_{k+2}-x_{k+1})^\\top(x_{k+1}-x_k)=0$, so the path zig-zags across the contour lines.",
        "<strong>Step size for a quadratic:</strong> the exact distance to fly before hitting the bottom of the curve is $\\alpha=\\dfrac{-g^\\top u}{u^\\top Qu}$. The numerator is the downward momentum (how steep the slope is); the denominator is the brakes (how fast the terrain curves back up along that path)."],
    "math": r"$$\alpha_k=\frac{-g_k^\top u_k}{u_k^\top Q u_k},\qquad (x_{k+2}-x_{k+1})^\top(x_{k+1}-x_k)=0$$",
    "personalConnection": A + "You fly dead straight along your heading $u$ until the altimeter stops falling, and at that moment the new downhill is exactly 90 degrees to your old heading: that is the zig-zag. The slope gauge ($-g^\\top u$) says how hard you are diving; the curvature brakes ($u^\\top Qu$) say how soon the ground curves back up, so a steep dive on gently curving ground means a long leg.",
    "examTrap": "Perpendicular turns do NOT mean fast. In a long narrow valley (large condition number) the zig-zag wastes many legs. Also, the right-angle property holds only for an EXACT line search, not for Armijo/backtracking steps.",
})]

# ---------------------------------------------------------------- airplane connections for the rest of topics 01-08
_TXT = {
# topic 5 (gradient descent)
502: "Descending with step $1/L$: the first legs shed lots of altitude, but squeezing out the last few metres above the valley floor takes progressively more legs, so the gap shrinks only like $1/k$.",
503: "Each leg removes a fixed fraction of the altitude still left above the valley floor, like a glide path losing the same percentage every mile: error is multiplied by $\\rho\\lt1$ per leg, so the gap vanishes geometrically.",
504: "The worst-case guarantee: how badly can your nose ($-g$) be misaligned with the valley's long axis? Kantorovich bounds that misalignment, and with it the least altitude you must gain back per leg.",
505: "A narrow canyon: heading perpendicular to the contour sends you straight into the opposite canyon wall instead of down the stream. The longer and thinner the valley (large condition number $\\kappa$), the worse the zig-zag.",
506: "No radar sweeps: size your next leg from your last two footprints, how far you flew ($s$) compared with how much the slope gauge changed ($y$), so the stride matches the terrain.",
507: "A heavy airliner keeps its heading through small gusts, so it rattles less between the canyon walls and holds the line down the valley. Nesterov looks ahead along the heading before correcting.",
# topic 6 (Newton)
601: "The autopilot fits a parabola-shaped model of the terrain from the slope and curvature gauges and flies straight to the lowest point of that model in one leg, instead of inching along with the slope alone.",
602: "Far from the airfield the autopilot manoeuvres cautiously; once inside the terminal approach bubble each leg squares the remaining error, so the number of correct digits roughly doubles.",
603: "In fog near a hilltop or saddle the parabola model opens downward. The autopilot flies to the model's peak, straight over the summit, because pure Newton hunts any flat ground, not low ground.",
604: "Far from the field you shorten each leg after a backtracking check (small $\\alpha_k$); on the final approach you fly the full unit step $\\alpha=1$.",
605: "If the curvature gauge is not all positive, add a stabiliser $\\tau I$ to stiffen the terrain model into a bowl. A large $\\tau$ behaves like a short gradient leg, $\\tau\\to0$ is pure Newton.",
606: "Newton flies a bridge straight across the banana-shaped canyon in a few legs, while gradient descent hikes down hundreds of switchbacks to the riverbed and back up the other wall.",
# topic 7 (CG)
701: "Headings that are $Q$-conjugate follow the valley's own natural axes: pushing down along one heading does not undo what you gained along another, unlike plain perpendicular headings in a skewed valley.",
702: "After $k$ legs you sit at the lowest point of the entire flight plane spanned by your $k$ headings, not only along the last line, and later conjugate legs never spoil the altitude already won.",
703: "Instead of recalculating the whole voyage, trim the previous heading: the new heading is fresh downhill plus a fraction $\\beta_k=\\|g_{k+1}\\|^2/\\|g_k\\|^2$ of the previous heading, like keeping some momentum from the last leg.",
704: "In $n$ dimensions a quadratic valley has only $n$ natural axes: each conjugate leg kills one more, so you land after at most $n$ legs (only $m$ if there are just $m$ distinct curvature values).",
705: "When the terrain is not a perfect quadratic, Polak-Ribière headings can go bad. Reset the heading to straight downhill (a restart), like re-zeroing a compass after passing a magnetic deposit.",
706: "Two legs finish the job in 2D: the first removes the error along $d_0$, the second removes the rest along $d_1$, and the first leg is never spoiled by the second.",
# topic 8 (quasi-Newton)
801: "From the flight log: how far you flew ($s_k$) and how much the slope gauge changed ($y_k$) reveal the terrain's curvature along that path, so you learn it without surveying the whole valley.",
802: "A single rank-one correction to the curvature estimate: quick and light, but if the denominator is near zero the update can blow up and the estimate jams.",
803: "Two corrections to the curvature estimate: one matches the leg you just flew, the other cleans up so the estimate stays consistent.",
804: "BFGS is the autopilot that corrects its own gyro drift: each rank-two update keeps the curvature estimate positive definite and consistent with the flight log, so it is the standard choice.",
805: "Only trust a leg if the terrain curved upward along it ($s_k^\\top y_k\\gt0$), which a Wolfe line search guarantees. If the ground sagged, refuse to log that leg so the estimate stays safe.",
806: "Keep only the last $m$ legs of the flight log $(s,y)$ instead of a full curvature map: nearly the same guidance for a fraction of the memory.",
# topic 1
101: "A fenced airfield with a locked gate is compact: closed (its boundary belongs to it) and bounded (finite size). An endless runway is closed but unbounded, and an airfield with missing fence boards is bounded but not closed.",
102: "At a cliff edge the altimeter reports the lower of the two heights, so a plane approaching from above still lands on the true low point and never falls through an imaginary floor.",
103: "A continuous terrain over a fenced, finite airfield always has a lowest point the plane can actually touch down on, rather than tapering off toward infinity.",
104: "Mountain walls rise without limit in every direction around the airport, so the lowest altitude cannot be far away: the plane never has to search to infinity.",
105: "The sky above the terrain is the epigraph. If the terrain is convex then any straight flight path between two points in that sky stays in the sky.",
106: "Build the fence first: coercivity says the terrain outside a large enough fence is higher than your starting altitude, so searching inside the fence cannot miss the lowest point.",
# topic 2
201: "In fog the pilot has three instruments: the altimeter $f(x)$, the slope gauge $\\nabla f(x)$ and the curvature gauge $\\nabla^2f(x)$. Together they give a local model of the terrain around the plane.",
202: "At the lowest parking spot the slope gauge reads zero: in no direction does the plane start to descend.",
203: "The curvature gauge must never read negative at the lowest spot: if even one direction curved downward, the plane would roll off that way.",
204: "Every direction curves strictly upward, like the inside of a valley with steep sides, so the plane is trapped at a guaranteed strict local low point.",
205: "The Hessian's eigenvalues are the curvature along each natural axis: all positive is a valley bottom, all negative a hilltop, mixed is a mountain pass (low along the ridge, high across the trail).",
206: "Rosenbrock is a long curved banana canyon along $y=x^2$: the floor is nearly flat while the walls are steep, with condition number around 2500, so following the floor needs tiny careful legs.",
# topic 3
301: "A convex corridor: any two points can be joined by a straight flight path that stays inside. The straight path between two points on a convex terrain always flies above the terrain.",
302: "At any point the flat glide plane touching the terrain there lies beneath the terrain everywhere else: the slope gauge always underestimates the true altitude of a convex terrain.",
303: "At every point the seat is pressed up by the ground (never floats up): the terrain curves upward everywhere, which is the positive semidefinite Hessian.",
304: "Strong convexity means the terrain curves up at least like a bowl of fixed steepness $m$: leaving the bottom costs at least $\\tfrac m2\\|x-x^*\\|^2$ of altitude.",
305: "The higher you are above the lowest point, the steeper the slope under you, so the plane can never sit on a flat plateau far above the valley floor.",
306: "Convex allows level ramps (cruise flat forever); strictly convex has no level stretch but can flatten near the bottom ($x^4$); strongly convex is a true bowl everywhere.",
# topic 4
401: "Pick a heading $d_k$ that points downhill ($\\nabla f^\\top d_k\\lt0$) and decide how far $\\alpha_k$ to fly before checking the radar again.",
402: "Fly dead straight until the altitude stops dropping and starts rising: that is the very bottom of that straight track, found exactly for a quadratic.",
403: "Armijo asks each leg for a fair altitude drop in proportion to the distance flown and the slope: refuse a leg that burns lots of fuel for little drop.",
404: "Armijo stops you flying so far that you overshoot the valley; the curvature condition stops tiny hops by demanding that the slope has flattened enough after the leg.",
405: "As long as your heading is not turned sideways to the slope ($\\theta_k\\ne90^\\circ$), each leg keeps taking altitude and the slope gauge is driven to zero.",
406: "Plan a long leg, check the altitude drop; if it is too small, shorten the leg by half and check again until the drop is acceptable.",
}
for k, v in _TXT.items():
    FIX.setdefault(k, {})["personalConnection"] = A + v
