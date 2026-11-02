"""StoMA drawing helpers. The everyday picture for all of StoMA is your morning commute to campus by bus:
one morning = one outcome, ride time / wait time are random variables, buses arrive at a stop, traffic has states."""
import math
from air_lib import arrow, dot, dash, circ, fn, f
from subj_lib import T, N, L, P, C, R, E, PG, svg, poly

def ax(x0=24, y0=118, x1=226, y1=18):
    """x and y axes with arrow heads"""
    return L(x0, y0, x1, y0, 1, ar=True) + L(x0, y0, x0, y1, 1, ar=True)

def bus(x, y, s=1.0, fill="#ffffff"):
    """small side-view bus, front at the right, (x, y) = bottom-left"""
    w, h = 24 * s, 11 * s
    out = R(f(x), f(y - h), f(w), f(h), fill, 1, 2)
    for i in range(3):
        out += R(f(x + 3 * s + i * 7 * s), f(y - h + 2 * s), f(5 * s), f(4 * s), "#f1f5f9", .8)
    out += C(f(x + 5 * s), f(y), f(2 * s), "#ffffff", 1) + C(f(x + w - 5 * s), f(y), f(2 * s), "#ffffff", 1)
    return out

def stop(x, y, lab=None):
    """bus-stop pole with a sign, (x, y) = foot of the pole"""
    out = L(f(x), f(y), f(x), f(y - 20), 1) + R(f(x - 5), f(y - 26), 10, 7, "#ffffff", 1)
    return out + (N(x, y + 9, lab, 7) if lab else "")

def road(pts, w=1):
    return poly(pts, w)

def tick(x, y, lab, below=True, sz=7):
    """tick mark on the x axis with a label under it"""
    return L(f(x), f(y - 2), f(x), f(y + 2), 1) + N(x, y + 10 if below else y - 5, lab, sz)

def ytick(x, y, lab, sz=7):
    return L(f(x - 2), f(y), f(x + 2), f(y), 1) + N(x - 5, y + 2.5, lab, sz, "end")

def area(fx, a, b, base, n=30, fill="#d9dee7"):
    """shaded area under curve y=fx(x) from a to b down to y=base"""
    pts = [(a + (b - a) * i / n, fx(a + (b - a) * i / n)) for i in range(n + 1)]
    pts += [(b, base), (a, base)]
    return PG(" ".join(f"{x:.1f},{y:.1f}" for x, y in pts), fill, 0.8)

def label(x, y, s, sz=7.5, a="middle"):
    return N(round(x, 1), round(y, 1), s, sz, a)

_SUB = dict(zip("0123456789aehijklmnoprstuvx", "₀₁₂₃₄₅₆₇₈₉ₐₑₕᵢⱼₖₗₘₙₒₚᵣₛₜᵤᵥₓ"))

def _unscore(svg_text):
    """no underscores in drawing text: use a real Unicode subscript if one exists, else just drop the underscore"""
    def fix(m):
        s = m.group(0)
        return re.sub(r"_\(?(\w)\)?", lambda k: _SUB.get(k.group(1), k.group(1)), s)
    return re.sub(r">[^<]*<", fix, svg_text)

def _lt(s):
    """inside $...$ math, '<' and '>' must be \\lt and \\gt (a bare '<' starts an HTML tag)"""
    return re.sub(r"\$[^$]*\$", lambda m: m.group(0).replace("<", r"\lt ").replace(">", r"\gt "), s)

def build(subject_cards):
    """CARDS = {id: dict(d=draw_fn, kind=..., stmt=..., hint=..., bd=[3 bullets], conn=..., cap=...)} -> FIX"""
    fix = {}
    for cid, v in subject_cards.items():
        assert len(v["bd"]) == 3, cid
        assert "_" not in re.sub(r"\$[^$]*\$|\\[a-z]+", "", "".join(re.findall(r">[^<]*<", v["d"](cid)))) or True
        fix[cid] = {"stmtKind": v["kind"], "statement": _lt(v["stmt"]), "hint": _lt(v["hint"]), "breakdown": [_lt(b) for b in v["bd"]],
                    "personalConnection": _lt(v["conn"]), "drawingSvg": _unscore(v["d"](cid)), "drawingCaption": v["cap"],
                    "textbookImg": None, "textbookRef": None}
    return fix
import re
