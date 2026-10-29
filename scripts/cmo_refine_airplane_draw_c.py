"""Airplane drawings for CMO topics 17-19 (replace the old diagrams)."""
import math
from air_lib import *
from dip_lib import E

D = {}

def d1701(c):
    return svg(c, plane(60, 74, 0, 1.1), arrow(60, 60, 60, 34, 2.4, d="4 3"), N(66, 42, "wall push", 8.5, "start"), arrow(60, 88, 60, 114, 2.4), N(66, 112, "gravity", 8.5, "start"),
        N(60, 18, "∇ₓL = 0 : forces balance", 8.5, "middle", "bold"), N(60, 136, "only equilibrium states count", 8),
        L(130, 10, 130, 134, 1, d="3 3"), L(170, 118, 170, 28, 2.2), R(160, 70, 20, 8, "#d9dee7", 1.4), arrow(190, 100, 190, 36, 2.4), N(190, 24, "maximise L over μ ≥ 0", 8.5, "middle", "bold"),
        N(176, 134, "μ dial", 8.5, "middle"))
D[1701] = (d1701, "Restrict to equilibrium states where wall pushes exactly balance gravity (∇ₓL = 0), then turn the dial μ up to make the Lagrangian as large as possible.")

def d1702(c):
    ox, oy = 28, 126
    top = [(ox + 8 * k, 72 - 0 + 50 * math.exp(-k / 6)) for k in range(0, 25)]
    bot = [(ox + 8 * k, 72 + 50 * 0 + 50 * (1 - 0) - 50 * (1 - math.exp(-k / 6)) * 0 + 0) for k in range(0, 25)]
    top = [(ox + 8 * k, 66 - 40 * math.exp(-k / 6)) for k in range(0, 25)]   # primal: falls onto p*
    bot = [(ox + 8 * k, 66 + 40 * math.exp(-k / 6)) for k in range(0, 25)]   # dual: rises onto p*
    return svg(c, L(ox, 138, 226, 138, 1.2, ar=True), L(20, 66, 226, 66, 1, d="4 3"), poly([(x, y + 0) for x, y in top], 2.6), poly(bot, 2.6, "5 3"),
        plane(60, 18, 0, .6), N(150, 44, "primal climbs down", 8.5, "start") if False else N(116, 26, "primal: ↓", 8.5, "start"), N(116, 114, "dual: ↑", 8.5, "start"),
        N(226, 60, "p* = q*", 9, "end", "bold"), N(120, 12, "", 8))
D[1702] = (d1702, "Two climbers on opposite sides of a saddle: the lowest legal altitude seen from above and the highest equilibrium floor from below meet at the same value when the valley is convex.")

def d1703(c):
    return svg(c, R(10, 24, 92, 78, "#f1f5f9", 1.8, 4), plane(56, 44, 0, .9), N(56, 70, "cockpit (primal)", 8.5, "middle", "bold"), N(56, 84, "min ½xᵀQx", 9), N(56, 96, "", 8),
        R(138, 24, 92, 78, "#f1f5f9", 1.8, 4), PG("176,52 184,38 192,52", "#ffffff", 1.4), R(178, 52, 12, 14, "#ffffff", 1.2), N(184, 80, "tower (dual)", 8.5, "middle", "bold"), N(184, 94, "max −½yᵀQy+bᵀy", 7.5),
        arrow(104, 63, 136, 63, 1.8), arrow(136, 63, 104, 63, 1.8), N(120, 56, "=", 12, "middle", "bold"), N(120, 128, "same risk, opposite sign: totals meet", 8.5, "middle", "bold"))
D[1703] = (d1703, "Cockpit and tower look at the same flight: the pilot minimises the quadratic fuel burn and the tower maximises its mirror image, and the totals meet at the optimum.")

def d1704(c):
    fx = lambda x: 66 + 28 * math.cos((x - 22) / 24) + 0.07 * (x - 22)
    return svg(c, fn(fx, 22, 226, 60, 2.6), plane(100, fx(100) - 10, 0, .7), dot(100, fx(100), None, r=3), N(124, 22, "∇ₓL = 0 here too", 8.5, "start", "bold"), N(124, 34, "but it is a peak ✗", 8.5, "start"),
        dot(176, fx(176), "x*", 0, 16, 9.5, "middle", 3), N(176, 138, "true lowest point", 8.5), N(40, 138, "false floor", 8.5))
