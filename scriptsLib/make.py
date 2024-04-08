# -*- coding: UTF-8 -*-
#
#   Making the separate Bitcount masters, with the pixel shapes filled in.
#
import os, shutil
import codecs
import ufoLib2
import subprocess

from fontTools.designspaceLib import (
    DesignSpaceDocument,
    SourceDescriptor,
    InstanceDescriptor,
)

from scriptsLib import (
    BITCOUNT,
    DEFAULT_LOCATION,
    DESIGNSPACE_TEMPLATE_PATH,
    ELSH_MAX,
    ELSH_MIN,
    ELXP_MAX,
    ELXP_MIN,
    LAYER_ELEMENTS,
    LAYER_ELEMENTS_ITALIC,
    LDEF,
    LMAX,
    LMIN,
    MASTERS_PATH,
    PIXEL_NAME,
    POST_FIX,
    SDEF,
    SHAPES,
    SLNT_MAX,
    SLNT_MIN,
    SMAX,
    SMIN,
    UFO_PATH,
    VARIATION_PIXELS,
    WGHT_DEF,
    WGHT_MAX,
    WGHT_MIN,
    wght_DEF,
)
from scriptsLib.glyphData import (
    PIXEL_DATA,
)  # Data of all pixel glyphs
from scriptsLib.masterData import MASTERS_DATA

ITALIC_ANGLE = -7.9696100000  # Italic angle to make exact 14:100 ratio.
BUILD = 11


def getMasterName(md, pd):
    """Calculate the master name from the master data and pixel data location."""
    return f"{BITCOUNT}_{md.variant}_{md.stem}-wght{pd.wght}_ELXP{pd.ELXP}_ELSH{pd.ELSH}_slnt{pd.slnt}.ufo"


def getFamilyName(md):
    return f"{BITCOUNT} {md.variant} {md.stem}"


def getStyleName(pd):
    return f"wght{pd.wght} ELXP{pd.ELXP} ELSH{pd.ELSH} slnt{pd.slnt}"


def deleteUFOs(path):
    """Delete all UFOs in this directory. Faster than removing them one by one."""
    os.system("rm -r %s*.ufo" % path)


def copyMasters(dsName, dsParams):
    """Copy the Bitcount masters into MASTERS_PATH, alther their name an fill in the pixels
    shape at that location in the design space.
    If subsetAsTest is True, then copy from a source UFO with a small sybset of glyphs.
    """
    # Make the local _masters/ path. Note that this directory does not commit to Github.
    print("... Cleaning/creating directories in _masters/")
    if not os.path.exists(MASTERS_PATH):
        print("... Make %s folder" % MASTERS_PATH)
        os.mkdir(MASTERS_PATH)
    ufoPath = dsParams.ufoPath
    if not os.path.exists(ufoPath):
        os.mkdir(ufoPath)
    else:
        # Remove old UFO masters one by one in case they are here
        deleteUFOs(ufoPath)

    # Copy pixels from this UFO.
    pixels = ufoLib2.Font.open(UFO_PATH + VARIATION_PIXELS)
    # Copy COLRv1 mask elements from this UFO.
    elements = ufoLib2.Font.open(UFO_PATH + LAYER_ELEMENTS)
    elementsItalic = ufoLib2.Font.open(UFO_PATH + LAYER_ELEMENTS_ITALIC)

    # Open the pixel font, as lead for the masters that need to be generated.
    md = MASTERS_DATA[dsParams.masterName]
    ufoDirPath = UFO_PATH

    print(
        "... Copy %s %d location masters (wght=3, open=2, shape=12, slanted=2)"
        % (dsParams.masterName, len(PIXEL_DATA))
    )
    for pName, pd in PIXEL_DATA.items():
        if pd.slnt:
            ufoName = md.italicName
        else:
            ufoName = md.ufoName
        dstName = getMasterName(
            md, pd
        )  # Calculate master name from master data and pixel data
        dstPath = md.path + dstName
        if not os.path.exists(dstPath):
            print("    ... Make master %s" % dstName)
            srcPath = ufoDirPath + ufoName
            if (
                pd.ELSH or pd.ELXP or pd.wght != wght_DEF
            ):  # Only copy pixels, this can be sparse
                dst = ufoLib2.Font()
            else:
                shutil.copytree(srcPath, dstPath)
                dst = ufoLib2.Font.open(dstPath)
            dst.info.familyName = getFamilyName(md)
            dst.info.styleName = getStyleName(pd)
            copyGlyph(pixels, pName, dst, PIXEL_NAME)
            # if pd.slnt:
            #    copyGlyph(pixels, '_canvas_i', dst, '_canvas')
            #    copyGlyph(pixels, 'canvas_i', dst, 'canvas')
            # else:
            #    copyGlyph(pixels, '_canvas', dst, '_canvas')
            #    copyGlyph(pixels, 'canvas', dst, 'canvas')
            # Copy the COLRv1 mask pixel glyphs. Roman and italic pixels get copied from their own element source.
            # If this is the default instance, we add the elements too
            dst.info.italicAngle = 0  # Set default angle
            if pd.is_default or pd.slnt:
                if pd.slnt:
                    dst.info.italicAngle = ITALIC_ANGLE
                    eFont = elementsItalic
                else:
                    eFont = elements
                for elementName in eFont.keys():
                    # print('... Copy element', elementName,'to', POST_FIX+elementName)
                    copyGlyph(eFont, elementName, dst, POST_FIX + elementName)
            dst.save(dstPath, overwrite=True)
            dst.close()

    pixels.close()


