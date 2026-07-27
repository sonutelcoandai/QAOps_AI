class OptimizationResult:
    def __init__(self, component, optimization, improved):

        self.component = component

        self.optimization = optimization

        self.improved = improved

    def to_dict(self):

        return {
            "component": self.component,
            "optimization": self.optimization,
            "improved": self.improved,
        }
