# -*- coding: UTF-8 -*-
# This is a COLRv1 paint definition file for paintcompiler
import sys
from collections import defaultdict

sys.path.append(".")
from scriptsLib import SMIN, SDEF, SMAX, LDEF, LMIN, LMAX, POST_FIX

P = 100
G = 7*P # Layer grid size, so we can divide into 7 spectrum colors
LS = 1 # Layer scaling of elements
SLOPE = 14 # Horizontal slant offset per 100 vertical units 

if font['post'].italicAngle:
    slope = SLOPE
    so1 = SLOPE * 7
    so2 = SLOPE * 7 * 2 
else:
    slope = so2 = so1 = 0

# String additions to the colors, defining standard level of opacity
OPAQUE = "FF"
TRANSPARANT = "AA"
FAINT = "80"

###
# Colors and gradients
###

BLACK = "#000000"
GREY = "#808080"
LIGHT_GREY = "#EEEEEE"
WHITE = "#FFFFFF"

# 7 Spectrum colors, double red
RED = "#FF0000"  # Red=(1, 0, 0, ?)
ORANGE = "#FFAB00"
YELLOW = "#FFFF00"
GREEN = "#70E000"
BLUE = "#01A6F0"
PURPLE = "#C700FF"
#RED = "#FF0000"  # Red=(1, 0, 0, ?)

DARK_RED = ""
DARK_ORANGE = ""
DARK_YELLOW = ""
DARK_GREEN = ""
DARK_BLUE = "005080"
DARK_PURPLE = ""

# Interesting range of colors for the gradient circles
CIRCLE_COLORS = [
    WHITE + OPAQUE,  # white
    GREY + OPAQUE,  # color16=grey
    "#FF00FF80",  # color1 = (1, 0, 1, 0.5)
    "#FFFFFF80",  # color2 = (1, 1, 1, 0.5)
    "#0033FF80",  # color3 = (0, 0.2, 1, 0.5)
    "#FF330080",  # color4 = (1, 0.2, 0, 0.5)
    "#00FF0080",  # color5 = (0, 1, 0, 0.5),
    "#00FFFF80",  # color6 = (0, 1, 1, 0.5),
    BLACK + OPAQUE,  # color7 = (0, 0, 0, 0.5),
    "#0033FFFF",  # color10 = (0, 0.2, 1, 1),
    "#FF3300FF",  # color11 = (1, 0.2, 0, 1),
    "#FF00FFFF",  # color12= (1, 0, 1, 1),
    "#00FF00FF",  # color13= (0, 1, 0, 1),
    WHITE + OPAQUE,  # color14= (1, 1, 1, 1),
    BLACK + OPAQUE,  # color15=(0, 0, 0, 1),
]


# Define our two colour lines for the radial gradient.
# Colour line one is just all the colours spaced out linearly.
COLOR_LINE1 = {ix / len(CIRCLE_COLORS): stop for ix, stop in enumerate(CIRCLE_COLORS)}
COLOR_STOPS1 = ColorLine(COLOR_LINE1)

# Colour line two is white plus all the colours in reverse.
CIRCLE_COLORS2 = [CIRCLE_COLORS[0]] + CIRCLE_COLORS[-1:0:-1]
COLOR_LINE2 = {ix / len(CIRCLE_COLORS): stop for ix, stop in enumerate(CIRCLE_COLORS2)}
COLOR_STOPS2 = ColorLine({ix / len(CIRCLE_COLORS2): stop for ix, stop in enumerate(CIRCLE_COLORS2)})

BLUE_RANGE = ColorLine({0: BLUE + OPAQUE, 1: YELLOW + OPAQUE})

SPECTRUM = ColorLine({
    0: RED + OPAQUE, 
    1/6: ORANGE + OPAQUE, 
    2/6: YELLOW + OPAQUE, 
    3/6: GREEN + OPAQUE,  
    4/6: BLUE + OPAQUE, 
    5/6: PURPLE + OPAQUE,
    1: RED + OPAQUE,
})

SPECTRUM_TRANSPARANT = ColorLine({
    0: RED + TRANSPARANT, 
    1/6: ORANGE + TRANSPARANT, 
    2/6: YELLOW + TRANSPARANT, 
    3/6: GREEN + TRANSPARANT,  
    4/6: BLUE + TRANSPARANT, 
    5/6: PURPLE + TRANSPARANT,
    1: RED + TRANSPARANT, 
})

###
# Elements and layers
###

# The 3 layers are really large areas that can be used to crop pixels shapes from.

