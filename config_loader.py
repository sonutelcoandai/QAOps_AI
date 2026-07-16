"""
Central Configuration Loader
QAOps-AI
"""

import yaml
from pathlib import Path


class ConfigLoader:
    @staticmethod
    def load_config(file_name: str):

        config_path = Path("config") / file_name

        if not config_path.exists():
            raise FileNotFoundError(f"Config file not found: {config_path}")

        with open(config_path, "r") as file:
            return yaml.safe_load(file)
