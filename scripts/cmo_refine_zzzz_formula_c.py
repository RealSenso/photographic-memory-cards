"""CMO topics 8-19: every diagram labels the terms of the formula on its card.
Most figures keep their drawing and get the formula's symbols (relabel / add);
8.02-8.04 are redrawn term by term."""
import glob, os, importlib, json
from air_lib import *

_here = os.path.dirname(os.path.abspath(__file__))
_me = os.path.basename(__file__)
_cards = None

def prev_svg(cid):
    """the drawing an earlier patch module produced for this card (else the one in cards_data.js)"""
    global _cards
    out = None
    for p in sorted(glob.glob(os.path.join(_here, "cmo_refine_*.py"))):
        name = os.path.basename(p)
        if name >= _me: break
        fx = getattr(importlib.import_module(name[:-3]), "FIX", {}).get(cid, {})
        if "drawingSvg" in fx: out = fx["drawingSvg"]
    if out is None:
        if _cards is None:
            t = open(os.path.join(_here, "..", "cards_data.js")).read()
            _cards = {c["id"]: c for c in json.loads(t[t.index("["):t.rindex("]") + 1])}
        out = _cards[cid]["drawingSvg"]
    return out

def relabel(cid, *pairs, add=()):
    """swap label texts (first match each), then append extra parts before </svg>"""
    s = prev_svg(cid)
    for a, b in pairs:
        a = a.replace("<", "&lt;"); b = b.replace("<", "&lt;")
        if f">{a}<" in s:
            s = s.replace(f">{a}<", f">{b}<", 1)
        else:
            assert f">{b}<" in s, (cid, a)   # already relabelled in cards_data.js
    extra = "".join(add)
    if extra and extra not in s:
        s = s.replace("</svg>", extra + "</svg>")
    return s

def terms_fig(c, title, terms, notes):
    """a formula laid out as boxes, one per term, with what each term does underneath"""
    widths = [max(len(t) * 5.0 + 10, 14) if m is not None else 10 for t, m, _ in terms]
    gap = 4
    x = 120 - (sum(widths) + gap * (len(terms) - 1)) / 2
    parts = [N(120, 16, title, 8.5, "middle")]
    for (t, m, shade), w in zip(terms, widths):
        if m is None:
            parts.append(N(x + w / 2, 62, t, 10, "middle"))
        else:
            parts += [R(x, 46, w, 26, "#d9dee7" if shade else "#f1f5f9", 1, 3), N(x + w / 2, 63, t, 8.5, "middle")]
            for k, line in enumerate(m.split("|")):
                parts.append(N(x + w / 2, 84 + 9 * k, line, 6.8, "middle"))
        x += w + gap
    for k, line in enumerate(notes):
        parts.append(N(120, 118 + 11 * k, line, 7.5, "middle"))
    return svg(c, *parts, plane(224, 14, 0, .45))

D = {}

# ---------- topic 8: quasi-Newton ----------
D[801] = (lambda c: relabel(c, ("s = step flown", "sₖ = xₖ₊₁ − xₖ (hop)"), ("y = gₖ₊₁ − gₖ", "yₖ = gₖ₊₁ − gₖ"),
                           ("curvature ≈ y / s", "curvature ≈ yₖ / sₖ"), ("secant: B s = y", "Bₖ₊₁sₖ = yₖ ⇔ Hₖ₊₁yₖ = sₖ")),
    "The hop sₖ = xₖ₊₁ − xₖ and the change in slope yₖ = gₖ₊₁ − gₖ come free from the flight log. Their ratio is the curvature along the hop, so the new model must satisfy the secant equation Bₖ₊₁sₖ = yₖ (equivalently Hₖ₊₁yₖ = sₖ).")

D[802] = (lambda c: terms_fig(c, "SR1:  Bₖ₊₁ = Bₖ + r rᵀ / rᵀsₖ,   r = yₖ − Bₖsₖ", [
        ("Bₖ", "old curvature|model", False), ("+", None, False), ("r rᵀ", "one correction,|only along r", True),
        ("/", None, False), ("rᵀsₖ", "scale so that|Bₖ₊₁sₖ = yₖ", True)],
        ["r = yₖ − Bₖsₖ: how far the old model misses the secant", "rᵀsₖ ≈ 0: dividing by ~0, so skip this update"]),
    "SR1 measures the miss r = yₖ − Bₖsₖ (what the old model predicts for the hop versus what the slope really did) and adds one rank-1 correction r rᵀ / rᵀsₖ along it, which makes Bₖ₊₁sₖ = yₖ. If rᵀsₖ is nearly zero the update is skipped.")

D[803] = (lambda c: terms_fig(c, "DFP:  Hₖ₊₁ = Hₖ + sₖsₖᵀ / sₖᵀyₖ − HₖyₖyₖᵀHₖ / yₖᵀHₖyₖ", [
        ("Hₖ", "old inverse|model", False), ("+", None, False), ("s sᵀ / sᵀy", "add the hop|you flew", True),
        ("−", None, False), ("Hy yᵀH / yᵀHy", "remove the old|guess along y", True)],
        ["result: Hₖ₊₁yₖ = sₖ (the secant equation holds)", "two rank-1 pieces: rank-2 update"]),
    "DFP updates the inverse model H directly with two rank-1 terms: + sₖsₖᵀ/sₖᵀyₖ puts in the hop just flown, − HₖyₖyₖᵀHₖ/yₖᵀHₖyₖ takes out what the old model said along yₖ. Together they give Hₖ₊₁yₖ = sₖ.")

