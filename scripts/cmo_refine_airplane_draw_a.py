"""Airplane drawings for CMO topics 10-13 (replace the old diagrams)."""
import math
from air_lib import *
from dip_lib import E

def ang(cx, cy, r, deg):
    a = math.radians(deg); return cx + r * math.cos(a), cy - r * math.sin(a)

def wedge(cx, cy, r, a0, a1, fill="#d9dee7", w=1.5, d=None):
    pts = [(cx, cy)] + [ang(cx, cy, r, a0 + (a1 - a0) * i / 12) for i in range(13)]
    return poly(pts, w, d, fill)

D = {}

def d1001(c):
    return svg(c, E(60, 72, 42, 40, 0, "#d1d5db", 1.8), it(60, 76, "restricted", 9.5), it(60, 88, "zone C₁", 9.5),
        PG("150,38 212,48 222,100 162,116 138,76", "#f1f5f9", 1.8), plane(186, 80, -20, 0.9), it(186, 36, "your corridor C₂", 9),
        L(112, 14, 100, 132, 2.4, d="6 3"), N(110, 11, "aᵀx = b", 8.5), arrow(106, 74, 134, 72, 1.8), it(124, 66, "a", 9.5))
D[1001] = (d1001, "Two convex airspaces that do not overlap: one flat do-not-cross wall (aᵀx = b) has the restricted zone on one side and your corridor on the other.")

def d1002(c):
    return svg(c, E(112, 82, 74, 50, 0, "#f1f5f9", 2), L(28, 32, 196, 32, 2.6), wall(28, 32, 196, 32, 0, -1, 14, 5, 0.1),
        plane(112, 42, 0, 0.9), dot(112, 32, "x₀", 6, -12), arrow(112, 32, 112, 8, 1.8), it(122, 14, "a", 9.5, "start"),
        N(112, 142, "whole airspace lies on one side: aᵀx ≤ aᵀx₀", 8))
D[1002] = (d1002, "A flat cliff face touches the airspace at exactly one parked spot x₀; the entire airspace stays on one side of it.")

def d1003(c):
    parts = [L(120, 8, 120, 138, 1, d="3 3")]
    for ox, inside in ((18, True), (138, False)):
        oy = 116
        parts.append(poly([(ox, oy), (ox + 91, oy - 15), (ox + 39, oy - 81)], 1.2, None, "#e5e7eb"))
        parts.append(arrow(ox, oy, ox + 70, oy - 12, 2.4)); parts.append(arrow(ox, oy, ox + 30, oy - 62, 2.4))
        parts.append(it(ox + 74, oy - 8, "a₁", 9, "start")); parts.append(it(ox + 24, oy - 64, "a₂", 9, "end"))
        parts.append(plane(ox, oy, -20, .6))
    parts += [arrow(18, 116, 66, 84, 2.8), it(70, 82, "b", 10.5, "start"), N(60, 134, "b inside: walls hold ✓", 8),
              arrow(138, 116, 200, 124, 2.8), it(194, 138, "b", 10.5, "end"), dash(128, 118, 232, 116, 1.4, "5 3"),
              arrow(138, 116, 138, 84, 2.2), it(144, 88, "y", 10, "start"), N(180, 12, "b outside: y proves it ✗", 8)]
    return svg(c, *parts)
D[1003] = (d1003, "Left: gravity b sits inside the cone of wall pushes a₁, a₂, so the walls hold the plane. Right: b is outside; the heading y is allowed by every wall yet gravity drags you down it.")

