class MovingAverage {
private:
    std::vector<double> prices;
    int period;

public:
    MovingAverage(int period) : period(period) {}

    void addPrice(double price) {
        prices.push_back(price);
        if (prices.size() > period) {
            prices.erase(prices.begin());
        }
    }

    double calculateSimpleMovingAverage() {
        double sum = 0;
        for (double price : prices) {
            sum += price;
        }
        return sum / prices.size();
    }
};

void executeTrade(double price, const std::string& action) {
    std::cout << "Executing " << action << " trade at price: $" << price << std::endl;
}

void tradingStrategy(RingBuffer& marketData, MovingAverage& shortMA, MovingAverage& longMA) {
    while (true) {
        try {
            double price = marketData.get();
            shortMA.addPrice(price);
            longMA.addPrice(price);

            double shortAvg = shortMA.calculateSimpleMovingAverage();
            double longAvg = longMA.calculateSimpleMovingAverage();

            if (shortAvg > longAvg) {
                executeTrade(price, "Buy");
            } else if (shortAvg < longAvg) {
                executeTrade(price, "Sell");
            }
        } catch (const std::out_of_range&) {
            continue; // Buffer is empty, simply skip
        }
    }
}
