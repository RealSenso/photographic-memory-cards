"""CMO topics 1-3: every diagram labels the terms of the formula on its card (airplane side views, curves)."""
import math
from air_lib import *
from cmo_refine_zzz_curves import g, bowl, tangent, pg

D = {}

def ground_axis(y=120, x0=10, x1=232, lab="x"):
    return [L(x0, y, x1, y, 1, ar=True), N(x1 + 2, y + 3, lab, 8, "start")]

def vlab(x, y1, y2, text, dx=4, a="start", sz=7.5):
    """vertical double-headed bracket with a label"""
    return [L(x, y1, x, y2, 1, ar=True), L(x, y2, x, y1, 1, ar=True), N(x + dx, (y1 + y2) / 2 + 3, text, sz, a)]

# ---------------- topic 1 ----------------
def d101(c):
    return svg(c, R(22, 38, 40, 34, "#f3f4f6", 1.2), C(42, 55, 33, "none", .9).replace('fill="none"', 'fill="none" stroke-dasharray="3 2"'),
        plane(42, 55, 0, .5), N(42, 100, "R", 8, "middle"), L(42, 55, 42 + 23, 55 + 23, .8, d="2 2"),
        N(42, 14, "K = airfield", 8, "middle"), N(42, 112, "bounded: ‖x‖ ≤ R", 7.5, "middle"), N(42, 122, "closed: fence ∈ K", 7.5, "middle"), N(42, 135, "compact ✓", 8, "middle"),
        L(84, 6, 84, 142, .7, d="2 3"),
        L(96, 55, 160, 55, 1.2, ar=True), L(96, 45, 96, 65, 1.2), plane(116, 47, 0, .45),
        N(128, 14, "endless runway", 8, "middle"), N(128, 112, "closed, but no R", 7.5, "middle"), N(128, 122, "fits ‖x‖ ≤ R", 7.5, "middle"), N(128, 135, "not bounded ✗", 8, "middle"),
        L(170, 6, 170, 142, .7, d="2 3"),
        R(186, 38, 40, 34, "#f3f4f6", 1.2).replace('stroke-width', 'stroke-dasharray="6 4" stroke-width'), plane(206, 55, 0, .5),
        N(206, 14, "fence gaps", 8, "middle"), N(206, 112, "edge points", 7.5, "middle"), N(206, 122, "not in K", 7.5, "middle"), N(206, 135, "not closed ✗", 8, "middle"))
D[101] = (d101, "K is compact exactly when it is closed (the fence belongs to the airfield) and bounded (it fits inside a ball ‖x‖ ≤ R). An endless runway fails 'bounded'; a fence with missing boards fails 'closed'.")

def d102(c):
    x0, ylo, yhi, al = 120, 92, 50, 70
    return svg(c, *ground_axis(), L(20, yhi, x0, yhi, 1.2), C(x0, yhi, 2.6, "#ffffff", 1), L(x0, ylo, 222, ylo - 20, 1.2), C(x0, ylo, 2.6),
        plane(70, yhi - 9, 0, .55), dash(x0, ylo, x0, 120, .8), N(x0, 131, "x₀", 8.5, "middle"),
        N(x0 + 6, ylo + 12, "f(x₀): the true reading", 7.5, "start"), N(60, yhi - 16, "liminf f(x) as x → x₀", 7.5, "middle"), N(60, yhi + 12, "(cliff top: open dot)", 7, "middle"),
        dash(14, al, 228, al, .9, "5 3"), N(228, al - 3, "α", 8.5, "end"),
        L(x0, 136, 222, 136, 1.2), C(x0, 136, 2.2), N(176, 145 - 1, "𝓛α = {f ≤ α} includes x₀: closed", 7, "middle"),
        N(120, 12, "lsc: liminf f(x) ≥ f(x₀): the altimeter takes the lower value", 7.5, "middle"))
