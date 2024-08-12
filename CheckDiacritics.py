f = CurrentFont()
for gName in sorted(f.keys()):
    g = f[gName]
    for a in g.anchors:
        if a.name == '_top':
            print(g.name, a.name)
        if a.name == '_bottom':
            print(g.name, a.name)
        if a.name == '_ogonek':
            print(g.name, a.name)
            if not 'comb' in gName:
                a.name = 'ogonek'
                g.changed()
print('---')

for gName in sorted(f.keys()):
    g = f[gName]
    for a in g.anchors:
        if a.name == 'top':
            print(g.name, a.name)
        if a.name == 'bottom':
            print(g.name, a.name)

print('---')

for gName in sorted(f.keys()):
    g = f[gName]
    for a in g.anchors:
        if a.name == 'ogonek':
            print(g.name, a.name)
