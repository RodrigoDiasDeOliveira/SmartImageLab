# src/image_pipeline.py
from image_processor import ImageProcessor
from image_classifier import ImageClassifier
from image_identifier import ImageIdentifier
from image_storage import ImageStorage
from data_validator import DataValidator

class ImagePipeline:
    def __init__(self):
        self.processor = ImageProcessor()
        self.classifier = ImageClassifier()
        self.identifier = ImageIdentifier()
        self.storage = ImageStorage()
        self.validator = DataValidator()

    def execute_pipeline(self, prompt, image_name):
        image = self.processor.generate_image(prompt)
        if not self.validator.validate_image(image):
            return "Imagem inválida."
        
        preprocessed_image = self.processor.preprocess_image(image)
        classification = self.classifier.classify(preprocessed_image)
        identification = self.identifier.identify(preprocessed_image)
        
        self.storage.upload_image(preprocessed_image, image_name)
        return {"classification": classification, "identification": identification}
