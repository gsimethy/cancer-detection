from src.config.configuration import ConfigurationManager
from src.components.base_model import BaseModel
from src.logger.custom_logger import logger

STAGE_NAME = 'Prepare base model'

class BaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        base_model_config=config.base_model_config()
        base_model=BaseModel(config=base_model_config)
        base_model.get_base_model()
        base_model.update_base_model()


if __name__=="__main__":
    try:
        logger.info(f"*********** {STAGE_NAME} started **************")
        obj=BaseModelTrainingPipeline()
        obj.main()
        logger.info(f"*********** {STAGE_NAME} ended **************")
    except Exception as e:
        logger.exception(e)
        raise e