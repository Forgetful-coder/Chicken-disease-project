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