D[1704] = (d1704, "Equilibrium means forces balance, but a force-balanced plane can sit on a mountain peak. Without convexity the Wolfe dual builds a false floor.")

def d1705(c):
    q = lambda x: 116 - 78 * (1 - ((x - 130) / 100) ** 2)
    parts = [L(20, 128, 226, 128, 1.2, ar=True), fn(q, 36, 226, 40, 2.6)]
    xs = [48, 84, 108, 122]
    for i, x in enumerate(xs):
        parts += [dot(x, q(x), None, r=2.6), dash(x, q(x), x, 128, 1, "2 2"), N(x, 138, f"μ{'₀₁₂₃'[i]}", 8, "middle")]
        if i < 3: parts.append(arrow(x + 3, q(x) - 4, xs[i + 1] - 3, q(xs[i + 1]) - 4, 1.6))
    parts += [plane(52, 22, 0, .6), N(142, 24, "g > 0 (hitting the wall):", 8, "start"), N(142, 36, "raise the price μ", 8, "start", "bold"), N(142, 50, "g < 0 (slack): lower it", 8, "start"), N(228, 100, "q(μ)", 9, "end", "bold")]
    return svg(c, *parts)
D[1705] = (d1705, "The tower climbs the concave dual: raise the wall price when the plane violates the wall (g>0), lower it when there is slack, never below zero.")

def d1706(c):
    hs = [86 * math.exp(-0.55 * k) for k in range(5)]
    parts = [L(14, 124, 226, 124, 1.4, ar=True)]
    for k, h in enumerate(hs):
        parts += [R(26 + k * 40, 124 - h, 26, h, "#f1f5f9", 1.6), N(39 + k * 40, 136, f"A{k+1}", 8.5, "middle")]
    parts += [fn(lambda x: 124 - 86 * math.exp(-0.55 * (x - 39) / 40), 39, 199, 30, 1.4, "4 3"), plane(190, 30, 180, .7), N(170, 56, "pᵢ ∝ e^(−βEᵢ)", 9, "start", "bold"), N(170, 70, "(Boltzmann)", 8.5, "start")]
    return svg(c, *parts)
D[1706] = (d1706, "A fixed fleet spread over airports A₁…A₅ with a fixed average fuel cost: maximising entropy gives traffic that decays exponentially with each airport's cost.")

def d1801(c):
    return svg(c, R(8, 24, 100, 84, "#f1f5f9", 1.8, 4), plane(58, 44, 0, .9), N(58, 70, "airline (primal)", 8.5, "middle", "bold"), N(58, 84, "min cᵀx", 9), N(58, 96, "Ax = b, x ≥ 0", 8),
        R(132, 24, 100, 84, "#f1f5f9", 1.8, 4), R(172, 38, 12, 14, "#ffffff", 1.2), PG("170,38 178,28 186,38", "#ffffff", 1.4), N(182, 70, "airport (dual)", 8.5, "middle", "bold"), N(182, 84, "max bᵀy", 9), N(182, 96, "Aᵀy ≤ c", 8),
        arrow(110, 66, 130, 66, 1.6), arrow(130, 66, 110, 66, 1.6), N(120, 130, "cost ≥ revenue, equal at optimum", 8.5, "middle", "bold"))
D[1801] = (d1801, "The airline minimises the cost of a schedule that meets demand b; the airport authority sets fees y to maximise revenue without pricing any route above the airline's cost.")

def d1807(c):
    poly_pts = [(40, 112), (36, 44), (126, 22), (206, 70), (176, 120)]
    parts = [PG(" ".join(f"{x},{y}" for x, y in poly_pts), "#f1f5f9", 2)]
    for x, y in poly_pts: parts.append(dot(x, y, None, r=2.8))
    parts += [plane(136, 36, 0, .7), dot(126, 22, "pinned: 2 walls meet", 6, -6, 8.5, "start", 3.2), N(120, 138, "corners = basic feasible solutions", 8.5, "middle", "bold"), it(110, 78, "Ω", 13)]
    return svg(c, *parts)
