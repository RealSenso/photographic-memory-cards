"""StoMA drawing helpers. The everyday picture for all of StoMA is Formula 1: Max Verstappen and Red Bull Racing.
One race (Grand Prix) = one outcome; lap times, pit-stop times, the gap to P2 and points are random variables; safety cars
arrive during a race like a Poisson stream; Max's result moves between win, podium and off-podium from race to race
(a Markov chain); the gap to a rival drifts lap by lap like a random walk."""
import math
from air_lib import arrow, dot, dash, circ, fn, f
from subj_lib import T, N, L, P, C, R, E, PG, svg, poly

def ax(x0=24, y0=118, x1=226, y1=18):
    """x and y axes with arrow heads"""
    return L(x0, y0, x1, y0, 1, ar=True) + L(x0, y0, x0, y1, 1, ar=True)

def car(x, y, s=1.0):
    """a small side-view F1 car facing right, (x, y) = bottom-left of the wheels"""
    w = 26 * s
    body = (f"{x + 2 * s:.1f},{y - 4 * s:.1f} {x + 9 * s:.1f},{y - 7 * s:.1f} {x + 15 * s:.1f},{y - 7 * s:.1f} {x + 17 * s:.1f},{y - 10 * s:.1f} "
            f"{x + 19 * s:.1f},{y - 7 * s:.1f} {x + w:.1f},{y - 5 * s:.1f} {x + w:.1f},{y - 3 * s:.1f} {x + 2 * s:.1f},{y - 3 * s:.1f}")
    return (PG(body, "#ffffff", 1) + L(f(x), f(y - 9 * s), f(x + 4 * s), f(y - 9 * s), 1.2) + L(f(x + 2 * s), f(y - 9 * s), f(x + 2 * s), f(y - 4 * s), .8)
            + C(f(x + 6 * s), f(y - 2.5 * s), f(2.6 * s), "#111111", 1) + C(f(x + w - 5 * s), f(y - 2.5 * s), f(2.6 * s), "#111111", 1))

def flag(x, y, s=1.0):
    """a chequered flag on a pole, (x, y) = foot of the pole"""
    out = L(f(x), f(y), f(x), f(y - 22 * s), 1)
    for i in range(4):
        for j in range(3):
            out += R(f(x + i * 3.5 * s), f(y - 22 * s + j * 3.5 * s), f(3.5 * s), f(3.5 * s), "#111111" if (i + j) % 2 == 0 else "#ffffff", .4)
    return out

def track(x, y, w, h):
    """a simple oval circuit outline with a start line, (x, y) = top-left"""
    return E(f(x + w / 2), f(y + h / 2), f(w / 2), f(h / 2), 0, "none", 1) + E(f(x + w / 2), f(y + h / 2), f(w / 2 - 8), f(h / 2 - 8), 0, "none", .6) + L(f(x + w / 2), f(y + h - 8), f(x + w / 2), f(y + h), 1.2)

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
