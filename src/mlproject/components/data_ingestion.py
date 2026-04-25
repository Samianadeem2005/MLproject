# This file gives order to the functions present in utils.py to load data. 

import os
import sys
from src.mlproject.exception import CustomException # hmesha use krna 
from src.mlproject.logger import logging # hmesha use krna
import pandas as pd
from src.mlproject.utils import read_sql_data
from sklearn.model_selection import train_test_split

from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'raw.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        try:
            # reading data from mysql
            df = read_sql_data()
            logging.info("Data read from SQL database successfully.")

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True) # create artifacts directory if not exists , we can give any path either raw_data_path or train_data_path or test_data_path because all are in artifacts folder.

            df.to_csv(self.ingestion_config.raw_data_path, index=False,header=True)# save the data in raw_data_path in artifacts folder 
                # split the data into train and test
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False,header=True) # save the train data in train_data_path in artifacts folder
            test_set.to_csv(self.ingestion_config.test_data_path, index=False,header=True)

            logging.info("Data ingestion completed successfully.")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        
        except Exception as ex:
            raise CustomException(ex, sys)