D[804] = (lambda c: terms_fig(c, "BFGS:  Hₖ₊₁ = (I − ρsyᵀ) Hₖ (I − ρysᵀ) + ρssᵀ", [
        ("I − ρsyᵀ", "wipe the old|info along y", False), ("Hₖ", "old|model", False), ("I − ρysᵀ", "wipe the old|info along y", False),
        ("+", None, False), ("ρ s sᵀ", "add the hop|you flew", True)],
        ["ρₖ = 1 / yₖᵀsₖ > 0 (Wolfe guarantees it)", "⇒ Hₖ₊₁ ≻ 0: the nose always points downhill"]),
    "BFGS sandwiches the old inverse model Hₖ between (I − ρsyᵀ) and (I − ρysᵀ), which wipe out its old information along the latest hop, then adds ρssᵀ for the hop just flown. With ρₖ = 1/yₖᵀsₖ > 0 the new Hₖ₊₁ stays positive definite.")

D[805] = (lambda c: relabel(c, ("s", "sₖ"), ("y", "yₖ"), ("s", "sₖ"), ("y", "yₖ"),
                           ("sᵀy > 0 ✓ trust it", "sₖᵀyₖ > 0 ⇔ Hₖ₊₁ ≻ 0 ✓"), ("sᵀy ≤ 0 ✗ refuse", "sₖᵀyₖ ≤ 0 ✗ refuse")),
    "Left: the ground curves up along the hop, so the slope change yₖ points with sₖ and sₖᵀyₖ > 0; then the BFGS update stays positive definite. Right: the ground sags, sₖᵀyₖ ≤ 0 and the update must be refused. The Wolfe curvature condition ∇f(xₖ + αpₖ)ᵀpₖ ≥ c₂∇f(xₖ)ᵀpₖ guarantees the left case.")

D[806] = (lambda c: relabel(c, ("L-BFGS: keep only the last m hops", "L-BFGS: keep the last m pairs (sᵢ, yᵢ)"),
                           ("last m kept", "m pairs: O(mn) memory"),
                           ("nearly the same guidance, a fraction of the memory", "start from H₀ᵏ = γₖI, γₖ = sᵀy / ‖y‖²")),
    "L-BFGS keeps only the last m (s, y) pairs, so memory is O(mn) instead of O(n²). Each step starts from the scaled identity H₀ᵏ = γₖI with γₖ = sₖ₋₁ᵀyₖ₋₁/‖yₖ₋₁‖² and replays the m stored updates.")

# ---------- topic 9: feasible set, tangent cone ----------
D[901] = (lambda c: relabel(c, ("only g₁ is touching x*; g₂, g₃ are far away", "𝒜(x*) = {1}: g₁(x*) = 0; g₂, g₃ < 0")),
    "Ω = {x : hᵢ(x) = 0, gⱼ(x) ≤ 0} is the legal airspace. At x* only wall g₁ is touched, g₁(x*) = 0, so the active set is 𝒜(x*) = {1}; walls g₂ and g₃ are strictly negative there and do not matter locally.")

D[902] = (lambda c: relabel(c, ("t_k ↓ 0", "tₖ ↓ 0"), ("h(x)=0", "h(x) = 0"), ("d = lim (x_k − x*) / t_k", "ẋ(t*) = d = lim (xₖ − x*) / tₖ"),
                           add=(N(14, 22, "M = {y : ∇h(x*)ᵀy = 0}", 7.5, "start"),)),
    "Legal points x₁, x₂, x₃ on the runway h(x) = 0 approach x*. The directions (xₖ − x*)/tₖ tend to the tangent vector d = ẋ(t*). All such d form the tangent plane M = {y : ∇h(x*)ᵀy = 0}, at right angles to ∇h(x*).")

D[903] = (lambda c: relabel(c, ("T_Ω(x*)", "T(x*)"), add=(N(236, 140, "d = lim (xₖ − x*)/tₖ,  xₖ ∈ Ω,  tₖ ↓ 0", 7, "end"),)),
    "The tangent cone T(x*) collects every heading d you can reach as a limit of legal points: d = lim (xₖ − x*)/tₖ with xₖ ∈ Ω and tₖ ↓ 0. If d is in it, so is any λd with λ ≥ 0.")

D[905] = (lambda c: relabel(c, ("∇f·d ≥ 0", "∇f(x*)ᵀd ≥ 0"), ("for every legal d", "for every d in the tangent cone")),
    "At a local minimum x* on Ω, no legal heading goes downhill: ∇f(x*)ᵀd ≥ 0 for every d in the tangent cone T(x*). The only downhill direction −∇f points into the rock.")

D[906] = (lambda c: relabel(c, ("L = the whole x₁-axis, also ← into the rock", "L = {d : ∇gⱼᵀd ≤ 0} = the whole x₁-axis")),
    "At the cusp x* = 0 the walls' normals are parallel, so LICQ fails. The true tangent cone T is only the ray to the right, but the linearized cone L = {d : ∇gⱼᵀd ≤ 0} is the whole x₁-axis, including headings into the rock. With LICQ, T = L.")

# ---------- topic 10: separation, Farkas ----------
D[1001] = (lambda c: relabel(c, ("one flat wall: aᵀx ≤ b on A's side, ≥ b on B's", "sup over A of aᵀx ≤ β ≤ inf over B of aᵀy")),
    "Two disjoint convex airspaces A and B can be split by one flat wall with normal a ≠ 0: every x in A has aᵀx ≤ β and every y in B has aᵀy ≥ β, i.e. sup over A of aᵀx ≤ inf over B of aᵀy.")

D[1002] = (lambda c: relabel(c, ("whole airspace lies on one side: aᵀx ≤ aᵀx₀", "x₀ ∈ ∂C:  aᵀx ≤ aᵀx₀ for all x ∈ C")),
    "At any boundary point x₀ of a convex set C there is a supporting wall with normal a ≠ 0 that touches C at x₀ and has all of C on one side: aᵀx ≤ aᵀx₀ for every x ∈ C.")

