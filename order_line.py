from product import Product


class OrderLine:
    def __init__(self, product: Product, qty: int):
        self.product: Product = product
        if qty <= 0:
            raise ValueError("Quantity must be more than 0")
        self.quantity: int = qty

    def calculate_subtotal(self) -> float:
        return self.product.price * self.quantity
