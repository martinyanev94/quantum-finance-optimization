class TradeQueue:
    def __init__(self):
        self.trades = []

    def enqueue(self, trade):
        self.trades.append(trade)

    def dequeue(self):
        if self.trades:
            return self.trades.pop(0)
        return "No trades"

    def peek(self):
        return self.trades[0] if self.trades else "No trades"
