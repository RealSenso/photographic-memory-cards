"""CMO figures redrawn as airplane side views with curves (no contour lines, no textbook scans).
Each figure is one picture the user can copy by hand: ground = a curve, the plane flies over it."""
import math
from air_lib import *

W = 240

def g(f, x0, x1, step=3):
    return [(x, f(x)) for x in range(int(x0), int(x1) + 1, step)]

def bowl(cx, by, half, depth):
    """U-shaped ground: bottom at (cx, by), walls rise by `depth` over `half` pixels"""
    return lambda x: by - depth * ((x - cx) / half) ** 2

def tangent(f, x, h=0.5):
    return (f(x + h) - f(x - h)) / (2 * h)

def tline(f, x, a, b, w=1.1, d="4 3"):
    s = tangent(f, x)
    return dash(x - a, f(x) - a * s, x + b, f(x) + b * s, w, d)

def dir_(f, x, sign=1):
    s = tangent(f, x); n = math.hypot(1, s)
    return sign / n, sign * s / n

D = {}

def pg(pts, fill="#e5e7eb", w=1.8):
    return PG(" ".join(f"{x:.1f},{y:.1f}" for x, y in pts), fill, w)

# ---------- 1 · 2 · 3: foundations ----------
def d105(c):
    f = bowl(120, 112, 95, 80)
    pts = g(f, 25, 215)
    sky = pg(pts + [(215, 26), (25, 26)], "#e5e7eb", 0)
    xa, xb = 55, 190
    return svg(c, sky, poly(pts, 2.4), L(f"{xa}", f"{f(xa):.1f}", f"{xb}", f"{f(xb):.1f}", 1.6),
        dot(xa, f(xa), None, r=2.6), dot(xb, f(xb), None, r=2.6), plane(122, 60, 0, .75),
        N(120, 14, "epigraph = all the sky on or above the ground", 8.5, "middle", "bold"),
        N(120, 128, "convex ground: a straight flight between two", 8, "middle"),
        N(120, 139, "points on the ground never leaves the sky", 8, "middle"))
D[105] = (d105, "Shade everything on or above the ground: that is the epigraph. The ground is convex exactly when the shaded sky is convex: a straight flight between any two ground points stays in the sky.")

def d202(c):
    f = bowl(120, 108, 95, 75)
    xa = 55
    return svg(c, poly(g(f, 25, 215), 2.4), dash(88, 108, 152, 108, 1.4, "4 3"), plane(120, 96, 0, .8), dot(120, 108, None, r=2.6),
        N(120, 124, "at the bottom the slope gauge reads 0: ∇f(x*) = 0", 8.5, "middle", "bold"),
        tline(f, xa, 14, 18), plane(xa, f(xa) - 12, math.degrees(math.atan(tangent(f, xa))), .6),
        N(xa - 4, f(xa) + 16, "slope ≠ 0: still", 7.5, "middle"), N(xa - 4, f(xa) + 25, "a way down", 7.5, "middle"),
        N(120, 14, "first-order test: flat floor under the plane", 8.5, "middle"))
D[202] = (d202, "On a slope the gauge is not zero, so there is still a way down. At the bottom of the valley the ground under the plane is flat: ∇f(x*) = 0.")

def d301(c):
    f = bowl(120, 110, 100, 80)
    xa, xb, t = 45, 200, .4
    xm = xa + t * (xb - xa); ym = f(xa) + t * (f(xb) - f(xa))
    return svg(c, poly(g(f, 22, 220), 2.4), L(f"{xa}", f"{f(xa):.1f}", f"{xb}", f"{f(xb):.1f}", 1.6, d="5 3"),
        dot(xa, f(xa), "x", -6, 2, 10, "end", 2.6), dot(xb, f(xb), "y", 6, 2, 10, "start", 2.6),
        plane(xm, ym - 9, math.degrees(math.atan((f(xb) - f(xa)) / (xb - xa))), .7),
        L(f"{xm:.1f}", f"{ym + 4:.1f}", f"{xm:.1f}", f"{f(xm) - 3:.1f}", 1.1, ar=True), dot(xm, f(xm), None, r=2.4),
        N(xm + 5, (ym + f(xm)) / 2 + 3, "string above ground", 7.5, "start"),
        N(120, 14, "convex: the string between two ground points", 8.5, "middle", "bold"),
        N(120, 25, "is never below the ground", 8.5, "middle", "bold"),
        N(120, 132, "f(λx + (1−λ)y) ≤ λf(x) + (1−λ)f(y)", 8.5, "middle"))
D[301] = (d301, "Stretch a string between two points on the ground. On convex terrain the string (a straight flight) is never below the ground anywhere in between.")

def d302(c):
    f = bowl(120, 108, 100, 80)
    x = 70; s = tangent(f, x)
    yb = 185
    return svg(c, poly(g(f, 22, 220), 2.4), L(f"{x - 50}", f"{f(x) - 50 * s:.1f}", f"{x + 150}", f"{f(x) + 150 * s:.1f}", 1.6, d="6 3"),
        plane(x, f(x) - 11, math.degrees(math.atan(s)), .75), dot(x, f(x), "x", -6, 12, 10, "end", 2.6),
        dot(yb, f(yb), "y", 6, -2, 10, "start", 2.4), L(f"{yb}", f"{f(yb) + 3:.1f}", f"{yb}", f"{f(x) + (yb - x) * s - 3:.1f}", 1.1, ar=True),
        N(yb - 4, 124, "ground stays above", 7.5, "end"), N(yb - 4, 133, "the glide line", 7.5, "end"),
        N(120, 14, "the glide line at your spot never cuts the ground", 8.5, "middle", "bold"),
        N(70, 140, "f(y) ≥ f(x) + ∇f(x)ᵀ(y − x)", 8.5, "middle"))
