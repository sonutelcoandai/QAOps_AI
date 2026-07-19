from agent_frameworks.langgraph.execution_graph import ExecutionGraph

from agent_frameworks.langgraph.graph_node import GraphNode

from orchestration.agent_execution_engine import AgentExecutionEngine


class BlueprintExecutionBuilder:
    @staticmethod
    def build(blueprint):

        graph = ExecutionGraph()

        for agent_name in blueprint.agents:

            def create_node(current_agent):

                def execute(payload):

                    result = AgentExecutionEngine.execute(current_agent, payload)

                    payload[f"{current_agent}_result"] = result

                    return payload

                return execute

            graph.add_node(GraphNode(agent_name, create_node(agent_name)))

        return graph
