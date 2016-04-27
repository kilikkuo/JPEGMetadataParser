# exif tag definition.
#http://www.media.mit.edu/pia/Research/deepview/exif.html
BYTE_ALIGN_INTEL    = 0x4949
BYTE_ALIGN_MOTOROLA = 0x4d4d

# Start Of Frame N
# N indicates the compression process, only SOF0~SOF2 are commonly used.
# Nondifferential Huffman-coding frames
JPEG_SOF0   = 0xc0 # Baseline DCT
JPEG_SOF1   = 0xc1 # Extended sequential DCT
JPEG_SOF2   = 0xc2 # Progressive DCT
JPEG_SOF3   = 0xc3 # Lossless (sequential)
# Differential Huffman-coding frames
JPEG_SOF5   = 0xc5 # Differential sequential DCT
JPEG_SOF6   = 0xc6 # Differential progressive DCT
JPEG_SOF7   = 0xc7 # Differential lossless
# Nodifferential arithmetic-coding frames
JPEG_SOF9   = 0xc9 # Extended sequential DCT
JPEG_SOF10  = 0xca # Progressive DCT
JPEG_SOF11  = 0xcb # Lossless (sequential)
# Differential arithmetic-coding frames
JPEG_SOF13  = 0xcd # Differential sequential DCT
JPEG_SOF14  = 0xce # Differential progressive DCT
JPEG_SOF15  = 0xcf # Differential lossless

JPEG_SOI    = 0xd8 # Start Of Image
JPEG_EOI    = 0xd9 # End Of Image
JPEG_SOS    = 0xda # Start Of Scan
JPEG_APP0   = 0xe0 # Jfif marker
JPEG_APP1   = 0xe1 # Exif marker
JPEG_APP2   = 0xe2
JPEG_COM    = 0xfe # Comment
JPEG_DQT    = 0xdb # Define quantization table(s)
JPEG_DHT    = 0xc4 # Define Huffman table(s)
JPEG_DRI    = 0xdd # Define restart interval
JPEG_APP13  = 0xed

# Tags used by IFD0 (main image)
# http://www.awaresystems.be/imaging/tiff.html
# Baseline TIFF tags are those tags that are listed as part of the core of TIFF,
# the essentials that all mainstream TIFF developers should support in their
# products, according to the TIFF specification.
TAGID_NewSubFileType            = 0x00fe
TAGID_SubFileType               = 0x00ff
TAGID_ImageWidth                = 0x0100
TAGID_ImageHeight               = 0x0101
TAGID_BitsPerSample             = 0x0102
TAGID_Compression               = 0x0103
TAGID_PhotometricInterpretation = 0x0106
TAGID_ThreshHolding             = 0x0107
TAGID_CellWidth                 = 0x0108
TAGID_CellLength                = 0x0109
TAGID_FillOrder                 = 0x010a
TAGID_ImageDescription          = 0x010e
TAGID_Make                      = 0x010f
TAGID_Model                     = 0x0110
TAGID_StripOffsets              = 0x0111
TAGID_Orientation               = 0x0112
TAGID_SamplePerPixel            = 0x0115
TAGID_RowsPerStrip              = 0x0116
TAGID_StripByteCounts           = 0x0117
TAGID_MinSampleValue            = 0x0118
TAGID_MaxSampleValue            = 0x0119
TAGID_XResolution               = 0x011a
TAGID_YResolution               = 0x011b
TAGID_PlanarConfiguration       = 0x011c
TAGID_FreeOffsets               = 0x0120
TAGID_FreeByteCounts            = 0x0121
TAGID_GrayResponseUnit          = 0x0122
TAGID_GrayResponseCurve         = 0x0123
TAGID_ResolutionUnit            = 0x0128
TAGID_Software                  = 0x0131
TAGID_DateTime                  = 0x0132
TAGID_Artist                    = 0x013b
TAGID_HostComputer              = 0x013c
TAGID_ColorMap                  = 0x0140
TAGID_ExtraSample               = 0x0152
TAGID_COPYRIGHT                 = 0x8298
# Extension tags
# Private tags
# Private IFD tags

lstMsgTags = []
def log(msg, tag=None, op=None):
    if op == 'add' and tag not in lstMsgTags:
        lstMsgTags.append(tag)
    strTag = ''
    for t in lstMsgTags:
        strTag += t
    print strTag + " " + msg
    if op == 'remove' and tag in lstMsgTags:
        lstMsgTags.remove(tag)

class IFDEntry:
    def __init__(self, tag, format, comps, offset):
        self.__tagNumber = tag
        self.__dataFormat = format
        self.__numberOfComponents = comps
        self.__dataValueOffset = offset

