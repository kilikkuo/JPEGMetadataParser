import weakref
from misc import log
from FileOPs import nowAt, seekTo, getChar, getCharToOrd, getBytes2, getBytes4,\
                    getBytes8, BYTE_ALIGN_INTEL, BYTE_ALIGN_MOTOROLA
import pprint
import struct

H_CMM_TYPE                  = "CMMType"
H_VERSION                   = "Version"
H_DEVICE_CLASS              = "DeviceClass"
H_COLOR_SPACE               = "ColorSpace"
H_PROFILE_CONNECTION_SPACE  = "ProfileConnectionSpace"
H_CREATE_DATETIME           = "Datetime"
H_SIGNATURE                 = "Signature"
H_PLATFORM                  = "Platform"
H_IS_EMBEDED                = "IsEmbeded"
H_USED_INDENDENTLY          = "UsedIndependently"
H_DEVICE_MANUFACTURER       = "DeviceManufacturer"
H_DEVICE_MODEL              = "DeviceModel"
H_ATTR_T_R                  = "Attribute_1"
H_ATTR_M_G                  = "Attribute_2"
H_RENDERING_INTENT          = "RenderingIntent"
H_PROFILE_CREATOR           = "ProfileCreator"
H_PROFILE_D50_XYZ           = "XYZ-D50"

dicTagName2Sig = {
"AToB0Tag"                  :   "A2B0",
"AToB1Tag"                  :   "A2B1",
"AToB2Tag"                  :   "A2B2",
"blueColorantTag"           :   "bXYZ",
"blueTRCTag"                :   "bTRC",
"BToA0Tag"                  :   "B2A0",
"BToA1Tag"                  :   "B2A1",
"BToA2Tag"                  :   "B2A2",
"calibrationDateTimeTag"    :   "calt",
"charTargetTag"             :   "targ",
"chromaticAdaptationTag"    :   "chad",
"copyrightTag"              :   "cprt",
"deviceMfgDescTag"          :   "dmnd",
"deviceModelDescTag"        :   "dmdd",
"gamutTag"                  :   "gamt",
"grayTRCTag"                :   "kTRC",
"greenColorantTag"          :   "gXYZ",
"greenTRCTag"               :   "gTRC",
"luminanceTag"              :   "lumi",
"measurementTag"            :   "meas",
"mediaBlackPointTag"        :   "bkpt",
"mediaWhitePointTag"        :   "wtpt",
"namedColorTag"             :   "ncol",
"namedColor2Tag"            :   "ncl2",
"preview0Tag"               :   "pre0",
"preview1Tag"               :   "pre1",
"preview2Tag"               :   "pre2",
"profileDescriptionTag"     :   "desc",
"profileSequence-DescTag"   :   "pseq",
"ps2CRD0Tag"                :   "psd0",
"ps2CRD1Tag"                :   "psd1",
"ps2CRD2Tag"                :   "psd2",
"ps2CRD3Tag"                :   "psd3",
"ps2CSATag"                 :   "ps2s",
"ps2RenderingIntentTag"     :   "ps2i",
"redColorantTag"            :   "rXYZ",
"redTRCTag"                 :   "rTRC",
"screeningDescTag"          :   "scrd",
"screeningTag"              :   "scrn",
"technologyTag"             :   "tech",
"ucrbgTag"                  :   "bfd ",
"viewingCondDescTag"        :   "vued",
"viewingConditionsTag"      :   "view",
}

dicDevCls2Name = {
'scnr' : "Input devices - scanners and digital cameras",
'mntr' : "Display devices - CRTs and LCDs",
'prtr' : "Output devices - printers",
'link' : "Additional - Device link profiles",
'spac' : "Additional - Color space conversion profiles",
'abst' : "Additional - Abstract profiles",
'nmcl' : "Additional - Named color profiles",
}

dicPlatformSig2Desc = {
'APPL' : "Apple Computer, Inc.",
'MSFT' : "Microsoft Corporation",
'SGI ' : "Silicon Graphics, Inc.",
'SUNW' : "Sun Microsystems, Inc.",
'TGNT' : "Taligent, Inc.",
}

