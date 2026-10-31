"""CMO topics 4-6: every diagram labels the terms of the formula on its card.
Small fixes relabel the existing drawing (relabel); the rest are redrawn."""
import math, glob, os, importlib
from air_lib import *
from cmo_refine_zzz_curves import g, bowl, tangent
from cmo_refine_zzzz_formula_a import vlab, ground_axis

_here = os.path.dirname(os.path.abspath(__file__))
_me = os.path.basename(__file__)

def prev_svg(cid):
    """the drawing an earlier patch module produced for this card"""
    out = None
    for p in sorted(glob.glob(os.path.join(_here, "cmo_refine_*.py"))):
        name = os.path.basename(p)
        if name >= _me: break
        fx = getattr(importlib.import_module(name[:-3]), "FIX", {}).get(cid, {})
        if "drawingSvg" in fx: out = fx["drawingSvg"]
    assert out, cid
    return out

def relabel(cid, *pairs):
    s = prev_svg(cid)
    for a, b in pairs:
        a = a.replace("<", "&lt;"); b = b.replace("<", "&lt;")
        assert f">{a}<" in s, (cid, a)
        s = s.replace(f">{a}<", f">{b}<", 1)
    return s

D = {}

def slice_fig(c, title, slope, curv, bottom, flat, foot):
    """altitude along one heading: start slope, curvature, bottom (701 style, reused)"""
    oy = 112
    h = lambda a: 62 * ((a - 130) / 100) ** 2 + 4
    y = lambda a: oy - h(a)
    s0 = y(30.5) - y(29.5)
    return svg(c, N(120, 10, title, 8, "middle"), L(22, oy, 232, oy, 1, ar=True), N(234, oy + 3, "α", 8.5, "start"), poly(g(y, 30, 230, 2), 1.4),
        plane(34, y(30) - 9, 50, .55), C(30, y(30), 2.2), dash(30, y(30), 50, y(30) + 20 * s0, 1, "2 2"),
        N(54, 44, slope, 7.5, "start"), N(54, 54, "(downward momentum)", 7, "start"),
        N(130, 72, curv, 7.5, "middle"), N(130, 82, "(curvature = the brakes)", 7, "middle"),
        C(130, y(130), 2.6), dash(110, y(130), 150, y(130), .8, "3 2"), dash(130, y(130) + 3, 130, oy), N(130, oy + 10, "α*", 8.5, "middle"),
        N(156, y(130) - 3, flat, 7.5, "start"), N(120, 136, bottom, 8, "middle"), N(120, 145 - 1, foot, 6.8, "middle") if foot else "")

D[401] = (lambda c: relabel(c, ("αₖ = how far to fly", "xₖ₊₁ = xₖ + αₖdₖ")),
    "Side view of the valley. The plane sits at xₖ; its nose dₖ must point downhill (∇fᵀdₖ < 0). The new position is xₖ₊₁ = xₖ + αₖdₖ, where αₖ is how far it flies before reading the radar again.")

D[402] = (lambda c: slice_fig(c, "exact line search: fly to the slice bottom", "slope ∇f(xₖ)ᵀdₖ < 0", "dₖᵀQdₖ",
        "α* = −∇f(xₖ)ᵀdₖ / dₖᵀQdₖ", "∇f(xₖ₊₁)ᵀdₖ = 0 (flat)", ""),
    "Slice the quadratic valley along dₖ: the start slope is ∇f(xₖ)ᵀdₖ and the curvature is dₖᵀQdₖ. The bottom of that parabola is at α* = −∇f(xₖ)ᵀdₖ / dₖᵀQdₖ, where the slope along dₖ is zero: ∇f(xₖ₊₁)ᵀdₖ = 0.")

def d403(c):
    ox, oy = 26, 120
    h = lambda a: 70 * ((a - 130) / 100) ** 2
    y = lambda a: oy - 12 - h(a)
    s0 = (y(ox + .5) - y(ox - .5))
    arm = lambda a: y(ox) + .25 * s0 * (a - ox)
    a1 = max(a for a in range(ox + 1, 228) if y(a) >= arm(a))
    return svg(c, L(ox, oy, 232, oy, 1, ar=True), N(235, oy + 3, "α", 9, "start"), poly(g(y, ox, 228), 1.4),
        dash(ox, y(ox), ox + 30, y(ox) + 30 * s0, 1, "2 2"), N(ox + 30, y(ox) + 30 * s0 + 12, "f(xₖ) + α∇fᵀdₖ", 7.2, "middle"),
        L(ox, y(ox), 220, arm(220), 1, d="6 3"), N(150, arm(150) - 6, "f(xₖ) + c₁α∇fᵀdₖ", 7.2, "middle"),
        N(226, 34, "f(xₖ + αdₖ)", 7.5, "end"), C(ox, y(ox), 2.2), N(ox + 4, y(ox) - 4, "f(xₖ)", 7.5, "start"),
        plane(ox + 6, y(ox) - 12, 30, .55), L(ox + 1, oy + 8, a1, oy + 8, 1.4), dash(a1, arm(a1), a1, oy + 8),
        N((ox + a1) / 2, oy + 19, "accepted α: curve below the Armijo line", 7.5, "middle"),
        N(130, 10, "Armijo: f(xₖ + αdₖ) ≤ f(xₖ) + c₁α∇f(xₖ)ᵀdₖ, c₁ ∈ (0, 1)", 7.3, "middle"))
