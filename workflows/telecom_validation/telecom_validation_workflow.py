from execution.workflow_state import WorkflowState

from orchestration.agent_execution_engine import AgentExecutionEngine


class TelecomValidationWorkflow:
    @staticmethod
    def execute(telecom_input):

        state = WorkflowState()

        state.set_status("running")

        tmforum_result = AgentExecutionEngine.execute(
            "tmforum_agent", {"query": telecom_input}
        )

        state.complete_node("tmforum_agent")

        architect_result = AgentExecutionEngine.execute(
            "test_architect", {"input": tmforum_result}
        )

        state.complete_node("test_architect")

        state.set_status("completed")

        return {
            "workflow": "telecom_validation",
            "status": "completed",
            "workflow_state": {
                "status": state.status,
                "completed_nodes": state.completed_nodes,
                "failed_nodes": state.failed_nodes,
            },
            "validation_result": {
                "tmforum": tmforum_result,
                "architect_review": architect_result,
            },
        }