D[302] = (d302, "Draw the glide line (tangent) at the plane's position. On convex terrain the ground is above it everywhere, so the tangent is a guaranteed underestimate of the altitude.")

# ---------- 4 · 5 · 6 ----------
def d403(c):
    ox, oy = 26, 120
    h = lambda a: 70 * ((a - 130) / 100) ** 2          # altitude above the floor along the heading
    y = lambda a: oy - 12 - h(a)
    s0 = (y(ox + .5) - y(ox - .5))
    arm = lambda a: y(ox) + .25 * s0 * (a - ox)
    a1 = max(a for a in range(ox + 1, 228) if y(a) >= arm(a))
    return svg(c, L(ox, oy, 232, oy, 1.2, ar=True), N(235, oy + 3, "α", 9, "start"), poly(g(y, ox, 228), 2.4),
        dash(ox, y(ox), ox + 28, y(ox) + 28 * s0, 1.1, "2 2"), N(ox + 24, y(ox) + 28 * s0 + 12, "full slope", 7.5, "middle"),
        L(f"{ox}", f"{y(ox):.1f}", "220", f"{arm(220):.1f}", 1.4, d="6 3"), N(222, arm(220) + 12, "Armijo line", 7.5, "end"),
        plane(ox + 6, y(ox) - 12, 30, .6), L(f"{ox + 1}", f"{oy + 8}", f"{a1}", f"{oy + 8}", 2.6),
        dash(a1, arm(a1), a1, oy + 8), N((ox + a1) / 2, oy + 19, "accepted: ends below the Armijo line", 8, "middle", "bold"),
        N(130, 12, "a hop must earn a fraction c₁ of the promised drop", 8, "middle"))
D[403] = (d403, "Flying along the heading, the altitude φ(α) first drops at the full slope. Armijo draws a shallower line (a fraction c₁ of that slope): a hop is accepted only if the altitude ends up below that line.")

def d504(c):
    ox, oy = 30, 112
    xs = lambda k: ox + (math.log10(k) / 2.3) * 190
    r = lambda k: ((k - 1) / (k + 1)) ** 2
    ys = lambda v: oy - v * 86
    pts = [(xs(10 ** (i / 40)), ys(r(10 ** (i / 40)))) for i in range(0, 93)]
    parts = [L(ox, oy, 228, oy, 1.2, ar=True), L(ox, oy, ox, 18, 1.2, ar=True), N(228, oy + 11, "κ (canyon thinness)", 7.5, "end"),
        N(ox + 3, 16, "shrink per hop", 7.5, "start"), dash(ox, ys(1), 226, ys(1)), N(226, ys(1) - 3, "1 = no progress", 7, "end"),
        poly(pts, 2.4)]
    for k, lab, dx in ((1, "round bowl: one hop", 6), (10, "κ=10", 6), (100, "κ=100: crawl", -6)):
        x, y = xs(k), ys(r(k)); parts += [dot(x, y, None, r=2.6), N(x + dx, y + (12 if k == 1 else -6), lab, 7.5, "start" if dx > 0 else "end")]
    parts += [plane(xs(100) - 8, ys(r(100)) - 22, 0, .6), N(130, 132, "worst-case shrink = ((κ−1)/(κ+1))²", 8.5, "middle", "bold")]
    return svg(c, *parts)
D[504] = (d504, "Kantorovich's bound: each steepest-descent hop shrinks the altitude gap by at most ((κ−1)/(κ+1))². A round bowl (κ = 1) needs one hop; a thin canyon (large κ) gives a factor close to 1, so the pilot crawls.")

def d601(c):
    base = 122
    h = lambda x: 20 + 62 * ((x - 150) / 110) ** 2 + 5 * math.sin(x / 14)
    y = lambda x: base - h(x)
    xk = 52; s = (h(xk + .5) - h(xk - .5)); cv = h(xk + 1) - 2 * h(xk) + h(xk - 1)
    cv = max(cv, .008)
    m = lambda x: h(xk) + s * (x - xk) + .5 * cv * (x - xk) ** 2
    xn = xk - s / cv
    ym = lambda x: base - m(x)
    lo, hi = max(14, xn - 80), min(230, xn + 80)
    return svg(c, poly(g(y, 14, 230), 2.4), poly([(x, ym(x)) for x in range(int(lo), int(hi), 3) if ym(x) > 30], 1.4, "5 3"),
        plane(xk, y(xk) - 12, -math.degrees(math.atan(s)), .7), dot(xk, y(xk), "xₖ", -6, 12, 9.5, "end", 2.6),
        dot(xn, ym(xn), None, r=2.6), L(f"{xk + 8}", f"{y(xk) - 6:.1f}", f"{xn - 4:.1f}", f"{ym(xn) - 5:.1f}", 1.6, ar=True),
        dash(xn, ym(xn) + 3, xn, y(xn) - 3, 1, "2 2"), N(xn - 6, ym(xn) + 4, "model bottom", 7.5, "end"),
        N(120, 12, "fit a parabola with slope + curvature (dashed)", 8.5, "middle", "bold"),
        N(120, 24, "and fly straight to its bottom", 8.5, "middle", "bold"),
        N(120, 140, "xₖ₊₁ = xₖ − (∇²f)⁻¹ ∇f", 8.5, "middle"))
D[601] = (d601, "Newton's autopilot reads the slope and the curvature at xₖ, fits a parabola (dashed) to the terrain there, and flies straight to the bottom of that parabola.")

