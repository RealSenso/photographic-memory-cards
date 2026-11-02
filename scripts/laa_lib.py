"""LAA drawing helpers. The everyday picture for all of LAA is a photo edited on your phone:
vectors are arrows pinned at the photo's centre (the origin), a linear map is an edit
(rotate, zoom, stretch, shear, flatten) applied to every arrow at once."""
from air_lib import arrow, dot, dash, circ, fn, f
from subj_lib import T, N, L, P, C, R, E, PG, svg, poly

def sheet(pts, fill="#f1f5f9", d=None):
    """flat polygon from a list of (x, y)"""
    return PG(" ".join(f"{x},{y}" for x, y in pts), fill, 1, d)

def phone(x, y, w, h, label=None):
    """the phone screen holding the photo, with its home bar"""
    out = R(x, y, w, h, "#ffffff", 1, 6) + L(x + w / 2 - 8, y + h - 4, x + w / 2 + 8, y + h - 4, 1)
    if label: out += N(x + w / 2, y - 3, label, 7, "middle")
    return out

def pin(x, y, lab="0", dx=-4, dy=11):
    """the pinch point at the photo's centre (the origin)"""
    return C(f(x), f(y), 2.4) + C(f(x), f(y), 4.5, "none", .8) + (N(x + dx, y + dy, lab, 7.5, "end") if lab else "")

def vec(o, p, lab=None, dx=4, dy=-3, a="start", sz=8, d=None):
    """an arrow pinned at o"""
    return arrow(o[0], o[1], p[0], p[1], 1.1, d) + (N(p[0] + dx, p[1] + dy, lab, sz, a) if lab else "")