dicRenderingIntent2Desc = {
0 : "Perceptual",
1 : "Relative Colorimetric",
2 : "Saturation",
3 : "Absolute Colorimetric",
}

dicIlluminantType2Desc = {
hex(0)  :   "unknown",
hex(1)  :   "D50",
hex(2)  :   "D65",
hex(3)  :   "D93",
hex(4)  :   "F2",
hex(5)  :   "D55",
hex(6)  :   "A",
hex(7)  :   "Equi-Power (E)",
hex(8)  :   "F8",
}

dicTechType2Desc = {
'fscn'  :   'Film Scanner',
'dcam'  :   'Digital Camera',
'rscn'  :   'Reflective Scanner',
'ijet'  :   'Ink Jet Printer',
'twax'  :   'Thermal Wax Printer',
'epho'  :   'Electrophotographic Printer',
'esta'  :   'Electrostatic Printer',
'dsub'  :   'Dye Sublimation Printer',
'rpho'  :   'Photographic Paper Printer',
'fprn'  :   'Film Writer',
'vidm'  :   'Video Monitor',
'vidc'  :   'Video Camera',
'pjtv'  :   'Projection Television',
'CRT '  :   'Cathode Ray Tube Display',
'PMD '  :   'Passive Matrix Display',
'AMD '  :   'Active Matrix Display',
'KPCD'  :   'Photo CD',
'imgs'  :   'PhotoImageSetter',
'grav'  :   'Gravure',
'offs'  :   'Offset Lithography',
'silk'  :   'Silkscreen',
'flex'  :   'Flexography',
}

dicStdObserver2Desc = {
hex(0)  :   'unknown',
hex(1)  :   '1931 2 degree Observer',
hex(2)  :   '1964 10 degree Observer',
}

dicGeometry2Desc = {
hex(0)  :   'unknown',
hex(1)  :   '0/45 or 45/0',
hex(2)  :   '0/d or d/0',
}

dicColorimetricIntentImageState2Desc = {
'scoe'  :   'Scene colorimetry estimates',
'sape'  :   'Scene appearance estimates',
'fpce'  :   'Focal plane colorimetry estimates',
'rhoc'  :   'Reflection hardcopy original colorimetry',
'rpoc'  :   'Reflection print output colorimetry',
}

class Type(object):
    def __init__(self, sig=None):
        assert sig != None, "input sig should be something !!"
        self._sig = sig
        pass

class Curve(Type):
    descriptor = "curv"
    def __init__(self, sig, exp=None, table=[]):
        Type.__init__(self, sig)
        self._exp = exp
        self._lookUp = table

class ParaCurve(Type):
    descriptor = "para"
    def __init__(self, sig, g, a=None, b=None, c=None, d=None, e=None, f=None):
        Type.__init__(self, sig)
        self._g = g
        self._a = a
        self._b = b
        self._c = c
        self._d = d
        self._e = e
        self._f = f

class Data(Type):
    descriptor = "data"
    def __init__(self):
        Type.__init__(self)

class DateTime(Type):
    descriptor = "dtim"
    def __init__(self):
        Type.__init__(self)

class Lut16(Type):
    descriptor = "mft2"
    def __init__(self):
        Type.__init__(self)

class Lut8(Type):
    descriptor = "mft1"
    def __init__(self):
        Type.__init__(self)

class LutAToB(Type):
    descriptor = "mAB "
    def __init__(self, sig, lstCurveB=None, matM=None, lstCurveM=None, clut=None, lstCurveA=None):
        Type.__init__(self, sig)
        self._lstCurveB = lstCurveB
        self._matM = matM
        self._lstCurveM = lstCurveM
        self._clut = clut
        self._lstCurveA = lstCurveA

class Measurement(Type):
    descriptor = "meas"
    def __init__(self, sig, stdObserver, tristimulus, geometry, flare, stdIlluminant):
        Type.__init__(self, sig)

class NamedColor(Type):
    descriptor = "ncol"
    def __init__(self):
        Type.__init__(self)

class NamedColor2(Type):
    descriptor = "ncol"
    def __init__(self):
        Type.__init__(self)

