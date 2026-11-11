import sys, importlib.util, os
sys.path.insert(0, '/Users/senso/Projects/photographic-memory-cards/scripts')
from retheme_patch import patch, Name
for t in sys.argv[1:]:
    spec = importlib.util.spec_from_file_location('fb' + t, os.path.join(os.path.dirname(os.path.abspath(__file__)), f'fb{t}.py'))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    n = patch(f'/Users/senso/Projects/photographic-memory-cards/scripts/subj_stoma_{t}.py', doc=m.DOC, draw=m.DRAW, cards=m.CARDS, story=getattr(m, 'STORY', {}))
    path = f'/Users/senso/Projects/photographic-memory-cards/scripts/subj_stoma_{t}.py'
    src = open(path).read()
    for a, b in getattr(m, 'SUBS', []):
        assert a in src or b in src, (t, a)
        src = src.replace(a, b)
    open(path, 'w').write(src)
    print(t, n, 'edits,', len(getattr(m, 'SUBS', [])), 'label subs')
