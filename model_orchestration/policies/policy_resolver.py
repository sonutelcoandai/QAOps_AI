from model_orchestration.policies.routing_policy import RoutingPolicy


class PolicyResolver:
    @staticmethod
    def resolve_task_model(task_name):

        tasks = RoutingPolicy.get_tasks()

        task = tasks.get(task_name)

        if task:
            return task["model"]

        return None

    @staticmethod
    def resolve_agent_model(agent_name):

        agents = RoutingPolicy.get_agents()

        agent = agents.get(agent_name)

        if agent:
            return agent["model"]

        return None

    @staticmethod
    def resolve_domain_model(domain_name):

        domains = RoutingPolicy.get_domains()

        domain = domains.get(domain_name)

        if domain:
            return domain["model"]

        return None
