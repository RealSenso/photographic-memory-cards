"""Airplane drawings for CMO topics 14-16 (replace the old diagrams)."""
import math
from air_lib import *

D = {}

def d1401(c):
    return svg(c, R(150, 8, 80, 130, "#d1d5db", 0), wall(150, 8, 150, 138, 1, 0, 14, 7), N(206, 28, "rock", 8),
        plane(96, 38, 20, .85), dot(96, 38, "xₖ", -2, -12, 9.5, "end", 2.5),
        arrow(98, 40, 186, 70, 1.8, d="4 3"), dot(186, 70, None, r=2.2), it(186, 94, "xₖ−α∇f", 8.5, "end"),
        arrow(184, 71, 154, 71, 2.8), dot(150, 71, "xₖ₊₁", -4, 16, 9.5, "end", 3),
        N(60, 138, "slide along the wall, never through it", 8))
D[1401] = (d1401, "A gravity step would carry the plane into the mountain; air-traffic control projects it straight back to the nearest legal point on the wall.")

def d1402(c):
    return svg(c, R(150, 8, 80, 130, "#d1d5db", 0), wall(150, 8, 150, 138, 1, 0, 14, 7), N(192, 40, "rock", 8),
        plane(126, 72, 0, .9), dot(150, 72, "x*", -4, 18, 10, "end", 3), arrow(130, 62, 196, 62, 2, d="4 3"), it(194, 56, "x*−α∇f", 8.5, "end"),
        arrow(196, 82, 154, 82, 2.8), it(184, 98, "P", 10, "middle"),
        N(86, 20, "P(x* − α∇f(x*)) = x*", 9, "middle", "bold"), N(86, 134, "no net motion: a stationary spot", 8))
D[1402] = (d1402, "At the optimum gravity shoves the plane into the wall with full force and the projection returns it to the same parked spot: a fixed point.")

def d1403(c):
    ox, oy = 30, 124
    sub = [(ox + 8 * k, oy - 100 / (1 + 0.15 * k)) for k in range(0, 24)]
    lin = [(ox + 8 * k, oy - 100 * 0.85 ** k) for k in range(0, 24)]
    return svg(c, L(ox, oy, 226, oy, 1.2, ar=True), L(ox, oy, ox, 10, 1.2, ar=True), poly(sub, 2.4, "5 3"), poly(lin, 2.4),
        N(190, 44, "O(1/k) merely convex", 8, "end"), N(176, 106, "ρᵏ strongly convex", 8, "end", "bold"), N(18, 18, "gap", 8, "middle"), N(212, 138, "k (legs flown)", 8, "end"),
        plane(54, 22, 0, .6))
D[1403] = (d1403, "Distance to the best parking spot versus legs flown: a merely convex valley closes in like 1/k, a strongly convex bowl shrinks by a fixed factor each leg. The walls do not change the rate.")

def d1404(c):
    xk = (170, 30)
    pts = [(80, 66, "✓"), (80, 78, "✗"), (80, 102, "✗")]
    parts = [R(8, 8, 72, 130, "#d1d5db", 0), wall(80, 8, 80, 138, -1, 0, 14, 7), plane(*xk, 20, .8), dot(*xk, "xₖ", 0, -12, 9.5, "middle", 2.5),
             dash(*xk, 20, 132, 1.2, "3 3"), N(34, 128, "−α∇f", 8)]
    parts.append(poly([(80, 62), (80, 112)], 1.4, "2 2"))
    for (x, y, m) in pts:
        parts.append(dot(x, y, None, r=2.8))
        parts.append(N(x + 8, y + 3, m + (" accepted" if m == "✓" else ""), 8.5, "start", "bold" if m == "✓" else "normal"))
    parts += [N(176, 108, "trial points slide", 8.5, "middle"), N(176, 120, "along the wall (arc)", 8.5), N(176, 134, "first big enough drop wins", 8)]
    return svg(c, *parts)
D[1404] = (d1404, "Shortening the step traces an arc along the mountain wall. Try points on that arc and accept the first one that gives a big enough altitude drop.")

def d1405(c):
    cx, cy, r = 112, 84, 46
    y = (168, 36)
    ux, uy = y[0] - cx, y[1] - cy; n = math.hypot(ux, uy)
    px, py = cx + ux / n * r, cy + uy / n * r
    return svg(c, circ(cx, cy, r, "#f1f5f9", 2.2), plane(cx, cy - r, 0, .8), dot(cx, cy - r, "xₖ", -4, -9, 9.5, "end", 2.5),
        arrow(cx + 14, cy - r - 2, y[0] - 3, y[1], 2, d="4 3"), dot(y[0], y[1], "y", 6, -2, 10, "start", 2.5),
        arrow(y[0], y[1], px + 2, py - 1, 2.8), dot(px, py, "xₖ₊₁", 7, 10, 9.5, "start", 3),
        N(cx - 4, cy + 4, "curved surface", 8.5), N(40, 138, "tangent step leaves it; drop back along the radius", 8, "start"))
