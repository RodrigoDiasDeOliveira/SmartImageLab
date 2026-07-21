# src/image_validator.py
from pathlib import Path

from PIL import Image


class ImageValidator:
    """
    Validation utilities for images and AI models.
    """

    VALID_MODEL_EXTENSIONS = {
        ".h5",
        ".pt",
        ".pth",
        ".onnx",
    }

    MODEL_ALIASES = {
        "imagenet",
        "yolov5s",
        "yolov5m",
        "yolov5l",
    }

    def is_valid(self, image_path) -> bool:
        """
        Validates an image file on disk.
        Used by the unit tests.
        """

        try:
            image = Image.open(image_path)
            image.verify()
            return True

        except Exception:
            return False

    def validate_image(self, image) -> bool:
        """
        Validates an in-memory PIL image.
        Used by the processing pipeline.
        """

        return (
            isinstance(image, Image.Image) and image.size[0] > 0 and image.size[1] > 0
        )

    def validate_model_path(self, model_path) -> bool:

        if not isinstance(model_path, str):
            return False

        model_path = model_path.strip()

        if not model_path:
            return False

        if model_path in self.MODEL_ALIASES:
            return True

        path = Path(model_path)

        if not path.exists():
            return False

        return path.suffix.lower() in self.VALID_MODEL_EXTENSIONS
