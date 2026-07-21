# src/error_logger.py
import logging


class ErrorLogger:
    def __init__(self, log_file="logs/errors.log"):
        self.logger = logging.getLogger("errors")
        if not self.logger.handlers:
            h = logging.FileHandler(log_file)
            h.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
            self.logger.addHandler(h)
            self.logger.setLevel(logging.ERROR)

    def log_error(self, error):
        self.logger.error(str(error))

    def handle_api_error(self, response):
        if getattr(response, "status_code", 200) != 200:
            self.log_error(f"API {response.status_code}: {response.text}")
            return False
        return True
