from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir:Path
    source_url:str
    local_file:Path
    unzip_dir:Path


@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    model_path: Path
    updated_model_path: Path
    image_size: list
    learning_rate:float
    weights: str
    classes:int
    include_top: bool

@dataclass(frozen=True)
class PrepareCallbackConfig:
    root_dir: Path
    tensorboard_log_root_dir: Path
    checkpoint_model_file_path: Path

@dataclass(frozen=True)
class TrainingConfig:
    root_dir: Path
    trained_model_path: Path
    updated_model_path: Path
    training_data: Path
    params_epochs: int
    params_batch_size: int
    params_is_augmentation: bool
    params_image_size: list


@dataclass(frozen=True)
class EvaluationConfig:
    path_of_model: Path
    training_data: Path
    all_params: dict
    params_image_size: list
    params_batch_size: int
