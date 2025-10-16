from src.cnn.constants import *
from src.cnn.utils.common import *
import os
from src.cnn.entity.config_entity import diconfig

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
