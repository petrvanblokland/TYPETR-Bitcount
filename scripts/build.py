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
import sys

sys.path.append(".")

from scriptsLib.make import *

if 1:
    MAKE_DESIGNSPACES = True # 
    SUBSET_AS_TEST = False # If True, then compile with a subset of only a couple of glyph (whithout features)
    COPY_MASTERS = True # Copy master to location. Set the right pixel shape. Add COLRV1 pixel layers to each glyph.
    SET_GLYPH_ORDER = True
    MAKE_STAT = True
    MAKE_UFO = True
    MAKE_TTF = True
    MAKE_VF = True
    ADD_COLRV1 = True
    USE_PRODUCTION_NAMES = False
else:
    MAKE_DESIGNSPACES = True 
    SUBSET_AS_TEST = False # If True, then compile with a subset of only a couple of glyph (whithout features)
    COPY_MASTERS = True # Copy master to location. Set the right pixel shape. Add COLRV1 pixel layers to each glyph.
    SET_GLYPH_ORDER = False
    MAKE_STAT = False
    MAKE_UFO = False
    MAKE_TTF = False
    MAKE_VF = False
    ADD_COLRV1 = True
    USE_PRODUCTION_NAMES = False

for dsName, dsParams in DESIGN_SPACES.items():
    print('---', dsName)

    if MAKE_DESIGNSPACES:
        # For all 6 design spaces, generate the OTF/TTF/VF
        # Auto generate the design space file for this variant.
        # This is fast, we can always do all of them.
        makeDesignSpaceFile(dsName, dsParams)

    if dsName not in [
        'Bitcount_Grid_Single4.designspace',
        'Bitcount_Grid_Double4.designspace',
        'Bitcount_Mono_Single4.designspace',
        'Bitcount_Mono_Double4.designspace',
        'Bitcount_Prop_Single4.designspace',
        'Bitcount_Prop_Double4.designspace',
    ]:
        print('### Skipping design space', dsName)
        continue

    if COPY_MASTERS:
        print('--- Copy UFO masters')
        # Copy the ufo/ masters to _masters/<variant>/<UFOs> for every master and apply the 
        # right file name based on location  and variant
        copyMasters(dsName, dsParams, SUBSET_AS_TEST)

    if MAKE_VF:
        print('--- Make variable fonts')
        # Compile calibrated UFOs masters/ into vf/ variable font
        if not os.path.exists(VF_PATH):
            os.makedirs(VF_PATH)
        vfPath = VF_PATH + dsName.replace('.designspace', '-%03d.ttf' % BUILD)
        cmd = 'fontmake -o variable -m %s --output-path %s' % (dsName, vfPath)
        print('...', cmd)
        os.system(cmd)
        
        if 0:
            if USE_PRODUCTION_NAMES:
                cmd += ' --use_production_names'
            else:
                cmd += ' --no-production-names'
            print('---', cmd)
            print('--- Fixing TTF name tables')
            fixTTFNameTables(VF_PATH, NAME_TABLES)
            os.system(cmd)

            cmd = 'statmake --designspace %s --stylespace %s %s' % (dsName, STYLE_SPACE, vfPath)
            print('...', cmd)
            if MAKE_STAT:
                os.system(cmd)

    if ADD_COLRV1:
        vfPath = VF_PATH + dsName.replace('.designspace', '-%03d.ttf' % BUILD)
        print('... Add COLRv1 to', vfPath)
        addCOLRv1toVF(vfPath)

print('Done')