def d1007(c):
    ox, oy, u = 40, 112, 38
    P_ = lambda a, b: (ox + a * u, oy - b * u)
    parts = [poly([(ox, oy), (206, oy), (ox + 104, oy - 104)], 1, None, "#e5e7eb"),
             dash(ox, oy, 214, oy, 1, "4 3"), dash(ox, oy, 150, oy - 110, 1, "4 3"),
             arrow(ox, oy, *P_(1, 0), 2.8), it(*P_(1, 0.0), "a₁", 9.5, "middle") if False else it(ox + 44, oy + 12, "a₁", 9.5, "start"),
             arrow(ox, oy, *P_(1, 1), 2.8), it(ox + 44, oy - 52, "a₂", 9.5, "start"),
             arrow(ox, oy, *P_(2, 1), 2.2), dot(*P_(2, 1), "b ✓", 5, -6, 9, "start"), 
             arrow(ox, oy, *P_(0, 1), 2.2), dot(*P_(0, 1), "b′ ✗", 5, -6, 9, "start"),
             arrow(ox, oy, ox + 24, oy + 26, 2.2), it(ox + 26, oy + 30, "y", 9.5, "start"),
             plane(ox, oy, -30, 0.6)]
    return svg(c, *parts)
D[1007] = (d1007, "Cone of two wall pushes a₁=(1,0), a₂=(1,1). Gravity b=(2,1) sits inside; b′=(0,1) sits outside, and y=(1,−1) is the heading that proves it.")

def d1004(c):
    parts = [L(120, 8, 120, 138, 1, d="3 3"),
             wall(14, 110, 100, 120, 0.1, 1, 8), plane(56, 78, -30, 1), arrow(66, 72, 98, 50, 2.6), it(100, 46, "x", 10, "start"),
             N(60, 20, "open sky: Ax < 0", 8.5, "middle", "bold"), N(60, 34, "tilt away from all walls", 8)]
    tri = [(176, 24), (226, 104), (132, 108)]
    parts.append(PG(" ".join(f"{x},{y}" for x, y in tri), "#f1f5f9", 1.2))
    for i in range(3):
        a, b = tri[i], tri[(i + 1) % 3]
        mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
        parts.append(arrow(mx, my, 176 + (mx - 176) * 0.45, 79 + (my - 79) * 0.45, 2))
    parts += [plane(176, 80, 0, .75), N(178, 126, "boxed in: Σ yᵢaᵢ = 0", 8.5, "middle", "bold"), N(178, 138, "pushes cancel exactly", 8)]
    return svg(c, *parts)
D[1004] = (d1004, "Gordan: either a heading tilts you strictly away from every wall (open sky), or the wall pushes cancel with non-negative weights (boxed into a canyon).")

def d1005(c):
    ox, oy = 118, 76
    parts = [wedge(ox, oy, 62, 160, 280, "#ffffff", 1.4, "4 3"), wedge(ox, oy, 56, -20, 110, "#eef0f4", 1.4, "5 3"),
             wedge(ox, oy, 46, 10, 70, "#c9ced8", 2), plane(ox, oy, -40, .7)]
    parts += [it(*ang(ox, oy, 31, 40), "K", 11), N(*ang(ox, oy, 46, -12), "K*", 9, "middle", "bold") if False else it(*ang(ox, oy, 66, -8), "K*", 10.5),
              it(*ang(ox, oy, 38, 222), "K°", 10.5), N(120, 142, "K legal headings · K° safe pulls", 8)]
    return svg(c, *parts)
D[1005] = (d1005, "The shaded wedge K is the set of legal headings. K* (dashed, wide) contains every force that never opposes a legal heading; its mirror image K° contains every pull that makes every legal heading uphill.")

def d1006(c):
    cx, cy = 110, 108
    return svg(c, wall(cx, 14, cx, cy, -1, 0, 9), wall(cx, cy, 228, cy, 0, 1, 10), R(0, 0, 0, 0, "none", 0),
        plane(cx + 14, cy - 14, -45, .8), dot(cx, cy, None),
        arrow(cx, cy, cx - 34, cy + 28, 2.2, d="4 3"), it(cx - 4, cy + 34, "−∇f", 9.5, "end"),
        arrow(cx + 4, cy - 44, cx + 40, cy - 44, 2.6), it(cx + 42, cy - 40, "push₁", 9, "start"),
        arrow(cx + 52, cy - 4, cx + 52, cy - 40, 2.6), it(cx + 56, cy - 24, "push₂", 9, "start"),
        N(176, 134, "−∇f = μ₁∇g₁ + μ₂∇g₂", 8.5), N(176, 144, "μ ≥ 0", 8))
