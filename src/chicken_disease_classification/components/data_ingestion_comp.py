import os
import urllib.request as request
import zipfile
from chicken_disease_classification import logger
from chicken_disease_classification.utils.common import get_size
from chicken_disease_classification.entity.config_entity import DataIngestionConfig
from pathlib import Path


class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_url,
                filename=self.config.local_file
            )
        else:
            logger.info(f"file already exists of size: {get_size(Path(self.config.local_file))}")
    
    def extract_zip_file(self):
        '''
        zip_path:str
        Access the zip file and extracts all the information and finally creates
        and store them in a directory
        Return None
        '''
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_file,'r') as f:
            f.extractall(unzip_path)