import sys, importlib, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
out = ['<meta charset=utf-8><body style="font-family:sans-serif;display:grid;grid-template-columns:repeat(3,1fr);gap:8px;background:#fff">']
for name in sys.argv[2:]:
    m = importlib.import_module(name)
    for cid, v in m.FIX.items():
        out.append(f'<div style="border:1px solid #ccc;padding:2px"><b style="font-size:11px">{cid}</b><div style="width:100%;aspect-ratio:240/145">{v["drawingSvg"]}</div></div>')
open(sys.argv[1], 'w').write("".join(out))
