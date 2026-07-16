# src/image_preprocessor.py
from pathlib import Path

import numpy as np
from PIL import Image


class ImagePreprocessor:
    """
    Image preprocessing utilities.
    """

    def __init__(self, size=(224, 224)):

        self.size = size

    def preprocess_image(self, image: Image.Image):

        return image.convert("RGB").resize(self.size)

    def load(self, image_path):

        return Image.open(image_path)

    def resize(self, image):

        return image.resize(self.size)

    def to_numpy(self, image):

        if isinstance(image, (str, Path)):
            image = Image.open(image)

        image = self.preprocess_image(image)

        return np.asarray(image)

    def to_tensor(self, image):

        """
        Returns a NumPy tensor (C,H,W).

        This avoids adding a hard dependency on torch
        while remaining compatible with future ML code.
        """

        array = self.to_numpy(image)

        return np.transpose(array, (2, 0, 1))