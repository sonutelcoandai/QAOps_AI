from agent_registry.load_agents import load_agents


class AgentBootstrap:
    @staticmethod
    def initialize():

        print("\nInitializing Agent Layer...\n")

        load_agents()

        print("Agents Loaded")

        print("\nAgent Layer Ready\n")
