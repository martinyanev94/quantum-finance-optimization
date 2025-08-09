class Order:
    def __init__(self, order_id, amount):
        self.order_id = order_id
        self.amount = amount

class OrderBook:
    def __init__(self):
        self.orders = {}

    def add_order(self, order_id, amount):
        self.orders[order_id] = Order(order_id, amount)

    def get_order(self, order_id):
        return self.orders.get(order_id, "Order not found")
