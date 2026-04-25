# This module basically contains functions that load data.
# While DataIngestion is the file , which gives order to the functions to load data.

import os
import sys
from src.mlproject.exception import CustomException # hmesha use krna 
from src.mlproject.logger import logging # hmesha use krna
import pandas as pd
from dotenv import load_dotenv
import psycopg2

load_dotenv()  # Load environment variables from .env file

host = os.getenv('host')
user = os.getenv('user')
password = os.getenv('password')
database = os.getenv('database')
port = os.getenv('port')



def read_sql_data():
    logging.info("Reading data from SQL database.")
    try:
        mydb = psycopg2.connect(host=host, user=user, password=password, database=database, port=port)
        logging.info(f"Connection Established: {mydb}")
        df = pd.read_sql('SELECT * FROM college', con=mydb)
        print(df.head())
        return df


    except Exception as ex:
        raise CustomException(ex, sys)

