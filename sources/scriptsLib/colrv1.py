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

def addCOLRv1(f):
    print(f'... Add COLRv1 to {f.path}')

'''
DS = """<?xml version='1.0' encoding='utf-8'?>
<designspace format="3">
    <axes>
        <axis default="50" maximum="500" minimum="50" name="Weight" tag="wght"/>
        <axis default="0" maximum="500" minimum="-500" name="Layer1-X" tag="LR1X"/>
        <axis default="0" maximum="500" minimum="-500" name="Layer1-Y" tag="LR1Y"/>
        <axis default="0" maximum="500" minimum="-500" name="Layer2-X" tag="LR2X"/>
        <axis default="0" maximum="500" minimum="-500" name="Layer2-Y" tag="LR2Y"/>
    </axes>
    <sources>

        %(sources)s

    </sources>
</designspace>
"""

SRC = """
    <source familyname="Bitcount Mono Double" filename="%(ufoPath)s">
        <location>
            <dimension name="Weight" xvalue="%(s)d"/>
            <dimension name="Layer1-X" xvalue="%(x1)d"/>
            <dimension name="Layer1-Y" xvalue="%(y1)d"/>
            <dimension name="Layer2-X" xvalue="%(x2)d"/>
            <dimension name="Layer2-Y" xvalue="%(y2)d"/>
        </location>
        %(info)s
    </source>
"""


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

def XXXbuildPixelGlyph(pixelGlyphName, pixelPositions, s, gx, gy):
    layers = []
    for layerIndex in range(3):
        for x, y in pixelPositions:
            # Three nested Paints:
            # - PaintTranslate to move the pixel to the right place
            # - PaintGlyph to say which glyph to be drawn
            # - PaintGradient to say how to fill the glyph
            pixel = {
                "Format": ot.PaintFormat.PaintTranslate,
                "Paint": {
                    "Format": ot.PaintFormat.PaintGlyph,
                    "Paint": {
                        "Format": ot.PaintFormat.PaintRadialGradient,
                        "ColorLine": {
                            "ColorStop": ((0.0, color1), (0.15, color2), (0.3, color3), (0.45, color4), (0.6, color5), (0.65, color6), (1, color7)),  # can be more than 2
                            #"ColorStop": ((0.0, color1), (0.25, color2), (0.5, color3), (0.75, color4), (1, color5)),  # can be more than 2
                            "Extend": "pad",  # pad, repeat, reflect
                        },
                        "x0": gx+50+layerIndex*10,
                        "y0": gy+50+layerIndex+10,
                        "r0": 5,
                        "x1": gx+50,
                        "y1": gy+50,
                        "r1": s+5+layerIndex*20,
                    },
                    "Glyph": pixelGlyphName,
                },
                "dx": x,
                "dy": y,
            }
            layers.append(pixel)
    if len(layers) == 1:
        return layers[0]
    else:
        return (ot.PaintFormat.PaintColrLayers, layers)

fonts = {}
ufoNameTemplates = dict(S='Bitcount_Mono_Double_S.ufo', Smax='Bitcount_Mono_Double_Smax.ufo')
for s in ('S', 'Smax'):
    for x1 in ('X1min', 'X1', 'X1max'):
        for y1 in ('Y1min', 'Y1', 'Y1max'):
            for x2 in ('X2min', 'X2', 'X2max'):
                for y2 in ('Y2min', 'Y2', 'Y2max'):
                    key = s + x1 + y1 + x2 + y2
                    srcPath = 'ufo-src/' + ufoNameTemplates[s]
                    ufoPath = 'ufo/' + ufoNameTemplates[s].replace('.ufo', '_%s_%s_%s_%s.ufo' % (x1, y1, x2, y2))
                    if os.path.exists(ufoPath):
                        shutil.rmtree(ufoPath)
                    shutil.copytree(srcPath, ufoPath)
                    fonts[key] = ufoLib2.Font.open(ufoPath)

palettes = (
    (
        (1, 0, 1, 1),
        (1, 1, 1, 1),
        (0, 0.2, 1, 1),
        (1, 0.2, 0, 1),
        (0, 1, 0, 1),
        (0, 1, 1, 1),
        (0, 0, 0, 1),
    ),
)
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

def getPaintRadialGradient1(s, x, y):
    layers = []
    r1 = {
        "Format": ot.PaintFormat.PaintRadialGradient,
        "ColorLine": {
            "ColorStop": ((0.0, color10), (0.15, color11), (0.3, color12), (0.45, color13), (0.6, color14), (0.65, color15), (1, color16)),  # can be more than 2
            #"ColorStop": ((0.0, color1), (0.25, color2), (0.5, color3), (0.75, color4), (1, color5)),  # can be more than 2
            "Extend": "pad",  # pad, repeat, reflect
        },
        "x0": x+50,
        "y0": y+50,
        "r0": 5,
        "x1": x+50,
        "y1": y+50,
        "r1": s+5,
    }
    layers.append(r1)
    return layers[0]
    return (ot.PaintFormat.PaintColrLayers, layers)

def getPaintRadialGradient2(s, x, y):
    layers = []
    r1 = {
        "Format": ot.PaintFormat.PaintRadialGradient,
        "ColorLine": {
            "ColorStop": ((0.0, color1), (0.15, color2), (0.3, color3), (0.45, color4), (0.6, color5), (0.65, color6), (1, color7)),  # can be more than 2
            #"ColorStop": ((0.0, color1), (0.25, color2), (0.5, color3), (0.75, color4), (1, color5)),  # can be more than 2
            "Extend": "pad",  # pad, repeat, reflect
        },
        "x0": x+50,
        "y0": y+50,
        "r0": 1,
        "x1": x+50,
        "y1": y+50,
        "r1": s+5,
    }
    layers.append(r1)
    return layers[0]
    return (ot.PaintFormat.PaintColrLayers, layers)

def getPaintCircle(gName, s, x, y, colorIndex):
    layers = []
    r1 = {
        "Format": ot.PaintFormat.PaintTranslate,
        "Paint": {
            "Format": ot.PaintFormat.PaintGlyph,
            "Paint": {
                "Format": ot.PaintFormat.PaintSolid,
                "PaletteIndex":  colorIndex,
                "Alpha": 1,
            },
            "Glyph": 'circle',
        },
        "dx": x,
        "dy": y,
    }
    layers.append(r1)
    r1 = {
        "Format": ot.PaintFormat.PaintScale,
        "Paint": {
            "Format": ot.PaintFormat.PaintTranslate,
            "Paint": {
                "Format": ot.PaintFormat.PaintGlyph,
                "Paint": {
                    "Format": ot.PaintFormat.PaintSolid,
                    "PaletteIndex":  colorIndex,
                    "Alpha": 1,
                },
                "Glyph": gName,
            },
            "dx": x+200,
            "dy": y+200,
        },
        "scaleX": 0.1,
        "scaleY": 0.1,
    }
    layers.append(r1)
    return (ot.PaintFormat.PaintColrLayers, layers)



def pixelPositions(f, gName):
    positions = []
    for component in f[gName].components:
        positions.append(tuple(component.transformation[-2:]))
    return tuple(positions)

designSpaceSources = []

#print(fonts)
#values = dict(S=50, Smax=500, X1min=-500, X1=0, X1max=500, Y1min=-500, Y1=0, Y1max=500,
#                               X2min=-500, X2=0, X2max=500, Y2min=-500, Y2=0, Y2max=500)
# for s in ('S', 'Smax'):
#     for x1 in ('X1min', 'X1', 'X1max'):
#         for y1 in ('Y1min', 'Y1', 'Y1max'):
#             for x2 in ('X2min', 'X2', 'X2max'):
#                 for y2 in ('Y2min', 'Y2', 'Y2max'):
#                     key = s + x1 + y1 + x2 + y2
#                     if s == 0 and x1 == y1 == x2 == y2 == 0:
#                         info = '\t\t\t<info copy="1"/>\n'
#                     else:
#                         info = ''
#                     ufoPath = 'ufo/' + ufoNameTemplates[s].replace('.ufo', '_%s_%s_%s_%s.ufo' % (x1, y1, x2, y2))
#                     designSpaceSources.append(SRC % dict(s=values[s], x1=values[x1], y1=values[y1], x2=values[x2], y2=values[y2], ufoPath=ufoPath, info=info ))
#                     print('===', key)

#                     f = fonts[key]
#                     pixelLayer1 = getPaintRadialGradient1(values[s], values[x1], values[y1])
#                     pixelLayer2 = getPaintRadialGradient2(values[s], values[x2], values[y2])
#                     #circleLayer2 = getPaintCircle(values[s], values[x]+20, values[y]+20, color2)
#                     colorGlyphs = {}
#                     for glyphName in ('a', 'b', 'c', 'space'): #sorted(f.keys()):
#                         circleLayer1 = getPaintCircle(glyphName, values[s], values[x2], values[y2], white)

#                         colorGlyphs[glyphName] = buildPixelGlyph("px", pixelPositions(f, glyphName), pixelLayer1, circleLayer1)

#                     #print(colorGlyphs)
#                     f.lib = {}
#                     f.lib[COLOR_PALETTES_KEY] = palettes
#                     f.lib[COLOR_LAYERS_KEY] = colorGlyphs
#                     #print(f.lib)

#                     f.save()


# designSpace = DS % dict(sources='\n'.join(designSpaceSources))

# dsFile = codecs.open('BitcountMono_Double2-TEST.designspace', 'w', encoding='utf-8')
# dsFile.write(designSpace)
# dsFile.close()

# os.system('fontmake -m BitcountMono_Double2-TEST.designspace -o variable')

# print('--- Done')
'''