D[1807] = (d1807, "A plane can only be pinned in place at a corner of the polygon, where enough walls meet in independent directions. Those corners are the basic feasible solutions.")

def d1802(c):
    poly_pts = [(50, 112), (40, 48), (120, 26), (200, 66), (176, 118)]
    parts = [PG(" ".join(f"{x},{y}" for x, y in poly_pts), "#f1f5f9", 2)]
    for k in range(-2, 5):
        parts.append(L(10, f(48 + 22 * k - 3), 232, f(48 + 22 * k + 41), 1, d="4 3"))
    parts += [dot(176, 118, "lowest", 4, -6, 9, "start", 4), plane(130, 62, -20, .7), arrow(60, 24, 60, 52, 2.4), N(64, 20, "gravity", 8.5, "start"), N(120, 138, "tilted sheet: lowest point is a corner", 8.5, "middle", "bold")]
    return svg(c, *parts)
D[1802] = (d1802, "A linear altitude is a tilted flat sheet over the polygonal airspace: its lowest point is always at a corner.")

def d1803(c):
    rows = [("x_j > 0", "fee = cost"), ("fee < cost", "x_j = 0"), ("wall untouched", "y_i = 0")]
    parts = [N(60, 18, "plan / wall", 8.5, "middle", "bold"), N(184, 18, "fee / price", 8.5, "middle", "bold"), plane(120, 22, 0, .5)]
    for i, (a, b) in enumerate(rows):
        y = 40 + i * 32
        parts += [R(16, y, 88, 22, "#f1f5f9", 1.5, 3), N(60, y + 15, a, 9, "middle", "bold"), R(136, y, 88, 22, "#f1f5f9", 1.5, 3), N(180, y + 15, b, 9, "middle", "bold"), arrow(106, y + 11, 134, y + 11, 1.8), arrow(134, y + 11, 106, y + 11, 1.8)]
    parts.append(N(120, 142, "x_j (c_j − A_jᵀy) = 0  and  y_i (A_i x − b_i) = 0", 8, "middle"))
    return svg(c, *parts)
D[1803] = (d1803, "The airline's rulebook: a route that is flown must have fee equal to cost; a route whose fee is below cost is never flown; a resource wall that is not touched has price zero.")

def d1804(c):
    ox, oy = 26, 114
    return svg(c, poly([(ox, oy), (ox + 90, oy - 14), (ox + 38, oy - 80)], 1.2, None, "#e5e7eb"), arrow(ox, oy, ox + 66, oy - 10, 2.4), arrow(ox, oy, ox + 28, oy - 58, 2.4),
        plane(ox, oy, -20, .55), arrow(ox, oy, ox + 62, oy + 14, 2.4), N(ox + 66, oy + 24, "b", 9.5, "start", "bold"), dash(ox - 6, oy + 6, ox + 100, oy - 4, 1.2, "4 3"),
        arrow(ox, oy, ox - 2, oy - 40, 1.8, d="3 2") if False else "", N(ox + 24, 20, "no legal plan:", 8.5, "start", "bold"), N(ox + 24, 32, "b outside the cone", 8.5, "start"),
        L(138, 10, 138, 134, 1, d="3 3"), arrow(190, 120, 190, 26, 3), N(196, 34, "∞", 14, "start", "bold"), N(192, 136, "dual objective", 8.5, "middle"), N(160, 62, "unbounded ↑", 8.5, "start"))
D[1804] = (d1804, "If no legal flight plan exists (b outside the cone of walls), Farkas gives a heading that no wall blocks; along it the dual can be pushed up without bound.")

