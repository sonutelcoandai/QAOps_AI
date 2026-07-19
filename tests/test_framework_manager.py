from orchestration.framework_manager import FrameworkManager

FrameworkManager.load()

print(FrameworkManager.get_default_framework())
