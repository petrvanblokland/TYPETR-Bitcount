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
from scriptsLib.smartsets import SMARTSETS_INDEXED, SMARTSET_V6
from scriptsLib.buildData import *
from scriptsLib.names import NAME_TABLES, BUILD
from scriptsLib.fixttf import fixTTFNameTables

if 0:
    FIX_MASTERS = True
    SET_GLYPH_ORDER = True
    EXPORT_MASTERS = True # Export drawn masters in ufo/ into calibrated masters/
    MAKE_STAT = True
    MAKE_UFO = True
    MAKE_TTF = True
    MAKE_VF = True
    USE_PRODUCTION_NAMES = False
else:
    FIX_MASTERS = False
    SET_GLYPH_ORDER = False
    EXPORT_MASTERS = False # Export drawn masters in ufo/ into calibrated masters/
    MAKE_STAT = False
    MAKE_UFO = False
    MAKE_TTF = False
    MAKE_VF = False
    USE_PRODUCTION_NAMES = False

# Calibrating from drawn UFO sources in ufo/ into final masters/
DESIGN_SPACE_EXPORT = 'ZZZ.designspace'

# Compile  main masters _instances/, _ttf/ and vf/
DESIGN_SPACE_TTF = 'ZZZ.designspace'
DESIGN_SPACE_VF = 'ZZZ.designspace'

STYLE_SPACE = 'ZZZ.stylespace'

def copyAnchors(srcG, dstG):
    dstG.clearAnchors()
    for anchor in srcG.anchors:
        dstG.appendAnchor(name=anchor.name, position=(dstG.width/2, anchor.y))

def setFeatures(mastersData):
    for ufoName, md in sorted(mastersData.items()):
        if not md.isMaster:
            continue
        print('--- Set feature code for', ufoName)
        f = RFont(UFO_PATH + ufoName, showInterface=False)
        f.features.text = '\ninclude(features/Bitcount.fea);\n'
        f.save()
        f.close()

def setGlyphOrders(mastersData):
    glyphOrder = None
    for ufoName, md in sorted(mastersData.items()):
        if not md.isMaster:
            continue
        print('--- Set glyph order of %s' % ufoName)
        f = RFont(UFO_PATH + ufoName, showInterface=False)
        if glyphOrder is None:
            glyphOrder = f.naked().unicodeData.sortGlyphNames(f.glyphOrder, sortDescriptors=[dict(type="unicode", ascending=True, allowPseudoUnicode=True)])
        f.glyphOrder = glyphOrder
        print('--- %d glyphs: Set glyph order of %s' % (len(f), ufoName))
        f.save()
        f.close()

def fixWidths(mastersData):
    for ufoName, md in sorted(mastersData.items()):
        if not md.isMaster:
            continue
        ufo = RFont(UFO_PATH + ufoName, showInterface=False)
        for gName in ufo.keys():
            g = ufo[gName]
            if g.width < 0:
                print('... Fix negative width for /%s from %s' % (gName, ufoName))
                g.width = 0
        ufo.save()
        ufo.close()

def removeObsoleteGlyphs(mastersData):
    """Remove obsolete glyphs, such as /FLIPPED and /TMP"""
    for ufoName, md in sorted(mastersData.items()):
        if not md.isMaster:
            continue
        ufo = RFont(UFO_PATH + ufoName, showInterface=False)
        for gName in ('FLIPPED', 'TMP', 'imod.copy_1'):
            if gName in ufo:
                print('... Remove obsolete glyph /%s from %s' % (gName, ufoName))
                ufo.removeGlyph(gName)
        ufo.save()
        ufo.close()

def fixAnchors(mastersData):
    """Check/fix all Black anchors"""
    print('--- Fixing anchors')
    srcName = DISPLAY_REGULAR
    src = RFont(UFO_PATH + srcName, showInterface=False)

    for dstName, md in sorted(mastersData.items()):
        if not md.isMaster:
            continue
        dst = RFont(UFO_PATH + dstName, showInterface=False)
        if src.path == dst.path: # Don't do on self
            continue
        for gName in src.keys():
            if gName not in dst:
                dst[gName] = src[gName]
                print('... [fixAnchors] Copy /%s from %s to %s' % (gName, srcName, dstName))
            srcG = src[gName]
            dstG = dst[gName]
            if (len(srcG.anchors) != len(dstG.anchors)):
                print('### Inconsistent anchors for /%s %s' % (gName, dstName))
                copyAnchors(srcG, dstG)
        dst.save()
        dst.close()

if SET_GLYPH_ORDER:
    print('--- Set glyph order for all masters')
    setGlyphOrders(MASTERS_DATA)

if FIX_MASTERS:   
    print('--- Fixing all masters') 
    setFeatures(MASTERS_DATA) # Set the feature reference in all masters
    removeObsoleteGlyphs(MASTERS_DATA) # Remove glyphs such as /FLIPPED and /TMP
    fixWidths(MASTERS_DATA) # Set negative widths to zero
    #fixAnchors(MASTERS_DATA) # Check/fix anchors from Bold to Black version masters

if EXPORT_MASTERS:
    # Export drawn ufo/ into calibrated masters/
    print('--- Export UFO masters by %s' % DESIGN_SPACE_EXPORT)
    cmd = 'fontmake -o ufo -m %s -i' % DESIGN_SPACE_EXPORT
    print('---', cmd)
    os.system(cmd)

if MAKE_UFO:
    # Export calibrated UFOs masters/ into _instances/
    if not os.path.exists('_instances'):
        os.system('mkdir _instances')
    cmd = 'fontmake -o ufo -i -m %s --round-instances' % DESIGN_SPACE_TTF
    print('---', cmd)
    os.system(cmd)

if MAKE_TTF:
    # Compile calibrated UFOs _instances/ into _ttf/
    if not os.path.exists('_ttf'):
        os.system('mkdir _ttf')
    cmd = 'fontmake -o ttf -u _instances/*.ufo --output-dir _ttf/ --keep-overlaps'
    print('---', cmd)
    os.system(cmd)
    fixTTFNameTables('_ttf/', NAME_TABLES)

if MAKE_VF:
    # Compile calibrated UFOs masters/ into vf/ variable font
    if not os.path.exists('vf'):
        os.system('mkdir vf')
    vfPath = 'vf/' + DESIGN_SPACE_VF.replace('.designspace', '-%03d.ttf' % BUILD)
    cmd = 'fontmake -o variable -m %s --output-path %s' % (DESIGN_SPACE_VF, vfPath)
    if USE_PRODUCTION_NAMES:
        cmd += ' --use_production_names'
    else:
        cmd += ' --no-production-names'
    print('---', cmd)
    print('--- Fixing TTF name tables')
    fixTTFNameTables('vf/', NAME_TABLES)
    os.system(cmd)
    cmd = 'statmake --designspace %s --stylespace %s %s' % (DESIGN_SPACE_VF, STYLE_SPACE, vfPath)
    print('---', cmd)
    if MAKE_STAT:
        os.system(cmd)


print('Done')


