# -*- coding: UTF-8 -*-
#
#   Build a variants of Bitcount VF/TTF/OTF from here.
#   Optionally add COLRv1 pixels to the VF.
#
import os
import fontmake
from fontmake.font_project import FontProject
from fontTools.ttLib import TTFont, TTLibError

from scriptsLib import *
from scriptsLib.make import *

if 1: # Build all masters + COLRv1 pixels
    MAKE_DESIGNSPACES = False # Not yet implemented
    COPY_MASTERS = True # Copy base masters of ufo/ to named _masters/
    MAKE_MASTERS = True
    BUILD_VF = True
    ADD_COLRV1 = True
elif 0: 
    MAKE_DESIGNSPACES = False # Not yet implemented
    COPY_MASTERS = False
    MAKE_MASTERS = False
    BUILD_VF = True
    ADD_COLRV1 = False
else: # Just add the COLRv1 pixels to existing VF, to save time during development.
    MAKE_DESIGNSPACES = False # Not yet implemented
    COPY_MASTERS = False
    MAKE_MASTERS = False
    BUILD_VF = False
    ADD_COLRV1 = True

args = {
    'subset': None,
    'use_production_names': False,
    #'mark_writer_class': None,
    'reverse_direction': False,
    #'kern_writer_class': None,
    'interpolate_binary_layout': False,
    'remove_overlaps': False,
    'autohint': False,
    'conversion_error': None,
    #'no_round': False,
    'masters_as_instances': False,
    'interpolate': False,
    'use_afdko': False,
    'subroutinize': True,
    'output':['variable'],
}

# 4 axis variant
# wght Weight by size of the pixels
# OPEN Showing open inside of pixels - outline
# SHPE Catalog axis with a number of pixel variants
# slnt Slanting angle of pixels
axisCount = 4

DESIGN_SPACE_PATHS = [
    # Un-comment the design space that should be generated.
    ('BitcountGrid_Double%s.designspace' % axisCount, GRID),
    ('BitcountGrid_Single%s.designspace' % axisCount, GRID),
    ('BitcountMono_Double%s.designspace' % axisCount, MONO),
    ('BitcountMono_Single%s.designspace' % axisCount, MONO),
    ('BitcountProp_Double%s.designspace' % axisCount, PROP),
    ('BitcountProp_Single%s.designspace' % axisCount, PROP),
]

project = FontProject()
for path, variant in DESIGN_SPACE_PATHS:

    # Auto generate the design space file vor this variant. (TBD)
    if MAKE_DESIGNSPACES:
        makeDesignSpaceFiles(axisCount, variant)

    # Copy the ufo/ masters to _masters/<variant> for every master and apply the 
    # right file name based on location  and variant
    if COPY_MASTERS:
        copyMasters(UFO_PATH, variant)

    # Make all master UFO's, combining the base masters with their pixel shapes
    # based on location/variant
    if MAKE_MASTERS:
        makePixelMasters(variant)

    # Build the VF fonts from the enab-d=led design space files.
    if BUILD_VF:
        print('--- Building VF from design space "%s"' % path)
        result = project.run_from_designspace(designspace_path=path, **args)
        #os.system('open variable_ttf/' + path.replace('.designspace', '-VF.ttf'))
        #os.system('open variable_ttf')

    # Add COLRv1 pixels to a copy of the generated VF
    #if ADD_COLRV1:
    #    vfPath = path.replace('.designspace', '-VF.ttf')
    #    addCOLRv1toVF(VF_PATH + vfPath)

print('--- Done')

