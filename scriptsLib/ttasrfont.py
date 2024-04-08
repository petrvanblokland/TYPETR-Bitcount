#
#    This scripts shows the compatibility between the font.info RoboFont dialog and script parameters.
#
from fontTools.ttLib import TTFont
from fontTools.ttLib.tables._n_a_m_e import NameRecord

BIT0 = 0x0001
BIT1 = 0x0002
BIT2 = 0x0004
BIT3 = 0x0008
BIT4 = 0x0010
BIT5 = 0x0020
BIT6 = 0x0040
BIT7 = 0x0080
BIT8 = 0x0100
BIT9 = 0x0200

class TTasRFont:
    def __init__(self, path):
        """A TTFont that with the UI of an RFont."""
        self.path = path
        self.f = TTFont(path)

    XML = """<?xml version="1.0" encoding="UTF-8"?><namerecord nameID="%d" platformID="3" platEncID="1" langID="0x409" unicode="True">%s</namerecord>"""

    def getNameRecord(self, nameID):
        nameTable = self.f['name']
        for nrIndex, nameRecord in enumerate(list(nameTable.names)):
            if nameID == nameRecord.nameID: # Integer index as string
                return nameRecord
        nameRecord = NameRecord()
        nameRecord.nameID = nameID
        nameRecord.platformID = 3
        nameRecord.platEncID = 1
        nameRecord.langID = 0x409
        nameRecord.string = ''

        nameTable.names.append(nameRecord)
        return nameRecord

    def removeNameRecord(self, nameID):
        #print('... Remove name table record', nameID)
        nameTable = self.f['name']
        names = []
        for nameRecord in nameTable.names:
            if nameRecord.nameID != nameID:
                names.append(nameRecord)
        nameTable.names = names

    def setNameRecord(self, nameID, value):

        if isinstance(value, (list, tuple)):
            value = ''.join(value)
        value = value.strip()

        nameRecord = self.getNameRecord(nameID)
        nameRecord.string = value
    
    def save(self, path=None):
        if path is None:
            path = self.path
        out = open(path, 'wb')
        self.f.save(out)
        out.close()
          
    def _get_familyName(self):
        return str(self.getNameRecord(1))        
    def _set_familyName(self, name):
        self.setNameRecord(1, name)
    familyName = property(_get_familyName, _set_familyName)
    
    # TTFont['name']-->subFamilyName
    def _get_styleName(self):
        return str(self.getNameRecord(2))        
    def _set_styleName(self, name):
        self.setNameRecord(2, name)
    styleName = property(_get_styleName, _set_styleName)

    # TTFont['name']-->uniqueID
    def _get_openTypeNameUniqueID(self):
        return str(self.getNameRecord(3))        
    def _set_openTypeNameUniqueID(self, name):
        self.setNameRecord(3, name)
    openTypeNameUniqueID = property(_get_openTypeNameUniqueID, _set_openTypeNameUniqueID)

    # TTFont['name']-->fullName
    def _get_openTypeNameCompatibleFullName(self):
        return self.str(self.getNameRecord(4))
    def _set_openTypeNameCompatibleFullName(self, name):
        self.setNameRecord(4, name)
    openTypeNameCompatibleFullName = property(_get_openTypeNameCompatibleFullName, _set_openTypeNameCompatibleFullName)

    # TTFont['name']-->version
    def _get_openTypeNameVersion(self):
        return self.str(self.getNameRecord(5))
    def _set_openTypeNameVersion(self, version):
        self.setNameRecord(5, version)
    openTypeNameVersion = property(_get_openTypeNameVersion, _set_openTypeNameVersion)
    
    # TTFont['name']-->openTypeNamePostscriptName
    def _get_openTypeNamePostscriptName(self):
        return self.str(self.getNameRecord(6))
    def _set_openTypeNamePostscriptName(self, name):
        self.setNameRecord(6, name)
    openTypeNamePostscriptName = property(_get_openTypeNamePostscriptName, _set_openTypeNamePostscriptName)
    
    # TTFont['name']-->preferredFamily
    def _get_openTypeNamePreferredFamilyName(self):
        nameRecord = self.getNameRecord(16)
        if nameRecord is not None:
            print(nameRecord)
            return nameRecord
        return None
    def _set_openTypeNamePreferredFamilyName(self, name):
        if name is None:
            self.removeNameRecord(16)
        else:
            self.setNameRecord(16, name)
    openTypeNamePreferredFamilyName = property(_get_openTypeNamePreferredFamilyName, _set_openTypeNamePreferredFamilyName)
    
    # TTFont['name']-->preferredSubFamily
    def _get_openTypeNamePreferredSubfamilyName(self):
        nameRecord = self.getNameRecord(17)
        if nameRecord is not None:
            return str(nameRecord)
        return None
    def _set_openTypeNamePreferredSubfamilyName(self, name):
        if name is None:
            self.removeNameRecord(17)
        else:
            self.setNameRecord(17, name)
    openTypeNamePreferredSubfamilyName = property(_get_openTypeNamePreferredSubfamilyName, _set_openTypeNamePreferredSubfamilyName)
    
    def _get_styleMapStyleName(self):
        fsSelection = self.f['OS/2'].fsSelection
        if self.fsSelectionBold and self.fsSelectionItalic:
            return 'bold italic'
        if self.fsSelectionItalic:
            return 'italic'
        if self.fsSelectionBold:
            return 'bold'
        if self.fsSelectionRegular:
            return 'regular'
        return None       
    def _set_styleMapStyleName(self, name):
        name = (name or '').lower() # Can be None
        useTypoMetrics = self.useTypoMetrics
        assert name in ('', 'regular', 'italic', 'bold', 'bold italic')
        if name == 'italic':
            self.fsSelectionRegular = False
            self.fsSelectionBold = False
            self.fsSelectionItalic = True
            self.f['head'].macStyle = BIT1
        elif name == 'bold':
            self.fsSelectionRegular = False
            self.fsSelectionBold = True
            self.fsSelectionItalic = False
            self.f['head'].macStyle = BIT0
        elif name == 'bold italic':
            self.fsSelectionRegular = False
            self.fsSelectionBold = True
            self.fsSelectionItalic = True
            self.f['head'].macStyle = BIT1 | BIT0
        elif name =='regular':
            self.fsSelectionRegular = True
            self.fsSelectionBold = False
            self.fsSelectionItalic = False
            self.f['head'].macStyle = 0
        else:
            self.fsSelectionRegular = False
            self.fsSelectionBold = False
            self.fsSelectionItalic = False
            self.f['head'].macStyle = 0
    styleMapStyleName = property(_get_styleMapStyleName, _set_styleMapStyleName)

    # https://learn.microsoft.com/en-us/typography/opentype/spec/os2#fsselection

    def _get_fsSelectionItalic(self):
        return bool(self.f['OS/2'].fsSelection & BIT0)
    def _set_fsSelectionItalic(self, flag):
        if flag:
            self.f['OS/2'].fsSelection |= BIT0
        else:
            self.f['OS/2'].fsSelection &= ~BIT0
    fsSelectionItalic = property(_get_fsSelectionItalic, _set_fsSelectionItalic)

    def _get_fsSelectionUnderscore(self):
        return bool(self.f['OS/2'].fsSelection & BIT1)
    def _set_fsSelectionUnderscore(self, flag):
        if flag:
            self.f['OS/2'].fsSelection |= BIT1
        else:
            self.f['OS/2'].fsSelection &= ~BIT1
    fsSelectionUnderscore = property(_get_fsSelectionUnderscore, _set_fsSelectionUnderscore)

    def _get_fsSelectionNegative(self):
        return bool(self.f['OS/2'].fsSelection & BIT2)
    def _set_fsSelectionNegative(self, flag):
        if flag:
            self.f['OS/2'].fsSelection |= BIT2
        else:
            self.f['OS/2'].fsSelection &= ~BIT2
    fsSelectionNegative = property(_get_fsSelectionNegative, _set_fsSelectionNegative)

    def _get_fsSelectionOutlined(self):
        return bool(self.f['OS/2'].fsSelection & BIT3)
    def _set_fsSelectionOutlined(self, flag):
        if flag:
            self.f['OS/2'].fsSelection |= BIT3
        else:
            self.f['OS/2'].fsSelection &= ~BIT3
    fsSelectionOutlined = property(_get_fsSelectionOutlined, _set_fsSelectionOutlined)

    def _get_fsSelectionStrikeOut(self):
        return bool(self.f['OS/2'].fsSelection & BIT4)
    def _set_fsSelectionStrikeOut(self, flag):
        if flag:
            self.f['OS/2'].fsSelection |= BIT4
        else:
            self.f['OS/2'].fsSelection &= ~BIT4
    fsSelectionStrikeOut = property(_get_fsSelectionStrikeOut, _set_fsSelectionStrikeOut)

    def _get_fsSelectionBold(self):
        return bool(self.f['OS/2'].fsSelection & BIT5)
    def _set_fsSelectionBold(self, flag):
        if flag:
            self.f['OS/2'].fsSelection |= BIT5
        else:
            self.f['OS/2'].fsSelection &= ~BIT5
    fsSelectionBold = property(_get_fsSelectionBold, _set_fsSelectionBold)

    def _get_fsSelectionRegular(self):
        return bool(self.f['OS/2'].fsSelection & BIT6)
    def _set_fsSelectionRegular(self, flag):
        if flag:
            self.f['OS/2'].fsSelection |= BIT6
        else:
            self.f['OS/2'].fsSelection &= ~BIT6
    fsSelectionRegular = property(_get_fsSelectionRegular, _set_fsSelectionRegular)

    #   https://learn.microsoft.com/en-us/typography/opentype/spec/os2#fsselection
    def _get_useTypoMetrics(self):
        return bool(self.f['OS/2'].fsSelection & BIT7)
    def _set_useTypoMetrics(self, flag):
        if flag:
            self.f['OS/2'].fsSelection |= BIT7 # Set bit 7
        else:
            self.f['OS/2'].fsSelection &= ~BIT7 # Clear bit 7 
    useTypoMetrics = property(_get_useTypoMetrics, _set_useTypoMetrics)

    def _get_fsSelectionWWS(self):
        return bool(self.f['OS/2'].fsSelection & BIT8)
    def _set_fsSelectionWWS(self, flag):
        if flag:
            self.f['OS/2'].fsSelection |= BIT8
        else:
            self.f['OS/2'].fsSelection &= ~BIT8
    fsSelectionWWS = property(_get_fsSelectionWWS, _set_fsSelectionWWS)

    def _get_fsSelectionOblique(self):
        return bool(self.f['OS/2'].fsSelection & BIT9)
    def _set_fsSelectionOblique(self, flag):
        if flag:
            self.f['OS/2'].fsSelection |= BIT9
        else:
            self.f['OS/2'].fsSelection &= ~BIT9
    fsSelectionOblique = property(_get_fsSelectionOblique, _set_fsSelectionOblique)

    # https://learn.microsoft.com/en-us/typography/opentype/spec/os2#fst
    # None = No embedding restrictions
    # 1 = No embedding allowed.
    # 2 = Only preview and print embedding allowed.
    # 3 = Editable embedding allowed.
    # 8 = No subsetting allowed. (This does reverse the [x] checkbox setting, counter intutitive. Use in combination with 1, 2, 3)
    # 9 = Allow only bitmap editing. (This set the [x] checkbox. Use in combination with 1, 2, 3)
    def _get_openTypeOS2Type(self):
        flags = []
        fsType = self.f['OS/2'].fsType
        if fsType & BIT1:
            flags.append(1)
        if fsType & BIT2:
            flags.append(2)
        if fsType & BIT3:
            flags.append(3)
        if fsType & BIT4:
            flags.append(8)
        if fsType & BIT5:
            flags.append(9)
        return flags
    def _set_openTypeOS2Type(self, flags):
        if isinstance(flags, (int, float)):
            flags = [flags]
        fsType = 0
        if 1 in flags:
            fsType = BIT1
        elif 2 in flags:
            fsType = BIT2
        elif 3 in flags:
            fsType = BIT3
        if 8 in flags:
            fsType |= BIT8
        if 9 in flags:
            fsType |= BIT9
        self.f['OS/2'].fsType = fsType
    fsType = property(_get_openTypeOS2Type, _set_openTypeOS2Type)

    def _get_openTypeOS2Panose(self):
        panose = {}
        for name, value in self.f['OS/2'].panose.items():
            panose[name] = value
        return panose
    def _set_openTypeOS2Panose(self, panose):
        """@panoseDict is optional dictionary with individual name. Default is to clear all"""
        panoseFormat = dict(
            bFamilyType=0,
            bSerifStyle=0,
            bWeight=0,
            bProportion=0,
            bContrast=0,
            bStrokeVariation=0,
            bArmStyle=0,
            bLetterForm=0,
            bMidline=0,
            bXHeight=0,
        )
        for name, value in (panose or {}).items():
            assert name in panoseFormat
            panoseFormat[name] = value
        self.f['OS/2'].panose = panoseFormat
    openTypeOS2Panose = property(_get_openTypeOS2Panose, _set_openTypeOS2Panose)

