import pandas as pd
import logging
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

logger = logging.getLogger(__name__)

def createTableSQL(cleanCSV, tableName='loan_level_data', engine=None):
    if engine is None:
        print("No database engine provided.")
        return

    headers = cleanCSV[0]
    data = cleanCSV[1:]

    df = pd.DataFrame(data, columns=headers) #create dataframe

    df.to_sql(tableName, engine, if_exists='replace', index=False) #insert dataframe into SQL database

    logger.info(f"Table '{tableName}' created successfully in the database.")
