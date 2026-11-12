"""Helpers for adding StoMA cards in the current format (statement, hint, breakdown, F1 translation, drawing, story band).
Used by build_stoma_named_distributions.py and build_stoma_gap_cards.py. Writing keeps every other card / story entry as is."""
import json, math, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from stoma_lib import T, N, L, V, P, C, R, AX, box, svg, HL, STOMA_TOPICS  # noqa: F401  (re-exported for the build scripts)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def ln(s, indent=False):
    return f'<span class="ln{" in" if indent else ""}">{s}</span>'


def stmt(head, lines, src):
    return f"<b>{head}</b>" + "".join(lines) + f'<span class="src">{src}</span>'


def bars(vals, x0, base, step, scale, w=None, fill="#f1f5f9", labels=True, ks=None, sz=6.5):
    """Bar chart: bar i at x0 + i*step, height vals[i]*scale, tick label ks[i] under it."""
    w = w or step * 0.62
    out = []
    for i, v in enumerate(vals):
        cx = x0 + i * step
        h = v * scale
        out.append(R(round(cx - w / 2, 1), round(base - h, 1), round(w, 1), round(h, 1), fill, 1.1))
        if labels:
            out.append(N(cx, base + 9, str(ks[i] if ks else i), sz))
    return "".join(out)


def binom(n, p, k):
    return math.comb(n, k) * p ** k * (1 - p) ** (n - k)


def poi(lam, k):
    return math.exp(-lam) * lam ** k / math.factorial(k)


def curve(f, t0, t1, x0, base, sx, sy, n=60):
    """SVG path of y = f(t) for t in [t0, t1]; screen x = x0 + (t - t0) * sx, screen y = base - f(t) * sy."""
    pts = []
    for i in range(n + 1):
        t = t0 + (t1 - t0) * i / n
        pts.append(f"{x0 + (t - t0) * sx:.1f} {base - f(t) * sy:.1f}")
    return "M " + " L ".join(pts)


def make(topic, k, category, title, parts, caption, core, math_, conn, trap, kind, statement, hint, breakdown):
    tid, ttitle = STOMA_TOPICS[topic]
    cid = 30000 + topic * 100 + k
    assert len(breakdown) == 3 and len(core) == 3, cid
    return {
        "id": cid, "subject": "StoMA", "topicId": tid, "topicTitle": ttitle, "cardNumber": f"{k:02d}",
        "category": category, "highlighterClass": HL[(k - 1) % 4], "title": title,
        "drawingSvg": svg(cid, *parts), "drawingCaption": caption, "coreTranslation": core, "math": math_,
        "personalConnection": conn, "examTrap": trap, "stmtKind": kind, "statement": statement, "hint": hint,
        "breakdown": breakdown, "textbookImg": None, "textbookRef": None,
    }


def write_cards(cards, path=os.path.join(ROOT, "cards_stoma.js")):
    text = open(path, encoding="utf-8").read()
    head, rest = text[: text.find("[\n")], text[text.find("[\n"):]
    tail = rest[rest.rfind("}\n]") + 3:]
    m = {c["id"]: c for c in json.loads(rest[: rest.rfind("}\n]") + 3])}
    for c in cards:
        m[c["id"]] = c
    out = sorted(m.values(), key=lambda c: c["id"])
    open(path, "w", encoding="utf-8").write(head + json.dumps(out, indent=2) + tail)
    print(f"cards_stoma.js: {len(out)} cards ({len(cards)} written)")


def write_story(entries, add_links=(), path=os.path.join(ROOT, "story_stoma.js")):
    """entries: {id: (s, b, f, n)}. add_links: (existing_id, [target_id, why]) pairs appended to an existing band's 'n'."""
    text = open(path, encoding="utf-8").read()
    i, j = text.find("{\n"), text.rfind("}") + 1
    d = json.loads(text[i:j])
    for k, (s, b, f, n_) in entries.items():
        d[k] = {"s": s, "b": b, "f": f, "n": n_}
    for src, link in add_links:
        if link not in d[src]["n"]:
            d[src]["n"].append(link)
    d = dict(sorted(d.items(), key=lambda kv: int(kv[0])))
    open(path, "w", encoding="utf-8").write(text[:i] + json.dumps(d, indent=1, ensure_ascii=False) + text[j:])
    print(f"story_stoma.js: {len(d)} story bands")
