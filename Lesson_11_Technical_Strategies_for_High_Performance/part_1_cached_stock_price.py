from functools import lru_cache
import time

@lru_cache(maxsize=128)
def get_stock_price(symbol):
    # Simulating a time-consuming operation, like querying a database
    time.sleep(2)
    return f"Current price for {symbol}: ${random.uniform(100, 500):.2f}"

# Example calls
print(get_stock_price('AAPL'))  # This will take time
print(get_stock_price('AAPL'))  # This will be fast
print(get_stock_price('GOOG'))  # This will take time
print(get_stock_price('GOOG'))  # This will be fast