D[1003] = (lambda c: relabel(c, ("b inside: walls hold ✓", "b = Ax, x ≥ 0 ✓"), ("b outside: y proves it ✗", "Aᵀy ≥ 0, bᵀy < 0 ✗")),
    "Exactly one holds. Either b is inside the cone of the columns a₁, a₂, so b = Ax with x ≥ 0; or b is outside and a wall normal y separates it: Aᵀy ≥ 0 (every column on one side) but bᵀy < 0 (b on the other).")

D[1007] = (lambda c: relabel(c, ("y", "y: Aᵀy = (1, 0) ≥ 0"), ("b′ ✗", "b′ ✗"), add=(N(10, 16, "b′ᵀy = −1 < 0  ⇒  b′ ∉ cone(a₁, a₂)", 7.5, "start"),)),
    "With real numbers: y gives Aᵀy = (1, 0) ≥ 0, so both columns are on y's side, while b′ᵀy = −1 < 0. That y certifies b′ ∉ cone(a₁, a₂). The point b inside the cone has no such certificate.")

D[1004] = (lambda c: relabel(c, ("open sky: Ax < 0", "∃x: Ax < 0"), ("tilt away from all walls", "aᵢᵀx < 0 for every row aᵢ"),
                            ("boxed in: Σ yᵢaᵢ = 0", "Aᵀy = Σ yᵢaᵢ = 0, y ≥ 0, y ≠ 0")),
    "Gordan: exactly one holds. Either some heading x makes aᵢᵀx < 0 for every row (Ax < 0, open sky), or the rows box you in: nonnegative weights y ≠ 0 make the pushes cancel, Aᵀy = Σ yᵢaᵢ = 0.")

D[1005] = (lambda c: relabel(c, ("K legal headings · K° safe pulls", " "), add=(N(8, 16, "K* = {y : yᵀx ≥ 0 for all x ∈ K}", 7.5, "start"), N(8, 27, "K° = −K*", 7.5, "start"))),
    "The dual cone K* holds every y making a non-obtuse angle with all of K: yᵀx ≥ 0 for every x ∈ K. The polar cone is its mirror, K° = −K*. Taking the dual twice gives K back exactly when K is closed and convex.")

D[1006] = (lambda c: relabel(c, ("push₁", "μ₁∇g₁"), ("push₂", "μ₂∇g₂"), ("μ ≥ 0", "μⱼ ≥ 0, j ∈ 𝒜(x*)")),
    "Farkas applied at x*: there is no heading with ∇fᵀd < 0 and ∇gⱼᵀd ≤ 0, so −∇f(x*) must lie in the cone of the active wall normals: −∇f = μ₁∇g₁ + μ₂∇g₂ with μⱼ ≥ 0. That is the KKT balance.")

# ---------- topic 11: KKT ----------
D[1101] = (lambda c: relabel(c, ("gravity −∇f", "gravity −∇f(x*)"), ("wall push μ∇g", "wall push μ*∇g(x*)"),
                            ("1. ∇f + μ∇g = 0 (balance)", "1. ∇f + Σλᵢ∇hᵢ + Σμⱼ∇gⱼ = 0"), ("3. μ ≥ 0 (walls only push)", "3. μⱼ* ≥ 0 (walls only push)"),
                            ("4. μg = 0 (push only if touching)", "4. μⱼ*gⱼ(x*) = 0 (push if touching)")),
    "Parked against the wall, gravity −∇f(x*) is cancelled by the wall's push μ*∇g(x*). KKT: (1) ∇f + Σλᵢ∇hᵢ + Σμⱼ∇gⱼ = 0, (2) the point is legal, (3) μⱼ* ≥ 0, (4) μⱼ*gⱼ(x*) = 0.")

D[1102] = (lambda c: relabel(c, ("gap", "gap −gⱼ(x*)"), ("g < 0 : OFF", "gⱼ(x*) < 0 ⇒ μⱼ* = 0"), ("μ = 0, no push", "switch OFF: no push"),
                            ("μ>0", "μⱼ* > 0"), ("g = 0 : ON", "⇒ gⱼ(x*) = 0"), ("wall pushes back", "switch ON: wall pushes")),
    "μⱼ*gⱼ(x*) = 0 works like a switch. Left: a gap to the wall, gⱼ(x*) < 0, forces μⱼ* = 0 (no push). Right: a push μⱼ* > 0 forces gⱼ(x*) = 0 (touching).")

D[1103] = (lambda c: relabel(c, ("global min", "x*: global min"), ("convex valley, flat walls: one lowest spot", "f, gⱼ convex, hᵢ affine"),
                            ("KKT holds  ⇒  global minimum", "KKT ⇒ f(x*) ≤ f(x) for all x ∈ Ω")),
    "In a convex valley (f and every gⱼ convex) with flat equality walls (hᵢ affine), any KKT point is a global minimum: f(x*) ≤ f(x) for every legal x.")

D[1104] = (lambda c: relabel(c, ("LICQ holds", "rank[∇g₁ ∇g₂] = 2 ✓"), ("LICQ fails (cusp)", "rank = 1 < 2: LICQ fails")),
    "LICQ asks that the active wall normals be linearly independent: rank[∇hᵢ, ∇gⱼ (j ∈ 𝒜)] = p + |𝒜|. Left: two independent normals, rank 2. Right: at a cusp the normals are parallel, rank 1, and KKT multipliers may not exist.")

