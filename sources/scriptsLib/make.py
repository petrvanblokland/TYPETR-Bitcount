# -*- coding: UTF-8 -*-
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

def deleteUFOs(path):
    """Delete all UFOs in this directory. Faster than removing them one by one."""
    os.system('rm -r %s*.ufo' % path)

def copyMasters(srcPath, variant):
    """Copy the Bitcount masters into MASTERS_PATH, alther their name an fill in the pixels
    shape at that location in the design space.
    """
    # Make the local _masters/ path. Note that this directory does not commit to Github.
    print('--- Cleaning/creating directories in _masters/')
    if not os.path.exists(srcPath):
        print('... Make %s folder' % srcPath)
        os.mkdir(srcPath)
    for masterPath in MASTER_PATHS:
        if variant.lower() in masterPath: # Create variant directories, if not existing
            if not os.path.exists(masterPath):
                os.mkdir(masterPath)
            # Remove old UFO masters one by one in case they are here
            deleteUFOs(masterPath)

    # Open the pixel font, as lead for the masters that need to be generated.
    print('--- Copy %d location masters (wght=3, italic=2, open=2, shape=12)' % len(PIXEL_DATA))
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

def isRoboFont():
    try:
        from mojo.roboFont import AllFonts, OpenFont
        return True
    except ModuleNotFoundError: # Not in RoboFont
        pass
    return False

def openFont(nameOrPath, showInterface=False):
    """
    Open a font defined by the name of path. If the font is already open
    in RoboFont, then answer it.
    """
    if nameOrPath.endswith('.otf') or nameOrPath.endswith('.ttf'):
        from fontTools.ttLib.ttFont import TTFont
        return TTFont(nameOrPath)

    if isRoboFont():
        from mojo.roboFont import AllFonts, OpenFont
        for f in AllFonts():
            if nameOrPath == f.info.familyName or f.path.endswith(nameOrPath):
                return f
        assert os.path.exists(nameOrPath)
        try:
            f = OpenFont(nameOrPath, showInterface=False)
        except:
            f = OpenFont(nameOrPath, showUI=False)
        if showInterface:
            f.openInterface()
        return f
        
    # Else not in RoboFont, use plain fontParts instead
    from fontParts.fontshell.font import RFont
    #print('RFONT', nameOrPath) 
    return RFont(nameOrPath, showInterface=showInterface)

def copyUFO(srcPath, dstPath):
    """Copy the UFO in srcPath to dstPath (directory or UFO name).
    Make sure they are not equal and that the srcPath indeed is 
    has a ufo extension.
    """
    assert os.path.exists(srcPath) and srcPath.endswith('.ufo'), ('Wrong source path %s' % srcPath)
    if os.path.exists(dstPath):
        assert os.path.isdir(dstPath) or dstPath.endswith('.ufo'), ('Wrong existing destination path %s' % dstPath)
    else:
        assert dstPath.endswith('.ufo'), ('Wrong destination path %s' % dstPath)
    shutil.copytree(srcPath, dstPath)

def copyGlyph(srcFont, glyphName, dstFont=None, dstGlyphName=None, copyUnicode=True):
    """If dstFont is omitted, then the dstGlyphName (into the same font) should be defined.
    If dstGlyphName is omitted, then dstFont (same glyph into another font) should be defined.
    Note that this also overwrites/copies the anchors.
    """
    if dstFont is None:
        dstFont = srcFont
    if dstGlyphName is None:
        dstGlyphName = glyphName
    assert srcFont != dstFont or glyphName != dstGlyphName, ('### Either dstFont or dstGlyphName should be defined.')
    assert glyphName in srcFont, ('### Glyph /%s does not exist source font "%s"' % (glyphName, srcFont.path))
    #print('@@@', glyphName, dstGlyphName, dstGlyphName in dstFont)
    #print('... Copy pixel /%s to /%s to' % (glyphName, dstGlyphName), dstFont.path)
    srcGlyph = srcFont[glyphName]
    #if not PIXEL_NAME in dstFont:
    #    dstFont.newGlyph(PIXEL_NAME)
    #print('---', srcGlyph.name)
    #dstFont.insertGlyph(srcGlyph, name=dstGlyphName)
    dstFont[dstGlyphName] = srcGlyph
    assert dstGlyphName in dstFont, ('### Glyph /%s does not exist destination font "%s"' % (dstGlyphName, dstFont.path))
    g = dstFont[dstGlyphName]
    #print('@@1', glyphName, PIXEL_NAME, dstGlyphName in dstFont)
    g.changed()
    return g
    #return dstFont[dstGlyphName]
  
def makePixelMasters(variant):
    """Copy the right pixels shapes in the copied _masters/* master ufo files."""
    print('--- Set pixel shape of %d masters' % len(PIXEL_DATA))
    pixels = openFont(UFO_PATH + VARIATION_PIXELS)
    for masterName, md in MASTERS_DATA.items():
        if md.variant == variant:
            for pName, pd in PIXEL_DATA.items():
                ufoName = getMasterName(md, pd)
                dstPath = md.path + ufoName
                dst = openFont(dstPath)
                # Copy the pixel shape to this axis/variant master
                copyGlyph(pixels, pName, dst, PIXEL_NAME)
                assert PIXEL_NAME in dst
                dst.info.familyName = md.familyName
                dst.info.styleName = md.styleName % pName
                dst.save()
                dst.close()
    pixels.close()


def makeDesignSpaceFiles(axisCount, variant):
    """Dynamic generation of the design space file for this number of axes and this variant"""
    xml = []
    for pName, pd in PIXEL_DATA.items():
        pass
        #print(pName, pd)
    # TBD: Make dynamic designspace files here.