class ProfileSequenceDesc(Type):
    descriptor = "pseq"
    def __init__(self):
        Type.__init__(self)

class S15Fixed16Array(Type):
    descriptor = "sf32"
    def __init__(self, sig, matArray):
        Type.__init__(self, sig)
        self._array = matArray

class Screen(Type):
    descriptor = "scrn"
    def __init__(self):
        Type.__init__(self)

class Signature(Type):
    descriptor = "sig "
    def __init__(self, sig, content):
        Type.__init__(self, sig)
        self._techContent = content

class TextDescription(Type):
    descriptor = "desc"
    def __init__(self, sig, asciiDesc, unicodeDesc, scriptDesc):
        Type.__init__(self, sig)
        self._asciiDesc = asciiDesc
        self._uniDesc = unicodeDesc
        self._scriptDesc = scriptDesc

class MultiLocalizedUnicode(Type):
    descriptor = "mluc"
    def __init__(self, sig):
        Type.__init__(self, sig)
        self._dicCountry2Lang = {}
        self._dicCountry2Desc = {}

    def add(self, langCode, countryCode, desc):
        assert countryCode not in self._dicCountry2Lang, "Same country for language !!"
        assert countryCode not in self._dicCountry2Desc, "Same country for description !!"
        self._dicCountry2Lang[countryCode] = langCode
        self._dicCountry2Desc[countryCode] = desc

class Text(Type):
    descriptor = "text"
    def __init__(self, sig, content):
        Type.__init__(self, sig)
        self._content = content

class U16Fixed16Array(Type):
    descriptor = "uf32"
    def __init__(self):
        Type.__init__(self)

class Ucrbg(Type):
    descriptor = "bfd "
    def __init__(self):
        Type.__init__(self)

class UInt16Array(Type):
    descriptor = "ui16"
    def __init__(self):
        Type.__init__(self)

class UInt32Array(Type):
    descriptor = "ui32"
    def __init__(self):
        Type.__init__(self)

class UInt64Array(Type):
    descriptor = "ui64"
    def __init__(self):
        Type.__init__(self)

class UInt8Array(Type):
    descriptor = "ui08"
    def __init__(self):
        Type.__init__(self)

class ViewingConditions(Type):
    descriptor = "view"
    def __init__(self, sig, illuminantXYZ, surroundXYZ, illuinantType):
        Type.__init__(self, sig)
        self._absXYZIlluminant = illuminantXYZ
        self._absXYZSurround = surroundXYZ
        self._illuminantType = illuinantType

class XYZ(Type):
    descriptor = "XYZ "
    def __init__(self, sig, X, Y, Z):
        Type.__init__(self, sig)
        self._XYZ = (X, Y, Z)

def GetS15Fixed16Number(_fd):
    intUnsigned = getBytes2(_fd)
    intSigned = intUnsigned - 65536 if intUnsigned >= 32768 else intUnsigned
    fracPart = getBytes2(_fd)
    v = intSigned + float(fracPart) / 65536
    return v

def GetXYZHelper(_fd):
    assert _fd, "_fd should not be null !"
    X = GetS15Fixed16Number(_fd)
    Y = GetS15Fixed16Number(_fd)
    Z = GetS15Fixed16Number(_fd)
    return X, Y, Z

def GetCurveHelper(_fd, sig):
    reserved = getBytes4(_fd)
    assert reserved == 0
    count = getBytes4(_fd)

    exp = None
    tblLookUp = []
    if count in [0, 1]:
        first = 1.0 if count == 0 else getCharToOrd(_fd)
        second = 0.0 if count == 0 else getCharToOrd(_fd)
        exp = first + float(second/256.0)
        log(" count = %d / exp(%f)"%(count, exp))
    else:
        for _ in xrange(count):
            first, second = getCharToOrd(_fd), getCharToOrd(_fd)
            v = first + float(second/256.0)
            tblLookUp.append(v)
        log(" count = %d "%(count))
    sigDescObj = Curve(sig, exp, tblLookUp)
    return sigDescObj