D[1006] = (d1006, "Parked in a mountain corner: gravity pulls into both walls and each wall pushes back with a non-negative weight, so the net force is zero.")

def d1101(c):
    return svg(c, R(10, 10, 48, 118, "#d1d5db", 0), wall(58, 10, 58, 128, -1, 0, 12, 7), N(30, 70, "rock", 8),
        plane(84, 70, 0, 1), arrow(80, 58, 62, 58, 2.4, d="4 3"), it(78, 52, "−∇f", 9, "end") if False else it(94, 54, "−∇f", 9),
        arrow(70, 90, 112, 90, 2.6), it(116, 94, "μ", 10, "start"),
        L(150, 10, 150, 128, 0.8, d="2 3"),
        N(160, 28, "① ∇f + μ∇g = 0", 8, "start"), N(160, 50, "② g ≤ 0", 8, "start"), N(160, 72, "③ μ ≥ 0", 8, "start"), N(160, 94, "④ μ·g = 0", 8, "start"),
        N(160, 115, "forces cancel · inside", 7.5, "start"), N(160, 126, "walls only push · off = 0", 7.5, "start"))
D[1101] = (d1101, "The four KKT checks as a pre-flight list: forces cancel, you are inside, walls only push, and a wall you are not touching pushes zero.")

def d1102(c):
    parts = [L(120, 8, 120, 138, 1, d="3 3"), wall(114, 14, 114, 126, 1, 0, 10, 0), R(0, 0, 0, 0, "none", 0)]
    parts = [L(120, 8, 120, 138, 1, d="3 3"),
             wall(104, 20, 104, 120, 1, 0, 9, 6), plane(46, 70, 0, 1), arrow(66, 70, 98, 70, 1.4, d="2 2"), N(82, 62, "gap", 7.5),
             N(60, 18, "g < 0 : OFF", 9, "middle", "bold"), N(60, 128, "μ = 0, no push", 8.5),
             wall(228, 20, 228, 120, 1, 0, 9, 6), plane(210, 70, 0, 1), arrow(196, 90, 164, 90, 2.6), it(166, 84, "μ>0", 9, "start"),
             N(172, 18, "g = 0 : ON", 9, "middle", "bold"), N(172, 128, "wall pushes back", 8.5)]
    return svg(c, *parts)
D[1102] = (d1102, "A wall is an on/off switch: across the valley (gap, g<0) it pushes with zero; wing against it (g=0) it may push back with μ>0.")

def d1103(c):
    return svg(c, fn(lambda x: 112 - 80 * (((x - 120) / 88) ** 2), 32, 208, 40, 2.4), wall(32, 28, 32, 112, -1, 0, 6, 6), wall(208, 28, 208, 112, 1, 0, 6, 6),
        plane(120, 94, 0, 1), dash(66, 112, 174, 112, 1.2), dot(120, 112, "global min", 0, 14, 9, "middle"),
        N(120, 16, "convex valley, flat walls: one lowest spot", 8.5, "middle", "bold"), N(120, 142, "KKT holds  ⇒  global minimum", 8.5))
D[1103] = (d1103, "A convex valley with flat walls has only one lowest parking spot: if the forces balance there, nothing deeper exists elsewhere.")

def d1104(c):
    parts = [L(120, 8, 120, 138, 1, d="3 3"),
             wall(20, 100, 100, 100, 0, 1, 7), wall(100, 100, 100, 24, 1, 0, 6), plane(70, 70, -45, .8), dot(100, 100),
             arrow(60, 100, 60, 122, 2), it(66, 124, "∇g₁", 8.5, "start"), arrow(100, 62, 126, 62, 2) if False else arrow(100, 50, 118, 50, 2), it(104, 44, "∇g₂", 8.5, "start"),
             N(60, 18, "independent normals ✓", 8, "middle", "bold"), N(60, 138, "LICQ holds", 8)]
    up = [(130 + i * 6, 76 - 0.012 * (i * 6) ** 2) for i in range(0, 15)]
    parts += [poly(up, 2.2), L(130, 76, 224, 76, 2.2), dot(130, 76), plane(168, 64, 0, .6),
              arrow(196, 76, 196, 100, 2), it(200, 104, "∇g₂", 8.5, "start"), arrow(196, 42, 196, 20, 2), it(200, 24, "∇g₁", 8.5, "start"),
              N(176, 18, "", 8), N(176, 128, "parallel normals ✗", 8, "middle", "bold"), N(176, 140, "LICQ fails (cusp)", 8)]
    return svg(c, *parts)
