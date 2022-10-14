from pprint import pprint
import random
import sys
from fontTools.ttLib import TTFont
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
    if len(layers) == 1:
        return layers[0]
    else:
        return (ot.PaintFormat.PaintColrLayers, layers)


def buildPixelGlyphFromColorGlyph(pixelGlyphName, pixelPositions):
    layers = []
    for x, y in pixelPositions:
        # Two nested Paints:
        # - PaintTranslate to move the pixel to the right place
        # - PaintColrGlyph to say which color glyph to be drawn
        layer = {
            "Format": ot.PaintFormat.PaintTranslate,
            "Paint": {
                "Format": ot.PaintFormat.PaintColrGlyph,
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


def buildPixelGlyphFromColorGlyphRandomRotation(pixelGlyphName, pixelPositions):
    layers = []
    for x, y in pixelPositions:
        # Three nested Paints:
        # - PaintTranslate to move the pixel to the right place
        # - PaintRotate to randomly rotate the pixel
        # - PaintColrGlyph to say which color glyph to be drawn
        layer = {
            "Format": ot.PaintFormat.PaintTranslate,
            "Paint": {
                "Format": ot.PaintFormat.PaintRotate,
                "Paint": {
                    "Format": ot.PaintFormat.PaintColrGlyph,
                    "Glyph": pixelGlyphName,
                },
                "angle": random.random() * 360,
            },
            "dx": x,
            "dy": y,
        }
        layers.append(layer)
    if len(layers) == 1:
        return layers[0]
    else:
        return (ot.PaintFormat.PaintColrLayers, layers)


def scaleTranslate(points, scale, dx, dy):
    return [(scale * x + dx, scale * y + dy) for x, y in points]


palettes = [
    [
        (1, 0.2, 0, 1),
        (0, 0.2, 1, 0.3),
    ],
]

color1 = 0  # palette index
color2 = 1  # palette index


pixelGradient = {
    "Format": ot.PaintFormat.PaintLinearGradient,
    "ColorLine": {
        "ColorStop": [(0.0, color1), (1.0, color2)],  # can be more than 2
        "Extend": "pad",  # pad, repeat, reflect
    },
    "x0": -50,
    "y0": -50,
    "x1": 50,
    "y1": 50,
    "x2": -100,  # x2, y2 determine the shear of the gradient, relative to (x0, y0), (x1, y1)
    "y2": 0,
}

def add_colorv1(path):
    font = TTFont(path)
    font["CPAL"] = buildCPAL(palettes)

    glyphMap = font.getReverseGlyphMap()
    colorGlyphs = {}
    for gName in glyphMap.keys(): 
        g = font['glyf'][gName]
        pixelPositions = []
        if hasattr(g, 'components'):
            for component in g.components:
                pixelPositions.append((component.x, component.y))
            pixelPositions.sort()
            colorGlyphs[gName] = buildPixelGlyph("px", pixelPositions, pixelGradient)

    font["COLR"] = buildCOLR(
        colorGlyphs,
        glyphMap=glyphMap,
        clipBoxes={},
    )

    font.save(path)


if __name__ == "__main__":
    path = '../variable_ttf/BitcountMono_Double4-VF.ttf'
    add_colorv1(path)
    print('Done')
