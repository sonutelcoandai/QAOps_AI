from agent_registry.agent_registry import AgentRegistry

from agents.engineering.qa_engineer.qa_engineer_agent import QAEngineerAgent

from agents.engineering.senior_qa_engineer.senior_qa_engineer_agent import (
    SeniorQAEngineerAgent,
)

from agents.leadership.test_architect.test_architect_agent import TestArchitectAgent


def load_agents():

    AgentRegistry.register("qa_engineer", QAEngineerAgent())

    AgentRegistry.register("senior_qa_engineer", SeniorQAEngineerAgent())

    AgentRegistry.register("test_architect", TestArchitectAgent())
