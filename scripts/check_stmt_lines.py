"""Checks the line-by-line statements in scripts/subj_<subject>_lines_NN.py against the card data, without writing anything.

Usage: python3 scripts/check_stmt_lines.py [stoma|dip] 02 03 ...   (subject defaults to stoma; no topics: every lines module)
For each card it checks that
  - the card exists, is of this subject, and has a statement
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

args = sys.argv[1:]
key = args.pop(0) if args and args[0] in ("stoma", "dip") else "stoma"
SUBJECT = {"stoma": "StoMA", "dip": "DIP"}[key]
prefix = f"subj_{key}_lines_"
cards = {c["id"]: c for p in ("cards_data.js", f"cards_{key}.js") for c in load(os.path.join(root, p))}

def norm(s):
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"\\(nolimits|displaystyle|textstyle|quad|qquad|,|;|!| )", "", s)
    return re.sub(r"[\s$().,;:]", "", s)

ALLOWED = re.compile(r'</?b>|<span class="(ln|ln in|ln in2|src)">|</span>')
mods = args or sorted(os.path.basename(p)[len(prefix):-3] for p in glob.glob(os.path.join(here, prefix + "*.py")))
bad = 0
for m in mods:
    mod = importlib.import_module(prefix + m)
    for cid, f in mod.FIX.items():
        c = cards.get(cid)
        errs = []
        if not c or c.get("subject") != SUBJECT: errs.append(f"not a {SUBJECT} card")
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
    print(f"{prefix}{m}: {len(mod.FIX)} statements checked")
print("OK" if not bad else f"{bad} card(s) need a look")
