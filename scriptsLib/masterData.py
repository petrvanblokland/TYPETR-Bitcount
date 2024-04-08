# -*- coding: UTF-8 -*-
#
#   MasterData instance contain all master names, with their specific characteristics,
#   such as VF location in axis values
#


from scriptsLib import (
    DOUBLE,
    SINGLE,
    ROMAN,
    GRID,
    MASTERS_PATH,
    MONO,
    PROP,
)
from scriptsLib.glyphData import (
    COLR_PIX_GRID_DATA,
    COLR_PIX_MONO_DATA,
    COLR_PIX_PROP_DATA,
)


class MasterData:
    def __init__(
        self,
        variant=None,  # grid, mono or prop
        stem=None,
        style=None,
        familyName=None,
        styleName=None,
    ):
        self.name = "Bitcount " + variant + " " + stem
        self.ufoName = self.name.replace(" ", "_") + ".ufo"
        self.italicName = self.name.replace(" ", "_") + "-Italic.ufo"
        self.stem = stem
        self.variant = variant
        self.path = MASTERS_PATH + self.variant + "-" + self.stem + "/"
        self.familyName = familyName or self.name
        self.style = style
        self.styleName = (
            styleName or "%s"
        )  # Just replace by pixel name for this location/variant master
        if self.variant == MONO:
            self.colorPixelData = COLR_PIX_MONO_DATA
        elif self.variant == PROP:
            self.colorPixelData = COLR_PIX_PROP_DATA
        else:
            self.colorPixelData = COLR_PIX_GRID_DATA


MASTERS = [
    # Fill master data with sources, without location, so we can recognize them.
    # Grid is fixed 5x7 (6x8 including space), where the best possible of every
    # glyph is cropped inside the space. The result is that a number of accents
    # all translate into a single pixel.
    MasterData(variant=GRID, stem=DOUBLE),
    MasterData(variant=GRID, stem=SINGLE, style=ROMAN),
    # Grid is horizontally fixed on 5 pixels (6 including space), but vertical it
    # takes the space the is needed for full accent showing, to max of 11.
    MasterData(variant=MONO, stem=DOUBLE),
    MasterData(variant=MONO, stem=SINGLE, style=ROMAN),
    # Same height as GRID (max 11 pixels), but here glyphs take horizontally
    # the amount of pixels that they need (max is 10 pixels).
    MasterData(variant=PROP, stem=DOUBLE),
    MasterData(variant=PROP, stem=SINGLE, style=ROMAN),
    # Other master data generated automatically for the key positions in
    # extreme axis positions for various design spaces.
]
MASTERS_DATA = {md.ufoName: md for md in MASTERS}
