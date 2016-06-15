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
TAGID_EXIF_ExposureTime                    = 0x829A
TAGID_EXIF_FNumber                         = 0x829D
TAGID_EXIF_ExposureProgram                 = 0x8822
TAGID_EXIF_SpectralSensitivity             = 0x8824
TAGID_EXIF_ISOSpeedRatings                 = 0x8827
TAGID_EXIF_OECF                            = 0x8828
TAGID_EXIF_ExifVersion                     = 0x9000
TAGID_EXIF_DateTimeOriginal                = 0x9003
TAGID_EXIF_DateTimeDigitized               = 0x9004
TAGID_EXIF_ComponentsConfiguration         = 0x9101
TAGID_EXIF_CompressedBitsPerPixel          = 0x9102
TAGID_EXIF_ShutterSpeedValue               = 0x9201
TAGID_EXIF_ApertureValue                   = 0x9202
TAGID_EXIF_BrightnessValue                 = 0x9203
TAGID_EXIF_ExposureBiasValue               = 0x9204
TAGID_EXIF_MaxApertureValue                = 0x9205
TAGID_EXIF_SubjectDistance                 = 0x9206
TAGID_EXIF_MeteringMode                    = 0x9207
TAGID_EXIF_LightSource                     = 0x9208
TAGID_EXIF_Flash                           = 0x9209
TAGID_EXIF_FocalLength                     = 0x920A
TAGID_EXIF_SubjectArea                     = 0x9214
TAGID_EXIF_MakerNote                       = 0x927C
TAGID_EXIF_UserComment                     = 0x9286
TAGID_EXIF_SubsecTime                      = 0x9290
TAGID_EXIF_SubsecTimeOriginal              = 0x9291
TAGID_EXIF_SubsecTimeDigitized             = 0x9292
TAGID_EXIF_FlashpixVersion                 = 0xA000
TAGID_EXIF_ColorSpace                      = 0xA001
TAGID_EXIF_PixelXDimension                 = 0xA002
TAGID_EXIF_PixelYDimension                 = 0xA003
TAGID_EXIF_RelatedSoundFile                = 0xA004
TAGID_EXIF_FlashEnergy                     = 0xA20B
TAGID_EXIF_SpatialFrequencyResponse        = 0xA20C
TAGID_EXIF_FocalPlaneXResolution           = 0xA20E
TAGID_EXIF_FocalPlaneYResolution           = 0xA20F
TAGID_EXIF_FocalPlaneResolutionUnit        = 0xA210
TAGID_EXIF_SubjectLocation                 = 0xA214
TAGID_EXIF_ExposureIndex                   = 0xA215
TAGID_EXIF_SensingMethod                   = 0xA217
TAGID_EXIF_FileSource                      = 0xA300
TAGID_EXIF_SceneType                       = 0xA301
TAGID_EXIF_CFAPattern                      = 0xA302
TAGID_EXIF_CustomRendered                  = 0xA401
TAGID_EXIF_ExposureMode                    = 0xA402
TAGID_EXIF_WhiteBalance                    = 0xA403
TAGID_EXIF_DigitalZoomRatio                = 0xA404
TAGID_EXIF_FocalLengthIn35mmFilm           = 0xA405
TAGID_EXIF_SceneCaptureType                = 0xA406
TAGID_EXIF_GainControl                     = 0xA407
TAGID_EXIF_Contrast                        = 0xA408
TAGID_EXIF_Saturation                      = 0xA409
TAGID_EXIF_Sharpness                       = 0xA40A
TAGID_EXIF_DeviceSettingDescription        = 0xA40B
TAGID_EXIF_SubjectDistanceRange            = 0xA40C
TAGID_EXIF_ImageUniqueID                   = 0xA420
# ====
# GPS
"""
GPS tags are used to encode positioning information, related largely to image
generation by digital still cameras.
"""
TAGID_GPS_GPSVersionID                    = 0x0000
TAGID_GPS_GPSLatitudeRef                  = 0x0001
TAGID_GPS_GPSLatitude                     = 0x0002
TAGID_GPS_GPSLongitudeRef                 = 0x0003
TAGID_GPS_GPSLongitude                    = 0x0004
TAGID_GPS_GPSAltitudeRef                  = 0x0005
TAGID_GPS_GPSAltitude                     = 0x0006
TAGID_GPS_GPSTimeStamp                    = 0x0007
TAGID_GPS_GPSSatellites                   = 0x0008
TAGID_GPS_GPSStatus                       = 0x0009
TAGID_GPS_GPSMeasureMode                  = 0x000A
TAGID_GPS_GPSDOP                          = 0x000B
TAGID_GPS_GPSSpeedRef                     = 0x000C
TAGID_GPS_GPSSpeed                        = 0x000D
TAGID_GPS_GPSTrackRef                     = 0x000E
TAGID_GPS_GPSTrack                        = 0x000F
TAGID_GPS_GPSImgDirectionRef              = 0x0010
TAGID_GPS_GPSImgDirection                 = 0x0011
TAGID_GPS_GPSMapDatum                     = 0x0012
TAGID_GPS_GPSDestLatitudeRef              = 0x0013
TAGID_GPS_GPSDestLatitude                 = 0x0014
TAGID_GPS_GPSDestLongitudeRef             = 0x0015
TAGID_GPS_GPSDestLongitude                = 0x0016
TAGID_GPS_GPSDestBearingRef               = 0x0017
TAGID_GPS_GPSDestBearing                  = 0x0018
TAGID_GPS_GPSDestDistanceRef              = 0x0019
TAGID_GPS_GPSDestDistance                 = 0x001A
TAGID_GPS_GPSProcessingMethod             = 0x001B
TAGID_GPS_GPSAreaInformation              = 0x001C
TAGID_GPS_GPSDateStamp                    = 0x001D
TAGID_GPS_GPSDifferential                 = 0x001E
# ====
# Interoperability
"""
The single Interoperability tag is used to encode compability information,
related to image generation by digital still cameras.
"""
TAGID_INTEROPERABILITY_InteroperabilityIndex    = 0x0001
# ===========================================================
dicTagToVal = {'AliasLayerMetadata': 50784,
 'AnalogBalance': 50727,
 'AntiAliasStrength': 50738,
 'ApertureValue': 37378,
 'Artist': 315,
 'AsShotNeutral': 50728,
 'AsShotWhiteXY': 50729,
 'BadFaxLines': 326,
 'BaselineExposure': 50730,
 'BaselineNoise': 50731,
 'BaselineSharpness': 50732,
 'BayerGreenSplit': 50733,
 'BestQualityScale': 50780,
 'BitsPerSample': 258,
 'BlackLevel': 50714,
 'BlackLevelDeltaH': 50715,
 'BlackLevelDeltaV': 50716,
 'BlackLevelRepeatDim': 50713,
 'BrightnessValue': 37379,
 'CFALayout': 50711,
 'CFAPattern': 41730,
 'CFAPlaneColor': 50710,
 'CalibrationIlluminant1': 50778,
 'CalibrationIlluminant2': 50779,
 'CameraCalibration1': 50723,
 'CameraCalibration2': 50724,
 'CameraSerialNumber': 50735,
 'CellLength': 265,
 'CellWidth': 264,
 'ChromaBlurRadius': 50737,
 'CleanFaxData': 327,
 'ClipPath': 343,
 'CodingMethods': 403,
 'ColorMap': 320,
 'ColorMatrix1': 50721,
 'ColorMatrix2': 50722,
 'ColorSpace': 40961,
 'ComponentsConfiguration': 37121,
 'CompressedBitsPerPixel': 37122,
 'Compression': 259,
 'ConsecutiveBadFaxLines': 328,
 'Contrast': 41992,
 'Copyright': 33432,
 'CustomRendered': 41985,
 'DNGBackwardVersion': 50707,
 'DNGPrivateData': 50740,
 'DNGVersion': 50706,
 'DateTime': 306,
 'DateTimeDigitized': 36868,
 'DateTimeOriginal': 36867,
 'Decode': 433,
 'DefaultCropOrigin': 50719,
 'DefaultCropSize': 50720,
 'DefaultImageColor': 434,
 'DefaultScale': 50718,
 'DeviceSettingDescription': 41995,
 'DigitalZoomRatio': 41988,
 'DocumentName': 269,
 'DotRange': 336,
 'ExifIFD': 34665,
 'ExifVersion': 36864,
 'ExposureBiasValue': 37380,
 'ExposureIndex': 41493,
 'ExposureMode': 41986,
 'ExposureProgram': 34850,
 'ExposureTime': 33434,
 'ExtraSamples': 338,
 'FNumber': 33437,
 'FaxProfile': 402,
 'FileSource': 41728,
 'FillOrder': 266,
 'Flash': 37385,
 'FlashEnergy': 41483,
 'FlashpixVersion': 40960,
 'FocalLength': 37386,
 'FocalLengthIn35mmFilm': 41989,
 'FocalPlaneResolutionUnit': 41488,
 'FocalPlaneXResolution': 41486,
 'FocalPlaneYResolution': 41487,
 'FreeByteCounts': 289,
 'FreeOffsets': 288,
 'GPSAltitude': 6,
 'GPSAltitudeRef': 5,
 'GPSAreaInformation': 28,
 'GPSDOP': 11,
 'GPSDateStamp': 29,
 'GPSDestBearing': 24,
 'GPSDestBearingRef': 23,
 'GPSDestDistance': 26,
 'GPSDestDistanceRef': 25,
 'GPSDestLatitude': 20,
 'GPSDestLatitudeRef': 19,
 'GPSDestLongitude': 22,
 'GPSDestLongitudeRef': 21,
 'GPSDifferential': 30,
 'GPSIFD': 34853,
 'GPSImgDirection': 17,
 'GPSImgDirectionRef': 16,
 'GPSLatitude': 2,
 'GPSLatitudeRef': 1,
 'GPSLongitude': 4,
 'GPSLongitudeRef': 3,
 'GPSMapDatum': 18,
 'GPSMeasureMode': 10,
 'GPSProcessingMethod': 27,
 'GPSSatellites': 8,
 'GPSSpeed': 13,
 'GPSSpeedRef': 12,
 'GPSStatus': 9,
 'GPSTimeStamp': 7,
 'GPSTrack': 15,
 'GPSTrackRef': 14,
 'GPSVersionID': 0,
 'GainControl': 41991,
 'GeoAsciiParamsTag': 34737,
 'GeoDoubleParamsTag': 34736,
 'GeoKeyDirectoryTag': 34735,
 'GlobalParametersIFD': 400,
 'GrayResponseCurve': 291,
 'GrayResponseUnit': 290,
 'HalftoneHints': 321,
 'HostComputer': 316,
 'HylaFAXFaxRecvParams': 34908,
 'HylaFAXFaxRecvTime': 34910,
 'HylaFAXFaxSubAddress': 34909,
 'ICCProfile': 34675,
 'INGRFlagRegisters': 33919,
 'INGRPacketDataTag': 33918,
 'IPTC': 33723,
 'ISOSpeedRatings': 34855,
 'ImageDescription': 270,
 'ImageID': 32781,
 'ImageLayer': 34732,
 'ImageLength': 257,
 'ImageSourceData': 37724,
 'ImageUniqueID': 42016,
 'ImageWidth': 256,
 'Indexed': 346,
 'InkNames': 333,
 'InkSet': 332,
 'InteroperabilityIFD': 40965,
 'InteroperabilityIndex': 1,
 'IrasBTransformationMatrix': 33920,
 'JPEGACTables': 521,
 'JPEGDCTables': 520,
 'JPEGInterchangeFormat': 513,
 'JPEGInterchangeFormatLength': 514,
 'JPEGLosslessPredictors': 517,
 'JPEGPointTransforms': 518,
 'JPEGProc': 512,
 'JPEGQTables': 519,
 'JPEGRestartInterval': 515,
 'JPEGTables': 347,
 'LensInfo': 50736,
 'LightSource': 37384,
 'LinearResponseLimit': 50734,
 'LinearizationTable': 50712,
 'LocalizedCameraModel': 50709,
 'MDColorTable': 33447,
 'MDFileTag': 33445,
 'MDFileUnits': 33452,
 'MDLabName': 33448,
 'MDPrepDate': 33450,
 'MDPrepTime': 33451,
 'MDSampleInfo': 33449,
 'MDScalePixel': 33446,
 'METADATA': 42112,
 'Make': 271,
 'MakerNote': 37500,
 'MakerNoteSafety': 50741,
 'MaxApertureValue': 37381,
 'MaxSampleValue': 281,
 'MeteringMode': 37383,
 'MinSampleValue': 280,
 'ModeNumber': 405,
 'Model': 272,
 'ModelPixelScaleTag': 33550,
 'ModelTiepointTag': 33922,
 'ModelTransformationTag': 34264,
 'NODATA': 42113,
 'NewSubfileType': 254,
 'NumberOfInks': 334,
 'OECF': 34856,
 'OPIProxy': 351,
 'OceApplicationSelector': 50216,
 'OceIdentificationNumber': 50217,
 'OceImageLogicCharacteristics': 50218,
 'OceScanjobDescription': 50215,
 'Orientation': 274,
 'PageName': 285,
 'PageNumber': 297,
 'PhotometricInterpretation': 262,
 'Photoshop': 34377,
 'PixelXDimension': 40962,
 'PixelYDimension': 40963,
 'PlanarConfiguration': 284,
 'Predictor': 317,
 'PrimaryChromaticities': 319,
 'ProfileType': 401,
 'ReductionMatrix1': 50725,
 'ReductionMatrix2': 50726,
 'ReferenceBlackWhite': 532,
 'RelatedSoundFile': 40964,
 'ResolutionUnit': 296,
 'RowsPerStrip': 278,
 'SMaxSampleValue': 341,
 'SMinSampleValue': 340,
 'SampleFormat': 339,
 'SamplesPerPixel': 277,
 'Saturation': 41993,
 'SceneCaptureType': 41990,
 'SceneType': 41729,
 'SensingMethod': 41495,
 'Sharpness': 41994,
 'ShutterSpeedValue': 37377,
 'Software': 305,
 'SpatialFrequencyResponse': 41484,
 'SpectralSensitivity': 34852,
 'StripByteCounts': 279,
 'StripOffsets': 273,
 'StripRowCounts': 559,
 'SubIFDs': 330,
 'SubfileType': 255,
 'SubjectArea': 37396,
 'SubjectDistance': 37382,
 'SubjectDistanceRange': 41996,
 'SubjectLocation': 41492,
 'SubsecTime': 37520,
 'SubsecTimeDigitized': 37522,
 'SubsecTimeOriginal': 37521,
 'T4Options': 292,
 'T6Options': 293,
 'TargetPrinter': 337,
 'Threshholding': 263,
 'TileByteCounts': 325,
 'TileLength': 323,
 'TileOffsets': 324,
 'TileWidth': 322,
 'TransferFunction': 301,
 'TransferRange': 342,
 'UniqueCameraModel': 50708,
 'UserComment': 37510,
 'VersionYear': 404,
 'WangAnnotation': 32932,
 'WhiteBalance': 41987,
 'WhiteLevel': 50717,
 'WhitePoint': 318,
 'XClipPathUnits': 344,
 'XMP': 700,
 'XPosition': 286,
 'XResolution': 282,
 'YCbCrCoefficients': 529,
 'YCbCrPositioning': 531,
 'YCbCrSubSampling': 530,
 'YClipPathUnits': 345,
 'YPosition': 287,
 'YResolution': 283}
