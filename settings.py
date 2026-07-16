"""
Environment Settings
"""

import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_NAME = os.getenv("APP_NAME", "QAOps-AI")

    ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

    DEFAULT_PROVIDER = os.getenv("DEFAULT_AI_PROVIDER", "ollama")