# ---------- 8 ----------
def d801(c):
    f = bowl(140, 110, 110, 85)
    xa, xb = 55, 105
    return svg(c, poly(g(f, 30, 230), 2.4), tline(f, xa, 18, 22), tline(f, xb, 22, 22),
        plane(xa, f(xa) - 12, math.degrees(math.atan(tangent(f, xa))), .6), plane(xb, f(xb) - 12, math.degrees(math.atan(tangent(f, xb))), .6),
        dot(xa, f(xa), None, r=2.4), dot(xb, f(xb), None, r=2.4), N(xa - 6, f(xa) + 14, "slope gₖ", 8, "end"), N(xb + 6, f(xb) + 14, "slope gₖ₊₁", 8, "start"),
        L(xa, 124, xb, 124, 1.2, ar=True), N((xa + xb) / 2, 135, "s = step flown", 8, "middle"),
        N(120, 12, "the flight log measures curvature for free", 8.5, "middle", "bold"),
        N(178, 34, "y = gₖ₊₁ − gₖ", 8.5, "middle"), N(178, 46, "curvature ≈ y / s", 8.5, "middle"), N(178, 58, "secant: B s = y", 8.5, "middle", "bold"))
D[801] = (d801, "Two slope readings, one hop apart: how much the slope changed (y) over the distance flown (s) is a curvature reading. The secant equation B s = y asks the curvature model to agree with it.")

# ---------- 10 · 11 · 12 ----------
def d1001(c):
    A = [(30, 40), (78, 28), (96, 70), (60, 104), (28, 86)]
    B = [(150, 50), (204, 34), (222, 92), (176, 116), (140, 92)]
    return svg(c, pg(A, "#e5e7eb", 1.8), pg(B, "#e5e7eb", 1.8), L(118, 10, 122, 130, 2.6),
        plane(60, 68, 0, .75), plane(184, 76, 180, .75), N(60, 120, "airspace A", 8.5, "middle"), N(184, 132, "airspace B", 8.5, "middle"),
        arrow(120, 60, 142, 59, 1.4), N(146, 62, "a", 9, "start", "bold"),
        N(120, 140, "one flat wall: aᵀx ≤ b on A's side, ≥ b on B's", 8, "middle"))
D[1001] = (d1001, "Two convex airspaces that do not overlap can always be split by one flat wall: everything in A lies on one side of aᵀx = b, everything in B on the other.")

def d1101(c):
    f = lambda x: 30 + (x - 14) * .5
    wx = 150
    return svg(c, poly(g(f, 14, wx), 2.4), L(wx, 16, wx, 112, 2.6), *[L(wx, y, wx + 6, y + 5, 1) for y in range(20, 110, 10)],
        N(wx + 9, 24, "wall", 8, "start"),
        plane(wx - 14, f(wx - 14) - 10, math.degrees(math.atan(.5)), .8), dot(wx - 2, f(wx - 2), None, r=2.6),
        arrow(60, 38, 84, 50, 2), N(58, 34, "gravity −∇f", 8, "end"),
        arrow(wx - 3, 70, wx - 30, 70, 2), N(wx - 4, 63, "wall push μ∇g", 8, "end"),
        N(120, 10, "parked against the wall: the forces balance", 8.5, "middle", "bold"),
        N(14, 118, "1. ∇f + μ∇g = 0 (balance)", 7.5, "start"), N(14, 129, "2. g(x) ≤ 0 (legal)", 7.5, "start"),
        N(130, 118, "3. μ ≥ 0 (walls only push)", 7.5, "start"), N(130, 129, "4. μg = 0 (push only if touching)", 7.5, "start"))
D[1101] = (d1101, "The plane rolls downhill until a wall stops it. At rest, gravity (−∇f) is balanced by the wall's push (μ∇g). That balance, being legal, a wall that only pushes, and 'only a touching wall pushes' are the four KKT conditions.")

def d1201(c):
    up = bowl(62, 92, 48, 50)
    dn = lambda x: 52 + 40 * ((x - 180) / 48) ** 2
    return svg(c, poly(g(up, 14, 110), 2.4), plane(62, 80, 0, .7), dot(62, 92, None, r=2.4),
        poly(g(dn, 132, 228), 2.4, "5 3"), plane(180, 40, 0, .7), dot(180, 52, None, r=2.4), L(122, 10, 122, 140, .8, d="2 3"),
        N(62, 14, "along the runway", 8.5, "middle", "bold"), N(62, 112, "must curve up ✓", 8, "middle"), N(62, 123, "(tangent directions M)", 7.5, "middle"),
        N(180, 14, "across the runway", 8.5, "middle", "bold"), N(180, 112, "may curve down:", 8, "middle"), N(180, 123, "illegal, ignored", 7.5, "middle"),
        N(120, 139, "test dᵀ∇²L d ≥ 0 only for d on the runway", 8, "middle"))
D[1201] = (d1201, "Second-order test with walls: only the directions you can legally fly (along the runway, the tangent subspace M) must curve upward. Across the runway the terrain may curve down; you can't go there, so it doesn't count.")

# ---------- 14 · 16 · 19 ----------
def d1401(c):
    wall = [L(20, 96, 220, 60, 2.6)] + [L(f"{20 + i * 20}", f"{96 - i * 3.6:.1f}", f"{26 + i * 20}", f"{104 - i * 3.6:.1f}", 1) for i in range(10)]
    xk = (70, 87); out = (150, 112); px = (145, 73.9)
    return svg(c, *wall, N(214, 80, "rock", 8, "end"), plane(xk[0] - 12, xk[1] - 12, 20, .7), dot(*xk, "xₖ", -2, 13, 9.5, "middle", 2.6),
        L(xk[0] + 3, xk[1] + 3, out[0] - 4, out[1] - 1, 1.6, d="5 3", ar=True), dot(*out, None, r=2.4), N(out[0] + 6, out[1] + 4, "xₖ − α∇f (inside the rock)", 7.5, "start"),
        L(out[0], out[1] - 4, px[0] + 1, px[1] + 5, 1.4, ar=True), dot(*px, "xₖ₊₁ = P(·)", 4, -8, 9, "start", 2.6),
        N(120, 14, "step downhill; if you end up in the rock,", 8.5, "middle", "bold"), N(120, 26, "drop back to the nearest legal point", 8.5, "middle", "bold"),
        N(120, 140, "xₖ₊₁ = P(xₖ − α∇f(xₖ))", 8.5, "middle"))
