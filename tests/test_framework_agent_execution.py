from orchestration.platform_bootstrap import PlatformBootstrap

from agent_frameworks.framework_factory import FrameworkFactory

PlatformBootstrap.initialize()

framework = FrameworkFactory.get_framework("langgraph")

result = framework.execute_agent(
    "qa_engineer", {"requirement": "Generate TMF641 API test cases"}
)

print(result)
