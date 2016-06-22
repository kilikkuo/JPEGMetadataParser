# JPEGMetadataParser
 - Main tiff/exif information is parsed by JPEGMetadataParser
 - XMP data is parsed by XMPParser
 - ICCProfile is parsed by ICCProfileParser

$> python JPEGMetadataParser.py -i FILE_PATH

# ICCProfileParser
$> python ICCProfileParser.py -i ICC_FILE_PATH
 - You can find one under profiles/ to give a test

# Reference Spec
 - doc/icc32.pdf (v3.2, 1995-11)
 - doc/ICC1v43_2010-12.pdf (v4.3)

NOTE : Currently the metadata information is printed out in console.
