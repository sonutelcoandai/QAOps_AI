from orchestration.platform_bootstrap import PlatformBootstrap

from workflows.requirement_to_test.requirement_to_test_workflow import (
    RequirementToTestWorkflow,
)

PlatformBootstrap.initialize()

result = RequirementToTestWorkflow.execute("Generate TMF641 API Test Cases")

print(result)
