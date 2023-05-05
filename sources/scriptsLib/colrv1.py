# -*- coding: UTF-8 -*-
#
#   Build a variants of Bitcount VF/TTF/OTF from here.
#   Optionally add COLRv1 pixels into the UFO.
#
#   https://github.com/googlefonts/colr-gradients-spec
#
import os
import ufoLib2
import shutil
import codecs
from ufo2ft.constants import COLOR_LAYERS_KEY, COLOR_PALETTES_KEY
from fontTools.ttLib.tables import otTables as ot
from fontTools.colorLib.builder import buildCOLR
from fontTools.colorLib.builder import buildCPAL

from scriptsLib import SMIN, S1DEF, S2DEF, SMAX, LMIN, LDEF, LMAX


def addCOLRv1Layers(f, LR1S=S1DEF, LR1X=LDEF, LR1Y=LDEF, LR2S=S2DEF, LR2X=LDEF, LR2Y=LDEF):
    #print(f'... Add COLRv1 to {f.path}')

    pixelLayer1 = getPaintRadialGradient1(LR1S, LR1X, LR1Y)
    pixelLayer2 = getPaintRadialGradient2(LR2S, LR2X, LR2Y)
    colorGlyphs = {}
    for glyphName in f.keys():

        colorGlyphs[glyphName] = buildPixelGlyph("px", pixelPositions(f, glyphName), pixelLayer1, pixelLayer2)

    #print(colorGlyphs)
    f.lib[COLOR_PALETTES_KEY] = palettes
    f.lib[COLOR_LAYERS_KEY] = colorGlyphs

def buildPixelGlyph(pixelGlyphName, pixelPositions, layer1, layer2):
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
                "Paint": layer1,
                "Glyph": pixelGlyphName,
            },
            "dx": x,
            "dy": y,
        }
        layers.append(layer)
        layer = {
            "Format": ot.PaintFormat.PaintTranslate,
            "Paint": {
                "Format": ot.PaintFormat.PaintGlyph,
                "Paint": layer2,
                "Glyph": pixelGlyphName,
            },
            "dx": x,
            "dy": y,
        }
        layers.append(layer)
    if len(layers) == 1:
        return layers[0]
    else:
        return (ot.PaintFormat.PaintColrLayers, layers)

palettes = (
    (
        (1, 0, 1, 0.5),
        (1, 1, 1, 0.5),
        (0, 0.2, 1, 0.5),
        (1, 0.2, 0, 0.5),
        (0, 1, 0, 0.5),
        (0, 1, 1, 0.5),
        (0, 0, 0, 0.5),

        (0, 0.2, 1, 1),
        (1, 0.2, 0, 1),
        (1, 0, 1, 1),
        (0, 1, 0, 1),
        (1, 1, 1, 1),
        (0, 0, 0, 1),
        (0, 1, 1, 1),

        (1, 1, 1, 1), # White
    ),
)

color1 = 0  # palette index
color2 = 1  # palette index
color3 = 2  # palette index
color4 = 3  # palette index
color5 = 4  # palette index
color6 = 5  # palette index
color7 = 6  # palette index

color10 = 7
color11 = 8
color12 = 9
color13 = 10
color14 = 11
color15 = 12
color16 = 13

white = 14

N = 14
# TODO: Organize this as a loop
COLOR_STOPS1 = ((0/N, white), (1/N, color1), (2/N, color2), (3/N, color3), (4/N, color4), (5/N, color5), (6/N, color6), (7/N, color7),
                (8/N, color10), (9/N, color11), (10/N, color12), (11/N, color13), (12/N, color14), (13/N, color15), (14/N, color16))
COLOR_STOPS2 = ((0/N, white), (1/N, color16), (2/N, color15), (3/N, color14), (4/N, color13), (5/N, color12), (6/N, color11), (7/N, color10),
                (8/N, color7), (9/N, color6), (10/N, color5), (11/N, color4), (12/N, color3), (13/N, color2), (14/N, color1))

def getPaintRadialGradient1(s, x, y):
    layers = []
    r1 = {
        "Format": ot.PaintFormat.PaintRadialGradient,
        "ColorLine": {
            "ColorStop": COLOR_STOPS1,  # can be more than 2
            "Extend": "pad",  # pad, repeat, reflect
        },
        "x0": x+50,
        "y0": y+50,
        "r0": 1,
        "x1": x+50,
        "y1": y+50,
        "r1": s+1,
    }
    r2 = {
        "Format": ot.PaintFormat.PaintRadialGradient,
        "ColorLine": {
            "ColorStop": COLOR_STOPS2,  # can be more than 2
            "Extend": "pad",  # pad, repeat, reflect
        },
        "x0": x+500, # Offset into middle of pixel
        "y0": y+50,
        "r0": 1,
        "x1": x+500,
        "y1": y+50,
        "r1": s+1,
    }
    layers.append(r1)
    return layers[0] # @@@@@ This should be changed
    return (ot.PaintFormat.PaintColrLayers, layers)

def getPaintRadialGradient2(s, x, y):
    layers = []
    r1 = {
        "Format": ot.PaintFormat.PaintRadialGradient,
        "ColorLine": {
            "ColorStop": COLOR_STOPS2,  # can be more than 2
            "Extend": "pad",  # pad, repeat, reflect
        },
        "x0": x+50,
        "y0": y+50,
        "r0": 1,
        "x1": x+50,
        "y1": y+50,
        "r1": s+1,
    }
    layers.append(r1)
    return layers[0] # @@@@@ This should be changed
    return (ot.PaintFormat.PaintColrLayers, layers)


def pixelPositions(f, gName):
    positions = []
    for component in f[gName].components:
        positions.append(tuple(component.transformation[-2:]))
    return tuple(positions)

