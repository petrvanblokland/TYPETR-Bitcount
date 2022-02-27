#
#   MasterData instance contain all master names, with their specific characteristics,
#   such as VF location in axis values
#

# Name parts to auto-construct generated master UFO names.
BITCOUNT = 'Bitcount'
GRID = 'Grid'
MONO = 'Mono'
PROP = 'Prop'
TYPES = (GRID, MONO, PROP)
SINGLE = 'Single'
DOUBLE = 'Double'
STEMS = (SINGLE, DOUBLE)

# Source masters in sources/ufo/, used to copy into _masters/ with replaced pixel shape.
VARIATION_PIXELS = 'Bitcount-VariationPixels.ufo'
GRID_DOUBLE = 'Bitcount_Grid_Double.ufo'
GRID_SINGLE_ITALIC = 'Bitcount_Grid_Single_Italic.ufo'
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

AXES = dict(
    # Minimum, Default, Maximum
    wght=(0, 500, 1000),
    OPEN=(0, 0, 1000), # 0 = Filled, 1000 = Outline
    LINE=(0, 500, 1000), # Thickness of outline
    SHPE=(0, 300, 900), # Catalog of a sequence of pixel variations
    slnt=(0, 0, 1000), # Slant angle
)
class Location:
    """Location in design space"""
    def __init__(self, wght, OPEN, SHPE, LINE, slnt):
        minimum, _, maximum = AXES['wght']
        assert minimum <= wght <= maximum
        self.wght = wght
        minimum, _, maximum = AXES['OPEN']
        assert minimum <= OPEN <= maximum
        self.OPEN = OPEN
        minimum, _, maximum = AXES['SHPE']
        assert minimum <= SHPE <= maximum
        self.SHPE = SHPE
        minimum, _, maximum = AXES['SHPE']
        assert minimum <= LINE <= maximum
        self.LINE = LINE
        minimum, _, maximum = AXES['slnt']
        assert minimum <= slnt <= maximum
        self.slnt = slnt

class MasterData:
    def __init__(self, fileName=None, path=None, type=None, # grid, mono or prop
            styleName=None, location=None,
        ):
        self.fileName = fileName
        self.path = path
        self.type = type
        self.styleName = styleName
        assert location is None or isinstance(location, Location))
        self.location = location 

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
    GRID_DOUBLE: MD(fileName=GRID_DOUBLE),
    GRID_DOUBLE_ITALIC: MD(fileName=GRID_DOUBLE_ITALIC),
    GRID_SINGLE: MD(fileName=GRID_DOUBLE_ITALIC),
    GRID_SINGLE_ITALIC: MD(fileName=GRID_DOUBLE_ITALIC),
    # Grid is horizontally ixed on 5 pixels (6 including space), but vertical it
    # takes the space the is needed for full accent showing.
    MONO_DOUBLE: MD(fileName=MONO_DOUBLE),
    MONO_DOUBLE_ITALIC: MD(fileName=MONO_DOUBLE_ITALIC),
    MONO_SINGLE: MD(fileName=MONO_SINGLE),
    MONO_SINGLE_ITALIC: MD(fileName=MONO_SINGLE_ITALIC),
    # Same height as GRID, but here glyph take horizontally the amount of pixels
    # that they need. 
    PROP_DOUBLE: MD(fileName=PROP_DOUBLE),
    PROP_DOUBLE_ITALIC: MD(fileName=PROP_DOUBLE_ITALIC),
    PROP_SINGLE: MD(fileName=PROP_SINGLE),
    PROP_SINGLE_ITALIC: MD(fileName=PROP_SINGLE_ITALIC),
    # Other master data generated automatically for the key positions in
    # various design spaces.
}
