# -*- coding: UTF-8 -*-
#
#   MasterData instance contain all master names, with their specific characteristics,
#   such as VF location in axis values
#

from scriptsLib import *
from scriptsLib.glyphData import *

VERSION_MAJOR = 1
VERSION_MINOR = 0
VERSION_BUILD = 13

VERSION = 'Version %d.%03d Build %03d' % (VERSION_MAJOR, VERSION_MINOR, VERSION_BUILD)
COPYRIGHT = """Copyright 2023 TYPETR | Buro Petr van Blokland + Claudia Mens. 
All Rights Reserved. Presti is a registered trademark by TYPETR.
Designers: Petr van Blokland
Software: RoboFont and Outliner by Frederik Berlaen, Skateboard, Similarity and EditThatNextMaster by Erik van Blokland, Prepolator by Tal Leming, DrawBot by Just van Rossum and Frederik Berlaen, FontGoggles by Just van Rossum, FontTools and FontMake by Just van Rossum, Google and many others, paintcompiler by Simon Cozens"""
TRADEMARK = """Bitcount is a trademark of TYPETR | Buro Petr van Blokland + Claudia Mens"""
DEFAULT_WEIGHT_CLASS = 400
DEFAULT_WIDTH_CLASS = 5
LOWEST_PPEM = 6
UNITS_PER_EM = 1000
OS2_WIN_ASCENT = 1052
OS2_WIN_DESCENT = 549
DESIGNER = 'TYPETR | Petr van Blokland'
MANUFACTURER = 'TYPETR | Google Fonts'
VENDOR_URL = MANUFACTURER_URL = 'https://www.typenetwork.com'
DESIGNER_URL = 'https://typetr.typenetwork.com'
EULA_URL = None #'https://store.typenetwork.com/cart/eula/type-network'
EULA_DESCRIPTION = None #'' #https://store.typenetwork.com/cart/eula/type-network. This Font Software License Agreement (the "Agreement") becomes a binding contract between you and Type Network LLC ("Type Network") when you click on the area marked "OK," "I Accept," "ACCEPT LICENSE AGREEMENT," "I AGREE" or similar language. Other rights and limitations may apply depending upon your selections at the time you purchase a license. If you do not wish to be bound by the agreement, you cannot access, download or use the font software."""

REGULAR = 'Regular' # Default fsSelection flag

class MasterData:
    def __init__(self, ufoName=None, path=None,  
            variant=None, # grid, mono or prop
            stem=None, name=None, style=None, familyName=None, styleName=None, italicName=None,
            colorPixelData=None,
            # FOr VF-TTF name table fixes
            isMaster=True,
            fsSelection=REGULAR,
            italicAngle=0,
            uniqueID=None,
            postscriptName=None,
            fullName=None, # Or uniqueID
            version=None, versionMajor=VERSION_MAJOR, versionMinor=VERSION_MINOR,
            openTypeOS2WinAscent=OS2_WIN_ASCENT, openTypeOS2WinDescent=OS2_WIN_DESCENT,
            preferredFamily=None, preferredSubFamily=None,
            copyright=COPYRIGHT, trademark=TRADEMARK, lowestRecPPEM=LOWEST_PPEM,
            openTypeOS2Type=[2, 8], # fsType, TN standard
        ):
        self.ufoName = ufoName
        self.name = name
        self.path = path
        self.stem = stem
        self.variant = variant
        self.familyName = familyName or name
        self.style = style
        self.styleName = styleName or '%s' # Just replace by pixel name for this location/variant master
        self.uniqueID = uniqueID
        self.postscriptName = postscriptName
        self.fullName = fullName or uniqueID
        self.italicName = italicName # The italic companion of this master
        self.colorPixelData = colorPixelData # Glyphdata with pixels/positions
        self.isMaster = isMaster # Separate realy UFO masters from generated output VF-TTF files
        self.fsSelection = fsSelection # Flag for VF-TTF files
        self.italicAngle = italicAngle
        self.version = version or VERSION
        self.versionMajor = versionMajor
        self.versionMinor = versionMinor
        self.lowestRecPPEM = lowestRecPPEM
        self.copyright = copyright
        self.trademark = trademark
        self.lowestRecPPEM = lowestRecPPEM
        self.openTypeOS2Type = openTypeOS2Type
        self.preferredFamily = preferredFamily
        self.preferredSubFamily = preferredSubFamily