D[1104] = (d1104, "Left: two touching walls with independent normals pin the plane uniquely. Right: a cusp where both normals point the same way, so the wall pushes cannot be told apart.")

def d1105(c):
    return svg(c, PG("20,30 104,22 112,112 28,120", "#f1f5f9", 2), plane(66, 70, -10, 1), dot(66, 70, "x̄", 4, 18, 9.5, "start", 2.5),
        N(66, 140, "room inside: g < 0 strictly ✓", 8), L(120, 8, 120, 138, 1, d="3 3"),
        L(146, 36, 218, 106, 4), N(184, 70, "g ≤ 0 and −g ≤ 0", 8, "start") if False else N(176, 132, "no interior: knife-edge ✗", 8),
        N(176, 18, "Slater fails", 9, "middle", "bold"), plane(182, 71, 40, .7))
D[1105] = (d1105, "Slater's condition: a hangar with room to move (a strictly interior point x̄, left) versus a zero-thickness knife-edge corridor (right).")

def d1106(c):
    ox, oy, u = 56, 112, 80
    X = lambda a, b: (ox + a * u, oy - b * u)
    return svg(c, E(ox, oy, 66, 33, 0, "none", 1.2, "4 3"), L(*X(1.4, -0.4), *X(-0.2, 1.2), 2.4), wall(*X(1.0, 0), *X(0.0, 1.0), -0.7, 0.7, 8, 6, 0.1),
        L(ox - 14, oy, 226, oy, 1, ar=True), L(ox, oy + 8, ox, 8, 1, ar=True),
        dot(ox, oy, None), N(6, 20, "Case 1: μ = 0", 8.5, "start", "bold"), N(6, 32, "lowest point is outside ✗", 8, "start"),
        plane(*X(0.8, 0.2), -35, .7), dot(*X(0.8, 0.2), "x*", 6, 12, 9, "start", 2.5), N(236, 50, "Case 2: on the wall", 8.5, "end", "bold"), N(236, 62, "μ* = 8/5 > 0 ✓", 8.5, "end"))
D[1106] = (d1106, "Contours of f centred at the origin. Case 1 (free flight, μ=0) lands outside the legal side of the wall x₁+x₂ ≥ 1. Case 2 (pressed to the wall) gives x*=(4/5,1/5) with μ*=8/5.")

def d1201(c):
    return svg(c, fn(lambda x: 76 - 46 * ((x - 120) / 80) ** 2, 40, 200, 40, 2.4), fn(lambda x: 76 + 50 * ((x - 120) / 80) ** 2, 40, 200, 40, 1.6, "5 3"),
        plane(120, 66, 0, .8), dot(120, 76), N(60, 22, "along runway M: curves up ✓", 8, "start") if False else N(42, 20, "along runway M: dᵀ∇²L d ≥ 0 ✓", 8, "start"),
        N(160, 134, "off the runway it may plunge", 8), N(120, 144, "(that is fine)", 7.5))
D[1201] = (d1201, "Solid: the terrain along the runway (tangent subspace M) must be level or curve up. Dashed: across the runway it may plunge steeply, and that does not matter.")

def d1202(c):
    return svg(c, fn(lambda x: 112 - 66 * ((x - 120) / 85) ** 2, 36, 204, 40, 2.4), fn(lambda x: 112 - 26 * ((x - 120) / 85) ** 2, 36, 204, 40, 1.2, "4 3"),
        plane(120, 98, 0, .8), dot(120, 112), dash(60, 112, 180, 112, 1), N(120, 20, "strict bowl along every critical direction", 8.5, "middle", "bold"),
        N(120, 132, "dᵀ∇²L d ≥ c‖d‖² > 0", 8.5))
