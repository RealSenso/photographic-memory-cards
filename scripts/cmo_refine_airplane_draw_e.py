"""Airplane drawings for CMO topics 01-04 and 08 (screen y points down: LOW altitude = LARGE y)."""
import math
from air_lib import *
from dip_lib import E

D = {}
def ax(): return L(20, 130, 226, 130, 1.2, ar=True)

# ------------------------------------------------------------------ topic 1
def d101(c):
    return svg(c, L(80, 8, 80, 138, 1, d="3 3"), L(160, 8, 160, 138, 1, d="3 3"),
        R(14, 40, 52, 44, "#f1f5f9", 2.2), plane(40, 62, 0, .7), N(40, 98, "fenced + gate", 8, "middle", "bold"), N(40, 110, "compact ✓", 8.5, "middle", "bold"),
        arrow(92, 62, 148, 62, 2.4), L(92, 62, 148, 62, 2.4), L(92, 54, 92, 70, 2), N(120, 90, "endless runway", 8, "middle"), N(120, 102, "closed, unbounded", 8, "middle"),
        L(176, 40, 226, 40, 2.2), L(226, 40, 226, 84, 2.2), L(226, 84, 176, 84, 2.2), L(176, 84, 176, 56, 2.2, d="3 3"), plane(200, 62, 0, .6), N(200, 100, "missing fence boards", 8, "middle"), N(200, 112, "bounded, not closed", 8, "middle"))
D[101] = (d101, "Left: a fenced airfield with a locked gate (closed and bounded = compact). Middle: an endless runway (closed, unbounded). Right: fence boards missing (bounded, not closed).")

def d102(c):
    return svg(c, L(20, 130, 226, 130, 1.2, ar=True), L(30, 52, 120, 52, 2.6), L(120, 88, 214, 88, 2.6), dash(120, 52, 120, 88, 1.2, "2 2"),
        circ(120, 88, 3.2, "#000000", 1.5), circ(120, 52, 3.2, "#ffffff", 1.5), plane(70, 38, 0, .65), plane(176, 76, 0, .65),
        N(120, 112, "cliff: altimeter reads the lower height", 8.5, "middle", "bold"), N(150, 40, "closed dot = true value", 8, "start"))
D[102] = (d102, "At a cliff edge the altimeter reports the lower of the two heights (filled dot), so a plane landing there touches real ground.")

def d103(c):
    f_ = lambda x: 78 + 26 * math.sin((x - 40) / 22) - 12 * math.sin((x - 40) / 9)
    xs = [x for x in range(40, 201)]
    lo = max(xs, key=f_); hi = min(xs, key=f_)
    return svg(c, wall(40, 18, 40, 130, -1, 0, 8, 5), wall(200, 18, 200, 130, 1, 0, 8, 5), fn(f_, 40, 200, 80, 2.6),
        plane(lo - 4, f_(lo) - 20, 0, .6), dot(lo, f_(lo), "lowest ✓", 8, 4, 8.5, "start", 3), dot(hi, f_(hi), "peak", 0, -8, 8.5, "middle", 3),
        N(120, 12, "continuous terrain over a fenced airfield", 8.5, "middle", "bold"), N(120, 142, "always has a lowest point you can touch", 8.5))
D[103] = (d103, "A continuous terrain over a fenced, finite airfield always has a lowest point the plane can touch down on (and a highest peak).")

def d104(c):
    return svg(c, fn(lambda x: 112 - 0.0058 * 0 - 82 * ((x - 120) / 96) ** 2 + 0 if False else 38 + 74 * (1 - ((x - 120) / 96) ** 2) * 0 + 0, 30, 30, 2, 1) if False else "",
        fn(lambda x: 112 - 80 * ((x - 120) / 92) ** 2, 28, 212, 40, 2.6), arrow(28, 40, 28, 18, 2), arrow(212, 40, 212, 18, 2), plane(120, 98, 0, .75),
        N(120, 16, "walls rise without limit", 8.5, "middle", "bold"), N(120, 138, "the lowest point cannot be far away", 8.5), dash(54, 62, 186, 62, 1.2, "4 3"), N(120, 58, "sublevel set", 8, "middle"))
D[104] = (d104, "The terrain rises without limit in every direction: the lowest point cannot be far away, so the sublevel fence (dashed) is finite.")

