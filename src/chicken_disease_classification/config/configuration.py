from chicken_disease_classification.constants import *
from chicken_disease_classification.utils.common import read_yaml, create_directories
from chicken_disease_classification.entity.config_entity import DataIngestionConfig, ModelTrainerConfig


class ConfigurationManager:
    def __init__(self,
                 config_file_path=CONFIG_FILE_PATH,
                 params_file_path=PARAMS_FILE_PATH):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)

        create_directories([self.config.artifacts_root])
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_file=config.local_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config
    
    def model_trainer(self) -> ModelTrainerConfig:
            config = self.config.prepare_base_model
            params = self.params
            create_directories([config.root_dir])

            model_trainer_config = ModelTrainerConfig(
                    root_dir = config.root_dir,
                    model_path = config.model_path,
                    updated_model_path = config.updated_model_path,
                    image_size= params.IMAGE_SIZE,
                    learning_rate=params.LEARNING_RATE,
                    weights= params.WEIGHTS,
                    classes = params.CLASSES,
                    include_top=params.INCLUDE_TOP
                    )
            return model_trainer_config
        