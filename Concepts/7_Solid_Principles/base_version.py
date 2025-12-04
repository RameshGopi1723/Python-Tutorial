# order_system.py

class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

class Order:
    def __init__(self, products: list):
        self.products = products

    def calculate_total(self) -> float:
        total = 0
        for product in self.products:
            total += product.price
        return total
    
    def print_invoice(self, order: Order, total: float):
        print("📄 Invoice")
        for product in order.products:
            print(f"{product.name}: ₹{product.price}")
        print(f"Total: ₹{total}")