# ===========================================================
def getTagStringByValue(value):
    # TODO : Use a pre-calculated map to reduce time & fix the multiple value issue
    strTag = ""
    for k, v in dicTagToVal.iteritems():
        if v == value:
            return k
    assert strTag != ""

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

from misc import log
from FileOPs import nowAt, seekTo, getChar, getCharToOrd, getBytes2, getBytes4,\
                    getBytes8, BYTE_ALIGN_INTEL, BYTE_ALIGN_MOTOROLA

EXIF_TIFF_DATAFORMAT_LIST = [1,1,1,2,4,8,1,1,2,4,8,4,8]
class JPEGMetadataParser:
    def __init__(self):
        self._file = None
        self._orderAPP1 = None
        pass

    def __getDataFromFormat(self, tag, format, size):
        from array import array
        bytesPerComp = EXIF_TIFF_DATAFORMAT_LIST[format]
        entry = IFDEntry(tag, bytesPerComp)
        #print 'format(%d)/Size(%d)'%(format, size)
        lstValue = []
        if format in [1, 6, 7]:
            # unsigned byte / # signed byte / # undefined
            data = array('b', getChar(self._file, size))
            pass
        elif format == 2:
            # ascii string
            data = array('c', getChar(self._file, size))
            pass
        elif format in [3, 8]:
            # unsigned short / # signed short
            while size > 0:
                v = getBytes2(self._file, self._orderAPP1)
                lstValue.append(v)
                size -= 2
            encode = 'H' if format == 3 else 'h'
            data = array('H', lstValue)
            pass
        elif format in [4, 9]:
            # unsigned long / # signed long
            while size > 0:
                v = getBytes4(self._file, self._orderAPP1)
                lstValue.append(v)
                size -= 4
            encode = 'L' if format == 4 else 'l'
            data = array('L', lstValue)
            pass
        elif format in [5, 10]:
            # unsigned rational / # signed rational
            while size > 0:
                numerator = getBytes4(self._file, self._orderAPP1)
                denominator = getBytes4(self._file, self._orderAPP1)
                size -= 8
                lstValue.append(float(numerator) / float(denominator))
            data = array('d', lstValue)
            pass
        elif format == 11:
            # signed float
            while size > 0:
                v = getBytes4(self._file, self._orderAPP1)
                lstValue.append(v)
                size -= 4
            data = array('f', lstValue)
            pass
        elif format == 12:
            # double float
            while size > 0:
                numerator = getBytes4(self._file, self._orderAPP1)
                denominator = getBytes4(self._file, self._orderAPP1)
                size -= 8
                lstValue.append(float(numerator) / float(denominator))
            data = array('d', lstValue)
            pass
        entry.setData(data)

        log(" --- tag(%s), %s"%(getTagStringByValue(tag), str(data)))
        return entry

    def __parseBasicIFD(self, base, start, end):
        log("Enter", "[BasicIFD]", "add")

        if not self._file:
            assert False
        entries = getBytes2(self._file, self._orderAPP1)
        log("Number of entries = %d"%(entries))

        for idx in xrange(entries):
            tag = getBytes2(self._file, self._orderAPP1)
            dataFormat = getBytes2(self._file, self._orderAPP1)
            numOfComps = getBytes4(self._file, self._orderAPP1)
            posBeforeDataOffset = nowAt(self._file)
            dataOffset = getBytes4(self._file, self._orderAPP1)
            posAfterDataOffset = nowAt(self._file)

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
                    seekTo(self._file, targetOffset)
            else:
                seekTo(self._file, posBeforeDataOffset)

            entry = self.__getDataFromFormat(tag, dataFormat, dataSize)
            if entry.getTag() == TAGID_ExifIFD:
                ifdOffset = entry.getValue()
                seekTo(self._file, base+ifdOffset)
                self.__parseIFDs(base, start, end, "ExifIFD")
            elif entry.getTag() == TAGID_SubIFDs:
                log("SubIFDs")
            elif entry.getTag() == TAGID_GPSIFD:
                ifdOffset = entry.getValue()
                seekTo(self._file, base+ifdOffset)
                self.__parseIFDs(base, start, end, IFD="GPSIFD")
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


            seekTo(self._file, posAfterDataOffset)

        log("Leave", "[BasicIFD]", "remove")

    def __parseIFDs(self, base, start, end, IFD=""):
        assert IFD != ""
        log("Enter", "[%s]"%(IFD), "add")

        if not self._file:
            assert False
        entries = getBytes2(self._file, self._orderAPP1)
        log("Number of entries = %d"%(entries))

        for idx in xrange(entries):
            tag = getBytes2(self._file, self._orderAPP1)
            dataFormat = getBytes2(self._file, self._orderAPP1)
            numOfComps = getBytes4(self._file, self._orderAPP1)
            posBeforeDataOffset = nowAt(self._file)
            dataOffset = getBytes4(self._file, self._orderAPP1)
            posAfterDataOffset = nowAt(self._file)

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
                    seekTo(self._file, targetOffset)
            else:
                seekTo(self._file, posBeforeDataOffset)
            entry = self.__getDataFromFormat(tag, dataFormat, dataSize)
            seekTo(self._file, posAfterDataOffset)

        log("Leave", "[%s]"%(IFD), "remove")

    def __parseAPP1(self, base, start, end):
        if not self._file:
            assert False

        seekTo(self._file, base)
        self._orderAPP1 = getBytes2(self._file)
        log("order = %s"%(hex(self._orderAPP1)))

        if self._orderAPP1 not in [BYTE_ALIGN_MOTOROLA, BYTE_ALIGN_INTEL]:
            log("order incorrect")
            assert False

        check = getBytes2(self._file, self._orderAPP1)
        if check != 0x002a:
            assert False

        offsetToNextIFD = getBytes4(self._file, self._orderAPP1)
        log("offsetToNextIFD = %s"%(hex(offsetToNextIFD)))
        while offsetToNextIFD:
            seekTo(self._file, base+offsetToNextIFD)
            self.__parseBasicIFD(base, start, end)
            offsetToNextIFD = getBytes4(self._file, self._orderAPP1)
            log("offsetToNextIFD = %s"%(hex(offsetToNextIFD)))

    def __parseXMP(self, data, dataLen):
        if not self._file:
            assert False

        from XMPParser import XMPParser
        meta = XMPParser.parse(data)
        log('XMP = %s'%(str(meta)))

    def __parseAPP2(self, length):
        curPos = nowAt(self._file)
        iptcData = getChar(self._file, length)
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
            seekTo(self._file, curPos+14)
            from ICCProfileParser import ICCProfileParser
            iccParser = ICCProfileParser(self._file, iccData[2:], iccLen)
        else:
            log("Wrong ICC Profile format !")
            assert False

    def parse(self, filePath):
        self._file = open(filePath)
        seekTo(self._file, 0)
        first = getCharToOrd(self._file)
        marker = getCharToOrd(self._file)
        if (first != 0xff or marker != JPEG_SOI):
            assert False, "Not in JPEG format !!"

        while (marker):
            first = getCharToOrd(self._file)
            if first != 0xff or first < 0:
                break
            marker = getCharToOrd(self._file)
            log("%s-%s"%(hex(first), hex(marker)))
            length = getBytes2(self._file)
            curPos = nowAt(self._file)
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
                header = getChar(self._file, 4)
                log("header = %s"%(header))
                if header.lower() == 'exif':
                    self.__parseAPP1(curPos+6, curPos, curPos+length-2)
                elif header.lower() == 'http':
                    seekTo(self._file, curPos)
                    xmpBuffer = getChar(self._file, length)
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
            seekTo(self._file, curPos+length-2)

import argparse
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='Input jpeg file to be parsed')
    args = parser.parse_args()
    if (args.input != None):
        jpgParser = JPEGMetadataParser()
        jpgParser.parse(args.input)
    else:
        print "Nothing to be parsed, make sure there's an input file !! "
