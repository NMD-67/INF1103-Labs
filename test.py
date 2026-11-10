from supplier import Supplier
from product import Product
from physical_product import PhyscialProduct
from digital_product import DigitalProduct
from inventory import Inventory
from order import Order

test_supplier = Supplier("test_supplier_id", "test_supplier_name", "test@supplier.com")
test_physical_product = PhyscialProduct(
    100, "test_product_name", 67, 67.67, 69, test_supplier
)
test_digital_product = DigitalProduct(
    101, "test_digital_name", 23, 45, 67, test_supplier
)
test_inventory = Inventory()
test_inventory_B = Inventory()
test_order = Order("test_order_id")
test_order_B = Order("test_order_B_id")


def show_product_details(product: Product) -> None:
    product.display_information()
    product.get_fulfilment_info()


def test_5():
    test_inventory.add_product(test_physical_product)
    test_inventory.add_product(test_digital_product)
    test_inventory.display_all()


def test_4():
    show_product_details(test_physical_product)
    show_product_details(test_digital_product)


def test_3():
    test_order.add_order_line(test_physical_product, 45)
    test_order.add_order_line(test_digital_product, 67)
    test_order.display_order_line()
    print(f"Order Total: ${test_order.calculate_total()}")
    test_order_B.add_order_line(test_physical_product, 89)
    print(
        f"Original Product is OrderLine Product: {test_physical_product is test_order.order_lines[0].product}"
    )
    print(
        f"OrderLine_B Product is OrderLine Product: {test_order_B.order_lines[0].product is test_order.order_lines[0].product}"
    )
    test_order_B.remove_order_line(0)
    test_order_B.display_order_line()


def test_2():
    test_inventory.add_product(test_physical_product)
    test_inventory.remove_product(test_physical_product.product_id)
    test_physical_product.display_information()
    test_inventory_B.add_product(test_physical_product)


def test_1():
    test_physical_product.supplier.display_information()
    test_digital_product.supplier.display_information()


test_5()