D[1401] = (d1401, "Projected gradient: fly the ordinary downhill hop; if it ends inside the rock, drop straight back onto the nearest legal point.")

def omega_axes(ox, oy, x1, top):
    return [L(ox - 4, oy, x1, oy, 1.2, ar=True), L(ox + 40, oy + 4, ox + 40, top, 1.2, ar=True)]

def d1601(c):
    ox, oy = 20, 116
    w = lambda z: 40 + 26 * math.exp(-(z - 40) / 40) * 1.4 - 12
    zc = ox + 40
    s = tangent(w, zc)
    return svg(c, *omega_axes(ox, oy, 228, 14), N(228, oy + 11, "z: move the wall by z", 7.5, "end"), poly(g(w, ox + 4, 226), 2.4),
        L(f"{ox}", f"{w(zc) - 40 * s + 6:.1f}", "226", f"{w(zc) + (226 - zc) * s + 6:.1f}", 1.4, d="6 3"),
        dot(zc, w(zc), None, r=2.6), dot(zc, w(zc) + 6, None, r=2.2), plane(zc + 8, w(zc) - 12, math.degrees(math.atan(s)), .6),
        N(zc + 5, w(zc) + 18, "ruler height at z=0 = dual value q(μ)", 7.5, "start"),
        N(170, 80, "ω(z) = lowest altitude", 8, "middle"), N(170, 91, "if the wall moves by z", 8, "middle"),
        N(120, 140, "slope of the ruler = −μ (the wall's price)", 8, "middle"))
D[1601] = (d1601, "ω(z) is the best altitude the pilot can reach when the wall is moved by z. Slide a straight ruler under that curve: its height at z = 0 is the dual value, and its slope is −μ.")

def d1603(c):
    a = lambda z: 92 - 1.1 * (z - 20) + .012 * (z - 20) ** 2
    zc = 55; s = tangent(a, zc)
    b = lambda z: 80 - .9 * (z - 130) + 30 * math.exp(-((z - 178) / 12) ** 2) * -1 + .01 * (z - 130) ** 2
    return svg(c, L(16, 120, 110, 120, 1.2, ar=True), L(55, 124, 55, 14, 1, d="2 3"), poly(g(a, 18, 108), 2.4),
        L(f"{18}", f"{a(zc) - 37 * s:.1f}", "108", f"{a(zc) + 53 * s:.1f}", 1.3, d="6 3"), dot(zc, a(zc), None, r=2.6), plane(zc + 8, a(zc) - 13, math.degrees(math.atan(s)), .55),
        N(62, 14, "convex + Slater", 8.5, "middle", "bold"), N(62, 134, "ruler touches at z=0: gap 0", 7.5, "middle"),
        L(124, 10, 124, 140, .8, d="2 3"),
        L(134, 120, 230, 120, 1.2, ar=True), L(178, 124, 178, 14, 1, d="2 3"), poly(g(b, 136, 228), 2.4),
        L("136", f"{b(136) + 4:.1f}", "228", f"{b(228) + 4:.1f}", 1.3, d="6 3"), dot(178, b(178), None, r=2.6),
        L(178, f"{b(178) + 3:.1f}", 178, f"{b(136) + 4 + (178 - 136) * (b(228) - b(136)) / 92 - 1:.1f}", 1.2, ar=True),
        N(182, 14, "bump in ω(z)", 8.5, "middle", "bold"), N(182, 134, "ruler can't reach: gap > 0", 7.5, "middle"))
D[1603] = (d1603, "Left: with convexity and Slater's room, the ruler under ω(z) touches it exactly at z = 0, so the dual value equals the true lowest altitude. Right: a bump in ω(z) keeps the ruler below, leaving a duality gap.")

def d1901(c):
    wx, base = 120, 124
    h = lambda x: 86 - (x - 14) * .3
    parts = [L(wx, 18, wx, 120, 1.6, d="4 3"), N(wx, 14, "wall x = b", 8, "middle"), L(14, 120, 230, 120, 1.2)]
    for cc, lab in ((.004, "c small"), (.02, "c medium"), (.14, "c huge")):
        y = lambda x, cc=cc: base - (h(x) + (cc * (x - wx) ** 2 if x > wx else 0))
        xs = [x for x in range(14, 232, 2) if y(x) > 18]
        parts += [poly([(x, y(x)) for x in xs], 2.2 if cc > .1 else 1.4, None if cc > .1 else "5 3")]
        xm = max(range(wx, 232), key=y); parts += [dot(xm, y(xm), None, r=2.2), N(xs[-1] + 2, y(xs[-1]) + 3, lab, 7, "start")]
    parts += [plane(wx - 30, base - h(wx - 30) - 10, 17, .6), N(170, 120 - 4, "", 7, "middle"),
        N(60, 64, "ground keeps falling", 8, "middle"), N(60, 75, "past the wall", 8, "middle"),
        N(120, 136, "fine c·(violation)²: bigger c, stops closer to the wall", 8, "middle")]
    return svg(c, *parts)
D[1901] = (d1901, "Past the wall the ground would keep falling, so add a fine c·(violation)². With a small c the plane stops well past the wall. As c grows the fine bends the ground up faster, and the resting point slides toward the wall.")

