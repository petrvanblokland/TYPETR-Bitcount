#
#   Bitcount production scripts
#
import os, shutil

# This is the common share glyph name, that all Bitcount glyph refer
# to as component. But replacing this glyph by the pixel shape that
# is bound to a certain location, all glyphs in the UFO’s will show
# the right pixel shape accordingly.
PIXEL_NAME = "px"

POST_FIX = "el_"  # Add to element name

# Name parts to auto-construct generated master UFO names.
BITCOUNT = "Bitcount"
# Variants
GRID = "Grid"
MONO = "Mono"
PROP = "Prop"
VARIANTS = (GRID, MONO, PROP)
# Stems
SINGLE = "Single"
DOUBLE = "Double"
STEMS = (SINGLE, DOUBLE)

UFO_PATH = "sources/ufo/"
FEATURES_PATH = "sources/features/"
MASTERS_PATH = "sources/build/"  # Gitignore, not committing into Github

MASTERS_GRID_SINGLE_PATH = f"{MASTERS_PATH}{GRID}-{SINGLE}/"
MASTERS_GRID_DOUBLE_PATH = f"{MASTERS_PATH}{GRID}-{DOUBLE}/"
MASTERS_MONO_SINGLE_PATH = f"{MASTERS_PATH}{MONO}-{SINGLE}/"
MASTERS_MONO_DOUBLE_PATH = f"{MASTERS_PATH}{MONO}-{DOUBLE}/"
MASTERS_PROP_SINGLE_PATH = f"{MASTERS_PATH}{PROP}-{SINGLE}/"
MASTERS_PROP_DOUBLE_PATH = f"{MASTERS_PATH}{PROP}-{DOUBLE}/"
MASTER_PATHS = (
    MASTERS_GRID_SINGLE_PATH,
    MASTERS_GRID_DOUBLE_PATH,
    MASTERS_MONO_SINGLE_PATH,
    MASTERS_MONO_DOUBLE_PATH,
    MASTERS_PROP_SINGLE_PATH,
    MASTERS_PROP_DOUBLE_PATH,
)

# MASTERS_COLG_GRID_PATH = MASTERS_PATH + 'gridCOLG/'
# MASTERS_COLG_MONO_PATH = MASTERS_PATH + 'monoCOLG/'
# MASTERS_COLG_PROP_PATH = MASTERS_PATH + 'propCOLG/'
# MASTER_COLG_PATHS = (MASTERS_COLG_GRID_PATH, MASTERS_COLG_MONO_PATH, MASTERS_COLG_PROP_PATH)

VF_PATH = "fonts/ttf/variable/"  # vf/

DESIGNSPACE_TEMPLATE_PATH = "sources/Bitcount_Template.designspace"

# Source UFO that contains all separate black pixel shapes.
VARIATION_PIXELS = "Bitcount-VariationPixels.ufo"
# VARIATION_PIXELS = 'Bitcount-VariationPixelsQ.ufo' # Quadratic curves in pixels

# Source UFO that contains all colour layer "elements"
LAYER_ELEMENTS = "Bitcount-LayerElements.ufo"
LAYER_ELEMENTS_ITALIC = "Bitcount-LayerElements-Italic.ufo"

# Source masters in ufo/, used to copy into _masters/ with replaced pixel shape.
GRID_DOUBLE = f"{BITCOUNT}_{GRID}_{DOUBLE}.ufo"
GRID_DOUBLE_ITALIC = "Bitcount_Grid_Double_Italic.ufo"
GRID_SINGLE = "Bitcount_Grid_Single.ufo"
GRID_SINGLE_ITALIC = "Bitcount_Grid_Single_Italic.ufo"
MONO_DOUBLE = "Bitcount_Mono_Double.ufo"
MONO_DOUBLE_ITALIC = "Bitcount_Mono_Double-Italic.ufo"
MONO_SINGLE = "Bitcount_Mono_Single.ufo"
MONO_SINGLE_ITALIC = "Bitcount_Mono_Single-Italic.ufo"
PROP_DOUBLE = "Bitcount_Prop_Double.ufo"
PROP_DOUBLE_ITALIC = "Bitcount_Prop_Double-Italic.ufo"
PROP_SINGLE = "Bitcount_Prop_Single.ufo"
PROP_SINGLE_ITALIC = "Bitcount_Prop_Single-Italic.ufo"