## I'm going to define some "elements" here, some of which are just
## simple glyphs, and some are combinations of glyphs. We expect each
## element to be 100x100 and to be placed at the origin. We'll translate
## them to their correct place on the "layer" later.
## These elements come from the UFO Bitcount-LayerElements but when we
## copy them into the current font, we add an POST_FIX (el_) to the start of their
## names.

# "hstripes" is an element made up of a 7 stripes in spectrum color, with red on top and bottom.

hstripes = PaintColrLayers(
    [
        PaintTranslate(
            0, -G/2 + P/2, PaintScale(LS, PaintGlyph(POST_FIX + "hstripe", PaintSolid(RED + OPAQUE)))
        ),
        PaintTranslate(
            slope, -G/2 + P/2 + P, PaintScale(LS, PaintGlyph(POST_FIX + "hstripe", PaintSolid(ORANGE + OPAQUE)))
        ),
        PaintTranslate(
            2*slope, -G/2 + P/2 + 2*P, PaintScale(LS, PaintGlyph(POST_FIX + "hstripe", PaintSolid(YELLOW + OPAQUE)))
        ),
        PaintTranslate(
            3*slope, -G/2 + P/2 + 3*P, PaintScale(LS, PaintGlyph(POST_FIX + "hstripe", PaintSolid(GREEN + OPAQUE)))
        ),
        PaintTranslate(
            4*slope, -G/2 + P/2 + 4*P, PaintScale(LS, PaintGlyph(POST_FIX + "hstripe", PaintSolid(BLUE + OPAQUE)))
        ),
        PaintTranslate(
            5*slope, -G/2 + P/2 + 5*P, PaintScale(LS, PaintGlyph(POST_FIX + "hstripe", PaintSolid(PURPLE + OPAQUE)))
        ),
        PaintTranslate(
            6*slope, -G/2 + P/2 + 6*P, PaintScale(LS, PaintGlyph(POST_FIX + "hstripe", PaintSolid(RED + OPAQUE)))
        ),
    ]
)
hstripes_opaque = PaintColrLayers(
    [
        PaintTranslate(
            0, -G/2 + P/2, PaintScale(LS, PaintGlyph(POST_FIX + "hstripe", PaintSolid(RED + TRANSPARANT)))
        ),
        PaintTranslate(
            slope, -G/2 + P/2 + P, PaintScale(LS, PaintGlyph(POST_FIX + "hstripe", PaintSolid(ORANGE + TRANSPARANT)))
        ),
        PaintTranslate(
            2*slope, -G/2 + P/2 + 2*P, PaintScale(LS, PaintGlyph(POST_FIX + "hstripe", PaintSolid(YELLOW + TRANSPARANT)))
        ),
        PaintTranslate(
            3*slope, -G/2 + P/2 + 3*P, PaintScale(LS, PaintGlyph(POST_FIX + "hstripe", PaintSolid(GREEN + TRANSPARANT)))
        ),
        PaintTranslate(
            4*slope, -G/2 + P/2 + 4*P, PaintScale(LS, PaintGlyph(POST_FIX + "hstripe", PaintSolid(BLUE + TRANSPARANT)))
        ),
        PaintTranslate(
            5*slope, -G/2 + P/2 + 5*P, PaintScale(LS, PaintGlyph(POST_FIX + "hstripe", PaintSolid(PURPLE + TRANSPARANT)))
        ),
        PaintTranslate(
            6*slope, -G/2 + P/2 + 6*P, PaintScale(LS, PaintGlyph(POST_FIX + "hstripe", PaintSolid(RED + TRANSPARANT)))
        ),
    ]
)
vstripes = PaintColrLayers(
    [
        PaintTranslate(
            -G/2 + P/2, 0, PaintScale(LS, PaintGlyph(POST_FIX + "vstripe", PaintSolid(RED + OPAQUE)))
        ),
        PaintTranslate(
            -G/2 + P/2 + P, 0, PaintScale(LS, PaintGlyph(POST_FIX + "vstripe", PaintSolid(ORANGE + OPAQUE)))
        ),
        PaintTranslate(
            -G/2 + P/2 + 2*P, 0, PaintScale(LS, PaintGlyph(POST_FIX + "vstripe", PaintSolid(YELLOW + OPAQUE)))
        ),
        PaintTranslate(
            -G/2 + P/2 + 3*P, 0, PaintScale(LS, PaintGlyph(POST_FIX + "vstripe", PaintSolid(GREEN + OPAQUE)))
        ),
        PaintTranslate(
            -G/2 + P/2 + 4*P, 0, PaintScale(LS, PaintGlyph(POST_FIX + "vstripe", PaintSolid(BLUE + OPAQUE)))
        ),
        PaintTranslate(
            -G/2 + P/2 + 5*P, 0, PaintScale(LS, PaintGlyph(POST_FIX + "vstripe", PaintSolid(PURPLE + OPAQUE)))
        ),
        PaintTranslate(
            -G/2 + P/2 + 6*P, 0, PaintScale(LS, PaintGlyph(POST_FIX + "vstripe", PaintSolid(RED + OPAQUE)))
        ),
    ]
)
vstripes_opaque = PaintColrLayers(
    [
        PaintTranslate(
            -G/2 + P/2, 0, PaintScale(LS, PaintGlyph(POST_FIX + "vstripe", PaintSolid(RED + TRANSPARANT)))
        ),
        PaintTranslate(
            -G/2 + P/2 + P, 0, PaintScale(LS, PaintGlyph(POST_FIX + "vstripe", PaintSolid(ORANGE + TRANSPARANT)))
        ),
        PaintTranslate(
            -G/2 + P/2 + 2*P, 0, PaintScale(LS, PaintGlyph(POST_FIX + "vstripe", PaintSolid(YELLOW + TRANSPARANT)))
        ),
        PaintTranslate(
            -G/2 + P/2 + 3*P, 0, PaintScale(LS, PaintGlyph(POST_FIX + "vstripe", PaintSolid(GREEN + TRANSPARANT)))
        ),
        PaintTranslate(
            -G/2 + P/2 + 4*P, 0, PaintScale(LS, PaintGlyph(POST_FIX + "vstripe", PaintSolid(BLUE + TRANSPARANT)))
        ),
        PaintTranslate(
            -G/2 + P/2 + 5*P, 0, PaintScale(LS, PaintGlyph(POST_FIX + "vstripe", PaintSolid(PURPLE + TRANSPARANT)))
        ),
        PaintTranslate(
            -G/2 + P/2 + 6*P, 0, PaintScale(LS, PaintGlyph(POST_FIX + "vstripe", PaintSolid(RED + TRANSPARANT)))
        ),
    ]
)

