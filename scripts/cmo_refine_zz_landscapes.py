"""Valley/landscape cards (topics 05-07) redrawn as a tilted top view of the bowl so the hops are visible."""
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
    parts += [plane(p0[0] - 4, p0[1] - 12, 0, .65), N(p0[0] - 6, p0[1] + 12, "x₀", 10, "end"), N(128, 130, "each hop stops where it grazes a ring,", 8, "middle"),
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
D[504] = (d504, "The nose (−g) is rarely aimed at the lowest point; Kantorovich bounds the worst misalignment θ, and with it the least altitude gained per hop.")

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
        N(128, 130, "2D: exactly two hops", 8, "middle"), N(128, 140, "hop 1 kills the error along d₀; hop 2 kills the rest", 8.5, "middle", "bold")]
    return svg(c, *parts)
D[706] = (d706, "In 2D conjugate gradient lands on the lowest point in exactly two hops: the first removes the error along d₀, the second removes the rest.")

def d401(c):
    import math
    Y = lambda x: 40 + 70 * (1 - ((x - 125) / 100) ** 2)
    xk = 45; yk = Y(xk); ang = math.atan(70 * 2 * 0.8 / 100); ux, uy = math.cos(ang), math.sin(ang)
    px, py = xk + 2, yk - 20
    parts = [poly([(x, Y(x)) for x in range(25, 226, 4)], 2.4), N(225, 34, "ground = f", 7.5, "end"),
        N(120, 12, "nose points downhill: ∇fᵀdₖ < 0", 9, "middle", "bold"),
        dot(xk, yk, None, 0, 0, 9, "start", 2.6), N(xk - 2, yk + 14, "xₖ", 9.5, "middle"), dash(px, py + 5, xk, yk - 3, 1, "2 2"),
        plane(px, py, math.degrees(ang), .95),
        arrow(px + 14 * ux, py + 14 * uy, px + 40 * ux, py + 40 * uy, 2.4), N(px + 42 * ux + 3, py + 40 * uy - 2, "dₖ ✓", 9, "start", "bold"),
        arrow(px - 14 * ux, py - 14 * uy, px - 26 * ux, py - 26 * uy, 1.1), N(px - 26 * ux - 2, py - 26 * uy - 2, "uphill ✗", 7.5, "end")]
    for x, lab, dx, a in ((80, "too short", -5, "end"), (125, "just right", 0, "middle"), (190, "overshoot", 6, "start")):
        parts += [C(f"{x:.1f}", f"{Y(x):.1f}", 3.2), N(x + dx, Y(x) + 13, lab, 8, a)]
    parts += [L(xk, 138, 125, 138, 1.4, ar=True), N(131, 141, "αₖ = how far to fly", 8.5, "start", "bold")]
    return svg(c, *parts)
D[401] = (d401, "Side view of the valley. The plane sits at xₖ; its nose dₖ must point downhill (that is ∇fᵀdₖ < 0). The step αₖ is how far it flies before reading the radar again: too short barely helps, just right reaches the bottom, too far climbs the other side.")

FIX = {cid: {"drawingSvg": fnc(cid), "drawingCaption": cap} for cid, (fnc, cap) in D.items()}
FIX[401].update(textbookImg=None, textbookRef=None)
