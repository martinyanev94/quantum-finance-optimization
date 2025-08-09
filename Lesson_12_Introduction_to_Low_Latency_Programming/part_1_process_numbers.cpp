#include <iostream>

void processInteger(int n) {
    // Simple integer processing
    int result = n * n;
    std::cout << "Processed Integer: " << result << std::endl;
}

void processFloat(float f) {
    // Simple float processing
    float result = f * f;
    std::cout << "Processed Float: " << result << std::endl;
}

int main() {
    processInteger(10);
    processFloat(10.5);
    return 0;
}
