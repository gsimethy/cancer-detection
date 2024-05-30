import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
import time
from src.entity.config_entity import TrainingConfig
from pathlib import Path

class Training:
    def __init__(self,config:TrainingConfig):
        self.config=config

        # Check for GPU availability
        gpus = tf.config.list_physical_devices('GPU')
        if gpus:
            try:
                for gpu in gpus:
                    tf.config.experimental.set_memory_growth(gpu, True)
                logical_gpus = tf.config.list_logical_devices('GPU')
                print(f"{len(gpus)} Physical GPUs, {len(logical_gpus)} Logical GPUs")
            except RuntimeError as e:
                print(e)

    def get_base_model(self):
        self.model=tf.keras.models.load_model(
            self.config.updated_base_model_file_path
        )
    
    def train_valid_generator(self):
        data_gen_kwargs=dict(
            rescale= 1./255,
            validation_split=0.20
        )

        dataflow_kwargs= dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation='bilinear'
        )

        valid_gen= tf.keras.preprocessing.image.ImageDataGenerator(
            **data_gen_kwargs
        )

        self.valid_gen= valid_gen.flow_from_directory(
            directory=self.config.training_data,
            subset='validation',
            shuffle=False,
            **dataflow_kwargs
        )

        if self.config.params_augmentation:
            train_gen=tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=40,
                horizontal_flip=True,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                **data_gen_kwargs
            )
        else:
            train_gen=valid_gen

        self.train_gen=train_gen.flow_from_directory(
            directory=self.config.training_data,
            subset='training',
            shuffle=True,
            **dataflow_kwargs
        )

    @staticmethod
    def save_model(path: Path, model=tf.keras.Model):
        model.save(path)

    def train(self):
        self.steps_per_epoch = self.train_gen.samples//self.train_gen.batch_size
        self.validation_steps = self.valid_gen.samples//self.valid_gen.batch_size

        self.model.fit(
            self.train_gen,
            epochs=self.config.params_epochs,
            steps_per_epoch=self.steps_per_epoch,
            validation_steps=self.validation_steps,
            validation_data=self.valid_gen
        )

        self.save_model(
            path=self.config.trained_model_path,
            model=self.model
        )