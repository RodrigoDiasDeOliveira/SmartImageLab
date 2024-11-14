# src/image_processor.py
from PIL import Image
import requests
from io import BytesIO
from config_manager import ConfigManager

class ImageProcessor:
    def __init__(self):
        self.config = ConfigManager()

    def generate_image(self, prompt):
        api_key = self.config.get_api_key('openai')
        # Implementação da geração de imagem com a API da OpenAI.

    def download_image(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return Image.open(BytesIO(response.content))
        else:
            ErrorLogger().log_error("Erro ao baixar imagem.")
            return None

    def preprocess_image(self, image, size=(224, 224)):
        return image.resize(size).convert('RGB')
