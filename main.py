from chicken_disease_classification import logger
from chicken_disease_classification.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = 'Data_ingestion'




if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e