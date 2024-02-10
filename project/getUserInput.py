from datetime import datetime
import logging

logger = logging.getLogger(__name__)

def verifyUserInput(prompt):
    while True:
        try:
            inputYear = input(prompt)  # user input year
            yearObj = datetime.strptime(inputYear, "%Y")  # parse input year
            if yearObj.strftime("%Y") != inputYear:  # validate input year
                raise ValueError

            inputMonth = input("Enter the month (MMM): ")  # user input month
            monthObj = datetime.strptime(inputMonth, "%b")  # parse input month
            if monthObj.strftime("%b") != inputMonth:  # validate input month
                raise ValueError

            yymm = yearObj.strftime("%y") + monthObj.strftime("%m")  # get YYMM format for later use
            inputDate = datetime.strptime(yymm, '%y%m')

            # Check if the input date is July 2007 or later
            if inputDate < datetime(2007, 7, 1):
                raise ValueError("Date should be July 2007 or later.")

            return inputDate

        except ValueError as e:
            print(f"Invalid format or date! {e} Please enter the date in YYYY-MMM format (e.g., 2007-Jul).")


def getUserInput():
    inputDate = verifyUserInput("Enter the year (YYYY): ")
    logger.info(f'User action: {inputDate}')
    return inputDate
