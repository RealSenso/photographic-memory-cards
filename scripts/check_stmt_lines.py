"""Checks the line-by-line StoMA statements in scripts/subj_stoma_lines_NN.py against the card data, without writing anything.

Usage: python3 scripts/check_stmt_lines.py 02 03 ...   (no arguments: every subj_stoma_lines_*.py)
For each card it checks that
  - the card exists, is StoMA, and has a statement
  - only the allowed markup is used: <b>..</b>, <span class="ln">, <span class="ln in">, <span class="ln in2">, <span class="src">
  - spans are balanced and $ signs pair up
  - the words and maths are the same as the current statement (only layout changed); differences are printed
"""
import glob, importlib, json, os, re, sys

here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
root = os.path.join(here, "..")

def load(path):
    text = open(path).read()
    i, j = re.search(r"\[\s*\{", text).start(), text.rindex("]") + 1
    return json.loads(text[i:j])

cards = {c["id"]: c for p in ("cards_data.js", "cards_stoma.js") for c in load(os.path.join(root, p))}

def norm(s):
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"\\(displaystyle|textstyle|quad|qquad|,|;|!| )", "", s)
    return re.sub(r"[\s$().,;:]", "", s)

ALLOWED = re.compile(r'</?b>|<span class="(ln|ln in|ln in2|src)">|</span>')
mods = sys.argv[1:] or sorted(os.path.basename(p)[17:-3] for p in glob.glob(os.path.join(here, "subj_stoma_lines_*.py")))
bad = 0
for m in mods:
    mod = importlib.import_module(f"subj_stoma_lines_{m}")
    for cid, f in mod.FIX.items():
        c = cards.get(cid)
        errs = []
        if not c or c.get("subject") != "StoMA": errs.append("not a StoMA card")
        st = f.get("statement", "")
        if set(f) != {"statement"}: errs.append(f"fields other than statement: {sorted(set(f) - {'statement'})}")
        for tag in re.findall(r"<[^>]+>", st):
            if not ALLOWED.fullmatch(tag): errs.append(f"markup not allowed: {tag}")
        if st.count("<span") != st.count("</span>"): errs.append("unbalanced <span>")
        if re.sub(r"\$\$", "", st).count("$") % 2: errs.append("odd number of $")
        if not st.startswith("<b>"): errs.append("should start with the <b>title</b>")
        if c and c.get("statement") and norm(st) != norm(c["statement"]):
            a, b = norm(c["statement"]), norm(st)
            k = next((i for i in range(min(len(a), len(b))) if a[i] != b[i]), min(len(a), len(b)))
            errs.append(f"text differs from the card at ...{a[max(0,k-30):k+40]}... vs ...{b[max(0,k-30):k+40]}...")
        if errs:
            bad += 1
            print(f"{cid}:"); [print("   ", e) for e in errs]
    print(f"subj_stoma_lines_{m}: {len(mod.FIX)} statements checked")
print("OK" if not bad else f"{bad} card(s) need a look")
