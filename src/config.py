import json
import os

from dataclasses import asdict

from src.dto.config import Config


class ConfigManager:
    file_path = os.path.expanduser('~/.fosslight/config.json')

    @classmethod
    def save_config(cls, config: Config):
        dir_path = os.path.dirname(cls.file_path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        with open(cls.file_path, 'w') as f:
            json.dump(asdict(config), f, indent=4)

    @classmethod
    def read_config(cls) -> Config:
        try:
            with open(cls.file_path, 'r') as f:
                config = json.load(f)
                return Config(**config)
        except FileNotFoundError:
            return Config()
