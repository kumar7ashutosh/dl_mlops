import os
from box.exceptions import BoxValueError
import yaml
from src.cnn import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path:Path)->ConfigBox:
    try:
        with open(path) as f:
            data=yaml.safe_load(f)
            logger.info(f'{path} loaded successfully')
            return ConfigBox(data)
    except BoxValueError:
        raise ValueError('yaml file is empty')
    except Exception as e:
        raise e

@ensure_annotations

def create_directories(directories:list,verbose=True):
    for path in directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f'created directory at {path}')

@ensure_annotations

def save_json(path:Path,data:dict):
    with open(path,'w') as f:
        json.dump(data,f,indent=4)
    logger.info(f'json file saved at {path}')
    
@ensure_annotations
 
def load_json(path:Path)->ConfigBox:
    with open(path) as f:
        data=json.load(f)
    logger.info(f'json file loaded from {path}')
    return ConfigBox(data)

@ensure_annotations
def save_bin(data:Any,path:Path):
    joblib.dump(value=data,filename=path)
    logger.info(f'binary file saved at {path}')
    
@ensure_annotations
def load_bin(path:Path)->Any:
    data=joblib.load(path)
    logger.info(f'binary file loaded at {path}')
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"


def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())