# boxes is four boxes; the element is 100x100 so we'll scale it down,
# then reposition four copies of it.
boxes = PaintColrLayers(
    [
        PaintTranslate(
            0, G/2, PaintScale(LS, PaintGlyph(POST_FIX + "square", PaintSolid("#F34F1CFF")))
        ),
        PaintTranslate(
            G/2, G/2, PaintScale(LS, PaintGlyph(POST_FIX + "square", PaintSolid("#7FBC00FF")))
        ),
        PaintTranslate(
            0, 0, PaintScale(LS, PaintGlyph(POST_FIX + "square", PaintSolid("#01A6F0FF")))
        ),
        PaintTranslate(
            G/2, 0, PaintScale(LS, PaintGlyph(POST_FIX + "square", PaintSolid("#FFBA01FF")))
        ),
        # Oh look it's the Microsoft logo.
    ]
)

balls = PaintColrLayers(
    [
        PaintTranslate(
            0, G/2, PaintScale(LS, PaintGlyph(POST_FIX + "circle", PaintSolid("#F34F1CFF")))
        ),
        PaintTranslate(
            G/2, G/2, PaintScale(LS, PaintGlyph(POST_FIX + "circle", PaintSolid("#7FBC00FF")))
        ),
        PaintTranslate(
            0, 0, PaintScale(LS, PaintGlyph(POST_FIX + "circle", PaintSolid("#01A6F0FF")))
        ),
        PaintTranslate(
            G/2, 0, PaintScale(LS, PaintGlyph(POST_FIX + "circle", PaintSolid("#FFBA01FF")))
        ),
    ]
)

zigzag = PaintScale(
    LS,
    PaintGlyph(
        POST_FIX + "zigzag",
        PaintLinearGradient(
            (0, 0),
            (G/2, G/2),
            (G, G),
            SPECTRUM,
        ),
    ),
)

vzigzag = PaintScale(
    LS,
    PaintGlyph(
        POST_FIX + "vzigzag",
        PaintLinearGradient(
            (0, 0),
            (G/2, G/2),
            (G, G),
            SPECTRUM_TRANSPARANT,
        ),
    ),
)

squares = PaintScale(
    LS,
    PaintGlyph(
        POST_FIX + "squares",
        PaintRadialGradient((0, 0), 1, (0, 0), G/2, COLOR_STOPS1),
    ),
)

