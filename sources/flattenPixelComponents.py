# -*- coding: UTF-8 -*-

from scriptsLib import *

for f in AllFonts():
    found = False
    print('---', f.path)
    for g in f:
        references = []
        for component in g.components:
            if component.baseGlyph != 'px':
                #print(g.name, component.baseGlyph, f.path)
                references.append((component.baseGlyph, component.transformation[-2:]))

        if references:
            print(g.name, references)
            found = True
    if found:
        break
                
print('Done')