import os
import sys

from Network_Security.exception.exception import NetworkSecurityException 
from Network_Security.logger.logger import logging

from Network_Security.entity.artifact_entity import DataTransformationArtifact,ModelTrainerArtifact
from Network_Security.entity.config_entity import ModelTrainerConfig

from xgboost import XGBClassifier

from Network_Security.utils.ml_utils.model.estimator import NetworkModel
from Network_Security.utils.main_utils.utils import save_object,load_object
from Network_Security.utils.main_utils.utils import load_numpy_array_data
from Network_Security.utils.ml_utils.metric.classification_metric import get_classification_score


class ModelTrainer:
    def __init__(self, model_trainer_config : ModelTrainerConfig, data_transformation_artifact : DataTransformationArtifact):
        try:
            self.model_trainer_config = model_trainer_config
            self.data_transformation_artifact = data_transformation_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def perform_hyper_param_tuning(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def train_model(self, X_train, y_train):
        try:
            xgb_clf = XGBClassifier()
            xgb_clf.fit(X_train, y_train)
            return xgb_clf
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def initiate_model_trainer(self):
        try:
            train_file_path = self.data_transformation_artifact.transformed_train_file_path
            test_file_path = self.data_transformation_artifact.transformed_test_file_path

            train_arr = load_numpy_array_data(train_file_path)
            test_arr = load_numpy_array_data(test_file_path)

            X_train, y_train, X_test, y_test = (
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:, :-1],
                test_arr[:, -1]
            )

            model = self.train_model(X_train, y_train)

            y_train_pred = model.predict(X_train)

            classification_train_metric = get_classification_score(y_true=y_train, y_pred=y_train_pred)

            if classification_train_metric.f1_score <= self.model_trainer_config.expected_accuracy:
                raise Exception("Trained Model is not up to mark")
            
            y_test_pred = model.predict(X_test)
            classification_test_metric = get_classification_score(y_true=y_test, y_pred=y_test_pred)

            diff = abs(classification_train_metric.f1_score - classification_test_metric.f1_score)

            if diff > self.model_trainer_config.overfitting_underfitting_threshold:
                raise Exception("Model is not good try optimization")
            
            preprocessor = load_object(file_path=self.data_transformation_artifact.transformed_object_file_path)

            model_dir_path = os.path.dirname(self.model_trainer_config.trained_model_file_path)
            os.makedirs(model_dir_path,exist_ok=True)
            Network_Model = NetworkModel(preprocessor=preprocessor,model=model)
            save_object(self.model_trainer_config.trained_model_file_path, obj=Network_Model)

            #model trainer artifact

            model_trainer_artifact = ModelTrainerArtifact(trained_model_file_path=self.model_trainer_config.trained_model_file_path, train_metric_artifact=classification_train_metric, test_metric_artifact=classification_test_metric)
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")
            return model_trainer_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    