def copyGlyph(srcFont, glyphName, dstFont=None, dstGlyphName=None):
    """If dstFont is omitted, then the dstGlyphName (into the same font) should be defined.
    If dstGlyphName is omitted, then dstFont (same glyph into another font) should be defined.
    Note that this also overwrites/copies the anchors.
    """
    if dstFont is None:
        dstFont = srcFont
    if dstGlyphName is None:
        dstGlyphName = glyphName
    assert (
        srcFont != dstFont or glyphName != dstGlyphName
    ), "### Either dstFont or dstGlyphName should be defined."
    assert glyphName in srcFont, '### Glyph /%s does not exist source font "%s"' % (
        glyphName,
        srcFont.path,
    )
    # print('@@@', glyphName, dstGlyphName, dstGlyphName in dstFont)
    # print('... Copy pixel /%s to /%s to' % (glyphName, dstGlyphName), dstFont.path)
    srcGlyph = srcFont[glyphName]
    # if not PIXEL_NAME in dstFont:
    #    dstFont.newGlyph(PIXEL_NAME)
    # print('---', srcGlyph.name)
    # dstFont.insertGlyph(srcGlyph, name=dstGlyphName)
    dstFont[dstGlyphName] = srcGlyph
    assert (
        dstGlyphName in dstFont
    ), '### Glyph /%s does not exist destination font "%s"' % (
        dstGlyphName,
        dstFont.path,
    )
    g = dstFont[dstGlyphName]
    # print('@@1', glyphName, PIXEL_NAME, dstGlyphName in dstFont)
    return g
    # return dstFont[dstGlyphName]


def makeDesignSpaceFile(dsName, dsParams):
    """Dynamic generation of the design space file for this number of axes and this variant.
    The <sources> definition has two parts, it's actually a merge of two independent design spaces.
    The main part is the “traditional” definition of the shapes of the pixels in 4 axes.
    The COLRv1 part defind the scale and relative position (for each pixel) of the color
    layers that use the main pixels as mask.
    """
    print("... Make design space %s" % dsName)
    # Read the template file
    template = DesignSpaceDocument.fromfile(DESIGNSPACE_TEMPLATE_PATH)

    stem = dsParams.stem  # Stem width in pixels: Single or Double
    variant = dsParams.variant  # Variant of VF: Grid, Mono or Prop

    weightInstances = {
        200: "Thin",
        300: "Light",
        400: "Regular",
        500: "Medium",
        600: "Semibold",
        700: "Bold",
        800: "Extrabold",
        900: "Black",
    }
    # Layer axes are independent from main Bitcount shape axes
    for wght in (WGHT_MIN, WGHT_DEF, WGHT_MAX):
        # minValue is the same as default
        for ELXP in (ELXP_MIN, ELXP_MAX):
            # minValue is the same as default
            for ELSH in SHAPES:
                # minValue is the same as default
                for slnt in (SLNT_MIN, SLNT_MAX):
                    path = f"{variant}-{stem}/Bitcount_{variant}_{stem}-wght{wght}_ELXP{ELXP}_ELSH{ELSH}_slnt{slnt}.ufo"
                    source = SourceDescriptor(
                        filename=path,
                        familyName=f"Bitcount {variant} {stem}",
                        name=f"Bitcount {variant} {stem}",
                        styleName=f"wght{wght} ELXP{ELXP} ELSH{ELSH} slnt{slnt}",
                        location={
                            "Weight": wght,
                            "Element Expansion": ELXP,
                            "Element Shape": ELSH,
                            "Slant": slnt,
                        },
                    )
                    if DEFAULT_LOCATION == (wght, ELXP, ELSH, slnt):
                        source.copyInfo = True
                    template.sources.append(source)

    for wght, weightName in sorted(weightInstances.items()):
        # minValue is the same as default
        for ELXP in (ELXP_MIN, ELXP_MAX):
            # minValue is the same as default
            for ELSH in SHAPES:
                # minValue is the same as default
                for slnt in (SLNT_MIN, SLNT_MAX):
                    wName = weightName
                    if slnt == SLNT_MAX:
                        wName += " Italic"
                    template.instances.append(
                        InstanceDescriptor(
                            familyName=f"Bitcount {variant} {stem}",
                            name=f"Bitcount {variant} {stem}",
                            styleName=f"wght {wName} ELXP {ELXP} ELSH{ELSH} slnt{slnt}",
                            location={
                                "Weight": wght,
                                "Element Expansion": ELXP,
                                "Element Shape": ELSH,
                                "Slant": slnt,
                            },
                        )
                    )

    template.write(dsName)


def addCOLRv1toVF(vfPath, dstPath):
    print("--- Adding COLORv1 pixels to", dstPath)
    cmd = [
        "paintcompiler",
        "-o",
        dstPath,
        "--add-axis",
        f"SZP1:{SMIN}:{SDEF}:{SMAX}:Size of Paint 1",
        "--add-axis",
        f"XPN1:{LMIN}:{LDEF}:{LMAX}:Horizontal Position of Paint 1",
        "--add-axis",
        f"YPN1:{LMIN}:{LDEF}:{LMAX}:Vertical Position of Paint 1",
        "--add-axis",
        f"SZP2:{SMIN}:{SDEF}:{SMAX}:Size of Paint 2",
        "--add-axis",
        f"XPN2:{LMIN}:{LDEF}:{LMAX}:Horizontal Position of Paint 2",
        "--add-axis",
        f"YPN2:{LMIN}:{LDEF}:{LMAX}:Vertical Position of Paint 2",
        "--paints",
        "scriptsLib/colrv1.py",
        vfPath,
    ]
    print(" ".join(cmd))
    subprocess.run(cmd, check=True)
