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
    GRID_DOUBLE,
    GRID_DOUBLE_ITALIC,
    GRID_SINGLE,
    GRID_SINGLE_ITALIC,
    MASTERS_GRID_DOUBLE_PATH,
    MASTERS_GRID_SINGLE_PATH,
    MASTERS_MONO_DOUBLE_PATH,
    MASTERS_MONO_SINGLE_PATH,
    MASTERS_PROP_DOUBLE_PATH,
    MASTERS_PROP_SINGLE_PATH,
    MONO,
    MONO_DOUBLE,
    MONO_DOUBLE_ITALIC,
    MONO_SINGLE,
    MONO_SINGLE_ITALIC,
    PROP,
    PROP_DOUBLE,
    PROP_DOUBLE_ITALIC,
    PROP_SINGLE,
    PROP_SINGLE_ITALIC,
)
from scriptsLib.glyphData import (
    COLR_PIX_GRID_DATA,
    COLR_PIX_MONO_DATA,
    COLR_PIX_PROP_DATA,
)


class MasterData:
    def __init__(
        self,
        ufoName=None,
        path=None,
        variant=None,  # grid, mono or prop
        stem=None,
        name=None,
        style=None,
        familyName=None,
        styleName=None,
        italicName=None,
        colorPixelData=None,
    ):
        self.ufoName = ufoName
        self.name = name
        self.path = path
        self.stem = stem
        self.variant = variant
        self.familyName = familyName or name
        self.style = style
        self.styleName = (
            styleName or "%s"
        )  # Just replace by pixel name for this location/variant master
        self.italicName = italicName  # The italic companion of this master
        self.colorPixelData = colorPixelData  # Glyphdata with pixels/positions


MD = MasterData


MASTERS_DATA = {
    # Fill master data with sources, without location, so we can recognize them.
    # Grid is fixed 5x7 (6x8 including space), where the best possible of every
    # glyph is cropped inside the space. The result is that a number of accents
    # all translate into a single pixel.
    GRID_DOUBLE: MD(
        ufoName=GRID_DOUBLE,
        name="Bitcount Grid Double",
        path=MASTERS_GRID_DOUBLE_PATH,
        variant=GRID,
        stem=DOUBLE,
        italicName=GRID_DOUBLE_ITALIC,
        colorPixelData=COLR_PIX_GRID_DATA,
    ),
    GRID_SINGLE: MD(
        ufoName=GRID_SINGLE,
        name="Bitcount Grid Single",
        path=MASTERS_GRID_SINGLE_PATH,
        variant=GRID,
        stem=SINGLE,
        style=ROMAN,
        italicName=GRID_SINGLE_ITALIC,
        colorPixelData=COLR_PIX_GRID_DATA,
    ),
    # Grid is horizontally fixed on 5 pixels (6 including space), but vertical it
    # takes the space the is needed for full accent showing, to max of 11.
    MONO_DOUBLE: MD(
        ufoName=MONO_DOUBLE,
        name="Bitcount Mono Double",
        path=MASTERS_MONO_DOUBLE_PATH,
        variant=MONO,
        stem=DOUBLE,
        italicName=MONO_DOUBLE_ITALIC,
        colorPixelData=COLR_PIX_MONO_DATA,
    ),
    MONO_SINGLE: MD(
        ufoName=MONO_SINGLE,
        name="Bitcount Mono Single",
        path=MASTERS_MONO_SINGLE_PATH,
        variant=MONO,
        stem=SINGLE,
        style=ROMAN,
        italicName=MONO_SINGLE_ITALIC,
        colorPixelData=COLR_PIX_MONO_DATA,
    ),
    # Same height as GRID (max 11 pixels), but here glyphs take horizontally
    # the amount of pixels that they need (max is 10 pixels).
    PROP_DOUBLE: MD(
        ufoName=PROP_DOUBLE,
        name="Bitcount Prop Double",
        path=MASTERS_PROP_DOUBLE_PATH,
        variant=PROP,
        stem=DOUBLE,
        italicName=PROP_DOUBLE_ITALIC,
        colorPixelData=COLR_PIX_PROP_DATA,
    ),
    PROP_SINGLE: MD(
        ufoName=PROP_SINGLE,
        name="Bitcount Prop Single",
        path=MASTERS_PROP_SINGLE_PATH,
        variant=PROP,
        stem=SINGLE,
        style=ROMAN,
        italicName=PROP_SINGLE_ITALIC,
        colorPixelData=COLR_PIX_PROP_DATA,
    ),
    # Other master data generated automatically for the key positions in
    # extreme axis positions for various design spaces.
}
