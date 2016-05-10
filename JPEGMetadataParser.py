"""
 By Kilik Kuo. Released under the MIT license.
 See file LICENSE for detail or copy at https://opensource.org/licenses/MIT
"""

# exif tag definition.
# http://www.media.mit.edu/pia/Research/deepview/exif.html
# ====
# metadata structure
# http://metalith.ru/en/help_files/structure.htm
# ===
# Exchangeable image file format for digital still cameras: Exif Version 2.3
# http://www.cipa.jp/std/documents/e/DC-008-2012_E.pdf
# ===

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
# ===========================================================
# Baseline
"""
Baseline TIFF tags are those tags that are listed as part of the core of TIFF,
the essentials that all mainstream TIFF developers should support in their
products, according to the TIFF specification.
"""
TAGID_NewSubfileType                  = 0x00FE
TAGID_SubfileType                     = 0x00FF
TAGID_ImageWidth                      = 0x0100
TAGID_ImageLength                     = 0x0101
TAGID_BitsPerSample                   = 0x0102
TAGID_Compression                     = 0x0103
TAGID_PhotometricInterpretation       = 0x0106
TAGID_Threshholding                   = 0x0107
TAGID_CellWidth                       = 0x0108
TAGID_CellLength                      = 0x0109
TAGID_FillOrder                       = 0x010A
TAGID_ImageDescription                = 0x010E
TAGID_Make                            = 0x010F
TAGID_Model                           = 0x0110
TAGID_StripOffsets                    = 0x0111
TAGID_Orientation                     = 0x0112
TAGID_SamplesPerPixel                 = 0x0115
TAGID_RowsPerStrip                    = 0x0116
TAGID_StripByteCounts                 = 0x0117
TAGID_MinSampleValue                  = 0x0118
TAGID_MaxSampleValue                  = 0x0119
TAGID_XResolution                     = 0x011A
TAGID_YResolution                     = 0x011B
TAGID_PlanarConfiguration             = 0x011C
TAGID_FreeOffsets                     = 0x0120
TAGID_FreeByteCounts                  = 0x0121
TAGID_GrayResponseUnit                = 0x0122
TAGID_GrayResponseCurve               = 0x0123
TAGID_ResolutionUnit                  = 0x0128
TAGID_Software                        = 0x0131
TAGID_DateTime                        = 0x0132
TAGID_Artist                          = 0x013B
TAGID_HostComputer                    = 0x013C
TAGID_ColorMap                        = 0x0140
TAGID_ExtraSamples                    = 0x0152
TAGID_Copyright                       = 0x8298
# ===========================================================
# Extension tags
"""
Extension TIFF tags are those tags listed as part of TIFF features that may
not be supported by all TIFF readers, according to the TIFF specification.
"""
TAGID_DocumentName                    = 0x010D
TAGID_PageName                        = 0x011D
TAGID_XPosition                       = 0x011E
TAGID_YPosition                       = 0x011F
TAGID_T4Options                       = 0x0124
TAGID_T6Options                       = 0x0125
TAGID_PageNumber                      = 0x0129
TAGID_TransferFunction                = 0x012D
TAGID_Predictor                       = 0x013D
TAGID_WhitePoint                      = 0x013E
TAGID_PrimaryChromaticities           = 0x013F
TAGID_HalftoneHints                   = 0x0141
TAGID_TileWidth                       = 0x0142
TAGID_TileLength                      = 0x0143
TAGID_TileOffsets                     = 0x0144
TAGID_TileByteCounts                  = 0x0145
TAGID_BadFaxLines                     = 0x0146
TAGID_CleanFaxData                    = 0x0147
TAGID_ConsecutiveBadFaxLines          = 0x0148
TAGID_SubIFDs                         = 0x014A
TAGID_InkSet                          = 0x014C
TAGID_InkNames                        = 0x014D
TAGID_NumberOfInks                    = 0x014E
TAGID_DotRange                        = 0x0150
TAGID_TargetPrinter                   = 0x0151
TAGID_SampleFormat                    = 0x0153
TAGID_SMinSampleValue                 = 0x0154
TAGID_SMaxSampleValue                 = 0x0155
TAGID_TransferRange                   = 0x0156
TAGID_ClipPath                        = 0x0157
TAGID_XClipPathUnits                  = 0x0158
TAGID_YClipPathUnits                  = 0x0159
TAGID_Indexed                         = 0x015A
TAGID_JPEGTables                      = 0x015B
TAGID_OPIProxy                        = 0x015F
TAGID_GlobalParametersIFD             = 0x0190
TAGID_ProfileType                     = 0x0191
TAGID_FaxProfile                      = 0x0192
TAGID_CodingMethods                   = 0x0193
TAGID_VersionYear                     = 0x0194
TAGID_ModeNumber                      = 0x0195
TAGID_Decode                          = 0x01B1
TAGID_DefaultImageColor               = 0x01B2
TAGID_JPEGProc                        = 0x0200
TAGID_JPEGInterchangeFormat           = 0x0201
TAGID_JPEGInterchangeFormatLength     = 0x0202
TAGID_JPEGRestartInterval             = 0x0203
TAGID_JPEGLosslessPredictors          = 0x0205
TAGID_JPEGPointTransforms             = 0x0206
TAGID_JPEGQTables                     = 0x0207
TAGID_JPEGDCTables                    = 0x0208
TAGID_JPEGACTables                    = 0x0209
TAGID_YCbCrCoefficients               = 0x0211
TAGID_YCbCrSubSampling                = 0x0212
TAGID_YCbCrPositioning                = 0x0213
TAGID_ReferenceBlackWhite             = 0x0214
TAGID_StripRowCounts                  = 0x022F
TAGID_XMP                             = 0x02BC
TAGID_ImageID                         = 0x800D
TAGID_ImageLayer                      = 0x87AC
# ===========================================================
# Private tags
"""
Private TIFF tags are, at least originally, allocated by Adobe for
organizations that wish to store information meaningful only to that
organization in a TIFF file. The private tags listed here are the ones that
found their way into the public domain and more general applications, and the
ones that the owning organizations documented for the benefit of the TIFF community.
"""
TAGID_WangAnnotation                  = 0x80A4
TAGID_MDFileTag                       = 0x82A5
TAGID_MDScalePixel                    = 0x82A6
TAGID_MDColorTable                    = 0x82A7
TAGID_MDLabName                       = 0x82A8
TAGID_MDSampleInfo                    = 0x82A9
TAGID_MDPrepDate                      = 0x82AA
TAGID_MDPrepTime                      = 0x82AB
TAGID_MDFileUnits                     = 0x82AC
TAGID_ModelPixelScaleTag              = 0x830E
TAGID_IPTC                            = 0x83BB
TAGID_INGRPacketDataTag               = 0x847E
TAGID_INGRFlagRegisters               = 0x847F
TAGID_IrasBTransformationMatrix       = 0x8480
TAGID_ModelTiepointTag                = 0x8482
TAGID_ModelTransformationTag          = 0x85D8
TAGID_Photoshop                       = 0x8649
TAGID_ExifIFD                         = 0x8769
TAGID_ICCProfile                      = 0x8773
TAGID_GeoKeyDirectoryTag              = 0x87AF
TAGID_GeoDoubleParamsTag              = 0x87B0
TAGID_GeoAsciiParamsTag               = 0x87B1
TAGID_GPSIFD                          = 0x8825
TAGID_HylaFAXFaxRecvParams            = 0x885C
TAGID_HylaFAXFaxSubAddress            = 0x885D
TAGID_HylaFAXFaxRecvTime              = 0x885E
TAGID_ImageSourceData                 = 0x935C
TAGID_InteroperabilityIFD             = 0xA005
TAGID_GDAL_METADATA                   = 0xA480
TAGID_GDAL_NODATA                     = 0xA481
TAGID_OceScanjobDescription           = 0xC427
TAGID_OceApplicationSelector          = 0xC428
TAGID_OceIdentificationNumber         = 0xC429
TAGID_OceImageLogicCharacteristics    = 0xC42A
TAGID_DNGVersion                      = 0xC612
TAGID_DNGBackwardVersion              = 0xC613
TAGID_UniqueCameraModel               = 0xC614
TAGID_LocalizedCameraModel            = 0xC615
TAGID_CFAPlaneColor                   = 0xC616
TAGID_CFALayout                       = 0xC617
TAGID_LinearizationTable              = 0xC618
TAGID_BlackLevelRepeatDim             = 0xC619
TAGID_BlackLevel                      = 0xC61A
TAGID_BlackLevelDeltaH                = 0xC61B
TAGID_BlackLevelDeltaV                = 0xC61C
TAGID_WhiteLevel                      = 0xC61D
TAGID_DefaultScale                    = 0xC61E
TAGID_DefaultCropOrigin               = 0xC61F
TAGID_DefaultCropSize                 = 0xC620
TAGID_ColorMatrix1                    = 0xC621
TAGID_ColorMatrix2                    = 0xC622
TAGID_CameraCalibration1              = 0xC623
TAGID_CameraCalibration2              = 0xC624
TAGID_ReductionMatrix1                = 0xC625
TAGID_ReductionMatrix2                = 0xC626
TAGID_AnalogBalance                   = 0xC627
TAGID_AsShotNeutral                   = 0xC628
TAGID_AsShotWhiteXY                   = 0xC629
TAGID_BaselineExposure                = 0xC62A
TAGID_BaselineNoise                   = 0xC62B
TAGID_BaselineSharpness               = 0xC62C
TAGID_BayerGreenSplit                 = 0xC62D
TAGID_LinearResponseLimit             = 0xC62E
TAGID_CameraSerialNumber              = 0xC62F
TAGID_LensInfo                        = 0xC630
TAGID_ChromaBlurRadius                = 0xC631
TAGID_AntiAliasStrength               = 0xC632
TAGID_DNGPrivateData                  = 0xC634
TAGID_MakerNoteSafety                 = 0xC635
TAGID_CalibrationIlluminant1          = 0xC65A
TAGID_CalibrationIlluminant2          = 0xC65B
TAGID_BestQualityScale                = 0xC65C
TAGID_AliasLayerMetadata              = 0xC660
# Private IFD tags ==========================================
# EXIF
"""
Exif tags are used largely to encode additional information related to image
generation by digital still cameras. Exif is the abbreviation of 'Exchangeable
image file format', though this can be argued to be a misnomer, as Exif does
not relate to TIFF like e.g. JFIF relates to JPEG.
"""
TAGID_ExposureTime                    = 0x829A
TAGID_FNumber                         = 0x829D
TAGID_ExposureProgram                 = 0x8822
TAGID_SpectralSensitivity             = 0x8824
TAGID_ISOSpeedRatings                 = 0x8827
TAGID_OECF                            = 0x8828
TAGID_ExifVersion                     = 0x9000
TAGID_DateTimeOriginal                = 0x9003
TAGID_DateTimeDigitized               = 0x9004
TAGID_ComponentsConfiguration         = 0x9101
TAGID_CompressedBitsPerPixel          = 0x9102
TAGID_ShutterSpeedValue               = 0x9201
TAGID_ApertureValue                   = 0x9202
TAGID_BrightnessValue                 = 0x9203
TAGID_ExposureBiasValue               = 0x9204
TAGID_MaxApertureValue                = 0x9205
TAGID_SubjectDistance                 = 0x9206
TAGID_MeteringMode                    = 0x9207
TAGID_LightSource                     = 0x9208
TAGID_Flash                           = 0x9209
TAGID_FocalLength                     = 0x920A
TAGID_SubjectArea                     = 0x9214
TAGID_MakerNote                       = 0x927C
TAGID_UserComment                     = 0x9286
TAGID_SubsecTime                      = 0x9290
TAGID_SubsecTimeOriginal              = 0x9291
TAGID_SubsecTimeDigitized             = 0x9292
TAGID_FlashpixVersion                 = 0xA000
TAGID_ColorSpace                      = 0xA001
TAGID_PixelXDimension                 = 0xA002
TAGID_PixelYDimension                 = 0xA003
TAGID_RelatedSoundFile                = 0xA004
TAGID_FlashEnergy                     = 0xA20B
TAGID_SpatialFrequencyResponse        = 0xA20C
TAGID_FocalPlaneXResolution           = 0xA20E
TAGID_FocalPlaneYResolution           = 0xA20F
TAGID_FocalPlaneResolutionUnit        = 0xA210
TAGID_SubjectLocation                 = 0xA214
TAGID_ExposureIndex                   = 0xA215
TAGID_SensingMethod                   = 0xA217
TAGID_FileSource                      = 0xA300
TAGID_SceneType                       = 0xA301
TAGID_CFAPattern                      = 0xA302
TAGID_CustomRendered                  = 0xA401
TAGID_ExposureMode                    = 0xA402
TAGID_WhiteBalance                    = 0xA403
TAGID_DigitalZoomRatio                = 0xA404
TAGID_FocalLengthIn35mmFilm           = 0xA405
TAGID_SceneCaptureType                = 0xA406
TAGID_GainControl                     = 0xA407
TAGID_Contrast                        = 0xA408
TAGID_Saturation                      = 0xA409
TAGID_Sharpness                       = 0xA40A
TAGID_DeviceSettingDescription        = 0xA40B
TAGID_SubjectDistanceRange            = 0xA40C
TAGID_ImageUniqueID                   = 0xA420
# ====
# GPS
"""
GPS tags are used to encode positioning information, related largely to image
generation by digital still cameras.
"""
TAGID_GPSVersionID                    = 0x0000
TAGID_GPSLatitudeRef                  = 0x0001
TAGID_GPSLatitude                     = 0x0002
TAGID_GPSLongitudeRef                 = 0x0003
TAGID_GPSLongitude                    = 0x0004
TAGID_GPSAltitudeRef                  = 0x0005
TAGID_GPSAltitude                     = 0x0006
TAGID_GPSTimeStamp                    = 0x0007
TAGID_GPSSatellites                   = 0x0008
TAGID_GPSStatus                       = 0x0009
TAGID_GPSMeasureMode                  = 0x000A
TAGID_GPSDOP                          = 0x000B
TAGID_GPSSpeedRef                     = 0x000C
TAGID_GPSSpeed                        = 0x000D
TAGID_GPSTrackRef                     = 0x000E
TAGID_GPSTrack                        = 0x000F
TAGID_GPSImgDirectionRef              = 0x0010
TAGID_GPSImgDirection                 = 0x0011
TAGID_GPSMapDatum                     = 0x0012
TAGID_GPSDestLatitudeRef              = 0x0013
TAGID_GPSDestLatitude                 = 0x0014
TAGID_GPSDestLongitudeRef             = 0x0015
TAGID_GPSDestLongitude                = 0x0016
TAGID_GPSDestBearingRef               = 0x0017
TAGID_GPSDestBearing                  = 0x0018
TAGID_GPSDestDistanceRef              = 0x0019
TAGID_GPSDestDistance                 = 0x001A
TAGID_GPSProcessingMethod             = 0x001B
TAGID_GPSAreaInformation              = 0x001C
TAGID_GPSDateStamp                    = 0x001D
TAGID_GPSDifferential                 = 0x001E
# ====
# Interoperability
"""
The single Interoperability tag is used to encode compability information,
related to image generation by digital still cameras.
"""
TAGID_InteroperabilityIndex           = 0x0001
# ===========================================================
{0: 'GPSVersionID',
 1: 'GPSLatitudeRef',
 2: 'GPSLatitude',
 3: 'GPSLongitudeRef',
 4: 'GPSLongitude',
 5: 'GPSAltitudeRef',
 6: 'GPSAltitude',
 7: 'GPSTimeStamp',
 8: 'GPSSatellites',
 9: 'GPSStatus',
 10: 'GPSMeasureMode',
 11: 'GPSDOP',
 12: 'GPSSpeedRef',
 13: 'GPSSpeed',
 14: 'GPSTrackRef',
 15: 'GPSTrack',
 16: 'GPSImgDirectionRef',
 17: 'GPSImgDirection',
 18: 'GPSMapDatum',
 19: 'GPSDestLatitudeRef',
 20: 'GPSDestLatitude',
 21: 'GPSDestLongitudeRef',
 22: 'GPSDestLongitude',
 23: 'GPSDestBearingRef',
 24: 'GPSDestBearing',
 25: 'GPSDestDistanceRef',
 26: 'GPSDestDistance',
 27: 'GPSProcessingMethod',
 28: 'GPSAreaInformation',
 29: 'GPSDateStamp',
 30: 'GPSDifferential',
 254: 'NewSubfileType',
 255: 'SubfileType',
 256: 'ImageWidth',
 257: 'ImageLength',
 258: 'BitsPerSample',
 259: 'Compression',
 262: 'PhotometricInterpretation',
 263: 'Threshholding',
 264: 'CellWidth',
 265: 'CellLength',
 266: 'FillOrder',
 269: 'DocumentName',
 270: 'ImageDescription',
 271: 'Make',
 272: 'Model',
 273: 'StripOffsets',
 274: 'Orientation',
 277: 'SamplesPerPixel',
 278: 'RowsPerStrip',
 279: 'StripByteCounts',
 280: 'MinSampleValue',
 281: 'MaxSampleValue',
 282: 'XResolution',
 283: 'YResolution',
 284: 'PlanarConfiguration',
 285: 'PageName',
 286: 'XPosition',
 287: 'YPosition',
 288: 'FreeOffsets',
 289: 'FreeByteCounts',
 290: 'GrayResponseUnit',
 291: 'GrayResponseCurve',
 292: 'T4Options',
 293: 'T6Options',
 296: 'ResolutionUnit',
 297: 'PageNumber',
 301: 'TransferFunction',
 305: 'Software',
 306: 'DateTime',
 315: 'Artist',
 316: 'HostComputer',
 317: 'Predictor',
 318: 'WhitePoint',
 319: 'PrimaryChromaticities',
 320: 'ColorMap',
 321: 'HalftoneHints',
 322: 'TileWidth',
 323: 'TileLength',
 324: 'TileOffsets',
 325: 'TileByteCounts',
 326: 'BadFaxLines',
 327: 'CleanFaxData',
 328: 'ConsecutiveBadFaxLines',
 330: 'SubIFDs',
 332: 'InkSet',
 333: 'InkNames',
 334: 'NumberOfInks',
 336: 'DotRange',
 337: 'TargetPrinter',
 338: 'ExtraSamples',
 339: 'SampleFormat',
 340: 'SMinSampleValue',
 341: 'SMaxSampleValue',
 342: 'TransferRange',
 343: 'ClipPath',
 344: 'XClipPathUnits',
 345: 'YClipPathUnits',
 346: 'Indexed',
 347: 'JPEGTables',
 351: 'OPIProxy',
 400: 'GlobalParametersIFD',
 401: 'ProfileType',
 402: 'FaxProfile',
 403: 'CodingMethods',
 404: 'VersionYear',
 405: 'ModeNumber',
 433: 'Decode',
 434: 'DefaultImageColor',
 512: 'JPEGProc',
 513: 'JPEGInterchangeFormat',
 514: 'JPEGInterchangeFormatLength',
 515: 'JPEGRestartInterval',
 517: 'JPEGLosslessPredictors',
 518: 'JPEGPointTransforms',
 519: 'JPEGQTables',
 520: 'JPEGDCTables',
 521: 'JPEGACTables',
 529: 'YCbCrCoefficients',
 530: 'YCbCrSubSampling',
 531: 'YCbCrPositioning',
 532: 'ReferenceBlackWhite',
 559: 'StripRowCounts',
 700: 'XMP',
 32781: 'ImageID',
 32932: 'WangAnnotation',
 33432: 'Copyright',
 33434: 'ExposureTime',
 33437: 'FNumber',
 33445: 'MDFileTag',
 33446: 'MDScalePixel',
 33447: 'MDColorTable',
 33448: 'MDLabName',
 33449: 'MDSampleInfo',
 33450: 'MDPrepDate',
 33451: 'MDPrepTime',
 33452: 'MDFileUnits',
 33550: 'ModelPixelScaleTag',
 33723: 'IPTC',
 33918: 'INGRPacketDataTag',
 33919: 'INGRFlagRegisters',
 33920: 'IrasBTransformationMatrix',
 33922: 'ModelTiepointTag',
 34264: 'ModelTransformationTag',
 34377: 'Photoshop',
 34665: 'ExifIFD',
 34675: 'ICCProfile',
 34732: 'ImageLayer',
 34735: 'GeoKeyDirectoryTag',
 34736: 'GeoDoubleParamsTag',
 34737: 'GeoAsciiParamsTag',
 34850: 'ExposureProgram',
 34852: 'SpectralSensitivity',
 34853: 'GPSIFD',
 34855: 'ISOSpeedRatings',
 34856: 'OECF',
 34908: 'HylaFAXFaxRecvParams',
 34909: 'HylaFAXFaxSubAddress',
 34910: 'HylaFAXFaxRecvTime',
 36864: 'ExifVersion',
 36867: 'DateTimeOriginal',
 36868: 'DateTimeDigitized',
 37121: 'ComponentsConfiguration',
 37122: 'CompressedBitsPerPixel',
 37377: 'ShutterSpeedValue',
 37378: 'ApertureValue',
 37379: 'BrightnessValue',
 37380: 'ExposureBiasValue',
 37381: 'MaxApertureValue',
 37382: 'SubjectDistance',
 37383: 'MeteringMode',
 37384: 'LightSource',
 37385: 'Flash',
 37386: 'FocalLength',
 37396: 'SubjectArea',
 37500: 'MakerNote',
 37510: 'UserComment',
 37520: 'SubsecTime',
 37521: 'SubsecTimeOriginal',
 37522: 'SubsecTimeDigitized',
 37724: 'ImageSourceData',
 40960: 'FlashpixVersion',
 40961: 'ColorSpace',
 40962: 'PixelXDimension',
 40963: 'PixelYDimension',
 40964: 'RelatedSoundFile',
 40965: 'InteroperabilityIFD',
 41483: 'FlashEnergy',
 41484: 'SpatialFrequencyResponse',
 41486: 'FocalPlaneXResolution',
 41487: 'FocalPlaneYResolution',
 41488: 'FocalPlaneResolutionUnit',
 41492: 'SubjectLocation',
 41493: 'ExposureIndex',
 41495: 'SensingMethod',
 41728: 'FileSource',
 41729: 'SceneType',
 41730: 'CFAPattern',
 41985: 'CustomRendered',
 41986: 'ExposureMode',
 41987: 'WhiteBalance',
 41988: 'DigitalZoomRatio',
 41989: 'FocalLengthIn35mmFilm',
 41990: 'SceneCaptureType',
 41991: 'GainControl',
 41992: 'Contrast',
 41993: 'Saturation',
 41994: 'Sharpness',
 41995: 'DeviceSettingDescription',
 41996: 'SubjectDistanceRange',
 42016: 'ImageUniqueID',
 42112: 'GDAL_METADATA',
 42113: 'GDAL_NODATA',
 50215: 'OceScanjobDescription',
 50216: 'OceApplicationSelector',
 50217: 'OceIdentificationNumber',
 50218: 'OceImageLogicCharacteristics',
 50706: 'DNGVersion',
 50707: 'DNGBackwardVersion',
 50708: 'UniqueCameraModel',
 50709: 'LocalizedCameraModel',
 50710: 'CFAPlaneColor',
 50711: 'CFALayout',
 50712: 'LinearizationTable',
 50713: 'BlackLevelRepeatDim',
 50714: 'BlackLevel',
 50715: 'BlackLevelDeltaH',
 50716: 'BlackLevelDeltaV',
 50717: 'WhiteLevel',
 50718: 'DefaultScale',
 50719: 'DefaultCropOrigin',
 50720: 'DefaultCropSize',
 50721: 'ColorMatrix1',
 50722: 'ColorMatrix2',
 50723: 'CameraCalibration1',
 50724: 'CameraCalibration2',
 50725: 'ReductionMatrix1',
 50726: 'ReductionMatrix2',
 50727: 'AnalogBalance',
 50728: 'AsShotNeutral',
 50729: 'AsShotWhiteXY',
 50730: 'BaselineExposure',
 50731: 'BaselineNoise',
 50732: 'BaselineSharpness',
 50733: 'BayerGreenSplit',
 50734: 'LinearResponseLimit',
 50735: 'CameraSerialNumber',
 50736: 'LensInfo',
 50737: 'ChromaBlurRadius',
 50738: 'AntiAliasStrength',
 50740: 'DNGPrivateData',
 50741: 'MakerNoteSafety',
 50778: 'CalibrationIlluminant1',
 50779: 'CalibrationIlluminant2',
 50780: 'BestQualityScale',
 50784: 'AliasLayerMetadata'}
