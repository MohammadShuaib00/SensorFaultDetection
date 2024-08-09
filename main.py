import sys
from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.exception import SensorException
from sensor.logger import logging
from sensor.pipeline.training_pipeline import TrainPipeline
from sensor.pipeline import training_pipeline
from sensor.ml.model.estimator import ModelResolver,TargetValueMapping
from sensor.utils.main_utils import load_object
from sensor.constant.training_pipeline import SAVED_MODEL_DIR
from sensor.utils.main_utils import read_yaml_file


if __name__ == "__main__":
   data = TrainPipeline()
   data_ignestion = data.start_data_ingestion()
   data_valiation_arf = data.start_data_validaton(data_ignestion)
   data_transfor = data.start_data_transformation(data_valiation_arf)
   data_trainer = data.start_model_trainer(data_transfor)
   data_eval = data.start_model_evaluation(data_valiation_arf,data_trainer)
   data.start_model_pusher(data_eval)
   
   
