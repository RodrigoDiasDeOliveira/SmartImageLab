# src/__init__.py

import logging

# Configura o logger para o projeto
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Importa módulos principais
from .image_processor import ImageProcessor
from .image_classifier import ImageClassifier
from .image_identifier import ImageIdentifier
from .image_storage import ImageStorage
from .image_logger import ImageLogger

# Mensagem de boas-vindas ou inicialização
logger.info("ImageLab package initialized.")
