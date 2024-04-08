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

from scriptsLib import DESIGN_SPACES, MASTERS_PATH, VF_PATH
from scriptsLib.make import addCOLRv1toVF, copyMasters, makeDesignSpaceFile

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
    makeDesignSpaceFile(dsPath, dsParams)

    print("--- Copy UFO masters")
    # Copy the ufo/ masters to _masters/<variant>/<UFOs> for every master and apply the
    # right file name based on location  and variant
    copyMasters(dsName, dsParams)

    print("--- Make variable fonts")
    vfPath = VF_PATH + dsParams.vfName  # Regular VF name
    # Compile calibrated UFOs masters/ into vf/ variable font
    cmd = ["fontmake", "-o", "variable", "-m", dsPath, "--output-path", vfPath]
    print("...", " ".join(cmd))
    subprocess.run(cmd, check=True)

    print("... Add COLRv1 to", vfPath)
    colorPath = VF_PATH + dsParams.colorVfName  # Target color VF name
    addCOLRv1toVF(vfPath, colorPath)

    # Add STAT table to the freshly generate VF for all 10 axes
    cmd = "statmake --stylespace %s --designspace %s %s" % (
        styleSpacePath,
        dsPath,
        vfPath,
    )
    print("... statMake VF", cmd)
    subprocess.run(cmd, shell=True, check=True)

    cmd = "statmake --stylespace %s --designspace %s %s" % (
        styleSpaceCOLRv1Path,
        dsPath,
        colorPath,
    )
    print("... statMake COLRv1 VF", cmd)
    subprocess.run(cmd, shell=True, check=True)
