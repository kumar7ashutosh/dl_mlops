from src.cnn import logger
from src.cnn.pipeline.di import dipipeline
stage_name='data ingestion training'

logger.info(f'{stage_name} started')
obj=dipipeline()
obj.main()
logger.info(f'{stage_name} completed')