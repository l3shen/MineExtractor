from bs4 import BeautifulSoup
import pandas as pd
import datetime
import os

def preprocessKML(kmlObject):
    soup = BeautifulSoup(kmlObject, 'html.parser')
    descEntries = soup.find_all('description')
    tempFile = open('temp.html', 'w')
    for i in descEntries:
        temp = str(i).splitlines()
        temp2 = temp[1:-1]
        temp3 = ''.join(temp2)
        tempFile.write(temp3)
    tempFile.close()

def createCSV(columnFields, filenamePath, save=True):

    # Set directory for downloaded data.
    cwd = os.getcwd()
    currentDate = datetime.datetime.now()

    # Pull current date.
    day = str(currentDate.day)
    month = str(currentDate.month)
    year = str(currentDate.year)

    if len(day) < 2:
        day = '0' + day

    if len(month) < 2:
        month = '0' + month

    datetimeString = year + '-' + month + '-' + day

    # Set directory and create if it doesn't exist.
    dataDirectoryRoot = os.path.join(cwd,datetimeString)

    # Create our filename.
    removedExtension = filenamePath[:-4]
    print removedExtension
    dataName = datetimeString + '-' + removedExtension[-2:] + '.csv'
    dataFilePath = os.path.join(dataDirectoryRoot, dataName)

    if os.path.isdir(dataDirectoryRoot) == False:
        os.mkdir(dataDirectoryRoot)
    else:
        # Change directory.
        os.chdir(dataDirectoryRoot)

    # Now load our newly formatted HTML in.
    htmlData = open('temp.html', 'r')

    htmlSoup = BeautifulSoup(htmlData, 'html.parser')  # WORKS!!!!
    bodyEntries = htmlSoup.find_all('body')

    indexValues = [4, 6, 8, 14, 16, 18]
    parsedData = []
    for entries in bodyEntries:
        tempList = []
        tds = entries.find_all('td')
        for i in indexValues:
            for entry in tds[i]:
                tempList.append(entry)
        parsedData.append(tempList)

    # Convert data to pandas dataframe.
    # Create our empty pandas data structure to be filled in later.
    dataFrame = pd.DataFrame(parsedData, columns=columnFields)

    if save == True:
        # Save to CSV file if it doesn't exist.
        if os.path.isfile(dataFilePath) != True:
            dataFrame.to_csv(dataFilePath, sep=',', encoding='utf-8-sig')
        elif os.path.isfile(dataFilePath) == True:
            print 'Data already saved.'
    elif save != True:
        # Display message.
        print 'Data not saved.'

    # Close our file.
    htmlData.close()

    # Delete the HTML file after completing everything as it is temporary.
    os.remove('temp.html')

    # Return dataframe.
    return dataFrame