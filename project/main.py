import threading
from datetime import datetime
import os
import csv
from sqlalchemy import create_engine, Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, Text
from sqlalchemy import func
from cleanCSV import cleanCSV
from aggrCleanLoanData import aggrCleanLoanData
from sqlConnection import sqlConnection
from isFoundByDate import isFoundByDate
import sqlite3
from createTableSQL import createTableSQL
from printTable import printTable
import sys
import logging
from setupLogging import setupLogging
from getUserInput import getUserInput
from openPDF import openPDF
import warnings
from introMsg import introMsg

warnings.filterwarnings("ignore", category=DeprecationWarning)

def main():    
    setupLogging()
    
    logging.info('Program started')

    introMsg()

    #get directory where main.py is
    script_dir = os.path.dirname(os.path.realpath(__file__))
    #construct path to CSV folder
    sourceFolder = os.path.join(script_dir, "enhancedLoanLevelData")

    while True:
        inputDate = getUserInput()
        flag, csvName, digits = isFoundByDate(sourceFolder, inputDate)

        if flag:
            engine = sqlConnection() #establish connection
            cleanedCSV = cleanCSV(csvName) #clean found CSV
            createTableSQL(cleanedCSV, engine=engine) #create SQL table in databse

            logging.info("Clean data successfully added into SQL database.")

            Session = sessionmaker(bind=engine) #create session for querying into SQL database
            session = Session()

            logging.info("Successfully created session with SQL database.")

            data = aggrCleanLoanData(session,engine=engine) #query table in database to get aggregated total fund values
            printTable(data) #print resulting aggregated values

            # Open associated PDF for comparison
            pdf = openPDF(digits)
            if pdf:
                logging.info(f"Found PDF file: {pdf}")
            else:
                print("No matching PDF file found.")

            # Close SQL connection
            engine.dispose()

            logging.info("Data processing completed successfully.")

        # Ask user if they want to end the program
        choice = input("Do you want to end the program? (yes/no): ").lower()
        logging.info(f'User choice: {choice}')
        
        if choice == "yes":
            logging.info('Program ended by user')
            break

if __name__ == "__main__":
    main()
