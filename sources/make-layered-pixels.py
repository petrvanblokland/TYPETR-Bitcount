# -*- coding: UTF-8 -*-
import os

from scriptsLib import *
from scriptsLib.make import copyMasters, makePixelMasters, makeDesignSpaceFiles
from scriptsLib.glyphData import PIXEL_DATA

COPY_TEMP = True
#FIND_PIXEL_GRID = False
COPY_INDEXED_PIXELS = True
SET_INDEXED_PIXELS = True

# Create temp directory for target ufo's witn mapped pixels.
UFO_TEMP_PATH = SOURCES_PATH + 'ufo-mapped-pixels/'
if not os.path.exists(UFO_TEMP_PATH):
    print('... Make %s' % UFO_TEMP_PATH)
    os.mkdir(UFO_TEMP_PATH)

if COPY_TEMP:
    print("--- Copy all Bitcount ufo's from %s" % UFO_PATH)
    for ufoName in os.listdir(UFO_PATH):
        if not ufoName.endswith('.ufo'):
            continue
        ufoPath = UFO_PATH + ufoName
        dstPath = UFO_TEMP_PATH + ufoName
        if os.path.exists(dstPath):
            deleteUFO(dstPath)
        copyUFO(ufoPath, dstPath)
        print('... Copy %s --> %s' % (ufoPath, dstPath))

# if FIND_PIXEL_GRID:
#     # Write the source or the dictionary of pixel grid dimensions
#     print("--- Find pixel grid dimensions")
#     for ufoName in os.listdir(UFO_TEMP_PATH):
#         if not ufoName.endswith('.ufo'):
#             continue
#         ufoPath = UFO_TEMP_PATH + ufoName
#         f = openFont(ufoPath)
#         # Find max dimensions of pixels
#         xMax = xMin = yMax = yMin = 0
#         for g in f:
#             # Skip ligatures, since the have a different width
#             if g.name.split('.')[0] in ('fi', 'fl'):
#                 continue
#             if g.width > 600 and not 'Prop' in ufoName:
#                 print(g.name)
#             for component in g.components:
#                 px, py = component.transformation[-2:]
#                 # In case of italic, correct for slanted position
#                 if 'Italic' in ufoName: # f.info.italicAngle != 0
#                     # Pixel offset of Bitcount italic is 14/100
#                     # with baseline offset of 8
#                     px = px - 8 - py*14/100
#                 # Find pixel index from pixel position (100 units grid)
#                 ix = int(px/100)
#                 iy = int(py/100)

#                 xMax = max(xMax, ix) # Find max pixel index
#                 xMin = min(xMin, ix) # Find min pixel index
#                 yMax = max(yMax, iy)
#                 yMin = min(yMin, iy)
#         print("\t'%s': (%d, %d, %d, %d)," % (ufoName, xMin, xMax, yMin, yMax))
#         f.close()

DIMENSIONS = {
    # Pixel grid dimensions (by index number) (xMin, xMax, yMin, yMax)
    'Bitcount_Grid_Double.ufo': (0, 6, -1, 7),
    'Bitcount_Grid_Double_Italic.ufo': (0, 6, -1, 7),
    'Bitcount_Grid_Single.ufo': (0, 6, -1, 7),
    'Bitcount_Grid_Single_Italic.ufo': (0, 6, -1, 7),

    'Bitcount_Mono_Double.ufo': (0, 6, -3, 10),
    'Bitcount_Mono_Double-Italic.ufo': (0, 6, -3, 10),
    'Bitcount_Mono_Single.ufo': (0, 6, -3, 10),
    'Bitcount_Mono_Single-Italic.ufo': (0, 6, -3, 10),

    'Bitcount_Prop_Single.ufo': (-1, 10, -3, 10),
    'Bitcount_Prop_Single-Italic.ufo': (-1, 10, -3, 10),
    'Bitcount_Prop_Double.ufo': (-1, 10, -3, 10),
    'Bitcount_Prop_Double-Italic.ufo': (-1, 10, -3, 10),

    #'Bitcount-VariationPixelsQ.ufo': (0, 0, 0, 0),
    #'Bitcount-VariationPixels.ufo': (0, 0, 0, 0),
}
def getPixelName(ufoName, ix, iy):
    """Answer the horizontal offset, in case the width overflows
    the width of the pixel matrix."""
    xOffset = 0
    xMin, xMax, yMin, yMax = DIMENSIONS[ufoName]
    # If ix overshoots the xMax, then repeat the pattern again
    for n in range(10):
        if ix >= xMax:
            ix = ix - (xMax - xMin)
            xOffset += xMax - xMin
            break
    for n in range(10):
        if iy >= yMax:
            iy = iy - (yMax - yMin)
            break
    return xOffset, 'px.ix%d.iy%d' % (ix, iy)

if COPY_INDEXED_PIXELS:
    print("--- Copy indexed pixels and move them to their grid position")
    for ufoName in os.listdir(UFO_TEMP_PATH):
        if not ufoName.endswith('.ufo'):
            continue
        if ufoName not in DIMENSIONS:
            continue
        ufoPath = UFO_TEMP_PATH + ufoName
        f = openFont(ufoPath)
        # Find max dimensions of pixels
        xMin, xMax, yMin, yMax = DIMENSIONS[ufoName]
        for ix in range(xMin, xMax):
            for iy in range(yMin, yMax):
                xOffset, pixelName = getPixelName(ufoName, ix, iy)
                if pixelName in f:
                    f.removeGlyph(pixelName)
                copyGlyph(f, 'px', f, pixelName)
                g = f[pixelName] # Get the copied pixel
                for contour in g.contours:
                    for p in contour.points:
                        dx = ix*100
                        dy = iy*100
                        if 'Italic' in ufoName: # f.info.italicAngle != 0
                            # Pixel offset of Bitcount italic is 14/100
                            # with baseline offset of 8
                            dx = dx + 8 + iy*14
                        p.x += dx
                        p.y += dy
        f.save()
        f.close()

if SET_INDEXED_PIXELS:
    # Now the masters contain indexed/positioned, we can alter the
    # references and positions of the components in all glyphs.
    print("--- Set component references to index pixels")
    for ufoName in os.listdir(UFO_TEMP_PATH):
        if not ufoName.endswith('.ufo'):
            continue
        if ufoName not in DIMENSIONS:
            continue
        ufoPath = UFO_TEMP_PATH + ufoName
        f = openFont(ufoPath)
        for g in f:
            if g.name.startswith('px'): # Ignore the main pixels
                continue
            for component in g.components:
                assert component.baseGlyph == 'px'
                px, py = component.transformation[-2:]
                # In case of italic, correct for slanted position
                if 'Italic' in ufoName: # f.info.italicAngle != 0
                    # Pixel offset of Bitcount italic is 14/100
                    # with baseline offset of 8
                    italicOffset = - 8 - py*14/100
                    px = px + italicOffset
                else:
                    italicOffset = 0
                # Find pixel index from pixel component position (100 units grid)
                ix = int(px/100)
                iy = int(py/100)
                xOffset, pixelName = getPixelName(ufoName, ix, iy)
                assert pixelName in f, ('### Cannot find pixel /%s in %s' % (pixelName, ufoName))
                component.baseGlyph = pixelName
                # Reset the position, because the component pixel
                # has it's own position defined.
                # Add offset in case of overshoot of matrix with and
                # if there is italic offset.
                component.transformation = (1, 0, 0, 1, xOffset*100, 0)
        f.save()
        f.close()


print('--- Done')