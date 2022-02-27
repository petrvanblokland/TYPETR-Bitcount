#
#   Making the separate Bitcount masters, with the pixel shapes filled in.
#
import os
from scriptsLib import *

class GlyphData:
    """Instances hold data for each glyph and or pixel glyphs.

    <axes>
        <axis default="500" maximum="1000" minimum="0" name="Weight" tag="wght"/>
        <axis default="0" maximum="1000" minimum="0" name="Open" tag="OPEN"/>
        <axis default="300" maximum="900" minimum="0" name="Shape" tag="SHPE"/>
        <axis default="500" maximum="1000" minimum="0" name="Line" tag="LINE"/>
        <axis default="0" maximum="1000" minimum="0" name="Slanted" tag="slnt"/>
    </axes>
    """
    def __init__(self, uni=None, unicodes=None, c=None, name=None, comment=None, hex=None,
        wght=REGULAR, OPEN=CLOSED_QUAD, SHPE=CIRCLE, LINE=FILLED, slnt=ROMAN,
        ):
        # Design space location
        self.wght = wght
        self.OPEN = OPEN
        self.SHPE = SHPE
        self.LINE = LINE
        self.slnt = slnt

        # Add x-ref and accent-component relations
        if uni is None and c is not None:
            uni = ord(c)
        elif uni is not None and c is None:
            c = chr(uni)
        else:
            assert (uni is None and c is None) or (c is not None and uni == ord(c)), ('### %s %s %s %s %s' % (name, uni, ord(c or ' '), c, chr(uni or 0)))
        self.uni = uni
        if name is None and self.uni is not None:
            name = 'uni%04d' % self.uni
        self.name = name or 'Untitled'
        self.unicodes = unicodes
        if comment is None:
            comment = ''
            if self.c is not None:
                comment += self.c + ' - '
            comment += self.name
        self.comment = comment

    def __repr__(self):
        s = '<%s /%s' % (self.__class__.__name__, self.name)
        if self.uni is not None:
            s += ' %04x' % self.uni
        s += '>'
        return s

    def _get_c(self):
        if self.uni is not None:
            return chr(self.uni)
        return None
    c = property(_get_c)

    def _get_hex(self):
        if self.uni is not None:
            return '%04x' % self.uni
        return None
    hex = property(_get_hex)

GD = GlyphData

