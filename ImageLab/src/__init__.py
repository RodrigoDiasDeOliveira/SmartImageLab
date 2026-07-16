# src/__init__.py

import logging
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)

from .image_preprocessor import ImagePreprocessor
from .image_classifier import ImageClassifier
from .image_identifier import ImageIdentifier
from .image_storage import ImageStorage
from .image_logger import ImageLogger
from .error_logger import ErrorLogger
from .config_manager import ConfigManager
from .image_validator import ImageValidator
from .image_pipeline import ImagePipeline
from .image_generator import  ImageGenerator

__all__ = [
    "ImagePreprocessor",
    "ImageClassifier",
    "ImageIdentifier",
    "ImageStorage",
    "ImageLogger",
    "ErrorLogger",
    "ConfigManager",
    "ImageValidator",
    "ImagePipeline",
    "ImageGenerator"
]