D[102] = (d102, "At the cliff x₀ the terrain jumps. Lower semicontinuity means the altimeter takes the lower value: f(x₀) ≤ liminf f(x). Then every sublevel set 𝓛α = {f ≤ α} contains its edge point x₀, so it is closed.")

def d103(c):
    f = lambda x: 70 - 22 * math.sin((x - 40) / 22) + 8 * math.cos((x - 40) / 9)
    a, b = 40, 210
    xs = min(range(a, b + 1), key=lambda x: -f(x))
    return svg(c, *ground_axis(), poly(g(f, a, b, 2), 1.4), L(a, 18, a, 120, 1.2), L(b, 18, b, 120, 1.2),
        N(a, 131, "a", 8.5, "middle"), N(b, 131, "b", 8.5, "middle"), N((a + b) / 2, 140, "K = [a, b]: closed and bounded (compact)", 7.5, "middle"),
        C(xs, f(xs), 2.6), plane(xs, f(xs) - 10, 0, .55), dash(xs, f(xs) + 3, xs, 120, .8), N(xs, 131, "x*", 8.5, "middle"),
        N(xs + 8, f(xs) + 4, "f(x*) = min over K", 7.5, "start"), N(80, 22, "f continuous: no gaps in the ground", 7.5, "middle"),
        N(120, 10, "compact K + continuous f ⇒ a lowest point x* exists", 7.5, "middle"))
D[103] = (d103, "Weierstrass: if the airfield K is compact (closed and bounded, fence included) and the terrain f is continuous, the pilot can always land on a lowest point x* ∈ K with f(x*) = min f.")

def d104(c):
    f = bowl(120, 104, 70, 70)
    al = 74
    hw = 70 * math.sqrt((104 - al) / 70)
    return svg(c, *ground_axis(), poly(g(f, 46, 194, 2), 1.4), L(48, 40, 44, 20, 1, ar=True), L(192, 40, 196, 20, 1, ar=True),
        N(40, 16, "f → +∞", 7.5, "end"), N(200, 16, "f → +∞", 7.5, "start"), N(120, 10, "as ‖x‖ → ∞", 7.5, "middle"),
        dash(30, al, 210, al, .9, "5 3"), N(212, al + 3, "α", 8.5, "start"),
        L(120 - hw, 128, 120 + hw, 128, 1.2), C(120 - hw, 128, 2), C(120 + hw, 128, 2), dash(120 - hw, al, 120 - hw, 128, .7), dash(120 + hw, al, 120 + hw, 128, .7),
        N(120, 139, "𝓛α = {f ≤ α}: closed and bounded = compact", 7.5, "middle"),
        C(120, 104, 2.4), plane(120, 94, 0, .5), N(128, 112, "min exists inside", 7, "start"))
D[104] = (d104, "Coercive terrain rises to +∞ in every direction (‖x‖ → ∞), so any altitude α cuts out a sublevel set 𝓛α = {f ≤ α} that is closed and bounded. Weierstrass applies inside it, so a global minimum exists.")

def d105(c):
    f = bowl(120, 112, 95, 80)
    pts = g(f, 25, 215)
    xp, tp = 150, 54
    return svg(c, pg(pts + [(215, 26), (25, 26)], "#e5e7eb", 0), poly(pts, 1.4),
        C(xp, tp, 2.4), N(xp + 5, tp - 3, "(x, t)", 8, "start"), dash(xp, tp + 3, xp, f(xp), .9), C(xp, f(xp), 2), N(xp + 5, f(xp) + 10, "f(x)", 8, "start"),
        N(xp - 4, (tp + f(xp)) / 2 + 3, "t ≥ f(x)", 7.5, "end"), plane(80, 50, 0, .6),
        N(120, 14, "epi(f) = {(x, t) : f(x) ≤ t}: all the sky on or above the ground", 7.5, "middle"),
        N(120, 128, "f convex ⇔ epi(f) is a convex set", 8, "middle"), N(120, 139, "(the shaded sky has no dents)", 7, "middle"))
