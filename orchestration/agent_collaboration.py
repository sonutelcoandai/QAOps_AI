from orchestration.agent_execution_engine import AgentExecutionEngine


class AgentCollaboration:
    @staticmethod
    def execute_workflow(task):

        results = []

        qa_result = AgentExecutionEngine.execute("qa_engineer", task)

        results.append(qa_result)

        senior_result = AgentExecutionEngine.execute(
            "senior_qa_engineer",
            {
                "agent": qa_result["agent"],
            },
        )

        results.append(senior_result)

        architect_result = AgentExecutionEngine.execute(
            "test_architect",
            {
                "agent": senior_result["agent"],
            },
        )

        results.append(architect_result)

        return results


from orchestration.agent_execution_engine import AgentExecutionEngine


class AgentCollaboration:
    @staticmethod
    def execute_workflow(task):

        results = []

        qa_result = AgentExecutionEngine.execute("qa_engineer", task)

        results.append(qa_result)

        senior_result = AgentExecutionEngine.execute(
            "senior_qa_engineer", {"input": qa_result}
        )

        results.append(senior_result)

        architect_result = AgentExecutionEngine.execute(
            "test_architect", {"input": senior_result}
        )

        results.append(architect_result)

        return results