def d105(c):
    f_ = lambda x: 112 - 0.0105 * (x - 120) ** 2
    x1, x2 = 60, 180
    return svg(c, poly([(28, 12)] + [(x, f_(x)) for x in range(28, 213, 8)] + [(212, 12)], 0.8, None, "#e5e7eb"), fn(f_, 28, 212, 40, 2.6),
        dot(x1, f_(x1), None, r=2.8), dot(x2, f_(x2), None, r=2.8), dash(x1, f_(x1), x2, f_(x2), 1.6, "5 3"),
        plane(120, 52, 0, .7), N(120, 134, "the sky above the terrain (epigraph)", 8.5, "middle", "bold"), N(120, 144, "straight flight paths stay in the sky", 8))
D[105] = (d105, "The sky above a convex terrain is the epigraph: any straight flight path between two points in it stays in the sky.")

def d106(c):
    F = lambda x: 66 - 30 * (2 * ((x - 120) / 50) ** 4 - 4 * ((x - 120) / 50) ** 2) / 2
    return svg(c, fn(F, 50, 190, 80, 2.6), dash(26, F(70), 214, F(70), 1.2, "4 3"), L(50, 20, 50, 130, 1.6), L(190, 20, 190, 130, 1.6),
        plane(120, F(120) - 20, 0, .6), dot(70, F(70), "(−1,−1)", -2, 16, 8.5, "middle", 3), dot(170, F(170), "(1,1)", 2, 16, 8.5, "middle", 3), dot(120, F(120), "saddle", 18, 4, 8.5, "start", 2.6),
        N(120, 12, "coercive: build a fence, search inside", 8.5, "middle", "bold"), N(120, 142, "global minimum −2 at ±(1,1)", 8.5, "middle"))
D[106] = (d106, "The terrain along the diagonal x₁=x₂ is a double well with its two lowest points at ±(1,1) (altitude −2) and a saddle at the origin; the fence encloses both.")

# ------------------------------------------------------------------ topic 2
def d201(c):
    f_ = lambda x: 60 + 30 * math.exp(-((x - 130) / 40) ** 2) - 0.0
    x0 = 100
    f0 = f_(x0); g0 = (f_(x0 + 1e-3) - f_(x0 - 1e-3)) / 2e-3; h0 = (f_(x0 + 2) - 2 * f0 + f_(x0 - 2)) / 4
    return svg(c, fn(f_, 20, 226, 60, 2.6), L(x0 - 50, f0 - 50 * g0, x0 + 50, f0 + 50 * g0, 1.5, d="5 3"),
        fn(lambda x: f0 + g0 * (x - x0) + 0.5 * h0 * (x - x0) ** 2, x0 - 40, x0 + 46, 30, 1.4, "2 2"), plane(x0 - 4, f0 - 16, 0, .6), dot(x0, f0, None, r=2.6),
        N(40, 24, "altimeter  f", 8.5, "start", "bold"), N(40, 36, "slope gauge  ∇f  (dashed line)", 8.5, "start"), N(40, 48, "curvature gauge  ∇²f  (dotted curve)", 8.5, "start"), N(120, 140, "local model of the terrain", 8.5, "middle", "bold"))
D[201] = (d201, "The pilot's three fog instruments at one point: altimeter f, slope gauge ∇f (tangent line) and curvature gauge ∇²f (the bending parabola).")

def d202(c):
    return svg(c, fn(lambda x: 40 + 70 * (1 - ((x - 120) / 92) ** 2), 28, 212, 40, 2.6), dash(60, 110, 180, 110, 1.4, "5 3"), plane(120, 96, 0, .8), dot(120, 110, None, r=3),
        N(120, 24, "slope gauge reads 0", 9, "middle", "bold"), N(120, 138, "no direction goes downhill first: ∇f(x*) = 0", 8.5, "middle"))
D[202] = (d202, "At the lowest parking spot the slope gauge reads zero: the tangent is level and no direction starts to descend.")