D[1105] = (lambda c: relabel(c, ("x̄", "x̂"), ("room inside: g < 0 strictly ✓", "gⱼ(x̂) < 0 strictly ⇒ d* = p*"),
                            ("Slater fails", "no x̂ with g < 0: gap possible")),
    "Slater: if some x̂ lies strictly inside every inequality wall (gⱼ(x̂) < 0) and satisfies Ax̂ = b, a convex program has zero duality gap, d* = p*. On the right the legal set is a knife edge with no interior, so the guarantee is lost.")

D[1106] = (lambda c: relabel(c, ("free bottom: illegal ✗", "μ = 0: free bottom, illegal ✗"),
                            ("Case 2: park against the wall, push μ* > 0 ✓", "Case 2: x* = (4/5, 1/5), μ* = 8/5 > 0 ✓")),
    "Case 1 (μ = 0): the free valley bottom lies past the wall, so it is illegal. Case 2 (wall active): solve (2x₁, 8x₂) + μ*(−1, −1) = 0 on the wall, giving x* = (4/5, 1/5) and μ* = 8/5 > 0, so this case survives.")

# ---------- topic 12: second order ----------
D[1201] = (lambda c: relabel(c, ("(tangent directions M)", "(d ∈ M: ∇hᵀd = 0)"), ("test dᵀ∇²L d ≥ 0 only for d on the runway", "dᵀ∇²ₓₓL d ≥ 0 only for d ∈ M(x*)")),
    "Second-order necessary condition: along the runway (tangent directions M, where ∇hᵀd = 0) the Lagrangian must curve up, dᵀ∇²ₓₓL d ≥ 0. Across the runway it may curve down; those directions are illegal and ignored.")

D[1202] = (lambda c: relabel(c, ("strict bowl along every critical direction", "dᵀ∇²L d > 0 ∀ d ∈ M ∖ {0}"), ("dᵀ∇²L d ≥ c‖d‖² > 0", "⇒ x* is a strict local min")),
    "Second-order sufficient condition: if the Lagrangian curves strictly up along every nonzero critical direction, dᵀ∇²ₓₓL d > 0 for all d ∈ M ∖ {0}, then x* is a strict local minimizer.")

D[1203] = (lambda c: relabel(c, ("(−1)^m × minors", "sign det B₂ₚ₊ₘ = (−1)ᵖ"), ("alternate in sign", "for m = 1, …, n − p"), ("⇒ runway dips", "⇒ strict local min"),
                            ("border the Hessian with the wall normals", "B = [0  J; Jᵀ  ∇²L], J = wall normals")),
    "Border ∇²L with the constraint gradients J to form B. Check the last n − p leading minors: if sign det B₂ₚ₊ₘ = (−1)ᵖ for m = 1, …, n − p, the Lagrangian curves up along the runway and x* is a strict local minimum.")

D[1204] = (lambda c: relabel(c, ("critical cone = {0}", "C = Null[∇h, ∇g𝒜]ᵀ"), ("critical cone = a wedge", "C = wedge: ∇gⱼᵀd ≤ 0")),
    "Strict complementarity: every active wall pushes, μⱼ* > 0, so the plane is pinned and the critical cone is the null space C = Null[∇hᵀ; ∇g𝒜ᵀ]. If some μⱼ = 0 the plane can peel off that wall and C becomes a wedge (∇gⱼᵀd ≤ 0).")

D[1205] = (lambda c: relabel(c, ("bank pushes", "λ*∇²h: the bank"), ("∇²f alone: flat or negative", "dᵀ∇²f d alone: ≤ 0"),
                            ("∇²f + μ∇²g > 0 ✓", "dᵀ[∇²f + Σλᵢ∇²hᵢ]d > 0 ✓")),
    "Along a curved runway, the true second derivative of altitude is dᵀ∇²f d + ∇fᵀẍ. The ∇fᵀẍ part is the bank's push, and it equals dᵀ(Σλᵢ∇²hᵢ)d. So the Hessian of f alone can look flat or negative while ∇²f + Σλᵢ∇²hᵢ is positive.")

D[1206] = (lambda c: relabel(c, ("det B < 0", "det B = −4√2 < 0"), ("⇒ min ✓", "= (−1)¹ ⇒ min ✓"), ("x₁+x₂", "f = x₁ + x₂")),
    "Minimise f = x₁ + x₂ on the ring x₁² + x₂² = 1. At the south-west point the bordered Hessian has det B = −4√2 < 0, which matches (−1)ᵖ with p = 1, so it is a strict local minimum.")

# ---------- topic 13: projection ----------
D[1301] = (lambda c: relabel(c, ("Ω", "C"), ("P(p)", "p = Π(x)"), ("p", "x"), ("(p−P)ᵀ(y−P) ≤ 0", "⟨x − p, y − p⟩ ≤ 0")),
    "Project x onto the closed convex set C: p = Π(x) is the nearest legal point. It is characterised by the angle test ⟨x − p, y − p⟩ ≤ 0 for every y ∈ C: every legal point makes an obtuse angle with the drop line.")

D[1302] = (lambda c: relabel(c, ("P(p)", "Π(x)"), ("P(q)", "Π(y)"), ("‖p−q‖", "‖x − y‖"), ("‖P(p)−P(q)‖ ≤ ‖p−q‖", "‖Π(x) − Π(y)‖ ≤ ‖x − y‖")),
    "Projecting two points never pulls them apart: ‖Π(x) − Π(y)‖ ≤ ‖x − y‖. Firm non-expansiveness is stronger: the squared shadow distance plus the squared distance of the dropped-off parts is at most ‖x − y‖².")

