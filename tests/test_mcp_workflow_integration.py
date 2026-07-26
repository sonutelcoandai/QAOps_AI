from workflows.mcp_workflow_service import MCPWorkflowService

print(MCPWorkflowService.create_defect("TMF641 billing issue"))

print(MCPWorkflowService.create_pull_request("TMF641 Fix"))

print(MCPWorkflowService.create_documentation("TMF641 Validation Guide"))

print(MCPWorkflowService.run_api_tests("TMF641 Collection"))