D[1202] = (d1202, "Along every critical heading the ground rises at least like a bowl c‖d‖² above the parking spot: a strict local minimum.")

def d1203(c):
    x0, y0 = 30, 26
    return svg(c, R(x0, y0, 22, 22, "#d9dee7", 1.2), R(x0 + 22, y0, 70, 22, "#d9dee7", 1.2), R(x0, y0 + 22, 22, 70, "#d9dee7", 1.2), R(x0 + 22, y0 + 22, 70, 70, "#ffffff", 1.2),
        N(x0 + 11, y0 + 15, "0", 9), N(x0 + 57, y0 + 15, "Jᵀ (wall normals)", 7.5), N(x0 + 11, y0 + 60, "J", 9), N(x0 + 57, y0 + 60, "∇²L", 10, "middle", "bold"),
        plane(160, 40, 0, .8), N(164, 66, "(−1)^m × minors", 8.5), N(164, 80, "alternate in sign", 8.5), N(164, 94, "⇒ runway dips", 8.5, "middle", "bold"),
        N(120, 134, "border the Hessian with the wall normals", 8))
D[1203] = (d1203, "The bordered Hessian: wall normals J form the border around ∇²L, and the sign pattern of its trailing minors tells you whether the runway dips at your parking spot.")

def d1204(c):
    parts = [L(120, 8, 120, 138, 1, d="3 3"),
             wall(20, 100, 100, 100, 0, 1, 7), wall(100, 100, 100, 20, 1, 0, 7), plane(78, 78, -45, .7), dot(100, 100),
             arrow(60, 100, 60, 78, 2), arrow(100, 60, 78, 60, 2),
             N(60, 22, "all μ > 0: pinned", 8.5, "middle", "bold"), N(60, 122, "μ₁, μ₂ > 0", 8), N(60, 134, "critical cone = {0}", 8),
             wall(130, 100, 226, 100, 0, 1, 9), plane(176, 82, 0, .8), dot(176, 100), arrow(176, 98, 176, 98, 1),
             arrow(176, 84, 214, 70, 1.5, d="3 2"), arrow(176, 84, 138, 70, 1.5, d="3 2"), arrow(176, 84, 176, 44, 1.5, d="3 2"),
             N(176, 22, "μ = 0 : can peel off", 8.5, "middle", "bold"), N(176, 134, "critical cone = a wedge", 8)]
    return svg(c, *parts)
D[1204] = (d1204, "Left: both touching walls push strictly (μ>0), so the plane is pinned with no freedom. Right: a touching wall pushing zero lets you peel away in some headings, so the critical cone is a wedge.")

def d1205(c):
    return svg(c, P("M24,34 Q120,176 216,34", "none", 3), wall(24, 34, 216, 34, 0, 0.0001, 1, 0, 0.1) if False else "",
        plane(120, 98, 0, .85), arrow(120, 118, 120, 52, 2.6), it(126, 62, "bank pushes", 8.5, "start"),
        arrow(80, 98, 80, 122, 1.8, d="3 2"), it(76, 132, "−∇f", 8.5, "end"), N(120, 18, "∇²f alone: flat or negative", 8.5), N(120, 142, "∇²f + μ∇²g > 0 ✓", 8.5, "middle", "bold"))
D[1205] = (d1205, "A banked, curved runway: the curve of the wall itself supplies an extra push, so the Lagrangian's curvature ∇²f + μ∇²g is what holds the plane in the bowl.")

def d1206(c):
    cx, cy, r = 112, 66, 46
    sx, sy = cx - r / 1.4142, cy + r / 1.4142
    return svg(c, circ(cx, cy, r, "#f1f5f9", 2.2), plane(sx + 8, sy - 8, 90 + 45 - 90 + 0, .6) if False else "",
        dash(sx - 20, sy - 20, sx + 20, sy + 20, 1.2), dot(sx, sy, "x*", -8, 14, 9.5, "end"), arrow(sx, sy, sx - 26, sy + 26, 2.2), it(sx - 30, sy + 40, "−∇f", 9, "end"),
        plane(cx + 14, cy - 40, -20, .7), N(cx, 12, "ring x₁²+x₂² = 1", 8.5),
        N(168, 48, "altitude", 8.5, "start"), N(168, 60, "x₁+x₂", 8.5, "start"), N(168, 76, "lowest: SW", 8.5, "start"), N(168, 96, "det B < 0", 8.5, "start", "bold"), N(168, 108, "⇒ min ✓", 8.5, "start"))
