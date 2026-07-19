from agent_frameworks.base_framework import BaseFramework
from agent_frameworks.base_framework import BaseFramework

from agent_frameworks.langgraph.langgraph_agent_runner import LangGraphAgentRunner


class LangGraphFramework(BaseFramework):
    def create_agent(self, agent):
        return agent

    def create_workflow(self, workflow):
        return workflow

    def execute_agent(self, agent_name, task):
        return LangGraphAgentRunner.execute_agent(agent_name, task)

    def execute(self, workflow):
        return workflow()
