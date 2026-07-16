from unittest.mock import MagicMock, patch
from src.image_generator import ImageGenerator

@patch("src.image_generator.OpenAI")
def test_generate_returns_url(mock_openai: MagicMock) -> None:
    mock_openai.return_value.images.generate.return_value = MagicMock(
        data=[MagicMock(url="https://example.com/img.png")]
    )
    url = ImageGenerator(api_key="test").generate("um gato")
    assert url.startswith("https://")
