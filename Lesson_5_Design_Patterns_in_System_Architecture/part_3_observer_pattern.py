class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, data):
        for observer in self._observers:
            observer.update(data)

class TradingStrategy(Observer):
    def update(self, data):
        print(f"Trading strategy updated with data: {data}")

# Example usage
subject = Subject()
strategy = TradingStrategy()
subject.attach(strategy)

# Simulating market data change
subject.notify("Market price updated to $123.45")
