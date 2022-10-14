# -*- coding: UTF-8 -*-
import os
import fontmake
from fontmake.font_project import FontProject
from fontTools.ttLib import TTFont, TTLibError

from scriptsLib import *
from scriptsLib.make import copyMasters, makePixelMasters, makeDesignSpaceFiles
from scriptsLib.glyphData import PIXEL_DATA

MAKE_DESIGNSPACES = True # Not yet implemented
COPY_MASTERS = True
MAKE_MASTERS = True
BUILD_VF = True

args = {
    'subset': None,
    'use_production_names': False,
    #'mark_writer_class': None,
    'reverse_direction': False,
    #'kern_writer_class': None,
    'interpolate_binary_layout': False,
    'remove_overlaps': False,
    #'autohint': False,
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
    ('BitcountGrid_Double%s.designspace' % axisCount, GRID),
    ('BitcountGrid_Single%s.designspace' % axisCount, GRID),
    ('BitcountMono_Double%s.designspace' % axisCount, MONO),
    ('BitcountMono_Single%s.designspace' % axisCount, MONO),
    ('BitcountProp_Double%s.designspace' % axisCount, PROP),
    ('BitcountProp_Single%s.designspace' % axisCount, PROP),
]

project = FontProject()
for path, variant in DESIGN_SPACE_PATHS:

    # Auto generate the design space file.
    if MAKE_DESIGNSPACES:
        makeDesignSpaceFiles(axisCount, variant)

    # Copy the masters to _masters/ and apply the right file name based on location 
    if COPY_MASTERS:
        copyMasters(variant)

    # Make all master UFO's, combining the base masters with the pixel shapes
    if MAKE_MASTERS:
        makePixelMasters(variant)

    # Build the VF fonts from the enabled design space files.
    if BUILD_VF:
        print('--- Building VF from design space "%s"' % path)
        result = project.run_from_designspace(designspace_path=path, **args)
        print(result)
        #os.system('open variable_ttf/' + path.replace('.designspace', '-VF.ttf'))
        #os.system('open variable_ttf')


print('--- Done')