from src.config.configuration import ConfigurationManager
from src.components.model_evaluation import ModelEvaluation
from src.logger.custom_logger import logger

STAGE_NAME = "Evaluation stage"

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        eval_config=config.get_evaluation_config()
        evaluation=ModelEvaluation(eval_config)
        evaluation.evaluation()
        evaluation.save_score()
        # evaluation.log_into_mlflow()
