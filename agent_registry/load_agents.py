from agent_registry.agent_registry import AgentRegistry

from agents.engineering.qa_engineer.qa_engineer_agent import QAEngineerAgent

from agents.engineering.senior_qa_engineer.senior_qa_engineer_agent import (
    SeniorQAEngineerAgent,
)

from agents.leadership.test_architect.test_architect_agent import TestArchitectAgent
from agents.specialized.tmforum_agent.tmforum_agent import TMForumAgent

from agents.specialized.billing_agent.billing_agent import BillingAgent
from agents.specialized.oss_agent.oss_agent import OSSAgent
from agents.specialized.bss_agent.bss_agent import BSSAgent
from agents.specialized.telecom_architect_agent.telecom_architect_agent import (
    TelecomArchitectAgent,
)


def load_agents():

    AgentRegistry.register("qa_engineer", QAEngineerAgent())

    AgentRegistry.register("senior_qa_engineer", SeniorQAEngineerAgent())

    AgentRegistry.register("test_architect", TestArchitectAgent())
    AgentRegistry.register("tmforum_agent", TMForumAgent())
    AgentRegistry.register("billing_agent", BillingAgent())
    AgentRegistry.register("oss_agent", OSSAgent())
    AgentRegistry.register("bss_agent", BSSAgent())
    AgentRegistry.register("telecom_architect_agent", TelecomArchitectAgent())
