from execution.workflow_state import WorkflowState

from orchestration.agent_execution_engine import AgentExecutionEngine

from execution.api.api_execution import APIExecution


class APIValidationWorkflow:
    @staticmethod
    def execute(api_input):

        state = WorkflowState()

        state.set_status("running")

        tmf_result = AgentExecutionEngine.execute("tmforum_agent", {"query": api_input})

        state.complete_node("tmforum_agent")

        executor = APIExecution()

        execution_result = executor.execute_test(
            {
                "endpoint": "/tmf641/serviceOrder",
                "method": "POST",
                "payload": {"request": api_input},
            }
        )

        state.complete_node("api_execution")

        state.set_status("completed")

        return {
            "workflow": "api_validation",
            "status": "completed",
            "workflow_state": {
                "status": state.status,
                "completed_nodes": state.completed_nodes,
                "failed_nodes": state.failed_nodes,
            },
            "tmforum_analysis": tmf_result,
            "execution_result": execution_result,
        }