# Full colored squares
squareLargeBlue = PaintColrLayers(
    [   
        PaintGlyph(POST_FIX + "square_large", PaintLinearGradient((0, 0), (G/2, G/2), (0, G/2), BLUE_RANGE)),
    ]
)
squareLargeRed = PaintColrLayers(
    [   
        PaintGlyph(POST_FIX + "square_large", PaintSolid(RED + OPAQUE)),
    ]
)
squareLargeYellow = PaintColrLayers(
    [   
        PaintGlyph(POST_FIX + "square_large", PaintSolid(YELLOW + OPAQUE)),
    ]
)
squareLargeGreen = PaintColrLayers(
    [   
        PaintGlyph(POST_FIX + "square_large", PaintSolid(GREEN + OPAQUE)),
    ]
)

chesssquare = PaintColrLayers(
    [   
        PaintGlyph(POST_FIX + "chesssquare", PaintRadialGradient((0, 0), 1, (0, 0), G/2, COLOR_STOPS1)),
    ]
)
squares2 = PaintColrLayers(
    [   
        PaintGlyph(POST_FIX + "squares2", PaintRadialGradient((0, 0), 1, (0, 0), G/2, COLOR_STOPS1)),
    ]
)
raster = PaintColrLayers(
    [   
        PaintGlyph(POST_FIX + "raster", PaintRadialGradient((0, 0), 1, (0, 0), G/2, COLOR_STOPS1)),
    ]
)
five = PaintColrLayers(
    [   
        PaintGlyph(POST_FIX + "five", PaintRadialGradient((0, 0), 1, (0, 0), G/2, COLOR_STOPS1)),
    ]
)
circles = PaintColrLayers(
    [   
        PaintGlyph(POST_FIX + "circles", PaintRadialGradient((0, 0), 1, (0, 0), G/2, COLOR_STOPS1)),
    ]
)
diamond = PaintColrLayers(
    [   
        PaintGlyph(POST_FIX + "diamond", PaintRadialGradient((0, 0), 1, (0, 0), G/2, COLOR_STOPS1)),
    ]
)
star = PaintColrLayers(
    [   
        PaintGlyph(POST_FIX + "star", PaintRadialGradient((0, 0), 1, (0, 0), G/2, COLOR_STOPS1)),
    ]
)

circleLargeBlue = PaintColrLayers(
    [   
        PaintGlyph(POST_FIX + "circle_large", PaintSolid(BLUE + OPAQUE)),
    ]
)
circleLargeRed = PaintColrLayers(
    [   
        PaintGlyph(POST_FIX + "circle_large", PaintSolid(RED + OPAQUE)),
    ]
)
circleLargeYellow = PaintColrLayers(
    [   
        PaintGlyph(POST_FIX + "circle_large", PaintSolid(YELLOW + OPAQUE)),
    ]
)
circleLargeGreen = PaintColrLayers(
    [   
        PaintGlyph(POST_FIX + "circle_large", PaintSolid(GREEN + OPAQUE)),
    ]
)

circle1 = PaintColrLayers(
    [   
        # Start with a gray square to fill the space a bit.
        PaintGlyph(POST_FIX + "square_large", PaintSolid(LIGHT_GREY + OPAQUE)),
        # The white circle as background.
        PaintGlyph(POST_FIX + "circle_large", PaintSolid(BLACK + OPAQUE)),
        PaintGlyph(POST_FIX + "circle_large", PaintRadialGradient((0, 0), 1, (0, 0), G/2, COLOR_STOPS1)),

    ]
)
circle2 = PaintGlyph(
   POST_FIX + "circle_large", PaintRadialGradient((0, 0), 1, (0, 0), G/2, COLOR_STOPS2)
)
#circle3 = PaintGlyph(
#    POST_FIX + "circle_large", PaintRadialGradient((0, 0), 1, (0, 0), G/2, COLOR_STOPS2)
#)

triangleLargeBlue = PaintColrLayers(
    [   
        PaintGlyph(POST_FIX + "triangle", PaintSolid(BLUE + OPAQUE)),
    ]
)
triangleLargeRed = PaintColrLayers(
    [   
        PaintGlyph(POST_FIX + "triangle", PaintSolid(RED + OPAQUE)),
    ]
)
triangleLargeYellow = PaintColrLayers(
    [   
        PaintGlyph(POST_FIX + "triangle", PaintSolid(YELLOW + OPAQUE)),
    ]
)
triangleLargeGreen = PaintColrLayers(
    [   
        PaintGlyph(POST_FIX + "triangle", PaintSolid(GREEN + OPAQUE)),
    ]
)

