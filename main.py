# -*- coding: utf-8 -*-

import kmzdownloader
import KMZtoKML
import preprocessor

# Import provinces from list.
provinceList = preprocessor.importProvinces('provinces.csv')

# Perform the function for each province.
for province in provinceList:
    print province
    filenamePath = kmzdownloader.kmzDownload(province)
    kmlFile = KMZtoKML.KMLgenerator(filenamePath)

    fields = ['ID', 'Número', 'Ano', 'Último Evento', 'Titular', 'Substância']

    preprocessor.preprocessKML(kmlFile)
    dataFrame = preprocessor.createData(fields, filenamePath, province, save=True)

    #TODO: Save data in pickle file.
