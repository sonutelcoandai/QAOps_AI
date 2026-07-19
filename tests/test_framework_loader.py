from agent_frameworks.framework_registry import FrameworkRegistry

from agent_frameworks.load_frameworks import load_frameworks

load_frameworks()

print(FrameworkRegistry.get_all())
