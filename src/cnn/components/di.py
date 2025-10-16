import os
import zipfile
import gdown
from src.cnn import logger
from src.cnn.utils.common import get_size
from src.cnn.entity.config_entity import *
class di:
    def __init__(self,config:diconfig):
        self.config=config
    def download_file(self)->str:
        try:
            data_url=self.config.source_URL
            zip_url=self.config.local_data_file
            os.makedirs('artifacts/data_ingestion',exist_ok=True)
            file_id=data_url.split('/')[-2]
            prefix='https://drive.google.com/uc?export=download&id='
            gdown.download(prefix+file_id,zip_url)
        except Exception as e:
            raise e
    def extract_zip(self):
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file) as zip_ref:
            zip_ref.extractall(unzip_path)
            
