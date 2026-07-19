from orchestration.platform_bootstrap import PlatformBootstrap

from orchestration.agent_collaboration import AgentCollaboration

PlatformBootstrap.initialize()

result = AgentCollaboration.execute_workflow(
    {"requirement": "Generate TMF641 API test cases"}
)

print(result)
