# -*- coding: UTF-8 -*-
#
#   Main build script for Segoe pilots (weight, width, optical size) VF
#

import os
from io import StringIO
from fontTools.ttLib.tables._n_a_m_e import NameRecord
from fontTools.ttLib import TTFont
from fontTools.misc.xmlWriter import XMLWriter

from scriptsLib.ttasrfont import TTasRFont

def fixTTFNameTables(path, mastersData):
    for fileName in sorted(os.listdir(path)):
        if fileName.endswith('.ttf') or fileName.endswith('.otf'):
            print('... Fix TTF/OTF name tables', fileName)
            fontKey = fileName.split('/')[-1] # Remove path from the name, to be used as key
            md = mastersData[fontKey] 
            filePath = path + fileName
            fixTTFNameTable(filePath, md)

def fixTTFNameTable(filePath, md):

    ttf = TTasRFont(filePath)
    fileName = filePath.split('/')[-1]

    ttf.familyName = md.familyName # Name record #1
    ttf.styleName = md.styleName # Name record #2
    ttf.openTypeNameUniqueID = md.uniqueID # Name record #3
    ttf.openTypeNameCompatibleFullName = md.fullName # Name record #4
    ttf.openTypeNameVersion = md.version # Name record $5
    ttf.openTypeNamePostscriptName = md.postscriptName
    ttf.openTypeNamePreferredFamilyName = md.preferredFamily
    ttf.openTypeNamePreferredSubfamilyName = md.preferredSubFamily

    #https://developer.apple.com/fonts/TrueType-Reference-Manual/RM06/Chap6head.html
        
    ttf.styleMapStyleName = md.fsSelection
    ttf.useTypoMetrics = True # Set fsSelection bit 7
    ttf.fsType = 2  # TN advises setting the fsType to bit 4, Print & Preview, which slightly more restrictive.
    ttf.openTypeOS2Panose = None # Clears all flags.
    
    ttf.save(filePath)

    #if makeTTX:
    #    ttxPath = '%s%s' % (path.replace('ttf/', 'ttx/'), fileName.replace('.ttf', '.ttx')) 
    #    cmd = """ttx -o %s %s """ % (ttxPath, ttfPath)
    #    os.system(cmd)

def makeTTX(mastersData):
    for fontName, md in nameTableData.items():
        for path in md.paths:
            ttfPath = '%s%s.ttf' % (path, fontName)
            ttxPath = '%s%s.ttx' % (path.replace('ttf/', 'ttx/'), fontName) 
            if os.path.exists(ttfPath):
                cmd = """ttx -q -o %s %s """ % (ttxPath, ttfPath)
                os.system(cmd)

            

