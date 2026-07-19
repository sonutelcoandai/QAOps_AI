from agent_frameworks.load_frameworks import load_frameworks

from orchestration.framework_execution_engine import FrameworkExecutionEngine

from orchestration.framework_manager import FrameworkManager

load_frameworks()

FrameworkManager.load()


def sample_workflow():

    return {"status": "workflow_executed"}


result = FrameworkExecutionEngine.execute(sample_workflow)

print(result)
