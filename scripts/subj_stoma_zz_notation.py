"""StoMA: one notation across every card (the last layer, so it wins over the earlier ones).

  probability   ℙ(·)  (LaTeX \\mathbb P), never a plain P(·); P stays the transition matrix / kernel (P_ij, Pⁿ, P(t))
  expectation   𝔼[·], 𝔼|·|  (LaTeX \\mathbb E), never a plain E[·]
  normal        𝒩(μ, σ²)  (LaTeX \\mathcal N), never a plain N(0, 1)
  char. fn      φ_X  (LaTeX \\varphi_X), never \\phi_X
  uniform       Uniform(a, b), never Unif(·) or Uniform[a, b]
Var, Cov, f_X, p_X, F_X, M_X, G_X, P_ij^(n) and the convergence arrows (a.s., P, d, Lᵖ) were already used one way.
"""
import json, os, re

SUBJECT = "StoMA"
_here = os.path.dirname(os.path.abspath(__file__))


def _load(name):
    t = open(os.path.join(_here, "..", name)).read()
    return json.loads(t[re.search(r"\[\s*\{", t).start():t.rindex("]") + 1])


CARDS = {c["id"]: c for f in ("cards_data.js", "cards_stoma.js") for c in _load(f) if c["subject"] == SUBJECT}
MATRIX_P = {32203, 32204, 32702}   # P is the transition matrix, kernel or P(t) here
FIELDS = ["title", "statement", "math", "coreTranslation", "breakdown", "drawingCaption", "personalConnection",
          "examTrap", "hint", "drawingSvg"]
SEG = re.compile(r"\$\$[\s\S]+?\$\$|\$[^$]+\$")
NB = r"(?<![A-Za-z\\{])"   # not part of a word or a command


# P(·) that is a transition entry or the matrix function, not a probability: P(O,L), P(i, j), P(t), P(s+t), P(0), P'(t)
TRANS = re.compile(r"\((?:[A-Za-z0-9]{1,3}\s*,\s*[A-Za-z0-9]{1,3}|t|s|h|0|t\s*\+\s*s|s\s*\+\s*t)\)")


def _sub(s, letter, cmd, unicode_ok, guard=lambda s, j: True):
    """replace a bare letter (P, E, N) before ( [ or | by cmd, skipping words, commands and ones already done"""
    out, i = [], 0
    for m in re.finditer(r"(?<![A-Za-z\\{])" + letter + r"(?=[\[(|])", s):
        before = s[:m.start()]
        if re.search(r"\\math(?:bb|cal)\s*\{?\s*$", before) or not guard(s, m.end()):
            continue
        out.append(s[i:m.start()] + cmd); i = m.end()
    return "".join(out) + s[i:]


def _prob(s, j):
    return s[j] == "(" and not TRANS.match(s, j)


def _normal(s, j):
    return re.match(r"\((?:0\s*,|\\mu|μ)", s[j:]) is not None


def tex(s, cid):
    if cid not in MATRIX_P:
        s = _sub(s, "P", r"\mathbb P", False, _prob)
    s = _sub(s, "E", r"\mathbb E", False, lambda s, j: s[j] in "[|(")
    s = _sub(s, "N", r"\mathcal N", False, _normal)
    s = re.sub(r"\\phi(?=_)", r"\\varphi", s)
    s = re.sub(r"\\(?:mathrm|text|operatorname)\{Unif(?:orm)?\}", r"\\text{Uniform}", s)
    s = re.sub(r"(\\text\{Uniform\})\s*\[([^\]]*)\]", r"\1(\2)", s)
    return s


def plain(s, cid):
    if cid not in MATRIX_P:
        s = _sub(s, "P", "ℙ", True, _prob)
    s = _sub(s, "E", "𝔼", True, lambda s, j: s[j] in "[|")
    s = _sub(s, "N", "𝒩", True, _normal)
    s = re.sub(r"\bUnif(?:orm)?\s*\[([^\]]*)\]", r"Uniform(\1)", s)
    s = re.sub(r"\bUnif\(", "Uniform(", s)
    return s


def mixed(s, cid):
    parts = re.split(r"(\$\$[\s\S]+?\$\$|\$[^$]+\$)", s)
    return "".join(tex(p, cid) if p.startswith("$") else plain(p, cid) for p in parts)


def svg(s, cid):
    return re.sub(r"(<text[^>]*>)(.*?)(</text>)", lambda m: m.group(1) + plain(m.group(2), cid) + m.group(3), s, flags=re.S)


FIX = {}
for cid, c in CARDS.items():
    out = {}
    for f in FIELDS:
        v = c.get(f)
        if v is None:
            continue
        fn = svg if f == "drawingSvg" else (lambda s, i: tex(s, i)) if f == "math" else mixed
        out[f] = [fn(x, cid) for x in v] if isinstance(v, list) else fn(v, cid)
    FIX[cid] = out
