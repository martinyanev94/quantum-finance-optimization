class MarketDataPublisher:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def publish_data(self, data):
        for subscriber in self.subscribers:
            subscriber.update(data)

class MarketDataSubscriber:
    def update(self, data):
        print(f"Received market data update: {data}")

# Example usage
publisher = MarketDataPublisher()
subscriber1 = MarketDataSubscriber()
subscriber2 = MarketDataSubscriber()

publisher.subscribe(subscriber1)
publisher.subscribe(subscriber2)

# Publishing market data
publisher.publish_data("Market Update: AAPL prices up by 5%")