MD = MasterData


MASTERS_DATA = {
    # Fill master data with sources, without location, so we can recognize them.
    # Grid is fixed 5x7 (6x8 including space), where the best possible of every
    # glyph is cropped inside the space. The result is that a number of accents
    # all translate into a single pixel.
    GRID_DOUBLE: MD(ufoName=GRID_DOUBLE, name='Bitcount Grid Double', 
        path=MASTERS_GRID_DOUBLE_PATH, 
        variant=GRID, stem=DOUBLE, italicName=GRID_DOUBLE_ITALIC,
        colorPixelData=COLR_PIX_GRID_DATA),
    GRID_SINGLE: MD(ufoName=GRID_SINGLE, name='Bitcount Grid Single', 
        path=MASTERS_GRID_SINGLE_PATH, 
        variant=GRID, stem=SINGLE, style=ROMAN, italicName=GRID_SINGLE_ITALIC,
        colorPixelData=COLR_PIX_GRID_DATA),
    # Grid is horizontally fixed on 5 pixels (6 including space), but vertical it
    # takes the space the is needed for full accent showing, to max of 11.
    MONO_DOUBLE: MD(ufoName=MONO_DOUBLE, name='Bitcount Mono Double', 
        path=MASTERS_MONO_DOUBLE_PATH, 
        variant=MONO, stem=DOUBLE, italicName=MONO_DOUBLE_ITALIC,
        colorPixelData=COLR_PIX_MONO_DATA),
    MONO_SINGLE: MD(ufoName=MONO_SINGLE, name='Bitcount Mono Single', 
        path=MASTERS_MONO_SINGLE_PATH, 
        variant=MONO, stem=SINGLE, style=ROMAN, italicName=MONO_SINGLE_ITALIC,
        colorPixelData=COLR_PIX_MONO_DATA),
    # Same height as GRID (max 11 pixels), but here glyphs take horizontally 
    # the amount of pixels that they need (max is 10 pixels). 
    PROP_DOUBLE: MD(ufoName=PROP_DOUBLE, name='Bitcount Prop Double', 
        path=MASTERS_PROP_DOUBLE_PATH, 
        variant=PROP, stem=DOUBLE, italicName=PROP_DOUBLE_ITALIC,
        colorPixelData=COLR_PIX_PROP_DATA),
    PROP_SINGLE: MD(ufoName=PROP_SINGLE, name='Bitcount Prop Single', 
        path=MASTERS_PROP_SINGLE_PATH, 
        variant=PROP, stem=SINGLE, style=ROMAN, italicName=PROP_SINGLE_ITALIC,
        colorPixelData=COLR_PIX_PROP_DATA),
    # Other master data generated automatically for the key positions in
    # extreme axis positions for various design spaces.

    # Masters data for the generated VF and VF_COLRv1: used to fix name tables of generated TTF files.
    GRID_SINGLE_VF: MD(name=GRID_SINGLE_VF, isMaster=False,
        familyName='Bitcount Grid Single VF', styleName='Regular', fsSelection=REGULAR, italicAngle=0,
        uniqueID='Bitcount Grid Single VF Regular', postscriptName='BitcountGridSingleVF-Regular', 
        # preferredFamily, preferredSubFamily
    ),
    GRID_SINGLE_VF_COLRv1: MD(name=GRID_SINGLE_VF_COLRv1, isMaster=False,
        familyName='Bitcount Grid Single VF COLRv1', styleName='Regular', fsSelection=REGULAR, italicAngle=0,
        uniqueID='Bitcount Grid Single VF COLRv1 Regular', postscriptName='BitcountVFGridSingleCOLRv1-Regular', 
        # preferredFamily, preferredSubFamily
    ),
    GRID_DOUBLE_VF: MD(name=GRID_DOUBLE_VF, isMaster=False,
        familyName='Bitcount Grid Double VF', styleName='Regular', fsSelection=REGULAR, italicAngle=0,
        uniqueID='Bitcount Grid Double VF Regular', postscriptName='BitcountGridDoubleVF-Regular', 
        # preferredFamily, preferredSubFamily
    ),
    GRID_DOUBLE_VF_COLRv1: MD(name=GRID_DOUBLE_VF_COLRv1, isMaster=False,
        familyName='Bitcount Grid Double VF COLRv1', styleName='Regular', fsSelection=REGULAR, italicAngle=0,
        uniqueID='Bitcount Grid Double VF COLRv1 Regular', postscriptName='BitcountVFGridDoubleCOLRv1-Regular', 
        # preferredFamily, preferredSubFamily
    ),

    MONO_SINGLE_VF: MD(name=MONO_SINGLE_VF, isMaster=False,
        familyName='Bitcount Mono Single VF', styleName='Regular', fsSelection=REGULAR, italicAngle=0,
        uniqueID='Bitcount Mono Single VF Regular', postscriptName='BitcountMonoSingleVF-Regular', 
        # preferredFamily, preferredSubFamily
    ),
    MONO_SINGLE_VF_COLRv1: MD(name=MONO_SINGLE_VF_COLRv1, isMaster=False,
        familyName='Bitcount Mono Single VF COLRv1', styleName='Regular', fsSelection=REGULAR, italicAngle=0,
        uniqueID='Bitcount Mono Single VF COLRv1 Regular', postscriptName='BitcountVFMonoSingleCOLRv1-Regular', 
        # preferredFamily, preferredSubFamily
    ),
    MONO_DOUBLE_VF: MD(name=MONO_DOUBLE_VF, isMaster=False,
        familyName='Bitcount Mono Double VF', styleName='Regular', fsSelection=REGULAR, italicAngle=0,
        uniqueID='Bitcount Mono Double VF Regular', postscriptName='BitcountMonoDoubleVF-Regular', 
        # preferredFamily, preferredSubFamily
    ),
    MONO_DOUBLE_VF_COLRv1: MD(name=MONO_DOUBLE_VF_COLRv1, isMaster=False,
        familyName='Bitcount Mono Double VF COLRv1', styleName='Regular', fsSelection=REGULAR, italicAngle=0,
        uniqueID='Bitcount Mono Double VF COLRv1 Regular', postscriptName='BitcountVFMonoDoubleCOLRv1-Regular', 
        # preferredFamily, preferredSubFamily
    ),

    PROP_SINGLE_VF: MD(name=PROP_SINGLE_VF, isMaster=False,
        familyName='Bitcount Prop Single VF', styleName='Regular', fsSelection=REGULAR, italicAngle=0,
        uniqueID='Bitcount Prop Single VF Regular', postscriptName='BitcountPropSingleVF-Regular', 
        # preferredFamily, preferredSubFamily
    ),
    PROP_SINGLE_VF_COLRv1: MD(name=PROP_SINGLE_VF_COLRv1, isMaster=False,
        familyName='Bitcount Prop Single VF COLRv1', styleName='Regular', fsSelection=REGULAR, italicAngle=0,
        uniqueID='Bitcount Prop Single VF COLRv1 Regular', postscriptName='BitcountVFPropSingleCOLRv1-Regular', 
        # preferredFamily, preferredSubFamily
    ),
    PROP_DOUBLE_VF: MD(name=PROP_DOUBLE_VF, isMaster=False,
        familyName='Bitcount Prop Double VF', styleName='Regular', fsSelection=REGULAR, italicAngle=0,
        uniqueID='Bitcount Prop Double VF Regular', postscriptName='BitcountPropDoubleVF-Regular', 
        # preferredFamily, preferredSubFamily
    ),
    PROP_DOUBLE_VF_COLRv1: MD(name=PROP_DOUBLE_VF_COLRv1, isMaster=False,
        familyName='Bitcount Prop Double VF COLRv1', styleName='Regular', fsSelection=REGULAR, italicAngle=0,
        uniqueID='Bitcount Prop Double VF COLRv1 Regular', postscriptName='BitcountVFPropDoubleCOLRv1-Regular', 
        # preferredFamily, preferredSubFamily
    ),
}

# Collection of pixel shapes for every design space configuration
VARIATION_PIXELS: MD(ufoName=VARIATION_PIXELS)
