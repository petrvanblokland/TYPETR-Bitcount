# -*- coding: UTF-8 -*-
# This is a COLRv1 paint definition file for paintcompiler
import sys
from collections import defaultdict

sys.path.append(".")
from scriptsLib import SMIN, SMAX, LMIN, LMAX


COLORS = [
    "#FFFFFFFF",  # white
    "#808080FF",  # color16=grey
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
]


# Define our two colour lines for the radial gradient.
# Colour line one is just all the colours spaced out linearly.
COLOR_STOPS1 = ColorLine({ix / len(COLORS): stop for ix, stop in enumerate(COLORS)})

# Colour line two is white plus all the colours in reverse.
COLORS2 = [COLORS[0]] + COLORS[-1:0:-1]
COLOR_STOPS2 = ColorLine({ix / len(COLORS2): stop for ix, stop in enumerate(COLORS2)})

# Define a variable point. This point will be the origin of the radial
# gradient for layer 1. Its X coordinate varies based on the value of
# the LR1X axis, and similarly for the Y coordinate.
pt1 = (
    {
        # We set the value of the X coordinate at the minimum and
        # maximum values of the LR1X axis, and let the coordinate be
        # interpolated at other locations.
        (("LR1X", LMIN),): LMIN + 50,
        (("LR1X", LMAX),): LMAX + 50,
    },
    {
        (("LR1Y", LMIN),): LMIN + 50,
        (("LR1Y", LMAX),): LMAX + 50,
    },
)
# Now exactly the same but for the origin of the radial gradient for
# layer 2, based on LR2X/LR2Y.
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
# Now we want to define how the radius of the second "circle" in
# the radial gradient varies; at minimum value of LR1S/LR2S it is 1,
# and at the maximum value is it is SMAX+1.
LR1S = {(("LR1S", SMIN),): 1, (("LR1S", SMAX),): SMAX + 1}
LR2S = {(("LR2S", SMIN),): 1, (("LR2S", SMAX),): SMAX + 1}

# So now we can define these radial gradients to be used for the pixels.
rg1 = PaintRadialGradient(pt1, 1, pt1, LR1S, COLOR_STOPS1)
rg2 = PaintRadialGradient(pt2, 1, pt2, LR2S, COLOR_STOPS2)

# This is the same as the above, but for the canvas glyph.
pt1x = (
    {
        (("LR1X", LMIN),): LMIN + 500,
        (("LR1X", LMAX),): LMAX + 500,
    },
    {
        (("LR1Y", LMIN),): LMIN + 50 + 100,
        (("LR1Y", LMAX),): LMAX + 50 + 100,
    },
)
pt2x = (
    {
        (("LR2X", LMIN),): LMIN + 500,
        (("LR2X", LMAX),): LMAX + 500,
    },
    {
        (("LR2Y", LMIN),): LMIN + 50 + 100,
        (("LR2Y", LMAX),): LMAX + 50 + 100,
    },
)

rg1x = PaintRadialGradient(pt1x, 1, pt1x, LR1S, COLOR_STOPS1)
rg2x = PaintRadialGradient(pt2x, 1, pt2x, LR2S, COLOR_STOPS2)


# To build a pixel glyph, we paint each pixel twice, once with each
# layer. We might want to change this to clever compositing/blending
# later, depending on how things look when we have the layers working
# correctly. So this function returns a paint tree with a PaintColrLayers
# operation, containing two layers for each pixel.
def buildPixelGlyph(pixelGlyphName, pixelPositions, layer1, layer2):
    layers = []
    for x, y in pixelPositions:
        layers.append(PaintTranslate(x, y, PaintGlyph(pixelGlyphName, layer1)))
        layers.append(PaintTranslate(x, y, PaintGlyph(pixelGlyphName, layer2)))
    return PaintColrLayers(layers)


# Now admittedly this is complicated, because the "pixel position"
# differs across the design space. To make this work, the returned
# coordinates will actually be "variable points" like those we
# created above (for the centers of our radial gradients), specifying
# how each pixel moves in the designspace.
# Thankfully, the pixel only differs when the "slnt" axis is applied
# (at this point - I think we might need to do the same for the width
# axis in compressed fonts), so we gather each pixel position at the
# extremes of that axis, and turn them into a dictionary.
def pixelPositions(f, gName):
    positions_x = defaultdict(dict)
    positions_y = defaultdict(dict)
    for slnt_ax in [0, 1000]:
        location = {"slnt": slnt_ax}
        # We are working on the (binary) TTFont, so we have to do
        # horrible magic to find the component locations.
        gs = font.getGlyphSet(location=location)
        glyph = gs[gName]._getGlyphInstance()
        if not hasattr(glyph, "components"):
            return []
        for ix, component in enumerate(glyph.components):
            positions_x[ix][tuple(location.items())] = component.x
            positions_y[ix][tuple(location.items())] = component.y
    return list(zip(list(positions_x.values()), list(positions_y.values())))


# OK, we are finally ready to create the paint trees for each glyph.
# We do this by adding an entry into the "glyphs" dictionary mapping
# the glyph name to the paint tree.
for glyphName in font.getGlyphOrder():
    if glyphName == "canvas":
        glyphs[glyphName] = buildPixelGlyph(
            "_canvas", pixelPositions(font, glyphName), rg1x, rg2x
        )
    else:
        glyphs[glyphName] = buildPixelGlyph(
            "px", pixelPositions(font, glyphName), rg1, rg2
        )

# We have a problem; we have added six new axes to the font at this point,
# and while the gvar table can cope with that because it gets rebuilt when
# the font is saved, the HVAR table is not fully decompiled by fontTools,
# so it still refers to four axes, which makes it invalid when you try
# to save the font. Thankfully, HVAR isn't very necessary anyway, so we
# just get rid of it.
del font["HVAR"]
