# -*- coding: UTF-8 -*-
#
#   Sort the components as overlappong tiles.
#   In COLRv1 the order is showing for bold overlapping pixels.
#
#
#import os
#import fontmake
#from fontmake.font_project import FontProject
#from fontTools.ttLib import TTFont, TTLibError

for f in AllFonts():
    print(f.path)
    for g in f:
        positions = []
        for component in g.components:
            x = component.transformation[-2]
            y = component.transformation[-1]
            positions.append((y, x))
        for cIndex, (y, x) in enumerate(sorted(positions)):
            component = g.components[cIndex]
            t = list(component.transformation)
            t[-2] = x
            t[-1] = y
            component.transformation = t
        g.changed()
    
print('--- Done')

