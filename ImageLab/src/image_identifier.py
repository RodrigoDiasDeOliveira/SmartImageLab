import torch
from PIL import Image

class ImageIdentifier:
    def __init__(self, model_name="yolov5s"):
        self.model = torch.hub.load("ultralytics/yolov5", model_name, pretrained=True)
        self.model.eval()

    def identify(self, image: Image.Image):
        results = self.model(image)
        return results.pandas().xyxy[0].to_dict(orient="records")
