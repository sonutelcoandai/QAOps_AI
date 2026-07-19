from agent_frameworks.langgraph.execution_graph import ExecutionGraph
from agent_frameworks.langgraph.graph_node import GraphNode

from orchestration.agent_execution_engine import AgentExecutionEngine
from workflows.requirement_to_test.risk_router import RiskRouter


class WorkflowGraphBuilder:
    @staticmethod
    def build():

        graph = ExecutionGraph()

        def qa_node(payload):

            result = AgentExecutionEngine.execute("qa_engineer", payload)

            payload["qa_result"] = result

            return payload

        def senior_node(payload):

            result = AgentExecutionEngine.execute("senior_qa_engineer", payload)

            payload["senior_result"] = result

            return payload

        def architect_node(payload):

            risk = RiskRouter.evaluate(payload)

            if risk != "high":
                payload["architect_result"] = {
                    "agent": "test_architect",
                    "review": "Skipped",
                    "summary": "Architect review not required",
                }

                return payload

            result = AgentExecutionEngine.execute("test_architect", payload)

            payload["architect_result"] = result

            return payload

        graph.add_node(GraphNode("qa_engineer", qa_node))

        graph.add_node(GraphNode("senior_qa_engineer", senior_node))

        graph.add_node(GraphNode("test_architect", architect_node))

        return graph
