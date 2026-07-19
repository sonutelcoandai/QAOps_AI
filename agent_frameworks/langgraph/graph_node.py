class GraphNode:
    def __init__(self, node_name, function):

        self.node_name = node_name
        self.function = function

    def execute(self, payload):

        state = payload.get("_workflow_state")

        try:
            result = self.function(payload)

            if state:
                state.complete_node(self.node_name)

            return result

        except Exception as error:
            if state:
                state.fail_node(self.node_name)

                state.add_error(self.node_name, error)

            raise
