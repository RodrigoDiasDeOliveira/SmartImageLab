# src/error_logger.py
import logging

class ErrorLogger:
    def __init__(self, log_file='errors.log'):
        logging.basicConfig(filename=log_file, level=logging.ERROR)

    def log_error(self, error):
        logging.error(str(error))

    def handle_api_error(self, response):
        if response.status_code != 200:
            error_message = f"API error: {response.status_code} - {response.text}"
            self.log_error(error_message)
            return False
        return True
