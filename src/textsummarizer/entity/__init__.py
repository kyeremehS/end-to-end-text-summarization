from pathlib import Path
from typing import List
from pydantic import BaseModel, ConfigDict

class DataIngestionConfig(BaseModel):
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
    model_config = ConfigDict(frozen=True)

class DataValidationConfig(BaseModel):
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: List[str]
    model_config = ConfigDict(frozen=True)

class DataTransformationConfig(BaseModel):
    root_dir: Path
    data_path: Path
    tokenizer_name: str
    model_config = ConfigDict(frozen=True)

class ModelTrainerConfig(BaseModel):
    root_dir: Path
    data_path: Path
    model_ckpt: str
    num_train_epochs: int
    warmup_steps: int
    per_device_train_batch_size: int
    weight_decay: float
    logging_steps: int
    evaluation_strategy: str
    eval_steps: int
    save_steps: int
    gradient_accumulation_steps: int
    model_config = ConfigDict(frozen=True)

class ModelEvaluationConfig(BaseModel):
    root_dir: Path
    data_path: Path
    tokenizer_path: Path
    metric_file_path: Path
    model_config = ConfigDict(frozen=True)