diamondLargeBlue = PaintColrLayers(
    [   
        PaintGlyph(POST_FIX + "diamond", PaintSolid(BLUE + OPAQUE)),
    ]
)
diamondLargeRed = PaintColrLayers(
    [   
        PaintGlyph(POST_FIX + "diamond", PaintSolid(RED + OPAQUE)),
    ]
)
diamondLargeYellow = PaintColrLayers(
    [   
        PaintGlyph(POST_FIX + "diamond", PaintSolid(YELLOW + OPAQUE)),
    ]
)
diamondLargeGreen = PaintColrLayers(
    [   
        PaintGlyph(POST_FIX + "diamond", PaintSolid(GREEN + OPAQUE)),
    ]
)

starLargeBlue = PaintColrLayers(
    [   
        PaintGlyph(POST_FIX + "star", PaintSolid(BLUE + OPAQUE)),
    ]
)
starLargeRed = PaintColrLayers(
    [   
        PaintGlyph(POST_FIX + "star", PaintSolid(RED + OPAQUE)),
    ]
)
starLargeYellow = PaintColrLayers(
    [   
        PaintGlyph(POST_FIX + "star", PaintSolid(YELLOW + OPAQUE)),
    ]
)
starLargeGreen = PaintColrLayers(
    [   
        PaintGlyph(POST_FIX + "star", PaintSolid(GREEN + OPAQUE)),
    ]
)

fiveCircles = PaintColrLayers(
    [   
        PaintGlyph(POST_FIX + "five_circles", PaintRadialGradient((0, 0), 1, (0, 0), G/2, COLOR_STOPS1)),
    ]
)
fiveCirclesBlue = PaintColrLayers(
    [   
        PaintGlyph(POST_FIX + "five_circles", PaintSolid(BLUE + OPAQUE)),
    ]
)
fiveCirclesRed = PaintColrLayers(
    [   
        PaintGlyph(POST_FIX + "five_circles", PaintSolid(RED + OPAQUE)),
    ]
)
fiveCirclesYellow = PaintColrLayers(
    [   
        PaintGlyph(POST_FIX + "five_circles", PaintSolid(YELLOW + OPAQUE)),
    ]
)
fiveCircleGreen = PaintColrLayers(
    [   
        PaintGlyph(POST_FIX + "five_circles", PaintSolid(GREEN + OPAQUE)),
    ]
)



linear_box1 = PaintGlyph(
    POST_FIX + "square_large", PaintLinearGradient((0, 0), (P/2, P/2), (G/2, G/2), COLOR_STOPS1)
)
linear_box2 = PaintGlyph(
    POST_FIX + "square_large", PaintLinearGradient((0, 0), (P/2, P/2), (G/2, G/2), COLOR_STOPS2)
)
#linear_box3 = PaintGlyph(
#    POST_FIX + "square_large", PaintLinearGradient((0, 0), (P/2, P/2), G/3, COLOR_STOPS1)
#)

concentric_boxes = PaintColrLayers(
    [
        PaintTransform(
            (1.0, 0.0, 0.0, 1.0, 0, 0), PaintGlyph(POST_FIX + "square", PaintSolid(CIRCLE_COLORS[1]))
        ),
        PaintTransform(
            (0.75, 0.0, 0.0, 0.75, 12, 12),
            PaintGlyph(POST_FIX + "square", PaintSolid(CIRCLE_COLORS[2])),
        ),
        PaintTransform(
            (0.5, 0.0, 0.0, 0.5, 25, 25), PaintGlyph(POST_FIX + "square", PaintSolid(CIRCLE_COLORS[3]))
        ),
        PaintTransform(
            (0.25, 0.0, 0.0, 0.25, 37, 37),
            PaintGlyph(POST_FIX + "square", PaintSolid(CIRCLE_COLORS[4])),
        ),
    ]
)

concentric_boxes2 = PaintColrLayers(
    [
        PaintTransform(
            (1.0, 0.0, 0.0, 1.0, 0, 0), PaintGlyph(POST_FIX + "square", PaintSolid(CIRCLE_COLORS[-1]))
        ),
        PaintTransform(
            (0.75, 0.0, 0.0, 0.75, 12, 12),
            PaintGlyph(POST_FIX + "square", PaintSolid(CIRCLE_COLORS[-2])),
        ),
        PaintTransform(
            (0.5, 0.0, 0.0, 0.5, 25, 25),
            PaintGlyph(POST_FIX + "square", PaintSolid(CIRCLE_COLORS[-3])),
        ),
        PaintTransform(
            (0.25, 0.0, 0.0, 0.25, 37, 37),
            PaintGlyph(POST_FIX + "square", PaintSolid(CIRCLE_COLORS[-4])),
        ),
    ]
)

