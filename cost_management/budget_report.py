class BudgetReport:
    def __init__(self, budget, current_cost, remaining):

        self.budget = budget

        self.current_cost = current_cost

        self.remaining = remaining

    def to_dict(self):

        return {
            "budget": self.budget,
            "current_cost": self.current_cost,
            "remaining": self.remaining,
        }