def d203(c):
    return svg(c, L(120, 8, 120, 138, 1, d="3 3"), fn(lambda x: 112 - 70 * ((x - 66) / 50) ** 2, 22, 110, 30, 2.6), plane(66, 98, 0, .6), N(66, 128, "curves up ✓ stays put", 8.5, "middle", "bold"),
        fn(lambda x: 52 + 62 * ((x - 174) / 50) ** 2 * 0 + 0 - 0 + 62 * ((x - 174) / 50) ** 2 - 62 * 0, 124, 224, 30, 2.6) if False else fn(lambda x: 40 + 70 * ((x - 174) / 50) ** 2 * 0 + 0, 124, 124, 2, 1) if False else
        fn(lambda x: 66 + 62 * ((x - 174) / 50) ** 2 - 0, 124, 224, 30, 2.6) if False else fn(lambda x: 44 + 70 * ((x - 174) / 50) ** 2, 124, 224, 30, 1.0, "") if False else "",
        fn(lambda x: 40 + 70 * ((x - 174) / 50) ** 2, 124, 224, 30, 2.6, "5 3"), plane(174, 28, 0, .6), arrow(174, 36, 206, 56, 1.8), N(174, 128, "curves down ✗ rolls away", 8.5, "middle", "bold"),
        N(66, 16, "SONC: ∇²f ⪰ 0", 8.5, "middle", "bold"))
D[203] = (d203, "Left: ground curving up in every direction holds the plane. Right: one direction curving down and the plane rolls away, so the Hessian must be positive semidefinite.")

def d204(c):
    return svg(c, fn(lambda x: 110 - 76 * ((x - 120) / 90) ** 2, 30, 210, 40, 2.6), fn(lambda x: 110 - 30 * ((x - 120) / 90) ** 2, 40, 200, 30, 1.2, "4 3"), plane(120, 96, 0, .75), dot(120, 110, None, r=3),
        N(120, 22, "strictly up in every direction", 8.5, "middle", "bold"), N(120, 138, "∇f=0 and ∇²f ≻ 0  ⇒  strict local min", 8.5), N(206, 66, "c‖d‖² floor", 8, "end"))
D[204] = (d204, "The ground curves strictly upward in every direction, at least like the dotted floor c‖d‖²: a guaranteed strict local lowest spot.")

def d205(c):
    parts = [L(80, 10, 80, 136, 1, d="3 3"), L(160, 10, 160, 136, 1, d="3 3")]
    parts += [fn(lambda x: 100 - 56 * ((x - 40) / 28) ** 2 * 1, 12, 68, 20, 2.4), plane(40, 84, 0, .5), N(40, 126, "all λ>0", 8.5, "middle", "bold"), N(40, 138, "bowl: min", 8, "middle")]
    parts += [fn(lambda x: 44 + 56 * ((x - 120) / 28) ** 2 * 1, 92, 148, 20, 2.4), plane(120, 32, 0, .5), N(120, 126, "all λ<0", 8.5, "middle", "bold"), N(120, 138, "hilltop: max", 8, "middle")]
    parts += [fn(lambda x: 100 - 52 * ((x - 200) / 30) ** 2, 172, 228, 20, 2.4), fn(lambda x: 44 + 52 * ((x - 200) / 30) ** 2, 172, 228, 20, 1.4, "4 3"), plane(200, 60, 0, .5), N(200, 126, "mixed λ", 8.5, "middle", "bold"), N(200, 138, "saddle (pass)", 8, "middle")]
    return svg(c, *parts)
D[205] = (d205, "Hessian eigenvalues tell the shape: all positive is a bowl, all negative a hilltop, mixed is a mountain pass (low along the ridge, high across the trail).")

def d206(c):
    par = lambda x: 124 - 0.0105 * (x - 120) ** 2
    parts = [fn(lambda x: par(x) - 12, 26, 214, 40, 1.8), fn(lambda x: par(x) + 12, 26, 214, 40, 1.8), fn(par, 26, 214, 40, 1.0, "3 3"), plane(46, par(46) - 16, 20, .6),
             dot(120, par(120), None, r=3), N(120, 20, "banana canyon y = x²", 8.5, "middle", "bold"), N(120, 32, "κ ≈ 2500: walls far steeper than the floor", 8, "middle"), N(120, 142, "follow the floor with tiny careful legs", 8.5)]
    return svg(c, *parts)
D[206] = (d206, "Rosenbrock is a long curved canyon: the floor (dashed) is almost flat while the walls are enormously steeper, condition number about 2500.")

