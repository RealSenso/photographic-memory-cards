"""Airplane-scene helpers for the CMO Midterm 3 drawings (black and white, 240x145)."""
import math
from subj_lib import T, N, L, P, C, R, PG, svg, poly

def f(v): return f"{v:.1f}"

def plane(x, y, rot=0, s=1.0):
    """small top-down airplane, nose pointing +x before rotation (rot in degrees, y down)"""
    g = (f'<g transform="translate({f(x)} {f(y)}) rotate({rot}) scale({s})" fill="#ffffff" stroke="#000000" '
         f'stroke-width="{1.2/s:.2f}" stroke-linejoin="round">'
         '<polygon points="12,0 5,-2.2 -9,-1.6 -9,1.6 5,2.2"/>'
         '<polygon points="3,0 -4,-10 -7,-10 -3,0 -7,10 -4,10"/>'
         '<polygon points="-8,0 -11,-4.5 -12.5,-4.5 -10.5,0 -12.5,4.5 -11,4.5"/></g>')
    return g

def arrow(x1, y1, x2, y2, w=2.2, d=None):
    return L(f(x1), f(y1), f(x2), f(y2), w, d=d, ar=True)

def wall(x1, y1, x2, y2, nx, ny, n=8, tick=6, w=2.4):
    """a mountain wall: bold edge plus ticks pointing into the rock (direction nx,ny)"""
    out = [L(f(x1), f(y1), f(x2), f(y2), w)]
    for i in range(n):
        t = (i + .5) / n
        x, y = x1 + (x2 - x1) * t, y1 + (y2 - y1) * t
        out.append(L(f(x), f(y), f(x + nx * tick), f(y + ny * tick), 1.1))
    return "".join(out)

def dot(x, y, lab=None, dx=6, dy=-5, sz=9.5, a="start", r=3):
    s = C(f(x), f(y), r)
    if lab: s += T(round(x + dx,1), round(y + dy,1), lab, sz, a)
    return s

def dash(x1, y1, x2, y2, w=1.1, d="4 3"):
    return L(f(x1), f(y1), f(x2), f(y2), w, d=d)

def circ(cx, cy, r, fill="none", w=1.6, d=None):
    ds = f' stroke-dasharray="{d}"' if d else ""
    return f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r)}" fill="{fill}" stroke="#000000" stroke-width="{w}"{ds}/>'

def curve(pts, w=2, d=None, fill="none"):
    """smooth-ish polyline through (x,y) pts"""
    return poly(pts, w, d, fill)

def fn(fx, a, b, n=40, w=2, d=None):
    pts = [(a + (b - a) * i / n, fx(a + (b - a) * i / n)) for i in range(n + 1)]
    return poly(pts, w, d)

def label(x, y, s, sz=8.5, a="middle", bold=False):
    return N(round(x,1), round(y,1), s, sz, a, "bold" if bold else "normal")

def it(x, y, s, sz=9.5, a="middle"):
    return T(round(x,1), round(y,1), s, sz, a)

def sky(parts):  # nothing, placeholder for symmetry
    return "".join(parts)

def panel(x, y, w, h, fill="none", d=None):
    return R(x, y, w, h, fill, 1.1, 3, d)
