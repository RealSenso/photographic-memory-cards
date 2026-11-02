"""DIP drawing helpers. The everyday picture for all of DIP is a street camera: a CCTV camera on a pole
watching a street corner (bus stop, shop front with windows, lane lines, fence, parked car, wheel, passer-by).
Every frame it records is the image f(x, y); every DIP operation is something done to that frame."""
from air_lib import arrow, dot, dash, circ, fn, f
from subj_lib import T, N, L, P, C, R, E, PG, svg, poly

def cam(x, y, s=1.0, rot=0):
    """the street camera on its pole, lens pointing +x before rotation"""
    return (f'<g transform="translate({f(x)} {f(y)}) rotate({rot}) scale({s})" fill="#ffffff" stroke="#000000" stroke-width="{1/s:.2f}">'
            '<rect x="-9" y="-5" width="14" height="10" rx="1.5"/><polygon points="5,-3 11,-5.5 11,5.5 5,3"/></g>')

def pole(x, y_top, y_bot):
    return L(f(x), f(y_top), f(x), f(y_bot), 1)

def person(x, y, h=24, w=1.0):
    """stick figure standing on (x, y), height h"""
    r = h * .11
    return (C(f(x), f(y - h + r), f(r), "#ffffff", w) + L(f(x), f(y - h + 2 * r), f(x), f(y - h * .35), w)
            + L(f(x), f(y - h * .35), f(x - h * .15), f(y), w) + L(f(x), f(y - h * .35), f(x + h * .15), f(y), w)
            + L(f(x - h * .2), f(y - h * .6), f(x + h * .2), f(y - h * .6), w))

def car(x, y, w=36, h=14):
    """side view car, (x, y) = bottom-left"""
    return (P(f"M{f(x)},{f(y)} L{f(x)},{f(y - h * .5)} L{f(x + w * .22)},{f(y - h * .55)} L{f(x + w * .36)},{f(y - h)} L{f(x + w * .7)},{f(y - h)} "
              f"L{f(x + w * .84)},{f(y - h * .55)} L{f(x + w)},{f(y - h * .5)} L{f(x + w)},{f(y)} Z", "#ffffff", 1)
            + C(f(x + w * .22), f(y), f(h * .2), "#ffffff", 1) + C(f(x + w * .78), f(y), f(h * .2), "#ffffff", 1))

def building(x, y, w, h, cols=3, rows=2, fill="#f1f5f9"):
    """shop front with windows, (x, y) = top-left"""
    out = R(f(x), f(y), f(w), f(h), fill, 1)
    cw, rh = w / (cols * 2 + 1), h / (rows * 2 + 1)
    for i in range(cols):
        for j in range(rows):
            out += R(f(x + cw * (2 * i + 1)), f(y + rh * (2 * j + 1)), f(cw), f(rh), "#ffffff", .8)
    return out

def quad(pts, fill="#f1f5f9", d=None, w=1):
    return PG(" ".join(f"{f(a)},{f(b)}" for a, b in pts), fill, w, d)

def pix(x, y, vals, cell=12, sz=7, shade=None):
    """small grid of grey values"""
    out = ""
    for r, row in enumerate(vals):
        for c, v in enumerate(row):
            fl = "#d9dee7" if shade and (r, c) in shade else "#ffffff"
            out += R(f(x + c * cell), f(y + r * cell), cell, cell, fl, .8) + (N(round(x + c * cell + cell / 2, 1), round(y + r * cell + cell / 2 + 2.5, 1), str(v), sz) if v != "" else "")
    return out

def frame(x, y, w, h, lab=None, fill="#ffffff"):
    """a recorded frame (the image f)"""
    return R(f(x), f(y), f(w), f(h), fill, 1) + (N(round(x + w / 2, 1), round(y - 3, 1), lab, 7, "middle") if lab else "")

def bars(x0, base, vals, bw=8, gap=2, fill="#f1f5f9"):
    out = ""
    for i, v in enumerate(vals):
        out += R(f(x0 + i * (bw + gap)), f(base - v), bw, f(v), fill, .8)
    return out

def axes(x0, y0, x1, y1):
    return arrow(x0, y0, x1, y0, 1) + arrow(x0, y0, x0, y1, 1)

def build_fix(CARDS):
    return {cid: {"stmtKind": v["stmtKind"], "statement": v["statement"], "hint": v["hint"], "breakdown": v["breakdown"],
                  "personalConnection": v["conn"], "drawingSvg": v["d"](cid), "drawingCaption": v["cap"],
                  "textbookImg": None, "textbookRef": None} for cid, v in CARDS.items()}

import math
def bell(x0, x1, c, w, h, base, lw=1, d=None, n=40):
    """smooth bump centred at c"""
    pts = [(x0 + (x1 - x0) * i / n, base - h * math.exp(-((x0 + (x1 - x0) * i / n - c) / w) ** 2)) for i in range(n + 1)]
    return poly(pts, lw, d)

def curve(fx, a, b, n=50, lw=1, d=None):
    return poly([(a + (b - a) * i / n, fx(a + (b - a) * i / n)) for i in range(n + 1)], lw, d)

def bgrid(x, y, rows, cell=8, fill="#b8c0cc", lw=.6, mark=None):
    """binary pixel grid: '#' object, '.' background, 'o' = object cell shown in white with a dot (removed)"""
    out = ""
    for r, row in enumerate(rows):
        for c, ch in enumerate(row):
            fl = fill if ch == "#" else ("#7b8494" if ch == "p" else "#ffffff")
            out += R(f(x + c * cell), f(y + r * cell), cell, cell, fl, lw)
    return out
