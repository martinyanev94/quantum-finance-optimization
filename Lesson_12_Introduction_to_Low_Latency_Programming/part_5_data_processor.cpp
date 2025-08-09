#include <iostream>

void processData(int input) {
    if (input > 100) {
        std::cout << "High: " << input << std::endl;
    } else {
        std::cout << "Low: " << input << std::endl;
    }
}

int main() {
    for (int i = 0; i < 1000000; ++i) {
        processData(i);
    }
    return 0;
}
