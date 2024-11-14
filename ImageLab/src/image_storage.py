# src/image_storage.py
import oci
from config_manager import ConfigManager

class ImageStorage:
    def __init__(self):
        self.config = ConfigManager()
        self.client = oci.object_storage.ObjectStorageClient({})

    def upload_image(self, image, image_name):
        # Implementação de upload usando OCI.

    def download_image(self, image_id):
        # Implementação de download usando OCI.
