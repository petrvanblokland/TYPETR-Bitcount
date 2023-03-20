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
        (0, 0, 0, 1),
        (1, 0, 1, 1),
        (1, 1, 1, 1),
        (0, 0.2, 1, 1),
        (1, 0.2, 0, 1),
        (0, 1, 0, 1),
        (0, 1, 1, 1),
    ),
)

color1 = 0  # palette index
color2 = 1  # palette index
color3 = 2  # palette index
color4 = 3  # palette index
color5 = 4  # palette index
color6 = 5  # palette index
color7 = 6  # palette index

pixelGradient1 = {
    "Format": ot.PaintFormat.PaintLinearGradient,
    "ColorLine": {
        "ColorStop": ((0.0, color1), (0.1, color2), (0.2, color3), (0.3, color4), (0.4, color5), (0.5, color6), (0.6, color7)),  # can be more than 2
        #"ColorStop": ((0.0, color1), (0.25, color2), (0.5, color3), (0.75, color4), (1, color5)),  # can be more than 2
        "Extend": "pad",  # pad, repeat, reflect
    },
    "x0": 500,
    "y0": 500,
    "x1": -1000,
    "y1": -1000,
    "x2": 0,  # x2, y2 determine the shear of the gradient, relative to (x0, y0), (x1, y1)
    "y2": 1000,
}

pixelGradient2 = {
    "Format": ot.PaintFormat.PaintLinearGradient,
    "ColorLine": {
        "ColorStop": ((0.0, color1), (0.1, color2), (0.2, color3), (0.3, color4), (0.4, color5), (0.5, color6), (0.6, color7)),  # can be more than 2
        #"ColorStop": ((0.0, color5), (0.25, color4), (0.5, color3), (0.75, color2), (1, color1)),  # can be more than 2
        "Extend": "reflect",  # pad, repeat, reflect
    },
    "x0": -1500,
    "y0": -1500,
    "x1": 1500,
    "y1": 1500,
    "x2": 0,  # x2, y2 determine the shear of the gradient, relative to (x0, y0), (x1, y1)
    "y2": 1000,
}

PaintRadialGradient1 = {
    "Format": ot.PaintFormat.PaintRadialGradient,
    "ColorLine": {
        "ColorStop": ((0.0, color1), (0.15, color2), (0.3, color3), (0.45, color4), (0.6, color5), (0.65, color6), (1, color7)),  # can be more than 2
        #"ColorStop": ((0.0, color1), (0.25, color2), (0.5, color3), (0.75, color4), (1, color5)),  # can be more than 2
        "Extend": "pad",  # pad, repeat, reflect
    },
    "x0": 50,
    "y0": 50,
    "r0": 0,
    "x1": 50,
    "y1": 50,
    "r1": 50,
}

pixelRadialGradient2 = {
    "Format": ot.PaintFormat.PaintRadialGradient,
    "ColorLine": {
        "ColorStop": ((0.0, color1), (0.15, color2), (0.3, color3), (0.45, color4), (0.6, color5), (0.65, color6), (1, color7)),  # can be more than 2
        #"ColorStop": ((0.0, color5), (0.25, color4), (0.5, color3), (0.75, color2), (1, color1)),  # can be more than 2
        "Extend": "pad",  # pad, repeat, reflect
    },
    "x0": 50,
    "y0": 50,
    "r0": 0,
    "x1": 50,
    "y1": 50,
    "r1": 3000,
}

def pixelPositions(f, gName):
    positions = []
    for component in f[gName].components:
        positions.append(tuple(component.transformation[-2:]))
    return tuple(positions)

for f, pixelGradient in (
        (f1, PaintRadialGradient1), 
        (f2, pixelRadialGradient2)):
    colorGlyphs = {}
    for glyphName in ('a', 'b', 'c', 'space'): #sorted(f.keys()):

        colorGlyphs[glyphName] = buildPixelGlyph("px", pixelPositions(f, glyphName), pixelGradient)

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

