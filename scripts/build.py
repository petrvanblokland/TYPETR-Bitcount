# -*- coding: UTF-8 -*-
#
#   Main build script for TYPETR Bitcount
#   Build a variants of Bitcount VF/TTF/OTF from here.
#   Optionally add COLRv1 pixels to the VF.
#
#   Building process
#
#
import os
import subprocess
import sys

import yaml

sys.path.insert(0, ".")

from scriptsLib import DESIGN_SPACES, MASTERS_PATH, VF_PATH, STAT_LOCATIONS
from scriptsLib.make import (
    addCOLRv1toVF,
    copyMasters,
    makeDesignSpaceFile,
    getFamilyName,
)

GOOGLEFONTS = True

styleSpacePath = "sources/Bitcount.stylespace"
styleSpaceCOLRv1Path = "sources/Bitcount_COLRv1.stylespace"

if not os.path.exists(VF_PATH):
    os.makedirs(VF_PATH)


for dsName in [
    "Bitcount_Grid_Single4.designspace",
    "Bitcount_Grid_Double4.designspace",
    "Bitcount_Mono_Single4.designspace",
    "Bitcount_Mono_Double4.designspace",
    "Bitcount_Prop_Single4.designspace",
    "Bitcount_Prop_Double4.designspace",
]:

    dsParams = DESIGN_SPACES[dsName]

    print("---", dsName)
    dsPath = os.path.join(MASTERS_PATH, dsName)

    # For all 6 design spaces, generate the OTF/TTF/VF
    # Auto generate the design space file for this variant.
    # This is fast, we can always do all of them.
    makeDesignSpaceFile(dsPath, dsParams, googlefonts=GOOGLEFONTS)

    print("--- Copy UFO masters")
    # Copy the ufo/ masters to _masters/<variant>/<UFOs> for every master and apply the
    # right file name based on location  and variant
    copyMasters(dsParams, googlefonts=GOOGLEFONTS)

    print("--- Make variable fonts")
    vfPath = VF_PATH + dsParams.vfName  # Regular VF name
    # Compile calibrated UFOs masters/ into vf/ variable font
    cmd = ["fontmake", "-o", "variable", "-m", dsPath, "--output-path", vfPath]
    print("...", " ".join(cmd))
    subprocess.run(cmd, check=True)

    if GOOGLEFONTS:
        from gftools.stat import gen_stat_tables_from_config
        from fontTools.ttLib import TTFont

        stat = yaml.safe_load(open("sources/stat.yaml"))
        ttfont = TTFont(vfPath)
        gen_stat_tables_from_config(stat, [ttfont], locations=STAT_LOCATIONS)
        ttfont.save(vfPath)
    else:
        # Add STAT table to the freshly generate VF for all 10 axes
        cmd = "statmake --stylespace %s --designspace %s %s" % (
            styleSpacePath,
            dsPath,
            vfPath,
        )
        print("... statMake VF", cmd)
        subprocess.run(cmd, shell=True, check=True)

    if GOOGLEFONTS:
        print("... Run Google Fonts fixes", cmd)
        subprocess.run(
            ["gftools", "fix-family", "--inplace", vfPath],
            check=True,
        )

    print("... Add COLRv1 to", vfPath)
    colorPath = VF_PATH + dsParams.colorVfName  # Target color VF name
    addCOLRv1toVF(vfPath, colorPath)

    if GOOGLEFONTS:
        oldColorPath = colorPath
        colorPath = colorPath.replace("[", "Ink[")  # Filename
        newFamilyName = dsParams.familyName + " Ink"  # Family name
        cmd = [  # Avoid shell globbing problems
            "gftools-rename-font",
            "--out",
            colorPath,
            oldColorPath,
            newFamilyName,
            "--just-family",
        ]
        print("... rename font", cmd)
        subprocess.run(cmd, check=True)
        # Remove the old font
        os.remove(oldColorPath)

    if GOOGLEFONTS:
        from gftools.stat import gen_stat_tables_from_config
        from fontTools.ttLib import TTFont

        stat = yaml.safe_load(open("sources/stat-color.yaml"))
        ttfont = TTFont(colorPath)
        gen_stat_tables_from_config(stat, [ttfont], locations=STAT_LOCATIONS)
        ttfont.save(colorPath)
    else:
        cmd = "statmake --stylespace %s --designspace %s %s" % (
            styleSpaceCOLRv1Path,
            dsPath,
            colorPath,
        )
        print("... statMake COLRv1 VF", cmd)
        subprocess.run(cmd, shell=True, check=True)