D[1303] = (lambda c: relabel(c, ("P(p)", "x − (aᵀx − b)a/‖a‖²"), ("outside → dropped on the wall", "aᵀx > b: drop along a"),
                            ("already legal: stays", "aᵀx ≤ b: max(0, ·) = 0, stays")),
    "Onto the wall aᵀx = b: x − (aᵀx − b)a/‖a‖², a drop along the normal a. Onto the halfspace aᵀx ≤ b: the same drop with max(0, aᵀx − b), so a point already legal stays put.")

D[1307] = (lambda c: relabel(c, ("P", "Π(x)"), ("clamp each coordinate", "min(uᵢ, max(lᵢ, xᵢ))"), ("P", "Π(x)"), ("scale back to the radius", "x / max(1, ‖x‖/R)")),
    "Box: clamp each coordinate to its own limits, [Π(x)]ᵢ = min(uᵢ, max(lᵢ, xᵢ)). Ball of radius R: a point outside is scaled back to the rim, Π(x) = x / max(1, ‖x‖/R); a point inside stays.")

D[1304] = (lambda c: relabel(c, ("P_K(x)", "x₁ = Πᴋ(x)"), ("P_K°(x)", "x₂ = Πᴋ°(x)"), ("x = P_K(x) + P_K°(x),  ⟂", "x = x₁ + x₂,  ⟨x₁, x₂⟩ = 0")),
    "Moreau: any x splits into a part x₁ = Πᴋ(x) in the cone K and a part x₂ = Πᴋ°(x) in its polar cone, with x = x₁ + x₂ and ⟨x₁, x₂⟩ = 0.")

D[1305] = (lambda c: relabel(c, ("Dykstra: apex", "Dykstra: true Π"),
                            add=(N(120, 9, "yₖ = Π₁(xₖ + pₖ₋₁),  pₖ = xₖ + pₖ₋₁ − yₖ  (same for C₂ with q)", 6.8, "middle"),)),
    "Plain alternating projection lands on some point of C₁ ∩ C₂. Dykstra adds back the correction it removed last time, yₖ = Π₁(xₖ + pₖ₋₁) with pₖ = xₖ + pₖ₋₁ − yₖ (and the same with q for C₂), and so reaches the true projection onto C₁ ∩ C₂.")

D[1306] = (lambda c: relabel(c, ("above the level:", "τ = 1.5/2 = 0.75"), ("keep what sticks", "keep max(0, xᵢ − τ)"),
                            ("p = (.75,.25,0,0)", "p = (.75, .25, 0, 0)")),
    "Pour the tanks x into a budget Σ = 1: lower a common level τ until what sticks out above it sums to 1. Here τ = (2.5 − 1)/2 = 0.75, and p = max(0, x − τ1) = (0.75, 0.25, 0, 0).")

# ---------- topic 14: projected gradient ----------
D[1401] = (lambda c: relabel(c, ("xₖ − α∇f (inside the rock)", "xₖ − αₖ∇f(xₖ) (in the rock)"), ("xₖ₊₁ = P(·)", "xₖ₊₁ = Π(·)"),
                            ("xₖ₊₁ = P(xₖ − α∇f(xₖ))", "xₖ₊₁ = Π(xₖ − αₖ∇f(xₖ))")),
    "Fly a plain downhill hop xₖ − αₖ∇f(xₖ). If that lands inside the rock, drop back to the nearest legal point: xₖ₊₁ = Π(xₖ − αₖ∇f(xₖ)).")

D[1402] = (lambda c: relabel(c, ("P", "Π"), ("P(x* − α∇f(x*)) = x*", "Π(x* − α∇f) = x*"),
                            ("no net motion: a stationary spot", "−∇f ∈ N(x*): stays")),
    "At a stationary point the downhill hop goes straight into the rock and the projection brings it back to x* itself: Π(x* − α∇f(x*)) = x*, i.e. Gα(x*) = 0, i.e. −∇f(x*) lies in the normal cone N(x*).")

D[1403] = (lambda c: relabel(c, ("O(1/k) merely convex", "L‖x₀ − x*‖²/2k: convex"), ("ρᵏ strongly convex", "c·ρᵏ: strongly convex"), ("gap", "f(xₖ) − f*")),
    "Merely convex: the gap f(xₖ) − f* shrinks like L‖x₀ − x*‖²/2k, sublinear. Strongly convex: the distance shrinks like c·ρᵏ with ρ < 1, linear, which is a straight line on a log scale.")

D[1404] = (lambda c: relabel(c, ("trial points slide", "α = s, βs, β²s, … slide"), ("first big enough drop wins", "f(x(α)) ≤ f(xₖ) − (γ/α)‖xₖ − x(α)‖²")),
    "Try α = s, βs, β²s, …; each trial x(α) = Π(xₖ − α∇f) slides along the wall. Accept the first one whose drop is big enough: f(x(α)) ≤ f(xₖ) − (γ/α)‖xₖ − x(α)‖².")

D[1405] = (lambda c: relabel(c, ("y", "y = xₖ − αPₖ∇f"), ("curved surface", "h(x) = 0"),
                            ("tangent step leaves it; drop back along the radius", "restore: y − ∇h[∇hᵀ∇h]⁻¹h(y) lands back on h = 0")),
    "Fly a tangent step y = xₖ − αPₖ∇f(xₖ); on a curved surface h(x) = 0 it leaves the surface. The restoration step xₖ₊₁ = y − ∇h(xₖ)[∇h(xₖ)ᵀ∇h(xₖ)]⁻¹h(y) drops it back onto the surface.")

D[1406] = (lambda c: relabel(c, ("x − α∇f dips below ground", "(1,1) − (−1,5) = (2,−4)"), ("max(0, ·) clamps it back", "max(0, ·) = (2,0): fixed point")),
    "From x₀ = (1, 1) the gradient step lands at (2, −4), below the ground x₂ = 0; max(0, ·) clamps it back to (2, 0). The next step from (2, 0) is clamped back to (2, 0) again, so it is a fixed point.")

