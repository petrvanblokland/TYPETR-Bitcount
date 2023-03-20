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

DS = """<?xml version='1.0' encoding='utf-8'?>
<designspace format="3">
    <axes>
        <axis default="50" maximum="500" minimum="50" name="Weight" tag="wght"/>
        <axis default="0" maximum="500" minimum="-500" name="ColorX" tag="COLX"/>
        <axis default="0" maximum="500" minimum="-500" name="ColorY" tag="COLY"/>
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
            <dimension name="ColorX" xvalue="%(x)d"/>
            <dimension name="ColorY" xvalue="%(y)d"/>
        </location>
        %(info)s
    </source>
"""

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

fonts = {}
ufoNameTemplates = dict(S='Bitcount_Mono_Double_S.ufo', Smax='Bitcount_Mono_Double_Smax.ufo')
for s in ('S', 'Smax'):
    for x in ('Xmin', 'X', 'Xmax'):
        for y in ('Ymin', 'Y', 'Ymax'):
            key = s + x + y
            srcPath = 'ufo-src/' + ufoNameTemplates[s]
            ufoPath = 'ufo/' + ufoNameTemplates[s].replace('.ufo', '_%s_%s.ufo' % (x, y))
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

color1 = 0  # palette index
color2 = 1  # palette index
color3 = 2  # palette index
color4 = 3  # palette index
color5 = 4  # palette index
color6 = 5  # palette index
color7 = 6  # palette index

def getPaintRadialGradient(s, x, y):
    return {
        "Format": ot.PaintFormat.PaintRadialGradient,
        "ColorLine": {
            "ColorStop": ((0.0, color1), (0.15, color2), (0.3, color3), (0.45, color4), (0.6, color5), (0.65, color6), (1, color7)),  # can be more than 2
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


def pixelPositions(f, gName):
    positions = []
    for component in f[gName].components:
        positions.append(tuple(component.transformation[-2:]))
    return tuple(positions)

designSpaceSources = []

print(fonts)
values = dict(S=50, Smax=500, Xmin=-500, X=0, Xmax=500, Ymin=-500, Y=0, Ymax=500)
for s in ('S', 'Smax'):
    for x in ('Xmin', 'X', 'Xmax'):
        for y in ('Ymin', 'Y', 'Ymax'):
            key = s + x + y
            if s == 0 and x == y == 0:
                info = '\t\t\t<info copy="1"/>\n'
            else:
                info = ''
            ufoPath = 'ufo/' + ufoNameTemplates[s].replace('.ufo', '_%s_%s.ufo' % (x, y))
            designSpaceSources.append(SRC % dict(s=values[s], x=values[x], y=values[y], ufoPath=ufoPath, info=info ))
            print('===', key)

            f = fonts[key]
            pixelGradient = getPaintRadialGradient(values[s], values[x], values[y])
            colorGlyphs = {}
            for glyphName in ('a', 'b', 'c', 'space'): #sorted(f.keys()):

                colorGlyphs[glyphName] = buildPixelGlyph("px", pixelPositions(f, glyphName), pixelGradient)

            #print(colorGlyphs)
            f.lib = {}
            f.lib[COLOR_PALETTES_KEY] = palettes
            f.lib[COLOR_LAYERS_KEY] = colorGlyphs
            #print(f.lib)

            f.save()

designSpace = DS % dict(sources='\n'.join(designSpaceSources))

dsFile = codecs.open('BitcountMono_Double2-TEST.designspace', 'w', encoding='utf-8')
dsFile.write(designSpace)
dsFile.close()

os.system('fontmake -m BitcountMono_Double2-TEST.designspace -o variable')

print('--- Done')