D[1405] = (d1405, "On a curved runway a straight tangent step floats off the surface (y); restoration descends along the normal to plant the wheels back on it.")

def d1406(c):
    ox, oy, u = 50, 100, 26
    X = lambda a, b: (ox + a * u, oy - b * u)
    return svg(c, PG(f"{ox},{oy} 226,{oy} 226,12 {ox},12", "#f1f5f9", 0.1), L(ox, oy, 226, oy, 2, ar=True), L(ox, oy, ox, 8, 2, ar=True),
        N(120, 26, "x ≥ 0 : legal", 8.5, "start", "bold"), N(236, 112, "ground x₂ = 0", 8.5, "end"),
        plane(*X(1, 3), 0, .75), dot(*X(2, -1), None, r=2.4), arrow(X(1, 3)[0] + 6, X(1, 3)[1] + 10, X(2, -1)[0] - 2, X(2, -1)[1] - 4, 1.8, d="4 3"),
        arrow(*X(2, -1), *X(2, 0.05), 2.8), dot(*X(2, 0), "(2,0)", 5, -8, 9, "start", 3), N(150, 128, "x − α∇f dips below ground", 8, "middle"),
        N(120, 140, "max(0, ·) clamps it back", 8, "middle", "bold"))
D[1406] = (d1406, "Altitude cannot go below the ground x₂ = 0: the gradient step dips under it and the clamp max(0,·) puts the plane back on the tarmac.")

def d1501(c):
    return svg(c, wall(14, 42, 226, 42, 0, -1, 18, 8), wall(14, 104, 226, 104, 0, 1, 18, 8),
        plane(120, 73, 0, 1.1), arrow(142, 73, 214, 73, 2.6), arrow(98, 73, 26, 73, 2.6),
        N(120, 24, "walls you touch act as rails", 8.5, "middle", "bold"), N(120, 130, "A_W p = 0 : slide along the corridor only", 8.5))
D[1501] = (d1501, "Lock down the walls you are touching and treat them as rails: only motion along the corridor is left to solve for.")

def d1502(c):
    return svg(c, R(138, 14, 90, 118, "#d1d5db", 0), wall(138, 14, 138, 132, 1, 0, 11, 7),
        plane(46, 72, 0, 1), arrow(64, 72, 130, 72, 2.8), dot(138, 72, "stop: α < 1", -2, 20, 9, "end", 3), arrow(140, 72, 190, 72, 1.5, d="4 3"),
        dot(186, 72, None, r=2.4), N(190, 56, "intended x̂", 8, "end"), N(60, 20, "blocking wall joins", 8.5, "start", "bold"), N(60, 32, "the working set", 8.5, "start", "bold"))
D[1502] = (d1502, "Rolling toward the target, a wall ahead stops the plane early (step α<1) and joins the working set.")

def d1503(c):
    return svg(c, R(10, 104, 220, 34, "#d1d5db", 0), wall(10, 104, 230, 104, 0, 1, 18, 7), plane(80, 92, 0, 1),
        arrow(80, 82, 80, 36, 2.4, d="4 3"), it(86, 44, "gravity points away", 8.5, "start"), N(160, 82, "μ < 0 : the wall", 9, "start", "bold"), N(160, 94, "would have to pull", 9, "start", "bold"),
        arrow(98, 88, 178, 52, 2.8), N(232, 44, "take off ↗", 8.5, "end", "bold"))
D[1503] = (d1503, "A negative multiplier means gravity actually pulls you away from the wall: release the brakes, drop that wall from the working set, and take off.")

def d1504(c):
    parts = []
    xs = [(14, 24, "W₀", "f₀"), (66, 52, "W₁", "f₁"), (118, 80, "W₂", "f₂"), (170, 108, "W₃", "f₃")]
    for i, (x, y, w, fv) in enumerate(xs):
        parts.append(R(x, y, 50, 22, "#f1f5f9", 1.6, 3)); parts.append(N(x + 25, y + 15, f"{w}  {fv}", 9, "middle", "bold"))
        if i < 3: parts.append(arrow(x + 52, y + 11, xs[i + 1][0] - 2, xs[i + 1][1] + 11, 2))
    parts += [plane(234, 136, 0, .5), N(10, 112, "altitude strictly falls:", 8.5, "start"), N(10, 124, "f₀ > f₁ > f₂ > f₃", 9, "start", "bold"), N(10, 136, "no working set repeats", 8.5, "start")]
    return svg(c, *parts)