# ---------- topic 15: active set ----------
D[1501] = (lambda c: relabel(c, ("A_W p = 0 : slide along the corridor only", "A𝒲p = 0: slide along the corridor only"), ("walls you touch act as rails", "[Q  A𝒲ᵀ; A𝒲  0][p; −λ] = [−∇f; 0]")),
    "Walls in the working set 𝒲ₖ act as rails: the step must keep A_𝒲 p = 0. Solving the KKT system [Q A_𝒲ᵀ; A_𝒲 0][p; −λ] = [−∇f(xₖ); 0] gives the best step along the corridor and the walls' multipliers λ.")

D[1502] = (lambda c: relabel(c, ("stop: α < 1", "αₖ = (bᵢ − aᵢᵀxₖ)/(aᵢᵀpₖ) < 1"), ("intended x̂", "xₖ + pₖ (α = 1)"),
                            ("blocking wall joins", "𝒲ₖ₊₁ = 𝒲ₖ ∪ {i}"), ("the working set", "(blocking wall joins)")),
    "Head for xₖ + pₖ, but a wall i not in the working set is in the way. Stop where you hit it, αₖ = (bᵢ − aᵢᵀxₖ)/(aᵢᵀpₖ) < 1, and add it: 𝒲ₖ₊₁ = 𝒲ₖ ∪ {i}.")

D[1503] = (lambda c: relabel(c, ("μ < 0 : the wall", "λⱼ < 0: the wall"), ("take off ↗", "𝒲ₖ₊₁ = 𝒲ₖ ∖ {j} ↗")),
    "With pₖ = 0 you are stuck on the current walls. If some multiplier λⱼ < 0, that wall would have to pull you back, so gravity points away from it: drop it, 𝒲ₖ₊₁ = 𝒲ₖ ∖ {j}, and take off.")

D[1504] = (lambda c: relabel(c, ("altitude strictly falls:", "Q ≻ 0, αₖ > 0 ⇒"), ("no working set repeats", "no 𝒲 repeats ⇒ ≤ 2ᵐ steps")),
    "With Q ≻ 0 and every step αₖ > 0, the altitude strictly falls, f₀ > f₁ > f₂ > …. A working set can never come back, and there are at most 2ᵐ of them, so the method stops in finitely many steps.")

D[1505] = (lambda c: relabel(c, ("three walls meet at one point", "extra wall with bᵢ − aᵢᵀxₖ = 0"), ("α = 0 : tower swaps walls, plane idles", "αₖ = 0: xₖ₊₁ = xₖ, only 𝒲 changes")),
    "Degeneracy: an extra wall already passes through xₖ, bᵢ − aᵢᵀxₖ = 0, so the blocking step is αₖ = 0. The plane does not move (xₖ₊₁ = xₖ, f unchanged); only the working set changes, and an anti-cycling rule is needed.")

D[1506] = (lambda c: relabel(c, ("slide, block,", "drop x₁=0, slide;"), ("drop, slide", "drop x₂=0: λ*=(2,2)")),
    "From x₀ = (0, 0): drop the wall x₁ = 0 and slide to x₁ = (2, 0); drop the wall x₂ = 0 and slide to x* = (2, 2). There both multipliers are positive, λ* = (2, 2), so it is optimal.")

# ---------- topic 16: duality ----------
D[1601] = (lambda c: relabel(c, ("ω(z) = lowest altitude", "ω(z) = inf{f(x) : g(x) ≤ z}"), ("ruler height at z=0 = dual value q(μ)", "ruler at z = 0: φ(μ) = inf ω(z) + μᵀz")),
    "ω(z) = inf{f(x) : g(x) ≤ z} is the lowest altitude if the wall is moved by z. Lay a ruler with slope −μ under it; its height at z = 0 is φ(μ) = inf over z of ω(z) + μᵀz, the dual value.")

D[1602] = (lambda c: relabel(c, ("q(μ) ≤ p*", "d* = sup q(λ, μ) ≤ p*"), ("gap", "gap p* − d* ≥ 0")),
    "Every dual value q(λ, μ) with μ ≥ 0 is a floor under the true optimum p*. Raising the floor as high as possible gives d* = sup q ≤ p*, so the duality gap p* − d* ≥ 0 always.")

D[1603] = (lambda c: relabel(c, ("convex + Slater", "convex + Slater ⇒ p* = d*"), ("bump in ω(z)", "non-convex ω: gap")),
    "If the problem is convex and Slater holds, ω(z) is a convex bowl and a ruler touches it at z = 0: p* = d*. A bump in a non-convex ω(z) can hide the true optimum from every ruler, leaving a gap.")

D[1604] = (lambda c: relabel(c, ("each plan x gives a straight line in μ", "each x: line f(x) + μᵀg(x) in μ"), ("lowest of all lines = concave q(μ)", "q(μ) = min over x: concave")),
    "For each fixed plan x, f(x) + μᵀg(x) is a straight line in μ. The dual function q(μ) is the lowest of all these lines, so it is concave: q(αy₁ + (1−α)y₂) ≥ αq(y₁) + (1−α)q(y₂), whether or not the problem is convex.")

D[1605] = (lambda c: relabel(c, ("ω drops by μ*", "p*(z) drops by μ*·Δz"), ("multiplier = shadow price", "∇p*(0) = −μ*: shadow price")),
    "Move the wall out by Δz = 1 and the best altitude drops by about μ*: p*(z) ≥ p*(0) − μ*ᵀz, and ∇p*(0) = −μ*. The multiplier is the price of loosening that wall.")