def d1902(c):
    wx, base = 200, 124
    h = lambda x: 80 - (x - 14) * .25
    parts = [L(wx, 18, wx, 122, 2.6)] + [L(wx, y, wx + 6, y + 5, 1) for y in range(22, 120, 10)] + [N(wx + 8, 30, "wall", 8, "start"), L(14, 122, wx, 122, 1.2)]
    for mu, lab in ((14, "μ big"), (5, "μ medium"), (1.4, "μ small")):
        y = lambda x, mu=mu: base - (h(x) - mu * math.log((wx - x) / 186))
        xs = [x for x in range(14, wx) if 18 < y(x) < 122]
        parts += [poly([(x, y(x)) for x in xs], 2.2 if mu < 2 else 1.4, None if mu < 2 else "5 3")]
        xm = max(range(14, wx), key=y); parts += [dot(xm, y(xm), None, r=2.2), N(xm - 5, y(xm) + {14: -6, 5: 2, 1.4: 11}[mu], lab, 7, "end")]
    parts += [plane(60, base - h(60) - 12, 14, .6), N(110, 12, "barrier −μ·log(distance to wall) blows up at the wall", 8, "middle", "bold"),
        N(110, 136, "the plane never touches the wall; as μ → 0 it creeps closer", 7.8, "middle")]
    return svg(c, *parts)
D[1902] = (d1902, "A barrier adds −μ·log(distance to the wall), which shoots up to infinity at the wall, so the plane can never touch it. As μ shrinks, the resting point creeps toward the wall from inside.")

# ---------- contour rings replaced by curves ----------
def d501(c):
    f = bowl(140, 116, 115, 80)
    x = 64; ux, uy = dir_(f, x)
    return svg(c, poly(g(f, 22, 230), 2.4), tline(f, x, 22, 22), dot(x, f(x), "xₖ", -6, 13, 9.5, "end", 2.6),
        plane(x, f(x) - 13, math.degrees(math.atan2(uy, ux)), .75),
        arrow(x - 4 * ux, f(x) - 4 * uy + 6, x - 30 * ux, f(x) - 30 * uy + 6, 1.4), N(x - 30 * ux - 3, f(x) - 30 * uy + 14, "∇f: steepest up", 8, "end"),
        arrow(x + 12 * ux, f(x) + 12 * uy - 8, x + 44 * ux, f(x) + 44 * uy - 8, 2.6), N(x + 44 * ux + 4, f(x) + 44 * uy - 10, "dₖ = −∇f", 9, "start", "bold"),
        N(120, 12, "point the nose exactly opposite the uphill gauge", 8.5, "middle", "bold"),
        N(140, 132, "simple, but blind to the valley's curvature", 8, "middle"))
D[501] = (d501, "The slope gauge ∇f points to steepest uphill. Steepest descent points the nose exactly the other way, dₖ = −∇f. It only looks at the slope, never at how the valley curves.")

def canyon_bounce(f, cx, xs):
    """zig-zag of an exact line search seen in the canyon's cross-section: hops alternate wall to wall"""
    pts = [(x, f(x)) for x in xs]
    out = [poly(pts, 1.6, "4 2")]
    out += [dot(x, y, None, r=2.2) for x, y in pts]
    for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
        out.append(arrow(x1 + (x2 - x1) * .55, y1 + (y2 - y1) * .55, x1 + (x2 - x1) * .62, y1 + (y2 - y1) * .62, 1.6))
    return out

def d508(c):
    f = bowl(120, 116, 70, 80)
    xs = [56, 178, 72, 160, 88, 144, 104, 130]
    return svg(c, poly(g(f, 50, 190), 2.4), *canyon_bounce(f, 120, xs), plane(56, f(56) - 12, 30, .7), N(56 - 8, f(56) + 4, "x₀", 9.5, "end"),
        N(120, 12, "seen across the canyon: each hop stops where", 8.5, "middle", "bold"), N(120, 24, "it is flat, the next turns 90° → wall to wall", 8.5, "middle", "bold"),
        N(120, 132, "exact line search: gₖ₊₁ ⊥ gₖ, so the path zig-zags", 8, "middle"))
D[508] = (d508, "Look at the canyon from its end. Each exact hop flies until the ground along it is flat, which happens on the opposite wall; the next heading is at 90°, so the plane bounces wall to wall while creeping down.")

def d505(c):
    wide = bowl(58, 108, 48, 50)
    thin = bowl(176, 112, 22, 90)
    return svg(c, poly(g(wide, 12, 104), 2.4), L(30, wide(30), 56, wide(56), 2.2, ar=True), dot(30, wide(30), None, r=2.4), plane(30, wide(30) - 12, 30, .6),
        N(58, 14, "κ ≈ 1: round bowl", 8.5, "middle", "bold"), N(58, 124, "one hop to the bottom", 8, "middle"),
        L(122, 10, 122, 140, .8, d="2 3"),
        poly(g(thin, 154, 198, 1), 2.4), *canyon_bounce(thin, 176, [157, 194, 160, 191, 163, 188, 166, 185, 170, 181]),
        plane(157, thin(157) - 10, 40, .55), N(182, 14, "κ large: thin canyon", 8.5, "middle", "bold"), N(182, 124, "bounces, crawls down", 8, "middle"),
        N(120, 139, "κ = steepest wall ÷ gentlest floor curvature", 7.8, "middle"))
D[505] = (d505, "Cross-sections of two valleys. In a round bowl (κ ≈ 1) one steepest-descent hop reaches the bottom. In a thin canyon (large κ) the walls are much steeper than the floor, so the plane bounces wall to wall and crawls.")

