from pathlib import Path
import sys
from feature_flags.feature_manager import FeatureManager

ROOT_DIR = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(ROOT_DIR))

FeatureManager.load()

print("MCP:", FeatureManager.is_enabled("mcp"))

print("Analytics:", FeatureManager.is_enabled("analytics"))

print("Marketplace:", FeatureManager.is_enabled("marketplace"))

print("Non-existing feature:", FeatureManager.is_enabled("non_existing_feature"))