def GetMlucHelper(_fd, sig, tagStartPos):
    reserved = getBytes4(_fd)
    assert reserved == 0
    numOfRecords = getBytes4(_fd)
    recordSize = getBytes4(_fd)
    log(" numOfRecords = %d / recordSize = %s"%(numOfRecords, recordSize))

    sigDescObj = MultiLocalizedUnicode(sig)
    for _ in xrange(numOfRecords):
        langCode = ''.join(getChar(_fd) for i in xrange(2))
        langCountryCode = ''.join(getChar(_fd) for i in xrange(2))
        lenRecordString = getBytes4(_fd)
        offsetRecordString = getBytes4(_fd)

        here = nowAt(_fd)
        seekTo(_fd, tagStartPos + offsetRecordString)
        uniBytes = getChar(_fd, lenRecordString)
        # TODO : Think a better way to store these special unicode glyph
        uniChar = unicode(uniBytes, errors='replace')
        log(" uniChar = %s"%(uniChar))
        sigDescObj.add(langCode, langCountryCode, uniChar)
        seekTo(_fd, here)
    return sigDescObj

def GetParaCurveHelper(_fd, sig):
    reserved = getBytes4(_fd)
    assert reserved == 0
    funcType = getBytes2(_fd)
    reserved2 = getBytes2(_fd)
    assert reserved2 == 0
    para_g = para_a = para_b = para_c = para_d = para_e = para_f = None

    if funcType == 0:
        para_g = GetS15Fixed16Number(_fd)
    elif funcType == 1:
        para_g = GetS15Fixed16Number(_fd)
        para_a = GetS15Fixed16Number(_fd)
        para_b = GetS15Fixed16Number(_fd)
    elif funcType == 2:
        para_g = GetS15Fixed16Number(_fd)
        para_a = GetS15Fixed16Number(_fd)
        para_b = GetS15Fixed16Number(_fd)
        para_c = GetS15Fixed16Number(_fd)
    elif funcType == 3:
        para_g = GetS15Fixed16Number(_fd)
        para_a = GetS15Fixed16Number(_fd)
        para_b = GetS15Fixed16Number(_fd)
        para_c = GetS15Fixed16Number(_fd)
        para_d = GetS15Fixed16Number(_fd)
    elif funcType == 4:
        para_g = GetS15Fixed16Number(_fd)
        para_a = GetS15Fixed16Number(_fd)
        para_b = GetS15Fixed16Number(_fd)
        para_c = GetS15Fixed16Number(_fd)
        para_d = GetS15Fixed16Number(_fd)
        para_e = GetS15Fixed16Number(_fd)
        para_f = GetS15Fixed16Number(_fd)
    sigDescObj = ParaCurve(sig, para_g, para_a, para_b, para_c, para_d,\
                           para_e, para_f)
    log(" ParaCurve - g(%f), a(%f), b(%f), c(%f), d(%f), e(%f), f(%f)"%(\
        para_g, para_a, para_b, para_c, para_d, para_e, para_f))
    return sigDescObj

