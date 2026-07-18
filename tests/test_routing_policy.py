from pathlib import Path
import sys
from model_orchestration.policies.routing_policy import RoutingPolicy

ROOT_DIR = Path(__file__).resolve().parent.parent.parent

sys.path.insert(0, str(ROOT_DIR))


RoutingPolicy.load()

print("Strategy:", RoutingPolicy.get_strategy())

print("Tasks:", RoutingPolicy.get_tasks())

print("Agents:", RoutingPolicy.get_agents())

print("Domains:", RoutingPolicy.get_domains())