D[105] = (d105, "The epigraph is every point (x, t) with t ≥ f(x): all the sky on or above the ground. f is convex exactly when that shaded region is a convex set.")

def d106(c):
    h = lambda t: 2 * t ** 4 - 4 * t ** 2           # f along the slice x1 = x2 = t
    X = lambda t: 120 + t * 55
    Y = lambda t: 70 - h(t) * 14
    ts = [i / 50 for i in range(-80, 81)]
    pts = [(X(t), Y(t)) for t in ts if 12 < Y(t) < 128]
    return svg(c, *ground_axis(124), poly(pts, 1.4), dash(14, Y(-1), 226, Y(-1), .8, "4 3"), N(228, Y(-1) + 3, "−2", 8, "end"),
        C(X(-1), Y(-1), 2.4), C(X(1), Y(1), 2.4), N(X(-1), Y(-1) + 12, "(−1, −1)", 7.5, "middle"), N(X(1), Y(1) + 12, "(1, 1)", 7.5, "middle"),
        C(X(0), Y(0), 2), N(X(0), Y(0) - 6, "saddle (0, 0)", 7, "middle"), plane(X(1), Y(1) - 10, 0, .5),
        N(120, 10, "f ≥ x₁⁴ + x₂⁴ − 2(x₁² + x₂²) → ∞: coercive", 7.5, "middle"), N(120, 136, "min f = f(1, 1) = f(−1, −1) = −2", 8, "middle"),
        N(40, 30, "x⁴ wins:", 7, "middle"), N(40, 39, "walls → ∞", 7, "middle"))
D[106] = (d106, "Slice along x₁ = x₂: the x⁴ terms beat −2x², so the walls rise to infinity (coercive) and a global minimum must exist. Setting ∇f = 0 finds it at (1, 1) and (−1, −1), with value −2.")

# ---------------- topic 2 ----------------
def d201(c):
    f = bowl(150, 110, 120, 85)
    x, xd = 50, 95
    s_ = tangent(f, x)
    yt = f(x) + s_ * (xd - x)
    return svg(c, *ground_axis(124), poly(g(f, 30, 232, 2), 1.4), L(x - 20, f(x) - 20 * s_, xd + 14, f(x) + (xd + 14 - x) * s_, 1, d="5 3"),
        dash(x, f(x), xd + 30, f(x), .8, "2 2"), C(x, f(x), 2.4), plane(x, f(x) - 10, math.degrees(math.atan(s_)), .5), N(x - 5, f(x) + 3, "f(x)", 8, "end"),
        dash(x, f(x) + 3, x, 124, .6), dash(xd, f(xd) + 3, xd, 124, .6), L(x, 132, xd, 132, 1, ar=True), N((x + xd) / 2, 142, "step d", 7.5, "middle"),
        C(xd, f(xd), 2.4), C(xd, yt, 1.8),
        *vlab(xd + 22, f(x), yt, "", 0), N(xd + 26, (f(x) + yt) / 2, "∇f(x)ᵀd", 8, "start"), N(xd + 26, (f(x) + yt) / 2 + 10, "slope term (tangent drop)", 7, "start"),
        *vlab(xd + 8, yt, f(xd), "", 0), L(xd + 10, (yt + f(xd)) / 2, xd + 40, 112, .6), N(xd + 42, 115, "½ dᵀ∇²f d: curvature lifts back up", 7, "start"),
        N(xd - 7, 112, "f(x + d)", 8, "end"), L(xd - 6, 108, xd - 2, f(xd) + 3, .6),
        N(120, 10, "f(x + d) = f(x) + ∇f(x)ᵀd + ½ dᵀ∇²f d", 8, "middle"), N(120, 21, "altimeter + slope gauge + curvature gauge", 7, "middle"))