# Now we make the background layer, by transforming those elements into place in a grid
layer1 = PaintColrLayers(
    [
        # Dark background for background layer

        PaintTranslate(2*G + P/2, -2*G + P/2, PaintGlyph(POST_FIX + "square_large", PaintSolid(BLACK + OPAQUE))),
        PaintTranslate(G + P/2, -2*G + P/2, PaintGlyph(POST_FIX + "square_large", PaintSolid(BLACK + OPAQUE))),
        PaintTranslate( + P/2, -2*G + P/2, PaintGlyph(POST_FIX + "square_large", PaintSolid(BLACK + OPAQUE))),
        PaintTranslate(-G + P/2, -2*G + P/2, PaintGlyph(POST_FIX + "square_large", PaintSolid(BLACK + OPAQUE))),
        PaintTranslate(-2*G + P/2, -2*G + P/2, PaintGlyph(POST_FIX + "square_large", PaintSolid(BLACK + OPAQUE))),

        PaintTranslate(2*G + P/2, -G + P/2, PaintGlyph(POST_FIX + "square_large", PaintSolid("#222222" + OPAQUE))),
        PaintTranslate(G + P/2, -G + P/2, PaintGlyph(POST_FIX + "square_large", PaintSolid("#222222" + OPAQUE))),
        PaintTranslate( + P/2, -G + P/2, PaintGlyph(POST_FIX + "square_large", PaintSolid("#222222" + OPAQUE))),
        PaintTranslate(-G + P/2, -G + P/2, PaintGlyph(POST_FIX + "square_large", PaintSolid("#222222" + OPAQUE))),
        PaintTranslate(-2*G + P/2, -G + P/2, PaintGlyph(POST_FIX + "square_large", PaintSolid("#222222" + OPAQUE))),

        PaintTranslate(2*G + P/2, P/2, PaintGlyph(POST_FIX + "square_large", PaintSolid("#444444" + OPAQUE))),
        PaintTranslate(G + P/2,  P/2, PaintGlyph(POST_FIX + "square_large", PaintSolid("#444444" + OPAQUE))),
        PaintTranslate(P/2 + P/2, P/2, PaintGlyph(POST_FIX + "square_large", PaintSolid("#444444" + OPAQUE))),
        PaintTranslate(-G + P/2, P/2, PaintGlyph(POST_FIX + "square_large", PaintSolid("#444444" + OPAQUE))),
        PaintTranslate(-2*G + P/2, P/2, PaintGlyph(POST_FIX + "square_large", PaintSolid("#444444" + OPAQUE))),

        PaintTranslate(2*G + P/2, G + P/2, PaintGlyph(POST_FIX + "square_large", PaintSolid("#666666" + OPAQUE))),
        PaintTranslate(G + P/2, G + P/2, PaintGlyph(POST_FIX + "square_large", PaintSolid("#666666" + OPAQUE))),
        PaintTranslate(P/2, G + P/2, PaintGlyph(POST_FIX + "square_large", PaintSolid("#666666" + OPAQUE))),
        PaintTranslate(-G + P/2, G + P/2, PaintGlyph(POST_FIX + "square_large", PaintSolid("#666666" + OPAQUE))),
        PaintTranslate(-2*G + P/2, G + P/2, PaintGlyph(POST_FIX + "square_large", PaintSolid("#666666" + OPAQUE))),

        PaintTranslate(2*G + P/2, 2*G + P/2, PaintGlyph(POST_FIX + "square_large", PaintSolid("#888888" + OPAQUE))),
        PaintTranslate(G + P/2, 2*G + P/2, PaintGlyph(POST_FIX + "square_large", PaintSolid("#888888" + OPAQUE))),
        PaintTranslate(P/2, 2*G + P/2, PaintGlyph(POST_FIX + "square_large", PaintSolid("#888888" + OPAQUE))),
        PaintTranslate(-G + P/2, 2*G + P/2, PaintGlyph(POST_FIX + "square_large", PaintSolid("#888888" + OPAQUE))),
        PaintTranslate(-2*G + P/2, 2*G + P/2, PaintGlyph(POST_FIX + "square_large", PaintSolid("#888888" + OPAQUE))),

        # Background cells

        PaintTranslate(-2*G + P/2 + so2, 2*G + P/2, squareLargeBlue),
        PaintTranslate(-G + P/2 + so2, 2*G + P/2, zigzag),
        PaintTranslate(P/2 + so2, 2*G + P/2, squares2),
        PaintTranslate(G + P/2 + so2, 2*G + P/2, vzigzag),
        PaintTranslate(2*G + P/2 + so2, 2*G + P/2, squareLargeRed),

        PaintTranslate(-2*G + P/2 + so1, G + P/2, raster),
        PaintTranslate(-G + P/2 + so1, G + P/2, diamond),
        PaintTranslate(P/2 + so1, G + P/2, chesssquare),
        PaintTranslate(G + P/2 + so1, G + P/2, circles),
        PaintTranslate(2*G + P/2 + so1, G + P/2, raster),

        PaintTranslate(-2*G + P/2, P/2, circle1),
        PaintTranslate(-G + P/2, P/2, circles),
        PaintTranslate(P/2, P/2, fiveCircles),
        PaintTranslate(G + P/2, P/2, diamond),
        PaintTranslate(2*G + P/2, P/2, star),
        
        PaintTranslate(-2*G + P/2 - so1, -G + P/2, circles),
        PaintTranslate(-G + P/2 - so1, -G + P/2, raster),
        PaintTranslate(P/2 - so1, -G + P/2, star),
        PaintTranslate(G + P/2 - so1, -G + P/2, chesssquare),
        PaintTranslate(2*G + P/2 - so1, -G + P/2, squares),

        PaintTranslate(-2*G + P/2 - so2, -2*G + P/2, squareLargeYellow),
        PaintTranslate(-G + P/2 - so2, -2*G + P/2, hstripes),
        PaintTranslate(P/2 - so2, -2*G + P/2, raster),
        PaintTranslate(G + P/2 - so2, -2*G + P/2, vstripes),
        PaintTranslate(2*G + P/2 - so2, -2*G + P/2, squareLargeGreen),
    ]
)

