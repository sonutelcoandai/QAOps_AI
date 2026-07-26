from execution.workflow_state import WorkflowState

from orchestration.agent_execution_engine import AgentExecutionEngine


class BillingValidationWorkflow:
    @staticmethod
    def execute(billing_input):

        state = WorkflowState()

        state.set_status("running")

        billing_result = AgentExecutionEngine.execute(
            "billing_agent", {"query": billing_input}
        )

        state.complete_node("billing_agent")

        architect_result = AgentExecutionEngine.execute(
            "telecom_architect_agent", {"query": billing_input}
        )

        state.complete_node("telecom_architect_agent")

        state.set_status("completed")

        return {
            "workflow": "billing_validation",
            "status": "completed",
            "workflow_state": {
                "status": state.status,
                "completed_nodes": state.completed_nodes,
                "failed_nodes": state.failed_nodes,
            },
            "validation_result": {
                "billing": billing_result,
                "architect_review": architect_result,
            },
        }
