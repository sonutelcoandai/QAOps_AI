from pathlib import Path
import sys
from model_orchestration.policies.routing_policy import RoutingPolicy

from model_orchestration.policies.policy_resolver import PolicyResolver

ROOT_DIR = Path(__file__).resolve().parent.parent.parent

sys.path.insert(0, str(ROOT_DIR))

RoutingPolicy.load()

print(PolicyResolver.resolve_task_model("test_case_generation"))

print(PolicyResolver.resolve_agent_model("automation_engineer"))

print(PolicyResolver.resolve_domain_model("telecom"))
