"""Airplane drawings for CMO topics 05-07 (gradient descent, Newton, conjugate gradient)."""
import math
from air_lib import *
from dip_lib import E

D = {}
CX, CY = 150, 74

def quad_contours(Q, levels, sc, cx=CX, cy=CY, w=1.2):
    a, b, c = Q[0][0], Q[0][1], Q[1][1]
    tr, det = a + c, a * c - b * b
    l1 = tr / 2 + math.sqrt(max(tr * tr / 4 - det, 0)); l2 = tr - l1
    th = math.degrees(math.atan2(l1 - a, b)) if abs(b) > 1e-9 else (0.0 if a >= c else 90.0)   # angle of the l1 eigenvector (math y-up)
    out = []
    for lv in levels:
        out.append(E(cx, cy, math.sqrt(2 * lv / l1) * sc, math.sqrt(2 * lv / l2) * sc, -th, "none", w))
    return out

def mv(Q, x): return [Q[0][0] * x[0] + Q[0][1] * x[1], Q[1][0] * x[0] + Q[1][1] * x[1]]
def dotp(u, v): return u[0] * v[0] + u[1] * v[1]

def sd_path(Q, x0, n):
    x = x0[:]; pts = [x[:]]
    for _ in range(n):
        g = mv(Q, x); a = dotp(g, g) / dotp(g, mv(Q, g))
        x = [x[0] - a * g[0], x[1] - a * g[1]]; pts.append(x[:])
    return pts

def cg_path(Q, x0):
    x = x0[:]; g = mv(Q, x); d = [-g[0], -g[1]]; pts = [x[:]]
    for _ in range(2):
        a = -dotp(g, d) / dotp(d, mv(Q, d)); x = [x[0] + a * d[0], x[1] + a * d[1]]; pts.append(x[:])
        gn = mv(Q, x); beta = dotp(gn, gn) / max(dotp(g, g), 1e-12); d = [-gn[0] + beta * d[0], -gn[1] + beta * d[1]]; g = gn
    return pts[:3]

def S(p, sc, cx=CX, cy=CY): return (cx + sc * p[0], cy - sc * p[1])

# ------------------------------------------------------------------ topic 5
def d502(c):
    fx = lambda x: 124 - 96 / (1 + 0.16 * (x - 30) / 8)
    pts = [(30 + 8 * k, fx(30 + 8 * k)) for k in range(0, 25)]
    return svg(c, L(30, 124, 226, 124, 1.2, ar=True), L(30, 124, 30, 10, 1.2, ar=True), poly(pts, 2.6), plane(60, 22, 0, .6),
        N(206, 76, "f(xₖ) − f*", 8.5, "end"), N(206, 90, "≤ L‖x₀−x*‖² / 2k", 8.5, "end", "bold"), N(206, 138, "k (legs flown)", 8, "end"),
        N(40, 22, "huge drops", 8, "start") if False else "", N(150, 108, "last metres: many legs", 8.5, "middle"))
D[502] = (d502, "Descending with step 1/L: the first legs shed lots of altitude, the last metres above the valley floor take many legs, so the gap shrinks only like 1/k.")

def d503(c):
    parts = [L(14, 124, 226, 124, 1.2, ar=True)]
    for k in range(5):
        h = 90 * 0.62 ** k
        parts += [R(24 + k * 40, 124 - h, 26, h, "#f1f5f9", 1.6), N(37 + k * 40, 136, f"k={k}", 8, "middle")]
        if k < 4: parts.append(arrow(52 + k * 40, 124 - h + 6, 62 + k * 40, 124 - 90 * 0.62 ** (k + 1) - 4, 1.4)); parts.append(N(57 + k * 40, 124 - h - 4, "×ρ", 8, "middle", "bold")) if k < 3 else None
    parts += [plane(206, 40, 180, .6), N(200, 62, "ρ = 1 − μ/L", 8.5, "end", "bold"), N(200, 76, "gap × ρ per leg", 8.5, "end")]
    return svg(c, *parts)
D[503] = (d503, "Every leg removes the same fraction of the altitude still left above the valley floor: the gap is multiplied by ρ<1 each leg.")

