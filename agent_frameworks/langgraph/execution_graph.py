class ExecutionGraph:
    def __init__(self):

        self.nodes = []

    def add_node(self, node):

        self.nodes.append(node)

    def execute(self, payload):

        current_payload = payload

        for node in self.nodes:
            current_payload = node.execute(current_payload)

        return current_payload