# ------------------------------------------------------------------ topic 3
def d301(c):
    return svg(c, L(120, 8, 120, 138, 1, d="3 3"), E(60, 66, 44, 32, 0, "#f1f5f9", 2), dot(34, 70, None, r=2.6), dot(90, 56, None, r=2.6), dash(34, 70, 90, 56, 1.8, "none") if False else L(34, 70, 90, 56, 2),
        N(60, 112, "convex ✓", 8.5, "middle", "bold"), PG("140,60 186,34 226,60 190,52", "#f1f5f9", 2) if False else
        P("M140,38 Q176,100 226,38 Q184,70 140,38 Z", "#f1f5f9", 2), dot(146, 42, None, r=2.6), dot(220, 42, None, r=2.6), L(146, 42, 220, 42, 2, d="4 3"), N(182, 112, "crescent ✗", 8.5, "middle", "bold"), plane(60, 66, 0, .5))
D[301] = (d301, "Left: a convex airspace, where every straight flight path between two points stays inside. Right: a crescent, where the straight path leaves the airspace.")

def d302(c):
    f_ = lambda x: 112 - 76 * ((x - 120) / 90) ** 2
    x0 = 160; f0 = f_(x0); m = (f_(x0 + 1e-3) - f_(x0 - 1e-3)) / 2e-3
    return svg(c, fn(f_, 30, 210, 40, 2.6), L(x0 - 70, f0 - 70 * m, x0 + 40, f0 + 40 * m, 1.6, d="5 3"), plane(x0 - 2, f0 + 16, 0, .6), dot(x0, f0, None, r=3),
        N(120, 134, "the glide plane touching at your spot lies under the whole terrain", 8, "middle", "bold"))
D[302] = (d302, "At any point the flat glide plane touching the terrain lies beneath the terrain everywhere else (a convex terrain is always above its tangents).")

def d303(c):
    f_ = lambda x: 112 - 76 * ((x - 120) / 90) ** 2
    parts = [fn(f_, 30, 210, 40, 2.6)]
    for x in (60, 100, 140, 180):
        parts.append(arrow(x, f_(x) - 4, x + (120 - x) * 0.0, f_(x) - 30, 1.6)) if False else None
    parts += [plane(120, 98, 0, .7), arrow(120, 120, 120, 134, 0.1) if False else "", arrow(120, 86, 120, 54, 2.4), N(130, 56, "seat pressed up", 8.5, "start", "bold"),
              N(120, 138, "never floats off the seat: ∇²f ⪰ 0 everywhere", 8.5, "middle", "bold")]
    for x in (66, 174):
        parts += [plane(x, f_(x) - 12, 0, .45)]
    return svg(c, *parts)
D[303] = (d303, "Flying across a convex terrain the seat is always pressed up by the ground and never floats off: the terrain curves upward everywhere (PSD Hessian).")

def d304(c):
    return svg(c, fn(lambda x: 112 - 76 * ((x - 120) / 90) ** 2, 30, 210, 40, 2.6), fn(lambda x: 112 - 110 * ((x - 120) / 90) ** 2 + 0, 52, 188, 30, 1.4, "4 3"),
        plane(120, 98, 0, .75), dot(120, 112, None, r=3), arrow(160, 112, 160, 60, 1.4, d="2 2") if False else "", N(206, 28, "floor: m/2 ‖x−x*‖²", 8.5, "end", "bold"), N(120, 138, "leaving the bottom always costs altitude", 8.5, "middle"),
        N(120, 20, "strong convexity", 9, "middle", "bold"))
D[304] = (d304, "The terrain stays above a bowl-shaped floor (dotted) of fixed steepness: leaving the bottom always costs at least m/2 ‖x − x*‖² of altitude.")

def d305(c):
    f_ = lambda x: 112 - 80 * ((x - 120) / 90) ** 2
    parts = [fn(f_, 30, 210, 40, 2.6), plane(120, 98, 0, .6)]
    for x, ln in ((74, 28), (52, 50), (166, 28), (188, 50)):
        sgn = 1 if x < 120 else -1
        y = f_(x)
        parts.append(arrow(x, y - 6, x + sgn * ln, y + 6 + ln * 0.2, 1.8))
    parts += [N(120, 20, "higher up = steeper slope", 8.5, "middle", "bold"), N(120, 138, "no flat plateau far above the valley floor", 8.5)]
    return svg(c, *parts)
