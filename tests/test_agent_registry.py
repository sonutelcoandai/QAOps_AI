from agent_registry.agent_registry import AgentRegistry


class DummyAgent:
    pass


AgentRegistry.register("dummy", DummyAgent())

print(AgentRegistry.get_all())
