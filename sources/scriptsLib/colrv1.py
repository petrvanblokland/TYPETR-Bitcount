# -*- coding: UTF-8 -*-
#
#   Build a variants of Bitcount VF/TTF/OTF from here.
#   Optionally add COLRv1 pixels into the UFO.
#
#   https://github.com/googlefonts/colr-gradients-spec
#
import sys
from collections import defaultdict

sys.path.append(".")
from scriptsLib import SMIN, SMAX, LMIN, LMAX
from scriptsLib import slnt_AXIS, OPEN_AXIS, wght_AXIS, SHPE_AXIS


COLORS = [
    "#FFFFFFFF",  # (1, 1, 1, 1)
    "#FF00FF80",  # color1 = (1, 0, 1, 0.5)
    "#FFFFFF80",  # color2 = (1, 1, 1, 0.5)
    "#0033FF80",  # color3 = (0, 0.2, 1, 0.5)
    "#FF330080",  # color4 = (1, 0.2, 0, 0.5)
    "#00FF0080",  # color5 = (0, 1, 0, 0.5),
    "#00FFFF80",  # color6 = (0, 1, 1, 0.5),
    "#00000080",  # color7 = (0, 0, 0, 0.5),
    "#0033FFFF",  # color10 = (0, 0.2, 1, 1),
    "#FF3300FF",  # color11 = (1, 0.2, 0, 1),
    "#FF00FFFF",  # color12= (1, 0, 1, 1),
    "#00FF00FF",  # color13= (0, 1, 0, 1),
    "#FFFFFFFF",  # color14= (1, 1, 1, 1),
    "#000000FF",  # color15=(0, 0, 0, 1),
    "#00FFFFFF",  # color16=(0, 1, 1, 1),
]

COLOR_STOPS1 = ColorLine({ix / len(COLORS): stop for ix, stop in enumerate(COLORS)})
COLOR_STOPS2 = ColorLine(
    {ix / len(COLORS): stop for ix, stop in enumerate(reversed(COLORS))}
)

pt1 = (
    {
        (("LR1X", LMIN),): LMIN + 50,
        (("LR1X", LMAX),): LMAX + 50,
    },
    {
        (("LR1Y", LMIN),): LMIN + 50,
        (("LR1Y", LMAX),): LMAX + 50,
    },
)
pt2 = (
    {
        (("LR2X", LMIN),): LMIN + 50,
        (("LR2X", LMAX),): LMAX + 50,
    },
    {
        (("LR2Y", LMIN),): LMIN + 50,
        (("LR2Y", LMAX),): LMAX + 50,
    },
)
LR1S = {(("LR1S", SMIN),): 1, (("LR1S", SMAX),): SMAX + 1}
LR2S = {(("LR2S", SMIN),): 1, (("LR2S", SMAX),): SMAX + 1}

rg1 = PaintRadialGradient(pt1, 1, pt1, LR1S, COLOR_STOPS1)

rg2 = PaintRadialGradient(pt2, 1, pt2, LR2S, COLOR_STOPS2)


pt1x = (
    {
        (("LR1X", LMIN),): LMIN + 50 + 450,
        (("LR1X", LMAX),): LMAX + 50 + 450,
    },
    {
        (("LR1Y", LMIN),): LMIN + 50 + 100,
        (("LR1Y", LMAX),): LMAX + 50 + 100,
    },
)
pt2x = (
    {
        (("LR2X", LMIN),): LMIN + 50 + 450,
        (("LR2X", LMAX),): LMAX + 50 + 450,
    },
    {
        (("LR2Y", LMIN),): LMIN + 50 + 100,
        (("LR2Y", LMAX),): LMAX + 50 + 100,
    },
)

rg1x = PaintRadialGradient(pt1x, 1, pt1x, LR1S, COLOR_STOPS1)
rg2x = PaintRadialGradient(pt2x, 1, pt2x, LR2S, COLOR_STOPS2)


def buildPixelGlyph(pixelGlyphName, pixelPositions, layer1, layer2):
    layers = []
    for x, y in pixelPositions:
        layers.append(PaintTranslate(x, y, PaintGlyph(pixelGlyphName, layer1)))
        layers.append(PaintTranslate(x, y, PaintGlyph(pixelGlyphName, layer2)))
    return PaintColrLayers(layers)


# Now admittedly this is complicated; we need to make a variable
# translate, specifying the pixel positions at all the points in 
# the designspace that we care about (using the original B&W axes)
def pixelPositions(f, gName):
    positions_x = defaultdict(dict)
    positions_y = defaultdict(dict)
    for slnt_ax in [0, 1000]:
        # slnt is actually the only one that moves the pixels
        location = {"slnt": slnt_ax}
        gs = font.getGlyphSet(location=location)
        glyph = gs[gName]._getGlyphInstance()
        if not hasattr(glyph, "components"):
            return []
        for ix, component in enumerate(glyph.components):
            positions_x[ix][tuple(location.items())] = component.x
            positions_y[ix][tuple(location.items())] = component.y
    return list(zip(list(positions_x.values()), list(positions_y.values())))


for glyphName in font.getGlyphOrder():
    if glyphName == "canvas":
        glyphs[glyphName] = buildPixelGlyph(
            "_canvas", pixelPositions(font, glyphName), rg1x, rg2x
        )
    else:
        glyphs[glyphName] = buildPixelGlyph(
            "px", pixelPositions(font, glyphName), rg1, rg2
        )

# I hate you, HVAR table, go away.
del font["HVAR"]
