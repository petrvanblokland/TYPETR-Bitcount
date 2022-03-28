#
#   Making the separate Bitcount masters, with the pixel shapes filled in.
#
import os
from scriptsLib import *
from scriptsLib.glyphData import PIXEL_DATA # Data of all pixel glyphs
from scriptsLib.masterData import MASTERS_DATA

def getMasterName(md, pd):
    """Calculate the master name from the master data and pixel data location."""
    return '%s%s_%s_OPEN%d_SHPE%d_slnt%d_wght%d.ufo' % (
        BITCOUNT, md.variant, md.stem, pd.OPEN, pd.SHPE, pd.slnt, pd.wght)

def copyMasters(variant):
    """Copy the Bitcount masters into MASTERS_PATH, alther their name an fill in the pixels
    shape at that location in the design space.
    """
    # Make the local masters path. Note that this directory does not commit to Github.
    print('--- Cleaning/creating directories in _masters/')
    if not os.path.exists(MASTERS_PATH):
        # Make _masters/ folder
        os.mkdir(MASTERS_PATH)
    for masterPath in MASTER_PATHS:
        if variant.lower() in masterPath:
            if not os.path.exists(masterPath):
                os.mkdir(masterPath)
            # Remove old UFO masters in case they are here
            for fileName in os.listdir(masterPath):
                if fileName.endswith('.ufo'):
                    deleteUFO(masterPath + fileName)

    # Open the pixel font, as lead for the masters that need to be generated.
    print('--- Copy location masters')
    for masterName, md in MASTERS_DATA.items():
        if md.variant == variant:
            for pName, pd in PIXEL_DATA.items():
                if pd.slnt: # Italic, then take the related italic ufo instead to copy from
                    srcPath = UFO_PATH + md.italicName
                else:
                    srcPath = UFO_PATH + masterName
                # Bitcount generated masters, that include location-bound pixel shape, typically is called
                # BitcountMono_DoubleCircleSquare_LINE0_OPEN0_SHPE0_slnt0_wght500.ufo
                ufoName = getMasterName(md, pd) # Calculate master name from master data and pixel data
                dstPath = md.path + ufoName
                copyUFO(srcPath, dstPath)

def makePixelMasters(variant):
    """Copy the right pixels in the copied _masters/* master ufo files."""
    print('--- Making pixel masters')
    pixels = openFont(UFO_PATH + VARIATION_PIXELS)
    for masterName, md in MASTERS_DATA.items():
        if md.variant == variant:
            for pName, pd in PIXEL_DATA.items():
                ufoName = getMasterName(md, pd)
                dstPath = md.path + ufoName
                dst = openFont(dstPath)
                copyGlyph(pixels, pName, dst, PIXEL_NAME)
                assert PIXEL_NAME in dst
                dst.save()
                dst.close()
    pixels.close()
    

def makeDesignSpaceFiles(axisCount, variant):
    xml = []
    for pName, pd in PIXEL_DATA.items():
        pass
        #print(pName, pd)
    # TBD: Make dynamic design space files here.