# Pixel weight sizes in pixel glyph names, this is the stem width of Bitcount glyphs
# Instead we use OS/2 weight values on the axis values.
THIN = 100  # Pixel size: 24, smaller get irregular curves
REGULAR = 400  # Pixel size: 100
BLACK = 900  # Pixel size: 200

# Scale of the COLRv1 layers
SMIN = 0
SDEF = 30
SMAX = 100
# Position of the COLRv1 layers
LMIN = 0  # -100 #For 3x3 elements. Before it was -200 for 5x5 elements
LDEF = 50  # 0
LMAX = 100  # For 3x3 elements. Before it was 200 for 5x5 elements

WGHT_MIN = THIN
WGHT_DEF = REGULAR
WGHT_MAX = BLACK
ELXP_MIN = ELSH_MIN = SLNT_MIN = 0
ELXP_MAX = ELSH_MAX = SLNT_MAX = 90

# COLRv1 axes are defined as independent directions
DEFAULT_LOCATION = (WGHT_MIN, ELXP_MIN, ELSH_MIN, SLNT_MIN)

AXISCOUNT = len(DEFAULT_LOCATION)  # Number of main axes, besides the COLV1 axes.

DESIGN_SPACES = {}
for variant in VARIANTS:
    for stem in STEMS:
        # Name of the design space to generate
        dsName = f"{BITCOUNT}_{variant}_{stem}{AXISCOUNT}.designspace"
        # Master UFO to be used as source for all different pixel masters
        masterName = f"{BITCOUNT}_{variant}_{stem}.ufo"
        # Same for italic (slanted) master
        masterItalicName = f"{BITCOUNT}_{variant}_{stem}_Italic.ufo"
        # Path to copy the created masters to
        ufoPath = f"{MASTERS_PATH}{variant}-{stem}/"
        dsParams = dict(
            variant=variant,
            stem=stem,
            axisCount=AXISCOUNT,
            ufoPath=ufoPath,
            masterName=masterName,
            masterItalicName=masterItalicName,
            dsName=dsName,
        )
        DESIGN_SPACES[dsName] = dsParams


CLOSED_QUAD = 0
ELXP_QUAD = 100

# Style
ROMAN = 0
ITALIC = 90

# Shapes
# There are 12 separate shapes in the pixels fonts, that get distributes on ths ELSH axis.

# Convert the shape index number to an actual axis value
# This values depends on the amount of different shapes to fit in ELSH_MAX
ELSH2VALUE = {
    1: 0,
    2: 9,
    3: 18,
    4: 27,
    5: 36,
    6: 45,
    7: 54,
    8: 63,
    9: 72,
    10: 81,
    11: 90,
    12: 100,
}

SHAPES = sorted(ELSH2VALUE.values())

# Total number of masters:
# 3 (slnt) x 3 (ELXP) x 3 (LINE) x 6 (wght)
# Axis values: Minimum, Default, Maximum
wght_MIN, wght_DEF, wght_MAX = wght_AXIS = (THIN, REGULAR, BLACK)
ELXP_MIN, ELXP_DEF, ELXP_MAX = ELXP_AXIS = (
    CLOSED_QUAD,
    CLOSED_QUAD,
    ELXP_QUAD,
)  # Connected or open quadrants
ELSH_MIN, ELSH_DEF, ELSH_MAX = ELSH_AXIS = (
    0,
    0,
    100,
)  # Catalog of a sequence of pixel variations
slnt_MIN, slnt_DEF, slnt_MAX = slnt_AXIS = (ROMAN, ROMAN, ITALIC)  # Slant angle

MONO_AXES = ["wght", "ELXP", "ELSH", "slnt"]
COLOR_AXES = ["SZP1", "XPN1", "YPN1", "SZP2", "XPN2", "YPN2"]
