from integrations.integration_lifecycle_service import IntegrationLifecycleService

IntegrationLifecycleService.activate("jira")

print(IntegrationLifecycleService.get_status("jira"))

IntegrationLifecycleService.deprecate("jira")

print(IntegrationLifecycleService.get_status("jira"))

IntegrationLifecycleService.retire("jira")

print(IntegrationLifecycleService.get_status("jira"))
