#
#   MasterData instance contain all master names, with their specific characteristics,
#   such as VF location in axis values
#

from scriptsLib import *
from scriptsLib.glyphData import Location

class MasterData:
    def __init__(self, fileName=None, path=None, type=None, # grid, mono or prop
            styleName=None, loc=None,
        ):
        self.fileName = fileName
        self.path = path
        self.type = type
        self.styleName = styleName
        assert loc is None or isinstance(loc, Location)
        self.loc = loc 

    def _get_style(self):
        style = [OPSZ[self.opsz], WGHT[self.wght]]
        if WDTH[self.wdth]:
            style.append(WDTH[self.wdth])
        return ' '.join(style)
    style = property(_get_style)
       
MD = MasterData

MASTERS_DATA = {
    # Collection of pixel shapes for every design space configuration
    VARIATION_PIXELS: MD(fileName=VARIATION_PIXELS),
    # Fill master data with sources, without location, so we can recognize them.
    # Grid is fixed 5x7 (6x8 including space), where the best possible of every
    # glyph is cropped inside the space. The result is that a number of accents
    # all translate into a single pixel.
    GRID_DOUBLE: MD(fileName=GRID_DOUBLE, name='Bitcount Grid Double'),
    GRID_DOUBLE_ITALIC: MD(fileName=GRID_DOUBLE_ITALIC, name='Bitcount Grid Double Italic'),
    GRID_SINGLE: MD(fileName=GRID_SINGLE, name='Bitcount Grid Single'),
    GRID_SINGLE_ITALIC: MD(fileName=GRID_SINGLE_ITALIC, name='Bitcount Grid Single Italic'),
    # Grid is horizontally ixed on 5 pixels (6 including space), but vertical it
    # takes the space the is needed for full accent showing.
    MONO_DOUBLE: MD(fileName=MONO_DOUBLE, name='Bitcount Mono Double'),
    MONO_DOUBLE_ITALIC: MD(fileName=MONO_DOUBLE_ITALIC, name='Bitcount Mono Double Italic'),
    MONO_SINGLE: MD(fileName=MONO_SINGLE, name='Bitcount Mono Single'),
    MONO_SINGLE_ITALIC: MD(fileName=MONO_SINGLE_ITALIC, name='Bitcount Mono Single Italic'),
    # Same height as GRID, but here glyph take horizontally the amount of pixels
    # that they need. 
    PROP_DOUBLE: MD(fileName=PROP_DOUBLE, name='Bitcount Prop Double'),
    PROP_DOUBLE_ITALIC: MD(fileName=PROP_DOUBLE_ITALIC, name='Bitcount Prop Double Italic'),
    PROP_SINGLE: MD(fileName=PROP_SINGLE, name='Bitcount Prop Single'),
    PROP_SINGLE_ITALIC: MD(fileName=PROP_SINGLE_ITALIC, name='Bitcount Prop Single Italic'),
    # Other master data generated automatically for the key positions in
    # various design spaces.
}
