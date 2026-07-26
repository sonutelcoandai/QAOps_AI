from orchestration.telecom_domain_router import TelecomDomainRouter

print(TelecomDomainRouter.get_agent("Validate billing charges"))

print(TelecomDomainRouter.get_agent("Validate service provisioning"))

print(TelecomDomainRouter.get_agent("Validate customer order flow"))

print(TelecomDomainRouter.get_agent("Validate TMF641 API"))