def d507(c):
    f1 = bowl(60, 110, 46, 80); f2 = bowl(180, 110, 46, 80)
    return svg(c, poly(g(f1, 14, 106), 2.4), *canyon_bounce(f1, 60, [22, 98, 26, 94, 30, 90, 34, 86]), plane(22, f1(22) - 10, 30, .55),
        N(60, 14, "no momentum", 8.5, "middle", "bold"), N(60, 124, "keeps bouncing", 8, "middle"),
        L(120, 10, 120, 140, .8, d="2 3"),
        poly(g(f2, 134, 226), 2.4), *canyon_bounce(f2, 180, [142, 206, 166, 190, 178]), plane(142, f2(142) - 10, 30, .55),
        N(180, 14, "heavy-ball momentum", 8.5, "middle", "bold"), N(180, 124, "bounces die out fast", 8, "middle"),
        N(120, 139, "xₖ₊₁ = xₖ − α∇f + β(xₖ − xₖ₋₁)", 8, "middle"))
D[507] = (d507, "Across the canyon: plain steepest descent keeps bouncing wall to wall. A heavy plane carries part of its last hop (momentum β), the side-to-side swings cancel, and it settles to the floor quickly.")

def slice_(cx, by, half, depth, px, lab, ok):
    f = bowl(cx, by, half, depth)
    out = [poly(g(f, cx - half, cx + half), 2.2), plane(px, f(px) - 10, math.degrees(math.atan(tangent(f, px))), .55), dot(px, f(px), None, r=2.2)]
    if px != cx: out += [dot(cx, f(cx), None, r=1.6), N(cx, f(cx) + 11, "bottom", 7, "middle")]
    out += [N(cx, by - depth - 8, lab, 8, "middle", "bold")]
    return out

def mini(cx, by, half, depth, px):
    f = bowl(cx, by, half, depth)
    return [poly(g(f, cx - half, cx + half, 2), 2), dot(cx, f(cx), None, r=1.6), plane(px, f(px) - 8, math.degrees(math.atan(tangent(f, px))), .45), dot(px, f(px), None, r=2.2)]

def d701(c):
    oy = 104
    h = lambda a: 58 * ((a - 70) / 58) ** 2 + 6
    y = lambda a: oy - h(a)
    s0 = y(12.5) - y(11.5)
    return svg(c, N(60, 11, "one hop along heading dₖ", 8.5, "middle", "bold"),
        L(10, oy, 116, oy, 1.2, ar=True), N(116, oy + 10, "α", 8.5, "end"), poly(g(y, 12, 116, 2), 2.4),
        plane(16, y(12) - 9, 60, .55), dash(12, y(12), 26, y(12) + 14 * s0, 1.2, "2 2"),
        N(30, 40, "slope gₖᵀdₖ < 0", 7.5, "start", "bold"), N(30, 49, "(downward momentum)", 7, "start"),
        N(70, 64, "curvature dₖᵀQdₖ", 7.5, "middle", "bold"), N(70, 73, "(the brakes)", 7, "middle"),
        dot(70, y(70), None, r=2.6), dash(70, y(70) + 3, 70, oy), N(70, oy + 10, "αₖ", 9, "middle", "bold"),
        N(62, 128, "αₖ = −gₖᵀdₖ / dₖᵀQdₖ", 8.5, "middle", "bold"), N(60, 139, "rₖ = −gₖ: radar's downhill reading", 7, "middle"),
        L(122, 4, 122, 142, .8, d="2 3"),
        N(180, 10, "after hop dⱼ,", 7.8, "middle", "bold"), N(180, 19, "slice along old dᵢ", 7.8, "middle", "bold"),
        *mini(148, 62, 20, 30, 160), N(174, 38, "dᵢᵀQdⱼ ≠ 0 ✗", 8, "start", "bold"), N(174, 49, "pushed off the", 7, "start"), N(174, 58, "dᵢ bottom", 7, "start"),
        *mini(148, 112, 20, 30, 148), N(174, 88, "dᵢᵀQdⱼ = 0 ✓", 8, "start", "bold"), N(174, 99, "still at the", 7, "start"), N(174, 108, "dᵢ bottom", 7, "start"),
        N(180, 136, "Q-conjugate = 'no crosswind'", 7, "middle"))
D[701] = (d701, "Left: slice the valley along the heading dₖ. The starting slope gₖᵀdₖ is the downward momentum, the curvature dₖᵀQdₖ is the brakes, and the bottom of the slice is at αₖ = −gₖᵀdₖ / dₖᵀQdₖ. Right: after flying dⱼ, look along an old heading dᵢ. If dᵢᵀQdⱼ = 0 the plane is still at the bottom of that slice; otherwise hop j undid hop i.")

def d702(c):
    parts = [N(120, 11, "xₖ = lowest point of the flight plane x₀ + 𝓑ₖ", 8.5, "middle", "bold")]
    for i, cx in enumerate((42, 120, 198)):
        f = bowl(cx, 84, 30, 42)
        parts += [poly(g(f, cx - 30, cx + 30, 2), 2.2), plane(cx, 72, 0, .5), dot(cx, 84, None, r=2.4), dash(cx - 18, 84, cx + 18, 84, 1.2, "3 2"),
            N(cx, 30, f"slice along d{'₀₁₂'[i]}", 8, "middle", "bold"), N(cx, 98, f"gₖᵀd{'₀₁₂'[i]} = 0", 8.5, "middle", "bold"), N(cx, 108, "flat: no slope left", 7, "middle")]
    parts += [N(120, 124, "the slope gₖ is perpendicular to every old heading dᵢ", 8, "middle"),
        N(120, 137, "𝓑ₖ = span(d₀, …, dₖ₋₁): all the headings flown so far", 7.5, "middle")]
    return svg(c, *parts)
D[702] = (d702, "After k conjugate hops, slice the valley along each earlier heading dᵢ: the plane is at the bottom of every slice, so the slope there is flat, gₖᵀdᵢ = 0. That makes xₖ the lowest point of the whole flight plane x₀ + 𝓑ₖ.")

