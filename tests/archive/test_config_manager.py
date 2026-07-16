from orchestration.config_manager import ConfigManager

ConfigManager.initialize()

print(ConfigManager.get_platform())
