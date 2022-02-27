#
#   Making the separate Bitcount masters, with the pixel shapes filled in.
#
import os
from scriptsLib import copyUFO
from scriptsLib import MASTERS_PATH


def makePixelMasters():
    """Copy the Bitcount masters into MASTERS_PATH, alther their name an fill in the pixels
    shape at that location in the design space.
    """
    print('--- Making pixel masters')
    
    # Make the local masters path. Note that this directory does not commit to Github.
    if not os.path.exists(MASTERS_PATH):
        os.mkdir(MASTERS_PATH)

    # Remove old UFO masters here
    for fileName in os.listdir(MASTERS_PATH):
        if fileName.endswith('.ufo'):
            deleteUFO(dstPath)
