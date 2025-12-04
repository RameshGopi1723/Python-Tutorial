class OrderCalculator:
    def calculate_total(self, order: Order, customer_type: str) -> float:
        total = sum(product.price for product in order.products)
        
        if customer_type == "vip":
            total *= 0.9
        elif customer_type == "coupon":
            total -= 100
        
        return total
