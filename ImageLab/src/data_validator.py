import os
from PIL import Image
class DataValidator:
    def validate_image(self, img):
        return isinstance(img, Image.Image) and img.size[0] > 0 and img.size[1] > 0
    def validate_model_path(self, model_path):
        if not isinstance(model_path, str) or not model_path.strip(): return False
        # aceita alias (ex: 'imagenet', 'yolov5s') OU arquivo existente
        if model_path in {"imagenet", "yolov5s", "yolov5m", "yolov5l"}: return True
        if not os.path.exists(model_path): return False
        return os.path.splitext(model_path)[1].lower() in {".h5", ".pt", ".pth", ".onnx"}
