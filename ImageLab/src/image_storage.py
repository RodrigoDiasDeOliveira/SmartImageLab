import io, oci
from PIL import Image
from .config_manager import ConfigManager
from .error_logger import ErrorLogger

class ImageStorage:
    def __init__(self):
        cfg = ConfigManager()
        self.bucket = cfg.get("oracle_cloud", "bucket_name")
        self.namespace = cfg.get("oracle_cloud", "namespace")
        profile = cfg.get("oracle_cloud", "profile", default="DEFAULT")
        oci_cfg = oci.config.from_file(profile_name=profile)
        self.client = oci.object_storage.ObjectStorageClient(oci_cfg)
        self.err = ErrorLogger()

    def upload_image(self, image: Image.Image, object_name: str, fmt="JPEG"):
        try:
            buf = io.BytesIO(); image.save(buf, format=fmt); buf.seek(0)
            self.client.put_object(self.namespace, self.bucket, object_name, buf)
            return True
        except Exception as e:
            self.err.log_error(f"upload {object_name}: {e}"); return False

    def download_image(self, object_name: str) -> Image.Image | None:
        try:
            r = self.client.get_object(self.namespace, self.bucket, object_name)
            return Image.open(io.BytesIO(r.data.content))
        except Exception as e:
            self.err.log_error(f"download {object_name}: {e}"); return None
