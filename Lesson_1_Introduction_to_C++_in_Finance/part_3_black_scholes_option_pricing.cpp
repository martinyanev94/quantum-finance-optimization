#include <ql/quantlib.hpp>
using namespace QuantLib;

int main() {
    Date today(15, 3, 2021);
    Settings::instance().evaluationDate() = today;

    Option::Type optionType = Option::Call;
    Real strikePrice = 100.0;
    Real underlyingPrice = 105.0;
    Real volatility = 0.2;
    Rate riskFreeRate = 0.05;
    Date expiryDate(15, 3, 2022);

    EuropeanOption option(optionType, strikePrice);
    BlackScholesProcess bsm(Handle<Quote>(boost::make_shared<SimpleQuote>(underlyingPrice)),
                             Handle<YieldTermStructure>(boost::make_shared<FlatForward>(today, Handle<Quote>(boost::make_shared<SimpleQuote>(riskFreeRate)), Actual360())),
                             Handle<BlackVolTermStructure>(boost::make_shared<BlackConstantVol>(today, TARGET(), Handle<Quote>(boost::make_shared<SimpleQuote>(volatility)), Actual360())));

    Real optionPrice = option.NPV(bsm);
    std::cout << "Option Price: $" << optionPrice << std::endl;

    return 0;
}
