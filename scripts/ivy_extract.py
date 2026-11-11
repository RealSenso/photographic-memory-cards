import fitz, glob, os, sys, json
root, out = sys.argv[1], sys.argv[2]
allq = {}
for f in sorted(glob.glob(os.path.join(root, '*/Ivy*.pdf'))):
    topic = os.path.basename(os.path.dirname(f))
    d = fitz.open(f)
    items = []
    for pno, page in enumerate(d):
        for b in page.get_text('dict')['blocks']:
            if b['type'] == 0:
                txt = '\n'.join(''.join(s['text'] for s in l['spans']) for l in b['lines']).strip()
                if txt: items.append((pno, b['bbox'][1], 'text', txt, list(b['bbox'])))
        for info in page.get_image_info(xrefs=True):
            items.append((pno, info['bbox'][1], 'img', info['xref'], list(info['bbox'])))
    items.sort(key=lambda t: (t[0], t[1]))
    qs, cur, texts, supp = [], None, [], False
    header = []
    for it in items:
        if it[2] == 'text':
            t = it[3]
            if t.startswith('['):
                label = texts[-1] if texts else ''
                cur = {'label': label.replace('\n', ' '), 'tag': ' '.join(t.split('\n')).strip('[] '), 'imgs': [], 'supp': supp}
                qs.append(cur); texts = []
            else:
                if t.startswith('SUPPLEMENTAL'): supp = True
                if not qs: header.append(t)
                texts.append(t)
        else:
            if cur is not None: cur['imgs'].append([it[0], it[3], it[4]])
    allq[topic] = {'header': '\n'.join(header), 'qs': qs, 'file': os.path.basename(f)}
    print(topic[:2], len(qs), 'imgs/q', sorted({len(q['imgs']) for q in qs}), 'nolabel', sum(1 for q in qs if not q['label']), 'supp', sum(q['supp'] for q in qs), 'beyond', sum(q['tag'].startswith('beyond') for q in qs))
json.dump(allq, open(os.path.join(out, 'index.json'), 'w'), indent=1)