class JPEGMetadataParser:
    def __init__(self):
        self._file = None
        self._orderAPP1 = None
        pass

    def __getcToOrd(self):
        if not self._file:
            assert False
        c = self._file.read(1)
        if c == '':
            return -1
        return ord(c)

    def __getLen2(self, order=BYTE_ALIGN_MOTOROLA):
        # 0x4d4d for MM / 0x4949 for II.
        lenLow = self.__getcToOrd()
        lenHigh = self.__getcToOrd()
        if order == BYTE_ALIGN_MOTOROLA:
            return lenLow << 8 | lenHigh
        else:
            return lenLow | lenHigh << 8

    def __getLen4(self, order=BYTE_ALIGN_MOTOROLA):
        # 0x4d4d for MM / 0x4949 for II.
        lenLL = self.__getcToOrd()
        lenLH = self.__getcToOrd()
        lenHL = self.__getcToOrd()
        lenHH = self.__getcToOrd()
        if order == BYTE_ALIGN_MOTOROLA:
            return lenLL << 24 | lenLH << 16 | lenHL << 8 | lenHH
        else:
            return lenLL | lenLH << 8 | lenHL << 16 | lenHH << 24

    def __parseBasicIFD(self, base, start, end):
        log("Enter", "[BasicIFD]", "add")
        def checkEntryValid(format, comps):
            lstDataFormat = [1,1,2,4,8,1,1,2,4,8,4,8]
            if 0 == format or format > len(lstDataFormat):
                return False
            bytesPerComp = lstDataFormat[format]
            if bytesPerComp * comps > 4:
                offset = self.__getLen4(self._orderAPP1)
                if offset <= start and offset >= end:
                    return False
                self._file.seek(offset)
            return True

        if not self._file:
            assert False
        entries = self.__getLen2(self._orderAPP1)
        log("Number of entries = %d"%(entries))

        for idx in xrange(entries):
            tag = self.__getLen2(self._orderAPP1)
            dataFormat = self.__getLen2(self._orderAPP1)
            numOfComps = self.__getLen4(self._orderAPP1)
            dataOffset = self.__getLen4(self._orderAPP1)

            curPos = self._file.tell()
            isValid = checkEntryValid(dataFormat, numOfComps)
            if isValid:
                entry = IFDEntry(tag, dataFormat, numOfComps, dataOffset)
                log("Entry(%d), %s, %d, %d, %d"%(idx, hex(tag), dataFormat, numOfComps, dataOffset))
        log("Leave", "[BasicIFD]", "remove")

    def __parseAPP1(self, base, start, end):
        if not self._file:
            assert False

        self._file.seek(base)
        self._orderAPP1 = self.__getLen2()
        log("order = %s"%(hex(self._orderAPP1)))

        if self._orderAPP1 not in [BYTE_ALIGN_MOTOROLA, BYTE_ALIGN_INTEL]:
            log("order incorrect")
            assert False

        check = self.__getLen2(self._orderAPP1)
        if check != 0x002a:
            assert False

        offsetToIFD = self.__getLen4(self._orderAPP1)
        log("offsetToIFD = %s"%(hex(offsetToIFD)))
        self._file.seek(base+offsetToIFD)
        self.__parseBasicIFD(base, start, end)

    def __parseXMP(self):
        if not self._file:
            assert False

    def parse(self, filePath):
        self._file = open(filePath)
        self._file.seek(0)
        first = self.__getcToOrd()
        marker = self.__getcToOrd()
        if (first != 0xff or marker != JPEG_SOI):
            assert False, "Not in JPEG format !!"

        while (marker):
            first = self.__getcToOrd()
            if first != 0xff or first < 0:
                break
            marker = self.__getcToOrd()
            log("%s-%s"%(hex(first), hex(marker)))
            len = self.__getLen2()
            curPos = self._file.tell()
            log("len= %d, curPos=%d"%(len,curPos))

            if marker in [JPEG_EOI, JPEG_SOS]:
                log("EOI or SOS ... exit parsing")
                break
            elif marker == JPEG_APP0:
                log("Enter", "[APP0]", "add")
                log("Leave", "[APP0]", "remove")
                pass # TBD
            elif marker == JPEG_APP1:
                log("Enter", "[APP1]", "add")
                header = self._file.read(4)
                log("header = %s"%(header))
                if header.lower() == 'exif':
                    self.__parseAPP1(curPos+6, curPos, curPos+len-2)
                elif header.lower() == 'http':
                    pass
                log("Leave", "[APP1]", "remove")

            elif marker == JPEG_APP2:
                log("Enter", "[APP2]", "add")
                log("Leave", "[APP2]", "remove")
                pass # TBD
            elif marker == JPEG_APP13:
                log("Enter", "[APP13]", "add")
                log("Leave", "[APP13]", "remove")
                pass # TBD
            self._file.seek(curPos+len-2)

import os
fPath = "./images/brownie.jpg"
fullPath = os.path.abspath(fPath)

jpgParser = JPEGMetadataParser()
jpgParser.parse(fullPath)
