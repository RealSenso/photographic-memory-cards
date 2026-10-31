"""Valley/landscape cards (topics 05-07) redrawn as a tilted top view of the bowl so the legs are visible."""
from bowl_lib import *

D = {}

def d501(c):
    Q = [[1, 0], [0, 3]]; B = Bowl(Q, 128, 84, 20)
    x0 = x0_on_level(Q, 200, 7); g = mv(Q, x0); n = math.hypot(*g); u = [-g[0] / n, -g[1] / n]
    tip = [x0[0] + 1.5 * u[0], x0[1] + 1.5 * u[1]]; up = [x0[0] - 1.1 * u[0], x0[1] - 1.1 * u[1]]
    p0, pt, pu = B.pr(x0), B.pr(tip), B.pr(up)
    parts = B.rings() + [B.seg(x0, up, 1.3, "3 3"), B.seg(x0, tip, 2.8), arrow(*B.pr([tip[0] - .15 * u[0], tip[1] - .15 * u[1]]), *pt, 2.8),
        dot(*p0, None, r=3), plane(p0[0] - 4, p0[1] - 12, 0, .7), dot(*B.pr([0, 0]), None, r=2.6),
        N(pt[0] + 8, pt[1] + 12, "d = −∇f", 9, "start", "bold"), N(pu[0] - 4, pu[1] - 4, "steepest UP", 8.5, "end"),
        N(128, 140, "fly opposite to the steepest upward slope", 8.5, "middle", "bold")]
    return svg(c, *parts)
D[501] = (d501, "Contour rings of the valley: at your spot the steepest uphill direction is ∇f, so the pilot points the nose exactly opposite, straight down the wall.")

def d508(c):
    Q = [[1, 0], [0, 4]]; B = Bowl(Q, 128, 86, 19)
    pts = sd_pts(Q, x0_on_level(Q, 160, 8), 6)
    parts = B.rings() + [B.path(pts, 2.2)] + [dot(*B.pr(p), None, r=2.4) for p in pts[:5]]
    p0 = B.pr(pts[0])
    parts += [plane(p0[0] - 4, p0[1] - 12, 0, .65), N(p0[0] - 6, p0[1] + 12, "x₀", 10, "end"), N(128, 130, "each leg stops where it grazes a ring,", 8, "middle"),
              N(128, 140, "so the next heading is ⊥ → zig-zag", 8.5, "middle", "bold")]
    return svg(c, *parts)
D[508] = (d508, "Exact line search flies until the path just grazes a ring of equal altitude, so the next heading is perpendicular to the last: the zig-zag.")

def d504(c):
    Q = [[1, 0], [0, 6]]; B = Bowl(Q, 128, 86, 19)
    x0 = x0_on_level(Q, 190, 8); g = mv(Q, x0); n = math.hypot(*g); u = [-g[0] / n, -g[1] / n]
    tip = [x0[0] + 1.6 * u[0], x0[1] + 1.6 * u[1]]; ax = [x0[0] + 3.0, x0[1] * 0.0 + 0.0]
    p0, pt, pa = B.pr(x0), B.pr(tip), B.pr([x0[0] + 1.9, x0[1] * 0.45])
    parts = B.rings() + [B.seg(x0, tip, 2.8), arrow(*B.pr([tip[0] - .15 * u[0], tip[1] - .15 * u[1]]), *pt, 2.8), B.seg(x0, [0, 0], 1.4, "4 3"),
        dot(*p0, None, r=3), dot(*B.pr([0, 0]), None, r=2.6), plane(p0[0] - 4, p0[1] - 12, 0, .7),
        N(pt[0] + 6, pt[1] + 4, "−g", 9.5, "start", "bold"), N(pa[0] + 4, pa[1] - 6, "to the lowest point", 8, "start"), N(p0[0] + 18, p0[1] - 8, "θ", 11, "start", "bold"),
        N(128, 140, "worst case: cos θ ≥ 2√κ/(κ+1)", 8.5, "middle", "bold")]
    return svg(c, *parts)
D[504] = (d504, "The nose (−g) is rarely aimed at the lowest point; Kantorovich bounds the worst misalignment θ, and with it the least altitude gained per leg.")

def d505(c):
    Q = [[1, 0], [0, 14]]; B = Bowl(Q, 128, 86, 19)
    pts = sd_pts(Q, x0_on_level(Q, 160, 8), 7)
    parts = B.rings() + [B.path(pts, 2.4), plane(B.pr(pts[0])[0] - 4, B.pr(pts[0])[1] - 12, 0, .65),
        N(128, 12, "narrow canyon: large κ", 8.5, "middle", "bold"), N(128, 130, "bounces off the walls,", 8, "middle"), N(128, 140, "crawls along the floor", 8.5, "middle", "bold")]
    return svg(c, *parts)
D[505] = (d505, "In a long thin canyon (large condition number κ) heading perpendicular to the contour slams you into the opposite wall; progress along the floor is slow.")

def d507(c):
    Q = [[1, 0], [0, 12]]; B = Bowl(Q, 128, 86, 19)
    x0 = x0_on_level(Q, 160, 8)
    sp = sd_pts(Q, x0, 6)
    x, xp, mom = x0[:], x0[:], [x0[:]]
    for _ in range(12):
        g = mv(Q, x); xn = [x[0] - 0.12 * g[0] + 0.55 * (x[0] - xp[0]), x[1] - 0.12 * g[1] + 0.55 * (x[1] - xp[1])]
        xp, x = x, xn; mom.append(x[:])
    parts = B.rings() + [B.path(sp, 1.4, "3 3"), B.path(mom, 2.6), plane(B.pr(x0)[0] - 4, B.pr(x0)[1] - 12, 0, .65),
        N(128, 12, "dashed: plain steepest descent bounces", 8, "middle"),
        N(128, 130, "solid: momentum keeps its heading", 8, "middle"), N(128, 140, "and rolls down the canyon floor", 8.5, "middle", "bold")]
    return svg(c, *parts)
D[507] = (d507, "A heavy airliner keeps its heading through small gusts: the momentum path (solid) glides down the canyon floor while plain steepest descent (dashed) rattles between the walls.")

def d706(c):
    from cmo_refine_zz_conjugate_cards import Q7, X0, cg_path
    B = Bowl(Q7, 128, 90, 17, rot=0)
    x0, x1, xs = cg_path(Q7, X0)
    p0, p1, ps = B.pr(x0), B.pr(x1), B.pr(xs)
    parts = B.rings() + [B.seg(x0, x1), B.seg(x1, xs), dot(*p0, "x₀", -6, 3, 10, "end", 3), dot(*p1, "x₁", 7, -6, 10, "start", 3), dot(*ps, "x*", 9, 4, 10, "start", 3.4),
        N(128, 130, "2D: exactly two legs", 8, "middle"), N(128, 140, "leg 1 kills the error along d₀; leg 2 kills the rest", 8.5, "middle", "bold")]
    return svg(c, *parts)
D[706] = (d706, "In 2D conjugate gradient lands on the lowest point in exactly two legs: the first removes the error along d₀, the second removes the rest.")

FIX = {cid: {"drawingSvg": fnc(cid), "drawingCaption": cap} for cid, (fnc, cap) in D.items()}
