import sys
from sensor.exception import SensorException
from sensor.logger import logging
from sensor.pipeline.training_pipeline import TrainPipeline
from sensor.pipeline import training_pipeline


if __name__ == "__main__":
   data = TrainPipeline()
   data_ignestion = data.start_data_ingestion()
   data_valiation_arf = data.start_data_validaton(data_ignestion)
   data_transfor = data.start_data_transformation(data_valiation_arf)
   data.start_model_trainer(data_transfor)
   
   
