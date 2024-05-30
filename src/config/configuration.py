import os
from src.constants import * 
from src.utils.utils import read_yaml,create_directories
from src.entity.config_entity import DataIngestionConfig,BaseModelConfig,TrainingConfig,EvaluationConfig

class ConfigurationManager:
    def __init__(
            self,
            config_path= CONFIG_FILE_PATH,
            params_path= PARAMS_FILE_PATH,
    ):
        
        self.config=read_yaml(config_path)
        self.params=read_yaml(params_path)

        create_directories([self.config.artifact_dir])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config=self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_URL,
            zip_file_path=config.zip_file_path,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config
    
    def base_model_config(self) -> BaseModelConfig:
        config=self.config.base_model
        create_directories([config.root_dir])

        base_model_config=BaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_file_path=Path(config.base_model_file_path),
            updated_base_model_file_path=Path(config.updated_base_model_file_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS,
            params_classes=self.params.CLASSES
        )

        return base_model_config
    

    def get_training_config(self) -> TrainingConfig:
        training=self.config.model_training
        base_model=self.config.base_model
        params=self.params
        training_data=os.path.join(self.config.data_ingestion.unzip_dir,'Chest-CT-Scan-data')
        create_directories([Path(training.root_dir)])

        training_config=TrainingConfig(
            root_dir=Path(training.root_dir),
            trained_model_path=Path(training.trained_model_path),
            updated_base_model_file_path=Path(base_model.updated_base_model_file_path),
            training_data=Path(training_data),
            params_epochs=params.EPOCHS,
            params_batch_size=params.BATCH_SIZE,
            params_augmentation=params.AUGMENTATION,
            params_image_size=params.IMAGE_SIZE
        )

        return training_config
    
    
    def get_evaluation_config(self) -> EvaluationConfig:
        training=self.config.model_training
        eval_config=EvaluationConfig(
            model_path=training.trained_model_path,
            training_data="artifacts/data_ingestion/Chest-CT-Scan-data",
            mlflow_uri='https://dagshub.com/gsimethy/cancer-detection.mlflow',
            all_params=self.params,
            params_image_size=self.params.IMAGE_SIZE,
            params_batch_size=self.params.BATCH_SIZE
        )

        return eval_config

    

    
    