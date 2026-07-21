# src/image_storage.py
import io

import oci
from PIL import Image

from .config_manager import ConfigManager
from .error_logger import ErrorLogger


class ImageStorage:
    """
    OCI Object Storage abstraction.
    """

    def __init__(
        self,
        client=None,
        bucket=None,
        namespace=None,
    ):

        self.err = ErrorLogger()

        #
        # Unit tests
        #
        if client is not None:
            self.client = client
            self.bucket = bucket or "test-bucket"
            self.namespace = namespace or "test-namespace"

            return

        #
        # Production
        #
        cfg = ConfigManager()

        self.bucket = cfg.get(
            "oracle_cloud",
            "bucket_name",
        )

        self.namespace = cfg.get(
            "oracle_cloud",
            "namespace",
        )

        profile = cfg.get(
            "oracle_cloud",
            "profile",
            default="DEFAULT",
        )

        oci_cfg = oci.config.from_file(profile_name=profile)

        self.client = oci.object_storage.ObjectStorageClient(oci_cfg)

    def upload_image(
        self,
        image: Image.Image,
        object_name: str,
        fmt="JPEG",
    ) -> bool:

        try:
            buffer = io.BytesIO()

            image.save(buffer, format=fmt)

            buffer.seek(0)

            self.client.put_object(
                self.namespace,
                self.bucket,
                object_name,
                buffer,
            )

            return True

        except Exception as exc:
            self.err.log_error(f"upload {object_name}: {exc}")

            return False

    def download_image(
        self,
        object_name: str,
    ):

        try:
            response = self.client.get_object(
                self.namespace,
                self.bucket,
                object_name,
            )

            return Image.open(io.BytesIO(response.data.content))

        except Exception as exc:
            self.err.log_error(f"download {object_name}: {exc}")

            return None