D[1606] = (lambda c: relabel(c, ("eastbound", "yᵢ = +1: wᵀx + b ≥ 1"), ("westbound", "yᵢ = −1: wᵀx + b ≤ −1")),
    "Two traffic streams: eastbound yᵢ = +1 must satisfy wᵀxᵢ + b ≥ 1 and westbound yᵢ = −1 must satisfy wᵀxᵢ + b ≤ −1. The gap between the two lanes is 2/‖w‖, so maximising it means minimising ½‖w‖².")

D[1608] = (lambda c: relabel(c, ("only planes on the edges carry weight", "w* = Σαᵢyᵢxᵢ: only αᵢ > 0 (edges) count")),
    "In the dual each plane gets a weight αᵢ ≥ 0. Only the planes on the lane edges get αᵢ > 0 (support vectors); all others have αᵢ = 0. The wall is w* = Σαᵢyᵢxᵢ, built from the support vectors alone.")

# ---------- topic 17: Wolfe dual ----------
D[1701] = (lambda c: relabel(c, ("∇ₓL = 0 : forces balance", "∇f + ∇hλ + ∇gμ = 0: balance"), ("maximise L over μ ≥ 0", "max f + λᵀh + μᵀg, μ ≥ 0")),
    "The Wolfe dual only considers equilibrium states, where gravity and the wall pushes balance: ∇f(x) + ∇h(x)λ + ∇g(x)μ = 0. Among them, with μ ≥ 0, it maximises the Lagrangian f(x) + λᵀh(x) + μᵀg(x).")

D[1702] = (lambda c: relabel(c, ("primal: ↓", "primal: min f ↓"), ("dual: ↑", "Wolfe: max L ↑"), ("p* = q*", "max L = f(x*) = min f")),
    "For a convex problem (f, gⱼ convex, hᵢ affine), the primal coming down and the Wolfe dual coming up meet: max L over the Wolfe set equals f(x*) = min f over Ω.")

D[1703] = (lambda c: relabel(c, ("min ½xᵀQx", "min ½xᵀQx + cᵀx"), ("max −½yᵀQy+bᵀy", "max −½xᵀQx + bᵀy"),
                            ("same risk, opposite sign: totals meet", "Qx − Aᵀy + c ≥ 0, y ≥ 0: totals meet")),
    "For the quadratic program min ½xᵀQx + cᵀx s.t. Ax ≥ b, x ≥ 0, the dual is max −½xᵀQx + bᵀy s.t. Qx − Aᵀy + c ≥ 0, y ≥ 0. The same quadratic term appears with the opposite sign, and the two optimal values meet.")

D[1704] = (lambda c: relabel(c, ("x*", "x = 0"), ("true lowest point", "min −x² = −∞"), ("false floor", "f′(0) = 0: f(0) = 0")),
    "For f(x) = −x², the only point with f′(x) = 0 is the peak x = 0, so the Wolfe dual reports 0. But the true minimum is −∞. Without convexity, d* > p* and the Wolfe dual fails.")

D[1705] = (lambda c: relabel(c, ("g > 0 (hitting the wall):", "g(x(μₖ)) > 0:"), ("raise the price μ", "μₖ₊₁ = μₖ + αₖg ↑"), ("g < 0 (slack): lower it", "g < 0: lower, floor at 0")),
    "For the current price μₖ, solve x(μₖ) = argmin L(x, μₖ). If it breaks the wall (g > 0), raise the price; if there is slack (g < 0), lower it, never below zero: μₖ₊₁ = max(0, μₖ + αₖg(x(μₖ))).")

D[1706] = (lambda c: relabel(c, ("pᵢ ∝ e^(−βEᵢ)", "pᵢ = exp(aᵢᵀλ − 1)"), ("(Boltzmann)", "q(λ) = bᵀλ − Σ pᵢ")),
    "Maximising entropy subject to Ap = b gives probabilities pᵢ = exp(aᵢᵀλ − 1). Plugging them in gives the dual q(λ) = bᵀλ − Σᵢ exp(aᵢᵀλ − 1), a smooth concave function with no constraints left.")

# ---------- topic 18: LP ----------
D[1801] = (lambda c: relabel(c, ("cost ≥ revenue, equal at optimum", "cᵀx ≥ bᵀy, equal at optimum")),
    "Primal: the airline picks flights x ≥ 0 with Ax = b and minimises cost cᵀx. Dual: the airport sets prices y with Aᵀy ≤ c and maximises revenue bᵀy. Always cᵀx ≥ bᵀy, with equality at the optimum.")

D[1807] = (lambda c: relabel(c, ("pinned: 2 walls meet", "xɴ = 0, xʙ = B⁻¹b ≥ 0"), ("corners = basic feasible solutions", "vertices = basic feasible solutions")),
    "Pick m columns forming an invertible B, set the rest to zero (x_N = 0) and solve x_B = B⁻¹b. If x_B ≥ 0 this point is a corner of {Ax = b, x ≥ 0}, and every corner arises this way.")

D[1802] = (lambda c: relabel(c, ("sheet tilts this way", "altitude cᵀx tilts this way"), ("lowest corner", "x* = [B⁻¹b; 0]"),
                            ("linear altitude over a polygon: lowest point is a corner", "linear cᵀx over 𝒫 = {Ax = b, x ≥ 0}: min at a vertex")),
    "The altitude cᵀx is a tilted flat sheet over the polygon 𝒫 = {Ax = b, x ≥ 0}, so its lowest point is at a corner, a basic feasible solution x = [B⁻¹b; 0].")