# Keep GlyphData instances, that know about the design space location of the pixel glyph.
PIXEL_DATA = {
    #CircleSquare@cnci1000
    #CircleSquare@line1000
    #CircleSquare@open0
    #CircleSquare@rndi1000
    #CircleSquare@rndo1000
    #CircleSquare@sqri1000
    #CircleSquare@sqro1000
    #CircleSquare@wght500
    'Instance@Circle-Black': GD(wght=BLACK, SHPE=CIRCLE),
    'Instance@Circle-Bold': GD(wght=BOLD, SHPE=CIRCLE),
    'Instance@Circle-Book': GD(wght=BOOK, SHPE=CIRCLE),
    'Instance@Circle-Regular': GD(wght=REGULAR, SHPE=CIRCLE),
    'Instance@Circle-Semibold': GD(wght=SEMIBOLD, SHPE=CIRCLE),
    'Instance@Circle-Thin': GD(wght=THIN, SHPE=CIRCLE),
    
    'Instance@LineCircle-Black': GD(wght=BLACK, SHPE=CIRCLE, LINE=LINE),
    'Instance@LineCircle-Bold': GD(wght=BOLD, SHPE=CIRCLE, LINE=LINE),
    'Instance@LineCircle-Book': GD(wght=BOOK, SHPE=CIRCLE, LINE=LINE),
    'Instance@LineCircle-Regular': GD(wght=REGULAR, SHPE=CIRCLE, LINE=LINE),
    'Instance@LineCircle-Semibold': GD(wght=SEMIBOLD, SHPE=CIRCLE, LINE=LINE),
    'Instance@LineCircle-Thin': GD(wght=THIN, SHPE=CIRCLE, LINE=LINE),
    
    'Instance@LineSquare-Black': GD(wght=BLACK, SHPE=SQUARE, LINE=LINE),
    'Instance@LineSquare-Bold': GD(wght=BOLD, SHPE=SQUARE, LINE=LINE),
    'Instance@LineSquare-Book': GD(wght=BOOK, SHPE=SQUARE, LINE=LINE),
    'Instance@LineSquare-Regular': GD(wght=REGULAR, SHPE=SQUARE, LINE=LINE),
    'Instance@LineSquare-Semibold': GD(wght=SEMIBOLD, SHPE=SQUARE, LINE=LINE),
    'Instance@LineSquare-Thin': GD(wght=THIN, SHPE=SQUARE, LINE=LINE),
    
    'Instance@OpenCircle-Black': GD(wght=BLACK, SHPE=CIRCLE, OPEN=OPEN_QUAD),
    'Instance@OpenCircle-Bold': GD(wght=BOLD, SHPE=CIRCLE, OPEN=OPEN_QUAD),
    'Instance@OpenCircle-Book': GD(wght=BOOK, SHPE=CIRCLE, OPEN=OPEN_QUAD),
    'Instance@OpenCircle-Regular': GD(wght=REGULAR, SHPE=CIRCLE, OPEN=OPEN_QUAD),
    'Instance@OpenCircle-Semibold': GD(wght=SEMIBOLD, SHPE=CIRCLE, OPEN=OPEN_QUAD),
    'Instance@OpenCircle-Thin': GD(wght=THIN, SHPE=CIRCLE, OPEN=OPEN_QUAD),
    
    'Instance@OpenLineCircle-Black': GD(),
    'Instance@OpenLineCircle-Bold': GD(),
    'Instance@OpenLineCircle-Book': GD(),
    'Instance@OpenLineCircle-Regular': GD(),
    'Instance@OpenLineCircle-Semibold': GD(),
    'Instance@OpenLineCircle-Thin': GD(),
    'Instance@OpenLineSquare-Black': GD(),
    'Instance@OpenLineSquare-Bold': GD(),
    'Instance@OpenLineSquare-Book': GD(),
    'Instance@OpenLineSquare-Regular': GD(),
    'Instance@OpenLineSquare-Semibold': GD(),
    'Instance@OpenLineSquare-Thin': GD(),
    'Instance@OpenSquare-Black': GD(),
    'Instance@OpenSquare-Bold': GD(),
    'Instance@OpenSquare-Book': GD(),
    'Instance@OpenSquare-Regular': GD(),
    'Instance@OpenSquare-Semibold': GD(),
    'Instance@OpenSquare-Thin': GD(),
    'Instance@Plus-Black': GD(),
    'Instance@Plus-Bold': GD(),
    'Instance@Plus-Book': GD(),
    'Instance@Plus-Regular': GD(),
    'Instance@Plus-Semibold': GD(),
    'Instance@Plus-Thin': GD(),
    'Instance@Square-Black': GD(),
    'Instance@Square-Bold': GD(),
    'Instance@Square-Book': GD(),
    'Instance@Square-Regular': GD(),
    'Instance@Square-Semibold': GD(),
    'Instance@Square-Thin': GD(),
    'InstanceItalic@Circle-Black': GD(),
    'InstanceItalic@Circle-Bold': GD(),
    'InstanceItalic@Circle-Book': GD(),
    'InstanceItalic@Circle-Regular': GD(),
    'InstanceItalic@Circle-Semibold': GD(),
    'InstanceItalic@Circle-Thin': GD(),
    'InstanceItalic@LineCircle-Black': GD(),
    'InstanceItalic@LineCircle-Bold': GD(),
    'InstanceItalic@LineCircle-Book': GD(),
    'InstanceItalic@LineCircle-Regular': GD(),
    'InstanceItalic@LineCircle-Semibold': GD(),
    'InstanceItalic@LineCircle-Thin': GD(),
    'InstanceItalic@LineSquare-Black': GD(),
    'InstanceItalic@LineSquare-Bold': GD(),
    'InstanceItalic@LineSquare-Book': GD(),
    'InstanceItalic@LineSquare-Regular': GD(),
    'InstanceItalic@LineSquare-Semibold': GD(),
    'InstanceItalic@LineSquare-Thin': GD(),
    'InstanceItalic@OpenCircle-Black': GD(),
    'InstanceItalic@OpenCircle-Bold': GD(),
    'InstanceItalic@OpenCircle-Book': GD(),
    'InstanceItalic@OpenCircle-Regular': GD(),
    'InstanceItalic@OpenCircle-Semibold': GD(),
    'InstanceItalic@OpenCircle-Thin': GD(),
    'InstanceItalic@OpenLineCircle-Black': GD(),
    'InstanceItalic@OpenLineCircle-Bold': GD(),
    'InstanceItalic@OpenLineCircle-Book': GD(),
    'InstanceItalic@OpenLineCircle-Regular': GD(),
    'InstanceItalic@OpenLineCircle-Semibold': GD(),
    'InstanceItalic@OpenLineCircle-Thin': GD(),
    'InstanceItalic@OpenLineSquare-Black': GD(),
    'InstanceItalic@OpenLineSquare-Bold': GD(),
    'InstanceItalic@OpenLineSquare-Book': GD(),
    'InstanceItalic@OpenLineSquare-Regular': GD(),
    'InstanceItalic@OpenLineSquare-Semibold': GD(),
    'InstanceItalic@OpenLineSquare-Thin': GD(),
    'InstanceItalic@OpenSquare-Black': GD(),
    'InstanceItalic@OpenSquare-Bold': GD(),
    'InstanceItalic@OpenSquare-Book': GD(),
    'InstanceItalic@OpenSquare-Regular': GD(),
    'InstanceItalic@OpenSquare-Semibold': GD(),
    'InstanceItalic@OpenSquare-Thin': GD(),
    'InstanceItalic@Plus-Black': GD(),
    'InstanceItalic@Plus-Bold': GD(),
    'InstanceItalic@Plus-Book': GD(),
    'InstanceItalic@Plus-Regular': GD(),
    'InstanceItalic@Plus-Semibold': GD(),
    'InstanceItalic@Plus-Thin': GD(),
    'InstanceItalic@Square-Black': GD(),
    'InstanceItalic@Square-Bold': GD(),
    'InstanceItalic@Square-Book': GD(),
    'InstanceItalic@Square-Regular': GD(),
    'InstanceItalic@Square-Semibold': GD(),
    'InstanceItalic@Square-Thin': GD(),
}
for name, gd in PIXEL_DATA.items():
    gd.name = name