D[1206] = (d1206, "The plane laps a circular ring; altitude is x₁+x₂. The lowest point is south-west, and the bordered Hessian determinant −4√2 < 0 confirms a strict minimum.")

def d1301(c):
    pg = [(40, 56), (110, 30), (158, 60), (150, 114), (70, 122), (34, 88)]
    return svg(c, PG(" ".join(f"{x},{y}" for x, y in pg), "#f1f5f9", 2), it(88, 86, "Ω", 14),
        plane(190, 20, 130, .8), dash(190, 20, 140, 46, 1.4), dot(140, 46, "P(p)", -4, 14, 9, "end", 2.8), dot(190, 20, None) if False else "",
        it(204, 14, "p", 11, "start"), dot(70, 100, "y", -5, 14, 9.5, "end", 2.4), dash(140, 46, 70, 100, 1.2, "2 3"),
        N(200, 112, "(p−P)ᵀ(y−P) ≤ 0", 8, "middle"), N(200, 126, "every y makes an", 8), N(200, 138, "obtuse angle", 8))
D[1301] = (d1301, "A plane blown outside the airspace is guided to the closest legal point P(p); every other legal point y sits at an obtuse angle from there.")

def d1302(c):
    p, q, Pp, Pq = (60, 35), (175, 50), (80, 102), (181, 72)
    return svg(c, L(14, 124, 226, 62, 2.6), wall(14, 124, 226, 62, 0.28, 0.96, 14, 6, 0.1),
        plane(*p, 20, .7), plane(*q, 20, .7), dash(*p, *Pp, 1.2), dash(*q, *Pq, 1.2), dot(*Pp, "P(p)", 0, 16, 8.5, "middle", 2.5), dot(*Pq, "P(q)", 8, 14, 8.5, "middle", 2.5),
        L(p[0], p[1] - 14, q[0], q[1] - 14, 1.2, d="2 2"), N(118, 28, "‖p−q‖", 8.5), L(Pp[0], Pp[1] + 12, Pq[0], Pq[1] + 12, 1.2, d="2 2") if False else "",
        N(122, 140, "‖P(p)−P(q)‖ ≤ ‖p−q‖", 8.5, "middle", "bold"))
D[1302] = (d1302, "Two off-course planes are each guided to the nearest legal spot on the wall: their landing spots are never farther apart than the planes were.")

def d1303(c):
    return svg(c, L(24, 118, 214, 46, 2.6), wall(24, 118, 214, 46, 0.36, 0.93, 13, 6, 0.1) if False else wall(24, 118, 214, 46, -0.36, -0.93, 0, 0, 0.1) if False else "",
        wall(24, 118, 214, 46, 0.36, 0.93, 14, 6, 0.1),
        plane(130, 22, 20, .75), dash(130, 28, 147, 69, 1.4), dot(147, 69, "P(p)", 8, 14, 8.5, "start", 2.5), it(143, 20, "outside", 9, "start") if False else "",
        N(160, 14, "outside → dropped on the wall", 8, "start"), plane(70, 96, 20, .75), N(70, 128, "already legal: stays", 8))
D[1303] = (d1303, "Half-space of legal altitudes: a plane outside is dropped straight along the wall's normal; a plane already on the legal side stays put.")

def d1307(c):
    return svg(c, L(120, 8, 120, 138, 1, d="3 3"),
        R(22, 52, 74, 60, "#f1f5f9", 2), plane(112, 26, 40, .7) if False else plane(116, 24, 130, .7), arrow(110, 30, 99, 49, 1.4, d="2 2"), dot(96, 52, "P", 4, -4, 9, "start", 2.5),
        N(60, 128, "clamp each coordinate", 8.5, "middle", "bold"), N(60, 140, "to its own limits", 8),
        circ(178, 75, 32, "#f1f5f9", 2), plane(226, 30, 135, .7), dash(222, 34, 202, 53, 1.4), dot(201, 52, "P", 4, 14, 9, "start", 2.5),
        N(178, 128, "scale back to the radius", 8.5, "middle", "bold"), N(178, 140, "if outside the ball", 8))
