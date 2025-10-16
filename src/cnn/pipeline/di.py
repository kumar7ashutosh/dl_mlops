from src.cnn.config.configuration import configurationmanager
from src.cnn.components.di import di
from src.cnn import logger

stage_name='data ingestion training'

class dipipeline:
    def __init__(self):
        pass
    def main(self):
        config=configurationmanager()
        di_config=config.get_di_config()
        di1=di(config=di_config)
        di1.download_file()
        di1.extract_zip()
        
if __name__=='__main__':
    logger.info(f'{stage_name} started')
    obj=dipipeline()
    obj.main()
    logger.info(f'{stage_name} completed')