def GetAToBHelper(_fd, sig, tagStartPos):
    reserved = getBytes4(_fd)
    assert reserved == 0
    numOfInputChannel = getCharToOrd(_fd)
    numOfOutputChannel = getCharToOrd(_fd)
    padding = getBytes2(_fd)
    log(" Input(%d) , Output(%d), padding(%d)"%(numOfInputChannel, numOfOutputChannel, padding))
    assert padding == 0

    sigDescObj = None
    lstBCurve = []
    mMat = None
    lstMCurve = []
    clut = None
    lstACurve = []

    offset2BCurve = getBytes4(_fd)
    if offset2BCurve != 0:
        here = nowAt(_fd)
        seekTo(_fd, tagStartPos + offset2BCurve)
        for _ in xrange(numOfOutputChannel):
            subType = getChar(_fd, 4)
            log(" B Curve subtype = %s"%(subType))
            if subType == "para":
                sigSubDescObj = GetParaCurveHelper(_fd, sig)
                lstBCurve.append(sigSubDescObj)
            elif subType == "curv":
                sigSubDescObj = GetCurveHelper(_fd, sig)
                lstBCurve.append(sigSubDescObj)
        seekTo(_fd, here)
        assert len(lstBCurve) == numOfOutputChannel

    offset2Matrix = getBytes4(_fd)
    if offset2Matrix != 0:
        here = nowAt(_fd)
        seekTo(_fd, tagStartPos + offset2Matrix)
        mat = []
        for _ in xrange(12):
            intUnsigned = getBytes2(_fd)
            intSigned = intUnsigned - 65536 if intUnsigned >= 32768 else intUnsigned
            fracPart = getBytes2(_fd)
            v = intSigned + float(fracPart) / 65536
            mat.append(v)
        log(" Matrix = %s"%(str(mat)))
        mMat = S15Fixed16Array(sig, mat)
        seekTo(_fd, here)

    offset2MCurve = getBytes4(_fd)
    if offset2MCurve != 0:
        here = nowAt(_fd)
        seekTo(_fd, tagStartPos + offset2MCurve)
        for _ in xrange(numOfOutputChannel):
            subType = getChar(_fd, 4)
            log(" M Curve subtype = %s"%(subType))
            if subType == "para":
                sigSubDescObj = GetParaCurveHelper(_fd, sig)
                lstMCurve.append(sigSubDescObj)
            elif subType == "curv":
                sigSubDescObj = GetCurveHelper(_fd, sig)
                lstMCurve.append(sigSubDescObj)
        seekTo(_fd, here)
        assert len(lstMCurve) == numOfOutputChannel

    offset2CLUT = getBytes4(_fd)
    if offset2CLUT != 0:
        # TODO : Not implement yet
        here = nowAt(_fd)
        seekTo(_fd, tagStartPos + offset2CLUT)
        seekTo(_fd, here)

    offset2ACurve = getBytes4(_fd)
    if offset2ACurve != 0:
        # TODO : Need to check correctness
        here = nowAt(_fd)
        seekTo(_fd, tagStartPos + offset2ACurve)
        for _ in xrange(numOfOutputChannel):
            subType = getChar(_fd, 4)
            log(" M Curve subtype = %s"%(subType))
            if subType == "para":
                sigSubDescObj = GetParaCurveHelper(_fd, sig)
                lstACurve.append(sigSubDescObj)
            elif subType == "curv":
                sigSubDescObj = GetCurveHelper(_fd, sig)
                lstACurve.append(sigSubDescObj)
        seekTo(_fd, here)
        assert len(lstACurve) == numOfOutputChannel

    log(" O2B(%d) / O2mat(%d) / O2M(%d) / O2CLUT(%d) / O2A(%d)"%(offset2BCurve,\
        offset2Matrix, offset2MCurve, offset2CLUT, offset2ACurve))

    sigDescObj = LutAToB(sig, lstBCurve, mMat, lstMCurve, clut, lstACurve)
    return sigDescObj

