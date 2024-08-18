import os
import sys

from Network_Security.exception.exception import NetworkSecurityException
from Network_Security.logger.logger import logging

from Network_Security.pipeline.training_pipeline import TrainingPipeline

def start_training():
    try:
        pass
    except Exception as e:
        raise NetworkSecurityException(e, sys)

if __name__ == '__main__':
    start_training()