# The layer now gets shifted and scaled based on the value of the
# BG-X/BG-Y/BG-S coords
scale_factor1 = {
    (("BG-S", SMIN),): 0.85, # Smallest scale of the background, ensures that there never will be all white pixels
    (("BG-S", SDEF),): 1, 
    (("BG-S", SMAX),): 10, # Arbitrary enlargement factor.
}
# Position of the pixels in normal glyphs
x_pixel1 = {
    (("BG-X", LMIN),): - 2 * G,
    (("BG-X", LDEF),): 0,
    (("BG-X", LMAX),): 2 * G,
}
y_pixel1 = {
    (("BG-Y", LMIN),): - 2 * G,
    (("BG-Y", LDEF),): 0,
    (("BG-Y", LMAX),): 2 * G,
}
# Position of the pixels in the /canvas glyph
x_canvas1 = {
    (("BG-X", LMIN),): 500 - P/2 - 2 * G,
    (("BG-X", LDEF),): 500 - P/2,
    (("BG-X", LMAX),): 500 - P/2 + 2 * G,
}
y_canvas1 = {
    (("BG-Y", LMIN),): P - 2 * G,
    (("BG-Y", LDEF),): P,
    (("BG-Y", LMAX),): P + 2 * G,
}

layer1_pixel = PaintTranslate(
    x_pixel1, y_pixel1, PaintTransform((scale_factor1, 0, 0, scale_factor1, 0, 0), layer1)
)
layer1_canvas = PaintTranslate(
    x_canvas1, y_canvas1, PaintTransform((scale_factor1, 0, 0, scale_factor1, 0, 0), layer1)
)

