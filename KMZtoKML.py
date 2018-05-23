'''
Kamil Krawczyk - 2017
version 0.0.1
Method used to convert KMZ to KML and return the inside doc.kml file.
Principle packages used zipfile.
'''

from zipfile import ZipFile

def KMLgenerator (filenamePath):

    kmz = ZipFile(filenamePath, 'r')
    kml = kmz.open('doc.kml', 'r').read()

    return kml