class RoutingNode:
    def __init__(self, router_function):

        self.router_function = router_function

    def evaluate(self, payload):

        return self.router_function(payload)