D[201] = (d201, "Starting at altitude f(x), fly a step d. The tangent (dashed) predicts the slope term ∇f(x)ᵀd; the gap between the tangent and the real ground is the curvature term ½dᵀ∇²f d. Their sum gives f(x + d).")

def d203(c):
    up = bowl(62, 100, 46, 54)
    dn = lambda x: 46 + 54 * ((x - 180) / 46) ** 2
    return svg(c, N(120, 10, "SONC at a minimum: ∇f(x*) = 0 and ∇²f(x*) ⪰ 0", 7.5, "middle"),
        poly(g(up, 16, 108, 2), 1.4), dash(44, 100, 80, 100, .9, "3 2"), C(62, 100, 2.4), plane(62, 90, 0, .5), N(62, 112, "∇f(x*) = 0 (flat)", 7.5, "middle"),
        N(62, 124, "dᵀ∇²f d ≥ 0 for every d", 7.5, "middle"), N(62, 136, "curves up: stays put ✓", 7.5, "middle"),
        L(122, 18, 122, 142, .7, d="2 3"),
        poly(g(dn, 134, 226, 2), 1.4, "5 3"), C(180, 46, 2.4), plane(180, 36, 0, .5), L(184, 44, 204, 52, 1, ar=True),
        N(180, 112, "one d with dᵀ∇²f d < 0", 7.5, "middle"), N(180, 124, "curves down along d", 7.5, "middle"), N(180, 136, "rolls away: not a min ✗", 7.5, "middle"))
D[203] = (d203, "At a minimum the floor is flat (∇f(x*) = 0) and curves up or stays flat in every direction: dᵀ∇²f(x*)d ≥ 0. If even one direction curved down, the plane would roll away along it.")

def d206(c):
    steep = bowl(62, 100, 18, 80)
    flat = bowl(182, 100, 46, 26)
    return svg(c, N(120, 10, "at (1, 1): ∇f = 0, slices along the two eigen-directions", 7.5, "middle"),
        poly(g(steep, 44, 80, 1), 1.4), C(62, 100, 2.4), plane(62, 90, 0, .45), N(62, 24, "across the canyon", 7.5, "middle"), N(62, 112, "λ₁ ≈ 1001.6", 8, "middle"),
        L(122, 18, 122, 120, .7, d="2 3"),
        poly(g(flat, 136, 228, 2), 1.4), C(182, 100, 2.4), plane(182, 90, 0, .45), N(182, 60, "along the canyon floor", 7.5, "middle"), N(182, 112, "λ₂ ≈ 0.4", 8, "middle"),
        N(120, 128, "det = λ₁λ₂ = 400 > 0, tr = λ₁ + λ₂ = 1002 > 0 ⇒ both λ > 0: strict min", 7, "middle"),
        N(120, 139, "κ = λ₁/λ₂ ≈ 2500: walls far steeper than the floor", 7, "middle"))
D[206] = (d206, "At (1, 1) the slope is zero. Slicing along the two eigen-directions of the Hessian: across the canyon the curvature is λ₁ ≈ 1001.6, along the floor only λ₂ ≈ 0.4. det = 400 > 0 and tr = 1002 > 0 say both are positive: a strict minimum, but with κ ≈ 2500.")

