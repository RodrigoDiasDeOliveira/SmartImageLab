# src/image_classifier.py
import numpy as np
from PIL import Image

class ImageClassifier:
    def __init__(self, weights="imagenet"):
        from tensorflow.keras.applications.resnet50 import (
            ResNet50,
            decode_predictions,
            preprocess_input,
        )
        from tensorflow.keras.utils import img_to_array

        self.decode_predictions = decode_predictions
        self.preprocess_input = preprocess_input
        self.img_to_array = img_to_array
        self.model = ResNet50(weights=weights)

    def classify(self, img: Image.Image, top=3):
        img = img.convert("RGB").resize((224, 224))
        arr = np.expand_dims(self.img_to_array(img), 0)
        preds = self.model.predict(self.preprocess_input(arr), verbose=0)

        return [
            {"label": lbl, "score": float(score)}
            for (_, lbl, score) in self.decode_predictions(preds, top=top)[0]
        ]