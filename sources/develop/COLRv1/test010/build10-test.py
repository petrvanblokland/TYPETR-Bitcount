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

SMIN = 0
SDEF = 500
SMAX = 1000
LMIN = -500
LDEF = 0
LMAX = 500

DS = f"""<?xml version='1.0' encoding='utf-8'?>
<designspace format="3">
    <axes>
        <axis minimum="{SMIN}" default="{SDEF}" maximum="{SMAX}" name="Layer1-Scale" tag="LR1S"/>
        <axis minimum="{LMIN}" default="{LDEF}" maximum="{LMAX}" name="Layer1-X" tag="LR1X"/>
        <axis minimum="{LMIN}" default="{LDEF}" maximum="{LMAX}" name="Layer1-Y" tag="LR1Y"/>
        <axis minimum="{SMIN}" default="{SDEF}" maximum="{SMAX}" name="Layer2-Scale" tag="LR2S"/>
        <axis minimum="{LMIN}" default="{LDEF}" maximum="{LMAX}" name="Layer2-X" tag="LR2X"/>
        <axis minimum="{LMIN}" default="{LDEF}" maximum="{LMAX}" name="Layer2-Y" tag="LR2Y"/>
    </axes>
    <sources>

        %(sources)s

    </sources>
</designspace>
"""

