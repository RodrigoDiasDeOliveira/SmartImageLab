from .image_processor import ImageProcessor
from .image_classifier import ImageClassifier
from .image_identifier import ImageIdentifier
from .image_storage import ImageStorage
from .data_validator import DataValidator
from .image_logger import ImageLogger
from .error_logger import ErrorLogger
from .config_manager import ConfigManager

class ImagePipeline:
    def __init__(self):
        cfg = ConfigManager()
        self.flags = cfg.get("pipeline", default={}) or {}
        self.processor  = ImageProcessor()
        self.classifier = ImageClassifier() if self.flags.get("enable_classification") else None
        self.identifier = ImageIdentifier() if self.flags.get("enable_identification") else None
        self.storage    = ImageStorage()    if self.flags.get("enable_storage") else None
        self.validator  = DataValidator()
        self.log = ImageLogger(); self.err = ErrorLogger()

    def execute_pipeline(self, prompt: str, image_name: str):
        img = self.processor.generate_image(prompt)
        if not self.validator.validate_image(img):
            self.err.log_error("Imagem inválida"); return {"error": "invalid_image"}
        self.log.log_processing(image_name)
        pre = self.processor.preprocess_image(img)
        out = {}
        if self.classifier: out["classification"] = self.classifier.classify(pre)
        if self.identifier: out["identification"] = self.identifier.identify(pre)
        if self.storage and self.storage.upload_image(pre, image_name):
            self.log.log_upload(image_name)
        return out
