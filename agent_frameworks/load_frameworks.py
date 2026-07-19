from agent_frameworks.framework_registry import FrameworkRegistry

from agent_frameworks.langgraph.langgraph_framework import LangGraphFramework


def load_frameworks():

    FrameworkRegistry.register("langgraph", LangGraphFramework())