# ---------------- topic 3 ----------------
def d301(c):
    f = bowl(120, 110, 100, 78)
    xa, xb, t = 40, 200, .62
    xm = t * xa + (1 - t) * xb
    ym = t * f(xa) + (1 - t) * f(xb)
    return svg(c, *ground_axis(124), poly(g(f, 22, 220, 2), 1.4), L(xa, f(xa), xb, f(xb), 1.2, d="5 3"),
        C(xa, f(xa), 2.4), C(xb, f(xb), 2.4), N(xa - 4, f(xa) + 12, "f(x)", 8, "end"), N(xb + 4, f(xb) + 12, "f(y)", 8, "start"),
        dash(xa, f(xa) + 3, xa, 124, .7), dash(xb, f(xb) + 3, xb, 124, .7), N(xa, 135, "x", 8.5, "middle"), N(xb, 135, "y", 8.5, "middle"),
        dash(xm, ym, xm, 124, .7), N(xm, 135, "θx + (1−θ)y", 7.5, "middle"), C(xm, ym, 2.2), C(xm, f(xm), 2.2),
        N(xm + 5, ym - 3, "θf(x) + (1−θ)f(y): string", 7.5, "start"), N(xm + 5, f(xm) + 3, "f(θx + (1−θ)y): ground", 7.5, "start"),
        plane(xm - 30, t * f(xa) + (1 - t) * f(xb) - 8 + (xm - 30 - xm) * (f(xb) - f(xa)) / (xb - xa), math.degrees(math.atan((f(xb) - f(xa)) / (xb - xa))), .5),
        N(120, 10, "convex: ground ≤ string, for every θ ∈ [0, 1]", 7.5, "middle"))
D[301] = (d301, "Pick two ground points at x and y. Mixing them with weight θ gives the point θx + (1−θ)y; the string (straight flight) is at height θf(x) + (1−θ)f(y). Convexity says the ground f(θx + (1−θ)y) is never above the string.")

def d302(c):
    f = bowl(120, 92, 100, 78)
    x, y = 100, 180
    s = tangent(f, x)
    return svg(c, *ground_axis(124), poly(g(f, 22, 220, 2), 1.4), L(x - 46, f(x) - 46 * s, y + 30, f(x) + (y + 30 - x) * s, 1, d="6 3"),
        C(x, f(x), 2.4), plane(x, f(x) - 10, math.degrees(math.atan(s)), .5), N(x - 6, f(x) + 3, "f(x)", 8, "end"),
        dash(x, f(x) + 3, x, 124, .7), dash(y, f(y) + 3, y, 124, .7), N(x, 135, "x", 8.5, "middle"), N(y, 135, "y", 8.5, "middle"),
        C(y, f(y), 2.4), C(y, f(x) + (y - x) * s, 2.2), N(y - 5, f(y) + 2, "f(y)", 8, "end"),
        N(y - 5, f(x) + (y - x) * s + 10, "f(x) + ∇f(x)ᵀ(y − x)", 7.5, "end"), *vlab(y + 6, f(y) + 2, f(x) + (y - x) * s - 2, "gap ≥ 0", 3),
        N(120, 10, "f(y) ≥ f(x) + ∇f(x)ᵀ(y − x): the glide line never cuts the ground", 7.3, "middle"))
D[302] = (d302, "At x the glide line (tangent) predicts altitude f(x) + ∇f(x)ᵀ(y − x) at any other point y. On convex terrain the real ground f(y) is always at or above that prediction.")

def d303(c):
    f = bowl(120, 104, 100, 80)
    parts = [*ground_axis(124), poly(g(f, 22, 218, 2), 1.4)]
    for x in (50, 120, 186):
        parts += [C(x, f(x), 2), N(x, f(x) + 14, "∇²f ⪰ 0", 7.5, "middle")]
    parts += [plane(120, 94, 0, .5), N(120, 10, "convex on C ⇔ ∇²f(x) ⪰ 0 at every x ∈ C", 7.5, "middle"),
        N(120, 22, "the ground curves up (or is flat) everywhere, not just at one spot", 7, "middle"), N(120, 136, "check it at every point of the set", 7.5, "middle")]
    return svg(c, *parts)
D[303] = (d303, "Convexity is the Hessian test applied everywhere: ∇²f(x) ⪰ 0 at every point x of the set, so the ground never curves downward anywhere.")