D[1504] = (d1504, "Each leg lowers altitude, so a working set is never revisited; with only finitely many wall subsets the flight must end in finitely many legs.")

def d1505(c):
    cx, cy = 120, 72
    parts = []
    for a in (0, 60, 120):
        r = math.radians(a)
        parts.append(L(f(cx - 80 * math.cos(r)), f(cy + 80 * math.sin(r)), f(cx + 80 * math.cos(r)), f(cy - 80 * math.sin(r)), 2.2))
    parts += [plane(cx, cy, 0, .85), P(f"M{cx+30},{cy-8} A30,30 0 1,1 {cx+8},{cy-30}", "none", 1.6, "3 2", True),
              N(cx, 14, "three walls meet at one point", 8.5, "middle", "bold"), N(cx, 138, "α = 0 : tower swaps walls, plane idles", 8.5)]
    return svg(c, *parts)
D[1505] = (d1505, "A degenerate corner: three walls meet at one point, the step is zero, and without an anti-cycling rule the tower can swap walls forever.")

def d1506(c):
    ox, oy, u = 36, 120, 34
    X = lambda a, b: (ox + a * u, oy - b * u)
    return svg(c, R(ox, oy - 2 * u, 2 * u, 2 * u, "#f1f5f9", 2), plane(*X(0, 0), 0, .75), dot(*X(2, 0), "x₁=(2,0)", 6, 14, 8.5, "start", 2.5), dot(*X(2, 2), "x*=(2,2)", 6, -4, 9, "start", 3),
        poly([X(0, 0), X(2, 0), X(2, 2)], 2.8), dot(*X(3.2, 3.2), None, r=3), N(X(3.2, 3.2)[0] + 4, X(3.2, 3.2)[1] - 8, "beacon", 8.5, "start"),
        dash(*X(2, 2), *X(3.2, 3.2), 1.2, "2 3"), N(236, 96, "slide, block,", 8.5, "end", "bold"), N(236, 108, "drop, slide", 8.5, "end", "bold"))
D[1506] = (d1506, "A beacon lies outside the square room: slide along one wall, get blocked, drop the wall that no longer pushes, slide again, and park at the corner nearest it.")

OM = lambda x: 36 + 78 * math.exp(-(x - 50) / 55)

def d1601(c):
    om = OM
    return svg(c, L(34, 128, 226, 128, 1.2, ar=True), L(70, 132, 70, 10, 1.2, d="4 3"), fn(om, 50, 222, 40, 2.6),
        L(70, 78, 190, 126, 1.6), dot(120, om(120), None, r=3), plane(128, om(120) - 14, 20, .6),
        dot(70, 78, "φ(μ)", -6, 4, 9, "end", 2.8), dot(70, om(70), "p*", -6, 4, 9, "end", 2.5), N(214, 20, "ω(z)", 10, "end", "bold"), N(214, 140, "z (wall position)", 8, "end"),
        N(190, 110, "slope −μ", 8.5, "start"))
D[1601] = (d1601, "Move the wall by z and record the lowest legal altitude ω(z). A flat ruler of slope −μ pushed up from underneath touches ω; where it crosses z=0 is the dual value φ(μ).")

def d1602(c):
    return svg(c, L(20, 54, 150, 54, 3), N(156, 50, "p*", 10, "start", "bold"),
        plane(60, 42, 0, .7), L(20, 84, 150, 84, 1.4, d="5 3"), L(20, 106, 150, 106, 1.4, d="5 3"), L(20, 124, 150, 124, 1.4, d="5 3"),
        N(156, 88, "q(μ) ≤ p*", 8.5, "start"), arrow(40, 124, 40, 90, 1.6), N(160, 128, "raise the floor", 8.5, "start"),
        arrow(120, 82, 120, 58, 1.2, d="2 2"), N(130, 72, "gap", 8.5, "start"), N(120, 12, "dual floors can never pass the true floor", 8.5, "middle", "bold"))
D[1602] = (d1602, "Every wall price μ builds a floor q(μ) beneath the lowest legal altitude p*. The best floor can never rise above it, and the leftover distance is the duality gap.")

def d1603(c):
    return svg(c, L(20, 76, 220, 76, 3), plane(120, 36, 90, .9), arrow(120, 48, 120, 70, 2.2), arrow(120, 124, 120, 82, 2.2),
        N(130, 108, "dual floor rises", 8.5, "start"), N(130, 36, "primal descends", 8.5, "start"), N(120, 138, "p* = q*   gap = 0", 9, "middle", "bold"), N(34, 70, "meet", 8.5, "start"))