D[403] = (d403, "The altitude along the heading is f(xₖ + αdₖ). The tangent f(xₖ) + α∇fᵀdₖ is the full promised drop; Armijo's line f(xₖ) + c₁α∇fᵀdₖ asks only for a fraction c₁ of it. A hop α is accepted while the curve stays below that line.")

def d404(c):
    ox, oy = 26, 118
    h = lambda a: 70 * ((a - 140) / 110) ** 2
    y = lambda a: oy - 12 - h(a)
    sl = lambda a: y(a + .5) - y(a - .5)
    s0 = sl(30)
    a_bad, a_ok = 60, 128
    return svg(c, L(ox, oy, 232, oy, 1, ar=True), N(235, oy + 3, "α", 9, "start"), poly(g(y, 30, 230), 1.4),
        plane(34, y(30) - 10, 40, .55), dash(30, y(30), 52, y(30) + 22 * s0, 1, "2 2"), N(56, y(30) + 22 * s0 - 2, "∇f(xₖ)ᵀdₖ: start slope", 7.2, "start"),
        C(a_bad, y(a_bad), 2.2), dash(a_bad - 14, y(a_bad) - 14 * sl(a_bad), a_bad + 14, y(a_bad) + 14 * sl(a_bad), 1, "2 2"), N(a_bad - 4, y(a_bad) + 16, "still steep ✗", 7.2, "end"),
        C(a_ok, y(a_ok), 2.4), dash(a_ok - 20, y(a_ok) - 20 * sl(a_ok), a_ok + 20, y(a_ok) + 20 * sl(a_ok), 1, "2 2"), N(a_ok, y(a_ok) + 14, "flattened ✓", 7.2, "middle"),
        N(a_ok + 4, y(a_ok) - 12, "∇f(xₖ + αdₖ)ᵀdₖ", 7.2, "start"),
        N(130, 10, "|∇f(xₖ + αdₖ)ᵀdₖ| ≤ c₂ |∇f(xₖ)ᵀdₖ|", 8, "middle"), N(130, 21, "the slope at the landing must have flattened to a fraction c₂", 7, "middle"),
        N(130, 138, "0 < c₁ < c₂ < 1: Armijo + this = strong Wolfe", 7.3, "middle"))
D[404] = (d404, "Compare the slope along the heading at the start, ∇f(xₖ)ᵀdₖ, with the slope where the hop lands, ∇f(xₖ + αdₖ)ᵀdₖ. Strong Wolfe accepts the landing only if its slope has flattened to at most c₂ times the start slope, so tiny hops that stop on a steep slope are refused.")

D[406] = (lambda c: relabel(c, ("α₀/2 ✗", "ρα₀ ✗"), ("α₀/4 ✓", "ρ²α₀ ✓"), ("too big? halve it and look again", "α ← ρα until Armijo holds (ρ ∈ (0,1))")),
    "Start with a long trial hop α₀. If it fails Armijo (the dashed line), shrink it, α ← ρα, and test again, until f(x + αd) ≤ f(x) + c₁α∇f(x)ᵀd holds.")

D[501] = (lambda c: relabel(c, ("simple, but blind to the valley's curvature", "xₖ₊₁ = xₖ − αₖ∇f(xₖ); stop when ‖gₖ‖ ≤ tol·‖g₀‖")),
    "The slope gauge ∇f points to steepest uphill; steepest descent flies the other way, dₖ = −∇f, so xₖ₊₁ = xₖ − αₖ∇f(xₖ). It stops once the gauge reads almost flat: ‖gₖ‖ ≤ tol·‖g₀‖.")

D[508] = (lambda c: relabel(c, ("seen across the canyon: each hop stops where", "each hop αₖ = −gₖᵀuₖ / uₖᵀQuₖ stops where"),
                           ("exact line search: gₖ₊₁ ⊥ gₖ, so the path zig-zags", "(xₖ₊₂ − xₖ₊₁)ᵀ(xₖ₊₁ − xₖ) = 0: consecutive hops ⊥")),
    "Looking along the canyon: each exact hop αₖ = −gₖᵀuₖ / uₖᵀQuₖ flies until the ground along it is flat, which is on the opposite wall. The next hop is at 90° to it, (xₖ₊₂ − xₖ₊₁)ᵀ(xₖ₊₁ − xₖ) = 0, so the path zig-zags wall to wall.")

D[503] = (lambda c: relabel(c, ("ρ = 1 − μ/L", "ρ = (κ−1)/(κ+1), κ = L/μ"), ("gap × ρ per hop", "‖xₖ − x*‖ × ρ per hop")),
    "Each hop multiplies the distance to the bottom ‖xₖ − x*‖ by the same factor ρ = (κ − 1)/(κ + 1), with κ = L/μ, so the error shrinks geometrically.")

