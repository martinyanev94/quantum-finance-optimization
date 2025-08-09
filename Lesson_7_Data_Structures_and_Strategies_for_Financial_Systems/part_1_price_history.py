class PriceHistory:
    def __init__(self, size):
        self.size = size
        self.prices = [0] * size
        self.index = 0

    def add_price(self, price):
        self.prices[self.index % self.size] = price
        self.index += 1

    def get_history(self):
        return self.prices