def d504(c):
    sc = 8
    parts = quad_contours([[1, 0], [0, 6]], [8, 25, 55], sc, 150, 76)
    x0 = (-9, 2.2); s0 = S(x0, sc, 150, 76); g = (x0[0], 6 * x0[1]); n = math.hypot(*g); u = (-g[0] / n, -g[1] / n)
    nose = (s0[0] + 38 * u[0], s0[1] - 38 * u[1])
    parts += [plane(*s0, math.degrees(math.atan2(-(nose[1] - s0[1]) * -1, 1)) * 0 + math.degrees(math.atan2(nose[1] - s0[1], nose[0] - s0[0])), .75), arrow(*s0, *nose, 2.6), N(nose[0] + 4, nose[1] + 12, "−g", 9.5, "start", "bold"),
              arrow(s0[0] + 8, s0[1] - 4, 140, 74, 1.6, d="4 3"), N(86, 108, "valley axis", 8.5, "middle"), dot(150, 76, None, r=2.4), N(188, 20, "θ = misalignment", 8.5, "middle", "bold"),
              N(150, 140, "worst case: cos θ ≥ 2√κ/(κ+1)", 8.5, "middle", "bold")]
    return svg(c, *parts)
D[504] = (d504, "The nose (−g) is never perfectly aligned with the valley axis; Kantorovich bounds the worst misalignment, and with it the least altitude you must gain per leg.")

def d505(c):
    sc = 8
    parts = quad_contours([[1, 0], [0, 14]], [10, 35, 90], sc, 140, 74, 1.3)
    pts = sd_path([[1, 0], [0, 14]], [-12.5, 1.3], 6)
    sp = [S(p, sc, 140, 74) for p in pts]
    parts += [poly(sp, 2.4), plane(sp[0][0] - 4, sp[0][1] - 14, 0, .6), N(120, 18, "narrow canyon: large κ", 8.5, "middle", "bold"), N(120, 140, "bounces off the walls, crawls along the floor", 8.5)]
    return svg(c, *parts)
D[505] = (d505, "In a long thin canyon (large condition number κ) heading perpendicular to the contour slams you into the opposite wall; progress along the floor is slow.")

def d506(c):
    return svg(c, L(20, 126, 226, 126, 1.2, ar=True), fn(lambda x: 126 - 0.0042 * (x - 20) ** 2 * 1.0 if False else 126 - 60 * (1 - ((x - 126) / 106) ** 2) if x < 232 else 126, 20, 226, 40, 2.4),
        dot(70, 126, None, r=2.4), dot(118, 126, None, r=2.4), plane(70, 114, 0, .6), N(70, 138, "xₖ₋₁", 8.5), N(118, 138, "xₖ", 8.5),
        arrow(72, 120, 116, 120, 2.2), N(94, 112, "s", 10, "middle", "bold"), L(150, 124, 150, 98, 1.6), arrow(150, 124, 150, 98, 2), N(156, 112, "y", 10, "start", "bold"),
        N(150, 56, "α = sᵀs / sᵀy", 9, "start", "bold"), N(150, 68, "(no radar sweep)", 8, "start"), N(40, 22, "how far you flew (s)", 8.5, "start"), N(40, 34, "vs how the slope changed (y)", 8.5, "start"))
D[506] = (d506, "Size the next leg from the last two footprints: how far you flew (s) against how much the slope gauge changed (y).")

def d507(c):
    sc = 8
    Q = [[1, 0], [0, 12]]
    parts = quad_contours(Q, [6, 25, 80], sc, 150, 74, 1.2)
    sp = [S(p, sc, 150, 74) for p in sd_path(Q, [-12, 1.2], 6)]
    parts += [poly(sp, 1.4, "3 3"), poly([(38, 62), (70, 74), (100, 75), (126, 74.5), (150, 74)], 2.8), plane(38, 62, 20, .7), arrow(124, 74, 150, 74, 2.2) if False else "",
              N(120, 20, "plain: bounces (dashed)", 8.5, "middle"), N(120, 134, "momentum: keeps its heading, rolls down the floor", 8.5, "middle", "bold"), dot(150, 74, None, r=2.4)]
    return svg(c, *parts)
