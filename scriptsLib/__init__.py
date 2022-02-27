#
#   Bitcount production scripts
#
UFO_PATH = 'sources/'
FEATURES_PATH = UFO_PATH + 'features/'
MASTERS_PATH = '_masters/'

def XXXcopyUfoMasters():
    print('--- Copy masters from', UFO_PATH, 'to', MASTERS_PATH)
    if not os.path.exists(MASTERS_PATH):
        os.mkdir(MASTERS_PATH)
    # Copy feature sources
    shutil.copytree(mastersData.path + FEATURES_PATH, MASTERS_PATH + FEATURES_PATH, dirs_exist_ok=True)
    # Copy ufo4/ to masters4/
    for ufoName, d in sorted(mastersData.items()):
        srcPath = masterData.path + ufoName
        dstPath = MASTERS_PATH + ufoName #+ name2MasterName(ufoName)
        if os.path.exists(dstPath):
            deleteUFO(dstPath)
        if VERBOSE:
            print('... Copy', srcPath, 'to', dstPath)
        copyUFO(srcPath, dstPath)



def deleteUFO(path):
    assert path.endswith('.ufo')
    if os.path.exists(path):
        shutil.rmtree(path)

def copyUFO(srcPath, dstPath):
    """Copy the UFO in srcPath to dstPath (directory or UFO name).
    Make sure they are not equal and that the srcPath indeed is 
    has a ufo extension.
    """
    assert os.path.exists(srcPath) and srcPath.endswith('.ufo'), ('Wrong source path %s' % srcPath)
    if os.path.exists(dstPath):
        assert os.path.isdir(dstPath) or dstPath.endswith('.ufo'), ('Wrong existing destination path %s' % dstPath)
    else:
        assert dstPath.endswith('.ufo'), ('Wrong destination path %s' % dstPath)
    shutil.copytree(srcPath, dstPath)

def copyUFOs(srcDirPath, dstDirPath):
    """Copy all UFO's in the srcDirPath to dstDirPath.
    """
    if not srcDirPath.endswith('/'):
        srcDirPath += '/'
    if not dstDirPath.endswith('/'):
        dstDirPath += '/'
    assert os.path.isdir(srcDirPath)
    copiedFiles = []
    for fileName in os.listdir(srcDirPath):
        if fileName.endswith('.ufo'):
            shutil.copytree(srcDirPath + fileName, dstDirPath + fileName)
            copiedFiles.append(fileName)
    return copiedFiles
   
 