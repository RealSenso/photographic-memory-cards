"""Tilted top view of a quadratic valley f = 1/2 x'Qx: rings of equal altitude, higher rings drawn higher up the page.
Paths are lifted onto the surface so legs, bends and zig-zags stay readable and easy to copy by hand."""
import math
from air_lib import *

class Bowl:
    def __init__(self, Q, cx=128, cy=90, sc=17.0, hs=3.0, tilt=0.8, levels=(9, 5, 2.2, 0.5), rot=-35):
        self.rot = math.radians(rot)
        self.Q, self.cx, self.cy, self.sc, self.hs, self.tilt, self.levels = Q, cx, cy, sc, hs, tilt, levels

    def f(self, x):
        Q = self.Q
        return 0.5 * (x[0] * (Q[0][0] * x[0] + Q[0][1] * x[1]) + x[1] * (Q[1][0] * x[0] + Q[1][1] * x[1]))

    def pr(self, x, f=None):
        f = self.f(x) if f is None else f
        c, s_ = math.cos(self.rot), math.sin(self.rot)
        u, v = x[0] * c - x[1] * s_, x[0] * s_ + x[1] * c
        return (self.cx + self.sc * u, self.cy - self.sc * self.tilt * v - self.hs * f)

    def ring(self, level, w=1.2):
        Q, pts = self.Q, []
        for i in range(73):
            th = math.radians(i * 5)
            u = (math.cos(th), math.sin(th))
            r = math.sqrt(2 * level / (u[0] * (Q[0][0] * u[0] + Q[0][1] * u[1]) + u[1] * (Q[1][0] * u[0] + Q[1][1] * u[1])))
            pts.append(self.pr((r * u[0], r * u[1])))
        return poly(pts, w)

    def rings(self):
        return [self.ring(l, 2.2 if i == 0 else 1.2) for i, l in enumerate(self.levels)]

    def seg(self, a, b, w=2.8, d=None, n=24):
        return poly([self.pr((a[0] + (b[0] - a[0]) * i / n, a[1] + (b[1] - a[1]) * i / n)) for i in range(n + 1)], w, d)

    def path(self, pts, w=2.8, d=None):
        return "".join(self.seg(a, b, w, d) for a, b in zip(pts, pts[1:]))

    def at(self, x):
        return self.pr(x)

def mv(Q, x): return [Q[0][0] * x[0] + Q[0][1] * x[1], Q[1][0] * x[0] + Q[1][1] * x[1]]
def dotp(u, v): return u[0] * v[0] + u[1] * v[1]

def sd_pts(Q, x0, n):
    x = x0[:]; pts = [x[:]]
    for _ in range(n):
        g = mv(Q, x); a = dotp(g, g) / dotp(g, mv(Q, g))
        x = [x[0] - a * g[0], x[1] - a * g[1]]; pts.append(x[:])
    return pts

def x0_on_level(Q, deg, level):
    t = math.radians(deg); v = [math.cos(t), math.sin(t)]
    f = 0.5 * dotp(v, mv(Q, v)); r = math.sqrt(level / f)
    return [r * v[0], r * v[1]]