D[305] = (d305, "The higher you are above the lowest point the steeper the slope under you (longer arrows), so the plane never sits on a flat plateau far above the floor.")

def d306(c):
    parts = [L(80, 10, 80, 136, 1, d="3 3"), L(160, 10, 160, 136, 1, d="3 3")]
    parts += [poly([(10, 60), (30, 90), (50, 90), (70, 60)][0:1] + [(10, 52), (28, 92), (52, 92), (70, 52)], 2.4), N(40, 118, "convex", 8.5, "middle", "bold"), N(40, 130, "flat ramps allowed", 8)]
    parts += [fn(lambda x: 96 - 44 * ((x - 120) / 30) ** 4, 92, 148, 30, 2.4), N(120, 118, "strictly convex", 8.5, "middle", "bold"), N(120, 130, "no flat stretch, x⁴", 8)]
    parts += [fn(lambda x: 96 - 44 * ((x - 200) / 30) ** 2, 172, 228, 30, 2.4), N(200, 118, "strongly convex", 8.5, "middle", "bold"), N(200, 130, "true bowl", 8), plane(200, 80, 0, .45)]
    return svg(c, *parts)
D[306] = (d306, "Three terrains: convex allows level ramps, strictly convex has no level stretch but can flatten (x⁴), strongly convex is a true bowl everywhere.")

# ------------------------------------------------------------------ topic 4
def d401(c):
    return svg(c, L(20, 100, 226, 40, 1.4, d="5 3"), plane(60, 88, 70, .8) if False else plane(70, 84, 16.7 * 0 + 16, .8), arrow(80, 82, 176, 108, 3), N(180, 118, "dₖ", 10, "start", "bold"),
        arrow(70, 76, 84, 24, 1.8, d="3 2"), N(88, 30, "∇f (uphill)", 8.5, "start"), dot(176, 108, None, r=3), N(176, 128, "xₖ + αₖdₖ", 8.5, "middle"), N(120, 140, "∇fᵀdₖ < 0: heading points downhill", 8.5, "middle", "bold"),
        arrow(76, 92, 172, 118, 0.1) if False else "", N(120, 14, "α: how far before checking the radar", 8.5, "middle"))
D[401] = (d401, "Choose a heading dₖ that points downhill (∇fᵀd<0) and decide how far α to fly before checking the radar again.")

def d402(c):
    return svg(c, ax(), fn(lambda x: 112 - 72 * ((x - 120) / 90) ** 2, 30, 210, 40, 2.6), plane(120, 96, 0, .7), dot(120, 112, None, r=3), dash(120, 112, 120, 130, 1.2, "3 3"),
        N(120, 142, "α*", 9.5, "middle", "bold"), N(206, 56, "altitude along the track", 8.5, "end"), N(120, 12, "exact line search: fly to the very bottom", 8.5, "middle", "bold"), N(216, 142, "α", 8.5, "end"))
D[402] = (d402, "Altitude along one straight track: fly exactly to the bottom (α*) before turning, found in closed form for a quadratic.")

def d403(c):
    f_ = lambda a: 108 - 62 * ((a - 150) / 120) ** 2
    y0 = f_(30); slope = (f_(31) - f_(29)) / 2
    arm = lambda a: y0 + 0.35 * slope * (a - 30)
    xs = [a for a in range(30, 211) if f_(a) >= arm(a) + 0.5]
    x1, x2 = min(xs), max(xs)
    return svg(c, ax(), fn(f_, 30, 210, 60, 2.6), L(30, arm(30), 210, arm(210), 1.6, d="5 3"), R(x1, 132, x2 - x1, 6, "#c9ced8", 1.2), N((x1 + x2) / 2, 128, "accept", 8.5, "middle", "bold"),
        plane(30, y0 - 14, 0, .6), N(120, 12, "Armijo: the drop must beat the dashed line", 8.5, "middle", "bold"), N(216, 126, "α", 8.5, "end"), N(60, 76, "fair drop", 8, "start"))
D[403] = (d403, "Altitude along the leg: accept only steps where the actual altitude falls below the dashed Armijo line (a fair drop for the distance and slope).")