D[507] = (d507, "A heavy airliner keeps its heading through small gusts: the momentum path (solid) glides down the canyon floor while plain steepest descent (dashed) rattles between the walls.")

# ------------------------------------------------------------------ topic 6
def d601(c):
    f_ = lambda x: 56 + 54 * math.exp(-((x - 140) / 48) ** 2)
    xk = 122
    h = 1e-3; f0 = f_(xk); g0 = (f_(xk + h) - f_(xk - h)) / (2 * h); h0 = (f_(xk + 2) - 2 * f0 + f_(xk - 2)) / 4.0
    par = lambda x: f0 + g0 * (x - xk) + 0.5 * h0 * (x - xk) ** 2
    xv = xk - g0 / h0
    return svg(c, fn(f_, 20, 226, 60, 2.6), fn(par, xk - 46, xk + 66, 40, 1.6, "4 3"), plane(xk - 4, f0 - 14, 0, .6), dot(xk, f0, "xₖ", -6, 14, 9.5, "end", 2.6),
        dot(xv, par(xv), None, r=3), dash(xv, par(xv), xv, 124, 1.2, "2 2"), N(xv, 136, "xₖ₊₁", 9, "middle", "bold"), arrow(xk + 4, 124, xv - 4, 124, 2),
        N(120, 16, "fit a parabola, fly to its bottom", 8.5, "middle", "bold"))
D[601] = (d601, "The autopilot fits a parabola to the local terrain (slope and curvature gauges) and flies straight to the bottom of that model in one leg.")

def d602(c):
    parts = [L(14, 124, 226, 124, 1.2, ar=True)]
    for k, h in enumerate([8, 18, 38, 78]):
        parts += [R(30 + k * 48, 124 - h, 30, h, "#f1f5f9", 1.6), N(45 + k * 48, 136, f"leg {k+1}", 8, "middle")]
        parts.append(N(45 + k * 48, 124 - h - 4, f"{[1, 2, 4, 8][k]} digits", 8, "middle", "bold"))
    parts += [plane(40, 40, 0, .6), N(120, 18, "inside the final approach bubble", 8.5, "middle", "bold"), N(120, 30, "correct digits double each leg", 8.5)]
    return svg(c, *parts)
D[602] = (d602, "Inside the terminal approach bubble each leg squares the remaining error, so the number of correct digits roughly doubles every leg.")

def d603(c):
    f_ = lambda x: 100 - 66 * math.exp(-((x - 120) / 40) ** 2) + 0.18 * (x - 120)
    xk = 92
    return svg(c, fn(f_, 20, 226, 60, 2.6), fn(lambda x: 24 + 0.012 * (x - 126) ** 2 + 0.0, 62, 190, 30, 1.4, "4 3"),
        plane(xk - 4, f_(xk) - 16, 0, .6), dot(126, 24, None, r=3), arrow(xk + 6, f_(xk) - 18, 120, 28, 2.2), N(150, 14, "model peak ✗", 8.5, "start", "bold"),
        N(196, 74, "flies over", 8.5, "start"), N(196, 86, "the summit", 8.5, "start"), N(120, 138, "negative curvature: parabola opens downward", 8.5, "middle", "bold"))
D[603] = (d603, "In fog near a hilltop or saddle the parabola model opens downward: the autopilot flies to the model's peak, straight over the summit.")

def d604(c):
    xs = [24, 46, 74, 110, 150, 196]
    f_ = lambda x: 26 + 98 * (1 - math.exp(-(x - 24) / 50))
    parts = [L(20, 134, 226, 134, 1.2, ar=True), fn(f_, 24, 226, 40, 2.0, "4 3")]
    for i, x in enumerate(xs):
        parts.append(dot(x, f_(x), None, r=2.6))
        if i < len(xs) - 1: parts.append(arrow(x + 2, f_(x) + 6, xs[i + 1] - 2, f_(xs[i + 1]) - 2, 1.8))
    parts += [N(54, 62, "α<1", 8.5, "middle", "bold"), N(176, 110, "α=1", 8.5, "middle", "bold"), plane(30, 16, 0, .55), N(120, 144, "short cautious legs → full unit steps", 8.5, "middle", "bold")]
    return svg(c, *parts)
