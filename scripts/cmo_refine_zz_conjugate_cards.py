"""Topic 07 cards 01-02 rewritten with the crosswind / flight-plane analogy and notebook-friendly diagrams."""
from air_lib import *
from subj_lib import poly
from cmo_refine_airplane_draw_d import quad_contours, sd_path, cg_path, S

Q7 = [[4, 3], [3, 4]]
X0 = [-2.4, 0.7]

CX, CY, SC, HS = 122, 100, 17.0, 5.2
def fq(x): return 0.5 * (x[0] * (Q7[0][0] * x[0] + Q7[0][1] * x[1]) + x[1] * (Q7[1][0] * x[0] + Q7[1][1] * x[1]))
from dip_lib import E

def wy(x, c=120, bottom=106, depth=70, half=86):
    return bottom - depth * ((x - c) / half) ** 2

def bowl_parts():
    """a hand-drawable bowl: rim ellipse, U-shaped walls, two rings on the surface"""
    out = [E(120, 36, 86, 13, 0, "none", 2.2)]
    xs = [34 + 172 * i / 40 for i in range(41)]
    out.append(poly([(x, wy(x)) for x in xs], 1.9))
    for r in (0.5, 0.18):
        out.append(E(120, 106 - 70 * r, 86 * r ** .5, 13 * r ** .5, 0, "none", 1.0))
    return out

X0P, X1P, XSP = (48, wy(48)), (100, wy(100)), (126, 106.5)

def d701(c):
    W = lambda x: (x, wy(x))
    parts = bowl_parts() + [
        poly([X0P, W(150), W(66), W(134), W(96), XSP], 1.5, "3 3"),
        poly([X0P, (74, (wy(48) + wy(100)) / 2 + 9), X1P], 2.8), poly([X1P, (113, 106.2), XSP], 2.8),
        dot(*X0P, "x₀", -6, -3, 10, "end", 3), dot(*X1P, "x₁", -5, 14, 10, "end", 3), dot(*XSP, "x*", 8, 13, 10, "start", 3.4),
        it(66, 92, "d₀", 10, "end"), it(116, 124, "d₁", 10, "middle"),
        N(6, 9, "dashed: ⊥ legs zig-zag", 8, "start"), N(6, 19, "across the valley", 8, "start"),
        N(120, 140, "solid: Q-conjugate d₀ᵀQd₁ = 0, two legs", 8.5, "middle", "bold")]
    return svg(c, *parts)

def d702(c):
    sheet = poly([(26, 28), (180, 28), (180, 116), (26, 116), (26, 28)], 1.3, "5 3")
    pf = lambda x: 106 - 60 * ((x - 100) / 74) ** 2
    prof = [(x, pf(x)) for x in [26 + 154 * i / 50 for i in range(51)]]
    x0 = (50, pf(50))
    parts = [sheet] + bowl_parts() + [poly(prof, 2.6), poly([(100, 106), (113, 106.4), XSP], 2.6),
        dot(*x0, "x₀", -6, -3, 10, "end", 3), dot(100, 106, "x₁", -5, 14, 10, "end", 3), dot(*XSP, "x₂", 8, 13, 10, "start", 3.4),
        N(236, 8, "plywood sheet = vertical slice along d₀", 8, "end"), N(236, 18, "x₁ = lowest point of the sheet", 8, "end"),
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
