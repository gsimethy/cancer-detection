import os
import zipfile
import gdown
from src.logger.custom_logger import logger
from src.utils.utils import get_size
from src.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config

    def download_file(self) -> None:
        """
        Download data from the url
        """

        try:
            url=self.config.source_url
            zip_download_dir=self.config.zip_file_path
            os.makedirs(self.config.unzip_dir,exist_ok=True)
            logger.info(f"Downloading the data from {url} into file {zip_download_dir}")

            file_id = url.split("/")[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix+file_id,zip_download_dir)

            logger.info(f"Downloaded data from {url} into file {zip_download_dir}")
        except Exception as e:
            raise e
    
    def extract_zip_file(self) -> None:
        """
        Extracts the zip file into the data folder
        """
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.zip_file_path,'r') as zip:
            zip.extractall(unzip_path)

