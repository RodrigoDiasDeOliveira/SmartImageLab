# src/image_classifier.py
import numpy as np
from PIL import Image
from tensorflow.keras.applications.resnet50 import (
    ResNet50,
    decode_predictions,
    preprocess_input,
)
from tensorflow.keras.utils import img_to_array


class ImageClassifier:
    def __init__(self, weights="imagenet"):
        self.model = ResNet50(weights=weights)

    def classify(self, img: Image.Image, top=3):
        img = img.convert("RGB").resize((224, 224))
        arr = np.expand_dims(img_to_array(img), 0)
        preds = self.model.predict(preprocess_input(arr), verbose=0)
        return [
            {"label": lbl, "score": float(p)}
            for (_, lbl, p) in decode_predictions(preds, top=top)[0]
        ]
