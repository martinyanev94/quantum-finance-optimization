class LegacyTradingAPI:
    def place_order(self, stock, quantity):
        return f"Order placed for {quantity} shares of {stock}."

class ModernTradingAPI:
    def send_order(self, order_details):
        return f"Sending order: {order_details}"

class TradingAdapter:
    def __init__(self, legacy_api: LegacyTradingAPI):
        self.legacy_api = legacy_api

    def place_order(self, stock, quantity):
        return self.legacy_api.place_order(stock, quantity)

# Example usage
legacy_api = LegacyTradingAPI()
adapter = TradingAdapter(legacy_api)
print(adapter.place_order("TSLA", 10))
