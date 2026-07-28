from observability.operations_dashboard import OperationsDashboard


class OperationsCommandCenter:
    @staticmethod
    def generate():

        return {"operations": OperationsDashboard.generate()}
