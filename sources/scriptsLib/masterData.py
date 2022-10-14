# -*- coding: UTF-8 -*-
#
#   MasterData instance contain all master names, with their specific characteristics,
#   such as VF location in axis values
#

from scriptsLib import *
from scriptsLib.glyphData import *

class MasterData:
    def __init__(self, fileName=None, path=None, variant=None, # grid, mono or prop
            stem=None, name=None, style=None, styleName=None, italicName=None,
            colorPixelData=None,
        ):
        self.fileName = fileName
        self.name = name
        self.path = path
        self.stem = stem
        self.variant = variant
        self.style = style
        self.styleName = styleName
        self.italicName = italicName # The italic companion of this master
        self.colorPixelData = colorPixelData # Glyphdata with pixels/positions
     
MD = MasterData

MASTERS_DATA = {
    # Fill master data with sources, without location, so we can recognize them.
    # Grid is fixed 5x7 (6x8 including space), where the best possible of every
    # glyph is cropped inside the space. The result is that a number of accents
    # all translate into a single pixel.
    GRID_DOUBLE: MD(fileName=GRID_DOUBLE, name='Bitcount Grid Double', path=MASTERS_GRID_PATH,
        variant=GRID, stem=DOUBLE, italicName=GRID_DOUBLE_ITALIC,
        colorPixelData=COLR_PIX_GRID_DATA),
    GRID_SINGLE: MD(fileName=GRID_SINGLE, name='Bitcount Grid Single', path=MASTERS_GRID_PATH,
        variant=GRID, stem=SINGLE, style=ROMAN, italicName=GRID_SINGLE_ITALIC,
        colorPixelData=COLR_PIX_GRID_DATA),
    # Grid is horizontally fixed on 5 pixels (6 including space), but vertical it
    # takes the space the is needed for full accent showing, to max of 11.
    MONO_DOUBLE: MD(fileName=MONO_DOUBLE, name='Bitcount Mono Double', path=MASTERS_MONO_PATH,
        variant=MONO, stem=DOUBLE, italicName=MONO_DOUBLE_ITALIC,
        colorPixelData=COLR_PIX_MONO_DATA),
    MONO_SINGLE: MD(fileName=MONO_SINGLE, name='Bitcount Mono Single', path=MASTERS_MONO_PATH,
        variant=MONO, stem=SINGLE, style=ROMAN, italicName=MONO_SINGLE_ITALIC,
        colorPixelData=COLR_PIX_MONO_DATA),
    # Same height as GRID (max 11 pixels), but here glyphs take horizontally 
    # the amount of pixels that they need (max is 10 pixels). 
    PROP_DOUBLE: MD(fileName=PROP_DOUBLE, name='Bitcount Prop Double', path=MASTERS_PROP_PATH,
        variant=PROP, stem=DOUBLE, italicName=PROP_DOUBLE_ITALIC,
        colorPixelData=COLR_PIX_PROP_DATA),
    PROP_SINGLE: MD(fileName=PROP_SINGLE, name='Bitcount Prop Single', path=MASTERS_PROP_PATH, 
        variant=PROP, stem=SINGLE, style=ROMAN, italicName=PROP_SINGLE_ITALIC,
        colorPixelData=COLR_PIX_PROP_DATA),
    # Other master data generated automatically for the key positions in
    # various design spaces.
}

# Collection of pixel shapes for every design space configuration
VARIATION_PIXELS: MD(fileName=VARIATION_PIXELS)
