from order_line import OrderLine
from product import Product
from discount_strategy import DiscountStrategy
from no_discount import NoDiscount


class Order:
    def __init__(self, order_id: str, discount_strategy: DiscountStrategy = None):
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []
        if discount_strategy is None:
            discount_strategy = NoDiscount
        self.discount: DiscountStrategy = discount_strategy

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.order_lines.append(order_line)

    def remove_order_line(self, index: int) -> None:
        if index >= len(self.order_lines):
            return
        self.order_lines.pop(index)

    def display_order_line(self) -> None:
        print("================")
        print(f"Order Line for {self.order_id}")
        print("================")
        for order_line in self.order_lines:
            print(
                f"{order_line.product.name}: \tx{order_line.quantity}\t ${order_line.calculate_subtotal()}"
            )
        if len(self.order_lines) < 1:
            print("Order Is empty")

    def set_discount(self, discount_strategy: DiscountStrategy):
        self.discount = discount_strategy

    def calculate_total(self) -> float:
        total = 0
        for order_line in self.order_lines:
            total += order_line.calculate_subtotal()
        return self.discount.apply(total)
