"""Redrawn diagrams that explain the idea better (later layer: overrides earlier drawings)."""
from air_lib import *

# ---------- 1104: LICQ. Can the wall pushes balance the downhill pull? ----------
def d1104(c):
    p = []
    # left: two straight walls meeting at a corner (x >= 0, y >= 0), pull -grad f = (-1,-1)
    O = (52, 88)
    p.append('<rect x="52" y="20" width="62" height="68" fill="#e5e7eb"/>')
    p.append(wall(52, 88, 114, 88, 0, 1, n=6, w=1.2) + wall(52, 88, 52, 20, -1, 0, n=6, w=1.2))
    p.append(plane(86, 52, -45, 0.8))
    p.append(L(28, 88, 28, 112, 1.0, d="3 2") + L(52, 112, 28, 112, 1.0, d="3 2"))
    p.append(arrow(52, 88, 52, 112, 1.2) + it(56, 114, "∇g₁", 9, "start"))
    p.append(arrow(52, 88, 28, 88, 1.2) + it(24, 82, "∇g₂", 9, "middle"))
    p.append(arrow(52, 88, 29, 111, 1.2) + it(25, 122, "−∇f", 9, "end"))
    p.append(dot(52, 88, r=2.6))
    p.append(N(60, 12, "independent normals", 8))
    p.append(N(60, 130, "rank 2: any pull is a mix", 7.5))
    p.append(N(60, 141, "−∇f = ∇g₁ + ∇g₂ ✓", 7.5))
    p.append(L(120, 6, 120, 140, 1.0, d="3 3"))
    # right: min x1 s.t. x2 <= x1^3, x2 >= 0. A cusp at the origin, both normals vertical, pull (-1,0) sideways
    C0, W, H = (150, 88), 80, 70
    ys = lambda x: C0[1] - H * ((x - C0[0]) / W) ** 3
    pts = [(x, ys(x)) for x in range(150, 231, 4)]
    p.append('<polygon points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y in pts) + ' 230,88" fill="#e5e7eb"/>')
    p.append('<polyline points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y in pts) + '" fill="none" stroke="#000000" stroke-width="1.2"/>')
    p.append(wall(150, 88, 230, 88, 0, 1, n=7, w=1.2))
    p.append(plane(210, 79, 0, 0.5))
    p.append(arrow(150, 88, 150, 63, 1.2) + it(154, 66, "∇g₁", 9, "start"))
    p.append(arrow(150, 88, 150, 113, 1.2) + it(154, 113, "∇g₂", 9, "start"))
    p.append(arrow(150, 88, 127, 88, 1.2) + it(134, 80, "−∇f", 9, "middle"))
    p.append(N(138, 100, "✗", 9))
    p.append(dot(150, 88, r=2.6))
    p.append(N(180, 12, "parallel normals (a cusp)", 8))
    p.append(N(180, 130, "rank 1: pushes only go ↕", 7.5))
    p.append(N(180, 141, "sideways pull: no λ ✗", 7.5))
    return svg(c, *p)

# one text line made of parts: (text, 0) plain, (text, 1) subscript, (text, 2) italic
# (the unicode subscript letters render badly in Helvetica, so subscripts are real tspans)
def tx(x, y, parts, sz=8, a="middle"):
    def part(t, k):
        if k == 1: return f'<tspan baseline-shift="sub" font-size="{sz*0.72:.1f}">{t}</tspan>'
        if k == 2: return f'<tspan font-style="italic" font-family="serif" font-size="{sz*1.12:.1f}">{t}</tspan>'
        return t
    return f'<text x="{x}" y="{y}" font-size="{sz}" font-family="sans-serif" text-anchor="{a}" fill="#000000">' + "".join(part(t, k) for t, k in parts) + '</text>'

# ---------- 1103: KKT convex sufficiency, every term in the picture labelled ----------
def d1103(c):
    p = []
    yv = lambda x: 112 - 80 * ((x - 120) / 88) ** 2
    p.append('<rect x="32" y="26" width="176" height="86" fill="#f1f3f5"/>')
    p.append(tx(120, 37, [("Ω", 0), (": the legal region between the walls", 0)], 7))
    p.append(wall(32, 26, 32, 112, -1, 0, n=6, w=1.2) + wall(208, 26, 208, 112, 1, 0, n=6, w=1.2))
    p.append('<polyline points="' + " ".join(f"{x:.1f},{yv(x):.1f}" for x in range(32, 209, 4)) + '" fill="none" stroke="#000000" stroke-width="1.2"/>')
    p.append(tx(60, 52, [("f", 2), (": convex terrain", 0)], 7.5, "start"))
    p.append(plane(120, 94, 0, 1))
    p.append(L(66, 112, 174, 112, 1.2, d="4 3"))
    p.append(dot(120, 112, r=3))
    p.append(tx(114, 123, [("x*", 2), (": KKT point = global min", 0)], 7, "end"))
    p.append(tx(126, 123, [("dashed: tangent at x*, under ", 0), ("f", 2)], 6.3, "start"))
    p.append(tx(32, 13, [("g", 0), ("j", 1), (" ≤ 0", 0)], 8) + tx(32, 21, [("convex wall", 0)], 6))
    p.append(tx(208, 13, [("h", 0), ("i", 1), (" = 0", 0)], 8) + tx(208, 21, [("flat wall", 0)], 6))
    p.append(tx(120, 15, [("f", 2), (", g", 0), ("j", 1), (" convex,  h", 0), ("i", 1), (" affine", 0)], 8.5))
    p.append(tx(120, 140, [("KKT ⇒ ", 0), ("f", 2), ("(x*) ≤ ", 0), ("f", 2), ("(x) for all x ∈ Ω", 0)], 8))
    return svg(c, *p)

FIX = {
    1103: {
        "drawingSvg": d1103("1103"),
        "drawingCaption": "Every term in the picture: <i>f</i> is the convex terrain (the valley), the walls are the constraints g<sub>j</sub> ≤ 0 (convex) and h<sub>i</sub> = 0 (affine, so flat), and Ω is the legal region between them. x* is a KKT point; the dashed tangent at x* lies under <i>f</i> everywhere, so f(x*) ≤ f(x) for every x in Ω: the KKT point is the global minimum.",
    },
    1104: {
        "drawingSvg": d1104("1104"),
        "drawingCaption": "KKT asks the wall pushes to cancel the downhill pull: −∇f = Σ λⱼ∇gⱼ. Left: walls x ≥ 0 and y ≥ 0 meet at a corner, the two normals point different ways (rank 2), so any pull is a mix of them; for −∇f = (−1,−1) the multipliers are λ = (1,1). Right: min x₁ subject to x₂ ≤ x₁³, x₂ ≥ 0. The minimum is the cusp at the origin, but there ∇g₁ = (0,1) and ∇g₂ = (0,−1) lie on one line (rank 1). The pull −∇f = (−1,0) is sideways and vertical pushes can never cancel it, so no multipliers exist and KKT fails at a true minimum.",
    },
}
