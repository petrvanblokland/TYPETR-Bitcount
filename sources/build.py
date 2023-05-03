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

from fontParts.fontshell.font import RFont
from scriptsLib.make import *

if 0:
    MAKE_DESIGNSPACES = True # 
    COPY_MASTERS = True # Copy master to location. Set the right pixel shape. Add COLRV1 pixel layers to each glyph.
    SET_GLYPH_ORDER = True
    MAKE_STAT = True
    MAKE_UFO = True
    MAKE_TTF = True
    MAKE_VF = True
    USE_PRODUCTION_NAMES = False
else:
    MAKE_DESIGNSPACES = True 
    COPY_MASTERS = False # Copy master to location. Set the right pixel shape. Add COLRV1 pixel layers to each glyph.
    SET_GLYPH_ORDER = False
    MAKE_STAT = False
    MAKE_UFO = False
    MAKE_TTF = False
    MAKE_VF = False
    USE_PRODUCTION_NAMES = False

for dsName, dsParams in DESIGN_SPACES.items():

    if MAKE_DESIGNSPACES:
        # For all 6 design spaces, generate the OTF/TTF/VF
        # Auto generate the design space file vor this variant. (TBD)
        makeDesignSpaceFile(dsName, dsParams, AXES)

    if COPY_MASTERS:
        print('--- Copy UFO masters')
        # Copy the ufo/ masters to _masters/<variant> for every master and apply the 
        # right file name based on location  and variant
        copyMasters(dsName, dsParams, AXES)

    if MAKE_VF:
        print('--- Make variable fonts')
        # Compile calibrated UFOs masters/ into vf/ variable font
        if not os.path.exists('vf'):
            os.system('mkdir vf')
        vfPath = 'vf/' + dsName.replace('.designspace', '-%03d.ttf' % BUILD)
        cmd = 'fontmake -o variable -m %s --output-path %s' % (dsName, vfPath)
        print('...', cmd)
        os.system(cmd)
        continue

        if USE_PRODUCTION_NAMES:
            cmd += ' --use_production_names'
        else:
            cmd += ' --no-production-names'
        print('---', cmd)
        print('--- Fixing TTF name tables')
        fixTTFNameTables('vf/', NAME_TABLES)
        os.system(cmd)
        cmd = 'statmake --designspace %s --stylespace %s %s' % (DESIGN_SPACE_VF, STYLE_SPACE, vfPath)
        print('...', cmd)
        if MAKE_STAT:
            os.system(cmd)


print('Done')


