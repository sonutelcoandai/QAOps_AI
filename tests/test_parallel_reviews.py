from agent_frameworks.langgraph.graph_node import GraphNode

from agent_frameworks.langgraph.parallel_group import ParallelGroup

from workflows.requirement_to_test.review_nodes import ReviewNodes

group = ParallelGroup(
    [
        GraphNode("coverage", ReviewNodes.coverage_review),
        GraphNode("risk", ReviewNodes.risk_review),
    ]
)

result = group.execute({"requirement": "Generate TMF641 API test cases"})

print(result)
