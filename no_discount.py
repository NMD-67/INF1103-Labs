from discount_strategy import DiscountStrategy


class NoDiscount(DiscountStrategy):
    def apply(self, total):
        return total
