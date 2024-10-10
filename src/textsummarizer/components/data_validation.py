import os
from textsummarizer.logging import logger
from textsummarizer.entity import DataValidationConfig

import os

class DataValidation:
    def __init__(self, config):
        self.config = config

    def validate_all_files_exist(self) -> bool:
        try:
            # Ensure directory exists
            dataset_dir = os.path.join("artifacts", "data_ingestion", "samsum_dataset")
            if not os.path.exists(dataset_dir):
                raise FileNotFoundError(f"Directory not found: {dataset_dir}")
            
            # Get list of files in the directory
            all_files = os.listdir(dataset_dir)
            
            # Initialize validation status
            validation_status = True
            missing_files = []

            # Check if all required files exist
            for required_file in self.config.ALL_REQUIRED_FILES:
                if required_file not in all_files:
                    validation_status = False
                    missing_files.append(required_file)

            # Ensure status directory exists
            os.makedirs(os.path.dirname(self.config.STATUS_FILE), exist_ok=True)

            # Write the validation status to the file
            with open(self.config.STATUS_FILE, 'w') as f:
                if validation_status:
                    f.write(f"Validation status: {validation_status}. All files are present.\n")
                else:
                    f.write(f"Validation status: {validation_status}. Missing files: {', '.join(missing_files)}\n")
            
            return validation_status

        except Exception as e:
            raise e
