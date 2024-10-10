from textsummarizer.config.configuration import configurationManager
from textsummarizer.components.data_validation import DataValidation
from textsummarizer.logging import logger

class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = configurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation_config = DataValidation(config=data_validation_config)
        data_validation_config.validate_all_files_exist()