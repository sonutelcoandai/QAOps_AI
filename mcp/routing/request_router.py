from mcp.routing.action_router import ActionRouter

from mcp.load_clients import get_client


class RequestRouter:
    @staticmethod
    def route(request):

        action = request.get("action")

        target = ActionRouter.get_target(action)

        if target is None:
            raise ValueError(f"No route found for action '{action}'")

        client = get_client(target)

        return client.execute(request)
