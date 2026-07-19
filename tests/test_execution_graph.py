from agent_frameworks.langgraph.execution_graph import ExecutionGraph

from agent_frameworks.langgraph.graph_node import GraphNode


def step1(payload):

    payload["step1"] = True

    return payload


def step2(payload):

    payload["step2"] = True

    return payload


graph = ExecutionGraph()

graph.add_node(GraphNode("step1", step1))

graph.add_node(GraphNode("step2", step2))

result = graph.execute({})

print(result)
