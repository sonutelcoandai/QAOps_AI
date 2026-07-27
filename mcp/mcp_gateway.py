from mcp.routing.request_router import RequestRouter

from event_bus.events.mcp_events import MCPActionEvent

from event_bus.publishers.mcp_event_publisher import MCPEventPublisher


class MCPGateway:
    @staticmethod
    def execute(request):

        result = RequestRouter.route(request)

        action = request.get("action")

        MCPEventPublisher.publish(MCPActionEvent(action, result))

        return result
