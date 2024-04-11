# -*- coding: UTF-8 -*-
#
#   Making the separate Bitcount masters, with the pixel shapes filled in.
#
import os, shutil
import ufoLib2
import subprocess

from gftools.constants import OFL_LICENSE_INFO
from gftools.util.google_fonts import _KNOWN_WEIGHTS
from fontTools.designspaceLib import (
    DesignSpaceDocument,
    SourceDescriptor,
    InstanceDescriptor,
)
from fontTools.feaLib.parser import Parser
from fontTools.feaLib import ast

from scriptsLib import (
    BITCOUNT,
    DEFAULT_LOCATION,
    DESIGNSPACE_TEMPLATE_PATH,
    ELSH_DEF,
    ELXP_DEF,
    ELXP_MAX,
    ELXP_MIN,
    GF_COPYRIGHT,
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
    slnt_MAX,
    slnt_MIN,
    slnt_DEF,
    SMAX,
    SMIN,
    UFO_PATH,
    VARIATION_PIXELS,
    wght_DEF,
    wght_MAX,
    wght_MIN,
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


def copyMasters(dsParams, googlefonts=False):
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
        os.system("rm -r %s*.ufo" % ufoPath)

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
            dst[PIXEL_NAME] = pixels[pName]
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
                    dst[POST_FIX + elementName] = eFont[elementName]
            if googlefonts:
                dst.info.openTypeNameLicense = OFL_LICENSE_INFO
                dst.info.copyright = GF_COPYRIGHT
                if dst.info.familyName == "Bitcount Mono Double":
                    dst.info.familyName = "Bitcount"
                    dst.info.styleMapFamilyName = "Bitcount"
                    dst.info.postscriptFontName = "Bitcount-Regular"
                    dst.info.openTypeNamePreferredFamilyName = "Bitcount"
                dst.info.openTypeOS2WinAscent = 1000
                dst.info.openTypeOS2TypoLineGap = 0
                dst.info.openTypeOS2TypoAscender = 840
                dst.info.openTypeOS2TypoDescender = -360
                dst.info.openTypeNameDescription = ""
                if "space" in dst:
                    dst["uni00A0"] = dst["space"].copy("uni00A0")
                    dst["uni00A0"].unicode = 0x00A0
                    dst.info.styleName = "Regular"
                dst.info.openTypeOS2Type = []
                dst.info.openTypeOS2Selection = [7]

            dst.save(dstPath, overwrite=True)
            dst.close()

    pixels.close()


def makeDesignSpaceFile(dsName, dsParams, googlefonts=False):
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

    familyName = f"Bitcount {variant} {stem}"
    if familyName == "Bitcount Mono Double":
        familyName = "Bitcount"

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
    if googlefonts:
        weightInstances = {v: k for k, v in _KNOWN_WEIGHTS.items() if k}
        weightInstances[100] = "Thin"

    # Layer axes are independent from main Bitcount shape axes

    for wght in (wght_MIN, wght_DEF, wght_MAX):
        # minValue is the same as default
        for ELXP in (ELXP_MIN, ELXP_MAX):
            # minValue is the same as default
            for ELSH in SHAPES:
                # minValue is the same as default
                for slnt in (slnt_MIN, slnt_MAX):
                    path = f"{variant}-{stem}/Bitcount_{variant}_{stem}-wght{wght}_ELXP{ELXP}_ELSH{ELSH}_slnt{slnt}.ufo"
                    source = SourceDescriptor(
                        filename=path,
                        familyName=familyName,
                        name=familyName,
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
                for slnt in (slnt_MIN, slnt_MAX):
                    wName = weightName
                    stylename = f"{wName} ELXP {ELXP} ELSH{ELSH} slnt{slnt}"
                    if ELXP == ELXP_DEF and ELSH == ELSH_DEF:
                        stylename = wName
                        if slnt == slnt_MIN:
                            stylename += " Italic"
                        if stylename == "Regular Italic":
                            stylename = "Italic"
                    elif (
                        googlefonts
                    ):  # For GF builds, only add default wght/slnt instances
                        continue

                    template.instances.append(
                        InstanceDescriptor(
                            familyName=familyName,
                            name=familyName,
                            styleName=stylename,
                            location={
                                "Weight": wght,
                                "Element Expansion": ELXP,
                                "Element Shape": ELSH,
                                "Slant": slnt,
                            },
                        )
                    )

    # Add cursive axis rules
    #
    features = Parser(UFO_PATH + f"Bitcount_{variant}_{stem}.ufo/features.fea").parse()
    # Find ss08
    ss08 = [
        s
        for s in features.statements
        if isinstance(s, ast.FeatureBlock) and s.name == "ss08"
    ][0]
    for statement in ss08.statements:
        if not isinstance(statement, ast.SingleSubstStatement):
            continue
        not_italic = statement.glyphs[0].glyphSet()
        italic = statement.replacements[0].glyphSet()
        for src, dest in zip(not_italic, italic):
            template.rules[0].subs.append((src, dest))
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