def d404(c):
    f_ = lambda a: 108 - 62 * ((a - 150) / 120) ** 2
    a1 = 150; m0 = (f_(31) - f_(29)) / 2
    return svg(c, ax(), fn(f_, 30, 210, 60, 2.6), L(30, f_(30), 100, f_(30) + 70 * m0, 1.4, d="4 3"), N(60, f_(30) - 8, "initial slope", 8, "start"),
        L(a1 - 40, f_(a1), a1 + 40, f_(a1), 1.6), dot(a1, f_(a1), None, r=3), plane(a1, f_(a1) - 14, 0, .6),
        N(120, 12, "curvature: slope must have flattened enough", 8.5, "middle", "bold"), N(120, 144, "tiny hops on a steep slope are refused", 8.5), N(216, 126, "α", 8.5, "end"))
D[404] = (d404, "After the leg the slope under you must have flattened enough compared with the starting slope; tiny hops that leave you on a steep slope are refused.")

def d405(c):
    ox, oy = 70, 100
    return svg(c, arrow(ox, oy, ox + 8, oy - 62, 2.6, d="4 3"), N(ox - 2, oy - 66, "−∇f", 9.5, "end", "bold"), arrow(ox, oy, ox + 98, oy - 44, 3), N(ox + 100, oy - 46, "dₖ", 10, "start", "bold"),
        P(f"M{ox+30},{oy-22} A32,32 0 0,1 {ox+7},{oy-31}", "none", 1.5), N(ox + 38, oy - 36, "θ", 11, "middle", "bold"), plane(ox, oy, -25, .75),
        N(176, 108, "Σ cos²θ ‖g‖² < ∞", 9, "middle", "bold"), N(176, 122, "⇒ g → 0 if θ ≠ 90°", 8.5), N(120, 14, "never turn sideways to the slope", 8.5, "middle", "bold"))
D[405] = (d405, "The angle θ between your heading and straight downhill: as long as it never reaches 90° the slope gauge is driven to zero.")

def d406(c):
    f_ = lambda a: 108 - 62 * ((a - 150) / 120) ** 2
    y0 = f_(30); sl = (f_(31) - f_(29)) / 2
    arm = lambda a: y0 + 0.3 * sl * (a - 30)
    trial = [(205, "✗", "α₀"), (118, "✗", "α₀/2"), (80, "✓", "α₀/4")]
    parts = [ax(), fn(f_, 30, 214, 60, 2.6), L(30, arm(30), 214, arm(214), 1.5, d="5 3"), plane(30, y0 - 14, 0, .6)]
    for a, m, nm in trial:
        parts += [dot(a, f_(a), None, r=3), N(a, 144, f"{nm} {m}", 8.5, "middle", "bold")]
    parts += [N(120, 12, "too big? halve it and look again", 8.5, "middle", "bold")]
    return svg(c, *parts)
D[406] = (d406, "Plan a long leg; if the altitude drop is too small (above the dashed line), halve the leg and check again until the drop is acceptable.")

# ------------------------------------------------------------------ topic 8
def d801(c):
    return svg(c, L(20, 126, 226, 126, 1.2, ar=True), L(30, 22, 30, 130, 1.2, ar=True), L(34, 110, 220, 40, 2.2), dot(80, 91, None, r=3), dot(170, 57, None, r=3),
        dash(80, 126, 80, 91, 1, "2 2"), dash(170, 126, 170, 57, 1, "2 2"), arrow(82, 120, 168, 120, 2), N(125, 116, "s", 9.5, "middle", "bold"), dash(80, 91, 170, 91, 1, "2 2"), arrow(172, 89, 172, 59, 2), N(184, 76, "y", 9.5, "start", "bold"),
        plane(80, 78, 0, .55), N(80, 138, "xₖ", 8.5, "middle"), N(170, 138, "xₖ₊₁", 8.5, "middle"), N(40, 18, "slope gauge ∇f", 8.5, "start"), N(120, 12, "B s = y", 9.5, "middle", "bold"))
D[801] = (d801, "From the flight log: how far you flew (s) and how much the slope gauge changed (y) give the curvature along the path, B s = y.")