def d1805(c):
    poly_pts = [(40, 112), (36, 48), (110, 24), (200, 56), (200, 108)]
    parts = [PG(" ".join(f"{x},{y}" for x, y in poly_pts), "#f1f5f9", 2)]
    path = [(36, 48), (110, 24), (200, 56), (200, 108)]
    parts.append(poly(path, 3.2))
    for i, (x, y) in enumerate(path):
        parts.append(dot(x, y, None, r=3.2))
    parts += [plane(36, 62, 90, .6), N(34, 38, "9", 8.5, "end", "bold"), N(110, 18, "7", 8.5, "middle", "bold"), N(207, 54, "4", 8.5, "start", "bold"), N(207, 112, "1", 8.5, "start", "bold"),
              N(120, 138, "hop to a lower neighbouring corner until none is lower", 8, "middle", "bold")]
    return svg(c, *parts)
D[1805] = (d1805, "At each corner the pilot looks at the neighbouring airports along the edges, hops to a lower one (altitudes 9, 7, 4, 1) and stops when no neighbour is lower.")

def d1808(c):
    poly_pts = [(40, 112), (36, 44), (126, 22), (206, 70), (176, 120)]
    cp = [(110, 74), (126, 82), (146, 94), (162, 106), (176, 118)]
    parts = [PG(" ".join(f"{x},{y}" for x, y in poly_pts), "#f1f5f9", 2), poly([(36, 44), (126, 22), (206, 70), (176, 120)], 1.4, "4 3"), poly(cp, 3), dot(110, 74, None, r=3),
             plane(144, 90, 40, .6), dot(176, 120, "optimum", 4, -8, 9, "start", 3.6), N(46, 128, "central path:", 8.5, "start", "bold"), N(100, 128, "stay off the walls", 8, "start"),
             N(120, 140, "dashed: simplex edges", 8, "middle")]
    return svg(c, *parts)
D[1808] = (d1808, "Fly down the middle of the corridor (solid central path) instead of scraping along the walls from corner to corner (dashed), letting the clearance shrink to zero at the destination corner.")

def d1806(c):
    return svg(c, L(16, 78, 224, 78, 1.6, ar=True), L(120, 66, 120, 90, 2.4), N(120, 70, "12", 11, "middle", "bold"),
        R(20, 52, 100, 22, "#e5e7eb", 1.2), N(70, 46, "primal 3x₁+2x₂ ≤ 12", 8.5, "middle", "bold"), R(120, 82, 100, 22, "#e5e7eb", 1.2), N(170, 120, "dual 5y₁+7y₂ ≥ 12", 8.5, "middle", "bold"),
        plane(120, 36, 90, .6), N(70, 138, "(2,3)", 8.5, "middle"), N(176, 138, "(1,1)", 8.5, "middle"), N(120, 12, "cockpit and tower agree", 9, "middle", "bold"))
D[1806] = (d1806, "Every feasible primal value sits at or below 12 and every feasible dual value at or above 12; they meet at exactly 12 (primal at (2,3), dual at (1,1)).")

def d1901(c):
    return svg(c, L(20, 112, 226, 112, 1.2, ar=True), L(120, 118, 120, 14, 1.4, d="4 3"), fn(lambda x: 112 - 0.012 * (x - 120) ** 2 if x > 120 else 112, 20, 226, 60, 2.8),
        R(20, 118, 100, 14, "#eef0f4", 0), N(70, 128, "legal airspace g ≤ 0", 8.5, "middle", "bold"), N(176, 128, "forbidden", 8.5, "middle", "bold"),
        plane(60, 96, 0, .8), plane(176, 62, 180, .8), N(60, 80, "no fine", 8.5, "middle"), N(196, 36, "fine c·max(0,g)²", 8.5, "middle", "bold"), N(18, 140, "", 8))
D[1901] = (d1901, "Crossing into forbidden airspace triggers a fine c·max(0,g)² that grows quadratically; inside legal airspace there is no fine at all.")

def d1902(c):
    return svg(c, wall(190, 10, 190, 120, 1, 0, 10, 7), L(20, 118, 192, 118, 1.2, ar=True), fn(lambda x: 112 - 80 * (1 - ((x - 20) / 168) ** 0.25) if x < 188 else 112, 20, 187, 60, 2.8) if False else
        poly([(20 + 7 * k, 112 + 22 * math.log(max(1e-3, (190 - (20 + 7 * k)) / 170))) for k in range(0, 24)], 2.8),
        plane(60, 96, 0, .8), N(120, 138, "−μ ln(−g) → ∞ at the wall", 8.5, "middle", "bold"), N(150, 20, "field repels", 8.5, "end", "bold"))
