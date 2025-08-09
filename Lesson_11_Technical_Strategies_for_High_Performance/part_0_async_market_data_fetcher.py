import asyncio
import random

async def fetch_market_data(symbol):
    await asyncio.sleep(random.uniform(0.1, 1))  # Simulating network delay
    return f"Market data for {symbol}"

async def process_data(symbols):
    tasks = [fetch_market_data(symbol) for symbol in symbols]
    market_data = await asyncio.gather(*tasks)
    return market_data

# Example run
symbols = ["AAPL", "GOOG", "TSLA", "AMZN"]
async def main():
    data = await process_data(symbols)
    for item in data:
        print(item)

asyncio.run(main())
