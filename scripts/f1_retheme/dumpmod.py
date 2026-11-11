import ast, sys
p = sys.argv[1]; src = open(p).read(); t = ast.parse(src)
print('DOC:', ast.get_docstring(t))
for n in t.body:
    if isinstance(n, ast.FunctionDef) and n.name not in ('_',):
        print(ast.get_source_segment(src, n))
    if isinstance(n, ast.Assign) and n.targets[0].id == 'CARDS':
        for k, v in zip(n.value.keys, n.value.values):
            kw = {x.arg: x.value for x in v.keywords}
            print('\n##', k.value, 'd=', ast.get_source_segment(src, kw['d']), 'kind=', ast.literal_eval(kw['kind']))
            for key in ('hint', 'bd', 'conn', 'cap'):
                print(' ', key + ':', ast.literal_eval(kw[key]))
    if isinstance(n, ast.Assign) and n.targets[0].id == 'STORY':
        for k, v in zip(n.value.keys, n.value.values):
            kw = {x.arg: x.value for x in v.keywords}
            print('S', k.value, ast.literal_eval(kw['s']), '|', ast.literal_eval(kw['b']))
