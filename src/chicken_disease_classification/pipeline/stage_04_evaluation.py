from chicken_disease_classification.config.configuration import ConfigurationManager
from chicken_disease_classification import logger
from chicken_disease_classification.components import evaluation_comp

STAGE_NAME = 'Evaluation'

class EvaluationPipeline:
    def __init__(self):
        pass
    
    def main(self):
     try:
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = evaluation_comp.Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()

     except Exception as e:
        raise e

if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e