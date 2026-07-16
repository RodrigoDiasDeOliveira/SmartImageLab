# src/config_manager.py
import os
import yaml


class ConfigManager:
    _instance = None

    def __new__(cls, config_path="config/config.yaml"):

        if cls._instance is None:

            cls._instance = super().__new__(cls)

            cls._instance.config = {}

            if os.path.exists(config_path):
                cls._instance._load(config_path)

        return cls._instance

    def _load(self, path):

        with open(path, "r", encoding="utf-8") as f:
            self.config = yaml.safe_load(f) or {}

    def get(self, *keys, default=None):

        node = self.config

        for key in keys:

            if isinstance(node, dict) and key in node:
                node = node[key]
            else:
                return default

        return node

    def get_api_key(self, provider):

        return self.get(
            "api_keys",
            provider,
            default=None,
        )