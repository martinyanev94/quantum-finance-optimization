class LiquidityPool:
    def __init__(self):
        self.pool = {}

    def add_liquidity(self, token, amount):
        self.pool[token] = self.pool.get(token, 0) + amount

    def remove_liquidity(self, token, amount):
        if token in self.pool and self.pool[token] >= amount:
            self.pool[token] -= amount
            return True
        return False
