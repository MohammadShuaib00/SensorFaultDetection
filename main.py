import sys
from sensor.exception import SensorException
from sensor.logger import logging
from sensor.pipeline.training_pipeline import TrainPipeline

if __name__ == "__main__":
   data = TrainPipeline()
   data_ignestion = data.start_data_ingestion()
   data.start_data_validaton(data_ignestion)
   
