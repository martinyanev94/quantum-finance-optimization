#include <iostream>
#include <string>

class TradingAlgorithm {
public:
    void executeTrade(std::string stockSymbol, double price, int quantity) {
        std::cout << "Buying " << quantity << " shares of " << stockSymbol 
                  << " at $" << price << std::endl;
    }

    void evaluateMarketCondition(double currentPrice, double targetPrice) {
        if (currentPrice < targetPrice) {
            executeTrade("AAPL", currentPrice, 10);
        } else {
            std::cout << "Current price exceeds target price." << std::endl;
        }
    }
};

int main() {
    TradingAlgorithm algo;
    algo.evaluateMarketCondition(150.25, 155.00);
    return 0;
}