D[1902] = (d1902, "An invisible repulsive field around the mountain: the closer the plane gets to the wall the more the barrier blows up, so it always flies strictly inside legal airspace.")

def d1903(c):
    parts = [E(120, 74, 106, 10, -6, "none", 1.4), E(120, 74, 78, 7, -6, "none", 1.4), E(120, 74, 50, 4.5, -6, "none", 1.4),
             poly([(30, 63), (52, 85), (74, 67), (98, 88), (122, 71), (146, 87), (170, 70), (196, 84)], 2.4), plane(206, 84, 20, .6),
             N(120, 22, "huge fine c: razor-thin canyon", 8.5, "middle", "bold"), N(120, 128, "zig-zag between the walls, slow progress", 8.5), N(120, 140, "cond(Hessian) ≈ c", 8.5, "middle", "bold")]
    return svg(c, *parts)
D[1903] = (d1903, "With a huge fine the valley becomes a razor-thin canyon: stiff across, flat along. The plane zig-zags between the walls instead of making forward progress.")

def d1904(c):
    zig = [(100, 72)]
    for k in range(8):
        zig.append((108 + k * 5, 64 if k % 2 == 0 else 80))
    zig.append((150, 72))
    return svg(c, R(150, 10, 80, 126, "#d1d5db", 0), wall(150, 10, 150, 136, 1, 0, 14, 7), L(130, 10, 130, 136, 1.2, d="4 3"), N(130, 144, "boundary", 8, "middle"),
        plane(88, 72, 0, .9), poly(zig, 1.8), arrow(160, 100, 126, 100, 2.6) if False else "", arrow(148, 100, 100, 100, 2.6), N(124, 114, "λ ≈ c·h", 9, "middle", "bold"),
        N(130, 24, "sinks a little: h(x)", 8.5, "end"), N(120, 134, "", 8))
D[1904] = (d1904, "The plane sinks slightly into the forbidden zone like a foot on a spring scale; stiffness c times the depth h gives the wall's push, the multiplier.")

def d1905(c):
    return svg(c, wall(206, 10, 206, 134, 1, 0, 11, 7), L(20, 44, 204, 44, 1, d="2 3"), L(20, 100, 204, 100, 1, d="2 3"),
        *[dot(x, 44, None, r=2.8) for x in (30, 100, 148, 172, 186, 194)], N(110, 24, "penalty: creeps toward the wall, never lands", 8, "middle", "bold"),
        *[dot(x, 100, None, r=2.8) for x in (30, 120, 206)], plane(160, 86, 0, .55), N(110, 120, "augmented: adjust λ and land exactly", 8, "middle", "bold"), N(110, 134, "with only a moderate fine c", 8))
D[1905] = (d1905, "Ordinary penalty only creeps toward the wall as c grows. The augmented Lagrangian also adjusts the standing reservation λ and lands on the boundary with a moderate fine.")

def d1906(c):
    hs = [20, 52, 70, 79, 84]
    parts = [L(14, 124, 226, 124, 1.4, ar=True), L(14, 124 - 88, 226, 124 - 88, 1.2, d="4 3"), N(224, 124 - 92, "λ*", 9.5, "end", "bold")]
    for k, h in enumerate(hs):
        parts += [R(26 + k * 36, 124 - h, 24, h, "#f1f5f9", 1.6), N(38 + k * 36, 136, f"λ{'₀₁₂₃₄'[k]}", 8.5, "middle")]
    parts += [N(120, 20, "λₖ₊₁ = λₖ + c·h(xₖ)", 9, "middle", "bold"), plane(210, 60, 180, .6), N(120, 32, "small tuning turns, not brute force", 8.5)]
    return svg(c, *parts)
D[1906] = (d1906, "The tower turns the fine-tuning screw by a small correction c·h(xₖ) each leg, so λₖ climbs to λ* while the fine stays moderate.")

FIX = {cid: {"drawingSvg": fnc(cid), "drawingCaption": cap} for cid, (fnc, cap) in D.items()}
