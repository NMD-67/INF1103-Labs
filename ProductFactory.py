from supplier import Supplier
from product import Product
from physical_product import PhyscialProduct
from digital_product import DigitalProduct
from service_product import ServiceProduct


class ProductFactory:
    _product_classes = {
        "physical": PhyscialProduct,
        "digital": DigitalProduct,
        "service": ServiceProduct,
    }

    @staticmethod
    def create(
        product_type: str,
        product_id: str,
        name: str,
        price: float,
        stock_qty: int,
        supplier: Supplier,
        additional_fields: dict = None,
    ) -> Product:
        if stock_qty <= 0:
            raise ValueError("Quantity must be greater than 0")
        if price <= 0:
            raise ValueError("Price must be greater than 0")

        product_class = ProductFactory._product_classes.get(product_type.lower())
        if product_class is None:
            raise ValueError(f"Unknown product type: {product_type}")

        return product_class(
            product_id=product_id,
            name=name,
            stock=stock_qty,
            price=price,
            supplier=supplier,
            **(additional_fields or {}),
        )
