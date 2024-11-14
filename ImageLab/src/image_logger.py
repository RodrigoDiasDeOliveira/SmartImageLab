# src/image_logger.py
import logging
from datetime import datetime

class ImageLogger:
    def __init__(self, log_file='image_operations.log'):
        logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')

    def log_operation(self, operation, image_name, status):
        message = f"Operação: {operation}, Imagem: {image_name}, Status: {status}"
        logging.info(message)

    def log_upload(self, image_name, status="Sucesso"):
        self.log_operation("Upload", image_name, status)

    def log_download(self, image_name, status="Sucesso"):
        self.log_operation("Download", image_name, status)

    def log_processing(self, image_name, status="Sucesso"):
        self.log_operation("Processamento", image_name, status)
