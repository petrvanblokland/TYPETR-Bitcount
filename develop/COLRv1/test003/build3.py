# -*- coding: UTF-8 -*-
#
#   Build a variants of Bitcount VF/TTF/OTF from here.
#   Optionally add COLRv1 pixels into the UFO.
#
#   https://github.com/googlefonts/colr-gradients-spec
#
import os
import ufoLib2
from ufo2ft.constants import COLOR_LAYERS_KEY, COLOR_PALETTES_KEY
from fontTools.ttLib.tables import otTables as ot
from fontTools.colorLib.builder import buildCOLR
from fontTools.colorLib.builder import buildCPAL


def buildPixelGlyph(pixelGlyphName, pixelPositions, gradient):
    layers = []
    for x, y in pixelPositions:
        # Three nested Paints:
        # - PaintTranslate to move the pixel to the right place
        # - PaintGlyph to say which glyph to be drawn
        # - PaintGradient to say how to fill the glyph
        layer = {
            "Format": ot.PaintFormat.PaintTranslate,
            "Paint": {
                "Format": ot.PaintFormat.PaintGlyph,
                "Paint": gradient,
                "Glyph": pixelGlyphName,
            },
            "dx": x,
            "dy": y,
        }
        layers.append(layer)
    layers = tuple(layers)
    if len(layers) == 1:
        return layers[0]
    else:
        return (ot.PaintFormat.PaintColrLayers, layers)


f1 = ufoLib2.Font.open('ufo/Bitcount_Mono_Double1.ufo')
f2 = ufoLib2.Font.open('ufo/Bitcount_Mono_Double2.ufo')

palettes = (
    (
        (1, 0.2, 0, 1),
        (0, 0.2, 1, 1),
    ),
)

color1 = 0  # palette index
color2 = 1  # palette index

pixelGradient1 = {
    "Format": ot.PaintFormat.PaintLinearGradient,
    "ColorLine": {
        #"ColorStop": ((0.0, color1), (1.0, color2)),  # can be more than 2
        "ColorStop": ((0.0, color1), (1.0, color2)),  # can be more than 2
        "Extend": "pad",  # pad, repeat, reflect
    },
    "x0": -50,
    "y0": -50,
    "x1": 50,
    "y1": 50,
    "x2": -100,  # x2, y2 determine the shear of the gradient, relative to (x0, y0), (x1, y1)
    "y2": 0,
}

pixelGradient2 = {
    "Format": ot.PaintFormat.PaintLinearGradient,
    "ColorLine": {
        #"ColorStop": ((0.0, color2), (1.0, color1)),  # can be more than 2
        "ColorStop": ((0.0, color1), (1.0, color2)),  # can be more than 2
        "Extend": "pad",  # pad, repeat, reflect
    },
    "x0": -150,
    "y0": -150,
    "x1": 150,
    "y1": 150,
    "x2": -200,  # x2, y2 determine the shear of the gradient, relative to (x0, y0), (x1, y1)
    "y2": 0,
}

def pixelPositions(f, gName):
    positions = []
    for component in f[gName].components:
        positions.append(tuple(component.transformation[-2:]))
    return tuple(positions)

for f, pixelGradient in (
        (f1, pixelGradient1), 
        (f2, pixelGradient2)):
    colorGlyphs = {}
    for glyphName in ('a', 'b', 'c', 'space'): #sorted(f.keys()):

        colorGlyphs[glyphName] = buildPixelGlyph("d", pixelPositions(f, glyphName), pixelGradient)

    #print(colorGlyphs)
    f.lib = {}
    f.lib[COLOR_PALETTES_KEY] = palettes
    f.lib[COLOR_LAYERS_KEY] = colorGlyphs
    #print(f.lib)
    #buildCOLR(
    #    colorGlyphs,
    #    #glyphMap=glyphMap,
    #    #clipBoxes={},
    #)


    f.save()

os.system('fontmake -m BitcountMono_Double2-TEST.designspace -o variable')

print('--- Done')

