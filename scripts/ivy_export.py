import fitz, json, os, sys, io
from PIL import Image
root, idx, out = sys.argv[1], sys.argv[2], sys.argv[3]
d = json.load(open(idx)); total = 0; meta = {}
for topic, v in d.items():
    doc = fitz.open(os.path.join(root, topic, v['file']))
    t2 = topic[:2]; os.makedirs(os.path.join(out, t2), exist_ok=True)
    for n, q in enumerate(v['qs'], 1):
        q['files'] = []
        for k, (pno, xref, bbox) in enumerate(q['imgs']):
            im = Image.open(io.BytesIO(doc.extract_image(xref)['image'])).convert('L')
            # keep text crisp but light: at most 1400 px wide
            if im.width > 1400: im = im.resize((1400, round(im.height * 1400 / im.width)), Image.LANCZOS)
            name = f"{t2}/q{n:02d}{'abc'[k] if len(q['imgs']) > 1 else ''}.webp"
            im.save(os.path.join(out, name), 'WEBP', quality=72, method=6)
            q['files'].append([name, im.width, im.height]); total += os.path.getsize(os.path.join(out, name))
json.dump(d, open(idx.replace('index.json', 'index2.json'), 'w'), indent=1)
print('total MB', round(total / 1e6, 2))
