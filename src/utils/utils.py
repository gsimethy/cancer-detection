import os
from box.exceptions import BoxValueError
import yaml
from src.logger.custom_logger import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any,List
import base64

@ensure_annotations
def read_yaml(yaml_file_path:Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """

    try:
        with open(yaml_file_path) as f:
            content=yaml.safe_load(f)
            logger.info(f'Yaml file loaded succesfully from {yaml_file_path}')
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(dir_path: List, verbose:bool =True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in dir_path:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"Created directory at {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """

    with open(path,'w') as f:
        json.dump(data,f,indent=4)

    logger.info(f"json file saved at : {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content=json.load(f)

    logger.info(f"json file loaded succesfully from {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(path: Path, data: Any):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data,filename=path)
    logger.info(f"Binary succesfully saved at {path}")

@ensure_annotations
def load_bin(path: Path):
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(filename=path)
    logger.info(f"The binary file is loaded succesfully from {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size=round(os.path.getsize(path)/1024)
    return f"File size of {path} is {size} KB"

@ensure_annotations
def decode_image(img_string: str, filename: Path):
    """
    Converts image string to base64 format
    """
    img_data=base64.b64encode(img_string)
    with open(filename,'wb') as f:
        f.write(img_data)
        f.close()
    logger.info(f"Image succesfully decoded at location {filename}")

@ensure_annotations
def encode_image(filename:Path):
    """
    Converts base64 format to image string
    """
    with open(filename,'rb') as f:
        return base64.b64encode(f.read())
