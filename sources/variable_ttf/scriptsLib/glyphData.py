#
#   Making the separate Bitcount masters, with the pixel shapes filled in.
#
#
#   Glyph data for each glyph stored here.
#
import os
from scriptsLib import *

class GlyphData:
    """Instances hold data for each glyph and or pixel glyphs.

    <axes>
        <axis default="500" maximum="1000" minimum="0" name="Weight" tag="wght"/>
        <axis default="0" maximum="1000" minimum="0" name="Open" tag="OPEN"/>
        <axis default="300" maximum="900" minimum="0" name="Shape" tag="SHPE"/>
        <axis default="0" maximum="1000" minimum="0" name="Slanted" tag="slnt"/>
    </axes>
    """
    def __init__(self, uni=None, unicodes=None, c=None, name=None, comment=None, hex=None,
        wght=REGULAR, OPEN=CLOSED_QUAD, SHPEIndex=0, slnt=ROMAN,
        ):
        # Design space location
        self.wght = wght
        self.OPEN = OPEN
        self.slnt = slnt

        self.SHPEIndex = SHPEIndex
        self.SHPE = SHPE2VALUE.get(SHPEIndex) # Shape value for axis value. Use SHPEIndex for shape index value

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

    # Roman

    # Glyph names of the pixels have this format:
    # Pix<SHPEIndex>@<wghtIndex><open>

    'Pix01@00': GD(SHPEIndex=1, wght=THIN),
    'Pix01@00_i': GD(SHPEIndex=1, wght=THIN, slnt=ITALIC),
    'Pix01@01': GD(SHPEIndex=1, wght=THIN, OPEN=OPEN_QUAD),
    'Pix01@01_i': GD(SHPEIndex=1, wght=THIN, OPEN=OPEN_QUAD, slnt=ITALIC),
    'Pix01@10': GD(SHPEIndex=1, wght=REGULAR, ),
    'Pix01@10_i': GD(SHPEIndex=1, wght=REGULAR, slnt=ITALIC),
    'Pix01@11': GD(SHPEIndex=1, wght=REGULAR, OPEN=OPEN_QUAD),
    'Pix01@11_i': GD(SHPEIndex=1, wght=REGULAR, OPEN=OPEN_QUAD, slnt=ITALIC),
    'Pix01@20': GD(SHPEIndex=1, wght=BLACK,),
    'Pix01@20_i': GD(SHPEIndex=1, wght=BLACK, slnt=ITALIC),
    'Pix01@21': GD(SHPEIndex=1, wght=BLACK, OPEN=OPEN_QUAD),
    'Pix01@21_i': GD(SHPEIndex=1, wght=BLACK, OPEN=OPEN_QUAD, slnt=ITALIC),
    'Pix02@00': GD(SHPEIndex=2, wght=THIN, ),
    'Pix02@00_i': GD(SHPEIndex=2, wght=THIN, slnt=ITALIC),
    'Pix02@01': GD(SHPEIndex=2, wght=THIN, OPEN=OPEN_QUAD),
    'Pix02@01_i': GD(SHPEIndex=2, wght=THIN, OPEN=OPEN_QUAD, slnt=ITALIC),
    'Pix02@10': GD(SHPEIndex=2, wght=REGULAR, ),
    'Pix02@10_i': GD(SHPEIndex=2, wght=REGULAR, slnt=ITALIC),
    'Pix02@11': GD(SHPEIndex=2, wght=REGULAR, OPEN=OPEN_QUAD),
    'Pix02@11_i': GD(SHPEIndex=2, wght=REGULAR, OPEN=OPEN_QUAD, slnt=ITALIC),
    'Pix02@20': GD(SHPEIndex=2, wght=BLACK, ),
    'Pix02@20_i': GD(SHPEIndex=2, wght=BLACK, slnt=ITALIC),
    'Pix02@21': GD(SHPEIndex=2, wght=BLACK, OPEN=OPEN_QUAD),
    'Pix02@21_i': GD(SHPEIndex=2, wght=BLACK, OPEN=OPEN_QUAD, slnt=ITALIC),
    'Pix03@00': GD(SHPEIndex=3, wght=THIN, ),
    'Pix03@00_i': GD(SHPEIndex=3, wght=THIN, slnt=ITALIC),
    'Pix03@01': GD(SHPEIndex=3, wght=THIN, OPEN=OPEN_QUAD),
    'Pix03@01_i': GD(SHPEIndex=3, wght=THIN, OPEN=OPEN_QUAD, slnt=ITALIC),
    'Pix03@10': GD(SHPEIndex=3, wght=REGULAR, ),
    'Pix03@10_i': GD(SHPEIndex=3, wght=REGULAR, slnt=ITALIC),
    'Pix03@11': GD(SHPEIndex=3, wght=REGULAR, OPEN=OPEN_QUAD),
    'Pix03@11_i': GD(SHPEIndex=3, wght=REGULAR, OPEN=OPEN_QUAD, slnt=ITALIC),
    'Pix03@20': GD(SHPEIndex=3, wght=BLACK, ),
    'Pix03@20_i': GD(SHPEIndex=3, wght=BLACK, slnt=ITALIC),
    'Pix03@21': GD(SHPEIndex=3, wght=BLACK, OPEN=OPEN_QUAD),
    'Pix03@21_i': GD(SHPEIndex=3, wght=BLACK, OPEN=OPEN_QUAD, slnt=ITALIC),
    'Pix04@00': GD(SHPEIndex=4, wght=THIN, ),
    'Pix04@00_i': GD(SHPEIndex=4, wght=THIN, slnt=ITALIC),
    'Pix04@01': GD(SHPEIndex=4, wght=THIN, OPEN=OPEN_QUAD),
    'Pix04@01_i': GD(SHPEIndex=4, wght=THIN, OPEN=OPEN_QUAD, slnt=ITALIC),
    'Pix04@10': GD(SHPEIndex=4, wght=REGULAR, ),
    'Pix04@10_i': GD(SHPEIndex=4, wght=REGULAR, slnt=ITALIC),
    'Pix04@11': GD(SHPEIndex=4, wght=REGULAR, OPEN=OPEN_QUAD),
    'Pix04@11_i': GD(SHPEIndex=4, wght=REGULAR, OPEN=OPEN_QUAD, slnt=ITALIC),
    'Pix04@20': GD(SHPEIndex=4, wght=BLACK, ),
    'Pix04@20_i': GD(SHPEIndex=4, wght=BLACK, slnt=ITALIC),
    'Pix04@21': GD(SHPEIndex=4, wght=BLACK, OPEN=OPEN_QUAD),
    'Pix04@21_i': GD(SHPEIndex=4, wght=BLACK, OPEN=OPEN_QUAD, slnt=ITALIC),
    'Pix05@00': GD(SHPEIndex=5, wght=THIN, ),
    'Pix05@00_i': GD(SHPEIndex=5, wght=THIN, slnt=ITALIC),
    'Pix05@01': GD(SHPEIndex=5, wght=THIN, OPEN=OPEN_QUAD),
    'Pix05@01_i': GD(SHPEIndex=5, wght=THIN, OPEN=OPEN_QUAD, slnt=ITALIC),
    'Pix05@10': GD(SHPEIndex=5, wght=REGULAR, ),
    'Pix05@10_i': GD(SHPEIndex=5, wght=REGULAR, slnt=ITALIC),
    'Pix05@11': GD(SHPEIndex=5, wght=REGULAR, OPEN=OPEN_QUAD),
    'Pix05@11_i': GD(SHPEIndex=5, wght=REGULAR, OPEN=OPEN_QUAD, slnt=ITALIC),
    'Pix05@20': GD(SHPEIndex=5, wght=BLACK, ),
    'Pix05@20_i': GD(SHPEIndex=5, wght=BLACK, slnt=ITALIC),
    'Pix05@21': GD(SHPEIndex=5, wght=BLACK, OPEN=OPEN_QUAD),
    'Pix05@21_i': GD(SHPEIndex=5, wght=BLACK, OPEN=OPEN_QUAD, slnt=ITALIC),
    'Pix06@00': GD(SHPEIndex=6, wght=THIN, ),
    'Pix06@00_i': GD(SHPEIndex=6, wght=THIN, slnt=ITALIC),
    'Pix06@01': GD(SHPEIndex=6, wght=THIN, OPEN=OPEN_QUAD),
    'Pix06@01_i': GD(SHPEIndex=6, wght=THIN, OPEN=OPEN_QUAD, slnt=ITALIC),
    'Pix06@10': GD(SHPEIndex=6, wght=REGULAR, ),
    'Pix06@10_i': GD(SHPEIndex=6, wght=REGULAR, slnt=ITALIC),
    'Pix06@11': GD(SHPEIndex=6, wght=REGULAR, OPEN=OPEN_QUAD),
    'Pix06@11_i': GD(SHPEIndex=6, wght=REGULAR, OPEN=OPEN_QUAD, slnt=ITALIC),
    'Pix06@20': GD(SHPEIndex=6, wght=BLACK, ),
    'Pix06@20_i': GD(SHPEIndex=6, wght=BLACK, slnt=ITALIC),
    'Pix06@21': GD(SHPEIndex=6, wght=BLACK, OPEN=OPEN_QUAD),
    'Pix06@21_i': GD(SHPEIndex=6, wght=BLACK, OPEN=OPEN_QUAD, slnt=ITALIC),
    'Pix07@00': GD(SHPEIndex=7, wght=THIN, ),
    'Pix07@00_i': GD(SHPEIndex=7, wght=THIN, slnt=ITALIC),
    'Pix07@01': GD(SHPEIndex=7, wght=THIN, OPEN=OPEN_QUAD),
    'Pix07@01_i': GD(SHPEIndex=7, wght=THIN, OPEN=OPEN_QUAD, slnt=ITALIC),
    'Pix07@10': GD(SHPEIndex=7, wght=REGULAR, ),
    'Pix07@10_i': GD(SHPEIndex=7, wght=REGULAR, slnt=ITALIC),
    'Pix07@11': GD(SHPEIndex=7, wght=REGULAR, OPEN=OPEN_QUAD),
    'Pix07@11_i': GD(SHPEIndex=7, wght=REGULAR, OPEN=OPEN_QUAD, slnt=ITALIC),
    'Pix07@20': GD(SHPEIndex=7, wght=BLACK, ),
    'Pix07@20_i': GD(SHPEIndex=7, wght=BLACK, slnt=ITALIC),
    'Pix07@21': GD(SHPEIndex=7, wght=BLACK, OPEN=OPEN_QUAD),
    'Pix07@21_i': GD(SHPEIndex=7, wght=BLACK, OPEN=OPEN_QUAD, slnt=ITALIC),
    'Pix08@00': GD(SHPEIndex=8, wght=THIN, ),
    'Pix08@00_i': GD(SHPEIndex=8, wght=THIN, slnt=ITALIC),
    'Pix08@01': GD(SHPEIndex=8, wght=THIN, OPEN=OPEN_QUAD),
    'Pix08@01_i': GD(SHPEIndex=8, wght=THIN, OPEN=OPEN_QUAD, slnt=ITALIC),
    'Pix08@10': GD(SHPEIndex=8, wght=REGULAR, ),
    'Pix08@10_i': GD(SHPEIndex=8, wght=REGULAR, slnt=ITALIC),
    'Pix08@11': GD(SHPEIndex=8, wght=REGULAR, OPEN=OPEN_QUAD),
    'Pix08@11_i': GD(SHPEIndex=8, wght=REGULAR, OPEN=OPEN_QUAD, slnt=ITALIC),
    'Pix08@20': GD(SHPEIndex=8, wght=BLACK, ),
    'Pix08@20_i': GD(SHPEIndex=8, wght=BLACK, slnt=ITALIC),
    'Pix08@21': GD(SHPEIndex=8, wght=BLACK, OPEN=OPEN_QUAD),
    'Pix08@21_i': GD(SHPEIndex=8, wght=BLACK, OPEN=OPEN_QUAD, slnt=ITALIC),
    'Pix09@00': GD(SHPEIndex=9, wght=THIN, ),
    'Pix09@00_i': GD(SHPEIndex=9, wght=THIN, slnt=ITALIC),
    'Pix09@01': GD(SHPEIndex=9, wght=THIN, OPEN=OPEN_QUAD),
    'Pix09@01_i': GD(SHPEIndex=9, wght=THIN, OPEN=OPEN_QUAD, slnt=ITALIC),
    'Pix09@10': GD(SHPEIndex=9, wght=REGULAR, ),
    'Pix09@10_i': GD(SHPEIndex=9, wght=REGULAR, slnt=ITALIC),
    'Pix09@11': GD(SHPEIndex=9, wght=REGULAR, OPEN=OPEN_QUAD),
    'Pix09@11_i': GD(SHPEIndex=9, wght=REGULAR, OPEN=OPEN_QUAD, slnt=ITALIC),
    'Pix09@20': GD(SHPEIndex=9, wght=BLACK, ),
    'Pix09@20_i': GD(SHPEIndex=9, wght=BLACK, slnt=ITALIC),
    'Pix09@21': GD(SHPEIndex=9, wght=BLACK, OPEN=OPEN_QUAD),
    'Pix09@21_i': GD(SHPEIndex=9, wght=BLACK, OPEN=OPEN_QUAD, slnt=ITALIC),
    'Pix10@00': GD(SHPEIndex=10, wght=THIN, ),
    'Pix10@00_i': GD(SHPEIndex=10, wght=THIN, slnt=ITALIC),
    'Pix10@01': GD(SHPEIndex=10, wght=THIN, OPEN=OPEN_QUAD),
    'Pix10@01_i': GD(SHPEIndex=10, wght=THIN, OPEN=OPEN_QUAD, slnt=ITALIC),
    'Pix10@10': GD(SHPEIndex=10, wght=REGULAR, ),
    'Pix10@10_i': GD(SHPEIndex=10, wght=REGULAR, slnt=ITALIC),
    'Pix10@11': GD(SHPEIndex=10, wght=REGULAR, OPEN=OPEN_QUAD),
    'Pix10@11_i': GD(SHPEIndex=10, wght=REGULAR, OPEN=OPEN_QUAD, slnt=ITALIC),
    'Pix10@20': GD(SHPEIndex=10, wght=BLACK, ),
    'Pix10@20_i': GD(SHPEIndex=10, wght=BLACK, slnt=ITALIC),
    'Pix10@21': GD(SHPEIndex=10, wght=BLACK, OPEN=OPEN_QUAD),
    'Pix10@21_i': GD(SHPEIndex=10, wght=BLACK, OPEN=OPEN_QUAD, slnt=ITALIC),
    'Pix11@00': GD(SHPEIndex=11, wght=THIN, ),
    'Pix11@00_i': GD(SHPEIndex=11, wght=THIN, slnt=ITALIC),
    'Pix11@01': GD(SHPEIndex=11, wght=THIN, OPEN=OPEN_QUAD),
    'Pix11@01_i': GD(SHPEIndex=11, wght=THIN, OPEN=OPEN_QUAD, slnt=ITALIC),
    'Pix11@10': GD(SHPEIndex=11, wght=REGULAR, ),
    'Pix11@10_i': GD(SHPEIndex=11, wght=REGULAR, slnt=ITALIC),
    'Pix11@11': GD(SHPEIndex=11, wght=REGULAR, OPEN=OPEN_QUAD),
    'Pix11@11_i': GD(SHPEIndex=11, wght=REGULAR, OPEN=OPEN_QUAD, slnt=ITALIC),
    'Pix11@20': GD(SHPEIndex=11, wght=BLACK, ),
    'Pix11@20_i': GD(SHPEIndex=11, wght=BLACK, slnt=ITALIC),
    'Pix11@21': GD(SHPEIndex=11, wght=BLACK, OPEN=OPEN_QUAD),
    'Pix11@21_i': GD(SHPEIndex=11, wght=BLACK, OPEN=OPEN_QUAD, slnt=ITALIC),
    'Pix12@00': GD(SHPEIndex=12, wght=THIN, ),
    'Pix12@00_i': GD(SHPEIndex=12, wght=THIN, slnt=ITALIC),
    'Pix12@01': GD(SHPEIndex=12, wght=THIN, OPEN=OPEN_QUAD),
    'Pix12@01_i': GD(SHPEIndex=12, wght=THIN, OPEN=OPEN_QUAD, slnt=ITALIC),
    'Pix12@10': GD(SHPEIndex=12, wght=REGULAR, ),
    'Pix12@10_i': GD(SHPEIndex=12, wght=REGULAR, slnt=ITALIC),
    'Pix12@11': GD(SHPEIndex=12, wght=REGULAR, OPEN=OPEN_QUAD),
    'Pix12@11_i': GD(SHPEIndex=12, wght=REGULAR, OPEN=OPEN_QUAD, slnt=ITALIC),
    'Pix12@20': GD(SHPEIndex=12, wght=BLACK, ),
    'Pix12@20_i': GD(SHPEIndex=12, wght=BLACK, slnt=ITALIC),
    'Pix12@21': GD(SHPEIndex=12, wght=BLACK, OPEN=OPEN_QUAD),
    'Pix12@21_i': GD(SHPEIndex=12, wght=BLACK, OPEN=OPEN_QUAD, slnt=ITALIC),
}
# Add the key as name to the GlyphData instances.
for name, gd in PIXEL_DATA.items():
    gd.name = name

# Build the pixel layer, where each position in the matrics refers
# to a separate pixel glyph

COLR_PIX_GRID_DATA = {}
COLR_PIX_MONO_DATA = {}
COLR_PIX_PROP_DATA = {}

for data, w, h in (
    (COLR_PIX_GRID_DATA, 6, 8),   # Max grid bounding box as pixels
    (COLR_PIX_MONO_DATA, 6, 11),  # Max mono bounding box as pixels
    (COLR_PIX_PROP_DATA, 10, 11), # Max proportional bounding box as pixels
    ):
    for x in range(w):
        for y in range(h):
            pixName = '_Pix%02d%0d' % (x, y)
            data[pixName] = GD(name=pixName)

