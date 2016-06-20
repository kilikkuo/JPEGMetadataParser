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
    def __init__(self):
        Type.__init__(self)

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
    def __init__(self):
        Type.__init__(self)

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

def GetXYZHelper(_fd):
    assert _fd, "_fd should not be null !"
    intX, intY, intZ = getBytes4(_fd), getBytes4(_fd), getBytes4(_fd)
    if intX != 0 and intY != 0 and intZ != 0:
        X = struct.unpack('f', struct.pack('i', intX))
        Y = struct.unpack('f', struct.pack('i', intY))
        Z = struct.unpack('f', struct.pack('i', intZ))
        CIEXYZ_X = X[0] / Y[0]
        CIEXYZ_Y = Y[0] / Y[0]
        CIEXYZ_Z = Z[0] / Y[0]
        return CIEXYZ_X, CIEXYZ_Y, CIEXYZ_Z
    return 0, 0, 0

def GetSigObject(sig, type, _fd, size):
    # _fd is already seeked to starting point of data
    # 4bytes type(description) is included in size
    sigDescObj = None
    if sig == "A2B0":
        pass
    elif sig == "A2B1":
        pass
    elif sig == "A2B1":
        pass
    elif sig == "A2B0":
        pass
    elif sig == "A2B1":
        pass
    elif sig == "A2B2":
        pass
    elif sig in ["bXYZ", "gXYZ", "rXYZ", "bkpt", "wtpt"]:
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
    elif sig == "targ":
        pass
    elif sig == "cprt":
        content = ''.join(getChar(_fd) for _ in xrange(size-4))
        log(" cpry content = %s"%(content))
        sigDescObj = Text(sig, content)
        pass
    elif sig == "dmnd":
        pass
    elif sig == "dmdd":
        pass
    elif sig == "gamt":
        pass
    elif sig == "kTRC":
        pass
    elif sig == "lumi":
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
    elif sig == "desc":
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
    elif sig == "scrd":
        pass
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
                typeDesc = ''.join(getChar(self._fd) for _ in xrange(4))
                log("Tag sig(%s) / type(%s) / offset(%d) / size(%d)"%(sig, typeDesc, offset, size))

                sigDescObj = None
                if typeDesc == "desc":
                    reserved = getBytes4(self._fd)
                    assert reserved == 0
                    asciiCount = getBytes4(self._fd)
                    log(" asciiCount = %d"%(asciiCount))
                    asciiInvariantDesc = getChar(self._fd, asciiCount)
                    log(" asciiInvariantDesc = %s"%(asciiInvariantDesc))
                    uniLangCode = getBytes4(self._fd)
                    uniCount = getBytes4(self._fd)
                    log(" uniLangCode, uniCount = %d, %d"%(uniLangCode, uniCount))
                    if uniLangCode != 0 and uniCount != 0:
                        uniLocalizableDesc = getChar(self._fd, uniCount)
                        log(" uniLocalizableDesc = %s"%(uniLocalizableDesc))
                    scriptCode = getBytes2(self._fd)
                    scriptCount = getCharToOrd(self._fd)
                    log(" scriptCode, scriptCount = %d, %d"%(scriptCode, scriptCount))
                    if scriptCode != 0 and scriptCount != 0:
                        localMacintoshDesc = getChar(self._fd, scriptCount)
                        log(" localMacintoshDesc = %s"%(localMacintoshDesc))
                else:
                    sigDescObj = GetSigObject(sig, typeDesc, self._fd, size)

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