SRC = """
    <source familyname="Bitcount Mono Double" filename="%(ufoPath)s">
        <location>
            <dimension name="Layer1-Scale" xvalue="%(s1)d"/>
            <dimension name="Layer1-X" xvalue="%(x1)d"/>
            <dimension name="Layer1-Y" xvalue="%(y1)d"/>
            <dimension name="Layer2-Scale" xvalue="%(s2)d"/>
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

SRC_PATH = 'ufo-src/Bitcount_Mono_Double.ufo'
DST_PATH = 'ufo/Bitcount_Mono_Double_%s_%s_%s_%s_%s_%s.ufo'
fonts = {}
#ufoNameTemplates = dict(S1='Bitcount_Mono_Double_S.ufo', S1max='Bitcount_Mono_Double_Smax.ufo',
#                        S2='Bitcount_Mono_Double_S.ufo', S2max='Butcount_Mono_Double_Smax.ufo')
for s1 in ('S1min', 'S1def', 'S1max'):
    for x1 in ('X1min', 'X1def', 'X1max'):
        for y1 in ('Y1min', 'Y1def', 'Y1max'):
            for s2 in ('S2min', 'S2def', 'S2max'):
                for x2 in ('X2min', 'X2def', 'X2max'):
                    for y2 in ('Y2min', 'Y2def', 'Y2max'):
                        key = s1 + x1 + y1 + s2 + x2 + y2
                        ufoPath = DST_PATH % (s1, x1, y1, s2, x2, y2)
                        if os.path.exists(ufoPath):
                            shutil.rmtree(ufoPath)
                        shutil.copytree(SRC_PATH, ufoPath)
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

N = 14

COLOR_STOPS1 = ((0/N, white), (1/N, color1), (2/N, color2), (3/N, color3), (4/N, color4), (5/N, color5), (6/N, color6), (7/N, color7),
                (8/N, color10), (9/N, color11), (10/N, color12), (11/N, color13), (12/N, color14), (13/N, color15), (14/N, color16))
COLOR_STOPS2 = ((0/N, white), (1/N, color16), (2/N, color15), (3/N, color14), (4/N, color13), (5/N, color12), (6/N, color11), (7/N, color10),
                (8/N, color7), (9/N, color6), (10/N, color5), (11/N, color4), (12/N, color3), (13/N, color2), (14/N, color1))

def getPaintRadialGradient1(s, x, y):
    r1 = {
        "Format": ot.PaintFormat.PaintRadialGradient,
        "ColorLine": {
            "ColorStop": COLOR_STOPS1,  # can be more than 2
            "Extend": "pad",  # pad, repeat, reflect
        },
        "x0": x+50, # Offset into middle of pixel
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
        "x0": x+1500, # Offset into middle of pixel
        "y0": y+50,
        "r0": 1,
        "x1": x+1500,
        "y1": y+50,
        "r1": s+1,
    }
    return r1
    layers = [r1, r2]
    return (ot.PaintFormat.PaintColrLayers, layers)

def getPaintRadialGradient2(s, x, y):
    layers = []
    r1 = {
        "Format": ot.PaintFormat.PaintRadialGradient,
        "ColorLine": {
            "ColorStop": COLOR_STOPS2,  # can be more than 2
            #"ColorStop": ((0.0, color1), (0.25, color2), (0.5, color3), (0.75, color4), (1, color5)),  # can be more than 2
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
    return layers[0]
    return (ot.PaintFormat.PaintColrLayers, layers)

def pixelPositions(f, gName):
    positions = []
    for component in f[gName].components:
        positions.append(tuple(component.transformation[-2:]))
    return tuple(positions)

designSpaceSources = []

values = dict(S1min=SMIN, S1def=SDEF, S1max=SMAX, X1min=LMIN, X1def=LDEF, X1max=LMAX, Y1min=LMIN, Y1def=LDEF, Y1max=LMAX,
              S2min=SMIN, S2def=SDEF, S2max=SMAX, X2min=LMIN, X2def=LDEF, X2max=LMAX, Y2min=LMIN, Y2def=LDEF, Y2max=LMAX)
for s1 in ('S1min', 'S1def', 'S1max'):
    for x1 in ('X1min', 'X1def', 'X1max'):
        for y1 in ('Y1min', 'Y1def', 'Y1max'):
            for s2 in ('S2min', 'S2def', 'S2max'):
                for x2 in ('X2min', 'X2def', 'X2max'):
                    for y2 in ('Y2min', 'Y2def', 'Y2max'):
                        key = s1 + x1 + y1 + s2 + x2 + y2
                        if s1 == s2 == SDEF and x1 == y1 == x2 == y2 == LDEF:
                            info = '\t\t\t<info copy="1"/>\n'
                        else:
                            info = ''
                        ufoPath = DST_PATH % (s1, x1, y1, s2, x2, y2)
                        designSpaceSources.append(SRC % dict(s1=values[s1], x1=values[x1], y1=values[y1], s2=values[s2], x2=values[x2], y2=values[y2], ufoPath=ufoPath, info=info ))
                        print('===', key)

                        f = fonts[key]
                        pixelLayer1 = getPaintRadialGradient1(values[s1], values[x1], values[y1])
                        pixelLayer2 = getPaintRadialGradient2(values[s2], values[x2], values[y2])

                        pixelLayer1x = getPaintRadialGradient1(values[s1], values[x1]+450, values[y1]+100)
                        pixelLayer2x = getPaintRadialGradient2(values[s2], values[x2]+450, values[y2]+100)
                        #circleLayer2 = getPaintCircle(values[s], values[x]+20, values[y]+20, color2)
                        colorGlyphs = {}
                        for glyphName in ('a', 'b', 'c', 'e', 'space', 'canvas'): #sorted(f.keys()):
                            #circleLayer1 = getPaintCircle(glyphName, values[s2], values[x2], values[y2], white)
                            if glyphName == 'canvas':
                                colorGlyphs[glyphName] = buildPixelGlyph('_canvas', pixelPositions(f, glyphName), pixelLayer1x, pixelLayer2x)
                            else:
                                colorGlyphs[glyphName] = buildPixelGlyph('px', pixelPositions(f, glyphName), pixelLayer1, pixelLayer2)

                        f.lib = {}
                        f.lib[COLOR_PALETTES_KEY] = palettes
                        f.lib[COLOR_LAYERS_KEY] = colorGlyphs

                        f.save()

designSpace = DS % dict(sources='\n'.join(designSpaceSources))

dsFile = codecs.open('BitcountMono_Double2-TEST.designspace', 'w', encoding='utf-8')
dsFile.write(designSpace)
dsFile.close()

os.system('fontmake -m BitcountMono_Double2-TEST.designspace -o variable')

print('--- Done')

