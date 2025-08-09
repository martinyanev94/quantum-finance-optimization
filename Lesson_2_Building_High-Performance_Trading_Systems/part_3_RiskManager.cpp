class RiskManager {
private:
    double accountBalance;
    double riskFactor;

public:
    RiskManager(double balance, double risk) : accountBalance(balance), riskFactor(risk) {}

    double calculateTradeSize(double stopLoss) {
        return (accountBalance * riskFactor) / stopLoss;
    }
};
