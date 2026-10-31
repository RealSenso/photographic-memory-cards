"""Topic 07 cards 01-02 rewritten with the crosswind / flight-plane analogy and notebook-friendly diagrams."""
from air_lib import *
from subj_lib import poly
from cmo_refine_airplane_draw_d import quad_contours, sd_path, cg_path, S

Q7 = [[2.5, 1.5], [1.5, 2.5]]
X0 = [-3.03, 1.1]

CX, CY, SC, HS = 122, 100, 17.0, 5.2
def fq(x): return 0.5 * (x[0] * (Q7[0][0] * x[0] + Q7[0][1] * x[1]) + x[1] * (Q7[1][0] * x[0] + Q7[1][1] * x[1]))
from dip_lib import E

import math
CX, CY, SC, HS = 128, 90, 17.0, 3.0
def fq(x): return 0.5 * (x[0] * (Q7[0][0] * x[0] + Q7[0][1] * x[1]) + x[1] * (Q7[1][0] * x[0] + Q7[1][1] * x[1]))
def pr(x, f=None):
    f = fq(x) if f is None else f
    return (CX + SC * x[0], CY - SC * 0.8 * x[1] - HS * f)

def ring(level, w=1.2):
    pts = []
    for i in range(73):
        th = math.radians(i * 5)
        u = (math.cos(th), math.sin(th))
        r = math.sqrt(2 * level / (u[0] * (Q7[0][0] * u[0] + Q7[0][1] * u[1]) + u[1] * (Q7[1][0] * u[0] + Q7[1][1] * u[1])))
        pts.append(pr((r * u[0], r * u[1])))
    return poly(pts, w)

def bowl():
    """the valley seen from above and a little to the side: rings of equal altitude, higher rings drawn higher up the page"""
    return [ring(9, 2.2), ring(5), ring(2.2), ring(0.5)]

def seg(a, b, w=2.8, d=None, n=24):
    return poly([pr((a[0] + (b[0] - a[0]) * i / n, a[1] + (b[1] - a[1]) * i / n)) for i in range(n + 1)], w, d)

def d701(c):
    x0, x1, xs = cg_path(Q7, X0)
    sdp = sd_path(Q7, X0, 5)
    parts = bowl() + [seg(a, b, 1.8, "3 3") for a, b in zip(sdp, sdp[1:])] + [seg(x0, x1), seg(x1, xs)]
    p0, p1, ps = pr(x0), pr(x1), pr(xs)
    parts += [dot(*p0, "x₀", -6, 3, 10, "end", 3), dot(*p1, "x₁", 7, -6, 10, "start", 3), dot(*ps, "x*", 9, 4, 10, "start", 3.4),
              it((p0[0] + p1[0]) / 2 - 5, (p0[1] + p1[1]) / 2 - 7, "d₀", 10, "end"), it((p1[0] + ps[0]) / 2 + 9, (p1[1] + ps[1]) / 2 + 3, "d₁", 10, "start"),
              N(120, 130, "dashed: ⊥ legs zig-zag across the valley", 8, "middle"),
              N(120, 140, "solid: Q-conjugate, d₀ᵀQd₁ = 0, two legs", 8.5, "middle", "bold")]
    return svg(c, *parts)

def d702(c):
    x0, x1, x2 = cg_path(Q7, X0)
    d = [x1[0] - x0[0], x1[1] - x0[1]]
    at = lambda t: (x0[0] + t * d[0], x0[1] + t * d[1])
    ts = [t / 50 for t in range(-250, 251) if fq(at(t / 50)) <= 9.0]
    ta, tb = ts[0], ts[-1]
    A, B, A0, B0 = pr(at(ta)), pr(at(tb)), pr(at(ta), 0), pr(at(tb), 0)
    prof = [pr(at(ta + (tb - ta) * i / 40)) for i in range(41)]
    parts = bowl() + [poly([A0, B0], 1.2, "5 3"), poly([A0, A], 1.2, "5 3"), poly([B0, B], 1.2, "5 3"), poly(prof, 1.6), seg(x0, x1, 3.0), seg(x1, x2, 3.0)]
    p0, p1, p2 = pr(x0), pr(x1), pr(x2)
    parts += [dot(*p0, "x₀", -6, 3, 10, "end", 3), dot(*p1, "x₁", 7, -6, 10, "start", 3), dot(*p2, "x₂", 9, 4, 10, "start", 3.4),
              N(120, 130, "dashed edges = plywood sheet along d₀; x₁ is its lowest point", 8, "middle"),
              N(120, 140, "x₂ = lowest of the whole plane span{d₀,d₁};  g₂ ⊥ d₀, d₁", 8, "middle", "bold")]
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