D[604] = (d604, "Far from the field fly short, cautious legs (backtracking, α<1); on the final approach fly the full unit step α=1.")

def d605(c):
    return svg(c, fn(lambda x: 30 + 0.0045 * (x - 120) ** 2, 40, 200, 40, 1.6, "4 3"), fn(lambda x: 120 - 0.0125 * (x - 120) ** 2, 40, 200, 40, 2.6),
        plane(120, 92, 0, .6), N(120, 12, "H not positive definite: the model is a hill (dashed)", 8, "middle"), N(120, 134, "add τI: the model becomes a bowl", 8.5, "middle", "bold"),
        N(120, 144, "τ→0 Newton · τ→∞ short gradient leg", 8))
D[605] = (d605, "If the curvature gauge is not all positive the model is a hill (dashed). Adding the stabiliser τI stiffens it into a bowl (solid) the autopilot can safely fly to.")

def d606(c):
    par = lambda x: 120 - 0.0105 * (x - 120) ** 2
    parts = [fn(lambda x: par(x) - 9, 28, 212, 40, 1.6), fn(lambda x: par(x) + 9, 28, 212, 40, 1.6), fn(par, 28, 212, 40, 1.0, "3 3")]
    sw = []
    x = 34
    while x < 118:
        sw.append((x, par(x) - 6)); x += 6; sw.append((x, par(x) + 6))
    parts += [poly(sw, 1.2, "2 2"), poly([(34, par(34)), (84, par(84)), (122, par(122))], 3), dot(122, par(122), None, r=3), plane(40, par(34) - 14, 20, .6),
              N(236, 50, "Newton: 2–3 legs", 8.5, "end", "bold"), N(236, 62, "(a bridge)", 8, "end"), N(236, 82, "gradient descent:", 8.5, "end"), N(236, 94, "many switchbacks", 8.5, "end"), N(120, 142, "Rosenbrock banana canyon", 8.5, "middle")]
    return svg(c, *parts)
D[606] = (d606, "Newton flies a bridge across the banana canyon in a few legs; gradient descent hikes down hundreds of switchbacks along the walls.")

# ------------------------------------------------------------------ topic 7
Q7 = [[3, 1], [1, 2]]
X0 = [-6.0, 2.5]

def d701(c):
    sc = 9
    parts = quad_contours(Q7, [6, 18, 45], sc, 150, 74)
    sd = [S(p, sc, 150, 74) for p in sd_path(Q7, X0, 4)]
    cg = [S(p, sc, 150, 74) for p in cg_path(Q7, X0)]
    parts += [poly(sd, 1.4, "3 3"), poly(cg, 2.8), plane(cg[0][0] - 6, cg[0][1] - 14, 0, .65), dot(*cg[1], "d₀ ends", 4, -6, 8, "start", 2.4),
              N(120, 16, "perpendicular legs (dashed) zig-zag", 8.5, "middle"), N(120, 138, "Q-conjugate legs (solid) follow the natural axes", 8.5, "middle", "bold")]
    return svg(c, *parts)
D[701] = (d701, "In a skewed valley perpendicular legs (dashed) undo each other; Q-conjugate headings (solid) follow the valley's natural axes and reach the bottom in two legs.")

def d702(c):
    sc = 9
    parts = [PG("20,128 220,128 232,20 32,20", "#eef0f4", 0.8)] + quad_contours(Q7, [6, 18, 45], sc, 150, 74)
    cg = [S(p, sc, 150, 74) for p in cg_path(Q7, X0)]
    parts += [L(cg[0][0] - 40, cg[0][1] + 18, cg[1][0] + 60, cg[1][1] - 26, 1.2, d="5 3"), poly(cg, 2.8), plane(cg[0][0] - 6, cg[0][1] - 14, 0, .65), dot(*cg[2], "x₂", 5, 12, 9, "start", 3),
              N(120, 136, "lowest point of the whole flight plane span{d₀,d₁}", 8.5, "middle", "bold"), N(40, 34, "span{d₀,d₁}", 8.5, "start")]
    return svg(c, *parts)
D[702] = (d702, "After k legs you sit at the lowest point of the whole flight plane spanned by your headings, not just along the last line.")

