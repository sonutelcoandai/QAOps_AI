from observability.operations_dashboard import OperationsDashboard

from observability.operations_report import OperationsReport

report = OperationsReport(OperationsDashboard.generate())

print(report.to_dict())