def GetSigObject(sig, type, _fd, size, tagStartPos=None):
    # _fd is already seeked to starting point of data
    # 4bytes type(description) is included in size
    sigDescObj = None
    if sig == "A2B0":
        if type == "mAB ":
            sigDescObj = GetAToBHelper(_fd, sig, tagStartPos)
        elif type == "mft2":
            pass
        pass
    elif sig == "A2B1":
        if type == "mAB ":
            sigDescObj = GetAToBHelper(_fd, sig, tagStartPos)
        elif type == "mft2":
            pass
        pass
    elif sig == "A2B2":
        if type == "mAB ":
            sigDescObj = GetAToBHelper(_fd, sig, tagStartPos)
        elif type == "mft2":
            pass
        pass
    elif sig in ["bXYZ", "gXYZ", "rXYZ", "bkpt", "wtpt", "lumi"]:
        reserved = getBytes4(_fd)
        assert reserved == 0
        assert size == 20
        X, Y, Z = GetXYZHelper(_fd)
        log(" XYZ = (%f, %f, %f)"%(X, Y, Z))
        sigDescObj = XYZ(sig, X, Y, Z)
    elif sig == "B2A0":
        pass
    elif sig == "B2A1":
        pass
    elif sig == "B2A2":
        pass
    elif sig == "calt":
        pass
    elif sig == "ciis":
        content = ''.join(getChar(_fd) for _ in xrange(size-4)).strip('\0x00')
        log(" ciis content = %s "%(dicColorimetricIntentImageState2Desc.get(content, "Unknown")))
        sigDescObj = Signature(sig, content)
    elif sig == "targ":
        pass
    elif sig == "cprt":
        if type == "mluc":
            sigDescObj = GetMlucHelper(_fd, sig, tagStartPos)
        else:
            content = ''.join(getChar(_fd) for _ in xrange(size-4))
            log(" cpry content = %s"%(content))
            sigDescObj = Text(sig, content)
        pass
    elif sig == "chad":
        reserved = getBytes4(_fd)
        assert reserved == 0
        assert size == 44
        mat = []
        for _ in xrange(9):
            intUnsigned = getBytes2(_fd)
            intSigned = intUnsigned - 65536 if intUnsigned >= 32768 else intUnsigned
            fracPart = getBytes2(_fd)
            v = intSigned + float(fracPart) / 65536
            mat.append(v)
        log(" chad = %s"%(str(mat)))
        sigDescObj = S15Fixed16Array(sig, mat)
        pass
    elif sig == "gamt":
        pass
    elif sig == "kTRC":
        pass
    elif sig == "meas":
        reserved = getBytes4(_fd)
        assert reserved == 0
        assert size == 36
        obs = dicStdObserver2Desc.get(hex(getBytes4(_fd)), dicStdObserver2Desc[hex(0)])
        tristimulusXYZ = GetXYZHelper(_fd)
        geo = dicGeometry2Desc.get(hex(getBytes4(_fd)), dicGeometry2Desc[hex(0)])
        flareInt, flareFractional = getBytes2(_fd), getBytes2(_fd)
        flare = flareInt + float(flareFractional) / 65536
        illuminantType = dicIlluminantType2Desc.get(hex(getBytes4(_fd)), dicIlluminantType2Desc[hex(0)])
        log(" obs(%s) / triXYZ(%s) / geo(%s) / flare(%f) / illu(%s)"%(obs, str(tristimulusXYZ),\
        geo, flare, illuminantType))
        sigDescObj = Measurement(sig, obs, tristimulusXYZ, geo, flare, illuminantType)
    elif sig == "ncol":
        pass
    elif sig == "ncl2":
        pass
    elif sig == "pre0":
        pass
    elif sig == "pre1":
        pass
    elif sig == "pre2":
        pass
    elif sig in ["dscm"]:
        if type == "mluc":
            sigDescObj = GetMlucHelper(_fd, sig, tagStartPos)

    elif sig in ["desc", "dmdd", "dmnd", "scrd", "vued"]:
        if type == "mluc":
            sigDescObj = GetMlucHelper(_fd, sig, tagStartPos)
        else:
            reserved = getBytes4(_fd)
            assert reserved == 0
            asciiCount = getBytes4(_fd)
            log(" asciiCount = %d"%(asciiCount))
            asciiInvariantDesc = getChar(_fd, asciiCount)
            log(" asciiInvariantDesc = %s"%(asciiInvariantDesc))
            uniLangCode = getBytes4(_fd)
            uniCount = getBytes4(_fd)
            log(" uniLangCode, uniCount = %d, %d"%(uniLangCode, uniCount))
            uniLocalizableDesc = None
            if uniCount != 0:
                uniLocalizableDesc = u""
                for _ in xrange(uniCount):
                    uniLocalizableDesc.join(getBytes2(_fd).decode("utf-8", "ignore"))
                log(" uniLocalizableDesc = %s"%(uniLocalizableDesc))
            scriptCode = getBytes2(_fd)
            scriptCount = getCharToOrd(_fd)
            log(" scriptCode, scriptCount = %d, %d"%(scriptCode, scriptCount))
            localMacintoshDesc = None
            if scriptCount != 0:
                localMacintoshDesc = getChar(_fd, min(67,scriptCount))
                log(" localMacintoshDesc = %s"%(localMacintoshDesc))
            sigDescObj = TextDescription(sig, asciiInvariantDesc,\
                                         uniLocalizableDesc, localMacintoshDesc)
        pass
    elif sig == "pseq":
        pass
    elif sig == "psd0":
        pass
    elif sig == "psd1":
        pass
    elif sig == "psd2":
        pass
    elif sig == "psd3":
        pass
    elif sig == "ps2s":
        pass
    elif sig == "ps2i":
        pass
    elif sig in ["rTRC", "gTRC", "bTRC"]:
        sigDescObj = GetCurveHelper(_fd, sig)
    elif sig == "scrn":
        pass
    elif sig == "tech":
        content = ''.join(getChar(_fd) for _ in xrange(size-4)).strip('\0x00')
        log(" tech content = %s "%(dicTechType2Desc.get(content, 'None')))
        sigDescObj = Signature(sig, content)
        pass
    elif sig == "bfd ":
        pass
    elif sig == "vued":
        pass
    elif sig == "view":
        reserved = getBytes4(_fd)
        assert reserved == 0
        illuminantXYZ = GetXYZHelper(_fd)
        surroundXYZ = GetXYZHelper(_fd)
        log(" illXYZ = (%f, %f, %f)"%(illuminantXYZ))
        log(" surXYZ = (%f, %f, %f)"%(surroundXYZ))
        illuminantType = dicIlluminantType2Desc.get(hex(getBytes4(_fd)), dicIlluminantType2Desc[hex(0)])
        sigDescObj = ViewingConditions(sig, illuminantXYZ, surroundXYZ, illuminantType)
        log(" illuminantType = %s"%illuminantType)

    return sigDescObj

