# JPEGMetadataParser
 - Main tiff/exif information is parsed by JPEGMetadataParser
 - XMP data is parsed by XMPParser
 - ICCProfile is parsed by ICCProfileParser

$> python JPEGMetadataParser.py -i FILE_PATH

# ICCProfileParser
$> python ICCProfileParser.py -i ICC_FILE_PATH
 - You can find one under profiles/ to give a test

NOTE : Currently the metadata information is printed out in console.
