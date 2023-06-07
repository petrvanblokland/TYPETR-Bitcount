# -*- coding: UTF-8 -*-
#
#   Making the separate Bitcount masters, with the pixel shapes filled in.
#
import os, shutil
import codecs
import ufoLib2

from ufo2ft.constants import COLOR_LAYERS_KEY, COLOR_PALETTES_KEY

from scriptsLib import *
from scriptsLib.glyphData import PIXEL_DATA, DEFAULT_PIXEL_NAME # Data of all pixel glyphs
from scriptsLib.masterData import MASTERS_DATA

BUILD = 9

def getMasterName(md, pd):
    """Calculate the master name from the master data and pixel data location."""
    return f'{BITCOUNT}_{md.variant}_{md.stem}-wght{pd.wght}_OPEN{pd.OPEN}_SHPE{pd.SHPE}_slnt{pd.slnt}.ufo'

def getFamilyName(md):
    return f'{BITCOUNT} {md.variant} {md.stem}'

def getStyleName(pd):
    return f'wght{pd.wght} OPEN{pd.OPEN} SHPE{pd.SHPE} slnt{pd.slnt}'

def deleteUFOs(path):
    """Delete all UFOs in this directory. Faster than removing them one by one."""
    os.system('rm -r %s*.ufo' % path)

def copyMasters(dsName, dsParams, subsetAsTest=False):
    """Copy the Bitcount masters into MASTERS_PATH, alther their name an fill in the pixels
    shape at that location in the design space.
    Then add the COLRv1 layers in the f.lib.
    If subsetAsTest is True, then copy from a source UFO with a small sybset of glyphs.
    """
    # Make the local _masters/ path. Note that this directory does not commit to Github.
    print('... Cleaning/creating directories in _masters/')
    if not os.path.exists(MASTERS_PATH):
        print('... Make %s folder' % MASTERS_PATH)
        os.mkdir(MASTERS_PATH)
    ufoPath = dsParams['ufoPath']    
    for masterPath in MASTER_PATHS:
        if not os.path.exists(ufoPath):
            os.mkdir(ufoPath)
        else:
            # Remove old UFO masters one by one in case they are here
            deleteUFOs(ufoPath)

    # Copy pixels from this UFO.
    pixels = openFont(UFO_PATH + VARIATION_PIXELS)

    # Open the pixel font, as lead for the masters that need to be generated.
    masterName = dsParams['masterName']
    md = MASTERS_DATA[masterName]

    # In case of fast susbest compiling, use different source UFO
    if subsetAsTest:
        ufoDirPath = UFO_TEST_PATH
    else:
        ufoDirPath = UFO_PATH

    print('... Copy %s %d location masters (wght=3, open=2, shape=12, slanted=2)' % (masterName, len(PIXEL_DATA)))
    for pName, pd in PIXEL_DATA.items():
        if pd.slnt:
            ufoName = md.italicName
        else:
            ufoName = md.ufoName
        dstName = getMasterName(md, pd) # Calculate master name from master data and pixel data
        dstPath = md.path + dstName
        if not os.path.exists(dstPath):
            print('    ... Make master %s' % dstName)
            srcPath = ufoDirPath + ufoName
            if pd.SHPE or pd.OPEN or pd.wght != wght_DEF: # Only copy pixels, this can be sparse
                dst = ufoLib2.Font()
            else:
                copyUFO(srcPath, dstPath)
                dst = ufoLib2.Font.open(dstPath)
            dst.info.familyName = getFamilyName(md)
            dst.info.styleName = getStyleName(pd)
            copyGlyph(pixels, pName, dst, PIXEL_NAME)
            dst.save(dstPath, overwrite=True)
            dst.close()

    pixels.close()

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
    #print('RFONT', nameOrPath) 
    return ufoLib2.Font.open(nameOrPath)

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
    return g
    #return dstFont[dstGlyphName]
  
