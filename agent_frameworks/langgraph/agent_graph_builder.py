from agent_frameworks.langgraph.execution_graph import ExecutionGraph

from agent_frameworks.langgraph.graph_node import GraphNode

from orchestration.agent_execution_engine import AgentExecutionEngine


class AgentGraphBuilder:
    @staticmethod
    def build(agent_names):

        graph = ExecutionGraph()

        for agent_name in agent_names:

            def create_node(current_agent):

                def execute(payload):

                    return AgentExecutionEngine.execute(current_agent, payload)

                return execute

            graph.add_node(GraphNode(agent_name, create_node(agent_name)))

        return graph
