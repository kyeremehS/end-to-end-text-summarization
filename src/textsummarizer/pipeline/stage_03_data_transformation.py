from textsummarizer.config.configuration import configurationManager
from textsummarizer.components.data_transformation import DataTransformation
from textsummarizer.logging import logger

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = configurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataTransformation(config=data_validation_config)
        data_validation.validate_all_files_exist()