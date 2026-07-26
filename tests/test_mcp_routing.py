from mcp.routing.request_router import RequestRouter

print(RequestRouter.route({"action": "create_ticket", "summary": "TMF641 defect"}))

print(RequestRouter.route({"action": "create_pr", "branch": "feature/tmf641"}))

print(RequestRouter.route({"action": "run_collection", "collection": "TMF641"}))
