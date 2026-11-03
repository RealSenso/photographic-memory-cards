"""Helpers for the notation passes: textual substitutions over the current card fields, plus explicit overrides.

build(SUBS, EXPLICIT) -> FIX.  SUBS = {card_id: [(old, new), ...]} applied to math, breakdown, personalConnection,
drawingCaption, drawingSvg, coreTranslation, examTrap, hint.  Every pair must be found (old, or already new) in some field.
Math inside $...$ is also normalised: ^T -> ^\\top and bare < > -> \\lt \\gt.
"""
import json, os, re

_here = os.path.dirname(os.path.abspath(__file__))
_t = open(os.path.join(_here, "..", "cards_data.js")).read()
CARDS = {c["id"]: c for c in json.loads(_t[_t.index("["):_t.rindex("]") + 1])}
MISSES = []
FIELDS = ["math", "breakdown", "personalConnection", "drawingCaption", "drawingSvg", "coreTranslation", "examTrap", "hint", "statement"]


def _norm_math(s):
    def seg(m):
        x = m.group(0)
        x = re.sub(r"\^T(?![A-Za-z])", r"^\\top", x)
        x = re.sub(r"\^\{T\}", r"^\\top", x)
        x = re.sub(r"(?<![\\<])<(?![\\a-zA-Z/!])", r"\\lt ", x) if "<" in x else x
        x = re.sub(r"(?<![\\>-])>(?![a-zA-Z])", r"\\gt ", x) if ">" in x else x
        return x
    return re.sub(r"\$\$.+?\$\$|\$[^$\n]+\$", seg, s, flags=re.S)


def build(SUBS=None, EXPLICIT=None, normalise_ids=()):
    SUBS, EXPLICIT = SUBS or {}, EXPLICIT or {}
    out = {}
    for cid in set(SUBS) | set(EXPLICIT) | set(normalise_ids):
        c = CARDS[cid]
        fix = {}
        for fld in FIELDS:
            v = c.get(fld)
            if v is None:
                continue
            is_list = isinstance(v, list)
            items = list(v) if is_list else [v]
            items = [_norm_math(x) if fld != "drawingSvg" else x for x in items]
            fix[fld] = items if is_list else items[0]
        found = set()
        for old, new in sorted(SUBS.get(cid, []), key=lambda t: -len(t[0])):
            hit = False
            for fld, v in fix.items():
                items = v if isinstance(v, list) else [v]
                new_items = []
                for x in items:
                    if old in x or new in x:
                        hit = True
                    new_items.append(x.replace(old, new))
                fix[fld] = new_items if isinstance(v, list) else new_items[0]
            if not hit:
                MISSES.append(f"card {cid}: pattern not found: {old[:70]!r}")
        fix.update(EXPLICIT.get(cid, {}))
        out[cid] = fix
    return out
