# src/image_identifier.py
import torch

class ImageIdentifier:
    def __init__(self, model_path='yolov5s.pt'):
        self.model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path)

    def identify(self, image):
        results = self.model(image)
        return results.pandas().xyxy[0]  # Retorna coordenadas e rótulos.
