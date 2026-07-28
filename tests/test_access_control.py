from security.access_control_service import AccessControlService

print(AccessControlService.authorize("qa_manager", "approve_workflow"))

print(AccessControlService.authorize("qa_lead", "approve_release"))
