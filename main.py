# -*- coding: utf-8 -*-

import kmzdownloader
import KMZtoKML
import preprocessor
import pandas as pd

# Download our file and return our filename path.
filenamePath = kmzdownloader.kmzDownload()

# Convert the KMZ to a KML file and return it.
kmlFile = KMZtoKML.KMLgenerator(filenamePath)

# Define our desired fields to scrape.
fields = ['ID', 'Número', 'Ano', 'Último Evento', 'Titular', 'Substância']

# Create our temporary HTML file stripped of description tags.
preprocessor.preprocessKML(kmlFile)

# Generate our data and save.
dataFrame = preprocessor.createCSV(fields, filenamePath, save=True)

#TODO: Add multiple provinces (i.e. via for loop), GUI.