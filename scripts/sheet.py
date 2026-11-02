"""Contact sheet of one DIP topic's drawings -> sheet_dip_NN.html (open in the browser pane)."""
import re,json,sys
n=int(sys.argv[1]); out=[]
for p in ('cards_data.js','cards_dip.js'):
    t=open(p).read(); i=re.search(r"\[\s*\{",t).start(); j=t.rindex("]")+1
    for c in json.loads(t[i:j]):
        if c['subject']=='DIP' and int(c['topicId'][:2])==n:
            out.append(f"<div style='width:480px;display:inline-block;margin:6px;font:11px sans-serif'><div style='border:1px solid #ccc;background:#fff'>{c['drawingSvg']}</div>{c['id']} {c['title']}<br>{c.get('drawingCaption','')}</div>")
open(f"sheet_dip_{n:02d}.html","w").write("<meta charset=utf-8><body style='background:#eee'>"+"".join(out))
