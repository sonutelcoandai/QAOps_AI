from orchestration.agent_collaboration import AgentCollaboration


class RequirementToTestWorkflow:
    @staticmethod
    def execute(requirement):

        workflow_result = AgentCollaboration.execute_workflow(
            {"requirement": requirement}
        )

        return {
            "workflow": "requirement_to_test",
            "requirement": requirement,
            "status": "completed",
            "agents_executed": ["qa_engineer", "senior_qa_engineer", "test_architect"],
            "final_review": workflow_result[-1],
        }
