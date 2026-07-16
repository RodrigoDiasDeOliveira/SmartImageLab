# src/image_generator.py
import base64
import io

import requests
from openai import OpenAI
from PIL import Image

from .config_manager import ConfigManager
from .error_logger import ErrorLogger


class ImageGenerator:
    """
    Generates images using the OpenAI Images API.
    """

    def __init__(self, api_key=None, client=None):

        self.err = ErrorLogger()

        if client is not None:
            self.client = client
            return

        if api_key is None:
            cfg = ConfigManager()
            api_key = cfg.get_api_key("openai")

        self.client = OpenAI(api_key=api_key)

    def generate(self, prompt: str, size="1024x1024"):

        try:

            response = self.client.images.generate(
                model="gpt-image-1",
                prompt=prompt,
                size=size,
                n=1,
            )

            image = response.data[0]

            if getattr(image, "url", None):
                return image.url

            if getattr(image, "b64_json", None):
                return self._decode_image(image.b64_json)

            return None

        except Exception as exc:
            self.err.log_error(f"generate(): {exc}")
            return None

    def generate_image(self, prompt: str, size="1024x1024"):

        result = self.generate(prompt, size)

        if isinstance(result, Image.Image):
            return result

        if isinstance(result, str):
            return self.download_image(result)

        return None

    def download_image(self, url):

        try:

            response = requests.get(url, timeout=30)
            response.raise_for_status()

            return Image.open(io.BytesIO(response.content))

        except Exception as exc:

            self.err.log_error(f"download_image(): {exc}")

            return None

    @staticmethod
    def _decode_image(data):

        binary = base64.b64decode(data)

        return Image.open(io.BytesIO(binary))