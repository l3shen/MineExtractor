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

# # Begin parsing our data.
# # Step 1 involves the parsing of all <description> fields followed by saving it to a temporary HTML file.
# soup = BeautifulSoup(kmlFile, 'html.parser')
# descEntries = soup.find_all('description')
# tempFile = open('temp.html','w')
# for i in descEntries:
#     temp = str(i).splitlines()
#     temp2 = temp[1:-1]
#     temp3 = ''.join(temp2)
#     tempFile.write(temp3)
# tempFile.close()
#
# # Now load our newly formatted HTML in.
# htmlData = open('temp.html','r')
# soup2 = BeautifulSoup(htmlData, 'html.parser') # WORKS!!!!
# bodyEntries = soup2.find_all('body')
#
# indexValues = [4, 6, 8, 14, 16, 18]
# # rowIndexer = 0
# # columnIndexer = 0
# parsedData = []
# for entries in bodyEntries:
#     tempList = []
#     tds = entries.find_all('td')
#     for i in indexValues:
#         for entry in tds[i]:
#             tempList.append(entry)
#     # print tempList
#     parsedData.append(tempList)
#
# # Convert data to pandas dataframe.
# # Create our empty pandas data structure to be filled in later.
# dataFrame = pd.DataFrame(parsedData, columns=fields)
#
# # Save to CSV file.
# dataFrame.to_csv('testData.csv', sep=',', encoding='utf-8-sig')
#
# # Delete the HTML file after completing everything.
# os.remove('temp.html')