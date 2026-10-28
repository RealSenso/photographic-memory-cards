"""Topic 09: the airplane-and-mountains analogy as the CONNECTION, and our own drawn diagrams (no textbook figures)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from subj_lib import T, N, L, P, C, R, PG, svg

def hatch(x1, y1, x2, y2, dx, dy, n):
    """short outward ticks along the edge (x1,y1)->(x2,y2), pointing (dx,dy): the 'mountain' side"""
    out = []
    for i in range(n):
        t = (i + .5) / n
        x, y = x1 + (x2 - x1) * t, y1 + (y2 - y1) * t
        out.append(L(round(x, 1), round(y, 1), round(x + dx, 1), round(y + dy, 1), 1.1))
    return "".join(out)

def d901(cid):
    poly = "54,36 190,24 214,92 150,126 70,122 40,80"
    return svg(cid,
        PG(poly, "#f1f5f9", 2.4),
        hatch(40, 80, 54, 36, -7, -2, 4), hatch(54, 36, 190, 24, -1, -7, 8), hatch(190, 24, 214, 92, 6, -2, 5),
        T(125, 82, "Ω", 15),
        C(47, 58, 3.2), T(62, 62, "x*", 10, "start"),
        '<circle cx="47" cy="58" r="14" fill="none" stroke="#000000" stroke-width="1.2" stroke-dasharray="3 2.5"/>',
        N(2, 42, "g₁=0", 8, "start", "bold"), N(122, 14, "g₂=0", 8, "middle", "bold"), N(213, 44, "g₃=0", 8, "start", "bold"),
        N(120, 140, "only g₁ is touching x*; g₂, g₃ are far away", 8))

def d902(cid):
    pts = [(66, 88), (84, 79), (102, 74)]
    parts = [P("M30,115 Q120,30 210,115", "none", 2.2),
             L(95, 72.5, 215, 72.5, 1.1, d="4 3"),
             L(120, 72.5, 120, 28, 1.8, ar=True), T(128, 34, "∇h(x*)", 9, "start")]
    for (x, y), nm in zip(pts, ["x₁", "x₂", "x₃"]):
        parts += [L(x, y, 120, 72.5, 1, d="2 2.5"), C(x, y, 2.4), T(x - 2, y + 13, nm, 8.5)]
    parts += [C(120, 72.5, 3.4), T(113, 86, "x*", 10),
              L(120, 72.5, 182, 72.5, 3, ar=True), T(186, 66, "d", 11, "start", w="bold"),
              T(214, 80, "M", 9), N(38, 128, "t_k ↓ 0", 8.5), N(206, 128, "h(x)=0", 8.5),
              T(120, 140, "d = lim (x_k − x*) / t_k", 9)]
    return svg(cid, *parts)

def d903(cid):
    om = "45,72 85,40 110,50 140,26 160,40 200,24 215,70 190,110 150,96 120,128 85,104"
    parts = [PG(om, "#f1f5f9", 1.8)]
    for k, (ex, ey) in enumerate([(125, 8), (125, 22), (125, 47), (125, 72), (125, 97), (125, 122), (125, 136)]):
        edge = k in (0, 6)
        parts.append(L(45, 72, ex, ey, 1.5 if edge else 1, d=None if edge else "3 3"))
    parts += [L(45, 72, 112, 72, 2.8, ar=True), T(98, 66, "d", 10, w="bold"),
              L(114, 72, 205, 72, 1.4, d="5 3", ar=True), T(166, 65, "λd", 10),
              C(45, 72, 3.4), T(33, 90, "x*", 10), T(6, 133, "T_Ω(x*)", 9.5, "start")]
    return svg(cid, *parts)

def d905(cid):
    parts = []
    for r in (55, 85, 120):
        parts.append(f'<circle cx="10" cy="73" r="{r}" fill="none" stroke="#000000" stroke-width="1" stroke-dasharray="3 3"/>')
    parts.append(R(0, 0, 65, 145, "#d1d5db", 0))
    parts.append(L(65, 0, 65, 145, 2.6))
    parts.append(hatch(65, 0, 65, 145, -9, 6, 12))
    parts += [N(30, 14, "rock", 8), L(65, 73, 140, 73, 3.2, ar=True), T(142, 67, "∇f", 11, "start"),
              L(62, 73, 24, 73, 1.6, d="4 3", ar=True), T(44, 90, "−∇f", 9),
              C(65, 73, 3.6), T(74, 90, "x*", 10, "start")]
    for ex, ey in [(105, 42), (110, 104), (65, 32), (65, 114), (100, 73)]:
        pass
    for ex, ey in [(105, 42), (110, 104), (65, 30), (65, 116)]:
        parts.append(L(65, 73, ex, ey, 1.3, ar=True))
    parts += [T(108, 38, "d", 9.5, "start"), N(168, 112, "∇f·d ≥ 0", 8.5), N(168, 126, "for every legal d", 8)]
    return svg(cid, *parts)

def d906(cid):
    ox, oy = 80, 90
    top = [(ox + 10 * i, round(oy - 70 * ((10 * i) / 110) ** 3, 1)) for i in range(0, 12)]
    poly = " ".join(f"{x},{y}" for x, y in top) + f" {ox + 110},{oy}"
    parts = [R(12, 62, ox - 12, 54, "#d1d5db", 1.2), hatch(ox, 62, ox, 116, -6, 5, 8),
             N(46, 112, "rock", 8), PG(poly, "#f1f5f9", 1.8),
             L(14, oy, 218, oy, 1.1, d="5 3", ar=True), L(ox, oy, 214, oy, 3.2, ar=True),
             C(ox, oy, 3.4), T(ox + 5, oy + 15, "x*=0", 9, "start"),
             N(96, 16, "g₁: x₂ ≤ x₁³", 8, "start"), N(96, 28, "g₂: −x₂ ≤ 0", 8, "start"),
             N(150, 118, "T = just this ray →", 8, "start", "bold"), N(98, 132, "L = the whole x₁-axis, also ← into the rock", 8, "start"),
             T(34, 84, "L says ok", 8.5)]
    return svg(cid, *parts)

COMMON = {"textbookImg": "", "textbookRef": ""}

FIX = {
    901: dict(COMMON,
        coreTranslation=[
            "The <strong>Feasible Set $\\Omega$</strong> is your legal playground where $h_i(x)=0$ and $g_j(x)\\le 0$ hold simultaneously.",
            "The <strong>Active Set $\\mathcal{A}(x)=\\{j: g_j(x)=0\\}$</strong> identifies boundary walls you are physically pressing against right now.",
            "<strong>Inactive constraints ($g_j(x)<0$):</strong> candidate $x^*$ touches $g_1(x)=0$, while $g_2(x)=0$ and $g_3(x)=0$ are far away! In a local ball around $x^*$, they remain strictly $<0$ and have zero local influence."],
        drawingSvg=d901(901),
        drawingCaption="A top-down view of an airplane parked against one mountain wall (g₁). The other walls are far across the valley. The open tarmac is Ω; the dashed circle is the local ball around x*.",
        personalConnection="<strong>The airplane analogy.</strong> The Feasible Set (Ω) is the legal airspace and runway tarmac where you are permitted to fly and taxi. The Active Set names the mountain walls your plane is physically parked against right now. The mountains on the other side of the valley (inactive constraints) have zero effect on your immediate next move."),
    902: dict(COMMON,
        coreTranslation=[
            "<strong>Curve definition (Luenberger, p. 323):</strong> a curve on the surface $S$ is parameterized as $x(t)\\in S$. Its derivative at $x^*$ is the velocity $\\dot x(t^*)$, and the tangent plane is the collection of all such derivatives!",
            "<strong>Discrete sequence version:</strong> $d=\\lim_{k\\to\\infty}\\dfrac{x_k-x^*}{t_k}$ with $x_k\\in\\Omega$ and $t_k\\downarrow 0$.",
            "<strong>Tangent plane:</strong> the plane $M=\\{y:\\nabla h(x^*)^\\top y=0\\}$ is strictly orthogonal to the normal gradient $\\nabla h(x^*)$."],
        drawingSvg=d902(902),
        drawingCaption="A time-lapse dotted line tracking an airplane coming down onto the tarmac. At the touchdown point x* a single bold arrow d shoots forward along the tarmac: that is the velocity.",
        personalConnection="<strong>The airplane analogy.</strong> Think of $x_k$ as your GPS coordinates ticking down every millisecond ($t_k\\downarrow 0$) during your final descent through legal airspace. The tangent vector $d$ is your exact, instantaneous velocity at the precise moment your tires touch the tarmac at $x^*$. The crucial requirement: the whole approach path stayed inside legal airspace ($\\Omega$)."),
    903: dict(COMMON,
        coreTranslation=[
            "The <strong>Tangent Cone $T_\\Omega(x)$</strong> is the set of all tangent vectors to $\\Omega$ at the point $x$.",
            "<strong>Cone property:</strong> if $d\\in T_\\Omega(x)$, then $\\lambda d\\in T_\\Omega(x)$ for all $\\lambda\\ge0$. You can stretch the arrow as long as you want.",
            "It is <strong>always a closed set</strong>, even if the underlying feasible set $\\Omega$ is non-convex or has sharp jagged edges."],
        drawingSvg=d903(903),
        drawingCaption="Radiating out from the nose of the parked plane is a pie-shaped wedge (the cone), drawn with several dashed runway lines: the whole fan of safe departure headings.",
        personalConnection="<strong>The airplane analogy.</strong> This is the complete catalog of every legal runway heading available to you from your parked position. Cone property: if a heading $d$ is safe, you can throttle forward along it as far as you want ($\\lambda d$) without immediately hitting the mountain."),
    905: dict(COMMON,
        drawingSvg=d905(905),
        drawingCaption="The bold arrow (gravity, −∇f is the dashed one) points straight into the rock. Every open runway d points away from the wall or along it. The plane is trapped at the lowest point.",
        personalConnection="<strong>The airplane analogy.</strong> Your objective $f$ is altitude: you want to park at the lowest elevation possible, and the negative gradient $-\\nabla f$ (gravity) points exactly downhill. At the minimum, gravity must pull the plane straight into the solid mountain wall. $\\nabla f(x^*)^\\top d\\ge0$ is the pre-flight check proving that every legal runway $d$ goes flat or uphill. If one sloped downhill, you could just release the brakes!"),
    906: dict(COMMON,
        coreTranslation=[
            "The <strong>Linearized Cone $L_\\Omega(x)$</strong> is defined by the active constraint gradients: $L_\\Omega=\\{d:\\nabla h_i^\\top d=0,\\ \\nabla g_j^\\top d\\le0\\}$. In general $T_\\Omega\\subseteq L_\\Omega$.",
            "<strong>Constraint Qualification (CQ):</strong> a condition guaranteeing $T_\\Omega(x^*)=L_\\Omega(x^*)$. The gold standard is <strong>LICQ</strong>: the active gradients $\\{\\nabla h_i,\\nabla g_j\\}_{j\\in\\mathcal A}$ are linearly independent.",
            "Without CQ, $T_\\Omega\\subsetneq L_\\Omega$, and the KKT conditions can FAIL completely even at an obvious local minimum!"],
        drawingSvg=d906(906),
        drawingCaption="A thin horn of tarmac pinches to a point at x* (g₁: x₂ ≤ x₁³, g₂: x₂ ≥ 0). The Nav Computer draws a straight safe line through the whole x₁-axis, including the stretch that runs into the rock.",
        personalConnection="<strong>The airplane analogy.</strong> $L_\\Omega$ is your Nav Computer's map: it guesses the safe airspace with perfectly straight lines based only on the slope where your wheels touch. LICQ is the safety check. If the wall curves sharply inwards (a cusp), the straight-line map over-approximates the safe zone, and if you follow the computer you smash into solid rock."),
}
DELETE = [904]
