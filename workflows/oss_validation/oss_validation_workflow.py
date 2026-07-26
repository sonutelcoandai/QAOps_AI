from execution.workflow_state import WorkflowState

from orchestration.agent_execution_engine import AgentExecutionEngine


class OSSValidationWorkflow:
    @staticmethod
    def execute(oss_input):

        state = WorkflowState()

        state.set_status("running")

        oss_result = AgentExecutionEngine.execute("oss_agent", {"query": oss_input})

        state.complete_node("oss_agent")

        architect_result = AgentExecutionEngine.execute(
            "telecom_architect_agent", {"query": oss_input}
        )

        state.complete_node("telecom_architect_agent")

        state.set_status("completed")

        return {
            "workflow": "oss_validation",
            "status": "completed",
            "workflow_state": {
                "status": state.status,
                "completed_nodes": state.completed_nodes,
                "failed_nodes": state.failed_nodes,
            },
            "validation_result": {
                "oss": oss_result,
                "architect_review": architect_result,
            },
        }
