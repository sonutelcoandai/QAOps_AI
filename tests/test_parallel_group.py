from agent_frameworks.langgraph.graph_node import GraphNode

from agent_frameworks.langgraph.parallel_group import ParallelGroup


def coverage_check(payload):

    return {"coverage": "passed"}


def risk_check(payload):

    return {"risk": "low"}


group = ParallelGroup(
    [GraphNode("coverage", coverage_check), GraphNode("risk", risk_check)]
)

result = group.execute({})

print(result)
