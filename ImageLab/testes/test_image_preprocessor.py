from pathlib import Path
from src.image_preprocessor import ImagePreprocessor

def test_resize(sample_image: Path) -> None:
    tensor = ImagePreprocessor(size=(224, 224)).to_tensor(sample_image)
    assert tuple(tensor.shape) == (3, 224, 224)
