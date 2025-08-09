import numpy as np

class TradingEnvironment:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.current_price = 100  # Initial stock price
        self.stock_owned = 0

    def buy_stock(self, amount):
        if amount <= self.balance:
            self.stock_owned += amount / self.current_price
            self.balance -= amount

    def sell_stock(self, amount):
        if self.stock_owned > 0:
            self.balance += amount * self.current_price
            self.stock_owned -= amount

    def step(self, action):
        # Simulate price movement
        self.current_price *= np.random.uniform(0.95, 1.05)
        if action == 0:  # Buy
            self.buy_stock(10)
        elif action == 1:  # Sell
            self.sell_stock(self.stock_owned)

        return self.balance, self.current_price, self.stock_owned

# Demonstrating the environment
env = TradingEnvironment(1000)

for _ in range(10):  # Simulate 10 trading steps
    action = np.random.choice([0, 1])  # Random action: 0 for buy, 1 for sell
    state = env.step(action)
    print(state)  # Print balance, current price, and stock owned
