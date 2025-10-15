import os,logging
from pathlib import Path

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s')
project_name='cnn'
list_of_files=[
    '.github/workflows/.gitkeep',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/utils/common.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/config/configuration.py',
    'config/config.yaml',
    'dvc.yaml',
    'params.yaml',
    'notebook/exp.ipynb',
    'templates/index.html'
]
for i in list_of_files:
    i=Path(i)
    filedir,filename=os.path.split(i)
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f'{filename} created at {filedir}')
    if (not os.path.exists(i)) or (os.path.getsize(i)==0):
        with open (i,'w') as f:
            pass
            logging.info(f'creating empty file : {i}')
    else:
        logging.info(f'{filename} already exists')