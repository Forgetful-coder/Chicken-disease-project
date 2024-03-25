import os
from chicken_disease_classification.constants import *
from chicken_disease_classification.utils.common import read_yaml, create_directories
from chicken_disease_classification.entity.config_entity import (DataIngestionConfig, 
                                                                 ModelTrainerConfig,
                                                                 PrepareCallbackConfig,
                                                                 TrainingConfig)


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
    
    def prepare_callbacks_config(self)-> PrepareCallbackConfig:
        config = self.config.prepare_callbacks
        model_chkpoint_dir = os.path.dirname(config.checkpoint_model_file_path)
        create_directories([Path(model_chkpoint_dir),
                            Path(config.tensorboard_log_root_dir)
                            ])
        prepare_callbacks_config = PrepareCallbackConfig(
            root_dir=Path(config.root_dir),
            tensorboard_log_root_dir= Path(config.tensorboard_log_root_dir),
            checkpoint_model_file_path= Path(config.checkpoint_model_file_path)

        )
        return prepare_callbacks_config

    
    def get_training_config(self) -> TrainingConfig:
        training = self.config.training
        prepare_base_model = self.config.prepare_base_model
        params = self.params
        training_data = os.path.join(self.config.data_ingestion.unzip_dir, "Chicken_disease")
        create_directories([
            Path(training.root_dir)
        ])

        training_config = TrainingConfig(
            root_dir=Path(training.root_dir),
            trained_model_path=Path(training.trained_model_path),
            updated_model_path=Path(prepare_base_model.updated_model_path),
            training_data=Path(training_data),
            params_epochs=params.EPOCHS,
            params_batch_size=params.BATCH_SIZE,
            params_is_augmentation=params.AUGMENTATION,
            params_image_size=params.IMAGE_SIZE
        )

        return training_config
        