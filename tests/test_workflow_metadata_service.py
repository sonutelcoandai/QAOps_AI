from workflows.registry.workflow_manager import WorkflowManager

from workflows.registry.workflow_metadata_service import WorkflowMetadataService

WorkflowManager.load()

print(WorkflowMetadataService.get_metadata("requirement_to_test"))