class ICCProfileParser(object):
    def __init__(self, fd):
        self.__dicHeaderInfo = {}
        self.__dicSig2TagInfo = {}
        self._fdWRef = weakref.ref(fd)

    def parse(self):
        self.__parseICCProfile()

    def __getattr__(self, attr):
        if attr == "_fd":
            return self._fdWRef()
        else:
            raise AttributeError

    def __parseICCProfile(self):
        # Refer to http://blog.fpmurphy.com/2012/03/extract-icc-profile-from-images.html

        basePos = nowAt(self._fd)
        def parseHeader():
            log("Enter", "[ICCProfileHeader]", "add")
            profileSize = getBytes4(self._fd)

            cmmType = ''.join(getChar(self._fd) for _ in xrange(4))
            lstVer = [str(getCharToOrd(self._fd)) for _ in xrange(4)]
            self.__dicHeaderInfo[H_CMM_TYPE] = cmmType
            self.__dicHeaderInfo[H_VERSION] = lstVer[0] + "." + lstVer[1]

            deviceClass = ''.join(getChar(self._fd) for _ in xrange(4))
            colorSpaceOfData = ''.join(getChar(self._fd) for _ in xrange(4))
            pcs = ''.join(getChar(self._fd) for _ in xrange(4))
            self.__dicHeaderInfo[H_DEVICE_CLASS] = dicDevCls2Name.get(deviceClass, "Not found")
            self.__dicHeaderInfo[H_COLOR_SPACE] = colorSpaceOfData.strip()
            self.__dicHeaderInfo[H_PROFILE_CONNECTION_SPACE] = pcs.strip()

            lstDatetime = [getBytes2(self._fd) for _ in xrange(6)]
            signature = ''.join(getChar(self._fd) for _ in xrange(4))
            assert signature == "acsp", "Not a standard ICC Profile !!"
            primaryPlatform = ''.join(getChar(self._fd) for _ in xrange(4))

            def getBitsList(numBytes):
                lstBits = []
                for _ in xrange(numBytes):
                    bits_short = bin(getCharToOrd(self._fd))[2:]
                    bits_full = '00000000'[len(bits_short):] + bits_short
                    lstBits.extend([int(b) for b in bits_full])
                return lstBits

            lstProfileFlags = getBitsList(4)
            self.__dicHeaderInfo[H_CREATE_DATETIME] = "Datatime = %d/%d/%d-%d:%d:%d"%tuple(lstDatetime)
            self.__dicHeaderInfo[H_SIGNATURE] = signature
            self.__dicHeaderInfo[H_PLATFORM] = dicPlatformSig2Desc.get(primaryPlatform, "Not found")
            self.__dicHeaderInfo[H_IS_EMBEDED] = True if lstProfileFlags[0] == 1 else False
            self.__dicHeaderInfo[H_USED_INDENDENTLY] = False if lstProfileFlags[1] == 1 else True

            deviceManufacturer = ''.join(getChar(self._fd) for _ in xrange(4))
            deviceModel = ''.join(getChar(self._fd) for _ in xrange(4))
            lstDeviceAttributes = getBitsList(8)
            renderingIntent, zeroPadding = getBytes2(self._fd), getBytes2(self._fd)

            self.__dicHeaderInfo[H_DEVICE_MANUFACTURER] = deviceManufacturer
            self.__dicHeaderInfo[H_DEVICE_MODEL] = deviceModel
            self.__dicHeaderInfo[H_ATTR_T_R] = "Transparency" if lstDeviceAttributes[0] == 1 else "Reflective"
            self.__dicHeaderInfo[H_ATTR_M_G] = "Matte" if lstDeviceAttributes[1] == 1 else "Glossy"
            self.__dicHeaderInfo[H_RENDERING_INTENT] = dicRenderingIntent2Desc.get(renderingIntent, "Not found")

            intX, intY, intZ = getBytes4(self._fd), getBytes4(self._fd), getBytes4(self._fd)
            X = struct.unpack('f', struct.pack('i', intX))
            Y = struct.unpack('f', struct.pack('i', intY))
            Z = struct.unpack('f', struct.pack('i', intZ))
            CIEXYZ_X = X[0] / Y[0]
            CIEXYZ_Y = Y[0] / Y[0]
            CIEXYZ_Z = Z[0] / Y[0]

            profileCreator = ''.join(getChar(self._fd) for _ in xrange(4))
            profileID = [hex(getCharToOrd(self._fd)) for _ in xrange(16)]
            reserved = [hex(getCharToOrd(self._fd)) for _ in xrange(28)]

            self.__dicHeaderInfo[H_PROFILE_CREATOR] = profileCreator
            self.__dicHeaderInfo[H_PROFILE_D50_XYZ] = "(%f, %f, %f)"%(CIEXYZ_X, CIEXYZ_Y, CIEXYZ_Z)
            log("Header Information : \n%s "%(pprint.pformat(self.__dicHeaderInfo, indent=2)))
            log("Leave", "[ICCProfileHeader]", "remove")

        def parseTagTable():
            log("Enter", "[ICCProfileTagTable]", "add")
            tagCount = getBytes4(self._fd)
            log("Tag count = %d"%(tagCount))
            for idx in xrange(tagCount):
                tagStartPos = nowAt(self._fd)
                sig = ''.join(getChar(self._fd) for _ in xrange(4))
                offset = getBytes4(self._fd)
                size = getBytes4(self._fd)
                seekTo(self._fd, basePos+offset)
                log("Tag sig(%s) / offset(%d) / size(%d) / basePos(%d) / tagSigPos(%d) / tagTypePos(%d) "%(sig, offset, size, basePos, tagStartPos, basePos+offset))
                typeDesc = ''.join(getChar(self._fd) for _ in xrange(4))
                log("Type Desc(%s)"%(typeDesc))
                sigDescObj = GetSigObject(sig, typeDesc, self._fd, size, basePos+offset)
                assert sig not in self.__dicSig2TagInfo, "Check this file, two same sig !"
                self.__dicSig2TagInfo[sig] = sigDescObj
                seekTo(self._fd, tagStartPos+12)

            log("Leave", "[ICCProfileTagTable]", "remove")
            pprint.pprint(self.__dicSig2TagInfo)
            pass

        parseHeader()
        parseTagTable()

import argparse
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='Input .icc file to be parsed')
    args = parser.parse_args()
    if (args.input != None):
        _file = open(args.input)
        iccParser = ICCProfileParser(_file)
        iccParser.parse()
    else:
        print "Nothing to be parsed, make sure there's an input file !! "