D[1803] = (lambda c: relabel(c, ("x_j > 0", "xⱼ > 0"), ("fee = cost", "Aⱼᵀy = cⱼ"), ("fee < cost", "Aⱼᵀy < cⱼ"), ("x_j = 0", "xⱼ = 0"), ("y_i = 0", "yᵢ = 0"),
                            ("x_j (c_j − A_jᵀy) = 0  and  y_i (A_i x − b_i) = 0", "xⱼ(cⱼ − Aⱼᵀy) = 0  and  yᵢ(Aᵢx − bᵢ) = 0")),
    "At the optimum, a flight that is used (xⱼ > 0) has its fee exactly equal to its cost, Aⱼᵀy = cⱼ; a flight whose fee is below cost is not used, xⱼ = 0. Likewise a wall that is not touched has price yᵢ = 0.")

D[1804] = (lambda c: relabel(c, ("b outside the cone", "Aᵀy ≥ 0, bᵀy < 0"), ("unbounded ↑", "bᵀ(y₀ + td) → +∞")),
    "If no legal plan exists, b is outside the cone of A's columns and Farkas gives a direction with Aᵀy ≥ 0, bᵀy < 0. Flip its sign to get d; adding td to any dual-feasible y₀ keeps it feasible while bᵀ(y₀ + td) → +∞.")

D[1805] = (lambda c: relabel(c, ("hop to a lower neighbouring corner until none is lower", "stop when cɴᵀ − cʙᵀB⁻¹N ≥ 0")),
    "The simplex method hops from corner to a cheaper neighbouring corner (9 → 7 → 4 → 1). It stops when every reduced cost c_Nᵀ − c_BᵀB⁻¹N is ≥ 0, meaning no neighbour is cheaper.")

D[1808] = (lambda c: relabel(c, ("optimum", "x* (μ → 0)"), add=(N(120, 11, "x(μ) = argmin cᵀx − μΣ ln xⱼ  →  x* as μ → 0", 7.2, "middle"),)),
    "Interior-point methods add a log barrier −μΣ ln xⱼ that keeps the plane off the walls. The minimisers x(μ) trace the central path, which reaches the optimum x* as μ → 0. The simplex method walks the edges instead (dashed).")

D[1806] = (lambda c: relabel(c, ("cockpit and tower agree", "z* = 3·2 + 2·3 = 12 = 5·1 + 7·1 = w*")),
    "Primal optimum at (2, 3) gives z* = 3·2 + 2·3 = 12; dual optimum at (1, 1) gives w* = 5·1 + 7·1 = 12. The two values agree, and complementary slackness holds at both points.")

# ---------- topic 19: penalty and barrier ----------
D[1901] = (lambda c: relabel(c, ("fine c·(violation)²: bigger c, stops closer to the wall", "q = f + (c/2)·max(0, g)²: c → ∞ ⇒ x*")),
    "Replace the wall by a fine (c/2)·max(0, g(x))² that grows with the violation: q(c, x) = f(x) + (c/2)Σ hᵢ² + (c/2)Σ max(0, gⱼ)². The bigger c, the closer the plane stops to the wall; as c → ∞ it reaches x*.")

D[1902] = (lambda c: relabel(c, ("barrier −μ·log(distance to wall) blows up at the wall", "B(x) = −Σ ln(−gⱼ(x)) → +∞ at the wall"),
                            ("the plane never touches the wall; as μ → 0 it creeps closer", "x(c) = argmin f + B/c: c ↑ ⇒ creeps closer"),
                            ("μ big", "1/c big"), ("μ medium", "1/c medium"), ("μ small", "1/c small")),
    "The barrier B(x) = −Σ ln(−gⱼ(x)) blows up at the wall, so the plane never touches it. Minimising f + B/c with larger and larger c lets it creep closer: x(c) → x*.")

D[1903] = (lambda c: relabel(c, ("gentle curvature", "λmin: gentle"), ("across the wall: ~c", "λmax ~ c across the wall"),
                            ("κ grows like c: huge fine = huge condition number", "κ = λmax/λmin ≈ O(c) → ∞")),
    "Along the wall the penalised valley curves gently (λmin), but across it the curvature grows like c (λmax). So κ = λmax/λmin ≈ O(c) → ∞: a razor canyon where gradient methods zig-zag.")

D[1904] = (lambda c: relabel(c, ("λ ≈ c·h", "λ⁽ᵏ⁾ = cₖh → λ*"), ("sinks a little: h(x)", "misses by h ≈ λ*/cₖ")),
    "The penalised plane always sinks a little past the boundary, by h(x(cₖ)). That small miss times the fine is the multiplier estimate: λ⁽ᵏ⁾ = cₖh(x(cₖ)) → λ* (and μ⁽ᵏ⁾ = cₖ max(0, g) → μ*).")

D[1905] = (lambda c: relabel(c, ("augmented: adjust λ and land exactly", "augmented: λₖ₊₁ = λₖ + cₖh(xₖ)"), ("with only a moderate fine c", "lands exactly with a moderate c")),
    "Pure penalty creeps toward the wall but never lands. The augmented Lagrangian also adjusts the multiplier after each solve, λₖ₊₁ = λₖ + cₖh(xₖ), and lands exactly on the wall with only a moderate fine c.")

D[1906] = (lambda c: relabel(c, ("λ*", "λ* = −2"), ("λ₀", "λ₀ = 0"), ("λ₁", "−4/3"), ("λ₂", "−16/9")),
    "λ₀ = 0 gives x⁽⁰⁾ = (2/3, 2/3); λ₁ = −4/3 gives (8/9, 8/9); λ₂ = −16/9 gives (26/27, 26/27). Each update λₖ₊₁ = λₖ + c·h(xₖ) closes the gap, and λₖ → λ* = −2 while x → (1, 1).")

FIX = {cid: {"drawingSvg": fn(cid), "drawingCaption": cap, "textbookImg": None, "textbookRef": None} for cid, (fn, cap) in D.items()}
