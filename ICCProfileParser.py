import weakref
from misc import log
from FileOPs import nowAt, seekTo, getChar, getCharToOrd, getBytes2, getBytes4,\
                    getBytes8, BYTE_ALIGN_INTEL, BYTE_ALIGN_MOTOROLA

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

class Type(object):
    def __init__(self):
        pass

class Curve(Type):
    descriptor = "curv"
    def __init__(self):
        Type.__init__(self)

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
    def __init__(self):
        Type.__init__(self)

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
    def __init__(self):
        Type.__init__(self)

class TextDescription(Type):
    descriptor = "desc"
    def __init__(self):
        Type.__init__(self)

class Text(Type):
    descriptor = "text"
    def __init__(self):
        Type.__init__(self)

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
    def __init__(self):
        Type.__init__(self)

class XYZ(Type):
    descriptor = "XYZ "
    def __init__(self):
        Type.__init__(self)


class ICCProfileParser(object):
    def __init__(self, fd, data, length):
        self.__dicICC = {}
        self._fdWRef = weakref.ref(fd)
        self.__parseICCProfile(data, length)

    def __getattr__(self, attr):
        if attr == "_fd":
            return self._fdWRef()
        else:
            raise AttributeError

    def __parseICCProfile(self, iccData, iccLen):
        # Refer to http://blog.fpmurphy.com/2012/03/extract-icc-profile-from-images.html

        basePos = nowAt(self._fd)
        def parseHeader():
            log("Enter", "[ICCProfileHeader]", "add")
            profileSize = getBytes4(self._fd)
            cmmType = ''.join(getChar(self._fd) for _ in xrange(4))
            lstVersion = [getCharToOrd(self._fd) for _ in xrange(4)]
            log("ICCProfile version = %s"%str(lstVersion))

            deviceClass = ''.join(getChar(self._fd) for _ in xrange(4))
            log("Profile Size = %d, %s, %s"%(profileSize, cmmType, deviceClass))

            colorSpaceOfData = ''.join(getChar(self._fd) for _ in xrange(4))
            pcs = ''.join(getChar(self._fd) for _ in xrange(4))
            log("CS Data, pcs = %s, %s"%(colorSpaceOfData, pcs))

            lstDatetime = [getBytes2(self._fd) for _ in xrange(6)]
            log("Datatime = Y(%d)M(%d)D(%d)H(%d)M(%d)S(%d)"%tuple(lstDatetime))

            signature = ''.join(getChar(self._fd) for _ in xrange(4))
            primaryPlatform = ''.join(getChar(self._fd) for _ in xrange(4))
            log("signature, primaryPlatform = %s, %s"%(signature, primaryPlatform))

            lstProfileFlags = [hex(getCharToOrd(self._fd)) for _ in xrange(4)]
            log("Profile Flags = %s"%str(lstProfileFlags))

            deviceManufacturer = ''.join(getChar(self._fd) for _ in xrange(4))
            deviceModel = ''.join(getChar(self._fd) for _ in xrange(4))
            log("deviceManufacturer, deviceModel = %s, %s"%(deviceManufacturer, deviceModel))

            lstDeviceAttributes = [hex(getCharToOrd(self._fd)) for _ in xrange(8)]
            log("Device Attributes = %s"%str(lstDeviceAttributes))

            renderingIntent, zeroPadding = getBytes2(self._fd), getBytes2(self._fd)
            log("Rendering Intent = %d"%(renderingIntent))

            intX, intY, intZ = getBytes4(self._fd), getBytes4(self._fd), getBytes4(self._fd)
            import struct
            X = struct.unpack('f', struct.pack('i', intX))
            Y = struct.unpack('f', struct.pack('i', intY))
            Z = struct.unpack('f', struct.pack('i', intZ))
            CIEXYZ_X = X[0] / Y[0]
            CIEXYZ_Y = Y[0] / Y[0]
            CIEXYZ_Z = Z[0] / Y[0]
            log("CIEXYZ = (%f, %f, %f)"%(CIEXYZ_X, CIEXYZ_Y, CIEXYZ_Z))

            profileCreator = ''.join(getChar(self._fd) for _ in xrange(4))
            log("Profile Creator = %s"%(profileCreator))
            profileID = [hex(getCharToOrd(self._fd)) for _ in xrange(16)]
            log("Profile ID = %s"%(str(profileID)))
            reserved = [hex(getCharToOrd(self._fd)) for _ in xrange(28)]
            log("Reserved = %s"%(str(reserved)))
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
                log("Tag sig(%s) / offset(%d) / size(%d)"%(sig, offset, size))
                seekTo(self._fd, basePos+offset)
                typeDesc = ''.join(getChar(self._fd) for _ in xrange(4))
                if typeDesc == "curv":
                    reserved = getBytes4(self._fd)
                    assert reserved == 0
                    count = getBytes4(self._fd)
                    log(" count = %d"%(count))
                    if count == 0:
                        exp = 1.0
                    else:
                        first, second = getCharToOrd(self._fd), getCharToOrd(self._fd)
                        exp = first + float(second/256.0)
                    log(" exp = %f"%(exp))
                elif typeDesc == "XYZ ":
                    reserved = getBytes4(self._fd)
                    assert reserved == 0
                    assert size == 20
                    intX, intY, intZ = getBytes4(self._fd), getBytes4(self._fd), getBytes4(self._fd)
                    if intX != 0 and intY != 0 and intZ != 0:
                        import struct
                        X = struct.unpack('f', struct.pack('i', intX))
                        Y = struct.unpack('f', struct.pack('i', intY))
                        Z = struct.unpack('f', struct.pack('i', intZ))
                        CIEXYZ_X = X[0] / Y[0]
                        CIEXYZ_Y = Y[0] / Y[0]
                        CIEXYZ_Z = Z[0] / Y[0]
                        log("CIEXYZ = (%f, %f, %f)"%(CIEXYZ_X, CIEXYZ_Y, CIEXYZ_Z))
                    else:
                        log("CIEXYZ = (%f, %f, %f)"%(0, 0, 0))
                elif typeDesc == "text":
                    text = ''.join(getChar(self._fd) for _ in xrange(size-4))
                    log(" txt = %s"%(text))
                elif typeDesc == "desc":
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
                    pass
                seekTo(self._fd, tagStartPos+12)

            log("Leave", "[ICCProfileTagTable]", "remove")
            pass
            #tagCount = getBytes4(self._fd)
            #print "Tag count = %d"%(tagCount)

        parseHeader()
        parseTagTable()
