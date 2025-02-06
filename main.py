from ml_project import logger
from ml_project.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from ml_project.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nX==========X")
except Exception as e:
    logger.exception(f"stage {STAGE_NAME} failed",e)
    raise e


STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nX==========X")
except Exception as e:
    logger.exception(f"stage {STAGE_NAME} failed",e)
    raise e