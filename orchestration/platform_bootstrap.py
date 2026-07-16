from orchestration.config_manager import ConfigManager

from orchestration.provider_manager import ProviderManager

from feature_flags.feature_manager import FeatureManager

from ai_providers.load_providers import load_providers


class PlatformBootstrap:
    @staticmethod
    def initialize():

        print("\nInitializing QAOps-AI...\n")

        ConfigManager.initialize()

        print("✓ Config Manager Loaded")

        FeatureManager.load()

        print("✓ Feature Manager Loaded")

        ProviderManager.load()

        print("✓ Provider Manager Loaded")

        load_providers()

        print("✓ Providers Loaded")

        print("\nQAOps-AI Ready\n")
