# src/image_logger.py
import logging


class ImageLogger:
    def __init__(self, log_file="logs/image_operations.log"):
        self.logger = logging.getLogger("image_ops")
        if not self.logger.handlers:
            h = logging.FileHandler(log_file)
            h.setFormatter(logging.Formatter("%(asctime)s %(message)s"))
            self.logger.addHandler(h)
            self.logger.setLevel(logging.INFO)

    def log_operation(self, op, name, status="Sucesso"):
        self.logger.info(f"{op} | {name} | {status}")

    def log_upload(self, n, s="Sucesso"):
        self.log_operation("Upload", n, s)

    def log_download(self, n, s="Sucesso"):
        self.log_operation("Download", n, s)

    def log_processing(self, n, s="Sucesso"):
        self.log_operation("Processamento", n, s)
