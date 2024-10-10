import os
from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from transformers import AutoModelForSeq2SeqLM, DataCollatorForSeq2Seq
import torch
from datasets import load_dataset, load_from_disk
from textsummarizer.entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self,config: ModelTrainerConfig):
        self.config = config

    def train(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
        seq2seq_data_collector = DataCollatorForSeq2Seq(tokenizer,model=model_pegasus)

        # loading data
        dataset_sansum_pt = load_from_disk(self.config.data_path)

       # trainer_args = TrainingArguments(
            #output_dir = self.config.root_dir,
            #data_path = self.config.data_path,
            #model_ckpt = self.config.model_ckpt,
            #num_train_epochs = self.params.num_train_epochs,
            #warmup_steps = self.params.warmup_steps,
            #per_device_train_batch_size  = self.params.per_device_train_batch_size,
            #weight_decay = self.params.weight_decay,
            #logging_steps = self.params.logging_steps,
            #evaluation_strategy = self.params.evaluation_strategy,
            #eval_steps = self.params.eval_steps = 1e6,
            #save_steps = self.params.save_steps,
            #gradient_accumulation_steps = self.params.gradient_accumulation_steps
        #)

        trainer_args = TrainingArguments(
            output_dir = self.config.root_dir, num_train_epochs=1,warmup_steps=500,
            per_device_train_batch_size=1, per_device_eval_batch_size=1,
            weight_decay=0.01, logging_steps=10,
            evaluation_strategy='steps',eval_steps=500, save_steps=1e6,
            gradient_accumulation_steps=16
)
        
        trainer = Trainer(model=model_pegasus, args = trainer_args,
                  tokenizer=tokenizer,data_collator=seq2seq_data_collector,
                  train_dataset=dataset_sansum_pt["test"],
                  eval_dataset=dataset_sansum_pt["validation"])
        
        trainer.train()

        # save model
        model_pegasus.save_model(os.path.join(self.config.root_dir,"pegasus-samsum-model"))

        # save tokenizer
        tokenizer.save_pretrained(os.path.join(self.config.root_dir,"tokenizer"))