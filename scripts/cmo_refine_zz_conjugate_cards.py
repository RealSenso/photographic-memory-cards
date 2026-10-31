"""Topic 07 cards 01-02 rewritten with the crosswind / flight-plane analogy and notebook-friendly diagrams."""
from air_lib import *
from subj_lib import poly
from cmo_refine_airplane_draw_d import quad_contours, sd_path, cg_path, S

Q7 = [[4, 3], [3, 4]]
X0 = [-2.4, 0.7]

CX, CY, SC, HS = 122, 100, 17.0, 5.2
def fq(x): return 0.5 * (x[0] * (Q7[0][0] * x[0] + Q7[0][1] * x[1]) + x[1] * (Q7[1][0] * x[0] + Q7[1][1] * x[1]))
def pr(x, f=None):
    f = fq(x) if f is None else f
    return (CX + SC * 0.87 * (x[0] - x[1]), CY + SC * 0.35 * (x[0] + x[1]) - HS * f)

def bowl(fmax=12.0):
    """wire-frame of the valley surface f = 1/2 x'Qx, clipped at altitude fmax, plus its rim"""
    out = []
    n = 60
    for k in range(-4, 5, 2):
        v = k * 0.65
        for horiz in (True, False):
            run = []
            for i in range(n + 1):
                t = -3 + 6 * i / n
                x = (t, v) if horiz else (v, t)
                if fq(x) <= fmax: run.append(pr(x))
                elif len(run) > 1: out.append(poly(run, 0.9)); run = []
                else: run = []
            if len(run) > 1: out.append(poly(run, 0.9))
    import math
    rim = []
    for i in range(0, 73):
        th = math.radians(i * 5)
        u = (math.cos(th), math.sin(th)); r = math.sqrt(2 * fmax / (u[0] * (Q7[0][0] * u[0] + Q7[0][1] * u[1]) + u[1] * (Q7[1][0] * u[0] + Q7[1][1] * u[1])))
        rim.append(pr((r * u[0], r * u[1])))
    out.append(poly(rim, 2.0))
    return out

def lift(a, b, n=24):
    """the straight leg a->b in the floor plane, drawn as it sits on the valley surface"""
    return poly([pr((a[0] + (b[0] - a[0]) * i / n, a[1] + (b[1] - a[1]) * i / n)) for i in range(n + 1)], 2.8)

def d701(c):
    sdp = sd_path(Q7, X0, 6)
    cgp = cg_path(Q7, X0)
    cg = [pr(p) for p in cgp]
    parts = bowl() + [poly([q for a, b in zip(sdp, sdp[1:]) for q in [pr(a), pr(b)]], 1.5, "3 3"), lift(cgp[0], cgp[1]), lift(cgp[1], cgp[2]),
              dot(*cg[0], "x₀", -5, -4, 10, "end", 2.8), dot(*cg[1], "x₁", -7, 14, 10, "end", 2.8), dot(*cg[2], "x*", 6, 13, 10, "start", 3.2),
              N(6, 12, "dashed: ⊥ legs zig-zag", 8, "start"), N(6, 22, "up the valley wall", 8, "start"),
              N(120, 139, "solid: Q-conjugate d₀ᵀQd₁ = 0, two legs", 8.5, "middle", "bold")]
    return svg(c, *parts)

def d702(c):
    cg3 = cg_path(Q7, X0)
    x0, x1, x2 = cg3
    d0 = [x1[0] - x0[0], x1[1] - x0[1]]
    okt = [t / 100 for t in range(-400, 401) if fq((x0[0] + t / 100 * d0[0], x0[1] + t / 100 * d0[1])) <= 11.5]
    ts = [okt[0] + (okt[-1] - okt[0]) * i / 40 for i in range(41)]
    curve_pts = [pr((x0[0] + t * d0[0], x0[1] + t * d0[1])) for t in ts]
    ea, eb = (x0[0] + ts[0] * d0[0], x0[1] + ts[0] * d0[1]), (x0[0] + ts[-1] * d0[0], x0[1] + ts[-1] * d0[1])
    fa, fb = pr(ea, 0), pr(eb, 0)
    parts = bowl(12.0) + [L(fa[0], fa[1], fb[0], fb[1], 1.2, d="4 3"), poly(curve_pts, 1.4), lift(x0, x1), lift(x1, x2),
              dot(*pr(x0), "x₀", -5, -4, 10, "end", 2.6), dot(*pr(x1), "x₁", -7, 14, 10, "end", 2.6), dot(*pr(x2), "x₂", 6, 13, 10, "start", 3.2),
              N(6, 12, "plywood sheet along d₀:", 8, "start"), N(6, 22, "x₁ = its lowest point", 8, "start"),
              N(120, 139, "x₂ = lowest of the whole plane span{d₀,d₁}; g₂ ⊥ d₀, d₁", 8, "middle", "bold")]
    return svg(c, *parts)

FIX = {
701: {
 "textbookImg": None, "textbookRef": None,
 "drawingSvg": d701(701),
 "drawingCaption": "Dashed perpendicular legs zig-zag and undo each other; solid Q-conjugate legs cut straight to the centre along the valley's natural axes.",
 "hint": "Why are Q-conjugate headings better than plain perpendicular ones in a skewed valley with crosswinds?",
 "breakdown": [
  r"<strong>$d_i^\top Qd_j=0$ = a $Q$-twisted right angle.</strong> $Q$ is the valley's skewed curvature, the crosswinds. A plain right angle ignores them; a $Q$-conjugate angle accounts for them, so flying along $d_j$ never pushes you back up the hill you conquered along $d_i$.",
  r"<strong>$\alpha_k=-g_k^\top d_k/d_k^\top Qd_k$:</strong> the perfect flight distance. Downward momentum (numerator) divided by the brakes, the curvature along that heading (denominator), lands you at the bottom of that line.",
  r"<strong>$r_k=-g_k$ is the residual:</strong> the radar reading of your slope with the sign flipped to point downhill.",
 ],
 "personalConnection": r"<strong>The crosswind analogy.</strong> A steepest-descent pilot pushes the nose straight down, gets blown off course, turns 90 degrees and flies back into the same crosswind: a zig-zag. $Q$-conjugate headings follow the valley's natural aerodynamic axes, so pushing down along one heading never fights the crosswinds already conquered on the last.",
},
702: {
 "textbookImg": None, "textbookRef": None,
 "drawingSvg": d702(702),
 "drawingCaption": "The sheet of plywood: after two legs you sit at the lowest point of the whole plane x₀ + span{d₀,d₁}, not just the lowest point of the last line.",
 "hint": "After k sequential legs, where in the whole flight plane is the pilot sitting?",
 "breakdown": [
  r"<strong>$x_k=\arg\min f$ over the flight plane $x_0+\mathcal B_k$:</strong> step 1 is a tightrope, step 2 lays down a flat sheet of plywood holding both paths. You are not at the end of a line, you are at the lowest altitude of that whole sheet.",
  r"<strong>$g_k^\top d_i=0$ for every earlier heading:</strong> the proof of perfection. Your slope $g_k$ is flat (perpendicular) to every path you flew before, so going back along any of them would not improve your altitude.",
  r"<strong>Why it matters:</strong> you have squeezed all the juice out of those dimensions, so later conjugate legs never spoil the altitude already won.",
 ],
 "personalConnection": r"<strong>Securing the airspace.</strong> After $k$ maneuvers you have conquered $k$ dimensions of airspace: you sit at the lowest point of the entire flight plane spanned by your previous headings. Your new slope is flat relative to all of them, so later conjugate maneuvers never spoil the altitude you already won.",
},
}
