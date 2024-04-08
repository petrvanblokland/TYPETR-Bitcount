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

sys.path.insert(0, ".")

from scriptsLib import COLOR_AXES, DESIGN_SPACES, MASTERS_PATH, MONO_AXES, VF_PATH
from scriptsLib.make import addCOLRv1toVF, copyMasters, makeDesignSpaceFile

for dsName, dsParams in DESIGN_SPACES.items():
    print("---", dsName)
    dsPath = os.path.join(MASTERS_PATH, dsName)
    styleSpacePath = "sources/Bitcount.stylespace"
    styleSpaceCOLRv1Path = "sources/Bitcount_COLRv1.stylespace"

    # For all 6 design spaces, generate the OTF/TTF/VF
    # Auto generate the design space file for this variant.
    # This is fast, we can always do all of them.
    makeDesignSpaceFile(dsPath, dsParams)

    if dsName not in [
        "Bitcount_Grid_Single4.designspace",
        "Bitcount_Grid_Double4.designspace",
        "Bitcount_Mono_Single4.designspace",
        "Bitcount_Mono_Double4.designspace",
        "Bitcount_Prop_Single4.designspace",
        "Bitcount_Prop_Double4.designspace",
    ]:
        print("### Skipping design space", dsName)
        continue

    print("--- Copy UFO masters")
    # Copy the ufo/ masters to _masters/<variant>/<UFOs> for every master and apply the
    # right file name based on location  and variant
    copyMasters(dsName, dsParams)

    axis_suffix = ",".join(sorted(MONO_AXES))
    color_axis_suffix = ",".join(sorted(COLOR_AXES) + sorted(MONO_AXES))

    vfNames = (
        {  # Translate design space name into VF output name as requested by Google.
            "Bitcount_Grid_Single4.designspace": (
                f"BitcountGridSingle[{axis_suffix}].ttf",
                f"BitcountGridSingle[{color_axis_suffix}].ttf",
            ),
            "Bitcount_Grid_Double4.designspace": (
                f"BitcountGridDouble[{axis_suffix}].ttf",
                f"BitcountGridDouble[{color_axis_suffix}].ttf",
            ),
            "Bitcount_Mono_Single4.designspace": (
                f"BitcountSingle[{axis_suffix}].ttf",
                f"BitcountSingle[{color_axis_suffix}].ttf",
            ),
            "Bitcount_Mono_Double4.designspace": (
                f"Bitcount[{axis_suffix}].ttf",
                f"Bitcount[{color_axis_suffix}].ttf",
            ),
            "Bitcount_Prop_Single4.designspace": (
                f"BitcountPropSingle[{axis_suffix}].ttf",
                f"BitcountPropSingle[{color_axis_suffix}].ttf",
            ),
            "Bitcount_Prop_Double4.designspace": (
                f"BitcountPropDouble[{axis_suffix}].ttf",
                f"BitcountPropDouble[{color_axis_suffix}].ttf",
            ),
        }
    )
    # vfPath = VF_PATH + dsName.replace('.designspace', f'[{axis_suffix}].ttf')
    vfPath = VF_PATH + vfNames[dsName][0]  # Regular VF name

    print("--- Make variable fonts")
    # Compile calibrated UFOs masters/ into vf/ variable font
    if not os.path.exists(VF_PATH):
        os.makedirs(VF_PATH)
    cmd = ["fontmake", "-o", "variable", "-m", dsPath, "--output-path", vfPath]
    print("...", " ".join(cmd))
    subprocess.run(cmd, check=True)

    # if FIX_NAME_TABLES:
    #    fixTTFNameTables('vf/', MASTERS_DATA)

    colorPath = VF_PATH + vfNames[dsName][1]  # Target color VF name
    print("... Add COLRv1 to", vfPath)
    addCOLRv1toVF(vfPath, colorPath)

    # Add STAT table to the freshly generate VF for all 10 axes
    cmd = "statmake --stylespace %s --designspace %s %s" % (
        styleSpacePath,
        dsPath,
        vfPath,
    )
    print("... statMake VF", cmd)
    os.system(cmd)

    cmd = "statmake --stylespace %s --designspace %s %s" % (
        styleSpaceCOLRv1Path,
        dsPath,
        colorPath,
    )
    print("... statMake COLRv1 VF", cmd)
    os.system(cmd)
