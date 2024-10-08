import os
import sys
import json

from dotenv import load_dotenv # type: ignore
load_dotenv()
MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi
ca = certifi.where()

import pandas as pd
import numpy as np

import pymongo # type: ignore

from Network_Security.exception.exception import NetworkSecurityException
from Network_Security.logger.logger import logging

class NetworkDataExtraction():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def csv_to_json_converter(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def push_data_to_mongo(self, records, database, collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records

            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]

            self.collection.insert_many(self.records)
            return len(self.records)
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
if __name__ == "__main__":
    FILE_PATH = './Network_Data/NetworkData.csv'
    DATABASE = 'NetworkSecurity'
    COLLECTION = 'NetworkData'

    networkObj = NetworkDataExtraction()
    records = networkObj.csv_to_json_converter(FILE_PATH)
    num_records_inserted = networkObj.push_data_to_mongo(records, DATABASE, COLLECTION)
    print(num_records_inserted)