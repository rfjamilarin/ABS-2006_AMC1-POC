import os
from datetime import datetime

def isFoundByDate(sourceFolder, inputDate):
    flag = False  #flag to indicate if file found
    csvName = None  #variable to store CSV filename
    digits = None  #variable to store YYMM as string for later use

    for filename in os.listdir(sourceFolder):
        if filename.endswith(".csv"):
            fileDate_str = filename[-8:-4]  #extract yymm from CSV filename
            digits = datetime.strptime(fileDate_str, '%y%m')

            if inputDate == digits:
                flag = True
                csvName = os.path.join(sourceFolder, filename)  #get CSV file
                break

    if not flag:
        print("No files found within the specified date range.")

    return flag, csvName, digits.strftime('%y%m')
