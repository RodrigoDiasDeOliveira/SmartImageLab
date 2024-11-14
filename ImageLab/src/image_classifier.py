# src/image_classifier.py
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.preprocessing import image
import numpy as np

class ImageClassifier:
    def __init__(self, model_path=None):
        self.model = ResNet50(weights=model_path or 'imagenet')

    def classify(self, img):
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)
        predictions = self.model.predict(img)
        # Conversão de predicções em rótulos legíveis.
