from human_in_loop.hitl_policy_service import HITLPolicyService

print(HITLPolicyService.requires_approval("release_readiness"))

print(HITLPolicyService.requires_approval("telecom_validation"))

print(HITLPolicyService.requires_approval("requirement_to_test"))
