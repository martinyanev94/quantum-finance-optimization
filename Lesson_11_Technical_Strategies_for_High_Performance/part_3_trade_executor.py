from concurrent.futures import ThreadPoolExecutor
import time

def execute_trade(order):
    time.sleep(1)  # Simulating trade execution time
    return f"Executed trade: {order}"

orders = ["Buy AAPL", "Sell GOOG", "Buy TSLA", "Sell AMZN"]

with ThreadPoolExecutor(max_workers=2) as executor:
    results = list(executor.map(execute_trade, orders))

for result in results:
    print(result)
