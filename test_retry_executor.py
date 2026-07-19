from execution.retry_executor import RetryExecutor

from execution.workflow_state import WorkflowState

state = WorkflowState()

counter = {"attempts": 0}


def unstable_function(payload):

    counter["attempts"] += 1

    if counter["attempts"] < 3:
        raise Exception("Temporary Failure")

    return {"status": "success"}


result = RetryExecutor.execute(unstable_function, {}, state, "test_node")

print(result)

print(state.retry_count)
