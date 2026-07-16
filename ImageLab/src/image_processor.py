import io, requests
from PIL import Image
from openai import OpenAI
from .config_manager import ConfigManager
from .error_logger import ErrorLogger

class ImageProcessor:
    def __init__(self):
        self.cfg = ConfigManager()
        self.err = ErrorLogger()
        self.client = OpenAI(api_key=self.cfg.get_api_key("openai"))

    def generate_image(self, prompt: str, size="1024x1024") -> Image.Image | None:
        try:
            resp = self.client.images.generate(
                model="gpt-image-1", prompt=prompt, size=size, n=1)
            data = resp.data[0]
            if getattr(data, "b64_json", None):
                import base64
                return Image.open(io.BytesIO(base64.b64decode(data.b64_json)))
            return self.download_image(data.url)
        except Exception as e:
            self.err.log_error(f"generate_image: {e}"); return None

    def download_image(self, url):
        r = requests.get(url, timeout=30)
        if r.ok: return Image.open(io.BytesIO(r.content))
        self.err.log_error(f"download {url} -> {r.status_code}"); return None

    def preprocess_image(self, image: Image.Image, size=(224, 224)) -> Image.Image:
        return image.convert("RGB").resize(size)
