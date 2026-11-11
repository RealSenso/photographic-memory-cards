"""Rewrites parts of a subj_<subject>_NN.py module in place, leaving everything else (statements, kinds) untouched.

Usage (from Python):  patch(path, doc=..., draw={fname: new_source}, cards={id: {key: value}}, story={id: {key: value}})
- doc:   new module docstring
- draw:  full new source of drawing functions, replacing the function of that name (or appended if new)
- cards: new values for keyword arguments of CARDS[id] = dict(...) (hint, bd, conn, cap, d, ...)
- story: new values for keyword arguments of STORY[id] = dict(...)
Values are written as Python literals; strings with backslashes become raw strings where that is safe.
"""
import ast


def lit(v):
    if isinstance(v, str):
        if '\\' in v and '"' not in v and not v.endswith('\\') and '\n' not in v:
            return 'r"' + v + '"'
        return repr(v)
    if isinstance(v, list):
        return '[' + ',\n      '.join(lit(x) for x in v) + ']'
    if isinstance(v, (int, float)):
        return repr(v)
    if isinstance(v, Name):
        return v.s
    raise TypeError(type(v))


class Name:
    """a bare identifier, e.g. the drawing function d=d3"""
    def __init__(self, s): self.s = s


def _pos(src):
    lines = src.encode().splitlines(keepends=True)
    starts = [0]
    for l in lines: starts.append(starts[-1] + len(l))
    return lambda node, end=False: starts[(node.end_lineno if end else node.lineno) - 1] + (node.end_col_offset if end else node.col_offset)


def patch(path, doc=None, draw=None, cards=None, story=None):
    text = open(path).read()
    tree = ast.parse(text)
    off = _pos(text)
    src = text.encode()   # AST offsets are byte offsets
    edits = []   # (start, end, text)
    if doc is not None:
        d = tree.body[0]
        assert isinstance(d, ast.Expr) and isinstance(d.value, ast.Constant)
        edits.append((off(d), off(d, True), ('"""' + doc + '"""').encode()))
    seen = set()
    for n in tree.body:
        if isinstance(n, ast.FunctionDef) and draw and n.name in draw:
            edits.append((off(n), off(n, True), draw[n.name].strip('\n').encode()))
            seen.add(n.name)
        if isinstance(n, ast.Assign) and isinstance(n.targets[0], ast.Name) and n.targets[0].id in ('CARDS', 'STORY'):
            table = cards if n.targets[0].id == 'CARDS' else story
            if not table: continue
            for k, v in zip(n.value.keys, n.value.values):
                cid = k.value
                for kw in v.keywords:
                    if cid in table and kw.arg in table[cid]:
                        edits.append((off(kw.value), off(kw.value, True), lit(table[cid][kw.arg]).encode()))
    missing = set(draw or {}) - seen
    for e in sorted(edits, key=lambda t: -t[0]):
        src = src[:e[0]] + e[2] + src[e[1]:]
    src = src.decode()
    if missing:   # new drawing functions go right before CARDS
        i = src.index('\nCARDS = {')
        src = src[:i] + '\n' + '\n\n'.join(draw[m].strip('\n') for m in sorted(missing)) + '\n' + src[i:]
    ast.parse(src)
    open(path, 'w').write(src)
    return len(edits)
