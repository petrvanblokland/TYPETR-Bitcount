# -*- coding: UTF-8 -*-
import os
import fontmake
from fontmake.font_project import FontProject
from fontTools.ttLib import TTFont, TTLibError
from scriptsLib.make import makePixelMasters

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

project = FontProject()

# 5 axis variant
# wght Weight by size of the pixels
# OPEN Showing open inside of pixels - outline
# SHPE Catalog axis with a number of pixel variants
# LINE Thickness of outline
# slnt Slanting angle of pixels
axisCount = 5

PATHS = [
    #'BitcountGrid_DoubleCircleSquare%d.designspace' % axisCount,
    #'BitcountGrid_SingleCircleSquare%d.designspace' % axisCount,
    #'BitcountMono_DoubleCircleSquare%d.designspace' % axisCount,
    #'BitcountMono_SingleCircleSquare%d.designspace' % axisCount,
    #'BitcountProp_DoubleCircleSquare%d.designspace' % axisCount,
    #'BitcountProp_SingleCircleSquare%d.designspace' % axisCount,
]
# Make all master UFO's, combining the base masters with the pixel shapes
makePixelMasters()

# Build the VF fonts from the enabled design space files.
for path in PATHS:
    print('--- Building VF from design space "%s"' % path)
    #result = project.run_from_designspace(designspace_path=path, **args)
    print(result)
    #os.system('open variable_ttf/' + path.replace('.designspace', '-VF.ttf'))
    #os.system('open variable_ttf')


print('--- Done')