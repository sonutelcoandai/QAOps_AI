from execution.base_execution import BaseExecution

from execution.ui.locator_manager import LocatorManager

from execution.ui.ui_validator import UIValidator

from execution.ui.ui_result import UIResult


class UIExecution(BaseExecution):
    def __init__(self):

        self.results = []

    def execute_test(self, test_case):

        locator = LocatorManager.get_locator(test_case.get("locator"))

        UIValidator.validate_element(locator)

        result = UIResult(status="passed", page=test_case.get("page"), locator=locator)

        self.results.append(result)

        return result.to_dict()

    def collect_results(self):

        return [result.to_dict() for result in self.results]
