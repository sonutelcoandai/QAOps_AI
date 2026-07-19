from execution.workflow_state import (
    WorkflowState,
)

from orchestration.framework_execution_engine import (
    FrameworkExecutionEngine,
)

from workflows.requirement_to_test.workflow_graph_builder import (
    WorkflowGraphBuilder,
)


class RequirementToTestWorkflow:
    @staticmethod
    def execute(requirement):

        graph = WorkflowGraphBuilder.build()

        def workflow():

            state = WorkflowState()

            state.set_status("running")

            result = graph.execute(
                {
                    "requirement": requirement,
                    "_workflow_state": state,
                }
            )

            state.set_status("completed")

            return {
                "workflow": "requirement_to_test",
                "requirement": requirement,
                "status": "completed",
                "agents_executed": [
                    "qa_engineer",
                    "senior_qa_engineer",
                    "test_architect",
                ],
                "workflow_state": {
                    "status": state.status,
                    "completed_nodes": state.completed_nodes,
                    "failed_nodes": state.failed_nodes,
                    "retry_count": state.retry_count,
                    "error_details": state.error_details,
                },
                "final_review": result["architect_result"],
            }

        return FrameworkExecutionEngine.execute(workflow)