def d706(c):
    ox, oy = 26, 114
    xs = lambda k: ox + k * 30
    sd = [100, 64, 50, 40, 33, 28, 25]
    cg = [100, 46, 0]
    ys = lambda v: oy - 6 - v * .8
    parts = [L(ox, oy, 232, oy, 1.2, ar=True), L(ox, oy, ox, 16, 1.2, ar=True), N(232, oy + 11, "hops", 7.5, "end"), N(ox + 3, 13, "altitude above floor", 7.5, "start"),
        poly([(xs(k), ys(v)) for k, v in enumerate(sd)], 1.4, "5 3"), poly([(xs(k), ys(v)) for k, v in enumerate(cg)], 2.6)]
    parts += [dot(xs(k), ys(v), None, r=1.8) for k, v in enumerate(sd)] + [dot(xs(k), ys(v), None, r=2.8) for k, v in enumerate(cg)]
    for k in range(7): parts.append(N(xs(k), oy + 10, str(k), 7.5, "middle"))
    parts += [N(xs(0) + 6, ys(100) + 2, "x₀", 9, "start", "bold"), N(xs(1) - 6, ys(46) + 4, "x₁", 9, "end", "bold"), N(xs(2) + 6, ys(0) - 3, "x₂ = x*", 9, "start", "bold"),
        N(150, 26, "x₀ = (4, 1)", 8, "start", "bold"), N(150, 37, "↓ α₀ = 1/5", 7.5, "start"), N(150, 48, "x₁ = (2.4, −0.6)", 8, "start", "bold"),
        N(150, 59, "↓ β₀ = 0.36, α₁ = 5/16", 7.5, "start"), N(150, 70, "x₂ = (0, 0) = x*", 8, "start", "bold"),
        N(xs(6), ys(25) + 13, "steepest descent", 7.5, "end"), N(xs(1) - 4, ys(20) + 4, "CG", 9, "end", "bold"), plane(xs(2) + 2, ys(0) - 14, 0, .5)]
    return svg(c, *parts)
D[706] = (d706, "Altitude after each hop on the 2-D example. CG (solid) flies x₀ = (4,1) → x₁ = (2.4, −0.6) with α₀ = 1/5, then blends in β₀ = 0.36 of the old heading and lands on x* = (0,0) with α₁ = 5/16. Steepest descent (dashed) keeps creeping.")

def d703(c):
    px, py = 28, 100
    gx, gy = 36, -62          # fresh downhill −g_{k+1}
    bx, by_ = 50, 8           # β_k d_k
    return svg(c, plane(px - 6, py + 6, -40, .6),
        L(px, py, px + gx, py + gy, 1.8, d="5 3", ar=True), N(px + gx - 4, py + gy - 4, "−gₖ₊₁ (fresh radar)", 7.8, "middle", "bold"),
        L(px, py, px + bx, py + by_, 1.8, d="5 3", ar=True), N(px + bx + 2, py + by_ + 12, "βₖdₖ (memory)", 7.8, "middle", "bold"),
        L(px + gx, py + gy, px + gx + bx, py + gy + by_, 1, d="2 2"), L(px + bx, py + by_, px + gx + bx, py + gy + by_, 1, d="2 2"),
        arrow(px, py, px + gx + bx, py + gy + by_, 2.6), N(px + gx + bx + 4, py + gy + by_ - 2, "dₖ₊₁", 9.5, "start", "bold"),
        N(70, 132, "dₖ₊₁ = −gₖ₊₁ + βₖdₖ", 8.5, "middle", "bold"),
        L(144, 4, 144, 142, .8, d="2 3"),
        R(156, 30, 18, 70, "#d1d5db", 1.2), R(196, 72, 18, 28, "#d1d5db", 1.2), L(150, 100, 228, 100, 1.2),
        N(165, 112, "‖gₖ‖²", 8, "middle"), N(205, 112, "‖gₖ₊₁‖²", 8, "middle"), N(165, 24, "old slope", 7, "middle"), N(205, 66, "new slope", 7, "middle"),
        N(190, 12, "how much memory to keep", 8, "middle", "bold"),
        N(190, 126, "βₖ = ‖gₖ₊₁‖² / ‖gₖ‖²", 8.5, "middle", "bold"), N(190, 138, "αₖ = ‖rₖ‖² / dₖᵀQdₖ", 7.5, "middle"))
D[703] = (d703, "Left: the new heading is the fresh downhill −gₖ₊₁ plus a fraction βₖ of the old heading dₖ (the memory). Right: βₖ compares the new slope to the old one, ‖gₖ₊₁‖²/‖gₖ‖²; the hop length αₖ is still momentum ‖rₖ‖² over brakes dₖᵀQdₖ.")

def d704(c):
    base = 104
    errs = [[60, 40, 24], [0, 34, 20], [0, 0, 16], [0, 0, 0]]
    parts = [N(120, 11, "each hop adds one Krylov direction and kills one axis", 8.3, "middle", "bold"), L(10, base, 232, base, 1.2)]
    labs = ["𝒦₁: r₀", "𝒦₂: + Qr₀", "𝒦₃: + Q²r₀", "x₃ = x*"]
    for k, e in enumerate(errs):
        x0 = 18 + k * 56
        for j, v in enumerate(e):
            fill = ["#9ca3af", "#d1d5db", "#ffffff"][j]
            parts.append(R(x0 + j * 13, base - max(v, 1), 11, max(v, 1), fill, 1.1))
        parts += [N(x0 + 19, base + 11, f"after hop {k}", 7.2, "middle"), N(x0 + 19, base + 21, labs[k], 7.5, "middle", "bold")]
    parts += [plane(206, 80, 0, .6), N(120, 30, "bars = error along each natural axis of Q", 7.5, "middle"),
        N(120, 139, "m = 3 distinct curvatures |σ(Q)| → land in m ≤ n hops", 7.8, "middle")]
    return svg(c, *parts)