D[1603] = (d1603, "Under convexity and Slater's room to move, the pilot descending from above and the tower raising a floor from below meet at the same altitude.")

def d1604(c):
    h = lambda x: 112 - 80 * (1 - ((x - 120) / 100) ** 2)
    dh = lambda x: 160 * (x - 120) / 100 ** 2
    parts = [L(20, 128, 224, 128, 1.2, ar=True)]
    for x0 in (50, 88, 130, 176):
        a, b = 20, 222
        y0 = h(x0); m = dh(x0)
        parts.append(L(a, f(y0 + m * (a - x0)), b, f(y0 + m * (b - x0)), 1))
    parts += [fn(h, 30, 214, 40, 2.8), N(120, 12, "each plan x gives a straight line in μ", 8.5, "middle", "bold"), N(120, 142, "lowest of all lines = concave q(μ)", 8.5), plane(196, 40, 0, .6)]
    return svg(c, *parts)
D[1604] = (d1604, "For each fixed flight plan x, 'altitude + μ × wall violation' is a straight line in μ. The lowest of all those lines is always a concave arch.")

def d1605(c):
    om = OM
    x0 = 90
    y0 = om(x0); m = -78 / 55 * math.exp(-(x0 - 50) / 55)
    return svg(c, L(34, 128, 226, 128, 1.2, ar=True), fn(om, 50, 222, 40, 2.6), L(60, f(y0 + m * (60 - x0)), 190, f(y0 + m * (190 - x0)), 1.6, d="5 3"),
        dot(x0, y0, "z=0", -2, -10, 9, "middle", 3), plane(x0 - 18, y0 - 18, 20, .55), dash(x0, y0 + 2, x0 + 40, y0 + 2, 1.2, "2 2"), dash(x0 + 40, y0 + 2, x0 + 40, y0 + 2 + m * 40, 1.2, "2 2"),
        N(150, y0 + 34, "Δz = +1", 8.5, "middle"), N(206, 60, "ω drops by μ*", 8.5, "end", "bold"), N(120, 142, "multiplier = shadow price", 8.5, "middle", "bold"))
D[1605] = (d1605, "Slide the wall back by Δz: the lowest legal altitude falls along the tangent of slope −μ*, so μ* prices one unit of extra airspace.")

def d1606(c):
    parts = [R(90, 10, 60, 124, "#eef0f4", 1.2, 0, "4 3"), L(90, 10, 90, 134, 1.6), L(150, 10, 150, 134, 1.6), L(120, 10, 120, 134, 1.4, d="6 3"),
             arrow(92, 70, 148, 70, 1.4), arrow(148, 70, 92, 70, 1.4), N(120, 64, "margin", 8.5, "middle", "bold"), N(120, 84, "2/‖w‖", 8.5)]
    for (x, y) in [(88, 38), (88, 104), (50, 70), (36, 112), (60, 26)]:
        parts.append(plane(x - 8, y, 0, .5))
    for (x, y) in [(152, 52), (152, 112), (190, 86), (208, 38), (180, 124)]:
        parts.append(plane(x + 8, y, 180, .5))
    parts += [N(46, 140, "eastbound", 8, "middle"), N(194, 140, "westbound", 8, "middle")]
    return svg(c, *parts)
D[1606] = (d1606, "Two opposing traffic flows: the widest no-fly strip between them has a width set only by the planes nearest its edges, so maximising the margin means minimising ½‖w‖².")

def d1608(c):
    parts = [L(90, 10, 90, 134, 1.6), L(150, 10, 150, 134, 1.6), L(120, 10, 120, 134, 1.2, d="6 3")]
    for (x, y, sv) in [(88, 38, True), (88, 104, True), (50, 70, False), (36, 112, False), (60, 26, False)]:
        parts.append(plane(x - 8, y, 0, .5))
        parts.append(N(x - 8, y - 10, "α>0" if sv else "α=0", 7.5, "middle", "bold" if sv else "normal"))
    for (x, y, sv) in [(152, 52, True), (152, 112, True), (190, 86, False), (208, 38, False), (180, 124, False)]:
        parts.append(plane(x + 8, y, 180, .5))
        parts.append(N(x + 8, y - 10, "α>0" if sv else "α=0", 7.5, "middle", "bold" if sv else "normal"))
    parts += [N(120, 144, "only planes on the edges carry weight", 7.5, "middle")]
    return svg(c, *parts)
D[1608] = (d1608, "Only the planes touching the edges of the strip (support vectors, α>0) carry weight; every other plane has α=0 and could be removed without moving the strip.")

FIX = {cid: {"drawingSvg": fnc(cid), "drawingCaption": cap} for cid, (fnc, cap) in D.items()}
