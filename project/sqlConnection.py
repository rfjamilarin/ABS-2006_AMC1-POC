from sqlalchemy import create_engine, text
import logging

# Set up module-level logger
logger = logging.getLogger(__name__)

def sqlConnection(dbName='loan_database', host='127.0.0.1', port=3306, user='root', password='1234'):
    # Create MySQL connection
    engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}:{port}')

    # Connect to MySQL server
    with engine.connect() as conn:
        # Check if the database exists
        result = conn.execute(text("SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = :dbName"), {"dbName": dbName})
        if result.fetchone() is None:
            # Create the database if it doesn't exist
            conn.execute(text(f"CREATE DATABASE {dbName}"))
            print(f"Database '{dbName}' created successfully.")

    # Reconnect to the specified database
    engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{dbName}')
    logger.info(f"Connected to MySQL database '{dbName}' successfully.")
    return engine
