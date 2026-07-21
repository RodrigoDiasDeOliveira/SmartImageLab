# src/image_pipeline.py
from .config_manager import ConfigManager
from .error_logger import ErrorLogger
from .image_classifier import ImageClassifier
from .image_generator import ImageGenerator
from .image_identifier import ImageIdentifier
from .image_logger import ImageLogger
from .image_preprocessor import ImagePreprocessor
from .image_storage import ImageStorage
from .image_validator import ImageValidator


class ImagePipeline:
    def __init__(self):
        cfg = ConfigManager()
        self.flags = cfg.get("pipeline", default={}) or {}

        self.generator = ImageGenerator()
        self.preprocessor = ImagePreprocessor()
        self.validator = ImageValidator()

        self.classifier = (
            ImageClassifier() if self.flags.get("enable_classification") else None
        )

        self.identifier = (
            ImageIdentifier() if self.flags.get("enable_identification") else None
        )

        self.storage = ImageStorage() if self.flags.get("enable_storage") else None

        self.log = ImageLogger()
        self.err = ErrorLogger()

    def execute_pipeline(self, prompt: str, image_name: str):

        image = self.generator.generate_image(prompt)

        if not self.validator.validate_image(image):
            self.err.log_error("Invalid image")
            return {"error": "invalid_image"}

        self.log.log_processing(image_name)

        processed = self.preprocessor.preprocess_image(image)

        result = {}

        if self.classifier:
            result["classification"] = self.classifier.classify(processed)

        if self.identifier:
            result["identification"] = self.identifier.identify(processed)

        if self.storage and self.storage.upload_image(processed, image_name):
            self.log.log_upload(image_name)

        return result