# ===========================================================
lstMsgTags = []
def log(msg, tag=None, op=None):
    if op == 'add' and tag not in lstMsgTags:
        lstMsgTags.append(tag)
    strTag = ''.join(lstMsgTags)
    print strTag + " " + msg
    if op == 'remove' and tag in lstMsgTags:
        lstMsgTags.remove(tag)

class IFDEntry:
    def __init__(self, tag, bytesPerComp):
        self.__tagNumber = tag
        self.__bytesPerComponent = 0
        self.__value = None

    def setData(self, value):
        self.__value = value

    def getTag(self):
        return self.__tagNumber

    def getValue(self):
        assert not (len(self.__value) != 1), "Contains not exact 1 element !"
        return self.__value[0]

EXIF_TIFF_DATAFORMAT_LIST = [1,1,1,2,4,8,1,1,2,4,8,4,8]
class JPEGMetadataParser:
    def __init__(self):
        self._file = None
        self._orderAPP1 = None
        pass

    def __getChar(self):
        if not self._file:
            assert False
        return self._file.read(1)

    def __getcToOrd(self):
        if not self._file:
            assert False
        c = self._file.read(1)
        if c == '':
            return -1
        return ord(c)

    def __getLen2(self, order=BYTE_ALIGN_MOTOROLA):
        # 0x4d4d for MM / 0x4949 for II.
        L = self.__getcToOrd()
        H = self.__getcToOrd()
        if order == BYTE_ALIGN_MOTOROLA:
            return L << 8 | H
        else:
            return L | H << 8

    def __getLen4(self, order=BYTE_ALIGN_MOTOROLA):
        # 0x4d4d for MM / 0x4949 for II.
        LL = self.__getcToOrd()
        LH = self.__getcToOrd()
        HL = self.__getcToOrd()
        HH = self.__getcToOrd()
        if order == BYTE_ALIGN_MOTOROLA:
            return LL << 24 | LH << 16 | HL << 8 | HH
        else:
            return LL | LH << 8 | HL << 16 | HH << 24

    def __getLen8(self, order=BYTE_ALIGN_MOTOROLA):
        # 0x4d4d for MM / 0x4949 for II.
        LLL = self.__getcToOrd()
        LLH = self.__getcToOrd()
        LHL = self.__getcToOrd()
        LHH = self.__getcToOrd()
        HLL = self.__getcToOrd()
        HLH = self.__getcToOrd()
        HHL = self.__getcToOrd()
        HHH = self.__getcToOrd()
        if order == BYTE_ALIGN_MOTOROLA:
            return LLL << 56 | LLH << 48 | LHL << 40 | LHH << 32 |\
                    HLL << 24 | HLH << 16 | HHL << 8 | HHH
        else:
            return LLL | LLH << 8 | LHL << 16 | LHH << 24 |\
                    HLL << 32 | HLH << 40 | HHL << 48 | HHH << 56

    def __getDataFromFormat(self, tag, format, size):
        from array import array
        bytesPerComp = EXIF_TIFF_DATAFORMAT_LIST[format]
        entry = IFDEntry(tag, bytesPerComp)
        print 'format(%d)/Size(%d)'%(format, size)
        lstValue = []
        if format in [1, 6, 7]:
            # unsigned byte / # signed byte / # undefined
            data = array('b', self._file.read(size))
            pass
        elif format == 2:
            # ascii string
            data = array('c', self._file.read(size))
            pass
        elif format in [3, 8]:
            # unsigned short / # signed short
            while size > 0:
                v = self.__getLen2(self._orderAPP1)
                lstValue.append(v)
                size -= 2
            encode = 'H' if format == 3 else 'h'
            data = array('H', lstValue)
            pass
        elif format in [4, 9]:
            # unsigned long / # signed long
            while size > 0:
                v = self.__getLen4(self._orderAPP1)
                lstValue.append(v)
                size -= 4
            encode = 'L' if format == 4 else 'l'
            data = array('L', lstValue)
            pass
        elif format in [5, 10]:
            # unsigned rational / # signed rational
            while size > 0:
                numerator = self.__getLen4(self._orderAPP1)
                denominator = self.__getLen4(self._orderAPP1)
                size -= 8
                lstValue.append(float(numerator) / float(denominator))
            data = array('d', lstValue)
            pass
        elif format == 11:
            # signed float
            while size > 0:
                v = self.__getLen4(self._orderAPP1)
                lstValue.append(v)
                size -= 4
            data = array('f', lstValue)
            pass
        elif format == 12:
            # double float
            while size > 0:
                numerator = self.__getLen4(self._orderAPP1)
                denominator = self.__getLen4(self._orderAPP1)
                size -= 8
                lstValue.append(float(numerator) / float(denominator))
            data = array('d', lstValue)
            pass
        entry.setData(data)
        log(" --- tag(%s), %s"%(hex(tag), str(data)))
        return entry

    def __parseBasicIFD(self, base, start, end):
        log("Enter", "[BasicIFD]", "add")

        if not self._file:
            assert False
        entries = self.__getLen2(self._orderAPP1)
        log("Number of entries = %d"%(entries))

        for idx in xrange(entries):
            tag = self.__getLen2(self._orderAPP1)
            dataFormat = self.__getLen2(self._orderAPP1)
            numOfComps = self.__getLen4(self._orderAPP1)
            posBeforeDataOffset = self._file.tell()
            dataOffset = self.__getLen4(self._orderAPP1)
            posAfterDataOffset = self._file.tell()

            if 0 == dataFormat or dataFormat >= len(EXIF_TIFF_DATAFORMAT_LIST):
                assert False, "dataformat incorrect = %d"%(dataFormat)
                continue
            bytesPerComp = EXIF_TIFF_DATAFORMAT_LIST[dataFormat]
            dataSize = bytesPerComp * numOfComps
            if dataSize > 4:
                targetOffset = base + dataOffset
                if targetOffset <= start or targetOffset >= end:
                    continue
                else:
                    self._file.seek(targetOffset)
            else:
                self._file.seek(posBeforeDataOffset)

            entry = self.__getDataFromFormat(tag, dataFormat, dataSize)
            if entry.getTag() == TAGID_ExifIFD:
                subExifOffset = entry.getValue()
                self._file.seek(base+subExifOffset)
                self.__parseExifSubIFD(base, start, end)
            elif entry.getTag() == TAGID_SubIFDs:
                log("SubIFDs")
                pass
            elif entry.getTag() == TAGID_GPSIFD:
                log("GPSIFD")
                pass
            elif entry.getTag() == TAGID_IPTC:
                log("IPTC")
                pass
            elif entry.getTag() == TAGID_XMP:
                log("XMP")
                pass
            elif entry.getTag() == TAGID_Photoshop:
                log("Photoshop")
                pass
            elif entry.getTag() == TAGID_ICCProfile:
                log("ICCProfile")
                pass
            elif entry.getTag() == TAGID_DNGPrivateData:
                log("DNGPrivateData")
                pass

            self._file.seek(posAfterDataOffset)

        log("Leave", "[BasicIFD]", "remove")

    def __parseExifSubIFD(self, base, start, end):
        log("Enter", "[SubIFDs]", "add")

        if not self._file:
            assert False
        entries = self.__getLen2(self._orderAPP1)
        log("Number of entries = %d"%(entries))

        for idx in xrange(entries):
            tag = self.__getLen2(self._orderAPP1)
            dataFormat = self.__getLen2(self._orderAPP1)
            numOfComps = self.__getLen4(self._orderAPP1)
            posBeforeDataOffset = self._file.tell()
            dataOffset = self.__getLen4(self._orderAPP1)
            posAfterDataOffset = self._file.tell()

            if 0 == dataFormat or dataFormat >= len(EXIF_TIFF_DATAFORMAT_LIST):
                assert False, "dataformat incorrect = %d"%(dataFormat)
                continue
            bytesPerComp = EXIF_TIFF_DATAFORMAT_LIST[dataFormat]
            dataSize = bytesPerComp * numOfComps
            if dataSize > 4:
                targetOffset = base + dataOffset
                if targetOffset <= start or targetOffset >= end:
                    continue
                else:
                    self._file.seek(targetOffset)
            else:
                self._file.seek(posBeforeDataOffset)
            entry = self.__getDataFromFormat(tag, dataFormat, dataSize)
            self._file.seek(posAfterDataOffset)

        log("Leave", "[SubIFDs]", "remove")

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

        offsetToNextIFD = self.__getLen4(self._orderAPP1)
        log("offsetToNextIFD = %s"%(hex(offsetToNextIFD)))
        while offsetToNextIFD:
            self._file.seek(base+offsetToNextIFD)
            self.__parseBasicIFD(base, start, end)
            offsetToNextIFD = self.__getLen4(self._orderAPP1)
            log("offsetToNextIFD = %s"%(hex(offsetToNextIFD)))

    def __parseXMP(self, data, dataLen):
        if not self._file:
            assert False

        s1 = data.find('<?')
        s2 = data.find('?>')
        s3 = data.find('<?', s2)
        s4 = data.find('?>', s3)
        dataCut = data[s2+2:s3]
        from XMPParser import XMPParser
        meta = XMPParser.parse(dataCut)
        log('XMP = %s'%(str(meta)))

    def __parseAPP2(self, length):
        curPos = self._file.tell()
        iptcData = self._file.read(length)
        iccIdentifier = "ICC_PROFILE"
        if (iptcData.startswith(iccIdentifier)):
            iccData = iptcData[len(iccIdentifier)+1:]
            iccLen = 0
            if ord(iccData[0]) == 0x01 and ord(iccData[1]) == 0x01:
                iccLen = length -14
            elif ord(iccData[0]) == 0x01: # multi-page, support header only
                iccLen = 128
            else:
                log("Wrong ICC Profile format !")
                return
            self._file.seek(curPos+14)
            self.__parseICCProfile(iccData[2:], iccLen)
        else:
            log("Wrong ICC Profile format !")
            assert False

    def __parseICCProfile(self, iccData, iccLen):
        # Refer to http://blog.fpmurphy.com/2012/03/extract-icc-profile-from-images.html
        basePos = self._file.tell()

        def parseHeader():
            profileSize = self.__getLen4()
            cmmType = ''.join(self.__getChar() for _ in xrange(4))
            lstVersion = [self.__getcToOrd() for _ in xrange(4)]
            print str(lstVersion)
            deviceClass = ''.join(self.__getChar() for _ in xrange(4))
            print "Profile Size = %d, %s, %s"%(profileSize, cmmType, deviceClass)
            colorSpaceOfData = ''.join(self.__getChar() for _ in xrange(4))
            pcs = ''.join(self.__getChar() for _ in xrange(4))
            print "CS Data, pcs = %s, %s"%(colorSpaceOfData, pcs)
            lstDatetime = [self.__getcToOrd() for _ in xrange(12)]
            print str(lstDatetime)
            signature = ''.join(self.__getChar() for _ in xrange(4))
            primaryPlatform = ''.join(self.__getChar() for _ in xrange(4))
            print "signature, primaryPlatform = %s, %s"%(signature, primaryPlatform)
            lstProfileFlags = [hex(self.__getcToOrd()) for _ in xrange(4)]
            print str(lstProfileFlags)
            deviceManufacturer = ''.join(self.__getChar() for _ in xrange(4))
            deviceModel = ''.join(self.__getChar() for _ in xrange(4))
            print "deviceManufacturer, deviceModel = %s, %s"%(deviceManufacturer, deviceModel)
            lstDeviceAttributes = [hex(self.__getcToOrd()) for _ in xrange(8)]
            print str(lstDeviceAttributes)
            renderingIntent, zeroPadding = self.__getLen2(), self.__getLen2()
            print "Rendering Intent = %d"%(renderingIntent)
            lstCIEXYZValue = [hex(self.__getcToOrd()) for _ in xrange(12)]
            print str(lstCIEXYZValue)
            profileCreator = ''.join(self.__getChar() for _ in xrange(4))
            print "Profile Creator = %s"%(profileCreator)
            profileID = [hex(self.__getcToOrd()) for _ in xrange(16)]
            print str(profileID)
            reserved = [hex(self.__getcToOrd()) for _ in xrange(28)]
            print str(reserved)

        def parseTagTable():
            pass
            #tagCount = self.__getLen4()
            #print "Tag count = %d"%(tagCount)

        parseHeader()
        parseTagTable()

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
            length = self.__getLen2()
            curPos = self._file.tell()
            log("length= %d, curPos=%d"%(length,curPos))

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
                    self.__parseAPP1(curPos+6, curPos, curPos+length-2)
                elif header.lower() == 'http':
                    self._file.seek(curPos)
                    xmpBuffer = self._file.read(length)
                    checkURL = "http://ns.adobe.com/xap/1.0/"
                    if xmpBuffer.startswith(checkURL):
                        headLen = len(checkURL)
                        self.__parseXMP(xmpBuffer[headLen:], length-headLen)
                    pass
                log("Leave", "[APP1]", "remove")

            elif marker == JPEG_APP2:
                log("Enter", "[APP2]", "add")
                self.__parseAPP2(length)
                log("Leave", "[APP2]", "remove")
                pass # TBD
            elif marker == JPEG_APP13:
                log("Enter", "[APP13]", "add")
                log("Leave", "[APP13]", "remove")
                pass # TBD
            self._file.seek(curPos+length-2)

import os
#fPath = "./images/Sample.JPG"
#fPath = "./images/brownie.jpg"
fPath = "./images/tampa_AdobeRGB.jpg"
#fPath = "./images/exif-iptc.jpg"
#fPath = "./images/Reagan.jpg"

fullPath = os.path.abspath(fPath)

jpgParser = JPEGMetadataParser()
jpgParser.parse(fullPath)
