from discount_strategy import DiscountStrategy


class PercentageDiscount(DiscountStrategy):
    def __init__(self, discount_percent: float):
        super().__init__()
        self.discount = discount_percent

    def apply(self, total):
        return total - (total * self.discount / 100)
