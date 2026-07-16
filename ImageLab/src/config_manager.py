import os, yaml
from dotenv import load_dotenv

load_dotenv()

class ConfigManager:
    _instance = None
    def __new__(cls, config_path="config/config.yaml"):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._load(config_path)
        return cls._instance

    def _load(self, path):
        with open(path, "r", encoding="utf-8") as f:
            raw = f.read()
        # expansão de ${VAR}
        raw = os.path.expandvars(raw)
        self.config = yaml.safe_load(raw)

    def get_api_key(self, service):
        return self.config.get("api_keys", {}).get(service) or os.getenv(f"{service.upper()}_API_KEY")

    def get(self, *keys, default=None):
        node = self.config
        for k in keys:
            if not isinstance(node, dict): return default
            node = node.get(k, default)
        return node
