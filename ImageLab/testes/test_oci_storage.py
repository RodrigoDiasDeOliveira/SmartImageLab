from unittest.mock import MagicMock

from PIL import Image
from src.image_storage import ImageStorage


def test_upload_image():

    client = MagicMock()

    storage = ImageStorage(client=client)

    image = Image.new("RGB", (100, 100))

    result = storage.upload_image(image, "test.jpg")

    assert result is True

    client.put_object.assert_called_once()


def test_download_image():

    client = MagicMock()

    image = Image.new("RGB", (50, 50))

    import io

    buffer = io.BytesIO()
    image.save(buffer, format="JPEG")
    buffer.seek(0)

    response = MagicMock()
    response.data.content = buffer.read()

    client.get_object.return_value = response

    storage = ImageStorage(client=client)

    downloaded = storage.download_image("test.jpg")

    assert downloaded is not None
    assert downloaded.size == (50, 50)
