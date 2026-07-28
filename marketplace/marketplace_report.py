class MarketplaceReport:
    def __init__(self, marketplace):

        self.marketplace = marketplace

    def to_dict(self):

        return {"marketplace": self.marketplace}