def _boxes(c, items, ttl, foot, notes=""):
    parts = []
    x = 8
    for lab, w, bold in items:
        parts.append(R(x, 50, w, 36, "#f1f5f9" if not bold else "#d9dee7", 1.6, 3)); parts.append(N(x + w / 2, 72, lab, 8.5, "middle", "bold" if bold else "normal")); x += w + 6
    parts += [N(120, 24, ttl, 9, "middle", "bold"), N(120, 112, foot, 8.5, "middle"), N(120, 130, notes, 8.5, "middle", "bold") if notes else "", plane(222, 24, 0, .5)]
    return svg(c, *parts)

D[802] = (lambda c: _boxes(c, [("Bₖ", 28, False), ("+", 10, False), ("(y−Bs)(y−Bs)ᵀ", 88, True), ("/", 10, False), ("(y−Bs)ᵀs", 58, False)], "SR1: one set screw (rank-1)", "fast and light", "denominator ≈ 0 → the mechanism jams"),
          "A single rank-one correction to the curvature estimate: quick and light, but if the denominator is near zero the update jams.")
D[803] = (lambda c: _boxes(c, [("Hₖ", 26, False), ("−", 12, False), ("Hy yᵀH / yᵀHy", 78, True), ("+", 12, False), ("s sᵀ / yᵀs", 62, True)], "DFP: two counterbalancing weights", "one removes the old direction", "one adds the new leg you flew"),
          "Two corrections to the curvature estimate: one balances out the old information along y, the other adds the leg you just flew.")
D[804] = (lambda c: _boxes(c, [("Bₖ", 28, False), ("−", 12, False), ("Bs sᵀB / sᵀBs", 76, True), ("+", 12, False), ("y yᵀ / yᵀs", 62, True)], "BFGS: self-correcting gyro (rank-2)", "stays positive definite", "the gold standard"),
          "BFGS's rank-two update removes the old direction and adds the new one, keeping the curvature estimate positive definite: the standard choice.")

def d805(c):
    return svg(c, L(120, 8, 120, 138, 1, d="3 3"),
        fn(lambda x: 110 - 60 * ((x - 60) / 44) ** 2, 18, 104, 30, 2.4), arrow(40, 118, 78, 118, 2), arrow(40, 118, 40, 118, 0.1) if False else "", N(60, 132, "s", 9, "middle", "bold"), arrow(86, 112, 86, 76, 2), N(96, 94, "y", 9, "start", "bold"),
        N(60, 18, "ground curves up", 8.5, "middle", "bold"), N(60, 30, "sᵀy > 0 ✓ trust it", 8.5, "middle"),
        fn(lambda x: 56 + 60 * ((x - 180) / 44) ** 2 * 0 + 0, 140, 140, 2, 1) if False else fn(lambda x: 60 + 52 * ((x - 180) / 44) ** 2, 138, 224, 30, 2.4, "5 3"),
        arrow(160, 118, 198, 118, 2), N(180, 132, "s", 9, "middle", "bold"), arrow(206, 76, 206, 108, 2), N(214, 92, "y", 9, "start", "bold"), N(180, 18, "ground sags", 8.5, "middle", "bold"), N(180, 30, "sᵀy ≤ 0 ✗ refuse", 8.5, "middle"))
D[805] = (d805, "Trust a leg only if the terrain curved upward along it (sᵀy>0), which a Wolfe line search guarantees; if the ground sagged, refuse to log that leg.")

def d806(c):
    parts = []
    for i in range(6):
        x = 12 + i * 38
        old = i < 2
        parts.append(R(x, 52, 32, 40, "#f1f5f9" if not old else "#ffffff", 1.6, 3, "3 3" if old else None))
        parts.append(N(x + 16, 70, "s", 9, "middle", "bold" if not old else "normal")); parts.append(N(x + 16, 84, "y", 9, "middle", "bold" if not old else "normal"))
    parts += [N(120, 24, "L-BFGS: keep only the last m legs", 9, "middle", "bold"), N(50, 108, "old: forgotten", 8.5, "middle"), N(160, 108, "last m kept", 8.5, "middle", "bold"), plane(222, 24, 0, .5),
              N(120, 130, "nearly the same guidance, a fraction of the memory", 8.5, "middle")]
    return svg(c, *parts)
D[806] = (d806, "Keep only the last m flight-log legs (s, y) instead of a full curvature map: nearly the same guidance for a fraction of the memory.")

FIX = {cid: {"drawingSvg": fnc(cid), "drawingCaption": cap} for cid, (fnc, cap) in D.items()}
