import re,json,sys
n=int(sys.argv[1])
for p in ('cards_data.js','cards_dip.js'):
    t=open(p).read(); i=re.search(r"\[\s*\{",t).start(); j=t.rindex("]")+1
    for c in json.loads(t[i:j]):
        if c['subject']=='DIP' and int(c['topicId'][:2])==n:
            print(c['id'],c['title']);print(' M:',c['math']);print(' C:',' || '.join(c['coreTranslation']));print(' T:',c['examTrap'])
