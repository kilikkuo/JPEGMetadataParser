"""
 Origin by Matt Swain. Released under the MIT license.
 See file LICENSE for detail or copy at https://opensource.org/licenses/MIT
"""

NS_CROSSMARK    = 'http://crossref.org/crossmark/1.0/'
NS_DC           = 'http://purl.org/dc/elements/1.1/'
NS_EXIF         = 'http://ns.adobe.com/exif/1.0/'
NS_PDF          = 'http://ns.adobe.com/pdf/1.3/'
NS_PDFX         = 'http://ns.adobe.com/pdfx/1.3/'
NS_PHOTOSHOP    = 'http://ns.adobe.com/photoshop/1.0/'
NS_PRISM        = 'http://prismstandard.org/namespaces/basic/2.0/'
NS_RDF          = 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'
NS_TIFF         = 'http://ns.adobe.com/tiff/1.0/'
NS_XAP          = 'http://ns.adobe.com/xap/1.0/'
NS_XAP_MM       = 'http://ns.adobe.com/xap/1.0/mm/'
NS_XAP_RIGHTS   = 'http://ns.adobe.com/xap/1.0/rights/'
NS_XML          = 'http://www.w3.org/XML/1998/namespace'

dicNSLinktoNSTag = {NS_CROSSMARK    : 'crossmark',
                    NS_DC           : 'dc',
                    NS_EXIF         : 'exif',
                    NS_PDF          : 'pdf',
                    NS_PDFX         : 'pdfx',
                    NS_PHOTOSHOP    : 'photoshop',
                    NS_PRISM        : 'prism',
                    NS_RDF          : 'rdf',
                    NS_TIFF         : 'tiff',
                    NS_XAP          : 'xap',
                    NS_XAP_MM       : 'xapmm',
                    NS_XAP_RIGHTS   : 'rights',
                    NS_XML          : 'xml'}

import re
try:
    import xml.etree.cElementTree as ET
except:
    import xml.etree.ElementTree as ET

class XMPParser(object):
    def __init__(self):
        assert False
        pass

    @staticmethod
    def parse(inputData):

        s1 = inputData.find('<x:xmpmeta')
        s2 = inputData.find('/x:xmpmeta>')
        s3 = inputData.find('<x:xapmeta')
        s4 = inputData.find('/x:xapmeta>')
        #print "XMP index <x:xmpmeta=%d, /x:xmpmeta>=%d ==> <x:xapmeta=%d, /x:xapmeta>=%d"%(s1, s2, s3, s4)
        assert not (s1 == s2 and s3 == s4), "New kind of XMP meta in this file !!"
        data = None
        if s1 != s2 and s3 == s4:
            data = inputData[s1:s2+11]
        elif s3 != s4 and s1 == s2:
            data = inputData[s3:s4+11]
        else:
            assert False, "Containing multiple meta tags, correct the code !"

        meta = {}
        xmlTree = ET.XML(data)
        rdfTree = xmlTree.find('{' + NS_RDF + '}' + 'RDF')
        targetDesc = '{' + NS_RDF + '}Description'
        for description in rdfTree.findall(targetDesc):
            for e in iter(description):
                namespace = tag = None
                lstLinkTag = re.split("[{}]", e.tag)
                if lstLinkTag[1].startswith('http'):
                    namespace = dicNSLinktoNSTag.get(lstLinkTag[1], namespace)
                    tag = lstLinkTag[2]
                else:
                    continue
                if not namespace and not tag:
                    continue

                v = e.text
                if e.find('{' + NS_RDF + '}Alt') != None:
                    v = {}
                    targetPath = '{' + NS_RDF + '}Alt/' + '{' + NS_RDF + '}li'
                    for li in e.findall(targetPath):
                        v[li.get('{' + NS_XML + '}lang')] = li.text
                elif e.find('{' + NS_RDF + '}Bag') != None:
                    v = []
                    targetPath = '{' + NS_RDF + '}Bag/' + '{' + NS_RDF + '}li'
                    for li in e.findall(targetPath):
                        v.append(li.text)
                elif e.find('{' + NS_RDF + '}Seq') != None:
                    v = []
                    targetPath = '{' + NS_RDF + '}Seq/' + '{' + NS_RDF + '}li'
                    for li in e.findall(targetPath):
                        v.append(li.text)
                meta.setdefault(namespace, {})[tag] = v
        return meta