D[1307] = (d1307, "Left: a box is clamped coordinate by coordinate. Right: a ball is the holding circle around the airport, so you steer to the centre until you reach its edge.")

def d1304(c):
    ox, oy = 128, 106
    X = lambda a, b: (ox + a, oy - b)
    return svg(c, wedge(ox, oy, 64, 10, 70, "#c9ced8", 2), wedge(ox, oy, 52, 160, 280, "#ffffff", 1.2, "4 3"),
        arrow(ox, oy, *X(-40, 69.3), 2.6), it(*X(-44, 74), "x", 11, "end"),
        arrow(ox, oy, *X(17.6, 48.3), 2.2), it(*X(24, 54), "P_K(x)", 9, "start"),
        arrow(ox, oy, *X(-57.6, 21), 2.2), it(*X(-60, 28), "P_K°(x)", 9, "end"),
        dash(*X(-40, 69.3), *X(17.6, 48.3), 1.2, "2 3"), dash(*X(-40, 69.3), *X(-57.6, 21), 1.2, "2 3"),
        plane(ox, oy, -40, .6), N(ox - 20, oy + 28, "x = P_K(x) + P_K°(x),  ⟂", 8.5), N(ox + 38, oy - 10, "K", 10, "middle", "bold"), N(ox - 38, oy + 6, "K°", 10, "middle", "bold"))
D[1304] = (d1304, "Any wind vector x splits into a part along the legal cone K and a part in its polar cone K°, and the two parts are perpendicular.")

def d1305(c):
    wedge_pts = [(140, 75), (234, 128), (234, 22)]
    return svg(c, poly(wedge_pts, 1.6, None, "#d9dee7"), L(52, 28, 226, 128, 1.2), L(52, 122, 226, 22, 1.2), N(34, 20, "C₁", 9), N(34, 138, "C₂", 9),
        plane(40, 76, 0, .8), poly([(40, 76), (96, 108), (130, 90), (160, 106), (176, 98), (190, 105)], 1.3, "3 2"),
        dot(190, 105, "plain: some point", 0, 15, 8, "middle", 2.5), dot(140, 75, "Dykstra: apex", 0, -8, 8.5, "middle", 3), poly([(40, 76), (140, 75)], 2.4))
D[1305] = (d1305, "Two overlapping airspaces C₁, C₂. Plain alternating projections zig-zag and stop at some point of the overlap; Dykstra's memory sends the plane straight to the nearest point (the apex).")

def d1306(c):
    xs, hs, base, w = [30, 62, 94, 126], [90, 60, 30, 12], 122, 24
    parts = []
    for x, h in zip(xs, hs):
        parts.append(R(x, base - h, w, h, "#f1f5f9", 1.5)); parts.append(R(x, base - h, w, max(0, h - 45), "#c9ced8", 1.5) if h > 45 else "")
    parts += [L(20, base - 45, 158, base - 45, 1.6, d="5 3"), N(20, base - 50, "τ = 0.75", 8.5, "start"), L(14, base, 158, base, 1.4)]
    parts += [N(74, 136, "tanks (x)", 8.5), plane(206, 40, 0, .9), N(204, 66, "fuel budget Σ = 1", 8.5), N(204, 84, "keep what sticks", 8), N(204, 96, "above the level:", 8), N(204, 112, "p = (.75,.25,0,0)", 8, "middle", "bold")]
    return svg(c, *parts)
D[1306] = (d1306, "Fuel tanks with readings x. Shave one common level τ off every tank, clip at empty, and choose τ so the leftover fuel sums to exactly 1.")

FIX = {cid: {"drawingSvg": fnc(cid), "drawingCaption": cap} for cid, (fnc, cap) in D.items()}
