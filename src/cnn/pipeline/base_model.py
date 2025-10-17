from src.cnn.config.configuration import *
from src.cnn.components.base_model import *
from src.cnn import logger

stage_name='base model'

class bmpipeline:
    def __init__(self):
        pass 
    def main(self):
        config=configurationmanager()
        prepare_base_model_config=config.prepare_base_model()
        prepare_base_model=preparebasemodel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()

if __name__=='__main__':
    logger.info(f'{stage_name} started')
    obj=bmpipeline()
    obj.main()
    logger.info(f'{stage_name} completed')
        