D[504] = (lambda c: relabel(c, ("worst-case shrink = ((κ−1)/(κ+1))²", "E(xₖ₊₁) ≤ ((κ−1)/(κ+1))² E(xₖ)"), ("shrink per hop", "E(xₖ₊₁)/E(xₖ)")),
    "Kantorovich's inequality bounds how badly −g can miss the valley's axis, giving E(xₖ₊₁) ≤ ((κ − 1)/(κ + 1))² E(xₖ). A round bowl (κ = 1) needs one hop; a thin canyon (large κ) gives a factor near 1, so the pilot crawls.")

D[505] = (lambda c: relabel(c, ("κ = steepest wall ÷ gentlest floor curvature", "κ = λmax/λmin; (κ−1)/(κ+1) → 1 as κ → ∞: stagnation"),
                           ("κ ≈ 1: round bowl", "λmax ≈ λmin: κ ≈ 1"), ("κ large: thin canyon", "λmax ≫ λmin: κ large")),
    "κ = λmax/λmin compares the steepest wall curvature with the gentlest floor curvature. With κ ≈ 1 one hop reaches the bottom; with large κ the factor (κ − 1)/(κ + 1) → 1 and the plane stagnates, bouncing wall to wall.")

D[506] = (lambda c: relabel(c, ("how far you flew (s)", "s = xₖ − xₖ₋₁ (how far you flew)"), ("vs how the slope changed (y)", "y = gₖ − gₖ₋₁ (how the slope changed)"),
                           ("α = sᵀs / sᵀy", "BB1: α = sᵀs / sᵀy"), ("(no radar sweep)", "BB2: α = sᵀy / yᵀy")),
    "Barzilai-Borwein sizes the next hop from the last two footprints: s = xₖ − xₖ₋₁ is how far you flew and y = gₖ − gₖ₋₁ is how much the slope changed. BB1 uses sᵀs/sᵀy, BB2 uses sᵀy/yᵀy.")

D[507] = (lambda c: relabel(c, ("keeps bouncing", "rate (κ−1)/(κ+1)"), ("bounces die out fast", "rate (√κ−1)/(√κ+1)")),
    "Across the canyon: plain steepest descent keeps bouncing and shrinks the error by (κ − 1)/(κ + 1) per hop. Momentum adds β(xₖ − xₖ₋₁) to the −α∇f step, the swings cancel, and the rate improves to (√κ − 1)/(√κ + 1).")

D[601] = (lambda c: relabel(c, ("model bottom", "xₖ + pₖ, with ∇²f pₖ = −∇f")),
    "Newton's autopilot reads the slope ∇f(xₖ) and curvature ∇²f(xₖ), fits a parabola (dashed), and flies to its bottom: solve ∇²f(xₖ)pₖ = −∇f(xₖ), then xₖ₊₁ = xₖ + pₖ.")

D[602] = (lambda c: relabel(c, ("correct digits double each hop", "‖xₖ₊₁ − x*‖ ≤ (L/2m)‖xₖ − x*‖²: digits double")),
    "Inside the final approach bubble the error is squared each hop, ‖xₖ₊₁ − x*‖ ≤ (L/2m)‖xₖ − x*‖², so the number of correct digits doubles: superlinear convergence.")

D[603] = (lambda c: relabel(c, ("negative curvature: parabola opens downward", "∇²f ⊁ 0: hill model, pₖᵀ∇f can be > 0")),
    "When the Hessian is not positive definite the fitted parabola opens downward (a hill). Newton then flies to the model's peak, and pₖ need not be a descent direction: pₖᵀ∇f(xₖ) can be positive.")

D[604] = (lambda c: relabel(c, ("α<1", "α = βᵐ < 1"), ("short cautious hops → full unit steps", "far: backtrack α = βᵐ; near x*: α = 1 accepted")),
    "Far from the bottom the full Newton step fails Armijo, so backtrack: α = βᵐ. Close to x* (with c₁ < 1/2) the unit step α = 1 passes, and full Newton speed returns.")

D[605] = (lambda c: relabel(c, ("add τI: the model becomes a bowl", "(H + τI)p = −∇f, τ ≥ −λmin + δ: a bowl"), ("τ→0 Newton · τ→∞ short gradient hop", "τ → 0: Newton · τ → ∞: short −∇f hop")),
    "If H has a negative eigenvalue the model is a hill. Adding τI with τ ≥ −λmin(H) + δ lifts every curvature above zero, so (H + τI)p = −∇f is a bowl. Small τ is Newton; huge τ is a short gradient hop.")

D[606] = (lambda c: relabel(c, ("Newton: 2–3 hops", "Newton: p = −H⁻¹g = (1, 0)"), ("Rosenbrock banana canyon", "at (0,0): g = (−2, 0), H = diag(2, 200), κ = 100")),
    "At (0, 0) on Rosenbrock: g = (−2, 0) and H = diag(2, 200), so κ = 100. Newton's step p = −H⁻¹g = (1, 0) goes straight along the canyon, while gradient descent switchbacks between its steep walls.")

FIX = {cid: {"drawingSvg": fn(cid), "drawingCaption": cap, "textbookImg": None, "textbookRef": None} for cid, (fn, cap) in D.items()}
