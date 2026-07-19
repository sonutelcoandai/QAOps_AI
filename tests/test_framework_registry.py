from agent_frameworks.framework_registry import FrameworkRegistry


class DummyFramework:
    pass


FrameworkRegistry.register("dummy", DummyFramework())

print(FrameworkRegistry.get_all())
