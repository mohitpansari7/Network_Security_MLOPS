import os
import sys

import pandas as pd

from Network_Security.exception.exception import NetworkSecurityException
from Network_Security.logger.logger import logging

from Network_Security.constants.training_pipeline import SCHEMA_FILE_PATH
from Network_Security.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from Network_Security.entity.config_entity import DataValidationConfig
from Network_Security.exception.exception import NetworkSecurityException 
from Network_Security.logger.logger import logging 
from Network_Security.utils.main_utils.utils import read_yaml_file,write_yaml_file
from scipy.stats import ks_2samp
import pandas as pd
import os,sys


class DataValidation:
    def __init__(self) -> None:
        pass

    def validate_number_of_columns(self, dataframe):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    @staticmethod
    def read_data(file_path):
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def detect_dataset_drift(self, base_df, current_df, threshold=0.05):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def initiate_data_validation(self):
        try:
            self.read_data()
            self.validate_number_of_columns()
            self.detect_dataset_drift()
        except Exception as e:
            raise NetworkSecurityException(e, sys)