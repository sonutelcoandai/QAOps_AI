from workflows.base_workflow import BaseWorkflow


def test_workflow_import():
    workflow = BaseWorkflow()
    assert workflow is not None


print("BaseWorkflow Loaded")
