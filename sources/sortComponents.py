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

UFO_PATH = 'ufo/'
UFO_NAMES = [
    'Bitcount_Grid_Double_Italic.ufo',    'Bitcount_Grid_Double.ufo',    'Bitcount_Grid_Single_Italic.ufo',    'Bitcount_Grid_Single.ufo',    'Bitcount_Mono_Double-Italic.ufo',    'Bitcount_Mono_Double.ufo',    'Bitcount_Mono_Single-Italic.ufo',    'Bitcount_Mono_Single.ufo',    'Bitcount_Prop_Double-Italic.ufo',    'Bitcount_Prop_Double.ufo',    'Bitcount_Prop_Single-Italic.ufo',    'Bitcount_Prop_Single.ufo',
]
for ufoName in UFO_NAMES:
    f = OpenFont(UFO_PATH + ufoName, showInterface=False)
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
    f.save()
    f.close()
    
print('--- Done')

