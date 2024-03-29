from ML_project import logger
from ML_project.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
#from ML_project.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
#from ML_project.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
#from ML_project.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
#from ML_project.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline



STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e