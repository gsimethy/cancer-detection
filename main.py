from src.logger.custom_logger import logger
from src.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.pipeline.stage_02_base_model import BaseModelTrainingPipeline
from src.pipeline.stage_03_model_training import ModelTrainingPipeline
from src.pipeline.stage_04_model_evaluation import EvaluationPipeline

from src.config.configuration import ConfigurationManager
from src.components.data_ingestion import DataIngestion
from src.logger.custom_logger import logger



STAGE_NAME = "Data Ingestion Stage"




try:
    logger.info(f"*********** {STAGE_NAME} started **************")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"*********** {STAGE_NAME} ended **************")
except Exception as e:
    logger.exception(e)
    raise e 

STAGE_NAME = 'Prepare base model'
    
if __name__=="__main__":
    try:
        logger.info(f"*********** {STAGE_NAME} started **************")
        obj=BaseModelTrainingPipeline()
        obj.main()
        logger.info(f"*********** {STAGE_NAME} ended **************")
    except Exception as e:
        logger.exception(e)
        raise e
    

    STAGE_NAME="training"

    if __name__=="__main__":
        try:
            logger.info(f"*********** {STAGE_NAME} started **************")
            obj=ModelTrainingPipeline()
            obj.main()
            logger.info(f"*********** {STAGE_NAME} ended **************")
        except Exception as e:
            logger.exception(e)
            raise e
        
    STAGE_NAME = "Evaluation stage"

    if __name__=="__main__":
        try:
            logger.info(f"*********** {STAGE_NAME} started **************")
            obj=EvaluationPipeline()
            obj.main()
            logger.info(f"*********** {STAGE_NAME} ended **************")
        except Exception as e:
            logger.exception(e)
            raise e