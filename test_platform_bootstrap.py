from pathlib import Path
import sys
from orchestration.platform_bootstrap import PlatformBootstrap

ROOT_DIR = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(ROOT_DIR))

PlatformBootstrap.initialize()
