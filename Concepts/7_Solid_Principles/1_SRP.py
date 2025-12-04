class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price


class Order:
    def __init__(self, products: list[Product]):
        self.products = products


class OrderCalculator:
    def total_calculator(self, order: Order) -> float:
        total = sum(product.price for product in order.products)
        return total


class OrderInvoice:
    def print_invoice(self, order: Order, total: float) -> list:
        print("Invoices: ")
        for product in order.products:
            print("Product Name: ", product.name, "Product Price: ", product.price)
        print("Total: ", total)
        product_name_list = [product.name for product in order.products]
        product_price_list = [product.price for product in order.products]
        return {
            "Product Name": product_name_list,
            "Product Price": product_price_list,
            "total": total,
        }


# Example run
products = [
    Product(name="Laptop", price=27000),
    Product(name="Mouse", price=1000),
    Product(name="Keyboard", price=2500),
]

orders = Order(products=products)
calculator = OrderCalculator()
printer = OrderInvoice()

print(
    printer.print_invoice(order=orders, total=calculator.total_calculator(order=orders))
)
