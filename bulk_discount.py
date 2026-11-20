from discount_strategy import DiscountStrategy


class BulkDiscount(DiscountStrategy):
    def __init__(self, threshold: int, amt: float):
        super().__init__()
        self.threshold = threshold
        self.amt = amt

    def apply(self, total):
        if total >= self.threshold:
            total -= self.amt

        return total
