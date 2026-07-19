class ParallelGroup:
    def __init__(self, nodes):

        self.nodes = nodes

    def execute(self, payload):

        results = {}

        for node in self.nodes:
            results[node.node_name] = node.execute(dict(payload))

        return results
