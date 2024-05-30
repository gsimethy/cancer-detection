import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

def create():

    project_name="chest_cancer_classification"

    dir_list=[
        f"src/{project_name}/__init__.py",
        f"src/{project_name}/components/__init__.py",
        f"src/{project_name}/utils/__init__.py",
        f"src/{project_name}/config/__init__.py",
        f"src/{project_name}/constants/__init__.py",
        f"src/{project_name}/pipeline/__init__.py",
        f"src/{project_name}/entity/__init__.py",
        'config/config.yaml',
        'params.yaml',
        'dvc.yaml',
        'setup.py',
        'requirements.txt'
    ]

    for filepath in dir_list:
        filepath=Path(filepath)
        file_dir,file_name=os.path.split(filepath)
        

        if filepath!="":
            os.makedirs(filepath,exist_ok=True)
            logging.info(f"Created file directory: {file_dir}")

        if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
            with open(filepath,"w",) as f:
                pass
                logging.info(f"Created file : {file_name}")

        else:
            logging.info(f"File : {file_name} already exists")

if __name__=="__main__":
    create()

