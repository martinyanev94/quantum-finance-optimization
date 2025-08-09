class TradingStrategy:
    def execute(self):
        return "Executing basic trading strategy."

class StrategyDecorator:
    def __init__(self, strategy: TradingStrategy):
        self._strategy = strategy

    def execute(self):
        return self._strategy.execute()

class LoggingDecorator(StrategyDecorator):
    def execute(self):
        result = self._strategy.execute()
        return f"{result} with logging enabled."

class RiskManagementDecorator(StrategyDecorator):
    def execute(self):
        result = self._strategy.execute()
        return f"{result} with risk management applied."

# Example usage
base_strategy = TradingStrategy()
logging_strategy = LoggingDecorator(base_strategy)
risk_management_strategy = RiskManagementDecorator(logging_strategy)
print(risk_management_strategy.execute())
