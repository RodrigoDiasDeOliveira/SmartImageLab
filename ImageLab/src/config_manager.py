# src/config_manager.py
import yaml

class ConfigManager:
    def __init__(self, config_path='config/config.yaml'):
        self.config = self.load_config(config_path)

    def load_config(self, path):
        with open(path, 'r') as file:
            return yaml.safe_load(file)

    def get_api_key(self, service):
        return self.config.get('api_keys', {}).get(service)

    def get_config(self, key):
        return self.config.get(key)