def d703(c):
    ox, oy = 62, 96
    return svg(c, arrow(ox, oy, ox + 60, oy - 6, 2, d="4 3"), N(ox + 62, oy - 8, "β dₖ", 9, "start"), arrow(ox, oy, ox + 8, oy - 54, 2, d="4 3"), N(ox + 2, oy - 58, "−gₖ₊₁", 9, "middle"),
        arrow(ox, oy, ox + 68, oy - 60, 3), N(ox + 70, oy - 60, "dₖ₊₁", 10, "start", "bold"), dash(ox + 60, oy - 6, ox + 68, oy - 60, 1.2, "2 2"), dash(ox + 8, oy - 54, ox + 68, oy - 60, 1.2, "2 2"),
        plane(ox, oy, -40, .7), N(176, 108, "dₖ₊₁ = −gₖ₊₁ + βₖ dₖ", 8.5, "end", "bold"), N(236, 122, "β = ‖gₖ₊₁‖² / ‖gₖ‖²", 8.5, "end"), N(120, 20, "fresh downhill + a fraction of the last heading", 8.5, "middle", "bold") if False else N(120, 20, "fresh downhill + part of the last heading", 8.5, "middle", "bold"))
D[703] = (d703, "The new heading is fresh downhill (−g) plus a fraction β of the previous heading: you keep some momentum instead of restarting.")

def d704(c):
    parts = [L(14, 124, 226, 124, 1.2, ar=True)]
    for i, (h1, h2) in enumerate([(70, 40), (0, 40), (0, 0)]):
        x = 30 + i * 70
        parts += [R(x, 124 - max(h1, 1), 18, max(h1, 1), "#c9ced8", 1.4), R(x + 22, 124 - max(h2, 1), 18, max(h2, 1), "#f1f5f9", 1.4), N(x + 20, 136, f"after leg {i}", 8, "middle")]
    parts += [N(120, 18, "each leg kills one more curvature axis", 8.5, "middle", "bold"), N(120, 30, "n axes → at most n legs", 8.5), plane(204, 62, 0, .6)]
    return svg(c, *parts)
D[704] = (d704, "Each conjugate leg removes the error along one more natural axis (dark bar, light bar), so after n legs the error is zero: finite termination.")

def d705(c):
    return svg(c, circ(60, 62, 30, "#f1f5f9", 1.8), L(60, 62, 76, 40, 3), arrow(60, 62, 76, 40, 3), N(60, 108, "corrupted heading", 8.5, "middle"), N(60, 120, "(wrong direction)", 8),
        circ(176, 62, 30, "#f1f5f9", 1.8), arrow(176, 62, 176, 34, 3), N(176, 108, "restart: d = −g", 8.5, "middle", "bold"), N(176, 120, "(straight downhill)", 8),
        arrow(98, 60, 138, 60, 2.2), N(118, 52, "reset", 9, "middle", "bold"), plane(60, 24, 0, .55), plane(176, 24, 0, .55))
D[705] = (d705, "After a magnetic deposit the compass heading is corrupted; restart resets the heading to straight downhill (−g) like re-zeroing the compass.")

def d706(c):
    sc = 9
    parts = quad_contours(Q7, [6, 18, 45], sc, 150, 74)
    cg = [S(p, sc, 150, 74) for p in cg_path(Q7, X0)]
    parts += [poly(cg, 3), plane(cg[0][0] - 6, cg[0][1] - 14, 0, .65), dot(*cg[0], "x₀", -6, 12, 9, "end", 2.8), dot(*cg[1], "x₁", 6, -6, 9, "start", 2.8), dot(*cg[2], "x*", 6, 12, 9.5, "start", 3.2),
              N(120, 18, "2D: exactly two legs", 8.5, "middle", "bold"), N(120, 138, "leg 1 kills the error along d₀; leg 2 kills the rest", 8.5, "middle")]
    return svg(c, *parts)
D[706] = (d706, "In 2D conjugate gradient lands on the optimum in exactly two legs: the first removes the error along d₀, the second removes the rest.")

FIX = {cid: {"drawingSvg": fnc(cid), "drawingCaption": cap} for cid, (fnc, cap) in D.items()}
