from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    zip_file_path: Path
    unzip_dir: Path

@dataclass
class BaseModelConfig:
    root_dir: Path
    base_model_file_path: Path
    updated_base_model_file_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: float
    params_weights: str
    params_classes: int
    

@dataclass(frozen=True)
class TrainingConfig:
    root_dir: Path
    trained_model_path: Path
    updated_base_model_file_path: Path
    training_data: Path
    params_epochs: int
    params_batch_size: int
    params_augmentation: bool
    params_image_size: list

@dataclass(frozen=True)
class EvaluationConfig:
    model_path: Path
    training_data: Path
    all_params: dict
    mlflow_uri: dict
    params_image_size: list
    params_batch_size: int
    
