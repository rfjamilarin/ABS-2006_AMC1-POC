import csv
from datetime import datetime
import logging

# Set up module-level logger
logger = logging.getLogger(__name__)

def cleanCSV(csvName, dtColName='paid_to_date', startDate=None, endDate=None):
    if startDate is None:
        startDate = datetime(2006, 1, 1)  # Default start date: January 1, 2006

    if endDate is None:
        endDate = datetime.now()  # Default end date: current date and time

    cleanCSV = []
    outlierDateCnt = 0
    blankDateCnt = 0

    with open(csvName, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        header_row = next(csv_reader)
        cleaned_header_row = [header.lower().replace(' ', '_').replace('#', 'id') for header in header_row]
        cleanCSV.append(cleaned_header_row)
    
        # Identify the index of the date column
        dtColIndex = cleaned_header_row.index(dtColName.strip())  # Strip whitespace from column name

        for row in csv_reader:
            # Check if the value in the date column is empty
            if not row[dtColIndex]:
                cleanCSV.append(row)
                blankDateCnt += 1
            elif isDateOutlier(row[dtColIndex], startDate, endDate):
                outlierDateCnt += 1
            else:
                cleanCSV.append(row)

    logger.info(f"{blankDateCnt} rows have blank dates.")
    logger.info(f"{outlierDateCnt} rows detected with date outliers.")
    return cleanCSV

def isDateOutlier(strDate, startDate, endDate):
    date_obj = datetime.strptime(strDate, '%Y%m%d')
    return not (startDate <= date_obj <= endDate)
