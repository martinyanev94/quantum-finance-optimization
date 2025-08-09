class TradingStrategy:
    def execute(self):
        raise NotImplementedError

class MarketOrderStrategy(TradingStrategy):
    def execute(self):
        return "Executing market order!"

class LimitOrderStrategy(TradingStrategy):
    def execute(self):
        return "Executing limit order!"

class StrategyFactory:
    @staticmethod
    def create_strategy(strategy_type):
        if strategy_type == "market":
            return MarketOrderStrategy()
        elif strategy_type == "limit":
            return LimitOrderStrategy()
        else:
            raise ValueError("Unknown strategy type.")
