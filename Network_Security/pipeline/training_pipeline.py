import os
import sys

from Network_Security.exception.exception import NetworkSecurityException
from Network_Security.logger.logger import logging

from Network_Security.components.data_ingestion import DataIngestion 
from Network_Security.components.data_transformation import DataTransformation
from Network_Security.components.data_validation import DataValidation
from Network_Security.components.model_trainer import ModelTrainer
from Network_Security.components.model_evaluation import ModelEvaluation
from Network_Security.components.model_pusher import ModelPusher

from Network_Security.entity.config_entity import (
    TrainingPipelineConfig,
    DataIngestionConfig,
    DataTransformationConfig,
    DataValidationConfig,
    ModelTrainerConfig,
    ModelEvaluationConfig,
    ModelPusherConfig
)

from Network_Security.entity.artifact_entity import (
    DataIngestionArtifact,
    DataTransformationArtifact,
    DataValidationArtifact,
    ModelTrainerArtifact,
    ModelEvaluationArtifact,
    ModelPusherArtifact
)

class TrainingPipeline:
    def __init__(self):
        pass

    def start_data_ingestion(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def start_data_validation(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def start_data_transformation(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def start_model_trainer(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def start_model_evaluation(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def start_model_pusher(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def run_pipeline(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)