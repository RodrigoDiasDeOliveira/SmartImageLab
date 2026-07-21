from pathlib import Path

from src.image_validator import ImageValidator


def test_valid_image(sample_image: Path) -> None:
    assert ImageValidator().is_valid(sample_image) is True


def test_missing_file(tmp_path: Path) -> None:
    assert ImageValidator().is_valid(tmp_path / "nope.png") is False


def test_corrupt_file(tmp_path: Path) -> None:
    f = tmp_path / "bad.png"
    f.write_bytes(b"not-an-image")
    assert ImageValidator().is_valid(f) is False