# Same deal for foreground layer
# And the slant offset to the X, in case the font is slanted.
layer2 = PaintColrLayers(
    [
        PaintTranslate(-2*G + P/2 + so2, 2*G + P/2, squareLargeBlue),
        PaintTranslate(-G + P/2 + so2, 2*G + P/2, circleLargeRed),
        PaintTranslate(P/2 + so2, 2*G + P/2, fiveCircles),
        PaintTranslate(G + P/2 + so2, 2*G + P/2, circleLargeBlue),
        PaintTranslate(2*G + P/2 + so2, 2*G + P/2, squareLargeRed),

        PaintTranslate(-2*G + P/2 + so1, G + P/2, triangleLargeYellow),
        PaintTranslate(-G + P/2 + so1, G + P/2, vstripes_opaque),
        PaintTranslate(P/2 + so1, G + P/2, chesssquare),
        PaintTranslate(G + P/2 + so1, G + P/2, hstripes_opaque),
        PaintTranslate(2*G + P/2 + so1, G + P/2, triangleLargeGreen),

        PaintTranslate(-2*G + P/2, P/2, fiveCirclesBlue),
        PaintTranslate(-G + P/2, P/2, diamondLargeBlue),
        PaintTranslate(P/2, P/2, circle2),
        PaintTranslate(G + P/2, P/2, starLargeRed),
        PaintTranslate(2*G + P/2, P/2, fiveCirclesRed),
        
        PaintTranslate(-2*G + P/2 - so1, -G + P/2, triangleLargeBlue),
        PaintTranslate(-G + P/2 - so1, -G + P/2, vzigzag),
        PaintTranslate(P/2 - so1, -G + P/2, chesssquare),
        PaintTranslate(G + P/2 - so1, -G + P/2, zigzag),
        PaintTranslate(2*G + P/2 - so1, -G + P/2, triangleLargeRed),

        PaintTranslate(-2*G + P/2 - so2, -2*G + P/2, squareLargeYellow),
        PaintTranslate(-G + P/2 - so2, -2*G + P/2, circleLargeGreen),
        PaintTranslate(P/2 - so2, -2*G + P/2, raster),
        PaintTranslate(G + P/2 - so2, -2*G + P/2, circleLargeYellow),
        PaintTranslate(2*G + P/2 - so2, -2*G + P/2, squareLargeGreen),
    ]
)
scale_factor2 = {
    (("FG-S", SMIN),): 0, # Allow foreground layer scaling to 0
    (("FG-S", SDEF),): 0.5, # Default foreground layer is 100% of pixel (100 Em-units)
    (("FG-S", SMAX),): 10, # Arbitrary enlargement scale
}
# Position of the pixels in normal glyphs
x_pixel2 = {
    (("FG-X", LMIN),): -2 * G,
    (("FG-X", LDEF),): 0,
    (("FG-X", LMAX),): 2 * G,
}
y_pixel2 = {
    (("FG-Y", LMIN),): -2 * G,
    (("FG-Y", LDEF),): 0,
    (("FG-Y", LMAX),): 2 * G,
}
# Position of the pixels in the /canvas glyph
x_canvas2 = {
    (("FG-X", LMIN),): 500 - P/2 - 2 * G,
    (("FG-X", LDEF),): 500 - P/2,
    (("FG-X", LMAX),): 500 - P/2 + 2 * G,
}
y_canvas2 = {
    (("FG-Y", LMIN),): P - 2 * G,
    (("FG-Y", LDEF),): P,
    (("FG-Y", LMAX),): P + 2 * G
}

# Background
layer2_pixel = PaintTranslate(
    x_pixel2, y_pixel2, PaintTransform((scale_factor2, 0, 0, scale_factor2, 0, 0), layer2)
)
# Foreground
layer2_canvas = PaintTranslate(
    x_canvas2, y_canvas2, PaintTransform((scale_factor2, 0, 0, scale_factor2, 0, 0), layer2)
)

##
# Applying the pixels
##

# To build a pixel glyph, we paint each pixel twice, once with each
# layer. We might want to change this to clever compositing/blending
# later, depending on how things look when we have the layers working
# correctly. So this function returns a paint tree with a PaintColrLayers
# operation, containing two layers for each pixel.
def buildPixelGlyph(pixelGlyphName, pixelPositions, layer1, layer2): #, layer3):
    layers = []
    for x, y in pixelPositions:
        #layers.append(PaintTranslate(x, y, PaintGlyph(pixelGlyphName, layer1))) # Background
        layers.append(PaintTranslate(x, y, PaintGlyph(pixelGlyphName, layer2))) # Foreground
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
            "_canvas",
            pixelPositions(font, glyphName),
            layer1_canvas, # Background
            layer2_canvas, # Foreground
        )
    else:
        glyphs[glyphName] = buildPixelGlyph(
            "px",
            pixelPositions(font, glyphName),
            layer1_pixel, # Background
            layer2_pixel, # Foreground
        )

# We have a problem; we have added six new axes to the font at this point,
# and while the gvar table can cope with that because it gets rebuilt when
# the font is saved, the HVAR table is not fully decompiled by fontTools,
# so it still refers to four axes, which makes it invalid when you try
# to save the font. Thankfully, HVAR isn't very necessary anyway, so we
# just get rid of it.
del font["HVAR"]
