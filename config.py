import json

from dataclasses import asdict

from dto.config import Config


class ConfigManager:
    file_path = '~/.fosslight/config.json'

    def save_config(self, config: Config):
        with open(self.file_path, 'w') as f:
            json.dump(asdict(config), f, indent=4)

    def read_config(self) -> Config:
        with open(self.file_path, 'r') as f:
            config = json.load(f)
            return Config(**config)
