import sys
from pathlib import Path

import pytest
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "ImageLab"))


@pytest.fixture
def sample_image(tmp_path: Path) -> Path:
    p = tmp_path / "sample.png"
    Image.new("RGB", (256, 256), (128, 64, 200)).save(p)
    return p
