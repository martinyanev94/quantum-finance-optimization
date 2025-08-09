#include <queue>
#include <iostream>

struct Order {
    int orderId;
    double price;
    std::string action; // "Buy" or "Sell"
};

class OrderBook {
private:
    std::queue<Order> pendingOrders;

public:
    void placeOrder(int id, double price, const std::string& action) {
        pendingOrders.push({id, price, action});
    }

    void executeOrder() {
        if (pendingOrders.empty()) {
            std::cout << "No orders to execute." << std::endl;
            return;
        }

        Order order = pendingOrders.front();
        pendingOrders.pop();
        std::cout << "Executing Order ID: " << order.orderId 
                  << " | Action: " << order.action 
                  << " | Price: $" << order.price << std::endl;
    }
};
