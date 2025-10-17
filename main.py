from src.cnn import logger
from src.cnn.pipeline.di import dipipeline
from src.cnn.pipeline.base_model import bmpipeline
stage_name='data ingestion training'

logger.info(f'{stage_name} started')
obj=dipipeline()
obj.main()
logger.info(f'{stage_name} completed')

stage_name='base model'
logger.info(f'{stage_name} started')
obj=bmpipeline()
obj.main()
logger.info(f'{stage_name} completed')