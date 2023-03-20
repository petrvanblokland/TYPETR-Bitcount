#
#   Bitcount production scripts
#
import os, shutil

# This is the common share glyph name, that all Bitcount glyph refer
# to as component. But replacing this glyph by the pixel shape that
# is bound to a certain location, all glyphs in the UFO’s will show
# the right pixel shape accordingly.
PIXEL_NAME = 'px'

UFO_PATH = 'ufo/'
FEATURES_PATH = 'features/'
MASTERS_PATH = '_masters/'

MASTERS_GRID_PATH = MASTERS_PATH + 'grid/'
MASTERS_MONO_PATH = MASTERS_PATH + 'mono/'
MASTERS_PROP_PATH = MASTERS_PATH + 'prop/'
MASTER_PATHS = (MASTERS_GRID_PATH, MASTERS_MONO_PATH, MASTERS_PROP_PATH)

MASTERS_COLG_GRID_PATH = MASTERS_PATH + 'gridCOLG/'
MASTERS_COLG_MONO_PATH = MASTERS_PATH + 'monoCOLG/'
MASTERS_COLG_PROP_PATH = MASTERS_PATH + 'propCOLG/'
MASTER_COLG_PATHS = (MASTERS_COLG_GRID_PATH, MASTERS_COLG_MONO_PATH, MASTERS_COLG_PROP_PATH)

VF_PATH = 'variable_ttf/' # vf/

# Name parts to auto-construct generated master UFO names.
BITCOUNT = 'Bitcount'
GRID = 'Grid'
MONO = 'Mono'
PROP = 'Prop'
VARIANTS = (GRID, MONO, PROP)
SINGLE = 'Single'
DOUBLE = 'Double'
STEMS = (SINGLE, DOUBLE)

# Source UFO that contains all separate black pixel shapes.
#VARIATION_PIXELS = 'Bitcount-VariationPixels.ufo'
VARIATION_PIXELS = 'Bitcount-VariationPixelsQ.ufo' # QUadratic curves in pixels

# Source masters in ufo/, used to copy into _masters/ with replaced pixel shape.
GRID_DOUBLE = 'Bitcount_Grid_Double.ufo'
GRID_DOUBLE_ITALIC = 'Bitcount_Grid_Double_Italic.ufo'
GRID_SINGLE = 'Bitcount_Grid_Single.ufo'
GRID_SINGLE_ITALIC = 'Bitcount_Grid_Single_Italic.ufo'
MONO_DOUBLE = 'Bitcount_Mono_Double.ufo'
MONO_DOUBLE_ITALIC = 'Bitcount_Mono_Double-Italic.ufo'
MONO_SINGLE = 'Bitcount_Mono_Single.ufo'
MONO_SINGLE_ITALIC = 'Bitcount_Mono_Single-Italic.ufo'
PROP_DOUBLE = 'Bitcount_Prop_Double.ufo'
PROP_DOUBLE_ITALIC = 'Bitcount_Prop_Double-Italic.ufo'
PROP_SINGLE = 'Bitcount_Prop_Single.ufo'
PROP_SINGLE_ITALIC = 'Bitcount_Prop_Single-Italic.ufo'

# Pixel weight sizes in pixel glyph names, this is the stem width of Bitcount glyphs
THIN = 0
#BOOK = 80
REGULAR = 500 
#SEMIBOLD = 116
#BOLD = 160
BLACK = 1000
#WEIGHTS = (THIN, BOOK, REGULAR, SEMIBOLD, BOLD, BLACK)

CLOSED_QUAD = 0
OPEN_QUAD = 1000

# Style
ROMAN = 0
ITALIC = 1000

# Shapes
# There are 12 separate shapes in the pixels fonts, that get distributes on ths SHPE axis.

# Convert the shape index number to an actual axis value
# This values depends on the amount of different shapes to fit in SHPE_MAX
SHPE2VALUE = {
    1:  0,
    2:  90,
    3:  180,
    4:  270,
    5:  360,
    6:  450,
    7:  540,
    8:  630,
    9:  720,
    10: 810,
    11: 900,
    12: 1000,
}

# Total number of masters:
# 3 (slnt) x 3 (OPEN) x 3 (LINE) x 6 (wght) 
# Axis values: Minimum, Default, Maximum
wght_MIN, wght_DEF, wght_MAX = wght_AXIS = (THIN, REGULAR, BLACK) 
OPEN_MIN, OPEN_DEF, OPEN_MAX = OPEN_AXIS = (CLOSED_QUAD, CLOSED_QUAD, OPEN_QUAD) # Connected or open quadrants
SHPE_MIN, SHPE_DEF, SHPE_MAX = SHPE_AXIS = (0, 0, 1000) # Catalog of a sequence of pixel variations
slnt_MIN, slnt_DEF, slnt_MAX = slnt_AXIS = (ROMAN, ROMAN, ITALIC) # Slant angle

