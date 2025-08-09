class TradeExecutionStrategy:
    def execute(self):
        raise NotImplementedError

class BestPriceExecution(TradeExecutionStrategy):
    def execute(self):
        return "Executing trade at the best market price."

class IcebergOrderExecution(TradeExecutionStrategy):
    def execute(self):
        return "Executing trade using an iceberg order method."

class TradeContext:
    def __init__(self, strategy: TradeExecutionStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: TradeExecutionStrategy):
        self._strategy = strategy

    def execute_trade(self):
        return self._strategy.execute()

# Example usage
trade_context = TradeContext(BestPriceExecution())
print(trade_context.execute_trade())

trade_context.set_strategy(IcebergOrderExecution())
print(trade_context.execute_trade())