D[704] = (d704, "Bars show the remaining error along each natural axis of the valley. Hop k adds the next Krylov direction (r₀, then Qr₀, then Q²r₀) to the flight plane and kills one more axis, so with m distinct curvatures the plane lands in m ≤ n hops.")

def d705(c):
    px, py = 34, 96
    return svg(c, arrow(px, py, px + 56, py - 6, 1.8), N(px + 58, py - 4, "gₖ (old reading)", 7.5, "start"),
        arrow(px, py, px + 30, py - 58, 1.8), N(px + 30, py - 63, "gₖ₊₁ (new)", 7.5, "middle"),
        L(px + 56, py - 6, px + 32, py - 56, 1.6, d="3 2", ar=True), N(px + 50, py - 36, "gₖ₊₁ − gₖ", 8, "start", "bold"), N(px + 50, py - 26, "(what changed)", 7, "start"),
        plane(px - 8, py + 8, -30, .55),
        N(62, 126, "βᴾᴿ = gₖ₊₁ᵀ(gₖ₊₁ − gₖ) / ‖gₖ‖²", 8, "middle", "bold"), N(62, 137, "new reading · change, scaled", 7, "middle"),
        L(126, 4, 126, 142, .8, d="2 3"),
        R(134, 62, 46, 18, "#d1d5db", 0), L(134, 80, 230, 80, 1.6, ar=True), L(180, 74, 180, 86, 1.6), N(180, 96, "0", 8.5, "middle"),
        N(157, 56, "βᴾᴿ < 0", 8, "middle", "bold"), N(157, 108, "reset to 0", 7.8, "middle", "bold"), N(157, 118, "fly d = −g", 7.5, "middle"),
        N(206, 56, "βᴾᴿ > 0", 8, "middle", "bold"), N(206, 108, "keep it", 7.8, "middle", "bold"), N(206, 118, "β⁺ = βᴾᴿ", 7.5, "middle"),
        N(182, 12, "β⁺ = max(0, βᴾᴿ)", 8.5, "middle", "bold"), N(182, 24, "automatic reset", 7.5, "middle"))
D[705] = (d705, "Left: Polak-Ribière looks at how much the radar reading changed, gₖ₊₁ − gₖ, measured along the new reading and scaled by ‖gₖ‖². Right: β⁺ = max(0, βᴾᴿ). A negative value means the memory would steer backwards, so it is reset to 0 and the plane flies straight downhill.")

def d1106(c):
    f = bowl(175, 112, 150, 80)
    wx = 120
    return svg(c, poly(g(f, 25, 232), 2.4), L(wx, 16, wx, 120, 2.6), *[L(wx, y, wx + 6, y + 5, 1) for y in range(20, 118, 10)],
        dot(175, f(175), None, r=2.4), N(175, f(175) + 12, "free bottom: illegal ✗", 7.5, "middle"),
        plane(wx - 14, f(wx - 14) - 10, math.degrees(math.atan(tangent(f, wx - 14))), .65), dot(wx - 2, f(wx - 2), None, r=2.6),
        N(wx - 6, 14, "legal side", 8, "end"), N(wx + 10, 14, "beyond the wall", 8, "start"),
        N(14, 40, "Case 1: ignore the wall →", 7.5, "start"), N(14, 50, "bottom is past it ✗", 7.5, "start"),
        N(120, 136, "Case 2: park against the wall, push μ* > 0 ✓", 8.5, "middle", "bold"))
D[1106] = (d1106, "Case analysis in the airplane picture. Case 1 (no wall active): the free valley bottom lies past the wall, so it is illegal. Case 2 (wall active): the plane parks against the wall and the wall pushes with μ* > 0, so this case survives.")

def d1802(c):
    P = [(40, 50), (110, 26), (196, 46), (210, 104), (90, 118)]
    return svg(c, pg(P, "#e5e7eb", 2), arrow(24, 22, 64, 62, 2), N(24, 16, "sheet tilts this way", 8, "start"),
        plane(118, 72, 25, .7), L(118, 76, 205, 103, 1.4, d="4 3", ar=True), dot(210, 104, "lowest corner", -4, 14, 8.5, "end", 3.2),
        *[dot(x, y, None, r=2.2) for x, y in P[:3] + P[4:]],
        N(120, 140, "linear altitude over a polygon: lowest point is a corner", 8, "middle"))
D[1802] = (d1802, "An LP is a flat tilted sheet over a polygon of legal positions. A plane released on it slides downhill until it hits the edge, then along the edge to the lowest corner: the optimum is always at a vertex.")

def d1903(c):
    gentle = bowl(60, 104, 50, 34)
    razor = bowl(182, 112, 14, 92)
    return svg(c, poly(g(gentle, 10, 110), 2.4), N(60, 14, "along the wall", 8.5, "middle", "bold"), N(60, 124, "gentle curvature", 8, "middle"),
        plane(60, gentle(60) - 10, 0, .55), L(122, 10, 122, 140, .8, d="2 3"),
        poly(g(razor, 168, 196, 1), 2.4), *canyon_bounce(razor, 182, [169, 195, 171, 193, 173, 191, 175, 189]),
        N(182, 14, "across the wall: ~c", 8.5, "middle", "bold"), N(182, 124, "razor canyon, zig-zag", 8, "middle"),
        N(120, 139, "κ grows like c: huge fine = huge condition number", 7.8, "middle"))
D[1903] = (d1903, "With a huge fine c, the ground across the wall becomes a razor-thin canyon (curvature ~c) while along the wall it stays gentle. That is a huge κ, so plain descent zig-zags.")

FIX = {cid: {"drawingSvg": fn(cid), "drawingCaption": cap, "textbookImg": None, "textbookRef": None} for cid, (fn, cap) in D.items()}
