#include <iostream>
#include <vector>
#include <algorithm>

class MarketDataProcessor {
private:
    std::vector<double> marketData;

public:
    void addData(double price) {
        marketData.push_back(price);
    }

    double calculateAverage() {
        double sum = std::accumulate(marketData.begin(), marketData.end(), 0.0);
        return sum / marketData.size();
    }

    void displayMarketConditions() {
        std::cout << "Current Average Price: $" << calculateAverage() << std::endl;
    }
};

int main() {
    MarketDataProcessor dataProcessor;
    dataProcessor.addData(150.55);
    dataProcessor.addData(152.30);
    dataProcessor.addData(151.85);
    dataProcessor.displayMarketConditions();
    return 0;
}
