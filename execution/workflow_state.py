from datetime import datetime


class WorkflowState:
    def __init__(self):

        self.status = "created"

        self.started_at = datetime.now().isoformat()

        self.completed_nodes = []

        self.failed_nodes = []

        self.metadata = {}

        self.retry_count = {}

        self.error_details = {}

    def increment_retry(self, node_name):

        current = self.retry_count.get(node_name, 0)

        self.retry_count[node_name] = current + 1

    def add_error(self, node_name, error):

        self.error_details[node_name] = str(error)

    def complete_node(self, node_name):

        self.completed_nodes.append(node_name)

    def fail_node(self, node_name):

        self.failed_nodes.append(node_name)

    def set_status(self, status):

        self.status = status

    def add_metadata(self, key, value):

        self.metadata[key] = value
