from textsummarizer.config.configuration import configurationManager
from textsummarizer.components.data_transformation import DataTransformation
from textsummarizer.logging import logger

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = configurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation_config = DataTransformation(config=data_transformation_config)
        data_transformation_config.convert()