if __name__ == '__main__':
    import os
    OTF_PATH = '../otf/PrestiDisplay-Thin.otf'
    f = TTasRFont(OTF_PATH)
    #f.f['OS/2'].fsSelection = 0

    print('useTypoMetrics', f.useTypoMetrics)
    f.fsSelectionUnderscore = False
    f.fsSelectionNegative = False
    f.fsSelectionOutlined = False
    f.fsSelectionStrikeOut = False
    f.styleMapStyleName = 'bold italic'
    f.useTypoMetrics = True
    f.fsType = [2, 9]
    f.openTypeOS2Panose = dict(
            bFamilyType=0,
            bSerifStyle=0,
            bWeight=0,
            bProportion=0,
            bContrast=0,
            bStrokeVariation=0,
            bArmStyle=0,
            bLetterForm=0,
            bMidline=0,
            bXHeight=0,
    )
    print(f.openTypeOS2Panose)
    f.openTypeOS2Panose = None
    print(f.openTypeOS2Panose)
    f.openTypeOS2Panose = dict(bContrast=1)
    print(f.openTypeOS2Panose)

    path = OTF_PATH.replace('.otf', '-OUT.otf')
    f.save(path)

    #ttxPath = path.replace('.otf', '.ttx')
    #os.system('rm %s;ttx %s' % (ttxPath, path))
    print('Done')
    if 0:
        f.useTypoMetrics = False
        print(f.useTypoMetrics)
        f.useTypoMetrics = True
        print(f.useTypoMetrics)
        print(f.styleMapStyleName)
        print(f.useTypoMetrics)
        f.styleMapStyleName = 'bold'
        print('bold', f.styleMapStyleName)
        print(f.useTypoMetrics)
        f.styleMapStyleName = 'bold italic'
        print('bold italic', f.styleMapStyleName)
        print(f.useTypoMetrics)
        f.styleMapStyleName = 'italic'
        print('italic', f.styleMapStyleName)    
        print(f.useTypoMetrics)
        print(f.fsType)
        f.fsType = [2]
        print(f.fsType)
        f.fsType = [2, 8, 9]
        print(f.fsType)
        f.fsType = []
        print(f.fsType)
        print(f.openTypeNamePreferredFamilyName)
        f.openTypeNamePreferredFamilyName = 'AAA'
        print(f.openTypeNamePreferredFamilyName)
        print(f.openTypeNamePreferredSubfamilyName)
        f.openTypeNamePreferredSubfamilyName = 'BBB'
        print(f.openTypeNamePreferredSubfamilyName)


