from src.cnn.constants import *
from src.cnn.utils.common import *
import os
from src.cnn.entity.config_entity import *

class configurationmanager:
    def __init__(self,config_filepath=CONFIG_FILE_PATH,params_filepath=PARAMS_FILE_PATH):
        self.config=read_yaml(config_filepath)
        self.params=read_yaml(params_filepath)
        
        create_directories([self.config.artifacts_root])
        
    def get_di_config(self)->diconfig:
        config=self.config.data_ingestion
        create_directories([config.root_dir])
        di_config=diconfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return di_config

    def prepare_base_model(self)->PrepareBaseModelConfig:
        config=self.config.prepare_base_model
        create_directories([config.root_dir])
        prepare_base_model_config=PrepareBaseModelConfig(
            root_dir=config.base_model_path,
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=config.updated_base_model_path,
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS,
            params_classes=self.params.CLASSES
        )
        return prepare_base_model_config
    