def makeDesignSpaceFile(dsName, dsParams):
    """Dynamic generation of the design space file for this number of axes and this variant.
    The <sources> definition has two parts, it's actually a merge of two independent design spaces.
    The main part is the “traditional” definition of the shapes of the pixels in 4 axes.
    The COLRv1 part defind the scale and relative position (for each pixel) of the color
    layers that use the main pixels as mask.
    """
    print('... Make design space %s' % dsName)
    for pName, pd in PIXEL_DATA.items():
        pass
        #print(pName, pd)

    fin = codecs.open(DESIGNSPACE_TEMPLATE_PATH, 'r', encoding='UTF-8')
    template = fin.read()
    fin.close()

    # Define the dictionary of values that are substituted in the Bitcount_Template.designspace file.
    axisParams = dict(sources='', instances='') # XML for the <sources> and <instances> will be filled here.
    axisParams['title'] = 'Design space of Bitcount %(variant)s %(stem)s'
    axisParams['stem'] = stem = dsParams['stem'] # Stem width in pixels: Single or Double
    axisParams['variant'] = variant = dsParams['variant'] # Variant of VF: Grid, Mono or Prop

    # Main axis values
    axisParams['wghtMin'] = WGHT_MIN
    axisParams['wghtDef'] = WGHT_DEF
    axisParams['wghtMax'] = WGHT_MAX
    axisParams['OPENMin'] = OPEN_MIN # Also default for the open axis
    axisParams['OPENMax'] = OPEN_MAX
    axisParams['SHPEMin'] = SHPE_MIN # Also default for the shape axis
    axisParams['SHPEMax'] = SHPE_MAX
    axisParams['slntMin'] = SLNT_MIN # Also default for the slant axis
    axisParams['slntMax'] = SLNT_MAX

    # COLRv1 layer #1 axis values
    axisParams['LR1SMin'] = SMIN # Scale
    axisParams['LR1SDef'] = SDEF
    axisParams['LR1SMax'] = SMAX
    axisParams['LR1XMin'] = LMIN # Horizontal position
    axisParams['LR1XDef'] = LDEF
    axisParams['LR1XMax'] = LMAX
    axisParams['LR1YMin'] = LMIN
    axisParams['LR1YDef'] = LDEF
    axisParams['LR1YMax'] = LMAX

    # COLRv1 layer #2 axis values   
    axisParams['LR2SMin'] = SMIN # Scale
    axisParams['LR2SDef'] = SDEF
    axisParams['LR2SMax'] = SMAX
    axisParams['LR2XMin'] = LMIN # Horizontal position
    axisParams['LR2XDef'] = LDEF
    axisParams['LR2XMax'] = LMAX
    axisParams['LR2YMin'] = LMIN # Vertical position
    axisParams['LR2YDef'] = LDEF
    axisParams['LR2YMax'] = LMAX

    # Layer axes are independent from main Bitcount shape axes
    for wght in (WGHT_MIN, WGHT_DEF, WGHT_MAX):
        # minValue is the same as default
        for OPEN in (OPEN_MIN, OPEN_MAX):
            # minValue is the same as default
            for SHPE in SHAPES:
                # minValue is the same as default
                for slnt in (SLNT_MIN, SLNT_MAX):
                    if DEFAULT_LOCATION == (wght, OPEN, SHPE, slnt):
                        info = '<info copy="1"/>'
                    else: 
                        info = ''
                    path = f'_masters/{variant}-{stem}/Bitcount_{variant}_{stem}-wght{wght}_OPEN{OPEN}_SHPE{SHPE}_slnt{slnt}.ufo'

                    axisParams['sources'] += f"""
        <source familyname="Bitcount {variant} {stem}" 
            filename="{path}" 
            name="Bitcount {variant} {stem}" 
            stylename="wght{wght} OPEN{OPEN} SHPE{SHPE} slnt{slnt}">
            <location>
                <!-- Main pixel shape axes, final names to be defined -->
                <dimension name="Weight" xvalue="{wght}"/>
                <dimension name="Open" xvalue="{OPEN}"/>
                <dimension name="Shape" xvalue="{SHPE}"/>
                <dimension name="Slanted" xvalue="{slnt}"/>
            </location>
            {info}
        </source>
            """

    xml = template % axisParams
    fds = codecs.open(dsName, 'w', encoding='UTF-8')
    fds.write(xml)
    fds.close()

def addCOLRv1toVF(vfPath):
    dstPath = vfPath.replace('.ttf', '_COLRv1.ttf')
    print('--- Adding COLORv1 pixels to', dstPath)
    cmd = (f'paintcompiler -o {dstPath} '
           f'--add-axis LR1X:{LMIN}:{LDEF}:{LMAX}:Layer1-X '
           f'--add-axis LR1Y:{LMIN}:{LDEF}:{LMAX}:Layer1-Y '
           f'--add-axis LR1S:{SMIN}:{SDEF}:{SMAX}:Layer1-Scale '
           f'--add-axis LR2X:{LMIN}:{LDEF}:{LMAX}:Layer2-X '
           f'--add-axis LR2Y:{LMIN}:{LDEF}:{LMAX}:Layer2-Y '
           f'--add-axis LR2S:{SMIN}:{SDEF}:{SMAX}:Layer2-Scale '
           '--paints scriptsLib/colrv1.py '+vfPath)
    print(cmd)
    os.system(cmd)
