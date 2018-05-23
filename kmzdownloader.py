'''
Kamil Krawczyk - 2017
version 0.1.3
KMZ Downloader module - used to download KMZ files from DNPM and stores to subdirectory called 'data'.
Principle packages used are wget.
'''

import wget
import os
import datetime

def kmzDownload():
    '''
    Code that will download KMZ file from specified website if not present already.
    :return filenamePath - the filename path used for the download:
    '''


    # Find the current working directory and add subfolder for data, if non-existent.
    cwd = os.getcwd()
    dataDirectory = os.path.join(cwd,'kmzData')

    # Create subfolder.
    if os.path.isdir(dataDirectory) != True:
        os.mkdir(dataDirectory)
    elif os.path.isdir(dataDirectory):
        print 'Folder already present.'
    else:
        print 'Unknown error.'

    # Define our download URL.
    url = 'http://sigmine.dnpm.gov.br/sirgas2000/PR.kmz'

    # Define our filename and full path.
    currentDate = datetime.datetime.now()
    filename = generateFilename(currentDate, 'PR.kmz')
    filenamePath = os.path.join(dataDirectory, filename)

    # Check to see if file present, and download if not.
    if os.path.isfile(filenamePath) != True:
        # Download.
        try:
            wget.download(url,filenamePath)
        except Exception,e:
            print 'Error presented: %s' % (e)
        else:
            print 'File downloaded successfully!'
    elif os.path.isfile(filenamePath):
        # Alert user that file is already present.
        print 'File already downloaded.'
    else:
        print 'Unknown error'

    return filenamePath

def generateFilename(dateTime, fileName):
    '''
    Returns the full file path based on today's date.
    :param dateTime - the datetime object created by datetime package:
    :param fileName - the desired filename:
    :return result - the full filepath:
    '''

    # Pull current date.
    day = str(dateTime.day)
    month = str(dateTime.month)
    year = str(dateTime.year)

    if len(day) < 2:
        day = '0' + day

    if len(month) < 2:
        month = '0' + month

    result = year + '-' + month + '-' + day + '-' + fileName
    return result