import weakref
from misc import log
from FileOPs import nowAt, seekTo, getChar, getCharToOrd, getBytes2, getBytes4,\
                    getBytes8, BYTE_ALIGN_INTEL, BYTE_ALIGN_MOTOROLA

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
