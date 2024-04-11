#
#   Bitcount production scripts
#
from dataclasses import dataclass
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

VF_PATH = "fonts/ttf/variable/"  # vf/

DESIGNSPACE_TEMPLATE_PATH = "sources/Bitcount_Template.designspace"

# Source UFO that contains all separate black pixel shapes.
VARIATION_PIXELS = "Bitcount-VariationPixels.ufo"

# Source UFO that contains all colour layer "elements"
LAYER_ELEMENTS = "Bitcount-LayerElements.ufo"
LAYER_ELEMENTS_ITALIC = "Bitcount-LayerElements-Italic.ufo"

# Metadata for the Googlefonts build
GF_COPYRIGHT = "Copyright 2024 The Bitcount Project Authors (https://github.com/petrvanblokland/TYPETR-Bitcount)"

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

CLOSED_QUAD = 0
ELXP_QUAD = 100

# Style
ROMAN = 0
ITALIC = -8

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

slnt_MIN, slnt_DEF, slnt_MAX = slnt_AXIS = (ITALIC, ROMAN, ROMAN)  # Slant angle

# COLRv1 axes are defined as independent directions
DEFAULT_LOCATION = (wght_MIN, ELXP_MIN, ELSH_MIN, slnt_MIN)

AXISCOUNT = len(DEFAULT_LOCATION)  # Number of main axes, besides the COLV1 axes.

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

MONO_AXES = ["wght", "CRSV", "ELXP", "ELSH", "slnt"]
COLOR_AXES = ["SZP1", "XPN1", "YPN1", "SZP2", "XPN2", "YPN2"]


axis_suffix = ",".join(sorted(MONO_AXES))
color_axis_suffix = ",".join(sorted(COLOR_AXES + MONO_AXES))


@dataclass
class DesignSpaceParams:
    variant: str
    stem: str

    @property
    def dsName(self):
        return f"{BITCOUNT}_{self.variant}_{self.stem}{AXISCOUNT}.designspace"

    @property
    def masterName(self):
        return f"{BITCOUNT}_{self.variant}_{self.stem}.ufo"

    @property
    def masterItalicName(self):
        return f"{BITCOUNT}_{self.variant}_{self.stem}_Italic.ufo"

    # Path to copy the created masters to
    @property
    def ufoPath(self):
        return f"{MASTERS_PATH}{self.variant}-{self.stem}/"

    @property
    def _vfPrefix(self):
        # Bitcount Mono Double -> Bitcount
        # Bitcount Mono Single -> Bitcount Single
        # everthing else -> Bitcount Variant Stem
        if self.variant == "Mono":
            if self.stem == "Double":
                return BITCOUNT
            else:
                return f"{BITCOUNT}{self.stem}"
        else:
            return f"{BITCOUNT}{self.variant}{self.stem}"

    @property
    def vfName(self):
        return self._vfPrefix + f"[{axis_suffix}].ttf"

    @property
    def colorVfName(self):
        return self._vfPrefix + f"[{color_axis_suffix}].ttf"


DESIGN_SPACES = {}
for variant in VARIANTS:
    for stem in STEMS:
        designspace = DesignSpaceParams(variant, stem)
        DESIGN_SPACES[designspace.dsName] = designspace