def d304(c):
    f = lambda x: 104 - 80 * (abs((x - 120) / 100)) ** 1.6
    fl = bowl(120, 104, 100, 48)
    return svg(c, *ground_axis(124), poly(g(f, 22, 218, 2), 1.4), poly(g(fl, 22, 218, 2), 1, "5 3"),
        C(120, 104, 2.4), plane(120, 94, 0, .5), dash(120, 104, 120, 124, .7), N(120, 135, "x*", 8.5, "middle"),
        N(40, 30, "f(x)", 8, "middle"), N(200, 72, "f(x*) + μ/2 ‖x − x*‖²", 7.5, "end"), N(200, 82, "(the guaranteed floor)", 7, "end"),
        N(120, 10, "μ-strongly convex: ∇²f ⪰ μI, curvature never below μ", 7.5, "middle"))
D[304] = (d304, "Strong convexity means the curvature never drops below μ (∇²f ⪰ μI). Equivalently, the terrain always stays above the bowl f(x*) + μ/2‖x − x*‖², so leaving the bottom always costs altitude.")

def d305(c):
    f = bowl(120, 108, 100, 80)
    x = 60; s = tangent(f, x)
    return svg(c, *ground_axis(124), poly(g(f, 22, 218, 2), 1.4), dash(14, 108, 226, 108, .8, "4 3"), N(226, 104, "f*", 8, "end"),
        C(x, f(x), 2.4), plane(x, f(x) - 10, math.degrees(math.atan(s)), .5), L(x - 16, f(x) - 16 * s, x + 18, f(x) + 18 * s, 1, d="2 2"),
        N(x + 22, f(x) + 18 * s + 10, "slope ‖∇f(x)‖", 7.5, "start"), *vlab(x - 10, f(x), 108, "f(x) − f*", -3, "end"),
        N(120, 10, "PL: ‖∇f(x)‖² ≥ 2μ (f(x) − f*)", 8, "middle"), N(120, 21, "high above the floor ⇒ the slope must be steep", 7, "middle"),
        N(120, 136, "each 1/L hop: gap × (1 − μ/L)", 7.5, "middle"))
D[305] = (d305, "PL compares the steepness ‖∇f(x)‖ under the plane with its height f(x) − f* above the floor: steepness² ≥ 2μ × height. No flat plateau high up, so each 1/L hop shrinks the gap by the factor (1 − μ/L).")

def d306(c):
    p1 = [(18, 36), (34, 100), (66, 100), (82, 36)]
    q = lambda x: 100 - 60 * ((x - 120) / 30) ** 4
    b = bowl(200, 100, 30, 60)
    return svg(c, poly(p1, 1.4), plane(50, 90, 0, .45), N(50, 14, "convex", 8, "middle"), N(50, 114, "∇²f ⪰ 0", 7.5, "middle"), N(50, 125, "flat stretch allowed", 7, "middle"),
        L(90, 8, 90, 140, .7, d="2 3"),
        poly(g(q, 90, 150, 1), 1.4), plane(120, 90, 0, .45), N(120, 14, "strictly convex", 8, "middle"), N(120, 114, "x⁴: no flat stretch", 7.5, "middle"), N(120, 125, "but ∇²f(0) = 0", 7, "middle"),
        L(150, 8, 150, 140, .7, d="2 3"),
        poly(g(b, 170, 230, 2), 1.4), plane(200, 90, 0, .45), N(200, 14, "strongly convex", 8, "middle"), N(200, 114, "∇²f ⪰ μI", 7.5, "middle"), N(200, 125, "true bowl", 7, "middle"),
        N(120, 139, "μ-strongly ⇒ strictly ⇒ convex (not the other way)", 7.5, "middle"))
D[306] = (d306, "Convex allows flat stretches (∇²f ⪰ 0). Strictly convex forbids them, but x⁴ shows the curvature can still be 0 at a point. Strongly convex needs curvature at least μ everywhere (∇²f ⪰ μI): a true bowl.")

FIX = {cid: {"drawingSvg": fn(cid), "drawingCaption": cap, "textbookImg": None, "textbookRef": None} for cid, (fn, cap) in D.items()}
